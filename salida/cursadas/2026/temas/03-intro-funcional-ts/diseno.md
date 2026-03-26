# Diseño de Tema — Tema 03
## Introducción a Programación Funcional con TypeScript

> 🗂️ **Diseñado por:** Lic. Marcos (topic-designer)
> **Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
> **Estado:** ✅ aprobado
> **Aprobado por:** Matías Gel
> **Fecha de aprobación:** 2026-03-26

---

## Datos Operativos

| Campo | Valor |
|-------|-------|
| Número de tema | 03 |
| Nombre | Introducción a Programación Funcional con TypeScript |
| Módulo del plan | Módulo II — Paradigma de Programación Funcional |
| Semana | 2 — Clase 1 |
| Duración de clase | **120 minutos** ← constraint de generación |
| Perfil docente | profesor-teorico |
| Estado | ✅ aprobado |

---

## Tópicos del Plan Mínimo Cubiertos

| Contenido mínimo institucional (plan-minimo.md) | Cubierto en este tema |
|---|---|
| Paradigmas de programación: funcional | ✅ Introducción completa |
| Criterios de diseño e implementación de LP | ✅ Comparación imperativo vs funcional |
| Entidades y ligaduras (intro parcial) | ✅ `const` como ligadura inmutable |

---

## Descripción del Tema

Introducción al **paradigma funcional** desde sus fundamentos teóricos (λ-cálculo, Gabbrielli-Martini cap. 11; Sebesta cap. 15) con **dos lenguajes en paralelo**:

- **TypeScript** como lenguaje principal de trabajo, forzando estilo **puramente funcional** (sin `class`, sin mutación, sin loops imperativos). El énfasis está en el **porqué**: cada restricción funcional se justifica conceptualmente, no sólo se enuncia.
- **Clojure** como lenguaje puro de referencia, que ilustra el paradigma en su forma más disciplinada (dialecto Lisp en JVM, inmutabilidad estructural nativa, todo es expresión).

El hilo conductor es el contraste con el paradigma imperativo ya conocido: **¿qué ganamos al renunciar al estado mutable?**

---

## Objetivos de Aprendizaje

Al finalizar la clase, el alumno será capaz de:

| # | Nivel Bloom | Objetivo |
|---|---|---|
| OA-1 | Comprender | Explicar la diferencia fundamental entre computación por transformación de estado vs computación por reescritura de expresiones |
| OA-2 | Comprender | Enunciar los tres pilares del paradigma funcional: funciones puras, inmutabilidad e inmutabilidad referencial |
| OA-3 | Aplicar | Escribir funciones puras en TypeScript usando `const`, arrow functions y sin efectos colaterales |
| OA-4 | Aplicar | Usar `map`, `filter` y `reduce` en TypeScript como sustitutos funcionales de los loops imperativos |
| OA-5 | Analizar | Justificar por qué cada restricción funcional en TS (no `let`, no mutación, no loops) mejora predecibilidad del código |
| OA-6 | Analizar | Reconocer en Clojure la expresión pura de los mismos conceptos (listas, `map`, `filter`, funciones anónimas con `fn`) |
| OA-7 | Comprender | Trazar el origen del paradigma funcional desde el λ-cálculo de Church y explicar por qué los lenguajes multiparadigma incorporaron características funcionales a partir de los 2000s |

---

## Estructura Temporal — 120 minutos

| Bloque | Tiempo | Contenido | Dinámica |
|---|---|---|---|
| **A0 — Historia: del Entscheidungsproblem al funcional** | 20 min | Church vs Turing (1936), λ-cálculo como origen, recorrido de lenguajes y nichos, por qué entró en multiparadigma | Exposición narrativa con línea de tiempo visual |
| **A — ¿Qué es el paradigma funcional?** | 10 min | Contraste directo imperativo vs funcional. Cómputo como reescritura de expresiones. | Código comparativo en pizarra — ancla lo histórico |
| **B — Tres pilares del funcional** | 20 min | Funciones puras, inmutabilidad y transparencia referencial. Ejemplos con justificación del porqué. Código TS + Clojure en paralelo. | Exposición + ejemplos live-coding |
| **C — TypeScript en modo funcional** | 25 min | Funciones de orden superior: `map`, `filter`, `reduce`. Composición. Arrow functions. Por qué no usamos `for`. Por qué `const` y no `let`. | Live-coding TS — estudiantes predicen resultados |
| **D — Clojure: el funcional puro** | 20 min | Clojure como dialecto Lisp en JVM. Listas como estructura central. `map`, `filter`, `reduce`, `fn`. Todo es expresión. Sin variables, sin estado. | Demo + lectura guiada de código |
| **E — Integración y cierre** | 15 min | Comparativa TS-Clojure. ¿Qué pierde cada uno al ser multiparadigma? Preguntas de alto orden. | Debate socrático breve |
| **Buffer / preguntas** | 10 min | Buffer y preguntas | — |

