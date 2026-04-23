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
11. **Knowledge Base ChromaDB** — `_edu-knowledge/` contiene referencias académicas (12 documentos) y documentación de herramientas (16 documentos + 6 fuentes OpenMAIC) ingestados en ChromaDB (414 chunks vectorizados). Todos los agentes DEBEN consultar la knowledge base antes de implementar funcionalidades de los sprints de mejoras. Usar `python scripts/knowledge_base.py search "query"` para buscar. Filtrar por tipo: `--type reference` (papers académicos) o `--type tool` (docs de herramientas). Documentos disponibles: Multimedia Learning (Fiorella/Mayer 2023), Cognitive Load Theory (Sweller/Chen 2023), WCAG 2.2/3.0 (W3C), FSRS v4 (Ye 2023), Bloom Taxonomy & Assessment (Haladyna 2024), Learning Analytics (Ifenthaler/Tsai/Yan 2020-2024), CS Education & GitHub (SIGCSE/Feliciano/Denny 2023-2024), Slide Composition (Duarte/Scheiter 2019-2023), Adaptive Learning & ITS (VanLehn/ALEKS/Du 2023), MCP Protocol (Anthropic 2024-2025), MAIC (Yu et al. 2024, Tsinghua), OpenMAIC Platform (THU-MAIC 2026). API importable: `from scripts.knowledge_base import query_knowledge; result = query_knowledge("cognitive load slides")`

12. **Scripts son INMUTABLES para agentes** — Los archivos en `scripts/` (todos los `.py` y `requirements.txt`) son de SOLO LECTURA para todos los agentes EDU. Los agentes pueden LEER y EJECUTAR scripts, pero NUNCA crear, editar, renombrar ni borrar archivos en `scripts/`. Si un script necesita una corrección o nueva funcionalidad → el docente lo escala al Arquitecto. Esta regla aplica también a `scripts/` en `production/scripts/`. Los scripts son el contrato técnico del pipeline — modificarlos sin control de versiones rompe la reproducibilidad.

13. **Schemas son INMUTABLES para agentes** — Los archivos en `_edu/schemas/` (todos los `.json`, incluyendo `schema-registry.json`) son INMUTABLES para todos los agentes EDU. Los agentes leen schemas para validar, pero NUNCA los modifican. Si un tipo de filmina nuevo es necesario o un campo debe cambiar → escalar al Arquitecto con bump de versión mayor (`schema-registry.json` → `"version": "4.0.0"`). Cualquier agente que detecte inconsistencia en un schema debe reportarla al docente sin tocar el archivo.

14. **Templates son INMUTABLES para agentes** — Los archivos en `_edu/templates/` (`class-template.md`, `filminas-schema.yaml`, `filminas-template.md`, `prompt-imagen-guide.md`, etc.) no pueden ser modificados por agentes. Se usan como referencia de lectura. Si el docente quiere actualizar un template → edición directa por el docente, no por agente.

15. **refresh_plan.py — Uso obligatorio al re-publicar** — Si `filminas.md` fue modificado DESPUÉS de que `slides_pipeline.py` ya generó imágenes y subió assets a Google Drive, se DEBE usar `python scripts/refresh_plan.py {topic_folder}` en lugar de regenerar el plan desde cero. Este script preserva `image.local_asset`, `image.drive_id`, `image.prompt`, `layout` y `type` de las filminas existentes, evitando regenerar imágenes Gemini costosas. Solo re-parsea el contenido textual nuevo.

16. **generate_gift_quiz.py — Cuestionarios Moodle GIFT** — Para generar cuestionarios importables en Moodle desde el plan de filminas de un tema: `python scripts/generate_gift_quiz.py --topic {nombre} --course {course_id}`. Genera un archivo `.gift` y un manifiesto `.json` en `{topic_folder}/slides/`. Compatible con Moodle 5. Si existe `exam-blueprint.json` en la carpeta del tema, lo usa para asignar niveles Bloom a cada pregunta.

17. **publish_loop.py — Loop de publicación OBLIGATORIO** — Para publicar filminas en Google Slides, el agente `slides-publisher` (Diego) DEBE usar `python scripts/publish_loop.py {topic_folder} --course {course_id}`. **NUNCA llamar `slides_pipeline.py` directamente.** El loop ejecuta automáticamente: reparar schema (hasta 3 intentos) → validar coherencia (WCAG, reglas cognitivas, composición, facts, drift semántico) → publicar en Slides → thumbnails → `publish-report.json` → `memory.db`. Opciones: `--dry-run` (validar sin publicar), `--skip-phase2` (solo schema+publicar), `--skip-facts` (omitir NLI), `--max-attempts N`. Exit 3 = coherencia bloqueada (revisar `publish-report.json`).

18. **error_registry.py — Registro de errores OBLIGATORIO (lectura + escritura)** — Existe un registro persistente de errores de publicación en `error-registry.jsonl` accesible por todas las ramas (estrategia git `merge=union`). **ANTES de generar cualquier plan:** ejecutar `python scripts/error_registry.py rules` y `python scripts/error_registry.py query --topic {nombre-tema} --status open`. Aplicar TODAS las reglas de prevención listadas. **DESPUÉS de cualquier error de publicación:** registrarlo con `python scripts/error_registry.py record --phase {FASE1|FASE2|FASE3} --type {tipo} --topic {tema} --course {id} --desc "descripción exacta" --cause "causa raíz"`. **Al resolver un error:** `python scripts/error_registry.py resolve --id {uuid} --resolution "cómo se resolvió"`. `publish_loop.py` registra automáticamente los errores de pipeline — los errores al generar el plan (ANTES de ejecutar publish_loop) deben registrarse manualmente. Esta regla aplica a TODOS los agentes EDU que generen o publiquen contenido.
<!-- EDU:END -->
