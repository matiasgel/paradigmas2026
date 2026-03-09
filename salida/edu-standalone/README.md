U — Academic Course Production Suite

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
4. Usá `/edu-start-course` para comenzar

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
