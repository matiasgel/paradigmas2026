---
description: 'EDU Fase 3: Diseñar o ajustar tema — inicializa directorio del tema y genera diseno.md'
agent: 'edu-agent-topic-designer'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.

2. Resolve topic directory:
   - If `{project-root}/_edu/active-topic.yaml` exists:
     - Load it, store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables
     - Load `{topic_folder}/topic.yaml` and check `status`
     - If `status == "closed"` OR the user specified a different topic number → treat as new topic (go to else branch)
     - Otherwise → confirm: "¿Continuar con el tema activo: [{topic_number}] {topic_name}? (s/n)"
       If n → ask for new topic number and go to else branch
   - Otherwise (no active-topic.yaml, closed, or different topic number specified):
     - Ask: "¿Qué número de tema vas a diseñar? (ej: 01)"
     - Look up the topic name for that number in `plan-borrador.md` to derive `{topic_slug}`
     - Set `{topic_folder}` = `temas/{topic_number}-{topic_slug}/`
     - Create directory `{project-root}/{topic_folder}` if it doesn't exist
     - Create `{project-root}/{topic_folder}/topic.yaml`:
       ```yaml
       topic_number: "{topic_number}"
       topic_name: "{topic_name}"
       topic_slug: "{topic_slug}"
       topic_folder: "{topic_folder}"
       class_duration: "{default_class_duration}"
       git_branch: "tema-{topic_number}-{topic_slug}"
       created_at: "{today}"
       status: "design"
       artifacts:
         diseno: "diseno.md"
         minuta: "minuta.md"
         filminas: "filminas.md"
         tp: "tp.md"
         score: "score-pedagogico.md"
         faq: "faq-anticipado.md"
         slides_url: "slides/slides-url.txt"
       ```
     - Create/update `{project-root}/_edu/active-topic.yaml`:
       ```yaml
       topic_folder: "{topic_folder}"
       topic_number: "{topic_number}"
       topic_name: "{topic_name}"
       ```

3. Load and follow the workflow at `{project-root}/_edu/workflows/topic-cycle/workflow.md`.
4. Purpose: Design topic content. `class_duration` from `topic.yaml` is the central constraint.
   All outputs go to `{topic_folder}/diseno.md`. Also use to adjust an existing design before approval.

