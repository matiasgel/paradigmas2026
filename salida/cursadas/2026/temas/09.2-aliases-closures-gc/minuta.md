# Minuta — Tema 09.2: Aliases, Closures, GC y Tipos

**Materia:** Paradigmas y Lenguajes de Programación 2026
**Duración:** 120 min (1 clase)
**Agente:** Dr. Roberto ✍️ — Class Writer · 2026-06-28
**Corregido contra:** `clase_dada.txt` (1102 líneas) + ChromaDB
**Estado:** ✅ Corregido — pendiente de revisión docente

---

## Objetivos de la clase

| # | Objetivo | Bloom |
|---|---|---|
| OA1 | Analizar aliases: identificar fuentes, razonar sobre implicancias en verificación formal y análisis estático | Analizar |
| OA2 | Analizar closures: comparar deep vs. shallow binding, evaluar consecuencias en ciclo de vida de variables | Analizar |
| OA3 | Comparar garbage collection (reference counting vs. mark-sweep) con gestión manual y por ownership | Analizar |
| OA4 | Explicar gradual typing y el rol de TypeScript como lenguaje gradualmente tipado | Comprender |
| OA5 | Contrastar variables mutables (imperativo) con bindings inmutables (funcional) en Haskell, Scala y TypeScript | Analizar |
| OA6 | Aplicar type narrowing en TypeScript para manejar union types de forma segura | Aplicar |
| OA7 | Detectar errores de aliases, mutabilidad y closures en código generado por IA; proponer correcciones | Evaluar |

---

## Mapa de tiempos

| Bloque | Slides | Tiempo |
|---|---|---|
| Portada | F-00 | 2 min |
| Bloque 1 — Aliases | F-01 a F-07 | 15 min |
| Bloque 2 — Closures | F-08 a F-16 | 20 min |
| Bloque 3 — GC | F-17 a F-26 | 22 min |
| Bloque 4 — Gradual Typing | F-27 a F-33 | 16 min |
| Bloque 5 — FP Inmutabilidad | F-34 a F-39 | 14 min |
| Bloque 6 — Contraste multilenguaje | F-40 a F-42 | 8 min |
| Bloque 7 — Bloque IA | F-43 a F-47 | 12 min |
| Cierre | F-48 | 5 min |
| Buffer / preguntas | — | 6 min |
| **Total** | | **120 min** |

---

## Trazabilidad bibliográfica (ChromaDB)

Las citas usadas en filminas y minuta están respaldadas por ChromaDB contra los 3 libros del curso:

| Referencia | Fuente ChromaDB | Capítulo / Sección |
|---|---|---|
| Aliases — definición y fuentes | Sebesta, *Concepts of PL* (Pearson 2019) | Cap. 5 §5.3.3 (p. 221-258) |
| Aliases por paso por referencia — 3 escenarios | Sebesta | Cap. 9 §9.5 (p. 389-440) |
| Closures — deep vs. shallow binding | Gabbrielli & Martini, *PL: Principles and Paradigms* (Springer 2023) | §7.4 (p. 136-282) |
| Closures — makeAdder | Sebesta | Cap. 10 §10.6 (p. 441-470) |
| GC — mark-and-sweep | Sebesta | §6.11 (p. 259-324) |
| GC — reference counting, ciclos | Louden & Lambert, *PL: Principles and Practices* (Cengage 2012) | §10.5 (p. 448-495) |
| GC — tres defectos del mark-sweep + compactación | Gabbrielli & Martini | §8.11 (p. 136-282) |
| Gradual typing — TypeScript | Gabbrielli & Martini | §16.9 (p. 533-574) |
| Transparencia referencial | Sebesta §7.4 (p. 325-388); Louden §9.1 (p. 406-447) | — |
| Rust — ownership y borrow checker | Gabbrielli & Martini | Cap. 16 (p. 533-574) |

---

## PORTADA

---

### [F-00] Portada

**Tiempo:** 2 min

**Qué decir:**
- Presentar la continuación de la clase anterior: "Semana pasada formalizamos la variable como 5-tupla, los momentos de binding y el ámbito estático. Hoy arrancamos donde quedamos: dos nombres que apuntan al mismo objeto."
- Mencionar la estructura: aliases → closures → garbage collection → gradual typing → FP → bloque IA.
- Señalar el prerequisito: quien no vio la clase 09.1 va a tener lagunas en binding y ciclo de vida.

**Conceptos clave:**
- La clase 09.2 es la segunda parte del bloque Variables/Binding
- La 5-tupla de 09.1 es el lenguaje base para todo lo de hoy

**Preguntas anticipadas:** ninguna en portada.

**Transición:** Arrancamos con el primer concepto: ¿qué pasa cuando dos nombres apuntan al mismo objeto?

---

## BLOQUE 1 — Aliases: Dos Nombres, Un Objeto (15 min)

---

### [F-01] ¿Qué es un alias?

**Tiempo:** 2 min

**Qué decir:**
- Definición de Sebesta §5.3.3: un alias ocurre cuando **dos nombres distintos** están vinculados a la **misma celda de memoria** en el mismo momento. No dos celdas con el mismo valor — una sola celda con dos nombres.
- La diferencia con una copia: una copia crea una celda nueva con el mismo contenido — dos L-values distintos. Un alias no crea nada nuevo — solo agrega un segundo nombre que apunta al mismo L-value.
- Remarcar las tres consecuencias: (1) cambiar desde uno afecta el otro silenciosamente, (2) el verificador formal pierde capacidad de razonamiento, (3) el compilador no puede optimizar porque no sabe si los punteros se solapan.
- Fuentes principales: asignación de referencias, parámetros por referencia, union types.

**Conceptos clave:**
- Alias = dos nombres, una sola celda (L-value compartido)
- La modificación es silenciosa: el programador puede no notar que hay dos nombres
- El compilador no puede asumir que dos nombres distintos apuntan a celdas distintas

**Preguntas anticipadas:**
- *"¿Un alias es siempre un bug?"* → No. A veces es intencional: pasar un objeto por referencia para modificarlo es usar aliases a propósito. El problema es cuando es accidental.
- *"¿En lenguajes funcionales hay aliases?"* → Buena pregunta — la contestamos en el bloque 5. Anticipar: en FP puro no hay mutación, así que los aliases son inofensivos.

**Transición:** Veamos la fuente más común de aliases en TypeScript — la asignación de referencia de objeto.

---

### [F-02] Alias por asignación de referencia — TypeScript

**Tiempo:** 2 min

**Qué decir:**
- Empezar con el ejemplo TypeScript: `const obj2 = obj1`. Preguntar al grupo si `obj2` es una copia o un alias. Esperar respuestas — la mayoría sabe la respuesta correcta pero no por qué.
- Explicar: en TypeScript, los objetos se pasan por referencia. La asignación `obj2 = obj1` no copia el objeto — copia la **referencia** (el puntero al heap). El L-value de `obj2` y el de `obj1` son el mismo.
- Mostrar la comprobación: `obj1 === obj2` es `true` — misma identidad de objeto.
- Contrastar con primitivos: `let y = x` sobre un número sí copia el valor — `x` y `y` son L-values independientes. Los primitivos no tienen alias por asignación — los objetos sí.

**Conceptos clave:**
- Asignación de objeto en TypeScript = copiar la referencia (el puntero), no el objeto
- Los primitivos se copian por valor — los objetos se comparten por referencia
- `obj1 === obj2` devuelve `true` cuando son aliases — misma identidad

**Preguntas anticipadas:**
- *"¿Los primitivos también tienen este problema?"* → No. Los primitivos (`number`, `boolean`, `string`) se pasan por valor — se copia el dato. Solo los objetos y arrays son por referencia.
- *"¿Esto pasa en Python también?"* → Exactamente igual. `a = b` sobre una lista en Python es un alias.

**Transición:** El alias también aparece cuando pasamos un objeto a una función — el parámetro es un alias del argumento.

---

### [F-03] Alias a través de parámetros — Kotlin y Go

**Tiempo:** 2 min

**Qué decir:**
- Kotlin: el parámetro `p` recibe la misma referencia que `origen`. El método `desplazar` modifica el objeto original a través del alias `p`. El caller no lo ve de forma obvia — fuente de bugs silenciosos.
- Go: punteros explícitos — el alias es visible en la firma de la función (`*int`, `&x`). En Go el alias es explícito (el `&` y el `*`): más visible que en Kotlin o TypeScript.
- Mensaje: en TypeScript y Kotlin el alias es implícito para objetos. En Go es explícito con `&` y `*`.

**Conceptos clave:**
- Pasar un objeto a una función = crear un alias dentro de esa función
- TypeScript y Kotlin hacen el alias implícito — Go lo hace explícito con `&`
- El alias por parámetro es la fuente más común de efectos laterales invisibles

**Preguntas anticipadas:**
- *"¿En Go se puede pasar por valor?"* → Sí — si no se usa `&`, Go pasa una copia. El `&` es explícito y opt-in.

**Transición:** Tenemos aliases. ¿Qué consecuencias tienen para el razonamiento sobre el programa?

---

### [F-04] Consecuencias de los aliases

**Tiempo:** 2 min

**Qué decir:**
- El problema de razonabilidad local: si `f(a, b)` recibe dos parámetros que son aliases del mismo objeto, el supuesto de independencia falla silenciosamente. Modificar `b` modifica `a` — resultados inesperados.
- Impacto en verificación formal: las precondiciones de la lógica de Hoare no se pueden establecer correctamente con aliases. El análisis estático no puede probar ausencia de efectos laterales. El compilador pierde oportunidades de optimización.
- Impacto en concurrencia: dos threads con aliases al mismo objeto necesitan sincronización explícita. Sin ella: race condition — resultado no determinístico.
- Regla de diseño defensivo: las funciones puras no deberían modificar sus parámetros. Usar `readonly` en TypeScript / `val` en Kotlin para comunicar esa intención.

**Conceptos clave:**
- Los aliases rompen el supuesto de independencia entre parámetros
- La verificación formal (lógica de Hoare) no funciona con aliases ocultos
- Race conditions en concurrencia cuando dos threads comparten un alias

**Preguntas anticipadas:**
- *"¿El compilador detecta aliases automáticamente?"* → En general no. El compilador asume que dos nombres distintos pueden apuntar a la misma celda. Por eso no puede optimizar.

**Transición:** Sebesta identifica tres categorías específicas de alias involuntarios por paso por referencia. Veamos los tres escenarios.

---

### [F-04b] Alias por colisión en paso por referencia — tres escenarios de Sebesta §9.5

**Tiempo:** 2 min

**Qué decir:**
- Sebesta §9.5 describe tres escenarios donde el paso por referencia crea aliases involuntarios:
  1. **Colisión entre parámetros actuales:** `fun(a, a)` — dos parámetros formales son aliases del mismo argumento. Comportamiento dependiente de implementación en C++.
  2. **Parámetro y variable global:** el argumento pasado por referencia coincide con una variable global accesible dentro de la función — dos caminos al mismo dato.
  3. **Elemento de array y array completo:** `fun1(list[i], list)` — el primer parámetro es alias de `list[i]`, el segundo da acceso a todo el array incluyendo `list[i]`.
