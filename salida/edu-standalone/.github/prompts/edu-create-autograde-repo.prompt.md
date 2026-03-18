---
description: 'EDU: Regenerar Repo Autograde — regenera o ajusta autograde-repo/ a partir del tp.md actual. La creación inicial es automática con /edu-create-tp.'
agent: 'edu-agent-classroom-designer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}`.
   If not found → "Primero iniciá un tema con /edu-topic" → STOP.
3. Verify `{project-root}/{topic_folder}/tp.md` exists.
   If not → "Primero creá el TP con /edu-create-tp" → STOP.
4. Read `tp_type` from `{project-root}/{topic_folder}/topic.yaml`.
   Route based on type:
   - `repo` → load and follow `{project-root}/_edu/workflows/create-autograde-repo/workflow.md`
     (Purpose: regenerar `{topic_folder}/autograde-repo/` con el template de GitHub Classroom)
   - `quiz-moodle` → load and follow `{project-root}/_edu/workflows/create-tp-quiz/workflow.md`
     (Purpose: regenerar `{topic_folder}/tp-quiz.gift` + `{topic_folder}/tp-quiz-moodle-config.md`)
   - `quiz-google` → load and follow `{project-root}/_edu/workflows/create-tp-quiz/workflow.md`
     (Purpose: regenerar `{topic_folder}/tp-quiz-forms.md` + `{topic_folder}/tp-quiz-forms-script.js`)
   - Any other value → inform "Tipo '{tp_type}' no requiere output adicional" → STOP.

