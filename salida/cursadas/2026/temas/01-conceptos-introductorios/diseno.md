# Diseño — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Estado:** APROBADO
> **Agente:** Lic. Marcos (topic-designer)
> **Fecha:** 2026-03-09 — actualizado con material de `material/01-conceptos-introductorios/` (ingesta PDFs)
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
- Criterios de evaluación de lenguajes:
  - **Legibilidad** — ¿Es fácil de leer por otros programadores? *(Sebesta)*
  - **Escribibilidad** — ¿Se puede expresar lo que se quiere sin pelear con el lenguaje? *(Sebesta)*
  - **Confiabilidad** — ¿Las verificaciones formales y semánticas simplifican el testing? *(Sebesta)*
  - **Costo** — desarrollo, mantenimiento y entrenamiento de programadores *(Sebesta)*
  - **Portabilidad** — ¿El lenguaje es independiente de la máquina? *(slides 2024)*
  - **Eficiencia** — velocidad de ejecución + espacio ocupado *(slides 2024)*
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
- **El cuello de botella de Von Neumann** (Louden & Lambert, Cap. 1):
  - La ejecución secuencial instrucción a instrucción es una *restricción* heredada del hardware
  - Limita el paralelismo y el cómputo no determinista
  - Pregunta disparadora: ¿hay formas de describir cómputo *sin* depender de Von Neumann?
  - Respuesta: sí — y de ahí nacen el funcional y el lógico
- Los 4 paradigmas fundamentales y sus bases formales:
  - **Imperativo**: ejecución secuencial + variables como ubicaciones de memoria + asignación
  - **Funcional**: basado en el cálculo lambda — funciones matemáticas, sin estado
  - **Lógico**: basado en lógica simbólica — relaciones y deducción (Prolog)
  - **Orientado a Objetos**: extensión del imperativo con encapsulamiento y paso de mensajes
- Tabla comparativa: modelo de cómputo, unidad de abstracción, lenguajes representativos
  - Imperativo: C, C++, Go — estado mutable, asignación
  - OO: Smalltalk, Java, Dart — objetos y mensajes
  - Funcional: Haskell, LISP, Clojure — funciones como objetos de primera clase
  - Lógico: Prolog — relaciones y deducción
  - Multiparadigma: TypeScript, Python, Scala, F#
- Lenguajes puros vs. multiparadigma
- Dominios de aplicación: ¿cuándo usar cada uno?

### Bloque 3 — Paradigma imperativo y máquina abstracta (20 min)
- **La escalera de abstracciones** (Louden & Lambert, Cap. 1 — Fig. 1.4 y 1.5):
  - Nivel 0: lenguaje de máquina / ensamblador (LC-3) — difícil de leer, propenso a errores
  - Nivel 1: lenguaje de alto nivel (C, Java) — legible, estructurado
  - Cada nivel agrega *abstracción*: permite decir más con menos
  - Esto motiva estudiar LP: entender *qué abstraje* y *qué perdí* al subir de nivel
- **La conexión Von Neumann → imperativo**:
  - Variables de programa = celdas de memoria
  - Instrucción de asignación = transferencia CPU ↔ memoria
  - Saltos condicional/incondicional = sentencias de control
  - Estado = conjunto de pares nombre-valor de variables en un instante
  - Un cómputo = una sucesión de estados
- Ejemplo comparativo: mismo algoritmo (suma de los valores absolutos de un array de 10 enteros)
  - En ensamblador LC-3: 13 líneas con registros, saltos, direcciones de memoria — opaco, ilegible sin comentarios
  - En **C** (lenguaje puro imperativo):
  ```c
  int suma_abs(int arr[], int n) {
      int acc = 0;
      for (int i = 0; i < n; i++)
          acc += (arr[i] < 0) ? -arr[i] : arr[i];
      return acc;
  }
  ```
  - Discusión: ¿qué ganamos? ¿qué sigue implícito? (gestión de memoria, punteros, efectos laterales)
