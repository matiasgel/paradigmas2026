# FAQ Anticipado — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Agente:** 🎓 Simulador de Alumno (student-simulator)
> **Fecha:** 2026-03-10
> **Modo:** Batch — 4 perfiles (estratégico, ansioso, disperso, recursero)
> **Fuente:** Simulación dual — experiencia en clase (minuta + filminas) + autoestudio (guia-estudio.md)
> **Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI

---

## Cómo usar este documento

Las preguntas están agrupadas por el momento en que el alumno las formula. Para cada pregunta se indica:
- **Perfil origen** — qué tipo de alumno la hace
- **Prioridad** — 🔴 Alta (frecuente o crítica), 🟡 Media, 🟢 Baja
- **Respuesta sugerida** — para que el docente pueda responder sin preparación adicional

---

## SECCIÓN 1 — Preguntas durante o inmediatamente después de clase

---

### F01 — ¿Tenemos que entender el código en ensamblador LC-3?

**Perfil:** Ansioso | **Prioridad:** 🔴 Alta

**Por qué surge:** El Bloque 3 incluye 13 líneas de ensamblador LC-3. El docente aclara verbalmente que "no hay que entenderlo", pero el alumno ansioso no internaliza esa instrucción si viene en tono informal.

**Respuesta sugerida:**
> *"No. El LC-3 está ahí como punto de contraste — para que veas lo que C ya te abstrae. No hay ninguna pregunta en el TP sobre ensamblador. Lo que sí necesitás entender es por qué C es más legible que LC-3, y por qué TypeScript agrega otra capa encima de eso."*

**Acción preventiva:** Decirlo explícitamente al mostrar F-13: *"Este código NO entra al TP. Está para que lo vean."*

---

### F02 — ¿TypeScript es interpretado o compilado?

**Perfil:** Disperso, Ansioso | **Prioridad:** 🔴 Alta

**Por qué surge:** La explicación de F-16 introduce tres términos cercanos: "interpretación pura", "compilación pura" y "lenguaje intermedio". El alumno que se perdió el razonamiento intermedio queda con la pregunta binaria.

**Respuesta sugerida:**
> *"Ni uno ni otro, en sentido estricto. TypeScript se compila a JavaScript (eso hace `tsc`), y luego ese JavaScript es ejecutado por V8 que hace compilación JIT en runtime. Es el modelo de 'máquina intermedia' que explica Gabbrielli — igual que Java, que produce bytecode que ejecuta la JVM. En la guía de estudio hay una tabla comparativa en la sección 4.2 que lo resume bien."*

---

### F03 — ¿Todo el Bloque 5 (Schmidt & Runfola) entra al TP?

**Perfil:** Estratégico | **Prioridad:** 🟡 Media

**Por qué surge:** El Bloque 5 tiene una referencia bibliográfica específica y datos numéricos (20/50/30%). El alumno estratégico evalúa si vale la pena memorizarlos.

**Respuesta sugerida:**
> *"El TP tiene una pregunta sobre el Bloque 5 (P05). No hay que memorizar figuras ni páginas exactas — sí tener claro el concepto del loop trust-but-verify y por qué los paradigmas son relevantes para trabajar con IA. Los porcentajes exactos no entran."*

---

### F04 — Un lenguaje multiparadigma, ¿es "mejor" que un lenguaje puro?

**Perfil:** Disperso | **Prioridad:** 🟡 Media

**Por qué surge:** al presentar TypeScript como multiparadigma superior a Kotlin, el alumno inquieto generaliza la pregunta.

**Respuesta sugerida:**
> *"Depende del contexto. Haskell (funcional puro) es mejor que TypeScript para ciertas tareas donde la garantía de ausencia de efectos laterales vale más que la flexibilidad. Prolog es mejor para razonamiento lógico. 'Mejor' siempre implica 'mejor para qué problema'. Los multiparadigma son más flexibles pero pagan con inconsistencia de estilo en equipos grandes."*

---

### F05 — ¿La máquina abstracta de Gabbrielli es un concepto formal o una metáfora?

**Perfil:** Ansioso | **Prioridad:** 🟡 Media

**Por qué surge:** La palabra "abstracta" genera incertidumbre sobre el nivel de formalismo requerido.

**Respuesta sugerida:**
> *"Es un concepto técnico preciso, no una metáfora — pero no vamos a hacer matemática formal con él en esta materia. Lo que necesitás entender es la idea: todo lenguaje define un ejecutor, y ese ejecutor puede ser implementado por compilación, interpretación o algo intermedio. En esta materia usamos el concepto para entender cómo se ejecuta TypeScript."*

---

### F06 — Si Smalltalk es OO puro y Java es OO, ¿por qué Java no es tan puro como Smalltalk?

**Perfil:** Estratégico | **Prioridad:** 🟢 Baja

**Por qué surge:** En F-09 y F-10 Smalltalk aparece como "OO puro" y Java como "OO mainstream". El alumno detallista nota la diferencia.

