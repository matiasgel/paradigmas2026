---
description: 'EDU: Validar Knowledge Graph buscando ciclos, huérfanos y anomalías Bloom'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run `python scripts/knowledge_graph.py --course {course_id} validate`.
3. If cycles are detected, display them and suggest corrections.
4. If orphan concepts exist, list them and suggest adding them to the KG.
5. If Bloom monotonicity warnings appear, recommend reordering or relabeling.
6. Present a summary: total concepts, edges, validation status.
