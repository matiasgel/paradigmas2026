# Story 3.2 — Implementar reporte de coherencia curricular con formato estándar

**ID:** S3.2
**Epic:** E3 — Coherencia curricular
**Status:** Done
**Archivos modificados/creados:**
- `_edu/tasks/coherencia-curricular.md` (Paso 3 del task file define el formato del reporte)

---

## Descripción

**Como** docente, **quiero** recibir un reporte estándar de solapamientos detectados, **para** decidir la estrategia de tratamiento de cada concepto antes de que comience la extracción bibliográfica.

---

## Criterios de Aceptación — TODOS CUMPLIDOS

### CA-1 — Formato de tabla
- Reporte presenta tabla: Concepto | Tema previo | Nivel solapamiento.

### CA-2 — Opciones de estrategia
- Docente puede elegir: [A] asumir-conocido, [R] resumir, [D] desarrollar para cada concepto.

### CA-3 — Default por nivel
- Alto → asumir-conocido por defecto. Medio → resumir. Bajo → asumir-conocido.

### CA-4 — Solo cuando hay solapamientos
- Si no se detectan solapamientos → no se muestra el reporte (UX limpia).

### CA-5 — Formato del reporte
- Encabezado estándar con emoji 📚, tabla de solapamientos, prompt de estrategias con defaults explícitos.

### CA-6 — Captura interactiva de estrategias
- El agente espera respuesta del docente para cada estrategia o acepta Enter para aplicar defaults.
