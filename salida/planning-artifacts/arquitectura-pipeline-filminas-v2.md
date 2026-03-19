# Arquitectura — Pipeline EDU Filminas v2
## Plan de Mejora: Scripts Inmutables + Esquemas Canónicos por Filmina

**Proyecto:** Paradigmas y Lenguajes de Programación 2026  
**Arquitecto:** Winston (BMAD Architect)  
**Fecha:** 19 de marzo de 2026  
**Estado:** PROPUESTA — aprobación pendiente  
**Contexto:** Post-análisis del informe de producción del Tema 02

---

## 1. Diagnóstico — Causa Raíz de los Bugs

### El problema no son los tres bugs. El problema es la violación de SRP (Single Responsibility Principle).

El `slides_pipeline.py` actual tomaba **decisiones que no le corresponden**:

| Función en el script | Qué decisión tomaba | Bug resultante |
|---|---|---|
| `_detect_type()` | Infería el tipo de filmina desde Markdown | Bug 1: tipo `codigo` tapaba el cuerpo |
| `_image_prompt()` | Generaba prompts de imagen automáticamente | Bug 3: prompts con vocabulario técnico → texto en inglés |
| `generate_plan()` | Parsea filminas.md y asigna layouts/estrategias | Bug 2: budget de imágenes hardcodeado |
| `_image_safety_rules()` | Generaba instrucciones anti-texto para Gemini | Bug 3 contributorio |

**Conclusión:** El script tenía lógica de diseño. Eso es incorrecto. El script **solo debe ejecutar**, nunca decidir.

---

## 2. Principios de la Arquitectura v2

### P1 — Scripts inmutables
El `slides_pipeline.py` es un **motor de renderizado**. Lee un contrato de datos (el plan YAML), valida que esté completo, y ejecuta las 3 fases. **No genera prompts, no infiere tipos, no toma decisiones de diseño.**

Un script corregido = un cambio planificado con revisión, nunca un fix de emergencia.

### P2 — Esquema canónico por filmina (Filmina Schema)
Cada filmina es un **objeto JSON completo con todos sus campos explícitos**. El agente es responsable de llenarlo. El schema valida que esté completo.

### P3 — Los agentes generan, el script ejecuta
El agente EDU (slides-designer o class-writer) es el único que:
- Asigna el tipo de filmina (siempre explícito, nunca inferido)
- Especifica el prompt de imagen completo (visual puro, sin conceptos)
- Define el layout zona por zona

### P4 — Validación pre-ejecución strict
El pipeline valida el schema **antes de hacer cualquier llamada API**. Si falta un campo obligatorio → error descriptivo. Sin valores por defecto a ciegas.

### P5 — Prompts de imagen como artefactos versionables
Un prompt de imagen es parte del plan YAML, escrito por el agente con la técnica de **lenguaje visual puro** (geometría, colores, posiciones — sin nombrar conceptos). Es revisable y corregible por el docente **sin tocar el script**.

---

## 3. Arquitectura de Datos — Filmina Schema v2

### 3.1 Schema canónico por filmina (JSON Schema)

```yaml
# Filmina Schema v2 — Contrato inmutable
# Ubicación: _edu/templates/filmina-slide-schema.yaml
# Versión: slides/v2

$schema: "filmina/v2"
$id: "filmina-slide"

required:
  - id          # F-00, F-01, ...
  - type        # OBLIGATORIO — nunca inferido
  - title       # Texto del título
  - body_blocks # Puede ser []
  - layout      # Todas las zonas EXPLÍCITAS
  - image       # Siempre presente, strategy puede ser "none"

properties:
  id:
    type: string
    pattern: "^F-[0-9]{2}$"
  
  type:
    type: string
    enum:
      - portada
      - concepto-abstracto
      - concepto-mixto      # texto + código en columnas
      - codigo              # solo código
      - tabla
      - tabla-comparativa
      - diagrama
      - socratica
      - demo
      - cierre
      - timeline
    # NO HAY default. Si falta → error de validación.
  
  title:
    type: string
    minLength: 1          # No puede estar vacío
  
  subtitle:
    type: string
    default: ""
  
  body_blocks:
    type: array
    items:
      oneOf:
        - {type: "text", content: string}
        - {type: "heading", level: integer, content: string}
        - {type: "list", ordered: boolean, items: array}
  
  tables:
    type: array
    default: []
  
  code_blocks:
    type: array
    items:
      - lang: string
        content: string
    default: []
  
  layout:
    type: object
    required: [title, body, image, code, table]
    # Todas las zonas deben ser explícitas — no hay "compute from type"
    properties:
      title: {enum: [center-middle, full-title, center-top, left-top]}
      body:  {enum: [center-bottom, left-middle, center-middle, subtitle-only, table-intro, full-center, full-bottom, none]}
      image: {enum: [background, right-half, none]}
      code:  {enum: [right-half, full-bottom, none]}
      table: {enum: [table-main, none]}
  
  image:
    type: object
    required: [layer, prompt]
    properties:
      layer:
        type: string
        enum: [background, content, none]
      prompt:
        type: string
        description: >
          Cuando layer != none: OBLIGATORIO. Debe ser lenguaje visual puro.
          Regla: describir SOLO geometría (formas, colores, posiciones, tamaños).
          NUNCA nombrar conceptos técnicos (compilador, parser, semántica, etc.)
          que Gemini convertiría en etiquetas de texto.
          Siempre terminar con: "Sin texto, sin letras, sin etiquetas."
        # Validación: si layer != "none" y prompt vacío → error
      local_asset: {type: string, default: ""}
      drive_id:    {type: ["string", "null"], default: null}
  
  table_assets:
    type: array
    default: []
```

