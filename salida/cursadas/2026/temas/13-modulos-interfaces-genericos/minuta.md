# Minuta de Clase — Clase 13B: Subprogramas: del contrato a la ejecución

> **Tema (topic.yaml):** Módulos, Interfaces y Genéricos
> **Contenido real:** Subprogramas: del contrato a la ejecución
> **Duración total:** 120 minutos | **Lenguaje principal:** TypeScript
> **Contrastes:** Go, Rust, Swift, Kotlin
> **Docente:** Matías Gel
> **Fecha de generación:** 2026-06-28

---

## ⚠️ Drift detectado

El tema se llama **"Módulos, Interfaces y Genéricos"** en `topic.yaml` (Clase 13B), pero el `clase_dada.txt` (607 líneas) contiene la clase sobre **"Subprogramas: del contrato a la ejecución"**. Existe un tema gemelo `13-subprogramas-parametros-sobrecarga` (Clase 13A) cuyo `clase_dada.txt` trata sobre TAD/módulos/interfaces/genéricos — lo inverso. Pareciera que los dos `clase_dada.txt` están intercambiados entre las carpetas 13.

**Decisión operativa:** se mantiene el nombre del tema de `topic.yaml` para consistencia con el sistema, pero esta minuta es fiel al `clase_dada.txt` (subprogramas). Se sugiere al docente revisar si los `clase_dada.txt` de las dos carpetas 13 están intercambiados, o si el título del tema debe renombrarse.

---

## Trazabilidad bibliográfica general

Las citas siguientes respaldan el contenido de la clase con la knowledge base ChromaDB (3 libros ingestados):

- **Sebesta 2019** — *Concepts of Programming Languages*, Pearson.
  - Cap. 9: Subprograms (§9.2 Fundamentals, §9.5 Parameter-Passing Methods, §9.6 Parameters That Are Subprograms, §9.9 Overloaded Subprograms, §9.10 Generic Subprograms) — pp. 389–440.
  - Cap. 10: Implementing Subprograms (§10.1 General Semantics of Calls and Returns, §10.2 Simple Subprograms, §10.4 Nested Subprograms — static link, dynamic link, ARI) — pp. 441–470.
- **Gabbrielli & Martini 2023** — *Programming Languages: Principles and Paradigms*, Springer.
  - Cap. 7 (pp. 106–135): function vs. procedure, activation record fields, dynamic chain pointer / dynamic link / control link.
  - Cap. 7 (pp. 136–282): parameter passing modes (by value, by reference, read-only), parameter passing discipline, cost of modes.
- **Louden & Lambert 2012** — *Programming Languages: Principles and Practices*, Course Technology. Apoyo terminológico.

---

## BLOQUE A — El subprograma como abstracción de acción (20 min)

---

### [F-00] Portada — Subprogramas: del contrato a la ejecución

**Tiempo:** — (no cuenta)

**Guion del docente:**

"Buenos días. Hoy vamos a hablar de subprogramas, pero no desde el lugar habitual —no desde 'cómo se declara una función'— sino desde una pregunta más interesante: ¿qué contrato establece un subprograma con quien lo invoca, y cómo se materializa ese contrato cuando se ejecuta? Vamos a recorrer el camino completo: desde lo que el cliente ve hasta lo que pasa en memoria cuando se llama."

**Conceptos clave a enfatizar:**
- El título de la clase anuncia el hilo conductor: contrato → ejecución.
- No es una clase de sintaxis; es una clase de decisiones de diseño.

**Transición:** "Empecemos por la idea más básica: un subprograma abstrae una acción."

---

### [F-01] Un subprograma abstrae una acción

**Tiempo:** 5 min

**Guion del docente:**

"Un subprograma permite razonar por contrato, no por instrucciones. Cuando ustedes llaman a `console.log` no leen el cuerpo —confían en el contrato. Esa es la idea central. Un subprograma tiene un punto de entrada único y devuelve el control al llamador. Su encabezado establece qué datos recibe y qué resultado produce. El cuerpo queda oculto durante el uso: el cliente invoca una abstracción. Y algo sutil pero importante: cada llamada crea una activación distinta del mismo código. El código es uno; las activaciones son muchas."

**Conceptos clave a enfatizar:**
- Razonar por contrato, no por instrucciones.
- Punto de entrada único + retorno de control.
- Cuerpo oculto: el cliente no necesita leerlo.
- Activación ≠ código: cada llamada crea una activación nueva.

**Preguntas anticipadas:**
- *¿Cuál es la diferencia entre función y subprograma?* — Respuesta: un subprograma es el concepto general; la función es un caso particular que retorna un valor. Lo veremos en F-03.
- *¿"Oculto" significa privado?* — No exactamente: significa que el cliente no necesita leerlo para usar el subprograma. El contrato basta.

**Transición:** "Si el cliente no lee el cuerpo, ¿con qué información razona? Con la definición visible y la llamada. Veamos cómo esos dos roles forman un contrato."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.2 Fundamentals of Subprograms, p. 389: "A subprogram definition describes the interface to and the actions of the subprogram abstraction. A subprogram call is the explicit request that a specific subprogram be executed. A subprogram is said to be active if, after having been called, it has begun execution but has not yet completed that execution."
- Gabbrielli & Martini 2023, Cap. 7, p. 136: "The concept of procedure, or function, or subprogram, constitutes the fundamental unit of program modularisation. Communication between procedures is effected using return values, parameters and the nonlocal environment."

---

### [F-02] Definición y llamada forman un contrato

**Tiempo:** 7 min

**Guion del docente:**

"Miren esta función `distancia`. En la definición, el nombre identifica el servicio; los parámetros son formales —variables locales del llamado—; el perfil es número, orden y tipos; el protocolo agrega el tipo de retorno; y el cuerpo implementa el servicio. En la llamada, todo cambia de rol: el nombre selecciona el servicio; los parámetros son reales —valores o expresiones aportadas—; el perfil debe ser compatible con los argumentos; el protocolo determina el tipo de la expresión resultante; y el cuerpo permanece oculto al cliente. La definición y la llamada cumplen roles distintos. Forman un contrato."

