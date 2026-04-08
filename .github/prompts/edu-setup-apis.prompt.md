---
description: 'EDU: Configurar APIs — Google OAuth + Gemini key para publicación en Google Slides'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

1. Load `{project-root}/_edu/config.yaml` and store all fields as session variables
2. Guide the user interactively through API setup:

   **Paso 1 — Google OAuth (para Google Slides API):**
   - Explicar qué es y para qué se usa (crear presentaciones en Google Drive del usuario)
   - Guiar paso a paso:
     1. Ir a https://console.cloud.google.com
     2. Crear proyecto nuevo o seleccionar existente
     3. Habilitar "Google Slides API" en APIs & Services → Library
     4. Crear credenciales OAuth 2.0 → Desktop App
     5. Descargar el archivo `credentials.json`
     6. Moverlo a `{project-root}/_edu/credentials.json`
   - Verificar que el archivo existe antes de continuar

   **Paso 2 — Gemini API key (para generación de imágenes):**
   - Explicar qué es y para qué se usa (generar imágenes contextuales para las filminas)
   - Guiar:
     1. Ir a https://aistudio.google.com/app/apikey
     2. Crear nueva API key
     3. Copiar la key
   - Pedir al usuario que pegue la key

3. Crear/actualizar `{project-root}/_edu/secrets.local.yaml` con:
   ```yaml
   google_credentials_path: "_edu/credentials.json"
   gemini_api_key: "<key-ingresada>"
   ```
   NUNCA escribir la credentials.json completa dentro de secrets.local.yaml — solo la ruta.

4. Verificar que `{project-root}/_edu/secrets.local.yaml` existe y tiene ambos campos.

5. Verificar que `{project-root}/.gitignore` incluye:
   - `_edu/secrets.local.yaml`
   - `_edu/credentials.json`
   Si no están, agregarlos al `{project-root}/.gitignore` automáticamente.

6. Confirmar: "✅ APIs configuradas correctamente. Ahora podés correr /edu_slides_designer para definir el diseño visual."
