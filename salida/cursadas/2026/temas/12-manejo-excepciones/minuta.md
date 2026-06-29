# Minuta de Clase — Tema 12: Manejo de Excepciones

> **Docente:** Matías Gel
> **Materia:** Paradigmas y Lenguajes de Programación · UNTDF IDEI 2026
> **Duración:** 120 minutos
> **Módulo:** IX | **Semana 12**
> **Estado:** Corregido · listo-para-guardrail
> **Referencia de soporte:** filminas.md (F-00 a F-17)
> **Bibliografía principal:** Sebesta Cap. 14, pp. 611–646
> **Bibliografía auxiliar:** Gabbrielli & Martini §7.3.1, Louden §9.5
> **Pipeline:** v3 · Corregido: 2026-06-28
> **Baseline:** clase_dada.txt · ChromaDB: ✅ verificado

---

## Modo de uso de esta minuta

Esta minuta es tu guion de clase: podés dictarla abriendo **solo este archivo**.
Cada sección corresponde a una filmina ([F-XX]) con: qué decir, cuánto tiempo, conceptos clave, preguntas anticipadas y transición.

---

## Objetivos de la clase

- Definir excepción, handler, raise y propagación (Sebesta §14.1)
- Distinguir terminación vs. reanudación
- Escribir try/catch/finally en TypeScript con excepciones user-defined
- Implementar Result\<T,E\> (enfoque funcional)
- Comparar Go, Kotlin y Rust como decisiones de diseño de lenguaje
- Identificar la relevancia en programación agéntica

---

## Distribución de tiempos (verificación = 120 min)

| Filmina | Título | Minutos |
|---------|--------|---------|
| F-00 | Portada | 2 |
| F-01 | Pregunta de apertura | 3 |
| F-02 | Objetivos | 2 |
| F-03 | ¿Qué es una excepción? | 8 |
| F-04 | El problema antes de las excepciones | 6 |
| F-05 | Historia: de PL/I a TypeScript | 5 |
| F-06 | Terminación vs. reanudación | 7 |
| F-07 | Las 8 preguntas de diseño | 5 |
| F-08 | try / catch / finally en TypeScript | 11 |
| F-09 | Propagación por el call stack | 7 |
| F-10 | Excepciones user-defined en TypeScript | 8 |
| F-11 | El enfoque funcional: Result\<T,E\> | 11 |
| F-12 | Go: errors as values | 7 |
| F-13 | Kotlin: sealed classes y try-expression | 7 |
| F-14 | Rust: Result\<T,E\> y el operador `?` | 7 |
| F-15 | Tabla comparativa | 8 |
| F-16 | Excepciones en programación agéntica | 11 |
| F-17 | Cierre y puntos clave | 5 |
| **Total** | | **120** |

---

## BLOQUE A — Fundamentos conceptuales (38 min)

---

### [F-00] Portada

**Tiempo:** 2 min
**Qué decir:**
- Anunciar el tema: "Hoy vemos Manejo de Excepciones — Módulo IX, el capítulo 14 de Sebesta."
- Contextualizar: "Es un tema que todo el mundo cree que sabe hacer, pero muy pocos lo hacen bien. Vamos a empezar desde los fundamentos antes de ver código."
- Dar el panorama de la clase: "Vamos a cubrir desde la teoría de Sebesta hasta cómo esto aplica en programación agéntica con MCP."

**Citas de soporte:** Sebesta, *Concepts of Programming Languages*, Cap. 14, pp. 611–646
**Transición:** Ir directamente a F-01 sin pausa.

---

### [F-01] Pregunta de apertura

**Tiempo:** 3 min
**Qué decir:**
- Leer los tres escenarios de la slide lentamente, haciendo pausa después de cada uno.
- "¿Qué hace tu programa cuando algo falla? No cuando hay un bug — sino cuando el entorno falla."
- Dejar 30–60 segundos para que los alumnos piensen o respondan en voz alta.
- No dar la respuesta aún: "Vamos a construir el vocabulario para responder esto con precisión."

