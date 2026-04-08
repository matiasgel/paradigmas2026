---
description: 'EDU: Construir o explorar el Knowledge Graph universal de CS (ACM CC2023 + MIT OCW)'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Build the universal KG: `python scripts/universal_kg_builder.py --course {course_id} build`.
3. It includes 18 ACM/IEEE CC2023 Knowledge Areas with prerequisite relationships.
4. Optionally merge with course KG: `python scripts/universal_kg_builder.py --course {course_id} merge`.
5. Display a summary of knowledge areas and their relationships.
