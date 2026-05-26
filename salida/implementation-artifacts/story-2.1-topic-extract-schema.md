# Story 2.1 — Crear esquema formal topic-extract-schema.yaml

**ID:** S2.1
**Epic:** E2 — Bibliographic-first
**Status:** Done
**Creado:** 2026-05-23
**Implementado en:** salida/edu-standalone/_edu/schemas/topic-extract-schema.yaml

---

## Descripción

**Como** agente topic-designer-v3, **quiero** un schema YAML formal con tipos, restricciones y validaciones para `topic-extract.md`, **para** que todos los agentes downstream parseen el artefacto de forma consistente.

---

## Criterios de Aceptación

### CA-1 — Secciones obligatorias
El schema define las 5 secciones: `fuentes`, `conceptos-clave`, `ejemplos-bibliograficos`, `tendencias`, `superposiciones-detectadas`.

### CA-2 — Validaciones
- `fuentes`: mínimo 1 ítem con `pagina` no nulo
- `conceptos-clave`: mínimo 3 ítems
- Items con `pagina: null` marcados con `⚠️ referencia incompleta`

### CA-3 — Compatibilidad con agentes downstream
El schema es compatible con el formato que leen `class-writer`, `study-guide-writer` y `create-teacher-guide`.
