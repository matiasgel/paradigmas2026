# Minuta — Tema 09.2: Aliases, Closures, GC y Tipos

**Materia:** Paradigmas y Lenguajes de Programación 2026
**Duración:** 120 min (1 clase)
**Agente:** Dr. Roberto ✍️ — Class Writer · 2026-05-14
**Estado:** 🔲 Borrador — pendiente de revisión docente

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
| Bloque 1 — Aliases | F-01 a F-04 | 17 min |
| Bloque 2 — Closures | F-05 a F-09 | 20 min |
| Bloque 3 — GC | F-10 a F-14 | 18 min |
| Bloque 4 — Gradual Typing | F-15 a F-18 | 14 min |
| Bloque 5 — FP Inmutabilidad | F-19 a F-21 | 10 min |
| Bloque 6 — Contraste multilenguaje | F-22 a F-23 | 8 min |
| Bloque 7 — Bloque IA | F-24 a F-26 | 12 min |
| Cierre | F-27 a F-28 | 8 min + 11 buffer |
| **Total** | | **120 min** |

---

## PORTADA

---

### [F-00] Portada

**Tiempo estimado:** 2 min

**Qué decir:**
- Presentar brevemente la continuación de la clase anterior: "Semana pasada formalizamos la variable como 5-tupla, los momentos de binding y el ámbito estático. Hoy arrancamos donde quedamos: dos nombres que apuntan al mismo objeto."
- Mencionar la estructura de la clase: aliases → closures → garbage collection → gradual typing → FP → bloque IA.
- Señalar el prerequisito explícito: quien no vio la clase 09.1 va a tener lagunas en los ejemplos de binding y ciclo de vida.

**Conceptos clave:**
- La clase 09.2 es la segunda parte del bloque Variables/Binding
- La 5-tupla de 09.1 es el lenguaje base para todo lo de hoy

**Preguntas anticipadas:** ninguna en portada.

**Transición:** Arrancamos directamente con el primer concepto: ¿qué pasa cuando dos nombres apuntan al mismo objeto?

---

## BLOQUE 1 — Aliases: Dos Nombres, Un Objeto (17 min)

---

### [F-01] ¿Qué es un alias?

**Tiempo estimado:** 4 min

**Qué decir:**
- Definición de Sebesta §5.3.3: un alias ocurre cuando **dos nombres distintos** están vinculados a la **misma celda de memoria** en el mismo momento. No dos celdas con el mismo valor — una sola celda con dos nombres.
- El diagrama lo muestra bien: dos flechas, un solo rectángulo. La intuición es que "el mismo objeto tiene dos puertas de entrada".
- Remarcar las tres consecuencias: (1) cambiar desde uno afecta el otro silenciosamente, (2) el verificador formal pierde capacidad de razonamiento, (3) el compilador no puede optimizar porque no sabe si los punteros se solapan.
- No profundizar en análisis estático — eso es para la carrera, no para este curso. Lo que importa es la consecuencia de bugs silenciosos.

**Conceptos clave:**
- Alias = dos nombres, una sola celda (L-value compartido)
- La modificación es silenciosa: el programador puede no notar que hay dos nombres
- El compilador no puede asumir que dos nombres distintos apuntan a celdas distintas

**Preguntas anticipadas:**
- *"¿Un alias es siempre un bug?"* → No. A veces es intencional: pasar un objeto por referencia para modificarlo es usar aliases a propósito. El problema es cuando es accidental.
- *"¿En lenguajes funcionales hay aliases?"* → Buena pregunta — la contestamos en el bloque 5. Anticipar: en FP puro no hay mutación, así que los aliases son inofensivos.

**Transición:** Ahora veamos la fuente más común de aliases en TypeScript — la asignación de referencia de objeto.

---

### [F-02] Fuentes de aliases — referencias de objeto

**Tiempo estimado:** 5 min

**Qué decir:**
- Empezar con el ejemplo TypeScript: `const obj2 = obj1`. Preguntar al grupo si `obj2` es una copia o un alias. Esperar respuestas — la mayoría sabe la respuesta correcta pero no por qué.
- Explicar: en TypeScript, los objetos se pasan por referencia. La asignación `obj2 = obj1` no copia el objeto — copia la **referencia** (el puntero al heap). Desde la terminología de 09.1: el L-value de `obj2` y el L-value de `obj1` son el mismo.
- El ejemplo de Kotlin muestra el mismo patrón con una clase: `desplazar(origen, 5)` recibe `p` como alias de `origen`. El método puede modificar el objeto original.
- Mencionar Go con punteros explícitos como contraste: en Go el alias es explícito (`&x`, `*p`). En TypeScript es implícito para objetos.

**Conceptos clave:**
- Asignación de objeto en TypeScript = copiar la referencia (el puntero), no el objeto
- Pasar un objeto a una función = crear un alias dentro de esa función
- TypeScript y Kotlin hacen el alias implícito — Go lo hace explícito con `&`

**Preguntas anticipadas:**
- *"¿Los primitivos también tienen este problema?"* → No. Los primitivos (`number`, `boolean`, `string`) se pasan por valor — se copia el dato. Solo los objetos y arrays son por referencia.
- *"¿Esto pasa en Python también?"* → Exactamente igual. `a = b` sobre una lista en Python es un alias.

**Transición:** Tenemos aliases, sabemos que son peligrosos. ¿Cómo los detectamos y prevenimos?

---

### [F-03] Consecuencias y detección con `readonly`

**Tiempo estimado:** 4 min

**Qué decir:**
- Recorrer las tres consecuencias de tener aliases: razonamiento difícil, verificación formal imposible, optimización del compilador bloqueada.
- La herramienta de detección en TypeScript es `readonly` y `Readonly<T>`. Mostrarlo con el ejemplo de la función que recibe `readonly number[]`. El compilador **rechaza en compilación** cualquier intento de modificar `data`.
- Importante: `readonly` no impide crear el alias — impide **modificar a través del alias**. Es un guardrail, no una solución completa.
- Conectar con el bloque IA que viene más adelante: este patrón es uno de los tres errores más comunes en código generado por LLMs.

