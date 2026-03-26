---
description: 'EDU: Producir material completo de un tema automáticamente con Director Agent'
tools: ['read', 'write', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Follow the auto-topic workflow at `_edu/workflows/auto-topic/workflow.md`.
3. Execute each step in sequence:
   - Design → WAIT FOR APPROVAL → Content → Quality Loops → Pipeline → TP → Simulation
4. Save checkpoints after each step in `{topic_folder}/.pipeline-state.json`.
5. If a step fails, log the error and pause for human intervention.
6. At the end, display a summary of all steps completed, artifacts generated, and quality metrics.
