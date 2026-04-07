## PORTADA

---

### [F-01] Portada

@tipo: portada
@imagen: background
@prompt-imagen: fondo oscuro abstracto con circuitos y símbolos matemáticos lambda (λ) y letras griegas en tonos azul profundo, estilo académico-tecnológico

# Introducción a Programación Funcional con TypeScript

Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
Tema 03 · Módulo II

---

## BLOQUE A0 — Historia: del Entscheidungsproblem al funcional

---

### [F-02] El origen: una pregunta de 1928

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: retrato estilizado de David Hilbert frente a un pizarrón con fórmulas matemáticas formales, estilo ilustración académica en blanco y negro con acentos azul

# El Entscheidungsproblem

## David Hilbert, 1928

> "¿Existe un procedimiento mecánico que, dado cualquier enunciado matemático, determine si es verdadero o falso?"

## Por qué importa

- Hilbert buscaba fundamentar *toda* la matemática en un sistema formal decidible
- Esta pregunta define qué pueden y qué no pueden hacer las computadoras
- La respuesta llegó en 1936 — desde dos lugares a la vez, sin coordinación

---

### [F-03] Alan Turing — La Máquina (Cambridge, 1936)

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama simple de una Máquina de Turing: cinta infinita con celdas, cabeza lectora/escritora y tabla de estados, estilo diagrama técnico en colores azul y gris

# La Máquina de Turing

## El modelo

- Dispositivo abstracto: cinta infinita + cabeza de lectura/escritura + tabla de estados
- Computa **modificando** el estado de la cinta paso a paso

## El resultado

- Demostró el **halting problem**: ningún algoritmo puede decidir si un programa arbitrario termina
- → El Entscheidungsproblem **no tiene solución general**

## El legado en LP

- Máquina de Turing → arquitectura von Neumann → **paradigma imperativo**
- *"On Computable Numbers"*, 1936, Proceedings of the London Mathematical Society

---

### [F-04] Alonzo Church — El λ-cálculo (Princeton, 1936)

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: retrato estilizado de Alonzo Church con fórmulas de lambda cálculo flotando alrededor — β-reducción: (λx.x*x) 3 → 3*3 → 9 — estilo ilustración académica azul

# El λ-cálculo de Church

## El modelo

- Sistema formal donde todo es **función** — el cómputo es **sustitución de expresiones**
- No hay estado, no hay memoria: solo transformaciones de expresiones

## El resultado

- Demostró que el problema de equivalencia de funciones tampoco tiene solución
- → El Entscheidungsproblem **no tiene solución general** (camino independiente)

## El legado en LP

- λ-cálculo → Lisp (1958) → **paradigma funcional**
- *"An Unsolvable Problem of Elementary Number Theory"*, 1936, Annals of Mathematics

---

### [F-05] Dos filosofías de computación

@tipo: tabla-comparativa
@imagen: none

# Church vs Turing: misma respuesta, distinto legado

## La Tesis Church-Turing

Todo lo computable por uno es computable por el otro → **equivalentes en poder**

## Dos formas de computar

| | **Turing → von Neumann → Imperativo** | **Church → λ-cálculo → Funcional** |
|---|---|---|
| **Computar es…** | Modificar el estado de una cinta/memoria | Reducir una expresión a su forma normal |
| **Elemento central** | Variable mutable + asignación | Función + sustitución |
| **Control de flujo** | Instrucciones secuenciales, loops | Recursión, composición de funciones |
| **Primer lenguaje** | Fortran (1957) | Lisp (1958) |

> ⚠️ El λ-cálculo no nació como lenguaje de programación — nació para demostrar que un problema matemático era **imposible**

---

### [F-06] Recorrido de lenguajes funcionales — parte 1 (1958–1990)

@tipo: timeline
@imagen: none

# Lenguajes funcionales: cada uno responde a su época (1958–1990)

| Año | Lenguaje | Creador / Origen | Nicho actual |
|---|---|---|---|
| 1958 | **Lisp** | John McCarthy — MIT | IA simbólica, Emacs Lisp, primer funcional |
| 1962 | **APL** | Kenneth Iverson — IBM | Computación matricial, precursor del data science |
| 1973 | **ML** | Robin Milner — Edinburgh | Compiladores, verificación formal, inferencia de tipos |
| 1975 | **Scheme** | Steele/Sussman — MIT | Educación, investigación — base teórica de muchos cursos |
| 1985 | **Miranda** | David Turner — Kent | Primer lenguaje puramente lazy; origen directo de Haskell |
| 1986 | **Erlang** | Armstrong — Ericsson | Telecomunicaciones, concurrencia masiva (*WhatsApp* en producción) |
| 1990 | **Haskell** | Comité académico | Finanzas cuantitativas, compiladores, criptografía |

