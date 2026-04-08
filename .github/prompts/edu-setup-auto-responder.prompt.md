---
description: 'EDU: Configurar auto-responder de Git para repos de alumnos'
tools: ['read', 'write']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Read `{project-root}/_edu/templates/student-helper-action.yml` — this is the GitHub Action template.
3. Read `{project-root}/_edu/knowledge/git-help-students.md` — this is the knowledge base of common Git errors.
4. Copy the action YAML to the student's `autograde-repo/.github/workflows/student-helper.yml` inside the topic folder.
5. Inform the user that the auto-responder detects 7 common Git errors and will comment on PRs/pushes automatically.
6. Remind: the template is editable — the user can customize detection patterns.
