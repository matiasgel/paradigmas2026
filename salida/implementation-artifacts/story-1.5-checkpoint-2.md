# Story 1.5 — Implementar Checkpoint 2 — aprobación del plan de generación

**ID:** S1.5
**Epic:** E1 — Pipeline base v3
**Status:** Done
**Creado:** 2026-05-23
**Implementado en:** salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md §CHECKPOINT 2 + salida/edu-standalone/_edu/agents/topic-designer-v3.md §paso-2

---

## Descripción

**Como** docente, **quiero** revisar y modificar el plan de filminas antes de que comience la generación del material, **para** controlar la estructura pedagógica del tema antes del proceso de generación.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Plan con metadatos
Al ejecutar Paso 2, produce lista numerada con: número, título descriptivo, conceptos cubiertos, nivel de densidad aplicado.

### CA-2 — Reordenamiento
- Docente: "mové la filmina 5 al final" → agente reordena y presenta plan modificado antes de pedir confirmación.

### CA-3 — Persistencia al aprobar
- "ok" → `checkpoint_2_aprobado: true` en state file + continúa al Paso 3.

### CA-4 — Loop de modificaciones
- Docente modifica plan → agente actualiza y vuelve a presentar CP2 (no genera sin aprobación explícita).

---

## Contrato de salida (AD-06 de arquitectura)

Antes de invocar `class-writer`:
- `checkpoint_1_aprobado: true` en state file ✓
- `checkpoint_2_aprobado: true` en state file ✓
- `topic-extract.md` existe en `{topic_folder}/` ✓
