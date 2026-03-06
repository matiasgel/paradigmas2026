# Workflow Specification: adaptive-replan

**Module:** edu
**Categoría:** Feature
**Prioridad de implementación:** 11
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Re-planificar los temas restantes de la cursada en tiempo real a partir de lo que realmente ocurrió en cada clase.

**Description:** El docente registra el resultado real de la clase (`/edu-register-class-result`): tiempo real utilizado y observaciones. Elena analiza el delta entre lo planificado y lo ocurrido, y propone ajustes a los temas no dictados aún. Permite ajuste de densidad si el perfil docente necesita recalibrarse.

**Workflow Type:** Create-only — produce propuesta de ajuste del plan restante

---

## Workflow Structure

```yaml
---
name: adaptive-replan
description: "Registros post-clase + plan restante → análisis de delta → propuesta de ajuste"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/adaptive-replan'
entryCommands:
  - /edu-register-class-result
  - /edu-adjust-remaining-plan
  - /edu-apply-density-adjustment
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | register-result | Registrar tiempo real + observaciones del docente |
| step-02 | analyze-delta | Elena calcula el delta planificado vs. real |
| step-03 | propose-adjustments | Proponer ajustes a temas N+1..M con justificación |
| step-04 | density-adjustment | Si delta de tiempo sostenido, proponer ajuste de densidad de perfil |
| step-05 | apply-plan | Docente confirma y Elena actualiza el plan |

---

## Workflow Inputs

### Required Inputs

- `{N}` — número de tema/clase
- `{minutos-reales}` — tiempo real utilizado
- `"{observaciones}"` — notas del docente post-clase

---

## Workflow Outputs

### Output Files

- `salida/{materia}/{año}/ajuste-plan-{fecha}.md`

---

## Agent Integration

### Primary Agent

`course-planner` (Elena)

### Other Agents

`plan-coverage-checker` — consultado internamente para verificar que los ajustes no comprometan cobertura

---

_Spec creada: 2026-03-06_
