# Story 2.5 — Generación completa de topic-extract.md con validaciones

**ID:** S2.5
**Epic:** E2 — Bibliographic-first
**Status:** Done
**Creado:** 2026-05-23
**Implementado en:** salida/edu-standalone/_edu/tasks/topic-extract-generation.md

---

## Descripción

**Como** topic-designer-v3, **quiero** una tarea detallada de generación de `topic-extract.md` que consolide los resultados de Pasos 1a/1b/1c, aplique el esquema formal, ejecute validaciones y presente el artefacto listo para CP1.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Conformidad con schema
- El archivo generado cumple `topic-extract-schema.yaml`: 5 secciones, frontmatter correcto, tipos y restricciones.

### CA-2 — Validaciones automáticas
- V01: mínimo 1 fuente con página verificada
- V02: mínimo 3 conceptos-clave
- V03: páginas null marcadas con `⚠️`

### CA-3 — Formato de referencia estandarizado
- Citas en formato: `[Autor, Libro §Sección, p. N]`

### CA-4 — Artefacto listo para CP1
- Tras la generación, el agente presenta el Checkpoint 1 con el bloque visual estandarizado.
