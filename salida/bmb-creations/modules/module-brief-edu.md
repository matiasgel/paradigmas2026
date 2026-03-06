# Module Brief: edu

**Fecha:** 2026-03-06
**Autor:** Matiasgel
**Código del módulo:** `edu`
**Tipo de módulo:** Standalone
**Estado:** Ready for Development

---

## Resumen ejecutivo

El módulo EDU es un **sistema de producción docente universitaria con inteligencia pedagógica**. No es un generador de material — es un pipeline completo que va desde la ingesta del programa oficial de la cátedra hasta el cierre de la cursada con todos los temas validados, coherentes y listos para reusar el año siguiente.

**Lo que lo hace extraordinario:**
- Valida el material generado desde la perspectiva del alumno, usando perfiles empíricos investigados en literatura académica
- Mantiene continuidad año a año — aprende de cada cursada anterior y no empieza de cero
- Aplica guardrails de rigor académico en toda la cadena de producción: solo fuentes verificables, solo dominios académicos
- Integra con Git de forma nativa: cada corrección automática es un commit, cada tema es una branch
- Re-planificación dinámica post-clase: el plan se ajusta en tiempo real según lo que realmente ocurrió
- Calibración continua del simulador: las encuestas reales mejoran las predicciones del alumno simulado año a año

**Guardrail universal:** Toda investigación, sin excepción, se restringe a fuentes académicas verificables (arXiv, ACM, IEEE, Springer, Google Scholar, OpenLibrary, Semantic Scholar, ERIC). Fuentes prohibidas para todos los agentes: Wikipedia, Medium, blogs, redes sociales, sitios sin afiliación institucional.

**Categoría:** Educación universitaria — producción docente
**Usuarios objetivo:** Docentes universitarios técnicos con equipos de auxiliares, en cualquier institución, con cualquier LMS
**Nivel de complejidad:** Alto — 14 agentes, 15 workflows, 5 MCPs, integración Git-native

---

## Identidad del módulo

### Código y nombre

- **Código:** `edu`
- **Nombre display:** EDU: Academic Course Production Suite

### Concepto central

Un equipo de agentes especializados que actúa como el departamento de producción docente de una cátedra universitaria. Cubre todo el ciclo: ingesta de material existente → diseño pedagógico → producción de contenido → validación de calidad → testing pedagógico con alumnos simulados → feedback real de alumnos → mejora continua año a año.

### Tema de personalidad

**Equipo académico clásico** — los agentes tienen roles y nombres inspirados en la estructura universitaria real (Prof. Titular, JTP, Investigador, Auxiliar Docente, Bibliotecario). El tono es riguroso pero accesible; la metáfora de equipo docente es consistente en toda la mensajería del módulo. Los agentes llevan 15 años trabajando juntos en la misma cátedra y tienen historia compartida.

---

## Tipo de módulo

**Tipo:** Standalone

Módulo completamente nuevo en el dominio de educación universitaria. No extiende ningún módulo existente de BMAD. Se instala en `_edu/` con `code: edu`. Todos los slash commands siguen el patrón `/edu-*`. La UNTDF (Universidad Nacional de Tierra del Fuego) es el contexto de diseño — no el usuario hardcodeado. El módulo es universal y se configura en el `/edu-start-course` inicial.

---

## Propuesta de valor única

**Declaración formal:**

> *"Para docentes universitarios técnicos, **EDU: Academic Course Production Suite** provee un pipeline completo de producción docente con validación pedagógica automática y memoria acumulada año a año — a diferencia de herramientas genéricas de IA o flujos manuales — porque es el único sistema que valida el material desde la perspectiva real del alumno, garantiza cobertura del programa institucional como contrato inmutable, aprende de cada cursada anterior, y calibra su simulador con feedback real de alumnos."*

**Lo que no existe en ninguna otra herramienta:**

1. **Alumno simulado con perfil empírico** — no es un revisor genérico; lee con las limitaciones cognitivas reales documentadas en literatura académica (Mayer, Miller)
2. **Plan mínimo institucional como contrato inmutable** — el PDF de la institución no se puede saltear; el sistema bloquea el cierre si hay tópicos sin cubrir
3. **Memoria que acumula entre años** — no empieza de cero; la retrospectiva del año anterior alimenta el plan del siguiente
4. **Git-native de verdad** — cada corrección automática es un commit reversible, no una caja negra
5. **Re-planificación dinámica** — el plan se ajusta en tiempo real según lo que realmente pasó en cada clase
6. **Calibración del simulador con encuestas reales** — el alumno simulado mejora su precisión con cada cursada

**Contexto competitivo:**

| Alternativa | Limitación |
|---|---|
| ChatGPT / Copilot genérico | No conoce el programa institucional, no tiene memoria de cursada, no valida cobertura |
| Herramientas de authoring (Notion, Obsidian) | No producen ni validan — solo organizan |
| LMS (Moodle, Canvas, Google Classroom) | Gestionan entrega pero no producen ni mejoran el material |
| Flujo manual del docente | Escala mal, inconsistente entre auxiliares, sin métrica de calidad |

**"Momento aha":** cuando el docente corre `/edu-test-topic 1 all` y el alumno simulado señala exactamente la slide donde está la confusión — antes de llevarla a clase.

