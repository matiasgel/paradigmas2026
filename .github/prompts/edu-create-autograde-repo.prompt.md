---
description: 'EDU Fase 3: Crear Repo Autograde — genera estructura completa de GitHub Classroom con autograding trazable al tp.md'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}`.
   If not found → "Primero iniciá un tema con /edu-topic" → STOP.
3. Verify `{project-root}/{topic_folder}/tp.md` exists.
   If not → "Primero creá el TP con /edu-create-tp" → STOP.
4. Load and follow the workflow at `{project-root}/_edu/workflows/create-autograde-repo/workflow.md`.
5. Purpose: Generate `{topic_folder}/autograde-repo/` with the complete GitHub Classroom template repo.
   Each test in `autograding.json` must be directly traceable to a consigna in `{topic_folder}/tp.md`.

