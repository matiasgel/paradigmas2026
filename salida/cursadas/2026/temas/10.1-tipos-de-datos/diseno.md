# Diseño de Clase — Tema 10.1
## Tipos de Datos y Sistemas de Tipos

> **Estado:** BORRADOR REFORMULADO — pendiente aprobación docente
> **Actualizado:** 2026-05-22
> **Agente:** Lic. Marcos 🗂️ (Topic Designer)
> **Decisión docente aplicada:** contenido reformulado para eliminar solapamientos con T09.1/T09.2 y enriquecer con Sebesta Cap. 6, Gabbrielli Cap. 8, Louden Cap. 8.
> **Motivo de reformulación:** T09.2 ya cubre extensivamente: tipado estático/dinámico/gradual, `any`/`unknown`, type narrowing y type guards. Esos bloques son eliminados de T10.1 y reemplazados por contenido exclusivo del dominio de tipos.

---

## Metadata del Tema

| Campo | Valor |
|-------|-------|
| Número de tema | 10.1 |
| Nombre | Tipos de Datos y Sistemas de Tipos |
| Módulo | VII — Tipos de Datos |
| Semana | 11 |
| Clase | 1 (extendida) |
| **Duración (constraint operativo)** | **360 minutos** |
| Perfil docente | profesor-teorico |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | Haskell, C, Kotlin, Python |
| Sibling topic | — (único tema del módulo VII) |

---

## Contexto en el Plan

**Prerequisito inmediato:** T09.1 (binding de tipos, 5-tupla) y T09.2 (gradual typing, narrowing — ya dictados).
**Diferenciación con T09.x:** T09.x trató *cómo se vincula* un tipo a una variable (binding) y *cómo el sistema verifica esa vinculación* (estático/dinámico/gradual). T10.1 trata *qué son los tipos* como estructuras de datos formales y cómo se organizan en sistemas.
**Diferenciación con T14:** T14 profundizará en inferencia formal, sistema HM y teoría de subtipos. T10.1 introduce los conceptos con orientación operacional y multilenguaje.

---

## Objetivos de Aprendizaje

Al finalizar el tema, el alumno podrá:

| # | Objetivo | Nivel Bloom |
|---|----------|-------------|
| OA1 | **Definir** el tipo como par (conjunto de valores + operaciones admisibles) y explicar su rol en corrección y seguridad | Recordar/Comprender |
| OA2 | **Clasificar y caracterizar** los tipos primitivos (numéricos, bool, char, enumeraciones) y sus representaciones internas | Comprender |
| OA3 | **Analizar** tipos producto (arrays, registros, tuplas) diferenciando sus variantes, binding times y representación en memoria | Analizar |
| OA4 | **Comparar** uniones libres (C) con uniones discriminadas (Kotlin sealed, Haskell ADT) y razonar sobre seguridad de tipos | Analizar |
| OA5 | **Evaluar** los problemas del tipo puntero (dangling pointer, memory leak) y aplicar mecanismos de null safety en Kotlin | Evaluar |
| OA6 | **Diferenciar** equivalencia de nombres y equivalencia estructural en distintos lenguajes y razonar sobre compatibilidad de tipos | Analizar |
| OA7 | **Aplicar** coerciones implícitas y conversiones explícitas identificando riesgos de precisión y truncamiento | Aplicar |
| OA8 | **Explicar** polimorfismo ad-hoc, paramétrico y por subtipo; aplicar generics con bounds y razonar sobre varianza | Analizar |
| OA9 | **Diferenciar** sistemas monomórficos de polimórficos e identificar qué nivel de polimorfismo usa cada construcción del lenguaje | Analizar |

---

## Mapa de Cobertura T10.1

