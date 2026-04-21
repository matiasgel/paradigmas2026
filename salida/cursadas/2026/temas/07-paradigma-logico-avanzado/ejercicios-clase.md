# Ejercicios de Clase — Tema 07: Paradigma Lógico (reformulado)

> **Materia:** Paradigmas y Lenguajes de Programación 2026
> **Docente:** Matías Gel — UNTDF / IDEI
> **Uso:** resolver en clase con SWISH (https://swish.swi-prolog.org/) o SWI-Prolog local
> **Estructura:** bloques alineados a las filminas reformuladas (B0, B1, B2, B3, B4, B5, B8)
> **Énfasis:** **listas** (bloque B8 extendido)
> **Modalidad sugerida:** pares o tríos. Resolver en pizarrón/SWISH, chequear respuesta, discutir.
> **Fecha:** 2026-04-21

---

## Cómo usar esta guía

- Cada ejercicio indica **tiempo sugerido** (T), **dificultad** (⭐ fácil, ⭐⭐ media, ⭐⭐⭐ difícil) y **objetivo**.
- Hay **resolución + explicación** al final de cada bloque (plegá la hoja si querés resolver sin mirar).
- Los que dicen **"En voz alta"** no se tipean: se trazan a mano o se explican oralmente.
- Los ejercicios marcados **🎯 clave** son los que deberían salir sí o sí.

---

## B0 — Repaso relámpago (10 min)

### E0.1 ⭐ Identificá (T: 30 s c/u) 🎯 clave

Decí si cada expresión es **átomo, variable, número o estructura**:

1. `ana`
2. `Ana`
3. `42`
4. `padre(juan, X)`
5. `_edad`
6. `'Buenos Aires'`
7. `[1, 2, 3]`

### E0.2 ⭐ Lectura de cláusulas (T: 2 min)

Leé en voz alta en castellano natural:

```prolog
abuelo(X, Z) :- padre(X, Y), progenitor(Y, Z).
```

### E0.3 ⭐ ¿Qué responde Prolog? (T: 2 min)

Dada la base:
```prolog
madre(ana, carlos).
madre(ana, beatriz).
padre(carlos, laura).
```
¿Qué responde?

1. `?- madre(ana, X).`
2. `?- madre(X, laura).`
3. `?- padre(carlos, laura).`

---

## B1 — Unificación (25 min)

### E1.1 ⭐ Los 4 casos (T: 5 min) 🎯 clave

Indicá si unifica y, si unifica, qué sustitución produce:

| # | Expresión | ¿Unifica? | Sustitución |
|---|-----------|:---:|-------------|
| a | `ana = ana` | | |
| b | `X = pedro` | | |
| c | `X = Y` | | |
| d | `f(a, Y) = f(X, b)` | | |
| e | `ana = pedro` | | |
| f | `f(X, X) = f(a, b)` | | |
| g | `padre(X) = madre(X)` | | |
| h | `f(a, b) = f(a, b, c)` | | |

### E1.2 ⭐⭐ Trazado a mano (T: 5 min) 🎯 clave

Unificá paso a paso (escribí cada sustitución):

```
padre(juan, hijo(pedro, X)) = padre(Y, hijo(Z, ana))
```

### E1.3 ⭐⭐ = vs. == vs. =:= (T: 4 min) 🎯 clave

Predecí la respuesta antes de ejecutar:

```prolog
?- X = 5, X == 5.
?- X == 5.
?- X = 2+3, X == 5.
?- X = 2+3, X =:= 5.
?- 2+3 = 5.
?- 2+3 =:= 5.
```

### E1.4 ⭐⭐ Término con `=..` (T: 3 min)

```prolog
?- padre(juan, maria) =.. L.
?- T =.. [saludo, hola, mundo].
?- f(a, b, c) =.. [F | Args].
```

### E1.5 ⭐⭐⭐ El gotcha del occurs-check (T: 3 min)

1. ¿Qué devuelve `?- X = f(X).` en SWI por default?
2. ¿Y `?- unify_with_occurs_check(X, f(X)).`?
3. Explicá en una frase por qué SWI permite la primera.

### E1.6 ⭐⭐ Construí con `=..` (T: 5 min)

Escribí un predicado `mismo_funtor(T1, T2)` que sea verdadero si `T1` y `T2` tienen el mismo funtor y aridad (sin importar los argumentos).

```prolog
mismo_funtor(T1, T2) :-
    % completar usando =..
```

**Ejemplo esperado:**
```prolog
?- mismo_funtor(padre(a,b), padre(x,y)).     true.
?- mismo_funtor(padre(a,b), madre(x,y)).     false.
?- mismo_funtor(padre(a), padre(x,y)).       false.
```

---

## B2 — Resolución SLD (25 min)

### E2.1 ⭐⭐ Árbol SLD a mano (T: 8 min) 🎯 clave

Dada la base:
```prolog
madre(ana, carlos).
madre(ana, beatriz).
padre(carlos, laura).
progenitor(X,Y) :- madre(X,Y).
progenitor(X,Y) :- padre(X,Y).
abuelo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).
```

Dibujá el árbol SLD para `?- abuelo(ana, N).` indicando:
- Todos los choice points.
- Las sustituciones en cada paso.
- Qué ramas fallan y cuáles tienen éxito.

### E2.2 ⭐ Orden de cláusulas (T: 4 min)

Mirá estas dos versiones de `ancestro/2`. ¿Cuál es correcta y cuál puede colgarse?

```prolog
% Versión A
ancestro(X,Y) :- progenitor(X,Y).
ancestro(X,Y) :- progenitor(X,Z), ancestro(Z,Y).

% Versión B
ancestro(X,Y) :- progenitor(X,Z), ancestro(Z,Y).
ancestro(X,Y) :- progenitor(X,Y).
```

**Justificá** por qué una puede entrar en bucle infinito.

### E2.3 ⭐⭐ Regla de selección leftmost (T: 4 min)

Dada la regla:
```prolog
chef(X) :- trabaja(X, Y), cocina(Y), tiene_licencia(X).
```

¿Qué goal prueba Prolog primero? Si querés que falle rápido ante personas sin licencia, ¿cómo reescribirías la regla? Escribila y justificá.

### E2.4 ⭐⭐⭐ "Prolog demuestra, no computa" (T: 4 min, grupal)

Discutí en pareja:
> *"Cada respuesta de Prolog es una demostración formal, no un cálculo."*

¿Qué implicancia práctica tiene esta afirmación para **depurar** un programa?

---

## B3 — Backtracking (25 min)

### E3.1 ⭐ Choice points (T: 3 min) 🎯 clave

Dada:
```prolog
color(rojo).
color(verde).
color(azul).
bebida(agua).
bebida(vino).
```

¿Cuántos choice points crea Prolog al ejecutar `?- color(X), bebida(Y).`? ¿Cuántas soluciones genera en total?

### E3.2 ⭐⭐ `fail`-driven loop (T: 4 min)

Escribí una consulta que **imprima** todos los colores y bebidas combinados usando `write/1`, `nl/0` y `fail/0`.

### E3.3 ⭐⭐ Restricción `\=` (T: 4 min)

```prolog
almuerzo(B, C) :- bebida(B), comida(C), B \= C.
```

Con `comida(vino). comida(pasta).` y `bebida(agua). bebida(vino).`:

1. ¿Cuántas respuestas da `?- almuerzo(B, C).`?
2. Enumeralas en el orden exacto que las da Prolog.

### E3.4 ⭐⭐⭐ Grafo con ciclo (T: 6 min)

Dado:
```prolog
amigo(ana, beto).
amigo(beto, ana).   % ¡ciclo!
amigo(beto, carla).

conoce(X, Y) :- amigo(X, Y).
conoce(X, Z) :- amigo(X, Y), conoce(Y, Z).
```

1. ¿`?- conoce(ana, carla).` termina? ¿En qué respuestas?
2. ¿`?- conoce(ana, X).` termina? ¿Por qué?
3. Reescribí `conoce/2` con **lista de visitados** para que no se cuelgue.

### E3.5 ⭐⭐ Cheatsheet de backtracking (T: 4 min)

Uní con flechas qué hace cada operador:

```
;              →   (a) fuerza backtrack
once(G)        →   (b) colecta todas las soluciones
findall(T,G,L) →   (c) corta alternativas
fail           →   (d) siguiente solución en REPL
!              →   (e) parar en la primera solución
```

### E3.6 ⭐⭐⭐ (Pizarrón) El trail (T: 4 min)

Explicá en 3 viñetas qué es el **trail** y por qué Prolog lo necesita. Mencioná:
- Qué guarda exactamente.
- Qué pasa cuando Prolog hace backtrack.
- Qué diferencia hay con el stack de control.

---

## B4 — Corte `!` (20 min)

### E4.1 ⭐⭐ Verde vs. rojo (T: 5 min) 🎯 clave

Para cada versión de `max/3`, decí si el corte es **verde, rojo** o **no hace falta**:

```prolog
% A
max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.

% B
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).

% C
max(X, Y, X) :- X >= Y, !.
max(X, Y, Y) :- X < Y.
```

### E4.2 ⭐⭐ Descubrí el bug del corte rojo (T: 5 min)

```prolog
clasificar(X, positivo) :- X > 0, !.
clasificar(X, negativo) :- X < 0, !.
clasificar(_, cero).
```

1. ¿Qué devuelve `?- clasificar(5, C).`?
2. ¿Qué devuelve `?- clasificar(0, C).`?
3. ¿Qué devuelve `?- clasificar(-3, C).`?
4. Ahora **sin cortes**: escribí la versión declarativa pura con condiciones **mutuamente excluyentes**.

### E4.3 ⭐⭐ `(-> ;)` (T: 4 min) 🎯 clave

Reescribí usando `(Cond -> Then ; Else)` sin corte:

```prolog
abs(X, X) :- X >= 0, !.
abs(X, Y) :- Y is -X.
```

### E4.4 ⭐⭐⭐ Negación implementada con corte (T: 4 min)

Dada la implementación clásica:
```prolog
not(P) :- call(P), !, fail.
not(_).
```

Explicá paso a paso qué pasa en cada una de estas consultas (base: `color(rojo).`):

1. `?- not(color(rojo)).`
2. `?- not(color(amarillo)).`
3. `?- not(X = 1).`

---

## B5 — Negación por falla (15 min)

### E5.1 ⭐ CWA (T: 3 min)

Dada solo `madre(ana, carlos).`, ¿qué responde Prolog?
1. `?- madre(ana, carlos).`
2. `?- madre(ana, juan).`
3. `?- madre(beatriz, carlos).`

Relacioná con la **Closed World Assumption**.

### E5.2 ⭐⭐ La trampa de `\+` con variables (T: 5 min) 🎯 clave

Predecí y explicá:

```prolog
?- X = 2, \+ X = 1.
?- \+ X = 1, X = 2.
?- \+ member(X, [1,2,3]).
```

**Regla práctica:** ¿cuándo usar `\+` y cuándo **no**?

### E5.3 ⭐⭐ `dif/2` vs `\+` (T: 4 min)

Mostrá un caso donde `dif/2` da la respuesta correcta y `\+` da falsa negativa:

```prolog
?- dif(X, 1), X = 2.
?- \+ X = 1, X = 2.
```

### E5.4 ⭐⭐ `soltero/1` (T: 3 min)

Dada `casado(ana). casado(beto).` escribí `soltero/1` usando `\+`. ¿Qué limitación tiene tu definición?

---

## B8 — Listas (bloque EXTENDIDO, 60 min)

> **Énfasis del docente:** este bloque es el núcleo del TP y del parcial. Resolver TODOS los marcados 🎯.

### B8.A — Notación y estructura (10 min)

#### E8.1 ⭐ Traducí a `[H|T]` (T: 3 min) 🎯 clave

Reescribí cada lista usando la notación **cabeza | cola** (sin azúcar sintáctico cuando se pueda):

| Lista | `[H|T]` | Estructura cruda `./2` |
|-------|---------|------------------------|
| `[a]` | | |
| `[a, b]` | | |
| `[a, b, c]` | | |
| `[a | [b, c]]` | | |

#### E8.2 ⭐ Decí cuál unifica (T: 3 min)

| # | Término 1 | Término 2 | ¿Unifica? | Sust. |
|---|-----------|-----------|:---:|-------|
| a | `[X\|T]` | `[1, 2, 3]` | | |
| b | `[X, Y]` | `[1, 2, 3]` | | |
| c | `[X, Y \| T]` | `[1, 2, 3]` | | |
| d | `[X \| T]` | `[]` | | |
| e | `[X \| Y]` | `[a, b \| Z]` | | |

#### E8.3 ⭐ Lista vacía y no vacía (T: 2 min) 🎯 clave

Definí `esVacia/1` y `noEsVacia/1` por pattern matching (sin operadores de comparación).

---

### B8.B — Primitivas clásicas (15 min)

#### E8.4 ⭐⭐ `primero`, `segundo`, `tercero` (T: 4 min)

Definí tres predicados por pattern matching directo (sin recursión):

```prolog
primero(L, X).   % X es el primero de L
segundo(L, X).
tercero(L, X).
```

#### E8.5 ⭐⭐ `length/2` a mano (T: 4 min) 🎯 clave

Escribí tu propia versión de `length/2` **sin usar la built-in**. Después trazá la ejecución de `?- mi_length([a,b,c], N).`.

```prolog
mi_length([], 0).
mi_length([_|T], N) :- ...
```

#### E8.6 ⭐⭐ `member/2` a mano (T: 4 min) 🎯 clave

Escribí `mi_member/2` desde cero. Luego probá:

1. `?- mi_member(2, [1,2,3]).`
2. `?- mi_member(X, [a,b,c]).`  ← ¿cuántas respuestas?
3. `?- mi_member(X, []).`

#### E8.7 ⭐⭐ `last/2` a mano (T: 3 min)

Definí `mi_last/2` que recupere el último elemento:

```prolog
?- mi_last([a,b,c,d], X).     X = d.
```

---

### B8.C — `append/3` — la joya (15 min)

#### E8.8 ⭐⭐ Los 3 modos de `append/3` (T: 5 min) 🎯 clave

Predecí las respuestas:

```prolog
?- append([1,2], [3,4], R).
?- append(X, Y, [1,2,3]).
?- append([1,2], X, [1,2,3,4]).
?- append(X, [3], [1,2,3]).
```

#### E8.9 ⭐⭐ `append/3` desde cero (T: 4 min) 🎯 clave

Escribí `mi_append/3` en 2 cláusulas. Verificá que funcione en los 3 modos anteriores.

#### E8.10 ⭐⭐⭐ `append` como generador (T: 6 min)

Usá `append/3` (built-in) para definir:

1. `segundo(L, X).` — el segundo elemento de L
2. `ultimos_dos(L, A, B).` — los dos últimos elementos
3. `sublista(S, L).` — S es una sublista contigua de L
4. `sin_ultimo(L, R).` — R es L sin el último elemento

**Pista:** todas se pueden hacer con **una sola línea** usando `append/3`.

---

### B8.D — Recursión sobre listas (15 min)

#### E8.11 ⭐⭐ `suma_lista/2` (T: 4 min) 🎯 clave

Definí `suma_lista(L, S)` que sume los enteros de `L`. Usá `is/2` correctamente.

```prolog
?- suma_lista([1,2,3,4], S).     S = 10.
?- suma_lista([], S).            S = 0.
```

#### E8.12 ⭐⭐ `maximo/2` (T: 4 min)

Definí `maximo(L, M)` que devuelva el mayor elemento de una lista no vacía.

```prolog
?- maximo([3,1,5,2,4], M).     M = 5.
?- maximo([7], M).             M = 7.
```

#### E8.13 ⭐⭐⭐ `reverse/2` ingenua vs. con acumulador (T: 6 min) 🎯 clave

Escribí **dos** versiones de `reverse/2`:

**A) Ingenua con `append/3`:**
```prolog
reverse_v1([], []).
reverse_v1([H|T], R) :- reverse_v1(T, RT), append(RT, [H], R).
```

