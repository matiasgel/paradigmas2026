# EDU — Academic Course Production Suite

Pipeline completo de producción docente universitaria con inteligencia pedagógica.
Desde el programa institucional hasta el cierre de cursada, con validación automática y memoria acumulada año a año.

<!-- última actualización: 2026-03-25 · Arquitectura v3 JSON Schema-driven -->

---

## Workflow Completo del Profesor

El módulo está organizado en 4 fases. Cada fase tiene comandos concretos y produce artefactos bien definidos.

---

### ⚙️ Setup inicial (una sola vez, siempre)

Estos pasos se hacen **una única vez** cuando instalás el módulo por primera vez.

#### 1. Configurar la materia

Editá `_edu/config.yaml`:

```yaml
project_name: "Paradigmas de Programación"
institution:  "Universidad XYZ"
user_name:    "Prof. Matías"
default_professor_profile: "profesor-practico"   # ver tabla de perfiles al final
default_class_duration:    "90"                  # minutos
```

#### 2. Configurar el entorno Python

```bash
# Desde la raíz del módulo edu-standalone/:
bash scripts/setup.sh
```

Crea `.venv`, instala dependencias de `requirements.txt` y genera `.env`. Para setup manual:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS  |  .venv\Scripts\activate en Windows
pip install -r requirements.txt
```

#### 3. Configurar APIs (Google + Gemini)

Solo si vas a publicar filminas en Google Slides.

```
/edu-setup-apis
```

O manualmente: copiá `credentials.json` a `_edu/` y editá `_edu/secrets.local.yaml` con tu `gemini_api_key`. Este archivo está en `.gitignore` — nunca se sube al repo.

#### 4. Diseñar el sistema visual del cursado

Solo si vas a publicar filminas. Se hace **una sola vez por cursada**.

```
/edu-slides-designer
```

Activa a Vera 🎨, que te guía para definir paleta, tipografía, layouts por tipo de filmina y el contrato de render semántico de Markdown. Produce `_edu/slides-config.yaml`.

---

### 📚 Fase 1 — Configuración del Cursado (una vez por año)

```
/edu-start-course
```

**¿Qué hace?** Un solo comando que corre tres pasos en secuencia:

| Paso | Descripción | Artefacto generado |
|------|-------------|-------------------|
| 1 | Configurar nombre de materia, perfil del docente, LMS y duración de clase | `_edu/config.yaml` (actualiza) |
| 2 | Cargar el programa institucional (PDF) y extraer los tópicos mínimos | `salida/cursadas/{year}/plan-minimo.md` |
| 3 | Confirmar el plan mínimo como **contrato inmutable** de la cursada | `plan-minimo.md` bloqueado |

> **Importante:** Una vez confirmado, `plan-minimo.md` no puede ser modificado por ningún agente.
> Es el contrato social con la institución.

---

### 🗺️ Fase 2 — Planificación del Curso (una vez por año)

Con el plan mínimo confirmado, construís el plan de trabajo real.

```
/edu-build-course
```

**Dos modos disponibles:**
- **Desde material existente** — sube tus PDFs/PPTX a `material/` y el módulo extrae los tópicos
- **Desde investigación** — el módulo busca fuentes académicas y propone un plan

**Artefacto generado:** `salida/cursadas/{year}/plan-borrador.md` — cronograma de temas con duraciones.

**Comandos adicionales de fase 2:**

| Comando | Cuándo usarlo |
|---------|---------------|
| `/edu-check-coverage` | Verificar que el plan-borrador cubre todos los tópicos del plan mínimo |
| `/edu-propose-curriculum-change` | Proponer un cambio con evidencia académica |
| `/edu-adaptive-replan` | Reajustar el cronograma cuando hubo desvíos en clases anteriores |

---

### 📝 Fase 3 — Producción de Temas (una vez por cada tema)

Este es el ciclo principal. Para cada tema del cronograma, seguís estos pasos en orden.

**Punto de entrada recomendado:**

```
/edu-topic
```

Este comando detecta automáticamente el estado del tema activo y te dice exactamente cuál es el próximo paso. Podés seguir sus recomendaciones o elegir un paso distinto.

---

#### Paso 3.1 — Diseñar el tema

```
/edu-design-topic
```

**¿Qué hace?** Marcos 🗂️ te ayuda a definir el diseño pedagógico del tema: objetivos, subtópicos, profundidad y duración como constraint central.

**Artefactos generados:**
```
salida/cursadas/2026/temas/NN-nombre/
  topic.yaml      ← estado del tema, duración, branch Git
  diseno.md       ← diseño pedagógico aprobado
