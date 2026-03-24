# Diseño — Tema 03: Introducción a Programación Funcional con TypeScript

> **Estado:** BORRADOR — pendiente aprobación docente
> **Agente:** Lic. Marcos (topic-designer)
> **Fecha:** 2026-03-23
> **Workflow:** topic-cycle / Step 1
> **Material de referencia:** `material/03-Funcional-Intro/` (5 fuentes — 5 `.txt` disponibles)

---

## Datos del Tema

| Campo | Valor |
|-------|-------|
| Número | 03 |
| Nombre | Introducción a Programación Funcional con TypeScript |
| Módulo del plan mínimo | Módulo II |
| Semana | 2 |
| Clase | 1 de 1 |
| Duración total | **120 minutos** ← constraint de generación, no sugerencia |
| Lenguaje principal | TypeScript (estilo puramente funcional) |
| Lenguaje puro de contraste | Clojure (lenguaje funcional puro de la familia LISP) |
| Perfil docente | profesor-teorico |

---

## Tópicos del Plan Mínimo cubiertos en este tema

| Tópico | Código plan mínimo |
|--------|--------------------|
| Introducción y fundamentos de la programación funcional | Módulo II |
| Importancia e impacto en lenguajes y frameworks actuales | Módulo II |
| Funciones puras, inmutabilidad, recursividad | Módulo II |
| Ventajas, desventajas y dominios de aplicación | Módulo II |
| TypeScript como lenguaje funcional *(reemplaza Kotlin)* | Módulo II adaptado |
| Expresiones lambda y funciones anónimas (TypeScript y comparación) | Módulo II |
| Funciones de orden superior y clausuras y ámbito léxico | Módulo II |

> ⚠️ **Fuera de scope de T03 — quedan en T04:**
> Composición de funciones, aplicación parcial, currificación, evaluación perezosa.
> ⚠️ **Fuera de scope de T03 — quedan en T05:**
> Mónadas, functores, manejo de efectos con tipos.

---

## Fuentes de Referencia

| Archivo fuente | Contenido relevante |
|----------------|---------------------|
| `351-423.txt` | Gabbrielli & Martini, Cap. 11 — *Functional Programming Paradigm* — teoría del paradigma, cómputo sin estado, λ-cálculo, máquina SECD |
| `647-702.txt` | Sebesta, Cap. 15 — *Functional Programming Languages* — historia, Lisp/Scheme, ML, Haskell, comparación imperativo vs. funcional |
| `Introducción a la Programación Funcional.txt` | Filminas 2025 (base Kotlin) — conceptos trasladados a TypeScript |
| `054-147.txt` | Contenido adicional de bibliografía base |
| `2511.17696v1.txt` | Schmidt & Runfola (2026) — IA y pensamiento computacional — base del bloque IA |

---

## Decisión Curricular: TypeScript + Clojure

**TypeScript como lenguaje principal funcional:**
- Permite practicar estilo funcional *puro por elección* (igual que Kotlin en 2025)
- Los alumnos ya lo conocen del Tema 01
- Características usadas en este tema: `const`, tipos de función `(A) => B`, genéricos, `readonly`, arrow functions
- Se restringe explícitamente el uso de `let`, mutación, bucles `for`/`while` y clases

**Clojure como lenguaje puro de contraste** (reemplaza Haskell del plan-borrador):
- Es un dialecto moderno de Lisp — conecta con la historia del paradigma (Lisp → Scheme → Clojure)
- Inmutabilidad y funciones puras *por defecto*, no por elección
- Sintaxis de prefijo más accesible para mostrar HOF que Haskell para primer contacto
- Usado solo en modo *lectura* — no se programa, se analiza y contrasta

---

## Estructura Temporal — 120 minutos

