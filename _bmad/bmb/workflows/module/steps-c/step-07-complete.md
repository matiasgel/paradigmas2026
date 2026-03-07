---
name: 'step-07-complete'
description: 'Finalize, offer to run validation'

buildTrackingFile: '{bmb_creations_output_folder}/modules/module-build-{module_code}.md'
targetLocation: '{build_tracking_targetLocation}'
moduleHelpGenerateWorkflow: '../module-help-generate.md'
validationWorkflow: '../steps-v/step-01-validate.md'
moduleHelpCsvFile: '{build_tracking_targetLocation}/module-help.csv'
---

# Step 7: Complete

## STEP GOAL:

Finalize the module build, update tracking, and offer to run validation.

## MANDATORY EXECUTION RULES:

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- ✅ Speak in `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Module Builder** — completing the build
- ✅ Celebrate what was created
- ✅ Guide next steps

---

## MANDATORY SEQUENCE

### 1. Generate module-help.csv

"**🎯 Generating module-help.csv...**"

Load and execute the module-help-generate workflow:
```
{moduleHelpGenerateWorkflow}
```

**Set these variables before loading:**
- `modulePath: {targetLocation}`
- `moduleYamlFile: {targetLocation}/module.yaml`
- `moduleHelpCsvFile: {targetLocation}/module-help.csv`
- `workflowsDir: {targetLocation}/workflows`
- `agentsDir: {targetLocation}/agents`

**What this does:**
- Scans all workflows in `{workflowsDir}/`
- Scans all agents in `{agentsDir}/`
- Generates `{moduleHelpCsvFile}` with proper structure:
  - `anytime` entries at top (no sequence)
  - Phased entries below (phase-1, phase-2, etc.)
  - Agent-only entries have empty `workflow-file`

**Wait for workflow completion** before proceeding.

### 2. Final Build Summary

"**🎉 Module structure build complete!**"

**Module:** {moduleName} ({moduleCode})
**Type:** {moduleType}
**Location:** {targetLocation}

**What was created:**

| Component | Count | Location |
|-----------|-------|----------|
| Agent specs | {count} | agents/ |
| Workflow specs | {count} | workflows/ |
| Configuration | 1 | module.yaml |
| Help Registry | 1 | module-help.csv |
| Documentation | 2 | README.md, TODO.md |

### 3. Update Build Tracking

Update `{buildTrackingFile}`:
```yaml
---
moduleCode: {module_code}
moduleName: {name}
moduleType: {type}
targetLocation: {location}
standalonePackageLocation: {standalone_package_location}  # solo si Standalone
stepsCompleted: ['step-01-load-brief', 'step-02-structure', 'step-03-config', 'step-04-agents', 'step-05-workflows', 'step-06-docs', 'step-07-complete']
created: {created_date}
completed: {date}
status: COMPLETE
---
```

### 3b. For Standalone Modules: Finalize Standalone Package

**ONLY if moduleType == Standalone:**

"**📦 Finalizing standalone package at `{standalone_package_location}`...**"

Poblar la estructura standalone con los artefactos construidos:

**`_{module_code}/` dentro del standalone:**
- Copiar agents finales → `{standalone_package_location}/_{module_code}/agents/`
- Copiar workflows finales → `{standalone_package_location}/_{module_code}/workflows/`
- Generar `{standalone_package_location}/_{module_code}/config.yaml` a partir de `module.yaml`: convertir cada `variable_name.default` en un campo YAML comentado con el prompt como guía. Omitir campos solo-installer (`code`, `name`, `header`, `subheader`, `default_selected`). Mantener variables de runtime. Agregar sección `# --- Module ---` con `code`, `name`, `header`, `subheader` como campos de solo-lectura.
- Copiar `{targetLocation}/module-help.csv` → `{standalone_package_location}/_{module_code}/module-help.csv`

**`.github/agents/` dentro del standalone — formato EXACTO:**

Para cada agente visible (no-interno), crear `{standalone_package_location}/.github/agents/{module_code}-agent-{agent_name}.agent.md`.

Formato obligatorio (usar `chatagent` code fence — NO frontmatter `---` directo):

