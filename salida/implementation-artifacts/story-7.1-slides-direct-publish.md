# Story 7.1 — Pipeline de publicación directa de filminas (sin imágenes, tablas nativas, highlight, partición)

**ID:** S7.1
**Epic:** E7 — Publicación directa de filminas v2
**Status:** done
**Sprint:** 7
**Fecha de creación:** 2026-05-28
**Baseline:** c0b3095

---

## Descripción

**Como** docente que produce filminas con `/edu-design-topic`, **quiero** que la publicación a Google Slides sea directa via `slides_pipeline.py` sin pasos intermedios de imágenes ni validaciones de agente, que las tablas sean siempre nativas de Google Slides, que el código tenga highlight por lenguaje, que el layout se extraiga de un template PPTX con variables, que el contenido que no entra se auto-regule o se parta en slides adicionales, y que si la presentación supera 60 slides se generen 2 partes, **para** que el resultado sea limpio, completamente nativo, reproducible y sin dependencia de Gemini ni matplotlib.

---

## Contexto técnico de la historia

### Archivos impactados

| Archivo | Tipo de cambio | Descripción |
|---|---|---|
| `salida/edu-standalone/scripts/slides_pipeline.py` | MODIFICAR | Múltiples cambios (ver detalles por feature) |
| `salida/edu-standalone/_edu/agents/slides-publisher.md` | MODIFICAR | Eliminar mandato de `publish_loop.py`; permitir invocación directa |
| `salida/edu-standalone/_edu/slides-config.yaml` | MODIFICAR | Agregar campo `pptx_template_path` |
| `salida/edu-standalone/requirements.txt` | MODIFICAR | Agregar `python-pptx` |

### Archivos NO modificar
- `salida/edu-standalone/scripts/publish_loop.py` — permanece como opción avanzada, no obligatorio
- `salida/edu-standalone/_edu/schemas/schema-registry.json` — inmutable
- `salida/edu-standalone/_edu/schemas/filmina-slide.schema.json` — inmutable
- `_edu/workflows/topic-cycle/workflow.md` — brownfield, sin cambios
- Cualquier otro script del pipeline distinto a `slides_pipeline.py`

### Dependencias
- `python-pptx >= 1.0.2` — nueva dependencia para lectura de template PPTX
- `google-api-python-client` — ya existe
- `google-auth-oauthlib` — ya existe

### Constantes relevantes en `slides_pipeline.py`
```python
MIN_READABLE_CODE_PT = 9    # umbral mínimo de fuente para código — si quedara menor, se parte
SLIDES_PER_PRESENTATION = 60  # máximo slides por presentación antes de dividir
EMU_PER_PT = 12_700
SLIDE_W = 9_144_000
SLIDE_H = 5_143_500
```

---

## Criterios de Aceptación

### CA-1 — Script directo (sin publish_loop obligatorio)

*Dado que* existe `filminas.md` en una carpeta de tema,  
*cuando* se ejecuta `python scripts/slides_pipeline.py {topic_folder}`,  
*entonces* la presentación se publica en Google Slides sin necesidad de `publish_loop.py`, y la URL queda guardada en `{topic_folder}/slides/slides-url.txt`.

*Dado que* el agente `slides-publisher.md` ejecuta la publicación,  
*cuando* el docente pide publicar con `[PB]`,  
*entonces* el agente puede usar `python scripts/slides_pipeline.py {topic_folder}` directamente; `publish_loop.py` es opcional pero no obligatorio.

### CA-2 — Sin imágenes, todo nativo

*Dado que* un slide tiene tablas Markdown (cualquier tamaño),  
*cuando* se publica,  
*entonces* las tablas son siempre objetos nativos de Google Slides (`createTable` API), nunca imágenes PNG ni Drive uploads. No se invoca `_render_table_png` ni `_upload_drive` para tablas.

*Dado que* el plan JSON tiene `image.layer != "none"` en algún slide,  
*cuando* se ejecuta el pipeline,  
*entonces* el campo se ignora silenciosamente: no se genera imagen Gemini, no se sube nada a Drive por imágenes. El slide se publica sin imagen de fondo.

*Dado que* no se generan imágenes,  
*cuando* se ejecuta el pipeline,  
*entonces* `generate_assets` no hace network calls a Gemini ni uploads a Drive; la fase de assets puede omitirse completamente o ser un no-op.

