---
description: 'EDU: Validar reglas cognitivas de filminas (Mayer/Fiorella/Assertion-Evidence)'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run: `cd {project-root} && python scripts/validate_layout_cognition.py --topic {topic_id} --course {course_id}`
   - If `cognitive_validation_enabled` is false, inform the user how to enable it.
3. Display a summary of cognitive issues: assertion-evidence violations, density problems, sequence issues.
4. For each warning, explain the cognitive science principle and suggest specific improvements.
