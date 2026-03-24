# Filminas — Tema 03: Introducción a Programación Funcional con TypeScript

> **Estado:** GENERADA
> **Agente:** Dr. Roberto (class-writer)
> **Fecha:** 2026-03-23
> **Duración total:** 120 minutos · 8 bloques · 29 filminas (F-00 portada + F-01 a F-28)
> **Formato:** Markdown estructurado para exportar a presentación
> **Input:** `temas/03-intro-funcional-ts/diseno.md` (aprobado)

---

## PORTADA

---

### [1]

# Introducción a Programación Funcional con TypeScript

**Paradigmas y Lenguajes de Programación 2026**
Universidad Nacional de Tierra del Fuego — IDEI

Semana 2 · Clase 1 de 1 · 120 minutos

*Lenguaje principal: TypeScript (estilo puro) · Contraste: Clojure*

@imagen: background
@prompt-imagen: prompt="Dark abstract background with lambda symbol (λ) in minimalist white lines, computational mathematics aesthetic, university lecture style"

---

## BLOQUE 0 — Recap y punto de partida (5 min)

---

### [2]

# ¿Dónde estamos?

**En T01 vimos el mapa de los paradigmas:**

| Paradigma | Raíz formal | Unidad |
|-----------|-------------|--------|
| Imperativo | Máquina de Turing | Instrucción + estado |
| Orientado a Objetos | Imperativo + encapsulamiento | Objeto / mensaje |
| **Funcional** | **λ-cálculo (Church, 1936)** | **Función** |
| Lógico | Lógica simbólica | Relación / hecho |

> *"Hoy nos adentramos en el funcional. Y empezamos con una pregunta rara:"*

**¿Qué tiene de especial un lenguaje donde ninguna variable cambia de valor?**

---

## BLOQUE 0.5 — Historia y Raíces Formales (15 min)

---

### [3]

# El problema que lo originó todo

## El *Entscheidungsproblem* — Hilbert, 1928

> *"¿Existe un algoritmo mecánico que, dado cualquier enunciado matemático, determine en tiempo finito si es verdadero o falso?"*

**Por qué importaba:**
- Era la pregunta central del programa formalista de Hilbert
- Para responderla había que definir primero: ¿qué es un **algoritmo mecánico**?
- Esa definición dio origen a dos modelos de cómputo que cambiaron la historia

@imagen: content
@prompt-imagen: prompt="Portrait of David Hilbert with a chalkboard showing mathematical formulas, academic early 20th century style, black and white"

---

### [4]

# La respuesta de Turing: la máquina con cinta (1936)

**Modelo:** cabezal + cinta infinita + tabla de transiciones

```
Estado q0 → lee '0' → escribe '1', mueve derecha → pasa a q1
Estado q0 → lee '1' → escribe '0', mueve derecha → pasa a q2
...
```

**El cómputo avanza *modificando estado* paso a paso**

- Variables = celdas de la cinta
- Instrucciones = filas de la tabla de transiciones
- Programa = la tabla completa

> *"Es esencialmente un modelo del calculador humano: alguien con papel, lápiz y borrador."*

**Respuesta al Entscheidungsproblem:** NO — el **Problema de la Parada** (*Halting Problem*) es indecidible

---

### [5]

# La respuesta de Church: el λ-cálculo (1936)

**Un camino completamente diferente al mismo resultado**

El λ-cálculo tiene un solo concepto primitivo: la **función**

| Operación | Notación | Ejemplo |
|-----------|----------|---------|
| Definir una función | `λx. expr` | `λx. x * x` = "la función que eleva al cuadrado" |
| Aplicar una función | `f arg` | `(λx. x * x) 3` |
| Reducción β (cómputo) | sustituir argumento | `(λx. x * x) 3 → 3 * 3 → 9` |

**NO existen:**
- Variables que cambien de valor
- Celdas de memoria
- Pasos secuenciales

**Solo hay expresiones que se transforman en otras expresiones**

---

### [6]

# El cómputo como reescritura

**Factorial de 3 en el λ-cálculo** *(Gabbrielli & Martini, Cap. 11.1.2)*

```
fact 3
  → if 3=0 then 1 else 3 * fact(3-1)
  → 3 * fact(2)
  → 3 * (2 * fact(1))
  → 3 * (2 * (1 * fact(0)))
  → 3 * (2 * (1 * 1))
  → 6
```

> *"No hay variables. No hay memoria. No hay pasos. Solo sustitución de expresiones."*

**Esto es la esencia del paradigma funcional**

---

### [7]