**Conceptos clave a enfatizar:**
- Parámetros formales (definición) vs. reales (llamada) — roles distintos.
- Perfil = número, orden, tipos. Protocolo = perfil + tipo de retorno.
- El cuerpo permanece oculto al cliente en ambos lados del contrato.
- La tabla es la herramienta conceptual central de la clase.

**Preguntas anticipadas:**
- *¿El perfil incluye el tipo de retorno?* — No. El perfil es solo parámetros. El protocolo agrega el retorno.
- *¿Los parámetros formales son variables locales?* — Sí, del llamado. Se inicializan con los valores de los reales.

**Transición:** "Ya tenemos dos roles: definición y llamada. Pero hay una distinción más fina que el contrato expresa: ¿el subprograma calcula un valor o produce un efecto? Esa es la diferencia entre procedimiento y función."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.2, p. 389: subprogram definition describes the interface and the actions; subprogram call is the explicit request for execution.
- Gabbrielli & Martini 2023, Cap. 7, p. 136: "Communication between procedures is effected using return values, parameters and the nonlocal environment."

---

### [F-03] Procedimiento vs. función

**Tiempo:** 4 min

**Guion del docente:**

"Un procedimiento cambia estado o produce un efecto; su resultado es implícito. Una función calcula un valor; su resultado es explícito mediante retorno. Un procedimiento se encadena por secuencia; una función se compone dentro de expresiones. Kotlin usa `Unit` para efectos; Rust exige declarar el tipo retornado cuando no es `()`. El riesgo del procedimiento son los efectos difíciles de rastrear; el riesgo de la función es la dependencia de entradas y entorno. El retorno distingue cálculo de efecto."

**Conceptos clave a enfatizar:**
- Intención: efecto (procedimiento) vs. cálculo (función).
- Composición: secuencia vs. expresión.
- Contrastes modernos: Kotlin `Unit`, Rust tipo de retorno obligatorio.
- Riesgos distintos para cada uno.

**Preguntas anticipadas:**
- *¿Es mejor función o procedimiento?* — No es de mejor o peor: expresan intenciones diferentes. La pregunta es cuál intención querés comunicar.
- *¿Una función puede tener efectos?* — Sí, pero el contrato debería hacerlo visible. Lo veremos en F-07.

**Transición:** "Si el contrato distingue procedimiento de función, ¿cómo verifica el compilador que una llamada es compatible? Con perfil y protocolo."

**Trazabilidad bibliográfica:**
- Gabbrielli & Martini 2023, Cap. 7, p. 106: "The term 'procedure' should denote a subprogram which does not directly return a value, while a function is a subprogram that returns one."
- Sebesta 2019, §9.8 Design Issues for Functions, p. 389.

---

### [F-04] Perfil y protocolo: verificar sin leer el cuerpo

**Tiempo:** 4 min

**Guion del docente:**

"El perfil incluye cantidad, orden y tipos de los parámetros. El protocolo agrega el tipo de retorno. El chequeo estático rechaza llamadas incompatibles antes de ejecutar. Miren este tipo `Distancia`: exige cuatro argumentos numéricos y retorna un número. TypeScript rechaza cantidad y tipos incompatibles. El algoritmo, sus variables locales y su costo permanecen ocultos. El contrato reduce conocimiento necesario, pero no describe toda la semántica. Y algo que vamos a ver reaparecer: el mismo concepto de protocolo reaparece en sobrecarga y funciones de orden superior."

**Conceptos clave a enfatizar:**
- Perfil = parámetros (número, orden, tipos). Protocolo = perfil + retorno.
- Chequeo estático rechaza antes de ejecutar.
- El contrato reduce conocimiento pero no describe toda la semántica.
- Reaparece en sobrecarga y orden superior (anticipación).

**Preguntas anticipadas:**
- *¿Qué significa "no describe toda la semántica"?* — Que el tipo no captura efectos como mutación, falla o suspensión. Lo veremos en F-07.
- *¿TypeScript verifica el protocolo en runtime?* — No, en compilación. En runtime los tipos se borran.

**Transición:** "El contrato dice qué entra y qué sale. Pero antes de hablar del mecanismo de pasaje, tenemos que hablar de la dirección del flujo. ¿El dato entra, sale, o circula en ambas direcciones?"

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.2, p. 389: protocolo como parte del contrato del subprograma.
- Sebesta 2019, §9.9, p. 389: "An overloaded subprogram must have a unique protocol; that is, it must be different from the others in the number, order, or types of its parameters, and possibly in its return type."

---

## BLOQUE B — Parámetros: modos, permisos y efectos (18 min)

---

### [F-05] La dirección del flujo: in, out, inout

**Tiempo:** 4 min

**Guion del docente:**

"Los parámetros describen flujo de información. Antes del mecanismo, importa la dirección del flujo. Modo in: el llamado recibe información del llamador. Modo out: el llamado produce información para el llamador. Modo inout: la información circula en ambas direcciones. La elección debería minimizar acceso innecesario a datos externos. Luego se elige un mecanismo que implemente ese modo. Primero pensás la dirección; después el mecanismo. No al revés."

**Conceptos clave a enfatizar:**
- Dirección del flujo antes que mecanismo.
- in = recibe, out = produce, inout = ambas.
- Minimizar acceso innecesario a datos externos.
- La decisión de modo es semántica; la de mecanismo es implementación.

**Preguntas anticipadas:**
- *¿No es lo mismo in que pass-by-value?* — No. in es un modo (dirección del flujo); pass-by-value es un mecanismo que implementa in. También se puede implementar in con referencia inmutable.
- *¿Por qué minimizar acceso?* — Porque menos acceso significa menos oportunidades de efectos inesperados. Es el principio de permiso mínimo.

**Transición:** "Si la dirección del flujo nos dice qué permiso necesitamos, ¿cómo se relaciona eso con la intención del subprograma? Veamos la tabla intención-permiso."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.5 Parameter-Passing Methods, p. 389: modos in, out, inout como semántica del pasaje.
- Gabbrielli & Martini 2023, Cap. 7, p. 136: "Parameter passing mode: From a semantic viewpoint, there are in modes, out modes and inout modes."