- **Concepto de máquina abstracta** (Gabbrielli & Martini, Cap. 1):
  - Una máquina abstracta ML es un ejecutor de algoritmos definido por el lenguaje L
  - Todo lenguaje define una máquina abstracta — no hay lenguaje sin máquina
  - **Dos formas de implementar** un lenguaje sobre una máquina huésped:
    - *Interpretación pura*: el intérprete decodifica y ejecuta instrucciones en runtime (flexible, lento)
    - *Compilación pura*: un compilador traduce el programa entero a lenguaje objeto antes de ejecutar (rápido, menos flexible)
  - En la práctica siempre hay un **lenguaje intermedio** (la máquina real no es ni puramente interpretada ni compilada)

### Bloque 4 — Intro a TypeScript como lenguaje multiparadigma (30 min)
- ¿Por qué TypeScript en 2026? Ecosistema, tipos, adopción, IA
- Setup mínimo: `tsc` / Deno Playground / editor online
- **TypeScript como ejemplo de máquina intermedia** (conecta con Bloque 3):
  - `tsc` = compilador: TypeScript → JavaScript (lenguaje intermedio)
  - V8 / Node.js / Deno = intérprete/JIT del lenguaje intermedio JS
  - Pipeline completo: `.ts` →[tsc]→ `.js` →[V8]→ ejecución
  - Igual que Java: `.java` → bytecode JVM → ejecución; o Python: `.py` → bytecode → CPython
  - **No es un lenguaje interpretado ni compilado — usa máquina intermedia**, exactamente como predice Gabbrielli Cap. 1
- Mismo ejemplo en TypeScript:
  ```typescript
  const suma = (arr: number[]): number =>
    arr.reduce((acc, x) => acc + x, 0);
  ```
- **Conexión con paradigma funcional** (Louden & Lambert, Cap. 1 — `map` y `reduce`):
  - `reduce` es una *función de orden superior*: recibe otra función como argumento
  - El mismo patrón existe en Scheme (Lisp): `(reduce + (map abs lista))`
  - Esto es programación funcional: sin bucles, sin estado mutable, composición de funciones
  - TypeScript puede escribirse en estilo funcional — anticipación de Temas 03–05
- Observar diferencias vs C: tipos estáticos, función como valor, sin estado mutable explícito
- TypeScript como lenguaje con "aceleradores de paradigma": puede ser imperativo, funcional u OO según cómo se escriba
- Breve introducción al sistema de tipos: type annotations, inferencia

### Bloque 5 — IA Generativa y los paradigmas (15 min)
- **El cambio de rol del programador** (Schmidt & Runfola, 2025):
  - Antes: 70% codificación manual + depuración; 30% comprensión del problema
  - Hoy: 20% codificación manual; **50% prompting, supervisión y orquestación de IA**; 30% formulación del problema
  - *"Natural language has become the new compiler, and developer's focus is migrating from syntax and semantics to strategy"*
  - Tener conocimiento de paradigmas es la diferencia entre un prompt útil y uno que produce basura
- **¿Por qué estudiar LP en la era de la IA?** — La jerarquía de proficiencia (Schmidt & Runfola, Fig. 12):
  - *AI Literacy*: cualquiera puede leer e interpretar lo que genera la IA
  - *AI Fluency*: diseñar prompts, criticar el comportamiento del modelo, construir soluciones — requiere pensamiento computacional
  - *AI Mastery*: construir, optimizar y auditar los sistemas que todos usan — requiere dominar fundamentos
  - Los alumnos de esta materia apuntan a **AI Fluency**: no alcanzan sin conocer paradigmas y semántica
- **Demo en vivo** — pedirle a Copilot/Claude que implemente "sumar los elementos de una lista":
  - Observar: ¿qué paradigma elige la IA por defecto? (¿imperativo con `for`? ¿funcional con `reduce`?)
  - Reformular el prompt: *"usá estilo funcional puro, sin mutación de estado"* → observar el cambio
  - Reformular: *"explicá qué máquina abstracta ejecuta este código"* → ¿puede la IA responder?
- **El loop "trust but verify"** (Schmidt & Runfola, Fig. 8):
  1. Formular el problema con precisión
  2. Hacer el prompt a la IA
  3. Revisar el output con conocimiento de dominio (¿qué paradigma usó? ¿es correcto semánticamente?)
  4. Testear con casos borde
  5. Refinar el prompt o escribir manualmente si falla
  - ⚠️ El "sweet spot": demasiada dependencia de IA atrofia habilidades cognitivas (Fig. 14) — los fundamentos son el antídoto
