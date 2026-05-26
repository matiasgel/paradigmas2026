# Story 6.1 — Agregar lógica condicional v3 a class-writer.md

**ID:** S6.1
**Epic:** E6 — Agentes downstream
**Status:** Done
**Creado:** 2026-05-23
**Archivos modificados:** salida/edu-standalone/_edu/agents/class-writer.md (append aditivo)

---

## Descripción

**Como** class-writer, **quiero** verificar si existe `topic-extract.md` en `{topic_folder}` con `checkpoint_2_aprobado: true`, **para** usar ese artefacto como fuente primaria de conceptos y ejemplos (v3) sin alterar el comportamiento v2 cuando no existe.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Activación condicional
- `topic-extract.md` NO existe → comportamiento v2 completo sin cambios.
- `topic-extract.md` SÍ existe Y `checkpoint_2_aprobado: true` → comportamiento v3.

### CA-2 — Fuente primaria v3
- En modo v3: usa `topic-extract.md` como fuente de conceptos, ejemplos y terminología. No re-consulta ChromaDB.

### CA-3 — Nivel de densidad
- Lee `nivel` de `.pipeline-v3-state.yaml` y aplica modificadores: N1 ≤3 conceptos/filmina, N2 ≤5, N3 todos los necesarios.

### CA-4 — Implementación aditiva
- El XML original de `class-writer.md` permanece sin modificaciones. La lógica v3 se agrega como sección Markdown aditiva al final del archivo.