```

**Pedir ajustes:** corré `/edu-design-topic` de nuevo antes de aprobar.

---

#### Paso 3.2 — Aprobar el diseño

```
/edu-approve-design
```

Marca `diseno.md` como aprobado y habilita la creación de la clase. Sin aprobación, Roberto no puede escribir.

---

#### Paso 3.3 — Crear la clase

```
/edu-create-class
```

**¿Qué hace?** Roberto ✍️ genera la minuta y las filminas proporcionales a la duración definida en `diseno.md`.

*Si tenés PDFs de referencia*, copiálos a `material/NN-nombre/` primero y ejecutá:
```bash
python scripts/pdf-to-text.py material/NN-nombre/
```
Roberto los usa como referencia factual.

**Artefactos generados:**
```
temas/NN-nombre/
  minuta.md       ← clase magistral con estructura detallada
  filminas.md     ← slides en Markdown con directivas de tipo/imagen
```

**Formato de filminas.md:** cada slide usa `### [F-XX] Título` con directivas opcionales:
- `@tipo: codigo|tabla|diagrama|concepto-abstracto|...`
- `@imagen: background|content|none`
- `@prompt-imagen: descripción visual en lenguaje geométrico puro`

---

#### Paso 3.4 — Crear la guía de estudio

```
/edu-create-study-guide
```

**¿Qué hace?** Sofía 📖 produce un documento completo para que el alumno estudie de forma autónoma. Integra los PDFs fuente, expande los conceptos de la minuta y agrega glosario, autoevaluación y referencias.

**Artefacto generado:** `temas/NN-nombre/guia-estudio.md`

**Exportar a PDF:**
```
/edu-export-pdf
```
Convierte `guia-estudio.md` a PDF con portada institucional (requiere pandoc + LaTeX).

---

#### Paso 3.5 — Crear el TP

```
/edu-create-tp
```

**¿Qué hace?** Valeria 📝 genera el trabajo práctico trazable a la minuta. Te pregunta el tipo:

| Tipo | Output adicional |
|------|-----------------|
| `desarrollo` | `tp.md` — preguntas/ejercicios abiertos |
| `repo` | `autograde-repo/` — plantilla GitHub con Actions autograding |
| `quiz-moodle` | `tp-quiz.gift` + `tp-quiz-moodle-config.md` — banco de preguntas GIFT |
| `quiz-google` | `tp-quiz-forms.md` + `tp-quiz-forms-script.js` |
| `mixto` | Combinación de los anteriores |

**Para Moodle:** el módulo genera el banco de preguntas GIFT importable (no la actividad Quiz completa). Validalo con `/edu-validate-gift` antes de importar.

---

#### Paso 3.6 — Loops de calidad

```
/edu-quality
```

**¿Qué hace?** Corre cuatro loops automáticos en secuencia sobre todos los artefactos del tema:

```
Loop 1: Escritura     → ortografía, gramática, claridad
Loop 2: Coherencia    → alineación minuta ↔ filminas ↔ guía ↔ TP
Loop 3: Referencias   → verifica citas contra bases académicas
Loop 4: Guardrail     → formalidad, scope creep y densidad cognitiva
```

Cada loop produce un reporte en `quality-reports/` y genera un commit reversible en Git.
Podés correr `/edu-quality` varias veces hasta que todos los loops pasen.

---

#### Paso 3.7 — Testing pedagógico

```
/edu-test-topic
```

**¿Qué hace?** El simulador 🎓 crea perfiles de alumno empíricos y simula cómo experimentan el material. Produce:

```
temas/NN-nombre/
  score-pedagogico.md    ← métricas de densidad y accesibilidad
  faq-anticipado.md      ← preguntas que los alumnos van a hacer
```

---

#### Paso 3.8 — Cerrar el tema

```
/edu-close-topic
```

**¿Qué hace?** Elena 🎓 verifica que todos los loops estén resueltos, hace commit de todos los artefactos del tema y actualiza la matriz de cobertura.

```
temas/NN-nombre/topic.yaml → status: "closed"
```

Después del cierre, `active-topic.yaml` se limpia para que el próximo `/edu-topic` arranque fresco.

---

#### Paso 3.9 — Publicar filminas en Google Slides (opcional)

```
/edu-publish-slides
```

**¿Cuándo hacerlo?** Después de crear y aprobar `filminas.md`. No necesitás esperar al cierre del tema.

**¿Qué hace?** Diego 🚀 ejecuta el pipeline completo schema-driven:

```
filminas.md  →  plan JSON v3  →  validación  →  imágenes Gemini  →  Google Slides  →  URL
```