```
00:00 ──────── Bloque 0:   Recap y punto de partida (5 min)
00:05 ──────── Bloque 0.5: Historia y raíces formales del paradigma (15 min)
00:20 ──────── Bloque 1:   Fundamentos del paradigma funcional (20 min)
00:40 ──────── Bloque 2:   TypeScript funcional — funciones como valores (20 min)
01:00 ──────── Bloque 3:   HOF en TypeScript y contraste con Clojure (30 min)
01:30 ──────── Bloque 4:   Clausuras, ámbito léxico y recursión (15 min)
01:45 ──────── Bloque IA:  IA generativa y el paradigma funcional (10 min)
01:55 ──────── Cierre y adelanto T04 (5 min)
02:00 ──────── FIN
```

---

### Bloque 0 — Recap y punto de partida (5 min)

**Propósito:** conectar con T01, recordar el mapa de paradigmas.

- Recap relámpago de T01: los cuatro paradigmas, sus raíces formales
- El funcional: basado en el **λ-cálculo** (Church, 1936) — el mismo año que la Máquina de Turing
- Pregunta disparadora: *"¿Qué tiene de raro un lenguaje donde no existe el concepto de 'variable que cambia'?"*
- Anticipar: hoy TypeScript, contrastado con Clojure como espejo puro

---

### Bloque 0.5 — Historia y raíces formales del paradigma funcional (15 min)

**Propósito:** anclar el paradigma en su historia matemática — mostrar que el funcional no es una moda sino un modelo de cómputo tan antiguo y legítimo como el imperativo.

#### El problema que lo originó todo: el *Entscheidungsproblem*

- En 1928, David Hilbert formuló el **Entscheidungsproblem** ("problema de decisión"): *¿existe un algoritmo mecánico que, dado cualquier enunciado matemático, determine en tiempo finito si es verdadero o falso?*
- Era la pregunta central del programa formalista de Hilbert: demostrar que la matemática entera podía reducirse a un sistema formal completo y decidible
- La respuesta requería primero definir con precisión qué significa "algoritmo mecánico" — y aquí es donde nacen dos visiones radicalmente distintas

#### La respuesta de Turing: la máquina con cinta (1936)

- Alan Turing modeló el cómputo como una **máquina con estados**: un cabezal que lee y escribe símbolos en una cinta infinita, moviéndose según una tabla de transiciones
- El cómputo avanza *modificando el estado*: en cada paso, la máquina lee un símbolo, escribe otro (o el mismo), cambia de estado, y mueve el cabezal
- Es esencialmente un modelo de la actividad de un *calculador humano*: alguien con papel, lápiz y borrador, siguiendo reglas mecánicas paso a paso
- Este modelo es el ancestro directo del paradigma imperativo: **variables = celdas de memoria, instrucciones = pasos de la máquina, programa = tabla de estados**
- La respuesta de Turing al Entscheidungsproblem: NO — demostró que existe el **Problema de la Parada** (*Halting Problem*): ninguna máquina puede determinar en general si otra máquina terminará o no → hay preguntas matemáticas que ningún algoritmo puede decidir

#### La respuesta de Church: el λ-cálculo (1936)

- Alonzo Church, de Princeton, llegó a la misma conclusión por un camino completamente distinto
- Su herramienta fue el **λ-cálculo**: un sistema formal donde el único concepto primitivo es la *función* — su definición y su aplicación
  - **Abstracción lambda** (`λx. expr`): define una función sin nombre — "la función que toma `x` y devuelve `expr`"
  - **Aplicación**: aplicar una función a un argumento — `(λx. x * x) 3` → `3 * 3` → `9`
  - **Reducción β**: la regla de cómputo — sustituir el argumento en el cuerpo de la función
- En el λ-cálculo no existen variables que cambien de valor, ni celdas de memoria, ni pasos secuenciales — *solo expresiones que se transforman en otras expresiones*
- El cómputo es **reescritura**: `fact 3 → if 3=0 then 1 else 3 * fact(2) → 3 * fact(2) → 3 * (2 * fact(1)) → ... → 6` *(Gabbrielli & Martini, Cap. 11.1.2)*
- Church demostró: hay enunciados que el λ-cálculo no puede decidir → también responde NO al Entscheidungsproblem

