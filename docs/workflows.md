# Referencia de workflows — EDU

El módulo EDU incluye **15 workflows** organizados en 3 categorías: Core, Feature y Utility.

---

## Core (4 workflows)

### `load-official-plan`

**Propósito:** Cargar el programa institucional y generar `plan-minimo.md`.
**Cuándo usarlo:** Inicio de año/cuatrimestre, antes de cualquier producción.
**Agente owner:** Elena (orquesta `plan-extractor`)
**Inputs:** PDF del programa oficial de la institución
**Outputs:**
- `plan-minimo.md` — lista de tópicos obligatorios (inmutable tras confirmación)
- `temas/` — carpeta con subdirectorios vacíos por tema
**Comando:** `/edu-load-official-plan programa.pdf`

---

### `topic-cycle`

**Propósito:** Producción completa de un tema: diseño → clase → TP → calidad → testing → cierre.
**Cuándo usarlo:** Cuando el plan está confirmado y querés avanzar un tema.
**Agente owner:** Elena (orquesta Marcos, Roberto, Valeria, loops de calidad, student-simulator)
**Inputs:** ID de tema, duración de clase
**Outputs:**
- `temas/{N}/diseno.md`
- `temas/{N}/minuta.md`
- `temas/{N}/filminas.md`
- `temas/{N}/tp.md`
- `temas/{N}/score-pedagogico.md`
- `temas/{N}/faq-anticipado.md`
- Git: branch `tema/NN-nombre` mergeada a main
**Comandos clave:** `/edu-design-topic {N}`, `/edu-create-class {N}`, `/edu-create-tp {N}`, `/edu-close-topic {N}`

---

### `quality-loops`

**Propósito:** Ejecutar los 3 loops de calidad + guardrail sobre el material de un tema.
**Cuándo usarlo:** Tras la producción inicial de un tema, antes del testing pedagógico.
**Agente owner:** Elena (orquesta writing-validator, writing-fixer, coherence-fixer, reference-validator, academic-guardrail)
**Inputs:** ID de tema
**Outputs:**
- Correcciones aplicadas con commits Git individuales y reversibles
- `temas/{N}/reporte-calidad.md`
**Comandos:** `/edu-validate-writing {N}`, `/edu-fix-writing-auto {N}`, `/edu-validate-coherence {N}`, `/edu-fix-coherence-auto {N}`, `/edu-validate-references {N}`, `/edu-validate-scope {N}`, `/edu-validate-density {N}`

---

### `close-course`

**Propósito:** Cierre formal del año académico con retrospectiva y traspaso de memoria.
**Cuándo usarlo:** Fin de cuatrimestre / fin de año.
**Agente owner:** Elena (orquesta `plan-coverage-checker`)
**Inputs:** Ninguno (trabaja con la memoria acumulada del año)
**Outputs:**
- `retrospectiva-{año}.md` — análisis del año
- `notas-para-{año+1}.md` — recomendaciones de mejora
- Git: tag de versión del cursado completo
**Comando:** `/edu-close-course`

---

## Feature (8 workflows)

### `build-course-from-materials`

**Propósito:** Construir el plan del cursado a partir de material docente existente (PDFs, PPTX, DOCX).
**Cuándo usarlo:** Tenés material del año anterior que querés reactivar.
**Agente owner:** Elena (orquesta `material-ingester`, Carlos, Marcos)
**Inputs:** Carpeta con archivos de material existente
**Outputs:** `plan-borrador.md` listo para revisión de Elena
**Comando:** `/edu-build-course-from-materials ./carpeta-material/`

---

### `build-course-from-research`

**Propósito:** Construir el plan del cursado desde investigación académica pura.
**Cuándo usarlo:** Tema nuevo, sin material previo.
**Agente owner:** Elena (orquesta Carlos para investigación)
**Inputs:** Lista de tópicos del `plan-minimo.md`
**Outputs:** `plan-borrador.md` + referencias académicas por tema
**Comando:** `/edu-research-plan`

---

### `pedagogical-testing`

