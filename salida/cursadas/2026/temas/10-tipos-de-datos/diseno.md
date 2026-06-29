# Diseño de Clase — Tema 10
## Tipos de Datos y Sistemas de Tipos

> **Estado:** 🟡 EN PRODUCCION — filminas.md y minuta.md corregidos contra `clase_dada.txt` (1122 líneas) + ChromaDB el 2026-06-28 (360 min, 54 filminas F-00 a F-53)
> **Revisión previa:** 2026-05-26 — Ajuste de autocontenido post-publicación (ver sección al final)
> **Creado:** 2026-05-25
> **Agente:** Lic. Marcos 🗂️ (Topic Designer)
> **Fuente principal:** Sebesta, *Concepts of Programming Languages* 12ª ed., Cap. 6 "Data Types" (pp. 259–324)
> **Fuentes secundarias:** Louden Cap. 8, Gabbrielli & Martini Cap. 8

---

## Metadata del Tema

| Campo | Valor |
|-------|-------|
| Número de tema | 10 |
| Nombre | Tipos de Datos y Sistemas de Tipos |
| Módulo Plan Mínimo | VII — Tipos de Datos |
| Semana | 11 |
| Clase | 1 (extendida) |
| **Duración (constraint operativo)** | **360 minutos** |
| Perfil docente | profesor-teorico |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | Kotlin, Haskell, C, Python |

---

## Contexto en el Plan

**Prerequisito inmediato:** T09.1 (binding de tipos, 5-tupla de variables) y T09.2 (scope, aliases, GC).  
**Lo que trae T09.x:** *Cómo se vincula* un tipo a una variable (binding time) y cómo el sistema verifica esa vinculación.  
**Lo que agrega T10:** *Qué son los tipos* como estructuras formales — sus taxonomías, implementaciones internas y el sistema que los conecta coherentemente.  
**Conexión con T14 (futuro):** T14 profundizará en inferencia de tipos (Hindley-Milner), sistema de tipos formales y polimorfismo paramétrico avanzado. T10 introduce los conceptos con orientación operacional y multilenguaje.

---

## Objetivos de Aprendizaje

Al finalizar el tema, el alumno podrá:

| # | Objetivo | Nivel Bloom | Fuente |
|---|----------|-------------|--------|
| OA1 | **Definir** tipo de dato como conjunto de valores + conjunto de operaciones admisibles, y explicar por qué los lenguajes los usan (legibilidad, confiabilidad, seguridad) | Recordar/Comprender | Sebesta §6.1 |
| OA2 | **Clasificar** los tipos primitivos (numérico-entero, floating, boolean, char, decimal) y relacionar su representación interna con sus rangos y precisión | Comprender | Sebesta §6.2 |
| OA3 | **Definir** tipos ordinales por el usuario (enumeraciones, subrangos) y analizar cómo TypeScript, Kotlin y C los implementan con distintos niveles de seguridad | Analizar | Sebesta §6.4, Louden §8.2 |
| OA4 | **Comparar** arrays estáticos, semi-dinámicos y dinámicos según su binding time de forma y rango; calcular la función de acceso para arrays multidimensionales | Analizar | Sebesta §6.5, Gabbrielli §8.4 |
| OA5 | **Explicar** tipos secuencia (strings), su semántica de valor vs. referencia y las operaciones más comunes entre lenguajes | Comprender | Sebesta §6.3 |
| OA6 | **Distinguir** registros (structs) y tuplas de arrays; analizar implementación en memoria y casos de uso en TypeScript `interface`/`type` y (contraste) Kotlin `data class` | Aplicar | Sebesta §6.6 |
| OA7 | **Analizar** uniones libres (C `union`) vs. uniones discriminadas (TypeScript discriminated unions, Haskell ADT) y razonar sobre seguridad de tipos; contrastar con Kotlin `sealed class` | Analizar | Sebesta §6.10, Gabbrielli §8.7 |
| OA8 | **Explicar** el tipo puntero: semántica, aritmética de punteros, punteros colgantes (*dangling*), memory leaks y mecanismos de garbage collection | Analizar | Sebesta §6.11 |
| OA9 | **Aplicar** tipos opcionales en TypeScript (`T | null`, `?.`, `??`, `!`) con `strictNullChecks`; comparar con Kotlin `T?` y Haskell `Maybe a` | Aplicar | Sebesta §6.12 |
| OA10 | **Diferenciar** equivalencia nominal vs. estructural de tipos y razonar sobre compatibilidad e incompatibilidad en sistemas tipados | Analizar | Sebesta §6.15, Louden §8.5 |
| OA11 | **Comparar** sistemas monomórficos vs. polimórficos; clasificar polimorfismo paramétrico (generics), ad-hoc (overloading) y por subtipo | Analizar | Sebesta §6.13, Louden §8.8-8.9 |
| OA12 | **Evaluar** el grado de fuertemente tipado (*strong typing*) en distintos lenguajes y relacionarlo con confiabilidad del software | Evaluar | Sebesta §6.14, Gabbrielli §8.2 |
| OA13 | **Aplicar** el chequeo de tipos (estático vs. dinámico) y explicar el concepto de coerción implícita vs. conversión explícita | Aplicar | Sebesta §6.13 |
| OA14 | **Distinguir** tipos lista funcionales (Haskell, Python) de arrays y analizar sus operaciones head/tail/cons | Comprender | Sebesta §6.9 |

---

## Cobertura del Plan Mínimo — MÓDULO VII

