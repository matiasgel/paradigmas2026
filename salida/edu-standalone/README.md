# EDU — Academic Course Production Suite

Pipeline completo de producción docente universitaria con inteligencia pedagógica.

## Quick Start

1. Cloná o copiá este directorio como raíz de tu proyecto
2. Abrí VS Code
3. Configurá tu materia editando `_edu/config.yaml`:
   - `project_name`: nombre de la materia
   - `institution`: tu institución
   - `user_name`: tu nombre
   - `default_professor_profile`: tu perfil docente
   - `default_class_duration`: duración en minutos
4. Escribí `/edu_start_course` en Copilot Chat para comenzar

## Estructura del Proyecto

```
tu-materia/
├── .github/
│   ├── copilot-instructions.md    ← Contexto para Copilot
│   ├── agents/                    ← Agentes (@edu-agent-nombre)
│   └── prompts/                   ← Slash commands (/edu_*)
├── .vscode/
│   └── settings.json              ← Habilita prompt files
├── _edu/
│   ├── config.yaml                ← Configuración del módulo
│   ├── module-help.csv            ← Índice de comandos
│   ├── secrets.local.yaml         ← API keys (en .gitignore)
│   ├── slides-config.yaml         ← Diseño visual (generado por Vera)
│   ├── agents/                    ← Definiciones completas de agentes
│   └── workflows/                 ← Definiciones de workflows
├── _edu-memory/                   ← Memoria persistente (creada en runtime)
├── temas/                         ← Contenido por tema (creado en runtime)
│   └── NN-nombre/
│       ├── diseno.md
│       ├── minuta.md
│       ├── filminas.md
│       ├── tp.md
│       └── slides/                ← Scripts y link de Google Slides
├── salida/                        ← Planes y reportes del cursado
└── material/                      ← Material docente existente (opcional)
```

## Agentes Disponibles

Usá `@` en Copilot Chat para invocar agentes directamente:

| Agente | Persona | Qué Hace |
|--------|---------|----------|
| `@edu-agent-course-planner` | Elena 🎓 | Orquesta todo el cursado |
| `@edu-agent-topic-designer` | Marcos 🗎️ | Diseña contenidos del tema |
| `@edu-agent-class-writer` | Roberto ✍️ | Escribe minutas y filminas |
| `@edu-agent-tp-designer` | Valeria 📝 | Diseña trabajos prácticos |
| `@edu-agent-slides-designer` | Vera 🎨 | Define el diseño visual del cursado |
| `@edu-agent-slides-publisher` | Diego 🚀 | Exporta filminas a Google Slides |
| `@edu-agent-curriculum-reviewer` | Ana 🔍 | Revisa cambios curriculares |
| `@edu-agent-academic-researcher` | Carlos 📚 | Investiga bibliografía |
| `@edu-agent-student-simulator` | Simulador 🎓 | Simula alumnos por perfil |
| `@edu-agent-plan-coverage-checker` | Verificador 📊 | Chequea cobertura del plan |
| `@edu-agent-writing-validator` | Validador 🔎 | Detecta errores de escritura |
| `@edu-agent-coherence-fixer` | Coherencia 🔗 | Unifica coherencia entre docs |
| `@edu-agent-reference-validator` | Referencias 🔬 | Valida citas académicas |
| `@edu-agent-academic-guardrail` | Guardrail 🛡️ | Controla formalidad y densidad |

## Slash Commands (27)

Escribí `/edu_` en Copilot Chat para ver todos los comandos disponibles.

### En cualquier momento
| Comando | Qué hace |
|---------|----------|
| `/edu_help` | Estado del cursado y próximo paso recomendado |
| `/edu_status` | Estado de producción de un tema específico |
| `/edu_check_coverage` | Cobertura del plan mínimo |
| `/edu_manage_profiles` | Gestionar perfiles de alumno del simulador |
| `/edu_update_context` | Refrescar contexto de Copilot al retomar sesión |

### Fase 1 — Configuración
| Comando | Qué hace |
|---------|----------|
| `/edu_start_course` | **Único comando de Fase 1** — configura materia, carga programa institucional y congela plan mínimo |