> Cada lenguaje nació para **resolver un problema concreto**, no como ejercicio académico

---

### [F-07] Recorrido de lenguajes funcionales — parte 2 (2003–2012)

@tipo: timeline
@imagen: none

# Lenguajes funcionales: modernos y sus nichos (2003–2012)

| Año | Lenguaje | Creador / Origen | Nicho actual |
|---|---|---|---|
| 2003 | **Scala** | Odersky — EPFL | Big Data (*Apache Spark*, *Kafka*), backend JVM |
| 2005 | **F#** | Don Syme — Microsoft | Finanzas cuantitativas, modelado científico en .NET |
| 2007 | **Clojure** | Rich Hickey | Concurrencia, datos inmutables, **blockchain** (*Datomic*) |
| 2012 | **Elixir** | José Valim | Web en tiempo real, IoT, telecomunicaciones (corre sobre BEAM/Erlang) |

## Por qué esta época

- Los problemas de **concurrencia y escala** se volvieron inmanejables con estado mutable compartido
- El funcional los **elimina por diseño** — no por disciplina del programador

---

### [F-08] ¿Por qué el funcional entró en los lenguajes multiparadigma?

@tipo: tabla-comparativa
@imagen: none

# El funcional en los multiparadigma: causa y adopción

## La causa: el fin del clock scaling

A mediados de los 2000s los CPUs dejaron de crecer en frecuencia → pasaron a **múltiples núcleos**
→ Estado mutable compartido entre threads genera condiciones de carrera
→ El funcional **elimina el problema de raíz**

## La adopción

| Lenguaje | Año | Qué incorporó |
|---|---|---|
| **Java** | 2014 (Java 8) | Lambdas, Stream API, `Optional` |
| **JavaScript** | 2015 (ES6) | Arrow functions, `.map()`, `.filter()`, `.reduce()` |
| **TypeScript** | desde 2012 | Todo JS funcional + tipos estáticos, `readonly`, union types |
| **C++** | 2011 (C++11) | Lambdas, `std::function`, `std::transform` |
| **Python** | desde 2.x | `map`, `filter`, `functools`, list comprehensions |
| **Rust** | 2015 | Immutability by default, closures, ownership sin GC |
| **Kotlin / Swift** | 2011 / 2014 | `val`, colecciones funcionales, closures, value semantics |

> La tendencia **no reemplazó al imperativo — lo enriqueció**: I/O + performance en imperativo, transformación de datos + concurrencia en funcional

---

### [F-09] Frase de anclaje

@tipo: socratica
@imagen: background
@prompt-imagen: fondo abstracto con símbolo λ grande y circuitos digitales difuminados, tonos azul oscuro y plateado, estilo minimalista

# "Si el paradigma imperativo es la Máquina de Turing hecha lenguaje…

## …el funcional es el λ-cálculo de Church hecho lenguaje."

Aprender ambos no es aprender dos herramientas —
es entender las **dos formas fundamentales** de formalizar la computación.

> **Para reflexionar:** ¿Cuándo conviene computar modificando estado vs computando reduciendo expresiones?

---

## BLOQUE A — ¿Qué es el paradigma funcional?

---

### [F-10] Dos formas de resolver el mismo problema — imperativo

@tipo: codigo
@imagen: none

# El mismo problema: sumar cuadrados de pares — versión imperativa

## ¿Qué queremos? Sumar el cuadrado de los números pares

```typescript
// ❌ Estilo imperativo — describe el CÓMO

const numeros = [1, 2, 3, 4, 5, 6];
let suma = 0;                           // acumulador mutable externo

for (let i = 0; i < numeros.length; i++) {  // loop — detalle de iteración
  if (numeros[i] % 2 === 0) {               // filtro inline
    suma += numeros[i] * numeros[i];         // acumulación con mutación
  }
}

console.log(suma); // 56
```

## Identificar los problemas

- `suma` vive afuera del loop: cualquier código puede modificarla
- El loop mezcla *cómo iterar* con *qué hacer*
- Para entender el resultado hay que simular mentalmente el estado paso a paso

---

### [F-11] Dos formas de resolver el mismo problema — funcional

