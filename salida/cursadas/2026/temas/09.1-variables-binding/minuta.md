# Minuta — Tema 09.1: Variables, Binding y Ámbito

**Materia:** Paradigmas y Lenguajes de Programación 2026
**Duración:** 120 min (1 clase)
**Agente:** Dr. Roberto ✍️ — Class Writer · 2026-06-28
**Estado:** 🔲 Borrador — pendiente de revisión docente
**Baseline:** `clase_dada.txt` (filminas reales dadas en clase)

---

## Objetivos de la clase

| # | Objetivo | Bloom |
|---|---|---|
| OA1 | Describir la variable como 5-tupla `<nombre, dirección, tipo, L-valor, R-valor>` | Recordar |
| OA2 | Distinguir los 6 momentos de binding | Comprender |
| OA3 | Clasificar variables según sus 4 categorías de tiempo de vida | Analizar |
| OA4 | Comparar ámbito estático vs. dinámico | Analizar |
| OA5 | Diferenciar tipado fuerte/débil y binding estático/dinámico como dimensiones ortogonales | Analizar |
| OA6 | Aplicar el algoritmo de resolución de ámbito estático en código TypeScript | Aplicar |
| OA7 | Detectar errores de ámbito, hoisting y variables globales silenciosas en código generado por IA | Evaluar |

---

## Trazabilidad bibliográfica (ChromaDB)

Las siguientes citas están respaldadas por la knowledge base ChromaDB (3 libros ingestados):

- **Sebesta (2019)** — *Concepts of Programming Languages*, 12th ed., Pearson. Cap. 5 (§5.3–5.8), pp. 221–258. Archivo: `221-258.txt`.
- **Gabbrielli & Martini (2023)** — *Programming Languages: Principles and Paradigms*, 2nd ed., Springer. Cap. 4 (§4.3, pp. 083–105), Cap. 5 (pp. 106–135), Cap. 8 (§8.8, pp. 136–282).
- **Louden & Lambert (2012)** — *Programming Languages: Principles and Practices*, 3rd ed., Course Technology. Cap. 7 (§7.5, pp. 210–330).

---

## BLOQUE 1 — Variable como Abstracción (20 min)
---

### [F-00] Portada

**Tiempo:** 1 min

**Qué decir:**
- Presentar la clase: "Hoy arrancamos el bloque de Variables, Binding y Ámbito. Es la base conceptual sobre la que se apoyan closures, GC y tipos — todo lo que viene en 09.2 y 10."
- Anunciar duración: 120 min, 7 bloques, actividad práctica al final.

**Transición:** Empecemos por el origen físico de toda variable: la arquitectura Von Neumann.

---

### [F-01] Von Neumann: el origen de la variable

**Tiempo:** 4 min

**Qué decir:**
- Arrancar con la pregunta: "¿qué es exactamente una variable?" — dejar 15 segundos de silencio. La respuesta habitual es "un nombre que guarda un valor". Está bien, pero es incompleta.
- Mostrar el modelo Von Neumann: la memoria como celdas numeradas y el procesador que las lee y escribe. El lenguaje es una capa que le pone nombre a las celdas y esconde las direcciones.
- La sentencia de asignación destruye el valor previo de la celda — por eso se llama "modificación destructiva". En lenguajes funcionales puros esto no existe.
- Remarcar: la inmutabilidad (`const`, `val`, `let` en Rust) es una restricción artificial del lenguaje, no del hardware. El hardware siempre permite escritura destructiva.

**Conceptos clave:**
- La variable abstrae la celda de memoria Von Neumann
- Nombre ≠ dirección ≠ valor — son tres cosas distintas
- La asignación es una operación destructiva sobre una celda

**Preguntas anticipadas:**
- *"¿Una variable en Python es lo mismo?"* → Sí, el modelo es el mismo aunque Python oculta más cosas. Lo vemos en F-05.
- *"¿Qué es una variable anónima?"* → Un objeto creado con `new` sin asignar a ningún nombre — tiene dirección y valor pero no nombre.

**Transición:** Veamos qué hace exactamente el compilador/runtime por nosotros para construir esa abstracción.

---

### [F-02] La abstracción en capas

**Tiempo:** 2 min

**Qué decir:**
- Recorrer la tabla fila por fila — es el núcleo de la slide: celda → variable, dirección → nombre, modificación destructiva → asignación. Estos mapeos justifican por qué existen los lenguajes de alto nivel.
- Los tres puntos sobre "lo que el compilador hace por nosotros" son la transición natural al binding: asignar/liberar celdas, traducir nombres a direcciones, verificar tipos. Eso es exactamente lo que estudiaremos en el bloque 2.

**Conceptos clave:**
- El compilador/runtime abstrae tres tareas: allocation, resolución de nombres, verificación de tipos
- La tabla hardware → lenguaje es la justificación de toda la semántica de variables

**Transición:** Ahora precisemos qué atributos tiene esa abstracción. Porque no es solo nombre y valor — hay seis atributos formales.

---

### [F-03] Los seis atributos de una variable

**Tiempo:** 4 min

**Qué decir:**
- Recorrer la tabla fila por fila. No leer — explicar cada atributo con una oración.
- Énfasis en que **tiempo de vida** y **ámbito** son cosas distintas: el tiempo de vida es sobre cuándo la variable existe en memoria; el ámbito es sobre cuándo su nombre es visible. Una variable puede existir pero estar fuera de ámbito.
- La 5-tupla `<nombre, dirección, tipo, L-valor, R-valor>` es la formalización de Sebesta — agrupa tiempo de vida con ámbito como atributo de contexto. Cada atributo se vincula en un momento distinto — eso es el binding.
- El nombre puede no existir: objetos creados con `new Nodo()` sin asignar tienen L-value y R-value pero no nombre.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4.3, p. 221–258: "The lifetime of a variable is the time during which the variable is bound to a specific memory location."
- Sebesta (2019), §5.3: "The name, address, type, and value attributes of variables are discussed in the following subsections."

**Conceptos clave:**
- L-value = dirección; R-value = contenido
- Tiempo de vida ≠ ámbito — son atributos independientes
- La 5-tupla es la formalización canónica de Sebesta

**Transición:** Veamos L-value y R-value en detalle — es la distinción más importante para entender asignación y aliases.

---

### [F-04] L-value y R-value — el doble rol de una variable

**Tiempo:** 3 min

**Qué decir:**
- En `x = y + 1`: cuando `x` aparece a la izquierda del `=`, denota la dirección donde escribir (L-value). Cuando `y` aparece a la derecha, denota el contenido a leer (R-value). El mismo nombre puede ser L-value o R-value según su posición.
- La definición formal de Gabbrielli & Martini es la cita exacta: l-values representan ubicaciones, r-values representan valores almacenables.
- El punto sobre constantes: `const PI = 3.14` tiene L-value (la celda existe) pero el lenguaje prohíbe usarla como L-value en una nueva asignación. `PI = 2.71` → error de compilación, no error de hardware.

