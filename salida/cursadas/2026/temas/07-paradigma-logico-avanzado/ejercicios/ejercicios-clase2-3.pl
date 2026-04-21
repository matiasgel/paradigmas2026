:- encoding(utf8).
% ============================================================
%  EJERCICIOS — Paradigma Lógico: Prolog — Clase 2+3
%  Unificación, Backtracking, Corte, Negación, Aritmética,
%  Listas, Recursión avanzada, Meta-predicados, Aplicaciones
%
%  Paradigmas y Lenguajes de Programación 2026 — UNTdF
%
%  INSTRUCCIONES:
%    1. Completar cada predicado donde dice "% COMPLETAR".
%    2. Cargar en SWI-Prolog: ?- consult('ejercicios-clase2-3.pl').
%       O en SWISH: https://swish.swi-prolog.org/
%    3. Correr los tests locales: swipl -l tests/test_ejercicios.pl
%    4. Cada ejercicio tiene ejemplos de consulta al final de su sección.
% ============================================================

:- use_module(library(lists)).

% ============================================================
%  BASE DE CONOCIMIENTO COMPARTIDA
%  No modificar esta sección.
% ============================================================

% --- Personas y edades ---
persona(ana,    22).
persona(beto,   30).
persona(carla,  22).
persona(diego,  45).
persona(elena,  18).
persona(fede,   30).

% --- Viajes ---
viaja(ana,    parana).
viaja(ana,    rosario).
viaja(beto,   rosario).
viaja(carla,  parana).
viaja(diego,  ushuaia).
viaja(elena,  ushuaia).
viaja(fede,   rosario).

% --- Grafo de vuelos (ciudad1, ciudad2, duracion_min) ---
vuelo(ush, bue, 210).
vuelo(bue, mvd, 45).
vuelo(bue, spo, 140).
vuelo(mvd, spo, 135).
vuelo(spo, bog, 360).
vuelo(bue, bog, 380).


% ============================================================
%  EJERCICIO 1 — Unificación: iguales/2
%  Definir iguales(X, Y) que sea true si X e Y unifican.
%  Usar el operador = de Prolog.
%
%  ?- iguales(foo(1,2), foo(A,B)).  % A=1, B=2
%  ?- iguales(ana, ana).             % true
%  ?- \+ iguales(ana, beto).         % true (no unifican)
% ============================================================

% COMPLETAR: iguales(X, Y) :- ???
iguales(_, _) :- fail.


% ============================================================
%  EJERCICIO 2 — Identidad estricta vs unificación: son_identicos/2
%  son_identicos(X, Y) es true si X e Y son estructuralmente
%  idénticos (usar ==). OJO: X == Y NO liga variables.
%
%  ?- son_identicos(ana, ana).        % true
%  ?- \+ son_identicos(X, ana).       % true (X libre, no es idéntico a ana)
%  ?- X = ana, son_identicos(X, ana). % true (X ya ligado)
% ============================================================

% COMPLETAR: son_identicos(X, Y) :- ???
son_identicos(_, _) :- fail.


% ============================================================
%  EJERCICIO 3 — Univ (=..): descomponer/2
%  descomponer(Termino, Lista) debe unificar Lista con
%  [Funtor | Argumentos] del Termino. Usar =..
%
%  ?- descomponer(punto(3,4), L).   % L = [punto, 3, 4]
%  ?- descomponer(persona(ana,22), L). % L = [persona, ana, 22]
% ============================================================

% COMPLETAR: descomponer(T, L) :- ???
descomponer(_, _) :- fail.


% ============================================================
%  EJERCICIO 4 — Backtracking: comparten_destino/2
%  comparten_destino(X, Y) true si X e Y viajan al mismo
%  destino y son personas distintas.
%
%  ?- comparten_destino(ana, carla).   % true (parana)
%  ?- comparten_destino(ana, beto).    % true (rosario)
%  ?- \+ comparten_destino(ana, diego).% true (no comparten)
%  ?- \+ comparten_destino(ana, ana).  % true (X \= Y)
% ============================================================

