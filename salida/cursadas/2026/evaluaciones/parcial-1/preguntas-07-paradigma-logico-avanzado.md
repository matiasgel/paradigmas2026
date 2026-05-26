---
topic_id: "07-paradigma-logico-avanzado"
topic_name: "Paradigma Lógico: Prolog — Clase 2+3 (Unificación, Backtracking, Listas)"
exam_type: "parcial-1"
course_id: "2026"
question_count: 9
points_total: 31
bloom_mix: "recordar: 3pts, comprender: 9pts, aplicar: 8pts, analizar: 8pts, evaluar: 3pts"
generated_at: "2026-05-25"
---

# Preguntas — Tema 07: Paradigma Lógico — Prolog II+III

---

## P-07-001 | Recordar | Conceptual | 3 pts

**¿Qué es la unificación en Prolog?**

a) Un algoritmo de búsqueda que recorre el árbol de soluciones de izquierda a derecha  
b) El proceso de calcular el valor numérico de una expresión aritmética  
c) El proceso de encontrar una sustitución de variables que haga que dos términos sean sintácticamente idénticos  
d) La técnica de ordenar los hechos en la base de conocimiento para optimizar las consultas  

**Respuesta correcta:** c  
**Justificación:** La unificación es el mecanismo central de Prolog: dados dos términos, busca la sustitución más general (MGU — Most General Unifier) que los haga iguales sintácticamente. No evalúa, no computa numéricamente — solo hace "matching con variables". Ejemplo: `f(X, b)` unifica con `f(a, Y)` bajo la sustitución `{X=a, Y=b}`.  
**Fuente:** minuta.md §BLOQUE 1 — Unificación (F-006 a F-023)  
**Bloom:** Recordar  

---

## P-07-002 | Comprender | Conceptual | 3 pts

**En Prolog, si ejecutamos `?- X = 2 + 3.`, el motor responde `X = 2+3` sin evaluar la suma. ¿Por qué?**

a) Porque Prolog no tiene operadores aritméticos  
b) Porque `=` realiza unificación, no evaluación. `2+3` es una estructura `+(2,3)` que se unifica como término; para evaluar numéricamente se usa `is/2`  
c) Porque `X` es una variable entera y no puede contener una expresión  
d) Porque la unificación en Prolog es lazy y solo evalúa cuando se necesita el resultado  

**Respuesta correcta:** b  
**Justificación:** En Prolog `=` es el predicado de unificación. `2+3` no es "dos más tres" sino la estructura de término `+(2,3)` — un functor `+` con dos argumentos. La unificación simplemente liga `X` a esa estructura. Para evaluar aritméticamente se usa `is/2`: `?- X is 2+3.` da `X = 5`. Esta distinción entre estructura y evaluación es fundamental en Prolog.  
**Fuente:** minuta.md §BLOQUE 1 — `=` vs `==` vs `is` (F-015, F-016)  
**Bloom:** Comprender  

---

## P-07-003 | Comprender | Conceptual | 3 pts

**¿Qué es un "choice point" (punto de elección) en el backtracking de Prolog?**

a) El punto del programa donde el programador declara que hay una sola solución posible  
b) Una marca que el motor crea cuando encuentra múltiples cláusulas que pueden unificar con el goal actual, guardando las alternativas para explorar si la rama actual falla  
c) Un predicado especial que le permite al programador elegir entre varias bases de conocimiento  
d) El nodo raíz del árbol SLD a partir del cual se inicia la resolución  

**Respuesta correcta:** b  
**Justificación:** Cuando Prolog intenta resolver un goal y hay varias cláusulas que podrían unificar con él, crea un **choice point**: guarda el estado actual (bindings del trail) y la lista de cláusulas alternativas no probadas. Si la rama que tomó falla, el motor retrocede (backtrack) hasta el último choice point y prueba la siguiente alternativa. El corte `!` elimina los choice points creados en la cláusula actual.  
**Fuente:** minuta.md §BLOQUE 3 — Backtracking: choice points y trail (F-039 a F-043)  
**Bloom:** Comprender  

---

## P-07-004 | Comprender | Conceptual | 3 pts

**¿Cuál es la diferencia entre `=` y `==` en Prolog?**

