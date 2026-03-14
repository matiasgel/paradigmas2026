# FAQ Anticipado — Tema 03
## Introducción a Programación Funcional con TypeScript

**Agente:** student-simulator 🎓  
**Fecha:** 2026-03-13  
**Método:** Simulación de los 4 perfiles procesando minuta.md + filminas.md (en clase) y guia-estudio.md (autónomo)  
**Organización:** Agrupado por fuente (en clase vs estudiando solos)

---

## Preguntas anticipadas EN CLASE

Agrupadas por bloque. Ordenadas de más a menos probable.

---

### 🔵 Bloque 1 — Motivación (10 min)

**P1.1** *(🔵 Estratégico — alta probabilidad)*
> *"Profe, en el ejemplo de `promedioPositivos`, la versión funcional usa `if (positivos.length === 0)` — ¿eso no es control de flujo imperativo dentro de la función funcional?"*

**Respuesta sugerida:**  
El controlde flujo (`if`) está permitido. La clave es que no hay *estado mutable* — `positivos` es un nuevo valor, no una variable modificada. Funcional no prohíbe condicionales; prohíbe la mutación.

---

**P1.2** *(🔵 Estratégico + 🟡 Ansioso)*
> *"¿Haskell es el único lenguaje funcional 'puro'? ¿TypeScript es funcional?"*

**Respuesta sugerida:**  
TypeScript es multiparadigma — soporta estilo funcional pero no lo impone. Haskell y Elm son funcionales puros. El paradigma funcional es un estilo de programar, no una propiedad del lenguaje.

---

### 🔵 Bloque 2 — Funciones puras, inmutabilidad, recursión (20 min)

**P2.1** *(🟡 Ansioso — alta probabilidad)*
> *"¿La clausura `crearContador` del ejemplo es pura o impura? Captura el entorno pero lo modifica... ¿eso cuenta como efecto secundario?"*

**Respuesta sugerida:**  
`crearContador` **es impura**: modifica `cuenta` entre llamadas. El estado mutable interno es un efecto secundario aunque esté "encapsulado". Una función pura no recuerda nada entre llamadas — devuelve el mismo output para los mismos inputs siempre.

---

**P2.2** *(🔴 Disperso — media probabilidad)*
> *"Profe, ¿`const dobleExterno = n => n * factor` no es pura si al llamarla siempre me da el mismo resultado mientras no cambio `factor`?"*

**Respuesta sugerida:**  
Clave: *¿puede cambiar `factor` entre llamadas?* Sí. La pureza se define por el contrato de la función, no por cómo la usamos en un momento dado. Si alguien puede cambiar `factor`, la función *depende de contexto externo* y no es pura.

---

**P2.3** *(🟡 Ansioso — alta probabilidad)*
> *"¿`sort()` muta el array? ¡Pensé que era funcional!"*

**Respuesta sugerida:**  
En JavaScript, `Array.prototype.sort()` **muta in-place**. Es una de las trampas más comunes. La solución: `[...arr].sort()` — copiar primero, ordenar después. La guía §3.3 tiene la tabla completa de métodos que mutan vs los que no.

---

**P2.4** *(🔵 Estratégico)*
> *"¿TypeScript puede garantizar inmutabilidad en profundidad (deep immutability) o solo superficial?"*

**Respuesta sugerida:**  
`readonly` solo garantiza la primera capa. Para objetos anidados, hay que usar `as const` (convierte literales a tipos inmutables), o librerías como `immer`. En runtime, `Object.freeze()` es la única opción nativa, pero es superficial.

---

**P2.5** *(🔵 Estratégico)*
> *"¿TypeScript implementa tail call optimization (TCO)?"*

**Respuesta sugerida:**  
No de forma confiable en V8. Es un tema abierto en TC39 (propuesta Stage 4 pero no implementada por todos los engines). La práctica recomendada en JS/TS: usar `reduce` en lugar de recursión explícita para arrays grandes.

---

### 🟠 Bloque 3 — HOF y clausuras (30 min)

**P3.1** *(🟡 Ansioso — alta probabilidad)*
> *"¿`reduce` puede reemplazar siempre a `map` y `filter`? ¿Por qué usaríamos los otros entonces?"*

