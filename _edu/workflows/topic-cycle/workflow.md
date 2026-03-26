# Workflow: Topic Cycle

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** course-planner (orchestrator), topic-designer, class-writer, study-guide-writer, tp-designer

---

## Overview

Ciclo completo de producción de un tema: diseño → clase → **guía de estudio** → TP → calidad → testing → cierre.

## Steps

### Step 0: Initialize Topic Directory
- **Precondition:** `_edu/active-topic.yaml` must exist (written by /edu-design-topic or /edu-topic)
- **Actions:**
  1. Read `{project-root}/_edu/config.yaml` → store `{topics_folder}`, `{course_id}` como variables de sesión
  2. Read `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables
     - **⚠️ VALIDACIÓN DE RUTA:** `topic_folder` DEBE ser ruta bajo `{topics_folder}` (ej: `salida/cursadas/leng-2026/temas/01-intro`). Si es una ruta bare como `temas/NN-nombre`, corregir automáticamente a `{topics_folder}/NN-nombre` y actualizar `active-topic.yaml`.
  3. Read `{project-root}/{topic_folder}/topic.yaml` → store all fields (`class_duration`, `git_branch`, `status`, `artifacts` map)
  4. Use `{class_duration}` from `topic.yaml` as the duration constraint for ALL subsequent steps
  5. Resolve all artifact paths as `{project-root}/{topic_folder}/{artifact}` (e.g. `diseno.md`, `minuta.md`, `filminas.md`, `guia-estudio.md`, `tp.md`)
  6. **Consultar memoria colectiva:** ejecutar `python scripts/edu_memory.py search "{topic_name}" --course {course_id}` y también `python scripts/edu_memory.py list --course {course_id} --topic {topic_number} --unresolved`. Los resultados se pasan como contexto a todos los agentes del ciclo (errores previos a evitar, correcciones ya aplicadas, insights pedagógicos del tema).
- **Crear si falta:** Si `active-topic.yaml` no existe Y se dispone de número/nombre del tema → CREAR con `topic_folder: {topics_folder}/NN-nombre` y continuar.
- **Error:** If `active-topic.yaml` is missing AND no topic info available → STOP and instruct: "Primero iniciá un tema con /edu-design-topic"

### Step 0.5: Ingest Reference PDFs
- **Precondition:** `{project-root}/material/{topic_number}-{topic_name}/` debe existir (subcarpeta del tema activo)
- **Material folder:** `{material_folder}` = `{project-root}/material/{topic_number}-{topic_name}/`  ← almacenar como variable de sesión
- **Actions:**
  1. Construir `{material_folder}` = `{project-root}/material/{topic_number}-{topic_name}/`
  2. Si la carpeta no existe → avisarle al docente y continuar sin material de referencia (no es bloqueante)
  3. Listar todos los archivos `.pdf` en `{material_folder}`
  4. Para cada PDF, verificar si ya existe `{material_folder}/txt/{nombre}.txt`
  5. Si **todos** los PDFs tienen su `.txt` → continuar al Step 1
  6. Si **algún PDF falta su `.txt`** → indicar al docente que ejecute:
     ```
     python scripts/pdf-to-text.py material/{topic_number}-{topic_name}/
     ```
     y esperar confirmación antes de continuar
  7. Una vez confirmada la conversión, almacenar la lista de paths `.txt` como variable de sesión `{material_texts}` (e.g. `material/01-intro/txt/ref1.txt`)
- **Script:** `{project-root}/scripts/pdf-to-text.py` — requiere `pip install pdfminer.six`
- **Idempotente:** El script omite archivos ya convertidos; es seguro ejecutarlo múltiples veces
- **Error — script faltante:** Si `scripts/pdf-to-text.py` no existe, el agente lo crea copiando el template canónico del repo antes de indicar su ejecución
- **Note:** Los pasos subsiguientes (especialmente Step 4.5) leen desde `{material_folder}/txt/` — NO directamente de los `.pdf`

### Step 1: Design Topic
- **Agent:** topic-designer (Marcos)
- **Input:** Topic number from plan-borrador.md + textos en `{material_texts}` como contexto de referencia
- **Output:** `{topics_folder}/NN-nombre/diseno.md`
- **Gate:** Professor approval required

### Step 2: (Optional) Adjust Design
- **Agent:** topic-designer (Marcos)
- **Condition:** Only before approval
- **Output:** Updated `diseno.md`

### Step 3: Approve Design
- **Agent:** course-planner (Elena)
- **Gate:** Explicit professor confirmation
- **Output:** `diseno.md` marked as approved

### Step 4: Create Class
- **Agent:** class-writer (Roberto)
- **Input:** Approved `diseno.md`
- **Output:** `{topic_folder}/minuta.md`, `{topic_folder}/filminas.md`
- **Constraint:** Content proportional to `default_class_duration`

### Step 4.5: Create Study Guide
- **Agent:** study-guide-writer (Sofía)
- **Input:** `minuta.md` + `filminas.md` + `diseno.md` + PDFs fuente de `{project-root}/material/` + cualquier material en `{topic_folder}/`
- **Output:** `{topic_folder}/guia-estudio.md`
- **Purpose:** Documento completo para estudio autónomo del alumno. Más profundo que la minuta — incluye desarrollo teórico expandido (integrando los PDFs fuente), ejemplos trabajados paso a paso, glosario y autoevaluación.
- **Structure:** Portada → Objetivos → Conceptos previos → Desarrollo teórico (con referencias a filminas y PDFs) → Ejemplos trabajados → Puntos clave → Autoevaluación → Glosario → Referencias
- **Constraint:** Scope estrictamente definido por `diseno.md`. La guía NO debe incluir contenido fuera de los tópicos del diseño aprobado.
- **PDF integration:** Sofía lee los textos extraídos en `{material_folder}/txt/` (generados por `scripts/pdf-to-text.py` en el Step 0.5). Si esa carpeta no existe o algún `.txt` falta, NO continuar: indicar al docente que ejecute `python scripts/pdf-to-text.py material/{topic_number}-{topic_name}/` primero. Los fragmentos que aún resulten vacíos o ilegibles se marcan con `<!-- PENDIENTE: revisar manualmente {archivo}.txt -->`.
- **Gate:** Professor review after generation — same as minuta/filminas.
- **Note:** Recuperable con `/edu-create-study-guide` si se necesita regenerar de forma aislada. Exportable a PDF final con `/edu-export-pdf`.

### Step 4.6: Create Teacher Guide (Guía del Profesor)
- **Agent:** class-writer (Roberto)
- **Input:** `diseno.md`, `minuta.md`, `filminas.md`, `guia-estudio.md`, y cualquier material de `{project-root}/material/{topic_number}-{topic_name}/` (PDFs + txt extraídos)
- **Output:** `{topic_folder}/guiaprofesor.md`
- **Purpose:** Documento autocontenido para el docente — el único archivo que necesita abrir para repasar el tema. Contiene:
  - Plan de clase por bloques de tiempo (derivado de la minuta per-filmina)
  - Índice de artefactos (minuta, filminas, guía de estudio, TP) con rutas del repo
  - Extractos clave de los PDFs fuente (citas textuales, tablas, ejemplos relevantes)
  - Sugerencias de preguntas para clase, debates y evaluaciones
  - Resumen ejecutivo: qué enseñar, cómo enseñarlo y dónde está cada recurso
- **Constraint:** Autocontenido — el docente repasa el tema sin abrir otros archivos (aunque todos se referencian con rutas locales).
- **Note:** Recuperable con `/edu-create-teacher-guide`. Regenerar cuando cambie minuta.md o filminas.md.

### Step 5: Create TP
- **Agent:** tp-designer (Valeria)
- **Input:** `minuta.md` + `guia-estudio.md` (para que Valeria pueda verificar que las consignas del TP no dupliquen la autoevaluación de la guía)
- **Gate — Tipo de TP:** Antes de generar, preguntar al docente:
  > "¿Qué tipo de entrega es este TP?"
  > 1. **Desarrollo** — preguntas abiertas / ejercicios a resolver (tp.md clásico)
  > 2. **Repo** — entrega como repositorio de código
  > 3. **Quiz Moodle** — múltiple opción exportable a Moodle (formato GIFT)
  > 4. **Quiz Google** — múltiple opción para Google Forms / Google Classroom
  > 5. **Mixto** — combinación de tipos (el docente especifica cuáles)

  Guardar el tipo elegido en `{topic_folder}/topic.yaml` bajo la clave `tp_type`.

- **Output base (todos los tipos):** `{topic_folder}/tp.md` — consignas trazables a la minuta
- **Constraint:** tp.md trazable a secciones de minuta. Scope creep = eliminarlo.

### Step 5.5: TP Type-Specific Output (Opcional por tipo)

Según `tp_type` guardado en Step 5, ejecutar el sub-paso correspondiente:

#### Tipo: `repo`
- **Agent:** classroom-designer (Rodrigo)
- **Output:** `{topic_folder}/autograde-repo/` — repo plantilla con GitHub Actions autograding
- **Workflow:** `_edu/workflows/create-autograde-repo/workflow.md`
- **Note:** Si el docente eligió `repo` en Step 5, este sub-paso se ejecuta directamente. Recuperable con `/edu-create-autograde-repo` si se necesita regenerar.

#### Tipo: `quiz-moodle`
- **Agent:** tp-designer (Valeria)
- **Output:** `{topic_folder}/tp-quiz.gift` + `{topic_folder}/tp-quiz-moodle-config.md`
- **Workflow:** `_edu/workflows/create-tp-quiz/workflow.md`

#### Tipo: `quiz-google`
- **Agent:** tp-designer (Valeria)
- **Output:** `{topic_folder}/tp-quiz-forms.md` + `{topic_folder}/tp-quiz-forms-script.js`
- **Workflow:** `_edu/workflows/create-tp-quiz/workflow.md`

#### Tipo: `desarrollo` o no requiere output adicional
- Continuar directamente al Step 6.

#### Tipo: `mixto`
- Ejecutar los sub-pasos correspondientes a cada tipo incluido, en secuencia.

### Step 6: Quality Loops
- **Workflow:** quality-loops/workflow.md
- **Sequential:** Loop 1 (writing) → Loop 2 (coherence) → Loop 3 (references) → Guardrail

### Step 7: Pedagogical Testing
- **Workflow:** pedagogical-testing/workflow.md
- **Output:** `score-pedagogico.md`, `faq-anticipado.md`

### Step 8: Close Topic
- **Agent:** course-planner (Elena)
- **Gate:** All loops resolved
- **Action:** Git commit + merge, update coverage matrix

### Step 9: Push Both Branches
- **Action:** `git push origin main` y `git push origin production`
- **Condition:** Run always after Step 8

### Step 9.5: Publish Slides (Optional)
- **Prompt:** `/edu-publish-slides`
- **Condition:** Solo si `_edu/secrets.local.yaml`, `_edu/slides-config.yaml` y `_edu/schemas/schema-registry.json` existen
- **Input:** `{topic_folder}/filminas.md` (aprobadas y corregidas)
- **Output:**
  - `{topic_folder}/slides/plan-filminas-{tema}.json` — plan JSON v3 validado contra schema
  - `{topic_folder}/slides/assets/` — imágenes generadas (Gemini + matplotlib)
  - `{topic_folder}/slides/slides-url.txt` — URL de la presentación publicada

**Flujo v3 (schema-driven):**

**Paso 1 — Generar plan DRAFT:**
```bash
python scripts/parse_filminas.py {topic_folder}
```
Produce `slides/plan-draft-{tema}.json` con `type: pending` para slides sin `@tipo:`.

**Paso 2 — El agente (invocado por `/edu-publish-slides`) completa el plan:**
- Lee `_edu/schemas/schema-registry.json` → `type_layout_map`, `canonical_types`, `image_prompt_rules`
- Asigna un `type` explícito del enum `canonical_types` a cada slide con `type: pending`
- COPIA `layout` = `type_layout_map[type].layout` (EXACTO, determinista)
- COPIA `image.layer` = `type_layout_map[type].image_layer`
- Si `image.layer != "none"` → escribe `image.prompt` con **lenguaje visual puro**
  (ver `_edu/templates/prompt-imagen-guide.md` — REGLA ANTI-BUG 3)
- Elimina la clave `_draft_instructions`
- Renombra el archivo a `slides/plan-filminas-{tema}.json`
- Incluye `$schema_version: "plan-filminas/v3"` y `meta` con rutas de trazabilidad

**Paso 3 — Validación con loop de reparación (máximo 3 intentos):**
```bash
python scripts/repair_plan.py {topic_folder} --attempt 1 --max-attempts 3
```
- Exit `0` → plan válido → continuar al Paso 4
- Exit `1` → errores encontrados → agente corrige **solo** los campos reportados → `--attempt 2`
- Exit `2` → 3 intentos fallidos → STOP, revisión humana requerida

**Paso 4 — Publicar:**
```bash
python scripts/slides_pipeline.py {topic_folder}
```
El script carga el plan JSON, valida contra JSON Schema, genera assets y publica en Google Slides.

**Corrección de imágenes sin tocar el script:**
1. Editar `image.prompt` en el plan JSON con lenguaje visual puro
2. Poner `image.drive_id: null` para forzar regeneración
3. Eliminar `slides/assets/F-XX-*.png` si existe localmente
4. `python scripts/slides_pipeline.py {topic_folder} --assets-only`
5. `python scripts/slides_pipeline.py {topic_folder} --publish-only`
6. Verificar: `python scripts/capture_thumbnails.py <id> {topic_folder}/slides/thumbnails/`

- **Note:** Si `_edu/slides-config.yaml` no existe, activar `/edu-slides-designer` primero (una sola vez por cursada)

