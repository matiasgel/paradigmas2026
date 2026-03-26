# Workflow: Close Course

**Module:** edu
**Phase:** 4 — Cierre
**Owner Agent:** course-planner

---

## Overview

Cierre formal del año académico con retrospectiva y traspaso de memoria al año siguiente.

## Steps

### Step 1: Final Coverage Check
- **Agent:** plan-coverage-checker
- **Gate:** Coverage must be 100% to proceed
- **If not 100%:** Alert professor and BLOCK closure

### Step 2: Generate Retrospective
- **Agent:** course-planner (Elena)
- **Output:** `retrospectiva.md` with:
  - Topics produced and their quality scores
  - Simulation vs reality comparison
  - Time allocation analysis
  - Lessons learned

### Step 3: Generate Handover Notes
- **Agent:** course-planner (Elena)
- **Output:** `notas-para-{año+1}.md` with:
  - What worked well
  - What needs improvement
  - Calibration data summary
  - Recommended changes for next year

### Step 3.5: Write Retrospective to Collective Memory
- **Action:** Ejecutar:
  ```
  python scripts/edu_memory.py add --course {course_id} --category retrospective \
    --summary "Cierre {course_id}: {resumen_principal}" \
    --detail "{contenido de notas-para-{año+1}.md resumido}"
  ```
- **Purpose:** Las lecciones del cierre quedan indexadas y buscables para años futuros y otras materias.
- **Also:** Exportar la memoria completa del curso para archivo:
  ```
  python scripts/edu_memory.py export --course {course_id} > {course_output_folder}/memoria-colectiva-{course_id}.md
  ```

### Step 4: Archive
- **Action:** Tag Git repository with `cursado-{año}`
- **Preserve:** All memory sidecars for continuity

### Step 5: Push Both Branches
- **Action:** `git push origin main` y `git push origin production`
- **Condition:** Run always after Step 4

