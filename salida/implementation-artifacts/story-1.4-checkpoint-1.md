# Story 1.4 — Implementar Checkpoint 1 — aprobación de topic-extract.md

**ID:** S1.4
**Epic:** E1 — Pipeline base v3
**Status:** Done
**Creado:** 2026-05-23
**Implementado en:** salida/edu-standalone/_edu/workflows/topic-cycle-v3/workflow.md §CHECKPOINT 1 + salida/edu-standalone/_edu/agents/topic-designer-v3.md §checkpoint cp1

---

## Descripción

**Como** docente, **quiero** que el pipeline se detenga después de generar `topic-extract.md` y espere mi aprobación, con posibilidad de editar el archivo directamente, **para** validar el grounding bibliográfico antes de generar cualquier material.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Bloque visual estandarizado
Al alcanzar CP1, muestra:
```
╔═══════════════════════════════════════════════════════════╗
║  CHECKPOINT 1 — Aprobación de topic-extract.md            ║
║  Revisá: [{topic_folder}/topic-extract.md]                ║
║  Verificá: fuentes, conceptos-clave, ejemplos.            ║
║  Podés editar el archivo directamente antes de responder. ║
║  Respondé "ok" para continuar, o indicá correcciones.    ║
╚═══════════════════════════════════════════════════════════╝
```

### CA-2 — Persistencia al aprobar
- Docente responde "ok" → `checkpoint_1_aprobado: true` en state file + continúa al Paso 2.

### CA-3 — Respeta edición manual
- Docente edita el archivo y responde "ok" → persiste `checkpoint_1_aprobado: true` sin revertir ediciones.

### CA-4 — Loop de correcciones
- Docente indica corrección → agente actualiza `topic-extract.md` y vuelve a presentar CP1 (no continúa sin aprobación explícita).