```
Tipos de Datos y Sistemas de Tipos (T10.1)
  ├── A. Fundamentos del tipo como contrato formal
  │    ├── Tipo = valores + operaciones (Gabbrielli §8)
  │    ├── Type safety y soundness
  │    └── Taxonomía: primitivos / compuestos / monomórficos / polimórficos
  │
  ├── B. Tipos primitivos y su representación
  │    ├── Numéricos: enteros (complemento a 2), flotantes (IEEE 754)
  │    ├── Boolean, carácter (Unicode) y string
  │    └── Enumeraciones y tipos ordinales (Sebesta §6.4)
  │
  ├── C. Tipos producto (composición estructural)
  │    ├── Arrays: binding times, variantes, slices, row/column-major
  │    ├── Arrays asociativos / Maps
  │    ├── Registros / Records / Structs + alineamiento de memoria
  │    └── Tuplas como producto cartesiano formal (Gabbrielli §8.3)
  │
  ├── D. Tipos suma (uniones)
  │    ├── Uniones libres en C (inseguras)
  │    ├── Uniones discriminadas: Pascal, Ada, Haskell ADT
  │    ├── Kotlin sealed classes + when exhaustivo
  │    └── Tipos recursivos: listas y árboles (Gabbrielli §8.4)
  │
  ├── E. Punteros, referencias y null safety
  │    ├── Tipo puntero: operaciones, aritmética, peligros en C
  │    ├── Dangling pointer y lost heap-dynamic variables
  │    ├── Referencias vs. punteros (Java, Kotlin, C++)
  │    └── Null safety en Kotlin: ?, !!, ?., ?: 
  │
  ├── F. Equivalencia, coerción y conversión
  │    ├── Equivalencia de nombres (name equivalence)
  │    ├── Equivalencia estructural (structural equivalence)
  │    ├── Compatibilidad de tipos en asignación
  │    └── Coerción implícita vs. conversión explícita (widening/narrowing)
  │
  └── G. Polimorfismo y sistemas paramétricos
       ├── Sistemas monomórficos vs. polimórficos (Gabbrielli §8.6)
       ├── Ad-hoc: sobrecarga y resolución estática/dinámica
       ├── Paramétrico: generics, type variables, bounds (Kotlin, Haskell)
       ├── Subtipo: inclusión, sustitución de Liskov, varianza
       └── Inferencia de tipos: Hindley-Milner (intuición) (Louden §8)
```

---

## Estructura Didáctica

> **Nota de separación con T09.2:** los temas de estático vs. dinámico, fuerte vs. débil, gradual typing, `any`/`unknown` y type narrowing/guards NO se repiten — están completamente cubiertos en T09.2. Si un alumno tiene dudas sobre esos conceptos, se referencia a T09.2.

### Bloque A — El tipo como contrato formal (30 min)
**Fuentes:** Gabbrielli §8.1–§8.2; Sebesta §6.1; Louden §8.1

- Definición formal: tipo = conjunto de valores admisibles + conjunto de operaciones válidas.
  - Ejemplo: `Int` = valores {−2^31, …, 2^31−1} + operaciones {+, −, ×, /, mod, comparación, …}
  - Sin tipo, el procesador opera sobre bits sin semántica — el tipo *da significado* a los patrones binarios.
- **Type safety:** garantía de que ninguna operación se aplica a un valor fuera de su dominio.
  - *Soundness* de un sistema de tipos: si el sistema dice que el programa está bien tipado → no ocurrirán errores de tipo en ejecución.
  - C no es sound (unsafe casts); Haskell, ML y Kotlin (sin `!!`) sí lo son.
- **Taxonomía de tipos** (trazada a lo largo de toda la clase):
  - Primitivos vs. compuestos
  - Monomórficos vs. polimórficos (Gabbrielli §8.6)
  - De referencia vs. de valor (boxing/unboxing en Kotlin)
- Criterios de diseño de tipos (Sebesta §6.1): expresividad, eficiencia de representación, seguridad.

### Bloque B — Tipos primitivos y su representación interna (50 min)
**Fuentes:** Sebesta §6.2–§6.4; Gabbrielli §2.3; Louden §8.2

**B.1 — Tipos enteros (15 min)**
- Representación en complemento a 2: rango = [−2^(n−1), 2^(n−1)−1]
- Tipos en Kotlin: `Byte` (8 bits), `Short` (16), `Int` (32), `Long` (64)
- Overflow silencioso en C; overflow checked en Kotlin (`Math.addExact`) y en Rust (panic en debug)
- Enteros sin signo: ausentes en Kotlin (UInt existente pero no idiomático); presentes en C, Rust

