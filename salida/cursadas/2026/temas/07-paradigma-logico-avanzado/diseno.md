# Diseño de Tema 07 — Paradigma Lógico: Prolog — Clase 2+3 (Unificación, Backtracking, Listas, Recursión y Aplicaciones)

**Materia:** Paradigmas y Lenguajes de Programación 2026
**Institución:** UNTDF — Instituto IDEI
**Docente:** Matías Gel
**Duración de clase:** 240 minutos (clase doble — fusiona clases 2 y 3 del módulo III)
**Estado:** APROBADO — Actualizado post-dictado 2026-04-27
**Fecha de diseño:** 2026-04-21 | **Actualización post-dictado:** 2026-04-27
**Clase en el ciclo:** 2 de 2 (cierre del módulo Prolog)
**Prerrequisito:** Tema 06 aprobado (hechos, reglas, consultas, trazado básico, recursión simple)

---

## 1. Objetivo General de la Clase

Completar el dominio del **Paradigma Lógico** cubriendo los mecanismos internos del motor Prolog (unificación y backtracking) y las estructuras de datos fundamentales (listas). Al finalizar la clase el alumno debe ser capaz de:

1. Explicar el algoritmo de unificación y su rol en la resolución.
2. Trazar árboles de búsqueda SLD con backtracking y corte.
3. Procesar listas con las primitivas canónicas (`append/3`, `member/2`, `length/2`) directamente desde Prolog.
4. Distinguir corte verde de corte rojo y aplicar el corte con responsabilidad.
5. Situar Prolog en el panorama 2026 (bases deductivas, razonamiento neuro-simbólico).

> **⚠️ Nota post-dictado (2026-04-27):** Los siguientes objetivos del diseño original **no fueron cubiertos** en la clase: aritmética `is/2`, recursión con acumulador/LCO, meta-predicados (`findall`/`bagof`/`setof`), aplicaciones de restricciones (N-reinas, mapa de colores). Quedan disponibles para auto-estudio en la guía del alumno.

---

## 2. Objetivos Específicos (Bloom)

| Nivel | Objetivo |
|-------|----------|
| **Recordar** | Definir unificación, sustitución, MGU, resolvente, corte, negación por falla, acumulador |
| **Comprender** | Explicar por qué `?- X = Y, Y = 2.` tiene éxito y `?- X is Y + 1, Y = 2.` falla |
| **Aplicar** | Escribir `append/3`, `member/2`, `length/3` con acumulador y predicados aritméticos recursivos |
| **Analizar** | Dibujar el árbol SLD de una consulta con 3+ ramas y marcar los nodos podados por `!` |
| **Evaluar** | Comparar Prolog declarativo puro vs. Prolog con cortes rojos/verdes — juzgar la pérdida de declaratividad |
| **Crear** | Modelar un dominio (viajes, parentescos, grafos) como base deductiva Prolog + consultas compuestas |

---

## 3. Conocimientos Previos Requeridos

- **Tema 06 (Prolog Clase 1):** hechos, reglas, consultas, cláusulas de Horn, términos, trazado elemental, recursión `ancestro/2`.
- **Funcional (Temas 03–05):** recursión con patrón base/recursivo, listas como `[H|T]` (intuición).
- **Imperativo (Tema 01):** noción de stack de llamadas (para comparar con stack de resolución Prolog).
- Lógica: `∀`, `∃`, implicación, resolución (informal, de Tema 06).

---

## 4. Estructura de la Clase — Dictado Real (240 min)

> **⚠️ Reorganizado post-dictado (2026-04-27):** El orden real de la clase difirió del diseño original. Las Listas fueron dictadas ANTES de SLD/Backtracking. Los bloques no cubiertos se marcan con ⚠️.

