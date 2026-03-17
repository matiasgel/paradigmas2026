# EDU — Academic Course Production Suite

Pipeline completo de producción docente universitaria con inteligencia pedagógica.

## Quick Start

1. Cloná o copiá este directorio como raíz de tu proyecto
2. Abrí VS Code
3. Configurá tu materia editando `_edu/config.yaml`:
   - `project_name`: nombre de la materia
   - `institution`: tu institución
   - `user_name`: tu nombre
   - `default_professor_profile`: tu perfil docente
   - `default_class_duration`: duración en minutos
4. Escribí `/edu-start-course` en Copilot Chat para comenzar

## Estructura del Proyecto

```
tu-materia/
├── .github/
│   ├── copilot-instructions.md    ← Contexto para Copilot
│   ├── agents/                    ← Agentes (@edu-agent-nombre)
│   └── prompts/                   ← Slash commands (/edu-*)
├── .vscode/
│   └── settings.json              ← Habilita prompt files
├── _edu/
│   ├── config.yaml                ← Configuración del módulo
│   ├── module-help.csv            ← Índice de comandos
│   ├── agents/                    ← Definiciones completas de agentes
│   ├── tasks/                     ← Tasks internas
│   └── workflows/                 ← Definiciones de workflows
├── _edu-memory/                   ← Memoria persistente (creada en runtime)
├── salida/
│   └── cursadas/
│       └── {course_year}/         ← Año de cursada activo (ej: 2026) — creado en runtime
│           ├── plan-minimo.md
│           ├── plan-borrador.md
│           └── temas/
│               └── NN-nombre/
│                   ├── diseno.md
│                   ├── minuta.md
│                   ├── filminas.md
│                   ├── guia-estudio.md  ← Material de estudio del alumno
│                   ├── guia-estudio.pdf ← PDF exportado para cátedra
│                   ├── tp.md
│                   └── slides/          ← Scripts y link de Google Slides
└── material/                      ← Material docente existente (opcional)
```

## Agentes Disponibles

Usá `@` en Copilot Chat para invocar agentes directamente:

| Agente | Persona | Qué Hace |
|--------|---------|----------|
| `@edu-agent-course-planner` | Elena 🎓 | Orquesta todo el cursado |
| `@edu-agent-topic-designer` | Marcos �️ | Diseña contenidos del tema |
| `@edu-agent-class-writer` | Roberto ✍️ | Escribe minutas y filminas || `@edu-agent-study-guide-writer` | Sofía 📖 | Escribe guías de estudio completas para alumnos || `@edu-agent-tp-designer` | Valeria 📝 | Diseña trabajos prácticos |
| `@edu-agent-curriculum-reviewer` | Ana 🔍 | Revisa cambios curriculares |
| `@edu-agent-academic-researcher` | Carlos 📚 | Investiga bibliografía |
| `@edu-agent-student-simulator` | Simulador 🎓 | Simula alumnos por perfil |
| `@edu-agent-classroom-designer` | Rodrigo 🎓 | Regenera outputs de TP (autograde, quiz) |
| `@edu-agent-plan-coverage-checker` | Verificador 📊 | Chequea cobertura del plan |
| `@edu-agent-writing-validator` | Validador 🔎 | Detecta errores de escritura |
| `@edu-agent-writing-fixer` | Corrector ✏️ | Corrige escritura automáticamente |
| `@edu-agent-coherence-fixer` | Coherencia 🔗 | Unifica coherencia entre docs |
| `@edu-agent-reference-validator` | Referencias 🔬 | Valida citas académicas |
| `@edu-agent-academic-guardrail` | Guardrail 🛡️ | Controla formalidad y densidad |

## Slash Commands (28)

Escribí `/edu-` en Copilot Chat para ver todos los comandos disponibles.

> **Nuevo:** `/edu-create-study-guide` genera la guía de estudio para el alumno. `/edu-export-pdf` la convierte a PDF listo para distribuir como material de cátedra.

### En cualquier momento
| Comando | Qué hace |
|---------|----------|
| `/edu-help` | Estado del cursado y próximo paso recomendado |
| `/edu-status` | Estado de producción de un tema específico |
| `/edu-check-coverage` | Cobertura del plan mínimo |
| `/edu-student-profiles` | Gestionar perfiles de alumno del simulador |
| `/edu-update-context` | Refrescar contexto de Copilot al retomar sesión |
| `/edu-edit-class-template` | Personalizar la estructura de minutas y filminas |

