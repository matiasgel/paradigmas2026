#!/usr/bin/env python3
"""
fact_verifier.py — Pipeline NLI de verificación factual (S9.3)

Descompone texto en claims atómicos, busca evidencia en ChromaDB
y plan-minimo, y clasifica con NLI (cross-encoder) o fallback heurístico.

Uso:
    python scripts/fact_verifier.py --topic 05-sorting --course leng-2026

Exit codes:
    0 — todos los claims verificados o neutros
    1 — al menos un claim refutado (CONTRADICTION)
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

from pipeline_common import find_project_root, load_yaml


def extract_claims(text: str) -> list[str]:
    """Descompone texto en claims atómicos (oraciones verificables)."""
    # Separar en oraciones
    sentences = re.split(r"(?<=[.!?])\s+", text)
    claims = []
    for s in sentences:
        s = s.strip()
        # Filtrar líneas no verificables (encabezados, directivas, código)
        if not s or len(s) < 20:
            continue
        if s.startswith("#") or s.startswith("@") or s.startswith("```"):
            continue
        if re.match(r"^[-*]\s", s):
            s = re.sub(r"^[-*]\s+", "", s)
        # Solo claims declarativos (no preguntas)
        if s.endswith("?"):
            continue
        claims.append(s[:300])

    return claims[:100]  # Limitar para performance


def retrieve_evidence(claim: str, course_dir: Path) -> list[str]:
    """Busca evidencia relevante para el claim."""
    evidence = []

    # Buscar en plan-minimo.md
    plan_path = course_dir / "plan-minimo.md"
    if plan_path.exists():
        plan_text = plan_path.read_text(encoding="utf-8")
        # Buscar párrafos relevantes por palabras clave
        claim_words = set(claim.lower().split())
        for para in plan_text.split("\n\n"):
            para_words = set(para.lower().split())
            overlap = len(claim_words & para_words)
            if overlap >= 3:
                evidence.append(para.strip()[:500])

    # Intentar ChromaDB
    try:
        import chromadb  # type: ignore
        kb_path = course_dir.parent.parent.parent / "_edu-knowledge" / "chroma_db"
        if kb_path.exists():
            client = chromadb.PersistentClient(path=str(kb_path))
            collection = client.get_or_create_collection("edu_knowledge")
            results = collection.query(query_texts=[claim], n_results=3)
            if results and results.get("documents"):
                for docs in results["documents"]:
                    evidence.extend(d[:500] for d in docs if d)
    except (ImportError, Exception):
        pass

    return evidence[:5]


def classify_nli(claim: str, evidence: list[str]) -> dict:
    """Clasifica claim vs evidencia con NLI cross-encoder o fallback."""
    if not evidence:
        return {"verdict": "NEUTRAL", "confidence": 0.0, "label": "⚠️"}

    try:
        from sentence_transformers import CrossEncoder  # type: ignore
        model = CrossEncoder("cross-encoder/nli-deberta-v3-small")
        best_score = {"entailment": 0.0, "contradiction": 0.0, "neutral": 0.0}

        for ev in evidence:
            scores = model.predict([(ev, claim)])[0]
            # scores: [contradiction, entailment, neutral]
            if scores[1] > best_score["entailment"]:
                best_score["entailment"] = float(scores[1])
            if scores[0] > best_score["contradiction"]:
                best_score["contradiction"] = float(scores[0])

        if best_score["entailment"] > 0.7:
            return {"verdict": "ENTAILMENT", "confidence": best_score["entailment"], "label": "✅"}
        if best_score["contradiction"] > 0.7:
            return {"verdict": "CONTRADICTION", "confidence": best_score["contradiction"], "label": "❌"}
        return {"verdict": "NEUTRAL", "confidence": max(best_score.values()), "label": "⚠️"}

    except ImportError:
        # Fallback heurístico: word overlap
        claim_words = set(claim.lower().split())
        max_overlap = 0
        for ev in evidence:
            ev_words = set(ev.lower().split())
            overlap = len(claim_words & ev_words) / max(len(claim_words), 1)
            max_overlap = max(max_overlap, overlap)

        if max_overlap > 0.5:
            return {"verdict": "ENTAILMENT", "confidence": max_overlap, "label": "✅"}
        if max_overlap < 0.1:
            return {"verdict": "NEUTRAL", "confidence": 1 - max_overlap, "label": "⚠️"}
        return {"verdict": "NEUTRAL", "confidence": 0.5, "label": "⚠️"}


def generate_report(results: list[dict], output_path: Path, topic_id: str) -> str:
    """Genera fact-check report Markdown."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    contradictions = [r for r in results if r["verdict"] == "CONTRADICTION"]
    verified = [r for r in results if r["verdict"] == "ENTAILMENT"]
    neutral = [r for r in results if r["verdict"] == "NEUTRAL"]

    lines = [
        f"# Fact-Check Report — {topic_id}",
        f"\n> Generado: {now}",
        f"> Claims analizados: {len(results)} | ✅ {len(verified)} | ❌ {len(contradictions)} | ⚠️ {len(neutral)}\n",
    ]

    if contradictions:
        lines.extend([
            "## ❌ Claims refutados (requieren revisión)\n",
            "| # | Claim | Confianza |",
            "|---|-------|-----------|",
        ])
        for i, r in enumerate(contradictions, 1):
            lines.append(f"| {i} | {r['claim'][:100]} | {r['confidence']:.2f} |")

    if neutral:
        lines.extend([
            "\n## ⚠️ Evidencia insuficiente\n",
            "| # | Claim | Confianza |",
            "|---|-------|-----------|",
        ])
        for i, r in enumerate(neutral[:20], 1):
            lines.append(f"| {i} | {r['claim'][:100]} | {r['confidence']:.2f} |")

    lines.extend([
        "\n## Resumen\n",
        f"- **Verificados:** {len(verified)}",
        f"- **Refutados:** {len(contradictions)}",
        f"- **Sin evidencia:** {len(neutral)}",
    ])

    report = "\n".join(lines) + "\n"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return str(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="NLI Fact Verifier")
    parser.add_argument("--topic", required=True, help="ID del tema")
    parser.add_argument("--course", required=True, help="ID del curso")
    args = parser.parse_args()

    root = find_project_root(Path(__file__).parent)
    course_dir = root / "salida" / "cursadas" / args.course
    topic_folder = course_dir / "temas" / args.topic

    # Buscar textos para verificar
    texts = []
    for md_file in ("minuta.md", "filminas.md"):
        path = topic_folder / md_file
        if path.exists():
            texts.append(path.read_text(encoding="utf-8"))

    if not texts:
        print(f"ℹ️  Sin textos para verificar en {topic_folder}")
        return 0

    full_text = "\n".join(texts)
    claims = extract_claims(full_text)
    if not claims:
        print("ℹ️  Sin claims verificables extraídos")
        return 0

    print(f"🔍 Verificando {len(claims)} claims...")

    results = []
    for claim in claims:
        evidence = retrieve_evidence(claim, course_dir)
        classification = classify_nli(claim, evidence)
        results.append({
            "claim": claim,
            "evidence_count": len(evidence),
            **classification,
        })

    output = topic_folder / "fact-check-report.md"
    path = generate_report(results, output, args.topic)

    contradictions = sum(1 for r in results if r["verdict"] == "CONTRADICTION")
    print(f"✅ Reporte generado: {path}")

    if contradictions > 0:
        print(f"❌ {contradictions} claims refutados — requieren revisión humana")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
