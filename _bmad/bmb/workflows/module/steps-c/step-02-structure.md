---
name: 'step-02-structure'
description: 'Create directory structure based on module type'

nextStepFile: './step-03-config.md'
moduleStandardsFile: '../data/module-standards.md'
buildTrackingFile: '{bmb_creations_output_folder}/modules/module-build-{module_code}.md'
---

# Step 2: Directory Structure

## STEP GOAL:

Create the module directory structure based on the module type (Standalone/Extension/Global).

## MANDATORY EXECUTION RULES:

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ Speak in `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Module Builder** — creating the foundation
- ✅ Structure follows standards
- ✅ Confirm before creating

---

## MANDATORY SEQUENCE

### 1. Determine Target Location

Load `{moduleStandardsFile}` and determine location:

**IF Standalone:**
- Target (dev artifacts): `{bmb_creations_output_folder}/modules/{module_code}/`
- Standalone package: `{bmb_creations_output_folder}/{module_code}-standalone/`
- Store `standalone_package_location = {bmb_creations_output_folder}/{module_code}-standalone/`

**IF Extension:**
- Target: `{bmb_creations_output_folder}/modules/{base_module_code}/extensions/{extension_folder_name}/`
- Get base_module_code from brief
- extension_folder_name: unique name (e.g., `{base_module}-{feature}`)

**IF Global:**
- Target: `{bmb_creations_output_folder}/modules/{module_code}/`
- Will add `global: true` to module.yaml

### 2. Present Structure Plan

"**I'll create this directory structure:**"

For Standalone:
```
{bmb_creations_output_folder}/modules/{module_code}/  ← dev artifacts
├── module.yaml
├── README.md
├── agents/
│   └── {agent files}
└── workflows/
    └── {workflow folders}

{bmb_creations_output_folder}/{module_code}-standalone/  ← deployable package (step 7)
├── .github/
│   ├── copilot-instructions.md
│   ├── agents/                    ← {module_code}-agent-*.agent.md
│   └── prompts/                   ← {module_code}-*.prompt.md
├── .vscode/
│   └── settings.json
├── README.md                      ← user-facing
└── _{module_code}/
    ├── config.yaml
    ├── module-help.csv
    ├── agents/
    └── workflows/
```

"**Dev artifacts location:** {bmb_creations_output_folder}/modules/{module_code}/"
"**Standalone package location:** {standalone_package_location}"
"**Module type:** Standalone"

### 3. Confirm and Create

"**Shall I create the directory structure?**"

**IF confirmed:**

Create folders for dev artifacts:
- `{target_location}/agents/`
- `{target_location}/workflows/`

For Standalone, also create the package skeleton:
- `{standalone_package_location}/.github/agents/`
- `{standalone_package_location}/.github/prompts/`
- `{standalone_package_location}/.vscode/`
- `{standalone_package_location}/_{module_code}/agents/`
- `{standalone_package_location}/_{module_code}/workflows/`

### 4. Update Build Tracking

Update `{buildTrackingFile}`:
- Add 'step-02-structure' to stepsCompleted
- Set `targetLocation: {bmb_creations_output_folder}/modules/{module_code}/`
- If Standalone, set `standalonePackageLocation: {standalone_package_location}`
- Update status to IN_PROGRESS

### 5. Report Success

"**✓ Directory structure created at:** {target_location}"

### 6. MENU OPTIONS

**Select an Option:** [C] Continue

- IF C: Update tracking, load `{nextStepFile}`
- IF Any other: Help, then redisplay menu

---

## Success Metrics

✅ Directory structure created
✅ Location based on module type
✅ Folders: agents/, workflows/
✅ Build tracking updated
