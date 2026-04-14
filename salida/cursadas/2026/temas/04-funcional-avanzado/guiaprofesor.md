# Guía del Profesor — Tema 04

## Aspectos Avanzados de Programación Funcional

> **Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
> **Clase:** 04 | **Duración:** 120 minutos | **Filminas:** F-01 a F-36

---

## Resumen ejecutivo

Esta clase profundiza en patrones avanzados de programación funcional usando Clojure y TypeScript como vehículos de enseñanza. Se estructura en 4 bloques: (1) HOF y composición, (2) partial/currying y validación web con `Result`, (3) recursión de cola y patrones avanzados, (4) taller integrador. El hilo conductor es **construir un pipeline completo de validación/transformación sin mutaciones ni excepciones**, demostrando que los patrones son transferibles entre lenguajes.

**Premisa pedagógica:** Según Sweller & Chen (2023), la carga cognitiva extrínseca se reduce segmentando contenido en bloques de ≤35 minutos con transiciones explícitas. Los 4 bloques están diseñados respetando este principio (35-35-30-20).

---

## Índice de artefactos

| Artefacto | Archivo | Propósito |
|-----------|---------|-----------|
| Diseño (scope y objetivos) | `diseno.md` | Alcance, OA, estructura y riesgos |
| Minuta (guión por filmina) | `minuta.md` | Guión docente para cada F-01 a F-36 |
| Filminas (presentación) | `filminas.md` | 36 filminas aprobadas, fuente de verdad |
| Guía de estudio (alumno) | `guia-estudio.md` | Material autónomo con ejemplos paso a paso |
| Trabajo práctico | `tp.md` | Consignas trazables a filminas |
| Esta guía (profesor) | `guiaprofesor.md` | Documento autocontenido para repasar el tema |

---

## Objetivos de la sesión (10 OA mapeados a Bloom)

| OA | Descripción | Nivel Bloom | Filminas |
|----|-------------|-------------|----------|
| OA-1 | Comprender first-class functions y HOF | Comprender | F-04, F-05 |
| OA-2 | Construir pipelines con `pipe` y `->>` | Aplicar | F-06, F-07, F-08 |
| OA-3 | Aplicar inmutabilidad y transformaciones declarativas | Aplicar | F-09, F-10, F-11, F-12 |
| OA-4 | Diferenciar partial application de currying | Comprender/Aplicar | F-13 a F-18 |
| OA-5 | Modelar errores con `Result<T, E>` | Aplicar | F-19, F-20, F-21 |
| OA-6 | Construir middleware composable con HOF | Aplicar | F-22, F-23 |
| OA-7 | Implementar recursión de cola | Aplicar | F-24 a F-27 |
| OA-8 | Usar memoization, lazy sequences y DSLs | Aplicar/Analizar | F-28 a F-31 |
| OA-9 | Mapear patrones entre Clojure y TypeScript | Analizar | F-32 |
| OA-10 | Resolver taller integrador | Crear | F-33 |

---

## Plan de clase por bloques de tiempo

### BLOQUE 1 — Funciones de orden superior y composición (35 min)

**Meta del bloque:** que el alumno entienda que `map`, `filter`, `reduce`, `compose` y `pipe` son el vocabulario con el que se construye todo lo que viene después.

| Min | Filmina | Acción docente | Recurso |
|-----|---------|---------------|---------|
| 0-1 | F-01 | Proyectar portada. Frase: "Hoy construimos pipelines completos." | — |
| 1-3 | F-02 | Recorrer 4 bloques. Preguntar: "¿Usaron `map` esta semana?" | Pizarra |
| 3-5 | F-03 | Explicitar qué NO se cubre: concurrency, categorías, librerías FP. | — |
| 5-8 | F-04 | **Concepto clave:** first-class functions. Preguntar por lenguajes donde NO existe. | — |
| 8-11 | F-05 | Los 5 patrones HOF: map, filter, reduce, compose, pipe. Una frase por cada uno. | — |
| 11-14 | F-06 | Fórmulas de compose vs pipe. Dibujar flujo de datos en pizarra. | Pizarra |
| 14-18 | F-07 | **Código TS:** implementación de `pipe`, ejemplo `normalizeEmail`. Trazar paso a paso. | IDE/proyector |
| 18-22 | F-08 | **Código Clojure:** `->>` con filter/map/reduce. Comparar con TS: "Mismo patrón, distinta sintaxis." | IDE/proyector |
| 22-25 | F-09 | Antipatrón mutación vs spread. Conectar con React/Vue. | IDE/proyector |
| 25-28 | F-10 | Firmas de tipo: map, filter, flatMap. Diferenciar qué cambia en cada una. | — |
| 28-31 | F-11 | `flatMap` aplicado: roles de usuarios + `mapcat` en Clojure. | IDE/proyector |
| 31-35 | F-12 | `reduce` como fold universal: suma + índice. Transición: "Ahora creamos funciones configurables." | IDE/proyector |