| Tópico plan mínimo | Cobertura en T10 | Sección |
|--------------------|-----------------|---------|
| Tipos built-in y primitivos | ✅ Completa | Bloque 1 |
| Tipos ordinales definidos por el usuario | ✅ Completa | Bloque 1 |
| Tipos de agregación: producto cartesiano, uniones, uniones discriminadas, mapeos finitos | ✅ Completa | Bloques 2–3 |
| Arrays: estáticos, de pila dinámica, dinámicos de heap | ✅ Completa | Bloque 2 |
| Tipos secuencia, strings, conjunto potencia, tipos recursivos | ✅ Completa | Bloque 2 |
| Tipo puntero: inseguridad, punteros colgantes, recolección de basura | ✅ Completa | Bloque 3 |
| Sistemas de tipos: monomórficos vs. polimórficos | ✅ Completa | Bloque 4 |
| Tipos que aceptan null y sus operadores | ✅ Completa | Bloque 3 |
| Lenguajes fuertemente tipados; clases | ✅ Completa | Bloque 4 |
| Ejemplos en TypeScript y otros lenguajes | ✅ Transversal | Todos |

---

## Estructura de la Clase (360 min)

### Bloque 0 — Apertura y Conexión (15 min)

**Pregunta disparadora:** *"¿Qué diferencia hay entre el número `1` en C, en Python y en Haskell?"*  
- Recapitulación rápida T09: binding de tipos ya visto (estático/dinámico)  
- Mapeo visual: "Hoy vemos QUÉ son los tipos; antes vimos CUÁNDO se les asignan"  
- Presentación del roadmap de la clase con mapa conceptual

---

### Bloque 1 — Tipos Primitivos y Ordinales (70 min)

**Referencia principal:** Sebesta §6.1–§6.2, §6.4 (enumeraciones) y §6.15 (equivalencia)

#### 1.1 ¿Qué es un tipo de dato? (15 min)
- Definición formal: tipo = {conjunto de valores} + {operaciones admisibles}  
  - *Sebesta §6.1:* "A data type defines a collection of data values and a set of predefined operations on those values"
- Razones para incluir tipos en lenguajes: legibilidad, detectabilidad de errores, reusabilidad
- Clasificación de tipos: primitivos / compuestos / definidos por el usuario

#### 1.2 Tipos numéricos (15 min)
- **Enteros:** representación binaria en complemento a 2; rangos según tamaño (8/16/32/64 bits)
  - TypeScript: tipo `number` unificado (IEEE 754 64-bit) — no distingue entero/float
  - `bigint` en TypeScript: enteros de precisión arbitraria (`9007199254740991n`)
  - Comparación: `number` (TypeScript/JS), `int`/`long` (C/Java), `Int` (Kotlin — JVM), `int` (Python — ilimitado)
- **Floating point:** estándar IEEE 754; TypeScript `number` es siempre double (64-bit)
  - `Float` vs `Double` en Kotlin — contraste: TypeScript no distingue, todo es 64-bit
  - Consecuencia: `0.1 + 0.2 !== 0.3` en TypeScript — demostrar en clase
- **Decimal:** TypeScript no tiene tipo decimal nativo — requiere librerías (`decimal.js`); contraste con `BigDecimal` en Java/Kotlin
- **Complejo (§6.2.1.3):** Python tiene tipo `complex` nativo (`3+4j`); Fortran también. La mayoría de lenguajes OO los implementan como clase. Discusión: ¿es mejor tipo nativo o librería?
- **Boolean:** TypeScript `boolean` (tipo real); contraste con C `0`/no-cero
- **Char:** TypeScript **no tiene** tipo `char` — solo `string`; contraste con `Char` en Kotlin (UTF-16) y `char` en C (byte). Ejemplo de decisión de diseño de lenguaje.

#### 1.3 Tipos ordinales definidos por el usuario (20 min)
- **Enumeraciones:**
  - TypeScript: `enum Direction { Up, Down, Left, Right }` — tipo de primera clase; `const enum` para inlining en compilación
  - TypeScript string enum: `enum Status { Active = 'active', Inactive = 'inactive' }` — útil para interoperabilidad con APIs
  - Contraste con C: `enum` débil (valor numérico filtrable con `int`, inseguro)
  - Contraste con Kotlin: `enum class` — más rico (propiedades, métodos, exhaustividad en `when`)
  - Haskell: tipo algebraico simple — `data Color = Red | Green | Blue`
  - *Sebesta §6.4.1:* Problema con enums en C — no son type-safe
- **Subrangos (subrange types):**
  - Pascal: `type DiasLaborables = 1..5` — chequeo estático de rango
  - TypeScript: no tiene subrangos nativos; se simula con `type Day = 1|2|3|4|5` (literal union)
  - Kotlin: `IntRange` permite expresarlo; tampoco es subtype nativo
  - Utilidad: verificación en tiempo de compilación vs. en tiempo de ejecución
  - *Tradeoff:* seguridad vs. expresividad vs. rendimiento

#### 1.4 Equivalencia de tipos (20 min)
- **Equivalencia nominal:** dos tipos son iguales si tienen el *mismo nombre*
  - Kotlin, Java, C (con `typedef struct`) — sistema por defecto
- **Equivalencia estructural:** dos tipos son iguales si tienen la *misma estructura*
  - TypeScript, Go, Haskell
  - Ejemplo: `type Punto = {x: number, y: number}` — ¿es compatible con otro objeto `{x:2, y:3}`?
- **Tabla comparativa:** C, Pascal, Java, Kotlin, TypeScript, Haskell
- *Louden §8.5:* Implicaciones en diseño de compiladores

**→ Actividad rápida (10 min):** Los alumnos reciben 4 declaraciones de tipo en TypeScript y Kotlin — identifican qué sistema aplica cada lenguaje y predicen la compatibilidad.

---

### Bloque 2 — Tipos de Agregación y Colecciones (90 min)

**Referencia principal:** Sebesta §6.3 (strings), §6.5–§6.10, Gabbrielli §8.4–§8.7

