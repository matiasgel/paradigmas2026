## PORTADA

---

### [F-01] Portada

@tipo: portada
@imagen: background
@prompt-imagen: fondo oscuro con circuitos y símbolos de lambda (λ) y componentes de código abstractos en tonos azul profundo, estilo académico-tecnológico

# Aspectos Avanzados de Programación Funcional

Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
Tema 04 · Módulo II

---

## BLOQUE 1 — Fundamentos avanzados

---

### [F-02] ¿Por qué hablar de funcional?

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: infografía con una ruta que va de un nodo "estado mutable" a otro nodo "expresiones puras", con flechas y colores azul y gris, estilo académico moderno

# ¿Por qué hablar de programación funcional?

## Contexto actual

- Concurrencia y multicore obligan a pensar en datos inmutables
- El funcional es una forma de controlar la complejidad
- No es solo teoría: es una forma práctica de diseño

---

### [F-03] Imperativo vs funcional

@tipo: tabla-comparativa
@imagen: none

# Imperativo vs funcional

| Paradigma | Qué representa | Punto fuerte |
|---|---|---|
| Imperativo | Estado mutable + pasos | Control detallado |
| Funcional | Expresiones + composición | Menos efectos colaterales |

---

### [F-04] Funciones puras

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de cajas y flechas mostrando entrada, función y salida sin cambios en el origen, con colores azul y blanco, estilo plano

# Funciones puras

## Definición

- Misma entrada → mismo resultado
- No producen efectos secundarios
- Son fáciles de razonar y de testear

---

### [F-05] Inmutabilidad

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: ilustración de dos objetos de datos, uno original y otro nuevo, con flechas que muestran copia por valor y sin mutación, estilo minimalista en gris y azul

# Inmutabilidad

## Por qué importa

- El valor original no cambia
- Se evita el estado compartido corrupto
- Es la base de modelos funcionales seguros

---

### [F-06] Pipeline en TypeScript

@tipo: codigo
@imagen: none

# Pipeline funcional en TypeScript

```typescript
const numeros = [1, 2, 3, 4, 5, 6];
const resultado = numeros
  .filter(n => n % 2 === 0)
  .map(n => n * n)
  .reduce((acc, n) => acc + n, 0);
```

---

### [F-07] `filter` + `map`

@tipo: tabla
@imagen: none

# `filter` y `map`

## ¿Qué hacen?

| Operación | Resultado |
|---|---|
| `filter` | Selecciona elementos que cumplen la condición |
| `map` | Transforma cada elemento |

---

### [F-08] `reduce`

@tipo: codigo
@imagen: none

# `reduce` en TypeScript

```typescript
const suma = numeros.reduce((acc, n) => acc + n, 0);
```

- Acumula un valor sin mutar la colección
- Útil para agregaciones y cálculos finales

---

### [F-09] Composición en TypeScript

@tipo: codigo
@imagen: content
@prompt-imagen: diagrama de bloques de funciones encadenadas de izquierda a derecha con flechas, estilo clean tech

# Composición funcional en TypeScript

```typescript
type Transform<T> = (items: T[]) => T[];

const filterPares: Transform<number> = items =>
  items.filter(n => n % 2 === 0);

const mapCuadrado: Transform<number> = items =>
  items.map(n => n * n);

const compose = <T>(...fns: Transform<T>[]) =>
  (input: T[]) => fns.reduce((acc, fn) => fn(acc), input);

const pipeline = compose(filterPares, mapCuadrado);
```

---

### [F-10] Colecciones inmutables en TS

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: infografía con un objeto original y un objeto nuevo creado por copia, con un candado y flechas, estilo profesional sin texto

# Colecciones inmutables en TypeScript

## Herramientas

- `const` + `readonly`
- `ReadonlyArray<T>`
- Spread `...` para crear nuevos valores

---

### [F-11] Secuencias perezosas en Clojure

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama simple de datos que fluyen lentamente por una tubería con gotas, estilo minimalista azul-gris

# Secuencias perezosas en Clojure

- Las operaciones no se ejecutan hasta que se necesita el resultado
- Permite trabajar con colecciones grandes sin pasos intermedios innecesarios

---

### [F-12] Pipeline en Clojure

@tipo: codigo
@imagen: none

# Pipeline en Clojure

```clojure
(def numeros [1 2 3 4 5 6])
(def resultado
  (->> numeros
       (filter even?)
       (map #(* % %))
       (reduce +)))
```

---

### [F-13] Colecciones persistentes en Clojure

@tipo: diagrama
@imagen: content
@prompt-imagen: ilustración de una estructura de datos que comparte nodos entre dos versiones, con un efecto de capas y estilo plano

# Colecciones persistentes

## Ventaja clave

- Nuevas versiones se construyen sin copiar todo
- Acceso rápido y seguro a datos antiguos

---

## BLOQUE 2 — Abstracciones y efectos

---

### [F-14] Algebraic data types en TS

