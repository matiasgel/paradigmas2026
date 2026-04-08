---
description: 'EDU Fase 3: Comparar encuesta real vs simulador — calibrar'
agent: 'edu-agent-student-simulator'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` if exists → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as context.
   (Optional — calibration can apply globally, but topic context improves analysis quality.)
3. Load and follow the workflow at `{project-root}/_edu/workflows/student-feedback-loop/workflow.md`.

