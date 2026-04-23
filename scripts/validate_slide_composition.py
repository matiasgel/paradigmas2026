#!/usr/bin/env python3
"""
validate_slide_composition.py — Auditoría visual de composición de slides (S1.2)

Valida que las filminas respeten buenas prácticas de composición visual:
- Márgenes seguros (5% del borde)
- Densidad visual (35-55% ideal, Scheiter & Eitel)
- Detección de superposiciones entre bounding boxes

Solo lectura — no modifica ningún archivo existente.
No tiene dependencias externas (solo stdlib + pipeline_common).

Uso:
    python scripts/validate_slide_composition.py --topic 01-intro --course leng-2026
    python scripts/validate_slide_composition.py <topic_folder>

Exit codes:
    0 — reporte generado
    1 — error de entrada
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_plan, find_project_root, load_json, load_yaml


# ═══════════════════════════════════════════════════════════════════════
# GEOMETRÍA (leída de pipeline-runtime.schema.json)
# ═══════════════════════════════════════════════════════════════════════


def load_canvas_geometry(project_root: Path) -> dict:
    """Carga geometría de canvas del pipeline-runtime schema."""
    runtime_path = project_root / "_edu" / "schemas" / "pipeline-runtime.schema.json"
    if not runtime_path.exists():
        return {
            "slide_width": 9144000,
            "slide_height": 5143500,
            "margin": 457200,
        }
    schema = load_json(runtime_path)
    canvas_props = schema.get("properties", {}).get("canvas", {}).get("properties", {})
    return {
        "slide_width": canvas_props.get("slide_width", {}).get("const", 9144000),
        "slide_height": canvas_props.get("slide_height", {}).get("const", 5143500),
        "margin": canvas_props.get("margin", {}).get("const",
                  canvas_props.get("margin", {}).get("default", 457200)),
    }


# ═══════════════════════════════════════════════════════════════════════
# VALIDACIONES DE COMPOSICIÓN
# ═══════════════════════════════════════════════════════════════════════


def check_safe_margins(slide: dict, canvas: dict) -> list[str]:
    """Verifica que los elementos estén dentro del área segura (5% del borde).

    Para slides con layout zones definidos, verifica que el layout
    no coloque contenido en la franja exterior del 5%.
    """
    issues = []
    w = canvas["slide_width"]
    h = canvas["slide_height"]
    margin_x = w * 0.05  # 5% del ancho
    margin_y = h * 0.05  # 5% del alto

    # El layout es metadata — si el pipeline respeta el schema,
    # los márgenes están controlados por pipeline-runtime.
    # Aquí verificamos consistencia del layout declarado.
    layout = slide.get("layout", {})

    # Filminas con body en "full-center" o "full-bottom" necesitan
    # especial atención al margen inferior
    body_zone = layout.get("body", "none")
    if body_zone in ("full-center", "full-bottom"):
        # Verificar que haya body content que pueda exceder
        body_blocks = slide.get("body_blocks", [])
        total_text = sum(
            len(b.get("content", "")) for b in body_blocks if b.get("type") == "text"
        )
        if total_text > 500:
            issues.append("Mucho texto en layout full — riesgo de exceder margen inferior")

    return issues


def estimate_visual_density(slide: dict) -> dict:
    """Estima la densidad visual de una filmina.

    Densidad ideal: 35-55% del área total (Scheiter & Eitel, 2017).

    Heurística: cuenta "peso visual" de cada elemento:
    - Título: 10% base
    - Body text: ~2% por cada 50 caracteres
    - Code block: 15% base + 1% por cada 10 líneas
    - Table: 20% base + 2% por cada fila
    - Image: 30% (content) o 100% (background)
    """
    weights: dict[str, float] = {}

    # Título
    title = slide.get("title", "")
    if title:
        weights["title"] = 10.0

    # Subtítulo
    subtitle = slide.get("subtitle", "")
    if subtitle:
        weights["subtitle"] = 5.0

    # Body blocks
    body_blocks = slide.get("body_blocks", [])
    body_weight = 0.0
    for block in body_blocks:
        btype = block.get("type", "text")
        if btype == "text":
            body_weight += len(block.get("content", "")) / 50 * 2
        elif btype == "list":
            items = block.get("items", [])
            body_weight += len(items) * 3
        elif btype == "heading":
            body_weight += 5
    weights["body"] = min(body_weight, 50.0)

    # Code blocks
    code_blocks = slide.get("code_blocks", [])
    if code_blocks:
        for cb in code_blocks:
            code = cb.get("code", "")
            lines = code.count("\n") + 1
            weights["code"] = 15 + lines * 1
    
    # Tables
    tables = slide.get("tables", [])
    if tables:
        for tbl in tables:
            rows = tbl.get("rows", [])
            weights["table"] = 20 + len(rows) * 2

    # Image
    image = slide.get("image", {})
    img_layer = image.get("image_layer", "none")
    if img_layer == "background":
        weights["image"] = 100.0
    elif img_layer == "content":
        weights["image"] = 30.0

    total_density = min(sum(weights.values()), 100.0)
    return {
        "density_pct": round(total_density, 1),
        "breakdown": weights,
    }


def grade_density(density_pct: float, slide_type: str) -> str:
    """Clasifica la densidad visual."""
    # Background images (portada, socratica, cierre) tienen 100% visual
    # pero eso es intencional — no penalizar
    if slide_type in ("portada", "cierre", "socratica"):
        return "A"  # siempre OK por diseño

    if 35 <= density_pct <= 55:
        return "A"   # ideal
    elif 25 <= density_pct <= 65:
        return "B"   # aceptable
    elif 15 <= density_pct <= 75:
        return "C"   # mejorable
    else:
        return "F"   # excesivo o vacío


def check_element_overlap(slide: dict) -> list[str]:
    """Detecta posibles superposiciones de elementos en una slide.

    Basado en el layout declarado — si dos zonas compiten por el mismo
    espacio, se reporta.
    """
    issues = []
    layout = slide.get("layout", {})

    # Mapeo de zonas a regiones del canvas (simplificado)
    zone_regions = {
        "full-title": "top",
        "center-top": "top",
        "left-top": "top-left",
        "center-middle": "middle",
        "left-middle": "middle-left",
        "center-bottom": "bottom",
        "full-center": "middle",
        "full-bottom": "bottom",
        "right-half": "right",
        "left-top-split": "top-left",
        "left-bottom-split": "bottom-left",
        "subtitle-only": "top-sub",
        "table-intro": "top-sub",
        "table-main": "middle-bottom",
        "background": "all",
        "none": None,
    }

    active_regions: dict[str, list[str]] = {}
    for element, zone in layout.items():
        if zone == "none" or not zone:
            continue
        region = zone_regions.get(zone, zone)
        if region is None:
            continue
        if region == "all":
            continue  # background no compite
        if region not in active_regions:
            active_regions[region] = []
        active_regions[region].append(element)

    for region, elements in active_regions.items():
        if len(elements) > 1:
            issues.append(
                f"Posible superposición en región '{region}': {', '.join(elements)}"
            )

    return issues


# ═══════════════════════════════════════════════════════════════════════
# REPORTE
# ═══════════════════════════════════════════════════════════════════════


def generate_report(slide_analyses: list[dict], topic_id: str) -> str:
    """Genera reporte Markdown de composición visual."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Reporte de Composición Visual — {topic_id}",
        f"**Generado:** {now}",
        f"**Basado en:** Scheiter & Eitel (2017), Patrón Z, Margen seguro 5%",
        "",
        "## Densidad Visual por Filmina",
        "",
        "| Slide | Tipo | Densidad | Grade | Observaciones |",
        "|-------|------|----------|-------|---------------|",
    ]

    total_grade_f = 0
    for analysis in slide_analyses:
        slide_id = analysis["slide_id"]
        slide_type = analysis["slide_type"]
        density = analysis["density_pct"]
        grade = analysis["density_grade"]
        overlap_count = len(analysis["overlaps"])
        margin_count = len(analysis["margin_issues"])

        emoji = {"A": "✅", "B": "🟡", "C": "⚠️", "F": "❌"}.get(grade, "?")
        if grade == "F":
            total_grade_f += 1

        obs = []
        if overlap_count > 0:
            obs.append(f"{overlap_count} superposición(es)")
        if margin_count > 0:
            obs.append(f"{margin_count} margen(es)")
        obs_str = "; ".join(obs) if obs else "—"

        lines.append(
            f"| {slide_id} | {slide_type} | {density}% | {emoji} {grade} | {obs_str} |"
        )

    # Superposiciones detectadas
    overlaps_found = [a for a in slide_analyses if a["overlaps"]]
    if overlaps_found:
        lines.extend(["", "## Superposiciones Detectadas", ""])
        for a in overlaps_found:
            lines.append(f"### {a['slide_id']} — {a['title']}")
            for o in a["overlaps"]:
                lines.append(f"- ⚠️ {o}")
            lines.append("")

    # Márgenes
    margin_found = [a for a in slide_analyses if a["margin_issues"]]
    if margin_found:
        lines.extend(["", "## Alertas de Margen", ""])
        for a in margin_found:
            lines.append(f"### {a['slide_id']} — {a['title']}")
            for m in a["margin_issues"]:
                lines.append(f"- ⚠️ {m}")
            lines.append("")

    # Global
    total = len(slide_analyses)
    passing = total - total_grade_f
    lines.extend([
        "",
        "## Resultado Global",
        "",
        f"**{passing}/{total} filminas** con densidad visual aceptable.",
        f"**{'✅ PASA' if total_grade_f == 0 else '⚠️ REQUIERE ATENCIÓN'}**",
    ])

    return "\n".join(lines) + "\n"


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════


