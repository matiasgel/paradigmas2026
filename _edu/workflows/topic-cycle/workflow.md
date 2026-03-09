# Workflow: Topic Cycle

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** course-planner (orchestrator), topic-designer, class-writer, tp-designer

---

## Overview

Ciclo completo de producción de un tema: diseño → clase → TP → calidad → testing → cierre.

## Steps

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

