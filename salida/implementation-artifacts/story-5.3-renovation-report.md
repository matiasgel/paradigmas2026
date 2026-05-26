# Story 5.3 — Implementar reporte de renovación y priorización en generación

**ID:** S5.3
**Epic:** E5 — Renovación de año anterior
**Status:** Done
**Archivos modificados/creados:**
- `_edu/tasks/renovacion-anio-anterior.md` (Paso 4: integración con CP2 y class-writer)
- `_edu/agents/class-writer.md` (sección v3 ya prepara backup y lógica de regeneración)

---

## Descripción

**Como** docente, **quiero** que el plan de CP2 incluya la columna `Acción` con el resultado del análisis, **para** poder ajustar qué filminas se conservan, actualizan o crean nuevas antes de aprobar la generación.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Plan de CP2 con columna Acción
- Cuando `--base` fue especificado, el plan de CP2 incluye columna `Acción` (conservar/actualizar/nueva).

### CA-2 — filminas-base-acciones.yaml
- El archivo de acciones se genera en `{topic_folder}/filminas-base-acciones.yaml` antes de CP2.

### CA-3 — Uso por class-writer
- class-writer en modo v3: lee `filminas-base-acciones.yaml` si existe y aplica cada acción.
- `conservar` → copia filmina previa sin cambios.
- `actualizar` → usa filmina previa como base, aplica delta de topic-extract.md.
- `nueva` → genera desde cero.

### CA-4 — Priorización de generación
- Docente puede solicitar generar solo `actualizar` + `nueva` (salteando las `conservar`).

### CA-5 — Backup automático
- Antes de sobrescribir filminas.md → crear filminas-v2-backup.md (protocolo de backup de S6.4).

### CA-6 — Sin --base → sin impacto
- Si `--base` no está → `filminas-base-acciones.yaml` no se genera → class-writer funciona en modo normal v3.
