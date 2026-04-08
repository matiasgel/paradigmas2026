#!/usr/bin/env python3
"""
generate_exam_blueprint.py — Generador de Blueprints de Examen (S2.2)

Genera una tabla de especificaciones (blueprint) para parciales con:
- Distribución ponderada de temas según tiempo dedicado en clase
- Distribución por niveles de Bloom (Recordar→Evaluar)
- Validación contra exam-blueprint.schema.json

No tiene dependencias externas (solo stdlib + pipeline_common).

Uso:
    python scripts/generate_exam_blueprint.py --course leng-2026 \
        --topics "01-intro,02-tipos,03-memoria" --points 100 --time 120
    python scripts/generate_exam_blueprint.py --course leng-2026 \
        --topics "01-intro,02-tipos" --points 100 --time 90 --bloom-profile research

Exit codes:
    0 — blueprint generado
    1 — error de entrada
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


# ═══════════════════════════════════════════════════════════════════════
# BLOOM TAXONOMY PROFILES
# ═══════════════════════════════════════════════════════════════════════

BLOOM_PROFILES = {
    "default": {
        "recordar": 0.20,
        "comprender": 0.30,
        "aplicar": 0.30,
        "analizar": 0.15,
        "evaluar": 0.05,
    },
    "practical": {
        "recordar": 0.10,
        "comprender": 0.20,
        "aplicar": 0.40,
        "analizar": 0.20,
        "evaluar": 0.10,
    },
    "research": {
        "recordar": 0.10,
        "comprender": 0.15,
        "aplicar": 0.25,
        "analizar": 0.30,
        "evaluar": 0.20,
    },
    "introductory": {
        "recordar": 0.30,
        "comprender": 0.35,
        "aplicar": 0.25,
        "analizar": 0.10,
        "evaluar": 0.00,
    },
}


# ═══════════════════════════════════════════════════════════════════════
# BLUEPRINT GENERATION
# ═══════════════════════════════════════════════════════════════════════


def estimate_topic_weight(topic_id: str, topic_folder: Path) -> float:
    """Estima el peso de un tema basado en la cantidad de contenido.

    Heurística: cuenta filminas si existe filminas.md, o usa peso uniforme.
    """
    filminas_path = topic_folder / "filminas.md"
    if filminas_path.exists():
        content = filminas_path.read_text(encoding="utf-8")
        # Contar separadores de filmina (---) como proxy de cantidad de slides
        slide_count = content.count("\n---\n") + 1
        return max(1.0, slide_count)

    # Si hay minuta, contar secciones
    minuta_path = topic_folder / "minuta.md"
    if minuta_path.exists():
        content = minuta_path.read_text(encoding="utf-8")
        sections = content.count("\n## ")
        return max(1.0, sections)

    return 1.0  # peso uniforme si no hay datos


def generate_blueprint(topics: list[str], total_points: int,
                       exam_time_min: int, bloom_profile: str,
                       project_root: Path, course_id: str) -> dict:
    """Genera el blueprint del examen."""
    bloom = BLOOM_PROFILES.get(bloom_profile, BLOOM_PROFILES["default"])

    # Calcular pesos por tema
    topic_weights: dict[str, float] = {}
    topics_base = project_root / "salida" / "cursadas" / course_id / "temas"

    for topic_id in topics:
        topic_folder = topics_base / topic_id
        topic_weights[topic_id] = estimate_topic_weight(topic_id, topic_folder)

    total_weight = sum(topic_weights.values())
    if total_weight == 0:
        total_weight = len(topics)
        topic_weights = {t: 1.0 for t in topics}

    # Distribuir puntos por tema (proporcional al peso)
    topic_points: dict[str, int] = {}
    remaining = total_points
    sorted_topics = sorted(topic_weights.items(), key=lambda x: x[1], reverse=True)

    for i, (topic_id, weight) in enumerate(sorted_topics):
        if i == len(sorted_topics) - 1:
            topic_points[topic_id] = remaining
        else:
            pts = round(total_points * weight / total_weight)
            topic_points[topic_id] = pts
            remaining -= pts

    # Construir matriz tema × bloom
    matrix: list[dict] = []
    for topic_id in topics:
        pts = topic_points[topic_id]
        bloom_dist: dict[str, int] = {}
        remaining_pts = pts
        bloom_items = list(bloom.items())

        for i, (level, pct) in enumerate(bloom_items):
            if i == len(bloom_items) - 1:
                bloom_dist[level] = remaining_pts
            else:
                level_pts = round(pts * pct)
                bloom_dist[level] = level_pts
                remaining_pts -= level_pts

        # Tiempo sugerido proporcional
        time_min = round(exam_time_min * topic_weights[topic_id] / total_weight)

        matrix.append({
            "topic_id": topic_id,
            "points": pts,
            "time_minutes": time_min,
            "bloom_distribution": bloom_dist,
            "weight_pct": round(100 * topic_weights[topic_id] / total_weight, 1),
        })

    # Resumen de Bloom totales
    bloom_totals: dict[str, int] = {}
    for level in bloom:
        bloom_totals[level] = sum(
            row["bloom_distribution"].get(level, 0) for row in matrix
        )

    blueprint = {
        "exam_blueprint_version": "1.0",
        "course_id": course_id,
        "generated_at": datetime.now().isoformat(),
        "parameters": {
            "total_points": total_points,
            "exam_time_minutes": exam_time_min,
            "bloom_profile": bloom_profile,
            "topic_count": len(topics),
        },
        "bloom_profile_used": bloom,
        "matrix": matrix,
        "bloom_totals": bloom_totals,
    }

    return blueprint


def blueprint_to_markdown(blueprint: dict) -> str:
    """Convierte un blueprint JSON a reporte Markdown legible."""
    params = blueprint["parameters"]
    lines = [
        f"# Blueprint de Examen — {blueprint['course_id']}",
        f"**Generado:** {blueprint['generated_at'][:10]}",
        f"**Puntos totales:** {params['total_points']} | "
        f"**Tiempo:** {params['exam_time_minutes']} min | "
        f"**Perfil Bloom:** {params['bloom_profile']}",
        "",
        "## Matriz de Especificaciones",
        "",
    ]

    # Header de tabla
    bloom_levels = list(blueprint["bloom_profile_used"].keys())
    header = "| Tema | Puntos | Tiempo | " + " | ".join(
        level.capitalize() for level in bloom_levels
    ) + " |"
    separator = "|------|--------|--------|" + "|".join(
        "-----:" for _ in bloom_levels
    ) + "|"
    lines.extend([header, separator])

    for row in blueprint["matrix"]:
        bloom_vals = " | ".join(
            str(row["bloom_distribution"].get(level, 0)) for level in bloom_levels
        )
        lines.append(
            f"| {row['topic_id']} | {row['points']} ({row['weight_pct']}%) | "
            f"{row['time_minutes']} min | {bloom_vals} |"
        )

    # Fila de totales
    totals = blueprint["bloom_totals"]
    totals_vals = " | ".join(str(totals.get(level, 0)) for level in bloom_levels)
    lines.append(
        f"| **TOTAL** | **{params['total_points']}** | "
        f"**{params['exam_time_minutes']} min** | {totals_vals} |"
    )

    # Perfil Bloom usado
    lines.extend([
        "",
        "## Perfil Bloom Aplicado",
        "",
        "| Nivel | Porcentaje |",
        "|-------|-----------|",
    ])
    for level, pct in blueprint["bloom_profile_used"].items():
        bar = "█" * round(pct * 20) + "░" * (20 - round(pct * 20))
        lines.append(f"| {level.capitalize()} | {bar} {pct:.0%} |")

    lines.extend([
        "",
        "## Sugerencias de Diseño",
        "",
        "- **Recordar:** Definiciones, enumeraciones, completar blancos",
        "- **Comprender:** Explicar con sus palabras, dar ejemplos, parafrasear",
        "- **Aplicar:** Resolver ejercicios, escribir código, usar fórmulas",
        "- **Analizar:** Comparar enfoques, encontrar errores, descomponer problemas",
        "- **Evaluar:** Justificar decisiones, defender posiciones, criticar soluciones",
    ])

    return "\n".join(lines) + "\n"


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generador de Blueprints de Examen (tabla de especificaciones)"
    )
    parser.add_argument("--course", required=True, help="ID del curso (ej: leng-2026)")
    parser.add_argument("--topics", required=True,
                        help="Temas separados por coma (ej: 01-intro,02-tipos)")
    parser.add_argument("--points", type=int, default=100,
                        help="Puntos totales del examen (default: 100)")
    parser.add_argument("--time", type=int, default=120,
                        help="Duración del examen en minutos (default: 120)")
    parser.add_argument("--bloom-profile", default="default",
                        choices=list(BLOOM_PROFILES.keys()),
                        help="Perfil de distribución Bloom (default: default)")
    parser.add_argument("--exam-name", default=None,
                        help="Nombre del examen (ej: parcial-1)")
    args = parser.parse_args()

    project_root = find_project_root(Path(__file__).parent)
    topics = [t.strip() for t in args.topics.split(",") if t.strip()]

    if not topics:
        parser.error("Especificar al menos un tema con --topics")

    blueprint = generate_blueprint(
        topics=topics,
        total_points=args.points,
        exam_time_min=args.time,
        bloom_profile=args.bloom_profile,
        project_root=project_root,
        course_id=args.course,
    )

    # Determinar nombre y ruta de salida
    exam_name = args.exam_name
    if not exam_name:
        # Auto-numerar
        output_base = project_root / "salida" / "cursadas" / args.course / "evaluaciones"
        output_base.mkdir(parents=True, exist_ok=True)
        existing = sorted(output_base.glob("blueprint-parcial-*.json"))
        n = len(existing) + 1
        exam_name = f"parcial-{n}"

    output_dir = project_root / "salida" / "cursadas" / args.course / "evaluaciones"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Guardar JSON
    json_path = output_dir / f"blueprint-{exam_name}.json"
    json_path.write_text(
        json.dumps(blueprint, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Guardar Markdown
    md_path = output_dir / f"blueprint-{exam_name}.md"
    md_content = blueprint_to_markdown(blueprint)
    md_path.write_text(md_content, encoding="utf-8")

    # Validar contra schema si existe
    schema_path = project_root / "_edu" / "schemas" / "exam-blueprint.schema.json"
    if schema_path.exists():
        try:
            import jsonschema
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            jsonschema.validate(blueprint, schema)
            print("✅ Blueprint válido contra exam-blueprint.schema.json")
        except ImportError:
            print("⚠️ jsonschema no instalado — validación de schema omitida")
        except Exception as e:
            print(f"⚠️ Blueprint no pasa validación de schema: {e}")

    print(f"✅ Blueprint generado:")
    print(f"   JSON: {json_path}")
    print(f"   Markdown: {md_path}")
    print(f"   Temas: {len(topics)} | Puntos: {args.points} | Tiempo: {args.time} min")


if __name__ == "__main__":
    main()
