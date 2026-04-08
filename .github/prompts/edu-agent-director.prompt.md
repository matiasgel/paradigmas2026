---
description: 'EDU: Ejecutar el Director Agent inteligente con smolagents para producción autónoma'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ensure `orchestrator_enabled: true` and `orchestrator_mode: "smolagents"` in config.
3. Ensure `HF_TOKEN` is set as environment variable.
4. Run: `python scripts/edu_smolagent_director.py --topic {topic_id} --course {course_id}`
5. The agent uses Qwen/Llama via HuggingFace Inference API to orchestrate the pipeline.
6. If HF_TOKEN is missing, the system falls back to the minimal director (edu_director.py).
7. Monitor the agent's decisions and approve at human gates.
