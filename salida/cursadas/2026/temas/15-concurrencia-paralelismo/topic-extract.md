---
tema: "Concurrencia y Paralelismo"
libro_principal: "Sebesta"
nivel: 2
generado_en: "2026-06-15T21:58:32-03:00"
aprobado_en: null
version: "1"
---

# topic-extract - Concurrencia y Paralelismo

> Pipeline v3. Libro principal: Sebesta Cap. 13. Lenguaje principal: TypeScript. Contrastes: Java, Go, Kotlin.  
> Estado: listo para Checkpoint 1; pendiente de aprobacion docente.

## fuentes

- libro: "Concepts of Programming Languages"
  autor: "Robert W. Sebesta"
  seccion: "Cap. 13: Concurrency, secciones 13.1-13.5"
  pagina: "535-552"
  relevancia: "alta"
  fragmento: "Presenta concurrencia a nivel de subprogramas, tareas, sincronizacion de competencia/cooperacion, semaforos, monitores y pasaje de mensajes."

- libro: "Concepts of Programming Languages"
  autor: "Robert W. Sebesta"
  seccion: "Cap. 13: Ada, Java, C# y funcionales"
  pagina: "552-584"
  relevancia: "alta"
  fragmento: "Compara soporte de lenguajes para tareas, threads, monitores, comunicacion y modelos funcionales de concurrencia."

- libro: "Programming Languages: Principles and Paradigms"
  autor: "Maurizio Gabbrielli y Simone Martini"
  seccion: "Cap. 14: Concurrent Programming"
  pagina: "447-486"
  relevancia: "alta"
  fragmento: "Distingue procesos e hilos, modelos de memoria compartida y mecanismos de comunicacion; refuerza que el foco del curso es el nivel de partes de programa."

- libro: "Programming Languages: Principles and Practices"
  autor: "Kenneth C. Louden y Kenneth A. Lambert"
  seccion: "Cap. 13: Concurrency"
  pagina: "546-584"
  relevancia: "media"
  fragmento: "Aporta vocabulario complementario sobre unidades concurrentes, sincronizacion y coordinacion."

## conceptos-clave

- concepto: "Concurrencia vs. paralelismo"
  definicion: "Concurrencia es la composicion de actividades que progresan de manera solapada; paralelismo es ejecucion simultanea efectiva, usualmente sobre multiples nucleos. Un programa puede ser concurrente sin ser paralelo."
  fuente_seccion: "Sebesta Cap. 13"
  nivel_bloom: "comprender"
  nivel_minimo: 1

- concepto: "Concurrencia a nivel de subprogramas"
  definicion: "El programa se divide en unidades de ejecucion que pueden avanzar independientemente: tareas, threads, corrutinas o procesos livianos segun el lenguaje y su runtime."
  fuente_seccion: "Sebesta 13.2"
  nivel_bloom: "comprender"
  nivel_minimo: 1

- concepto: "Tarea, thread y proceso"
  definicion: "Una tarea es una unidad logica de trabajo concurrente; un thread es una unidad de ejecucion dentro de un proceso; un proceso tiene espacio de memoria propio. La materia debe distinguir el concepto del mecanismo concreto."
  fuente_seccion: "Sebesta 13.2; Gabbrielli/Martini 14.1"
  nivel_bloom: "analizar"
  nivel_minimo: 1

- concepto: "Condicion de carrera"
  definicion: "Ocurre cuando el resultado depende del orden temporal no controlado entre accesos concurrentes a estado compartido. Es el ejemplo base para justificar sincronizacion."
  fuente_seccion: "Sebesta 13.2"
  nivel_bloom: "aplicar"
  nivel_minimo: 1

- concepto: "Sincronizacion de competencia"
  definicion: "Controla el acceso mutuamente excluyente a un recurso compartido para evitar interferencias entre unidades concurrentes."
  fuente_seccion: "Sebesta 13.2-13.4"
  nivel_bloom: "aplicar"
  nivel_minimo: 1

- concepto: "Sincronizacion de cooperacion"
  definicion: "Controla el orden relativo de ejecucion cuando una unidad necesita que otra produzca una condicion, dato o evento antes de continuar."
  fuente_seccion: "Sebesta 13.2-13.5"
  nivel_bloom: "aplicar"
  nivel_minimo: 1

- concepto: "Semaforo"
  definicion: "Estructura con contador y cola de espera que puede modelar exclusion mutua o coordinacion. Es poderoso pero propenso a errores porque el compilador no detecta omisiones o mal orden de wait/release."
  fuente_seccion: "Sebesta 13.3"
  nivel_bloom: "analizar"
  nivel_minimo: 2

- concepto: "Monitor"
  definicion: "Abstraccion que encapsula estado compartido y procedimientos sincronizados, similar a un tipo abstracto de datos con control de acceso concurrente."
  fuente_seccion: "Sebesta 13.4"
  nivel_bloom: "analizar"
  nivel_minimo: 2

- concepto: "Pasaje de mensajes"
  definicion: "Modelo donde las unidades concurrentes coordinan intercambiando mensajes en lugar de compartir memoria directamente; puede resolver cooperacion y competencia mediante protocolos de comunicacion."
  fuente_seccion: "Sebesta 13.5; Gabbrielli/Martini 14"
  nivel_bloom: "analizar"
  nivel_minimo: 2

- concepto: "Asincronia en TypeScript"
  definicion: "`async`/`await` expresa suspensiones sobre operaciones asincronas sin bloquear el hilo principal. Es concurrencia de espera, no paralelismo de CPU por si misma."
  fuente_seccion: "MDN JavaScript execution model; Sebesta 13"
  nivel_bloom: "aplicar"
  nivel_minimo: 1

