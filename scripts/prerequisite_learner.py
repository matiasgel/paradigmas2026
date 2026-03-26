#!/usr/bin/env python3
"""
prerequisite_learner.py — Concept Prerequisite Learning con ML (S11.2)
======================================================================
Classifier XGBoost/LightGBM para inferir relaciones de prerequisito
entre conceptos usando features semánticas y estructurales.

Uso:
    python scripts/prerequisite_learner.py --course leng-2026 predict
    python scripts/prerequisite_learner.py --course leng-2026 annotate

Dependencias: scikit-learn, numpy  (XGBoost opcional)
"""

from __future__ import annotations

import argparse
import csv
import json
import pickle
import sys
from itertools import combinations
from pathlib import Path

import numpy as np

# --- path setup -----------------------------------------------------------
_this = Path(__file__).resolve()
_scripts = _this.parent
_root = _scripts.parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from pipeline_common import (
    Result,
    find_project_root,
    load_config,
    load_json,
    save_json,
)


# ═══════════════════════════════════════════════════════════════════════
# FEATURE EXTRACTION
# ═══════════════════════════════════════════════════════════════════════

def _load_embeddings(project_root: Path) -> dict[str, np.ndarray] | None:
    """Intenta cargar embeddings precomputados."""
    emb_path = project_root / "_edu-knowledge" / "concept-embeddings.json"
    if not emb_path.exists():
        return None
    data = load_json(emb_path)
    return {k: np.array(v) for k, v in data.items()}


def compute_features(
    concept_a: str,
    concept_b: str,
    embeddings: dict[str, np.ndarray] | None,
    concept_order: dict[str, int],
) -> np.ndarray:
    """Computa features para el par (A, B)."""
    features = []

    # Feature 1: Similaridad semántica
    if embeddings and concept_a in embeddings and concept_b in embeddings:
        emb_a = embeddings[concept_a]
        emb_b = embeddings[concept_b]
        cos_sim = float(np.dot(emb_a, emb_b) / (np.linalg.norm(emb_a) * np.linalg.norm(emb_b) + 1e-8))
    else:
        cos_sim = 0.0
    features.append(cos_sim)

    # Feature 2: Orden en el curso
    order_a = concept_order.get(concept_a, -1)
    order_b = concept_order.get(concept_b, -1)
    order_diff = order_a - order_b if order_a >= 0 and order_b >= 0 else 0
    features.append(order_diff)

    # Feature 3: Distancia absoluta de orden
    features.append(abs(order_diff))

    # Feature 4: A aparece antes que B (binario)
    features.append(1.0 if order_diff < 0 else 0.0)

    return np.array(features, dtype=np.float32)


# ═══════════════════════════════════════════════════════════════════════
# CPL LEARNER
# ═══════════════════════════════════════════════════════════════════════

