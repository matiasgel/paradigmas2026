# Informe Técnico — Pipeline de Filminas EDU
## Correcciones Aplicadas, Proceso Completo y Archivos de Referencia

**Proyecto:** Paradigmas y Lenguajes de Programación 2026  
**Institución:** Universidad Nacional de Tierra del Fuego — Instituto IDEI  
**Docente:** Matías Gel  
**Fecha:** 18 de marzo de 2026  
**Tema procesado:** 02 — Sintaxis y Semántica de Lenguajes  
**Presentación final:** https://docs.google.com/presentation/d/1nY5Zl8c7fKjWxQPdd32fau4Y-vNOyOIASLLRJxBb5eE/edit

---

## Tabla de Contenidos

1. [Descripción General del Sistema](#1-descripción-general-del-sistema)
2. [Archivos Involucrados](#2-archivos-involucrados)
3. [Bug 1 — Contenido de filminas no renderizaba en slides con código](#3-bug-1--contenido-de-filminas-no-renderizaba-en-slides-con-código)
4. [Bug 2 — Presupuesto de imágenes insuficiente](#4-bug-2--presupuesto-de-imágenes-insuficiente)
5. [Bug 3 — Prompts de imágenes generaban texto en inglés](#5-bug-3--prompts-de-imágenes-generaban-texto-en-inglés)
6. [Mejora — Flag `--regen-plan`](#6-mejora--flag---regen-plan)
7. [Proceso Completo de Ejecución](#7-proceso-completo-de-ejecución)
8. [Inspección Visual y Corrección Iterativa de Imágenes](#8-inspección-visual-y-corrección-iterativa-de-imágenes)
9. [Resultados Finales](#9-resultados-finales)
10. [Archivos de Referencia](#10-archivos-de-referencia)

---

## 1. Descripción General del Sistema

El pipeline `slides_pipeline.py` es el componente central del módulo EDU que convierte un archivo `filminas.md` en una presentación Google Slides publicada. Opera en tres fases secuenciales:

```
filminas.md
    │
    ▼
[Fase 1: generate_plan()]
    │  Parsea filminas.md sección por sección.
    │  Detecta tipo de cada slide (_detect_type).
    │  Asigna layout y estrategia de imagen.
    │  Genera prompts para Gemini.
    │  Salida: plan-filminas-{tema}.yaml
    ▼
[Fase 2: generate_assets()]
    │  Lee plan YAML.
    │  Llama Gemini Imagen 4.0 para generar imágenes.
    │  Renderiza tablas como PNG (matplotlib).
    │  Sube assets a Google Drive.
    │  Actualiza el plan con drive_ids.
    ▼
[Fase 3: publish_slides()]
    │  Copia la plantilla Google Slides (template_id).
    │  Construye 742 requests de la Google Slides API.
    │  Envía en lotes de 50 (batchUpdate).
    │  Escribe URL final en slides-url.txt.
    ▼
Presentación publicada en Google Slides (40 slides)
```

**Tecnologías utilizadas:**
- Python 3.x con venv en `.venv/`
- Google Slides API v1 y Google Drive API v3
- Gemini Imagen 4.0 (`imagen-4.0-generate-001`) via REST
- PyYAML, requests, matplotlib, Pillow
- Autenticación OAuth2 con token persistente en `_edu/token_slides.json`

---

## 2. Archivos Involucrados

### Scripts

| Archivo | Descripción | Líneas |
|---------|-------------|--------|
| `scripts/slides_pipeline.py` | Pipeline completo: plan → assets → Google Slides | 2070 |

### Configuración

| Archivo | Descripción |
|---------|-------------|
| `_edu/slides-config.yaml` | Sistema de diseño: paleta, tipografía, layouts, estrategia Gemini |
| `_edu/config.yaml` | Configuración global del módulo EDU |
| `_edu/secrets.local.yaml` | Credenciales API (gemini_api_key, google_credentials_path) — **no copiado por seguridad** |
| `_edu/token_slides.json` | Token OAuth2 persistente para Google APIs — **no copiado por seguridad** |

### Artefactos del Tema 02

| Archivo | Descripción |
|---------|-------------|
| `salida/.../filminas.md` | Fuente del contenido: 40 filminas, 120 minutos |
| `slides/plan-filminas-02-sintaxis-semantica.yaml` | Plan completo con metadata, layouts y prompts de imagen |
| `slides/assets-manifest.yaml` | Inventario de todos los assets generados con sus drive_ids |
| `slides/publish-context.yaml` | Contexto de publicación: rutas, template_id, política de imagen |
| `slides/slides-url.txt` | URL final de la presentación publicada |
| `slides/assets/` | 21 archivos PNG (12 imágenes Gemini + 9 tablas renderizadas) |

---

## 3. Bug 1 — Contenido de filminas no renderizaba en slides con código

### Síntoma

La filmina **F-03 "Sintaxis"** contenía tanto texto explicativo (definición, bullets) como un bloque de código de ejemplo. Al publicar la presentación, **solo aparecía el bloque de código** — el texto del cuerpo no se mostraba.

**Contenido original de F-03 en `filminas.md`:**
```markdown
## Sintaxis

> **Reglas que determinan cuándo un programa está bien formado.**

- Se ocupa de la **forma**
- No decide todavía el comportamiento
- Responde: *¿es este texto un programa válido?*

**Ejemplo canónico:**

\```text
if (<expresión>) <sentencia>
\```
```

### Causa Raíz

La función `_detect_type()` en `slides_pipeline.py` tenía esta lógica:

```python
# CÓDIGO ANTERIOR (con bug):
def _detect_type(slide_id, title, code_blocks, tables, directives=None, body_blocks=None):
    ...
    if code_blocks:
        return "codigo"   # ← Cualquier slide con código → tipo "codigo"
    ...
```

El tipo `"codigo"` tenía este layout asignado en `LAYOUT_MAP`:

```python
"codigo": {
    "title": "full-title",
    "body":  "subtitle-only",   # ← Zona pequeñísima, solo para un subtítulo
    "image": "none",
    "code":  "full-bottom",     # ← Código ocupa casi la pantalla completa
    "table": "none"
}
```

La zona `subtitle-only` es una franja muy delgada (alto ≈ 300px) bajo el título, diseñada para un subtítulo corto. Los bullets, la definición y el texto explicativo no cabían y quedaban fuera de los límites del slide, invisibles en la presentación final.

### Solución Aplicada

**Paso 1:** Se agregó un nuevo tipo `"concepto-mixto"` a las tablas `IMAGE_STRATEGY` y `LAYOUT_MAP`:

```python
# NUEVO — En IMAGE_STRATEGY:
IMAGE_STRATEGY["concepto-mixto"] = "none"   # sin imagen: body izquierdo + código derecho

# NUEVO — En LAYOUT_MAP:
LAYOUT_MAP["concepto-mixto"] = {
    "title": "full-title",
    "body":  "left-middle",    # ← Columna izquierda: texto completo visible
    "image": "none",
    "code":  "right-half",     # ← Columna derecha: bloque de código
    "table": "none"
}
```

**Paso 2:** Se modificó `_detect_type()` para distinguir entre slides de código puro y slides mixtos (texto + código):

```python
# CÓDIGO CORREGIDO:
def _detect_type(slide_id, title, code_blocks, tables,
                 directives=None, body_blocks=None):
    forced_type = str((directives or {}).get("type", "")).strip()
    if forced_type in LAYOUT_MAP:
        return forced_type
    num = int(slide_id.split("-")[1])
    if num == 0:
        return "portada"
    if code_blocks:
        # NUEVO: verificar si hay también cuerpo sustancial
        if body_blocks:
            substantial = sum(
                len(b.get("items", []))
                if b.get("type") == "list"
                else (1 if b.get("type") in ("text", "heading") else 0)
                for b in body_blocks
            )
            if substantial >= 2:
                return "concepto-mixto"   # ← Layout dividido: body izq + código der
        return "codigo"   # ← Solo código sin cuerpo relevante
    ...
```

**Lógica de detección:** Si un slide tiene bloques de código (`code_blocks`) Y además tiene 2 o más ítems de cuerpo (`lista con ≥2 items` o `≥2 bloques de texto/heading`), se clasifica como `"concepto-mixto"` en lugar de `"codigo"`.

**Resultado:** F-03 pasó a tipo `concepto-mixto`. El layout resultante divide la filmina en dos columnas: columna izquierda con la definición y bullets visibles, columna derecha con el ejemplo de código.

---

## 4. Bug 2 — Presupuesto de imágenes insuficiente

### Síntoma

Las filminas F-20, F-26, F-33 y F-37 tenían `strategy: none` en el plan YAML — no se les asignaba imagen a pesar de que deberían tenerla (son de tipo `concepto-abstracto` o `diagrama`).

### Causa Raíz

La configuración en `_edu/slides-config.yaml` tenía:

```yaml
gemini_image_strategy:
  max_images_per_presentation: 4
```

Y la función `_max_images_per_presentation()` leía ese valor directamente:

```python
def _max_images_per_presentation(config: dict) -> int:
    strategy = config.get("gemini_image_strategy", {}) or {}
    raw = strategy.get("max_per_presentation",
            strategy.get("max_images_per_presentation", 8))
    return int(raw)
```

Con solo 4 imágenes permitidas, el algoritmo de asignación por prioridad agotaba el budget antes de llegar a las slides mencionadas.

### Solución Aplicada

Se agregó un piso mínimo de 12 imágenes en la función `generate_plan()`:

```python
# ANTES:
max_images = _max_images_per_presentation(config)

# DESPUÉS:
max_images = _max_images_per_presentation(config)
if max_images < 12:
    max_images = 12    # ← Garantiza mínimo 12 imágenes independientemente del config
```

**Resultado:** Las 40 filminas del tema 02 terminaron con **12 imágenes planificadas**, incluyendo F-20, F-26, F-33 y F-37.

---

## 5. Bug 3 — Prompts de imágenes generaban texto en inglés

### Síntoma

Tras la primera regeneración de imágenes, la inspección visual (descargando thumbnails via Google Slides API `getThumbnail`) reveló que **7 de las 12 imágenes** tenían labels o texto en inglés generado por Gemini Imagen 4.0:

| Slide | Texto incorrecto generado |
|-------|--------------------------|
| F-02 | "Compiler Layer", "Execution Base" en bloques 3D |
| F-04 | Banner "FLATH ICONS" en la esquina |
| F-12 | "AMBINICITY", "FORMACL GRAMMAR", "AUTOMATIC VALIDATION" bajo íconos |
| F-23 | "PROGRAMMORS", "IMPLEMENTER" en banners |
| F-26 | "Named Name", "Variable", "function", "Constant" como labels |
| F-33 | "{OUTPILER}" en ícono de archivo |
| F-37 | "Parser", "Lexicon", "Grammaris", "Disgandor", "Semantics", "Compiler" |

### Causa Raíz

Los prompts de imagen describían conceptos técnicos usando sus nombres (p. ej. "diagrama de infografía con capas: compilador, ejecución"). Gemini Imagen interpreta cualquier elemento conceptual nombrado como algo que necesita una etiqueta de texto para identificarse.

**Patrón detectado:** Cualquier prompt que:
1. Usa la palabra "infografía"
2. Describe múltiples elementos por su nombre conceptual (compilador, parser, semántica, etc.)
3. Lista "componentes" o "fases" de un proceso técnico

...resulta en una imagen con labels en inglés aproximado (transliteraciones incorrectas del español al inglés, tipo "Grammaris" por "Gramática", "PROGRAMMORS" por "Programadores").

### Solución Aplicada — Estrategia de Prompts Visuales Puros

La función `_image_safety_rules()` se simplificó:

```python
# ANTES (verboso, instrucciones negativas largas que Gemini ignoraba):
def _image_safety_rules() -> str:
    return (
        "No se deben incluir palabras, letras, números ni texto de ningún tipo. "
        "Si la imagen necesita texto o etiquetas para comunicar su mensaje, "
        "rediseñar usando solo formas, colores e iconos. "
        "No incluir pantallas con código legible, diagramas con nombres de nodos, "
        "whiteboard con texto, ecuaciones ni fórmulas matemáticas..."
        # ... 8 líneas más
    )

# DESPUÉS (corto, directo, efectivo):
def _image_safety_rules() -> str:
    return (
        "Sin texto, sin letras, sin código, sin etiquetas ni fórmulas. "
        "Solo elementos visuales: objetos, iconos, escenas o diagramas mudos. "
        "Estilo vectorial limpio, fondo claro, académico."
    )
```

Para las 7 imágenes problemáticas se aplicaron prompts de **puro lenguaje visual** — describiendo únicamente propiedades geométricas, posicionales y de color, sin nombrar los conceptos que los elementos representan:

#### Prompts corregidos (Ronda 3):

**F-02** (antes: "diagrama de capas sintaxis/semántica"):
```
Two flat squares stacked vertically. Top square dark red. Bottom square light gray.
Three thin curved lines connecting them in the center. White background.
Pure geometric abstract composition. Alta resolución. Sin texto, sin letras...
```

**F-04** (antes: "balanza con reglas bien formadas vs errores"):
```
Justice scales flat icon. Left bowl contains orderly stacked horizontal rectangles.
Right bowl contains randomly scattered small squares. Bordo and dark gray tones.
White background. Zero text. Alta resolución. Sin texto, sin letras...
```

**F-12** (antes: "infografía ambigüedad → gramática formal → validación automática"):
```
Three flat icons in a horizontal sequence on white background separated by thin arrows.
First: irregular blob shape. Second: symmetrical triangular branching tree.
Third: bold checkmark symbol. Flat design, bordo and dark gray palette. Nothing written.
Alta resolución. Sin texto, sin letras...
```

**F-23** (antes: "tres roles: programador, implementador, usuario"):
```
Three human silhouettes arranged in a column on white background.
First silhouette has a monitor floating beside it.
Second silhouette has a gear floating beside it.
Third silhouette has a closed book floating beside it.
Flat design, bordo and dark navy palette. No labels, no text at all.
Alta resolución. Sin texto, sin letras...
```

**F-26** (antes: "nombre y objetos denotables: variable, función, constante, tipo"):
```
Small empty rectangle on the bottom left with a bold arrow pointing to a larger square
on the right. Inside the large square: six distinct geometric shapes — cylinder, diamond,
triangle, hexagon, circle, star — arranged loosely. Bordo and gray palette.
White background. No text whatsoever. Alta resolución. Sin texto, sin letras...
```

**F-33** (antes: "compilador vs intérprete pipeline"):
```
Two vertical parallel columns. Each column has four plain gray and bordo rectangles
connected by downward arrows. Left column ends at a document icon with a folded top corner.
Right column ends at a microchip icon. White background. Flat minimal design.
No text, no code symbols. Alta resolución. Sin texto, sin letras...
```

**F-37** (antes: "mapa conceptual: lexer, parser, gramática, diagramas, semántica, pipeline"):
```
One large bordo filled circle in the center. Six thin straight lines radiate outward.
At the end of each line, one small flat icon: magnifying glass, gear, downward branching
tree, two-by-two grid, cube, horizontal tube. White background.
No labels, no words, nothing written anywhere. Alta resolución. Sin texto, sin letras...
```

**Principio clave descubierto:** Gemini Imagen agrega labels cuando el prompt nombra conceptos técnicos. La solución es describir **exclusivamente la geometría visual** de la imagen (formas, colores, posiciones, tamaños) sin mencionar qué representa cada elemento.

### Proceso de Inspección Visual via API

Para verificar las imágenes directamente en la presentación publicada (no solo los assets locales), se usó la Google Slides API `getThumbnail`:

```python
# Endpoint usado para descarga de thumbnails:
GET https://slides.googleapis.com/v1/presentations/{presentationId}/pages/{pageObjectId}/thumbnail
    ?thumbnailProperties.thumbnailSize=LARGE

# Guardado local en:
salida/cursadas/2026/temas/02-sintaxis-semantica/slides/thumbnails/
```

Esto permitió ver exactamente cómo la imagen aparecía en el contexto del slide (con layout, colores del template, etc.) en lugar de solo el PNG crudo de Gemini.

---

## 6. Mejora — Flag `--regen-plan`

### Necesidad

El plan `plan-filminas-{tema}.yaml` es el artefacto central que conecta el contenido Markdown con los assets de imagen. Cuando se corrigen los prompts directamente en el YAML (para afinar las imágenes), el plan refleja los cambios. Pero cuando se necesita regenerar el plan completo desde `filminas.md` (por ejemplo, después de editar el contenido de la clase), no había forma de hacerlo sin ejecutar el pipeline completo.

### Implementación

Se agregó el flag `--regen-plan` al argparser en `main()`:

```python
# En main():
parser.add_argument(
    "--regen-plan",
    action="store_true",
    help="Regenera plan-filminas YAML desde filminas.md"
)

# Lógica de ejecución:
if args.regen_plan:
    filminas_path = topic_folder / "filminas.md"
    new_plan = generate_plan(filminas_path, config, template_id)
    plan_path.parent.mkdir(parents=True, exist_ok=True)
    save_yaml(plan_path, new_plan)
    print(f"  📄 Plan regenerado: {plan_path.relative_to(project_root)}")
    print(f"     {new_plan['meta']['total_slides']} filminas, {new_plan['meta']['images_planned']} imágenes planificadas.")
    return
```

**Uso:**
```bash
python scripts/slides_pipeline.py salida/cursadas/2026/temas/02-sintaxis-semantica --regen-plan
```

**Importante:** `--regen-plan` NO requiere credenciales de Google API (solo lee `slides-config.yaml`), lo que lo hace muy rápido para iterar sobre el contenido.

---

## 7. Proceso Completo de Ejecución

El proceso completo del tema 02 siguió esta secuencia de comandos:

```bash
# Activar entorno virtual
source .venv/bin/activate

# 1. Regenerar el plan YAML desde filminas.md con los fixes aplicados
python scripts/slides_pipeline.py \
    salida/cursadas/2026/temas/02-sintaxis-semantica \
    --regen-plan
# Output: Plan regenerado: 40 filminas, 12 imágenes planificadas

# 2. Generar assets con los prompts del plan nuevo
python scripts/slides_pipeline.py \
    salida/cursadas/2026/temas/02-sintaxis-semantica \
    --assets-only
# Output: 12 imágenes generadas, subidas a Google Drive con drive_ids

# [INSPECCIÓN VISUAL] — Descargar thumbnails via API y verificar imágenes
# 7 imágenes con texto identificadas → corrección de prompts en plan YAML

# 3. Eliminar los 7 assets con texto para forzar regeneración
rm -f slides/assets/F-02-content.png slides/assets/F-04-content.png
rm -f slides/assets/F-12-bg.png slides/assets/F-23-bg.png
rm -f slides/assets/F-26-content.png slides/assets/F-33-content.png
rm -f slides/assets/F-37-content.png
# También: drive_id → null en el plan YAML para los 7 slides

# 4. Regenerar solo las 7 imágenes corregidas
python scripts/slides_pipeline.py \
    salida/cursadas/2026/temas/02-sintaxis-semantica \
    --assets-only
# Output: 7 imágenes regeneradas sin texto ✅

# 5. Publicar presentación final
python scripts/slides_pipeline.py \
    salida/cursadas/2026/temas/02-sintaxis-semantica \
    --publish-only
# Output: 742 requests, 15 lotes, URL publicada
```

### Flags disponibles del pipeline

| Flag | Descripción | Requiere Google Auth |
|------|-------------|---------------------|
| *(sin flag)* | Ejecuta las 3 fases: plan + assets + publish | Sí |
| `--plan-only` | Solo valida los YAML de publicación existentes | No |
| `--regen-plan` | Regenera plan-filminas desde filminas.md | No |
| `--assets-only` | Genera imágenes faltantes (omite las que ya tienen drive_id) | Sí |
| `--publish-only` | Publica sin regenerar assets | Sí |

---

## 8. Inspección Visual y Corrección Iterativa de Imágenes

### Ronda 1 (Primera publicación)

Presentación ID: `1JZ9-uHRA4ID7LVsiugud0IqhCKkknOa8bVIadzaUC7U`

Problemas detectados:
- F-03: texto del cuerpo no aparecía (→ **Bug 1**, resuelto con concepto-mixto)
- F-20, F-26, F-33, F-37: sin imagen asignada (→ **Bug 2**, resuelto con budget=12)
- Múltiples imágenes con texto en inglés (→ **Bug 3**, prompts simplificados)

### Ronda 2 (Segunda generación de imágenes, post-fix)

Prompts de segunda ronda escritos directamente en el YAML. Aún con texto en 7 imágenes:

| Imagen | Estado Ronda 2 |
|--------|---------------|
| F-00-bg.png | ✅ Aula con pizarrón, aceptable |
| F-02-content.png | ❌ "Compiler Layer", "Execution Base" |
| F-04-content.png | ❌ "FLATH ICONS" banner |
| F-09-content.png | ⚠️ "AB", "C" como símbolos (borderline OK) |
| F-12-bg.png | ❌ "AMBINICITY", "FORMACL GRAMMAR", "AUTOMATIC VALIDATION" |
| F-20-content.png | ✅ Árbol sintáctico limpio |
| F-21-content.png | ✅ Diagrama de railway perfecto |
| F-23-bg.png | ❌ "PROGRAMMORS", "IMPLEMENTER" |
| F-26-content.png | ❌ "Named Name", "Variable", "function", "Constant" |
| F-33-content.png | ❌ "{OUTPILER}" en ícono de archivo |
| F-37-content.png | ❌ "Parser", "Lexicon", "Grammaris", "Disgandor", "Semantics", "Compiler" |
| F-39-content.png | ✅ Libros limpios, sin texto |

### Ronda 3 (Prompts visuales puros — resultado final)

Presentación ID: `1nY5Zl8c7fKjWxQPdd32fau4Y-vNOyOIASLLRJxBb5eE`

| Imagen | Estado Final |
|--------|-------------|
| F-00-bg | ✅ Aula universitaria con pizarrón |
| F-02-content | ✅ Dos cuadrados (bordo/gris) con líneas curvas, sin texto |
| F-04-content | ✅ Balanza con rectángulos ordenados/dispersos, limpia |
| F-09-content | ✅ Grilla 3×3 con símbolos abstractos |
| F-12-bg | ✅ Tres íconos (mancha, árbol, tilde) con flechas, sin etiquetas |
| F-20-content | ✅ Árbol de derivación limpio |
| F-21-content | ✅ Diagrama de railway (excelente, referencia) |
| F-23-bg | ✅ Tres siluetas con monitor, engranaje, libro — sin texto |
| F-26-content | ✅ Rectángulo → flecha → cuadrado con formas geométricas |
| F-33-content | ✅ Dos pipelines verticales con documento y CPU |
| F-37-content | ✅ Rueda radial con 6 íconos, sin labels |
| F-39-content | ✅ Libros con marcapáginas, completamente limpia |

**Resultado: 12/12 imágenes sin texto** ✅

---

## 9. Resultados Finales

### Presentación publicada

- **URL:** https://docs.google.com/presentation/d/1nY5Zl8c7fKjWxQPdd32fau4Y-vNOyOIASLLRJxBb5eE/edit
- **Total de slides:** 40
- **Requests Google Slides API:** 742, enviados en 15 lotes de 50
- **Imágenes generadas:** 12 (Gemini Imagen 4.0)
- **Tablas renderizadas:** 9 (matplotlib → PNG)
- **Template Google Slides:** `1mGncfOizGbRHXNo5xqi9wfqePnlnGKbZUtlvTysYMsI`

### Distribución de tipos de filmina

| Tipo | Cantidad | Layout asignado |
|------|----------|----------------|
| portada | 1 | center-middle + background |
| concepto-abstracto | ~18 | full-title + left-middle + right-half |
| **concepto-mixto** (nuevo) | ~4 | full-title + left-middle + right-half (código) |
| tabla | 9 | full-title + table-intro + table-main |
| diagrama | ~3 | full-title + left-middle + right-half |
| socratica | 1 | center-top + center-middle + background |
| cierre | ~2 | center-middle + center-bottom + background |
| codigo | ~2 | full-title + subtitle-only + full-bottom |

### Cambios en el código fuente

| Función/Sección | Tipo de cambio | Descripción |
|----------------|---------------|-------------|
| `IMAGE_STRATEGY` | Adición | Nueva clave `"concepto-mixto": "none"` |
| `LAYOUT_MAP` | Adición | Nueva entrada `"concepto-mixto"` con layout dividido |
| `_detect_type()` | Modificación | Detección de slides mixtos (código + cuerpo sustancial) |
| `_image_safety_rules()` | Refactoring | Instrucción más corta y efectiva para eliminar texto |
| `_image_prompt()` | Refactoring | Prompts más concisos, orientados a imagen conceptual |
| `generate_plan()` | Modificación | Floor mínimo de 12 imágenes por presentación |
| `main()` | Adición | Flag `--regen-plan` para regenerar YAML desde filminas.md |

---

## 10. Archivos de Referencia

Todos los archivos utilizados en el proceso se encuentran copiados en `informefinal/archivos/`:

### `slides_pipeline.py` — Script principal
Script Python de 2070 líneas. Pipeline completo: parseo Markdown → plan YAML → generación de imágenes Gemini → publicación Google Slides. Ver [`informefinal/archivos/slides_pipeline.py`](archivos/slides_pipeline.py).

**Secciones clave del script (con números de línea):**
- Líneas 82–107: `IMAGE_STRATEGY` y `LAYOUT_MAP` (incluye `concepto-mixto`)
- Líneas 812–843: `_detect_type()` — detección de tipo por contenido
- Líneas 899–919: `_image_safety_rules()` — instrucción anti-texto para Gemini
- Líneas 920–978: `_image_prompt()` — generación de prompt por tipo de slide
- Líneas 978–985: budget mínimo de 12 imágenes
- Líneas 1976–2070: `main()` — CLI con flags `--regen-plan`, `--assets-only`, `--publish-only`

### `slides-config.yaml` — Sistema de diseño
Configuración del diseño visual de la presentación. Define paleta de colores (bordo `#8B0000`, blanco `#FFFFFF`, gris carbón `#1A1A1A`), tipografías (Roboto / Roboto Mono) y layouts por tipo de filmina. Ver [`informefinal/archivos/slides-config.yaml`](archivos/slides-config.yaml).

### `plan-filminas-02-sintaxis-semantica.yaml` — Plan completo
YAML de 45 KB con los 40 slides planificados. Para cada slide define: `id`, `type`, `title`, `body_blocks`, `code_blocks`, `tables`, `layout`, `background_image` y `content_image` (con `prompt`, `local_asset` y `drive_id`). Este archivo es el output de la Fase 1 y el input de las Fases 2 y 3. Ver [`informefinal/archivos/plan-filminas-02-sintaxis-semantica.yaml`](archivos/plan-filminas-02-sintaxis-semantica.yaml).

### `assets-manifest.yaml` — Inventario de assets
Registro de todos los assets generados con sus nombres, tipos, drive_ids y rutas locales. Ver [`informefinal/archivos/assets-manifest.yaml`](archivos/assets-manifest.yaml).

### `publish-context.yaml` — Contexto de publicación
Metadatos del proceso de publicación: rutas a filminas.md, plan, template_id, config, secrets. Sirve como registro reproducible de cómo se generó la presentación. Ver [`informefinal/archivos/publish-context.yaml`](archivos/publish-context.yaml).

### `filminas.md` — Fuente de contenido
El archivo Markdown de 40 filminas del cual se deriva todo el pipeline. Contiene el contenido de la clase de 120 minutos sobre Sintaxis y Semántica de Lenguajes de Programación. Ver [`informefinal/archivos/filminas.md`](archivos/filminas.md).

### `slides-url.txt` — URL final
Archivo de una línea con la URL de la presentación publicada en Google Slides. Ver [`informefinal/archivos/slides-url.txt`](archivos/slides-url.txt).

### `edu-config.yaml` — Configuración global EDU
Configuración del módulo EDU: nombre del proyecto, institución, docente, carpetas de salida y perfiles pedagógicos. Ver [`informefinal/archivos/edu-config.yaml`](archivos/edu-config.yaml).

---

## Apéndice — Lecciones Aprendidas

### Sobre Gemini Imagen y texto no deseado

1. **Instrucciones negativas largas no funcionan**: Listas de 10 prohibiciones son ignoradas. Una instrucción corta y directa al final del prompt es más efectiva.

2. **Vocabulario conceptual → labels automáticos**: Si el prompt menciona "compilador", "parser", "semántica", Gemini entiende que esos elementos deben estar identificados visualmente con texto.

3. **Solución**: Describir SOLO geometría. En lugar de "diagrama con fases del compilador", escribir "columna de 4 rectángulos grises conectados por flechas, con un ícono de documento al final". El modelo genera la imagen sin necesidad de etiquetar nada.

4. **Imágenes de referencia exitosas**: F-20 (árbol de derivación), F-21 (diagrama de railway), F-39 (libros) — todas descritas en términos puramente visuales, sin conceptos técnicos nombrados.

### Sobre el tipo `concepto-mixto`

El layout dividido (texto izquierda / código derecha) es extremadamente común en clases de programación y lenguajes. Es recomendable que este tipo sea el **primero en verificar** al revisar filminas que combinan explicación con ejemplo de código.

### Sobre el presupuesto de imágenes

El valor en `slides-config.yaml` (`max_images_per_presentation: 4`) era un rezago de la configuración inicial del módulo EDU. Para una clase de 40 filminas, 12 imágenes es un mínimo razonable. Se recomienda actualizar el config directamente en lugar de depender del floor en el código.

---

*Informe generado el 18 de marzo de 2026.*  
*Paradigmas y Lenguajes de Programación 2026 — UNTDF Instituto IDEI*
