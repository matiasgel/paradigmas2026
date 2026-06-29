# Clase: Concurrencia y Paralelismo
**Materia:** Laboratorio de Programación y Lenguajes 2026 (IF009) | **Fecha:** Semana 15 | **Duración:** 120 min
**Módulo:** XI | **Lenguaje principal:** TypeScript | **Contrastes:** Java, Go, Kotlin

## Objetivos

1. Distinguir concurrencia, paralelismo, asincronía y ejecución secuencial.
2. Explicar qué significa concurrencia a nivel de subprogramas.
3. Diferenciar tarea, thread, proceso y corrutina como unidades de ejecución.
4. Detectar una condición de carrera sobre estado compartido.
5. Explicar sincronización de competencia y cooperación con ejemplos concretos.
6. Usar semáforos y monitores como modelos conceptuales de coordinación.
7. Comparar memoria compartida con pasaje de mensajes.
8. Aplicar en TypeScript la diferencia entre `Promise.all`, `async`/`await` y `worker_threads`.
9. Comparar decisiones de lenguaje en Java, Go y Kotlin.
10. Evaluar cuándo un problema necesita asincronía, concurrencia o paralelismo real.

---

### [F-00] Concurrencia y Paralelismo
**Tiempo:** 0 min (portada — se presenta al iniciar, sin tiempo contado)
**Qué decir:**
- Presentar el tema: "Hoy hablamos de concurrencia y paralelismo, el módulo XI."
- Anunciar el recorrido: fundamentos, sincronización, modelos de comunicación.
- Aclarar que TypeScript es el lenguaje ancla y Java/Go/Kotlin aparecen como contraste.
**Conceptos clave:** recorrido de la clase; lenguaje ancla TypeScript.
**Preguntas anticipadas:** "¿Vamos a programar en Go?" — Sí, como contraste, no como eje.
**Transición:** "Empecemos con un problema que no necesita definiciones previas."

---

### [F-01] Un resultado que cambia solo con el orden
**Tiempo:** 5 min
**Qué decir:**
- Mostrar el pseudo-código TOTAL := 3 con Tarea A (suma 1) y Tarea B (multiplica por 2).
- Preguntar al curso: "¿Cuál es el resultado final?" — dejar que respondan 4, 6, 7 u 8.
- Explicar los tres escenarios: A antes que B = 6; B antes que A = 4; interleaving = 4, 6, 7 u 8.
- Remarcar: "Leer–calcular–escribir no es una operación atómica. El problema no es el lenguaje: es estado compartido sin coordinación."
- No definir nada todavía: la idea es que el conflicto motive el vocabulario que viene.
**Conceptos clave:** estado compartido; leer-calcular-escribir no atómico; el resultado depende del orden.
**Preguntas anticipadas:** "¿Por qué puede dar 7 u 8?" — porque B lee antes de que A escriba, o viceversa, según el interleaving exacto.
**Transición:** "Para hablar de esto necesitamos cuatro palabras que NO son sinónimos."

---

### [F-02] Cuatro palabras que no son sinónimos
**Tiempo:** 7 min
**Qué decir:**
- Recorrer la tabla término por término: concurrencia (¿progresan solapadas?), paralelismo (¿ejecutan simultáneamente en hardware?), asincronía (¿puedo continuar mientras espero?), thread (¿quién ejecuta?).
- Insistir: "Cada término responde una pregunta diferente. No las usemos como sinónimos."
- Subrayar las tres afirmaciones clave: concurrente sin paralelo (un núcleo, multitarea); asíncrono sin concurrente (single event loop, un handler a la vez); paralelismo necesita hardware múltiple, concurrencia no.
- Cerrar: "El foco de esta clase es la concurrencia a nivel de subprogramas."
**Conceptos clave:** concurrencia ≠ paralelismo ≠ asincronía ≠ thread; cada término responde una pregunta distinta.
**Preguntas anticipadas:** "¿Asincronía no es concurrencia?" — Puede serlo, pero no necesariamente: un event loop de un solo handler es asíncrono sin ser concurrente.
**Transición:** "¿Qué significa 'a nivel de subprogramas'? Veamos los dos niveles de concurrencia."

