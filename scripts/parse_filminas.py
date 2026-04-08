#!/usr/bin/env python3
"""
parse_filminas.py — Genera plan DRAFT desde filminas.md (v3 — Schema-Driven)
=============================================================================
Primer paso del flujo v3: filminas.md → plan-draft-{tema}.json

Lee TODOS los enums y mapeos desde schema-registry.json — no importa
LAYOUT_MAP ni IMAGE_STRATEGY de slides_pipeline.py.

DIFERENCIA CLAVE con v2:
  - type: usa SOLO la directiva @tipo:. Sin @tipo: → type: "pending".
    NUNCA infiere tipos desde el título o contenido.
  - image: objeto unificado {layer, prompt, local_asset, drive_id}
    (ya no hay background_image / content_image separados)
  - Salida: JSON, no YAML
  - Schema: lee type_layout_map del schema-registry.json

El agente (slides-designer o class-writer) recibe el DRAFT, asigna tipos explícitos
y escribe prompts de imagen con lenguaje visual puro (ver _edu/templates/prompt-imagen-guide.md).
Luego validate_plan.py / repair_plan.py verifican el contrato antes de publicar.

Uso:
    python scripts/parse_filminas.py salida/cursadas/2026/temas/03-paradigmas

Produce:
    {topic_folder}/slides/plan-draft-{tema}.json

Flujo completo v3:
    1. python scripts/parse_filminas.py <topic_folder>         → DRAFT JSON
    2. Agente completa tipos y prompts en plan-draft-{tema}.json
    3. Renombrar a plan-filminas-{tema}.json (o el agente lo hace)
    4. python scripts/repair_plan.py <topic_folder>            → valida y repara
    5. python scripts/slides_pipeline.py <topic_folder>        → publica

Requiere:
    _edu/slides-config.yaml                — sistema de diseño
    _edu/schemas/schema-registry.json      — mapeos y enums
    {topic_folder}/filminas.md
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

# Pipeline compartido — utilidades centralizadas
from pipeline_common import (
    find_project_root,
    load_registry,
    load_yaml,
    save_json,
)

# Reutiliza SOLO funciones de parseo del pipeline principal
from slides_pipeline import (
    load_filminas_schema,
    parse_filminas,
)


# ═══════════════════════════════════════════════════════════════════════
# SCHEMA REGISTRY
# ═══════════════════════════════════════════════════════════════════════


def _build_maps(registry: dict) -> tuple[dict[str, dict], dict[str, str]]:
    """Construye LAYOUT_MAP e IMAGE_STRATEGY desde el schema registry."""
    type_layout_map = registry.get("type_layout_map", {})
    return (
        {
            stype: mapping.get("layout", {})
            for stype, mapping in type_layout_map.items()
            if isinstance(mapping, dict)
        },
        {
            stype: mapping.get("image_layer", "none")
            for stype, mapping in type_layout_map.items()
            if isinstance(mapping, dict)
        },
    )


# ═══════════════════════════════════════════════════════════════════════
# CORE
# ═══════════════════════════════════════════════════════════════════════

PENDING = "pending"


def generate_draft(filminas_path: Path, _config: dict, template_id: str) -> tuple[dict, int, int]:
    """
    Parsea filminas.md y produce un plan DRAFT en formato v3.

    Returns:
        (draft_dict, n_pending_types, n_pending_prompts)
    """
    project_root = find_project_root(filminas_path.parent)
    schema = load_filminas_schema(project_root)
    registry = load_registry(project_root)
    layout_map, image_strategy = _build_maps(registry)

    canonical_types = registry.get("canonical_types", {}).get("enum", [])

    # parse_filminas() devuelve type = directives.get("type") or "pending"
    slides = parse_filminas(filminas_path, schema)

    topic_id = filminas_path.parent.name
    topic_title = topic_id.replace("-", " ").title()
    if slides:
        first = slides[0]
        candidate = (first.get("subtitle") or first.get("title") or "").strip()
        if candidate:
            topic_title = candidate

    pending_types: list[str] = []
    pending_prompts: list[str] = []
    plan_slides = []

    for slide in slides:
        sid = slide["id"]
        stype = slide.get("type", PENDING)
        directives = slide.get("directives") or {}

        if stype == PENDING:
            pending_types.append(sid)

        # Layout: desde registry type_layout_map si tipo conocido, {} si pending
        layout = dict(layout_map.get(stype, {})) if stype != PENDING else {}

        # Imagen: determinar layer desde registry image_strategy
        img_directive = directives.get("image", "")
        if img_directive == "background":
            image_layer = "background"
        elif img_directive == "content":
            image_layer = "content"
        else:
            image_layer = image_strategy.get(stype, "none") if stype != PENDING else "none"

        # Prompt: desde @prompt-imagen: si existe, sino "" (agente lo completa)
        explicit_prompt = (directives.get("image_prompt") or "").strip()
        image_prompt = explicit_prompt if image_layer != "none" else ""

        # Marcar como pendiente si falta prompt para slide con imagen
        if image_layer != "none" and not image_prompt:
            pending_prompts.append(sid)

        # Local asset path
        if image_layer == "background":
            local_asset = f"slides/assets/{sid}-bg.png"
        elif image_layer == "content":
            local_asset = f"slides/assets/{sid}-content.png"
        else:
            local_asset = ""

        table_assets = [
            {
                "index": idx,
                "table_markdown": tmd,
                "local_asset": f"slides/assets/{sid}-table-{idx + 1}.png",
                "drive_id": None,
            }
            for idx, tmd in enumerate(slide.get("tables") or [])
        ]

        plan_slides.append({
            "id":          sid,
            "type":        stype,
            "title":       slide["title"],
            "subtitle":    slide.get("subtitle", ""),
            "body_blocks": slide.get("body_blocks") or [],
            "code_blocks": slide.get("code_blocks") or [],
            "tables":      slide.get("tables") or [],
            "layout":      layout,
            "image": {
                "layer":       image_layer,
                "prompt":      image_prompt,
                "local_asset": local_asset,
                "drive_id":    None,
            },
            "table_assets": table_assets,
        })

    total = len(slides)

    # Calcular type_distribution
    type_dist: dict[str, int] = {}
    for s in plan_slides:
        t = s["type"]
        if t != PENDING:
            type_dist[t] = type_dist.get(t, 0) + 1

    images_count = sum(1 for s in plan_slides if s["image"]["layer"] != "none")
    tables_count = sum(len(s.get("table_assets", [])) for s in plan_slides)
    code_slides = sum(1 for s in plan_slides if s.get("code_blocks"))

    draft = {
        "$schema_version": "plan-filminas/v3",
        "meta": {
            "topic_id":             topic_id,
            "title":                topic_title,
            "source":               "filminas.md",
            "generated_at":         datetime.now().isoformat(timespec="seconds"),
            "template_id":          template_id,
            "topics_folder":        str(filminas_path.parent.parent),
            "topic_folder":         str(filminas_path.parent),
            "design_system_path":   "_edu/slides-config.yaml",
            "pipeline_runtime_path": "_edu/slides-pipeline.json",
            "schema_registry_path": "_edu/schemas/schema-registry.json",
        },
        "summary": {
            "total_slides":      total,
            "images_planned":    images_count,
            "tables_planned":    tables_count,
            "code_slides":       code_slides,
            "status":            "DRAFT",
            "pending_types":     len(pending_types),
            "pending_prompts":   len(pending_prompts),
            "type_distribution": type_dist,
        },
        "slides": plan_slides,
        # Instrucciones para el agente — eliminar del plan-filminas final
        "_draft_instructions": {
            "pending_type_ids":    pending_types,
            "pending_prompt_ids":  pending_prompts,
            "canonical_types":     canonical_types or [
                "portada", "concepto-abstracto", "concepto-mixto", "codigo",
                "tabla", "tabla-comparativa", "tabla-mixta", "diagrama",
                "socratica", "demo", "cierre", "timeline",
            ],
            "next_steps": [
                "1. Leer schema-registry.json ANTES de cualquier edición",
                "2. Asignar type explícito desde canonical_types a cada slide en pending_type_ids",
                "3. Copiar layout EXACTO del type_layout_map para cada tipo asignado",
                "4. Para slides con image.layer!='none': escribir prompt VISUAL PURO (ver prompt-imagen-guide.md)",
                "5. Actualizar summary: total_slides, images_planned, tables_planned, code_slides, type_distribution",
                "6. Cambiar summary.status a 'READY_FOR_VALIDATION'",
                "7. Eliminar esta clave '_draft_instructions'",
                f"8. Renombrar a: slides/plan-filminas-{topic_id}.json",
                "9. Validar: python scripts/repair_plan.py <topic_folder> --attempt 1",
                "10. Publicar: python scripts/slides_pipeline.py <topic_folder>",
            ],
        },
    }

    return draft, len(pending_types), len(pending_prompts)


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="parse_filminas.py — Plan DRAFT desde filminas.md (v3, schema-driven, JSON output)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "topic_folder",
        help="Ruta a la carpeta del tema (ej: salida/cursadas/2026/temas/03-paradigmas)",
    )
    args = parser.parse_args(argv)

    topic_folder = Path(args.topic_folder).resolve()
    if not topic_folder.is_dir():
        print(f"❌ Directorio no existe: {topic_folder}")
        sys.exit(1)

    project_root = find_project_root(topic_folder)
    config_path = project_root / "_edu" / "slides-config.yaml"
    if not config_path.exists():
        print("❌ Falta _edu/slides-config.yaml — ejecutar /edu-slides-designer primero.")
        sys.exit(1)

    config = load_yaml(config_path)
    template_id = config.get("template_id", "")
    filminas_path = topic_folder / "filminas.md"
    if not filminas_path.exists():
        print(f"❌ No se encontró filminas.md en {topic_folder}")
        sys.exit(1)

    # Verificar schema registry
    registry_path = project_root / "_edu" / "schemas" / "schema-registry.json"
    if not registry_path.exists():
        print("⚠️  _edu/schemas/schema-registry.json no encontrado — usando fallback.")

    print(f"📋 Parseando {filminas_path.relative_to(project_root)} …")
    try:
        draft, n_pending_types, n_pending_prompts = generate_draft(filminas_path, config, template_id)
    except ValueError as exc:
        print(f"❌ Contrato de filminas inválido:\n{exc}")
        sys.exit(1)

    topic_id = topic_folder.name
    draft_name = f"plan-draft-{topic_id}.json"
    draft_path = topic_folder / "slides" / draft_name
    save_json(draft_path, draft)

    summary = draft["summary"]
    total = summary["total_slides"]

    print(f"""
