# Filminas — Tema 10
## Tipos de Datos y Sistemas de Tipos

> **Curso:** Paradigmas y Lenguajes de Programación — UNTDF IDEI 2026
> **Duración:** 360 minutos (clase unificada — Módulo VII completo)
> **Lenguaje principal:** TypeScript | Contrastes: Kotlin, Haskell, C, Python
> **Referencia principal:** Sebesta, *Concepts of Programming Languages* 12ª ed., Cap. 6

---

## PORTADA

---

### [F-00] Portada

@tipo: portada
@imagen: background
@prompt-imagen: fondo abstracto de red de nodos de tipos conectados con flechas de herencia y composición, paleta azul oscuro y cyan, estilo minimalista académico

# Tipos de Datos y Sistemas de Tipos

Paradigmas y Lenguajes de Programación · UNTDF IDEI 2026
Tema 10 · Módulo VII

---

## BLOQUE 0 — Apertura y Conexión (15 min)

---

### [F-01] ¿Qué diferencia hay entre `1` en tres lenguajes?

@tipo: socratica

# `1` en C, Python y Haskell — ¿son lo mismo?

```c
int x = 1;     // C: entero de 32 bits, complemento a 2, sin GC
```
```python
x = 1          # Python: objeto int de precisión arbitraria, GC
```
```haskell
x = 1          -- Haskell: Num a => a (polimórfico, determinado en uso)
```

**¿Qué distingue a cada `1`?**

- ¿El tamaño en memoria?
- ¿Las operaciones disponibles?
- ¿Cuándo se verifica el tipo?
- ¿Quién libera la memoria?

---

### [F-02] ¿Qué vimos en T09? ¿Qué veremos hoy?

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama de dos columnas: izquierda muestra binding de variables con flechas de tiempo (estático, dinámico), derecha muestra árbol de clasificación de tipos de datos con ramas primitivos, compuestos, sistemas

# Conexión T09 → T10

## T09 respondió: *¿Cuándo* se vincula un tipo a una variable?
- Binding estático vs. dinámico
- Tipado gradual
- Scope y aliases

## T10 responde: *¿Qué* son los tipos como estructuras formales
- Taxonomías de tipos
- Tipos compuestos e implementaciones
- Sistemas de tipos: monomórfico vs. polimórfico

---

### [F-03] Hoja de ruta de la clase

@tipo: diagrama
@imagen: content
@prompt-imagen: mapa de ruta horizontal con 5 paradas etiquetadas: Primitivos y Ordinales, Agregación y Colecciones, Punteros y Null Safety, Sistemas de Tipos, Síntesis

# 360 minutos — 5 bloques

| Bloque | Contenido | Tiempo |
|--------|-----------|--------|
| 1 | Tipos Primitivos y Ordinales | 70 min |
| 2 | Tipos de Agregación y Colecciones | 90 min |
| 3 | Punteros, Null Safety, Tipos Recursivos | 75 min |
| 4 | Sistemas de Tipos — Polimorfismo | 80 min |
| 5 | Síntesis, Discusión y Cierre | 30 min |

> **Hilo conductor:** TypeScript como lenguaje principal · contrastes en C, Kotlin, Haskell, Python

---

## BLOQUE 1 — Tipos Primitivos y Ordinales (70 min)

---

### [F-04] ¿Qué es un tipo de dato?

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de dos círculos superpuestos: uno etiquetado "conjunto de valores" y otro "operaciones admisibles", con una flecha que apunta al resultado "tipo de dato"

# Definición formal

## Sebesta §6.1
> "A data type defines a **collection of data values** and a set of **predefined operations** on those values"

## Los tipos sirven para…
- **Legibilidad:** el código expresa la intención
- **Detectabilidad de errores:** el compilador/runtime verifica uso incorrecto
- **Reusabilidad:** abstraer comportamiento por tipo

## Clasificación de tipos
- **Primitivos:** representaciones directas de hardware (`int`, `float`, `bool`, `char`)
- **Compuestos:** construidos sobre primitivos (`struct`, `array`, `union`)
- **Definidos por el usuario:** enumeraciones, subrangos, ADTs

---

### [F-05] Tipos numéricos — Enteros

@tipo: tabla-comparativa

# Enteros en distintos lenguajes

| Lenguaje | Tipo | Tamaño | Nota |
|----------|------|--------|------|
| C | `int` / `long` | 32/64 bits | No hay GC; overflow silencioso |
| Java/Kotlin | `Int` / `Long` | 32/64 bits | JVM; checked exceptions |
| TypeScript | `number` | 64-bit IEEE 754 | **No distingue entero/float** |
| TypeScript | `bigint` | Ilimitado | `9007199254740991n` |
| Python | `int` | Ilimitado | Objeto; GC |

## Atención TypeScript
- `number` es siempre `double` (IEEE 754 de 64 bits)
- Para enteros grandes: `bigint` con literales `n` — `const x = 2n ** 53n`
- `Number.MAX_SAFE_INTEGER` = 2⁵³ − 1

---

### [F-06] Tipos numéricos — Floating Point

@tipo: concepto-mixto

# IEEE 754 y sus consecuencias

## El estándar IEEE 754
- Representación de punto flotante: signo + exponente + mantisa
- TypeScript `number` = IEEE 754 de **64 bits** (double) **siempre**
- Kotlin: `Float` (32 bits) vs `Double` (64 bits)
- Java: idem Kotlin · Python: `float` = double de 64 bits

## La "trampa" clásica

```typescript
console.log(0.1 + 0.2)          // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3)  // false ← ¡No usar == con floats!
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON)  // true ✓
```

## Decimal nativo: ¿cuándo importa?
- TypeScript: **no tiene** decimal nativo → usar `decimal.js` para finanzas
- Contraste: `BigDecimal` en Java/Kotlin; `decimal` en C#
- **Python:** `from decimal import Decimal` — disponible pero no default

---

### [F-07] Tipos numéricos especiales — Complejo y Decimal

@tipo: tabla-comparativa

# Tipos numéricos especiales — decisiones de diseño

| Tipo | Lenguaje | Soporte | Comentario |
|------|----------|---------|------------|
| Complejo | Python | `complex` nativo (`3+4j`) | Primer ciudadano |
| Complejo | Fortran | Nativo | Orientado a cómputo científico |
| Complejo | Java/TS | Solo librería | Decisión: tipo vs. librería |
| Decimal | Python | `decimal.Decimal` | Módulo estándar |
| Decimal | Kotlin/Java | `BigDecimal` | En JDK |
| Decimal | TypeScript | `decimal.js` | Librería externa |
| Boolean | TypeScript | `boolean` (tipo real) | `true` / `false` literales |
| Boolean | C (pre-C99) | `0` / no-cero | Sin tipo propio |

## Pregunta de diseño
> ¿Debe un lenguaje incluir tipos numéricos como `complex` y `decimal` como tipos primitivos, o como librerías de la plataforma?

---

### [F-08] Boolean y Char — Decisiones de diseño

@tipo: tabla-comparativa

# Boolean y Char — Sin equivalente universal

