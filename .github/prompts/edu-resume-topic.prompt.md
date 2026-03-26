---
description: 'EDU: Reanudar producción de tema desde el último checkpoint'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Read `{topic_folder}/.pipeline-state.json` to find the last completed checkpoint.
3. Display current state: which steps are complete, which is next.
4. Resume execution from the next step in the auto-topic workflow.
5. Continue saving checkpoints and respecting all quality gates.
6. If no `.pipeline-state.json` exists, inform the user and suggest running `/edu-auto-topic` instead.
