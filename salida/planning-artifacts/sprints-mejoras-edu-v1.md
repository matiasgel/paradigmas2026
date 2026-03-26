# Sprints de Mejoras — EDU Module

**Fecha:** 2026-03-25  
**Regla cardinal:** CERO modificaciones destructivas. Todo es aditivo. Los tests actuales deben seguir pasando. Ningún archivo existente pierde funcionalidad.

---

## Principio de seguridad

Cada ítem sigue estas reglas:

| Regla | Descripción |
|-------|-------------|
| **Aditivo** | Solo se CREAN archivos nuevos. Los existentes se extienden con campos opcionales |
| **Opt-in** | Todo feature nuevo se activa con un flag en `config.yaml` (default: desactivado) |
| **Schema-safe** | El Schema Registry v3 es INMUTABLE. Schemas nuevos se registran como extensiones, no modifican los existentes |
| **Test-safe** | `test_pipeline.py` y `test_slides_contract.py` siguen pasando sin cambios |
| **Rollback** | Si se borra el archivo nuevo, el sistema vuelve al estado anterior sin efectos secundarios |

---

## Resumen de Sprints

| Sprint | Nombre | Items | Foco | Riesgo |
|--------|--------|-------|------|--------|
| S1 | Validadores pasivos | #2, #8 | Scripts que leen y reportan. No modifican nada | Nulo |
| S2 | Herramientas docentes | #11, #12 | Scripts + prompts nuevos para planificación | Nulo |
| S3 | GitHub Classroom | #4, #6 | Workflow nuevo + templates GitHub Actions | Nulo |
| S4 | Inteligencia cognitiva | #1, #10 | Schemas de extensión + validadores | Bajo — flag opt-in |
| S5 | Analytics y adaptativo | #5, #7 | Tablas SQLite nuevas + scripts | Bajo — aislado en analytics/ |
| S6 | Investigación | #3, #9 | Agente nuevo + MCP server | Bajo — módulos independientes |

---

## Sprint 1 — Validadores Pasivos

**Objetivo:** Agregar validaciones que leen artefactos existentes y generan reportes. No tocan nada.

### S1.1 — Accesibilidad WCAG (#2)

**Story:** Como docente, quiero validar que mis slides cumplen WCAG 2.2 AA para que alumnos con discapacidades visuales puedan consumirlas.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/validate_accessibility.py` | Script | Validador de contraste, tipografía mínima, alt_text |
| `.github/prompts/edu-check-accessibility.prompt.md` | Prompt | Slash command `/edu-check-accessibility` |

**Qué hace `validate_accessibility.py`:**
- Lee `_edu/slides-config.yaml` → extrae `palette` (colores hex)
- Calcula contraste relativo (fórmula WCAG: luminancia relativa)
- Verifica contra umbrales AA (4.5:1 texto normal, 3:1 texto grande) y AAA (7:1)
- Lee `config.yaml` → si existe `classroom_distance_meters`, calcula tamaño mínimo tipográfico recomendado
- Lee plan JSON del tema → verifica que cada filmina con `image_file` tenga `alt_text` no vacío
- Output: `{topic_folder}/accessibility-report.md` con score A/AA/F por slide

**Config nuevos (opcionales, se agregan al final de config.yaml):**
```yaml
# --- Accessibility (Sprint 1) ---
accessibility_check_enabled: false          # activar con true
delivery_mode: "presencial"                 # presencial | remoto | hybrid
classroom_distance_meters: 6               # distancia fila trasera
screen_resolution: "1080p"                  # para modo remoto
```

**Criterios de aceptación:**
- [ ] `python scripts/validate_accessibility.py --topic 01-intro --course leng-2026` genera reporte
- [ ] Sin flag `accessibility_check_enabled: true`, el script imprime "Accessibility check disabled" y sale con 0
- [ ] `test_pipeline.py` sigue pasando sin cambios
- [ ] El script no requiere dependencias nuevas (solo stdlib: `colorsys`, `json`, `re`)

---

### S1.2 — Auditoría Visual de Slides (#8)

**Story:** Como docente, quiero validar que la composición visual de mis slides respeta márgenes seguros, densidad visual y patrones de atención.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/validate_slide_composition.py` | Script | Validador de márgenes, densidad, patrón Z |
| `.github/prompts/edu-check-composition.prompt.md` | Prompt | Slash command `/edu-check-composition` |

