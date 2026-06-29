# Minuta de Clase — Tema 10
## Tipos de Datos y Sistemas de Tipos

> **Docente:** Matías Gel
> **Duración:** 360 minutos (clase unificada — Módulo VII completo)
> **Referencia:** `filminas.md` — F-00 a F-53
> **Uso:** Esta minuta es autocontenida. El docente puede conducir toda la clase usando solo este archivo.
> **Reconstrucción:** 2026-06-28 — fidelidad a `clase_dada.txt` (1122 líneas)

---

## Indicaciones generales

- **Ritmo:** 1 filmina cada ~6-7 minutos en promedio; las actividades tienen su tiempo propio
- **Código en vivo:** tener VSCode / TypeScript Playground abiertos para F-07, F-08, F-12, F-20, F-21, F-29, F-38, F-43, F-44
- **Pizarra:** reservar para F-02 (conexión T09→T10), F-49 (mapa conceptual integrador) y F-53 (Q&A)
- **Lenguaje principal:** TypeScript · contrastes puntuales en C, Kotlin, Haskell, Python

---

## Trazabilidad bibliográfica

> Las citas ChromaDB son respaldo para el docente — NO se muestran inline en filminas (regla: solo en minuta).

| Filmina | Sección .txt | Respaldo bibliográfico (ChromaDB) |
|---------|--------------|----------------------------------|
| F-04 | 26-37 | Sebesta §6.1 (definition of data type) — relevancia 0.6 |
| F-07 | 77-122 | Sebesta §6.2.1.1 (Integer) + §6.2 (Numeric Types) — relevancia 0.594 |
| F-08 | 123-172 | Sebesta §6.2.1 (Floating-point, info hiding) — relevancia 0.593 |
| F-10 | 199-218 | Sebesta §6.2.4 (Boolean) — relevancia 0.627 |
| F-13 | 263-301 | Sebesta §6.4.1 (Enumeration, C no type-safe) — relevancia 0.657 |
| F-16 | 384-414 | Sebesta §6.3 (Character String Types) — relevancia 0.67 |
| F-17 | 415-447 | Sebesta §6.5 (Array Types, Figura 6.2) — relevancia 0.492 |
| F-20 | 504-521 | Sebesta §6.8 (Associative Arrays) — relevancia 0.489 |
| F-23 | 565-585 | Sebesta §6.7 (Record Types) — relevancia 0.492 |
| F-24 | 587-601 | Sebesta §6.8 (Tuple Types) — relevancia 0.458 |
| F-26 | 616-665 | Sebesta §6.9 (List Types) — relevancia 0.492 |
| F-28 | 695-710 | Sebesta §6.10 (Union Types, fundamentally unsafe) — relevancia 0.691 |
| F-31 | 752-765 | Sebesta §6.11.1 (Pointer Types, nil) — relevancia 0.699 |
| F-32 | 766-779 | Sebesta §6.11.6 (Dangling pointers) + Gabbrielli §8.5 (Dangling references) — relevancia 0.735 |
| F-34 | 805-818 | Sebesta §6.11.5 (Reference Types) — relevancia 0.68 |
| F-37 | 982-987 | Sebesta §6.12 (Optional Types) — relevancia 0.613 |
| F-46 | 1047-1066 | Sebesta §6.13 (Type Checking) — relevancia 0.657 |
| F-47 | 1068-1095 | Sebesta §6.15 (Type Equivalence) — relevancia 0.693 + Gabbrielli §8.5 — relevancia 0.656 |
| F-41 | 877-890 | Louden §8.8 (Polymorphic Type Checking) — relevancia 0.767 + Gabbrielli §8.8 — relevancia 0.726 |
| F-43 | 911-931 | Louden §8.9 (Explicit Polymorphism) — relevancia 0.767 |

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
> "En T09 trabajamos con la 5-tupla de variables y el binding: cuándo se asocia un nombre a un tipo, a un valor, a una ubicación. Vimos binding estático, dinámico y gradual. Vimos scope, aliases."

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
- Definición formal de Sebesta §6.1

**🗣 Guion docente:**
> "La definición canónica es de Sebesta: un tipo de dato define una colección de valores y un conjunto de operaciones predefinidas sobre esos valores. Simple, pero poderosa."

> "¿Por qué los lenguajes incluyen tipos? Tres razones principales: **legibilidad** — el código expresa la intención; **detectabilidad de errores** — el compilador o runtime puede atrapar uso incorrecto; y **reusabilidad** — podemos abstraer comportamiento por tipo."

Dibujar el diagrama de los dos círculos superpuestos: valores y operaciones.

**Trazabilidad bibliográfica:** Sebesta §6.1 (relevancia ChromaDB 0.627) — *"A data type defines a collection of data values and a set of predefined operations on those values"*. Louden §8.1 también define el concepto de tipo.

**❓ Preguntas anticipadas:**
- *"¿`string` es primitivo?"* → Depende del lenguaje: en TypeScript sí (aunque con métodos via boxing). En Java es un objeto. Gran punto de diferencia.
- *"¿Las clases son tipos?"* → Sí — en OOP, cada clase define un tipo. Lo vemos en el Bloque 4.

**→ Transición:** "Veamos cómo se clasifican los tipos."

---

### [F-05] Clasificación de tipos

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- 6 grandes familias: primitivos, definidos por el usuario, compuestos, referenciales, algebraicos, paramétricos
- Hilo conductor: TypeScript con contrastes multilenguaje

**🗣 Guion docente:**
> "Los tipos se clasifican en seis grandes familias. Los **primitivos** son los más básicos — representaciones directas del hardware. Los **definidos por el usuario** los crea el programador: enums, subrangos, aliases, branded types. Los **compuestos** construyen valores más grandes a partir de otros tipos: arrays, registros, tuplas, uniones. Los **referenciales** son punteros y referencias. Los **algebraicos** combinan productos y sumas. Y los **paramétricos** son los generics."

> "Esta clasificación no es estricta — muchos tipos cruzan categorías. Pero nos da un mapa mental. Hoy vamos a recorrerlas en orden."

**→ Transición:** "Empecemos con los primitivos."

---

### [F-06] Tipos primitivos — Preguntas centrales

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Preguntas que guían el estudio de cada tipo primitivo
- Familias: numéricos, lógicos, texto elemental

**🗣 Guion docente:**
> "Los tipos primitivos son los más básicos — provistos por el lenguaje o la plataforma. Para estudiar cada uno, vamos a hacernos cinco preguntas: ¿qué valores representa?, ¿qué operaciones permite?, ¿cómo se almacena?, ¿qué errores puede detectar el compilador?, ¿qué queda delegado al runtime?"

> "Las familias son tres: **numéricos** (enteros, floating point, decimal, complex), **lógicos** (boolean), y **texto elemental** (char y string). Vamos una familia a la vez."

**→ Transición:** "Empecemos por los numéricos — los enteros."

---

### [F-07] Tipos numéricos — Enteros

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- Representación en complemento a 2, tamaños, rangos
- TypeScript `number` no distingue entero de float
- `bigint` para enteros de precisión arbitraria
- C: overflow es undefined behavior

**🗣 Guion docente:**
> "En C, los enteros son directos: `int` son 32 bits en complemento a 2, `long` son 64. El overflow es silencioso y wrappea — nadie te avisa. Peor aún: en C, el overflow de `int` es **undefined behavior** — el compilador puede hacer cualquier cosa."

> "En TypeScript, la situación es peculiar: **no hay tipo entero**. `number` es siempre un IEEE 754 de 64 bits — el mismo tipo que `double` en Java. Esto significa que `number` puede representar enteros exactamente hasta `Number.MAX_SAFE_INTEGER` = 2⁵³ − 1."

> "Para enteros más grandes existe `bigint` — precisión arbitraria, con literales que terminan en `n`. `9007199254740991n + 1n` funciona perfectamente."

Mostrar el bloque de complemento a 2 en pantalla. Recorrer los cuatro valores (+1, +42, -1, -42) bit a bit.

> "El bit más significativo es el signo: 0 positivo, 1 negativo. Por esto el rango no es simétrico: 2³¹ negativos pero solo 2³¹−1 positivos. El cero ocupa un lugar del lado positivo."

**Trazabilidad bibliográfica:** Sebesta §6.2.1.1 (Integer, complemento a 2). Louden §8.2 también discute representación numérica.

**❓ Preguntas anticipadas:**
- *"¿Por qué TypeScript no tiene int separado?"* → Herencia de JavaScript: JS siempre tuvo un solo tipo numérico. TypeScript es JS tipado, no un lenguaje nuevo.
- *"¿Qué pasa si desborda un `bigint`?"* → Solo lo limita la memoria disponible. Lento pero correcto.

