---
description: 'EDU: Buscar en la memoria colectiva — consulta errores pasados, correcciones, insights y patrones cross-curso'
agent: 'agent'
tools: ['read', 'execute', 'search']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Ask the user:
   > "¿Qué querés buscar en la memoria colectiva? Podés escribir palabras clave o una pregunta."
   >
   > Opciones de filtro (opcionales):
   > - **Materia:** por defecto {course_id}, o `todas` para cross-curso
   > - **Categoría:** `agent-error`, `agent-correction`, `quality-finding`, `pedagogy-insight`, `student-feedback`, `cross-topic`, `retrospective`, `tool-issue`
   > - **Tema:** número de tema (ej: `01`)
3. Construct the command:
   ```
   python scripts/edu_memory.py search "{user_query}" --course {course_id}
   ```
   Add `--all` if the user asked for cross-curso. Add `--category` and `--topic` if specified.
4. Execute the command and show the results formatted.
5. If the user wants to add a new entry → ask for category, summary and detail, then execute:
   ```
   python scripts/edu_memory.py add --course {course_id} --category {cat} --summary "{summary}" --detail "{detail}"
   ```
6. If the user wants to mark an entry as resolved → execute:
   ```
   python scripts/edu_memory.py resolve {id}
   ```