% COMPLETAR: comparten_destino(X, Y) :- ???
comparten_destino(_, _) :- fail.


% ============================================================
%  EJERCICIO 5 — findall/3: todos_los_viajeros/2
%  todos_los_viajeros(Destino, Lista) une Lista con la lista
%  de personas que viajan a Destino (puede tener duplicados).
%  Usar findall/3.
%
%  ?- todos_los_viajeros(rosario, L).
%    L = [ana, beto, fede].
%  ?- todos_los_viajeros(ushuaia, L).
%    L = [diego, elena].
%  ?- todos_los_viajeros(mendoza, L).
%    L = [].
% ============================================================

% COMPLETAR: todos_los_viajeros(D, L) :- ???
todos_los_viajeros(_, []) :- fail.


% ============================================================
%  EJERCICIO 6 — setof/3: destinos_unicos/1
%  destinos_unicos(L) une L con la lista ordenada y sin
%  duplicados de todos los destinos visitados (de viaja/2).
%  Usar setof/3 con cuantificación existencial (^).
%
%  ?- destinos_unicos(L).
%    L = [parana, rosario, ushuaia].
% ============================================================

% COMPLETAR: destinos_unicos(L) :- ???
destinos_unicos([]) :- fail.


% ============================================================
%  EJERCICIO 7 — Aritmética: cuadrado/2
%  cuadrado(N, C) unifica C con N*N. Usar is/2.
%
%  ?- cuadrado(5, C).   % C = 25
%  ?- cuadrado(0, C).   % C = 0
%  ?- cuadrado(-3, C).  % C = 9
% ============================================================

% COMPLETAR: cuadrado(N, C) :- ???
cuadrado(_, _) :- fail.


% ============================================================
%  EJERCICIO 8 — Aritmética recursiva: factorial/2
%  factorial(N, F) unifica F con N!.
%  Caso base: factorial(0, 1).
%  Recursivo: factorial(N, F) :- N > 0, ..., F is N * F1.
%
%  ?- factorial(0, F).   % F = 1
%  ?- factorial(5, F).   % F = 120
%  ?- factorial(7, F).   % F = 5040
% ============================================================

% COMPLETAR (dos cláusulas): factorial/2
factorial(_, _) :- fail.


% ============================================================
%  EJERCICIO 9 — Corte verde: maximo/3
%  maximo(X, Y, M) unifica M con el mayor entre X e Y.
%  Usar corte (!) para evitar backtracking redundante.
%
%  ?- maximo(7, 3, M).   % M = 7
%  ?- maximo(3, 7, M).   % M = 7
%  ?- maximo(5, 5, M).   % M = 5
% ============================================================

% COMPLETAR: maximo/3
maximo(_, _, _) :- fail.


% ============================================================
%  EJERCICIO 10 — Corte rojo: valor_absoluto/2
%  valor_absoluto(X, A) unifica A con |X|.
%  Usar corte para el caso X >= 0.
%
%  ?- valor_absoluto(5, A).    % A = 5
%  ?- valor_absoluto(-5, A).   % A = 5
%  ?- valor_absoluto(0, A).    % A = 0
% ============================================================

% COMPLETAR: valor_absoluto/2
valor_absoluto(_, _) :- fail.


% ============================================================
%  EJERCICIO 11 — if-then-else: clasificar_edad/2
%  clasificar_edad(Edad, Categoria) asigna:
%    - "menor"  si Edad < 18
%    - "adulto" si 18 =< Edad < 65
%    - "mayor"  si Edad >= 65
%  Usar el operador (Cond -> Then ; Else).
%
%  ?- clasificar_edad(15, C).  % C = menor
%  ?- clasificar_edad(30, C).  % C = adulto
%  ?- clasificar_edad(70, C).  % C = mayor
%  ?- clasificar_edad(18, C).  % C = adulto
%  ?- clasificar_edad(65, C).  % C = mayor
% ============================================================

