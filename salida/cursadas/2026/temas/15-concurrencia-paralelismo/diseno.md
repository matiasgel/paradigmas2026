# Diseno de Clase - Tema 15: Concurrencia y Paralelismo

> **Estado:** PENDIENTE DE APROBACION  
> **Disenador:** Marcos v3 (topic-designer-v3)  
> **Fecha:** 2026-06-15  
> **Modulo:** XI | **Semana:** 15 | **Clase:** 1 de 1  
> **Duracion:** 120 minutos (constraint de generacion)

---

## Datos del Tema

| Campo | Valor |
|-------|-------|
| Numero | 15 |
| Nombre | Concurrencia y Paralelismo |
| Modulo curricular | XI - Concurrencia |
| Duracion | 120 minutos |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | Java, Go, Kotlin |
| Libro principal | Sebesta, Cap. 13 |
| Nivel v3 | 2 - Estandar |

---

## Alcance Curricular Obligatorio

Este tema cubre exactamente el Modulo XI del plan minimo:

1. Conceptos fundamentales de concurrencia a nivel de subprogramas.
2. Niveles de concurrencia; threads.
3. Sincronizacion de cooperacion y competencia.
4. Comunicacion entre procesos y tareas.
5. Programacion asincrona.
6. Ejemplos en TypeScript y otros lenguajes.

---

## Fuera de Scope

Eso esta fuera de scope del Tema 15:

- Programacion distribuida completa: redes, consenso, tolerancia a particiones.
- GPU, CUDA, OpenCL u OpenMP como contenido central.
- Actores/Erlang como desarrollo completo; puede aparecer como mencion historica si hace falta.
- Reactive streams, RxJS o Effect-TS como tema propio.
- Rust ownership/borrow checker como solucion de concurrencia; queda como contraste opcional de una filmina, no como eje.
- Optimizacion de rendimiento de bajo nivel.

Justificacion: la clase dura 120 minutos y el contrato institucional pide fundamentos de concurrencia de lenguajes, no arquitectura paralela ni sistemas distribuidos.

---

## Objetivos de Aprendizaje

Al finalizar la clase, el estudiante podra:

1. Distinguir concurrencia, paralelismo, asincronia y ejecucion secuencial.
2. Explicar que significa concurrencia a nivel de subprogramas.
3. Diferenciar tarea, thread, proceso y corrutina como unidades de ejecucion.
4. Detectar una condicion de carrera sobre estado compartido.
5. Explicar sincronizacion de competencia y cooperacion con ejemplos concretos.
6. Usar semaforos y monitores como modelos conceptuales de coordinacion.
7. Comparar memoria compartida con pasaje de mensajes.
8. Aplicar en TypeScript la diferencia entre `Promise.all`, `async`/`await` y `worker_threads`.
9. Comparar decisiones de lenguaje en Java, Go y Kotlin.
10. Evaluar cuando un problema necesita asincronia, concurrencia o paralelismo real.

---

## Bibliografia Principal

- Robert W. Sebesta, *Concepts of Programming Languages*, Pearson 2019, Cap. 13: Concurrency. Fuente primaria estructural.
- Maurizio Gabbrielli y Simone Martini, *Programming Languages: Principles and Paradigms*, Springer 2023, Cap. 14: Concurrent Programming. Complementa modelos modernos.
- Kenneth C. Louden y Kenneth A. Lambert, *Programming Languages: Principles and Practices*, Course Technology 2012, Cap. 13: Concurrency. Apoyo terminologico.

Fuentes actuales para contrastes de lenguaje:

- MDN Web Docs: JavaScript execution model.
- Node.js Documentation: worker_threads.
- Kotlin Documentation: Coroutines.
- Go Documentation: Memory Model y paquete sync.

---

## Estrategia Pedagogica

La clase empieza con un conflicto simple: dos tareas actualizan el mismo valor y el resultado cambia segun el orden. Desde ahi se construye el vocabulario de Sebesta: unidad concurrente, estado compartido, competencia, cooperacion, sincronizacion y comunicacion.

TypeScript es el lenguaje ancla, pero no se lo presenta como "lenguaje de threads" en el sentido clasico. La idea didactica es separar tres niveles:

1. `async`/`await`: concurrencia de espera sobre el event loop.
2. `Promise.all`: coordinacion de operaciones asincronas.
3. `worker_threads`: paralelismo real para computo intensivo.

Los contrastes se usan para que el alumno vea decisiones de diseno:

- Java: threads, `synchronized`, `wait` y `notify` como modelo clasico cercano a Sebesta.
- Go: goroutines y channels para pensar comunicacion.
- Kotlin: corrutinas y concurrencia estructurada para lifecycle, cancelacion y errores.
- Ada: aparece solo como referencia historica de tareas y rendezvous.

---

## Plan de Filminas