**Señales de comprensión a monitorear:**
- El alumno puede responder "¿`map` es una HOF?" con "sí, porque recibe una función como argumento."
- El alumno identifica que `pipe` y `->>` son el mismo patrón.
- El alumno explica por qué `raw !== clean` después de `normalizeUser(raw)`.

---

### BLOQUE 2 — Aplicación parcial, currying y validación web (35 min)

**Meta del bloque:** que el alumno pueda crear funciones configurables (validators, middlewares) y modelar errores explícitamente con `Result<T, E>`.

| Min | Filmina | Acción docente | Recurso |
|-----|---------|---------------|---------|
| 35-38 | F-13 | Concepto de partial application. Ejemplo: `add5 = partial(add, 5)`. Conectar con fábricas web. | — |
| 38-41 | F-14 | **Código TS:** `makeRequiredValidator` + `validateName`, `validateEmail`. | IDE/proyector |
| 41-44 | F-15 | **Código Clojure:** `partial` nativo, `double`, `triple`. Comparar con TS. | IDE/proyector |
| 44-47 | F-16 | **Concepto crítico:** tabla partial vs currying. Preguntar: "`curriedAdd(5)(3)` — ¿es currying o partial?" | Pizarra |
| 47-50 | F-17 | **Código TS:** `curry2`, `cHasMinLength`, validators de password. | IDE/proyector |
| 50-53 | F-18 | **Código Clojure:** `make-validator`, `validate-field` con reduce. Anticipar `chain` de F-20. | IDE/proyector |
| 53-56 | F-19 | **Tipo `Result`:** definición, 4 ventajas sobre try/catch. "Si puede fallar, el tipo debe decirlo." | — |
| 56-60 | F-20 | **Código TS:** 3 validators + `chain` + `validateForm`. Trazar con datos válidos e inválidos. | IDE/proyector |
| 60-63 | F-21 | **Código TS:** `registerHandler` — Result en un handler HTTP real. Sin try/catch. | IDE/proyector |
| 63-66 | F-22 | Concepto: middleware = HOF que recibe handler y devuelve handler. Firma en pizarra. | Pizarra |
| 66-70 | F-23 | **Código TS:** `withAuth`, `withLogging`, composición con `pipe`. Transición al Bloque 3. | IDE/proyector |

**Señales de comprensión a monitorear:**
- El alumno distingue partial de currying sin confundirlos.
- El alumno puede explicar qué hace `chain`: "si error, propaga; si ok, continúa."
- El alumno identifica que `withAuth("secret")` es partial application.

---

### BLOQUE 3 — Recursión de cola y patrones avanzados (30 min)

**Meta del bloque:** entender recursión de cola como solución al stack overflow y conocer patrones de optimización (memoize, lazy) y diseño (DSL data-driven).

| Min | Filmina | Acción docente | Recurso |
|-----|---------|---------------|---------|
| 70-73 | F-24 | Visualizar stack de factorial(5). "Cada frame espera." | Pizarra |
| 73-76 | F-25 | Acumulador convierte recursión en tail call. "Nada pendiente después." | Pizarra |
| 76-80 | F-26 | **Código Clojure:** `sum-list` + traza paso a paso. `my-flatten` como ejemplo avanzado. | IDE/proyector |
| 80-84 | F-27 | **Código TS:** `sumList`, `findInTree`. "El patrón es portable." | IDE/proyector |
| 84-87 | F-28 | Concepto memoize: cuándo sí (puras, caras), cuándo no (efectos, objetos). | — |
| 87-91 | F-29 | **Código TS:** `memoize` con Map. **Clojure:** `memoize` nativo + fetch-user. | IDE/proyector |
| 91-95 | F-30 | Lazy sequences: `range`, `take`, streaming de logs. Conectar con generators de TS. | IDE/proyector |
| 95-100 | F-31 | **DSL data-driven:** `user-rules` como datos. Motor genérico `validate`. Pattern: las reglas son datos. | IDE/proyector |