**Conceptos clave:**
- `readonly` en TypeScript impide modificar a través de la referencia
- `readonly` no previene el alias — previene la mutación a través de él
- El compilador con `strict: true` detecta violaciones de `readonly` en compilación

**Preguntas anticipadas:**
- *"¿`readonly` hace una copia internamente?"* → No. El objeto sigue siendo el mismo — solo cambia lo que el compilador permite hacer con él.

**Transición:** Sabemos detectar aliases con `readonly`. ¿Cómo los eliminamos cuando necesitamos una copia verdadera?

---

### [F-04] Shallow copy vs. deep copy

**Tiempo estimado:** 4 min

**Qué decir:**
- Este slide es muy concreto — explicar ambos ejemplos paso a paso.
- Shallow copy con spread `{ ...original }`: el objeto de primer nivel es una copia nueva, pero las propiedades que son objetos siguen siendo aliases. En el ejemplo, `copia1.config` y `original.config` apuntan al mismo objeto — modificar uno modifica el otro.
- Deep copy con `structuredClone()` (ES2022): copia todo el grafo de objetos. Ningún nivel comparte celda con el original. Es la solución real cuando hay objetos anidados.
- Regla práctica para llevarse: si el objeto es plano (sin anidación) → spread alcanza. Si hay anidación → `structuredClone()`.
- Nota de rendimiento: `structuredClone()` es más costoso que spread — tiene sentido solo cuando realmente necesitamos independencia total.

**Conceptos clave:**
- Shallow copy (`{ ...obj }`) → el primer nivel es independiente, los anidados son aliases
- Deep copy (`structuredClone()`) → ningún nivel comparte celda — ES2022
- Elegir según si el objeto tiene niveles anidados que necesitamos independizar

**Preguntas anticipadas:**
- *"¿Existe `JSON.parse(JSON.stringify(obj))`?"* → Sí, es el deep copy clásico antes de ES2022. Problema: no funciona con `Date`, `undefined`, `Map`, `Set`, funciones. `structuredClone()` maneja más tipos.

**Transición:** Bien. Comprendimos aliases. Ahora el segundo gran tema: ¿qué pasa cuando una función "recuerda" el entorno en el que fue creada? Eso es una closure.

---

## BLOQUE 2 — Closures: el Entorno que Viaja con la Función (20 min)

---

### [F-05] ¿Qué es una closure?

**Tiempo estimado:** 4 min

**Qué decir:**
- Definición de Sebesta §10 y Gabbrielli §7.4: una closure es la combinación de una **función** y el **entorno léxico** en el que fue definida.
- La intuición: la función "viaja" con una mochila — esa mochila tiene las variables de su ámbito de creación. Aunque ese ámbito haya cerrado (el activation record se destruyó), la mochila sigue disponible.
- El diagrama lo muestra: el frame del stack (la casa) ya no existe, pero hay un objeto en el heap que tiene las variables capturadas.
- Conectar con la 5-tupla de 09.1: las variables capturadas pasan de Categoría 2 (stack-dynamic) a Categoría 3 (heap-dynamic) cuando son capturadas por una closure. El tiempo de vida se extiende.

**Conceptos clave:**
- Closure = función + entorno léxico capturado al momento de la creación
- Las variables capturadas migran del stack al heap con duración extendida
- La closure "lleva su contexto consigo" aunque el ámbito original haya terminado

**Preguntas anticipadas:**
- *"¿Qué es el entorno léxico exactamente?"* → Es el conjunto de variables accesibles en el ámbito donde la función fue **definida** (no donde se llama). Viene del ámbito estático que vimos en 09.1.

**Transición:** Veamos una closure concreta en TypeScript y analicemos paso a paso qué pasa con el ciclo de vida de la variable capturada.

---

### [F-06] Closure en TypeScript — contador

**Tiempo estimado:** 5 min

**Qué decir:**
- Recorrer el código de `crearContador` línea por línea. Preguntar: "cuando `crearContador(10)` retorna, ¿qué pasa con `cuenta`?"
- La respuesta esperada habitual: "se libera porque la función terminó". La respuesta correcta: **no se libera** — `cuenta` escapa al heap porque el objeto retornado (`{ incrementar, valor }`) mantiene referencias a ella.
- Demostrar con los dos `console.log`: después de que `crearContador()` retornó, `c.incrementar()` sigue funcionando. Si `cuenta` se hubiera liberado, esto fallaría.
- Enfatizar la frase: "el activation record de `crearContador` fue destruido, pero `cuenta` sigue viva porque el GC detecta que hay una referencia activa desde `c`".
- Esta es la conexión entre closures y garbage collection — la closure es lo que mantiene la variable con vida.

**Conceptos clave:**
- `cuenta` escapa al heap porque la closure la mantiene referenciada
- El GC no libera `cuenta` mientras exista `c` (la closure está viva)
- El activation record de `crearContador` se destruyó — `cuenta` sobrevivió en heap

**Preguntas anticipadas:**
- *"¿Cómo sabe el motor que `cuenta` escapó al heap?"* → V8 usa "escape analysis" en la compilación JIT: detecta que `cuenta` es referenciada por las funciones retornadas y la aloja en el heap desde el principio.

**Transición:** El mismo patrón existe en otros lenguajes. Veamos Python, Go y Kotlin brevemente para confirmar que es un concepto universal.

---

### [F-07] Closures en Python, Go y Kotlin

**Tiempo estimado:** 4 min