@tipo: codigo
@imagen: none

# El mismo problema — versión funcional

## ¿Qué queremos? Sumar el cuadrado de los números pares

```typescript
// ✅ Estilo funcional — describe el QUÉ

const numeros = [1, 2, 3, 4, 5, 6];

const suma = numeros
  .filter(n => n % 2 === 0)          // seleccionar pares: [2, 4, 6]
  .map(n => n * n)                    // elevar al cuadrado: [4, 16, 36]
  .reduce((acc, n) => acc + n, 0);   // sumar: 56

// suma = 56 — sin variables intermedias mutables
```

## ¿Qué ganamos?

- **Trazabilidad**: cada línea hace *una sola cosa*, con nombre explícito
- **Testeable por partes**: puedo testear `filter`, `map` y `reduce` por separado
- **Paralelizable**: ninguna operación depende del estado externo
- Lee como una especificación del problema, no como instrucciones de máquina

---

### [F-12] El modelo funcional — cómputo como reescritura de expresiones

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de reducción de expresiones: árbol con nodos que se reemplazan por sus valores paso a paso, arrows mostrando sustitución, fondo blanco con colores azul y verde

# Computar = reducir expresiones (no modificar estado)

## Ejemplo de reducción (β-reducción del λ-cálculo)

```
suma(suma(1, 2), suma(3, 4))
  → suma(3, suma(3, 4))          // se sustituye suma(1,2) por 3
  → suma(3, 7)                    // se sustituye suma(3,4) por 7
  → 10                            // resultado final
```

## La consecuencia fundamental

En cada paso no se "modifica" nada — se **reemplaza** una expresión por su equivalente

→ El mismo input **siempre** produce el mismo output
→ El resultado no depende del "estado de la máquina" en ese momento

> Este es el modelo del λ-cálculo de Church (§11.1, Gabbrielli-Martini)

---

## BLOQUE B — Los tres pilares

---

### [F-13] Pilar 1: Funciones puras — definición

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama caja negra de una función: flecha de entrada, caja con "f(x)" y flecha de salida, sin flechas laterales (sin efectos), fondo blanco con azul

# Pilar 1: Funciones Puras

## Definición

Una función es **pura** si:
1. Su salida depende **únicamente** de su entrada
2. No produce **efectos colaterales** observables (no modifica variables externas, no hace I/O, no lanza excepciones con side effects)

## ¿Por qué importa?

| Propiedad | Consecuencia |
|---|---|
| Predecible | Mismos args → mismo resultado — siempre |
| Testeable en aislamiento | No necesita setup/teardown de estado global |
| Segura en paralelo | No compite por estado compartido con otros threads |
| Razonable localmente | Para entender la función, solo hay que leer la función |

---

### [F-14] Pilar 1: Funciones puras — impura vs pura en TypeScript

@tipo: codigo
@imagen: none

# Función impura vs función pura — TypeScript

## ❌ Impura: lee y modifica estado externo

```typescript
let contador = 0;

// Esta función NO es pura:
// - lee `contador` del scope externo
// - lo modifica como efecto colateral
const incrementar = (): number => {
  contador++;          // ← efecto colateral: modifica estado externo
  return contador;    // ← resultado depende del estado externo
};

incrementar(); // → 1
incrementar(); // → 2   ← mismo llamado, distinto resultado
```

## ✅ Pura: entrada → salida, sin efectos

```typescript
// Esta función SÍ es pura:
// - solo usa sus argumentos
// - devuelve siempre el mismo resultado para los mismos inputs
const sumar = (a: number, b: number): number => a + b;

sumar(3, 4); // → 7   — siempre 7, sin importar cuándo se llame
sumar(3, 4); // → 7   — predecible como una función matemática
```

---

### [F-15] Pilar 1: Funciones puras — en Clojure

@tipo: codigo
@imagen: none

# Funciones puras en Clojure

## En Clojure, las funciones son puras por defecto

```clojure
;; ✅ Función pura — mismo resultado siempre
(defn sumar [a b]
  (+ a b))              ; solo usa sus argumentos

(sumar 3 4)  ; → 7
(sumar 3 4)  ; → 7 — siempre

;; ✅ Función pura con múltiples pasos
(defn cuadrado-de-par? [n]
  (if (even? n)        ; even? es una función pura
    (* n n)            ; devuelve el cuadrado si es par
    nil))              ; nil si no lo es

(cuadrado-de-par? 4)   ; → 16
(cuadrado-de-par? 3)   ; → nil
```

