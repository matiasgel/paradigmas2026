# Workflow Specification: curriculum-change

**Module:** edu
**Categoría:** Feature
**Prioridad de implementación:** 9
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Proponer cambios al plan de estudios basados en el estado del arte académico, con justificación verificable por fuente académica.

**Description:** `curriculum-reviewer` (Prof. Ana) analiza el plan actual y detecta posibles desalineaciones con el estado del arte. Trabaja con `academic-researcher` para buscar evidencia académica. Produce una propuesta formal con justificación por fuente. La decisión final es siempre del docente.

**Workflow Type:** Create-only — produce propuesta de cambio curricular

---

## Workflow Structure

```yaml
---
name: curriculum-change
description: "Plan actual + señal de cambio → propuesta justificada con fuente académica"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/curriculum-change'
entryCommand: /edu-propose-curriculum-change
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | analyze-current-plan | curriculum-reviewer analiza el plan actual |
| step-02 | research-state-of-art | academic-researcher busca evidencia del estado del arte |
| step-03 | draft-proposal | curriculum-reviewer redacta la propuesta con fuente académica |
| step-04 | present-to-teacher | Elena presenta la propuesta al docente para decisión |

---

## Workflow Inputs

### Required Inputs

- Señal de cambio: puede ser una observación del docente o resultado del cierre de cursada

---

## Workflow Outputs

### Output Files

- `salida/{materia}/{año}/curriculum-change-proposal.md`

---

## Agent Integration

### Primary Agent

`curriculum-reviewer` (Prof. Ana) + `academic-researcher` (Carlos)

### Other Agents

`course-planner` (Elena) — presenta la propuesta al docente

---

_Spec creada: 2026-03-06_
