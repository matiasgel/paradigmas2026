#!/usr/bin/env python3
"""
universal_kg_builder.py — Universal CS Knowledge Graph Builder (S13.2)
======================================================================
Construye un KG universal de CS desde fuentes abiertas:
  - ACM/IEEE CC2023 (14 KAs, 52 KUs) — embebido
  - MIT OCW sitemap (opcional, requiere red)

Uso:
    python scripts/universal_kg_builder.py --course leng-2026 build
    python scripts/universal_kg_builder.py --course leng-2026 merge

Dependencias: networkx, requests (opcional)
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

from pipeline_common import find_project_root, load_config, save_json


# ═══════════════════════════════════════════════════════════════════════
# ACM/IEEE CC2023 DATA (embebido — no requiere scraping)
# ═══════════════════════════════════════════════════════════════════════

ACM_CC2023_KAS: dict[str, str] = {
    "AL": "Algorithms and Complexity",
    "AR": "Architecture and Organization",
    "CN": "Computational Science",
    "DS": "Discrete Structures",
    "GV": "Graphics and Visualization",
    "HCI": "Human-Computer Interaction",
    "IAS": "Information Assurance and Security",
    "IM": "Information Management",
    "IS": "Intelligent Systems",
    "NC": "Networking and Communication",
    "OS": "Operating Systems",
    "PBD": "Platform-Based Development",
    "PD": "Parallel and Distributed Computing",
    "PL": "Programming Languages",
    "SDF": "Software Development Fundamentals",
    "SE": "Software Engineering",
    "SF": "Systems Fundamentals",
    "SP": "Social Issues and Professional Practice",
}

# Prerequisitos inter-KA basados en CC2023 §3
CC2023_PREREQS: list[tuple[str, str]] = [
    ("DS", "AL"),
    ("DS", "PL"),
    ("SDF", "SE"),
    ("SDF", "PL"),
    ("AR", "OS"),
    ("OS", "NC"),
    ("OS", "PD"),
    ("AL", "IS"),
    ("IM", "IS"),
    ("DS", "IS"),
    ("SF", "AR"),
    ("SF", "OS"),
    ("PL", "SE"),
    ("SDF", "AL"),
]


# ═══════════════════════════════════════════════════════════════════════
# BUILDER
# ═══════════════════════════════════════════════════════════════════════

class UniversalKGBuilder:
    """Construye y fusiona el KG universal de CS desde fuentes abiertas."""

    def __init__(self) -> None:
        self.nodes: list[dict] = []
        self.edges: list[dict] = []

    def ingest_acm_cc2023(self) -> None:
        """Ingesta las 18 Knowledge Areas de ACM/IEEE CC2023."""
        for ka_code, ka_name in ACM_CC2023_KAS.items():
            self.nodes.append({
                "@id": f"acm:{ka_code}",
                "label": ka_name,
                "source": "ACM/IEEE CC2023",
                "layer": "KA",
                "bloom_level": None,
            })
        for prereq, target in CC2023_PREREQS:
            self.edges.append({
                "from": prereq,
                "to": target,
                "relation": "hasPrerequisite",
                "source": "ACM/IEEE CC2023",
                "confidence": 1.0,
            })

    def ingest_mit_ocw(self, max_courses: int = 50) -> int:
        """Ingesta títulos de cursos MIT OCW (requiere red)."""
        try:
            import requests
        except ImportError:
            print("⚠️  requests no instalado — omitiendo MIT OCW")
            return 0

        try:
            resp = requests.get(
                "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/",
                timeout=10,
            )
            resp.raise_for_status()
        except Exception:
            print("⚠️  No se pudo acceder a MIT OCW — modo offline")
            return 0

        # Parse basic course info from the page
        count = 0
        for line in resp.text.split("\n"):
            if "/courses/6-" in line and count < max_courses:
                # Extract course number
                import re

                match = re.search(r"/courses/(6-[\w-]+)", line)
                if match:
                    course_id = match.group(1)
                    label = course_id.replace("-", " ").title()
                    self.nodes.append({
                        "@id": f"mit:{course_id}",
                        "label": label,
                        "source": "MIT OCW",
                        "layer": "course",
                        "bloom_level": None,
                    })
                    count += 1
        return count

    def to_jsonld(self) -> dict:
        """Exporta como JSON-LD."""
        return {
            "@context": {
                "edu": "https://edu-module.org/ontology#",
                "acm": "https://www.acm.org/education/curricula/cc2023#",
                "mit": "https://ocw.mit.edu/courses/",
            },
            "@graph": self.nodes,
            "edges": self.edges,
        }

    def build(self, output_path: Path) -> Path:
        """Construye y guarda el KG universal."""
        self.ingest_acm_cc2023()
        mit_count = self.ingest_mit_ocw()
        save_json(output_path, self.to_jsonld())
        print(f"✅ KG universal generado: {output_path}")
        print(f"   ACM/IEEE CC2023: {len(ACM_CC2023_KAS)} KAs, {len(CC2023_PREREQS)} prereqs")
        if mit_count:
            print(f"   MIT OCW: {mit_count} cursos")
        return output_path


def merge_with_course_kg(universal_path: Path, course_kg_path: Path) -> None:
    """Fusiona el KG universal con el KG del curso."""
    from knowledge_graph import CourseKnowledgeGraph

    course_kg = CourseKnowledgeGraph.load(course_kg_path)
    from pipeline_common import load_json

    universal = load_json(universal_path)

    # Agregar nodos del KG universal que no existen en el curso
    for node in universal.get("@graph", []):
        nid = node["@id"].replace("acm:", "").replace("mit:", "")
        if nid not in course_kg.concepts:
            course_kg.add_concept(
                nid,
                label=node.get("label", nid),
                source=node.get("source", "universal"),
                layer=node.get("layer", "KA"),
            )

    course_kg.save(course_kg_path)
    print(f"✅ KG del curso fusionado con KG universal → {course_kg_path}")


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(description="Universal CS KG Builder (S13.2)")
    parser.add_argument("--course", required=True, help="ID del curso")
    parser.add_argument(
        "command",
        choices=["build", "merge"],
        help="build: generar KG universal | merge: fusionar con KG del curso",
    )
    args = parser.parse_args()

    project_root = find_project_root(Path.cwd())
    config = load_config(project_root)

    if not config.get("knowledge_graph_enabled", False):
        print("ℹ️  knowledge_graph_enabled no está habilitado. Saliendo.")
        return 0

    universal_path = project_root / "_edu-knowledge" / "universal-kg.json"

    if args.command == "build":
        builder = UniversalKGBuilder()
        builder.build(universal_path)
        return 0

    elif args.command == "merge":
        course_kg_path = (
            project_root / "salida" / "cursadas" / args.course / "knowledge-graph.json"
        )
        if not course_kg_path.exists():
            print(f"❌ KG del curso no encontrado: {course_kg_path}")
            return 1
        if not universal_path.exists():
            print(f"❌ KG universal no encontrado: {universal_path}. Ejecute 'build' primero.")
            return 1
        merge_with_course_kg(universal_path, course_kg_path)
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
