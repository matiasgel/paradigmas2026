---
description: 'EDU Fase 2: Construir cursado — desde material existente (PDFs, PPTX, DOCX) o desde investigación académica pura'
agent: 'edu-agent-course-planner'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load {project-root}/_edu/config.yaml and store ALL fields as session variables
2. Ask the user which mode to use:
   - [M] Materiales — tengo PDFs, PPTX o DOCX existentes para importar
   - [I] Investigación — construir desde cero con investigación académica pura
   If the user's original message already indicates the intent (e.g. "tengo un PDF" or "desde cero"), skip asking and infer the mode directly.
3. For [M]: Load and follow the workflow at {project-root}/_edu/workflows/build-course-from-materials/workflow.md
   For [I]: Load and follow the workflow at {project-root}/_edu/workflows/build-course-from-research/workflow.md
