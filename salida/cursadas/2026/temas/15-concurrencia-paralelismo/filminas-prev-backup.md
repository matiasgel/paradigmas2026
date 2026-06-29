# Filminas — Tema 15: Concurrencia y Paralelismo

> **Curso:** Laboratorio de Programación y Lenguajes 2026 (IF009) | **Módulo XI** | **Semana 15**
> **Duración:** 120 minutos | **Lenguaje principal:** TypeScript | **Contrastes:** Java, Go, Kotlin
> **Baseline:** `concurrencia.txt` (filminas reales dadas en clase) — recuperadas y mejoradas.

---

## PORTADA

---

### [F-00] Concurrencia y Paralelismo

@tipo: portada
@imagen: background
@prompt-imagen: Two parallel horizontal sequences of flat geometric shapes on white background. Top sequence: three bordo rectangles connected by thin rightward arrows. Bottom sequence: three dark gray circles connected by thin rightward arrows. Between both sequences, a vertical dashed line in the center. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Concurrencia y Paralelismo

Recorrido: fundamentos, sincronización, modelos de comunicación.

Módulo XI — Semana 15

---

## BLOQUE A — Vocabulario y frontera conceptual

---

### [F-01] Un resultado que cambia solo con el orden

@tipo: socratica
@imagen: background
@prompt-imagen: One large central oval shape in bordo color on white background. Inside the oval, a small dark gray diamond. Three thin curved lines radiate outward from the oval toward three small flat icons arranged in a triangle: a checkmark, a magnifying glass, and a gear. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# ¿Si dos unidades modifican el mismo dato, quién decide el valor final?

## El caso TOTAL

```
TOTAL := 3

Tarea A:
  x := TOTAL
  x := x + 1
  TOTAL := x

Tarea B:
  x := TOTAL
  x := x * 2
  TOTAL := x
```

- Si A completa antes que B: resultado = **6**
- Si B completa antes que A: resultado = **4**
- Si se intercalan (interleaving): puede ser **4, 6, 7 u 8**

Leer–calcular–escribir **no es** una operación atómica.
El problema no es el lenguaje: es **estado compartido sin coordinación**.

---

### [F-02] Cuatro palabras que no son sinónimos

@tipo: tabla-comparativa

# Concurrencia, paralelismo, asincronía y threads: cuatro preguntas distintas

## No son sinónimos; cada término responde una pregunta diferente

| Término | Pregunta que responde | Ejemplo concreto |
|---------|----------------------|------------------|
| Concurrencia | ¿Varias actividades progresan solapadas? | Dos tareas alternando en un núcleo |
| Paralelismo | ¿Ejecutan simultáneamente en hardware? | Dos núcleos corriendo al mismo tiempo |
| Asincronía | ¿Puedo continuar mientras espero? | `await fetch(url)` sin bloquear |
| Thread | ¿Quién ejecuta instrucciones? | Unidad de ejecución del OS |

## Lo que importa para este curso

- Un programa puede ser **concurrente sin ser paralelo** (un núcleo, multitarea).
- Un programa puede ser **asíncrono sin ser concurrente** (single event loop, un handler a la vez).
- Paralelismo necesita hardware múltiple; concurrencia no.
- El foco de esta clase es la **concurrencia a nivel de subprogramas**.

---

### [F-03] Concurrencia a nivel de subprogramas

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Two horizontal layers on white background. Top layer: a single wide dark gray rectangle. Bottom layer: four small bordo squares arranged in a horizontal row connected by thin curved lines to the top rectangle. A thin vertical dashed line connects the two layers in the center. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Concurrencia física vs concurrencia lógica

## El hardware y el lenguaje ofrecen dos niveles de concurrencia

### Concurrencia física

- Requiere multiprocesadores o multinúcleo.
- Ejecución simultánea efectiva.
- El runtime mapea tareas lógicas a núcleos disponibles.

### Concurrencia lógica (multiprogramación)

- Un solo núcleo intercala tareas rápidamente.
- El programador ve avance simultáneo.
- El scheduler decide el orden real.
- Es la **abstracción central** para razonar sobre concurrencia en lenguajes.