## Por qué Clojure facilita la pureza

- No hay asignación destructiva: `def` crea una ligadura nueva, no modifica la anterior
- Las estructuras de datos no tienen métodos mutadores
- Los efectos colaterales deben ser explícitos (el lenguaje los hace "ruidosos")

---

### [F-16] Pilar 2: Inmutabilidad — `const` en TypeScript

@tipo: codigo
@imagen: none

# Pilar 2: Inmutabilidad — TypeScript

## `const`: la referencia no se puede reasignar

```typescript
const x = 10;
// x = 20;  // ❌ Error de compilación: no se puede reasignar const

const numeros = [1, 2, 3];
// numeros = [4, 5, 6];  // ❌ Error: la referencia no puede cambiar
```

## ⚠️ Pero el contenido sí puede mutar (si no tomamos precauciones)

```typescript
const numeros = [1, 2, 3];
numeros.push(4);  // ✅ Compila — pero es mutación oculta, rompe el paradigma
console.log(numeros); // [1, 2, 3, 4] — el array "cambió"
```

## ✅ Estilo funcional: crear nueva colección en lugar de mutar

```typescript
const numeros = [1, 2, 3] as const;  // readonly array
const masNumeros = [...numeros, 4];   // nuevo array — el original intacto

console.log(numeros);     // [1, 2, 3]   — intacto
console.log(masNumeros);  // [1, 2, 3, 4]
```

---

### [F-17] Pilar 2: Inmutabilidad nativa en Clojure

@tipo: codigo
@imagen: none

# Pilar 2: Inmutabilidad — Clojure (nativa, no opt-in)

## En Clojure: ninguna estructura es mutable por defecto

```clojure
;; Una lista en Clojure
(def numeros '(1 2 3))

;; conj agrega un elemento — devuelve una NUEVA lista
(def mas-numeros (conj numeros 4))

(println numeros)       ; → (1 2 3)     ← intacta, siempre
(println mas-numeros)   ; → (4 1 2 3)   ← nueva lista

;; No existe ningún método para "push" en la original
;; La "mutación" es imposible por diseño del runtime
```

## Structural sharing — sin overhead real

- Clojure usa **persistent data structures**: la nueva colección comparte la memoria interna de la original
- Crear `mas-numeros` no copia todos los elementos — solo agrega el puntero al nuevo nodo
- Es eficiente **y** seguro en múltiples threads simultáneos (nadie puede ver un estado intermedio)

## La diferencia con TypeScript

| | TypeScript | Clojure |
|---|---|---|
| Inmutabilidad | Opt-in (`as const`, `readonly`) | **Nativa — siempre** |
| Quién la garantiza | El programador (disciplina) | El lenguaje (diseño) |

---

### [F-18] Pilar 3: Transparencia referencial

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de sustitución: expresión "cuadrado(3)" con flecha rotulada "reemplazar por valor" apuntando a "9", sin cambios de contexto alrededor, colores azul y verde claro

# Pilar 3: Transparencia Referencial

## Definición

Una expresión tiene **transparencia referencial** si puede ser reemplazada por su valor sin cambiar el comportamiento del programa

## Ejemplo — expresión referencialmente transparente

```typescript
const cuadrado = (n: number): number => n * n;

// Puedo reemplazar cuadrado(3) por 9 en cualquier parte del código
// sin cambiar el resultado:
const a = cuadrado(3) + cuadrado(3);  // → 18
const b = 9 + 9;                       // → 18 — equivalente
```

## Contraejemplos — no son transparentes

```typescript
Date.now()    // ← distinto valor cada vez que se llama
Math.random() // ← distinto valor cada vez
console.log() // ← efecto colateral (I/O)
```

## ¿Por qué importa?

- Permite **memoización automática** (el compilador puede cachear resultados)
- Permite **evaluación lazy** (no calcular hasta que se necesite)
- Permite **razonar localmente**: para entender una expresión, no hay que conocer el estado global

---

## BLOQUE C — TypeScript en modo funcional

---

### [F-19] Las reglas del modo funcional en TypeScript

@tipo: concepto-abstracto
@imagen: none

# Modo funcional en TypeScript: las reglas

## Las restricciones (y por qué existen)

