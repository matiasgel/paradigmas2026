# Workflow Specification: build-course-from-research

**Module:** edu
**Categoría:** Feature
**Prioridad de implementación:** 6
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Construir el plan del curso desde cero a partir de investigación académica — flujo greenfield.

**Description:** El docente provee el tema o los objetivos de la materia. `academic-researcher` (Carlos) investiga en fuentes académicas verificables. Elena analiza los resultados y propone un plan de temas con bibliografía integrada. Ideal para materias nuevas o cuando no hay material previo.

**Workflow Type:** Create-only — produce plan sugerido con bibliografía

---

## Workflow Structure

```yaml
---
name: build-course-from-research
description: "Tema/objetivos → investigación académica → plan sugerido (greenfield)"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/build-course-from-research'
entryCommand: /edu-research-plan
---
```

### Mode

- [x] Create-only (steps-c/)

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | define-scope | El docente define tema, nivel, objetivos |
| step-02 | research | academic-researcher investiga en arXiv, ACM, IEEE, Semantic Scholar, ERIC |
| step-03 | structure-plan | Elena estructura el plan a partir de los papers encontrados |
| step-04 | review-and-adjust | Docente ajusta el plan propuesto |
| step-05 | coverage-check | Verificar cobertura del plan propuesto vs. plan-minimo.md |

---

## Workflow Inputs

### Required Inputs

- Tema o descripción de la materia (en conversación)

---

## Workflow Outputs

### Output Files

- `salida/{materia}/{año}/plan-de-estudio.md` — plan propuesto con bibliografía integrada

---

## Agent Integration

### Primary Agent

`academic-researcher` (Carlos) → `course-planner` (Elena)

### MCP Tools Required

- herramienta de búsqueda web con lista blanca: arXiv, ACM, IEEE, Springer, Semantic Scholar, ERIC

---

_Spec creada: 2026-03-06_
