---
description: 'EDU: Validar accesibilidad WCAG de filminas'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/validate_accessibility.py --topic {topic_id} --course {course_id}`
   - If `accessibility_check_enabled` is false, inform the user how to enable it.
3. If the report was generated, display a summary of the accessibility results.
4. Suggest fixes for any failing criteria (contrast, alt_text, font size).