#### 2.1 Strings y secuencias (15 min)
- **Semántica de cadenas:** tipo primitivo vs. objeto
  - TypeScript: `string` es primitivo (como `number`) — no es un objeto, pero tiene métodos via autoboxing del motor JS
  - Contraste: C: puntero a char terminado en `\0`; Kotlin/Python: objeto
- Operaciones: concatenación, comparación, `substring`/`slice`, `length`
- **Mutabilidad:** TypeScript `string` es inmutable — las operaciones devuelven nuevas strings
  - Contraste con Kotlin `StringBuilder`; Python `str` inmutable vs. `bytearray`
- Comparación: en TypeScript `===` compara por valor (no referencia) — correcto por defecto
  - Error clásico en Java: `==` compara referencias; hay que usar `.equals()`
- *Sebesta §6.4:* "The most common string operations are: assignment, concatenation, substring reference, comparison, and pattern matching"

#### 2.2 Arrays (35 min)
- **Taxonomía por binding time de forma:** *(Sebesta §6.5, Figura 6.2)*
  | Categoría | Forma | Binding de rango | Almacenamiento | Ejemplo |
  |-----------|-------|-----------------|---------------|---------|
  | Estático | Estática | Estático (compila) | Estático | C array global |
  | Semi-dinámico (stack) | Estática (runtime) | Después de elab. | Stack (liberado al salir) | C local `int a[n]` (C99) |
  | Dinámico de heap (fijo) | Dinámica (heap) | Runtime, luego fijo | Heap (manual) | `new Array<number>(n)` en TS / `IntArray(n)` en Kotlin |
  | Dinámico de heap (flexible) | Completamente dinámica | Cambia en runtime | Heap (GC) | TypeScript `number[]` / Python `list` |

- **Función de acceso para arrays multidimensionales:**
  - *Row-major* (C, Kotlin, Java): `a[i][j]` → `base + (i * cols + j) * size`
  - *Column-major* (Fortran, MATLAB): `a[i][j]` → `base + (i + j * rows) * size`
  - Implicancias de rendimiento: cache locality
