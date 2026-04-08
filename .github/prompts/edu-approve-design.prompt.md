---
description: 'EDU Fase 3: Aprobar diseño de tema — habilita creación de clase'
agent: 'edu-agent-plan-coverage-checker'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Load and follow the workflow at `{project-root}/_edu/workflows/topic-cycle/workflow.md`.
5. Purpose: Approve topic design. Target file: `{topic_folder}/diseno.md`. Required before /edu-create-class.

