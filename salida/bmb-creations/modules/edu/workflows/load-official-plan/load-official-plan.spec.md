# Workflow Specification: load-official-plan

**Module:** edu
**Categoría:** Core — camino feliz crítico
**Prioridad de implementación:** 1 (primer workflow a implementar)
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Extraer los tópicos obligatorios del PDF del programa institucional oficial y generar `plan-minimo.md` como contrato inmutable de la cursada.

**Description:** El docente provee el PDF del programa de la asignatura emitido por la institución. `plan-extractor` (motor interno) lee el PDF y extrae todos los tópicos obligatorios. Elena presenta el resultado al docente para revisión. Tras `/edu-confirm-official-plan`, `plan-minimo.md` se bloquea como solo lectura para el resto de la cursada. Ningún agente puede modificarlo desde ese momento.

**Workflow Type:** Create-only — produce un documento inmutable

---

## Workflow Structure

### Entry Point

```yaml
---
name: load-official-plan
description: "Extrae tópicos del programa institucional y genera plan-minimo.md bloqueado"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/load-official-plan'
entryCommand: /edu-load-official-plan
confirmCommand: /edu-confirm-official-plan
---
```

### Mode

- [x] Create-only (steps-c/)

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | extract-topics | plan-extractor lee el PDF y extrae tópicos |
| step-02 | review-topics | Elena presenta tópicos al docente para revisión/ajuste manual |
| step-03 | confirm-and-lock | /edu-confirm-official-plan bloquea plan-minimo.md como inmutable |

---

## Workflow Inputs

### Required Inputs

- `{ruta-pdf}` — ruta al PDF del programa institucional oficial

### Optional Inputs

- Ninguno

---

## Workflow Outputs

### Output Format

- [x] Document-producing

### Output Files

- `salida/{materia}/{año}/plan-minimo.md` — **INMUTABLE tras confirmar**

---

## Agent Integration

### Primary Agent

`plan-extractor` (motor interno) → `course-planner` (Elena, presenta y confirma)

### Other Agents

`plan-coverage-checker` — inicializa su sidecar con los tópicos del plan-minimo al confirmar

### MCP Tools Required

- herramienta de archivos — lectura del PDF de programa + escritura del plan-minimo.md

---

## Notas de implementación

- El bloqueo de `plan-minimo.md` se implementa marcando el archivo como read-only via herramienta de archivos tras la confirmación
- Los tópicos ambiguos o poco claros del PDF deben ser marcados `requires_human_review` por el plan-extractor antes de la presentación
- Este workflow es **prerequisito** para: `topic-cycle`, `check-coverage`, `close-course`

---

_Spec creada: 2026-03-06_
