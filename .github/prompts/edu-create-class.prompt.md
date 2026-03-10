---
description: 'EDU Fase 3: Crear clase — genera minuta.md y filminas.md en el directorio del tema'
agent: 'agent'
tools: ['read', 'edit', 'search']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Check if `{project-root}/_edu/templates/class-template.md` exists.
   If yes → load it and pass it to Roberto as the structural constraint for minuta.md and filminas.md.
5. Load and follow the workflow at `{project-root}/_edu/workflows/topic-cycle/workflow.md`.
6. Purpose: Generate `{topic_folder}/minuta.md` and `{topic_folder}/filminas.md`.
   Content proportional to `class_duration` from topic.yaml. Requires approved diseno.md.

