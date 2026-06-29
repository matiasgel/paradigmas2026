# Clase: Concurrencia y Paralelismo
**Materia:** Laboratorio de Programación y Lenguajes 2026 (IF009) | **Fecha:** Semana 15 | **Duración:** 120 min
**Módulo:** XI | **Lenguaje principal:** TypeScript | **Contrastes:** Java, Go
**Baseline:** `concurrencia.txt` (filminas reales dadas en clase) — minuta reconstruida fielmente.

## Objetivos

1. Distinguir concurrencia, paralelismo, asincronía y threads como cuatro preguntas distintas.
2. Diferenciar concurrencia física de concurrencia lógica y explicar por qué la lógica es la abstracción de razonamiento.
3. Identificar tarea, thread, proceso y corrutina como unidades concurrentes y usar el término general "unidad concurrente".
4. Detectar una condición de carrera sobre estado compartido (las tres condiciones).
5. Explicar la sección crítica y sus cuatro propiedades.
6. Usar semáforos de Dijkstra como modelo conceptual (binario/contador, wait/release atómicos) y su implementación con Atomics en TypeScript.
7. Diferenciar sincronización de competencia (mutex) y de cooperación (productor/consumidor).
8. Reconocer los cinco errores típicos con semáforos.
9. Explicar monitores (estado privado + procedimientos sincronizados + variables de condición) y su implementación en Java con `synchronized`/`wait`/`notifyAll`.
10. Comparar memoria compartida con pasaje de mensajes (síncrono, asincrónico, canales).
11. Crear hilos en Java con `Thread` y `Runnable` y justificar por qué `Runnable` separa tarea de mecanismo.
12. Explicar goroutines y channels de Go como encarnación del pasaje de mensajes.
13. Explicar el event loop de JavaScript, `async`/`await` y `Promise.all` como concurrencia de espera (no paralelismo de CPU).
14. Decidir cuándo usar workers y cuándo async/await según el tipo de trabajo (I/O vs CPU-bound).
15. Reconocer Atomics como exclusión mutua de bajo nivel sobre `SharedArrayBuffer`.

---

### [F-00] Concurrencia y Paralelismo
**Tiempo:** 2 min
**Qué decir:**
- Presentar el tema: "Hoy hablamos de concurrencia y paralelismo, el módulo XI."
- Anunciar el recorrido: fundamentos, sincronización, modelos de comunicación.
- Aclarar que TypeScript es el lenguaje ancla y Java y Go aparecen como contraste.
**Conceptos clave:** recorrido de la clase; lenguaje ancla TypeScript; contrastes Java y Go.
**Preguntas anticipadas:** "¿Vamos a programar en Go?" — Sí, como contraste, no como eje.
**Transición:** "Empecemos con un problema que no necesita definiciones previas."

---

### [F-01] Un resultado que cambia solo con el orden
**Tiempo:** 7 min
**Qué decir:**
- Mostrar el pseudo-código `TOTAL := 3` con Tarea A (suma 1) y Tarea B (multiplica por 2), tal cual está en el `.txt`.
- Preguntar al curso: "¿Cuál es el resultado final?" — dejar que respondan 4, 6, 7 u 8.
- Explicar los tres escenarios: A antes que B = 6; B antes que A = 4; interleaving = 4, 6, 7 u 8.
- Remarcar textualmente: "Leer–calcular–escribir no es una operación atómica. El problema no es el lenguaje: es estado compartido sin coordinación."
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
- Subrayar las tres afirmaciones clave del `.txt`: concurrente sin paralelo (un núcleo, multitarea); asíncrono sin concurrente (single event loop, un handler a la vez); paralelismo necesita hardware múltiple, concurrencia no.
- Cerrar: "El foco de esta clase es la concurrencia a nivel de subprogramas."
**Conceptos clave:** concurrencia ≠ paralelismo ≠ asincronía ≠ thread; cada término responde una pregunta distinta.
**Preguntas anticipadas:** "¿Asincronía no es concurrencia?" — Puede serlo, pero no necesariamente: un event loop de un solo handler es asíncrono sin ser concurrente.
**Transición:** "¿Qué significa 'a nivel de subprogramas'? Veamos los dos niveles de concurrencia."

---

### [F-03] Concurrencia física vs concurrencia lógica
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

