# Filminas - Tema 15: Concurrencia y Paralelismo

## PORTADA

---

### [F-00] Concurrencia y Paralelismo

@tipo: portada
@imagen: none

# Concurrencia y Paralelismo

## Tema 15 — Modulo XI

- Lenguaje principal: TypeScript
- Contrastes: Java, C#, Go, Kotlin, Erlang, Rust
- Pregunta guia: que puede avanzar a la vez y que debe coordinarse?
- Recorrido: fundamentos, sincronizacion, modelos de comunicacion y lenguajes modernos

---

## BLOQUE A — Vocabulario y frontera conceptual

---

### [F-01] Un resultado que cambia solo con el orden

@tipo: socratica
@imagen: none

# Si dos unidades modifican el mismo dato, quien decide el valor final?

## El caso TOTAL

```
TOTAL := 3                       -- valor inicial compartido

-- Tarea A                       -- Tarea B
x := TOTAL  -- lee 3             x := TOTAL  -- lee 3
x := x + 1  -- calcula 4         x := x * 2  -- calcula 6
TOTAL := x  -- escribe 4         TOTAL := x  -- escribe 6
```

- Si A completa antes que B: resultado = 6
- Si B completa antes que A: resultado = 4
- Si se intercalan (interleaving): puede ser 4, 6, 7 u 8
- Leer–calcular–escribir **no es una operacion atomica**
- El problema no es el lenguaje: es estado compartido sin coordinacion

---

### [F-02] Concurrencia, paralelismo, asincronia y threads: cuatro preguntas distintas

@tipo: tabla-comparativa
@imagen: none

# No son sinonimos; cada termino responde una pregunta diferente

| Termino | Pregunta que responde | Ejemplo concreto |
|---------|----------------------|------------------|
| Concurrencia | ¿Varias actividades progresan solapadas? | Dos tareas alternando en un nucleo |
| Paralelismo | ¿Ejecutan simultaneamente en hardware? | Dos nucleos corriendo al mismo tiempo |
| Asincronia | ¿Puedo continuar mientras espero? | `await fetch(url)` sin bloquear |
| Thread | ¿Quien ejecuta instrucciones? | Unidad de ejecucion del OS |

## Lo que importa para este curso

- Un programa puede ser **concurrente sin ser paralelo** (un nucleo, multitarea)
- Un programa puede ser **asincrono sin ser concurrente** (single event loop, un handler a la vez)
- **Paralelismo necesita hardware multiple**; concurrencia no
- El foco de esta clase es la *concurrencia a nivel de subprogramas*

---

### [F-03] Concurrencia fisica vs concurrencia logica

@tipo: concepto-abstracto
@imagen: none

# El hardware y el lenguaje ofrecen dos niveles de concurrencia

## Concurrencia fisica

- Requiere multiprocesadores o multinucleo
- Ejecucion simultanea efectiva
- El runtime mapea tareas logicas a nucleos disponibles

## Concurrencia logica (multiprogramacion)

- Un solo nucleo intercala tareas rapidamente
- El programador ve avance simultane
- El scheduler decide el orden real
- Es **la abstraccion central para razonar sobre concurrencia en lenguajes**

## Por que importa la distincion

- Un programa correcto en logica debe serlo independientemente del hardware
- Las condiciones de carrera aparecen **en ambos niveles**

---

### [F-04] Concurrencia a nivel de subprogramas

@tipo: concepto-abstracto
@imagen: none

# Un programa se divide en unidades que avanzan independientemente

## La idea central

- La unidad concurrente puede ser una **tarea, un thread, un proceso liviano o una corrutina**
- El nombre no importa; lo que importa es el **avance independiente**
- El lenguaje define que operaciones se permiten y como se coordinan
- El runtime decide cuanto de eso se ejecuta en paralelo real

## Dos preguntas que el lenguaje debe responder

1. **¿Como se crean las unidades concurrentes?** (palabras reservadas, librerias, corrutinas)
2. **¿Como se sincronizan y comunican?** (semaforos, monitores, mensajes, canales)

## Consecuencias de diseno