#### Dos respuestas NO al mismo problema → dos visiones del cómputo

- En 1937 Turing demostró que ambos modelos son **computacionalmente equivalentes**: todo lo que puede calcular una Máquina de Turing puede calcularlo el λ-cálculo, y viceversa (**Tesis de Church-Turing**)
- Pero las dos visiones son filosóficamente opuestas:

| | Máquina de Turing | λ-cálculo de Church |
|---|---|---|
| Unidad básica | Estado + transición | Función + aplicación |
| Progresa... | ...modificando estado | ...reduciendo expresiones |
| ¿Hay memoria? | Sí — la cinta | No — solo el entorno |
| Metáfora | Calculador con libreta | Matemático ecuando |
| Paradigma que inspira | **Imperativo** | **Funcional** |

- **La consecuencia cultural:** la arquitectura de Von Neumann (1945) implementó físicamente el modelo de Turing — CPU + RAM = cabezal + cinta — y los primeros lenguajes de programación (Fortran, COBOL) siguieron ese modelo porque era el hardware real. El λ-cálculo quedó como herramienta matemática... hasta Lisp.

#### Del λ-cálculo a Lisp: el salto a lenguaje de programación (1958)

- John McCarthy (MIT, 1958) fue el primero en preguntar: *¿podemos implementar el λ-cálculo como lenguaje de programación real?*
- Creó **Lisp** basándose directamente en el λ-cálculo:
  - Las listas S-expressions modelan la aplicación de funciones: `(f a b)` = aplicar `f` a `a` y `b`
  - Las funciones son valores de primera clase — se pasan como argumentos, se devuelven como resultados
  - La recursión reemplaza a los bucles
  - Introdujo el **Garbage Collector** automático — porque sin mutación manual, la memoria se gestiona sola
- McCarthy inventó sin buscarlo gran parte de lo que hoy es estándar: GC, funciones de orden superior, evaluación condicional como expresión, tipado dinámico *(Sebesta, Cap. 15.4)*
- Con Lisp nació el paradigma funcional como práctica de ingeniería, no solo como teoría matemática

#### Línea de tiempo: de Lisp a TypeScript

| Año | Lenguaje / Hito | Nota |
|-----|-----------------|------|
| 1936 | **λ-cálculo** (Church) | Base matemática del paradigma funcional |
| 1936 | Máquina de Turing | Base del paradigma imperativo — *el mismo año* |
| 1958 | **Lisp** (McCarthy, MIT) | Primer LP basado en λ-cálculo; listas, recursión, GC automático |
| 1964 | Máquina SECD (Landin) | Primera máquina abstracta para HOF — el equivalente funcional de la Máquina de Turing *(G&M, Cap. 11)* |
| 1975 | **Scheme** (Steele & Sussman) | Dialecto puro y pequeño de Lisp — influyó masivamente en educación CS |
| 1977 | Backus — ACM Turing Award | Creador de Fortran critica el imperativo y propone FP puro *(Sebesta, Cap. 15.1)* |
| 1983 | **ML / SML** | Sistema de tipos polimórfico, inferencia de tipos — la madurez académica |
| 1990 | **Haskell** | LP funcional puro con evaluación perezosa (*lazy*) — estándar académico |
| 2003 | **Scala** | Funcional + OO sobre la JVM — populariza el estilo en la industria |
| 2007 | **Clojure** (Rich Hickey) | Dialecto de Lisp moderno sobre la JVM — inmutabilidad por defecto, concurrencia |
| 2012+ | **TypeScript / ES6+** | Arrow functions, HOF nativas, `const` — el funcional llega al mainstream web |