| Bloque | Duración | Contenido | Tipo | Estado |
|--------|----------|-----------|------|--------|
| **B0** | 10 min | Repaso activo de Clase 1 (quiz relámpago en pizarra) | Repaso guiado | ✅ dictado |
| **B1** | 40 min | Unificación: algoritmo, MGU, occurs-check, `=`/`==`/`=..`, variable anónima, pattern matching, ejercicio relámpago | Exposición + trazado | ✅ dictado |
| **B2** | 35 min | **Listas**: `[H\|T]`, `member/2`, `append/3`, `last/2`, `nth0/3`, `msort/sort`, pares, anidadas, `forall/2`, `between/3`, construir listas | Demo derivada + live | ✅ dictado |
| **B3** | 30 min | Resolución SLD: resolvente, selección, regla de escritura, árbol SLD, DFS | Pizarrón + demo | ✅ dictado |
| **B4** | 30 min | Backtracking: choice points, trail, fail-driven loop, árbol de búsqueda, bucle infinito | Live SWISH | ✅ dictado |
| **B5** | 30 min | Corte (`!`): verde vs. rojo, `max/3`, `if-then-else`, implementación de `not/1` | Código + dilema ético | ✅ dictado |
| **B6** | 25 min | Panorama 2026: Datalog, neuro-simbólico, implementaciones modernas (SWI, Scryer, Tau, XSB) | Exposición breve | ✅ dictado |
| ~~B7~~ | — | ~~Aritmética: `is/2`, operadores~~ | — | ⚠️ no dictado |
| ~~B8~~ | — | ~~Recursión avanzada: acumuladores, LCO, `reverse/2`~~ | — | ⚠️ no dictado |
| ~~B9~~ | — | ~~Meta-predicados: `findall/3`, `bagof/3`, `setof/3`~~ | — | ⚠️ no dictado |
| ~~B10~~ | — | ~~Aplicaciones: mapa de colores, N-reinas, CLP(FD)~~ | — | ⚠️ no dictado |

**Total dictado:** ~200 min

---

## 5. Contenidos Detallados

### 5.1 Bloque 0 — Repaso de Clase 1 (10 min)

Quiz relámpago (4 preguntas, 30 s cada una, votación a mano alzada):

1. ¿Un hecho Prolog termina en punto? (sí)
2. ¿Las variables van en mayúscula? (sí)
3. ¿`padre(juan, X)` significa “quien sea el padre de Juan”? (no — “el hijo de Juan se llama X”; argumentos son posicionales)
4. ¿El motor busca de arriba a abajo? (sí)

Cerrar con recordatorio del ejemplo `ancestro/2`. Conectar: “hoy vamos a abrir la caja negra: ¿CÓMO Prolog encuentra las respuestas?”

---

### 5.2 Bloque 1 — Unificación (25 min)

#### 5.2.1 Definición intuitiva
Unificar dos términos = encontrar sustitución de variables que los haga sintácticamente idénticos.

Ejemplos verbales:
- `ana` con `ana` → éxito, sustitución `{}`
- `X` con `ana` → éxito, `{X/ana}`
- `padre(juan, X)` con `padre(Y, pedro)` → éxito, `{Y/juan, X/pedro}`
- `padre(juan, X)` con `madre(Y, pedro)` → falla (símbolos funtores distintos)
- `f(X, X)` con `f(ana, beatriz)` → falla (X no puede ser dos átomos distintos)

#### 5.2.2 Algoritmo de unificación (Robinson 1965, informal)
```
unify(t1, t2):
    si t1 == t2 (variable o átomo iguales) → éxito
    si t1 es variable no ligada → ligar t1 := t2
    si t2 es variable no ligada → ligar t2 := t1
    si t1 = f(a1..an) y t2 = f(b1..bn) con mismo funtor/aridad →
        unificar recursivamente a_i con b_i
    en otro caso → falla
```

#### 5.2.3 Sustitución más general (MGU)
La unificación produce la **sustitución más general** que iguala los términos — no cualquier sustitución. Ejemplo:
- `f(X)` con `f(Y)` → MGU `{X/Y}` (o `{Y/X}`). NO `{X/ana, Y/ana}`.

#### 5.2.4 Occurs-check
Problema patológico: `?- X = f(X).`
- Sin occurs-check (default SWI-Prolog) → crea término cíclico infinito (bug silencioso)
- Con occurs-check (`?- unify_with_occurs_check(X, f(X)).`) → falla correctamente