- El diagnóstico de Sebesta: "Los problemas con estos tipos de aliasing son los mismos que en otras situaciones de aliasing: hacen que los programas sean difíciles de leer y mantener."
- Sebesta propone **pass-by-value-result** como alternativa que elimina los tres escenarios.

**Conceptos clave:**
- Tres escenarios de alias involuntario por paso por referencia (Sebesta §9.5)
- Pass-by-value-result los elimina: copia al inicio, escritura al final
- El problema no es teórico — aparece en listas enlazadas, árboles con padre, grafos

**Preguntas anticipadas:**
- *"¿TypeScript tiene paso por referencia explícito?"* → No. TypeScript pasa objetos por referencia implícitamente. No hay `ref` como en C#. Los tres escenarios de Sebesta aplican igual.

**Transición:** TypeScript tiene una herramienta para detectar mutaciones involuntarias a través de aliases: `readonly`.

---

### [F-05] `readonly` como guardrail contra aliases peligrosos

**Tiempo:** 2 min

**Qué decir:**
- Sin `readonly`: el parámetro es un alias del argumento y puede mutarlo. `data.push(99)` muta el array ORIGINAL del caller — efecto lateral invisible.
- Con `readonly`: el compilador impide cualquier mutación del objeto recibido. `data.push(99)` da error de compilación. La solución es crear un nuevo array: `return [...data, 99]`.
- `Readonly<T>` para objetos — protege todas las propiedades de primer nivel. El compilador rechaza `cfg.host = "otro"`.
- Importante: `readonly` no impide crear el alias — impide **modificar a través del alias**. Es un guardrail, no una solución completa.

**Conceptos clave:**
- `readonly` en TypeScript impide modificar a través de la referencia
- `readonly` no previene el alias — previene la mutación a través de él
- El compilador con `strict: true` detecta violaciones de `readonly` en compilación

**Preguntas anticipadas:**
- *"¿`readonly` hace una copia internamente?"* → No. El objeto sigue siendo el mismo — solo cambia lo que el compilador permite hacer con él.

**Transición:** Sabemos detectar aliases con `readonly`. ¿Cómo los eliminamos cuando necesitamos una copia verdadera?

---

### [F-06] Shallow copy — el alias sobrevive en los niveles anidados

**Tiempo:** 2 min

**Qué decir:**
- El spread operator `{ ...original }` copia solo el primer nivel — los anidados siguen siendo aliases.
- Nivel 0: independiente. `copia.nombre = "Carlos"` no afecta `original.nombre`.
- Nivel 1 (objetos anidados): ALIAS. `copia.config.debug = false` modifica `original.config.debug` también.
- Nivel 1 (arrays anidados): ALIAS. `copia.tags.push("guest")` modifica `original.tags`.
- Comprobación: `original.config === copia.config` es `true` — mismo L-value.

**Conceptos clave:**
- Shallow copy (`{ ...obj }`) → el primer nivel es independiente, los anidados son aliases
- El spread copia referencias, no objetos — los sub-objetos se comparten
- Para objetos planos alcanza; para anidados necesitas deep copy

**Preguntas anticipadas:**
- *"¿`Array.from(arr)` también es shallow?"* → Sí. Copia el array nuevo pero los elementos objeto siguen siendo aliases.

**Transición:** Para eliminar el alias en todos los niveles necesitamos deep copy.

---

### [F-07] Deep copy con `structuredClone` — ningún nivel queda como alias

**Tiempo:** 1 min

**Qué decir:**
- `structuredClone()` (ES2022) es la única forma estándar de obtener una copia completa en todos los niveles.
- Nivel 0: independiente. Nivel 1 (objetos): independiente. Nivel 1 (arrays): independiente.
- Comprobación: `original.config === copia.config` es `false` — L-values distintos.
- Nota: `structuredClone` no copia funciones, símbolos ni prototipos. Para esos casos: `JSON.parse(JSON.stringify(obj))` (limitado) o librerías como lodash.cloneDeep.
- Regla práctica: si el objeto es plano → spread alcanza. Si hay anidación → `structuredClone()`.

**Conceptos clave:**
- Deep copy (`structuredClone()`) → ningún nivel comparte celda — ES2022
- Elegir según si el objeto tiene niveles anidados que necesitamos independizar
- `structuredClone` no copia funciones ni símbolos — limitación a conocer

**Preguntas anticipadas:**
- *"¿Existe `JSON.parse(JSON.stringify(obj))`?"* → Sí, es el deep copy clásico antes de ES2022. Problema: no funciona con `Date`, `undefined`, `Map`, `Set`, funciones. `structuredClone()` maneja más tipos.

**Transición:** Comprendimos aliases. Ahora el segundo gran tema: ¿qué pasa cuando una función "recuerda" el entorno en el que fue creada? Eso es una closure.

---

## BLOQUE 2 — Closures: el Entorno que Viaja con la Función (20 min)

---

### [F-08] ¿Qué es una closure?

**Tiempo:** 2 min

**Qué decir:**
- Definición de Sebesta §10 y Gabbrielli §7.4: una closure es la combinación de una **función** y el **entorno léxico** en el que fue definida.
- La intuición: la función "viaja" con una mochila — esa mochila tiene las variables de su ámbito de creación. Aunque ese ámbito haya cerrado (el activation record se destruyó), la mochila sigue disponible.
- El ciclo de vida extendido: las variables locales ordinarias viven en el stack — se destruyen cuando la función retorna. Las variables capturadas por una closure no pueden vivir en el stack: deben migrar al **heap**. Viven mientras al menos una closure mantenga una referencia a ellas.
- Las closures aplican **deep binding**: el entorno se captura al crear la closure, no al llamarla. Las variables capturadas son variables heap-dynamic implícitas (Categoría 3 del Tema 09.1).

**Conceptos clave:**
- Closure = función + entorno léxico capturado al momento de la creación
- Las variables capturadas migran del stack al heap con duración extendida
- Deep binding: el entorno se captura al crear, no al llamar

**Preguntas anticipadas:**
- *"¿Qué es el entorno léxico exactamente?"* → Es el conjunto de variables accesibles en el ámbito donde la función fue **definida** (no donde se llama). Viene del ámbito estático que vimos en 09.1.

**Transición:** Veamos una closure concreta en TypeScript y analicemos qué pasa con el ciclo de vida de la variable capturada.

---

### [F-09] Closure en TypeScript — contador con estado compartido

**Tiempo:** 2 min

**Qué decir:**
- Recorrer el código de `crearContador` línea por línea. Preguntar: "cuando `crearContador(10)` retorna, ¿qué pasa con `cuenta`?"
- La respuesta esperada habitual: "se libera porque la función terminó". La respuesta correcta: **no se libera** — `cuenta` escapa al heap porque el objeto retornado mantiene referencias a ella.
- Demostrar con los `console.log`: después de que `crearContador()` retornó, `c.incrementar()` sigue funcionando. Si `cuenta` se hubiera liberado, esto fallaría.
- Las tres closures (incrementar, decrementar, valor) **comparten la misma celda heap** de `cuenta`. Son aliases de la misma variable — pero aliases controlados y encapsulados.

**Conceptos clave:**
- `cuenta` escapa al heap porque la closure la mantiene referenciada
- El activation record de `crearContador` se destruyó — `cuenta` sobrevivió en heap
- Las tres closures comparten la misma celda — aliases encapsulados

**Preguntas anticipadas:**
- *"¿Cómo sabe el motor que `cuenta` escapó al heap?"* → V8 usa "escape analysis" en la compilación JIT: detecta que `cuenta` es referenciada por las funciones retornadas y la aloja en el heap desde el principio.

**Transición:** ¿Por qué `cuenta` no se destruye? Formalicemos el ciclo de vida.

---

### [F-10] ¿Por qué `cuenta` no se destruye? — ciclo de vida de variables capturadas

**Tiempo:** 2 min

**Qué decir:**
- Variables locales ordinarias — tiempo de vida de stack: se crean al llamar la función, se destruyen al retornar. Sin costo de GC — liberación inmediata e implícita.
- Variables capturadas por closure — tiempo de vida de heap: el compilador detecta que la variable "escapa" al scope de la función. Migra al heap. Vive mientras al menos una closure activa tenga una referencia. El GC la libera cuando ninguna closure la referencia.
- ¿Qué significa "escapar"? Una variable escapa cuando su lifetime debe ser mayor que el del activation record que la contiene: cuando una función anidada la captura, cuando se retorna una referencia a ella, o cuando se almacena en una estructura con mayor lifetime.
- Implicación práctica: si una closure se mantiene viva indefinidamente, todas las variables que captura también se mantienen vivas. Conecta con GC del bloque 3.

**Conceptos clave:**
- Variables capturadas → Categoría 3 (heap-dynamic), no Categoría 2 (stack-dynamic)
- "Escapar" = lifetime mayor que el del activation record contenedor
- El ciclo de vida de una variable capturada dura mientras dure la closure que la captura

**Preguntas anticipadas:** ninguna típica en este punto.

**Transición:** Gabbrielli plantea formalmente por qué las variables capturadas no pueden vivir en el stack.

---

### [F-10b] La closure como solución al problema del dangling reference — Gabbrielli §7.4

**Tiempo:** 2 min

**Qué decir:**
- La pregunta de Gabbrielli §7.4: cuando una función F retorna una función interna `gg` que captura la variable local `x`, el entorno de F será destruido al terminar su ejecución. ¿Cómo invocar `gg` sin producir una referencia colgante a `x`?
- En C, retornar un puntero a una variable local produce exactamente eso: un **dangling reference** — apunta a stack memory ya reciclada. Es un bug.
- La solución: migración al heap garantizada por el runtime. El compilador detecta que `x` escapa, la aloja en el heap desde el inicio, el closure object contiene una referencia directa a esa celda heap. Cuando F retorna, `x` en heap sigue viva. El GC libera `x` solo cuando ninguna closure la referencia.
- La definición formal de Gabbrielli: "Clausuras: estructuras de datos compuestas por un fragmento de código y un entorno de evaluación. El modelo canónico para implementar la llamada por nombre y todas las situaciones en que una función debe pasarse como parámetro o retornar como resultado."

**Conceptos clave:**
- Gabbrielli §7.4: la closure resuelve el dangling reference migrando variables al heap
- Una closure es un par (código, entorno) — el entorno es el contexto léxico capturado
- En C retornar puntero a local = bug; en lenguajes modernos = garantía estructural

**Preguntas anticipadas:**
- *"¿Esto significa que todas las variables locales van al heap?"* → No. Solo las que escapan. El compilador hace escape analysis y solo migra las necesarias.

**Transición:** El mismo patrón existe en Python, Go y Kotlin. Veamos las diferencias sintácticas.

---

