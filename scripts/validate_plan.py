#!/usr/bin/env python3
"""
validate_plan.py — Validador de plan-filminas (v3 schema-driven)

Valida que el plan JSON de un tema cumpla el contrato canónico antes
de ejecutar el pipeline de generación y publicación de filminas.

Carga JSON Schemas desde _edu/schemas/ y valida con jsonschema.
Lee TODOS los enums y mapeos desde schema-registry.json — no tiene
constantes propias de diseño.

Uso:
    python scripts/validate_plan.py salida/cursadas/2026/temas/02-sintaxis-semantica

Exit codes:
    0 — plan válido
    1 — errores encontrados (muestra lista detallada)
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    jsonschema = None  # type: ignore[assignment]

from pipeline_common import (
    Result,
    find_plan,
    find_project_root,
    load_config,
    load_json,
    load_registry,
)


# ═══════════════════════════════════════════════════════════════════════
# VALIDACIÓN v3 (JSON Schema)
# ═══════════════════════════════════════════════════════════════════════


def _validate_v3_schema(plan: dict, project_root: Path) -> Result[dict]:
    """Valida un plan JSON v3 contra los JSON Schemas.

    Retorna Result[dict] con el plan si pasa, o errores de schema.
    """
    if jsonschema is None:
        return Result.fail(
            "FATAL: paquete 'jsonschema' no instalado. "
            "Ejecutar: pip install jsonschema"
        )

    schemas_dir = project_root / "_edu" / "schemas"
    plan_schema_path = schemas_dir / "plan-filminas.schema.json"
    slide_schema_path = schemas_dir / "filmina-slide.schema.json"

    if not plan_schema_path.exists():
        return Result.fail(
            f"SCHEMA: No se encontró {plan_schema_path.relative_to(project_root)}"
        )

    plan_schema = load_json(plan_schema_path)
    slide_schema = load_json(slide_schema_path) if slide_schema_path.exists() else None

    # Construir resolver para $ref
    schema_store: dict[str, dict] = {}
    if slide_schema:
        schema_store[slide_schema.get("$id", "filmina-slide.schema.json")] = slide_schema
        schema_store["filmina-slide.schema.json"] = slide_schema

    registry = jsonschema.RefResolver.from_schema(plan_schema, store=schema_store)

    try:
        validator_cls = jsonschema.Draft202012Validator
    except AttributeError:
        validator_cls = jsonschema.Draft7Validator  # fallback

    validator = validator_cls(plan_schema, resolver=registry)

    errors = tuple(
        f"SCHEMA [{'.'.join(str(p) for p in e.absolute_path) or '(root)'}]: {e.message}"
        for e in validator.iter_errors(plan)
    )
    return Result.fail(*errors) if errors else Result.ok(plan)


def _validate_v3_semantic(plan: dict, project_root: Path) -> Result[dict]:
    """Validaciones semánticas que complementan el JSON Schema.

    Retorna Result[dict] con el plan si pasa, o errores semánticos.
    Acumula todos los errores encontrados (no cortocircuita).
    """
    errors: list[str] = []
    registry_data = load_registry(project_root)
    config = load_config(project_root)

    slides = plan.get("slides", [])
    summary = plan.get("summary", {})
    type_layout_map = registry_data.get("type_layout_map", {})

    # 1. Verificar conteo de slides
    actual_total = len(slides)
    declared_total = summary.get("total_slides", 0)
    if actual_total != declared_total:
        errors.append(
            f"SUMMARY: total_slides={declared_total} pero hay {actual_total} slides reales"
        )

    # 2. Verificar IDs únicos
    seen_ids: set[str] = set()
    for slide in slides:
        sid = slide.get("id", "?")
        if sid in seen_ids:
            errors.append(f"DUPLICADO: id='{sid}' aparece más de una vez")
        seen_ids.add(sid)

    # 3. Verificar type_distribution vs slides reales
    real_distribution: dict[str, int] = {}
    for slide in slides:
        stype = slide.get("type", "")
        real_distribution[stype] = real_distribution.get(stype, 0) + 1

    declared_dist = summary.get("type_distribution", {})
    if declared_dist and declared_dist != real_distribution:
        errors.append(
            f"SUMMARY: type_distribution declarada no coincide con la distribución real. "
            f"Real: {real_distribution}"
        )

    # 4. Verificar images_planned
    images_count = sum(
        1 for s in slides
        if (s.get("image") or {}).get("layer", "none") != "none"
    )
    declared_images = summary.get("images_planned", 0)
    if images_count != declared_images:
        errors.append(
            f"SUMMARY: images_planned={declared_images} pero hay {images_count} slides con image.layer != 'none'"
        )

    # 5. Verificar budget de imágenes
    gem_strategy = config.get("gemini_image_strategy", {}) or {}
    max_images = int(gem_strategy.get("max_per_presentation",
                     gem_strategy.get("max_images_per_presentation", 12)))
    if images_count > max_images:
        errors.append(
            f"BUDGET: {images_count} imágenes planificadas pero max_per_presentation={max_images}. "
            "Reducir imágenes o actualizar slides-config.yaml."
        )

    # 6. Verificar determinismo tipo→layout contra schema registry
    if type_layout_map:
        for slide in slides:
            sid = slide.get("id", "?")
            stype = slide.get("type", "")
            if stype not in type_layout_map:
                continue
            expected = type_layout_map[stype]
            expected_layout = expected.get("layout", {})
            actual_layout = slide.get("layout", {})
            for zone in ("title", "body", "image", "code", "table"):
                exp_val = expected_layout.get(zone)
                act_val = actual_layout.get(zone)
                if exp_val and act_val and exp_val != act_val:
                    errors.append(
                        f"DETERMINISMO [{sid}]: layout.{zone}='{act_val}' "
                        f"pero schema registry dice '{exp_val}' para type='{stype}'"
                    )
            expected_layer = expected.get("image_layer", "none")
            actual_layer = (slide.get("image") or {}).get("layer", "none")
            if expected_layer != actual_layer:
                errors.append(
                    f"DETERMINISMO [{sid}]: image.layer='{actual_layer}' "
                    f"pero schema registry dice '{expected_layer}' para type='{stype}'"
                )

    # 7. Verificar pending_types y pending_prompts
    pending_types = sum(1 for s in slides if not s.get("type"))
    declared_pending = summary.get("pending_types", 0)
    if pending_types != declared_pending:
        errors.append(
            f"SUMMARY: pending_types={declared_pending} pero hay {pending_types} slides sin tipo"
        )

    pending_prompts = sum(
        1 for s in slides
        if (s.get("image") or {}).get("layer", "none") != "none"
        and not (s.get("image") or {}).get("prompt", "").strip()
    )
    declared_pending_prompts = summary.get("pending_prompts", 0)
    if pending_prompts != declared_pending_prompts:
        errors.append(
            f"SUMMARY: pending_prompts={declared_pending_prompts} pero hay {pending_prompts} prompts vacíos"
        )

    return Result.fail(*errors) if errors else Result.ok(plan)


def validate_plan_v3(plan: dict, project_root: Path) -> Result[dict]:
    """Validación completa v3: JSON Schema + semántica.

    Ejecuta ambas validaciones y acumula todos los errores.
    """
    schema_result = _validate_v3_schema(plan, project_root)
    semantic_result = _validate_v3_semantic(plan, project_root)

    # Acumular errores de ambas validaciones
    all_errors = schema_result.errors + semantic_result.errors
    if all_errors:
        return Result.fail(*all_errors)
    return Result.ok(plan)


# ═══════════════════════════════════════════════════════════════════════
# API PÚBLICA
# ═══════════════════════════════════════════════════════════════════════


def validate_plan(topic_folder: Path) -> list[str]:
    """Valida el plan JSON v3 del tema y retorna lista de errores (vacía = válido)."""
    project_root = find_project_root(topic_folder)
    plan_result = find_plan(topic_folder)

    if not plan_result.is_ok:
        return list(plan_result.errors)

    plan_path = plan_result.unwrap()
    plan = load_json(plan_path)

    result = validate_plan_v3(plan, project_root)
    return list(result.errors)


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python scripts/validate_plan.py <ruta-tema>")
        print("Ejemplo: python scripts/validate_plan.py salida/cursadas/2026/temas/02-sintaxis-semantica")
        sys.exit(1)

    topic_folder = Path(sys.argv[1])
    if not topic_folder.is_absolute():
        topic_folder = (Path.cwd() / topic_folder).resolve()

    if not topic_folder.exists():
        print(f"ERROR: La carpeta del tema no existe: {topic_folder}")
        sys.exit(1)

    print(f"Validando plan de: {topic_folder.name}")
    errors = validate_plan(topic_folder)

    if errors:
        print(f"\n❌ {len(errors)} error(es) encontrado(s):\n")
        for err in errors:
            print(f"  • {err}")
        print("\n→ El agente debe corregir el plan antes de ejecutar el pipeline.")
        sys.exit(1)
    else:
        print("✅ Plan válido — todos los campos obligatorios presentes y coherentes.")
        print("   Podés ejecutar: python scripts/slides_pipeline.py <tema> --assets-only")
        sys.exit(0)


if __name__ == "__main__":
    main()
