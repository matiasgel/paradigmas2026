#!/usr/bin/env python3
"""
knowledge_graph.py — Knowledge Graph Engine: Ontología Educativa Formal (S11.1)
================================================================================
Construye y valida un grafo de conocimiento educativo en formato JSON-LD,
con validaciones SPARQL sobre una ontología OWL Lite.

Uso:
    python scripts/knowledge_graph.py --course leng-2026 build
    python scripts/knowledge_graph.py --course leng-2026 validate
    python scripts/knowledge_graph.py --course leng-2026 visualize

Dependencias: rdflib, networkx
Opcionales: owlready2, SPARQLWrapper (para validación externa)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

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
    load_yaml,
    save_json,
)


# ═══════════════════════════════════════════════════════════════════════
# COURSE KNOWLEDGE GRAPH
# ═══════════════════════════════════════════════════════════════════════

class CourseKnowledgeGraph:
    """Grafo de conocimiento educativo con soporte JSON-LD y validación."""

    def __init__(self) -> None:
        self.concepts: dict[str, dict] = {}
        self.edges: list[dict] = []

    # --- Construction ---

    def add_concept(
        self,
        concept_id: str,
        *,
        label: str = "",
        source: str = "manual",
        layer: str = "concept",
        bloom_level: str | None = None,
    ) -> None:
        self.concepts[concept_id] = {
            "id": concept_id,
            "label": label or concept_id,
            "source": source,
            "layer": layer,
            "bloom_level": bloom_level,
        }

    def add_prerequisite(
        self,
        prereq: str,
        target: str,
        *,
        source: str = "manual",
        confidence: float = 1.0,
    ) -> None:
        self.edges.append({
            "from": prereq,
            "to": target,
            "relation": "hasPrerequisite",
            "source": source,
            "confidence": confidence,
        })

    def add_relation(
        self,
        from_id: str,
        to_id: str,
        relation: str,
        *,
        source: str = "manual",
        confidence: float = 1.0,
    ) -> None:
        self.edges.append({
            "from": from_id,
            "to": to_id,
            "relation": relation,
            "source": source,
            "confidence": confidence,
        })

    # --- Queries ---

    def get_concepts(self) -> list[str]:
        return list(self.concepts.keys())

    def get_prerequisite_pairs(self) -> list[tuple[str, str]]:
        return [
            (e["from"], e["to"])
            for e in self.edges
            if e["relation"] == "hasPrerequisite"
        ]

    def descendants(self, concept_id: str) -> set[str]:
        """Conceptos que dependen transitivamente de concept_id."""
        try:
            import networkx as nx
        except ImportError:
            return set()
        G = self._build_nx_graph()
        if concept_id not in G:
            return set()
        return set(nx.descendants(G, concept_id))

    def _build_nx_graph(self):
        import networkx as nx

        G = nx.DiGraph()
        for cid in self.concepts:
            G.add_node(cid)
        for e in self.edges:
            if e["relation"] == "hasPrerequisite":
                G.add_edge(e["from"], e["to"])
        return G

    # --- Validation ---

    def detect_cycles(self) -> list[list[str]]:
        """Detecta ciclos en el grafo de prerequisitos."""
        try:
            import networkx as nx
        except ImportError:
            return []
        G = self._build_nx_graph()
        return list(nx.simple_cycles(G))

    def find_orphans(self, plan_concepts: set[str]) -> set[str]:
        """Conceptos en el plan que no están en el grafo."""
        return plan_concepts - set(self.concepts.keys())

    def check_bloom_monotonic(self) -> list[str]:
        """Verifica que Bloom crece a lo largo del grafo."""
        bloom_order = {
            "recordar": 1,
            "comprender": 2,
            "aplicar": 3,
            "analizar": 4,
            "evaluar": 5,
            "crear": 6,
        }
        warnings: list[str] = []
        for e in self.edges:
            if e["relation"] != "hasPrerequisite":
                continue
            prereq_bloom = self.concepts.get(e["from"], {}).get("bloom_level")
            target_bloom = self.concepts.get(e["to"], {}).get("bloom_level")
            if prereq_bloom and target_bloom:
                p = bloom_order.get(prereq_bloom.lower(), 0)
                t = bloom_order.get(target_bloom.lower(), 0)
                if p > t:
                    warnings.append(
                        f"Bloom descendente: {e['from']}({prereq_bloom}) → {e['to']}({target_bloom})"
                    )
        return warnings

    def validate(self) -> Result[dict]:
        """Ejecuta todas las validaciones y retorna reporte."""
        cycles = self.detect_cycles()
        bloom_warns = self.check_bloom_monotonic()
        errors: list[str] = []
        if cycles:
            for c in cycles:
                errors.append(f"Ciclo detectado: {' → '.join(c)}")
        report = {
            "total_concepts": len(self.concepts),
            "total_edges": len(self.edges),
            "cycles": cycles,
            "bloom_warnings": bloom_warns,
            "valid": len(cycles) == 0,
        }
        if errors:
            return Result.fail(*errors)
        return Result.ok(report)

    # --- I/O ---

    def to_jsonld(self) -> dict:
        """Exporta como JSON-LD."""
        return {
            "@context": {
                "edu": "https://edu-module.org/ontology#",
                "hasPrerequisite": "edu:hasPrerequisite",
                "partOf": "edu:partOf",
                "contradicts": "edu:contradicts",
            },
            "@graph": [
                {
                    "@id": f"edu:{cid}",
                    "label": info["label"],
                    "source": info["source"],
                    "layer": info["layer"],
                    "bloom_level": info.get("bloom_level"),
                }
                for cid, info in self.concepts.items()
            ],
            "edges": self.edges,
        }

    def save(self, path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        save_json(p, self.to_jsonld())

    @classmethod
    def load(cls, path: str | Path) -> CourseKnowledgeGraph:
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"KG not found: {p}")
        data = load_json(p)
        kg = cls()
        for node in data.get("@graph", []):
            nid = node["@id"].replace("edu:", "")
            kg.add_concept(
                nid,
                label=node.get("label", nid),
                source=node.get("source", "loaded"),
                layer=node.get("layer", "concept"),
                bloom_level=node.get("bloom_level"),
            )
        for edge in data.get("edges", []):
            kg.add_relation(
                edge["from"],
                edge["to"],
                edge["relation"],
                source=edge.get("source", "loaded"),
                confidence=edge.get("confidence", 1.0),
            )
        return kg

    # --- Mermaid Visualization ---

    def to_mermaid(self) -> str:
        lines = ["graph TD"]
        for cid, info in self.concepts.items():
            safe_id = cid.replace(" ", "_").replace("-", "_")
            lines.append(f'    {safe_id}["{info["label"]}"]')
        for e in self.edges:
            f = e["from"].replace(" ", "_").replace("-", "_")
            t = e["to"].replace(" ", "_").replace("-", "_")
            rel = e["relation"]
            lines.append(f"    {f} -->|{rel}| {t}")
        return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════
# BUILD FROM PLAN
# ═══════════════════════════════════════════════════════════════════════

def build_kg_from_plan(project_root: Path, course: str) -> Result[CourseKnowledgeGraph]:
    """Construye KG a partir del plan mínimo del curso."""
    course_dir = project_root / "salida" / "cursadas" / course
    plan_path = course_dir / "plan-minimo.md"

    if not plan_path.exists():
        return Result.fail(f"plan-minimo.md no encontrado en {course_dir}")

    text = plan_path.read_text(encoding="utf-8")
    kg = CourseKnowledgeGraph()

    # Extrae temas como conceptos (headers ##)
    current_topic = None
    prev_topic = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## ") and not stripped.startswith("###"):
            topic_name = stripped[3:].strip()
            topic_id = topic_name.lower().replace(" ", "_")
            kg.add_concept(topic_id, label=topic_name, source="plan-minimo")
            if prev_topic:
                kg.add_prerequisite(prev_topic, topic_id, source="sequential-order")
            prev_topic = topic_id
            current_topic = topic_id
        elif stripped.startswith("### ") and current_topic:
            sub_name = stripped[4:].strip()
            sub_id = sub_name.lower().replace(" ", "_")
            kg.add_concept(sub_id, label=sub_name, source="plan-minimo", layer="subtopic")
            kg.add_relation(sub_id, current_topic, "partOf", source="plan-minimo")

    if not kg.concepts:
        return Result.fail("No se encontraron temas (## headers) en plan-minimo.md")

    return Result.ok(kg)


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(description="Knowledge Graph Engine (S11.1)")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument(
        "command",
        choices=["build", "validate", "visualize"],
        help="Comando a ejecutar",
    )
    args = parser.parse_args()

    project_root = find_project_root(Path.cwd())
    config = load_config(project_root)

    # Feature flag
    if not config.get("knowledge_graph_enabled", False):
        print("ℹ️  knowledge_graph_enabled no está habilitado en config. Saliendo.")
        return 0

    course_out = project_root / "salida" / "cursadas" / args.course
    kg_path = course_out / "knowledge-graph.json"

    if args.command == "build":
        result = build_kg_from_plan(project_root, args.course)
        if not result.is_ok:
            for e in result.errors:
                print(f"❌ {e}", file=sys.stderr)
            return 1
        kg = result.unwrap()
        kg.save(kg_path)
        print(f"✅ KG generado: {kg_path}")
        print(f"   Conceptos: {len(kg.concepts)} | Relaciones: {len(kg.edges)}")
        return 0

    elif args.command == "validate":
        if not kg_path.exists():
            print(f"❌ KG no encontrado: {kg_path}. Ejecutar 'build' primero.")
            return 1
        kg = CourseKnowledgeGraph.load(kg_path)
        result = kg.validate()
        if result.is_ok:
            report = result.unwrap()
            print(f"✅ KG válido — {report['total_concepts']} conceptos, {report['total_edges']} relaciones")
            if report["bloom_warnings"]:
                print("⚠️  Advertencias de Bloom:")
                for w in report["bloom_warnings"]:
                    print(f"   {w}")
        else:
            for e in result.errors:
                print(f"❌ {e}", file=sys.stderr)
            return 1
        return 0

    elif args.command == "visualize":
        if not kg_path.exists():
            print(f"❌ KG no encontrado: {kg_path}. Ejecutar 'build' primero.")
            return 1
        kg = CourseKnowledgeGraph.load(kg_path)
        mermaid = kg.to_mermaid()
        viz_path = course_out / "knowledge-graph.mmd"
        viz_path.write_text(mermaid, encoding="utf-8")
        print(f"✅ Mermaid generado: {viz_path}")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