````
```chatagent
---
description: '{agent_title_with_icon}: {agent_role_brief}'
tools: ['read', 'edit', 'search', 'execute']
---

You must fully embody this agent's persona and follow all activation instructions exactly as specified.

<agent-activation CRITICAL="TRUE">
1. LOAD the FULL agent file from {project-root}/_{module_code}/agents/{agent_name}.md
2. READ its entire contents - this contains the complete agent persona, menu, and instructions
3. FOLLOW every step in the <activation> section precisely
4. DISPLAY the welcome/greeting as instructed
5. PRESENT the numbered menu
6. WAIT for user input before proceeding
</agent-activation>
```
````

**`.github/prompts/` dentro del standalone — formato EXACTO:**

Para cada entrada en `module-help.csv`, crear `{standalone_package_location}/.github/prompts/{module_code}-{slash_command_name}.prompt.md`.

Formato obligatorio (usar `prompt` code fence — NO frontmatter `---` directo):

**Para comandos CON workflow-file:**
````
```prompt
---
description: '{module_display_name} {phase_label}: {command_description}'
agent: 'agent'
tools: ['read', 'edit', 'search']
---

1. Load {project-root}/_{module_code}/config.yaml and store ALL fields as session variables
2. Load and follow the workflow at {project-root}/{workflow-file}
3. Purpose: {command_description_detailed}
```
````

**Para comandos SIN workflow-file (agent-only, anytime):**
````
```prompt
---
description: '{module_display_name}: {command_description}'
agent: 'agent'
tools: ['read', 'search']
---

1. Load {project-root}/_{module_code}/config.yaml and store ALL fields as session variables
2. {natural_language_instruction_matching_command_description}
```
````

Derivat el `slash_command_name` del campo `command` en module-help.csv: reemplazar `_` por `-` (e.g. `edu_design_topic` → `edu-design-topic`).
Derivat el `phase_label` de la columna `phase` (e.g. `phase-3` → `Fase 3`).
Derivat el nombre de tools según si el comando es read-only o write-capable (validaciones → `['read', 'search']`; generadores/fixers → `['read', 'edit', 'search']`).

"**✅ Standalone package complete at `{standalone_package_location}`**"

Estructura final generada:
```
{standalone_package_location}/
├── .github/
│   ├── copilot-instructions.md
│   ├── agents/   ({agent_count} agentes)
│   └── prompts/  ({prompt_count} slash commands)
├── .vscode/settings.json
├── README.md
└── _{module_code}/
    ├── config.yaml
    ├── module-help.csv
    ├── agents/   ({agent_count} archivos)
    └── workflows/ ({workflow_count} carpetas)
```

### 4. Next Steps

"**Your module structure is ready! Here's what to do next:**"

For Standalone:
1. **Revisar el paquete standalone** — Verificar `{standalone_package_location}`
2. **Distribuir** — El directorio `{standalone_package_location}` es el deployable que el usuario copia como raíz de su proyecto
3. **Iterar** — Refiná agentes y workflows y regenerá el standalone con este proceso

For all types:
1. **Review the build** — Check {targetLocation}
2. **Build agents** — Use `bmad:bmb:agents:agent-builder` for each agent spec
3. **Build workflows** — Use `bmad:bmb:workflows:workflow` for each workflow spec
4. **Test installation** — Run `bmad install {module_code}`
5. **Iterate** — Refine based on testing

### 5. Offer Validation

"**Would you like to run validation on the module structure?**"

Validation checks:
- File structure compliance
- module.yaml correctness
- Spec completeness
- Installation readiness

### 6. MENU OPTIONS

**Select an Option:** [V] Validate Module [D] Done

#### EXECUTION RULES:

- ALWAYS halt and wait for user input

#### Menu Handling Logic:

- IF V: Load `{validationWorkflow}` to run validation
- IF D: Celebration message, workflow complete
- IF Any other: Help user, then redisplay menu

### 7. Completion Message (if Done selected)

"**🚀 You've built a module structure for BMAD!**"

"**Module:** {moduleName} ({moduleCode})"
"**Location:** {targetLocation}"
"**Status:** Ready for agent and workflow implementation"

"**The journey from idea to installable module continues:**
- Agent specs → create-agent workflow
- Workflow specs → create-workflow workflow
- Full module → `bmad install`

"**Great work! Let's build something amazing.** ✨"

---

## Success Metrics

✅ module-help.csv generated at module root
✅ Build tracking marked COMPLETE
✅ Summary presented to user
✅ Next steps clearly explained
✅ Validation offered (optional)