**B) Con acumulador:**
```prolog
reverse_v2(L, R) :- rev(L, [], R).
rev([], Acc, Acc).
rev([H|T], Acc, R) :- ...
```

Respondé:
1. ¿Cuál es O(n²) y cuál O(n)? ¿Por qué?
2. Trazá ambas para `[1,2,3]`.
3. Investigá: ¿cuál aprovecha **Last-Call Optimization**?

#### E8.14 ⭐⭐ `contar/3` (T: 4 min)

Definí `contar(X, L, N)`: N es cuántas veces aparece `X` en `L`.

```prolog
?- contar(a, [a,b,a,c,a], N).     N = 3.
?- contar(z, [a,b,c], N).         N = 0.
```

---

### B8.E — Meta / utilidades (5 min)

#### E8.15 ⭐⭐ `msort/2` vs `sort/2` (T: 2 min)

Predecí:
```prolog
?- msort([3,1,2,1,3], L).
?- sort([3,1,2,1,3], L).
?- sort(0, @>, [3,1,2,1], L).
```

#### E8.16 ⭐⭐ Lista de pares (T: 3 min)

```prolog
edades([ana-22, beto-30, carla-22]).
```

Escribí una consulta que:
1. Obtenga la edad de `beto`.
2. Ordene la lista de pares por edad usando `keysort/2` (después de invertir los pares).

