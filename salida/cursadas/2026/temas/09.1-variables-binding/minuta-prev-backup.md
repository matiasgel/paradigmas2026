# Minuta — Tema 09.1: Variables, Binding y Ámbito

**Materia:** Paradigmas y Lenguajes de Programación 2026
**Duración:** 120 min (1 clase)
**Agente:** Dr. Roberto ✍️ — Class Writer · 2026-05-14
**Estado:** 🔲 Borrador — pendiente de revisión docente

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

## BLOQUE 1 — Variable como Abstracción (22 min)

---

### [F-01] Von Neumann: el origen de la variable

**Tiempo estimado:** 10 min

**Qué decir:**
- Arrancar con la pregunta: "¿qué es exactamente una variable?" — dejar 15 segundos de silencio. La respuesta habitual es "un nombre que guarda un valor". Está bien, pero es incompleta.
- Mostrar el diagrama Von Neumann: la memoria como celdas numeradas y el procesador que las lee y escribe. El lenguaje es una capa que le pone nombre a las celdas y esconde las direcciones.
- La tabla de abstracción es el núcleo de la slide: celda → variable, dirección → nombre, modificación destructiva → asignación. Estos tres mapeos son la justificación de por qué existen los lenguajes de alto nivel.
- Remarcar: la sentencia de asignación destruye el valor previo de la celda — por eso se llama "modificación destructiva". En lenguajes funcionales puros esto no existe.

**Conceptos clave:**
- La variable abstrae la celda de memoria Von Neumann
- Nombre ≠ dirección ≠ valor — son tres cosas distintas
- La asignación es una operación destructiva sobre una celda

**Preguntas anticipadas:**
- *"¿Una variable en Python es lo mismo?"* → Sí, el modelo es el mismo aunque Python oculta más cosas. Lo vamos a ver en F-04.
- *"¿Qué es una variable anónima?"* → Un objeto creado con `new` sin asignar a ningún nombre — tiene dirección y valor pero no nombre. Buena pregunta, responder brevemente y seguir.

**Transición:** Bien, sabemos que la variable abstrae una celda. Ahora necesitamos precisar qué atributos tiene esa abstracción. Porque no es solo nombre y valor — hay seis atributos formales.

---

### [F-02] Los seis atributos de una variable

**Tiempo estimado:** 7 min

**Qué decir:**
- Recorrer la tabla fila por fila. No leer — explicar cada atributo con una oración.
- Énfasis en que **tiempo de vida** y **ámbito** son cosas distintas: el tiempo de vida es sobre cuándo la variable existe en memoria; el ámbito es sobre cuándo su nombre es visible. Una variable puede existir pero estar fuera de ámbito.
- La 5-tupla es una simplificación que agrupa tiempo de vida con ámbito. Sebesta trabaja con los seis por separado — es más preciso.
- El nombre puede no existir: objetos creados con `new Nodo()` sin asignar tienen L-value y R-value pero no nombre.

**Conceptos clave:**
- L-value = dirección; R-value = contenido
- Tiempo de vida ≠ ámbito — son atributos independientes
- La 5-tupla es una simplificación pedagógica de seis atributos reales

**Preguntas anticipadas:**
- *"¿Qué es el L-value exactamente?"* → La próxima slide lo muestra en código, anticipar que lo vamos a ver.

**Transición:** Ahora veamos L-value y R-value en acción con código concreto.

---

### [F-03] L-value y R-value en acción

**Tiempo estimado:** 3 min

**Qué decir:**
- En `x = y`: cuando `x` aparece a la izquierda del `=`, denota la dirección donde escribir (L-value). Cuando `y` aparece a la derecha, denota el contenido a leer (R-value). El mismo nombre puede ser L-value o R-value según su posición.
- Python con `id()` sirve para mostrar que el L-value existe aunque TypeScript lo oculte — el `id()` de Python es la dirección real del objeto en heap.
- No profundizar en el ejemplo de Python — es solo para mostrar que la dirección existe aunque los lenguajes la escondan.

**Conceptos clave:**
- L-value vs R-value según la posición en la sentencia de asignación
- Los lenguajes de alto nivel ocultan el L-value al programador (excepto C/Rust/Go con punteros)