| Restricción | Por qué |
|---|---|
| Sin `let` ni `var` | Una variable reasignable rompe la trazabilidad del dato |
| Sin `for` / `while` | El loop mezcla *cómo iterar* con *qué hacer* |
| Sin `push`, `splice`, mutación de arrays | Un array que cambia puede afectar código que no lo esperaba |
| Sin `class` con estado mutable | El estado encapsulado en un objeto es estado oculto |
| Solo `const` + arrow functions | Las funciones son valores, no procedimientos |

## Importante

TypeScript **no obliga** a estas restricciones — las imponemos nosotros para aprender el paradigma.
Luego Clojure nos muestra qué pasa cuando el **lenguaje** sí las impone.

> La disciplina autoimpuesta enseña más que la disciplina del compilador, porque obliga a entender el **porqué**.

---

### [F-20] `map` — el problema (código imperativo)

@tipo: codigo
@imagen: none

# `map` — ¿qué tiene de problemático el estilo imperativo?

## ❌ Estilo imperativo: transformar cada elemento de una lista

```typescript
const numeros = [1, 2, 3, 4, 5];
const dobles: number[] = [];          // ← acumulador mutable externo

for (const n of numeros) {            // ← loop: detalle de cómo iterar
  dobles.push(n * 2);                 // ← mutación del acumulador
}

// dobles = [2, 4, 6, 8, 10]
```

## Los tres problemas

1. **Acumulador mutable externo** (`dobles`): cualquier código entre el `[]` y el `for` podría modificarlo
2. **Mezcla iteración y lógica**: el `for` dice *cómo* recorrer; `n * 2` dice *qué* hacer — están entrelazados
3. **Lectura no declarativa**: hay que simular el loop mentalmente para saber qué produce

---

### [F-21] `map` — la solución funcional

@tipo: codigo
@imagen: none

# `map` — transformar sin mutar

## ✅ Estilo funcional

```typescript
const numeros = [1, 2, 3, 4, 5];

const dobles = numeros.map(n => n * 2);
// → [2, 4, 6, 8, 10]

// El array original no cambia:
console.log(numeros); // [1, 2, 3, 4, 5]  ← intacto
```

## Por qué `map` y no `for`

- `map` expresa el **QUÉ**: "transformar cada elemento aplicando esta función"
- La iteración es un **detalle de implementación** — `map` la abstrae
- La función que le paso (`n => n * 2`) es **pura**: solo depende de `n`
- `map` siempre devuelve un array nuevo del **mismo largo**

## `map` es una función de orden superior

Recibe una función como argumento → las funciones son valores de primera clase en el paradigma funcional

---

### [F-22] `filter` — seleccionar sin mutar

@tipo: codigo
@imagen: none

# `filter` — conservar solo los elementos que cumplen una condición

## ✅ Estilo funcional

```typescript
const numeros = [1, 2, 3, 4, 5, 6];

const pares = numeros.filter(n => n % 2 === 0);
// → [2, 4, 6]

// El array original no cambia:
console.log(numeros); // [1, 2, 3, 4, 5, 6]  ← intacto
```

## El predicado es una función pura

`n => n % 2 === 0` : dado un número, devuelve `true` o `false` — sin efectos

## Encadenamiento: filter + map

```typescript
const cuadradosDePares = [1, 2, 3, 4, 5, 6]
  .filter(n => n % 2 === 0)   // [2, 4, 6]
  .map(n => n * n);            // [4, 16, 36]

// Pipeline de transformaciones — sin variables intermedias mutables
```

---

### [F-23] `reduce` — el problema (código imperativo)

@tipo: codigo
@imagen: none

# `reduce` — ¿qué tiene de problemático el acumulador mutable?

## ❌ Estilo imperativo: sumar todos los elementos

```typescript
const numeros = [1, 2, 3, 4];
let suma = 0;                        // ← acumulador externo mutable

for (const n of numeros) {
  suma += n;                         // ← mutación en cada iteración
}

// suma = 10
```

## El problema: state leakage

- `suma` existe **antes y después** del loop — puede ser leída o modificada desde afuera
- Si el loop está en una función larga, `suma` "contamina" el scope local
- Para paralelizar este loop, necesitaría sincronización explícita (mutex/lock) para proteger `suma`

---

### [F-24] `reduce` — la solución funcional

@tipo: codigo
@imagen: none

# `reduce` — el acumulador viaja adentro

## ✅ Estilo funcional

```typescript
const numeros = [1, 2, 3, 4];

const suma = numeros.reduce(
  (acc, n) => acc + n,  // función: acumulador actual + elemento → nuevo acumulador
  0                      // valor inicial del acumulador
);

// suma = 10
```

## Por qué `reduce` resuelve el problema

