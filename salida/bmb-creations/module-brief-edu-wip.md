---
# ESTADO DE SESIÓN — COMPLETADO
workflow: create-module-brief
status: complete
date_started: "2026-03-06"
date_completed: "2026-03-06"
user_name: Matiasgel
communication_language: spanish

# Pasos completados del workflow
steps_completed: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Brief final generado
output_file: "salida/bmb-creations/modules/module-brief-edu.md"

# Decisiones confirmadas
module_type: standalone
module_code: edu
collaboration_mode: express

# Decisiones de Step 5 — CONFIRMADAS
module_name: "EDU: Academic Course Production Suite"
personality_theme: "Equipo académico clásico — roles universitarios reales (Prof. Titular, JTP, Investigador)"

# Notas de sesión
session_notes: >
  Step 5 completado 2026-03-06.
  Nombre: EDU: Academic Course Production Suite.
  Tema de personalidad: equipo académico clásico con roles universitarios reales.
  Step 6 completado: personas (Adrián y Laura, UNTDF) y journey de usuario confirmados.
  Step 7 completado: propuesta de valor formalizada, contexto competitivo, notas de roadmap (GitHub Pages, Actions, Codespaces, Copilot Agent).
  Step 8 completado: personalidades de agentes confirmadas, patrón de acceso Opción C (Elena coordina flujo, acceso directo para calidad/testing), plan-coverage-checker en modo mixto (silencioso → Elena, interrumpe directo solo si crítico), sidecars definidos.
  Step 9 completado: ecosistema de workflows confirmado — 4 core, 6 feature (incluyendo reopen-topic), 3 utility. Quality-loops invocables independientemente. Dos modos de entrada separados (brownfield/greenfield).
  Step 10 completado: MCP tools (git, filesystem, web-search restringido, github, google-workspace), modelo tema/clase (duración vive en el tema como constraint de generación), métricas de densidad cognitiva en perfil docente, comandos nuevos (plan-classes, set-topic-duration, validate-density, export-*, setup-google-workspace), google-workspace-mcp Fase 1.
  Step 11 completado: tres escenarios de uso confirmados (primera vez, momento de mayor valor, aha de Laura).
  Step 12 completado: elementos creativos confirmados — catchphrases por agente, 5 easter eggs, lore del equipo docente.
  Step 13 en curso: modelo LMS-agnóstico confirmado (init configurable), Moodle MCP investigado (peancor/moodle-mcp-server ⭐31, funcional), lms-mcp como adaptador intercambiable. Features nuevas: adaptive-replan (re-planificación dinámica post-clase) y student-feedback-loop (encuestas guiadas + calibración del simulador).
---

# Module Brief: edu — TRABAJO EN PROGRESO

**Fecha:** 2026-03-06
**Autor:** Matiasgel
**Código del módulo:** `edu`
**Tipo de módulo:** Standalone
**Estado:** En elaboración — retomar en Step 8 (Agentes)

---

## Resumen ejecutivo

El módulo EDU es un **sistema de producción docente universitaria con inteligencia pedagógica**. No es un generador de material — es un pipeline completo que va desde la ingesta del programa oficial de la cátedra hasta el cierre de la cursada con todos los temas validados, coherentes y listos para reusar el año siguiente.

**Lo que lo hace extraordinario:**
- Valida el material generado desde la perspectiva del alumno, usando perfiles empíricos investigados en literatura académica
- Mantiene continuidad año a año — aprende de cada cursada anterior y no empieza de cero
- Aplica guardrails de rigor académico en toda la cadena de producción: solo fuentes verificables, solo dominios académicos
- Integra con Git de forma nativaMCP: cada corrección automática es un commit, cada tema es una branch

**Guardrail universal:** Toda investigación, sin excepción, se restringe a fuentes académicas verificables (arXiv, ACM, IEEE, Springer, Google Scholar, OpenLibrary, Semantic Scholar, ERIC). Fuentes prohibidas para todos los agentes: Wikipedia, Medium, blogs, redes sociales, sitios sin afiliación institucional.

---

## Identidad del módulo

### Código y nombre

- **Código:** `edu`
- **Nombre display:** EDU: Acadermic Course Production Suite

### Concepto central

Un equipo de agentes especializados que actúa como el departamento de producción docente de una cátedra universitaria. Cubre todo el ciclo: ingesta de material existente → diseño pedagógico → producción de contenido → validación de calidad → testing pedagógico con alumnos simulados.

### Tema de personalidad

**Equipo académico clásico** — los agentes tienen roles y nombres inspirados en la estructura universitaria real (Prof. Titular, Jefe de Trabajos Prácticos, Investigador, Auxiliar Docente, etc.). El tono es riguroso pero accesible; la metáfora de equipo docente es consistente en toda la mensajería del módulo.

---

## Tipo de módulo

**Tipo:** Standalone

Módulo completamente nuevo en el dominio de educación universitaria. No extiende ningún módulo existente de BMAD. Se instala en `src/modules/edu/` con `code: edu`. Todos los slash commands siguen el patrón `/edu-*`.

---

## Propuesta de valor única

**Declaración formal:**

> *"Para docentes universitarios técnicos de la UNTDF (y universidades similares), **EDU: Academic Course Production Suite** provee un pipeline completo de producción docente con validación pedagógica automática y memoria acumulada año a año — a diferencia de herramientas genéricas de IA o flujos manuales — porque es el único sistema que valida el material desde la perspectiva real del alumno, garantiza cobertura del programa institucional como punto de verdad inmutable, y aprende de cada cursada anterior."*

**Lo que no existe en ninguna otra herramienta:**

1. **Alumno simulado con perfil empírico** — no es un revisor genérico; lee con las limitaciones cognitivas reales documentadas en literatura académica
2. **Plan mínimo institucional como contrato inmutable** — el PDF de la institución no se puede saltear; el sistema bloquea el cierre si hay tópicos sin cubrir
3. **Memoria que acumula entre años** — no empieza de cero; la retrospectiva del año anterior alimenta el plan del siguiente
4. **Git-native de verdad** — cada corrección automática es un commit reversible, no una caja negra

**Contexto competitivo:**

| Alternativa | Limitación |
|---|---|
| ChatGPT / Copilot genérico | No conoce el programa institucional, no tiene memoria de cursada, no valida cobertura |
| Herramientas de authoring (Notion, Obsidian) | No producen ni validan — solo organizan |
| LMS (Moodle, Canvas) | Gestionan entrega pero no producen ni mejoran el material |
| Flujo manual del docente | Escala mal, inconsistente entre JTPs, sin métrica de calidad |

**"Momento aha"** para Adrián: cuando corre `/edu-test-topic 1 all` y el alumno simulado señala exactamente la slide donde está la confusión — antes de llevarla a clase.

---

## Usuarios del módulo

### Persona 1 — Usuario primario

> **Adrián, Jefe de Cátedra — Programación 2, UNTDF**
> - Lleva 8 años dictando la misma materia; parte del material tiene más de 5 años
> - Usa Git para el código de ejemplos pero nunca para el material docente
> - Tiene 3 JTPs que producen material inconsistente entre sí
> - **Goal:** Que el material de este año sea coherente, esté documentado y pueda reusar el año que viene sin empezar de cero
> - **Pain points:** Revisa errores de escritura manualmente, las referencias están desactualizadas, no sabe si cubre todos los tópicos del programa oficial
> - **Éxito:** Cierra la cursada con `retrospectiva-anual.md` generada, score pedagógico medible, y el año siguiente arranca con `/edu-start-new-year` en 10 minutos