@tipo: codigo
@imagen: content
@prompt-imagen: diagrama con dos cajas etiquetadas "ok" y "error" conectadas a un tipo genérico, estilo flat blue

# Algebraic Data Types en TypeScript

```typescript
type Resultado<T, E> =
  | { status: "ok"; value: T }
  | { status: "error"; error: E };
```

---

### [F-15] `Result` vs excepción

@tipo: tabla-comparativa
@imagen: none

# `Result` vs excepciones

| Enfoque | ¿Qué muestra? | Beneficio |
|---|---|---|
| Excepción | Salida normal o error inesperado | Control fuera del tipo |
| `Result` | Flujo explícito de éxito/fallo | Más fácil de razonar |

---

### [F-16] Ejemplo `Result` en TS

@tipo: codigo
@imagen: none

# Ejemplo de `Result` en TypeScript

```typescript
const dividir = (a: number, b: number): Resultado<number, string> =>
  b === 0
    ? { status: "error", error: "División por cero" }
    : { status: "ok", value: a / b };
```

---

### [F-17] `Option` / `Maybe`

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: iconos de un objeto presente y otro ausente, con un signo de interrogación y flechas, estilo gráfico educativo

# `Option` / `Maybe`

- Representa un valor que puede o no existir
- Evita `null` y `undefined`
- Es útil para datos opcionales en pipeline funcional

---

### [F-18] Manejo de errores en Clojure

@tipo: codigo
@imagen: none

# Manejo funcional de errores en Clojure

```clojure
(defn dividir [a b]
  (if (zero? b)
    {:status :error :error "División por cero"}
    {:status :ok :value (/ a b)}))
```

---

### [F-19] ¿Qué es un transducer?

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de dos transformaciones compuestas en una sola etapa, con líneas y cajas transparentes, estilo plano

# Transducers en Clojure

- Componen transformaciones sin crear colecciones intermedias
- Separan qué transformar de cómo procesar
- Son reutilizables en distintos contextos

---

### [F-20] Ejemplo de `transduce`

@tipo: codigo
@imagen: none

# Ejemplo `transduce`

```clojure
(def xf
  (comp
    (filter even?)
    (map #(* % %))))

(transduce xf + [1 2 3 4 5 6])
```

---

### [F-21] Transducers vs pipeline convencional

@tipo: tabla-comparativa
@imagen: none

# Transducers vs pipeline convencional

| Característica | Pipeline | Transducer |
|---|---|---|
| Colecciones intermedias | Sí | No |
| Reutilización | Media | Alta |
| Ideal para | listas pequeñas | flujos grandes |

---

### [F-22] API funcional genérica en TS

@tipo: codigo
@imagen: content
@prompt-imagen: esquema de un API genérico con cajas de tipo `<T>` y flechas, estilo técnico limpio

# API funcional genérica en TS

```typescript
type Transform<T> = (items: T[]) => T[];

const compose = <T>(...fns: Transform<T>[]) =>
  (input: T[]) => fns.reduce((acc, fn) => fn(acc), input);
```

---

### [F-23] Funciones de orden superior

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama con una función que recibe otra función como argumento y retorna una nueva función, estilo abstracto y educativo

# Higher-order functions

- Reciben o devuelven funciones
- Permiten crear abstracciones muy expresivas
- Son la base de la composición funcional

---

### [F-24] Metaprogramación en Clojure

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: ilustración de un árbol sintáctico que se transforma en código, con estilo marcado y abstracto

# Metaprogramación en Clojure

- Las macros operan sobre código como datos
- Son útiles para DSLs y abstracciones de dominio
- Se usan con moderación para no complicar el diseño

---

## BLOQUE 3 — Concurrencia y metaprogramación

---

### [F-25] Concurrencia funcional: por qué

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: imagen abstracta con múltiples flujos paralelos y un candado simbolizando seguridad, estilo flat sin texto

# Concurrencia funcional

- Evita condiciones de carrera
- Se apoya en datos inmutables
- Da predictibilidad a programas paralelos

---

### [F-26] `core.async`: canales en Clojure

@tipo: codigo
@imagen: none

# `core.async` en Clojure

```clojure
(require '[clojure.core.async :refer [chan go >! <! close!]])

(let [in (chan)
      out (chan)]
  ...)
```

- `chan` crea una cola segura
- Permite separar productor de consumidor

---

### [F-27] `go` blocks y comunicación

@tipo: codigo
@imagen: content
@prompt-imagen: diagrama de un bloque `go` conectado a un canal con flechas de entrada y salida, estilo educativo en azul-gris

# `go` blocks en Clojure

```clojure
(go (loop []
      (when-some [x (<! in)]
        (>! out (* x x))
        (recur))))
```

- Crea una coroutine ligera
- No bloquea el hilo principal

---

### [F-28] STM y transacciones

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de dos transacciones sobre un recurso compartido con líneas que representan bloqueo lógico, estilo plano educativo

# STM en Clojure