**Trazabilidad bibliográfica:**
- Gabbrielli & Martini (2023), §8.4, p. 136–282: "l-values are those values that indicate locations and therefore are the values of expressions that can be on the left of an assignment command. On the other hand, r-values are the values that can be stored in locations."
- Sebesta (2019), §5.3.2, p. 221–258: "A variable's value is sometimes called its r-value because it is what is required when the name of the variable appears on the right side of an assignment statement. To access the r-value, the l-value must be determined first."

**Conceptos clave:**
- L-value = dirección (destino de escritura); R-value = contenido (fuente de lectura)
- Una constante tiene L-value pero el lenguaje prohíbe reasignarla
- El mismo nombre puede actuar como L-value o R-value según su posición

**Transición:** Veamos cómo Python expone el L-value con `id()` — TypeScript lo oculta, Python lo muestra.

---

### [F-05] L-value y R-value — código Python

**Tiempo:** 2 min

**Qué decir:**
- Python con `id()` sirve para mostrar que el L-value existe aunque TypeScript lo oculte — el `id()` de Python es la dirección real del objeto en heap.
- Remarcar: la reasignación `contador = 43` crea un NUEVO objeto — no modifica el existente. El `id()` cambia. Esto es heap implícita (categoría 4, lo vemos en F-27).
- El contraste con `lista.append(4)`: misma dirección, contenido modificado — objeto mutable.

**Conceptos clave:**
- `id()` expone el L-value (dirección) en Python
- Reasignar un primitivo crea un nuevo objeto (nueva dirección)
- Los objetos mutables conservan su dirección al modificarlos

**Transición:** Veamos la 5-tupla en cuatro lenguajes distintos — mismo concepto, cuatro perspectivas.

---

### [F-06] La 5-tupla — TypeScript y Kotlin

**Tiempo:** 2 min

**Qué decir:**
- Pasar rápido — es una confirmación visual de que la 5-tupla aplica a todos los lenguajes, no solo a TypeScript.
- TypeScript: `let x: number = 42` — tipo vinculado en compilación, dirección gestionada por V8 en carga, ámbito de bloque.
- `const limite` — binding de VALOR inmutable: el lenguaje prohíbe re-asignar, pero la celda sigue existiendo (tiene L-value).
- Kotlin: `var` (mutable) vs `val` (inmutable de valor) — equivalente a TypeScript `let`/`const` para primitivos.

**Conceptos clave:**
- La 5-tupla es universal — varía cómo se expone, no si existe
- `const`/`val` inmutabilizan el binding de valor, no el L-value

**Transición:** Veamos Rust y Go — dos perspectivas más extremas.

---

### [F-07] La 5-tupla — Rust y Go

**Tiempo:** 2 min

**Qué decir:**
- Rust muestra explícitamente el L-value como puntero raw — `let addr = &x as *const i32` da la dirección física de `x` en el stack. Esto es seguro en Rust porque el ownership garantiza que la dirección es válida.
- La inmutabilidad en Rust es la regla por defecto: `let x = 42` es inmutable; `let mut y = 42` requiere declaración explícita de mutabilidad.
- Go: los zero values son una decisión de diseño que elimina la clase de errores de "usar variable no inicializada" que tiene C. `var n int` → `n = 0`, nunca hay basura.

**Conceptos clave:**
- Rust expone el L-value de forma segura (ownership garantiza validez)
- Inmutabilidad por defecto en Rust — mutabilidad explícita con `mut`
- Go zero values: `0`, `""`, `false`, `nil` — sin basura por diseño

**Transición:** Ahora que entendemos qué es la variable, pasamos a entender cuándo se establecen sus atributos. Eso es el binding.

---

## BLOQUE 2 — Binding: el momento de la vinculación (12 min)
---

### [F-08] ¿Qué es el Binding?

**Tiempo:** 4 min

**Qué decir:**
- Definición precisa: binding = la asociación entre una entidad y uno de sus atributos, establecida en un momento determinado. La clave es "momento determinado" — eso es lo que distingue los lenguajes.
- El binding no es solo sobre variables — aplica a operadores, literales, subprogramas. El significado de `*` como multiplicación es un binding establecido en tiempo de diseño del lenguaje.
- Contraste con lenguajes funcionales: en Haskell un valor se vincula a un nombre una sola vez — no existe re-asignación. Por eso no se necesita un binding de ubicación (L-value) separado.
- Tradeoff central: binding temprano → eficiente (la dirección está en el ejecutable, no hay que computarla en runtime); binding tardío → flexible (podés cambiar qué hace un operador, cambiar el tipo de una variable).
- El momento determina dónde se detectan los errores: compilación = antes de ejecutar; ejecución = mientras el usuario usa la app.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4, p. 221–258: "A binding is static if it first occurs before run time begins and remains unchanged throughout program execution. If the binding first occurs during run time or can change in the course of program execution, it is called dynamic."
- Gabbrielli & Martini (2023), §4, p. 083–105: "The binding of an identifier to a variable, for example, is defined in the program but is effectively created only when execution reaches the point where the declaration is."

**Conceptos clave:**
- Binding = asociación entidad ↔ atributo en un momento
- Binding temprano ↔ eficiencia; binding tardío ↔ flexibilidad
- No es solo sobre variables — aplica a operadores, literales, subprogramas

**Preguntas anticipadas:**
- *"¿El binding siempre es para variables?"* → No — el significado de `*` como multiplicación es un binding establecido en tiempo de diseño del lenguaje. Lo vemos en la próxima tabla.

**Transición:** ¿En cuántos momentos puede ocurrir el binding? Exactamente seis.

---

### [F-09] Los 6 tiempos de binding

**Tiempo:** 4 min

**Qué decir:**
- Recorrer la tabla de arriba a abajo — son los 6 momentos en orden cronológico.
- El "tiempo de diseño" es el menos obvio: cuando los diseñadores del lenguaje deciden que `*` significa multiplicación, están haciendo un binding. No está en el código del programador — está en la especificación del lenguaje.
- "Tiempo de implementación": el rango de `number` en TypeScript (IEEE 754 float64) es una decisión de los implementadores del compilador, no del diseñador del lenguaje ni del programador.
- Hacer énfasis en la distinción compilación vs. ejecución: el tipo se vincula en compilación (estático), pero el valor se vincula en ejecución. Esto va a ser clave para los próximos bloques.
- El refinamiento de Louden: el binding estático se subdivide (translation, link, load time) y el dinámico también (entrada/salida de procedimiento, asignación).

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4, p. 221–258: tabla de tiempos de vinculación.
- Louden & Lambert (2012), §7.5, p. 210–330: "Location bindings of variables — the environment at line 10."
- Gabbrielli & Martini (2023), §4, p. 083–105: "In the previous description we have ignored other important phases, such as linking and loading in which other bindings (for example for external names referring to objects in other modules)."

**Conceptos clave:**
- Los 6 momentos en orden: diseño → implementación → compilación → linkeo → carga → ejecución
- Tipo: binding en compilación (TypeScript) vs. en ejecución (Python)
- Valor: siempre se vincula en ejecución

**Transición:** Veamos todos los tiempos en un solo fragmento de código para solidificar la idea.

---

### [F-10] Los 6 tiempos — análisis de un fragmento TypeScript

**Tiempo:** 4 min