**Preguntas anticipadas:**
- *"¿En TypeScript nunca vemos el L-value?"* → Correcto — TypeScript abstrae la dirección. Rust y Go la hacen explícita de forma segura. C también pero de forma insegura.

**Transición:** Veamos ahora estos mismos conceptos en cuatro lenguajes distintos — mismo concepto, cuatro perspectivas.

---

### [F-04] La 5-tupla en cuatro lenguajes

**Tiempo estimado:** 2 min

**Qué decir:**
- Pasar rápido — es una confirmación visual de que la 5-tupla aplica a todos los lenguajes, no solo a TypeScript.
- Destacar Go: los zero values son una decisión de diseño que elimina la clase de errores de "usar variable no inicializada" que tiene C.
- Rust muestra explícitamente el L-value como puntero raw — esto es seguro en Rust porque el ownership garantiza que la dirección es válida.

**Conceptos clave:**
- La 5-tupla es universal — varía cómo se expone, no si existe
- Go zero values: `0`, `""`, `false`, `nil` — sin basura por diseño

**Transición:** Ahora que entendemos qué es la variable, pasamos a entender cuándo se establecen sus atributos. Eso es el binding.

---

## BLOQUE 2 — Binding: el momento de la vinculación (15 min)

---

### [F-05] ¿Qué es el Binding?

**Tiempo estimado:** 5 min

**Qué decir:**
- Definición precisa: binding = la asociación entre una entidad y uno de sus atributos, establecida en un momento determinado. La clave es "momento determinado" — eso es lo que distingue los lenguajes.
- El diagrama (flecha entidad → atributo) es simple pero poderoso: cualquier par entidad-atributo que el lenguaje necesita establecer es un binding. El tipo de una variable es un binding. El significado del operador `+` es un binding. La dirección de memoria de una variable es un binding.
- Tradeoff central: binding temprano → eficiente (la dirección está en el ejecutable, no hay que computarla en runtime); binding tardío → flexible (podés cambiar qué hace un operador, cambiar el tipo de una variable).

**Conceptos clave:**
- Binding = asociación entidad ↔ atributo en un momento
- Binding temprano ↔ eficiencia; binding tardío ↔ flexibilidad
- No es solo sobre variables — aplica a operadores, literales, subprogramas

**Preguntas anticipadas:**
- *"¿El binding siempre es para variables?"* → No — el significado de `*` como multiplicación es un binding establecido en tiempo de diseño del lenguaje. Lo vemos en la próxima tabla.

**Transición:** ¿En cuántos momentos puede ocurrir el binding? Exactamente seis.

---

### [F-06] Los 6 tiempos de binding

**Tiempo estimado:** 5 min

**Qué decir:**
- Recorrer la tabla de arriba a abajo — son los 6 momentos en orden cronológico.
- El "tiempo de diseño" es el menos obvio: cuando los diseñadores del lenguaje deciden que `*` significa multiplicación, están haciendo un binding. No está en el código del programador — está en la especificación del lenguaje.
- "Tiempo de implementación": el rango de `number` en TypeScript (IEEE 754 float64) es una decisión de los implementadores del compilador, no del diseñador del lenguaje ni del programador.
- Hacer énfasis en la distinción compilación vs. ejecución: el tipo se vincula en compilación (estático), pero el valor se vincula en ejecución. Esto va a ser clave para los próximos bloques.

**Conceptos clave:**
- Los 6 momentos en orden: diseño → implementación → compilación → linkeo → carga → ejecución
- Tipo: binding en compilación (TypeScript) vs. en ejecución (Python)
- Valor: siempre se vincula en ejecución

**Preguntas anticipadas:**
- *"¿El linkeo aplica a TypeScript?"* → Sí — cuando TypeScript llama a `console.log`, en el bundle final eso resuelve a código en el runtime de Node.js o el browser. El mecanismo exacto varía pero el concepto aplica.

**Transición:** Veamos todos los tiempos en un solo fragmento de código para solidificar la idea.

---

### [F-07] Los 6 tiempos en un fragmento TypeScript

**Tiempo estimado:** 5 min