- **La cita de Backus (1978):** *"Programs written in a purely functional style are easier to understand because the meanings of expressions are independent of their context"* — hoy lo llamamos **transparencia referencial** *(Sebesta, Cap. 15.1)*
- **El renacimiento reciente:** durante 50 años el funcional fue académico. Los últimos 15 años lo llevaron al mainstream:
  - React (2013) adoptó componentes como funciones puras + inmutabilidad en el estado
  - Rust adoptó ownership inmutable como pilar de seguridad de memoria
  - TypeScript/JavaScript incorporaron `const`, spread, `map/filter/reduce` como herramientas de primera clase
- **La razón de fondo:** en un mundo de cómputo multi-core y distribuido, la mutabilidad compartida es el problema central de concurrencia — el funcional lo elimina por diseño

---

### Bloque 1 — Fundamentos del paradigma funcional (25 min)

**Propósito:** construir el modelo mental correcto *antes* de ver código.

#### 1.0 La función matemática como modelo (5 min)

- Una función matemática es un **mapeo** del conjunto dominio al conjunto codominio — no una secuencia de instrucciones *(Sebesta, Cap. 15.2)*
- Formalmente: `f : A → B` — para cada `a ∈ A` existe exactamente un `b ∈ B` tal que `f(a) = b`
- Propiedades que la distinguen de un procedimiento imperativo:
  1. **Determinismo**: el resultado depende *solo* del input — nada más
  2. **Sin efecto colateral**: evaluar `f(x)` no cambia nada fuera de `f`
  3. **Sin historia**: no importa cuántas veces se evaluó antes — el resultado es siempre el mismo
- Contraste: `getTime()` devuelve distintos valores en distintos momentos → *no es una función matemática* aunque tenga la misma sintaxis de llamada
- Esta distinción es el corazón del paradigma: un programa funcional es un sistema de ecuaciones matemáticas, no un guión de instrucciones

#### 1.1 Cómputo sin estado (8 min)

- El modelo imperativo: cómputo = transformación de estado → variables = celdas de memoria → asignación = operación central *(Gabbrielli & Martini, Cap. 11.1)*
- El modelo funcional: cómputo = **reescritura de expresiones** — no hay estado, no hay memoria mutable
- Axioma central: *"Si el entorno está fijo, una expresión siempre denota el mismo valor"* *(Gabbrielli & Martini, Cap. 11)*
- Consecuencia radical: sin asignación → la iteración pierde sentido → **la recursión es el mecanismo de control de flujo**
- **Transparencia referencial**: `f(x)` siempre devuelve lo mismo para el mismo `x` — la propiedad que permite razonamiento ecuacional sobre programas
- Nota: la **Máquina SECD** de Landin (1964) fue la primera máquina abstracta diseñada para ejecutar lenguajes funcionales de orden superior — el equivalente funcional de la Máquina de Turing *(Gabbrielli & Martini, Cap. 11)*

#### 1.2 Funciones puras e impuras — la distinción central (8 min)

- Función pura: (1) mismo input → mismo output, (2) sin efectos colaterales observables
- Función impura: depende de estado externo o modifica estado externo
- Ejemplos en pseudocódigo — luego en TypeScript:
  - Pura: `suma(a, b) => a + b`
  - Impura: `getSaldo()` (depende de estado del sistema), `console.log()` (efecto colateral de I/O)
- **Los efectos no desaparecen** — se aíslan en los bordes del sistema (el exterior de un núcleo funcional puro)
- Diagrama: núcleo funcional puro rodeado por una capa de efectos

#### 1.3 Inmutabilidad (7 min)

