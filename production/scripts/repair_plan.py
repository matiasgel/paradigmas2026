#!/usr/bin/env python3
"""
repair_plan.py ÔÇö Orquesta el ciclo validaci├│n ÔåÆ correcci├│n ÔåÆ revalidaci├│n (v3)
================================================================================
Dise├▒ado para ser llamado en un loop por un agente. El agente corrige el plan
entre intentos; repair_plan.py solo normaliza, valida y reporta.

Solo soporta planes JSON v3.

Flujo del agente:
    1. Agente genera/corrige plan-filminas-{tema}.json
    2. python scripts/repair_plan.py {topic_folder} --attempt 1
       ÔåÆ exit 0: plan v├ílido ÔåÆ ejecutar slides_pipeline.py
       ÔåÆ exit 1: errores ÔåÆ agente corrige SOLO los campos reportados ÔåÆ --attempt 2
       ÔåÆ exit 2: max_attempts superado ÔåÆ STOP, revisi├│n humana

Uso:
    python scripts/repair_plan.py salida/cursadas/2026/temas/03-paradigmas
    python scripts/repair_plan.py salida/cursadas/2026/temas/03-paradigmas --attempt 2
    python scripts/repair_plan.py salida/cursadas/2026/temas/03-paradigmas --auto-publish

Exit codes:
    0 ÔÇö plan v├ílido
    1 ÔÇö errores encontrados (lista detallada por campo)
    2 ÔÇö max_attempts superado ÔÇö requiere revisi├│n humana
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from pipeline_common import (
    Result,
    find_plan,
    find_project_root,
    load_json,
    save_json,
)
import validate_plan as vp


# ÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉ
# NORMALIZACI├ôN
# ÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉ

def normalize_plan(plan_path: Path) -> None:
    """Re-serializa el plan JSON en forma can├│nica (indentaci├│n 2, UTF-8)."""
    data = load_json(plan_path)
    save_json(plan_path, data)


def _check_draft_not_used(plan_path: Path) -> Result[Path]:
    """Verifica que el plan no sea todav├¡a un DRAFT sin completar.

    Retorna Result[Path] con el path si no es draft, o errores.
    """
    data = load_json(plan_path)
    warnings: list[str] = []

    if "_draft_instructions" in data:
        warnings.append(
            "DRAFT: el plan contiene '_draft_instructions' ÔÇö eliminar esa clave "
            "y completar todos los campos pendientes antes de validar"
        )

    summary = data.get("summary", {})
    status = summary.get("status", "")
    if status == "DRAFT":
        warnings.append(
            f"DRAFT: summary.status='{status}' ÔÇö el plan a├║n no fue completado por el agente"
        )

    pending_count = int(summary.get("pending_types", 0) or 0)
    if pending_count > 0:
        warnings.append(
            f"DRAFT: summary.pending_types={pending_count} ÔÇö hay slides con type pendiente sin resolver"
        )

    return Result.fail(*warnings) if warnings else Result.ok(plan_path)


# ÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉ
# CLI
# ÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉÔòÉ

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="repair_plan.py ÔÇö Valida plan JSON y reporta errores estructurados por campo",
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
        help="N├║mero de intento actual (default: 1)",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=3,
        help="M├íximo de intentos antes de exit 2 (default: 3)",
    )
    parser.add_argument(
        "--auto-publish",
        action="store_true",
        help="Si el plan es v├ílido, ejecutar slides_pipeline.py directamente",
    )
    args = parser.parse_args(argv)

    topic_folder = Path(args.topic_folder).resolve()
    if not topic_folder.is_dir():
        print(f"ÔØî Directorio no existe: {topic_folder}")
        sys.exit(1)

    attempt = args.attempt
    max_attempts = args.max_attempts

    project_root = find_project_root(topic_folder)

    # ÔöÇÔöÇ Buscar el plan JSON v3 ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
    plan_result = find_plan(topic_folder)
    if not plan_result.is_ok:
        for err in plan_result.errors:
            print(f"ÔØî {err}")
        print("   Ejecutar primero: python scripts/parse_filminas.py <topic_folder>")
        print("   Luego completar el DRAFT y renombrar a plan-filminas-{tema}.json")
        sys.exit(1)

    plan_path = plan_result.unwrap()

    rel_path = plan_path.relative_to(project_root)
    print(f"­ƒöº Intento {attempt}/{max_attempts} ÔÇö {rel_path}")

    # ÔöÇÔöÇ Verificar que no sea un DRAFT sin completar ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
    draft_result = _check_draft_not_used(plan_path)
    if not draft_result.is_ok:
        print(f"\nÔÜá´©Å  El plan parece estar incompleto ({len(draft_result.errors)} advertencia(s)):\n")
        for w in draft_result.errors:
            print(f"   ÔÇó {w}")
        print("\n   Completar el plan antes de validar.")
        if attempt < max_attempts:
            print(f"\n   Volver a ejecutar con --attempt {attempt + 1} cuando el plan est├® completo.")
        sys.exit(1)

    # ÔöÇÔöÇ 1. Normalizar plan ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
    try:
        normalize_plan(plan_path)
        print("   Ô£ô JSON normalizado")
    except Exception as e:
        print(f"   ÔØî Error al normalizar JSON: {e}")
        print("   El archivo puede estar mal formado. Verificar sintaxis JSON.")
        sys.exit(1)

    # ÔöÇÔöÇ 2. Validar ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
    errors = vp.validate_plan(topic_folder)

    # ÔöÇÔöÇ 3a. Plan v├ílido ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
    if not errors:
        print(f"\nÔ£à Plan v├ílido en intento {attempt}/{max_attempts}.")
        print(f"   {rel_path}")

        if args.auto_publish:
            print("\n­ƒÜÇ --auto-publish activado ÔåÆ ejecutando slides_pipeline.py ÔÇª")
            import subprocess
            pipeline = Path(__file__).parent / "slides_pipeline.py"
            result = subprocess.run(
                [sys.executable, str(pipeline), str(topic_folder)],
                check=False,
            )
            sys.exit(result.returncode)

        print(f"\n   Siguiente paso: python scripts/slides_pipeline.py {args.topic_folder}")
        sys.exit(0)

    # ÔöÇÔöÇ 3b. Hay errores ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇ
    print(f"\nÔØî {len(errors)} error(es) en intento {attempt}/{max_attempts}:\n")
    for err in errors:
        print(f"   ÔÇó {err}")

    # M├íximo de intentos alcanzado
    if attempt >= max_attempts:
        print(f"""
