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
4. Escribí `/edu-start-course` en Copilot Chat para comenzar

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
│   ├── tasks/                     ← Tasks internas
│   └── workflows/                 ← Definiciones de workflows
├── _edu-memory/                   ← Memoria persistente (creada en runtime)
├── salida/
│   └── cursadas/                  ← Output del cursado (creado en runtime)
│       ├── plan-minimo.md
│       ├── plan-borrador.md
│       └── temas/
│           └── NN-nombre/
│               ├── diseno.md
│               ├── minuta.md
│               ├── filminas.md
│               ├── tp.md
│               └── slides/        ← Scripts y link de Google Slides
└── material/                      ← Material docente existente (opcional)
```

## Agentes Disponibles

Usá `@` en Copilot Chat para invocar agentes directamente:

| Agente | Persona | Qué Hace |
|--------|---------|----------|
| `@edu-agent-course-planner` | Elena 🎓 | Orquesta todo el cursado |
| `@edu-agent-topic-designer` | Marcos �️ | Diseña contenidos del tema |
| `@edu-agent-class-writer` | Roberto ✍️ | Escribe minutas y filminas |
| `@edu-agent-tp-designer` | Valeria 📝 | Diseña trabajos prácticos |
| `@edu-agent-curriculum-reviewer` | Ana 🔍 | Revisa cambios curriculares |
| `@edu-agent-academic-researcher` | Carlos 📚 | Investiga bibliografía |
| `@edu-agent-student-simulator` | Simulador 🎓 | Simula alumnos por perfil |
| `@edu-agent-classroom-designer` | Rodrigo 🎓 | Regenera outputs de TP (autograde, quiz) |
| `@edu-agent-plan-coverage-checker` | Verificador 📊 | Chequea cobertura del plan |
| `@edu-agent-writing-validator` | Validador 🔎 | Detecta errores de escritura |
| `@edu-agent-writing-fixer` | Corrector ✏️ | Corrige escritura automáticamente |
| `@edu-agent-coherence-fixer` | Coherencia 🔗 | Unifica coherencia entre docs |
| `@edu-agent-reference-validator` | Referencias 🔬 | Valida citas académicas |
| `@edu-agent-academic-guardrail` | Guardrail 🛡️ | Controla formalidad y densidad |

## Slash Commands (28)

Escribí `/edu-` en Copilot Chat para ver todos los comandos disponibles.

### En cualquier momento
| Comando | Qué hace |
|---------|----------|
| `/edu-help` | Estado del cursado y próximo paso recomendado |
| `/edu-status` | Estado de producción de un tema específico |
| `/edu-check-coverage` | Cobertura del plan mínimo |
| `/edu-student-profiles` | Gestionar perfiles de alumno del simulador |
| `/edu-update-context` | Refrescar contexto de Copilot al retomar sesión |
| `/edu-edit-class-template` | Personalizar la estructura de minutas y filminas |

### Fase 1 — Configuración
| Comando | Qué hace |
|---------|----------|
| `/edu-start-course` | **Único comando de Fase 1** — configura materia, carga programa institucional y congela plan mínimo |

### Fase 2 — Planificación
| Comando | Qué hace |
|---------|----------|
| `/edu-build-course` | Armar cursado — desde material existente (PDFs, PPTX) o desde investigación académica |
| `/edu-propose-curriculum-change` | Proponer cambio curricular con justificación |

### Fase 3 — Producción de Temas
| Comando | Qué hace |
|---------|----------|
| `/edu-topic` | ⭐ **Guía inteligente** — detecta el estado del tema activo y recomienda el próximo paso |
| `/edu-design-topic` | Diseñar o ajustar el tema (antes de aprobar) |
| `/edu-approve-design` | Aprobar el diseño — habilita la creación de clase |
| `/edu-create-class` | Generar minuta.md y filminas.md |
| `/edu-create-tp` | Generar trabajo práctico trazable a la minuta |
| `/edu-create-autograde-repo` | Regenerar output de TP (autograde-repo, quiz) |
| `/edu-quality` | Calidad unificada — valida y/o corrige escritura, coherencia, referencias y scope |
| `/edu-test-topic` | Testing pedagógico — simula experiencia de alumnos por perfil |
| `/edu-debate-topic` | Panel multi-agente para decisiones complejas de diseño |
| `/edu-compare-survey-simulator` | Calibrar simulador con encuestas reales de alumnos |
| `/edu-adaptive-replan` | Replanificar cronograma respetando plan mínimo |
| `/edu-close-topic` | Cerrar tema — commit + merge Git |
| `/edu-reopen-topic` | Reabrir tema cerrado para correcciones |

### Publicación en Google Slides
| Comando | Cuándo usarlo |
|---------|---------------|
| `/edu-setup-apis` | **Una vez** — configura Google OAuth + Gemini key |
| `/edu-slides-designer` | **Una vez por cursada** — define diseño visual del cursado |
| `/edu-publish-slides` | **En cada tema** — flujo completo: valida + genera + link |
| `/edu-slides-publisher` | Re-exportar sin rediseñar |

### Fase 4 — Cierre
| Comando | Qué hace |
|---------|----------|
| `/edu-close-course` | Cierre formal del año: retrospectiva y traspaso de memoria |
| `/edu-start-new-year` | Iniciar nuevo año con workspace limpio y memoria del anterior |

## Flujo típico de un tema

```
/edu-start-course          ← Solo una vez al iniciar el cursado

/edu-topic                 ← Punto de entrada recomendado para cada tema
  └→ /edu-design-topic
  └→ /edu-approve-design
  └→ /edu-create-class
  └→ /edu-create-tp
  └→ /edu-create-autograde-repo  ← Solo si el TP tiene autograde o quiz
  └→ /edu-quality
  └→ /edu-test-topic
  └→ /edu-adaptive-replan   ← Opcional: ajustar cronograma si hubo desvíos
  └→ /edu-close-topic
  └→ /edu-publish-slides    ← Opcional: genera presentación en Google Slides
```

## Perfiles Docentes

| Perfil | Palabras/slide | Conceptos/clase | Min/slide |
|--------|---------------|-----------------|-----------|
| profesor-teorico | ≤50 | ≤5 | 4-5 |
| profesor-practico | ≤30 | ≤3 | 2-3 |
| profesor-socratico | ≤35 | ≤4 | 3-4 |
| profesor-flipped | ≤35 | ≤4 | 3-4 |
| profesor-investigador | ≤45 | ≤5 | 4-5 |

## Licencia

MIT