**Qué decir:**
- Mostrar el fragmento dos líneas. Luego mostrar los comentarios de a uno — preguntar a la clase antes de revelar cada uno qué binding ocurre ahí.
- La pregunta "¿cuándo se vincula el tipo de `count`?" tiene respuesta en compilación (TypeScript lo infiere o verifica cuando transpila). La pregunta "¿cuándo se vincula el valor de `count`?" tiene respuesta en ejecución (cuando se ejecuta la línea `count = count + 5`).
- Este ejercicio de dos minutos fija la distinción más importante del bloque.

**Conceptos clave:**
- El mismo fragmento involucra bindings en múltiples momentos simultáneamente
- Tipo → compilación; valor → ejecución; rango del tipo → implementación

**Transición:** Ahora entramos al binding de tipos en detalle — hay dos dimensiones independientes que hay que mantener separadas.

---

## BLOQUE 3 — Binding de Tipos (12 min)

---

### [F-08] Cuatro dimensiones del binding de tipos

**Tiempo estimado:** 5 min

**Qué decir:**
- Énfasis principal: estático/dinámico y fuerte/débil son **dimensiones ortogonales** — no son lo mismo, no son opuestos. Un lenguaje puede ser cualquier combinación de los cuatro.
- Ejemplos de combinaciones: TypeScript = estático + fuerte. Python = dinámico + fuerte. JavaScript = dinámico + débil. C = estático + débil. Haskell/Rust = estático + fuerte (más extremo que TypeScript).
- Preguntar a la clase: "¿Qué ventaja tiene el binding estático de tipos?" — la respuesta es detección de errores en compilación antes de ejecutar.

**Conceptos clave:**
- Estático/dinámico = cuándo se establece el tipo (compilación vs. ejecución)
- Fuerte/débil = qué tan estricto es el chequeo (sin/con coerciones implícitas arbitrarias)
- Las dos dimensiones son independientes — cualquier combinación existe en lenguajes reales

**Preguntas anticipadas:**
- *"¿TypeScript es fuerte o débil?"* → Fuerte en modo strict. Con `any` se vuelve débil — por eso `any` es desaconsejado.

**Transición:** Veamos la inferencia — que es estático pero sin declaración explícita.

---

### [F-09] Inferencia de tipos

**Tiempo estimado:** 3 min

**Qué decir:**
- La inferencia es binding estático sin declaración explícita — el compilador lo deduce del contexto. No es binding dinámico — sigue ocurriendo en compilación.
- El ejemplo de TypeScript muestra inferencia bidireccional: `items` se infiere como `number[]` por el literal; `x` en el `forEach` se infiere como `number` por el contexto del array.
- El contraste con Python es importante: en Python el tipo cambia en runtime — no es inferencia, es binding dinámico real.

**Conceptos clave:**
- Inferencia = binding estático sin declaración explícita del programador
- No confundir inferencia con binding dinámico

**Transición:** Veamos ahora la diferencia fuerte/débil con coerciones concretas.

---

### [F-10] Coerciones: fuerte vs. débil en código

**Tiempo estimado:** 4 min

**Qué decir:**
- El ejemplo de JavaScript es el más impactante: `"5" + 3 = "53"` pero `"5" - 3 = 2`. El tipo de coerción depende del operador — no hay regla consistente. Eso es tipado débil.
- TypeScript strict corta esto en compilación — el error es claro y temprano.
- Python es fuerte y dinámico: el tipo es flexible pero las operaciones incompatibles siempre dan excepción explícita, nunca resultado silencioso incorrecto.
- Preguntar: "¿Preferirían que el error salga en compilación o en runtime?" — la respuesta obvia es compilación, pero hay contextos (scripting rápido, prototipado) donde el dinamismo tiene valor.

**Conceptos clave:**
- Débil ≠ dinámico — JavaScript es dinámico Y débil; Python es dinámico Y fuerte
- Fuerte = errores explícitos; débil = resultados silenciosos potencialmente incorrectos

**Transición:** Ahora que entendemos el binding de tipos, pasamos al binding de almacenamiento — ¿cuándo y dónde vive la variable en memoria?

---

## BLOQUE 4 — Binding de Almacenamiento (18 min)

---

### [F-11] Las 4 categorías de variables

**Tiempo estimado:** 3 min

