---
description: 'EDU: Crear proyecto PBL multi-clase con milestones, rúbricas y medidas anti-delegación'
tools: ['read', 'write']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Read `plan-minimo.md` to identify topics for the PBL project.
3. Propose 2-3 driving questions and WAIT for teacher approval.
4. Generate the PBL project following `_edu/workflows/create-pbl/workflow.md`:
   - 3+ milestones with deliverables and weights
   - Rubric criteria per milestone using `_edu/templates/pbl-rubric-template.md`
   - ≥2 anti-delegation measures
5. Validate output against `_edu/schemas/pbl-project.schema.json`.
6. Save to `{course_output_folder}/pbl/pbl-{name}.json` + `.md`.