### CA-3 — Layout desde template PPTX

*Dado que* `slides-config.yaml` tiene `pptx_template_path: "_edu/templates/slides-template.pptx"`,  
*cuando* el archivo .pptx existe,  
*entonces* el pipeline extrae las posiciones (en EMU) de los placeholders `{titulo}`, `{subtitulo}`, `{contenido}` de la primera slide del template usando python-pptx, y los usa como zonas para title, body y code/table respectivamente.

*Dado que* el template PPTX tiene posicionados los placeholders,  
*cuando* se calculan las zonas `{header}` y `{footer}`,  
*entonces* `header` = rectángulo desde `(0, 0)` hasta la coordenada y mínima del contenido, y `footer` = rectángulo desde la coordenada y máxima del contenido hasta `SLIDE_H`; ningún elemento de contenido se renderiza en esas zonas.

*Dado que* `pptx_template_path` no está configurado o el archivo no existe,  
*cuando* se ejecuta el pipeline,  
*entonces* el pipeline usa las constantes `ZONES` hardcodeadas actuales como fallback sin error.

**Especificación técnica de la función:**
```python
def _load_template_zones(pptx_path: Path, slide_w: int = SLIDE_W, slide_h: int = SLIDE_H) -> dict[str, tuple] | None:
    """
    Lee un .pptx y extrae las posiciones de placeholders como zonas EMU.
    Busca en slide layouts y slide masters.
    Retorna dict con keys: titulo, subtitulo, contenido, header, footer.
    Retorna None si el archivo no existe o no tiene los placeholders esperados.
    
    Los placeholders se detectan por nombre (case-insensitive):
      - "titulo" o "title" → zona del título
      - "subtitulo" o "subtitle" → zona del subtítulo  
      - "contenido" o "content" o "body" → zona del contenido principal
    
    EMU conversion: python-pptx usa Emu natively (int); no requiere conversión.
    """
```

### CA-4 — Auto-regulación de tamaños de letra en tablas

*Dado que* una tabla tiene muchas filas o columnas y no entraría a tamaño estándar (13pt),  
*cuando* se renderiza como tabla nativa en `add_native_table`,  
*entonces* el font size se reduce automáticamente usando `_fit_table_font_size()` hasta un mínimo de 7pt para que la tabla entre en la zona asignada.

*Dado que* la tabla tiene filas > 8 o columnas > 6,  
*cuando* se calcula el tamaño,  
*entonces* el tamaño resultante es ≤ 10pt para el body y ≤ 11pt para el header.

**Especificación técnica:**
```python
def _fit_table_font_size(
    n_rows: int,
    n_cols: int,
    geo: tuple[int, int, int, int],
    preferred_body: float = 13.0,
    preferred_header: float = 14.0,
    min_size: float = 7.0,
) -> tuple[float, float]:
    """
    Retorna (header_font_size, body_font_size) ajustados para que la tabla entre en geo.
    Modelo: cada fila ocupa aprox size * 1.6pt de alto; cada col ocupa aprox size * 7pt de ancho.
    """
```

### CA-5 — División de código grande en 2 slides

*Dado que* un slide tiene un único bloque de código que a `MIN_READABLE_CODE_PT` no entraría en la zona asignada,  
*cuando* `_split_oversized_code_slides` procesa ese slide,  
*entonces* el bloque se divide en 2 slides consecutivas:
- Slide A: título original + ` (1/2)`, primeras N/2 líneas del código
- Slide B: título original + ` (2/2)`, líneas restantes del código
- Ambas tienen `type: "codigo"` y `layout` de `codigo`

*Dado que* el código entra a tamaño ≥ `MIN_READABLE_CODE_PT`,  
*cuando* se procesa,  
*entonces* no se divide (comportamiento actual preservado).

*Dado que* el código tiene múltiples bloques (comportamiento actual),  
*cuando* se procesa,  
*entonces* el split existente de múltiples bloques sigue funcionando igual.

### CA-6 — Separación de filminas mixtas