- `ref` guarda estado coordinado
- `dosync` agrupa actualizaciones
- Permite rollback si falla

---

### [F-29] Agentes y estado asíncrono

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: ilustración de un agente enviando mensajes a un estado centralizado con estilo iconográfico limpio

# Agentes en Clojure

- `agent` actualiza estado de forma asíncrona
- Ideal para tareas que no requieren transacción inmediata
- Separación clara entre envío y procesamiento

---

### [F-30] Concurrencia en TypeScript

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de un navegador y una promesa representada como un reloj, estilo moderno sin texto

# Concurrencia en TypeScript

- `Promise` representa un valor futuro
- `async-await` hace el código más legible
- No elimina la necesidad de pensar en efectos

---

### [F-31] Promesas y `async-await`

@tipo: codigo
@imagen: none

# `async-await` en TS

```typescript
async function fetchData(url: string): Promise<string> {
  const response = await fetch(url);
  return response.text();
}
```

---

### [F-32] Efectos puros vs I/O

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: iconos abstractos de un cubo puro y un enchufe de energía, estilo plano y minimalista

# Efectos puros vs I/O

- Una función pura no observa el mundo exterior
- I/O rompe la pureza
- Es útil separar lógica pura de efectos

---

### [F-33] Canal vs promesa

@tipo: tabla-comparativa
@imagen: none

# Canal vs promesa

| Modelo | Uso ideal | Característica |
|---|---|---|
| `core.async` | Flujos continuos | Canales backpressure |
| `Promise` | Operación puntual | Valor único futuro |

---

### [F-34] Diseño de flujo continuo

@tipo: diagrama
@imagen: content
@prompt-imagen: flujo de datos constante entrando por la izquierda, transformándose y saliendo por la derecha, estilo técnico sin texto

# Flujo funcional continuo

- Datos entran, se transforman, salen
- Ideal para pipelines de eventos y streaming
- El modelo funcional simplifica la razón sobre el flujo

---

## BLOQUE 4 — Práctica guiada y reflexión

---

### [F-35] Taller comparativo

@tipo: demo
@imagen: content
@prompt-imagen: ilustración de dos pantallas lado a lado, una con código TS y otra con código Clojure, estilo flat y académico sin texto

# Taller comparativo

## Desafío

- Filtrar órdenes con `amount` y `status`
- Calcular total funcionalmente
- Manejar errores con `Result` / `Either`

---

### [F-36] Guion TS del taller

@tipo: codigo
@imagen: none

# Ejercicio en TypeScript

```typescript
type Order = { amount: number; status: "valid" | "invalid" };

type Resultado<T, E> =
  | { status: "ok"; value: T }
  | { status: "error"; error: E };
```

- Definir pipeline de validación y suma
- Mantener la lógica pura independiente de efectos

---

### [F-37] Guion Clojure del taller

@tipo: codigo
@imagen: none

# Ejercicio en Clojure

```clojure
(def orders [{:amount 100 :status :valid}
             {:amount 50 :status :invalid}])

(defn validar-orden [order]
  (if (= :valid (:status order))
    {:status :ok :value (:amount order)}
    {:status :error :error "Orden inválida"}))
```

---

### [F-38] Comparar soluciones

@tipo: socratica
@imagen: background
@prompt-imagen: dos bloques de código frente a frente con símbolos de comparación, estilo conceptual sin texto

# Comparar soluciones

- ¿Qué se entiende mejor en TypeScript?
- ¿Qué es más natural en Clojure?
- ¿Dónde se repite la misma idea?

---

### [F-39] Buenas preguntas para el cierre

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: iconos de preguntas y reflexión, estilo educativo sin texto

# Buenas preguntas para el cierre

- ¿Qué abstraemos con un `Result`?
- ¿En qué caso elegimos `core.async`?
- ¿Cuál es la diferencia clave entre pipeline y transducer?

---

### [F-40] Evaluación pedagógica rápida

@tipo: tabla
@imagen: none

# Evaluación rápida

| Comprensión | Indicador |
|---|---|
| Patrones funcionales | Puede explicar composición y pureza |
| Manejo de errores | Usa `Result`/`Either` para flujo explícito |
| Concurrencia | Identifica cuándo usar canales vs promesas |

---

### [F-41] Resumen final

@tipo: cierre
@imagen: background
@prompt-imagen: fondo claro con un camino de hitos y un punto final resaltado, estilo infográfico limpio sin texto

# Cierre

- Menos estado mutable, más composición
- `Result` hace el flujo explícito
- Clojure y TypeScript comparten los mismos principios

---

### [F-42] Próxima clase y TP

@tipo: cierre
@imagen: background
@prompt-imagen: ilustración de un calendario y un archivo de código en colores azules, estilo plano sin texto

# Próxima clase y TP

- Tema siguiente: Mónadas en TypeScript
- TP: implementar una API funcional y justificar la elección de efectos

---

## FIN DEL BLOQUE
