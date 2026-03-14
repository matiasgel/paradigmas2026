# TP 03 — Introducción a Programación Funcional con TypeScript

> **Tipo:** Repo GitHub Classroom (autograding)
> **Agente:** Aux. Valeria 📝 (tp-designer)
> **Fecha de generación:** 2026-03-14
> **Trazabilidad:** minuta.md — Bloques 1 a 7
> **Workflow:** create-tp / Part A + autograde-repo

---

## Datos del TP

| Campo | Valor |
|-------|-------|
| Materia | Paradigmas y Lenguajes de Programación 2026 |
| Tema Nº | 03 |
| Nombre del tema | Introducción a Programación Funcional con TypeScript |
| Tipo de entrega | Quiz Moodle (importar tp-quiz.gift) |
| Tiempo límite | 30 minutos |
| Intentos permitidos | 1 |
| Puntaje total | 15 puntos (1 pt por pregunta) |
| Penalización | Sin penalización por error |
| Mostrar respuestas | Sí, al finalizar |

---

## Instrucciones para el alumno

Este quiz evalúa los conceptos centrales de programación funcional vistos en clase.
Cada pregunta tiene **una sola respuesta correcta**. Tenés **30 minutos** para completarlo.
No hay penalización por respuesta incorrecta, así que respondé todas las preguntas.

---

## Preguntas

### Pregunta 1 — Funciones puras *(trazable: minuta.md § Bloque 2.2)*

¿Cuál de las siguientes afirmaciones describe correctamente una **función pura**?

- **(A)** Puede modificar variables globales siempre que devuelva un valor.
- **(B)** ✅ Para los mismos argumentos, siempre devuelve el mismo resultado y no produce efectos secundarios.
- **(C)** Puede realizar operaciones de I/O si las registra en un log.
- **(D)** Es una función que solo acepta un único argumento.

---

### Pregunta 2 — Inmutabilidad en TypeScript *(trazable: minuta.md § Bloque 2.3)*

¿Cuál de las siguientes expresiones aplica el principio de **inmutabilidad** correctamente al agregar un elemento a un array en TypeScript?

- **(A)** `arr.push(item); return arr;`
- **(B)** `arr[arr.length] = item; return arr;`
- **(C)** ✅ `const nuevo = [...arr, item]; return nuevo;`
- **(D)** `arr.splice(arr.length, 0, item); return arr;`

---

### Pregunta 3 — Recursión como control de flujo *(trazable: minuta.md § Bloque 2.4)*

¿Por qué la **recursión** es el mecanismo de control de flujo preferido en la programación funcional pura?

- **(A)** ✅ Porque permite expresar iteraciones sin necesidad de variables mutables de contador.
- **(B)** Porque siempre es más eficiente que los bucles en JavaScript/TypeScript.
- **(C)** Porque TypeScript implementa optimización de recursión de cola (TCO) por defecto.
- **(D)** Porque es la única forma de procesar arrays en TypeScript.

---

### Pregunta 4 — Funciones de primera clase *(trazable: minuta.md § Bloque 3.1)*

¿Qué significa que las funciones son **"valores de primera clase"** en TypeScript?

- **(A)** Son más eficientes en memoria que las funciones en otros lenguajes.
- **(B)** Solo pueden definirse con la sintaxis de arrow function (`=>`).
- **(C)** Tienen acceso automático al contexto del módulo donde se definen.
- **(D)** ✅ Pueden guardarse en variables, pasarse como argumentos y retornarse como resultado de otras funciones.

---

### Pregunta 5 — `map` *(trazable: minuta.md § Bloque 3.2)*

Dado el siguiente código:

```typescript
const nums = [1, 2, 3];
const resultado = nums.map(n => n * n);
```

¿Qué contiene `resultado`?

- **(A)** `[1, 2, 3, 1, 4, 9]`
- **(B)** `6`
- **(C)** ✅ `[1, 4, 9]`
- **(D)** Modifica `nums` in-place y devuelve `undefined`.

---

### Pregunta 6 — `map` vs `filter` *(trazable: minuta.md § Bloque 3.2)*

¿Cuál es la diferencia principal entre `map` y `filter`?

- **(A)** ✅ `map` transforma cada elemento del array; `filter` selecciona elementos según un predicado booleano.
- **(B)** `map` devuelve un array de booleanos; `filter` devuelve el array original sin cambios.
- **(C)** `filter` solo funciona con arrays de strings; `map` es genérico.
- **(D)** Son equivalentes: ambos retornan un nuevo array con la misma longitud que el original.

---

### Pregunta 7 — `reduce` *(trazable: minuta.md § Bloque 3.2)*

¿Qué resultado produce la siguiente expresión?

```typescript
[1, 2, 3, 4].reduce((acc, n) => acc + n, 0)
```

- **(A)** `[0, 1, 3, 6, 10]`
- **(B)** `[1, 2, 3, 4]`
- **(C)** `NaN`
- **(D)** ✅ `10`

---

### Pregunta 8 — Clausuras *(trazable: minuta.md § Bloque 3.3)*

Dado el siguiente código:

```typescript
const multiplicadorPor = (factor: number) => (n: number) => n * factor;
const triple = multiplicadorPor(3);
triple(7);
```

¿Qué valor retorna `triple(7)`?

- **(A)** `10`
- **(B)** ✅ `21`
- **(C)** `3`
- **(D)** `undefined`