*Dado que* un slide de tipo `concepto-mixto`, `tabla-mixta` o `demo` tiene `body_blocks` con ≥ 2 ítems Y `code_blocks` no vacíos,  
*cuando* la nueva función `_split_mixed_slides` pre-procesa antes de `_split_oversized_code_slides`,  
*entonces* el slide original se reemplaza por 2 slides consecutivas:
- Slide A: mismo título + " — Conceptos", tipo `concepto-abstracto`, solo `body_blocks`, sin `code_blocks`
- Slide B: mismo título + " — Código", tipo `codigo`, solo `code_blocks`, sin `body_blocks`

*Dado que* un slide tiene `body_blocks` Y `tables` no vacías,  
*cuando* se procesa,  
*entonces* se divide en:
- Slide A: mismo título + " — Conceptos", tipo `concepto-abstracto`, solo `body_blocks`
- Slide B: mismo título + " — Tabla", tipo `tabla`, solo la tabla, con `body_blocks: []`

*Dado que* un slide tiene `body_blocks` con < 2 ítems sustanciales Y código/tabla,  
*cuando* se procesa,  
*entonces* NO se divide (el subtítulo puede quedar en el mismo slide de código/tabla).

**Especificación técnica:**
```python
def _split_mixed_slides(slides: list[dict]) -> list[dict]:
    """
    Pre-procesa slides con body + código o body + tabla.
    Un body es "sustancial" si tiene ≥ 2 bloques (texto, lista o heading).
    Se ejecuta ANTES de _split_oversized_code_slides en el flujo de _publish_part.
    """
```

### CA-7 — Syntax highlighting de código

*Dado que* un slide tiene `code_blocks` con `lang` conocido (python, java, javascript, haskell, c, cpp, scala, sql, bash, kotlin),  
*cuando* se renderiza el textbox de código,  
*entonces* las expresiones del lenguaje reciben colores específicos:
- Keywords: `#0000CC` (azul)
- Strings y caracteres: `#007700` (verde oscuro)
- Comentarios: `#999999` (gris medio)
- Números: `#AA0000` (rojo oscuro)
- Tipos/clases: `#666600` (oliva)
- Decoradores/anotaciones: `#AA6600` (marrón)
- Operadores especiales (`->`, `=>`, `::`, `|>`): `#884400` (terracota)

*Dado que* `lang` es `"text"`, `""` o no reconocido,  
*cuando* se renderiza,  
*entonces* NO se aplica highlight (todo texto en color base `#222222`).

*Dado que* la función de highlight falla o produce un error,  
*cuando* ocurre el error,  
*entonces* se ignora silenciosamente y el código se muestra en color uniforme (degradación elegante).

**Especificación técnica:**
```python
# Tokenizador regex liviano (sin dependencias externas pesadas):
HIGHLIGHT_TOKENS: dict[str, dict[str, str]] = {
    "python": {
        "keyword": r"\b(def|class|import|from|return|if|elif|else|for|while|in|not|and|or|is|None|True|False|lambda|with|as|try|except|finally|raise|yield|async|await|pass|break|continue|global|nonlocal|del)\b",
        "builtin": r"\b(print|len|range|str|int|float|list|dict|set|tuple|type|isinstance|hasattr|getattr|open|super)\b",
        "string": r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"[^"\n]*"|\'[^\'\n]*\')',
        "comment": r"#[^\n]*",
        "number": r"\b\d+(\.\d+)?\b",
        "decorator": r"@\w+",
    },
    "java": {
        "keyword": r"\b(public|private|protected|class|interface|extends|implements|static|final|void|int|String|boolean|return|new|if|else|for|while|import|package|try|catch|throw|throws|super|this|null|true|false)\b",
        "string": r'"[^"\n]*"',
        "comment": r"//[^\n]*|/\*[\s\S]*?\*/",
        "number": r"\b\d+(\.\d+)?\b",
        "annotation": r"@\w+",
    },
    "haskell": {
        "keyword": r"\b(data|type|class|instance|where|let|in|do|of|case|if|then|else|import|module|deriving|newtype|infixl|infixr)\b",
        "string": r'"[^"\n]*"',
        "comment": r"--[^\n]*|\{-[\s\S]*?-\}",
        "number": r"\b\d+(\.\d+)?\b",
        "operator": r"(->|=>|::|<-|\|>|\$|@|\\\\)",
    },
    # ... etc
}

def _apply_syntax_highlighting(
    tb_id: str,
    code_text: str,
    lang: str,
) -> list[dict]:
    """
    Retorna lista de updateTextStyle requests con foregroundColor por token.
    Usa tokenizador regex no-overlapping (prioridad: comment > string > keyword > rest).
    Si lang no está en HIGHLIGHT_TOKENS, retorna [].
    """
```

