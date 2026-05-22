# Clase: Tipos de Datos y Sistemas de Tipos
**Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF
**Fecha:** __________________ | **Semana:** 11 | **Duración:** 360 min
**Lenguaje principal:** TypeScript | **Aula/Modalidad:** ________________

---

## Objetivos de la clase

Al finalizar, el alumno podrá:
1. Definir el tipo como par (conjunto de valores + operaciones) y explicar type safety/soundness
2. Clasificar y caracterizar los tipos primitivos con sus representaciones internas
3. Analizar tipos producto (arrays 5 variantes, records, tuplas) y tipos suma (uniones discriminadas)
4. Comparar uniones libres de C con tipos suma seguros en TypeScript/Haskell/Kotlin
5. Evaluar dangling pointer y null safety; diferenciar name vs. structural equivalence
6. Aplicar coerciones y conversiones identificando riesgos
7. Explicar polimorfismo ad-hoc, paramétrico y por subtipo; razonar sobre varianza

---

### [F-00] Portada
**Tiempo:** 2 min (presentación)
**Qué decir:**
- Presentar el tema con la cita de Gabbrielli: *"Un tipo es una colección de valores homogéneos con un conjunto uniforme de operaciones."*
- Anticipar la estructura: 7 bloques, 360 minutos, una clase densa pero con un hilo conductor claro
- Conectar: venimos de estudiar *cómo se vinculan los tipos a las variables* (T09.1) y *cómo el sistema verifica esa vinculación* (T09.2). Hoy estudiamos *qué son los tipos* como estructuras formales.
- Aclarar explícitamente: gradual typing, `any`/`unknown` y type narrowing NO se repiten — ya están en T09.2. Hoy entramos al corazón de la teoría de tipos.

**Conceptos clave:** ninguno aún — solo establecer el marco mental
**Transición:** "Empecemos por la pregunta más básica: ¿qué es un tipo?"

---

## BLOQUE A — El tipo como contrato formal (30 min)

---

### [F-01] El tipo como contrato formal
**Tiempo:** 10 min
**Qué decir:**
- Arrancar con la pregunta: "¿Para qué sirve un tipo?" — esperar respuestas del aula (seguridad, documentación, verificación)
- Formalizar: tipo = par (D, O) — dominio de valores y operaciones válidas. Sin el tipo, los procesadores operan sobre bits sin semántica.
- Usar el ejemplo de TypeScript: mostrar que `const n: number` limita qué se puede hacer. El compilador rechaza `const s: string = n` — eso ES el sistema de tipos funcionando.
- Importante: `number` en TypeScript = IEEE 754 double. No hay tipo entero nativo. Esto importará mucho en F-04.
- Dar el ejemplo concreto: `string` no tiene operador `+` aritmético (o sí, pero como concatenación — que es una operación del dominio `string`)

**Conceptos clave:** tipo = (D, O); el tipo da significado a los bits; type annotations en TypeScript
**Preguntas anticipadas:**
- *"¿Un array también es un tipo?"* → Sí, es un tipo compuesto — lo veremos en Bloque C
- *"¿TypeScript verifica los tipos en runtime?"* → No, en compilación (transpilación). En runtime JavaScript no tiene tipos estáticos.
**Transición:** "Ahora que definimos qué es un tipo, ¿qué significa que un sistema de tipos sea *seguro*?"

---

### [F-02] Type safety y soundness
**Tiempo:** 10 min
**Qué decir:**
- Diferenciar type safety (garantía práctica) de soundness (garantía formal matemática)
- Recorrer la tabla por filas: Haskell → soundness total porque el compilador rechaza TODO programa potencialmente inseguro. Kotlin → lo mismo pero con null safety integrado. TypeScript → interesante: es *deliberadamente* no-sound.
- Explicar la decisión de TypeScript: priorizan usabilidad sobre soundness. Por ejemplo, los arrays son covariantes (lo veremos en G) aunque eso rompe soundness. Es una decisión de diseño pragmática.
- C → mencionar brevemente el ejemplo `(float*) &intVar`: el cast reinterpreta los bytes del int como si fuera float. El compilador no verifica nada. Total falta de soundness.
- Citar Sebesta §6.1 — criterios de diseño de tipos: expresividad, eficiencia, seguridad. TypeScript prioriza expresividad sobre seguridad máxima.

**Conceptos clave:** type safety; soundness; el tradeoff TypeScript — usabilidad vs. soundness formal
**Preguntas anticipadas:**
- *"¿Entonces TypeScript es inseguro?"* → No equivale a inseguro. Es "parcialmente sound" por diseño. En la práctica captura la vasta mayoría de errores. La no-soundness aparece en casos específicos como covarianza de arrays.
**Transición:** "Antes de entrar a los tipos específicos, necesitamos un mapa de todo lo que vamos a ver."

---

### [F-03] Taxonomía de tipos
**Tiempo:** 10 min
**Qué decir:**
- Mostrar el diagrama como la "hoja de ruta" de toda la clase: primitivos, producto (AND), suma (OR), recursivos
- Dar un ejemplo rápido de cada categoría para que el alumno tenga el marco mental antes de profundizar:
  - Primitivos: `number`, `string`, `boolean`
  - Producto: `interface Persona {nombre: string; edad: number}` — tiene AMBOS campos
  - Suma: `type Resultado = {ok: true} | {ok: false; error: string}` — tiene UNO de los dos
  - Recursivo: una lista — `Nodo` que contiene otro `Nodo` en su interior
- Segundo eje: monomórfico vs. polimórfico. `function sumar(a: number, b: number)` es monomórfica. `function identidad<T>(x: T)` es polimórfica. Los detalles en Bloque G.
- Decir explícitamente: "Este diagrama va a estar en el examen. Vamos a construirlo slide a slide durante la clase."

**Conceptos clave:** taxonomía primitivos/producto/suma/recursivos; monomórfico vs. polimórfico
**Preguntas anticipadas:**
- *"¿Las clases de TypeScript dónde van?"* → Depende: una clase es un tipo de referencia. Su estructura interna puede ser un tipo producto. Con herencia, introduce subtipado (Bloque G).
**Transición:** "Empecemos por los tipos primitivos — los átomos del sistema."

---

## BLOQUE B — Tipos primitivos y su representación interna (50 min)

---

### [F-04] Enteros: representación en complemento a 2
**Tiempo:** 13 min
**Qué decir:**
- Iniciar con la pregunta: "¿Por qué `Number.MAX_SAFE_INTEGER` existe en JavaScript?" — para motivar el problema.
- Explicar brevemente complemento a 2: con n bits, representamos [−2^(n−1), 2^(n−1)−1]. No hay que memorizar la fórmula de conversión, pero sí entender que es la razón del límite.
- El punto crítico de TypeScript: `number` es SIEMPRE IEEE 754 double de 64 bits. No hay tipo `int` nativo. Esto significa que para enteros mayores de 2^53, la precisión se pierde — mostrar el ejemplo `MAX_SAFE + 1 === MAX_SAFE + 2 // true`.
- Introducir `bigint` como la solución: enteros arbitrariamente grandes, con sintaxis literal `42n`.
- Contrastar con Kotlin donde `Int` tiene overflow silencioso — el ejemplo `Int.MAX_VALUE + 1 = -2^31` es contraproducente pero importante para entender el límite.
- Preguntar al aula: "¿Cuándo les importa esto en la práctica?" → aplicaciones financieras, criptografía, IDs de bases de datos grandes.