## Por qué importa la distinción

- Un programa correcto en lógica debe ser **independiente del hardware**.
- Las condiciones de carrera aparecen en **ambos niveles**.

---

### [F-04] Tarea, thread, proceso y corrutina

@tipo: tabla-comparativa

# Unidades concurrentes: la unidad que avanza independientemente

## La unidad concurrente puede llamarse tarea, thread, proceso liviano o corrutina

| Unidad | Qué es | Quién la gestiona |
|--------|--------|-------------------|
| Tarea | Unidad lógica de trabajo concurrente | El programa / runtime |
| Thread | Unidad de ejecución dentro de un proceso | El OS |
| Proceso | Espacio de memoria propio con uno o más threads | El OS |
| Corrutina | Unidad concurrente suspendible cooperativamente | El lenguaje / runtime |

## Para esta clase

- Usamos el término general: **unidad concurrente**.
- Lo importante es que **avanza independientemente**.
- El lenguaje o runtime decide **cómo ejecutarla** (mapeo a threads del OS, event loop, etc.).

---

## BLOQUE B — Race conditions, sincronización y comunicación

---

### [F-05] Condición de carrera: el caso TOTAL

@tipo: demo

# Anatomía del problema: leer–calcular–escribir no es atómico

## Tres condiciones para que haya carrera

1. Existe **estado compartido mutable**.
2. Al menos **dos unidades** lo acceden concurrentemente.
3. Al menos **una lo modifica**.

## Código TypeScript (workers compartidos)

```ts
let total = 3

// Tarea A
const x = total
total = x + 1

// Tarea B
const y = total
total = y * 2
```

- El error nace al pensar en atomicidad de leer-calcular-escribir.
- En TypeScript con workers compartidos; en Java con threads: **el problema es el mismo**.

---

### [F-06] Estado compartido: por qué aparece el problema

@tipo: diagrama
@imagen: content
@prompt-imagen: One central dark gray cylinder on white background. Three thin arrows pointing inward toward the cylinder from three small bordo squares at different positions around it. One thin arrow pointing outward from the cylinder to a small dark gray diamond. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# El estado compartido mutable es la raíz

## Por qué no alcanza con un flag booleano simple

- Leer el flag y asignarlo **no es atómico** → se puede generar carrera sobre el propio mecanismo.
- Necesitamos una región donde el interleaving **no importe**.

## La sección crítica

- **Sección crítica:** segmento de código que accede a un recurso compartido y **no debe ejecutarse concurrentemente** por más de una tarea.
- **Exclusión mutua:** sólo una tarea puede estar dentro de la sección crítica a la vez.

---

### [F-07] Sincronización de competencia

@tipo: concepto-mixto

# La sección crítica y sus cuatro propiedades

## Cuatro propiedades que debe garantizar cualquier solución

1. **Exclusión mutua:** como máximo una unidad dentro.
2. **Progreso:** si nadie está adentro y alguien quiere entrar, debe poder.
3. **Espera acotada:** nadie espera indefinidamente si el recurso está libre periódicamente.
4. **Sin suposición de velocidad:** la solución funciona independientemente del planificador.

## Por qué importan las cuatro

- Sin exclusión mutua: hay carrera.
- Sin progreso: el recurso queda inaccesible.
- Sin espera acotada: hay inanición.
- Sin independencia de velocidad: la solución depende del hardware.

```text
Protocolo de entrada  →  Sección crítica  →  Protocolo de salida
```

---

### [F-08] Semáforos: el mecanismo clásico de Dijkstra

@tipo: demo

# Un semáforo coordina acceso con un contador entero y una cola de espera

## Operaciones fundamentales

```text
wait(s)
  si contador(s) > 0: decrementar
  si no: suspender tarea en cola(s)

release(s)
  si cola(s) no vacía: despertar una tarea
  si no: incrementar contador(s)
```

## Dos usos canónicos

- **Semáforo binario** (contador=1): exclusión mutua → actúa como mutex.
- **Semáforo contador** (contador=N): limita N accesos simultáneos a un recurso.

## Propiedad clave

