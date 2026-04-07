# Clase: Aspectos Avanzados de Programación Funcional
**Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
**Tema:** 04 | **Módulo:** II
**Duración:** 120 minutos | **Fecha:** ___________

> **Cómo usar esta minuta:** Cada sección corresponde a una filmina. Los momentos (▶) son acciones secuenciales dentro de esa filmina. El texto entrecomillado es lo que decís en voz alta. El código está inline — no necesitás abrir `filminas.md` para dar la clase.

---

## Objetivos de la Clase

- OA-1: Comparar la expresión de patrones funcionales en TypeScript y Clojure.
- OA-2: Aplicar transformaciones de datos con funciones puras y colecciones inmutables.
- OA-3: Construir y usar `Result` / `Either` para manejo funcional de errores.
- OA-4: Entender transducers en Clojure y su equivalente en TS como composición de transformaciones.
- OA-5: Identificar modelos de concurrencia funcional en Clojure y contrastarlos con `Promise` / `async-await` en TypeScript.
- OA-6: Diseñar una pequeña API funcional generics-safe en TypeScript.

---

## BLOQUE 1 — Fundamentos avanzados (35 min)

### [F-01] Portada

**Tiempo:** 1 min

**▶ Al mostrar la portada**
> "Hoy vamos a avanzar más allá de los fundamentos funcionales. Vamos a comparar cómo se resuelven los mismos problemas en TypeScript y Clojure, y cómo ese contraste nos ayuda a elegir buenas abstracciones."

**▶ Transición:** "Comenzamos con una regla simple: menos estado, más composición."

---

### [F-02] ¿Por qué hablar de funcional?

**Tiempo:** 3 min

**▶ Al mostrar la regulación**
> "El funcional no es un capricho académico. Es la respuesta a problemas reales de concurrencia, escala y mantenibilidad."

**▶ Enfatizar**
- El estado mutable complica el desarrollo concurrente.
- El funcional reduce los efectos secundarios.
- Las ideas que veremos hoy aplican en TS y Clojure.

**▶ Transición:** "Veamos cómo se comparan los paradigmas."

---

### [F-03] Imperativo vs funcional

**Tiempo:** 3 min

**▶ Al mostrar la tabla**
- Explicar la diferencia de enfoque.
- Resaltar que ambos paradigmas son igualmente poderosos, pero con modelos mentales distintos.

**▶ Pregunta:** "¿Qué paradigma prefieren cuando necesitan controlar estado muy fino?"

**▶ Transición:** "Ahora definamos con más precisión qué es una función pura."

---

### [F-04] Funciones puras

**Tiempo:** 3 min

**▶ Al mostrar la definición**
> "Una función pura no mira ni modifica nada que no esté en sus parámetros. Eso nos da predictibilidad y facilita pruebas."

**▶ Ejemplos:**
- `const doble = x => x * 2`
- `const area = ({ radius }) => Math.PI * radius ** 2`

**▶ Transición:** "Ahora conectemos esto con la inmutabilidad."

---

### [F-05] Inmutabilidad

**Tiempo:** 3 min

**▶ Al mostrar la comparación**
- Explicar que en funcional no cambiamos valores, creamos nuevos.
- Relacionar con errores de estado compartido.

**▶ Punto clave:**
> "La inmutabilidad es la mejor defensa contra bugs de concurrencia."

**▶ Transición:** "Veamos cómo se ve esto en TypeScript."

---

### [F-06] Pipeline en TypeScript

**Tiempo:** 3 min

**▶ Al mostrar el código**
- Recorrer `.filter()`, `.map()`, `.reduce()`.
- Señalar que cada paso transforma datos sin mutarlos.

**▶ Pregunta:** "¿Qué valor devuelve el método `filter`?"

**▶ Transición:** "Ahora desglosamos cada operación."

---

### [F-07] `filter` + `map`

**Tiempo:** 3 min

**▶ Al mostrar la tabla**
- Explicar que `filter` selecciona y `map` transforma.
- Relacionar ambos con la idea de composición.

**▶ Ejemplo rápido:**
- De [1,2,3,4] a [4,16]

**▶ Transición:** "Seguimos con `reduce`."

---

### [F-08] `reduce`

**Tiempo:** 3 min

**▶ Al mostrar el código**
- Mostrar cómo acumula sin mutar.
- Aclarar que no es un loop imperativo, es una reducción funcional.

**▶ Transición:** "Hagamos el pipeline más reusable con composición."

---

### [F-09] Composición en TypeScript

**Tiempo:** 3 min

**▶ Al mostrar el patrón**
- Explicar `compose` como una función que arma un pipeline.
- Relacionar con `transduce` más adelante.

**▶ Transición:** "Pasamos a Clojure para ver el mismo patrón."

---

### [F-10] Colecciones inmutables en TS

**Tiempo:** 3 min

**▶ Al mostrar ejemplos**
- `const persona = { name: "Ana" } as const`
- `const nuevaPersona = { ...persona, age: 29 }`

**▶ Punto clave:**
> "La versión original sigue intacta."

**▶ Transición:** "En Clojure esto es la norma."

---