**Conceptos clave:** complemento a 2; límite de `NUMBER.MAX_SAFE_INTEGER`; `bigint` para enteros precisos; TypeScript no tiene tipo entero nativo
**Preguntas anticipadas:**
- *"¿`BigInt` tiene overhead?"* → Sí, es más lento que `number`. Se usa solo cuando se necesita precisión de enteros > 2^53.
**Transición:** "El número entero es el caso más sencillo. El flotante es más complejo..."

---

### [F-05] Punto flotante: IEEE 754
**Tiempo:** 12 min
**Qué decir:**
- Mostrar el diagrama de formato: signo (1 bit), exponente (11 bits), mantisa (52 bits). No hace falta que memoricen los campos — sí que entiendan qué implican.
- El ejemplo `0.1 + 0.2 !== 0.3` es el momento "wow" de esta filmina. Ejecutarlo si hay computadora disponible. La representación binaria de 0.1 es periódica en base 2 → nunca exacta.
- Mostrar `Number.EPSILON` como la forma correcta de comparar flotantes — comparar con `< EPSILON` en lugar de `===`.
- Valores especiales: `Infinity`, `-Infinity`, `NaN`. El hecho de que `NaN !== NaN` siempre sorprende a los alumnos. Explicar que es parte del estándar IEEE 754 — NaN no es un valor definido.
- Cuándo NO usar `number`: aplicaciones financieras → usar enteros en centavos multiplicados (evitar representación binaria), o una librería `Decimal`.

**Conceptos clave:** IEEE 754; por qué 0.1 + 0.2 ≠ 0.3; NaN ≠ NaN; cuándo usar Decimal
**Preguntas anticipadas:**
- *"¿Todas las CPUs modernas usan IEEE 754?"* → Sí, prácticamente todas. Es el estándar universal desde 1985.
- *"¿Por qué `NaN !== NaN`?"* → Por diseño del estándar: NaN representa "resultado no determinado" — que dos resultados no determinados sean iguales no tendría sentido matemático.
**Transición:** "Antes de tipos compuestos, completamos los primitivos simples."

---

### [F-06] Boolean, Char y Unicode
**Tiempo:** 10 min
**Qué decir:**
- Boolean: enfatizar que en TypeScript `boolean` es un tipo real con exactamente dos valores — `true` y `false`. En C, cualquier número diferente de cero es "verdadero" — no hay type safety real. Haskell va más lejos: `Bool = True | False` es un ADT (lo veremos en Bloque D).
- El tema central de esta filmina es Unicode. Ejecutar el ejemplo del emoji `"😀".length === 2` — siempre genera reacción en el aula.
- Explicar la diferencia: **code unit** (lo que cuenta `.length`) vs. **code point** (el carácter Unicode real). UTF-16 usa code units de 16 bits. Los caracteres fuera del BMP (Basic Multilingual Plane) requieren dos code units — llamados "surrogate pairs".
- La lección práctica: para contar caracteres en TypeScript, usar `[...str].length` (spread operator usa el iterator de code points) o `Intl.Segmenter` para texto con emojis complejos (familia, banderas).

**Conceptos clave:** boolean como tipo real vs. C integer; code unit vs. code point; `.length` no es lo que parece
**Preguntas anticipadas:**
- *"¿Por qué TypeScript usa UTF-16 y no UTF-8?"* → JavaScript fue diseñado antes de que UTF-8 se consolidara como estándar dominante. UTF-16 es el formato interno del motor V8 y todos los motores JS.
**Transición:** "El string parece primitivo pero tiene diseño profundo..."

---

### [F-07] String: inmutabilidad y diseño
**Tiempo:** 8 min
**Qué decir:**
- El punto principal: strings en TypeScript son inmutables. Cada operación crea un nuevo string, no modifica el original.
- Implicación para aliases: si `const a = "hola"` y `const b = a`, cambiar `b` (que no se puede) no afecta `a`. A diferencia de los objetos donde sí hay aliasing.
- El problema clásico de performance: concatenación en loop `for (i) s += "x"` es O(n²) porque crea n strings nuevos. La solución: `Array.join` o acumular en array.
- Template literals: mostrar como la forma idiomática TypeScript para construir strings con interpolación. Es type-safe: el compilador verifica que las expresiones dentro `${}` tengan toString.
- Tabla de contraste: enfatizar que C es el único de la lista con strings mutables — y por eso hay tantos bugs de seguridad (buffer overflow, etc.)

**Conceptos clave:** inmutabilidad de strings; implicaciones de performance; template literals
**Preguntas anticipadas:**
- *"¿`String` (con mayúscula) vs `string` en TypeScript?"* → `string` es el tipo primitivo (lo que se usa siempre). `String` es el objeto wrapper — casi nunca se usa directamente.
**Transición:** "Último primitivo: enumeraciones."

---

### [F-08] Enumeraciones y tipos ordinales
**Tiempo:** 7 min
**Qué decir:**
- Motivar: ¿por qué usar `Direccion.Norte` en vez de `"NORTE"` o la constante `0`? Tres razones: legibilidad, type safety (el compilador rechaza valores inválidos) y autocompletado en el IDE.
- TypeScript `enum`: compilar a objeto JavaScript, valores literales — mostrar que en strict mode no se puede pasar un string directamente.
- C `enum`: es solo un alias de int. Se puede asignar `42` a un campo de tipo enum y el compilador no dice nada. No hay type safety real.
- Kotlin `enum class`: tipo cerrado que puede tener comportamiento (métodos, propiedades). La diferencia es fundamental: una enum class es un tipo real, no un número disfrazado.
- Haskell `newtype`: el más fuerte. Dos newtypes con la misma estructura son tipos completamente distintos — el compilador rechaza mezclarlos. Costo de runtime: cero (se optimiza).
- Cerrar el bloque B: tenemos todos los primitivos. Ahora combinamos para construir tipos compuestos.

**Conceptos clave:** ventajas de enum sobre constantes; jerarquía C enum < TS enum < Kotlin enum class < Haskell newtype
**Preguntas anticipadas:**
- *"¿Los `const enum` de TypeScript son diferentes?"* → Sí: se inlinan en tiempo de compilación (no generan objeto JS). Más eficiente pero menos debuggeable.
**Transición:** "Pasamos a los tipos compuestos — comenzando por el tipo producto."

---

## BLOQUE C — Tipos producto: arrays, registros y tuplas (65 min)

---