Pasos internos:
1. Lee `_edu/schemas/schema-registry.json` → tipos canónicos, mapeos layout, reglas de imagen
2. Genera `slides/plan-filminas-{tema}.json` determinista (un solo archivo JSON)
3. Valida el plan contra JSON Schema (máximo 3 reintentos automáticos)
4. Genera imágenes con Gemini API (prompts en lenguaje visual puro, sin conceptos técnicos)
5. Renderiza tablas como PNG con matplotlib
6. Sube todos los assets a Google Drive
7. Crea la presentación en Google Slides con el template y la paleta de Vera
8. Guarda la URL en `slides/slides-url.txt`

**Artefactos generados:**
```
temas/NN-nombre/slides/
  plan-filminas-NN-nombre.json    ← plan v3 validado (JSON Schema)
  assets/                         ← imágenes Gemini + tablas PNG
  slides-url.txt                  ← URL de la presentación
```

**Corrección de imágenes (sin tocar scripts):**

```bash
# 1. Editá image.prompt en el plan JSON con lenguaje visual puro
# 2. Poné image.drive_id: null para forzar regeneración
# 3. Borrá el asset local si existe

source .venv/bin/activate
python scripts/slides_pipeline.py temas/NN-nombre --assets-only
python scripts/slides_pipeline.py temas/NN-nombre --publish-only
```

**Opciones del pipeline:**

```bash
python scripts/slides_pipeline.py temas/NN-nombre               # flujo completo
python scripts/slides_pipeline.py temas/NN-nombre --assets-only  # solo imágenes + tablas
python scripts/slides_pipeline.py temas/NN-nombre --publish-only # solo publicar
```

---

### 🏁 Fase 4 — Cierre del Cursado (una vez al final del año)

```
/edu-close-course
```

Retrospectiva del año: qué funcionó, qué no, resumen de cobertura y traspaso de memoria acumulada.

```
/edu-start-new-year
```

Prepara el workspace para el año siguiente conservando toda la memoria del simulador y las calibraciones previas.

---

## Resumen visual del flujo

```
SETUP (una vez)
  └── config.yaml + python setup.sh + /edu-setup-apis + /edu-slides-designer

FASE 1 — Una vez por año
  └── /edu-start-course
        ├── configura materia
        ├── extrae plan mínimo del PDF institucional
        └── congela plan-minimo.md (inmutable)

FASE 2 — Una vez por año
  └── /edu-build-course
        └── genera plan-borrador.md con cronograma

FASE 3 — Por cada tema del cronograma
  └── /edu-topic  ← punto de entrada inteligente
        ├── /edu-design-topic       → diseno.md
        ├── /edu-approve-design     → diseno.md aprobado
        ├── /edu-create-class       → minuta.md + filminas.md
        ├── /edu-create-study-guide → guia-estudio.md
        │     └── /edu-export-pdf   → guia-estudio.pdf (opcional)
        ├── /edu-create-tp          → tp.md + output según tipo
        ├── /edu-quality            → reportes + fixes en Git
        ├── /edu-test-topic         → score-pedagogico.md + faq-anticipado.md
        ├── /edu-close-topic        → topic.yaml status: "closed"
        └── /edu-publish-slides     → plan JSON + Google Slides URL (opcional)

FASE 4 — Una vez al final del año
  └── /edu-close-course
  └── /edu-start-new-year
```

---

## Estructura del Proyecto

