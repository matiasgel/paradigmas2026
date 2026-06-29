# Minuta de Clase - Tema 11

## Expresiones y Estructuras de Control

> Docente: Matías Gel
> Curso: Laboratorio de Programación y Lenguajes · UNTDF IDEI 2026
> Referencia de soporte: filminas.md (F-00 a F-44)
> Duración total: 180 minutos (constraint absoluto)
> Lenguaje principal: TypeScript
> Bibliografía principal: Sebesta, Concepts of Programming Languages, caps. 7–8
> Bibliografía auxiliar: Gabbrielli-Martini caps. 4–6, Louden cap. 8
> Baseline de corrección: clase_dada.txt (859 líneas)

---

## Modo de uso de esta minuta

- Esta minuta está pensada para lectura docente previa y conducción en aula.
- Cada entrada referencia una filmina y define foco conceptual, guion, tiempo asignado, conceptos clave, preguntas anticipadas y transición.
- El docente debe poder dar la clase usando solo esta minuta, sin abrir ningún otro archivo.
- Los tiempos asignados suman exactamente 180 minutos.

---

## BLOQUE A — Fundamentos de expresiones y semántica (F-00 a F-16)

### [F-00] Portada

- **Tiempo:** 3 min
- **Foco:** presentar el tema y su alcance dentro del módulo VIII.
- **Guion:** "Hoy abordamos expresiones y estructuras de control. No es solo 'cómo escribir un if', es entender qué decide un lenguaje cuando evalúa una expresión y por qué eso importa para escribir código confiable."
- **Conceptos clave:** alcance del tema, módulo VIII, posición en el cursado.
- **Preguntas anticipadas:** ninguna — es apertura.
- **Transición:** "Empecemos con una pregunta que va a romper la intuición."

### [F-01] Pregunta de apertura

- **Tiempo:** 5 min
- **Foco:** activar conflicto cognitivo con un caso concreto.
- **Guion:** Mostrar `let x = 1; const r = x++ + x`. Preguntar: "¿Dos expresiones equivalentes siempre se comportan igual?" Listar las cinco fuentes de divergencia: precedencia, asociatividad, orden de evaluación, efectos colaterales, coerciones. Dejar la pregunta abierta: "¿El problema está en la matemática o en la semántica del lenguaje?"
- **Conceptos clave:** precedencia, asociatividad, orden de evaluación, efectos colaterales, coerciones.
- **Preguntas anticipadas:** "¿Y eso no da error en TypeScript?" — responder que TypeScript lo permite pero es ilegible; el compilador no protege contra esto.
- **Transición:** "Para responder esto, necesitamos objetivos claros."

### [F-02] Objetivos

- **Tiempo:** 3 min
- **Foco:** explicitar metas de la secuencia.
- **Guion:** Leer los siete objetivos. Remarcar que no se verá solo "cómo" escribir control, sino "cuándo" y "por qué" cada estructura. El último objetivo —evaluar decisiones de diseño de lenguajes modernos— es el hilo conductor.
- **Conceptos clave:** distinción expresión/sentencia, precedencia, short-circuit, selección, iteración, decisiones de diseño.
- **Preguntas anticipadas:** ninguna.
- **Transición:** "Veamos el mapa de cómo vamos a recorrer todo esto."

### [F-03] Mapa conceptual del tema

- **Tiempo:** 3 min
- **Foco:** ubicar los ejes del tema en una progresión.
- **Guion:** Recorrer el mapa: Expresiones → Evaluación → Asignación y efectos → Booleanos y short-circuit → Selección → Iteración → Saltos restringidos y mecanismos modernos. Aclarar que cada bloque construye sobre el anterior.
- **Conceptos clave:** progresión conceptual, dependencia entre bloques.
- **Preguntas anticipadas:** ninguna.
- **Transición:** "Empecemos por la distinción más básica."

### [F-04] Expresión y sentencia

- **Tiempo:** 4 min
- **Foco:** distinción base entre lo que produce valor y lo que causa efecto.
- **Guion:** Definir expresión como construcción sintáctica que se evalúa; sentencia como unidad ejecutable. Mostrar que en TypeScript una asignación también es expresión: `let y = (x = 5)`. Preguntar: "¿Qué valor tiene `y`?" Respuesta: 5, porque la asignación devuelve el valor asignado.
- **Conceptos clave:** expresión, sentencia, asignación como expresión.
- **Preguntas anticipadas:** "¿En todos los lenguajes pasa eso?" — No. En Kotlin la asignación no es expresión de valor.
- **Transición:** "Y esta distinción no es académica: tiene consecuencias prácticas."

### [F-05] Por qué esta distinción importa

- **Tiempo:** 4 min
- **Foco:** riesgo semántico de mezclar cálculo y mutación.
- **Guion:** Mostrar `function sumar(x) { total += x; return total }`. Explicar: si una expresión solo calcula, es más fácil razonar. Si además muta estado, aparece riesgo semántico. La misma sintaxis puede mezclar cálculo y efecto. Mencionar que Haskell favorece expresiones puras, TypeScript permite ambos estilos, Rust controla más estrictamente la mutabilidad.
- **Conceptos clave:** expresión pura, expresión con efecto, transparencia referencial.
- **Preguntas anticipadas:** "¿Y eso es malo?" — No necesariamente, pero rompe la transparencia referencial y dificulta el razonamiento.
- **Transición:** "Para entender por qué una expresión se evalúa como se evalúa, necesitamos el AST."

