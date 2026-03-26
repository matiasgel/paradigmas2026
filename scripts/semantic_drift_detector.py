#!/usr/bin/env python3
"""
semantic_drift_detector.py — Detector de inconsistencias semánticas (S9.1)

Compara definiciones entre clases para detectar drift de vocabulario,
inconsistencias y saltos temáticos abruptos. Reutiliza MiniLM ya
instalado para ChromaDB.

Uso:
    python scripts/semantic_drift_detector.py --course leng-2026

Exit codes:
    0 — reporte generado (o sin material)
    1 — error
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


# Patrones para extraer definiciones explícitas
DEFINITION_PATTERNS = [
    re.compile(r"(?:^|\.\s)(\w[\w\s]{2,30})\s+(?:se define como|es un|es una|significa|se refiere a|consiste en)\s+(.{10,200}?)(?:\.|$)", re.IGNORECASE | re.MULTILINE),
    re.compile(r"(?:\*\*|__)(\w[\w\s]{2,30})(?:\*\*|__)\s*[:—–-]\s*(.{10,200}?)(?:\.|$)", re.MULTILINE),
]


def extract_definitions(text: str) -> list[dict]:
    """Extrae definiciones explícitas del texto."""
    defs = []
    for pattern in DEFINITION_PATTERNS:
        for match in pattern.finditer(text):
            term = match.group(1).strip().lower()
            definition = match.group(2).strip()
            if len(term) > 2 and len(definition) > 10:
                defs.append({"term": term, "definition": definition})
    return defs


def cosine_similarity_simple(vec_a: list[float], vec_b: list[float]) -> float:
    """Cosine similarity sin numpy (fallback stdlib)."""
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = sum(a * a for a in vec_a) ** 0.5
    norm_b = sum(b * b for b in vec_b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def load_embedder():
    """Intenta cargar sentence-transformers; fallback a None."""
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore
        return SentenceTransformer("all-MiniLM-L6-v2")
    except ImportError:
        return None


def analyze_definitions(all_defs: dict[str, list[dict]], embedder) -> list[dict]:
    """Analiza consistencia de definiciones entre temas."""
    # Agrupar por término
    term_map: dict[str, list[dict]] = {}
    for topic_id, defs in all_defs.items():
        for d in defs:
            term_map.setdefault(d["term"], []).append({
                "topic": topic_id, "definition": d["definition"],
            })

    issues = []
    for term, occurrences in term_map.items():
        if len(occurrences) < 2:
            continue

        if embedder is not None:
            texts = [o["definition"] for o in occurrences]
            embeddings = embedder.encode(texts)
            for i in range(len(occurrences)):
                for j in range(i + 1, len(occurrences)):
                    sim = cosine_similarity_simple(embeddings[i].tolist(), embeddings[j].tolist())
                    if sim < 0.70:
                        issues.append({
                            "type": "inconsistencia",
                            "severity": "🔴",
                            "term": term,
                            "topic_a": occurrences[i]["topic"],
                            "topic_b": occurrences[j]["topic"],
                            "def_a": occurrences[i]["definition"][:80],
                            "def_b": occurrences[j]["definition"][:80],
                            "similarity": sim,
                        })
                    elif sim < 0.85:
                        issues.append({
                            "type": "complementaria",
                            "severity": "⚠️",
                            "term": term,
                            "topic_a": occurrences[i]["topic"],
                            "topic_b": occurrences[j]["topic"],
                            "similarity": sim,
                        })
        else:
            # Sin embedder, solo reportar definiciones múltiples
            topics = [o["topic"] for o in occurrences]
            issues.append({
                "type": "multiple_defs",
                "severity": "ℹ️",
                "term": term,
                "topics": topics,
                "note": "Instalar sentence-transformers para análisis de similitud",
            })

    return issues


def analyze_narrative_coherence(topics_text: list[tuple[str, str]], embedder) -> list[dict]:
    """Analiza coherencia narrativa secuencial entre temas."""
    if embedder is None or len(topics_text) < 2:
        return []

    issues = []
    embeddings = embedder.encode([t[1][:2000] for t in topics_text])

    for i in range(1, len(embeddings)):
        sim = cosine_similarity_simple(embeddings[i - 1].tolist(), embeddings[i].tolist())
        if sim < 0.30:
            issues.append({
                "type": "salto_abrupto",
                "severity": "🔴",
                "from_topic": topics_text[i - 1][0],
                "to_topic": topics_text[i][0],
                "similarity": sim,
            })

    return issues


def generate_report(def_issues: list[dict], coherence_issues: list[dict], output_path: Path, course_id: str) -> str:
    """Genera reporte Markdown de consistencia."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Análisis de Consistencia Semántica — {course_id}",
        f"\n> Generado: {now}\n",
    ]

    if def_issues:
        lines.extend([
            "## Definiciones\n",
            "| Severidad | Término | Tema A | Tema B | Similitud |",
            "|-----------|---------|--------|--------|-----------|",
        ])
        for issue in def_issues:
            sim = f"{issue.get('similarity', 0):.2f}" if "similarity" in issue else "N/A"
            topic_b = issue.get("topic_b", ", ".join(issue.get("topics", [])))
            lines.append(f"| {issue['severity']} | {issue['term']} | {issue.get('topic_a', '')} | {topic_b} | {sim} |")
    else:
        lines.append("\n✅ Sin inconsistencias detectadas en definiciones.\n")

    if coherence_issues:
        lines.extend([
            "\n## Coherencia Narrativa\n",
            "| Severidad | De | A | Similitud |",
            "|-----------|----|----|-----------|",
        ])
        for issue in coherence_issues:
            lines.append(f"| {issue['severity']} | {issue['from_topic']} | {issue['to_topic']} | {issue['similarity']:.2f} |")
    else:
        lines.append("\n✅ Coherencia narrativa entre temas sin saltos abruptos.\n")

    total = len(def_issues) + len(coherence_issues)
    lines.append(f"\n---\n**Total issues:** {total}")

    report = "\n".join(lines) + "\n"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return str(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Semantic Drift Detector")
    parser.add_argument("--course", required=True, help="ID del curso")
    args = parser.parse_args()

    root = find_project_root(Path(__file__).parent)
    topics_dir = root / "salida" / "cursadas" / args.course / "temas"

    if not topics_dir.is_dir():
        print(f"ℹ️  No hay temas en {topics_dir}")
        return 0

    # Recolectar textos de todos los temas
    all_defs: dict[str, list[dict]] = {}
    topics_text: list[tuple[str, str]] = []

    for topic_dir in sorted(topics_dir.iterdir()):
        if not topic_dir.is_dir():
            continue
        topic_id = topic_dir.name
        full_text = ""
        for md_file in ("minuta.md", "filminas.md", "guia-estudio.md"):
            path = topic_dir / md_file
            if path.exists():
                full_text += "\n" + path.read_text(encoding="utf-8")

        if full_text.strip():
            all_defs[topic_id] = extract_definitions(full_text)
            topics_text.append((topic_id, full_text))

    if not topics_text:
        print("ℹ️  Sin minutas/filminas disponibles para analizar")
        return 0

    embedder = load_embedder()
    if embedder is None:
        print("⚠️  sentence-transformers no instalado — análisis limitado a pattern matching")

    def_issues = analyze_definitions(all_defs, embedder)
    coherence_issues = analyze_narrative_coherence(topics_text, embedder)

    output = root / "salida" / "cursadas" / args.course / "coherence-analysis" / "consistency-report.md"
    path = generate_report(def_issues, coherence_issues, output, args.course)
    print(f"✅ Reporte generado: {path}")
    print(f"   Definiciones: {len(def_issues)} issues | Coherencia: {len(coherence_issues)} issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