# Dos respuestas al mismo problema → dos paradigmas

| | Máquina de Turing | λ-cálculo de Church |
|---|---|---|
| Unidad básica | Estado + transición | Función + aplicación |
| El cómputo... | ...modifica estado | ...reduce expresiones |
| ¿Hay memoria? | Sí — la cinta | No — solo el entorno |
| Metáfora | Calculador con libreta | Matemático ecuando |
| Paradigma | **Imperativo** | **Funcional** |

**Son computacionalmente equivalentes — Tesis de Church-Turing (1937)**

**La consecuencia histórica:**
- Von Neumann (1945) implementó físicamente el modelo de Turing → CPU + RAM
- Los primeros lenguajes (Fortran, COBOL) siguieron ese modelo
- El λ-cálculo quedó académico… hasta 1958

---

### [8]

# De la teoría a la práctica: la línea de tiempo

| Año | Hito | Por qué importa |
|-----|------|-----------------|
| 1936 | **λ-cálculo** (Church) | La base matemática |
| 1936 | Máquina de Turing | La base del imperativo — *el mismo año* |
| 1958 | **Lisp** (McCarthy, MIT) | Primer LP funcional: GC, HOF, recursión |
| 1964 | Máquina SECD (Landin) | Primera máquina abstracta para HOF |
| 1975 | **Scheme** | Lisp puro y pequeño — base de la educación CS |
| 1977 | Backus — ACM Turing Award | El creador de Fortran critica el imperativo |
| 1990 | **Haskell** | Funcional puro con tipos — estándar académico |
| 2007 | **Clojure** | Lisp moderno en la JVM, inmutabilidad por defecto |
| 2012+ | **TypeScript / ES6+** | El funcional llega al mainstream web |

> *Backus (1978): "Programs written in a purely functional style are easier to understand because the meanings of expressions are independent of their context."*
> — Hoy lo llamamos **transparencia referencial** *(Sebesta, Cap. 15.1)*

---

## BLOQUE 1 — Fundamentos del Paradigma Funcional (20 min)

---

### [9]

# La función matemática como modelo

**Una función matemática:** `f : A → B`
- Para cada `a ∈ A` existe exactamente un `b ∈ B` tal que `f(a) = b`

**Tres propiedades que la distinguen de un procedimiento:**

| Propiedad | Significado |
|-----------|-------------|
| **Determinismo** | El resultado depende *solo* del input — nada más |
| **Sin efecto colateral** | Evaluar `f(x)` no cambia nada fuera de `f` |
| **Sin historia** | No importa cuántas veces se evaluó antes |

**¿`getTime()` es una función matemática?**
> $t_1 \neq t_2 \Rightarrow$ `getTime()` ≠ función matemática

*Un programa funcional es un sistema de ecuaciones matemáticas, no un guión de instrucciones *(Sebesta, Cap. 15.2)**

---

### [10]

# Cómputo sin estado

**Modelo imperativo:**
> cómputo = transformación de estado → variables = celdas → asignación = operación central

**Modelo funcional:**
> cómputo = reescritura de expresiones — sin estado, sin memoria mutable

**Axioma central** *(Gabbrielli & Martini, Cap. 11)*:
> *"Si el entorno está fijo, una expresión siempre denota el mismo valor."*

**Consecuencias:**
- Sin asignación → la iteración pierde sentido
- **La recursión es el mecanismo primario de control de flujo**
- **Transparencia referencial:** `f(x)` devuelve siempre lo mismo para el mismo `x`

@imagen: content
@prompt-imagen: prompt="Diagram comparing imperative model (boxes with arrows showing state mutation, variable reassignment) vs functional model (expression tree reduction, lambda symbols, no mutation), clean academic illustration style"

---

### [11]

# Funciones puras vs. impuras

**Función pura:**
1. Mismo input → mismo output (siempre)
2. Sin efectos colaterales observables

**Función impura:**
- Depende de estado externo, O
- Modifica estado externo

```typescript
// ✅ PURA — el resultado solo depende de a y b
const suma = (a: number, b: number): number => a + b;

// ❌ IMPURA — depende del estado del sistema
const getSaldo = (): number => bancoDB.query("saldo");

// ❌ IMPURA — efecto colateral: escritura a consola
const log = (msg: string): void => console.log(msg);
```

> *"Los efectos no desaparecen — se aíslan en los bordes del sistema."*

---

### [12]

# Inmutabilidad — no hay variables, hay bindings

**En el imperativo:** variable = celda de memoria reutilizable
```
x = 5
x = x + 1   // misma celda, nuevo valor
```

