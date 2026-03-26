# Workflow: New Year

**Module:** edu
**Phase:** 4 → 1 (Transition)
**Owner Agent:** course-planner

---

## Overview

Arranca el nuevo año académico reutilizando la memoria del año anterior.

## Steps

### Step 1: Load Previous Year Memory
- **Agent:** course-planner (Elena)
- **Input:** `notas-para-{año}.md` + calibration data from `_edu-memory/`
- **Action:**
  1. Read and internalize previous year's lessons from `notas-para-{año}.md`
  2. Consultar memoria colectiva del año anterior:
     ```
     python scripts/edu_memory.py search "" --course {course_prefix}-{año_anterior} --limit 50
     ```
  3. Exportar y archivar:
     ```
     python scripts/edu_memory.py export --course {course_prefix}-{año_anterior} --format md > {course_output_folder_anterior}/memoria-colectiva.md
     ```
  4. Presentar al docente un resumen de las lecciones más relevantes (categorías `retrospective`, `pedagogy-insight`, `student-feedback`)

### Step 2: Clean Workspace
- **Action:** Archivar la carpeta del año anterior `{topics_folder}`. Incrementar `course_year` en `_edu/config.yaml` al nuevo valor (`course_output_folder` y `topics_folder` se resuelven automáticamente).
- **Preserve:** `_edu-memory/calibracion-simulador/` (NEVER reset)
- **Preserve:** `plan-minimo.md` (if same institutional plan)
- **Reset:** Session-level sidecars

### Step 3: Initialize New Course
- **Agent:** course-planner (Elena)
- **Action:** Create fresh workspace structure
- **Options:** 
  - Same course, new year (reuse most config)
  - Different course (start from Phase 1)

### Step 4: Apply Improvements
- **Agent:** course-planner (Elena)
- **Action:** Proactively suggest improvements based on previous year's retrospective