**B.2 — Tipos de punto flotante (15 min)**
- Estándar IEEE 754: signo, exponente, mantisa
- `Float` (32 bits, ~7 dígitos significativos) vs. `Double` (64 bits, ~15 dígitos)
- Problemas de precisión: `0.1 + 0.2 ≠ 0.3` — demo en Kotlin y Python
- Valores especiales: `NaN`, `Infinity`, `-0.0` — comportamiento en operaciones
- Cuándo usar `BigDecimal` (monetario, científico) vs. `Double`

**B.3 — Boolean, carácter y string (10 min)**
- Boolean: 1 bit lógico, implementación varía (1 byte en C, 4 bytes en JVM históricamente)
- Char en Kotlin: Unicode UTF-16 (un `Char` = un code unit, no un code point completo)
- String: secuencia inmutable en Kotlin/Java; longitud en code units vs. caracteres (problemas con emojis)
- Diseño: strings mutables (StringBuilder) vs. inmutables (String) — consecuencias para aliases

**B.4 — Enumeraciones y tipos ordinales (10 min) — Sebesta §6.4**
- Tipo ordinal: valores discretos con orden total y operaciones pred/succ
- Enumeraciones en C: sinónimos de enteros, sin type safety real
- `enum class` de Kotlin: tipo cerrado, valores no son enteros, se puede agregar comportamiento
- Haskell `newtype`: envoltura de tipo sin costo en runtime — type safety total
- Diseño: Sebesta §6.4 — ventajas de enumeraciones sobre constantes enteras (legibilidad, type-safe)

### Bloque C — Tipos producto: arrays, registros y tuplas (65 min)
**Fuentes:** Sebesta §6.5–§6.8; Gabbrielli §8.3; Louden §8.3

**C.1 — Arrays y su diseño (25 min) — Sebesta §6.5**
- Definición: secuencia de elementos del mismo tipo, acceso por subíndice
- **5 variantes de binding time** (Sebesta §6.5.2):
  1. **Estáticos** (static arrays): tamaño fijado en compilación, almacenados en área estática — C `static int a[10]`
  2. **Stack-dynamic de tamaño fijo**: tamaño definido en elaboración, en stack — C local array, Kotlin array en función
  3. **Stack-dynamic de tamaño variable** (VLA): tamaño calculado en runtime, en stack — C99 `int a[n]`
  4. **Heap-dynamic de tamaño fijo**: tamaño fijado al asignar, en heap — Java `new int[n]`, Kotlin `IntArray(n)`
  5. **Heap-dynamic de tamaño variable**: tamaño cambia en runtime — Kotlin `MutableList`, Java `ArrayList`
- Verificación de bounds: en tiempo de compilación (estáticos), runtime (C++/Java/Kotlin — Kotlin lanza `IndexOutOfBoundsException`)
- **Arrays multidimensionales** (Sebesta §6.5.7): row-major (C, Kotlin, Java) vs. column-major (Fortran) — impacto en cache performance
- **Slices** (Sebesta §6.5.8): subarreglos con referencia compartida — Kotlin `subList`, Go slices, Python slices
- Arrays asociativos (Sebesta §6.5.9): `Map<K,V>` en Kotlin / `dict` Python — hash tables vs. balanced trees

**C.2 — Registros / Records / Structs (25 min) — Sebesta §6.7**
- Definición: tipo producto con campos nombrados de tipos potencialmente distintos
  - Producto cartesiano formal: `Person = String × Int × Boolean` (Gabbrielli §8.3)
- C `struct`: campos en posiciones contiguas de memoria con **alineamiento**
  - Padding: `struct { char c; int i; }` tiene 8 bytes, no 5 — el procesador requiere alineamiento a 4 bytes
  - Representación literal vs. representación con padding
- Kotlin `data class`: record con `equals`, `hashCode`, `copy` y `toString` automáticos
  - `copy` provee *pattern de copia parcial*: `persona.copy(edad = 30)` — sin aliases del original
- TypeScript interfaces como record types estructurales
- Haskell record syntax: `data Person = Person { name :: String, age :: Int }` — acceso y actualización
- Design issues (Sebesta §6.7.1): ¿fields con el mismo nombre en distintos records son el mismo tipo?