- El acumulador (`acc`) **solo existe dentro de `reduce`** — nadie puede tocarlo desde afuera
- En cada llamada, se pasa el acumulador como **argumento explícito** — el estado "viaja" visible
- Es paralizable: `reduce` (con variante `reduce` paralelo) puede dividir el array sin coordinación

## `reduce` es el más general

`map` y `filter` pueden implementarse con `reduce` — es la operación de plegado fundamental
(también llamado `fold` en Haskell, ML, Clojure)

---

### [F-25] Composición de funciones — `pipe`

@tipo: codigo
@imagen: none

# Composición: construir pipelines desde funciones puras

## Encadenamiento directo (para arrays)

```typescript
const resultado = [1, -2, 3, -4, 5]
  .filter(n => n > 0)         // [1, 3, 5]
  .map(n => n * 2);            // [2, 6, 10]
```

## `pipe` — composición general de funciones

```typescript
// pipe aplica funciones en secuencia: pipe(f, g, h)(x) = h(g(f(x)))
const pipe = <T>(...fns: Array<(x: T) => T>) =>
  (valor: T): T =>
    fns.reduce((v, fn) => fn(v), valor);
    // ← pipe usa reduce internamente: los pilares se componen entre sí

// Crear un pipeline reutilizable
const procesarPositivos = pipe(
  (nums: number[]) => nums.filter(n => n > 0),
  (nums: number[]) => nums.map(n => n * 2),
  (nums: number[]) => nums.filter(n => n < 8),
);

procesarPositivos([1, -2, 3, -4, 5]);  // → [2, 6]
procesarPositivos([-1, 4, 2, -3]);     // → [8 filtrado] → [4] reutilizable
```

## Por qué `pipe` importa

- Construir transformaciones complejas desde **piezas simples y puras**
- Cada pieza es testeable por separado
- El pipeline es una **función** — es un valor, puede pasarse como argumento

---

### [F-26] Resumen: las restricciones y sus raíces en los pilares

@tipo: tabla-comparativa
@imagen: none

# Por qué las restricciones funcionales existen

## La conexión entre pilar y restricción

| Restricción | Pilar que protege | Sin esta restricción… |
|---|---|---|
| Sin `let` / `var` | Inmutabilidad | Las variables reasignables crean estado mutable oculto |
| Sin `for` / `while` | Funciones puras + abstracción | El loop mezcla iteración con lógica; dificulta reutilización |
| Sin `push` / mutación | Inmutabilidad | Los efectos en colecciones se propagan de forma impredecible |
| Sin `class` con estado | Funciones puras | El estado encapsulado rompe la transparencia referencial |
| Solo `const` | Transparencia referencial | Si un nombre puede cambiar de valor, no es transparente |

## En TypeScript: disciplina elegida

Estas restricciones las imponemos **nosotros** — `tslint`/`eslint` puede ayudar a verificarlas

## En Clojure: garantizadas por el lenguaje

El compilador/runtime de Clojure hace que las tres primeras sean **imposibles de violar**

---

## BLOQUE D — Clojure: el funcional puro

---

### [F-27] Contexto de Clojure

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: logo de Clojure (símbolo λ estilizado en verde) sobre fondo oscuro con código Lisp flotando en tipografía monoespaciada, estilo ilustración tech minimal

# Clojure: el funcional hecho lenguaje

## Quién y cuándo

- Rich Hickey, 2007 — diseñado para resolver la concurrencia en sistemas reales
- Dialecto de Lisp que corre en la JVM (puede usar cualquier librería Java)
- En producción: **Nubank** (banco digital más grande de Latinoamérica), Datomic, sistemas financieros

## Propiedades de diseño

| Propiedad | Descripción |
|---|---|
| Inmutabilidad estructural | Todas las estructuras son persistentes e inmutables **por defecto** |
| Todo es expresión | No hay sentencias, no hay `return` implícito diferente del body |
| Funciones como valores | No hay diferencia entre función y dato |
| Sintaxis Lisp | `(función arg1 arg2)` — directamente el λ-cálculo |
| Concurrencia segura | Las referencias mutables son explícitas y coordinadas (STM, atoms) |

---

### [F-28] Sintaxis básica de Clojure

@tipo: codigo
@imagen: none

# Clojure: sintaxis — la notación prefija del λ-cálculo

## Aritmética y definición

