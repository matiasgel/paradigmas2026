# Diseño del Tema 05 — Mónadas en TypeScript

> ESTADO: APROBADO
> Generado: 2026-04-09
> Aprobado: 2026-04-09
> Agente: topic-designer (Marcos 🗂️)
> Duración constraint: 120 minutos

Duración de clase: 120 minutos
Enfoque: construcción progresiva del concepto de mónada — desde la motivación práctica (encadenamiento de operaciones con efectos) hasta la implementación en TypeScript con comparación lado a lado en Clojure para cada mónada. Se prioriza la comprensión intuitiva y la aplicación sobre la formalización categórica. La cantidad de filminas no está acotada: cada mónada tiene su bloque TS + Clojure completo.

---

## 1. Objetivos de aprendizaje

1. Explicar qué problema resuelven las mónadas en programación funcional y por qué surgen como patrón.
2. Identificar las tres leyes monádicas (identidad izquierda, identidad derecha, asociatividad) y verificarlas en código TypeScript.
3. Implementar desde cero las mónadas `Maybe`, `Either` y `IO` en TypeScript usando genéricos y tipos de unión.
4. Encadenar operaciones con `flatMap` / `bind` para construir pipelines funcionales con manejo de efectos.
5. Contrastar la implementación monádica en TypeScript con la aproximación idiomática en Clojure (protocolos, `cats`, `either`).
6. Reconocer mónadas en APIs existentes: `Promise`, `Array.flatMap`, `Option` de fp-ts/Effect.

## 2. Prerrequisitos

- Tema 03: Funciones puras, inmutabilidad, `map`, `filter`, `reduce`, funciones de orden superior.
- Tema 04: Algebraic data types en TypeScript, patrón `Result<T, E>` / `Either`, composición de funciones, pipes.
- Comprensión de tipos genéricos en TypeScript (`T`, `<T, E>`).
- Familiaridad básica con Clojure (sintaxis, colecciones inmutables, REPL — vistas en T04).

## 3. Alcance del tema

### Incluye

- **Motivación**: el problema del encadenamiento de operaciones que pueden fallar, producir nulidad o tener efectos secundarios.
- **Construcción inductiva**: desde `map` (Functor) → `flatMap` / `bind` (Monad) → leyes monádicas.
- **Tres mónadas canónicas implementadas en TypeScript Y Clojure (lado a lado)**:
  - `Maybe<T>` / `maybe` — computaciones que pueden no producir valor. TS: tagged union + genéricos. Clojure: `cats.monad.maybe` / `some->` idiomático.
  - `Either<E, T>` / `either` — computaciones que pueden fallar con error tipado. TS: tagged union con discriminante. Clojure: `cats.monad.either` + `mlet`.
  - `IO<T>` / thunks y `delay` — computaciones que encapsulan efectos. TS: función envuelta. Clojure: `delay`, closures, comparación con `core.async`.
- **Leyes monádicas**: enunciado, verificación en TS con tests y en Clojure con REPL.
- **Composición monádica**: `flatMap`/`pipe` en TS, `mlet`/`>>=`/threading macros en Clojure.
- **Comparación transversal TS vs Clojure**: por cada mónada se presenta una tabla de diferencias (tipado, ergonomía, ecosistema, idiomaticidad).
- **Mónadas "escondidas"**: `Promise` como mónada (`.then` = `flatMap`), `Array.flatMap`, `Optional chaining` como Maybe simplificado.
- **fp-ts / Effect (mención)**: ecosistema TypeScript para FP con mónadas — `Option`, `Either`, `TaskEither`. Se muestra, no se enseña a fondo.
- **Bloque IA (15 min)**: cómo los LLMs manejan internamente la composición de efectos; uso de mónadas para pipelines de prompting seguros con tipado.

### No incluye

- Teoría de categorías formal (endofunctores, categorías, morfismos naturales). Solo se menciona como "para el curioso".
- Monad transformers (se mencionan como problema motivacional, no se implementan).
- Free monads, algebraic effects, effect handlers (se dejan para lectura complementaria).
- Implementación completa de una librería FP (fp-ts/Effect se muestra como referencia, no se replica).
- Haskell como lenguaje de implementación (se usa solo como contraste notacional en una o dos filminas comparativas).

