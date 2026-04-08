---
description: 'EDU: Generar instrucciones de anotación en pizarra por filmina (Drawing principle)'
tools: ['read', 'write']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Read `filminas.md` and the plan JSON for the topic.
3. For each slide of type `concepto-abstracto`, `diagrama`, or `codigo`:
   - Generate a sequence of whiteboard annotation steps (draw_text, draw_shape, draw_arrow, highlight, etc.)
   - Each step includes: action, description, duration in seconds, position hint
   - Total duration must fit within the minuta time allocated for that slide
4. Add a "📝 Desarrollo Visual" section to `guia-profesor.md` for each applicable slide.
5. Do NOT overwrite the existing guia-profesor — extend it with the new sections.
6. Validate the steps against `_edu/schemas/annotation-steps.schema.json`.