---

## Contenidos por Bloque

### Bloque A0 — Historia: del Entscheidungsproblem al paradigma funcional (20 min)

**Hilo narrativo:** Antes de escribir una línea de código funcional, hay que saber *de dónde viene* el paradigma — y la respuesta es una pregunta matemática que permanece irrespondible.

---

#### 1. El Entscheidungsproblem — el problema que lo disparó todo

En 1928, David Hilbert propuso el **Entscheidungsproblem** (problema de la decisión):

> *"¿Existe un procedimiento mecánico que, dado cualquier enunciado matemático, determine de forma finita si es verdadero o falso?"*

Hilbert buscaba fundamentar toda la matemática en un sistema formal completo y decidible. La respuesta llegó en 1936, desde dos lugares al mismo tiempo y por caminos completamente distintos.

---

#### 2. Church y Turing: dos modelos, la misma respuesta, distinto legado

| | Alonzo Church (Princeton) | Alan Turing (Cambridge) |
|---|---|---|
| **Herramienta** | λ-cálculo — sistema formal de funciones y sustitución | Máquina de Turing — dispositivo abstracto con estados y cinta |
| **Resultado** | No existe tal algoritmo (demostrado con el problema de la "equivalencia de funciones") | No existe tal algoritmo (demostrado con el problema de la parada — *halting problem*) |
| **Publicación** | 1936, *Annals of Mathematics* | 1936, *Proceedings of the London Mathematical Society* |
| **Legado en LP** | → Paradigma **funcional** | → Paradigma **imperativo** / von Neumann |

**Ambos modelos son computacionalmente equivalentes** — la *Tesis Church-Turing* establece que todo lo computable por uno lo es por el otro. Pero representan dos filosofías opuestas sobre qué *es* computar:

- **Turing → von Neumann → imperativo**: computar = modificar el estado de una cinta/memoria paso a paso
- **Church → λ-cálculo → funcional**: computar = reducir una expresión a su forma normal mediante sustitución

**Para el docente:** La pregunta de Hilbert resultó irrespondible, pero el intento de responderla inventó la computación formal. El λ-cálculo no nació como lenguaje de programación — nació para demostrar que un problema matemático era imposible.

---

#### 3. Recorrido de lenguajes funcionales — cada uno es una respuesta a su época

| Año | Lenguaje | Creador / Origen | Nicho dominante hoy |
|---|---|---|---|
| 1958 | **Lisp** | John McCarthy — MIT | IA simbólica (primer funcional; sigue vivo en Emacs Lisp y Common Lisp) |
| 1962 | **APL** | Kenneth Iverson — IBM | Computación matricial, data science precursor |
| 1973 | **ML** | Robin Milner — Edinburgh | Compiladores, verificación formal, inferencia de tipos |
| 1975 | **Scheme** | Steele/Sussman — MIT | Educación, investigación (base teórica de muchos cursos universitarios) |
| 1985 | **Miranda** | David Turner — Kent | Primer lenguaje puramente lazy — origen directo de Haskell |
| 1986 | **Erlang** | Armstrong — Ericsson | Telecomunicaciones, concurrencia masiva (*WhatsApp usa Erlang en producción*) |
| 1990 | **Haskell** | Comité académico | Finanzas cuantitativas, compiladores, criptografía, verificación formal |
| 2003 | **Scala** | Odersky — EPFL | Big Data (*Apache Spark*, *Kafka*), backend JVM |
| 2005 | **F#** | Don Syme — Microsoft | Finanzas cuantitativas, modelado científico en .NET |
| 2007 | **Clojure** | Rich Hickey | Concurrencia, datos inmutables, **blockchain** (*Datomic*, sistemas de base de datos funcionales) |
| 2012 | **Elixir** | José Valim | Web en tiempo real, telecomunicaciones (corre sobre BEAM/Erlang) |

