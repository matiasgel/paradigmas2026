# Workflow Specification: student-feedback-loop

**Module:** edu
**Categoría:** Feature
**Prioridad de implementación:** 12
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Procesar las respuestas reales de alumnos a las encuestas, compararlas con las predicciones del simulador, y calibrar el perfil de alumno simulado para mejorar su precisión en cursadas futuras.

**Description:** El docente registra las respuestas de la encuesta (`/edu-analyze-survey`). `student-simulator` compara las predicciones previas con las respuestas reales. El delta se almacena en el sidecar long-term del simulador. Este es el mecanismo que hace que el simulador mejore año a año.

**Workflow Type:** Create-only — calibra el sidecar long-term del simulador

---

## Workflow Structure

```yaml
---
name: student-feedback-loop
description: "Respuestas reales de alumnos → comparación con predicciones → simulador calibrado"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/student-feedback-loop'
entryCommands:
  - /edu-create-survey
  - /edu-export-survey
  - /edu-analyze-survey
  - /edu-compare-survey-simulator
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | create-survey | Generar encuesta guiada desde faq-anticipado.md del tema |
| step-02 | export-survey | Publicar encuesta en LMS configurado |
| step-03 | analyze-responses | Procesar respuestas y actualizar score-pedagogico.md |
| step-04 | compare-with-simulator | Calcular delta predicciones del simulador vs. respuestas reales |
| step-05 | calibrate-simulator | Almacenar delta en sidecar long-term del simulador |

---

## Workflow Inputs

### Required Inputs

- `{N}` — número de tema
- Respuestas de la encuesta (importadas del LMS o provistas manualmente)

---

## Workflow Outputs

### Output Files

```
temas/NN-nombre/
  encuesta-{N}.md         ← preguntas generadas
  respuestas-{N}.md       ← análisis de respuestas reales
  calibracion-simulador-{N}.md
_edu-memory/calibracion-simulador/{materia}-calibracion.md  ← actualizado (long-term)
```

---

## Agent Integration

### Primary Agent

`student-simulator` — ejecuta la comparación y calibra el sidecar

### MCP Tools Required

- conector LMS — export de encuesta a Moodle / Google Forms
- Google Workspace — si lms_provider = google-classroom

---

_Spec creada: 2026-03-06_