```clojure
(+ 1 2)          ; → 3      (operador primero, siempre)
(* 3 4)          ; → 12
(- 10 3)         ; → 7

(def x 5)        ; define una constante — no se puede reasignar
(def pi 3.14159)
```

## Listas de datos

```clojure
'(1 2 3 4 5)     ; lista de datos (el apóstrofe evita la evaluación)

(first '(1 2 3)) ; → 1
(rest  '(1 2 3)) ; → (2 3)
(count '(1 2 3)) ; → 3
```

## Definición de funciones

```clojure
(defn cuadrado [x]   ; defn: nombre + vector de parámetros + cuerpo
  (* x x))

(cuadrado 5)  ; → 25
```

## Una sola forma sintáctica para todo

En TS hay muchas formas de definir funciones, iterar, condicionar — en Clojure hay **una**: `(f a b)`

---

### [F-29] `map`, `filter`, `reduce` en Clojure

@tipo: codigo
@imagen: none

# `map`, `filter`, `reduce` en Clojure

## `map` — transformar cada elemento

```clojure
(map #(* % 2) '(1 2 3 4 5))
;; → (2 4 6 8 10)
;;   #(* % 2) es la función anónima: % es el argumento
;;   El original '(1 2 3 4 5) no cambia — nunca puede cambiar
```

## `filter` — conservar los que cumplen la condición

```clojure
(filter even? '(1 2 3 4 5 6))
;; → (2 4 6)
;;   even? es una función pura predefinida: (even? 4) → true
```

## `reduce` — acumular

```clojure
(reduce + 0 '(1 2 3 4))
;; → 10
;;   + es una función normal que se pasa como argumento
;;   0 es el valor inicial del acumulador
```

## Pipeline con `->>` (thread-last macro)

```clojure
(->> '(1 2 3 4 5 6)
     (filter even?)          ; → (2 4 6)
     (map #(* % %))          ; → (4 16 36)
     (reduce + 0))            ; → 56

;; Lee de arriba a abajo: igual que el encadenamiento en TS
```

---

### [F-30] Funciones anónimas en Clojure — `fn`

@tipo: codigo
@imagen: none

# Funciones anónimas en Clojure: `fn` y la notación `#()`

## Forma completa con `fn`

```clojure
;; (fn [parámetros] cuerpo) — directamente el λ-cálculo
(fn [x] (* x x))          ; función anónima: eleva al cuadrado

;; Aplicación inmediata: define y aplica en el mismo lugar
((fn [x y] (+ x y)) 3 4)  ; → 7
;; equivale a: (λx.λy. x+y) 3 4 → 7

;; Guardar en un nombre
(def doble (fn [x] (* x 2)))
(doble 5)  ; → 10
```

## Forma abreviada `#()`

```clojure
#(* % 2)           ; equivale a (fn [x] (* x 2))   — % es el único argumento
#(+ %1 %2)         ; dos argumentos: %1 y %2
#(* % %)           ; cuadrado
```

## Funciones como valores de primera clase

```clojure
;; Una función puede ser argumento de otra función
(map (fn [x] (* x x)) '(1 2 3 4))  ; → (1 4 9 16)

;; Una función puede retornar una función (currying manual)
(defn multiplicador [factor]
  (fn [x] (* x factor)))    ; devuelve una función

((multiplicador 3) 7)  ; → 21
```

---

### [F-31] Comparativa completa TypeScript ↔ Clojure

@tipo: tabla-comparativa
@imagen: none

# TypeScript (funcional) vs Clojure (puro) — comparativa

| Concepto | TypeScript (funcional) | Clojure (puro) |
|---|---|---|
| Valor inmutable | `const x = 5` | `(def x 5)` |
| Función pura con nombre | `const f = (x: number) => x * 2` | `(defn f [x] (* x 2))` |
| Función anónima | `(x) => x * 2` | `(fn [x] (* x 2))` o `#(* % 2)` |
| Aplicación inmediata | `((x) => x * 2)(5)` | `((fn [x] (* x 2)) 5)` |
| Map | `arr.map(fn)` | `(map fn coll)` |
| Filter | `arr.filter(pred)` | `(filter pred coll)` |
| Reduce | `arr.reduce(fn, init)` | `(reduce fn init coll)` |
| Pipeline | `.filter().map().reduce()` o `pipe()` | `(->> coll (filter) (map) (reduce))` |
| Inmutabilidad de colecciones | **Opt-in** (`as const`, `readonly`) | **Nativa — siempre** |
| Garantía de pureza | Disciplina del programador | Diseño del lenguaje |
| Sintaxis | Múltiples formas (arrow, function, method) | Una sola forma: `(f a b)` |