**Qué decir:**
- Presentar la tabla como el mapa del bloque — van a ver las cuatro categorías en detalle. La tabla es una vista rápida para orientarse.
- La columna "Permite recursión" es clave: las estáticas no la permiten porque hay un solo frame para toda la vida del programa. Las demás sí.
- No explicar cada categoría aquí — solo dar el panorama. Las slides siguientes desarrollan cada una.

**Conceptos clave:**
- Las 4 categorías se distinguen por cuándo ocurre el binding de almacenamiento
- Estáticas = tiempo de vida = toda la ejecución; stack-dynamic = activación del subprograma

**Transición:** Empezamos con la más simple: las variables estáticas.

---

### [F-12] Categoría 1 — Variables estáticas

**Tiempo estimado:** 4 min

**Qué decir:**
- Las estáticas tienen su dirección conocida antes de que el programa comience a ejecutar — eso las hace las más eficientes de acceder (la dirección puede estar hardcodeada en el código máquina).
- El ejemplo de `_cache` con inicialización lazy (`??=`) es un patrón importante: la variable estática existe siempre pero se inicializa la primera vez que se usa.
- Kotlin: `companion object` es el equivalente a `static` de Java. Todo lo que está ahí tiene tiempo de vida de toda la ejecución.
- Consecuencia importante: como hay un solo frame, si la función se llama recursivamente, todas las invocaciones comparten la misma variable estática. Por eso no soportan recursión.

**Conceptos clave:**
- Dirección conocida en compilación → acceso eficiente
- Persisten entre llamadas (historia) — útil para cachés, contadores globales
- No soportan recursión efectiva

**Transición:** Las variables locales son la categoría 2 — viven solo mientras dura el subprograma.

---

### [F-13] Categoría 2 — Stack-dynamic

**Tiempo estimado:** 4 min

**Qué decir:**
- Estas son las variables más comunes en TypeScript: cualquier `let` o `const` declarado dentro de una función es stack-dynamic.
- La analogía de la pila de platos: al llamar a una función, se pone un "plato" (frame) en la pila con todas las variables locales. Al retornar, se saca el plato — las variables desaparecen.
- El ejemplo de `factorial` es el argumento central: cada llamada recursiva crea su propio frame con su propia `n`. Si `factorial(3)` llama a `factorial(2)`, cada uno tiene su `n` independiente.

**Conceptos clave:**
- Variables locales de funciones son stack-dynamic en TypeScript
- Cada invocación crea su propio espacio — por eso la recursión funciona
- Se destruyen automáticamente al retornar — no hay leak posible en pila

**Transición:** Veamos el frame independiente gráficamente.

---

### [F-14] Frame independiente → recursión posible

**Tiempo estimado:** 3 min

**Qué decir:**
- El diagrama es simple — tres frames apilados, cada uno con su propia `n`. Lo importante es que cuando `factorial(3)` llama a `factorial(2)`, el frame de `factorial(3)` sigue en la pila, con su `n = 3` intacta.
- Cuando `factorial(2)` retorna, su frame desaparece y `factorial(3)` puede continuar con su `n = 3`.
- Mención explícita de que los detalles internos (static link, dynamic link) se estudian en Tema 13. No profundizar — la idea que importa hoy es "frame independiente = recursión posible".

**Conceptos clave:**
- Frame independiente por invocación → variables locales no se pisam
- La pila crece al llamar, decrece al retornar

**Transición:** Las últimas dos categorías viven en el heap, no en la pila.

---

### [F-15] Categorías 3 y 4 — Heap

**Tiempo estimado:** 4 min

**Qué decir:**
- Categoría 3 (heap explícita): el programador decide cuándo crear el objeto (`new`) y el sistema decide cuándo liberarlo (GC en TypeScript, drop automático en Rust).
- El ejemplo de Rust es poderoso: Rust garantiza que no hay leaks de memoria sin necesitar GC — el ownership hace que el compilador inserte el drop automáticamente al salir del scope.
- Categoría 4 (heap implícita, Python): la más flexible y la más costosa. Cada asignación puede cambiar el tipo, el valor Y la dirección. El intérprete maneja todo.
- TypeScript con `any` se aproxima a categoría 4 — pero es desaconsejado precisamente por eso.

**Conceptos clave:**
- Heap explícita = `new` crea; GC/ownership libera
- Heap implícita = cualquier asignación vincula todos los atributos
- Rust elimina el GC usando ownership — cero overhead de runtime

