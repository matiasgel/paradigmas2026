# Workflow Specification: update-copilot-context

**Module:** edu
**Categoría:** Utility
**Prioridad de implementación:** 15
**Status:** Placeholder — Pendiente de implementación
**Created:** 2026-03-06

---

## Workflow Overview

**Goal:** Regenerar `.github/copilot-instructions.md` con el contexto real y actualizado de la cursada activa.

**Description:** Elena lee el estado actual del sidecar (plan activo, temas completados, temas en progreso, loops pendientes, próximo paso recomendado) y regenera el archivo de instrucciones de Copilot para que el IDE tenga contexto completo de la cursada. Permite que Copilot asista al docente con conocimiento real del estado del módulo.

**Workflow Type:** Non-document (actualiza un archivo de configuración)

---

## Workflow Structure

```yaml
---
name: update-copilot-context
description: "Estado de la cursada → .github/copilot-instructions.md actualizado"
web_bundle: true
installed_path: '{project-root}/_edu/workflows/update-copilot-context'
entryCommand: /edu-update-copilot-context
---
```

---

## Planned Steps

| Step | Nombre | Goal |
|------|--------|------|
| step-01 | read-course-state | Leer estado completo del sidecar de Elena |
| step-02 | generate-context | Generar sección EDU para copilot-instructions.md |
| step-03 | update-file | Actualizar .github/copilot-instructions.md vía github |

---

## Workflow Inputs

### Required Inputs

- Ninguno (usa estado del sidecar de course-planner)

---

## Workflow Outputs

### Output Files

- `.github/copilot-instructions.md` — actualizado con sección EDU del estado actual

---

## Agent Integration

### Primary Agent

`course-planner` (Elena)

### MCP Tools Required

- GitHub — actualizar `.github/copilot-instructions.md`

---

_Spec creada: 2026-03-06_
