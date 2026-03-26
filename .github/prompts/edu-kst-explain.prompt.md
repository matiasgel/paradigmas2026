---
description: 'EDU: Explicar el siguiente concepto frontera KST al estudiante'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run `python scripts/knowledge_space.py --course {course_id} next --known "{known_concepts}"`.
3. The KST engine returns the optimal next concept based on prerequisite graph centrality.
4. Explain why this concept unlocks the most future learning.
5. Show the learning path: `python scripts/knowledge_space.py --course {course_id} path --target {concept} --known "{known}"`.
6. Generate a brief explanation of the concept tailored to the student's current knowledge.