**Qué decir:**
- Python: enfatizar `nonlocal`. En Python, las closures pueden leer variables capturadas sin declarar nada especial. Pero para **escribir** en ellas (modificarlas), se necesita `nonlocal`. Sin `nonlocal`, Python crea una variable local nueva con el mismo nombre — bug silencioso idéntico al de `var` en JS.
- Go: el código es casi idéntico al TypeScript. Go tiene closures de primera clase — la closure captura `cuenta` por referencia. El tipo de retorno `func() int` es una función sin argumentos que retorna int.
- Kotlin: lambda con captura. Notar que en Kotlin la variable capturada debe ser `var` para poder modificarla desde la lambda — `val` daría error de compilación.
- La nota sobre C es el contraste más pedagógico: los callbacks en C (`void (*f)(int)`) no tienen entorno léxico. El programador que venga de C necesita esta comparación para entender por qué las closures son útiles.

**Conceptos clave:**
- El patrón es el mismo en TypeScript, Python, Go y Kotlin — es una propiedad del lenguaje, no de la sintaxis
- Python: `nonlocal` es necesario para modificar (no solo leer) la variable capturada
- C no tiene closures: no hay captura de entorno, todo lo no-local debe ser global

**Preguntas anticipadas:**
- *"¿Java tiene closures?"* → Sí, a partir de Java 8 con lambdas. Pero con restricción: la variable capturada debe ser `final` o "effectively final" — no se puede modificar desde la lambda.

**Transición:** Ahora entendemos qué es una closure y dónde vive `cuenta`. El siguiente slide formaliza esa idea con el modelo de heap y stack.

---

### [F-08] Ciclo de vida extendido y el heap

**Tiempo estimado:** 3 min

**Qué decir:**
- Este slide es una síntesis visual y formal del concepto anterior. No reexplicar el ejemplo — usarlo para formalizar.
- Sin closure: la variable vive en el stack del activation record. Al retornar → destruida. Este es el comportamiento de las variables Categoría 2 de 09.1.
- Con closure: la variable capturada "migra" al heap. El motor detecta esto en escape analysis o en la resolución léxica. La variable pasa a tener tiempo de vida de Categoría 3.
- Conectar con GC: las variables capturadas por closures serán liberadas por el garbage collector cuando la closure quede inaccesible. Esto es lo que estudiamos en el bloque 3.

**Conceptos clave:**
- Variables capturadas → Categoría 3 (heap-dynamic), no Categoría 2 (stack-dynamic)
- El ciclo de vida de una variable capturada dura mientras dure la closure que la captura
- Esta es la conexión directa entre closures y GC

**Preguntas anticipadas:** ninguna típica en este punto.

**Transición:** Antes de pasar al GC, necesitamos ver un detalle crítico del binding en closures: la diferencia entre deep y shallow binding, y el bug más famoso de JavaScript.

---

### [F-09] Deep binding vs. Shallow binding — el bug de `var`

**Tiempo estimado:** 4 min

**Qué decir:**
- Este es el bug más clásico de JavaScript — muchos alumnos lo habrán visto aunque no sepan el nombre técnico.
- Con `var`: hay una sola variable `i` en el scope de la función que contiene el loop. Todas las closures capturan la **referencia** a esa misma variable. Cuando se ejecutan, `i` ya vale 3 (o 5, o lo que sea el tope del loop).
- Con `let`: por cada iteración del loop se crea un **nuevo binding** de `j`. Cada closure captura su propia `j`. Esta es la semántica de deep binding — capturo el entorno **en el momento de creación de la closure**.
- La tabla al final es el resumen: deep binding = momento de creación (TypeScript con `let`, Python, Haskell). Shallow binding = momento de llamada (ámbito dinámico, LISP clásico).
- Para el curso: TypeScript, Python y todos los lenguajes modernos usan deep binding. Shallow binding es casi historia — lo mencionamos por completitud y porque aparece en Gabbrielli §7.4.

**Conceptos clave:**
- `var` en loops = un solo binding compartido = bug de closures en loops
- `let` en loops = nuevo binding por iteración = comportamiento esperado intuitivamente
- Deep binding (moderno): la closure captura el entorno en su **creación**
- Shallow binding (histórico): la función usa el entorno en su **llamada**

**Preguntas anticipadas:**
- *"¿Cómo se evita el bug con `var` sin cambiar a `let`?"* → Con un IIFE: `(function(i){ funcs.push(() => i); })(i)`. Crea un nuevo scope por iteración. Solución pre-ES6 — hoy solo se usa `let`.

**Transición:** Bien. Tenemos closures — y sabemos que las variables capturadas viven en el heap. ¿Quién las libera? Eso es el garbage collector.

---

## BLOQUE 3 — Garbage Collection: Memoria Automática (18 min)

---

### [F-10] El problema de la memoria en heap

**Tiempo estimado:** 3 min

**Qué decir:**
- Recordar de 09.1: las variables de Categoría 3 (heap-explicit) y Categoría 4 (heap-implicit) viven en el heap. Categoría 4 = se crean implícitamente, se liberan por el GC.
- El stack se libera solo — al destruir el frame, todas las variables locales desaparecen. El heap no tiene frame — necesita otro mecanismo.
- Mostrar la tabla de estrategias brevemente: manual (C, C++), reference counting (Python, Swift), mark-and-sweep (Java, TypeScript/V8), ownership (Rust). El curso se centra en las dos intermedias.
- Anticipar: vamos a ver reference counting y mark-and-sweep en detalle porque TypeScript usa una variante combinada.

**Conceptos clave:**
- Stack → liberación automática al destruir el frame (Categoría 1 y 2)
- Heap → necesita mecanismo explícito de liberación (Categoría 3 y 4)
- Cuatro estrategias: manual, reference counting, mark-and-sweep, ownership

**Preguntas anticipadas:**
- *"¿TypeScript tiene `delete` o `free`?"* → No. TypeScript no expone gestión manual de memoria. V8 lo maneja todo. Hay `delete obj.property` pero borra una propiedad, no libera la celda del heap.

