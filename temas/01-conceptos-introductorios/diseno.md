# Diseño — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Estado:** PENDIENTE DE APROBACIÓN DOCENTE
> **Agente:** Lic. Marcos (topic-designer)
> **Fecha:** 2026-03-09 — actualizado con material de `temas/tema1/` (ingesta PDFs)
> **Workflow:** topic-cycle / Step 1

---

## Datos del Tema

| Campo | Valor |
|-------|-------|
| Número | 01 |
| Nombre | Conceptos Introductorios + Intro a TypeScript |
| Módulo del plan mínimo | Módulo I |
| Semana | 1 |
| Clase | 1 de 2 |
| Duración total | **120 minutos** ← constraint de generación, no sugerencia |
| Lenguaje principal | TypeScript |
| Lenguaje puro de contraste | C (paradigma imperativo puro) |
| Perfil docente | profesor-teorico |

---

## Tópicos del Plan Mínimo cubiertos en este tema

| Tópico | Código plan mínimo |
|--------|--------------------|
| Razones e importancia del estudio de LP | Módulo I |
| Síntesis de los paradigmas de programación | Módulo I |
| Paradigma imperativo: conceptos fundamentales | Módulo I |
| Paradigma declarativo: conceptos fundamentales | Módulo I |
| Aportes de cada paradigma y dominios de aplicación | Módulo I |
| Criterios para estudio, análisis, selección y evaluación de lenguajes | Módulo I |
| Evolución de los LP — perspectiva histórica | Módulo I |
| Criterios de diseño e implementación de LP | Contenido mínimo #7 |
| Introducción a TypeScript como lenguaje multiparadigma *(reemplaza Kotlin)* | Módulo I adaptado |

> ⚠️ El tópico "Lenguajes característicos de los diferentes dominios" se cubre parcialmente aquí y se refuerza en temas 03–07.

---

## Estructura temporal (120 min)

### Bloque 1 — ¿Por qué estudiar lenguajes? (20 min)
- Costo de elegir mal un lenguaje en un proyecto real
- La proliferación de lenguajes: ¿cuántos hay y por qué?
- Perspectiva histórica express: FORTRAN → C → Smalltalk → Java → Python → TypeScript
- Criterios de evaluación de lenguajes (Sebesta, Cap. 1):
  - **Legibilidad** — ¿Es fácil de leer por otros programadores?
  - **Escribibilidad** — ¿Se puede expresar lo que se quiere sin pelear con el lenguaje?
  - **Confiabilidad** — ¿Las verificaciones formales y semánticas simplifican el testing?
  - **Portabilidad** — ¿El lenguaje es independiente de la máquina?
  - **Eficiencia** — No solo velocidad de ejecución; también costo de desarrollo y mantenimiento
  - **Entorno de programación** — Editores, depuradores, ecosistema
- **Punto de tensión:** ¿importa el lenguaje si la IA puede escribir en cualquiera?

### Bloque 2 — Los paradigmas: mapa general (25 min)
- Qué es un paradigma de programación
- **Factores que moldearon los paradigmas** (de las slides 2024):
  - Arquitectura de Von Neumann → paradigma imperativo ("variables" = celdas de memoria)
  - Evolución de metodologías de programación:
    - Hasta principios de los 70: programación "artesanal"
    - Años 70: análisis y diseño estructurado
    - Abstracción de datos (Simula, Ada)
    - Programación funcional (LISP)
    - Orientación a objetos (Smalltalk)
    - Multiparadigma (Python, TypeScript, Scala)
- Los 4 paradigmas fundamentales: imperativo, OO, funcional, lógico
- Tabla comparativa rápida: modelo de cómputo, unidad de abstracción, lenguajes representativos
  - Imperativo: C, C++, Go — estado mutable, asignación
  - OO: Smalltalk, Java, Dart — objetos y mensajes
  - Funcional: Haskell, LISP, Clojure — funciones como objetos de primera clase
  - Lógico: Prolog — relaciones y deducción
  - Multiparadigma: TypeScript, Python, Scala, F#
- Lenguajes puros vs. multiparadigma
- Dominios de aplicación: ¿cuándo usar cada uno?

### Bloque 3 — Paradigma imperativo: el baseline (20 min)
- **La conexión Von Neumann → imperativo** (clave conceptual):
  - Variables de programa = celdas de memoria
  - Instrucción de asignación = transferencia CPU ↔ memoria
  - Saltos condicional/incondicional = sentencias de control
  - Estado = conjunto de pares nombre-valor de variables en un instante
  - Un cómputo = una sucesión de estados
