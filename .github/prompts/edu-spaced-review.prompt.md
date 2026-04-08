---
description: 'EDU: Generar calendario de repasos distribuidos (FSRS v4)'
tools: ['read', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Determine the action:
   - **Generate calendar**: `cd {project-root} && python scripts/spaced_repetition.py --course {course_id} generate`
   - **Record a review**: `cd {project-root} && python scripts/spaced_repetition.py --course {course_id} --topic {topic_id} record --score {score}`
   - **View status**: `cd {project-root} && python scripts/spaced_repetition.py --course {course_id} status`
3. Display the generated calendar or review status.
4. If slides de repaso were generated, inform the user where to find them.