### [F-11] Closure en Python — `nonlocal` para escritura

**Tiempo:** 2 min

**Qué decir:**
- Python: las closures pueden leer variables capturadas sin declarar nada especial. Pero para **escribir** en ellas (modificarlas), se necesita `nonlocal`. Sin `nonlocal`, Python crea una variable local nueva con el mismo nombre — bug silencioso idéntico al de `var` en JS.
- Recorrer el código: `nonlocal total` es requerido para `total += n`. Sin `nonlocal`, al leer `total` antes de asignarle → `UnboundLocalError`.
- `obtener()` solo lee `total` — no necesita `nonlocal`. La lectura es siempre accesible; la escritura requiere declaración explícita.
- El estado persiste entre llamadas: `agregar(5)` → 5, `agregar(3)` → 8, `agregar(2)` → 10. `obtener()` → 10.

**Conceptos clave:**
- Python: `nonlocal` es necesario para modificar (no solo leer) la variable capturada
- Sin `nonlocal`: Python crea una variable LOCAL nueva — bug silencioso
- Lectura no necesita `nonlocal`; escritura sí

**Preguntas anticipadas:**
- *"¿Por qué Python exige `nonlocal`?"* → Para evitar ambigüedad: sin `nonlocal`, Python asume que cualquier asignación dentro de una función crea una variable local. `nonlocal` rompe esa asunción explícitamente.

**Transición:** Go y Kotlin soportan closures de primera clase con la misma semántica de captura.

---

### [F-12] Closures en Go y Kotlin

**Tiempo:** 1 min

**Qué decir:**
- Go: el código es casi idéntico al TypeScript. Go tiene closures de primera clase — la closure captura `cuenta` por referencia. El tipo de retorno `func() int` es una función sin argumentos que retorna int. La función retornada "lleva consigo" a `cuenta` en el heap.
- Kotlin: lambda con captura. Notar que en Kotlin la variable capturada debe ser `var` para poder modificarla desde la lambda — `val` daría error de compilación.
- Mensaje: el patrón es el mismo en TypeScript, Python, Go y Kotlin — es una propiedad del lenguaje, no de la sintaxis.

**Conceptos clave:**
- Go: closures de primera clase, captura por referencia, misma semántica que TypeScript
- Kotlin: la variable capturada debe ser `var` para modificarla desde la lambda
- El patrón es universal — no es específico de un lenguaje

**Preguntas anticipadas:**
- *"¿Java tiene closures?"* → Sí, a partir de Java 8 con lambdas. Pero con restricción: la variable capturada debe ser `final` o "effectively final" — no se puede modificar desde la lambda.

**Transición:** C no tiene closures — veamos la limitación por contraste.

---

### [F-13] C no tiene closures — la limitación por contraste

**Tiempo:** 1 min

**Qué decir:**
- C permite pasar punteros a funciones, pero esos punteros solo contienen la **dirección de inicio del código**. No existe ninguna estructura de datos para guardar el entorno en el que se definió la función.
- Consecuencias: si una función necesita acceder a estado entre llamadas → debe usar variable global o estructura pasada manualmente como parámetro extra (`void*` genérico). El programador debe gestionar manualmente el ciclo de vida de ese estado. La composición funcional es posible solo por convención.
- En TypeScript, Python, Go y Kotlin, el runtime detecta automáticamente: (1) qué variables escapan, (2) las mueve al heap, (3) les aplica GC cuando ya no son alcanzables. En C, todo ese trabajo recae en el programador.
- La comparación revela exactamente cuánto valor aporta el runtime de un lenguaje moderno.

**Conceptos clave:**
- C: function pointers = solo dirección de código, sin entorno
- Estado entre llamadas en C → variable global o `void*` manual
- El runtime de lenguajes modernos automatiza lo que en C es manual

**Preguntas anticipadas:**
- *"¿Se puede simular closures en C?"* → Sí, con `static` dentro de una función. Pero tiene el mismo problema que `var` en loops: una sola variable compartida entre todas las "instancias".

**Transición:** Ahora entendemos qué es una closure y dónde vive la variable capturada. El siguiente concepto es crítico: el momento en que se captura el entorno.

---

### [F-14] Deep binding vs. Shallow binding — el contrato de las closures

**Tiempo:** 2 min

**Qué decir:**
- **Deep binding** (la norma en todos los lenguajes modernos): el entorno se captura **en el momento de crear la closure**. Los nombres y sus valores "se congelan" en ese instante. Comportamiento: predecible e intuitivo — la closure siempre ve el entorno de su creación. Todos los lenguajes modernos usan deep binding: TypeScript, Python, Go, Kotlin, Haskell, Rust.
- **Shallow binding** (ámbito dinámico): el entorno se resuelve **en el momento de llamar la función**, no al crearla. Los nombres se buscan en la pila de llamadas activa en ese momento. LISP clásico (pre-Scheme) usaba shallow binding — prácticamente abandonado.
- La implicación práctica: con deep binding, el comportamiento de una closure es **local y cerrado** — depende solo de dónde fue definida en el código fuente, no de cómo llegó la ejecución hasta ella. Eso es exactamente lo que permite razonar sobre el código sin seguir toda la cadena de llamadas.

**Conceptos clave:**
- Deep binding (moderno): la closure captura el entorno en su **creación**
- Shallow binding (histórico): la función usa el entorno en su **llamada**
- Deep binding hace el comportamiento de la closure local y cerrado — predecible

**Preguntas anticipadas:**
- *"¿Shallow binding se usa hoy en algo?"* → Prácticamente no. Algunos lenguajes de scripting con `eval` dinámico pueden tener comportamientos similares, pero los lenguajes mainstream usan deep binding.

**Transición:** Veamos el ejemplo canónico de Sebesta: `makeAdder`.

---

### [F-14b] `makeAdder` — el ejemplo canónico de Sebesta §10.6.4

**Tiempo:** 2 min

**Qué decir:**
- Sebesta §10.6.4: `makeAdder` captura su parámetro `x` — cada llamada crea una celda heap distinta.
- `makeAdder(10)` crea la closure 1 con `x = 10` en heap — celda A. `makeAdder(5)` crea la closure 2 con `x = 5` en heap — celda B (independiente).
- Cada closure lee su propia celda — sin interferencia. `add10(1)` → 11 (celda A). `add5(7)` → 12 (celda B). `add10(10)` → 20 (celda A sigue siendo x=10).
- La cita de Sebesta: "La variable x referenciada en la función clausura está ligada al parámetro enviado a makeAdder. La función makeAdder se invoca dos veces: una con el parámetro 10 y otra con el parámetro 5, produciendo dos clausuras diferentes."
- Contraste con `crearContador` (F-09): `makeAdder` captura un **parámetro** (celda nueva por llamada, inmutable). `crearContador` captura una **variable local** (compartida entre closures, mutable).

**Conceptos clave:**
- `makeAdder`: cada llamada crea su propio activation record con su propio `x` — celdas independientes
- Parámetro capturado = celda nueva por invocación (binding fresco)
- Contraste: `crearContador` comparte `cuenta` entre tres closures; `makeAdder` no comparte

**Preguntas anticipadas:**
- *"¿Por qué `makeAdder` no comparte `x` entre closures?"* → Porque `x` es un parámetro — cada invocación de `makeAdder` crea un activation record nuevo con su propio `x`. Las variables locales de `crearContador` también son nuevas por invocación, pero las tres closures retornadas comparten la misma.

**Transición:** Ahora veamos el bug más famoso de JavaScript — el bug de `var` en loops con closures.

---

### [F-15] El bug clásico de `var` en loops — el código problemático

**Tiempo:** 2 min

**Qué decir:**
- `var` declara una variable en el scope de la **FUNCIÓN CONTENEDORA**, no del bloque. Hay exactamente UNA variable `i` para todo el loop.
- Todas las closures apuntan a la MISMA `i` (deep binding). Pero `i` es una sola celda de memoria — son aliases de ella.
- En este punto: `i === 3` (el loop terminó). Todas las closures leen la misma celda que ahora contiene 3: `funcs[0]()` → 3, `funcs[1]()` → 3, `funcs[2]()` → 3.
- El deep binding no es el bug — la captura es correcta. El bug es que `var` comparte la MISMA celda entre todas las iteraciones.

**Conceptos clave:**
- `var` en loops = un solo binding compartido = bug de closures en loops
- Deep binding capturó correctamente la REFERENCIA a `i` — el bug es que `var` hace que esa referencia sea compartida
- Todas las closures leen el valor final de `i` — no el valor que tenía cuando se crearon

**Preguntas anticipadas:**
- *"¿Cómo se evita el bug con `var` sin cambiar a `let`?"* → Con un IIFE: `(function(i){ funcs.push(() => i); })(i)`. Crea un nuevo scope por iteración. Solución pre-ES6 — hoy solo se usa `let`.

**Transición:** La corrección es `let` — una variable independiente por iteración.

---

### [F-16] Corrección con `let` — una variable independiente por iteración

**Tiempo:** 2 min

**Qué decir:**
- `let` crea una nueva variable `j` en CADA iteración del bloque `for`. Cada closure captura su PROPIA `j` — celda distinta en heap.
- Tres variables `j` distintas en el heap — tres closures, tres celdas independientes: `funcs2[0]()` → 0, `funcs2[1]()` → 1, `funcs2[2]()` → 2.
- Alternativa funcional — evita el problema por diseño: `Array.from({ length: 3 }, (_, k) => () => k)`. `Array.from` llama al callback con un parámetro `k` nuevo en cada invocación — bindings fresh.
- Regla práctica: en TypeScript moderno, nunca usar `var`. `let` y `const` tienen semántica de scope predecible.

**Conceptos clave:**
- `let` en loops = nuevo binding por iteración = comportamiento esperado intuitivamente
- `Array.from` funcional: el parámetro `k` es siempre un binding nuevo — el problema nunca existe
- Regla: nunca `var` en TypeScript moderno

**Preguntas anticipadas:**
- *"¿`const` también funciona en loops?"* → `const` no se puede usar como variable de loop (no se puede incrementar). Pero `for (const x of arr)` sí funciona — cada iteración tiene su propio binding de `x`.

**Transición:** Tenemos closures — y sabemos que las variables capturadas viven en el heap. ¿Quién las libera? Eso es el garbage collector.

---

## BLOQUE 3 — Garbage Collection: Memoria Automática (22 min)

---

### [F-17] El problema de la memoria en heap

**Tiempo:** 2 min

**Qué decir:**
- Revisión de categorías de variables y liberación (Tema 09.1): static (nunca se libera), stack-dynamic (libera al desapilar el frame), heap-dynamic (alguien debe decidir cuándo liberar).
- El dilema fundamental: liberar demasiado pronto → dangling pointer (crash o corrupción silenciosa). Liberar demasiado tarde → memory leak (el proceso crece). No liberar manualmente → necesitamos un mecanismo automático: el Garbage Collector.
- La pregunta que todo GC debe responder: ¿cuándo se puede liberar una celda del heap de forma segura? Respuesta: cuando no existe ninguna referencia viva a ella — es inaccesible desde el programa. El desafío es detectar esa condición de forma eficiente y correcta.