---

### B8.F — Listas anidadas y `forall/between` (5 min)

#### E8.17 ⭐⭐ Matriz (T: 3 min)

```prolog
matriz([[1,2,3],
        [4,5,6],
        [7,8,9]]).
```

Escribí `fila(N, M, F)` y `elemento(I, J, M, E)` (fila `I`, columna `J`).

#### E8.18 ⭐⭐ `forall` + `between` (T: 2 min)

Predecí:
```prolog
?- forall(between(1,5,X), X > 0).
?- forall(between(1,5,X), X > 3).
?- forall(member(X, [2,4,6]), 0 is X mod 2).
```

---

### B8.G — Ejercicios integradores 🔥 (10 min — elegí 1)

#### E8.19 ⭐⭐⭐ `aplanar/2` 🎯 clave

Definí `aplanar/2` que convierta listas anidadas en una lista plana:

```prolog
?- aplanar([1, [2, [3, 4]], 5], R).     R = [1,2,3,4,5].
?- aplanar([[], [[1,2]], [3]], R).      R = [1,2,3].
```

#### E8.20 ⭐⭐⭐ `permutacion/2`

Definí `permutacion(L1, L2)` que sea verdadero si `L2` es una permutación de `L1`.

```prolog
?- permutacion([1,2,3], P).
P = [1,2,3] ; P = [1,3,2] ; P = [2,1,3] ; ... (6 soluciones)
```