- **Arrays rectangulares vs. escalonados (§6.5.6):**
  - *Rectangular* (C#, Fortran): todos los sub-arrays tienen la misma longitud — `int[,]` en C#
  - *Jagged* (Java, C, Kotlin): array de punteros a arrays — cada fila puede tener distinto tamaño
  - Ventajas/desventajas: acceso más rápido en rectangular; flexibilidad en jagged
  - En Java todos los arrays multidimensionales son jagged por diseño
- **Slices (§6.5.7):**
  - Una *slice* es una referencia a una subsecuencia de un array (sin copiar los datos)
  - Python: `lista[1:4]` — muy utilizado, produce nueva lista (copia)
  - Kotlin: `lista.subList(1, 4)` — vista viva sobre la lista original
  - Go: slices son ciudadanos de primera clase con length/capacity separados
  - Ada: `A(2..4)` — slice de array nativo
- **Arrays asociativos / mapeos finitos:**
  - TypeScript `Map<K, V>` — operaciones básicas: `.set(k, v)`, `.get(k)`, `.has(k)`, `.delete(k)`
  - TypeScript `Record<string, number>` — objeto como mapa con clave string
  - Contraste con Kotlin `Map<K,V>` (hashCode y equals), Python `dict`
  - *Sebesta §6.8:* "An associative array is an unordered collection of data elements that are indexed by an equal number of values called keys"
- **Ejemplo en código (TypeScript):**
  ```typescript
  // Array de tamaño conocido (heap dinámico tipado)
  const fijo: number[] = new Array(5).fill(0).map((_, i) => i * 2)
  // Array dinámico
  const lista: number[] = [1, 2, 3]
  lista.push(4)

  // Typed Array para rendimiento (sin overhead de boxing)
  const binario: Int32Array = new Int32Array([10, 20, 30])

  // Array asociativo (Map)
  const scores = new Map<string, number>([["Ana", 9], ["Luis", 7]])
  scores.set("Marta", 8)
  console.log(scores.get("Ana"))  // 9

  // Record como mapa
  const config: Record<string, boolean> = { dark: true, sound: false }
  ```
  > **Contraste (Kotlin):** `val fijo = IntArray(5) { it * 2 }` / `mutableMapOf("x" to 1)`

#### 2.3 Registros, structs y tuplas (20 min)
- **Registro / struct:**
  - C `struct`: campos heterogéneos, acceso por nombre, padding en memoria
  - TypeScript `interface` / `type`: forma preferida de definir registros — tipado estructural
    ```typescript
    interface Usuario { nombre: string; email: string; edad: number }
    type Punto = { x: number; y: number }       // equivalente funcional
    // Inmutabilidad: readonly
    type PuntoFijo = { readonly x: number; readonly y: number }
    ```
  - Contraste con Kotlin `data class`: genera `equals`, `hashCode`, `copy()` automáticos — TypeScript no tiene equivalente nativo
  - *Sebesta §6.6:* "A record is a collection of data fields, in which the individual elements are identified by name"
- **Tuplas:**
  - TypeScript tiene tipos tupla nativos: `[string, number]`, `[string, number, boolean]`
    ```typescript
    const par: [string, number] = ["hola", 42]
    const [nombre, edad] = par    // desestructuración
    type RGB = [number, number, number]     // tipo nombrado
    ```
  - Contraste con Kotlin `Pair<A,B>` / `Triple<A,B,C>` — TypeScript las hace con tuples literales
  - Python: `(1, "hola", True)` — inmutables por defecto
- **Producto cartesiano formal:** tipo `A × B` = todos los pares `(a, b)` con `a:A`, `b:B`

#### 2.4 List Types — Listas funcionales (§6.9) (15 min)

**Referencia:** Sebesta §6.9

- **Definición:** tipo secuencia donde el orden importa y el tamaño puede ser dinámico; originados en LISP (1958)
- **Propiedades fundamentales:**
  - Acceso por posición (head / tail)
  - Construcción con `cons` — añade elemento al frente
  - Recursividad inherente: lista = cabeza + lista
- **En TypeScript:** `T[]` / `Array<T>` — array dinámico que actúa como lista; métodos: `push`, `pop`, `shift`, `unshift`, `map`, `filter`, `reduce`
  - `ReadonlyArray<T>` para listas inmutables
- **En Python:** `list` es en realidad un array dinámico (no lista enlazada), pero semánticamente funciona como lista
- **En Kotlin:** `List<T>` (inmutable) / `MutableList<T>` (dinámica) — implementadas sobre ArrayList (contraste: más rico en API que TypeScript)
- **En Haskell:** listas homogéneas `[a]` — `head`, `tail`, `(:)`, pattern matching
- **Diferencia clave con arrays:** acceso O(1) en array vs. O(n) en lista enlazada; inserción O(1) al frente en lista vs. O(n) en array
- *Sebesta §6.9:* "Lists are collections of data that can have varying numbers of elements and to which elements can be easily added or removed from either end"

#### 2.5 Uniones (20 min)

- **Uniones libres (unsafe) — C `union`:**
  - Comparten espacio de memoria — el programador sabe qué campo es válido
  - *Sebesta §6.10:* "The fundamental problem with unions in Pascal and C is that they are unsafe—there is no way to ensure that a union is accessed in the correct way"
  - Ejemplo: `union Data { int i; float f; char c; }` — leer `f` después de escribir `i`
- **Uniones discriminadas (safe) — tagged unions:**
  - TypeScript Union Types con discriminante: `type Shape = Circle | Rect` — primer ciudadano del lenguaje
  - Haskell ADT: `data Shape = Circle Float | Rect Float Float`
  - Contraste con Kotlin `sealed class`: el compilador garantiza exhaustividad en `when`
  - **Diferencia clave:** la etiqueta discriminante forzada hace imposible el acceso incorrecto
- **Ejemplo en código (TypeScript) — primario:**
  ```typescript
  type Result<T> =
    | { kind: 'success'; value: T }
    | { kind: 'error';   message: string }

  function handle(r: Result<number>) {
    switch (r.kind) {
      case 'success': console.log(r.value);   break  // r es Success<number>
      case 'error':   console.log(r.message); break  // r es Error
    }
  }
  ```
- **Contraste con Kotlin `sealed class`:**
  ```kotlin
  sealed class Result<out T> {
      data class Success<T>(val value: T) : Result<T>()
      data class Error(val message: String) : Result<Nothing>()
  }
  fun handle(r: Result<Int>) = when (r) {    // exhaustividad garantizada por el compilador
      is Result.Success -> println(r.value)
      is Result.Error   -> println(r.message)
  }
  ```
  > Kotlin agrega exhaustividad garantizada por el compilador en `when`; en TypeScript el compilador también detecta casos no manejados con `--strictNullChecks` y `never`.

**→ Actividad: Diseño de ADT (5 min):** El alumno modela "Figura geométrica" usando un discriminated union en TypeScript y una unión en C. Discusión sobre qué errores puede cometer el compilador vs. el programador.

---

### Bloque 3 — Punteros, Null Safety y Tipos Recursivos (75 min)

**Referencia principal:** Sebesta §6.11–§6.12, Gabbrielli §8.4

#### 3.1 Tipo puntero (35 min)
- **Definición y semántica:**
  - Un puntero es un valor que denota una *dirección de memoria*
  - Operaciones básicas: asignación, derreferenciación (`*p`), aritmética
  - *Sebesta §6.11.1:* "A pointer type variable has a range of values that consists of memory addresses and a special value, nil"
- **Usos principales:**
  - Manejo indirecto de datos en heap
  - Paso de estructuras grandes por referencia (eficiencia)
  - Construcción de estructuras dinámicas (listas enlazadas, árboles)
- **Problemas clásicos:**
  | Problema | Descripción | Lenguaje afectado |
  |----------|-------------|------------------|
  | Puntero colgante (*dangling pointer*) | Puntero apunta a memoria ya liberada | C, C++ |
  | Memory leak | Memoria asignada sin referencia pero no liberada | C, C++ |
  | Double free | Liberar el mismo bloque dos veces → UB | C |
  | Null pointer dereference | Desreferenciar `null` → crash | Java, C, pre-Kotlin, pre-TS strict |
  | Buffer overflow | Aritmética de punteros fuera de rango | C |
  - *Sebesta §6.11.4:* "Tombstones" y "locks and keys" como soluciones históricas
- **Garbage Collection:**
  - Recolección por referencia (*reference counting*): Python, Swift
  - Recolección por alcance (*tracing GC*): Java/JVM, Kotlin, Python (ciclos)
  - Ventajas: elimina dangling pointers y memory leaks
  - Costo: pausas GC, overhead de memoria
- **Referencias en TypeScript/JS:** tampoco tienen punteros explícitos — todo es gestionado por el motor JS (V8, SpiderMonkey). Mismo concepto que Kotlin/JVM pero en un runtime diferente.
- **Reference Types vs. Pointer Types (§6.11.5):**
  - C++: referencias (`int& r = x`) — alias que no puede reasignarse, no admite aritmética, siempre válido
  - Java: todas las variables de objeto son referencias (no punteros) — no hay aritmética
  - TypeScript/JS: ídem Java, GC-managed, sin control manual
  - Kotlin: ídem Java — referencias implícitas, GC-managed
  - Diferencia clave con puntero: referencia = alias seguro; puntero = dirección aritmética peligrosa
  - *Sebesta §6.11.5:* "A reference variable is a constant pointer that is always implicitly dereferenced"

#### 3.2 Tipos recursivos (10 min)
- **Definición:** un tipo que se define en términos de sí mismo
- **Lista enlazada en C:**
  ```c
  struct Node {
      int value;
      struct Node* next;   // referencia recursiva — posible por puntero
  };
  ```
- **Lista en Haskell:**
  ```haskell
  data List a = Nil | Cons a (List a)
  -- isomorfo a [a] built-in
  ```
- **Árbol binario en TypeScript (tipo recursivo):**
  ```typescript
  type BinaryTree<T> =
    | { kind: 'leaf' }
    | { kind: 'node'; value: T; left: BinaryTree<T>; right: BinaryTree<T> }

  // Función recursiva que explota el tipo recursivo
  function depth<T>(t: BinaryTree<T>): number {
    if (t.kind === 'leaf') return 0
    return 1 + Math.max(depth(t.left), depth(t.right))
  }
  ```
- **Contraste Kotlin `sealed class` (Tree):**
  ```kotlin
  sealed class Tree<T> {
      object Empty : Tree<Nothing>()
      data class Node<T>(val value: T, val left: Tree<T>, val right: Tree<T>) : Tree<T>()
  }
  ```
- Relación con tipos algebraicos — recursividad + sealed = estructuras de datos inductivas

#### 3.3 Null Safety y tipos opcionales (30 min)
- **El problema del null:**
  - Tony Hoare (inventor del null): *"My billion-dollar mistake"* (QCon 2009)
  - `null` en Java: cualquier referencia puede ser null → NPE en runtime
  - *Sebesta §6.12:* "An optional type allows an entity to take a special value (often None or null) in addition to its normal values"
- **TypeScript Null Safety (primario):**
  - Con `"strictNullChecks": true` en `tsconfig.json` — null y undefined son tipos separados
  - Tipos not-null: `string` — nunca puede ser null/undefined (garantizado por el compilador)
  - Tipos nulos: `string | null` / `string | undefined` / `string | null | undefined`
  - Parámetros opcionales: `function f(x?: string)` → `x` es `string | undefined`
  - **Operadores:**
    | Operador | Nombre | Comportamiento |
    |----------|--------|---------------|
    | `?.` | Optional chaining | Evalúa solo si no-null/undefined, si no retorna `undefined` |
    | `??` | Nullish coalescing | Si la expresión es null/undefined, usa el valor de la derecha |
    | `!` | Non-null assertion | Fuerza acceso; puede fallar en runtime si null (usar con precaución) |
    | `if (x !== null)` | Type narrowing | El compilador infiere el tipo más estrecho en el bloque |
  - Ejemplo completo:
    ```typescript
    interface User { name: string; email: string | null }

    function sendEmail(user: User) {
      const dest = user.email ?? 'sin email'   // nullish coalescing (~ Elvis ?: en Kotlin)
      const upper = user.email?.toUpperCase()  // optional chaining (~ ?. en Kotlin)
      const forced = user.email!               // non-null assertion (~ !! en Kotlin)

      if (user.email !== null) {
        // Aquí TypeScript sabe que email es string (type narrowing)
        console.log(`Enviando a ${user.email}`)
      }
    }
    ```
- **Contraste con Kotlin null safety:**
  - Kotlin `T?` vs. TypeScript `T | null` — semántica similar, sináxis distinta
  - Kotlin: null safety a nivel del sistema de tipos (JVM), sin flag de configuración
  - TypeScript: requiere `strictNullChecks: true` para activarse — es opt-in
  - Kotlin `?:` (Elvis) = TypeScript `??` (Nullish coalescing)
  - Kotlin `!!` = TypeScript `!` (non-null assertion)
  - Kotlin `?.let { }` = TypeScript `if (x !== null) { ... }` o `x?.someMethod()`
- **Comparación multilenguaje:**
  | Lenguaje | Mecanismo | Safety level |
  |---------|-----------|-------------|
  | C/Java | `null` sin restricción | ❌ Peligroso |
  | Python | `None` sin restricción | ❌ Peligroso |
  | TypeScript | `T \| null` con `strictNullChecks` | ✅ (config-dependiente) |
  | Kotlin | `T` vs `T?` + operadores | ✅ Type-safe |
  | Haskell | `Maybe a = Nothing \| Just a` | ✅ Type-safe (monádico) |
  | Rust | `Option<T> = None \| Some(T)` | ✅ Type-safe |
- *Conexión con T02 (mónadas):* `Maybe`/`Option` es la mónada de null safety — `flatMap` = `?.` encadenado

**→ Actividad: Null Safety Refactor (10 min):** Se da código JavaScript (sin `strictNullChecks`) con posibles NPEs — los alumnos lo reescriben en TypeScript con `strictNullChecks`, `| null`, `?.` y `??`. Discusión: ¿por qué TypeScript lo hace opt-in y Kotlin no?

---

### Bloque 4 — Sistemas de Tipos: Monomórficos, Polimórficos y Strong Typing (80 min)

**Referencia principal:** Louden §8.8–§8.9, Sebesta §6.13–§6.15, Gabbrielli §8.2

#### 4.1 Type Checking — Chequeo de tipos (§6.13) (20 min)

**Referencia:** Sebesta §6.13

- **Definición:** actividad de asegurar que los operandos de un operador son de tipos compatibles
- **Tipo compatible:** legal para el operador, o convertible implícitamente por el compilador
- **Coerción (coercion):** conversión implícita generada por el compilador
  - `int + float` → el `int` es *coercionado* a float antes de la operación
  - Distinción coerción implícita vs. conversión explícita (*casting*)
  - Widening vs. Narrowing: widening = sin pérdida de información; narrowing = puede perder datos
  ```
  int → long → float → double   (widening, seguro)
  double → float → int           (narrowing, pérdida posible)
  ```
- **Type error:** aplicación de un operador a un operando de tipo inapropiado
- **Estático vs. dinámico:**
  - Si todos los bindings son estáticos → chequeo estático (compile time) — más eficiente
  - Binding dinámico → chequeo dinámico (runtime) — más flexible pero más costoso
  - JavaScript/Python: solo dinámico por diseño
  - TypeScript: chequeo estático encima de JavaScript → el runtime sigue siendo JS
- **Complejidad con uniones:** lenguajes con `union` (C) o tipos discriminados (Haskell) requieren chequeo dinámico adicional incluso con tipos estáticos
- *Sebesta §6.13:* "If all bindings of variables to types are static in a language, then type checking can nearly always be done statically"


#### 4.2 Sistemas de tipos: visión general (10 min)
- **Definición (Louden §8.1):** Un sistema de tipos es el conjunto de reglas que define cómo los tipos son asignados, verificados y combinados en un lenguaje.
- **Dimensiones de clasificación:**
  - ¿Cuándo se verifica? → Estático (compilación) vs. dinámico (runtime) ← ya visto en T09
  - ¿Qué tan rígidamente? → Strong vs. Weak typing
  - ¿Cuántos tipos puede tener un valor? → Monomórfico vs. Polimórfico
- **Strong typing — §6.14:**
  - Definición: **todos** los errores de tipo son *siempre* detectados (en compilación o runtime)
  - Coerciones implícitas como zona gris:
    - `int + float` en C — conversión implícita = ¿weak typing?
    - *Sebesta §6.14:* "A programming language is strongly typed if type errors are always detected"
    - *Sebesta §6.14:* "Haskell and Ada are the most strongly typed languages"
    - C/C++: NO strongly typed (uniones sin discriminación, punteros void*)
    - Java: moderado (coerciones numéricas implícitas)
    - TypeScript (con `strict: true`): strongly typed dentro de la compilación; Kotlin/Haskell: strongly typed
    - TypeScript peculiaridad: el runtime es JS (sin tipos) — los tipos existen solo en compilación
  - Tabla: C (weak), Java (moderado), TypeScript/Kotlin (strong en compilación), Haskell (strong en runtime también)
- **Type errors:** errores detectados por el sistema de tipos — cuánto antes, mejor
- **§6.15 Type Equivalence:**
  - Dos tipos son equivalentes si pueden sustituirse sin coerción
  - *Name equivalence:* equivalentes si tienen el mismo nombre → Kotlin, Java, C con struct
  - *Structure equivalence:* equivalentes si tienen la misma estructura → TypeScript, Go
  - Problema de structure equivalence: `Celsius = Float` y `Fahrenheit = Float` serían equivalentes aunque semánticamente distintos

#### 4.3 Sistemas monomórficos (10 min)
- **Definición:** cada expresión tiene exactamente un tipo
- Ventajas: simple, predecible, herramientas de análisis directas
- Ejemplos: C (sin templates), Pascal clásico, primeras versiones de C
- Limitación: `max(int, int)` y `max(float, float)` requieren funciones separadas → código duplicado

#### 4.4 Polimorfismo — Taxonomía de Strachey/Cardelli (35 min)
*(Louden §8.8–§8.9, Cardelli & Wegner 1985)*

**Tres formas principales:**

**a) Polimorfismo ad-hoc (sobrecarga):**
- Un nombre = múltiples implementaciones con distinto tipo
- El compilador elige la versión correcta según los tipos de los argumentos
- TypeScript: sobrecarga mediante *function overloads* (firmas declaradas + implementación única)
- *Distinción importante:* no es "un tipo acepta varios valores" — es "varios tipos comparten un nombre"
```typescript
// Firmas de sobrecarga
function area(radio: number): number
function area(base: number, altura: number): number
// Implementación única
function area(a: number, b?: number): number {
  return b !== undefined ? a * b / 2 : Math.PI * a * a
}
```
> **Contraste (Kotlin):** sobrecarga directa con funciones de igual nombre y distinta firma de parámetros.