a) `=` compara por valor; `==` compara por referencia de memoria  
b) `=` intenta unificar los dos términos (puede ligar variables); `==` verifica si los dos términos son ya idénticos sin ligar ninguna variable  
c) `=` solo funciona con átomos; `==` funciona con cualquier término  
d) Son sinónimos — en SWI-Prolog ambos realizan la misma operación  

**Respuesta correcta:** b  
**Justificación:** `=` es el predicado de **unificación**: `?- X = ana.` tiene éxito y liga `X = ana`. `==` es el predicado de **identidad estructural**: `?- X == ana.` falla si `X` no está ya ligada a `ana`. La diferencia clave: `=` puede ligar variables como efecto secundario; `==` nunca liga variables y solo tiene éxito si los dos términos son ya estructuralmente idénticos. Ejemplo: `?- X = Y, X == Y.` tiene éxito porque `=` liga X e Y, y luego `==` confirma que son idénticos.  
**Fuente:** minuta.md §BLOQUE 1 — `=` vs `==` vs `=..` (F-015, F-016)  
**Bloom:** Comprender  

---

## P-07-005 | Aplicar | Con código Prolog | 4 pts

**¿Cuál de las siguientes consultas de unificación tiene ÉXITO en Prolog?**

a) `?- f(X, b) = f(a, a).`  
b) `?- f(X, X) = f(ana, beatriz).`  
c) `?- f(X, b) = f(a, Y).`  
d) `?- f(X, g(X)) = f(a, g(b)).`  

**Respuesta correcta:** c  
**Justificación:** Analisis de cada opción:  
a) `f(X, b) = f(a, a)`: liga `X=a` pero el segundo argumento `b ≠ a` → **falla**.  
b) `f(X, X) = f(ana, beatriz)`: `X` debe unificar con `ana` y con `beatriz` simultáneamente → **falla** (conflicto).  
c) `f(X, b) = f(a, Y)`: liga `X=a` y `Y=b` → **éxito** con sustitución `{X=a, Y=b}`.  
d) `f(X, g(X)) = f(a, g(b))`: liga `X=a` pero luego `g(a) ≠ g(b)` → **falla**.  
**Fuente:** minuta.md §BLOQUE 1 — Ejemplos de unificación y falla (F-008, F-009)  
**Bloom:** Aplicar  

---

## P-07-006 | Aplicar | Con código Prolog | 4 pts

**Dada la siguiente base de conocimiento:**

```prolog
miembro(X, [X|_]).
miembro(X, [_|T]) :- miembro(X, T).
```

**¿Cuáles son TODAS las respuestas que da Prolog a `?- miembro(X, [a, b, c]).`?**

a) Solo `X = a` — Prolog devuelve la primera solución encontrada y se detiene  
b) `X = a ; X = b ; X = c` — Prolog devuelve las tres soluciones vía backtracking  
c) `X = [a, b, c]` — Prolog unifica X con la lista completa  
d) `false` — `miembro/2` requiere que el primer argumento ya esté instanciado  

**Respuesta correcta:** b  
**Justificación:** `miembro/2` tiene dos cláusulas. Primera: unifica `X` con la cabeza de la lista → `X = a` (éxito). Si se pide más (`;`), backtrack: segunda cláusula con `T = [b, c]` → aplica de nuevo → `X = b`. Backtrack: `T = [c]` → `X = c`. Backtrack: `T = []` → falla la segunda cláusula → fin. Resultado: tres soluciones `a`, `b`, `c` via backtracking. Este es `member/2` canónico de Prolog.  
**Fuente:** minuta.md §BLOQUE 2 — Listas: `member/2` (B2)  
**Bloom:** Aplicar  

---

## P-07-007 | Analizar | Con código Prolog | 4 pts

**Considerá el siguiente programa:**

```prolog
color(rojo). color(verde). color(azul).

?- color(X), write(X), nl, fail.
```

**¿Qué imprime esta consulta y por qué?**

