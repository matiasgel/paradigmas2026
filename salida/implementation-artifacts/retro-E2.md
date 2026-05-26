# Retrospectiva Sprint 2 — E2: Bibliographic-first

**Sprint:** 2
**Epic:** E2 — Bibliographic-first
**Fecha:** 2026-05-23
**Stories completadas:** 2.1, 2.2, 2.3, 2.4, 2.5 (5/5)

---

## Qué salió bien

- **Schema formal completo:** `topic-extract-schema.yaml` captura el 100% del contrato de interfaz entre topic-designer-v3 y agentes downstream. Las 5 validaciones (V01-V05) cubren los requisitos de calidad bibliográfica.
- **Fail-fast pattern:** La regla de parar si `chroma-mcp` no responde evita que el pipeline produzca material sin grounding bibliográfico. Decisión correcta de diseño.
- **Task file unificado:** `topic-extract-generation.md` centraliza toda la lógica de los Pasos 1a/1b/1c en un solo lugar, facilitando el mantenimiento.
- **Integración brownfield preservada:** Ningún agente v2 fue modificado en este sprint.

## Decisiones de diseño notables

- **Chunk sizes diferenciados:** reference/tool=1500 chars, material=800 chars (texto denso de libros). Decisión basada en observación empírica de los PDFs.
- **Retry sin filtro de libro:** Si 0 resultados con filtro de libro → retry sin filtro. Permite descubrimiento cuando el libro no tiene ese tópico específico.

## Qué se mejoraría

- El campo `nivel_minimo` en `conceptos-clave` fue añadido en Sprint 4 (E4). Sería mejor haberlo incluido en el schema desde el inicio.
- La sección `tendencias` en el topic-extract.md es opcional pero su presencia en downstream agents es alta. Podría ser `required: false, strongly_recommended: true`.

## Deuda técnica

- Ninguna deuda crítica.
