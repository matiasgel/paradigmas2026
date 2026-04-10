# FAQ Anticipado — Tema 04: Aspectos Avanzados de Programación Funcional

**Generado:** 2026-04-09 | **Agente:** student-simulator (modo Batch — 4 perfiles)
**Fuentes:** minuta.md (42 filminas) + guia-estudio.md + tp.md (20 ejercicios) + calibración Tema 03

---

## En clase 🎓

### Bloque 1 — Fundamentos avanzados (F-01 a F-13)

**Q1.** "¿`const` hace que un array sea inmutable?"
- **Perfil predictor:** disperso (misconception arrastrada de Tema 03)
- **Filmina:** F-05 (Inmutabilidad)
- **Respuesta sugerida:** "No. `const` impide reasignar la variable, pero el contenido del array puede mutar con `push`, `splice`, etc. Para inmutabilidad real en TS usamos spread `[...arr, nuevo]` o `as const` para literales."
- **Intervención:** Mostrar en vivo: `const a = [1,2]; a.push(3); console.log(a)` → funciona → "¿Sorprendidos?"

**Q2.** "¿Cuál es la diferencia entre `filter` y `reduce`? ¿No pueden hacer lo mismo?"
- **Perfil predictor:** recursero
- **Filmina:** F-07, F-08
- **Respuesta sugerida:** "`filter` selecciona elementos (misma forma, ≤ cantidad). `reduce` colapsa toda la colección a un valor (cualquier forma). Sí, `reduce` puede hacer lo que `filter` hace, pero `filter` expresa la intención más claramente."

**Q3.** "¿El pipeline de Clojure con `->>` es lo mismo que encadenar `.filter().map()` en TS?"
- **Perfil predictor:** estratégico
- **Filmina:** F-12
- **Respuesta sugerida:** "Conceptualmente sí: ambos componen transformaciones. La diferencia es que en Clojure `->>` pasa el resultado como último argumento de cada forma, y no depende de que sean métodos de un objeto. Es más general."

**Q4.** "¿Por qué Clojure no necesita tipos si TypeScript sí?"
- **Perfil predictor:** ansioso
- **Filmina:** F-11, F-12
- **Respuesta sugerida:** "Clojure usa tipado dinámico: los errores de tipo se detectan en runtime. TS usa tipado estático: se detectan en compilación. Ninguno es 'mejor' — son trade-offs. Con tipos estáticos tenés más seguridad antes de ejecutar; sin ellos tenés más flexibilidad y menos ceremonia."

### Bloque 2 — Abstracciones y efectos (F-14 a F-24)

**Q5.** "¿`Result` y `Maybe` son lo mismo?"
- **Perfil predictor:** ansioso, recursero
- **Filmina:** F-15, F-17
- **Respuesta sugerida:** "No. `Result<T,E>` modela operaciones que pueden fallar con una razón (`error: E`). `Maybe<T>` modela ausencia de valor sin explicar por qué (`some: false`). Ejemplo: buscar un usuario → `Maybe` (está o no). Dividir por cero → `Result` (el error importa)."

**Q6.** "¿Para qué sirve `Result` si ya tenemos `try/catch`?"
- **Perfil predictor:** recursero, disperso
- **Filmina:** F-15, F-16
- **Respuesta sugerida:** "Con `try/catch` el error es invisible en la firma de la función — no sabés que puede fallar hasta que falla. Con `Result`, el tipo te obliga a manejar ambos casos. El compilador te avisa si te olvidás del caso de error."

**Q7.** "¿Qué es un transducer? No entendí la diferencia con un pipeline normal."
- **Perfil predictor:** disperso, ansioso
- **Filmina:** F-19, F-20, F-21
- **Respuesta sugerida:** "Un pipeline normal (`filter → map → reduce`) crea un array intermedio en cada paso. Un transducer fusiona las transformaciones en una sola pasada: procesa cada elemento por todas las etapas antes de pasar al siguiente. Ganancia: menos memoria, una sola recorrida."
- **Intervención:** Dibujar en pizarra: 3 arrays intermedios vs 1 recorrida