**Observación clave para debatir con los estudiantes:** cada lenguaje de la lista nació para resolver un problema concreto de su momento — no como ejercicio académico. La industria adoptó el funcional cuando los problemas de concurrencia y escala se volvieron imposibles de resolver con estado mutable compartido.

---

#### 4. ¿Por qué el funcional entró en los lenguajes multiparadigma?

A partir de mediados de los 2000s, los CPUs dejaron de crecer en frecuencia de clock y pasaron a tener múltiples núcleos. El paradigma imperativo con estado mutable compartido genera condiciones de carrera en ese escenario — el funcional las elimina por diseño.

| Lenguaje imperativo | Año de adopción funcional | Qué incorporó |
|---|---|---|
| **Java** | 2014 (Java 8) | Lambdas, Stream API, `Optional` |
| **Python** | Desde 2.x | `map`, `filter`, `reduce`, list comprehensions, `functools` |
| **JavaScript** | 2015 (ES6) | Arrow functions, `.map()`, `.filter()`, `.reduce()`, destructuring |
| **TypeScript** | Desde 2012 | Todo JS funcional + tipos estáticos, `readonly`, discriminated unions |
| **C++** | 2011 (C++11) | Lambdas, `std::function`, `std::transform` |
| **Rust** | 2015 | Immutability by default, closures, iterators, ownership sin GC |
| **Swift** | 2014 | Closures, `map`/`filter`/`reduce`, value semantics |
| **Kotlin** | 2011 | `val`, colecciones funcionales, sequences — igual que TS pero en JVM |

**La tendencia no reemplazó al imperativo — lo enriqueció.** Los lenguajes modernos son multiparadigma porque los problemas modernos mezclan imperativo (I/O, performance) y funcional (transformación de datos, concurrencia, lógica de negocio).

**Frase de anclaje para los alumnos:**
> *"Si el paradigma imperativo es la Máquina de Turing hecha lenguaje, el funcional es el λ-cálculo de Church hecho lenguaje. Aprender ambos no es aprender dos herramientas — es entender las dos formas fundamentales de formalizar la computación."*

---

### Bloque A — ¿Qué es el paradigma funcional? (10 min)

**Concepto central:** El paradigma imperativo computa *modificando* el estado. El funcional computa *reescribiendo* expresiones.

**Hilo de construcción:**
1. Partir del código imperativo conocido (loop + variable mutable)
2. Mostrar el problema: efectos colaterales, impredecibilidad con threading, dificultad de testear
3. Introducir el modelo alternativo: λ-cálculo como base (Gabbrielli-Martini §11.1)
4. Frase clave: *"En puro funcional, una función siempre devuelve lo mismo para los mismos argumentos — sin importar el estado del entorno"*

**Por qué importa esto:** Los estudiantes ya conocen el paradigma imperativo (Tema 01). Este bloque ancla el nuevo paradigma en contraste concreto, no abstracto.

---

### Bloque B — Los tres pilares (20 min)

**Pilar 1: Funciones puras**
- Definición: ningún efecto colateral, salida determinada exclusivamente por entrada
- TypeScript:
  ```typescript
  // ❌ Impura — lee estado externo
  let contador = 0;
  const incrementar = () => { contador++; return contador; };

  // ✅ Pura — sin estado externo
  const sumar = (a: number, b: number): number => a + b;
  ```
- Clojure:
  ```clojure
  ;; ✅ Pura — mismo resultado siempre
  (defn sumar [a b] (+ a b))
  ```
- **Por qué**: Una función pura es predecible, testeable en aislamiento y segura en paralelo.

**Pilar 2: Inmutabilidad**
- En TS: `const` no reasignable + estructuras con `Object.freeze()` o `readonly`
- Por qué `const` y no `let`:
  ```typescript
  // ❌ Estilo imperativo con let
  let numeros = [1, 2, 3];
  numeros.push(4); // mutación oculta

  // ✅ Estilo funcional
  const numeros = [1, 2, 3] as const;
  const masNumeros = [...numeros, 4]; // nueva colección
  ```