Perfil técnico:
- Maneja Git con fluidez (commits, branches, merge, revert)
- Usa GitHub Copilot activamente como herramienta de trabajo
- Lee y edita Markdown sin dificultad
- Comprende el modelo mental de slash commands y agentes de AI
- **No requiere modo tutorial básico** — sí se beneficia de orientación de flujo tipo `bmad-help`

### Persona 2 — Usuario secundario

> **Laura, Auxiliar Docente — primer año en la cátedra, UNTDF**
> - Recién incorporada al equipo de cátedra
> - Produce TPs y minutas pero sin criterio de consistencia con el resto del equipo
> - **Goal:** Integrarse al estilo de la cátedra sin tener que pedir validación constante
> - **Pain points:** No sabe si su material es coherente con lo que ya se enseñó; comete errores de scope (incluye temas no vistos)
> - **Éxito:** Sus TPs pasan los loops automáticos sin intervención del Jefe de Cátedra

### User Journey — Adrián en la cursada de Programación 2 (UNTDF)

```
SITUACIÓN: Primera semana del cuatrimestre.

1. Adrián tiene el PDF del programa institucional y slides del año pasado.
   → /edu-load-official-plan plan-institucional.pdf
   → plan-minimo.md creado y bloqueado ← punto de verdad inmutable

2. Investiga y arma el plan de estudio.
   → /edu-research-plan
   → Propone 14 temas; Adrián confirma, reordena 2, elimina 1.

3. Para Tema 1 — Paradigmas de programación:
   → /edu-design-topic 1
   → /edu-create-class 1
   → /edu-create-tp 1

4. Loop de calidad automático:
   → /edu-validate-writing 1    → 2 errores críticos → /edu-fix-writing-auto 1
   → /edu-validate-coherence 1  → terminología unificada
   → /edu-validate-references 1 → 1 referencia obsoleta → Adrián sugiere alternativa
   → /edu-validate-scope 1      → sin desvíos

5. Testing pedagógico:
   → /edu-test-topic 1 all
   → student-simulator detecta: "La diferencia entre OOP y FP no queda clara en slide 4"
   → faq-anticipado.md generado: Adrián sabe qué preguntar en clase

6. Cierre:
   → /edu-close-topic 1   ← Git: branch merged a main, commit con hash

7. Fin de cursada:
   → /edu-close-course programacion-2 2026
   → retrospectiva-anual.md + score-pedagogico comparado con año anterior

AÑO SIGUIENTE:
   → /edu-start-new-year programacion-2 2027
   → Lee retrospectiva + sugiere mejoras basadas en score pedagógico
```

---

## Arquitectura de agentes

### Patrón de acceso (Opción C — confirmado en Step 8)

```
Comandos de FLUJO (inicio, diseño, cierre)      → Prof. Elena (course-planner) coordina
Comandos de CALIDAD/TESTING (loops, validación) → acceso directo al agente especializado
Comandos de COBERTURA                           → Elena (consulta plan-coverage-checker
                                                  internamente; interrumpe al docente
                                                  solo si hay tópico obligatorio en riesgo)
```

**El docente es siempre el usuario humano** — no es un agente. Adrián y Laura interactúan directamente con el sistema mediante slash commands.

### 5 capas de agentes

#### Capa 1 — Ingesta e investigación

| Agente | Nombre | Rol universitario | Operación principal | CommunicationStyle | Sidecar |
|---|---|---|---|---|---|
| `material-ingester` | *(motor interno)* | — | PDF, PPTX, slides exportadas → Markdown (solo conversión, nunca interpreta) | Sin comunicación directa al docente — reporta resultado estructurado | No |
| `plan-extractor` | *(motor interno)* | — | Procesar PDF universitario y producir lista de tópicos obligatorios (solo extrae, nunca infiere) | Sin comunicación directa al docente — reporta resultado estructurado | No |
| `academic-researcher` | **Bib. Carlos** | Bibliotecario académico | Solo arXiv, ACM, IEEE, Springer, Google Scholar, OpenLibrary, Semantic Scholar, ERIC | Preciso, neutral, no opina sobre el contenido — entrega fuentes con DOI/URL verificable | No |

#### Capa 2 — Análisis y diseño pedagógico

| Agente | Nombre | Rol universitario | Operación principal | CommunicationStyle | Sidecar |
|---|---|---|---|---|---|
| `course-planner` | **Prof. Elena** | Profesora Titular | Coordina flujo; importa, analiza y genera plan de estudio | Rigurosa, metódica, coordina al equipo; interrumpe cuando detecta riesgo de scope o cobertura | **Sí** — recuerda plan activo, años anteriores, score pedagógico acumulado |
| `topic-designer` | **Lic. Marcos** | JTP — Jefe de Trabajos Prácticos | Define contenidos, objetivos de aprendizaje y semanas por tema | Detallista, orientado a objetivos; frena scope creep explícitamente | No |
| `curriculum-reviewer` | **Prof. Ana** | Investigadora / Consejo académico | Compara plan actual vs. nuevo; cambios siempre justificados con fuente académica verificada | Crítica constructiva, nunca propone cambio sin citar fuente | No |

#### Capa 3 — Producción documental

| Agente | Nombre | Rol universitario | Operación principal | CommunicationStyle | Sidecar |
|---|---|---|---|---|---|
| `class-writer` | **Dr. Roberto** | Profesor de clase magistral | Genera minuta y filminas; respeta duración y scope de `diseño.md` | Claro y narrativo; estructura explicaciones como docente experimentado; acepta feedback y corrige sin drama | No |
| `tp-designer` | **Aux. Valeria** | Auxiliar Docente | Genera guía de prácticos trazable a `minuta.md`; no incluye temas no vistos | Práctica y directa; orientada al ejercicio concreto; alerta si detecta scope creep | No |

#### Capa 4 — Calidad (orden secuencial obligatorio, motores internos)

| Agente | Rol | Guardrail específico | CommunicationStyle | Sidecar |
|---|---|---|---|---|
| `writing-validator` | Detección de errores de escritura | No toca contenido temático; solo señaliza | Motor interno — reporta lista estructurada de hallazgos | No |
| `writing-fixer` | Corrección automática de escritura | No toca bloques de código, fragmentos técnicos ni nombres de archivo | Motor interno — aplica correcciones y reporta diff | No |
| `coherence-fixer` | Corrección de coherencia textual | Detecta rupturas inter e intra documento; unifica terminología | Motor interno — reporta inconsistencias y aplica fixes confirmados | No |
| `reference-validator` | Validación de referencias | Cruza con CrossRef, Semantic Scholar, OpenLibrary, arXiv; nunca elimina, siempre señaliza | Motor interno — reporta estado de cada referencia con URL de verificación | No |
| `academic-guardrail` | Control de formalidad y scope | Detecta lenguaje informal, desvíos de scope, nivel inadecuado | Motor interno — pide confirmación antes de reformular | No |
| `plan-coverage-checker` | Verificación de cobertura | Mantiene matriz en tiempo real; **modo mixto**: silencioso por defecto (Elena consulta), interrumpe directo al docente solo si tópico obligatorio está en riesgo real de quedar sin cubrir | Motor interno con alerta crítica directa al docente en caso límite | **Sí** — mantiene matriz de cobertura persistente |

