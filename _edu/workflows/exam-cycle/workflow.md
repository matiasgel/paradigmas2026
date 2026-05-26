# Workflow: Exam Cycle

**Module:** edu
**Phase:** anytime (evaluaciones)
**Owner Agent:** exam-designer (Santiago)

---

## Overview

Ciclo completo de producción de un examen: selección de tipo → blueprint → generación de preguntas (topic-by-topic) → revisión docente → exportación.

**Diseño anti-saturación de contexto:** Las preguntas se generan un tema por vez. Cada bloque se guarda a disco antes de pasar al siguiente. El agente nunca carga simultáneamente las preguntas de todos los temas.

---

## Step 0: Detect State and Route

- **Precondition:** `_edu/config.yaml` already loaded by activation (step 2 of agent)
- **Actions:**
  1. Read `{project-root}/_edu/active-exam.yaml` — store all fields as `{active_exam}`
  2. Read `{memory_folder}/exam-designer-sidecar/exams-created.yaml` — store as `{exams_created}`
  3. Determine routing based on `{active_exam.status}`:
     - `null` / file doesn't exist → go to **Step 1** (new exam)
     - `started` → go to **Step 1** (resume exam type selection)
     - `blueprint-pending` → go to **Step 2** (run blueprint)
     - `blueprint-approved` → go to **Step 3** (generate questions)
     - `questions-generated` → go to **Step 4** (assemble exam)
     - `assembled` → go to **Step 5** (docente review)
     - `approved` → go to **Step 6** (export)
     - `exported` → show summary + ask if starting a new exam or exit
  4. Announce routing: "📌 Retomando desde: [Step N — Nombre]" or "✅ Iniciando nuevo examen"

---

## Step 1: Select Exam Type and Topics

- **Agent:** exam-designer (Santiago — inline, no workflow delegation)
- **Actions:**
  1. Ask docente to choose exam type:
     ```
     ¿Qué tipo de examen?
     1. Parcial 1
     2. Parcial 2
     3. Parcial 3 (si corresponde)
     4. Final Integrador
     ```
  2. Based on type, auto-suggest topics from `{course_output_folder}/plan-borrador.md`:
     - **Parcial 1:** primeros ~33% de temas del plan
     - **Parcial 2:** siguientes ~33% de temas del plan
     - **Parcial 3:** siguientes ~33% de temas del plan
     - **Final:** todos los temas del plan (ajustar peso por temas ya evaluados)
  3. Show suggested topic list. Allow docente to add/remove topics.
  4. Ask: total de puntos (default: 100), duración en minutos (default: 120), perfil Bloom:
     - `default` — distribución estándar (20% Recordar, 30% Comprender, 25% Aplicar, 15% Analizar, 7% Evaluar, 3% Crear)
     - `practical` — más peso en Aplicar y Analizar
     - `research` — más peso en Evaluar y Crear
     - `introductory` — más peso en Recordar y Comprender
  5. Write `{project-root}/_edu/active-exam.yaml`:
     ```yaml
     exam_type: "parcial-1"      # parcial-1 | parcial-2 | parcial-3 | final
     exam_number: 1
     topics: ["01-intro", "02-tipos", "03-memoria"]
     points: 100
     duration_minutes: 120
     bloom_profile: "default"
     status: "started"
     output_folder: "{course_output_folder}/evaluaciones/parcial-1"
     created_at: "YYYY-MM-DD"
     ```
  6. Create output directory: `{course_output_folder}/evaluaciones/{exam_type}/`
  7. Update status to `blueprint-pending` in `active-exam.yaml`
  8. Announce: "✅ Examen configurado. Procediendo al blueprint..."
  9. Fall through to **Step 2**

---

## Step 2: Generate Blueprint

- **Agent:** exam-designer (Santiago — runs script, reviews result)
- **Precondition:** `active-exam.status == "blueprint-pending"`
- **Actions:**
  1. Run blueprint script:
     ```bash
     cd {project-root} && python scripts/generate_exam_blueprint.py \
       --course {course_id} \
       --topics "{topics_comma_separated}" \
       --points {points} \
       --time {duration_minutes} \
       --bloom-profile {bloom_profile}
     ```
  2. Script genera: `{course_output_folder}/evaluaciones/{exam_type}/blueprint.json` y `blueprint.md`
  3. Display the blueprint matrix to docente (tabla: tema × nivel Bloom × puntos × N preguntas)
  4. Highlight any topic with weight > 30% or < 5% and suggest adjustment
  5. **Gate — Aprobación del blueprint:**
     > "¿Aprobás este blueprint, o querés ajustar la distribución?"
     > - **Aprobado** → update status to `blueprint-approved`, save `blueprint_path` in `active-exam.yaml`, fall through to Step 3
     > - **Ajustar** → ask what to change, modify `active-exam.yaml` parameters, re-run script from 2.1
     > - **Cancelar** → set status back to `started`, exit workflow

---

## Step 3: Generate Questions (Topic-by-Topic — Anti Context Overflow)

