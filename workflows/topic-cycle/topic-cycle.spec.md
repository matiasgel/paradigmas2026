# Workflow Specification: topic-cycle

**Module:** edu
**Categoría:** Core — camino feliz crítico
**Prioridad de implementación:** 2
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Orquestar el ciclo completo de producción de un tema: diseño → clase → TP, con la duración como constraint central.

**Description:** Flujo secuencial para producir los documentos del tema N. Marcos diseña el contenido con la duración como constraint. Roberto genera la minuta y filminas proporcionales. Valeria genera el TP trazable a la minuta. El resultado es la carpeta `temas/NN-nombre/` completa, lista para entrar a los loops de calidad.

**Workflow Type:** Create-only — produce documentos del tema

---

## Workflow Structure

### Entry Point

```yaml
---
name: topic-cycle
description: "Diseño → clase → TP: producción completa de un tema"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/topic-cycle'
entryCommands:
  - /edu-design-topic
  - /edu-create-class
  - /edu-create-tp
---
```

### Mode

- [x] Create-only (steps-c/)

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | design-topic | topic-designer genera diseño.md con duración como constraint |
| step-02 | assign-topics | Mapeo explícito de tópicos del plan-minimo.md al tema N |
| step-03 | create-class | class-writer genera minuta.md y filminas.md |
| step-04 | create-tp | tp-designer genera tp.md trazable a minuta.md |
| step-05 | validate-coverage | Verificación de que el material cubre los tópicos asignados |

---

## Workflow Inputs

### Required Inputs

- `{N}` — número de tema
- `{duracion}` — en minutos (tomada de config o sobrescrita con `/edu-set-topic-duration`)

### Optional Inputs

- `{IDs-topicos}` — asignación explícita de tópicos del plan-minimo (o auto-detectada)

---

## Workflow Outputs

### Output Format

- [x] Document-producing

### Output Files

```
temas/NN-nombre-del-tema/
  diseño.md         ← duración como constraint
  minuta.md
  filminas.md
  tp.md
  cobertura-tema.md
```

---

## Agent Integration

### Primary Agent

`topic-designer` (Marcos) → `class-writer` (Roberto) → `tp-designer` (Valeria) — orquestados por `course-planner` (Elena)

### Other Agents

`plan-coverage-checker` — consultado al final para validar cobertura del tema

### MCP Tools Required

- herramienta de archivos — escritura de documentos en `temas/NN-*/`
- git — crear branch `tema/NN-nombre-del-tema`

---

## Notas de implementación

- Cambiar duración con `/edu-set-topic-duration` dispara regeneración del step-03 en adelante y reabre loops si ya estaban ejecutados
- El tema NO puede cerrarse (`/edu-close-topic`) hasta que los loops de calidad estén completos
- Prerequisito: `load-official-plan` completado y confirmado

---

_Spec creada: 2026-03-06_
