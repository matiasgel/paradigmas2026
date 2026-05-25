# Story 4.2 — Implementar modificadores de densidad en class-writer (niveles 1, 2 y 3)

**ID:** S4.2
**Epic:** E4 — Niveles de densidad
**Status:** Done
**Archivos modificados:**
- `_edu/agents/class-writer.md` (ya modificado en Story 6.1 con bloques N1/N2/N3)
- `_edu/tasks/density-levels.md` (detalla modificadores de filminas)

---

## Descripción

**Como** class-writer, **quiero** ajustar el número de conceptos por filmina, la cantidad de ejemplos y el estilo de citas según el nivel leído del estado del pipeline, **para** que las filminas generen el nivel de profundidad correcto.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Modificadores de Nivel 1
- ≤ 3 conceptos/filmina, 1 ejemplo directo, formato simple, cita principal únicamente.

### CA-2 — Modificadores de Nivel 2
- ≤ 5 conceptos/filmina, 2–3 ejemplos, comparación contextual, referencias de fuentes y ejemplos.

### CA-3 — Modificadores de Nivel 3
- Sin límite, múltiples ejemplos + contra-ejemplos, máxima profundidad, todas las referencias.

### CA-4 — Fuente del nivel
- Lee `nivel` de `{topic_folder}/.pipeline-v3-state.yaml` en modo v3.

### CA-5 — Implementación en class-writer.md
- Sección v3 de class-writer.md ya incluye los 3 niveles con sus modificadores de densidad.

### CA-6 — nivel_minimo respetado
- Si un concepto tiene `nivel_minimo: 3` en topic-extract.md → no incluirlo en N1 ni N2.