**Qué hace `validate_slide_composition.py`:**
- Lee `_edu/schemas/pipeline-runtime.schema.json` → obtiene geometría EMU (ancho, alto, márgenes)
- Lee plan JSON del tema → por cada filmina:
  - **Margen seguro:** Verifica que `position_x`, `position_y` estén dentro del 5% del borde
  - **Densidad visual:** Calcula ratio área-ocupada / área-total. Ideal: 35-55% (Scheiter & Eitel, 2023)
  - **Elementos superpuestos:** Detecta colisiones de bounding boxes entre `title`, `body`, `image`, `code_block`
- Output: `{topic_folder}/composition-report.md` con score A/B/C/F por slide

**Criterios de aceptación:**
- [ ] `python scripts/validate_slide_composition.py --topic 01-intro --course leng-2026`
- [ ] No modifica ningún archivo — solo lectura y reporte
- [ ] `test_pipeline.py` sigue pasando

---

### Entregables Sprint 1

| Archivo | Estado |
|---------|--------|
| `scripts/validate_accessibility.py` | NUEVO |
| `scripts/validate_slide_composition.py` | NUEVO |
| `.github/prompts/edu-check-accessibility.prompt.md` | NUEVO |
| `.github/prompts/edu-check-composition.prompt.md` | NUEVO |
| `_edu/module-help.csv` | EXTEND — 2 filas nuevas al final |
| `_edu/config.yaml` | EXTEND — bloque `# --- Accessibility ---` al final |
| `WORKFLOW_PROMPT_MAP.md` | EXTEND — 2 filas nuevas |
| `README.md` | EXTEND — sección "Validadores" |