% COMPLETAR: clasificar_edad/2
clasificar_edad(_, _) :- fail.


% ============================================================
%  EJERCICIO 12 — Negación por falla: no_viaja/2
%  no_viaja(Persona, Destino) true si Persona existe pero
%  no viaja a Destino. Usar \+/1.
%  REQUISITO: Persona debe estar en persona/2 (evita problemas con CWA).
%
%  ?- no_viaja(ana, ushuaia).    % true (ana va a parana y rosario)
%  ?- \+ no_viaja(ana, parana).  % true (sí viaja)
%  ?- no_viaja(diego, parana).   % true
% ============================================================

% COMPLETAR: no_viaja/2
no_viaja(_, _) :- fail.


% ============================================================
%  EJERCICIO 13 — member/2 manual: pertenece/2
%  Definir pertenece(X, Lista) SIN usar member/2 incorporado.
%  Usar recursión con patrón [H|T].
%
%  ?- pertenece(2, [1,2,3]).       % true
%  ?- \+ pertenece(5, [1,2,3]).    % true
%  ?- findall(X, pertenece(X, [a,b,c]), L).  % L = [a,b,c]
% ============================================================

% COMPLETAR (dos cláusulas): pertenece/2
pertenece(_, _) :- fail.


% ============================================================
%  EJERCICIO 14 — append/3 manual: concatenar/3
%  Definir concatenar(L1, L2, L3) SIN usar append/3 incorporado.
%
%  ?- concatenar([1,2], [3,4], L).   % L = [1,2,3,4]
%  ?- concatenar([], [1,2], L).      % L = [1,2]
%  ?- concatenar([a], [], L).        % L = [a]
% ============================================================

% COMPLETAR (dos cláusulas): concatenar/3
concatenar(_, _, _) :- fail.


% ============================================================
%  EJERCICIO 15 — length/2 manual: longitud/2
%  Definir longitud(Lista, N) SIN usar length/2 incorporado.
%
%  ?- longitud([], N).            % N = 0
%  ?- longitud([a,b,c], N).       % N = 3
%  ?- longitud([1,2,3,4,5], N).   % N = 5
% ============================================================

% COMPLETAR (dos cláusulas): longitud/2
longitud(_, _) :- fail.


% ============================================================
%  EJERCICIO 16 — Último elemento: ultimo/2
%  ultimo(Lista, U) unifica U con el último elemento de Lista.
%  Recursión sin acumulador.
%
%  ?- ultimo([1,2,3], U).   % U = 3
%  ?- ultimo([unico], U).   % U = unico
%  ?- \+ ultimo([], _).     % true (falla con lista vacía)
% ============================================================

% COMPLETAR (dos cláusulas): ultimo/2
ultimo(_, _) :- fail.


% ============================================================
%  EJERCICIO 17 — Reverse con acumulador: reversa/2
%  reversa(Lista, R) unifica R con Lista invertida.
%  OBLIGATORIO: implementar con acumulador (O(n)).
%
%  Pista: definir reversa(L, R) :- reversa_aux(L, [], R).
%         Caso base:   reversa_aux([], Acc, Acc).
%         Recursivo:   reversa_aux([H|T], Acc, R) :- reversa_aux(T, [H|Acc], R).
%
%  ?- reversa([1,2,3], R).   % R = [3,2,1]
%  ?- reversa([], R).        % R = []
%  ?- reversa([a], R).       % R = [a]
% ============================================================

% COMPLETAR: reversa/2 y reversa_aux/3
reversa(_, _) :- fail.


