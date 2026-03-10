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
  1. Read `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables
  2. Read `{project-root}/{topic_folder}/topic.yaml` → store all fields (`class_duration`, `git_branch`, `status`, `artifacts` map)
  3. Use `{class_duration}` from `topic.yaml` as the duration constraint for ALL subsequent steps
  4. Resolve all artifact paths as `{project-root}/{topic_folder}/{artifact}` (e.g. `diseno.md`, `minuta.md`, `filminas.md`, `guia-estudio.md`, `tp.md`)
- **Error:** If `active-topic.yaml` is missing → STOP and instruct: "Primero iniciá un tema con /edu-design-topic"

### Step 1: Design Topic
- **Agent:** topic-designer (Marcos)
- **Input:** Topic number from plan-borrador.md
- **Output:** `temas/NN-nombre/diseno.md`
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
- **Output:** `temas/NN-nombre/minuta.md`, `temas/NN-nombre/filminas.md`
- **Constraint:** Content proportional to `default_class_duration`

### Step 4.5: Create Study Guide
- **Agent:** study-guide-writer (Sofía)
- **Input:** `minuta.md` + `filminas.md` + `diseno.md` + PDFs fuente de `{project-root}/material/` + cualquier material en `{topic_folder}/`
- **Output:** `temas/NN-nombre/guia-estudio.md`
- **Purpose:** Documento completo para estudio autónomo del alumno. Más profundo que la minuta — incluye desarrollo teórico expandido (integrando los PDFs fuente), ejemplos trabajados paso a paso, glosario y autoevaluación.
- **Structure:** Portada → Objetivos → Conceptos previos → Desarrollo teórico (con referencias a filminas y PDFs) → Ejemplos trabajados → Puntos clave → Autoevaluación → Glosario → Referencias
- **Constraint:** Scope estrictamente definido por `diseno.md`. La guía NO debe incluir contenido fuera de los tópicos del diseño aprobado.
- **PDF integration:** Sofía intenta leer los PDFs en `{project-root}/material/` para integrar contenido relevante al tema. Los fragmentos no accesibles se marcan con `<!-- PENDIENTE: integrar contenido de {archivo}.pdf -->`.
- **Gate:** Professor review after generation — same as minuta/filminas.
- **Note:** Recuperable con `/edu-create-study-guide` si se necesita regenerar de forma aislada. Exportable a PDF final con `/edu-export-pdf`.

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

- **Output base (todos los tipos):** `temas/NN-nombre/tp.md` — consignas trazables a la minuta
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
- **Output:** `{topic_folder}/tp-quiz.gift` — importable directo en Moodle
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
- **Prompt:** `/edu_publish_slides`
- **Agent:** slides-publisher (Diego), orquestado por el prompt
- **Condition:** Solo si `_edu/secrets.local.yaml` existe (APIs configuradas)
- **Input:** `temas/NN-nombre/filminas.md` (ya aprobadas y corregidas por quality loops)
- **Output:** `temas/NN-nombre/slides/publish_slides.py`, `temas/NN-nombre/slides/slide-plan.yaml`, `temas/NN-nombre/slides/slides-url.txt`
- **Gate:** El docente aprueba el plan de imágenes filmina por filmina antes de generar
- **Note:** Si `_edu/slides-config.yaml` no existe, Diego invoca a Vera primero automáticamente