**Conceptos clave:**
- Stack → liberación automática al destruir el frame (Categoría 1 y 2)
- Heap → necesita mecanismo explícito de liberación (Categoría 3 y 4)
- Dilema: demasiado pronto = dangling; demasiado tarde = leak; automático = GC

**Preguntas anticipadas:**
- *"¿TypeScript tiene `delete` o `free`?"* → No. TypeScript no expone gestión manual de memoria. V8 lo maneja todo. Hay `delete obj.property` pero borra una propiedad, no libera la celda del heap.

**Transición:** Veamos las cuatro estrategias principales para gestionar la memoria heap.

---

### [F-18] Cuatro estrategias de gestión de memoria

**Tiempo:** 2 min

**Qué decir:**
- Recorrer la tabla fila por fila. No leer cada celda — comentar las diferencias clave.
- **Manual** (C, C++): el programador decide cuándo liberar. Problemas: dangling pointers, double-free, memory leaks.
- **Reference Counting** (Python, Swift, PHP): el runtime mantiene un contador por celda. Libera cuando el contador cae a 0. Problema: no resuelve ciclos de referencia.
- **Mark-and-Sweep** (Java, JavaScript/V8, Go): el GC marca todo lo alcanzable y libera lo no marcado. Problema: pausa el programa (stop-the-world).
- **Ownership + Drop** (Rust): el compilador hace análisis estático. Libera al salir del scope — garantía en compilación. Problema: modelo de programación más restrictivo.

**Conceptos clave:**
- Cuatro estrategias con distintos trade-offs entre determinismo, seguridad y rendimiento
- Manual = bugs; RC = no resuelve ciclos; Mark-Sweep = pausas; Ownership = restrictivo
- El curso se centra en RC y Mark-Sweep porque TypeScript usa una variante combinada

**Preguntas anticipadas:**
- *"¿Por qué no todos usan ownership como Rust?"* → Curva de aprendizaje alta, menor ecosistema para web/data, no es gradual. TypeScript es más práctico para muchos dominios.

**Transición:** Empecemos con la estrategia más intuitiva: contar cuántas referencias hay activas a cada objeto.

---

### [F-19] Reference Counting — la idea central

**Tiempo:** 2 min

**Qué decir:**
- El invariante: `ref_count(celda) = cantidad de variables/campos que apuntan a esa celda en este momento`. Cuando `ref_count == 0` → la celda es inaccesible → liberar inmediatamente.
- Ventajas: **determinístico** (la liberación ocurre en el instante exacto en que el contador llega a 0), **sin stop-the-world** (no hay que pausar el programa), **predecible** (en Python, `del x` libera inmediatamente), **localizado** (el costo se distribuye a lo largo del tiempo).
- La limitación fundamental: el algoritmo asume que `ref_count == 0` equivale a "inaccesible". Esa equivalencia es verdadera **en ausencia de ciclos**. Si dos objetos se apuntan mutuamente, sus contadores nunca llegan a 0 aunque el programa no pueda alcanzarlos — fuga de memoria estructural del algoritmo.

**Conceptos clave:**
- Liberación inmediata y determinista cuando el contador llega a 0
- Ventajas: determinístico, sin stop-the-world, localizado
- Limitación: no resuelve ciclos de referencia — fuga estructural del algoritmo

**Preguntas anticipadas:**
- *"¿Tiene overhead?"* → Sí: cada asignación de referencia incrementa/decrementa el contador. Para objetos muy efímeros en loops intensos, este overhead puede ser significativo.

**Transición:** Sebesta y Louden coinciden en el diagnóstico: RC y mark-sweep son procesos opuestos.

---

### [F-19b] Las ventajas y los dos problemas fundamentales del RC — Sebesta §6.11 + Louden §10.5

**Tiempo:** 2 min

**Qué decir:**
- Sebesta §6.11 describe el RC como incremental: la reclamación ocurre en el instante exacto en que una celda se vuelve inaccesible. Sin stop-the-world, determinístico, local.
- El primer problema (Louden §10.5): overhead de mantenimiento. Cada asignación de referencia requiere dos operaciones: incrementar el contador del nuevo destino y decrementar el del anterior.
- El segundo problema (Louden §10.5 — el peor defecto): referencias circulares. "Aún más grave es que las referencias circulares pueden provocar que la memoria sin referencias nunca sea liberada." Louden ilustra con una lista circular: ningún contador llega a cero.
- El diagnóstico de Sebesta §6.11.7: "Estos dos enfoques de recolección de basura son, en muchos aspectos, procesos opuestos." Los GC modernos (Python, Swift, V8) combinan ambos o hibridan técnicas.

**Conceptos clave:**
- Sebesta §6.11: RC = incremental, determinístico, sin stop-the-world
- Louden §10.5: overhead de mantenimiento + ciclos = el peor defecto
- Sebesta §6.11.7: RC y mark-sweep son procesos opuestos — los GC modernos los combinan

**Preguntas anticipadas:**
- *"¿Python usa solo RC?"* → No. Python usa RC + cycle detector separado en el módulo `gc`. El cycle detector corre periódicamente y libera los ciclos inaccesibles.

**Transición:** Python usa RC internamente — `sys.getrefcount` permite observar el contador en tiempo real.

---

### [F-20] Reference Counting — seguimiento del contador en Python

**Tiempo:** 2 min

**Qué decir:**
- Recorrer el código paso a paso. `lista = [1, 2, 3]` → ref_count = 1. `sys.getrefcount(lista)` devuelve 2 (getrefcount mismo crea una referencia temporal).
- `alias = lista` → ref_count = 3. `contenedor = [lista]` → ref_count = 4.
- Eliminar referencias una a una: `del contenedor` → 3, `del alias` → 2. Solo `lista` referencia el objeto → ref_count = 1 (más la temporal de getrefcount).
- `del lista` → ref_count → 0 → el runtime libera `[1, 2, 3]` INMEDIATAMENTE. No hay que esperar ningún ciclo de GC. Este es el comportamiento determinístico del RC.

**Conceptos clave:**
- `sys.getrefcount()` permite observar el contador en tiempo real — buen ejercicio de laboratorio
- `del x` libera inmediatamente si no hay otras referencias — determinismo del RC
- El contador incluye referencias temporales (como las de `getrefcount` mismo)

**Preguntas anticipadas:**
- *"¿Por qué `getrefcount` devuelve 2 y no 1?"* → Porque la función `getrefcount` misma recibe el objeto como argumento — eso crea una referencia temporal adicional.

**Transición:** Ahora veamos el talón de Aquiles del RC: los ciclos de referencia.

---

### [F-21] El problema de los ciclos de referencia

**Tiempo:** 2 min

**Qué decir:**
- El escenario del ciclo: `ref_count(A) = 2` (variable externa `a` + B.siguiente). `ref_count(B) = 2` (variable externa `b` + A.siguiente). Al eliminar las variables externas: `del a` → `ref_count(A) = 1` (B todavía apunta). `del b` → `ref_count(B) = 1` (A todavía apunta). El programa ya no puede alcanzar A ni B. Son INACCESIBLES. Pero `ref_count(A) = 1` y `ref_count(B) = 1`. Con RC puro: NUNCA se liberan → MEMORY LEAK permanente.
- Por qué es un problema real y frecuente: listas doblemente enlazadas, árboles con punteros al padre, grafos generales con ciclos, objetos de UI con referencias bidireccionales (parent/child).
- Soluciones: Python (RC + cycle detector), Swift (ARC + `weak` references), Rust (borrow checker prohíbe ciclos mutables), JavaScript/V8 (Mark-and-Sweep que detecta ciclos por diseño).

**Conceptos clave:**
- Referencia circular = ciclo → ningún contador llega a 0 → memory leak
- Estructuras comunes que generan ciclos: listas doblemente enlazadas, árboles con padre, grafos
- Cada lenguaje resuelve distinto: cycle detector, weak refs, borrow checker, o mark-sweep

**Preguntas anticipadas:**
- *"¿Un ciclo siempre es un bug?"* → No. A veces es necesario (lista circular, árbol con padre). La responsabilidad es del programador en lenguajes con GC, o del diseño del tipo en Rust.

**Transición:** Veamos el código concreto en TypeScript.

---

### [F-22] Ciclo de referencia en TypeScript — código con nodos mutuamente enlazados

**Tiempo:** 1 min

**Qué decir:**
- Dos nodos `Nodo` con referencias mutuas: `a.siguiente = b` (A → B) y `b.previo = a` (B → A). Ciclo de referencia.
- Si TypeScript/V8 usara RC puro y elimináramos las referencias externas: `a = null` → `ref_count(A) = 1` (B.previo lo apunta) → no se libera. `b = null` → `ref_count(B) = 1` (A.siguiente lo apunta) → no se libera. Ambos son inaccesibles pero el RC nunca los liberaría — MEMORY LEAK.
- V8 usa Mark-and-Sweep — los detecta como inaccesibles y los libera correctamente. No se necesitan referencias `weak` explícitas como en Swift/ARC.

**Conceptos clave:**
- Dos nodos con referencias mutuas = ciclo que RC puro no podría liberar
- V8 usa Mark-and-Sweep — detecta el ciclo como inaccesible y lo libera
- En Swift/ARC necesitarías `weak` para romper el ciclo manualmente

**Preguntas anticipadas:** ninguna típica.

**Transición:** El algoritmo que sí resuelve los ciclos es mark-and-sweep. Veamos cómo funciona.

---

### [F-23] Mark-and-Sweep — la idea general

**Tiempo:** 2 min

**Qué decir:**
- Las raíces del grafo de objetos: variables activas en todos los activation records del stack, variables globales del programa, registros de la CPU con referencias.
- Fase 1 — Mark: a partir de cada raíz, el GC realiza un traversal transitivo del grafo de referencias. Si puede llegar a un objeto directa o transitivamente → lo marca como alcanzable. Si no → queda sin marcar.
- Fase 2 — Sweep: recorre TODO el heap. Celda marcada → sigue viva → desmarcarla para el próximo ciclo. Celda no marcada → es inaccesible → liberar.
- La ventaja clave sobre RC: un ciclo entre A y B que no sea alcanzable desde ninguna raíz queda sin marcar → ambos se liberan en el sweep. El problema de los ciclos desaparece.
- El costo: durante mark y sweep, el programa se pausa (stop-the-world). Los GC modernos minimizan esta pausa con técnicas incrementales y concurrentes.

**Conceptos clave:**
- Mark: trazar todos los objetos alcanzables desde las raíces (stack, globales, CPU)
- Sweep: liberar todo lo no marcado — incluyendo ciclos
- Costo: stop-the-world durante la ejecución del GC

