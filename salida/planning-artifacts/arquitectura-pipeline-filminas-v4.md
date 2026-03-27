---
stepsCompleted: [1]
inputDocuments:
  - salida/planning-artifacts/arquitectura-pipeline-filminas-v3.md
workflowType: architecture
project_name: paradigmas2026
user_name: Matiasgel
date: 2026-03-27
---

# Arquitectura Pipeline EDU Filminas v4
## Calibración Interactiva + Separación Tablas/Imágenes + Correcciones de Publicación

**Proyecto:** Paradigmas y Lenguajes de Programación 2026  
**Arquitecto:** Winston (BMAD Architect)  
**Fecha:** 27 de marzo de 2026  
**Estado:** REVISADO — APROBADO CON CORRECCIONES  
**Base:** Arquitectura v3 (implementada) + issues detectados en producción (tema 3)

---

## 0. Hallazgos de la Revisión Arquitectónica

| # | Hallazgo | Impacto | Acción |
|---|---|---|---|
| H-01 | **Diagnóstico 1.1 es parcialmente incorrecto**: el pipeline ya usa `_render_table_png` (matplotlib) para tablas, no Gemini. Sin embargo hay **dos copias** del pipeline con comportamientos distintos. | Medio | Consolidar en uno solo. |
| H-02 | **Dos copias del pipeline**: `scripts/slides_pipeline.py` (formato viejo `background_image/content_image`) y `salida/edu-standalone/scripts/slides_pipeline.py` (formato v3 `image.layer`). La raíz es la que se ejecuta. | Alto | Definir cuál es la fuente de verdad y eliminar el otro o sincronizar. |
| H-03 | **Pipeline raíz no lee schema registry**: tiene `TYPE_LAYOUT_MAP` y `IMAGE_STRATEGY` hardcodeados, violando principio P6 de v3. | Alto | Migrar a lectura de schema registry. |
| H-04 | **Plan existente del tema 3 tiene `timeline.layout.table = "none"`** y no se va a corregir solo con cambiar el schema — hay que regenerar el plan. | Bajo | Regenerar plan del tema 3 antes de republicar. |
| H-05 | **Calibración requiere OAuth mínimo una vez** para descargar el template como referencia. `python-pptx` sin template descargado genera slides genéricas que no coinciden con el template real. | Medio | La calibración se ejecuta con OAuth para descarga de template; luego itera localmente con `python-pptx`. |

---

## 1. Diagnóstico — Problemas Detectados en v3

### 1.1 Drift entre dos copias del pipeline (Bug estructural)
**Observado:** Existen dos versiones del pipeline:  
- `scripts/slides_pipeline.py` — formato viejo (`background_image`, `content_image`), constantes hardcodeadas, no lee schema registry  
- `salida/edu-standalone/scripts/slides_pipeline.py` — formato v3 (`image.layer`), lee schema registry  

Ambas usan `_render_table_png` con matplotlib para tablas (no Gemini), pero la versión raíz no cumple los principios P5-P6 de la arquitectura v3.  
**Impacto:** El pipeline que se ejecuta (`scripts/slides_pipeline.py`) viola la arquitectura v3. El que cumple (`salida/edu-standalone/`) no se usa.

### 1.2 Filminas timeline incompletas (F-06, F-07)
**Observado:** El tipo `timeline` tiene `layout.table = "none"` en el schema registry, por lo que la tabla renderizada como PNG se sube a Drive pero nunca se coloca en la slide.  
**Impacto:** Las diapositivas de timeline aparecen sin contenido principal.

### 1.3 Ausencia de calibración previa al pipeline
**Observado:** El agente genera el plan y ejecuta directamente, sin verificar que los parámetros de layout (posiciones en EMU, tamaños de fuente, colores, zonas de texto) sean correctos para el template de Google Slides del docente.  
**Impacto:** Primera publicación siempre requiere correcciones manuales post-facto. Deuda acumulada de ajustes que no quedan registrados.

---

## 2. Principios Nuevos de v4

### P8 — Consolidación del Pipeline
Una sola copia del pipeline es la fuente de verdad. Se define `scripts/slides_pipeline.py` como la copia canónica. Debe migrar al formato v3 (`image.layer`) y leer del schema registry (sin constantes propias). La copia en `salida/edu-standalone/` se sincroniza desde la raíz.

### P9 — Calibración como Fase 0 Explícita
Antes de cualquier publicación de un tema, el docente pasa por una fase interactiva de calibración.  
La calibración usa OAuth **una sola vez** para descargar el template de Google Slides como base. Luego itera localmente con `python-pptx` generando slides de prueba en `calibracion/` (carpeta gitignored).  
Hace preguntas específicas sobre posición y diseño, y persiste las respuestas en `_edu/calibracion-config.json`.  
El pipeline v4 lee `calibracion-config.json` como override de los valores por defecto del pipeline runtime.

