# Clase: Concurrencia y Paralelismo

**Materia:** Laboratorio de Programacion y Lenguajes 2026  
**Tema:** 15 — Modulo XI  
**Duracion:** 120 minutos  
**Lenguaje principal:** TypeScript  
**Contrastes:** Java, C#, Go, Kotlin, Erlang, Rust  
**Referencia:** Sebesta Cap. 13 (13.1–13.10), Gabbrielli/Martini Cap. 14, Louden/Lambert Cap. 13

## Objetivos

Al finalizar la clase, el estudiante podra:

1. Distinguir concurrencia, paralelismo, asincronia y ejecucion secuencial.
2. Explicar concurrencia fisica vs logica y su relacion con el hardware.
3. Explicar concurrencia a nivel de subprogramas segun Sebesta.
4. Diferenciar tarea, thread, proceso y corrutina como unidades concurrentes.
5. Detectar y explicar una condicion de carrera sobre estado compartido.
6. Describir exclusion mutua, semaforos y monitores con variables de condicion.
7. Comparar sincronizacion de competencia vs cooperacion.
8. Aplicar AbortController, MessageChannel y Atomics en TypeScript para control de ciclo de vida.
9. Aplicar threads Java con `synchronized`, `wait`/`notify` y `java.util.concurrent`.
10. Describir `lock` en C# y el modelo de actores de Erlang.
11. Usar goroutines, channels y `sync.Mutex` en Go para coordinacion.
12. Aplicar corrutinas de Kotlin con structured concurrency.
13. Distinguir `async`/`await`, `Promise.all` y `worker_threads` en TypeScript.
14. Explicar concurrencia a nivel de sentencias (FORALL/HPF) como caso especial.
15. Elegir el mecanismo de coordinacion adecuado segun el tipo de problema.

---

### [F-00] Concurrencia y Paralelismo

**Tiempo:** 2 min

**Que decir:**

- Presentar como cierre conceptual del Modulo XI: no es "aprender una API mas", sino ordenar decisiones de lenguajes.
- Anticipar la pregunta guia: que puede avanzar a la vez y que debe coordinarse?
- Mencionar que la clase recorre el arco completo de Sebesta Cap. 13: desde fundamentos hasta lenguajes concretos.
- Advertir que seis lenguajes apareceran como contrastes; TypeScript es el ancla, los demas muestran decisiones de diseno distintas.

**Conceptos clave:** concurrencia, paralelismo, coordinacion, Sebesta Cap. 13.

**Preguntas anticipadas:**

- "Vemos sistemas distribuidos?" → No; el foco es concurrencia dentro de un programa.

**Transicion:** Empezar donde el resultado deja de ser obvio: dos unidades actualizan el mismo dato.

---

### [F-01] Un resultado que cambia solo con el orden

**Tiempo:** 3 min

**Que decir:**

- Escribir en pizarron el caso TOTAL = 3 con dos tareas; pedir que el alumno calcule el resultado.
- Mostrar que leer–calcular–escribir tiene tres pasos y que el interleaving puede intercalar cualquiera.
- Enumerar los cuatro resultados posibles: 4, 6, 7 u 8 segun el orden de ejecucion.
- Remarcar: el problema no es sumar ni multiplicar; es que leer–calcular–escribir NO es atomico.
- Este ejemplo viene de Sebesta p. 540 y abre el capitulo.

**Conceptos clave:** interleaving, estado compartido, resultado no determinista, atomicidad.

**Preguntas anticipadas:**

- "JavaScript es single-threaded, esto no pasa en TypeScript normal" → El ejemplo es conceptual; workers y SharedArrayBuffer lo hacen real en TS.
- "Esto siempre reproduce el bug?" → No; depende del timing, por eso es peligroso.

**Transicion:** Antes de resolver, separamos vocabulario. Cuatro palabras que suelen mezclarse.

---

### [F-02] Concurrencia, paralelismo, asincronia y threads: cuatro preguntas distintas

**Tiempo:** 4 min

**Que decir:**

- Recorrer la tabla columna por columna: que pregunta responde, no que definicion tiene.
- Concurrencia: pregunta de composicion de actividades solapadas — no implica hardware multiple.
- Paralelismo: pregunta de ejecucion simultanea fisica — requiere nucleos o procesadores separados.
- Asincronia: pregunta de no bloqueo durante espera — independiente de si hay paralelismo.
- Thread: pregunta mecanica — quien ejecuta instrucciones, no como se organizan.
- Insistir: se pueden combinar, pero no son sinonimos.

**Conceptos clave:** concurrencia, paralelismo, asincronia, thread.

**Preguntas anticipadas:**

- "Promise.all es paralelo?" → Puede tener varias esperas pendientes simultaneamente; no necesariamente computo CPU en paralelo.
- "Un programa concurrente es mas rapido?" → No siempre; puede ser mas responsivo o mas organizado sin ganacias de velocidad.

**Transicion:** Con el vocabulario limpio, la distincion fisica/logica explica por que la concurrencia importa mas alla del hardware disponible.

