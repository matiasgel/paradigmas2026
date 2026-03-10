---
description: 'EDU Fase 3: Validar calidad — escritura, coherencia, referencias, scope y densidad'
agent: 'agent'
tools: ['read', 'search']
---

1. Load {project-root}/_edu/config.yaml and store ALL fields as session variables
2. Load and follow the workflow at {project-root}/_edu/workflows/quality-loops/workflow.md
3. Purpose: Run quality validation. Detect existing validation reports and suggest the next pending loop:
   Loop 1a (writing errors) → Loop 2 (coherence breaks) → Loop 3 (references) → Guardrail (scope + density).
   Ask the user which loop to run, or offer to run all pending loops in sequence.
