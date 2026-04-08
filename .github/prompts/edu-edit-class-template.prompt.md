---
description: 'EDU: Editar template de clase — personaliza la estructura de minuta.md y filminas.md generadas por Roberto'
agent: 'edu-agent-class-writer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store all fields as session variables.

2. Load `{project-root}/_edu/active-topic.yaml` if exists → store `{topic_folder}` for context reference.
   (The template is global — stored in `_edu/templates/` — not topic-specific. Topic context is informational only.)

3. Check if `{project-root}/_edu/templates/class-template.md` exists:
   - **Si existe** → leer el archivo y mostrárselo al docente con el mensaje:
     "📄 Este es el template actual de clase. ¿Qué sección querés modificar?"
   - **Si NO existe** → mostrar el template por defecto (ver paso 3) y preguntar:
     "No hay template personalizado aún. ¿Usamos este template base y lo ajustamos,
     o querés definirlo desde cero?"

3. **Template base por defecto** (usar si no existe archivo):

   ```markdown
   # Template de Clase — {project_name}

   ## minuta.md

   ### Estructura obligatoria
   - **Apertura** (~10% del tiempo): pregunta disparadora o caso real
   - **Desarrollo** (~75% del tiempo): bloques temáticos del diseño, uno por sección
   - **Cierre** (~10% del tiempo): síntesis de conceptos clave
   - **Ejercicio en clase** (~5% del tiempo): actividad breve y trazable al TP

   ### Restricciones
   - Extensión proporcional a `default_class_duration` (1 carilla por cada 15 min)
   - Cada sección debe referenciar al menos un concepto del diseno.md
   - Lenguaje: {document_output_language}

   ## filminas.md

   ### Estructura obligatoria
   - **Portada**: título del tema, número de tema, fecha
   - **Agenda**: lista de bloques del desarrollo
   - **Filminas de desarrollo**: 1 filmina por concepto clave (máx. 6 bullets por filmina)
   - **Filmina de cierre**: take-aways de la clase
   - **Referencias**: fuentes académicas usadas

   ### Restricciones
   - Máximo 6 bullets por filmina
   - Sin texto corrido — solo bullets o diagramas
   - Imágenes marcadas como `[IMG: descripción]` (Diego las genera al publicar)
   ```

4. Guiar al docente interactivamente:
   - Mostrar las secciones disponibles para editar: minuta / filminas / ambas
   - Para cada sección a modificar: preguntar qué cambiar (agregar, quitar, ajustar restricciones)
   - Validar que la duración de clase siga siendo el constraint central
   - Avisar si un cambio rompe la trazabilidad con diseno.md o tp.md

5. Guardar el resultado en `{project-root}/_edu/templates/class-template.md`.
   - Crear el directorio `_edu/templates/` si no existe.
   - Si el archivo ya existía: editarlo (no reemplazar completo — sólo las secciones modificadas).

6. Confirmar: "✅ Template de clase actualizado en `_edu/templates/class-template.md`.
   Roberto usará esta estructura la próxima vez que ejecutes `/edu-create-class`."

7. **Nota para el agente:** A partir de este momento, cuando se ejecute el paso Create Class
   del topic-cycle, verificar si `{project-root}/_edu/templates/class-template.md` existe.
   Si existe, **ese archivo es el constraint de estructura** — tiene precedencia sobre la
   estructura por defecto embebida en class-writer.md.
