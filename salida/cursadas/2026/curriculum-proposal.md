# Propuesta de Cambio Curricular
## TypeScript como Lenguaje Principal + IA Generativa como Eje Transversal + Lenguajes Puros por Paradigma

> **Autor:** Prof. Ana — Revisora Curricular (EDU)
> **Fecha:** 2026-03-09
> **Estado:** ✅ APROBADA POR EL DOCENTE
> **Afecta:** `plan-borrador.md` únicamente
> **Restricción verificada:** No modifica ningún contenido de `plan-minimo.md`

---

## 1. Descripción del Cambio

Esta propuesta tiene **tres ejes simultáneos**, todos aprobados:

### 1.1 Eje A — TypeScript reemplaza a Kotlin como lenguaje principal

Kotlin queda fuera del cursado. TypeScript pasa a ser el lenguaje de referencia para todos los temas.

**Justificación de la elección:**
- Sistema de tipos estático robusto (structural typing, generics, union types, type guards) — ideal para enseñar tipos, binding y polimorfismo
- Soporta paradigma funcional real (inmutabilidad, funciones de orden superior, composición)
- OO completo con interfaces, herencia, mixins y genéricos
- Cobertura de IA generativa: top-2 junto con Python (los modelos están entrenados extensamente en TS)
- Ecosistema real: frontend, backend (Node/Deno/Bun), scripting de agentes IA

| Tema | Lenguaje anterior (Kotlin) | Lenguaje nuevo |
|------|--------------------------|----------------|
| Funcional | Kotlin | **TypeScript** |
| OO | Kotlin | **TypeScript** |
| Variables y tipos | Kotlin | **TypeScript** |
| Estructuras de control | Kotlin | **TypeScript** |
| Excepciones | Kotlin | **TypeScript** |
| Modularidad | Kotlin | **TypeScript** |
| Concurrencia | Kotlin coroutines | **TypeScript async/await + Promises** |

### 1.2 Eje B — Lenguajes puros por paradigma (ejemplos de contraste)
| 01 — Introducción | ¿Qué paradigma usa la IA por defecto? ¿Por qué el código generado tiende al imperativo? |

En cada tema de paradigma se incorporan **ejemplos en el lenguaje puro representativo**, para mostrar el paradigma en su forma más expresiva y sin compromisos multiparadigma.

| Paradigma | Lenguaje principal | Lenguaje puro de contraste | Propósito pedagógico |
|-----------|-------------------|--------------------------|---------------------|
| **Imperativo** | TypeScript | **C** | Memoria, punteros, control explícito del estado |
| **Funcional** | TypeScript | **Haskell** | Pureza total, lazy evaluation, tipos algebraicos, sin efectos secundarios |
| **Lógico** | Prolog | Prolog (ya es puro) | Unificación, backtracking, base de conocimiento |
| **OO** | TypeScript | **Smalltalk** | Mensaje como mecanismo central, todo es objeto |
| **Tipos** | TypeScript | **Haskell** (type system) | Inferencia de tipos, type classes, polimorfismo paramétrico |

Los ejemplos en lenguajes puros **no requieren instalación ni práctica** por parte del alumno — son ejemplos leídos en clase para contrastar con TypeScript.

### 1.3 Eje C — IA Generativa como eje transversal (15–20 min por clase)

Cada tema incorpora un bloque de cierre: *"¿Cómo razona, produce y falla la IA con este paradigma/construcción?"*, orientado a desarrollar pensamiento crítico sobre el código asistido por IA.

Python se usa exclusivamente en el bloque IA (y en el Tema 06) por su rol dominante en ecosistemas de IA generativa (LangChain, LlamaIndex, APIs de OpenAI/Anthropic).

---

## 2. Justificación Académica

### 2.1 El problema que resuelve

Los graduados de ciencias de la computación en 2026 usarán IA generativa como herramienta cotidiana. Sin una base conceptual sólida en paradigmas, no pueden:
- **Verificar** si el código generado es semánticamente correcto
- **Debuggear** errores que la IA introduce (especialmente en tipos, ámbito, concurrencia)
- **Escribir prompts** que explotan el paradigma correcto para el problema
- **Detectar alucinaciones** técnicas (código que compila pero es algorítmicamente incorrecto)

### 2.2 Evidencia académica

> ⚠️ **Nota de validación (2026-03-09):** Las referencias originales REF-01 y REF-02 fueron verificadas contra ACM Digital Library y arXiv. REF-01 tenía DOI válido pero mal atribuido; REF-02 tenía DOI inexistente (404). Ambas fueron reemplazadas por fuentes verificadas. Las referencias que siguen tienen URLs o DOIs confirmados.

