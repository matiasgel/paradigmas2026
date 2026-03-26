#!/usr/bin/env python3
"""
validate_accessibility.py — Validador de accesibilidad WCAG para filminas (S1.1)

Valida que las filminas cumplan criterios de accesibilidad:
- Contraste de colores (WCAG AA 4.5:1, AAA 7:1)
- Tamaño tipográfico mínimo según distancia de aula
- Presencia de alt_text en filminas con imágenes

Solo lectura — no modifica ningún archivo existente.
No tiene dependencias externas (solo stdlib).

Uso:
    python scripts/validate_accessibility.py --topic 01-intro --course leng-2026
    python scripts/validate_accessibility.py <topic_folder>

Exit codes:
    0 — reporte generado (o feature desactivada)
    1 — error de entrada (topic no encontrado, plan no existe)
"""
from __future__ import annotations

import argparse
import colorsys
import json
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_plan, find_project_root, load_json, load_yaml


# ═══════════════════════════════════════════════════════════════════════
# WCAG CONTRAST CALCULATION (WCAG 2.1 §1.4.3 / §1.4.6)
# ═══════════════════════════════════════════════════════════════════════


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convierte #RRGGBB o #RGB a (R, G, B) 0-255."""
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = h[0] * 2 + h[1] * 2 + h[2] * 2
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _relative_luminance(r: int, g: int, b: int) -> float:
    """Calcula luminancia relativa WCAG 2.1 (fórmula sRGB linearizada)."""
    def _linearize(c: int) -> float:
        s = c / 255.0
        return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4

    return 0.2126 * _linearize(r) + 0.7152 * _linearize(g) + 0.0722 * _linearize(b)