### [F-04] Tarea, thread, proceso y corrutina como unidades concurrentes
**Tiempo:** 6 min
**Qué decir:**
- Presentar la idea del `.txt`: la unidad concurrente puede llamarse tarea, thread, proceso liviano o corrutina.
- Aclarar: "Para esta clase usamos el término general: unidad concurrente. Lo importante es que avanza independientemente."
- Explicar que el lenguaje o runtime decide cómo ejecutarla: mapeo a threads del OS, event loop, scheduler de goroutines, etc.
- No inventar una tabla comparativa: el `.txt` no la trae. Alcanza con el término general y la idea de "avanza independientemente".
- Ejemplo: "Una corrutina de Kotlin no es un thread del OS; el runtime la multiplexa. Una goroutine tampoco. Pero conceptualmente todas son unidades concurrentes."
**Conceptos clave:** unidad concurrente como término general; tarea/thread/proceso/corrutina son mecanismos concretos; el runtime decide el mapeo.
**Preguntas anticipadas:** "¿Una corrutina es un thread?" — No necesariamente; es una unidad concurrente suspendible que el runtime mapea a threads.
**Transición:** "Volvamos al problema de TOTAL. ¿Por qué fue una carrera?"

---

### [F-05] Condición de carrera: anatomía del problema
**Tiempo:** 6 min
**Qué decir:**
- Enunciar las tres condiciones para que haya carrera: (1) estado compartido mutable, (2) al menos dos unidades lo acceden concurrentemente, (3) al menos una lo modifica.
- Mostrar el código TypeScript del `.txt` con `let total = 3`, Tarea A (`const x = total; total = x + 1`) y Tarea B (`const y = total; total = y * 2`).
- Remarcar: "El error nace al pensar en atomicidad de leer-calcular-escribir. En TypeScript con workers compartidos o en Java con threads: el problema es el mismo."
- Pedir al curso que identifiquen cuál de las tres condiciones se viola si `total` fuera `const` (no hay mutabilidad) o si solo una tarea accede (no hay concurrencia).
**Conceptos clave:** tres condiciones de carrera; leer-calcular-escribir no atómico; el problema es independiente del lenguaje.
**Preguntas anticipadas:** "¿Y si uso `volatile`?" — `volatile` garantiza visibilidad, no atomicidad de la secuencia leer-calcular-escribir.
**Transición:** "¿Cómo evitamos que el interleaving rompa el dato? Necesitamos una sección crítica."

---

### [F-06] Sincronización: la sección crítica
**Tiempo:** 6 min
**Qué decir:**
- Definir sección crítica: "Segmento de código que accede a un recurso compartido y no debe ejecutarse concurrentemente por más de una tarea."
- Definir exclusión mutua: "Sólo una tarea puede estar dentro de la sección crítica a la vez."
- Listar las cuatro propiedades del `.txt`: exclusión mutua (como máximo una unidad dentro), progreso (si nadie está adentro y alguien quiere entrar, debe poder), espera acotada (nadie espera indefinidamente si el recurso está libre periódicamente), sin suposición de velocidad (la solución funciona independientemente del planificador).
- Explicar por qué no alcanza con un flag booleano simple: "Leer el flag y asignarlo no es atómico → se puede generar carrera sobre el propio mecanismo."
- Dejar plantado: "Necesitamos una región donde el interleaving no importe."
**Conceptos clave:** sección crítica y exclusión mutua; cuatro propiedades; flag simple no alcanza porque leer-asignar no es atómico.
**Preguntas anticipadas:** "¿Un `boolean` no es atómico?" — La lectura/escritura individual sí puede serlo, pero la secuencia leer-decidir-asignar no lo es.
**Transición:** "El mecanismo clásico de Dijkstra para garantizar esto: los semáforos."

---

### [F-07] Semáforos: el mecanismo clásico de Dijkstra
**Tiempo:** 7 min
**Qué decir:**
- Presentar el semáforo como contador entero + cola de espera.
- Mostrar las operaciones `wait(s)` (si contador > 0 decrementa, si no suspende en cola) y `release(s)` (si cola no vacía despierta una, si no incrementa contador).
- Explicar los dos usos canónicos: semáforo binario (contador=1, exclusión mutua, actúa como mutex) y semáforo contador (contador=N, limita N accesos simultáneos).
- Remarcar la propiedad clave: "`wait` y `release` son operaciones atómicas — el hardware garantiza que no hay interleaving dentro de ellas. El programador es responsable de usar el protocolo correctamente."
- Aclarar que esto es concepto puro de Dijkstra; la implementación concreta viene en la siguiente filmina.
**Conceptos clave:** semáforo = contador + cola; wait/release atómicos; binario (mutex) vs contador; el programador es responsable del protocolo.
**Preguntas anticipadas:** "¿Quién garantiza que wait sea atómico?" — El hardware, mediante instrucciones de comparación e intercambio atómicas.
**Transición:** "Veamos cómo se implementa esto en TypeScript con Atomics."