- `wait` y `release` son **operaciones atómicas** — el hardware garantiza que no hay interleaving dentro de ellas.
- El programador es responsable de usar el protocolo correctamente.

## Exclusión mutua con Atomics en TypeScript (workers)

```ts
// SharedArrayBuffer compartido entre workers.
const sab = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT)
const mutex = new Int32Array(sab)

// Convención: 0 = libre, 1 = tomado
function adquirir(): void {
  while (Atomics.compareExchange(mutex, 0, 0, 1) !== 0) {
    Atomics.wait(mutex, 0, 1)
  }
}

function liberar(): void {
  Atomics.store(mutex, 0, 0)
  Atomics.notify(mutex, 0, 1)
}

// Uso: sección crítica protegida
adquirir()
try {
  total = total + 1
} finally {
  liberar()
}
```

---

### [F-09] Errores típicos con semáforos

@tipo: tabla

# Errores típicos con semáforos y su consecuencia

| Error de protocolo | Causa | Efecto observable |
|--------------------|-------|-------------------|
| Olvidar `release` tras `wait` | El programador omite la llamada | Deadlock permanente |
| `release` sin `wait` previo | Lógica incorrecta | Otro thread entra en sección crítica — dato corrupto |
| `wait` y `release` en orden invertido | Error de diseño | Deadlock o corrupción según timing |
| Sección crítica demasiado pequeña | Protege solo parte del acceso | Carrera sobre el resto del código |
| Sección crítica demasiado grande | Protege más de lo necesario | Serializa trabajo que podría ser paralelo |

## Por qué los semáforos son frágiles

- El compilador **no detecta** omisiones ni mal orden de `wait`/`release`.
- El mismo mecanismo resuelve competencia y cooperación, pero combinarlos mal puede causar **deadlock**.

---

### [F-10] Monitores: encapsular estado compartido

@tipo: concepto-mixto

# Un monitor protege estado compartido con exclusión garantizada por el lenguaje

## Idea general de monitor

Un monitor es una abstracción con tres partes:

1. **Estado privado:** solo accesible desde dentro del monitor.
2. **Procedimientos sincronizados:** la entrada al monitor garantiza exclusión mutua automática.
3. **Variables de condición:** permiten que una tarea espere dentro del monitor sin bloquear a otras.

## Monitor en Java (`synchronized`)

- `synchronized` es la palabra que convierte el método en procedimiento de monitor.
- `wait()` suspende dentro del monitor y libera el lock temporalmente.
- `notifyAll()` despierta a todos los que esperan para que re-evalúen la condición.

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
    while (cola.isEmpty()) wait();            // espera si vacío
    T item = cola.poll();
    notifyAll();                              // avisa que hay lugar
    return item;
  }
}
```

---

### [F-11] Sincronización de cooperación

@tipo: concepto-mixto

# Cooperación: esperar una condición producida por otra unidad

## Productor / consumidor con semáforos

- Un semáforo resuelve **competencia** (mutex) y **cooperación** (lleno/vacío) por separado.
- Combinar mal los `wait` puede causar **deadlock**.

## Modelo conceptual

```text
Productor:
  wait(vacio)        // espera que haya lugar
  wait(mutex)        // entra a sección crítica
  ... insertar dato ...
  release(mutex)
  release(lleno)     // avisa que hay dato

Consumidor:
  wait(lleno)        // espera que haya dato
  wait(mutex)        // entra a sección crítica
  ... extraer dato ...
  release(mutex)
  release(vacio)     // avisa que hay lugar