**Preguntas anticipadas:**
- *"¿Se puede hacer sin pausar el programa?"* → Sí — GC incremental y concurrente (lo hace V8). Requiere sincronización entre el GC y el programa en ejecución — complejo de implementar.

**Transición:** Gabbrielli §8.11 identifica tres defectos estructurales del mark-and-sweep clásico.

---

### [F-23b] Los tres defectos del mark-and-sweep y la compactación como solución — Gabbrielli §8.11

**Tiempo:** 2 min

**Qué decir:**
- Gabbrielli §8.11: "La técnica de mark-and-sweep padece tres defectos principales."
- Defecto 1 — Fragmentación externa: los objetos vivos y los inaccesibles quedan entremezclados en memoria. La suma de huecos puede ser suficiente para una nueva alocación, pero no hay ningún bloque contiguo disponible.
- Defecto 2 — Stop-the-world: a diferencia del RC (incremental), el mark-and-sweep acumula trabajo y lo ejecuta todo junto. En heaps grandes: pausas de cientos de milisegundos inaceptables para aplicaciones interactivas.
- Defecto 3 — Actualización de punteros tras compactación: si se añade compactación, todos los punteros a objetos movidos deben actualizarse. El costo es proporcional al número de referencias en el grafo.
- La solución (Gabbrielli §8.11): compactación — "Los objetos vivos se mueven de modo que queden contiguos, dejando así un bloque contiguo de memoria libre."
- V8 usa semi-space copying en el New Space: los objetos vivos se copian al semi-space vacío ("to"), y al terminar los roles se intercambian. El semi-space "from" queda completamente libre en un solo paso.

**Conceptos clave:**
- Gabbrielli §8.11: tres defectos — fragmentación, stop-the-world, actualización de punteros
- Compactación resuelve la fragmentación — mueve objetos vivos a posiciones contiguas
- V8: semi-space copying — compactación sin actualizaciones in-place

**Preguntas anticipadas:**
- *"¿La compactación es obligatoria?"* → No. Mark-sweep sin compactación funciona, pero el heap se fragmenta. V8 compacta en la generación vieja (Mark-Compact) pero no en la joven (usa copying).

**Transición:** Veamos el trazado del algoritmo sobre un heap de ejemplo.

---

### [F-24] Mark-and-Sweep — trazado del algoritmo sobre un heap de ejemplo

**Tiempo:** 1 min

**Qué decir:**
- Estado inicial: raíces activas `x → Obj1`, `y → Obj3`. Obj1 referencia Obj2. Obj4 referencia Obj5. Obj5 referencia Obj4 (ciclo). Obj4 y Obj5 no son alcanzables desde ninguna raíz.
- Fase Mark: desde `x` → Obj1 ✓ (marcado). Obj1.ref → Obj2 ✓ (marcado transitivamente). Desde `y` → Obj3 ✓ (marcado). Obj4, Obj5: no alcanzables → sin marcar.
- Fase Sweep: Obj1 ✓ → vivo. Obj2 ✓ → vivo. Obj3 ✓ → vivo. Obj4 → LIBERAR (inaccesible — aunque forma ciclo con Obj5). Obj5 → LIBERAR (inaccesible — aunque forma ciclo con Obj4).
- Estado final: Obj1, Obj2, Obj3 — vivos. El ciclo Obj4 ↔ Obj5 fue liberado correctamente.

**Conceptos clave:**
- Mark traza desde las raíces — marca todo lo alcanzable transitivamente
- Sweep libera todo lo no marcado — incluyendo ciclos inaccesibles
- El ciclo Obj4 ↔ Obj5 se libera correctamente — RC puro no podría

**Preguntas anticipadas:** ninguna típica.

**Transición:** V8, el motor que ejecuta TypeScript, combina mark-sweep con una idea poderosa: GC generacional.

---

### [F-25] GC generacional en V8 — el principio

**Tiempo:** 2 min

**Qué decir:**
- La hipótesis generacional: evidencia empírica en lenguajes con GC — la gran mayoría de los objetos tienen un ciclo de vida muy corto. Resultados de `map`/`filter`, objetos temporales de request, closures de un solo uso. Pocos objetos sobreviven mucho tiempo.
- La estrategia: dividir el heap en generaciones. Generación joven (Young Gen / Nursery): objetos recién creados → GC muy frecuente, espacio pequeño → muy rápido. Generación vieja (Old Gen / Tenured): objetos que sobrevivieron varios ciclos → GC infrecuente → más costoso pero ocurre raramente.
- Promoción: un objeto que sobrevive un número configurable de ciclos se promueve a la generación vieja.
- Resultado práctico: el 90% de los ciclos de GC solo barren la generación joven (unos pocos megabytes) y duran menos de 1 ms. Los ciclos sobre la generación vieja son raros y se pueden ejecutar de forma incremental o concurrente.

**Conceptos clave:**
- Hipótesis generacional: la mayoría de los objetos mueren jóvenes
- Dividir el heap en generaciones optimiza el GC — joven frecuente/barato, vieja infrecuente/costosa
- Promoción: sobrevivir N ciclos → migrar a la generación vieja

**Preguntas anticipadas:**
- *"¿Quién descubrió la hipótesis generacional?"* → Fue observada empíricamente en sistemas como Lisp y Smalltalk. Los GC generacionales modernos (V8, Java HotSpot, Go) la explotan sistemáticamente.

**Transición:** Veamos el layout interno del heap de V8.

---

### [F-26] GC generacional en V8 — estructura del heap

**Tiempo:** 2 min

**Qué decir:**
- New Space (Generación joven): dos semi-spaces ("from" y "to"). Scavenger GC frecuente, muy rápido. Capacidad ~1-8 MB.
- Old Space (Generación vieja): objetos promovidos — sobrevivieron en New Space. Mark-Compact incremental + concurrent. Capacidad de cientos de MB — GC infrecuente.
- Code Space: código JIT compilado. Large Object Space: objetos > 512KB — no se compactan. Map Space: descriptores de forma de objetos.
- Minor GC (Scavenger): evacúa New Space — semi-space copying, muy rápido. Major GC (Mark-Compact): mark + sweep + compact en Old Space — concurrent.
- Mensaje para llevar: en TypeScript, el programador **no gestiona memoria**. Sabe que existe un GC, entiende que las closures extienden el ciclo de vida de variables al heap, y confía en que V8 los libera eventualmente.

**Conceptos clave:**
- V8 heap: New Space (Scavenger, semi-space copying) + Old Space (Mark-Compact)
- Minor GC < 1ms sobre New Space; Major GC incremental sobre Old Space
- El programador de TypeScript no gestiona memoria — V8 lo hace todo

**Preguntas anticipadas:** ninguna típica en este punto.

**Transición:** Pasemos a la segunda gran idea del día — la dimensión del tipado. TypeScript no es solo "JavaScript con tipos": es un ejemplo canónico de un concepto teórico llamado gradual typing.

---

## BLOQUE 4 — Gradual Typing: TypeScript como Caso Paradigmático (16 min)

---

### [F-27] El espectro del tipado

**Tiempo:** 2 min

**Qué decir:**
- Tipado estático puro: los tipos se verifican en compilación. Si hay un error de tipos → el programa no compila. Ejemplos: Java, C, Haskell, Rust.
- Tipado dinámico puro: los tipos se verifican en ejecución. El programa compila siempre — los errores de tipos son excepciones en runtime. Ejemplos: Python (sin mypy), Ruby, Scheme, JavaScript puro.
- Tipado gradual — la tercera vía: permite mezclar. Algunas partes tienen tipos estáticos, otras usan `any` (tipo dinámico). El programador elige la cobertura según la criticidad de cada módulo o función. Formalizado por Jeremy Siek y Walid Taha en 2006. TypeScript lo implementó de forma práctica y a escala industrial.

**Conceptos clave:**
- Estático: tipos verificados en compilación; Dinámico: tipos verificados en runtime
- Gradual: elige dónde y cuánto — anotaciones opcionales en el mismo lenguaje
- TypeScript es el ejemplo canónico de gradual typing en producción masiva

**Preguntas anticipadas:**
- *"¿Groovy y Dart también son graduales?"* → Sí, pero TypeScript es el más estudiado en la bibliografía del curso (Gabbrielli §16.9 le dedica una sección completa).

**Transición:** El gradual typing no es solo una característica de TypeScript — tiene base teórica rigurosa.

---

### [F-27b] El origen académico del gradual typing — Gabbrielli §16.9 y Siek & Taha (2006)

**Tiempo:** 2 min

**Qué decir:**
- La motivación histórica (Gabbrielli §16.9): "A medida que el número de proyectos de software de gran escala desarrollados con lenguajes de tipado dinámico creció con el tiempo, los usuarios advirtieron que sacrificar las verificaciones estáticas en favor de la rapidez de prototipado era un trato desfavorable."
- La base formal — Siek & Taha (2006): un tipo especial `?` (tipo dinámico) — compatible con cualquier tipo en compilación. Relación de **consistencia de tipos** (`∼`): `T ∼ ?` para cualquier `T` — más débil que la igualdad. Cast implícito automático: el compilador inserta verificaciones en los límites entre código tipado y no tipado.
- TypeScript y la corrección formal (Gabbrielli §16.9): Gabbrielli distingue el tipado gradual **formalmente correcto** del enfoque de TypeScript, que es **deliberadamente incompleto**: acepta ciertos programas con potenciales errores de tipo por razones de usabilidad y compatibilidad con JavaScript. Esta decisión está documentada en la especificación oficial.

**Conceptos clave:**
- Gabbrielli §16.9: motivación histórica — proyectos grandes en dinámico necesitan contratos
- Siek & Taha 2006: tipo `?`, relación de consistencia `∼`, cast implícito automático
- TypeScript: deliberadamente unsound — acepta programas potencialmente incorrectos por usabilidad

**Preguntas anticipadas:**
- *"¿Qué significa 'deliberadamente incompleto'?"* → Que TypeScript no garantiza que todos los programas que compilan estén libres de errores de tipo en runtime. Prioriza compatibilidad con JavaScript sobre corrección formal.

**Transición:** Veamos la comparación de los tres enfoques.

---

### [F-28] Tipado estático, dinámico y gradual — comparación

**Tiempo:** 2 min

**Qué decir:**
- Recorrer la tabla rápido — no leer cada celda, comentar las diferencias clave.
- Verificación de tipos: estático en compilación, dinámico en ejecución, gradual en compilación donde hay tipos.
- Error de tipos: estático no compila, dinámico es excepción en runtime, gradual es error de compilación si hay tipo.
- Escape hatch: estático no existe, dinámico todo es dinámico, gradual tiene `any` — explícito y auditable.
- Migración desde JS: solo gradual la permite incremental, archivo por archivo.

**Conceptos clave:**
- La tabla resume las diferencias clave entre los tres enfoques
- El escape hatch `any` es la firma del gradual typing — explícito y auditable
- La migración incremental desde JS es la propuesta de valor única del gradual typing

**Preguntas anticipadas:** ninguna típica.

