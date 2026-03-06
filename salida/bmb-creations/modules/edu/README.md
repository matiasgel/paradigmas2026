# EDU: Academic Course Production Suite

**Pipeline completo de producción docente universitaria con inteligencia pedagógica**

Desde la ingesta del programa oficial hasta el cierre de cursada con validación automática y memoria acumulada año a año.

---

## Visión general

EDU es un **sistema de producción docente universitaria** con inteligencia pedagógica. No es un generador de material — es un pipeline completo que va desde la ingesta del programa oficial de la cátedra hasta el cierre de la cursada con todos los temas validados, coherentes y listos para reusar el año siguiente.

**Lo que lo hace extraordinario:**
- Valida el material generado desde la perspectiva del alumno, usando perfiles empíricos investigados en literatura académica
- Mantiene continuidad año a año — aprende de cada cursada anterior y no empieza de cero
- Aplica guardrails de rigor académico en toda la cadena de producción
- Integra con Git de forma nativa: cada corrección automática es un commit
- Re-planificación dinámica post-clase: el plan se ajusta en tiempo real según lo que realmente ocurrió
- Calibración continua del simulador: las encuestas reales mejoran las predicciones del alumno simulado año a año

**Guardrail universal:** Toda investigación se restringe a fuentes académicas verificables (arXiv, ACM, IEEE, Springer, Google Scholar, OpenLibrary, Semantic Scholar, ERIC). Prohibido: Wikipedia, Medium, blogs, redes sociales.

---

## Instalación

```bash
copiá la carpeta `_edu/` a tu workspace
```

Seguí los prompts para configurar el módulo. Alternativamente, instalá este módulo copiando la carpeta `_edu/` a tu workspace.

---

## Quick Start

```bash
# 1. Configurar la materia
/edu-start-course

# 2. Cargar el programa institucional
/edu-load-official-plan programa.pdf
/edu-confirm-official-plan

# 3. Construir el plan desde material existente
/edu-build-course-from-materials ./material-año-anterior/

# 4. Ciclo de un tema
/edu-design-topic 1
/edu-create-class 1
/edu-create-tp 1

# 5. Loops de calidad (automáticos)
/edu-validate-writing 1
/edu-fix-writing-auto 1
/edu-validate-coherence 1
/edu-validate-references 1

# 6. Testing pedagógico
/edu-test-topic 1 all

# 7. Cerrar tema (solo cuando todos los loops resueltos)
/edu-close-topic 1
```

**Para guías detalladas, ver [docs/](docs/).**

---

## Componentes

### Agentes (16)

| Área | Agentes |
|---|---|
| **Ingesta** | `material-ingester` *(interno)*, `plan-extractor` *(interno)*, `academic-researcher` (Bib. Carlos) |
| **Diseño pedagógico** | `course-planner` (Prof. Elena ✦ orquestadora), `topic-designer` (Lic. Marcos), `curriculum-reviewer` (Prof. Ana) |
| **Producción documental** | `class-writer` (Dr. Roberto), `tp-designer` (Aux. Valeria) |
| **Calidad** | `writing-validator`, `writing-fixer`, `coherence-fixer`, `reference-validator`, `academic-guardrail`, `plan-coverage-checker` |
| **Testing pedagógico** | `student-simulator` (Estudiante ✦ sidecar dual), `test-runner` *(interno)* |

*(internos)* = sin slash commands propios, no invocables directamente por el docente.

### Workflows (15)

| Categoría | Workflows |
|---|---|
| **Core** | `load-official-plan`, `topic-cycle`, `quality-loops`, `close-course` |
| **Feature** | `build-course-from-materials`, `build-course-from-research`, `pedagogical-testing`, `new-year`, `curriculum-change`, `reopen-topic`, `adaptive-replan`, `student-feedback-loop` |
| **Utility** | `manage-student-profiles`, `check-coverage`, `update-copilot-context` |

---

## Configuración

Variables configuradas durante la instalación:

| Variable | Descripción | Default |
|---|---|---|
| `course_output_folder` | Carpeta de salida de cursadas | `{output_folder}/cursadas` |
| `default_professor_profile` | Perfil docente por defecto | `profesor-practico` |
| `default_class_duration` | Duración de clase en minutos | `90` |
| `lms_provider` | LMS institucional | `none` |
| `academic_guardrail_enabled` | Activar guardrail académico | `true` |
| `command_aliases` | Aliases de comandos en español | `true` |

---

## Estructura del módulo

```
_edu/
├── module.yaml
├── README.md
├── TODO.md
├── docs/
│   ├── getting-started.md
│   ├── agents.md
│   ├── workflows.md
│   └── examples.md
├── agents/
│   ├── course-planner.md          ← Elena (orquestadora, sidecar)
│   ├── topic-designer.md          ← Marcos
│   ├── curriculum-reviewer.md     ← Prof. Ana
│   ├── class-writer.md            ← Roberto
│   ├── tp-designer.md             ← Valeria
│   ├── academic-researcher.md     ← Carlos
│   ├── writing-validator.md
│   ├── writing-fixer.md
│   ├── coherence-fixer.md
│   ├── reference-validator.md
│   ├── academic-guardrail.md
│   ├── plan-coverage-checker.md   ← sidecar
│   ├── student-simulator.md       ← sidecar dual
│   ├── material-ingester.md       ← interno
│   ├── plan-extractor.md          ← interno
│   └── test-runner.md             ← interno
└── workflows/
    ├── load-official-plan/
    ├── topic-cycle/
    ├── quality-loops/
    ├── close-course/
    ├── build-course-from-materials/
    ├── build-course-from-research/
    ├── pedagogical-testing/
    ├── new-year/
    ├── curriculum-change/
    ├── reopen-topic/
    ├── adaptive-replan/
    ├── student-feedback-loop/
    ├── manage-student-profiles/
    ├── check-coverage/
    └── update-copilot-context/
```

---

## Documentación

Para guías de usuario detalladas, ver la carpeta **[docs/](docs/)**:
- [Primeros pasos](docs/getting-started.md)
- [Referencia de agentes](docs/agents.md)
- [Referencia de workflows](docs/workflows.md)
- [Ejemplos prácticos](docs/examples.md)

---

## Estado de desarrollo

Este módulo está en desarrollo activo.

- [ ] Agentes: 16 (specs listas — pendiente implementación)
- [ ] Workflows: 15 (specs listas — pendiente implementación)

Ver [TODO.md](TODO.md) para el roadmap detallado.

---

## Creado por

Matiasgel — EDU Framework, 2026
