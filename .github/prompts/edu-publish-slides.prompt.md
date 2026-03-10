---
description: 'EDU: Publicar slides — flujo completo orquestado: verifica setup → diseño → exporta a Google Slides'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store all fields as session variables.

2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}` as session variables.
   If not found → ask: "¿Qué tema querés publicar? (ej: temas/01-conceptos-introductorios)" → set `{topic_folder}`.

3. **Verificación de prerequisitos (en orden):**

   a. Verificar `{project-root}/_edu/secrets.local.yaml`:
      - Si NO existe → "Primero configurá las APIs con /edu-setup-apis" → STOP

   b. Verificar `{project-root}/_edu/slides-config.yaml`:
      - Si NO existe → "No hay sistema de diseño configurado. Activando Vera..."
        - Load `{project-root}/_edu/agents/slides-designer.md`
        - Follow ALL activation instructions
        - After Vera completes, continue to step c
      - Si existe → continuar

   c. Verificar que `{project-root}/{topic_folder}/filminas.md` existe.
      Si no existe → "No se encontró filminas.md en {topic_folder}. ¿Corriste /edu-create-class primero?" → STOP

4. **Activar Diego:**
   - Load `{project-root}/_edu/agents/slides-publisher.md`
   - Follow ALL activation instructions
   - Pass `{topic_folder}` as active context
   - Execute [PB] Publish automatically since prerequisites are confirmed

5. Wait for Diego to complete and surface the Google Slides link to the user.
