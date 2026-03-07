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
- **Action:** Read and internalize previous year's lessons

### Step 2: Clean Workspace
- **Action:** Archive previous year's `temas/` folder
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