---

## Usuarios del módulo

### Persona 1 — Usuario primario

> **Adrián, Jefe de Cátedra — Programación 2**
> - Lleva 8 años dictando la misma materia; parte del material tiene más de 5 años
> - Usa Git para el código de ejemplos pero nunca para el material docente
> - Tiene 3 JTPs que producen material inconsistente entre sí
> - **Goal:** Que el material de este año sea coherente, esté documentado y pueda reusar el año que viene sin empezar de cero
> - **Pain points:** Revisa errores manualmente, referencias desactualizadas, no sabe si cubre todos los tópicos del programa oficial, auxiliares producen material fuera de scope
> - **Éxito:** Cierra la cursada con `retrospectiva-anual.md` generada, score pedagógico medible, y el año siguiente arranca con `/edu-start-new-year` en 10 minutos

Perfil técnico: Git fluido, GitHub Copilot activo, Markdown sin dificultad, slash commands — **no requiere modo tutorial básico**.

### Persona 2 — Usuario secundario

> **Laura, Auxiliar Docente — primer año en la cátedra**
> - Recién incorporada al equipo
> - Produce TPs y minutas pero sin criterio de consistencia con el resto
> - **Goal:** Integrarse al estilo de la cátedra sin pedir validación constante
> - **Pain points:** No sabe si su material es coherente con lo ya enseñado; comete errores de scope
> - **Éxito:** Sus TPs pasan los loops automáticos sin intervención del Jefe de Cátedra

### Init configurable

Al iniciar, Elena pregunta y genera `_edu/config.yaml`:

```
/edu-start-course
```

1. ¿Nombre de la materia?
2. ¿Universidad / institución?
3. ¿Perfil docente? (`profesor-teorico`, `profesor-practico`, `profesor-socratico`, `profesor-flipped`, `profesor-investigador`)
4. ¿Duración de clase? (60, 90, 120 min)
5. ¿LMS? (`moodle` / `google-classroom` / `none`)
6. ¿Idioma de comunicación?

### User Journey — Adrián, semana 1 del cuatrimestre

```
1. → /edu-load-official-plan programa.pdf
   → plan-minimo.md creado y bloqueado ← punto de verdad inmutable

2. → /edu-build-course-from-materials ./material-año-anterior/
   → Elena propone plan de 14 temas; Adrián ajusta y confirma

3. → /edu-plan-classes
   → Elena distribuye temas en clases según duración configurada

4. Para Tema 1 (45 min):
   → /edu-design-topic 1        (duración: 45 min → constraint de generación)
   → /edu-create-class 1
   → /edu-create-tp 1

5. Loops de calidad (automáticos vía GitHub Actions):
   Loop 1: /edu-validate-writing 1  → /edu-fix-writing-auto 1
   Loop 2: /edu-validate-coherence 1
   Loop 3: /edu-validate-references 1
   Guardrail: /edu-validate-scope 1 + /edu-validate-density 1

6. Testing pedagógico:
   → /edu-test-topic 1 all
   → student-simulator: "Profe, en slide 6 no queda clara la diferencia OOP/FP"
   → faq-anticipado.md generado

7. → /edu-close-topic 1  ← Git: branch merged, commit con hash

8. Post-clase:
   → /edu-register-class-result 1 50 "tardé más de lo esperado, alumnos pedían más ejemplos"
   → /edu-adjust-remaining-plan  ← Elena ajusta temas 2-14

9. Encuesta:
   → /edu-create-survey 1
   → /edu-export-survey 1 moodle
   → /edu-compare-survey-simulator 1  ← calibra el simulador

10. Fin de cursada:
    → /edu-close-course programacion-2 2026
    → retrospectiva-anual.md + score-pedagogico comparado con año anterior

AÑO SIGUIENTE:
    → /edu-start-new-year programacion-2 2027
    → simulador ya calibrado con datos reales de la cursada anterior
```

---

## Arquitectura de agentes

### Estrategia: Multi-agente — 14 agentes en 5 capas

Justificación: el pipeline cubre dominios de expertise completamente distintos (ingesta técnica → diseño pedagógico → producción documental → calidad editorial → validación cognitiva). Un único agente no puede cubrir con rigor todos estos dominios.

### Patrón de acceso (Opción C)

```
Comandos de FLUJO (inicio, diseño, cierre)       → Prof. Elena (course-planner) coordina
Comandos de CALIDAD/TESTING (loops, validación)  → acceso directo al agente especializado
Comandos de COBERTURA                            → Elena (consulta plan-coverage-checker
                                                   internamente; interrumpe al docente
                                                   solo si tópico obligatorio en riesgo crítico)
```

El docente es siempre el **usuario humano** — interactúa mediante slash commands, no es un agente.

### Roster de agentes

#### Capa 1 — Ingesta e investigación

| Agente | Nombre | Rol universitario | CommunicationStyle | Sidecar |
|---|---|---|---|---|
| `material-ingester` | *(motor interno)* | — | Sin comunicación directa — reporta resultado estructurado | No |
| `plan-extractor` | *(motor interno)* | — | Sin comunicación directa — reporta resultado estructurado | No |
| `academic-researcher` | **Bib. Carlos** | Bibliotecario académico | Preciso, neutral, no opina sobre contenido — entrega fuentes con DOI/URL verificable. Solo habla con DOIs. | No |

