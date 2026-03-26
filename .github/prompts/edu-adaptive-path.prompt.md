---
description: 'EDU: Generar rutas de aprendizaje adaptativas por nivel de rendimiento'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/adaptive_path.py --course {course_id} --topic {topic_id}`
   - Optionally add `--student "Apellido, N."` for a specific student.
3. Display the three generated routes: avanzada (≥80%), estándar (50-79%), refuerzo (<50%).
4. If no grade data is available, inform the user that all three generic routes were generated.
5. Suggest running `/edu-student-analytics import-grades` first if grade data is missing.
