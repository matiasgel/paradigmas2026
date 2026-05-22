# Filminas — Tema 10.1: Tipos de Datos y Sistemas de Tipos
**Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF
**Duración total:** 360 min | **Semana:** 11 | **Lenguaje principal:** TypeScript

---

## PORTADA

---

### [F-00] Portada

@tipo: portada
@imagen: background
@prompt-imagen: diagrama abstracto de un sistema de tipos — nodos con etiquetas Int, String, List<T>, Tree<A> conectados por flechas de subtipo y polimorfismo, estilo blueprint técnico sobre fondo oscuro

# Tipos de Datos y Sistemas de Tipos

Paradigmas y Lenguajes de Programación · Semana 11

> "Un tipo es una colección de valores homogéneos con un conjunto uniforme de operaciones." — Gabbrielli & Martini

---

## BLOQUE A — El tipo como contrato formal

---

### [F-01] El tipo como contrato formal

@tipo: concepto-abstracto
@imagen: content
@asset: kind=diagram position=right-half prompt="diagrama: caja 'Tipo Int' con dos listas: 'Valores: {-2^31 … 2^31-1}' y 'Operaciones: +, -, *, /, mod, <, >, =='"

# Tipo = conjunto de valores + operaciones válidas

## Definición (Gabbrielli §8.1)

- Un **tipo** es un par **(D, O)** donde:
  - **D** = dominio de valores admisibles
  - **O** = operaciones válidas sobre esos valores
- Sin tipo, el procesador opera sobre **patrones de bits sin semántica**
  - El tipo *da significado* a los bits

## Ejemplo concreto

```ts
// El tipo 'number' define qué valores existen y qué se puede hacer
const n: number = 42;      // valor en D
const r: number = n + 1;   // operación en O: + es válida
// const s: string = n;    // ERROR: la asignación fuera del dominio es inválida
```

- `number` en TypeScript: IEEE 754 double — D = ℝ (con límites de precisión), O = {+, -, *, /, %, **}
- `string`: D = secuencias Unicode, O = concatenación, slice, search — **NO** suma aritmética

---

### [F-02] Type safety y soundness

@tipo: concepto-abstracto

# ¿Cuándo un sistema de tipos es seguro?

## Type safety

- **Definición:** garantía de que **ninguna operación se aplica a un valor fuera de su dominio**
- Si el sistema dice que el programa es "bien tipado" → no ocurrirán errores de tipo en ejecución

## Soundness

| Lenguaje | ¿Sound? | Por qué |
|----------|---------|---------|
| Haskell | ✅ Sí | Sin casts inseguros; el compilador rechaza todo programa potencialmente inseguro |
| Kotlin (sin `!!`) | ✅ Sí | Null safety en el sistema de tipos |
| TypeScript (strict) | ⚠️ Parcial | Soundness deliberadamente sacrificada en algunos casos para usabilidad |
| C | ❌ No | Casts arbitrarios: `(float*) &intVar` — reinterpreta bits sin verificación |

## Implicación de diseño

- Un sistema **más restrictivo** detecta más errores en compilación — mayor seguridad, menor flexibilidad
- Un sistema **más permisivo** permite más programas — mayor flexibilidad, más errores en runtime
- TypeScript elige deliberadamente no ser fully sound: prioriza practicidad (Sebesta §6.1 — criterios de diseño)

---

### [F-03] Taxonomía de tipos

@tipo: diagrama
@imagen: content
@prompt-imagen: árbol jerárquico de clasificación de tipos: raíz 'Tipos', dos ramas: 'Primitivos' (con hijos: numéricos, boolean, char, enum) y 'Compuestos' (con hijos: producto: arrays/records/tuplas; suma: uniones; recursivos: listas/árboles); segunda dimensión horizontal: 'Monomórficos' vs 'Polimórficos'

# Clasificación de los tipos de datos

## Eje estructural (Gabbrielli §8.2)

- **Tipos primitivos:** unidades atómicas — `number`, `boolean`, `string`, `symbol`
- **Tipos compuestos:**
  - **Producto** (AND): combinan múltiples valores simultáneamente — `Array<T>`, `interface`, tuplas
  - **Suma** (OR): uno entre varios tipos posibles — uniones discriminadas
  - **Recursivos:** se definen en términos de sí mismos — listas, árboles

## Eje de polimorfismo (Gabbrielli §8.6)

- **Monomórficos:** una función — un tipo de dominio y codominio
- **Polimórficos:** una implementación — múltiples tipos posibles

## Hoja de ruta de la clase

> Esta taxonomía es el mapa de todo lo que cubre T10.1. Al finalizar, el alumno podrá ubicar cualquier tipo de TypeScript, C, Haskell o Kotlin en este árbol.

---

## BLOQUE B — Tipos primitivos y su representación interna

---

### [F-04] Enteros: representación en complemento a 2

@tipo: codigo

# ¿Por qué los enteros tienen un límite?

## Complemento a 2 (n bits)

- Rango: **[−2^(n−1), 2^(n−1)−1]**
- Para 32 bits: [−2.147.483.648, 2.147.483.647]
- Para 64 bits: [−9.223.372.036.854.775.808, 9.223.372.036.854.775.807]

## Tipos enteros en distintos lenguajes

| Tipo | Bits | Lenguaje |
|------|------|---------|
| `number` | 64 (IEEE 754) | TypeScript |
| `Int` | 32 | Kotlin |
| `Long` | 64 | Kotlin |
| `int` | 32 (típico) | C |
| `bigint` | ilimitado | TypeScript |

## El problema del overflow

```ts
// TypeScript: number es IEEE 754 double — enteros exactos solo hasta 2^53
const MAX_SAFE = Number.MAX_SAFE_INTEGER; // 9.007.199.254.740.991
console.log(MAX_SAFE + 1 === MAX_SAFE + 2); // true ← ¡overflow de precisión!

// Solución: BigInt para enteros arbitrarios
const big: bigint = 9007199254740993n;
console.log(big + 1n); // 9007199254740994n — correcto
```

```kotlin
// Kotlin: Int tiene overflow silencioso
val x: Int = Int.MAX_VALUE   // 2147483647
println(x + 1)               // -2147483648 ← overflow silencioso
```

> **Diferencia clave:** TypeScript no tiene tipo entero puro — `number` es siempre flotante. Para enteros grandes, `bigint` es obligatorio.

---

### [F-05] Punto flotante: IEEE 754

@tipo: codigo
@imagen: content
@asset: kind=diagram position=right-half prompt="diagrama del formato IEEE 754 de 64 bits: campo 'signo' (1 bit), 'exponente' (11 bits), 'mantisa' (52 bits), con etiquetas y colores diferenciados"

# El estándar que usa TypeScript

## Estructura IEEE 754 de 64 bits

- **Signo:** 1 bit
- **Exponente:** 11 bits (rango ~ 10^−308 a 10^308)
- **Mantisa:** 52 bits (~15 dígitos significativos)