## Boolean
| Lenguaje | Tipo | Observación |
|----------|------|-------------|
| TypeScript | `boolean` | Tipo real: `true` / `false` |
| C (clásico) | No existe | `0` = false, cualquier otro valor = true |
| Python | `bool` | Subtipo de `int`! `True == 1` |
| Kotlin | `Boolean` | Tipo real, no JVM-int |

## Char
| Lenguaje | Tipo | Observación |
|----------|------|-------------|
| TypeScript | **No existe** | Solo `string`; `"a"` es string de longitud 1 |
| Kotlin | `Char` | UTF-16, tipo real |
| C | `char` | Byte (8 bits) — ni Unicode, ni propio |
| Java | `char` | UTF-16; `'a'` es char literal |

> **TypeScript:** no tener `char` es una decisión deliberada — JS históricamente solo tiene `string`.

---

### [F-09] Enumeraciones en TypeScript

@tipo: codigo

# TypeScript — `enum` como tipo real

## Numeric enum

```typescript
enum Direction { Up, Down, Left, Right }
// Up = 0, Down = 1, Left = 2, Right = 3

const move = (dir: Direction) => {
  if (dir === Direction.Up) console.log("subiendo")
}
move(Direction.Up)
```

## String enum — para interoperabilidad con APIs

```typescript
enum Status { Active = 'active', Inactive = 'inactive' }
const s: Status = Status.Active    // valor en runtime: 'active'
```

## `const enum` — inlining en compilación

```typescript
const enum Color { Red = 0, Green = 1, Blue = 2 }
// El compilador reemplaza Color.Red por 0 directamente → sin objeto en runtime
```

> **`const enum`:** optimización de compilación — el enum no existe en JS emitido.

---

### [F-10] Enumeraciones — Comparación multilenguaje

@tipo: tabla-comparativa

# Enumeraciones — C vs. TypeScript vs. Kotlin vs. Haskell

| Aspecto | C `enum` | TypeScript `enum` | Kotlin `enum class` | Haskell `data` |
|---------|---------|-------------------|---------------------|----------------|
| Tipo propio | ❌ | ✅ | ✅ | ✅ |
| Type-safe | ❌ (es un `int`) | ✅ | ✅ | ✅ |
| Propiedades | ❌ | Limitado | ✅ | ❌ (ADT) |
| Métodos | ❌ | ❌ | ✅ | ❌ (funciones) |
| Exhaustividad | No | Con `never` | `when` garantiza | Pattern matching |
| Ejemplo | `enum Dir { UP }` | `enum Dir { Up }` | `enum class Dir { UP }` | `data Dir = Up` |

> **Sebesta §6.4.1:** El problema con `enum` en C es que no son type-safe — pueden ser mezclados con enteros sin advertencia del compilador.

---

### [F-11] Subrangos y equivalencia de tipos (introducción)

@tipo: concepto-abstracto

# Subrangos (subrange types)

## Definición
Tipo cuyo rango de valores es un subconjunto contiguo de un tipo ordinal.

## En distintos lenguajes
| Lenguaje | Soporte | Ejemplo |
|----------|---------|---------|
| Pascal | Nativo | `type DiasLaborables = 1..5` |
| Ada | Nativo | `type Day is range 1..7` |
| TypeScript | Simulado | `type Day = 1\|2\|3\|4\|5` (literal union) |
| Kotlin | Aproximado | `IntRange(1, 5)` — no es un tipo separado |

## ¿Por qué importa?
- Pascal / Ada: chequeo **estático** de rango en compilación
- TypeScript literal union: chequeo estático — el compilador rechaza `const d: Day = 6`
- **Tradeoff:** seguridad vs. expresividad vs. rendimiento

---

### [F-12] Equivalencia nominal vs. estructural

@tipo: concepto-mixto

# ¿Cuándo son iguales dos tipos?

## Equivalencia nominal
> Dos tipos son iguales si tienen el **mismo nombre**

```kotlin
data class Celsius(val v: Double)
data class Fahrenheit(val v: Double)
// No son intercambiables — aunque ambas wrappean Double
fun calenta(c: Celsius) { ... }
// calenta(Fahrenheit(100.0)) ← ERROR de compilación ✓
```

## Equivalencia estructural
> Dos tipos son iguales si tienen la **misma estructura**

```typescript
type Punto = { x: number; y: number }
// Cualquier objeto con campos x: number, y: number es compatible
function distancia(p: Punto) { ... }
distancia({ x: 3, y: 4 })   // ✓ — tipado estructural
```

## TypeScript es estructural — ventajas y riesgos
- **Ventaja:** flexibilidad — menos boilerplate, duck typing seguro
- **Riesgo:** `Celsius = number` y `Fahrenheit = number` serían equivalentes → usar branded types

---

### [F-13] Equivalencia — Tabla comparativa de lenguajes

@tipo: tabla-comparativa

# Nominal vs. Estructural por lenguaje

| Lenguaje | Sistema | Observación |
|----------|---------|-------------|
| C (struct) | Nominal (con `typedef`) | Dos `struct` distintos → tipos distintos |
| Java | Nominal | `class A {}` y `class B {}` nunca son iguales |
| Kotlin | Nominal | Herencia/interfaces para compatibilidad |
| TypeScript | **Estructural** | Si la forma coincide, el tipo es compatible |
| Go | Estructural | Interfaces satisfechas implícitamente |
| Haskell | Nominal + paramétrico | `data` define tipos nominales |

## Consecuencia de diseño
> En TypeScript, ¿puedo intercambiar `UserId` y `Email` si ambos son `string`?

```typescript
type UserId = string
type Email  = string
function buscar(id: UserId) { ... }
buscar("correo@dominio.com")    // ← TypeScript lo acepta (estructural)
// Solución: branded types (Bloque 4)
```

---

### [F-14] Actividad rápida — Equivalencia de tipos

@tipo: socratica

# Actividad: ¿compatible o no? (8 min)

## Predicen la compatibilidad:

```typescript
type Punto2D = { x: number; y: number }
type Vector2D = { x: number; y: number }
type Punto3D = { x: number; y: number; z: number }

function graficar(p: Punto2D) { ... }

graficar({ x: 1, y: 2 })         // Caso A — ¿OK?
graficar({ x: 1, y: 2, z: 3 })   // Caso B — ¿OK?

const v: Vector2D = { x: 5, y: 5 }
graficar(v)                        // Caso C — ¿OK?
```

```kotlin
data class Punto2D(val x: Double, val y: Double)
data class Vector2D(val x: Double, val y: Double)
fun graficar(p: Punto2D) { ... }
graficar(Vector2D(5.0, 5.0))    // Caso D (Kotlin) — ¿OK?
```

> **Discusión:** ¿Cuál sistema genera más errores accidentales? ¿Cuál es más flexible?

---

## BLOQUE 2 — Tipos de Agregación y Colecciones (90 min)

---

### [F-15] Strings — Tipo primitivo vs. objeto

@tipo: tabla-comparativa

# Strings: ¿primitivo o objeto?

