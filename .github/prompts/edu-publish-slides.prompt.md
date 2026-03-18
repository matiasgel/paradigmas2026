---
description: 'EDU: Publicar filminas — pipeline completo: plan → imágenes Gemini → Google Slides (sin preguntas)'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

## edu-publish-slides — Pipeline genérico + planeamiento por agente

> **Sin preguntas al usuario.** Todo el proceso es automático desde que se invoca.
> El prompt orquesta. La inteligencia semántica y la creación de artefactos previos al publish las hace el agente llamado por el prompt.

### Prerequisitos mínimos

1. `_edu/secrets.local.yaml` debe existir → si no: informar al usuario que ejecute `/edu-setup-apis` → STOP.
2. `_edu/slides-config.yaml` debe existir → si no: activar `/edu-slides-designer` automáticamente antes de continuar.
3. `filminas.md` del tema activo debe existir → si no: informar que ejecute `/edu-create-class` → STOP.

### Contrato UX del pipeline

- El pipeline debe respetar el sistema definido por Vera como UX designer de filminas.
- Las listas Markdown se convierten a bullets nativos de Google Slides, nunca se publican con prefijos literales como `-`, `*`, `•` o `1.`.
- Los headings internos, énfasis, inline code y links del Markdown se renderizan como estilo de texto real en Slides.
- El objetivo es una filmina proyectable y limpia, no una copia textual del markup.

### Separación de responsabilidades

- El script de publicación debe ser **genérico**: consume artefactos YAML ya resueltos y ejecuta rendering + upload + publish.
- El agente invocado por este prompt debe leer `filminas.md` y crear por sí mismo los artefactos necesarios para publicar.
- El prompt **no debe pedir modificar scripts** para resolver la semántica del tema.
- Las imágenes deben responder al contenido del tema y de cada filmina, no a prompts visuales genéricos.
- La generación de imágenes debe producir material **original** y topical; no debe pedir copia de obras, estilos protegidos, personajes o assets con copyright no licenciados.

### Resolución del tema activo

- Leer `active-topic.yaml` si existe → extraer `topic_folder`.
- Si no existe → usar el primer argumento del usuario (ej: `01-conceptos-introductorios`) para construir la ruta:
  `{topics_folder}/{tema}` según `_edu/config.yaml`.

### Ejecución del pipeline

Antes de ejecutar el script, el agente debe generar estos artefactos en `{topic_folder}/slides/`:

1. `plan-filminas-{tema}.yaml`
  - Contenido completo de cada slide
  - Layout resuelto
  - Estrategia de assets
  - Prompts de imagen específicos del tópico
2. `assets-manifest.yaml`
  - Lista de imágenes/tablas/código a materializar
  - Naming estable de archivos locales
3. `publish-context.yaml`
  - template_id
  - metadatos del tema
  - opciones de publicación necesarias para el script

El contrato canónico del plan debe vivir en:

- `{project-root}/_edu/templates/slides-plan-schema.yaml`

Una vez generados y validados esos artefactos, ejecutar en terminal **sin preguntas**:

```bash
python {project-root}/salida/edu-standalone/scripts/slides_pipeline.py \
       {topic_folder}
```

El script realiza automáticamente:

| Fase | Descripción | Salida |
|------|-------------|--------|
| 1. Load plan | Lee `slides/plan-filminas-{tema}.yaml`, `assets-manifest.yaml` y `publish-context.yaml` | Artefactos cargados |
| 2. Assets | Genera imágenes con Gemini API, renderiza tablas como PNG con matplotlib, sube todo a Google Drive | `slides/assets/` + Drive IDs en el plan |
| 3. Publish | Copia plantilla, crea cada filmina con layout correcto, inserta imágenes, tablas, código y formato semántico de Markdown, guarda URL | `slides/slides-url.txt` |

### Opciones de ejecución parcial

```bash
# Solo validar artefactos YAML y generar assets
python slides_pipeline.py {topic_folder} --assets-only

# Solo publicar (si plan y assets ya existen)
python slides_pipeline.py {topic_folder} --publish-only

# Publicación completa a partir de artefactos ya generados por el agente
python slides_pipeline.py {topic_folder}
```

### Output final

Mostrar al usuario:
```
✅ Pipeline completado
URL: https://docs.google.com/presentation/d/{id}/edit
Plan: {topic_folder}/slides/plan-filminas-{tema}.yaml
```

### Instalación de dependencias

Si las dependencias no están instaladas:
```bash
pip install -r {project-root}/salida/edu-standalone/scripts/requirements.txt
```