**→ Transición:** "Y ahora el punto flotante — con la trampa que ya adelanté."

---

### [F-08] Tipos numéricos — Floating Point

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- IEEE 754 de 64 bits: signo + exponente + mantisa
- `0.1 + 0.2 !== 0.3` — mostrar en vivo
- TypeScript no tiene decimal nativo — usar `decimal.js` para finanzas
- Estructura de bits del double

**🗣 Guion docente:**
> "El estándar IEEE 754 define cómo se representan los números de punto flotante en binario. TypeScript `number` es *siempre* un double de 64 bits — no hay `float` de 32 bits como en Kotlin o Java."

Mostrar el diagrama ASCII de la estructura de 64 bits. Recorrer cada campo:
- **Signo:** 1 bit
- **Exponente:** 11 bits (desplazado en 1023)
- **Mantisa:** 52 bits

> "La fórmula es: valor = (−1)^signo × 1.mantisa × 2^(exponente−1023). Esto permite representar números muy grandes y muy pequeños, pero **no todos los decimales son representables exactamente**."

Abrir TypeScript Playground en vivo:
```
console.log(0.1 + 0.2)           // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3)  // false ← demostrar
```

> "¿Qué pasa? 0.1 en decimal no tiene representación finita en base 2 — es periódico, como 1/3 en decimal. La mantisa tiene tamaño limitado, así que se redondea. La suma hereda el error. **Esto pasa en cualquier lenguaje que use IEEE 754** — Python, Java, C, todos."

> "Para aplicaciones financieras donde la exactitud decimal es crítica — dinero, impuestos — TypeScript no tiene tipo decimal nativo. Se usa la librería `decimal.js`. Contraste: Java tiene `BigDecimal` en el JDK, Python tiene `decimal.Decimal` en la biblioteca estándar."

**Trazabilidad bibliográfica:** Sebesta §6.2.1 (Floating-point types, information hiding) — relevancia ChromaDB 0.593.