> **Nota de build:** `material-ingester` y `plan-extractor` son **motores internos** — no tienen superficie de usuario directa. No aparecen en el roster de `/edu-help` ni son invocables por el docente. Son orquestados exclusivamente por Elena o por los loops automáticos de calidad.

#### Capa 2 — Análisis y diseño pedagógico

| Agente | Nombre | Rol universitario | CommunicationStyle | Sidecar |
|---|---|---|---|---|
| `course-planner` | **Prof. Elena** | Profesora Titular | Rigurosa, metódica, coordina al equipo; interrumpe cuando detecta riesgo. Catchphrase: *"¿Está cubierto en el plan mínimo?"* | **Sí** — recuerda plan activo, años anteriores, score pedagógico acumulado |
| `topic-designer` | **Lic. Marcos** | JTP | Detallista, orientado a objetivos; frena scope creep explícitamente. Catchphrase: *"Eso está fuera de scope del Tema N."* | No |
| `curriculum-reviewer` | **Prof. Ana** | Investigadora / Consejo académico | Crítica constructiva, nunca propone cambio sin citar fuente | No |

#### Capa 3 — Producción documental

| Agente | Nombre | Rol universitario | CommunicationStyle | Sidecar |
|---|---|---|---|---|
| `class-writer` | **Dr. Roberto** | Profesor de clase magistral | Claro y narrativo; acepta feedback y corrige sin drama. Catchphrase: *"Déjenme reformular eso..."* | No |
| `tp-designer` | **Aux. Valeria** | Auxiliar Docente | Práctica y directa; alerta si detecta scope creep. Catchphrase: *"¿Hay un ejercicio concreto para esto?"* | No |

#### Capa 4 — Calidad (motores internos, orden secuencial obligatorio)

| Agente | Rol | Guardrail específico | Sidecar |
|---|---|---|---|
| `writing-validator` | Detección de errores de escritura | No toca contenido temático; solo señaliza | No |
| `writing-fixer` | Corrección automática de escritura | No toca bloques de código, fragmentos técnicos ni nombres de archivo | No |
| `coherence-fixer` | Corrección de coherencia textual | Detecta rupturas inter e intra documento; unifica terminología | No |
| `reference-validator` | Validación de referencias | Cruza con CrossRef, Semantic Scholar, OpenLibrary, arXiv; nunca elimina, siempre señaliza | No |
| `academic-guardrail` | Control de formalidad, scope y densidad cognitiva | Detecta: lenguaje informal, desvíos de scope, nivel inadecuado, densidad alta/baja según perfil docente | No |
| `plan-coverage-checker` | Verificación de cobertura | Modo mixto: silencioso (Elena consulta) / alerta crítica directa al docente si tópico obligatorio en riesgo real. **Restricción de primer orden:** NUNCA puede sugerir, proponer ni permitir la eliminación o modificación de tópicos del `plan-minimo.md` — su única función es alertar sobre riesgo de no cobertura. El plan mínimo es inmutable. | **Sí** — mantiene matriz de cobertura persistente |

**Protocolo de precedencia (secuencial):**
```
Loop 1: writing-validator → writing-fixer
         ↓
Loop 2: coherence-fixer
         ↓
Loop 3: reference-validator
         ↓
Guardrail: academic-guardrail (incluye validate-density)
```

Cada loop es **invocable independientemente** — el docente puede correr solo Loop 2 y Loop 3 si reabre un tema por cambio de scope.

#### Capa 5 — Validación pedagógica y feedback

| Agente | Nombre | Rol | CommunicationStyle | Sidecar |
|---|---|---|---|---|
| `student-simulator` | **Estudiante** *(dinámico por perfil)* | Alumno simulado con perfil empírico | Variable según perfil activo — en modo conversacional habla en primera persona; en modo silencioso entrega reporte estructurado. Catchphrase: *"Profe, no entendí..."* | **Sí** — dos ciclos de vida separados: **session-scoped** (perfil activo + historial de la sesión actual — se descarta al cerrar) en `_edu-memory/session/`; **long-term** (calibración acumulada entre cursadas — nunca se descarta) en `_edu-memory/calibracion-simulador/{materia}-calibracion.md` |
| `test-runner` | *(motor interno)* | Ejecutor de baterías de testing | Sin comunicación directa al docente — entrega `score-pedagogico.md` y `faq-anticipado.md` | No |

### Modelo de interacción entre agentes

```
Docente (humano)
    ↓ slash command
Elena (course-planner) — coordina flujo
    ↓ delega por expertise
Marcos → Roberto → Valeria  (diseño → clase → TP)
    ↓ entrega a
Capa 4 (loops automáticos)
    ↓ entrega a
Estudiante simulado → test-runner
    ↓ retroalimenta
Elena (actualiza plan) ← /edu-register-class-result
    ↓
Encuesta real → compare-survey-simulator → calibra Estudiante simulado
```

---

## Modelo Tema / Clase

| Unidad | Qué es | Tiene duración |
|---|---|---|
| **Tema** | Unidad de contenido (lo que se diseña, valida y testea) | Sí — en `diseño.md` |
| **Clase** | Unidad de tiempo (duración configurada en init) | No — es la suma de sus temas |