> *"Full unification requires the occurs check, but most Prolog systems omit it for efficiency."*
> — Sebesta, Cap. 16

#### 5.2.5 `=` vs. `==` vs. `=..`
| Operador | Significado |
|----------|-------------|
| `X = Y` | Unificación (intenta ligar) |
| `X == Y` | Identidad estructural estricta (no liga) |
| `X \= Y` | Falla unificación |
| `X =.. L` | Univ: descompone término en lista `[funtor, arg1, arg2, ...]` |

Ejemplo demo:
```prolog
?- padre(juan, X) =.. L.
L = [padre, juan, X].
```

---

### 5.3 Bloque 2 — Resolución SLD (25 min)

#### 5.3.1 Resolución SLD = *Selective Linear Definite*
Algoritmo por el cual Prolog prueba una consulta:

1. La consulta es la **resolvente inicial**.
2. Elegir el **goal más a la izquierda** (regla de selección Prolog).
3. Buscar una cláusula cuya cabeza unifique (de arriba a abajo).
4. Reemplazar el goal por el cuerpo de la cláusula, aplicando la sustitución.
5. Si la resolvente queda vacía → éxito con las sustituciones acumuladas.
6. Si no unifica ninguna cláusula → backtrack.

#### 5.3.2 Árbol SLD
Ejemplo base:
```prolog
madre(ana, carlos).
madre(ana, beatriz).
padre(carlos, laura).
progenitor(X,Y) :- madre(X,Y).
progenitor(X,Y) :- padre(X,Y).
abuelo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).
```

Consulta: `?- abuelo(ana, N).`

Dibujar el árbol en pizarrón: raíz `abuelo(ana,N)`, rama única por `abuelo/2`, dos subramas por `progenitor` → unificación con hechos → soluciones `N=laura` y backtracking para encontrar `N=pedro`.

#### 5.3.3 Regla de escritura = “izquierda-primero, tope-primero”
Prolog NO explora soluciones en ancho; es **búsqueda en profundidad** con backtracking cronológico. Consecuencia: el orden de las cláusulas y el orden de los goals en el cuerpo importa.

Ejemplo del riesgo — versión mala de `ancestro`:
```prolog
% MAL: recursión primero
ancestro(X,Y) :- ancestro(X,Z), progenitor(Z,Y).
ancestro(X,Y) :- progenitor(X,Y).
% Entra en bucle infinito porque expande ancestro antes de tocar la base.
```

---

### 5.4 Bloque 3 — Backtracking (25 min)

#### 5.4.1 Puntos de elección
Un **punto de elección** se crea cada vez que hay más de una cláusula que puede unificar con un goal. Prolog recuerda el punto para volver si la rama elegida falla.

#### 5.4.2 Demo en SWISH
```prolog
color(rojo).
color(verde).
color(azul).
?- color(X), write(X), nl, fail.
```
- Imprime los tres colores → `fail` fuerza backtracking.
- Construcción `fail-driven loop` — el patrón más antiguo de Prolog para iterar.

#### 5.4.3 Ejemplo con árbol de búsqueda
Problema: ¿qué combinaciones de 2 colores distintos son posibles?

```prolog
par(X, Y) :- color(X), color(Y), X \= Y.
?- par(A, B).
```

Trazar en pizarrón el árbol:
- 3 elecciones para X × 3 elecciones para Y × filtro `X\=Y` = 6 soluciones.

#### 5.4.4 Backtracking destructivo
Cuando una variable se liga dentro de una rama y la rama falla, la ligadura se **deshace** automáticamente. Esto se llama *trail*: el motor mantiene un log de ligaduras para revertirlas.

Comparar con estado mutable imperativo: “imaginá un `try/catch` que revierte todas las asignaciones”.

---

### 5.5 Bloque 4 — Corte (`!`) (20 min)

#### 5.5.1 ¿Qué hace el corte?
`!` “confirma” la rama actual y **elimina puntos de elección** a la izquierda del corte y en la cabeza actual. Es un compromiso irrevocable.

#### 5.5.2 Ejemplo canónico — `max/3`
```prolog
% Sin corte (correcto pero ineficiente / ambiguo)
max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.

% Con corte verde (declarativo preservado, más eficiente)
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
```

