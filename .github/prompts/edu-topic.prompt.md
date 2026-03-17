---
description: 'EDU Fase 3: Ciclo de tema — detecta el estado actual, escribe active-topic.yaml y guía el próximo paso'
agent: 'edu-agent-topic-designer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Resolve active topic:
   - If `{project-root}/_edu/active-topic.yaml` exists → load it (show: "Tema activo: [{topic_number}] {topic_name}")
     - Load `{topic_folder}/topic.yaml` and check `status`
     - If `status == "closed"` → inform the user and fall through to scan
   - Otherwise: scan `{project-root}/temas/` for folders containing `topic.yaml` with status != "closed"
     - If multiple found → show the list and ask: "¿Cuál tema querés continuar? (escribí el número)"
     - If exactly one found → use it automatically
   - If no active topic found → ask: "¿Qué número de tema querés iniciar?"
     → run topic initialization (same logic as /edu-design-topic step 2)
3. Write/update `{project-root}/_edu/active-topic.yaml` with the detected or confirmed topic.
4. Load `{project-root}/{topic_folder}/topic.yaml` and store all fields as session variables.
5. Check artifacts in `{topic_folder}/` and determine current state:
   - No diseno.md → próximo: /edu-design-topic
   - diseno.md sin APROBADO → próximo: /edu-design-topic (ajustar) o /edu-approve-design
   - diseno.md APROBADO, sin minuta.md → próximo: /edu-create-class
   - minuta.md existe, sin guia-estudio.md y sin tp.md → próximo: /edu-create-study-guide
   - minuta.md existe, sin guia-estudio.md pero tp.md ya existe → ⚠️ aviso al docente: "La guía de estudio no fue generada. Se recomienda /edu-create-study-guide — o podés avanzar con el estado actual indicando cuál es el próximo paso."
   - guia-estudio.md existe (o docente elige avanzar sin ella), sin tp.md → próximo: /edu-create-tp
   - tp.md existe, sin reporte de calidad → próximo: /edu-quality
   - Reportes de validación existen sin fixes → próximo: /edu-quality
   - Fixes aplicados, sin testing → próximo: /edu-test-topic
   - Testing hecho, topic.yaml status != "closed" → próximo: /edu-close-topic
6. Mostrar estado actual del tema y recomendar el próximo paso con el comando exacto.
7. Preguntar al docente si confirma o elige un paso diferente.
8. Ejecutar el paso elegido cargando y siguiendo el workflow correspondiente.