**Transición:** Ahora pasamos al ámbito — ¿dónde en el código es visible el nombre de la variable?

---

## BLOQUE 5 — Ámbito (15 min)

---

### [F-16] Ámbito estático (léxico): el algoritmo

**Tiempo estimado:** 4 min

**Qué decir:**
- El ámbito define **visibilidad del nombre** — no es lo mismo que tiempo de vida. Una variable puede existir (estar en memoria) pero estar fuera de ámbito (nombre invisible).
- El algoritmo de resolución es lo que el compilador hace cada vez que ve un identificador: buscar local → padre → abuelo → hasta el módulo raíz. Si no lo encuentra, error de compilación.
- "Estático" significa que este recorrido se hace en compilación, no en runtime. El compilador ya sabe qué variable es cada nombre antes de ejecutar.
- Historia: ALGOL 60 fue el primer lenguaje con ámbito léxico. Todos los lenguajes modernos lo usan como default (Python, TypeScript, Go, Rust, Java, C++...).

**Conceptos clave:**
- Ámbito ≠ tiempo de vida — visibilidad del nombre vs. existencia en memoria
- El algoritmo sube por la cadena estática hasta encontrar el nombre o fallar en compilación
- "Estático" = resuelto en compilación, no en ejecución

**Transición:** Veamos el algoritmo en TypeScript concreto.

---

### [F-17] Ámbito estático en TypeScript

**Tiempo estimado:** 4 min

**Qué decir:**
- Recorrer el código línea por línea: `interna()` puede ver `x` (módulo), `y` (externa), `z` (propio). `externa()` puede ver `x` y `y` pero no `z`. El módulo no puede ver ninguna variable local de ninguna función.
- El comentario `// ❌ z no visible aquí — error de compilación` es el punto pedagógico central: TypeScript sabe en compilación que `z` no existe en ese scope.
- El "problema del ámbito global" (Sebesta §5.5.5): las variables de módulo son visibles en todos los bloques. Eso es un arma de doble filo — cómodo pero peligroso si se usan como canal de comunicación implícito entre funciones.

**Conceptos clave:**
- La visibilidad sigue la estructura léxica del código — no la secuencia de ejecución
- Variables de módulo visibles en todo el código del módulo — cuidado con el abuso

**Transición:** ¿Y si la visibilidad dependiera de quién llama en lugar de dónde está escrito el código?

---

### [F-18] Ámbito dinámico — qué cambia

**Tiempo estimado:** 4 min

**Qué decir:**
- La diferencia conceptual: en estático la cadena que se recorre es la cadena léxica (estructura del código); en dinámico es la cadena de llamadas activas en runtime.
- El problema de legibilidad es clave: con ámbito dinámico, para saber qué variable usa una función tenés que trazar la cadena de llamadas en tu cabeza — eso puede cambiar en cada ejecución.
- El ejemplo de `this` en JavaScript es el más relevante para la audiencia: `this` se resuelve en tiempo de llamada (dinámico). Por eso las arrow functions lo capturan léxicamente — es la solución de TypeScript al problema de ámbito dinámico del `this`.
- No profundizar en Emacs Lisp — es solo para mostrar que existe en lenguajes reales.

**Conceptos clave:**
- Dinámico = cadena de llamadas en runtime determina visibilidad
- `this` en JavaScript/TypeScript tiene semántica dinámica — arrow functions lo fijan léxicamente
- Verificación de tipos para variables no-locales es imposible con ámbito dinámico

**Transición:** Un fenómeno interesante del ámbito estático son los "agujeros de ámbito" — shadowing.

---

### [F-19] Scope holes — shadowing

**Tiempo estimado:** 3 min

**Qué decir:**
- El shadowing ocurre cuando una variable local tiene el mismo nombre que una del bloque exterior. La exterior queda "tapada" — sigue existiendo pero su nombre no es visible.
- El ejemplo es sutil a propósito: dentro del `for`, el `x` que se imprime es el interior (`item * 2`). Después del `for`, el `x` que se imprime es el exterior (`10`). El mismo nombre, dos variables distintas, sin advertencia de TypeScript.
- Los linters están ahí para esto: `@typescript-eslint/no-shadow` detecta y advierte. Mostrar el comando de configuración si hay tiempo.

