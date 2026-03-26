---
description: 'EDU: Construir Knowledge Graph educativo desde plan mínimo y fuentes del curso'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ensure `knowledge_graph_enabled: true` in config.
3. Run `python scripts/knowledge_graph.py --course {course_id} build`.
4. Review the generated `knowledge-graph.json` with the teacher.
5. If the teacher wants to add manual relations, edit the JSON-LD directly.
6. Optionally run CPL inference: `python scripts/prerequisite_learner.py --course {course_id} predict`.
7. Validate: `python scripts/knowledge_graph.py --course {course_id} validate`.
8. Generate visualization: `python scripts/knowledge_graph.py --course {course_id} visualize`.