**Conceptos clave:** excepción vs. bug, responsabilidad del manejo de errores
**Preguntas anticipadas:**
- *"¿No es lo mismo un error que una excepción?"* → "Muy buena pregunta — lo vamos a distinguir ahora."

**Transición:** "Para responder bien, primero necesitamos definir qué es exactamente una excepción. Sebesta tiene una definición muy precisa."

---

### [F-02] Objetivos

**Tiempo:** 2 min
**Qué decir:**
- Leer los objetivos rápidamente: "Esto es lo que vamos a cubrir en 120 minutos."
- Marcar los dos que suelen sorprender: "Vamos a ver dos enfoques distintos en TypeScript — imperativo y funcional. Y vamos a ver por qué esto importa en programación agéntica, que es algo que Sebesta no cubre porque su libro es de 2019."

**Transición:** "Empecemos por la base: ¿qué es una excepción?"

---

### [F-03] ¿Qué es una excepción? (Sebesta §14.1)

**Tiempo:** 8 min
**Qué decir:**
- Leer la cita de Sebesta en voz alta: *"Any unusual event, either erroneous or not, detectable by either hardware or software, that may require special processing."*
- Destacar: "Sebesta dice 'erroneous or not' — no toda excepción es un error. Archivo no encontrado no es un bug, es una condición esperada pero infrecuente."
- Explicar los 4 componentes: exception / handler / raise / catch.
- Mostrar la distinción: "Error de lógica en el código → bug, lo resolvés con debugging. Condición inesperada en runtime → excepción, la manejás con un handler."
- Dar un ejemplo extra: "Un agente de IA que llama a una tool y la tool falla — eso es una excepción, no un bug del código del agente."

**Citas de soporte:** [Sebesta, Cap. 14 §14.1, p. 611] — ChromaDB ✅ verificado (relevancia 0.695)
**Conceptos clave:** excepción (definición Sebesta), raise, handler, catch
**Preguntas anticipadas:**
- *"¿NullPointerException es un bug o una excepción?"* → "Puede ser las dos cosas. Si fue un bug del programador (olvidó chequear null) → bug. Si fue input inesperado del usuario → excepción."
- *"¿Toda excepción es un error?"* → "No. Sebesta lo dice explícitamente: 'erroneous or not'."

**Transición:** "Antes de ver cómo se manejan hoy, veamos el problema que existía antes del try/catch."

---

### [F-04] El problema antes de las excepciones

**Tiempo:** 6 min
**Qué decir:**
- Mostrar el código C con `errno`: "Este es el patrón pre-try/catch. ¿Qué problema tiene? Primero: fácil olvidarlo. Si no chequeas el `if (f == NULL)`, el programa sigue corriendo con un puntero nulo."
- Mostrar el callback de error (Louden §9.5): "Este fue un intento de solución: inyectar el handler como parámetro. El problema: solo cubre un tipo de error por función."
- Enumerar los problemas: "El código de manejo de errores mezcla con la lógica principal. `errno` es global y no es thread-safe. Y podés silenciar el error accidentalmente."
- "Estos problemas motivaron la invención del try/catch."

**Citas de soporte:** [Louden & Lambert, Cap. 9 §9.5, p. 406] — ChromaDB ✅ verificado (relevancia 0.606)
**Conceptos clave:** códigos de retorno, errno, callback de error, mezcla de concerns
**Preguntas anticipadas:**
- *"¿Go no usa exactamente esto?"* → "Muy buena observación — Go volvió a errores como valores, pero con el sistema de tipos más fuerte. Lo vemos en F-12."

**Transición:** "¿Cuándo apareció el try/catch? Veamos la historia rápida."

---

### [F-05] Historia: de PL/I a TypeScript

**Tiempo:** 5 min
**Qué decir:**
- Recorrer la timeline: "PL/I en los 60s fue el primero, pero usaba un modelo que hoy casi nadie usa: el modelo de reanudación. Ada en el 83 inventó el modelo que usamos hoy: terminación. C++ copió a Ada, Java refinó a C++, y TypeScript heredó de JavaScript/Java."
- Señalar la tendencia: "Los lenguajes más recientes — Go 2009, Kotlin 2011, Rust 2015 — están moviendo el pendulo hacia errores como valores. ¿Por qué? Lo vamos a entender en los próximos bloques."
- Mencionar ES2022 y Go 1.20 como evoluciones recientes: "Error.cause y errors.Join son de 2022 y 2023 — el tema sigue evolucionando."