### 3.2 Tabla de tipos y layouts (en config, nunca en el script)

```yaml
# _edu/slides-config.yaml — sección slide_types (INMUTABLE)
slide_types:
  portada:
    layout: {title: center-middle, body: center-bottom, image: background, code: none, table: none}
    image_layer: background
  
  concepto-abstracto:
    layout: {title: full-title, body: left-middle, image: right-half, code: none, table: none}
    image_layer: content
  
  concepto-mixto:
    layout: {title: full-title, body: left-middle, image: none, code: right-half, table: none}
    image_layer: none
    note: "Texto + código en columnas. Añadido en v2 post-Bug 1."
  
  codigo:
    layout: {title: full-title, body: subtitle-only, image: none, code: full-bottom, table: none}
    image_layer: none
  
  tabla:
    layout: {title: full-title, body: table-intro, image: none, code: none, table: table-main}
    image_layer: none
  
  diagrama:
    layout: {title: full-title, body: left-middle, image: right-half, code: none, table: none}
    image_layer: content
  
  socratica:
    layout: {title: center-top, body: center-middle, image: background, code: none, table: none}
    image_layer: background
  
  cierre:
    layout: {title: center-middle, body: center-bottom, image: background, code: none, table: none}
    image_layer: background
  
  timeline:
    layout: {title: full-title, body: full-center, image: none, code: none, table: none}
    image_layer: none
  
  demo:
    layout: {title: full-title, body: left-middle, image: none, code: right-half, table: none}
    image_layer: none
  
  tabla-comparativa:
    layout: {title: full-title, body: table-intro, image: none, code: none, table: table-main}
    image_layer: none

# Configuración de imagen
gemini_image_strategy:
  max_per_presentation: 12      # Era 4 — era el Bug 2. Fijo a 12.
  apply_floor: false            # Ya no necesitamos floor en el script
  safety_rules: "Sin texto, sin letras, sin código, sin etiquetas ni fórmulas. Solo elementos visuales: objetos, iconos, escenas o diagramas mudos. Estilo vectorial limpio, fondo claro, académico."
```

---

## 4. Rediseño del Flow Completo

### 4.1 Flow actual (v1) — PROBLEMÁTICO

```
filminas.md
    │
    ▼
[slides_pipeline.py: generate_plan()]
    │  ⚠️ DECISIONES DE DISEÑO DENTRO DEL SCRIPT
    │  - _detect_type() infiere tipo desde Markdown
    │  - _image_prompt() genera prompts automáticos
    │  - budget hardcodeado
    │
    ▼
plan-filminas.yaml
    ▼
[slides_pipeline.py: generate_assets()]
    ▼
[slides_pipeline.py: publish_slides()]
```

### 4.2 Flow propuesto (v2) — INMUTABLE

