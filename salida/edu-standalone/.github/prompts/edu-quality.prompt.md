---
description: 'EDU Fase 3: Calidad — valida y/o corrige escritura, coherencia, referencias, scope y densidad con commits Git'
agent: 'edu-agent-writing-validator'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Load and follow the workflow at `{project-root}/_edu/workflows/quality-loops/workflow.md`.
5. Purpose: Unified quality command. All reports and fixes apply to files in `{topic_folder}/`.
   On startup, detect the current state automatically:
   - If NO validation reports exist → Validate mode: detect pending loops and run in sequence
     (Loop 1a: writing errors → Loop 2: coherence → Loop 3: references → Guardrail: scope + density)
   - If reports exist WITHOUT applied fixes → Fix mode: apply selectively or auto-fix
     (Writing: auto or selective; Coherence: auto; Reference: specific ID or suggest alternative; Guardrail: auto)
   - If user explicitly requests a mode (“validar” / “corregir”) → override detection
   Each fix generates a reversible Git commit on branch `{git_branch}`.