- En Clojure: todas las estructuras son persistentes e inmutables por defecto (`vector`, `list`, `map`)
- **Por qué**: eliminar mutación hace que el flujo de datos sea rastreable de principio a fin. No hay "estado sorpresa".

**Pilar 3: Transparencia referencial**
- Cualquier expresión puede ser sustituida por su valor sin cambiar el programa
- Consecuencia directa de los dos pilares anteriores
- Ejemplo de *breaking* de transparencia referencial con `Date.now()` o `Math.random()`

---

### Bloque C — TypeScript en modo funcional (25 min)

**Por qué usamos TypeScript funcionalmente:**
> TypeScript no *obliga* al estilo funcional, pero *permite* adoptarlo de forma disciplinada. Usarlo así nos enseña los principios con sintaxis familiar; luego Clojure nos muestra el caso extremo.

**`map` — transformar sin mutar**
```typescript
// ❌ Imperativo
const dobles: number[] = [];
for (const n of [1, 2, 3]) {
  dobles.push(n * 2);
}

// ✅ Funcional — map transforma sin efecto colateral
const dobles = [1, 2, 3].map(n => n * 2);
// → [2, 4, 6]
```
**Por qué `map` y no `for`**: `map` expresa *qué* transformación hacer, no *cómo* iterar. La iteración es un detalle de implementación — el funcional la abstrae.

**`filter` — seleccionar sin mutar**
```typescript
const pares = [1, 2, 3, 4, 5].filter(n => n % 2 === 0);
// → [2, 4]
```

**`reduce` — acumular sin estado externo**
```typescript
// ❌ Imperativo — acumulador externo mutable
let suma = 0;
for (const n of [1, 2, 3, 4]) { suma += n; }

// ✅ Funcional — el acumulador viaja dentro del fold
const suma = [1, 2, 3, 4].reduce((acc, n) => acc + n, 0);
// → 10
```
**Por qué `reduce`**: elimina el acumulador mutable externo. El estado "viaja" como argumento explícito en cada paso.

**Composición de funciones**
```typescript
const pipe = <T>(...fns: Array<(x: T) => T>) =>
  (valor: T): T =>
    fns.reduce((v, fn) => fn(v), valor);

const procesar = pipe(
  (nums: number[]) => nums.filter(n => n > 0),
  (nums: number[]) => nums.map(n => n * 2),
);
procesar([-1, 2, -3, 4]); // → [4, 8]
```

**Funciones de orden superior — por qué existen:**
En el funcional, las funciones son *valores de primera clase*: pueden pasarse como argumento, retornarse, componerse. Esto permite abstraer patrones de cómputo de forma análoga a cómo los tipos abstraen datos.

---

### Bloque D — Clojure: el funcional puro (20 min)

**Contexto de Clojure:**
- Dialecto de Lisp creado por Rich Hickey (2007), corre en JVM
- Inmutabilidad estructural nativa: ninguna estructura del lenguaje es mutable por defecto
- Todo es una expresión; no hay sentencias — sólo formas especiales y funciones
- Relacionado con la familia Lisp (como Scheme visto en años anteriores)

**Sintaxis básica — lista como estructura central:**
```clojure
;; Una lista de números
'(1 2 3 4 5)

;; map — igual que TypeScript pero más puro
(map #(* % 2) '(1 2 3))
;; → (2 4 6)

;; filter
(filter even? '(1 2 3 4 5))
;; → (2 4)

;; reduce
(reduce + 0 '(1 2 3 4))
;; → 10
```

**Funciones anónimas con `fn`:**
```clojure
;; Función anónima
(fn [x] (* x x))

;; Aplicación inmediata
((fn [x y] (+ x y)) 3 4)
;; → 7

;; Definición con nombre
(defn cuadrado [x] (* x x))
```

**Comparativa TS ↔ Clojure:**