- Inmutabilidad: una vez asignado un valor, no cambia
- No hay variable — hay **binding** (ligadura nombre-valor): en el λ-cálculo declarar una función es *extender el entorno* con una nueva asociación nombre-valor, no crear una celda de memoria *(Gabbrielli & Martini, Cap. 11)*
- En ML (la síntaxis que se usa didácticamente para el λ-cálculo): `val f = fn x => x * x` — `val` introduce una *declaración*, no una *asignación*. Es la misma operación que `const f = (x) => x * x` en TypeScript
- La diferencia conceptual es profunda: en el imperativo reutilizamos la misma celda con distintos valores; en el funcional cada nombre se liga *una sola vez y para siempre*
- Beneficios prácticos: razonamiento local (el valor no cambia mientras uno lee el código), paralelismo seguro (no hay condiciones de carrera si no hay mutación), debugging predecible
- Cita de Sebesta: *"Variables in pure functional languages are bound to values only once"* *(Cap. 15.3)*
- Vínculo con Backus (1977): usó exactamente este argumento — la ausencia de estado hace que los programas sean más fáciles de entender formalmente — para criticar los lenguajes imperativos en su discurso del Premio Turing

---

### Bloque 2 — TypeScript funcional — funciones como valores (25 min)

**Propósito:** pasar de los conceptos al código en TypeScript, restringidos al estilo puro.

#### 2.1 Funciones como ciudadanos de primera clase (8 min)

- Una función es un valor: puede almacenarse en una variable, pasarse como argumento, devolverse como resultado
- Tipo de función en TypeScript: `(parametro: Tipo) => ReturnTipo`
- Arrow functions — sintaxis concisa para funciones anónimas:
  ```typescript
  // Función nombrada (binding)
  const duplicar = (n: number): number => n * 2;

  // Almacenada en una variable const — inmutable
  const operacion: (x: number) => number = duplicar;

  // Pasada como argumento
  const aplicar = (f: (x: number) => number, valor: number): number => f(valor);
  console.log(aplicar(duplicar, 5)); // 10
  ```
- `const` vs. `let` — en estilo funcional: **solo `const`**. No `let`, no `var`.
- Por qué TypeScript es bueno para esto: los tipos de función son ciudadanos de primera clase del sistema de tipos

#### 2.2 Inmutabilidad en TypeScript (8 min)

- `const` para bindings — pero no garantiza inmutabilidad profunda del objeto
- `readonly` en tipos para propiedades de objetos:
  ```typescript
  type Punto = {
    readonly x: number;
    readonly y: number;
  };

  const p: Punto = { x: 3, y: 4 };
  // p.x = 10; // Error de compilación ✓
  ```
- `ReadonlyArray<T>` en lugar de `T[]` para arrays inmutables:
  ```typescript
  const nums: ReadonlyArray<number> = [1, 2, 3];
  // nums.push(4); // Error de compilación ✓
  ```
- El patrón de "transformación sin mutación": en lugar de mutar, crear nuevo valor:
  ```typescript
  // Imperativo (prohibido en estilo funcional):
  // nums.push(4);

  // Funcional (permitido):
  const nuevoNums = [...nums, 4];
  ```
- Contraste con Clojure:
  ```clojure
  ; En Clojure, los datos son inmutables por defecto
  (def nums [1 2 3])
  (conj nums 4)   ; => [1 2 3 4] — nums no cambia
  ```

#### 2.3 Funciones anónimas y closures básicos (9 min)

- Lambda = función anónima en TypeScript:
  ```typescript
  const cuadrado = (x: number): number => x * x;
  ```
- Closures: una función que "captura" variables del entorno léxico donde fue definida:
  ```typescript
  const crearSumador = (n: number) => (x: number) => x + n;
  const sumar5 = crearSumador(5);
  console.log(sumar5(3)); // 8
  console.log(sumar5(10)); // 15
  ```
  - `sumar5` es una clausura — lleva consigo el valor de `n = 5` de su entorno de creación
- Ámbito léxico: la closure recuerda el entorno en el que fue *definida*, no el de *llamada*
- Contraste en Clojure:
  ```clojure
  (defn crear-sumador [n]
    (fn [x] (+ x n)))
  (def sumar5 (crear-sumador 5))
  (sumar5 3)  ; => 8
  ```
  - La sintaxis refleja el mismo concepto — las funciones capturan el entorno léxico en ambos lenguajes

