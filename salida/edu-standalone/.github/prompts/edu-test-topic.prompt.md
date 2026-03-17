---
description: 'EDU Fase 3: Testing pedagógico — simula experiencia de alumnos por perfil'
agent: 'edu-agent-student-simulator'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Load and follow the workflow at `{project-root}/_edu/workflows/pedagogical-testing/workflow.md`.
5. Purpose: Simulate the student experience for one or more profiles.
   Outputs: `{topic_folder}/score-pedagogico.md` and `{topic_folder}/faq-anticipado.md`.
   Requires quality loops completed.

