---
description: 'EDU: Publicar filminas — pipeline completo: plan → imágenes Gemini → Google Slides (sin preguntas)'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute', 'web']
---

## edu-publish-slides — Pipeline unificado

> **Sin preguntas al usuario.** Todo el proceso es automático desde que se invoca.

### Prerequisitos mínimos

1. `_edu/secrets.local.yaml` debe existir → si no: informar al usuario que ejecute `/edu-setup-apis` → STOP.
2. `_edu/slides-config.yaml` debe existir → si no: activar `/edu-slides-designer` automáticamente antes de continuar.
3. `filminas.md` del tema activo debe existir → si no: informar que ejecute `/edu-create-class` → STOP.

### Resolución del tema activo

- Leer `active-topic.yaml` si existe → extraer `topic_folder`.
- Si no existe → usar el primer argumento del usuario (ej: `01-conceptos-introductorios`) para construir la ruta:
  `{topics_folder}/{tema}` según `_edu/config.yaml`.

### Ejecución del pipeline

Una vez validados los prerequisitos, ejecutar en terminal **sin preguntas**:

```bash
python {project-root}/salida/edu-standalone/scripts/slides_pipeline.py \
       {topic_folder}
```

El script realiza automáticamente:

| Fase | Descripción | Salida |
|------|-------------|--------|
| 1. Plan | Lee `filminas.md` → genera `slides/plan-filminas-{tema}.yaml` con contenido completo, directrices de layout e instrucciones de imágenes | `slides/plan-filminas-{tema}.yaml` |
| 2. Assets | Genera imágenes con Gemini API, renderiza tablas como PNG con matplotlib, sube todo a Google Drive | `slides/assets/` + Drive IDs en el plan |
| 3. Publish | Copia plantilla, crea cada filmina con layout correcto, inserta imágenes, tablas y código, guarda URL | `slides/slides-url.txt` |

### Opciones de ejecución parcial

```bash
# Solo generar el plan YAML (para revisar antes de publicar)
python slides_pipeline.py {topic_folder} --plan-only

# Solo generar assets (si el plan ya fue revisado)
python slides_pipeline.py {topic_folder} --assets-only

# Solo publicar (si plan y assets ya existen)
python slides_pipeline.py {topic_folder} --publish-only
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