### [F-06] AST y parseo

- **Tiempo:** 6 min
- **Foco:** el árbol sintáctico abstracto fija la semántica de la expresión.
- **Guion:** Explicar que la precedencia determina la estructura del árbol de parseo; la asociatividad resuelve empates. El AST captura estructura, no evaluación: es una representación intermedia. Parseo y evaluación son fases distintas. Mostrar `const r = a + b * c` → `a + (b * c)` porque `*` tiene mayor precedencia y queda más profundo en el árbol. Dibujar el árbol en pizarra si es posible.
- **Conceptos clave:** AST, precedencia, asociatividad, parseo vs. evaluación.
- **Preguntas anticipadas:** "¿El AST garantiza el orden de evaluación?" — No. El AST fija la forma, no el orden temporal.
- **Transición:** "Veamos la precedencia en detalle."

### [F-07] Precedencia de operadores

- **Tiempo:** 4 min
- **Foco:** la precedencia determina la agrupación sintáctica.
- **Guion:** Mostrar que multiplicación precede a suma. Los paréntesis expresan intención. La tabla de precedencia es decisión de diseño. Mostrar `const r = a + b << c` — preguntar: "¿Se suma antes o se desplaza antes?" Dejar la duda: la respuesta depende del lenguaje.
- **Conceptos clave:** precedencia, agrupación, paréntesis como intención.
- **Preguntas anticipadas:** "¿Y cómo sé cuál tiene más precedencia?" — Hay que consultar la tabla del lenguaje. No es universal.
- **Transición:** "Y precisamente porque no es universal, hay que tener cuidado."

### [F-08] Precedencia no es una ley universal

- **Tiempo:** 3 min
- **Foco:** las reglas varían entre lenguajes.
- **Guion:** Las reglas aritméticas suelen coincidir, pero las lógicas, bit a bit y de asignación varían. Mostrar `const a = 2 + 3 * 4` → 14 y `const b = (2 + 3) * 4` → 20. TypeScript, Java, Kotlin: reglas similares. Python agrega `**` como exponenciación. Scheme evita el problema usando notación prefija.
- **Conceptos clave:** variación entre lenguajes, notación prefija, exponenciación.
- **Preguntas anticipadas:** "¿Scheme no tiene precedencia?" — Correcto, la notación prefija elimina la ambigüedad.
- **Transición:** "Y cuando dos operadores tienen la misma precedencia, entra la asociatividad."

### [F-09] Asociatividad

- **Tiempo:** 4 min
- **Foco:** empate entre operadores de misma precedencia.
- **Guion:** Asociatividad izquierda: mayoría de los aritméticos. Asociatividad derecha: exponenciación, asignación en C/Java, ternario. Mostrar `const r = 10 - 3 - 2` → `(10 - 3) - 2 = 5`. Caso crítico: `a = b = c = 5` en C evalúa de derecha a izquierda. Mostrar Scheme `(- (- 10 3) 2)` — no depende de asociatividad infija.
- **Conceptos clave:** asociatividad izquierda, asociatividad derecha, asignación encadenada.
- **Preguntas anticipadas:** "¿Por qué la asignación es derecha?" — Para permitir `a = b = c = 5` asignando primero a `c`, luego a `b`, luego a `a`.
- **Transición:** "Cuando la asociatividad no basta para aclarar, los paréntesis son tu amigo."

### [F-10] Paréntesis como decisión semántica

- **Tiempo:** 3 min
- **Foco:** parentizar no es redundante si mejora la lectura.
- **Guion:** Si una expresión exige recordar demasiadas reglas, se usan paréntesis. Mostrar `const habilitado = (usuario.activo && usuario.emailVerificado) || usuario.esAdmin`. Los paréntesis aquí expresan intención: primero la conjunción, luego la disyunción.
- **Conceptos clave:** paréntesis como intención, legibilidad.
- **Preguntas anticipadas:** "¿No es redundante?" — No. Es redundancia productiva: comunica intención al lector.
- **Transición:** "Hasta aquí hablamos de la forma. Ahora hablemos del orden temporal."

### [F-11] Orden de evaluación de operandos

- **Tiempo:** 6 min
- **Foco:** parseo ≠ orden de evaluación temporal.
- **Guion:** El AST indica estructura. El lenguaje define, o deja sin definir, el orden temporal. Con funciones puras, puede no importar. Con efectos colaterales, importa mucho. Explicar que C/C++ deja el orden sin especificar en muchos casos; TypeScript define más orden que C pero no elimina el problema de diseño. Este es el punto donde la semántica operacional entra en juego.
- **Conceptos clave:** orden temporal, semántica operacional, funciones puras vs. efectos.
- **Preguntas anticipadas:** "¿Y TypeScript garantiza izquierda a derecha?" — En muchos contextos sí, pero no en todos. No hay que depender de eso.
- **Transición:** "Veamos un caso concreto donde esto explota."