## El problema de la precisión

```ts
console.log(0.1 + 0.2);             // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);     // false ← ¡sorpresa!

// Comparación correcta:
const EPSILON = Number.EPSILON;
console.log(Math.abs(0.1 + 0.2 - 0.3) < EPSILON); // true
```

## Valores especiales

```ts
console.log(1 / 0);          // Infinity
console.log(-1 / 0);         // -Infinity
console.log(0 / 0);          // NaN
console.log(NaN === NaN);    // false ← NaN no es igual a sí mismo
console.log(Number.isNaN(NaN)); // true ← forma correcta de verificar
```

## Cuándo usar otras opciones

- **Cálculos monetarios:** nunca `number` directamente — usar enteros en centavos o una biblioteca `Decimal`
- **JavaScript/TypeScript** no tiene `float` vs `double` — siempre es `number` (64 bits)

---

### [F-06] Boolean, Char y Unicode

@tipo: concepto-abstracto

# Tipos simples con implicaciones no triviales

## Boolean

- **Semántica:** exactamente dos valores: `true`, `false`
- **TypeScript:** `boolean` es un tipo primitivo real (no alias de número como en C)
- **C:** `_Bool` / `int` — 0 = false, ≠0 = true — **no hay type safety real**
- **Haskell:** `Bool = True | False` — tipo algebraico (ya lo veremos en Bloque D)

## Char y Unicode

```ts
// TypeScript: strings son UTF-16
const emoji: string = "😀";
console.log(emoji.length);         // 2 ← ¡dos code units, no un carácter!
console.log([...emoji].length);    // 1 ← correcto con spread iterator

// Code point vs code unit
const char = "A";
console.log(char.charCodeAt(0));   // 65 (code unit UTF-16)
console.log(char.codePointAt(0));  // 65 (code point Unicode — igual aquí)

const snowman = "☃";
console.log(snowman.charCodeAt(0));  // 9731 (BMP: 1 code unit)
console.log("𝄞".length);            // 2 (SMP: 2 code units, surrogate pair)
```

## Implicación de diseño

> En TypeScript `string.length` NO es la cantidad de caracteres visibles — es la cantidad de code units UTF-16. Para emojis y caracteres fuera del BMP, usar `[...str].length` o la API `Intl.Segmenter`.

---

### [F-07] String: inmutabilidad y diseño

@tipo: codigo

# Strings: decisión fundamental de diseño

## Inmutabilidad

```ts
// TypeScript/JavaScript: strings son inmutables
const s: string = "hola";
// s[0] = "H";  // silenciosamente ignorado en JS (no lanza error)
const s2: string = "H" + s.slice(1); // "Hola" — nueva instancia

// Implicación: s y s2 son objetos distintos en memoria
// Concatenación en loop → O(n²) copias → usar Array.join o template literals
```

```ts
// Comparación correcta
console.log("hola" === "hola"); // true — igualdad de contenido
console.log("A" < "B");         // true — orden lexicográfico

// Template literals (TypeScript)
const nombre = "Ada";
const msg: string = `Hola ${nombre}, bienvenida`; // interpolación type-safe
```

## Contraste

| Lenguaje | ¿Mutable? | Tipo |
|----------|-----------|------|
| TypeScript | ❌ Inmutable | primitivo |
| Java | ❌ Inmutable | objeto |
| C | ✅ Mutable | array de `char` |
| Kotlin | ❌ Inmutable | clase (con `StringBuilder` para mutación) |
| Python | ❌ Inmutable | secuencia |

> **Punto de reflexión:** la inmutabilidad evita aliases de strings — un diseño deliberado para seguridad. Pero afecta performance en manipulación intensiva.

---

### [F-08] Enumeraciones y tipos ordinales

@tipo: codigo

# Tipos con valores discretos ordenados

## Definición (Sebesta §6.4)

- **Tipo ordinal:** valores discretos con **orden total** y operaciones `pred`/`succ`
- Ventaja sobre constantes enteras: legibilidad + **type safety** + exhaustividad en switch

## Enumeraciones en TypeScript y comparación

```ts
// TypeScript enum — compila a un objeto JS
enum Direccion {
    Norte = "NORTE",
    Sur = "SUR",
    Este = "ESTE",
    Oeste = "OESTE"
}

function mover(dir: Direccion): void {
    console.log(`Moviendo hacia ${dir}`);
}

mover(Direccion.Norte);  // ✅ correcto
// mover("NORTE");        // ❌ Error de tipo en strict mode
```

```c
// C: enum — solo alias de int, sin type safety real
enum Dia { Lunes=1, Martes, Miercoles, ... };
enum Dia d = 42;  // ✅ C acepta esto — no hay verificación de rango
```

```kotlin
// Kotlin enum class — tipo cerrado con comportamiento
enum class Color(val hex: String) {
    ROJO("#FF0000"), VERDE("#00FF00"), AZUL("#0000FF");
    fun esPrimario() = this in listOf(ROJO, VERDE, AZUL)
}
```

```haskell
-- Haskell newtype — envoltura sin costo en runtime, type safety total
newtype Metros = Metros Double
newtype Kilos  = Kilos  Double
-- Metros y Kilos son tipos DISTINTOS — no intercambiables
```

> **Jerarquía de seguridad:** C enum (solo alias) < TypeScript enum (mejor) < Kotlin enum class (typed) < Haskell newtype (máxima seguridad)

---

## BLOQUE C — Tipos producto: arrays, registros y tuplas

---

### [F-09] Arrays: las 5 variantes de binding time

@tipo: tabla

# El array no es uno solo — son cinco tipos distintos

## Sebesta §6.5.2 — clasificación por cuándo se fija el tamaño

| Variante | ¿Cuándo se fija el tamaño? | ¿Dónde vive? | Ejemplo |
|----------|---------------------------|--------------|---------|
| **1. Estático** | Tiempo de compilación | Área estática | `static int a[10]` en C |
| **2. Stack-dynamic fijo** | Elaboración (entrada a función) | Stack | `int a[10]` local en C |
| **3. Stack-dynamic variable (VLA)** | Runtime (valor calculado) | Stack | `int a[n]` en C99 |
| **4. Heap-dynamic fijo** | Al crear (new/alloc) | Heap | `new int[n]` en Java/Kotlin |
| **5. Heap-dynamic variable** | Crece/achica en runtime | Heap | `ArrayList`, `MutableList` |

## En TypeScript

```ts
// TypeScript: solo variante 4 y 5 (siempre heap-dynamic)
const arr4: number[] = new Array(10);          // heap-dynamic fijo (lógicamente)
const arr5: number[] = [];                     // heap-dynamic variable
arr5.push(1); arr5.push(2);                   // crece en runtime

// TypeScript no tiene acceso a stack ni a arrays estáticos
// → C/Kotlin dan más control sobre binding time
```

