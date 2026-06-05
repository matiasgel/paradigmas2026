#!/usr/bin/env python3
"""
publish_loop.py â€” Loop de publicaciÃ³n con prueba de coherencia de esquema (v1)
================================================================================
Orquesta el ciclo completo:

    FASE 1 â€” VALIDACIÃ“N ESTRUCTURAL (schema contract)
        repair_plan.py --attempt N
        â†’ exit 0: plan vÃ¡lido â†’ continuar
        â†’ exit 1: errores schema â†’ agente corrige â†’ reintentar
        â†’ exit 2: max intentos â†’ STOP humano

    FASE 2 â€” COHERENCIA DEL ESQUEMA (antes de publicar)
        2a. validate_plan.py         â†’ contrato JSON Schema v3
        2b. validate_accessibility.py â†’ WCAG AA contraste/tipografÃ­a/alt_text
        2c. validate_layout_cognition.py â†’ reglas cognitivas (Mayer/Garner)
        2d. validate_slide_composition.py â†’ mÃ¡rgenes, densidad visual
        2e. fact_verifier.py          â†’ verificaciÃ³n factual NLI (si habilitado)
        2f. semantic_drift_detector.py â†’ coherencia inter-clases (si habilitado)

    FASE 3 â€” PUBLICACIÃ“N (solo si FASE 2 pasa)
        slides_pipeline.py

    FASE 4 â€” POST-PUBLICACIÃ“N
        capture_thumbnails.py (si habilitado)
        â†’ Escribe resultado en memory.db

Uso:
    python scripts/publish_loop.py <topic_folder>
    python scripts/publish_loop.py <topic_folder> --course leng-2026
    python scripts/publish_loop.py <topic_folder> --dry-run     # validar, no publicar
    python scripts/publish_loop.py <topic_folder> --skip-phase2  # solo schema + publicar
    python scripts/publish_loop.py <topic_folder> --skip-facts   # omitir fact_verifier
    python scripts/publish_loop.py <topic_folder> --max-attempts 5

Exit codes:
    0 â€” publicaciÃ³n exitosa
    1 â€” errores de validaciÃ³n (se muestra reporte)
    2 â€” max intentos de reparaciÃ³n superados â†’ revisiÃ³n humana
    3 â€” FASE 2 fallÃ³: coherencia bloqueada
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

_this = Path(__file__).resolve()
_scripts = _this.parent
_root = _scripts.parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from pipeline_common import find_project_root, find_plan, load_yaml, save_json

# Registro de errores â€” importaciÃ³n tolerante a fallo (no bloquea el pipeline)
try:
    from error_registry import ErrorRegistry as _ErrorRegistry
    _registry = _ErrorRegistry()
except Exception:  # noqa: BLE001
    _registry = None  # type: ignore[assignment]


def _record_error(
    phase: str,
    error_type: str,
    description: str,
    topic: str = "",
    course: str = "",
    root_cause: str = "",
    context: dict | None = None,
) -> None:
    """Registra un error en el registro persistente (silencioso si falla)."""
    if _registry is None:
        return
    try:
        eid = _registry.record(
            phase=phase,
            error_type=error_type,
            description=description,
            topic=topic,
            course=course,
            root_cause=root_cause,
            context=context,
        )
        print(f"  ðŸ“‹ Error registrado en error-registry.jsonl (ID: {eid[:8]}...)")
        print(f"     Consultar reglas: python scripts/error_registry.py rules --phase {phase}")
    except Exception as exc:  # noqa: BLE001
        print(f"  âš ï¸  No se pudo registrar en error-registry.jsonl: {exc}", file=sys.stderr)


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Helpers
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def _run(cmd: list[str], label: str) -> tuple[int, str]:
    """Ejecuta un comando y retorna (exit_code, stdout+stderr)."""
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output


def _print_section(title: str) -> None:
    width = 72
    print(f"\n{'â•' * width}")
    print(f"  {title}")
    print(f"{'â•' * width}")


def _status(ok: bool, label: str, detail: str = "") -> None:
    icon = "âœ…" if ok else "âŒ"
    detail_str = f" â€” {detail}" if detail else ""
    print(f"  {icon} {label}{detail_str}")


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# Fases
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def phase0_consult_registry(topic_folder: Path, course_id: str) -> None:
    """
    FASE 0: Consulta obligatoria del registro de errores antes de iniciar.
    Muestra las reglas de prevenciÃ³n relevantes para el tema y las globales.
    No bloquea la ejecuciÃ³n â€” es informativa.
    """
    _print_section("FASE 0 â€” Consulta del registro de errores (obligatoria)")

    if _registry is None:
        print("  âš ï¸  error_registry.py no disponible â€” omitiendo consulta")
        return

    topic_name = topic_folder.name

    # Errores anteriores para este tema especÃ­fico
    topic_errors = _registry.query(topic=topic_name, status="open")
    if topic_errors:
        print(f"  âš ï¸  {len(topic_errors)} error(es) ABIERTO(S) previos para '{topic_name}':")
        for e in topic_errors[-5:]:  # Ãºltimos 5
            ts = (e.get("timestamp") or "?")[:10]
            print(f"     [{ts}] {e.get('phase')} / {e.get('error_type')}: "
                  f"{(e.get('description') or '')[:80]}")
        print()

    # Reglas de prevenciÃ³n para las fases del pipeline
    rules = _registry.get_prevention_rules()
    pipeline_rules = [r for r in rules if r["phase"] in ("FASE1", "FASE2", "FASE3")]

    if pipeline_rules:
        print(f"  ðŸ“‹ {len(pipeline_rules)} regla(s) de prevenciÃ³n activas para este pipeline:")
        for r in pipeline_rules[:6]:  # mostrar hasta 6
            print(f"     [{r['phase']} / {r['error_type']}]")
            # Primera oraciÃ³n de la regla
            first_sentence = (r.get("rule") or "").split(".")[0][:100]
            if first_sentence:
                print(f"     â†’ {first_sentence}.")
        if len(pipeline_rules) > 6:
            print(f"     ... y {len(pipeline_rules) - 6} mÃ¡s. "
                  f"Ver: python scripts/error_registry.py rules")
    else:
        print("  âœ… Sin errores previos registrados. Primera publicaciÃ³n de este pipeline.")

    print(f"\n  Para consulta completa: python scripts/error_registry.py rules")
    print(f"  Para historial del tema: python scripts/error_registry.py query --topic {topic_name}")


def phase1_repair_loop(
    topic_folder: Path,
    python: str,
    max_attempts: int,
) -> int:
    """
    Ejecuta repair_plan.py en loop hasta que el plan sea vÃ¡lido o se agoten los intentos.
    El agente (Diego) corrige el plan entre intentos cuando se corre en modo agente.
    Retorna el exit code final (0=ok, 1=errores, 2=max_attempts).
    """
    _print_section("FASE 1 â€” ValidaciÃ³n estructural del plan (schema v3)")

    repair_script = _scripts / "repair_plan.py"
    if not repair_script.exists():
        print(f"  âŒ repair_plan.py no encontrado en {_scripts}", file=sys.stderr)
        return 1

    for attempt in range(1, max_attempts + 1):
        print(f"\n  Intento {attempt}/{max_attempts}:")
        code, output = _run(
            [python, str(repair_script), str(topic_folder), "--attempt", str(attempt)],
            f"repair_plan attempt={attempt}",
        )
        # Mostrar output relevante
        for line in output.strip().splitlines():
            print(f"    {line}")

        if code == 0:
            _status(True, f"Plan vÃ¡lido en intento {attempt}")
            return 0
        elif code == 2:
            _status(False, f"MÃ¡x intentos superados â€” revisiÃ³n humana requerida")
            return 2
        else:
            _status(False, f"Intento {attempt}: errores encontrados")
            if attempt < max_attempts:
                print(f"\n  âš ï¸  El agente debe corregir SOLO los campos reportados arriba.")
                print(f"     Luego retomar con: python scripts/publish_loop.py {topic_folder}")
                # En modo automÃ¡tico el agente puede iterar; en modo CLI retornamos para que corrija
                return 1

    return 2


def phase2_coherence_checks(
    topic_folder: Path,
    python: str,
    course_id: str,
    skip_facts: bool,
    skip_drift: bool,
) -> tuple[bool, list[dict]]:
    """
    Ejecuta todos los validadores de coherencia.
    Retorna (all_passed: bool, results: list[dict]) con detalle por check.
    """
    _print_section("FASE 2 â€” Coherencia del esquema (pre-publicaciÃ³n)")

    checks = [
        {
            "id": "schema-contract",
            "label": "Contrato JSON Schema v3",
            "script": "validate_plan.py",
            "args": [str(topic_folder)],
            "blocking": True,
        },
        {
            "id": "accessibility",
            "label": "Accesibilidad WCAG AA (contraste, tipografÃ­a, alt_text)",
            "script": "validate_accessibility.py",
            "args": ["--topic", topic_folder.name, "--course", course_id],
            "blocking": False,  # warning, no bloquea
        },
        {
            "id": "layout-cognition",
            "label": "Reglas cognitivas (Mayer/Garner: assertion-evidence, densidad)",
            "script": "validate_layout_cognition.py",
            "args": ["--topic", topic_folder.name, "--course", course_id],
            "blocking": False,
        },
        {
            "id": "composition",
            "label": "ComposiciÃ³n visual (mÃ¡rgenes, densidad 35-55%, superposiciones)",
            "script": "validate_slide_composition.py",
            "args": ["--topic", topic_folder.name, "--course", course_id],
            "blocking": False,
        },
    ]

    if not skip_facts:
        checks.append({
            "id": "fact-check",
            "label": "VerificaciÃ³n factual NLI (ChromaDB evidence)",
            "script": "fact_verifier.py",
            "args": ["--topic", topic_folder.name, "--course", course_id],
            "blocking": False,
        })

    if not skip_drift:
        checks.append({
            "id": "semantic-drift",
            "label": "Coherencia semÃ¡ntica inter-clases (MiniLM drift detector)",
            "script": "semantic_drift_detector.py",
            "args": ["--course", course_id],
            "blocking": False,
        })

    results: list[dict] = []
    all_blocking_passed = True

    for check in checks:
        script_path = _scripts / check["script"]
        if not script_path.exists():
            results.append({**check, "code": -1, "output": "script no encontrado", "passed": False})
            _status(False, check["label"], "script no encontrado â€” omitido")
            continue

        code, output = _run(
            [python, str(script_path)] + check["args"],
            check["label"],
        )
        passed = (code == 0)
        results.append({**check, "code": code, "output": output, "passed": passed})

        if passed:
            _status(True, check["label"])
        else:
            _status(False, check["label"], "BLOQUEA" if check["blocking"] else "advertencia")
            # Mostrar las primeras lÃ­neas del output de error
            lines = [l for l in output.strip().splitlines() if l.strip()][:8]
            for line in lines:
                print(f"    {line}")
            if check["blocking"]:
                all_blocking_passed = False

    # Mostrar resumen de advertencias (non-blocking)
    warnings = [r for r in results if not r["passed"] and not r.get("blocking", False)]
    if warnings:
        print(f"\n  âš ï¸  {len(warnings)} advertencia(s) no bloqueantes â€” pueden publicarse con precauciÃ³n:")
        for w in warnings:
            print(f"     â€¢ {w['label']}")

    return all_blocking_passed, results


def phase3_publish(
    topic_folder: Path,
    python: str,
    dry_run: bool,
) -> int:
    """Ejecuta slides_pipeline.py para publicar en Google Slides."""
    if dry_run:
        _print_section("FASE 3 â€” PublicaciÃ³n [DRY-RUN â€” omitida]")
        print("  â„¹ï¸  Modo --dry-run: pipeline no ejecutado. El plan es vÃ¡lido.")
        return 0

    _print_section("FASE 3 â€” PublicaciÃ³n â†’ Google Slides")
    pipeline = _scripts / "slides_pipeline.py"
    if not pipeline.exists():
        print(f"  âŒ slides_pipeline.py no encontrado en {_scripts}", file=sys.stderr)
        return 1

    print(f"  Ejecutando slides_pipeline.py para: {topic_folder.name}")
    code, output = _run([python, str(pipeline), str(topic_folder)], "slides_pipeline")

    for line in output.strip().splitlines():
        print(f"  {line}")

    if code == 0:
        _status(True, "Pipeline completado â€” presentaciÃ³n publicada en Google Slides")
        url_file = topic_folder / "slides" / "slides-url.txt"
        if url_file.exists():
            print(f"\n  ðŸ”— URL: {url_file.read_text(encoding='utf-8').strip()}")
    else:
        _status(False, "Pipeline fallÃ³")

    return code


def phase4_post(
    topic_folder: Path,
    python: str,
    course_id: str,
    coherence_results: list[dict],
    publish_code: int,
) -> None:
    """Captura thumbnails y escribe resultado en memory.db."""
    _print_section("FASE 4 â€” Post-publicaciÃ³n")

    # Intentar capture_thumbnails
    url_file = topic_folder / "slides" / "slides-url.txt"
    thumbs_script = _scripts / "capture_thumbnails.py"
    if publish_code == 0 and url_file.exists() and thumbs_script.exists():
        pres_id = _extract_presentation_id(url_file.read_text(encoding="utf-8").strip())
        if pres_id:
            thumbs_dir = topic_folder / "slides" / "thumbnails"
            thumbs_dir.mkdir(parents=True, exist_ok=True)
            code, _ = _run(
                [python, str(thumbs_script), pres_id, str(thumbs_dir)],
                "capture_thumbnails",
            )
            _status(code == 0, "Thumbnails capturados", str(thumbs_dir) if code == 0 else "fallÃ³")

    # Escribir reporte de coherencia en slides/
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topic": topic_folder.name,
        "course_id": course_id,
        "publish_success": publish_code == 0,
        "coherence_checks": [
            {
                "id": r["id"],
                "label": r["label"],
                "passed": r["passed"],
                "blocking": r.get("blocking", False),
                "exit_code": r.get("code", -1),
            }
            for r in coherence_results
        ],
        "all_blocking_passed": all(
            r["passed"] for r in coherence_results if r.get("blocking", False)
        ),
    }

    report_path = topic_folder / "slides" / "publish-report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    save_json(report_path, report)
    _status(True, f"Reporte guardado: {report_path.relative_to(find_project_root(Path(__file__)))}")

    # Escribir en memory.db si estÃ¡ disponible
    memory_script = _scripts / "edu_memory.py"
    if memory_script.exists():
        checks_summary = ", ".join(
            f"{r['id']}={'âœ“' if r['passed'] else 'âœ—'}" for r in coherence_results
        )
        category = "publish-success" if publish_code == 0 else "publish-failure"
        note = (
            f"publish_loop: {category} â€” coherencia: [{checks_summary}]"
        )
        _run(
            [python, str(memory_script), "add",
             "--course", course_id,
             "--category", category,
             "--topic", topic_folder.name,
             "--note", note],
            "edu_memory",
        )
        _status(True, "Resultado registrado en memory.db")


def _extract_presentation_id(url: str) -> str | None:
    """Extrae el ID de presentaciÃ³n de una URL de Google Slides."""
    import re
    m = re.search(r"/presentation/d/([a-zA-Z0-9_-]+)", url)
    return m.group(1) if m else None


# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# CLI
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def main() -> None:
    parser = argparse.ArgumentParser(
        description="publish_loop.py â€” Loop de publicaciÃ³n con prueba de coherencia de esquema",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("topic_folder", help="Ruta al directorio del tema")
    parser.add_argument("--course", default=None, help="ID del curso (ej: leng-2026)")
    parser.add_argument("--max-attempts", type=int, default=3,
                        help="MÃ¡x intentos de reparaciÃ³n de schema (default: 3)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Validar y probar coherencia sin publicar en Google Slides")
    parser.add_argument("--skip-phase2", action="store_true",
                        help="Omitir FASE 2 (coherencia) â€” solo reparar schema y publicar")
    parser.add_argument("--skip-facts", action="store_true",
                        help="Omitir fact_verifier.py (mÃ¡s lento, requiere ChromaDB)")
    parser.add_argument("--skip-drift", action="store_true",
                        help="Omitir semantic_drift_detector.py")
    parser.add_argument("--python", default=sys.executable,
                        help="IntÃ©rprete Python a usar (default: sys.executable)")

    args = parser.parse_args()
    topic_folder = Path(args.topic_folder).resolve()

    if not topic_folder.exists():
        print(f"âŒ No existe: {topic_folder}", file=sys.stderr)
        sys.exit(1)

    # Determinar course_id
    course_id = args.course
    if not course_id:
        root = find_project_root(Path(__file__))
        try:
            cfg = load_yaml(root / "_edu" / "config.yaml").value
            prefix = cfg.get("course_prefix", "edu")
            year = cfg.get("course_year", "2026")
            course_id = f"{prefix}-{year}"
        except Exception:
            course_id = "edu-2026"

    print(f"\nðŸ”„ publish_loop â€” Tema: {topic_folder.name}  |  Curso: {course_id}")
    print(f"   Modo: {'DRY-RUN' if args.dry_run else 'PUBLICAR'}  |  "
          f"MÃ¡x intentos reparaciÃ³n: {args.max_attempts}")

    # â”€â”€ FASE 0: consulta obligatoria del registro de errores â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    phase0_consult_registry(topic_folder, course_id)

    # â”€â”€ FASE 1: repair loop â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    code = phase1_repair_loop(topic_folder, args.python, args.max_attempts)
    if code != 0:
        err_type = "repair_exhausted" if code == 2 else "schema_violation"
        err_desc = (
            f"repair_plan agotÃ³ {args.max_attempts} intentos sin plan vÃ¡lido"
            if code == 2
            else f"repair_plan reportÃ³ errores de schema (exit {code})"
        )
        _record_error(
            phase="FASE1",
            error_type=err_type,
            description=err_desc,
            topic=topic_folder.name,
            course=course_id,
            context={"exit_code": code, "max_attempts": args.max_attempts},
        )
        print(f"\nðŸ›‘ FASE 1 fallÃ³ (exit {code}). Corregir plan antes de continuar.", file=sys.stderr)
        print(f"   âœ… Error registrado. Ver: python scripts/error_registry.py query --topic {topic_folder.name}",
              file=sys.stderr)
        sys.exit(code)

    # â”€â”€ FASE 2: coherence checks â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    coherence_results: list[dict] = []
    if not args.skip_phase2:
        all_ok, coherence_results = phase2_coherence_checks(
            topic_folder, args.python, course_id,
            skip_facts=args.skip_facts,
            skip_drift=args.skip_drift,
        )
        if not all_ok:
            # Registrar cada check bloqueante que fallÃ³
            for r in coherence_results:
                if not r.get("passed") and r.get("blocking"):
                    _type_map = {
                        "schema-contract": "schema_violation",
                        "accessibility": "accessibility",
                        "layout-cognition": "layout_cognition",
                        "composition": "composition",
                        "fact-check": "fact_check",
                        "semantic-drift": "semantic_drift",
                    }
                    etype = _type_map.get(r.get("id", ""), "other")
                    _record_error(
                        phase="FASE2",
                        error_type=etype,
                        description=f"{r.get('label', r.get('id'))} fallÃ³ (exit {r.get('code', -1)})",
                        topic=topic_folder.name,
                        course=course_id,
                        context={
                            "check_id": r.get("id"),
                            "exit_code": r.get("code"),
                            "output_excerpt": (r.get("output") or "")[:500],
                        },
                    )
            print(f"\nðŸ›‘ FASE 2 bloqueÃ³ la publicaciÃ³n â€” corregir errores marcados con âŒ BLOQUEA.",
                  file=sys.stderr)
            print(f"   âœ… Errores registrados. Ver: python scripts/error_registry.py query --topic {topic_folder.name}",
                  file=sys.stderr)
            # Igual escribir el reporte
            phase4_post(topic_folder, args.python, course_id, coherence_results, publish_code=3)
            sys.exit(3)
    else:
        print("\n  âš ï¸  FASE 2 omitida (--skip-phase2)")

    # â”€â”€ FASE 3: publicar â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    publish_code = phase3_publish(topic_folder, args.python, args.dry_run)
    if publish_code != 0 and not args.dry_run:
        _record_error(
            phase="FASE3",
            error_type="pipeline",
            description=f"slides_pipeline.py fallÃ³ con exit code {publish_code}",
            topic=topic_folder.name,
            course=course_id,
            context={"exit_code": publish_code},
        )
        print(f"   âœ… Error de pipeline registrado. Ver: python scripts/error_registry.py query --phase FASE3",
              file=sys.stderr)

    # â”€â”€ FASE 4: post-publicaciÃ³n â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    phase4_post(topic_folder, args.python, course_id, coherence_results, publish_code)

    # Resumen final
    _print_section("RESUMEN FINAL")
    _status(publish_code == 0, "PublicaciÃ³n",
            "completada" if publish_code == 0 else f"exit code {publish_code}")
    if not args.dry_run and publish_code == 0:
        url_file = topic_folder / "slides" / "slides-url.txt"
        if url_file.exists():
            print(f"\n  ðŸ”— {url_file.read_text(encoding='utf-8').strip()}")
    print(f"\n  ðŸ“„ Reporte: {topic_folder}/slides/publish-report.json")
    print(f"  ðŸ“‹ Registro errores: python scripts/error_registry.py stats\n")

    sys.exit(publish_code)


if __name__ == "__main__":
    main()