### [F-12] Efectos colaterales en expresiones

- **Tiempo:** 6 min
- **Foco:** fragilidad semántica con side effects.
- **Guion:** Mostrar `let i = 1; const r = i++ + ++i`. Preguntar: "¿Cuánto vale `r`?" La respuesta depende del orden garantizado por el lenguaje. Contrastar con C: `i = i++ + ++i` — en C/C++ algunos casos son indefinidos o no especificados. Mostrar Rust: `i += 1` — no existe `i++`. En TypeScript puede estar definido pero seguir siendo ilegible. Regla de diseño: evitar expresiones que mezclen cálculo y mutación en la misma sentencia.
- **Conceptos clave:** post-incremento, pre-incremento, comportamiento indefinido, ilegibilidad.
- **Preguntas anticipadas:** "¿Entonces TypeScript está bien definido?" — Puede estar definido, pero el código sigue siendo ilegible. Definido ≠ correcto.
- **Transición:** "Y si la asignación es expresión, hay un bug histórico que aparece."

### [F-13] Asignación como expresión

- **Tiempo:** 4 min
- **Foco:** decisiones de lenguaje sobre assignment expressions.
- **Guion:** Mostrar C idiomático: `while ((c = getchar()) != EOF) { procesar(c); }` — getchar asigna y su valor se compara con EOF. Mostrar TypeScript: `let y = (x = 5) + 3`. Mostrar Kotlin: `x = 5` — no se usa asignación como expresión de valor. Riesgo: lenguajes que admiten assignment expressions en condiciones habilitan el bug clásico `if (x = 0)`. C lo permite; compiladores modernos emiten warning con `-Wall`. Rust, Swift, Kotlin restringen el patrón por diseño.
- **Conceptos clave:** assignment expression, bug clásico, restricción por diseño.
- **Preguntas anticipadas:** "¿Por qué C lo permite si es peligroso?" — Porque es útil en patrones idiomáticos como getchar. El trade-off es poder vs. seguridad.
- **Transición:** "Veamos cómo prevenir ese bug."

### [F-14] Prevención de bugs de asignación

- **Tiempo:** 3 min
- **Foco:** estrategias de prevención del bug `if (x = 0)`.
- **Guion:** Yoda conditions: `if (0 == x)` → una asignación accidental falla al compilar. Activar warnings: `-Wparentheses`, `-Wall` en GCC/Clang. Lenguajes modernos (Rust, Swift, Kotlin) eliminan el problema por diseño. Linters como ESLint/TSLint detectan automáticamente este patrón.
- **Conceptos clave:** Yoda conditions, warnings, linters, diseño de lenguaje.
- **Preguntas anticipadas:** "¿Yoda conditions no son feo?" — Sí, pero prevenir un bug silencioso justifica la fealdad. En lenguajes modernos no hace falta.
- **Transición:** "Otra fuente de sorpresas: las coerciones."

### [F-15] Conversión y coerción

- **Tiempo:** 4 min
- **Foco:** conversión explícita vs. coerción implícita.
- **Guion:** Mostrar la tabla: conversión explícita (cast) — control del programador, riesgo bajo. Coerción widening — control del lenguaje, riesgo medio. Coerción narrowing — riesgo alto, pérdida de datos. Sobrecarga de operadores — riesgo variable. Principio: la coerción implícita puede enmascarar errores de tipo. Lenguajes con tipado estático fuerte (Haskell, Rust) minimizan coerciones implícitas.
- **Conceptos clave:** cast, widening, narrowing, sobrecarga, tipado fuerte.
- **Preguntas anticipadas:** "¿TypeScript tiene coerción?" — Sí, y es fuente de bugs clásicos como `[] + {}`.
- **Transición:** "Antes de pasar al bloque de booleanos, consolidemos."

### [F-16] Control conceptual — Bloque A

- **Tiempo:** 3 min
- **Foco:** consolidar el bloque A con preguntas orales.
- **Guion:** Hacer las tres preguntas: (1) ¿Cuál es la diferencia entre precedencia y orden de evaluación? (2) ¿Cuándo una assignment expression en un if se convierte en bug? (3) Dar un ejemplo donde la coerción implícita produce un resultado diferente al esperado. No esperar respuestas perfectas — usarlas para detectar gaps.
- **Conceptos clave:** consolidación de precedencia, asignación, coerción.
- **Preguntas anticipadas:** Las preguntas mismas son la actividad.
- **Transición:** "Ahora entremos al mundo de los booleanos, donde el short-circuit cambia todo."

---

## BLOQUE B — Booleanos, short-circuit y seguridad semántica (F-17 a F-25)

### [F-17] Álgebra booleana aplicada

- **Tiempo:** 5 min
- **Foco:** operadores lógicos como control del flujo de evaluación.
- **Guion:** En código real, `&&` y `||` controlan qué sub-expresiones se evalúan. La conjunción y disyunción permiten codificar precondiciones de forma declarativa. Operadores lógicos con y sin short-circuit tienen semánticas distintas. El short-circuit es semántica perezosa de operadores lógicos. No son solo tablas de verdad: son control de flujo.
- **Conceptos clave:** operadores lógicos, control de flujo, semántica perezosa.
- **Preguntas anticipadas:** "¿Y los operadores bit a bit cortocircuitan?" — No. `&` y `|` evalúan ambos operandos siempre.
- **Transición:** "Y qué cuenta como true depende del lenguaje."