**Qué decir:**
- Mostrar el fragmento dos líneas. Luego mostrar los comentarios de a uno — preguntar a la clase antes de revelar cada uno qué binding ocurre ahí.
- La pregunta "¿cuándo se vincula el tipo de `count`?" tiene respuesta en compilación (TypeScript lo infiere o verifica cuando transpila). La pregunta "¿cuándo se vincula el valor de `count`?" tiene respuesta en ejecución (cuando se ejecuta la línea `count = count + 5`).
- El rango de `number` (IEEE 754 float64) es implementación del compilador — no del lenguaje ni del programador.
- El significado del operador `+` se resuelve en compilación: `number + number` = suma numérica.
- Este ejercicio de dos minutos fija la distinción más importante del bloque.

**Conceptos clave:**
- El mismo fragmento involucra bindings en múltiples momentos simultáneamente
- Tipo → compilación; valor → ejecución; rango del tipo → implementación
- Significado del operador `+` → compilación (resolución de sobrecarga)

**Transición:** Ahora entramos al binding de tipos en detalle — hay dos dimensiones independientes que hay que mantener separadas.

---

## BLOQUE 3 — Binding de Tipos (16 min)
---

### [F-11] Binding de tipos — estático vs. dinámico

**Tiempo:** 3 min

**Qué decir:**
- Presentar la tabla como la dimensión 1: el momento del binding de tipo. Estático = compilación; dinámico = ejecución.
- Énfasis: estático/dinámico es sobre CUÁNDO se vincula el tipo, no sobre si el tipo puede cambiar. En estático no puede cambiar; en dinámico sí.
- Preguntar a la clase: "¿Qué ventaja tiene el binding estático de tipos?" — la respuesta es detección de errores en compilación antes de ejecutar.
- TypeScript tiene binding estático (tipo fijo en compilación), pero compila a JavaScript (binding dinámico). El tipado de TS desaparece en runtime — solo existe en el código fuente y en el compilador.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4.2, p. 221–258: "The primary advantage of dynamic binding of variables to types is that it provides more programming flexibility."
- Gabbrielli & Martini (2023), §8, p. 136–282: "A language has static typing if its checking of type constraints can be conducted on the program text at compile time. Otherwise, it has dynamic typing."

**Conceptos clave:**
- Estático/dinámico = cuándo se establece el tipo (compilación vs. ejecución)
- Estático: tipo fijo, error en compilación; dinámico: tipo flexible, error en runtime
- TypeScript es estático en compilación pero compila a JavaScript dinámico

**Transición:** La segunda dimensión es ortogonal: fuerte vs. débil.

---

### [F-12] Binding de tipos — fuerte vs. débil

**Tiempo:** 2 min

**Qué decir:**
- Énfasis principal: fuerte/débil es ORTOGONAL a estático/dinámico. Un lenguaje puede ser cualquier combinación de los cuatro.
- Ejemplos de combinaciones: TypeScript = estático + fuerte. Python = dinámico + fuerte. JavaScript = dinámico + débil. C = estático + débil. Haskell/Rust = estático + fuerte.
- La cita de Gabbrielli es clave: "los lenguajes con verificación de tipos fuerte tienden a tener pocas coerciones. En C, el sistema de tipos está diseñado para poder ser eludido."
- Una coerción es una conversión automática. En tipado débil ocurre silenciosamente — resultado incorrecto sin aviso. En tipado fuerte, error explícito.

**Trazabilidad bibliográfica:**
- Gabbrielli & Martini (2023), §8.3, p. 136–282: "Languages with strong type checking tend to have few coercions. On the other hand, in a language like C, the type system is designed to be by-passed and so permits numerous coercions."
- Sebesta (2019), §5.4.2, p. 221–258: "The value of strong typing is weakened by coercion. Languages with a great deal of coercion, like C, and C++, are less reliable than those with no coercion, such as ML and F#."

**Conceptos clave:**
- Fuerte/débil = qué tan estricto es el chequeo (sin/con coerciones implícitas)
- Las dos dimensiones son independientes — cualquier combinación existe
- C es estático + débil; Python es dinámico + fuerte; JS es dinámico + débil

**Transición:** Veamos la inferencia — que es estático pero sin declaración explícita.

---

### [F-13] Inferencia de tipos — concepto

**Tiempo:** 2 min

**Qué decir:**
- La inferencia es binding estático sin declaración explícita — el compilador lo deduce del contexto. No es binding dinámico — sigue ocurriendo en compilación.
- Dos formas: unidireccional (del valor asignado) y bidireccional (del contexto de uso).
- Diferencia fundamental con tipado dinámico: la inferencia es en compilación, no hay overhead en runtime, el tipo no cambia una vez inferido.

**Trazabilidad bibliográfica:**
- Gabbrielli & Martini (2023), §8.8, p. 136–282: "Type inference is exactly this process of the attribution of a type to an expression in which explicit type declarations of its components do not occur."

**Conceptos clave:**
- Inferencia = binding estático sin declaración explícita del programador
- No confundir inferencia con binding dinámico
- Dos formas: unidireccional (del valor) y bidireccional (del contexto)

**Transición:** Veamos la inferencia en TypeScript concreto.

---

### [F-14] Inferencia de tipos — TypeScript

**Tiempo:** 2 min

**Qué decir:**
- El ejemplo muestra inferencia bidireccional: `items` se infiere como `number[]` por el literal; `x` en el `forEach` se infiere como `number` por el contexto del array.
- `items.reduce((acc, x) => acc + x, 0)` — el acumulador inicial `0` determina el tipo del resultado: `number`.
- El compilador detecta `x.length` como error sin anotación explícita — `number` no tiene `.length`.

**Conceptos clave:**
- TypeScript infiere tipos en compilación sin declaraciones explícitas
- Inferencia bidireccional: el contexto del array determina el tipo del parámetro
- El compilador puede rechazar código incorrecto aunque no haya anotaciones

**Transición:** Veamos el contraste: Python con binding dinámico real.

---

### [F-15] Binding dinámico de tipo — Python

**Tiempo:** 2 min

**Qué decir:**
- En Python el tipo se vincula en cada asignación — puede cambiar completamente. `x` pasa de `list` a `str` con una reasignación.
- Python ES fuertemente tipado: no permite operaciones incompatibles sin conversión. `x + 42` da `TypeError` en runtime — no en compilación.
- Para mezclar, se requiere conversión explícita: `x + str(42)` o `int("5") + 42`.

**Conceptos clave:**
- Python: binding dinámico — el tipo cambia en cada asignación
- Python es fuerte: las operaciones incompatibles dan excepción explícita
- La conversión siempre es explícita

**Transición:** Veamos el extremo opuesto: JavaScript con tipado débil y coerciones silenciosas.

---

### [F-16] Coerciones — JavaScript (tipado débil)

**Tiempo:** 2 min

**Qué decir:**
- El ejemplo de JavaScript es el más impactante: `"5" + 3 = "53"` pero `"5" - 3 = 2`. El tipo de coerción depende del operador — no hay regla consistente. Eso es tipado débil.
- `==` hace coerciones, `===` no. `0 == false` → `true`; `0 === false` → `false`.
- Los casos famosos: `[] + [] = ""`, `[] + {} = "[object Object]"` — resultados contraintuitivos.

