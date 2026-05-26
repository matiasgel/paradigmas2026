# Story 2.2 — Paso 1a: Extracción ChromaDB libro principal con fail-fast

**ID:** S2.2
**Epic:** E2 — Bibliographic-first
**Status:** Done
**Creado:** 2026-05-23
**Implementado en:** salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md §Paso 1a + salida/edu-standalone/_edu/tasks/topic-extract-generation.md §paso-1a

---

## Descripción

**Como** topic-designer-v3, **quiero** implementar el Paso 1a con verificación fail-fast de chroma-mcp y extracción multi-query del libro principal, **para** garantizar grounding bibliográfico verificado antes de generar cualquier material.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Fail-fast ante chroma-mcp no disponible
- Si chroma-mcp no responde → STOP inmediato con diagnóstico claro.

### CA-2 — Query multi-término
- Busca `{tópico}`, `{tópico} conceptos fundamentales`, `{tópico} definición` en `edu_knowledge` filtrando por `libro_principal`.

### CA-3 — Fallback sin filtro libro
- 0 resultados con filtro libro → reintento sin filtro; si sigue en 0 → STOP con diagnóstico.

### CA-4 — Marcado de referencias incompletas
- Fragmentos con `pagina: null` marcados como `⚠️ referencia incompleta`.