---

### [F-32] Por qué Clojure muestra el paradigma en su forma más pura

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: dos columnas visuales: izquierda "TypeScript" con un candado abierto (opt-in), derecha "Clojure" con un candado cerrado (garantizado), fondo blanco colores azul y verde

# La diferencia que importa: disciplina vs garantía

## En TypeScript

```typescript
const numeros = [1, 2, 3];
numeros.push(4);  // ← el compilador lo permite aunque lo hayamos "prohibido"
                   // la inmutabilidad es una convención del equipo, no del lenguaje
```
 
## En Clojure

```clojure
(def numeros '(1 2 3))
;; No existe ninguna operación para mutar 'numeros en su lugar
;; Todas las operaciones devuelven nuevas colecciones
;; Es imposible violar la inmutabilidad — el runtime lo garantiza
```

## La consecuencia

En Clojure, cuando el código compila y corre:
- **Ninguna función modificó una estructura compartida** — es una garantía del sistema de tipos y el runtime
- En concurrencia: múltiples threads pueden leer la misma estructura sin locks → correctitud por diseño

> En TS, confías en la disciplina del equipo.
> En Clojure, confías en el diseño del lenguaje.

---

## BLOQUE E — Integración y cierre

---

### [F-33] Línea de tiempo — síntesis visual

@tipo: timeline
@imagen: none

# Del λ-cálculo al TypeScript funcional: 90 años de paradigma

| Año | Hito |
|---|---|
| **1936** | Church: λ-cálculo / Turing: Máquina de Turing — dos modelos de computación |
| **1958** | Lisp — primer lenguaje funcional (McCarthy, MIT) |
| **1973–75** | ML y Scheme — inferencia de tipos y minimalismo |
| **1985–86** | Miranda y Erlang — lazy evaluation y concurrencia por actores |
| **1990** | Haskell — primer lenguaje puramente funcional de uso académico amplio |
| **2003–05** | Scala, F# — funcional en plataformas .NET y JVM, Big Data |
| **2007** | Clojure — funcional puro moderno, blockchain, concurrencia |
| **2011–15** | Kotlin, Rust, JS ES6, Java 8 — funcional entra en todos los multiparadigma |
| **2015+** | TypeScript funcional — el paradigma disponible en el lenguaje del ecosistema web |

> Cada lenguaje nació para resolver el problema concreto de su época

---

### [F-34] Pregunta de debate

@tipo: socratica
@imagen: background
@prompt-imagen: sala de debate con siluetas de personas alrededor de una mesa, pizarrón al fondo con λ y el símbolo de TypeScript, tonos azul y naranja cálido

# Pregunta de debate

> *"Si TypeScript permite el estilo funcional pero no lo obliga, ¿tiene sentido aprender Clojure o Haskell?*
> *¿O alcanza con disciplina y convenciones en TypeScript?"*

## Ejes para el debate

- **Escala del equipo**: la disciplina individual no escala con 50 desarrolladores
- **Dominio de aplicación**: sistemas financieros de alta criticidad vs aplicaciones web
- **Profundidad de comprensión**: un lenguaje puro fuerza a entender el paradigma a fondo
- **Interoperabilidad**: TypeScript accede al ecosistema npm; Clojure a la JVM

## No hay respuesta única — depende del contexto

---

### [F-35] Cierre — síntesis y próximas clases

@tipo: cierre
@imagen: background
@prompt-imagen: fondo oscuro con símbolo lambda λ grande en azul luminoso, línea de tiempo abajo con puntos brillantes, estilo ilustración académica de cierre de clase

# Síntesis de la clase

## Los tres hilos que conectan toda la clase

1. **El origen** — Church (1936) y Turing (1936): dos modelos equivalentes, dos filosofías opuestas → funcional e imperativo
2. **Los tres pilares** — funciones puras + inmutabilidad + transparencia referencial → código predecible, testeable y paralelizable
3. **De la teoría al código** — TypeScript nos deja elegir ser funcionales; Clojure nos obliga

## Próximas clases

| Tema | Contenido |
|---|---|
| **Tema 04** | Aspectos avanzados: currying, aplicación parcial, tipos algebraicos, pattern matching |
| **Tema 05** | Mónadas en TypeScript — cómo manejar `null`, errores e I/O sin romper los pilares |

## TP

→ Ver próxima clase para tipo y fecha de entrega
  