### CA-8 — División en 2 presentaciones si > 60 slides

*Dado que* el total de slides (post-splits) es > `SLIDES_PER_PRESENTATION` (60),  
*cuando* se ejecuta la publicación,  
*entonces* se crean 2 presentaciones en Google Slides:
- Parte 1: primeras ⌈total/2⌉ slides, título = `{titulo_tema} — Parte 1`, URL en `slides-url-1.txt`
- Parte 2: slides restantes, título = `{titulo_tema} — Parte 2`, URL en `slides-url-2.txt`

*Dado que* el total es ≤ 60,  
*cuando* se publica,  
*entonces* se crea una única presentación, URL en `slides-url.txt` (comportamiento actual preservado).

*Dado que* se crean 2 partes,  
*cuando* termina la publicación,  
*entonces* el output muestra:
```
✅ Parte 1: https://docs.google.com/presentation/d/{id1}/edit  (slides 1-N)
✅ Parte 2: https://docs.google.com/presentation/d/{id2}/edit  (slides N+1-Total)
```

---

## Tareas de implementación

El agente de desarrollo debe ejecutar estas tareas en orden:

### TAREA 1: Actualizar `requirements.txt`
- Agregar `python-pptx>=1.0.2` en `salida/edu-standalone/requirements.txt`

### TAREA 2: Agregar `pptx_template_path` en `slides-config.yaml`
- En `salida/edu-standalone/_edu/slides-config.yaml`, agregar campo:
  ```yaml
  pptx_template_path: "_edu/templates/slides-template.pptx"  # opcional; si no existe, usa zonas hardcodeadas
  ```

### TAREA 3: Implementar `_load_template_zones` en `slides_pipeline.py`
- Nueva función arriba de `_zones()` (antes de `ZONES = _zones()`)
- Usa `python-pptx`: `from pptx import Presentation` con importación tolerante (try/except ImportError)
- Lee placeholders del primer slide layout o slide master que los tenga
- Detecta por nombre (case-insensitive): titulo/title, subtitulo/subtitle, contenido/content/body
- Extrae `.left`, `.top`, `.width`, `.height` (ya en EMU en python-pptx)
- Calcula `header` y `footer` a partir de los bordes del contenido
- Si falla: retorna None (no bloquea el pipeline)

### TAREA 4: Modificar `_build_slide_requests` — tablas siempre nativas
- Sección "── 5. Tablas ──": reemplazar el bloque condicional por llamada directa a `add_native_table`
- Eliminar toda la lógica de fallback a imagen Drive para tablas
- `add_native_table` debe llamar a `_fit_table_font_size` para calcular el tamaño dinámico
- Tabla de cualquier dimensión → siempre `createTable` API

Código actual a reemplazar (en `_build_slide_requests`):
```python
    if table_zone and table_zone != "none":
        if tables and _should_use_native_table(tables[0]):
            add_native_table(tables[0], table_zone)
        else:
            used_image = False
            for ta in ta_list:
                if ta.get("drive_id"):
                    add_image(_drive_url(ta["drive_id"]), table_zone)
                    used_image = True
                    break
            if not used_image and tables:
                add_native_table(tables[0], table_zone)
```

Código nuevo:
```python
    if table_zone and table_zone != "none" and tables:
        add_native_table(tables[0], table_zone)
```

### TAREA 5: Implementar `_fit_table_font_size`
- Nueva función en sección helpers, junto a `_fit_code_font_size` y `_fit_text_font_size`
- Parámetros: `(n_rows, n_cols, geo, preferred_body=13.0, preferred_header=14.0, min_size=7.0) -> tuple[float, float]`
- Modelo simple: `row_height_pt = size * 1.6; col_width_pt = size * 7.0`
- Retorna `(header_size, body_size)` que entran en `(geo[2], geo[3])`

### TAREA 6: Actualizar `add_native_table` para usar `_fit_table_font_size`
- Dentro de `add_native_table`, reemplazar el bloque hardcodeado de font sizes (13/12/10/9) por llamada a `_fit_table_font_size(n_rows, n_cols, geo)`
- El `(x, y, w, h) = geo` ya está disponible en la función
- Pasar `header_font, body_font = _fit_table_font_size(n_rows, n_cols, (x, y, w, h))`