### [F-18] Truthiness entre lenguajes

- **Tiempo:** 4 min
- **Foco:** semántica de verdad no booleana.
- **Guion:** Mostrar la tabla: C usa int (0 es falsy), Python y TypeScript son flexibles, Java es estricto, Kotlin da error de compilación con `""`. Regla de diseño: no migrar intuiciones de truthiness de un lenguaje a otro sin validar la semántica local. Mostrar `if ("")` en TypeScript (válido, falsy) vs. Kotlin (error).
- **Conceptos clave:** truthiness, falsy, bool estricto, variación semántica.
- **Preguntas anticipadas:** "¿Por qué TypeScript es tan flexible?" — Herencia de JavaScript, que prioriza interoperabilidad sobre seguridad.
- **Transición:** "Y si todo se evalúa siempre, hay problemas."

### [F-19] Evaluación estricta

- **Tiempo:** 3 min
- **Foco:** todos los operandos se evalúan siempre.
- **Guion:** La evaluación estricta evalúa todos los operandos antes de aplicar el operador lógico. Predecible y conveniente para análisis formal. Pero puede ejecutar sub-expresiones inválidas innecesariamente (división por cero, acceso null). Pascal original usaba `and`/`or` sin garantía de short-circuit. La evaluación estricta favorece la verificabilidad; el short-circuit favorece la corrección operativa.
- **Conceptos clave:** evaluación estricta, verificabilidad, Pascal.
- **Preguntas anticipadas:** "¿Pascal no tenía short-circuit?" — El Pascal original no lo garantizaba. Algunos dialectos modernos sí.
- **Transición:** "Veamos la alternativa: short-circuit."

### [F-20] Short-circuit

- **Tiempo:** 5 min
- **Foco:** evaluación que se detiene cuando el resultado ya es conocido.
- **Guion:** `p && q`: si `p` es false, `q` no se evalúa. `p || q`: si `p` es true, `q` no se evalúa. Es una herramienta de corrección semántica, no solo de rendimiento. Permite usar la primera condición como guarda de seguridad de la segunda. El short-circuit es semántica perezosa de operadores lógicos.
- **Conceptos clave:** short-circuit, guarda, corrección semántica.
- **Preguntas anticipadas:** "¿Es lo mismo que lazy evaluation?" — No exactamente. Es pereza localizada en operadores lógicos, no evaluación perezosa general.
- **Transición:** "Veamos cómo usarlo defensivamente."

### [F-21] Patrón defensivo con short-circuit

- **Tiempo:** 5 min
- **Foco:** evitar división por cero y acceso null.
- **Guion:** Mostrar `if (x !== 0 && y / x > 2)` — guarda contra división por cero. Mostrar `if (user !== null && user.isActive())` — guarda contra acceso null. Mostrar C: `if (p != NULL && p->value > 0)`. Explicar: si la primera condición falla, la segunda nunca se evalúa. Es una forma práctica de guarda operacional. Invertir el orden destruye la guarda y puede causar runtime error.
- **Conceptos clave:** guarda, división por cero, acceso null, orden de condiciones.
- **Preguntas anticipadas:** "¿Y si pongo la división primero?" — Segfault o NaN. El orden es semántico, no estético.
- **Transición:** "Pero el short-circuit también puede jugar en contra si hay side effects."

### [F-22] Side effects en booleanos: anti-patrón

- **Tiempo:** 3 min
- **Foco:** mezclar predicados con efectos en operadores lógicos.
- **Guion:** Mostrar el anti-patrón: `if (isReady() || logAndMutate())` — logAndMutate puede no ejecutarse si isReady es true. Mostrar la versión correcta: `const logged = logAndMutate(); if (isReady() || logged)`. Principio: separar predicados (sin efectos) de funciones con efectos colaterales. Short-circuit convierte un efecto secundario en un efecto condicional → comportamiento inesperado.
- **Conceptos clave:** anti-patrón, efecto condicional, separación de responsabilidades.
- **Preguntas anticipadas:** "¿Y si quiero que el efecto sea condicional?" — Entonces sé explícito con un if, no lo escondas en un operador lógico.
- **Transición:** "Veamos cómo se ven los operadores en distintos lenguajes."

### [F-23] Operadores lógicos: comparativa por lenguaje

- **Tiempo:** 3 min
- **Foco:** variaciones de sintaxis y significado.
- **Guion:** Mostrar la tabla con AND lógico, OR lógico, AND bit, OR bit y NOT lógico para C/C++, Java, TypeScript, Python y Kotlin. Resaltar que Python usa `and`/`or`/`not` (palabras) mientras C usa símbolos. Kotlin usa `&&`/`||` para lógicos y `and`/`or` para bit a bit.
- **Conceptos clave:** operadores lógicos, operadores bit a bit, variación de sintaxis.
- **Preguntas anticipadas:** "¿Por qué Python usa palabras?" — Legibilidad. Guido van Rossum priorizó claridad sobre concisión.
- **Transición:** "Y TypeScript tiene operadores especializados para null."