### [F-09] Arrays: las 5 variantes de binding time
**Tiempo:** 10 min
**Qué decir:**
- Iniciar con la sorpresa: "El array no es un solo concepto — hay cinco tipos distintos según cuándo se fija el tamaño."
- Recorrer la tabla fila por fila. Para cada variante: 1) cuándo se decide el tamaño, 2) dónde vive (stack vs. heap), 3) ejemplo de lenguaje.
- Variante 1 (static): muy rápida, siempre disponible, tamaño fijo para siempre — útil para tablas de lookup, configuración.
- Variante 2 y 3 (stack-dynamic): tamaño fijo al entrar a la función. La variante 3 (VLA en C99) es interesante pero peligrosa con arrays grandes (stack overflow).
- Variante 4 (heap-dynamic fijo): el `new int[n]` de Java — tamaño fijo al crear, pero en heap.
- Variante 5 (heap-dynamic variable): `ArrayList`, `MutableList` — el más flexible, el más usado en TypeScript.
- TypeScript siempre usa variantes 4 y 5 — no tiene acceso al stack ni a arrays estáticos. Es más seguro pero menos performante para casos donde la variante 1 o 2 sería ideal.

**Conceptos clave:** binding time del tamaño; stack vs. heap allocation; TypeScript solo tiene heap-dynamic
**Preguntas anticipadas:**
- *"¿Por qué importa si está en stack o heap?"* → Stack: O(1) allocation, destrucción automática al salir del scope. Heap: O(1) amortizado, GC tiene que limpiar. Para código de alto rendimiento, la diferencia es significativa.
**Transición:** "Veamos más características del array: multidimensionales, slices y asociativos."

---

### [F-10] Arrays: multidimensionales, slices y asociativos
**Tiempo:** 10 min
**Qué decir:**
- Multidimensional: TypeScript implementa como "array de arrays" (not a true multidimensional array). En memoria, cada fila es un objeto separado.
- Row-major vs. column-major: la razón de esto es la cache del procesador. Cuando se accede en orden row-major, los datos son contiguos en memoria → cache hits. Si se accede column-major en un row-major language, cada acceso puede ser un cache miss → 10-100x más lento en matrices grandes. Importante para HPC (computación científica).
- Slices en TypeScript vs. Go: esta es una diferencia importante. `slice()` en TypeScript crea una copia — cambiar el original no afecta el slice. En Go, un slice es una vista del array subyacente — más eficiente pero con riesgo de aliasing.
- Arrays asociativos: mostrar `Record<K,V>` (tipo estático, object literal) vs. `Map<K,V>` (dinámico, cualquier tipo de clave). `Record` compila a un objeto JS común. `Map` es una estructura de hash separada con operaciones `get/set/has`.

**Conceptos clave:** row-major y cache locality; slice como copia (TypeScript) vs. vista (Go); Record vs. Map
**Preguntas anticipadas:**
- *"¿Cuál es más eficiente, Record o Map?"* → Para claves string simples: Record (object literal) es más rápido. Para claves de otros tipos o gran cantidad de inserciones/eliminaciones: Map.
**Transición:** "Pasamos de arrays a registros — estructuras con campos nombrados."

---

### [F-11] Records: alineamiento de memoria
**Tiempo:** 10 min
**Qué decir:**
- Este es el slide más "de sistemas" del bloque. La idea central: el procesador no puede leer datos desalineados en algunas arquitecturas, y el compilador de C inserta padding para alinearlos.
- Mostrar el ejemplo del struct con `char` seguido de `int`: el `char` ocupa 1 byte, pero el `int` requiere alineación a 4 bytes → 3 bytes de padding automático. El struct tiene 8 bytes, no 5.
- La lección práctica: en C, ordenar los campos del struct de mayor a menor tamaño para minimizar padding. Es una optimización real en código embebido o de alto rendimiento.
- Formalización de Gabbrielli: el record es el tipo producto cartesiano de sus campos. `Persona = String × Int × Boolean` — un valor de Persona es una 3-tupla (nombre, edad, activo). Esto conecta la notación matemática con la implementación.
- TypeScript no expone esto — los objetos JS son dinámicos, sin layout de memoria fijo.

**Conceptos clave:** alineamiento de memoria; padding en C structs; record como producto cartesiano formal
**Preguntas anticipadas:**
- *"¿TypeScript/JS también tiene este problema de alineamiento?"* → No — los objetos JavaScript son dinámicos (hash tables internamente), no tienen layout fijo de memoria. El motor V8 optimiza internamente pero el programador no lo controla.
**Transición:** "TypeScript usa interfaces para definir la forma de sus objetos/records."

---

### [F-12] TypeScript interfaces y objetos como records
**Tiempo:** 8 min
**Qué decir:**
- TypeScript `interface`: define la "forma" esperada de un objeto. No genera código en runtime — es solo para el compilador.
- Diferencia `interface` vs `type`: para objetos simples son intercambiables. `interface` es más extensible (se puede hacer `extends`). `type` permite uniones y expresiones de tipos más complejas. En práctica moderna, `type` es más flexible.
- Readonly: `Readonly<T>` hace todos los campos inmutables a nivel de tipo. El compilador rechaza asignaciones. Importante para objetos de configuración o Value Objects en DDD.
- Desestructuración: mostrar la equivalencia con Kotlin `data class` y `copy`. El spread `{...ana, edad: 31}` crea un nuevo objeto con todos los campos de `ana` excepto `edad`. Es el patrón de "modificación no destructiva" — sin aliases con el original.
- Esto conecta con el tema de aliases de T09.2: los objetos TypeScript SÍ tienen aliasing. Los types Readonly y el spread son herramientas para controlarlo.

**Conceptos clave:** interface vs. type; Readonly; spread como copia-con-modificación; TypeScript es estructural
**Preguntas anticipadas:**
- *"¿Interface es lo mismo que una clase abstracta?"* → No. Interface es solo un contrato de tipos en compilación — sin implementación, sin constructores. Las clases pueden implementar interfaces, pero una interface sola no genera código.
**Transición:** "Las tuplas son como registros pero con campos posicionales."

---

### [F-13] Tuplas como producto cartesiano formal
**Tiempo:** 7 min
**Qué decir:**
- Distinguir la tupla del array: un `number[]` puede tener cualquier cantidad de elementos, todos `number`. Una `[string, number]` tiene exactamente 2 elementos con tipos específicos en posiciones específicas.
- La formalización de Gabbrielli: el tipo `T1 × T2 × … × Tn`. Cada instancia de ese tipo ES una n-tupla. La notación matemática de "producto cartesiano" es exactamente esto.
- TypeScript 4.0 trajo named tuples: `[x: number, y: number, z: number]` — legibilidad mejorada sin cambio de semántica.
- Haskell: las tuplas son ciudadanas de primera clase del lenguaje. `(a, b)` es azúcar sintáctica para el tipo producto. La conexión con currying: `f :: a -> b -> c` es equivalente a `f :: (a, b) -> c` vía isomorfismo.
- Cuándo usar tupla vs. record: si los valores son anónimos y temporales → tupla. Si tienen semántica nombrada que importa para mantenibilidad → interface/type.

**Conceptos clave:** tupla vs. array; producto cartesiano formal; named tuples; tupla vs. record
**Preguntas anticipadas:**
- *"¿Se puede desestructurar una tupla TypeScript?"* → Sí: `const [nombre, edad] = par` — el compilador verifica los tipos de cada posición.
**Transición:** "Hemos visto tipos que combinan valores. Ahora vemos tipos que ELIGEN entre valores: los tipos suma."

---

## BLOQUE D — Tipos suma: uniones y tipos recursivos (50 min)