**Protocolo de precedencia (secuencial, no paralelo):**
```
Loop 1: writing-validator → writing-fixer
         ↓
Loop 2: coherence-fixer
         ↓
Loop 3: reference-validator
         ↓
Guardrail: academic-guardrail
```

#### Capa 5 — Validación pedagógica (NUEVO — no estaba en brainstorming original)

| Agente | Nombre | Rol | Operación principal | CommunicationStyle | Sidecar |
|---|---|---|---|---|---|
| `student-simulator` | **Estudiante** *(dinámico por perfil)* | Alumno simulado con perfil empírico | Lee material con guardrails de reducción cognitiva según perfil configurado | Variable según perfil activo — en modo conversacional habla en primera persona como alumno real; en modo silencioso solo entrega reporte | **Sí** — recuerda perfiles configurados para cada materia |
| `test-runner` | *(motor interno)* | Ejecutor de baterías de testing | Corre múltiples perfiles y consolida resultados | Sin comunicación directa al docente — entrega `score-pedagogico.md` y `faq-anticipado.md` | No |

**Dos modos de simulación:**
- `silencioso` — corre en background, solo interrumpe si hay algo crítico
- `conversacional` — el alumno simulado habla directamente ("Profe, no entendí qué diferencia hay entre X e Y en la slide 4")

**Salidas del testing pedagógico:**
- `test-alumno-{perfil}.md` — hallazgos por documento y perfil
- `faq-anticipado.md` — preguntas que los alumnos simulados no pudieron responder; el docente lleva a clase preparado
- `score-pedagogico.md` — métrica de claridad por tema y perfil; acumulable año a año

**Comandos:**
```
/edu-research-student-profiles {materia} {año-curricular}   ← investiga perfiles empíricos en literatura académica
/edu-create-student-profile {nombre} {fuente}               ← adopta o crea un perfil
/edu-test-topic {N} {perfil}                                ← simula la experiencia de un alumno con ese perfil
/edu-test-topic {N} all                                     ← corre todos los perfiles configurados
```

---

## Workflows del módulo

### Categorías de workflows (confirmado en Step 9)

#### ⚙️ Core Workflows — funcionalidad esencial

| Workflow | Agente owner | Input → Proceso → Output |
|---|---|---|
| `load-official-plan` | `plan-extractor` | PDF institucional → extracción de tópicos → `plan-minimo.md` bloqueado |
| `topic-cycle` | `topic-designer` → `class-writer` → `tp-designer` | N° de tema → diseño + clase + TP → carpeta `temas/NN-*` completa |
| `quality-loops` | Capa 4 (secuencial) | Documentos del tema → loops 1-3 + guardrail → documentos corregidos + historial |
| `close-course` | `course-planner` | Materia + año → retrospectiva + score acumulado + carpeta protegida |

**Nota:** Los 4 loops internos de `quality-loops` son **invocables independientemente** (el docente puede correr solo Loop 2 y Loop 3 si reabre un tema por cambio de scope). El workflow `quality-loops` completo existe para runs desde cero.

#### 🌟 Feature Workflows — capacidades especializadas

| Workflow | Agente owner | Input → Proceso → Output |
|---|---|---|
| `build-course-from-materials` | `material-ingester` → `course-planner` | PDFs/PPTX existentes → conversión + análisis → plan de estudio sugerido **(modo brownfield)** |
| `build-course-from-research` | `academic-researcher` → `course-planner` | Tema/objetivos → investigación académica → plan de estudio sugerido **(modo greenfield)** |
| `pedagogical-testing` | `student-simulator` → `test-runner` | Tema N + perfiles → simulación por perfil → `faq-anticipado.md` + `score-pedagogico.md` |
| `new-year` | `course-planner` | Materia + año anterior → lectura retrospectiva → borrador nuevo plan con mejoras sugeridas |
| `curriculum-change` | `curriculum-reviewer` | Plan actual + señal de cambio → comparación justificada con fuente académica → `curriculum-change-proposal.md` |
| `reopen-topic` | `course-planner` → agentes afectados | Tema ya cerrado + scope del cambio → re-apertura acotada de loops necesarios → tema re-cerrado |

| `student-feedback-loop` | `student-simulator` → `test-runner` | Respuestas de alumnos reales → análisis comparativo con predicciones del simulador → score actualizado + perfil calibrado |
| `adaptive-replan` | `course-planner` (Elena) | Registros de clases dictadas + plan restante → análisis de delta acumulado → propuesta de ajuste al plan |

**Decisión de diseño — dos modos de entrada separados:** `build-course-from-materials` y `build-course-from-research` son workflows distintos porque activan agentes de entrada completamente diferentes (`material-ingester` vs `academic-researcher`). Ambos convergen en `topic-cycle` a partir del plan de estudio confirmado.

#### 🔧 Utility Workflows — soporte operativo

| Workflow | Agente owner | Input → Proceso → Output |
|---|---|---|
| `manage-student-profiles` | `student-simulator` | Materia + año curricular → investigación ERIC/ACM → perfiles empíricos disponibles|
| `check-coverage` | `plan-coverage-checker` | Estado actual → matrix de cobertura → `cobertura-actual.md` |
| `update-copilot-context` | `course-planner` | Estado de la cursada → `.github/copilot-instructions.md` actualizado |

### Conexiones entre workflows

```
build-course-from-materials ─┐
                              ├─→ load-official-plan ─→ topic-cycle (loop) ─→ quality-loops ─→ pedagogical-testing ─→ close-course
build-course-from-research ──┘                                │                                                             │
                                                      reopen-topic ←─ curriculum-change                               new-year
                                                      (si cambio de scope)                                               │
                                                                                                              topic-cycle (próximo año)
```

**Workflows en cualquier momento (no secuenciales):**
`check-coverage` · `curriculum-change` · `update-copilot-context` · `manage-student-profiles`

### Workflows por etapa (referencia de comandos)

| Etapa | Workflow | Comandos clave |
|---|---|---|
| 0 — Plan mínimo | `load-official-plan` | `/edu-load-official-plan`, `/edu-confirm-official-plan` |
| 1 — Plan de estudio | `build-course-from-materials` / `build-course-from-research` | `/edu-research-plan`, `/edu-check-coverage` |
| 2 — Ciclo por tema | `topic-cycle` (loop) | `/edu-design-topic`, `/edu-create-class`, `/edu-create-tp` |
| 2 — Calidad | `quality-loops` (loops independientes) | Loops 1-3 + guardrail |
| 2 — Testing | `pedagogical-testing` | `/edu-test-topic`, `/edu-research-student-profiles` |
| 2 — Cambio curricular | `curriculum-change` + `reopen-topic` | `/edu-propose-curriculum-change` |
| 3 — Cierre | `close-course` | `/edu-check-coverage`, `/edu-close-course` |
| — | `new-year` | `/edu-start-new-year`, `/edu-copy-topic`, `/edu-adapt-topic` |

### Ciclo completo por tema