**En el funcional:** binding = ligadura nombre → valor (una sola vez)
```
val x = 5   // (ML) declaración — no "asignación"
```

**En TypeScript:**
```typescript
const x = 5;
// x = 6; // Error de compilación — no es reasignable
```

**Beneficios:**
- Razonamiento local: el valor no cambia mientras uno lee el código
- Paralelismo seguro: no hay condiciones de carrera
- Debugging predecible

> *Sebesta: "Variables in pure functional languages are bound to values only once." (Cap. 15.3)*

---

## BLOQUE 2 — TypeScript Funcional: Funciones como Valores (20 min)

---

### [13]

# Funciones como ciudadanos de primera clase

**Una función es un valor** — se puede guardar, pasar, devolver

```typescript
// Definir (binding)
const duplicar = (n: number): number => n * 2;

// Guardar en variable
const operacion: (x: number) => number = duplicar;

// Pasar como argumento
const aplicar = (f: (x: number) => number, valor: number): number =>
  f(valor);

console.log(aplicar(duplicar, 5));  // 10
```

**Regla de oro en estilo funcional:**
- ✅ Solo `const`
- ❌ No `let`, no `var`
- ❌ No `for`, no `while`
- ❌ No mutación

---

### [14]

# Inmutabilidad en TypeScript: `readonly`

**`const` no alcanza para objetos — `readonly` sí:**

```typescript
type Punto = {
  readonly x: number;
  readonly y: number;
};

const p: Punto = { x: 3, y: 4 };
// p.x = 10;  // ❌ Error de compilación ✓

// ReadonlyArray — arrays inmutables
const nums: ReadonlyArray<number> = [1, 2, 3];
// nums.push(4);  // ❌ Error de compilación ✓
```

**El patrón funcional: transformar en lugar de mutar**

```typescript
// ❌ Imperativo (mutación):
// nums.push(4);

// ✅ Funcional (nueva colección):
const nuevoNums = [...nums, 4];
// => [1, 2, 3, 4]  — nums sigue siendo [1, 2, 3]
```

---

### [15]

# Contraste: inmutabilidad en Clojure

**En TypeScript:** la inmutabilidad es una elección — usamos `const` y `readonly`

**En Clojure:** la inmutabilidad es el default — no hay forma de mutar (a menos que se use explícitamente `atom`)

```clojure
; En Clojure, los datos son inmutables por defecto
(def nums [1 2 3])

(conj nums 4)
; => [1 2 3 4]  — nueva colección
; nums sigue siendo [1 2 3]

; La diferencia con TypeScript:
; en TS elegimos no mutar
; en Clojure no podemos mutar aunque quisiéramos
```

> *"Esta diferencia es la que separa un lenguaje multiparadigma de uno funcional puro."*

---

### [16]

# Arrow functions y funciones anónimas (lambdas)

**Lambda = función sin nombre — el concepto de Church llevado a TypeScript**

```typescript
// Lambda (función anónima)
const cuadrado = (x: number): number => x * x;

// Equivalencia con λ-cálculo:
// λx. x * x   →   (x: number) => x * x
```

**Closures — una función que captura su entorno léxico:**

```typescript
const crearSumador = (n: number) => (x: number) => x + n;

const sumar5 = crearSumador(5);  // captura n=5
console.log(sumar5(3));   // 8
console.log(sumar5(10));  // 15
```

**`sumar5` lleva consigo el valor de `n = 5`** — es una clausura

---

### [17]

# Contraste: closures en Clojure

```clojure
; Clojure — misma semántica, distinta sintaxis
(defn crear-sumador [n]
  (fn [x] (+ x n)))

(def sumar5 (crear-sumador 5))
(sumar5 3)   ; => 8
(sumar5 10)  ; => 15
```

**Ámbito léxico:** la closure recuerda el entorno donde fue *definida*, no donde se *llama*

| | TypeScript | Clojure |
|---|---|---|
| Lambda | `(x) => x + n` | `(fn [x] (+ x n))` |
| Binding | `const f = ...` | `(def f ...)` |
| Closure | captura `const` del entorno | captura bindings del entorno |
| Scope | léxico | léxico |

> *"El ámbito léxico es el mismo en ambos. La sintaxis cambia, la semántica no."*

---

## BLOQUE 3 — Funciones de Orden Superior (30 min)

---

### [18]

# ¿Qué es una función de orden superior?

**HOF:** función que toma funciones como argumentos **o** devuelve funciones como resultado

> *Gabbrielli & Martini: "Higher-order functions and recursion are the basic ingredients of the stateless computational model." (Cap. 11)*