---

### [F-06] Intención y permiso mínimo

**Tiempo:** 5 min

**Guion del docente:**

"Los efectos exigen permisos sobre los datos. El contrato debe limitar qué puede hacer el subprograma. Si la intención es consultar, el permiso mínimo es lectura compartida —referencia inmutable, readonly. Si es modificar, acceso mutable exclusivo —&mut, inout. Si es consumir, transferencia de ownership —parámetro por valor no copiable. Si es producir, retorno tipado —valor, Result o promesa. Esta relación entre intención y permiso conduce a los modos y mecanismos de pasaje. No es decoración: es la diferencia entre un contrato seguro y uno que permite demasiado."

**Conceptos clave a enfatizar:**
- Intención → permiso mínimo (no máximo).
- Consultar = readonly; modificar = &mut; consumir = ownership; producir = retorno.
- La tabla es un mapa de decisión, no una lista de opciones.
- Permiso mínimo = menos superficie de error.

**Preguntas anticipadas:**
- *¿Qué pasa si pido más permiso del necesario?* — El contrato permite efectos que no necesitás, y eso genera bugs difíciles de rastrear.
- *¿"Consumir" es de Rust?* — El concepto es general, pero Rust lo hace explreso con ownership. Lo veremos en F-10.

**Transición:** "El permiso mínimo cubre mutación y consumo. Pero el contrato moderno incluye más efectos: falla, suspensión, cancelación. Veamos cómo."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.5, p. 389: "Constant parameters and in-mode parameters are not exactly alike. Constant parameters clearly implement in-mode semantics."
- Gabbrielli & Martini 2023, Cap. 7, p. 136: "When the formal parameter is not modified in the body of the function, we can imagine maintaining the semantics of passing by value, implementing it using call by reference. This is what constitutes the read-only parameter."

---

### [F-07] Efectos observables en el contrato moderno

**Tiempo:** 4 min

**Guion del docente:**

"La firma tipada no siempre cuenta toda la historia. El contrato moderno incluye efectos observables. Retorno normal: tipo de retorno, composición directa. Mutación: &mut, inout, objeto mutable —estado compartido observable. Falla: Result<T,E> o excepción documentada —flujo alternativo. Suspensión: async, suspend —continuación diferida. Cancelación: señal o contexto —terminación cooperativa. La firma tipada no siempre cuenta toda la historia. Por eso Rust usa Result, Kotlin usa suspend y Swift usa @escaping. El efecto es parte del contrato."

**Conceptos clave a enfatizar:**
- La firma tipada no captura todos los efectos.
- Cinco efectos: retorno, mutación, falla, suspensión, cancelación.
- Cada efecto tiene evidencia moderna en lenguajes reales.
- El contrato moderno es más rico que el tipo de retorno.

**Preguntas anticipadas:**
- *¿Una excepción es un efecto?* — Sí. Si no está documentada en el contrato, el llamador no puede manejarla.
- *¿Suspensión y asincronía son lo mismo?* — Suspensión es el efecto; async/suspend son mecanismos que lo expresan.

**Transición:** "Ya sabemos qué dirección queremos y qué efectos producimos. Ahora: ¿con qué mecanismo implementamos el pasaje? Hay cinco clásicos, y cada uno tiene ventajas y riesgos."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.5, p. 389: pass-by-reference, constant parameters, in-mode parameters.
- Sebesta 2019, §9.8, p. 389: design issues for functions, side effects.

---

### [F-08] Mecanismos de pasaje: tradeoffs

**Tiempo:** 5 min

**Guion del docente:**

"Valor implementa in: aísla al llamador, pero copiar objetos grandes es costoso. Resultado implementa out: expresa salida, pero puede colisionar al copiar resultados. Valor-resultado implementa inout: evita aliasing durante la llamada, pero el orden de copia al retornar importa. Referencia implementa inout: evita copias grandes, pero introduce aliasing y efectos laterales. Nombre implementa inout: reevalúa expresiones, pero la semántica es difícil de predecir. No existe un mecanismo óptimo para todos los casos. Cada uno tiene un costo."

**Conceptos clave a enfatizar:**
- Cinco mecanismos clásicos: valor, resultado, valor-resultado, referencia, nombre.
- Cada uno implementa un modo (in, out, inout).
- Ventaja y riesgo son las dos caras de cada mecanismo.
- No hay óptimo universal: la elección depende del contexto.

**Preguntas anticipadas:**
- *¿JavaScript usa cuál?* — Pass-by-value para primitivos, pass-by-sharing para objetos. Lo veremos en F-12.
- *¿Nombre se usa hoy?* — Casi no. Scala lo tiene como call-by-name. Es históricamente importante pero semánticamente difícil.

**Transición:** "Para hacer concreto esto, veamos tres lenguajes que toman decisiones distintas: Go con pass-by-value, Rust con aliasing mutable restringido, y Swift con inout explícito."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.5, p. 389: "The implementation of pass-by-value, -result, -value-result, and -reference, where the run-time stack is used."
- Gabbrielli & Martini 2023, Cap. 7, p. 136: "The mode in which actual parameters are paired with formal parameters, and the semantics which results from this, is called the parameter passing discipline."

---

## BLOQUE C — Tres lenguajes, tres decisiones de pasaje (18 min)

---

### [F-09] Go — aislamiento de pass-by-value

**Tiempo:** 6 min

**Guion del docente:**

"Go muestra el aislamiento de pass-by-value. La expresión real se evalúa antes de entrar. Su valor inicializa una nueva variable local. La asignación afecta solo esa copia. El retorno explícito comunica el resultado. Miren: `incrementar` recibe `n int`, le suma 1, y retorna. Pero `edad` sigue siendo 20. El formal es una copia. Modificar el formal no modifica el argumento. Si querés modificar el argumento en Go, tenés que pasar un puntero explícitamente. El contrato lo hace visible."

**Conceptos clave a enfatizar:**
- Pass-by-value: el formal es una copia.
- Modificar el formal no modifica el argumento.
- El retorno explícito comunica el resultado.
- Go hace explícito el puntero si querés mutar.