% ============================================================
%  EJERCICIO 18 — Suma con acumulador: suma_lista/2
%  suma_lista(Lista, S) unifica S con la suma de elementos.
%  OBLIGATORIO: usar acumulador.
%
%  ?- suma_lista([1,2,3,4], S).   % S = 10
%  ?- suma_lista([], S).          % S = 0
%  ?- suma_lista([10], S).        % S = 10
% ============================================================

% COMPLETAR: suma_lista/2 y suma_lista_aux/3
suma_lista(_, _) :- fail.


% ============================================================
%  EJERCICIO 19 — Máximo de lista: maximo_lista/2
%  maximo_lista(Lista, M) unifica M con el mayor elemento.
%  Asumir lista no vacía. Usar acumulador o recursión.
%
%  ?- maximo_lista([3, 1, 4, 1, 5, 9, 2, 6], M).  % M = 9
%  ?- maximo_lista([42], M).                      % M = 42
%  ?- maximo_lista([-3, -1, -7], M).              % M = -1
% ============================================================

% COMPLETAR: maximo_lista/2
maximo_lista(_, _) :- fail.


% ============================================================
%  EJERCICIO 20 — Contar ocurrencias: contar/3
%  contar(X, Lista, N) unifica N con la cantidad de veces
%  que X aparece en Lista.
%
%  ?- contar(a, [a,b,a,c,a], N).   % N = 3
%  ?- contar(z, [a,b,c], N).       % N = 0
%  ?- contar(1, [], N).            % N = 0
% ============================================================

% COMPLETAR (dos cláusulas dependiendo de si H==X): contar/3
contar(_, _, _) :- fail.


% ============================================================
%  EJERCICIO 21 — Pares de la lista: pares/2
%  pares(Lista, P) unifica P con la lista de elementos pares.
%  Usar findall/3 + member/2 + aritmética (0 is X mod 2).
%
%  ?- pares([1,2,3,4,5,6], P).   % P = [2,4,6]
%  ?- pares([1,3,5], P).         % P = []
%  ?- pares([], P).              % P = []
% ============================================================

% COMPLETAR: pares/2
pares(_, []) :- fail.


% ============================================================
%  EJERCICIO 22 — Meta-predicado: promedio_edades/1
%  promedio_edades(P) unifica P con el promedio de edades
%  de todas las personas de persona/2. Usar findall + aritmética.
%
%  ?- promedio_edades(P).
%  % P es el promedio (22+30+22+45+18+30)/6 = 27.833...
% ============================================================

% COMPLETAR: promedio_edades/1
promedio_edades(_) :- fail.


% ============================================================
%  EJERCICIO 23 — Grafo: vuelo_directo_o_escala/2
%  vuelo_directo_o_escala(Origen, Destino) true si existe
%  un vuelo directo Origen -> Destino O un vuelo con 1 escala.
%  Usar OR (;) o dos cláusulas.
%
%  ?- vuelo_directo_o_escala(ush, bue).  % true (directo)
%  ?- vuelo_directo_o_escala(ush, mvd).  % true (ush->bue->mvd)
%  ?- vuelo_directo_o_escala(ush, spo).  % true (ush->bue->spo)
%  ?- \+ vuelo_directo_o_escala(bog, ush).% true (no hay vuelta)
% ============================================================

% COMPLETAR: vuelo_directo_o_escala/2
vuelo_directo_o_escala(_, _) :- fail.


% ============================================================
%  EJERCICIO 24 — Grafo recursivo: ruta/3
%  ruta(Origen, Destino, Camino) unifica Camino con una lista
%  de ciudades visitadas para llegar de Origen a Destino.
%
%  Caso base:   ruta(A, B, [A,B]) :- vuelo(A, B, _).
%  Recursivo:   ruta(A, B, [A|R]) :- vuelo(A, C, _), ruta(C, B, R).
%
%  ?- ruta(ush, bog, C).
%    C = [ush, bue, bog] ;
%    C = [ush, bue, spo, bog] ;
%    C = [ush, bue, mvd, spo, bog].
% ============================================================