Ambos son correctos; el segundo evita evaluar la segunda cláusula después de probar la primera.

#### 5.5.3 Corte rojo vs. verde
| Tipo | Definición | Ejemplo |
|------|-----------|---------|
| **Verde** | No cambia la semántica; solo mejora eficiencia | `max` arriba |
| **Rojo** | Cambia la semántica — quitarlo rompe el programa | `if-then-else` codificado con `!` |

#### 5.5.4 `if-then-else` con corte
```prolog
abs(X, X)  :- X >= 0, !.
abs(X, Y)  :- Y is -X.
```
Si quitás `!`, `?- abs(3, Z).` produce `Z=3 ; Z=-3` (erróneo).

#### 5.5.5 Costo pedagógico
El corte destruye la simetría declarativa. Usar con moderación. Preferir `if-then-else` explícito `(Cond -> Then ; Else)`.

---

### 5.6 Bloque 5 — Negación por falla (15 min)

#### 5.6.1 `\+` Goal
“Goal no es demostrable con la base actual” ≠ “Goal es falso en el mundo”. Esta es la **asunción del mundo cerrado** (CWA — *Closed World Assumption*).

#### 5.6.2 Trampa clásica
```prolog
soltero(X) :- \+ casado(X).
```
Si `casado/1` no está definido o no figura `casado(juan).` → `soltero(juan)` es verdadero. Pero podemos NO saber que Juan está casado.

#### 5.6.3 Variables no ligadas y `\+`
```prolog
?- \+ (X = 1).   % falla: X=1 sí es demostrable
?- \+ (X = 1), X = 2.   % orden importa
```
**Regla:** usar `\+` solo sobre goals completamente ligados (*ground*).

---

### 5.7 Bloque 6 — Ejercicio colaborativo (20 min)

Trabajo en pares — 3 consultas, 5 min cada una + puesta en común 5 min.

**Ejercicio 1:** Dada la base
```prolog
viaja(ana, parana).
viaja(ana, rosario).
viaja(beto, rosario).
comparten_destino(X, Y) :- viaja(X, D), viaja(Y, D), X \= Y.
```
Trazar `?- comparten_destino(ana, Q).`

**Ejercicio 2:** Explicar por qué `?- \+ X = 1, X = 2.` falla pero `?- X = 2, \+ X = 1.` tiene éxito.

**Ejercicio 3:** Reescribir con `!` y con `(→ ;)`:
```prolog
signo(X, positivo) :- X > 0.
signo(0, cero).
signo(X, negativo) :- X < 0.
```

---

### 5.8 Bloque 7 — Aritmética en Prolog (20 min)

#### 5.8.1 El momento incómodo
```prolog
?- X = 2 + 3.
X = 2+3.
```
Prolog NO evalúa expresiones por defecto — las trata como términos.

#### 5.8.2 `is/2`: evaluación forzada
```prolog
?- X is 2 + 3.
X = 5.
```
- `is/2` requiere que la expresión sea **ground** (sin variables libres en el lado derecho).
- No funciona al revés: `?- 5 is X + 3.` → error.

#### 5.8.3 Operadores
| Categoría | Operadores |
|-----------|-----------|
| Aritméticos | `+`, `-`, `*`, `/`, `//` (división entera), `mod`, `**` |
| Comparadores aritméticos (evalúan) | `=:=`, `=\=`, `<`, `=<`, `>`, `>=` |
| Unificación | `=`, `\=`, `==`, `\==` |

**Trampa del menor-igual:** `=<` (no `<=`). El `=` va primero.

#### 5.8.4 Ejemplo: factorial
```prolog
factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.
```

#### 5.8.5 Contra-ejemplo anti-patrón
```prolog
% MAL
factorial(N, N * factorial(N-1)).  % nunca evalúa
```

---

### 5.9 Bloque 8 — Listas (25 min)

#### 5.9.1 Notación canónica
| Sintaxis | Significado |
|----------|-------------|
| `[]` | Lista vacía |
| `[a, b, c]` | Azúcar sintáctico de `.(a, .(b, .(c, [])))` |
| `[H | T]` | Patrón: cabeza `H`, cola `T` |
| `[A, B | T]` | Primeros dos + resto |