**Conceptos clave:**
- JavaScript convierte tipos automáticamente sin avisar
- `+` con string concatena; `-` siempre es aritmético
- `==` coerciona, `===` no — siempre usar `===`

**Transición:** Veamos cómo TypeScript strict y Python rechazan estas coerciones.

---

### [F-17] Coerciones — TypeScript strict y Python

**Tiempo:** 3 min

**Qué decir:**
- TypeScript strict corta esto en compilación — el error TS2365 aparece en el editor, antes de ejecutar cualquier código.
- Si queremos concatenar, la conversión debe ser explícita: `a + b.toString()` o `String(b) + a`.
- Python es fuerte y dinámico: el tipo es flexible pero las operaciones incompatibles siempre dan excepción explícita, nunca resultado silencioso incorrecto.
- Preguntar: "¿Preferirían que el error salga en compilación o en runtime?" — la respuesta obvia es compilación, pero hay contextos (scripting rápido, prototipado) donde el dinamismo tiene valor.

**Conceptos clave:**
- Débil ≠ dinámico — JavaScript es dinámico Y débil; Python es dinámico Y fuerte
- Fuerte = errores explícitos; débil = resultados silenciosos potencialmente incorrectos
- TypeScript strict y Python exigen conversión explícita para mezclar tipos

**Transición:** Ahora que entendemos el binding de tipos, pasamos al binding de almacenamiento — ¿cuándo y dónde vive la variable en memoria?

---

## BLOQUE 4 — Binding de Almacenamiento (26 min)
---

### [F-18] Las 4 categorías de variables

**Tiempo:** 3 min

**Qué decir:**
- Presentar la tabla como el mapa del bloque — van a ver las cuatro categorías en detalle. La tabla es una vista rápida para orientarse.
- La columna "Permite recursión" es clave: las estáticas no la permiten porque hay un solo frame para toda la vida del programa. Las demás sí.
- Definiciones base: allocation = tomar celda del pool; deallocation = devolver celda al pool.
- No explicar cada categoría aquí — solo dar el panorama. Las slides siguientes desarrollan cada una.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4.3, p. 221–258: "The memory cell to which a variable is bound must be taken from a pool of available memory. This process is called allocation. Deallocation is the process of placing a memory cell that has been unbound from a variable back into the pool of available memory."

**Conceptos clave:**
- Las 4 categorías se distinguen por cuándo ocurre el binding de almacenamiento
- Estáticas = tiempo de vida = toda la ejecución; stack-dynamic = activación del subprograma
- Solo las estáticas no permiten recursión

**Transición:** Empezamos con la más simple: las variables estáticas.

---

### [F-19] Variables estáticas — concepto

**Tiempo:** 3 min

**Qué decir:**
- Las estáticas tienen su dirección conocida antes de que el programa comience a ejecutar — eso las hace las más eficientes de acceder (la dirección puede estar hardcodeada en el código máquina).
- Cuándo usarlas: constantes del módulo, configuración, cache/estado compartido.
- La restricción de recursión: como hay un solo frame, si la función se llama recursivamente, todas las invocaciones comparten la misma variable estática. Por eso no soportan recursión.
- FORTRAN 77 prohíbe la recursión directamente por esta razón — cada subprograma tiene una única área de datos fija.
- En lenguajes modernos: TypeScript, Python, Java, Go y Kotlin usan stack-dynamic para locales. La estática existe para variables de módulo y `companion object` en Kotlin.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4.3.1, p. 221–258: variables estáticas y su restricción de recursión.
- Gabbrielli & Martini (2023), §5, p. 106–135: "The situation of a language with only static memory allocation is shown in Fig. 5.1. Successive calls to the same procedure share the same memory areas."

**Conceptos clave:**
- Dirección conocida en compilación → acceso eficiente
- Persisten entre llamadas (historia) — útil para cachés, contadores globales
- No soportan recursión efectiva

**Transición:** Veamos las variables estáticas en TypeScript concreto.

---

### [F-20] Variables estáticas — TypeScript

**Tiempo:** 2 min

**Qué decir:**
- El ejemplo de `_cache` con inicialización lazy (`??=`) es un patrón importante: la variable estática existe siempre pero se inicializa la primera vez que se usa.
- `const VERSION = "1.0.0"` — constante estática, dirección fija desde carga.
- `let sesionesActivas = 0` — variable estática mutable, existe todo el tiempo de vida del módulo.
- Traza de ejecución: 1ra llamada crea el Map; 2da+ llamada reutiliza la misma instancia.

**Conceptos clave:**
- Variables de módulo en TypeScript = binding de almacenamiento estático
- Inicialización lazy con `??=` — una sola vez en toda la vida del módulo
- `const` y `let` de módulo son estáticos

**Transición:** Veamos el equivalente en Kotlin: el companion object.

---

### [F-21] Kotlin companion object

**Tiempo:** 2 min

**Qué decir:**
- Kotlin: `companion object` es el equivalente a `static` de Java. Todo lo que está ahí tiene tiempo de vida de toda la ejecución.
- `contadorGlobal` es estática — un binding por toda la JVM. Todas las instancias de `Sesion` comparten la misma celda.
- `Sesion.nueva()` incrementa `contadorGlobal` y crea una nueva `Sesion` con ese id.
- `Sesion.totalSesiones()` devuelve el contador — la misma celda para todos.

**Conceptos clave:**
- `companion object` = espacio estático de la clase en Kotlin
- Una sola celda compartida por todas las instancias
- Persiste durante toda la ejecución de la JVM

**Transición:** Las variables locales son la categoría 2 — viven solo mientras dura el subprograma.

---

### [F-22] Stack-dynamic — concepto

**Tiempo:** 4 min

**Qué decir:**
- Estas son las variables más comunes en TypeScript: cualquier `let` o `const` declarado dentro de una función es stack-dynamic.
- El concepto de "elaboración" de Sebesta es clave: la declaración `let resultado = 0` no reserva memoria en compilación. La reserva se produce cuando la ejecución llega a esa declaración. Para una variable local dentro de una función, la elaboración ocurre en cada llamada a esa función, creando un binding fresco en el frame correspondiente.
- La analogía de la pila de platos: al llamar a una función, se pone un "plato" (frame) en la pila con todas las variables locales. Al retornar, se saca el plato — las variables desaparecen.
- Por qué son la norma: sin gestión manual de memoria, sin basura, sin interferencia entre llamadas.
- Por qué permiten recursión: cada llamada recursiva genera un frame nuevo en la pila. Las variables de diferentes invocaciones coexisten en frames distintos, sin interferencia.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4.3.2, p. 221–258: "Stack-dynamic variables are those whose storage bindings are created when their declaration statements are elaborated. Elaboration refers to the storage allocation and binding process indicated by the declaration, which takes place when execution reaches the code to which the declaration is attached — during run time."

**Conceptos clave:**
- Variables locales de funciones son stack-dynamic en TypeScript
- Elaboración = reserva + vinculación al alcanzar la declaración en runtime
- Cada invocación crea su propio espacio — por eso la recursión funciona
- Se destruyen automáticamente al retornar — no hay leak posible en pila

**Transición:** Veamos el código TypeScript que ilustra esto.

---

