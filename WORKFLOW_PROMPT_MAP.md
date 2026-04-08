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
| `/edu-knowledge-search` | Buscar en la knowledge base ChromaDB (referencias académicas + herramientas) |

### Sprint 1 — Validadores Pasivos

| Prompt | Descripción |
|--------|-------------|
| `/edu-check-accessibility` | Validar accesibilidad WCAG: contraste, alt_text, tipografía → `accessibility-report.md` |
| `/edu-check-composition` | Auditar composición visual: densidad, márgenes, superposiciones → `composition-report.md` |

### Sprint 2 — Herramientas de Planificación Docente

| Prompt | Descripción |
|--------|-------------|
| `/edu-spaced-review` | Calendario de repasos distribuidos FSRS v4 → `repaso-calendario.md` + `slides-repaso.md` |
| `/edu-create-exam` | Blueprint de examen con distribución Bloom → `blueprint-parcial-N.json/.md` |

### Sprint 4 — Inteligencia Cognitiva

| Prompt | Descripción |
|--------|-------------|
| `/edu-check-cognition` | Validar reglas cognitivas (assertion-evidence, densidad, contiguidad) → `cognition-report.md` |
| `/edu-check-cognitive-load` | Presupuesto cognitivo por clase con curva visual → `cognitive-budget-report.md` |

### Sprint 3 — GitHub Classroom Integration

| Prompt | Descripción |
|--------|-------------|
| `/edu-publish-classroom` | Publicar TPs y materiales a GitHub Classroom con gh CLI |
| `/edu-classroom-grades` | Importar notas de GitHub Classroom al dashboard de analytics |
| `/edu-setup-auto-responder` | Configurar GitHub Action auto-responder para errores de Git de alumnos |

### Sprint 5 — Student Analytics + Adaptive Path

| Prompt | Descripción |
|--------|-------------|
| `/edu-student-analytics` | Dashboard de progreso: tendencias, alertas tempranas, distribución |
| `/edu-adaptive-path` | Rutas de aprendizaje personalizadas por nivel de rendimiento |

### Sprint 6 — Investigation + MCP Server

| Prompt | Descripción |
|--------|-------------|
| `/edu-compare-curriculum` | Comparar currícula contra estándares ACM/IEEE y universidades internacionales |

### Sprint 7 — Interactivity + Multimedia

| Prompt | Descripción |
|--------|-------------|
| `/edu-create-interactive` | Simulación interactiva HTML5: drag-drop, slider, code-trace, etc. |
| `/edu-create-annotations` | Secuencia de anotaciones tipo pizarra con pasos JSON |
| `/edu-generate-audio` | Narración TTS por filmina con edge-tts |
| `/edu-simulate-classroom` | Simulación pedagógica grupal con 4 arquetipos de Schwanke |

### Sprint 8 — Orchestration + PBL

| Prompt | Descripción |
|--------|-------------|
| `/edu-create-pbl` | Proyecto PBL multi-clase con milestones, rúbricas y anti-delegación |
| `/edu-pbl-status` | Estado de proyectos PBL activos por milestone |
| `/edu-auto-topic` | Producción automática de tema completo con Director Agent |
| `/edu-resume-topic` | Reanudar producción desde último checkpoint |

### Sprint 9 — Semantic Analyzers

| Prompt | Descripción |
|--------|-------------|
| `/edu-check-semantic-drift` | Detectar drift semántico entre contenido y fuentes originales |
| `/edu-check-curriculum-gaps` | Detectar gaps y redundancias temáticas en el cursado |
| `/edu-verify-facts` | NLI fact-checking: entailment/contradiction/neutral por claim |

### Sprint 10 — Psychometrics + Visual Quality

| Prompt | Descripción |
|--------|-------------|
| `/edu-classify-bloom` | Clasificar preguntas por nivel de Bloom con DeBERTa ML + fallback keyword |
| `/edu-calibrate-assessment` | Calibrar dificultad IRT 2PL + estimar mastery BKT |
| `/edu-check-visual-quality` | Evaluar relevancia visual CLIP + layout quality de slides |

### Sprint 11 — Knowledge Engineering

| Prompt | Descripción |
|--------|-------------|
| `/edu-build-kg` | Construir Knowledge Graph educativo desde plan mínimo |
| `/edu-validate-kg` | Validar KG: ciclos, huérfanos, monotonía de Bloom |
| `/edu-learn-prerequisites` | Inferir prerequisitos con ML + active learning |

### Sprint 12 — Full-Stack Orchestration

| Prompt | Descripción |
|--------|-------------|
| `/edu-run-pipeline` | Pipeline completo de producción con 9 pasos + checkpoints |
| `/edu-resume-pipeline` | Reanudar pipeline desde último checkpoint exitoso |
| `/edu-agent-director` | Director inteligente con smolagents + Qwen/Llama |

### Sprint 13 — Zero-Curriculum Adaptive Learning

| Prompt | Descripción |
|--------|-------------|
| `/edu-kst-explain` | Explicar concepto frontera KST al estudiante |
| `/edu-universal-kg` | Construir KG universal de CS desde ACM CC2023 + MIT OCW |
| `/edu-adaptive-session` | Sesión de aprendizaje adaptativo sin currícula fija |
