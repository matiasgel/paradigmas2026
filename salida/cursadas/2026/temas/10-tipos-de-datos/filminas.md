# Filminas — Tema 10
## Tipos de Datos y Sistemas de Tipos

> **Curso:** Paradigmas y Lenguajes de Programación — UNTDF IDEI 2026
> **Duración:** 360 minutos (clase unificada — Módulo VII completo)
> **Lenguaje principal:** TypeScript | Contrastes: Kotlin, Haskell, C, Python
> **Referencia principal:** Sebesta, *Concepts of Programming Languages* 12ª ed., Cap. 6
> **Reconstrucción:** 2026-06-28 — fidelidad a `clase_dada.txt` (1122 líneas)
> **Fuente baseline:** `clase_dada.txt` + respaldo ChromaDB (Sebesta, Louden, Gabbrielli)

---

## PORTADA

---

### [F-00] Portada

@tipo: portada
@imagen: background
@prompt-imagen: red abstracta de nodos geométricos de distintos tamaños conectados por líneas finas, paleta azul oscuro y cyan, composición asimétrica con un nodo central más grande irradiando conexiones hacia nodos periféricos más pequeños, estilo minimalista académico

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

## ¿Qué distingue a cada `1`?

- ¿El tamaño en memoria?
- ¿Las operaciones disponibles?
- ¿Cuándo se verifica el tipo?
- ¿Quién libera la memoria?

---

### [F-02] ¿Qué vimos? ¿Qué veremos hoy?

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama de dos columnas separadas por línea vertical: columna izquierda con tres rectángulos pequeños apilados etiquetados con símbolos abstractos de flechas y un reloj, columna derecha con árbol jerárquico de círculos conectados por líneas

# Conexión T09 → T10

## Ya sabemos: ¿Cuándo se vincula un tipo a una variable?
- Binding estático vs. dinámico
- Tipado gradual
- Ámbito y aliases

## Vemos hoy: ¿Qué son los tipos como estructuras formales?
- Taxonomías de tipos
- Tipos compuestos e implementaciones
- Sistemas de tipos: monomórfico vs. polimórfico

---

### [F-03] Hoja de ruta de la clase

@tipo: diagrama
@imagen: content
@prompt-imagen: línea horizontal con cinco hitos circulares de izquierda a derecha conectados por una flecha larga, cada hito con un ícono geométrico distinto (cuadrado, triángulo, hexágono, estrella, círculo), paleta azul y gris

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
@prompt-imagen: dos círculos superpuestos tipo diagrama de Venn: círculo izquierdo con puntos dispersos, círculo derecho con flechas pequeñas, zona de superposición destacada con un ícono central, paleta azul y naranja

# Definición formal

## Sebesta §6.1
> "Un tipo de dato define una **colección de valores de datos** y un conjunto de **operaciones predefinidas** sobre esos valores"

## Los tipos sirven para…
- **Legibilidad:** el código expresa la intención
- **Detectabilidad de errores:** el compilador/runtime verifica uso incorrecto
- **Reusabilidad:** abstraer comportamiento por tipo

---

### [F-05] Clasificación de tipos

@tipo: concepto-abstracto

# Clasificación canónica

- **Primitivos:** `int`, `float`, `bool`, `char`
- **Definidos por el usuario:** `enum`, `subrange`, `type alias`, `branded types`
- **Compuestos:** `arrays`, `records`, `structs`, `tuples`, `maps`, `unions`
- **Referenciales:** `pointers`, `references`
- **Algebraicos:** productos, sumas, ADTs
- **Paramétricos:** `generics`, `templates`

> **Hilo conductor:** TypeScript como lenguaje principal · contrastes en C, Kotlin, Haskell, Python

---

### [F-06] Tipos primitivos

@tipo: concepto-abstracto

# Tipos primitivos — Preguntas centrales

Son tipos básicos provistos por el lenguaje o la plataforma.

## Preguntas que guían el estudio
- ¿Qué valores representan?
- ¿Qué operaciones permiten?
- ¿Cómo se almacenan?
- ¿Qué errores puede detectar el compilador?
- ¿Qué queda delegado al runtime?

