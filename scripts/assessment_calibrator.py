#!/usr/bin/env python3
"""
Assessment Calibrator — IRT 2PL + BKT por concepto (S10.2).

Calibra dificultad real de ítems de examen con IRT y estima
dominio conceptual por alumno con Bayesian Knowledge Tracing.

Uso:
  python scripts/assessment_calibrator.py --course leng-2026 --gradebook parcial-1.csv
  python scripts/assessment_calibrator.py --course leng-2026 --bkt
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import find_project_root, load_yaml


# ── BKT (Bayesian Knowledge Tracing) — Python puro ──

class BKTTracker:
    """Bayesian Knowledge Tracing por concepto."""

    def __init__(
        self,
        p_init: float = 0.3,
        p_learn: float = 0.1,
        p_guess: float = 0.25,
        p_slip: float = 0.10,
    ):
        self.p_init = p_init
        self.p_learn = p_learn
        self.p_guess = p_guess
        self.p_slip = p_slip
        self.mastery: dict[str, float] = {}

    def update(self, concept: str, correct: bool) -> float:
        """Actualizar P(mastery) para un concepto dado una respuesta."""
        p_know = self.mastery.get(concept, self.p_init)

        if correct:
            p_correct_if_know = 1.0 - self.p_slip
            p_correct_if_not = self.p_guess
        else:
            p_correct_if_know = self.p_slip
            p_correct_if_not = 1.0 - self.p_guess

        # Posterior
        p_evidence = p_know * p_correct_if_know + (1 - p_know) * p_correct_if_not
        if p_evidence > 0:
            p_know_post = (p_know * p_correct_if_know) / p_evidence
        else:
            p_know_post = p_know

        # Transition (learning)
        p_know_new = p_know_post + (1 - p_know_post) * self.p_learn
        self.mastery[concept] = p_know_new
        return p_know_new

    def get_mastery(self, concept: str) -> float:
        return self.mastery.get(concept, self.p_init)

    def get_all_mastery(self) -> dict[str, float]:
        return dict(self.mastery)


# ── IRT 2PL (simplificado) — Python puro ──

def irt_2pl_probability(theta: float, a: float, b: float) -> float:
    """P(correct | theta, a, b) = 1 / (1 + exp(-a * (theta - b)))"""
    z = a * (theta - b)
    z = max(-20, min(20, z))  # Clamp for numerical stability
    return 1.0 / (1.0 + math.exp(-z))


def estimate_irt_parameters(response_matrix: list[list[int]]) -> list[dict]:
    """
    Estimación simplificada de parámetros IRT 2PL.
    response_matrix: filas=alumnos, columnas=ítems (1=correcto, 0=incorrecto)
    """
    if not response_matrix or not response_matrix[0]:
        return []

    n_students = len(response_matrix)
    n_items = len(response_matrix[0])

    items = []
    for j in range(n_items):
        responses = [response_matrix[i][j] for i in range(n_students) if response_matrix[i][j] >= 0]
        if not responses:
            items.append({"item": j + 1, "difficulty": 0.0, "discrimination": 0.5, "p_value": 0.0})
            continue

        p_value = sum(responses) / len(responses)
        # Difficulty: inversión logit de p_value
        p_clamped = max(0.01, min(0.99, p_value))
        difficulty = -math.log(p_clamped / (1 - p_clamped))
        # Discrimination: correlación punto-biserial simplificada
        total_scores = [sum(r for r in row if r >= 0) for row in response_matrix]
        mean_total = sum(total_scores) / len(total_scores)
        correct_totals = [total_scores[i] for i in range(n_students) if response_matrix[i][j] == 1]
        if correct_totals:
            mean_correct = sum(correct_totals) / len(correct_totals)
            discrimination = max(0.1, (mean_correct - mean_total) / max(1, max(total_scores) - min(total_scores)))
        else:
            discrimination = 0.1

        items.append({
            "item": j + 1,
            "difficulty": round(difficulty, 3),
            "discrimination": round(discrimination, 3),
            "p_value": round(p_value, 3),
        })

    return items


def load_gradebook(csv_path: Path) -> tuple[list[str], list[str], list[list[int]]]:
    """Carga CSV de notas. Primera fila=headers, primera columna=alumno."""
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        items = headers[1:]
        students = []
        matrix = []
        for row in reader:
            students.append(row[0])
            responses = []
            for val in row[1:]:
                val = val.strip()
                if val in ("1", "1.0", "true", "si", "sí", "correct"):
                    responses.append(1)
                elif val in ("0", "0.0", "false", "no", "incorrect", ""):
                    responses.append(0)
                else:
                    try:
                        responses.append(1 if float(val) >= 0.5 else 0)
                    except ValueError:
                        responses.append(-1)
            matrix.append(responses)
    return students, items, matrix


def main():
    parser = argparse.ArgumentParser(description="Assessment Calibrator — IRT + BKT")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument("--gradebook", help="CSV de respuestas (alumnos × ítems)")
    parser.add_argument("--bkt", action="store_true", help="Ejecutar BKT sobre datos existentes")
    args = parser.parse_args()

    root = find_project_root()
    output_dir = root / "salida" / "cursadas" / args.course / "assessment-calibration"
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.gradebook:
        csv_path = Path(args.gradebook)
        if not csv_path.exists():
            print(f"❌ CSV no encontrado: {args.gradebook}")
            sys.exit(1)

        students, items, matrix = load_gradebook(csv_path)
        print(f"📊 Gradebook: {len(students)} alumnos × {len(items)} ítems")

        # IRT Analysis
        irt_results = estimate_irt_parameters(matrix)

        # Report
        report_lines = [
            f"# IRT Report — {args.course}\n",
            f"**Alumnos:** {len(students)} | **Ítems:** {len(items)}\n",
            "| # | Ítem | Dificultad | Discriminación | p-valor | Flag |",
            "|---|------|------------|----------------|---------|------|",
        ]
        items_to_revise = []
        for r in irt_results:
            flags = []
            if r["discrimination"] < 0.2:
                flags.append("⚠️ Baja discriminación")
            if r["difficulty"] > 2.5:
                flags.append("❌ Muy difícil")
            if r["difficulty"] < -2.5:
                flags.append("⚠️ Trivial")
            flag_str = " / ".join(flags) if flags else "✅"
            item_name = items[r["item"] - 1] if r["item"] <= len(items) else f"Item-{r['item']}"
            report_lines.append(
                f"| {r['item']} | {item_name} | {r['difficulty']:+.2f} | {r['discrimination']:.2f} | {r['p_value']:.2f} | {flag_str} |"
            )
            if flags:
                items_to_revise.append({"item": item_name, "issues": flags})

        report = "\n".join(report_lines)
        (output_dir / "irt-report.md").write_text(report, encoding="utf-8")
        print(f"✅ IRT report: {output_dir / 'irt-report.md'}")

        if items_to_revise:
            revise = "# Ítems a Revisar\n\n"
            for item in items_to_revise:
                revise += f"- **{item['item']}**: {', '.join(item['issues'])}\n"
            (output_dir / "items-to-revise.md").write_text(revise, encoding="utf-8")
            print(f"⚠️ {len(items_to_revise)} ítems flaggeados para revisión")

        # BKT
        if args.bkt or True:  # Always run BKT when gradebook is provided
            bkt = BKTTracker()
            mastery_report = [
                f"# BKT Mastery — {args.course}\n",
                "| Alumno | Concepto | P(mastery) | Estado |",
                "|--------|----------|------------|--------|",
            ]
            for i, student in enumerate(students):
                for j, item_name in enumerate(items):
                    if matrix[i][j] >= 0:
                        bkt.update(f"{student}:{item_name}", matrix[i][j] == 1)
                        p = bkt.get_mastery(f"{student}:{item_name}")
                        estado = "✅ Dominado" if p > 0.95 else ("⚠️ En progreso" if p > 0.5 else "❌ Repaso urgente")
                        mastery_report.append(f"| {student} | {item_name} | {p:.3f} | {estado} |")

            (output_dir / "bkt-mastery.md").write_text("\n".join(mastery_report), encoding="utf-8")
            print(f"✅ BKT mastery: {output_dir / 'bkt-mastery.md'}")

    elif not args.gradebook:
        # Generate template CSV
        template = output_dir / "gradebook-template.csv"
        with open(template, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["alumno", "pregunta_1", "pregunta_2", "pregunta_3"])
            writer.writerow(["García, M.", "1", "0", "1"])
            writer.writerow(["López, J.", "1", "1", "0"])
        print(f"📝 Template CSV generado: {template}")
        print("  Completar con datos reales y ejecutar:")
        print(f"  python scripts/assessment_calibrator.py --course {args.course} --gradebook {template}")


if __name__ == "__main__":
    main()