## 4. Tópicos del Plan Mínimo cubiertos

| Contenido mínimo institucional | Cobertura en este tema |
|-------------------------------|------------------------|
| Paradigmas de programación: funcional | Profundización del paradigma funcional — mónadas como patrón central |
| Sistemas de tipos | Uso de genéricos y tipos unión para modelar mónadas con type safety |
| Criterios de diseño e implementación de LP | Análisis de por qué TS permite mónadas (genéricos + tipos unión) vs. limitaciones sin HKTs |

## 5. Estructura de la clase (120 minutos)

> **Criterio de filminas:** cada mónada tiene filminas TS y filminas Clojure dedicadas, más filminas comparativas. No hay límite de cantidad — la claridad manda.

### Bloque 1 — Motivación: ¿por qué mónadas? (20 min)

- **Apertura (5 min)**: Retomar el `Result<T, E>` del Tema 04. Preguntar: "¿Qué pasa cuando queremos encadenar 3 operaciones que pueden fallar?". Mostrar el código con `if/else` anidados — feo, propenso a errores.
- **El problema del encadenamiento — en los dos lenguajes (10 min)**:
  1. **TypeScript**: Versión imperativa con `if (result !== null)` anidados → `map` que genera `Maybe<Maybe<T>>` → necesidad de `flatMap`.
  2. **Clojure**: Versión con `(when-let ...)` anidados → threading con `some->` que corta en nil → ¿y si queremos propagar *por qué* falló?
  3. Mismo problema, dos lenguajes, misma solución abstracta.
- **Definición de trabajo (5 min)**: Una mónada es un tipo/protocolo con dos operaciones:
  - `of` / `return`: meter un valor en el contexto.
  - `flatMap` / `bind` / `>>=`: encadenar una operación que produce otro contexto.
  - Analogía del contenedor: `of` envuelve, `flatMap` abre-transforma-reenvuelve.

### Bloque 2 — Maybe: la mónada de la opcionalidad (25 min)

- **Maybe en TypeScript (10 min)**:
  - Definir `type Maybe<T> = { tag: 'Just'; value: T } | { tag: 'Nothing' }`.
  - Implementar `of`, `map`, `flatMap`.
  - Ejemplo: buscar usuario → obtener dirección → obtener código postal. Pipeline limpio con `flatMap`.

- **Maybe en Clojure (10 min)**:
  - Clojure idiomático: `nil` como ausencia, `some->` / `some->>` como threading que corta en nil.
  - Con `cats`: `(require '[cats.monad.maybe :as m])`, `(m/just 42)`, `(m/nothing)`, `(m/bind v f)`.
  - Mismo ejemplo: buscar usuario → dirección → código postal con `mlet`.
  - Mostrar: en Clojure `nil` ya es parte del lenguaje — ¿para qué wrappear en Maybe? Discutir: `some->` es Maybe *implícito*; `cats/maybe` es Maybe *explícito*.

- **Comparativa Maybe — filmina dedicada (5 min)**:
  - Tabla lado a lado:
    | Aspecto | TypeScript | Clojure |
    |---------|-----------|----------|
    | Representación | Tagged union `Just/Nothing` | `nil` nativo o `cats/maybe` |
    | Type safety | Compilador fuerza pattern match | En runtime; no fuerza |
    | Encadenamiento | `.flatMap(fn)` / `pipe` | `some->` o `(m/bind v f)` |
    | Ergonomía | Verboso pero seguro | Conciso pero sin red |
    | Idiomático | Sí (con fp-ts/Effect) | `some->` sí; `cats/maybe` menos común |

### Bloque 3 — Either: la mónada del error tipado (25 min)