**❓ Preguntas anticipadas:**
- *"¿Esto pasa en todos los lenguajes?"* → Sí, en cualquier lenguaje que use IEEE 754. Python lo muestra igual. La diferencia es que algunos lenguajes incluyen decimal como tipo nativo (C#, Fortran).

**→ Transición:** "Veamos los tipos numéricos menos frecuentes pero interesantes por lo que revelan del diseño del lenguaje."

---

### [F-09] Tipos numéricos especiales — Complejo y Decimal

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Tipo complejo nativo vs. librería: decisión de diseño
- Decimal: evitar errores de floating point en finanzas

**🗣 Guion docente:**
> "Tipos interesantes que revelan decisiones de diseño: ¿deben los lenguajes incluir `complex` o `decimal` como tipos primitivos?"

> "Python eligió incluir `complex` como nativo: `3+4j` es un literal válido. Fortran también, porque es un lenguaje de cómputo científico. Java y TypeScript decidieron que es responsabilidad de una librería. ¿Cuál es mejor? Depende del dominio."

> "Para decimal: Python tiene `from decimal import Decimal` en la biblioteca estándar. Java/Kotlin tienen `BigDecimal` en el JDK. TypeScript depende de `decimal.js` como librería externa. **Idea central:** un lenguaje decide qué tipos incluye en su núcleo según sus prioridades: eficiencia, simplicidad, seguridad, precisión o dominio de aplicación."

**→ Transición:** "Boolean y Char muestran decisiones de diseño aún más diversas."

---

### [F-10] Boolean y Char

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- C no tiene tipo boolean real — consecuencias en legibilidad
- TypeScript no tiene `char` — solo `string`
- Python: `bool` es subtipo de `int`

**🗣 Guion docente:**
> "Boolean y Char parecen simples, pero revelan mucha decisión de diseño."

> "En TypeScript, `boolean` es un tipo real con dos valores: `true` y `false`. En C clásico, no existe tipo boolean — cualquier entero distinto de 0 es 'verdadero'. Eso genera código como `if (ptr)` que puede sorprender."

> "Char es aún más interesante. TypeScript directamente **no tiene tipo char**. Un carácter es una `string` de longitud 1. Es una decisión pragmática heredada de JavaScript. En Kotlin, `Char` es un tipo real de UTF-16. En C, `char` es un byte — ni siquiera representa Unicode."

> "Dato curioso de Python: `bool` es subtipo de `int`. `True == 1` da `True`. Eso hereda de la decisión de Python de hacer todo objeto y de la transición histórica de C sin boolean."

**Trazabilidad bibliográfica:** Sebesta §6.2.4 (Boolean types) — *"Boolean types are perhaps the simplest of all types... One popular exception is C89, in which numeric expressions can be used as if they were Boolean"* — relevancia ChromaDB 0.627.

**❓ Preguntas anticipadas:**
- *"¿Cómo trabajo con caracteres individuales en TypeScript?"* → `"hola"[0]` retorna `"h"` — una string de longitud 1.

**→ Transición:** "Pasamos a los tipos ordinales definidos por el usuario — primero la definición general."

---

### [F-11] Tipos ordinales y dominios finitos

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Definición de tipo ordinal
- Propiedades: discretos, sucesor/predecesor, comparación, rangos
- Permiten modelar dominios finitos o restringidos

**🗣 Guion docente:**
> "Un tipo ordinal tiene valores discretos que pueden enumerarse y, en muchos lenguajes, ordenarse. Ejemplos: boolean, char, integer, enum, subrange."

> "Las propiedades clave: valores discretos, existe sucesor y predecesor, se pueden comparar por orden, y permiten definir rangos válidos."

> "La idea central: los tipos ordinales permiten que el sistema de tipos modele dominios finitos o restringidos. En vez de aceptar cualquier entero para un día del mes, puedo restringir a 1..31."

**→ Transición:** "El ejemplo más usado de tipo ordinal definido por el usuario: las enumeraciones en TypeScript."

---

### [F-12] Enum TypeScript

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Numeric enum, string enum, const enum
- TypeScript: type-safe a diferencia de C
- `const enum` para inlining en compilación

**🗣 Guion docente:**
> "Los enums de TypeScript son un tipo de primera clase. `enum Direction { Up, Down, Left, Right }` crea un tipo real — no se puede pasar `42` donde se espera `Direction`."

Mostrar código en pantalla:
```typescript
enum Direction { Up, Down, Left, Right }
function move(dir: Direction) { ... }
```

> "String enums son para interoperabilidad con APIs: `enum Status { Active = 'active' }` compila a `'active'` en runtime. Numeric enums aceptan el número subyacente — un gotcha importante."

> "`const enum` es una optimización: el compilador reemplaza cada uso por el valor literal. Sin objeto en runtime — zero overhead."

**→ Transición:** "Comparemos con C, Kotlin y Haskell para ver cuánto varían."

---

### [F-13] Enumeraciones — Comparación multilenguaje

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- C: no type-safe — es un int con alias
- Kotlin: `enum class` con propiedades y métodos
- Haskell: ADT más poderoso

**🗣 Guion docente:**
> "La tabla resume las diferencias. El punto clave de Sebesta §6.4.1: el problema de los enums en C es que **no son type-safe**. `enum Direction { UP, DOWN }` en C es esencialmente un `int` con nombres. Puedes hacer `int x = UP + 5` y el compilador no se queja."

> "Kotlin va en la dirección opuesta: `enum class` puede tener propiedades y métodos. Cada valor de la enum puede tener comportamiento diferente. TypeScript está en el medio — type-safe pero sin propiedades por valor."

> "Haskell va más lejos: `data Color = Red | Green | Blue` es un ADT completo con pattern matching exhaustivo."

**Trazabilidad bibliográfica:** Sebesta §6.4.1 (Enumeration Types) — relevancia ChromaDB 0.657: *"C# enumeration types are like those of C++, except that they are never coerced to integer"*. Gabbrielli §8.3.7 también trata enumerations.

**→ Transición:** "Hay otro tipo ordinal definido por el usuario: los subrangos."

---

### [F-14] Rangos y subrangos — ejemplo Python

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Diferencia entre rango (selección) y subrango (restricción de tipo)
- Pascal y Ada tienen subrangos nativos
- Python: solo `range` — sin tipo subrango nativo, requiere validación explícita

**🗣 Guion docente:**
> "Un rango es una porción contigua de valores dentro de un tipo ordinal: `1..10`, `'a'..'z'`. Un subrango es un **tipo** cuyo dominio queda restringido a un rango."

> "Pascal y Ada tienen subrangos nativos: `type Nota = 0..10` crea un tipo real, el compilador rechaza asignar `15` a una variable `Nota`."

> "Python tiene `range(0, 11)` que representa los valores 0 a 10, pero **no crea un tipo**. `nota = 15` sigue siendo válido para Python. Para modelar un subrango, hay que programar la validación explícitamente con una clase que rechace valores fuera de rango en el constructor."

> "TypeScript lo simula con literal unions: `type Day = 1|2|3|4|5`. El compilador **sí** rechaza `const d: Day = 6`. No es un subrango en el sentido de Pascal, pero logra el mismo nivel de seguridad estática."

**Trazabilidad bibliográfica:** Louden §8.2 — *"Languages in the C family (C, C++, Java) do not have subrange types, since the same effect can be achieved using enumerated types"* — relevancia ChromaDB 0.503. Gabbrielli §8.3.9 (Intervals) — relevancia 0.529.

**→ Transición:** "Bloque 2 — tipos compuestos. Arrancamos con la clasificación general."

---

## BLOQUE 2 — Tipos de Agregación y Colecciones (90 min)

---

### [F-15] Tipos compuestos

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- 4 formas principales: producto, secuencia, mapeo, suma
- Cada forma tiene múltiples implementaciones en lenguajes

**🗣 Guion docente:**
> "Un tipo compuesto construye valores más grandes a partir de otros tipos. Hay cuatro formas principales."

> "**Producto**: varios campos simultáneos — record, struct, tuple, object. **Secuencia**: colección ordenada — array, list, string. **Mapeo**: asociación clave-valor — map, dictionary. **Suma/unión**: una alternativa entre varias formas — union, discriminated union, sealed class, ADT."

> "Estas cuatro formas algebraicas son la base de todos los tipos compuestos que veremos. La mayoría de los lenguajes las implementan de manera distinta, pero la estructura conceptual es la misma."

**→ Transición:** "Empecemos por las secuencias de texto: strings."

---

### [F-16] Strings — secuencias de texto

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- TypeScript: string primitivo + inmutable + comparación por valor con `===`
- Java: ERROR clásico con `==` (compara referencia)
- C: puntero a char — comparar con `strcmp`, no con `==`
- Sebesta §6.3: operaciones más comunes

**🗣 Guion docente:**
> "Los strings parecen simples hasta que comparás. El error clásico en Java: `str1 == str2` compara **referencias**, no contenido. Hay que usar `.equals()`. En TypeScript, `===` compara por **valor** siempre — no hay surpresas."

> "En C, una string es directamente un puntero a un array de chars terminado en `\0`. Comparar con `==` compara las direcciones, no el contenido. Hay que usar `strcmp()`."

> "TypeScript hereda de JavaScript: `string` es primitivo pero el runtime hace autoboxing para permitir llamar métodos como `.toUpperCase()`. El resultado siempre es una nueva string — son inmutables."

**Trazabilidad bibliográfica:** Sebesta §6.3 (Character String Types) — relevancia ChromaDB 0.67: *"A character string type is one in which the values consist of sequences of characters"*. Operaciones: *"assignment, concatenation, substring reference, comparison, and pattern matching"* — relevancia 0.554.

**→ Transición:** "Pasamos a los tipos más usados en programación: los arrays."

---

### [F-17] Arrays — Taxonomía por binding time

**⏱ Tiempo:** 8 min

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

**Trazabilidad bibliográfica:** Sebesta §6.5 (Array Types) — relevancia ChromaDB 0.492.

**→ Transición:** "Ahora algo que pocos piensan: cómo se accede a un array multidimensional en memoria."

---

### [F-18] Arrays — Función de acceso multidimensional

**⏱ Tiempo:** 6 min

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

### [F-19] Arrays — Rectangulares vs. Jagged + Slices

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Rectangular (C#, Fortran): todos los sub-arrays de igual longitud
- Jagged (Java, C, TypeScript): array de referencias/punteros a arrays
- Slices: referencia sin copia — diferente en Python vs. Kotlin vs. Go

**🗣 Guion docente:**
> "Java hizo una decisión de diseño: todos los arrays multidimensionales son jagged. `int[][] a = new int[3][4]` es en realidad un array de 3 referencias, cada una apuntando a un array de 4 ints. Esto implica una indirección extra pero permite filas de distinto tamaño."

> "Las slices son un tema relacionado: en Python, `lista[1:4]` produce una **nueva lista** (copia). En Kotlin, `lista.subList(1, 4)` produce una **vista viva** — si modificás la vista, modificás la original. En Go, las slices son ciudadanos de primera clase con length y capacity separados."

**→ Transición:** "Arrays asociativos — o mapeos finitos."

---

### [F-20] Arrays asociativos — Maps

**⏱ Tiempo:** 5 min

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

**Trazabilidad bibliográfica:** Sebesta §6.8 (Associative Arrays) — relevancia ChromaDB 0.489: *"An associative array is an unordered collection of data elements that are indexed by an equal number of values called keys"*.

**→ Transición:** "Código completo de arrays en TypeScript."

---

### [F-21] Arrays en TypeScript — cuatro formas

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Cuatro formas de crear arrays en TypeScript
- `ReadonlyArray<T>` para inmutabilidad
- `Int32Array` para rendimiento sin boxing

**🗣 Guion docente:**
Recorrer el código comentando cada variante:

> "El array más común es el dinámico: `const lista: number[] = [1, 2, 3]` con `push()`. El `new Array(5).fill(0).map(...)` es útil cuando necesitamos tamaño inicial conocido."

> "Los `TypedArrays` como `Int32Array` son para manipulación de buffers binarios o WebGL — sin el overhead de boxing de los arrays genéricos. No tienen `push()` — tamaño fijo. Lo vemos en detalle en la próxima."

> "`ReadonlyArray<T>` es solo a nivel de tipos — el compilador rechaza mutaciones, pero en runtime es un array normal."

**→ Transición:** "TypedArrays — por qué son distintos."

---

### [F-22] TypedArrays — almacenamiento binario directo

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- `number[]` guarda doubles de 64 bits envueltos (boxed) — overhead de memoria
- `Int32Array` almacena enteros en binario puro, 4 bytes por elemento
- ArrayBuffer — bloque de bytes crudos
- Cuándo usar TypedArrays: WebGL, imagen, comunicación binaria, alto rendimiento

**🗣 Guion docente:**
> "¿Por qué `Int32Array` no es lo mismo que `number[]`? En JavaScript/TypeScript, cada `number` es siempre un double IEEE 754 de 64 bits, envuelto en un objeto del motor V8. Eso es costoso."

> "Un TypedArray como `Int32Array` almacena enteros en binario puro, 4 bytes por elemento, en un `ArrayBuffer` — bloque de bytes crudos en memoria. Sin boxing, sin overhead."

Mostrar la tabla de la familia de TypedArrays. Recorrer los tipos principales:
- `Int8Array`, `Uint8Array`: 1 byte por elemento
- `Int16Array`, `Uint16Array`: 2 bytes
- `Int32Array`, `Uint32Array`: 4 bytes
- `Float32Array`: 4 bytes (precisión simple)
- `Float64Array`: 8 bytes — equivalente a `number`

> "¿Cuándo usarlos? Procesamiento de imagen con `Uint8ClampedArray` para píxeles en Canvas, WebGL/shaders donde la GPU requiere tipos binarios exactos, comunicación binaria por WebSocket o FileReader, algoritmos numéricos de alto rendimiento donde la memoria contigua reduce cache misses."

**→ Transición:** "De arrays a registros y estructuras."

---

### [F-23] Registros — `interface` y `type` en TypeScript

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Registro: colección de campos heterogéneos identificados por nombre
- `interface` vs `type`: diferencias sutiles (extensibilidad vs. expresividad)
- `readonly` para inmutabilidad
- Contraste con Kotlin `data class` — genera métodos automáticos

**🗣 Guion docente:**
> "Un registro es una colección de campos identificados por nombre — Sebesta §6.6. En TypeScript, usamos `interface` o `type`."

> "La diferencia práctica: `interface` puede ser extendida (`extends`) y augmentada después de declararse (declaration merging). `type` puede expresar uniones y tipos más complejos. Para objetos simples, son intercambiables."

> "En Kotlin, `data class` genera automáticamente `equals`, `hashCode`, `toString` y `copy()`. TypeScript no tiene nada equivalente — hay que implementarlos manualmente o usar librerías."

**Trazabilidad bibliográfica:** Sebesta §6.7 (Record Types) — relevancia ChromaDB 0.492: *"Records are frequently valuable data types in programming languages. The design of record types is straightforward, and their use is safe"*. Sebesta §6.7.3: *"Records and arrays are closely related structural forms"*.

**→ Transición:** "Ahora tuplas — el producto cartesiano formal."

---

### [F-24] Tuplas en TypeScript

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Tupla como producto cartesiano formal: A × B
- TypeScript: tuplas literales tipadas, desestructuración
- Contraste: Kotlin `Pair`/`Triple`, Python tuplas inmutables

**🗣 Guion docente:**
> "Una tupla es formalmente el producto cartesiano: `A × B` = todos los pares `(a, b)` donde `a: A` y `b: B`. TypeScript los expresa como `[string, number]`."

Mostrar desestructuración: `const [nombre, edad] = par` — muy usada en React hooks y retornos múltiples.

> "Kotlin tiene `Pair<A,B>` y `Triple<A,B,C>` — solo hasta 3 elementos nativos. Python tiene tuplas inmutables `(a, b, c)` por defecto. Haskell tiene tuplas como tipos algebraicos nativos. TypeScript las hace con tipos literales."

**Trazabilidad bibliográfica:** Sebesta §6.8 (Tuple Types) — relevancia ChromaDB 0.458: *"A tuple is a data type that is similar to a record, except that the elements are not named"*.

**→ Transición:** "Antes de pasar a uniones, veamos el ADT de Haskell — que combina producto y suma."

---

### [F-25] Tipos algebraicos de datos en Haskell

**⏱ Tiempo:** 4 min

**🎯 Conceptos clave:**
- ADT: conjunto cerrado de variantes
- `data Resultado = Exito String | Error String | Cargando`
- Pattern matching con `case`

**🗣 Guion docente:**
> "Haskell permite definir tipos algebraicos de datos con la palabra clave `data`. Un ADT define un nuevo tipo a partir de un conjunto cerrado de variantes posibles."

Mostrar el código Haskell:
```haskell
data Resultado = Exito String | Error String | Cargando

mostrar resultado = case resultado of
  Exito valor   -> "Valor recibido: " ++ valor
  Error mensaje -> "Error: " ++ mensaje
  Cargando      -> "Cargando..."
```

> "Cada variante es un constructor distinto. El `case` pattern matching es exhaustivo — si falta un caso, el compilador avisa. Esto es la base conceptual de las uniones discriminadas que veremos en TypeScript."

**→ Transición:** "Listas funcionales — otro tipo secuencial con semántica distinta."

---

### [F-26] Listas funcionales — Definición y multilenguaje

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Origen en LISP 1958: head, tail, cons
- Recursividad inherente: lista = head + tail (otra lista)
- Diferencia O(1) vs. O(n) con arrays
- Implementaciones multilenguaje: TS es array, no lista

**🗣 Guion docente:**
> "Las listas funcionales vienen de LISP, 1958. La operación fundamental es `cons`: construye una lista añadiendo un elemento al frente. La lista `[1, 2, 3]` en LISP era `cons(1, cons(2, cons(3, nil)))`."

> "En Haskell, los tipos lista son la estructura de datos principal. `head xs` retorna el primer elemento, `tail xs` retorna el resto, `x:xs` construye una lista añadiendo `x` al frente."

> "La diferencia clave con arrays: acceso aleatorio en lista enlazada es O(n) — hay que recorrer desde el inicio. Arrays tienen O(1). Pero inserción al frente de lista enlazada es O(1) — arrays requieren O(n) para desplazar."

> "Dato importante: Python `list` es en realidad un array dinámico, no una lista enlazada. Tiene acceso O(1) por índice. Haskell `[a]` sí es una lista enlazada real, inmutable, con pattern matching. En TypeScript, `T[]` es un array dinámico. `ReadonlyArray<T>` lo hace inmutable."

**Trazabilidad bibliográfica:** Sebesta §6.9 (List Types) — relevancia ChromaDB 0.492: *"Lists are collections of data that can have varying numbers of elements and to which elements can be easily added or removed from either end"*.

**→ Transición:** "Ahora las uniones — desde la inseguridad de C hasta la elegancia de TypeScript. Primero el marco algebraico."

---

### [F-27] Tipos algebraicos: producto vs. suma

**⏱ Tiempo:** 4 min

**🎯 Conceptos clave:**
- Producto = combinación (todos los campos) — record, struct, tuple
- Suma = alternativa (uno de los campos, discriminado) — union, ADT

**🗣 Guion docente:**
> "Antes de ver uniones, formalicemos las dos operaciones algebraicas fundamentales sobre tipos."

> "**Producto**: un valor contiene A **y** B simultáneamente. `type Punto = { x: number; y: number }` es el producto `number × number`. Un record o struct es un producto."

> "**Suma**: un valor puede ser A **o** B, discriminado por una etiqueta. `type Resultado = { kind: 'ok', value: number } | { kind: 'error', message: string }` es la suma `Ok + Error`. Una unión es una suma."

> "Idea central: producto = combinación, suma = alternativa. Las dos operaciones algebraicas básicas."

**→ Transición:** "Empecemos por las uniones inseguras de C."

---

### [F-28] Uniones libres (unsafe) — C `union`

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- C `union`: comparte espacio de memoria entre campos
- Sin forma de verificar qué campo fue escrito
- Bit pattern: los mismos 4 bytes reinterpretados
- Fuente de bugs difíciles de detectar

**🗣 Guion docente:**
> "En C, un `union` permite que distintos tipos compartan el mismo espacio de memoria. Si escribiste el campo `i` y lees el campo `f` — estás interpretando los mismos bits como un float. El resultado es basura."

> "Sebesta lo llama 'fundamentally unsafe'. El programador tiene que recordar qué campo es válido — el lenguaje no puede ayudar. Esto generó décadas de bugs."

Código en pantalla: `d.i = 42; printf("%f\n", d.f)` — destacar el acceso incorrecto.

> "¿Qué es un bit pattern? Cuando se escribe `d.i = 42`, los 4 bytes de la unión toman el patrón binario del entero 42. Al leer `d.f`, esos mismos 4 bytes se reinterpretan como un float IEEE 754. No se convierte el valor — se leen los mismos bits con otra semántica. El resultado es basura aritmética, y el programa continúa sin lanzar ningún error."

> "Este es el peligro de las uniones en C: el compilador no sabe qué campo está 'activo'. Las uniones discriminadas (TypeScript `kind`, Kotlin `sealed`) resuelven esto al nivel del sistema de tipos."

**Trazabilidad bibliográfica:** Sebesta §6.10 (Union Types) — relevancia ChromaDB 0.691: *"Type checking of unions requires that each union construct include a type indicator. Such an indicator is called a tag, or discriminant, and a union with a discriminant is called a discriminated union. The first language to provide discriminated unions was ALGOL 68"*.

**→ Transición:** "La solución moderna: uniones discriminadas."

---

### [F-29] Uniones discriminadas (safe) — TypeScript

**⏱ Tiempo:** 6 min

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

> "Dentro del case 'success', TypeScript **sabe** que `r` es `{ kind: 'success'; value: number }`. Este es el narrowing de tipos en acción. El compilador hace el trabajo que en C tendría que hacer el programador."

**❓ Preguntas anticipadas:**
- *"¿Cómo sé si todos los casos están cubiertos?"* → Usar el `never` trick: añadir `default: const _exhaustive: never = r` — si se agrega una nueva variante y no se maneja, el compilador da error.

**→ Transición:** "Comparemos con Kotlin y Haskell."

---

### [F-30] Uniones discriminadas — Tres implementaciones

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Kotlin `sealed class`: exhaustividad garantizada automáticamente por el compilador en `when`
- Haskell ADT: pattern matching exhaustivo
- TypeScript requiere `never` trick — los otros dos lo hacen por diseño

**🗣 Guion docente:**
> "En Kotlin, `sealed class` hace la exhaustividad automática. Si tenés un `when` sobre un `sealed class` y te falta un caso, el compilador te da error. No tenés que hacer ningún trick."

> "En Haskell, el pattern matching sobre ADTs es exhaustivo por construcción — el compilador avisa sobre casos no cubiertos."

> "La diferencia es que TypeScript requiere esfuerzo explícito (el `never` trick o la opción del compilador); Kotlin y Haskell lo hacen por diseño."

**Trazabilidad bibliográfica:** Gabbrielli §8.4.3 (Tagged Unions) — relevancia ChromaDB 0.682: *"A tagged union is the union of several other types, where, however, each value maintains trace of the original type it comes from. It is the modern evolution of Algol 68's unions"*.

**→ Transición:** "Bloque 3 — pasamos al nivel de la memoria con punteros."

---

## BLOQUE 3 — Punteros, Null Safety y Tipos Recursivos (75 min)

---

### [F-31] Tipo puntero — Definición y semántica

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- Puntero = dirección de memoria + valor especial `nil`
- Operaciones: `&` (toma dirección), `*` (derreferencia), aritmética
- Usos legítimos: heap, paso por referencia, estructuras dinámicas

**🗣 Guion docente:**
> "Un puntero es un valor que contiene una dirección de memoria. No es el valor en sí — es la dirección donde vive el valor."

Dibujar en pizarra: variable `ptr` con valor `0x1A2B3C` → flecha a una celda de heap con valor `42`.

> "En C: `int* ptr = &x` — el `&` toma la dirección de `x`; `*ptr` — el `*` desreferencia: accede al valor en esa dirección. `ptr++` avanza al siguiente `int` en memoria — aritmética de punteros."

> "Sebesta §6.11.1 lo define: 'Una variable de tipo puntero tiene un rango de valores que consiste en direcciones de memoria y un valor especial, nil'. El nil es el null pointer — cuando el puntero no apunta a nada."

> "Los usos legítimos son tres: manejo indirecto de datos en heap, paso eficiente de estructuras grandes (en lugar de copiar), y construcción de estructuras dinámicas como listas enlazadas o árboles."

**Trazabilidad bibliográfica:** Sebesta §6.11.1 (Pointer Types) — relevancia ChromaDB 0.699: *"A pointer type variable has a range of values that consists of memory addresses and a special value, nil"*.

**❓ Preguntas anticipadas:**
- *"¿TypeScript tiene punteros?"* → No en la superficie — lo vemos en las próximas filminas con referencias.

**→ Transición:** "Los punteros también generan problemas clásicos difíciles de debuggear."

---

### [F-32] Punteros — Problemas clásicos

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Dangling pointer, memory leak, double free, null dereference, buffer overflow
- Cinco problemas clásicos que motivan GC y sistemas de tipos modernos

**🗣 Guion docente:**
Recorrer la tabla fila a fila con un ejemplo breve de cada:

- **Dangling pointer:** `free(ptr); *ptr = 5;` — ya liberaste esa memoria; otro objeto puede estar ahí. Sebesta: *"A dangling pointer is a pointer that contains the address of a heap-dynamic variable that has been deallocated"*.
- **Memory leak:** olvidar llamar `free()` — la memoria nunca vuelve al sistema. En procesos largos, crece indefinidamente.
- **Double free:** llamar `free(ptr)` dos veces — comportamiento indefinido, puede corromper el heap.
- **Null dereference:** `*NULL` → crash con SIGSEGV.
- **Buffer overflow:** `int a[5]; a[10] = 0;` — sobreescribe memoria adyacente. Causa de vulnerabilidades de seguridad históricas (CVE, shellcode).

> "Estos cinco problemas son la principal motivación histórica para los lenguajes con GC y los sistemas de tipos modernos. El GC resuelve los tres primeros; los sistemas de tipos modernos (Rust, Kotlin, TypeScript con strict) previenen el null dereference."

**Trazabilidad bibliográfica:** Sebesta §6.11.6 (Dangling pointers) — relevancia 0.688. Gabbrielli §8.5 (Dangling references) — relevancia ChromaDB 0.735: *"If a language allows dangling references to happen, it is obvious that it cannot be type safe"*.

**→ Transición:** "¿Cómo se intentaron resolver estos problemas históricamente?"

---

### [F-33] Soluciones históricas — Tombstones y Locks

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Tombstones: marcador de objeto liberado
- Locks and Keys: verificación de clave al acceder
- Soluciones modernas: GC (Java, JS/TS, Python, Go) y ownership (Rust)

**🗣 Guion docente:**
> "Sebesta §6.11.4 documenta dos soluciones históricas."

> "**Tombstones**: cada objeto heap tiene un tombstone (marcador). Al liberar, el tombstone se marca como 'liberado'. Los punteros apuntan al tombstone, no al objeto directo. Al acceder: si el tombstone está marcado → error en lugar de basura."

> "**Locks and Keys**: cada puntero lleva una clave. Cada bloque de heap tiene un lock. Al acceder: se verifica que la clave coincida con el lock del bloque. Si no coinciden → acceso denegado (error detectable)."

> "Estas soluciones tienen overhead de memoria y rendimiento. El GC las reemplazó en la mayoría de los lenguajes modernos. Rust toma otro camino: ownership y borrow checker — verificación en compilación sin GC, sin overhead en runtime."

**Trazabilidad bibliográfica:** Sebesta §6.11.4 documenta Tombstones y Locks and Keys como soluciones históricas para dangling pointers.

**→ Transición:** "Una distinción importante: referencias vs. punteros."

---

### [F-34] Referencias vs. Punteros

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Referencia = alias constante implícitamente dereferenciado
- No hay aritmética, no puede ser null (en C++)
- TypeScript/Kotlin: referencias gestionadas por GC

**🗣 Guion docente:**
> "Sebesta §6.11.5: 'Una variable de referencia es un puntero constante que siempre se desreferencia implícitamente'. En C++, `int& r = x` es un alias que siempre apunta al mismo objeto — no se puede reasignar y no puede ser null."

> "La tabla muestra las diferencias entre tres modelos: puntero de C (con aritmética), referencia de C++ (sin aritmética, sin null, constante), y referencias de JS/TS/Kotlin (reasignables, nullables con tipo, GC)."

> "En TypeScript, todas las variables de objeto son referencias implícitas. Cuando escribís `const obj = { x: 1 }` y pasás `obj` a una función, pasás una referencia — la función puede modificar el objeto. Pero no podés hacer aritmética de punteros ni hay `*` explícito. El GC se encarga de todo — sin `free()`, sin `delete`."

**Trazabilidad bibliográfica:** Sebesta §6.11.5 (Reference Types) — relevancia ChromaDB 0.68: *"A reference variable is a constant pointer that is always implicitly dereferenced"*.

**→ Transición:** "Ahora tipos recursivos — donde los tipos se definen a sí mismos."

---

### [F-35] Tipos recursivos — Definición

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Un tipo que se define en términos de sí mismo
- Posible porque el campo recursivo es una referencia (tamaño fijo), no el objeto completo

**🗣 Guion docente:**
> "Un tipo recursivo se define en términos de sí mismo. La lista enlazada clásica en C: un nodo tiene un valor y un puntero al siguiente nodo. El nodo es del tipo `Node`, y tiene dentro un puntero a `Node`."

> "¿Por qué esto es posible? Porque `Node*` tiene tamaño fijo (el tamaño de un puntero) independientemente del tamaño de `Node`. Si fuera `struct Node { int value; struct Node next; }` — sin puntero — el compilador calcularía un tamaño infinito."

> "Haskell lo expresa elegantemente: `data List a = Nil | Cons a (List a)` — una lista es o la lista vacía o un elemento seguido de otra lista. Es isomorfo al tipo built-in `[a]`."

**→ Transición:** "En TypeScript, los tipos recursivos son elegantes gracias a las uniones discriminadas."

---

### [F-36] Tipos recursivos — Árbol binario en TypeScript

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Árbol binario como union discriminada recursiva
- Función `depth` que explota la estructura recursiva
- Contraste con Kotlin `sealed class`

**🗣 Guion docente:**
> "TypeScript permite tipos recursivos directamente en la definición de tipos alias. `BinaryTree<T>` es o una hoja o un nodo con valor y dos sub-árboles del mismo tipo."

Mostrar `depth()` en vivo: "La función es recursiva exactamente como el tipo. El case 'leaf' es el caso base. El case 'node' llama a `depth()` en ambos sub-árboles."

```typescript
function depth<T>(t: BinaryTree<T>): number {
  if (t.kind === 'leaf') return 0
  return 1 + Math.max(depth(t.left), depth(t.right))
}
```

> "Kotlin logra lo mismo con `sealed class Tree<T>` — la recursión es en los parámetros del constructor. Haskell con ADT es lo mismo conceptualmente."

> "La relación clave: tipos recursivos + uniones discriminadas = estructuras inductivas. Esto es la base de Haskell, Kotlin sealed y TypeScript."

**→ Transición:** "El problema del null — uno de los errores de diseño más costosos de la historia."

---

### [F-37] El problema del null

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Tony Hoare: "my billion-dollar mistake"
- El problema: cualquier referencia puede ser null sin que el tipo lo diga
- La solución: hacer null parte del sistema de tipos

**🗣 Guion docente:**
> "En 1965, Tony Hoare introdujo el null pointer en ALGOL W. En 2009, en la conferencia QCon, lo llamó 'my billion-dollar mistake': llevó a incontables errores, vulnerabilidades y crashes de sistemas."

> "El problema es conceptual: en Java, una variable de tipo `String` puede contener una string válida **o** el valor especial `null`. El tipo no lo distingue. El error solo aparece en runtime cuando intentás usar el `null` como si fuera una string."

Mostrar código Java problemático:
```java
String nombre = getUser().getName();  // puede retornar null
nombre.toUpperCase();                  // NullPointerException en runtime ❌
```

> "La solución es hacer que el sistema de tipos distinga: un tipo que puede ser null vs. uno que no puede. Kotlin y TypeScript (con `strictNullChecks`) lo hacen. Haskell lo hace con `Maybe`. Rust con `Option`."

**Trazabilidad bibliográfica:** Sebesta §6.12 (Optional Types) — relevancia ChromaDB 0.613: *"There are situations in programming when there is a need to be able to indicate that a variable does not currently have a value. Some older languages use zero as a nonvalue for numeric variables. This approach has the disadvantage of not being able to distinguish between when the variable is supposed to have the value zero and when it has no value"*.

**→ Transición:** "Operadores de null safety en TypeScript."

---

### [F-38] TypeScript Null Safety — Operadores + código completo

**⏱ Tiempo:** 12 min

**🎯 Conceptos clave:**
- `strictNullChecks: true` activa el sistema
- `T | null`, `?.`, `??`, `!`, narrowing
- Tabla de operadores + código completo

**🗣 Guion docente:**
Recorrer la tabla de operadores:

> "Con `strictNullChecks: true`, TypeScript distingue `string` (nunca null) de `string | null` (puede ser null). La declaración del tipo dice la verdad."

> "`?.` — optional chaining: si `x` es null, retorna `undefined` en lugar de lanzar error. `x?.prop` es equivalente a `x !== null ? x.prop : undefined`."

> "`??` — nullish coalescing: si la expresión izquierda es null o undefined, usa la derecha. `user.email ?? 'sin email'`."

> "`x!` — non-null assertion: le decís al compilador 'confía en mí, esto no es null'. Si te equivocas, el error ocurre en runtime. Usar solo cuando tenés certeza externa que el compilador no puede verificar."

Mostrar código en vivo, ejecutar en TypeScript Playground:

```typescript
interface User { name: string; email: string | null }
function sendEmail(user: User) {
  const dest = user.email ?? 'sin email'
  const upper = user.email?.toUpperCase()
  if (user.email !== null) {
    console.log(`Enviando a ${user.email.toUpperCase()}`)
  }
}
```

> "`user.email ?? 'sin email'` — si email es null, usa el string por defecto. Esto es el 'Elvis operator' que vienen de Groovy/Kotlin."

> "`user.email?.toUpperCase()` — si email es null, retorna `undefined` en lugar de lanzar. No es necesario el `if !== null` para este caso."

> "El `if (user.email !== null)` hace narrowing — dentro del bloque, TypeScript *sabe* que `email` es `string` (no `string | null`). Puede usar `.toUpperCase()` directamente."

> "Con `strict: true`, el compilador **rechaza** acceder a `user.email.toUpperCase()` directamente — te fuerza a verificar primero. Eso es exactamente lo que Tony Hoare pidió 40 años tarde."

**→ Transición:** "Comparemos con Kotlin y otros lenguajes."

---

### [F-39] Null Safety — Comparación multilenguaje

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- Kotlin: null safety por diseño, siempre activado
- TypeScript: opt-in con `strictNullChecks`
- Tabla de operadores equivalentes TS ↔ Kotlin
- Haskell `Maybe` y Rust `Option` — type-safe por diseño

**🗣 Guion docente:**
> "La gran diferencia de diseño: Kotlin activó null safety desde el día uno. TypeScript lo hizo opt-in por retrocompatibilidad con código JavaScript existente. Un proyecto TypeScript sin `strict: true` tiene null safety apagado."

> "Los operadores son casi idénticos: `?.` en ambos, `??` en TS = `?:` en Kotlin (Elvis), `!` en TS = `!!` en Kotlin."

> "Haskell y Rust van más lejos: no tienen null en absoluto. Haskell usa `Maybe a = Nothing | Just a` — una mónada. Rust usa `Option<T> = None | Some(T)`. El sistema de tipos te obliga a manejar el caso 'sin valor' explícitamente."

> "Conexión con T02 (mónadas): `Maybe`/`Option` es la mónada de null safety — `flatMap` = `?.` encadenado. El `?.` en TypeScript es esencialmente bind/flatMap sobre `T | null`."

**→ Transición:** "Bloque 4 — sistemas de tipos en profundidad."

---

## BLOQUE 4 — Sistemas de Tipos: Monomórficos, Polimórficos y Strong Typing (80 min)

---

### [F-40] Sistemas monomórficos

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Cada expresión: exactamente un tipo
- Limitación: código duplicado para cada tipo → motivación para polimorfismo
- Ventajas: simple, predecible, sin overhead

**🗣 Guion docente:**
> "En un sistema monomórfico, cada expresión tiene exactamente un tipo. C sin templates es el ejemplo clásico: si querés `max` para enteros y para floats, necesitás dos funciones distintas con el mismo código duplicado."

```c
int max_int(int a, int b) { return a > b ? a : b; }
float max_float(float a, float b) { return a > b ? a : b; }
```

> "Las ventajas: simple y predecible, herramientas de análisis directas, sin overhead de polimorfismo. La limitación es clara: código duplicado. No escala a bibliotecas grandes."

> "Esta limitación es la motivación histórica para el polimorfismo — quiero escribir `max` una sola vez y que funcione para cualquier tipo comparable."

**→ Transición:** "La taxonomía del polimorfismo — Strachey y Cardelli."

---

### [F-41] Polimorfismo — Taxonomía

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Ad-hoc: apariencia de uniformidad (sobrecarga, coerción)
- Universal: uniformidad real (paramétrico, subtipo)
- Diferencia clave: apariencia vs. uniformidad real

**🗣 Guion docente:**
> "La taxonomía de Strachey (1967) y Cardelli & Wegner (1985) distingue dos grandes familias."

> "**Ad-hoc:** apariencia de uniformidad. Sobrecarga — `+` en TypeScript funciona con números y con strings, pero son dos operaciones completamente diferentes. Coerción — `int + float` parece uniforme pero el compilador inserta una conversión."

> "**Universal:** uniformidad real. Paramétrico — la función `primero<T>(lista: T[])` funciona genuinamente para cualquier tipo T con el mismo código. Subtipo — cualquier `Animal` puede usarse donde se espera `Animal`, independientemente del subtipo concreto."

> "Diferencia clave: ad-hoc = apariencia de uniformidad; paramétrico = uniformidad real. Lo vemos con código."

**Trazabilidad bibliográfica:** Louden §8.8 (Polymorphic Type Checking) — relevancia ChromaDB 0.767. Gabbrielli §8.8 — relevancia 0.726: *"We introduced the concept of polymorphism... where we also distinguished between two radically different forms of it: overloading (or ad hoc polymorphism) and universal polymorphism"*.

**→ Transición:** "Sobrecarga en TypeScript — polimorfismo ad-hoc."

---

### [F-42] Polimorfismo ad-hoc — Sobrecarga en TypeScript

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- TypeScript: firmas de sobrecarga + implementación única
- Contraste Kotlin: sobrecarga directa de funciones
- Distinción: no es "un tipo acepta varios valores" — son múltiples funciones

**🗣 Guion docente:**
> "En TypeScript, la sobrecarga se declara con firmas de overload y una implementación genérica que las cubre todas."

Mostrar código de `area()` en vivo. Ejecutar `area(5)` y `area(3, 4)`.

> "La distinción importante: sobrecarga **no es** polimorfismo paramétrico. Son múltiples funciones distintas con el mismo nombre — el compilador elige cuál llamar basándose en los tipos de los argumentos. El binding es estático."

> "Kotlin hace sobrecarga directa: dos funciones con mismo nombre y distinta firma de parámetros. Sin necesidad de firmas declaradas + implementación única."

**→ Transición:** "Polimorfismo paramétrico — generics."

---

### [F-43] Polimorfismo paramétrico — Generics en TypeScript

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- `<T>` como parámetro de tipo
- Upper bounds con `extends`
- Clases y tipos genéricos
- Una sola implementación para múltiples tipos

**🗣 Guion docente:**
> "En el polimorfismo paramétrico, el tipo es un parámetro. `function primero<T>(lista: T[]): T` funciona para cualquier T con el mismo código — no hay distinción de implementación."

Mostrar en vivo:
```typescript
function primero<T>(lista: T[]): T { return lista[0] }
primero([1, 2, 3])           // T inferred como number
primero(["a", "b", "c"])     // T inferred como string
```

> "Con upper bounds, podemos restringir T: `T extends { valueOf(): number }` significa 'T debe tener método valueOf que retorne number'. TypeScript usa `extends` para constrains estructurales — no nominales."

> "Las clases genéricas como `Caja<T>` también siguen el mismo principio. `ReadonlyBox<T>` es un tipo genérico — una familia de tipos, uno por cada T posible."

> "Louden §8.9: 'Parametric polymorphism is the ability for a function to be applied to arguments of different types without changing the code'."

**Trazabilidad bibliográfica:** Louden §8.9 (Explicit Polymorphism) — relevancia ChromaDB 0.767.

**→ Transición:** "Polimorfismo por subtipo — herencia e interfaces."

---

### [F-44] Polimorfismo por subtipo

**⏱ Tiempo:** 8 min

**🎯 Conceptos clave:**
- Principio de Liskov (LSP)
- TypeScript `implements` + dispatch dinámico en runtime
- Diferencia con polimorfismo paramétrico: dispatch ocurre en runtime

**🗣 Guion docente:**
> "El Principio de Liskov: S es subtipo de T si cualquier programa que usa T funciona correctamente al reemplazarlo por S. `Circulo implements Forma` significa que `Circulo` puede usarse en cualquier contexto que espere `Forma`."

> "La diferencia con paramétrico: aquí el dispatch ocurre en **runtime** — el motor llama al método correcto según el tipo real del objeto. Con paramétrico, el binding es en compilación."

Mostrar `areaTotal` en vivo — el array mezcla `Circulo` y `Rectangulo`, el método `.area()` se resuelve correctamente para cada uno.

```typescript
areaTotal([new Circulo(3), new Rectangulo(4, 5)])   // polimorfismo en acción
```

> "Cada objeto sabe cómo responder a `.area()`. El array declarado como `Forma[]` puede contener cualquier subtipo — el dispatch dinámico garantiza el método correcto."

**→ Transición:** "Tabla comparativa de los tres polimorfismos."

---

### [F-45] Comparación de los tres polimorfismos

**⏱ Tiempo:** 6 min

**🎯 Conceptos clave:**
- Resumen: mecanismo, binding, overhead, restricción, expresividad

**🗣 Guion docente:**
Recorrer la tabla rápidamente, enfatizando:
- **Ad-hoc**: sin overhead, binding estático, expresividad baja
- **Paramétrico**: sin overhead (JVM usa type erasure), binding estático, expresividad alta
- **Subtipo**: virtual dispatch (pequeño overhead), binding dinámico, expresividad media-alta

> "La elección entre los tres depende del problema. Para casos limitados y específicos, sobrecarga. Para algoritmos genéricos, generics. Para jerarquías de objetos, subtipo. En la práctica, los tres conviven en lenguajes modernos."

**→ Transición:** "Cerramos el bloque con type checking y equivalencia."

---

### [F-46] Type Checking — Definición y coerción

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- Tipo compatible = tipo exacto + coercible implícitamente
- Widening (seguro) vs. Narrowing (pérdida posible)
- Type error: operador sobre operando inapropiado
- Estático vs. dinámico — TypeScript: caso especial (type erasure)

**🗣 Guion docente:**
> "El chequeo de tipos es la actividad de verificar que los operandos de cada operador son de tipos compatibles. La compatibilidad incluye coerción implícita — si el compilador puede convertir automáticamente el tipo."

> "Widening: `int → float` es seguro, no pierde información. Narrowing: `float → int` puede perder — el compilador suele dar warning. En TypeScript con `strict`, el narrowing explícito requiere casting."

> "Un type error es usar un operador con un tipo que no lo soporta: `\"hola\" - 5` en un lenguaje fuertemente tipado → error. En JavaScript/TypeScript sin strict → `NaN`. La tolerancia a errores varía."

> "Estático = en compilación. Dinámico = en runtime. TypeScript es un caso especial: hace chequeo estático durante la compilación, pero emite JavaScript — en runtime, los tipos desaparecen (type erasure). El GC no sabe de tipos TypeScript."

> "Sebesta §6.13: 'If all bindings of variables to types are static in a language, then type checking can nearly always be done statically'. Por eso TypeScript puede hacer casi todo el chequeo en compilación — los tipos son estáticos."

**Trazabilidad bibliográfica:** Sebesta §6.13 (Type Checking) — relevancia ChromaDB 0.657: *"Type checking is the activity of ensuring that the operands of an operator are of compatible types"*. Gabbrielli §8.8 (Type Checking and Inference) — relevancia 0.723.

**→ Transición:** "Equivalencia nominal vs. estructural."

---

### [F-47] Equivalencia nominal vs. estructural

**⏱ Tiempo:** 12 min

**🎯 Conceptos clave:**
- Nominal: iguales por nombre → Kotlin, Java
- Estructural: iguales por estructura → TypeScript, Go
- Consecuencias prácticas en diseño de código
- Riesgo: Celsius y Fahrenheit como `number` serían equivalentes

**🗣 Guion docente:**
> "Pregunta central: ¿cuándo son iguales dos tipos?"

> "La equivalencia **nominal** dice: dos tipos son iguales si tienen el mismo nombre. Kotlin: `data class Celsius(val v: Double)` y `data class Fahrenheit(val v: Double)` son tipos distintos aunque ambos wrappeen `Double`. El compilador los rechaza al intentar intercambiarlos."

> "La equivalencia **estructural** dice: dos tipos son iguales si tienen la misma estructura. TypeScript: si un objeto tiene campos `x: number` y `y: number`, es compatible con `Punto2D` sin importar cómo se llama."

Dibujar en pizarra: dos recuadros idénticos → nominal: ¿iguales? Depende del nombre → estructural: ¿iguales? Sí.

> "TypeScript eligió estructural por flexibilidad. Pero esto tiene un costo: `UserId = string` y `Email = string` son intercambiables. El compilador no puede ayudarte si confundes uno con otro. La solución son los branded types — intersección con un campo `_brand` que los hace estructuralmente distintos."

> "Sebesta §6.15: otro ejemplo canónico es `type Celsius = Float` y `type Fahrenheit = Float` en Ada — serían equivalentes aunque semánticamente distintos. Esa es la debilidad del tipado estructural."

**Trazabilidad bibliográfica:** Sebesta §6.15 (Type Equivalence) — relevancia ChromaDB 0.693: *"There are two approaches to defining type equivalence: name type equivalence and structure type equivalence"*. Gabbrielli §8.5 — relevancia 0.656: *"Under equivalence by name, each type has a unique definition... equivalence by name is the choice that most respects the intentions of the designer"*.

**→ Transición:** "Veamos la tabla comparativa entre lenguajes."

---

### [F-48] Equivalencia — Tabla comparativa de lenguajes

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- C con struct: nominal (con typedef)
- Java/Kotlin: nominal
- TypeScript/Go: estructural
- Haskell: nominal + paramétrico
- Consecuencia de diseño

**🗣 Guion docente:**
> "La tabla muestra la decisión de cada lenguaje. C con struct usa nominal — dos struct distintos son tipos distintos, aunque tengan los mismos campos. Java y Kotlin son nominales — `class A {}` y `class B {}` nunca son iguales. TypeScript y Go son estructurales. Haskell es nominal con polimorfismo paramétrico."

> "La consecuencia práctica de diseño: en TypeScript, si tengo `type UserId = string` y `type Email = string`, el compilador acepta pasar un email donde espero un userId. Eso es un bug semántico que el tipo no captura. La solución son los branded types."

> "La equivalencia de tipos define cuándo el compilador acepta que un valor de un tipo sea usado donde se esperaba otro. Esa decisión afecta la flexibilidad, la seguridad semántica y la complejidad del compilador."

**→ Transición:** "Bloque 5 — síntesis y cierre."

---

## BLOQUE 5 — Síntesis, Discusión y Cierre (30 min)

---

### [F-49] Mapa conceptual integrador

**⏱ Tiempo:** 10 min

**🎯 Conceptos clave:**
- Integrar todos los conceptos del día en un mapa
- Mostrar las conexiones entre bloques

**🗣 Guion docente:**
> "Construyamos juntos el mapa del día. Tenemos dos grandes áreas: Tipos de Datos y Sistemas de Tipos."

Dibujar en pizarra mientras se muestra la filmina:
- Tipos de Datos → Primitivos (enteros, float, bool, char) → Ordinales (enum, subrangos) → Compuestos (array, registro, tupla, unión, lista) → Recursivos (árbol, lista enlazada) → Opcionales (T|null, Maybe, Option)
- Sistemas de Tipos → dimensiones → equivalencia → polimorfismo

> "Las conexiones: los tipos primitivos son la base → los compuestos se construyen sobre ellos → los recursivos se construyen sobre los compuestos. El sistema de tipos define las reglas de compatibilidad entre todos."

> "Las dimensiones del sistema de tipos — cuándo verifica, qué tan rígido, cuántos tipos — son decisiones de diseño que cada lenguaje toma. No hay respuestas correctas, sino tradeoffs."

**→ Transición:** "Hacia dónde vamos desde acá."

---

### [F-50] Conexión con próximos temas

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- T11: coerciones, sobrecarga de operadores, short-circuit
- T14 (futuro): Hindley-Milner, λ-cálculo tipado, subtyping formal

**🗣 Guion docente:**
> "T11 la próxima clase: expresiones y estructuras de control. Vamos a ver cómo las coerciones que hoy conceptualizamos aparecen en operadores aritméticos, sobrecarga de operadores y evaluación booleana."

> "Y en T14, más adelante, volvemos a los sistemas de tipos con base formal: el algoritmo Hindley-Milner que mencionamos, el λ-cálculo tipado, y la teoría del subtyping."

> "Recordar el vínculo con T09: el sistema de tipos es la suma de las decisiones de binding que vimos antes. Un tipo primitivo, estáticamente vinculado, con equivalencia nominal = exactamente lo que vimos en la 5-tupla de variables."

**→ Transición:** "Consigna del TP."

---

### [F-51] Consigna del TP

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Exploración de un sistema de tipos no visto en clase
- Comparación con TypeScript en 5 dimensiones

**🗣 Guion docente:**
> "El TP asociado a este módulo es de exploración: eligen un lenguaje que no vimos en profundidad — Rust, Swift, Scala, Elm, Zig u otro aprobado — y documentan su sistema de tipos en comparación con TypeScript."

> "La entrega es un repositorio con código de ejemplo y un informe en Markdown. Deben documentar al menos 5 aspectos: equivalencia, null safety, polimorfismo, strong/weak typing, y gestión de memoria. Y comparar con TypeScript usando ejemplos propios."

> "La fecha límite y todos los detalles están en la plataforma. Cualquier duda sobre la elección del lenguaje, consúltenme antes de arrancar."

**→ Transición:** "Cierre y bibliografía."

---

### [F-52] Cierre y bibliografía

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Resumen del día
- Bibliografía para profundizar
- Conexión con T11

**🗣 Guion docente:**
> "Hoy cubrimos el Módulo VII completo. Fuimos desde la definición más básica de tipo de dato hasta los sistemas de tipos como espacio de decisiones de diseño de lenguajes."

> "La bibliografía principal es el Capítulo 6 de Sebesta — lo vimos prácticamente completo. Louden §8.8–§8.9 para el polimorfismo formal. Gabbrielli §8.2, §8.4 y §8.7 para type safety y tipos compuestos. Para TypeScript en profundidad, el handbook oficial es excelente."

> "Próxima clase: T11 — Expresiones y Estructuras de Control."

> *"Un lenguaje de programación es solo tan bueno como su sistema de tipos."* — Bjarne Stroustrup.

**→ Transición:** "Espacio de Q&A."

---

### [F-53] Preguntas finales y espacio Q&A

**⏱ Tiempo:** 5 min

**🎯 Conceptos clave:**
- Tres preguntas disparadoras para reflexión
- Espacio abierto para preguntas de los alumnos

**🗣 Guion docente:**
Abrir las tres preguntas para discusión. Guiar la clase hacia:

**Pregunta 1:** strictNullChecks opt-in → retrocompatibilidad con JS existente, adopción gradual. Es una decisión de adopción masiva, no de teoría.

**Pregunta 2:** Discriminated unions en TypeScript vs. sealed class Kotlin → TypeScript: más conciso para tipos simples. Kotlin: exhaustividad automática. Herencia tradicional: cuando necesitás extensión abierta (Open/Closed Principle).

**Pregunta 3:** Equivalencia estructural → gana flexibilidad, pierde seguridad semántica. `UserId` y `Email` son intercambiables sin branded types. Una librería de terceros puede satisfacer accidentalmente una interfaz sin intención.

> "Espacio abierto para sus preguntas. No hay preguntas tontas — las mejores son las que surgen de haber tratado de implementar algo y haber chocado con el sistema de tipos."

---

## Notas de preparación

### Material a tener listo antes de clase
- [ ] TypeScript Playground abierto en browser (para demos en vivo: F-07, F-08, F-12, F-20, F-21, F-29, F-38, F-43, F-44)
- [ ] VSCode con proyecto TypeScript para F-23, F-36, F-37
- [ ] Marcadores de colores para pizarra (mapa conceptual F-49, conexión T09 en F-02)

### Ajustes de tiempo si hay retraso
- Si el Bloque 1 se extiende → comprimir F-05 (Clasificación) a 3 min y F-09 (Complejo/Decimal) a 3 min
- Si el Bloque 2 se extiende → comprimir F-25 (Haskell ADT) y F-27 (Producto vs suma) a 3 min cada uno
- Si el Bloque 3 se extiende → comprimir F-33 (Soluciones históricas) a 3 min y F-35 (Tipos recursivos definición) a 4 min
- Si el Bloque 4 se extiende → comprimir F-45 (Comparación polimorfismos) a 4 min y F-50 (Conexión próximos) a 3 min
- El Bloque 5 no debe acortarse — la síntesis es crítica para el cierre pedagógico

### Verificación de tiempos (suma = 360 min)

| Bloque | Min | Filminas | Suma parcial |
|--------|-----|----------|---------------|
| 0 | 15 | F-00 a F-03 | 1+7+4+3 = 15 ✓ |
| 1 | 70 | F-04 a F-14 | 10+5+5+10+10+5+5+5+5+5+5 = 70 ✓ |
| 2 | 90 | F-15 a F-30 | 6+6+8+6+6+5+6+5+6+5+4+6+4+6+6+5 = 90 ✓ |
| 3 | 75 | F-31 a F-39 | 10+8+5+8+6+8+8+12+10 = 75 ✓ |
| 4 | 80 | F-40 a F-48 | 8+8+8+10+8+6+10+12+10 = 80 ✓ |
| 5 | 30 | F-49 a F-53 | 10+5+5+5+5 = 30 ✓ |
| **TOTAL** | **360** | **F-00 a F-53** | **15+70+90+75+80+30 = 360 ✓** |

### Trazabilidad bibliográfica — respaldo ChromaDB

Las siguientes filminas tienen citas Sebesta/Louden/Gabbrielli respaldadas por queries ChromaDB (resultados con relevancia ≥ 0.5):

- **F-04** ¿Qué es tipo de dato? → Sebesta §6.1 (0.627)
- **F-07** Enteros → Sebesta §6.2.1.1 (0.594)
- **F-08** Floating Point → Sebesta §6.2.1 (0.593)
- **F-10** Boolean/Char → Sebesta §6.2.4 (0.627)
- **F-13** Enum comparación → Sebesta §6.4.1 (0.657)
- **F-14** Rangos/subrangos → Louden §8.2 (0.503), Gabbrielli §8.3.9 (0.529)
- **F-16** Strings → Sebesta §6.3 (0.67, 0.554)
- **F-17** Arrays taxonomía → Sebesta §6.5 (0.492)
- **F-20** Maps → Sebesta §6.8 (0.489)
- **F-23** Registros → Sebesta §6.7 (0.492)
- **F-24** Tuplas → Sebesta §6.8 (0.458)
- **F-26** Listas → Sebesta §6.9 (0.492)
- **F-28** Uniones C → Sebesta §6.10 (0.691)
- **F-30** TS/Kotlin/Haskell uniones → Gabbrielli §8.4.3 (0.682)
- **F-31** Punteros → Sebesta §6.11.1 (0.699)
- **F-32** Problemas clásicos → Sebesta §6.11.6 (0.688), Gabbrielli §8.5 (0.735)
- **F-34** Referencias vs punteros → Sebesta §6.11.5 (0.68)
- **F-37** Problema del null → Sebesta §6.12 (0.613)
- **F-41** Polimorfismo taxonomía → Louden §8.8 (0.767), Gabbrielli §8.8 (0.726)
- **F-43** Generics → Louden §8.9 (0.767)
- **F-46** Type Checking → Sebesta §6.13 (0.657), Gabbrielli §8.8 (0.723)
- **F-47** Equivalencia nominal/estructural → Sebesta §6.15 (0.693), Gabbrielli §8.5 (0.656)

### Contexto adicional para consultas
- TypeScript Handbook (generics): https://www.typescriptlang.org/docs/handbook/2/generics.html
- Sebesta Cap. 6 tiene ejemplos en Ada y Fortran que pueden agregar color si hay tiempo
- Cardelli & Wegner 1985: "On understanding types, data abstraction, and polymorphism" — lectura opcional avanzada
