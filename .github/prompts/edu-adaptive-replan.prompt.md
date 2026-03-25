---
description: 'EDU Fase 3: Replanificación adaptativa — ajustar cronograma respetando plan mínimo'
agent: 'edu-agent-course-planner'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` if exists → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as context.
   (Optional — active topic context helps scope the replan impact.)
3. Load and follow the workflow at `{project-root}/_edu/workflows/adaptive-replan/workflow.md`.