**Preguntas anticipadas:**
- *¿Go tiene referencias?* — No. Go siempre es pass-by-value; para mutar pasás un puntero (que también se pasa por valor).
- *¿Es esto lo mismo que C?* — Conceptualmente sí. C también es pass-by-value; los punteros son el mecanismo para simular referencia.

**Transición:** "Go aísla copiando. Rust toma una decisión distinta: no copia, pero restringe el aliasing mutable. Veamos cómo."

**Trazabilidad bibliográfica:**
- Gabbrielli & Martini 2023, Cap. 7, p. 136: "Figure 7.3 shows a simple example of passing by value. Like in C, C++, Pascal and Java, when we do not explicitly indicate any parameter-passing mode, it is to be understood that parameter is to be passed by value. The variable y never changes its value."

---

### [F-10] Rust — aliasing mutable restringido

**Tiempo:** 6 min

**Guion del docente:**

"Rust restringe el aliasing mutable. Una referencia mutable exige acceso exclusivo. El formal se vincula con la ubicación del argumento real —no hay copia. Asignar al formal modifica directamente el dato del llamador. Pero Rust permite muchas referencias inmutables o una sola mutable. El borrow checker rechaza aliasing mutable antes de ejecutar. Miren: `incrementar` recibe `&mut i32`, desreferencia y suma. Si intentás pasar dos `&mut` al mismo dato simultáneamente, el compilador te frena. El contrato no es solo tipos: es aliasing."

**Conceptos clave a enfatizar:**
- &mut = acceso exclusivo (no copia).
- El formal se vincula con la ubicación del real.
- Borrow checker: muchas inmutables o una mutable.
- El contrato incluye reglas de aliasing, no solo tipos.

**Preguntas anticipadas:**
- *¿Por qué una sola mutable?* — Para garantizar que no hay dos escritores simultáneos al mismo dato. Elimina una clase entera de bugs en compilación.
- *¿Esto es pasaje por referencia?* — Sí, pero con una restricción adicional que el pasaje por referencia clásico no tiene.

**Transición:** "Rust restringe el aliasing. Swift toma una posición intermedia: permite mutar el argumento, pero hace explícita la mutación en la llamada con &."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.5, p. 389: "Pass-by-reference: the formal parameter is bound to the location of the actual parameter. Access to the formal parameters in the called subprogram is by indirect addressing from the stack location of the address."

---

### [F-11] Swift — mutación explícita con inout

**Tiempo:** 6 min

**Guion del docente:**

"Swift hace explícita la mutación del argumento. Los parámetros comunes son constantes dentro de la función. `inout` permite leer y escribir el argumento del llamador. La llamada usa `&` para hacer visible la posible mutación. Miren: `avanzar` recibe `posicion: inout Int` y `pasos: Int`. En la llamada, `&posicion` hace visible que `posicion` puede cambiar. Swift restringe accesos superpuestos al mismo almacenamiento. La idea es que el contrato sea visible en el sitio de llamada, no solo en la definición."

**Conceptos clave a enfatizar:**
- inout = entrada mutable (no es solo entrada ni solo salida).
- `&` en la llamada hace visible la mutación al llamador.
- Los parámetros comunes son constantes dentro de la función.
- Swift restringe accesos superpuestos.

**Preguntas anticipadas:**
- *¿inout es in-out o value-result?* — Semánticamente es value-result: se copia al entrar, se copia al salir. Pero el `&` lo hace visible.
- *¿Por qué `&` en la llamada?* — Para que el que lee la llamada sepa que ese argumento puede cambiar. Es documentación visual.

**Transición:** "Go copia, Rust restringe, Swift marca. Pero hay un caso que no cubre ninguno de los tres: cuando pasás un objeto y el objeto es mutable. Ahí aparece pass-by-sharing."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.5, p. 389: pass-by-value-result (inout mode), copia al entrar y copia al salir.
- Sebesta 2019, §9.5, p. 389: in-mode, out-mode, inout-mode semantics.

---

## BLOQUE D — Compartir objetos (8 min)

---

### [F-12] Pass-by-sharing: separar variable y objeto

**Tiempo:** 4 min

**Guion del docente:**

"Pass-by-sharing separa variable y objeto. La mutación compartida sobrevive; la reasignación local no. Miren este ejemplo: `usuario` tiene `nombre` y `roles`. `cambiar` recibe `u` y hace dos cosas: `u.roles.push('editor')` muta el objeto compartido —sobrevive. `u = { nombre: 'Otro', roles: [] }` reasigna la variable formal —no sobrevive. Después de la llamada, `usuario.nombre` sigue siendo 'Matias' pero `usuario.roles` tiene 'lector' y 'editor'. Compartir referencias no implica necesariamente compartir cambios. La mutabilidad define si compartir es peligroso."

**Conceptos clave a enfatizar:**
- Pass-by-sharing: la variable y el objeto son cosas distintas.
- Mutar el objeto compartido sobrevive a la llamada.
- Reasignar la variable formal no sobrevive.
- La mutabilidad define si compartir es peligroso.

**Preguntas anticipadas:**
- *¿Esto es pass-by-reference?* — No. En pass-by-reference, reasignar el formal cambia el real. En pass-by-sharing, no. La distinción es crucial.
- *¿JavaScript hace esto?* — Sí. Los objetos se pasan por sharing; los primitivos por valor.

**Transición:** "Este ejemplo usa un objeto pequeño. Pero ¿qué pasa con una matriz grande? Ahí el compromiso entre copia y aliasing se vuelve crítico."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.5, p. 389: pass-by-reference para objetos en Java (object references); pass-by-value del reference.
- Sebesta 2019, §9.5, p. 389: "Neither p1 nor p3 need be explicitly dereferenced in fun."

---

### [F-13] Una matriz grande: copia vs. aliasing

**Tiempo:** 4 min

**Guion del docente:**

"Una matriz grande muestra el compromiso entre copia y aliasing. Valor: copiar toda la matriz —aislamiento total, pero consumo de memoria. Referencia mutable: sin copia inicial —pero aliasing y efectos laterales. Valor-resultado: copia al entrar y salir —cambio diferido, pero orden de copia final. Referencia inmutable + resultado: copia solo del resultado —flujo explícito, pero construcción de nueva matriz. Elegir un mecanismo exige balancear riesgos. No hay respuesta universal: depende del tamaño del dato, de la frecuencia de llamada y de cuánto confiás en el llamador."