**Transición:** Empecemos con la estrategia más intuitiva: contar cuántas referencias hay activas a cada objeto.

---

### [F-11] Reference Counting — conteo de referencias

**Tiempo estimado:** 4 min

**Qué decir:**
- La idea es simple: cada objeto en heap lleva un contador. Cada vez que alguien apunta al objeto, +1. Cada vez que alguien deja de apuntar, -1. Cuando llega a 0 → nadie lo alcanza → liberar de inmediato.
- El pseudo-código en la slide (`del x → ref_count = 1`, `del y → ref_count = 0 → LIBERAR`) es el núcleo. Recorrerlo paso a paso.
- Ventaja principal: **determinismo**. En Python, `del x` libera inmediatamente si no hay más referencias. Útil para recursos con cleanup (archivos, sockets): el objeto los cierra exactamente cuando ya no se usa.
- Mencionar Python explícitamente: `sys.getrefcount()` permite ver el contador — buen ejercicio de laboratorio.

**Conceptos clave:**
- Liberación inmediata y determinista cuando el contador llega a 0
- Python usa reference counting como mecanismo principal
- Ventaja: el programador sabe exactamente cuándo se libera un objeto

**Preguntas anticipadas:**
- *"¿Tiene overhead?"* → Sí: cada asignación de referencia incrementa/decrementa el contador. Para objetos muy efímeros en loops intensos, este overhead puede ser significativo.

**Transición:** Reference counting tiene un problema crítico que lo hace insuficiente solo. ¿Alguno puede anticipar cuál es?

---

### [F-12] El talón de Aquiles: referencias circulares

**Tiempo estimado:** 4 min

**Qué decir:**
- Pedir al grupo que piense el escenario: `a` apunta a `b`, `b` apunta a `a`, y eliminamos las referencias externas (`a` y `b` del scope). ¿Cuánto vale `ref_count(a)`? 1. ¿Y `ref_count(b)`? 1. ¿Se libera alguno? No. **Memory leak.**
- El código de `Nodo` con `siguiente` circular lo muestra. No es un escenario teórico — las listas enlazadas circulares, los árboles con referencia al padre, y los grafos generan ciclos constantemente.
- Soluciones: Python agrega un **cycle detector** al reference counting (módulo `gc`). Swift usa `weak` references — al marcar una referencia como `weak`, el contador **no cuenta** esa referencia, y el ciclo se puede romper. Rust lo previene estructuralmente con el borrow checker.
- Para TypeScript/V8: el mark-and-sweep resuelve los ciclos — por eso V8 no solo usa reference counting.

**Conceptos clave:**
- Referencia circular = ciclo → ningún contador llega a 0 → memory leak
- Python: solución = cycle detector separado del RC principal
- Swift: `weak` references para romper ciclos manualmente
- Rust: el borrow checker prohíbe ciclos mutables en compilación

**Preguntas anticipadas:**
- *"¿Un ciclo siempre es un bug?"* → No. A veces es necesario (lista circular, árbol con padre). La responsabilidad es del programador en lenguajes con GC, o del diseño del tipo en Rust.

**Transición:** El algoritmo que sí resuelve los ciclos es mark-and-sweep. Veamos cómo funciona.

---

### [F-13] Mark-and-Sweep

**Tiempo estimado:** 4 min

**Qué decir:**
- Dos fases. Primero marcar — desde las raíces (stack y globales), trazar transitivamente todos los objetos alcanzables. Segundo barrer — todo lo no marcado es inaccesible y puede liberarse.
- El pseudo-diagrama del heap es clave: Obj1 y Obj3 alcanzables (marcados), Obj2 y Obj4 no alcanzables (liberados). Incluso si Obj2 y Obj4 se apuntaran mutuamente (ciclo), ambos están sin marcar → se liberan. Reference counting fallaría; mark-and-sweep no.
- El costo: mientras el GC trabaja, el programa **se pausa** (stop-the-world). En el V8 clásico, las pausas podían ser de cientos de milisegundos. Hoy el GC es incremental y concurrente, pero el principio es el mismo.
- Mencionara fragmentación brevemente: después de sweep, los objetos liberados dejan "huecos" en el heap. Sin compactación, el allocator tiene dificultad para encontrar bloques contiguos.

**Conceptos clave:**
- Mark: trazar todos los objetos alcanzables desde las raíces
- Sweep: liberar todo lo no marcado — incluyendo ciclos
- Costo: stop-the-world durante la ejecución del GC; fragmentación post-sweep

**Preguntas anticipadas:**
- *"¿Se puede hacer sin pausar el programa?"* → Sí — GC incremental y concurrente (lo hace V8). Requiere sincronización entre el GC y el programa en ejecución — complejo de implementar.

**Transición:** V8, el motor que ejecuta TypeScript y JavaScript, combina ambas técnicas en un GC generacional. Veamos cómo.

---

### [F-14] GC en V8 — TypeScript/JavaScript

**Tiempo estimado:** 3 min

**Qué decir:**
- V8 divide el heap en dos partes: generación joven (Young Gen) y generación vieja (Old Gen). La "hipótesis generacional" observa empíricamente que la mayoría de los objetos muere joven (closures temporales, objetos intermedios en expresiones).
- Minor GC sobre la generación joven: frecuente, barato, muy rápido (<1ms en V8 moderno). Los objetos que sobreviven migran a la generación vieja.
- Major GC sobre la generación vieja: infrecuente, más costoso. Solo se ejecuta cuando la generación vieja se llena.
- Compactación: V8 mueve los objetos vivos a posiciones contiguas para eliminar fragmentación. Los punteros se actualizan — por eso TypeScript no expone las direcciones de los objetos.
- Mensaje para llevar: en TypeScript, el programador **no gestiona memoria**. Sabe que existe un GC, entiende que las closures extienden el ciclo de vida de variables al heap, y confía en que V8 los libera eventualmente.