### Fase 1 — Configuración
| Comando | Qué hace |
|---------|----------|
| `/edu-start-course` | **Único comando de Fase 1** — configura materia, carga programa institucional y congela plan mínimo |

### Fase 2 — Planificación
| Comando | Qué hace |
|---------|----------|
| `/edu-build-course` | Armar cursado — desde material existente (PDFs, PPTX) o desde investigación académica |
| `/edu-propose-curriculum-change` | Proponer cambio curricular con justificación |

### Fase 3 — Producción de Temas
| Comando | Qué hace |
|---------|----------|
| `/edu-topic` | ⭐ **Guía inteligente** — detecta el estado del tema activo y recomienda el próximo paso |
| `/edu-design-topic` | Diseñar o ajustar el tema (antes de aprobar) |
| `/edu-approve-design` | Aprobar el diseño — habilita la creación de clase |
| `/edu-create-class` | Generar minuta.md y filminas.md |
| `/edu-create-study-guide` | **Nuevo** Generar guia-estudio.md — documento completo para estudio autónomo del alumno, integra PDFs fuente |
| `/edu-create-tp` | Generar trabajo práctico trazable a la minuta |
| `/edu-create-autograde-repo` | Regenerar output de TP (autograde-repo, quiz) |
| `/edu-quality` | Calidad unificada — valida y/o corrige escritura, coherencia, referencias y scope |
| `/edu-test-topic` | Testing pedagógico — simula experiencia de alumnos por perfil |
| `/edu-debate-topic` | Panel multi-agente para decisiones complejas de diseño |
| `/edu-compare-survey-simulator` | Calibrar simulador con encuestas reales de alumnos |
| `/edu-adaptive-replan` | Replanificar cronograma respetando plan mínimo |
| `/edu-close-topic` | Cerrar tema — commit + merge Git |
| `/edu-reopen-topic` | Reabrir tema cerrado para correcciones |

### Exportación PDF
| Comando | Cuándo usarlo |
|---------|---------------|
| `/edu-export-pdf` | Convierte guia-estudio.md a PDF con portada institucional y formato de cátedra (requiere pandoc + LaTeX) |

### Publicación en Google Slides
| Comando | Cuándo usarlo |
|---------|---------------|
| `/edu-setup-apis` | **Una vez** — configura Google OAuth + Gemini key |
| `/edu-slides-designer` | **Una vez por cursada** — define UX visual del cursado y cómo se renderiza Markdown en Slides |
| `/edu-publish-slides` | **En cada tema** — flujo completo: valida + genera + link |
| `/edu-slides-publisher` | Re-exportar sin rediseñar |

### Fase 4 — Cierre
| Comando | Qué hace |
|---------|----------|
| `/edu-close-course` | Cierre formal del año: retrospectiva y traspaso de memoria |
| `/edu-start-new-year` | Iniciar nuevo año con workspace limpio y memoria del anterior |

## Flujo típico de un tema

```
/edu-start-course          ← Solo una vez al iniciar el cursado

/edu-topic                 ← Punto de entrada recomendado para cada tema
  └→ /edu-design-topic
  └→ /edu-approve-design
  └→ /edu-create-class
  └→ /edu-create-study-guide     ← Guía de estudio completa (integra PDFs fuente)
  └→ /edu-create-tp
  └→ /edu-create-autograde-repo  ← Solo si el TP tiene autograde o quiz
  └→ /edu-quality
  └→ /edu-test-topic
  └→ /edu-adaptive-replan   ← Opcional: ajustar cronograma si hubo desvíos
  └→ /edu-close-topic
  └→ /edu-export-pdf         ← Opcional: exporta guia-estudio.md a PDF para cátedra
  └→ /edu-publish-slides    ← Opcional: genera presentación en Google Slides
```

## Perfiles Docentes

| Perfil | Palabras/slide | Conceptos/clase | Min/slide |
|--------|---------------|-----------------|-----------|
| profesor-teorico | ≤50 | ≤5 | 4-5 |
| profesor-practico | ≤30 | ≤3 | 2-3 |
| profesor-socratico | ≤35 | ≤4 | 3-4 |
| profesor-flipped | ≤35 | ≤4 | 3-4 |
| profesor-investigador | ≤45 | ≤5 | 4-5 |

## Configuración del Entorno Python

El pipeline de filminas requiere Python >= 3.10 y las dependencias del módulo.

### Setup automático (recomendado)