> **Por qué importa:** la variante 1 y 2 son más rápidas (stack allocation, sin GC) pero menos flexibles. La variante 5 es la más común en TypeScript.

---

### [F-10] Arrays: multidimensionales, slices y asociativos

@tipo: codigo

# Más allá del array simple

## Multidimensionales: row-major vs. column-major

```ts
// TypeScript: arrays de arrays (row-major por convención JS)
const matriz: number[][] = [[1,2,3],[4,5,6],[7,8,9]];
// matriz[fila][columna] — row-major: fila completa es contigua en memoria

// Implicación de performance (cache locality):
// ✅ Recorrer por filas (row-major) → acceso secuencial
for (let i = 0; i < 3; i++)
    for (let j = 0; j < 3; j++)
        console.log(matriz[i][j]);  // fila primero → cache-friendly
```

## Slices: subarreglos con referencia compartida

```ts
// TypeScript: slice crea una COPIA (no referencia compartida como en Go)
const original: number[] = [1, 2, 3, 4, 5];
const slice: number[] = original.slice(1, 4); // [2, 3, 4] — nueva copia
original[1] = 99;
console.log(slice[0]); // 2 — no cambia (es copia)

// Contrast: en Go, slice ES una referencia al array subyacente
// → TypeScript es más seguro pero menos eficiente en memoria
```

## Arrays asociativos (Maps)

```ts
// TypeScript: Record<K,V> o Map<K,V>
const capitales: Record<string, string> = {
    argentina: "Buenos Aires",
    chile:     "Santiago"
};
capitales["uruguay"] = "Montevideo";  // O(1) amortizado (hash table)

// Map<K,V>: permite claves de cualquier tipo
const edades = new Map<string, number>();
edades.set("Ana", 30);
console.log(edades.get("Ana")); // 30
```

---

### [F-11] Records: alineamiento de memoria

@tipo: diagrama
@imagen: content
@asset: kind=diagram position=right-half prompt="diagrama de memoria de un struct C: {char c; int i} mostrando: byte 0=char, bytes 1-3=padding (gris), bytes 4-7=int; total 8 bytes en vez de 5"

# El compilador no siempre hace lo que parece

## C struct y el problema del padding

```c
// C: alineamiento de memoria
struct Ejemplo {
    char  c;   // 1 byte
    int   i;   // 4 bytes — pero requiere alineamiento a 4 bytes
};
// Tamaño real: 8 bytes (1 byte char + 3 bytes padding + 4 bytes int)

struct Mejor {
    int   i;   // 4 bytes
    char  c;   // 1 byte
    // 3 bytes padding al final
};
// Mismo tamaño: 8 bytes — pero diferente distribución

struct Empaquetado {
    int   i;   // 4 bytes
    char  a;   // 1 byte
    char  b;   // 1 byte
    char  c;   // 1 byte
    char  d;   // 1 byte
};
// Tamaño: 8 bytes — ¡sin padding! 4 chars llenan el espacio restante
```

## Producto cartesiano formal (Gabbrielli §8.3)

- Un record `Persona = { nombre: string × edad: Int × activo: Boolean }`
- Es el **tipo producto cartesiano** de sus campos: D_nombre × D_edad × D_activo
- Cada valor del tipo es una n-tupla de valores de los tipos componentes

---

### [F-12] TypeScript interfaces y objetos como records

@tipo: codigo

# El record en TypeScript — tipado estructural

## Interfaces: definir la forma

```ts
// TypeScript: interface define la "forma" del objeto
interface Persona {
    nombre: string;
    edad: number;
    activo: boolean;
}

// El objeto DEBE tener exactamente esos campos (y puede tener más)
function saludar(p: Persona): string {
    return `Hola ${p.nombre}, edad: ${p.edad}`;
}

const ana: Persona = { nombre: "Ana", edad: 30, activo: true };
saludar(ana); // ✅
```

## Type alias para records

```ts
// Type alias — equivalente a interface para objetos simples
type Punto = {
    x: number;
    y: number;
};

// Record inmutable (readonly)
type PuntoFijo = Readonly<{
    x: number;
    y: number;
}>;

const p: PuntoFijo = { x: 3, y: 4 };
// p.x = 5; // Error: no se puede asignar a propiedad readonly
```

## Desestructuración

```ts
// TypeScript: desestructuración con type checking
const { nombre, edad }: Persona = ana;
console.log(nombre); // "Ana"

// Equivalente a Kotlin data class .copy() — spread operator
const anaEdited: Persona = { ...ana, edad: 31 };
```

---

### [F-13] Tuplas como producto cartesiano formal

@tipo: codigo

# Producto cartesiano con campos posicionales

## Formalización (Gabbrielli §8.3)

- **Tupla** = tipo producto con campos **anónimos** y posicionales
- Tipo `T1 × T2 × … × Tn` — el componente `i` es de tipo `Ti`
- Un valor de la tupla ES una n-tupla: `(v1: T1, v2: T2, …, vn: Tn)`

## Tuplas en TypeScript

```ts
// TypeScript: tuple types — tipos posicionales fijos
type Par = [string, number];
type RGB = [number, number, number];
type Resultado = [boolean, string | null]; // éxito + mensaje

const punto: Par = ["Ana", 30];    // ✅
// const mal: Par = [30, "Ana"];   // ❌ tipo incorrecto

// Desestructuración posicional
const [nombre, edad] = punto;
console.log(nombre); // "Ana" — tipo inferido: string

// Named tuples (TypeScript 4.0+) — legibilidad
type Coordenada = [x: number, y: number, z: number];
const pos: Coordenada = [1, 2, 3];
```

## Contraste con Haskell

```haskell
-- Haskell: tupla como tipo base del lenguaje
type Par = (String, Int)
let punto = ("Ana", 30) :: Par

-- Currying: función de 2 argumentos vs. función de tupla
sumar :: Int -> Int -> Int       -- currificada (estándar)
sumarTupla :: (Int, Int) -> Int  -- función de tupla
```

## Cuándo usar tupla vs. record

| Situación | Usar |
|-----------|------|
| Múltiples valores anónimos temporales | Tupla |
| Datos con semántica nombrada | Record/Interface |
| Retorno de función con 2-3 valores | Tupla |
| Modelo de dominio | Interface/Class |

---

## BLOQUE D — Tipos suma: uniones y tipos recursivos

---

### [F-14] Uniones libres en C: el problema de type safety

@tipo: codigo

# Cuando el tipo es inseguro por diseño

## C union — compartir memoria sin tipo

```c
// C: union — todos los campos comparten la misma memoria
union Dato {
    int   i;      // 4 bytes
    float f;      // 4 bytes
    char  c[4];   // 4 bytes
};
// Tamaño del union = max(4, 4, 4) = 4 bytes

union Dato d;
d.i = 65;             // escribimos un int
printf("%f\n", d.f);  // leemos como float — COMPORTAMIENTO INDEFINIDO
printf("%c\n", d.c[0]); // leemos como char — puede dar 'A' o basura
```

