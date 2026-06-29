# Diseno de Clase - Tema 11

## Expresiones y Estructuras de Control

> Estado: CORREGIDO (alineado con clase_dada.txt — 2026-06-28)
> Creado: 2026-06-01
> Corregido: 2026-06-28 por Dr. Roberto (class-writer)
> Agente: Marcos v3 (Topic Designer) → Roberto (class-writer, corrección)
> Modalidad: teórica con constraint absoluto de 180 minutos
> Referencia principal: Sebesta, Concepts of Programming Languages, caps. 7–8
> Referencias auxiliares: Gabbrielli-Martini caps. 4–6, Louden cap. 8
> Baseline de corrección: clase_dada.txt (859 líneas)

---

## Resolucion de alcance

Se redefine este tema con constraint absoluto de 180 minutos, generando una narrativa teorica completa en 45 filminas (F-00 a F-44), priorizando fidelidad al `clase_dada.txt` y trazabilidad bibliografica.

### Criterios de diseno aplicados (corregidos 2026-06-28)

1. **Fidelidad al clase_dada.txt**: los codigos textuales del .txt se preservan en filminas; no se inventan ejemplos.
2. Sebesta-first: el hilo argumental principal sigue definiciones y taxonomia del capitulo de expresiones y control.
3. Auxiliares por contraste: Gabbrielli-Martini y Louden se usan para tensionar decisiones de diseno, edge cases y variaciones de sintaxis/semantica.
4. Teoria antes de receta: cada patron practico queda anclado en una decision semantica.
5. Cobertura integral de modulo VIII, incluyendo conexiones explicitas con tipos (modulo VII) y concurrencia (modulo XI) cuando impacta el flujo de control.
6. **Imagenes con prompts visuales puros**: se generan imagenes para filminas clave (portada, mapa conceptual, AST, goto, invariantes, cierre) con prompts visuales originales centrados en conceptos del tema.

---

## Objetivos de aprendizaje (version extendida)

Al finalizar la secuencia completa del tema, el estudiante podra:

1. Definir formalmente expresion, sentencia y contexto de evaluacion.
2. Aplicar precedencia, asociatividad y orden de evaluacion de operandos con y sin efectos colaterales.
3. Diferenciar semantica de short-circuit versus evaluacion estricta y justificar su uso por correccion, no solo por eficiencia.
4. Analizar asignacion como sentencia y como expresion, incluyendo patrones de bug historicos.
5. Evaluar impacto de coerciones y conversiones en legibilidad, seguridad y verificabilidad.
6. Comparar seleccion simple, multiple y anidada segun criterios de mantenibilidad y acoplamiento.
7. Razonar sobre iteracion con invariantes, terminacion y mecanismos de escape.
8. Explicar iteradores y generadores como abstracciones de control de flujo.
9. Diseccionar anti-patrones de control (goto indiscriminado, cascadas no normalizadas, efectos ocultos).
10. Integrar teoria y practica en lectura critica de codigo real.

---

## Cobertura del plan minimo (Modulo VIII)

| Topico institucional | Cobertura en tema 11 |
| -------------------- | -------------------- |
| Expresiones aritmeticas, relacionales y booleanas | Completa y profundizada |
| Reglas de precedencia, asociatividad, parentesis | Completa y formalizada |
| Sentencias de asignacion; asignacion como expresion; modo mixto | Completa con casos de bug |
| Evaluacion corto-circuito vs evaluacion estricta | Completa con semantica operacional |
| Sobrecarga de operadores; conversiones y coerciones | Completa con trade-offs |
| Estructuras de control: seleccion y seleccion multiple | Completa con criterios de diseno |
| Enunciados iterativos y control de bucle | Completa con invariantes y terminacion |
| Iteradores y generadores | Completa con modelo de ejecucion |
| Ejemplos en lenguaje principal y contrastes | Completa |

---

## Arquitectura de filminas (45) — corregida 2026-06-28

### Bloque A - Fundamentos de expresiones y semantica (F-00 a F-16) — 68 min

- Portada, apertura socratica, objetivos, mapa conceptual.
- Expresion vs sentencia, por que importa, AST y parseo.
- Precedencia, asociatividad, parentesis como decision semantica.
- Orden de evaluacion, efectos colaterales (i++ + ++i), asignacion como expresion.
- Prevencion de bugs, conversion y coercion, control conceptual.

### Bloque B - Booleanos, short-circuit y seguridad semantica (F-17 a F-25) — 35 min

- Algebra booleana aplicada, truthiness por lenguaje.
- Evaluacion estricta vs short-circuit por correccion semantica.
- Patron defensivo, anti-patron con side effects.
- Operadores comparativos, null safety (?. ??), guard clauses.

### Bloque C - Seleccion estructurada y decisiones de diseno (F-26 a F-33) — 31 min