- concepto: "Workers en Node.js"
  definicion: "Los worker threads permiten ejecutar JavaScript en paralelo para trabajo intensivo de CPU y pueden transferir o compartir memoria bajo reglas explicitas."
  fuente_seccion: "Node.js worker_threads"
  nivel_bloom: "aplicar"
  nivel_minimo: 2

- concepto: "Concurrencia estructurada"
  definicion: "Modelo donde las unidades concurrentes viven dentro de un scope que gobierna ciclo de vida, cancelacion y errores. Kotlin lo hace visible con CoroutineScope, Job y dispatchers."
  fuente_seccion: "Kotlin coroutines overview"
  nivel_bloom: "analizar"
  nivel_minimo: 2

## ejemplos-bibliograficos

- titulo: "Actualizacion perdida sobre TOTAL"
  descripcion: "Dos tareas leen, modifican y escriben el mismo valor; el resultado final depende del interleaving. Sirve para introducir condicion de carrera y necesidad de exclusion mutua."
  codigo_o_texto: |
    // Modelo conceptual
    // TOTAL inicial = 3
    Tarea A: leer TOTAL; sumar 1; escribir TOTAL
    Tarea B: leer TOTAL; multiplicar por 2; escribir TOTAL
    // Segun el orden, el resultado puede variar: 4, 6, 7 u 8.
  fuente_libro: "Sebesta - Concepts of Programming Languages"
  fuente_pagina: "540-541"

- titulo: "Semaforo como contador y cola"
  descripcion: "El par wait/release sobre un contador permite limitar acceso a una seccion critica o coordinar disponibilidad de recursos."
  codigo_o_texto: |
    wait(s)
      si contador(s) > 0: decrementar
      si no: suspender tarea en cola(s)

    release(s)
      si cola(s) no vacia: despertar una tarea
      si no: incrementar contador(s)
  fuente_libro: "Sebesta - Concepts of Programming Languages"
  fuente_pagina: "542-545"

- titulo: "Monitor como dato compartido protegido"
  descripcion: "Un buffer se expone mediante operaciones insert/remove; el acceso al estado interno queda mediado por procedimientos sincronizados."
  codigo_o_texto: |
    monitor Buffer
      procedure insert(item)
      procedure remove() -> item
      // El estado interno no se manipula desde afuera.
  fuente_libro: "Sebesta - Concepts of Programming Languages"
  fuente_pagina: "546-549"

- titulo: "Canal como semaforo en Go"
  descripcion: "Un canal bufferizado puede limitar la cantidad de goroutines que ejecutan una region de trabajo concurrente."
  codigo_o_texto: |
    limit := make(chan int, 3)
    go func() {
      limit <- 1
      work()
      <-limit
    }()
  fuente_libro: "Go Memory Model"
  fuente_pagina: "referencia web"

## tendencias

- tendencia: "En TypeScript/JavaScript moderno conviene separar asincronia de paralelismo: el event loop habilita concurrencia de espera, mientras que workers habilitan paralelismo para CPU."
  relevancia: "alta"
  conflicto_con_bibliografía: "no"
  nota: "Sebesta explica la distincion conceptual; las herramientas concretas actuales de TypeScript se deben actualizar con MDN y Node.js."
  fuente_url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model"

- tendencia: "Node.js worker_threads esta estable y es el contraste natural para mostrar paralelismo real en JavaScript fuera del navegador."
  relevancia: "alta"
  conflicto_con_bibliografía: "sí"
  nota: "Sebesta 2019 no cubre worker_threads modernos; incorporarlo como actualizacion aplicada, no como reemplazo teorico."
  fuente_url: "https://nodejs.org/api/worker_threads.html"

- tendencia: "Kotlin organiza la concurrencia moderna alrededor de corrutinas, scope, Job, dispatcher y cancelacion estructurada."
  relevancia: "media"
  conflicto_con_bibliografía: "sí"
  nota: "Sebesta cubre Java/C#/Ada; Kotlin aporta una formulacion pedagogica actual de lifecycle y errores concurrentes."
  fuente_url: "https://kotlinlang.org/docs/coroutines-overview.html"

- tendencia: "Go refuerza comunicacion y sincronizacion mediante canales, mutexes y reglas de modelo de memoria; es buen contraste para pasaje de mensajes y memoria compartida."
  relevancia: "media"
  conflicto_con_bibliografía: "no"
  nota: "Complementa los modelos de Sebesta con un lenguaje actual centrado en goroutines y channels."
  fuente_url: "https://go.dev/ref/mem"

## superposiciones-detectadas

- tema_previo: "03-intro-funcional-ts"
  conceptos_solapados: "inmutabilidad, funciones puras, seguridad en paralelo"
  nivel_solapamiento: "medio"
  estrategia: "referenciar"

- tema_previo: "05-monadas-ts"
  conceptos_solapados: "Promise, composicion asincronica"
  nivel_solapamiento: "medio"
  estrategia: "asumir-conocido"

- tema_previo: "09.2-aliases-closures-gc"
  conceptos_solapados: "aliasing, estado compartido, race condition"
  nivel_solapamiento: "alto"
  estrategia: "resumir"

- tema_previo: "11-estructuras-control"
  conceptos_solapados: "async/await como flujo de control asincronico"
  nivel_solapamiento: "alto"
  estrategia: "asumir-conocido"

- tema_previo: "13-modulos-interfaces-genericos"
  conceptos_solapados: "interfaz publica y frontera de modulo"
  nivel_solapamiento: "bajo"
  estrategia: "referenciar"