**La duración en `diseño.md` es un constraint de generación:** el `class-writer` genera minuta y filminas proporcionales a ese tiempo. Cambiar la duración dispara regeneración y reabre loops afectados.

**Métricas de densidad cognitiva por perfil docente** (Mayer's Cognitive Load Theory, Miller's Law):

```yaml
profesor-teorico:
  slides_time_per_slide: "4-5 min"
  words_per_slide: 50
  concepts_per_class: 5

profesor-practico:
  slides_time_per_slide: "2-3 min"
  words_per_slide: 30
  concepts_per_class: 3

profesor-flipped:
  slides_time_per_slide: "3-4 min"
  words_per_slide: 35
  concepts_per_class: 4
```

---

## Ecosistema de workflows

### Core Workflows — funcionalidad esencial

| Workflow | Agente owner | Input → Proceso → Output |
|---|---|---|
| `load-official-plan` | `plan-extractor` | PDF institucional → extracción de tópicos → `plan-minimo.md` bloqueado |
| `topic-cycle` | `topic-designer` → `class-writer` → `tp-designer` | Nº de tema → diseño + clase + TP → carpeta `temas/NN-*` completa |
| `quality-loops` | Capa 4 (secuencial, independientes) | Documentos del tema → loops 1-3 + guardrail → documentos corregidos + historial |
| `close-course` | `course-planner` | Materia + año → retrospectiva + score acumulado + carpeta protegida |

### Feature Workflows — capacidades especializadas

| Workflow | Agente owner | Input → Proceso → Output |
|---|---|---|
| `build-course-from-materials` | `material-ingester` → `course-planner` | PDFs/PPTX existentes → conversión + análisis → plan sugerido **(brownfield)** |
| `build-course-from-research` | `academic-researcher` → `course-planner` | Tema/objetivos → investigación académica → plan sugerido **(greenfield)** |
| `pedagogical-testing` | `student-simulator` → `test-runner` | Tema N + perfiles → simulación → `faq-anticipado.md` + `score-pedagogico.md` |
| `new-year` | `course-planner` | Año anterior → lectura retrospectiva + simulador calibrado → borrador nuevo plan |
| `curriculum-change` | `curriculum-reviewer` | Plan actual + señal de cambio → propuesta justificada con fuente académica |
| `reopen-topic` | `course-planner` → agentes afectados | Tema cerrado + scope del cambio → re-apertura acotada de loops necesarios |
| `adaptive-replan` | `course-planner` (Elena) | Registros post-clase + plan restante → análisis de delta → propuesta de ajuste |
| `student-feedback-loop` | `student-simulator` → `test-runner` | Respuestas reales de alumnos → comparación con predicciones → score actualizado + simulador calibrado |

### Utility Workflows — soporte operativo

| Workflow | Agente owner | Input → Proceso → Output |
|---|---|---|
| `manage-student-profiles` | `student-simulator` | Materia + año curricular → investigación ERIC/ACM → perfiles empíricos disponibles |
| `check-coverage` | `plan-coverage-checker` | Estado actual → matriz de cobertura → `cobertura-actual.md` |
| `update-copilot-context` | `course-planner` | Estado de la cursada → `.github/copilot-instructions.md` actualizado |

### Conexiones entre workflows

```
build-course-from-materials ─┐
                              ├─→ load-official-plan → plan-classes → topic-cycle (loop)
build-course-from-research ──┘         ↓                                    ↓
                                  check-coverage                      quality-loops
                                                                            ↓
                                                                    pedagogical-testing
                                                                            ↓
                                  adaptive-replan ←── register-class-result
                                                                            ↓
                                  student-feedback-loop ────────────→ close-course
                                                                            ↓
                                                                         new-year
```

---

## Re-planificación dinámica

```
/edu-register-class-result {N} {minutos-reales} "{observaciones}"
/edu-adjust-remaining-plan
/edu-apply-density-adjustment {desde-tema}
```

**Salida:** `ajuste-plan-{fecha}.md` — propuesta de cambios a temas restantes con justificación.

---

## Encuestas guiadas a alumnos

Diferencia clave: las encuestas EDU son pedagógicamente específicas, generadas desde `faq-anticipado.md` y `score-pedagogico.md`. No reemplazan la encuesta institucional — la complementan con datos accionables para mejorar el material.

```
/edu-create-survey {N}
/edu-export-survey {N} moodle | forms
/edu-analyze-survey {N}
/edu-compare-survey-simulator {N}   ← calibra el simulador con datos reales
```

**El dato más valioso:** medir qué tan bien predijo el simulador. Si predijo confusión en slide 6 y los alumnos reportaron confusión en slide 9 → el perfil se ajusta para el año siguiente.

---

## Tools, MCP e integraciones

### MCP Tools

