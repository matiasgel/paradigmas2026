---
description: 'EDU: Estado del tema — muestra estado de producción de un tema específico'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Resolve topic:
   - If `{project-root}/_edu/active-topic.yaml` exists → load it as default
     Ask: "¿Ver estado del tema activo ({topic_name}) o de otro? (enter = activo, o número de tema)"
   - If no active-topic.yaml → ask: "¿Qué número de tema querés verificar?"
   Set `{topic_folder}` as session variable.
3. Load `{project-root}/{topic_folder}/topic.yaml` if exists → store all fields.
4. Read all artifacts:
   - `{topic_folder}/diseno.md`
   - `{topic_folder}/minuta.md`
   - `{topic_folder}/filminas.md`
   - `{topic_folder}/guia-estudio.md`
   - `{topic_folder}/guia-estudio.pdf`
   - `{topic_folder}/tp.md`
   - `{topic_folder}/score-pedagogico.md`
   - `{topic_folder}/faq-anticipado.md`
   - `{topic_folder}/quality-reports/` (scan for any `*.md` report files)
   - `{topic_folder}/slides/slides-url.txt`
   - `{topic_folder}/topic.yaml` (status field)
5. Report production status: design, class, study guide (+ PDF exportado si existe), TP, quality loops, testing, slides.
6. Recommend next step based on what is missing.