---

### [F-14] Uniones libres en C: el problema de type safety
**Tiempo:** 8 min
**Qué decir:**
- Iniciar con la motivación: ¿por qué C tiene unions? Para ahorrar memoria — cuando se sabe que una variable solo va a tener UNO de varios tipos posibles, se puede hacer que compartan el mismo espacio.
- El problema: el compilador de C no rastrea cuál campo fue escrito último. Leer el campo incorrecto es comportamiento indefinido (UB). No hay error, no hay crash garantizado — puede dar resultados silenciosamente incorrectos.
- Mostrar el ejemplo: escribimos `int i = 65`, leemos como `float f` → puede dar cualquier float. El patrón de bits de `65` como int interpretado como IEEE 754 float da algo completamente diferente.
- El caso de `char c[0]` es interesante: leer el primer byte del int 65 como char podría dar 'A' (65 = ASCII 'A') o podría dar 0 dependiendo de endianness.
- Uso legítimo: serialización de bajo nivel, instrucciones SIMD, drivers de hardware. Siempre con conocimiento explícito del layout de memoria.

**Conceptos clave:** C union = compartir memoria; sin discriminador = comportamiento indefinido; uso legítimo en sistemas de bajo nivel
**Preguntas anticipadas:**
- *"¿Los compiladores modernos de C detectan el uso incorrecto?"* → Algunos (LLVM con `-fsanitize=undefined`) sí detectan UB en runtime. Pero el estándar lo declara UB — el compilador NO está obligado a detectarlo.
**Transición:** "La solución: agregar un discriminador. Eso es el tipo suma seguro."

---

### [F-15] Tipo suma: uniones discriminadas
**Tiempo:** 10 min
**Qué decir:**
- La clave: el tipo suma agrega una **etiqueta** (tag) que identifica cuál variante está activa. Ahora el sistema de tipos sabe qué campo es válido.
- TypeScript discriminated unions: el campo `kind` es el discriminador — un tipo literal string. El compilador usa ese campo para narrowing.
- Mostrar el `switch` sobre `f.kind` — TypeScript sabe que dentro de `case "circulo"` el tipo de `f` es `{ kind: "circulo"; radio: number }` — tiene acceso directo a `f.radio`.
- Sin el discriminador, TypeScript no puede hacer ese narrowing.
- La comparación con C tagged union (estructura `{ enum tag; union valor }`) muestra que el concepto existe en C, pero es manual y verboso. TypeScript lo integra en el sistema de tipos nativamente.
- El `never` exhaustivo: anticipar que lo veremos en F-16 — es la técnica para que el compilador verifique exhaustividad.

**Conceptos clave:** discriminador/tag; narrowing automático en TypeScript; suma formal T1+T2; comparación con C tagged union
**Preguntas anticipadas:**
- *"¿El campo discriminador debe llamarse 'kind'?"* → No, puede tener cualquier nombre. `type`, `tag`, `variant` son comunes. Lo importante es que sea un tipo literal único para cada variante.
**Transición:** "Veamos cómo Haskell y Kotlin manejan esto más elegantemente."

---

### [F-16] Haskell ADT y Kotlin sealed classes
**Tiempo:** 10 min
**Qué decir:**
- Haskell ADT: la sintaxis `data Forma = Circulo Double | Rectangulo Double Double` crea automáticamente constructores y pattern matching. El compilador verifica exhaustividad con `-Wincomplete-patterns`. Es el sistema más elegante — el lenguaje fue diseñado alrededor de tipos algebraicos.
- Kotlin sealed classes: equivalente orientado a objetos de los ADT. `sealed` significa que todas las subclases deben estar en el mismo archivo — el compilador sabe la lista completa de subtipos.
- El `when` en Kotlin: cuando se usa sobre un tipo `sealed`, el compilador OBLIGA a cubrir todos los subtipos. Si se agrega una nueva subclase `sealed`, todos los `when` existentes fallan en compilación — excelente mantenibilidad.
- TypeScript `never` exhaustivo: la técnica `default: const _: never = f` hace que si hay un caso no cubierto, el tipo de `f` no será `never` → error de tipo. Es una verificación en tiempo de compilación.
- Comparar los tres enfoques: Haskell (más limpio, funcional), Kotlin (más cercano a OOP), TypeScript (más verboso, pero funciona bien).

**Conceptos clave:** Haskell ADT + exhaustividad automática; Kotlin sealed + when exhaustivo; TypeScript never para exhaustividad
**Preguntas anticipadas:**
- *"¿Sealed class es lo mismo que final class?"* → No. `final` prohíbe toda herencia. `sealed` permite herencia pero solo dentro del mismo archivo — el compilador conoce todos los subtipos posibles.
**Transición:** "El tipo recursivo es la última forma de tipo compuesto: tipos que se definen en términos de sí mismos."

---

### [F-17] Tipos recursivos: listas y árboles
**Tiempo:** 10 min
**Qué decir:**
- Definición informal: un tipo es recursivo si aparece en su propia definición. La pregunta inmediata del alumno: "¿no es un loop infinito?" — no, porque hay un caso base (Vacía, Hoja) que no es recursivo.
- Mostrar la definición inductiva: `Lista(A) = Vacía | Nodo(A, Lista(A))`. El caso base es Vacía. El caso inductivo tiene un Nodo que contiene otro Lista.
- Por qué necesita indirección: sin un puntero/referencia, `sizeof(Nodo) = sizeof(A) + sizeof(Nodo)` — ecuación sin solución finita. Con un puntero/referencia, `sizeof(Nodo) = sizeof(A) + sizeof(puntero)` — solución finita.
- En TypeScript: el tipo recursivo `type Lista<A> = { tipo: "vacia" } | { tipo: "nodo"; valor: A; siguiente: Lista<A> }` compila correctamente porque TypeScript soporta tipos mutuamente recursivos.
- En Haskell: la recursividad es nativa — `data List a = Nil | Cons a (List a)` sin ningún operador especial.
- Conectar con el plan mínimo: los árboles binarios del Módulo VII son exactamente tipos recursivos. No son estructuras arbitrarias — tienen una base formal en teoría de tipos.

**Conceptos clave:** recursividad con caso base; necesidad de indirección; listas y árboles como tipos recursivos
**Preguntas anticipadas:**
- *"¿Los tipos genéricos recursivos siempre necesitan '?' o nullable?"* → En TypeScript sí (para el caso base). En Haskell no (el caso base es un constructor sum type). En Kotlin: `Nodo<T>?` o usar `sealed class`.
**Transición:** "Pausa activa — consolidamos bloques A-D."

---

### [F-18] Checkpoint — Bloques A-D
**Tiempo:** 10 min (pausa activa)
**Qué decir:**
- Dar 3 minutos para que los alumnos intenten responder las preguntas antes de revelar las respuestas.
- **Respuesta 1:** `Resultado<T>` es un tipo suma. Tiene dos variantes mutuamente excluyentes — `{ok: true; valor: T}` O `{ok: false; error: string}`. No es producto porque un valor no puede ser ambos simultáneamente.
- **Respuesta 2:** `type ListaResultados<T> = { tipo: "vacia" } | { tipo: "nodo"; valor: Resultado<T>; siguiente: ListaResultados<T> }` — tipo recursivo que usa Resultado<T> como su tipo de valor.
- **Respuesta 3:** Agregar `default: const _: never = r; throw new Error(...)` — si se agrega una nueva variante a `Resultado`, el compilador detecta que `_` no puede ser `never` y lanza un error de tipo.
- Aprovechar para hacer preguntas de comprensión al aula y detectar gaps antes de entrar a Bloque E.

