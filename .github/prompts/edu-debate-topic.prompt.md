---
description: 'EDU Fase 3: Debate de Tema — Panel multi-agente para decisiones complejas de diseño'
agent: 'edu-agent-topic-designer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "No hay tema activo. Usá /edu-design-topic para iniciar un tema." → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Load and follow the workflow at `{project-root}/_edu/workflows/debate-topic/workflow.md`.
5. Purpose: Multi-agent debate panel for complex design, scope, and depth decisions for topic `{topic_name}`.
   Output: `{topic_folder}/debate-{date}.md`.

