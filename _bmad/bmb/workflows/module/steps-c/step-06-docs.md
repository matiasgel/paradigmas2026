---
name: 'step-06-docs'
description: 'Generate README.md, TODO.md, and docs/ folder'

nextStepFile: './step-07-complete.md'
buildTrackingFile: '{bmb_creations_output_folder}/modules/module-build-{module_code}.md'
targetLocation: '{build_tracking_targetLocation}'
---

# Step 6: Documentation

## STEP GOAL:

Generate README.md, TODO.md, and user documentation in docs/ folder for the module.

## MANDATORY EXECUTION RULES:

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ Speak in `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Module Builder** — documentation creator
- ✅ README is the user's first impression
- ✅ TODO tracks remaining work
- ✅ docs/ provides user-facing documentation

---

## MANDATORY SEQUENCE

### 1. Generate README.md

Create `{targetLocation}/README.md`:

```markdown
# {module_display_name}

{brief_header}

{subheader}

---

## Overview

{module_overview_from_brief}

---

## Installation

```bash
bmad install {module_code}
```

---

## Quick Start

{quick_start_from_brief}

**For detailed documentation, see [docs/](docs/).**

---

## Components

### Agents

{agent_list_from_brief}

### Workflows

{workflow_list_from_brief}

---

## Configuration

The module supports these configuration options (set during installation):

{config_variables_from_module_yaml}

---

## Module Structure

```
{module_code}/
├── module.yaml
├── README.md
├── TODO.md
├── docs/
│   ├── getting-started.md
│   ├── agents.md
│   ├── workflows.md
│   └── examples.md
├── agents/
└── workflows/
```

---

## Documentation

For detailed user guides and documentation, see the **[docs/](docs/)** folder:
- [Getting Started](docs/getting-started.md)
- [Agents Reference](docs/agents.md)
- [Workflows Reference](docs/workflows.md)
- [Examples](docs/examples.md)

---

## Development Status

This module is currently in development. The following components are planned:

- [ ] Agents: {agent_count} agents
- [ ] Workflows: {workflow_count} workflows

See TODO.md for detailed status.

---

## Author

Created via BMAD Module workflow

---

## License

Part of the BMAD framework.
```

### 2. Generate TODO.md

Create `{targetLocation}/TODO.md`:

```markdown
# TODO: {module_display_name}

Development roadmap for {module_code} module.

---

## Agents to Build

{for each agent}
- [ ] {agent_name} ({agent_title})
  - Use: `bmad:bmb:agents:agent-builder`
  - Spec: `agents/{agent_name}.spec.md`

---

## Workflows to Build

{for each workflow}
- [ ] {workflow_name}
  - Use: `bmad:bmb:workflows:workflow` or `/workflow`
  - Spec: `workflows/{workflow_name}/{workflow_name}.spec.md`

---

## Installation Testing

- [ ] Test installation with `bmad install`
- [ ] Verify module.yaml prompts work correctly
- [ ] Verify all agents and workflows are discoverable

---

## Documentation

- [ ] Complete README.md with usage examples
- [ ] Enhance docs/ folder with more guides
- [ ] Add troubleshooting section
- [ ] Document configuration options

---

## Next Steps

1. Build agents using create-agent workflow
2. Build workflows using create-workflow workflow
3. Test installation and functionality
4. Iterate based on testing

---

_Last updated: {date}_
```

### 3. Create docs/ Folder

Create `{targetLocation}/docs/` folder with user documentation:

### 3.1. getting-started.md

```markdown
# Getting Started with {module_display_name}

Welcome to {module_code}! This guide will help you get up and running.

---

## What This Module Does

{module_purpose_from_brief}

---

## Installation

If you haven't installed the module yet:

```bash
bmad install {module_code}
```

Follow the prompts to configure the module for your needs.

---

## First Steps

{first_steps_from_brief}

---

## Common Use Cases

{common_use_cases_from_brief}

---

## What's Next?

- Check out the [Agents Reference](agents.md) to meet your team
- Browse the [Workflows Reference](workflows.md) to see what you can do
- See [Examples](examples.md) for real-world usage

---

## Need Help?

If you run into issues:
1. Check the troubleshooting section in examples.md
2. Review your module configuration
3. Consult the broader BMAD documentation
```

### 3.2. agents.md

```markdown
# Agents Reference

{module_code} includes {agent_count} specialized agents:

---

{for each agent}
## {agent_title}

**ID:** `{agent_id}`
**Icon:** {agent_icon}

**Role:**
{agent_role_from_spec}

**When to Use:**
{when_to_use_from_spec}

**Key Capabilities:**
{agent_capabilities_from_spec}

**Menu Trigger(s):**
{menu_triggers_from_spec}

---
```

### 3.3. workflows.md

```markdown
# Workflows Reference

{module_code} includes {workflow_count} workflows:

---

{for each workflow}
## {workflow_title}