### [F-11] Secuencias perezosas en Clojure

**Tiempo:** 3 min

**▶ Al explicar**
- Mostrar que las operaciones no se ejecutan hasta que se necesita el resultado.
- Explicar ventaja de eficiencia.

**▶ Transición:** "Veamos el pipeline de Clojure."

---

### [F-12] Pipeline en Clojure

**Tiempo:** 3 min

**▶ Al mostrar el código**
- Leer `->>` como un flujo de datos.
- Señalar que `filter`, `map`, `reduce` están presentes aquí también.

**▶ Transición:** "Terminar con colecciones persistentes."

---

### [F-13] Colecciones persistentes en Clojure

**Tiempo:** 3 min

**▶ Al explicar**
- El nuevo valor comparte estructura con el viejo.
- No hay copias completas innecesarias.

**▶ Punto clave:**
> "La inmutabilidad en Clojure es eficiente por diseño."

---

## BLOQUE 2 — Abstracciones y efectos (35 min)

### [F-14] Algebraic data types en TS

**Tiempo:** 3 min

**▶ Al mostrar la definición**
- Explicar qué es un tipo algebraico.
- Enfatizar que el tipo describe resultados posibles.

**▶ Transición:** "Veamos ese patrón aplicado al manejo de errores."

---

### [F-15] `Result` vs excepción

**Tiempo:** 3 min

**▶ Al mostrar la tabla**
- Comparar gestión de error explícita vs implícita.
- Reforzar que `Result` hace visible el flujo.

**▶ Pregunta:** "¿Qué ocurre si no manejamos una excepción?"

---

### [F-16] Ejemplo `Result` en TS

**Tiempo:** 3 min

**▶ Al mostrar el código**
- Leer cada rama del `Result`.
- Explicar el estilo de programación defensiva.

**▶ Transición:** "Ahora un patrón equivalente en Clojure."

---

### [F-17] `Option` / `Maybe`

**Tiempo:** 3 min

**▶ Al explicar**
- Mostrar qué significa un valor opcional.
- Contrastar con `null` / `undefined`.

**▶ Punto clave:**
> "Es mejor modelar la ausencia de valor con tipos, no con valores especiales."

---

### [F-18] Manejo de errores en Clojure

**Tiempo:** 4 min

**▶ Al mostrar el código**
- Leer la función `dividir`.
- Resaltar que el resultado es un mapa con estado.

**▶ Discusión breve:**
> "Este patrón convierte errores en datos."

---

### [F-19] ¿Qué es un transducer?

**Tiempo:** 3 min

**▶ Al mostrar la definición**
- Explicar la idea de componer transformaciones independiente de la colección.
- Relacionar con `compose` en TS.

---

### [F-20] Ejemplo de `transduce`

**Tiempo:** 3 min

**▶ Al mostrar el código**
- Recorrer el comp `filter` + `map`.
- Explicar que el resultado se reduce sin colecciones intermedias.

**▶ Transición:** "Veamos por qué esto importa."

---

### [F-21] Transducers vs pipeline convencional

**Tiempo:** 3 min

**▶ Al mostrar la tabla**
- Comparar creación de colecciones intermedias.
- Resaltar reutilización y eficiencia.

---

### [F-22] API funcional genérica en TS

**Tiempo:** 3 min

**▶ Al mostrar el código**
- Explicar cómo los tipos genéricos hacen la API reusable.
- Relacionar con la robustez de firmas de función.

---

### [F-23] Funciones de orden superior

**Tiempo:** 3 min

**▶ Al explicar**
- Mostrar ejemplos de funciones que toman funciones.
- Enfatizar que son el corazón de la composición.

---

### [F-24] Metaprogramación en Clojure

**Tiempo:** 4 min

**▶ Al explicar**
- Describir macros como código que genera código.
- Aclarar que son poderosas pero deben usarse con cuidado.

**▶ Transición:** "Pasemos a concurrencia."

---

## BLOQUE 3 — Concurrencia y metaprogramación (30 min)

### [F-25] Concurrencia funcional: por qué

**Tiempo:** 3 min

**▶ Al mostrar el concepto**
- Recordar que el funcional reduce errores de estado compartido.
- Concurrencia funcional es una estrategia para programar con seguridad.

---

### [F-26] `core.async`: canales en Clojure

**Tiempo:** 3 min

**▶ Al mostrar el ejemplo parcial**
- Explicar qué es un canal.
- Señalar separación claro entre productor/consumidor.

---

### [F-27] `go` blocks y comunicación

**Tiempo:** 3 min

**▶ Al mostrar el código**
- Explicar el flujo dentro de `go`.
- Mostrar cómo se leen/escriben valores asincrónicos.

---

### [F-28] STM y transacciones

**Tiempo:** 3 min

**▶ Al mostrar el concepto**
- Explicar `ref` y `dosync`.
- Relacionar con rollback seguro.

---

### [F-29] Agentes y estado asíncrono

**Tiempo:** 3 min

**▶ Al mostrar el concepto**
- Explicar que `agent` actualiza estado fuera de línea.
- Mostrar cuándo es una buena opción.

---

### [F-30] Concurrencia en TypeScript

