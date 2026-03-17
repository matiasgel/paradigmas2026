---
description: 'EDU Fase 3: Reabrir tema cerrado para correcciones mayores'
agent: 'edu-agent-topic-designer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Resolve topic to reopen:
   - If `{project-root}/_edu/active-topic.yaml` exists → load it as default, confirm: "¿Re-abrir el tema activo ({topic_name})?"
   - If not, or if user specifies a different topic → ask "¿Qué número de tema querés reabrir?"
     Scan `{project-root}/temas/` for that topic folder and load its `topic.yaml`
   - Store `{topic_folder}` as session variable
   - Update `{project-root}/_edu/active-topic.yaml` with the selected topic
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Load and follow the workflow at `{project-root}/_edu/workflows/reopen-topic/workflow.md`.
5. Purpose: Reopen a closed topic for major corrections. Reactivates Git branch `{git_branch}`.
   Updates `topic.yaml` status back to the appropriate state.

