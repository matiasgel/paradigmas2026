#!/usr/bin/env python3
"""
train_prerequisite_model.py — Entrenamiento CPL con LectureBank (S11.2)
=======================================================================
Script auxiliar para entrenar el clasificador de prerequisitos.
Diseñado para correr en Google Colab T4 (o CPU local).

Uso:
    python scripts/train_prerequisite_model.py --dataset lecturebank
    python scripts/train_prerequisite_model.py --dataset custom --csv annotations.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import pickle
import sys
from pathlib import Path

import numpy as np

_this = Path(__file__).resolve()
_scripts = _this.parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from pipeline_common import find_project_root


# ═══════════════════════════════════════════════════════════════════════
# SEED DATASET (LectureBank-inspired pairs)
# ═══════════════════════════════════════════════════════════════════════

SEED_PAIRS: list[dict] = [
    {"from": "variables", "to": "funciones", "label": 1},
    {"from": "funciones", "to": "recursion", "label": 1},
    {"from": "recursion", "to": "arboles", "label": 1},
    {"from": "tipos_datos", "to": "estructuras_datos", "label": 1},
    {"from": "listas", "to": "arboles", "label": 1},
    {"from": "arboles", "to": "grafos", "label": 1},
    {"from": "algebra_booleana", "to": "logica_proposicional", "label": 1},
    {"from": "logica_proposicional", "to": "logica_predicados", "label": 1},
    {"from": "matrices", "to": "grafos", "label": 1},
    {"from": "probabilidad", "to": "machine_learning", "label": 1},
    {"from": "grafos", "to": "recursion", "label": 0},
    {"from": "machine_learning", "to": "variables", "label": 0},
    {"from": "arboles", "to": "tipos_datos", "label": 0},
    {"from": "funciones", "to": "variables", "label": 0},
    {"from": "grafos", "to": "algebra_booleana", "label": 0},
    {"from": "logica_predicados", "to": "listas", "label": 0},
    {"from": "machine_learning", "to": "algebra_booleana", "label": 0},
    {"from": "recursion", "to": "matrices", "label": 0},
    {"from": "estructuras_datos", "to": "probabilidad", "label": 0},
    {"from": "logica_proposicional", "to": "funciones", "label": 0},
]


def load_custom_dataset(csv_path: Path) -> list[dict]:
    """Carga anotaciones desde CSV (columnas: from, to, is_prereq)."""
    pairs = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pairs.append({
                "from": row["from"],
                "to": row["to"],
                "label": int(row["is_prereq"]),
            })
    return pairs


def pairs_to_features(pairs: list[dict]) -> tuple[np.ndarray, np.ndarray]:
    """Convierte pares en features simples para entrenamiento."""
    # Features simplificados: hash-based (para demo; en prod usar embeddings)
    X_list = []
    y_list = []
    all_concepts = set()
    for p in pairs:
        all_concepts.add(p["from"])
        all_concepts.add(p["to"])

    concept_list = sorted(all_concepts)
    concept_idx = {c: i for i, c in enumerate(concept_list)}

    for p in pairs:
        idx_a = concept_idx[p["from"]]
        idx_b = concept_idx[p["to"]]
        features = [
            idx_a,
            idx_b,
            idx_a - idx_b,
            abs(idx_a - idx_b),
        ]
        X_list.append(features)
        y_list.append(p["label"])

    return np.array(X_list, dtype=np.float32), np.array(y_list, dtype=np.int32)


def main() -> int:
    parser = argparse.ArgumentParser(description="Train CPL Model (S11.2)")
    parser.add_argument(
        "--dataset",
        choices=["lecturebank", "custom"],
        default="lecturebank",
        help="Dataset a usar",
    )
    parser.add_argument("--csv", type=str, help="Path al CSV custom (con --dataset custom)")
    args = parser.parse_args()

    project_root = find_project_root(Path.cwd())
    model_dir = project_root / "_edu-knowledge" / "models"
    model_path = model_dir / "cpl-model.pkl"

    if args.dataset == "custom" and args.csv:
        csv_path = Path(args.csv)
        if not csv_path.exists():
            print(f"❌ CSV no encontrado: {csv_path}")
            return 1
        pairs = load_custom_dataset(csv_path)
        print(f"📊 Dataset custom: {len(pairs)} pares")
    else:
        pairs = SEED_PAIRS
        print(f"📊 Dataset seed (LectureBank-inspired): {len(pairs)} pares")

    X, y = pairs_to_features(pairs)
    print(f"   Features shape: {X.shape}")
    print(f"   Label distribution: {int(y.sum())} positivos, {int(len(y) - y.sum())} negativos")

    # Train
    try:
        from xgboost import XGBClassifier

        model = XGBClassifier(
            n_estimators=100, max_depth=4,
            use_label_encoder=False, eval_metric="logloss",
        )
        print("🔧 Usando XGBoost")
    except ImportError:
        from sklearn.ensemble import GradientBoostingClassifier

        model = GradientBoostingClassifier(n_estimators=100, max_depth=4)
        print("🔧 Usando GradientBoostingClassifier (sklearn fallback)")

    model.fit(X, y)

    # Cross-validation score
    from sklearn.model_selection import cross_val_score

    scores = cross_val_score(model, X, y, cv=min(3, len(y)), scoring="accuracy")
    print(f"✅ Accuracy (CV): {scores.mean():.2f} ± {scores.std():.2f}")

    # Save
    model_dir.mkdir(parents=True, exist_ok=True)
    with model_path.open("wb") as f:
        pickle.dump({"model": model, "is_trained": True}, f)
    print(f"💾 Modelo guardado: {model_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