## El problema: no hay marca del campo activo

- El compilador no rastreo *qué campo fue escrito último*
- Leer el campo incorrecto → **comportamiento indefinido** (undefined behavior en C)
- El programador es el único responsable de la coherencia

## Uso legítimo

- **Serialización de bajo nivel:** interpretar los mismos bytes como int o como byte array
- **Optimizaciones SIMD:** operar sobre registros de 128 bits de múltiples maneras
- **Nunca** como estructura de datos de alto nivel sin un discriminador externo

> **Conclusión:** La unión de C es un ejemplo de tipo **inseguro** — sacrifica seguridad por eficiencia de memoria. El tipo suma *seguro* resuelve esto.

---

### [F-15] Tipo suma: uniones discriminadas

@tipo: codigo

# La solución al problema de las uniones libres

## Tipo suma formal (Gabbrielli §8.3)

- **Tipo suma** `T1 + T2 + … + Tn` (también: *disjoint union*, *tagged union*, *sum type*)
- Un valor es **o bien** un T1, **o bien** un T2, … nunca dos al mismo tiempo
- Incluye una **etiqueta discriminadora** que identifica el tipo activo
- Contraste con tipo producto `T1 × T2`: combina todos los tipos **simultáneamente**

## TypeScript discriminated unions — el idioma nativo

```ts
// TypeScript: cada variante tiene un campo literal discriminador
type Forma =
    | { kind: "circulo";     radio: number }
    | { kind: "rectangulo";  ancho: number; alto: number }
    | { kind: "triangulo";   base: number;  altura: number };

function area(f: Forma): number {
    switch (f.kind) {  // TypeScript verifica exhaustividad
        case "circulo":     return Math.PI * f.radio ** 2;
        case "rectangulo":  return f.ancho * f.alto;
        case "triangulo":   return (f.base * f.altura) / 2;
        // Si olvidamos un case, TypeScript NO nos avisa aquí...
        // → ver F-16 para exhaustive check con never
    }
}
```

## Comparación con C tagged union

```c
// C: "unión discriminada manual" — el programador agrega el tag
typedef struct {
    enum { INT_VAL, FLOAT_VAL } tag;  // discriminador
    union { int i; float f; } valor;
} Dato;
// Correcto pero verboso y sin verificación automática de exhaustividad
```

---

### [F-16] Haskell ADT y Kotlin sealed classes

@tipo: codigo

# Tipos suma en lenguajes de paradigma mixto

## Haskell: Algebraic Data Types (ADT)

```haskell
-- Haskell: tipo suma algebraico con pattern matching
data Forma = Circulo Double
           | Rectangulo Double Double
           | Triangulo Double Double

area :: Forma -> Double
area (Circulo r)        = pi * r * r
area (Rectangulo a b)   = a * b
area (Triangulo b h)    = b * h / 2
-- El compilador VERIFICA exhaustividad — si falta un caso, warning/error
```

## Kotlin sealed classes

```kotlin
// Kotlin: sealed class = tipo suma con herencia controlada
sealed class Forma {
    data class Circulo(val radio: Double) : Forma()
    data class Rectangulo(val ancho: Double, val alto: Double) : Forma()
    data class Triangulo(val base: Double, val altura: Double) : Forma()
}

fun area(f: Forma): Double = when (f) {
    is Forma.Circulo     -> Math.PI * f.radio * f.radio
    is Forma.Rectangulo  -> f.ancho * f.alto
    is Forma.Triangulo   -> f.base * f.altura / 2
    // El compilador OBLIGA a cubrir todos los subtipos — exhaustividad garantizada
}
```

## TypeScript: exhaustive check con never

```ts
// Técnica para garantizar exhaustividad en TypeScript
function area(f: Forma): number {
    switch (f.kind) {
        case "circulo":     return Math.PI * f.radio ** 2;
        case "rectangulo":  return f.ancho * f.alto;
        case "triangulo":   return (f.base * f.altura) / 2;
        default:
            const _exhaustivo: never = f; // Error de tipo si hay casos no cubiertos
            throw new Error(`Tipo no manejado: ${_exhaustivo}`);
    }
}
```

---

### [F-17] Tipos recursivos: listas y árboles

@tipo: codigo
@imagen: content
@asset: kind=diagram position=right-half prompt="árbol binario visual con nodos etiquetados: Nodo(1, Nodo(2, Hoja(4), Hoja(5)), Nodo(3, Hoja(6), Hoja(7))); cada nodo con flecha izquierda y derecha"

# Tipos que se definen en términos de sí mismos

## Definición formal (Gabbrielli §8.4)

- Un tipo **recursivo** aparece en su propia definición
- Requiere **indirección** (puntero/referencia) — sin ella el tipo tendría tamaño infinito

## Lista enlazada (definición inductiva)

```
Lista(A) = Vacía | Nodo(A, Lista(A))
```

```ts
// TypeScript: tipo recursivo con interfaz
type Lista<A> =
    | { tipo: "vacia" }
    | { tipo: "nodo"; valor: A; siguiente: Lista<A> };

// Instancia
const lista: Lista<number> = {
    tipo: "nodo", valor: 1,
    siguiente: { tipo: "nodo", valor: 2,
        siguiente: { tipo: "vacia" } }
};
```

## Árbol binario

```ts
// TypeScript
type Arbol<A> =
    | { tipo: "hoja"; valor: A }
    | { tipo: "nodo"; izq: Arbol<A>; valor: A; der: Arbol<A> };

function altura<A>(a: Arbol<A>): number {
    if (a.tipo === "hoja") return 0;
    return 1 + Math.max(altura(a.izq), altura(a.der));
}
```

```haskell
-- Haskell: tipo recursivo nativo
data Arbol a = Hoja a | Nodo (Arbol a) a (Arbol a)

altura :: Arbol a -> Int
altura (Hoja _)     = 0
altura (Nodo i _ d) = 1 + max (altura i) (altura d)
```

> **Conexión con plan mínimo:** listas y árboles (Módulo VII) son instancias directas del concepto de tipo recursivo. No son "estructuras de datos arbitrarias" — tienen una base formal en teoría de tipos.

---

### [F-18] Checkpoint — Bloques A-D

@tipo: socratica

# Pausa activa: consolidación de tipos primitivos y compuestos

## ¿Qué acabamos de ver?

| Bloque | Concepto clave | TypeScript |
|--------|---------------|-----------|
| A | Tipo = (D, O) — contrato formal | type annotations |
| B | Representación interna de primitivos | `number`, `bigint`, `string`, `boolean` |
| C — Producto | Arrays (5 variantes), records, tuplas | `interface`, `[]`, `[T1, T2]` |
| D — Suma | Uniones discriminadas, tipos recursivos | `type A \| B`, `never` exhaustivo |