**Respuesta sugerida:**
> *"Buena observación. Java tiene tipos primitivos (`int`, `boolean`, etc.) que no son objetos — eso rompe la pureza. En Smalltalk hasta un entero es un objeto que recibe mensajes. Esta tensión la vamos a ver más en el Tema 8 cuando trabajemos OO en profundidad."*

---

### F07 — ¿Hay que instalar TypeScript antes de la Clase 2?

**Perfil:** Todos | **Prioridad:** 🔴 Alta (logística)

**Por qué surge:** El cierre de la Clase 1 menciona que en la Clase 2 "vamos a escribir código".

**Respuesta sugerida:**
> *"No es obligatorio instalarlo. Para la Clase 2 pueden usar el Deno Playground en el navegador — es el mismo entorno que usamos hoy. El enlace está en la guía de estudio y en las filminas (F-17). Si quieren tenerlo local, instrucciones en la guía."*

---

## SECCIÓN 2 — Preguntas que surgen estudiando la guía de estudio

---

### G01 — Q3 de autoevaluación dice "sin mutación de estado observable" — ¿observable significa que el estado existe pero no se ve?

**Perfil:** Ansioso | **Prioridad:** 🟡 Media

**Por qué surge:** La respuesta de Q3 en la guía usa el adverbio "observable" y el alumno ansioso lo interpreta como una afirmación oculta sobre la existencia de estado.

**Respuesta sugerida:**
> *"La palabra 'observable' está usada en el sentido de 'accesible al programador'. En el funcional puro, no existe estado mutable desde el punto de vista del programador — no hay variable con un valor que cambie a lo largo del tiempo. `const result = datos.reduce(...)` no tiene estado que mute después de que se asigna: es un valor inmutable. El contra-ejemplo seria `let acc = 0; for ... { acc += x }` donde `acc` sí muta."*

---

### G02 — ¿La diferencia entre `let acc` y `const result` es la misma diferencia que entre imperativo y funcional?

**Perfil:** Disperso | **Prioridad:** 🔴 Alta

**Por qué surge:** Es una confusión frecuente y pedagógicamente crítica. El alumno confunde el indicador lexical (`let`/`const`) con el paradigma subyacente.

**Respuesta sugerida:**
> *"`let` vs `const` es una pista útil pero no es la definición del paradigma. Podría existir código funcional que use `const` para todo, pero también código imperativo con `const` para algunas variables. La diferencia real está en si el cómputo depende de estado que muta — si hay una variable cuyo valor va cambiando instrucción a instrucción, eso es imperativo, independientemente de cómo se declara. En TypeScript, `let` casi siempre indica imperativo porque se usa justamente para declarar variables que van a mutar, pero no es la única señal posible."*

---

### G03 — ¿El glosario de la guía cubre todo lo que puede entrar en el TP?

**Perfil:** Estratégico, Recursero | **Prioridad:** 🟡 Media

**Por qué surge:** El Recursero quiere saber si el Glosario es suficiente para prepararse. El Estratégico quiere confirmar que no se está perdiendo términos.

**Respuesta sugerida:**
> *"El glosario cubre los 22 conceptos centrales del tema y está alineado con las 10 preguntas del TP. Pero hay preguntas que requieren no solo conocer el término sino recordar un momento específico de clase (como P05), y eso el glosario solo no resuelve. Usá el glosario para verificar conceptos, pero no como sustituto de leer la teoría y hacer la autoevaluación."*

---

### G04 — ¿Hay que saber los años exactos (Church 1936, Robinson 1965)?

**Perfil:** Ansioso | **Prioridad:** 🟡 Media

**Por qué surge:** La guía menciona años específicos para el cálculo lambda y la lógica de resolución.

**Respuesta sugerida:**
> *"No hay que memorizar años exactos. Sí tener claro que el cálculo lambda precede a las computadoras (lo que explica por qué el funcional no depende de Von Neumann) y que la lógica de resolución es también una base matemática previa al paradigma lógico. Los años son contexto histórico, no datos de evaluación."*

---

### G05 — En la pregunta P02 del TP, ¿por qué incluyen la opción JVM si es obviamente falsa?

**Perfil:** Recursero | **Prioridad:** 🟡 Media

**Por qué surge:** El Recursero memoriza la respuesta correcta desde el glosario pero no entiende el propósito pedagógico de las trampas bien diseñadas.

**Respuesta sugerida:**
> *"La opción JVM en P02 no es para alguien que simplemente memoriza. Es un distractor efectivo porque TypeScript y Kotlin (el lenguaje que usábamos antes en este cursado) sí compilan a JVM — hay una asociación plausible. Quien estuvo atento en clase y procesó el pipeline de F-16 responde sin dudar. Quien solo memorizó listas puede confundirse. Las preguntas trampa están diseñadas para distinguir comprensión de memorización."*

---

### G06 — ¿Cuál es la diferencia entre el `.js` intermedio de TypeScript y el bytecode `.class` de Java? ¿No hacen lo mismo?

**Perfil:** Disperso, Ansioso | **Prioridad:** 🟡 Media

