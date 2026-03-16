# Análisis Visual — Pipeline EDU Slides
**Fecha:** 16 de marzo de 2026  
**Analista:** Winston (Architect)  
**Scope:** 29 filminas — Tema 01: Conceptos Introductorios + Intro a TypeScript

---

## RESUMEN EJECUTIVO

Se identificaron **11 categorías de bugs** que afectan la calidad visual de las filminas. Los bugs se dividen en cuatro grupos arquitecturales:

| Grupo | Bugs | Impacto |
|-------|------|---------|
| **Layout y geometría** | 3 bugs | Títulos cortados, solapamiento texto-tabla |
| **Limpieza de contenido** | 4 bugs | Markdown visible, marcadores de lenguaje, secciones `##` |
| **Calidad de imágenes IA** | 2 bugs | Watermarks hex, texto inglés en imágenes |
| **Compatibilidad de API** | 2 bugs | `_rgb_color` faltante, modelo Gemini antiguo en edu-standalone |

---

## BUGS ENCONTRADOS POR FILMINA

### Filmina 01 — Portada (PORTADA)
**Errores críticos:**
- 🔴 Texto `#A9191B` visible en esquina superior derecha y pie de slide (watermark de imagen IA)
- 🔴 Texto desborda por debajo del límite inferior (`## BLOQUE 1 — ¿Por qué...` visible fuera de bordes)
- 🟡 Bullets con formato Markdown sin procesar (`**Paradigmas y Lenguajes...**`)
- 🟡 El título "Portada" en tamaño gigante se solapa con el subtítulo

### Filmina 02 — La pregunta incómoda (SOCRATICA)
**Errores críticos:**
- 🔴 Imagen IA tiene texto inglés ("The Uncomfortable Question") que se solapa con título español
- 🔴 `#A9191B` visible como texto en el cuerpo de la slide
- 🟡 Texto cuerpo con markdown sin procesar (`> *"La elección..."*`)
- 🟡 Texto cuerpo cortado por la imagen de fondo

### Filmina 03 — El costo de elegir mal (CONCEPTO-ABSTRACTO)
**Errores críticos:**
- 🔴 Imagen IA contiene `#A9191B` visible (watermark) y texto inglés "The Cost of Choosing Poorly"
- 🔴 Texto desborda por debajo del borde inferior
- 🟡 Markdown sin limpiar (`*Caso típico*`, `- Startup elige`)
- 🟡 Título cortado en 2 líneas solapando el contenido

### Filmina 04 — Perspectiva histórica (TABLA)
**Errores críticos:**
- 🔴 Título con TITLE_H insuficiente → "Perspectiva" desemboca en "históri" cortado
- 🔴 El título gigante cae encima de la fila de header de la tabla
- 🟡 Zone "left-top" (media anchura) demasiada estrecha para este título

### Filmina 05 — Criterios de evaluación de lenguajes (TABLA)
**Errores críticos:**
- 🔴 Título "Criterios de evaluación de lenguajes" se desborda en 3 líneas inmensas
- 🔴 Las 3 líneas del título solapan completamente la tabla
- 🟡 Zone "left-top" insuficiente para título largo

### Filmina 06 — Pregunta abierta (SOCRATICA)
**Errores:**
- 🔴 `#A9191B` visible en título (watermark)
- 🟡 Imagen IA muestra texto inglés "Open question" dos veces
- 🟡 Body incluye `## BLOQUE 2 —` como texto de contenido (sección doc, no contenido)

### Filmina 07 — ¿Qué es un paradigma? (SOCRATICA)
**Errores:**
- 🔴 Imagen IA muestra `#A9191B` watermark en pie de slide
- 🟡 Bullets con dash sin limpiar: `• - No es solo sintaxis`
- 🟡 Markdown sin limpiar: `**modelo mental**`

### Filmina 08 — Los factores que formaron los paradigmas (CONCEPTO-ABSTRACTO)
**Errores críticos:**
- 🔴 Título 4 líneas enormes solapando el cuerpo y la imagen de contenido
- 🔴 Body desborda la zona asignada (texto sale por el borde inferior)
- 🟡 Markdown: `**Arquitectura de Von Neumann**`
- 🟡 Bullets: `• - CPU + Memoria + Bus de datos`

### Filmina 09 — El cuello de botella de Von Neumann (CODIGO)
**Errores:**
- 🔴 Título cortado: solo muestra "El cuello de" (debería ser "El cuello de botella de Von Neumann")
- 🔴 `// TEXT` literal aparece como primera línea del código
- 🟡 Bloque de código muy escaso (3 líneas) en box que ocupa casi todo el slide

