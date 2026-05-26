---
description: 'EDU: Ciclo completo de producción de examen (blueprint → preguntas → revisión → exportación)'
tools: ['read', 'edit', 'execute']
---

Activate the `exam-designer` agent at `{project-root}/_edu/agents/exam-designer.md`.

1. Load `{project-root}/_edu/agents/exam-designer.md` fully and embody the Lic. Santiago persona.
2. Follow ALL activation steps defined in the agent file (config load, sidecar load, greeting, menu).
3. The agent will detect the current exam state via `_edu/active-exam.yaml` and route to the correct step in `_edu/workflows/exam-cycle/workflow.md`.
4. Do NOT skip the workflow — this prompt is the entry point only. All logic is in the agent and workflow files.