```
tu-materia/
├── .github/
│   ├── copilot-instructions.md     ← Contexto automático para Copilot
│   ├── agents/                     ← Agentes VS Code (@edu-agent-nombre)
│   └── prompts/                    ← Slash commands (/edu-*)
├── _edu/
│   ├── config.yaml                 ← Configuración del módulo
│   ├── secrets.local.yaml          ← Credenciales (en .gitignore)
│   ├── slides-config.yaml          ← Sistema visual del cursado (generado por Vera)
│   ├── active-topic.yaml           ← Tema activo (estado de runtime)
│   ├── schemas/                    ← JSON Schemas v3 (fuente de verdad del pipeline)
│   │   ├── schema-registry.json    ← Registro central: tipos, layouts, reglas de imagen
│   │   ├── filmina-slide.schema.json
│   │   ├── plan-filminas.schema.json
│   │   ├── design-system.schema.json
│   │   └── pipeline-runtime.schema.json
│   ├── agents/                     ← Definiciones completas de agentes
│   ├── templates/                  ← Templates de autoría (filminas-template.md, etc.)
│   ├── tasks/                      ← Tasks internas (gift-validator, etc.)
│   └── workflows/                  ← Definiciones de workflows por fase
├── _edu-memory/                    ← Memoria persistente inter-sesión (en runtime)
├── scripts/                        ← Pipeline técnico de filminas
│   ├── pipeline_common.py          ← Utilidades compartidas + Result[T] monad FP
│   ├── slides_pipeline.py          ← Validación + assets + publicación Google Slides
│   ├── validate_plan.py            ← Validación JSON Schema del plan
│   ├── parse_filminas.py           ← Genera plan DRAFT desde filminas.md
│   ├── repair_plan.py              ← Loop de reparación automática
│   ├── test_pipeline.py            ← Test de integración end-to-end
│   └── requirements.txt
├── salida/
│   └── cursadas/
│       └── {year}/
│           ├── plan-minimo.md      ← Plan institucional inmutable
│           ├── plan-borrador.md    ← Cronograma de trabajo
│           └── temas/
│               └── NN-nombre/
│                   ├── topic.yaml
│                   ├── diseno.md
│                   ├── minuta.md
│                   ├── filminas.md
│                   ├── guia-estudio.md
│                   ├── tp.md
│                   ├── quality-reports/
│                   └── slides/
│                       ├── plan-filminas-NN-nombre.json
│                       ├── assets/
│                       └── slides-url.txt
└── material/                       ← PDFs/PPTX del docente (opcional, en .gitignore)
```

---

## Agentes Disponibles

Invocar con `@edu-agent-nombre` en Copilot Chat o seleccionarlos en el dropdown de agentes.

### Capa 1 — Persona (visibles al docente)

| Agente | Persona | Qué hace |
|--------|---------|----------|
| `@edu-agent-course-planner` | Elena 🎓 | Orquesta todo el cursado |
| `@edu-agent-topic-designer` | Marcos 🗂️ | Diseña contenidos del tema |
| `@edu-agent-class-writer` | Roberto ✍️ | Escribe minutas y filminas |
| `@edu-agent-study-guide-writer` | Sofía 📖 | Escribe guías de estudio para alumnos |
| `@edu-agent-tp-designer` | Valeria 📝 | Diseña trabajos prácticos |
| `@edu-agent-curriculum-reviewer` | Ana 🔍 | Revisa cambios curriculares |
| `@edu-agent-academic-researcher` | Carlos 📚 | Investiga bibliografía |
| `@edu-agent-slides-designer` | Vera 🎨 | Define UX visual → `slides-config.yaml` |
| `@edu-agent-slides-publisher` | Diego 🚀 | Genera plan JSON v3 + publica en Google Slides |

### Capa 2 — Calidad (automáticos)

| Agente | Rol |
|--------|-----|
| `@edu-agent-writing-validator` | Detecta errores de escritura |
| `@edu-agent-writing-fixer` | Aplica correcciones con commits Git |
| `@edu-agent-coherence-fixer` | Unifica coherencia entre documentos |
| `@edu-agent-reference-validator` | Valida citas académicas |
| `@edu-agent-academic-guardrail` | Controla formalidad, scope y densidad |

### Capa 3 — Testing y Verificación

| Agente | Rol |
|--------|-----|
| `@edu-agent-student-simulator` | Simula alumnos con perfiles empíricos |
| `@edu-agent-plan-coverage-checker` | Verifica cobertura del plan mínimo |

---

## Referencia de Comandos

### Anytime

| Comando | Descripción |
|---------|-------------|
| `/edu-help` | Orientación contextual y próximo paso recomendado |
| `/edu-status` | Estado detallado del tema activo |
| `/edu-update-context` | Refrescar contexto de Copilot al retomar sesión |
| `/edu-edit-class-template` | Personalizar la estructura de minutas y filminas |

### Fase 1

| Comando | Descripción |
|---------|-------------|
| `/edu-start-course` | Configurar materia + cargar programa + congelar plan mínimo |

### Fase 2

| Comando | Descripción |
|---------|-------------|
| `/edu-build-course` | Construir plan-borrador desde material o investigación |
| `/edu-check-coverage` | Verificar cobertura del plan mínimo |
| `/edu-propose-curriculum-change` | Proponer cambio curricular con evidencia |
| `/edu-adaptive-replan` | Reajustar cronograma tras desvíos |

### Fase 3 — Ciclo de tema