```
filminas.md (fuente del contenido)
    │
    ▼
[AGENTE: slides-designer (Vera)]
    │  - Lee filminas.md
    │  - Para cada slide: asigna type (explícito)
    │  - Genera layout desde tabla de tipos en config
    │  - Genera image.prompt con lenguaje visual puro
    │  - Valida contra filmina-slide-schema.yaml
    │  - Escribe plan-filminas-{tema}.yaml
    │
    ▼
[VALIDACIÓN: schema validator]
    │  python scripts/validate_plan.py <tema>
    │  - Valida cada slide contra filmina-slide-schema.yaml
    │  - Verifica: type explícito, prompt cuando image != none
    │  - Falla con mensaje clara si hay campo faltante
    │  - SI PASA → continúa. SI FALLA → el agente debe corregir.
    │
    ▼
[SCRIPT: slides_pipeline.py] (INMUTABLE — solo ejecuta)
    │  --assets-only → genera imágenes y tablas
    │  --publish-only → publica en Google Slides
    │
    ▼
[VERIFICACIÓN: capture_thumbnails.py]
    │  - Descarga thumbnails via Google Slides API
    │  - El docente inspecciona visualmente
    │  - Si hay imágenes con texto → editar prompt en plan YAML
    │    y ejecutar --assets-only nuevamente (sin tocar el script)
    │
    ▼
Presentación publicada verificada
```

### 4.3 Validación por contrato cerrado con reintento automático

El flow v2 propuesto **sí debe evolucionar** a un loop cerrado de contrato. La validación previa ya existe, pero hoy el documento deja la corrección en manos del agente de forma implícita. Conviene volverlo explícito:

```
[AGENTE GENERADOR]
  │  produce plan-filminas.yaml
  ▼
[NORMALIZADOR]
  │  parsea YAML y lo reserializa en forma canónica
  │  elimina variaciones superficiales de formato
  ▼
[VALIDADOR DE CONTRATO]
  │  1. sintaxis
  │  2. estructura obligatoria
  │  3. enums cerrados
  │  4. reglas semánticas cruzadas
  ▼
¿válido?
  ├─ sí  → slides_pipeline.py
  └─ no  → generar diff/errores estructurados → volver al agente
         con máximo N reintentos
```

Regla operativa propuesta:
- `max_attempts: 3`
- Cada fallo devuelve errores determinísticos por slide y campo (`F-12.layout.code`, `F-26.content_image.prompt`, etc.)
- El agente corrige **solo** los campos reportados, no regenera todo el plan desde cero
- Si al tercer intento falla, se detiene el workflow y escala a revisión humana

Esto reduce drift, evita correcciones creativas fuera de contrato y hace trazable por qué falló cada intento.

### 4.4 EBNF vs schema estructural

**Sí, se puede usar EBNF, pero no es la mejor herramienta como validador principal de este caso.**

EBNF sirve bien para validar la **forma textual** de una entrada, por ejemplo:
- la gramática de `filminas.md`
- la sintaxis de directivas como `@tipo:`, `@imagen:` o `@prompt-imagen:`
- restricciones del orden de secciones en Markdown

Pero EBNF **no resuelve bien** lo que más importa en este pipeline:
- campos obligatorios en YAML/JSON
- enums cerrados
- validaciones cruzadas (`image != none` implica `prompt != ""`)
- coherencia `type ↔ layout ↔ assets`
- límites globales como budget de imágenes

Para el contrato canónico de salida, la combinación recomendada es:
- **JSON Schema o CUE** para estructura exacta del plan YAML/JSON
- **Validador Python** para reglas semánticas cruzadas que el schema no expresa cómodo
- **Normalizador canónico** para reserializar el YAML y quitar ambigüedad de formato
- **Loop de reparación** que reciba los errores y reintente automáticamente

Decisión arquitectónica recomendada:
- `filminas.md`: opcionalmente EBNF o parser ad hoc, porque ahí sí hay gramática textual
- `plan-filminas.yaml`: contrato principal con JSON Schema o CUE, no con EBNF
- `validate_plan.py`: segunda capa semántica y de negocio

---

## 5. Cambios Concretos al Script (lo mínimo necesario)

Para hacer el script verdaderamente inmutable, se eliminan las funciones de decisión:

### 5.1 Eliminar `generate_plan()` del pipeline principal
La función `generate_plan()` que parsea `filminas.md` **se separa a un script auxiliar** `scripts/parse_filminas.py`. Este script:
- Solo parsea Markdown y produce un plan DRAFT
- El plan DRAFT NO tiene tipos asignados (marcados como `type: pending`)
- El agente revisa el DRAFT y completa todos los tipos y prompts

```
filminas.md → parse_filminas.py → plan-draft.yaml (sin tipos)
                                        │
                                        ▼
                                [agente completa tipos + prompts]
                                        │
                                        ▼
                               plan-filminas.yaml (completo)
                                        │
                                        ▼
                          [validate_plan.py] → slides_pipeline.py
```