**Respuesta sugerida:**  
Sí, `reduce` es la función más general (map y filter son casos especiales). Pero explicititud importa: `arr.filter(isEven).map(double)` comunica intención mejor que un `reduce` que hace ambas cosas. La composabilidad también es más clara.

---

**P3.2** *(🔴 Disperso / ⚫ Recursero)*
> *"¿Hay una librería que ya tenga `pipe`, `compose`, `map` y todo eso implementado?"*

**Respuesta sugerida:**  
Sí: `ramda`, `fp-ts` (TypeScript first), `lodash/fp`. Pero el objetivo de hoy es *entender cómo funcionan* implementándolas desde cero. En producción se usan las librerías; en este tema, el ejercicio manual es la herramienta de aprendizaje.

---

**P3.3** *(🟡 Ansioso)*
> *"En el ejercicio de `frecuencias`, ¿el spread `{ ...acc, [palabra]: ... }` no es costoso? ¿No muta el acumulador?"*

**Respuesta sugerida:**  
El spread en `reduce` crea un nuevo objeto en cada paso — sí, es O(n²) en objetos grandes (en almacenamiento). En producción, si la performance importa, se usan librerías como `immer` o mutación controlada en el acumulador. Para el aprendizaje del paradigma, el spread es la forma correcta de mostrar inmutabilidad.

---

**P3.4** *(🔵 Estratégico)*
> *"¿La clausura captura por referencia o por valor en JavaScript?"*

**Respuesta sugerida:**  
Por **referencia** a la variable del entorno léxico. Por eso `crearContador` puede modificar `cuenta` — la clausura mantiene una referencia viva a esa variable. Contraste con closures en lenguajes con semántica de valor (Haskell — no aplica porque no hay mutación).

---

### 🔴 Bloque 4 — Composición, currificación (20 min)

**P4.1** *(🟡 Ansioso — MUY ALTA probabilidad)*
> *"¿`addCurried` retorna una función o un número? Cuando escribo `addCurried(5)` no entiendo qué tengo en `add5`."*

**Respuesta sugerida:**  
`addCurried(5)` retorna **una función** — específicamente `(b: number) => 5 + b`. Eso es `add5`. Después, `add5(3)` aplica esa función a `3` y retorna `8`. TypeScript lo puede mostrar con `.d.ts`: el tipo de `add5` es `(b: number) => number`.

> **Tip docente:** Mostrar en el tipo del IDE: `const add5: (b: number) => number = addCurried(5)`. Verlo explícito en el tipado ayuda al ansioso.

---

**P4.2** *(🔴 Disperso — alta probabilidad — puede no preguntar pero estar perdido)*
> *"¿`compose` y `pipe` hacen lo mismo? ¿Cuándo uso uno y cuándo el otro?"*

**Respuesta sugerida:**  
Hacen lo mismo, en distinto orden. `compose(f, g)(x) = f(g(x))` — g primero (matemético). `pipe(g, f)(x) = f(g(x))` — g primero también, pero se lista g antes que f (orden de lectura natural). En código, `pipe` es más legible porque leés el pipeline de izquierda a derecha.

---

**P4.3** *(🔵 Estratégico)*
> *"En Haskell todas las funciones están currificadas por defecto. ¿Hay una forma de que TypeScript haga eso automáticamente?"*

**Respuesta sugerida:**  
No de forma nativa. `fp-ts` provee un helper `curry`. Pero en TypeScript la currificación manual es explícita por diseño — TypeScript no infiere que querés currificar una función binaria.

---

**P4.4** *(⚫ Recursero)*
> *"¿`pipe` de ramda es lo mismo que `pipe` que estamos implementando?"*

**Respuesta sugerida:**  
Sí, exactamente. Ramda's `pipe` acepta N funciones (no solo 2 como nuestra implementación binaria). La implementación de hoy entiende el núcleo; en producción, usar `ramda.pipe` o `fp-ts.pipe`.

---

### 🟡 Bloque 5 — Efectos y evaluación perezosa (10 min)

**P5.1** *(🔴 Disperso)*
> *"¿La evaluación perezosa es lo mismo que `async/await` o `Promise`?"*

