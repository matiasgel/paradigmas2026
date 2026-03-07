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

## Key Conventions

- Always load `_bmad/bmm/config.yaml` before any agent activation or workflow execution
- Store all config fields as session variables: `{user_name}`, `{communication_language}`, `{output_folder}`, `{planning_artifacts}`, `{implementation_artifacts}`, `{project_knowledge}`
- MD-based workflows execute directly — load and follow the `.md` file
- YAML-based workflows require the workflow engine — load `workflow.xml` first, then pass the `.yaml` config
- Follow step-based workflow execution: load steps JIT, never multiple at once
- Save outputs after EACH step when using the workflow engine
- The `{project-root}` variable resolves to the workspace root at runtime

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
<!-- BMAD:END -->

<!-- EDU:START -->
## EDU Module — Output Rules

The EDU module lives **exclusively** in `salida/edu-standalone/`. There is no root `_edu/` folder.

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
