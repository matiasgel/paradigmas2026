---
description: 'EDU Fase 3: Corregir calidad — escritura, coherencia, referencias y guardrail con commits Git'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute']
---

1. Load {project-root}/_edu/config.yaml and store ALL fields as session variables
2. Load and follow the workflow at {project-root}/_edu/workflows/quality-loops/workflow.md
3. Purpose: Apply quality fixes. Check for existing validation reports and ask which fixes to apply:
   - Writing fixes (Loop 1b — auto-fix or selective apply)
   - Coherence fixes (Loop 2 — auto-fix)
   - Reference fix (specific reference ID) or suggest academic alternative
   - Guardrail fixes (scope + density — auto-fix)
   Each fix generates a reversible Git commit.