---

### [F-08] Semáforos en código: exclusión mutua con Atomics
**Tiempo:** 7 min
**Qué decir:**
- Mostrar el código TypeScript del `.txt` con `SharedArrayBuffer`, `Int32Array`, `Atomics.compareExchange`, `Atomics.wait`, `Atomics.store`, `Atomics.notify`.
- Explicar la convención 0=libre, 1=tomado y el patrón adquirir/try/finally/liberar.
- Recorrer `adquirir`: el `compareExchange` intenta pasar de 0 a 1; si no lo logra, el worker se bloquea con `Atomics.wait` hasta que alguien notifique.
- Recorrer `liberar`: `store` vuelve a 0 y `notify` despierta a un worker que estaba esperando.
- Aclarar: "Esto es un semáforo binario implementado sobre Atomics. El concepto es el de Dijkstra; la implementación es de bajo nivel."
- Insistir en el `try/finally`: si la sección crítica lanza una excepción, el `liberar` igual se ejecuta.
**Conceptos clave:** Atomics como implementación de bajo nivel de un semáforo binario; compareExchange/wait/notify; patrón try/finally para no olvidar liberar.
**Preguntas anticipadas:** "¿`Atomics.compareExchange` es atómico?" — Sí, el hardware garantiza la atomicidad de la operación de comparación e intercambio.
**Transición:** "Los semáforos también resuelven cooperación, no solo competencia. Veamos productor/consumidor."

---

### [F-09] Semáforos en cooperación: productor/consumidor
**Tiempo:** 6 min
**Qué decir:**
- Explicar que el semáforo resuelve competencia (mutex) y cooperación (lleno/vacío) por separado, con el mismo mecanismo.
- Presentar el escenario productor/consumidor: el productor produce datos y los pone en un buffer; el consumidor los saca.
- Tres semáforos: `mutex` (exclusión mutua sobre el buffer), `lleno` (cuántos datos hay disponibles), `vacío` (cuántos lugares libres hay).
- Remarcar el punto crítico del `.txt`: "Combinar mal los `wait` puede causar deadlock."
- Explicar el orden correcto: el productor hace `wait(vacio)` antes que `wait(mutex)`; si lo invierte y el buffer está lleno, se bloquea dentro de la sección crítica y el consumidor nunca puede entrar → deadlock.
- No inventar pseudo-código detallado: el `.txt` solo trae la idea conceptual. Alcanza con explicar el orden de los wait.
**Conceptos clave:** cooperación = esperar una condición producida por otra; tres semáforos (mutex/lleno/vacío); el orden de los wait importa; combinar mal causa deadlock.
**Preguntas anticipadas:** "¿Por qué no un solo semáforo?" — Porque competencia (mutex) y cooperación (lleno/vacío) son problemas distintos que necesitan señales distintas.
**Transición:** "Los semáforos son poderosos pero frágiles. Veamos los errores típicos."

---

### [F-10] Errores típicos con semáforos
**Tiempo:** 5 min
**Qué decir:**
- Recorrer la tabla del `.txt` de cinco errores: olvidar `release` tras `wait` (deadlock permanente), `release` sin `wait` previo (otro thread entra en sección crítica, dato corrupto), `wait`/`release` en orden invertido (deadlock o corrupción según timing), sección crítica demasiado pequeña (carrera sobre el resto del código), sección crítica demasiado grande (serializa trabajo que podría ser paralelo).
- Insistir: "El compilador NO detecta omisiones ni mal orden de wait/release. Esa es la fragilidad de los semáforos."
- Mencionar que el mismo mecanismo resuelve competencia y cooperación, pero combinarlos mal puede causar deadlock (refuerzo de F-09).
**Conceptos clave:** cinco errores típicos; el compilador no detecta errores de protocolo; fragilidad de los semáforos.
**Preguntas anticipadas:** "¿Cómo se evita olvidar el `release`?" — Con try/finally o abstracciones de más alto nivel (monitores).
**Transición:** "Los monitores justamente encapsulan esto para que el lenguaje te ayude."

---