```

## Por qué importa el orden

- Si el productor hace `wait(mutex)` antes que `wait(vacio)`, y el buffer está lleno, se bloquea dentro de la sección crítica.
- El consumidor nunca puede entrar → **deadlock**.

---

### [F-12] Pasaje de mensajes: comunicar en lugar de compartir

@tipo: diagrama
@imagen: content
@prompt-imagen: Two flat rectangles on white background, left and right, separated by a horizontal gap. Left rectangle bordo, right rectangle dark gray. A thin horizontal arrow pointing from the left rectangle to the right rectangle. A small circle in the middle of the arrow. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Cada unidad concurrente tiene estado local

## El protocolo se vuelve explícito

- Cada unidad concurrente tiene **estado local**.
- La coordinación ocurre **enviando y recibiendo mensajes**.
- No hay memoria compartida visible.
- No compartir memoria mutable **reduce la necesidad de locks**.

## Operaciones

```text
send(destino, mensaje)   -- enviar un mensaje a una unidad
receive(origen, mensaje) -- recibir un mensaje desde una unidad
```

Puede ser **síncrono o asíncrono** según el lenguaje/modelo.

## Mensajes sincrónicos, asincrónicos y canales

| Modelo | Quién espera | Consecuencia de diseño |
|--------|-------------|------------------------|
| Síncrono | Emisor y receptor se encuentran | Más predecible, menos concurrencia real |
| Asincrónico | Emisor no bloquea | Mayor concurrencia, puede haber acumulación de mensajes |
| Canal | Medio explícito por donde circulan mensajes | Tipado y sincronización explícitos |

---

## BLOQUE C — TypeScript y contrastes de lenguaje

---

### [F-13] TypeScript: event loop, `async` y `Promise.all`

@tipo: codigo

# JavaScript corre en un único hilo con un event loop cooperativo

## El modelo de ejecución

- JavaScript tiene **un solo hilo** de ejecución por defecto.
- El event loop toma tareas de la cola y las ejecuta **hasta completion**.
- `await` suspende el handler actual y devuelve el control al event loop.
- Otros handlers pueden correr mientras se espera la I/O.

## Qué es y qué no es

- **Es:** concurrencia de espera sobre I/O — múltiples operaciones pendientes a la vez.
- **No es:** cómputo paralelo en CPU — el código JavaScript es secuencial.
- **No es:** multiprocesamiento — un solo heap, un solo GC, un solo thread (por defecto).

## Código: dos fetches pendientes al mismo tiempo

```ts
// Dos fetches pendientes al mismo tiempo, pero solo un handler activo
async function main() {
  const promA = fetch("/api/datos-a"); // inicia sin esperar
  const promB = fetch("/api/datos-b"); // inicia sin esperar

  const [resA, resB] = await Promise.all([promA, promB]); // espera ambas
  // solo un handler a la vez, pero dos requests pendientes simultáneamente
}
```

---

### [F-14] TypeScript: workers cuando hay CPU de verdad

@tipo: codigo

# Workers: paralelismo real para cómputo intensivo

## Qué es un worker

- Un worker ejecuta código en una **unidad separada**.
- Sirve para **cómputo intensivo** (CPU-bound).
- Se comunica con **mensajes**.
- Puede compartir memoria mediante `SharedArrayBuffer`, pero eso **reintroduce problemas de sincronización**.

## Cuándo usar workers

| Situación | Mecanismo |
|-----------|-----------|
| Esperar I/O | `async`/`await` |
| Cómputo CPU-bound | Worker |
| Estado compartido | Sincronización / Atomics |

## Atomics: exclusión mutua de bajo nivel

```ts
const sab = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT)
const mutex = new Int32Array(sab)

// 0 = libre, 1 = tomado
function adquirir(): void {
  while (Atomics.compareExchange(mutex, 0, 0, 1) !== 0) {
    Atomics.wait(mutex, 0, 1)
  }
}

function liberar(): void {
  Atomics.store(mutex, 0, 0)
  Atomics.notify(mutex, 0, 1)
}
```

---

### [F-15] Java, Go y Kotlin: tres decisiones de lenguaje

@tipo: tabla-comparativa

# Tres lenguajes, tres modelos de concurrencia

## Java: threads y monitores (modelo clásico)

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
t1.start();    // crea el hilo del OS y llama run() en él
t2.start();
t1.join();     // esperar que t1 termine antes de continuar
t2.join();

// Alternativa: Runnable (separa tarea de mecanismo)
Runnable tarea = () -> {
  for (int i = 0; i < 3; i++) System.out.println("Lambda: " + i);
};
Thread t = new Thread(tarea);
t.start();
t.join();
```

## Go: goroutines y channels (pasaje de mensajes)

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
  close(out)          // señal: no envío más
}

