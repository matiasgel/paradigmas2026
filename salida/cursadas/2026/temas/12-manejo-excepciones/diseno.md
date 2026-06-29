# Diseño de Clase — Tema 12: Manejo de Excepciones

> **Estado:** APROBADO · Corregido 2026-06-28
> **Diseñador:** Marcos v3 (topic-designer-v3) · Pipeline v3
> **Aprobado por:** Docente (implícito — avance solicitado)
> **Fecha:** 2026-06-04 · **Corrección:** 2026-06-28 (Dr. Roberto — class-writer)
> **Módulo:** IX | **Semana:** 12 | **Clase Nº 1 de 1**

---

## Datos del Tema

| Campo | Valor |
|-------|-------|
| Número | 12 |
| Nombre | Manejo de Excepciones |
| Duración | 120 minutos |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | Go, Kotlin, Rust |
| Módulo curricular | IX |

---

## Objetivos de Aprendizaje

Al finalizar esta clase el estudiante podrá:

1. **Definir** qué es una excepción, cómo se levanta y cómo se liga a un handler — siguiendo la terminología de Sebesta Cap. 14.
2. **Distinguir** el modelo de terminación del de reanudación y justificar por qué el primero domina los lenguajes modernos.
3. **Explicar** el mecanismo de propagación de excepciones a lo largo del call stack.
4. **Implementar** manejo de excepciones en TypeScript usando `try / catch / finally` y excepciones user-defined.
5. **Implementar** el enfoque funcional con `Result<T,E>` en TypeScript.
6. **Comparar** cómo Go, Kotlin y Rust abordan el manejo de errores, contrastando con TypeScript.
7. **Evaluar** las ventajas del enfoque funcional vs. imperativo según el contexto de uso.
8. **Identificar** por qué el manejo de excepciones es crítico en la programación agéntica.

---

## Bibliografía Principal

- **Sebesta**, *Concepts of Programming Languages*, Pearson 2019 — **Cap. 14** (Exception Handling and Event Handling), pp. 611–646. **Fuente primaria estructural.**
- **Gabbrielli & Martini**, *Programming Languages: Principles and Paradigms*, Springer 2023 — Cap. 7 §7.3.1 (Implementing Exceptions). Aporta perspectiva de implementación.
- **Louden & Lambert**, *Programming Languages: Principles and Practices*, 2012 — Cap. 9 §9.5 (Exception Handling). Contexto histórico: callbacks de error pre-try/catch.

---

## Plan de Filminas (17 slides + portada)

| F-# | Título | Tipo | Duración |
|-----|--------|------|----------|
| F-00 | Portada | portada | 2 min |
| F-01 | Pregunta de apertura | socratica | 3 min |
| F-02 | Objetivos de la clase | concepto-abstracto | 2 min |
| F-03 | ¿Qué es una excepción? (Sebesta §14.1) | concepto-abstracto | 8 min |
| F-04 | El problema antes de las excepciones | codigo | 6 min |
| F-05 | Historia: de PL/I a los lenguajes modernos | timeline | 5 min |
| F-06 | Terminación vs. reanudación | tabla-comparativa | 7 min |
| F-07 | Preguntas de diseño de lenguaje (Sebesta) | concepto-abstracto | 5 min |
| F-08 | try / catch / finally en TypeScript | codigo | 11 min |
| F-09 | Propagación por el call stack | diagrama | 7 min |
| F-10 | Excepciones user-defined en TypeScript | codigo | 8 min |
| F-11 | El enfoque funcional: Result\<T,E\> en TypeScript | codigo | 11 min |
| F-12 | Go: errors as values | codigo | 7 min |
| F-13 | Kotlin: sealed classes y try-expression | codigo | 7 min |
| F-14 | Rust: Result\<T,E\> y el operador `?` | codigo | 7 min |
| F-15 | Tabla comparativa: imperativo vs funcional, 4 lenguajes | tabla-comparativa | 8 min |
| F-16 | Excepciones en programación agéntica | concepto-mixto | 11 min |
| F-17 | Cierre y puntos clave | cierre | 5 min |

**Total:** 120 min (constraint absoluto)

---

## Distribución por Bloques

| Bloque | Filminas | Tema | Tiempo |
|--------|----------|------|--------|
| A | F-00 a F-07 | Fundamentos y conceptos (Sebesta-first) | 38 min |
| B | F-08 a F-11 | TypeScript: imperativo y funcional | 37 min |
| C | F-12 a F-15 | Contraste multi-lenguaje | 29 min |
| D | F-16 a F-17 | Agéntica + cierre | 16 min |

---

## Estrategia Pedagógica

- **Apertura socrática** (F-01): activar conflicto cognitivo con una pregunta real.
- **Sebesta-first** (F-03 a F-07): establecer vocabulario y preguntas de diseño antes de ver código.
- **Código en vivo** (F-08, F-10, F-11): TypeScript como lenguaje-ancla, ejemplos ejecutables en Playground.
- **Contraste lenguajes** (F-12 a F-15): después de TS consolidado, mostrar Go/Kotlin/Rust como decisiones de diseño distintas.
- **Conexión curricular** (F-16): excepciones como tema vivo en el propio toolchain de la cátedra (MCP server, publish_loop).

---

## Conexiones Curriculares

- **← Tema 11** (Estructuras de Control): las excepciones son un mecanismo de control de flujo no lineal.
- **→ Tema 13** (Abstracción Procedural y Modularidad): cómo las excepciones cruzan límites de módulos.
- **← Tema 5** (Mónadas en TypeScript): `Result<T,E>` es una mónada — el alumno ya conoce `map`/`flatMap`.
- **Contexto real**: el `edu-mcp-server` y `publish_loop.py` de esta cátedra son ejemplos directos.