| Lenguaje | Naturaleza | Mutabilidad | Comparación |
|----------|-----------|-------------|-------------|
| TypeScript | Primitivo (con métodos via boxing) | Inmutable | `===` por valor ✓ |
| Kotlin | Objeto (`String`) | Inmutable | `==` por valor (llama `equals`) |
| Java | Objeto (`String`) | Inmutable | `==` por **referencia** ← ERROR clásico |
| C | Puntero a `char[]` terminado en `\0` | Mutable | `strcmp()` (no `==`) |
| Python | Objeto `str` | Inmutable | `==` por valor ✓ |

## Operaciones comunes (Sebesta §6.4)
> "The most common string operations are: assignment, concatenation, substring reference, comparison, and pattern matching"

```typescript
const s = "hola"
s.length            // 4
s.toUpperCase()     // "HOLA" (nueva string — inmutable)
s.slice(1, 3)       // "ol"
s.includes("ol")    // true
`¡${s}!`            // "¡hola!" — template literal
```

---

### [F-16] Arrays — Taxonomía por binding time

@tipo: tabla-comparativa
@imagen: content
@prompt-imagen: tabla visual con cuatro tipos de arrays mostrando cuándo se fija la forma y el rango: estático en compilación, semi-dinámico en stack, dinámico de heap con tamaño fijo, dinámico de heap flexible

# Arrays — Clasificación (Sebesta §6.5)

| Categoría | Forma | Rango | Almacenamiento | Ejemplo |
|-----------|-------|-------|----------------|---------|
| **Estático** | Estático | Compila | Estático | `int a[10]` en C (global) |
| **Semi-dinámico (stack)** | Fija en runtime | Post-elaboración | Stack (se libera al salir) | `int a[n]` en C99 (local) |
| **Heap fijo** | Dinámica (heap) | Fija luego | Heap (manual) | `new Array<number>(n)` en TS |
| **Heap flexible** | Totalmente dinámica | Cambia | Heap (GC) | `number[]` en TS / `list` Python |

## Figura 6.2 de Sebesta
> La categorización es por **binding time de forma** y **binding time de rango**.

---

### [F-17] Arrays — Función de acceso multidimensional

@tipo: concepto-mixto

# Arrays multidimensionales — cómo se accede en memoria

## Row-major (C, Java, Kotlin, Python)
> Los elementos de una fila se almacenan contiguos

```
a[i][j] → base + (i × cols + j) × size
```

## Column-major (Fortran, MATLAB, R)
> Los elementos de una columna se almacenan contiguos

```
a[i][j] → base + (i + j × rows) × size
```

## ¿Por qué importa?
- **Cache locality:** acceder en el orden incorrecto → cache misses → lentitud
- Multiplicación de matrices en C: iterar en row-major order = hasta 10× más rápido

```typescript
// Row-major access — eficiente
for (let i = 0; i < n; i++)
  for (let j = 0; j < m; j++)
    suma += matrix[i][j]   // accede fila a fila ✓
```

---

### [F-18] Arrays — Rectangulares vs. Jagged + Slices

@tipo: tabla-comparativa

# Rectangular vs. Jagged vs. Slices

## Rectangular (Fortran, C#)
- Todos los sub-arrays tienen **la misma longitud**
- `int[,]` en C#: acceso más rápido y lineal en memoria

## Jagged (C, Java, Kotlin)
- Array de **punteros a arrays** — cada fila puede tener distinto tamaño
- Java: **todos** los arrays multidimensionales son jagged por diseño
- Mayor flexibilidad; mayor overhead por indirección

## Slices — referencia sin copia
| Lenguaje | Sintaxis | Comportamiento |
|----------|----------|----------------|
| Python | `lista[1:4]` | Produce **nueva lista** (copia) |
| Kotlin | `lista.subList(1, 4)` | Vista **viva** — comparte memoria |
| Go | `a[1:4]` | Ciudadano de primera clase (length + capacity) |
| Ada | `A(2..4)` | Slice de array nativo |

---

### [F-19] Arrays asociativos — Maps

@tipo: codigo

# Arrays asociativos — Mapeos finitos

## Sebesta §6.8
> "An associative array is an unordered collection of data elements indexed by an equal number of values called **keys**"

## TypeScript

```typescript
// Map tipado
const scores = new Map<string, number>([["Ana", 9], ["Luis", 7]])
scores.set("Marta", 8)
console.log(scores.get("Ana"))   // 9
scores.has("Luis")                // true
scores.delete("Luis")

// Record — objeto como mapa de clave string
const config: Record<string, boolean> = { dark: true, sound: false }
config["alerts"] = true
```

## Contraste Kotlin

```kotlin
val scores = mutableMapOf("Ana" to 9, "Luis" to 7)
scores["Marta"] = 8
println(scores["Ana"])    // 9
```

> **TypeScript:** `Map<K,V>` para tipos arbitrarios de clave · `Record<string, V>` para claves string

---

### [F-20] Código completo — Arrays en TypeScript

@tipo: codigo

# Arrays en TypeScript — cuatro formas

```typescript
// 1. Array dinámico (heap flexible)
const lista: number[] = [1, 2, 3]
lista.push(4)                             // [1, 2, 3, 4]

// 2. Array de tamaño conocido (heap fijo tipado)
const fijo: number[] = new Array(5).fill(0).map((_, i) => i * 2)
// [0, 2, 4, 6, 8]

// 3. Typed Array — sin overhead de boxing (para rendimiento)
const binario: Int32Array = new Int32Array([10, 20, 30])

// 4. Readonly — inmutable (contraste con lista)
const constante: ReadonlyArray<number> = [1, 2, 3]
// constante.push(4) ← ERROR de compilación ✓
```

## Contraste Kotlin

```kotlin
val fijo = IntArray(5) { it * 2 }        // [0, 2, 4, 6, 8]
val lista = mutableListOf(1, 2, 3)
lista.add(4)
val inmutable: List<Int> = listOf(1, 2, 3)
```

---

### [F-21] Registros e interfaces en TypeScript

@tipo: codigo

# Registros — `interface` y `type` en TypeScript

## Sebesta §6.6
> "A record is a collection of data fields, identified by name"

```typescript
// interface — preferida para objetos extensibles
interface Usuario {
  nombre: string
  email:  string
  edad:   number
}

// type — equivalente funcional
type Punto = { x: number; y: number }

// Inmutabilidad con readonly
type PuntoFijo = { readonly x: number; readonly y: number }

// Tipo con campo opcional
interface Config { debug: boolean; nivel?: number }
```

## Contraste Kotlin `data class`

```kotlin
data class Usuario(val nombre: String, val email: String, val edad: Int)
// Genera: equals, hashCode, toString, copy() automáticos
// TypeScript no tiene equivalente nativo — se implementa manualmente
```

---

### [F-22] Tuplas en TypeScript

@tipo: codigo

# Tuplas — producto cartesiano formal

## Definición
Tipo `A × B` = todos los pares `(a, b)` con `a: A`, `b: B`

## TypeScript — tuplas literales