### 5.2 Eliminar `_detect_type()` del pipeline
El pipeline ya no infiere tipos. Si un slide llega sin `type` explícito → `ValidationError`.

### 5.3 Eliminar `_image_prompt()` del pipeline
El pipeline ya no genera prompts. Si `image.layer != "none"` y `image.prompt == ""` → `ValidationError`.

### 5.4 Eliminar `generate_plan()` del pipeline
El flag `--regen-plan` se mantiene en `parse_filminas.py` pero queda fuera de `slides_pipeline.py`.

### 5.5 Mantener en el script solo:
- Validación de schema (`validate_plan()`)
- Generación de assets: llamadas a Gemini Imagen, tablas con matplotlib, subida a Drive
- Publicación en Google Slides: construcción de requests y batchUpdate
- CLI: `--plan-only`, `--assets-only`, `--publish-only`

---

## 6. Template de Prompt Visual Puro

Regla derivada del Bug 3. **El agente debe seguir este template al escribir prompts de imagen:**

### Template

```
[Elemento principal]: [forma geométrica] [color] [posición].
[Elemento secundario]: [forma geométrica] [color] [posición relativa].
[Relación]: [descripción posicional/conector].
[Estilo]: flat design, bordo y gris oscuro, fondo blanco.
Sin texto, sin letras, sin etiquetas, sin código, sin números.
Alta resolución.
```

### Ejemplos correctos (del Tema 02)

| Filmina | Prompt CORRECTO |
|---|---|
| F-12 (ambigüedad→gramática→validación) | "Three flat icons in a horizontal sequence on white background separated by thin arrows. First: irregular blob shape. Second: symmetrical triangular branching tree. Third: bold checkmark symbol. Flat design, bordo and dark gray. Nothing written." |
| F-26 (nombres y objetos denotables) | "Small empty rectangle on the bottom left with a bold arrow pointing to a larger square on the right. Inside the large square: six distinct geometric shapes — cylinder, diamond, triangle, hexagon, circle, star — arranged loosely. Bordo and gray palette. White background. No text whatsoever." |
| F-37 (mapa conceptual) | "One large bordo filled circle in the center. Six thin straight lines radiate outward. At the end of each line, one small flat icon: magnifying glass, gear, downward branching tree, two-by-two grid, cube, horizontal tube. White background. No labels, no words, nothing written anywhere." |

### Ejemplos INCORRECTOS (causaron Bug 3)

| Filmina | Prompt INCORRECTO | Consecuencia |
|---|---|---|
| F-12 | "infografía ambigüedad → gramática formal → validación automática" | Gemini agregó etiquetas: "AMBINICITY", "FORMACL GRAMMAR", "AUTOMATIC VALIDATION" |
| F-37 | "mapa conceptual: lexer, parser, gramática, diagramas, semántica, pipeline" | Gemini etiquetó todos: "Parser", "Lexicon", "Grammaris", "Disgandor" |

**Regla de oro:** Si el prompt nombra un concepto técnico → Gemini lo etiquetará. Describir solo la forma, no lo que representa.

---

## 7. Nuevo Archivo: `scripts/validate_plan.py`

Script de validación independiente que corre ANTES del pipeline:

```python
# scripts/validate_plan.py
# Uso: python scripts/validate_plan.py salida/cursadas/2026/temas/NN-nombre

# Valida:
# 1. Cada slide tiene type explícito en el enum permitido
# 2. Cada slide con image.layer != "none" tiene image.prompt no vacío
# 3. El layout de cada slide es coherente con el tipo (según slide_types en config)
# 4. No hay slides con type: pending o type: null
# 5. El número de imágenes planificadas no supera max_per_presentation

# Exit code 0 = válido
# Exit code 1 = errores (lista detallada)
```

### 7.1 Siguiente paso recomendado: `scripts/repair_plan.py`

Para cerrar el contrato de salida y evitar correcciones manuales repetitivas, agregar un orquestador simple:

```python
# scripts/repair_plan.py
# Uso: python scripts/repair_plan.py <tema> --max-attempts 3

# Loop:
# 1. Invoca al agente generador para producir o corregir plan-filminas.yaml
# 2. Normaliza el YAML a forma canónica
# 3. Ejecuta validate_plan.py
# 4. Si falla: devuelve al agente SOLO la lista estructurada de errores
# 5. Si pasa: retorna exit code 0 y habilita slides_pipeline.py
# 6. Si supera max-attempts: exit code 2 y requiere revisión humana
```