**Las tres HOF fundamentales en TypeScript:**

| HOF | ¿Qué hace? | Tipo |
|-----|-----------|------|
| `map` | Transforma cada elemento | `(A => B) => A[] => B[]` |
| `filter` | Selecciona elementos | `(A => bool) => A[] => A[]` |
| `reduce` | Pliega a un valor | `((B,A) => B) => B => A[] => B` |

> *"Estas tres son el toolkit mínimo del paradigma funcional aplicado."*

---

### [19]

# `map` — Transformar colecciones

**Semántica:** aplica una función pura a cada elemento, devuelve nuevo array

```typescript
const nums: ReadonlyArray<number> = [1, 2, 3, 4, 5];

// Con lambda inline
const dobles = nums.map(n => n * 2);
// => [2, 4, 6, 8, 10]  — nums sin cambiar ✓

// Con función nombrada
const esPar = (n: number): boolean => n % 2 === 0;
const sonPares = nums.map(esPar);
// => [false, true, false, true, false]
```

**Tipo de `map`:** `Array<A>.map<B>(f: (a: A) => B): B[]`

**En Clojure:**
```clojure
(map #(* % 2) [1 2 3 4 5])  ; => (2 4 6 8 10)
```

> *"`map` abstrae el patrón "aplicar algo a cada elemento" — elimina el `for` loop.*

---

### [20]

# `filter` — Seleccionar elementos

**Semántica:** retiene solo los elementos donde el predicado devuelve `true`

```typescript
const pares = [1, 2, 3, 4, 5, 6].filter(n => n % 2 === 0);
// => [2, 4, 6]

type Producto = { readonly nombre: string; readonly precio: number };
const catalogo: ReadonlyArray<Producto> = [
  { nombre: "Laptop",  precio: 1200 },
  { nombre: "Mouse",   precio: 25 },
  { nombre: "Monitor", precio: 400 },
];

const económicos = catalogo.filter(p => p.precio < 100);
// => [{ nombre: "Mouse", precio: 25 }]
```

**En Clojure:**
```clojure
(filter even? [1 2 3 4 5 6])  ; => (2 4 6)
```

---

### [21]

# `reduce` — Plegar a un valor

**Semántica:** combina todos los elementos en un único resultado usando un acumulador

```typescript
const nums = [1, 2, 3, 4, 5];

// Suma
const suma = nums.reduce((acc, n) => acc + n, 0);   // 15

// Máximo
const max = nums.reduce((acc, n) => n > acc ? n : acc, nums[0]);   // 5
```

**Tipo:** `Array<A>.reduce<B>(f: (acc: B, val: A) => B, init: B): B`

**En Clojure:**
```clojure
(reduce + 0 [1 2 3 4 5])  ; => 15
```

> *"`reduce` es la más poderosa — `map` y `filter` pueden implementarse con `reduce`."*

---

### [22]

# El pipeline funcional: map → filter → reduce

**Problema:** dado el catálogo, obtener el precio total de los productos económicos

```typescript
type Producto = { readonly nombre: string; readonly precio: number };
const catalogo: ReadonlyArray<Producto> = [
  { nombre: "Laptop",  precio: 1200 },
  { nombre: "Mouse",   precio: 25 },
  { nombre: "Teclado", precio: 80 },
  { nombre: "Monitor", precio: 400 },
];

// Pipeline funcional — sin ninguna variable mutable
const totalEconómicos = catalogo
  .filter(p => p.precio < 100)
  .map(p => p.precio)
  .reduce((acc, precio) => acc + precio, 0);
// => 105
```

**En Clojure:**
```clojure
(->> catalogo
     (filter #(< (:precio %) 100))
     (map :precio)
     (reduce + 0))
; => 105
```

> *"No hay secuencia de estados. Solo transformación de datos."*

---

## BLOQUE 4 — Clausuras, Ámbito Léxico y Recursión (15 min)

---

### [23]

# Clausuras: fábricas de funciones

**Aplicación práctica:** funciones configurables con closures

```typescript
const crearMultiplicador = (factor: number) =>
  (x: number): number => x * factor;

const triple  = crearMultiplicador(3);
const décuplo = crearMultiplicador(10);

[1, 2, 3].map(triple);   // => [3, 6, 9]
[1, 2, 3].map(décuplo);  // => [10, 20, 30]
```

**Ámbito léxico vs. dinámico:**