## Pregunta de comprensión

> **¿Cuál es la diferencia fundamental entre tipo producto y tipo suma?**

- Tipo producto `T1 × T2`: un valor tiene **ambos** — un T1 Y un T2
- Tipo suma `T1 + T2`: un valor tiene **uno** — un T1 O un T2

## Actividad rápida (5 min)

Dado este tipo TypeScript:
```ts
type Resultado<T> =
    | { ok: true;  valor: T }
    | { ok: false; error: string };
```
Preguntas:
1. ¿Es tipo suma o tipo producto? ¿Por qué?
2. ¿Qué tipo recursivo podría usarse para implementar una lista de Resultado?
3. ¿Cómo se garantiza exhaustividad al procesar con `switch`?

---

## BLOQUE E — Punteros, referencias y null safety

---

### [F-19] El tipo puntero en C

@tipo: codigo
@imagen: content
@asset: kind=diagram position=right-half prompt="diagrama de memoria: variable 'p' contiene dirección 0x1234, flecha apunta a celda de memoria 0x1234 que contiene el valor 42; segunda parte muestra 'dangling pointer': p apunta a celda marcada como 'liberada/inválida'"

# El tipo más peligroso del zoo

## Operaciones fundamentales (Sebesta §6.11.2)

```c
int x = 42;
int *p = &x;    // & = address-of: obtiene la dirección de x
printf("%d\n", *p);  // * = dereference: lee el valor apuntado → 42
*p = 99;             // escritura vía puntero: x ahora es 99

// Aritmética de punteros
int arr[5] = {10, 20, 30, 40, 50};
int *q = arr;        // q apunta al primer elemento
printf("%d\n", *(q + 2)); // 30 — q+2 avanza sizeof(int)*2 = 8 bytes
```

## Dangling pointer (Sebesta §6.11.3.1)

```c
// Causa 1: free sin anular el puntero
int *p = malloc(sizeof(int));
*p = 42;
free(p);
// p todavía contiene la dirección — ya no es válida
*p = 99;  // COMPORTAMIENTO INDEFINIDO — puede corromper el heap

// Causa 2: retornar dirección de variable local
int* crear() {
    int local = 5;
    return &local;  // ERROR: local se destruye al retornar
}                   // el puntero retornado apunta a stack ya reusado
```

---

### [F-20] Memory leak y referencias vs. punteros

@tipo: tabla

# Dos problemas opuestos del tipo puntero

## Lost heap-dynamic variable / Memory leak (Sebesta §6.11.3.2)

```c
// El heap crece sin que el OS lo pueda recuperar
int *p = malloc(100 * sizeof(int)); // celda heap creada
p = malloc(200 * sizeof(int));      // ← p ahora apunta a OTRA celda
// La primera celda de 100 ints ya no tiene puntero que la referencie
// → NUNCA se puede liberar → memory leak
```

## Referencias vs. punteros (Sebesta §6.11.4)

| Característica | Puntero (C) | Referencia (TypeScript/Java/Kotlin) |
|----------------|-------------|-------------------------------------|
| Aritmética | ✅ `p + 1`, `p - 1` | ❌ No permitida |
| Puede ser null | ✅ `int *p = NULL` | Depende del lenguaje |
| Acceso a dirección | ✅ `printf("%p", p)` | ❌ No accesible |
| Memory management | Manual (`malloc`/`free`) | GC automático |
| Dangling pointer | ✅ Posible | ❌ Imposible (GC mantiene referencias) |
| Aritmética de bytes | ✅ `(char*)p + 3` | ❌ Imposible |

> **TypeScript:** todas las variables de tipo objeto son referencias — sin punteros, sin aritmética de memoria. El precio: menos control, pero mucho más seguro.

---

### [F-21] Null safety: el problema de los mil millones

@tipo: concepto-abstracto

# El "billion-dollar mistake" de Tony Hoare

## El problema (1965 — Algol W)

> *"I call it my billion-dollar mistake. It was the invention of the null reference in 1965."* — Tony Hoare

- La referencia nula permite que **cualquier** variable de tipo objeto pueda no existir
- Resultado: en Java/C# legacy, **NullPointerException** es la excepción #1 en producción
- En TypeScript sin strict: `undefined` y `null` pueden aparecer en cualquier tipo

## Null safety en Kotlin (Sebesta §6.11.5 / Kotlin docs)

```kotlin
// Kotlin resuelve esto en el SISTEMA DE TIPOS
val s1: String  = "hola"  // NUNCA null — el compilador lo garantiza
val s2: String? = null    // PUEDE ser null — requiere verificación explícita

// s1.length  → ✅ siempre seguro
// s2.length  → ❌ Error de compilación: s2 puede ser null
s2?.length    → ✅ null-safe: retorna null si s2 es null
s2?.length ?: 0  → ✅ Elvis: valor por defecto si null
```

> **Por qué usamos Kotlin aquí:** el manejo de `null | undefined` en TypeScript fue cubierto extensivamente en T09.2 (F-29 a F-33). Kotlin muestra la *solución a nivel de sistema de tipos* de forma más limpia.

---

### [F-22] Null safety: operadores Kotlin

@tipo: codigo

# Cuatro operadores para vivir sin NullPointerException

```kotlin
data class Persona(val nombre: String, val direccion: Direccion?)
data class Direccion(val ciudad: String, val codigoPostal: String?)

val persona: Persona? = obtenerPersona()

// 1. Safe call (?.) — retorna null si cualquier eslabón es null
val ciudad: String? = persona?.direccion?.ciudad

// 2. Elvis operator (?:) — valor por defecto si null
val ciudadODefault: String = persona?.direccion?.ciudad ?: "Desconocida"

// 3. Non-null assertion (!!) — lanza KotlinNullPointerException si null
//    → usar SOLO cuando se tiene certeza absoluta de non-null
val ciudadForzada: String = persona!!.direccion!!.ciudad  // peligroso

// 4. let { } — ejecuta bloque solo si no es null
persona?.let { p ->
    println("Persona encontrada: ${p.nombre}")
    p.direccion?.let { d ->
        println("Ciudad: ${d.ciudad}")
    }
}
```

## Comparación con TypeScript (T09.2)

| TypeScript | Kotlin | Significado |
|-----------|--------|-------------|
| `T \| null \| undefined` | `T?` | tipo nullable |
| `?.` (optional chaining) | `?.` | safe call |
| `?? "default"` | `?: "default"` | null coalescing / Elvis |
| Covered in T09.2 | Covered in T10.1 | — |

---

## BLOQUE F — Equivalencia, coerción y conversión de tipos

---

### [F-23] Equivalencia de nombres

@tipo: codigo

# ¿Cuándo dos tipos son "el mismo"?

## Name equivalence (Sebesta §6.12.1)

- Dos tipos son equivalentes **solo si tienen el mismo nombre** en el mismo scope
- Cada declaración de tipo crea un tipo **distinto**, aunque tenga la misma estructura

