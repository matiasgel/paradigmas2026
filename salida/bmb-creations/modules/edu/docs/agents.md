# Referencia de agentes — EDU

El módulo EDU incluye **16 agentes especializados** en 5 capas. Los agentes marcados *(interno)* no son invocables directamente por el docente.

---

## Capa 1 — Ingesta e investigación

### `material-ingester` *(motor interno)*

**Rol:** Convierte material docente existente (PDFs, PPTX, DOCX) a Markdown estructurado.
**Invocado por:** Elena en `/edu-build-course-from-materials`
**MCP:** herramienta de archivos

---

### `plan-extractor` *(motor interno)*

**Rol:** Lee el PDF del programa institucional y extrae los tópicos obligatorios para `plan-minimo.md`.
**Invocado por:** Elena en `/edu-load-official-plan`
**Output clave:** `plan-minimo.md` — inmutable tras `/edu-confirm-official-plan`

---

### `academic-researcher` — Bib. Carlos 📚

**Rol:** Investigación académica en fuentes verificables. Provee fuentes con DOI para el plan, las referencias del material, y propuestas curriculares.
**Lista blanca estricta:** arXiv, ACM, IEEE, Springer, CrossRef, Semantic Scholar, ERIC, OpenLibrary. Prohibido: Wikipedia, blogs, Medium.
**Catchphrase:** Solo habla con DOIs. *"Wikipedia no figura en mi lista."*
**MCP:** herramienta de búsqueda web con lista blanca

---

## Capa 2 — Análisis y diseño pedagógico

### `course-planner` — Prof. Elena 🎓 *(orquestadora principal)*

**Rol:** Coordina todos los flujos del módulo. Es la cara visible del sistema para el docente en los comandos de flujo.
**Sidecar:** `_edu-memory/course-planner-sidecar/` — plan activo, años anteriores, score acumulado
**Catchphrase:** *"¿Está cubierto en el plan mínimo?"*
**Comandos principales:** `/edu-start-course`, `/edu-load-official-plan`, `/edu-plan-classes`, `/edu-help`, `/edu-status`, `/edu-close-course`, `/edu-start-new-year`

---

### `topic-designer` — Lic. Marcos 🗂️

**Rol:** Diseña el contenido de cada tema con la duración como constraint central. Controla el scope.
**Catchphrase:** *"Eso está fuera de scope del Tema N."*
**Comandos:** `/edu-design-topic {N}`, `/edu-assign-topics {N} {IDs}`, `/edu-set-topic-duration {N} {min}`

---

### `curriculum-reviewer` — Prof. Ana 🔍

**Rol:** Propone cambios curriculares justificados con fuentes académicas. Nunca propone cambio sin citar fuente.
**Comandos:** `/edu-propose-curriculum-change`

---

## Capa 3 — Producción documental

### `class-writer` — Dr. Roberto ✍️

**Rol:** Genera `minuta.md` y `filminas.md` proporcionales a la duración del tema.
**Catchphrase:** *"Déjenme reformular eso..."*
**Comandos:** `/edu-create-class {N}`

---

### `tp-designer` — Aux. Valeria 📝

**Rol:** Genera `tp.md` trazable a la minuta. Frena scope creep en el TP.
**Catchphrase:** *"¿Hay un ejercicio concreto para esto?"*
**Comandos:** `/edu-create-tp {N}`

---

## Capa 4 — Calidad (secuencia obligatoria)

### `writing-validator` 🔎 — Loop 1a

**Rol:** Detecta errores de escritura. No toca contenido temático.
**Comandos:** `/edu-validate-writing {N}`

### `writing-fixer` ✏️ — Loop 1b

**Rol:** Aplica correcciones de escritura. Cada corrección = commit Git reversible.
**Comandos:** `/edu-fix-writing-auto {N}`, `/edu-apply-writing-fixes {N}`, `/edu-fix-writing {N} {ID}`

### `coherence-fixer` 🔗 — Loop 2

**Rol:** Detecta rupturas de coherencia inter e intra documento. Unifica terminología.
**Comandos:** `/edu-validate-coherence {N}`, `/edu-fix-coherence-auto {N}`, `/edu-unify-terminology {N}`

### `reference-validator` 🔬 — Loop 3

**Rol:** Verifica referencias contra CrossRef, Semantic Scholar, OpenLibrary, arXiv. Nunca elimina — siempre señaliza.
**Comandos:** `/edu-validate-references {N}`, `/edu-fix-reference {N} {ID}`, `/edu-suggest-alternative {N} {ID}`

### `academic-guardrail` 🛡️ — Guardrail final

**Rol:** Detecta lenguaje informal, desvíos de scope y densidad cognitiva inadecuada según el perfil docente activo.
**Comandos:** `/edu-validate-scope {N}`, `/edu-validate-density {N}`, `/edu-fix-guardrail-auto {N}`

### `plan-coverage-checker` 📊 *(sidecar — restricción de primer orden)*

**Rol:** Verifica cobertura del `plan-minimo.md`. En modo silencioso (consultado por Elena) o alerta crítica si tópico obligatorio en riesgo real.
**⚠️ Restricción inamovible:** NUNCA puede sugerir, proponer ni permitir la modificación del `plan-minimo.md`. Solo reporta riesgo de no-cobertura.
**Sidecar:** `_edu-memory/plan-coverage-sidecar/` — matriz persistente entre sesiones
**Comandos:** `/edu-check-coverage`

---

## Capa 5 — Validación pedagógica y feedback

### `student-simulator` 🎓 *(sidecar dual)*

**Rol:** Simula la experiencia de aprendizaje de un alumno con perfil empírico basado en literatura académica.
**Sidecar session-scoped:** `_edu-memory/session/` — perfil activo + historial (se descarta al cerrar)
**Sidecar long-term:** `_edu-memory/calibracion-simulador/` — calibración acumulada (nunca se descarta)
**Catchphrase:** *"Profe, no entendí..."* — siempre en primera persona
**Comandos:** `/edu-test-topic {N} {perfil}`, `/edu-test-topic {N} all`, `/edu-research-student-profiles`, `/edu-compare-survey-simulator {N}`

### `test-runner` 🧪 *(motor interno)*

**Rol:** Consolida resultados del student-simulator en `score-pedagogico.md` y `faq-anticipado.md`.
**Invocado por:** `student-simulator`