```bash
# Desde la raíz del módulo edu-standalone/ (o del repo):
bash scripts/setup.sh
```

Crea `.venv`, instala dependencias y genera `.env` automáticamente.

### Setup manual

```bash
# Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

# Instalar dependencias
pip install -r requirements.txt
```

---

## Publicación de Filminas (Google Slides)

### Prerrequisitos

1. **Cuenta de Google** con acceso a Google Drive y Slides
2. **Credenciales OAuth 2.0** — descargá `credentials.json` desde [Google Cloud Console](https://console.cloud.google.com/) (tipo _Desktop App_)
3. **Gemini API Key** — obtenela en [Google AI Studio](https://aistudio.google.com/)
4. **Entorno Python** configurado (ver sección anterior)

### Configurar credenciales

Via Copilot Chat (recomendado):

```
/edu-setup-apis
```

O manualmente:

```bash
# 1. Copiá credentials.json al directorio _edu/
cp ~/Descargas/credentials.json _edu/credentials.json

# 2. Editá _edu/secrets.local.yaml (NO commitear este archivo):
#    google_credentials_path: _edu/credentials.json
#    gemini_api_key: TU_API_KEY_AQUI
```

> `_edu/secrets.local.yaml` y `_edu/token_slides.json` están en `.gitignore` — nunca se suben al repo.

### Diseñar el sistema visual del cursado

```
/edu-slides-designer
```

Genera `_edu/slides-config.yaml` con la paleta, tipografías, grilla del cursado y contrato de render semántico para Markdown. Se hace **una sola vez** por cursada.

Ese contrato UX define, entre otras cosas:

- listas Markdown como bullets nativos de Google Slides;
- headings internos con jerarquía visual real;
- `**bold**`, `*italic*`, `` `inline code` `` y links convertidos a estilo de texto;
- ausencia de markup residual en la presentación final.

### Ejecutar el pipeline de filminas

```bash
# Activar el entorno virtual
source .venv/bin/activate

# Flujo completo: plan → assets (imágenes/tablas) → publicar en Slides
python scripts/slides_pipeline.py salida/cursadas/2026/temas/01-conceptos-introductorios

# Solo generar el plan YAML (sin subir nada)
python scripts/slides_pipeline.py salida/cursadas/2026/temas/01-conceptos-introductorios --plan-only

# Solo generar assets (imágenes con Gemini + tablas PNG)
python scripts/slides_pipeline.py salida/cursadas/2026/temas/01-conceptos-introductorios --assets-only

# Solo publicar en Google Slides (requiere plan + assets ya generados)
python scripts/slides_pipeline.py salida/cursadas/2026/temas/01-conceptos-introductorios --publish-only
```

La primera vez que corrás el flujo completo, se abrirá el navegador para autorizar el acceso OAuth a tu cuenta de Google.

### Flujo recomendado via Copilot Chat

```
/edu-publish-slides    ← flujo completo guiado: valida filminas + genera + link de Slides
/edu-slides-publisher  ← re-exportar sin rediseñar el sistema visual
```

---

## Publicar en Rama Production

El módulo `edu-standalone/` se despliega automáticamente a las ramas `production` y `lenguajes` cuando se hace push a `main` (via [GitHub Actions](.github/workflows/goproduction.yml)).

### Método 1: Trigger via GitHub Actions (recomendado)

```bash
python scripts/goproduction.py
```

Detecta cambios sin commitear en `edu-standalone/`, ofrece hacer commit automático y hace push a `main`. GitHub Actions toma el control desde ahí.

### Método 2: Deploy local directo

```bash
# Deploy a production y lenguajes sin GitHub Actions
python scripts/goproduction.py --local

# Solo a una rama específica
python scripts/goproduction.py --local --branches production

# Ver qué se haría sin ejecutar nada
python scripts/goproduction.py --dry-run
```

Usa `git worktree` para no ensuciar el repo local.

### Opciones disponibles

| Opción | Descripción |
|--------|-------------|
| _(sin opciones)_ | Trigger via push a `main` → GitHub Actions |
| `--local` | Deploy local directo con git worktree |
| `--branches BRANCH+` | Ramas destino para `--local` (defecto: `production lenguajes`) |
| `--dry-run` | Mostrar qué se haría sin ejecutar cambios |

### Via Copilot Chat

Escribí `/goproduction` en el chat y confirmá con `si` para activar el deploy desde GitHub Actions.

---

## Licencia

MIT