### [F-11] Monitores: encapsulamiento y exclusión automática
**Tiempo:** 7 min
**Qué decir:**
- Definir monitor: abstracción con tres partes — estado privado (solo accesible desde dentro), procedimientos sincronizados (la entrada garantiza exclusión mutua automática), variables de condición (permiten esperar dentro del monitor sin bloquear a otras).
- Explicar el código Java `BufferMonitor<T>` del `.txt`: `synchronized` convierte el método en procedimiento de monitor, `wait()` suspende y libera el lock temporalmente, `notifyAll()` despierta a todos los que esperan para que re-evalúen la condición.
- Recorrer `insertar` (while lleno wait, add, notifyAll) y `extraer` (while vacío wait, poll, notifyAll).
- Contrastar con semáforos: "El monitor encapsula el lock. No te olvidás de liberar porque el lenguaje lo hace al salir del método synchronized."
- Mencionar el patrón `while (condición) wait()` — no `if` — para evitar despertares espurios.
**Conceptos clave:** monitor = estado privado + procedimientos sincronizados + variables de condición; `synchronized`/`wait`/`notifyAll` en Java; el lenguaje gestiona el lock.
**Preguntas anticipadas:** "¿Por qué `while` y no `if` antes del `wait`?" — Para re-evaluar la condición al despertar; puede haber despertares espurios o múltiples consumidores.
**Transición:** "¿Y si en lugar de compartir memoria nos comunicamos? Pasaje de mensajes."

---

### [F-12] Pasaje de mensajes: comunicar en lugar de compartir
**Tiempo:** 6 min
**Qué decir:**
- Presentar el modelo del `.txt`: cada unidad concurrente tiene estado local, la coordinación ocurre enviando y recibiendo mensajes, no hay memoria compartida visible, el protocolo se vuelve explícito, no compartir memoria mutable reduce la necesidad de locks.
- Mostrar las operaciones `send(destino, mensaje)` y `receive(origen, mensaje)`.
- Aclarar que puede ser síncrono o asíncrono según el lenguaje/modelo.
- Adelantar: "Go encarna este modelo con channels. Lo veremos en F-15."
- Mencionar que el pasaje de mensajes puede resolver tanto cooperación como competencia mediante protocolos de comunicación.
**Conceptos clave:** comunicar en lugar de compartir; send/receive; reduce la necesidad de locks; protocolo explícito.
**Preguntas anticipadas:** "¿El pasaje de mensajes elimina las carreras?" — Elimina las carreras sobre memoria compartida, pero introduce problemas de orden de mensajes y deadlock de comunicación.
**Transición:** "¿Síncrono o asincrónico? Veamos las tres variantes."

---

### [F-13] Mensajes sincrónicos, asincrónicos y canales
**Tiempo:** 6 min
**Qué decir:**
- Recorrer la tabla del `.txt`: síncrono (sincronización implícita, más predecible, menos concurrencia real), asincrónico (mayor concurrencia, pero puede haber acumulación de mensajes), canal (medio explícito por donde circulan mensajes).
- Explicar la diferencia: en síncrono el emisor bloquea hasta que el receptor recibe; en asincrónico el emisor no bloquea; el canal es el medio explícito que puede ser sincrónico o asincrónico.
- Ejemplo: "El canal sin buffer de Go que veremos es sincrónico: el envío bloquea hasta que alguien reciba."
- Mencionar que Occam fue el primer lenguaje a nivel de programación en usar channels (referencia Gabbrielli/Martini).
**Conceptos clave:** síncrono (emisor bloquea) vs asincrónico (emisor no bloquea) vs canal (medio explícito); cada modelo tiene un trade-off de predecibilidad vs concurrencia.
**Preguntas anticipadas:** "¿Un canal puede ser asincrónico?" — Sí, si tiene buffer; el canal sin buffer es sincrónico.
**Transición:** "Bajemos todo esto a lenguajes concretos. Empecemos por Java."

---

### [F-14] Java Thread y Runnable: creación de hilos
**Tiempo:** 7 min
**Qué decir:**
- Presentar las dos formas de crear un hilo en Java: extender `Thread` o implementar `Runnable`.
- Mostrar el código del `.txt`: `MiTarea extends Thread` con `run()`, `start()` (crea el hilo del OS y llama `run` en él), `join()` (esperar que termine).
- Luego mostrar la alternativa `Runnable` con lambda: "Un objeto puede implementar Runnable y extender otra clase a la vez. Se separa la tarea (lógica) del mecanismo (Thread)."
- Explicar la diferencia clave: `start()` crea el hilo del OS y llama `run()` en él; llamar `run()` directamente NO crea un hilo, es una llamada secuencial.
- `join()` espera que el hilo termine antes de continuar — es sincronización de cooperación.
**Conceptos clave:** dos formas de crear hilos en Java; `start()` crea el hilo del OS; `join()` espera; `Runnable` separa tarea de mecanismo.
**Preguntas anticipadas:** "¿Qué pasa si llamo `run()` en vez de `start()`?" — No se crea un hilo; se ejecuta secuencialmente en el hilo actual.
**Transición:** "Go tomó una decisión distinta: goroutines y channels."

