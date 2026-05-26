# Story 6.4 — Mecanismo de backup de artefactos v2

**ID:** S6.4
**Epic:** E6 — Agentes downstream
**Status:** Done
**Archivos creados:** salida/edu-standalone/_edu/tasks/backup-v2-artifacts.md

---

## Descripción

**Como** agente downstream en modo v3, **quiero** crear backups idempotentes de artefactos v2 antes de sobrescribir, **para** que el docente pueda restaurar el estado v2 si lo necesita.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Task file creado
- `tasks/backup-v2-artifacts.md` documenta el protocolo completo de backup para cada agente.

### CA-2 — Idempotencia
- Si el backup ya existe → NO volver a crearlo (protege la versión original v2).

### CA-3 — Tabla de mappings completa
- filminas.md → filminas-v2-backup.md
- minuta.md → minuta-v2-backup.md
- guia-estudio.md → guia-estudio-v2-backup.md
- guiaprofesor.md → guiaprofesor-v2-backup.md

### CA-4 — Protocolo de restauración
- El task file incluye comandos de restauración manual para revertir de v3 a v2.

### CA-5 — Implementación por referencia
- Cada agente downstream (6.1, 6.2, 6.3) ya tiene el backup protocol incluido en su sección v3.
- El task file centraliza la documentación sin duplicar lógica.
