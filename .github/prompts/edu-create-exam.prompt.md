---
description: 'EDU: Generar blueprint de examen (tabla de especificaciones)'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ask the user (if not provided in the prompt):
   - Which topics to include (comma-separated topic IDs)
   - Total points (default: 100)
   - Exam duration in minutes (default: 120)
   - Bloom profile: default | practical | research | introductory
3. Run: `cd {project-root} && python scripts/generate_exam_blueprint.py --course {course_id} --topics "{topics}" --points {points} --time {time} --bloom-profile {profile}`
4. Display the generated blueprint matrix and Bloom distribution.
5. Suggest adjustments if any topic has disproportionate weight.