**b) Polimorfismo paramétrico (generics):**
- Una implementación = válida para múltiples tipos sin conocerlos
- El tipo es un *parámetro* de la función o estructura
- *Louden §8.9:* "Parametric polymorphism is the ability for a function to be applied to arguments of different types"
- TypeScript con generics:
```typescript
function primero<T>(lista: T[]): T { return lista[0] }

// Con upper bound (constraint)
function max<T extends { valueOf(): number }>(a: T, b: T): T {
  return a.valueOf() > b.valueOf() ? a : b
}

// Clase genérica
class Caja<T> {
  constructor(private contenido: T) {}
  abrir(): T { return this.contenido }
}

// Tipo genérico con varianza estructural (TypeScript usa tipado estructural)
type ReadonlyBox<T> = { readonly value: T }  // covariant naturalmente
```
- **Varianza en TypeScript:** TypeScript usa tipado estructural — la varianza se infiere automáticamente; no hay `out`/`in` explícito como en Kotlin
  - Contraste Kotlin: `out T` (covariant = productor), `in T` (contravariant = consumidor)
  - En TypeScript: `Readonly<T>` hace las propiedades covariant naturalmente

**c) Polimorfismo por subtipo (subtype/inclusion polymorphism):**
- Un tipo S es subtipo de T si S puede usarse donde se espera T (*Liskov*)
- Implementado mediante herencia e interfaces
- TypeScript: `interface Forma`, clases que lo implementan → `function total(f: Forma[])`
```typescript
interface Forma {
  area(): number
}
class Circulo implements Forma {
  constructor(private r: number) {}
  area() { return Math.PI * this.r ** 2 }
}
class Rectangulo implements Forma {
  constructor(private b: number, private h: number) {}
  area() { return this.b * this.h }
}

function areaTotal(formas: Forma[]) {
  return formas.reduce((sum, f) => sum + f.area(), 0)
}
```
> **Contraste (Kotlin):**
```kotlin
interface Forma { fun area(): Double }
data class Circulo(val r: Double) : Forma { override fun area() = Math.PI * r * r }
fun areaTotal(formas: List<Forma>) = formas.sumOf { it.area() }
```
- Diferencia con polimorfismo paramétrico:
  | Aspecto | Paramétrico | Por subtipo |
  |---------|------------|------------|
  | Mecanismo | Type parameter `<T>` | Herencia / interface |
  | Binding | Compilación | Runtime (dispatch) |
  | Overhead | Sin overhead | Virtual dispatch |
  | Restricción | Upper bounds | Is-a relationship |