```typescript
const par: [string, number] = ["hola", 42]

// Desestructuración
const [nombre, edad] = par
console.log(nombre)   // "hola"

// Tipo nombrado
type RGB = [number, number, number]
const rojo: RGB = [255, 0, 0]

// Tupla con elemento opcional (TypeScript 3+)
type HttpResponse = [number, string, string?]
```

## Comparación

| Lenguaje | Tuplas | Observación |
|----------|--------|-------------|
| TypeScript | `[A, B, C]` | Literales tipados |
| Kotlin | `Pair<A,B>` / `Triple<A,B,C>` | Solo hasta 3 elementos nativos |
| Python | `(a, b, c)` | Inmutables por defecto |
| Haskell | `(a, b, c)` | Tipos algebraicos nativos |

---

### [F-23] Listas funcionales — Definición (Sebesta §6.9)

@tipo: concepto-abstracto

# List Types — Tipo secuencia con acceso funcional

## Origen: LISP (1958)

## Propiedades fundamentales
- **head:** primer elemento
- **tail:** resto de la lista
- **cons:** construcción añadiendo al frente
- **Recursividad inherente:** lista = `head` + `tail` (otra lista)

## Diferencia clave con arrays
| Aspecto | Array | Lista enlazada |
|---------|-------|----------------|
| Acceso aleatorio | O(1) | O(n) |
| Inserción al frente | O(n) | O(1) |
| Uso de memoria | Contigua | Fragmentada (punteros) |
| Mutabilidad | Mutable por defecto | Inmutable en FP |

## Haskell — listas homogéneas
```haskell
xs = [1, 2, 3, 4]
head xs         -- 1
tail xs         -- [2, 3, 4]
1 : xs          -- [1, 1, 2, 3, 4]
```

---

### [F-24] Listas funcionales — TypeScript y Kotlin

@tipo: tabla-comparativa

# Listas — Implementaciones multilenguaje

| Lenguaje | Tipo | Estructura real | Inmutable |
|----------|------|----------------|-----------|
| TypeScript | `T[]` / `Array<T>` | Array dinámico | Solo con `ReadonlyArray<T>` |
| TypeScript | `ReadonlyArray<T>` | Array dinámico | ✅ |
| Kotlin | `List<T>` | ArrayList | ✅ |
| Kotlin | `MutableList<T>` | ArrayList | ❌ |
| Python | `list` | Array dinámico (¡no lista enlazada!) | ❌ |
| Haskell | `[a]` | Lista enlazada real | ✅ siempre |

## Sebesta §6.9
> "Lists are collections of data that can have varying numbers of elements and to which elements can be easily added or removed from either end"

---

### [F-25] Uniones libres (unsafe) — C `union`

@tipo: codigo

# Uniones en C — el problema clásico

## C `union` comparte espacio de memoria

```c
union Data {
  int   i;
  float f;
  char  c;
};

union Data d;
d.i = 42;
printf("%f\n", d.f);  // ← Lee basura — interpretación incorrecta del bit pattern
```

## El problema fundamental
**Sebesta §6.10:**
> "The fundamental problem with unions in Pascal and C is that they are **unsafe** — there is no way to ensure that a union is accessed in the correct way"

- El programador debe recordar qué campo fue escrito
- No hay verificación en compilación ni en runtime
- Fuente de bugs difíciles de detectar

---

### [F-26] Uniones discriminadas (safe) — TypeScript

@tipo: codigo

# TypeScript — Discriminated Unions

## El discriminante garantiza acceso correcto

```typescript
type Result<T> =
  | { kind: 'success'; value: T }
  | { kind: 'error';   message: string }

function handle(r: Result<number>) {
  switch (r.kind) {
    case 'success':
      console.log(r.value)    // TypeScript sabe: r es { kind: 'success'; value: number }
      break
    case 'error':
      console.log(r.message)  // TypeScript sabe: r es { kind: 'error'; message: string }
      break
  }
}
```

## Seguridad de tipos
- El campo `kind` actúa como **etiqueta discriminante**
- TypeScript **narrowea** el tipo en cada rama del switch
- Con `--strictNullChecks`, si hay un caso sin manejar: error de compilación

---

### [F-27] Uniones discriminadas — TypeScript vs. Kotlin vs. Haskell

@tipo: tabla-comparativa

# Tagged Unions — tres implementaciones

## Kotlin `sealed class`

```kotlin
sealed class Result<out T> {
  data class Success<T>(val value: T)          : Result<T>()
  data class Error(val message: String)         : Result<Nothing>()
}

fun handle(r: Result<Int>) = when (r) {   // exhaustividad GARANTIZADA por el compilador
  is Result.Success -> println(r.value)
  is Result.Error   -> println(r.message)
}
```

## Haskell ADT

```haskell
data Result a = Success a | Error String

handle :: Result Int -> IO ()
handle (Success v) = print v
handle (Error msg) = putStrLn msg
```

| Aspecto | TypeScript | Kotlin | Haskell |
|---------|-----------|--------|---------|
| Mecanismo | `kind` explícito | `sealed class` | ADT (`data`) |
| Exhaustividad | Con `never` trick | Compilador garantiza | Pattern matching |
| Runtime tag | Campo de objeto | `is` check | Constructor tag |

---

### [F-28] Actividad — Diseño de ADT (5 min)

@tipo: socratica

# Actividad: "Figura geométrica" como union

## Tarea: modelar en TypeScript Y en C

```typescript
// TypeScript — usar discriminated union
type Figura = ??? // completar

function area(f: Figura): number { ??? }
```

```c
// C — usar union sin discriminante
union FigData { float radio; float base; };
enum FigKind { CIRCULO, RECTANGULO };
struct Figura {
  enum FigKind kind;
  union FigData data;
};
// ¿Qué errores puede cometer el programador?
```

## Discusión
- ¿Cuál versión puede generar errores en runtime? ¿Por qué?
- ¿Cuál garantiza exhaustividad?
- ¿Qué tiene que hacer el compilador para lograrlo?

---

## BLOQUE 3 — Punteros, Null Safety y Tipos Recursivos (75 min)

---

### [F-29] Tipo puntero — Definición y semántica

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de memoria con una variable "ptr" que contiene una dirección de memoria, una flecha apuntando a una celda de heap etiquetada con un valor, y otra variable "null" señalando a nada

# Tipo puntero

## Sebesta §6.11.1
> "A pointer type variable has a range of values that consists of **memory addresses** and a special value, **nil**"

## Operaciones básicas (C)
```c
int x = 42;
int* ptr = &x;    // & → toma la dirección de x
int y = *ptr;     // * → derreferencia: accede al valor en la dirección

ptr++;            // aritmética de punteros — avanza sizeof(int) bytes
```

## Usos legítimos de punteros
- Manejo indirecto de datos en el heap
- Paso de estructuras grandes por referencia (eficiencia)
- Construcción de estructuras dinámicas (listas enlazadas, árboles)

---

### [F-30] Punteros — Problemas clásicos

@tipo: tabla-comparativa
@imagen: content
@prompt-imagen: ilustración de tres problemas de memoria: un puntero colgante apuntando a zona liberada, una flecha de memory leak sin referencia pero con bloque en heap, y un doble free con dos flechas al mismo bloque

