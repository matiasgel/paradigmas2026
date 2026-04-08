---
description: 'EDU: Auditar composición visual de filminas'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/validate_slide_composition.py --topic {topic_id} --course {course_id}`
3. Display a summary of the composition audit: density grades, overlaps, margin alerts.
4. For slides graded C or F, suggest specific improvements to improve visual density.