**Conceptos clave a enfatizar:**
- El tamaño del dato cambia el tradeoff.
- Valor = aislamiento pero costo de copia.
- Referencia mutable = eficiencia pero aliasing.
- Referencia inmutable + resultado = flujo explícito, sin aliasing.

**Preguntas anticipadas:**
- *¿Cuándo conviene valor-resultado?* — Cuando querés inout sin aliasing durante la llamada. Es raro en lenguajes modernos.
- *¿La referencia inmutable + resultado es funcional?* — Sí. Es el estilo de funciones puras que retornan un nuevo valor en lugar de mutar.

**Transición:** "Hasta aquí hablamos de datos. Pero un subprograma también puede recibir comportamiento: un callback. Y eso cambia el contrato."

**Trazabilidad bibliográfica:**
- Gabbrielli & Martini 2023, Cap. 7, p. 136: "Let us note how this is an expensive mode when the value parameter is bound to a large data structure. In such a case, the entire structure is copied to the formal. On the other hand, the cost of accessing the formal parameter is minimal."

---

## BLOQUE E — Callbacks (12 min)

---

### [F-14] Un callback es parte del contrato

**Tiempo:** 5 min

**Guion del docente:**

"Un callback es un subprograma recibido como parámetro y ejecutado por otro subprograma. Pasar comportamiento exige definir protocolo, efectos y frecuencia. La firma establece entradas y retorno del callback. El contrato debe aclarar cuántas veces y cuándo será invocado. También importa si puede fallar, suspenderse o retenerse. Una callback retenida puede extender la vida de su entorno capturado. La closure ya la estudiamos; aquí importa su impacto contractual. Miren: `Comparador<T>` es un tipo función; `ordenar` lo recibe como parámetro. El callback es parte del contrato del llamador."

**Conceptos clave a enfatizar:**
- Callback = subprograma como parámetro.
- El contrato debe especificar: frecuencia, fallo, retención.
- Una callback retenida extiende la vida del entorno capturado.
- El callback es parte del contrato del llamador, no del llamado.

**Preguntas anticipadas:**
- *¿Un callback es una closure?* — Puede serlo. Una closure es un callback que captura su entorno. Pero no todo callback es una closure.
- *¿Qué quiere decir "frecuencia"?* — Cuántas veces se invoca: una, muchas, cero. El contrato debería decirlo.

**Transición:** "El callback tiene un contrato. Pero ese contrato cambia según si el callback es síncrono, suspendible o escapante. Veamos tres casos."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.6 Parameters That Are Subprograms, p. 393: "Although the idea is natural and seemingly simple, the details of how it works can be confusing. If only the transmission of the subprogram code was necessary, it could be done by passing a single pointer. However, two complications arise."
- Sebesta 2019, §9.7 Calling Subprograms Indirectly, p. 389.

---

### [F-15] Síncrono, suspendible y escapante

**Tiempo:** 7 min

**Guion del docente:**

"Kotlin distingue callback síncrono y suspendible. `(T) -> R` debe completar antes de devolver el control —es síncrono. `suspend (T) -> R` puede suspender y reanudarse —el modificador comunica un efecto que el tipo de retorno no expresa solo. Miren `transformar`: usa `f: (T) -> R` y mapea. `transformarAsync` usa `f: suspend (T) -> R` y puede pausar sin bloquear el hilo. El modificador `suspend` es parte del contrato.

Pero hay otra dimensión: escapar. Una callback no diferido se ejecuta durante la llamada. Una callback diferido se almacena y ejecuta más tarde. Swift exige marcar `@escaping` para volver visible esa diferencia. Miren: `registrar` almacena el handler en una lista —el callback escapa. `emitir` lo ejecuta después. Retener callbacks puede crear ciclos de referencias y recursos vivos. El escape cambia duración, ownership y manejo de errores."

**Conceptos clave a enfatizar:**
- Síncrono vs. suspendible: `suspend` comunica un efecto.
- No diferido vs. diferido (escapante): `@escaping` hace visible el escape.
- Retener callbacks puede crear ciclos de referencias.
- El escape cambia duración, ownership y manejo de errores.

**Preguntas anticipadas:**
- *¿@escaping es de Swift solamente?* — El concepto es general; Swift es el lenguaje que lo hace explícito en el tipo.
- *¿Un callback suspendible puede escapar?* — Sí. Son dimensiones ortogonales: sincronía y escape.

**Transición:** "Los callbacks son una forma de variación: el comportamiento varía. Pero hay otras herramientas para expresar variación: sobrecarga, unión sellada, genérico, interfaz dinámica. Veamos cuándo usar cada una."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.6, p. 393: parameters that are subprograms, passing subprograms as parameters.
- Sebesta 2019, §9.7, p. 389: calling subprograms indirectly.

---

## BLOQUE F — Variación: sobrecarga, dispatch y trait (14 min)

---

### [F-16] Herramientas para expresar variación

**Tiempo:** 5 min

**Guion del docente:**

"El contrato debe expresar la variación correcta. Elegir dispatch evita contratos engañosos. Sobrecarga: protocolos estáticos distintos —`parsear(string)` y `parsear(bytes)`— pero riesgo de ambigüedad. Unión sellada: conjunto cerrado de casos —estado de una operación— pero acopla todos los casos. Genérico/trait: capacidad uniforme —algoritmo sobre ordenables— pero restricción excesiva. Interfaz dinámica: implementaciones abiertas —plugins— pero fallas tardías de integración.

Y hay otra pregunta: ¿cuándo se selecciona la implementación? Sobrecarga: en compilación, usando tipos y argumentos. Despacho virtual: en ejecución, usando el tipo dinámico del receptor. Callback: en ejecución, usando el valor función recibido. Trait/genérico: en compilación o ejecución, según la estrategia del lenguaje. Un nombre puede resolverse en momentos diferentes. Resolución estática, despacho dinámico e indirección no son equivalentes."

