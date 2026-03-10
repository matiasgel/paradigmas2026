---
description: 'EDU Fase 3: Ciclo de tema — detecta el estado actual y guía el próximo paso'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute']
---

1. Load {project-root}/_edu/config.yaml and store ALL fields as session variables
2. Scan temas/ folder to detect the active topic (folder without git-merge marker).
3. Check artifacts in that topic folder and determine current state:
   - No diseno.md → próximo: /edu_design_topic
   - diseno.md sin APROBADO → próximo: /edu_design_topic (para ajustar) o /edu_approve_design
   - diseno.md APROBADO, sin minuta.md → próximo: /edu_create_class
   - minuta.md existe, sin tp.md → próximo: /edu_create_tp
   - tp.md existe, sin reporte de calidad → próximo: /edu_quality_validate
   - Reportes de validación existen sin fixes → próximo: /edu_quality_fix
   - Fixes aplicados, sin testing → próximo: /edu_test_topic
   - Testing hecho, sin git-merge → próximo: /edu_close_topic
   - Sin tema activo → preguntar qué número de tema iniciar
4. Mostrar estado actual del tema y recomendar el próximo paso con el comando exacto.
5. Preguntar al docente si confirma o elige un paso diferente.
6. Ejecutar el paso elegido cargando y siguiendo el workflow correspondiente.
