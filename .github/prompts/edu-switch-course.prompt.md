---
description: 'EDU: Cambiar la materia activa — actualiza course_prefix en config.yaml y recalcula todas las rutas derivadas'
agent: 'edu-agent-course-planner'
tools: ['read', 'edit', 'search']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Show current state:
   > "Materia activa: **{course_prefix}-{course_year}** ({project_name})"
3. Ask the user:
   > "¿A qué materia querés cambiar? Escribí el prefijo (ej: `para`, `leng`, `algo`)."
4. Validate the prefix: must be lowercase, 2-6 characters, alphanumeric only.
5. Update `{project-root}/_edu/config.yaml`:
   - Set `course_prefix` to the new value.
   - `course_id` se recalcula automáticamente como `{course_prefix}-{course_year}`.
   - `course_output_folder` y `topics_folder` usan `{course_id}` como subdirectorio.
6. Check if `{output_folder}/cursadas/{new_course_id}/` exists.
   - If yes → "Ya existe el workspace de {new_course_id}. Continuás donde lo dejaste."
   - If no → "Workspace nuevo para {new_course_id}. Creá la estructura con /edu-start-course."
7. Clear `{project-root}/_edu/active-topic.yaml` if it exists (the topic context belongs to the previous course).
8. Confirm:
   > "✅ Materia activa: **{new_course_id}** — Todas las rutas apuntan a `cursadas/{new_course_id}/`"