### Fase 2 — Planificación
| Comando | Qué hace |
|---------|----------|
| `/edu_build_course_from_materials` | Armar cursado desde material existente (PDFs, PPTX) |
| `/edu_research_plan` | Armar cursado desde investigación académica |
| `/edu_propose_curriculum_change` | Proponer cambio curricular con justificación |

### Fase 3 — Producción de Temas
| Comando | Qué hace |
|---------|----------|
| `/edu_topic` | ⭐ **Guía inteligente** — detecta el estado del tema activo y recomienda el próximo paso |
| `/edu_design_topic` | Diseñar o ajustar el tema (antes de aprobar) |
| `/edu_approve_design` | Aprobar el diseño — habilita la creación de clase |
| `/edu_create_class` | Generar minuta.md y filminas.md |
| `/edu_create_tp` | Generar trabajo práctico trazable a la minuta |
| `/edu_quality_validate` | Validar calidad: escritura + coherencia + referencias + scope |
| `/edu_quality_fix` | Corregir calidad: aplica fixes con commits Git reversibles |
| `/edu_test_topic` | Testing pedagógico — simula experiencia de alumnos por perfil |
| `/edu_debate_topic` | Panel multi-agente para decisiones complejas de diseño |
| `/edu_compare_survey_simulator` | Calibrar simulador con encuestas reales de alumnos |
| `/edu_close_topic` | Cerrar tema — commit + merge Git |
| `/edu_reopen_topic` | Reabrir tema cerrado para correcciones |
| `/edu_adaptive_replan` | Replanificar cronograma respetando plan mínimo |

### Publicación en Google Slides
| Comando | Cuándo usarlo |
|---------|---------------|
| `/edu_setup_apis` | **Una vez** — configura Google OAuth + Gemini key |
| `/edu_slides_designer` | **Una vez por cursada** — Vera define diseño visual |
| `/edu_publish_slides` | **En cada tema** — flujo completo: valida + genera + link |
| `/edu_slides_publisher` | Re-exportar sin rediseñar (Diego solo) |

### Fase 4 — Cierre
| Comando | Qué hace |
|---------|----------|
| `/edu_close_course` | Cierre formal del año: retrospectiva y traspaso de memoria |
| `/edu_start_new_year` | Iniciar nuevo año con workspace limpio y memoria del anterior |

## Flujo típico de un tema

```
/edu_start_course          ← Solo una vez al iniciar el cursado

/edu_topic                 ← Punto de entrada recomendado para cada tema
  └→ /edu_design_topic
  └→ /edu_approve_design
  └→ /edu_create_class
  └→ /edu_create_tp
  └→ /edu_quality_validate
  └→ /edu_quality_fix
  └→ /edu_test_topic
  └→ /edu_close_topic
  └→ /edu_publish_slides    ← Opcional: genera presentación en Google Slides
```

## Perfiles Docentes

| Perfil | Palabras/slide | Conceptos/clase | Min/slide |
|--------|---------------|-----------------|----------|
| profesor-teorico | ≤50 | ≤5 | 4-5 |
| profesor-practico | ≤30 | ≤3 | 2-3 |
| profesor-socratico | ≤35 | ≤4 | 3-4 |
| profesor-flipped | ≤35 | ≤4 | 3-4 |
| profesor-investigador | ≤45 | ≤5 | 4-5 |

## Licencia

MIT


## Estructura del Proyecto

```
tu-materia/
├── .github/
│   ├── copilot-instructions.md    ← Contexto para Copilot
│   ├── agents/                    ← Agentes (@edu-agent-nombre)
│   └── prompts/                   ← Slash commands (/edu-*)
├── .vscode/
│   └── settings.json              ← Habilita prompt files
├── _edu/
│   ├── config.yaml                ← Configuración del módulo
│   ├── module-help.csv            ← Índice de comandos
│   ├── agents/                    ← Definiciones completas de agentes
│   └── workflows/                 ← Definiciones de workflows
├── _edu-memory/                   ← Memoria persistente (creada en runtime)
├── salida/                        ← Output generado (creado en runtime)
│   └── cursadas/
│       └── temas/
└── material/                      ← Material docente existente (opcional)
```

## Agentes Disponibles

En Copilot Chat, usá `@` para invocar agentes:

