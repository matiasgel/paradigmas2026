<!-- BMAD:START -->
# BMAD Method — Project Instructions

## Project Configuration

- **Project**: paradigmas2026
- **User**: Matiasgel
- **Communication Language**: spanish
- **Document Output Language**: spanish
- **User Skill Level**: intermediate
- **Output Folder**: {project-root}/salida
- **Planning Artifacts**: {project-root}/salida/planning-artifacts
- **Implementation Artifacts**: {project-root}/salida/implementation-artifacts
- **Project Knowledge**: {project-root}/docs

## BMAD Runtime Structure

- **Agent definitions**: `_bmad/bmm/agents/` (BMM module) and `_bmad/core/agents/` (core)
- **Workflow definitions**: `_bmad/bmm/workflows/` (organized by phase)
- **Core tasks**: `_bmad/core/tasks/` (help, editorial review, indexing, sharding, adversarial review)
- **Core workflows**: `_bmad/core/workflows/` (brainstorming, party-mode, advanced-elicitation)
- **Workflow engine**: `_bmad/core/tasks/workflow.xml` (executes YAML-based workflows)
- **Module configuration**: `_bmad/bmm/config.yaml`
- **Core configuration**: `_bmad/core/config.yaml`
- **Agent manifest**: `_bmad/_config/agent-manifest.csv`
- **Workflow manifest**: `_bmad/_config/workflow-manifest.csv`
- **Help manifest**: `_bmad/_config/bmad-help.csv`
- **Agent memory**: `_bmad/_memory/`

## Propósito del Proyecto

> **REGLA FUNDAMENTAL:** Todo pedido al usuario o cualquier instrucción dirigida a BMAD en este proyecto tiene como **único objetivo desarrollar el módulo `edu-standalone`**. Los agentes y workflows de BMAD se usan como herramientas de trabajo, pero **NUNCA se modifican los archivos de BMAD** (`_bmad/`). Cualquier artefacto generado debe depositarse en `salida/edu-standalone/` según las reglas del módulo EDU.

## Key Conventions

- Always load `_bmad/bmm/config.yaml` before any agent activation or workflow execution
- Store all config fields as session variables: `{user_name}`, `{communication_language}`, `{output_folder}`, `{planning_artifacts}`, `{implementation_artifacts}`, `{project_knowledge}`
- MD-based workflows execute directly — load and follow the `.md` file
- YAML-based workflows require the workflow engine — load `workflow.xml` first, then pass the `.yaml` config
- Follow step-based workflow execution: load steps JIT, never multiple at once
- Save outputs after EACH step when using the workflow engine
- The `{project-root}` variable resolves to the workspace root at runtime
- **NUNCA modificar archivos dentro de `_bmad/`** — BMAD es solo el framework de trabajo, no el producto final

## Available Agents

| Agent | Persona | Title | Capabilities |
|---|---|---|---|
| bmad-master | BMad Master | BMad Master Executor, Knowledge Custodian, and Workflow Orchestrator | runtime resource management, workflow orchestration, task execution, knowledge custodian |
| analyst | Mary | Business Analyst | market research, competitive analysis, requirements elicitation, domain expertise |
| architect | Winston | Architect | distributed systems, cloud infrastructure, API design, scalable patterns |
| dev | Amelia | Developer Agent | story execution, test-driven development, code implementation |
| pm | John | Product Manager | PRD creation, requirements discovery, stakeholder alignment, user interviews |
| qa | Quinn | QA Engineer | test automation, API testing, E2E testing, coverage analysis |
| quick-flow-solo-dev | Barry | Quick Flow Solo Dev | rapid spec creation, lean implementation, minimum ceremony |
| sm | Bob | Scrum Master | sprint planning, story preparation, agile ceremonies, backlog management |
| tech-writer | Paige | Technical Writer | agent capabilities |
| ux-designer | Sally | UX Designer | user research, interaction design, UI patterns, experience strategy |

## Slash Commands

Type `/bmad-` in Copilot Chat to see all available BMAD workflows and agent activators. Agents are also available in the agents dropdown.

## GitHub Copilot — Manual Completo (actualizado marzo 2026)

Para conocer todas las funciones de GitHub Copilot, mejores prácticas, novedades 2026 y cómo BMAD las aprovecha, consultar:

📄 **[docs/copilot.md](../docs/copilot.md)**

Incluye (actualizado):
- Arquitectura de las **8 capas** de personalización de Copilot
- Custom instructions (`copilot-instructions.md`, `.instructions.md` con `applyTo`, `AGENTS.md`, `CLAUDE.md`)
- Custom agents (`.agent.md`) — campos nuevos: `icon`, `temperature`, `max-tokens`, tool `fetch`
- Prompt files (`.prompt.md`) — variable `${file:ruta}` nueva, `${changes}`, `${problems}`
- Agent Skills (`SKILL.md`) — capacidades portables (estándar abierto agentskills.io)
- Hooks de ciclo de vida (GA) — campo `condition` nuevo, variables `$WORKSPACE_ROOT`, `$SESSION_ID`
- Servidores MCP — config en `.vscode/mcp.json`, tipos stdio/http/sse, 9+ servidores populares
- Modos de agente: Ask, Agent, Plan (GA), Background, Cloud — llamadas paralelas de herramientas
- Variables de contexto: `#changes`, `#problems`, `#testFailure`, `#sym`, `#searchResults`
- Modelos disponibles: Claude Sonnet 4.7, o3-mini, Gemini 2.0 Flash, GPT-4.5 y más
- Copilot Coding Agent (Cloud) — asignar issues de GitHub a Copilot para PRs automáticos
- Copilot Extensions — `@docker`, `@azure`, `@sentry`, etc.
- Estrategias BMAD + Copilot (7 estrategias actualizadas)
- Mejores prácticas, anti-patrones y checklist de deploy para agentes/prompts

## Commit & Push at Session End

**MANDATORY RULE for all agents:** At the end of a session where files have been created or modified and the user has accepted the changes, the agent MUST automatically execute the following steps:

1. Check for changes with `git status`
2. Stage all changes: `git add -A`
3. Create a descriptive commit with the format:
   `git commit -m "agent: <brief summary of changes made>"`
   - Use the active agent name as prefix (e.g. `dev:`, `pm:`, `analyst:`, `sm:`, `architect:`, `qa:`)
   - The message must clearly summarize what artifacts were created or modified
4. Push to the current branch: `git push`

**When to commit:**
- After successfully completing a workflow or task
- When the user confirms the changes are correct
- At the end of the session if there are new or modified uncommitted files

**When NOT to commit:**
- If the user explicitly indicates they don't want a commit yet
- If there are errors or incomplete changes pending
<!-- BMAD:END -->


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
<!-- EDU:END -->