def contrast_ratio(color1: str, color2: str) -> float:
    """Calcula ratio de contraste WCAG entre dos colores hex."""
    l1 = _relative_luminance(*_hex_to_rgb(color1))
    l2 = _relative_luminance(*_hex_to_rgb(color2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def grade_contrast(ratio: float, large_text: bool = False) -> str:
    """Clasifica el contraste según WCAG 2.1."""
    if large_text:
        if ratio >= 4.5:
            return "AAA"
        if ratio >= 3.0:
            return "AA"
        return "F"
    else:
        if ratio >= 7.0:
            return "AAA"
        if ratio >= 4.5:
            return "AA"
        return "F"


# ═══════════════════════════════════════════════════════════════════════
# TAMAÑO TIPOGRÁFICO (distancia de aula)
# ═══════════════════════════════════════════════════════════════════════


def min_font_size_pt(distance_meters: float, resolution: str = "1080p") -> float:
    """Tamaño mínimo de fuente en pt para que el texto sea legible a distancia.

    Base: regla de 1/150 del ancho de proyección (ISO 3864-1 adaptada).
    Un proyector Full HD a 6m con pantalla de 2m ancho → ~0.013m por carácter
    → ~37pt mínimo para texto de cuerpo.
    """
    # Ancho típico de proyección según distancia (throw ratio ~1.5:1)
    screen_width_m = distance_meters / 1.5
    # Resolución horizontal
    h_pixels = {"720p": 1280, "1080p": 1920, "4k": 3840}.get(resolution, 1920)
    # Un carácter debe ocupar al menos 1/100 del ancho de pantalla
    char_width_m = screen_width_m / 100
    # Convertir metros de carácter a puntos (1pt = 0.000352778m)
    return char_width_m / 0.000352778


# ═══════════════════════════════════════════════════════════════════════
# VALIDACIÓN
# ═══════════════════════════════════════════════════════════════════════


def validate_palette_contrast(slides_config: dict) -> list[dict]:
    """Valida contrastes entre pares de colores del sistema de diseño."""
    palette = slides_config.get("palette", {})
    bg = palette.get("background", "#FFFFFF")
    results = []

    pairs = [
        ("text", "background", False),
        ("primary", "background", True),   # títulos = texto grande
        ("secondary", "primary", True),     # subtítulos sobre fondo primario
        ("accent", "background", False),
    ]

    for fg_key, bg_key, large in pairs:
        fg_color = palette.get(fg_key)
        bg_color = palette.get(bg_key, bg)
        if not fg_color or not bg_color:
            continue

        ratio = contrast_ratio(fg_color, bg_color)
        grade = grade_contrast(ratio, large_text=large)
        results.append({
            "pair": f"{fg_key} sobre {bg_key}",
            "fg": fg_color,
            "bg": bg_color,
            "ratio": round(ratio, 2),
            "grade": grade,
            "large_text": large,
        })

    return results


def validate_slides_alt_text(slides: list[dict]) -> list[dict]:
    """Verifica que filminas con imagen tengan alt_text no vacío."""
    issues = []
    for slide in slides:
        image = slide.get("image", {})
        has_image = (
            image.get("image_layer", "none") != "none"
            or image.get("prompt", "")
        )
        if has_image:
            alt = image.get("alt_text", "")
            if not alt or not alt.strip():
                issues.append({
                    "slide_id": slide.get("id", "?"),
                    "title": slide.get("title", ""),
                    "issue": "Filmina con imagen pero sin alt_text",
                    "severity": "AA",
                })
    return issues


def validate_font_sizes(slides_config: dict, distance_m: float,
                        resolution: str = "1080p") -> list[dict]:
    """Verifica que los tamaños de fuente sean legibles a la distancia dada."""
    min_size = min_font_size_pt(distance_m, resolution)
    issues = []

    typography = slides_config.get("typography", {})
    for zone_name, zone_cfg in typography.items():
        size = zone_cfg.get("size", 0)
        if size and size < min_size:
            issues.append({
                "zone": zone_name,
                "current_size": size,
                "min_recommended": round(min_size, 1),
                "distance_m": distance_m,
                "issue": f"Fuente {zone_name} ({size}pt) menor que mínimo recomendado ({round(min_size, 1)}pt) a {distance_m}m",
            })

    return issues


# ═══════════════════════════════════════════════════════════════════════
# REPORTE
# ═══════════════════════════════════════════════════════════════════════


def generate_report(contrast_results: list[dict],
                    alt_issues: list[dict],
                    font_issues: list[dict],
                    topic_id: str) -> str:
    """Genera reporte Markdown de accesibilidad."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Reporte de Accesibilidad — {topic_id}",
        f"**Generado:** {now}",
        f"**Estándar:** WCAG 2.1 Level AA",
        "",
        "## Contraste de Colores",
        "",
        "| Par | FG | BG | Ratio | Grade | Texto Grande |",
        "|-----|----|----|-------|-------|--------------|",
    ]

    all_pass = True
    for r in contrast_results:
        emoji = "✅" if r["grade"] != "F" else "❌"
        if r["grade"] == "F":
            all_pass = False
        lines.append(
            f"| {r['pair']} | `{r['fg']}` | `{r['bg']}` | "
            f"{r['ratio']}:1 | {emoji} {r['grade']} | "
            f"{'Sí' if r['large_text'] else 'No'} |"
        )

    lines.extend(["", "## Alt Text en Imágenes", ""])
    if alt_issues:
        all_pass = False
        lines.append("| Slide | Título | Problema |")
        lines.append("|-------|--------|----------|")
        for issue in alt_issues:
            lines.append(
                f"| {issue['slide_id']} | {issue['title']} | ❌ {issue['issue']} |"
            )
    else:
        lines.append("✅ Todas las filminas con imagen tienen `alt_text`.")

    lines.extend(["", "## Tamaño Tipográfico", ""])
    if font_issues:
        all_pass = False
        lines.append("| Zona | Actual | Mínimo | Distancia |")
        lines.append("|------|--------|--------|-----------|")
        for issue in font_issues:
            lines.append(
                f"| {issue['zone']} | {issue['current_size']}pt | "
                f"{issue['min_recommended']}pt | {issue['distance_m']}m |"
            )
    else:
        lines.append("✅ Todos los tamaños de fuente cumplen el mínimo recomendado.")

    lines.extend([
        "",
        "## Resultado Global",
        "",
        f"**{'✅ PASA' if all_pass else '⚠️ REQUIERE ATENCIÓN'}**",
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
        description="Validador de accesibilidad WCAG para filminas EDU"
    )
    parser.add_argument("topic_folder", nargs="?", help="Carpeta del tema (path directo)")
    parser.add_argument("--topic", help="ID del tema (ej: 01-intro)")
    parser.add_argument("--course", help="Prefijo del curso (ej: leng-2026)")
    args = parser.parse_args()

    if not args.topic_folder and not args.topic:
        parser.error("Especificar topic_folder o --topic")

    project_root = find_project_root(Path(__file__).parent)

    # Verificar si está habilitado
    edu_config_path = project_root / "_edu" / "config.yaml"
    edu_config = load_yaml(edu_config_path) if edu_config_path.exists() else {}
    if not edu_config.get("accessibility_check_enabled", False):
        print("ℹ️  Accesibilidad desactivada. Activar con accessibility_check_enabled: true en config.yaml")
        sys.exit(0)

    topic_folder = resolve_topic_folder(args, project_root)
    if not topic_folder.exists():
        print(f"ERROR: Carpeta de tema no encontrada: {topic_folder}", file=sys.stderr)
        sys.exit(1)

    # Cargar slides-config.yaml
    slides_config_path = project_root / "_edu" / "slides-config.yaml"
    slides_config = load_yaml(slides_config_path) if slides_config_path.exists() else {}

    # Cargar plan JSON del tema
    plan_result = find_plan(topic_folder)
    slides = []
    if plan_result.is_ok:
        plan = load_json(plan_result.unwrap())
        slides = plan.get("slides", [])
    else:
        print(f"AVISO: No se encontró plan JSON — solo se validará paleta y tipografía.")

    # Validaciones
    contrast_results = validate_palette_contrast(slides_config)
    alt_issues = validate_slides_alt_text(slides)

    # Tamaño tipográfico (solo si hay distancia configurada)
    distance_m = edu_config.get("classroom_distance_meters", 0)
    resolution = edu_config.get("screen_resolution", "1080p")
    font_issues = []
    if distance_m > 0:
        font_issues = validate_font_sizes(slides_config, distance_m, resolution)

    # Generar reporte
    topic_id = topic_folder.name
    report = generate_report(contrast_results, alt_issues, font_issues, topic_id)

    output_path = topic_folder / "accessibility-report.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"✅ Reporte generado: {output_path}")


if __name__ == "__main__":
    main()