**Tiempo:** 3 min

**▶ Al mostrar el concepto**
- Explicar que `Promise` es un contenedor de valor futuro.
- Aclarar que la pureza se pierde con I/O.

---

### [F-31] Promesas y `async-await`

**Tiempo:** 3 min

**▶ Al mostrar el código**
- Explicar el flujo secuencial.
- Señalar dónde ocurre el efecto.

---

### [F-32] Efectos puros vs I/O

**Tiempo:** 3 min

**▶ Al mostrar la comparación**
- Definir pureza versus efecto.
- Mostrar cuándo separar lógica pura de efectos.

---

### [F-33] Canal vs promesa

**Tiempo:** 3 min

**▶ Al mostrar la tabla**
- Comparar casos de uso.
- Preguntar cuál modelo es más natural para eventos continuos.

---

### [F-34] Diseño de flujo continuo

**Tiempo:** 3 min

**▶ Al mostrar el diagrama**
- Explicar el pipeline de eventos.
- Relacionar con arquitecturas de datos en tiempo real.

---

## BLOQUE 4 — Práctica guiada y reflexión (20 min)

### [F-35] Taller comparativo

**Tiempo:** 8 min

**▶ Al presentar el desafío**
- Definir claramente el objetivo.
- Repartir roles TS/Clojure.

**▶ Instrucción clave:**
- Mantener la solución en un dominio simple.
- Usar `Result`/`Either` y `transduce`.

---

### [F-36] Guion TS del taller

**Tiempo:** 3 min

**▶ Al mostrar el código base**
- Explicar tipos y pipeline.
- Asegurar que el equipo entienda la estructura.

---

### [F-37] Guion Clojure del taller

**Tiempo:** 3 min

**▶ Al mostrar el código base**
- Explicar la función de validación.
- Mostrar cómo se combina con `transduce`.

---

### [F-38] Comparar soluciones

**Tiempo:** 2 min

**▶ Al guiar la puesta en común**
- Pedir diferencias y similitudes.
- Resaltar conceptos que se repiten.

---

### [F-39] Buenas preguntas para el cierre

**Tiempo:** 1 min

**▶ Sugerir preguntas**
- ¿Qué abstraemos con un `Result`?
- ¿En qué caso elegimos `core.async`?
- ¿Cuál es la diferencia clave entre pipeline y transducer?

---

### [F-40] Evaluación pedagógica rápida

**Tiempo:** 1 min

**▶ Revisar indicadores**
- Comprensión de patrones funcionales
- Manejo de errores explícito
- Concurrencia funcional definida

---

### [F-41] Resumen final

**Tiempo:** 1 min

**▶ Reforzar lo esencial**
- Menos estado mutable, más composición
- `Result` hace el flujo explícito
- Clojure y TypeScript comparten los mismos principios

---

### [F-42] Próxima clase y TP

**Tiempo:** 1 min

**▶ Concluir con la agenda siguiente**
- Tema siguiente: Mónadas en TypeScript
- TP: implementar una API funcional y justificar la elección de efectos

---

## Materiales y recursos en clase

- Código de ejemplo TypeScript con `readonly`, `Result`, `compose`
- Código de ejemplo Clojure con `->>`, `transduce`, `core.async`
- Pizarra: diagrama comparativo TS ↔ Clojure
- Ejercicio en parejas con dataset de órdenes

---

## Trazabilidad a filminas

- F-01 → Portada del tema
- F-02 → ¿Por qué hablar de funcional?
- F-03 → Imperativo vs funcional
- F-04 → Funciones puras
- F-05 → Inmutabilidad
- F-06 → Pipeline TS
- F-07 → `filter` + `map`
- F-08 → `reduce`
- F-09 → Composición TS
- F-10 → Colecciones inmutables TS
- F-11 → Secuencias perezosas Clojure
- F-12 → Pipeline Clojure
- F-13 → Colecciones persistentes Clojure
- F-14 → Algebraic data types TS
- F-15 → `Result` vs excepción
- F-16 → Ejemplo `Result` TS
- F-17 → `Option` / `Maybe`
- F-18 → Manejo de errores Clojure
- F-19 → ¿Qué es un transducer?
- F-20 → Ejemplo de `transduce`
- F-21 → Transducers vs pipeline convencional
- F-22 → API funcional genérica TS
- F-23 → Funciones de orden superior
- F-24 → Metaprogramación en Clojure
- F-25 → Concurrencia funcional: por qué
- F-26 → `core.async` canales
- F-27 → `go` blocks
- F-28 → STM y transacciones
- F-29 → Agentes Clojure
- F-30 → Concurrencia TS
- F-31 → Promesas y `async-await`
- F-32 → Efectos puros vs I/O
- F-33 → Canal vs promesa
- F-34 → Diseño de flujo continuo
- F-35 → Taller comparativo
- F-36 → Guion TS del taller
- F-37 → Guion Clojure del taller
- F-38 → Comparar soluciones
- F-39 → Buenas preguntas para el cierre
- F-40 → Evaluación pedagógica rápida
- F-41 → Resumen final
- F-42 → Próxima clase y TP