| Concepto | TypeScript (funcional) | Clojure (puro) |
|---|---|---|
| Valor inmutable | `const x = 5` | `(def x 5)` |
| Función pura | `const f = (x: number) => x * 2` | `(defn f [x] (* x 2))` |
| Función anónima | `(x) => x * 2` | `(fn [x] (* x 2))` o `#(* % 2)` |
| Map | `arr.map(fn)` | `(map fn coll)` |
| Filter | `arr.filter(fn)` | `(filter pred coll)` |
| Reduce | `arr.reduce(fn, init)` | `(reduce fn init coll)` |
| Inmutabilidad de colecciones | opt-in (`as const`, `readonly`) | **nativa — siempre** |

**Por qué Clojure muestra el paradigma en su forma pura:** En TS *podemos* mutar aunque digamos que no lo haremos. En Clojure, mutar una estructura crea una *nueva* estructura — la original nunca cambia. Es la disciplina hecha lenguaje.

---

### Bloque E — Integración y cierre (15 min)

**Pregunta de alto orden para debate:**
> _"Si TypeScript permite el estilo funcional pero no lo obliga, ¿qué ventaja tiene aprender Clojure? ¿Y Haskell?"_

**Línea de tiempo — referencia rápida** (ya desarrollada en Bloque A0):
- λ-cálculo (1936) → Lisp (1958) → ML/Scheme (1973–75) → Erlang/Miranda (1985–86) → Haskell (1990) → Scala/F# (2003–05) → Clojure/Elixir (2007–12) → TS/Rust funcional (2010s)

**Pregunta de cierre:**
> _"¿En qué situaciones preferiría usar TypeScript funcional sobre Clojure? ¿Y al revés?"_

**Anticipación para próximas clases:**
- Tema 04: Aspectos avanzados — currying, mónadas, tipos algebraicos
- Tema 05: Mónadas en TypeScript — `Maybe`, `Either`, `Result`

---

## Material de Referencia Consultado

| Fuente | Fragmento relevante |
|---|---|
| Gabbrielli-Martini cap. 11 (`351-423.txt`) | Fundamento teórico del paradigma funcional: cómputo sin estado, funciones de orden superior, λ-cálculo |
| Sebesta cap. 15 (`647-702.txt`) | Historia del paradigma, Lisp, Scheme, Haskell, ML, soporte funcional en lenguajes imperativos |
| Apunte UNTDF 2025 (`Introducción a la Programación Funcional.txt`) | Adaptación del paradigma al contexto de la cátedra (originalmente en Kotlin, adaptado a TS) |
| ChromaDB — material ingestado | Confirmó cobertura teórica en los libros del corpus; Clojure sin cobertura directa → diseño propio |

---

## Estrategia de Filminas

**Perfil declarado del docente:** ritmo lento, filminas completas y autocontenidas.

### Principios que rigen la generación de `filminas.md`

| Principio | Implicación concreta |
|---|---|
| **Una idea por filmina** | Nunca agrupar dos conceptos distintos en la misma slide. Si hay duda, separar. |
| **Autocontenida** | El alumno que estudie solo debe poder entender la filmina sin la narración del docente. Incluir título descriptivo, contexto mínimo, código comentado y conclusión explícita. |
| **Ritmo lento = más filminas** | Cada subtítulo de los bloques A0–E se convierte en al menos una filmina propia. Los ejemplos de código se presentan en pasos: primero el problema (❌), luego la solución (✅), en filminas separadas o con secciones claramente divididas. |
| **Sin texto decorativo** | Todo texto en la filmina es contenido que el alumno necesita, no relleno. |
| **Código anotado** | Los bloques de código llevan comentarios inline que explican *por qué*, no sólo *qué*. El alumno no depende de recordar lo que dijo el docente. |
| **Comparativas explícitas** | Las columnas TS ↔ Clojure se presentan en filminas propias de comparación — no mezcladas dentro de una filmina de concepto. |

### Estimación de filminas por bloque

