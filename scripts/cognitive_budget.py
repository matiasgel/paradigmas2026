#!/usr/bin/env python3
"""
cognitive_budget.py — Calculador de presupuesto cognitivo por clase (S4.2)

Analiza la secuencia de filminas de un tema y produce un reporte de
carga cognitiva acumulada, ideal para detectar agotamiento antes de
dar la clase.

Puede trabajar directamente con filminas.md (no requiere plan JSON).
Sin dependencias externas.

Uso:
    python scripts/cognitive_budget.py --topic 01-intro --course leng-2026
    python scripts/cognitive_budget.py <topic_folder>

Exit codes:
    0 — reporte generado
    1 — error de entrada
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_plan, find_project_root, load_json, load_yaml


# ═══════════════════════════════════════════════════════════════════════
# MODELO DE CARGA COGNITIVA
# ═══════════════════════════════════════════════════════════════════════
# Basado en: Chen & Sweller (2023), Cognitive Load Theory.
# Las filminas se clasifican por "peso cognitivo" que simula la
# demanda de working memory acumulada.

COGNITIVE_WEIGHT = {
    # Tipo → peso base (1-10) donde 10 = máxima demanda cognitiva
    "portada": 1,
    "concepto-abstracto": 6,
    "concepto-mixto": 7,
    "codigo": 8,
    "tabla": 5,
    "tabla-comparativa": 6,
    "tabla-mixta": 7,
    "diagrama": 5,
    "socratica": 3,      # Attention reset — reduce carga
    "demo": 4,           # Práctica activa — moderado
    "cierre": 2,
    "timeline": 4,
}

# Modificadores
MODIFIER_LONG_TEXT = 1.5       # Body > 40 palabras
MODIFIER_DENSE_CODE = 2.0     # Code > 20 líneas
MODIFIER_REPETITION = -1.0    # Concepto que ya se vio antes (interleavig)
MODIFIER_RESET = -3.0         # Socrática/demo tras teoría pesada

# Umbrales
FATIGUE_THRESHOLD = 50         # Carga acumulada donde la atención cae
CRITICAL_THRESHOLD = 75        # Riesgo alto de sobrecarga
AVG_MINUTES_PER_SLIDE = 2.0   # Estimación conservadora


# ═══════════════════════════════════════════════════════════════════════
# ANÁLISIS DESDE PLAN JSON
# ═══════════════════════════════════════════════════════════════════════


def analyze_from_plan(slides: list[dict]) -> list[dict]:
    """Analiza carga cognitiva desde plan JSON."""
    results = []
    cumulative = 0.0

    for i, slide in enumerate(slides):
        stype = slide.get("type", "concepto-abstracto")
        base_weight = COGNITIVE_WEIGHT.get(stype, 5)

        # Modificadores
        modifier = 0.0

        # Body largo
        total_words = 0
        for block in slide.get("body_blocks", []):
            if block.get("type") == "text":
                total_words += len(block.get("content", "").split())
            elif block.get("type") == "list":
                for item in block.get("items", []):
                    total_words += len(item.get("content", "").split())
        if total_words > 40:
            modifier += MODIFIER_LONG_TEXT

        # Código denso
        for cb in slide.get("code_blocks", []):
            code_lines = cb.get("code", "").count("\n") + 1
            if code_lines > 20:
                modifier += MODIFIER_DENSE_CODE

        # Attention reset
        if stype in ("socratica", "demo") and i > 0:
            prev_type = slides[i - 1].get("type", "")
            if prev_type in ("concepto-abstracto", "concepto-mixto", "codigo"):
                modifier += MODIFIER_RESET

        effective = max(1, base_weight + modifier)
        cumulative += effective
        time_min = round((i + 1) * AVG_MINUTES_PER_SLIDE)

        results.append({
            "index": i + 1,
            "slide_id": slide.get("id", f"S-{i+1:02d}"),
            "type": stype,
            "title": slide.get("title", "")[:50],
            "base_weight": base_weight,
            "modifier": round(modifier, 1),
            "effective": round(effective, 1),
            "cumulative": round(cumulative, 1),
            "time_min": time_min,
            "zone": (
                "🟢 OK" if cumulative < FATIGUE_THRESHOLD
                else "🟡 Fatiga" if cumulative < CRITICAL_THRESHOLD
                else "🔴 Sobrecarga"
            ),
        })

    return results


# ═══════════════════════════════════════════════════════════════════════
# ANÁLISIS DESDE filminas.md (fallback)
# ═══════════════════════════════════════════════════════════════════════


def analyze_from_filminas_md(filminas_path: Path) -> list[dict]:
    """Analiza carga cognitiva directamente desde filminas.md."""
    content = filminas_path.read_text(encoding="utf-8")
    
    # Dividir por separador de filmina
    raw_slides = re.split(r"\n---\n", content)
    results = []
    cumulative = 0.0

    type_patterns = {
        r"tipo:\s*concepto": "concepto-abstracto",
        r"tipo:\s*codigo|```": "codigo",
        r"tipo:\s*socr[aá]tica|\?": "socratica",
        r"tipo:\s*tabla|\|.*\|": "tabla",
        r"tipo:\s*diagrama": "diagrama",
        r"tipo:\s*demo": "demo",
        r"tipo:\s*portada": "portada",
        r"tipo:\s*cierre": "cierre",
    }

    for i, raw in enumerate(raw_slides):
        if not raw.strip():
            continue

        # Detectar tipo
        stype = "concepto-abstracto"  # default
        for pattern, detected_type in type_patterns.items():
            if re.search(pattern, raw, re.IGNORECASE):
                stype = detected_type
                break

        # Extraer título
        title_match = re.search(r"^#{1,3}\s+(.+)$", raw, re.MULTILINE)
        title = title_match.group(1)[:50] if title_match else f"Filmina {i+1}"

        base_weight = COGNITIVE_WEIGHT.get(stype, 5)
        word_count = len(raw.split())

        modifier = 0.0
        if word_count > 80:
            modifier += MODIFIER_LONG_TEXT
        if stype in ("socratica", "demo") and i > 0:
            modifier += MODIFIER_RESET

        effective = max(1, base_weight + modifier)
        cumulative += effective
        time_min = round((i + 1) * AVG_MINUTES_PER_SLIDE)

        results.append({
            "index": i + 1,
            "slide_id": f"F-{i:02d}",
            "type": stype,
            "title": title,
            "base_weight": base_weight,
            "modifier": round(modifier, 1),
            "effective": round(effective, 1),
            "cumulative": round(cumulative, 1),
            "time_min": time_min,
            "zone": (
                "🟢 OK" if cumulative < FATIGUE_THRESHOLD
                else "🟡 Fatiga" if cumulative < CRITICAL_THRESHOLD
                else "🔴 Sobrecarga"
            ),
        })

    return results


# ═══════════════════════════════════════════════════════════════════════
# REPORTE
# ═══════════════════════════════════════════════════════════════════════


def generate_report(analyses: list[dict], topic_id: str,
                    total_minutes: int) -> str:
    """Genera reporte Markdown de presupuesto cognitivo."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        f"# Presupuesto Cognitivo — {topic_id}",
        f"**Generado:** {now}",
        f"**Basado en:** Chen & Sweller (2023), Cognitive Load Theory",
        f"**Filminas:** {len(analyses)} | **Tiempo estimado:** ~{total_minutes} min",
        "",
        "## Curva de Carga Cognitiva",
        "",
        "```",
    ]

    # ASCII art de la curva
    if analyses:
        max_cum = max(a["cumulative"] for a in analyses)
        scale = 40 / max(max_cum, 1)
        for a in analyses:
            bar_len = round(a["cumulative"] * scale)
            bar = "█" * bar_len
            zone_marker = ""
            if a["cumulative"] >= CRITICAL_THRESHOLD:
                zone_marker = " ← 🔴"
            elif a["cumulative"] >= FATIGUE_THRESHOLD:
                zone_marker = " ← 🟡"
            lines.append(f"  {a['slide_id']:>6} |{bar}{zone_marker}")

        lines.append(f"         {'─' * 42}")
        lines.append(f"         0{'─' * 10}Fatiga{'─' * 8}Sobrecarga{'─' * 7}")
    lines.append("```")

    # Tabla detallada
    lines.extend([
        "",
        "## Detalle por Filmina",
        "",
        "| # | ID | Tipo | Título | Peso | Mod | Efect | Acum | Min | Zona |",
        "|---|-----|------|--------|------|-----|-------|------|-----|------|",
    ])

    for a in analyses:
        lines.append(
            f"| {a['index']} | {a['slide_id']} | {a['type']} | "
            f"{a['title']} | {a['base_weight']} | {a['modifier']:+.1f} | "
            f"{a['effective']} | {a['cumulative']} | {a['time_min']} | {a['zone']} |"
        )

    # Resumen
    fatigue_slide = next((a for a in analyses if a["cumulative"] >= FATIGUE_THRESHOLD), None)
    critical_slide = next((a for a in analyses if a["cumulative"] >= CRITICAL_THRESHOLD), None)

    lines.extend(["", "## Recomendaciones", ""])

    if critical_slide:
        lines.append(
            f"🔴 **Sobrecarga alcanzada** en {critical_slide['slide_id']} "
            f"(~min {critical_slide['time_min']}). "
            "Insertar pausa activa, demo o filmina socrática antes de este punto."
        )
    elif fatigue_slide:
        lines.append(
            f"🟡 **Fatiga esperada** a partir de {fatigue_slide['slide_id']} "
            f"(~min {fatigue_slide['time_min']}). "
            "Considerar un attention reset (demo, pregunta, pausa)."
        )
    else:
        lines.append("✅ La clase se mantiene dentro del presupuesto cognitivo ideal.")

    # Patrón U invertida
    if len(analyses) > 6:
        first_third = analyses[:len(analyses)//3]
        last_third = analyses[2*len(analyses)//3:]
        avg_first = sum(a["effective"] for a in first_third) / len(first_third)
        avg_last = sum(a["effective"] for a in last_third) / len(last_third)

        if avg_last > avg_first * 1.2:
            lines.append(
                "\n⚠️ **Patrón invertido:** La carga SUBE al final en vez de bajar. "
                "Idealmente la clase debe cerrar con intensidad decreciente (U invertida)."
            )
        else:
            lines.append(
                "\n✅ **Patrón correcto:** La intensidad disminuye hacia el cierre."
            )

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
        description="Calculador de presupuesto cognitivo para clases EDU"
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

    # Intentar plan JSON primero, fallback a filminas.md
    plan_result = find_plan(topic_folder)
    if plan_result.is_ok:
        plan = load_json(plan_result.unwrap())
        slides = plan.get("slides", [])
        analyses = analyze_from_plan(slides)
    else:
        filminas_path = topic_folder / "filminas.md"
        if filminas_path.exists():
            analyses = analyze_from_filminas_md(filminas_path)
        else:
            print(f"ERROR: No se encontró plan JSON ni filminas.md en {topic_folder}", file=sys.stderr)
            sys.exit(1)

    total_minutes = round(len(analyses) * AVG_MINUTES_PER_SLIDE)
    topic_id = topic_folder.name
    report = generate_report(analyses, topic_id, total_minutes)

    output_path = topic_folder / "cognitive-budget-report.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"✅ Reporte generado: {output_path}")


if __name__ == "__main__":
    main()