#### 5.9.2 Reconocer listas
```prolog
esLista([]).
esLista([_|T]) :- esLista(T).
```

#### 5.9.3 `member/2`
```prolog
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).
```
Comportamiento *multi-modo*:
- `?- member(2, [1,2,3]).` → true
- `?- member(X, [1,2,3]).` → X=1 ; X=2 ; X=3

#### 5.9.4 `append/3` — la joya de Prolog
```prolog
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).
```
Usos:
1. Concatenar: `?- append([1,2],[3,4],R).` → `R=[1,2,3,4]`
2. Dividir: `?- append(A, B, [1,2,3]).` → 4 soluciones
3. Pertenecer: `?- append(_, [X|_], [1,2,3]).` → enumera elementos

#### 5.9.5 `length/2`
```prolog
length([], 0).
length([_|T], N) :- length(T, N1), N is N1 + 1.
```

---

### 5.10 Bloque 9 — Recursión avanzada (25 min)

#### 5.10.1 Patrón con acumulador — `reverse/2`
Versión ingenua (O(n²)):
```prolog
reverse([], []).
reverse([H|T], R) :- reverse(T, RT), append(RT, [H], R).
```

Versión con acumulador (O(n)):
```prolog
reverse(L, R) :- rev(L, [], R).
rev([], Acc, Acc).
rev([H|T], Acc, R) :- rev(T, [H|Acc], R).
```

#### 5.10.2 Last-Call Optimization (LCO)
Cuando la última llamada de una cláusula es recursiva Y no hay puntos de elección pendientes, el motor puede reutilizar el stack frame → recursión iterativa en memoria constante.

#### 5.10.3 Ejercicio en vivo — `suma_lista/2`
```prolog
suma([], 0).
suma([H|T], S) :- suma(T, ST), S is H + ST.

% Con acumulador:
suma(L, S) :- suma(L, 0, S).
suma([], Acc, Acc).
suma([H|T], Acc, S) :- Acc1 is Acc + H, suma(T, Acc1, S).
```

#### 5.10.4 Comparación final con paradigmas
| Lenguaje | `reverse` |
|----------|-----------|
| TypeScript | `xs.reduce((acc, x) => [x, ...acc], [])` |
| Haskell | `foldl (flip (:)) []` |
| Prolog | `rev([H\|T],A,R) :- rev(T,[H\|A],R).` |

Mensaje: la recursión con acumulador es **universal**. Cambia el envoltorio, no el pensamiento.

---

### 5.11 Bloque 10 — Meta-predicados (20 min)

#### 5.11.1 Colectar todas las soluciones

| Predicado | Qué hace | Orden/duplicados |
|-----------|----------|------------------|
| `findall(T, Goal, L)` | Todas las soluciones de `T` | Con duplicados, lista vacía si no hay |
| `bagof(T, Goal, L)` | Igual pero falla si no hay soluciones | Agrupa por variables libres |
| `setof(T, Goal, L)` | Ordenado y sin duplicados | Falla si no hay soluciones |

#### 5.11.2 Ejemplo
```prolog
edad(ana, 22).
edad(beto, 30).
edad(carla, 22).
?- findall(N, edad(N, 22), L).
L = [ana, carla].
?- setof(E, N^edad(N, E), L).  % ^ = "cuantifica existencialmente"
L = [22, 30].
```

#### 5.11.3 Uso real: convertir Prolog en “SQL en 1 línea”
```prolog
?- findall(N-E, edad(N, E), Pares).
Pares = [ana-22, beto-30, carla-22].
```

---

### 5.12 Bloque 11 — Aplicaciones (20 min)

#### 5.12.1 Mapa de colores (grafo)
```prolog
% Regiones vecinas no pueden compartir color
color(rojo). color(verde). color(azul). color(amarillo).
distinto(A,B) :- A \= B.

mapa(Nor, Sur, Est, Oes) :-
    color(Nor), color(Sur), color(Est), color(Oes),
    distinto(Nor, Sur), distinto(Nor, Est),
    distinto(Sur, Oes), distinto(Est, Oes).
```

