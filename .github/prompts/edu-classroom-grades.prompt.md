---
description: 'EDU: Obtener notas de GitHub Classroom para un assignment'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. If `classroom_enabled` is false, inform the user how to enable it and exit.
3. Run: `cd {project-root} && python scripts/classroom_publish.py grades --topic {topic_id} --course {course_id}`
4. Display the grades summary and any students flagged as at-risk.
5. Suggest running `/edu-student-analytics` for deeper analysis.
