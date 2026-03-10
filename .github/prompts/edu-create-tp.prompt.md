---
description: 'EDU Fase 3: Crear TP — genera tp.md trazable a la minuta y autograde-repo/ para GitHub Classroom en el directorio del tema'
agent: 'agent'
tools: ['read', 'edit', 'search']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Load and follow the workflow at `{project-root}/_edu/workflows/topic-cycle/workflow.md` — Step 5.
5. **Part A — TP:** Generate `{topic_folder}/tp.md`.
   Each consigna must be directly traceable to a section in `{topic_folder}/minuta.md`. Requires class created.
6. **Part B — Autograde Repo:** Immediately after tp.md is created, load and follow
   `{project-root}/_edu/workflows/create-autograde-repo/workflow.md` to generate
   `{topic_folder}/autograde-repo/` with starter code, tests and classroom.yml for GitHub Classroom.
   Both outputs (tp.md + autograde-repo/) are required to complete this step.