#### 5.12.2 N-reinas (resumen — cuerpo completo en TP)
Ecuación clásica de Prolog. Explicar el patrón *generate and test* sin entrar al código completo.

#### 5.12.3 Base deductiva de trayectos
```prolog
vuelo(ush, bue, 2200).
vuelo(bue, mvd, 150).
vuelo(mvd, spo, 1500).

ruta(A, B, [A,B], T)  :- vuelo(A, B, T).
ruta(A, B, [A|R], T)  :-
    vuelo(A, C, T1), ruta(C, B, R, T2),
    T is T1 + T2.
```
Consulta:
```prolog
?- ruta(ush, spo, Camino, T).
```
**Punto:** misma base sirve para “¿hay vuelo directo?”, “¿cuál es el más corto?” (con `findall` + ordenar), “¿cuántas escalas?”.

#### 5.12.4 Parsing con DCG — mención
1 minuto para mostrar cómo Prolog hace parsers:
```prolog
oracion --> sujeto, verbo, objeto.
sujeto --> [el], [gato].
verbo  --> [come].
objeto --> [pescado].
?- phrase(oracion, [el, gato, come, pescado]).
true.
```
No se profundiza en clase, se deja de lectura.

---

### 5.13 Bloque 12 — Prolog en 2026 (10 min)

#### 5.13.1 Bases de datos deductivas (Datalog)
Variante restringida de Prolog usada en:
- **Logica** (Google, facturación interna)
- **Soufflé** (análisis estático de código)
- **RecStep**, **Differential Datalog** (procesamiento incremental)

#### 5.13.2 Sistemas neuro-simbólicos
- **LLM + Prolog:** el LLM propone reglas, Prolog las verifica. Combina intuición con rigor.
- **DeepProbLog**, **SymbolicAI** (2024–2026): modelos híbridos que integran redes neuronales con motores lógicos.
- **Razonamiento matemático** (AlphaProof, 2024): parcialmente basado en búsqueda lógica.

#### 5.13.3 Industria hoy
- **SWI-Prolog** — estable, usado en sistemas de salud (Erlang lo inspira).
- **Scryer Prolog**, **Trealla Prolog** — implementaciones modernas en Rust/C con WASM.
- **Clojure + core.logic** — Prolog dentro de un lenguaje funcional.

---

### 5.14 Bloque 13 — Cierre (10 min)

**Síntesis en 5 puntos:**
1. Unificación + resolución SLD = corazón de Prolog.
2. El backtracking es gratis — pero el orden de cláusulas importa.
3. `!` y `\+` te dan control, pero sacrifican declaratividad.
4. Listas + recursión con acumulador = 90% de programas útiles.
5. Prolog sigue vivo en 2026: dondequiera que haya reglas, relaciones y razonamiento.

**Consigna del TP:** modelar un dominio real + consultas compuestas + 1 puzzle.

**Pregunta de salida:** “Dame un ejemplo (de tu vida cotidiana o trabajo) que sería **más fácil** en Prolog que en Python.”

---

## 6. Mapa de Filminas (≈150 filminas — 1 cada 1–2 min)

Distribución tentativa para la redacción de clase (el desglose final se decide al escribir la minuta):

| Bloque | Min | Filminas estimadas | Rango |
|--------|-----|--------------------|-------|
| B0 Repaso | 10 | 5 | F-001 a F-005 |
| B1 Unificación | 25 | 18 | F-006 a F-023 |
| B2 SLD | 25 | 15 | F-024 a F-038 |
| B3 Backtracking | 25 | 16 | F-039 a F-054 |
| B4 Corte | 20 | 12 | F-055 a F-066 |
| B5 Negación | 15 | 9 | F-067 a F-075 |
| B6 Ejercicio | 20 | 8 | F-076 a F-083 |
| B7 Aritmética | 20 | 13 | F-084 a F-096 |
| B8 Listas | 25 | 16 | F-097 a F-112 |
| B9 Recursión | 25 | 14 | F-113 a F-126 |
| B10 Meta-predicados | 20 | 10 | F-127 a F-136 |
| B11 Aplicaciones | 20 | 13 | F-137 a F-149 |
| B12 2026 | 10 | 5 | F-150 a F-154 |
| B13 Cierre | 10 | 4 | F-155 a F-158 |
| **Total** | **270†** | **≈158** | — |