| | Léxico (TypeScript, Clojure) | Dinámico |
|---|---|---|
| La closure captura | El entorno donde fue *definida* | El entorno donde se *llama* |
| Resultado | **Predecible** | Imprevisible |
| Transparencia referencial | ✅ Se mantiene | ❌ Se rompe |

> *"La composición de estas funciones (`triple ∘ décuplo`) viene en T04."*

---

### [24]

# Recursión — el `for` loop del paradigma funcional

**Sin `for`, sin `while` — la recursión es el único mecanismo de iteración en el paradigma puro**

```typescript
// Versión directa
const factorial = (n: number): number =>
  n <= 1 ? 1 : n * factorial(n - 1);
```

```clojure
(defn factorial [n]
  (if (<= n 1)
    1
    (* n (factorial (- n 1)))))
```

**Anatomía de la recursión funcional:**
1. **Caso base** — el valor que no necesita más reducción
2. **Caso recursivo** — reducir el problema y combinar resultados parciales

> *"Es la evaluación por sustitución del λ-cálculo en acción."*

---

### [25]

# Tail Recursion — recursión eficiente

**Problema:** la recursión directa consume `O(n)` espacio en la pila de llamadas

**Solución:** tail recursion con acumulador

```typescript
// Acumulador evita crecer la pila
const factAux = (n: number, acc: number): number =>
  n <= 1 ? acc : factAux(n - 1, n * acc);

const factorial = (n: number): number => factAux(n, 1);
```

```clojure
; En Clojure, recur garantiza TCO (tail-call optimization)
(defn factorial [n]
  (loop [n n acc 1]
    (if (<= n 1) acc
      (recur (- n 1) (* n acc)))))
```

> ⚠️ *Nota TypeScript/JavaScript: el runtime NO garantiza TCO. El patrón es correcto conceptualmente, pero en producción con n grande: usar trampolín o iteración.*

---

## BLOQUE IA — IA Generativa y el Paradigma Funcional (10 min)

---

### [26]

# Pensar funcionalmente para trabajar con IA

> *Schmidt & Runfola (2026): "What matters is no longer just fluency in traditional programming languages but the ability to think computationally."*

**El funcional como lenguaje de especificación para IA:**

Las HOF describen *qué* se quiere, no *cómo* lograrlo — los LLMs entienden mejor las especificaciones declarativas

| Forma | Prompt |
|-------|--------|
| ❌ Imperativa | "Iterá sobre el array, si el elemento es par…" |
| ✅ Funcional | "Aplicá `filter(esPar).map(doble)` sobre el array" |

**El funcional como defensa ante código generado inseguro:**
- Funciones puras son fáciles de testear unitariamente — `f(input)` → verificar output, sin mocks
- Código generado con efectos colaterales es difícil de auditar
- Una función pura incorrecta falla de forma *visible y predecible*

---

### [27]

# La IA puede mentirte: cómo detectarlo

**La IA puede generar código "con aspecto funcional" que en realidad muta estado:**

```typescript
// Parece funcional — en realidad no lo es
const procesarLista = (items: string[]): string[] => {
  const resultado: string[] = [];
  items.forEach(item => resultado.push(item.toUpperCase())); // ❌ mutación
  return resultado;
};

// Funcional real:
const procesarLista = (items: ReadonlyArray<string>): ReadonlyArray<string> =>
  items.map(item => item.toUpperCase()); // ✅ sin mutación
```

**Checklist de auditoría para código generado:**
- [ ] ¿Usa solo `const`?
- [ ] ¿Hay `push`, `pop`, `splice`, reasignación de propiedades?
- [ ] ¿El tipo de retorno coincide con el tipo del input (transformado)?
- [ ] ¿La función tiene efectos colaterales ocultos?

---

## CIERRE (5 min)

---

### [28]

# Resumen de hoy

| Concepto | Key takeaway |
|----------|-------------|
| Entscheidungsproblem | Church y Turing resolvieron el mismo problema con modelos opuestos |
| λ-cálculo | Cómputo = reescritura de expresiones, sin estado |
| Función pura | Determinismo + sin efectos colaterales |
| Inmutabilidad | No variables — bindings. `const` + `readonly` en TypeScript |
| Ciudadanía de primera clase | Las funciones son valores que se pasan y devuelven |
| HOF | `map`, `filter`, `reduce` — el toolkit funcional básico |
| Clausuras | Capturan el entorno léxico — fábricas de funciones |
| Recursión | El `for` loop del paradigma funcional |

**Próxima clase (T04):** Composición de funciones · Aplicación parcial · Currificación

**Pregunta para pensar:** *¿Cuándo NO usarías estilo funcional en un proyecto real de TypeScript?*