func imprimirNumeros(in <-chan int, wg *sync.WaitGroup) {
  defer wg.Done()
  for n := range in { // recibir hasta que el canal se cierre
    fmt.Println(n)
  }
}

func main() {
  canal := make(chan int)    // canal sin buffer: sincrónico
  var wg sync.WaitGroup
  wg.Add(2)

  go generarNumeros(canal, &wg)
  go imprimirNumeros(canal, &wg)

  wg.Wait()
}
```

## Comparación de los tres modelos

| Lenguaje | Unidad concurrente | Mecanismo principal | Filosofía |
|----------|-------------------|---------------------|-----------|
| Java | Thread (OS) | `synchronized`, `wait`/`notify` | Memoria compartida + monitores |
| Go | Goroutine (~2 KB) | Channels tipados | "Share memory by communicating" |
| Kotlin | Corrutina | `CoroutineScope`, `Job`, dispatchers | Concurrencia estructurada + lifecycle |

## Go: principio rector

> "Do not communicate by sharing memory; share memory by communicating."

- Las goroutines cuestan ~2 KB de stack (vs ~1 MB de un thread del OS).
- El scheduler de Go multiplexa goroutines sobre threads del OS automáticamente.
- Los channels son **tipados**: el compilador detecta errores de tipo en la comunicación.

## Kotlin: concurrencia estructurada

- Las corrutinas viven dentro de un `CoroutineScope` que gobierna **ciclo de vida, cancelación y errores**.
- Un `Job` modela la unidad concurrente; al cancelar el scope, se cancelan todas sus corrutinas hijas.
- Los dispatchers deciden dónde se ejecuta (Default para CPU, IO para I/O).

---

## BLOQUE D — Decisión de diseño y cierre

---

### [F-16] Elegir el mecanismo correcto

@tipo: demo

# Caso integrador: 10.000 imágenes y tres servicios externos

## El escenario

> Tengo que procesar 10.000 imágenes y además consultar tres servicios externos.
> ¿Qué parte conviene hacer con `Promise.all`, qué parte requiere workers,
> y qué datos no deberían compartirse sin sincronización?

## Decisión por tipo de trabajo

| Parte del problema | Mecanismo | Por qué |
|---------------------|-----------|---------|
| Consultar 3 servicios externos | `Promise.all` + `async`/`await` | Es I/O: el event loop basta |
| Procesar 10.000 imágenes (CPU) | `worker_threads` | Cómputo intensivo: el event loop se bloquea |
| Contador compartido entre workers | `Atomics` o `SharedArrayBuffer` | Estado compartido: necesita sincronización |
| Resultados parciales del worker | `postMessage` (mensajes) | Evita compartir memoria mutable |

## Regla práctica

- **I/O** → asincronía (event loop).
- **CPU-bound** → paralelismo (workers).
- **Estado compartido** → sincronización explícita o evitarlo con mensajes.

---

### [F-17] Cierre: mapa mental de concurrencia

@tipo: cierre
@imagen: background
@prompt-imagen: One large bordo filled circle in the center of white background. Six thin straight lines radiate outward to six small flat icons arranged in a circle: a gear, a horizontal tube, a branching tree, a checkmark, a magnifying glass, and a cube. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Mapa mental de concurrencia

## Tres preguntas para decidir

1. **¿Varias actividades progresan solapadas?** → concurrencia.
2. **¿Ejecutan simultáneamente en hardware?** → paralelismo.
3. **¿Puedo continuar mientras espero?** → asincronía.

## Tres mecanismos de coordinación

- **Semáforos:** contador + cola, atómicos pero frágiles.
- **Monitores:** encapsulamiento + exclusión automática (el lenguaje ayuda).
- **Pasaje de mensajes:** comunicar en lugar de compartir (Go lo encarna).

## Tres niveles en TypeScript

- `async`/`await` → concurrencia de espera.
- `Promise.all` → coordinación de operaciones asincrónicas.
- `worker_threads` → paralelismo real para CPU.

## Idea final

> El problema no es el lenguaje: es **estado compartido sin coordinación**.