**Pista:** `select/3` + recursión.

#### E8.21 ⭐⭐⭐ `zip/3`

Definí `zip(L1, L2, Pares)`:

```prolog
?- zip([a,b,c], [1,2,3], P).     P = [a-1, b-2, c-3].
?- zip([a,b], [1,2,3], P).       false.
```

---

## Checkpoint de clase (10 min)

### CP1 🎯 En 1 frase cada uno

1. ¿Qué es la MGU?
2. ¿Por qué el orden de las cláusulas importa?
3. ¿Diferencia entre corte verde y corte rojo?
4. ¿Por qué `\+` falla con variables libres?
5. ¿Qué hace `append/3` en su tercer modo?

### CP2 Código ciego

Sin ejecutarlo, ¿qué imprime?

```prolog
?- X = [1,2,3], append(X, [4,5], Y), length(Y, N).
```

### CP3 Escritura libre (2 min)

En un post-it escribí:
> "Lo que más me costó entender de Prolog hasta ahora fue ______."

---

## Soluciones breves (respuestas finales)

### B0
E0.1: 1-átomo, 2-variable, 3-número, 4-estructura, 5-variable (empieza con `_`), 6-átomo, 7-estructura (lista).
E0.3: 1) `X=carlos;X=beatriz.` 2) `false.` (no hay `madre/2` con carlos como madre de laura) 3) `true.`