- **Either en TypeScript (10 min)**:
  - Definir `type Either<E, T> = { tag: 'Left'; error: E } | { tag: 'Right'; value: T }`.
  - Implementar `of`, `map`, `flatMap`.
  - Ejemplo: validar formulario con múltiples campos → cada paso puede fallar con mensaje tipado.
  - Contraste: `Either` vs `try/catch` — propagación explícita vs. implícita del error.

- **Either en Clojure (10 min)**:
  - Con `cats`: `(require '[cats.monad.either :as e])`, `(e/right value)`, `(e/left error)`, `(e/bind v f)`.
  - Mismo ejemplo: validar formulario con `mlet` — cada paso devuelve `right` o `left`.
  - Alternativa idiomática Clojure sin `cats`: retornar mapas `{:ok value}` / `{:error msg}` con convenciones de equipo — es un "Either manual".
  - Discutir: Clojure resuelve errores con datos (mapas), no con tipos — ¿ventaja o desventaja?

- **Comparativa Either — filmina dedicada (5 min)**:
  - Tabla lado a lado:
    | Aspecto | TypeScript | Clojure |
    |---------|-----------|----------|
    | Representación | Tagged union `Left/Right` | `cats/either` o mapa `{:ok/:error}` |
    | Error tipado | `E` es un tipo genérico — compilador verifica | String o keyword — runtime |
    | Encadenamiento | `.flatMap(fn)` con tipo inferido | `(mlet [x (validate-name input) ...])` |
    | vs try/catch | Reemplaza por completo | Complementa (Clojure usa ex-info) |
    | Idiomático | Sí (fp-ts `Either`, Effect) | `cats/either` nicho; mapas convencionales más común |

### Bloque 4 — IO, leyes monádicas y mónadas en el mundo real (25 min)

- **IO en TypeScript (7 min)**:
  - Definir `type IO<T> = { run: () => T }` — la computación como valor.
  - `of`, `map`, `flatMap` para IO.
  - Ejemplo: leer de consola → transformar → escribir. Nada se ejecuta hasta `.run()`.
  - IO separa "qué hacer" de "cuándo hacerlo" — puro hasta el borde del programa.

- **IO en Clojure (7 min)**:
  - Clojure es *impuro por defecto* — no necesita IO como wrapper obligatorio.
  - Sin embargo: `delay` crea un thunk diferido, closures encapsulan efectos.
  - Con `cats`: `(require '[cats.monad.identity :as id])` — en la práctica Clojure no usa IO monad.
  - `core.async` como alternativa: canales como composición de efectos asincrónicos.
  - Comparativa: TS necesita IO para ser "puro"; Clojure elige ser pragmático y controlar efectos por convención.

- **Las tres leyes monádicas — verificadas en ambos lenguajes (6 min)**:
  1. Identidad izquierda: `of(a).flatMap(f) === f(a)` / `(m/bind (m/return a) f) == (f a)`.
  2. Identidad derecha: `m.flatMap(of) === m` / `(m/bind m m/return) == m`.
  3. Asociatividad: `m.flatMap(f).flatMap(g) === m.flatMap(x => f(x).flatMap(g))`.
  - Verificar en TS con tests unitarios y en Clojure en el REPL.

- **Mónadas escondidas (5 min)**:
  - TS: `Promise.then` ≈ `flatMap` (casi-mónada: eager, no lazy). `Array.flatMap`. `?.` como Maybe simplificado.
  - Clojure: `some->` ≈ Maybe. `for` comprehension ≈ List monad. `go` blocks ≈ IO/async.
  - Tabla unificada: `Promise`/`Array`/`Maybe`/`Either`/`IO` — mismo patrón, distintos efectos, dos lenguajes.

### Bloque 5 — Ecosistemas, IA y reflexión final (15 min)

- **Ecosistemas industriales (5 min)**:
  - **TS**: fp-ts (`pipe`, `O.fromNullable`, `E.flatMap`), Effect (`Effect.gen`, do-notation moderna).
  - **Clojure**: `cats` (funcool), `manifold` (async), `missionary` (reactive). Menos mainstream que en TS.
  - Mensaje: "existen librerías maduras que industrializan lo que construimos a mano — en ambos lenguajes, pero con distinta adopción".