% COMPLETAR (dos cláusulas): ruta/3
ruta(_, _, _) :- fail.


% ============================================================
%  EJERCICIO 25 — CSP: colorear_triangulo/3
%  Dado un triángulo de regiones A, B, C donde cada par es
%  vecino, asignar colores distintos usando 3 colores disponibles.
%  Los colores son: rojo, verde, azul.
%
%  colorear_triangulo(A, B, C) debe unificar A, B, C con
%  colores tales que todos sean distintos.
%
%  ?- colorear_triangulo(A, B, C).
%  % debe enumerar las 6 permutaciones.
%  ?- findall(A-B-C, colorear_triangulo(A,B,C), L), length(L, N).
%  % N = 6
% ============================================================

% Helper (no modificar):
color_disponible(rojo).
color_disponible(verde).
color_disponible(azul).

% COMPLETAR: colorear_triangulo/3
colorear_triangulo(_, _, _) :- fail.


% ============================================================
%  EJERCICIO 26 — Listas con condición: mayores_de/3
%  mayores_de(Edad, Lista) unifica Lista con los nombres de
%  personas cuya edad es > Edad. Ordenar con setof.
%
%  ?- mayores_de(25, L).    % L = [beto, diego, fede]
%  ?- mayores_de(40, L).    % L = [diego]
%  ?- \+ mayores_de(50, _). % true (setof falla si no hay)
% ============================================================

% COMPLETAR: mayores_de/2
mayores_de(_, _) :- fail.


% ============================================================
%  EJERCICIO 27 — Integrador: estadisticas_lista/4
%  estadisticas_lista(Lista, Min, Max, Prom) con Lista no vacía.
%  Usa min_list, max_list y sum_list (incorporados).
%
%  ?- estadisticas_lista([1,2,3,4,5], Min, Max, P).
%    Min = 1, Max = 5, P = 3.0.
%  ?- estadisticas_lista([10], Min, Max, P).
%    Min = 10, Max = 10, P = 10.0.
% ============================================================

% COMPLETAR: estadisticas_lista/4
estadisticas_lista(_, _, _, _) :- fail.


% ============================================================
%  EJERCICIO 28 — Desafío: n_reinas simplificado (N=4)
%  Resolver 4-reinas (4 reinas en tablero 4x4 sin atacarse).
%  Cada solución es una lista [C1,C2,C3,C4] donde Ci es la
%  columna de la reina en la fila i.
%
%  Reglas:
%  - Todas las columnas distintas (no misma columna).
%  - No en misma diagonal: |Ci - Cj| \= |i - j|.
%
%  cuatro_reinas(Sol) debe devolver una lista de 4 enteros.
%
%  ?- cuatro_reinas(S).
%    S = [2,4,1,3] ; S = [3,1,4,2].
%  ?- findall(S, cuatro_reinas(S), L), length(L, N).
%    N = 2.
%
%  Pista: usar permutation/2 y luego chequear no_ataca_diagonales/1.
% ============================================================

% Helper provisto (no modificar):
no_ataca_diagonales([]).
no_ataca_diagonales([C|Cs]) :-
    no_ataca(C, Cs, 1),
    no_ataca_diagonales(Cs).

no_ataca(_, [], _).
no_ataca(C, [C2|Cs], Dist) :-
    abs(C - C2) =\= Dist,
    Dist1 is Dist + 1,
    no_ataca(C, Cs, Dist1).

% COMPLETAR: cuatro_reinas/1
% Pista: permutation([1,2,3,4], Sol), no_ataca_diagonales(Sol).
cuatro_reinas(_) :- fail.


% ============================================================
%  FIN DE EJERCICIOS
%
%  Para correr tests:
%    swipl -l tests/test_ejercicios.pl
%
%  Para entregar:
%    commit + push al repo de GitHub Classroom.
%    El workflow autograding corre tests automáticamente.
% ============================================================
