# Workflow: Pedagogical Testing

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** student-simulator, test-runner (internal)

---

## Overview

Simula la experiencia de alumnos con diferentes perfiles antes de dar clase.

## Steps

### Step 1: Select Profile(s)
- **Agent:** student-simulator
- **Options:** Single profile or all profiles (batch mode)
- **Profiles:** estratégico, ansioso, disperso, recursero

### Step 2: Simulate Experience
- **Agent:** student-simulator
- **Input:** Topic's minuta.md + filminas.md
- **Mode:** Conversational (single) or batch (all profiles)
- **Action:** Process content through cognitive profile lens

### Step 3: Generate Reports
- **Agent:** test-runner (internal)
- **Output:**
  - `temas/NN-nombre/score-pedagogico.md` — quantifiable pedagogical score
  - `temas/NN-nombre/faq-anticipado.md` — anticipated student questions/confusions

### Step 4: Professor Review
- **Gate:** Professor reviews scores and decides if adjustments needed
- **If adjustments needed:** Return to appropriate step in topic-cycle