- Lenguajes con soporte nativo (Go, Rust) hacen visible la concurrencia en la sintaxis
- Lenguajes con librerias (Java, C#) la delegan a clases y frameworks
- Lenguajes funcionales (Erlang) eliminan el estado compartido y usan mensajes

---

### [F-05] Tarea, thread, proceso y corrutina como unidades concurrentes

@tipo: tabla-comparativa
@imagen: none

# Separar concepto, mecanismo y costo de creacion evita confusiones

| Unidad | Nivel | Memoria | Costo creacion | Lenguajes tipicos |
|--------|-------|---------|----------------|-------------------|
| Tarea (task) | Logico/concurrente | Comparte con proceso | Bajo-medio | Modelo conceptual del tema |
| Thread | OS o runtime | Comparte heap del proceso | Medio | Java, C#, C++, TypeScript workers |
| Proceso | OS | Espacio propio | Alto | C, Unix fork, microservicios |
| Goroutine | Runtime (Go) | Stack dinamico propio | Muy bajo (~2 KB) | Go |
| Corrutina | Lenguaje | Stack suspendible | Muy bajo | Kotlin, Python, Dart, TypeScript |

## Que comparten los threads pero no los procesos

- Heap, variables globales y descriptores de archivo
- Por eso la condicion de carrera existe: comparten estado mutable

---

### [F-06] Condicion de carrera: anatomia del problema

@tipo: demo
@imagen: none

# El error nace en la ilusoria atomicidad de leer-calcular-escribir

## En TypeScript con workers compartidos

```ts
// SharedArrayBuffer compartido entre workers
const sab = new SharedArrayBuffer(4);
const arr = new Int32Array(sab);
arr[0] = 3;

// Worker A                    // Worker B
const x = arr[0];  // lee 3   const x = arr[0];  // lee 3
arr[0] = x + 1;    // = 4     arr[0] = x * 2;    // = 6
// resultado final: 4 o 6, dependiendo del interleaving
```

## En Java con threads

```java
class Contador {
  int total = 3;

  void incrementar() { total = total + 1; } // no atomico
  void duplicar()    { total = total * 2; } // no atomico
}
```

## Tres condiciones para que haya carrera

1. Existe estado compartido mutable
2. Al menos dos unidades lo acceden concurrentemente
3. Al menos una lo modifica

---

## BLOQUE B — Mecanismos de sincronizacion clasicos

---

### [F-07] Sincronizacion de competencia: la seccion critica

@tipo: concepto-abstracto
@imagen: none

# La seccion critica es la region donde el interleaving importa

## Definicion

- **Seccion critica**: segmento de codigo que accede a un recurso compartido y **no debe ejecutarse concurrentemente** por mas de una tarea
- **Exclusion mutua**: solo una tarea puede estar dentro de la seccion critica a la vez

## Cuatro propiedades que debe garantizar cualquier solucion

1. **Exclusion mutua**: como maximo una unidad dentro
2. **Progreso**: si nadie esta adentro y alguien quiere entrar, debe poder
3. **Espera acotada**: nadie espera indefinidamente si el recurso esta libre periodicamente
4. **Sin suposicion de velocidad**: la solucion funciona independientemente del scheduling

## Por que no alcanza con un flag booleano simple

- Leer el flag y setearlo no es atomico → se puede generar carrera sobre el propio mecanismo

---

### [F-08] Semaforos: el mecanismo clasico de Dijkstra

@tipo: concepto-mixto
@imagen: none

# Un semaforo coordina acceso con un contador entero y una cola de espera

## Operaciones fundamentales

```
wait(s):
  si contador(s) > 0 entonces
    contador(s) := contador(s) - 1
  si no
    suspender tarea actual en cola(s)
  fin

release(s):
  si cola(s) no esta vacia entonces
    despertar primera tarea de cola(s)
  si no
    contador(s) := contador(s) + 1
  fin
```

## Dos usos canonicos

- **Semaforo binario (contador=1)**: exclusion mutua → actua como mutex
- **Semaforo contador (contador=N)**: limita N accesos simultaneos a un recurso

## Propiedad clave

- `wait` y `release` son operaciones **atomicas** — el hardware garantiza que no hay interleaving dentro de ellas
- El programador es responsable de usar el protocolo correctamente

---

### [F-09] Semaforos en codigo: exclusion mutua y cooperacion

@tipo: codigo
@imagen: none

# El semaforo resuelve competencia y cooperacion con el mismo mecanismo

## Exclusion mutua con Atomics en TypeScript (workers)

```ts
// SharedArrayBuffer compartido entre workers
const sab = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT);
const mutex = new Int32Array(sab); // 0 = libre, 1 = tomado

function adquirir(): void {
  // compareExchange atomico: si es 0, setear a 1 y continuar
  while (Atomics.compareExchange(mutex, 0, 0, 1) !== 0) {
    Atomics.wait(mutex, 0, 1); // suspender hasta que alguien libere
  }
}

function liberar(): void {
  Atomics.store(mutex, 0, 0); // liberar
  Atomics.notify(mutex, 0, 1); // despertar un waiter
}

// Uso: seccion critica protegida
adquirir();
total = total + 1;
liberar();
```

## Sincronizacion de cooperacion: productor/consumidor

```
-- Semaforos: lleno y vacio
vacio : Semaphore := N;   -- cuantos lugares quedan libres
lleno : Semaphore := 0;   -- cuantos elementos hay disponibles

Productor:                 Consumidor:
  loop                       loop
    producir(item)             Wait(lleno)
    Wait(vacio)                Wait(mutex)
    Wait(mutex)                item := extraer()
    insertar(item)             Release(mutex)
    Release(mutex)             Release(vacio)
    Release(lleno)             consumir(item)
  end loop                   end loop
```

- Un semaforo resuelve **competencia** (mutex) y **cooperacion** (lleno/vacio) por separado
- Combinar mal los Wait puede causar **deadlock**

---

### [F-10] Errores tipicos con semaforos y su consecuencia

@tipo: tabla
@imagen: none

# El poder del semaforo es proporcional al riesgo de usarlo mal

| Error de protocolo | Causa | Efecto observable |
|--------------------|-------|-------------------|
| Olvidar `release` tras `wait` | El programador omite la llamada | Deadlock permanente |
| `release` sin `wait` previo | Logica incorrecta | Otro thread entra en seccion critica — dato corrupto |
| `wait` y `release` en orden invertido | Error de diseno | Deadlock o corrupcion segun timing |
| Seccion critica demasiado pequeña | Protege solo parte del acceso | Carrera sobre el resto del codigo |
| Seccion critica demasiado grande | Protege mas de lo necesario | Serializa trabajo que podria ser paralelo |
| Semaforo compartido entre modulos distintos | Acoplamiento implicito | Bloqueo inesperado desde codigo remoto |

## Por que los monitores existen

- Los errores de semaforos **no son detectables por el compilador**
- Los monitores encapsulan el estado y hacen el protocolo **estructural**, no opcional

---

### [F-11] Monitores: encapsulamiento y exclusion automatica

@tipo: concepto-mixto
@imagen: none

# Un monitor protege estado compartido con exclusion garantizada por el lenguaje

## Modelo de Hoare

Un monitor es una abstraccion con tres partes:
1. **Estado privado**: solo accesible desde dentro del monitor
2. **Procedimientos sincronizados**: la entrada al monitor garantiza exclusion mutua automatica
3. **Variables de condicion**: permiten que una tarea espere dentro del monitor sin bloquear a otras

## Monitor en Java (keyword `synchronized`)

```java
class BufferMonitor<T> {
  private final Queue<T> cola = new ArrayDeque<>();
  private final int capacidad;

  BufferMonitor(int cap) { this.capacidad = cap; }

  synchronized void insertar(T item) throws InterruptedException {
    while (cola.size() == capacidad) wait();  // espera si lleno
    cola.add(item);
    notifyAll();                               // avisa que hay dato
  }

  synchronized T extraer() throws InterruptedException {
    while (cola.isEmpty()) wait();            // espera si vacio
    T item = cola.poll();
    notifyAll();                              // avisa que hay lugar
    return item;
  }
}
```

- `synchronized` es la palabra que convierte el metodo en procedimiento de monitor
- `wait()` suspende dentro del monitor **y libera el lock temporalmente**
- `notifyAll()` despierta a todos los que esperan para que re-evaluen la condicion

---

### [F-12] Monitores con variables de condicion: cooperacion explicita

@tipo: concepto-mixto
@imagen: none

# Las variables de condicion permiten coordinar el orden de ejecucion dentro del monitor

## Variables de condicion

- Permiten a una tarea **esperar** dentro del monitor hasta que se cumpla una condicion
- Dos operaciones: `wait(c)` — suspender en cola de c; `signal(c)` — despertar una tarea de c
- `wait(c)` **libera el lock del monitor** mientras espera (diferencia clave con semaforo)

## Productor/consumidor con `java.util.concurrent`

```java
import java.util.concurrent.locks.*;

class BufferCondicion<T> {
  private final Queue<T> cola = new ArrayDeque<>();
  private final Lock lock = new ReentrantLock();
  private final Condition noVacio = lock.newCondition();
  private final Condition noLleno = lock.newCondition();
  private final int cap;

  void insertar(T item) throws InterruptedException {
    lock.lock();
    try {
      while (cola.size() == cap) noLleno.await(); // esperar lugar
      cola.add(item);
      noVacio.signal();                            // avisar al consumidor
    } finally { lock.unlock(); }
  }

  T extraer() throws InterruptedException {
    lock.lock();
    try {
      while (cola.isEmpty()) noVacio.await();      // esperar dato
      T item = cola.poll();
      noLleno.signal();                            // avisar al productor
      return item;
    } finally { lock.unlock(); }
  }
}
```

- Usar condiciones separadas (`noVacio`, `noLleno`) es mas eficiente que `notifyAll`
- El patron `while (condicion) await()` — nunca `if` — protege contra spurious wakeups

---

### [F-13] Pasaje de mensajes: comunicar en lugar de compartir

@tipo: diagrama
@imagen: none

# El estado queda local; la coordinacion ocurre mediante mensajes

## Modelo

- Cada unidad concurrente tiene **estado local privado**
- Las unidades se coordinan enviando y recibiendo **mensajes**
- No hay memoria compartida visible → no hay seccion critica por defecto

## Dos operaciones basicas

```
send(destino, mensaje)   -- enviar un mensaje a una unidad
receive(origen, mensaje) -- recibir un mensaje desde una unidad
```

## Ventaja fundamental

- Elimina la necesidad de locks y semaforos para la mayoria de los casos
- El protocolo se hace **explicito** en el codigo: quien le habla a quien
- Erlang y Go hacen de esto su principio de diseno central

## Desventaja potencial

- Copiar datos tiene costo; para volumenes grandes hay que diseñar el protocolo

---

### [F-14] Mensajes sincronicos, asincronicos y canales

@tipo: tabla-comparativa
@imagen: none

# El modelo de mensaje define quien espera y cuanto

| Variante | Comportamiento del emisor | Comportamiento del receptor | Lenguaje tipico |
|----------|---------------------------|-----------------------------|-----------------|
| Sincrona / canal sin buffer | Espera hasta que el receptor acepta | Espera hasta que hay mensaje | Go `make(chan T)`, TS MessageChannel |
| Asincrona bufferizada | Continua si hay lugar en el buffer | Espera si buffer vacio | Go `make(chan T, N)`, BroadcastChannel |
| Asincrona pura | Continua siempre sin esperar | El mensaje llega a la cola del receptor | Erlang `!`, TS `postMessage` |

## Consecuencias de diseno

- **Sincrona** = sincronizacion implicita → mas predecible, menos concurrencia real
- **Asincrona** = mayor concurrencia, pero puede haber acumulacion de mensajes
- La eleccion del modelo **cambia la semantica del programa**

---

## BLOQUE C — TypeScript avanzado: cancelacion, canales y Rust

---

### [F-15] TypeScript: cancelacion estructurada con AbortController

@tipo: codigo
@imagen: none

# AbortController conecta el ciclo de vida de una operacion asincrona con su cancelacion

## Patron de timeout y cancelacion manual

```ts
// Cancelacion con timeout automatico
async function fetchConTimeout<T>(url: string, ms: number): Promise<T> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(new Error("timeout")), ms);

  try {
    const resp = await fetch(url, { signal: controller.signal });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    return await resp.json();
  } finally {
    clearTimeout(timer);
  }
}

// Cancelacion desde fuera: el usuario hace click en "Cancelar"
const controller = new AbortController();
botonCancelar.addEventListener("click", () => controller.abort());

// Propagar signal a operaciones encadenadas
async function procesarPaginas(signal: AbortSignal): Promise<void> {
  for (let pag = 1; !signal.aborted; pag++) {
    const datos = await fetch(`/api?p=${pag}`, { signal }).then(r => r.json());
    if (datos.fin) break;
    await procesarLote(datos.items, signal); // propagar la misma signal
  }
}
```

## Por que esto importa para concurrencia

- `signal.aborted` es el flag de cancelacion compartido entre operaciones encadenadas
- Es la version TypeScript de "structured concurrency": el padre controla el ciclo de vida de sus hijos
- Conecta conceptualmente con `coroutineScope` de Kotlin y los scopes de Go

---

### [F-16] TypeScript: MessageChannel y BroadcastChannel — pasaje de mensajes real

@tipo: codigo
@imagen: none

# TypeScript tiene canales de mensajes reales; no solo async/await sobre el event loop

## MessageChannel: canal privado punto a punto entre contextos

```ts
// Crear el canal y los dos extremos del tubo
const { port1, port2 } = new MessageChannel();

// Lado receptor (puede estar en un Worker)
port1.onmessage = ({ data }: MessageEvent) => {
  console.log("Recibido en port1:", data);
  port1.postMessage({ respuesta: "ok", eco: data }); // responder
};

// Lado emisor: enviar y esperar respuesta
port2.postMessage({ tipo: "ping", valor: 42 });
port2.onmessage = ({ data }) => console.log("Respuesta:", data);

// Transferir port2 a un Worker para comunicacion privada
const worker = new Worker("./worker.js");
worker.postMessage({ canal: port2 }, [port2]); // transferencia de ownership
```

## BroadcastChannel: fan-out a todos los contextos del mismo origen

```ts
// Cualquier tab, worker o iframe que tenga el mismo nombre recibe el mensaje
const receptor = new BroadcastChannel("cache-invalidation");
receptor.onmessage = ({ data }) => {
  if (data.tipo === "invalidar") limpiarCache(data.clave);
};

// Desde cualquier otro contexto:
new BroadcastChannel("cache-invalidation").postMessage({
  tipo: "invalidar",
  clave: "usuarios"
});
```

## Conexion con los modelos de comunicacion

- `MessageChannel` implementa pasaje de mensajes punto a punto
- `BroadcastChannel` implementa el modelo de publicacion/suscripcion
- La transferencia de ownership con `[port2]` conecta con el concepto de Rust: mover el recurso

---

### [F-17] Rust: el compilador como garante de la concurrencia

@tipo: concepto-mixto
@imagen: none

# Rust hace imposible compilar codigo con data races — sin GC, sin runtime de seguridad

## Threads con Arc<Mutex<T>> — compartir memoria de forma segura

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // Arc = puntero con conteo de referencias thread-safe
    // Mutex<i32> = el i32 solo es accesible con el lock tomado
    let contador = Arc::new(Mutex::new(0));

    let handles: Vec<_> = (0..4).map(|_| {
        let c = Arc::clone(&contador); // clonar la referencia, no el dato
        thread::spawn(move || {
            let mut lock = c.lock().unwrap(); // tomar el mutex
            *lock += 1;                       // seccion critica
            // lock se libera AUTOMATICAMENTE al salir del scope (RAII)
        })
    }).collect();

    for h in handles { h.join().unwrap(); }
    println!("Total: {}", *contador.lock().unwrap()); // siempre 4
}
```

## Lo que el compilador rechaza en Rust

```rust
let datos = vec![1, 2, 3];