### [F-23] Stack-dynamic — código TypeScript

**Tiempo:** 2 min

**Qué decir:**
- El ejemplo de `calcular(n)` muestra dos variables locales: `resultado` y `temp`. Al entrar a la función, se reservan dos celdas en la pila. Al retornar, las celdas se destruyen.
- Las dos llamadas `calcular(5)` y `calcular(7)` son completamente independientes: cada una crea sus propias celdas. La `temp` de `calcular(5)` y la `temp` de `calcular(7)` son celdas diferentes.
- No hay interferencia entre las dos invocaciones.

**Conceptos clave:**
- Cada llamada a una función crea sus propias variables locales en la pila
- Las celdas se destruyen al retornar — no hay leak posible
- Invocaciones independientes = celdas independientes

**Transición:** Veamos el ejemplo canónico: factorial recursivo.

---

### [F-24] Factorial recursivo — código

**Tiempo:** 3 min

**Qué decir:**
- El ejemplo de `factorial` es el argumento central: cada llamada recursiva crea su propio frame con su propia `n`. Si `factorial(3)` llama a `factorial(2)`, cada uno tiene su `n` independiente.
- Recorrer la traza: `factorial(3)` espera a `factorial(2)` que espera a `factorial(1)`. El caso base retorna 1, `factorial(2)` calcula `2*1=2`, `factorial(3)` calcula `3*2=6`.
- Cada llamada tiene su propia copia de `n` en su propio frame — esa es la clave de la recursión.

**Conceptos clave:**
- Frame independiente por invocación → variables locales no se pisan
- La pila crece al llamar, decrece al retornar
- El caso base libera el frame y retorna

**Transición:** Las últimas dos categorías viven en el heap, no en la pila.

---

### [F-25] Categorías 3 y 4 — Heap — concepto

**Tiempo:** 3 min

**Qué decir:**
- Categoría 3 (heap explícita): el programador decide cuándo crear el objeto (`new`) y el sistema decide cuándo liberarlo (GC en TypeScript, drop automático en Rust).
- La cita de Sebesta es precisa: "Las variables dinámicas explícitas del heap son celdas de memoria sin nombre (abstractas) que se asignan y liberan mediante instrucciones explícitas." La característica distintiva es que no tienen nombre propio — se acceden siempre a través de un puntero o referencia.
- Rust: ownership como alternativa al GC. Cada valor tiene un único propietario; el compilador inserta el drop automáticamente al salir del scope. Sin GC, sin leaks.
- Categoría 4 (heap implícita, Python): la más flexible y la más costosa. Cada asignación puede cambiar el tipo, el valor Y la dirección. El intérprete maneja todo.
- Trade-offs: heap explícita = alto control, riesgo de leaks sin GC; heap implícita = bajo control, menor riesgo, máxima flexibilidad.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4.3.3, p. 221–258: "Explicit heap-dynamic variables are nameless (abstract) memory cells that are allocated and deallocated by explicit run-time instructions written by the programmer. These variables, which are allocated from and deallocated to the heap, can only be referenced through pointer or reference variables."
- Sebesta (2019), §5.4.3.4, p. 221–258: "Implicit heap-dynamic variables are bound to heap storage only when they are assigned values. In fact, all their attributes are bound every time they are assigned."
- Gabbrielli & Martini (2023), §14: "Each value in Rust is attached to a variable, which is its exclusive 'owner'. Owners can transfer the ownership of a value to other variables, and other variables can borrow values from their owners."

**Conceptos clave:**
- Heap explícita = `new` crea; GC/ownership libera; objeto sin nombre propio
- Heap implícita = cualquier asignación vincula todos los atributos
- Rust elimina el GC usando ownership — cero overhead de runtime

**Transición:** Veamos el código de categoría 3 en TypeScript y Rust.

---

### [F-26] Categoría 3 — Heap explícita — TypeScript y Rust

**Tiempo:** 2 min

**Qué decir:**
- TypeScript: `new Nodo(42)` crea el objeto en el heap; el GC lo libera automáticamente cuando no hay referencias.
- Al reasignar `cabeza = new Nodo(99)`, el `Nodo(42)` anterior queda sin referencias → el GC lo recolectará. El programador no necesita liberar memoria manualmente.
- Rust: `Box::new(42i32)` asigna en el heap. Al salir del scope, el destructor de `Box` se llama automáticamente — la memoria se libera ahí, sin GC, sin memory leak posible.

**Conceptos clave:**
- TypeScript: `new` + GC — liberación automática
- Rust: `Box::new` + drop automático al salir del scope — sin GC, determinístico
- Ambos son heap explícita — el programador solicita la memoria

**Transición:** Veamos el extremo: categoría 4 en Python.

---

### [F-27] Categoría 4 — Heap implícita — Python

**Tiempo:** 2 min

**Qué decir:**
- En Python, toda asignación puede cambiar tipo, valor y dirección simultáneamente. `x` pasa de `list` a `str` a `int` con reasignaciones.
- El objeto `[1,2,3]` anterior quedó sin referencias — el GC de Python lo recolecta eventualmente.
- Comparar con Cat. 1 o Cat. 2: en esas categorías el tipo es fijo y la dirección no cambia durante la vida de la variable. En Cat. 4 todo cambia en cada asignación.

**Conceptos clave:**
- Python: heap implícita — cada asignación puede cambiar todos los atributos
- El GC recolecta los objetos sin referencias
- Máxima flexibilidad, máximo overhead

**Transición:** Ahora pasamos al ámbito — ¿dónde en el código es visible el nombre de la variable?

---

## BLOQUE 5 — Ámbito (18 min)
---

### [F-28] Ámbito estático — concepto y algoritmo

**Tiempo:** 3 min

**Qué decir:**
- El ámbito define **visibilidad del nombre** — no es lo mismo que tiempo de vida. Una variable puede existir (estar en memoria) pero estar fuera de ámbito (nombre invisible).
- El algoritmo de resolución es lo que el compilador hace cada vez que ve un identificador: buscar local → padre → abuelo → hasta el módulo raíz. Si no lo encuentra, error de compilación.
- "Estático" significa que este recorrido se hace en compilación, no en runtime. El compilador ya sabe qué variable es cada nombre antes de ejecutar.
- El ámbito comienza en la declaración: `console.log(x)` antes de `let x = 10` da error. TypeScript recomienda declarar cerca de donde se usa.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.5, p. 221–258: ámbito estático y algoritmo de resolución.
- Gabbrielli & Martini (2023), §4.3, p. 083–105: "A variable becomes visible at the declaration, but the storage binding (and initialization, if it is specified in the declaration) occurs when the function or method begins execution."

**Conceptos clave:**
- Ámbito ≠ tiempo de vida — visibilidad del nombre vs. existencia en memoria
- El algoritmo sube por la cadena estática hasta encontrar el nombre o fallar en compilación
- "Estático" = resuelto en compilación, no en ejecución
- El ámbito comienza en la declaración, no al principio del bloque

**Transición:** Veamos el algoritmo en TypeScript concreto.

---

### [F-29] Ámbito estático — TypeScript

**Tiempo:** 4 min