# Punteros inseguros — Catálogo de problemas

| Problema | Qué pasa | Detectado por |
|---------|----------|---------------|
| **Dangling pointer** | Puntero apunta a memoria ya liberada | Valgrind / AddressSanitizer |
| **Memory leak** | Memoria asignada sin referencia, sin liberar | Valgrind / Heaptrack |
| **Double free** | Liberar el mismo bloque dos veces → UB | AddressSanitizer |
| **Null dereference** | `*null` → crash | OS (SIGSEGV) |
| **Buffer overflow** | Aritmética fuera de rango → sobreescritura | AddressSanitizer |

## Soluciones históricas (Sebesta §6.11.4)
- **Tombstones:** cada heap object tiene un tombstone — al liberar, el tombstone se marca; los punteros apuntan al tombstone, no al objeto
- **Locks and keys:** cada puntero lleva una clave; al acceder, se verifica contra el lock del bloque

---

### [F-31] Garbage Collection

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de grafo de objetos en heap con flechas de referencia, algunos nodos alcanzables desde raíz marcados en verde, otros nodos aislados marcados en rojo como "recolectables"

# Garbage Collection — Eliminación automática de problemas

## Reference counting (Python, Swift)
- Cada objeto lleva un contador de referencias
- Al llegar a 0 → se libera inmediatamente
- **Problema:** ciclos de referencia → memory leak

## Tracing GC (Java/JVM, Kotlin, Go, JS/TS)
- Periodicamente, el GC recorre el grafo de objetos desde las raíces
- Los objetos no alcanzables son recolectados
- Kotlin/Java: Garbage First (G1GC), ZGC — pausas breves

## Ventajas del GC
- ✅ Elimina dangling pointers
- ✅ Elimina memory leaks (en ciclos: tracing GC)
- ✅ Elimina double free

## Costo
- ⚠️ Pausas de GC (stop-the-world)
- ⚠️ Mayor uso de memoria (mantiene objetos para análisis)

---

### [F-32] Referencias vs. Punteros

@tipo: tabla-comparativa

# Referencias ≠ Punteros (Sebesta §6.11.5)

> "A reference variable is a **constant pointer** that is always **implicitly dereferenced**"

| Aspecto | Puntero (C) | Referencia (C++) | Referencias JS/TS/Kotlin |
|---------|-------------|-----------------|--------------------------|
| Aritmética | ✅ `ptr++` | ❌ No permitida | ❌ No existe |
| Reasignable | ✅ | ❌ Siempre apunta al mismo objeto | ✅ Variables reasignables |
| Puede ser null | ✅ `NULL` | ❌ Debe inicializarse | ✅ (con nullable) |
| Derreferencia explícita | ✅ `*ptr` | ❌ Implícita | ❌ Implícita |
| Gestión de memoria | Manual | Manual (o RAII) | GC automático |

## TypeScript / JavaScript
- **Sin punteros explícitos** — todo objeto vive en heap, gestionado por V8
- Las variables almacenan **referencias implícitas** (igual que Java/Kotlin)
- El GC se encarga de todo — sin `free()`, sin `delete`

---

### [F-33] Tipos recursivos — Definición

@tipo: concepto-abstracto

# Tipos recursivos

## Definición
Un tipo que se **define en términos de sí mismo**

## Lista enlazada en C
```c
struct Node {
  int          value;
  struct Node* next;   // referencia recursiva — posible porque es un puntero (tamaño fijo)
};
```

## Lista en Haskell
```haskell
data List a = Nil | Cons a (List a)
-- Isomorfo al tipo built-in [a]
```

> **Clave:** la recursión es posible porque el "campo recursivo" es una referencia/puntero (tamaño fijo), no el objeto completo (que sería infinito)

---

### [F-34] Tipos recursivos — Árbol binario en TypeScript

@tipo: codigo

# Árbol binario como tipo recursivo en TypeScript

```typescript
type BinaryTree<T> =
  | { kind: 'leaf' }
  | { kind: 'node'; value: T; left: BinaryTree<T>; right: BinaryTree<T> }

// Función que explota el tipo recursivo
function depth<T>(t: BinaryTree<T>): number {
  if (t.kind === 'leaf') return 0
  return 1 + Math.max(depth(t.left), depth(t.right))
}

const arbol: BinaryTree<number> = {
  kind: 'node', value: 1,
  left:  { kind: 'node', value: 2, left: { kind: 'leaf' }, right: { kind: 'leaf' } },
  right: { kind: 'leaf' }
}
```

## Contraste Kotlin `sealed class`

```kotlin
sealed class Tree<T> {
  object Empty : Tree<Nothing>()
  data class Node<T>(val value: T, val left: Tree<T>, val right: Tree<T>) : Tree<T>()
}
```

> **Relación:** tipos recursivos + uniones discriminadas = estructuras inductivas (Haskell, Kotlin sealed, TypeScript)

---

### [F-35] El problema del null — "Mi error de un billón de dólares"

@tipo: concepto-abstracto

# El problema del null

## Tony Hoare — inventor del null pointer (1965, ALGOL W)
> *"I call it my billion-dollar mistake. [...] It has led to innumerable errors, vulnerabilities, and system crashes"*
> — QCon 2009

## El problema
- **En Java (y C, Python sin disciplina):** cualquier referencia puede ser `null`
- No hay distinción de tipos entre `"una string válida"` y `null`
- El error ocurre en **runtime** — el compilador no puede ayudar

```java
String nombre = getUser().getName();  // puede retornar null
nombre.toUpperCase();                  // NullPointerException en runtime ❌
```

## La solución: hacer null parte del sistema de tipos
- Si `null` es un valor posible → el tipo debe decirlo explícitamente
- Si el tipo no incluye `null` → el compilador garantiza que nunca es null

---

### [F-36] TypeScript Null Safety — Operadores

@tipo: tabla-comparativa

# TypeScript — Operadores de null safety

Con `"strictNullChecks": true` en `tsconfig.json`

| Operador | Nombre | Comportamiento |
|----------|--------|----------------|
| `T \| null` | Tipo nulable | Declara que `T` puede ser null |
| `T \| undefined` | Tipo indefinido | Parámetros opcionales por defecto |
| `x?.prop` | Optional chaining | Si `x` es null/undefined → retorna `undefined` |
| `x ?? valor` | Nullish coalescing | Si `x` es null/undefined → usa `valor` |
| `x!` | Non-null assertion | Fuerza acceso — puede fallar en runtime |
| `if (x !== null)` | Type narrowing | El compilador infiere tipo más estrecho |
| `function f(x?: T)` | Parámetro opcional | `x` es `T \| undefined` |

---

### [F-37] TypeScript Null Safety — Código completo

@tipo: codigo

# Null Safety en acción