**Respuesta sugerida:**  
No son lo mismo. `async/await` es para operaciones asíncronas (I/O, red). La evaluación perezosa (lazy) es sobre *cuándo se evalúa una expresión* — los generadores producen valores solo cuando se piden, sin importar si son async. Podés tener generadores síncronos y lazy.

---

**P5.2** *(🔵 Estratégico)*
> *"¿El patrón de 'aislar efectos en los bordes' es lo que hace la arquitectura hexagonal?"*

**Respuesta sugerida:**  
Exacto — la arquitectura hexagonal (ports & adapters) es una materialización architectural de este principio funcional. El núcleo puro (dominio) en el centro; los adaptadores (I/O, red, DB) en el borde. Es una de las maneras en que el paradigma funcional influye en el diseño de sistemas.

---

### 🔴 Bloque 6 — Mónadas (20 min)

**P6.1** *(🟡 Ansioso — alta probabilidad)*
> *"¿`Maybe` y `Either` son clases de TypeScript o librerías externas?"*

**Respuesta sugerida:**  
Son *patrones de diseño* — los estamos implementando desde cero para entender la idea. En producción existén en librerías: `fp-ts` provee `Option` (= `Maybe`) y `Either` con todas las operaciones. TypeScript nativo no los tiene.

---

**P6.2** *(🔴 Disperso — alta probabilidad)*
> *"¿Para qué usar `Maybe` si ya tenemos `try/catch`?"*

**Respuesta sugerida:**  
`try/catch` actúa por efectos secundarios (una excepción rompe el flujo). `Maybe`/`Either` son **valores** — podés pasarlos, componerlos y transformarlos como cualquier dato. Ventaja: el tipo te dice que puede fallar; no podés olvidarte de manejarlo. Con `try/catch` podés olvidarte y el error explota en runtime.

---

**P6.3** *(⚫ Recursero + 🟡 Ansioso)*
> *"¿Mónadas entran en el parcial?"*

**Respuesta sugerida:**  
La *intuición* sí: entender que `Promise.then()` actúa como `flatMap`, y que `Maybe`/`Either` son patrones para manejo de opcionalidad/errores. La implementación formal de mónadas (leyes, categoría) es Tema 05.

---

**P6.4** *(🔵 Estratégico)*
> *"¿`flatMap` en el array de JavaScript es una mónada?"*

**Respuesta sugerida:**  
Sí — en el sentido de que `Array` con `flatMap` satisface las leyes monádicas. Es una mónada no-determinista (cada elemento del array es una "rama posible"). Veremos esto en Tema 05.

---

## Preguntas anticipadas ESTUDIANDO SOLOS (guia-estudio.md)

Estas emergen del estudio autónomo. Refleja puntos donde la guía puede generar confusión adicional o donde el alumno llega con conceptos mal consolidados de clase.

---

**S1.1** *(🟡 Ansioso — guía §3.2)*
> *"La guía dice que las funciones puras son 'memoizables'. ¿Qué quiere decir eso exactamente?"*

**Respuesta sugerida:**  
Memoización = cachear el resultado. Si `f(x) = y` siempre para el mismo `x`, podés guardar `{x: y}` en un diccionario y devolver el valor cacheado sin recalcular. Solo funciona con funciones puras porque el resultado no cambia. Ver Sección §5 de la guía, y también la librería `memoize` de lodash.

---

**S1.2** *(🔴 Disperso — guía §4.3 — confusión persistent)*
> *"En la guía dice que `crearContador` no es puro. Pero también dice que clausuras capturan el entorno léxico. ¿No debería el entorno ser inmutable si es funcional?"*

**Respuesta sugerida:**  
En funcional *puro* (Haskell), sí — el entorno léxico es inmutable. Pero en TypeScript el entorno léxico puede contener variables mutables (`let`, `var`). `crearContador` es funcional en estructura (retorna funciones) pero no en pureza porque captura un `let`. La distinción es: *clausura* (captura de entorno) es ortogonal a *pureza* (no mutación).

---

**S1.3** *(🟡 Ansioso — guía §5.2 currificación)*
> *"La guía muestra `addCurried(3)(4)` pero el tipo dice `(a: number) => (b: number): number`. ¿Por qué la anotación de retorno `: number` está después del paréntesis y no después de la flecha?"*