**Qué decir:**
- Recorrer el código línea por línea: `interna()` puede ver `x` (módulo), `y` (externa), `z` (propio). `externa()` puede ver `x` y `y` pero no `z`. El módulo no puede ver ninguna variable local de ninguna función.
- El comentario `// ❌ z no visible aquí — error de compilación` es el punto pedagógico central: TypeScript sabe en compilación que `z` no existe en ese scope.
- Recorrer la resolución de cada `console.log` paso a paso: ¿x en nivel 2? No → ¿nivel 1? No → ¿nivel 0? Sí → x = 10. El algoritmo de búsqueda hacia afuera.
- El "problema del ámbito global": las variables de módulo son visibles en todos los bloques. Eso es un arma de doble filo — cómodo pero peligroso si se usan como canal de comunicación implícito entre funciones.

**Conceptos clave:**
- La visibilidad sigue la estructura léxica del código — no la secuencia de ejecución
- Variables de módulo visibles en todo el código del módulo — cuidado con el abuso
- El compilador valida todos los usos en compilación

**Transición:** ¿Y si la visibilidad dependiera de quién llama en lugar de dónde está escrito el código?

---

### [F-30] Ámbito dinámico — comparativa

**Tiempo:** 4 min

**Qué decir:**
- La diferencia conceptual: en estático la cadena que se recorre es la cadena léxica (estructura del código); en dinámico es la cadena de llamadas activas en runtime.
- La definición formal de Gabbrielli: "la asociación válida para un nombre X, en cualquier punto P, es la asociación más reciente (en el sentido temporal) creada para X que todavía se encuentra activa cuando el flujo de control llega a P."
- La implementación es sencilla: recorrer la pila de activación hacia atrás hasta encontrar un frame que declare `x`.
- Los tres problemas de Sebesta: (1) imposibilidad de verificación estática de tipos, (2) código difícil de leer, (3) accesos más costosos.
- El ejemplo de `this` en JavaScript es el más relevante: `this` se resuelve en tiempo de llamada (dinámico). Por eso las arrow functions lo capturan léxicamente.
- Lenguajes con ámbito dinámico: Emacs Lisp (original), Perl `local`, shells POSIX. Lenguajes con estático: TypeScript, Python, Go, Rust, Java.

**Trazabilidad bibliográfica:**
- Gabbrielli & Martini (2023), §4.3, p. 083–105: "According to the rule of dynamic scope, the valid association for a name X, at any point P of a program, is the most recent (in the temporal sense) association created for X which is still active when the control flow arrives at P."
- Gabbrielli & Martini (2023), §4.3, p. 106–135: "Conceptually, the implementation of the dynamic scope rule is much simpler than the one for static scope."
- Sebesta (2019), §5.5.4, p. 221–258: problemas del ámbito dinámico.

**Conceptos clave:**
- Dinámico = cadena de llamadas en runtime determina visibilidad
- `this` en JavaScript/TypeScript tiene semántica dinámica — arrow functions lo fijan léxicamente
- Verificación de tipos para variables no-locales es imposible con ámbito dinámico
- Más difícil de leer — hay que rastrear quién llamó a quién

**Transición:** Veamos el ejemplo de `this` en JavaScript concreto.

---

### [F-31] Ámbito dinámico — `this` en JavaScript

**Tiempo:** 3 min

**Qué decir:**
- El ejemplo de `Timer` muestra los dos casos: función regular vs arrow function.
- `startConFunctionRegular`: `this` dentro de `setTimeout(function() {...})` NO es la instancia `Timer` — lo perdió `setTimeout`. En strict mode: `this === undefined`. Resultado: `console.log(this?.delay)` → `undefined`.
- `startConArrow`: `this` dentro de `setTimeout(() => {...})` ES la instancia `Timer` — garantizado por el ámbito léxico. El compilador sabe en compilación qué es `this` dentro de la arrow. Resultado: `console.log(this.delay)` → `1000`.
- Este es el ejemplo más concreto de cómo el ámbito dinámico causa bugs y cómo la arrow function es la solución léxica.

**Conceptos clave:**
- `this` en función regular = dinámico (depende del contexto de llamada)
- `this` en arrow function = léxico (capturado en compilación)
- `setTimeout` pierde el `this` de la instancia — arrow function lo preserva

**Transición:** Un fenómeno interesante del ámbito estático son los "agujeros de ámbito" — shadowing.

---

### [F-32] Scope holes — shadowing — concepto

**Tiempo:** 2 min

**Qué decir:**
- El shadowing ocurre cuando una variable local tiene el mismo nombre que una del bloque exterior. La exterior queda "tapada" — sigue existiendo pero su nombre no es visible.
- El mecanismo: el algoritmo de resolución siempre prefiere el binding más local. Si encuentra el nombre en el bloque actual, no continúa buscando en los padres.
- Por qué es problemático: el código parece estar usando la variable exterior pero en realidad usa la interior. Los linters alertan sobre shadowing porque es una fuente frecuente de bugs sutiles.
- Herramientas: `@typescript-eslint/no-shadow` produce advertencia. TypeScript por sí solo no bloquea el shadowing — requiere ESLint.

**Conceptos clave:**
- Scope hole: la variable exterior existe pero su nombre es invisible en el bloque interior
- El algoritmo prefiere el binding más local
- Shadowing silencioso = bug difícil de rastrear — configurar ESLint `no-shadow`

**Transición:** Veamos el código de shadowing.

---

### [F-33] Shadowing — código

**Tiempo:** 2 min

**Qué decir:**
- El ejemplo es sutil a propósito: dentro del `for`, el `x` que se imprime es el interior (`item * 2`). Después del `for`, el `x` que se imprime es el exterior (`10`). El mismo nombre, dos variables distintas, sin advertencia de TypeScript.
- Salida: `20, 40, 60, 10` — el `x` del módulo nunca fue modificado.
- Los linters están ahí para esto: `@typescript-eslint/no-shadow` detecta y advierte.

**Conceptos clave:**
- Dos variables con el mismo nombre coexisten en scopes distintos
- El `x` interior oculta al exterior dentro del `for`
- ESLint `no-shadow` detecta el patrón

**Transición:** Cerremos el bloque de conceptos con el entorno de referencia y la inicialización.

---

## BLOQUE 6 — Entorno de Referencia, Constantes e Inicialización (10 min)
---

### [F-34] Entorno de referencia

**Tiempo:** 3 min

**Qué decir:**
- El entorno de referencia es la "foto" de todo lo que es visible en un punto del programa. Si uno mentalmente enumera todos los nombres válidos en una sentencia dada — eso es el entorno de referencia.
- Cambia a lo largo del programa: dentro de una función el entorno incluye los parámetros y las variables locales; fuera no.
- Componentes en TypeScript: variables locales, parámetros, variables de funciones externas (capturadas por closure), variables del módulo, identificadores globales del runtime.
- Relación con closures: una closure "congela" el entorno de referencia en el momento en que se crea la función. El entorno capturado puede incluir variables que ya salieron del stack pero siguen vivas por la closure. Esto se estudia en Tema 09.2.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.7, p. 221–258: "The referencing environment of a statement is the collection of all variables that are visible in the statement. The referencing environment of a statement in a static-scoped language is the variables declared in its local scope plus the collection of all variables of its ancestor scopes that are visible."

