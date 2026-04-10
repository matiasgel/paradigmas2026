#!/usr/bin/env python3
"""
EDU Slides Pipeline — Publish ALL topics into a single Google Slides presentation.

Combina todos los planes JSON v3 de todos los temas en una sola presentación.
Las imágenes Gemini se omiten; las tablas nativas se mantienen.

Uso:
  python publish_all_slides.py <topics_folder> [--no-images]
  python publish_all_slides.py salida/cursadas/iapjn-2026/temas --no-images
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Reuse the entire pipeline infrastructure
from slides_pipeline import (
    LAYOUT_MAP,
    _build_slide_requests,
    _clear_slides,
    _copy_template,
    _get_creds,
    _override_maps_from_registry,
    load_yaml,
)
from pipeline_common import find_project_root, load_json, load_registry


def _collect_plans(topics_folder: Path) -> list[tuple[str, dict]]:
    """Collect all plan JSON files sorted by topic folder name."""
    plans: list[tuple[str, dict]] = []
    for topic_dir in sorted(topics_folder.iterdir()):
        if not topic_dir.is_dir():
            continue
        slides_dir = topic_dir / "slides"
        if not slides_dir.is_dir():
            continue
        plan_files = list(slides_dir.glob("plan-filminas-*.json"))
        if not plan_files:
            continue
        plan_path = plan_files[0]
        plan = load_json(plan_path)
        if not plan.get("slides"):
            print(f"  ⚠️  {topic_dir.name}: plan sin slides, omitido")
            continue
        plans.append((topic_dir.name, plan))
        print(f"  📄 {topic_dir.name}: {len(plan['slides'])} filminas")
    return plans


def _disable_images(plan: dict) -> dict:
    """Set all image layers to none (skip Gemini images)."""
    for slide in plan.get("slides", []):
        img = slide.get("image", {})
        img["layer"] = "none"
        img["drive_id"] = None
        img["prompt"] = ""
        img["local_asset"] = ""
        slide["image"] = img
    return plan


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Publish ALL topics into one Google Slides deck")
    parser.add_argument("topics_folder", help="Path to the topics folder")
    parser.add_argument("--no-images", action="store_true", default=True,
                        help="Skip Gemini images (default: True)")
    args = parser.parse_args(argv)

    topics_folder = Path(args.topics_folder).resolve()
    if not topics_folder.is_dir():
        print(f"❌ No existe: {topics_folder}")
        sys.exit(1)

    project_root = find_project_root(topics_folder)

    # Load registry & override maps
    registry = load_registry(project_root)
    if registry:
        _override_maps_from_registry(registry)
        print("  ✓ Schema registry cargado")

    secrets_path = project_root / "_edu" / "secrets.local.yaml"
    config_path = project_root / "_edu" / "slides-config.yaml"
    token_path = project_root / "_edu" / "token_slides.json"

    for p, label in [(secrets_path, "secrets.local.yaml"), (config_path, "slides-config.yaml")]:
        if not p.exists():
            print(f"❌ Falta {label}")
            sys.exit(1)

    config = load_yaml(config_path)
    template_id = config.get("template_id", "")
    if not template_id:
        print("❌ template_id no configurado en slides-config.yaml")
        sys.exit(1)

    # Collect all plans
    print(f"\n📋 Recopilando planes de {topics_folder} …")
    plans = _collect_plans(topics_folder)
    if not plans:
        print("❌ No se encontraron planes JSON en ningún tema")
        sys.exit(1)

    total_slides = sum(len(p["slides"]) for _, p in plans)
    print(f"\n  Total: {len(plans)} temas, {total_slides} filminas")

    # Disable images if requested
    if args.no_images:
        for i, (name, plan) in enumerate(plans):
            plans[i] = (name, _disable_images(plan))
        print("  🚫 Imágenes Gemini desactivadas")

    # Authenticate
    creds = _get_creds(secrets_path, token_path)
    from googleapiclient.discovery import build
    drive_svc = build("drive", "v3", credentials=creds)
    slides_svc = build("slides", "v1", credentials=creds)

    # Create presentation from template
    course_title = "IA aplicada al Poder Judicial — Jornada Completa 2026"
    print(f"\n🚀 Creando presentación: {course_title}")
    pres_id = _copy_template(drive_svc, template_id, course_title)
    print(f"  Presentación creada: {pres_id}")

    _clear_slides(slides_svc, pres_id)

    # Build all requests
    all_reqs: list[dict] = []
    slide_idx = 0
    for topic_name, plan in plans:
        for slide in plan["slides"]:
            # Make page_id unique across all topics
            page_id = f"s_{topic_name[:20]}_{slide['id']}".replace("-", "_")[:50]
            reqs = _build_slide_requests(slide, config, page_id, slide_idx)
            all_reqs.extend(reqs)
            slide_idx += 1

    # Send in batches
    BATCH = 50
    total_reqs = len(all_reqs)
    failed_batches: list[str] = []
    print(f"  Enviando {total_reqs} requests en lotes de {BATCH} …")
    for i in range(0, total_reqs, BATCH):
        batch = all_reqs[i:i + BATCH]
        label = f"Lote {i // BATCH + 1}/{(total_reqs + BATCH - 1) // BATCH}"
        try:
            slides_svc.presentations().batchUpdate(
                presentationId=pres_id, body={"requests": batch}
            ).execute()
            print(f"  {label} ✓")
        except Exception as exc:
            print(f"  ⚠️  Error en {label}: {exc}")
            failed_batches.append(f"{label}: {exc}")

    if failed_batches:
        print(f"\n  ⚠️  {len(failed_batches)} lote(s) fallaron:")
        for msg in failed_batches:
            print(f"     • {msg}")

    url = f"https://docs.google.com/presentation/d/{pres_id}/edit"

    # Save URL
    url_path = topics_folder.parent / "slides-all-url.txt"
    url_path.write_text(url, encoding="utf-8")

    print(f"""
🎉 Presentación completa generada!
   Temas:   {len(plans)}
   Slides:  {total_slides}
   URL:     {url}
   Guardado en: {url_path.relative_to(project_root)}
""")


if __name__ == "__main__":
    main()
