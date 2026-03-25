# Workflow: Load Official Plan

**Module:** edu
**Phase:** 1 — Configuración Inicial
**Owner Agent:** course-planner, plan-extractor (internal)

---

## Overview

Lee el PDF del programa institucional oficial y genera `plan-minimo.md` como contrato inmutable.

## Steps

### Step 1: Start Course Configuration
- **Agent:** course-planner (Elena)
- **Action:** Collect course metadata (name, institution, professor profile, class duration, LMS, language)
- **Output:** Update `_edu/config.yaml` with course-specific values

### Step 2: Load Official Plan PDF
- **Agent:** plan-extractor (internal)
- **Input:** PDF file path provided by professor
- **Action:** Extract all mandatory topics from the institutional program
- **Output:** Draft `plan-minimo.md` with numbered topics
- **Flag:** Ambiguous topics marked as `requires_human_review`

### Step 3: Review Plan
- **Agent:** course-planner (Elena)
- **Action:** Present extracted topics to professor for review
- **Gate:** Professor reviews and resolves any `requires_human_review` items

### Step 4: Confirm Official Plan
- **Agent:** course-planner (Elena)
- **Gate:** Explicit professor confirmation with "CONFIRMO"
- **Action:** Lock `plan-minimo.md` as IMMUTABLE contract
- **Post-condition:** No agent can ever modify this file after confirmation

