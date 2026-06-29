# Minuta de Clase — Tema 10
## Tipos de Datos y Sistemas de Tipos

> **Docente:** Matías Gel
> **Duración:** 360 minutos (clase unificada — Módulo VII completo)
> **Referencia:** `filminas.md` — F-00 a F-58
> **Uso:** Esta minuta es autocontenida. El docente puede conducir toda la clase usando solo este archivo.

---

## Indicaciones generales

- **Ritmo:** 1 filmina cada ~5-6 minutos en promedio; las actividades tienen su tiempo propio
- **Código en vivo:** tener VSCode / TypeScript Playground abiertos para F-06, F-19, F-20, F-26, F-36, F-46, F-47
- **Pizarra:** reservar para mapa conceptual en F-03 (roadmap), F-12 (diagrama equivalencia) y F-53 (integrador)
- **Actividades:** F-14, F-28, F-39 — distribuir código en papel o en pantalla antes de comenzar cada una

---

## BLOQUE 0 — Apertura y Conexión (15 min)

---

### [F-00] Portada

**⏱ Tiempo:** 1 min
**Acción:** proyectar mientras los alumnos se acomodan.

---

### [F-01] ¿Qué diferencia hay entre `1` en tres lenguajes?

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- Los tipos son más que nombres — tienen implementación, semántica y binding
- Mismo literal, representaciones completamente distintas

**🗣 Guion docente:**
> "Hoy abrimos con una pregunta aparentemente simple: ¿qué diferencia hay entre el número `1` en C, en Python y en Haskell? Porque si los tres imprimen `1`, ¿realmente son lo mismo?"

Mostrar los tres bloques de código en pantalla. Para cada uno:
- **C:** "En C, `int x = 1` es exactamente 4 bytes en memoria, complemento a 2. Punto. Si desborda, se wrappea silenciosamente."
- **Python:** "En Python, `x = 1` es un objeto de la clase `int`, con un contador de referencias, con GC. Puede crecer tanto como la memoria lo permita."
- **Haskell:** "En Haskell, `x = 1` no tiene tipo concreto todavía — es `Num a => a`. El tipo real se decide cuando el compilador ve cómo se usa `x`."

> "Esto nos muestra que los tipos no son solo etiquetas — son decisiones de diseño con consecuencias concretas en rendimiento, seguridad y expresividad. Eso es lo que vamos a ver hoy."

**❓ Preguntas anticipadas:**
- *"¿No es lo mismo un entero en todos los lenguajes?"* → No. El tamaño, el overflow behavior y quién gestiona la memoria varían enormemente.
- *"¿Qué es `Num a => a`?"* → Anticipar brevemente: es polimorfismo paramétrico — lo vemos en el Bloque 4.

**→ Transición:** "Antes de arrancar, conectemos con T09 — ¿qué vimos la clase pasada?"

---

### [F-02] Conexión T09 → T10

**⏱ Tiempo:** 4 min

**🎯 Conceptos clave:**
- T09 respondió CUÁNDO se vincula un tipo → T10 responde QUÉ son los tipos
- La clase de hoy es complementaria, no repetición

**🗣 Guion docente:**
> "En T09 trabajamos con la 5-tupla de variables y el binding: cuándo se asocia un nombre a un tipo, a un valor, a una ubicación. Vimos tipado estático, dinámico y gradual. Vimos scope, aliases."

> "Hoy subimos un nivel de abstracción: nos preguntamos ¿qué son los tipos como estructuras formales? ¿Cómo se clasifican? ¿Cómo se construyen unos a partir de otros? ¿Qué es un sistema de tipos?"

Dibujar en pizarra: dos recuadros con flechas → T09 = 'binding' y T10 = 'estructura formal del tipo'.

**❓ Preguntas anticipadas:**
- *"¿No es lo mismo?"* → No — binding de tipo ≠ tipo en sí. Como la diferencia entre saber cuándo una persona tiene un nombre y saber qué significa ese nombre.

**→ Transición:** "Miren la hoja de ruta de la clase para saber cómo organizamos los 360 minutos."

---

### [F-03] Hoja de ruta

**⏱ Tiempo:** 3 min

**🎯 Conceptos clave:**
- 5 bloques, 360 minutos
- TypeScript es el lenguaje hilo conductor

**🗣 Guion docente:**
> "Vamos a tener cinco bloques. El primero cubre los tipos más simples: primitivos y ordinales. El segundo los tipos compuestos: arrays, registros, uniones. El tercero punteros, null safety y tipos recursivos. El cuarto sistemas de tipos y polimorfismo. Y el quinto síntesis y cierre."

> "El lenguaje principal va a ser TypeScript — todos los ejemplos centrales van en TypeScript. Los contrastes con C, Kotlin, Haskell y Python los hacemos en comparaciones puntuales, no como narrativas paralelas."

**→ Transición:** "Arrancamos con el Bloque 1 — lo más fundamental: ¿qué es un tipo de dato?"

---

## BLOQUE 1 — Tipos Primitivos y Ordinales (70 min)

---

### [F-04] ¿Qué es un tipo de dato?

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- Tipo = conjunto de valores + conjunto de operaciones
- Razones para incluir tipos: legibilidad, detección de errores, reusabilidad
- Clasificación: primitivos / compuestos / definidos por el usuario

**🗣 Guion docente:**
> "La definición canónica es de Sebesta: un tipo de dato define una colección de valores y un conjunto de operaciones predefinidas sobre esos valores. Simple, pero poderosa."

> "¿Por qué los lenguajes incluyen tipos? Tres razones principales: **legibilidad** — el código expresa la intención; **detectabilidad de errores** — el compilador o runtime puede atrapar uso incorrecto; y **reusabilidad** — podemos abstraer comportamiento por tipo."

Dibujar el diagrama de los dos círculos superpuestos: valores y operaciones.

> "La clasificación básica es: primitivos (representaciones directas de hardware — int, float, bool, char), compuestos (construidos sobre primitivos — struct, array, union) y definidos por el usuario (enumeraciones, subrangos, ADTs)."

**❓ Preguntas anticipadas:**
- *"¿`string` es primitivo?"* → Depende del lenguaje: en TypeScript sí (aunque con métodos via boxing). En Java es un objeto. Gran punto de diferencia.
- *"¿Las clases son tipos?"* → Sí — en OOP, cada clase define un tipo. Lo vemos en el Bloque 4.

**→ Transición:** "Empecemos con los primitivos numéricos — enteros."

---

### [F-05] Tipos numéricos — Enteros

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Representación en complemento a 2, tamaños, rangos
- TypeScript `number` no distingue entero de float
- `bigint` para enteros de precisión arbitraria

**🗣 Guion docente:**
> "En C, los enteros son directos: `int` son 32 bits en complemento a 2, `long` son 64. El overflow es silencioso y wrappea — nadie te avisa."

> "En TypeScript, la situación es peculiar: **no hay tipo entero**. `number` es siempre un IEEE 754 de 64 bits — el mismo tipo que `double` en Java. Esto significa que `number` puede representar enteros exactamente hasta `Number.MAX_SAFE_INTEGER` = 2⁵³ − 1."

> "Para enteros más grandes existe `bigint` — precisión arbitraria, con literales que terminan en `n`. `9007199254740991n + 1n` funciona perfectamente."

