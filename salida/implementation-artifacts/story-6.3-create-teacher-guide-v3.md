# Story 6.3 — Agregar sección condicional v3 a create-teacher-guide/workflow.md

**ID:** S6.3
**Epic:** E6 — Agentes downstream
**Status:** Done
**Archivos modificados:** salida/edu-standalone/_edu/workflows/create-teacher-guide/workflow.md (append aditivo)

---

## Descripción

**Como** workflow de guía docente, **quiero** incluir secciones adicionales cuando existe `topic-extract.md` aprobado, **para** que la guía del profesor refleje la profundidad bibliográfica y nivel de densidad del pipeline v3.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Activación condicional
- Modo v2 si topic-extract.md no existe. Modo v3 si existe y checkpoint_2_aprobado: true.

### CA-2 — Sección fundamentos bibliográficos
- Nueva sección 0.5 en guiaprofesor.md con fuentes de `## fuentes` (relevancia: alta).

### CA-3 — Sección variantes por nivel
- Nueva sección 2.5 con tabla N1/N2/N3 de conceptos según nivel de densidad.

### CA-4 — Sección tendencias académicas
- Nueva sección 7.5 con tendencias `relevancia: alta`, señalando conflictos con bibliografía.

### CA-5 — Backup
- Si guiaprofesor.md ya existe → crear guiaprofesor-v2-backup.md antes de sobrescribir.

### CA-6 — Implementación aditiva
- Workflow original sin modificaciones. Lógica v3 como sección Markdown al final.