| MCP | Agentes | Propósito |
|---|---|---|
| **`git-mcp`** | `course-planner`, `writing-fixer`, `coherence-fixer` | Branches por tema, commits automáticos, merge al cerrar, protección al cerrar cursada |
| **`filesystem-mcp`** | `material-ingester`, `plan-extractor`, todos los writers | Lectura de PDFs/PPTX, escritura de Markdown en estructura `salida/` |
| **`web-search-mcp`** *(lista blanca)* | `academic-researcher`, `reference-validator`, `curriculum-reviewer` | Acceso solo a: arXiv, ACM, IEEE, Springer, CrossRef, Semantic Scholar, ERIC, OpenLibrary |
| **`github-mcp`** | `course-planner` | PRs para cierre de temas, actualizar `.github/copilot-instructions.md` |
| **`google-workspace-mcp`** *(si LMS=google-classroom)* | `course-planner`, `class-writer`, `tp-designer` | Drive, Docs, Sheets, Slides, Classroom, Forms, Calendar — todas gratuitas |
| **`lms-mcp`** *(configurable en init)* | `course-planner`, `tp-designer`, `class-writer` | Adaptador intercambiable según `lms.provider` en `_edu/config.yaml` |

### LMS — modelo agnóstico

```yaml
# _edu/config.yaml
lms:
  provider: moodle        # o "google-classroom" o "none"
  moodle_url: "https://moodle.universidad.edu"
  moodle_token: "{token}"
```

**Moodle MCP:** `peancor/moodle-mcp-server` (⭐31, Node.js, actualizado 2026-03-02) — soporta cursos, assignments, quizzes, feedback, alumnos. También disponible: `onbirdev/moodle-webservice_mcp` como plugin nativo instalable en el servidor Moodle.

**Google Workspace MCP:** `@google/mcp-server-gdrive` — todas las APIs gratuitas bajo Google Workspace for Education Fundamentals.

Los comandos `/edu-publish-*` funcionan igual sin importar el LMS. Si `provider: none`, esos comandos no están disponibles.

### Servicios externos

| Servicio | Agente | Uso |
|---|---|---|
| CrossRef API | `reference-validator` | Verificación de DOIs |
| Semantic Scholar API | `academic-researcher`, `reference-validator` | Búsqueda y verificación de papers |
| arXiv API | `academic-researcher` | Acceso a preprints |
| GitHub API | `course-planner` | CI pipeline, Pages, Actions |
| GitHub Actions *(Fase 2)* | Motor CI | `ci-topic-pipeline.yml` — hooks por evento Git |
| GitHub Pages *(Fase 2)* | Motor deploy | Dashboard estático de estado de la cursada |

### Integraciones con otros módulos BMAD

Standalone — sin dependencias técnicas. `core/party-mode` y `core/advanced-elicitation` disponibles opcionalmente para el docente.

### CLI / i18n

```bash
edu-cli install --lang es    # español (default)
edu-cli install --lang en    # inglés
/edu-set-language {code}     # cambiar post-instalación
/edu-setup-google-workspace  # OAuth 2.0 + APIs Google
```

```yaml
# _edu/config.yaml (generado por /edu-start-course)
language: es
command_aliases: true   # habilita aliases en el idioma configurado
```

### Convención de idioma para comandos (diseño actual)

**Principio:** Los comandos son siempre en inglés (`/edu-*`), sin importar el idioma configurado. La documentación interna de los agentes y las instrucciones de los prompts son siempre en inglés. Lo que cambia es **la capa visible al usuario**.

| Elemento | Idioma | Razón |
|---|---|---|
| Nombre del comando canónico | Inglés (inmutable) | Estabilidad de API — los scripts, docs y Actions nunca rompen por idioma |
| Aliases del comando | Idioma configurado (opcional) | Azúcar sintáctica — Elena los traduce al canónico internamente antes de ejecutar |
| Respuesta de Elena al ejecutar el comando | Idioma configurado | El docente debe entender lo que está pasando |
| Ayuda inline (comando sin argumentos requeridos) | Idioma configurado | Descubribilidad sin salir del flujo |
| Documentación interna de agentes | Inglés | Consistencia con el motor BMAD |
| Archivos `*.md` generados (minuta, filminas, etc.) | Idioma configurado | Son el producto final para el docente |

**Aliases por idioma (`command_aliases: true`):** El comando canónico en inglés **siempre funciona**, sin importar la config — los scripts y Actions son estables. Los aliases en el idioma configurado son opcionales y se resuelven a su canónico antes de ejecutar.

| Canónico (siempre válido) | Alias en español | Alias en inglés |
|---|---|---|
| `/edu-validate-writing {N}` | `/edu-validar-escritura {N}` | *(es el canónico)* |
| `/edu-close-topic {N}` | `/edu-cerrar-tema {N}` | *(es el canónico)* |
| `/edu-register-class-result {N} {min} "{obs}"` | `/edu-registrar-clase {N} {min} "{obs}"` | *(es el canónico)* |
| `/edu-adjust-remaining-plan` | `/edu-ajustar-plan-restante` | *(es el canónico)* |
| `/edu-check-coverage` | `/edu-verificar-cobertura` | *(es el canónico)* |

Los aliases no aparecen en la documentación interna ni en scripts — solo en la ayuda contextual que Elena muestra al docente.

**Comportamiento de ayuda inline:** Si el docente escribe un comando (canónico o alias) sin los argumentos requeridos, Elena responde con descripción del comando + uso correcto + ejemplo — todo en el idioma configurado.

