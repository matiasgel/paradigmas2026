# Workflow Specification: pedagogical-testing

**Module:** edu
**Categoría:** Feature
**Prioridad de implementación:** 7
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Simular la experiencia de aprendizaje de uno o más perfiles de alumno sobre el material del tema N, generando score pedagógico y FAQ anticipado.

**Description:** `student-simulator` lee el material del tema N con las limitaciones cognitivas del perfil activo y reporta confusiones, preguntas anticipadas y score de comprensión. `test-runner` consolida los resultados en `score-pedagogico.md` y `faq-anticipado.md`. El docente puede correr un perfil específico o todos a la vez.

**Workflow Type:** Create-only — produce score y FAQ

---

## Workflow Structure

```yaml
---
name: pedagogical-testing
description: "Tema N + perfiles → simulación → faq-anticipado.md + score-pedagogico.md"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/pedagogical-testing'
entryCommands:
  - /edu-test-topic
  - /edu-research-student-profiles
  - /edu-create-student-profile
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | load-profile | Cargar perfil de alumno activo (session-scoped) |
| step-02 | simulate | student-simulator lee el material con las lentes del perfil |
| step-03 | generate-faq | Extraer confusiones como preguntas anticipadas |
| step-04 | score | test-runner calcula score pedagógico |
| step-05 | multi-profile | Si `all`: iterar sobre todos los perfiles configurados |

---

## Workflow Inputs

### Required Inputs

- `{N}` — número de tema
- `{perfil}` — nombre del perfil o `all`

---

## Workflow Outputs

### Output Files

```
temas/NN-nombre/
  test-alumno-{perfil}.md
  faq-anticipado.md
  score-pedagogico.md
```

---

## Agent Integration

### Primary Agent

`student-simulator` → `test-runner` (motor interno)

### Sidecar

- **Session-scoped**: perfil activo + historial de la sesión → `_edu-memory/session/`
- **Long-term**: calibración acumulada → `_edu-memory/calibracion-simulador/{materia}-calibracion.md`

---

_Spec creada: 2026-03-06_