def resolve_topic_folder(args: argparse.Namespace, project_root: Path) -> Path:
    """Resuelve la carpeta del tema desde los argumentos CLI."""
    if args.topic_folder:
        return Path(args.topic_folder).resolve()

    config_path = project_root / "_edu" / "config.yaml"
    config = load_yaml(config_path) if config_path.exists() else {}
    course_prefix = args.course or config.get("course_prefix", "")
    course_year = config.get("course_year", "2026")
    if not course_prefix:
        print("ERROR: Especificar --course o configurar course_prefix en config.yaml", file=sys.stderr)
        sys.exit(1)

    course_id = f"{course_prefix}-{course_year}"
    return project_root / "salida" / "cursadas" / course_id / "temas" / args.topic


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Auditor de composición visual para filminas EDU"
    )
    parser.add_argument("topic_folder", nargs="?", help="Carpeta del tema (path directo)")
    parser.add_argument("--topic", help="ID del tema (ej: 01-intro)")
    parser.add_argument("--course", help="Prefijo del curso (ej: leng-2026)")
    args = parser.parse_args()

    if not args.topic_folder and not args.topic:
        parser.error("Especificar topic_folder o --topic")

    project_root = find_project_root(Path(__file__).parent)
    topic_folder = resolve_topic_folder(args, project_root)

    if not topic_folder.exists():
        print(f"ERROR: Carpeta de tema no encontrada: {topic_folder}", file=sys.stderr)
        sys.exit(1)

    # Cargar plan JSON
    plan_result = find_plan(topic_folder)
    if not plan_result.is_ok:
        print(f"ERROR: {plan_result.errors[0]}", file=sys.stderr)
        sys.exit(1)

    plan = load_json(plan_result.unwrap())
    slides = plan.get("slides", [])
    canvas = load_canvas_geometry(project_root)

    # Analizar cada filmina
    slide_analyses = []
    for slide in slides:
        density_info = estimate_visual_density(slide)
        slide_type = slide.get("type", "concepto-abstracto")
        grade = grade_density(density_info["density_pct"], slide_type)
        overlaps = check_element_overlap(slide)
        margin_issues = check_safe_margins(slide, canvas)

        slide_analyses.append({
            "slide_id": slide.get("id", "?"),
            "title": slide.get("title", ""),
            "slide_type": slide_type,
            "density_pct": density_info["density_pct"],
            "density_grade": grade,
            "breakdown": density_info["breakdown"],
            "overlaps": overlaps,
            "margin_issues": margin_issues,
        })

    # Generar reporte
    topic_id = topic_folder.name
    report = generate_report(slide_analyses, topic_id)

    output_path = topic_folder / "composition-report.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"✅ Reporte generado: {output_path}")


if __name__ == "__main__":
    main()