**Q8.** "¿Los ADT de TypeScript son como las clases de Java?"
- **Perfil predictor:** recursero
- **Filmina:** F-14
- **Respuesta sugerida:** "No exactamente. Los ADT modelan variantes con un discriminador (`kind`, `status`). En Java usarías herencia o sealed classes. En TS es más liviano: un tipo unión con un campo literal que distingue cada caso. No hay herencia — solo datos."

**Q9.** "¿`defmacro` en Clojure es como un template en C++?"
- **Perfil predictor:** estratégico
- **Filmina:** F-24
- **Respuesta sugerida:** "Comparten la idea de generar código en tiempo de compilación, pero los macros de Clojure trabajan sobre la estructura del código como datos (homoiconicidad). No es sustitución textual como en C/C++ — es transformación del AST."

### Bloque 3 — Concurrencia y metaprogramación (F-25 a F-34)

**Q10.** "¿`core.async` es como las goroutines de Go?"
- **Perfil predictor:** disperso, estratégico
- **Filmina:** F-26, F-27
- **Respuesta sugerida:** "La inspiración es la misma: CSP (Communicating Sequential Processes). Los `go` blocks de Clojure son similares a goroutines: procesos livianos que se comunican por canales. La diferencia es que en Clojure corren sobre el thread pool de la JVM con macro-transformación, no son threads reales del OS."

**Q11.** "¿Cuándo uso STM vs core.async vs agentes?"
- **Perfil predictor:** estratégico, recursero
- **Filmina:** F-28, F-29
- **Respuesta sugerida:** "Regla simple: STM cuando necesitás transacciones coordinadas sobre múltiples refs (como una transferencia bancaria). core.async cuando tenés flujos de datos entre productores y consumidores. Agentes cuando tenés estado independiente que se actualiza de forma asíncrona sin coordinación."

**Q12.** "¿`async/await` en TS es programación funcional?"
- **Perfil predictor:** ansioso
- **Filmina:** F-30, F-31
- **Respuesta sugerida:** "No automáticamente. `async/await` es azúcar sintáctico sobre Promises. Es funcional si las funciones async son puras respecto a su entrada — pero si hacen I/O (fetch, lectura de archivos), tienen efectos secundarios. La clave es separar la lógica pura del I/O (F-32)."

**Q13.** "¿Qué diferencia hay entre un canal y una promesa?"
- **Perfil predictor:** ansioso, disperso
- **Filmina:** F-33
- **Respuesta sugerida:** "Una promesa se resuelve UNA vez con UN valor. Un canal puede transmitir MUCHOS valores en el tiempo. Promesa = sobre con una carta. Canal = tubo por donde pasan muchos mensajes."

### Bloque 4 — Práctica guiada (F-35 a F-42)

**Q14.** "¿En el taller puedo usar solo TypeScript para los dos ejercicios?"
- **Perfil predictor:** recursero, disperso
- **Filmina:** F-35
- **Respuesta sugerida:** "No — el ejercicio requiere comparar ambos lenguajes. La idea es que veas las mismas abstracciones en dos sintaxis distintas. El de Clojure es más corto de lo que parece."

**Q15.** "¿Los transducers y STM entran en el TP?"
- **Perfil predictor:** recursero, ansioso
- **Filmina:** F-42
- **Respuesta sugerida:** "Sí. El TP tiene ejercicios de transducers (ej11, ej12) y STM (ej16). Pero los ejercicios están graduados — podés empezar por los de pipeline (ej01-ej06) y avanzar después."

---

## Estudiando solos 📖

### Sobre la guía de estudio

**Q16.** "La guía dice 4-5 horas de estudio, ¿es real?"
- **Perfil predictor:** ansioso
- **Respuesta sugerida:** "Es un estimado para lectura comprensiva + ejercicios de autoevaluación. Si venís con B1 sólido de clase, probablemente sean 3-4h. Si necesitás repasar Clojure básico, puede ser 5-6h."