---

### [F-03] Concurrencia a nivel de subprogramas
**Tiempo:** 6 min
**Qué decir:**
- Distinguir concurrencia física (multiprocesadores/multinúcleo, ejecución simultánea efectiva, el runtime mapea tareas lógicas a núcleos) de concurrencia lógica (un solo núcleo intercala tareas rápidamente, el scheduler decide el orden real).
- Remarcar que la concurrencia lógica es "la abstracción central para razonar sobre concurrencia en lenguajes" — es lo que el programador ve.
- Explicar por qué importa la distinción: un programa correcto en lógica debe ser independiente del hardware; las condiciones de carrera aparecen en ambos niveles.
- Ejemplo: "Si razonan solo en concurrencia física, van a pensar que en un núcleo no hay carrera. Falso: hay interleaving lógico."
**Conceptos clave:** concurrencia física (hardware) vs lógica (multiprogramación); la lógica es la abstracción de razonamiento; las carreras aparecen en ambos niveles.
**Preguntas anticipadas:** "¿Entonces en un solo núcleo hay race condition?" — Sí, si hay interleaving lógico sobre estado compartido.
**Transición:** "¿Qué cosas avanzan independientemente? Llamémoslas unidades concurrentes."

---

### [F-04] Tarea, thread, proceso y corrutina
**Tiempo:** 7 min
**Qué decir:**
- Recorrer la tabla: tarea (unidad lógica de trabajo, la gestiona el programa/runtime), thread (unidad de ejecución dentro de un proceso, la gestiona el OS), proceso (espacio de memoria propio con uno o más threads, la gestiona el OS), corrutina (unidad concurrente suspendible cooperativamente, la gestiona el lenguaje/runtime).
- Aclarar: "Para esta clase usamos el término general: unidad concurrente. Lo importante es que avanza independientemente."
- Explicar que el lenguaje o runtime decide cómo ejecutarla: mapeo a threads del OS, event loop, scheduler de goroutines, etc.
- Ejemplo: "Una corrutina de Kotlin no es un thread del OS; el runtime la multiplexa. Una goroutine tampoco. Pero conceptualmente todas son unidades concurrentes."
**Conceptos clave:** unidad concurrente como término general; tarea/thread/proceso/corrutina son mecanismos concretos; el runtime decide el mapeo.
**Preguntas anticipadas:** "¿Una corrutina es un thread?" — No necesariamente; es una unidad concurrente suspendible que el runtime mapea a threads.
**Transición:** "Volvamos al problema de TOTAL. ¿Por qué fue una carrera?"

---

### [F-05] Condición de carrera: el caso TOTAL
**Tiempo:** 8 min
**Qué decir:**
- Enunciar las tres condiciones para que haya carrera: (1) estado compartido mutable, (2) al menos dos unidades lo acceden concurrentemente, (3) al menos una lo modifica.
- Mostrar el código TypeScript con `let total = 3`, Tarea A (`x = total; total = x + 1`) y Tarea B (`y = total; total = y * 2`).
- Remarcar: "El error nace al pensar en atomicidad de leer-calcular-escribir. En TypeScript con workers compartidos o en Java con threads: el problema es el mismo."
- Pedir al curso que identifiquen cuál de las tres condiciones se viola si `total` fuera `const` (no se puede, no hay mutabilidad) o si solo una tarea accede (no hay concurrencia).
**Conceptos clave:** tres condiciones de carrera; leer-calcular-escribir no atómico; el problema es independiente del lenguaje.
**Preguntas anticipadas:** "¿Y si uso `volatile`?" — `volatile` garantiza visibilidad, no atomicidad de la secuencia leer-calcular-escribir.
**Transición:** "¿Por qué aparece el problema? Porque hay estado compartido. Veámoslo como diagrama."

---