### Filmina 10 — Los 4 paradigmas fundamentales (TABLA)
**Errores críticos:**
- 🔴 "Los 4" y "paradigmas" en tamaño gigante caen encima de la tabla
- 🔴 "fundamentales" aparece como fila extra en la tabla (solapamiento)
- 🟡 `**Imperativo**`, `**Inmutable**` con markdown sin limpiar en las celdas

### Filmina 11 — Dominios de aplicación (TABLA)
**Errores:**
- 🔴 Título "Dominios de" + "apli..." parcialmente cortado solapando tabla
- 🟡 Zone título demasiado estrecha (half_w)

### Filminas 12–16 — Problemas repetitivos en tipo CODIGO/TABLA
- 🔴 Todas las slides de tipo `codigo` muestran `// TEXT` o `// TYPESCRIPT` como primera línea visible
- 🔴 Títulos cortados parcialmente: "La escalera de", "Von Neumann →", "Mismo algoritmo"
- 🟡 Espacios vacíos excesivos en code blocks con poco contenido

### Filminas 17–29 — Tipo CODIGO y TABLA mixto
- 🔴 Mismo problema con `// TYPESCRIPT`, `// TEXT` en código
- 🔴 Markdown en tablas: `**Ecosistema**`, `**IA**`, `**Funcional**`, etc.
- 🟡 Filminas 21, 28: código desborda el borde inferior con el último elemento cortado
- 🟡 Filmina 29 "Adelanto —" solo tiene 1 línea de código en un box enorme

---

## ANÁLISIS DE CAUSAS RAÍZ

### BUG-01: TITLE_H demasiado pequeño (820,000 EMU ≈ 64pt)
**Causa:** `TITLE_H = 820_000` con font size 46pt y zone de media anchura → solo cabe 1 línea, el texto desborda hacia zonas de contenido.
**Afecta:** F-03, F-04, F-05, F-08, F-09, F-10, F-11, F-13, F-14, F-15, F-17–F-28

### BUG-02: Zone título de media anchura para slides sin imagen derecha
**Causa:** `LAYOUT_MAP["codigo"]["title"] = "left-top"` usa `(m, m, half_w - m, th)` = mitad del ancho. Para slides `codigo` y `tabla` sin imagen en panel derecho, el título debería usar el ancho completo.
**Afecta:** F-09 a F-29 (todos los de tipo codigo y tabla)

### BUG-03: Marcadores de lenguaje `// LANG` en código
**Causa:** En `_build_slide_requests()`:
```python
code_text = "\n\n".join(
    f"// {cb.get('lang', '').upper() or 'CODE'}\n{cb['content']}"
    ...
)
```
El marcador de lenguaje se inserta como texto real del bloque de código.  
**Afecta:** F-09, F-11, F-12, F-13, F-14, F-15, F-17–F-22, F-25, F-26, F-27, F-28, F-29

### BUG-04: Markdown sin limpiar en `_blocks_to_text()`
**Causa:** La función no stripea `**bold**`, `*italic*`, `` `code` ``, ni `> blockquotes`.  
**Afecta:** F-01, F-02, F-03, F-07, F-08, F-16, F-17, F-21 (todas con body_blocks)

### BUG-05: Secciones `## BLOQUE N —` llegan al body
**Causa:** El parser `_finalize_slide()` solo intercepta `# titulo` (un solo `#`). Las líneas `## BLOQUE` caen al bloque de texto.  
**Afecta:** F-01, F-06

### BUG-06: Regex de bullets no stripea el guión `- `
**Causa:** Regex actual `^\s*[-*•\d]+[.)]\s*` requiere `[.)]` (punto o paréntesis) después del bullet. `- texto` tiene espacio, no `.` ni `)` → el guión queda como contenido.
**Resultado:** `• - No es solo sintaxis` en vez de `• No es solo sintaxis`.  
**Afecta:** F-07, F-08, F-03, F-06

### BUG-07: Código hex `{primary}` en prompts de imagen IA
**Causa:** En `_image_prompt()`:
```python
style = f"... paleta {primary} y gris oscuro ..."
```
`{primary}` = `#A9191B` → Imagen 4.0 lo interpreta como texto y lo renderiza en la imagen.  
**Afecta:** F-00-bg, F-01-bg, F-02-content, F-05-bg, F-06-bg, F-07-content (todas las imágenes IA)

### BUG-08: Imágenes IA generan texto en inglés
**Causa:** Los prompts de `_image_prompt()` dicen "sin texto, sin palabras, sin letras" pero en español. Imagen 4.0 puede ignorar estas instrucciones en español.  
**Fix:** Añadir las restricciones en inglés también: "no text, no words, no letters, no captions".