### B1
E1.1: a) sí, `{}`. b) sí, `{X/pedro}`. c) sí, `{X/Y}`. d) sí, `{X/a, Y/b}`. e) no. f) no. g) no. h) no.
E1.2: `{Y/juan, Z/pedro, X/ana}`.
E1.3: `true; false; false; true; false; true`.
E1.5: 1) éxito con término cíclico. 2) false. 3) occurs-check cuesta O(n); se desactiva por velocidad.

```prolog
mismo_funtor(T1, T2) :-
    T1 =.. [F|A1], T2 =.. [F|A2], length(A1, N), length(A2, N).
```

### B3
E3.1: 3×2=6 choice points implícitos; 6 soluciones.
E3.3: 4 soluciones: (agua,vino),(agua,pasta),(vino,pasta)...
 (solo excluye vino-vino).

### B4
E4.1: A) no hace falta corte B) verde (quita 1 choice point) C) verde.
E4.2:
```prolog
clasificar(X, positivo) :- X > 0.
clasificar(X, negativo) :- X < 0.
clasificar(X, cero)     :- X =:= 0.
```
E4.3:
```prolog
abs(X, Y) :- ( X >= 0 -> Y = X ; Y is -X ).
```

### B5
E5.2: el orden importa; usar `\+` solo con goals **ground**.