---

### [F-03] Concurrencia fisica vs concurrencia logica

**Tiempo:** 3 min

**Que decir:**

- Lado izquierdo del diagrama: dos barras al mismo nivel = ejecucion simultanea fisica en dos nucleos.
- Lado derecho del diagrama: dos barras que se alternan = multiprogramacion sobre un solo nucleo.
- Destacar: Sebesta estudia el nivel logico — el programa debe funcionar correctamente independientemente de cuantos nucleos haya.
- Consecuencia: las condiciones de carrera aparecen en ambos niveles; no es un problema solo de hardware paralelo.

**Conceptos clave:** concurrencia fisica, concurrencia logica, multiprogramacion, scheduler.

**Preguntas anticipadas:**

- "Si solo hay un nucleo, no hay carrera?" → Si hay; el scheduler puede interrumpir a mitad de un read-modify-write.

**Transicion:** Ahora si: que es concurrencia a nivel de subprogramas segun el libro.

---

### [F-04] Concurrencia a nivel de subprogramas (Sebesta 13.2)

**Tiempo:** 4 min

**Que decir:**

- El foco del capitulo de Sebesta no es hardware; es como un lenguaje permite dividir un programa en unidades que avanzan.
- La unidad puede llamarse tarea, thread, proceso liviano o corrutina segun el lenguaje.
- Separar dos preguntas que el lenguaje debe responder: como se crean las unidades y como se coordinan.
- Lenguajes con soporte nativo (Go, Rust) hacen visible la concurrencia en la sintaxis.
- Lenguajes de libreria (Java, C#) la delegan a clases; lenguajes funcionales (Erlang) eliminan el estado compartido.

**Conceptos clave:** subprograma concurrente, creacion de unidades, coordinacion.

**Preguntas anticipadas:**

- "Una corrutina es un thread?" → No necesariamente; puede suspenderse sobre un runtime sin mapear uno-a-uno con threads del OS.

**Transicion:** Hay cinco tipos de unidades; veamos como se diferencian en costo y semantica.

---

### [F-05] Tarea, thread, proceso, goroutine y corrutina

**Tiempo:** 3 min

**Que decir:**

- Leer la tabla fila por fila: nivel, memoria, costo de creacion y lenguaje tipico.
- Destacar el extremo del goroutine (~2 KB) vs el proceso (espacio propio, fork costoso).
- Remarcar que thread comparte heap → por eso existe la carrera; proceso tiene memoria propia → aislamiento pero comunicacion mas costosa.
- La corrutina es suspendible; el runtime la puede reanudar en el mismo u otro thread.

**Conceptos clave:** tarea, thread, proceso, goroutine, corrutina, heap compartido.

**Preguntas anticipadas:**

- "Worker de Node es proceso?" → No; es un thread con aislamiento parcial y comunicacion explicita.

**Transicion:** Volvamos a la carrera con ejemplos mas concretos y multiples lenguajes.

---

### [F-06] Condicion de carrera: anatomia en TypeScript y Java

**Tiempo:** 4 min

**Que decir:**

- El ejemplo en TypeScript usa SharedArrayBuffer — memoria real compartida entre workers.
- Descomponer verbalmente las tres lineas: leer arr[0], calcular, escribir arr[0].
- Mostrar que si dos workers hacen eso al mismo tiempo, una escritura pisa a la otra.
- El ejemplo de Java refuerza que el lenguaje no cambia la naturaleza del problema.
- Enunciar las tres condiciones necesarias para que haya carrera: estado compartido mutable + dos unidades + al menos una modifica.

**Conceptos clave:** SharedArrayBuffer, condicion de carrera, tres condiciones necesarias.

**Preguntas anticipadas:**

- "Si uso inmutabilidad se resuelve?" → Si el dato nunca cambia, no hay carrera. Por eso los lenguajes funcionales son mas seguros en concurrencia.

**Transicion:** Para evitar la carrera en estado compartido, necesitamos mecanismos de sincronizacion. El primero: la seccion critica.

---

### [F-07] Sincronizacion de competencia: la seccion critica

**Tiempo:** 4 min

**Que decir:**

- Usar el diagrama: dos unidades quieren entrar al rectangulo central; solo una puede en un momento dado.
- Definir seccion critica como region donde el interleaving puede romper una invariante.
- Enunciar las cuatro propiedades que debe garantizar cualquier solucion: exclusion mutua, progreso, espera acotada, sin suponer velocidad relativa.
- Explicar por que un flag booleano simple no alcanza: leer-y-setear el flag tampoco es atomico.

**Conceptos clave:** seccion critica, exclusion mutua, cuatro propiedades, atomicidad del protocolo.

**Preguntas anticipadas:**

- "No alcanza con un lock?" → El lock SI puede implementar las cuatro propiedades; la pregunta es como se implementa el lock mismo.

**Transicion:** El primer mecanismo formal que implementa exclusion mutua y algo mas: el semaforo de Dijkstra.

---

### [F-08] Semaforos: modelo formal de Dijkstra (Sebesta 13.3)

**Tiempo:** 5 min

**Que decir:**

- Leer `wait` paso a paso: si hay capacidad, decrementar; si no, suspender en cola.
- Leer `release` paso a paso: si hay alguien esperando, despertar; si no, incrementar.
- Insistir en que `wait` y `release` son operaciones atomicas — garantizadas por hardware.
- Dar los dos usos canonicos: contador=1 como mutex, contador=N como limite de concurrencia.
- Conectar con la fragilidad: el protocolo correcto queda en manos del programador.

**Conceptos clave:** semaforo, wait, release, atomicidad hardware, semaforo binario vs contador.

**Preguntas anticipadas:**

- "Semaforo y mutex son lo mismo?" → Mutex es un caso especial con contador=1; el semaforo es mas general.
- "Para que sirve capacidad N?" → Limitar acceso a N conexiones de base de datos, slots de trabajo, etc.

**Transicion:** Veamos como usar semaforos para exclusion mutua Y cooperacion con codigo real.

---

### [F-09] Semaforos en codigo: TypeScript con Atomics y productor/consumidor

**Tiempo:** 5 min

**Que decir:**

- El ejemplo de TypeScript con Atomics muestra exclusion mutua en workers reales: `compareExchange` es la operacion atomica que lee y escribe en un paso.
- Explicar `Atomics.wait`: suspende el worker hasta que el valor cambia, igual que `wait()` de Java pero sobre un entero en SharedArrayBuffer.
- `Atomics.notify` despierta a los waiters, igual que `notifyAll`.
- El pseudocodigo de productor/consumidor introduce DOS semaforos: `vacio` y `lleno` para cooperacion.
- Pedir que el alumno identifique que pasa si se invierten los Wait del mutex y del semaforo de cooperacion: posible deadlock.

**Conceptos clave:** Atomics.compareExchange, Atomics.wait, Atomics.notify, semaforos duales, riesgo de deadlock.

**Preguntas anticipadas:**

- "Por que el mutex va DENTRO de los semaforos de cooperacion?" → Si va fuera y el consumidor espera con el mutex tomado, el productor nunca puede entrar.

**Transicion:** Antes de pasar a monitores, veamos los errores tipicos que generan semaforos mal usados.

---

### [F-10] Errores tipicos con semaforos

**Tiempo:** 3 min

**Que decir:**

- Pasar rapido por la tabla; esta filmina es de cierre del tema semaforos.
- Olvidar `release`: deadlock permanente — el programa se congela.
- `release` de mas: la capacidad real se supera — dato corrupto.
- Seccion critica pequeña: la carrera sigue; seccion critica grande: el programa se serializa.
- El compilador NO detecta estos errores → necesitamos abstracciones mas estructuradas.

**Conceptos clave:** deadlock, corrupcion de datos, cuello de botella por seccion critica excesiva.

**Preguntas anticipadas:**

- "Linters o herramientas detectan esto?" → Algunos race detectors de runtime si (Go tiene uno); el compilador en general no.

**Transicion:** La respuesta estructural a los errores de semaforos es el monitor.

---

### [F-11] Monitores: encapsulamiento y exclusion automatica (Sebesta 13.4)

**Tiempo:** 4 min

**Que decir:**

- Presentar el monitor como tipo abstracto de datos con sincronizacion garantizada por el lenguaje.
- El estado privado no se accede desde afuera — encapsulamiento.
- Cada procedimiento publico tiene exclusion mutua automatica al entrar.
- Java usa `synchronized` como keyword que convierte un metodo en procedimiento de monitor.
- Leer el codigo Java: `wait()` libera el lock y suspende; `notifyAll()` despierta a todos para que re-evaluen.
- Destacar el patron `while (condicion) wait()` — siempre `while`, nunca `if`.

**Conceptos clave:** monitor, sincronizado, wait, notifyAll, spurious wakeup, while-not-if.

**Preguntas anticipadas:**

- "synchronized es como volatile?" → No; `volatile` garantiza visibilidad; `synchronized` garantiza exclusion mutua y visibilidad.
- "Por que notifyAll y no notify?" → Con `notify` puede despertar a la unidad equivocada; con `notifyAll` todas re-evaluan la condicion.

**Transicion:** Para mayor control sobre las condiciones de espera, se pueden usar variables de condicion explicitas.

---

### [F-12] Monitores con variables de condicion

**Tiempo:** 4 min

**Que decir:**

- Mostrar `ReentrantLock` + `Condition` como alternativa mas expresiva a `synchronized`.
- Dos condiciones separadas: `noVacio` para el consumidor, `noLleno` para el productor.
- `await()` equivale a `wait()` pero sobre una condicion especifica → mas eficiente que `notifyAll`.
- `signal()` despierta solo a quien espera en ESA condicion — no a todos.
- El `finally { lock.unlock() }` garantiza que el lock siempre se libera incluso si hay excepcion.

**Conceptos clave:** ReentrantLock, Condition, await, signal, finally-unlock.

**Preguntas anticipadas:**

- "Que ventaja tiene sobre synchronized?" → Condiciones separadas, tryLock con timeout, posibilidad de interrumpir la espera.

**Transicion:** Hay otro modelo de coordinacion que evita el estado compartido directamente: el pasaje de mensajes.

---

### [F-13] Pasaje de mensajes: modelo conceptual (Sebesta 13.5)

**Tiempo:** 3 min

**Que decir:**

- Usar el diagrama: las unidades no comparten dato; intercambian mensajes.
- El estado queda local → no hay seccion critica por defecto.
- Las dos operaciones basicas: `send` y `receive` — quien envia, quien recibe.
- El protocolo se vuelve explicito en el codigo.
- Erlang y Go hacen de esto su principio central de diseno.

**Conceptos clave:** pasaje de mensajes, estado local, send, receive, protocolo explicito.

**Preguntas anticipadas:**

- "Mensajes siempre es mejor?" → No; copiar datos tiene costo. Para grandes volumenes de datos compartidos, puede ser menos eficiente.

**Transicion:** El modelo de mensajes tiene variantes segun cuando bloquea el emisor: sincrono vs asincrono.

---

### [F-14] Mensajes sincronicos, asincronicos y canales

**Tiempo:** 3 min

**Que decir:**

- Leer la tabla fila por fila: que pasa con el emisor y con el receptor en cada caso.
- Canal sin buffer (Go default) = sincrono: el emisor espera hasta que el receptor acepta.
- Canal bufferizado (Go `make(chan T, N)`) = asincrono con capacidad: el emisor continua si hay lugar.
- Asincrono puro (Erlang `!`): el emisor nunca espera; el mensaje va a la cola del receptor.
- TypeScript MessageChannel se comporta como canal asincrono; BroadcastChannel es fan-out a todos los suscriptores.
- La eleccion del modelo cambia cuanto puede avanzar cada unidad de manera independiente.

**Conceptos clave:** mensaje sincrono, asincrono, bufferizado, canal sin buffer.

**Preguntas anticipadas:**

- "Que pasa si el buffer se llena?" → El emisor bloquea como si fuera sincrono. Hay que diseñar el protocolo para eso.

**Transicion:** TypeScript tiene su propio modelo de pasaje de mensajes con ciclo de vida controlable. Veamos AbortController.

---

### [F-15] TypeScript: cancelacion estructurada con AbortController

**Tiempo:** 5 min

**Que decir:**

- Presentar AbortController como la pieza que TypeScript agrega para controlar el ciclo de vida de operaciones asincronas.
- `controller.abort()` cancela todas las operaciones que reciban la misma `signal` — un mecanismo de cancelacion estructurada.
- Leer el patron de timeout: crear el controller, setear un timer que llame `abort()`, pasar `signal` al `fetch`.
- El `finally { clearTimeout(timer) }` garantiza limpieza tanto en exito como en falla.
- Mostrar la propagacion: `signal` se pasa de funcion en funcion, igual que se propaga la cancelacion en coroutineScope de Kotlin.
- Conectar con la idea de structured concurrency: el padre (controller) controla el ciclo de vida de sus hijos (todas las operaciones que usen esa signal).

**Conceptos clave:** AbortController, signal, timeout, propagacion de cancelacion, structured concurrency en TS.

**Preguntas anticipadas:**

- "Puedo abortar una Promise cualquiera?" → Solo si la implementacion chequea `signal.aborted` o acepta `{ signal }`. Las Promises nativas de JS no tienen cancelacion integrada.
- "Esto existe en el browser?" → Si; `AbortController` esta disponible en todos los browsers modernos y en Node.js.

**Transicion:** TypeScript tambien tiene canales de mensajes reales: MessageChannel y BroadcastChannel.

---

### [F-16] TypeScript: MessageChannel y BroadcastChannel

**Tiempo:** 4 min

**Que decir:**

- `MessageChannel` crea un canal privado con dos extremos (`port1`, `port2`) — es el equivalente TypeScript de un canal de Go sin buffer, pero asincrono.
- Leer el ejemplo: `port1.onmessage` recibe, `port2.postMessage` envia; se puede transferir `port2` a un Worker (transferencia de ownership del recurso).
- `BroadcastChannel` es fan-out: todos los contextos del mismo origen que tengan el mismo nombre reciben el mensaje — como `notifyAll` pero entre tabs y workers.
- Conectar con el modelo de pasaje de mensajes de Sebesta 13.5: el estado queda en cada contexto, la coordinacion es por mensajes.
- La transferencia `worker.postMessage({ canal: port2 }, [port2])` ilustra el concepto de mover un recurso sin copiarlo — puente hacia el concepto de ownership de Rust.

**Conceptos clave:** MessageChannel, port, BroadcastChannel, transferencia de ownership, fan-out.

**Preguntas anticipadas:**

- "MessageChannel es sincrono o asincrono?" → Asincrono; los mensajes se entregan a traves del event loop.
- "Puedo usar esto entre tabs del browser?" → BroadcastChannel si; MessageChannel requiere pasar los ports explicitamente.

**Transicion:** Para cerrar el arco de lenguajes, veamos Rust: el unico lenguaje donde el compilador mismo garantiza que no hay data races.

---

### [F-17] Rust: el compilador como garante de la concurrencia

**Tiempo:** 4 min

**Que decir:**

- Explicar el contraste con TypeScript: en TS la seguridad de concurrencia depende del programador; en Rust el compilador rechaza el codigo inseguro.
- `Arc<Mutex<T>>`: Arc es puntero con conteo de referencias thread-safe; Mutex<T> es el dato envuelto — el lock es parte del TIPO, no una convencion.
- Mostrar que el lock se libera automaticamente al salir del scope (RAII: Resource Acquisition Is Initialization) — equivalente al `defer Unlock()` de Go pero garantizado por el compilador.
- Leer el ejemplo del error: intentar compartir datos sin `Send` — el compilador rechaza el codigo antes de ejecutarlo.
- Conectar con la tabla comparativa que viene: TypeScript requiere disciplina; Rust da garantia pero cuesta verbosidad.
- Mencionar que Rust tiene canales (`mpsc::channel`) para pasaje de mensajes igual que Go.

**Conceptos clave:** Arc, Mutex<T>, RAII, Send trait, Sync trait, garantia en tiempo de compilacion.

**Preguntas anticipadas:**

- "Vale la pena aprender Rust solo para la concurrencia?" → Para sistemas, drivers o WebAssembly critico, si. Para web backends, TypeScript/Go/Kotlin suelen ser suficientes.
- "Rust tiene async/await?" → Si; tambien tiene async/await y futures, pero son mas complejos de usar que en TS o Kotlin.

**Transicion:** Pasamos a Java — el lenguaje que la mayoria conoce mejor para el tema de threads.

---

### [F-18] Java Thread y Runnable (Sebesta 13.7)

**Tiempo:** 4 min

**Que decir:**

- Dos formas de crear un thread: extender Thread (sencilla pero limita herencia) o implementar Runnable (preferida, separa logica de mecanismo).
- Leer la lambda como forma moderna de Runnable: la tarea es el bloque de codigo, el Thread es el mecanismo.
- `start()` crea el thread del OS y llama `run()` en el; `join()` espera que termine.
- Advertencia: llamar `run()` directamente no crea un nuevo thread — ejecuta en el thread actual.
- Java `java.util.concurrent.Executors` va a aparecer en la filmina siguiente como forma de no crear threads crudos.

**Conceptos clave:** Thread, Runnable, start, join, no llamar run directamente.

**Preguntas anticipadas:**

- "Lambda Runnable y Thread class son equivalentes?" → La logica si; la forma de Runnable es mas composable con el ecosistema de java.util.concurrent.

**Transicion:** Con threads creados, vemos como Java implementa monitores con synchronized y wait/notify.

---

### [F-19] Java synchronized, wait y notify (Sebesta 13.7)

**Tiempo:** 4 min

**Que decir:**

- `synchronized` en un metodo convierte ese metodo en procedimiento de monitor: solo un thread a la vez.
- `wait()` hace dos cosas: libera el lock del objeto y suspende — las dos a la vez, atomicamente.
- `notifyAll()` despierta a todos los threads suspendidos en ese objeto para que re-evaluen la condicion.
- El patron `while (condicion) wait()` protege contra spurious wakeups.
- Leer el BufferCircular como implementacion completa de productor/consumidor en Java.
- Conectar con el monitor abstracto de Sebesta 13.4: los procedimientos son insert/remove, las condiciones son lleno/vacio.

**Conceptos clave:** synchronized, wait, notifyAll, while-not-if, spurious wakeup.

**Preguntas anticipadas:**

- "Si notify despierta solo a uno, por que usamos notifyAll?" → Porque no sabemos si la que despierta es exactamente la que puede continuar. Con notifyAll todas re-evaluan.

**Transicion:** Java 5 agrego java.util.concurrent con abstracciones mas expresivas. Repaso rapido.

---

### [F-20] Java java.util.concurrent: herramientas modernas

**Tiempo:** 4 min

**Que decir:**

- Leer la tabla como menu: cada clase resuelve un problema especifico.
- `ExecutorService` es la forma moderna de manejar threads: pool reutilizable, no crear crudos.
- `Future<T>` encapsula un resultado asincrono: `get()` espera y retorna o lanza excepcion.
- `ReentrantLock` da tryLock con timeout — imposible con `synchronized`.
- `AtomicInteger.incrementAndGet()` es la alternativa sin lock para contadores simples.
- Leer el ejemplo del pool: submit envia tareas, get espera resultados, shutdown cierra el pool.

**Conceptos clave:** ExecutorService, Future, ReentrantLock, AtomicInteger, pool de threads.

**Preguntas anticipadas:**

- "CompletableFuture reemplaza a Promise en Java?" → Se usa de forma similar; permite encadenar operaciones asincronas con thenApply, thenCombine, etc.

**Transicion:** C# tiene un modelo muy parecido a Java pero con sintaxis mas integrada en el lenguaje.

---

### [F-21] C# threads, lock y Task (Sebesta 13.8)

**Tiempo:** 3 min

**Que decir:**

- `lock(obj) { }` es la contraparte de `synchronized` en Java, pero como statement, no como keyword de metodo.
- `Monitor.Wait` / `Monitor.Pulse` son los equivalentes de `wait`/`notify` en C#.
- C# 5 integro `async`/`await` en el lenguaje antes que Java; `Task` es mas ergonomico que `Future`.
- `Task.WhenAll` es el equivalente a `Promise.all` de TypeScript o `CompletableFuture.allOf` de Java.
- Mencionar brevemente que la idea de C# es que `async`/`await` sea la abstraccion preferida sobre threads crudos.

**Conceptos clave:** lock, Monitor.Wait, Task, async/await en C#, Task.WhenAll.

**Preguntas anticipadas:**

- "C# tiene algo como goroutines?" → No directamente; las corrutinas de C# (async/await) son mas parecidas a Kotlin que a Go.

**Transicion:** Erlang va en direccion opuesta: elimina el estado compartido por diseno. Sin locks, sin monitores.

---

### [F-22] Erlang y actores: sin estado compartido (Sebesta 13.9)

**Tiempo:** 4 min

**Que decir:**

- El modelo de actores de Erlang es: cada proceso tiene estado propio; nadie mas lo toca; comunicacion solo por mensajes asincronicos.
- Leer la sintaxis Erlang: `spawn` crea proceso, `receive` espera mensajes, `!` envia mensajes.
- El estado del contador esta en el parametro recursivo de la funcion — no en una variable global.
- Destacar: si un proceso falla, los demas siguen — fault isolation por diseno.
- Mencionar Elixir como heredero moderno de Erlang (misma VM, sintaxis mas amigable).
- Akka en Scala/Java y el modelo de actores de Go (goroutines + channels) son influencias directas.

**Conceptos clave:** actor, proceso Erlang, spawn, receive, send (!), fault isolation.

**Preguntas anticipadas:**

- "Si no hay estado compartido, como coordino?" → Mediante el protocolo de mensajes. El estado esta en la "cabeza" de cada proceso.

**Transicion:** Antes de pasar a los lenguajes modernos, un tipo especial de concurrencia que el compilador puede explotar solo.

---

### [F-23] Concurrencia a nivel de sentencias: FORALL y HPF (Sebesta 13.10)

**Tiempo:** 3 min

**Que decir:**

- Explicar el contexto: en computo cientifico sobre arreglos, cada iteracion suele ser independiente.
- FORALL en HPF declara esa independencia y el compilador/runtime puede paralelizar automaticamente.
- `parallelStream()` en Java es el equivalente moderno: el programador declara independencia, el runtime elige cuantos threads usar.
- La responsabilidad del programador es garantizar que no hay dependencias ocultas entre iteraciones (lo que el compilador no puede probar en general).
- Este mecanismo esta en Sebesta 13.10 como caso especial; no se estudia en profundidad en este curso.

**Conceptos clave:** statement-level concurrency, FORALL, HPF, parallelStream, independencia de iteraciones.

**Preguntas anticipadas:**

- "OpenMP hace esto en C?" → Si; `#pragma omp parallel for` es el equivalente en C/C++ con directivas de compilador.

**Transicion:** Volvemos a los lenguajes del dia a dia: Go con goroutines y canales.

---

### [F-24] Go goroutines y channels

**Tiempo:** 5 min

**Que decir:**

- Goroutines son baratas (~2 KB de stack inicial); el scheduler de Go las multiplexa sobre threads del OS.
- Un channel es tipado: `chan int` solo puede llevar enteros — el compilador detecta errores de tipo.
- `close(out)` es la señal de que no se enviaran mas valores; `range canal` itera hasta que el canal se cierra.
- `sync.WaitGroup` permite esperar que un grupo de goroutines termine — `Add(2)`, `Done()` en cada goroutine, `Wait()` para bloquear.
- Leer el ejemplo completo: `generarNumeros` envia, `imprimirNumeros` recibe, el canal es el punto de sincronizacion.
- Conectar con el pasaje de mensajes de Sebesta: el estado queda en cada goroutine; el canal coordina.

**Conceptos clave:** goroutine, channel tipado, close, range, WaitGroup.

**Preguntas anticipadas:**

- "Un channel sin buffer es sincrono?" → Si; el emisor espera hasta que el receptor acepta — es un punto de sincronizacion, como los canales sin buffer de Go y MessageChannel en TypeScript.

**Transicion:** Go tambien tiene mutex para cuando si se necesita compartir memoria. No todo es channels.

---

### [F-25] Go select y sync.Mutex

**Tiempo:** 3 min

**Que decir:**

- `select` elige el primer canal disponible — como `select` del sistema operativo pero integrado en el lenguaje.
- `case <-timeout` implementa un timeout: si ninguna goroutine comunico en N segundos, hacer algo.
- `sync.Mutex` con `defer Unlock()` es el patron idiomatico en Go para proteger estructuras compartidas.
- `defer` garantiza que el Unlock se llama incluso si la funcion hace `return` o panica.
- La regla de Go: channels para transferir datos y señalar eventos; mutex para proteger estado cuando realmente se necesita compartir.

**Conceptos clave:** select de Go, defer Unlock, channels vs mutex, timeout.

**Preguntas anticipadas:**

- "Por que no usar siempre channels?" → Para contadores simples o caches, el mutex es mas simple y eficiente que diseñar un protocolo de mensajes.

**Transicion:** Kotlin resuelve el ciclo de vida y la cancelacion con structured concurrency.

---

### [F-26] Kotlin corrutinas y concurrencia estructurada

**Tiempo:** 4 min

**Que decir:**

- `coroutineScope { }` garantiza que ninguna corrutina hija escapa del scope: si el padre se cancela, todas las hijas se cancelan.
- `async { }` lanza una corrutina hija y devuelve un `Deferred`; `.await()` suspende sin bloquear el thread.
- Si cualquier `async` dentro del scope falla, el scope cancela las demas automaticamente.
- Los dispatchers separan "que hacer" de "donde hacerlo": IO, Default (CPU), Main (UI).
- Conectar con el concepto de ciclo de vida estructurado: `coroutineScope` garantiza que las corrutinas hijas no escapan del scope padre, igual que `AbortController` en TypeScript controla el ciclo de vida de las operaciones hijas.

**Conceptos clave:** coroutineScope, async, await, Deferred, dispatchers, cancelacion en cascada.

**Preguntas anticipadas:**

- "Kotlin coroutines son threads?" → No directamente; el runtime decide sobre cuantos threads corren las corrutinas, segun el dispatcher.

**Transicion:** De vuelta a TypeScript: el modelo de ejecucion que subyace a todo lo que ya conocen.

---

### [F-27] TypeScript y el event loop de JavaScript

**Tiempo:** 3 min

**Que decir:**

- JavaScript tiene un solo thread de ejecucion por defecto para el codigo del programa.
- El event loop toma tareas de la cola y ejecuta cada una hasta que termina o hace `await`.
- `await` suspende el handler actual y devuelve el control al event loop — otros handlers pueden correr.
- Consecuencia: dos `await` sobre I/O diferente pueden estar "en vuelo" al mismo tiempo, pero el codigo del programa no corre en paralelo.
- Mostrar el ejemplo: `fetch(a)` y `fetch(b)` se inician antes de `await` — dos requests en vuelo, un solo handler activo.

**Conceptos clave:** event loop, single thread JS, await como suspension, handlers concurrentes de I/O.

**Preguntas anticipadas:**

- "Node.js es single-threaded?" → El loop de eventos lo es; hay threads internos para I/O del OS, pero el codigo JS corre en uno.

**Transicion:** La composicion de Promises es la forma idiomatica de coordinar multiples esperas.

---

### [F-28] async/await, Promise.all y Promise.allSettled

**Tiempo:** 3 min

**Que decir:**

- `Promise.all`: espera todas o falla al primer rechazo — ideal cuando TODAS las respuestas son necesarias.
- `Promise.allSettled`: espera todas sin importar si alguna falla — ideal para verificar N servicios y colectar estado de cada uno.
- `Promise.race`: devuelve la primera que resuelve o rechaza — patron clasico de timeout.
- Leer el ejemplo de timeout: `Promise.race` entre la promesa real y una que rechaza despues de N ms.
- Advertir: con `Promise.race`, si la promesa "real" termina tarde, la operacion sigue corriendo en background — hay que cancelarla explicitamente si importa.

**Conceptos clave:** Promise.all, Promise.allSettled, Promise.race, patron timeout.

**Preguntas anticipadas:**

- "Como cancelo una Promise?" → No hay cancelacion nativa en JS; se usa AbortController para I/O o flags manuales.

**Transicion:** Para trabajo CPU-bound que bloquea el event loop, necesitamos Workers.

---

### [F-29] worker_threads: paralelismo real en Node.js

**Tiempo:** 4 min

**Que decir:**

- Workers son threads del OS que corren V8 independiente — paralelismo real para CPU-bound.
- El mismo archivo puede ser main thread y worker con el flag `isMainThread`.
- `workerData` pasa datos al worker en la creacion; `parentPort.postMessage` devuelve resultados.
- `SharedArrayBuffer` + `Atomics` permite memoria compartida con operaciones atomicas — como `java.util.concurrent.atomic` en Java.
- `Atomics.wait` / `Atomics.notify` implementan un primitivo de sincronizacion similar a `wait`/`notifyAll` de monitores, pero sobre un array compartido.
- Cuando usar: hashing, compresion, ML inference, procesamiento de imagenes — no para I/O.

**Conceptos clave:** worker_threads, SharedArrayBuffer, Atomics, CPU-bound, isMainThread.

**Preguntas anticipadas:**

- "Workers comparten el mismo heap?" → No el heap principal; con SharedArrayBuffer se puede compartir un segmento de memoria explicitamente.

**Transicion:** Con todos los mecanismos vistos, la decision de cual usar depende del problema.

---

### [F-30] Mapa de decisiones: elegir el mecanismo correcto

**Tiempo:** 4 min

**Que decir:**

- Leer la tabla como checklist de decision, no como regla rigida.
- Para esperar N servicios externos: `Promise.all` o equivalente asincrono — el costo dominante es espera de I/O.
- Para computo CPU-intensivo: Workers/ExecutorService — el costo dominante es calculo.
- Para contadores compartidos: Atomics/synchronized/lock — identificar la seccion critica.
- Para productor/consumidor desacoplado: BlockingQueue (Java), channel (Go) o condicion de monitor.
- Para ciclo de vida con cancelacion: corrutinas estructuradas (Kotlin, C# async).
- Para modelo sin estado compartido: actores (Erlang, Akka).
- Insistir: en un sistema real pueden coexistir varios mecanismos; lo importante es no confundir que resuelve cada uno.

**Conceptos clave:** I/O-bound vs CPU-bound, eleccion por problema, mezcla de mecanismos.

**Preguntas anticipadas:**

- "Como aprendo a elegir bien?" → Identificar primero el tipo de problema; despues el mecanismo. No al reves.

**Transicion:** Una tabla comparativa de todos los lenguajes vistos para llevarse de la clase.

---

### [F-31] Comparativa de lenguajes: el arco completo de Sebesta

**Tiempo:** 3 min

**Que decir:**

- Leer la tabla como arco de diseno: Java/C# en un extremo (monitores clasicos + abstracciones modernas), Rust en el otro (garantia del compilador sin GC).
- Java y C# son el centro: monitores clasicos + abstracciones modernas coexisten en el mismo lenguaje.
- Go: channels preferidos, mutex disponible.
- Kotlin: structured concurrency resuelve lifecycle, cancelacion y errores.
- TypeScript: la responsabilidad de la sincronizacion queda en el desarrollador; AbortController + MessageChannel + Atomics son las piezas clave.
- Rust: unico lenguaje de la tabla donde el compilador garantiza la ausencia de data races.
- Concluir: cada lenguaje no solo da herramientas — tambien orienta como pensar el problema concurrente.

**Conceptos clave:** espectro de decision de lenguajes, garantias del lenguaje vs del programador.

**Preguntas anticipadas:**

- "Cual es el mejor modelo?" → Depende del problema, del equipo y de las garantias buscadas. No hay respuesta universal.

**Transicion:** Cierre con el mapa conceptual de toda la clase.

---

### [F-32] Cierre: lo que la clase deja

**Tiempo:** 3 min

**Que decir:**

- Repasar las tres capas: vocabulario (cuatro preguntas distintas), mecanismos (semaforos → monitores → mensajes), lenguajes (Java → C# → Go → Kotlin → TypeScript → Erlang → Rust).
- Enunciar las cuatro preguntas que el programador debe responder ante un problema concurrente.
- Anunciar el TP: implementar productor/consumidor en TypeScript usando Atomics + SharedArrayBuffer.
- Mencionar la opcion de contraste: el mismo problema en Go (channels) o Java (BlockingQueue).
- Cerrar con la idea de Sebesta: la concurrencia es una propiedad de los lenguajes, no solo de los sistemas operativos.

**Conceptos clave:** tres capas del tema, cuatro preguntas de decision, arco de Sebesta.

**Preguntas anticipadas:**

- "Que entra a la evaluacion?" → Distinguir conceptos, detectar carreras, justificar mecanismos — no memorizar APIs.

**Transicion:** Siguiente clase: cierre de cursada con integracion de paradigmas y criterios de eleccion de lenguaje.

---

## Cierre

**Resumen:** La clase separo tres capas del tema concurrencia: vocabulario conceptual (Sebesta 13.1–13.2), mecanismos clasicos y formales (semaforos, monitores, mensajes — Sebesta 13.3–13.5), y lenguajes concretos que implementan esos mecanismos de manera diferente (Java, C#, Go, Kotlin, TypeScript, Erlang, Rust — Sebesta 13.7–13.10). El hilo conductor fue el caso TOTAL roto de Sebesta p.540 hasta la decision de que mecanismo usar segun el problema. TypeScript fue el ancla: se cubrieron async/await, Promise.all, workers, Atomics, AbortController y MessageChannel.

**Anuncio del TP:** Implementar productor/consumidor en TypeScript con Atomics + SharedArrayBuffer; opcional: comparar con Go (channels) o Java (BlockingQueue con condiciones).

**Proxima clase:** Cierre de cursada — integracion de paradigmas, criterios de eleccion de lenguaje y retrospectiva del cursado.