class CPLLearner:
    """Concept Prerequisite Learning con scikit-learn."""

    def __init__(self) -> None:
        self.model = None
        self.is_trained = False

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """Entrena el clasificador."""
        try:
            from xgboost import XGBClassifier
            self.model = XGBClassifier(
                n_estimators=100,
                max_depth=4,
                use_label_encoder=False,
                eval_metric="logloss",
            )
        except ImportError:
            from sklearn.ensemble import GradientBoostingClassifier
            self.model = GradientBoostingClassifier(n_estimators=100, max_depth=4)

        self.model.fit(X, y)
        self.is_trained = True

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        if not self.is_trained or self.model is None:
            raise RuntimeError("Modelo no entrenado. Ejecute train() o load() primero.")
        return self.model.predict_proba(X)[:, 1]

    def save(self, path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("wb") as f:
            pickle.dump({"model": self.model, "is_trained": self.is_trained}, f)

    @classmethod
    def load(cls, path: str | Path) -> CPLLearner:
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Modelo CPL no encontrado: {p}")
        with p.open("rb") as f:
            data = pickle.load(f)  # noqa: S301
        learner = cls()
        learner.model = data["model"]
        learner.is_trained = data["is_trained"]
        return learner

    def infer_cross_institution_prerequisites(self, kg) -> list[tuple[str, str, float]]:
        """Infiere prerequisitos entre conceptos del KG."""
        if not self.is_trained:
            return []
        concepts = kg.get_concepts()
        results = []
        embeddings = None  # In real use, load from KB
        concept_order = {c: i for i, c in enumerate(concepts)}
        pairs = list(combinations(concepts, 2))
        if not pairs:
            return []
        X = np.array([
            compute_features(a, b, embeddings, concept_order)
            for a, b in pairs
        ])
        probas = self.predict_proba(X)
        for (a, b), prob in zip(pairs, probas):
            if prob > 0.5:
                results.append((a, b, float(prob)))
        return results


# ═══════════════════════════════════════════════════════════════════════
# ACTIVE LEARNING
# ═══════════════════════════════════════════════════════════════════════

def run_active_learning(
    learner: CPLLearner,
    concepts: list[str],
    embeddings: dict[str, np.ndarray] | None,
    concept_order: dict[str, int],
    n_questions: int = 30,
    annotations_path: Path | None = None,
) -> list[dict]:
    """Sesión de active learning: presenta pares inciertos al docente."""
    pairs = list(combinations(concepts, 2))
    if not pairs:
        print("No hay pares de conceptos para anotar.")
        return []

    X = np.array([compute_features(a, b, embeddings, concept_order) for a, b in pairs])

    # Si el modelo ya está entrenado, seleccionar los más inciertos
    if learner.is_trained:
        probas = learner.predict_proba(X)
        uncertainty = np.abs(probas - 0.5)
        indices = np.argsort(uncertainty)[:n_questions]
    else:
        # Sin modelo, seleccionar aleatoriamente
        rng = np.random.default_rng(42)
        indices = rng.choice(len(pairs), size=min(n_questions, len(pairs)), replace=False)

    annotations = []
    print(f"\n📝 Sesión de anotación — {len(indices)} preguntas")
    print("Responda S (sí) / N (no) / Q (salir)\n")

    for idx in indices:
        a, b = pairs[idx]
        resp = input(f"  ¿'{a}' es prerequisito de '{b}'? [S/N/Q]: ").strip().upper()
        if resp == "Q":
            break
        label = 1 if resp == "S" else 0
        annotations.append({"from": a, "to": b, "is_prereq": label})

    if annotations and annotations_path:
        annotations_path.parent.mkdir(parents=True, exist_ok=True)
        with annotations_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["from", "to", "is_prereq"])
            writer.writeheader()
            writer.writerows(annotations)
        print(f"\n✅ {len(annotations)} anotaciones guardadas en {annotations_path}")

    return annotations


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(description="Concept Prerequisite Learner (S11.2)")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument(
        "command",
        choices=["predict", "annotate"],
        help="Comando: predict genera sugerencias, annotate inicia active learning",
    )
    args = parser.parse_args()

    project_root = find_project_root(Path.cwd())
    config = load_config(project_root)

    if not config.get("knowledge_graph_enabled", False):
        print("ℹ️  knowledge_graph_enabled no está habilitado. Saliendo.")
        return 0

    course_out = project_root / "salida" / "cursadas" / args.course
    kg_path = course_out / "knowledge-graph.json"
    model_path = project_root / "_edu-knowledge" / "models" / "cpl-model.pkl"

    if not kg_path.exists():
        print(f"❌ KG no encontrado: {kg_path}. Ejecutar 'knowledge_graph.py build' primero.")
        return 1

    # Load KG
    from knowledge_graph import CourseKnowledgeGraph

    kg = CourseKnowledgeGraph.load(kg_path)
    concepts = kg.get_concepts()
    embeddings = _load_embeddings(project_root)
    concept_order = {c: i for i, c in enumerate(concepts)}

    learner = CPLLearner()
    if model_path.exists():
        learner = CPLLearner.load(model_path)

    if args.command == "predict":
        if not learner.is_trained:
            print("⚠️  Modelo CPL no entrenado. Ejecute 'annotate' primero o proporcione modelo.")
            print(f"   Ruta esperada: {model_path}")
            return 0

        pairs = list(combinations(concepts, 2))
        if not pairs:
            print("No hay pares de conceptos para evaluar.")
            return 0

        X = np.array([compute_features(a, b, embeddings, concept_order) for a, b in pairs])
        probas = learner.predict_proba(X)

        suggestions = [
            {"from": pairs[i][0], "to": pairs[i][1], "confidence": float(probas[i])}
            for i in range(len(pairs))
            if probas[i] > 0.6
        ]
        suggestions.sort(key=lambda x: x["confidence"], reverse=True)

        out_path = course_out / "cpl-suggestions.json"
        save_json(out_path, {"suggestions": suggestions})
        print(f"✅ {len(suggestions)} prerequisitos sugeridos → {out_path}")
        for s in suggestions[:10]:
            print(f"   {s['from']} → {s['to']} (conf: {s['confidence']:.2f})")

    elif args.command == "annotate":
        annotations_path = course_out / "cpl-annotations.csv"
        run_active_learning(
            learner, concepts, embeddings, concept_order,
            n_questions=30, annotations_path=annotations_path,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