### TAREA 7: Implementar `_split_mixed_slides`
- Nueva función en sección de pre-procesado (antes de `_split_oversized_code_slides`)
- Detecta slides con body sustancial (≥ 2 bloques) + código O tabla
- Crea dos slides según lógica de CA-6
- IDs de splits: `{slide['id']}-info` y `{slide['id']}-code` (o `-table`)
- El layout de Slide A usa `LAYOUT_MAP["concepto-abstracto"]`; el de Slide B usa `LAYOUT_MAP["codigo"]` o `LAYOUT_MAP["tabla"]`

### TAREA 8: Extender `_split_oversized_code_slides` para un solo bloque grande
- Actualmente cuando `len(code_blocks) <= 1`: `result.append(slide); continue` (no divide)
- NUEVO comportamiento: cuando el único bloque no entra a `MIN_READABLE_CODE_PT`:
  ```python
  lines = code_blocks[0]["content"].splitlines()
  half = len(lines) // 2
  block_a = {"lang": code_blocks[0]["lang"], "content": "\n".join(lines[:half])}
  block_b = {"lang": code_blocks[0]["lang"], "content": "\n".join(lines[half:])}
  # Slide A: título + " (1/2)", code_block = [block_a]
  # Slide B: título + " (2/2)", code_block = [block_b]
  ```

### TAREA 9: Implementar `_apply_syntax_highlighting`
- Nueva función en sección de helpers de código
- Diccionario `HIGHLIGHT_TOKENS` con patrones para: python, java, javascript, haskell, c, cpp, scala, sql, bash, kotlin
- Algoritmo: tokenizar sin solapamiento (orden: comment > string > decorator/annotation > keyword > builtin/type > number > operator)
- Retorna lista de `updateTextStyle` requests
- Llamar desde dentro del bloque de renderizado de código en `_build_slide_requests`, después de `add_textbox_geo(code_text, ...)`

### TAREA 10: Actualizar `_publish_part` para usar `_split_mixed_slides`
- En la función `_publish_part`, antes del llamado a `_split_oversized_code_slides`:
  ```python
  slides = _split_mixed_slides(slides)
  slides = _split_oversized_code_slides(slides, config, page_w, page_h)
  ```

### TAREA 11: Verificar división en 2 presentaciones (CA-8)
- Revisar la función principal `publish_slides` (o equivalente) en `slides_pipeline.py`
- Verificar que cuando `len(all_slides) > SLIDES_PER_PRESENTATION`:
  - Se llama `_publish_part(..., slides[:mid], ..., url_suffix="-1")` 
  - Se llama `_publish_part(..., slides[mid:], ..., url_suffix="-2")`
  - Los títulos incluyen ` — Parte 1` y ` — Parte 2`
- Si la lógica no está completa, implementarla
- Verificar que `slides-url-1.txt` y `slides-url-2.txt` se escriben correctamente

### TAREA 12: Actualizar `slides-publisher.md` — publicación directa
- En la sección `[PB] Publish — Pipeline Automático`, reemplazar:
  ```
  Diego DEBE usar publish_loop.py — NUNCA llamar slides_pipeline.py directamente.
  ```
  Por:
  ```
  Diego puede usar slides_pipeline.py directamente O publish_loop.py para validación extendida.
  
  Comando directo (recomendado para publicación normal):
    python {project-root}/scripts/slides_pipeline.py {topic_folder}
  
  Comando con validación extendida (opcional):
    python {project-root}/scripts/publish_loop.py {topic_folder} --course {course_id}
  ```
- Eliminar la regla `NUNCA llamar slides_pipeline.py directamente`
- El resto del flujo del agente (plan semántico, consulta de registro, etc.) permanece

### TAREA 13: Eliminar fase de assets de Gemini/Drive de la función principal
- En `main()` de `slides_pipeline.py`, la fase `--assets-only` y la llamada a `generate_assets` pueden permanecer como no-op (para no romper CLI existente)
- La fase de publicación (`_publish_part`) ya NO debe llamar `generate_assets` antes de publicar
- Verificar que `_publish_part` no hace Drive uploads ni Gemini calls

---

## Guardrails para el agente de desarrollo