### P10 — Fix de Timeline: tabla como contenido principal
El tipo `timeline` requiere que la tabla renderizada sea el contenido central de la slide.  
El layout de `timeline` se actualiza en el schema registry para incluir `table: "table-main"`.  
Los body_blocks son introductorios (heading + lista corta), no el cuerpo principal.

---

## 3. Arquitectura de la Fase de Calibración

### 3.1 Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  FASE 0 — CALIBRACIÓN (nueva, ejecuta antes del pipeline)      │
│                                                                 │
│  TRIGGER: Primer uso || cambio de template || comando manual    │
│                                                                 │
│  INPUT:   _edu/slides-config.yaml (design system)              │
│           _edu/schemas/schema-registry.json                     │
│                                                                 │
│  OUTPUT:  _edu/calibracion-config.json  (persiste)             │
│           calibracion/slide-XX.png      (gitignored)            │
│                                                                 │
│  INTERACCIÓN: El agente hace preguntas → docente responde       │
│               → genera slide de prueba → docente aprueba/ajusta │
│               → Loop hasta que docente dice "listo"             │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Script: `calibrate_pipeline.py`

**Responsabilidades:**
1. Leer `slides-config.yaml` y `schema-registry.json`
2. Crear una presentación temporal en Google Slides (o localmente en PNG via `python-pptx`)
3. Para cada zona calibrable, generar un slide de prueba y hacer preguntas al docente
4. Persistir respuestas en `_edu/calibracion-config.json`
5. Loop interactivo hasta que el docente confirme cierre

**Zonas calibrables (preguntas del agente):**

| Zona | Pregunta | Parámetro en config |
|---|---|---|
| Título portada | ¿El título queda centrado y con buen margen? | `title_zone.top`, `title_zone.left`, `title_zone.width` |
| Color primario | ¿El color bordo #8B0000 se ve bien sobre el fondo blanco? | `palette.primary` |
| Tamaño fuente título | ¿El título es legible desde 3 metros? (30pt) | `typography.title.size` |
| Tamaño fuente cuerpo | ¿Los bullets del cuerpo son cómodos de leer? (16pt) | `typography.body.size` |
| Zona imagen derecha | ¿La imagen ocupa bien el panel derecho sin recortar contenido? | `zones.right_half.left`, `zones.right_half.width` |
| Tabla principal | ¿Las columnas de la tabla caben sin overflow? | `zones.table_main.width`, `table_render.col_widths` |
| Código | ¿El bloque de código es legible y no se desborda? | `zones.code.height`, `typography.code.size` |

### 3.3 Flujo de Interacción del Agente

```
agente: "Voy a generar una slide de portada de prueba. Publicando en calibracion/..."
        → genera slide F-CAL-01 (portada) en PNG/Slides
        → muestra thumbnail
agente: "¿El título queda bien posicionado? [s/n o ajuste libre]"
docente: "el título está muy arriba"
agente: → ajusta top_emu en config
        → regenera slide
        → muestra nuevo thumbnail
agente: "¿Mejor? [s/continuar/nueva prueba]"
docente: "sí"
agente: → pasa a siguiente zona
        ...
agente: "¿Querés probar otro tipo de slide o cerramos calibración?"
docente: "probá una de código"
agente: → genera F-CAL-05 (codigo) con ejemplo genérico
        → muestra thumbnail
        ...
docente: "listo, corta calibración"
agente: → guarda calibracion-config.json
        → "✅ Calibración completada y guardada en _edu/calibracion-config.json"
```

### 3.4 Formato de `_edu/calibracion-config.json`

```json
{
  "$version": "calibracion/v1",
  "calibrated_at": "2026-03-27T10:00:00",
  "template_id": "1mGncfOizGbRHXNo5xqi9wfqePnlnGKbZUtlvTysYMsI",
  "overrides": {
    "palette": {
      "primary": "#8B0000",
      "background": "#FFFFFF",
      "text": "#1A1A1A"
    },
    "zones": {
      "title_full": { "top": 360000, "left": 457200, "width": 8229600, "height": 1143000 },
      "body_left_middle": { "top": 1500000, "left": 457200, "width": 4114800, "height": 4000000 },
      "right_half": { "top": 1200000, "left": 4800000, "width": 4000000, "height": 4000000 },
      "code_full_bottom": { "top": 1500000, "left": 457200, "width": 8229600, "height": 3600000 },
      "table_main": { "top": 1500000, "left": 457200, "width": 8229600, "height": 4000000 }
    },
    "typography": {
      "title": { "size": 30, "font": "Roboto", "bold": true },
      "subtitle": { "size": 22, "font": "Roboto", "bold": false },
      "body": { "size": 16, "font": "Roboto", "bold": false },
      "code": { "size": 14, "font": "Roboto Mono", "bold": false }
    },
    "table_render": {
      "col_width_strategy": "auto",
      "max_font_size": 13,
      "min_font_size": 9,
      "header_bg": "#8B0000",
      "header_fg": "#FFFFFF",
      "row_alt_bg": "#F5F5F5"
    }
  },
  "approved_slides": ["portada", "concepto-abstracto", "codigo", "tabla", "timeline"]
}
```