**Conceptos clave:** PL/I (reanudación), Ada (terminación), tendencia hacia errores-como-valores
**Transición:** "Vamos a ver qué significa terminación vs. reanudación — que es la decisión de diseño más importante de este capítulo."

---

### [F-06] Terminación vs. reanudación

**Tiempo:** 7 min
**Qué decir:**
- Explicar el modelo de terminación: "Cuando se lanza una excepción, el scope donde se lanzó **se termina**. El handler toma control y no hay vuelta."
- Explicar el modelo de reanudación: "PL/I hacía esto: el handler ejecutaba y luego devolvía control al punto exacto donde se lanzó la excepción. Como si el raise fuera una llamada a función."
- Pregunta: "¿Por qué casi nadie usa reanudación hoy?" — esperar respuesta — "Porque el handler tendría que conocer el estado interno del caller para poder 'arreglarlo' y retomar. Es demasiado acoplamiento."
- Citar a Sebesta: *"Termination is obviously the simpler of the two models and is the model used in most contemporary languages."*
- Citar a Gabbrielli: complementa con la frase sobre "handling with termination".
- Nota sobre Go y Rust: "Go y Rust no tienen excepciones clásicas, pero su modelo de propagación sigue la semántica de terminación — no hay vuelta al punto de falla."

**Citas de soporte:**
- [Sebesta, Cap. 14 §14.2.3, p. 612] — ChromaDB ✅ verificado (relevancia 0.657): "Termination is obviously the simpler of the two models"
- [Gabbrielli & Martini, Cap. 7 §7.3.1, p. 282] — ChromaDB ✅ verificado (relevancia 0.743): "handling with termination"

**Conceptos clave:** terminación (dominante), reanudación (legacy PL/I), por qué terminación ganó
**Preguntas anticipadas:**
- *"¿Hay casos donde la reanudación sería útil?"* → "Sí — sistemas de corrección de errores en tiempo real, como algunos sistemas embebidos. Pero el costo en complejidad es alto."

**Transición:** "Sebesta va más allá y enumera 8 preguntas que todo lenguaje debe responder sobre excepciones. Veámoslas."

---

### [F-07] Las 8 preguntas de diseño (Sebesta §14.1)

**Tiempo:** 5 min
**Qué decir:**
- Leer las 8 preguntas de la slide.
- Enfatizar el cambio de perspectiva: "No me interesa que recuerden esta lista. Me interesa que entiendan que TypeScript, Go, Kotlin y Rust son respuestas **distintas** a estas mismas preguntas."
- Pregunta para la clase: "¿TypeScript tiene checked exceptions como Java?" — esperar — "No. Java dice 'sí' a la pregunta 8, TypeScript dice 'no'. Esa decisión cambia cómo escribís código."
- Mencionar que estas preguntas estructuran el resto de la clase: "Cada lenguaje que vamos a ver responde estas 8 preguntas de forma diferente."

**Citas de soporte:** [Sebesta, Cap. 14 §14.1, pp. 612–614] — ChromaDB ✅ verificado (relevancia 0.595)
**Conceptos clave:** checked vs. unchecked, las 8 dimensiones de diseño de Sebesta
**Transición:** "Ahora sí — código. Bloque B: TypeScript en acción."

---

## BLOQUE B — TypeScript: imperativo y funcional (37 min)

---

### [F-08] try / catch / finally en TypeScript