**Transición:** Veamos TypeScript concreto — el nivel 0 de cobertura.

---

### [F-29] TypeScript — nivel 0: `any` implícito

**Tiempo:** 2 min

**Qué decir:**
- Sin strict mode: TypeScript infiere `any` para parámetros sin anotación. El código compila — es válido como punto de partida en una migración desde JS.
- `sumar(1, 2)` → 3. `sumar("1", 2)` → "12" (concatenación de strings — sin error en compilación). `sumar({}, [])` → "[object Object]" — TypeScript no objeta.
- Con `strict: true` en tsconfig.json → Error: Parameter 'a' implicitly has an 'any' type. Ese error es la señal de que el código necesita anotaciones.
- Nivel 0 es el punto de entrada de toda migración JS → TS: renombrar `.js` → `.ts` ya es válido en nivel 0, sin cambiar ninguna línea.

**Conceptos clave:**
- Nivel 0: `any` implícito — compatible con JavaScript puro, sin garantías
- `strict: true` activa `noImplicitAny` — el error es la señal de que faltan anotaciones
- La migración JS → TS empieza por renombrar `.js` → `.ts` — compila inmediatamente

**Preguntas anticipadas:**
- *"¿Sin strict, TypeScript sirve de algo?"* → Sí — permite agregar tipos gradualmente. Pero sin strict, los tipos son opt-in y el compilador no objeta el código sin anotaciones.

**Transición:** El mecanismo que TypeScript usa para razonar sobre union types es el type narrowing.

---

### [F-30] Type Narrowing — ¿qué es y por qué existe?

**Tiempo:** 2 min

**Qué decir:**
- El problema que resuelve: un union type como `string | number | null` permite que una variable sea cualquiera de esos tipos. Para usar `toUpperCase()`, necesitamos saber que es `string`. Sin verificar, el compilador (con strict) rechaza el código.
- ¿Qué es el type narrowing? Es el proceso por el cual TypeScript **estrecha** (narrows) el tipo de una variable dentro de cada rama de control de flujo, basándose en las condiciones verificadas en las ramas anteriores.
- Los guardas de tipo más comunes: `typeof x === "string"`, `x === null`, `x instanceof Clase`, `"propiedad" in x`, narrowing exhaustivo con `switch` + `default: never`.
- La garantía formal: dentro de cada rama del narrowing, TypeScript garantiza estáticamente que el tipo es el esperado. Si se agrega un nuevo caso al union type y no se actualiza el código, el compilador lo detecta.

**Conceptos clave:**
- Narrowing: TypeScript refina el tipo conocido dentro de cada rama condicional
- Guardas de tipo: `typeof`, `===`, `instanceof`, `in`, `switch` exhaustivo
- El compilador verifica exhaustividad — si falta una rama, error de compilación

**Preguntas anticipadas:**
- *"¿Hay narrowing con `instanceof`?"* → Sí. `if (error instanceof TypeError)` es type narrowing para clases. `typeof` es para primitivos, `instanceof` para instancias de clase.

**Transición:** Veamos el código concreto con `typeof` e `instanceof`.

---

### [F-31] Type Narrowing con `typeof` e `instanceof`

**Tiempo:** 2 min

**Qué decir:**
- Recorrer la función `formatear` rama por rama. En cada `if`, TypeScript **refina** su conocimiento del tipo. Después del primer `if (r === null)`, en el resto TypeScript sabe que `r` no puede ser null. Después del segundo `if (typeof r === "number")`, sabe que `r` es `string`.
- La última línea `return r.toUpperCase()` es válida porque TypeScript infiere que en ese punto, `r: string`. Si el programador hubiera olvidado el `if (typeof r === "number")`, TypeScript daría error.
- `instanceof` — para clases con herencia: `if (animal instanceof Perro)` → en esa rama, TypeScript sabe que `animal` es `Perro`. En el resto, es `Gato` (único tipo restante).

**Conceptos clave:**
- `typeof` estrecha primitivos; `instanceof` estrecha instancias de clase
- TypeScript elimina tipos del union en cada rama verificada
- El tipo final se infiere por eliminación — el último `return` tiene el tipo restante

**Preguntas anticipadas:**
- *"¿`typeof null` devuelve 'null'?"* → No — devuelve `"object"` (bug histórico de JavaScript). Por eso se usa `=== null` en lugar de `typeof` para narrowing de null.

**Transición:** El patrón más poderoso es el switch exhaustivo con `never`.

---

### [F-32] Type Narrowing exhaustivo con `switch` y el patrón `never`

**Tiempo:** 2 min

**Qué decir:**
- El compilador detecta en compilación si falta un caso al agregar un nuevo tipo al union.
- Si el tipo `Forma` creciera a incluir "rectángulo" y olvidáramos agregar el `case "rectángulo"`, TypeScript llega al `default` con `f: "rectángulo"` — NO es `never`. El cast a `never` fuerza el error de compilación: `Type '"rectángulo"' is not assignable to type 'never'`.
- Con este patrón: agregar un caso al tipo sin actualizar el switch → error inmediato en IDE, antes de correr cualquier test.
- Conectar con el bloque IA del final: el type narrowing es el guardrail que detecta cuando el código IA no maneja todos los casos de un union type.

**Conceptos clave:**
- Switch exhaustivo + `never` = el compilador detecta casos faltantes al agregar tipos al union
- El cast `const _exhaustive: never = f` fuerza el error si llega un tipo no manejado
- Agregar un tipo al union sin actualizar el switch → error inmediato en IDE

**Preguntas anticipadas:**
- *"¿El `never` type está relacionado con esto?"* → Exactamente. `never` es el tipo que no tiene valores. Si TypeScript llega al `default` con un tipo que no es `never`, significa que hay un caso no manejado.

**Transición:** Veamos cómo se traduce esto a proyectos reales.

---

### [F-33] Gradual typing en proyectos grandes — impacto real

**Tiempo:** 2 min

**Qué decir:**
- Recorrer la tabla: JavaScript puro vs. TypeScript gradual vs. TypeScript strict.
- Detección de errores de tipo: solo en runtime (JS) → en compilación parcial (TS gradual) → en compilación total (TS strict).
- Refactoring seguro: muy difícil en JS (puede romper silencioso) → parcialmente seguro (gradual) → seguro (strict — el compilador verifica).
- Null crashes: muy frecuentes en JS → reducidos donde hay tipos (gradual) → eliminados con `strictNullChecks` (strict).
- Tiempo de detección: runtime en producción (JS) → build en CI (gradual) → IDE en tiempo real (strict).
- La cita de Gabbrielli §16.9 como cierre de bloque: TypeScript demuestra que el gradual typing es viable en producción masiva — no es solo un experimento académico.

**Conceptos clave:**
- Gradual typing: los errores de tipo pasan de runtime a compilación gradualmente
- `strict: true` = máxima detección; equipos grandes se benefician más
- TypeScript es la validación empírica de la propuesta teórica del gradual typing

**Preguntas anticipadas:** ninguna típica.

**Transición:** Ahora el quinto bloque — un cambio de paradigma literal. En FP puro, no existen variables mutables. Solo bindings.

---

## BLOQUE 5 — Variables en Programación Funcional (14 min)

---

### [F-34] Variables en FP puro — sin mutabilidad

**Tiempo:** 2 min

**Qué decir:**
- El contraste fundamental: en LP imperativos, las variables son celdas de memoria mutables — la asignación `x = 5` es una operación destructiva que sobreescribe el R-value. En LP funcionales puros, no existen variables mutables — existen **bindings**. Un binding es una asociación nombre → valor, definitiva dentro de su scope.
- En FP: `x = 5` no asigna a una celda, declara que `x` ES 5 en ese scope.
- La computación como reescritura de expresiones: en FP puro, computar no significa modificar el estado de celdas de memoria. Significa reescribir expresiones hasta obtener un valor. El resultado es idéntico sin importar cuántas veces se evalúe — transparencia referencial.
- Por qué importa: sin estado mutable → sin efectos laterales → sin aliases peligrosos por definición. El razonamiento ecuacional funciona: si `f(x) = 10`, entonces cualquier `f(x)` puede reemplazarse por 10.

**Conceptos clave:**
- FP puro: no hay L-value, no hay mutación, no hay asignación destructiva
- Los bindings en Haskell son definitivos — como constantes matemáticas
- Sin estado mutable → sin aliases peligrosos → razonamiento ecuacional válido

**Preguntas anticipadas:**
- *"¿Cómo hace Haskell para hacer IO o estado?"* → Mónadas (IO monad, State monad). El estado existe, pero está encapsulado y explícito — no hay efectos ocultos.

**Transición:** Formalicemos la transparencia referencial con las definiciones de Sebesta y Louden.

---

### [F-34b] Transparencia referencial — la definición formal y sus consecuencias

**Tiempo:** 2 min

**Qué decir:**
- La definición de Sebesta §7.4: "Un programa tiene la propiedad de transparencia referencial si dos expresiones cualesquiera con el mismo valor pueden sustituirse mutuamente en cualquier punto del programa sin afectar su comportamiento."
- La definición equivalente de Louden §9.1: "Dos expresiones cualesquiera en un programa que tengan el mismo valor pueden reemplazarse mutuamente en cualquier lugar del programa sin alterar el resultado."
- Sebesta §7.4: "Como los lenguajes funcionales puros no tienen variables, los programas escritos en ellos son referencialmente transparentes. Las funciones en un lenguaje funcional puro no pueden tener estado."
- Las consecuencias formales: (1) razonamiento ecuacional — `f(x)` puede sustituirse por su valor; (2) memoización válida — el compilador puede cachear `f(5) = 25`; (3) reordenamiento seguro — el compilador puede evaluar `f(a)` y `g(b)` en cualquier orden; (4) pruebas aisladas — una función pura se prueba con sus argumentos, sin setup de estado.
- La conexión con aliases: los aliases sobre objetos mutables rompen la transparencia referencial. La inmutabilidad elimina esta categoría de problemas por diseño.

**Conceptos clave:**
- Sebesta §7.4 + Louden §9.1: transparencia referencial = sustitución sin afectar comportamiento
- Consecuencias: razonamiento ecuacional, memoización, reordenamiento, pruebas aisladas
- Los aliases sobre mutables rompen la transparencia referencial — la inmutabilidad los elimina

**Preguntas anticipadas:**
- *"¿La transparencia referencial aplica en TypeScript?"* → Solo si el código es puro (sin mutación, sin efectos laterales). TypeScript no la garantiza — el programador debe escribirla.

**Transición:** Veamos Haskell — el binding es definitivo.

---

### [F-35] Haskell — el binding es definitivo

**Tiempo:** 2 min