| F-# | Titulo | Tipo sugerido | Duracion |
|-----|--------|---------------|----------|
| F-00 | Concurrencia y Paralelismo | portada | - |
| F-01 | Pregunta de apertura: dos tareas, un resultado roto | socratica | 5 min |
| F-02 | Cuatro palabras que no son sinonimos | tabla-comparativa | 7 min |
| F-03 | Concurrencia a nivel de subprogramas | concepto-abstracto | 7 min |
| F-04 | Tarea, thread, proceso y corrutina | tabla-comparativa | 8 min |
| F-05 | Condicion de carrera: el caso TOTAL | demo | 8 min |
| F-06 | Estado compartido: por que aparece el problema | diagrama | 6 min |
| F-07 | Sincronizacion de competencia | concepto-mixto | 7 min |
| F-08 | Semaforos: contador, cola, wait/release | demo | 9 min |
| F-09 | Errores tipicos con semaforos | tabla | 6 min |
| F-10 | Monitores: encapsular estado compartido | concepto-mixto | 8 min |
| F-11 | Sincronizacion de cooperacion | concepto-mixto | 7 min |
| F-12 | Pasaje de mensajes: comunicar en lugar de compartir | diagrama | 8 min |
| F-13 | TypeScript: event loop, `async` y `Promise.all` | codigo | 10 min |
| F-14 | TypeScript: workers cuando hay CPU de verdad | codigo | 8 min |
| F-15 | Java, Go y Kotlin: tres decisiones de lenguaje | tabla-comparativa | 10 min |
| F-16 | Elegir el mecanismo correcto | caso | 8 min |
| F-17 | Cierre: mapa mental de concurrencia | cierre | 6 min |

**Total estimado:** 120 minutos.

---

## Distribucion por Bloques

| Bloque | Filminas | Tema | Tiempo |
|--------|----------|------|--------|
| A | F-00 a F-04 | Vocabulario y frontera conceptual | 27 min |
| B | F-05 a F-12 | Race conditions, sincronizacion y comunicacion | 59 min |
| C | F-13 a F-15 | TypeScript y contrastes de lenguaje | 28 min |
| D | F-16 a F-17 | Decision de diseno y cierre | 14 min |

La suma pedagogica es 128 min si se ejecuta todo con debate largo; para entrar en 120, F-09 y F-16 deben ser filminas rapidas de decision, no desarrollo teorico extendido. En generacion de clase se debe priorizar F-05, F-08, F-10, F-12 y F-13.

---

## Secuencia Didactica

### Bloque A - Separar conceptos

Objetivo: evitar que el alumno use concurrencia, paralelismo, asincronia y threads como sinonimos.

Actividades:

- Mostrar el problema de apertura antes de definir.
- Construir una tabla de diferencias:
  - concurrencia: varias actividades progresan;
  - paralelismo: varias actividades ejecutan simultaneamente;
  - asincronia: no bloqueo mientras se espera;
  - thread: mecanismo concreto de ejecucion.

### Bloque B - El nucleo Sebesta

Objetivo: que el alumno pueda explicar por que los lenguajes necesitan mecanismos de sincronizacion y comunicacion.

Orden:

1. Race condition sobre `TOTAL`.
2. Estado compartido y seccion critica.
3. Competencia: exclusion mutua.
4. Semaforos: poderosos, pero fragiles.
5. Monitores: estado + operaciones protegidas.
6. Cooperacion: esperar una condicion.
7. Pasaje de mensajes: coordinar sin acceso directo al estado.

### Bloque C - TypeScript y contrastes

Objetivo: bajar el modelo teorico a herramientas de lenguajes reales sin perder el eje conceptual.

TypeScript:

- `async`/`await` no crea paralelismo de CPU; expresa suspension.
- `Promise.all` coordina operaciones asincronas.
- `worker_threads` permite paralelismo real en Node.js cuando el trabajo es CPU-bound.

Contrastes:

- Java muestra el modelo clasico de threads y monitores.
- Go muestra canales y goroutines como pasaje de mensajes.
- Kotlin muestra concurrencia estructurada y ciclo de vida.

### Bloque D - Decision de diseno

Objetivo: que el alumno pueda elegir entre asincronia, memoria compartida, mensajes o paralelismo.

Caso integrador:

> "Tengo que procesar 10.000 imagenes y ademas consultar tres servicios externos. Que parte conviene hacer con `Promise.all`, que parte requiere workers, y que datos no deberian compartirse sin sincronizacion?"

---

## Criterios de Aprobacion del Diseno

El diseno queda aprobado si:

- Cubre todos los puntos del Modulo XI del plan minimo.
- No pisa Tema 11: `async/await` se retoma como asincronia, no como estructura de control.
- No pisa Tema 13: interfaces y modulos se usan como frontera conceptual, no se reexplican.
- Mantiene 120 minutos como constraint real.
- Usa TypeScript como lenguaje principal.
- Usa Java, Go y Kotlin como contraste, sin convertirlos en tres clases paralelas.
- Evita scope creep hacia sistemas distribuidos, GPU o arquitectura.

---

## Plan de Generacion Posterior

Si el docente aprueba este diseno:

1. Aprobar Checkpoint 1 del `topic-extract.md`.
2. Aprobar o ajustar el plan de filminas.
3. Invocar `class-writer` para generar `minuta.md` y `filminas.md`.
4. Mantener el vocabulario "interfaz de programacion", "interfaz publica" o "biblioteca" cuando corresponda; no convertir una capa de abstraccion externa en concepto central del lenguaje.
5. No incluir referencias bibliograficas inline dentro de las filminas; la trazabilidad queda en `topic-extract.md` y bibliografia del tema.