#### 4.5 Lenguajes fuertemente tipados y clases (20 min)
- **Clases como tipos:**
  - En POO, la clase define un tipo → los objetos son instancias del tipo
  - El sistema de tipos verifica asignabilidad entre tipos de clase
  - TypeScript: `const x: Animal = new Perro()` — OK si `Perro implements Animal`
- **Chequeo estático con herencia:**
  - El compilador verifica en tiempo de compilación que los métodos llamados existen en el tipo declarado
  - El dispatch dinámico ocurre en runtime (polimorfismo por subtipo)
- **Type aliases y branded types en TypeScript:**
```typescript
type UserId = string                              // alias simple
type Email = string & { readonly _brand: 'email' } // branded type — semejante al Celsius/Fahrenheit
type Celsius = number & { readonly _brand: 'celsius' }
type Fahrenheit = number & { readonly _brand: 'fahrenheit' }
// Celsius y Fahrenheit no son intercambiables aunque ambos sean number
```
- **`as const` y tipos literales:**
```typescript
const CONFIG = { debug: true, version: '1.0' } as const
// Tipo inferido: { readonly debug: true; readonly version: '1.0' }
```
- **Contraste con Kotlin:**
  - `typealias UserId = String` — alias simple sin nuevo tipo (igual que TypeScript)
  - `@JvmInline value class Email(val value: String)` — tipo wrapper sin overhead
  - `reified` type parameters: acceder al tipo en runtime desde un genérico (TypeScript no tiene equivalente)
