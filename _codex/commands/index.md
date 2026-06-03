# Codex Command Index

This index maps Copilot slash commands to Codex execution routes. Copilot prompt files live in `.github/prompts/`; use them as command specs when present.

## Anytime

| Command | Agent | Workflow or action | Copilot prompt |
|---|---|---|---|
| `/edu-help` | `course-planner` | contextual guidance | `.github/prompts/edu-help.prompt.md` |
| `/edu-status` | `course-planner` | inspect active course/topic | `.github/prompts/edu-status.prompt.md` |
| `/edu-update-context` | `course-planner` | `_edu/workflows/update-copilot-context/workflow.md` | `.github/prompts/edu-update-context.prompt.md` |
| `/edu-memory-search` | any | `python scripts/edu_memory.py search` | `.github/prompts/edu-memory-search.prompt.md` |
| `/edu-knowledge-search` | any | `python scripts/knowledge_base.py search` | `.github/prompts/edu-knowledge-search.prompt.md` |

## Course Setup and Planning

| Command | Agent | Workflow | Copilot prompt |
|---|---|---|---|
| `/edu-start-course` | `course-planner` | `_edu/workflows/load-official-plan/workflow.md` | `.github/prompts/edu-start-course.prompt.md` |
| `/edu-build-course` | `course-planner` | `_edu/workflows/build-course-from-materials/workflow.md` or `_edu/workflows/build-course-from-research/workflow.md` | `.github/prompts/edu-build-course.prompt.md` |
| `/edu-check-coverage` | `plan-coverage-checker` | `_edu/workflows/check-coverage/workflow.md` | `.github/prompts/edu-check-coverage.prompt.md` |
| `/edu-adaptive-replan` | `course-planner` | `_edu/workflows/adaptive-replan/workflow.md` | `.github/prompts/edu-adaptive-replan.prompt.md` |
| `/edu-propose-curriculum-change` | `curriculum-reviewer` | `_edu/workflows/curriculum-change/workflow.md` | `.github/prompts/edu-propose-curriculum-change.prompt.md` |

## Topic Cycle

| Command | Agent | Workflow | Copilot prompt |
|---|---|---|---|
| `/edu-topic` | `topic-designer` | `_edu/workflows/topic-cycle/workflow.md` | `.github/prompts/edu-topic.prompt.md` |
| `/edu-design-topic` | `topic-designer` | `_edu/workflows/topic-cycle/workflow.md` | `.github/prompts/edu-design-topic.prompt.md` |
| `/edu-approve-design` | `course-planner` | `_edu/workflows/topic-cycle/workflow.md` | `.github/prompts/edu-approve-design.prompt.md` |
| `/edu-create-class` | `class-writer` | `_edu/workflows/topic-cycle/workflow.md` | `.github/prompts/edu-create-class.prompt.md` |
| `/edu-create-study-guide` | `study-guide-writer` | `_edu/workflows/topic-cycle/workflow.md` | `.github/prompts/edu-create-study-guide.prompt.md` |
| `/edu-create-teacher-guide` | `class-writer` | `_edu/workflows/create-teacher-guide/workflow.md` | `.github/prompts/edu-create-teacher-guide.prompt.md` |
| `/edu-create-tp` | `tp-designer` | `_edu/workflows/topic-cycle/workflow.md` | `.github/prompts/edu-create-tp.prompt.md` |
| `/edu-quality` | quality agents | `_edu/workflows/quality-loops/workflow.md` | `.github/prompts/edu-quality.prompt.md` |
| `/edu-test-topic` | `student-simulator` | `_edu/workflows/pedagogical-testing/workflow.md` | `.github/prompts/edu-test-topic.prompt.md` |
| `/edu-close-topic` | `course-planner` | `_edu/workflows/topic-cycle/workflow.md` | `.github/prompts/edu-close-topic.prompt.md` |
| `/edu-reopen-topic` | `course-planner` | `_edu/workflows/reopen-topic/workflow.md` | `.github/prompts/edu-reopen-topic.prompt.md` |

## Slides and Publishing

| Command | Agent | Workflow or script | Copilot prompt |
|---|---|---|---|
| `/edu-slides-designer` | `slides-designer` | update `_edu/slides-config.yaml` | `.github/prompts/edu-slides-designer.prompt.md` |
| `/edu-publish-slides` | `slides-publisher` | topic-cycle Step 9.5 plus `scripts/slides_pipeline.py` | `.github/prompts/edu-publish-slides.prompt.md` |
| `/edu-test-pipeline` | `test-runner` | `python scripts/test_pipeline.py` | `.github/prompts/edu-test-pipeline.prompt.md` |
| `/edu-check-accessibility` | validator | `python scripts/validate_accessibility.py` | `.github/prompts/edu-check-accessibility.prompt.md` |
| `/edu-check-composition` | validator | `python scripts/validate_slide_composition.py` | `.github/prompts/edu-check-composition.prompt.md` |

## Extended Commands

For less frequent commands such as `/edu-create-exam`, `/edu-create-pbl`, `/edu-run-pipeline`, `/edu-build-kg`, `/edu-adaptive-session`, and `/edu-verify-facts`, read `WORKFLOW_PROMPT_MAP.md` and then open the corresponding `.github/prompts/edu-*.prompt.md`.

## Codex Execution Checklist

1. Read `AGENTS.md`.
2. Match the command to this index.
3. Read the Copilot prompt and canonical workflow.
4. Read the owner agent if persona or domain rules matter.
5. Inspect existing artifacts before editing.
6. Apply focused changes.
7. Run the relevant validator or explain why it was not run.
