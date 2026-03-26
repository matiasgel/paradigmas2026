#!/usr/bin/env python3
"""
Bloom Classifier — Clasificador DeBERTa fine-tuned para taxonomía de Bloom (S10.1).

Clasifica preguntas de TP/examen en 6 niveles de Bloom:
  Recordar / Comprender / Aplicar / Analizar / Evaluar / Crear

Uso:
  python scripts/bloom_classifier.py --course leng-2026 --exam parcial-1
  python scripts/bloom_classifier.py --file preguntas.txt

Sin modelo fine-tuned: usa fallback basado en keywords.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import find_project_root, load_yaml, Result

BLOOM_LEVELS = ["recordar", "comprender", "aplicar", "analizar", "evaluar", "crear"]

# Keywords heurísticos por nivel de Bloom (fallback sin modelo ML)
BLOOM_KEYWORDS: dict[str, list[str]] = {
    "recordar": ["definir", "listar", "nombrar", "identificar", "enumerar", "qué es", "cuál es", "mencionar"],
    "comprender": ["explicar", "describir", "resumir", "interpretar", "comparar", "diferenciar", "por qué"],
    "aplicar": ["aplicar", "implementar", "resolver", "calcular", "usar", "demostrar", "programar", "codificar"],
    "analizar": ["analizar", "descomponer", "clasificar", "examinar", "distinguir", "relación entre", "causa"],
    "evaluar": ["evaluar", "justificar", "argumentar", "criticar", "juzgar", "defender", "cuál es mejor"],
    "crear": ["diseñar", "crear", "proponer", "desarrollar", "construir", "inventar", "formular", "planificar"],
}


def _classify_keyword_fallback(question: str) -> tuple[str, float]:
    """Clasificador heurístico basado en keywords. Fallback sin modelo ML."""
    q_lower = question.lower()
    scores = {}
    for level, keywords in BLOOM_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in q_lower)
        scores[level] = score
    best = max(scores, key=scores.get)
    total = sum(scores.values())
    confidence = scores[best] / total if total > 0 else 0.2
    return best, round(confidence, 2)


def _load_ml_model(model_path: Path):
    """Intenta cargar el modelo DeBERTa fine-tuned."""
    try:
        from transformers import pipeline as hf_pipeline
        if model_path.exists():
            classifier = hf_pipeline("text-classification", model=str(model_path), top_k=None)
            return classifier
    except ImportError:
        pass
    return None


def classify_questions(questions: list[str], model_path: Path | None = None) -> list[dict]:
    """Clasifica una lista de preguntas por nivel de Bloom."""
    classifier = None
    if model_path:
        classifier = _load_ml_model(model_path)

    results = []
    for q in questions:
        if classifier:
            preds = classifier(q[:512])
            if preds and isinstance(preds[0], list):
                best = max(preds[0], key=lambda x: x["score"])
                bloom_ml = best["label"].lower()
                confidence = round(best["score"], 3)
            else:
                bloom_ml, confidence = _classify_keyword_fallback(q)
        else:
            bloom_ml, confidence = _classify_keyword_fallback(q)

        results.append({
            "question": q[:200],
            "bloom_level": bloom_ml,
            "confidence": confidence,
            "method": "ml" if classifier else "keyword-fallback",
        })
    return results


def _extract_questions_from_exam(exam_path: Path) -> list[str]:
    """Extrae preguntas de un archivo de blueprint o texto."""
    text = exam_path.read_text(encoding="utf-8")
    questions = []
    for line in text.splitlines():
        line = line.strip()
        if re.match(r"^\d+[\.\)]\s+", line) and len(line) > 15:
            questions.append(re.sub(r"^\d+[\.\)]\s+", "", line))
        elif line.endswith("?"):
            questions.append(line)
    return questions


def main():
    parser = argparse.ArgumentParser(description="Bloom Classifier — Taxonomía de Bloom por pregunta")
    parser.add_argument("--course", help="ID del curso (ej: leng-2026)")
    parser.add_argument("--exam", help="Nombre del examen (ej: parcial-1)")
    parser.add_argument("--file", help="Archivo con preguntas (una por línea)")
    args = parser.parse_args()

    root = find_project_root()
    model_path = root / "_edu-knowledge" / "models" / "bloom-classifier"

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"❌ Archivo no encontrado: {args.file}")
            sys.exit(1)
        questions = [l.strip() for l in file_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    elif args.course and args.exam:
        course_id = args.course
        eval_dir = root / "salida" / "cursadas" / course_id / "evaluaciones"
        exam_file = eval_dir / f"blueprint-{args.exam}.md"
        if not exam_file.exists():
            exam_file = eval_dir / f"blueprint-{args.exam}.json"
        if not exam_file.exists():
            print(f"⚠️ No se encontró blueprint para {args.exam} en {eval_dir}")
            print("  Uso alternativo: --file preguntas.txt")
            sys.exit(0)
        questions = _extract_questions_from_exam(exam_file)
    else:
        print("Uso: bloom_classifier.py --course COURSE --exam EXAM  o  --file ARCHIVO")
        sys.exit(1)

    if not questions:
        print("⚠️ No se encontraron preguntas para clasificar.")
        sys.exit(0)

    if not model_path.exists():
        print("⚠️ Modelo DeBERTa fine-tuned no encontrado. Usando fallback por keywords.")
        print(f"  Para entrenar: python scripts/train_bloom_model.py")

    results = classify_questions(questions, model_path if model_path.exists() else None)

    # Output
    print(f"\n📊 Clasificación Bloom — {len(results)} preguntas\n")
    print(f"{'#':<4} {'Nivel':<12} {'Conf.':<8} {'Método':<10} {'Pregunta':<60}")
    print("-" * 94)
    for i, r in enumerate(results, 1):
        print(f"{i:<4} {r['bloom_level']:<12} {r['confidence']:<8} {r['method']:<10} {r['question'][:60]}")

    # Distribution
    dist = {}
    for r in results:
        dist[r["bloom_level"]] = dist.get(r["bloom_level"], 0) + 1
    print(f"\n📈 Distribución:")
    for level in BLOOM_LEVELS:
        count = dist.get(level, 0)
        pct = count / len(results) * 100
        bar = "█" * int(pct / 2)
        print(f"  {level:<12} {count:>3} ({pct:5.1f}%) {bar}")


if __name__ == "__main__":
    main()
