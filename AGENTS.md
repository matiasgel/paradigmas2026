# Codex Project Instructions

This repository uses EDU, a multi-agent teaching-production system. Treat `_edu/` and `.github/` as the canonical sources, and use `_codex/` as the Codex-facing adapter layer.

## Project Shape

- `_edu/agents/`: full agent definitions and personas.
- `_edu/workflows/`: canonical workflow procedures by phase.
- `.github/agents/`: GitHub Copilot agent wrappers.
- `.github/prompts/`: GitHub Copilot slash-command prompts.
- `_codex/`: Codex-oriented indexes and command cards that map back to the canonical sources.
- `salida/cursadas/{course_id}/`: course outputs.

## Operating Rules

- Read `_edu/config.yaml` before executing EDU workflows.
- Respect the active topic in `_edu/active-topic.yaml` when working on topic artifacts.
- Do not modify `salida/cursadas/2026/plan-minimo.md` unless the user explicitly asks and confirms that the institutional plan can change.
- Prefer updating topic artifacts in the active topic folder:
  `salida/cursadas/2026/temas/11-estructuras-control/`.
- When asked for a Copilot command such as `/edu-create-class`, use `_codex/commands/index.md` to find the mapped agent and workflow, then read the referenced canonical files.
- When asked to behave as an EDU agent, read the matching file in `_edu/agents/` and follow its persona and rules as far as they fit Codex's current tool environment.

## Codex Adapter Convention

Codex command cards live in `_codex/commands/`. They are not separate sources of truth; each card should point to:

- the Copilot prompt in `.github/prompts/`
- the owner agent in `_edu/agents/`
- the workflow in `_edu/workflows/`
- expected inputs and outputs

If a command has no individual card yet, use `_codex/commands/index.md` plus `WORKFLOW_PROMPT_MAP.md`.
