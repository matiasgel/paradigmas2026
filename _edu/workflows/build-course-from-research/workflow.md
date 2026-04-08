# Workflow: Build Course from Research

**Module:** edu
**Phase:** 2 — Planificación del Cursado
**Owner Agent:** course-planner, academic-researcher

---

## Overview

Construye el plan del cursado desde investigación académica pura. Alternativa a build-from-materials cuando no hay material previo.

## Steps

### Step 1: Research Topics
- **Agent:** academic-researcher (Carlos)
- **Input:** `plan-minimo.md` mandatory topics
- **Action:** Search academic literature for each topic
- **Output:** Research notes per topic

### Step 2: Propose Plan
- **Agent:** course-planner (Elena)
- **Input:** Research notes + `plan-minimo.md`
- **Action:** Build topic sequence with durations based on research complexity
- **Output:** `plan-borrador.md`

### Step 3: Professor Review
- **Agent:** course-planner (Elena)
- **Gate:** Professor reviews and adjusts
- **Output:** Approved `plan-borrador.md`