```
/edu-design-topic {N}
/edu-create-class {N}
/edu-create-tp {N}

┌─── LOOP 1: ESCRITURA ──────────────────────────────────────────────────────────┐
│  /edu-validate-writing {N}     → /edu-fix-writing-auto {N}                    │
└────────────────────────────────────────────────────────────────────────────────┘
┌─── LOOP 2: COHERENCIA ─────────────────────────────────────────────────────────┐
│  /edu-validate-coherence {N}   → /edu-fix-coherence-auto {N}                  │
│  /edu-unify-terminology {N}                                                    │
└────────────────────────────────────────────────────────────────────────────────┘
┌─── LOOP 3: REFERENCIAS ────────────────────────────────────────────────────────┐
│  /edu-validate-references {N}  → fix / suggest / accept / reject               │
└────────────────────────────────────────────────────────────────────────────────┘
┌─── GUARDRAIL ──────────────────────────────────────────────────────────────────┐
│  /edu-validate-scope {N}       → /edu-fix-guardrail-auto {N}                  │
└────────────────────────────────────────────────────────────────────────────────┘
┌─── TESTING PEDAGÓGICO ─────────────────────────────────────────────────────────┐
│  /edu-test-topic {N} all                                                       │
└────────────────────────────────────────────────────────────────────────────────┘

/edu-close-topic {N}   ← bloqueado hasta que todos los loops estén resueltos
```

---

## Estructura de salida

```
salida/
  {nombre-materia}/
    {año}/
      plan-minimo.md              ← tópicos obligatorios (inmutable una vez confirmado)
      plan-de-estudio.md
      cobertura-actual.md         ← matriz en tiempo real
      cobertura-final.md
      curso-plan-general.md
      curriculum-change-proposal.md
      comparacion-vs-anio-anterior.md
      temas/
        NN-nombre-del-tema/
          diseño.md
          minuta.md
          filminas.md
          tp.md
          cobertura-tema.md
          referencias-estado.md
          revisión-escritura.md
          revisión-coherencia.md
          revisión-guardrail.md
          test-alumno-{perfil}.md
          faq-anticipado.md
          score-pedagogico.md
          correcciones-escritura-historial.md   ← opcional con Git-native
          correcciones-coherencia-historial.md  ← opcional con Git-native

_edu-memory/
  global-preferences.md
  patrones-recurrentes.md
  historial-decisiones.md
  ├── calibracion-simulador/
    {materia}-calibracion.md
  historial-encuestas/
    {materia}-{año}-encuestas.md
  perfiles-alumnos/
    {materia}-perfil.md
    {materia}-perfiles-investigados.md     ← output de /edu-research-student-profiles
  perfiles-profesores/
    perfil-{nombre}.md
```

---

## Modelo Tema / Clase

**Distinción fundamental (confirmada en Step 10):**

| Unidad | Qué es | Tiene duración |
|---|---|---|
| **Tema** | Unidad de contenido (lo que se diseña, valida y testea) | Sí — en `diseño.md` |
| **Clase** | Unidad de tiempo (90 min o la duración configurada) | No — es la suma de sus temas |

```
Tema 1: Paradigmas de programación  ─ 45 min ─┐
                                               ├─→ Clase 1 = 90 min
Tema 2: Introducción a OOP          ─ 45 min ─┘

Tema 3: Herencia y polimorfismo     ─ 60 min ─┐
                                               ├─→ Clase 2 = 90 min
Tema 4: Interfaces y contratos      ─ 30 min ─┘
```

**Implicancias:**
- La **duración en `diseño.md`** es un constraint de generación: el `class-writer` genera minuta y filminas proporcionales a ese tiempo
- Cambiar la duración de un tema (`/edu-set-topic-duration`) dispara regeneración del material y reabre los loops de calidad afectados
- Los loops de calidad, testing pedagógico y cierre operan **a nivel de tema** (unidad de contenido)
- `plan-classes` opera **a nivel de clase** (agrupa temas que suman la duración de la sesión)
- Google Calendar y Google Slides sincroniza **por clase**

---

## Métricas de densidad cognitiva

**Principio:** La duración del tema define el volumen de contenido generado. El perfil docente define las métricas de densidad.

### Métricas base (literatura académica)

| Métrica | Referencia | Valor estándar |
|---|---|---|
| Tiempo por slide | Mayer's Cognitive Load Theory | 2-7 min según tipo |
| Palabras por slide | Regla 6x6 (presentation design) | ≤ 40 palabras |
| Conceptos nuevos por clase | Miller's Law (7 ± 2) | ≤ 7 por sesión |
| Ratio texto/imagen | Split-attention effect | ≤ 60% texto |

### Métricas por perfil docente

```yaml
profesor-teorico:
  slides_time_per_slide: "4-5 min"
  words_per_slide: 50          # más denso, acepta más texto
  concepts_per_class: 5
  image_ratio_max: 40          # más texto que imagen

profesor-practico:
  slides_time_per_slide: "2-3 min"
  words_per_slide: 30          # más visual
  concepts_per_class: 3        # más tiempo por concepto con ejercicio
  image_ratio_max: 60

profesor-flipped:
  slides_time_per_slide: "3-4 min"
  words_per_slide: 35
  concepts_per_class: 4
  image_ratio_max: 50
```

### Validación de densidad (integrada en `academic-guardrail`)

El guardrail extiende su scope para detectar:
- `[DENSIDAD-ALTA]` — slide con más palabras que el límite del perfil
- `[TIEMPO-CORTO]` — cantidad de slides incompatible con la duración del tema
- `[SOBRECARGA]` — más conceptos nuevos que el máximo del perfil en una clase

Comando dedicado: `/edu-validate-density {N}` — corre solo las validaciones de densidad cognitiva del tema N.

---

## Tools, MCP e integraciones

### MCP Tools

| MCP | Agentes que lo usan | Propósito |
|---|---|---|
| **`git-mcp`** | `course-planner`, `writing-fixer`, `coherence-fixer` | Branches por tema, commits automáticos de correcciones, merge al cerrar tema, protección de branches al cerrar cursada |
| **`filesystem-mcp`** | `material-ingester`, `plan-extractor`, todos los writers | Lectura de PDFs/PPTX de entrada, escritura de Markdown en estructura `salida/` |
| **`web-search-mcp`** *(lista blanca)* | `academic-researcher`, `reference-validator`, `curriculum-reviewer` | Acceso restringido a: arXiv, ACM, IEEE, Springer, CrossRef, Semantic Scholar, ERIC, OpenLibrary. **Todo lo demás bloqueado por guardrail.** |
| **`github-mcp`** | `course-planner` | Crear/gestionar PRs para cierre de temas, actualizar `.github/copilot-instructions.md` |
| **`google-workspace-mcp`** *(Fase 1, si configurado)* | `course-planner`, `class-writer`, `tp-designer` | Exportar material a Google Workspace; ver detalle más abajo |
| **`lms-mcp`** *(configurable en init)* | `course-planner`, `tp-designer`, `class-writer` | Publicar material en el LMS de la institución; adaptador intercambiable según config |

### Modelo LMS-agnóstico (confirmado en Step 13)

**Principio:** la UNTDF es solo el contexto de diseño — no el usuario hardcodeado. El módulo es universal y se configura al iniciar:

```
/edu-start-course
```

Elena pregunta en el init:
1. ¿Nombre de la materia?
2. ¿Universidad / institución?
3. ¿Perfil docente? (`profesor-teorico`, `profesor-practico`, etc.)
4. ¿Duración de clase? (60, 90, 120 min)
5. ¿LMS? (`moodle` / `google-classroom` / `none`)
6. ¿Idioma de comunicación? (si no se configuró en el install)