### [F-06] Estado compartido: por qué aparece el problema
**Tiempo:** 6 min
**Qué decir:**
- Mostrar el diagrama conceptual: un recurso compartido (cilindro) al que varias unidades (cuadrados) acceden con flechas entrantes y una saliente.
- Explicar por qué no alcanza con un flag booleano simple: "Leer el flag y asignarlo no es atómico → se puede generar carrera sobre el propio mecanismo."
- Introducir la sección crítica: "Segmento de código que accede a un recurso compartido y no debe ejecutarse concurrentemente por más de una tarea."
- Definir exclusión mutua: "Sólo una tarea puede estar dentro de la sección crítica a la vez."
- Dejar plantado: "Necesitamos una región donde el interleaving no importe."
**Conceptos clave:** estado compartido mutable como raíz; flag simple no alcanza; sección crítica y exclusión mutua.
**Preguntas anticipadas:** "¿Un `boolean` no es atómico?" — La lectura/escritura individual sí puede serlo, pero la secuencia leer-decidir-asignar no lo es.
**Transición:** "¿Qué propiedades debe cumplir una sección crítica bien hecha? Cuatro."

---

### [F-07] Sincronización de competencia
**Tiempo:** 7 min
**Qué decir:**
- Listar las cuatro propiedades: exclusión mutua (como máximo una unidad dentro), progreso (si nadie está adentro y alguien quiere entrar, debe poder), espera acotada (nadie espera indefinidamente si el recurso está libre periódicamente), sin suposición de velocidad (la solución funciona independientemente del planificador).
- Explicar por qué importan las cuatro: sin exclusión mutua hay carrera; sin progreso el recurso queda inaccesible; sin espera acotada hay inanición; sin independencia de velocidad la solución depende del hardware.
- Mostrar el esquema: "Protocolo de entrada → Sección crítica → Protocolo de salida."
- Aclarar que estas propiedades son el contrato que cualquier mecanismo (semáforo, monitor, lock) debe cumplir.
**Conceptos clave:** cuatro propiedades de la sección crítica; protocolo de entrada/salida; el contrato es independiente del mecanismo.
**Preguntas anticipadas:** "¿Qué pasa si no hay espera acotada?" — Inanición: una unidad puede esperar para siempre.
**Transición:** "El mecanismo clásico de Dijkstra para garantizar esto: los semáforos."

---

### [F-08] Semáforos: el mecanismo clásico de Dijkstra
**Tiempo:** 9 min
**Qué decir:**
- Mostrar las operaciones `wait(s)` (si contador > 0 decrementa, si no suspende en cola) y `release(s)` (si cola no vacía despierta una, si no incrementa contador).
- Explicar los dos usos canónicos: semáforo binario (contador=1, exclusión mutua, actúa como mutex) y semáforo contador (contador=N, limita N accesos simultáneos).
- Remarcar la propiedad clave: "`wait` y `release` son operaciones atómicas — el hardware garantiza que no hay interleaving dentro de ellas. El programador es responsable de usar el protocolo correctamente."
- Mostrar el código TypeScript con `SharedArrayBuffer`, `Int32Array`, `Atomics.compareExchange`, `Atomics.wait`, `Atomics.store`, `Atomics.notify`.
- Explicar la convención 0=libre, 1=tomado y el patrón adquirir/try/finally/liberar.
- Aclarar: "Esto es un semáforo binario implementado sobre Atomics. El concepto es el de Dijkstra; la implementación es de bajo nivel."
**Conceptos clave:** semáforo = contador + cola; wait/release atómicos; binario (mutex) vs contador; Atomics como implementación de bajo nivel en TS.
**Preguntas anticipadas:** "¿`Atomics.compareExchange` es atómico?" — Sí, el hardware garantiza la atomicidad de la operación de comparación e intercambio.
**Transición:** "Los semáforos son poderosos pero frágiles. Veamos los errores típicos."

---