**Qué decir:**
- En Haskell, `let x = 5` declara que x ES 5 en este scope — no que x TIENE el valor 5. `x = 6` es ILEGAL: no existe el concepto de reasignación.
- La "iteración" en FP no usa un contador mutable — usa recursión con binding fresh: `sumaLista (x:xs) = x + sumaLista xs`. `x` es un binding nuevo en cada llamada recursiva — no es la misma celda modificada.
- Versión con fold — sin ninguna variable mutable explícita: `suma = foldl (+) 0 [1, 2, 3, 4, 5]`.
- Para "cambiar" el valor de x se necesita un binding nuevo: `let y = x + 1` — y está vinculado a 6, x sigue siendo 5. No es "x = x + 1" — es un nombre completamente nuevo.

**Conceptos clave:**
- Haskell: `let x = 5` es un binding definitivo — no hay reasignación
- La iteración usa recursión con bindings fresh — no un contador mutable
- "Cambiar" un valor = crear un binding nuevo con un nombre distinto

**Preguntas anticipadas:**
- *"¿Haskell tiene loops?"* → No tiene `for` ni `while`. Usa recursión, folds, maps y comprehensión de listas. El concepto de "loop con contador mutable" no existe.

**Transición:** Scala y Kotlin distinguen explícitamente entre binding inmutable y variable mutable.

---

### [F-36] `val` vs. `var` — Scala y Kotlin

**Tiempo:** 2 min

**Qué decir:**
- Scala: `val y = 5` (binding inmutable — como `const` en TypeScript, no puede reasignarse). `var x = 5` (variable mutable — como `let` en TypeScript, puede reasignarse). `x = 10` ✅ válido. `y = 10` ❌ Error: reassignment to val.
- En estilo funcional en Scala: siempre `val`, salvo que la mutación sea necesaria. `val` comunica intención: "este valor no va a cambiar después de este punto".
- Kotlin: misma distinción, misma semántica. `val inmutable = 42` (binding definitivo). `var mutable = 42` (variable mutable). Para colecciones: `listOf(1, 2, 3)` (inmutable) vs. `mutableListOf(1, 2, 3)` (mutable).

**Conceptos clave:**
- Scala: `val` = inmutable, `var` = mutable — elección explícita del programador
- Kotlin: misma distinción — `val` no se puede reasignar, `var` sí
- Las colecciones también tienen versión inmutable (`listOf`) y mutable (`mutableListOf`)

**Preguntas anticipadas:**
- *"¿`const` en TypeScript hace deep freeze del objeto?"* → No. `const` impide reasignar la variable, pero el objeto apuntado puede mutarse. `Readonly<T>` impide mutación de las propiedades — pero tampoco es deep por defecto.

**Transición:** TypeScript no es FP puro, pero permite adoptar un estilo funcional.

---

### [F-37] TypeScript funcional — `reduce` vs. loop imperativo

**Tiempo:** 2 min

**Qué decir:**
- Estilo imperativo: muta el acumulador en cada iteración. `suma += x` — `suma` cambia su valor (R-value) en cada iteración. `suma` es una variable en el sentido imperativo: L-value modificable.
- Estilo funcional: `numeros.reduce((acc, x) => acc + x, 0)`. En cada llamada al callback: `acc` y `x` son parámetros nuevos (bindings fresh). No hay ninguna variable que se mute — hay una cadena de aplicaciones de función.
- Transformación completa en cadena — sin estado mutable en ningún paso: `.filter(x => x % 2 === 0)` → nuevo array. `.map(x => x * 10)` → nuevo array. `.reduce((a, b) => a + b, 0)` → binding final. Cada transformación produce un valor nuevo — ningún paso modifica el anterior.

**Conceptos clave:**
- Imperativo: muta un acumulador — `suma` es L-value modificable
- Funcional: `reduce` con bindings fresh — `acc` y `x` son parámetros nuevos en cada llamada
- Cadena `filter.map.reduce` — cada paso produce un valor nuevo, nada se muta

**Preguntas anticipadas:**
- *"¿La versión funcional es más lenta por crear arrays intermedios?"* → En TypeScript sí hay overhead. En Haskell con lazy evaluation, los arrays intermedios se fusionan (fusion). En TypeScript, si el rendimiento es crítico, se puede usar transducers o un solo loop.

**Transición:** TypeScript provee herramientas de compilación para garantizar inmutabilidad en objetos.

---

### [F-38] `Readonly<T>` y objetos inmutables en TypeScript

**Tiempo:** 2 min

**Qué decir:**
- `Readonly<T>` — el compilador impide cualquier mutación de las propiedades del objeto. `cfg.debug = true` → ❌ Error: Cannot assign to 'debug' because it is a read-only property.
- `ReadonlyArray<T>` — array inmutable: no se puede `push`, `pop` ni asignar por índice. `COLORES.push("amarillo")` → ❌ Property 'push' does not exist on type 'readonly string[]'.
- `as const` — convierte literales en tipos inmutables ultra-estrictos. El tipo inferido es `{ readonly min: 0; readonly max: 100 }` — los valores son literales exactos.
- `Object.freeze()` — inmutabilidad en runtime. `frozen.retries = 5` → TypeError en runtime en modo strict del motor JS.

**Conceptos clave:**
- `Readonly<T>`: inmutabilidad de propiedades en compilación
- `ReadonlyArray<T>`: array sin `push`/`pop`/index assignment
- `as const`: literales como tipos inmutables exactos; `Object.freeze()`: inmutabilidad en runtime

**Preguntas anticipadas:**
- *"¿`Readonly<T>` es deep?"* → No. Solo protege el primer nivel. Para deep inmutabilidad se necesita una utilidad recursiva `DeepReadonly<T>` o librerías como `ts-readonly`.

**Transición:** ¿Por qué la inmutabilidad reduce bugs?

---

### [F-39] ¿Por qué la inmutabilidad reduce bugs?

**Tiempo:** 2 min

**Qué decir:**
- El origen del problema con el estado mutable compartido: una función puede modificar un objeto que otras partes del código asumen estable. El bug puede aparecer lejos del lugar donde ocurrió la modificación — difícil de rastrear. En pruebas: las pruebas que pasan en aislamiento pueden fallar cuando se ejecutan en conjunto. En concurrencia: dos threads que mutan el mismo objeto sin sincronización producen resultados no determinísticos.
- La garantía que aporta la inmutabilidad: si un objeto es inmutable, no puede haber aliases peligrosos — cualquier referencia al objeto siempre ve el mismo valor. No es necesario sincronizar accesos concurrentes — los datos nunca cambian. Las funciones puras son aisladas: su resultado depende solo de sus argumentos.
- La conexión con closures: una closure sobre un binding inmutable es inherentemente segura — la closure puede leer el valor capturado (siempre el mismo), no puede modificarlo, no puede producir efectos sobre el estado del caller.
- FP en TypeScript — el espectro práctico: TypeScript no es un LP puramente funcional. Pero permite adoptar un estilo funcional donde tiene sentido: `const` + `Readonly<T>` + `ReadonlyArray` + `reduce`/`map`/`filter` en lugar de loops con mutación.

**Conceptos clave:**
- La inmutabilidad elimina una clase entera de bugs: mutación accidental de objetos compartidos
- Sin mutación → sin aliases peligrosos → sin race conditions → funciones aisladas
- Closures sobre bindings inmutables son seguras por diseño
- TypeScript permite estilo funcional: `const` + `Readonly` + `reduce`/`map`/`filter`

**Preguntas anticipadas:** ninguna típica.

**Transición:** Antes del bloque IA, hagamos un recorrido rápido por cómo los lenguajes modernos resuelven todos estos problemas en conjunto.

---

## BLOQUE 6 — Contraste Multilenguaje: Gestión de Memoria Moderna (8 min)

---

### [F-40] Cuatro lenguajes, cuatro estrategias de memoria

**Tiempo:** 3 min

**Qué decir:**
- Recorrer la tabla fila por fila. No leer cada celda — comentar las diferencias que más sorprenden.
- Estrategia de GC: TypeScript/V8 (GC generacional — Scavenger + Mark-Compact concurrent), Python (RC + cycle detector), Go (GC concurrent tricolor incremental), Rust (Ownership + Drop — sin GC en runtime).
- Dangling pointer: en los cuatro lenguajes es **imposible**. Este fue el mayor problema de C y C++ durante décadas. Los lenguajes modernos lo resuelven cada uno a su manera.
- Alias de objeto: TypeScript y Python tienen referencia implícita (invisible al programador). Go tiene puntero explícito con `*` y `&`. Rust tiene borrow controlado por el compilador.
- Ciclos de referencia: V8 Mark-Sweep los resuelve. Python con módulo `gc` cycle detector. Go GC concurrente los resuelve. Rust: imposibles (mutables) — borrow checker.
- Pausa del programa: TypeScript Minor GC <1ms / Major GC incremental. Python RC incremental — impacto bajo. Go GC concurrent <1ms objetivo. Rust: sin GC → sin pausa.

**Conceptos clave:**
- Los cuatro lenguajes modernos eliminan dangling pointers con estrategias diferentes
- Rust: sin GC, sin pausa — garantías en tiempo de compilación
- Go: zero values eliminan variables sin inicializar — semántica más segura que C

**Preguntas anticipadas:**
- *"¿Por qué no todos usamos Rust entonces?"* → Curva de aprendizaje alta (el borrow checker es complejo), menor ecosistema para web/data, no es gradual. TypeScript es más práctico para muchos dominios.

**Transición:** Rust es el caso más extremo — sin GC en absoluto. Veamos por qué.

---

### [F-41] Rust: ownership — la idea central

**Tiempo:** 2 min

**Qué decir:**
- El sistema de ownership: cada valor tiene **un único dueño** (owner) en cada momento. Cuando el dueño sale del scope, el valor se destruye automáticamente (Drop trait — destructores determinísticos). La propiedad puede **transferirse** (move): el dueño anterior ya no puede usar el valor. La propiedad puede **prestarse** (borrow): referencias temporales que el compilador verifica.
- Las reglas del borrow checker — garantías en compilación: (1) puede haber cualquier cantidad de referencias inmutables (`&T`) al mismo tiempo; (2) o puede haber exactamente una referencia mutable (`&mut T`) — pero no simultáneamente con referencias inmutables; (3) las referencias no pueden vivir más tiempo que el valor al que apuntan (no hay dangling references).
- El resultado: sin GC en runtime → sin pausas → rendimiento predecible. Sin dangling pointers → verificado por el compilador, no por pruebas en runtime.

**Conceptos clave:**
- Ownership: cada objeto tiene un único dueño; al salir del scope → destruido sin GC
- Borrow checker: cualquier cantidad de `&T` o exactamente una `&mut T` — no ambas
- Sin GC → sin pausas → rendimiento predecible; sin dangling → verificado en compilación

**Preguntas anticipadas:**
- *"¿`drop()` es como `free()` de C?"* → Conceptualmente similar — libera el objeto. Pero en Rust no es necesario llamarlo manualmente; el compilador lo inserta automáticamente.

**Transición:** Veamos el borrow checker en acción con código.

---

### [F-42] Rust — el borrow checker en acción

**Tiempo:** 3 min