**C.3 — Tuplas y producto cartesiano formal (15 min) — Gabbrielli §8.3**
- Tupla = producto cartesiano con campos anónimos posicionales: `(Int, String, Bool)`
- Gabbrielli: el tipo `T1 × T2 × … × Tn` es el tipo de todas las n-tuplas donde el componente `i` es de tipo `Ti`
- Kotlin `Pair` y `Triple`; desestructuración: `val (nombre, edad) = Pair("Ana", 30)`
- TypeScript tuple types: `[string, number]` — diferencia con `Array<string | number>`
- Haskell: `(a, b)` como tipo base del lenguaje; relación con currying (función de tupla vs. función currificada)
- Cuándo preferir tupla sobre record: resultados múltiples anónimos vs. datos con semántica nombrada

### Bloque D — Tipos suma: uniones y tipos recursivos (50 min)
**Fuentes:** Sebesta §6.9; Gabbrielli §8.3–§8.4; Louden §8.4

**D.1 — Uniones libres en C (inseguras) (10 min) — Sebesta §6.9.1**
- Definición: varios campos comparten la misma región de memoria — tamaño = max de todos los campos
- C `union { int i; float f; char c[4]; }` — `i`, `f` y `c` son aliases del mismo bloque de 4 bytes
- **Problema de type safety**: no hay marca que indique qué campo está activo — el programador puede leer `f` cuando fue escrito `i` → comportamiento indefinido
- Uso legítimo: serialización/deserialización de bajo nivel, instrucciones SIMD — con conocimiento explícito del layout de memoria

