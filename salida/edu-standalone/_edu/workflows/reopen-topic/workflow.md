# Workflow: Reopen Topic

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** course-planner

---

## Overview

Reabre un tema cerrado para aplicar correcciones mayores.

## Steps

### Step 1: Verify Topic is Closed
- **Agent:** course-planner (Elena)
- **Check:** Topic must have status "closed"

### Step 2: Justify Reopening
- **Agent:** course-planner (Elena)
- **Gate:** Professor must provide reason for reopening
- **Log:** Reason recorded in topic metadata

### Step 3: Reactivate Git Branch
- **Action:** Create new branch from the topic's merge commit
- **Branch name:** `reopen/tema-NN-nombre`

### Step 4: Resume Topic Cycle
- **Action:** Topic returns to the appropriate step in topic-cycle workflow
- **Note:** All previous quality loop results are preserved for reference

