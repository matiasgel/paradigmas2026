# Story 2.3 — Paso 1b: Enriquecimiento con libros secundarios

**ID:** S2.3
**Epic:** E2 — Bibliographic-first
**Status:** Done
**Creado:** 2026-05-23
**Implementado en:** salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md §Paso 1b + salida/edu-standalone/_edu/tasks/topic-extract-generation.md §paso-1b

---

## Descripción

**Como** topic-designer-v3, **quiero** enriquecer la bibliografía con sub-temas no suficientemente cubiertos en Paso 1a consultando libros secundarios en ChromaDB, **para** ampliar la cobertura conceptual sin duplicar fuentes del libro principal.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Identificación de gaps
- Identifica sub-temas con cobertura insuficiente en el resultado del Paso 1a.

### CA-2 — Query secundaria sin filtro libro
- Consulta `edu_knowledge` sin filtrar por `libro_principal` para encontrar cobertura en otros libros.

### CA-3 — Deduplicación
- Filtra resultados que ya fueron capturados del libro principal.

### CA-4 — No bloqueante
- Si falla → `⚠️ ADVERTENCIA: No se pudo enriquecer con libros secundarios. Continuando con libro principal únicamente.`