- Comandos, estado mutable, secuencia, selección, iteración
- Ejemplo en **C** (lenguaje puro imperativo): suma de un array
  ```c
  int suma(int arr[], int n) {
      int acc = 0;
      for (int i = 0; i < n; i++) acc += arr[i];
      return acc;
  }
  ```
- Discusión: ¿qué quedó implícito en ese código? (memoria, punteros, efecto)
- Por qué C es el mejor espejo del paradigma imperativo "puro"

### Bloque 4 — Intro a TypeScript como lenguaje multiparadigma (30 min)
- ¿Por qué TypeScript en 2026? Ecosistema, tipos, adopción, IA
- Setup mínimo: `tsc` / Deno Playground / editor online
- Mismo ejemplo en TypeScript:
  ```typescript
  const suma = (arr: number[]): number =>
    arr.reduce((acc, x) => acc + x, 0);
  ```
- Observar diferencias: tipos estáticos, función como valor, sin estado mutable explícito
- TypeScript como lenguaje con "aceleradores de paradigma": puede ser imperativo, funcional u OO según cómo se escriba
- Breve introducción al sistema de tipos: type annotations, inferencia

### Bloque 5 — IA Generativa y los paradigmas (15 min)
- Demo en vivo: pedirle a Copilot/Claude que implemente "sumar los elementos de una lista"
- Observar: ¿qué paradigma elige la IA por defecto? (¿imperativo con `for`? ¿funcional con `reduce`?)
- ¿Por qué los LLMs tienden al imperativo cuando no se especifica? (sesgo de entrenamiento)
- Cómo indicar el paradigma en el prompt: *"implementá en estilo funcional puro, sin mutación de estado"*
- Reflexión: conocer paradigmas = saber qué pedirle a la IA y cómo verificar lo que da

### Cierre (10 min)
- Mapa conceptual de la materia: cómo se conectan los 15 temas
- Adelanto de la Clase 2: Sintaxis y Semántica — el "idioma formal" de los lenguajes
- Recursos de instalación/acceso a TypeScript para la próxima clase

---

## Stack de Lenguajes

| Rol | Lenguaje | Uso en esta clase |
|-----|----------|-------------------|
| Principal | TypeScript | Bloques 4 y 5 |
| Contraste imperativo puro | C | Bloque 3 — solo lectura, sin instalación requerida |
| Demo IA | Copilot / Claude en vivo | Bloque 5 |

---

## Objetivos de Aprendizaje

Al finalizar la clase, el alumno podrá:
1. Justificar por qué el estudio de paradigmas es relevante en la era de IA generativa
2. Identificar los 4 paradigmas fundamentales y sus lenguajes representativos
3. Distinguir código imperativo de código funcional observando mutación de estado
4. Escribir una función básica con tipos en TypeScript
5. Describir qué paradigma produce la IA por defecto y cómo guiarla hacia uno específico

---

## Recursos y Bibliografía del Tema

- **Sebesta, R.W.** (2018). *Concepts of Programming Languages*, 12th ed. Pearson. Cap. 1 — "Preliminaries" *(temas/tema1/025-184.pdf)*
- **Louden & Lambert** (2011). *Programming Languages: Principles and Practice*, 3rd ed. Cap. 1 — "Introduction"
- **Gabbrielli & Martini** (2023). *Programming Languages: Principles and Paradigms*, 2nd ed. Cap. 1 — "Why Study Programming Languages?"
- **Schmidt & Runfola** (2025). *Liberating Logic in the Age of AI*. arXiv:2511.17696 — para el Bloque 5

### Material base 2024

> Las diapositivas de `temas/tema1/01 introduccion.pdf` (UNTDF, 2024) constituyen el material de partida para esta clase. La estructura de bloques fue diseñada para alinear y expandir ese material, actualizando las referencias de Kotlin a TypeScript y sumando el Bloque 5 de IA generativa.

---

## Notas para el Docente

- El Bloque 3 (C imperativo puro) es opcional si el tiempo aprieta — puede reducirse a 10 min mostrando solo el snippet
- El Bloque 5 (IA) es el más flexible: puede expandirse si hay buena discusión o comprimirse a 10 min
- Tener preparado el Deno Playground (https://playground.deno.land) como fallback si hay problemas de instalación
- El tópico "Introducción a Kotlin" del plan mínimo original fue reemplazado por TypeScript (ver `curriculum-proposal.md` aprobado)

---

## Decisión Docente

> ⬜ **APROBADO** — Proceder con `/edu_create_class`
> ⬜ **AJUSTAR** — Indicar cambios con `/edu_adjust_design`