Todo queda en `_edu/config.yaml` — el módulo opera con ese contexto sin volver a preguntar.

```yaml
# _edu/config.yaml
lms:
  provider: moodle        # o "google-classroom" o "none"
  moodle_url: "https://moodle.universidad.edu"
  moodle_token: "{token}"
```

Los comandos `/edu-publish-*` funcionan igual sin importar el LMS elegido. Si el docente elige `none`, esos comandos no están disponibles.

### LMS MCP — adaptadores disponibles

#### Moodle MCP

**Estado del ecosistema:** Existen implementaciones reales y funcionales en 2026:

| Repo | Stars | Lang | Capacidades |
|---|---|---|---|
| `peancor/moodle-mcp-server` | ⭐31 | JavaScript | Cursos, alumnos, assignments, quizzes, feedback |
| `loyaniu/moodle-mcp` | ⭐14 | — | Interacción general con Moodle LMS |
| `onbirdev/moodle-webservice_mcp` | ⭐3 | — | Plugin nativo de Moodle (instala en el servidor) |

**Capacidades relevantes para EDU** (basado en `peancor/moodle-mcp-server`):

| Operación Moodle | Comando EDU correspondiente |
|---|---|
| Crear/actualizar assignment | `/edu-publish-tp {N}` |
| Publicar recurso en sección | `/edu-publish-class {N}` |
| Crear quiz desde preguntas | `/edu-export-quiz-moodle {N}` |
| Listar alumnos del curso | interno — `student-simulator` puede leer matrícula real |
| Ver submissions de alumnos | futuro — Fase 3 |

**Requisitos:** Token de API Moodle con permisos de web services habilitados. Configuración en `_edu/config.yaml`.

#### Google Classroom MCP

Ver sección Google Workspace MCP más abajo. Usa `@google/mcp-server-gdrive` + Classroom API.

### Google Workspace MCP — Fase 1

**Costo:** $0 — todas las APIs de Google Workspace son gratuitas. Las universidades argentinas tienen Google Workspace for Education Fundamentals gratuito.

**Setup inicial:** `/edu-setup-google-workspace` — configura OAuth 2.0 y habilita las APIs necesarias.

| API Google | Uso en EDU | Comando |
|---|---|---|
| **Drive API** | Organizar carpetas por materia y año | automático al exportar |
| **Docs API** | Plan de estudio, retrospectiva, minutas como documentos institucionales | `/edu-export-plan-doc`, `/edu-export-retrospective-doc` |
| **Sheets API** | Matriz de cobertura, score pedagógico comparativo | `/edu-export-coverage-sheet` |
| **Slides API** | Filminas directamente en Google Slides (sin copiar/pegar) | `/edu-export-slides {N}` |
| **Classroom API** | Publicar TPs como assignments, material de clase | `/edu-publish-tp {N}`, `/edu-publish-class {N}` |
| **Forms API** | Generar formularios de evaluación desde `faq-anticipado.md` | `/edu-export-faq-form {N}` |
| **Calendar API** | Sincronizar cronograma de clases | `/edu-sync-calendar` |

**Principio de uso:** Markdown es siempre la **fuente de verdad** (en Git). Google Workspace es la **capa de sharing institucional** — solo se edita en el repo, nunca directamente en Google. Los cambios en Google se ignoran.

### Servicios externos (APIs directas)

| Servicio | Agente | Uso |
|---|---|---|
| **CrossRef API** | `reference-validator` | Verificación de DOIs |
| **Semantic Scholar API** | `academic-researcher`, `reference-validator` | Búsqueda y verificación de papers |
| **arXiv API** | `academic-researcher` | Acceso a preprints |
| **GitHub API** | `course-planner` | CI pipeline, Pages, Actions |
| **GitHub Actions** *(Fase 2)* | Motor CI | `ci-topic-pipeline.yml` — hooks automáticos por evento Git |
| **GitHub Pages** *(Fase 2)* | Motor de deploy | Dashboard estático de estado de la cursada |

### Integraciones con otros módulos BMAD

| Integración | Tipo |
|---|---|
| **Standalone** | Sin dependencias técnicas de otros módulos BMAD |
| **`core/party-mode`** | Disponible opcionalmente para brainstorming del docente sobre el plan |
| **`core/advanced-elicitation`** | Disponible opcionalmente |

### CLI / i18n

| Componente | Descripción |
|---|---|
| `edu-cli install --lang {code}` | Instalación con idioma de comunicación |
| `_edu/config.yaml` | Config local: `language`, `professor_profile`, `active_course`, `class_duration` |
| `_edu/i18n/{lang}/` | Strings de comunicación por idioma (solo capa visible) |
| `/edu-set-language {code}` | Cambiar idioma post-instalación |
| `/edu-setup-google-workspace` | Configurar OAuth 2.0 y habilitar APIs de Google |

### Comandos nuevos (Step 10)

| Comando | Fase | Acción |
|---|---|---|
| `/edu-plan-classes` | Plan | Elena propone distribución de temas en clases según duraciones; Adrián confirma |
| `/edu-set-topic-duration {N} {min}` | Ciclo tema | Cambia duración del tema N; dispara regeneración y reabre loops afectados |
| `/edu-validate-density {N}` | Guardrail | Verifica métricas de densidad cognitiva del tema N contra el perfil activo |
| `/edu-export-coverage-sheet` | Exportación | `cobertura-actual.md` → Google Sheets |
| `/edu-export-plan-doc` | Exportación | `plan-de-estudio.md` → Google Doc |
| `/edu-export-retrospective-doc` | Exportación | `retrospectiva-anual.md` → Google Doc |
| `/edu-export-slides {N}` | Exportación | `filminas.md` del tema N → Google Slides |
| `/edu-publish-tp {N}` | Publicación | `tp.md` del tema N → Assignment en Google Classroom |
| `/edu-publish-class {N}` | Publicación | Material de la clase N → Google Classroom |
| `/edu-export-faq-form {N}` | Exportación | `faq-anticipado.md` → Google Form de evaluación |
| `/edu-sync-calendar` | Exportación | `plan-de-estudio.md` → Google Calendar de la cursada |
| `/edu-setup-google-workspace` | Configuración | Setup inicial OAuth 2.0 + habilitación de APIs |

- Cada tema trabaja en branch propia: `tema/NN-nombre-del-tema`
- Cada corrección automática = commit con mensaje estandarizado:
  - `[writing-fixer] E01: concordancia corregida en minuta.md`
  - `[coherence-fixer] C02: terminología unificada en filminas.md y tp.md`
- Cierre de tema = merge a `main` (solo cuando todos los loops resueltos)
- Cierre de cursada = branches protegidas (solo lectura)
- El docente puede hacer `git revert` de cualquier corrección automática

---

## Integración con GitHub Copilot

El módulo genera y mantiene `.github/copilot-instructions.md` con contexto real de la cursada activa:
- Nombre de la materia y perfil del alumno
- Resumen del plan mínimo institucional
- Estilo académico esperado y vocabulario técnico de la materia
- Estado actual (temas completados, en progreso)

Comando: `/edu-update-copilot-context`

---

## Perfiles de profesor

| Perfil | Características |
|---|---|
| `profesor-teorico` | Rigor formal, definiciones precisas, ejemplos abstractos, bibliografía clásica |
| `profesor-practico` | Ejemplos concretos, ejercicios aplicados, casos reales |
| `profesor-socratico` | Material estructurado como preguntas que guían al alumno |
| `profesor-flipped` | Clase invertida: lectura previa + clase de ejercicio |
| `profesor-investigador` | Papers recientes, estado del arte, conexión con investigación activa |