### [F-24] Null safety con operadores lógicos

- **Tiempo:** 4 min
- **Foco:** `?.` y `??` como short-circuit especializado.
- **Guion:** Mostrar TypeScript: `usuario?.direccion?.ciudad` — optional chaining corta en null/undefined. `entrada ?? "sin nombre"` — nullish coalescing, default solo para null/undefined (no para 0 ni ""). Combinados: `usuario?.direccion?.codigoPostal ?? "0000"`. Mostrar Kotlin: `?:` equivalente. Mostrar Rust: `and_then` y `map`. Semántica: `?.` es short-circuit ante null; `??` es más estricto que `||`.
- **Conceptos clave:** optional chaining, nullish coalescing, `?:` en Kotlin, `and_then`/`map` en Rust.
- **Preguntas anticipadas:** "¿Por qué `??` es mejor que `||`?" — Porque `||` cortocircuita ante 0 y "", que pueden ser valores válidos. `??` solo corta ante null/undefined.
- **Transición:** "Otra técnica de seguridad: guard clauses."

### [F-25] Guard clauses

- **Tiempo:** 3 min
- **Foco:** reducir anidamiento con cláusulas de guarda.
- **Guion:** Mostrar la versión sin guard clauses: anidamiento profundo con `if (x != null) { if (x >= 0) { ... } }`. Mostrar la versión con guard clauses: `if (x == null) return "faltante"; if (x < 0) return "inválido"; return ok`. El flujo plano es más legible. Early return reduce complejidad accidental sin cambiar la semántica.
- **Conceptos clave:** guard clause, early return, anidamiento, legibilidad.
- **Preguntas anticipadas:** "¿No es malo tener muchos returns?" — No. Un return por guarda es más legible que un anidamiento profundo.
- **Transición:** "Pasamos al bloque de selección, donde el debate sobre goto abre la historia."

---

## BLOQUE C — Selección estructurada y decisiones de diseño (F-26 a F-33)

### [F-26] Programación estructurada y el debate sobre goto

- **Tiempo:** 5 min
- **Foco:** contexto histórico del goto y criterio actual.
- **Guion:** `goto` permite saltos arbitrarios a cualquier punto. Aumenta poder de expresión local; reduce trazabilidad y verificabilidad global. Dijkstra (1968): "Go To Statement Considered Harmful". Las estructuras de control buscan control explícito: entrada única, salida única. El goto moderno restringido (C, C++) sobrevive para manejo de errores y salida de bucles anidados. Mostrar Go: `goto inicio` con etiqueta — restringido a la misma función, sin saltar inicializaciones.
- **Conceptos clave:** goto, Dijkstra, programación estructurada, goto restringido en Go.
- **Preguntas anticipadas:** "¿Go tiene goto?" — Sí, pero restringido. No puedes saltar a otra función ni saltarte declaraciones de variables.
- **Transición:** "La estructura de selección más básica: if-else."

### [F-27] If y else if: árbol de decisiones

- **Tiempo:** 5 min
- **Foco:** selección simple y encadenada.
- **Guion:** Propiedades: ramas mutuamente excluyentes, evaluación en orden, else como caso no capturado, orden de condiciones importa. Mostrar TypeScript: cascada de `if/else if` para grados. Mostrar Kotlin: `if` como expresión que devuelve valor. Resaltar que en Kotlin el if es expresión, en TypeScript es sentencia.
- **Conceptos clave:** if-else, ramas excluyentes, if como expresión en Kotlin.
- **Preguntas anticipadas:** "¿Por qué el orden importa?" — Porque una condición más general antes de una específica puede oscurecer ramas. `if (x > 0)` antes de `if (x > 10)` hace que la segunda nunca se ejecute para x > 10.
- **Transición:** "Cuando hay muchos casos por valor, switch es más claro."

### [F-28] Switch: selección múltiple

- **Tiempo:** 5 min
- **Foco:** switch como alternativa estructurada a cadenas de if-else.
- **Guion:** Switch clásico discrimina por valor. C/JavaScript/TypeScript heredan la necesidad de break. Kotlin reemplaza switch por when. Rust usa match exhaustivo. El problema de confiabilidad aparece cuando hay continuación implícita de una rama a otra (fallthrough). Mostrar TypeScript con break y Kotlin `when` sin break. La decisión de diseño afecta confiabilidad.
- **Conceptos clave:** switch, break, fallthrough, when, match, exhaustividad.
- **Preguntas anticipadas:** "¿Por qué C tiene fallthrough?" — Histórico. Era útil para agrupar casos, pero generó tantos bugs que lenguajes modernos lo eliminaron.
- **Transición:** "La evolución natural del switch es pattern matching."

### [F-29] Pattern matching: evolución del control múltiple

