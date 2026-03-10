---
description: 'EDU Fase 3: Crear TP — genera tp.md trazable a la minuta. Pregunta si el TP usa GitHub Classroom para generar autograde-repo/ en el mismo paso.'
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
6. **Part B — Autograde (opcional):** After tp.md is generated, ask the professor:
   > "¿Este TP se entrega vía GitHub Classroom con autograding? (sí / no)"
   - If **sí** → load and follow `{project-root}/_edu/workflows/create-autograde-repo/workflow.md`
     to generate `{topic_folder}/autograde-repo/`.
   - If **no** → skip. The repo can be created later with `/edu-create-autograde-repo`.