---

### Bloque 3 — Funciones de Orden Superior en TypeScript y Clojure (30 min)

**Propósito:** dominar `map`, `filter`, `reduce` como las herramientas principales del paradigma funcional aplicado.

#### 3.1 ¿Qué es una función de orden superior? (5 min)

- HOF: función que toma otras funciones como argumentos, o devuelve funciones como resultado
- Origen en el λ-cálculo: las funciones siempre fueron de orden superior
- Cita de Gabbrielli & Martini: *"Higher-order functions and recursion are the basic ingredients of the stateless computational model"* *(Cap. 11)*
- En TypeScript: `Array.prototype.map`, `filter`, `reduce` son HOF nativas
- Pregunta: ¿qué patrón tiene `map`? — abstrae la idea de *"aplicar una transformación a cada elemento"*

#### 3.2 `map` — Transformar colecciones (8 min)

- Semántica: aplica una función pura a cada elemento, devuelve un nuevo array (sin modificar el original)
  ```typescript
  const nums: ReadonlyArray<number> = [1, 2, 3, 4, 5];

  // Duplicar cada elemento
  const dobles = nums.map(n => n * 2);
  // => [2, 4, 6, 8, 10]  — nums sin cambiar

  // Con función nombrada
  const espar = (n: number): boolean => n % 2 === 0;
  const sonPares = nums.map(espar);
  // => [false, true, false, true, false]
  ```
- Tipo de `map` en TypeScript: `Array<A>.map<B>(f: (a: A) => B): B[]` — refleja claramente la polimorficidad
- Contraste en Clojure:
  ```clojure
  (def nums [1 2 3 4 5])
  (map #(* % 2) nums)   ; => (2 4 6 8 10)
  ```

#### 3.3 `filter` — Seleccionar elementos (7 min)

- Semántica: retiene solo los elementos para los cuales el predicado devuelve `true`
  ```typescript
  const nums: ReadonlyArray<number> = [1, 2, 3, 4, 5, 6];

  const pares = nums.filter(n => n % 2 === 0);
  // => [2, 4, 6]

  type Producto = { readonly nombre: string; readonly precio: number; };
  const catalogo: ReadonlyArray<Producto> = [
    { nombre: "Laptop", precio: 1200 },
    { nombre: "Mouse", precio: 25 },
    { nombre: "Monitor", precio: 400 },
  ];
  const económicos = catalogo.filter(p => p.precio < 100);
  // => [{ nombre: "Mouse", precio: 25 }]
  ```
- Contraste en Clojure:
  ```clojure
  (filter even? [1 2 3 4 5 6])  ; => (2 4 6)
  ```

#### 3.4 `reduce` — Plegar a un valor (10 min)

- Semántica: combina todos los elementos de una colección en un único valor usando un acumulador
  ```typescript
  const nums: ReadonlyArray<number> = [1, 2, 3, 4, 5];

  // Suma
  const suma = nums.reduce((acc, n) => acc + n, 0);
  // => 15

  // Máximo
  const maximo = nums.reduce((acc, n) => n > acc ? n : acc, nums[0]);
  // => 5

  // Contar ocurrencias (de string[])
  const letras: ReadonlyArray<string> = ["a", "b", "a", "c", "b", "a"];
  const conteo = letras.reduce<Record<string, number>>(
    (acc, letra) => ({ ...acc, [letra]: (acc[letra] ?? 0) + 1 }),
    {}
  );
  // => { a: 3, b: 2, c: 1 }
  ```
- Tipo de `reduce`: `Array<A>.reduce<B>(f: (acc: B, val: A) => B, init: B): B`
- `reduce` es la HOF más potente — `map` y `filter` se pueden expresar con `reduce`
- Contraste en Clojure:
  ```clojure
  (reduce + 0 [1 2 3 4 5])  ; => 15
  ```