| Comando | Descripción |
|---------|-------------|
| `/edu-topic` | ⭐ Punto de entrada — detecta estado y guía el próximo paso |
| `/edu-design-topic` | Diseñar o ajustar contenido del tema |
| `/edu-approve-design` | Aprobar diseño → habilita creación de clase |
| `/edu-create-class` | Generar `minuta.md` + `filminas.md` |
| `/edu-create-study-guide` | Generar guía de estudio para el alumno |
| `/edu-export-pdf` | Exportar guía de estudio a PDF |
| `/edu-create-tp` | Generar TP (desarrollo / repo / quiz / mixto) |
| `/edu-validate-gift` | Validar archivo GIFT antes de importar a Moodle |
| `/edu-create-autograde-repo` | Regenerar repo de autograding |
| `/edu-quality` | Loops de calidad: escritura → coherencia → referencias → guardrail |
| `/edu-test-topic` | Testing pedagógico con perfiles de alumno |
| `/edu-debate-topic` | Panel multi-agente para decisiones complejas |
| `/edu-close-topic` | Cerrar tema y actualizar cobertura |
| `/edu-reopen-topic` | Reabrir tema cerrado para correcciones |

### Fase 3 — Pipeline de filminas

| Comando | Descripción |
|---------|-------------|
| `/edu-setup-apis` | Configurar Google OAuth + Gemini API (una vez) |
| `/edu-slides-designer` | Definir sistema visual del cursado (una vez) |
| `/edu-publish-slides` | Pipeline completo v3: plan JSON → imágenes → Google Slides |
| `/edu-test-pipeline` | Test de integración end-to-end del pipeline |

### Fase 4

| Comando | Descripción |
|---------|-------------|
| `/edu-close-course` | Cierre formal: retrospectiva y traspaso de memoria |
| `/edu-start-new-year` | Iniciar nuevo año con workspace limpio y memoria acumulada |
| `/edu-student-profiles` | Gestionar perfiles empíricos de alumnos |
| `/edu-compare-survey-simulator` | Calibrar simulador con encuestas reales |

---

## Contrato Canónico de Filminas (v3)

El contrato vive en dos capas:

**Autoría** (quién escribe `filminas.md`):
- `_edu/templates/filminas-template.md` — plantilla con la estructura esperada
- `_edu/templates/filminas-schema.yaml` — markers, directivas y enum de tipos

**Pipeline** (validación y publicación):
- `_edu/schemas/schema-registry.json` — **fuente única de verdad**: enum de tipos, mapeos `tipo→layout`, reglas de imagen
- `_edu/schemas/plan-filminas.schema.json` — JSON Schema del plan por tema
- `_edu/schemas/filmina-slide.schema.json` — JSON Schema por slide individual
- `_edu/schemas/design-system.schema.json` — JSON Schema del sistema visual
- `_edu/schemas/pipeline-runtime.schema.json` — geometría EMU del pipeline

**Reglas clave:**
- Cada filmina: `### [F-XX] Título corto`
- Primer `#` interno: subtítulo visible en la slide
- `##` a `######`: encabezados del cuerpo
- Directiva `@tipo:` define el tipo desde el enum canónico del schema registry
- Directiva `@imagen: background|content|none` + `@prompt-imagen:` en lenguaje visual puro
- Los scripts no tienen constantes de diseño — todo viene del schema registry en runtime

---

## Perfiles Docentes

Afectan los umbrales del guardrail de calidad.

| Perfil | Palabras/slide | Conceptos/clase | Min/slide |
|--------|---------------|-----------------|-----------|
| `profesor-teorico` | ≤50 | ≤5 | 4-5 |
| `profesor-practico` | ≤30 | ≤3 | 2-3 |
| `profesor-socratico` | ≤35 | ≤4 | 3-4 |
| `profesor-flipped` | ≤35 | ≤4 | 3-4 |
| `profesor-investigador` | ≤45 | ≤5 | 4-5 |

---

## Deploy a Producción

El módulo `edu-standalone/` se despliega automáticamente a las ramas `production`, `lenguajes` y `lenguajes2026` cuando se hace push a `main` (via [GitHub Actions](.github/workflows/goproduction.yml)).

Se preservan los paths operativos de cada rama: `_edu/config.yaml`, `_edu/active-topic.yaml`, `.env`, `_edu-memory/`, `salida/`, `material/` y `docs/`.

```bash
# Trigger via GitHub Actions (recomendado):
python scripts/goproduction.py

# Deploy local directo:
python scripts/goproduction.py --local

# Solo a una rama específica:
python scripts/goproduction.py --local --branches production

# Ver qué se haría sin ejecutar:
python scripts/goproduction.py --dry-run
```

O desde Copilot Chat: escribí `/goproduction` y confirmá con `si`.

---

## Licencia

MIT

