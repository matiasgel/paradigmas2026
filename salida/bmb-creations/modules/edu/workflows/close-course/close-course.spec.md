# Workflow Specification: close-course

**Module:** edu
**Categoría:** Core — camino feliz crítico
**Prioridad de implementación:** 4
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Cerrar la cursada, generar la retrospectiva anual con score pedagógico comparado, y proteger las branches del año como solo lectura.

**Description:** Workflow de cierre de cursada. Verifica cobertura completa del `plan-minimo.md` como pre-condición (bloqueante). Genera `retrospectiva-anual.md` con comparación de score pedagógico vs. año anterior (si existe). Protege las branches Git del año. Deja preparado el estado para `/edu-start-new-year`.

**Workflow Type:** Create-only — produce retrospectiva y cierra el ciclo anual

---

## Workflow Structure

### Entry Point

```yaml
---
name: close-course
description: "Cierre de cursada: retrospectiva + score + protección de branches"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/close-course'
entryCommand: /edu-close-course
---
```

### Mode

- [x] Create-only (steps-c/)

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | verify-coverage | Verificar cobertura 100% del plan-minimo.md (bloqueante) |
| step-02 | verify-topics-closed | Verificar que todos los temas estén cerrados (bloqueante) |
| step-03 | generate-retrospective | Generar retrospectiva-anual.md con score pedagógico acumulado |
| step-04 | compare-years | Comparar score con año anterior (si existe) |
| step-05 | protect-branches | Proteger branches del año como solo lectura via git |
| step-06 | prepare-next-year | Dejar estado listo para /edu-start-new-year |

---

## Workflow Inputs

### Required Inputs

- `{materia}` — nombre de la materia
- `{año}` — año lectivo

### Optional Inputs

- Ninguno

---

## Workflow Outputs

### Output Format

- [x] Document-producing

### Output Files

```
salida/{materia}/{año}/
  retrospectiva-anual.md
  cobertura-final.md
  comparacion-vs-anio-anterior.md (si existe año anterior)
  score-pedagogico.md (consolidado de todos los temas)
```

---

## Agent Integration

### Primary Agent

`course-planner` (Elena) — orquesta todo el flujo

### Other Agents

`plan-coverage-checker` — verificación de cobertura (bloqueante)

### MCP Tools Required

- herramienta de archivos — lectura de todos los scores del año + escritura de retrospectiva
- git — protección de branches del año

---

## Notas de implementación

- Bloqueado si `plan-coverage-checker` reporta cobertura incompleta
- Bloqueado si algún tema no tiene estado `cerrado`
- Tras el cierre, `/edu-start-new-year` carga la retrospectiva como contexto base del nuevo año

---

_Spec creada: 2026-03-06_
