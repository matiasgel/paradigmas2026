# TODO: EDU: Academic Course Production Suite

Roadmap de desarrollo del módulo `edu`.

---

> **Instrucción de prioridad:** Los ítems están ordenados por camino feliz — implementar en este orden garantiza tener un módulo usable lo antes posible.

---

## Agentes a construir

Implementar con tu editor de IA preferido → Spec: `agents/{agente}.spec.md`

### Prioridad 1 — Camino feliz core

- [ ] `course-planner` (Prof. Elena) — orquestadora principal con sidecar
  - Spec: `agents/course-planner.spec.md`
- [ ] `plan-extractor` *(motor interno)* — extrae tópicos del PDF institucional
  - Spec: `agents/plan-extractor.spec.md`
- [ ] `topic-designer` (Lic. Marcos) — diseña contenido de cada tema
  - Spec: `agents/topic-designer.spec.md`
- [ ] `class-writer` (Dr. Roberto) — genera minuta y filminas
  - Spec: `agents/class-writer.spec.md`
- [ ] `tp-designer` (Aux. Valeria) — genera trabajos prácticos
  - Spec: `agents/tp-designer.spec.md`

### Prioridad 2 — Loops de calidad

- [ ] `writing-validator` — detecta errores de escritura (Loop 1a)
  - Spec: `agents/writing-validator.spec.md`
- [ ] `writing-fixer` — corrige errores de escritura (Loop 1b)
  - Spec: `agents/writing-fixer.spec.md`
- [ ] `coherence-fixer` — corrige rupturas de coherencia (Loop 2)
  - Spec: `agents/coherence-fixer.spec.md`
- [ ] `reference-validator` — valida referencias académicas (Loop 3)
  - Spec: `agents/reference-validator.spec.md`
- [ ] `academic-guardrail` — controla formalidad, scope y densidad (Guardrail)
  - Spec: `agents/academic-guardrail.spec.md`
- [ ] `plan-coverage-checker` — verifica cobertura del plan mínimo (sidecar)
  - Spec: `agents/plan-coverage-checker.spec.md`

### Prioridad 3 — Features clave

- [ ] `student-simulator` (Estudiante dinámico) — simulador pedagógico con sidecar dual
  - Spec: `agents/student-simulator.spec.md`
- [ ] `academic-researcher` (Bib. Carlos) — investigación académica con lista blanca
  - Spec: `agents/academic-researcher.spec.md`
- [ ] `curriculum-reviewer` (Prof. Ana) — propuestas curriculares con fuentes
  - Spec: `agents/curriculum-reviewer.spec.md`

### Prioridad 4 — Motores internos restantes

- [ ] `material-ingester` *(motor interno)* — convierte PDFs/PPTX a Markdown
  - Spec: `agents/material-ingester.spec.md`
- [ ] `test-runner` *(motor interno)* — consolida resultados de testing
  - Spec: `agents/test-runner.spec.md`

---

## Workflows a construir

Implementar con tu editor de IA preferido → Spec: `workflows/{wf}/{wf}.spec.md`

### Prioridad 1 — Core (camino feliz)

- [ ] `load-official-plan` — extrae tópicos del PDF institucional y bloquea plan-minimo.md
  - Spec: `workflows/load-official-plan/load-official-plan.spec.md`
- [ ] `topic-cycle` — ciclo completo diseño → clase → TP
  - Spec: `workflows/topic-cycle/topic-cycle.spec.md`
- [ ] `quality-loops` — 3 loops + guardrail sobre documentos del tema
  - Spec: `workflows/quality-loops/quality-loops.spec.md`
- [ ] `close-course` — cierre de cursada con retrospectiva y protección Git
  - Spec: `workflows/close-course/close-course.spec.md`

### Prioridad 2 — Features clave

- [ ] `build-course-from-materials` — plan desde material existente (brownfield)
  - Spec: `workflows/build-course-from-materials/build-course-from-materials.spec.md`
- [ ] `pedagogical-testing` — simulación de alumno sobre el tema
  - Spec: `workflows/pedagogical-testing/pedagogical-testing.spec.md`
- [ ] `new-year` — inicio de año lectivo desde el anterior
  - Spec: `workflows/new-year/new-year.spec.md`
- [ ] `adaptive-replan` — re-planificación post-clase en tiempo real
  - Spec: `workflows/adaptive-replan/adaptive-replan.spec.md`

### Prioridad 3 — Features adicionales

- [ ] `build-course-from-research` — plan desde investigación académica (greenfield)
  - Spec: `workflows/build-course-from-research/build-course-from-research.spec.md`
- [ ] `student-feedback-loop` — calibración del simulador con encuestas reales
  - Spec: `workflows/student-feedback-loop/student-feedback-loop.spec.md`
- [ ] `curriculum-change` — propuesta de cambio curricular justificada
  - Spec: `workflows/curriculum-change/curriculum-change.spec.md`
- [ ] `reopen-topic` — reapertura acotada de tema cerrado
  - Spec: `workflows/reopen-topic/reopen-topic.spec.md`

### Prioridad 4 — Utility

- [ ] `manage-student-profiles` — investigación y gestión de perfiles empíricos
  - Spec: `workflows/manage-student-profiles/manage-student-profiles.spec.md`
- [ ] `check-coverage` — matriz de cobertura del plan mínimo
  - Spec: `workflows/check-coverage/check-coverage.spec.md`
- [ ] `update-copilot-context` — actualiza .github/copilot-instructions.md
  - Spec: `workflows/update-copilot-context/update-copilot-context.spec.md`

---

## Testing de instalación

- [ ] Verificar instalación copiando `_edu/` al workspace
- [ ] Verificar que los prompts de `module.yaml` funcionen correctamente
- [ ] Verificar que todos los agentes y workflows sean descubribles
- [ ] Probar flujo completo: load-official-plan → topic-cycle → quality-loops → close-course
- [ ] Verificar integración Git-native (branches, commits automáticos)
- [ ] Verificar guardrail académico (rechazar fuentes no autorizadas)
- [ ] Verificar sidecar session-scoped vs. long-term del student-simulator

---

## Documentación

- [ ] Completar `docs/getting-started.md` con ejemplos de uso
- [ ] Completar `docs/agents.md` con referencia completa de cada agente
- [ ] Completar `docs/workflows.md` con referencia completa de cada workflow
- [ ] Completar `docs/examples.md` con casos de uso reales (Adrián, Laura)
- [ ] Agregar sección de troubleshooting en `docs/examples.md`
- [ ] Documentar configuración de LMS (Moodle, Google Classroom)
- [ ] Documentar setup de Google Workspace OAuth

---

## Fase 2 — GitHub Actions (roadmap futuro)

- [ ] `ci-topic-pipeline.yml` — hooks por evento Git (push a `tema/**`, PR, merge)
- [ ] GitHub Pages dashboard estático de estado de la cursada
- [ ] JSON de estado junto a Markdown (`estado-tema.json`, `cobertura-actual.json`)

---

## Fase 3 — Codespaces + Copilot Agent (roadmap futuro)

- [ ] Setup para abrir repo en browser sin instalar nada
- [ ] Issue → Copilot Coding Agent → loops → PR automático
- [ ] PR como interfaz de revisión con comentarios del alumno simulado

---

_Última actualización: 2026-03-06_