- **Punto de reflexión:** encadenar `map` → `filter` → `reduce` es el pipeline funcional básico — "el cuello de botella de Von Neumann al revés": no hay secuencia de estados, hay transformación de datos.

---

### Bloque 4 — Clausuras, ámbito léxico y recursión (15 min)

**Propósito:** cerrar los fundamentos con los dos mecanismos de control centrales del paradigma.

#### 4.1 Clausuras y ámbito léxico en profundidad (7 min)

- Retomar el ejemplo de `crearSumador` — ahora analizar el scope en detalle
- Contrastarlo con scope dinámico (breve mención): en scope dinámico, la closure capturaría el entorno de *llamada*, no de *definición* — resultados impredecibles
- El ámbito léxico garantiza la **transparencia referencial** de las closures
- Aplicación práctica: fábricas de funciones configurables:
  ```typescript
  const crearMultiplicador = (factor: number) =>
    (x: number): number => x * factor;

  const triple = crearMultiplicador(3);
  const décuplo = crearMultiplicador(10);

  [1, 2, 3].map(triple);   // => [3, 6, 9]
  [1, 2, 3].map(décuplo);  // => [10, 20, 30]
  ```
- Nota: la composición de funciones (unir `triple` y `décuplo`) queda en T04.

#### 4.2 Recursión como mecanismo de control (8 min)

- Sin `for`, sin `while` — la recursión es el único mecanismo de iteración en el paradigma puro
- Ejemplo: factorial con recursión directa en TypeScript:
  ```typescript
  const factorial = (n: number): number =>
    n <= 1 ? 1 : n * factorial(n - 1);
  ```
- El mismo en Clojure:
  ```clojure
  (defn factorial [n]
    (if (<= n 1)
      1
      (* n (factorial (- n 1)))))
  ```
- Construcción de intuición: la recursión funciona por *reducción a caso base* + *composición de resultados parciales* — es la evaluación por sustitución del λ-cálculo en acción
- Problema: desbordamiento de pila con valores grandes — anticipar tail recursion
- Tail recursion básica en TypeScript *(nota — el Runtime JS/TS no garantiza TCO, pero el patrón es correcto)*:
  ```typescript
  const factorialAux = (n: number, acc: number): number =>
    n <= 1 ? acc : factorialAux(n - 1, n * acc);

  const factorialTCO = (n: number): number => factorialAux(n, 1);
  ```
- En Clojure, `recur` garantiza TCO:
  ```clojure
  (defn factorial-tco [n]
    (loop [n n acc 1]
      (if (<= n 1) acc
        (recur (- n 1) (* n acc)))))
  ```

---

### Bloque IA — IA Generativa y el Paradigma Funcional (15 min)

**Propósito:** mostrar cómo el estilo funcional se entrelaza con el desarrollo asistido por IA y el pensamiento computacional actual.

#### Tema del bloque: "Pensar funcionalmente para trabajar con IA"

- **El contexto:** Schmidt & Runfola (2026) argumentan que lo que importa en la era IA no es la sintaxis del lenguaje, sino el **pensamiento computacional** — la capacidad de descomponer problemas en transformaciones precisas sobre datos
- **El funcional como lenguaje de especificación:** las HOF (`map`, `filter`, `reduce`) son, en esencia, *especificaciones declarativas* — describen *qué* se quiere, no *cómo lograrlo*. Los modelos de lenguaje entienden mejor las especificaciones declarativas que el código imperativo paso a paso.
- **Demostración en vivo (5 min):** formular el mismo problema de dos formas para un asistente de IA:
  1. *Forma imperativa:* "Iterá sobre el array, si el elemento es par multiplicalo por dos y guardalo en otro array"
  2. *Forma funcional:* "Aplicá `filter(espar).map(triplicar)` sobre el array"
  - Comparar calidad y precisión de las respuestas generadas