### [F-09] Errores típicos con semáforos
**Tiempo:** 5 min
**Qué decir:**
- Recorrer la tabla de errores: olvidar `release` tras `wait` (deadlock permanente), `release` sin `wait` previo (otro thread entra en sección crítica, dato corrupto), `wait`/`release` en orden invertido (deadlock o corrupción según timing), sección crítica demasiado pequeña (carrera sobre el resto del código), sección crítica demasiado grande (serializa trabajo que podría ser paralelo).
- Insistir: "El compilador NO detecta omisiones ni mal orden de wait/release. Esa es la fragilidad de los semáforos."
- Mencionar que el mismo mecanismo resuelve competencia y cooperación, pero combinarlos mal puede causar deadlock (adelanto de F-11).
**Conceptos clave:** cinco errores típicos; el compilador no detecta errores de protocolo; fragilidad de los semáforos.
**Preguntas anticipadas:** "¿Cómo se evita olvidar el `release`?" — Con try/finally o abstracciones de más alto nivel (monitores).
**Transición:** "Los monitores justamente encapsulan esto para que el lenguaje te ayude."

---

### [F-10] Monitores: encapsular estado compartido
**Tiempo:** 8 min
**Qué decir:**
- Definir monitor: abstracción con tres partes — estado privado (solo accesible desde dentro), procedimientos sincronizados (la entrada garantiza exclusión mutua automática), variables de condición (permiten esperar dentro del monitor sin bloquear a otras).
- Explicar el código Java `BufferMonitor<T>`: `synchronized` convierte el método en procedimiento de monitor, `wait()` suspende y libera el lock temporalmente, `notifyAll()` despierta a todos los que esperan para que re-evalúen la condición.
- Recorrer `insertar` (while lleno wait, add, notifyAll) y `extraer` (while vacío wait, poll, notifyAll).
- Contrastar con semáforos: "El monitor encapsula el lock. No te olvidás de liberar porque el lenguaje lo hace al salir del método synchronized."
- Mencionar el patrón `while (condición) wait()` — no `if` — para evitar despertares espurios.
**Conceptos clave:** monitor = estado privado + procedimientos sincronizados + variables de condición; `synchronized`/`wait`/`notifyAll` en Java; el lenguaje gestiona el lock.
**Preguntas anticipadas:** "¿Por qué `while` y no `if` antes del `wait`?" — Para re-evaluar la condición al despertar; puede haber despertares espurios o múltiples consumidores.
**Transición:** "Los monitores resuelven competencia. ¿Y cuando una unidad necesita que otra produzca algo? Cooperación."

---

### [F-11] Sincronización de cooperación
**Tiempo:** 6 min
**Qué decir:**
- Explicar el modelo productor/consumidor con semáforos: `vacio` (lugares disponibles), `lleno` (datos disponibles), `mutex` (exclusión mutua sobre el buffer).
- Mostrar el pseudo-código: productor hace `wait(vacio)`, `wait(mutex)`, inserta, `release(mutex)`, `release(lleno)`; consumidor hace `wait(lleno)`, `wait(mutex)`, extrae, `release(mutex)`, `release(vacio)`.
- Remarcar el orden crítico: "Si el productor hace `wait(mutex)` antes que `wait(vacio)` y el buffer está lleno, se bloquea dentro de la sección crítica. El consumidor nunca puede entrar → deadlock."
- Contrastar con el monitor de F-10: ahí el `while (cola.size() == capacidad) wait()` hace la cooperación dentro del monitor, sin semáforos explícitos.
**Conceptos clave:** cooperación = esperar una condición producida por otra; tres semáforos (vacio/lleno/mutex); el orden de wait importa.
**Preguntas anticipadas:** "¿Por qué no un solo semáforo?" — Porque competencia (mutex) y cooperación (lleno/vacío) son problemas distintos que necesitan señales distintas.
**Transición:** "¿Y si en lugar de compartir memoria nos comunicamos? Pasaje de mensajes."

---

