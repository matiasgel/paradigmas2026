# Sprints de Mejoras v2 — EDU Module (18 propuestas)

**Fecha:** 2026-03-26  
**Supersede:** `sprints-mejoras-edu-v1.md` (12 propuestas, 6 sprints)  
**Cambios v1→v2:** Integra 6 propuestas nuevas del análisis competitivo OpenMAIC (#13-#18). Reorganiza sprints en 8 (antes 6). Las stories de S1-S6 originales se mantienen intactas con ajustes menores de numeración.

**Regla cardinal:** CERO modificaciones destructivas. Todo es aditivo. Los tests actuales deben seguir pasando. Ningún archivo existente pierde funcionalidad.

---

## Principio de seguridad

| Regla | Descripción |
|-------|-------------|
| **Aditivo** | Solo se CREAN archivos nuevos. Los existentes se extienden con campos opcionales |
| **Opt-in** | Todo feature nuevo se activa con un flag en `config.yaml` (default: desactivado) |
| **Schema-safe** | El Schema Registry v3 es INMUTABLE. Schemas nuevos se registran como extensiones |
| **Test-safe** | `test_pipeline.py` y `test_slides_contract.py` siguen pasando sin cambios |
| **Rollback** | Si se borra el archivo nuevo, el sistema vuelve al estado anterior sin efectos secundarios |
| **KB-driven** | Antes de implementar, consultar `python scripts/knowledge_base.py search "tema"` |

---

## Mapa completo: Propuestas → Sprints

| # | Propuesta | Sprint | Fuente | Prioridad |
|---|-----------|--------|--------|-----------|
| 2 | Accesibilidad WCAG | **S1** | EDU | 🔴 Alta |
| 8 | Evidence-Based Slide Audit | **S1** | EDU | 🔴 Alta |
| 11 | Spaced Repetition Engine | **S2** | EDU | 🟡 Media |
| 12 | Exam Blueprint Generator | **S2** | EDU | 🟡 Media |
| 4 | GitHub Classroom Push | **S3** | EDU | 🟡 Media |
| 6 | Git Auto-Responder | **S3** | EDU | 🟡 Media |
| 1 | Layout Rules Cognitivas | **S4** | EDU | 🔴 Alta |
| 10 | Cognitive Load Budget | **S4** | EDU | 🔴 Alta |
| 5 | Student Analytics Dashboard | **S5** | EDU | 🔴 Alta |
| 7 | Adaptive Learning Path | **S5** | EDU | 🔴 Alta |
| 3 | Currícula Comparada (MCP) | **S6** | EDU | 🟡 Media |
| 9 | Cross-Campus MCP Server | **S6** | EDU | 🟡 Media |
| 13 | Interactive Scene Generator | **S7** | OpenMAIC | 🔴 Alta |
| 14 | Whiteboard Annotations | **S7** | OpenMAIC | 🟡 Media |
| 17 | TTS Narration | **S7** | OpenMAIC | 🟡 Media |
| 18 | Classmate Agents (Debate Sim) | **S7** | OpenMAIC | 🔴 Alta |
| 15 | PBL Generator | **S8** | OpenMAIC | 🔴 Alta |
| 16 | Multi-Agent LangGraph Orchestration | **S8** | OpenMAIC | 🔴 Alta |

---

## Resumen de Sprints

| Sprint | Nombre | Items | Foco | Riesgo | Deps |
|--------|--------|-------|------|--------|------|
| **S1** | Validadores pasivos | #2, #8 | Scripts que leen y reportan. No modifican nada | Nulo | — |
| **S2** | Herramientas docentes | #11, #12 | Scripts + prompts nuevos para planificación | Nulo | — |
| **S3** | GitHub Classroom | #4, #6 | Workflow nuevo + templates GitHub Actions | Nulo | — |
| **S4** | Inteligencia cognitiva | #1, #10 | Schemas de extensión + validadores | Bajo | — |
| **S5** | Analytics y adaptativo | #5, #7 | Tablas SQLite nuevas + scripts | Bajo | — |
| **S6** | Investigación | #3, #9 | Agente nuevo + MCP server | Bajo | S1-S5 |
| **S7** | Interactividad y simulación | #13, #14, #17, #18 | Nuevos tipos de artefactos + agentes | Medio | S1, S4 |
| **S8** | Orquestación avanzada | #15, #16 | PBL multi-clase + Director Agent | Alto | S3, S5, S7 |

**S1-S4 son paralelizables.** S5 es independiente. S6 requiere estabilización previa. S7 requiere S1 (WCAG para validar HTML) y S4 (reglas cognitivas). S8 requiere la mayoría de los anteriores.

---

## Sprint 1 — Validadores Pasivos

**Objetivo:** Scripts que leen artefactos existentes y generan reportes. No tocan nada.  
**Duración estimada:** 1 ciclo de trabajo.

### S1.1 — Accesibilidad WCAG (#2)

**Story:** Como docente, quiero validar que mis slides cumplen WCAG 2.2 AA para que alumnos con discapacidades visuales puedan consumirlas.

**KB consultar:** `python scripts/knowledge_base.py search "WCAG contrast accessibility" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/validate_accessibility.py` | Script | Validador de contraste, tipografía mínima, alt_text |
| `.github/prompts/edu-check-accessibility.prompt.md` | Prompt | `/edu-check-accessibility` |

**Qué hace `validate_accessibility.py`:**
- Lee `_edu/slides-config.yaml` → extrae `palette` (colores hex)
- Calcula contraste relativo (fórmula WCAG: luminancia relativa)
- Verifica contra umbrales AA (4.5:1 texto normal, 3:1 texto grande) y AAA (7:1)
- Lee `config.yaml` → si existe `classroom_distance_meters`, calcula tamaño mínimo tipográfico recomendado
- Lee plan JSON del tema → verifica que cada filmina con `image_file` tenga `alt_text` no vacío
- Output: `{topic_folder}/accessibility-report.md` con score A/AA/F por slide

**Config nuevos (opcionales, al final de config.yaml):**
```yaml
# --- Accessibility (Sprint 1) ---
accessibility_check_enabled: false
delivery_mode: "presencial"                 # presencial | remoto | hybrid
classroom_distance_meters: 6
screen_resolution: "1080p"
```

**Criterios de aceptación:**
- [ ] `python scripts/validate_accessibility.py --topic 01-intro --course leng-2026` genera reporte
- [ ] Sin flag `accessibility_check_enabled: true`, imprime aviso y sale con 0
- [ ] `test_pipeline.py` sigue pasando sin cambios
- [ ] Sin dependencias nuevas (solo stdlib: `colorsys`, `json`, `re`)

---

### S1.2 — Auditoría Visual de Slides (#8)

**Story:** Como docente, quiero validar que la composición visual de mis slides respeta márgenes seguros, densidad visual y patrones de atención.

**KB consultar:** `python scripts/knowledge_base.py search "slide composition visual density margins" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/validate_slide_composition.py` | Script | Validador de márgenes, densidad, patrón Z |
| `.github/prompts/edu-check-composition.prompt.md` | Prompt | `/edu-check-composition` |

**Qué hace `validate_slide_composition.py`:**
- Lee `_edu/schemas/pipeline-runtime.schema.json` → obtiene geometría EMU
- Por cada filmina en plan JSON:
  - **Margen seguro:** `position_x`, `position_y` dentro del 5% del borde
  - **Densidad visual:** Ratio área-ocupada / área-total. Ideal: 35-55% (Scheiter & Eitel)
  - **Elementos superpuestos:** Colisiones de bounding boxes entre title, body, image, code_block
- Output: `{topic_folder}/composition-report.md` con score A/B/C/F por slide

**Criterios de aceptación:**
- [ ] `python scripts/validate_slide_composition.py --topic 01-intro --course leng-2026`
- [ ] Solo lectura y reporte — no modifica archivos
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

**NO tocar:** agents/*, workflows/*, schemas/*, tests/*, slides_pipeline.py, validate_plan.py, parse_filminas.py, edu_memory.py

---

## Sprint 2 — Herramientas de Planificación Docente

**Objetivo:** Scripts independientes que ayudan al docente a planificar repasos y exámenes. No interactúan con el pipeline de slides.

### S2.1 — Spaced Repetition Engine (#11)

**Story:** Como docente, quiero un calendario de repasos distribuidos para insertar slides de revisión en clases futuras, combatiendo la curva del olvido.

**KB consultar:** `python scripts/knowledge_base.py search "FSRS spaced repetition schedule" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/spaced_repetition.py` | Script | Motor FSRS v4 de repaso distribuido |
| `.github/prompts/edu-spaced-review.prompt.md` | Prompt | `/edu-spaced-review` |

**Qué hace `spaced_repetition.py`:**
- Modelo DSR (Difficulty, Stability, Retrievability) — FSRS v4 (Ye 2023-2024)
- Python puro: solo `math`, `datetime`, `json`, `sqlite3`
- Lee `plan-borrador.md` → lista de temas con fechas de clase
- Lee scores de TPs (si existen en `memory.db`) → calibra dificultad
- Output:
  - `{course_output_folder}/repaso-calendario.md` — calendario Markdown
  - `{topic_folder}/slides-repaso.md` — 2-3 slides template tipo socrática
- Tabla nueva en `memory.db`: `spaced_reviews` (topic_id, review_date, review_number, score, next_review)

**Criterios de aceptación:**
- [ ] `python scripts/spaced_repetition.py --course leng-2026 generate` → calendario
- [ ] `python scripts/spaced_repetition.py --course leng-2026 --topic 01-intro record --score 0.7` → registra resultado
- [ ] Tabla `spaced_reviews` se crea con `IF NOT EXISTS`
- [ ] Sin temas registrados, sale con 0 y mensaje informativo

---

### S2.2 — Exam Blueprint Generator (#12)

**Story:** Como docente, quiero generar parciales con cobertura garantizada de temas y distribución explícita de Bloom.

**KB consultar:** `python scripts/knowledge_base.py search "Bloom taxonomy assessment matrix exam" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/schemas/exam-blueprint.schema.json` | Schema | JSON Schema para blueprints (independiente del registry) |
| `scripts/generate_exam_blueprint.py` | Script | Genera tabla de especificaciones automática |
| `.github/prompts/edu-create-exam.prompt.md` | Prompt | `/edu-create-exam` |

**Qué hace `generate_exam_blueprint.py`:**
- Input: temas + puntos + tiempo
- Lee minuta.md → extrae conceptos y niveles de Bloom
- Distribuye puntos proporcional al tiempo dedicado
- Bloom default: 20% recordar, 30% comprender, 30% aplicar, 15% analizar, 5% evaluar
- Output: `{course_output_folder}/evaluaciones/blueprint-parcial-N.json` + `.md`

**Criterios de aceptación:**
- [ ] `python scripts/generate_exam_blueprint.py --course leng-2026 --topics "01-intro,02-tipos" --points 100 --time 120`
- [ ] Output validable contra `exam-blueprint.schema.json`
- [ ] Schema Registry v3 NO se modifica

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

---

## Sprint 3 — GitHub Classroom Integration

**Objetivo:** Automatizar publish y feedback en GitHub Classroom. Workflows y templates nuevos.

### S3.1 — Classroom Push Directo (#4)

**Story:** Como docente, quiero publicar un TP directamente a GitHub Classroom con un solo comando.

**KB consultar:** `python scripts/knowledge_base.py search "GitHub Classroom assignment create CLI" --type tool`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/workflows/publish-to-classroom/workflow.md` | Workflow | Push de autograde-repo + Assignment |
| `scripts/classroom_publish.py` | Script | Wrapper de `gh classroom` CLI |
| `.github/prompts/edu-publish-classroom.prompt.md` | Prompt | `/edu-publish-classroom` |
| `.github/prompts/edu-classroom-grades.prompt.md` | Prompt | `/edu-classroom-grades` |

**Config nuevos:**
```yaml
# --- GitHub Classroom (Sprint 3) ---
classroom_enabled: false
classroom_org: ""
classroom_id: ""
classroom_default_deadline_days: 14
```

**Criterios de aceptación:**
- [ ] `python scripts/classroom_publish.py --course leng-2026 --topic 01-intro` publica y devuelve invite link
- [ ] Sin `gh` instalado, imprime instrucciones y sale con 1
- [ ] Sin `classroom_enabled: true`, sale con 0
- [ ] `autograde-repo/` debe existir (no lo genera)

---

### S3.2 — Git Auto-Responder (#6)

**Story:** Como docente, quiero que los repos de TP tengan un bot que responda a errores comunes de Git de alumnos.

**KB consultar:** `python scripts/knowledge_base.py search "Git errors students GitHub Actions" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/templates/student-helper-action.yml` | Template | GitHub Action YAML para repos alumnos |
| `_edu/knowledge/git-help-students.md` | Knowledge | Base de respuestas estandarizadas |
| `.github/prompts/edu-setup-auto-responder.prompt.md` | Prompt | `/edu-setup-auto-responder` |

**Detecta 7 errores comunes:**
1. Archivos binarios >1MB
2. Push directo a `main`
3. Build failure (test CI)
4. Commit messages vacíos/genéricos
5. Archivos de IDE (`.idea/`, `.vscode/`)
6. `node_modules/` o `.venv/`
7. Conflictos de merge no resueltos

**Criterios de aceptación:**
- [ ] YAML válido para GitHub Actions
- [ ] 7 patrones documentados en `git-help-students.md`
- [ ] Template editable — no afecta el módulo EDU

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

---

## Sprint 4 — Inteligencia Cognitiva

**Objetivo:** Validadores opcionales que aplican ciencia cognitiva al diseño de slides. Se activan por flag.

### S4.1 — Layout Rules Cognitivas (#1)

**Story:** Como docente, quiero que mis slides sean validadas contra principios de Multimedia Learning (Mayer/Fiorella 2023).

**KB consultar:** `python scripts/knowledge_base.py search "multimedia learning spatial contiguity assertion evidence" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/schemas/layout-rules.schema.json` | Schema | Reglas cognitivas por tipo de filmina |
| `scripts/validate_layout_cognition.py` | Script | Validador contra reglas cognitivas |
| `.github/prompts/edu-check-cognition.prompt.md` | Prompt | `/edu-check-cognition` |

**Reglas por tipo:**
- `concepto-abstracto`: max 30 palabras body, imagen obligatoria, no clipart decorativo
- `codigo`: max 25 líneas, no mezclar lenguajes en misma slide
- `socratica`: título pregunta, max 3 opciones, pausa sugerida
- `diagrama`: max 7 nodos (Miller), flechas con labels
- Global: assertion-evidence (título = oración declarativa, d=0.72-0.84)

**Config nuevos:**
```yaml
# --- Cognitive Science (Sprint 4) ---
cognitive_validation_enabled: false
cognitive_max_consecutive_theory: 3
cognitive_concepts_per_30min: 6
```

**Criterios de aceptación:**
- [ ] `python scripts/validate_layout_cognition.py --topic 01-intro --course leng-2026`
- [ ] Genera `{topic_folder}/cognition-report.md`
- [ ] Sin flag, sale con 0
- [ ] No modifica `schema-registry.json`

---

### S4.2 — Cognitive Load Budget (#10)

**Story:** Como docente, quiero un reporte de carga cognitiva por sesión de clase para detectar agotamiento acumulado.

**KB consultar:** `python scripts/knowledge_base.py search "cognitive load theory intrinsic extraneous germane" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/cognitive_budget.py` | Script | Calculador de presupuesto cognitivo por clase |
| `.github/prompts/edu-check-cognitive-load.prompt.md` | Prompt | `/edu-check-cognitive-load` |

**Reglas (Chen & Sweller, 2023):**
- Max 3 slides teóricas consecutivas sin attention reset
- Max 6 conceptos nuevos por bloque de 30 min
- Curva: U invertida (subir gradualmente, bajar para cierre)
- Penalizar bloques largos sin variación de formato

**Criterios de aceptación:**
- [ ] `python scripts/cognitive_budget.py --topic 01-intro --course leng-2026`
- [ ] Funciona con `filminas.md` (no requiere plan JSON)
- [ ] Guardrail existente NO se modifica

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

---

## Sprint 5 — Analytics y Adaptativo

**Objetivo:** Tablas SQLite nuevas para rastrear rendimiento de alumnos y generar learning paths.

### S5.1 — Student Analytics (#5)

**Story:** Como docente, quiero importar notas de GitHub Classroom y Moodle para detectar alumnos en riesgo con alertas semáforo.

**KB consultar:** `python scripts/knowledge_base.py search "learning analytics early warning at-risk" --type reference`

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
- [ ] `python scripts/student_analytics.py dashboard --course leng-2026` → `analytics/dashboard-{fecha}.md`
- [ ] Tablas nuevas no afectan `memory_entries` existente
- [ ] `.gitignore`: `analytics/*.csv` para proteger datos personales

---

### S5.2 — Adaptive Learning Paths (#7)

**Story:** Como docente, quiero generar rutas de estudio personalizadas basadas en resultados de diagnóstico.

**KB consultar:** `python scripts/knowledge_base.py search "adaptive learning ITS knowledge tracing" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/adaptive_path.py` | Script | Motor de recomendación de rutas |
| `.github/prompts/edu-adaptive-path.prompt.md` | Prompt | `/edu-adaptive-path` |

**Prerequisito:** S5.1 (necesita scores).

**Criterios de aceptación:**
- [ ] `python scripts/adaptive_path.py --course leng-2026 --topic 03-memoria --student "García, M."`
- [ ] Output: `{topic_folder}/adaptive/ruta-{nivel}.md` (3 archivos: avanzada/estándar/refuerzo)
- [ ] Sin datos, genera solo `ruta-estandar.md` (graceful degradation)

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

---

## Sprint 6 — Investigación y Arquitectura

**Objetivo:** Módulos de investigación que requieren diseño extenso. Completamente aislados.

### S6.1 — Curricula Comparator (#3)

**Story:** Como docente, quiero comparar mi programa contra universidades del mundo para detectar gaps.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/agents/curriculum-comparator.md` | Agente | Prof. Internacional 🌍 |
| `.github/agents/edu-agent-curriculum-comparator.md` | Agent file | Activador VS Code |
| `.github/prompts/edu-compare-curriculum.prompt.md` | Prompt | `/edu-compare-curriculum` |

**Criterios de aceptación:**
- [ ] Agente usa `fetch_webpage` para syllabi públicos
- [ ] Output: `{topic_folder}/comparacion-curricular.md`
- [ ] No modifica agentes existentes

---

### S6.2 — MCP Server (#9)

**Story:** Como equipo EDU, quiero exponer funcionalidades core como MCP server para consumo externo.

**KB consultar:** `python scripts/knowledge_base.py search "MCP server FastMCP tools expose" --type tool`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `edu-mcp-server/server.py` | Server | MCP server Python (stdio) |
| `edu-mcp-server/requirements.txt` | Deps | mcp-sdk |
| `edu-mcp-server/README.md` | Docs | Setup y tools expuestos |

**Prerequisito:** Sprints anteriores estabilizados.

**Criterios de aceptación:**
- [ ] `python edu-mcp-server/server.py` arranca sin errores
- [ ] Tools: `edu.search_memory`, `edu.validate_plan`, `edu.get_slide_template`
- [ ] Configurable en `.vscode/mcp.json`

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

---

## Sprint 7 — Interactividad y Simulación (OpenMAIC)

**Objetivo:** Dotar a EDU de capacidades interactivas inspiradas en OpenMAIC, pero integradas con el framework de calidad de EDU. Nuevos tipos de artefactos, agentes y validadores.

**Dependencias:** S1 (WCAG para validar HTML interactivo), S4 (reglas cognitivas para validar simulaciones).  
**KB consultar:** `python scripts/knowledge_base.py search "OpenMAIC interactive scene whiteboard" --type tool`

### S7.1 — Interactive Scene Generator (#13)

**Story:** Como docente, quiero generar simulaciones HTML interactivas para conceptos que se benefician de interactividad (visualizar recursión, simular scheduling, manipular árboles), con enlace/QR automático en las filminas.

**Evidencia (KB refs):** Wieman & Perkins 2023 (PhET, d=0.82), Freeman et al. 2023 (active learning +0.47 SD), OpenMAIC `scene-generator.ts`.

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/generate_interactive.py` | Script | Generador de HTML interactivo desde spec |
| `_edu/schemas/interactive-scene.schema.json` | Schema | Contrato para simulaciones (tipo, inputs, comportamiento esperado) |
| `_edu/templates/interactive-base.html` | Template | Plantilla HTML base con canvas/SVG + controles |
| `.github/prompts/edu-create-interactive.prompt.md` | Prompt | `/edu-create-interactive` |

**Qué hace `generate_interactive.py`:**
- Input: `interactive-spec.json` con tipo de simulación + parámetros
- Tipos soportados (v1):
  - `sorting-visualizer` — Comparación de algoritmos de sorting con animación paso-a-paso
  - `tree-explorer` — Visualización de BST/AVL con inserción/eliminación interactiva
  - `stack-simulator` — Simulación de stack con operaciones push/pop/peek
  - `fsm-simulator` — Autómata finito interactivo con transiciones
  - `memory-layout` — Visualización de layout de memoria (stack/heap/data)
  - `custom` — Template vacío para el agente
- Output: `{topic_folder}/interactivos/simulacion-{nombre}.html` (HTML + CSS + JS autocontenido)
- Pipeline integration: detecta `<!-- interactive: nombre.html -->` en `filminas.md` → agrega enlace/QR en slide
- Validación:
  - El HTML pasa `validate_accessibility.py` (S1.1) — alt_text, contraste, keyboard-nav
  - El HTML es autocontenido (no CDNs externos, no fetch a servidores)
  - Tamaño < 500KB por simulación

**Schema `interactive-scene.schema.json`:**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "EDU Interactive Scene",
  "type": "object",
  "required": ["type", "title", "topic_id", "concept"],
  "properties": {
    "type": {
      "enum": ["sorting-visualizer", "tree-explorer", "stack-simulator",
               "fsm-simulator", "memory-layout", "custom"]
    },
    "title": { "type": "string", "minLength": 5 },
    "topic_id": { "type": "string" },
    "concept": { "type": "string", "description": "Concepto pedagógico que la simulación aborda" },
    "bloom_level": { "enum": ["apply", "analyze", "evaluate", "create"] },
    "inputs": {
      "type": "object",
      "description": "Parámetros específicos del tipo de simulación"
    },
    "accessibility": {
      "type": "object",
      "properties": {
        "keyboard_navigable": { "type": "boolean", "default": true },
        "screen_reader_labels": { "type": "boolean", "default": true },
        "high_contrast_mode": { "type": "boolean", "default": false }
      }
    }
  }
}
```

**Config nuevos:**
```yaml
# --- Interactivity (Sprint 7) ---
interactive_scenes_enabled: false
interactive_max_size_kb: 500
interactive_types:
  - sorting-visualizer
  - tree-explorer
  - stack-simulator
  - fsm-simulator
  - memory-layout
  - custom
```

**Criterios de aceptación:**
- [ ] `python scripts/generate_interactive.py --spec interactivos/spec-sorting.json --topic 05-sorting --course leng-2026`
- [ ] El HTML generado es autocontenido — abrirlo con `file://` funciona sin servidor
- [ ] Pasa `validate_accessibility.py` (contraste, keyboard-nav)
- [ ] `filminas.md` con `<!-- interactive: ... -->` genera enlace en el slide correspondiente
- [ ] Sin `interactive_scenes_enabled: true`, aviso y sale con 0
- [ ] `test_pipeline.py` sigue pasando (el pipeline ignora bloques `<!-- interactive -->` si la feature está desactivada)

---

### S7.2 — Whiteboard Annotations (#14)

**Story:** Como docente, quiero instrucciones de dibujo paso-a-paso por filmina en mi guía-profesor, basadas en el principio Drawing de Mayer (d=0.40), para desarrollar conceptos visualmente durante la clase.

**Evidencia (KB refs):** Fiorella & Mayer 2023 (Drawing principle, d=0.40), OpenMAIC `tool-schemas.ts` (13 acciones de whiteboard).

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/schemas/annotation-steps.schema.json` | Schema | Contrato para secuencia de anotaciones |
| `.github/prompts/edu-create-annotations.prompt.md` | Prompt | `/edu-create-annotations` |

**Qué hace `/edu-create-annotations`:**
- No es un script Python — es un prompt que el agente `class-writer` (Roberto) ejecuta.
- Input: `filminas.md` del tema + plan JSON
- Para cada filmina de tipo `concepto-abstracto`, `diagrama`, o `codigo`:
  - Genera secuencia de pasos de anotación: `draw_text` → `draw_arrow` → `highlight` → `draw_shape`
  - Cada paso tiene: descripción textual + duración sugerida (ej: "20 seg")
- Output: campo adicional en `guia-profesor.md` — sección "📝 Desarrollo Visual" por filmina
- Formato de anotaciones:
  ```markdown
  #### 📝 Desarrollo Visual — Filmina 5 (Diagrama de Clases)
  1. **Dibujar** rectángulo central "Clase Animal" (15 seg)
  2. **Escribir** atributos: nombre, edad (10 seg)
  3. **Flecha** hacia abajo: "herencia" (5 seg)
  4. **Dibujar** rectángulo "Clase Perro" con atributos específicos (15 seg)
  5. **Destacar** la relación con color (5 seg)
  > Total: ~50 seg | Bloom: Comprender → Aplicar
  ```

**Schema `annotation-steps.schema.json`:**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "EDU Annotation Steps",
  "type": "object",
  "required": ["slide_number", "slide_type", "steps"],
  "properties": {
    "slide_number": { "type": "integer", "minimum": 1 },
    "slide_type": { "type": "string" },
    "steps": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["action", "description", "duration_seconds"],
        "properties": {
          "action": { "enum": ["draw_text", "draw_shape", "draw_arrow", "draw_line", "highlight", "erase", "label"] },
          "description": { "type": "string" },
          "duration_seconds": { "type": "integer", "minimum": 5, "maximum": 120 },
          "position": { "type": "string", "description": "Ubicación relativa: centro, derecha, arriba-izq, etc." }
        }
      },
      "minItems": 2
    },
    "total_duration_seconds": { "type": "integer" },
    "bloom_progression": { "type": "string" }
  }
}
```

**Criterios de aceptación:**
- [ ] `/edu-create-annotations` genera sección "Desarrollo Visual" en `guia-profesor.md`
- [ ] Solo para filminas tipo `concepto-abstracto`, `diagrama`, `codigo` — las de tipo `titulo` o `cierre` no aplican
- [ ] Las anotaciones respetan el tiempo de minuta asignado a esa filmina
- [ ] La guía-profesor existente se extiende — no se sobreescribe

---

### S7.3 — TTS Narration (#17)

**Story:** Como docente, quiero generar audio MP3 por filmina para clases asíncronas, repaso, y accesibilidad (alumnos con dificultades de lectura).

**Evidencia (KB refs):** Fiorella & Mayer 2023 (Modality principle, d=0.72; Personalization, d=0.79), Craig & Schroeder 2023 (voces TTS neurales ≈ humanas).

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/generate_tts.py` | Script | Generador de audio TTS desde minuta |
| `.github/prompts/edu-generate-audio.prompt.md` | Prompt | `/edu-generate-audio` |

**Qué hace `generate_tts.py`:**
- Lee `minuta.md` del tema → extrae el guión por filmina (sección "Guión del docente")
- Proveedores (seleccionable por config):
  - **`edge-tts`** (default) — gratuito, offline, Microsoft Edge Neural Voices, calidad alta
  - `gcloud-tts` — Google Cloud Text-to-Speech ($4/1M chars)
  - `elevenlabs` — ElevenLabs API (voz personalizada)
- Output: `{topic_folder}/audio/filmina-{N}.mp3` + `audio-manifest.json`
- `audio-manifest.json` contiene: filmina_number, duration_seconds, text_length, provider

**Dependencia pip:** `edge-tts` (MIT license, async, 30+ voces en español)

**Config nuevos:**
```yaml
# --- TTS (Sprint 7) ---
tts_enabled: false
tts_provider: "edge-tts"                   # edge-tts | gcloud-tts | elevenlabs
tts_voice: "es-AR-TomasNeural"             # voz específica del provider
tts_rate: "+0%"                            # velocidad: -20% a +30%
tts_output_format: "mp3"                   # mp3 | wav
```

**Criterios de aceptación:**
- [ ] `python scripts/generate_tts.py --topic 01-intro --course leng-2026`
- [ ] Genera `audio/filmina-{N}.mp3` para cada filmina con guión
- [ ] `audio-manifest.json` válido con duración y metadata
- [ ] Sin `tts_enabled: true`, sale con 0
- [ ] El script solicita confirmación antes de llamar a API pagos (gcloud/elevenlabs)
- [ ] `requirements.txt` → `edge-tts>=6.1.0` (solo si el feature se activa)

---

### S7.4 — Classmate Agents para Simulación de Debate (#18)

**Story:** Como docente, quiero simular una clase completa con N perfiles de alumnos interactuando (no solo respuestas individuales) para evaluar cómo funcionará el material antes de la clase real.

**Evidencia (KB refs):** Yu et al. 2024 MAIC (taxonomía Schwanke TI/ID/EC/CM), Park et al. 2023 (Generative Agents), Yue et al. 2024 (MathVC multi-agent classroom).

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/agents/classroom-simulator.md` | Agente | Director de simulación de aula completa 🎭 |
| `.github/agents/edu-agent-classroom-simulator.md` | Agent file | Activador VS Code |
| `_edu/templates/student-profiles-schwanke.yaml` | Template | 4 arquetipos de alumnos (TI/ID/EC/CM) |
| `.github/prompts/edu-simulate-classroom.prompt.md` | Prompt | `/edu-simulate-classroom` |

**Qué hace `classroom-simulator`:**
- Evoluciona `/edu-test-topic` de simulación individual → simulación grupal
- Carga N perfiles de alumnos (default: 4 arquetipos Schwanke):
  1. **Inquisitive Mind** (TI — Teaching & Initiation): "¿Qué pasa si...?", "No entendí la relación con..."
  2. **Deep Thinker** (ID — In-depth Discussion): "Esto se conecta con el paper de...", "¿No sería mejor...?"
  3. **Note Taker** (EC — Emotional Companionship): "¿Esto entra en el parcial?", "¿Podés repetir?"
  4. **Distracted Student** (CM — Classroom Management): requiere re-engagement, pierde el hilo
- Input: `filminas.md` + `minuta.md` del tema
- Simula la clase en turnos (docente → alumno → docente → debate → ...)
- Output:
  - `{topic_folder}/simulacion/transcripcion-debate.md` — transcripción completa
  - `{topic_folder}/simulacion/metricas-simulacion.md` — cobertura Bloom por perfil, preguntas difíciles, momentos de confusión
  - Registro en `memory.db`: categoría `simulation-result`, insights para futura referencia

**Integración con simulador existente:**
- El agente `student-simulator` existente (`/edu-test-topic`) sigue funcionando para simulación individual
- El nuevo `classroom-simulator` es complementario — simula la dinámica grupal
- Comparten los perfiles de `student-profiles-schwanke.yaml`
- **Ventaja sobre OpenMAIC:** EDU puede comparar simulación vs. encuesta real post-clase (`/edu-compare-survey-simulator`)

**Criterios de aceptación:**
- [ ] `/edu-simulate-classroom` genera transcripción con ≥4 perfiles interactuando
- [ ] Cada perfil tiene personalidad coherente a lo largo de la simulación
- [ ] Métricas incluyen: cobertura de Bloom, preguntas no resueltas, nivel de engagement estimado por perfil
- [ ] El agente `student-simulator` existente NO se modifica
- [ ] La transcripción se registra en `memory.db` como `simulation-result`

---

### Entregables Sprint 7

| Archivo | Estado |
|---------|--------|
| `scripts/generate_interactive.py` | NUEVO |
| `_edu/schemas/interactive-scene.schema.json` | NUEVO |
| `_edu/templates/interactive-base.html` | NUEVO |
| `.github/prompts/edu-create-interactive.prompt.md` | NUEVO |
| `_edu/schemas/annotation-steps.schema.json` | NUEVO |
| `.github/prompts/edu-create-annotations.prompt.md` | NUEVO |
| `scripts/generate_tts.py` | NUEVO |
| `.github/prompts/edu-generate-audio.prompt.md` | NUEVO |
| `_edu/agents/classroom-simulator.md` | NUEVO |
| `.github/agents/edu-agent-classroom-simulator.md` | NUEVO |
| `_edu/templates/student-profiles-schwanke.yaml` | NUEVO |
| `.github/prompts/edu-simulate-classroom.prompt.md` | NUEVO |
| `_edu/config.yaml` | EXTEND — bloques Interactivity + TTS |
| `_edu/module-help.csv` | EXTEND — 4 filas |
| `WORKFLOW_PROMPT_MAP.md` | EXTEND — 4 filas |
| `README.md` | EXTEND — sección "Interactividad y Simulación" |
| `scripts/requirements.txt` | EXTEND — `edge-tts>=6.1.0` (condicional) |

**NO tocar:** student-simulator.md, topic-cycle/*, quality-loops/*, schema-registry.json, slides_pipeline.py

---

## Sprint 8 — Orquestación Avanzada y PBL (OpenMAIC)

**Objetivo:** Features de alto nivel que requieren la mayoría de los sprints anteriores. Implementar PBL multi-clase y orquestación automática con Director Agent.

**Dependencias:** S3 (GitHub Classroom para PBL), S5 (analytics para PBL), S7 (simulación para validar PBL).

### S8.1 — PBL Generator (#15)

**Story:** Como docente, quiero generar proyectos multi-clase con driving question, milestones, deliverables evaluables y rúbricas, integrando GitHub Classroom para repos grupales.

**Evidencia (KB refs):** Krajcik & Shin 2022 (PBL, d=0.50), Kokotsaki et al. 2023 (condiciones efectividad), Denny et al. 2024 (PBL + IA: scaffolding explícito).

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/schemas/pbl-project.schema.json` | Schema | Contrato para proyectos PBL |
| `_edu/agents/pbl-designer.md` | Agente | Diseñador de proyectos multi-clase 🏗️ |
| `.github/agents/edu-agent-pbl-designer.md` | Agent file | Activador VS Code |
| `_edu/workflows/create-pbl/workflow.md` | Workflow | Ciclo completo de diseño PBL |
| `_edu/templates/pbl-rubric-template.md` | Template | Rúbrica por milestone |
| `.github/prompts/edu-create-pbl.prompt.md` | Prompt | `/edu-create-pbl` |
| `.github/prompts/edu-pbl-status.prompt.md` | Prompt | `/edu-pbl-status` |

**Schema `pbl-project.schema.json`:**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "EDU PBL Project",
  "type": "object",
  "required": ["title", "driving_question", "duration_weeks", "milestones", "topics_covered"],
  "properties": {
    "title": { "type": "string" },
    "driving_question": { "type": "string", "minLength": 20, "description": "Pregunta motivadora del proyecto" },
    "duration_weeks": { "type": "integer", "minimum": 2, "maximum": 16 },
    "team_size": { "type": "integer", "minimum": 1, "maximum": 6, "default": 3 },
    "topics_covered": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 2,
      "description": "IDs de temas del plan mínimo cubiertos por el PBL"
    },
    "bloom_target": {
      "type": "string",
      "enum": ["apply", "analyze", "evaluate", "create"],
      "default": "create"
    },
    "milestones": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "week", "deliverable", "weight_percent"],
        "properties": {
          "name": { "type": "string" },
          "week": { "type": "integer" },
          "deliverable": { "type": "string", "description": "Qué entrega: commit, documento, presentación, demo" },
          "weight_percent": { "type": "number", "minimum": 5, "maximum": 50 },
          "rubric_criteria": { "type": "array", "items": { "type": "string" } },
          "prerequisite_topics": { "type": "array", "items": { "type": "string" } }
        }
      },
      "minItems": 3
    },
    "github_classroom": {
      "type": "object",
      "properties": {
        "template_repo": { "type": "string" },
        "branch_per_milestone": { "type": "boolean", "default": true },
        "autograding_enabled": { "type": "boolean", "default": false }
      }
    },
    "anti_delegation_measures": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Medidas para evitar que alumnos deleguen todo al LLM (Denny et al. 2024)"
    }
  }
}
```

**Qué hace el workflow `create-pbl`:**
1. El docente invoca `/edu-create-pbl` con tema/scope
2. `pbl-designer` analiza temas del plan mínimo → propone driving question
3. Docente aprueba/modifica (human-in-the-loop gate)
4. Genera milestones con deliverables + rúbricas + anti-delegation measures
5. Si S3 (Classroom) está activo: crea repo template grupal con branches por milestone
6. Si S7.4 (Simulador) está activo: simula la factibilidad del PBL con perfiles de alumnos
7. Output: `{course_output_folder}/pbl/pbl-{nombre}.json` + `.md` + rúbricas

**Criterios de aceptación:**
- [ ] `/edu-create-pbl` genera proyecto validable contra `pbl-project.schema.json`
- [ ] Milestones tienen prerequisite_topics que se verifican contra plan mínimo
- [ ] anti_delegation_measures incluyen ≥2 medidas (ej: "presentación oral", "peer review")
- [ ] Sin S3 activo, omite integración GitHub — todo lo demás funciona
- [ ] El tp-designer (Valeria) NO se modifica — PBL es un tipo distinto de evaluación

---

### S8.2 — Multi-Agent Orchestration con Director Agent (#16)

**Story:** Como docente, quiero generar todo el material de un tema con un solo comando (`/edu-auto-topic`) que invoque automáticamente a todos los agentes en secuencia, con gates de calidad obligatorios.

**Evidencia (KB refs):** Yu et al. 2024 (Director Agent), Wu et al. 2023 (AutoGen), Hong et al. 2023 (MetaGPT SOPs), OpenMAIC `director-graph.ts` (LangGraph StateGraph).

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `_edu/agents/topic-director.md` | Agente | Director de producción de tema completo 🎬 |
| `.github/agents/edu-agent-topic-director.md` | Agent file | Activador VS Code |
| `_edu/workflows/auto-topic/workflow.md` | Workflow | Ciclo automático de producción completa |
| `_edu/schemas/director-state.schema.json` | Schema | Estado del Director (para checkpoints) |
| `.github/prompts/edu-auto-topic.prompt.md` | Prompt | `/edu-auto-topic` |
| `.github/prompts/edu-resume-topic.prompt.md` | Prompt | `/edu-resume-topic` (reanudar desde checkpoint) |

**Flujo del Director Agent:**
```
/edu-auto-topic --topic 05-sorting --course leng-2026

1. [DIRECTOR] Lee topic.yaml + active-topic.yaml + memory.db
   ↓
2. [DIRECTOR → Marcos (topic-designer)] Generar diseño del tema
   ↓ checkpoint: design-complete
3. [GATE] Docente aprueba diseño ← human-in-the-loop (OBLIGATORIO)
   ↓
4. [DIRECTOR → Roberto (class-writer)] Generar minuta + filminas
   ↓ checkpoint: content-complete
5. [QUALITY LOOP] coherencia-validator + guardrail automático
   ↓
6. [DIRECTOR → Pipeline] parse_filminas → validate_plan → slides_pipeline
   ↓ checkpoint: slides-pipeline-complete
7. [DIRECTOR → Valeria (tp-designer)] Generar TP (si asignado)
   ↓ checkpoint: tp-complete
8. [QUALITY LOOP] quality loop final
   ↓
9. [DIRECTOR → Simulador] Simulación pedagógica (si S7.4 activo)
   ↓ checkpoint: simulation-complete
10. [DIRECTOR] Resumen final → docente decide si publicar
```

**Schema `director-state.schema.json`:**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "EDU Director State",
  "type": "object",
  "required": ["topic_id", "course_id", "current_step", "status"],
  "properties": {
    "topic_id": { "type": "string" },
    "course_id": { "type": "string" },
    "current_step": {
      "enum": ["init", "design", "design-review", "content", "quality-check",
               "pipeline", "tp", "simulation", "final-review", "complete", "error"]
    },
    "status": { "enum": ["running", "waiting-human", "paused", "complete", "error"] },
    "checkpoints": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "timestamp": { "type": "string", "format": "date-time" },
          "artifacts": { "type": "array", "items": { "type": "string" } },
          "validation_passed": { "type": "boolean" }
        }
      }
    },
    "errors": { "type": "array", "items": { "type": "string" } },
    "started_at": { "type": "string", "format": "date-time" },
    "completed_at": { "type": "string", "format": "date-time" }
  }
}
```

**Ventajas sobre OpenMAIC:**
1. **Gates obligatorios**: El Director NO puede saltear quality loops (en OpenMAIC no hay validación)
2. **Human-in-the-loop**: El docente aprueba diseño antes de generar contenido (en OpenMAIC es 100% automático)
3. **Checkpoints persistentes**: Si la sesión se interrumpe, `/edu-resume-topic` retoma desde el último checkpoint
4. **Memory-aware**: El Director consulta `memory.db` para errores previos del mismo tema/tipo
5. **Schema-validated**: Cada artefacto se valida contra su schema correspondiente

**Criterios de aceptación:**
- [ ] `/edu-auto-topic --topic 05-sorting --course leng-2026` ejecuta el flujo completo
- [ ] El flujo se detiene en gate de diseño esperando aprobación humana
- [ ] Si se interrumpe la sesión, `/edu-resume-topic` retoma con estado preservado
- [ ] TODOS los quality loops existentes se respetan (no se saltean)
- [ ] Los agentes existentes (Marcos, Roberto, Valeria, Simulador) NO se modifican — el Director los invoca tal cual
- [ ] Registro completo en `memory.db`: categoría `director-run`, con duración, steps, errores

---

### Entregables Sprint 8

| Archivo | Estado |
|---------|--------|
| `_edu/schemas/pbl-project.schema.json` | NUEVO |
| `_edu/agents/pbl-designer.md` | NUEVO |
| `.github/agents/edu-agent-pbl-designer.md` | NUEVO |
| `_edu/workflows/create-pbl/workflow.md` | NUEVO |
| `_edu/templates/pbl-rubric-template.md` | NUEVO |
| `.github/prompts/edu-create-pbl.prompt.md` | NUEVO |
| `.github/prompts/edu-pbl-status.prompt.md` | NUEVO |
| `_edu/agents/topic-director.md` | NUEVO |
| `.github/agents/edu-agent-topic-director.md` | NUEVO |
| `_edu/workflows/auto-topic/workflow.md` | NUEVO |
| `_edu/schemas/director-state.schema.json` | NUEVO |
| `.github/prompts/edu-auto-topic.prompt.md` | NUEVO |
| `.github/prompts/edu-resume-topic.prompt.md` | NUEVO |
| `_edu/config.yaml` | EXTEND — bloques PBL + Director |
| `_edu/module-help.csv` | EXTEND — 4 filas |
| `WORKFLOW_PROMPT_MAP.md` | EXTEND — 4 filas |
| `README.md` | EXTEND — secciones PBL + Director Agent |

**NO tocar:** topic-designer.md, class-writer.md, tp-designer.md, student-simulator.md, quality-loops/*, topic-cycle/*, schema-registry.json

---

## Registro de Impacto — Archivos Existentes (v2)

| Archivo | Sprints | Cambio |
|---------|---------|--------|
| `_edu/config.yaml` | S1, S3, S4, S7, S8 | Bloques de config nuevos al final |
| `_edu/module-help.csv` | S1-S8 | Filas nuevas al final |
| `WORKFLOW_PROMPT_MAP.md` | S1-S8 | Filas nuevas al final |
| `README.md` | S1-S8 | Secciones nuevas al final |
| `.gitignore` | S5 | 1 línea nueva |
| `scripts/requirements.txt` | S7 | `edge-tts>=6.1.0` (condicional) |

**Total archivos existentes afectados: 6** (de ~80+ en el módulo)  
**Archivos NUNCA tocados:** agents existentes, workflows existentes, schemas/schema-registry.json, scripts existentes, tests

---

## Grafo de Dependencias

```
S1 (validadores) ──────┐
S2 (herramientas) ─────┤── S1-S4 parallelizables (0 dependencias)
S3 (GitHub) ───────────┤                    ┌── S7 requiere S1 + S4
S4 (cognitivo) ────────┘                    │
       │                                    │
       ▼                                    ▼
S5 (analytics) ──── independiente     S7 (interactividad) ── S7.1 + S7.2 + S7.3 + S7.4
       │                                    │
       ▼                                    │
S6 (investigación) ← requiere S1-S5        │
       │                                    │
       └────────────┬───────────────────────┘
                    ▼
              S8 (orquestación) ← requiere S3, S5, S7
                    │
                    ├── S8.1 (PBL) ← S3 + S5 + S7.4
                    └── S8.2 (Director) ← todos
```

---

## Orden de Ejecución Recomendado

### Fase 1 — Fundamentos (S1 + S2, paralelos)
```
S1.1 (accesibilidad) ─┐
S1.2 (composición)  ──┤── todos paralelizables
S2.1 (spaced rep)   ──┤
S2.2 (exam)         ──┘
```

### Fase 2 — Integración (S3 + S4, paralelos)
```
S3.1 (classroom) ──── S3.2 (auto-responder)
S4.1 (layout) ────── S4.2 (cognitive)
```

### Fase 3 — Analytics (S5)
```
S5.1 (analytics) ──── S5.2 (adaptive) ← S5.2 depende de S5.1
```

### Fase 4 — Interactividad (S7, paralelo con S6)
```
S7.1 (interactive HTML) ──┐
S7.2 (whiteboard)      ───┤── paralelizables entre sí
S7.3 (TTS)             ───┤
S7.4 (classmate sim)   ───┘
S6.1 (comparator) ── en paralelo ── S6.2 (MCP)
```

### Fase 5 — Orquestación (S8)
```
S8.1 (PBL) ────── S8.2 (Director) ← el Director es lo último
```

---

## Total de archivos nuevos por sprint

| Sprint | Scripts | Schemas | Agentes | Prompts | Templates/Workflows | Total |
|--------|---------|---------|---------|---------|---------------------|-------|
| S1 | 2 | 0 | 0 | 2 | 0 | **4** |
| S2 | 2 | 1 | 0 | 2 | 0 | **5** |
| S3 | 1 | 0 | 0 | 3 | 3 | **7** |
| S4 | 2 | 1 | 0 | 2 | 0 | **5** |
| S5 | 2 | 0 | 0 | 2 | 0 | **4** |
| S6 | 1 | 0 | 1 | 1 | 3 | **6** |
| S7 | 2 | 2 | 1 | 4 | 3 | **12** |
| S8 | 0 | 2 | 2 | 4 | 3 | **11** |
| **Total** | **12** | **6** | **4** | **20** | **12** | **54** |