**Archivos existentes NO tocados:** agents/*, workflows/*, schemas/*, tests/*, slides_pipeline.py, validate_plan.py, parse_filminas.py, edu_memory.py

---

## Sprint 2 — Herramientas de Planificación Docente

**Objetivo:** Scripts independientes que ayudan al docente a planificar repasos y exámenes. No interactúan con el pipeline de slides.

### S2.1 — Spaced Repetition Engine (#11)

**Story:** Como docente, quiero un calendario de repasos distribuidos para insertar slides de revisión en clases futuras, combatiendo la curva del olvido.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/spaced_repetition.py` | Script | Motor de repaso distribuido con FSRS v4 |
| `.github/prompts/edu-spaced-review.prompt.md` | Prompt | `/edu-spaced-review` |

**Qué hace `spaced_repetition.py`:**
- Algoritmo: **FSRS v4** (Free Spaced Repetition Scheduler, Ye 2023-2024, MIT license)
  - Modelo DSR (Difficulty, Stability, Retrievability)
  - Implementación en Python puro (sin dependencias — solo `math`, `datetime`, `json`, `sqlite3`)
- Lee `plan-borrador.md` → extrae lista de temas con fechas de clase
- Lee scores de TPs (si existen en `memory.db`) → calibra dificultad por tema
- Calcula intervalos óptimos de repaso: día 1, día 3, día 7, día 14, día 30 (ajustables)
- Output:
  - `{course_output_folder}/repaso-calendario.md` — calendario Markdown con fechas
  - `{topic_folder}/slides-repaso.md` — 2-3 slides template de revisión tipo socrática
- Tabla nueva en `memory.db`: `spaced_reviews` (topic_id, review_date, review_number, score, next_review)

**Criterios de aceptación:**
- [ ] `python scripts/spaced_repetition.py --course leng-2026 generate` → calendario
- [ ] `python scripts/spaced_repetition.py --course leng-2026 --topic 01-intro record --score 0.7` → registra resultado
- [ ] La tabla `spaced_reviews` se crea con `IF NOT EXISTS` — no rompe `memory.db` existente
- [ ] Sin temas enseñados, muestra "No hay temas con fecha de clase registrada" y sale con 0

---

### S2.2 — Exam Blueprint Generator (#12)

**Story:** Como docente, quiero generar parciales con cobertura garantizada de temas y distribución explícita de Bloom, para que mis evaluaciones sean trazables y equilibradas.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/schemas/exam-blueprint.schema.json` | Schema | Contrato JSON Schema para blueprints de examen |
| `scripts/generate_exam_blueprint.py` | Script | Genera tabla de especificaciones automática |
| `.github/prompts/edu-create-exam.prompt.md` | Prompt | `/edu-create-exam` |

**Qué hace `generate_exam_blueprint.py`:**
- Input: lista de temas a evaluar + puntos totales + tiempo
- Lee minuta.md de cada tema → extrae conceptos y niveles de Bloom implícitos
- Distribuye puntos proporcionalmente al tiempo dedicado a cada tema
- Aplica distribución de Bloom configurable (default: 20% recordar, 30% comprender, 30% aplicar, 15% analizar, 5% evaluar)
- Output:
  - `{course_output_folder}/evaluaciones/blueprint-parcial-N.json` (schema-validado)
  - `{course_output_folder}/evaluaciones/blueprint-parcial-N.md` (tabla legible)

**Schema `exam-blueprint.schema.json`:**
- Se registra como extensión independiente — NO se agrega al Schema Registry (el registry es para el pipeline de filminas exclusivamente)
- Path: `_edu/schemas/exam-blueprint.schema.json`

**Criterios de aceptación:**
- [ ] `python scripts/generate_exam_blueprint.py --course leng-2026 --topics "01-intro,02-tipos,03-memoria" --points 100 --time 120`
- [ ] Output validable contra `exam-blueprint.schema.json`
- [ ] El Schema Registry v3 NO se modifica
- [ ] `tp-designer` (Valeria) y sus workflows NO se modifican

---

### Entregables Sprint 2

| Archivo | Estado |
|---------|--------|
| `scripts/spaced_repetition.py` | NUEVO |
| `scripts/generate_exam_blueprint.py` | NUEVO |
| `_edu/schemas/exam-blueprint.schema.json` | NUEVO |
| `.github/prompts/edu-spaced-review.prompt.md` | NUEVO |
| `.github/prompts/edu-create-exam.prompt.md` | NUEVO |
| `_edu/module-help.csv` | EXTEND — 2 filas |
| `WORKFLOW_PROMPT_MAP.md` | EXTEND — 2 filas |
| `README.md` | EXTEND — sección "Planificación" |

**Archivos existentes NO tocados:** tp-designer.md, course-planner.md, topic-cycle/*, quality-loops/*, schemas/schema-registry.json

---

## Sprint 3 — GitHub Classroom Integration

**Objetivo:** Automatizar publish y feedback en GitHub Classroom. Nuevos workflows y templates, sin tocar los existentes.

### S3.1 — Classroom Push Directo (#4)

**Story:** Como docente, quiero publicar un TP directamente a GitHub Classroom con un solo comando, sin crear manualmente la Assignment.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/workflows/publish-to-classroom/workflow.md` | Workflow | Push de autograde-repo + creación de Assignment |
| `scripts/classroom_publish.py` | Script | Wrapper de `gh classroom` CLI |
| `.github/prompts/edu-publish-classroom.prompt.md` | Prompt | `/edu-publish-classroom` |
| `.github/prompts/edu-classroom-grades.prompt.md` | Prompt | `/edu-classroom-grades` |

**Prerequisitos del docente (verificados automáticamente):**
- `gh` CLI instalado (`which gh`)
- Extensión `gh classroom` instalada (`gh extension list | grep classroom`)
- Autenticación activa (`gh auth status`)

**Qué hace `classroom_publish.py`:**
- Verifica prerequisitos → mensaje claro si falta algo
- Crea repo template en la org (`gh repo create`)
- Push de `autograde-repo/` al template
- Crea Assignment (`gh classroom assignment create`)
- Guarda metadata en `{topic_folder}/classroom.yaml`
- Output: link de invitación para compartir con alumnos

**Config nuevos (opcionales):**
```yaml
# --- GitHub Classroom (Sprint 3) ---
classroom_enabled: false
classroom_org: ""                           # org de GitHub para la materia
classroom_id: ""                            # ID del classroom
classroom_default_deadline_days: 14         # días desde publicación
```

**Criterios de aceptación:**
- [ ] `python scripts/classroom_publish.py --course leng-2026 --topic 01-intro` publica y devuelve invite link
- [ ] Sin `gh` instalado, imprime instrucciones de instalación y sale con 1
- [ ] Sin `classroom_enabled: true`, imprime "Classroom integration disabled" y sale con 0
- [ ] `autograde-repo/` debe existir previamente (no lo genera — eso lo hace el workflow existente)
- [ ] El workflow `create-autograde-repo/` NO se modifica

---

### S3.2 — Git Auto-Responder (#6)

**Story:** Como docente, quiero que mis repos de TP tengan un bot que responda automáticamente a errores comunes de Git de los alumnos.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/templates/student-helper-action.yml` | Template | GitHub Action YAML para repos de alumnos |
| `_edu/knowledge/git-help-students.md` | Knowledge | Base de respuestas estandarizadas |
| `.github/prompts/edu-setup-auto-responder.prompt.md` | Prompt | `/edu-setup-auto-responder` |

**Qué hace `student-helper-action.yml`:**
- Trigger: `push`, `pull_request`
- Detecta 7 errores comunes (Fiksdal & Riedesel, 2023):
  1. Archivos binarios >1MB commiteados → sugiere `.gitignore`
  2. Push directo a `main` → sugiere workflow de branches
  3. Build failure (test CI) → link a sección relevante de guía de estudio
  4. Commit messages vacíos/genéricos → sugiere formato
  5. Archivos de IDE commiteados (`.idea/`, `.vscode/`) → sugiere `.gitignore`
  6. `node_modules/` o `.venv/` commiteado → sugiere `.gitignore`
  7. Archivos con conflictos de merge no resueltos → tutorial paso a paso
- Respuestas como PR comments via `actions/github-script`
- Mensajes personalizables desde `git-help-students.md`

**Integración con S3.1:** Si `classroom_publish.py` detecta que el template incluye `student-helper-action.yml`, lo copia al repo template automáticamente. Si no existe, todo funciona igual.

**Criterios de aceptación:**
- [ ] `student-helper-action.yml` es YAML válido y funciona en GitHub Actions
- [ ] `git-help-students.md` tiene los 7 patrones documentados con detección y respuesta
- [ ] Es un template — el docente puede editarlo sin afectar el módulo EDU
- [ ] No modifica ningún workflow existente de EDU

---

### Entregables Sprint 3

| Archivo | Estado |
|---------|--------|
| `_edu/workflows/publish-to-classroom/workflow.md` | NUEVO |
| `scripts/classroom_publish.py` | NUEVO |
| `_edu/templates/student-helper-action.yml` | NUEVO |
| `_edu/knowledge/git-help-students.md` | NUEVO |
| `.github/prompts/edu-publish-classroom.prompt.md` | NUEVO |
| `.github/prompts/edu-classroom-grades.prompt.md` | NUEVO |
| `.github/prompts/edu-setup-auto-responder.prompt.md` | NUEVO |
| `_edu/config.yaml` | EXTEND — bloque `# --- GitHub Classroom ---` |
| `_edu/module-help.csv` | EXTEND — 3 filas |

**Archivos existentes NO tocados:** classroom-designer.md, create-autograde-repo/*, topic-cycle/*

---

## Sprint 4 — Inteligencia Cognitiva

**Objetivo:** Validadores opcionales que aplican ciencia cognitiva al diseño de slides. Se activan por flag; desactivados no existen para el sistema.

### S4.1 — Layout Rules Cognitivas (#1)

**Story:** Como docente, quiero que mis slides sean validadas contra principios de Multimedia Learning (Mayer/Fiorella 2023) para maximizar la comprensión.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/schemas/layout-rules.schema.json` | Schema | Reglas cognitivas por tipo de filmina |
| `scripts/validate_layout_cognition.py` | Script | Validador contra reglas cognitivas |
| `.github/prompts/edu-check-cognition.prompt.md` | Prompt | `/edu-check-cognition` |

**Decisión de diseño:** `layout-rules.schema.json` es un schema NUEVO e independiente. No se agrega al Schema Registry (el registry es exclusivo del pipeline de rendering). Es consumido solo por el validador cognitivo.

**Reglas implementadas por tipo:**
- `concepto-abstracto`: max 30 palabras body, imagen obligatoria lado derecho (contigüidad), no clipart decorativo
- `codigo`: max 25 líneas, syntax highlighting implícito, no mezclar lenguajes en misma slide
- `socratica`: título como pregunta, no más de 3 opciones visibles, tiempo de pausa sugerido
- `diagrama`: no más de 7 nodos (Miller), flechas con labels, leyenda si >4 colores
- Regla global: assertion-evidence — título debe ser oración declarativa, no frase nominal (d=0.72-0.84)

**Criterios de aceptación:**
- [ ] `python scripts/validate_layout_cognition.py --topic 01-intro --course leng-2026`
- [ ] Genera `{topic_folder}/cognition-report.md`
- [ ] Sin `cognitive_validation_enabled: true` en config, no ejecuta (sale con 0)
- [ ] No modifica `schema-registry.json`, `academic-guardrail.md`, ni ningún script existente

---

### S4.2 — Cognitive Load Budget (#10)

**Story:** Como docente, quiero un reporte de carga cognitiva por sesión de clase (no solo por slide individual) para detectar agotamiento acumulado.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/cognitive_budget.py` | Script | Calculador de presupuesto cognitivo por clase |
| `.github/prompts/edu-check-cognitive-load.prompt.md` | Prompt | `/edu-check-cognitive-load` |

**Qué hace `cognitive_budget.py`:**
- Lee `filminas.md` del tema → cuenta conceptos nuevos, formato por slide, secuencia
- Aplica reglas (Chen & Sweller, 2023):
  - Máximo 3 slides teóricas consecutivas sin attention reset (socrática/demo/actividad)
  - Máximo 6 conceptos nuevos por bloque de 30 min
  - Curva de complejidad: ideal = U invertida (subir gradualmente, bajar para cierre)
  - Depleción acumulada: penalizar bloques largos sin variación de formato
- Output: `{topic_folder}/cognitive-report.md` con tabla por bloque de 10/15 min + sugerencias

**Config nuevos:**
```yaml
# --- Cognitive Science (Sprint 4) ---
cognitive_validation_enabled: false
cognitive_max_consecutive_theory: 3         # configurable por perfil
cognitive_concepts_per_30min: 6
```

**Criterios de aceptación:**
- [ ] `python scripts/cognitive_budget.py --topic 01-intro --course leng-2026`
- [ ] El guardrail existente NO se modifica — este es un validador independiente
- [ ] Funciona con `filminas.md` (Markdown) — no requiere plan JSON

---

### Entregables Sprint 4

| Archivo | Estado |
|---------|--------|
| `_edu/schemas/layout-rules.schema.json` | NUEVO |
| `scripts/validate_layout_cognition.py` | NUEVO |
| `scripts/cognitive_budget.py` | NUEVO |
| `.github/prompts/edu-check-cognition.prompt.md` | NUEVO |
| `.github/prompts/edu-check-cognitive-load.prompt.md` | NUEVO |
| `_edu/config.yaml` | EXTEND — bloque `# --- Cognitive Science ---` |
| `_edu/module-help.csv` | EXTEND — 2 filas |

**Archivos existentes NO tocados:** academic-guardrail.md, quality-loops/*, schema-registry.json, validate_plan.py, slides_pipeline.py

---

## Sprint 5 — Analytics y Adaptativo

**Objetivo:** Tablas SQLite nuevas para rastrear rendimiento de alumnos y generar learning paths adaptativos. Módulo completamente aislado.

### S5.1 — Student Analytics (#5)

**Story:** Como docente, quiero importar notas de GitHub Classroom y Moodle para detectar alumnos en riesgo con alertas tempranas tipo semáforo.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/student_analytics.py` | Script | Motor de analytics + importadores CSV |
| `.github/prompts/edu-student-analytics.prompt.md` | Prompt | `/edu-student-analytics` |

**Tablas nuevas en memory.db (CREATE IF NOT EXISTS):**
- `students` (student_id, name, email, course_id)
- `grades` (student_id, course_id, topic_id, tp_type, score, max_score, submitted_at)
- `attendance` (student_id, course_id, date, status)
- `risk_alerts` (student_id, course_id, alert_date, risk_level, reason, suggested_action)

**Criterios de aceptación:**
- [ ] `python scripts/student_analytics.py import-grades --csv grades.csv --course leng-2026`
- [ ] `python scripts/student_analytics.py dashboard --course leng-2026` → genera `analytics/dashboard-{fecha}.md`
- [ ] Las tablas nuevas no afectan la tabla `memory_entries` existente
- [ ] `edu_memory.py` sigue funcionando sin cambios
- [ ] Datos de alumnos NO se incluyen en commits automáticos (.gitignore: `analytics/*.csv`)

---

### S5.2 — Adaptive Learning Paths (#7)

**Story:** Como docente, quiero generar rutas de estudio personalizadas (avanzada/estándar/refuerzo) basadas en resultados de diagnóstico.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/adaptive_path.py` | Script | Motor de recomendación de rutas |
| `.github/prompts/edu-adaptive-path.prompt.md` | Prompt | `/edu-adaptive-path` |

**Prerequisito:** S5.1 (necesita scores para calcular rutas).

**Criterios de aceptación:**
- [ ] `python scripts/adaptive_path.py --course leng-2026 --topic 03-memoria --student "García, M."`
- [ ] Output: `{topic_folder}/adaptive/ruta-{nivel}.md` (3 archivos)
- [ ] Sin datos de analytics disponibles, genera solo `ruta-estandar.md` (graceful degradation)

---

### Entregables Sprint 5

| Archivo | Estado |
|---------|--------|
| `scripts/student_analytics.py` | NUEVO |
| `scripts/adaptive_path.py` | NUEVO |
| `.github/prompts/edu-student-analytics.prompt.md` | NUEVO |
| `.github/prompts/edu-adaptive-path.prompt.md` | NUEVO |
| `.gitignore` | EXTEND — `analytics/*.csv` |
| `_edu/module-help.csv` | EXTEND — 2 filas |

**Archivos existentes NO tocados:** edu_memory.py, memory.db (schema — solo tablas nuevas), student-simulator.md

---

## Sprint 6 — Investigación y Arquitectura

**Objetivo:** Módulos de investigación que requieren diseño más extenso. Completamente aislados.

### S6.1 — Curricula Comparator (#3)

**Story:** Como docente, quiero comparar mi programa contra universidades del mundo para detectar gaps o enfoques innovadores.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/agents/curriculum-comparator.md` | Agente | Prof. Internacional 🌍 |
| `.github/agents/edu-agent-curriculum-comparator.md` | Agent file | Activador VS Code |
| `.github/prompts/edu-compare-curriculum.prompt.md` | Prompt | `/edu-compare-curriculum` |

**Criterios de aceptación:**
- [ ] El agente tiene `fetch_webpage` en capabilities para consultar syllabi públicos
- [ ] Output: `{topic_folder}/comparacion-curricular.md`
- [ ] No modifica `academic-researcher.md` ni `topic-designer.md`
- [ ] Es invocable independientemente — no es parte obligatoria del topic-cycle

---

### S6.2 — MCP Server (#9)

**Story:** Como equipo EDU, quiero exponer funcionalidades core como MCP server para que otros agentes/universidades puedan consumirlas.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `edu-mcp-server/server.py` | Server | MCP server Python (stdio) |
| `edu-mcp-server/requirements.txt` | Deps | mcp-sdk |
| `edu-mcp-server/README.md` | Docs | Setup y tools expuestos |

**Prerequisito:** Todos los sprints anteriores estabilizados.

**Criterios de aceptación:**
- [ ] `python edu-mcp-server/server.py` arranca sin errores
- [ ] Tools: `edu.search_memory`, `edu.validate_plan`, `edu.get_slide_template`
- [ ] Configurable en `.vscode/mcp.json` como server stdio
- [ ] Es un módulo separado — no afecta la estructura de `_edu/`

---

### Entregables Sprint 6

| Archivo | Estado |
|---------|--------|
| `_edu/agents/curriculum-comparator.md` | NUEVO |
| `.github/agents/edu-agent-curriculum-comparator.md` | NUEVO |
| `.github/prompts/edu-compare-curriculum.prompt.md` | NUEVO |
| `edu-mcp-server/server.py` | NUEVO |
| `edu-mcp-server/requirements.txt` | NUEVO |
| `edu-mcp-server/README.md` | NUEVO |

**Archivos existentes NO tocados:** Todos los agentes, workflows, schemas y scripts actuales

---

## Registro de Impacto — Archivos Existentes

Estos son los ÚNICOS archivos existentes que se extienden (nunca se borran líneas, solo se agregan):

| Archivo | Sprint | Cambio |
|---------|--------|--------|
| `_edu/config.yaml` | S1, S3, S4 | Bloques de config nuevos al final |
| `_edu/module-help.csv` | S1-S6 | Filas nuevas al final |
| `WORKFLOW_PROMPT_MAP.md` | S1-S6 | Filas nuevas al final |
| `README.md` | S1-S6 | Secciones nuevas al final |
| `.gitignore` | S5 | 1 línea nueva |

**Total archivos existentes afectados: 5** (de ~80+ en el módulo)  
**Archivos NUNCA tocados:** agents/*, workflows/*, schemas/schema-registry.json, scripts existentes, tests

---

## Orden de Ejecución Sugerido

```
S1.1 (accesibilidad) ─┐
S1.2 (composición)  ──┤── parallelizable
S2.1 (spaced rep)   ──┤
S2.2 (exam)         ──┘
         │
         ▼
S3.1 (classroom) ──── S3.2 (auto-responder) ← depende parcialmente de S3.1
         │
         ▼
S4.1 (layout) ────── S4.2 (cognitive) ← independientes
         │
         ▼
S5.1 (analytics) ──── S5.2 (adaptive) ← S5.2 depende de S5.1
         │
         ▼
S6.1 (comparator) ── S6.2 (MCP) ← S6.2 requiere sprints anteriores estables
```

S1 y S2 son completamente parallelizables entre sí (0 dependencias). S3 en adelante son secuenciales solo por recomendación de estabilización, no por dependencias técnicas.
