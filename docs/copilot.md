# GitHub Copilot — Estrategias y Funciones Nuevas (2026)

> Documento de referencia conectado a `.github/copilot-instructions.md`.  
> Actualizado: marzo 2026 · Fuente: [VS Code Docs](https://code.visualstudio.com/docs/copilot/overview)

---

## Índice

1. [Arquitectura de personalización](#1-arquitectura-de-personalización)
2. [Instrucciones personalizadas](#2-instrucciones-personalizadas)
3. [Agentes personalizados (.agent.md)](#3-agentes-personalizados-agentmd)
4. [Prompt files (.prompt.md)](#4-prompt-files-promptmd)
5. [Agent Skills (SKILL.md)](#5-agent-skills-skillmd)
6. [Hooks de ciclo de vida](#6-hooks-de-ciclo-de-vida)
7. [Servidores MCP](#7-servidores-mcp)
8. [Modos de agente y sesiones](#8-modos-de-agente-y-sesiones)
9. [Contexto de workspace](#9-contexto-de-workspace)
10. [Modelos de lenguaje](#10-modelos-de-lenguaje)
11. [Estrategias BMAD + Copilot](#11-estrategias-bmad--copilot)

---

## 1. Arquitectura de personalización

GitHub Copilot permite siete capas de personalización independientes que se pueden combinar:

| Capa | Archivos | Para qué |
|---|---|---|
| **Instrucciones siempre activas** | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md` | Estándares globales del proyecto |
| **Instrucciones por archivo** | `.github/instructions/*.instructions.md` | Reglas específicas por tipo de archivo |
| **Agentes personalizados** | `.github/agents/*.agent.md` | Personas especializadas con herramientas propias |
| **Prompt files** | `.github/prompts/*.prompt.md` | Flujos de trabajo reutilizables (slash commands) |
| **Agent Skills** | `.github/skills/<nombre>/SKILL.md` | Capacidades portables con scripts y recursos |
| **Hooks** | `.github/hooks/*.json` | Automatización determinista en eventos del ciclo de vida |
| **MCP servers** | `settings.json` / `mcp.json` | Conectores a bases de datos, APIs, servicios externos |

### Prioridad de instrucciones

```
Personal (usuario) > Workspace (copilot-instructions.md / AGENTS.md) > Organización
```

---

## 2. Instrucciones personalizadas

### 2.1 `copilot-instructions.md` (siempre activo)

Archivo Markdown en `.github/copilot-instructions.md`. Se aplica **automáticamente** a todas las peticiones de chat del workspace.

- Usar para: estándares de código, stack tecnológico, convenciones de arquitectura, requisitos de seguridad.
- **Este proyecto ya tiene este archivo configurado con el bloque BMAD.**

### 2.2 `.instructions.md` por archivo (condicional)

Se guardan en `.github/instructions/`. Se aplican cuando el agente trabaja con archivos que coinciden con el patrón `applyTo`.

```markdown
---
name: 'Python Standards'
description: 'Convenciones para archivos Python'
applyTo: '**/*.py'
---
- Seguir PEP 8
- Usar type hints en todas las funciones
```

Ubicaciones disponibles:
- Workspace: `.github/instructions/` (recursivo)
- Compatibilidad Claude: `.claude/rules/`
- Usuario: `~/.copilot/instructions/`

### 2.3 `AGENTS.md` (multi-agente)

Alternativa a `copilot-instructions.md`, reconocida por múltiples agentes de IA. Soporta múltiples archivos en subcarpetas (experimental con `chat.useNestedAgentsMdFiles`).

### 2.4 `CLAUDE.md` (compatibilidad)

Compatible con Claude Code. VS Code lo detecta en el workspace root, `.claude/CLAUDE.md`, `~/.claude/CLAUDE.md` y `CLAUDE.local.md`.

### 2.5 Generación automática

```
/init          → genera copilot-instructions.md para el workspace actual
/create-instruction → genera un .instructions.md específico con IA
```

---

## 3. Agentes personalizados (`.agent.md`)

### Estructura del archivo

```markdown
---
name: "Code Reviewer"
description: "Revisa seguridad y calidad del código"
tools: ['read', 'search']
model: "claude-sonnet-4-5 (copilot)"
agents: []
handoffs:
  - label: Implementar correcciones
    agent: dev
    prompt: "Implementa las correcciones encontradas en la revisión."
    send: false
---

Eres un experto en seguridad. Revisa el código buscando...
```

### Campos del frontmatter

| Campo | Descripción |
|---|---|
| `name` | Nombre mostrado en el picker de agentes |
| `description` | Descripción mostrada como placeholder |
| `tools` | Lista de herramientas disponibles (`['read','edit','search','execute','fetch']`) |
| `agents` | Sub-agentes disponibles (`*` = todos, `[]` = ninguno) |
| `model` | Modelo a usar (string o array con fallback) |
| `user-invocable` | `false` = solo subagente, no aparece en el picker |
| `disable-model-invocation` | `true` = no puede ser invocado como subagente |
| `handoffs` | Transiciones guiadas a otros agentes |
| `hooks` | Hooks escopados a este agente (Preview, requiere `chat.useCustomAgentHooks`) |
| `mcp-servers` | Config MCP para agentes en GitHub Copilot cloud |

### Ubicaciones

| Scope | Ruta |
|---|---|
| Workspace | `.github/agents/*.agent.md` |
| Claude format | `.claude/agents/*.md` |
| Usuario | `~/.copilot/agents/` |

### Handoffs (transiciones entre agentes)

Crean flujos encadenados. Después de que el agente responde, aparecen botones que transicionan al siguiente agente con contexto pre-cargado.

```markdown
handoffs:
  - label: "Revisar con QA"
    agent: qa-agent
    prompt: "Revisa la implementación buscando problemas de calidad."
    send: true   # auto-envía el prompt
    model: "gpt-4o (copilot)"
```

### Generación con IA

```
/create-agent  → genera un .agent.md basado en descripción de rol
```

---

## 4. Prompt files (`.prompt.md`)

Flujos de trabajo codificados como Markdown, invocables como **slash commands** (`/nombre-prompt`).

### Estructura

```markdown
---
description: "Scaffold de componente React"
agent: agent
model: "claude-sonnet-4-5 (copilot)"
tools: ['read', 'edit', 'search']
argument-hint: "[nombre-componente] [props]"
---

Crea un componente React llamado ${input:componentName} con las siguientes características...
```

### Campos del frontmatter

| Campo | Descripción |
|---|---|
| `description` | Texto descriptivo |
| `agent` | `ask`, `agent`, `plan` o nombre de agente personalizado |
| `model` | Modelo específico para el prompt |
| `tools` | Herramientas disponibles (prioridad sobre el agente) |
| `argument-hint` | Guía de argumentos mostrada al usuario |

### Variables soportadas

- `${selection}` — texto seleccionado en el editor
- `${input:variable}` — input del usuario en runtime
- `${input:variable:placeholder}` — con placeholder

### Ubicaciones

| Scope | Ruta |
|---|---|
| Workspace | `.github/prompts/*.prompt.md` |
| Usuario | Carpeta `prompts` del perfil VS Code activo |

### Prioridad de herramientas

1. Herramientas del `.prompt.md`
2. Herramientas del agente referenciado en el prompt
3. Herramientas por defecto del agente activo

### Generación con IA

```
/create-prompt → genera un .prompt.md basado en descripción de tarea
```

---

## 5. Agent Skills (`SKILL.md`)

Capacidades especializadas portables entre herramientas (VS Code, Copilot CLI, Copilot coding agent). Estándar abierto: [agentskills.io](https://agentskills.io/).

### Estructura de directorio

```
.github/skills/
└── webapp-testing/
    ├── SKILL.md           ← obligatorio
    ├── test-template.js   ← recursos opcionales
    └── examples/
```

### Estructura de SKILL.md

```markdown
---
name: webapp-testing
description: "Ejecuta y depura tests de aplicaciones web. Úsala cuando necesites
             crear, ejecutar o analizar tests de integración o E2E."
argument-hint: "[archivo de test] [opciones]"
user-invocable: true
disable-model-invocation: false
---

# Web App Testing Skill

## Cuándo usar esta skill
...
```

### Diferencia vs instrucciones personalizadas

| | Agent Skills | Custom Instructions |
|---|---|---|
| Propósito | Capacidades especializadas | Estándares de código |
| Portabilidad | VS Code, CLI, coding agent | Solo VS Code y GitHub.com |
| Contenido | Instrucciones + scripts + recursos | Solo instrucciones |
| Carga | On-demand, solo cuando es relevante | Siempre activa |
| Estándar | Abierto (agentskills.io) | Específico de VS Code |

### Ubicaciones

| Scope | Ruta |
|---|---|
| Workspace | `.github/skills/`, `.claude/skills/`, `.agents/skills/` |
| Usuario | `~/.copilot/skills/` |

### Invocación

```
/nombre-skill [argumentos]     → invocación manual
```
El agente también las carga automáticamente cuando detecta que la tarea es relevante.

### Generación con IA

```
/create-skill → genera un directorio SKILL.md basado en descripción
```

---

## 6. Hooks de ciclo de vida

> **Preview** · Archivo: `.github/hooks/*.json`

Comandos de shell que se ejecutan en puntos específicos del ciclo de vida del agente. Funcionan de forma **determinista** (no dependen del modelo).

### Eventos disponibles

| Evento | Cuándo se dispara |
|---|---|
| `SessionStart` | Al iniciar una nueva sesión de agente |
| `UserPromptSubmit` | Al enviar un prompt el usuario |
| `PreToolUse` | Antes de que el agente invoque cualquier herramienta |
| `PostToolUse` | Después de que una herramienta completa exitosamente |
| `PreCompact` | Antes de compactar el contexto de conversación |
| `SubagentStart` | Al crear un sub-agente |
| `SubagentStop` | Al finalizar un sub-agente |
| `Stop` | Al terminar la sesión del agente |

### Formato de configuración

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "type": "command",
        "command": "npx prettier --write \"$TOOL_INPUT_FILE_PATH\"",
        "timeout": 30
      }
    ],
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/validate-tool.sh",
        "linux": "./scripts/validate-linux.sh",
        "windows": "powershell -File scripts\\validate.ps1"
      }
    ]
  }
}
```

### Casos de uso principales

- **Formateo automático**: ejecutar Prettier/Black/gofmt después de cada edición
- **Políticas de seguridad**: bloquear comandos peligrosos (`rm -rf`, `DROP TABLE`)
- **Auditoría**: registrar cada invocación de herramienta
- **Inyección de contexto**: añadir info del proyecto al iniciar sesión

### Hooks escopados a agente (Preview)

```markdown
---
name: "Strict Formatter"
hooks:
  PostToolUse:
    - type: command
      command: "./scripts/format-changed-files.sh"
---
```

Requiere habilitar: `chat.useCustomAgentHooks: true`

### Control de comportamiento (salida del hook)

```json
{
  "continue": false,           // detiene toda la sesión
  "stopReason": "Motivo",
  "systemMessage": "Advertencia mostrada al usuario"
}
```

Para `PreToolUse`:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",   // "allow" | "deny" | "ask"
    "permissionDecisionReason": "Operación bloqueada por política"
  }
}
```

### Generación con IA

```
/create-hook → genera configuración de hook basada en descripción
```

---

## 7. Servidores MCP

Model Context Protocol — extiende el agente con herramientas de servicios externos.

- **Bases de datos**: consultar PostgreSQL, MongoDB, etc.
- **APIs externas**: GitHub, Jira, Slack, etc.
- **Herramientas de desarrollo**: scripts, CI/CD, etc.

Configuración en `settings.json` o `mcp.json`. Los agentes personalizados pueden incluir configuración MCP inline con `mcp-servers`.

```
/create-hook, /create-agent, /create-skill → AI puede sugerir configuraciones MCP
```

---

## 8. Modos de agente y sesiones

### Modos disponibles

| Modo | Descripción |
|---|---|
| **Ask** | Preguntas sobre el código, búsqueda agentica automática del workspace |
| **Agent** | Edición de archivos, comandos de terminal, ciclo completo |
| **Plan** | Genera un plan de implementación antes de codificar |
| **Background** | Tareas autónomas en segundo plano (máquina local) |
| **Cloud** | Crea branch + implementación + PR automáticamente |

### Sesiones paralelas

- Se pueden correr múltiples sesiones simultáneas de agente
- La vista **Sessions** del panel Chat centraliza todas las sesiones activas
- Cada sesión puede usar un agente, modelo o modo diferente

### Plan agent (nuevo)

El agente Plan analiza el codebase, hace preguntas aclaratorias y genera un plan paso a paso. Al aprobarlo, se puede delegar a un agente de implementación (local, background o cloud).

### Delegación entre tipos de agente

```
Local → Background → Cloud
```
El historial de conversación se transfiere al delegar.

---

## 9. Contexto de workspace

### Índices disponibles

| Tipo | Cuándo se usa | Límite |
|---|---|---|
| **Remote (GitHub)** | Repos en GitHub.com o Azure DevOps | Sin límite práctico |
| **Local avanzado** | Repos sin GitHub, < 2500 archivos | 2500 archivos |
| **Básico** | Repos sin GitHub, > 2500 archivos | — |

### Estrategias de búsqueda automática

- GitHub code search (repos en GitHub)
- Búsqueda semántica local (significado, no solo keywords)
- Búsqueda por nombre de archivo y contenido
- IntelliSense/LSP (símbolos, firmas, jerarquías de tipos)

### Modo híbrido para cambios locales

Si hay cambios no commiteados, VS Code combina el índice remoto con tracking local de archivos modificados.

### Construcción manual del índice

```
Ctrl+Shift+P → Build Remote Workspace Index
Ctrl+Shift+P → Build local workspace index  (para < 2500 archivos)
```

---

## 10. Modelos de lenguaje

- Se puede seleccionar el modelo por conversación o por agente/prompt personalizado
- Soporta modelos de Anthropic (Claude), OpenAI (GPT), y otros
- Se pueden agregar claves de API propias para acceder a modelos adicionales o locales
- En agentes/prompts se puede especificar array de modelos con fallback:

```markdown
model: ["claude-sonnet-4-7 (copilot)", "gpt-4o (copilot)"]
```

---

## 11. Estrategias BMAD + Copilot

### Cómo BMAD aprovecha las nuevas funciones

| Función BMAD | Función Copilot | Sinergia |
|---|---|---|
| Agentes BMAD (`.agent.md`) | Custom Agents | Los agentes BMAD ya usan el formato `.agent.md` con instrucciones de activación |
| Workflows BMAD (`.prompt.md`) | Prompt files | Los workflows BMAD se exponen como slash commands en Copilot Chat |
| Skills BMAD (copilot-skill://) | Agent Skills | Los skills de Copilot se registran como Agent Skills del workspace |
| `copilot-instructions.md` | Always-on instructions | Contiene la configuración BMAD global del proyecto |

### Estrategias nuevas disponibles para BMAD

#### 1. Hooks de validación automática
Añadir `.github/hooks/bmad-commit.json` para ejecutar validaciones automáticas al final de cada sesión de agente:

```json
{
  "hooks": {
    "Stop": [
      {
        "type": "command",
        "command": "git status --short"
      }
    ]
  }
}
```

#### 2. Handoffs entre agentes BMAD
Los agentes pueden incluir handoffs para flujos PM → Architect → Dev → QA:

```markdown
handoffs:
  - label: "Pasar a Arquitecto"
    agent: bmad-agent-bmm-architect
    prompt: "Revisa el PRD y crea la arquitectura técnica."
```

#### 3. Instrucciones por fase del proyecto
Crear archivos `.instructions.md` específicos por tipo de artefacto:

```
.github/instructions/
  planning/
    prd.instructions.md      (applyTo: 'salida/planning-artifacts/**/*.md')
  edu/
    edu-agents.instructions.md (applyTo: 'salida/edu-standalone/**')
```

#### 4. Agent Skills para BMAD
El skill de Copilot en `_bmad/` ya actúa como un Agent Skill. Se puede registrar formalmente:

```
.github/skills/
└── bmad-workflow/
    └── SKILL.md
```

#### 5. Sesiones paralelas para revisión
Usar una sesión con QA Agent para revisión mientras otra sesión de Dev Agent implementa.

#### 6. Plan Agent para epics grandes
Invocar el modo **Plan** para romper una epic grande en stories antes de pasar a Dev.

### Comandos rápidos de Copilot disponibles en este proyecto

```
/bmad-*              → workflows BMAD (prompt files registrados en .github/prompts/)
/bmad-help           → ayuda de BMAD
/bmad-dev            → activa Dev workflow
/bmad-qa             → activa QA workflow
/init                → regenera copilot-instructions.md
/create-agent        → crea nuevo agente con IA
/create-skill        → crea nuevo Agent Skill con IA
/create-prompt       → crea nuevo prompt file con IA
/create-instruction  → crea nueva instrucción condicional con IA
/create-hook         → crea nuevo hook de ciclo de vida con IA
```

### Chat Customizations Editor (Preview)

Acceso centralizado a toda la personalización:

```
Ctrl+Shift+P → Chat: Open Chat Customizations
```

Permite descobrir, crear y gestionar: agentes, skills, instrucciones, prompts, hooks, MCP servers.

---

## Referencias

- [VS Code Copilot Overview](https://code.visualstudio.com/docs/copilot/overview)
- [Customize AI in VS Code](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Hooks (Preview)](https://code.visualstudio.com/docs/copilot/customization/hooks)
- [Workspace Context](https://code.visualstudio.com/docs/copilot/reference/workspace-context)
- [Agent Skills Standard](https://agentskills.io/)
- [Awesome Copilot (comunidad)](https://github.com/github/awesome-copilot)
