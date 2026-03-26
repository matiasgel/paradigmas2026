# Sprints de Mejoras v2 — EDU Module (28 propuestas)

**Fecha:** 2026-03-26 | **Actualizado:** 2026-03-26 (Beyond-LLM + Multi-Model Frontier + Zero-Curriculum Vision)  
**Supersede:** `sprints-mejoras-edu-v1.md` (12 propuestas, 6 sprints)  
**Cambios v1→v2:** Integra 6 propuestas OpenMAIC (#13-#18) → 8 sprints.  
**Cambios v2 (this):** Agrega 9 propuestas Beyond-LLM + Frontier (#19-27) → **12 sprints**. Propuesta #16 actualizada a Multi-Model Multi-Agent Orchestration. Nueva propuesta #27 (Open-Source Orchestrator).  
**Cambios v2.1:** Agrega propuesta #28 Zero-Curriculum Adaptive Learning → **S13** (sprint final). KST + Universal CS KG + aprendizaje adaptativo sin currícula fija. Supera a ALEKS en dominio, idioma y generación de contenido.

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
| **16** | **Multi-Model Multi-Agent Orchestration** | **S8** | **OpenMAIC + Frontier** | 🔴 Alta |
| **19** | **Knowledge Graph Engine (Ontología)** | **S11** | **Beyond-LLM** | 🔴 Alta |
| **20** | **NLI Fact Verifier (DeBERTa)** | **S9** | **Beyond-LLM** | 🔴 Alta |
| **21** | **BERTopic Curriculum Analyzer** | **S9** | **Beyond-LLM** | 🔴 Alta |
| **22** | **Concept Prerequisite Learning (CPL)** | **S11** | **Beyond-LLM** | 🔴 Alta |
| **23** | **IRT + BKT Assessment Calibrator** | **S10** | **Beyond-LLM** | 🔴 Alta |
| **24** | **CLIP + LayoutLM Slide Quality** | **S10** | **Beyond-LLM** | 🟡 Media |
| **25** | **Semantic Drift Detector** | **S9** | **Beyond-LLM** | 🔴 Alta |
| **26** | **Neuro-Symbolic Bloom Classifier** | **S10** | **Beyond-LLM** | 🟡 Media |
| **27** | **Open-Source Orchestrator + GitHub** | **S12** | **Beyond-LLM + Frontier** | 🔴 Alta |
| **28** | **Zero-Curriculum Adaptive Learning** | **S13** | **Zero-Curriculum Vision** | 🔴 Alta |

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
| **S8** | Orquestación avanzada | #15, #16 | PBL multi-clase + Director Agent multi-modelo | Alto | S3, S5, S7 |
| **S9** | Analizadores semánticos | #25, #21, #20 | Drift detector + BERTopic + NLI verifier | Medio | S1 |
| **S10** | Psicometría + calidad visual | #26, #23, #24 | Bloom ML + IRT/BKT + CLIP | Medio | S2, S7 |
| **S11** | Knowledge engineering | #19, #22 | Knowledge Graph (OWL) + CPL (GNN) | Alto | S9, S10 |
| **S12** | Full-stack orquestación | #27 | Open-source orchestrator + GitHub Actions | Alto | S8, S11 |
| **S13** | Zero-Curriculum Adaptativo | #28 | KST Engine + Universal CS KG + Adaptive Tutor | Muy Alto | S11, S12 |

**S1-S4 son paralelizables.** S5 es independiente. S6 requiere estabilización previa. S7 requiere S1 (WCAG para validar HTML) y S4 (reglas cognitivas). S8 requiere la mayoría de los anteriores. **S9 puede iniciarse en paralelo con S7-S8** (solo requiere S1). S10 requiere S2 (exam) y S7 (simulador para datos IRT). S11 requiere S9 (embeddings ya computados) y S10 (Bloom para el KG). S12 es el sprint final que integra todo.

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

## Sprint 9 — Analizadores Semánticos

**Objetivo:** Tres scripts de análisis semántico que validan la coherencia global del curso sin tocar el pipeline de slides. Orden de implementación recomendado: S9.1 (más simple) → S9.3 → S9.2.

**Dependencias:** S1 (embeddings de ChromaDB ya disponibles + model MiniLM ya instalado).

### S9.1 — Semantic Drift Detector (#25)

**Story:** Como docente, quiero detectar definiciones inconsistentes y saltos temáticos bruscos entre clases, para garantizar que el vocabulario del curso es coherente de principio a fin.

**KB consultar:** `python scripts/knowledge_base.py search "semantic coherence embedding drift curriculum" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/semantic_drift_detector.py` | Script | Comparación de embeddings inter-clase |
| `.github/prompts/edu-check-semantic-drift.prompt.md` | Prompt | `/edu-check-semantic-drift` |

**Qué hace `semantic_drift_detector.py`:**
- Reutiliza `sentence-transformers` (ya instalado para ChromaDB, modelo `all-MiniLM-L6-v2`)
- Extrae definiciones explícitas de cada minuta/filmina: patrones "X se define como", "X es un/una", "X significa"
- Para cada concepto con múltiples definiciones en distintas clases: calcula cosine similarity entre embeddings
  - < 0.70 → inconsistencia semántica 🔴 (el mismo término se explica de forma contradictoria)
  - 0.70-0.85 → complementaria ⚠️ (definición parcial en cada clase, posiblemente intencional)
  - > 0.85 → consistente ✅
- Coherencia narrativa inter-clase: embedding promedio de cada tema → curva de similitud secuencial
  - Caída < 0.30 entre temas consecutivos → salto temático abrupto
- Detección de "vocabulary drift": si el mismo concepto se llama "variable" en tema 2 e "identificador" en tema 8 sin redefinición, lo detecta via clustering de embeddings
- Genera `{course_output_folder}/coherence-analysis/consistency-report.md` + gráfico Mermaid

**Criterios de aceptación:**
- [ ] `python scripts/semantic_drift_detector.py --course leng-2026` genera reporte
- [ ] Sin minutas/filminas disponibles, sale con 0 y mensaje informativo
- [ ] Reutiliza modelo MiniLM ya instalado (no agrega dependencias nuevas)
- [ ] `test_pipeline.py` sigue pasando

---

### S9.2 — BERTopic Curriculum Analyzer (#21)

**Story:** Como docente, quiero detectar automáticamente gaps curriculares (temas del plan no cubiertos) y redundancias (temas repetidos en exceso), comparando el plan mínimo contra los artefactos producidos.

**KB consultar:** `python scripts/knowledge_base.py search "topic modeling curriculum gaps coverage BERTopic" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/curriculum_topic_analyzer.py` | Script | BERTopic sobre corpus de artefactos del curso |
| `.github/prompts/edu-check-curriculum-gaps.prompt.md` | Prompt | `/edu-check-curriculum-gaps` |

**Qué hace `curriculum_topic_analyzer.py`:**
- Corpus: `plan-minimo.md` + todos los `diseno.md` + `minuta.md` + filminas del curso
- `BERTopic` con guided topics extraídos del `plan-minimo.md` (semi-supervised)
- Por cada tópico del plan: verifica presencia en ≥1 diseño + ≥1 minuta + ≥1 filmina
  - Ausencia en todos → **GAP** 🔴
  - Ausencia en filminas pero presente en minuta → **GAP parcial** 🟡
- Tópicos en filminas que no están en el plan → **DRIFT** 🟡 (el docente agregó contenido no oficial)
- Tópicos en >3 temas distintos → **REDUNDANCIA** ⚠️
- Output: `{course_output_folder}/topic-analysis/gaps-report.md` + matriz de cobertura + visualización HTML interactiva

**Config nuevos (opcionales):**
```yaml
# --- Topic Analysis (Sprint 9) ---
topic_analysis_enabled: false
topic_gap_threshold: 0.3     # distancia mínima para considerar tópico cubierto
topic_redundancy_threshold: 3 # apariciones máximas antes de flaggear redundancia
```

**Dependencias Python:** `bertopic`, `umap-learn`, `hdbscan` (nuevas)

**Criterios de aceptación:**
- [ ] `python scripts/curriculum_topic_analyzer.py --course leng-2026` genera reporte + HTML
- [ ] Sin `topic_analysis_enabled: true`, imprime aviso y sale con 0
- [ ] `test_pipeline.py` sigue pasando

---

### S9.3 — NLI Fact Verifier (#20)

**Story:** Como docente, quiero verificar automáticamente que el contenido generado por la IA no contiene alucinaciones factuales, usando un modelo de inferencia de lenguaje natural que compare cada afirmación contra las fuentes primarias del curso.

**KB consultar:** `python scripts/knowledge_base.py search "NLI fact verification hallucination DeBERTa entailment" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/fact_verifier.py` | Script | Pipeline NLI: claims → evidencia → veredicto |
| `.github/prompts/edu-verify-facts.prompt.md` | Prompt | `/edu-verify-facts` |

**Qué hace `fact_verifier.py`:**
- **Fase 1:** LLM descompone el texto (minuta/filmina) en claims atómicos: oraciones con una sola afirmación verificable
- **Fase 2:** Por cada claim, retrieval de evidencia: ChromaDB (top-3) + `plan-minimo.md` + KB semántica
- **Fase 3:** NLI scoring con `cross-encoder/nli-deberta-v3-large` (HuggingFace, ~355M params, ~500ms/par en CPU):
  - ENTAILMENT → ✅ Verificado
  - CONTRADICTION → ❌ Refutado → flag obligatorio al docente
  - NEUTRAL → ⚠️ Evidencia insuficiente
- **Gate de calidad:** ningún claim con veredicto ❌ puede pasar al pipeline de publicación sin aprobación humana explicita
- Output: `{topic_folder}/fact-check-report.md` con tabla veredictos + confianza

**Dependencias Python:** `sentence-transformers` (ya instalado) — solo agregar el modelo cross-encoder al primer uso

**Criterios de aceptación:**
- [ ] `python scripts/fact_verifier.py --topic 05-sorting --course leng-2026` genera reporte
- [ ] Claims con veredicto ❌ generan salida de proceso con código 1 (error) para bloquear pipelines CI
- [ ] Sin texto de entrada, sale con 0
- [ ] `test_pipeline.py` sigue pasando

---

### Entregables Sprint 9

| Archivo | Estado |
|---------|--------|
| `scripts/semantic_drift_detector.py` | NUEVO |
| `scripts/curriculum_topic_analyzer.py` | NUEVO |
| `scripts/fact_verifier.py` | NUEVO |
| `.github/prompts/edu-check-semantic-drift.prompt.md` | NUEVO |
| `.github/prompts/edu-check-curriculum-gaps.prompt.md` | NUEVO |
| `.github/prompts/edu-verify-facts.prompt.md` | NUEVO |
| `_edu/config.yaml` | EXTEND — bloque `# --- Topic Analysis (S9) ---` |
| `_edu/module-help.csv` | EXTEND — 3 filas |
| `WORKFLOW_PROMPT_MAP.md` | EXTEND — 3 filas |
| `README.md` | EXTEND — sección "Analizadores Semánticos" |

**NO tocar:** coherencia-validator, guardrail, ChromaDB, schema-registry.json

---

## Sprint 10 — Psicometría + Calidad Visual

**Objetivo:** Tres herramientas que mejoran la calidad de las evaluaciones (IRT/BKT, Bloom ML) y de las slides visuales (CLIP). Independientes entre sí — pueden implementarse en paralelo.

**Dependencias:** S2 (exam blueprint, para datos de respuesta IRT), S7 (thumbnails generados, para CLIP).

### S10.1 — Neuro-Symbolic Bloom Classifier (#26)

**Story:** Como docente, quiero clasificar automáticamente cada pregunta de TP/examen por nivel de Bloom con mayor precisión que el LLM, usando un clasificador ML fine-tuned específicamente en taxonomía de Bloom.

**KB consultar:** `python scripts/knowledge_base.py search "Bloom taxonomy classification DeBERTa fine-tuning education" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/bloom_classifier.py` | Script | Clasificador DeBERTa fine-tuned para Bloom |
| `scripts/train_bloom_model.py` | Script | One-time: fine-tuning del modelo (Colab-friendly) |
| `.github/prompts/edu-classify-bloom.prompt.md` | Prompt | `/edu-classify-bloom` |

**Qué hace `bloom_classifier.py`:**
- Modelo: `microsoft/deberta-v3-base` fine-tuned en datasets de Bloom (Yusof 2024: 12k ítems, Mohammed 2020: 5k ítems)
- Clasifica cada pregunta en 6 niveles: Recordar / Comprender / Aplicar / Analizar / Evaluar / Crear
- Accuracy esperada: 82-86% (vs. 65-72% del LLM zero-shot según benchmarks)
- Cross-validation LLM ↔ ML: si hay discrepancia, flag para revisión humana
- Extiende la salida de `exam-blueprint` con columnas `bloom_ml` + `bloom_confidence` + `bloom_agree`

**`train_bloom_model.py`** — script auxiliar para que el docente entrene el modelo en Google Colab T4 gratuito (~2 horas). Se ejecuta una vez y el modelo queda en `_edu-knowledge/models/bloom-classifier/`. No es parte del pipeline regular.

**Criterios de aceptación:**
- [ ] `python scripts/bloom_classifier.py --course leng-2026 --exam parcial-1` genera tabla de clasificación
- [ ] Sin modelo fine-tuned disponible, usa LLM como fallback con aviso
- [ ] La tabla de clasificación es compatible con `exam-blueprint` existente
- [ ] `test_pipeline.py` sigue pasando

---

### S10.2 — IRT + BKT Assessment Calibrator (#23)

**Story:** Como docente, quiero calibrar la dificultad real de mis preguntas de examen usando psicometría formal (IRT) y estimar el conocimiento de cada alumno con Bayesian Knowledge Tracing.

**KB consultar:** `python scripts/knowledge_base.py search "IRT item response theory psychometrics assessment calibration" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/assessment_calibrator.py` | Script | IRT 2PL + BKT por concepto |
| `.github/prompts/edu-calibrate-assessment.prompt.md` | Prompt | `/edu-calibrate-assessment` |

**Qué hace `assessment_calibrator.py`:**
- **IRT 2PL** (librería `py-irt`): lee matriz alumno × respuesta (CSV de Moodle o GitHub Classroom)
  - Por ítem: dificultad (b: −3 a +3), discriminación (a: >0.5 = bueno), guessing implícito
  - Items con discriminación < 0.2: flag para revisión/reescritura
  - Items con dificultad > 2.5 o < −2.5: posiblemente triviales/imposibles
- **BKT** (implementación Python puro, sin deps extra): estima `P(alumno sabe concepto)` a partir de secuencia de respuestas por concepto
  - Umbrales: `P(mastery) > 0.95` = concepto dominado; `< 0.50` = requiere repaso urgente
  - Se integra con Spaced Repetition Engine (S2.1) para priorizar repasos automáticamente
- Output: `{course_output_folder}/assessment-calibration/`:
  - `irt-report.md` — parámetros por ítem + flags de revisión
  - `bkt-mastery.md` — mapa de dominio conceptual por alumno (anonimizado)
  - `items-to-revise.md` — lista de preguntas problemáticas con recomendaciones

**Dependencias Python:** `py-irt` (nueva — `pip install py-irt`)

**Criterios de aceptación:**
- [ ] `python scripts/assessment_calibrator.py --course leng-2026 --gradebook parcial-1.csv` genera reportes
- [ ] Sin datos de respuesta, genera template CSV de ejemplo y sale con 0
- [ ] EL BKT se alimenta de los mismos concepts del knowledge graph (S11) si está disponible
- [ ] `test_pipeline.py` sigue pasando

---

### S10.3 — CLIP + LayoutLM Slide Quality (#24)

**Story:** Como docente, quiero evaluar si las imágenes de mis slides son visualmente relevantes al contenido y si el layout transmite hierarquía correcta, usando modelos de visión en lugar de solo análisis de texto.

**KB consultar:** `python scripts/knowledge_base.py search "CLIP visual quality slide assessment multimodal layout" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/slide_quality_vision.py` | Script | CLIP score + layout metrics |
| `.github/prompts/edu-check-visual-quality.prompt.md` | Prompt | `/edu-check-visual-quality` |

**Qué hace `slide_quality_vision.py`:**
- **CLIP score (OpenCLIP ViT-B/32, 400MB, CPU-friendly)**:
  - Relevancia imagen-texto por filmina: cosine_similarity(CLIP(thumbnail), CLIP(title + body))
  - Umbral: < 0.15 = imagen irrelevante ❌, 0.15-0.25 = marginal ⚠️, > 0.25 = relevante ✅
  - Coherencia visual inter-slide: CLIP similarity entre thumbnails consecutivos; caída brusca = posible slide fuera de contexto
  - Detector de clipart genérico: CLIP score vs. prompt negativo "generic decorative stock photo"
- **Layout quality** (basado en coordenadas EMU de `plan-filminas.json`, sin inferencia adicional):
  - Balance horizontal: distribución de masa visual izquierda vs. derecha (ideal ±20%)
  - Alineación a grilla: % de elementos en posiciones redondeadas
  - Whitespace ratio: área libre / área total (ideal 40-60%, < 30% = sobredensidad ❌)
  - Regla de tercios: % de elementos cerca de las intersecciones
- Integración con `capture_thumbnails.py` (ya existente): procesa thumbnails generados automáticamente
- Output: `{topic_folder}/visual-quality-report.md` con tabla CLIP score + layout grade (A/B/C/F) por filmina

**Dependencias Python:** `open-clip-torch` (nueva — `pip install open-clip-torch`)

**Criterios de aceptación:**
- [ ] `python scripts/slide_quality_vision.py --topic 05-sorting --course leng-2026` genera reporte
- [ ] Requiere thumbnails existentes (generados por `capture_thumbnails.py`); si no existen, informa y sale con 0
- [ ] Primer uso: descarga modelo OpenCLIP ViT-B/32 a `_edu-knowledge/models/` (~400MB)
- [ ] `test_pipeline.py` sigue pasando

---

### Entregables Sprint 10

| Archivo | Estado |
|---------|--------|
| `scripts/bloom_classifier.py` | NUEVO |
| `scripts/train_bloom_model.py` | NUEVO |
| `scripts/assessment_calibrator.py` | NUEVO |
| `scripts/slide_quality_vision.py` | NUEVO |
| `.github/prompts/edu-classify-bloom.prompt.md` | NUEVO |
| `.github/prompts/edu-calibrate-assessment.prompt.md` | NUEVO |
| `.github/prompts/edu-check-visual-quality.prompt.md` | NUEVO |
| `_edu/module-help.csv` | EXTEND — 3 filas |
| `WORKFLOW_PROMPT_MAP.md` | EXTEND — 3 filas |
| `README.md` | EXTEND — sección "Psicometría + Calidad Visual" |

**NO tocar:** exam-blueprint (S2.2), tp-designer, schema-registry.json

---

## Sprint 11 — Knowledge Engineering

**Objetivo:** Los dos proyectos más complejos del roadmap. Se recomienda iniciar #19 primero (Knowledge Graph como base) y #22 después (CPL usa el KG como input).

**Dependencias:** S9 (embeddings computados, ChromaDB maduro), S10 (Bloom classifier para enriquecer el KG con niveles cognitivos), S6 (Wikidata MCP server, si implementado).

### S11.1 — Knowledge Graph Engine — Ontología Educativa Formal (#19)

**Story:** Como docente, quiero una representación formal de relaciones entre conceptos de mi materia (prerequisito-de, parte-de, contradice-a), validable con queries SPARQL, para garantizar que el orden de enseñanza es lógicamente coherente.

**KB consultar:** `python scripts/knowledge_base.py search "knowledge graph OWL ontology educational prerequisite SPARQL" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/knowledge_graph.py` | Script | Builder + validador del KG educativo |
| `_edu/knowledge/edu-ontology.ttl` | Ontología | OWL Lite en Turtle con clases EDU |
| `_edu/schemas/knowledge-graph.schema.json` | Schema | JSON-LD output format |
| `.github/prompts/edu-build-kg.prompt.md` | Prompt | `/edu-build-kg` |
| `.github/prompts/edu-validate-kg.prompt.md` | Prompt | `/edu-validate-kg` |

**Qué hace:**

1. **Ontología OWL Lite** (`edu-ontology.ttl`): Define clases y propiedades base:
   - Clases: `:Concepto`, `:Tema`, `:NivelBloom`, `:Competencia`
   - Propiedades: `:tienePrerequisito` (transitiva), `:perteneceA`, `:nivelCognitivo`, `:contradice` (simétrica), `:ejemplificadoPor`

2. **Poblado automático (LLM + validación ConceptNet/Wikidata)**:
   - LLM extrae pares (concepto, relación, concepto) de `plan-minimo.md` y `diseno.md`
   - Cada relación se verifica contra ConceptNet API o Wikidata SPARQL endpoint
   - Confianza alta (>0.8): acepta automáticamente. Confianza media: flag para docente.

3. **Validaciones formales (SPARQL queries)**:
   - Prerequisitos faltantes: "¿Todo concepto tiene sus prerequisitos enseñados antes?"
   - Ciclos: "¿Hay A→B→A en el grafo de prerequisitos?" (ciclo = error curricular)
   - Huérfanos: "¿Hay conceptos en filminas que no están en el grafo?"
   - Bloom monotónico: "¿Los niveles cognitivos crecen a lo largo del curso?"

4. **Output**: `{course_output_folder}/knowledge-graph.json` (JSON-LD) + visualización Mermaid

5. **Librerías**: `rdflib` + `owlready2` + `networkx` + `SPARQLWrapper`

**Criterios de aceptación:**
- [ ] `python scripts/knowledge_graph.py --course leng-2026 build` genera KG JSON-LD
- [ ] `python scripts/knowledge_graph.py --course leng-2026 validate` ejecuta queries SPARQL y reporta ciclos/huérfanos
- [ ] Detecta correctamente un ciclo sintético inyectado en tests
- [ ] Si Wikidata no está disponible, construye el KG sin validación externa (modo offline)
- [ ] `test_pipeline.py` sigue pasando

---

### S11.2 — Concept Prerequisite Learning — CPL con ML (#22)

**Story:** Como docente, quiero que el sistema aprenda automáticamente qué concepto es prerequisito de cuál, usando ML sobre corpus de libros de texto y datasets públicos de CS, reduciendo la carga de anotación manual al mínimo.

**KB consultar:** `python scripts/knowledge_base.py search "prerequisite learning concept dependency graph neural network active learning" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/prerequisite_learner.py` | Script | Classifier + active learning para prerequisitos |
| `scripts/train_prerequisite_model.py` | Script | One-time: entrenamiento con LectureBank dataset |
| `.github/prompts/edu-learn-prerequisites.prompt.md` | Prompt | `/edu-learn-prerequisites` |

**Qué hace `prerequisite_learner.py`:**
- **Features por par de conceptos (A, B):**
  - `semantic_similarity`: cosine(embed(A), embed(B)) con MiniLM
  - `order_in_course`: índice_tema(A) − índice_tema(B)
  - `co_occurrence_jaccard`: Jaccard entre documentos que contienen A y B
  - `conceptnet_has_prereq`: flag si ConceptNet tiene relación `HasPrerequisite(A,B)`
  - `wikidata_path_length`: longitud del camino más corto en Wikidata
- **Classifier**: XGBoost o LightGBM (CPU-friendly, <100ms de inferencia)
- **Pre-entrenado** en LectureBank (Johns Hopkins, 1.5k pares anotados de CS) via `train_prerequisite_model.py`
- **Active learning**: presenta al docente solo los pares más inciertos (top-30 pares con probabilidad más cercana a 0.5). Con ~30 anotaciones manuales, el modelo alcanza >90% del rendimiento del oráculo completo.
- **Output**: extiende `{course_output_folder}/knowledge-graph.json` con bordes inferidos por ML, con campo `source: "cpl-ml"` + `confidence`
- **Anomalías automáticas**: conceptos con muchos prerequisitos no cubiertos → flag ordenado por confianza

**Criterios de aceptación:**
- [ ] `python scripts/prerequisite_learner.py --course leng-2026 predict` genera sugerencias de prerequisitos
- [ ] `python scripts/prerequisite_learner.py --course leng-2026 annotate` inicia sesión de active learning (30 preguntas Y/N)
- [ ] Detecta ciclos en los prerequisitos sugeridos y los reporta antes de agregarlos al KG
- [ ] Sin modelo pre-entrenado, descarga LectureBank automáticamente y muestra instrucciones de entrenamiento
- [ ] `test_pipeline.py` sigue pasando

---

### Entregables Sprint 11

| Archivo | Estado |
|---------|--------|
| `scripts/knowledge_graph.py` | NUEVO |
| `scripts/prerequisite_learner.py` | NUEVO |
| `scripts/train_prerequisite_model.py` | NUEVO |
| `_edu/knowledge/edu-ontology.ttl` | NUEVO |
| `_edu/schemas/knowledge-graph.schema.json` | NUEVO |
| `.github/prompts/edu-build-kg.prompt.md` | NUEVO |
| `.github/prompts/edu-validate-kg.prompt.md` | NUEVO |
| `.github/prompts/edu-learn-prerequisites.prompt.md` | NUEVO |
| `_edu/module-help.csv` | EXTEND — 3 filas |
| `WORKFLOW_PROMPT_MAP.md` | EXTEND — 3 filas |
| `README.md` | EXTEND — sección "Knowledge Engineering" |

**NO tocar:** semantic_drift_detector.py, fact_verifier.py, coherencia-validator, schema-registry.json

---

## Sprint 12 — Full-Stack Orchestration (Open-Source Orchestrator)

**Objetivo:** Integrar todo el stack beyondLLM + Director Agent en un orquestador open-source que corre junto a Copilot, con deploy automático vía GitHub Actions. Este es el sprint más complejo y requiere que S8 (Director Agent), S9 (analizadores semánticos), S10 (psicometría) y S11 (KG) estén estables.

**Dependencias:** S8.2 (Director Agent base), S11 (Knowledge Graph como contexto del orquestador), S9.3 (NLI verifier como gate de calidad del orquestador).

### S12.1 — Python Director Script Minimalista (fase 2 de la propuesta #27)

**Story:** Como docente, quiero un script Python puro que orqueste todo el pipeline de producción de un tema con un solo comando, sin vendor lock-in, usando checkpoints persistentes.

**KB consultar:** `python scripts/knowledge_base.py search "orchestration pipeline automation subprocess checkpoint" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/edu_director.py` | Script | Orquestador Python puro — pipeline completo |
| `.github/prompts/edu-run-pipeline.prompt.md` | Prompt | `/edu-run-pipeline` |
| `.github/prompts/edu-resume-pipeline.prompt.md` | Prompt | `/edu-resume-pipeline` |

**Qué hace `edu_director.py`:**
```
/edu-run-pipeline --topic 05-sorting --course leng-2026

PIPELINE STEPS:
1. validate_plan         → validate_plan.py
2. fact_check            → fact_verifier.py (S9.3, si habilitado)
3. slides_pipeline       → slides_pipeline.py
4. capture_thumbnails    → capture_thumbnails.py
5. visual_quality        → slide_quality_vision.py (S10.3, si habilitado)
6. [HUMAN GATE]          → "Revisar output y presionar Enter..."
7. semantic_drift        → semantic_drift_detector.py (S9.1, si habilitado)
8. bloom_classify        → bloom_classifier.py (S10.1, si habilitado)
9. [FINAL GATE]          → "Publicar? [S/n]"
```
- Cada paso guarda checkpoint en `{topic_folder}/.pipeline-state.json`
- `/edu-resume-pipeline` retoma desde el último checkpoint completado
- Flag `--dry-run` para simular sin ejecutar
- Flag `--skip-gates` para CI/CD (GitHub Actions)
- Cada paso tiene timeout configurable (default: 300s)
- Log completo en `memory.db`: categoría `pipeline-run`

**Criterios de aceptación:**
- [ ] `python scripts/edu_director.py --topic 05-sorting --course leng-2026` ejecuta pipeline completo
- [ ] Interrupción a mitad → `edu_director.py --resume --topic 05-sorting` retoma desde el paso siguiente al último exitoso
- [ ] `--skip-gates` permite ejecución no interactiva (para GitHub Actions)
- [ ] Log en `memory.db` con duración, pasos, errores
- [ ] Pasos opcionales se omiten automáticamente si el script correspondiente no está disponible

---

### S12.2 — smolagents Director Agent (fase 3 de la propuesta #27)

**Story:** Como docente avanzado, quiero invocar un agente orquestador que use LLMs para decidir qué hacer en situaciones no previstas (pasos que fallan, contenido rechazado por el guardrail, feedback del docente), usando modelos open-source gratuitos vía HuggingFace Inference API.

**KB consultar:** `python scripts/knowledge_base.py search "multi-agent orchestration smolagents HuggingFace open-source model routing" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `scripts/edu_smolagent_director.py` | Script | Director con smolagents + modelo Qwen/Llama |
| `.github/prompts/edu-agent-director.prompt.md` | Prompt | `/edu-agent-director` |

**Qué hace `edu_smolagent_director.py`:**
- Director `CodeAgent` (smolagents) con acceso a tools:
  - `search_knowledge_base(query)` → ChromaDB
  - `validate_plan(topic, course)` → validate_plan.py
  - `run_slides_pipeline(topic, course)` → slides_pipeline.py
  - `check_facts(topic, course)` → fact_verifier.py
  - `check_bloom_coverage(topic, course)` → bloom_classifier.py
  - `query_knowledge_graph(sparql)` → knowledge_graph.py
- Sub-agentes gestionados como `ManagedAgent`:
  - `topic_designer` (genera diseño)
  - `academic_guardrail` (valida contenido)
- Modelo: `Qwen/Qwen2.5-72B-Instruct` vía HuggingFace Inference API (gratuito con token)
  - Fallback: `meta-llama/Llama-3.3-70B-Instruct`
- Human-in-the-loop gates implementados como `input()` en el CodeAgent (interrumpibles)
- Compatible con el Director Agent de S8.2 (lo extiende, no lo reemplaza)

**Config nuevos:**
```yaml
# --- Orchestrator (Sprint 12) ---
orchestrator_enabled: false
orchestrator_mode: "minimal"          # minimal | smolagents | crewai
orchestrator_model: "Qwen/Qwen2.5-72B-Instruct"
hf_inference_api: true                # usa HuggingFace Inference API gratuita
local_model_path: null                # alternativa: ruta a modelo Ollama local
```

**Dependencias Python:** `smolagents` (nueva — `pip install smolagents`)

**Criterios de aceptación:**
- [ ] `python scripts/edu_smolagent_director.py --topic 05-sorting --course leng-2026` genera topic completo
- [ ] Sin `HF_TOKEN` configurado, usa modo minimal (edu_director.py) automáticamente como fallback
- [ ] El flujo se detiene en gates humanos esperando aprobación
- [ ] Los tools EDU envueltos son los mismos scripts de S9-S11 — no duplicación
- [ ] `test_pipeline.py` sigue pasando

---

### S12.3 — GitHub Actions Integration (#27 — integración CI/CD)

**Story:** Como docente, quiero que el pipeline de generación se ejecute automáticamente cuando hago push de un `diseno.md` aprobado, sin intervención manual adicional.

**KB consultar:** `python scripts/knowledge_base.py search "GitHub Actions CI/CD automation pipeline education" --type reference`

**Archivos NUEVOS a crear:**

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `.github/workflows/edu-auto-pipeline.yml` | GitHub Actions | CI/CD de generación automática |
| `.github/workflows/edu-fact-check.yml` | GitHub Actions | Gate de verificación factual en PR |

**`edu-auto-pipeline.yml`:**
```yaml
name: EDU Auto-Pipeline
on:
  push:
    paths:
      - 'salida/cursadas/**/diseno.md'
      - 'salida/cursadas/**/topic.yaml'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -r salida/edu-standalone/requirements.txt
      - name: Extract topic from changed files
        run: |
          TOPIC=$(git diff --name-only HEAD~1 | grep diseno.md | cut -d'/' -f4)
          COURSE=$(git diff --name-only HEAD~1 | grep diseno.md | cut -d'/' -f3)
          echo "TOPIC=$TOPIC" >> $GITHUB_ENV
          echo "COURSE=$COURSE" >> $GITHUB_ENV
      - name: Run EDU pipeline (no-gates mode)
        run: |
          python scripts/edu_director.py \
            --topic $TOPIC --course $COURSE \
            --skip-gates --skip-steps visual_quality,semantic_drift
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
      - name: Commit generated artifacts
        run: |
          git config user.name "EDU Pipeline Bot"
          git config user.email "edu-bot@noreply.github.com"
          git add salida/cursadas/
          git diff --cached --quiet || git commit -m "edu-pipeline: auto-generated $TOPIC materials"
          git push
```

**`edu-fact-check.yml`:**
```yaml
name: EDU Fact Check on PR
on:
  pull_request:
    paths: ['salida/cursadas/**/minuta.md', 'salida/cursadas/**/*.pptx']

jobs:
  fact-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install sentence-transformers chromadb
      - name: Run NLI fact check
        run: |
          python scripts/fact_verifier.py --course $COURSE --topic $TOPIC
        # Exits with code 1 if any claim is CONTRADICTED → blocks merge
```

**Criterios de aceptación:**
- [ ] Push de `diseno.md` → GitHub Actions se activa → pipeline corre automáticamente
- [ ] Si `fact_verifier.py` detecta contradictions, la PR no puede mergearse
- [ ] El bot commitea solo si hay cambios reales (evita commits vacíos)
- [ ] Sin `HF_TOKEN` configurado, el pipeline corre en modo minimal (sin smolagents)

---

### Entregables Sprint 12

| Archivo | Estado |
|---------|--------|
| `scripts/edu_director.py` | NUEVO |
| `scripts/edu_smolagent_director.py` | NUEVO |
| `.github/workflows/edu-auto-pipeline.yml` | NUEVO |
| `.github/workflows/edu-fact-check.yml` | NUEVO |
| `.github/prompts/edu-run-pipeline.prompt.md` | NUEVO |
| `.github/prompts/edu-resume-pipeline.prompt.md` | NUEVO |
| `.github/prompts/edu-agent-director.prompt.md` | NUEVO |
| `_edu/config.yaml` | EXTEND — bloque `# --- Orchestrator (S12) ---` |
| `_edu/module-help.csv` | EXTEND — 3 filas |
| `WORKFLOW_PROMPT_MAP.md` | EXTEND — 3 filas |
| `README.md` | EXTEND — sección "Orquestación Full-Stack" |

**NO tocar:** edu_director (S8.2 topic-director.md), agents existentes, schema-registry.json

---

## Sprint 13 — Zero-Curriculum Adaptive Learning

**Propuesta:** #28 — Zero-Curriculum Adaptive Learning — Currícula Emergente desde Conocimiento Colectivo Universitario  
**Objetivo:** Construir un sistema de aprendizaje adaptativo que modela el estado de conocimiento de cada estudiante usando Knowledge Space Theory (KST) y genera contenido on-demand sobre los conceptos exactos que necesita, sin depender de una sílabo fijo.  
**Fundamento académico:** Falmagne & Doignon 1988→2023 (KST), ALOHA (Python KST), ACM/IEEE CC2023 (14 KAs, 52 KUs), Monroe & Mitra 2024 (AutoCurricula)  
**Riesgo:** Muy Alto (investigación aplicada, primero en combinarlo con LLM español + CS completo)  
**Dependencias:** S11.1 (Knowledge Graph OWL) + S11.2 (CPL prereqs) + S10.2 (BKT mastery) + S12.1 (Director Script)

### S13.1 — KST Engine (Propuesta #28 Fase B)

**Objetivo:** Construir el motor de Knowledge Space Theory sobre el Knowledge Graph del curso existente.

**Archivo:** `scripts/knowledge_space.py`

**Dependencias:** `pip install aloha` (en requirements.txt)

```python
# scripts/knowledge_space.py
"""
KST Engine — Knowledge Space Theory sobre el KG del curso.
Requiere: S11.1 (knowledge_graph.py), S10.2 (bkt_tracker.py)
"""
from aloha import KnowledgeSpace
from scripts.knowledge_graph import CourseKnowledgeGraph
from scripts.bkt_tracker import BKTTracker
import json

class KSTEngine:
    """Motor KST que integra el KG del curso con BKT mastery scores."""
    
    def __init__(self, kg_path: str = "_edu-knowledge/course-kg.json"):
        self.kg = CourseKnowledgeGraph.load(kg_path)
        self.ks = None  # KnowledgeSpace de ALOHA
        self._build_space()
    
    def _build_space(self):
        """Construye el KnowledgeSpace desde los prerequisitos del KG."""
        items = list(self.kg.get_concepts())
        prereqs = self.kg.get_prerequisite_pairs()  # [(A, B)] = A prereq de B
        self.ks = KnowledgeSpace(items=items, prerequisites=prereqs)
    
    def frontier(self, known_concepts: set) -> list[str]:
        """
        Devuelve los conceptos en la frontera de aprendizaje:
        conceptos que el estudiante AÚN NO conoce pero cuyos
        prerequisitos YA fueron dominados.
        """
        return [c for c in self.ks.frontier(known_concepts)]
    
    def next_concept(self, student_state: dict) -> str | None:
        """
        Dado el estado BKT del estudiante (mastery scores 0-1),
        devuelve el concepto frontera con mayor utilidad pedagógica.
        Prioriza conceptos con muchos descendientes (alto impacto).
        """
        known = {c for c, score in student_state.items() if score >= 0.75}
        candidates = self.frontier(known)
        if not candidates:
            return None
        # Ordenar por centralidad en el KG (más descendientes = mayor prioridad)
        scored = [(c, len(self.kg.descendants(c))) for c in candidates]
        return max(scored, key=lambda x: x[1])[0]
    
    def learning_path(self, target_concept: str, student_state: dict) -> list[str]:
        """
        Retorna el camino mínimo de aprendizaje desde el estado actual
        hasta poder aprender target_concept.
        """
        known = {c for c, score in student_state.items() if score >= 0.75}
        return self.ks.learning_path(target=target_concept, known=known)
```

**Archivos creados:**
- `scripts/knowledge_space.py` — KSTEngine con frontier(), next_concept(), learning_path()
- `.github/prompts/edu-kst-explain.prompt.md` — prompt para explicar el concepto frontera al estudiante

**Criterio de aceptación:**
- `KSTEngine("_edu-knowledge/course-kg.json").frontier({"algebra_lineal"})` → lista no vacía
- `next_concept({"algebra_lineal": 0.9, "vectores": 0.8})` → retorna un concepto CS válido
- Tests unitarios en `scripts/tests/test_kst_engine.py`

**NO tocar:** knowledge_graph.py (S11.1), bkt_tracker.py (S10.2), schema-registry.json

---

### S13.2 — Universal CS Knowledge Graph Builder (Propuesta #28 Fase C)

**Objetivo:** Construir un KG universal de Ciencias de la Computación desde fuentes abiertas (ACM/IEEE CC2023 + MIT OCW + Stanford syllabi), fusionado con el KG del curso existente.

**Archivo:** `scripts/universal_kg_builder.py`

**Dependencias:** `rdflib`, `requests`, `beautifulsoup4` (ya en requirements.txt desde S11)

```python
# scripts/universal_kg_builder.py
"""
Universal CS KG Builder.
Fuentes: ACM/IEEE CC2023 (14 KAs, 52 KUs) + MIT OCW sitemap + Stanford Explorecourses.
Requiere: S11.1 (knowledge_graph.py) para el formato base.
Output: _edu-knowledge/universal-kg.json
"""
import json
import requests
from scripts.knowledge_graph import CourseKnowledgeGraph
from scripts.cpl_learner import CPLLearner  # S11.2 — infiere prereqs cross-institucion

# ACM/IEEE CC2023 — 14 Knowledge Areas embebidas (no requieren scraping)
ACM_CC2023_KAS = {
    "AL": "Algorithms and Complexity",
    "AR": "Architecture and Organization",
    "CN": "Computational Science",
    "DS": "Discrete Structures",
    "GV": "Graphics and Visualization",
    "HCI": "Human-Computer Interaction",
    "IAS": "Information Assurance and Security",
    "IM": "Information Management",
    "IS": "Intelligent Systems",
    "NC": "Networking and Communication",
    "OS": "Operating Systems",
    "PBD": "Platform-Based Development",
    "PD": "Parallel and Distributed Computing",
    "PL": "Programming Languages",
    "SDF": "Software Development Fundamentals",
    "SE": "Software Engineering",
    "SF": "Systems Fundamentals",
    "SP": "Social Issues and Professional Practice",
}

class UniversalKGBuilder:
    """Construye y fusiona el KG universal de CS desde fuentes abiertas."""
    
    def __init__(self, output_path: str = "_edu-knowledge/universal-kg.json"):
        self.output_path = output_path
        self.kg = CourseKnowledgeGraph()
    
    def ingest_acm_cc2023(self):
        """Ingesta las 14 Knowledge Areas y 52 Knowledge Units de ACM/IEEE CC2023."""
        for ka_code, ka_name in ACM_CC2023_KAS.items():
            self.kg.add_concept(ka_code, label=ka_name, source="ACM/IEEE CC2023", layer="KA")
        # Prerequisitos inter-KA (basados en CC2023 §3)
        cc2023_prereqs = [
            ("DS", "AL"), ("DS", "PL"), ("SDF", "SE"), ("AR", "OS"),
            ("OS", "NC"), ("OS", "PD"), ("AL", "IS"), ("IM", "IS"),
        ]
        for prereq, target in cc2023_prereqs:
            self.kg.add_prerequisite(prereq, target, source="ACM/IEEE CC2023")
    
    def ingest_mit_ocw(self, max_courses: int = 50):
        """
        Ingesta títulos de cursos MIT OCW via sitemap público.
        Extrae conceptos CS y prerequisitos implícitos.
        """
        sitemap_url = "https://ocw.mit.edu/sitemap.xml"
        try:
            resp = requests.get(sitemap_url, timeout=10)
            # Parsea solo cursos de CS (6.xxx)
            cs_courses = [url for url in resp.text.split("<loc>") 
                         if "/courses/6-" in url][:max_courses]
            for course_url in cs_courses:
                url = course_url.split("</loc>")[0].strip()
                self.kg.add_concept(url.split("/")[-2], 
                                   label=url.split("/")[-2].replace("-", " "),
                                   source="MIT OCW", layer="course")
        except requests.RequestException:
            pass  # Falla silenciosamente — red no disponible en CI
    
    def apply_cpl_inference(self):
        """
        Usa el modelo CPL (S11.2) para inferir prerequisitos no explícitos
        entre cursos de distintas instituciones.
        """
        cpl = CPLLearner.load("_edu-knowledge/cpl-model.pkl")
        new_prereqs = cpl.infer_cross_institution_prerequisites(self.kg)
        for prereq, target, confidence in new_prereqs:
            if confidence > 0.7:
                self.kg.add_prerequisite(prereq, target, 
                                        source="CPL-inferred",
                                        confidence=confidence)
    
    def build(self) -> str:
        """Construye y guarda el KG universal."""
        self.ingest_acm_cc2023()
        self.ingest_mit_ocw()
        self.apply_cpl_inference()
        self.kg.save(self.output_path)
        return self.output_path
```

**Archivos creados:**
- `scripts/universal_kg_builder.py` — UniversalKGBuilder con ACM CC2023 + MIT OCW + CPL inference
- `_edu-knowledge/universal-kg.json` — artefacto generado (en .gitignore si >50MB)
- `.github/prompts/edu-universal-kg.prompt.md` — prompt para explorar el KG universal

**Criterio de aceptación:**
- `UniversalKGBuilder().build()` → genera `_edu-knowledge/universal-kg.json` sin errores
- KG contiene los 18 Knowledge Areas de ACM/IEEE CC2023
- CPL infiere al menos 10 prerequisitos cross-institution con confidence > 0.7
- Tests en `scripts/tests/test_universal_kg.py`

**NO tocar:** knowledge_graph.py (S11.1), cpl_learner.py (S11.2), schema-registry.json

---

### S13.3 — Adaptive Tutor Interface (Propuesta #28 Fase D)

**Objetivo:** Interfaz de aprendizaje adaptativo que integra KSTEngine + BKT + Director Agent para recomendar el siguiente concepto y generar contenido on-demand.

**Archivo:** `scripts/adaptive_tutor.py` + opcional `app_adaptive.py` (Streamlit)

```python
# scripts/adaptive_tutor.py
"""
Adaptive Tutor — integra KST + BKT + Director Agent para aprendizaje sin currícula fija.
Requiere: S13.1 (KSTEngine), S10.2 (BKTTracker), S12.1 (edu_director)
"""
import os
from openai import OpenAI
from scripts.knowledge_space import KSTEngine
from scripts.bkt_tracker import BKTTracker
from scripts.edu_director import EduDirector

# Cliente GitHub Models (Claude Sonnet vía GITHUB_TOKEN)
_client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

class AdaptiveTutor:
    """
    Tutor adaptativo sin currícula fija.
    Estado del estudiante → concepto frontera KST → contenido on-demand.
    """
    
    def __init__(self, student_id: str, 
                 kg_path: str = "_edu-knowledge/universal-kg.json"):
        self.student_id = student_id
        self.kst = KSTEngine(kg_path)
        self.bkt = BKTTracker(student_id)
        self.director = EduDirector()
    
    def get_student_state(self) -> dict:
        """Retorna el estado de mastery del estudiante (concepto → P(mastery) 0-1)."""
        return self.bkt.get_all_mastery()
    
    def recommend_next(self) -> dict:
        """
        Recomienda el siguiente concepto a aprender usando KST frontier.
        Retorna: {concept, explanation, prerequisites_met, learning_path}
        """
        state = self.get_student_state()
        next_concept = self.kst.next_concept(state)
        if not next_concept:
            return {"concept": None, "message": "¡Felicitaciones! Dominaste todos los conceptos."}
        
        path = self.kst.learning_path(next_concept, state)
        return {
            "concept": next_concept,
            "prerequisites_met": [c for c in path if state.get(c, 0) >= 0.75],
            "learning_path": path,
            "why": f"Es el siguiente concepto con mayor impacto: desbloquea {len(self.kst.kg.descendants(next_concept))} conceptos futuros."
        }
    
    def generate_content(self, concept: str, content_type: str = "slides") -> dict:
        """
        Genera contenido on-demand para el concepto dado usando el Director Agent.
        content_type: "slides" | "exercise" | "explanation" | "quiz"
        """
        state = self.get_student_state()
        known_concepts = [c for c, s in state.items() if s >= 0.75]
        
        # Generar via Director Agent (S12.1) que usa GitHub Models internamente
        result = self.director.generate(
            topic=concept,
            student_known=known_concepts,
            content_type=content_type,
        )
        return result
    
    def update_after_assessment(self, concept: str, correct: bool):
        """Actualiza el estado BKT del estudiante después de una evaluación."""
        self.bkt.update(concept=concept, correct=correct)
    
    def session_summary(self) -> str:
        """Genera un resumen de la sesión de aprendizaje."""
        state = self.get_student_state()
        mastered = [c for c, s in state.items() if s >= 0.75]
        frontier = self.kst.frontier(set(mastered))
        
        prompt = f"""Estudiante {self.student_id}.
Conceptos dominados ({len(mastered)}): {', '.join(mastered[:10])}...
Conceptos en frontera ({len(frontier)}): {', '.join(frontier[:5])}
Genera un resumen motivacional en español de 3 oraciones sobre el progreso."""
        
        response = _client.chat.completions.create(
            model="claude-4-5",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
        )
        return response.choices[0].message.content
```

**Archivo opcional — Streamlit UI:**

```python
# app_adaptive.py  (ejecutar con: streamlit run app_adaptive.py)
import streamlit as st
from scripts.adaptive_tutor import AdaptiveTutor

st.title("🎓 EDU — Aprendizaje Adaptativo")
st.caption("Sin currícula fija · Impulsado por Knowledge Space Theory + BKT + LLM")

student_id = st.text_input("ID del estudiante:", value="estudiante_01")
tutor = AdaptiveTutor(student_id)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Estado actual")
    state = tutor.get_student_state()
    mastered = [c for c, s in state.items() if s >= 0.75]
    st.metric("Conceptos dominados", len(mastered))
    st.metric("Conceptos en exploración", len(state) - len(mastered))

with col2:
    st.subheader("Próximo paso")
    recommendation = tutor.recommend_next()
    if recommendation.get("concept"):
        st.success(f"**{recommendation['concept']}**")
        st.caption(recommendation.get("why", ""))
        if st.button("Generar contenido"):
            with st.spinner("Generando slides on-demand..."):
                content = tutor.generate_content(recommendation["concept"])
                st.json(content)
    else:
        st.balloons()
        st.success(recommendation.get("message", "Completado"))
```

**Archivos creados:**
- `scripts/adaptive_tutor.py` — AdaptiveTutor con KST + BKT + Director + GitHub Models
- `app_adaptive.py` — UI Streamlit opcional (fuera del pipeline principal)
- `.github/prompts/edu-adaptive-session.prompt.md` — prompt para sesión adaptativa
- `_edu/workflows/adaptive-learning.yaml` — workflow de aprendizaje adaptativo

**Criterio de aceptación:**
- `AdaptiveTutor("test_student").recommend_next()` → retorna dict con `concept` válido
- `generate_content("algoritmos_sorting")` → llama al Director Agent sin errores
- `update_after_assessment("algoritmos_sorting", correct=True)` → actualiza BKT
- `session_summary()` → genera texto en español vía GitHub Models (Claude Sonnet)
- Tests mockean `GITHUB_TOKEN` y `EduDirector` en `scripts/tests/test_adaptive_tutor.py`

**NO tocar:** edu_director.py (S12.1), bkt_tracker.py (S10.2), knowledge_space.py (S13.1), schema-registry.json

---

## Registro de Impacto — Archivos Existentes (v2) — Archivos Existentes (v2)

| Archivo | Sprints | Cambio |
|---------|---------|--------|
| `_edu/config.yaml` | S1, S3, S4, S7, S8, S9, S12 | Bloques de config nuevos al final |
| `_edu/module-help.csv` | S1-S12 | Filas nuevas al final |
| `WORKFLOW_PROMPT_MAP.md` | S1-S12 | Filas nuevas al final |
| `README.md` | S1-S12 | Secciones nuevas al final |
| `.gitignore` | S5 | 1 línea nueva |
| `scripts/requirements.txt` | S7, S9, S10, S11, S12 | Dependencias nuevas (bertopic, py-irt, open-clip-torch, smolagents, rdflib) |

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

S9 (semánticos) ─── requiere S1 (MiniLM ya instalado)
       │   S9.1 + S9.2 + S9.3 paralelizables entre sí
       ▼
S10 (psicometría) ─── requiere S2 (exam) + S7.4 (simulador para IRT data)
       │   S10.1 + S10.2 + S10.3 paralelizables entre sí
       ▼
S11 (knowledge eng) ─── requiere S9 (embeddings) + S10 (Bloom para KG)
       │   S11.1 (KG) primero → S11.2 (CPL usa el KG)
       ▼
S12 (full-stack) ─── requiere S8.2 (Director) + S9.3 (NLI) + S11 (KG)
       │   S12.1 → S12.2 → S12.3 (secuencial — cada fase extiende la anterior)
       │
       ▼
S13 (zero-curriculum) ─── requiere S11.1 (KG) + S11.2 (CPL) + S10.2 (BKT) + S12.1 (Director)
       │   S13.1 (KST Engine) ── S13.2 (Universal KG) ── S13.3 (Adaptive UI)
       └── Sprint FINAL: integra todos los sprints beyond-LLM
```

**S9-S11 pueden iniciarse en paralelo con S6-S8** — son independientes del pipeline de slides.  
**S12 es el sprint de integración final** — no iniciar hasta que S8.2, S9.3, S11.1 estén estables.

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
```mejoras

### Fase 6 — Beyond-LLM (S9 + S10, en paralelo con S8)
```
S9.1 (semantic drift) ───┐
S9.2 (BERTopic)       ───┤── paralelizables entre sí
S9.3 (NLI verifier)   ───┘
S10.1 (Bloom ML)      ───┐
S10.2 (IRT/BKT)       ───┤── paralelizables entre sí
S10.3 (CLIP)          ───┘
```

### Fase 7 — Knowledge Engineering (S11)
```
S11.1 (Knowledge Graph) ────── S11.2 (CPL) ← CPL usa el KG
```

### Fase 8 — Full-Stack Orchestration (S12)
```
S12.1 (Director Script) ── S12.2 (smolagents) ── S12.3 (GitHub Actions)
```

### Fase 9 — Zero-Curriculum Adaptive Learning (S13)
```
S13.1 (KST Engine) ─── S13.2 (Universal KG Builder) ─── S13.3 (Adaptive Tutor UI)
                          └─ usa CPL (S11.2) para prereqs cross-institution
```

> **S13 es el sprint final.**
> Requiere que S11.1 (KG), S11.2 (CPL), S10.2 (BKT) y S12.1 (Director) estén estables.

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
| S9 | 3 | 0 | 0 | 3 | 0 | **6** |
| S10 | 4 | 0 | 0 | 3 | 0 | **7** |
| S11 | 3 | 1 | 0 | 3 | 1 | **8** |
| S12 | 2 | 0 | 0 | 3 | 2 | **7** |
| S13 | 3 | 0 | 0 | 3 | 1 | **7** |
| **Total** | **27** | **7** | **4** | **35** | **16** | **89** |