## Familias
- **Numéricos:** enteros, floating point, decimal, complex
- **Lógicos:** `boolean`
- **Texto elemental:** `char` / `string`

---

### [F-07] Tipos numéricos — Enteros

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

## Representación binaria — complemento a 2

Los enteros se almacenan como patrones de bits. Ejemplo con 32 bits:

```
Valor │ Binario (32 bits, complemento a 2)
──────┼─────────────────────────────────────────────
  +1  │ 0000 0000 0000 0000 0000 0000 0000 0001
 +42  │ 0000 0000 0000 0000 0000 0000 0010 1010
  -1  │ 1111 1111 1111 1111 1111 1111 1111 1111
 -42  │ 1111 1111 1111 1111 1111 1111 1101 0110
```

> El bit más significativo (bit 31) es el **signo**: `0` = positivo, `1` = negativo.
> Por esto el rango no es simétrico: de **−2.147.483.648** a **+2.147.483.647** (2³¹ negativos, 2³¹−1 positivos).
> En C: desbordamiento de `int` es **undefined behavior** — el compilador puede hacer cualquier cosa.

---

### [F-08] Tipos numéricos — Floating Point

@tipo: concepto-mixto

# IEEE 754 y sus consecuencias

## El estándar IEEE 754
- Representación de punto flotante: **signo + exponente + mantisa**
- TypeScript `number` = IEEE 754 de **64 bits** (double) **siempre**
- Kotlin: `Float` (32 bits) vs `Double` (64 bits)
- Java: idem Kotlin · Python: `float` = double de 64 bits

## La "trampa" clásica

```typescript
console.log(0.1 + 0.2)          // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3)  // false ← ¡No usar == con floats!
```

## Decimal nativo: ¿cuándo importa?
- TypeScript: **no tiene** decimal nativo → usar `decimal.js` para finanzas
- Contraste: `BigDecimal` en Java/Kotlin; `decimal` en C#
- Python: `from decimal import Decimal` — disponible pero no default

## Estructura de bits de `double` (IEEE 754, 64 bits)

```
 Bit 63     Bits 62–52       Bits 51–0
┌────────┬─────────────┬──────────────────────────────────────┐
│ Signo  │  Exponente  │          Mantisa (fracción)          │
│ 1 bit  │   11 bits   │              52 bits                 │
└────────┴─────────────┴──────────────────────────────────────┘
```

- **Signo:** `0` = positivo, `1` = negativo
- **Exponente:** indica la escala como potencia de 2 (desplazado en 1023)
- **Mantisa:** la parte fraccional — `1.mantisa × 2^(exponente−1023)`

> Ejemplo: `0.1` en decimal no tiene representación finita en base 2.
> En binario es periódico: `0.1₁₀ = 0.000110011001100110011...₂`
> Como la mantisa tiene tamaño limitado, el valor se redondea a `0.10000000000000000555...`
> **Por eso** `0.1 + 0.2 ≠ 0.3` en cualquier lenguaje que use IEEE 754.

---

### [F-09] Tipos numéricos especiales — Complejo y Decimal

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

## Pregunta de diseño
> ¿Deben ser tipos primitivos del lenguaje o abstracciones de biblioteca?

**Idea central:** Un lenguaje decide qué tipos incluye en su núcleo según sus prioridades: eficiencia, simplicidad, seguridad, precisión o dominio de aplicación.

---

### [F-10] Boolean y Char — tipos discretos básicos

@tipo: tabla-comparativa

# Boolean y Char — Sin equivalente universal

## Boolean
- Dominio mínimo de verdad: `true` / `false`
- En lenguajes modernos suele ser un tipo propio
- En C clásico se representaba con enteros: `0 = false`, no-cero = `true`

## Char
- Representa unidades de texto, pero no tiene equivalente universal
- En C puede verse como entero pequeño
- En Java/Kotlin es un tipo propio (UTF-16)
- En TypeScript **no existe** `char`: se usa `string`