---

## Re-planificación dinámica (adaptive-replan)

### Concepto

Desppués de cada clase, el docente registra lo que realmente ocurrió vs. lo planificado. Elena acumula ese delta y ajusta los temas restantes — densidad, duración, profundidad — para que el plan siga siendo alcanzable.

### Casos de uso

| Situación real | Ajuste sugerido por Elena |
|---|---|
| Tema 3 llevó 120 min en lugar de 90 | Comprimir Tema 4 o dividirlo en dos clases |
| Filminas demasiado densas — alumnos no siguieron el ritmo | Reducir `words_per_slide` para temas restantes |
| Sobró tiempo — poca información por filmina | Aumentar profundidad en próximos temas |
| Tema fue más fácil de lo esperado | Fusionar con el siguiente tema |

### Comandos

```
/edu-register-class-result {N} {minutos-reales} "{observaciones}"
    ← registra lo que realmente pasó en la clase del tema N

/edu-adjust-remaining-plan
    ← Elena analiza el delta acumulado y propone ajustes a los temas no dictados aún

/edu-apply-density-adjustment {desde-tema}
    ← aplica ajuste de perfil docente (densidad) a todos los temas a partir del N indicado
```

### Workflow: `adaptive-replan`

**Agente owner:** `course-planner` (Elena)
**Trigger:** opcional post-clase, o en cualquier momento
**Input → Proceso → Output:**
Registros de clases dictadas + plan restante → análisis de delta acumulado → propuesta de ajuste al plan + ajuste de perfil si corresponde

**Salida:** `ajuste-plan-{fecha}.md` — propuesta de cambios a temas restantes con justificación

---

## Encuestas guiadas a alumnos (student-feedback-loop)

### Concepto

La universidad ya entrega encuestas genéricas al final de la cursada. EDU genera encuestas **pedagógicamente específicas** por tema, diseñadas a partir del material real: las preguntas del `faq-anticipado.md` y los puntos de baja claridad del `score-pedagogico.md`.

### Diferencia con la encuesta institucional

| Encuesta institucional | Encuesta EDU |
|---|---|
| "¿La clase fue clara?" (escala 1-5) | "¿La diferencia entre OOP y FP quedó clara en la slide 6?" |
| Genérica para toda la cursada | Específica por tema y por concepto |
| Retroalimenta gestión académica | Retroalimenta el diseño del material |
| Se toma al final del cuatrimestre | Se puede tomar por tema, al cierre |

### El dato más valioso: calibración del simulador

El `student-simulator` predice qué conceptos van a generar confusión. La encuesta real mide qué concepts *realmente* generaron confusión. El delta entre predicción y realidad calibra el simulador para el año siguiente.

```
Simulador predijo: "confusión en slide 6 (OOP vs FP)"
Alumnos reales reportaron: "confusión en slide 9 (polimorfismo)"
→ Perfil "alumno-primer-año-promedio" se ajusta: agrega sensibilidad a polimorfismo
```

### Comandos

```
/edu-create-survey {N}
    ← genera encuesta guiada basada en faq-anticipado.md y score-pedagogico.md del tema N

/edu-export-survey {N} moodle
    ← publica encuesta como Quiz en Moodle

/edu-export-survey {N} forms
    ← publica encuesta como Google Form

/edu-analyze-survey {N}
    ← procesa respuestas recibidas y actualiza score-pedagogico.md

/edu-compare-survey-simulator {N}
    ← compara predicciones del alumno simulado vs. respuestas reales
    ← genera reporte de calibración del simulador
    ← actualiza perfil en _edu-memory/calibracion-simulador/
```

### Workflow: `student-feedback-loop`

**Agente owner:** `student-simulator` (procesa respuestas reales) + `test-runner` (consolida)
**Trigger:** al cerrar un tema o al final de la cursada
**Input → Proceso → Output:**
Respuestas de alumnos reales → análisis comparativo con predicciones del simulador → score actualizado + perfil calibrado

**Salidas nuevas:**
- `encuesta-{N}.md` — preguntas generadas
- `respuestas-{N}.md` — análisis de respuestas recibidas
- `calibracion-simulador-{N}.md` — delta predicción vs. realidad

### Extensión de `_edu-memory/`

```
_edu-memory/
  calibracion-simulador/              ← NUEVO
    {materia}-calibracion.md          ← delta simulador vs. alumnos reales acumulado
  historial-encuestas/                ← NUEVO
    {materia}-{año}-encuestas.md      ← respuestas reales procesadas
```

---

## Continuidad entre años

```
/edu-start-new-year {materia} {año}     ← lee retrospectiva + genera borrador del nuevo plan
/edu-copy-topic {tema} {año-origen}     ← copia sin cambios
/edu-adapt-topic {tema} {año-origen}    ← copia y abre ciclo de mejora
/edu-close-course {materia} {año}       ← genera retrospectiva-anual.md y protege carpeta
```

---

## Comandos completos del módulo

