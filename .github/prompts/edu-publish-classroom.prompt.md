---
description: 'EDU: Publicar TP a GitHub Classroom como assignment'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. If `classroom_enabled` is false, inform the user how to enable it and exit.
3. Run: `cd {project-root} && python scripts/classroom_publish.py --topic {topic_id} --course {course_id}`
4. Display the invite link returned by the script.
5. If the script fails (e.g., `gh` not installed), display the error and link to installation instructions.