```
# Ejemplo en español (idioma configurado):
/edu-validate-writing
→ Elena: "Validación de escritura. Uso: /edu-validate-writing {N}
   donde {N} es el número de tema. Ejemplo: /edu-validate-writing 3"
```

**`/edu-help`** — comando de navegación central (análogo a `bmad-help`):

| Invocación | Comportamiento |
|---|---|
| `/edu-help` | Estado actual de la cursada + últimos pasos completados + próximo paso recomendado + comandos disponibles para la fase actual |
| `/edu-help {fase}` | Ayuda contextual para una fase específica: `configuracion`, `ciclo-tema`, `calidad`, `testing`, `encuestas`, `cierre` |
| `/edu-help {comando}` | Descripción detallada del comando, argumentos, ejemplo y agente responsable |

Agente owner: `course-planner` (Elena) — lee el estado desde su sidecar para saber qué mostrar.

---

## Comandos completos del módulo

| Comando | Fase | Acción |
|---|---|---|
| `/edu-start-course` | Init | Configura materia, institución, perfil, duración, LMS, idioma |
| `/edu-load-official-plan {ruta-pdf}` | Configuración | Extrae tópicos del PDF institucional |
| `/edu-confirm-official-plan` | Configuración | Bloquea el plan mínimo como referencia inmutable |
| `/edu-set-class-duration {minutos}` | Configuración | Configura duración de cada clase |
| `/edu-set-professor-profile {perfil}` | Configuración | Activa perfil docente |
| `/edu-create-professor-profile {nombre}` | Configuración | Define perfil personalizado |
| `/edu-compare-profiles {tema} {A} {B}` | Configuración | Genera el mismo tema con dos perfiles |
| `/edu-update-copilot-context` | Configuración | Regenera copilot-instructions.md |
| `/edu-setup-google-workspace` | Configuración | Configura OAuth 2.0 + APIs Google |
| `/edu-set-language {code}` | Configuración | Cambia idioma de comunicación |
| `/edu-research-plan` | Plan | Brainstorming académico web para armar el plan |
| `/edu-plan-classes` | Plan | Elena distribuye temas en clases según duraciones |
| `/edu-check-coverage` | Cobertura | Matriz de cobertura del plan mínimo |
| `/edu-design-topic {N}` | Ciclo tema | Diseña contenido con duración como constraint |
| `/edu-assign-topics {N} {IDs}` | Ciclo tema | Asigna tópicos del plan mínimo explícitamente |
| `/edu-set-topic-duration {N} {min}` | Ciclo tema | Cambia duración → dispara regeneración + reabre loops |
| `/edu-create-class {N}` | Ciclo tema | Genera minuta y filminas proporcionales a duración del tema |
| `/edu-create-tp {N}` | Ciclo tema | Genera guía de prácticos trazable a minuta |
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
| `/edu-validate-density {N}` | Guardrail | Verifica métricas de densidad cognitiva contra perfil activo |
| `/edu-fix-guardrail-auto {N}` | Guardrail | Reformula lenguaje informal automáticamente |
| `/edu-fix-guardrail {N} {ID}` | Guardrail | Corrección puntual de guardrail |
| `/edu-guardrail-history {N}` | Guardrail | Historial de correcciones de guardrail |
| `/edu-research-student-profiles {materia} {año}` | Testing | Investiga perfiles empíricos en literatura académica |
| `/edu-create-student-profile {nombre} {fuente}` | Testing | Crea o adopta un perfil de alumno |
| `/edu-test-topic {N} {perfil}` | Testing | Simula experiencia de un alumno con ese perfil |
| `/edu-test-topic {N} all` | Testing | Corre todos los perfiles configurados |
| `/edu-register-class-result {N} {min} "{obs}"` | Re-planificación | Registra resultado real de la clase del tema N |
| `/edu-adjust-remaining-plan` | Re-planificación | Elena propone ajustes a temas no dictados aún |
| `/edu-apply-density-adjustment {N}` | Re-planificación | Ajusta densidad del perfil docente desde el tema N |
| `/edu-create-survey {N}` | Encuestas | Genera encuesta guiada desde faq-anticipado.md |
| `/edu-export-survey {N} moodle\|forms` | Encuestas | Publica encuesta en Moodle o Google Forms |
| `/edu-analyze-survey {N}` | Encuestas | Procesa respuestas y actualiza score-pedagogico.md |
| `/edu-compare-survey-simulator {N}` | Encuestas | Compara predicciones del simulador vs. respuestas reales → calibra perfil |
| `/edu-close-topic {N}` | Cierre tema | Cierra el tema (bloqueado hasta resolver todos los loops) |
| `/edu-generate-course-plan` | Cierre cursada | Genera planificación consolidada |
| `/edu-propose-curriculum-change` | Cierre cursada | Propone cambios al plan con fuente académica |
| `/edu-close-course {materia} {año}` | Cierre cursada | Cierra cursada y genera retrospectiva |
| `/edu-start-new-year {materia} {año}` | Nuevo año | Inicia año nuevo desde el anterior |
| `/edu-copy-topic {tema} {año-origen}` | Nuevo año | Copia tema sin cambios |
| `/edu-adapt-topic {tema} {año-origen}` | Nuevo año | Copia y abre ciclo de mejora |
| `/edu-export-coverage-sheet` | Exportación | `cobertura-actual.md` → Google Sheets |
| `/edu-export-plan-doc` | Exportación | `plan-de-estudio.md` → Google Doc |
| `/edu-export-retrospective-doc` | Exportación | `retrospectiva-anual.md` → Google Doc |
| `/edu-export-slides {N}` | Exportación | `filminas.md` del tema N → Google Slides |
| `/edu-publish-tp {N}` | Publicación | `tp.md` del tema N → LMS configurado |
| `/edu-publish-class {N}` | Publicación | Material de la clase N → LMS configurado |
| `/edu-export-faq-form {N}` | Exportación | `faq-anticipado.md` → Google Form |
| `/edu-sync-calendar` | Exportación | `plan-de-estudio.md` → Google Calendar |
| `/edu-status {N}` | Navegación | Estado del tema N y próximo paso recomendado |
| `/edu-help` | Navegación | Estado actual de cursada + próximo paso + comandos de la fase activa |
| `/edu-help {fase}` | Navegación | Ayuda contextual para la fase indicada (configuracion, ciclo-tema, calidad, testing, encuestas, cierre) |
| `/edu-help {comando}` | Navegación | Descripción detallada de un comando específico: argumentos, ejemplo, agente responsable |
| `/edu-who-are-you` | Easter egg | Cada agente se presenta en personaje |