- **Tiempo:** 3 min
- **Foco:** pattern matching como selección estructural sobre datos.
- **Guion:** Switch clásico discrimina por valor (escalar, enum). Pattern matching discrimina por estructura del dato — forma, tipo y desestructuración. Disponible en Haskell, Scala, Rust, Python 3.10+, Java 21+. Tabla de despacho: extensibilidad en dominios abiertos. En lenguajes con tipos algebraicos, pattern matching reemplaza la selección como estructura primaria.
- **Conceptos clave:** pattern matching, tipos algebraicos, desestructuración, extensibilidad.
- **Preguntas anticipadas:** "¿TypeScript tiene pattern matching?" — No nativamente, pero se simula con type guards y discriminated unions.
- **Transición:** "Pero antes de elegir estructura, hay que medir el costo del anidamiento."

### [F-30] Complejidad cognitiva del anidamiento

- **Tiempo:** 3 min
- **Foco:** cada nivel de anidamiento incrementa la carga cognitiva.
- **Guion:** Cada nivel de anidamiento extra multiplica los paths de ejecución posibles. Las ramas profundas elevan el riesgo de paths no testeados. La complejidad ciclomática mide el número de paths linealmente independientes. Guard clauses y early return reducen complejidad accidental sin cambiar la semántica. Regla práctica: máximo 3 niveles de anidamiento antes de extraer una función.
- **Conceptos clave:** complejidad ciclomática, anidamiento, paths, regla de 3 niveles.
- **Preguntas anticipadas:** "¿3 niveles es poco?" — Es un umbral práctico. Más de 3 suele indicar que falta una abstracción.
- **Transición:** "Con eso en mente, veamos criterios para elegir."

### [F-31] Criterios para elegir estructura de selección

- **Tiempo:** 3 min
- **Foco:** matriz de decisión entre if-else, switch y tabla de despacho.
- **Guion:** Mostrar la tabla: pocas ramas (2-3) → if-else óptimo. Muchas ramas (>5) → switch legible, tabla extensible. Condiciones complejas → if-else natural. Cambio frecuente → tabla (Open/Closed). Exhaustividad → switch con default. La elección no es estética: es una decisión de ingeniería de mantenimiento.
- **Conceptos clave:** matriz de decisión, Open/Closed, exhaustividad, mantenibilidad.
- **Preguntas anticipadas:** "¿Y si tengo 4 ramas?" — Zona gris. Si los casos son por valor, switch. Si son por condición, if-else.
- **Transición:** "Veamos la tabla de despacho en código."

### [F-32] Despacho por tabla

- **Tiempo:** 4 min
- **Foco:** separar lógica de control de los datos.
- **Guion:** Mostrar `const handlers: Record<string, () => void> = { INT: parseIntToken, ID: parseIdToken, STR: parseStringToken }` y `(handlers[token] ?? reportError)()`. Explicar: buscar en la tabla la función asociada al token; si no existe, usar reportError; luego ejecutar. Ventajas: agregar un caso = agregar una entrada, no se modifica lógica de control. Principio Open/Closed aplicado a selección. Cada rama es testeable independientemente.
- **Conceptos clave:** tabla de despacho, Open/Closed, testeabilidad independiente.
- **Preguntas anticipadas:** "¿No es overengineering para 3 casos?" — Sí. Para 3 casos, if-else o switch. La tabla brilla con muchos casos o cambio frecuente.
- **Transición:** "Y hay señales que indican que tu selección necesita refactor."

### [F-33] Code smells de selección

- **Tiempo:** 3 min
- **Foco:** señales de fragilidad en estructuras de selección.
- **Guion:** Listar los cuatro smells: (1) condiciones duplicadas en múltiples ramas → violan DRY. (2) default que esconde errores → enmascarar casos no manejados reduce trazabilidad. (3) predicados opacos con side effects → mezclan responsabilidades. (4) cascadas largas sin dominio explícito → falta una abstracción de datos.
- **Conceptos clave:** DRY, default tragatodo, predicados opacos, cascadas.
- **Preguntas anticipadas:** "¿Un default vacío es smell?" — Sí, si esconde casos no manejados. Mejor lanzar error explícito.
- **Transición:** "Pasamos al bloque de iteración, donde la corrección formal entra en juego."

---

## BLOQUE D — Iteración, iteradores y generadores (F-34 a F-42)

### [F-34] Estructuras iterativas clásicas

- **Tiempo:** 5 min
- **Foco:** while, do-while y for: tres formas de iteración.
- **Guion:** While evalúa condición al inicio → puede no ejecutarse. Do-while evalúa al final → garantiza al menos una ejecución. For: contador, condición y actualización en una línea. En la mayoría de lenguajes modernos, for es azúcar sintáctico sobre while. Mostrar TypeScript y Kotlin. Resaltar que Kotlin no tiene do-while explícito en este ejemplo pero sí lo soporta.
- **Conceptos clave:** while, do-while, for, azúcar sintáctico.
- **Preguntas anticipadas:** "¿Cuándo uso do-while?" — Cuando necesitas al menos una ejecución: menús, lectura de input.
- **Transición:** "Pero un bucle no es correcto por accidente: necesita un invariante."

### [F-35] Invariantes de bucle