thread::spawn(|| {
    println!("{:?}", datos); // ERROR: datos no cumple Send — no puede cruzar threads
});

// Para cruzar threads, el tipo debe implementar Send (seguro para threads)
// y Sync (seguro para compartirse). El compilador lo verifica estaticamente.
```

## Contraste pedagogico con TypeScript

| Aspecto | TypeScript | Rust |
|---------|-----------|------|
| Quien detecta la carrera | El programador / runtime | El compilador |
| Costo de la seguridad | Disciplina + tests | Verbose, pero garantizado |
| Modelo de memoria | GC, heap dinamico | Ownership, sin GC |
| Cuando usar | Web, servidores, tooling | Sistemas, drivers, Wasm critico |

---

## BLOQUE D — Java: threads clasicos y java.util.concurrent

---

### [F-18] Java Thread y Runnable: creacion de hilos

@tipo: codigo
@imagen: none

# Java tiene dos formas de crear un hilo: subclase o interfaz Runnable

## Forma 1: extender Thread

```java
class MiTarea extends Thread {
  private final String nombre;

  MiTarea(String nombre) { this.nombre = nombre; }

  @Override
  public void run() {
    for (int i = 0; i < 3; i++) {
      System.out.println(nombre + ": paso " + i);
    }
  }
}