Esto convierte la validación en una **puerta automática de calidad**, no solo en un checklist previo.

---

## 8. Plan de Implementación — Sprints

### Sprint 1 (inmediato — sin romper nada)
- [ ] Actualizar `_edu/slides-config.yaml` con sección `slide_types` completa (incluye `concepto-mixto`)
- [ ] Corregir `max_per_presentation: 12` en `slides-config.yaml` (eliminar necesidad de floor en script)
- [ ] Actualizar `_edu/templates/filminas-schema.yaml` con campo `image.prompt` obligatorio cuando `image != none`
- [ ] Crear `scripts/validate_plan.py` como herramienta de pre-verificación
- [ ] Crear `scripts/capture_thumbnails.py` (ya creado en esta sesión)
- [ ] Documentar template de prompt visual puro en `_edu/templates/prompt-imagen-guide.md`

### Sprint 2 (refactor del script)
- [ ] Extraer `generate_plan()` a `scripts/parse_filminas.py` (genera draft con `type: pending`)
- [ ] Eliminar `_detect_type()` del pipeline principal
- [ ] Eliminar `_image_prompt()` del pipeline principal
- [ ] El pipeline solo lee el plan — la validación es el contrato de entrada
- [ ] Actualizar tests en `scripts/test_pipeline.py` y `scripts/test_slides_contract.py`

### Sprint 3 (agentes)
- [ ] Actualizar prompt del agente `slides-designer.md` con instrucciones para asignar tipos explícitos
- [ ] Agregar regla de prompt visual puro en el agente
- [ ] Agregar step de validación (`python scripts/validate_plan.py`) en el workflow `topic-cycle`
- [ ] Agregar loop automático `repair_plan.py` con máximo 3 reintentos y errores estructurados por campo
- [ ] Crear template de filmina JSON/YAML editable por el docente en `_edu/templates/filmina-slide.yaml`

---

## 9. Estado Actual Post-Sesión (19 de marzo 2026)

### ✅ Completado en esta sesión
- Pipeline corregido (`concepto-mixto`, `--regen-plan`, `_image_safety_rules` mejorada, budget=12) desplegado en:
  - `scripts/slides_pipeline.py` (raíz)
  - `salida/edu-standalone/scripts/slides_pipeline.py`
- Tema 02 publicado con el pipeline corregido: 40 slides, 742 requests, 15 lotes
- **URL nueva:** https://docs.google.com/presentation/d/1bMGI0BttGqaYJBmvXWzr9R8VPqkq8eYuuE14MIVqozk/edit
- **40/40 thumbnails capturados** en `salida/cursadas/2026/temas/02-sintaxis-semantica/slides/thumbnails/`
- Script `scripts/capture_thumbnails.py` creado con retry y timeout robusto.

### ⏳ Pendiente de implementación
- Sprint 1-3 del plan anterior
- Validación visual de los 40 thumbnails capturados
- Actualización del `slides-config.yaml` con `slide_types` completo

---

## 10. Coherencia del Flow Completo

### Puntos de entrada válidos

| Comando | Cuándo usar | Prerrequisito |
|---|---|---|
| `python scripts/parse_filminas.py <tema>` | Generar plan DRAFT desde filminas.md | filminas.md existe |
| `python scripts/validate_plan.py <tema>` | Validar plan antes de ejecutar | plan YAML lleno por agente |
| `python scripts/slides_pipeline.py <tema> --assets-only` | Generar imágenes | plan válido |
| `python scripts/slides_pipeline.py <tema> --publish-only` | Publicar presentación | assets con drive_id |
| `python scripts/capture_thumbnails.py <id> <carpeta>` | Verificar visualmente | presentación publicada |

### El ciclo de corrección de imágenes sin tocar el script

```
1. Abrir plan-filminas.yaml
2. Localizar la slide con imagen problemática
3. Editar image.prompt con lenguaje visual puro
4. Eliminar image.drive_id (poner null)
5. Eliminar slides/assets/F-XX-content.png si existe
6. python scripts/slides_pipeline.py <tema> --assets-only
7. python scripts/slides_pipeline.py <tema> --publish-only
8. python scripts/capture_thumbnails.py <nuevo_id> <carpeta>
9. Verificar — repetir si es necesario
```

---

*Documento generado el 19 de marzo de 2026 — Winston (BMAD Architect)*  
*Paradigmas y Lenguajes de Programación 2026 — UNTDF Instituto IDEI*
