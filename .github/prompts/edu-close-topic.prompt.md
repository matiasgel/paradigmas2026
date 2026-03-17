---
description: 'EDU Fase 3: Cerrar tema — commit + merge Git, actualiza cobertura y topic.yaml'
agent: 'edu-agent-topic-designer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "No hay tema activo. Usá /edu-topic para detectar el estado." → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Load and follow the workflow at `{project-root}/_edu/workflows/topic-cycle/workflow.md`.
5. Purpose: Close topic when all quality loops are resolved. Updates `{topic_folder}/topic.yaml` status to "closed".
   Generates Git commit and merge on branch `{git_branch}`. El commit debe incluir TODOS los artefactos del tema: `diseno.md`, `minuta.md`, `filminas.md`, `guia-estudio.md` (si existe), `guia-estudio.pdf` (si existe), `tp.md`, todos los reportes de calidad y scores de testing. Updates coverage matrix.
6. After successful close:
   - Clear `{project-root}/_edu/active-topic.yaml` (delete or set all fields to empty)
     so that the next `/edu-topic` or `/edu-design-topic` starts fresh.
   - Inform: "✅ Tema {topic_name} cerrado. `active-topic.yaml` limpiado. Cuando quieras continuar, usá /edu-topic."

