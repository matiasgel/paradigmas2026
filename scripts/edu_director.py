#!/usr/bin/env python3
"""
edu_director.py — Pipeline Orchestrator Minimalista (S12.1)
============================================================
Orquesta todo el pipeline de producción de un tema con un solo comando,
usando checkpoints persistentes para reanudación.

Uso:
    python scripts/edu_director.py --topic 05-sorting --course leng-2026
    python scripts/edu_director.py --resume --topic 05-sorting --course leng-2026
    python scripts/edu_director.py --topic 05-sorting --course leng-2026 --skip-gates --dry-run

Pasos del pipeline:
    1. validate_plan
    2. fact_check (S9.3, si habilitado)
    3. slides_pipeline
    4. capture_thumbnails
    5. visual_quality (S10.3, si habilitado)
    6. [HUMAN GATE]
    7. semantic_drift (S9.1, si habilitado)
    8. bloom_classify (S10.1, si habilitado)
    9. [FINAL GATE]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

_this = Path(__file__).resolve()
_scripts = _this.parent
_root = _scripts.parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from pipeline_common import find_project_root, load_config, load_json, save_json


# ═══════════════════════════════════════════════════════════════════════
# PIPELINE STATE
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class StepResult:
    name: str
    status: str  # "success" | "skipped" | "failed" | "pending"
    duration_s: float = 0.0
    message: str = ""


@dataclass
class PipelineState:
    topic: str
    course: str
    current_step: int = 0
    steps: list[dict] = field(default_factory=list)
    started_at: str = ""
    completed: bool = False

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        save_json(path, asdict(self))

    @classmethod
    def load(cls, path: Path) -> PipelineState:
        data = load_json(path)
        return cls(**data)


# ═══════════════════════════════════════════════════════════════════════
# PIPELINE STEPS
# ═══════════════════════════════════════════════════════════════════════

def _run_script(
    script_name: str,
    args: list[str],
    *,
    timeout: int = 300,
    dry_run: bool = False,
) -> StepResult:
    """Ejecuta un script Python como subprocess."""
    script_path = _scripts / script_name
    if not script_path.exists():
        return StepResult(
            name=script_name,
            status="skipped",
            message=f"Script no encontrado: {script_name}",
        )

    if dry_run:
        return StepResult(
            name=script_name,
            status="skipped",
            message=f"[dry-run] Se ejecutaría: python {script_name} {' '.join(args)}",
        )

    cmd = [sys.executable, str(script_path), *args]
    t0 = time.monotonic()
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(_root),
        )
        elapsed = time.monotonic() - t0
        if result.returncode == 0:
            return StepResult(
                name=script_name,
                status="success",
                duration_s=round(elapsed, 2),
                message=result.stdout[:500] if result.stdout else "OK",
            )
        else:
            return StepResult(
                name=script_name,
                status="failed",
                duration_s=round(elapsed, 2),
                message=result.stderr[:500] if result.stderr else f"Exit code {result.returncode}",
            )
    except subprocess.TimeoutExpired:
        return StepResult(
            name=script_name,
            status="failed",
            duration_s=timeout,
            message=f"Timeout after {timeout}s",
        )


def _human_gate(prompt_msg: str, *, skip_gates: bool = False) -> StepResult:
    """Gate humano interactivo."""
    if skip_gates:
        return StepResult(name="human_gate", status="skipped", message="--skip-gates")
    try:
        resp = input(f"\n🔒 {prompt_msg} [Enter para continuar / 'n' para cancelar]: ").strip()
        if resp.lower() == "n":
            return StepResult(name="human_gate", status="failed", message="Cancelado por docente")
        return StepResult(name="human_gate", status="success", message="Aprobado")
    except (EOFError, KeyboardInterrupt):
        return StepResult(name="human_gate", status="failed", message="Interrumpido")


# ═══════════════════════════════════════════════════════════════════════
# MAIN PIPELINE
# ═══════════════════════════════════════════════════════════════════════

def build_pipeline(
    topic: str,
    course: str,
    config: dict,
    *,
    skip_gates: bool = False,
    dry_run: bool = False,
    skip_steps: set[str] | None = None,
) -> list[tuple[str, callable]]:
    """Construye la lista de pasos del pipeline."""
    _skip = skip_steps or set()
    base_args = ["--topic", topic, "--course", course]

    steps: list[tuple[str, callable]] = []

    # 1. validate_plan
    steps.append(("validate_plan", lambda: _run_script(
        "validate_plan.py", base_args, dry_run=dry_run,
    )))

    # 2. fact_check (opcional)
    if config.get("fact_check_enabled", False) and "fact_check" not in _skip:
        steps.append(("fact_check", lambda: _run_script(
            "fact_verifier.py", base_args, dry_run=dry_run,
        )))

    # 3. slides_pipeline
    steps.append(("slides_pipeline", lambda: _run_script(
        "slides_pipeline.py", base_args, dry_run=dry_run, timeout=600,
    )))

    # 4. capture_thumbnails
    steps.append(("capture_thumbnails", lambda: _run_script(
        "capture_thumbnails.py", base_args, dry_run=dry_run,
    )))

    # 5. visual_quality (opcional)
    if config.get("visual_quality_enabled", False) and "visual_quality" not in _skip:
        steps.append(("visual_quality", lambda: _run_script(
            "slide_quality_vision.py", base_args, dry_run=dry_run,
        )))

    # 6. Human gate
    steps.append(("review_gate", lambda: _human_gate(
        "Revisar output generado y presionar Enter...",
        skip_gates=skip_gates,
    )))

    # 7. semantic_drift (opcional)
    if config.get("semantic_drift_enabled", False) and "semantic_drift" not in _skip:
        steps.append(("semantic_drift", lambda: _run_script(
            "semantic_drift_detector.py", base_args, dry_run=dry_run,
        )))

    # 8. bloom_classify (opcional)
    if config.get("bloom_classifier_enabled", False) and "bloom_classify" not in _skip:
        steps.append(("bloom_classify", lambda: _run_script(
            "bloom_classifier.py", base_args, dry_run=dry_run,
        )))

    # 9. Final gate
    steps.append(("final_gate", lambda: _human_gate(
        "¿Publicar? (Enter = sí, 'n' = no)",
        skip_gates=skip_gates,
    )))

    return steps


def run_pipeline(
    topic: str,
    course: str,
    *,
    resume: bool = False,
    skip_gates: bool = False,
    dry_run: bool = False,
    skip_steps: set[str] | None = None,
) -> int:
    """Ejecuta el pipeline completo con checkpoints."""
    project_root = find_project_root(Path.cwd())
    config = load_config(project_root)

    if not config.get("orchestrator_enabled", False):
        print("ℹ️  orchestrator_enabled no está habilitado en config. Saliendo.")
        return 0

    topic_folder = project_root / "salida" / "cursadas" / course / topic
    state_path = topic_folder / ".pipeline-state.json"

    # Resume from checkpoint
    start_step = 0
    if resume and state_path.exists():
        state = PipelineState.load(state_path)
        start_step = state.current_step
        print(f"🔄 Reanudando pipeline desde paso {start_step + 1}")

    steps = build_pipeline(
        topic, course, config,
        skip_gates=skip_gates, dry_run=dry_run, skip_steps=skip_steps,
    )

    state = PipelineState(
        topic=topic,
        course=course,
        current_step=start_step,
        started_at=time.strftime("%Y-%m-%dT%H:%M:%S"),
    )

    print(f"\n🚀 EDU Pipeline — {topic} ({course})")
    print(f"   Pasos: {len(steps)} | Inicio desde: {start_step + 1}\n")

    for i, (step_name, step_fn) in enumerate(steps):
        if i < start_step:
            continue

        print(f"  [{i+1}/{len(steps)}] {step_name}...", end=" ", flush=True)
        result = step_fn()
        print(f"→ {result.status}" + (f" ({result.duration_s}s)" if result.duration_s else ""))

        state.steps.append(asdict(result))
        state.current_step = i + 1
        state.save(state_path)

        if result.status == "failed":
            print(f"\n❌ Pipeline detenido en paso '{step_name}': {result.message}")
            print(f"   Reanudar con: python scripts/edu_director.py --resume --topic {topic} --course {course}")
            return 1

    state.completed = True
    state.save(state_path)
    print(f"\n✅ Pipeline completado exitosamente.")
    return 0


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(description="EDU Pipeline Director (S12.1)")
    parser.add_argument("--topic", required=True, help="ID del tema")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument("--resume", action="store_true", help="Reanudar desde checkpoint")
    parser.add_argument("--skip-gates", action="store_true", help="Saltar gates humanos (CI/CD)")
    parser.add_argument("--dry-run", action="store_true", help="Simular sin ejecutar")
    parser.add_argument("--skip-steps", type=str, default="", help="Pasos a omitir (comma-separated)")
    args = parser.parse_args()

    skip = set(args.skip_steps.split(",")) if args.skip_steps else set()
    return run_pipeline(
        args.topic,
        args.course,
        resume=args.resume,
        skip_gates=args.skip_gates,
        dry_run=args.dry_run,
        skip_steps=skip,
    )


if __name__ == "__main__":
    raise SystemExit(main())
