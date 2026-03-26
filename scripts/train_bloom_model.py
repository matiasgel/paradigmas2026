#!/usr/bin/env python3
"""
Train Bloom Model — Fine-tuning de DeBERTa para clasificación de Bloom (S10.1).

Script auxiliar para entrenar el clasificador. Diseñado para Google Colab T4 (~2h).
Se ejecuta una vez y el modelo queda en _edu-knowledge/models/bloom-classifier/.

Uso:
  python scripts/train_bloom_model.py [--epochs 5] [--batch-size 16]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import find_project_root


BLOOM_LABELS = ["recordar", "comprender", "aplicar", "analizar", "evaluar", "crear"]

# Dataset sintético mínimo para bootstrap (el docente agrega más con active learning)
SEED_DATASET = [
    ("¿Qué es una variable?", "recordar"),
    ("Definir qué es un algoritmo", "recordar"),
    ("Enumerar los tipos de datos primitivos", "recordar"),
    ("Explicar la diferencia entre stack y heap", "comprender"),
    ("¿Por qué la recursión necesita un caso base?", "comprender"),
    ("Describir el funcionamiento de un garbage collector", "comprender"),
    ("Implementar una función que ordene una lista", "aplicar"),
    ("Resolver el problema usando programación dinámica", "aplicar"),
    ("Programar un servidor HTTP básico", "aplicar"),
    ("Analizar la complejidad temporal del algoritmo", "analizar"),
    ("¿Cuál es la relación entre herencia y polimorfismo?", "analizar"),
    ("Clasificar los siguientes errores por tipo", "analizar"),
    ("Justificar la elección de una estructura de datos", "evaluar"),
    ("¿Cuál enfoque es más eficiente y por qué?", "evaluar"),
    ("Criticar el diseño de la API propuesta", "evaluar"),
    ("Diseñar un sistema de caché distribuido", "crear"),
    ("Proponer una arquitectura para el problema dado", "crear"),
    ("Crear un protocolo de comunicación entre procesos", "crear"),
]


def main():
    parser = argparse.ArgumentParser(description="Train Bloom Classifier (DeBERTa fine-tuning)")
    parser.add_argument("--epochs", type=int, default=5, help="Número de epochs")
    parser.add_argument("--batch-size", type=int, default=16, help="Batch size")
    parser.add_argument("--model-name", default="microsoft/deberta-v3-base", help="Modelo base")
    args = parser.parse_args()

    root = find_project_root()
    output_dir = root / "_edu-knowledge" / "models" / "bloom-classifier"

    try:
        from datasets import Dataset
        from transformers import (
            AutoTokenizer,
            AutoModelForSequenceClassification,
            TrainingArguments,
            Trainer,
        )
    except ImportError:
        print("❌ Dependencias de entrenamiento no instaladas.")
        print("  pip install transformers datasets torch")
        print("\n  Recomendado: ejecutar en Google Colab con GPU T4 gratuita.")
        sys.exit(1)

    label2id = {l: i for i, l in enumerate(BLOOM_LABELS)}
    id2label = {i: l for i, l in enumerate(BLOOM_LABELS)}

    # Preparar dataset
    texts = [t for t, _ in SEED_DATASET]
    labels = [label2id[l] for _, l in SEED_DATASET]

    # Verificar si hay dataset extendido del docente
    custom_dataset = root / "_edu-knowledge" / "bloom-training-data.json"
    if custom_dataset.exists():
        custom = json.loads(custom_dataset.read_text(encoding="utf-8"))
        texts.extend(item["text"] for item in custom)
        labels.extend(label2id[item["label"]] for item in custom)
        print(f"📚 Dataset extendido cargado: {len(custom)} items adicionales")

    dataset = Dataset.from_dict({"text": texts, "label": labels})
    dataset = dataset.train_test_split(test_size=0.2, seed=42)

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        args.model_name,
        num_labels=len(BLOOM_LABELS),
        label2id=label2id,
        id2label=id2label,
    )

    def tokenize(batch):
        return tokenizer(batch["text"], padding="max_length", truncation=True, max_length=256)

    tokenized = dataset.map(tokenize, batched=True)

    training_args = TrainingArguments(
        output_dir=str(output_dir),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["test"],
    )

    print(f"🚀 Entrenando {args.model_name} por {args.epochs} epochs...")
    trainer.train()
    trainer.save_model(str(output_dir))
    tokenizer.save_pretrained(str(output_dir))
    print(f"✅ Modelo guardado en {output_dir}")


if __name__ == "__main__":
    main()
