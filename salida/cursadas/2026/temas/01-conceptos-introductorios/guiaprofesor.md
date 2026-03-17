# Guía del Profesor — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Docente:** Matías Gel
> **Institución:** Universidad Nacional de Tierra del Fuego — Instituto IDEI
> **Materia:** Paradigmas y Lenguajes de Programación 2026
> **Agente:** Dra. Sofía (study-guide-writer)
> **Fecha de generación:** 2026-03-17
> **Semana / Clase:** Semana 1 · Clase 1 de 2
> **Duración:** 120 minutos
> **Estado:** GENERADA — requiere revisión docente

---

## 1. Portada del Tema

| Campo | Valor |
|-------|-------|
| Número de tema | 01 |
| Nombre completo | Conceptos Introductorios + Intro a TypeScript |
| Módulo del plan mínimo | Módulo I |
| Tipo de clase | Teórica con demo en vivo |
| Lenguaje principal | TypeScript |
| Lenguaje de contraste | C (paradigma imperativo puro) |
| Perfil docente | profesor-teorico |
| Filminas | `filminas.md` → slides/ |
| Guía del alumno | `guia-estudio.md` |
| TP | `tp.md` (quiz tipo GIFT: `tp-quiz.gift`) |
| Estado del tema | **cerrado** |

---

## 2. Objetivos y Competencias

### 2.1 Objetivos generales del tema

Al concluir esta clase el alumno debe poder:

1. **Justificar** por qué el estudio de paradigmas es relevante incluso en la era de la IA generativa.
2. **Identificar** los cuatro paradigmas fundamentales (imperativo, funcional, lógico, OO) y reconocer sus lenguajes representativos.
3. **Distinguir** código imperativo de código funcional observando la presencia o ausencia de mutación de estado.
4. **Escribir** una función básica con tipos en TypeScript en ambos estilos (imperativo y funcional).
5. **Aplicar** el loop "trust but verify" para verificar código generado por IA: identificar el paradigma utilizado, detectar errores semánticos y reformular el prompt.

### 2.2 Tópicos del plan mínimo cubiertos

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

> ⚠️ "Lenguajes característicos de los diferentes dominios" se cubre parcialmente aquí y se refuerza en temas 03–07.

### 2.3 Competencias transversales

- Pensamiento crítico aplicado a la evaluación de herramientas tecnológicas.
- Uso reflexivo de IA generativa con supervisión basada en conocimiento de dominio.
- Capacidad de reconocer trade-offs entre paradigmas (legibilidad vs. eficiencia, pureza vs. flexibilidad).

---

## 3. Plan de Clase Detallado

### Preparación previa (−10 min antes de clase)

