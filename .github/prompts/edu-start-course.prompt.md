---
description: 'EDU Fase 1: Iniciar curso — configura materia, carga programa oficial y congela plan mínimo (flujo completo de Fase 1)'
agent: 'edu-agent-course-planner'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load {project-root}/_edu/config.yaml and store ALL fields as session variables
2. Load and follow the workflow at {project-root}/_edu/workflows/load-official-plan/workflow.md
3. Purpose: Complete Phase 1 in sequence:
   Step 1 — Configure course basics (name, institution, professor profile, class duration, LMS, language).
   Step 2 — Load the institutional PDF program and generate plan-minimo.md.
   Step 3 — Confirm plan-minimo.md as the immutable course contract. Requires explicit professor approval.