**Señales de comprensión a monitorear:**
- El alumno puede explicar por qué `recur` no produce stack overflow.
- El alumno identifica que `memoize` solo funciona con funciones puras.
- El alumno conecta el patrón de `user-rules` con configuración/permisos genéricos.

---

### BLOQUE 4 — Taller y cierre (20 min)

**Meta del bloque:** aplicar todos los conceptos juntos en un problema integrador y consolidar el aprendizaje.

| Min | Filmina | Acción docente | Recurso |
|-----|---------|---------------|---------|
| 100-103 | F-32 | Tabla comparativa 8 patrones. Recorrer rápido agrupando: transformaciones, configuración, lazy, TCO. | — |
| 103-113 | F-33 | **TALLER:** Leer consigna. 8 min trabajo. Circular entre grupos. Sugerir empezar por validators. | IDE alumnos |
| 113-115 | F-34 | Checklist: manos arriba para cada patrón. Identificar gaps. | — |
| 115-118 | F-35 | Guía de adopción: 6 escenarios. Preguntar por ejemplos propios. | — |
| 118-120 | F-36 | Cierre: 4 puntos clave + nexo Tema 05 (mónadas) + cita Hickey. | — |

---

## Profundización teórica por concepto

### First-class functions — fundamento histórico

El concepto proviene del cálculo lambda de Alonzo Church (1936), donde las funciones son la primitiva fundamental. En la práctica moderna, significa que el lenguaje no discrimina entre funciones y otros valores: una función puede almacenarse en una estructura de datos, pasarse a otra función o retornarse como resultado.

**Implicación pedagógica:** muchos alumnos vienen de lenguajes donde las funciones eran "especiales" (C sin punteros a función, Java pre-8). Establecer que "función = valor" temprano (F-04) cambia el marco mental para todo lo que sigue.

**En Clojure:** todas las funciones son objetos que implementan `IFn`. Incluso las keywords como `:name` son funciones (`(:name {:name "Ana"})` → `"Ana"`).

**En TypeScript:** las funciones son objetos de primera clase en JavaScript. El tipado de TS agrega seguridad: `(x: string) => number` es un tipo que el compilador verifica.

### Composición — por qué `pipe` prevalece sobre `compose`

Matemáticamente, la composición se define de derecha a izquierda: $$(f \circ g)(x) = f(g(x))$$

Pero en programación, `pipe` (izquierda a derecha) es más legible porque sigue el flujo natural de lectura del código y el flujo de datos. En la práctica industrial:
- **Unix pipes:** `cat file | grep error | sort | uniq -c` — de izquierda a derecha.
- **Clojure:** `->>` procesa de arriba hacia abajo.
- **RxJS, Effect-TS, fp-ts:** todos usan `pipe` como convención principal.

**Clave para la clase:** no invertir tiempo en debatir compose vs pipe. Mostrar ambos (F-06) y usar pipe como default.

### Partial application vs currying — la confusión más frecuente

Es el concepto que más confunde a los alumnos. La tabla de F-16 es la herramienta pedagógica central.

**Partial application:**
- Toma una función de N args y fija ALGUNOS, devolviendo una función de los args restantes.
- `makeValidator("email")` fija el campo, devuelve `(value) => Result`.
- Es pragmático: fijás lo que necesitás.

**Currying:**
- Transforma una función de N args en N funciones de 1 arg encadenadas.
- `curry(add)` convierte `add(a, b)` en `(a) => (b) => a + b`.
- Es sistemático: SIEMPRE produce funciones de 1 arg.

**Haskell/Elm/F# hacen currying automáticamente.** En TS y Clojure hay que hacerlo explícitamente.

**Test rápido para los alumnos:**
- `partial(add, 5)(3)` → partial application (fijé el primer arg).
- `curry(add)(5)(3)` → currying (cadena de funciones de 1 arg).
- El resultado numérico es el mismo (8), pero el mecanismo es distinto.

### `Result<T, E>` — por qué es fundamental

El tipo `Result` (también llamado `Either` en Haskell) es posiblemente el patrón más valioso que los alumnos se llevan de esta clase. Los prepara directamente para:

1. **Tema 05:** donde `Result` se formaliza como la mónada `Either` con `map`, `flatMap`, `fold`.
2. **Desarrollo profesional:** validación de APIs, procesamiento de datos, manejo de errores en servicios.

**Ventaja clave frente a excepciones:** El tipo de retorno hace **visible** que la función puede fallar. Con `throw`, el error es invisible en la firma — el consumidor descubre que falla solo cuando explota en runtime.