**Q17.** "¿La autoevaluación de la guía es igual al TP?"
- **Perfil predictor:** recursero
- **Respuesta sugerida:** "No. La autoevaluación es conceptual (preguntas de comprensión). El TP es implementación de código. La autoevaluación te prepara para entender qué hacer, el TP te pide hacerlo."

### Sobre el TP

**Q18.** "¿Puedo hacer los ejercicios de Clojure sin instalar nada localmente?"
- **Perfil predictor:** disperso
- **Respuesta sugerida:** "Los tests se ejecutan en GitHub Actions con cada push, pero para desarrollar necesitás un entorno local. Instalá Leiningen (gestor de Clojure) y Java 21. Instrucciones en el README del repo."

**Q19.** "El ej08 (Result<T,E>) me da error de tipos. ¿Cómo sé cuál variante estoy manejando?"
- **Perfil predictor:** ansioso
- **Respuesta sugerida:** "Usá el campo discriminador `status`. Dentro de un `if (r.status === 'ok')`, TypeScript sabe que `r.value` existe (narrowing). Si `r.status === 'error'`, TypeScript sabe que `r.error` existe. Revisá §2.2 de la guía de estudio."

**Q20.** "¿Cómo pruebo un `go` block de core.async localmente?"
- **Perfil predictor:** estratégico, recursero
- **Respuesta sugerida:** "En el REPL de Clojure (`lein repl`), evaluá el namespace del ejercicio. Los `go` blocks se ejecutan asincrónicamente — usá `(<!! canal)` para bloquear y leer el resultado en el REPL. Los tests ya hacen esto automáticamente."

**Q21.** "El ej19 (integrador TS) pide combinar pipeline + Result + async. ¿Por dónde empiezo?"
- **Perfil predictor:** ansioso, disperso
- **Respuesta sugerida:** "Empezá por la parte pura: el pipeline de transformación de datos (filter/map/reduce). Después envolvé cada operación riesgosa en `Result`. Finalmente, hacé que las funciones async devuelvan `Promise<Result<T,E>>`. Paso a paso, no todo junto."

**Q22.** "¿Qué pasa si mis tests pasan localmente pero fallan en GitHub Actions?"
- **Perfil predictor:** todos
- **Respuesta sugerida:** "Verificá: (1) que no dependas de archivos locales que no subiste, (2) que las versiones coincidan (Node 20, Java 21), (3) que los tests no dependan de orden de ejecución. Mirá los logs de GitHub Actions para el error exacto."

---

## Priorización para el docente

### Preguntas que DEBEN aparecer en clase (preparar respuesta)

| Prioridad | Pregunta | Filmina | Intervención |
|-----------|----------|---------|--------------|
| 🔴 Alta | Q1 — const ≠ inmutable | F-05 | Demo en vivo con `push` |
| 🔴 Alta | Q7 — ¿Qué es un transducer? | F-19 | Dibujo en pizarra: 3 arrays vs 1 pasada |
| 🔴 Alta | Q5 — Result vs Maybe | F-15,17 | Tabla comparativa lado a lado |
| 🟡 Media | Q13 — Canal vs promesa | F-33 | Analogía sobre/tubo |
| 🟡 Media | Q12 — async/await ≠ funcional | F-30 | Ejemplo de efecto impuro con await |
| 🟢 Baja | Q11 — STM vs async vs agentes | F-28,29 | Tabla resumen (ya en filminas) |

### Preguntas que aparecerán durante el TP (preparar en foro/canal)

| Pregunta | Ejercicio | Perfil |
|----------|-----------|--------|
| Q19 — narrowing con Result | ej08 | ansioso |
| Q20 — probar go block en REPL | ej15 | estratégico |
| Q21 — integrador por dónde empezar | ej19 | ansioso, disperso |
| Q22 — tests local vs Actions | todos | todos |

---

*Próxima actualización: post-clase-tema04-2026 (comparar FAQs predichos vs reales)*