```ts
// TypeScript con 'class' o 'unique symbol' puede simular name equivalence
// Pero TypeScript es PRINCIPALMENTE estructural — ver F-24

// Kotlin: name equivalence para tipos de referencia
data class Metros(val valor: Double)
data class Kilos(val valor: Double)

fun calcular(m: Metros): Double = m.valor * 9.8
// calcular(Kilos(70.0))  // ❌ Error de tipo — Kilos no es Metros
// aunque ambos tengan la misma estructura (Double envuelto)
```

```pascal
(* Pascal: name equivalence estricta *)
TYPE
    TipoA = RECORD x: Integer; y: Integer END;
    TipoB = RECORD x: Integer; y: Integer END;

VAR a: TipoA;
    b: TipoB;
(* a := b;  ← ERROR en Pascal — son tipos distintos aunque idénticos *)
```

## Ventaja del name equivalence

- **Mayor seguridad:** `Metros` y `Kilos` son tipos distintos — no se pueden mezclar accidentalmente
- **Mejor abstracción:** cada tipo es una unidad independiente del sistema
- Usado en: Java (clases), Kotlin (clases), Ada, Pascal

---

### [F-24] Equivalencia estructural — TypeScript

@tipo: codigo

# TypeScript y el sistema de tipos estructural

## Structural equivalence (Sebesta §6.12.2)

- Dos tipos son equivalentes si tienen **la misma estructura** — mismos campos, mismo orden, mismos tipos
- El nombre del tipo es **irrelevante** para la compatibilidad

```ts
// TypeScript es ESTRUCTURALMENTE tipado — el ejemplo canónico
interface Punto2D {
    x: number;
    y: number;
}

// Una función que espera Punto2D...
function distancia(p: Punto2D): number {
    return Math.sqrt(p.x ** 2 + p.y ** 2);
}

// ...acepta cualquier objeto con la forma correcta, sin importar su nombre
const p1 = { x: 3, y: 4 };                     // anónimo — ✅
const p2: { x: number; y: number } = { x: 1, y: 1 }; // ✅
distancia(p1);  // ✅ — tiene x: number y y: number
distancia(p2);  // ✅

// Incluso con campos adicionales (subtype compatibility)
const p3 = { x: 5, y: 12, etiqueta: "origen" };
distancia(p3);  // ✅ — tiene lo requerido + extra (compatible)
```

## Comparación

| Sistema | Ejemplo | Característica |
|---------|---------|----------------|
| TypeScript | `interface` | Estructural puro |
| OCaml | `{x: int; y: int}` | Estructural |
| Haskell | records | Nominal para `data`, estructural para typeclasses |
| Java | clases | Nominal — `implements` explícito requerido |
| Go | interfaces | Estructural para interfaces |

---

### [F-25] Name vs. structural — comparación y tradeoffs

@tipo: tabla

# Dos filosofías de compatibilidad de tipos

## La pregunta clave

> Si `A` y `B` tienen exactamente los mismos campos con los mismos tipos, ¿son compatibles?

| Sistema | ¿Compatibles? | Ejemplo |
|---------|---------------|---------|
| **Estructural** (TypeScript, Go) | ✅ Sí | Objeto `{x, y}` compatible con cualquier interfaz que pida `{x, y}` |
| **Nominal** (Java, Kotlin, C++) | ❌ No (por defecto) | `class A {x: int}` y `class B {x: int}` — tipos distintos |

## Tradeoffs

| Criterio | Name Equivalence | Structural Equivalence |
|----------|-----------------|----------------------|
| Seguridad | ✅ Mayor — tipos semánticamente distintos no se mezclan | ⚠️ Menor — tipos accidentalmente iguales son compatibles |
| Flexibilidad | ⚠️ Menor — requiere `implements` o cast explícito | ✅ Mayor — composición sin herencia formal |
| Refactoring | Fácil — renombrar tipo cambia todo | Difícil — cambiar estructura rompe compatibilidades ocultas |
| Duck typing | Compatible con nominal en runtime | Base teórica de duck typing |

## TypeScript: subtle structural edge case

```ts
// Dos interfaces "accidentalmente" iguales — ¿bug o feature?
interface Metros { valor: number; }
interface Kilos  { valor: number; }

function calcularFuerza(m: Metros): number { return m.valor * 9.8; }

const peso: Kilos = { valor: 70 };
calcularFuerza(peso);  // ✅ TypeScript acepta esto — misma estructura
// En Kotlin: ❌ Error — Metros y Kilos son tipos distintos
```

> **Lección:** TypeScript sacrifica name safety por flexibilidad compositiva. Para sistemas críticos con unidades de medida, usar branded types o Kotlin.

---

### [F-26] Coerción, conversión y mixed mode

@tipo: codigo

# Cómo los lenguajes manejan el cambio de tipo

## Coerción implícita (Sebesta §6.13)

```ts
// TypeScript/JavaScript: widening implícito en algunos contextos
const n: number = 42;
const s: string = "El número es: " + n; // coerción implícita: number → string
console.log(typeof s); // "string"

// Pero TypeScript NO hace numeric widening automático entre tipos:
// const x: number = 42;
// const y: bigint = x;  // ❌ Error — requiere conversión explícita
```

```c
// C: widening automático (numeric promotion)
int    i = 5;
double d = i + 3.14;  // i se convierte automáticamente a double
// Narrowing silencioso:
int truncado = 3.9;   // 3 — sin advertencia en C básico
```

## Conversión explícita

```ts
// TypeScript: conversiones explícitas
const n = 42;
const s = String(n);       // number → string: "42"
const n2 = Number("42");   // string → number: 42
const n3 = parseInt("42px", 10); // "42px" → 42 (parseo parcial)
const n4 = Number("42px"); // NaN — falla silenciosamente

// Kotlin: conversiones siempre explícitas (diseño intencional)
// val x: Long = 42        // ❌ Error en Kotlin — requiere:
// val x: Long = 42.toLong()  ✅
```

## Mixed mode arithmetic — el bug clásico

```ts
// JavaScript/TypeScript: ¡+ es concatenación con strings!
console.log(1 + 2);     // 3 (número + número)
console.log("1" + 2);   // "12" (string + número → concatenación)
console.log(1 + "2");   // "12" (número + string → concatenación)
// → TypeScript strict detecta esto en contextos tipados
```

```c
// C: división entera — el bug clásico de precisión
int resultado = 5 / 2;   // 2, no 2.5 — truncamiento entero
double bien = 5.0 / 2;   // 2.5 — widening implícito al primer operando
```

---

## BLOQUE G — Polimorfismo y sistemas paramétricos

---

### [F-27] Sistemas monomórficos vs. polimórficos

@tipo: concepto-abstracto

# La pregunta: ¿una función para un tipo o para muchos?