### [F-12] Pasaje de mensajes: comunicar en lugar de compartir
**Tiempo:** 8 min
**Qué decir:**
- Presentar el modelo: cada unidad concurrente tiene estado local, la coordinación ocurre enviando y recibiendo mensajes, no hay memoria compartida visible, el protocolo se vuelve explícito, no compartir memoria mutable reduce la necesidad de locks.
- Mostrar las operaciones `send(destino, mensaje)` y `receive(origen, mensaje)`.
- Explicar la tabla de modelos: síncrono (emisor y receptor se encuentran, más predecible, menos concurrencia real), asincrónico (emisor no bloquea, mayor concurrencia, puede haber acumulación de mensajes), canal (medio explícito por donde circulan mensajes, tipado y sincronización explícitos).
- Adelantar: "Go encarna este modelo con channels. Lo veremos en F-15."
- Mencionar que el pasaje de mensajes puede resolver tanto cooperación como competencia mediante protocolos de comunicación.
**Conceptos clave:** comunicar en lugar de compartir; send/receive; síncrono vs asincrónico vs canal; reduce la necesidad de locks.
**Preguntas anticipadas:** "¿El pasaje de mensajes elimina las carreras?" — Elimina las carreras sobre memoria compartida, pero introduce problemas de orden de mensajes y deadlock de comunicación.
**Transición:** "Bajemos todo esto a TypeScript. ¿Cómo se ve la concurrencia en un lenguaje con un solo hilo?"

---

### [F-13] TypeScript: event loop, `async` y `Promise.all`
**Tiempo:** 10 min
**Qué decir:**
- Explicar el modelo de ejecución: JavaScript tiene un solo hilo por defecto, el event loop toma tareas de la cola y las ejecuta hasta completion, `await` suspende el handler actual y devuelve el control al event loop, otros handlers pueden correr mientras se espera la I/O.
- Recorrer el código: `fetch` inicia sin esperar, `Promise.all` espera ambas, solo un handler a la vez pero dos requests pendientes simultáneamente.
- Insistir en qué es y qué no es: "Es concurrencia de espera sobre I/O. NO es cómputo paralelo en CPU — el código JavaScript es secuencial. NO es multiprocesamiento — un solo heap, un solo GC, un solo thread por defecto."
- Aclarar la distinción con el Tema 11: "Acá retomamos async/await como asincronía, no como estructura de control."
- Ejemplo: "Si los dos fetch tardan 2s cada uno, con Promise.all tardan ~2s, no 4s. Pero el CPU no está haciendo dos cosas a la vez: está esperando dos I/O a la vez."
**Conceptos clave:** event loop cooperativo; `await` suspende sin bloquear; `Promise.all` coordina operaciones asincrónicas; es concurrencia de espera, no paralelismo de CPU.
**Preguntas anticipadas:** "¿Entonces `async` crea un thread?" — No. Expresa suspensión sobre el event loop. El hilo sigue siendo uno.
**Transición:** "¿Y si necesito cómputo paralelo de verdad? Workers."

---

### [F-14] TypeScript: workers cuando hay CPU de verdad
**Tiempo:** 8 min
**Qué decir:**
- Definir worker: ejecuta código en una unidad separada, sirve para cómputo intensivo (CPU-bound), se comunica con mensajes, puede compartir memoria mediante `SharedArrayBuffer` pero eso reintroduce problemas de sincronización.
- Recorrer la tabla "cuándo usar workers": esperar I/O → async/await; cómputo CPU-bound → Worker; estado compartido → Sincronización/Atomics.
- Mostrar el código Atomics (repaso de F-08): `SharedArrayBuffer`, `Int32Array`, `compareExchange`, `wait`, `store`, `notify`.
- Explicar: "Si compartís memoria entre workers, volvé a tener carreras. Por eso muchos workers se comunican solo con `postMessage`."
- Aclarar que `worker_threads` es de Node.js; en el navegador hay Web Workers con API similar.
**Conceptos clave:** worker = unidad separada para CPU-bound; `postMessage` evita compartir memoria; `SharedArrayBuffer` + `Atomics` para compartir con sincronización.
**Preguntas anticipadas:** "¿Cuándo elijo worker y cuándo async?" — Si es I/O, async. Si es CPU intensivo, worker. Si mezclás, separá: worker para CPU, async para I/O del worker.
**Transición:** "Veamos cómo otros lenguajes resolvieron las mismas decisiones: Java, Go y Kotlin."

