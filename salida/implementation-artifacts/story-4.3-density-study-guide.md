# Story 4.3 — Implementar propagación de nivel en study-guide-writer

**ID:** S4.3
**Epic:** E4 — Niveles de densidad
**Status:** Done
**Archivos modificados:**
- `_edu/agents/study-guide-writer.md` (ya modificado en Story 6.2 con bloques N1/N2/N3)
- `_edu/tasks/density-levels.md` (detalla modificadores de guía de estudio)

---

## Descripción

**Como** study-guide-writer, **quiero** ajustar la profundidad de la guía de estudio según el nivel leído del estado del pipeline, **para** que la guía sea coherente con las filminas y el nivel pedagógico elegido.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Modificadores de Nivel 1 en guía
- Guía concisa: conceptos esenciales, 1 ejemplo trabajado, 5 preguntas autoevaluación, solo términos esenciales en glosario.

### CA-2 — Modificadores de Nivel 2 en guía
- Guía estándar: desarrollo completo, 2–3 ejemplos, 8 preguntas, glosario completo.

### CA-3 — Modificadores de Nivel 3 en guía
- Guía exhaustiva: máxima profundidad, múltiples ejemplos + contra-ejemplos + ejercicios, 10+ preguntas, glosario extendido.

### CA-4 — Coherencia nivel filminas/guía
- Ambos leen el mismo `nivel` del state file → misma profundidad sin configuración extra.

### CA-5 — Implementación en study-guide-writer.md
- Sección v3 de study-guide-writer.md ya incluye los 3 niveles con modificadores de guía.

### CA-6 — nivel_minimo respetado
- Si un concepto tiene `nivel_minimo: 2` o `3` → ajustar su presencia en §5 y §9 de la guía.