**Tiempo:** 11 min
**Qué decir:**
- Mostrar el ejemplo completo: "Vamos línea por línea."
- **try**: "Acá va el código que puede fallar. Si algo lanza, el resto del bloque try NO ejecuta."
- **catch**: "Recibe el objeto lanzado. En TypeScript, `error` es `unknown` — hay que hacer un `instanceof` para saber el tipo. Eso es una decisión de diseño de TS vs. Java."
- **throw dentro de catch**: "Esto es re-lanzar — capturamos, transformamos la excepción en una más específica, y la propagamos. Muy común en capas de servicio."
- **finally**: "Siempre ejecuta. No importa si hubo excepción o no. Ideal para cerrar conexiones, liberar recursos."
- Mostrar el flujo de control: los tres casos (sin excepción, con excepción capturada, con excepción propagada).
- Relación con las 8 preguntas de Sebesta: "Esto responde las preguntas 5 (continuación) y 6 (finalización)."

**Citas de soporte:** [Sebesta, Cap. 14 §14.1, preguntas 5 y 6, p. 613] — ChromaDB ✅ verificado
**Conceptos clave:** try, catch, finally, re-throw, flujo de control
**Demo sugerida:** Abrir TypeScript Playground, escribir el ejemplo y mostrar que el finally aparece en el log siempre.
**Preguntas anticipadas:**
- *"¿Puedo tener múltiples catch?"* → "En TS no — un solo catch con instanceof. En Java sí, con múltiples cláusulas. Otra decisión de diseño."
- *"¿Qué pasa si finally lanza?"* → "Eclipsa la excepción original. Cuidado con eso."

**Transición:** "¿Cómo sabe el catch dónde atrapar la excepción? Por la propagación por el call stack."

---

### [F-09] Propagación por el call stack

**Tiempo:** 7 min
**Qué decir:**
- Dibujar mentalmente (o señalar el diagrama): "Imaginen el stack de llamadas como una pila de cajas."
- Recorrer el ejemplo paso a paso: "fetch() lanza HttpError(404). Busca handler en loadUserData — lo encuentra, captura y relanza UserNotFoundError. Sube a fetchUserProfile — no tiene handler, propaga. Llega a main — lo captura."
- Enfatizar: "La información del error viaja con la excepción. En el handler podés acceder al statusCode, al message, al stack trace completo."
- Señalar la cita de Sebesta sobre la información disponible en el handler.
- Mencionar stack unwinding: "Este proceso de subir el stack se llama *stack unwinding*. Louden lo describe en §9.5."

**Citas de soporte:**
- [Sebesta, Cap. 14 §14.2, p. 614] — ChromaDB ✅ verificado (relevancia 0.645): "information about the exception is made available to the handler"
- [Louden & Lambert, Cap. 9 §9.5, p. 431] — ChromaDB ✅ verificado (relevancia 0.704): "stack unwinding"

**Conceptos clave:** propagación, call stack, información en el handler, stack unwinding
**Preguntas anticipadas:**
- *"¿Qué pasa si nadie captura la excepción?"* → "En Node.js: `UnhandledPromiseRejection` o el proceso muere. En browser: error en consola. Por eso siempre hay que tener un catch de último recurso en el entry point."

**Transición:** "Vimos cómo capturar. ¿Cómo hacemos nuestras propias excepciones con información útil?"

---

### [F-10] Excepciones user-defined en TypeScript

**Tiempo:** 8 min
**Qué decir:**
- Explicar la jerarquía: "Siempre extender de `Error`. Nunca lanzar un objeto plano — perdés el stack trace."
- Mostrar `AppError` como base: "El campo `code` es una string que identifica el tipo de error. Útil para logging y para switches sin instanceof anidados."
- Mostrar el fix de stack trace: "Este `captureStackTrace` es un detalle de TypeScript compilado a ES5 — en la práctica lo necesitás si querés que el stack trace muestre dónde se creó el error, no donde se creó la clase."
- Citar a Sebesta: "El thrown object puede tener cualquier cantidad de campos útiles para el handler. Eso es exactamente lo que hacemos."
- Error.cause (ES2022): "Desde ES2022 podés encadenar errores con `{ cause }`. Mismo patrón que `%w` en Go. Esto responde a la pregunta 4 de Sebesta — pasar información al handler."

**Citas de soporte:** [Sebesta, Cap. 14 §14.2, p. 614] — ChromaDB ✅ verificado (relevancia 0.866): "the thrown object could include any number of data fields that might be useful in the handler"
**Conceptos clave:** jerarquía de Error, campos custom, captureStackTrace, instanceof, Error.cause
**Preguntas anticipadas:**
- *"¿Por qué `this.name = this.constructor.name`?"* → "Porque sin eso, el error aparece como `Error` genérico en los logs, no como `HttpError`. Es un quirk de TypeScript."