- Goto y programacion estructurada (incluye goto restringido en Go).
- If/else if, switch (con Kotlin when), pattern matching.
- Complejidad cognitiva, criterios de eleccion, despacho por tabla, code smells.

### Bloque D - Iteracion, iteradores y generadores (F-34 a F-42) — 37 min

- While/do-while/for, invariantes de bucle, terminacion.
- Break/continue, contador vs centinela, iteradores.
- Generadores con yield, for...of vs for...in, recursion vs iteracion.

### Bloque E - Integracion y cierre (F-43 a F-44) — 9 min

- async/await como control de flujo moderno.
- Cierre con cinco ideas fuerza y referencias bibliograficas.

---

## Evidencia de grounding bibliografico (MCP ChromaDB) — verificado 2026-06-28

Hallazgos aplicados al diseno y verificados contra ChromaDB:

1. **Sebesta caps. 7-8**: precedencia/asociatividad y orden de evaluacion de operandos como fuente de diferencias semanticas en presencia de side effects (query: "operator precedence associativity expression evaluation" — relevancia 0.798).
2. **Sebesta + Gabbrielli-Martini**: short-circuit como mecanismo de correccion (evitar division por cero, null access), no solo optimizacion (query: "short-circuit evaluation boolean operator" — relevancia 0.786 Gabbrielli, 0.754 Sebesta).
3. **Sebesta**: asignacion como expresion y error historico de usar `=` en condiciones; mixed-mode assignment (query: "assignment expression side effect coercion mixed mode" — relevancia 0.578).
4. **Sebesta + Louden**: taxonomia de control statements (seleccion, iteracion, transferencia incondicional) y debate estructurado sobre goto (query: "GOTO structured programming Dijkstra" — relevancia 0.61 Sebesta; "selection if else if switch" — relevancia 0.61).
5. **Sebesta**: guarded commands de Dijkstra como antecedente del short-circuit defensivo (query: "guarded command Dijkstra nondeterministic" — relevancia 0.746).
6. **Gabbrielli-Martini**: invariantes de bucle y loop variant para terminacion (query: "iteration while for do loop invariant" — relevancia 0.575 Gabbrielli, 0.574 Sebesta).
7. **Gabbrielli-Martini**: tail call optimization y transformacion de recursion a iteracion (query: "recursion tail call optimization iteration" — relevancia 0.693).
8. **Gabbrielli-Martini + Sebesta**: generadores con yield y suspension de ejecucion (query: "iterator generator yield coroutine" — relevancia 0.519 Gabbrielli).

---

## Decision de aprobacion

Diseno corregido por Dr. Roberto (class-writer) el 2026-06-28, alineado con `clase_dada.txt` (859 lineas) y constraint absoluto de 180 minutos.

### Drift detectado y corregido

1. **Modalidad**: "sin restriccion por tiempo" → constraint absoluto de 180 min.
2. **Imagenes**: "no se generan imagenes" → imagenes con prompts visuales puros en filminas clave.
3. **F-09 (Efectos colaterales)**: codigo previo usaba `a[i] + i++` con array (no estaba en clase_dada.txt) → corregido a `i++ + ++i` (textual del .txt).
4. **F-12 (Efectos colaterales codigo)**: anadido contraste Rust `i += 1` (no existe `i++`) del .txt.
5. **F-13 (Asignacion)**: anadido ejemplo Kotlin `x = 5` del .txt (no se usa asignacion como expresion de valor).
6. **F-21 (Patron defensivo)**: anadido ejemplo C `if (p != NULL && p->value > 0)` del .txt.
7. **F-23 (Operadores comparativa)**: tabla previa tenia columna "Short-circuit" → corregida a tabla del .txt con NOT logico y AND/OR bit.
8. **F-24 (Null safety)**: anadidos Kotlin `?:` y Rust `and_then/map` del .txt (previo solo TypeScript).
9. **F-26 (Goto)**: anadido ejemplo Go con `goto inicio` del .txt (previo no lo incluia).
10. **F-28 (Switch)**: anadido codigo Kotlin `when` del .txt (previo solo lo mencionaba).
11. **F-34 (Iterativas)**: anadidos ejemplos Python y Kotlin del .txt (previo solo TypeScript).
12. **F-40 (Generadores)**: eliminado `fibonacci()` inventado (no estaba en .txt) → solo `rango` en TS y Python.
13. **F-43 (async/await)**: anadido `obtenerDatos()` que retorna `["A","B","C"]` del .txt (previo solo `pipeline()`).
14. **F-43/F-44 (Cierre)**: eliminado "caso integrador" inventado (no estaba en .txt) → F-43 = async/await, F-44 = cierre con ideas fuerza + referencias.

Estado resultante del tema:

- Diseno: corregido y alineado con clase_dada.txt
- Minuta: corregida, 45 filminas, suma = 180 min exactos
- Filminas: corregidas, 45 filminas, codigos textuales del .txt
