# Story 5.2 — Implementar análisis comparativo filminas previas vs topic-extract.md

**ID:** S5.2
**Epic:** E5 — Renovación de año anterior
**Status:** Done
**Archivos modificados/creados:**
- `_edu/tasks/renovacion-anio-anterior.md` (Pasos 1-3: lectura, análisis, reporte)
- `_edu/workflows/topic-cycle-v3/workflow.md` (Paso 2 actualizado con referencia al task file)

---

## Descripción

**Como** topic-designer-v3, **quiero** comparar las filminas previas contra el nuevo `topic-extract.md`, **para** categorizar cada filmina como conservar/actualizar/eliminar/nueva y presentar un reporte al docente.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Lectura de filminas previas
- Se lee el archivo especificado en `--base` y se extraen las filminas (por título/número).

### CA-2 — Categorización
- Cada filmina clasifica en: conservar | actualizar | eliminar | nueva.

### CA-3 — Criterios documentados
- Criterios de clasificación definidos en `tasks/renovacion-anio-anterior.md` Paso 2.

### CA-4 — Reporte al docente
- Formato estándar con tabla: número, título, acción, motivo. Emoji 🔄 en encabezado.

### CA-5 — Integración con superposiciones
- Concepto con `asumir-conocido` en superposiciones → filmina correspondiente se clasifica como `eliminar`.

### CA-6 — Integración con tendencias
- Bibliografía desactualizada + tendencia conflictiva → filmina se clasifica como `actualizar`.