// Uso
Thread t1 = new MiTarea("A");
Thread t2 = new MiTarea("B");
t1.start();    // crea el hilo del OS y llama run() en el
t2.start();
t1.join();     // esperar que t1 termine antes de continuar
t2.join();
```

## Forma 2: implementar Runnable (preferida)

```java
Runnable tarea = () -> {
  for (int i = 0; i < 3; i++) System.out.println("Lambda: " + i);
};

Thread t = new Thread(tarea);
t.start();
t.join();
```

## Por que Runnable es preferida

- Un objeto puede implementar `Runnable` y extender otra clase a la vez
- Se separa la **tarea** (logica) del **mecanismo** (Thread)
- Compatible con `ExecutorService` sin cambios

---

### [F-19] Java synchronized, wait y notify

@tipo: codigo
@imagen: none

# `synchronized` implementa monitores; `wait`/`notify` implementan cooperacion

## Exclusion mutua con synchronized

```java
class Banco {
  private double saldo = 1000.0;

  // Monitor: solo un thread ejecuta este metodo a la vez
  public synchronized void depositar(double monto) {
    saldo += monto;                        // seccion critica protegida
  }

  public synchronized void retirar(double monto) {
    if (saldo >= monto) saldo -= monto;
  }

  // Bloque synchronized: proteger parte del metodo
  public void transferir(Banco destino, double monto) {
    synchronized (this) {
      saldo -= monto;
    }
    synchronized (destino) {
      destino.saldo += monto;
    }
  }
}
```

## Cooperacion con wait/notify en el monitor

```java
class BufferCircular {
  private int[] datos = new int[10];
  private int entrada = 0, salida = 0, cantidad = 0;