**Conceptos clave:**
- Scope hole: la variable exterior existe pero su nombre es invisible en el bloque interior
- Shadowing silencioso = bug difícil de rastrear — configurar ESLint `no-shadow`

**Transición:** Cerremos el bloque de conceptos con el entorno de referencia y la inicialización.

---

## BLOQUE 6 — Entorno de Referencia e Inicialización (8 min)

---

### [F-20] Entorno de referencia y constantes

**Tiempo estimado:** 4 min

**Qué decir:**
- El entorno de referencia es la "foto" de todo lo que es visible en un punto del programa. Si uno mentalmente enumera todos los nombres válidos en una sentencia dada — eso es el entorno de referencia.
- Cambia a lo largo del programa: dentro de una función el entorno incluye los parámetros y las variables locales; fuera no.
- Constantes en TypeScript: enfatizar la diferencia entre inmutabilidad de referencia e inmutabilidad de contenido. `const obj = {}` hace inmutable la referencia (`obj` no puede apuntar a otro objeto) pero el objeto en sí es mutable. `Object.freeze()` agrega inmutabilidad de contenido.

**Conceptos clave:**
- Entorno de referencia = conjunto de identificadores visibles en un punto dado
- `const` en TypeScript = inmutabilidad de referencia, no de contenido
- Para inmutabilidad profunda: `Object.freeze()` o `Readonly<T>`

**Transición:** ¿Y qué pasa antes de asignar un valor? ¿Qué hay en la variable?

---

### [F-21] Inicialización — comparativa de lenguajes

**Tiempo estimado:** 4 min

**Qué decir:**
- El caso C es el más dramático: las variables locales no inicializadas contienen basura (lo que quedó en esa dirección de la invocación anterior). Esto genera bugs extremadamente difíciles de reproducir.
- Go tomó la decisión opuesta: zero values garantizados para todo. Cero configuración, cero sorpresas. Es una decisión de diseño explícita del lenguaje.
- TypeScript strict elimina el problema de raíz: si intentás usar una variable antes de asignarle un valor, error de compilación. No hay basura — hay error en desarrollo, no en producción.
- Python en el medio: no hay "basura" pero hay `NameError` en runtime si usás un nombre no definido. Mejor que C, pero más tardío que TypeScript.

**Conceptos clave:**
- C: variables locales no inicializadas = comportamiento indefinido (basura)
- TypeScript strict: error de compilación si se usa antes de asignar
- Go: zero values = `0`, `""`, `false`, `nil` — sin basura por diseño

**Transición:** Arrancamos el bloque final — cómo se conecta todo esto con el código generado por IA.

---

## BLOQUE 7 — IA y Variables (12 min)

---

### [F-22] La IA comete errores de scope

**Tiempo estimado:** 2 min

**Qué decir:**
- Introducir el tema: los modelos de lenguaje generan código que compila y a veces hasta pasa los tests, pero con patrones de scope que serían señalados por cualquier senior de TypeScript.
- ¿Por qué? Los modelos aprendieron de código JavaScript pre-ES6 donde `var` era la única opción. Ese código existe en millones de repositorios que el modelo procesó.
- Los tres patrones que vamos a ver son detectables y prevenibles — tanto por el programador que revisa como por un prompt bien diseñado.

**Conceptos clave:**
- El código generado por IA puede ser correcto sintácticamente pero incorrecto semánticamente en scope
- Los tres patrones se pueden prevenir con revisión activa o con prompts explícitos

**Transición:** Patrón uno: `var` hoisting.

---

### [F-23] Patrón 1 — `var` hoisting

**Tiempo estimado:** 2 min

**Qué decir:**
- Mostrar el código y preguntar: "¿qué imprime `console.log(resultado)`?" — Esperar respuestas. La respuesta intuitiva es "ok" si `activo = true` o error si `activo = false`. La respuesta real es `undefined` en ambos casos (si no se llega a la asignación) o `"ok"` (si `activo = true`).
- Explicar la TDZ (Temporal Dead Zone) de `let`/`const`: a diferencia de `var`, `let` y `const` no se pueden usar antes de su declaración en el código. Si `let resultado` estuviera fuera del `if`, usar `resultado` antes de la asignación daría error en compilación con TypeScript strict.