---

### [F-15] Java, Go y Kotlin: tres decisiones de lenguaje
**Tiempo:** 10 min
**Qué decir:**
- **Java:** mostrar `MiTarea extends Thread` con `run()`, `start()` (crea el hilo del OS y llama `run`), `join()` (esperar que termine). Luego mostrar la alternativa `Runnable` con lambda: "Un objeto puede implementar Runnable y extender otra clase a la vez. Se separa la tarea (lógica) del mecanismo (Thread)."
- **Go:** mostrar el código completo con `generarNumeros` (envía por `out <- i`, `close(out)`), `imprimirNumeros` (recibe con `for n := range in`), `main` con `make(chan int)` (canal sin buffer, sincrónico), `sync.WaitGroup`.
- Explicar el principio rector de Go: "Do not communicate by sharing memory; share memory by communicating."
- Datos clave: goroutines ~2 KB de stack (vs ~1 MB de un thread del OS), el scheduler de Go multiplexa goroutines sobre threads del OS automáticamente, los channels son tipados (el compilador detecta errores de tipo en la comunicación).
- **Kotlin:** explicar concurrencia estructurada — las corrutinas viven dentro de un `CoroutineScope` que gobierna ciclo de vida, cancelación y errores; un `Job` modela la unidad concurrente; al cancelar el scope se cancelan todas sus corrutinas hijas; los dispatchers deciden dónde se ejecuta (Default para CPU, IO para I/O).
- Recorrer la tabla comparativa: Java (Thread OS, synchronized/wait/notify, memoria compartida + monitores), Go (Goroutine ~2KB, channels tipados, share memory by communicating), Kotlin (Corrutina, CoroutineScope/Job/dispatchers, concurrencia estructurada + lifecycle).
**Conceptos clave:** Java = threads + monitores (modelo clásico cercano a Sebesta); Go = goroutines + channels (pasaje de mensajes); Kotlin = corrutinas + concurrencia estructurada (lifecycle y cancelación).
**Preguntas anticipadas:** "¿Cuál es mejor?" — Ninguno absolutamente. Cada uno toma una decisión de diseño distinta: Java apuesta por memoria compartida, Go por mensajes, Kotlin por lifecycle estructurado.
**Transición:** "Cierremos con un caso donde hay que decidir el mecanismo."

---

### [F-16] Elegir el mecanismo correcto
**Tiempo:** 6 min
**Qué decir:**
- Plantear el caso: "Tengo que procesar 10.000 imágenes y además consultar tres servicios externos. ¿Qué parte conviene hacer con `Promise.all`, qué parte requiere workers, y qué datos no deberían compartirse sin sincronización?"
- Recorrer la tabla de decisión: consultar 3 servicios externos → `Promise.all` + `async`/`await` (es I/O, el event loop basta); procesar 10.000 imágenes (CPU) → `worker_threads` (cómputo intensivo, el event loop se bloquea); contador compartido entre workers → `Atomics` o `SharedArrayBuffer` (estado compartido, necesita sincronización); resultados parciales del worker → `postMessage` (evita compartir memoria mutable).
- Enunciar la regla práctica: I/O → asincronía (event loop); CPU-bound → paralelismo (workers); estado compartido → sincronización explícita o evitarlo con mensajes.
- Pedir al curso que justifiquen por qué no usar `Promise.all` para las 10.000 imágenes: "Porque cada imagen es CPU-bound; el event loop se bloquea procesando una y no avanza las demás."
**Conceptos clave:** decisión por tipo de trabajo (I/O vs CPU vs estado compartido); `Promise.all` para I/O, workers para CPU, Atomics/mensajes para estado compartido.
**Preguntas anticipadas:** "¿Y si las imágenes son pocas?" — Si son pocas y livianas, el event loop puede bastar. La decisión depende del costo de cómputo por unidad.
**Transición:** "Cerramos con un mapa mental de toda la clase."