| Agente | Quién Sos | Qué Hace |
|--------|-----------|----------|
| `@edu-agent-course-planner` | Prof. Elena 🎓 | Orquesta todo el cursado |
| `@edu-agent-topic-designer` | Lic. Marcos 🗂️ | Diseña contenidos del tema |
| `@edu-agent-class-writer` | Dr. Roberto ✍️ | Escribe minutas y filminas |
| `@edu-agent-tp-designer` | Aux. Valeria 📝 | Diseña trabajos prácticos |
| `@edu-agent-curriculum-reviewer` | Prof. Ana 🔍 | Revisa cambios curriculares |
| `@edu-agent-academic-researcher` | Bib. Carlos 📚 | Investiga bibliografía |
| `@edu-agent-student-simulator` | Simulador 🎓 | Simula alumnos por perfil |
| `@edu-agent-plan-coverage-checker` | Verificador 📊 | Chequea cobertura del plan |
| `@edu-agent-writing-validator` | Validador 🔎 | Detecta errores de escritura |
| `@edu-agent-writing-fixer` | Corrector ✏️ | Corrige escritura automáticamente |
| `@edu-agent-coherence-fixer` | Coherencia 🔗 | Unifica coherencia entre docs |
| `@edu-agent-reference-validator` | Referencias 🔬 | Valida citas académicas |
| `@edu-agent-academic-guardrail` | Guardrail 🛡️ | Controla formalidad y densidad |

## Slash Commands

Escribí `/edu-` para ver los 36 comandos organizados por fase:

### Anytime
- `/edu-help` — Estado y próximo paso recomendado
- `/edu-status` — Estado de producción de un tema
- `/edu-check-coverage` — Cobertura del plan mínimo
- `/edu-manage-profiles` — Gestionar perfiles de alumno
- `/edu-update-context` — Refrescar contexto de Copilot
- `/edu-research-student-profiles` — Investigar perfiles en literatura

### Fase 1 — Configuración
- `/edu-start-course` — Configurar la materia
- `/edu-load-official-plan` — Cargar programa institucional
- `/edu-confirm-official-plan` — Congelar plan mínimo

### Fase 2 — Planificación
- `/edu-build-course-from-materials` — Armar cursado desde material existente
- `/edu-research-plan` — Armar cursado desde investigación
- `/edu-propose-curriculum-change` — Proponer cambio curricular

### Fase 3 — Producción
- `/edu-design-topic` — Diseñar tema
- `/edu-adjust-design` — Ajustar diseño
- `/edu-approve-design` — Aprobar diseño
- `/edu-create-class` — Crear clase (minuta + filminas)
- `/edu-create-tp` — Crear trabajo práctico
- `/edu-validate-writing` — Validar escritura
- `/edu-fix-writing-auto` — Corregir escritura automáticamente
- `/edu-apply-writing-fixes` — Aplicar correcciones selectivas
- `/edu-validate-coherence` — Validar coherencia
- `/edu-fix-coherence-auto` — Corregir coherencia automáticamente
- `/edu-validate-references` — Validar referencias
- `/edu-fix-reference` — Corregir referencia específica
- `/edu-suggest-alternative` — Sugerir referencia alternativa
- `/edu-validate-scope` — Validar scope y formalidad
- `/edu-validate-density` — Validar densidad cognitiva
- `/edu-fix-guardrail-auto` — Corregir guardrail automáticamente
- `/edu-test-topic` — Testing pedagógico
- `/edu-compare-survey-simulator` — Calibrar simulador con encuestas
- `/edu-debate-topic` — Panel multi-agente para decisiones complejas de tema
- `/edu-close-topic` — Cerrar tema
- `/edu-reopen-topic` — Reabrir tema
- `/edu-adaptive-replan` — Replanificar cronograma

### Fase 4 — Cierre
- `/edu-close-course` — Cerrar cursado
- `/edu-start-new-year` — Iniciar nuevo año

## Perfiles Docentes

| Perfil | Palabras/slide | Conceptos/clase | Min/slide |
|--------|---------------|-----------------|-----------|
| profesor-teorico | ≤50 | ≤5 | 4-5 |
| profesor-practico | ≤30 | ≤3 | 2-3 |
| profesor-socratico | ≤35 | ≤4 | 3-4 |
| profesor-flipped | ≤35 | ≤4 | 3-4 |
| profesor-investigador | ≤45 | ≤5 | 4-5 |

## Licencia

Generado por EDU Module v1.0.0
