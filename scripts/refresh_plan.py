#!/usr/bin/env python3
"""
refresh_plan.py ÔÇö Re-parsea filminas.md y actualiza plan-filminas preservando im├ígenes ya generadas.
======================================================================================================
Uso:
    python scripts/refresh_plan.py salida/cursadas/2026/temas/07-paradigma-logico-avanzado

Comportamiento:
  1. Re-parsea filminas.md con el parser corregido (sin @tipo: en body_blocks)
  2. Preserva del plan existente: image.local_asset, image.drive_id, image.prompt, layout, type
  3. Sobreescribe plan-filminas-{tema}.json con el contenido actualizado
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

# Agregar scripts/ al path
sys.path.insert(0, str(Path(__file__).parent))

from pipeline_common import find_project_root, load_registry, load_yaml, save_json
from slides_pipeline import load_filminas_schema, parse_filminas


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python scripts/refresh_plan.py <topic_folder>")
        sys.exit(1)

    topic_folder = Path(sys.argv[1])
    if not topic_folder.is_absolute():
        topic_folder = Path.cwd() / topic_folder

    filminas_path = topic_folder / "filminas.md"
    if not filminas_path.exists():
        print(f"ERROR: No se encontr├│ {filminas_path}")
        sys.exit(1)

    slides_dir = topic_folder / "slides"
    slides_dir.mkdir(exist_ok=True)

    topic_id = topic_folder.name
    plan_path = slides_dir / f"plan-filminas-{topic_id}.json"

    project_root = find_project_root(topic_folder)
    registry = load_registry(project_root)
    schema = load_filminas_schema(project_root)

    # Cargar plan existente para preservar im├ígenes
    existing_by_id: dict[str, dict] = {}
    if plan_path.exists():
        with open(plan_path, encoding="utf-8") as f:
            existing_plan = json.load(f)
        for slide in existing_plan.get("slides", []):
            existing_by_id[slide["id"]] = slide
        print(f"Plan existente cargado: {len(existing_by_id)} slides")
    else:
        print("No hay plan existente ÔÇö creando desde cero")

    # Re-parsear filminas.md con parser corregido
    print(f"Parseando {filminas_path} ...")
    new_slides_raw = parse_filminas(filminas_path, schema)
    print(f"Slides parseados: {len(new_slides_raw)}")

    type_layout_map = registry.get("type_layout_map", {})

    merged_slides = []
    for raw in new_slides_raw:
        sid = raw["id"]
        existing = existing_by_id.get(sid, {})

        # Tipo: prioridad al @tipo: de filminas.md (source of truth);
        # fallback al existente si el nuevo parse no detect├│ directiva
        directive_type = raw.get("directives", {}).get("type", "").strip()
        slide_type = directive_type or existing.get("type") or "pending"

        # Layout: del registry seg├║n tipo
        layout = existing.get("layout") or (
            type_layout_map.get(slide_type, {}).get("layout", {})
            if slide_type != "pending" else {}
        )

        # Imagen: preservar todo lo que existe (prompt, local_asset, drive_id)
        image_layer = (
            type_layout_map.get(slide_type, {}).get("image_layer", "none")
            if slide_type != "pending" else "none"
        )
        image = {
            "layer": existing.get("image", {}).get("layer", image_layer),
            "prompt": existing.get("image", {}).get("prompt", ""),
            "local_asset": existing.get("image", {}).get("local_asset", ""),
            "drive_id": existing.get("image", {}).get("drive_id", None),
        }

        # table_assets: preservar del existente
        table_assets = existing.get("table_assets", [])

        slide = {
            "id": sid,
            "type": slide_type,
            "title": raw.get("title", ""),
            "subtitle": raw.get("subtitle", ""),
            "body_blocks": raw.get("body_blocks", []),
            "code_blocks": raw.get("code_blocks", []),
            "tables": raw.get("tables", []),
            "directives": raw.get("directives", {}),
            "asset_hints": raw.get("asset_hints", []),
            "layout": layout,
            "image": image,
            "table_assets": table_assets,
        }
        merged_slides.append(slide)

    # Armar plan final
    slides_config = load_yaml(project_root / "_edu" / "slides-config.yaml")
    edu_config = load_yaml(project_root / "_edu" / "config.yaml")

    images_planned = sum(
        1 for s in merged_slides if s["image"]["layer"] not in ("none", "")
    )

    type_dist: dict[str, int] = {}
    for s in merged_slides:
        t = s["type"]
        type_dist[t] = type_dist.get(t, 0) + 1

    plan = {
        "meta": {
            "topic_id": topic_id,
            "title": merged_slides[0]["title"] if merged_slides else topic_id,
            "source": "filminas.md",
            "schema_version": "3.0.0",
            "schema_path": "_edu/templates/filminas-schema.yaml",
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "template_id": slides_config.get("template_id", ""),
            "total_slides": len(merged_slides),
            "images_planned": images_planned,
        },
        "summary": {
            "total_slides": len(merged_slides),
            "images_planned": images_planned,
            "type_distribution": type_dist,
        },
        "slides": merged_slides,
    }

    save_json(plan_path, plan)
    print(f"\nÔ£ô Plan actualizado: {plan_path}")
    print(f"  Slides: {len(merged_slides)} | Im├ígenes preservadas: {sum(1 for s in merged_slides if s['image']['local_asset'])}")

    # Verificar que no hay @tipo: en body_blocks
    tipo_count = sum(
        1
        for s in merged_slides
        for b in s["body_blocks"]
        if b.get("type") == "text" and "@tipo:" in str(b.get("content", ""))
    )
    if tipo_count:
        print(f"  ÔÜá ATENCI├ôN: quedan {tipo_count} bloques con @tipo: en body_blocks")
    else:
        print("  Ô£ô Sin directivas @tipo: en body_blocks")


if __name__ == "__main__":
    main()