## Sistema monomórfico (Gabbrielli §8.6)

```ts
// Una función tiene exactamente un tipo de dominio y codominio
function sumarEnteros(a: number, b: number): number {
    return a + b;
}
// Solo funciona para number — no sirve para bigint, string, etc.
```

```c
// C sin templates: monomórfico por defecto
// Para "generalizar", se usa void* → se pierde type safety
void* min_unsafe(void *a, void *b, int size);  // no-type-safe
```

## Sistema polimórfico — una implementación, muchos tipos

```ts
// Una función que funciona para cualquier tipo T
function identidad<T>(x: T): T {
    return x;
}

identidad<number>(42);     // T = number
identidad<string>("hola"); // T = string
identidad<boolean>(true);  // T = boolean
// Una SOLA implementación — cero código duplicado
```

## Taxonomía del polimorfismo (Gabbrielli §8.6)

```
Polimorfismo
├── Universal
│   ├── Paramétrico (generics, templates) ← F-29, F-30
│   └── Inclusión / Subtipo (herencia)    ← F-32
└── Ad-hoc
    ├── Sobrecarga (overloading)           ← F-28
    └── Coerción (conversión implícita)   ← F-26
```

---

### [F-28] Polimorfismo ad-hoc: sobrecarga

@tipo: codigo

# Mismo nombre, distintos tipos — dispatch en compilación

## Sobrecarga (Sebesta §11.2)

```ts
// TypeScript: sobrecarga con firmas múltiples
function formatear(x: number): string;
function formatear(x: string): string;
function formatear(x: boolean): string;
function formatear(x: number | string | boolean): string {
    if (typeof x === "number")  return x.toFixed(2);
    if (typeof x === "string")  return x.toUpperCase();
    return x ? "SÍ" : "NO";
}

formatear(3.14);     // "3.14"
formatear("hola");   // "HOLA"
formatear(true);     // "SÍ"
```

## Dispatch estático (en compilación)

```kotlin
// Kotlin: sobrecarga resuelta en tiempo de compilación
fun area(c: Circulo): Double    = Math.PI * c.radio * c.radio
fun area(r: Rectangulo): Double = r.ancho * r.alto
// El compilador decide qué función llamar según el tipo del argumento
// → costo cero en runtime
```

## Dispatch dinámico (en ejecución — polimorfismo por subtipo)

```kotlin
// Kotlin: virtual dispatch
open class Animal {
    open fun hablar(): String = "..."
}
class Perro : Animal() {
    override fun hablar(): String = "Guau"
}
class Gato : Animal() {
    override fun hablar(): String = "Miau"
}

val animales: List<Animal> = listOf(Perro(), Gato())
animales.forEach { println(it.hablar()) }
// Decisión de qué hablar() llamar → en runtime según el tipo real
```

> **Límite del ad-hoc:** hay que enumerar manualmente todos los tipos. Para una función realmente genérica, se necesita polimorfismo paramétrico.

---

### [F-29] Polimorfismo paramétrico: generics

@tipo: codigo

# Una implementación — todos los tipos

## Concepto (Sebesta §11.3, Gabbrielli §8.6)

```ts
// TypeScript: función genérica con type parameter T
function primero<T>(lista: T[]): T | undefined {
    return lista.length > 0 ? lista[0] : undefined;
}

primero([1, 2, 3]);        // T = number → retorna 1
primero(["a", "b"]);       // T = string → retorna "a"
primero<boolean>([true]);  // T = boolean → retorna true
```

## Tipos genéricos

```ts
// TypeScript: tipo genérico — List<T>, Maybe<T>, etc.
type Maybe<T> =
    | { tipo: "nada" }
    | { tipo: "justo"; valor: T };

function mapMaybe<A, B>(m: Maybe<A>, f: (x: A) => B): Maybe<B> {
    if (m.tipo === "nada") return { tipo: "nada" };
    return { tipo: "justo", valor: f(m.valor) };
}

const n: Maybe<number> = { tipo: "justo", valor: 42 };
const s: Maybe<string> = mapMaybe(n, x => x.toString()); // Maybe<string>
```

## Haskell: el sistema paramétrico más expresivo

```haskell
-- Haskell: una función polimórfica pura
identidad :: a -> a
identidad x = x  -- funciona para CUALQUIER tipo 'a'

-- Maybe como tipo genérico canónico
data Maybe a = Nothing | Just a

fmap :: (a -> b) -> Maybe a -> Maybe b
fmap _ Nothing  = Nothing
fmap f (Just x) = Just (f x)
```

---

### [F-30] Generics con constraints (bounded quantification)

@tipo: codigo

# No todos los tipos son iguales — constraints de tipo

## El problema: no toda T tiene todo

```ts
// ¿Por qué esto no compila?
function max<T>(a: T, b: T): T {
    return a > b ? a : b;  // ❌ Error: el operador '>' no existe para T genérico
}
// TypeScript no sabe si T tiene el operador de comparación
```

## Solución: bounded quantification

```ts
// TypeScript: extends como constraint
function max<T extends { valueOf(): number }>(a: T, b: T): T {
    return a.valueOf() > b.valueOf() ? a : b;
}

// Más idiomático: definir un tipo con comparación
interface Comparable {
    compareTo(other: this): number;
}

function maxComparable<T extends Comparable>(a: T, b: T): T {
    return a.compareTo(b) >= 0 ? a : b;
}
```

## Kotlin: upper bounds y where clauses

```kotlin
// Kotlin: upper bound simple
fun <T : Comparable<T>> max(a: T, b: T): T = if (a >= b) a else b

max(3, 5)           // T = Int → 5
max("Ana", "Bruno") // T = String → "Bruno"

// Múltiples constraints con 'where'
fun <T> clonarYComparar(a: T, b: T): Boolean
    where T : Cloneable, T : Comparable<T> {
    return a.compareTo(b) == 0
}
```

## Haskell: typeclasses como constraints

```haskell
-- Haskell: Ord a => T debe implementar la typeclass Ord
max' :: Ord a => a -> a -> a
max' x y = if x >= y then x else y

-- Múltiples constraints
showAndCompare :: (Show a, Ord a) => a -> a -> String
showAndCompare x y = show x ++ " vs " ++ show y
```

> **Gabbrielli §8.6:** bounded quantification = polimorfismo paramétrico **con restricción** — más poderoso que sobrecarga (genérico) pero más controlado que polimorfismo universal puro.

---

### [F-31] Polimorfismo por subtipo y el principio de Liskov

@tipo: concepto-abstracto
@imagen: content
@asset: kind=diagram position=right-half prompt="diagrama de jerarquía: Animal en la cima, flechas descendentes a Mamifero y Ave, flechas descendentes a Perro/Gato desde Mamifero y Aguila/Pinguino desde Ave; flecha LSP mostrando que Perro puede usarse donde se espera Animal"

# Cuando el tipo de una subclase puede reemplazar a su supertipo