**Conceptos clave:** consolidación; diferencia producto/suma; tipos recursivos; exhaustividad never
**Transición:** "Segunda mitad: punteros, equivalencia, coerción y polimorfismo."

---

## BLOQUE E — Punteros, referencias y null safety (40 min)

---

### [F-19] El tipo puntero en C
**Tiempo:** 10 min
**Qué decir:**
- El tipo puntero no existe en TypeScript — pero entenderlo es fundamental para comprender por qué los lenguajes modernos eliminaron el puntero crudo y lo reemplazaron con referencias gestionadas.
- Operaciones `&` y `*`: explicar con el diagrama de memoria. `&x` toma una variable en memoria y retorna su dirección (un número). `*p` toma esa dirección y va a buscar el valor almacenado allí.
- Aritmética: `p + 1` no suma 1 byte — suma `sizeof(*p)` bytes. Esto permite recorrer arrays como si fueran punteros, porque los elementos son contiguos. Es la fuente principal de inseguridad.
- Dangling pointer: dos causas. La primera (`free(p)` sin `p = NULL`) es la más común en código legacy. La segunda (retornar `&local`) es un error de principiante en C que el compilador moderno a veces detecta con `-Wreturn-local-addr`.
- Consecuencias: lectura → basura o crash segmentación. Escritura → corrupción de heap que puede manifestarse como bug silencioso horas después. Este es el tipo de bug que cuesta días de debugging.

**Conceptos clave:** & y * ; aritmética de punteros; dangling pointer — dos causas y consecuencias
**Preguntas anticipadas:**
- *"¿Rust tiene punteros?"* → Sí, pero el sistema de ownership/borrowing garantiza en compilación que no existen dangling pointers. Es la solución moderna al problema.
**Transición:** "El otro problema del tipo puntero: perder la referencia al heap."

---

### [F-20] Memory leak y referencias vs. punteros
**Tiempo:** 10 min
**Qué decir:**
- Lost heap-dynamic variable: mostrar que reasignar `p` sin hacer `free` primero crea una celda de memoria inaccesible. El OS no la recupera hasta que el proceso termina. En procesos long-running (servidores, daemons), esto hace crecer el uso de memoria indefinidamente.
- La tabla de comparación es el núcleo de esta filmina. Recorrerla fila por fila:
  - Aritmética: punteros C pueden hacer `p + 3`, referencias TypeScript/Java no tienen esta operación.
  - Dangling pointer: imposible en TypeScript porque el GC mantiene el objeto vivo mientras haya una referencia activa.
  - Acceso a dirección: en TypeScript no se puede hacer `console.log(&variable)` — la abstracción oculta completamente la dirección de memoria.
- TypeScript compila a JavaScript que corre sobre V8 (u otro motor). V8 gestiona la memoria automáticamente con GC. El programador TypeScript nunca ve direcciones de memoria.
- El tradeoff: TypeScript es más seguro, pero con un GC con pauses de colección. C es más riesgoso pero con control total de memoria para código de tiempo real.

**Conceptos clave:** memory leak = celda sin referencia; GC previene dangling; tabla puntero vs. referencia; tradeoff seguridad/control
**Preguntas anticipadas:**
- *"¿TypeScript puede tener memory leaks?"* → Sí — si se mantienen referencias activas a objetos que ya no se necesitan (listeners no removidos, caches que crecen sin límite). El GC solo libera lo que no está referenciado.
**Transición:** "El null reference es un problema específico. Kotlin lo resuelve a nivel de sistema de tipos."

---

### [F-21] Null safety: el problema de los mil millones
**Tiempo:** 10 min
**Qué decir:**
- La cita de Hoare es impactante — el inventor del null reference se arrepiente de haberlo creado. Vale la pena contarla: en 1965, cuando diseñaba Algol W, Tony Hoare agregó null "por comodidad". Décadas después, calcula que costó mil millones de dólares en bugs, crashes y vulnerabilidades.
- En Java legacy: `Object o = null; o.toString()` → NullPointerException en runtime. Era históricamente la excepción #1 en logs de producción de aplicaciones Java.
- Por qué usamos Kotlin aquí (no TypeScript): el manejo de `null | undefined` en TypeScript fue cubierto en T09.2 (F-29 a F-33). Kotlin muestra la solución de una manera más limpia porque integra null safety directamente en el sistema de tipos con dos tipos distintos: `String` y `String?`.
- En Kotlin: `String` garantiza que NUNCA es null. `String?` puede ser null. Esta garantía la da el compilador — si un método retorna `String`, el llamador puede usar el resultado directamente sin verificar.
- El contraste con Java: en Java, cualquier referencia puede ser null. En Kotlin, solo las declaradas con `?`.

**Conceptos clave:** historia del null reference; T09.2 ya cubrió TypeScript; Kotlin: String vs. String?; garantía del compilador
**Preguntas anticipadas:**
- *"¿TypeScript strict mode equivale a Kotlin null safety?"* → Parcialmente. Con `strictNullChecks`, TypeScript requiere manejar `null | undefined`. Pero TypeScript admite casts inseguros (`as string`). Kotlin es más restrictivo.
**Transición:** "Los cuatro operadores null-safe de Kotlin."

---

### [F-22] Null safety: operadores Kotlin
**Tiempo:** 10 min
**Qué decir:**
- Recorrer los cuatro operadores con el ejemplo de las cadenas de acceso:
  - `?.` (safe call): si cualquier eslabón de la cadena es null, toda la expresión retorna null sin lanzar excepción. Es el equivalente null-safe de `.`.
  - `?:` (Elvis): valor por defecto si el resultado es null. Nombre curioso — girado 90° se parece a los ojos de Elvis Presley.
  - `!!` (non-null assertion): explicitar la advertencia. Este operador es "peligroso por diseño" — es la salida de escape del sistema. Usar solo cuando se tiene certeza absoluta (ej: validación previa de negocio). Es preferible `?:` con un throw explícito.
  - `let {}`: el bloque ejecuta solo si la expresión no es null. Permite operar con seguridad dentro del bloque.
- La cadena `persona?.direccion?.ciudad` es el patrón más común en código Kotlin real.
- La tabla de comparación al final: recordar que el equivalente TypeScript fue cubierto en T09.2. Esta filmina es sobre el modelo de Kotlin.

**Conceptos clave:** cuatro operadores null-safe; `?.` para cadenas; `?:` para defaults; `!!` con precaución; `let {}` para bloques
**Preguntas anticipadas:**
- *"¿Hay alguna forma de convertir `String?` a `String` sin `!!`?"* → Sí: `?: throw IllegalStateException("Esperaba non-null")` o `checkNotNull(valor)` con mensaje — ambos más seguros que `!!`.
**Transición:** "Bloque F: ¿cuándo dos tipos son compatibles?"