**Transición:** "Hasta acá, manejo imperativo clásico. Ahora el giro: el enfoque funcional."

---

### [F-11] El enfoque funcional: Result\<T,E\>

**Tiempo:** 11 min
**Qué decir:**
- Motivar antes de mostrar el código: "¿Por qué molestarse? Porque `throw` es un efecto secundario — rompe el flujo de ejecución de una manera que es difícil de razonar en programación funcional. Si Tema 5 fue mónadas, ya conocen este concepto."
- Mostrar la definición de `Result<T,E>`: "Es una union type discriminada — o tenés `ok: true` con el valor, o `ok: false` con el error. TypeScript te fuerza a chequear antes de usar."
- Mostrar la implementación de `fetchUser`: "Fijate que no hay throw. Si algo falla, retornamos un valor."
- Mostrar el uso: "El TypeScript narrowing hace que si `result.ok` es true, el compilador sabe que `result.value` es `User`. Exhaustividad verificada en compilación."
- Mostrar la composición con map/flatMap: "Acá es donde brilla — podés encadenar operaciones sin try/catch anidados."
- Conexión curricular: "Este tipo es la mónada Either. En Haskell es `Either a b`. En fp-ts es `Either`. La idea es la misma. [Conexión curricular: Tema 5 — Mónadas. Result<T,E> es la mónada Either]"

**Citas de soporte:** [Gabbrielli & Martini, Cap. 7 §7.3.1, p. 282] — ChromaDB ✅ verificado (relevancia 0.575): "An exception is not an anonymous event — it has a name, often a value in one of the language's types"
**Conceptos clave:** Result<T,E>, union type discriminada, exhaustividad en compilación, mónada Either
**Preguntas anticipadas:**
- *"¿Cuándo uso throw y cuándo uso Result?"* → "Buena pregunta — lo respondemos en F-15 con la tabla."
- *"¿Qué pasa con async?"* → "Wrapeamos: `Promise<Result<T,E>>`. Es más verboso pero mantiene la exhaustividad."

**Transición:** "Ahora veamos cómo otros lenguajes toman estas mismas decisiones de forma diferente."

---

## BLOQUE C — Contraste multi-lenguaje (29 min)

---

### [F-12] Go: errors as values

**Tiempo:** 7 min
**Qué decir:**
- Contexto: "Go fue diseñado en Google en 2007. Los diseñadores vinieron de C y Unix. Tomaron una decisión radical: no hay try/catch."
- Mostrar el patrón: "Las funciones retornan `(T, error)`. Tupla implícita. El caller está **obligado** a hacer algo con el error — o lo ignora explícitamente con `_`, que es raro y no recomendado."
- Mostrar `%w` y `errors.As`: "Esto es el sistema de wrapping de errores de Go 1.13+. Podés encadenar errores y después 'desenvolverlos' con `errors.As` para encontrar el tipo original."
- `defer resp.Body.Close()`: "defer es el `finally` de Go — ejecuta cuando la función retorna, haya error o no."
- Ventajas e inconvenientes: leer la tabla honestamente. "Go tiene razón en lo de la legibilidad explícita. Pero `if err != nil` cada tres líneas es real — los programadores Go lo bromean."
- Go 1.20 errors.Join: "Útil para validaciones que pueden fallar en múltiples puntos. errors.Is/As recorren el árbol completo."

**Conceptos clave:** errors as values, retorno múltiple, %w wrapping, errors.As, defer, errors.Join
**Preguntas anticipadas:**
- *"¿Panic/recover es como try/catch?"* → "Solo en la superficie. panic es para errores irrecuperables, como un índice fuera de rango. recover en producción es raro. No es el patrón idiomático."

**Transición:** "Kotlin también rechaza las checked exceptions de Java, pero lo hace de una manera muy distinta."

---

### [F-13] Kotlin: sealed classes y try-expression