✅ Plan DRAFT generado: {draft_path.relative_to(project_root)}
   {total} filminas en total
   {total - n_pending_types} con tipo explícito (@tipo: en filminas.md)
   {n_pending_types} con type: pending — agente debe asignar tipo explícito
   {n_pending_prompts} sin prompt de imagen — agente debe escribir prompt visual puro""")

    if n_pending_types:
        ids = draft["_draft_instructions"]["pending_type_ids"]
        print(f"\n   Slides sin tipo: {', '.join(ids)}")
    if n_pending_prompts:
        ids = draft["_draft_instructions"]["pending_prompt_ids"]
        print(f"   Slides sin prompt: {', '.join(ids)}")

    print(f"""
Próximos pasos:
  1. Leer schema registry:        _edu/schemas/schema-registry.json
  2. El agente completa el plan:   {draft_path.relative_to(project_root)}
  3. Renombrar a:                  slides/plan-filminas-{topic_id}.json
  4. Validar y reparar:            python scripts/repair_plan.py {args.topic_folder} --attempt 1
  5. Publicar:                     python scripts/slides_pipeline.py {args.topic_folder}

Referencias:
  Schema registry:    _edu/schemas/schema-registry.json
  Schema de slide:    _edu/schemas/filmina-slide.schema.json
  Schema de plan:     _edu/schemas/plan-filminas.schema.json
  Guía de prompts:    _edu/templates/prompt-imagen-guide.md
""")


if __name__ == "__main__":
    main()