  public synchronized void poner(int valor) throws InterruptedException {
    while (cantidad == datos.length) wait();    // buffer lleno: libera lock y espera
    datos[entrada] = valor;
    entrada = (entrada + 1) % datos.length;
    cantidad++;
    notifyAll();                               // avisar a consumidores que hay dato
  }

  public synchronized int sacar() throws InterruptedException {
    while (cantidad == 0) wait();             // buffer vacio: libera lock y espera
    int val = datos[salida];
    salida = (salida + 1) % datos.length;
    cantidad--;
    notifyAll();                              // avisar a productores que hay lugar
    return val;
  }
}
```

- `wait()` **libera el lock** y suspende — luego re-adquiere el lock al despertar
- Siempre `while` con `wait()`, nunca `if` — protege contra spurious wakeups

---

### [F-20] Java java.util.concurrent: herramientas modernas

@tipo: tabla-comparativa
@imagen: none

# Java 5+ ofrece abstracciones de alto nivel sobre threads

| Clase / Interfaz | Para que sirve | Ejemplo de uso |
|-----------------|----------------|----------------|
| `ExecutorService` | Pool de threads reutilizable | `Executors.newFixedThreadPool(4)` |
| `Future<T>` | Resultado asincrono de una tarea | `future.get()` espera y retorna valor |
| `ReentrantLock` | Lock explicito con tryLock y timeout | Alternativa a `synchronized` mas flexible |
| `Semaphore` | Semaforo contable | `sem.acquire()` / `sem.release()` |
| `CountDownLatch` | Esperar que N tareas terminen | `latch.await()` despues de `latch.countDown()` |
| `BlockingQueue<T>` | Cola thread-safe con bloqueo | `queue.put()` / `queue.take()` |
| `AtomicInteger` | Operacion atomica sin lock | `counter.incrementAndGet()` |
| `CompletableFuture<T>` | Concurrencia funcional encadenada | `.thenApply()`, `.thenCombine()` |

## Pool de threads — patron tipico de produccion

```java
ExecutorService pool = Executors.newFixedThreadPool(4);
List<Future<Integer>> futuros = new ArrayList<>();

for (int i = 0; i < 20; i++) {
  final int id = i;
  futuros.add(pool.submit(() -> procesarElemento(id)));  // tarea asincrona
}

for (Future<Integer> f : futuros) {
  System.out.println("Resultado: " + f.get());           // esperar cada resultado
}
pool.shutdown();
```

---

## BLOQUE E — C# y concurrencia funcional

---

### [F-21] C# threads, lock y Task

@tipo: concepto-mixto
@imagen: none

# C# evoluciono de Thread/lock hacia Task y async/await como abstraccion preferida

## Thread y lock (API clasica)

```csharp
class Contador {
  private int valor = 0;
  private readonly object candado = new object();

  public void Incrementar() {
    lock (candado) {       // equivalente a synchronized de Java
      valor++;
    }
  }
}
```

## Task y async/await (API moderna)

```csharp
async Task<string[]> CargarDatosAsync() {
  Task<string> t1 = ObtenerUsuariosAsync();
  Task<string> t2 = ObtenerPedidosAsync();

  await Task.WhenAll(t1, t2);           // esperar ambas sin bloquear el hilo
  return new[] { t1.Result, t2.Result };
}
```

## Monitor.Wait / Monitor.Pulse

```csharp
lock (cola) {
  while (cola.Count == 0)
    Monitor.Wait(cola);       // equivalente a wait() de Java
  var item = cola.Dequeue();
  Monitor.Pulse(cola);        // equivalente a notify()
}
```

## Diferencia de diseno con Java

- C# `async`/`await` esta integrado en el lenguaje desde C# 5 (2012)
- `Task` es equivalente a `Future` de Java pero con mejor ergonomia
- No hay `synchronized` keyword; se usa `lock(objeto) { }` explicito

---

### [F-22] Erlang y actores: concurrencia sin estado compartido

@tipo: concepto-abstracto
@imagen: none

# Erlang elimina el estado compartido: cada proceso tiene su estado, comunica por mensajes

## Modelo de actores de Erlang

- Cada proceso Erlang tiene **estado completamente aislado**
- La comunicacion es **exclusivamente por mensajes asincrónicos**
- No existen locks, semaforos ni monitores — no hacen falta
- Si un proceso falla, los otros **no se ven afectados** (fault isolation)

## Sintaxis Erlang

```erlang
% Crear un proceso
Pid = spawn(fun contador/0).