**Tiempo:** 7 min
**Qué decir:**
- Mostrar el sealed class: "La diferencia con Result<T,E> de TypeScript es que Kotlin usa una jerarquía de clases con `sealed`. El compilador sabe todos los subtipos posibles."
- El gran punto: "when en Kotlin es **exhaustivo** cuando trabajás con sealed classes. Si no cubrís todos los casos, el compilador te da error. Eso es lo que TypeScript intenta lograr con los union types."
- try como expresión: "En Kotlin, try retorna un valor. Podés asignarlo directamente. Esto lo hace integrable con código funcional de una manera más limpia que Java."
- Sin checked exceptions: "A diferencia de Java, Kotlin eliminó las checked exceptions. No hay que declarar throws. Esa es la respuesta de Kotlin a la pregunta 8 de Sebesta."

**Conceptos clave:** sealed class, when exhaustivo, try-expression, sin checked exceptions
**Preguntas anticipadas:**
- *"¿Por qué Kotlin eliminó checked exceptions si Java las tenía?"* → "Experiencia práctica. Las checked exceptions en Java terminaban en `catch (Exception e) { e.printStackTrace() }` — exactamente lo que querían evitar."

**Transición:** "Rust va más lejos — no hay excepciones en runtime por garantía del lenguaje."

---

### [F-14] Rust: Result\<T,E\> y el operador `?`

**Tiempo:** 7 min
**Qué decir:**
- Contexto: "Rust fue diseñado con una promesa: si compila, es seguro. Eso incluye el manejo de errores."
- Mostrar el enum FetchError: "Los errores en Rust son enum — algebraic data types. No hay jerarquía de clases, hay variantes."
- El operador `?`: Explicar paso a paso. "Es azúcar sintáctica. Evalúa el Result — si es Ok, desenvuelve el valor. Si es Err, retorna el error inmediatamente." Mostrar la versión desazucarada.
- Drop trait: "Rust no tiene finally porque tiene RAII — cuando una variable sale de scope, su `drop` es llamado automáticamente. La limpieza es parte del tipo, no del flujo de control."

**Conceptos clave:** Result<T,E>, enum, operador ?, RAII/Drop, sin runtime exceptions
**Preguntas anticipadas:**
- *"¿Qué es `panic!` en Rust?"* → "Es para errores que no deberían ocurrir en código correcto — como índice fuera de rango. En producción se puede configurar para hacer unwind o abortar. No es el mecanismo principal de manejo de errores."

**Transición:** "Ahora que vimos los cuatro lenguajes, comparemos sistemáticamente."

---

### [F-15] Tabla comparativa

**Tiempo:** 8 min
**Qué decir:**
- Recorrer la tabla fila por fila: "Mecanismo, flujo, exhaustividad, composabilidad, stack unwinding, limpieza de recursos, verbosidad."
- Señalar los extremos: "TS funcional y Rust son los más seguros en términos de exhaustividad. Go es el más explícito pero el más verboso. TS imperativo es el más familiar para equipos con background Java/JS."
- Leer las reglas de selección: "No hay una respuesta correcta universal. Es una decisión de diseño que depende del contexto."
- Pregunta abierta: "¿En qué contextos prefieren el enfoque funcional Result sobre el throw?"

**Conceptos clave:** tabla de trade-offs, regla de selección según contexto
**Preguntas anticipadas:**
- *"¿Podemos mezclar throw y Result en el mismo proyecto?"* → "Sí, y es lo más común. Generalmente: throw para errores inesperados de sistema, Result para errores de negocio esperados."

**Transición:** "Último bloque — algo que Sebesta no cubre porque es de 2026: programación agéntica."

---

## BLOQUE D — Agéntica y cierre (16 min)

---

### [F-16] Excepciones en programación agéntica