**Conceptos clave a enfatizar:**
- Cuatro herramientas de variación con riesgos distintos.
- El momento de selección (compilación vs. ejecución) es una decisión de diseño.
- Resolución estática ≠ despacho dinámico ≠ indirección.
- Elegir la herramienta correcta evita contratos engañosos.

**Preguntas anticipadas:**
- *¿Sobrecarga es polimorfismo?* — Sí, ad hoc. Lo veremos en F-17.
- *¿Un trait es una interfaz?* — Similar, pero con poder adicional: puede tener implementación por defecto y restricciones. Lo veremos en F-18.

**Transición:** "Veamos dos casos concretos: Kotlin con sobrecarga y Rust con impl/dyn Trait."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.9 Overloaded Subprograms, p. 389: "A polymorphic subprogram takes parameters of different types on different activations. Overloaded subprograms provide a particular kind of polymorphism called ad hoc polymorphism."
- Sebesta 2019, §9.10 Generic Subprograms, p. 389: "Parametric polymorphism is provided by a subprogram that takes generic parameters."

---

### [F-17] Kotlin — sobrecarga entre cuerpos distintos

**Tiempo:** 4 min

**Guion del docente:**

"Kotlin resuelve sobrecargas entre cuerpos distintos. La firma selecciona una implementación en compilación. Cada sobrecarga tiene su propio cuerpo. El compilador busca la mejor coincidencia según los argumentos. Conversiones implícitas y parámetros por defecto pueden crear ambigüedad. Miren: `area(radio)` calcula el círculo; `area(base, altura)` calcula el rectángulo. Misma nombre, protocolos distintos, cuerpos distintos. Si el algoritmo es uniforme, una plantilla evita duplicación. La sobrecarga es ad hoc: cada cuerpo puede hacer algo distinto."

**Conceptos clave a enfatizar:**
- Sobrecarga = mismo nombre, protocolos distintos, cuerpos distintos.
- Selección en compilación por tipos y argumentos.
- Ambigüedad con conversiones implícitas y parámetros por defecto.
- Si el algoritmo es uniforme → genérico, no sobrecarga.

**Preguntas anticipadas:**
- *¿TypeScript tiene sobrecarga?* — TypeScript tiene overload signatures, pero una sola implementación. Es distinto a Kotlin.
- *¿Cuándo es ambiguo?* — Cuando dos sobrecargas pueden matchear la misma llamada. El compilador no puede decidir.

**Transición:** "Kotlin especializa cuerpos. Rust separa dispatch estático de dinámico con trait. Veamos cómo."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.9, p. 389: "An overloaded subprogram is one that has the same name as another subprogram in the same referencing environment."
- Sebesta 2019, §9.9, p. 389: "Overloaded subprograms that have default parameters can lead to ambiguous subprogram calls."

---

### [F-18] Rust — impl Trait vs. dyn Trait

**Tiempo:** 5 min

**Guion del docente:**

"Rust separa dispatch estático y dinámico. Un trait es una abstracción de comportamiento: define qué operaciones debe soportar un tipo, sin decir cómo. `impl Trait` permite especialización estática y optimización —el compilador genera código específico. `dyn Trait` acepta implementaciones heterogéneas mediante indirección —el compilador solo sabe que cumple el Trait, no cuál es. Miren: `Tarea` es un trait con `ejecutar`. `Email` lo implementa. `ejecutar_estatico` usa `&impl Tarea` —dispatch en compilación. `ejecutar_dinamico` usa `&dyn Tarea` —dispatch en ejecución. Ambos expresan capacidades, pero producen representaciones distintas. La elección afecta tamaño de código, rendimiento y flexibilidad."

**Conceptos clave a enfatizar:**
- Trait = abstracción de comportamiento (qué, no cómo).
- impl Trait = dispatch estático, especialización, mayor binario.
- dyn Trait = dispatch dinámico, indirección, flexibilidad heterogénea.
- La elección afecta tamaño, rendimiento y flexibilidad.

**Preguntas anticipadas:**
- *¿Cuándo uso dyn?* — Cuando tenés una colección heterogénea de tipos que comparten un trait y no conocés los tipos en compilación.
- *¿impl Trait es como un genérico?* — Sí, conceptualmente. Es dispatch estático con restricción de trait.

**Transición:** "Traits y genéricos son dos caras de la misma moneda: abstracción sobre tipos. Pero la abstracción genérica tiene costos de implementación. Veamos cuáles."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.10 Generic Subprograms, p. 389: "A generic subprogram is one whose computation can be done on data of different types in different activations."
- Sebesta 2019, §9.10, p. 389: "Parametric polymorphism is provided by a subprogram that takes generic parameters that are used in type expressions."
- Gabbrielli & Martini 2023, Cap. 7, p. 295: "By virtue of subtype compatibility, foo can receive as an argument a value of any subclass of A."

---

## BLOQUE G — Abstracción genérica (6 min)

---

### [F-19] Abstracción genérica: costos de implementación

**Tiempo:** 6 min

**Guion del docente:**

"La abstracción genérica tiene costos de implementación. Especialización por tipo: generar código por instanciación —optimización específica, pero mayor binario. Implementación compartida: compartir implementación runtime —menor duplicación, pero menor información runtime. Preservación selectiva: conservar ciertos tipos —inspección selectiva, pero reglas más complejas.

Miren TypeScript: `identidad<T>` es una sola definición. En compilación, `identidad<number>(10)` y `identidad<string>('hola')` comparten la misma implementación —TypeScript borra los tipos genéricos al compilar a JavaScript. En runtime no existe `T`. Si necesito información en runtime, debo pasarla explícitamente. Miren `esTipo<T>`: recibe un `check` que preserva la información de tipo en runtime. Especializar o compartir código intercambia rendimiento, tamaño y flexibilidad."

**Conceptos clave a enfatizar:**
- Tres estrategias: especialización, implementación compartida, preservación selectiva.
- TypeScript usa type erasure: en runtime no existe T.
- Preservación selectiva requiere pasar información explícitamente.
- El tradeoff es rendimiento vs. tamaño vs. flexibilidad.

