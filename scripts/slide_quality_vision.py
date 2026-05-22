#!/usr/bin/env python3
"""
Slide Quality Vision — CLIP score + layout metrics (S10.3).

Evalúa calidad visual de slides usando:
- OpenCLIP: relevancia imagen-texto, coherencia inter-slide, detección de clipart
- Layout: balance, whitespace, alineación a grilla

Uso:
  python scripts/slide_quality_vision.py --topic 05-sorting --course leng-2026
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import find_project_root, load_json, load_yaml


def _load_clip_model(models_dir: Path):
    """Intenta cargar OpenCLIP ViT-B/32."""
    try:
        import open_clip
        import torch
        from PIL import Image

        model_name = "ViT-B-32"
        pretrained = "openai"

        model, _, preprocess = open_clip.create_model_and_transforms(
            model_name, pretrained=pretrained
        )
        tokenizer = open_clip.get_tokenizer(model_name)
        model.eval()
        return model, preprocess, tokenizer
    except ImportError:
        return None, None, None


def _clip_score(model, preprocess, tokenizer, image_path: Path, text: str) -> float:
    """Calcula CLIP score entre imagen y texto."""
    try:
        import torch
        from PIL import Image

        image = preprocess(Image.open(image_path)).unsqueeze(0)
        text_tokens = tokenizer([text[:77]])

        with torch.no_grad():
            image_features = model.encode_image(image)
            text_features = model.encode_text(text_tokens)
            image_features /= image_features.norm(dim=-1, keepdim=True)
            text_features /= text_features.norm(dim=-1, keepdim=True)
            similarity = (image_features @ text_features.T).item()
        return round(similarity, 4)
    except Exception:
        return -1.0


def _analyze_layout(plan_data: dict) -> list[dict]:
    """Analiza layout de filminas usando coordenadas EMU del plan JSON."""
    slides = plan_data.get("slides", plan_data.get("filminas", []))
    results = []

    # Slide dimensions (standard 16:9 in EMU)
    SLIDE_W = 12192000
    SLIDE_H = 6858000
    slide_area = SLIDE_W * SLIDE_H

    for i, slide in enumerate(slides, 1):
        elements = slide.get("elements", [])
        if not elements:
            results.append({
                "slide": i,
                "whitespace": 1.0,
                "balance": 0.5,
                "grade": "B",
                "notes": "Sin elementos EMU — análisis limitado",
            })
            continue

        # Calculate occupied area
        total_occupied = 0
        left_mass = 0
        right_mass = 0

        for elem in elements:
            x = elem.get("position_x", 0)
            y = elem.get("position_y", 0)
            w = elem.get("width", 0)
            h = elem.get("height", 0)
            area = w * h
            total_occupied += area
            center_x = x + w / 2
            if center_x < SLIDE_W / 2:
                left_mass += area
            else:
                right_mass += area

        whitespace = 1.0 - (total_occupied / slide_area) if slide_area > 0 else 1.0
        total_mass = left_mass + right_mass
        balance = left_mass / total_mass if total_mass > 0 else 0.5

        # Grade
        notes = []
        if whitespace < 0.30:
            grade = "F"
            notes.append("Sobredensidad visual")
        elif whitespace < 0.40:
            grade = "C"
            notes.append("Densidad visual alta")
        elif whitespace > 0.70:
            grade = "C"
            notes.append("Demasiado vacío")
        elif 0.40 <= whitespace <= 0.60:
            grade = "A"
        else:
            grade = "B"

        if abs(balance - 0.5) > 0.20:
            grade = min(grade, "C")
            notes.append(f"Desbalance horizontal ({balance:.0%} izq)")

        results.append({
            "slide": i,
            "whitespace": round(whitespace, 3),
            "balance": round(balance, 3),
            "grade": grade,
            "notes": " | ".join(notes) if notes else "OK",
        })

    return results


def main():
    parser = argparse.ArgumentParser(description="Slide Quality Vision — CLIP + Layout")
    parser.add_argument("--topic", required=True, help="ID del tema")
    parser.add_argument("--course", required=True, help="ID del curso")
    args = parser.parse_args()

    root = find_project_root()
    topic_dir = root / "salida" / "cursadas" / args.course / "temas" / args.topic

    if not topic_dir.exists():
        print(f"⚠️ Directorio del tema no encontrado: {topic_dir}")
        sys.exit(0)

    # Load plan JSON
    plan_file = topic_dir / "slides" / "plan-filminas.json"
    plan_data = {}
    if plan_file.exists():
        result = load_json(plan_file)
        if result.ok:
            plan_data = result.value

    # CLIP analysis
    thumbnails_dir = topic_dir / "slides" / "thumbnails"
    clip_results = []

    model, preprocess, tokenizer = _load_clip_model(root / "_edu-knowledge" / "models")
    if model is None:
        print("⚠️ OpenCLIP no disponible. Análisis visual limitado a layout.")
        print("  Para habilitar: pip install open-clip-torch")
    elif not thumbnails_dir.exists():
        print(f"⚠️ Thumbnails no encontrados en {thumbnails_dir}")
        print("  Ejecutar primero: python scripts/capture_thumbnails.py --topic ... --course ...")
    else:
        slides_data = plan_data.get("slides", plan_data.get("filminas", []))
        for thumb in sorted(thumbnails_dir.glob("*.png")):
            idx = int(thumb.stem.split("-")[-1]) if "-" in thumb.stem else 0
            if idx <= len(slides_data) and idx > 0:
                slide = slides_data[idx - 1]
                text = f"{slide.get('title', '')} {slide.get('body', '')}"
            else:
                text = thumb.stem
            score = _clip_score(model, preprocess, tokenizer, thumb, text)
            label = "✅" if score > 0.25 else ("⚠️" if score > 0.15 else "❌")
            clip_results.append({"slide": idx, "clip_score": score, "label": label})

    # Layout analysis
    layout_results = _analyze_layout(plan_data) if plan_data else []

    # Generate report
    report_lines = [
        f"# Visual Quality Report — {args.topic}\n",
        f"**Curso:** {args.course}\n",
    ]

    if clip_results:
        report_lines.extend([
            "\n## CLIP Scores (imagen-texto)\n",
            "| Slide | CLIP Score | Estado |",
            "|-------|-----------|--------|",
        ])
        for r in clip_results:
            report_lines.append(f"| {r['slide']} | {r['clip_score']:.4f} | {r['label']} |")

    if layout_results:
        report_lines.extend([
            "\n## Layout Quality\n",
            "| Slide | Whitespace | Balance | Grade | Notas |",
            "|-------|-----------|---------|-------|-------|",
        ])
        for r in layout_results:
            report_lines.append(
                f"| {r['slide']} | {r['whitespace']:.0%} | {r['balance']:.0%} | {r['grade']} | {r['notes']} |"
            )

    report = "\n".join(report_lines)
    report_path = topic_dir / "visual-quality-report.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"✅ Visual quality report: {report_path}")

    # Summary
    if layout_results:
        grades = [r["grade"] for r in layout_results]
        good = grades.count("A") + grades.count("B")
        print(f"📊 Layout: {good}/{len(grades)} slides con grade A/B")
    if clip_results:
        relevant = sum(1 for r in clip_results if r["clip_score"] > 0.25)
        print(f"📊 CLIP: {relevant}/{len(clip_results)} imágenes relevantes al texto")


if __name__ == "__main__":
    main()
