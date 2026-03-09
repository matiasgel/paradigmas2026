# Workflow: Update Copilot Context

**Module:** edu
**Phase:** Anytime
**Owner Agent:** course-planner

---

## Overview

Actualiza el contexto activo de Copilot. Útil al retomar sesión o después de cambios grandes.

## Steps

### Step 1: Scan Current State
- **Agent:** course-planner (Elena)
- **Action:** Read all current course artifacts:
  - `_edu/config.yaml` — module config
  - `plan-minimo.md` — immutable contract
  - `plan-borrador.md` — course plan
  - Coverage matrix from `_edu-memory/`
  - Active topic status

### Step 2: Build Context Summary
- **Output:** Structured summary of:
  - Current phase
  - Active topic and its production status
  - Pending actions
  - Next recommended step

### Step 3: Display to Professor
- **Action:** Present context summary and await instructions

