# Workflow Specification: reopen-topic

**Module:** edu
**Categoría:** Feature
**Prioridad de implementación:** 10
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Reabrir un tema cerrado para aplicar cambios de scope acotados, reabriendo solo los loops de calidad afectados por el cambio.

**Description:** Cuando el docente necesita modificar un tema ya cerrado (por cambio de scope, corrección significativa, o resultado de un cambio curricular), este workflow determina qué loops de calidad deben reabrirse según el alcance del cambio. No reabre todos los loops por defecto — solo los afectados.

**Workflow Type:** Create-only — reabre estado del tema y loops necesarios

---

## Workflow Structure

```yaml
---
name: reopen-topic
description: "Tema cerrado + scope del cambio → re-apertura acotada de loops necesarios"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/reopen-topic'
entryCommand: /edu-reopen-topic
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | assess-change-scope | Elena evalúa el alcance del cambio |
| step-02 | determine-loops | Determinar qué loops deben reabrirse |
| step-03 | reopen-branch | Reabrir la branch Git del tema |
| step-04 | execute-changes | Ejecutar los cambios con los agentes afectados |
| step-05 | rerun-loops | Ejecutar solo los loops necesarios |
| step-06 | close-again | Cerrar el tema nuevamente |

---

## Workflow Inputs

### Required Inputs

- `{N}` — número de tema
- Descripción del cambio requerido

---

## Agent Integration

### Primary Agent

`course-planner` (Elena) — determina scope + orquesta agentes afectados

### MCP Tools Required

- git — reabrir y volver a mergear la branch del tema

---

_Spec creada: 2026-03-06_