---

## BLOQUE F — Equivalencia, coerción y conversión (40 min)

---

### [F-23] Equivalencia de nombres
**Tiempo:** 10 min
**Qué decir:**
- La pregunta central: si defino dos clases con exactamente los mismos campos, ¿son el mismo tipo? La respuesta depende del lenguaje.
- Name equivalence dice: NO — cada declaración de tipo es un tipo nuevo, independientemente de su estructura.
- El ejemplo de Kotlin `Metros` vs. `Kilos` es muy didáctico: ambas envuelven un `Double`, pero son tipos distintos. El compilador rechaza pasar `Kilos` donde se espera `Metros`. Esto previene bugs reales (errores de unidades de medida han causado accidentes de satélites — el caso Mars Climate Orbiter de 1999).
- Pascal y Ada son los ejemplos clásicos de name equivalence estricta. Dos `RECORD` con exactamente los mismos campos son tipos distintos si tienen nombres distintos.
- Java/Kotlin usan name equivalence para clases: `class A` y `class B` con los mismos campos son tipos distintos.
- TypeScript NO — es principalmente estructural. Lo veremos en F-24.

**Conceptos clave:** name equivalence — mismo nombre = mismo tipo; cada declaración = tipo nuevo; prevención de bugs semánticos (unidades)
**Preguntas anticipadas:**
- *"¿Los `typealias` en Kotlin son name equivalence?"* → No — `typealias Metros = Double` crea un alias transparente, no un tipo nuevo. `Metros` y `Double` son intercambiables. Para name equivalence real en Kotlin, usar `value class` o `data class`.
**Transición:** "TypeScript usa el sistema opuesto: equivalencia estructural."

---

### [F-24] Equivalencia estructural — TypeScript
**Tiempo:** 10 min
**Qué decir:**
- TypeScript es el ejemplo canónico de sistema estructuralmente tipado. La pregunta no es "¿cuál es el nombre del tipo?" sino "¿tiene los campos y tipos correctos?"
- Mostrar los ejemplos progresivamente: primero `p1` (objeto anónimo) pasa — tiene `x: number` y `y: number`. Luego `p2` (anotado diferente) pasa. Luego `p3` (con campo extra) también pasa — un objeto puede tener más de lo requerido.
- El principio: "duck typing" con comprobación estática. Si tiene los campos necesarios, es compatible.
- Comparar con Go: las interfaces de Go también son estructurales — cualquier tipo que implemente los métodos de una interfaz la satisface sin declaración explícita.
- La tabla de comparación al final: notar que Java/Kotlin son nominales, TypeScript/OCaml/Go son estructurales.
- Este sistema tiene implicaciones profundas para el diseño de APIs: en TypeScript, dos módulos pueden comunicarse con tipos compatibles sin haber coordinado previamente.

**Conceptos clave:** TypeScript estructural puro; cualquier objeto con la forma correcta es compatible; subtype compatibility con campos extra; Duck typing estático
**Preguntas anticipadas:**
- *"¿TypeScript NUNCA usa name equivalence?"* → Para algunos casos sí: clases tienen un componente nominal cuando se usan con `instanceof`. Pero en general, el sistema es estructural.
**Transición:** "Habiendo visto ambos sistemas, comparemos sus tradeoffs."

---

### [F-25] Name vs. structural — comparación y tradeoffs
**Tiempo:** 10 min
**Qué decir:**
- La pregunta central de la filmina: si `A` y `B` tienen exactamente los mismos campos, ¿son compatibles?
- Structural (TypeScript, Go): sí. Name (Java, Kotlin): no.
- Recorrer la tabla de tradeoffs con ejemplos de la vida real:
  - Seguridad: Kotlin previene el bug de `Metros`/`Kilos`. TypeScript podría pasar `Kilos` donde se espera `Metros` sin error.
  - Flexibilidad: en TypeScript se puede usar cualquier objeto con la forma correcta sin imports explícitos. En Java hay que declarar `implements`.
  - Refactoring: en sistemas estructurales, cambiar el nombre de un campo puede romper compatibilidades ocultas que no son visibles localmente.
- El edge case de TypeScript: `calcularFuerza(peso)` donde `peso` es de tipo `Kilos` pero tiene la misma estructura que `Metros` — TypeScript acepta. Kotlin rechaza.
- La lección: TypeScript sacrifica name safety por composición flexible. Para sistemas críticos con dominio rico, Kotlin o Haskell son más seguros.
- Branded types en TypeScript (avanzado, opcional): `type Metros = number & { readonly brand: unique symbol }` — simula name equivalence. No entra al examen pero es bueno mencionar que existe.

**Conceptos clave:** name vs. structural tradeoffs; unidades de medida como motivación de name equivalence; branded types como solución en TypeScript
**Preguntas anticipadas:**
- *"¿Cuál es mejor para proyectos grandes?"* → Depende: TypeScript estructural facilita la integración entre módulos. Para dominios complejos con tipos que no deben mezclarse, un sistema nominal o branded types son más seguros.
**Transición:** "El último tema del Bloque F: coerción y conversión."

---

### [F-26] Coerción, conversión y mixed mode
**Tiempo:** 10 min
**Qué decir:**
- Distinguir coerción implícita de conversión explícita. La coerción la hace el compilador automáticamente — sin código del programador. La conversión es explícita — el programador la escribe.
- TypeScript/JS: el `+` con un string es el ejemplo más famoso. `"1" + 2 = "12"` — el número se coerciona a string para la concatenación. Es una fuente de bugs clásica en JavaScript.
- Widening (ensanchamiento): `Int` → `Long` → `Double`. Siempre seguro porque el rango crece — no hay pérdida de información. Java lo hace automáticamente. Kotlin no — requiere `.toLong()` explícito (decisión de diseño deliberada para claridad).
- Narrowing (achicamiento): `Double` → `Int`. Puede perder información — truncamiento. C lo hace silenciosamente. Kotlin requiere `.toInt()` explícito y avisa que hay truncamiento potencial.
- El bug clásico de C: `5 / 2 = 2`, no `2.5`. División entera — el resultado se trunca. Solución: `5.0 / 2 = 2.5`.
- Kotlin `as` para cast de tipos de referencia: si el objeto no es del tipo esperado, lanza `ClassCastException`. `as?` retorna null en vez de lanzar — más seguro en código que no controla el tipo exacto.

**Conceptos clave:** coerción implícita vs. conversión explícita; widening seguro / narrowing con pérdida; `+` string en JS; división entera C
**Preguntas anticipadas:**
- *"¿TypeScript strict mode detecta la coerción de `+`?"* → Solo si los tipos están bien anotados. Si una variable es `number | string`, el compilador puede no detectar el problema.
**Transición:** "Último bloque — polimorfismo. Probablemente el concepto más poderoso de toda la clase."

---

## BLOQUE G — Polimorfismo y sistemas paramétricos (85 min)

---

