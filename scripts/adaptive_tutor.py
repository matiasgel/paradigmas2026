#!/usr/bin/env python3
"""
adaptive_tutor.py — Adaptive Tutor: KST + BKT + Director (S13.3)
==================================================================
Tutor adaptativo sin currícula fija. Integra KSTEngine para
recomendar el siguiente concepto y genera contenido on-demand.

Uso:
    python scripts/adaptive_tutor.py --course leng-2026 --student est01 recommend
    python scripts/adaptive_tutor.py --course leng-2026 --student est01 summary

Dependencias: S13.1 (knowledge_space.py), S10.2 (assessment_calibrator.py BKTTracker)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_this = Path(__file__).resolve()
_scripts = _this.parent
_root = _scripts.parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from pipeline_common import find_project_root, load_config, load_json, save_json


# ═══════════════════════════════════════════════════════════════════════
# SIMPLE BKT STATE MANAGER
# ═══════════════════════════════════════════════════════════════════════

class StudentState:
    """Gestión simple del estado de mastery del estudiante."""

    def __init__(self, student_id: str, state_dir: Path) -> None:
        self.student_id = student_id
        self.state_path = state_dir / f"student-{student_id}.json"
        self.mastery: dict[str, float] = {}
        self._load()

    def _load(self) -> None:
        if self.state_path.exists():
            data = load_json(self.state_path)
            self.mastery = data.get("mastery", {})

    def save(self) -> None:
        save_json(self.state_path, {
            "student_id": self.student_id,
            "mastery": self.mastery,
        })

    def update(self, concept: str, correct: bool) -> None:
        """Actualiza mastery con BKT simplificado."""
        p_L0 = self.mastery.get(concept, 0.3)  # prior
        p_T = 0.15   # P(transit)
        p_S = 0.10   # P(slip)
        p_G = 0.25   # P(guess)

        if correct:
            p_L_given_obs = (p_L0 * (1 - p_S)) / (p_L0 * (1 - p_S) + (1 - p_L0) * p_G)
        else:
            p_L_given_obs = (p_L0 * p_S) / (p_L0 * p_S + (1 - p_L0) * (1 - p_G))

        p_L_new = p_L_given_obs + (1 - p_L_given_obs) * p_T
        self.mastery[concept] = round(min(p_L_new, 1.0), 4)
        self.save()

    def get_all_mastery(self) -> dict[str, float]:
        return dict(self.mastery)


# ═══════════════════════════════════════════════════════════════════════
# ADAPTIVE TUTOR
# ═══════════════════════════════════════════════════════════════════════

class AdaptiveTutor:
    """Tutor adaptativo: estado → concepto frontera KST → contenido on-demand."""

    def __init__(
        self,
        student_id: str,
        kg_path: str | Path,
        state_dir: Path,
    ) -> None:
        from knowledge_space import KSTEngine

        self.student_id = student_id
        self.kst = KSTEngine(kg_path)
        self.state = StudentState(student_id, state_dir)

    def recommend_next(self) -> dict:
        """Recomienda el siguiente concepto a aprender."""
        mastery = self.state.get_all_mastery()
        nxt = self.kst.next_concept(mastery)
        if not nxt:
            return {"concept": None, "message": "¡Felicitaciones! Dominaste todos los conceptos."}

        path = self.kst.learning_path(nxt, mastery)
        desc_count = len(self.kst.kg.descendants(nxt))
        return {
            "concept": nxt,
            "learning_path": path,
            "unlocks": desc_count,
            "why": f"Desbloquea {desc_count} conceptos futuros.",
        }

    def update_after_assessment(self, concept: str, correct: bool) -> None:
        """Actualiza estado BKT después de una evaluación."""
        self.state.update(concept, correct)

    def session_summary(self) -> dict:
        """Resumen del estado del estudiante."""
        mastery = self.state.get_all_mastery()
        known = {c for c, s in mastery.items() if s >= 0.75}
        frontier = self.kst.frontier(known)
        total = len(self.kst.kg.get_concepts())
        return {
            "student_id": self.student_id,
            "mastered": len(known),
            "total_concepts": total,
            "progress_pct": round(len(known) / total * 100, 1) if total > 0 else 0,
            "frontier": frontier[:10],
            "frontier_size": len(frontier),
        }


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(description="Adaptive Tutor (S13.3)")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument("--student", required=True, help="ID del estudiante")
    parser.add_argument(
        "command",
        choices=["recommend", "summary", "update"],
        help="recommend: siguiente concepto | summary: estado | update: registrar respuesta",
    )
    parser.add_argument("--concept", type=str, help="Concepto (para 'update')")
    parser.add_argument("--correct", action="store_true", help="Respuesta correcta (para 'update')")
    args = parser.parse_args()

    project_root = find_project_root(Path.cwd())
    config = load_config(project_root)

    if not config.get("knowledge_graph_enabled", False):
        print("ℹ️  knowledge_graph_enabled no está habilitado. Saliendo.")
        return 0

    kg_path = project_root / "salida" / "cursadas" / args.course / "knowledge-graph.json"
    if not kg_path.exists():
        print(f"❌ KG no encontrado: {kg_path}. Ejecutar 'knowledge_graph.py build' primero.")
        return 1

    state_dir = project_root / "salida" / "cursadas" / args.course / "students"
    state_dir.mkdir(parents=True, exist_ok=True)

    tutor = AdaptiveTutor(args.student, kg_path, state_dir)

    if args.command == "recommend":
        rec = tutor.recommend_next()
        if rec.get("concept"):
            print(f"🎯 Siguiente concepto: {rec['concept']}")
            print(f"   {rec['why']}")
            if rec["learning_path"]:
                print(f"   Camino: {' → '.join(rec['learning_path'])}")
        else:
            print(f"🎓 {rec['message']}")

    elif args.command == "summary":
        s = tutor.session_summary()
        print(f"📊 Estudiante: {s['student_id']}")
        print(f"   Progreso: {s['mastered']}/{s['total_concepts']} ({s['progress_pct']}%)")
        print(f"   Frontera: {s['frontier_size']} conceptos disponibles")
        if s["frontier"]:
            print(f"   Próximos: {', '.join(s['frontier'][:5])}")

    elif args.command == "update":
        if not args.concept:
            print("❌ --concept requerido para 'update'")
            return 1
        tutor.update_after_assessment(args.concept, args.correct)
        m = tutor.state.mastery.get(args.concept, 0)
        status = "✅" if args.correct else "❌"
        print(f"{status} {args.concept}: mastery = {m:.2f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