Abrir TypeScript Playground: escribir `0.1 + 0.2 === 0.3` para anticipar la próxima filmina.

**❓ Preguntas anticipadas:**
- *"¿Por qué TypeScript no tiene int separado?"* → Herencia de JavaScript: JS siempre tuvo un solo tipo numérico. TypeScript es JS tipado, no un lenguaje nuevo.

**→ Transición:** "Y ahora el punto flotante — con la trampa que ya adelanté."

---

### [F-06] Tipos numéricos — Floating Point

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- IEEE 754 de 64 bits: signo + exponente + mantisa
- `0.1 + 0.2 !== 0.3` — mostrar en vivo
- TypeScript no tiene decimal nativo — usar `decimal.js` para finanzas

**🗣 Guion docente:**
> "El estándar IEEE 754 define cómo se representan los números de punto flotante en binario. TypeScript `number` es *siempre* un double de 64 bits — no hay `float` de 32 bits como en Kotlin o Java."

Abrir TypeScript Playground en vivo:
```
console.log(0.1 + 0.2)           // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3)   // false ← demostrar
```

> "¿Qué pasa? 0.1 y 0.2 no tienen representación exacta en binario. Su suma tiene un error de representación. La forma correcta de comparar floats es con epsilon."

> "Para aplicaciones financieras donde la exactitud decimal es crítica — dinero, impuestos — TypeScript no tiene tipo decimal nativo. Se usa la librería `decimal.js`. Contraste: Java tiene `BigDecimal` en el JDK."