### NO modificar
- `publish_loop.py` — no tocar
- `schema-registry.json` — inmutable
- `filmina-slide.schema.json` — inmutable
- `validate_plan.py`, `repair_plan.py` — no tocar
- Cualquier agente excepto `slides-publisher.md`
- El formato de `plan-filminas-{tema}.json` — debe seguir siendo válido

### Principio de degradación elegante
- Si `python-pptx` no está instalado → usar ZONES hardcodeadas (sin error fatal)
- Si el template .pptx no existe → usar ZONES hardcodeadas (sin error fatal)
- Si el highlight falla → mostrar código en color uniforme (sin error fatal)
- Si la división de slides falla → publicar slide original sin dividir (sin error fatal)

### Compatibilidad hacia atrás
- `slides_pipeline.py --plan-only` debe seguir funcionando
- `slides_pipeline.py --publish-only` debe seguir funcionando
- Los planes JSON existentes (ya generados) deben seguir siendo publicables
- El plan JSON sigue teniendo el campo `table_assets` (puede ser lista vacía) para compatibilidad

### Seguridad
- No hardcodear credenciales en ningún lugar
- El token OAuth se sigue guardando en `_edu/token_slides.json`
- No se hacen calls a APIs externas innecesariamente

---

## Criterio de completitud

La story está completa cuando:
1. `python scripts/slides_pipeline.py {topic_folder}` publica sin pasar por `publish_loop.py`
2. Ninguna tabla se renderiza como PNG; todas son objetos nativos Google Slides
3. Ninguna imagen Gemini se genera durante la publicación
4. Un slide con `body + código` se divide en 2 slides automáticamente
5. Un bloque de código que no entra a 9pt se divide en 2 slides con `(1/2)` / `(2/2)`
6. El código Python muestra keywords en azul, strings en verde, comentarios en gris
7. Si hay > 60 slides se crean 2 presentaciones con `— Parte 1` y `— Parte 2` en el título
8. Si existe `_edu/templates/slides-template.pptx` con placeholders, las zonas se extraen de él
9. `slides-publisher.md` no bloquea invocación directa de `slides_pipeline.py`
10. Todos los tests existentes en `test_pipeline.py` y `test_slides_contract.py` siguen pasando

---

## Notas de implementación adicionales

### Sobre python-pptx y la extracción de zonas
```python
from pptx import Presentation
from pptx.util import Emu

def _load_template_zones(pptx_path: Path, ...) -> dict | None:
    try:
        prs = Presentation(str(pptx_path))
    except Exception:
        return None
    
    # Buscar en slide_layouts primero, luego slide_master
    placeholders = {}
    for layout in prs.slide_layouts:
        for ph in layout.placeholders:
            name = (ph.name or "").lower()
            left = int(ph.left or 0)
            top = int(ph.top or 0)
            width = int(ph.width or 0)
            height = int(ph.height or 0)
            if "titulo" in name or "title" in name:
                placeholders["titulo"] = (left, top, width, height)
            elif "subtitulo" in name or "subtitle" in name:
                placeholders["subtitulo"] = (left, top, width, height)
            elif "contenido" in name or "content" in name or "body" in name:
                placeholders["contenido"] = (left, top, width, height)
        if len(placeholders) >= 2:
            break
    
    if "titulo" not in placeholders:
        return None
    
    # Calcular header y footer
    min_content_y = min(v[1] for v in placeholders.values())
    max_content_y = max(v[1] + v[3] for v in placeholders.values())
    slide_w = int(prs.slide_width)
    slide_h = int(prs.slide_height)
    
    placeholders["header"] = (0, 0, slide_w, min_content_y)
    placeholders["footer"] = (0, max_content_y, slide_w, slide_h - max_content_y)
    
    return placeholders
```

### Sobre el tokenizador de highlight (sin dependencias externas)
El tokenizador debe ser regex-only (sin `pygments` ni similares) para mantener dependencias mínimas. Usar `re.finditer` con non-overlapping matches. Prioridad: comment > string > decorator > keyword > number > operator. Asignar spans (startIndex, endIndex) en el texto plano del code_text para luego mapear a requests de Google Slides API.

### Sobre el autofit de fuente en tablas nativas
Google Slides API no soporta `autofit` en tablas. El ajuste de fuente debe calcularse ANTES de hacer el request. Usar `_fit_table_font_size` que retorna los pt sizes apropiados para que la tabla entre visualmente.