**Propósito:** Simular la experiencia de un alumno con uno o varios perfiles empíricos.
**Cuándo usarlo:** Antes de cerrar un tema; cuando querés validación pedagógica.
**Agente owner:** Elena (orquesta `student-simulator`, `test-runner`)
**Inputs:** ID de tema, perfil/s de alumno
**Perfiles disponibles:** `estrategico`, `ansioso`, `disperso`, `recursero`, `all`
**Outputs:** `score-pedagogico.md`, `faq-anticipado.md`
**Comandos:** `/edu-test-topic {N} {perfil}`, `/edu-test-topic {N} all`

---

### `new-year`

**Propósito:** Arrancar el nuevo año académico reutilizando la memoria del año anterior.
**Cuándo usarlo:** Inicio de año, después de `/edu-close-course` del año anterior.
**Agente owner:** Elena
**Inputs:** `notas-para-{año}.md` (opcional), nuevo programa institucional (opcional)
**Outputs:** Workspace limpio con memoria del año anterior disponible para consulta
**Comando:** `/edu-start-new-year`

---

### `curriculum-change`

**Propósito:** Proponer y evaluar un cambio curricular justificado académicamente.
**Cuándo usarlo:** Querés agregar/quitar/modificar tópicos con sustento académico.
**Agente owner:** Ana (orquesta Carlos para fuentes)
**⚠️ Restricción:** Solo puede proponer cambios a `plan-borrador.md`. Nunca a `plan-minimo.md`.
**Outputs:** Propuesta de cambio con justificación académica y análisis de impacto
**Comando:** `/edu-propose-curriculum-change`

---

### `reopen-topic`

**Propósito:** Reabrir un tema cerrado para aplicar correcciones mayores.
**Cuándo usarlo:** Recibiste feedback de alumnos reales que requiere revisión del material.
**Agente owner:** Elena
**Inputs:** ID de tema
**Outputs:** Branch Git reactivada para el tema; estado del tema vuelve a "en revisión"
**Comando:** `/edu-reopen-topic {N}`

---

### `adaptive-replan`

**Propósito:** Replantear el cronograma del cursado cuando hay temas atrasados o desfasados.
**Cuándo usarlo:** Mediados de cuatrimestre con temas en riesgo de no cobertura.
**Agente owner:** Elena (consulta `plan-coverage-checker` en modo silencioso)
**Outputs:** Plan ajustado respetando `plan-minimo.md`; nunca propone reducir tópicos obligatorios
**Comando:** `/edu-adaptive-replan`

---

### `student-feedback-loop`

**Propósito:** Procesar resultados de encuestas reales de alumnos y calibrar el simulador.
**Cuándo usarlo:** Después de tomar una encuesta en clase o en el LMS.
**Agente owner:** `student-simulator`
**Inputs:** Resultados de encuesta (CSV o texto libre)
**Outputs:** Actualización de `calibracion-simulador/` (long-term); reporte comparativo
**Comando:** `/edu-compare-survey-simulator {N}`

---

## Utility (3 workflows)

### `manage-student-profiles`

**Propósito:** Agregar, editar o consultar los perfiles de alumno disponibles para el simulador.
**Cuándo usarlo:** Querés agregar un perfil nuevo basado en literatura; o ajustar un perfil existente.
**Agente owner:** `student-simulator`
**Outputs:** Actualización de perfiles en `calibracion-simulador/`
**Comandos:** `/edu-research-student-profiles`, `/edu-add-student-profile`

---

### `check-coverage`

**Propósito:** Reporte de cobertura del `plan-minimo.md` en el estado actual del cursado.
**Cuándo usarlo:** Cualquier momento para auditar el estado de cobertura.
**Agente owner:** `plan-coverage-checker`
**Outputs:** Reporte de cobertura con alertas y porcentaje por tópico obligatorio
**Comando:** `/edu-check-coverage`

---

### `update-copilot-context`

**Propósito:** Actualizar el contexto activo de Copilot para el workspace del módulo.
**Cuándo usarlo:** Después de cambios grandes en el plan o al retomar sesión después de días.
**Agente owner:** Elena
**Outputs:** Contexto actualizado disponible para todos los agentes en la sesión
**Comando:** `/edu-update-context`