| Lenguaje | Boolean | Char | Observación |
|----------|---------|------|-------------|
| TypeScript | `boolean` real | **no existe** | `"a"` es string de longitud 1 |
| C (clásico) | `0`/no-cero | `char` (byte) | Sin tipo propio |
| Kotlin | `Boolean` | `Char` UTF-16 | Tipos reales |
| Python | `bool` (subtipo de `int`!) | `str` de longitud 1 | `True == 1` |

> **Idea central:** Incluso los tipos "simples" dependen de decisiones de diseño del lenguaje.

---

### [F-11] Tipos ordinales y dominios finitos

@tipo: concepto-abstracto

# Tipos ordinales y dominios finitos

## Definición
Un tipo **ordinal** tiene valores discretos que pueden enumerarse y, en muchos lenguajes, ordenarse.

## Ejemplos
- `boolean`: `false`, `true`
- `char`: `'a'`, `'b'`, `'c'`
- `integer`: `..., -1, 0, 1, 2`
- `enum`: `Up`, `Down`, `Left`, `Right`
- `subrange`: `1..10`

## Propiedades
- Valores discretos
- Sucesor / predecesor
- Comparación por orden
- Posibilidad de definir rangos válidos

> **Idea central:** Los tipos ordinales permiten que el sistema de tipos modele dominios finitos o restringidos.

---

### [F-12] Enum TypeScript

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

> Una enumeración crea un dominio simbólico cerrado.

---

### [F-13] Enumeraciones — Comparación multilenguaje

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

> **Sebesta §6.4.1:** El problema con `enum` en C es que **no son type-safe** — pueden ser mezclados con enteros sin advertencia del compilador.

---

### [F-14] Rangos y subrangos — ejemplo Python

@tipo: codigo

# Rangos y subrangos

## Definiciones
- **Rango:** porción contigua de valores dentro de un tipo ordinal
- **Subrango:** tipo cuyo dominio queda restringido a un rango de otro tipo ordinal

```
1..10       → 1, 2, 3, ..., 10
0..100      → 0, 1, 2, ..., 100
'a'..'z'    → 'a', 'b', 'c', ..., 'z'
```

## Ejemplos de subrangos
```
Nota = 0..10
Mes = 1..12
DiaDelMes = 1..31
```

## Python — `range` sin subrangos nativos

```python
# Python tiene range, pero no subrangos nativos.
range(0, 11)     # representa los valores: 0, 1, 2, ..., 10

notas = range(0, 11)
8 in notas       # → True
15 in notas      # → False

# Pero esto no crea un tipo Nota:
nota = 15        # → válido para Python

# Para modelar un subrango, usamos validación:
class Nota:
    def __init__(self, valor: int):
        if valor < 0 or valor > 10:
            raise ValueError("Nota inválida")
        self.valor = valor
```

> **Idea central:** Python permite representar rangos, pero la restricción del dominio debe programarse explícitamente.

---

## BLOQUE 2 — Tipos de Agregación y Colecciones (90 min)

---

### [F-15] Tipos compuestos

@tipo: concepto-abstracto

# Tipos compuestos — Formas principales

Un tipo compuesto construye valores más grandes a partir de otros tipos.

## Formas principales
- **Producto:** varios campos simultáneos
  - Ejemplo: `record`, `struct`, `tuple`, `object`
- **Secuencia:** colección ordenada de elementos
  - Ejemplo: `array`, `list`, `string`
- **Mapeo:** asociación clave → valor
  - Ejemplo: `map`, `dictionary`, `record dinámico`
- **Suma / unión:** una alternativa entre varias formas
  - Ejemplo: `union`, `discriminated union`, `sealed class`, `ADT`

---

### [F-16] Strings — secuencias de texto

@tipo: tabla-comparativa

# Strings: ¿primitivo, objeto o array de chars?

| Lenguaje | Naturaleza | Mutabilidad | Comparación |
|----------|-----------|-------------|-------------|
| TypeScript | Primitivo (con métodos via boxing) | Inmutable | `===` por valor ✓ |
| Kotlin | Objeto (`String`) | Inmutable | `==` por valor (llama `equals`) |
| Java | Objeto (`String`) | Inmutable | `==` por **referencia** ← ERROR clásico |
| C | Puntero a `char[]` terminado en `\0` | Mutable | `strcmp()` (no `==`) |
| Python | Objeto `str` | Inmutable | `==` por valor ✓ |

