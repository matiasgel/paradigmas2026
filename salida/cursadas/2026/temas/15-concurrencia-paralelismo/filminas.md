# Filminas — Tema 15: Concurrencia y Paralelismo

> **Curso:** Laboratorio de Programación y Lenguajes 2026 (IF009) | **Módulo XI** | **Semana 15**
> **Duración:** 120 minutos | **Lenguaje principal:** TypeScript | **Contrastes:** Java, Go
> **Baseline:** `concurrencia.txt` (filminas reales dadas en clase) — reconstruidas fielmente.

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

```text
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

### [F-03] Concurrencia física vs concurrencia lógica

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Two horizontal layers on white background. Top layer: a single wide dark gray rectangle. Bottom layer: four small bordo squares arranged in a horizontal row connected by thin curved lines to the top rectangle. A thin vertical dashed line connects the two layers in the center. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# El hardware y el lenguaje ofrecen dos niveles de concurrencia

## Concurrencia física

- Requiere multiprocesadores o multinúcleo.
- Ejecución simultánea efectiva.
- El runtime mapea tareas lógicas a núcleos disponibles.

## Concurrencia lógica (multiprogramación)

- Un solo núcleo intercala tareas rápidamente.
- El programador ve avance simultáneo.
- El scheduler decide el orden real.
- Es la **abstracción central** para razonar sobre concurrencia en lenguajes.

## Por qué importa la distinción

- Un programa correcto en lógica debe ser **independiente del hardware**.
- Las condiciones de carrera aparecen en **ambos niveles**.

---

### [F-04] Tarea, thread, proceso y corrutina como unidades concurrentes

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Four small flat shapes arranged in a horizontal row on white background: a bordo square, a dark gray circle, a bordo hexagon, and a dark gray triangle. A thin horizontal line connects all four shapes. Above the line, a single wide rectangle in light gray. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# La unidad concurrente puede llamarse tarea, thread, proceso liviano o corrutina

## Para esta clase

- Usamos el término general: **unidad concurrente**.
- Lo importante es que **avanza independientemente**.
- El lenguaje o runtime decide **cómo ejecutarla**.

---

## BLOQUE B — Race conditions y sincronización

---

### [F-05] Condición de carrera: anatomía del problema

@tipo: codigo

# El error nace al pensar en atomicidad de leer-calcular-escribir

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

- En TypeScript con workers compartidos; en Java con threads: **el problema es el mismo**.

---

### [F-06] Sincronización: la sección crítica

@tipo: concepto-mixto

# La sección crítica es la región donde el interleaving importa

## Definición

- **Sección crítica:** segmento de código que accede a un recurso compartido y **no debe ejecutarse concurrentemente** por más de una tarea.
- **Exclusión mutua:** sólo una tarea puede estar dentro de la sección crítica a la vez.

## Cuatro propiedades que debe garantizar cualquier solución

1. **Exclusión mutua:** como máximo una unidad dentro.
2. **Progreso:** si nadie está adentro y alguien quiere entrar, debe poder.
3. **Espera acotada:** nadie espera indefinidamente si el recurso está libre periódicamente.
4. **Sin suposición de velocidad:** la solución funciona independientemente del planificador.

## Por qué no alcanza con un flag booleano simple

- Leer el flag y asignarlo **no es atómico** → se puede generar carrera sobre el propio mecanismo.

---

### [F-07] Semáforos: el mecanismo clásico de Dijkstra

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: One central vertical pole in dark gray on white background. At the top of the pole, a bordo circle. Below it, a thin horizontal bar. At the bottom, a small dark gray rectangle. To the right of the pole, a vertical column of three small flat squares stacked. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

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

---

### [F-08] Semáforos en código: exclusión mutua con Atomics

@tipo: codigo

# El semáforo resuelve competencia con el mismo mecanismo

## Exclusión mutua con Atomics en TypeScript (workers)

```ts
// SharedArrayBuffer compartido entre workers.
// Un entero alcanza para representar el estado del mutex.
const sab = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT)
const mutex = new Int32Array(sab)

// Convención:
// 0 = libre
// 1 = tomado

function adquirir(): void {
  while (Atomics.compareExchange(mutex, 0, 0, 1) !== 0) {
    // Si sigue tomado, el worker se bloquea
    // hasta que alguien notifique un cambio.
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

### [F-09] Semáforos en cooperación: productor/consumidor

@tipo: concepto-mixto

# El semáforo resuelve competencia y cooperación por separado

## Sincronización de cooperación: productor/consumidor

- Un semáforo resuelve **competencia** (mutex) y **cooperación** (lleno/vacío) por separado.
- Combinar mal los `wait` puede causar **deadlock**.

## Por qué importa el orden de los wait

- Si el productor hace `wait(mutex)` antes que `wait(vacio)` y el buffer está lleno, se bloquea dentro de la sección crítica.
- El consumidor nunca puede entrar → **deadlock**.

---

### [F-10] Errores típicos con semáforos

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

### [F-11] Monitores: encapsulamiento y exclusión automática

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

## BLOQUE C — Modelos de comunicación

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

---

### [F-13] Mensajes sincrónicos, asincrónicos y canales

@tipo: tabla-comparativa

# El modelo de mensaje define quién espera y cuánto

## Consecuencias de diseño

| Modelo | Quién espera | Consecuencia de diseño |
|--------|-------------|------------------------|
| Síncrono | Emisor y receptor se encuentran | Sincronización implícita → más predecible, menos concurrencia real |
| Asincrónico | Emisor no bloquea | Mayor concurrencia, pero puede haber acumulación de mensajes |
| Canal | Medio explícito por donde circulan mensajes | Tipado y sincronización explícitos |

---

## BLOQUE D — Lenguajes: Java y Go

---

### [F-14] Java Thread y Runnable: creación de hilos

@tipo: codigo

# Java tiene dos formas de crear un hilo: subclase o interfaz Runnable

## Forma 1: extender Thread — Forma 2: implementar Runnable

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

Runnable tarea = () -> {
  for (int i = 0; i < 3; i++) System.out.println("Lambda: " + i);
};

Thread t = new Thread(tarea);
t.start();
t.join();
```

## Por qué Runnable

- Un objeto puede implementar `Runnable` y extender otra clase a la vez.
- Se separa la **tarea** (lógica) del **mecanismo** (Thread).

---

### [F-15] Go goroutines y channels

@tipo: codigo

# "Do not communicate by sharing memory; share memory by communicating"

## Goroutine: unidad de concurrencia ultra liviana

- Las goroutines cuestan **~2 KB de stack** (vs ~1 MB de un thread del OS).
- El scheduler de Go multiplexa goroutines sobre threads del OS automáticamente.
- Los channels son **tipados**: el compilador detecta errores de tipo en la comunicación.

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

---

## BLOQUE E — TypeScript: event loop, workers y Atomics

---

### [F-16] TypeScript y el event loop de JavaScript

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

### [F-17] Workers: paralelismo real

@tipo: tabla-mixta

# Un worker ejecuta código en una unidad separada

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

---

### [F-18] Atomics: exclusión mutua de bajo nivel

@tipo: cierre
@imagen: background
@prompt-imagen: One large bordo filled circle in the center of white background. Six thin straight lines radiate outward to six small flat icons arranged in a circle: a gear, a horizontal tube, a branching tree, a checkmark, a magnifying glass, and a cube. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Atomics: exclusión mutua de bajo nivel

## Cierre del recorrido

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

## Idea final

> El problema no es el lenguaje: es **estado compartido sin coordinación**.