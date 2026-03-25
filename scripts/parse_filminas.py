#!/usr/bin/env python3
"""
parse_filminas.py — Genera plan DRAFT desde filminas.md (Sprint 2 — Arquitectura v2)
======================================================================================
Primer paso del flujo v2: filminas.md → plan-draft-{tema}.yaml

DIFERENCIA CLAVE con generate_plan() (deprecated):
  - type: usa SOLO la directiva @tipo:. Sin @tipo: → type: "pending".
    NUNCA infiere tipos desde el título o contenido.
  - image.prompt: siempre vacío en el DRAFT. El agente lo completa.

El agente (slides-designer o class-writer) recibe el DRAFT, asigna tipos explícitos
y escribe prompts de imagen con lenguaje visual puro (ver _edu/templates/prompt-imagen-guide.md).
Luego validate_plan.py / repair_plan.py verifican el contrato antes de publicar.

Uso:
    python scripts/parse_filminas.py salida/cursadas/2026/temas/03-paradigmas

Produce:
    {topic_folder}/slides/plan-draft-{tema}.yaml

Flujo completo v2:
    1. python scripts/parse_filminas.py <topic_folder>         → DRAFT
    2. Agente completa tipos y prompts en plan-draft-{tema}.yaml
    3. Renombrar a plan-filminas-{tema}.yaml (o el agente lo hace)
    4. python scripts/repair_plan.py <topic_folder>            → valida y repara
    5. python scripts/slides_pipeline.py <topic_folder>        → publica

Requiere:
    _edu/slides-config.yaml   — sistema de diseño
    {topic_folder}/filminas.md
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

import yaml

# Reutiliza las funciones de parseo del pipeline principal (sin invocar APIs)
sys.path.insert(0, str(Path(__file__).parent))
from slides_pipeline import (
    apply_pipeline_runtime,
    parse_filminas,
    load_filminas_schema,
    find_project_root,
    load_yaml,
    save_yaml,
    LAYOUT_MAP,
    IMAGE_STRATEGY,
)

# ═══════════════════════════════════════════════════════════════════════
# CORE
# ═══════════════════════════════════════════════════════════════════════

PENDING = "pending"


def generate_draft(filminas_path: Path, config: dict, template_id: str) -> tuple[dict, int, int]:
    """
    Parsea filminas.md y produce un plan DRAFT.

    Returns:
        (draft_dict, n_pending_types, n_pending_prompts)
    """
    project_root = find_project_root(filminas_path.parent)
    apply_pipeline_runtime(project_root, config, filminas_path.parent)
    schema = load_filminas_schema(project_root)

    # parse_filminas() (v2) devuelve type = directives.get("type") or "pending"
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

        # Layout: desde LAYOUT_MAP si tipo conocido, {} si pending (agente lo completa)
        layout = dict(LAYOUT_MAP.get(stype, {})) if stype != PENDING else {}

        # Imagen: directiva @imagen: tiene prioridad, luego IMAGE_STRATEGY[tipo]
        img_directive = directives.get("image", "")
        if img_directive == "background":
            bg_strategy, ct_strategy = "gemini", "none"
        elif img_directive == "content":
            bg_strategy, ct_strategy = "none", "gemini"
        else:
            img_from_type = IMAGE_STRATEGY.get(stype, "none") if stype != PENDING else "none"
            if img_from_type == "background":
                bg_strategy, ct_strategy = "gemini", "none"
            elif img_from_type == "content":
                bg_strategy, ct_strategy = "none", "gemini"
            else:
                bg_strategy, ct_strategy = "none", "none"

        # Prompt: desde @prompt-imagen: si existe, sino "" (agente lo completa)
        explicit_prompt = (directives.get("image_prompt") or "").strip()
        bg_prompt = explicit_prompt if bg_strategy == "gemini" else ""
        ct_prompt = explicit_prompt if ct_strategy == "gemini" else ""

        # Marcar como pendiente si falta prompt para slide con imagen
        if (bg_strategy == "gemini" and not bg_prompt) or (ct_strategy == "gemini" and not ct_prompt):
            pending_prompts.append(sid)

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
            "type":        stype,           # "pending" si no hay @tipo: en filminas.md
            "title":       slide["title"],
            "subtitle":    slide.get("subtitle", ""),
            "body_blocks": slide.get("body_blocks") or [],
            "code_blocks": slide.get("code_blocks") or [],
            "tables":      slide.get("tables") or [],
            "directives":  directives,
            "asset_hints": slide.get("asset_hints") or [],
            # Layout: vacío si type es "pending", el agente lo completa
            "layout": layout,
            # Imágenes: prompts vacíos — AGENTE DEBE COMPLETARLOS con lenguaje visual puro
            # Ver: _edu/templates/prompt-imagen-guide.md
            "background_image": {
                "strategy":    bg_strategy,
                "prompt":      bg_prompt,   # "" si pendiente → OBLIGATORIO completar
                "local_asset": f"slides/assets/{sid}-bg.png" if bg_strategy == "gemini" else "",
                "drive_id":    None,
            },
            "content_image": {
                "strategy":    ct_strategy,
                "prompt":      ct_prompt,   # "" si pendiente → OBLIGATORIO completar
                "local_asset": f"slides/assets/{sid}-content.png" if ct_strategy == "gemini" else "",
                "drive_id":    None,
            },
            "table_assets": table_assets,
        })

    total = len(slides)
    known = total - len(pending_types)

    draft = {
        "meta": {
            "topic_id":        topic_id,
            "title":           topic_title,
            "source":          "filminas.md",
            "schema_version":  schema.get("version", "filminas/v2"),
            "schema_path":     schema.get("_path", "_edu/templates/filminas-schema.yaml"),
            "generated_at":    datetime.now().isoformat(timespec="seconds"),
            "template_id":     template_id,
            "total_slides":    total,
            "known_types":     known,
            "pending_types":   len(pending_types),
            "pending_prompts": len(pending_prompts),
            "status":          "DRAFT — INCOMPLETO: completar campos pendientes antes de publicar",
        },
        "slides": plan_slides,
        # Instrucciones para el agente — eliminar de plan-filminas-{tema}.yaml final
        "_draft_instructions": {
            "pending_type_ids":    pending_types,
            "pending_prompt_ids":  pending_prompts,
            "enum_types": [
                "portada", "concepto-abstracto", "concepto-mixto", "codigo",
                "tabla", "tabla-comparativa", "tabla-mixta", "diagrama",
                "socratica", "demo", "cierre", "timeline",
            ],
            "next_steps": [
                "1. Asignar type explícito a cada slide en pending_type_ids (ver filmina-slide-schema.yaml)",
                "2. Completar layout para slides con type anterior a pending",
                "3. Para slides con image.strategy=gemini: escribir prompt VISUAL PURO (ver prompt-imagen-guide.md)",
                f"4. Eliminar la clave '_draft_instructions' de este archivo",
                f"5. Renombrar a: slides/plan-filminas-{topic_id}.yaml",
                f"6. Validar: python scripts/repair_plan.py <topic_folder> --attempt 1",
                f"7. Publicar: python scripts/slides_pipeline.py <topic_folder>",
            ],
        },
    }

    return draft, len(pending_types), len(pending_prompts)


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="parse_filminas.py — Plan DRAFT desde filminas.md (v2, sin inferencia de tipos)",
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

    print(f"📋 Parseando {filminas_path.relative_to(project_root)} …")
    try:
        draft, n_pending_types, n_pending_prompts = generate_draft(filminas_path, config, template_id)
    except ValueError as exc:
        print(f"❌ Contrato de filminas inválido:\n{exc}")
        sys.exit(1)

    topic_id = topic_folder.name
    draft_name = f"plan-draft-{topic_id}.yaml"
    draft_path = topic_folder / "slides" / draft_name
    save_yaml(draft_path, draft)

    total = draft["meta"]["total_slides"]
    known = draft["meta"]["known_types"]

    print(f"""
✅ Plan DRAFT generado: {draft_path.relative_to(project_root)}
   {total} filminas en total
   {known} con tipo explícito (@tipo: en filminas.md)
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
  1. El agente completa el plan:   {draft_path.relative_to(project_root)}
  2. Renombrar a:                  slides/plan-filminas-{topic_id}.yaml
  3. Validar y reparar:            python scripts/repair_plan.py {args.topic_folder} --attempt 1
  4. Publicar:                     python scripts/slides_pipeline.py {args.topic_folder}

Referencias:
  Tipos permitidos:   _edu/templates/filmina-slide-schema.yaml
  Guía de prompts:    _edu/templates/prompt-imagen-guide.md
""")


if __name__ == "__main__":
    main()
