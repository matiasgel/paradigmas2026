# Workflow: Check Coverage

**Module:** edu
**Phase:** Anytime
**Owner Agent:** plan-coverage-checker

---

## Overview

Verifica el porcentaje de cobertura del plan mínimo en el estado actual del cursado.

## Steps

### Step 1: Load Coverage Matrix
- **Agent:** plan-coverage-checker
- **Input:** `plan-minimo.md` + all topic folders in `{topics_folder}` (leer de `_edu/config.yaml`)
- **Action:** Cross-reference mandatory topics with produced content

### Step 2: Generate Report
- **Output:** Coverage report with:
  - Total mandatory topics
  - Topics with completed content
  - Topics in progress
  - Topics not started
  - Risk assessment for uncovered topics
  - Overall coverage percentage

### Step 3: Alert if Critical
- **Condition:** If any mandatory topic has zero coverage and course is > 50% through
- **Action:** Display critical alert