**Por qué surge:** La tabla de la sección 4.2 de la guía los pone en el mismo rol (lenguaje intermedio), y el alumno curioso ve la equivalencia estructural pero intuye que hay una diferencia.

**Respuesta sugerida:**
> *"Buena pregunta. Ambos son lenguajes intermedios, pero con características distintas. El JavaScript que genera TypeScript es un lenguaje de propósito general, completo y legible por humanos — podés leerlo y entenderlo. El bytecode `.class` de Java está diseñado para ser ejecutado por la JVM, no para ser leído por humanos — es casi binario con estructura de stack. La similitud es funcional (ambos desacoplan el lenguaje fuente del hardware), pero la implementación es muy diferente. El JS intermedio es intencional — permite que TypeScript corra en cualquier entorno JS (Node, Deno, browser) sin recompilación."*

---

### G07 — C tiene tipos y funciones, ¿qué lo haría funcional?

**Perfil:** Estratégico | **Prioridad:** 🟢 Baja (profundización)

**Por qué surge:** La guía compara C (imperativo) con TypeScript funcional, y el alumno avanzado nota que C también tiene funciones.

**Respuesta sugerida:**
> *"C tiene funciones en el sentido léxico (subrutinas con nombre), pero no en el sentido del cálculo lambda. Para que un lenguaje sea funcional se necesitan: (1) funciones como valores de primera clase — asignables a variables, pasables como argumentos; (2) funciones de orden superior (`map`, `reduce`); (3) ausencia de efectos laterales por convención o restricción del lenguaje. C permite pasar punteros a funciones, pero no tiene clausuras ni inmutabilidad por diseño. TypeScript sí tiene todo eso. Esta distinción la vamos a ver en profundidad en los Temas 3–5."*

---

### G08 — ¿La autoevaluación Q7 (trust but verify) es un ejercicio que va a entrar al TP?

**Perfil:** Estratégico, Ansioso | **Prioridad:** 🟡 Media

**Por qué surge:** Q7 de la autoevaluación es un ejercicio aplicado (análisis de un output de IA). Varios alumnos preguntan si el TP tiene ejercicios de este tipo.

**Respuesta sugerida:**
> *"El TP1 es un quiz de opción múltiple. Q7 en la guía no es el formato del TP, pero el concepto que ejercita (identificar si la IA respetó la restricción de paradigma) sí está representado en P05. Vale la pena resolver Q7 antes del TP para consolidar ese razonamiento."*

---

## SECCIÓN 3 — Confusiones de alto impacto a monitorear

Estas no son preguntas directas sino errores conceptuales que los alumnos pueden tener sin formularlos como pregunta. Recomendado chequear activamente.

| ID | Confusión | Perfil en riesgo | Cómo detectarla | Corrección |
|----|-----------|-----------------|-----------------|-----------|
| CMI-01 | "El paradigma de un lenguaje = su sintaxis" — tipear `reduce` no hace funcional al código | Disperso, Recursero | Preguntar: *"¿Por qué la versión con `let acc` es imperativa si usa la misma función?"* | Distinción `let` como indicador vs. mutación como definición |
| CMI-02 | "TypeScript es un lenguaje interpretado porque V8 lo ejecuta en runtime" | Ansioso, Recursero | Preguntar: *"¿En qué momento `tsc` participa del proceso?"* | El pipeline tiene dos etapas con roles distintos |
| CMI-03 | "Von Neumann es solo historia — no es relevante para escribir código hoy" | Disperso | Preguntar: *"¿Por qué `let acc = 0` es imperativo? ¿De dónde viene esa idea?"* | La conexión Von Neumann → asignación → estado es la respuesta |
| CMI-04 | "`const` garantiza que el código es funcional" | Todos | Mostrar código con múltiples `const` pero con efectos laterales | La inmutabilidad de `const` es léxica (variable no reasignable), no semántica |
| CMI-05 | "AI Fluency = saber usar herramientas de IA" sin necesidad de paradigmas | Recursero | Preguntar post-demo: *"¿Cómo sabrías si la IA eligió el paradigma correcto?"* | La jerarquía de Schmidt & Runfola: sin paradigmas, AI Fluency no es alcanzable |

---

## SECCIÓN 4 — Preguntas de alto valor pedagógico (si el tiempo y la energía del aula lo permiten)

Estas preguntas, si surgen en clase, merecen expandirse aunque impliquen salirse brevemente del guión:

| Pregunta | Por qué vale expandirla |
|----------|------------------------|
| *"¿Hay lenguajes que solo permiten escribir en un estilo — que no te dejen usar el otro?"* | Introduce Haskell (funcional puro) y Prolog (lógico puro) con motivación real. Anticipa Temas 3–7. |
| *"¿La IA podría aprender paradigmas en lugar de solo escribir código?"* | Excelente entrada al debate de AGI vs. herramientas especializadas. Conecta con OA5. |
| *"¿`map` existe en C?"* | Respuesta: no nativamente. Motiva la diferencia entre lenguaje y biblioteca. Conecta con funciones de orden superior. |

---

*FAQ generado por student-simulator · testing pedagógico Tema 01 · UNTDF/IDEI 2026*