---

## 4. Fix: Separación Tablas vs Imágenes en el Pipeline

### 4.1 Problema actual en `slides_pipeline.py`

```python
# ACTUAL (v3) — INCORRECTO
# En la fase de assets, el pipeline llama a Gemini para todo:
for slide in plan["slides"]:
    if slide["image"]["layer"] != "none":
        generate_with_gemini(slide["image"]["prompt"])  # ✅ correcto
    for table in slide["table_assets"]:
        generate_with_gemini(table_to_prompt(table))   # ❌ INCORRECTO
```

### 4.2 Solución en v4

```python
# v4 — CORRECTO
for slide in plan["slides"]:
    # Imágenes → Gemini (solo conceptuales)
    if slide["image"]["layer"] != "none":
        _generate_image_gemini(slide["image"]["prompt"], output_path)

    # Tablas → matplotlib local (estructurado, no conceptual)
    for table_asset in slide["table_assets"]:
        _render_table_matplotlib(
            table_asset["table_markdown"],
            output_path,
            config=calibration_config["overrides"]["table_render"]
        )
```

**Función `_render_table_matplotlib`:**
- Parsea el Markdown pipe-table con `pandas`
- Renderiza con `matplotlib` usando los overrides de `calibracion-config.json`
- Aplica auto-scaling de fuente si el texto se desborda (entre `min_font_size` y `max_font_size`)
- Exporta PNG con fondo transparente o blanco según `layout.image` zone

---

## 5. Fix: Layout de `timeline` en Schema Registry

### 5.1 Cambio en `schema-registry.json`

```json
// ACTUAL (v3)
"timeline": {
  "layout": {
    "title": "full-title",
    "body": "full-center",
    "image": "none",
    "code": "none",
    "table": "none"       ← BUG: la tabla existe pero no se coloca
  },
  "image_layer": "none"
}

// v4 — CORREGIDO
"timeline": {
  "layout": {
    "title": "full-title",
    "body": "subtitle-only",   ← solo el texto introductorio pequeño
    "image": "none",
    "code": "none",
    "table": "table-main"      ← la tabla ES el contenido central
  },
  "image_layer": "none"
}
```

### 5.2 Consecuencia en el pipeline

Cuando `layout.table = "table-main"`, el pipeline posiciona la imagen PNG de la tabla en la zona `table_main` del calibration config, en lugar de ignorarla.

---

## 6. Flujo Completo v4

```
┌──────────────────────────────────────────────────────────────────┐
│  FASE 0 (nueva) — CALIBRACIÓN                                   │
│  calibrate_pipeline.py                                           │
│                                                                  │
│  Solo se ejecuta:                                                │
│  - Primera vez que se usa el pipeline                            │
│  - Cuando cambia el template_id en slides-config.yaml            │
│  - Cuando el docente ejecuta /edu-calibrate-slides               │
│                                                                  │
│  OUTPUT: _edu/calibracion-config.json                            │
└──────────────────┬───────────────────────────────────────────────┘
                   │ (si no existe calibracion-config.json → STOP)
                   ▼
┌──────────────────────────────────────────────────────────────────┐
│  FASE 1 — GENERACIÓN DEL PLAN (sin cambios vs v3)               │
│  Agente slides-publisher lee schema-registry.json                │
│  Genera plan-filminas-{tema}.json                                │
└──────────────────┬───────────────────────────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────────────────────┐
│  FASE 2 — VALIDACIÓN (sin cambios vs v3)                        │
│  validate_plan.py                                                │
└──────────────────┬───────────────────────────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────────────────────┐
│  FASE 3 — ASSETS (MODIFICADO en v4)                             │
│  slides_pipeline.py --assets-only                                │
│                                                                  │
│  Para cada slide:                                                │
│  ├─ image.layer != "none" → Gemini Imagen API                   │
│  └─ table_assets (si hay) → matplotlib local (SIN Gemini)       │
│                                                                  │
│  Lee calibracion-config.json para parámetros de render          │
└──────────────────┬───────────────────────────────────────────────┘
                   ▼
┌──────────────────────────────────────────────────────────────────┐
│  FASE 4 — PUBLICACIÓN (MODIFICADO en v4)                        │
│  slides_pipeline.py --publish-only                               │
│                                                                  │
│  Lee calibracion-config.json para posicionamiento exacto        │
│  de zonas (en lugar de constantes hardcodeadas del script)      │
│                                                                  │
│  Aplica fix de timeline: coloca tabla en zone table_main        │
└──────────────────────────────────────────────────────────────────┘
```