- **Bloque IA (5 min)**:
  - Pipeline de prompting: `prompt → LLM → parseo → validación → respuesta`.
  - En TS: modelar con `TaskEither` — cada paso devuelve `Either<Error, T>`, composición con `flatMap`.
  - En Clojure: modelar con `core.async` channels + mapas `{:ok/:error}` — pipeline con `go` blocks.
  - Conexión: composición funcional de efectos como principio de diseño para sistemas con incertidumbre.

- **Reflexión comparativa final (5 min)**:
  - "¿En qué lenguaje es más natural usar mónadas explícitas? ¿Por qué?"
  - TS: el sistema de tipos *recompensa* las mónadas (inferencia, autocompletado, errores en compilación).
  - Clojure: la filosofía de "datos simples" hace que las mónadas formales sean menos idiomáticas, pero los *patrones monádicos* están por todas partes (`some->`, `for`, `go`, mapas de error).
  - Conclusión: el concepto es universal; la forma de expresarlo depende del lenguaje.

### Cierre (10 min)

- **Síntesis visual (4 min)**: Diagrama comparativo con las 3 mónadas × 2 lenguajes + jerarquía Functor → Applicative → Monad.
- **Preguntas clave (3 min)**:
  - ¿Cuándo usar Maybe vs Either vs IO?
  - ¿Por qué flatMap y no solo map?
  - ¿Clojure necesita mónadas formales o le alcanza con `some->` y mapas?
- **Adelanto Tema 06 (3 min)**: Preview de FP en Python ecosistema IA.

## 6. Actividades y artefactos

### Actividad 1 — Maybe en dos lenguajes (Bloque 2)

- Tipo: codificación guiada TS + demo Clojure REPL.
- Input: Interfaz `UserRepo` con funciones que devuelven `User | null` (TS) / `nil` (Clojure).
- Objetivo: Eliminar todos los `if/null`/`when-let` usando Maybe y flatMap en ambos lenguajes.
- Salida: Pipeline limpio en TS con `flatMap` y en Clojure con `mlet`/`some->`. Comparar la ergonomía.

### Actividad 2 — Validador con Either en dos lenguajes (Bloque 3)

- Tipo: codificación guiada TS → demo Clojure.
- Input: Formulario de inscripción con 4 campos (nombre, email, edad, matrícula).
- Objetivo TS: Cada validación devuelve `Either<ValidationError, T>`. Encadenar con flatMap.
- Objetivo Clojure: Misma lógica con `cats/either` + `mlet`, y luego con mapas `{:ok/:error}` idiomáticos.
- Salida: Función `validateForm` en TS y `validate-form` en Clojure. Tabla de diferencias.

### Actividad 3 — Debate: ¿mónadas formales en Clojure? (Bloque 5)

- Tipo: discusión guiada en clase.
- Pregunta disparadora: "Si el compilador no te obliga a usar mónadas, ¿por qué hacerlo? ¿O alcanza con `some->` y datos simples?"
- Perspectivas: disciplina explícita (TS) vs. pragmatismo (Clojure). Errores como datos vs. errores como tipos.

### Actividad 4 — Pipeline IA con Either en TS y Clojure (Bloque 5)

- Tipo: diseño en parejas (pseudo-código / diagrama).
- Input: Flujo de un agente IA: prompt → LLM → parseo → validación → respuesta.
- Objetivo TS: Modelar con `Either<Error, T>` / `TaskEither` y encadenar con `flatMap`.
- Objetivo Clojure: Modelar con `go` blocks + mapas `{:ok/:error}` o `cats/either`.
- Salida: Dos diagramas de flujo monádico (uno por lenguaje) + reflexión sobre diferencias.

## 7. Recursos clave