**Preguntas anticipadas:**
- *¿Rust especializa o comparte?* — Rust especializa por defecto (monomorfización). C++ también. Java comparte (type erasure como TypeScript).
- *¿Por qué TypeScript borra los tipos?* — Porque compila a JavaScript, que no tiene tipos genéricos en runtime.

**Transición:** "Hasta aquí hablamos del contrato: qué acepta, qué retorna, cómo circulan los datos, qué efectos produce, cómo varía. Ahora bajemos al mecanismo de ejecución. ¿Qué pasa en memoria cuando llamás a un subprograma?"

**Trazabilidad bibliográfica:**
- Sebesta 2019, §9.10, p. 389: "Parametric polymorphism is provided by a subprogram that takes generic parameters that are used in type expressions that describe the types of the parameters of the subprogram. Different instantiations of such subprograms can be given different generic parameters."
- Sebesta 2019, §9.9, p. 389: "Overloaded subprograms provide a particular kind of polymorphism called ad hoc polymorphism. Overloaded subprograms need not behave similarly."

---

## BLOQUE H — Ejecución: activation records y async (19 min)

---

### [F-20] El activation record materializa una llamada

**Tiempo:** 5 min

**Guion del docente:**

"El activation record materializa una llamada. activation record = memoria de una activación. activación = instancia concreta de ejecución. Es la estructura de memoria que conserva el estado de una activación mientras la llamada está en ejecución. Tiene seis componentes. Parámetros: comunican datos desde el llamador. Variables locales: conservan el estado privado de esa activación. Dirección de retorno: indica dónde continuar al terminar. Dynamic link: apunta al activation record del llamador —¿quién me llamó? Valor de retorno: comunica el resultado. Static link, si aplica: permite acceder a variables no locales léxicas —¿dónde busco variables no locales?"

**Conceptos clave a enfatizar:**
- AR = memoria de una activación (no del código).
- Seis componentes: parámetros, locales, dirección de retorno, dynamic link, valor de retorno, static link.
- Dynamic link = ¿quién me llamó? Static link = ¿dónde busco variables no locales?
- El AR se crea al llamar y se libera al retornar.

**Preguntas anticipadas:**
- *¿El AR está en el stack o en el heap?* — Típicamente en el stack. Las closures pueden escapar al heap.
- *¿Siempre hay static link?* — No. Solo en lenguajes con subprogramas anidados y alcance estático. Lo veremos en F-23.

**Transición:** "El AR es la estructura. Pero ¿cómo se crea y se destruye? Con la secuencia call/return."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §10.2 Implementing "Simple" Subprograms, p. 441: activation record instance (ARI), componentes del AR.
- Gabbrielli & Martini 2023, Cap. 7, p. 106: "Dynamic chain pointer. This field stores a pointer to the previous activation record on the stack. Some authors call this pointer the dynamic link or control link."

---

### [F-21] Call y return: administrar el stack

**Tiempo:** 5 min

**Guion del docente:**

"Call y return administran el stack. Llamar crea un nuevo contexto; retornar restaura el anterior. Seis momentos. Primero: preparar la llamada —evaluar argumentos y establecer parámetros. Segundo: crear la activación —reservar el activation record. Tercero: transferir control —guardar la dirección de retorno y saltar al punto de entrada. Cuarto: ejecutar —usar parámetros, locales y enlaces. Quinto: retornar —producir el resultado y restaurar al llamador. Sexto: liberar —retirar el activation record terminado.

Miren el ejemplo: `sumar(2, 3)`. Al llamar, se crea el AR de `sumar`: `a = 2`, `b = 3`, `z = ?`, `ret addr -> main`, `dynamic link -> AR(main)`. Cuando `sumar` retorna, el AR se libera y el control vuelve a `main`."

**Conceptos clave a enfatizar:**
- Seis momentos: preparar, crear, transferir, ejecutar, retornar, liberar.
- Call crea; return restaura y libera.
- El ejemplo `sumar(2, 3)` muestra el AR concreto.
- Dynamic link apunta al AR del llamador (main).

**Preguntas anticipadas:**
- *¿Quién crea el AR: el llamador o el llamado?* — Depende del lenguaje y del ABI. Típicamente el llamador prepara argumentos y el llamado reserva espacio para locales.
- *¿Qué pasa con recursión?* — Cada llamada recursiva crea un AR distinto. Por eso la recursión consume stack.

**Transición:** "Ese modelo funciona para llamadas síncronas. Pero ¿qué pasa con async? La suspensión conserva estado sin mantener el stack síncrono completo."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §10.1 General Semantics of Calls and Returns, p. 441: "The required actions of a subprogram return are less complicated than those of a call."
- Sebesta 2019, §10.2, p. 441: "The caller actions are as follows: 1. Create an activation record."

---

### [F-22] async extiende el modelo de ejecución

**Tiempo:** 5 min

**Guion del docente:**

"async extiende el modelo de ejecución. Una suspensión conserva estado sin mantener el stack síncrono completo. Antes del primer `await`, la función ejecuta como una llamada ordinaria. Al suspenderse, debe conservar parámetros, locales y punto de continuación. El compilador o runtime materializa una máquina de estados reanudable. Miren: `cargar` es async. Cuando llega al `await fetch`, se suspende. El estado se conserva en la máquina de estados, no en el stack. Cuando la promesa resuelve, se reanuda. Los stack traces async reconstruyen una cadena lógica, no siempre el stack físico original."

**Conceptos clave a enfatizar:**
- async = extensión del modelo de ejecución, no un modelo distinto.
- Antes del primer await: ejecución ordinaria.
- Al suspender: máquina de estados reanudable conserva estado.
- Stack traces async son lógicos, no físicos.

**Preguntas anticipadas:**
- *¿async crea un thread?* — No. async es concurrencia de espera, no paralelismo. El hilo se libera al suspender.
- *¿La máquina de estados está en el stack o en el heap?* — Típicamente en el heap, porque debe sobrevivir a la suspensión.

