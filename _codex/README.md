# Codex Adapter for EDU

This folder initializes an agent/workflow/command structure for Codex based on the existing GitHub Copilot structure.

The goal is to make Codex usable with the same mental model:

- **Agents** answer "who should do this?"
- **Workflows** answer "what process should be followed?"
- **Commands** answer "what shortcut did the teacher invoke?"

## Source of Truth

Do not duplicate long instructions here unless Codex needs a small adapter note. The canonical content remains:

- Agents: `_edu/agents/`
- Workflows: `_edu/workflows/`
- Copilot agents: `.github/agents/`
- Copilot prompts: `.github/prompts/`
- Prompt to workflow map: `WORKFLOW_PROMPT_MAP.md`

## Structure

```text
_codex/
├── agents/
│   └── index.md
├── workflows/
│   └── index.md
├── commands/
│   └── index.md
└── templates/
    ├── agent-card.md
    ├── command-card.md
    └── workflow-card.md
```

## Use

1. Match the user's request to a command, agent, or workflow.
2. Open the matching `_codex/*/index.md` entry.
3. Read the canonical source files referenced there.
4. Execute the work in the repository, keeping generated artifacts in `salida/`.

The `.codex/` directory in this checkout is currently not writable from the sandbox, so this adapter starts in `_codex/` and is anchored by the root `AGENTS.md`.