**Conceptos clave:**
- Entorno de referencia = conjunto de identificadores visibles en un punto dado
- Cambia al entrar/salir de bloques y funciones
- Las closures "congelan" el entorno — se ve en Tema 09.2

**Transición:** Veamos las constantes — un tipo especial de variable con binding de valor inmutable.

---

### [F-35] Constantes — concepto

**Tiempo:** 2 min

**Qué decir:**
- Una constante es un identificador cuyo valor se fija en un momento determinado y el lenguaje prohíbe modificarlo después.
- Cuándo se fija el binding de valor: en compilación (`const PI = 3.14159`), en tiempo de carga (`const VERSION = pkg.version`), o en ejecución (`val limite = calcularLimite()` en Kotlin).
- `const` en TypeScript: para primitivos hace inmutable el valor; para objetos hace inmutable la referencia — el objeto interno puede mutar. Para inmutabilidad profunda: `Object.freeze()` o `Readonly<T>`.
- Por qué importan: representan un binding de R-value que no puede reasignarse. El L-value sigue existiendo. El compilador puede optimizar accesos a constantes.

**Conceptos clave:**
- Constante = binding de valor inmutable
- `const` en TypeScript = inmutabilidad de referencia, no de contenido
- Para inmutabilidad profunda: `Object.freeze()` o `Readonly<T>`

**Transición:** Veamos el código de constantes en TypeScript.

---

### [F-36] Constantes — código TypeScript

**Tiempo:** 2 min

**Qué decir:**
- Caso 1: `const PI = 3.14159` — primitivo, inmutable el valor. `PI = 2.71` → error.
- Caso 2: `const CONFIG = { debug: false, maxRetries: 3 }` — objeto, inmutable la referencia. `CONFIG.debug = true` es válido — el objeto es mutable. `CONFIG = { debug: true }` → error.
- Caso 3: `Object.freeze({ debug: false })` — inmutabilidad profunda. En JavaScript silencioso; en TypeScript strict, error de tipo.
- Patrón recomendado: `Object.freeze({...} as const)` para objetos de configuración inmutables.

**Conceptos clave:**
- `const` primitivo = inmutable el valor
- `const` objeto = inmutable la referencia, mutable el contenido
- `Object.freeze()` + `as const` = inmutabilidad profunda

**Transición:** ¿Y qué pasa antes de asignar un valor? ¿Qué hay en la variable?

---

### [F-37] Inicialización — comparativa de lenguajes

**Tiempo:** 2 min

**Qué decir:**
- El caso C es el más dramático: las variables locales no inicializadas contienen basura (lo que quedó en esa dirección de la invocación anterior). Esto genera bugs extremadamente difíciles de reproducir.
- Java: campos → valores por defecto (0, false, null); locales → error de compilación.
- TypeScript strict elimina el problema de raíz: si intentás usar una variable antes de asignarle un valor, error de compilación. No hay basura — hay error en desarrollo, no en producción.
- Python en el medio: no hay "basura" pero hay `NameError` en runtime si usás un nombre no definido. Mejor que C, pero más tardío que TypeScript.
- Go tomó la decisión opuesta a C: zero values garantizados para todo. Cero configuración, cero sorpresas. Es una decisión de diseño explícita del lenguaje.
- Rust: error de compilación — el compilador exige inicialización antes del primer uso.

**Trazabilidad bibliográfica:**
- Sebesta (2019), §5.4.3, p. 221–258: comportamientos de inicialización por lenguaje.

**Conceptos clave:**
- C: variables locales no inicializadas = basura (undefined behavior)
- TypeScript strict: error de compilación si se usa antes de asignar
- Go: zero values = `0`, `""`, `false`, `nil` — sin basura por diseño
- Rust: error de compilación — inicialización obligatoria

**Transición:** Veamos el código de TypeScript strict.

---

### [F-38] Inicialización — TypeScript strict code

**Tiempo:** 1 min

**Qué decir:**
- `let n: number; console.log(n)` → Error TS2454: Variable 'n' used before being assigned.
- El compilador analiza el flujo y detecta que `n` puede no estar inicializada. Esto es análisis de flujo de tipos — una característica de TypeScript strict mode.

**Conceptos clave:**
- TypeScript strict: análisis de flujo detecta uso antes de asignación
- Error TS2454 — error de compilación, no de runtime

**Transición:** Arrancamos el bloque final — cómo se conecta todo esto con el código generado por IA.

---

## BLOQUE 7 — IA y Variables (12 min)
---

### [F-39] La IA comete errores de scope

**Tiempo:** 2 min

**Qué decir:**
- Introducir el tema: los modelos de lenguaje generan código que compila y a veces hasta pasa los tests, pero con patrones de scope que serían señalados por cualquier senior de TypeScript.
- ¿Por qué? Los modelos aprendieron de código JavaScript pre-ES6 donde `var` era la única opción. Ese código existe en millones de repositorios que el modelo procesó.
- En JavaScript no-strict, muchos de estos errores no generan excepciones — el código "funciona" aunque sea incorrecto.
- Los tres patrones que vamos a ver son detectables y prevenibles — tanto por el programador que revisa como por un prompt bien diseñado.

**Conceptos clave:**
- El código generado por IA puede ser correcto sintácticamente pero incorrecto semánticamente en scope
- Los tres patrones se pueden prevenir con revisión activa o con prompts explícitos
- La raíz está en el corpus pre-ES6 con `var`, globales y shadowing

**Transición:** Patrón uno: `var` hoisting.

---

### [F-40] Patrón 1 — `var` hoisting — concepto

**Tiempo:** 2 min

**Qué decir:**
- Mostrar la tabla var vs let/const. `var` tiene ámbito de función, no de bloque. Se "eleva" (hoisted) al inicio de la función — la declaración sube, la inicialización permanece en su lugar.
- Temporal Dead Zone (TDZ): con `let`/`const`, la variable existe en el scope pero no puede usarse hasta que se alcanza su declaración. Usar la variable antes lanza `ReferenceError` — explícito y localizable.
- Con `var` no hay TDZ: cualquier uso antes de la asignación da `undefined` en silencio.

**Conceptos clave:**
- `var` = hoisting de función; inicialización permanece → `undefined` inesperado
- `let`/`const` = Temporal Dead Zone → error explícito y temprano
- Regla: nunca usar `var` en TypeScript moderno

**Transición:** Veamos el código.

---

### [F-41] Patrón 1 — `var` hoisting — código

**Tiempo:** 2 min

**Qué decir:**
- Mostrar el código y preguntar: "¿qué imprime `console.log(resultado)`?" — Esperar respuestas. La respuesta intuitiva es "ok" si `activo = true` o error si `activo = false`. La respuesta real es `undefined` si `activo = false` (no lanza error) o `"ok"` si `activo = true`.
- `var resultado` fue elevada al inicio de `procesar()` — equivale a `var resultado;` (undefined) al principio, y `if (activo) { resultado = "ok"; }`.
- Con `let`: `console.log(resultado)` fuera del `if` da `ReferenceError` — el error aparece exactamente donde está el problema.

