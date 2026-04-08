---
description: 'EDU: Ejecutar pipeline completo de producción de un tema con checkpoints'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ensure `orchestrator_enabled: true` in config.
3. Run the pipeline:
   ```
   python scripts/edu_director.py --topic {topic_id} --course {course_id}
   ```
4. The pipeline executes steps sequentially with checkpoints:
   validate_plan → fact_check → slides_pipeline → capture_thumbnails → visual_quality → [GATE] → semantic_drift → bloom_classify → [FINAL GATE]
5. If a step fails, the pipeline stops. Use `/edu-resume-pipeline` to retry.
6. For CI/CD: add `--skip-gates` to run non-interactively.
7. For simulation: add `--dry-run` to preview steps without execution.