- [ ] Abrir **Deno Playground**: https://playground.deno.land
- [ ] Tener abierto **Copilot Chat** (VS Code) o **Claude** (https://claude.ai) para la demo del Bloque 5
- [ ] Verificar proyector: filminas `slides/` cargadas y visibles
- [ ] Preparar buffer del editor con snippets de C y TypeScript (Bloques 3 y 4)
- [ ] **Optativo:** escribir los 4 paradigmas en el pizarrón antes de que entren los alumnos — genera curiosidad

---

### APERTURA — Bienvenida a la materia (5 min, fuera del tiempo de bloques)

**Filmina activa:** F-00 (portada)
**Tono:** cálido y situador — no empezar con teoría todavía

- Presentarse: nombre, años en la cátedra, cómo prefieren que le digan.
- Frase de anclaje: *"Esta es una materia que parece rara al principio — ¿para qué estudiar lenguajes si ya saben programar? La clase de hoy responde esa pregunta."*
- Dinámica de las clases: teoría con ejemplos, demos en vivo, preguntas siempre bienvenidas.
- Mencionar el cambio de lenguaje principal: TypeScript reemplaza a Kotlin este año.

---

### BLOQUE 1 — ¿Por qué estudiar lenguajes de programación? (20 min)

**Filminas:** F-01 · F-02 · F-03 · F-04 · F-05
**Objetivo:** Justificar el valor de la materia desde un ángulo práctico y provocador.

| Subbloque | Duración | Filmina | Actividad |
|-----------|----------|---------|-----------|
| ¿Para qué estudiar lenguajes de programación? | 2 min | F-01 | Preguntar cuántos lenguajes existen; dejar que respondan |
| El costo de elegir mal | 5 min | F-02 | Narrar caso startup Node.js → Python; conectar con modelo mental |
| Perspectiva histórica express | 7 min | F-03 | Recorrer timeline FORTRAN→TypeScript con justificación por cada hito |
| Criterios de evaluación (Sebesta) | 6 min | F-04 | Presentar los 6 criterios; ejemplo de tensión Python vs. C |
| Punto de tensión IA (dejar abierto) | 2 min | F-05 | Plantear sin resolver — retomar en Bloque 5 |

**Frase clave de apertura del bloque (F-01):**
> *"¿Cuántos lenguajes de programación existen hoy?"* — Respuesta real: más de 700 con uso documentado.

**Tensión a sembrar en F-05 (no resolver todavía):**
> *"¿Importa el lenguaje si la IA puede escribir en cualquiera? ¿O precisamente por eso importa más saber evaluarlos?"*
> — Retomar explícitamente al abrir el Bloque 5.

---

### BLOQUE 2 — Los paradigmas: mapa general (25 min)

**Filminas:** F-06 · F-07 · F-08 · F-09 · F-10
**Objetivo:** Dar el mapa completo de paradigmas con base teórica sólida.

| Subbloque | Duración | Filmina | Actividad |
|-----------|----------|---------|-----------|
| ¿Qué es un paradigma? | 4 min | F-06 | Definición conceptual; Java vs. C# (mismo paradigma, sintaxis diferente) |
| Factores históricos que formaron los paradigmas | 6 min | F-07 | Von Neumann → imperativo; cronología metodológica comprimida |
| El cuello de botella de Von Neumann | 5 min | F-08 | Pregunta disparadora sobre cómputo no-Von Neumann |
| Los 4 paradigmas fundamentales (tabla) | 8 min | F-09 | Tabla comparativa en filmina dedicada |
| Lenguajes puros vs. multiparadigma + dominios | 2 min | F-10 | Rápido; conectar con temas 03–07 |

**Tabla a presentar en F-09:**

| Paradigma | Base formal | Unidad | Estado | Ejemplos |
|-----------|-------------|--------|--------|----------|
| Imperativo | Máquina de Von Neumann | Instrucción | Mutable | C, Go, Pascal |
| OO | Imperativo + encapsulamiento | Objeto / mensaje | Mutable (encapsulado) | Java, C#, Dart |
| Funcional | Cálculo lambda (Church, 1936) | Función | Inmutable | Haskell, Clojure, LISP |
| Lógico | Lógica simbólica (resolución) | Relación / hecho | Sin estado | Prolog |

**Punto docente a marcar:** El OO es extensión del imperativo, no nació de cero. Funcional y lógico tienen raíces matemáticas previas a las primeras computadoras.

---

### BLOQUE 3 — Paradigma imperativo y máquina abstracta (20 min)

**Filminas:** F-11 · F-12 · F-13 · F-14
**Objetivo:** Conectar máquinas abstractas con código real. Dar rigor sin perder claridad.

| Subbloque | Duración | Filmina | Actividad |
|-----------|----------|---------|-----------|
| La escalera de abstracciones | 5 min | F-11 | Diagrama en filmina: LC-3 → C → Java/TS → Frameworks |
| La conexión Von Neumann → código imperativo | 5 min | F-12 | Variable = celda de memoria; asignación = transferencia CPU→mem |
| Ejemplo comparativo LC-3 / C / TypeScript | 8 min | F-13 | Mostrar LC-3 brevemente; detenerse en C; anticipar TypeScript |
| Máquina abstracta, interpretación y compilación | 2 min | F-14 | Síntesis Gabbrielli Cap. 1 — anticipar Bloque 4 |

**⚠️ Aclaración explícita a dar en F-13:**
> *"Este código LC-3 NO entra al TP. Está para que vean lo que C ya les abstrae."*
Este punto es crítico para el perfil de alumno ansioso (ver FAQ F01 en `faq-anticipado.md`).

**Escalera visual para pizarrón / F-11:**
```
LC-3 (ensamblador)      — Nivel 0: legibilidad nula, completo control
       ↕ abstracción
C, Pascal, Go            — Nivel 1: estructura, tipos, funciones
       ↕ abstracción
Java, Python, TypeScript — Nivel 2: GC, tipado, ecosistema
       ↕ abstracción
React, Django, Rails     — Nivel 3: frameworks
```

---

### BLOQUE 4 — Intro a TypeScript como lenguaje multiparadigma (30 min)

**Filminas:** F-15 · F-16 · F-17 · F-18 · F-19 · F-20
**Objetivo:** TypeScript como ejemplo vivo de los conceptos teóricos. Primera escritura de código.

| Subbloque | Duración | Filmina | Actividad |
|-----------|----------|---------|-----------|
| ¿Por qué TypeScript en 2026? | 4 min | F-15 | Argumentos: ecosistema, tipos, IA, multiparadigma |
| Pipeline TS como máquina intermedia | 8 min | F-16 | Dibujar `.ts → tsc → .js → V8/Deno → CPU` en pizarrón |
| Demo: versión imperativa + funcional | 10 min | F-17+F-18 | Deno Playground — tipear en vivo si el tiempo lo permite |
| Sistema de tipos básico | 8 min | F-19 | Tipos básicos; mostrar error de tipo en vivo |

**Setup Deno Playground (paso a paso):**
1. Abrir https://playground.deno.land en el proyector
2. `Ctrl+A` → `Delete` para borrar el código de ejemplo por defecto
3. Pegar (o tipear) los snippets de abajo
4. Ejecutar con ▶ **Run** o `Ctrl+Enter`
5. Output aparece en el panel inferior derecho

**Fallback:** https://www.typescriptlang.org/play (si Deno Playground no carga)

**Demo Paso 1 — Versión imperativa (F-17):**
```typescript
function sumaAbs(arr: number[]): number {
    let acc = 0;
    for (let i = 0; i < arr.length; i++) {
        acc += arr[i] < 0 ? -arr[i] : arr[i];
    }
    return acc;
}
console.log(sumaAbs([3, -1, 4, -1, 5])); // Output: 14
```

**Demo Paso 2 — Versión funcional (F-18):**
```typescript
const sumaAbs = (arr: number[]): number =>
    arr.map(x => Math.abs(x))
       .reduce((acc, x) => acc + x, 0);
console.log(sumaAbs([3, -1, 4, -1, 5])); // Output: 14
```

**Punto clave a marcar en el contraste:**
- Imperativa: `let acc` mutable + loop con índice = estado que cambia = paradigma imperativo
- Funcional: sin `let`, sin loop, `map`+`reduce` como funciones de orden superior = paradigma funcional
- Mismo resultado, distinto modelo mental

**Demo error de tipos (F-19):**
```typescript
sumaAbs(["hola", "mundo"]);
// Error: Argument of type 'string[]' is not assignable to parameter of type 'number[]'
```

**Pregunta para los alumnos (registrar respuestas en pizarrón):**
> *"¿Cuál versión les resulta más legible? ¿Cuál más fácil de escribir? ¿Coinciden sus respuestas?"*

---

### BLOQUE 5 — IA Generativa y los paradigmas (15 min)

**Filminas:** F-21 · F-22 · F-23 · F-24 · F-25 · F-26
**Objetivo:** Conectar los fundamentos de la materia con el contexto actual de la IA.

| Subbloque | Duración | Filmina | Actividad |
|-----------|----------|---------|-----------|
| Cierre pregunta F-05 + cambio de rol del programador | 4 min | F-21 | Datos Schmidt & Runfola (2025): 20/50/30% |
| La jerarquía de proficiencia en IA | 3 min | F-22 | Literacy → Fluency → Mastery |
| Demo en vivo: 3 prompts con la IA | 6 min | F-23+F-24+F-25 | Copilot Chat o Claude — ver resultados en vivo |
| El loop "trust but verify" | 2 min | F-26 | Esquema de 5 pasos |

**Apertura del bloque — retomar lo sembrado en F-05:**
> *"En el Bloque 1 dejamos una pregunta abierta: ¿importa el lenguaje si la IA puede escribir en cualquiera? Ahora la respondemos: importa más que nunca, pero por razones distintas."*

**Split de tiempo antes/después de IA (F-21):**
| Rol | Antes (pre-IA) | Hoy (con IA generativa) |
|-----|---------------|------------------------|
| Codificación manual + depuración | 70% | 20% |
| Prompting, supervisión y orquestación | — | 50% |
| Formulación del problema | 30% | 30% |

**Prompts para la demo en vivo:**

*Prompt 1 (F-23) — sin restricción de paradigma:*
```
Escribí en TypeScript una función que devuelva la suma
de los valores absolutos de una lista de números
```
→ La IA tenderá al imperativo. Señalar `let sum` mutable como evidencia de paradigma.

*Prompt 2 (F-24) — restricción funcional explícita:*
```
Implementá lo mismo en estilo funcional puro,
sin mutación de estado, sin variables intermedias
```
→ Verificar que no use `let`. Si lo usa: el ejemplo *vivo* de que la IA no siempre respeta restricciones.

*Prompt 3 (F-25) — máquinas abstractas:*
```
Explicá qué máquina abstracta ejecuta este código TypeScript
```
→ Verificar que mencione: `tsc`, lenguaje intermedio JS, V8/Deno/Node, comparación con JVM.

**El loop "trust but verify" (F-26) — esquema para el pizarrón:**
1. Formular el problema con precisión
2. Hacer el prompt a la IA
3. Revisar con conocimiento de dominio: ¿qué paradigma usó? ¿es correcto semánticamente?
4. Testear con casos borde
5. Refinar el prompt o escribir manualmente si falla

---

### CIERRE (10 min, fuera del tiempo de bloques o absorbidos del Bloque 5)

**Filminas:** F-27 · F-28

- Síntesis de los 5 bloques: los conceptos que deben quedarse del día.
- Anunciar el TP1: quiz en formato GIFT, disponible en `tp.md` y aula virtual.
- Mencionar la guía de estudio (`guia-estudio.md`) disponible en el repo y en el aula.
- Recordar: la próxima clase (Clase 2 de 2 del tema) profundiza en TypeScript y continúa con el Módulo II.

---

## 4. Resumen de Minuta y Links a Filminas

La minuta completa está en [`minuta.md`](minuta.md). Las filminas generadas están en [`filminas.md`](filminas.md) y los archivos de slides en [`slides/`](slides/).

**Mapa rápido de filminas por bloque:**

| Bloque | Filminas | Archivo fuente |
|--------|----------|----------------|
| Apertura | F-00 | `slides/` |
| Bloque 1 — ¿Por qué estudiar LP? | F-01 a F-05 | `slides/` |
| Bloque 2 — Mapa de paradigmas | F-06 a F-10 | `slides/` |
| Bloque 3 — Imperativo y máquina abstracta | F-11 a F-14 | `slides/` |
| Bloque 4 — Intro TypeScript | F-15 a F-20 | `slides/` |
| Bloque 5 — IA y paradigmas | F-21 a F-26 | `slides/` |
| Cierre | F-27 a F-28 | `slides/` |

**Guía del alumno:** [`guia-estudio.md`](guia-estudio.md) — disponible para los estudiantes antes, durante y después de clase.

---

## 5. Extractos Clave de los PDFs Fuente

Los siguientes extractos fueron tomados de los archivos de texto en `material/01-conceptos-introductorios/txt/`. Se incluyen citas textuales relevantes para apoyar la argumentación docente.

---

### 5.1 Louden & Lambert — Capítulo 1 (fuente: `txt/012-034.txt`)

**Sobre la influencia de Von Neumann en el paradigma imperativo:**

> *"A programming language that is characterized by these three properties — the sequential execution of instructions, the use of variables representing memory locations, and the use of assignment to change the values of variables — is called an imperative language, because its primary feature is a sequence of statements that represent commands, or imperatives."*
> — Louden & Lambert, Cap. 1 (fuente: `material/01-conceptos-introductorios/txt/012-034.txt`)

**Sobre el cuello de botella de Von Neumann:**

> *"The requirement that computation be described as a sequence of instructions, each operating on a single piece of data, is sometimes referred to as the von Neumann bottleneck. This bottleneck restricts the ability of a language to provide either parallel computation [...] or nondeterministic computation."*
> — Louden & Lambert, Cap. 1

**Sobre los paradigmas alternativos (cálculo lambda y lógica simbólica):**

> *"The functional paradigm is based on the abstract notion of a function as studied in the lambda calculus. The logic paradigm is based on symbolic logic. Each of these will be the subject of a subsequent chapter. The importance of these paradigms is their correspondence to mathematical foundations, which allows them to describe program behavior abstractly and precisely."*
> — Louden & Lambert, Cap. 1

**Sobre el objeto-orientado como extensión del imperativo:**

> *"In a sense, the object-oriented paradigm is an extension of the imperative paradigm, in that it relies primarily on the same sequential execution with a changing set of memory locations, particularly in the implementation of objects."*
> — Louden & Lambert, Cap. 1

**Sobre funciones de orden superior (relevante para Bloque 4):**

> *"The extensive use of functions is the basis of the functional programming paradigm [...]. Moreover, functions can be combined into higher-level abstractions known as higher-order functions. Such functions are capable of accepting other functions as arguments and returning functions as values. An example of a higher-order function is a map."*
> — Louden & Lambert, Cap. 1

**Ejemplo Scheme de map + reduce (conectar con TypeScript en Bloque 4):**
```scheme
(map abs (list 33 -10 66 88 -4))              ; Returns (33 10 66 88 4)
(reduce + (map abs (list 33 -10 66 88 -4)))   ; Returns 201
```
> *"The same pattern exists in TypeScript's `.map().reduce()` — the idea is 60 years old."*

---

### 5.2 Gabbrielli & Martini — Máquinas Abstractas (fuente: `txt/021-044.txt`)

**Sobre el concepto de máquina abstracta:**

> *"One of the most general concepts is the abstract machine. [...] Abstract machines allow describing what an implementation of a programming language is, without requiring us to go into the specific details of any particular implementation."*
> — Gabbrielli & Martini, Cap. 1

**Cita para usar al introducir el pipeline de TypeScript (Bloque 4, F-16):**

> *"In other words, the algorithms we want to execute must be represented using the instructions of a programming language, L. This language will be formally defined in terms of a specific syntax and a precise semantics."*
> — Gabbrielli & Martini, Cap. 1

---

### 5.3 Material de cátedra UNTDF 2024 (fuente: `txt/01 introduccion.txt`)

**Definición formal de lenguaje de programación:**

> *"Un lenguaje de programación es un conjunto de reglas sintácticas y semánticas usadas para definir programas. Este sistema de notación está compuesto por instrucciones que son comprendidas y ejecutadas por máquinas, usualmente computadoras."*
> — Slides cátedra UNTDF 2024

**Definición de cómputo y programa:**

> *"Un cómputo es un proceso que consiste en aplicar una serie de operaciones estructuradas a un conjunto de valores o datos de entrada, con el objetivo de obtener nuevos valores o datos como resultado."*
> *"Un programa es una colección definida y ordenada de cómputos diseñada para realizar una tarea específica o resolver un problema concreto."*
> — Slides cátedra UNTDF 2024

---

## 6. Preguntas para Clase, Debates y Actividades Prácticas

### 6.1 Preguntas disparadoras (para usar en clase)

| # | Pregunta | Bloque | Tipo |
|---|---------|--------|------|
| Q1 | ¿Cuántos lenguajes de programación existen hoy? | B1 | Apertura abierta |
| Q2 | ¿Tuvo sentido que se crearan tantos? ¿O es un caos? | B1 | Reflexión |
| Q3 | ¿Qué criterios usarían para elegir un lenguaje para un nuevo proyecto? | B1 | Aplicación |
| Q4 | ¿Se puede describir cómputo sin depender de Von Neumann? | B2 | Conceptual |
| Q5 | ¿Cuál versión de `sumaAbs` (imperativa vs. funcional) encuentran más legible? ¿Más fácil de escribir? | B4 | Comparación directa |
| Q6 | ¿Importa el lenguaje si la IA puede escribir en cualquiera? | B1+B5 | Debate (sembrar en B1, responder en B5) |
| Q7 | ¿Qué pasa en la cadena `.ts → .js → V8` si el archivo `.ts` tiene un error de tipos? | B4 | Comprensión |
| Q8 | ¿Por qué el OO no es un paradigma completamente independiente del imperativo? | B2 | Análisis |

### 6.2 Preguntas frecuentes anticipadas (para responder sin preparación adicional)

Estas preguntas emergen con alta probabilidad durante o después de clase. Respuestas sugeridas completas en [`faq-anticipado.md`](faq-anticipado.md).

| FAQ | Pregunta | Prioridad |
|-----|---------|-----------|
| F01 | ¿Tenemos que entender el código en ensamblador LC-3? | 🔴 Alta |
| F02 | ¿TypeScript es interpretado o compilado? | 🔴 Alta |
| F03 | ¿Todo el Bloque 5 (Schmidt & Runfola) entra al TP? | 🟡 Media |
| F04 | ¿Un lenguaje multiparadigma es "mejor" que uno puro? | 🟡 Media |

**Respuesta rápida F01:**
> *"No. El LC-3 está para que vean lo que C abstrae. No hay nada sobre ensamblador en el TP."*

**Respuesta rápida F02:**
> *"Ninguno de los dos en sentido estricto. TypeScript compila a JS con `tsc`, y ese JS es ejecutado por V8 vía JIT. Es el modelo de máquina intermedia — igual que Java con bytecode y JVM."*

### 6.3 Actividades prácticas opcionales (si sobra tiempo o para segundo turno)

**Actividad A1 — Clasificación de lenguajes (5 min):**
Dar una lista: Haskell, C, Java, Prolog, TypeScript, Python, Go. Pedir que los clasifiquen por paradigma(s) y dominio de aplicación predominante.

**Actividad A2 — Detección de paradigma en código (5 min):**
Mostrar dos fragmentos sin identificar (uno imperativo con mutación, uno funcional con `reduce`). Pedir que identifiquen cuál es cuál y justifiquen.

**Actividad A3 — Prompt engineering con paradigma (10 min, si hay acceso a IA):**
Cada alumno (o grupo) recibe un enunciado simple. Deben escribir un prompt que fuerce a la IA a responder en un paradigma específico y verificar que lo hizo correctamente.

### 6.4 Preguntas para debate abierto

1. *"La tendencia actual es hacia lenguajes multiparadigma. ¿Significa eso que los lenguajes puramente funcionales (como Haskell) van a desaparecer?"*
2. *"Si la mayoría del código nuevo se va a generar con IA, ¿tiene sentido enseñar sintaxis de lenguajes? ¿O deberíamos enseñar solo semántica y paradigmas?"*
3. *"Von Neumann diseñó su arquitectura en los años 40. Las GPU modernas (con miles de núcleos paralelos) la rompen. ¿Qué paradigma de programación corresponde mejor a una GPU?"*

---

## 7. Referencias y Localización de Recursos en el Repositorio

### 7.1 Bibliografía utilizada en este tema

| Referencia | Uso en clase | Archivo fuente |
|-----------|-------------|----------------|
| Louden, K. & Lambert, K. — *Programming Languages: Principles and Practice*, 3rd ed. (2012) | Bloques 2, 3 — Von Neumann, paradigmas, map/reduce | `material/01-conceptos-introductorios/txt/012-034.txt` |
| Gabbrielli, M. & Martini, S. — *Programming Languages: Principles and Paradigms* (2023) | Bloque 3 — Máquinas abstractas, interpretación y compilación | `material/01-conceptos-introductorios/txt/021-044.txt` |
| Sebesta, R. — *Concepts of Programming Languages*, 11th ed. | Bloque 1 — Criterios de evaluación de lenguajes | `material/01-conceptos-introductorios/txt/012-034.txt` |
| Schmidt, A. & Runfola, M. (2025) — *AI-Augmented Development Workflows* | Bloque 5 — Split de tiempo y jerarquía de proficiencia en IA | Citado en `minuta.md` |
| Slides cátedra UNTDF 2024 | Bloque 1 — Definiciones, criterios portabilidad y eficiencia | `material/01-conceptos-introductorios/txt/01 introduccion.txt` |

### 7.2 Archivos del tema en el repositorio

| Recurso | Ruta | Descripción |
|---------|------|-------------|
| Diseño aprobado | `salida/cursadas/2026/temas/01-conceptos-introductorios/diseno.md` | Diseño pedagógico — estado: APROBADO |
| Minuta de clase | `salida/cursadas/2026/temas/01-conceptos-introductorios/minuta.md` | Guión completo con tiempos y frases sugeridas |
| Filminas (fuente) | `salida/cursadas/2026/temas/01-conceptos-introductorios/filminas.md` | Contenido de todas las filminas en Markdown |
| Slides compilados | `salida/cursadas/2026/temas/01-conceptos-introductorios/slides/` | Archivos de presentación listos para proyectar |
| Guía del alumno | `salida/cursadas/2026/temas/01-conceptos-introductorios/guia-estudio.md` | Material de estudio completo para los estudiantes |
| Trabajo práctico | `salida/cursadas/2026/temas/01-conceptos-introductorios/tp.md` | Enunciado del TP1 (quiz) |
| TP formato GIFT | `salida/cursadas/2026/temas/01-conceptos-introductorios/tp-quiz.gift` | Para importar en Moodle o Google Classroom |
| FAQ anticipado | `salida/cursadas/2026/temas/01-conceptos-introductorios/faq-anticipado.md` | Preguntas frecuentes con respuestas sugeridas |
| Informe de coherencia | `salida/cursadas/2026/temas/01-conceptos-introductorios/coherence-report.md` | Resultado del loop de calidad |
| Informe de referencias | `salida/cursadas/2026/temas/01-conceptos-introductorios/references-report.md` | Validación de fuentes bibliográficas |
| Score pedagógico | `salida/cursadas/2026/temas/01-conceptos-introductorios/score-pedagogico.md` | Resultado del test con simulator |
| Autograde repo | `salida/cursadas/2026/temas/01-conceptos-introductorios/autograde-repo/` | Repositorio de corrección automática del TP |

### 7.3 Material fuente original

| Archivo | Ruta | Contenido |
|---------|------|-----------|
| `01 introduccion.pdf` | `material/01-conceptos-introductorios/01 introduccion.pdf` | Slides UNTDF 2024 — intro a LP |
| `012-034.pdf` | `material/01-conceptos-introductorios/012-034.pdf` | Sebesta pp. 12–34 — criterios de evaluación |
| `021-044.pdf` | `material/01-conceptos-introductorios/021-044.pdf` | Louden & Lambert Cap. 1 — historia y paradigmas |
| `025-184.pdf` | `material/01-conceptos-introductorios/025-184.pdf` | Gabbrielli pp. 25–184 — máquinas abstractas, TS |

Los archivos `.txt` correspondientes (procesados por `material-ingester`) están en `material/01-conceptos-introductorios/txt/`.

---

## 8. Notas Docentes y Observaciones

### 8.1 Riesgos pedagógicos identificados

| Riesgo | Bloque | Mitigación |
|--------|--------|------------|
| El LC-3 genera angustia en alumnos ansiosos | B3 | Decir explícitamente: *"No entra al TP"* al mostrar F-13 |
| La pregunta "¿TS es interpretado o compilado?" se responde mal de manera binaria | B4 | Preparar respuesta de la máquina intermedia (FAQ F02) |
| La discusión sobre IA consume tiempo del B4 si se abre antes de B5 | B4 | Mantener tema IA exclusivamente en B5 |
| Alumnos estratégicos preguntan si los datos de Schmidt & Runfola entran al TP | B5 | Aclarar: el loop trust-but-verify sí, los porcentajes exactos no |

### 8.2 Oportunidades de profundización (para alumnos avanzados)

- Alonzo Church y el cálculo lambda (1936): las bases matemáticas del paradigma funcional son anteriores a las computadoras.
- El debate Gabriel vs. Graham sobre por qué Lisp no "ganó" aunque sea más elegante — la dinámica de adopción de lenguajes va más allá de las propiedades técnicas.
- Lenguajes diseñados para GPU (CUDA, OpenCL) como ejemplo extremo de paradigma paralelo sin Von Neumann secuencial.

### 8.3 Conexión con temas siguientes

- **Tema 02:** La sintaxis de TypeScript en profundidad — puertas abiertas por el Bloque 4.
- **Tema 03:** Programación funcional con TypeScript — directamente construye sobre las versiones del Bloque 4 de este tema.
- **Temas 04–07:** Los cuatro paradigmas se profundizan uno por uno usando la tabla comparativa de F-09 como ancla.

---

*Guía generada por Dra. Sofía (study-guide-writer) — Paradigmas y Lenguajes de Programación 2026, UNTDF/IDEI.*
*Revisá `guiaprofesor.md`, hacé commit y continuá con la fase de calidad / testing.*