Ôøö STOP ÔÇö Se agotaron los {max_attempts} intentos de reparaci├│n autom├ítica.
   El plan requiere revisi├│n humana antes de continuar.

   Plan:  {rel_path}

   Pasos para revisi├│n manual:
   1. Abrir el plan y corregir los errores listados arriba
   2. Validar manualmente: python scripts/validate_plan.py {args.topic_folder}
   3. Si pasa: python scripts/slides_pipeline.py {args.topic_folder}

   Referencia:
     Schema registry:   _edu/schemas/schema-registry.json
     Schema de plan:    _edu/schemas/plan-filminas.schema.json
     Gu├¡a de prompts:   _edu/templates/prompt-imagen-guide.md
""")
        sys.exit(2)

    # Hay intentos disponibles ÔåÆ instrucciones para el agente
    next_attempt = attempt + 1
    print(f"""
   ÔÜÖ´©Å  Corregir SOLO los campos reportados arriba en:
   {rel_path}

   IMPORTANTE: NO regenerar el plan completo. Solo corregir los campos con error.
   Para prompts vac├¡os: usar LENGUAJE VISUAL PURO (ver _edu/templates/prompt-imagen-guide.md).
   Schema registry: _edu/schemas/schema-registry.json

   Luego volver a ejecutar:
   python scripts/repair_plan.py {args.topic_folder} --attempt {next_attempt} --max-attempts {max_attempts}
""")
    sys.exit(1)


if __name__ == "__main__":
    main()