#!/usr/bin/env python3
"""
repair_plan.py — Orquesta el ciclo validación → corrección → revalidación (Sprint 3)
======================================================================================
Diseñado para ser llamado en un loop por un agente. El agente corrige el plan
entre intentos; repair_plan.py solo normaliza, valida y reporta.

Flujo del agente:
    1. Agente genera/corrige plan-filminas-{tema}.yaml
    2. python scripts/repair_plan.py {topic_folder} --attempt 1
       → exit 0: plan válido → ejecutar slides_pipeline.py
       → exit 1: errores → agente corrige SOLO los campos reportados → --attempt 2
       → exit 2: max_attempts superado → STOP, revisión humana

Uso:
    python scripts/repair_plan.py salida/cursadas/2026/temas/03-paradigmas
    python scripts/repair_plan.py salida/cursadas/2026/temas/03-paradigmas --attempt 2
    python scripts/repair_plan.py salida/cursadas/2026/temas/03-paradigmas --auto-publish

Exit codes:
    0 — plan válido
    1 — errores encontrados (lista detallada por campo)
    2 — max_attempts superado — requiere revisión humana
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import validate_plan as vp
from slides_pipeline import find_project_root


# ═══════════════════════════════════════════════════════════════════════
# NORMALIZACIÓN
# ═══════════════════════════════════════════════════════════════════════

def normalize_plan(plan_path: Path) -> None:
    """
    Re-serializa el plan YAML en forma canónica.
    Elimina variaciones de formato (ordenación de claves, indentación, comillas)
    para que las diffs entre intentos reflejen solo cambios de contenido.
    """
    with plan_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    with plan_path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def _find_plan(topic_folder: Path) -> Path | None:
    """Busca el plan-filminas-*.yaml en slides/. Retorna None si no existe."""
    slides_dir = topic_folder / "slides"
    topic_id = topic_folder.name
    candidate = slides_dir / f"plan-filminas-{topic_id}.yaml"
    if candidate.exists():
        return candidate
    if slides_dir.exists():
        found = sorted(slides_dir.glob("plan-filminas-*.yaml"))
        if found:
            return found[0]
    return None


def _check_draft_not_used(plan_path: Path) -> list[str]:
    """Verifica que el plan no sea todavía un DRAFT sin completar."""
    warnings: list[str] = []
    with plan_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    meta = data.get("meta", {})
    if "_draft_instructions" in data:
        warnings.append(
            "DRAFT: el plan contiene '_draft_instructions' — eliminar esa clave "
            "y completar todos los campos pendientes antes de validar"
        )
    if str(meta.get("status", "")).startswith("DRAFT"):
        warnings.append(
            f"DRAFT: meta.status='{meta.get('status')}' — el plan aún no fue completado por el agente"
        )
    pending_count = int(meta.get("pending_types", 0) or 0)
    if pending_count > 0:
        warnings.append(
            f"DRAFT: meta.pending_types={pending_count} — hay slides con type: pending sin resolver"
        )
    return warnings


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="repair_plan.py — Valida plan YAML y reporta errores estructurados por campo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "topic_folder",
        help="Ruta a la carpeta del tema (ej: salida/cursadas/2026/temas/03-paradigmas)",
    )
    parser.add_argument(
        "--attempt",
        type=int,
        default=1,
        help="Número de intento actual (default: 1)",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=3,
        help="Máximo de intentos antes de exit 2 (default: 3)",
    )
    parser.add_argument(
        "--auto-publish",
        action="store_true",
        help="Si el plan es válido, ejecutar slides_pipeline.py directamente",
    )
    args = parser.parse_args(argv)

    topic_folder = Path(args.topic_folder).resolve()
    if not topic_folder.is_dir():
        print(f"❌ Directorio no existe: {topic_folder}")
        sys.exit(1)

    attempt = args.attempt
    max_attempts = args.max_attempts

    project_root = find_project_root(topic_folder)

    # ── Buscar el plan ────────────────────────────────────────────────
    plan_path = _find_plan(topic_folder)
    if not plan_path:
        slides_dir = topic_folder / "slides"
        print(f"❌ No se encontró plan-filminas-*.yaml en {slides_dir}")
        print("   Ejecutar primero: python scripts/parse_filminas.py <topic_folder>")
        print("   Luego completar el DRAFT y renombrar a plan-filminas-{tema}.yaml")
        sys.exit(1)

    rel_path = plan_path.relative_to(project_root)
    print(f"🔧 Intento {attempt}/{max_attempts} — {rel_path}")

    # ── Verificar que no sea un DRAFT sin completar ───────────────────
    draft_warnings = _check_draft_not_used(plan_path)
    if draft_warnings:
        print(f"\n⚠️  El plan parece estar incompleto ({len(draft_warnings)} advertencia(s)):\n")
        for w in draft_warnings:
            print(f"   • {w}")
        print("\n   Completar el plan antes de validar.")
        if attempt < max_attempts:
            print(f"\n   Volver a ejecutar con --attempt {attempt + 1} cuando el plan esté completo.")
        sys.exit(1)

    # ── 1. Normalizar YAML ────────────────────────────────────────────
    try:
        normalize_plan(plan_path)
        print("   ✓ YAML normalizado")
    except Exception as e:
        print(f"   ❌ Error al normalizar YAML: {e}")
        print("   El archivo puede estar mal formado. Verificar sintaxis YAML.")
        sys.exit(1)

    # ── 2. Validar ────────────────────────────────────────────────────
    errors = vp.validate_plan(topic_folder)

    # ── 3a. Plan válido ───────────────────────────────────────────────
    if not errors:
        print(f"\n✅ Plan válido en intento {attempt}/{max_attempts}.")
        print(f"   {rel_path}")

        if args.auto_publish:
            print("\n🚀 --auto-publish activado → ejecutando slides_pipeline.py …")
            import subprocess
            pipeline = Path(__file__).parent / "slides_pipeline.py"
            result = subprocess.run(
                [sys.executable, str(pipeline), str(topic_folder)],
                check=False,
            )
            sys.exit(result.returncode)

        print(f"\n   Siguiente paso: python scripts/slides_pipeline.py {args.topic_folder}")
        sys.exit(0)

    # ── 3b. Hay errores ───────────────────────────────────────────────
    print(f"\n❌ {len(errors)} error(es) en intento {attempt}/{max_attempts}:\n")
    for err in errors:
        print(f"   • {err}")

    # Máximo de intentos alcanzado
    if attempt >= max_attempts:
        print(f"""
⛔ STOP — Se agotaron los {max_attempts} intentos de reparación automática.
   El plan requiere revisión humana antes de continuar.

   Plan:  {rel_path}

   Pasos para revisión manual:
   1. Abrir el plan y corregir los errores listados arriba
   2. Validar manualmente: python scripts/validate_plan.py {args.topic_folder}
   3. Si pasa: python scripts/slides_pipeline.py {args.topic_folder}

   Referencia:
     Tipos permitidos:  _edu/templates/filmina-slide-schema.yaml
     Guía de prompts:   _edu/templates/prompt-imagen-guide.md
""")
        sys.exit(2)

    # Hay intentos disponibles → instrucciones para el agente
    next_attempt = attempt + 1
    print(f"""
   ⚙️  Corregir SOLO los campos reportados arriba en:
   {rel_path}

   IMPORTANTE: NO regenerar el plan completo. Solo corregir los campos con error.
   Para prompts vacíos: usar LENGUAJE VISUAL PURO (ver _edu/templates/prompt-imagen-guide.md).

   Luego volver a ejecutar:
   python scripts/repair_plan.py {args.topic_folder} --attempt {next_attempt} --max-attempts {max_attempts}
""")
    sys.exit(1)


if __name__ == "__main__":
    main()
