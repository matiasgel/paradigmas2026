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
- **Agentes**: `_edu/agents/` (17 agentes — 7 persona + 5 calidad + 2 testing + 3 internos)
- **Workflows**: `_edu/workflows/` (15 workflows organizados por fase)
- **Comandos**: `_edu/module-help.csv` (28 comandos en 4 fases + anytime)
- **Memoria**: `_edu-memory/` (persistente entre sesiones)

## Fases del Cursado

| Fase | Nombre | Descripción |
|------|--------|-------------|
| 1 | Configuración Inicial | Cargar programa oficial, generar plan-minimo.md inmutable |
| 2 | Planificación | Construir plan-borrador.md (desde material o investigación) |
| 3 | Producción de Temas | Ciclo: diseño → clase → **guía de estudio** → TP → calidad → testing → cierre |
| 4 | Cierre | Retrospectiva, traspaso de memoria al año siguiente |

## Agentes Disponibles

### Capa 1 — Persona (visibles al docente)
| Agente | Persona | Rol |
|--------|---------|-----|
| course-planner | Prof. Elena 🎓 | Planificadora y orquestadora del cursado |
| topic-designer | Lic. Marcos 🗂️ | Diseñador de contenidos por tema |
| class-writer | Dr. Roberto ✍️ | Escritor de minutas y filminas |
| study-guide-writer | Dra. Sofía 📖 | Escritora de guías de estudio completas para alumnos |
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
5. **Schema Registry es OBLIGATORIO** — Todo agente que genere o modifique planes de filminas DEBE leer `_edu/schemas/schema-registry.json` ANTES de cualquier operación. Los tipos, layouts y reglas de imagen son INMUTABLES y se definen exclusivamente ahí.
6. **Planes de filminas en JSON v3** — Formato de salida: `plan-filminas-{tema}.json` siguiendo `_edu/schemas/plan-filminas.schema.json`. No usar YAML para planes nuevos.
7. **Scripts no tienen constantes de diseño** — `slides_pipeline.py`, `validate_plan.py`, `parse_filminas.py` leen mapeos del schema registry en runtime. No se agregan constantes de tipos/layouts en los scripts.
8. **Utilidades compartidas en `pipeline_common.py`** — Funciones reutilizables (`find_project_root`, `load_json`, `save_json`, `load_registry`, `find_plan`) y el tipo `Result[T]` (mónada funcional con `bind`/`map`/`|`) están centralizados ahí. Los scripts importan de `pipeline_common`, no duplican lógica.
9. **Memoria colectiva SQLite FTS5** — `_edu-memory/memory.db` almacena errores de agentes, correcciones del usuario, hallazgos de calidad, insights pedagógicos y retrospectivas. Cada entrada tiene `course_id` (ej: `leng-2026`), categoría y tema. Usar `python scripts/edu_memory.py search "query"` para buscar. Los agentes DEBEN consultar la memoria antes de generar contenido (`agent-error`, `agent-correction` para evitar errores repetidos) y escribir en ella al detectar errores o recibir correcciones.
10. **Multi-clase con `course_id`** — `config.yaml` define `course_prefix` (ej: `leng`) + `course_year` (ej: `2026`) → `course_id` = `leng-2026`. Todas las rutas (`course_output_folder`, `topics_folder`) usan `{course_id}`. Un workspace puede contener múltiples materias. Usar `/edu-switch-course` para cambiar de materia activa.
11. **Knowledge Base ChromaDB** — `_edu-knowledge/` contiene referencias académicas (10 documentos) y documentación de herramientas (16 documentos) ingestados en ChromaDB (383 chunks vectorizados). Todos los agentes DEBEN consultar la knowledge base antes de implementar funcionalidades de los sprints de mejoras. Usar `python scripts/knowledge_base.py search "query"` para buscar. Filtrar por tipo: `--type reference` (papers académicos) o `--type tool` (docs de herramientas). Documentos disponibles: Multimedia Learning (Fiorella/Mayer 2023), Cognitive Load Theory (Sweller/Chen 2023), WCAG 2.2/3.0 (W3C), FSRS v4 (Ye 2023), Bloom Taxonomy & Assessment (Haladyna 2024), Learning Analytics (Ifenthaler/Tsai/Yan 2020-2024), CS Education & GitHub (SIGCSE/Feliciano/Denny 2023-2024), Slide Composition (Duarte/Scheiter 2019-2023), Adaptive Learning & ITS (VanLehn/ALEKS/Du 2023), MCP Protocol (Anthropic 2024-2025). API importable: `from scripts.knowledge_base import query_knowledge; result = query_knowledge("cognitive load slides")`
<!-- EDU:END -->