```kotlin
inline fun <reified T> esInstanciaDe(obj: Any): Boolean = obj is T
```

---

### Bloque 5 — Síntesis y Cierre (30 min)

#### 5.1 Mapa conceptual integrador (10 min)
- Dibujar en la pizarra: Tipos → [Primitivos | Ordinales | Compuestos | Recursivos | Opcionales]
- Sistemas de tipos → [Monomórfico | Polimórfico [Ad-hoc | Paramétrico | Subtipo]]
- Null Safety → Opcionales vs. tipos nulables vs. uniones discriminadas
- Línea temporal de evolución: C (1972) → Java (1995) → Python typing (2014) → TypeScript (2012/maduro 2017) → Kotlin (2016) → Rust (2015)

#### 5.2 Discusión: Diseño de sistemas de tipos (10 min)
- *"¿Por qué TypeScript hace `strictNullChecks` opt-in mientras Kotlin lo tiene activado siempre?"*
- *"¿Cuándo usar uniones discriminadas (TypeScript) vs. sealed class (Kotlin) vs. herencia tradicional?"*
- *"¿Qué perdió TypeScript al tener tipado estructural en lugar de nominal?"*
- Conexión con MÓDULO VI (T09): "El sistema de tipos es la suma de las decisiones de binding que vimos antes"

#### 5.3 Vista previa próximos temas (5 min)
- T11: Expresiones y Estructuras de Control — coerciones, sobrecarga de operadores
- T14 (futuro): Inferencia de tipos (HM), sistema de tipos formal, subtyping teórico

#### 5.4 Consigna del TP (5 min)
- Presentación breve del TP asociado — exploración de sistemas de tipos en un lenguaje elegido

---

## Recursos Bibliográficos

### Principal
- **Sebesta, Robert** (2019). *Concepts of Programming Languages*, 12ª ed. Pearson.
  - **Cap. 6 — Data Types** (pp. 259–324): §6.1–§6.16 completo
    - §6.1 Introduction, §6.2 Primitive Data Types (incl. Complex §6.2.1.3), §6.3 Character String Types, §6.4 Enumeration Types, §6.5 Array Types (incl. Rectangular/Jagged §6.5.6 y Slices §6.5.7), §6.6 Associative Arrays, §6.7 Record Types, §6.8 Tuple Types, §6.9 List Types, §6.10 Union Types, §6.11 Pointer and Reference Types (incl. Reference Types §6.11.5), §6.12 Optional Types, §6.13 Type Checking, §6.14 Strong Typing, §6.15 Type Equivalence, §6.16 Theory and Data Types

### Secundarios
- **Louden, Kenneth C.** (2012). *Programming Languages: Principles and Practice*, 3ª ed. Cengage.
  - **Cap. 8 — Data Types and Type Information** (pp. 328–405): §8.1–§8.10
  - Especialmente §8.5 (Type Equivalence), §8.6 (Type Checking), §8.8 (Polymorphic Type Checking), §8.9 (Explicit Polymorphism)

- **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms*, 2ª ed. Springer.
  - **Cap. 8 — Composite Types** (pp. 136–282): §8.2 (Type Safety), §8.4 (Arrays), §8.7 (Union types)

### Referencia de Lenguaje
- TypeScript Handbook — Types: https://www.typescriptlang.org/docs/handbook/2/types-from-types.html
- TypeScript Handbook — Narrowing & Null: https://www.typescriptlang.org/docs/handbook/2/narrowing.html
- TypeScript Handbook — Generics: https://www.typescriptlang.org/docs/handbook/2/generics.html
- Kotlin Documentation — Null Safety (contraste): https://kotlinlang.org/docs/null-safety.html
- Kotlin Documentation — Generics (contraste): https://kotlinlang.org/docs/generics.html