% Funcion que corre en el proceso
contador() ->
  receive
    {incrementar, N} ->
      % el estado es local: no hay nada compartido
      contador_con_valor(N + 1);
    {obtener, Remitente} ->
      Remitente ! {valor, 0},
      contador()
  end.

% Enviar mensaje (asincrono, no bloquea)
Pid ! {incrementar, 5}.
```

## Por que esto escala

- Millones de procesos livianisimos en la misma VM
- Sin memoria compartida = sin carreras de datos
- La supervision de procesos (`supervisor`) implementa tolerancia a fallas
- Influencia directa en Go, Akka (Scala/Java), Elixir

---

## BLOQUE F — Concurrencia a nivel de sentencias

---

### [F-23] Concurrencia a nivel de sentencias: FORALL y HPF

@tipo: concepto-abstracto
@imagen: none

# El compilador puede paralelizar iteraciones independientes sin gestion explicita

## Statement-level concurrency

- En algunos dominios (computo cientifico, matrices) todas las iteraciones son independientes
- El lenguaje puede declarar esta independencia y dejar que el compilador/runtime explote el paralelismo
- Sin necesidad de crear threads ni gestionar sincronizacion manualmente

## FORALL en High Performance Fortran (HPF)

```fortran
! Suma vectorial: cada iteracion es independiente -> paralelo automatico
FORALL (I = 1:N)
  A(I) = B(I) + C(I)
END FORALL

! Distribucion de datos entre procesadores
!HPF$ DISTRIBUTE A(BLOCK)
!HPF$ DISTRIBUTE B(BLOCK)
```

## Equivalente moderno: parallelStream en Java

```java
// El runtime elige cuantos threads usar automaticamente
int suma = IntStream.range(0, 1_000_000)
    .parallel()              // declarar independencia
    .filter(n -> n % 2 == 0)
    .sum();
```

## Cuando aplica

- **Si**: operaciones sobre arreglos sin dependencias entre iteraciones
- **No**: si una iteracion depende del resultado de la anterior (reduce)
- La responsabilidad de declarar la independencia es del programador

---

## BLOQUE G — Go y Kotlin: modelos modernos

---

### [F-24] Go goroutines y channels: comunicar en lugar de compartir

@tipo: codigo
@imagen: none

# Go encarna el principio: "Do not communicate by sharing memory; share memory by communicating"

## Goroutine: unidad de concurrencia ultra liviana

```go
package main

import (
  "fmt"
  "sync"
)

func generarNumeros(out chan<- int, wg *sync.WaitGroup) {
  defer wg.Done()
  for i := 0; i < 5; i++ {
    out <- i          // enviar por el canal
  }
  close(out)          // señal: no envio mas
}

func imprimirNumeros(in <-chan int, wg *sync.WaitGroup) {
  defer wg.Done()
  for n := range in { // recibir hasta que el canal se cierre
    fmt.Println(n)
  }
}

func main() {
  canal := make(chan int)    // canal sin buffer: sincronico
  var wg sync.WaitGroup
  wg.Add(2)

  go generarNumeros(canal, &wg)
  go imprimirNumeros(canal, &wg)

  wg.Wait()
}
```

## Caracteristicas clave

- Las goroutines cuestan ~2 KB de stack (vs ~1 MB de un thread del OS)
- El scheduler de Go multiplexa goroutines sobre threads del OS automaticamente
- Los channels son **tipados**: el compilador detecta errores de tipo en la comunicacion
- `select` elige el primer canal listo (igual que `select` de Unix o `select` de Go, pero sin callbacks)

---

### [F-25] Go select y sync.Mutex: cuando si se comparte memoria

@tipo: codigo
@imagen: none

# Go tiene channels Y mutex; usar el adecuado segun el caso

## select: esperar el primer canal disponible

```go
func despachador(urgentes, normales <-chan string, timeout <-chan time.Time) {
  for {
    select {
    case pedido := <-urgentes:          // si llego un urgente, atenderlo
      procesarUrgente(pedido)
    case pedido := <-normales:          // si llego un normal, atenderlo
      procesarNormal(pedido)
    case <-timeout:                     // si ninguno llego en X segundos
      fmt.Println("Sin actividad")
      return
    }
  }
}
```

## sync.Mutex: para contadores y estructuras compartidas

```go
import "sync"

type ContadorSeguro struct {
  mu    sync.Mutex
  valor int
}

func (c *ContadorSeguro) Incrementar() {
  c.mu.Lock()           // adquirir mutex
  defer c.mu.Unlock()   // liberar al salir (defer garantiza esto)
  c.valor++
}