a) Solo `rojo` — porque `fail` hace que la consulta falle después del primer resultado  
b) No imprime nada — `fail` hace que toda la consulta falle antes de ejecutar `write`  
c) Imprime `rojo`, luego `verde`, luego `azul`, luego falla — `fail` fuerza el backtracking que agota todos los valores de `color/1`  
d) Imprime `rojo verde azul` en una sola línea separado por espacios  

**Respuesta correcta:** c  
**Justificación:** Este es el patrón **fail-driven loop** de Prolog. La secuencia: (1) `color(X)` unifica `X=rojo`; (2) `write(rojo)` imprime `rojo`; (3) `nl` imprime nueva línea; (4) `fail` fuerza backtrack al choice point de `color(X)`; (5) `X=verde` → imprime `verde` → fail → backtrack; (6) `X=azul` → imprime `azul` → fail → no hay más cláusulas → consulta falla. Resultado: imprime las tres líneas y termina con `false`.  
**Fuente:** minuta.md §BLOQUE 3 — fail-driven loop y backtracking (F-041 a F-043)  
**Bloom:** Analizar  

---

## P-07-008 | Analizar | Con código Prolog | 4 pts

**Considerá los siguientes dos predicados:**

```prolog
% Versión A
maximo(X, Y, X) :- X >= Y.
maximo(X, Y, Y) :- X < Y.

% Versión B
maximo(X, Y, X) :- X >= Y, !.
maximo(_, Y, Y).
```

**¿Cuál es la diferencia de comportamiento entre la Versión A y la Versión B?**

a) Ambas son equivalentes en todos los casos — el corte `!` es solo una optimización de rendimiento sin impacto semántico  
b) La Versión B usa corte **verde**: elimina elección cuando ya se sabe cuál es el máximo, sin cambiar las soluciones; la Versión A recalcula ambas condiciones; ambas dan el mismo resultado para enteros instanciados  
c) La Versión B usa corte **rojo**: si se llama con variables no instanciadas, el corte hace que se devuelva una sola solución posiblemente incorrecta; la Versión A se comporta correctamente en más contextos  
d) La Versión A falla si X e Y son iguales; la Versión B siempre devuelve X en ese caso  

**Respuesta correcta:** b  
**Justificación:** El corte en Versión B es de tipo **verde** para inputs numéricos instanciados: si `X >= Y`, corta para evitar probar la segunda cláusula (que fallaría de todas formas, ya que `X < Y` sería falso). No elimina soluciones correctas. La Versión A es más declarativa pero hace dos tests. Para los propósitos del parcial, con argumentos instanciados ambas versiones producen el mismo resultado. Si se usaran con variables, Versión B produce resultados incorrectos (corte rojo), pero eso no se pide aquí.  
**Fuente:** minuta.md §BLOQUE 5 — Corte verde vs. rojo, `max/3` (B5)  
**Bloom:** Analizar  

---

## P-07-009 | Evaluar | Conceptual | 3 pts

**El corte `!` en Prolog fue descrito en clase como una "navaja de doble filo". ¿Cuál de las siguientes afirmaciones captura mejor esta idea?**

a) El corte es siempre perjudicial y no debería usarse en programas bien diseñados  
b) El corte verde mejora la eficiencia sin cambiar las soluciones; el corte rojo cambia el significado declarativo del programa, haciendo que Prolog encuentre menos soluciones de las que debería encontrar lógicamente  
c) El corte siempre mejora la eficiencia porque poda el árbol de búsqueda, pero nunca afecta la corrección del programa  
d) El corte rojo y el verde son sinónimos — la diferencia es solo de estilo  

**Respuesta correcta:** b  
**Justificación:** El **corte verde** (`!` que solo elimina alternativas que de todas formas fallarían) no cambia el significado declarativo: el programa con y sin `!` tiene las mismas soluciones, solo difiere en eficiencia. El **corte rojo** (`!` que elimina alternativas que podrían tener éxito) rompe la declaratividad: el programa ya no es una descripción pura de lo que es verdadero, sino que su comportamiento depende del orden de las cláusulas y de cuándo se coloca el corte. Es un compromiso entre eficiencia y claridad conceptual — de ahí la "navaja de doble filo".  
**Fuente:** minuta.md §BLOQUE 5 — Corte: dilema ético de declaratividad (B5)  
**Bloom:** Evaluar  
