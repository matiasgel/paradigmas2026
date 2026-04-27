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

<!-- EDU:START -->
## EDU Module — Output Rules

The EDU module lives **exclusively** in `salida/edu-standalone/`. There is no root `_edu/` folder.

### ChromaDB Knowledge Base — chroma-mcp (OBLIGATORIO)

**Todos los agentes EDU** tienen acceso al MCP server `chroma` configurado en `.vscode/mcp.json` (usa [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) con `--client-type persistent`).

- **Collection activa:** `edu_knowledge` con cosine similarity
- **Tipos de metadata (`type`):** `reference` (12 refs académicas), `tool` (16 docs de herramientas), `material` (libros del curso)
- **Chunk sizes:** reference/tool = 1500 chars, material = 800 chars (chunks pequeños para texto denso de libros sin separación de párrafos)
- **Búsqueda via MCP:** usar `chroma_query_documents` con `collection_name: "edu_knowledge"` y filtrar con `where: {"type": "material"}` si se necesita solo material del curso
- **Ruta ChromaDB:** se guarda en **disco local fuera del repo** (`EDU_CHROMA_PATH` en `.env`, default: `~/.edu/chroma_db`). NUNCA en git. Comando: `/edu-ingest`
- **Ingesta incremental (por defecto):** `python salida/edu-standalone/scripts/knowledge_base.py ingest --include-material` (agrega/actualiza sin borrar datos existentes; auto-convierte PDFs de `ingesta/` a TXT con pdfminer)
- **Re-ingesta destructiva (solo si es necesario):** `python salida/edu-standalone/scripts/knowledge_base.py ingest --force --include-material` (borra toda la collection primero)
- **Backup a Drive:** `python salida/edu-standalone/scripts/backup_knowledge_base.py` — comando `/edu-backup`
- **CLI alternativo:** `python salida/edu-standalone/scripts/knowledge_base.py search "query" --type material`

### REGLA CRÍTICA DE RUTAS — Sin excepciones

Cuando cualquier agente (BMAD o EDU) crea o modifica artefactos del módulo EDU, las rutas de destino son:

| Tipo de artefacto | Ruta de destino |
|---|---|
| Agentes EDU | `salida/edu-standalone/_edu/agents/` |
| Workflows EDU | `salida/edu-standalone/_edu/workflows/` |
| Tasks EDU | `salida/edu-standalone/_edu/tasks/` |
| Prompts EDU (`/edu-*`) | `salida/edu-standalone/.github/prompts/` |
| Agent files EDU | `salida/edu-standalone/.github/agents/` |
| Config EDU | `salida/edu-standalone/_edu/config.yaml` |
| Module help EDU | `salida/edu-standalone/_edu/module-help.csv` |

### Qué va a `salida/planning-artifacts/` o `salida/implementation-artifacts/`

Solo artefactos del framework BMAD (PRDs, epics, stories, arquitectura, etc.) que NO sean parte del módulo EDU.

### Deploy

`/goproduction` despliega `salida/edu-standalone/` → rama `production`. GitHub Actions lo ejecuta automáticamente al hacer push a `main` si se modificó algún path dentro de `salida/edu-standalone/`.
<!-- EDU:END -->