func (c *ContadorSeguro) Leer() int {
  c.mu.Lock()
  defer c.mu.Unlock()
  return c.valor
}
```

## Regla de Go para elegir

- **Channels** para coordinar trabajo, transferir propiedad de datos, señalizar eventos
- **Mutex** para proteger datos cuando multiples goroutines necesitan acceso compartido

---

### [F-26] Kotlin corrutinas y concurrencia estructurada

@tipo: codigo
@imagen: none

# Kotlin hace visible el ciclo de vida, la cancelacion y los errores como ciudadanos del lenguaje

## Structured Concurrency: todas las corrutinas tienen un scope padre

```kotlin
import kotlinx.coroutines.*

suspend fun cargarDashboard(): Dashboard = coroutineScope {
  // launch lanza corrutinas hijas; coroutineScope espera a todas
  val usuariosDeferred = async { api.obtenerUsuarios() }
  val pedidosDeferred  = async { api.obtenerPedidos() }
  val alertasDeferred  = async { api.obtenerAlertas() }

  // await() suspende sin bloquear el thread
  Dashboard(
    usuarios = usuariosDeferred.await(),
    pedidos  = pedidosDeferred.await(),
    alertas  = alertasDeferred.await()
  )
}
// Si cualquier async falla, el scope cancela las demas automaticamente
// Si el scope se cancela, todas las hijas se cancelan en cascada
```

## Dispatchers: elegir donde corre la corrutina

```kotlin
withContext(Dispatchers.IO)      { leerArchivo() }   // pool de I/O
withContext(Dispatchers.Default) { calcularHash() }  // pool CPU-bound
withContext(Dispatchers.Main)    { actualizarUI() }  // hilo principal (Android)
```

## Por que es pedagogicamente valioso

- Kotlin hace explicitos los tres problemas del async moderno: ciclo de vida, cancelacion y errores
- `coroutineScope` garantiza que ninguna corrutina hijo escapa del scope padre
- Los dispatchers separan "que hacer" de "donde hacerlo"

---

## BLOQUE H — TypeScript: asincronia y paralelismo real

---

### [F-27] TypeScript y el event loop de JavaScript

@tipo: diagrama
@imagen: none

# JavaScript corre en un unico hilo con un event loop cooperativo

## El modelo de ejecucion (MDN)

- JavaScript tiene **un solo hilo** de ejecucion por defecto
- El **event loop** toma tareas de la cola y las ejecuta hasta completion
- `await` suspende el handler actual y devuelve el control al event loop
- Otros handlers pueden correr mientras se espera la I/O

## Implicaciones para la concurrencia

```ts
// Dos fetches pendientes al mismo tiempo, pero solo un handler activo
async function main() {
  const promA = fetch("/api/datos-a"); // inicia sin esperar
  const promB = fetch("/api/datos-b"); // inicia sin esperar

  const [resA, resB] = await Promise.all([promA, promB]); // espera ambas
  // solo un handler a la vez, pero dos requests pendientes simultáneamente
}
```

## Que es y que no es la asincronia de JS

- **Es**: concurrencia de espera sobre I/O — multiples operaciones pendientes a la vez
- **No es**: computo paralelo en CPU — el codigo JavaScript es secuencial
- **No es**: multiprocesamiento — un solo heap, un solo GC, un solo thread (por defecto)

---

### [F-28] async/await, Promise.all y Promise.allSettled

@tipo: codigo
@imagen: none

# La composicion de Promises permite concurrencia de espera sin callbacks anidados

## Promise.all: todas o nada — falla si cualquiera falla

```ts
async function cargarDashboard(): Promise<Dashboard> {
  const [usuarios, ventas, alertas] = await Promise.all([
    api.get<Usuario[]>("/usuarios"),
    api.get<Venta[]>("/ventas"),
    api.get<Alerta[]>("/alertas")
  ]);
  return { usuarios, ventas, alertas };
}
```

## Promise.allSettled: colectar todos los resultados, incluso los fallidos

```ts
async function verificarServicios(urls: string[]): Promise<EstadoServicio[]> {
  const resultados = await Promise.allSettled(
    urls.map(url => fetch(url).then(r => r.json()))
  );

  return resultados.map((r, i) => ({
    url: urls[i],
    estado: r.status === "fulfilled" ? "ok" : "error",
    detalle: r.status === "rejected" ? r.reason : null
  }));
}
```

## Promise.race: el primero que responda gana (patron timeout)

```ts
async function conTimeout<T>(promesa: Promise<T>, ms: number): Promise<T> {
  const timeout = new Promise<never>((_, reject) =>
    setTimeout(() => reject(new Error("timeout")), ms)
  );
  return Promise.race([promesa, timeout]);
}
```

---

### [F-29] worker_threads: paralelismo real en Node.js

@tipo: codigo
@imagen: none

# Para computo CPU-intensivo, un worker es una unidad de ejecucion independiente con su propio V8

## Crear y comunicar con un worker

```ts
// main.ts — hilo principal
import { Worker, isMainThread, parentPort, workerData } from "node:worker_threads";
import { cpus } from "node:os";

const NUCLEOS = cpus().length;

async function procesarEnParalelo(datos: number[]): Promise<number[]> {
  const chunk = Math.ceil(datos.length / NUCLEOS);
  const workers = Array.from({ length: NUCLEOS }, (_, i) =>
    new Promise<number[]>((resolve, reject) => {
      const worker = new Worker(__filename, {
        workerData: { fragmento: datos.slice(i * chunk, (i + 1) * chunk) }
      });
      worker.on("message", resolve);
      worker.on("error", reject);
    })
  );
  return (await Promise.all(workers)).flat();
}