---

## 7. Cambios de Contrato de Responsabilidades

| Componente | v3 | v4 |
|---|---|---|
| `calibrate_pipeline.py` | No existía | **NUEVO** — calibración interactiva |
| `_edu/calibracion-config.json` | No existía | **NUEVO** — overrides del docente |
| `slides_pipeline.py` | Tablas vía Gemini | **Tablas vía matplotlib, imágenes vía Gemini** |
| `schema-registry.json` | `timeline.layout.table = "none"` | **`timeline.layout.table = "table-main"`** |
| `calibracion/` | No existía | **NUEVO** — carpeta gitignored de pruebas |

---

## 8. `.gitignore` — Cambios requeridos

```gitignore
# Calibración (slides de prueba — no commitear)
calibracion/
_edu/calibracion-config.json

# Token OAuth (ya debería estar)
_edu/token_slides.json
token_slides.json
```

---

## 9. Criterios de Aceptación

| # | Criterio | Cómo verificar |
|---|---|---|
| AC-01 | Las tablas no llaman a Gemini API | Log del pipeline no muestra "Generando imagen" para `table_assets` |
| AC-02 | Las tablas `timeline` aparecen en la slide | F-06 y F-07 muestran la tabla al abrir la presentación |
| AC-03 | La calibración genera slides en `calibracion/` | Carpeta existe y contiene PNGs tras ejecutar `calibrate_pipeline.py` |
| AC-04 | `calibracion-config.json` persiste las respuestas | El JSON se actualiza después de cada ajuste del docente |
| AC-05 | El pipeline lee `calibracion-config.json` | Si se cambia un valor en el JSON, el siguiente render lo refleja |
| AC-06 | La calibración termina cuando el docente dice "listo" | El agente acepta cualquier variante de "listo / corta / terminar / cerrar" |
| AC-07 | `calibracion/` está en `.gitignore` | `git status` no muestra los archivos de calibración |

---

## 10. Decisiones Arquitectónicas — Confirmadas por Matiasgel (27-03-2026)

| # | Decisión | Resolución |
|---|---|---|
| **D1** | Renderizado de calibración | **`python-pptx` + PNG local**, descargando el template de Google Slides al mismo tamaño (1280×720px) para máxima fidelidad sin OAuth durante calibración |
| **D2** | Trigger de calibración | **Ambos**: el pipeline detecta automáticamente si falta `calibracion-config.json` y corre calibración; también disponible como comando explícito `/edu-calibrate-slides` |
| **D3** | Tabla desbordada | **Partir en 2 slides**: mismo título + sufijo `(1/2)` / `(2/2)`, tabla dividida por filas a la mitad. No se reduce fuente por debajo del mínimo legible. |
| **D4** | Zona `timeline` | **Reservar espacio izquierdo**: bullets introductorios a la izquierda (`left-top-split`), tabla en panel derecho (`right-half`). Mismo patrón que `tabla-mixta`. |

### Consecuencias de D4 en el schema registry

El tipo `timeline` cambia de layout:

```json
// v4 — FINAL (tras D4)
"timeline": {
  "layout": {
    "title": "full-title",
    "body": "left-top-split",    ← bullets introductorios a la izquierda
    "image": "none",
    "code": "none",
    "table": "right-half"        ← tabla en panel derecho
  },
  "image_layer": "none"
}
```

### Consecuencias de D3: tabla split automático

El agente, al generar el plan, detecta tablas con más de `N` filas (umbral configurable en `calibracion-config.json`, default: 8 filas).  
Si supera el umbral → genera **dos slides consecutivas** con el mismo `type` y `title + " (1/2)"` / `" (2/2)"`, cada una con la mitad de las filas de la tabla.

El validador acepta IDs no secuenciales generados por split (ej: `F-06a`, `F-06b`) o puede usar IDs secuenciales normales si el agente renumera.

> **Decisión de numeración:** IDs secuenciales normales — el agente renumera todas las slides posteriores al split. Más limpio que sufijos alfanuméricos.
