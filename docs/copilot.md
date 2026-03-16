# GitHub Copilot — Manual Completo y Actualizado (2026)

> Documento de referencia conectado a `.github/copilot-instructions.md`.  
> Actualizado: **16 marzo 2026** · Fuentes: [VS Code Docs](https://code.visualstudio.com/docs/copilot/overview) · [GitHub Docs Copilot](https://docs.github.com/en/copilot) · [Copilot Changelog](https://github.blog/changelog/label/copilot/)

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
9. [Variables de contexto](#9-variables-de-contexto)
10. [Contexto de workspace e indexado](#10-contexto-de-workspace-e-indexado)
11. [Modelos de lenguaje disponibles](#11-modelos-de-lenguaje-disponibles)
12. [Copilot Coding Agent (Cloud)](#12-copilot-coding-agent-cloud)
13. [Copilot Extensions](#13-copilot-extensions)
14. [Copilot para PRs y Code Review](#14-copilot-para-prs-y-code-review)
15. [Inline Chat y Quick Chat](#15-inline-chat-y-quick-chat)
16. [Slash Commands de referencia](#16-slash-commands-de-referencia)
17. [Estrategias BMAD + Copilot](#17-estrategias-bmad--copilot)
18. [Mejores prácticas para prompts, agentes y workflows](#18-mejores-prácticas-para-prompts-agentes-y-workflows)

---

## 1. Arquitectura de personalización

GitHub Copilot permite **ocho capas** de personalización independientes y combinables (actualizado 2026):

| Capa | Archivos | Para qué | Estado |
|---|---|---|---|
| **Instrucciones siempre activas** | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md` | Estándares globales del proyecto | GA |
| **Instrucciones por archivo** | `.github/instructions/*.instructions.md` | Reglas específicas por tipo de archivo o carpeta | GA |
| **Agentes personalizados** | `.github/agents/*.agent.md` | Personas especializadas con herramientas, modelo y hooks propios | GA |
| **Prompt files** | `.github/prompts/*.prompt.md` | Flujos de trabajo reutilizables (slash commands) | GA |
| **Agent Skills** | `.github/skills/<nombre>/SKILL.md` | Capacidades portables con scripts y recursos | GA |
| **Hooks** | `.github/hooks/*.json` | Automatización determinista en eventos del ciclo de vida | Preview→GA |
| **MCP servers** | `settings.json` / `.vscode/mcp.json` / `mcp.json` | Conectores a bases de datos, APIs, servicios externos | GA |
| **Copilot Extensions** | GitHub Marketplace | Herramientas externas con `@extension-name` | GA |

### Prioridad de instrucciones

```
Personal (usuario) > Workspace (copilot-instructions.md / AGENTS.md) > Organización
```

### Estructura recomendada de carpetas en 2026

```
.github/
├── copilot-instructions.md    ← instrucciones siempre activas
├── agents/                    ← agentes personalizados
│   └── *.agent.md
├── prompts/                   ← slash commands / prompt files
│   └── *.prompt.md
├── instructions/              ← instrucciones condicionales por tipo de archivo
│   └── *.instructions.md
├── hooks/                     ← hooks de ciclo de vida
│   └── *.json
└── skills/                    ← agent skills
    └── <nombre>/SKILL.md
.vscode/
└── mcp.json                   ← config MCP del workspace (nuevo 2026)
```

---

## 2. Instrucciones personalizadas

### 2.1 `copilot-instructions.md` (siempre activo)

Archivo Markdown en `.github/copilot-instructions.md`. Se aplica **automáticamente** a todas las peticiones de chat del workspace.

- Usar para: estándares de código, stack tecnológico, convenciones de arquitectura, requisitos de seguridad.
- **Este proyecto ya tiene este archivo configurado con el bloque BMAD.**
- **Novedad 2026:** El archivo se trunca si supera el límite de tokens — mantenerlo conciso y usar referencias a otros docs (como este).

### 2.2 `.instructions.md` por archivo/carpeta (condicional)

Se guardan en `.github/instructions/`. Se aplican cuando el agente trabaja con archivos que coinciden con el patrón `applyTo`.

```markdown
---
name: 'Python Standards'
description: 'Convenciones para archivos Python'
applyTo: '**/*.py'
---
- Seguir PEP 8
- Usar type hints en todas las funciones públicas
- Docstrings en formato Google style
```

**Nuevos patrones `applyTo` soportados:**

```markdown
applyTo: '**'                      # aplica a todos los archivos
applyTo: 'salida/edu-standalone/**' # aplica solo en carpeta EDU
applyTo: '**/*.{ts,tsx}'           # múltiples extensiones
applyTo: 'src/components/**'       # carpeta específica
```

**Ubicaciones disponibles:**
- Workspace: `.github/instructions/` (recursivo en subcarpetas)
- Compatibilidad Claude: `.claude/rules/`
- Usuario: `~/.copilot/instructions/`

> **Buena práctica:** Descomponer en instrucciones pequeñas y específicas en lugar de un solo archivo grande. Usar `applyTo` preciso para que no se carguen instrucciones innecesarias.

### 2.3 `AGENTS.md` (multi-agente)

Alternativa a `copilot-instructions.md`, reconocida por múltiples agentes de IA (Copilot, Claude, Gemini). Soporta múltiples archivos en subcarpetas con `chat.useNestedAgentsMdFiles: true`.

```markdown
# Reglas del Proyecto

## Para todos los agentes
- Responder siempre en español
- No modificar archivos dentro de `_bmad/`

## Para agentes de código
- Tests obligatorios para funciones públicas
```

### 2.4 `CLAUDE.md` (compatibilidad)

Compatible con Claude Code. VS Code lo detecta en el workspace root, `.claude/CLAUDE.md`, `~/.claude/CLAUDE.md` y `CLAUDE.local.md`. En 2026, GitHub Copilot también lo lee cuando Claude es el modelo activo.

### 2.5 Generación automática con IA

```
/init                → genera copilot-instructions.md para el workspace actual
/create-instruction  → genera un .instructions.md específico con IA
```

---

## 3. Agentes personalizados (`.agent.md`)

### Estructura completa del archivo (2026)

```markdown
---
name: "Code Reviewer"
description: "Revisa seguridad y calidad del código"
icon: "🔍"
tools: ['read', 'search']
agents: ['qa-agent']
model: ["claude-sonnet-4-7 (copilot)", "gpt-4o (copilot)"]
user-invocable: true
disable-model-invocation: false
handoffs:
  - label: Implementar correcciones
    agent: dev-agent
    prompt: "Implementa las correcciones encontradas en la revisión."
    send: false
    model: "claude-sonnet-4-7 (copilot)"
hooks:
  PostToolUse:
    - type: command
      command: "./scripts/lint-changed.sh"
---

Eres un experto en seguridad. Revisa el código buscando...
```

### Campos del frontmatter — tabla completa

| Campo | Tipo | Descripción | Novedad |
|---|---|---|---|
| `name` | string | Nombre mostrado en el picker de agentes | — |
| `description` | string | Descripción como placeholder (se ve en el chat) | — |
| `icon` | string | Emoji o nombre de icono de VS Code | **Nuevo 2026** |
| `tools` | array | `['read','edit','search','execute','fetch','create']` | `fetch` y `create` **nuevos** |
| `agents` | array/`*` | Sub-agentes disponibles (`*` = todos, `[]` = ninguno) | — |
| `model` | string/array | Modelo o lista con fallback | — |
| `user-invocable` | bool | `false` = solo subagente, no aparece en el picker | — |
| `disable-model-invocation` | bool | `true` = no puede invocarse como subagente | — |
| `handoffs` | array | Transiciones guiadas a otros agentes | — |
| `hooks` | objeto | Hooks escopados a este agente | Estabilizado 2026 |
| `mcp-servers` | objeto | Config MCP inline para agentes cloud | — |
| `temperature` | float | Temperatura del modelo (0.0–2.0) | **Nuevo 2026** |
| `max-tokens` | int | Límite de tokens de salida | **Nuevo 2026** |

### Ubicaciones

| Scope | Ruta |
|---|---|
| Workspace | `.github/agents/*.agent.md` |
| Claude format | `.claude/agents/*.md` |
| Usuario | `~/.copilot/agents/` |

### Handoffs (transiciones entre agentes)

Crean flujos encadenados. Después de que el agente responde, aparecen botones de transición con contexto pre-cargado.

```markdown
handoffs:
  - label: "Revisar con QA"
    agent: qa-agent
    prompt: "Revisa la implementación buscando problemas de calidad y cobertura."
    send: true          # auto-envía el prompt al siguiente agente
    model: "gpt-4o (copilot)"
  - label: "Documentar con Tech Writer"
    agent: tech-writer
    prompt: "Documenta los cambios implementados."
    send: false         # espera confirmación del usuario
```

> **Novedad 2026:** `send: true` ejecuta automáticamente el handoff sin confirmación adicional del usuario.

### Tool: `fetch`

Permite al agente acceder a URLs externas durante la sesión. Útil para consultar docs o APIs. Se declara en `tools: ['fetch']`.

### Generación con IA

```
/create-agent  → genera un .agent.md basado en descripción de rol
```

---

## 4. Prompt files (`.prompt.md`)

Flujos de trabajo codificados como Markdown, invocables como **slash commands** (`/nombre-prompt`).

### Estructura completa (2026)

```markdown
---
description: "Scaffold de componente React con tests"
agent: agent
model: "claude-sonnet-4-7 (copilot)"
tools: ['read', 'edit', 'search', 'create']
argument-hint: "[nombre-componente] [props opcionales]"
---

# Crear Componente React

Crea un componente React llamado **${input:componentName:MyComponent}** en `src/components/`.

Contexto del proyecto actual:
${file:src/components/README.md}

## Especificaciones
- TypeScript con tipo de props explícito
- Tests unitarios con Vitest en `__tests__/`
- Exportar como named export

Archivos seleccionados como referencia: ${selection}
```

### Campos del frontmatter — tabla completa

| Campo | Descripción | Novedad |
|---|---|---|
| `description` | Texto descriptivo del prompt | — |
| `agent` | `ask`, `agent`, `plan`, o nombre de agente personalizado | — |
| `model` | Modelo específico para el prompt | — |
| `tools` | Herramientas disponibles (prioridad sobre el agente) | — |
| `argument-hint` | Guía de argumentos mostrada al usuario | — |
| `temperature` | Temperatura del modelo | **Nuevo 2026** |

### Variables soportadas — completas

| Variable | Descripción |
|---|---|
| `${selection}` | Texto seleccionado en el editor activo |
| `${input:var}` | Input del usuario en runtime |
| `${input:var:placeholder}` | Input con texto de ayuda |
| `${file:ruta/al/archivo}` | Contenido de un archivo del workspace |
| `${editor}` | Contenido del editor activo |
| `${codebase}` | Contexto del codebase actual |
| `${changes}` | Cambios git pendientes (unstaged/staged) |

> **Novedad 2026:** `${file:...}` permite incrustar el contenido de archivos directamente en el prompt en tiempo de ejecución.

### Ubicaciones

| Scope | Ruta |
|---|---|
| Workspace | `.github/prompts/*.prompt.md` |
| Usuario | Carpeta `prompts` del perfil VS Code activo |

### Prioridad de herramientas

1. Herramientas declaradas en el `.prompt.md`
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
    ├── SKILL.md              ← obligatorio
    ├── test-template.js      ← recursos opcionales
    ├── scripts/
    │   └── run-tests.sh
    └── examples/
        └── sample.test.js
```

### Estructura de SKILL.md completa

```markdown
---
name: webapp-testing
description: "Ejecuta y depura tests de aplicaciones web. Úsala cuando necesites
             crear, ejecutar o analizar tests de integración o E2E."
argument-hint: "[archivo de test] [opciones]"
user-invocable: true
disable-model-invocation: false
tools: ['read', 'execute', 'search']
---

# Web App Testing Skill

## Cuándo usar esta skill
Cuando el usuario pide crear, ejecutar, depurar o analizar tests.

## Cómo usarla
1. Leer el archivo de test indicado o buscar tests existentes
2. Ejecutar: `./scripts/run-tests.sh ${input:testFile}`
3. Analizar resultados y sugerir correcciones

## Recursos disponibles
- `test-template.js` — plantilla base para nuevos tests
- `examples/` — tests de referencia del proyecto
```

### Diferencia vs instrucciones personalizadas

| | Agent Skills | Custom Instructions |
|---|---|---|
| Propósito | Capacidades especializadas | Estándares de código |
| Portabilidad | VS Code, CLI, coding agent | Solo VS Code y GitHub.com |
| Contenido | Instrucciones + scripts + recursos | Solo instrucciones markdown |
| Carga | On-demand, solo cuando es relevante | Siempre activa (consume tokens) |
| Estándar | Abierto (agentskills.io) | Específico de VS Code |

### Ubicaciones

| Scope | Ruta |
|---|---|
| Workspace | `.github/skills/`, `.claude/skills/`, `.agents/skills/` |
| Usuario | `~/.copilot/skills/` |

### Invocación

```
/nombre-skill [argumentos]     → invocación manual explícita
```
El agente también las carga **automáticamente** cuando detecta que la tarea es relevante (basado en la `description` del SKILL.md).

### Generación con IA

```
/create-skill → genera un directorio SKILL.md basado en descripción
```

---

## 6. Hooks de ciclo de vida

> **Estado 2026:** Hooks básicos estabilizados (GA). Hooks escopados a agente siguen en Preview.  
> **Archivos:** `.github/hooks/*.json` o inline en `.agent.md`

Comandos de shell que se ejecutan en puntos específicos del ciclo de vida del agente. Funcionan de forma **determinista** (no dependen del LLM).

### Eventos disponibles — completos

| Evento | Cuándo se dispara | Uso principal |
|---|---|---|
| `SessionStart` | Al iniciar una nueva sesión de agente | Cargar contexto, hacer setup |
| `UserPromptSubmit` | Al enviar un prompt el usuario | Validar input, inyectar contexto |
| `PreToolUse` | Antes de que el agente invoque cualquier herramienta | Políticas de seguridad, bloquear comandos |
| `PostToolUse` | Después de que una herramienta completa exitosamente | Formateo, auditoría |
| `PreCompact` | Antes de compactar el contexto de conversación | Guardar estado importante |
| `SubagentStart` | Al crear un sub-agente | Setup del sub-agente |
| `SubagentStop` | Al finalizar un sub-agente | Cleanup |
| `Stop` | Al terminar la sesión del agente | Commits, notificaciones, cleanup |

### Variables de entorno disponibles en hooks

| Variable | Valor |
|---|---|
| `$TOOL_NAME` | Nombre de la herramienta invocada |
| `$TOOL_INPUT_FILE_PATH` | Ruta del archivo afectado (para `edit`, `create`, `read`) |
| `$TOOL_INPUT_COMMAND` | Comando ejecutado (para `execute`) |
| `$SESSION_ID` | ID único de la sesión actual |
| `$WORKSPACE_ROOT` | Ruta raíz del workspace |

### Formato de configuración completo

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "type": "command",
        "command": "npx prettier --write \"$TOOL_INPUT_FILE_PATH\"",
        "timeout": 30,
        "condition": {
          "toolName": ["edit", "create"],
          "filePattern": "**/*.{js,ts,jsx,tsx,json}"
        }
      }
    ],
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/validate-tool.sh",
        "linux": "./scripts/validate-linux.sh",
        "windows": "powershell -File scripts\\validate.ps1",
        "timeout": 10
      }
    ],
    "Stop": [
      {
        "type": "command",
        "command": "git status --short && echo '--- Sesión finalizada ---'",
        "timeout": 15
      }
    ]
  }
}
```

> **Novedad 2026:** Campo `condition` para filtrar el hook por nombre de herramienta o patrón de archivo.

### Casos de uso principales

- **Formateo automático**: ejecutar Prettier/Black/gofmt/ruff después de cada edición
- **Políticas de seguridad**: bloquear comandos peligrosos (`rm -rf`, `DROP TABLE`, `git push --force`)
- **Auditoría**: registrar cada invocación de herramienta en un log
- **Inyección de contexto**: añadir info del proyecto al iniciar sesión
- **Commits automáticos**: hacer commit al terminar la sesión (regla BMAD)
- **Linting**: ejecutar ESLint/flake8/mypy post-edición

### Hooks escopados a agente (Preview → estabilizándose)

```markdown
---
name: "Strict Formatter"
hooks:
  PostToolUse:
    - type: command
      command: "./scripts/format-changed-files.sh"
      condition:
        toolName: ["edit"]
---
```

Requiere: `"chat.useCustomAgentHooks": true` en `settings.json`

### Control de comportamiento (salida del hook)

```json
{
  "continue": false,
  "stopReason": "Operación cancelada por política de seguridad",
  "systemMessage": "Se detectó un comando bloqueado. Usa el script autorizado en scripts/."
}
```

Para `PreToolUse` — control de permisos:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Comando rm -rf bloqueado por política del proyecto"
  }
}
```

Valores de `permissionDecision`: `"allow"` | `"deny"` | `"ask"`

### Generación con IA

```
/create-hook → genera configuración de hook basada en descripción de caso de uso
```

---

## 7. Servidores MCP

Model Context Protocol (MCP) — extiende el agente con herramientas de servicios externos. Estabilizado como estándar abierto en 2025-2026.

### Configuración en VS Code (2026)

**Opción A — `.vscode/mcp.json` (workspace, recomendado):**
```json
{
  "servers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    },
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/al/workspace"]
    },
    "postgres": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${env:DATABASE_URL}"]
    }
  }
}
```

**Opción B — `settings.json` (usuario o workspace):**
```json
{
  "mcp": {
    "servers": {
      "my-server": {
        "type": "http",
        "url": "http://localhost:3100/mcp",
        "headers": {
          "Authorization": "Bearer ${env:MCP_TOKEN}"
        }
      }
    }
  }
}
```

### Tipos de transporte disponibles

| Tipo | Cuándo usar |
|---|---|
| `stdio` | Proceso local, más común. El servidor se inicia como subproceso |
| `http` | Servidor remoto o local ya corriendo con endpoint HTTP/SSE |
| `sse` | Server-Sent Events, para streams en tiempo real |

### Variables de entorno en config MCP

Usar `${env:VARIABLE}` para evitar hardcodear secretos en archivos versionados. Las variables se resuelven del entorno del sistema o de `.env` (si está configurado).

### MCP inline en agentes personalizados

```markdown
---
name: "DB Assistant"
tools: ['read', 'search']
mcp-servers:
  postgres:
    type: stdio
    command: npx
    args: ["-y", "@modelcontextprotocol/server-postgres", "${env:DATABASE_URL}"]
---
```

### Servidores MCP populares 2026

| Servidor | Paquete NPM | Para qué |
|---|---|---|
| GitHub | `@modelcontextprotocol/server-github` | Issues, PRs, repos, código |
| Filesystem | `@modelcontextprotocol/server-filesystem` | Acceso granular a archivos |
| PostgreSQL | `@modelcontextprotocol/server-postgres` | Consultas SQL |
| Brave Search | `@modelcontextprotocol/server-brave-search` | Búsqueda web |
| Puppeteer | `@modelcontextprotocol/server-puppeteer` | Browser automation |
| Slack | `@modelcontextprotocol/server-slack` | Mensajes y canales |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Docs y archivos Drive |
| Memory | `@modelcontextprotocol/server-memory` | Persistencia entre sesiones |
| Fetch | `@modelcontextprotocol/server-fetch` | HTTP requests a URLs externas |

### Descubrir e instalar desde VS Code

```
Ctrl+Shift+P → MCP: Add Server
Ctrl+Shift+P → MCP: List Servers
Ctrl+Shift+P → MCP: Restart Server
```

---

## 8. Modos de agente y sesiones

### Modos disponibles en 2026

| Modo | Comando | Descripción | Estado |
|---|---|---|---|
| **Ask** | (predeterminado) | Preguntas, explicaciones, búsqueda automática del workspace | GA |
| **Agent** | `@agent` o selector | Edición de archivos, terminal, ciclo completo agentico | GA |
| **Plan** | `@plan` o `plan:` | Genera plan checklist antes de codificar, luego delega | GA |
| **Background** | Panel Sessions | Tarea autónoma en segundo plano, máquina local | GA |
| **Cloud** | `@github` | Crea branch + commit + PR automáticamente en GitHub | GA |

> **Novedad 2026:** Plan mode es ahora **GA** y el modo recomendado para tareas complejas. No más Preview.

### Agent mode — novedades 2026

- **Llamadas a herramientas en paralelo**: el agente puede ejecutar múltiples herramientas simultáneamente cuando no hay dependencias entre ellas (ej: leer varios archivos al mismo tiempo).
- **Auto-recuperación de errores**: si un comando falla, el agente intenta alternativas antes de pedir ayuda.
- **Contexto persistente de terminal**: el agente recuerda el directorio actual y variables de entorno entre comandos de la misma sesión.
- **Tool: `fetch`**: el agente puede hacer requests HTTP a URLs externas (documentación, APIs públicas).

### Plan mode — flujo de trabajo

```
Usuario describe tarea
↓
Plan agent analiza el codebase
↓
Hace preguntas aclaratorias (si las hay)
↓
Genera checklist de pasos con archivos afectados
↓
Usuario revisa y aprueba (o modifica)
↓
Se delega a Agent mode (local) o Cloud agent (GitHub)
```

El plan puede exportarse como archivo `.md` para documentación.

### Sesiones paralelas

- Se pueden correr **múltiples sesiones simultáneas** (ej: Dev implementa mientras QA revisa)
- La vista **Sessions** (`Ctrl+Shift+P → Chat: Focus on Sessions View`) centraliza todas las sesiones
- Cada sesión puede usar un agente, modelo y modo diferente
- El historial se conserva cuando se transfiere entre modos (local → cloud)

### Delegación entre modos

```
Local Agent → Background Agent → Cloud Agent
     ↑                                 ↓
     └────────── Pull Request ──────────┘
```

---

## 9. Variables de contexto

Las variables de contexto se referencian con `#` en el chat o en prompt files con `${}`. Permiten adjuntar información específica sin copiar texto manualmente.

### Variables disponibles — completas 2026

| Variable de chat | Variable en prompt | Descripción |
|---|---|---|
| `#file` | `${file:ruta}` | Contenido de un archivo específico |
| `#folder` | — | Todos los archivos de una carpeta |
| `#editor` | `${editor}` | Contenido del editor activo actual |
| `#selection` | `${selection}` | Texto seleccionado en el editor |
| `#codebase` | `${codebase}` | Contexto general del workspace (indexado) |
| `#terminalSelection` | — | Texto seleccionado en la terminal activa |
| `#terminalLastCommand` | — | Último comando ejecutado en la terminal |
| `#problems` | `${problems}` | Errores y warnings del panel Problems |
| `#changes` | `${changes}` | Cambios git (unstaged + staged) |
| `#testFailure` | — | Resultado del último test fallido |
| `#sym` | — | Símbolo de código (función, clase, variable) |
| `#searchResults` | — | Resultados actuales de la vista Search |
| `#notebookCell` | — | Celda activa de Jupyter Notebook |

### Uso en el chat

```
Explica #file:src/slides_pipeline.py

¿Cómo puedo arreglar #problems?

Basándote en #changes, genera el commit message apropiado

Revisa #terminalLastCommand y dime qué salió mal
```

### Uso en prompt files

```markdown
Analiza los siguientes cambios y genera un CHANGELOG:

${changes}

Archivos de referencia:
${file:CHANGELOG.md}
```

---

## 10. Contexto de workspace e indexado

### Tipos de índice disponibles

| Tipo | Cuándo se usa | Límite | Novedad |
|---|---|---|---|
| **Remote (GitHub)** | Repos en GitHub.com o Azure DevOps con GitHub Copilot | Sin límite práctico | — |
| **Local avanzado** | Repos sin GitHub, < 2500 archivos indexables | 2500 archivos | — |
| **Básico** | Repos sin GitHub, > 2500 archivos | Sin límite, menos preciso | — |
| **Chroma local** | Indexado semántico con embeddings locales | 50.000 archivos | **Nuevo 2026** |

### Estrategias de búsqueda automática

- **GitHub code search** (repos en GitHub.com)
- **Búsqueda semántica** con embeddings (significado, no solo keywords)
- **Búsqueda por nombre de archivo** y contenido literal
- **IntelliSense/LSP**: símbolos, firmas, jerarquías de tipos, referencias cruzadas
- **Búsqueda de archivos recientes**: prioriza archivos abiertos/modificados recientemente

### Modo híbrido para cambios locales

Si hay cambios no commiteados, VS Code combina el índice remoto con tracking local de archivos modificados (via `#changes`).

### Construcción manual del índice

```
Ctrl+Shift+P → Copilot: Build Remote Workspace Index
Ctrl+Shift+P → Copilot: Build Local Workspace Index (< 2500 archivos)
Ctrl+Shift+P → Copilot: Rebuild Workspace Index
```

### Exclusión de archivos del índice

Usar `.copilotignore` en la raíz del workspace (mismo formato que `.gitignore`):

```
.env*
secrets/
node_modules/
*.log
_edu/credentials.json
_edu/token_slides.json
```

---

## 11. Modelos de lenguaje disponibles

### Modelos actuales en GitHub Copilot (marzo 2026)

| Modelo | ID en config | Fortaleza | Recomendado para |
|---|---|---|---|
| Claude Sonnet 4.5 | `claude-sonnet-4-5 (copilot)` | Equilibrio velocidad/calidad | Tareas cotidianas |
| Claude Sonnet 4.6 | `claude-sonnet-4-6 (copilot)` | Mejor razonamiento | Arquitectura, análisis |
| Claude Sonnet 4.7 | `claude-sonnet-4-7 (copilot)` | Última versión Claude | Tareas complejas (**recomendado**) |
| Claude Haiku 3.5 | `claude-haiku-3-5 (copilot)` | Ultra rápido, barato | Completions inline, scripts simples |
| GPT-4o | `gpt-4o (copilot)` | Multimodal, visión | Análisis de imágenes, UI |
| GPT-4.5 | `gpt-4.5 (copilot)` | Conversacional avanzado | Chat, brainstorming |
| o3-mini | `o3-mini (copilot)` | Razonamiento matemático | Algoritmos, lógica compleja |
| Gemini 2.0 Flash | `gemini-2.0-flash (copilot)` | Muy rápido | Completions, revisiones rápidas |
| Gemini 1.5 Pro | `gemini-1.5-pro (copilot)` | Contexto largo (1M tokens) | Análisis de repos grandes |

### Selección de modelo por contexto

```markdown
# En .agent.md o .prompt.md — fallback list
model: ["claude-sonnet-4-7 (copilot)", "gpt-4o (copilot)", "claude-sonnet-4-5 (copilot)"]

# Modelo único
model: "claude-sonnet-4-7 (copilot)"
```

### Modelos propios (BYOK — Bring Your Own Key)

Se pueden agregar modelos de Azure OpenAI, Anthropic API directa, Ollama local, etc.:

```json
// settings.json
{
  "github.copilot.models": [
    {
      "id": "ollama/llama3.2",
      "displayName": "Llama 3.2 (Local)",
      "endpoint": "http://localhost:11434/v1",
      "apiKey": "ollama"
    }
  ]
}
```

---

## 12. Copilot Coding Agent (Cloud)

> **Estado:** GA (disponible con GitHub Copilot Enterprise y algunas cuentas Pro+)

El Coding Agent es una modalidad completamente autónoma donde Copilot trabaja como si fuera un desarrollador asignado a un issue de GitHub.

### Flujo de trabajo

```
1. Asignar Copilot a un GitHub Issue (como asignee)
   ↓
2. Copilot analiza el issue, el codebase y el contexto
   ↓
3. Crea un branch automáticamente
   ↓
4. Implementa los cambios (commits iterativos)
   ↓
5. Abre un Pull Request con descripción detallada
   ↓
6. El humano revisa, comenta y aprueba/rechaza
   ↓
7. Copilot responde a los comentarios y actualiza el PR
```

### Cómo asignar

- En GitHub.com → Issues → Assignees → seleccionar **Copilot**
- Via CLI: `gh issue assign <number> --assignee @copilot`
- Via VS Code: en el panel de issues, asignar a Copilot

### Personalización del Coding Agent

El agente lee estos archivos del repo para adaptarse:

| Archivo | Propósito |
|---|---|
| `.github/copilot-instructions.md` | Instrucciones generales del proyecto |
| `.github/COPILOT_CODING_AGENT.md` | Instrucciones específicas para el coding agent |
| `.github/workflows/copilot-setup-steps.yml` | Setup del entorno (instalar deps, configurar) |
| `AGENTS.md` | Instrucciones multi-agente |

### Limitaciones conocidas

- Solo funciona con repos en GitHub.com (no GitLab, Bitbucket)
- El agent no puede hacer `git push --force` ni operaciones destructivas
- Acceso a internet durante la ejecución está limitado (configurable)
- Máximo N horas de ejecución por tarea (varía según plan)

---

## 13. Copilot Extensions

Extensiones publicadas en el GitHub Marketplace que agregan herramientas especializadas como contexto en el chat.

### Invocación

```
@docker Crea un Dockerfile para esta aplicación Python
@azure ¿Cuánto cuesta desplegar esto en App Service?
@sentry ¿Cuáles son los errores más frecuentes este mes?
@jira Crea un ticket para este bug
```

### Extensiones populares 2026

| Extension | Para qué |
|---|---|
| `@docker` | Gestión de imágenes, containers, compose |
| `@azure` | Recursos y servicios de Azure |
| `@github` | Búsqueda avanzada en GitHub, issues, PRs |
| `@sentry` | Monitoreo de errores en producción |
| `@datadog` | Métricas, logs, alertas |
| `@terraform` | Infraestructura como código |

### Desarrollar una Copilot Extension

Las extensiones se construyen como GitHub Apps con endpoints que implementan el protocolo de agente de Copilot. Ver: [docs.github.com/en/copilot/building-copilot-extensions](https://docs.github.com/en/copilot/building-copilot-extensions).

---

## 14. Copilot para PRs y Code Review

### Pull Request Summary

Copilot puede generar automáticamente la descripción de un PR:
- En GitHub.com: ícono de Copilot en el campo Description del PR
- Incluye: resumen de cambios, archivos afectados, posibles impactos

### Code Review automático

```
gh pr review --copilot    → Copilot revisa el PR desde la CLI
```

En GitHub.com → PR → `Review with Copilot` analiza:
- Posibles bugs y errores lógicos
- Problemas de seguridad (OWASP Top 10)
- Violaciones de las instrucciones del workspace
- Sugerencias de mejora con código alternativo

### Comentarios inteligentes en PRs

Copilot puede responder a comentarios de revisión en PRs y actualizar el código directamente desde la interfaz de GitHub.

---

## 15. Inline Chat y Quick Chat

### Inline Chat (en el editor)

```
Ctrl+I (Windows/Linux) / Cmd+I (Mac)
```

Abre un chat directamente en la línea/bloque seleccionado. Comandos especiales:

| Comando | Acción |
|---|---|
| `/explain` | Explica el código seleccionado |
| `/fix` | Corrige errores en la selección |
| `/doc` | Genera documentación (docstring, JSDoc, etc.) |
| `/tests` | Genera tests para la función seleccionada |
| `/simplify` | Simplifica código complejo |
| `/generate` | Genera código desde descripción natural |

> **Novedad 2026:** El inline chat ahora muestra un **diff visual** antes de aplicar cambios, con botones Accept/Reject por bloque.

### Quick Chat

```
Ctrl+Shift+Alt+L (Windows/Linux)
```

Abre un chat flotante sin abandonar el editor. Ideal para preguntas rápidas sin cambiar de contexto.

### Next Edit Suggestion (NES)

Después de una edición, Copilot anticipa el siguiente cambio lógico y lo muestra como sugerencia inline. Se acepta con `Tab`.

---

## 16. Slash Commands de referencia

### Comandos globales de VS Code

| Comando | Descripción |
|---|---|
| `/explain` | Explica código o concepto |
| `/fix` | Corrige el problema indicado o detectado |
| `/tests` | Genera tests para el código seleccionado |
| `/doc` | Genera documentación |
| `/new` | Crea un nuevo proyecto o archivo scaffold |
| `/api` | Consulta documentación de API |
| `/simplify` | Simplifica código |
| `/init` | Inicializa `copilot-instructions.md` para el workspace |
| `/create-agent` | Genera un `.agent.md` |
| `/create-prompt` | Genera un `.prompt.md` |
| `/create-skill` | Genera un `SKILL.md` |
| `/create-instruction` | Genera un `.instructions.md` |
| `/create-hook` | Genera configuración de hook |

### Comandos BMAD de este proyecto

| Comando | Descripción |
|---|---|
| `/bmad-help` | Ayuda y orientación de BMAD |
| `/bmad-dev` | Activa agente Dev (Amelia) |
| `/bmad-architect` | Activa agente Architect (Winston) |
| `/bmad-pm` | Activa agente Product Manager (John) |
| `/bmad-analyst` | Activa agente Analyst (Mary) |
| `/bmad-qa` | Activa agente QA (Quinn) |
| `/bmad-sm` | Activa agente Scrum Master (Bob) |
| `/bmad-ux` | Activa agente UX Designer (Sally) |
| `/bmad-techwriter` | Activa agente Tech Writer (Paige) |
| `/bmad-master` | Activa BMad Master Executor |
| `/goproduction` | Despliega edu-standalone → rama production |
| `/edu-*` | Comandos del módulo EDU (filminas, plan, etc.) |

---

## 17. Estrategias BMAD + Copilot

### Mapa de sinergia actualizado 2026

| Función BMAD | Función Copilot | Sinergia |
|---|---|---|
| Agentes BMAD (`.agent.md`) | Custom Agents | Los agentes BMAD ya usan el formato `.agent.md` nativo |
| Workflows BMAD (`.prompt.md`) | Prompt files | Expuestos como slash commands `/bmad-*` |
| Skills BMAD (`copilot-skill://`) | Agent Skills | Registrables como Agent Skills en `.github/skills/` |
| `copilot-instructions.md` con bloque BMAD | Always-on instructions | Config BMAD global del proyecto |
| Handoffs BMAD | Agent handoffs | Flujos PM→Architect→Dev→QA con botones de transición |
| Coding Agent (Cloud) | GitHub Issues → PR | Asignar issues de BMAD a Copilot para implementación autónoma |

### Estrategia 1: Hooks de validación y commit automático

Archivo `.github/hooks/bmad-session.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "type": "command",
        "command": "cd \"$WORKSPACE_ROOT\" && git status --short && echo '=== Sesión BMAD finalizada ==='",
        "timeout": 15
      }
    ],
    "PostToolUse": [
      {
        "type": "command",
        "command": "cd \"$WORKSPACE_ROOT\" && python scripts/validate-edu-paths.py \"$TOOL_INPUT_FILE_PATH\" 2>/dev/null || true",
        "condition": {
          "toolName": ["edit", "create"],
          "filePattern": "salida/**"
        },
        "timeout": 10
      }
    ]
  }
}
```

### Estrategia 2: Handoffs entre agentes BMAD

Agregar handoffs a los `.agent.md` de BMAD para flujos encadenados:

```markdown
handoffs:
  - label: "🏗️ Pasar a Arquitecto"
    agent: bmad-agent-bmm-architect
    prompt: "Revisá el PRD en salida/planning-artifacts/ y creá la arquitectura técnica para edu-standalone."
    send: false
  - label: "💻 Pasar a Dev"
    agent: bmad-agent-bmm-dev
    prompt: "Implementá la siguiente story según la arquitectura definida."
    send: false
```

### Estrategia 3: Instrucciones por fase y tipo de artefacto

```
.github/instructions/
├── edu-standalone.instructions.md     (applyTo: 'salida/edu-standalone/**')
├── planning-artifacts.instructions.md (applyTo: 'salida/planning-artifacts/**')
├── python.instructions.md             (applyTo: '**/*.py')
└── yaml-workflows.instructions.md     (applyTo: '_bmad/**/*.yaml')
```

Ejemplo `edu-standalone.instructions.md`:
```markdown
---
applyTo: 'salida/edu-standalone/**'
---
- Todos los artefactos EDU van en salida/edu-standalone/
- Los agentes EDU en _edu/agents/, workflows en _edu/workflows/
- NUNCA crear archivos EDU fuera de salida/edu-standalone/
- Los prompts EDU usan prefijo /edu-* y van en .github/prompts/
```

### Estrategia 4: Agent Skills formales para BMAD

Registrar capacidades BMAD como Agent Skills portables:

```
.github/skills/
└── bmad-workflow/
    ├── SKILL.md
    └── templates/
        ├── agent-template.md
        └── workflow-template.yaml
```

`SKILL.md`:
```markdown
---
name: bmad-workflow
description: "Ejecuta workflows BMAD (PM, Architect, Dev, QA). Úsala cuando
             necesites planificar, diseñar, implementar o revisar artefactos del
             proyecto usando el método BMAD."
user-invocable: true
---
## Cómo usarla
1. Cargar _bmad/bmm/config.yaml
2. Identificar el agente BMAD adecuado
3. Ejecutar el workflow correspondiente
```

### Estrategia 5: Coding Agent para issues de EDU

Flujo para implementación autónoma:

```
SM (Bob) crea GitHub Issues con stories de edu-standalone
↓
Asignar issue a Copilot como assignee
↓
Copilot lee .github/copilot-instructions.md + reglas EDU
↓
Implementa en branch feature/story-XXX
↓
Abre PR → Dev Agent (Amelia) revisa
↓
QA Agent (Quinn) aprueba
↓
Merge a main → GitHub Actions despliega
```

### Estrategia 6: Sesiones paralelas para revisión cruzada

```
Sesión A: Dev Agent (Amelia) implementando story actual
Sesión B: QA Agent (Quinn) revisando story anterior
Sesión C: Architect (Winston) documentando decisiones técnicas
```

Cada sesión puede usar un modelo diferente optimizado para la tarea.

### Estrategia 7: Plan Agent para epics grandes

```
/bmad-pm → John genera PRD
↓
Cambiar a Plan mode
↓
"Crea el plan de implementación para el Epic edu-slideshow-pipeline"
↓
Plan genera checklist con archivos y dependencias
↓
Aprobar plan → delegar a Agent mode o Cloud Agent
```

---

## 18. Mejores prácticas para prompts, agentes y workflows

### Principios generales

1. **Sé específico en las instrucciones**: instrucciones vagas producen resultados inconsistentes. Indicar siempre: formato de salida, dónde guardar archivos, qué herramientas usar.

2. **Una responsabilidad por agente**: evitar agentes que hacen todo. Mejor `pm-agent`, `dev-agent`, `qa-agent` separados con handoffs que un súper-agente monolítico.

3. **Instrucciones cortas y modulares**: el `copilot-instructions.md` global debe ser conciso. El detalle va en `.instructions.md` por contexto o en el agente específico.

4. **Modelo por tarea**: usar Haiku/Flash para tareas rápidas (completions, revisiones), Sonnet/GPT-4o para diseño y análisis, o3-mini para algoritmos y lógica.

5. **Variables en lugar de hardcode**: usar `${input:var}` en prompts y `${env:VAR}` en hooks/MCP para evitar valores fijos.

### Diseño de prompts efectivos

```markdown
---
description: "Tarea muy específica con salida esperada definida"
agent: agent
model: "claude-sonnet-4-7 (copilot)"
tools: ['read', 'edit', 'search']
---

## Contexto
${file:.github/copilot-instructions.md}

## Tarea
[Verbo imperativo] + [objeto] + [restricciones] + [formato de salida]

## Ejemplo esperado
[Mostrar un ejemplo de lo que se espera, si aplica]

## Restricciones
- No modificar archivos fuera de [ruta específica]
- Formato: [especificar]
- Idioma: español
```

### Diseño de agentes robustos

```markdown
---
name: "Nombre descriptivo de rol"
description: "Qué hace este agente. Úsalo cuando necesites X, Y o Z."
tools: ['read', 'search']            # mínimo necesario
model: ["claude-sonnet-4-7 (copilot)", "gpt-4o (copilot)"]  # con fallback
user-invocable: true
handoffs:
  - label: "Siguiente paso lógico"   # siempre proveer handoff de salida
    agent: siguiente-agente
    prompt: "Contexto específico para el siguiente agente"
    send: false
---

# Rol
[Descripción clara del rol y responsabilidades]

# Comportamiento
- [Comportamiento 1]
- [Comportamiento 2]

# Lo que NUNCA hace este agente
- [Restricción 1]
- [Restricción 2]

# Formato de salida
[Especificar formato esperado para los outputs]
```

### Anti-patrones a evitar

| Anti-patrón | Problema | Solución |
|---|---|---|
| `copilot-instructions.md` de 500+ líneas | Se trunca, degrada las instrucciones | Dividir en `.instructions.md` con `applyTo` |
| Agente con `tools: ['*']` | Acceso no controlado, comportamientos inesperados | Declarar solo las herramientas necesarias |
| Prompt sin `agent` ni `tools` | Hereda defaults del modo activo, inconsistente | Especificar siempre `agent` y `tools` |
| Instrucciones contradictorias entre archivos | El modelo no sabe cuál priorizar | Usar `applyTo` preciso para separar contextos |
| Hooks sin `timeout` | El hook puede colgar la sesión indefinidamente | Siempre poner `timeout` en segundos |
| Hardcodear secretos en archivos de config | Vulnerabilidad de seguridad | Usar `${env:VARIABLE}` siempre |
| Agente sin handoffs | El usuario queda atrapado en un agente | Siempre definir handoffs hacia el siguiente paso |

### Checklist antes de hacer deploy de un agente/prompt

- [ ] `name` y `description` son claros y descriptivos
- [ ] `tools` restringido al mínimo necesario
- [ ] `model` especificado con fallback
- [ ] Sin secretos hardcodeados (usar `${env:}`)
- [ ] Instrucciones en el idioma del proyecto (español)
- [ ] Al menos un `handoff` hacia el siguiente paso del flujo
- [ ] Probado con casos edge (input vacío, archivos no encontrados)
- [ ] Guardado en la ruta correcta (ver tabla de rutas EDU)

---

## Referencias

- [VS Code Copilot Overview](https://code.visualstudio.com/docs/copilot/overview)
- [Customize AI in VS Code](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Hooks (Preview→GA)](https://code.visualstudio.com/docs/copilot/customization/hooks)
- [MCP Servers en VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
- [Workspace Context](https://code.visualstudio.com/docs/copilot/reference/workspace-context)
- [Context Variables](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features#context-variables)
- [Copilot Coding Agent](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent)
- [Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions)
- [Agent Skills Standard](https://agentskills.io/)
- [Awesome Copilot (comunidad)](https://github.com/github/awesome-copilot)
- [MCP Servers populares](https://github.com/modelcontextprotocol/servers)