**Código que se escribe mucho en la industria (y que esto prepara):**
```typescript
// Zod (validación popular en TS) usa exactamente este patrón:
const result = userSchema.safeParse(data);
if (!result.success) return res.status(400).json(result.error);
// result.data está tipado como User
```

### Recursión de cola — detalle técnico

**Clojure:** `recur` es una form especial que el compilador verifica. Si `recur` no está en posición de cola, da error de compilación. Internamente, Clojure compila `recur` a un `goto` en la JVM — no hay acumulación de frames.

**JavaScript/TypeScript:** La especificación ES2015 incluye Proper Tail Calls (PTC), pero **solo Safari lo implementa**. V8 (Chrome/Node) no lo hace y probablemente nunca lo hará (por decisión del equipo V8). Esto significa que:
- La recursión de cola en TS NO tiene optimización automática.
- Para millones de iteraciones, hay que usar loops o trampolining.
- El valor de enseñar el patrón es conceptual: acumuladores como técnica de diseño.

**Trampolining** (opcional, para alumnos avanzados):
```typescript
type Thunk<T> = () => T | Thunk<T>;
const trampoline = <T>(fn: Thunk<T>): T => {
  let result = fn();
  while (typeof result === "function") result = (result as Thunk<T>)();
  return result;
};
```

### Memoization — trade-offs

**Complejidad temporal:** O(1) para lookups (amortizado), O(n) en espacio donde n = cantidad de inputs distintos.

**Problema con objetos como keys:** `Map` en JS usa referencia para objetos como key. `{a:1}` y `{a:1}` son dos keys distintas. Para funciones con argumentos de tipo objeto, necesitás serializar (`JSON.stringify`) o usar WeakMap.

**En producción:** librerías como `lodash.memoize` y `memoize-one` resuelven estos edge cases. React tiene `useMemo` y `React.memo` que son formas de memoization.

### Lazy sequences — relevancia práctica

En Clojure, las lazy sequences son fundamentales para:
- **Procesamiento de archivos grandes:** leer línea por línea sin cargar todo en memoria.
- **APIs paginadas:** modelar la paginación como secuencia perezosa.
- **Datos infinitos:** streams de eventos, logs, datos de sensores.

**Equivalente en TypeScript/JavaScript:** generators (`function*`) y los nuevos Array Helpers de TC39. Pero no son tan ergonómicos como en Clojure ni están integrados con las funciones estándar.

---

## Errores frecuentes a corregir en clase

| Error | Dónde aparece | Corrección |
|-------|--------------|-----------|
| Confundir `Result` con `throw` y usar ambos | F-19 a F-21 | "Elegí uno. Si usás Result, no necesitás throw en esa capa." |
| Usar `for` mutando arrays en vez de `map`/`filter` | F-10, F-12 | "¿Qué estás acumulando? Si es un array transformado, `map`. Si es un subconjunto, `filter`." |
| Pensar que `partial` es "una forma rara de llamar funciones" | F-13, F-14 | "No es raro — es una fábrica. `makeValidator('email')` produce un validator reusable." |
| Creer que currying y partial son lo mismo | F-16 | Referir a la tabla de diferencias. Hacer el test: ¿cadena de 1-arg o fijación de algunos args? |
| Sobrecomplicar la sintaxis de Clojure | F-08, F-15, F-26 | "Si te perdiste en los paréntesis, mirá el ejemplo TS — es lo mismo." |
| No entender `chain` en la validación | F-20 | Trazar paso a paso: "error → propaga, ok → continúa. Es un cortocircuito." |
| Usar `flatMap` cuando basta `map` | F-11 | "¿Tu función de transformación devuelve un array? → flatMap. ¿Devuelve un valor? → map." |

---

## Estrategias de contingencia

### Si el grupo se traba con Clojure (>5 min sin avanzar)

1. Pausar el ejemplo Clojure.
2. Mostrar solo el equivalente TypeScript.
3. Decir: "La sintaxis es diferente pero el patrón es el mismo. Lean el Clojure con calma en la guía de estudio."
4. En los bloques siguientes, dar el ejemplo TS primero y el Clojure como confirmación rápida.

### Si sobra tiempo en Bloque 1 (terminan antes de 35 min)

- Agregar ejercicio interactivo: "Definan un pipeline de 3 funciones que normalice nombres completos: trim, capitalizar cada palabra, cortar a 50 chars."
- Pedir que lo hagan primero mentalmente y después en código.