- **Agent:** exam-designer (Santiago — orchestrates, delegates generation inline)
- **Precondition:** `active-exam.status == "blueprint-approved"`
- **⚠️ CONTEXT MANAGEMENT:** Procesar UN TEMA POR VEZ. Cargar solo el contexto de ese tema. Guardar a disco antes de pasar al siguiente. No acumular preguntas de múltiples temas en contexto.

- **Initialize:**
  1. Read approved `blueprint.md` → extract: per-topic question count and required Bloom levels
  2. Read `{memory_folder}/exam-designer-sidecar/questions-registry.yaml` (create if missing: `{questions: []}`)
  3. Store `{topics_remaining}` = all topics from blueprint
  4. Store `{questions_output_files}` = [] (list of generated files)

- **Per-Topic Loop** (repeat for each topic in `{topics_remaining}`):

  **3.a — Load Topic Context (ONE topic only):**
  - Set `{current_topic}` = next topic from `{topics_remaining}`
  - Load ONLY `{topics_folder}/{current_topic}/minuta.md` (primary source)
  - Load ONLY `{topics_folder}/{current_topic}/diseno.md` (for scope boundaries)
  - Extract from blueprint: `{required_questions}` count and `{bloom_distribution}` for this topic
  - Extract from questions-registry: previously used question texts/hashes for this topic (to avoid repetition)
  
  **3.b — Generate Questions for This Topic:**
  - Generate exactly `{required_questions}` questions for `{current_topic}`
  - Distribute across required Bloom levels per blueprint
  - Each question must have:
    - `id`: `q-{topic_id}-{bloom_level}-{NNN}` (e.g. `q-01-intro-comprender-001`)
    - `bloom_level`: recordar | comprender | aplicar | analizar | evaluar | crear
    - `type`: opcion_multiple | verdadero_falso | desarrollo_corto | problema
    - `text`: enunciado completo
    - `answer`: respuesta esperada o key (para opción múltiple: opciones a/b/c/d + correcta)
    - `points`: asignados según blueprint
    - `topic`: `{current_topic}`
    - `source_ref`: sección de minuta.md de donde proviene el contenido
  - **ANTI-REPETICIÓN:** Si alguna pregunta tiene texto similar a las del registro previo → descartar y generar alternativa
  
  **3.c — Save Topic Questions to Disk (IMMEDIATELY):**
  - Write to: `{course_output_folder}/evaluaciones/{exam_type}/preguntas-{current_topic}.md`
  - Format: YAML frontmatter con metadata + preguntas en markdown
  - Append to `{questions_output_files}` the file path
  
  **3.d — Update Questions Registry:**
  - For each generated question, append to `{memory_folder}/exam-designer-sidecar/questions-registry.yaml`:
    ```yaml
    - id: "q-01-intro-comprender-001"
      topic: "01-intro"
      bloom: "comprender"
      text_preview: "Primeras 60 caracteres del texto..."
      exam_type: "parcial-1"
      course_id: "{course_id}"
      created_at: "YYYY-MM-DD"
    ```
  
  **3.e — Release Topic Context:**
  - Announce: "✅ Tema {current_topic}: {N} preguntas generadas y guardadas."
  - **Release** minuta.md and diseno.md from active context
  - Update `{active_exam}` in `active-exam.yaml` with `questions_progress: {current_topic}: done`
  - Move to next topic (back to 3.a)

- **After all topics processed:**
  - Update `active-exam.status = "questions-generated"` in `active-exam.yaml`
  - Store list of `questions_files` in `active-exam.yaml`
  - Announce: "✅ Preguntas generadas para {N} temas. Total: {total_questions} preguntas."
  - Fall through to **Step 4**

---

## Step 4: Assemble Full Exam

- **Agent:** exam-designer (Santiago)
- **Precondition:** `active-exam.status == "questions-generated"`
- **⚠️ CONTEXT MANAGEMENT:** Leer archivos de preguntas de a uno, extraer solo metadata, luego construir el índice. No cargar todos los contenidos en memoria simultáneamente.
- **Actions:**
  1. For each file in `questions_files`:
     - Read file metadata (frontmatter) only → extract: topic, N questions, bloom distribution
     - Accumulate in summary table (NOT full question text)
  2. Generate summary table:
     ```
     | Tema | Preguntas | Recordar | Comprender | Aplicar | Analizar | Evaluar | Crear | Puntos |
     ```
  3. Generate `{course_output_folder}/evaluaciones/{exam_type}/examen-indice.md`:
     - Tabla resumen + lista de archivos de preguntas
     - Total: N preguntas, X puntos, Y minutos
  4. Update `active-exam.status = "assembled"` in `active-exam.yaml`
  5. Fall through to **Step 5**

---

## Step 5: Docente Review Gate