**❓ Preguntas anticipadas:**
- *"¿Esto pasa en todos los lenguajes?"* → Sí, en cualquier lenguaje que use IEEE 754. Python lo muestra igual. La diferencia es que algunos lenguajes incluyen decimal como tipo nativo (C#, Fortran).

**→ Transición:** "Veamos los tipos numéricos menos frecuentes pero interesantes por lo que revelan del diseño del lenguaje."

---

### [F-07] Tipos numéricos especiales

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Tipo complejo nativo vs. librería: decisión de diseño
- Boolean en TypeScript vs. C — diferencias críticas
- Char en TypeScript: no existe — solo `string`

**🗣 Guion docente:**
> "Tipos interesantes que revelan decisiones de diseño: ¿deben los lenguajes incluir `complex` o `decimal` como tipos primitivos?"

> "Python eligió incluir `complex` como nativo: `3+4j` es un literal válido. Fortran también, porque es un lenguaje de cómputo científico. Java y TypeScript decidieron que es responsabilidad de una librería. ¿Cuál es mejor? Depende del dominio."

**→ Transición:** "Boolean y Char muestran decisiones de diseño aún más diversas."

---

### [F-08] Boolean y Char

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- C no tiene tipo boolean real — consecuencias en legibilidad
- TypeScript no tiene `char` — solo `string`

**🗣 Guion docente:**
> "En TypeScript, `boolean` es un tipo real con dos valores: `true` y `false`. En C clásico, no existe tipo boolean — cualquier entero distinto de 0 es 'verdadero'. Eso genera código como `if (ptr)` que puede sorprender."

> "Char es aún más interesante. TypeScript directamente **no tiene tipo char**. Un carácter es una `string` de longitud 1. Es una decisión pragmática heredada de JavaScript. En Kotlin, `Char` es un tipo real de UTF-16. En C, `char` es un byte — ni siquiera representa Unicode."

**❓ Preguntas anticipadas:**
- *"¿Cómo trabajo con caracteres individuales en TypeScript?"* → `"hola"[0]` retorna `"h"` — una string de longitud 1.

**→ Transición:** "Pasamos a los tipos ordinales definidos por el usuario — las enumeraciones."

---

### [F-09] Enumeraciones en TypeScript

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Numeric enum, string enum, const enum
- TypeScript: type-safe a diferencia de C
- `const enum` para inlining en compilación

**🗣 Guion docente:**
> "Los enums de TypeScript son un tipo de primera clase. `enum Direction { Up, Down, Left, Right }` crea un tipo real — no se puede pasar `42` donde se espera `Direction`."

Mostrar código en pantalla, ejecutar:
```typescript
enum Direction { Up, Down, Left, Right }
function move(dir: Direction) { ... }
// move(0) ← TypeScript acepta para numeric enums — este es un gotcha importante
```

> "Interesante: TypeScript numeric enums aceptan el número subyacente. Es una debilidad de diseño. String enums son más seguros porque `Status.Active` compila a `'active'` y no se puede pasar un string arbitrario."

> "`const enum` es una optimización: el compilador reemplaza cada uso por el valor literal. Sin objeto en runtime — zero overhead."

**❓ Preguntas anticipadas:**
- *"¿Cuándo usar string enum vs. numeric enum?"* → String enum para APIs externas y serialización; numeric enum para estados internos o flags de bits.

**→ Transición:** "Comparemos con C, Kotlin y Haskell para ver cuánto varían."

---

### [F-10] Enumeraciones — Comparación multilenguaje

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- C: no type-safe — es un int con alias
- Kotlin: `enum class` con propiedades y métodos
- Haskell: ADT más poderoso

**🗣 Guion docente:**
> "La tabla resume las diferencias. El punto clave de Sebesta: el problema de los enums en C es que no son type-safe. `enum Direction { UP, DOWN }` en C es esencialmente un `int` con nombres. Puedes hacer `int x = UP + 5` y el compilador no se queja."

> "Kotlin va en la dirección opuesta: `enum class` puede tener propiedades y métodos. Cada valor de la enum puede tener comportamiento diferente. TypeScript está en el medio."

**→ Transición:** "Hay otro tipo ordinal definido por el usuario: los subrangos."

---

### [F-11] Subrangos y equivalencia (introducción)

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Subrangos: Pascal/Ada tienen soporte nativo; TypeScript simula con literal unions
- El tradeoff: seguridad vs. expresividad vs. rendimiento

**🗣 Guion docente:**
> "Los subrangos son tipos cuyo rango de valores es un subconjunto contiguo de un ordinal. Pascal: `type DiasLaborables = 1..5`. El compilador sabe que solo 1 a 5 son válidos."

> "TypeScript lo simula con literal unions: `type Day = 1|2|3|4|5`. El compilador **sí** rechaza `const d: Day = 6`. No es un subrango en el sentido de Pascal, pero logra el mismo nivel de seguridad estática."

**→ Transición:** "Ahora algo conceptualmente más profundo: equivalencia de tipos."

---

### [F-12] Equivalencia nominal vs. estructural

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Nominal: iguales por nombre → Kotlin, Java
- Estructural: iguales por estructura → TypeScript, Go
- Consecuencias prácticas en diseño de código

**🗣 Guion docente:**
> "Pregunta central: ¿cuándo son iguales dos tipos?"

> "La equivalencia **nominal** dice: dos tipos son iguales si tienen el mismo nombre. Kotlin: `data class Celsius(val v: Double)` y `data class Fahrenheit(val v: Double)` son tipos distintos aunque ambos wrappeen `Double`. El compilador los rechaza al intentar intercambiarlos."

> "La equivalencia **estructural** dice: dos tipos son iguales si tienen la misma estructura. TypeScript: si un objeto tiene campos `x: number` y `y: number`, es compatible con `Punto2D` sin importar cómo se llama."

Dibujar en pizarra: dos recuadros idénticos → nominal: ¿iguales? Depende del nombre → estructural: ¿iguales? Sí.

> "TypeScript eligió estructural por flexibilidad. Pero esto tiene un costo: `UserId = string` y `Email = string` son intercambiables. El compilador no puede ayudarte si confundes uno con otro."

**❓ Preguntas anticipadas:**
- *"¿Cuál es mejor?"* → Depende del contexto. Nominal es más seguro semánticamente. Estructural es más flexible y menos verboso.

**→ Transición:** "Veamos la tabla comparativa entre lenguajes."

---

### [F-13] Equivalencia — Tabla comparativa

**⏱ Tiempo:** 4 min

**🎯 Conceptos clave:**
- Reforzar la tabla: C, Java, Kotlin → nominal; TypeScript, Go → estructural

**🗣 Guion docente:**
> "La consecuencia práctica de diseño: en TypeScript, si tengo `type UserId = string` y `type Email = string`, el compilador acepta pasar un email donde espero un userId. Eso es un bug semántico que el tipo no captura. La solución son los branded types — los vemos en el Bloque 4."

**→ Transición:** "Actividad rápida para fijar equivalencia."

---

### [F-14] Actividad — Equivalencia de tipos

**⏱ Tiempo:** 8 min (actividad: 5 min + discusión: 3 min)

**🎯 Conceptos clave:**
- TypeScript: estructural → Caso A ✓, Caso B ✓ (excess property check en literal), Caso C ✓
- Kotlin: nominal → Caso D ✗ (error de compilación)

**🗣 Guion docente:**
> "Tienen 5 minutos para predecir qué pasa en cada caso — sin ejecutar. Solo razonando sobre el sistema de tipos."

Respuestas correctas:
- **Caso A:** `{ x: 1, y: 2 }` → ✅ compatible con `Punto2D`
- **Caso B:** `{ x: 1, y: 2, z: 3 }` → ⚠️ compatible *si se pasa como variable* — TypeScript hace excess property check solo en object literals directos pasados inline; si está en una variable, pasa
- **Caso C:** `const v: Vector2D` → ✅ compatible — misma estructura
- **Caso D:** Kotlin → ❌ `Vector2D` no es subtipo de `Punto2D` — equivalencia nominal

> "El Caso B es el tricky. Si escriben `graficar({ x:1, y:2, z:3 })` directamente → TypeScript da error (excess property check). Pero si lo asignan a una variable primero → pasa. Ese es un comportamiento que hay que conocer."

**→ Transición:** "Bloque 2 — tipos compuestos. Arrancamos con strings."

---

## BLOQUE 2 — Tipos de Agregación y Colecciones (90 min)

---

### [F-15] Strings — Tipo primitivo vs. objeto

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- TypeScript: string primitivo + inmutable + comparación por valor con `===`
- Java: ERROR clásico con `==` (compara referencia)
- C: puntero a char — comparar con `strcmp`, no con `==`

**🗣 Guion docente:**
> "Los strings parecen simples hasta que comparás. El error clásico en Java: `str1 == str2` compara **referencias**, no contenido. Hay que usar `.equals()`. En TypeScript, `===` compara por **valor** siempre — no hay surpresas."

> "En C, una string es directamente un puntero a un array de chars terminado en `\0`. Comparar con `==` compara las direcciones, no el contenido. Hay que usar `strcmp()`."

> "TypeScript hereda de JavaScript: `string` es primitivo pero el runtime hace autoboxing para permitir llamar métodos como `.toUpperCase()`. El resultado siempre es una nueva string — son inmutables."

**❓ Preguntas anticipadas:**
- *"¿`String` con mayúscula en TypeScript?"* → Existe como objeto wrapper (`new String("hola")`) pero prácticamente nunca se usa — siempre usar `string` minúscula.

**→ Transición:** "Pasamos a los tipos más usados en programación: los arrays."

---

### [F-16] Arrays — Taxonomía por binding time

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- Clasificación por binding time de forma y rango (Figura 6.2 de Sebesta)
- Cuatro categorías: estático, semi-dinámico (stack), heap fijo, heap flexible

**🗣 Guion docente:**
> "Sebesta clasifica los arrays según **cuándo** se fija su forma y su rango. Esta clasificación es más profunda que solo 'arreglo de tamaño fijo vs. dinámico'."

Recorrer la tabla fila a fila:
- **Estático:** `int a[10]` en C global — forma y rango fijos en compilación, memoria estática. Sin GC, sin stack.
- **Semi-dinámico (stack):** `int a[n]` en C99 local — la forma se decide en runtime pero no cambia después. Se libera automáticamente al salir del scope. Llamados VLAs (Variable Length Arrays).
- **Heap fijo:** `new Array<number>(n)` en TypeScript — tamaño decidido en runtime, luego fijo. En heap, con GC.
- **Heap flexible:** `number[]` en TypeScript — puede crecer y achicarse. El más usado en lenguajes modernos.

> "En TypeScript, el tipo que usamos todo el tiempo — `T[]` — es un array de heap flexible. El motor gestiona el realloc automáticamente."

**→ Transición:** "Ahora algo que pocos piensan: cómo se accede a un array multidimensional en memoria."

---

### [F-17] Arrays — Función de acceso multidimensional

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Row-major vs. column-major: consecuencias de rendimiento
- Cache locality — el orden de iteración importa

**🗣 Guion docente:**
> "Cuando tenemos un array `a[i][j]`, ¿cómo se calcula la dirección de memoria? En C, Java, TypeScript: row-major — los elementos de una fila están contiguos. La dirección de `a[i][j]` es `base + (i × cols + j) × size`."

> "Fortran y MATLAB usan column-major — las columnas son contiguas. Esto es relevante para performance en multiplicación de matrices o procesamiento de imágenes."

Ejemplo concreto: "Si tenemos una imagen de 1000×1000 pixels y la procesamos fila a fila en C (row-major), accedemos contiguamente en memoria → los datos están en cache. Si la procesamos columna a columna → cada acceso es un cache miss → puede ser 10× más lento."

**❓ Preguntas anticipadas:**
- *"¿TypeScript tiene arrays bidimensionales?"* → Sí, como arrays de arrays: `number[][]`. Son jagged por naturaleza.

**→ Transición:** "Que nos lleva a la diferencia entre arrays rectangulares y jagged."

---

### [F-18] Arrays — Rectangulares vs. Jagged + Slices

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- Rectangular (C#, Fortran): todos los sub-arrays de igual longitud
- Jagged (Java, C, TypeScript): array de referencias/punteros a arrays
- Slices: referencia sin copia — diferente en Python vs. Kotlin vs. Go

**🗣 Guion docente:**
> "Java hizo una decisión de diseño: todos los arrays multidimensionales son jagged. `int[][] a = new int[3][4]` es en realidad un array de 3 referencias, cada una apuntando a un array de 4 ints. Esto implica una indirección extra pero permite filas de distinto tamaño."

> "Las slices son un tema relacionado: en Python, `lista[1:4]` produce una **nueva lista** (copia). En Kotlin, `lista.subList(1, 4)` produce una **vista viva** — si modificás la vista, modificás la original. En Go, las slices son ciudadanos de primera clase con length y capacity separados."

**→ Transición:** "Arrays asociativos — o mapeos finitos."

---

### [F-19] Arrays asociativos — Maps

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- `Map<K,V>` para claves arbitrarias
- `Record<string, V>` para claves string
- Sebesta §6.8: colección no ordenada indexada por claves

**🗣 Guion docente:**
> "Un array asociativo — Sebesta lo llama así — es una colección no ordenada de elementos indexada por claves. No es un array en el sentido de acceso por índice numérico."

Mostrar código en vivo en TypeScript Playground:
```typescript
const scores = new Map<string, number>([["Ana", 9]])
scores.set("Luis", 7)
console.log(scores.get("Ana"))   // 9
```

> "En TypeScript tenemos dos formas: `Map<K,V>` para claves de cualquier tipo, y `Record<string, V>` que usa un objeto como mapa — más simple para claves string, menos poderoso."

**→ Transición:** "Código completo de arrays en TypeScript."

---

### [F-20] Código completo — Arrays en TypeScript

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Cuatro formas de crear arrays en TypeScript
- `ReadonlyArray<T>` para inmutabilidad
- `Int32Array` para rendimiento sin boxing

**🗣 Guion docente:**
Recorrer el código comentando cada variante.

> "El array más común es el dinámico: `const lista: number[] = [1, 2, 3]` con `push()`. El `new Array(5).fill(0).map(...)` es útil cuando necesitamos tamaño inicial conocido. Los `TypedArrays` como `Int32Array` son para manipulación de buffers binarios o WebGL — sin el overhead de boxing de los arrays genéricos."

**→ Transición:** "De arrays a registros y estructuras."

---

### [F-21] Registros e interfaces en TypeScript

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- `interface` vs `type`: diferencias sutiles (extensibilidad vs. expresividad)
- `readonly` para inmutabilidad
- Contraste con Kotlin `data class` — genera métodos automáticos

**🗣 Guion docente:**
> "Un registro es una colección de campos identificados por nombre — Sebesta §6.6. En TypeScript, usamos `interface` o `type`."

> "La diferencia práctica: `interface` puede ser extendida (`extends`) y augmentada después de declararse (declaration merging). `type` puede expresar uniones y tipos más complejos. Para objetos simples, son intercambiables."

> "En Kotlin, `data class` genera automáticamente `equals`, `hashCode`, `toString` y `copy()`. TypeScript no tiene nada equivalente — hay que implementarlos manualmente o usar librerías."

**→ Transición:** "Ahora tuplas — el producto cartesiano formal."

---

### [F-22] Tuplas en TypeScript

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Tupla como producto cartesiano formal: A × B
- TypeScript: tuplas literales tipadas, desestructuración
- Contraste: Kotlin `Pair`/`Triple`, Python tuplas inmutables

**🗣 Guion docente:**
> "Una tupla es formalmente el producto cartesiano: `A × B` = todos los pares `(a, b)` donde `a: A` y `b: B`. TypeScript los expresa como `[string, number]`."

Mostrar desestructuración: `const [nombre, edad] = par` — muy usada en React hooks y retornos múltiples.

**→ Transición:** "Listas funcionales — otra estructura secuencial con semántica distinta."

---

### [F-23] Listas funcionales — Definición

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Origen en LISP 1958: head, tail, cons
- Recursividad inherente
- Diferencia O(1) vs. O(n) con arrays

**🗣 Guion docente:**
> "Las listas funcionales vienen de LISP, 1958. La operación fundamental es `cons`: construye una lista añadiendo un elemento al frente. La lista `[1, 2, 3]` en LISP era `cons(1, cons(2, cons(3, nil)))`."

> "En Haskell, los tipos lista son la estructura de datos principal. `head xs` retorna el primer elemento, `tail xs` retorna el resto, `x:xs` construye una lista añadiendo `x` al frente."

> "La diferencia clave con arrays: acceso aleatorio en lista enlazada es O(n) — hay que recorrer desde el inicio. Arrays tienen O(1). Pero inserción al frente de lista enlazada es O(1) — arrays requieren O(n) para desplazar."

**→ Transición:** "Tabla de implementaciones multilenguaje."

---

### [F-24] Listas funcionales — Implementaciones

**⏱ Tiempo:** 4 min

**🎯 Conceptos clave:**
- Python `list` es array dinámico, no lista enlazada real
- Haskell `[a]` es lista enlazada real — inmutable siempre

**🗣 Guion docente:**
> "Dato importante: Python `list` es en realidad un array dinámico, no una lista enlazada. Tiene acceso O(1) por índice. Haskell `[a]` sí es una lista enlazada real, inmutable, con pattern matching."

> "En TypeScript, `T[]` es un array dinámico. `ReadonlyArray<T>` lo hace inmutable — útil en paradigma funcional con TypeScript."

**→ Transición:** "Ahora las uniones — desde la inseguridad de C hasta la elegancia de TypeScript."

---

### [F-25] Uniones libres — C `union`

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- C `union`: comparte espacio de memoria
- Sin forma de verificar qué campo fue escrito
- Fuente de bugs difíciles de detectar

**🗣 Guion docente:**
> "En C, un `union` permite que distintos tipos compartan el mismo espacio de memoria. Si escribiste el campo `i` y lees el campo `f` — estás interpretando los mismos bits como un float. El resultado es basura."

> "Sebesta lo llama 'fundamentally unsafe'. El programador tiene que recordar qué campo es válido — el lenguaje no puede ayudar. Esto generó décadas de bugs."

Código en pantalla: `d.i = 42; printf("%f\n", d.f)` — destacar el acceso incorrecto.

**→ Transición:** "La solución moderna: uniones discriminadas."

---

### [F-26] Uniones discriminadas — TypeScript

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Campo `kind` como etiqueta discriminante
- TypeScript narrowea el tipo en cada rama
- Con `--strictNullChecks`: caso sin manejar → error

**🗣 Guion docente:**
> "La idea es simple pero poderosa: añadir una etiqueta — un campo `kind` — que siempre dice qué variante es activa. Así el lenguaje puede verificar que accedemos al campo correcto."

Mostrar código con `Result<T>` y el switch. Ejecutar en vivo:
```typescript
const r: Result<number> = { kind: 'success', value: 42 }
switch (r.kind) {
  case 'success': console.log(r.value)  // aquí TypeScript sabe que hay .value
}
```

> "Dentro del case 'success', TypeScript **sabe** que `r` es `{ kind: 'success'; value: number }`. Este es el narrowing de tipos en acción."

**❓ Preguntas anticipadas:**
- *"¿Cómo sé si todos los casos están cubiertos?"* → Usar el `never` trick: añadir `default: const _exhaustive: never = r` — si se agrega una nueva variante y no se maneja, el compilador da error.

**→ Transición:** "Comparemos con Kotlin y Haskell."

---

### [F-27] Uniones discriminadas — Tres implementaciones

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- Kotlin `sealed class`: exhaustividad garantizada automáticamente por el compilador en `when`
- Haskell ADT: pattern matching
- Comparar mecánicas

**🗣 Guion docente:**
> "En Kotlin, `sealed class` hace la exhaustividad automática. Si tenés un `when` sobre un `sealed class` y te falta un caso, el compilador te da error. No tenés que hacer ningún trick."

> "En Haskell, el pattern matching sobre ADTs es exhaustivo por construcción — el compilador avisa sobre casos no cubiertos."

> "La diferencia es que TypeScript requiere esfuerzo explícito (el `never` trick o la opción del compilador); Kotlin y Haskell lo hacen por diseño."

**→ Transición:** "Actividad: diseñar un ADT."

---

### [F-28] Actividad — Diseño de ADT

**⏱ Tiempo:** 8 min (5 min trabajo + 3 min discusión)

**🎯 Conceptos clave:**
- TypeScript discriminated union vs. C struct+union manual
- Errores posibles en C que TypeScript previene

**🗣 Guion docente:**
Distribuir el código o proyectarlo. Dar 5 minutos para completar la solución TypeScript.

Solución esperada TypeScript:
```typescript
type Figura =
  | { kind: 'circulo';     radio:  number }
  | { kind: 'rectangulo'; base: number; alto: number }

function area(f: Figura): number {
  switch (f.kind) {
    case 'circulo':     return Math.PI * f.radio ** 2
    case 'rectangulo': return f.base * f.alto
  }
}
```

Discusión: "En la versión C, ¿qué pasa si alguien lee `data.radio` cuando el kind es `RECTANGULO`? El compilador no avisa. En TypeScript, el compilador previene el acceso al campo incorrecto."

**→ Transición:** "Bloque 3 — pasamos al nivel de la memoria con punteros."

---

## BLOQUE 3 — Punteros, Null Safety y Tipos Recursivos (75 min)

---

### [F-29] Tipo puntero — Definición y semántica

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Puntero = dirección de memoria + valor especial `nil`
- Operaciones: `&` (toma dirección) y `*` (desreferencia)
- Usos legítimos

**🗣 Guion docente:**
> "Un puntero es un valor que contiene una dirección de memoria. No es el valor en sí — es la dirección donde vive el valor."

Dibujar en pizarra: variable `ptr` con valor `0x1A2B3C` → flecha a una celda de heap con valor `42`.

> "En C: `int* ptr = &x` — el `&` toma la dirección de `x`; `*ptr` — el `*` desreferencia: accede al valor en esa dirección. `ptr++` avanza al siguiente `int` en memoria — aritmética de punteros."

> "Los usos legítimos son tres: manejo indirecto de datos en heap, paso eficiente de estructuras grandes (en lugar de copiar), y construcción de estructuras dinámicas como listas enlazadas o árboles."

**❓ Preguntas anticipadas:**
- *"¿TypeScript tiene punteros?"* → No en la superficie — lo vemos en las próximas filminas.

**→ Transición:** "Los punteros también generan problemas clásicos difíciles de debuggear."

---

### [F-30] Punteros — Problemas clásicos

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Dangling pointer, memory leak, double free, null dereference, buffer overflow
- Herramientas de detección: Valgrind, AddressSanitizer

**🗣 Guion docente:**
Recorrer la tabla fila a fila con un ejemplo breve de cada:

- **Dangling pointer:** `free(ptr); *ptr = 5;` — ya liberaste esa memoria; otro objeto puede estar ahí.
- **Memory leak:** olvidar llamar `free()` — la memoria nunca vuelve al sistema. En procesos largos, crece indefinidamente.
- **Double free:** llamar `free(ptr)` dos veces — comportamiento indefinido, puede corromper el heap.
- **Null dereference:** `*NULL` → crash con SIGSEGV.
- **Buffer overflow:** `int a[5]; a[10] = 0;` — sobreescribe memoria adyacente. Causa de vulnerabilidades de seguridad históricas (CVE, shellcode).

> "Las soluciones históricas de Sebesta: Tombstones y Locks and Keys. Hoy usamos GC o Rust con ownership."

**→ Transición:** "La solución moderna más adoptada es el Garbage Collector."

---

### [F-31] Garbage Collection

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- Reference counting: Python, Swift — problema con ciclos
- Tracing GC: JVM, Go, JS/TS — stop-the-world pero sin ciclos
- Ventajas y costo

**🗣 Guion docente:**
> "El GC elimina automáticamente los tres problemas más comunes de punteros: dangling pointers, memory leaks y double free. El costo es rendimiento — el GC consume CPU y puede producir pausas."

> "Reference counting — Python y Swift — libera inmediatamente cuando el contador llega a 0. Pero no puede manejar ciclos: si A apunta a B y B apunta a A, ambos tienen contador 1 aunque nada los referencie desde el exterior."

> "Tracing GC — JVM, Go, JavaScript — periódicamente recorre el grafo de objetos desde las raíces (stack, variables globales). Los objetos no alcanzables son candidatos a recolección. Las pausas stop-the-world eran el gran problema histórico; los GC modernos (G1GC, ZGC) las reducen a sub-milisegundo."

**→ Transición:** "Una distinción importante: referencias vs. punteros."

---

### [F-32] Referencias vs. Punteros

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Referencia = alias constante implícitamente dereferenciado
- No hay aritmética, no puede ser null (en C++)
- TypeScript/Kotlin: referencias gestionadas por GC

**🗣 Guion docente:**
> "Sebesta: 'Una variable de referencia es un puntero constante que siempre se desreferencia implícitamente'. En C++, `int& r = x` es un alias que siempre apunta al mismo objeto — no se puede reasignar y no puede ser null."

> "En TypeScript, todas las variables de objeto son referencias implícitas. Cuando escribís `const obj = { x: 1 }` y pasás `obj` a una función, pasás una referencia — la función puede modificar el objeto. Pero no podés hacer aritmética de punteros ni hay `*` explícito."

**→ Transición:** "Ahora tipos recursivos — donde los tipos se definen a sí mismos."

---

### [F-33] Tipos recursivos — Definición

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Un tipo que se define en términos de sí mismo
- Posible porque el campo recursivo es una referencia (tamaño fijo)

**🗣 Guion docente:**
> "Un tipo recursivo se define en términos de sí mismo. La lista enlazada clásica en C: un nodo tiene un valor y un puntero al siguiente nodo. El nodo es del tipo `Node`, y tiene dentro un puntero a `Node`."

> "¿Por qué esto es posible? Porque `Node*` tiene tamaño fijo (el tamaño de un puntero) independientemente del tamaño de `Node`. Si fuera `struct Node { int value; struct Node next; }` — sin puntero — el compilador calcularía un tamaño infinito."

**→ Transición:** "En TypeScript, los tipos recursivos son elegantes gracias a las uniones discriminadas."

---

### [F-34] Tipos recursivos — Árbol binario en TypeScript

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- Árbol binario como union discriminada recursiva
- Función `depth` que explota la estructura recursiva
- Contraste con Kotlin `sealed class`

**🗣 Guion docente:**
> "TypeScript permite tipos recursivos directamente en la definición de tipos alias. `BinaryTree<T>` es o una hoja o un nodo con valor y dos sub-árboles del mismo tipo."

Mostrar `depth()` en vivo: "La función es recursiva exactamente como el tipo. El case 'leaf' es el caso base. El case 'node' llama a `depth()` en ambos sub-árboles."

> "Kotlin logra lo mismo con `sealed class Tree<T>` — la recursión es en los parámetros del constructor. Haskell con ADT es lo mismo conceptualmente."

**→ Transición:** "El problema del null — uno de los errores de diseño más costosos de la historia."

---

### [F-35] El problema del null

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Tony Hoare: "my billion-dollar mistake"
- El problema: cualquier referencia puede ser null sin que el tipo lo diga
- La solución: hacer null parte del sistema de tipos

**🗣 Guion docente:**
> "En 1965, Tony Hoare introdujo el null pointer en ALGOL W. En 2009, en la conferencia QCon, lo llamó 'my billion-dollar mistake': llevó a incontables errores, vulnerabilidades y crashes de sistemas."

> "El problema es conceptual: en Java, una variable de tipo `String` puede contener una string válida **o** el valor especial `null`. El tipo no lo distingue. El error solo aparece en runtime cuando intentás usar el `null` como si fuera una string."

> "La solución es hacer que el sistema de tipos distinga: un tipo que puede ser null vs. uno que no puede. Kotlin y TypeScript (con `strictNullChecks`) lo hacen."

**→ Transición:** "Operadores de null safety en TypeScript."

---

### [F-36] TypeScript Null Safety — Operadores

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- `strictNullChecks: true` activa el sistema
- `T | null`, `?.`, `??`, `!`, narrowing
- Tabla de operadores

**🗣 Guion docente:**
Recorrer la tabla de operadores:

> "Con `strictNullChecks: true`, TypeScript distingue `string` (nunca null) de `string | null` (puede ser null). La declaración del tipo dice la verdad."

> "`?.` — optional chaining: si `x` es null, retorna `undefined` en lugar de lanzar error. `x?.prop` es equivalente a `x !== null ? x.prop : undefined`."

> "`??` — nullish coalescing: si la expresión izquierda es null o undefined, usa la derecha. `user.email ?? 'sin email'`."

> "`x!` — non-null assertion: le decís al compilador 'confía en mí, esto no es null'. Si te equivocas, el error ocurre en runtime. Usar solo cuando tenés certeza externa que el compilador no puede verificar."

**→ Transición:** "Código completo que integra todos los operadores."

---

### [F-37] TypeScript Null Safety — Código completo

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- `User` con campo `email: string | null`
- Uso de `??`, `?.`, narrowing — todos en un ejemplo

**🗣 Guion docente:**
Mostrar código en vivo, ejecutar en TypeScript Playground.

> "`user.email ?? 'sin email'` — si email es null, usa el string por defecto. Esto es el 'Elvis operator' que vienen de Groovy/Kotlin."

> "`user.email?.toUpperCase()` — si email es null, retorna `undefined` en lugar de lanzar. No es necesario el `if !== null` para este caso."

> "El `if (user.email !== null)` hace narrowing — dentro del bloque, TypeScript *sabe* que `email` es `string` (no `string | null`). Puede usar `.toUpperCase()` directamente."

**→ Transición:** "Comparemos con Kotlin y otros lenguajes."

---

### [F-38] Null Safety — Comparación multilenguaje

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Kotlin: null safety por diseño, siempre activado
- TypeScript: opt-in con `strictNullChecks`
- Tabla de operadores equivalentes

**🗣 Guion docente:**
> "La gran diferencia de diseño: Kotlin activó null safety desde el día uno. TypeScript lo hizo opt-in por retrocompatibilidad con código JavaScript existente. Un proyecto TypeScript sin `strict: true` tiene null safety apagado."

> "Los operadores son casi idénticos: `?.` en ambos, `??` en TS = `?:` en Kotlin (Elvis), `!` en TS = `!!` en Kotlin."

**→ Transición:** "Actividad de refactoring con null safety."

---

### [F-39] Actividad — Null Safety Refactor

**⏱ Tiempo:** 12 min (8 min código + 4 min discusión)

**🎯 Conceptos clave:**
- Identificar puntos de NPE potencial
- Reescribir usando `| null`, `?.`, `??`
- Discutir la decisión de diseño de TypeScript de hacer opt-in

**🗣 Guion docente:**
Proyectar el código JavaScript problemático. Dar 8 minutos para reescribir.

Solución esperada:
```typescript
function getUserCity(userId: string): string {
  const user = findUser(userId)
  const city = user?.address?.city
  return city?.toUpperCase() ?? 'Ciudad desconocida'
}
```

> "La versión con optional chaining encadenado es elegante y segura. Si cualquier parte de la cadena es null, retorna `undefined`, y `??` lo reemplaza por el valor por defecto."

Discusión: "¿Por qué TypeScript hace opt-in y Kotlin no?" — Respuesta principal: TypeScript tiene que convivir con millones de líneas de código JavaScript existente. Activar strict mode en un proyecto legacy rompe todo. Kotlin fue diseñado desde cero sin ese legado.

**→ Transición:** "Bloque 4 — sistemas de tipos en profundidad."

---

## BLOQUE 4 — Sistemas de Tipos: Monomórficos, Polimórficos y Strong Typing (80 min)

---

### [F-40] Type Checking — Definición y coerción

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Tipo compatible = tipo exacto + coercible implícitamente
- Widening (seguro) vs. Narrowing (pérdida posible)
- Type error: operador sobre operando inapropiado

**🗣 Guion docente:**
> "El chequeo de tipos es la actividad de verificar que los operandos de cada operador son de tipos compatibles. La compatibilidad incluye coerción implícita — si el compilador puede convertir automáticamente el tipo."

> "Widening: `int → float` es seguro, no pierde información. Narrowing: `float → int` puede perder — el compilador suele dar warning. En TypeScript con `strict`, el narrowing explícito requiere casting."

> "Un type error es usar un operador con un tipo que no lo soporta: `"hola" - 5` en un lenguaje fuertemente tipado → error. En JavaScript/TypeScript sin strict → `NaN`. La tolerancia a errores varía."

**→ Transición:** "¿Cuándo ocurre el chequeo?"

---

### [F-41] Type Checking — Estático vs. Dinámico

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- TypeScript: caso especial — chequeo estático pero runtime es JS sin tipos
- Ventajas/costos de cada enfoque

**🗣 Guion docente:**
> "Estático = en compilación. Dinámico = en runtime. TypeScript es un caso especial: hace chequeo estático durante la compilación, pero emite JavaScript — en runtime, los tipos desaparecen (type erasure). El GC no sabe de tipos TypeScript."

> "Esto tiene consecuencias: puedes hacer un `as` cast que TypeScript acepta pero que en runtime falla porque el objeto no es del tipo esperado. TypeScript no puede garantizar nada en runtime — solo en compilación."

> "Python hace todo en runtime. JavaScript puro también. Haskell tiene el sistema de tipos más riguroso: todo verificado en compilación, y el runtime solo ve el resultado."

**→ Transición:** "Sistemas de tipos tienen tres dimensiones clave."

---

### [F-42] Visión general — Dimensiones de un sistema de tipos

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Tres dimensiones: cuándo / qué tan rígido / cuántos tipos
- Estático/dinámico, Strong/weak, Monomórfico/polimórfico

**🗣 Guion docente:**
> "Un sistema de tipos tiene tres dimensiones que podemos usar para clasificar cualquier lenguaje."

Dibujar o señalar el diagrama 3D:
> "**¿Cuándo verifica?** Estático = compilación (TypeScript, Kotlin, Haskell), Dinámico = runtime (Python, JS)."

> "**¿Qué tan rígido?** Strong: siempre detecta errores de tipo. Weak: coerciones amplias, errores posibles."

> "**¿Cuántos tipos por valor?** Monomórfico: exactamente uno. Polimórfico: puede ser de múltiples tipos (via generics o herencia)."

**→ Transición:** "Strong typing — una de las dimensiones más malentendidas."

---

### [F-43] Strong Typing — Definición y matices

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Sebesta: Haskell y Ada como los más fuertemente tipados
- C/C++: NO strongly typed (void*, union sin discriminación)
- TypeScript: strongly typed en compilación, no en runtime

**🗣 Guion docente:**
> "Sebesta define: un lenguaje es fuertemente tipado si todos los errores de tipo son **siempre** detectados. Haskell y Ada son los ejemplos más fuertes."

> "C falla en esto por dos razones: `void*` — un puntero sin tipo que puede castearse a cualquier cosa — y los `union` sin discriminación que vimos antes. El compilador no puede garantizar correctitud de tipos."

> "TypeScript está fuertemente tipado **dentro del compilador**. Con `strict: true`, el compilador detecta prácticamente todo. Pero el runtime es JavaScript sin tipos — podés introducir cualquier valor con `as any` y se escapa al runtime."

> "Kotlin está fuertemente tipado tanto en compilación como en runtime (JVM verifica tipos también). Haskell es el más estricto de todos — ni siquiera admite coerciones numéricas implícitas."

**→ Transición:** "Sistemas monomórficos — el baseline histórico."

---

### [F-44] Sistemas monomórficos

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Cada expresión: exactamente un tipo
- Limitación: código duplicado para cada tipo → motivación para polimorfismo

**🗣 Guion docente:**
> "En un sistema monomórfico, cada expresión tiene exactamente un tipo. C sin templates es el ejemplo clásico: si querés `max` para enteros y para floats, necesitás dos funciones distintas con el mismo código duplicado."

> "Esta limitación es la motivación histórica para el polimorfismo — quiero escribir `max` una sola vez y que funcione para cualquier tipo comparable."

**→ Transición:** "La taxonomía del polimorfismo — Strachey y Cardelli."

---

### [F-45] Polimorfismo — Taxonomía

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- Ad-hoc: apariencia de uniformidad (sobrecarga, coerción)
- Universal: uniformidad real (paramétrico, subtipo)

**🗣 Guion docente:**
> "La taxonomía de Strachey (1967) y Cardelli & Wegner (1985) distingue dos grandes familias."

> "**Ad-hoc:** apariencia de uniformidad. Sobrecarga — `+` en TypeScript funciona con números y con strings, pero son dos operaciones completamente diferentes. Coerción — `int + float` parece uniforme pero el compilador inserta una conversión."

> "**Universal:** uniformidad real. Paramétrico — la función `primero<T>(lista: T[])` funciona genuinamente para cualquier tipo T con el mismo código. Subtipo — cualquier `Animal` puede usarse donde se espera `Animal`, independientemente del subtipo concreto."

**→ Transición:** "Sobrecarga en TypeScript — polimorfismo ad-hoc."

---

### [F-46] Polimorfismo ad-hoc — Sobrecarga

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- TypeScript: firmas de sobrecarga + implementación única
- Contraste Kotlin: sobrecarga directa de funciones
- Distinción: no es "un tipo acepta varios valores" — son múltiples funciones

**🗣 Guion docente:**
> "En TypeScript, la sobrecarga se declara con firmas de overload y una implementación genérica que las cubre todas."

Mostrar código de `area()` en vivo. Ejecutar `area(5)` y `area(3, 4)`.

> "La distinción importante: sobrecarga **no es** polimorfismo paramétrico. Son múltiples funciones distintas con el mismo nombre — el compilador elige cuál llamar basándose en los tipos de los argumentos. El binding es estático."

**→ Transición:** "Polimorfismo paramétrico — generics."

---

### [F-47] Polimorfismo paramétrico — Generics

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- `<T>` como parámetro de tipo
- Upper bounds con `extends`
- Clases y tipos genéricos

**🗣 Guion docente:**
> "En el polimorfismo paramétrico, el tipo es un parámetro. `function primero<T>(lista: T[]): T` funciona para cualquier T con el mismo código — no hay distinción de implementación."

Mostrar en vivo:
```typescript
function primero<T>(lista: T[]): T { return lista[0] }
primero([1, 2, 3])           // T inferred como number
primero(["a", "b", "c"])     // T inferred como string
```

> "Con upper bounds, podemos restringir T: `T extends Comparable` significa 'T debe tener método de comparación'. TypeScript usa `extends` para constrains estructurales — no nominales."

> "Las clases genéricas como `Caja<T>` también siguen el mismo principio. `ReadonlyBox<T>` es un tipo genérico — una familia de tipos, uno por cada T posible."

**→ Transición:** "La varianza — ¿puede Caja<Gato> usarse donde Caja<Animal>?"

---

### [F-48] Polimorfismo paramétrico — Varianza

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Covariante, contravariante, invariante
- Kotlin: declaración explícita `out`/`in`
- TypeScript: inferida automáticamente desde estructura

**🗣 Guion docente:**
> "Si `Gato` es subtipo de `Animal`, ¿es `Caja<Gato>` subtipo de `Caja<Animal>`? Depende de la varianza."

> "Kotlin requiere que lo declares: `out T` (covariante — el tipo solo sale, es productor), `in T` (contravariante — el tipo solo entra, es consumidor). Si lees Y escribes, es invariante."

> "TypeScript lo infiere automáticamente desde la estructura: si `T` solo aparece en posiciones de salida, el tipo es covariant naturalmente. No hay anotaciones explícitas."

**→ Transición:** "Polimorfismo por subtipo — herencia e interfaces."

---

### [F-49] Polimorfismo por subtipo

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- Principio de Liskov (LSP)
- TypeScript `implements` + dispatch dinámico en runtime
- Diferencia con polimorfismo paramétrico

**🗣 Guion docente:**
> "El Principio de Liskov: S es subtipo de T si cualquier programa que usa T funciona correctamente al reemplazarlo por S. `Circulo implements Forma` significa que `Circulo` puede usarse en cualquier contexto que espere `Forma`."

> "La diferencia con paramétrico: aquí el dispatch ocurre en **runtime** — el motor llama al método correcto según el tipo real del objeto. Con paramétrico, el binding es en compilación."

Mostrar `areaTotal` en vivo — el array mezcla `Circulo` y `Rectangulo`, el método `.area()` se resuelve correctamente para cada uno.

**→ Transición:** "Tabla comparativa de los tres polimorfismos."

---

### [F-50] Comparación de los tres polimorfismos

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Resumen: mecanismo, binding, overhead, restricción

**🗣 Guion docente:**
Recorrer la tabla rápidamente, enfatizando:
- Ad-hoc: sin overhead, binding estático
- Paramétrico: sin overhead (JVM usa type erasure), binding estático
- Subtipo: virtual dispatch (pequeño overhead), binding dinámico

**→ Transición:** "Branded types — cómo simular equivalencia nominal en TypeScript."

---

### [F-51] Branded Types y Type Aliases

**⏱ Tiempo:** 7 min

**🎯 Conceptos clave:**
- TypeScript estructural: `UserId = string` y `Email = string` son intercambiables
- Branded types: añadir campo `_brand` para hacerlos estructuralmente distintos
- `as const` para tipos literales

**🗣 Guion docente:**
> "Recuerdan que TypeScript usa equivalencia estructural. Entonces `UserId = string` y `Email = string` son el mismo tipo — el compilador acepta intercambiarlos."

> "La solución: branded types. Usamos intersección `string & { readonly _brand: 'UserId' }` para crear un tipo estructuralmente distinto. El `_brand` nunca existe en runtime — es solo un marcador para el compilador."

> "`as const` es otra herramienta: fuerza que TypeScript infiera tipos literales en lugar de los tipos amplios. `{ debug: true } as const` tiene tipo `{ readonly debug: true }`, no `{ debug: boolean }`."

**→ Transición:** "Revisita final de equivalencia de tipos."

---

### [F-52] Type Equivalence — Revisita

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Kotlin `@JvmInline value class` para equivalencia nominal eficiente
- TypeScript: necesita discriminante o branded type

**🗣 Guion docente:**
> "En Kotlin, `@JvmInline value class Celsius(val v: Double)` crea un tipo nominal sin overhead en JVM — el compilador lo representa como un `Double` en bytecode, pero el sistema de tipos lo trata como `Celsius`. Perfecto para unidades de medida."

> "TypeScript no tiene nada equivalente nativo. Hay que usar branded types o campos discriminantes. La implicación de diseño: al elegir TypeScript, hay que ser consciente de esta limitación si se trabaja con unidades o tipos semánticamente distintos."

**→ Transición:** "Bloque 5 — síntesis y cierre."

---

## BLOQUE 5 — Síntesis y Cierre (30 min)

---

### [F-53] Mapa conceptual integrador

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Integrar todos los conceptos del día en un mapa
- Mostrar las conexiones entre bloques

**🗣 Guion docente:**
> "Construyamos juntos el mapa del día. Tenemos dos grandes áreas: Tipos de Datos y Sistemas de Tipos."

Dibujar en pizarra mientras se muestra la filmina:
- Tipos de Datos → Primitivos (enteros, float, bool, char) → Ordinales (enum, subrangos) → Compuestos (array, registro, tupla, unión, lista) → Recursivos (árbol, lista enlazada) → Opcionales (T|null, Maybe, Option)
- Sistemas de Tipos → dimensiones → equivalencia → polimorfismo

> "Las conexiones: los tipos primitivos son la base → los compuestos se construyen sobre ellos → los recursivos se construyen sobre los compuestos. El sistema de tipos define las reglas de compatibilidad entre todos."

**→ Transición:** "Miremos la evolución histórica."

---

### [F-54] Evolución de sistemas de tipos

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- De LISP (1958) a Rust (2015) — 57 años de evolución
- Cada lenguaje resolvió limitaciones del anterior

**🗣 Guion docente:**
Recorrer la timeline brevemente:
> "ML (1978) fue el gran salto: inferencia de tipos Hindley-Milner — el compilador infiere los tipos sin que el programador los declare. Toda la teoría detrás de lo que TypeScript, Haskell y Kotlin hacen hoy viene de ahí."

> "Haskell (1987-1990) llevó los ADTs, type classes y la ausencia de null al límite. TypeScript (2012) aplicó estas ideas al ecosistema JavaScript. Kotlin (2016) las aplicó a JVM con null safety por defecto. Rust (2015) resolvió los problemas de punteros sin GC con ownership."

**→ Transición:** "Tres preguntas para reflexionar."

---

### [F-55] Discusión — Diseño de sistemas de tipos

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Por qué TypeScript tiene strictNullChecks opt-in
- Cuándo discriminated unions vs. sealed class
- Qué pierde TypeScript con tipado estructural

**🗣 Guion docente:**
Abrir las tres preguntas para discusión. Guiar la clase hacia:

**Pregunta 1:** strictNullChecks opt-in → retrocompatibilidad con JS existente, adopción gradual. Es una decisión de adopción masiva, no de teoría.

**Pregunta 2:** Discriminated unions en TypeScript vs. sealed class Kotlin → TypeScript: más conciso para tipos simples. Kotlin: exhaustividad automática. Herencia tradicional: cuando necesitás extensión abierta (Open/Closed Principle).

**Pregunta 3:** Equivalencia estructural → gana flexibilidad, pierde seguridad semántica. `UserId` y `Email` son intercambiables sin branded types. Una librería de terceros puede satisfacer accidentalmente una interfaz sin intención.

**→ Transición:** "Hacia dónde vamos desde acá."

---

### [F-56] Conexión con próximos temas

**⏱ Tiempo:** 3 min

**🗣 Guion docente:**
> "T11 la próxima clase: expresiones y estructuras de control. Vamos a ver cómo las coerciones que hoy conceptualizamos aparecen en operadores aritméticos, sobrecarga de operadores y evaluación booleana."

> "Y en T14, más adelante, volvemos a los sistemas de tipos con base formal: el algoritmo Hindley-Milner que mencionamos, el λ-cálculo tipado, y la teoría del subtyping."

---

### [F-57] Consigna del TP

**⏱ Tiempo:** 3 min

**🗣 Guion docente:**
> "El TP asociado a este módulo es de exploración: eligen un lenguaje que no vimos en profundidad — Rust, Swift, Scala, Elm, Zig u otro aprobado — y documentan su sistema de tipos en comparación con TypeScript. La entrega es un repositorio con código de ejemplo y un informe en Markdown."

> "La fecha límite y todos los detalles están en la plataforma. Cualquier duda sobre la elección del lenguaje, consúltenme antes de arrancar."

---

### [F-58] Cierre y bibliografía

**⏱ Tiempo:** 3 min

**🗣 Guion docente:**
> "Hoy cubrimos el Módulo VII completo. Fuimos desde la definición más básica de tipo de dato hasta los sistemas de tipos como espacio de decisiones de diseño de lenguajes."

> "La bibliografía principal es el Capítulo 6 de Sebesta — lo vimos prácticamente completo. Louden §8.8–§8.9 para el polimorfismo formal. Para TypeScript en profundidad, el handbook oficial es excelente."

> "Próxima clase: T11 — Expresiones y Estructuras de Control."

---

## Notas de preparación

### Material a tener listo antes de clase
- [ ] TypeScript Playground abierto en browser (para demos en vivo: F-06, F-09, F-19, F-20, F-26, F-36, F-46, F-47)
- [ ] VSCode con proyecto TypeScript para F-37 y F-49
- [ ] Actividad F-14 proyectable o en papel
- [ ] Actividad F-28 proyectable o en papel
- [ ] Actividad F-39 proyectable o en papel
- [ ] Marcadores de colores para pizarra (mapa conceptual F-53)

### Ajustes de tiempo si hay retraso
- Si el Bloque 1 se extiende → comprimir F-11 y F-13 a 3 min cada uno
- Si el Bloque 2 se extiende → omitir F-23/F-24 (listas funcionales) o dejar como lectura
- Si el Bloque 3 se extiende → comprimir F-32 y F-33 a 4 min cada uno
- El Bloque 5 no debe acortarse — la síntesis es crítica para el cierre pedagógico

### Contexto adicional para consultas
- TypeScript Handbook (generics): https://www.typescriptlang.org/docs/handbook/2/generics.html
- Sebesta Cap. 6 tiene ejemplos en Ada y Fortran que pueden agregar color si hay tiempo
- Cardelli & Wegner 1985: "On understanding types, data abstraction, and polymorphism" — lectura opcional avanzada
