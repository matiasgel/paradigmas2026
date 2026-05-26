# Story 2.4 — Paso 1c: Web research de tendencias académicas

**ID:** S2.4
**Epic:** E2 — Bibliographic-first
**Status:** Done
**Creado:** 2026-05-23
**Implementado en:** salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md §Paso 1c + salida/edu-standalone/_edu/tasks/topic-extract-generation.md §paso-1c

---

## Descripción

**Como** topic-designer-v3, **quiero** buscar tendencias académicas recientes del tópico e identificar posibles conflictos con bibliografía de más de 5 años, **para** que el docente sepa si alguna sección de los libros podría estar desactualizada.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Búsqueda de tendencias recientes
- Busca tendencias académicas de los últimos 5 años del tópico.

### CA-2 — Detección de conflictos bibliográficos
- Identifica si hay conflicto entre tendencias actuales y la bibliografía del curso (>5 años).

### CA-3 — No bloqueante
- Si falla → `⚠️ ADVERTENCIA: No se pudo obtener tendencias académicas. Continuando sin datos de tendencias.` + `tendencias: []`

### CA-4 — Formato estándar
Cada tendencia incluye: `tendencia`, `relevancia`, `conflicto_con_bibliografía`, `nota`, `fuente_url`.
