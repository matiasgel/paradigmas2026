# Story 3.3 — Capturar estrategia de superposición y propagarla al topic-extract.md

**ID:** S3.3
**Epic:** E3 — Coherencia curricular
**Status:** Done
**Archivos modificados/creados:**
- `_edu/tasks/coherencia-curricular.md` (Paso 4 — captura y mapeo de estrategias)
- `_edu/schemas/topic-extract-schema.yaml` (sección superposiciones-detectadas ya definida)
- `_edu/agents/class-writer.md` (sección v3 ya incluye uso de ## superposiciones-detectadas)

---

## Descripción

**Como** topic-designer-v3, **quiero** persistir las estrategias de solapamiento acordadas con el docente en `topic-extract.md ## superposiciones-detectadas`, **para** que class-writer y study-guide-writer las respeten al generar el material.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Persistencia en topic-extract.md
- Estrategias acordadas en Paso 0 se incluyen en `## superposiciones-detectadas` del topic-extract.md.

### CA-2 — Schema compatible
- La sección `superposiciones-detectadas` ya está definida en `topic-extract-schema.yaml` con los campos correctos.

### CA-3 — Mapeo de estrategia "desarrollar"
- La opción [D] del docente = NO incluir en superposiciones-detectadas (el concepto se trata normalmente).

### CA-4 — Verificación en CP1
- En CP1 el docente puede modificar estrategias antes de aprobar el topic-extract.md.

### CA-5 — Uso por class-writer
- La sección v3 de class-writer.md ya incluye instrucción de leer `## superposiciones-detectadas` y aplicar la estrategia correspondiente.

### CA-6 — Idempotencia
- Si el pipeline se reanuda en Paso 1a+ (el state ya tiene paso-0 completo), no re-ejecutar el escaneo de coherencia.