---

### [F-17] Cierre: mapa mental de concurrencia
**Tiempo:** 4 min
**Qué decir:**
- Recapitular las tres preguntas para decidir: ¿varias actividades progresan solapadas? → concurrencia; ¿ejecutan simultáneamente en hardware? → paralelismo; ¿puedo continuar mientras espero? → asincronía.
- Recapitular los tres mecanismos de coordinación: semáforos (contador + cola, atómicos pero frágiles), monitores (encapsulamiento + exclusión automática, el lenguaje ayuda), pasaje de mensajes (comunicar en lugar de compartir, Go lo encarna).
- Recapitular los tres niveles en TypeScript: `async`/`await` (concurrencia de espera), `Promise.all` (coordinación de operaciones asincrónicas), `worker_threads` (paralelismo real para CPU).
- Cerrar con la idea final: "El problema no es el lenguaje: es estado compartido sin coordinación."
- Anunciar el TP y la próxima clase según el plan del cursado.
**Conceptos clave:** tres preguntas (concurrencia/paralelismo/asincronía); tres mecanismos (semáforos/monitores/mensajes); tres niveles en TS (async/Promise.all/workers); estado compartido sin coordinación es la raíz.
**Preguntas anticipadas:** — (cierre, no se esperan preguntas nuevas; si las hay, derivar al TP o a la guía de estudio).
**Transición:** Fin de la clase.

---

## Cierre (2-3 min)
**Resumen:**
- Concurrencia, paralelismo y asincronía responden preguntas distintas; no usarlas como sinónimos.
- La condición de carrera nace de estado compartido sin coordinación; los mecanismos son semáforos, monitores y pasaje de mensajes.
- En TypeScript: `async`/`await` para I/O, `Promise.all` para coordinar, `worker_threads` para CPU; Java/Go/Kotlin muestran tres decisiones de diseño distintas.

**Anuncio del TP:** según el plan del cursado (tipo a definir con Aux. Valeria).

**Próxima clase:** según el plan-borrador.md del cursado.

---

## Trazabilidad bibliográfica (para el docente — no en filminas)

- **Sebesta, *Concepts of Programming Languages*, Cap. 13 (Concurrency), §13.1–13.5, pp. 535–552:** concurrencia a nivel de subprogramas, tareas, sincronización de competencia/cooperación, semáforos, monitores, pasaje de mensajes. Fuente primaria estructural de F-03 a F-12.
- **Sebesta, Cap. 13, §Ada/Java/C#/funcionales, pp. 552–584:** soporte de lenguajes para tareas, threads, monitores, comunicación. Base de F-15 (Java).
- **Gabbrielli & Martini, *Programming Languages: Principles and Paradigms*, Cap. 14, pp. 447–486:** distinción procesos/hilos, modelos de memoria compartida y mecanismos de comunicación. Apoyo terminológico de F-03 y F-04.
- **Louden & Lambert, *Programming Languages: Principles and Practices*, Cap. 13, pp. 546–584:** vocabulario complementario sobre unidades concurrentes, sincronización y coordinación.
- **MDN Web Docs — JavaScript execution model:** F-13 (event loop, async/await).
- **Node.js Documentation — worker_threads:** F-14 (workers, SharedArrayBuffer, Atomics).
- **Kotlin Documentation — Coroutines overview:** F-15 (concurrencia estructurada, CoroutineScope, Job, dispatchers).
- **Go Documentation — Memory Model y paquete sync:** F-15 (goroutines, channels, WaitGroup).

> Nota: Las filminas no incluyen citas inline (regla 5 del plan de generación posterior del `diseno.md`). La trazabilidad queda en esta sección de la minuta y en `topic-extract.md`.