 EDU:START -->
# EDU — Academic Course Production Suite

## Descripción

Pipeline completo de producción docente universitaria con inteligencia pedagógica.
Desde la ingesta del programa oficial hasta el cierre de cursada con validación automática y memoria acumulada año a año.

## Configuración del Proyecto

- Cargar siempre `_edu/config.yaml` antes de cualquier activación de agente o ejecución de workflow
- Almacenar todos los campos como variables de sesión
- La variable `{project-root}` se resuelve a la raíz del workspace en runtime

## Estructura

- **Configuración**: `_edu/config.yaml`
- **Agentes**: `_edu/agents/` (16 agentes — 6 persona + 5 calidad + 2 testing + 3 internos)
- **Workflows**: `_edu/workflows/` (15 workflows organizados por fase)
- **Comandos**: `_edu/module-help.csv` (35 comandos en 4 fases + anytime)
- **Memoria**: `_edu-memory/` (persistente entre sesiones)

## Fases del Cursado

| Fase | Nombre | Descripción |
|------|--------|-------------|
| 1 | Configuración Inicial | Cargar programa oficial, generar plan-minimo.md inmutable |
| 2 | Planificación | Construir plan-borrador.md (desde material o investigación) |
| 3 | Producción de Temas | Ciclo: diseño → clase → TP → calidad → testing → cierre |
| 4 | Cierre | Retrospectiva, traspaso de memoria al año siguiente |

## Agentes Disponibles

### Capa 1 — Persona (visibles al docente)
| Agente | Persona | Rol |
|--------|---------|-----|
| course-planner | Prof. Elena 🎓 | Planificadora y orquestadora del cursado |
| topic-designer | Lic. Marcos 🗂️ | Diseñador de contenidos por tema |
| class-writer | Dr. Roberto ✍️ | Escritor de minutas y filminas |
| tp-designer | Aux. Valeria 📝 | Diseñadora de trabajos prácticos |
| curriculum-reviewer | Prof. Ana 🔍 | Revisora curricular con evidencia académica |
| academic-researcher | Bib. Carlos 📚 | Investigador bibliográfico |

### Capa 2 — Calidad (motores automáticos)
| Agente | Rol |
|--------|-----|
| writing-validator 🔎 | Detecta errores ortográficos, gramaticales y de estilo |
| writing-fixer ✏️ | Aplica correcciones automáticas con commits Git |
| coherence-fixer 🔗 | Unifica coherencia inter e intra documento |
| reference-validator 🔬 | Verifica referencias contra bases académicas |
| academic-guardrail 🛡️ | Control de formalidad, scope y densidad cognitiva |

### Capa 3 — Testing
| Agente | Rol |
|--------|-----|
| student-simulator 🎓 | Simula alumnos con perfiles empíricos |
| plan-coverage-checker 📊 | Verifica cobertura del plan mínimo |

### Capa 4 — Internos (no invocables directamente)
| Agente | Rol |
|--------|-----|
| material-ingester 📥 | Convierte PDFs/PPTX/DOCX a Markdown |
| plan-extractor 📋 | Extrae tópicos del programa institucional |
| test-runner 🧪 | Ejecuta baterías de simulación y genera scores |

## Slash Commands

Escribí `/edu-` en Copilot Chat para ver todos los comandos disponibles.
Los agentes están disponibles como `@edu-agent-nombre` en el dropdown de agentes.

## Restricciones Críticas

1. **plan-minimo.md es INMUTABLE** — Una vez confirmado, ningún agente puede modificarlo
2. **Loops de calidad son secuenciales** — Loop 1 (escritura) → Loop 2 (coherencia) → Loop 3 (referencias) → Guardrail
3. **La memoria del simulador NUNCA se resetea** — `_edu-memory/calibracion-simulador/` acumula año a año
4. **Fuentes prohibidas** — Wikipedia, blogs y fuentes no peer-reviewed son rechazadas automáticamente
<!-- EDU:END -->