**Conceptos clave:**
- `var` se eleva al inicio de la función — `undefined` silencioso
- `let` da `ReferenceError` explícito fuera del bloque
- El error silencioso puede ocurrir lejos de la causa real

**Transición:** El segundo patrón es más sutil — efectos secundarios ocultos en variables globales.

---

### [F-42] Patrón 2 — Variable global silenciosa — concepto

**Tiempo:** 2 min

**Qué decir:**
- La firma de `acumular(n: number)` promete que la función solo necesita `n`. Mentira — también depende de `total`, que no aparece en la firma.
- Esto hace que la función no sea pura: su resultado depende del estado externo y su orden de llamada importa. Difícil de testear, difícil de razonar.
- Señales de alerta: función que modifica una variable declarada fuera de su scope; función cuyo resultado varía según qué otras funciones se llamaron antes; variable `total`, `contador`, `estado` declarada en el módulo.
- La solución: convertir la variable externa en parámetro hace la dependencia visible en la firma. La función se vuelve predecible: mismos parámetros → mismo resultado.

**Conceptos clave:**
- Dependencia implícita en variable global = efecto secundario oculto
- Función pura: el resultado depende exclusivamente de los parámetros
- Señal de alerta: la función modifica algo no declarado en su firma

**Transición:** Veamos el código.

---

### [F-43] Patrón 2 — Variable global silenciosa — código

**Tiempo:** 2 min

**Qué decir:**
- `let total = 0` es una variable global oculta — no aparece en la firma de `acumular`.
- `acumular(5)` → total = 5; `acumular(3)` → total = 8; `acumular(5)` → total = 13. Mismo argumento (5), resultado diferente (5 vs 13) — no es predecible.
- La versión correcta `acumularPuro(total, n)` recibe `total` como parámetro — todas las dependencias son visibles. Mismos argumentos → siempre el mismo resultado.
- Predecible, testeable de forma aislada, sin estado oculto.

**Conceptos clave:**
- Variable global mutable = estado oculto entre llamadas
- Función pura: mismos argumentos → mismo resultado, sin efectos secundarios
- Pasar el estado como parámetro hace la dependencia visible

**Transición:** El tercer patrón: el nombre correcto apunta a la variable equivocada.

---

### [F-44] Patrón 3 — Shadowing inesperado — código

**Tiempo:** 2 min

**Qué decir:**
- Este ejemplo es más complicado: la intención del programador es filtrar con `limite = 100`, pero la redeclaración dentro de `validar` lo sombrea con `items.length`.
- La IA que generó este código puede haberlo hecho "por simetría" — usa `limite` como nombre genérico sin ver el conflicto con el módulo exterior.
- El `filter` usa el `limite` del bloque más cercano — `items.length`. Si `items.length < 100`, los resultados pueden parecer correctos, lo que hace el bug difícil de detectar en testing.
- La versión correcta `validarSinShadow` usa `valorLimite` como parámetro y `cantidadItems` como nombre local — sin shadowing, intención explícita.

**Conceptos clave:**
- Shadowing: el nombre correcto resuelve a la variable equivocada
- Los tests pueden pasar con datos que no revelan el bug
- Usar nombres diferentes para variables locales y exteriores

**Transición:** Ahora van a practicar los tres patrones al mismo tiempo.

---

## BLOQUE 8 — Actividad y Cierre (6 min)
---

### [F-45] Actividad — tres patrones mezclados

**Tiempo:** 3 min (2 silencio + 1 respuesta grupal)

**Qué decir:**
- Proyectar el código y dar 2 minutos de silencio. No agregar contexto — dejar que trabajen solos.
- Después de los 2 minutos, preguntar: "¿Cuántos encontraron?" y luego "¿Qué patrón es el primero?" — esperar respuestas antes de revelar.
- **Respuesta esperada:**
  - `var total = 0` → Patrón 2 (global mutable que acumula estado entre llamadas)
  - `var resultado = items[0] * 2` → Patrón 1 (hoisting — `console.log(resultado)` puede ser `undefined`)
  - `const limite = item` dentro del `for` → Patrón 3 (shadowing — el `filter` usa `item`, no `100`)

**Conceptos clave:** [Los tres patrones identificados — ver slides anteriores]

**Preguntas anticipadas:**
- *"¿TypeScript no detecta esto automáticamente?"* → `var resultado` sí con strict (no usada antes de asignación). `const limite` el shadowing solo con ESLint `no-shadow`. `var total` como global es válido en TypeScript — no hay error automático.

**Transición:** ¿Cómo pedirle a la IA que no genere estos patrones?

---

### [F-46] Prompt seguro para variables en TypeScript

**Tiempo:** 1 min

**Qué decir:**
- Mostrar el prompt como si fuera una directiva técnica — no una sugerencia vaga.
- Cada línea del prompt tiene una razón: `strict mode` activa el compilador más estricto; `let/const` elimina `var`; "sin variables globales" elimina el patrón 2; "tipos declarados" permite que el compilador detecte más errores.
- Este prompt no garantiza código perfecto pero reduce significativamente los tres patrones que acabamos de ver.

**Conceptos clave:**
- Los prompts explícitos y técnicos producen mejor código que los genéricos
- "TypeScript strict" y "sin var" son restricciones que el modelo puede cumplir
- Las restricciones también actúan como documentación técnica del proyecto

**Transición:** Cerramos la clase.

---

### [F-47] Cierre — tres ideas para llevarse

**Tiempo:** 2 min

**Qué decir:**
- Leer las tres ideas en voz alta — no explicarlas, solo enunciarlas. La clase ya las desarrolló.
- Anunciar Tema 09.2: "La próxima clase tomamos estas variables y las hacemos más complejas — aliases (cuando dos nombres apuntan a la misma dirección), closures (cuando una función captura variables de su ámbito léxico) y GC (cómo el sistema libera el heap de categoría 3)."
- Anunciar el TP — disponible en el aula virtual.
- Si queda tiempo: una pregunta abierta final — "¿En qué categoría de almacenamiento viven los parámetros de una función en TypeScript?" (Respuesta: stack-dynamic, igual que las variables locales).

**Resumen de la clase:**
1. La variable es una 5-tupla — nombre, dirección, tipo, L-value, R-value
2. Binding ocurre en 6 momentos — cuanto antes, más eficiente y menos flexible
3. El ámbito estático es predecible — se resuelve en compilación, no en ejecución

**Próxima clase:** Tema 09.2 — Aliases, Closures, GC y Tipos

**TP:** Disponible en el aula virtual.

---

## Resumen de tiempos

| Bloque | Filminas | Minutos |
|---|---|---|
| 1 — Variable como Abstracción | F-00 a F-07 | 20 |
| 2 — Binding | F-08 a F-10 | 12 |
| 3 — Binding de Tipos | F-11 a F-17 | 16 |
| 4 — Binding de Almacenamiento | F-18 a F-27 | 26 |
| 5 — Ámbito | F-28 a F-33 | 18 |
| 6 — Entorno, Constantes, Inicialización | F-34 a F-38 | 10 |
| 7 — IA y Variables | F-39 a F-44 | 12 |
| 8 — Actividad y Cierre | F-45 a F-47 | 6 |
| **Total** | **48 filminas** | **120 min** ✅ |