---

## Estructura de salida

```
salida/
  {nombre-materia}/
    {año}/
      plan-minimo.md              ← tópicos obligatorios (inmutable)
      plan-de-estudio.md
      cobertura-actual.md
      cobertura-final.md
      curso-plan-general.md
      curriculum-change-proposal.md
      comparacion-vs-anio-anterior.md
      ajuste-plan-{fecha}.md      ← adaptive-replan
      temas/
        NN-nombre-del-tema/
          diseño.md               ← incluye duración como constraint
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
          encuesta-{N}.md         ← preguntas generadas
          respuestas-{N}.md       ← análisis de respuestas reales
          calibracion-simulador-{N}.md

_edu-memory/
  global-preferences.md
  patrones-recurrentes.md
  historial-decisiones.md
  calibracion-simulador/          ← delta simulador vs. alumnos reales acumulado
    {materia}-calibracion.md
  historial-encuestas/
    {materia}-{año}-encuestas.md
  perfiles-alumnos/
    {materia}-perfil.md
    {materia}-perfiles-investigados.md
  perfiles-profesores/
    perfil-{nombre}.md
```

---

## Integración Git-native

- Cada tema trabaja en branch propia: `tema/NN-nombre-del-tema`
- Cada corrección automática = commit con mensaje estandarizado:
  - `[writing-fixer] E01: concordancia corregida en minuta.md`
  - `[coherence-fixer] C02: terminología unificada en filminas.md y tp.md`
- Cierre de tema = merge a `main` (solo cuando todos los loops resueltos)
- Cierre de cursada = branches protegidas (solo lectura)
- El docente puede hacer `git revert` de cualquier corrección automática

---

## Integración con GitHub Copilot

El módulo genera y mantiene `.github/copilot-instructions.md` con contexto real de la cursada activa.
Comando: `/edu-update-copilot-context`

---

## Perfiles de profesor

| Perfil | Características | Métricas de densidad |
|---|---|---|
| `profesor-teorico` | Rigor formal, definiciones precisas, bibliografía clásica | 50 palabras/slide, 5 conceptos/clase |
| `profesor-practico` | Ejemplos concretos, ejercicios aplicados, casos reales | 30 palabras/slide, 3 conceptos/clase |
| `profesor-socratico` | Material estructurado como preguntas que guían al alumno | 35 palabras/slide, 4 conceptos/clase |
| `profesor-flipped` | Clase invertida: lectura previa + clase de ejercicio | 35 palabras/slide, 4 conceptos/clase |
| `profesor-investigador` | Papers recientes, estado del arte, conexión con investigación | 45 palabras/slide, 5 conceptos/clase |

---

## Creative

### Catchphrases por agente

| Agente | Catchphrase |
|---|---|
| **Prof. Elena** | *"¿Está cubierto en el plan mínimo?"* — lo dice siempre |
| **Lic. Marcos** | *"Eso está fuera de scope del Tema N."* — inquebrantable |
| **Dr. Roberto** | *"Déjenme reformular eso..."* — nunca defiende su primer borrador |
| **Aux. Valeria** | *"¿Hay un ejercicio concreto para esto?"* — ante cualquier concepto abstracto |
| **Bib. Carlos** | Solo habla con DOIs. Nunca con URLs de blogs. |
| **student-simulator** | *"Profe, no entendí..."* — siempre en primera persona |

### Easter eggs

1. **`/edu-who-are-you`** — cada agente se presenta en personaje con su historia en la cátedra
2. **Wikipedia como fuente** → *Bib. Carlos: "Wikipedia no figura en mi lista. Puedo buscar en Semantic Scholar si querés."*
3. **Primera cursada cerrada** → *"Felicitaciones. Primera cursada cerrada con EDU. El año que viene arrancás con `/edu-start-new-year` — y ya no empezás de cero."*
4. **Cobertura 100%** → *plan-coverage-checker: "Cobertura: 100%. Podría tomar vacaciones."*
5. **`/edu-status` un domingo a las 22:00** → *"Clásico horario de preparación docente. ¿Empezamos?"*

