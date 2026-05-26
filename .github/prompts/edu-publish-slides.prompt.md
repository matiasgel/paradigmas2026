---
description: 'EDU: Publicar filminas — pipeline completo v3: schema-driven plan JSON → imágenes Gemini → Google Slides (sin preguntas)'
agent: 'agent'
tools: ['read', 'edit', 'search', 'execute', 'fetch']
---

## edu-publish-slides — Pipeline genérico + planeamiento determinista schema-driven

> **Sin preguntas al usuario.** Todo el proceso es automático desde que se invoca.
> El agente genera un plan JSON determinista siguiendo el schema registry inmutable.

### Prerequisitos mínimos

1. `_edu/secrets.local.yaml` debe existir → si no: informar al usuario que ejecute `/edu-setup-apis` → STOP.
2. `_edu/slides-config.yaml` debe existir → si no: activar `/edu-slides-designer` automáticamente antes de continuar.
3. `_edu/schemas/schema-registry.json` debe existir → si no: STOP con error "schemas v3 ausentes".
4. `filminas.md` del tema activo debe existir → si no: informar que ejecute `/edu-create-class` → STOP.

### PASO 0 OBLIGATORIO: Leer Schema Registry

**ANTES de cualquier otra acción**, el agente DEBE leer:
- `{project-root}/_edu/schemas/schema-registry.json`

De ahí extraer y memorizar:
- `canonical_types` (enum cerrado de tipos de filmina)
- `type_layout_map` (mapeo determinista tipo → layout + image_layer)
- `image_prompt_rules` (reglas de prompts visuales)
- `file_conventions` (formato JSON, nombres de archivo)

### Contrato UX del pipeline

- El pipeline respeta el sistema definido por Vera (slides-config.yaml).
- Las listas Markdown se convierten a bullets nativos de Google Slides.
- Los headings, énfasis, inline code y links se renderizan como estilo de texto real.

### Separación de responsabilidades

- El script de publicación es **genérico**: consume un plan JSON y ejecuta rendering + upload + publish.
- El agente genera el plan JSON siguiendo estrictamente el schema registry.
- El agente **NO modifica scripts** para resolver la semántica del tema.
- Las imágenes deben ser específicas del tema, no genéricas.
- Las imágenes deben ser **originales** — no pedir copia de obras o estilos protegidos.

### Resolución del tema activo

- Leer `active-topic.yaml` si existe → extraer `topic_folder`.
- Si no existe → usar el argumento del usuario para construir la ruta:
  `{topics_folder}/{tema}` según `_edu/config.yaml`.

### Generación del plan (SCHEMA-DRIVEN)

El agente DEBE generar UN SOLO archivo en `{topic_folder}/slides/`:

**`plan-filminas-{tema}.json`** — formato JSON, no YAML.

Procedimiento DETERMINISTA:
1. Leer `filminas.md` completo
2. Para cada slide:
   a. Asignar `type` del enum `canonical_types` del schema registry (NUNCA inventar)
   b. COPIAR `layout` = `type_layout_map[type].layout` (EXACTO, sin modificar)
   c. COPIAR `image.layer` = `type_layout_map[type].image_layer`
   d. Si `image.layer != "none"` → escribir `image.prompt` con lenguaje visual puro
   e. Poblar `body_blocks`, `code_blocks`, `tables` preservando TODO el contenido
   f. Crear `table_assets` vacíos para cada tabla
3. Incluir `$schema_version: "plan-filminas/v3"`
4. Incluir `meta` con `design_system_path`, `pipeline_runtime_path`, `schema_registry_path`
5. Calcular `summary` con conteos (total_slides, images_planned, type_distribution)

> ⚠️ **NUNCA** nombrar conceptos técnicos en prompts de imagen. Usar solo geometría, colores y posiciones.
> Ver guía anti-Bug 3 en `_edu/templates/prompt-imagen-guide.md`.

### Ejecución del pipeline (publish_loop obligatorio)

> ⚠️ **NUNCA llamar `slides_pipeline.py` directamente.** Usar siempre `publish_loop.py`.

Después de generar el plan JSON, ejecutar en terminal **sin preguntas**:

```bash
python {project-root}/salida/edu-standalone/scripts/publish_loop.py {topic_folder} --course {course_id}
```

`publish_loop.py` orquesta automáticamente:

| Fase | Descripción | Salida |
|------|-------------|--------|
| FASE 1 | Reparación schema (hasta 3 intentos con repair_plan.py) | Plan válido |
| FASE 2 | Coherencia: validate_plan + WCAG + cognitiva + composición + facts + drift semántico | Informe de coherencia |
| FASE 3 | Publicación: slides_pipeline.py | `slides/slides-url.txt` |
| FASE 4 | Post-publicación: thumbnails + memory.db | `publish-report.json` |

**Exit codes:**
- `0` → publicación exitosa
- `1` → errores de validación (ver reporte)
- `2` → max intentos de reparación → revisión humana
- `3` → FASE 2 falló: coherencia bloqueada (revisar `publish-report.json`)

**Opciones útiles:**
```bash
python publish_loop.py {topic_folder} --course {course_id} --dry-run      # validar sin publicar
python publish_loop.py {topic_folder} --course {course_id} --skip-phase2  # solo schema + publicar
python publish_loop.py {topic_folder} --course {course_id} --skip-facts   # omitir fact_verifier
```

**Solo para re-validar el plan sin publicar:**
```bash
python {project-root}/salida/edu-standalone/scripts/validate_plan.py {topic_folder}
```

**Solo para regenerar plan desde filminas.md preservando imágenes ya subidas a Drive:**
```bash
python {project-root}/salida/edu-standalone/scripts/refresh_plan.py {topic_folder}
```

### Output final

Mostrar al usuario:
```
✅ Pipeline completado (schema v3)
URL: https://docs.google.com/presentation/d/{id}/edit
Plan: {topic_folder}/slides/plan-filminas-{tema}.json
Schema: plan-filminas/v3
```

### Instalación de dependencias

Si las dependencias no están instaladas:
```bash
pip install -r {project-root}/salida/edu-standalone/scripts/requirements.txt
```
