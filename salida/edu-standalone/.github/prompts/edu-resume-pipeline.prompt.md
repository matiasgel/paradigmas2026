---
description: 'EDU: Reanudar pipeline desde el último checkpoint exitoso'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Run the pipeline with `--resume`:
   ```
   python scripts/edu_director.py --resume --topic {topic_id} --course {course_id}
   ```
3. The pipeline reads `.pipeline-state.json` and resumes from the next step after the last success.
4. If no `.pipeline-state.json` exists, inform the user and suggest `/edu-run-pipeline`.