### BUG-09: edu-standalone usa modelo Gemini obsoleto (404)
**Causa:** `_gemini_image()` en edu-standalone usa `gemini-2.0-flash-exp-image-generation` con payload para `:generateContent`. Este modelo ya no está disponible (404). La versión de informe usa correctamente `imagen-4.0-generate-001` con `:predict`.

### BUG-10: edu-standalone falta `_rgb_color()` y `_normalize_alignment()`
**Causa:** Estas funciones fueron agregadas en informe/slides_pipeline.py durante la sesión de producción pero no se actualizaron en edu-standalone/scripts/slides_pipeline.py:
- Sin `_rgb_color()`: los fondos de página y fill de celdas fallan
- Sin `_normalize_alignment()`: los valores de alineación "LEFT"/"RIGHT" causan errores de API

### BUG-11: Tabla: markdown en celdas no se limpia  
**Causa:** En `add_native_table()`, el `cell` viene directamente del markdown sin stripear `**texto**`, `` `codigo` ``, etc.
**Afecta:** F-04, F-09, F-10, F-15, F-16 (celdas con `**texto**`)

---

## PLAN DE CORRECCIONES

### Fix A — Geometría del título
```
TITLE_H: 820,000 → 1,400,000 EMU  (≈110pt, cabe 2 líneas de 46pt)
Nueva zone: "full-title" = (m, m, w - 2*m, th)
LAYOUT_MAP["codigo"]["title"] = "full-title"
LAYOUT_MAP["tabla"]["title"] = "full-title"  
LAYOUT_MAP["tabla-comparativa"]["title"] = "full-title"
LAYOUT_MAP["timeline"]["title"] = "full-title"
LAYOUT_MAP["diagrama"]["title"] = "full-title"
LAYOUT_MAP["concepto-abstracto"]["title"] = "full-title"
Actualizar t_align logic: "full-title" → "LEFT"
```

### Fix B — Auto-fit en text boxes
```
Agregar updateShapeProperties con autoFit: SHAPE_AUTO_FIT  
a todo add_textbox() para que el texto se ajuste sin desbordarse
```

### Fix C — Limpieza de Markdown
```
Nueva función: _strip_markdown(text) → elimina **, *, `, _, ##
Aplicar en: _blocks_to_text(), add_native_table()
```

### Fix D — Filtrar secciones ## del parser
```
En _finalize_slide(): skip líneas que matchean  r"^#{2,}\s+"
```

### Fix E — Regex bullets
```
Cambiar: re.sub(r"^\s*[-*•\d]+[.)]\s*", "", bl)
Por:     re.sub(r"^\s*[-*•]\s+|\s*\d+[.)]\s+", "", bl)
```

### Fix F — Sin marcadores `// LANG` en código  
```
Cambiar el código de generación de code_text:
- Antes: f"// {lang.upper()}\n{content}"  
+ Después: content  (solo el código, sin el marcador)
```

### Fix G — Prompts de imagen sin hex ni texto inglés
```
Cambiar:
  f"paleta {primary} y gris oscuro sobre fondo blanco"
Por:
  "paleta rojo granate institucional y gris oscuro sobre fondo blanco,
   no text, no words, no letters, no numbers, no captions, no watermarks,
   no hex codes, purely abstract visual"
```

### Fix H — API de imagen: Imagen 4.0 en edu-standalone
```
Migrar _gemini_image() en edu-standalone:
  model: imagen-4.0-generate-001  
  endpoint: :predict  
  payload: instances[]/prompt + parameters/sampleCount
  response: predictions[]/bytesBase64Encoded
```

### Fix I — Agregar _rgb_color() y _normalize_alignment()
```
Agregar ambas funciones a edu-standalone/scripts/slides_pipeline.py  
Usadas en: updatePageProperties, updateTableCellProperties
```

---

## IMPACTO ESPERADO

| Mejora | Filminas afectadas | Resultado esperado |
|--------|-------------------|-------------------|
| Títulos full-width + auto-fit | Todas (29/29) | Sin títulos cortados ni solapamiento |
| Sin `// LANG` en código | 17 filminas de tipo codigo | Código limpio sin marcadores |
| Markdown limpio | ~20 filminas | Texto presentable sin `**` ni `*` |
| Sin hex en imágenes | Todas las con imágenes IA (8) | Sin watermarks `#A9191B` |
| Imagen 4.0 operativa | 8 imágenes IA | Generación funcional |
| Secciones ## filtradas | F-01, F-06 | Sin texto de sección en body |
| Bullets limpiados | ~10 filminas | `• texto` sin `- ` extra |
