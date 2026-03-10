---
description: 'EDU Fase 3: Cerrar tema — commit + merge Git, actualiza cobertura y topic.yaml'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "No hay tema activo. Usá /edu-topic para detectar el estado." → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Load and follow the workflow at `{project-root}/_edu/workflows/topic-cycle/workflow.md`.
5. Purpose: Close topic when all quality loops are resolved. Updates `{topic_folder}/topic.yaml` status to "closed".
   Generates Git commit and merge on branch `{git_branch}`. Updates coverage matrix.