### [F-27] Sistemas monomórficos vs. polimórficos
**Tiempo:** 10 min
**Qué decir:**
- Motivar con el problema del código monomórfico: si escribo `sumarEnteros(a: number, b: number)`, ¿qué hago cuando necesito sumar bigints? ¿O concatenar strings? Duplico el código. El polimorfismo es la solución a ese problema.
- En C sin templates: la "solución" es `void*` — un puntero a cualquier tipo. Pero se pierde toda información de tipos en compilación → sin type safety. Es la peor opción para código de alto nivel.
- La función `identidad<T>` en TypeScript: una sola implementación, sirve para cualquier T. Cero duplicación.
- La taxonomía de Gabbrielli: universal (paramétrico + subtipo) vs. ad-hoc (sobrecarga + coerción). El universal es el "verdadero" polimorfismo porque una sola implementación funciona. El ad-hoc es polimorfismo de nombre — diferentes implementaciones con el mismo nombre.
- Anticipar los bloques: F-28 (sobrecarga), F-29-F-30 (paramétrico), F-31-F-32 (subtipo), F-32 (varianza).

**Conceptos clave:** monomórfico vs. polimórfico; taxonomía universal (paramétrico, subtipo) vs. ad-hoc (sobrecarga, coerción); identidad genérica
**Preguntas anticipadas:**
- *"¿El polimorfismo de Java con herencia es ad-hoc o universal?"* → Universal — es polimorfismo por subtipo (inclusión). Un método que acepta `Animal` acepta cualquier subtipo sin duplicar código.
**Transición:** "Empecemos por el ad-hoc: sobrecarga de funciones."

---

### [F-28] Polimorfismo ad-hoc: sobrecarga
**Tiempo:** 8 min
**Qué decir:**
- TypeScript sobrecarga: a diferencia de Java/Kotlin, TypeScript usa un sistema de "firmas de sobrecarga" + una implementación unificada. El compilador verifica que los llamadores usen una de las firmas válidas.
- Dispatch estático en Kotlin: el compilador de Kotlin resuelve en tiempo de compilación cuál función llamar según los tipos de los argumentos. Costo cero en runtime.
- Dispatch dinámico (virtual): cuando se usa `override`, el compilador genera una tabla de métodos virtuales (vtable). En runtime, se indexa la vtable para encontrar la implementación correcta del tipo real. Tiene un costo pequeño de indirección.
- La diferencia conceptual: el dispatch estático es resolución en compilación (más rápido). El dinámico es resolución en runtime (flexible, permite polimorfismo real).
- El límite de la sobrecarga: para N tipos, necesito N implementaciones con el mismo nombre. No es verdaderamente genérico — si aparece un tipo nuevo, hay que agregar otra firma.

**Conceptos clave:** TypeScript signature overloads; dispatch estático (compilación) vs. dinámico (runtime); vtable; límite de sobrecarga
**Preguntas anticipadas:**
- *"¿El dispatch dinámico es muy costoso?"* → El overhead es de 1-2 instrucciones de memoria (acceso a vtable + jump). En código normal no es relevante. En bucles críticos de alta frecuencia, puede importar — por eso C tiene funciones de puntero.
**Transición:** "Para escribir una sola función para todos los tipos, necesitamos generics."

---

### [F-29] Polimorfismo paramétrico: generics
**Tiempo:** 10 min
**Qué decir:**
- El concepto clave: el parámetro de tipo `<T>` es una *variable de tipo* — se instancia cuando se llama la función.
- Mostrar `primero<T>(lista: T[]): T | undefined`. En la invocación `primero([1, 2, 3])`, TypeScript infiere `T = number`. En `primero(["a", "b"])`, infiere `T = string`. Una implementación, infinitos tipos.
- `Maybe<T>` como el tipo genérico canónico de la programación funcional: encapsula la posencia de un valor sin usar null. Es la alternativa funcional al null safety de Kotlin. `mapMaybe` es una función de orden superior genérica — muestra que los genéricos y HOF se complementan.
- Haskell: el sistema paramétrico más puro — `identidad :: a -> a` es totalmente genérico. Las minúsculas `a, b, c` son variables de tipo. La signatura `fmap :: (a -> b) -> Maybe a -> Maybe b` dice: "dada una función de a a b, convierte Maybe a en Maybe b" — sin saber nada sobre a o b.
- TypeScript vs. Haskell: TypeScript requiere anotaciones en funciones públicas (`<T>`). Haskell las infiere automáticamente. Ambos son paramétricos — difieren en cuánta inferencia aplican.

**Conceptos clave:** variable de tipo T; instanciación en llamada; Maybe<T> como tipo canónico; Haskell inferencia de tipo paramétrico
**Preguntas anticipadas:**
- *"¿Los generics de TypeScript son los mismos que los de Java?"* → Similar en superficie, diferente en implementación. Java usa type erasure — en runtime no hay información del tipo T. TypeScript compila a JS que tampoco tiene tipos — mismo efecto.
**Transición:** "Cuando T no puede ser cualquier cosa, necesitamos constraints."

---

### [F-30] Generics con constraints
**Tiempo:** 10 min
**Qué decir:**
- Motivar con el error: `function max<T>(a: T, b: T)` no compila porque TypeScript no sabe si T tiene `>`. El operador `>` no es válido para cualquier tipo (¿qué significa `> ` para dos funciones?).
- La solución: `extends` en TypeScript actúa como constraint. `T extends { valueOf(): number }` dice "T debe tener un método `valueOf` que retorne number".
- Kotlin `upper bound`: `<T : Comparable<T>>` dice "T debe implementar la interfaz `Comparable<T>`". Es más idiomático y legible que el TypeScript equivalente.
- Haskell typeclasses: el sistema más expresivo. `Ord a =>` significa "a debe pertenecer a la typeclass Ord". Las typeclasses son contratos de comportamiento — similar a interfaces pero más flexibles (se pueden agregar instancias retroactivamente).
- Múltiples constraints: TypeScript usa intersección de tipos. Kotlin usa `where`. Haskell usa `(Ord a, Show a) =>`. Todos el mismo concepto con diferente sintaxis.
- El punto pedagógico: bounded quantification = polimorfismo paramétrico con restricción. Es más poderoso que sobrecarga (genérico) pero más controlado que polimorfismo universal sin bounds.

**Conceptos clave:** por qué T genérico no puede hacer todo; extends como constraint; Kotlin upper bounds; Haskell typeclasses
**Preguntas anticipadas:**
- *"¿Las typeclasses de Haskell son lo mismo que las interfaces de TypeScript/Java?"* → Similar en propósito, diferente en poder. Las typeclasses permiten retroactive conformance — se puede hacer que un tipo existente implemente una typeclass sin modificarlo. Las interfaces requieren declaration-site conformance.
**Transición:** "Polimorfismo por subtipo — cuando un tipo puede reemplazar a otro."

---