### B8 (clave)

```prolog
% E8.3
esVacia([]).
noEsVacia([_|_]).

% E8.5
mi_length([], 0).
mi_length([_|T], N) :- mi_length(T, N1), N is N1 + 1.

% E8.6
mi_member(X, [X|_]).
mi_member(X, [_|T]) :- mi_member(X, T).

% E8.7
mi_last([X], X).
mi_last([_|T], X) :- mi_last(T, X).

% E8.9
mi_append([], L, L).
mi_append([H|T], L, [H|R]) :- mi_append(T, L, R).

% E8.10
segundo(L, X)         :- append([_], [X|_], L).
ultimos_dos(L, A, B)  :- append(_, [A, B], L).
sublista(S, L)        :- append(_, R, L), append(S, _, R).
sin_ultimo(L, R)      :- append(R, [_], L).

% E8.11
suma_lista([], 0).
suma_lista([H|T], S) :- suma_lista(T, ST), S is H + ST.

% E8.12
maximo([X], X).
maximo([H|T], M) :- maximo(T, MT), ( H >= MT -> M = H ; M = MT ).

% E8.13 (B)
reverse_v2(L, R) :- rev(L, [], R).
rev([], Acc, Acc).
rev([H|T], Acc, R) :- rev(T, [H|Acc], R).

% E8.14
contar(_, [], 0).
contar(X, [X|T], N) :- !, contar(X, T, N1), N is N1 + 1.
contar(X, [_|T], N) :- contar(X, T, N).

% E8.17
fila(N, M, F)         :- nth0(N, M, F).
elemento(I, J, M, E)  :- nth0(I, M, Fila), nth0(J, Fila, E).

% E8.19
aplanar([], []).
aplanar([H|T], R) :- is_list(H), !, aplanar(H, HR), aplanar(T, TR), append(HR, TR, R).
aplanar([H|T], [H|TR]) :- aplanar(T, TR).

% E8.20
permutacion([], []).
permutacion(L, [H|P]) :- select(H, L, R), permutacion(R, P).

% E8.21
zip([], [], []).
zip([A|T1], [B|T2], [A-B|TP]) :- zip(T1, T2, TP).
```

---

## Tabla de tiempos sugeridos (clase 240 min)

| Bloque | Ejercicios obligatorios | Tiempo |
|--------|-------------------------|:---:|
| B0 | E0.1, E0.3 | 10 min |
| B1 | E1.1, E1.2, E1.3, E1.6 | 25 min |
| B2 | E2.1, E2.2 | 25 min |
| B3 | E3.1, E3.3, E3.4 | 25 min |
| B4 | E4.1, E4.2, E4.3 | 20 min |
| B5 | E5.1, E5.2 | 15 min |
| ☕ Descanso | — | 10 min |
| B8.A | E8.1, E8.3 | 10 min |
| B8.B | E8.5, E8.6 | 15 min |
| B8.C | E8.8, E8.9, E8.10 | 15 min |
| B8.D | E8.11, E8.13 | 15 min |
| B8.E | E8.15 | 5 min |
| B8.F | E8.17 | 5 min |
| B8.G | elegir 1 de E8.19/20/21 | 10 min |
| Checkpoint | CP1, CP2, CP3 | 10 min |
| **Total** | | **~215 min + 10 buffer** |

---

## Recursos

- **SWISH:** https://swish.swi-prolog.org/ (sin instalar, compartible con link)
- **Guía de estudio del tema:** [`guia-estudio.md`](guia-estudio.md)
- **Minuta del docente:** [`minuta.md`](minuta.md)
- **Filminas:** [`filminas.md`](filminas.md)

---

*Ejercicios elaborados por Aux. Valeria (tp-designer) — 2026-04-21*
*Alineados a las filminas reformuladas (bloques B0, B1, B2, B3, B4, B5, B8).*
*Énfasis especial en listas (B8 extendido a 7 sub-bloques).*