**Conceptos clave:**
- GC generacional: Young Gen (minor GC, frecuente, barato) + Old Gen (major GC, infrecuente)
- La hipótesis generacional: la mayoría de los objetos muere joven
- Compactación post-GC elimina fragmentación — los punteros son opacos en TypeScript por esta razón

**Preguntas anticipadas:** ninguna típica en este punto.

**Transición:** Pasemos a la segunda gran idea del día — la dimensión del tipado. TypeScript no es solo "JavaScript con tipos": es un ejemplo canónico de un concepto teórico llamado gradual typing.

---

## BLOQUE 4 — Gradual Typing: TypeScript como Caso Paradigmático (14 min)

---

### [F-15] El espectro del tipado

**Tiempo estimado:** 3 min

**Qué decir:**
- La tabla de los tres tipos de sistemas de tipado. Estático puro: los tipos se verifican en compilación, antes de que se ejecute una sola línea. Dinámico puro: los tipos se verifican en runtime, cuando se ejecuta la operación. Gradual: se puede elegir cuánto de cada uno.
- Conectar con 09.1: en 09.1 vimos que el binding de tipo puede ocurrir en compilación (TypeScript, Java, C) o en ejecución (Python, JavaScript). El gradual typing permite tener **ambas** en el mismo programa.
- La pregunta retórica para el grupo: "¿Por qué no usar estático puro siempre?" → Migración desde código existente (JavaScript), prototipado rápido, flexibilidad en configuraciones dinámicas.

**Conceptos clave:**
- Estático: tipos verificados en compilación; Dinámico: tipos verificados en runtime
- Gradual: elige dónde y cuánto — anotaciones opcionales en el mismo lenguaje
- TypeScript es el ejemplo canónico de gradual typing en producción masiva

**Preguntas anticipadas:**
- *"¿Groovy y Dart también son graduales?"* → Sí, pero TypeScript es el más estudiado en la bibliografía del curso (Gabbrielli §16.9 lo dedica una sección completa).

**Transición:** Veamos TypeScript concreto — los tres niveles de coverage que ofrece el sistema gradual.

---

### [F-16] TypeScript como caso canónico de gradual typing

**Tiempo estimado:** 4 min

**Qué decir:**
- Recorrer los tres niveles del código: (1) `any` implícito — como JavaScript puro, ninguna verificación, (2) tipos parciales — los argumentos y return están tipados, (3) `strict: true` — activa un conjunto de checkers adicionales.
- La migración incremental es la propuesta de valor de TypeScript: podés tomar una codebase de 100k líneas de JavaScript, renombrar `.js` → `.ts`, y **compila**. Luego vas agregando tipos donde más importa, sin reescribir todo de golpe.
- `tsconfig.json` con `"strict": true` activa `noImplicitAny`, `strictNullChecks`, `strictFunctionTypes` y varios más. Es el objetivo final — pero se puede llegar gradualmente.
- Esto es exactamente lo que Gabbrielli §16.9 describe como la propuesta del gradual typing: **no hay ruptura**, la migración es fluida.

**Conceptos clave:**
- Los tres niveles: `any` (dinámico), tipos parciales, `strict` (estático)
- La migración `.js` → `.ts` es inmediata — los tipos se agregan incrementalmente
- `strict: true` es el objetivo, `any` implícito es el punto de partida compatible

**Preguntas anticipadas:**
- *"¿`any` y `unknown` son lo mismo?"* → No. `any` desactiva la verificación de tipos en los dos sentidos. `unknown` es "no sé el tipo" pero sí requiere narrowing antes de usar — más seguro.

**Transición:** El mecanismo que TypeScript usa para razonar sobre union types es el type narrowing. Veamos cómo funciona y por qué es poderoso.

---

### [F-17] Type Narrowing — binding de tipo en runtime

**Tiempo estimado:** 4 min

**Qué decir:**
- El escenario: una función recibe `Resultado = string | number | null`. TypeScript no sabe cuál de los tres tipos es en runtime — tiene que ser el programador quien lo clarifique con condiciones.
- Recorrer la función `formatear` rama por rama. En cada `if`, TypeScript **refina** su conocimiento del tipo. Después del primer `if (r === null)`, en el resto de la función TypeScript sabe que `r` **no puede ser null**. Después del segundo `if (typeof r === "number")`, sabe que `r` es `string`.
- La última línea `return r.toUpperCase()` es válida porque TypeScript infiere que en ese punto, `r: string`. Si el programador hubiera olvidado el `if (typeof r === "number")`, TypeScript daría error: `Property 'toUpperCase' does not exist on type 'number'`.
- Conectar con el bloque IA del final: el type narrowing es el guardrail que detecta cuando el código IA no maneja todos los casos de un union type.

**Conceptos clave:**
- Narrowing: TypeScript refina el tipo conocido dentro de cada rama condicional
- El compilador verifica exhaustividad — si falta una rama, error de compilación
- `unknown` requiere narrowing antes de cualquier operación — más seguro que `any`

**Preguntas anticipadas:**
- *"¿Hay narrowing con `instanceof`?"* → Sí. `if (error instanceof TypeError)` es type narrowing para clases. `typeof` es para primitivos, `instanceof` para instancias de clase.

**Transición:** Una slide de síntesis antes de pasar al FP — ¿por qué el gradual typing importa en proyectos reales?

---

### [F-18] ¿Por qué gradual typing importa en la práctica?

**Tiempo estimado:** 3 min