**Tiempo:** 11 min
**Qué decir:**
- Contexto: "Esto no está en Sebesta. Es el contexto de la cátedra y de la industria actual."
- Explicar context poisoning: "Un agente de IA encadena llamadas. Si el paso 2 falla silenciosamente y el agente no lo sabe, el paso 3 trabaja con basura. El agente da resultados incorrectos con total confianza."
- Citar a Anthropic: "Los agentes autónomos tienen mayor costo y potencial de errores en cascada — cada error no manejado se amplifica en los pasos siguientes."
- Validación del estado: "Anthropic recomienda obtener ground truth del entorno en cada paso. Nunca asumir que un paso anterior fue exitoso sin verificar."
- Interfaz Agente-Computadora (ACI): "Hay que invertir en el diseño de tools tanto como en el diseño de prompts. Poka-yoke tus tools — diseñalas para que sea difícil cometer errores."
- Mostrar el ToolResult de MCP: "El protocolo MCP de Anthropic (que usamos en el edu-mcp-server de esta cátedra) especifica que las tools deben retornar `isError: true` cuando fallan. Eso es exactamente el enfoque funcional aplicado."
- Mostrar withRetry: "Este patrón es central en sistemas agénticos — reintentar con backoff exponencial, pero solo si el error es recuperable. La diferencia entre un error de red (retriable) y un error de autenticación (no retriable) importa."
- Conexión cátedra: "publish_loop.py hace exactamente esto — 3 reintentos, registra cada error en error-registry.jsonl. Lo hemos ejecutado ustedes mismos."

**Citas de soporte:** [Anthropic, "Building effective agents", dic. 2024]
**Conceptos clave:** context poisoning, errores en cascada, typed errors MCP, withRetry, isRetryable, ACI, poka-yoke
**Preguntas anticipadas:**
- *"¿Cómo sabe el agente si es retryable o no?"* → "Por el tipo del error. `NetworkTimeoutError` → retry. `AuthenticationError` → no retry. Por eso los tipos de error importan."

**Transición:** "Cerramos con los puntos que se llevan de hoy."

---

### [F-17] Cierre y puntos clave

**Tiempo:** 5 min
**Qué decir:**
- Leer los 5 puntos en voz alta, pausando después de cada uno para que los alumnos los anoten.
- "Si tienen que quedarse con una sola cosa: el manejo de excepciones es una **decisión de diseño de lenguaje**. Sebesta dedica un capítulo entero a ella porque afecta todo — la legibilidad, la correctitud, la composabilidad."
- Conexiones: repasar los tres links curriculares — Tema 11 (control de flujo), Tema 5 (mónadas), Tema 13 (módulos).
- Anunciar próxima clase: "Tema 13 — Abstracción Procedural y Modularidad. Vamos a ver cómo los contratos de error cruzan límites de módulos."

**Conceptos clave (resumen):**
1. Excepción = evento anómalo (Sebesta §14.1)
2. Terminación domina los lenguajes modernos
3. Propagación por call stack hasta encontrar handler
4. Dos filosofías: throw vs. Result
5. En agéntica: errores tipados son obligatorios

**Cierre:** "¿Preguntas antes de cerrar?"

---

## Apéndice — Preguntas frecuentes adicionales

**P: ¿TypeScript tiene checked exceptions?**
R: No. TypeScript no puede inferir qué excepciones puede lanzar una función — `throw` puede lanzar cualquier valor (no solo Error). Hay propuestas para esto (`throws` annotation) pero no están en el lenguaje. Por eso el enfoque `Result<T,E>` es más seguro en TS que en Java.

**P: ¿`finally` siempre ejecuta incluso si hago return dentro del try?**
R: Sí. Si haces `return value` dentro del try, el finally ejecuta antes de que el valor sea retornado al caller. Si el finally también tiene un return, ese valor eclipsa al del try.

**P: ¿Qué biblioteca usar para Result en TypeScript en proyectos reales?**
R: `neverthrow` (simple, Railway Oriented Programming), `fp-ts` (completa, mais verbosa), o implementar `Result` propio (como mostramos en clase). Para proyectos pequeños, la implementación propia es suficiente.

**P: ¿Por qué Go decidió no tener try/catch si era la tendencia?**
R: Los diseñadores de Go (Rob Pike, Ken Thompson, Robert Griesemer) argumentaron que las excepciones hacen el flujo de control difícil de razonar. El paper "Errors are values" de Rob Pike (2015) explica la filosofía.