---

### Pregunta 9 — `pipe` vs `compose` *(trazable: minuta.md § Bloque 4.1)*

En programación funcional, la función `pipe` aplica las funciones:

- **(A)** ✅ De izquierda a derecha: la primera función de la lista se aplica primero.
- **(B)** De derecha a izquierda: la última función de la lista se aplica primero.
- **(C)** En orden aleatorio optimizado por el runtime de JavaScript.
- **(D)** Solo a valores numéricos, en orden ascendente.

---

### Pregunta 10 — Currificación *(trazable: minuta.md § Bloque 4.2)*

¿Qué es la **currificación** de una función?

- **(A)** Optimizar una función para que se ejecute más rápido reduciendo el número de argumentos.
- **(B)** Convertir una función síncrona en una asíncrona usando Promises.
- **(C)** ✅ Transformar una función de N argumentos en una cadena de funciones que cada una recibe un solo argumento.
- **(D)** Hacer que una función acepte un número variable de argumentos con el operador `...rest`.

---

### Pregunta 11 — Aplicación parcial *(trazable: minuta.md § Bloque 4.2)*

Dado el siguiente código:

```typescript
const addCurried = (a: number) => (b: number) => a + b;
const add5 = addCurried(5);
add5(3);
```

¿Qué concepto demuestra `add5`?

- **(A)** Recursión de cola.
- **(B)** ✅ Aplicación parcial: se fijó el primer argumento (`5`) obteniendo una nueva función.
- **(C)** Composición de funciones usando `pipe`.
- **(D)** Una clausura que modifica el valor de `a` con cada llamada.

---

### Pregunta 12 — Evaluación perezosa *(trazable: minuta.md § Bloque 5.2)*

En TypeScript, ¿qué mecanismo permite construir pipelines de **evaluación perezosa** (lazy)?

- **(A)** `async/await` con Promises.
- **(B)** El operador `??` (nullish coalescing).
- **(C)** `try/catch` para diferir la evaluación de errores.
- **(D)** ✅ Generadores (`function*` / `yield`) que producen valores solo cuando son consumidos.

---

### Pregunta 13 — Tipo `Option` / `Maybe` *(trazable: minuta.md § Bloque 6.2)*

¿Cuál es el propósito principal del tipo `Option<A>` (también llamado `Maybe`) en programación funcional?

- **(A)** Almacenar múltiples valores de distintos tipos en una sola variable.
- **(B)** Registrar el historial de cambios de un valor inmutable.
- **(C)** ✅ Representar un valor que puede o no existir, eliminando los null pointer exceptions al encadenar operaciones.
- **(D)** Implementar herencia de tipos sin usar clases.

---

### Pregunta 14 — Tipo `Either` *(trazable: minuta.md § Bloque 6.3)*

En el tipo `Either<E, A>`, ¿para qué se usa el constructor `left(e)`?

- **(A)** ✅ Para representar el caso de **error**, donde `e` contiene la información del fallo.
- **(B)** Para representar el caso exitoso con el valor `e`.
- **(C)** Para combinar dos valores de tipo `E` y `A` en uno solo.
- **(D)** Para convertir un `Option<A>` en un tipo con manejo de errores explícito.

---

### Pregunta 15 — `Promise` como mónada *(trazable: minuta.md § Bloque 6.4)*

¿En qué sentido `Promise` en JavaScript/TypeScript puede considerarse una **mónada**?

- **(A)** Las Promises son inmutables, igual que los valores en programación funcional pura.
- **(B)** Las Promises implementan directamente la interfaz `Functor` definida por Haskell.
- **(C)** `.then()` es equivalente a `map` y siempre transforma el tipo del valor contenido.
- **(D)** ✅ `.then()` actúa como `flatMap`: encadena operaciones y propaga automáticamente el estado de éxito o error.

---

## Tabla de trazabilidad

| # | Concepto | Bloque minuta | Objetivo de aprendizaje |
|---|----------|---------------|-------------------------|
| 1 | Funciones puras | Bloque 2.2 | OA 1 |
| 2 | Inmutabilidad | Bloque 2.3 | OA 1 |
| 3 | Recursión | Bloque 2.4 | OA 1 |
| 4 | Funciones de primera clase | Bloque 3.1 | OA 1, OA 2 |
| 5 | `map` | Bloque 3.2 | OA 2 |
| 6 | `map` vs `filter` | Bloque 3.2 | OA 2 |
| 7 | `reduce` | Bloque 3.2 | OA 2 |
| 8 | Clausuras | Bloque 3.3 | OA 2 |
| 9 | `pipe` vs `compose` | Bloque 4.1 | OA 1, OA 2 |
| 10 | Currificación | Bloque 4.2 | OA 1 |
| 11 | Aplicación parcial | Bloque 4.2 | OA 2 |
| 12 | Evaluación perezosa (generadores) | Bloque 5.2 | OA 3 |
| 13 | `Option` / `Maybe` | Bloque 6.2 | OA 3, OA 4 |
| 14 | `Either` | Bloque 6.3 | OA 3, OA 4 |
| 15 | Promise como mónada | Bloque 6.4 | OA 3, OA 4 |

---

> **Nota:** Las marcas ✅ en este documento son para el docente. El archivo importable a Moodle es `tp-quiz.gift`.
