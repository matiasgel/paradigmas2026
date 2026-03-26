#!/usr/bin/env python3
"""
knowledge_space.py — KST Engine: Knowledge Space Theory (S13.1)
================================================================
Motor de Knowledge Space Theory sobre el Knowledge Graph del curso.
Implementa frontier(), next_concept(), learning_path().

Uso:
    python scripts/knowledge_space.py --course leng-2026 frontier --known "algebra,listas"
    python scripts/knowledge_space.py --course leng-2026 next --known "algebra,listas"
    python scripts/knowledge_space.py --course leng-2026 path --target grafos --known "algebra,listas"

Dependencias: networkx (ya instalado)
Opcional: aloha (pip install aloha)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_this = Path(__file__).resolve()
_scripts = _this.parent
_root = _scripts.parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from pipeline_common import find_project_root, load_config


# ═══════════════════════════════════════════════════════════════════════
# KST ENGINE
# ═══════════════════════════════════════════════════════════════════════

class KSTEngine:
    """Motor KST que integra el KG del curso con mastery scores."""

    def __init__(self, kg_path: str | Path) -> None:
        from knowledge_graph import CourseKnowledgeGraph

        self.kg = CourseKnowledgeGraph.load(kg_path)
        self._prereq_map: dict[str, set[str]] = {}
        self._build_prereq_map()

    def _build_prereq_map(self) -> None:
        """Construye mapa de prerequisitos directos por concepto."""
        for edge in self.kg.edges:
            if edge["relation"] == "hasPrerequisite":
                target = edge["to"]
                prereq = edge["from"]
                if target not in self._prereq_map:
                    self._prereq_map[target] = set()
                self._prereq_map[target].add(prereq)

    def frontier(self, known_concepts: set[str]) -> list[str]:
        """
        Conceptos en la frontera de aprendizaje:
        conceptos que el estudiante AÚN NO conoce pero cuyos
        prerequisitos YA fueron dominados.
        """
        all_concepts = set(self.kg.get_concepts())
        unknown = all_concepts - known_concepts
        result = []
        for concept in unknown:
            prereqs = self._prereq_map.get(concept, set())
            if prereqs.issubset(known_concepts):
                result.append(concept)
        return sorted(result)

    def next_concept(self, student_state: dict[str, float]) -> str | None:
        """
        Dado el estado del estudiante (concepto → mastery 0-1),
        concepto frontera con mayor utilidad pedagógica.
        Prioriza conceptos con muchos descendientes (alto impacto).
        """
        known = {c for c, score in student_state.items() if score >= 0.75}
        candidates = self.frontier(known)
        if not candidates:
            return None
        # Ordenar por centralidad (más descendientes = mayor prioridad)
        scored = [(c, len(self.kg.descendants(c))) for c in candidates]
        return max(scored, key=lambda x: x[1])[0]

    def learning_path(
        self, target_concept: str, student_state: dict[str, float]
    ) -> list[str]:
        """
        Camino mínimo de aprendizaje desde el estado actual
        hasta poder aprender target_concept.
        """
        known = {c for c, score in student_state.items() if score >= 0.75}
        if target_concept in known:
            return []

        # BFS inverso: encontrar todos los prerequisitos no dominados
        path: list[str] = []
        to_visit = [target_concept]
        visited = set()

        while to_visit:
            current = to_visit.pop(0)
            if current in visited:
                continue
            visited.add(current)

            if current not in known and current != target_concept:
                path.append(current)

            prereqs = self._prereq_map.get(current, set())
            for p in prereqs:
                if p not in known and p not in visited:
                    to_visit.append(p)

        # Ordenar topológicamente (prerequisitos primero)
        path.reverse()
        path.append(target_concept)
        return path


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(description="KST Engine (S13.1)")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument(
        "command",
        choices=["frontier", "next", "path"],
        help="Comando a ejecutar",
    )
    parser.add_argument("--known", type=str, default="", help="Conceptos conocidos (comma-separated)")
    parser.add_argument("--target", type=str, help="Concepto objetivo (para 'path')")
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

    engine = KSTEngine(kg_path)
    known = set(args.known.split(",")) if args.known else set()
    state = {c: 1.0 for c in known}

    if args.command == "frontier":
        front = engine.frontier(known)
        print(f"📚 Frontera de aprendizaje ({len(front)} conceptos):")
        for c in front:
            print(f"   • {c}")

    elif args.command == "next":
        nxt = engine.next_concept(state)
        if nxt:
            desc = len(engine.kg.descendants(nxt))
            print(f"🎯 Siguiente concepto recomendado: {nxt} (desbloquea {desc} conceptos)")
        else:
            print("🎓 ¡Todos los conceptos dominados!")

    elif args.command == "path":
        if not args.target:
            print("❌ --target requerido para el comando 'path'")
            return 1
        path = engine.learning_path(args.target, state)
        print(f"🗺️  Camino hacia '{args.target}' ({len(path)} pasos):")
        for i, c in enumerate(path, 1):
            marker = "🎯" if c == args.target else "📖"
            print(f"   {i}. {marker} {c}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