**[REF-01]** Savelka, J., Agarwal, A., An, M., Bogart, C., & Sakr, M. (2023). *Thrilled by Your Progress! Large Language Models (GPT-4) No Longer Struggle to Pass Assessments in Higher Education Programming Courses*. ACM ICER 2023, pp. 78–92.
> Demuestra que GPT-4 puede aprobar con holgura los cursos de programación universitarios con evaluaciones tradicionales — haciendo obsoleto el modelo de evaluación centrado en sintaxis. Argumento clave para rediseñar curricula hacia comprensión semántica, razonamiento y verificación de código generado.
> DOI verificado: https://doi.org/10.1145/3568813.3600142

**[REF-02]** Schmidt, D. C., & Runfola, D. (2025). *Liberating Logic in the Age of AI: Going Beyond Programming with Computational Thinking*. arXiv:2511.17696 [cs.CY], noviembre 2025.
> Argumenta que lo que importa en 2025+ no es la fluidez en un lenguaje sino la capacidad de pensar computacionalmente, verificar resultados de IA y diseñar soluciones. Recomienda explícitamente reformar los curricula de ciencias de la computación para mantener los principios fundamentales mientras se incorpora IA. Directamente aplicable a una materia de paradigmas.
> DOI verificado: https://doi.org/10.48550/arXiv.2511.17696

**[REF-03]** Benedek, M., & Sziklai, B. R. (2025). *Impact of AI Tools on Learning Outcomes: Decreasing Knowledge and Over-Reliance*. arXiv:2510.16019 [cs.CY], octubre 2025.
> Experimento controlado en Corvinus University of Budapest: el uso irrestricto de IA generativa produce estudiantes desenganchados con bajo entendimiento real del material. Justifica el eje pedagógico de este cambio curricular: no prohibir la IA sino desarrollar pensamiento crítico sobre ella.
> DOI verificado: https://doi.org/10.48550/arXiv.2510.16019

**[REF-04]** Qiao, Y., Hundhausen, C., Haque, S., & Shihab, M. I. H. (2025). *Comprehension-Performance Gap in GenAI-Assisted Brownfield Programming: A Replication and Extension*. arXiv:2511.02922 [cs.SE], noviembre 2025.
> Estudio experimental con 18 estudiantes de posgrado: GitHub Copilot redujo el tiempo de tarea y aumentó los test cases pasados, pero NO mejoró la comprensión del código base. Gap comprensión-rendimiento: los estudiantes *pasan* más código con IA pero no *entienden* más. Justifica que paradigmas enseñe a leer y razonar sobre código ajeno.
> DOI verificado: https://doi.org/10.48550/arXiv.2511.02922

**[REF-05]** Stack Overflow Developer Survey 2024.
> Python ocupa el #1 en lenguajes más usados (51.9%) y TypeScript el #5 con tendencia ascendente. TypeScript es el lenguaje de facto para proyectos de mayor escala y es dominante en ecosistemas de agentes IA (Vercel AI SDK, LangChain.js, OpenAI SDK oficial). Python domina el scripting IA; TypeScript domina la ingeniería de software con IA.
> URL verificada: https://survey.stackoverflow.co/2024/

**[REF-06]** Wadler, P. (1992). *The essence of functional programming*. POPL 1992.
> Fundamento clásico del paradigma funcional puro (Haskell). Justifica el uso de lenguajes puros como herramienta pedagógica para enseñar el paradigma sin ruido multiparadigma. Referencia canónica para introducir mónadas y efectos en FP.
> DOI: https://doi.org/10.1145/143165.143169

---

## 3. Cambios Propuestos al Plan Borrador

### 3.1 Lenguaje principal y lenguajes de contraste por tema