**Conceptos clave:**
- `var` = hoisting de función; inicialización permanece en su lugar → `undefined` inesperado
- `let`/`const` = Temporal Dead Zone → error explícito y temprano
- Regla: nunca usar `var` en TypeScript moderno

**Transición:** El segundo patrón es más sutil — efectos secundarios ocultos en variables globales.

---

### [F-24] Patrón 2 — Variable global silenciosa

**Tiempo estimado:** 2 min

**Qué decir:**
- La firma de `acumular(n: number)` promete que la función solo necesita `n`. Mentira — también depende de `total`, que no aparece en la firma.
- Esto hace que la función no sea pura: su resultado depende del estado externo y su orden de llamada importa. Difícil de testear, difícil de razonar.
- La versión correcta recibe `total` como parámetro — todas las dependencias son visibles en la firma. Eso es una función sin efectos secundarios.

**Conceptos clave:**
- Dependencia implícita en variable global = efecto secundario oculto
- Función pura: el resultado depende exclusivamente de los parámetros
- Señal de alerta: la función modifica algo no declarado en su firma

**Transición:** El tercer patrón: el nombre correcto apunta a la variable equivocada.

---

### [F-25] Patrón 3 — Shadowing inesperado

**Tiempo estimado:** 2 min

**Qué decir:**
- Este ejemplo es más complicado: la intención del programador es filtrar con `limite = 100`, pero la redeclaración dentro de `validar` lo sombrea con `items.length`.
- La IA que generó este código puede haberlo hecho "por simetría" — usa `limite` como nombre genérico sin ver el conflicto con el módulo exterior.
- El `filter` usa el `limite` del bloque más cercano — `items.length`. Si `items.length < 100`, los resultados pueden parecer correctos, lo que hace el bug difícil de detectar en testing.

**Conceptos clave:**
- Shadowing: el nombre correcto resuelve a la variable equivocada
- Los tests pueden pasar con datos que no revelan el bug

**Transición:** Ahora van a practicar los tres patrones al mismo tiempo.

---

### [F-26] Actividad — tres patrones mezclados

**Tiempo estimado:** 4 min (2 silencio + 2 respuesta grupal)

**Qué decir:**
- Proyectar el código y dar 2 minutos de silencio. No agregar contexto — dejar que trabajen solos.
- Después de los 2 minutos, preguntar: "¿Cuántos encontraron?" y luego "¿Qué patrón es el primero?" — esperar respuestas antes de revelar.
- **Respuesta esperada:**
  - `var total` → Patrón 2 (global mutable que accumula estado entre llamadas)
  - `var resultado` → Patrón 1 (hoisting — `console.log(resultado)` puede ser `undefined`)
  - `const limite = item` dentro del `for` → Patrón 3 (shadowing — el `filter` usa `item`, no `100`)

**Conceptos clave:** [Los tres patrones identificados — ver slides anteriores]

**Preguntas anticipadas:**
- *"¿TypeScript no detecta esto automáticamente?"* → `var resultado` sí con strict (no usada antes de asignación). `const limite` el shadowing solo con ESLint `no-shadow`. `var total` como global es válido en TypeScript — no hay error automático.

**Transición:** ¿Cómo pedirle a la IA que no genere estos patrones?

---

### [F-27] Prompt seguro para variables en TypeScript

**Tiempo estimado:** 2 min

**Qué decir:**
- Mostrar el prompt como si fuera una directiva técnica — no una sugerencia vaga.
- Cada línea del prompt tiene una razón: `strict mode` activa el compilador más estricto; `let/const` elimina `var`; "sin variables globales" elimina el patrón 2; "tipos declarados" permite que el compilador detecte más errores.
- Este prompt no garantiza código perfecto pero reduce significativamente los tres patrones que acabamos de ver.

**Conceptos clave:**
- Los prompts explícitos y técnicos producen mejor código que los genéricos
- "TypeScript strict" y "sin var" son restricciones que el modelo puede cumplir

**Transición:** Cerramos la clase.

---

## Cierre (3 min)

---

### [F-28] Cierre — tres ideas para llevarse

**Tiempo estimado:** 3 min

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
