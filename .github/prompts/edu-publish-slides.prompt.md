---
description: 'EDU: Publicar slides — flujo completo orquestado: verifica setup → diseño → exporta a Google Slides'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute']
---

1. Load `{project-root}/_edu/config.yaml` and store all fields as session variables

2. **Verificación de prerequisitos (en orden):**

   a. Verificar `{project-root}/_edu/secrets.local.yaml`:
      - Si NO existe → informar: "Primero configurá las APIs con /edu_setup_apis" → STOP

   b. Verificar `{project-root}/_edu/slides-config.yaml`:
      - Si NO existe → informar: "No hay sistema de diseño configurado. Activando Vera..."
        - Load `{project-root}/_edu/agents/slides-designer.md`
        - Follow ALL activation instructions
        - After Vera completes, continue to step c
      - Si existe → continuar

   c. Pedir al usuario el tema a publicar (ej: "temas/01-conceptos-introductorios")
      - Verificar que `{project-root}/{tema}/filminas.md` existe
      - Si no existe → "No se encontró filminas.md en ese tema. ¿Corriste /edu_create_class primero?" → STOP

3. **Activar Diego:**
   - Load `{project-root}/_edu/agents/slides-publisher.md`
   - Follow ALL activation instructions
   - Pass the identified tema path as active context
   - Execute [PB] Publish automatically since prerequisites are confirmed

4. Wait for Diego to complete and surface the Google Slides link to the user.