## Operaciones comunes (Sebesta §6.3)
> "Las operaciones más comunes sobre cadenas son: **asignación, concatenación, referencia a subcadenas, comparación y coincidencia de patrones**"

---

### [F-17] Arrays — Taxonomía por binding time

@tipo: tabla-comparativa
@imagen: content
@prompt-imagen: cuatro bloques rectangulares alineados verticalmente cada uno con una grilla de celdas, de arriba a abajo: bloque estático con celdas fijas grises, bloque semi-dinámico con celdas en un marco, bloque heap fijo con celdas dentro de un contorno grueso, bloque heap flexible con celdas de distintos tamaños y una flecha de expansión

# Arrays — Clasificación (Sebesta §6.5)

| Categoría | Forma | Rango | Almacenamiento | Ejemplo |
|-----------|-------|-------|----------------|---------|
| **Estático** | Estático | Compila | Estático | `int a[10]` en C (global) |
| **Semi-dinámico (stack)** | Fija en runtime | Post-elaboración | Stack (se libera al salir) | `int a[n]` en C99 (local) |
| **Heap fijo** | Dinámica (heap) | Fija luego | Heap (manual) | `new Array<number>(n)` en TS |
| **Heap flexible** | Totalmente dinámica | Cambia | Heap (GC) | `number[]` en TS / `list` Python |

> La categorización es por **binding time de forma** y **binding time de rango** (Figura 6.2 de Sebesta).

---

### [F-18] Arrays — Función de acceso multidimensional

@tipo: concepto-mixto

# Arrays multidimensionales — cómo se accede en memoria

## Row-major (C, Java, Kotlin, Python)
> Los elementos de una **fila** se almacenan contiguos

```
a[i][j] → base + (i × cols + j) × size
```

## Column-major (Fortran, MATLAB, R)
> Los elementos de una **columna** se almacenan contiguos

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

### [F-19] Arrays — Rectangulares vs. Jagged + Slices

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

### [F-20] Arrays asociativos — Maps

@tipo: codigo

# Arrays asociativos — Mapeos finitos

## Sebesta §6.8
> "Un array asociativo es una colección **no ordenada** de elementos indexada por **claves**"

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

### [F-21] Arrays en TypeScript — cuatro formas

@tipo: codigo

# Arrays en TypeScript — cuatro formas

```typescript
// 1. Array dinámico: heap flexible
const lista: number[] = [1, 2, 3];
lista.push(4);

// 2. Array con tamaño inicial, pero sigue siendo dinámico
const fijo: number[] = new Array(5).fill(0).map((_, i) => i * 2);
fijo.push(10); // permitido

// 3. TypedArray: tamaño fijo y memoria binaria
const binario: Int32Array = new Int32Array([10, 20, 30]);
// binario.push(40); // error: no existe push

// 4. ReadonlyArray: solo lectura a nivel de TypeScript
const constante: ReadonlyArray<number> = [1, 2, 3];
// constante.push(4); // error de compilación
```

---

### [F-22] TypedArrays — almacenamiento binario directo

@tipo: concepto-mixto

# ¿Por qué `Int32Array` no es lo mismo que `number[]`?

## El problema con `number[]`
En JavaScript/TypeScript, cada `number` es siempre un `double` IEEE 754 de 64 bits,
envuelto en un objeto del motor V8.

## TypedArray: memoria binaria contigua
```typescript
const binario: Int32Array = new Int32Array([10, 20, 30])
// Internamente: un ArrayBuffer de 12 bytes (3 × 4 bytes), sin boxing
// En memoria: [0A 00 00 00 | 14 00 00 00 | 1E 00 00 00] (little-endian)
```

## Familia de TypedArrays