**ID:** `{workflow_id}`
**Workflow:** `{workflow_name}`

**Purpose:**
{workflow_purpose_from_spec}

**When to Use:**
{when_to_use_from_spec}

**Key Steps:**
{workflow_steps_outline_from_spec}

**Agent(s):**
{associated_agents_from_spec}

---
```

### 3.4. examples.md

```markdown
# Examples & Use Cases

This section provides practical examples for using {module_display_name}.

---

## Example Workflows

{example_workflows_from_brief}

---

## Common Scenarios

{common_scenarios_from_brief}

---

## Tips & Tricks

{tips_from_brief}

---

## Troubleshooting

### Common Issues

{troubleshooting_from_brief}

---

## Getting More Help

- Review the main BMAD documentation
- Check module configuration in module.yaml
- Verify all agents and workflows are properly installed
```

### 4. For Standalone Modules: Generate Standalone Package Docs

**ONLY if moduleType == Standalone:** Generate the user-facing documentation for the deployable standalone package.

#### 4.1. Standalone README.md

Create `{standalone_package_location}/README.md` — user-facing, minimal, orientado al docente/usuario final:

```markdown
# {module_display_name}

{module_header}

## Quick Start

1. Cloná o copiá este directorio como raíz de tu proyecto
2. Abrí VS Code
3. Configurá el módulo editando `_{module_code}/config.yaml`
4. Usá `/{module_code}-start` para comenzar

## Estructura del Proyecto

```
tu-proyecto/
├── .github/
│   ├── copilot-instructions.md    ← Contexto para Copilot
│   ├── agents/                    ← Agentes (@{module_code}-agent-nombre)
│   └── prompts/                   ← Slash commands (/{module_code}-*)
├── .vscode/
│   └── settings.json              ← Habilita prompt files
├── _{module_code}/
│   ├── config.yaml                ← Configuración del módulo
│   ├── module-help.csv            ← Índice de comandos
│   ├── agents/                    ← Definiciones completas de agentes
│   └── workflows/                 ← Definiciones de workflows
└── {module_output_folder}/        ← Output generado (creado en runtime)
```

## Agentes Disponibles

{agent_table_from_brief}

## Slash Commands

Escribí `/{module_code}-` para ver los comandos disponibles.

{slash_commands_by_phase_from_brief}
```

#### 4.2. Standalone `.github/copilot-instructions.md`

Create `{standalone_package_location}/.github/copilot-instructions.md` — SOLO el bloque del módulo (sin BMAD):

```markdown
<!-- {MODULE_CODE_UPPER}:START -->
# {module_display_name}

## Descripción

{module_header}
{module_subheader}

## Configuración del Proyecto

- Cargar siempre `_{module_code}/config.yaml` antes de cualquier activación de agente o ejecución de workflow
- Almacenar todos los campos como variables de sesión
- La variable `{project-root}` se resuelve a la raíz del workspace en runtime

## Estructura

- **Configuración**: `_{module_code}/config.yaml`
- **Agentes**: `_{module_code}/agents/`
- **Workflows**: `_{module_code}/workflows/`
- **Comandos**: `_{module_code}/module-help.csv`

{phases_section_from_brief}

## Agentes Disponibles

{agents_summary_from_brief}

## Slash Commands

Escribí `/{module_code}-` en Copilot Chat para ver todos los comandos disponibles.
Los agentes están disponibles como `@{module_code}-agent-nombre` en el dropdown de agentes.

## Restricciones Críticas

{critical_restrictions_from_brief}
<!-- {MODULE_CODE_UPPER}:END -->
```

#### 4.3. Standalone `.vscode/settings.json`

Create `{standalone_package_location}/.vscode/settings.json`:

```json
{
  "chat.promptFiles": true,
  "chat.promptFilesLocations": {
    ".github/prompts": true
  }
}
```

### 5. Update Build Tracking

Update `{buildTrackingFile}`:
- Add 'step-06-docs' to stepsCompleted
- Note: README.md, TODO.md, docs/ folder, and standalone package docs created (if Standalone)

### 6. Report Success

"**✓ Documentation created:**"

- `{targetLocation}/README.md` — module development overview
- `{targetLocation}/TODO.md` — development roadmap
- `{targetLocation}/docs/` — developer documentation folder

If Standalone also:
- `{standalone_package_location}/README.md` — user-facing standalone README
- `{standalone_package_location}/.github/copilot-instructions.md` — module-only Copilot context
- `{standalone_package_location}/.vscode/settings.json` — prompt files enablement

### 7. MENU OPTIONS

**Select an Option:** [C] Continue

- IF C: Update tracking, load `{nextStepFile}`
- IF Any other: Help, then redisplay menu

---

## Success Metrics

✅ README.md created with all sections (dev artifacts)
✅ TODO.md created with agent/workflow checklist
✅ docs/ folder created with user documentation
✅ For Standalone: standalone package docs generated at `{standalone_package_location}`
✅ Build tracking updated