**D.2 — Uniones discriminadas (tipos suma seguros) (20 min) — Sebesta §6.9.2, Gabbrielli §8.3**
- Solución: agregar una **etiqueta de discriminador** al union — el tipo del campo activo queda registrado
- Pascal (variant records), Ada (discriminant records) — history
- Gabbrielli §8.3 — tipo suma formal: `T1 + T2 + … + Tn` (también: *disjoint union*, *tagged union*, *sum type*)
  - Un valor de `T1 + T2` es *o bien* un valor de `T1* *o bien* uno de `T2`, nunca los dos
  - Contraste con el producto: `T1 × T2` combina ambos tipos simultáneamente
- **Haskell ADTs** (Algebraic Data Types): `data Shape = Circle Double | Rect Double Double | Triangle Double Double Double`
  - Pattern matching como mecanismo de eliminación del tipo suma — el compilador verifica exhaustividad
- **Kotlin sealed classes** (Sebesta no las tiene — Kotlin es posterior):
  ```kotlin
  sealed class Forma {
      data class Circulo(val radio: Double) : Forma()
      data class Rectangulo(val ancho: Double, val alto: Double) : Forma()
  }
  ```
  - `when` exhaustivo: el compilador obliga a cubrir todos los subtipos
  - Equivalente directo a `match` en Haskell/Rust/Scala

**D.3 — Tipos recursivos: listas y árboles (20 min) — Gabbrielli §8.4**
- Definición formal: un tipo es recursivo si aparece en su propia definición
  - `Lista(A) = Vacia | Nodo(A, Lista(A))`  — definición inductiva
  - `Arbol(A) = Hoja(A) | Nodo(Arbol(A), A, Arbol(A))`
- Implementación: requiere indirección (puntero/referencia) porque el tipo tiene tamaño infinito sin ella
  - Kotlin: `data class Nodo<T>(val valor: T, val siguiente: Nodo<T>?)` — `?` es la referencia nullable que actúa como Vacia
  - Haskell: `data List a = Nil | Cons a (List a)` — algebraic recursion, size implícito en tags
- Tipos mutualmente recursivos: expresiones y sentencias en un parser (Gabbrielli §8.4)
- Conexión con el plan mínimo: árboles binarios, listas enlazadas — todos son tipos recursivos

### Bloque E — Punteros, referencias y null safety (40 min)
**Fuentes:** Sebesta §6.11.1–§6.11.4; Gabbrielli §8.5; Louden §7.8

**E.1 — Tipo puntero en C (15 min) — Sebesta §6.11.2**
- Operaciones fundamentales:
  - `&` (address-of): obtener la dirección de memoria de una variable — convierte L-value en R-value de tipo puntero
  - `*` (dereference): acceder al valor almacenado en la dirección apuntada
- Aritmética de punteros: `p + 1` avanza `sizeof(*p)` bytes — permite recorrer arrays como punteros
  - Sebesta: la aritmética de punteros es la principal fuente de inseguridad en C — fuera del rango del array → comportamiento indefinido
- **Dangling pointer** (Sebesta §6.11.3.1): puntero que apunta a memoria ya liberada o fuera de scope
  - Causa 1: `free(p)` sin hacer `p = NULL` — el valor de la dirección queda válido para el compilador
  - Causa 2: retornar la dirección de una variable local (`return &x` — x está en stack, se destruye al retornar)
  - Consecuencia: lectura → valores aleatorios (old stack data); escritura → corrupción de memoria o segfault
- **Lost heap-dynamic variable** / memory leak (Sebesta §6.11.3.2): celda heap sin puntero que la referencie → imposible liberar → memoria que el OS nunca recupera hasta terminar el proceso

**E.2 — Referencias vs. punteros (10 min) — Sebesta §6.11.4**
- Referencia (Java, Kotlin, C++): alias manejado por el runtime — sin aritmética, sin acceso a la dirección
  - En Java/Kotlin: toda variable de tipo objeto es una referencia — los tipos primitivos (`Int`, `Double`) son de valor
  - No hay `null` en Kotlin sin declaración explícita `?`
- Puntero (C, C++): dirección numérica manejada por el programador — con aritmética, con riesgo
  - C++ tiene `std::unique_ptr`, `std::shared_ptr` (smart pointers) para gestión automática

**E.3 — Null safety en Kotlin (15 min) — Kotlin docs / Sebesta §6.11.5**
- Hoare (1965): "null reference" es el *"billion dollar mistake"* — crashes silenciosos en producción
- Kotlin resuelve esto en el **sistema de tipos**:
  - `String` → never null (el compilador garantiza)
  - `String?` → puede ser null (el compilador obliga a verificar antes de usar)
- Operadores null-safe:
  - `?.` (safe call): `persona?.nombre` — retorna null si `persona` es null, sin NPE
  - `?:` (Elvis operator): `persona?.nombre ?: "Anónimo"` — valor por defecto si null
  - `!!` (non-null assertion): `persona!!.nombre` — lanza NPE si null — uso excepcional
  - `let { }` con null check: `persona?.let { println(it.nombre) }` — bloque ejecuta solo si no null
- Kotlin vs. Java: Java permite `null` en cualquier referencia sin restricción — históricamente NullPointerException es la excepción más frecuente en producción

### Bloque F — Equivalencia, coerción y conversión de tipos (40 min)
**Fuentes:** Sebesta §6.12–§6.13; Gabbrielli §8.2; Louden §8.5

**F.1 — Equivalencia de tipos (20 min) — Sebesta §6.12**

*¿Cuándo dos expresiones de tipo son el mismo tipo?*

- **Equivalencia de nombres (name equivalence)** — Sebesta §6.12.1:
  - Dos tipos son equivalentes solo si son **el mismo tipo declarado** (mismo nombre en el mismo scope)
  - Dos `struct` con exactamente los mismos campos pero nombres distintos son tipos diferentes
  - Pascal, Ada, Java usan name equivalence
  - Ventaja: mayor seguridad y modularidad — cada tipo es una abstracción independiente
  - Ejemplo en Kotlin: `typealias Metros = Double` y `typealias Kilos = Double` — con name equivalence serían tipos distintos (typealias en Kotlin es alias de compilación, sin garantía de diferenciación en runtime)

- **Equivalencia estructural (structural equivalence)** — Sebesta §6.12.2:
  - Dos tipos son equivalentes si tienen **la misma estructura** (mismos campos, mismo orden, mismos tipos de campos)
  - TypeScript, Haskell, OCaml usan equivalencia estructural
  - Un objeto con `{ nombre: string; edad: number }` es compatible con la interfaz `{ nombre: string; edad: number }` aunque no la implemente explícitamente (TypeScript)
  - Ventaja: flexibilidad, composición sin herencia formal
  - Desventaja: puede aceptar tipos que accidentalmente tienen la misma forma pero semántica distinta

- **Subtipado** (Sebesta §11.4 / Gabbrielli §8.7): relación de compatibilidad en asignación
  - Un tipo `S` es subtipo de `T` si cualquier valor de `S` puede usarse donde se espera `T`
  - Principio de sustitución de Liskov (LSP): el cliente no debe notar la diferencia

**F.2 — Coerción y conversión (20 min) — Sebesta §6.13**

- **Coerción implícita (widening coercion)**: conversión automática que no pierde información
  - `Int` → `Long` → `Double`: widening — siempre seguro
  - Java hace widening automático; Kotlin no — obliga a conversiones explícitas (principio de diseño)
  - C hace *numeric promotion*: `int + double` → el compilador convierte el `int` a `double` silenciosamente

- **Coerción implícita (narrowing coercion)**: conversión automática que puede perder información
  - `Double` → `Int`: truncamiento silencioso en C — `3.9` → `3` sin aviso
  - Kotlin prohíbe el narrowing implícito: `val x: Int = 3.9` → error de compilación — obliga a `3.9.toInt()`

- **Conversión explícita (explicit cast)**:
  - Kotlin: `.toInt()`, `.toDouble()`, `.toLong()` — semántica clara, sin sorpresas
  - C-style cast: `(int) 3.9` — peligroso, puede truncar o reinterpretar bits
  - Kotlin `as`: cast de tipos de referencia — lanza `ClassCastException` si incompatible; `as?` retorna null en vez de lanzar

- **Mixed mode arithmetic** (Sebesta §6.13.2): expresiones con operandos de tipos distintos
  - Reglas de promoción en C/Java: jerarquía de conversiones automáticas
  - Riesgos: `int / int` → truncamiento entero en C/Java (`5 / 2 = 2`) — bug clásico de precisión

### Bloque G — Polimorfismo y sistemas paramétricos (85 min)
**Fuentes:** Sebesta §11.1–§11.3, §12.4; Gabbrielli §8.6–§8.7; Louden §8.6–§8.7

**G.1 — Sistemas monomórficos vs. polimórficos (10 min) — Gabbrielli §8.6**
- **Sistema monomórfico**: cada expresión tiene exactamente un tipo; una función tiene exactamente un tipo de dominio y codominio
  - Ejemplo: `sumar(a: Int, b: Int): Int` solo opera sobre enteros — no sirve para doubles
  - C (sin templates) es esencialmente monomórfico — la genericidad se logra con `void*` perdiendo type safety
- **Sistema polimórfico**: una función o tipo puede operar sobre varios tipos distintos
  - Gabbrielli distingue polimorfismo universal (paramétrico + inclusión) y ad-hoc (sobrecarga + coerción)
  - El plan mínimo exige cubrir todos los niveles — este bloque los desarrolla sistemáticamente

**G.2 — Polimorfismo ad-hoc: sobrecarga (20 min) — Sebesta §11.2**
- Definición: misma nombre para múltiples funciones con tipos de parámetros distintos
- Resolución estática (static dispatch): el compilador decide qué función llamar según los tipos en compilación
  - Kotlin: sobrecarga resuelta en compilación — `fun area(c: Circulo)` vs. `fun area(r: Rectangulo)` — sin costo en runtime
- Resolución dinámica (dynamic dispatch): en herencia y polimorfismo por subtipo — la decisión se toma en runtime
  - Kotlin `open fun hablar()` + `override fun hablar()` — dispatch según el tipo real del objeto
- Operadores sobrecargados (Kotlin `operator fun plus(other: Vector): Vector`)
- Límite del polimorfismo ad-hoc: requiere enumerar todos los tipos manualmente — no es genérico

**G.3 — Polimorfismo paramétrico: generics (25 min) — Sebesta §11.3, Gabbrielli §8.6, Louden §8.7**
- Definición: la función o tipo tiene un **parámetro de tipo** `T` que puede ser instanciado con cualquier tipo
  - `fun <T> identidad(x: T): T = x` — funciona para cualquier tipo T sin duplicar código
  - Gabbrielli: es el polimorfismo "verdadero" porque una sola implementación sirve para todos los tipos
- Type variables y su instanciación:
  - `List<String>`, `List<Int>`, `List<Pair<String, Int>>` — son instanciaciones distintas del tipo genérico `List<T>`
- **Bounded quantification / constraints** (Sebesta §11.3.2, Kotlin):
  - `fun <T : Comparable<T>> max(a: T, b: T): T` — T debe ser Comparable para poder comparar
  - Kotlin upper bounds: `T : Number`, múltiple: `T : Comparable<T>` e interfaz adicional con `where`
  - Haskell typeclasses: `max :: Ord a => a -> a -> a` — más expresivo, permite múltiples constraints
- **Tipo `Maybe<T>` / `Option<T>` como ejemplo canónico** de tipo genérico:
  - `sealed class Maybe<out T> { object Nothing : Maybe<Nothing>(); data class Just<T>(val value: T) : Maybe<T>() }`
  - Encapsula la ausencia de valor sin usar null — patrón funcional puro

**G.4 — Polimorfismo por subtipo (inclusión) y varianza (20 min) — Sebesta §12.4, Gabbrielli §8.7**
- Principio de sustitución: si `Dog <: Animal`, donde se espere `Animal` se puede usar `Dog`
- **Covarianza**: `List<Dog>` ¿es subtipo de `List<Animal>`?
  - Intuitivamente sí, pero puede producir errores si la lista es mutable (agregar un `Cat` a la lista)
  - Kotlin: `List<out T>` (read-only) → covariante; `MutableList<T>` → invariante
- **Contravarianza**: `Consumer<Animal>` ¿es subtipo de `Consumer<Dog>`?
  - Si una función procesa animales, puede procesar perros — pero no al revés
  - Kotlin: `in T` → contravariante
- **Invarianza**: `MutableList<Dog>` NO es subtipo de `MutableList<Animal>` — requiere `T` exacto
- Gabbrielli §8.7: las tres reglas formales de varianza para tipos compuestos
- Ejemplo integrador: `Comparable<in T>` en Kotlin es contravariante por diseño

**G.5 — Inferencia de tipos: Hindley-Milner (intuición) (10 min) — Louden §8.6, Gabbrielli §8.9**
- El programador no siempre necesita anotar todos los tipos — el compilador puede *inferirlos*
- Hindley-Milner (HM): algoritmo W — garantiza inferencia de tipos *principal* (el tipo más general posible)
  - Inventado independientemente por Hindley (1969) y Milner (1978) para ML
  - Haskell usa HM extendido — la mayoría del código Haskell no necesita anotaciones de tipo
- Kotlin type inference: `val x = 42` → el compilador infiere `Int`; `val lista = listOf(1, 2, 3)` → `List<Int>`
  - Limitación: Kotlin requiere anotaciones en firmas de funciones públicas — deliberado para legibilidad de APIs
- Resultado pedagógico: la inferencia no es magia — es resolución de ecuaciones de tipos

---

## Actividades clave

| # | Actividad | Duración | Objetivo |
|---|-----------|----------|----------|
| A1 | **Diagnóstico de tipos**: dado un fragmento de C con `union` libre, identificar qué lecturas son undefined behavior | 15 min | OA4 |
| A2 | **Rediseño con sealed class**: reescribir el union C del A1 como Kotlin sealed class con `when` exhaustivo | 15 min | OA4 |
| A3 | **Aritmética de punteros**: trazar manualmente el comportamiento de un array recorrido con puntero en C; identificar el dangling pointer | 15 min | OA5 |
| A4 | **Null safety refactor**: dado código Kotlin con `!!` innecesarios, reemplazar por `?.` y `?:` | 10 min | OA5 |
| A5 | **Equivalencia nominal vs. estructural**: el mismo fragmento en TypeScript (estructural) y un pseudocódigo con name equivalence — predecir qué compila | 15 min | OA6 |
| A6 | **Generics con bounds**: implementar `fun <T : Comparable<T>> insertionSort(list: MutableList<T>)` — razonar por qué el bound es necesario | 20 min | OA8/OA9 |

---

## Tópicos del Plan Mínimo cubiertos

| Tópico institucional (Módulo VII) | Cobertura en T10.1 | Notas |
|-----------------------------------|--------------------|-------|
| Tipos built-in y primitivos | ✅ Bloque B | Numéricos, bool, char, string |
| Tipos ordinales definidos por usuario | ✅ B.4 | Enumeraciones, Kotlin enum class |
| Tipos de agregación: producto cartesiano | ✅ C.3 | Tuplas, formalización Gabbrielli |
| Tipos de agregación: uniones discriminadas | ✅ D.2 | C unsafe + Kotlin sealed + Haskell ADT |
| Arrays: estáticos, pila dinámica, heap dinámica | ✅ C.1 | 5 variantes Sebesta §6.5 |
| Tipos secuencia, strings | ✅ B.3, C.1 | String inmutable, slices |
| Tipo puntero: inseguridad, punteros colgantes, GC | ✅ E.1 | Dangling + lost variable |
| Sistemas de tipos: monomórficos vs. polimórficos | ✅ G.1 | Gabbrielli §8.6 |
| Tipos que aceptan null y sus operadores | ✅ E.3 | Null safety Kotlin |
| Lenguajes fuertemente tipados; clases | ✅ A | Type safety + clases Kotlin |
| Niveles de polimorfismo | ✅ G.2–G.4 | Ad-hoc, paramétrico, subtipo |
| Ejemplos en Kotlin y otros lenguajes | ✅ Todo | Kotlin principal; C/Haskell/TS contraste |

---

## Diferenciación explícita con T09.x (no repetir)

| Concepto | Cubierto en | NO repetir en T10.1 |
|----------|-------------|---------------------|
| Tipado estático vs. dinámico (espectro) | T09.2 F-27/F-28 | ✗ |
| Gradual typing y TypeScript como caso | T09.2 F-27b, F-29, F-30 | ✗ |
| `any` vs. `unknown` | T09.2 F-30b | ✗ |
| Type narrowing con `typeof`/`instanceof` | T09.2 F-31, F-32, F-33 | ✗ |
| Exhaustive narrowing con `never` | T09.2 F-33 | ✗ |
| Binding de tipos (estático/dinámico) | T09.1 F-08/F-09 | ✗ |
| Strong vs. weak typing | T09.2 F-27 | ✗ (mencionar brevemente para conectar, no desarrollar) |

---

## Conexiones curriculares

| Dirección | Tema | Conexión |
|-----------|------|----------|
| ← Prerequisito directo | T09.1 Variables, Binding y Ámbito | Binding de tipos → ahora se estudia qué son esos tipos |
| ← Prerequisito directo | T09.2 Aliases, Closures, GC | Gradual typing + narrowing → base para entender por qué los sistemas de tipos son seguros o no |
| → Continuación | T11 Estructuras de Control | Expresiones y tipos de retorno; type-driven control flow |
| → Profundización | T14 Sistemas de Tipos (avanzado) | Inferencia HM formal, teoría de subtipos, effect systems |

---

## Distribución de tiempo

| Bloque | Contenido | Duración |
|--------|-----------|----------|
| A | Tipo como contrato formal | 30 min |
| B | Tipos primitivos y representación | 50 min |
| C | Tipos producto (arrays, registros, tuplas) | 65 min |
| D | Tipos suma (uniones, tipos recursivos) | 50 min |
| Pausa activa + checkpoint | — | 10 min |
| E | Punteros, referencias, null safety | 40 min |
| F | Equivalencia, coerción, conversión | 40 min |
| G | Polimorfismo y sistemas paramétricos | 85 min |
| **Total** | | **370 min** |

> Nota: 370 min supera levemente los 360. El docente puede comprimir G.5 (inferencia HM) a 5 min o moverla a T14 si el tiempo no alcanza. OA9 de T14 la cubre en detalle.

---

## Bibliografía base

| Fuente | Capítulos relevantes | Uso |
|--------|----------------------|-----|
| Sebesta, R.W. (2019). *Concepts of Programming Languages* (12ª ed.). Pearson. | Cap. 6 (§6.1–§6.13), §11.1–§11.3, §12.4 | Base de tipos primitivos, arrays, records, unions, punteros, equivalencia, polimorfismo |
| Gabbrielli, M. & Martini, S. (2023). *Programming Languages: Principles and Paradigms* (2ª ed.). Springer. | Cap. 8 (§8.1–§8.9) | Formalización de tipos, productos, sumas, tipos recursivos, polimorfismo paramétrico, varianza |
| Louden, K.C. & Lambert, K.A. (2012). *Programming Languages: Principles and Practices* (3ª ed.). Course Technology. | Cap. 8 (§8.1–§8.7) | Inferencia de tipos, type expressions, HM, overloading resolution |

---

## Aprobación

| Estado | Fecha | Responsable |
|--------|-------|-------------|
| 🔲 BORRADOR REFORMULADO | 2026-05-22 | Marcos (Topic Designer) — reformulado por GitHub Copilot |
| ⬜ APROBADO | — | Matías Gel (Docente) |