| Tipo | Bits | Rango | Equivalente C |
|------|------|-------|---------------|
| `Int8Array` | 8 | −128 a +127 | `int8_t` |
| `Uint8Array` | 8 | 0 a 255 | `uint8_t` |
| `Int16Array` | 16 | −32.768 a +32.767 | `int16_t` |
| `Int32Array` | 32 | −2.147.483.648 a +2.147.483.647 | `int32_t` |
| `Uint32Array` | 32 | 0 a 4.294.967.295 | `uint32_t` |
| `Float32Array` | 32 | ±3.4 × 10³⁸ (precisión simple) | `float` |
| `Float64Array` | 64 | ±1.8 × 10³⁰⁸ — igual que `number` | `double` |

## ¿Cuándo usar TypedArrays?
- Procesamiento de imagen (`Uint8ClampedArray` para píxeles en Canvas)
- WebGL / shaders — datos de GPU requieren tipos binarios exactos
- Comunicación binaria: WebSocket, FileReader, protocolos de red
- Algoritmos numéricos de alto rendimiento (memoria contigua = menos cache misses)

---

### [F-23] Registros — `interface` y `type` en TypeScript

@tipo: codigo

# Registros — `interface` y `type` en TypeScript

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

### [F-24] Tuplas en TypeScript

@tipo: codigo

# Tuplas — producto cartesiano formal

## Definición
Tipo `A × B` = todos los pares `(a, b)` con `a: A`, `b: B`

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

---

### [F-25] Tipos algebraicos de datos en Haskell

@tipo: codigo

# ADT en Haskell — conjunto cerrado de variantes

Un ADT permite definir un nuevo tipo a partir de un conjunto cerrado de variantes posibles.

```haskell
-- Comentario de una sola línea en Haskell
data Resultado
  = Exito String
  | Error String
  | Cargando

mostrar :: Resultado -> String
mostrar resultado =
  case resultado of
    Exito valor   -> "Valor recibido: " ++ valor
    Error mensaje -> "Error: " ++ mensaje
    Cargando      -> "Cargando..."
```

> Cada variante es un constructor distinto. El `case` pattern matching es exhaustivo.

---

### [F-26] Listas funcionales — Definición y multilenguaje

@tipo: tabla-comparativa

# List Types — Tipo secuencia con acceso funcional

## Origen: LISP (1958)

## Propiedades fundamentales
- **head:** primer elemento
- **tail:** resto de la lista
- **cons:** construcción añadiendo al frente
- **Recursividad inherente:** lista = `head` + `tail` (otra lista)

## Diferencia clave con arrays
- Array: secuencia indexada, acceso rápido por posición
- Lista funcional: secuencia recursiva, acceso por `head`/`tail`

## Haskell — listas homogéneas
```haskell
xs = [1, 2, 3, 4]
head xs         -- 1
tail xs         -- [2, 3, 4]
1 : xs          -- [1, 1, 2, 3, 4]
```

## Implementaciones multilenguaje

| Lenguaje | Tipo | Estructura real | Inmutable |
|----------|------|----------------|-----------|
| TypeScript | `T[]` / `Array<T>` | Array dinámico | ❌ |
| TypeScript | `ReadonlyArray<T>` | Array dinámico | ✅ |
| Kotlin | `List<T>` | ArrayList | ✅ |
| Kotlin | `MutableList<T>` | ArrayList | ❌ |
| Python | `list` | Array dinámico (¡no lista enlazada!) | ❌ |
| Haskell | `[a]` | Lista enlazada real | ✅ siempre |

## Sebesta §6.9
> "Las listas son colecciones de datos que pueden tener una cantidad variable de elementos y a las que se les pueden agregar o quitar elementos fácilmente desde cualquiera de los extremos"

---

### [F-27] Tipos algebraicos: producto vs. suma

@tipo: concepto-mixto

# Producto vs. Suma — las dos operaciones algebraicas

## Tipo producto — un valor contiene A y B
```typescript
type Punto = { x: number; y: number }
// Punto = number × number
```

## Tipo suma — un valor puede ser A o B
```typescript
type Resultado =
  | { kind: "ok";      value: number }
  | { kind: "error";   message: string }
// Resultado = Ok + Error
```

> **Idea central:**
> - Producto = **combinación** (todos los campos)
> - Suma = **alternativa** (uno de los campos, discriminado)

---