### Sobre `add_native_table` — tablas grandes (> 8 filas o > 5 cols)
Actualmente la función existe en `_build_slide_requests` con lógica de font size hardcodeado (13/12/10/9). Reemplazar esa lógica por `_fit_table_font_size`. La función NO necesita cambiar su firma ni ubicación.

### Orden de pre-procesado en `_publish_part`
```python
# PRE-PROCESADO — ORDEN OBLIGATORIO:
slides = _split_mixed_slides(slides)           # 1. separar info de código/tabla
slides = _split_oversized_code_slides(slides, config, page_w, page_h)  # 2. partir código largo
# luego render normal...
```

---

## Suggested Review Order

**Entrada del pipeline y carga de zonas desde PPTX**

- Arranque de zona: lee pptx_template_path y sobreescribe ZONES globalmente si el template existe.
  [`slides_pipeline.py:2527`](../edu-standalone/scripts/slides_pipeline.py#L2527)

- Extracción de placeholders del template PPTX → zonas EMU con fallback elegante.
  [`slides_pipeline.py:176`](../edu-standalone/scripts/slides_pipeline.py#L176)

**Pre-procesado de slides (split logic)**

- `_split_mixed_slides` — divide slides con body sustancial + código o tabla en 2 consecutivas.
  [`slides_pipeline.py:2128`](../edu-standalone/scripts/slides_pipeline.py#L2128)

- `_split_oversized_code_slides` — ahora parte un solo bloque ilegible en `(1/2)` / `(2/2)`.
  [`slides_pipeline.py:2218`](../edu-standalone/scripts/slides_pipeline.py#L2218)

- `_publish_part` — orden obligatorio: `_split_mixed_slides` → `_split_oversized_code_slides`.
  [`slides_pipeline.py:2347`](../edu-standalone/scripts/slides_pipeline.py#L2347)

**Tablas nativas (CA-2)**

- `_build_slide_requests` sección tablas — siempre `add_native_table`, sin Drive fallback.
  [`slides_pipeline.py:1987`](../edu-standalone/scripts/slides_pipeline.py#L1987)

- `add_native_table` — font sizes calculados dinámicamente por `_fit_table_font_size`.
  [`slides_pipeline.py:1876`](../edu-standalone/scripts/slides_pipeline.py#L1876)

- `_fit_table_font_size` — modelo lineal (row_height=size×1.6pt, col_width=size×7pt).
  [`slides_pipeline.py:663`](../edu-standalone/scripts/slides_pipeline.py#L663)

**Syntax highlighting de código (CA-7)**

- `HIGHLIGHT_TOKENS` — diccionario de patrones regex por lenguaje (10 lenguajes).
  [`slides_pipeline.py:746`](../edu-standalone/scripts/slides_pipeline.py#L746)

- `_apply_syntax_highlighting` — tokenizador no-overlapping → `updateTextStyle` requests.
  [`slides_pipeline.py:819`](../edu-standalone/scripts/slides_pipeline.py#L819)

- Integración en `_build_slide_requests` — se aplica sobre el textbox de código explícito.
  [`slides_pipeline.py:2085`](../edu-standalone/scripts/slides_pipeline.py#L2085)

**División en 2 presentaciones (CA-8)**

- `publish_slides` — títulos con `— Parte 1` / `— Parte 2`; output con rangos de slides.
  [`slides_pipeline.py:2435`](../edu-standalone/scripts/slides_pipeline.py#L2435)

**Assets como no-op (CA-2, CA-13)**

- `generate_assets` — convertida a no-op: sin Gemini, sin Drive, sin matplotlib.
  [`slides_pipeline.py:1505`](../edu-standalone/scripts/slides_pipeline.py#L1505)

**Agente y configuración**

- `slides-publisher.md` — FASE 2+3 permite invocación directa de `slides_pipeline.py`.
  [`slides-publisher.md:101`](../edu-standalone/_edu/agents/slides-publisher.md#L101)

- `slides-config.yaml` — nuevo campo `pptx_template_path`.
  [`slides-config.yaml:8`](../edu-standalone/_edu/slides-config.yaml#L8)

- `requirements.txt` — nueva dependencia `python-pptx>=1.0.2`.
  [`requirements.txt:32`](../edu-standalone/requirements.txt#L32)