| Comando | Fase | Acción |
|---|---|---|
| `/edu-load-official-plan {ruta-pdf}` | Configuración | Extrae tópicos del PDF institucional |
| `/edu-confirm-official-plan` | Configuración | Bloquea el plan mínimo como referencia inmutable |
| `/edu-start-course` | Configuración | Inicia cursada nueva |
| `/edu-set-class-duration {minutos}` | Configuración | Configura duración de cada clase |
| `/edu-set-professor-profile {perfil}` | Configuración | Activa perfil docente |
| `/edu-create-professor-profile {nombre}` | Configuración | Define perfil personalizado |
| `/edu-compare-profiles {tema} {A} {B}` | Configuración | Genera el mismo tema con dos perfiles |
| `/edu-update-copilot-context` | Configuración | Regenera copilot-instructions.md |
| `/edu-research-plan` | Plan | Brainstorming académico web para armar el plan |
| `/edu-check-coverage` | Cobertura | Matriz de cobertura del plan mínimo |
| `/edu-design-topic {N}` | Ciclo tema | Diseña contenido y asigna tópicos del plan mínimo |
| `/edu-assign-topics {N} {IDs}` | Ciclo tema | Asigna tópicos explícitamente |
| `/edu-create-class {N}` | Ciclo tema | Genera minuta y filminas |
| `/edu-create-tp {N}` | Ciclo tema | Genera guía de prácticos |
| `/edu-validate-coverage {N}` | Validación | Verifica que el material desarrolle los tópicos asignados |
| `/edu-validate-writing {N}` | Loop 1 | Detecta errores de escritura |
| `/edu-fix-writing-auto {N}` | Loop 1 | Corrige [CRÍTICO] y [ERROR] automáticamente |
| `/edu-apply-writing-fixes {N}` | Loop 1 | Propone correcciones [MEJORA] con confirmación |
| `/edu-fix-writing {N} {ID}` | Loop 1 | Corrección manual puntual |
| `/edu-ignore-writing {N} {ID}` | Loop 1 | Descarta sugerencia [MEJORA] con justificación |
| `/edu-writing-history {N}` | Loop 1 | Historial de correcciones de escritura |
| `/edu-validate-coherence {N}` | Loop 2 | Detecta rupturas e inconsistencias |
| `/edu-fix-coherence-auto {N}` | Loop 2 | Repara [RUPTURA] e [INCOHERENCIA] automáticamente |
| `/edu-unify-terminology {N}` | Loop 2 | Unifica terminología entre documentos |
| `/edu-fix-coherence {N} {ID}` | Loop 2 | Corrección puntual de coherencia |
| `/edu-coherence-history {N}` | Loop 2 | Historial de correcciones de coherencia |
| `/edu-validate-references {N}` | Loop 3 | Estado de todas las referencias |
| `/edu-fix-reference {N} {ID} "{texto}"` | Loop 3 | Reescribe una referencia |
| `/edu-suggest-alternative {N} {ID}` | Loop 3 | Busca referencia alternativa verificada |
| `/edu-accept-reference {N} {ID}` | Loop 3 | Aprueba manualmente una referencia |
| `/edu-reject-reference {N} {ID}` | Loop 3 | Elimina una referencia |
| `/edu-validate-scope {N}` | Guardrail | Formalidad, scope y nivel académico |
| `/edu-fix-guardrail-auto {N}` | Guardrail | Reformula lenguaje informal automáticamente |
| `/edu-fix-guardrail {N} {ID}` | Guardrail | Corrección puntual de guardrail |
| `/edu-guardrail-history {N}` | Guardrail | Historial de correcciones de guardrail |
| `/edu-research-student-profiles {materia} {año}` | Testing | Investiga perfiles empíricos en literatura académica |
| `/edu-create-student-profile {nombre} {fuente}` | Testing | Crea o adopta un perfil de alumno |
| `/edu-test-topic {N} {perfil}` | Testing | Simula experiencia de un alumno |
| `/edu-test-topic {N} all` | Testing | Corre todos los perfiles |
| `/edu-close-topic {N}` | Cierre tema | Cierra el tema (bloqueado hasta resolver todos los loops) |
| `/edu-generate-course-plan` | Cierre cursada | Genera planificación consolidada |
| `/edu-propose-curriculum-change` | Cierre cursada | Propone cambios al plan |
| `/edu-close-course {materia} {año}` | Cierre cursada | Cierra cursada y genera retrospectiva |
| `/edu-start-new-year {materia} {año}` | Nuevo año | Inicia año nuevo desde el anterior |
| `/edu-copy-topic {tema} {año-origen}` | Nuevo año | Copia tema sin cambios |
| `/edu-adapt-topic {tema} {año-origen}` | Nuevo año | Copia y abre ciclo de mejora |
| `/edu-status {N}` | Navegación | Estado del tema N y próximo paso recomendado |
| `/edu-register-class-result {N} {min} "{obs}"` | Re-planificación | Registra resultado real de la clase del tema N |
| `/edu-adjust-remaining-plan` | Re-planificación | Elena propone ajustes a temas no dictados aún |
| `/edu-apply-density-adjustment {N}` | Re-planificación | Ajusta densidad del perfil docente desde el tema N |
| `/edu-create-survey {N}` | Encuestas | Genera encuesta guiada basada en faq-anticipado.md |
| `/edu-export-survey {N} moodle` | Encuestas | Publica encuesta como Quiz en Moodle |
| `/edu-export-survey {N} forms` | Encuestas | Publica encuesta como Google Form |
| `/edu-analyze-survey {N}` | Encuestas | Procesa respuestas y actualiza score-pedagogico.md |
| `/edu-compare-survey-simulator {N}` | Encuestas | Compara simulador vs. alumnos reales → calibra perfil |

---

## Escenarios de uso

### Escenario 1 — Primera vez (Adrián, semana 1 del cuatrimestre)

> Es domingo a la noche. Adrián tiene el PDF del programa de Programación 2 y las slides del año pasado en una carpeta. Mañana arranca el cuatrimestre.
>
> ```
> /edu-load-official-plan programa-prog2-2026.pdf
> ```
>
> En 40 segundos tiene `plan-minimo.md` con los 12 tópicos obligatorios extraídos del PDF. Lo revisa, confirma, y el archivo queda bloqueado.
>
> ```
> /edu-build-course-from-materials ./material-2025/
> ```
>
> Elena analiza las slides del año pasado, detecta que cubren 9 de los 12 tópicos, y propone un plan de 14 temas para cubrir los 3 faltantes y refrescar 2 que quedaron desactualizados. Adrián ajusta el orden de 2 temas. Son las 22:30 y ya tiene el plan del cuatrimestre.

**Lo que siente:** *"Hice en 30 minutos lo que antes me llevaba un fin de semana."*

---

### Escenario 2 — El momento de mayor valor (semana 3)

> Adrián terminó de diseñar el Tema 3. Los loops de calidad corrieron solos durante la noche (GitHub Actions).
>
> A la mañana abre el PR y ve:
> - Loop 1 ✅ — 3 errores de escritura corregidos automáticamente
> - Loop 2 ✅ — terminología unificada
> - Loop 3 ⚠️ — 1 referencia con DOI inválido, 2 alternativas sugeridas
> - Guardrail ✅ — 1 slide con densidad alta: 68 palabras (límite: 50 para su perfil `profesor-teorico`)
>
> Elige una de las referencias alternativas, acepta la corrección de densidad. Mergea el PR.
>
> Luego:
> ```
> /edu-test-topic 3 all
> ```
>
> El alumno simulado señala: *"Profe, en la slide 6 no entiendo por qué OOP sería mejor que imperativo para este ejemplo — parece arbitrario."*
>
> Adrián agrega una oración de justificación. Esa pregunta no lo va a agarrar desprevenido en clase.

**Lo que siente:** *"El módulo me prepara para las preguntas que no sé que me van a hacer."*

---

### Escenario 3 — El "aha" de Laura (semana 5)

> Laura tiene que preparar el TP del Tema 6 — su primer TP en la cátedra. Nunca lo hizo antes.
>
> ```
> /edu-create-tp 6
> ```
>
> Valeria genera el TP trazable a la minuta del Tema 6. Loop 1 corre automáticamente. El scope-check detecta que una consigna menciona "promesas en JavaScript" — tema que no se vio en clase.
>
> El guardrail la frena antes de que Adrián tenga que corregirla. Laura ajusta la consigna. El TP pasa todos los loops.
>
> Adrián lo revisa el viernes: cero correcciones. Primera vez en 3 años que un TP de auxiliar llega listo sin ir y volver.

**Lo que siente Laura:** *"No tuve que pedir validación constante."*
**Lo que siente Adrián:** *"Por fin el equipo produce material consistente."*

---

## Creative

### Tema de personalidad

**Equipo académico clásico** — los agentes son colegas que llevan años trabajando juntos en la misma cátedra. Tienen historia, tienen roce, tienen rutinas. El tono es riguroso pero humano.

### Catchphrases por agente

| Agente | Catchphrase |
|---|---|
| **Prof. Elena** | *"¿Está cubierto en el plan mínimo?"* — lo dice siempre, antes de cualquier decisión |
| **Lic. Marcos** | *"Eso está fuera de scope del Tema N."* — con seguridad inquebrantable |
| **Dr. Roberto** | *"Déjenme reformular eso..."* — nunca defiende su primer borrador |
| **Aux. Valeria** | *"¿Hay un ejercicio concreto para esto?"* — su pregunta refleja ante cualquier concepto abstracto |
| **Bib. Carlos** | Solo habla con DOIs. Nunca con URLs de blogs. |
| **student-simulator** | *"Profe, no entendí..."* — siempre en primera persona, nunca como reporte |