- Código TypeScript: implementación completa de `Maybe`, `Either`, `IO` con tests de leyes.
- Código Clojure: implementación completa con `cats` (`maybe`, `either`, `mlet`) y versión idiomática sin `cats` (mapas `{:ok/:error}`, `some->`).
- Fragmentos comparativos lado a lado TS vs Clojure para cada mónada (filminas dedicadas).
- Haskell: solo contraste notacional mínimo (1 filmina al final de la jerarquía Functor→Monad).
- Referencias:
  - Wadler, P. (1995). *Monads for Functional Programming* (paper fundacional accesible).
  - Anderlind & Åsberg (2023). *Monadic Programming in Imperative Languages* (Chalmers thesis — implementaciones en JS/TS).
  - funcool/cats — documentación oficial de la biblioteca de mónadas para Clojure.
  - Tema 04 — `Result<T, E>` como precursor de `Either`.

## 8. Indicadores de éxito

- El estudiante puede implementar `Maybe<T>` con `of`, `map` y `flatMap` en TypeScript sin ayuda.
- Puede reproducir el mismo pipeline Maybe en Clojure usando `cats/maybe` o `some->`.
- Puede encadenar 3+ operaciones con `flatMap` (TS) y `mlet`/`bind` (Clojure) y explicar por qué es mejor que `if/null` / `when-let` anidados.
- Puede implementar `Either<E, T>` en TS y el equivalente en Clojure (con `cats` o con mapas convencionales).
- Puede enunciar las 3 leyes monádicas y verificar una de ellas con un test (TS) o en el REPL (Clojure).
- Puede identificar `Promise.then` y `some->` como instancias del patrón monádico.
- Puede argumentar cuándo tiene sentido usar mónadas formales en Clojure vs. el enfoque idiomático de datos simples.

## 9. Riesgos y mitigaciones

| Riesgo | Mitigación |
|--------|-----------|
| Estudiantes se bloquean con la abstracción "mónada" como concepto matemático | Arrancar desde el problema práctico (encadenamiento con nulos), nunca desde la definición formal. La palabra "mónada" aparece recién en el minuto 10, después de que ya estén usando `flatMap`. |
| Confusión entre `map` y `flatMap` | Diagrama visual: `map` envuelve dos veces (`Maybe<Maybe<T>>`), `flatMap` aplana. Repetir 3 veces con ejemplos distintos. |
| Se pierde tiempo en la sintaxis de Clojure | Todos los ejemplos en Clojure vienen pre-cargados en el REPL. El docente ejecuta y explica, no escribe desde cero. Los alumnos ya vieron Clojure en T04. |
| Estudiantes piensan que "todo debería ser monádico" | Cerrar con criterio pragmático: "Usá mónadas cuando el error o el efecto es parte explícita de tu dominio. No para sumar dos números." |
| El bloque IA queda desconectado | Conectar explícitamente: "El pipeline de prompting ES el mismo patrón que el validador de formulario — falla tipada propagada con flatMap." |

## 10. Notas para la producción posterior

- `minuta.md` debe detallar los tiempos exactos y las transiciones entre bloques. Bloques 2 y 3 son los más densos (25 min c/u) — requieren ritmo cuidado.
- `filminas.md` debe tener para **cada mónada** (Maybe, Either, IO): filminas TS, filminas Clojure, y filmina comparativa lado a lado. No escatimar en cantidad — la claridad manda. Incluir diagramas de flujo monádico y tablas TS vs Clojure.
- `guia-estudio.md` debe incluir la implementación completa con tests y las 3 leyes verificadas con código.
- `tp.md` debe pedir implementar al menos Maybe y Either con tests que validen las leyes, más un pipeline realista. El TP del tema anterior (T04) ya usó `Result<T,E>` — asegurarse de no duplicar ejercicios.
- Los PDFs descargados en `_edu-knowledge/references/monads-pdfs/` son la base bibliográfica para la guía de estudio. Usar especialmente Wadler (1995) y Anderlind & Åsberg (2023).

---

> Eso está fuera de scope del Tema 05: monad transformers, free monads, algebraic effects y effect handlers quedan como lectura complementaria — no se evalúan ni se presentan en clase salvo mención mínima. — Marcos 🗂️