```typescript
interface User { name: string; email: string | null }

function sendEmail(user: User) {
  // Nullish coalescing: usa "sin email" si email es null/undefined
  const dest = user.email ?? 'sin email'

  // Optional chaining: retorna undefined si email es null (no lanza error)
  const upper = user.email?.toUpperCase()

  // Type narrowing: en este bloque, TypeScript sabe que email es string
  if (user.email !== null) {
    console.log(`Enviando a ${user.email.toUpperCase()}`)
  }

  // Non-null assertion: NO usar salvo que estés seguro
  // const forced = user.email!.toUpperCase()  ← peligroso
}
```

> **Con `strict: true`:** el compilador rechaza acceder a `user.email.toUpperCase()` directamente — te fuerza a verificar primero.

---

### [F-38] TypeScript vs. Kotlin vs. Haskell — Null Safety

@tipo: tabla-comparativa

# Null Safety — Comparación multilenguaje

| Lenguaje | Mecanismo | Activación | Safety |
|----------|-----------|-----------|--------|
| C / Java (pre-8) | `null` sin restricción | Siempre | ❌ Ninguna |
| Python | `None` sin restricción | Siempre | ❌ Ninguna |
| TypeScript | `T \| null` + `strictNullChecks` | **Opt-in** | ✅ Con flag |
| Kotlin | `T` vs. `T?` + operadores `?.` `?:` `!!` | **Siempre** | ✅ Por diseño |
| Haskell | `Maybe a = Nothing \| Just a` | Siempre | ✅ Monádico |
| Rust | `Option<T> = None \| Some(T)` | Siempre | ✅ Tipo de datos |

## Comparación de operadores

| TypeScript | Kotlin | Significado |
|-----------|--------|-------------|
| `x ?? y` | `x ?: y` | Si null → usar y (Elvis) |
| `x?.prop` | `x?.prop` | Acceso seguro (igual sintaxis) |
| `x!` | `x!!` | Forzar no-null (peligroso) |
| `if (x !== null)` | `if (x != null)` | Type narrowing |

---

### [F-39] Actividad — Null Safety Refactor (10 min)

@tipo: socratica

# Actividad: Refactorizar código con NPE potencial

## Código JavaScript (sin `strictNullChecks`)

```javascript
function getUserCity(userId) {
  const user = findUser(userId)           // puede retornar null
  const address = user.address            // NPE si user es null
  return address.city.toUpperCase()       // NPE si city es null
}
```

## Tarea: reescribir en TypeScript con `strictNullChecks`

```typescript
// Definir los tipos con null safety
interface Address { city: string | null; country: string }
interface User { name: string; address: Address | null }

function findUser(id: string): User | null { /* ... */ }

function getUserCity(userId: string): string {
  // ¿Cómo implementar esto de forma segura?
  // Usar: ?. ?? if !== null
}
```

> **Discusión final:** ¿Por qué TypeScript hace `strictNullChecks` opt-in mientras Kotlin no?

---

## BLOQUE 4 — Sistemas de Tipos: Monomórficos, Polimórficos y Strong Typing (80 min)

---

### [F-40] Type Checking — Definición y coerción

@tipo: concepto-abstracto

# Type Checking — Chequeo de tipos

## Sebesta §6.13
> "The activity of ensuring that the **operands** of an operator are of **compatible types**"

## Tipo compatible
- El tipo exacto esperado, **o**
- Un tipo convertible implícitamente (→ **coerción**)

## Coerción implícita vs. conversión explícita
```c
int i = 5;
float f = i + 3.14;    // coerción implícita: int → float antes de sumar

float g = (float) i;   // conversión explícita (casting)
```

## Widening vs. Narrowing
```
int → long → float → double     (widening — sin pérdida de información)
double → float → int             (narrowing — pérdida posible → warning)
```

## Type error
Aplicación de un operador a un operando de tipo **inapropiado**

---

### [F-41] Type Checking — Estático vs. Dinámico

@tipo: concepto-mixto

# ¿Cuándo se chequean los tipos?

## Chequeo estático (compilación)
- Todos los bindings de tipos son estáticos → el compilador puede verificar todo
- TypeScript, Kotlin, Java, Haskell
- **Ventaja:** errores detectados antes de ejecutar → más eficiente en producción

## Chequeo dinámico (runtime)
- Los bindings son dinámicos → la verificación ocurre en ejecución
- Python, JavaScript (puro), Ruby
- **Ventaja:** más flexible; **Costo:** overhead en runtime + errores tardíos

## TypeScript — caso especial
```typescript
const x: string = "hola"   // el tipo es static — existe en compilación
// En runtime: el código es JavaScript puro — los tipos se borran (type erasure)
// El chequeo estático de TypeScript ocurre SOLO en el compilador
```

> **Sebesta §6.13:** "If all bindings of variables to types are static in a language, then type checking can nearly always be done statically"

---

### [F-42] Visión general — Dimensiones de un sistema de tipos

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama de tres ejes en espacio tridimensional: eje X "cuándo verifica" con extremos Estático-Dinámico, eje Y "qué tan rígido" con extremos Weak-Strong, eje Z "cuántos tipos" con extremos Monomórfico-Polimórfico, con puntos representando lenguajes C Python TypeScript Kotlin Haskell

# Sistemas de tipos — Tres dimensiones

## Dimensión 1: ¿Cuándo?
- **Estático:** compilación (TypeScript, Kotlin, Haskell, Java)
- **Dinámico:** runtime (Python, JavaScript, Ruby)

## Dimensión 2: ¿Qué tan rígido?
- **Strong typing:** todos los errores de tipo son detectados (siempre)
- **Weak typing:** coerciones implícitas amplias, errores posibles en runtime

## Dimensión 3: ¿Cuántos tipos por valor?
- **Monomórfico:** cada expresión tiene exactamente un tipo
- **Polimórfico:** una expresión puede tener múltiples tipos

> **Louden §8.1:** "Un sistema de tipos es el conjunto de reglas que define cómo los tipos son **asignados**, **verificados** y **combinados** en un lenguaje"

---

### [F-43] Strong Typing — Definición y matices

@tipo: concepto-abstracto

# Strong Typing (Sebesta §6.14)

## Definición
> "A programming language is **strongly typed** if **type errors are always detected**"

## Los lenguajes más fuertemente tipados (Sebesta)
> "Haskell and Ada are the most strongly typed languages"

## El problema de las coerciones implícitas
- `int + float` en C → conversión implícita: ¿es eso weak typing?
- **La zona gris:** coerciones numéricas amplias = debilidad de tipado

## Tabla: ¿cuán fuerte es el tipado?

| Lenguaje | ¿Strongly typed? | Razón |
|----------|-----------------|-------|
| C / C++ | ❌ NO | Uniones sin discriminación, `void*`, coerciones |
| Java | ⚠️ MODERADO | Coerciones numéricas implícitas (widening) |
| Python | ❌ NO en práctica | Sin anotaciones → sin chequeo estático real |
| TypeScript (strict) | ✅ EN COMPILACIÓN | El runtime (JS) no tiene tipos |
| Kotlin | ✅ | Strong en compilación y runtime (JVM) |
| Haskell | ✅ | El más estricto — sin coerciones implícitas |

---

### [F-44] Sistemas monomórficos

@tipo: concepto-abstracto

# Sistemas monomórficos

