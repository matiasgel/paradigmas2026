# Workflow Specification: check-coverage

**Module:** edu
**Categoría:** Utility
**Prioridad de implementación:** 14
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Generar y mostrar la matriz de cobertura del plan mínimo institucional contra el estado actual del plan de estudios.

**Description:** `plan-coverage-checker` consulta su sidecar persistente y genera `cobertura-actual.md` con el estado de cada tópico obligatorio: cubierto, en progreso, pendiente, o en riesgo. También permite exportar la matriz a Google Sheets.

**Workflow Type:** Non-document en modo lazy (no genera cambios) / document-producing al exportar

---

## Workflow Structure

```yaml
---
name: check-coverage
description: "Estado actual → matriz de cobertura → cobertura-actual.md"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/check-coverage'
entryCommand: /edu-check-coverage
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | load-coverage-state | Cargar sidecar del plan-coverage-checker |
| step-02 | generate-matrix | Generar tabla de cobertura actualizada |
| step-03 | highlight-risks | Destacar tópicos en riesgo |
| step-04 | export (opcional) | Exportar a Google Sheets si se solicita |

---

## Workflow Inputs

### Required Inputs

- Ninguno (usa estado de sidecar)

---

## Workflow Outputs

### Output Files

- `salida/{materia}/{año}/cobertura-actual.md`
- (opcional) Google Sheets vía Google Workspace

---

## Agent Integration

### Primary Agent

`plan-coverage-checker` (sidecar persistente)

### Other Agents

`course-planner` (Elena) — puede invocar este workflow internamente antes de cualquier cierre

---

_Spec creada: 2026-03-06_
