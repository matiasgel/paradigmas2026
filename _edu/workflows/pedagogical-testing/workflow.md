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
- **Input:** Topic's `minuta.md` + `filminas.md` + `guia-estudio.md` (if it exists)
- **Mode:** Conversational (single) or batch (all profiles)
- **Action:** Process content through cognitive profile lens
- **Dual perspective:** Simulate BOTH the in-class experience (minuta + filminas) AND the self-study experience (guia-estudio). If `guia-estudio.md` is missing, notify the professor and simulate only the in-class experience.

### Step 3: Generate Reports
- **Agent:** test-runner (internal)
- **Output:**
  - `{topic_folder}/score-pedagogico.md` — quantifiable pedagogical score (includes separate sub-scores for class materials and study guide if both are present)
  - `{topic_folder}/faq-anticipado.md` — anticipated student questions/confusions (grouped by source: "En clase" vs "Estudiando solos")

### Step 4: Professor Review
- **Gate:** Professor reviews scores and decides if adjustments needed
- **If adjustments needed:** Return to appropriate step in topic-cycle