**Qué decir:**
- Recorrer la tabla rápido — no leer cada celda, comentar las diferencias clave.
- La columna de JavaScript vs. TypeScript strict es el contraste más importante: los errores de tipo que en JavaScript explotan en runtime, en TypeScript strict se detectan en compilación.
- La fila de "Tamaño del equipo" es pedagógicamente útil: en proyectos pequeños, el overhead del tipado puede no valer la pena. En proyectos grandes con múltiples desarrolladores, los tipos son la documentación viva que previene que un cambio rompa otro módulo.
- La cita de Gabbrielli §16.9 como cierre de bloque: TypeScript demuestra que el gradual typing es viable en producción masiva — no es solo un experimento académico.

**Conceptos clave:**
- Gradual typing: los errores de tipo pasan de runtime a compilación gradualmente
- `strict: true` = máxima detección; equipos grandes se benefician más
- TypeScript es la validación empírica de la propuesta teórica del gradual typing

**Preguntas anticipadas:** ninguna típica.

**Transición:** Ahora el quinto bloque — un cambio de paradigma literal. En FP puro, no existen variables mutables. Solo bindings.

---

## BLOQUE 5 — Variables en Programación Funcional (10 min)

---

### [F-19] Bindings inmutables — no hay variables en FP puro

**Tiempo estimado:** 3 min

**Qué decir:**
- El contraste fundamental: en imperativo, una variable es una celda mutable — tiene L-value (dirección) y R-value (contenido modificable). En FP puro, no existe L-value — no hay dirección porque no hay celda modificable.
- En Haskell, `let x = 5` es una **asociación nombre-valor definitiva**, no una instrucción de escritura en memoria. Intentar `x = 6` da error — no porque Haskell no lo permita por decisión de diseño, sino porque el modelo semántico **no tiene mutación**.
- Consecuencia de Gabbrielli §11: la computación en FP puro es reescritura de expresiones. `f(x)` siempre produce el mismo resultado para el mismo `x` (referencialmente transparente). No hay estado oculto, no hay efectos secundarios.
- Conectar con aliases: en FP puro, los aliases son inofensivos. Si ningún binding puede cambiar, no importa cuántos nombres apunten al mismo valor — el valor nunca cambia.

**Conceptos clave:**
- FP puro: no hay L-value, no hay mutación, no hay asignación destructiva
- Los bindings en Haskell son definitivos — como constantes matemáticas
- Referencialmente transparente: `f(x)` siempre produce el mismo resultado para el mismo `x`

**Preguntas anticipadas:**
- *"¿Cómo hace Haskell para hacer IO o estado?"* → Mónadas (IO monad, State monad). Tema 05 ya los vio. El estado existe, pero está encapsulado y explícito — no hay efectos ocultos.

**Transición:** Scala y TypeScript no son FP puros, pero tienen herramientas para acercarse al estilo inmutable. Veamos `val` vs. `var` y el código funcional en TypeScript.

---

### [F-20] val vs. var — Scala y TypeScript funcional

**Tiempo estimado:** 4 min

**Qué decir:**
- Scala tiene dos palabras clave explícitas: `var` para variables imperativas mutables, `val` para bindings inmutables. La elección es del programador. La buena práctica en Scala es preferir `val` por defecto.
- TypeScript equivalente: `const` es el análogo a `val`. `let` es el análogo a `var`.
- Los dos fragmentos TypeScript muestran el mismo cálculo: uno imperativo (muta `suma` en cada iteración), uno funcional (construye el resultado con `reduce`, sin mutación). Ambos producen el mismo resultado — el funcional es más fácil de razonar porque no hay estado que cambie.
- `Readonly<T>` en TypeScript es la herramienta para hacer objetos inmutables. `readonly` en arrays también. Esto es TypeScript funcional: mismo lenguaje, mentalidad de FP.
- Conectar con el tema 11: en el bloque de paradigma funcional profundizaremos esto. Hoy es suficiente con la distinción `val` vs. `var` y la equivalencia TypeScript.

**Conceptos clave:**
- Scala: `val` = inmutable, `var` = mutable — elección explícita del programador
- TypeScript: `const` ≈ `val`, `let` ≈ `var`
- `Readonly<T>` y `as const` para inmutabilidad de objetos y arrays

**Preguntas anticipadas:**
- *"¿`const` en TypeScript hace deep freeze del objeto?"* → No. `const` impide reasignar la variable, pero el objeto apuntado puede mutarse. `Readonly<T>` impide mutación de las propiedades — pero tampoco es deep por defecto.

**Transición:** ¿Por qué la inmutabilidad reduce bugs? Un slide concreto lo muestra.

---

### [F-21] ¿Por qué la inmutabilidad reduce bugs?

**Tiempo estimado:** 3 min

**Qué decir:**
- El ejemplo de `config` con `cfg.retries = 0` es un bug real en código de producción. La función muta el objeto del llamador sin que el llamador lo sepa. En un codebase grande, rastrear de dónde viene esta mutación puede tomar horas.
- La solución funcional: la función trabaja con un nuevo binding `cfgLocal` — el original nunca se toca. El llamador puede confiar en que su objeto no cambió.
- La síntesis de las tres conexiones del bloque: (1) inmutabilidad elimina aliases peligrosos — si nada puede mutar, no importa cuántos nombres apuntan al mismo valor; (2) closures sobre bindings inmutables son seguras — no hay estado capturado que cambie sorpresivamente; (3) el GC libera bindings sin riesgo de efectos ocultos.

**Conceptos clave:**
- La inmutabilidad elimina una clase entera de bugs: mutación accidental de objetos compartidos
- `Readonly<T>` + spread `{ ...cfg, campo: nuevoValor }` es el patrón funcional en TypeScript
- Conexión triple: inmutabilidad → sin aliases peligrosos → closures seguras → GC limpio

**Preguntas anticipadas:** ninguna típica.

**Transición:** Antes del bloque IA, hagamos un recorrido rápido por cómo los lenguajes modernos resuelven todos estos problemas en conjunto.

---

## BLOQUE 6 — Contraste Multilenguaje: Gestión de Memoria Moderna (8 min)

---

### [F-22] Cuatro lenguajes, cuatro estrategias