### Easter eggs

**1. `/edu-who-are-you`**
Cada agente responde presentándose en personaje:
> *"Soy el Dr. Roberto, docente de esta cátedra hace 15 años. He corregido más minutas de las que quisiera recordar. ¿En qué puedo ayudarte?"*

**2. Wikipedia como fuente**
Si el docente intenta incluir Wikipedia:
> 🔍 *Bib. Carlos: "Wikipedia no figura en mi lista de fuentes verificables. Puedo buscar el mismo concepto en Semantic Scholar si querés — dame un momento."*

**3. Al cerrar la primera cursada**
`/edu-close-course` por primera vez:
> 🎓 *"Felicitaciones, Prof. [nombre]. Primera cursada cerrada con EDU. Score pedagógico promedio: X/10. El año que viene arrancás con `/edu-start-new-year` — y ya no empezás de cero."*

**4. Cobertura 100% antes de fin de cursada**
> 📊 *plan-coverage-checker: "Cobertura: 100%. Todos los tópicos del plan mínimo cubiertos y validados. Podría tomar vacaciones."*

**5. `/edu-status` un domingo a la noche**
> *"Son las 22:00 del domingo. Clásico horario de preparación docente. ¿Empezamos por el Tema N o preferís que te dé el resumen del estado actual?"*

### Lore del módulo

Los agentes llevan años trabajando juntos en esta cátedra. Elena conoce cada error que cometió Roberto en sus primeras minutas. Marcos y Valeria tienen una tensión productiva sobre dónde termina teoría y empieza práctica. Carlos nunca habla de más — solo aparece cuando lo llaman.

**El estudiante simulado no tiene nombre fijo** — toma el nombre del perfil activo. En modo conversacional habla en primera persona con el tono del perfil: distinto si es "alumno-primer-año-promedio" que si es "alumno-avanzado-curioso".

---

## Roadmap / Extensibilidad futura

### Stack de interfaz (planificado para fases posteriores)

**Fase 1 — GitHub Pages (dashboard estático)**
- Action genera sitio estático en `docs/` con cada push a `main`
- Muestra: estado por tema, matriz de cobertura, score pedagógico, FAQ anticipado, links a PRs
- Sin frameworks pesados — Markdown → HTML estático (Astro / Eleventy)
- Solo lectura: el docente ve el estado, no ejecuta comandos desde acá

**Fase 2 — GitHub Actions como pipeline CI**

| Evento | Hook | Acción |
|---|---|---|
| `push` a `tema/**` | `on: push` | Loops 1-3 + guardrail automáticos |
| PR abierto | `on: pull_request` | Score pedagógico completo |
| PR aprobado | `on: pull_request_review` | `/edu-close-topic` preparado |
| Merge a `main` | `on: push to main` | Actualiza `cobertura-actual.md` + regenera Pages |
| Tag de cursada cerrada | `on: create tag` | `/edu-close-course` + retrospectiva |

**Fase 3 — Codespaces + Copilot Agent**
- Docente abre el repo en browser (sin instalar nada) desde Codespace
- UI → crea Issue → Copilot Coding Agent asignado → corre loops → abre PR automático
- PR = interfaz de revisión: checks por loop, diff de correcciones, comentarios del alumno simulado como review comments
- Merge del PR = `/edu-close-topic`

**Implicancia de diseño para Step 10:**
- Los agentes deben generar JSON de estado junto a los Markdown (`estado-tema.json`, `cobertura-actual.json`)
- Comandos deben retornar salida estructurada consumible por Actions y el dashboard
- Workflow CI dedicado: `ci-topic-pipeline.yml`

**Nota sobre Google Scholar:** permitido como índice de búsqueda para `academic-researcher`; la referencia final apunta al paper original (arXiv, IEEE, Springer, etc.), nunca a `scholar.google.com`.

### Convención de idioma en agentes (confirmada en Step 8)

- **Instrucciones internas del agente** (`persona`, `instructions`, `guardrails`): siempre en **inglés** — mayor precisión y robustez en LLMs
- **`communicationStyle`** (lo que el agente le dice al docente en pantalla): en el **idioma configurado**

### Fase 4 — Internacionalización (i18n) vía CLI

**Concepto:** al instalar el módulo por CLI y configurar Copilot, el docente elige el idioma de comunicación con un comando. Esto cambia únicamente la capa visible — las instrucciones internas del agente permanecen siempre en inglés.

```bash
# Durante la instalación
edu-cli install --lang es   # español (default)
edu-cli install --lang en   # inglés
edu-cli install --lang pt   # portugués
edu-cli install --lang fr   # francés

# O después de instalar
/edu-set-language {lang-code}
```

**Qué cambia con el idioma:**
- `communicationStyle` de todos los agentes → mensajes al docente en el idioma elegido
- Nombres de archivo de salida (`plan-minimo.md` → `minimum-plan.md` en inglés)
- Templates de documentos generados (minutas, TPs, retrospectivas)
- Mensajes de los loops y guardrails

**Qué NO cambia:**
- Instrucciones internas de los agentes (siempre en inglés)
- Guardrails (siempre en inglés)
- Comandos CLI y slash commands (siempre en inglés: `/edu-*`)
- Estructura de carpetas y nombres de variables internas

**Implementación sugerida:**
- Carpeta `_edu/i18n/{lang}/` con strings de comunicación por idioma
- El CLI genera `_edu/config.yaml` con `language: {lang-code}`
- Todos los agentes leen `{communication_language}` de ese config al inicio

**Idiomas prioritarios para v1:** `es` (español), `en` (inglés)

---

## Pasos pendientes del brief (retomar aquí)

- [x] **Step 5:** Nombre display = "EDU: Academic Course Production Suite"
- [x] **Step 5:** Personalidad = Equipo académico clásico (roles universitarios reales)
- [x] **Step 6:** Personas (Adrián y Laura, UNTDF) y user journey confirmados
- [x] **Step 7:** Propuesta de valor formalizada + contexto competitivo + roadmap de interfaz (Pages/Actions/Codespaces)
- [x] **Step 8:** Agentes — roster completo con nombres, roles universitarios, communicationStyle, sidecars, patrón de acceso Opción C confirmado
- [x] **Step 9:** Workflows — 4 core, 8 feature (incl. reopen-topic, adaptive-replan, student-feedback-loop), 3 utility. Loops independientes confirmados.
- [x] **Step 10:** Tools/MCP/integraciones — google-workspace-mcp, lms-mcp (Moodle/Classroom agnóstico), modelo tema/clase, métricas densidad cognitiva, comandos de exportación y publicación.
- [x] **Step 11:** Escenarios de uso — primera vez (Adrián semana 1), momento de mayor valor (PR con loops + alumno simulado), aha de Laura.
- [x] **Step 12:** Creative — catchphrases, 5 easter eggs, lore del equipo docente.
- [x] **Step 13:** Review y ajustes finales — LMS-agnóstico, Moodle MCP investigado, adaptive-replan, student-feedback-loop, calibración del simulador.
- [x] **Step 14:** Brief finalizado → `salida/bmb-creations/modules/module-brief-edu.md`

---

_Brief completado el 2026-03-06 por Matiasgel_
_Brief final: `salida/bmb-creations/modules/module-brief-edu.md`_