---

## Materiales de Apoyo a Preparar

| Material | Descripción | Responsable |
|---------|-------------|------------|
| Diagrama: Taxonomía de tipos | Árbol visual de clasificación | Docente |
| Código comparativo: arrays | 4 variantes (C, TypeScript, Python, Haskell) | Docente |
| Ejercicio: Null Safety Refactor | Código JavaScript (sin strict) con NPEs para reescribir en TypeScript | Docente |
| Ejercicio: Diseño de ADT | Problema de Figura geométrica en TypeScript y C | Docente |
| Tabla de sistemas de tipos | 8 lenguajes × 5 dimensiones | Docente |

---

## Posibles Preguntas de Parcial (por nivel Bloom)

| Nivel | Ejemplo |
|-------|---------|
| Recordar | ¿Qué es un tipo de dato? Enumerar 4 tipos primitivos en TypeScript |
| Comprender | Explicar la diferencia entre equivalencia nominal y estructural con un ejemplo |
| Aplicar | Reescribir código JavaScript con posibles NPEs usando TypeScript con `strictNullChecks` |
| Analizar | Comparar `union` de C con discriminated unions de TypeScript: ¿cuál es más seguro y por qué? |
| Evaluar | Dado un programa en TypeScript con `any`, evaluar el nivel de tipado fuerte y proponer mejoras |

---

## Notas del Diseñador

> **Scope alert:** El tema de *inferencia de tipos* (Hindley-Milner, polimorfismo let) queda explícitamente fuera de T10 y se reserva para T14. Si Roberto lo propone durante la clase, referirlo a T14.

> **Diferenciación con T09:** T09.1 cubre binding de tipos (estático/dinámico/gradual) y T09.2 cubre scope y aliases. T10 parte del "qué son los tipos" sin repetir "cuándo se asignan".

> **Lenguaje principal:** TypeScript es el hilo conductor de todos los ejemplos. Los contrastes con C, Haskell, Kotlin y Python se hacen en comparaciones puntuales, no como narrativas paralelas. Kotlin aparece como contraste cuando aporta construcciones sin equivalente directo en TypeScript (sealed class, reified, data class copy()).

> **Estado:** BORRADOR. Requiere revisión y aprobación del docente antes de avanzar a generación de clase.

---

## Revisi�n Post-publicaci�n � 2026-05-26

### Feedback del docente
Las filminas tienen demasiado c�digo sin explicaci�n profunda de qu� significan las construcciones.
Ejemplo concreto: Int32Array no explicaba que los datos se almacenan en binario puro.
**Principio aplicado:** Las filminas deben ser **autocontenidas** � el alumno no necesita recursos externos para entender el c�digo mostrado.

### Cambios aplicados en filminas.md

| Slide | Cambio |
|-------|--------|
| **[F-05]** Enteros | Agregado bloque visual de complemento a 2 � muestra patr�n de bits para +42, -1, -42 con explicaci�n del bit de signo y el rango asim�trico |
| **[F-06]** IEEE 754 | Agregado diagrama ASCII de la estructura de 64 bits (signo/exponente/mantisa) + explicaci�n de por qu� 0.1 no tiene representaci�n exacta en base 2 |
| **[F-20]** Arrays TS | Comentario de Int32Array expandido para indicar almacenamiento binario, bytes exactos y uso de ArrayBuffer |
| **[F-20b]** *(nuevo)* | Slide dedicado a TypedArrays: contraste boxing vs. binario, tabla completa de tipos con bits y rangos, ejemplo con ArrayBuffer expl�cito y casos de uso |
| **[F-25]** C union | Agregado bloque que explica qu� es un "bit pattern" � muestra los 4 bytes de 42 como int32 y qu� pasa al releerlos como float IEEE 754 |

### Total slides despu�s de revisi�n
- Antes: 58 slides (F-00 a F-57 + portada)
- Despu�s: 59 slides (F-00 a F-58 + portada, con F-20b nuevo)

---

## Revisi�n Post-publicaci�n � 2026-05-26

### Feedback del docente
Las filminas tienen demasiado c�digo sin explicaci�n profunda de qu� significan las construcciones.
Ejemplo concreto: Int32Array no explicaba que los datos se almacenan en binario puro.
**Principio aplicado:** Las filminas deben ser **autocontenidas** � el alumno no necesita recursos externos para entender el c�digo mostrado.

### Cambios aplicados en filminas.md

| Slide | Cambio |
|-------|--------|
| **[F-05]** Enteros | Agregado bloque visual de complemento a 2 � muestra patr�n de bits para +42, -1, -42 con explicaci�n del bit de signo y el rango asim�trico |
| **[F-06]** IEEE 754 | Agregado diagrama ASCII de la estructura de 64 bits (signo/exponente/mantisa) + explicaci�n de por qu� 0.1 no tiene representaci�n exacta en base 2 |
| **[F-20]** Arrays TS | Comentario de Int32Array expandido para indicar almacenamiento binario, bytes exactos y uso de ArrayBuffer |
| **[F-20b]** *(nuevo)* | Slide dedicado a TypedArrays: contraste boxing vs. binario, tabla completa de tipos con bits y rangos, ejemplo con ArrayBuffer expl�cito y casos de uso |
| **[F-25]** C union | Agregado bloque que explica qu� es un "bit pattern" � muestra los 4 bytes de 42 como int32 y qu� pasa al releerlos como float IEEE 754 |

### Total slides despu�s de revisi�n
- Antes: 58 slides (F-00 a F-57 + portada)
- Despu�s: 59 slides (F-00 a F-58 + portada, con F-20b nuevo)
