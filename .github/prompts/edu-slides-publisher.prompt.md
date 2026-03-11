---
description: 'EDU: Publicar filminas — Diego exporta filminas.md a Google Slides (requiere /edu-setup-apis y /edu-slides-designer)'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute', 'web']
---

1. Load `{project-root}/_edu/config.yaml` and store all fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → ask: "¿Qué tema querés publicar? (ej: temas/01-conceptos-introductorios)" → set `{topic_folder}`.
3. Load the full agent file from `{project-root}/_edu/agents/slides-publisher.md`.
4. Follow ALL activation instructions in the agent file.
5. Display the welcome/greeting as instructed.
6. Pass `{topic_folder}` as active context so Diego knows which filminas.md to publish.
7. Present the numbered menu.
8. Wait for user input before proceeding.