## Principio de sustitución de Liskov (LSP)

> *"Si S es un subtipo de T, entonces cualquier programa que use objetos de tipo T puede ser sustituido por objetos de tipo S sin alterar las propiedades correctas del programa."* — Barbara Liskov, 1987

```ts
// TypeScript: clase base + subclases
class Animal {
    hablar(): string { return "..."; }
}
class Perro extends Animal {
    override hablar(): string { return "Guau"; }
}
class Gato extends Animal {
    override hablar(): string { return "Miau"; }
}

// Función que usa Animal — acepta cualquier subtipo (LSP)
function hacerHablar(a: Animal): void {
    console.log(a.hablar());
}

hacerHablar(new Perro()); // "Guau" — Perro <: Animal
hacerHablar(new Gato()); // "Miau" — Gato <: Animal
```

## Relación con el sistema de tipos

- **TypeScript** implementa subtipado estructural: `Perro` es subtipo de `Animal` si tiene todos sus métodos con tipos compatibles
- **Kotlin/Java** implementa subtipado nominal: `Perro` debe declarar `extends Animal`
- En ambos casos, el **dispatch es dinámico** — la decisión de qué método llamar es en runtime

---

### [F-32] Varianza: covarianza y contravarianza

@tipo: tabla
@imagen: content
@asset: kind=diagram position=right-half prompt="diagrama de varianza: Perro <: Animal en la cima; debajo, tres líneas: covarianza: Array<Perro> <: Array<Animal> (con flecha verde); contravarianza: Consumer<Animal> <: Consumer<Perro> (con flecha azul invertida); invarianza: MutableArray<Perro> NO <: MutableArray<Animal> (con X roja)"

# ¿Cómo se propaga el subtipado a través de tipos genéricos?

## La pregunta de la varianza

> Si `Perro <: Animal`, ¿es `Lista<Perro> <: Lista<Animal>`?

## Covarianza: `out T` — solo lectura

```ts
// TypeScript: arrays son covariantes (solo lectura segura)
const perros: Perro[] = [new Perro()];
const animales: Animal[] = perros;  // ✅ TypeScript permite esto
animales.push(new Gato());         // ⚠️ Peligro: modifica el array original
// → TypeScript sacrifica soundness aquí por conveniencia

// Kotlin: covarianza explícita con 'out'
// fun <out T> leer(lista: Lista<T>): T  ← solo puede producir T
```

## Contravarianza: `in T` — solo escritura

```ts
// Si algo consume Animal, puede consumir Perro también
// Consumer<Animal> <: Consumer<Perro>
type Consumidor<T> = (x: T) => void;

const consumirAnimal: Consumidor<Animal> = (a) => console.log(a.hablar());
const consumirPerro: Consumidor<Perro>   = consumirAnimal; // ✅ contravarianza
```

```kotlin
// Kotlin: contravarianza con 'in'
interface Comparable<in T> {
    fun compareTo(other: T): Int
}
// Comparable<Animal> puede usarse donde se espera Comparable<Perro>
```

## Invarianza: sin subtipado

| Caso | TypeScript | Kotlin | Razón |
|------|-----------|--------|-------|
| Array<Perro> → Array<Animal> | ✅ (unsound) | ❌ `MutableList` | Si mutable, puede insertar Cat |
| ReadonlyArray<Perro> → ReadonlyArray<Animal> | ✅ (sound) | ✅ `List<out T>` | Solo lectura — seguro |
| (Animal) => void → (Perro) => void | ✅ contravariante | ✅ `in` | Consume — funciona para más |

---

### [F-33] Inferencia de tipos: Hindley-Milner

@tipo: codigo

# El compilador puede deducir los tipos — sin magia

## El problema

```ts
// ¿Qué tipo tiene 'resultado'?
const resultado = [1, 2, 3].map(x => x * 2).filter(x => x > 4);
// TypeScript infiere: number[] — sin que escribamos una sola anotación
```

## Hindley-Milner (HM) — Louden §8.6, Gabbrielli §8.9

- **Inventado** por Hindley (1969) y Milner (1978) para ML
- **Algoritmo W:** resuelve el sistema de ecuaciones de tipos de un programa
- **Garantía:** infiere el tipo **más general** (principal) de cada expresión
- Haskell usa HM extendido — la mayoría del código no necesita anotaciones

```haskell
-- Haskell: sin ninguna anotación, el compilador infiere
identidad x = x           -- inferido: a -> a (tipo más general)
sumar x y   = x + y       -- inferido: Num a => a -> a -> a
lista       = [1, 2, 3]   -- inferido: Num a => [a]
```

## TypeScript: inferencia limitada

```ts
// TypeScript infiere tipos locales (no HM completo)
const x = 42;               // inferido: number
const lista = [1, "a", true]; // inferido: (number | string | boolean)[]
const doble = (n: number) => n * 2; // inferido: (n: number) => number

// LIMITACIÓN: requiere anotaciones en firmas de funciones públicas
// function identidad(x) { return x; }  // ❌ implicitly has 'any' type
function identidad<T>(x: T): T { return x; } // ✅ explícito — mejor para APIs
```

> **Diferencia clave:** Haskell puede inferir tipos de funciones públicas completas. TypeScript requiere anotaciones en interfaces públicas — decisión de diseño para legibilidad de APIs (no limitación del algoritmo).

---

### [F-34] Cierre — Síntesis y conexiones curriculares

@tipo: cierre

# Lo que construimos hoy

## Mapa completo del tema

| Bloque | Concepto | TypeScript | Contraste |
|--------|---------|-----------|---------|
| A | Tipo = (D, O), type safety, soundness | type annotations | C vs Haskell |
| B | Primitivos: int, float, bool, char, enum | `number`, `bigint`, `string`, `boolean`, `enum` | IEEE 754, Unicode |
| C | Tipos producto: arrays (5 var.), records, tuplas | `interface`, `[]`, `[T1,T2]` | C struct + padding |
| D | Tipos suma: discriminated unions, recursivos | `type A\|B`, `never`, recursive types | Haskell ADT, Kotlin sealed |
| E | Punteros (C), null safety (Kotlin) | referencias TypeScript | C vs Kotlin |
| F | Name vs. structural equiv., coerción | TypeScript estructural | Kotlin nominal |
| G | Polimorfismo: ad-hoc, paramétrico, subtipo, varianza | generics `<T>`, extends, overloading | HM Haskell |

## Conexiones curriculares

- **← T09.1/T09.2:** vinculación de tipos (binding) → ahora sabemos *qué son* esos tipos
- **→ T11:** tipos de retorno y expresiones en estructuras de control
- **→ T14:** inferencia HM formal, teoría de subtipos, effect systems

## Anuncio

> **TP N° 4 — Sistemas de tipos:** análisis comparativo de type safety entre TypeScript y Kotlin/Haskell. Fecha de entrega: Semana 13.

---
