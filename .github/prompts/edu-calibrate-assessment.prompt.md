---
description: 'EDU: Calibrar dificultad de ítems con IRT y estimar dominio con BKT'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/assessment_calibrator.py --course {course_id} --gradebook {csv_path}`
   - If no gradebook CSV exists, the script generates a template.
3. Display the IRT report: difficulty, discrimination, and p-value per item.
4. Flag items with low discrimination (<0.2) or extreme difficulty for revision.
5. Display the BKT mastery report: concept mastery probability per student.
6. Suggest integrating with `/edu-spaced-review` for students below mastery threshold.
