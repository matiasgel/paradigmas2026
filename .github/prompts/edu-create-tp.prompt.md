---
description: 'EDU Fase 3: Crear TP — elige tipo (desarrollo / repo / quiz-moodle / quiz-google / mixto), genera tp.md trazable a la minuta y el output específico del tipo.'
agent: 'edu-agent-tp-designer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}`.
   If not found → "Primero iniciá un tema con /edu-design-topic" → STOP.
3. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields.
4. **Elección de tipo:** Preguntar al docente:
   > "¿Qué tipo de entrega es este TP?"
   > 1. Desarrollo — preguntas / ejercicios abiertos
   > 2. Repo — entrega como repositorio de código (GitHub Classroom)
   > 3. Quiz Moodle — múltiple opción exportable a Moodle (GIFT)
   > 4. Quiz Google — múltiple opción para Google Forms/Classroom
   > 5. Mixto — combinación (el docente especifica cuáles)
   Guardar en `tp_type` dentro de `{topic_folder}/topic.yaml`.
5. **Part A — tp.md:** Generate `{topic_folder}/tp.md` trazable a `{topic_folder}/minuta.md`.
6. **Part B — output específico según tipo:**
   - `desarrollo` → no hay output adicional. Continuar a calidad.
   - `repo` → load `{project-root}/_edu/workflows/create-autograde-repo/workflow.md`
     para generar `{topic_folder}/autograde-repo/`.
   - `quiz-moodle` → load `{project-root}/_edu/workflows/create-tp-quiz/workflow.md`
     para generar `{topic_folder}/tp-quiz.gift` + `{topic_folder}/tp-quiz-moodle-config.md`.
     **El workflow incluye validación GIFT obligatoria (Paso 2.5) antes de exportar.**
     Si la validación detecta errores críticos, corregir antes de escribir el archivo.
   - `quiz-google` → load `{project-root}/_edu/workflows/create-tp-quiz/workflow.md`
     para generar `{topic_folder}/tp-quiz-forms.md` + `{topic_folder}/tp-quiz-forms-script.js`.
   - `mixto` → ejecutar los sub-pasos de cada tipo incluido en secuencia.

