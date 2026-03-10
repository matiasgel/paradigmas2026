# Workflow: Topic Cycle

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** course-planner (orchestrator), topic-designer, class-writer, tp-designer

---

## Overview

Ciclo completo de producción de un tema: diseño → clase → TP → calidad → testing → cierre.

## Steps

### Step 0: Initialize Topic Directory
- **Precondition:** `_edu/active-topic.yaml` must exist (written by /edu-design-topic or /edu-topic)
- **Actions:**
  1. Read `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables
  2. Read `{project-root}/{topic_folder}/topic.yaml` → store all fields (`class_duration`, `git_branch`, `status`, `artifacts` map)
  3. Use `{class_duration}` from `topic.yaml` as the duration constraint for ALL subsequent steps
  4. Resolve all artifact paths as `{project-root}/{topic_folder}/{artifact}` (e.g. `diseno.md`, `minuta.md`, `filminas.md`, `tp.md`)
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

### Step 5: Create TP
- **Agent:** tp-designer (Valeria)
- **Input:** `minuta.md`
- **Output:** `temas/NN-nombre/tp.md`
- **Constraint:** Traceable to minuta sections

### Step 5.5: Create Autograde Repo (Optional)
- **Agent:** classroom-designer (Rodrigo)
- **Prompt:** `/edu-create-autograde-repo`
- **Condition:** Solo si el tp.md existe y se desea integración con GitHub Education
- **Input:** `{topic_folder}/tp.md`
- **Output:** `{topic_folder}/autograde-repo/` (repo plantilla completo para GitHub Classroom)
- **Note:** No bloquea la continuación del ciclo — puede ejecutarse antes o después de quality loops

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

