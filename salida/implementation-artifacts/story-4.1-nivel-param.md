# Story 4.1 — Implementar parámetro --nivel y propagación al estado del pipeline

**ID:** S4.1
**Epic:** E4 — Niveles de densidad
**Status:** Done
**Archivos modificados/creados:**
- `_edu/workflows/topic-cycle-v3/workflow.md` (ya implementado en Sprint 1)
- `_edu/agents/topic-designer-v3.md` (ya implementado en Sprint 1)
- `_edu/tasks/density-levels.md` (NEW — documentación extendida)
- `_edu/schemas/topic-extract-schema.yaml` (agrega campo `nivel_minimo` a conceptos-clave)

---

## Descripción

**Como** docente, **quiero** pasar `--nivel 1|2|3` al invocar `@topic-cycle-v3`, **para** que toda la cadena de generación aplique el nivel de densidad correcto sin configuración adicional.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Parámetro en invocación
- `--nivel 1|2|3` ya está en la invocación canónica del workflow.md (Paso 0).

### CA-2 — Default nivel 2
- Si `--nivel` ausente → nivel 2 por defecto. Paso 0 y mensaje de bienvenida ya implementados.

### CA-3 — Persistencia en estado
- `nivel` se guarda en `.pipeline-v3-state.yaml` al completar Paso 0.

### CA-4 — Legible por agentes downstream
- Agentes downstream leen `nivel` del state file en modo v3. Implementado en 6.1 y 6.2.

### CA-5 — Task file de densidad
- `tasks/density-levels.md` documenta la propagación completa con tabla de modificadores por agente.

### CA-6 — Campo nivel_minimo en schema
- `conceptos-clave` ahora soporta campo opcional `nivel_minimo` para marcar conceptos solo de N3.