---

### [F-15] Go goroutines y channels
**Tiempo:** 8 min
**Qué decir:**
- Presentar la filosofía de Go: "Do not communicate by sharing memory; share memory by communicating."
- Explicar las goroutines: unidad de concurrencia ultra liviana, cuestan ~2 KB de stack (vs ~1 MB de un thread del OS), el scheduler de Go multiplexa goroutines sobre threads del OS automáticamente.
- Los channels son tipados: el compilador detecta errores de tipo en la comunicación.
- Mostrar el código completo del `.txt`: `generarNumeros` (envía por `out <- i`, `close(out)`), `imprimirNumeros` (recibe con `for n := range in`), `main` con `make(chan int)` (canal sin buffer, sincrónico), `sync.WaitGroup`.
- Explicar `defer wg.Done()` — se ejecuta al salir de la función, garantiza que el WaitGroup se decrementa.
- `close(out)` señaliza que no se envían más datos; el `range` sobre el canal termina cuando se cierra.
- El `WaitGroup` espera que ambas goroutines terminen antes de que `main` retorne.
- Conectar con F-13: el canal sin buffer es sincrónico — el envío bloquea hasta que alguien reciba.
**Conceptos clave:** goroutine ~2KB; channels tipados; "share memory by communicating"; canal sin buffer = sincrónico; WaitGroup para esperar; close para señalizar fin.
**Preguntas anticipadas:** "¿Por qué `close(out)`?" — Para señalizar que no se envían más datos; el `range` del receptor termina al recibir el cierre.
**Transición:** "Veamos cómo TypeScript resuelve la concurrencia con un solo hilo."

---

### [F-16] TypeScript y el event loop de JavaScript
**Tiempo:** 8 min
**Qué decir:**
- Explicar el modelo de ejecución del `.txt`: JavaScript tiene un solo hilo por defecto, el event loop toma tareas de la cola y las ejecuta hasta completion, `await` suspende el handler actual y devuelve el control al event loop, otros handlers pueden correr mientras se espera la I/O.
- Recorrer el código: `fetch` inicia sin esperar, `Promise.all` espera ambas, solo un handler a la vez pero dos requests pendientes simultáneamente.
- Insistir en qué es y qué no es: "Es concurrencia de espera sobre I/O. NO es cómputo paralelo en CPU — el código JavaScript es secuencial. NO es multiprocesamiento — un solo heap, un solo GC, un solo thread por defecto."
- Ejemplo: "Si los dos fetch tardan 2s cada uno, con Promise.all tardan ~2s, no 4s. Pero el CPU no está haciendo dos cosas a la vez: está esperando dos I/O a la vez."
- Conectar con F-02: esto es asincronía (¿puedo continuar mientras espero?) sin ser paralelismo (no hay hardware múltiple).
**Conceptos clave:** event loop cooperativo; `await` suspende sin bloquear; `Promise.all` coordina operaciones asincrónicas; es concurrencia de espera, no paralelismo de CPU.
**Preguntas anticipadas:** "¿Entonces `async` crea un thread?" — No. Expresa suspensión sobre el event loop. El hilo sigue siendo uno.
**Transición:** "¿Y si necesito cómputo paralelo de verdad? Workers."

---