† Sobre-provisión ~30 min para preguntas/ejercicios flex. Ritmo real ≈ 240 min efectivos.

**Criterio de imagen (imagen realista vs. código+explicación):**
- Imagen realista: filminas de apertura, motivación histórica (Colmerauer, ICOT Japón), aplicaciones industriales (radar, medicina), cierre.
- Código + explicación: la mayoría (≥70%) — bloques de código Prolog con anotaciones.
- Diagramas: árboles SLD, árboles de backtracking, flujos de unificación.

---

## 7. Recursos y Bibliografía

### Material de la materia
- `06 programacion logica` (filminas previas de la cátedra — referencia para estilo)

### Libros (en `ingesta/`)
| Libro | Capítulos relevantes |
|-------|--------------------|
| **Sebesta** — *Concepts of Programming Languages* (Pearson 2019) | Cap. 16 — secciones 16.3 a 16.6 (unificación, resolución, ejemplos) |
| **Gabbrielli & Martini** — *Programming Languages: Principles and Paradigms* (Springer 2023) | `ingesta/txt/351-423.txt` — capítulo completo de Programación Lógica |
| **Louden & Lambert** — *Programming Languages: Principles and Practices* (2011) | Cap. 4 Logic Programming |
| **Sterling & Shapiro** — *The Art of Prolog* (MIT, 2e) | Caps. 3, 6, 8 (lectura opcional para TP) |
| **Spivey** — *An Introduction to Logic Programming through Prolog* | Caps. 4–6 |

### Papers 2024–2026 (en `ingesta/txt/2511.17696v1.txt`)
- Contexto de razonamiento neuro-simbólico moderno.

### Herramientas
- **SWI-Prolog 9.x** — https://www.swi-prolog.org/
- **SWISH** (sin instalación) — https://swish.swi-prolog.org/
- **Scryer Prolog** — implementación ISO moderna (opcional)

---

## 8. Notas Pedagógicas

- **Bloque 6 es el punto de respiro del cerebro.** Clase de 240 min sin ejercicio colaborativo en el medio = pérdida de atención garantizada (ver Cognitive Load Theory — Sweller 2023).
- **Trazado en pizarrón OBLIGATORIO** en B2 y B3. No alcanza con mostrar el código — hay que dibujar el árbol.
- **Live-coding en SWISH** en B7, B8, B9, B10 y B11. Tener la URL cargada de antemano.
- **Aritmética** es el bloque donde más errores cometerán. Reservar 2 min extra por pregunta.
- **Corte** es donde los alumnos se pierden conceptualmente. Usar la metáfora del “compromiso irrevocable”.
- **Listas**: si alguien no entiende `[H|T]`, dibujar la celda cons (`.(H, T)`) en pizarrón.

---

## 9. Restricciones de Tiempo

- **240 min efectivos** con 1 descanso de 10 min después de B6 (aprox. min 125).
- **B12 (Prolog 2026)** y **B13 (Cierre)** son compresibles a 15 min combinados si el ritmo se atrasa.
- **B6 (ejercicio)** NO es compresible — es pedagógicamente obligatorio.

---

## 10. Validación de Cobertura del Plan Mínimo

| Contenido mínimo institucional cubierto | Sección |
|-----------------------------------------|---------|
| Paradigmas: lógico | Todo el tema |
| Variables, unificación | B1 |
| Backtracking, control | B3, B4 |
| Negación | B5 |
| Listas, recursión | B8, B9 |
| Metaprogramación / consultas | B10 |
| Aplicaciones y dominios | B11, B12 |

---

*Tema 07 — Diseño pedagógico — Paradigmas y Lenguajes de Programación 2026 — UNTdF — 2026-04-21*
*Estado: **APROBADO** (auto-aprobación solicitada por docente)*