### [F-28] Uniones libres (unsafe) — C `union`

@tipo: codigo

# Uniones en C — el problema clásico

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

## ¿Qué es un "bit pattern"?

Cuando se escribe `d.i = 42`, los 4 bytes de la unión toman el patrón binario del entero 42:

```
42 como int32 (complemento a 2):
┌────────┬────────┬────────┬────────┐
│00000000│00000000│00000000│00101010│   ← d.i = 42
└────────┴────────┴────────┴────────┘
```

Al leer `d.f`, esos mismos 4 bytes se **reinterpretan** como un float IEEE 754 — sin conversión, solo se leen los mismos bits con otra semántica. El resultado es **basura aritmética** y el programa continúa sin lanzar ningún error.

> Este es el peligro de las uniones en C: el compilador no sabe qué campo está "activo".
> Las uniones discriminadas (TypeScript `kind`, Kotlin `sealed`) resuelven esto al nivel del sistema de tipos.

---

### [F-29] Uniones discriminadas (safe) — TypeScript

@tipo: codigo

# TypeScript — Discriminated Unions

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

### [F-30] Uniones discriminadas — TypeScript vs. Kotlin vs. Haskell

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

## Comparación

| Aspecto | TypeScript | Kotlin | Haskell |
|---------|-----------|--------|---------|
| Mecanismo | `kind` explícito | `sealed class` | ADT (`data`) |
| Exhaustividad | Con `never` trick | Compilador garantiza | Pattern matching |
| Runtime tag | Campo de objeto | `is` check | Constructor tag |

---

## BLOQUE 3 — Punteros, Null Safety y Tipos Recursivos (75 min)

---

### [F-31] Tipo puntero — Definición y semántica

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de memoria abstracta: cuadro izquierdo con la etiqueta "ptr" conteniendo una flecha, flecha apuntando a un cuadro derecho en una zona etiquetada "heap" con un valor numérico representado por puntos, debajo un cuadro con etiqueta "null" sin flecha

# Tipo puntero

## Sebesta §6.11.1
> "Una variable de tipo puntero tiene un rango de valores que consiste en **direcciones de memoria** y un valor especial, **nil**"

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

### [F-32] Punteros — Problemas clásicos

@tipo: tabla-comparativa
@imagen: content
@prompt-imagen: tres ilustraciones yuxtapuestas: izquierda una flecha apuntando a un rectángulo tachado (dangling), centro un rectángulo gris aislado sin flecha entrante (memory leak), derecha dos flechas apuntando al mismo rectángulo tachado dos veces (double free), paleta roja y gris

# Punteros inseguros — Catálogo de problemas

| Problema | Qué pasa | Lenguaje afectado |
|----------|----------|------------------|
| **Dangling pointer** | Puntero apunta a memoria ya liberada | C, C++ |
| **Memory leak** | Memoria asignada sin referencia, sin liberar | C, C++ |
| **Double free** | Liberar el mismo bloque dos veces → UB | C |
| **Null dereference** | `*null` → crash | Java, C, pre-Kotlin, pre-TS strict |
| **Buffer overflow** | Aritmética fuera de rango → sobreescritura | C |

> Estos problemas son la **principal motivación** histórica para los lenguajes con GC y los sistemas de tipos modernos.

---

### [F-33] Soluciones históricas — Tombstones y Locks

@tipo: concepto-abstracto

# Soluciones históricas (Sebesta §6.11.4)

## Tombstones
- Cada objeto heap tiene un **tombstone** (marcador)
- Al liberar, el tombstone se marca como "liberado"
- Los punteros apuntan al tombstone, no al objeto directo
- Al acceder: si el tombstone está marcado → error en lugar de basura

## Locks and Keys
- Cada puntero lleva una **clave**
- Cada bloque de heap tiene un **lock**
- Al acceder: se verifica que la clave coincida con el lock del bloque
- Si no coinciden → acceso denegado (error detectable)

## Soluciones modernas
- **Garbage Collection** (Java, Kotlin, JS/TS, Python, Go) — elimina dangling y leaks automáticamente
- **Ownership + Borrow checker** (Rust) — verificación en compilación sin GC

