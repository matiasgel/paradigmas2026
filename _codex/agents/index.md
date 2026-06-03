# Codex Agent Index

Codex should use these entries as routing cards. Full definitions live in `_edu/agents/`; Copilot wrappers live in `.github/agents/`.

## Visible Teaching Agents

| Codex handle | Copilot handle | Canonical agent | Main responsibility |
|---|---|---|---|
| `course-planner` | `@edu-agent-course-planner` | `_edu/agents/course-planner.md` | Orchestrate the course, coverage, replanning, closure |
| `topic-designer` | `@edu-agent-topic-designer` | `_edu/agents/topic-designer.md` | Design topic scope and class structure |
| `class-writer` | `@edu-agent-class-writer` | `_edu/agents/class-writer.md` | Write `minuta.md`, `filminas.md`, and teacher guide |
| `study-guide-writer` | `@edu-agent-study-guide-writer` | `_edu/agents/study-guide-writer.md` | Write autonomous student study guides |
| `tp-designer` | `@edu-agent-tp-designer` | `_edu/agents/tp-designer.md` | Design practical assignments and quizzes |
| `curriculum-reviewer` | `@edu-agent-curriculum-reviewer` | `_edu/agents/curriculum-reviewer.md` | Review curriculum changes with evidence |
| `academic-researcher` | `@edu-agent-academic-researcher` | `_edu/agents/academic-researcher.md` | Search and synthesize academic references |
| `slides-designer` | `@edu-agent-slides-designer` | `_edu/agents/slides-designer.md` | Maintain visual system and slide design rules |
| `slides-publisher` | `@edu-agent-slides-publisher` | `_edu/agents/slides-publisher.md` | Generate slide plans and publish slides |

## Quality Agents

| Codex handle | Copilot handle | Canonical agent | Main responsibility |
|---|---|---|---|
| `writing-validator` | `@edu-agent-writing-validator` | `_edu/agents/writing-validator.md` | Detect writing defects |
| `writing-fixer` | `@edu-agent-writing-fixer` | `_edu/agents/writing-fixer.md` | Apply writing corrections |
| `coherence-fixer` | `@edu-agent-coherence-fixer` | `_edu/agents/coherence-fixer.md` | Align artifacts across a topic |
| `reference-validator` | `@edu-agent-reference-validator` | `_edu/agents/reference-validator.md` | Validate citations and references |
| `academic-guardrail` | `@edu-agent-academic-guardrail` | `_edu/agents/academic-guardrail.md` | Enforce academic tone, density, and scope |

## Testing and Specialized Agents

| Codex handle | Copilot handle | Canonical agent | Main responsibility |
|---|---|---|---|
| `student-simulator` | `@edu-agent-student-simulator` | `_edu/agents/student-simulator.md` | Simulate student profiles |
| `plan-coverage-checker` | `@edu-agent-plan-coverage-checker` | `_edu/agents/plan-coverage-checker.md` | Verify plan coverage |
| `exam-designer` | `@edu-agent-exam-designer` | `_edu/agents/exam-designer.md` | Build exam blueprints and questions |
| `classroom-designer` | `@edu-agent-classroom-designer` | `_edu/agents/classroom-designer.md` | Build Classroom/autograding scaffolds |
| `topic-director` | `@edu-agent-topic-director` | `_edu/agents/topic-director.md` | Orchestrate automated topic production |

## Codex Invocation Pattern

When the user names an agent, read the canonical file first, then the relevant workflow. Keep the persona useful but prioritize concrete repo changes and verification.
