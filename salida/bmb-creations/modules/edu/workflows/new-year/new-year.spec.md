# Workflow Specification: new-year

**Module:** edu
**Categoría:** Feature
**Prioridad de implementación:** 8
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Iniciar el nuevo año lectivo a partir de los datos del año anterior, con el simulador ya calibrado y sin empezar de cero.

**Description:** Elena lee la `retrospectiva-anual.md` del año anterior y el estado de calibración del simulador. Propone un borrador del nuevo plan incorporando los aprendizajes del año anterior. El docente puede copiar temas sin cambios (`/edu-copy-topic`) o abrirlos para mejora (`/edu-adapt-topic`).

**Workflow Type:** Create-only — produce borrador del plan del nuevo año

---

## Workflow Structure

```yaml
---
name: new-year
description: "Año anterior → lectura retrospectiva + simulador calibrado → borrador nuevo plan"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/new-year'
entryCommand: /edu-start-new-year
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | load-retrospective | Cargar retrospectiva-anual.md del año anterior |
| step-02 | load-calibration | Cargar calibración acumulada del simulador |
| step-03 | propose-new-plan | Elena propone el plan del nuevo año con mejoras incorporadas |
| step-04 | copy-or-adapt | Docente decide tema a tema: copiar sin cambios o abrir para mejora |

---

## Workflow Inputs

### Required Inputs

- `{materia}` — nombre de la materia
- `{año-nuevo}` — año lectivo nuevo

---

## Workflow Outputs

### Output Files

- `salida/{materia}/{año-nuevo}/plan-de-estudio.md` — borrador del nuevo año
- Temas copiados: `temas/NN-*/` con flag `source: {año-anterior}`

---

## Agent Integration

### Primary Agent

`course-planner` (Elena)

### Sidecar

Sidecar long-term del `student-simulator` — calibración acumulada disponible desde el inicio

---

_Spec creada: 2026-03-06_