> Las soluciones históricas tienen overhead de memoria y rendimiento. El GC las reemplazó en la mayoría de los lenguajes modernos.

---

### [F-34] Referencias vs. Punteros

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

### [F-35] Tipos recursivos — Definición

@tipo: concepto-abstracto

# Tipos recursivos

## Definición
Un tipo que se **define en términos de sí mismo**

## Lista enlazada en C
```c
struct Node {
    int          value;
    struct Node* next;   // referencia recursiva — posible por ser puntero
};
```

## Lista en Haskell
```haskell
data List a = Nil | Cons a (List a)
-- Isomorfo al tipo built-in [a]
```

> **Clave:** la recursión es posible porque el "campo recursivo" es una **referencia/puntero** (tamaño fijo), no el objeto completo (que sería infinito).

---

### [F-36] Tipos recursivos — Árbol binario en TypeScript

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

### [F-37] El problema del null — "Mi error de un billón de dólares"

@tipo: concepto-abstracto

# El problema del null

## Tony Hoare — inventor del null pointer (1965, ALGOL W)
> *"I call it my billion-dollar mistake. [...] It has led to innumerable errors, vulnerabilities, and system crashes"*
> — QCon 2009

## El problema
- En Java (y C, Python sin disciplina): **cualquier referencia puede ser `null`**
- No hay distinción de tipos entre "una string válida" y `null`
- El error ocurre en **runtime** — el compilador no puede ayudar

```java
String nombre = getUser().getName();  // puede retornar null
nombre.toUpperCase();                  // NullPointerException en runtime ❌
```

## La solución: hacer null parte del sistema de tipos
- Si `null` es un valor posible → el tipo debe decirlo explícitamente
- Si el tipo no incluye `null` → el compilador garantiza que nunca es null

---

### [F-38] TypeScript Null Safety — Operadores + código completo

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

## Null Safety en acción

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

> Con `strict: true`, el compilador **rechaza** acceder a `user.email.toUpperCase()` directamente — te fuerza a verificar primero.

---

### [F-39] Null Safety — Comparación multilenguaje

@tipo: tabla-comparativa

# Null Safety — Comparación multilenguaje

| Lenguaje | Mecanismo | Activación | Safety level |
|----------|-----------|-----------|--------------|
| C / Java (pre-8) | `null` sin restricción | Siempre | ❌ Peligroso |
| Python | `None` sin restricción | Siempre | ❌ Peligroso |
| TypeScript | `T \| null` + `strictNullChecks` | **Opt-in** | ✅ (config-dependiente) |
| Kotlin | `T` vs `T?` + operadores `?.` `?:` `!!` | **Siempre** | ✅ Type-safe por diseño |
| Haskell | `Maybe a = Nothing \| Just a` | Siempre | ✅ Type-safe (monádico) |
| Rust | `Option<T> = None \| Some(T)` | Siempre | ✅ Type-safe |

## Comparación de operadores equivalentes

| TypeScript | Kotlin | Significado |
|-----------|--------|-------------|
| `x ?? y` | `x ?: y` | Si null → usar y (Elvis) |
| `x?.prop` | `x?.prop` | Acceso seguro (igual sintaxis) |
| `x!` | `x!!` | Forzar no-null (peligroso) |
| `if (x !== null)` | `if (x != null)` | Type narrowing |

> **Conexión con T02 (mónadas):** `Maybe`/`Option` es la mónada de null safety — `flatMap` = `?.` encadenado.

---

## BLOQUE 4 — Sistemas de Tipos: Monomórficos, Polimórficos y Strong Typing (80 min)

---

### [F-40] Sistemas monomórficos

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
- **Motivación histórica** para introducir el polimorfismo

---

### [F-41] Polimorfismo — Taxonomía

@tipo: diagrama
@imagen: content
@prompt-imagen: árbol jerárquico de clasificación: nodo raíz "Polimorfismo" con dos ramas principales, rama izquierda "Ad-hoc" con dos sub-ramas "Sobrecarga" y "Coerción", rama derecha "Universal" con dos sub-ramas "Paramétrico" y "Subtipo (inclusión)", cada hoja con un pequeño ícono geométrico distintivo