**Tiempo estimado:** 4 min

**Qué decir:**
- Recorrer la tabla fila por fila. No leer cada celda — comentar las diferencias que más sorprenden.
- La fila de "Dangling pointer": en los cuatro lenguajes es **imposible**. Este fue el mayor problema de C y C++ durante décadas. Los lenguajes modernos lo resuelven cada uno a su manera.
- La fila de "Pausa del GC": en Rust es cero — no hay GC. En TypeScript, Python y Go hay pausas, aunque los GC modernos las minimizan (<1ms en V8 y Go). Para sistemas de tiempo real (audio, video, sistemas embebidos), Rust es la única opción segura.
- La fila de "Variables sin inicializar": Go es especial — zero values. Toda variable de tipo `int` vale 0, toda `string` vale `""`. Nunca hay basura en memoria. TypeScript strict da error en compilación; Python lanza `NameError` en runtime.

**Conceptos clave:**
- Los cuatro lenguajes modernos eliminan dangling pointers con estrategias diferentes
- Rust: sin GC, sin pausa — garantías en tiempo de compilación
- Go: zero values eliminan variables sin inicializar — semántica más segura que C

**Preguntas anticipadas:**
- *"¿Por qué no todos usamos Rust entonces?"* → Curva de aprendizaje alta (el borrow checker es complejo), menor ecosistema para web/data, no es gradual. TypeScript es más práctico para muchos dominios.

**Transición:** Rust es el caso más extremo — sin GC en absoluto. Un slide rápido para entender por qué.

---

### [F-23] Rust: ownership como garantía en compilación

**Tiempo estimado:** 4 min

**Qué decir:**
- El modelo de ownership de Rust: cada objeto tiene exactamente **un owner**. Cuando el owner sale del scope, el objeto se destruye automáticamente (trait `Drop`). No hay GC porque el compilador sabe exactamente cuándo cada objeto muere.
- El ejemplo de `nueva_sesion`: `s` se crea dentro de la función y se **transfiere** (move) al llamador al retornar. Si no se transfiere, se destruye al salir del scope de `nueva_sesion`.
- El borrow checker detecta dangling references en compilación. El comentario en el código (`drop(s); println!("{}", ref1.id)`) muestra un error de compilación — no de runtime. Este es el punto clave de Rust: **lo que en TypeScript sería un bug en producción, en Rust es un error de compilación**.
- Para el curso: no necesitamos profundizar en Rust. El mensaje es que existen lenguajes donde la seguridad de memoria es una propiedad del sistema de tipos, no del runtime.

**Conceptos clave:**
- Ownership: cada objeto tiene un único dueño; al salir del scope → destruido sin GC
- Borrow checker: detecta dangling references en compilación
- Rust elimina tanto los bugs de memoria como el overhead del GC

**Preguntas anticipadas:**
- *"¿`drop()` es como `free()` de C?"* → Conceptualmente similar — libera el objeto. Pero en Rust no es necesario llamarlo manualmente; el compilador lo inserta automáticamente. Si lo llamás explícitamente es para controlar el momento exacto.

**Transición:** Ahora el bloque final antes del cierre — tres patrones concretos de errores que los LLMs generan y cómo el conocimiento de hoy nos da las herramientas para detectarlos.

---

## BLOQUE 7 — Bloque IA: Aliases, Closures y Type Narrowing (12 min)

---

### [F-24] IA Pattern 1 — Alias de objeto sin advertencia

**Tiempo estimado:** 4 min

**Qué decir:**
- Este patrón aparece frecuentemente en código generado: el LLM escribe `const configBackup = config` y lo comenta como "guardando copia". No es una copia — es un alias.
- La detección: ¿la IA usó `=` sobre un objeto? Revisar si el destinatario es una variable nueva o si hay operador de copia.
- Recorrer las tres opciones: alias directo (bug), shallow copy con spread (correcta para objetos planos), deep copy con `structuredClone` (correcta para objetos con anidación).
- El punto pedagógico: el LLM no "sabe" la diferencia entre copiar un valor primitivo y copiar una referencia. Genera el mismo operador `=` para ambos casos. El programador que conoce el modelo de memoria puede detectarlo.

**Conceptos clave:**
- El LLM genera `=` sobre objetos como si fuera una copia — es un alias
- Detección: si el lado derecho es un identificador de objeto sin `{ ... }` ni `structuredClone` → alias
- Corrección según profundidad: spread para planos, `structuredClone` para anidados

**Preguntas anticipadas:** ninguna típica — es un bloque práctico.

**Transición:** El segundo patrón es el bug de `var` que ya vimos en el bloque de closures — pero ahora desde la perspectiva de código generado por IA.

---

### [F-25] IA Pattern 2 — Closures con `var` (bug de binding)

**Tiempo estimado:** 4 min

**Qué decir:**
- Los LLMs entrenados con código histórico a veces generan `var` en loops, especialmente cuando el corpus de entrenamiento incluye código JavaScript pre-ES6 (anterior a 2015).
- Mostrar el código incorrecto y explicar **por qué** todas las closures retornan 5: porque `var i` es una sola variable en el scope de la función, y todas las closures capturan la **referencia** a esa variable — no su valor en el momento de creación.
- La corrección con `let` no es solo sintáctica — implica semántica diferente: cada iteración tiene su propio binding de `j` en el scope del bloque. Las closures capturan entornos distintos.
- Conectar con deep binding: `let` garantiza deep binding por bloque — la closure captura el entorno en el momento de creación.

**Conceptos clave:**
- LLMs pueden generar `var` en loops — código legacy aún presente en el corpus
- `var`: scope de función = un solo binding = todas las closures ven el valor final
- `let`: scope de bloque = nuevo binding por iteración = closures independientes

**Preguntas anticipadas:** ninguna típica.