| # | Tema | Lenguaje principal | Lenguaje puro de contraste | Bloque IA (15–20 min) |
|---|------|-------------------|--------------------------|----------------------|
| 01 | Conceptos Introductorios | TypeScript | C (imperativo puro) | ¿Qué paradigma genera la IA por defecto? |
| 02 | Sintaxis y Semántica | TypeScript (abstracto) | — | Errores semánticos en código generado. Prompts precisos |
| 03 | Funcional Intro | TypeScript | **Haskell** (pureza, sin efectos) | Inmutabilidad y funciones puras como prompt strategy |
| 04 | Funcional Avanzado | TypeScript | **Haskell** (lazy, composición) | IA y efectos secundarios ocultos. Composición como verificación |
| 05 | Mónadas | TypeScript | **Haskell** (Maybe, IO monad) | Errores de IA con manejo de efectos. Maybe/Result patterns |
| 06 | Funcional en Python | Python | — | Demo real: script Python → API LLM (OpenAI/Anthropic) |
| 07 | Paradigma Lógico | Prolog | Prolog (ya es puro) | LLMs vs. Prolog: inferencia aproximada vs. exacta. Alucinaciones lógicas |
| 08 | OO con TypeScript | TypeScript | **Smalltalk** (mensaje como mecanismo central) | IA y herencia: errores de diseño generado. Jerarquías en prompts |
| 09 | Variables y Binding | TypeScript | C (ámbito explícito) | Errores de ámbito en código generado. Variables globales silenciosas |
| 10 | Tipos de Datos | TypeScript | **Haskell** (algebraic types) | Type-driven prompting. Tipos como especificación para la IA |
| 11 | Estructuras de Control | TypeScript | C | Complejidad ciclomática en código generado |
| 12 | Excepciones | TypeScript | — | Error swallowing silencioso en código generado |
| 13 | Abstracción y Modularidad | TypeScript | — | Prompting para módulos reutilizables. Boundary design |
| 14 | Sistemas de Tipos | TypeScript | **Haskell** (type classes) | Contratos de tipos como guardrails del código generado |
| 15 | Concurrencia | TypeScript async/await | — | Race conditions y deadlocks silenciosos en código generado |

### 3.2 Estructura de cada diseno.md (actualizada)

Cada `diseno.md` incluirá una sección **"Stack de Lenguajes"** con:
- Lenguaje principal: TypeScript (o Python para Tema 06)
- Lenguaje puro de contraste: el indicado en la tabla (si aplica)
- Bloque IA: descripción del contenido del cierre
- Prompt de ejemplo para el tema
- Errores típicos del código generado con ese paradigma/construcción

---

## 4. Análisis de Impacto

### 4.1 Impacto en carga horaria
Cada bloque IA ocupa **15–20 min** de los 120 min por clase. Eso requiere comprimir levemente el contenido actual.

**Estrategia de compresión recomendada:** reducir ejemplos multi-lenguaje redundantes (donde ya hay 3-4 lenguajes de comparación, conservar 2).

### 4.2 Impacto en TPs
Se recomienda que al menos **2 TPs incorporen código generado por IA como punto de partida** — el alumno debe leerlo, identificar problemas paradigmáticos y corregirlos.

### 4.3 Impacto en evaluación
Ningún cambio en las instancias de evaluación del plan-mínimo. En el **Parcial 2** (presentación oral de lenguaje), se sugiere agregar como criterio opcional: análisis de cómo la IA generativa maneja ese lenguaje/paradigma.

### 4.4 Riesgo
- **Riesgo moderado — cambio de lenguaje principal:** TypeScript requiere preparar todos los ejemplos desde cero (Kotlin → TS). El contenido conceptual es idéntico, pero los ejemplos de código son nuevos.
- **Riesgo bajo — lenguajes puros:** Son solo ejemplos leídos en clase. No requieren instalación, práctica ni evaluación. Si el tiempo aprieta, se pueden reducir.
- **Riesgo bajo — bloque IA:** Si un tema queda ajustado de tiempo, el bloque IA se puede comprimir a 10 min sin afectar contenido obligatorio.

---

## 5. Cronograma de Implementación

| Acción | Cuándo |
|--------|--------|
| Actualizar `plan-borrador.md` (Kotlin → TypeScript en todos los temas) | Inmediato |
| Diseñar Tema 01 con stack TS + C + bloque IA | Esta semana |
| Diseñar Tema 02 con stack TS + bloque IA (sintaxis/semántica) | Esta semana |
| Preparar demo Python + API LLM para Tema 06 | Semana 4–5 |
| Incorporar ejemplos Haskell para temas funcionales (03–05, 10, 14) | Al diseñar cada tema |
| Incorporar ejemplos Smalltalk/Ruby para Tema 08 (OO) | Al diseñar Tema 08 |
| Revisar TPs para incluir "código generado como punto de partida" | Al crear cada TP |
| Evaluar impacto después del Parcial 1 | Semana 8 |

---

## 6. Decisión Docente

> ✅ **APROBADA** — Aplicar cambios a `plan-borrador.md`

**Observaciones del docente:**
- TypeScript reemplaza Kotlin como lenguaje principal en todos los temas
- Lenguajes puros de contraste por paradigma: Haskell (funcional/tipos), C (imperativo), Smalltalk (OO), Prolog (lógico)
- IA generativa como eje transversal con bloque de 15–20 min por clase
- Python para el bloque IA y Tema 06 (ecosistema LLM)

---

*Propuesta generada por Prof. Ana (curriculum-reviewer) — EDU Academic Course Production Suite*
*Basada en 5 fuentes académicas verificables (ver sección 2.2)*