**Transición:** "El AR tiene dos enlaces: dynamic link y static link. Responden preguntas diferentes. Veamos cuáles."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §10.1, p. 441: general semantics of calls and returns, transfer of control.
- Sebesta 2019, §10.4 Nested Subprograms, p. 441: "If the language supports nested subprograms, the call process must create some mechanism to provide access to nonlocal variables."

---

### [F-23] Dynamic link vs. static link

**Tiempo:** 4 min

**Guion del docente:**

"La cadena dinámica reconstruye quién llamó a quién. Dynamic link y static link responden preguntas diferentes. El dynamic link apunta al activation record del llamador —permite restaurar el stack al retornar. Responde: ¿quién me llamó? El static link apunta hacia un ancestro léxico —permite buscar variables no locales con alcance estático. Responde: ¿dónde busco variables no locales? El orden de llamadas y la estructura del programa no siempre coinciden. El dynamic link sigue el orden de llamadas en runtime. El static link sigue la estructura léxica del código fuente."

**Conceptos clave a enfatizar:**
- Dynamic link = ¿quién me llamó? (runtime, orden de llamadas).
- Static link = ¿dónde busco variables no locales? (léxico, estructura del programa).
- Orden de llamadas ≠ estructura del programa.
- El static link solo aplica en lenguajes con subprogramas anidados.

**Preguntas anticipadas:**
- *¿JavaScript necesita static link?* — No. JavaScript no tiene subprogramas anidados con alcance estático en el sentido clásico; usa closures y environment chains.
- *¿Por qué no coinciden?* — Porque podés llamar a una función anidada desde un contexto distinto al léxico. El dynamic link sigue la cadena de llamadas; el static link sigue la cadena léxica.

**Transición:** "Hemos recorrido el camino completo: del contrato visible al mecanismo de ejecución. Cerremos conectando todas las decisiones."

**Trazabilidad bibliográfica:**
- Sebesta 2019, §10.4 Nested Subprograms, p. 441: "Static and dynamic links must be maintained in the activation record instances. The static link is to allow references to nonlocal variables in static-scoped languages."
- Sebesta 2019, §10.4, p. 441: "The dynamic link for the new activation record instance for sub1 is set to point to the activation record instance for bigsub."
- Gabbrielli & Martini 2023, Cap. 7, p. 106: "Dynamic chain pointer. This field stores a pointer to the previous activation record on the stack. Some authors call this pointer the dynamic link or control link."

---

## BLOQUE I — Cierre (5 min)

---

### [F-24] Las decisiones de diseño están conectadas

**Tiempo:** 5 min

**Guion del docente:**

"Las decisiones de diseño están conectadas. Del contrato visible al mecanismo de ejecución. Seis preguntas sintetizan la clase. ¿Qué acepta y retorna? — Perfil y protocolo, verificación de llamadas. ¿Cómo circulan datos? — Modos y mecanismos de pasaje, copias, aliasing y efectos. ¿Qué efectos produce? — Mutación, falla, suspensión, obligaciones del llamador. ¿Puede retener callbacks? — Escapante o no escapante, duración y recursos. ¿Cómo selecciona implementación? — Sobrecarga, trait o dispatch, costo y extensibilidad. ¿Cómo se ejecuta? — Frames, continuaciones y ABI, call, return y depuración. Cada pregunta es una decisión. Cada decisión tiene consecuencias. Y todas están conectadas: el contrato que escribís determina el mecanismo que se ejecuta."

**Conceptos clave a enfatizar:**
- Seis preguntas = seis decisiones de diseño conectadas.
- Del contrato visible (perfil, protocolo) al mecanismo (frames, ABI).
- Cada decisión tiene consecuencias observables.
- El hilo conductor: contrato → ejecución.

**Preguntas anticipadas:**
- *¿Cuál es la decisión más importante?* — No hay una sola. Pero si tuviera que elegir: la dirección del flujo (modos) antes que el mecanismo. Es la que más impacta en la corrección del contrato.
- *¿Esto aplica a todos los lenguajes?* — Sí. Los conceptos son generales; los mecanismos varían.

**Transición:** — (cierre de clase)

**Trazabilidad bibliográfica:**
- Sebesta 2019, Cap. 9–10 (síntesis): del contrato del subprograma (§9.2) a la implementación con activation records (§10.2) y nested subprograms (§10.4).
- Gabbrielli & Martini 2023, Cap. 7 (síntesis): del procedimiento como unidad de modularización (p. 136) a la implementación con dynamic chain pointer (p. 106).

---

## Resumen de tiempos

| Filmina | Título | Tiempo |
|---------|--------|--------|
| F-00 | Portada | — |
| F-01 | Un subprograma abstrae una acción | 5 min |
| F-02 | Definición y llamada forman un contrato | 7 min |
| F-03 | Procedimiento vs. función | 4 min |
| F-04 | Perfil y protocolo: verificar sin leer el cuerpo | 4 min |
| F-05 | La dirección del flujo: in, out, inout | 4 min |
| F-06 | Intención y permiso mínimo | 5 min |
| F-07 | Efectos observables en el contrato moderno | 4 min |
| F-08 | Mecanismos de pasaje: tradeoffs | 5 min |
| F-09 | Go — aislamiento de pass-by-value | 6 min |
| F-10 | Rust — aliasing mutable restringido | 6 min |
| F-11 | Swift — mutación explícita con inout | 6 min |
| F-12 | Pass-by-sharing: separar variable y objeto | 4 min |
| F-13 | Una matriz grande: copia vs. aliasing | 4 min |
| F-14 | Un callback es parte del contrato | 5 min |
| F-15 | Síncrono, suspendible y escapante | 7 min |
| F-16 | Herramientas para expresar variación | 5 min |
| F-17 | Kotlin — sobrecarga entre cuerpos distintos | 4 min |
| F-18 | Rust — impl Trait vs. dyn Trait | 5 min |
| F-19 | Abstracción genérica: costos de implementación | 6 min |
| F-20 | El activation record materializa una llamada | 5 min |
| F-21 | Call y return: administrar el stack | 5 min |
| F-22 | async extiende el modelo de ejecución | 5 min |
| F-23 | Dynamic link vs. static link | 4 min |
| F-24 | Las decisiones de diseño están conectadas | 5 min |
| **Total** | | **120 min** |
