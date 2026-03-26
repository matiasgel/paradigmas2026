---
description: 'EDU Fase 3: Crear guía del profesor — genera guiaprofesor.md con todo el contexto, recursos y extractos clave para repaso docente.'
agent: 'edu-agent-class-writer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
4. Verify prerequisites:
   - `{project-root}/{topic_folder}/diseno.md` must exist and contain "APROBADO" → If not: "El diseño del tema no está aprobado. Ejecutá /edu-approve-design primero." → STOP.
   - `{project-root}/{topic_folder}/minuta.md` must exist → If not: "No existe la minuta. Ejecutá /edu-create-class primero." → STOP.
   - `{project-root}/{topic_folder}/filminas.md` must exist → If not: "No existen las filminas. Ejecutá /edu-create-class primero." → STOP.
   - `{project-root}/{topic_folder}/guia-estudio.md` should exist → if not, suggest: "Ejecutá /edu-create-study-guide primero para generar la guía de alumno." (no block).
5. Discover source materials:
   - List PDFs under `{project-root}/material/{topic_number}-{topic_name}/` and any `*.pdf` under `{topic_folder}`.
   - For each PDF, if `{...}/txt/{name}.txt` exists, load it and include relevant excerpts in the teacher guide.
6. Generate `{topic_folder}/guiaprofesor.md` with the following sections:
   - Portada (tema, docente, fecha)
   - Objetivos y competencias
   - Plan de clase (bloques de tiempo + actividades + recursos)
   - Resumen de minuta + links a filminas
   - Extractos clave de los PDFs fuente (incluye citas textuales o tablas relevantes)
   - Sugerencias de preguntas para clase, debates y actividades prácticas
   - Referencias y dónde encontrar cada recurso en el repo
7. Save the output and instruct the user: "Revisá `guiaprofesor.md`, hacé commit y continuá con la fase de calidad / testing."