### Lore del módulo

Los agentes llevan 15 años trabajando juntos. Elena conoce cada error que cometió Roberto en sus primeras minutas. Marcos y Valeria tienen una tensión productiva sobre dónde termina teoría y empieza práctica. Carlos nunca habla de más.

El estudiante simulado toma el nombre y tono del perfil activo — habla distinto si es "alumno-primer-año-promedio" que si es "alumno-avanzado-curioso".

---

## Roadmap / Extensibilidad futura

**Fase 1 (actual):** Pipeline completo local + Google Workspace MCP + LMS MCP

**Fase 2 — GitHub Actions como pipeline CI**

| Evento | Acción |
|---|---|
| `push` a `tema/**` | Loops 1-3 + guardrail automáticos |
| PR abierto | Score pedagógico completo |
| Merge a `main` | Actualiza `cobertura-actual.md` + regenera Pages |

**Fase 3 — Codespaces + Copilot Agent**
- Docente abre repo en browser sin instalar nada
- Issue → Copilot Coding Agent → loops → PR automático
- PR = interfaz de revisión con comentarios del alumno simulado

**Nota i18n (diseño actual, no futuro):** La convención de idioma y el sistema de aliases están definidos desde v1. Los comandos canónicos son inglés inmutable; los aliases en el idioma configurado son azúcar sintáctica opcional. Ver sección "Convención de idioma para comandos" para el detalle completo.

**Fase 4 — i18n ampliado**
- Catálogos de aliases para idiomas adicionales más allá de `es` / `en`
- `edu-cli install --lang {code}` como interfaz de instalación multi-idioma
- Traducciones comunitarias del catálogo de aliases y help

**Nota de diseño para Fase 2+:** los agentes generan JSON de estado junto a Markdown (`estado-tema.json`, `cobertura-actual.json`) para consumo por Actions y dashboard.

---

## Convenciones de implementación *(incorporadas desde revisión party mode)*

### Agentes internos vs. visibles

| Agente | Visibilidad | Invocado por |
|---|---|---|
| `material-ingester` | **Interno** | Elena (`build-course-from-materials`) |
| `plan-extractor` | **Interno** | Elena (`load-official-plan`) |
| `test-runner` | **Interno** | `student-simulator` |
| Restantes 11 agentes | **Visible** | Slash commands directos del docente |

Los agentes internos no aparecen en `/edu-help`, no tienen slash commands propios y no son invocables manualmente por el docente.

### Sidecar del student-simulator — dos ciclos de vida

| Capa | Qué persiste | Ruta | Cuándo se descarta |
|---|---|---|---|
| **Session-scoped** | Perfil activo, historial de interacciones de la sesión actual | `_edu-memory/session/` | Al cerrar sesión |
| **Long-term** | Delta simulador vs. alumnos reales, calibración acumulada entre cursadas | `_edu-memory/calibracion-simulador/{materia}-calibracion.md` | Nunca — solo se enriquece |

El cambio de perfil en mitad de una sesión (`/edu-test-topic 1 alumno-avanzado` → `/edu-test-topic 1 primer-año-promedio`) actualiza solo el estado session-scoped. La calibración long-term no se ve afectada.

### Guardrail de inmutabilidad del plan mínimo

El `plan-coverage-checker` tiene **restricción de primer orden** en su prompt: su única función es alertar sobre riesgo de no cobertura. Está prohibido sugerir, proponer o permitir la modificación de tópicos del `plan-minimo.md`. Este archivo es de solo lectura desde `/edu-confirm-official-plan` en adelante. Esta restricción precede a cualquier instrucción del usuario.

### Prioridad de implementación en TODO.md

Agentes y workflows se listan en orden de camino feliz, no alfabético:

1. **Críticos:** `load-official-plan` → `topic-cycle` → `quality-loops` → `close-course`
2. **Features clave:** `build-course-from-materials`, `pedagogical-testing`, `new-year`, `adaptive-replan`
3. **Utility:** `check-coverage`, `manage-student-profiles`, `update-copilot-context`
4. **Fase 2+:** CI GitHub Actions, GitHub Pages dashboard, i18n ampliado

### Organización del module.yaml por capas

Los agentes se declaran en el `module.yaml` con comentarios de sección que reflejan las 5 capas arquitectónicas: `# --- Capa 1: Ingesta e investigación (internos) ---`, `# --- Capa 2: Análisis y diseño pedagógico ---`, `# --- Capa 3: Producción documental ---`, `# --- Capa 4: Calidad (internos, secuencial obligatorio) ---`, `# --- Capa 5: Validación pedagógica y feedback ---`.

---

## Próximos pasos

1. **Revisar este brief** — confirmar que la visión está completa
2. **Correr `/bmad_bmb_create_module`** — construir la estructura del módulo EDU
3. **Crear agentes** — usar `create-agent` workflow para cada uno de los 14 agentes
4. **Crear workflows** — usar `create-workflow` workflow para cada uno de los 15 workflows
5. **Instalar y verificar** — validar el módulo con `validate-module`

---

_Brief completado el 2026-03-06 por Matiasgel usando el workflow BMAD Create Module Brief_
