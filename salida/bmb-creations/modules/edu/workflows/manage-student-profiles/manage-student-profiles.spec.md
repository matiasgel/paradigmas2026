# Workflow Specification: manage-student-profiles

**Module:** edu
**Categoría:** Utility
**Prioridad de implementación:** 13
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Investigar y gestionar los perfiles de alumno empíricos disponibles para el simulador.

**Description:** `student-simulator` investiga en ERIC y ACM los perfiles cognitivos de alumnos universitarios correspondientes al nivel y disciplina de la materia. Los perfiles son basados en literatura académica verificable — no son inventados. El docente puede adoptar un perfil investigado o crear uno personalizado.

**Workflow Type:** Create-only — produce perfiles de alumno para el simulador

---

## Workflow Structure

```yaml
---
name: manage-student-profiles
description: "Materia + año curricular → investigación ERIC/ACM → perfiles empíricos disponibles"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/manage-student-profiles'
entryCommands:
  - /edu-research-student-profiles
  - /edu-create-student-profile
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | research-profiles | Investigar en ERIC/ACM perfiles empíricos relevantes |
| step-02 | present-profiles | Presentar perfiles encontrados con fuente académica |
| step-03 | adopt-or-create | Docente adopta perfil existente o crea uno personalizado |
| step-04 | save-profile | Guardar perfil en sidecar del simulador |

---

## Workflow Inputs

### Required Inputs

- `{materia}` — nombre o área de la materia
- `{año-curricular}` — año del plan de estudios (1er año, 2do año, etc.)

---

## Workflow Outputs

### Output Files

```
_edu-memory/perfiles-alumnos/
  {materia}-perfiles-investigados.md
  {materia}-perfil.md  ← perfil activo adoptado
```

---

## Agent Integration

### Primary Agent

`student-simulator`

### MCP Tools Required

- herramienta de búsqueda web con lista blanca: ERIC, ACM, Semantic Scholar

---

_Spec creada: 2026-03-06_
