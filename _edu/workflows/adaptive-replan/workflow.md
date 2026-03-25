# Workflow: Adaptive Replan

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** course-planner

---

## Overview

Ajusta el cronograma del cursado cuando hay temas atrasados, respetando SIEMPRE el plan mínimo.

## Steps

### Step 1: Assess Current State
- **Agent:** course-planner (Elena)
- **Input:** Coverage matrix + topic statuses + remaining calendar
- **Action:** Identify delayed topics and time remaining

### Step 2: Propose Replan
- **Agent:** course-planner (Elena)
- **Constraint:** NEVER remove or reduce mandatory plan-minimo topics
- **Options:**
  - Merge optional topics
  - Adjust time allocation
  - Compress quality loops (NOT skip them)
  - Propose marathon sessions
- **Output:** `plan-actualizado.md`

### Step 3: Coverage Verification
- **Agent:** plan-coverage-checker
- **Check:** Verify replan still covers 100% of plan-minimo.md
- **Gate:** BLOCK if any mandatory topic would be dropped

### Step 4: Professor Approval
- **Gate:** Professor reviews and approves the updated plan

