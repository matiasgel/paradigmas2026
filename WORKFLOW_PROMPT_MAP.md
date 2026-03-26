# Mapa de Workflows y Prompts (EDU)

Este documento mapea los workflows del módulo EDU con los prompts `/edu-*` que los invocan.

> **Actualizado:** 2026-03-25 · Arquitectura v3 (JSON Schema-driven)

## Flujo principal del docente

```
/edu-start-course → /edu-design-topic → /edu-create-class → /edu-create-study-guide
→ /edu-create-tp → /edu-quality → /edu-test-topic → /edu-close-topic
→ /edu-publish-slides (opcional, en cualquier momento post-clase)
```

## Mapa completo

### Fase 1 — Configuración Inicial

| Prompt | Workflow | Agente | Descripción |
|--------|----------|--------|-------------|
| `/edu-start-course` | `load-official-plan/` | Elena 🎓 | Configura materia + carga programa oficial + congela plan mínimo |
| `/edu-build-course` | `build-course-from-materials/` o `build-course-from-research/` | Elena 🎓 | Construye plan-borrador desde PDFs o investigación |
| `/edu-setup-apis` | — | — | Configura credenciales Google + Gemini en `secrets.local.yaml` |

### Fase 2 — Planificación

| Prompt | Workflow | Agente | Descripción |
|--------|----------|--------|-------------|
| `/edu-check-coverage` | `check-coverage/` | Elena 🎓 | Matriz de cobertura del plan mínimo |
| `/edu-adaptive-replan` | `adaptive-replan/` | Elena 🎓 | Ajustar cronograma post-clase |
| `/edu-propose-curriculum-change` | `curriculum-change/` | Ana 🔍 | Proponer cambio curricular con evidencia |

### Fase 3 — Producción de Temas

| Prompt | Workflow | Agente | Descripción |
|--------|----------|--------|-------------|
| `/edu-topic` | `topic-cycle/` | Marcos 🗂️ | Detecta estado del tema activo, guía próximo paso |
| `/edu-design-topic` | `topic-cycle/` (Step 1) | Marcos 🗂️ | Diseñar tema con duración como constraint → `diseno.md` |
| `/edu-approve-design` | `topic-cycle/` (Step 3) | Elena 🎓 | Aprobar el diseño del tema |
| `/edu-create-class` | `topic-cycle/` (Step 4) | Roberto ✍️ | Generar `minuta.md` + `filminas.md` |
| `/edu-create-study-guide` | `topic-cycle/` (Step 4.5) | Sofía 📖 | Guía de estudio autónoma para alumnos |
| `/edu-create-teacher-guide` | `create-teacher-guide/` | Roberto ✍️ | Guía del profesor autocontenida |
| `/edu-create-tp` | `topic-cycle/` (Step 5) | Valeria 📝 | TP trazable (desarrollo/repo/quiz/mixto) |
| `/edu-validate-gift` | `create-tp-quiz/` | Valeria 📝 | Validar archivo GIFT para Moodle |
| `/edu-create-autograde-repo` | `create-autograde-repo/` | Rodrigo | Repo con GitHub Actions autograding |
| `/edu-quality` | `quality-loops/` | Validadores 🔎 | Loops de calidad: escritura → coherencia → referencias → guardrail |
| `/edu-test-topic` | `pedagogical-testing/` | Simulador 🎓 | Testing pedagógico con perfiles de alumno |
| `/edu-close-topic` | `topic-cycle/` (Step 8) | Elena 🎓 | Cerrar tema: commit + merge + cobertura |

### Pipeline de Filminas (v3 — Schema-Driven)

| Prompt | Workflow | Agente/Script | Descripción |
|--------|----------|---------------|-------------|
| `/edu-slides-designer` | — | Vera 🎨 | Define sistema de diseño visual → `slides-config.yaml` (una vez por cursada) |
| `/edu-publish-slides` | `topic-cycle/` (Step 9.5) | Diego 🚀 + scripts | Plan JSON determinista + Gemini + Google Slides |
| `/edu-slides-publisher` | → redirige a `/edu-publish-slides` | — | Alias unificado |
| `/edu-test-pipeline` | — | `scripts/test_pipeline.py` | Test de integración end-to-end del pipeline |

### Fase 4 — Cierre y Continuidad

| Prompt | Workflow | Agente | Descripción |
|--------|----------|--------|-------------|
| `/edu-close-course` | `close-course/` | Elena 🎓 | Retrospectiva y traspaso de memoria |
| `/edu-start-new-year` | `new-year/` | Elena 🎓 | Reutilizar memoria del año anterior |
| `/edu-student-profiles` | `manage-student-profiles/` | Simulador 🎓 | Gestionar perfiles empíricos de alumnos |
| `/edu-debate-topic` | `debate-topic/` | Panel multi-agente | Debate para decisiones complejas |
| `/edu-reopen-topic` | `reopen-topic/` | Elena 🎓 | Reabrir tema cerrado |

### Utilidades

| Prompt | Descripción |
|--------|-------------|
| `/edu-help` | Orientación contextual sobre comandos EDU |
| `/edu-status` | Estado de producción del tema activo |
| `/edu-export-pdf` | Exportar guía de estudio a PDF |
| `/edu-edit-class-template` | Editar template canónico de clases |
| `/edu-update-context` | Actualizar `copilot-instructions.md` con estado actual |
| `/edu-compare-survey-simulator` | Comparar encuesta real vs simulación |
| `/edu-switch-course` | Cambiar materia activa (multi-clase) |
| `/edu-memory-search` | Buscar en la memoria colectiva (SQLite FTS5) |
