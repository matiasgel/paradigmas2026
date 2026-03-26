---
description: 'EDU: Importar notas y generar dashboard de analytics de alumnos'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ask the user which operation:
   - **import-grades**: Import grades from a CSV file
   - **dashboard**: Generate analytics dashboard with risk alerts
3. For import: `cd {project-root} && python scripts/student_analytics.py import-grades --csv {csv_path} --course {course_id}`
4. For dashboard: `cd {project-root} && python scripts/student_analytics.py dashboard --course {course_id}`
5. Display the dashboard summary highlighting at-risk students (🔴 high risk, 🟡 medium risk).
6. Suggest `/edu-adaptive-path` for students flagged as at-risk.