### [F-17] Workers: paralelismo real
**Tiempo:** 8 min
**Qué decir:**
- Definir worker del `.txt`: ejecuta código en una unidad separada, sirve para cómputo intensivo (CPU-bound), se comunica con mensajes, puede compartir memoria mediante `SharedArrayBuffer` pero eso reintroduce problemas de sincronización.
- Recorrer la tabla "cuándo usar workers": esperar I/O → async/await; cómputo CPU-bound → Worker; estado compartido → Sincronización/Atomics.
- Explicar: "Si compartís memoria entre workers, volvé a tener carreras. Por eso muchos workers se comunican solo con `postMessage`."
- Aclarar que `worker_threads` es de Node.js; en el navegador hay Web Workers con API similar.
- Conectar con F-16: el event loop basta para I/O; el worker es para cuando hay que calcular de verdad.
**Conceptos clave:** worker = unidad separada para CPU-bound; `postMessage` evita compartir memoria; `SharedArrayBuffer` + `Atomics` para compartir con sincronización; decisión por tipo de trabajo.
**Preguntas anticipadas:** "¿Cuándo elijo worker y cuándo async?" — Si es I/O, async. Si es CPU intensivo, worker. Si mezclás, separá: worker para CPU, async para I/O del worker.
**Transición:** "Cerramos con el mecanismo de bajo nivel que vimos en F-08: Atomics."

---

### [F-18] Atomics: exclusión mutua de bajo nivel
**Tiempo:** 5 min
**Qué decir:**
- Mostrar el código final del `.txt`: `SharedArrayBuffer`, `Int32Array`, `compareExchange`, `wait`, `store`, `notify` — el mismo mutex de F-08, ahora como cierre.
- Recapitular el recorrido: empezamos con un TOTAL que cambiaba con el orden, pasamos por sección crítica, semáforos, monitores, pasaje de mensajes, Java, Go, TypeScript event loop, workers, y volvemos a Atomics como el mecanismo de bajo nivel que implementa la exclusión mutua.
- Cerrar con la idea final: "El problema no es el lenguaje: es estado compartido sin coordinación."
- Anunciar el TP y la próxima clase según el plan del cursado.
**Conceptos clave:** Atomics como cierre del recorrido; exclusión mutua de bajo nivel; estado compartido sin coordinación es la raíz.
**Preguntas anticipadas:** — (cierre, no se esperan preguntas nuevas; si las hay, derivar al TP o a la guía de estudio).
**Transición:** Fin de la clase.

---

## Cierre (incluido en F-18)
**Resumen:**
- Concurrencia, paralelismo y asincronía responden preguntas distintas; no usarlas como sinónimos.
- La condición de carrera nace de estado compartido sin coordinación; los mecanismos son semáforos, monitores y pasaje de mensajes.
- En TypeScript: `async`/`await` para I/O, `Promise.all` para coordinar, `worker_threads` para CPU; Java y Go muestran dos decisiones de diseño distintas (memoria compartida con monitores vs pasaje de mensajes con channels).

**Anuncio del TP:** según el plan del cursado (tipo a definir con Aux. Valeria).

**Próxima clase:** según el plan-borrador.md del cursado.

---

## Trazabilidad bibliográfica (para el docente — no en filminas)

Citas respaldadas por ChromaDB (colección `edu_knowledge`, tipo `material`):

- **Sebesta, *Concepts of Programming Languages*, Cap. 13 (Concurrency), pp. 557–610:** race condition ("two or more tasks are racing to use the shared resource"), competition synchronization, semáforos como "data structure consisting of an integer and a task description queue" usados para competencia y cooperación, monitores con shared data residente en el monitor, Java Thread/Runnable ("Any class that either inherits from Thread or implements Runnable can override a method named run"). Base de F-05, F-06, F-07, F-08, F-11, F-14.
- **Gabbrielli & Martini, *Programming Languages: Principles and Paradigms*, Cap. 14, pp. 447–486:** ventaja de los monitores sobre semáforos ("the programmer using a monitor can develop a process in a relatively independent way"), variables de condición, pasaje de mensajes con channels ("first appeared at the programming-language level in Occam"), comunicación síncrona vs asincrónica ("the sending and receiving of a message take place at different times, as in the case of e-mail"), sincronización entre threads en Java ("The synchronized methods allow mutual exclusion but not conditional synchronization... Java provides the specific methods wait, notify, and notifyAll"). Base de F-11, F-12, F-13, F-14.
- **Louden & Lambert, *Programming Languages: Principles and Practices*, Cap. 13, pp. 585–666:** monitores y mutual exclusion ("This organization of a monitor provides for mutual exclusion in accessing shared data, but it is not adequate by itself to synchronize processes that must wait for certain conditions"). Apoyo de F-06, F-11. Referencia a Dijkstra (guarded if statement, pp. 406–447) como antecedente conceptual de F-07.

> Nota: Las filminas no incluyen citas inline (regla del plan de generación posterior del `diseno.md`). La trazabilidad queda en esta sección de la minuta. Cada cita arriba fue verificada con `python scripts/knowledge_base.py search "..." --type material` contra ChromaDB local.