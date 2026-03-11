# Workflow: Curriculum Change

**Module:** edu
**Phase:** 2 — Planificación del Cursado
**Owner Agent:** curriculum-reviewer

---

## Overview

Propone cambios curriculares con justificación académica. Solo puede modificar `plan-borrador.md`, NUNCA `plan-minimo.md`.

## Steps

### Step 1: Identify Change
- **Agent:** curriculum-reviewer (Ana)
- **Input:** Professor request or detected academic evolution
- **Action:** Formulate change proposal with academic evidence

### Step 2: Validate Against Plan Mínimo
- **Agent:** curriculum-reviewer (Ana)
- **Check:** Ensure proposed change does NOT affect any `plan-minimo.md` topic
- **Gate:** If it touches plan-minimo → REJECT with explanation

### Step 3: Generate Proposal
- **Agent:** curriculum-reviewer (Ana)
- **Output:** `curriculum-proposal.md` with:
  - Change description
  - Academic justification (minimum 2 peer-reviewed sources)
  - Impact analysis on existing topics
  - Recommended implementation timeline

### Step 4: Professor Decision
- **Gate:** Professor approves/rejects
- **If approved:** Apply changes to `plan-borrador.md`