- **Agent:** exam-designer (Santiago)
- **Precondition:** `active-exam.status == "assembled"`
- **Actions:**
  1. Show `examen-indice.md` summary table
  2. Show per-topic question counts vs. blueprint targets
  3. Ask docente:
     ```
     ¿Cómo querés proceder?
     1. ✅ Aprobar examen → exportar
     2. 🔁 Ver preguntas de un tema específico → [ingresar número/nombre del tema]
     3. 🔁 Regenerar preguntas de un tema → vuelve a Step 3 solo para ese tema
     4. 📐 Ajustar blueprint y regenerar todo → vuelve a Step 2
     5. ❌ Cancelar
     ```
  4. If option 2: Read and display ONLY that topic's preguntas-{topic}.md (not others)
  5. If option 3: Set `{topics_remaining}` = [selected_topic], re-execute Step 3 loop for that topic only
  6. If option 4: Reset status to `blueprint-pending`, update `active-exam.yaml`, go to Step 2
  7. If option 1: Update `active-exam.status = "approved"` in `active-exam.yaml`, fall through to **Step 6**

---

## Step 6: Export

- **Agent:** exam-designer (Santiago)
- **Precondition:** `active-exam.status == "approved"`
- **Actions:**
  1. Ask export format(s):
     ```
     ¿En qué formato(s) exportar? (Podés elegir más de uno)
     1. GIFT — Banco de preguntas Moodle (.gift)
     2. Google Forms — Estructura + Apps Script
     3. PDF — Documento de examen (vía pandoc)
     4. Markdown — Examen completo en un solo .md
     5. Todos los anteriores
     ```
  
  2. **For GIFT:**
     - Read preguntas files → convert to GIFT format
     - Validate per `{project-root}/_edu/tasks/gift-validator.md` (if exists)
     - Rules: UTF-8 sin BOM, `::id::` titles, blank line between questions, escape reserved chars
     - Write: `{course_output_folder}/evaluaciones/{exam_type}/examen.gift`
     - Generate: `examen-moodle-config.md` (instrucciones de configuración: tiempo, intentos, navegación, review options)
  
  3. **For Google Forms:**
     - Write: `examen-forms.md` (estructura del formulario)
     - Write: `examen-forms-script.js` (Apps Script para creación automática)
     - Note al docente: Google Forms no tiene límite de tiempo nativo — documentar en el script
  
  4. **For PDF:**
     - Generate `examen-completo.md` (examen en un único markdown con portada, instrucciones, preguntas)
     - Run: `pandoc {exam_folder}/examen-completo.md -o examen.pdf --pdf-engine=xelatex` (si pandoc disponible)
     - Si pandoc no disponible: avisar al docente e instrucciones de instalación
  
  5. **For Markdown:**
     - Assemble all preguntas files into `examen-completo.md`
     - Includes: portada institucional, instrucciones generales, sección por tema, hoja de respuestas

  6. **Update Sidecar:**
     - Append to `{memory_folder}/exam-designer-sidecar/exams-created.yaml`:
       ```yaml
       - exam_type: "{exam_type}"
         exam_number: {exam_number}
         course_id: "{course_id}"
         topics: {topics}
         total_questions: {total_questions}
         total_points: {points}
         duration_minutes: {duration_minutes}
         bloom_profile: "{bloom_profile}"
         status: "exported"
         exported_at: "YYYY-MM-DD"
         files:
           blueprint: "evaluaciones/{exam_type}/blueprint.md"
           gift: "evaluaciones/{exam_type}/examen.gift"        # si se exportó
           forms: "evaluaciones/{exam_type}/examen-forms.md"  # si se exportó
           pdf: "evaluaciones/{exam_type}/examen.pdf"         # si se exportó
           markdown: "evaluaciones/{exam_type}/examen-completo.md"
       ```
     - Update `active-exam.status = "exported"` in `active-exam.yaml`
  
  7. **Final summary:**
     ```
     ✅ Examen exportado exitosamente.
     📁 Carpeta: evaluaciones/{exam_type}/
     📊 {total_questions} preguntas | {points} pts | {duration_minutes} min
     🎯 Distribución Bloom: [tabla compacta]
     📄 Archivos: [lista de archivos generados]
     ```

---

## Artifacts Summary

| Archivo | Descripción |
|---------|-------------|
| `active-exam.yaml` | Estado activo del examen en producción (en `_edu/`) |
| `evaluaciones/{type}/blueprint.json` | Blueprint machine-readable |
| `evaluaciones/{type}/blueprint.md` | Blueprint human-readable con tabla Bloom |
| `evaluaciones/{type}/preguntas-{topic}.md` | Preguntas por tema (uno por archivo) |
| `evaluaciones/{type}/examen-indice.md` | Índice y tabla resumen |
| `evaluaciones/{type}/examen-completo.md` | Examen ensamblado (Markdown) |
| `evaluaciones/{type}/examen.gift` | Banco de preguntas Moodle |
| `evaluaciones/{type}/examen-moodle-config.md` | Guía de configuración actividad Quiz |
| `evaluaciones/{type}/examen-forms.md` | Estructura Google Forms |
| `evaluaciones/{type}/examen-forms-script.js` | Apps Script para Google Forms |
| `evaluaciones/{type}/examen.pdf` | PDF para impresión/distribución |
| `_edu-memory/exam-designer-sidecar/exams-created.yaml` | Registro de todos los exámenes de la cursada |
| `_edu-memory/exam-designer-sidecar/questions-registry.yaml` | Registro de preguntas para prevenir repetición cross-exam |
