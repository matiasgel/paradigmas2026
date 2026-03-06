# Workflow Specification: build-course-from-materials

**Module:** edu
**Categoría:** Feature
**Prioridad de implementación:** 5
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Construir el plan del curso a partir de material docente existente (PDFs, PPTX, DOCX) del año anterior — flujo brownfield.

**Description:** El docente provee una carpeta con material existente. `material-ingester` convierte todo a Markdown. Elena analiza el material convertido y propone un plan de temas organizado. El docente ajusta y confirma. El plan resultante se integra con el `plan-minimo.md` para verificar cobertura.

**Workflow Type:** Create-only — produce plan sugerido para revisión

---

## Workflow Structure

```yaml
---
name: build-course-from-materials
description: "PDFs/PPTX existentes → conversión → análisis → plan sugerido (brownfield)"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/build-course-from-materials'
entryCommand: /edu-build-course-from-materials
---
```

### Mode

- [x] Create-only (steps-c/)

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | ingest-materials | material-ingester convierte PDFs/PPTX/DOCX a Markdown |
| step-02 | analyze-content | Elena analiza el material convertido |
| step-03 | propose-plan | Elena propone plan de temas organizado |
| step-04 | review-and-adjust | Docente ajusta el plan propuesto |
| step-05 | coverage-check | Verificar cobertura del plan propuesto vs. plan-minimo.md |

---

## Workflow Inputs

### Required Inputs

- `{ruta-carpeta}` — carpeta con material existente (acepta PDFs, PPTX, DOCX, MD)

---

## Workflow Outputs

### Output Files

- `salida/{materia}/{año}/plan-de-estudio.md` — plan propuesto para revisión del docente

---

## Agent Integration

### Primary Agent

`material-ingester` (motor interno) → `course-planner` (Elena)

### MCP Tools Required

- herramienta de archivos — lectura de materiales y escritura de Markdown

---

_Spec creada: 2026-03-06_
