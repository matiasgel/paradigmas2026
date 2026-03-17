# Informe de Producción — Tema 01: Conceptos Introductorios
**Paradigmas y Lenguajes de Programación 2026**  
Universidad Nacional de Tierra del Fuego — IDEI  
Fecha de generación: 16 de marzo de 2026  

---

## 1. Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| Tema | 01 — Conceptos Introductorios + Intro a TypeScript |
| Filminas generadas | 29 |
| Imágenes IA (Imagen 4.0) | 6 |
| Tablas renderizadas (matplotlib) | 8 |
| Bloques de código | 15 |
| Presentación Google Slides | [Ver presentación](https://docs.google.com/presentation/d/1_Iv25orXNS4f_L57xF6hD6b4o6SXpb1YG2NJg_tRxzQ/edit) |
| Template ID | `1mGncfOizGbRHXNo5xqi9wfqePnlnGKbZUtlvTysYMsI` |

---

## 2. Scripts utilizados y modificados

### `slides_pipeline.py` (copiado en este informe)
Script principal del pipeline EDU. Ubicación original: `scripts/slides_pipeline.py`  
**1139 líneas.** Fases:
1. **plan** — Lee `filminas.md` → genera `plan-filminas-{tema}.yaml`
2. **assets** — Genera imágenes con Imagen 4.0, renderiza tablas PNG con matplotlib, sube a Google Drive
3. **publish** — Lee el plan + assets y crea/puebla la presentación vía Google Slides API (`batchUpdate`)

**Cambios aplicados durante esta sesión:**

| Cambio | Descripción |
|--------|-------------|
| `_color()` / `_rgb_color()` | Split de función: `_color()` usa `opaqueColor` para texto, `_rgb_color()` usa `rgbColor` bare para fondos |
| `_normalize_alignment()` | Nueva función: convierte `"LEFT"→"START"`, `"RIGHT"→"END"` para la API de Google Slides |
| `updateParagraphStyle` | Ahora usa `_normalize_alignment(align)` en todos los nodos |
| `updatePageProperties` | Usa `_rgb_color(bg_color)` para fondos de página |
| Table/code backgrounds | Usan `_rgb_color()` para fill de celdas y rectángulos de código |
| Modelo de imagen | Migrado de `gemini-2.0-flash-exp-image-generation` (404) → `imagen-4.0-generate-001` |
| Endpoint imagen | Cambio de `:generateContent` (Gemini) → `:predict` (Imagen 4.0) |
| Payload imagen | `contents[]/parts[]` → `instances[]/prompt` + `parameters/sampleCount` |
| Response parsing | `candidates[]/content/parts/inlineData` → `predictions[]/bytesBase64Encoded` |

### Archivos de configuración

| Archivo | Descripción | Cambio |
|---------|-------------|--------|
| `_edu/slides-config.yaml` | Sistema de diseño (paleta, tipografía, estrategia de imagen) | `gemini_image_strategy` corregido de string a dict |
| `_edu/active-topic.yaml` | Tema activo actual | Path corregido a `salida/cursadas/2026/temas/03-intro-funcional-ts` |
| `_edu/secrets.local.yaml` | Credenciales (gitignored) | Agregado `gemini_api_key` |
| `.gitignore` | Ignorados | Agregado `_edu/token_slides.json` |

---

## 3. Artefactos de entrada

| Archivo | Descripción | Líneas |
|---------|-------------|--------|
| `filminas.md` (copiado aquí) | Fuente de contenido de las 29 filminas | 620 |
| `_edu/slides-config.yaml` (copiado aquí) | Sistema de diseño institucional UNTdF | ~80 |
| `_edu/credentials.json` | OAuth2 Google (gitignored) | — |
| `_edu/token_slides.json` | Token OAuth2 cacheado (gitignored) | — |

---

## 4. Artefactos generados

### Plan de filminas
- `plan-filminas-01-conceptos-introductorios.yaml` (copiado aquí) — 29 slides con layouts, prompts de imagen, tablas, bloques de código

### Assets de imagen (`assets-generados/`)

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `F-00-bg.png` | Imagen IA (Imagen 4.0) | Fondo portada — paradigmas de programación |
| `F-01-bg.png` | Imagen IA (Imagen 4.0) | Fondo socrática — pregunta incómoda |
| `F-02-content.png` | Imagen IA (Imagen 4.0) | Contenido — costo de elegir mal |
| `F-05-bg.png` | Imagen IA (Imagen 4.0) | Fondo socrática — pregunta abierta |
| `F-06-bg.png` | Imagen IA (Imagen 4.0) | Fondo socrática — ¿qué es un paradigma? |
| `F-07-content.png` | Imagen IA (Imagen 4.0) | Contenido — factores que formaron paradigmas |
| `F-03-table-1.png` | Tabla matplotlib | Perspectiva histórica |
| `F-04-table-1.png` | Tabla matplotlib | Criterios de evaluación de lenguajes |
| `F-09-table-1.png` | Tabla matplotlib | Los 4 paradigmas fundamentales |
| `F-10-table-1.png` | Tabla matplotlib | Dominios de aplicación |
| `F-12-table-1.png` | Tabla matplotlib | Von Neumann → código imperativo |
| `F-15-table-1.png` | Tabla matplotlib | ¿Por qué TypeScript en 2026? |
| `F-16-table-1.png` | Tabla matplotlib | TypeScript como máquina intermedia |
| `F-28-table-1.png` | Tabla matplotlib | Adelanto Clase 2 |

### Presentación final
- **URL**: https://docs.google.com/presentation/d/1_Iv25orXNS4f_L57xF6hD6b4o6SXpb1YG2NJg_tRxzQ/edit
- 29 slides, 8 lotes de `batchUpdate` (50 requests/lote = 384 requests total)

---

## 5. Inventario de filminas

| # | ID | Tipo | Título | Assets |
|---|----|----|--------|--------|
| 01 | F-00 | portada | Portada | — |
| 02 | F-01 | socratica | ¿Para qué estudiar lenguajes de programación? | F-01-bg.png (IA) |
| 03 | F-02 | concepto-abstracto | El costo de elegir mal | F-02-content.png (IA) |
| 04 | F-03 | tabla | Perspectiva histórica | F-03-table-1.png |
| 05 | F-04 | tabla | Criterios de evaluación de lenguajes | F-04-table-1.png |
| 06 | F-05 | socratica | Pregunta abierta | F-05-bg.png (IA) |
| 07 | F-06 | socratica | ¿Qué es un paradigma? | F-06-bg.png (IA) |
| 08 | F-07 | concepto-abstracto | Los factores que formaron los paradigmas | F-07-content.png (IA) |
| 09 | F-08 | codigo | El cuello de botella de Von Neumann | — |
| 10 | F-09 | tabla | Los 4 paradigmas fundamentales | F-09-table-1.png |
| 11 | F-10 | tabla | Dominios de aplicación | F-10-table-1.png |
| 12 | F-11 | codigo | La escalera de abstracciones | — |
| 13 | F-12 | tabla | Von Neumann → código imperativo | F-12-table-1.png |
| 14 | F-13 | codigo | Mismo algoritmo — 3 niveles | — |
| 15 | F-14 | codigo | Máquina abstracta, interpretación y compilación | — |
| 16 | F-15 | tabla | ¿Por qué TypeScript en 2026? | F-15-table-1.png |
| 17 | F-16 | codigo | TypeScript como máquina intermedia | F-16-table-1.png |
| 18 | F-17 | codigo | El mismo problema: imperativo en TypeScript | — |
| 19 | F-18 | codigo | El mismo problema: funcional en TypeScript | — |
| 20 | F-19 | codigo | Sistema de tipos básico | — |
| 21 | F-20 | codigo | TypeScript como "acelerador de paradigma" | — |
| 22 | F-21 | codigo | El cambio de rol del programador | — |
| 23 | F-22 | codigo | La jerarquía de proficiencia en IA | — |
| 24 | F-23 | codigo | Demo en vivo — La IA elige paradigmas | — |
| 25 | F-24 | codigo | Demo en vivo — Restricción de paradigma | — |
| 26 | F-25 | codigo | Demo en vivo — Máquinas abstractas | — |
| 27 | F-26 | codigo | El loop "trust but verify" | — |
| 28 | F-27 | codigo | Mapa de la materia — los 15 temas | — |
| 29 | F-28 | codigo | Adelanto — Clase 2: Sintaxis y Semántica | F-28-table-1.png |

---

## 6. Diseño visual (slides-config.yaml)

**Paleta institucional UNTdF:**
| Token | Valor | Uso |
|-------|-------|-----|
| primary | `#A9191B` | Títulos, acentos, bordes |
| secondary | `#1773AE` | Links institucionales |
| background | `#FFFFFF` | Fondo de diapositivas |
| text | `#3C3C3B` | Texto principal |
| surface | `#F4F4F4` | Fondo de bloques de código |

**Tipografía:**
- Títulos: Roboto Bold 46pt
- Headings: Roboto Medium 32pt
- Body: Roboto 21pt
- Código: Consolas 18pt

---

## 7. Stack tecnológico

| Componente | Tecnología |
|-----------|------------|
| Generación de plan | Python + regex + YAML |
| Imágenes IA | Google Imagen 4.0 (`imagen-4.0-generate-001`) via REST API |
| Tablas | matplotlib + pandas (render PNG) |
| Publicación | Google Slides API v1 (`batchUpdate`) |
| Almacenamiento assets | Google Drive API v3 |
| Autenticación | OAuth2 via `google-auth-oauthlib` |

---

## 8. Capturas de filminas

Las capturas se encuentran en `filminas/filmina01.png` a `filminas/filmina29.png`.  
Obtenidas via `presentations.pages.getThumbnail` (tamaño LARGE) de la Google Slides API.

| Filmina | Archivo | Tipo |
|---------|---------|------|
| 01 – Portada | [filminas/filmina01.png](filminas/filmina01.png) | portada |
| 02 – ¿Para qué estudiar lenguajes de programación? | [filminas/filmina02.png](filminas/filmina02.png) | socratica |
| 03 – El costo de elegir mal | [filminas/filmina03.png](filminas/filmina03.png) | concepto-abstracto |
| 04 – Perspectiva histórica | [filminas/filmina04.png](filminas/filmina04.png) | tabla |
| 05 – Criterios de evaluación | [filminas/filmina05.png](filminas/filmina05.png) | tabla |
| 06 – Pregunta abierta | [filminas/filmina06.png](filminas/filmina06.png) | socratica |
| 07 – ¿Qué es un paradigma? | [filminas/filmina07.png](filminas/filmina07.png) | socratica |
| 08 – Factores que formaron paradigmas | [filminas/filmina08.png](filminas/filmina08.png) | concepto-abstracto |
| 09 – Von Neumann | [filminas/filmina09.png](filminas/filmina09.png) | codigo |
| 10 – Los 4 paradigmas | [filminas/filmina10.png](filminas/filmina10.png) | tabla |
| 11 – Dominios de aplicación | [filminas/filmina11.png](filminas/filmina11.png) | tabla |
| 12 – Escalera de abstracciones | [filminas/filmina12.png](filminas/filmina12.png) | codigo |
| 13 – Von Neumann → imperativo | [filminas/filmina13.png](filminas/filmina13.png) | tabla |
| 14 – Mismo algoritmo, 3 niveles | [filminas/filmina14.png](filminas/filmina14.png) | codigo |
| 15 – Máquina abstracta | [filminas/filmina15.png](filminas/filmina15.png) | codigo |
| 16 – ¿Por qué TypeScript en 2026? | [filminas/filmina16.png](filminas/filmina16.png) | tabla |
| 17 – TypeScript como máquina intermedia | [filminas/filmina17.png](filminas/filmina17.png) | codigo |
| 18 – Imperativo en TypeScript | [filminas/filmina18.png](filminas/filmina18.png) | codigo |
| 19 – Funcional en TypeScript | [filminas/filmina19.png](filminas/filmina19.png) | codigo |
| 20 – Sistema de tipos básico | [filminas/filmina20.png](filminas/filmina20.png) | codigo |
| 21 – TypeScript acelerador de paradigma | [filminas/filmina21.png](filminas/filmina21.png) | codigo |
| 22 – Cambio de rol del programador | [filminas/filmina22.png](filminas/filmina22.png) | codigo |
| 23 – Jerarquía de proficiencia en IA | [filminas/filmina23.png](filminas/filmina23.png) | codigo |
| 24 – Demo: IA elige paradigmas | [filminas/filmina24.png](filminas/filmina24.png) | codigo |
| 25 – Demo: Restricción de paradigma | [filminas/filmina25.png](filminas/filmina25.png) | codigo |
| 26 – Demo: Máquinas abstractas | [filminas/filmina26.png](filminas/filmina26.png) | codigo |
| 27 – El loop "trust but verify" | [filminas/filmina27.png](filminas/filmina27.png) | codigo |
| 28 – Mapa de la materia | [filminas/filmina28.png](filminas/filmina28.png) | codigo |
| 29 – Adelanto Clase 2 | [filminas/filmina29.png](filminas/filmina29.png) | codigo |

---

## 9. Estructura del informe

```
informe/
├── informe.md                          ← este archivo
├── slides_pipeline.py                  ← script principal (copia)
├── slides-config.yaml                  ← diseño visual (copia)
├── filminas.md                         ← fuente de contenido (copia)
├── plan-filminas-01-conceptos-*.yaml   ← plan de filminas (copia)
├── assets-generados/                   ← imágenes generadas (14 archivos)
│   ├── F-00-bg.png ... F-28-table-1.png
└── filminas/                           ← capturas de cada slide
    ├── filmina01.png
    ├── filmina02.png
    └── ... filmina29.png
```

---

## 10. Observaciones para análisis

1. **Watermarks en imágenes IA**: Las imágenes generadas por Imagen 4.0 contienen el texto `#A9191B` (el código hex del color primario). Esto ocurre porque el prompt incluye el color como parte del contexto de estilo. Se recomienda refinar `_image_prompt()` para no incluir códigos hex o agregar la instrucción `"do not include color codes as text"` al prompt base.

2. **Filminas tipo `portada` sin imagen**: La filmina 01 (portada) no tiene imagen de fondo a pesar de ser tipo `portada`. Revisar la lógica de asignación de estrategia en `_plan_slide()` para que `portada` siempre reciba `strategy: background`.

3. **Filminas tipo `codigo` dominan la segunda mitad** (F-09 a F-28): 15 de 29 slides son de tipo `codigo`. La densidad de código es alta para una primera clase introductoria — considerar fragmentar en filminas más cortas o usar tipo `concepto-abstracto` para las demos.

4. **Calidad de tablas**: Las tablas generadas con matplotlib (8 archivos) tienen estilo académico neutro. Se puede mejorar aplicando la paleta institucional (`#A9191B`, `#1773AE`) al header de las tablas.

5. **Presentación URL válida**: Confirmada el 16/03/2026 — https://docs.google.com/presentation/d/1_Iv25orXNS4f_L57xF6hD6b4o6SXpb1YG2NJg_tRxzQ/edit