- **El estilo funcional como defensa ante el código generado inseguro:**
  - Las funciones puras son fáciles de testear unitariamente — `f(input)` → verificar output, sin mocks
  - El código generado por IA con efectos colaterales es difícil de auditar — el funcional acota el riesgo
  - Una función pura que la IA genera incorrectamente falla de forma *visible y predecible*
- **Advertencia:** la IA puede generar código "con aspecto funcional" que en realidad muta estado. Saber leer e identificar pureza es una habilidad crítica de auditoría.
- **Reflexión de cierre:** en la era de la IA generativa, el paradigma funcional no es "más difícil" — es el estilo donde el programador humano puede *razonar*, *verificar* y *componer* sobre el código resultante con mayor seguridad.

---

### Cierre y adelanto T04 (5 min)

- Resumen: aprendimos qué es el paradigma funcional, cómo se ve en TypeScript y cómo contrasta con Clojure
- Lo que dejamos para T04: **composición de funciones, aplicación parcial y currificación** — con esto se cierra el toolkit funcional avanzado
- Pregunta para reflexión asincrónica: *"¿Cuándo no usarías el estilo funcional en un proyecto real de TypeScript?"*

---

## Dependencias con otros Temas

| Tema | Relación |
|------|----------|
| T01 | **Prerrequisito** — paradigmas, TypeScript básico, máquina abstracta |
| T02 | Contexto — sintaxis y semántica (λ-cálculo como formalismo semántico) |
| T04 | **Continuación** — composición, aplicación parcial, currificación |
| T05 | Continuación — mónadas en TypeScript |

---

## Conocimiento Previo Esperado

| Concepto | Dónde se vio |
|----------|-------------|
| Qué es un paradigma de programación | T01 |
| TypeScript: `const`, arrow functions, tipos básicos | T01 |
| El paradigma funcional como alternativa al imperativo | T01 (mención) |
| Arrays y objetos en TypeScript | T01 |

---

## Alertas de Scope

> **⛔ FUERA DE SCOPE — T03** — Estos temas interrumpirían la clase si se mencionan en profundidad:
> - Composición de funciones (`pipe`, `compose`) → T04
> - Aplicación parcial y currificación → T04
> - Functores y mónadas → T05
> - Evaluación perezosa → T04
> - TypeScript strict mode / tsconfig avanzado → T01 ya lo cubre o es T08
> - Pattern matching → T04 o T14
> - Programación reactiva (RxJS) → T04 o fuera de scope

---

## Materiales y Referencias

| Fuente | Capítulo | Relevancia |
|--------|----------|------------|
| Gabbrielli & Martini (2023) | Cap. 11 — *Functional Programming Paradigm* | ⭐⭐⭐ Teoría central del paradigma |
| Sebesta (2018) | Cap. 15 — *Functional Programming Languages* | ⭐⭐⭐ Historia, Lisp/Scheme, comparación imperativo/funcional |
| Filminas 2025 (base) | *Intro FP con Kotlin* | ⭐⭐ Base adaptada — Kotlin → TypeScript |
| Schmidt & Runfola (2026) | *Going Beyond Programming* | ⭐ Bloque IA |

---

## Notas del Diseñador

- **Clojure como contraste:** el docente debe advertir desde el arranque que Clojure se usa en modo *lectura*: veremos su sintaxis, la analizaremos comparativamente, pero no se programa en Clojure en esta clase. La carga cognitiva de aprender dos lenguajes nuevos en 120 min sería excesiva.
- **TypeScript estilo puro:** reforzar en cada bloque que el estilo funcional es *una elección* que hacemos en TypeScript, no lo que TypeScript obliga. Esto diferencia T03 de T01 donde TypeScript fue presentado como multiparadigma.
- **Material 2025:** las filminas base están escritas para Kotlin — la adaptación a TypeScript es directa para la mayoría de los conceptos (especialmente HOF y closures). Los ejemplos de `tailrec` de Kotlin no tienen equivalente garantizado en TypeScript/JavaScript — se debe dejar en claro esta limitación.