## Definición
> Cada expresión tiene **exactamente un tipo**

## Ejemplo: C sin templates
```c
int max_int(int a, int b) { return a > b ? a : b; }
float max_float(float a, float b) { return a > b ? a : b; }
// Misma lógica, dos funciones — código duplicado inevitable
```

## Ventajas
- Simple y predecible
- Herramientas de análisis directas
- Sin overhead de polimorfismo

## Limitación
- **Código duplicado:** `max(int, int)` y `max(float, float)` requieren funciones separadas
- No escala a bibliotecas grandes
- Motivación histórica para introducir el polimorfismo

---

### [F-45] Polimorfismo — Taxonomía de Strachey/Cardelli

@tipo: diagrama
@imagen: content
@prompt-imagen: árbol de clasificación del polimorfismo: raíz "Polimorfismo", dos ramas principales "Ad-hoc" y "Universal", bajo Ad-hoc "Sobrecarga" y "Coerción", bajo Universal "Paramétrico" y "Subtipo (inclusión)"

# Polimorfismo — Taxonomía (Louden §8.8–§8.9, Cardelli & Wegner 1985)

## Polimorfismo Ad-hoc
- **Sobrecarga (overloading):** mismo nombre, múltiples implementaciones por tipo
- **Coerción:** conversión implícita que permite que un tipo sea tratado como otro

## Polimorfismo Universal
- **Paramétrico (generics):** una implementación para todos los tipos — el tipo es un parámetro
- **Subtipo / Inclusión:** S puede usarse donde se espera T si S es subtipo de T (Liskov)

> **Diferencia clave:** ad-hoc = apariencia de uniformidad; paramétrico = uniformidad real

---

### [F-46] Polimorfismo ad-hoc — Sobrecarga en TypeScript

@tipo: codigo

# Sobrecarga de funciones en TypeScript

## Firmas de sobrecarga + implementación única

```typescript
// Firmas declaradas (interfaz visible al consumidor)
function area(radio: number): number
function area(base: number, altura: number): number

// Implementación única (no visible desde afuera)
function area(a: number, b?: number): number {
  return b !== undefined
    ? (a * b) / 2          // triángulo
    : Math.PI * a * a      // círculo
}

area(5)       // → círculo (r=5)
area(3, 4)    // → triángulo (base=3, altura=4)
```

## Contraste Kotlin — sobrecarga directa

```kotlin
fun area(radio: Double): Double = Math.PI * radio * radio
fun area(base: Double, altura: Double): Double = base * altura / 2
```

> **Distinción:** sobrecarga ≠ polimorfismo paramétrico. Son múltiples funciones distintas — el compilador elige cuál llamar.

---

### [F-47] Polimorfismo paramétrico — Generics en TypeScript

@tipo: codigo

# Generics — una implementación para todos los tipos

```typescript
// Función genérica — T es el parámetro de tipo
function primero<T>(lista: T[]): T { return lista[0] }

primero([1, 2, 3])          // → 1  (T inferred como number)
primero(["a", "b", "c"])    // → "a" (T inferred como string)

// Con upper bound — T debe tener valueOf()
function max<T extends { valueOf(): number }>(a: T, b: T): T {
  return a.valueOf() > b.valueOf() ? a : b
}

// Clase genérica
class Caja<T> {
  constructor(private contenido: T) {}
  abrir(): T { return this.contenido }
}

// Tipo genérico
type ReadonlyBox<T> = { readonly value: T }
```

## Louden §8.9
> "Parametric polymorphism is the ability for a function to be applied to arguments of **different types** without changing the code"

---

### [F-48] Polimorfismo paramétrico — Varianza

@tipo: tabla-comparativa

# Varianza en tipos genéricos

## ¿Puede `Caja<Gato>` usarse donde se espera `Caja<Animal>`?

| Varianza | Definición | Kotlin | TypeScript |
|----------|-----------|--------|-----------|
| **Covariante** | `Caja<Gato>` ≤ `Caja<Animal>` — produce T | `out T` | Inferida automáticamente |
| **Contravariante** | `Caja<Animal>` ≤ `Caja<Gato>` — consume T | `in T` | Inferida automáticamente |
| **Invariante** | No hay subtipado | (por defecto) | (por defecto si read+write) |

## TypeScript — varianza estructural automática
```typescript
type ReadonlyBox<T> = { readonly value: T }     // covariant naturalmente
type WriteBox<T>    = { setValue(v: T): void }   // contravariant naturalmente
```

## Kotlin — varianza declarada explícita
```kotlin
class Productor<out T>(val value: T)    // covariant: solo produce T
class Consumidor<in T> { fun usar(v: T) {} }   // contravariant: solo consume T
```

---

### [F-49] Polimorfismo por subtipo

@tipo: codigo

# Subtipo / Inclusión — Herencia e interfaces

## Principio de Liskov (LSP)
> S es subtipo de T si cualquier programa que usa T funciona correctamente al reemplazarlo por S

## TypeScript — interfaces como contrato de subtipo

```typescript
interface Forma { area(): number }

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

areaTotal([new Circulo(3), new Rectangulo(4, 5)])   // polimorfismo en acción
```

---

### [F-50] Comparación de los tres tipos de polimorfismo

@tipo: tabla-comparativa

# Tres polimorfismos — Comparación

| Aspecto | Ad-hoc (sobrecarga) | Paramétrico (generics) | Por subtipo (herencia) |
|---------|---------------------|----------------------|----------------------|
| **Mecanismo** | Nombre compartido | Parámetro de tipo `<T>` | Herencia / interface |
| **Binding** | Compilación (static dispatch) | Compilación | Runtime (dynamic dispatch) |
| **Overhead** | Ninguno | Ninguno (erasure en JVM) | Virtual dispatch |
| **Restricción** | Firmas distintas | Upper bounds (`extends`) | Is-a relationship |
| **Ejemplo TS** | Function overloads | `function f<T>(...)` | `class C implements I` |
| **Expresividad** | Baja | Alta | Media-Alta |

---

### [F-51] Branded Types y Type Aliases

@tipo: codigo

# TypeScript — Branded Types como equivalencia nominal simulada

## El problema con aliases simples

```typescript
type UserId = string   // alias — estructuralmente idéntico a string
type Email  = string   // alias — estructuralmente idéntico a string

function buscar(id: UserId) { ... }
buscar("correo@example.com")  // TypeScript acepta — no detecta el error semántico
```

## Solución: Branded Types

```typescript
type UserId = string & { readonly _brand: 'UserId' }
type Email  = string & { readonly _brand: 'Email'  }

// Son estructuralmente distintos → TypeScript los rechaza al intercambiar
function buscar(id: UserId) { ... }
// buscar("correo@example.com" as Email)  ← ERROR ✓

// Crear con función factory
function makeUserId(s: string): UserId { return s as UserId }
```

## `as const` y tipos literales

```typescript
const CONFIG = { debug: true, version: '1.0' } as const
// Tipo: { readonly debug: true; readonly version: '1.0' }
// (no boolean y string — literales exactos)
```

---