- **Tiempo:** 5 min
- **Foco:** el invariante garantiza la corrección del bucle.
- **Guion:** Razonamiento formal sobre iteración. Qué se mantiene verdadero: la propiedad del invariante. Cómo se establece: debe ser verdadero antes de entrar. Cómo se preserva: el cuerpo lo mantiene en cada iteración. Qué permite concluir al terminar: invariante + negación de la condición → resultado correcto. Los invariantes son la base de la verificación formal (Hoare Logic).
- **Conceptos clave:** invariante, establecimiento, preservación, Hoare Logic.
- **Preguntas anticipadas:** "¿Tengo que escribir el invariante en el código?" — No necesariamente, pero tenerlo mental te ayuda a razonar sobre la corrección.
- **Transición:** "Y la corrección incluye garantizar que el bucle termina."

### [F-36] Terminación del bucle

- **Tiempo:** 3 min
- **Foco:** progreso medible hacia la condición de parada.
- **Guion:** Definir función de ranking (loop variant): entero acotado inferiormente que decrece en cada iteración. El bucle termina si el variant es estrictamente decreciente y acotado. Verificar casos borde: n = 0, colecciones vacías, centinela inalcanzable. Bucles con centinela: la terminación depende de que el centinela sea alcanzable en la entrada.
- **Conceptos clave:** loop variant, función de ranking, casos borde, centinela.
- **Preguntas anticipadas:** "¿Y si no encuentro un variant?" — Es una señal de que el bucle podría no terminar. Hay que revisar la lógica.
- **Transición:** "A veces necesitamos escapar del bucle antes de la condición natural."

### [F-37] Break y continue

- **Tiempo:** 5 min
- **Foco:** escapar del flujo normal de iteración.
- **Guion:** Break y continue son transferencias estructuradas: afectan solo el bucle más cercano. Java permite break label para salir de bucles anidados — transferencia estructurada restringida, similar al goto limitado. Mostrar el código: continue salta al próximo elemento, break sale del bucle. Resaltar que son estructuradas, no gotos: no saltan a cualquier punto, solo al cierre del bucle.
- **Conceptos clave:** break, continue, break label, transferencia estructurada.
- **Preguntas anticipadas:** "¿Break es un goto disfrazado?" — No. Break solo sale del bucle más cercano. Goto salta a cualquier etiqueta. La restricción es lo que lo hace estructurado.
- **Transición:** "Dos patrones clásicos de control de iteración: contador y centinela."

### [F-38] Contador y centinela

- **Tiempo:** 3 min
- **Foco:** dos patrones clásicos de control de iteración.
- **Guion:** Contador: control por límites explícitos; adecuado cuando la cota es conocida. Centinela (while): control por valor especial en el stream; evita evaluar longitud en cada iteración. El centinela es útil en lectura incremental de streams o archivos: `while ((c = getchar()) != EOF)` en C. Riesgo: si el valor centinela nunca aparece, el bucle no termina.
- **Conceptos clave:** contador, centinela, EOF, terminación con centinela.
- **Preguntas anticipadas:** "¿Cuándo uso centinela vs. contador?" — Contador cuando conoces el tamaño. Centinela cuando lees un stream de longitud desconocida.
- **Transición:** "Los iteradores llevan esto al siguiente nivel de abstracción."

### [F-39] Iteradores: separar estructura de recorrido

- **Tiempo:** 3 min
- **Foco:** el iterador desacopla la colección del recorrido.
- **Guion:** La colección almacena los datos. El iterador encapsula el estado de recorrido y define el traversal. Habilita recorridos alternativos sobre la misma estructura sin duplicar su estado interno. El protocolo Iterable/Iterator (TypeScript, Java, Python) estandariza el contrato. Los iteradores son la forma moderna de iterar sobre estructuras sin exponer su representación interna.
- **Conceptos clave:** iterador, Iterable/Iterator, desacoplamiento, traversal.
- **Preguntas anticipadas:** "¿Y el for...of usa iteradores?" — Sí. for...of consume el protocolo Iterable/Iterator por debajo.
- **Transición:** "Y los generadores son iteradores perezosos."

### [F-40] Generadores: secuencias perezosas

- **Tiempo:** 5 min
- **Foco:** producir valores bajo demanda con yield.
- **Guion:** El generador suspende la ejecución en cada yield y la reanuda al siguiente next(). Permite trabajar con secuencias infinitas sin consumir memoria proporcional al tamaño. Cada next() reanuda la función exactamente donde se suspendió. Mostrar TypeScript: `function* rango(inicio, fin) { for (let i = inicio; i < fin; i++) yield i }`. Mostrar Python equivalente. Resaltar que el asterisco en `function*` marca la función como generadora.
- **Conceptos clave:** yield, suspensión, reanudación, secuencias infinitas, `function*`.
- **Preguntas anticipadas:** "¿Y si llamo next() más veces que elementos hay?" — Devuelve `{ done: true, value: undefined }`.
- **Transición:** "Una trampa frecuente en TypeScript: for...of vs for...in."

### [F-41] for...of vs for...in