### Si falta tiempo en Bloque 3 (quedan <15 min para 4 filminas)

- F-28 y F-29 (memoization): reducir a explicación oral de 2 min. "El concepto es cache para funciones puras. Lean el ejemplo en la guía."
- F-30 (lazy): mención oral de 1 min. "Clojure evalúa perezosamente: solo calcula lo que pedís."
- F-31 (DSL): esta es importante; mantenerla aunque sea 3 min.

### Si un alumno avanzado pregunta por mónadas

- "Excelente pregunta. El `Result` que estamos viendo ES una mónada — específicamente `Either`. El `chain` que usamos es `flatMap`/`bind`. En la próxima clase (Tema 05) lo formalizamos."

### Si preguntan por concurrencia en Clojure

- "Clojure tiene un modelo de concurrencia excelente (STM, atoms, agents, core.async), pero NO es parte de esta clase — F-03 lo delimita. Lo veremos en el tema de Actores/CSP."

---

## Sugerencias de facilitación

### Para grupos que avanzan rápido

- Pedirles que refactoren `validateForm` para **acumular todos los errores** en vez de parar en el primero. Es un cambio de `chain` (cortocircuito) a `validateAll` (acumulación). Pista: cambiar el tipo de error a `string[]`.
- Pedirles que escriban `map` y `filter` implementados con `reduce`.

### Para grupos que se frenan

- Simplificar el pipeline de validación a 2 campos (email + nombre) en vez de 3.
- Dar el código de `chain` directamente y pedirles que solo escriban los validators.
- Usar la guía de estudio como material de referencia en clase — está diseñada para ser autocontenida.

### Uso del taller (F-33)

- **No es necesario que terminen.** El objetivo es que la ESTRUCTURA del pipeline quede clara.
- Si un grupo termina la Parte A (TS), invitarlos a intentar la Parte B (Clojure).
- Si nadie logra arrancar, mostrar el esqueleto del primer validator y dejar que completen.

---

## Conexiones con otros temas

| Tema | Conexión |
|------|---------|
| **Tema 03** (prerequisito) | Funciones puras, inmutabilidad, map/filter/reduce básicos |
| **Tema 05** (siguiente) | `Result` = mónada `Either`. `chain` = `flatMap`/`bind`. Formalización monádica. |
| **Tema 06** | Manejo disciplinado de side effects. IO monad. |
| **Tema de Actores/CSP** | Concurrencia en Clojure (excluida deliberadamente de esta clase). |
| **Proyecto de cursada** | Los alumnos aplican estos patrones en su pipeline de proyecto. |

---

## Principales citas textuales de referencia

> "When we describe a computation purely in terms of data transformations, we gain the ability to reason about each transformation independently." — Rich Hickey, *Simple Made Easy* (2011)

> "An essential feature of higher-order functions is that they allow us to abstract over actions, not just values." — Abelson & Sussman, *SICP* (1996)

> "Segmentation principle: People learn more deeply when a multimedia message is presented in learner-paced segments rather than as a continuous unit." — Mayer & Fiorella (2023), effect size d=0.79

> "Working memory resource depletion accumulates across tasks. Instructional design should account for temporal build-up of cognitive load." — Sweller & Chen (2023)

---

## Checklist pre-clase

- [ ] IDE preparado con ejemplos de F-07, F-08, F-09, F-14, F-20, F-23, F-26, F-29, F-31
- [ ] Proyector funcionando con las filminas cargadas
- [ ] Pizarra/marcador disponible para diagramas de flujo (F-06) y tabla partial/currying (F-16)
- [ ] Guía de estudio compartida con alumnos (para referencia durante taller)
- [ ] Conexión a internet para demos en vivo (opcional)
- [ ] Clojure REPL disponible (Leiningen o deps.edn) para demos interactivas
- [ ] Node.js/ts-node instalado para demos de TypeScript

---

## Nota final

El propósito de este tema es demostrar que los patrones funcionales no son ejercicios académicos abstractos sino herramientas concretas para desarrollo web profesional. Los alumnos deben salir con la capacidad de aplicar `pipe`, `Result`, `partial` y composición de middleware en sus propios proyectos de TypeScript, y de leer código Clojure reconociendo los mismos patrones con distinta sintaxis.

Las filminas (F-01 a F-36) son la **fuente de verdad**. Esta guía complementa con profundidad teórica, estrategias de contingencia y criterios de evaluación. En caso de duda, referirse siempre a las filminas aprobadas.
