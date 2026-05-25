# Story 3.1 — Implementar Paso 0 — escaneo del registro de temas dados

**ID:** S3.1
**Epic:** E3 — Coherencia curricular
**Status:** Done
**Archivos modificados/creados:**
- `_edu/workflows/topic-cycle-v3/workflow.md` (aditivo — agrega ítem 6 al Paso 0)
- `_edu/tasks/coherencia-curricular.md` (NEW — algoritmo completo de escaneo)

---

## Descripción

**Como** topic-designer-v3, **quiero** escanear los temas previos del curso en Paso 0, **para** detectar solapamiento de conceptos antes de iniciar la extracción bibliográfica.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Escaneo de topics_folder
- En Paso 0 ítem 6, se escanean carpetas hermanas en `{topics_folder}/` que tengan `topic-extract.md` aprobado.

### CA-2 — Solo temas aprobados
- Solo se consideran temas con `aprobado_en` no nulo. Temas v2 (sin topic-extract.md) se ignoran silenciosamente.

### CA-3 — Comparación de conceptos
- El algoritmo de comparación (fuzzy/exact match) está documentado en `tasks/coherencia-curricular.md`.

### CA-4 — Clasificación de nivel
- Solapamientos clasificados como alto/medio/bajo según nivel_bloom en ambos temas.

### CA-5 — Contexto de sesión
- Lista `{superposiciones_previas}` guardada en contexto para uso en Paso 1c y CP1.

### CA-6 — Primer tema del curso
- Si no hay temas previos aprobados → omitir reporte silenciosamente y continuar.
