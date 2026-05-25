# Story 6.2 — Agregar lógica condicional v3 a study-guide-writer.md

**ID:** S6.2
**Epic:** E6 — Agentes downstream
**Status:** Done
**Archivos modificados:** salida/edu-standalone/_edu/agents/study-guide-writer.md (append aditivo)

---

## Descripción

**Como** study-guide-writer, **quiero** verificar si existe `topic-extract.md` con `checkpoint_2_aprobado: true`, **para** usar ese artefacto como fuente bibliográfica primaria en la guía de estudio.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Activación condicional
- Modo v2 si topic-extract.md no existe. Modo v3 si existe y está aprobado.

### CA-2 — Bibliografía desde topic-extract.md
- Citas en formato `[Autor, Libro §Sección, p. N]` tomadas de `## fuentes`.

### CA-3 — Nivel de densidad
- N1: guía concisa (5 preguntas autoevaluación), N2: estándar (8), N3: exhaustiva (10+).

### CA-4 — Backup
- Si guia-estudio.md ya existe → crear guia-estudio-v2-backup.md antes de sobrescribir.

### CA-5 — Implementación aditiva
- XML original de study-guide-writer.md sin modificaciones. Lógica v3 como sección Markdown al final.
