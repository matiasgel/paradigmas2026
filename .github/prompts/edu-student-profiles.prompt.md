---
description: 'EDU: Perfiles de alumno — gestiona perfiles del simulador e investiga en literatura académica (ERIC, ACM, IEEE)'
agent: 'edu-agent-student-simulator'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load {project-root}/_edu/config.yaml and store ALL fields as session variables
2. Ask the user which mode to activate:
   - [G] Gestionar — administrar perfiles existentes del simulador (crear, editar, eliminar perfiles)
   - [I] Investigar — buscar en literatura académica (ERIC, ACM, IEEE) para calibrar o crear perfiles empíricos
   If the user's original message already indicates the intent (e.g. "investigar perfiles" or "agregar perfil"), skip asking and infer the mode directly.
3. Load and follow the workflow at {project-root}/_edu/workflows/manage-student-profiles/workflow.md
4. Purpose for [G]: Manage simulator student profiles.
   Purpose for [I]: Search academic literature to calibrate or create empirical profiles.
   Output calibration data to the memory_folder defined in config.yaml.