- **Tiempo:** 3 min
- **Foco:** diferencia crítica en iteración sobre colecciones.
- **Guion:** Mostrar `const arr = [10, 20, 30]`. `for (const k in arr)` → "0", "1", "2" (claves). `for (const v of arr)` → 10, 20, 30 (valores correctos). for...of itera sobre valores del iterable. for...in itera sobre claves del objeto (strings). Regla: para arrays, siempre for...of. for...in es para enumerar propiedades de objetos.
- **Conceptos clave:** for...of, for...in, claves vs. valores, iterable.
- **Preguntas anticipadas:** "¿Por qué for...in devuelve strings en un array?" — Porque las claves de un array en JavaScript son strings bajo el hood.
- **Transición:** "Cerramos el bloque con recursión vs. iteración."

### [F-42] Recursión e iteración: misma potencia, costos distintos

- **Tiempo:** 5 min
- **Foco:** equivalencia expresiva, costos operacionales distintos.
- **Guion:** Recursión: estilo declarativo; el estado está implícito en la pila de llamadas. Iteración: control operativo explícito; el estado está en variables locales. Toda recursión primitiva puede transformarse en iteración con una pila explícita. Equivalencia expresiva con costos operacionales distintos (stack vs. heap). Tail call optimization (TCO): Haskell, Scheme, Scala optimizan recursión en cola como iteración — elimina costo de stack.
- **Conceptos clave:** recursión, iteración, pila de llamadas, TCO, tail recursion.
- **Preguntas anticipadas:** "¿TypeScript tiene TCO?" — No. JavaScript en modo estricto lo tenía en la spec pero ningún motor lo implementó. En TypeScript, la recursión profunda puede agotar el stack.
- **Transición:** "Una última estructura de control moderna: async/await."

---

## BLOQUE E — Integración y cierre (F-43 a F-44)

### [F-43] Control asíncrono con async/await

- **Tiempo:** 5 min
- **Foco:** secuencialidad aparente sobre operaciones asíncronas.
- **Guion:** await suspende la función actual sin bloquear el hilo de ejecución. Permite escribir flujo de control lineal sobre operaciones inherentemente concurrentes. El runtime convierte el código en una máquina de estados implícita. Mostrar `obtenerDatos()` que retorna `["A", "B", "C"]` y `pipeline()` con tres awaits encadenados. Resaltar: el código se lee como secuencial, pero el runtime lo transforma en una máquina de estados. Es la estructura de control más moderna que vimos.
- **Conceptos clave:** async/await, suspensión, máquina de estados implícita, concurrencia.
- **Preguntas anticipadas:** "¿await bloquea el hilo?" — No. Suspende la función sin bloquear el hilo. El hilo puede hacer otra cosa mientras espera.
- **Transición:** "Cerramos con las ideas fuerza."

### [F-44] Cierre: criterios de diseño semántico

- **Tiempo:** 4 min
- **Foco:** consolidación de las cinco ideas fuerza.
- **Guion:** Repasar las cinco ideas: (1) Parseo ≠ evaluación: la precedencia fija la forma; el orden de evaluación lo fija el lenguaje. (2) Short-circuit por corrección: evita estados inválidos, no solo optimiza. (3) Estructuras por mantenibilidad: if-else, switch o dispatch según el dominio. (4) Iteración correcta: un bucle sin invariante y sin función de ranking no es correcto por accidente. (5) Legibilidad semántica: nombrar bien predicados y estructurar el flujo previene defectos. Cerrar con las tres referencias: Sebesta (principal, caps. 7-8), Gabbrielli-Martini (auxiliar, semántica operacional), Louden (auxiliar, implementación y legibilidad).
- **Conceptos clave:** cinco ideas fuerza, referencias bibliográficas.
- **Preguntas anticipadas:** "¿Qué leemos para profundizar?" — Sebesta caps. 7 y 8 son la fuente principal. Gabbrielli-Martini para semántica formal. Louden para implementación.
- **Transición:** Fin de la clase.

---

## Resumen de tiempos

| Bloque | Filminas | Minutos |
|--------|----------|---------|
| A — Fundamentos de expresiones | F-00 a F-16 | 68 |
| B — Booleanos y short-circuit | F-17 a F-25 | 35 |
| C — Selección estructurada | F-26 a F-33 | 31 |
| D — Iteración, iteradores y generadores | F-34 a F-42 | 37 |
| E — Integración y cierre | F-43 a F-44 | 9 |
| **Total** | **45 filminas** | **180 min** |

---

## Criterios de evaluación sugeridos

1. **Razonamiento semántico**: explica por qué una expresión se evalúa como se evalúa.
2. **Criterio de estructura**: justifica if/switch/dispatch con argumentos de mantenibilidad.
3. **Solidez de iteración**: demuestra invariantes y terminación.
4. **Higiene de código**: evita coerciones ambiguas y side effects ocultos.

---

## Bibliografía de referencia para esta minuta

- **Sebesta**, *Concepts of Programming Languages*, caps. 7–8 (fuente principal: expresiones, evaluación, asignación y estructuras de control).
- **Gabbrielli, Martini**, *Programming Languages: Principles and Paradigms* (complemento: semántica operacional, coerciones, invariantes de bucle, recursión y short-circuit).
- **Louden**, *Programming Languages: Principles and Practice* (complemento: implementación del control de flujo, legibilidad y decisiones de diseño de lenguajes).