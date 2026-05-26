# Story 5.1 — Implementar procesamiento del parámetro --base

**ID:** S5.1
**Epic:** E5 — Renovación de año anterior
**Status:** Done
**Archivos modificados/creados:**
- `_edu/workflows/topic-cycle-v3/workflow.md` (ya implementado en Sprint 1: Paso 0 ítem 3 + Paso 2)
- `_edu/tasks/renovacion-anio-anterior.md` (NEW — algoritmo de renovación)

---

## Descripción

**Como** docente, **quiero** pasar `--base RUTA_FILMINAS_PREVIAS` al invocar `@topic-cycle-v3`, **para** que el pipeline analice las filminas del año anterior y sugiera qué conservar, actualizar o generar nuevo.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Parámetro en Paso 0
- `--base` ya está en la invocación canónica y el Paso 0 lo guarda en `.pipeline-v3-state.yaml → base_filminas_previas`.

### CA-2 — Resolución de ruta
- Ruta relativa → resolver relativa a `{topic_folder}`. Error inmediato si no existe.

### CA-3 — Activación en Paso 2
- Si `--base` presente → ejecutar análisis comparativo (tarea `renovacion-anio-anterior.md`).

### CA-4 — Archivo de acciones
- Genera `{topic_folder}/filminas-base-acciones.yaml` con acciones por filmina para class-writer.

### CA-5 — Sin acción si --base ausente
- Si `--base` no está → Paso 2 funciona en modo normal, sin diferencias.