# Polimorfismo — Taxonomía (Louden §8.8–§8.9, Cardelli & Wegner 1985)

## Polimorfismo Ad-hoc
- **Sobrecarga (overloading):** mismo nombre, múltiples implementaciones por tipo
- **Coerción:** conversión implícita que permite que un tipo sea tratado como otro

## Polimorfismo Universal
- **Paramétrico (generics):** una implementación para todos los tipos — el tipo es un parámetro
- **Subtipo / Inclusión:** S puede usarse donde se espera T si S es subtipo de T

> **Diferencia clave:** ad-hoc = apariencia de uniformidad; paramétrico = uniformidad real

---

### [F-42] Polimorfismo ad-hoc — Sobrecarga en TypeScript

@tipo: codigo

# Sobrecarga de funciones en TypeScript

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

### [F-43] Polimorfismo paramétrico — Generics en TypeScript

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

> El tipo es un **parámetro** de la función o estructura — una sola implementación funciona para cualquier T.

---

### [F-44] Polimorfismo por subtipo

@tipo: codigo

# Subtipo / Inclusión — Herencia e interfaces

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

> Un tipo S es subtipo de T si S puede usarse donde se espera T (*Liskov*). El dispatch ocurre en runtime.

---

### [F-45] Comparación de los tres tipos de polimorfismo

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

### [F-46] Type Checking — Definición y coerción

@tipo: concepto-abstracto

# Type Checking — Chequeo de tipos

## Sebesta §6.13
> "El proceso de verificar que los **operandos** de un operador sean de tipos **compatibles**"

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
> Aplicación de un operador a un operando de tipo **inapropiado**

## Estático vs. dinámico (Sebesta §6.13)
- Si todos los bindings son estáticos → chequeo **estático** (compilación)
- Binding dinámico → chequeo **dinámico** (runtime)
- TypeScript: chequeo estático encima de JavaScript → el runtime sigue siendo JS
- JavaScript/Python: solo dinámico por diseño

> *"If all bindings of variables to types are static in a language, then type checking can nearly always be done statically"* — Sebesta §6.13

---

### [F-47] Equivalencia nominal vs. estructural

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

### [F-48] Equivalencia — Tabla comparativa de lenguajes

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

> La equivalencia de tipos define cuándo el compilador **acepta** que un valor de un tipo sea usado donde se esperaba otro. Esa decisión afecta la flexibilidad, la seguridad semántica y la complejidad del compilador.

---

## BLOQUE 5 — Síntesis, Discusión y Cierre (30 min)

---

### [F-49] Mapa conceptual integrador

@tipo: diagrama
@imagen: content
@prompt-imagen: mapa conceptual jerárquico: nodo raíz superior "Tipos de Datos" con cinco ramas hacia abajo (Primitivos, Ordinales, Compuestos, Recursivos, Opcionales) cada una con sub-ramas; nodo raíz inferior "Sistemas de Tipos" con tres ramas (Equivalencia, Polimorfismo, Strong Typing); líneas punteadas conectando conceptos entre los dos árboles

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

### [F-50] Conexión con próximos temas

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

### [F-51] Consigna del TP

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

### [F-52] Cierre y bibliografía

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

### [F-53] Preguntas finales y espacio Q&A

@tipo: socratica

# Q&A — Preguntas finales

## Tres preguntas para reflexionar

> *¿Por qué TypeScript hace `strictNullChecks` opt-in mientras Kotlin lo tiene activado siempre?*
> Pista: retrocompatibilidad con JavaScript, adopción gradual, codebase existente

> *¿Cuándo usar uniones discriminadas (TypeScript) vs. sealed class (Kotlin) vs. herencia tradicional?*
> Pista: exhaustividad, extensibilidad (Expression Problem), overhead de objetos

> *¿Qué pierde TypeScript al tener tipado estructural en lugar de nominal?*
> Pista: `UserId` y `Email` como strings, `Celsius` y `Fahrenheit` como numbers — ¿qué pasa?

## Espacio abierto para preguntas de los alumnos

---