**Respuesta sugerida:**  
Es la sintaxis de TypeScript para funciones que retornan funciones con tipo de retorno anotado. `(b: number): number` significa "función que recibe `b: number` y retorna `number`". Es equivalente a `(b: number) => number` como tipo. La guía §5.2 usa la forma más explícita para claridad tipográfica.

---

**S1.4** *(🔴 Disperso / ⚫ Recursero — guía §7 Mónadas)*
> *"La guía implementa `Option<A>` con un objeto con tag. ¿Por qué no usar directamente `A | null`?"*

**Respuesta sugerida:**  
`A | null` funciona para el caso simple. `Option<A>` (o `Maybe<A>`) es un *tipo con operaciones*: `mapOption`, `flatMapOption` — que encadenan transformaciones sin if/null-checks. La ventaja no es el tipo en sí sino las operaciones que vienen junto con él. Si usás `A | null`, tenés que verificar `null` manualmente en cada paso.

---

**S1.5** *(🔵 Estratégico — guía §6 efectos)*
> *"La guía habla de 'aislar efectos en los bordes'. ¿TypeScript tiene alguna forma de *forzar* eso en tiempo de compilación?"*

**Respuesta sugerida:**  
No nativamente. `fp-ts` tiene el tipo `IO<A>` que encapsula efectos, pero es convención, no forzado por el compilador. Haskell sí lo fuerza: el tipo `IO a` solo puede ejecutarse desde `main`. Eslint con reglas funcionales (`@typescript-eslint/no-unsafe-assignment`) puede aproximarse pero no es lo mismo.

---

## Preguntas TRAMPA / MISCONCEPTIONS a vigilar

Estas no son preguntas genuinas — son respuestas incorrectas que el docente puede anticipar en evaluaciones.

| Misconception | Perfil | Respuesta errónea que darán | Por qué es incorrecto |
|---|---|---|---|
| "Función pura = sin argumentos externos" | Disperso | "una función sin parámetros es pura" | Una función `const f = () => Date.now()` tiene 0 args y es impura |
| "Inmutable = `const`" | Ansioso | "`const arr` es inmutable" | `const` solo protege la referencia. `arr.push()` sigue funcionando |
| "Currificación = recursión" | Ansioso, Disperso | confunden la notación `f => g => h` con recursión | Son conceptos ortogonales |
| "Clausura = efecto secundario" | Ansioso | "toda clausura es impura" | Una clausura puede capturar valores inmutables y ser pura |
| "Mónada = Promise" | Estratégico | oversimplifica | `Promise` es una mónada específica; no toda mónada es async |

---

## Resumen de acciones pedagógicas

### Para implementar ANTES de la clase

| Acción | Motivo | Bloque |
|--------|--------|--------|
| Preparar "paso intermedio" de currificación (ver score-pedagogico §1) | Punto de mayor abandono del ansioso/disperso | B4 |
| Preparar pregunta de detección en B2 min 15 | Detecta si disperso perdió el hilo temprano | B2 |
| Anunciar en clase: "la guía está diseñada para repasar hoy en casa" | Activar al ansioso a usar la guía | B7 |

### Para implementar EN LA CLASE

| Momento | Acción |
|---------|--------|
| B6 inicio | Empezar con `try/catch` vs `Maybe` antes de mostrar el código — ancla en problema conocido |
| B4 durante | Demostrar el tipo inferido de `addCurried(5)` en el IDE — reduce ambigüedad de notación |
| B2 min ~15 | Cambiar `factor` en vivo en el ejemplo de `dobleExterno` para mostrar que el output cambia — hace el efecto secundario visible |

### Para la GUÍA (ya está bien estructurada)

- ✅ La guía-estudio.md es especialmente valiosa para el ansioso — compensa la clase, sube +12 puntos
- ✅ Los ejemplos trabajados acumulados (§8) son el recurso más utilizado por todos los perfiles
- ⚠️ Considerar agregar un callout explícito en §5.2 Currificación: *"Si esto te pareció confuso en clase, releerlo en esta guía con calma es la estrategia correcta."*