### [F-52] Type Equivalence — Revisita final

@tipo: concepto-abstracto

# Type Equivalence — Puntos clave (Sebesta §6.15)

## Name equivalence — Kotlin
```kotlin
// Celsius y Fahrenheit: mismo wrapper, tipos distintos
@JvmInline value class Celsius(val v: Double)
@JvmInline value class Fahrenheit(val v: Double)
fun calentarHasta(temp: Celsius) { ... }
// calentarHasta(Fahrenheit(100.0)) ← ERROR de compilación ✓
```

## Structure equivalence — TypeScript
```typescript
type Celsius    = { value: number; unit: 'C' }
type Fahrenheit = { value: number; unit: 'F' }
// Estructuralmente distintos — TypeScript los diferencia por el literal 'C'/'F'
// Sin el campo discriminante → serían equivalentes (¡peligroso!)
```

## Implicación de diseño
> La equivalencia estructural de TypeScript puede generar tipos semánticamente distintos que el compilador acepta intercambiar — usar branded types o campos discriminantes para evitarlo.

---

## BLOQUE 5 — Síntesis y Cierre (30 min)

---

### [F-53] Mapa conceptual integrador

@tipo: diagrama
@imagen: content
@prompt-imagen: mapa conceptual jerárquico completo: raíz "Tipos de Datos", ramas hacia Primitivos (enteros, float, bool, char), Compuestos (array, registro, tupla, unión), Recursivos (lista, árbol), Opcionales (null, Maybe); segunda raíz "Sistemas de Tipos" con ramas Monomórfico y Polimórfico (Ad-hoc, Paramétrico, Subtipo); flechas de conexión entre conceptos

# Mapa conceptual — Tipos y Sistemas de Tipos

## Tipos de Datos
- **Primitivos:** enteros · float (IEEE 754) · boolean · char
- **Ordinales:** enumeraciones · subrangos
- **Compuestos:** array · registro · tupla · unión discriminada · lista
- **Recursivos:** árbol · lista enlazada · ADT
- **Opcionales:** `T | null` · `Maybe a` · `Option<T>`

## Sistemas de Tipos
- **Dimensiones:** estático/dinámico · strong/weak · mono/polimórfico
- **Equivalencia:** nominal (Kotlin, Java) · estructural (TypeScript, Go)
- **Polimorfismo:** ad-hoc · paramétrico · subtipo
- **Null safety:** typed nulls → compile-time guarantees

---

### [F-54] Evolución de sistemas de tipos

@tipo: timeline

# Línea temporal — Evolución de sistemas de tipos

| Año | Lenguaje / Evento | Aporte al sistema de tipos |
|-----|-------------------|---------------------------|
| 1958 | LISP | Tipos dinámicos, listas como ciudadanos |
| 1968 | ALGOL 68 | Tipos compuestos ricos, equivalencia estructural |
| 1972 | C | Punteros, uniones, tipado débil |
| 1978 | ML | Inferencia de tipos (Hindley-Milner), polimorfismo paramétrico |
| 1985 | C++ | Templates, sobrecarga, herencia múltiple |
| 1987 | Haskell (precursor) | ADTs, type classes, sin null (Maybe) |
| 1995 | Java | GC, referencias, generics (2004) |
| 2012 | TypeScript | Tipado estructural sobre JS, generics, discriminated unions |
| 2016 | Kotlin | Null safety por diseño, data classes, sealed |
| 2015 | Rust | Ownership, lifetime, `Option<T>` sin null |

---

### [F-55] Discusión — Diseño de sistemas de tipos

@tipo: socratica

# Tres preguntas para pensar

## Pregunta 1
> *¿Por qué TypeScript hace `strictNullChecks` opt-in mientras Kotlin lo tiene activado siempre?*

Pista: retrocompatibilidad con JavaScript, gradual adoption, codebase existentes

## Pregunta 2
> *¿Cuándo usar uniones discriminadas (TypeScript) vs. sealed class (Kotlin) vs. herencia tradicional?*

Pista: exhaustividad, extensibilidad (Expression Problem), overhead de objetos

## Pregunta 3
> *¿Qué pierde TypeScript al tener tipado estructural en lugar de nominal?*

Pista: `UserId` y `Email` como strings, `Celsius` y `Fahrenheit` como numbers — ¿qué pasa?

---

### [F-56] Conexión con próximos temas

@tipo: concepto-abstracto

# Hacia dónde vamos desde T10

## Conexión hacia adelante

### T11 — Expresiones y Estructuras de Control
- Coerciones implícitas en expresiones aritméticas
- Sobrecarga de operadores — polimorfismo ad-hoc en operadores
- Short-circuit evaluation y su relación con tipos booleanos

### T14 — Sistemas de Tipos Formales (futuro)
- Inferencia de tipos — algoritmo Hindley-Milner
- λ-cálculo tipado como base formal
- Polimorfismo let (Milner) y sus límites
- Subtyping formal con reglas de deducción

## Recordar el vínculo con T09
> *"El sistema de tipos es la suma de las decisiones de binding que vimos en T09"*
> Un tipo primitivo, estáticamente vinculado, con equivalencia nominal = exactamente lo que vimos en la 5-tupla de variables.

---

### [F-57] Consigna del TP

@tipo: concepto-abstracto

# TP — Sistemas de Tipos en la práctica

## Objetivo
Explorar el sistema de tipos de un lenguaje **no visto en profundidad en clase** y compararlo con TypeScript.

## Consigna (detalle en TP doc)
1. **Elegir** un lenguaje: Rust, Swift, Scala, Elm, Zig, Nim u otro aprobado
2. **Documentar** al menos 5 aspectos del sistema de tipos:
   - Equivalencia (nominal/estructural)
   - Null safety (o ausencia)
   - Polimorfismo (tipos disponibles)
   - Strong/weak typing
   - Tipo de GC o gestión de memoria
3. **Comparar** con TypeScript usando ejemplos de código propios
4. **Evaluar:** ¿qué hace mejor? ¿qué sacrifica? ¿qué decisión de diseño te parece más acertada?

## Entrega
- Repositorio Git con código de ejemplo + informe `.md`
- Fecha: ver cronograma en la plataforma

---

### [F-58] Cierre y bibliografía

@tipo: cierre

# Cierre — Tipos de Datos y Sistemas de Tipos

## Qué construimos hoy
- Taxonomía completa de tipos: primitivos → compuestos → recursivos → opcionales
- Sistemas de tipos como espacio de decisiones de diseño
- TypeScript como ejemplo de sistema de tipos moderno, pragmático y estructural

## Para profundizar
- **Sebesta Cap. 6** — fuente primaria de toda la clase
- **Louden §8.8–§8.9** — polimorfismo formal
- **Gabbrielli §8.2, §8.4, §8.7** — type safety y tipos compuestos
- **TypeScript Handbook:** https://www.typescriptlang.org/docs/handbook/2/types-from-types.html

## Próxima clase: T11 — Expresiones y Estructuras de Control

> *"Un lenguaje de programación es solo tan bueno como su sistema de tipos."*
> — Bjarne Stroustrup

---
