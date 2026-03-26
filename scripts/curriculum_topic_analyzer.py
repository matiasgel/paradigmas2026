#!/usr/bin/env python3
"""
curriculum_topic_analyzer.py — BERTopic Curriculum Analyzer (S9.2)

Detecta gaps curriculares y redundancias comparando plan mínimo
contra artefactos producidos usando topic modeling.

Uso:
    python scripts/curriculum_topic_analyzer.py --course leng-2026

Exit codes:
    0 — reporte generado (o feature desactivada)
    1 — error
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


def extract_topics_from_plan(plan_path: Path) -> list[str]:
    """Extrae tópicos del plan mínimo."""
    if not plan_path.exists():
        return []
    text = plan_path.read_text(encoding="utf-8")
    topics = []
    for line in text.splitlines():
        line = line.strip()
        if re.match(r"^[-*]\s+", line) or re.match(r"^\d+\.\s+", line):
            topic = re.sub(r"^[-*\d.]+\s*", "", line).strip()
            if len(topic) > 3:
                topics.append(topic)
    return topics


def extract_concepts_from_artifacts(topic_dir: Path) -> list[str]:
    """Extrae conceptos de los artefactos de un tema."""
    concepts = []
    for md_file in ("diseno.md", "minuta.md", "filminas.md"):
        path = topic_dir / md_file
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        # Extraer encabezados como conceptos
        for match in re.finditer(r"^#{1,4}\s+(.+)$", text, re.MULTILINE):
            concept = match.group(1).strip()
            concept = re.sub(r"\[F-\d+\]\s*", "", concept)
            if len(concept) > 3:
                concepts.append(concept.lower())
    return concepts


def analyze_coverage(
    plan_topics: list[str],
    theme_concepts: dict[str, list[str]],
    embedder=None,
) -> dict:
    """Analiza cobertura: gaps, redundancias y drift."""
    gaps = []
    partial_gaps = []
    redundancies = []
    drift_topics = []

    all_concepts = []
    for concepts in theme_concepts.values():
        all_concepts.extend(concepts)

    concept_counts = Counter(all_concepts)

    if embedder is not None:
        plan_embeddings = embedder.encode(plan_topics)
        concept_unique = list(set(all_concepts))
        if concept_unique:
            concept_embeddings = embedder.encode(concept_unique)

            for i, plan_topic in enumerate(plan_topics):
                max_sim = 0.0
                found_in = []
                for theme_id, concepts in theme_concepts.items():
                    for concept in concepts:
                        if concept in concept_unique:
                            idx = concept_unique.index(concept)
                            sim = sum(a * b for a, b in zip(plan_embeddings[i], concept_embeddings[idx]))
                            norm_a = sum(a ** 2 for a in plan_embeddings[i]) ** 0.5
                            norm_b = sum(b ** 2 for b in concept_embeddings[idx]) ** 0.5
                            if norm_a > 0 and norm_b > 0:
                                sim_val = sim / (norm_a * norm_b)
                                if sim_val > max_sim:
                                    max_sim = sim_val
                                if sim_val > 0.5:
                                    found_in.append(theme_id)

                if max_sim < 0.3:
                    gaps.append({"topic": plan_topic, "max_similarity": max_sim})
                elif not found_in:
                    partial_gaps.append({"topic": plan_topic, "max_similarity": max_sim})
    else:
        # Fallback sin embeddings: matching por palabras clave
        for plan_topic in plan_topics:
            words = set(plan_topic.lower().split())
            found = False
            for concepts in theme_concepts.values():
                for concept in concepts:
                    if words & set(concept.split()):
                        found = True
                        break
                if found:
                    break
            if not found:
                gaps.append({"topic": plan_topic, "max_similarity": 0})

    # Redundancias
    for concept, count in concept_counts.items():
        if count > 3:
            themes = [tid for tid, cs in theme_concepts.items() if concept in cs]
            redundancies.append({"concept": concept, "count": count, "themes": themes[:5]})

    return {
        "gaps": gaps,
        "partial_gaps": partial_gaps,
        "redundancies": redundancies,
    }


def generate_report(analysis: dict, output_path: Path, course_id: str) -> str:
    """Genera reporte Markdown de análisis curricular."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Análisis Curricular — {course_id}",
        f"\n> Generado: {now}\n",
    ]

    gaps = analysis["gaps"]
    if gaps:
        lines.extend([
            "## 🔴 Gaps curriculares (tópicos no cubiertos)\n",
            "| Tópico del plan | Similitud máxima |",
            "|-----------------|------------------|",
        ])
        for g in gaps:
            lines.append(f"| {g['topic']} | {g['max_similarity']:.2f} |")
    else:
        lines.append("\n✅ Sin gaps — todos los tópicos del plan están cubiertos.\n")

    partial = analysis["partial_gaps"]
    if partial:
        lines.extend([
            "\n## 🟡 Gaps parciales\n",
            "| Tópico | Similitud |",
            "|--------|-----------|",
        ])
        for g in partial:
            lines.append(f"| {g['topic']} | {g['max_similarity']:.2f} |")

    redundancies = analysis["redundancies"]
    if redundancies:
        lines.extend([
            "\n## ⚠️ Redundancias (>3 apariciones)\n",
            "| Concepto | Apariciones | Temas |",
            "|----------|-------------|-------|",
        ])
        for r in redundancies:
            lines.append(f"| {r['concept']} | {r['count']} | {', '.join(r['themes'])} |")

    total = len(gaps) + len(partial) + len(redundancies)
    lines.append(f"\n---\n**Total issues:** {total}")

    report = "\n".join(lines) + "\n"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return str(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Curriculum Topic Analyzer")
    parser.add_argument("--course", required=True, help="ID del curso")
    args = parser.parse_args()

    root = find_project_root(Path(__file__).parent)
    config = load_yaml(root / "_edu" / "config.yaml")

    if not config.get("topic_analysis_enabled", False):
        print("ℹ️  Análisis de tópicos desactivado (topic_analysis_enabled: false)")
        return 0

    course_dir = root / "salida" / "cursadas" / args.course
    plan_path = course_dir / "plan-minimo.md"
    topics_dir = course_dir / "temas"

    plan_topics = extract_topics_from_plan(plan_path)
    if not plan_topics:
        print("ℹ️  plan-minimo.md no encontrado o sin tópicos")
        return 0

    theme_concepts: dict[str, list[str]] = {}
    if topics_dir.is_dir():
        for topic_dir in sorted(topics_dir.iterdir()):
            if topic_dir.is_dir():
                concepts = extract_concepts_from_artifacts(topic_dir)
                if concepts:
                    theme_concepts[topic_dir.name] = concepts

    if not theme_concepts:
        print("ℹ️  Sin artefactos de temas disponibles")
        return 0

    embedder = None
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore
        embedder = SentenceTransformer("all-MiniLM-L6-v2")
    except ImportError:
        print("⚠️  sentence-transformers no instalado — usando matching por palabras clave")

    analysis = analyze_coverage(plan_topics, theme_concepts, embedder)

    output = course_dir / "topic-analysis" / "gaps-report.md"
    path = generate_report(analysis, output, args.course)
    print(f"✅ Reporte generado: {path}")
    print(f"   Gaps: {len(analysis['gaps'])} | Parciales: {len(analysis['partial_gaps'])} | Redundancias: {len(analysis['redundancies'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