**Qué decir:**
- Drop automático: `nueva_sesion` crea `datos` y lo retorna — move: ownership transferido al caller. `datos` NO se destruye aquí. Si no se transfiriera, se destruiría automáticamente (Drop).
- Dangling reference — error de compilación: `referencia = &s` dentro de un bloque interno. Al salir del bloque, `s` sale de scope → Drop → `s` destruida. `println!("{}", referencia)` → ❌ Error: `s` does not live long enough. En C, esto compilaría y produciría comportamiento indefinido en runtime.
- Move semantics: `let v2 = v1` — ownership de `v1` transferido a `v2` (move). `println!("{:?}", v1)` → ❌ Error: value borrowed here after move. `v2` es el único dueño.
- Mensaje: **lo que en TypeScript sería un bug en producción, en Rust es un error de compilación**.

**Conceptos clave:**
- Drop automático al salir del scope — sin GC, sin `free()` manual
- Dangling reference = error de compilación en Rust; crash silencioso en C
- Move semantics: el compilador rastrea dónde está cada valor — el dueño anterior no puede usarlo

**Preguntas anticipadas:**
- *"¿Rust tiene aliases?"* → Sí, pero controlados: múltiples `&T` (inmutables) son aliases seguros. Un `&mut T` es un alias exclusivo — no puede coexistir con otros. El borrow checker lo garantiza en compilación.

**Transición:** Ahora el bloque final antes del cierre — tres patrones concretos de errores que los LLMs generan.

---

## BLOQUE 7 — Bloque IA: Aliases, Closures y Type Narrowing (12 min)

---

### [F-43] IA Pattern 1 — el LLM genera un alias donde debería ir una copia

**Tiempo:** 2 min

**Qué decir:**
- Este patrón aparece frecuentemente en código generado: el LLM escribe `const configBackup = config` y lo comenta como "guardando copia". No es una copia — es un alias.
- `configBackup.debug = true` modifica `config` también — el backup es inútil.
- Por qué la IA comete este error: el LLM fue entrenado con mucho código JavaScript donde la asignación de objetos es común y la distinción copia/alias no siempre está explícita en el nombre de la variable.
- El punto pedagógico: el LLM no "sabe" la diferencia entre copiar un valor primitivo y copiar una referencia. Genera el mismo operador `=` para ambos casos. El programador que conoce el modelo de memoria puede detectarlo.

**Conceptos clave:**
- El LLM genera `=` sobre objetos como si fuera una copia — es un alias
- El "backup" modifica el original — el backup es inútil
- El programador que conoce el modelo de memoria detecta el error

**Preguntas anticipadas:** ninguna típica — es un bloque práctico.

**Transición:** Veamos cómo detectar y corregir el alias invisible.

---

### [F-44] IA Pattern 1 — cómo detectar y corregir el alias invisible

**Tiempo:** 2 min

**Qué decir:**
- Tres señales de alerta en código IA: (1) `const backup = objeto` → alias (sin duda). (2) `const copia = { ...objeto }` → alias en sub-objetos anidados. (3) `const arr = Array.from(originalArr)` → alias en cada elemento objeto.
- Corrección 1 — Shallow copy: `const configBackup1 = { ...config }` — nivel 0 independiente, nivel 1+ sigue siendo alias.
- Corrección 2 — Deep copy: `const configBackup2 = structuredClone(config)` — todos los niveles son independientes.
- Verificación rápida: `config === configBackup1` → false ✅ (nivel 0 distinto). `config.nested === configBackup1.nested` → true ⚠️ (nivel 1 sigue siendo alias). `config.nested === configBackup2.nested` → false ✅ (deep copy real).

**Conceptos clave:**
- Detección: si el lado derecho es un identificador de objeto sin `{ ... }` ni `structuredClone` → alias
- Corrección según profundidad: spread para planos, `structuredClone` para anidados
- Verificación: comparar referencias anidadas para confirmar independencia

**Preguntas anticipadas:** ninguna típica.

**Transición:** El segundo patrón es el bug de `var` que ya vimos en closures — ahora desde la perspectiva de código generado por IA.

---

### [F-45] IA Pattern 2 — el LLM usa `var` en loops con closures

**Tiempo:** 2 min

**Qué decir:**
- Los LLMs entrenados con código histórico a veces generan `var` en loops, especialmente cuando el corpus de entrenamiento incluye código JavaScript pre-ES6 (anterior a 2015).
- Mostrar el código incorrecto: `for (var i = 0; i < 5; i++) { funcs.push(() => i); }`. Todas las closures capturan la MISMA celda de memoria. `var` es función-scope: `i` vive en el scope de la función contenedora. No se crea una `i` nueva en cada iteración — hay una sola.
- En este punto `i === 5` (el loop terminó). Todas las closures leen la misma celda que ahora contiene 5: `funcs[0]()` → 5, `funcs[1]()` → 5, `funcs[4]()` → 5.
- El deep binding capturó correctamente la REFERENCIA a `i`. El bug es que `var` hace que esa referencia sea compartida por todas las iteraciones.

**Conceptos clave:**
- LLMs pueden generar `var` en loops — código legacy aún presente en el corpus
- `var`: scope de función = un solo binding = todas las closures ven el valor final
- El deep binding no es el bug — el bug es `var` compartiendo la misma celda

**Preguntas anticipadas:** ninguna típica.

**Transición:** Veamos las dos correcciones correctas.

---

### [F-46] IA Pattern 2 — corrección con `let` y con estilo funcional

**Tiempo:** 2 min

**Qué decir:**
- Corrección 1: `let` — crea una variable `j` nueva en cada bloque de iteración. `for (let j = 0; j < 5; j++) { funcs2.push(() => j); }`. Cada closure captura su propia `j` — celda distinta en heap. `funcs2[0]()` → 0 ✅, `funcs2[4]()` → 4 ✅.
- Corrección 2: estilo funcional — el problema nunca existe con parámetros. `Array.from({ length: 5 }, (_, k) => () => k)`. `Array.from` llama al callback con un parámetro `k` nuevo en cada invocación. Los parámetros son bindings fresh — no se comparten entre llamadas. `funcs3[0]()` → 0 ✅, `funcs3[4]()` → 4 ✅.
- Alternativa con map sobre un array de índices: `[0, 1, 2, 3, 4].map(k => () => k)`. El parámetro `k` de cada llamada al callback es siempre un binding nuevo.

**Conceptos clave:**
- `let`: scope de bloque = nuevo binding por iteración = closures independientes
- `Array.from` funcional: el parámetro `k` es siempre un binding nuevo — el problema nunca existe
- Ambas correcciones eliminan el alias compartido entre iteraciones

**Preguntas anticipadas:** ninguna típica.

**Transición:** El tercer patrón es el más fácil de detectar con TypeScript strict: el LLM no maneja todos los casos de un union type.

---

### [F-47] IA Pattern 3 — código sin narrowing que puede crashear en runtime

**Tiempo:** 4 min

**Qué decir:**
- El LLM asume que el argumento siempre será string aunque el tipo diga `string | number`. Aplica `valor.toUpperCase()` sin verificar.
- TypeScript strict: ❌ Property 'toUpperCase' does not exist on type 'string | number'. Property 'toUpperCase' does not exist on type 'number'.
- Por qué es peligroso en producción: sin strict mode o con `any`, el código compila sin advertencia. En runtime: `TypeError: valor.toUpperCase is not a function` cuando se pasa un número — crash en producción.
- Por qué la IA lo genera así: el LLM infiere del nombre de la función que suele recibir strings y aplica el método sin verificar — replica el patrón más común en los ejemplos de training.
- Este es el patrón donde TypeScript funciona como guardrail automático. El type narrowing obliga al programador a manejar cada caso del union type. TypeScript verifica exhaustividad.
- Mensaje final del bloque IA: el conocimiento de tipos, binding, aliases y closures no es teórico — es exactamente lo que necesitamos para revisar y corregir código generado por IA de manera efectiva.

**Conceptos clave:**
- TypeScript strict detecta code IA sin narrowing — error en compilación, no en runtime
- Sin strict o con `any`: el código compila y crashea en producción
- El type narrowing es el guardrail que obliga a manejar todos los casos del union

**Preguntas anticipadas:**
- *"¿El `never` type está relacionado con esto?"* → Exactamente. En un switch exhaustivo con un `default: const exhaustive: never = f;` TypeScript detecta en compilación si algún caso no fue manejado. Patrón avanzado — mencionarlo si surge.

**Transición:** Cerramos con la síntesis de los cinco conceptos grandes de la clase.

---

## CIERRE

---

### [F-48] Cierre — síntesis de la clase

**Tiempo:** 5 min + buffer de preguntas (hasta 6 min disponibles)

**Qué decir:**
- Recorrer los cinco bullets del resumen en 2-3 oraciones cada uno — sin repetir los detalles, solo conectarlos.
- "Aliases, closures y GC son la misma historia contada desde tres ángulos: los aliases explican qué es tener dos nombres para la misma celda; las closures explican cómo una función captura y extiende el tiempo de vida de una celda; el GC explica quién libera esa celda cuando ya nadie la necesita."
- "Gradual typing e inmutabilidad son herramientas de diseño que reducen la clase de bugs que estudiamos hoy: TypeScript strict detecta operaciones ilegales en compilación; la inmutabilidad elimina la fuente misma de los aliases peligrosos."
- Anunciar próxima clase: Tema 10 — Tipos de Datos (escalares, estructurados, uniones discriminadas y sistemas de tipos formales).

**Conceptos clave:**
- La historia unificada: aliases → closures → GC es la misma cadena de ciclo de vida de variables en heap
- Herramientas de diseño: gradual typing + inmutabilidad reducen los bugs que genera ese ciclo
- Hacia adelante: Tema 10 construye sobre union types y type narrowing de hoy

**Preguntas anticipadas:** libre según lo que haya surgido en clase.

---

## Notas docentes

### Secuencia pedagógica recomendada

El bloque 3 (GC) se apoya completamente en el bloque 2 (closures): explicar el GC antes de las closures pierde la conexión de "¿por qué hay objetos en el heap?". Mantener el orden: aliases → closures → GC es importante.

### Si queda tiempo extra (buffer ~6 min)

- Abrir el live coding de `crearContador` en TypeScript Playground para mostrar en tiempo real que el objeto existe después de que la función retornó.
- Mostrar `sys.getrefcount()` en Python REPL para hacer tangible el reference counting.
- Profundizar en la pregunta socrática sobre closures y fugas de memoria.

### Material de referencia para el docente

- Sebesta §5.3.3 (aliases), §7.4 (transparencia referencial), §9.5 (alias por paso por referencia), §6.11 (GC), Cap. 10 (closures/makeAdder)
- Gabbrielli §7.4 (closures, deep/shallow binding), §8.11 (mark-sweep defectos), §11 (FP), §16.9 (TypeScript/gradual typing)
- Louden §7.7 (aliases), §9.1 (transparencia referencial), §10.3 (closures), §10.5 (GC: reference counting + mark-sweep)