**Transición:** El tercer patrón es el más fácil de detectar con TypeScript strict: el LLM no maneja todos los casos de un union type.

---

### [F-26] IA Pattern 3 — Type narrowing como guardrail

**Tiempo estimado:** 4 min

**Qué decir:**
- Este es el patrón donde TypeScript funciona como guardrail automático. El LLM genera código que llama `.toUpperCase()` sobre un valor que podría ser `number`. TypeScript strict detecta esto en compilación.
- La corrección con narrowing: forzar al programador a manejar cada caso del union type. TypeScript verifica **exhaustividad** — si se agrega un nuevo tipo al union, el compilador avisa que hay ramas sin manejar.
- El ejemplo del `switch` exhaustivo es especialmente pedagógico: si alguien agrega `"rombo"` al union `Forma` sin actualizar `área`, TypeScript da error. El LLM que generó el switch no "sabe" esto — el compilador lo detecta.
- Mensaje final del bloque IA: el conocimiento de tipos, binding, aliases y closures no es teórico — es exactamente lo que necesitamos para revisar y corregir código generado por IA de manera efectiva.

**Conceptos clave:**
- TypeScript strict detecta code IA sin narrowing — error en compilación, no en runtime
- El switch exhaustivo + narrowing garantiza que todos los casos del union están manejados
- La verificación de exhaustividad es automática: agregar un tipo al union fuerza actualizar el switch

**Preguntas anticipadas:**
- *"¿El `never` type está relacionado con esto?"* → Exactamente. En un switch exhaustivo con un `default: const exhaustive: never = f;` TypeScript detecta en compilación si algún caso no fue manejado. Patrón avanzado — mencionarlo si surge.

**Transición:** Antes del cierre, una pregunta socrática para reflexionar sobre el límite entre una closure útil y una fuga de memoria.

---

## PREGUNTAS Y CIERRE

---

### [F-27] Pregunta socrática — ¿cierre o fuga?

**Tiempo estimado:** 5 min

**Qué decir:**
- Presentar el código sin revelar la respuesta. Dejar 30-60 segundos de silencio.
- Guiar la discusión con las tres preguntas del slide: (1) ¿cuándo esta closure es correcta? → Cuando `logApp` se usa por un tiempo finito y luego se descarta. (2) ¿cuándo es una fuga? → Cuando `logApp` vive indefinidamente (variable global, módulo singleton) y acumula eventos sin límite. (3) ¿el GC puede ayudar? → Sí, si `logApp` queda inaccesible, el GC libera tanto la closure como `log`. No puede ayudar si `logApp` sigue siendo accesible — el GC no puede saber si los datos son "útiles" o no.
- El punto central: el GC libera objetos **inaccesibles**, no objetos **inútiles**. Si el programador mantiene una referencia viva a una closure con estado acumulado, el GC no puede hacer nada. La fuga es semántica, no sintáctica.

**Conceptos clave:**
- El GC libera objetos inaccesibles — no sabe si son "útiles"
- Una closure que acumula estado indefinidamente es una fuga si nadie la elimina
- La solución: limitar el tiempo de vida de la closure (local scope, `WeakRef`, o descarte explícito)

**Preguntas anticipadas:**
- *"¿`WeakRef` en JavaScript sirve para esto?"* → Sí. Un `WeakRef` permite mantener una referencia a un objeto sin que el GC lo cuente como referencia activa. Si no hay otras refs, el GC lo libera. Pero `WeakRef` es avanzado y fuera del scope de hoy.

**Transición:** Cerramos con la síntesis de los cinco conceptos grandes de la clase.

---

### [F-28] Cierre — síntesis de la clase

**Tiempo estimado:** 3 min + buffer de preguntas (hasta 11 min disponibles)

**Qué decir:**
- Recorrer los cinco bullets del resumen en 2-3 oraciones cada uno — sin repetir los detalles, solo conectarlos.
- "Aliases, closures y GC son la misma historia contada desde tres ángulos: los aliases explican qué es tener dos nombres para la misma celda; las closures explican cómo una función captura y extiende el tiempo de vida de una celda; el GC explica quién libera esa celda cuando ya nadie la necesita."
- "Gradual typing e inmutabilidad son herramientas de diseño que reducen la clase de bugs que estudiamos hoy: TypeScript strict detecta operaciones ilegales en compilación; la inmutabilidad elimina la fuente misma de los aliases peligrosos."
- Anunciar TP si corresponde. Anunciar próxima clase: Tema 10 — Tipos de Datos (escalares, estructurados, uniones y sistemas de tipos formales).

**Conceptos clave:**
- La historia unificada: aliases → closures → GC es la misma cadena de ciclo de vida de variables en heap
- Herramientas de diseño: gradual typing + inmutabilidad reducen los bugs que genera ese ciclo
- Hacia adelante: Tema 10 construye sobre union types y type narrowing de hoy

**Preguntas anticipadas:** libre según lo que haya surgido en clase.

---

## Notas docentes

### Secuencia pedagógica recomendada

El bloque 3 (GC) se apoya completamente en el bloque 2 (closures): explicar el GC antes de las closures pierde la conexión de "¿por qué hay objetos en el heap?". Mantener el orden: aliases → closures → GC es importante.

### Si queda tiempo extra (buffer ~11 min)

- Abrir el live coding de `crearContador` en TypeScript Playground para mostrar en tiempo real que el objeto existe después de que la función retornó.
- Mostrar `sys.getrefcount()` en Python REPL para hacer tangible el reference counting.
- Discutir la pregunta socrática más en profundidad (F-27).

### Material de referencia para el docente

- Sebesta §5.3.3 (aliases), §10 (closures), §6.11 (GC), §5.8 (FP)
- Gabbrielli §7.4 (closures, deep/shallow binding), §11 (FP), §16.9 (TypeScript/gradual typing)
- Louden §7.7 (aliases), §10.3 (closures), §10.5 (GC)