| Bloque | Mínimo de filminas | Notas |
|---|---|---|
| A0 — Historia | 6–8 | Portada historia · Hilbert+Entscheidungsproblem · Church · Turing · Tesis Church-Turing · Tabla lenguajes (puede dividirse en dos) · Tabla multiparadigma |
| A — ¿Qué es el funcional? | 3–4 | Modelo imperativo · Modelo funcional · Código comparativo imperativo vs funcional |
| B — Tres pilares | 6–8 | Una filmina por pilar + una por ejemplo TS + una por ejemplo Clojure + transparencia referencial |
| C — TS funcional | 8–10 | map (problema) · map (solución) · filter · reduce (problema) · reduce (solución) · composición · por qué const · por qué no for |
| D — Clojure | 5–6 | Contexto Clojure · listas · map/filter/reduce · fn anónimas · tabla comparativa TS↔Clojure |
| E — Cierre | 2–3 | Pregunta de debate · línea de tiempo · anticipo próxima clase |
| **Total estimado** | **30–39 filminas** | Referencia para Roberto al generar `filminas.md` |

---

## Restricciones del Diseño

- **Sin `class`** en todos los ejemplos de TypeScript — el paradigma funcional no usa objetos con estado
- **Sin `let` ni `var`** — toda declaración usa `const`
- **Sin `for`/`while`** — toda iteración se expresa con `map`/`filter`/`reduce` o recursión
- **Sin `push`/`splice`/mutación de arrays** — toda transformación produce nueva colección
- **Cada restricción se justifica conceptualmente** — no como regla arbitraria sino como consecuencia del modelo de computación

---

## Decisiones Pedagógicas

| Decisión | Justificación |
|---|---|
| TypeScript como lenguaje principal (no Haskell o Clojure) | Los estudiantes conocen JS/TS del Tema 01. Reducir carga cognitiva de sintaxis nueva permite enfocarse en el paradigma. |
| Clojure como lenguaje de referencia puro | Clojure hace explícito lo que TS deja implícito. La comparación forced revela la diferencia entre "puedo ser funcional" y "soy funcional". |
| Mostrar el porqué de cada restricción | La instrucción basada en contraste (Mayer 2023) potencia comprensión. Los estudiantes no memorizan reglas — entienden la lógica del paradigma. |
| No usar Haskell en este tema | Haskell introduce sistema de tipos lazy + mónadas en una sola clase es scope creep. Se menciona en el recorrido histórico (A0), no se profundiza. |
| Incluir historia (Bloque A0) como apertura | Situar el paradigma en su contexto matemático-histórico activa conocimiento previo (Turing ya fue mencionado en Tema 01) y responde el "¿para qué sirve esto en el mundo real?" antes de entrar al código. Nichos modernos (blockchain, finanzas, big data) contrarrestan la percepción académica del funcional. |
| Filminas autocontenidas y ritmo lento | El docente presenta a ritmo pausado — cada filmina debe poder leerse e interpretarse sin la narración oral. Esto también beneficia al alumno en el repaso autónomo posterior a la clase. |
| Más filminas, menos contenido por filmina | Fragmentar en 30–39 slides en lugar de condensar. Cada concepto tiene su espacio propio. Evita la sobrecolocación cognitiva (Sweller 2023: evitar más de 4 elementos nuevos por slide). |
| Código en pasos separados (❌ luego ✅) | Mostrar el problema antes de la solución en filminas distintas o secciones separadas. El contraste explícito potencia la comprensión (Mayer 2023: principio de contraste). |

---

## Artefactos a Generar

- [x] `minuta.md` — plan de clase detallado per-bloque (35 secciones, 88 momentos ▶)
- [x] `filminas.md` — 35 filminas autocontenidas, schema-compliant
- [x] `guia-estudio.md` — documento de estudio autónomo (6 partes, autoevaluación, glosario)
- [x] `guiaprofesor.md` — guía del docente autocontenida (plan por filmina, FAQ, fragmentos de libros)
- [ ] `tp.md` — trabajo práctico trazable a la minuta
- [ ] `score-pedagogico.md` — resultado de simulación pedagógica

---

## Checklist de Aprobación

- [x] Duración: todos los bloques suman exactamente 120 min (20+10+20+25+20+15+10)
- [x] Tópicos del plan mínimo cubiertos con evidencia
- [x] Restricciones de estilo funcional definidas y justificadas
- [x] Ejemplos TS y Clojure validados como correctos
- [x] Objetivos de aprendizaje medibles y alineados con bloques de contenido
- [x] Aprobado por: Matías Gel
- [x] Fecha de aprobación: 2026-03-26