### [F-31] Polimorfismo por subtipo y el principio de Liskov
**Tiempo:** 10 min
**Qué decir:**
- El LSP es un principio fundamental de diseño OOP — no solo de tipos. Enunciado fuerte: si reemplazo `Animal` por `Perro`, el programa debe funcionar correctamente. No solo "compilar" — funcionar correctamente.
- El ejemplo TypeScript muestra el polimorfismo en acción: `hacerHablar` acepta `Animal`, pero en runtime puede recibir `Perro` o `Gato`. El dispatch dinámico decide qué `hablar()` llamar.
- TypeScript estructural vs. Kotlin nominal: en TypeScript, `Perro` es subtipo de `Animal` si tiene todos los métodos de `Animal` con tipos compatibles — sin `extends` explícito. En Kotlin, requiere declaración.
- LSP y diseño: hay violaciones clásicas del LSP. El ejemplo canónico: `Cuadrado extends Rectángulo`. Si `Rectángulo` tiene `setAncho` y `setAlto` independientes, `Cuadrado` no puede satisfacer eso sin violar la invariante de cuadrado. El LSP dice: `Cuadrado <: Rectángulo` en ese diseño es incorrecto aunque matemáticamente un cuadrado es un rectángulo.
- Esto conecta directamente con la siguiente filmina sobre varianza.

**Conceptos clave:** LSP formal; dispatch dinámico para polimorfismo; violaciones de LSP en diseño OOP
**Preguntas anticipadas:**
- *"¿LSP aplica solo a OOP?"* → El principio aplica a cualquier relación de subtipado — funcional también. En Haskell, si `Ord a` implica `Eq a`, cualquier función que funcione para `Ord` debe funcionar para superconjuntos.
**Transición:** "La pregunta más sutil sobre subtipado: ¿cómo se propaga a través de tipos genéricos?"

---

### [F-32] Varianza: covarianza y contravarianza
**Tiempo:** 10 min
**Qué decir:**
- La pregunta de varianza sorprende a la mayoría: "¿Si Perro <: Animal, es Lista<Perro> <: Lista<Animal>?" La respuesta intuitiva es sí — pero depende de si la lista es mutable.
- Covarianza con lista mutable (el problema de TypeScript): si `Array<Perro>` fuera subtipo de `Array<Animal>`, podríamos agregar un `Gato` a través de la referencia `Array<Animal>` — pero el objeto subyacente es `Array<Perro>`. Ahora tenemos un Gato en un array de Perros. Esto rompe la type safety. TypeScript lo permite (decisión pragmática, sacrifica soundness).
- Kotlin lo resuelve: `List<out T>` (read-only) es covariante — solo puede producir T, nunca consumir. Seguro para leer. `MutableList<T>` es invariante — no es ni covariante ni contravariante.
- Contravarianza: más contraintuitivo. `Consumer<Animal>` puede usarse donde se espera `Consumer<Perro>` porque consume animales — y los perros son animales. Kotlin `in T` marca esto.
- Regla mnemotécnica (PECS — Producer Extends, Consumer Super en Java / `out` produce, `in` consume en Kotlin).
- `Comparable<in T>` es el ejemplo clásico de contravarianza: si puedo comparar animales, puedo comparar perros (porque los perros son animales). El comparador de animales funciona para cualquier subtipo de animal.

**Conceptos clave:** covarianza (out, read-only); contravarianza (in, write-only); invarianza (mutable); TypeScript covariante unsound; Kotlin out/in
**Preguntas anticipadas:**
- *"¿Cómo memorizo cuál es cuál?"* → Covarianza: la relación de subtipado se preserva en la misma dirección (`out` = produce, igual que generics normales). Contravarianza: se invierte (`in` = consume, el supertipo puede procesar subtipos).
**Transición:** "Cierre con inferencia de tipos — cómo el compilador deduce los tipos automáticamente."

---

### [F-33] Inferencia de tipos: Hindley-Milner
**Tiempo:** 10 min
**Qué decir:**
- El motivador: el alumno ya vio que TypeScript infiere tipos locales. La inferencia no es magia — es un algoritmo que resuelve ecuaciones de tipos.
- Hindley-Milner (1969/1978): el algoritmo estándar para inferencia de tipos en lenguajes funcionales. Inventado independientemente. Garantiza que se infiere el tipo más general posible (el tipo "principal").
- Haskell: la mayoría del código no necesita anotaciones de tipo. El compilador infiere `identidad x = x` como `a -> a` — el tipo más general. Para `sumar x y = x + y`, infiere `Num a => a -> a -> a` — cualquier tipo numérico.
- TypeScript: inferencia local excelente (variables, retornos de lambdas), pero requiere anotaciones en firmas de funciones públicas. Esta es una decisión de diseño deliberada para legibilidad de APIs — no una limitación del algoritmo.
- El resultado pedagógico: cuando el compilador infiere un tipo, no adivina — resuelve un sistema de ecuaciones donde cada expresión contribuye una restricción. La inferencia es determinista y correcta.
- Conexión con T14: en T14 se estudia el Algoritmo W formalmente. Hoy solo la intuición.

**Conceptos clave:** Algoritmo W; tipo principal (más general); Haskell = inferencia completa; TypeScript = inferencia local + anotaciones en APIs
**Preguntas anticipadas:**
- *"¿TypeScript podría inferir los tipos de funciones públicas sin anotaciones?"* → Técnicamente sí — el algoritmo existe. La decisión de requerirlos es pedagógica y de mantenibilidad: las anotaciones son documentación del contrato público.
**Transición:** "Cerramos con la síntesis de toda la clase."

---

### [F-34] Cierre — Síntesis y conexiones curriculares
**Tiempo:** 5 min
**Qué decir:**
- Recorrer la tabla rápidamente — cada fila evoca una sección entera de la clase. Preguntar si hay gaps.
- Conexiones curriculares: T09.1/T09.2 → T10.1 → T11 → T14. Hoy fue el corazón de la teoría de tipos. T11 (estructuras de control) usa tipos para expresar el tipo de retorno y el tipo de las condiciones. T14 profundiza formalmente.
- Anunciar el TP: análisis comparativo TypeScript vs. Kotlin/Haskell en type safety. Los alumnos ven cómo se aplica lo aprendido hoy.
- Pregunta de cierre al aula: "¿Qué diferencia fundamental hay entre tipo producto y tipo suma?" y "¿En qué se diferencia polimorfismo paramétrico de polimorfismo por subtipo?" — verificación rápida de objetivos clave.

**Conceptos clave:** mapa completo del tema; conexiones curriculares; anuncio TP
**Cierre de clase:**
- Resumir en una línea: "Hoy construimos el mapa formal de los tipos: primitivos, producto, suma, recursivos, y la dimensión del polimorfismo que los atraviesa."
- Próxima clase: Tema 11 — Estructuras de Control.

---

## Notas logísticas

| Item | Detalle |
|------|---------|
| Pausas | 10 min después de F-18 (checkpoint); hydration break implícita en F-21 |
| Material de apoyo | Sebesta Cap. 6, 11; Gabbrielli Cap. 8; Louden Cap. 8 |
| Actividades opcionales | A1/A2 (C union → TypeScript sealed) después de F-16; A3/A4 (punteros/null) después de F-22; A5 (structural vs nominal) después de F-25; A6 (generics con bounds) después de F-30 |
| Tiempo total estimado | 362 min (dentro de constraint 360 ± 5%) |
| Si falta tiempo | Comprimir F-33 (HM) a 5 min — es marcado como trasladable a T14 |
| Si sobra tiempo | Expandir F-16 con más ejemplos de TypeScript discriminated unions o F-32 con varianza en funciones |