// Codigo que corre DENTRO del worker (mismo archivo)
if (!isMainThread) {
  const resultado = (workerData.fragmento as number[]).map(n => n * n);
  parentPort!.postMessage(resultado);
}
```

## SharedArrayBuffer: memoria compartida entre workers

```ts
const sab = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT * 4);
const arr = new Int32Array(sab);

// Operacion atomica para evitar carreras
Atomics.add(arr, 0, 1);   // equivalente a arr[0]++ pero atomico
Atomics.wait(arr, 0, 0);  // esperar hasta que arr[0] != 0
Atomics.notify(arr, 0);   // despertar workers esperando en arr[0]
```

## Cuando usar workers

- **Si**: computo CPU-bound que bloquearia el event loop (hashing, compresion, ML inference)
- **No**: operaciones I/O — async/await es mas eficiente y mas simple

---

## BLOQUE I — Decision de diseno y cierre

---

### [F-30] Mapa de decisiones: elegir el mecanismo correcto

@tipo: tabla
@imagen: none

# La pregunta no es "que lenguaje esta de moda" sino "que problema tengo"

| Situacion | Mecanismo apropiado | Lenguaje tipico | Riesgo a cuidar |
|-----------|---------------------|-----------------|-----------------|
| Esperar N operaciones I/O simultaneas | `Promise.all` / `async/await` | TypeScript, C# | Propagacion de errores y timeouts |
| Cancelar operaciones con ciclo de vida | `AbortController` + signal | TypeScript | Propagar signal a todas las operaciones hijas |
| Computo CPU-bound aislable | Workers / `ExecutorService` | TS, Java | Costo de serializar datos al worker |
| Contadores y acumuladores compartidos | `Atomics` / `synchronized` / `lock` | TS, Java, C# | Seccion critica bien delimitada |
| Productores y consumidores desacoplados | `BlockingQueue` / channels | Java, Go | Esperas infinitas si el productor falla |
| Ciclo de vida con cancelacion estructurada | Corrutinas + scope | Kotlin, Swift | Propagacion de cancelacion en cascada |
| Pasaje de mensajes punto a punto | `MessageChannel` / channels | TS, Go | Transferencia de ownership del puerto |
| Modelo de actores sin estado compartido | Mensajes / Erlang | Erlang, Akka, Go | Mailbox sin limite puede crecer |
| Hardware paralelo / computo cientifico | FORALL / `parallelStream` | Fortran HPF, Java | Dependencias ocultas entre iteraciones |
| Garantia de no-data-race en compilacion | Ownership + `Arc<Mutex<T>>` | Rust | Verbose, curva de aprendizaje alta |

---

### [F-31] Comparativa de lenguajes: el arco completo

@tipo: tabla-comparativa
@imagen: none

# Cada lenguaje expone una vision distinta de la concurrencia

| Lenguaje | Unidad principal | Sincronizacion | Comunicacion | Garantia del lenguaje |
|----------|-----------------|----------------|--------------|----------------------|
| Java | Thread | synchronized / Lock | wait/notify / BlockingQueue | Runtime exclusion mutua |
| C# | Thread / Task | lock / Monitor | async/await | Compila concurrencia asincrona |
| Go | Goroutine | sync.Mutex | Channels tipados | Race detector en runtime |
| Kotlin | Coroutine | Mutex / Atomic | Flow, Channel | Scope garantiza no leak |
| TypeScript | Promise / Worker | Atomics + MessageChannel | postMessage / BroadcastChannel | AbortController para ciclo de vida |
| Erlang | Process | No hay: sin memoria compartida | send / receive | VM garantiza aislamiento |
| Rust | Thread + Arc<T> | Mutex<T> / Atomic | mpsc channels | Compilador: no data races posibles |

## Lectura pedagogica del arco

- **Java/C#**: monitores clasicos + abstracciones modernas coexisten en el mismo lenguaje
- **Go**: canales como primitiva preferida; mutex cuando realmente se necesita
- **Kotlin**: structured concurrency resuelve los tres grandes problemas (lifecycle, cancel, errores)
- **TypeScript**: excelente para I/O asincronico; workers + Atomics + MessageChannel para lo demas
- **Erlang**: el modelo funcional puro — sin estado compartido, sin carreras posibles
- **Rust**: la seguridad de concurrencia como propiedad del compilador; zero-cost pero verbose

---

### [F-32] Cierre: lo que la clase deja

@tipo: cierre
@imagen: none

# Concurrir es organizar avance, coordinacion y comunicacion entre unidades independientes

## Tres capas que estructuran el tema

1. **Vocabulario**: concurrencia / paralelismo / asincronia / thread — cuatro preguntas distintas
2. **Mecanismos**: semaforos → monitores → pasaje de mensajes — creciente nivel de abstraccion
3. **Lenguajes**: Java → C# → Go → Kotlin → TypeScript → Erlang → Rust — espectro de decisiones de diseno

## Preguntas que el programador debe responder ante un problema concurrente

- ¿Hay estado compartido mutable? → decidir mecanismo de exclusion mutua
- ¿Hay dependencias de orden? → decidir mecanismo de cooperacion
- ¿El costo dominante es I/O o CPU? → elegir entre async o workers
- ¿El ciclo de vida debe ser controlable? → considerar structured concurrency

## Para la proxima clase

- Práctica: implementar productor/consumidor en TypeScript (Atomics + SharedArrayBuffer)
- Opcional: comparar el mismo problema en Go (channels) y Java (BlockingQueue)