- **Reflexión de cierre**: conocer paradigmas = saber *qué* pedirle a la IA, *cómo* verificar lo que da, y *cuándo* no confiar en ella

### Cierre (10 min)
- Mapa conceptual de la materia: cómo se conectan los 15 temas
- **Adelanto de la Clase 2: Sintaxis y Semántica** (Louden & Lambert, Cap. 1 §1.4):
  - Todo lenguaje tiene *sintaxis* (estructura) y *semántica* (significado)
  - Sintaxis: gramática formal — define qué es un programa válido
  - Semántica: qué hace ese programa — mucho más difícil de formalizar
  - Ejemplo disparador: `if (x != 0) y = 1 / x;` — ¿qué pasa si no hay `else`? La semántica lo define
- Recursos de instalación/acceso a TypeScript para la próxima clase

---

## Stack de Lenguajes

| Rol | Lenguaje | Uso en esta clase |
|-----|----------|-------------------|
| Principal | TypeScript | Bloque 4 (código) y B5/edu (código generado por IA) |
| Contraste imperativo puro | C | Bloque 3 — solo lectura, sin instalación requerida |
| Demo IA | Copilot / Claude en vivo | Bloque 5 |

---

## Objetivos de Aprendizaje

Al finalizar la clase, el alumno podrá:
1. Justificar por qué el estudio de paradigmas es relevante en la era de IA generativa
2. Identificar los 4 paradigmas fundamentales y sus lenguajes representativos
3. Distinguir código imperativo de código funcional observando mutación de estado
4. Escribir una función básica con tipos en TypeScript
5. Aplicar el loop "trust but verify" para verifi/educar código generado por IA: identificar el paradigma usado, detectar errores semánticos y reformular el prompt con precisión

---

## Recursos y Bibliografía del Tema

- **Sebesta, R.W.** (2018). *Concepts of Programming Languages*, 12th ed. Pearson. Cap. 1 — "Preliminaries" *(material/01-conceptos-introductorios/025-184.pdf)*
- **Louden & Lambert** (2011). *Programming Languages: Principles and Practice*, 3rd ed. Cap. 1 — "Introduction" *(material/01-conceptos-introductorios/012-034.pdf)* — cubre abstracciones, paradigmas, sintaxis/semántica, traducción
- **Gabbrielli & Martini** (2023). *Programming Languages: Principles and Paradigms*, 2nd ed. Cap. 1 — "Abstract Machines" *(material/01-conceptos-introductorios/021-044.pdf)* — cubre máquina abstracta, intérprete vs compilador, máquina intermedia (JVM, Python bytecode)
- **Schmidt, D.C. & Runfola, D.** (2025). *Liberating Logic in the Age of AI: Going Beyond Programming with Computational Thinking*. arXiv:2511.17696 *(temas/2511.17696v1.pdf)* — para el Bloque 5: cambio de rol del programador, jerarquía de proficiencia en IA, loop "trust but verify"

### Material base 2024

> Las diapositivas de `material/01-conceptos-introductorios/01 introduccion.pdf` (UNTDF, 2024) constituyen el material de partida para esta clase. La estructura de bloques fue diseñada para alinear y expandir ese material, actualizando las referencias de Kotlin a TypeScript y sumando el Bloque 5 de IA generativa.

---

## Notas para el Docente

- El Bloque 3 (C imperativo puro) es opcional si el tiempo aprieta — puede reducirse a 10 min mostrando solo el snippet
- El Bloque 5 (IA) es el más flexible: puede expandirse si hay buena discusión o comprimirse a 10 min
- Tener preparado el Deno Playground (https://playground.deno.land) como fallback si hay problemas de instalación
- El tópico "Introducción a Kotlin" del plan mínimo original fue reemplazado por TypeScript (ver `curriculum-proposal.md` aprobado)

---

## Decisión Docente

> ✅ **APROBADO** — 2026-03-09 por Matías Gel — se procedió con `/edu_create_class`
> ⬜ **AJUSTAR** — Indicar cambios con `/edu_adjust_design`
