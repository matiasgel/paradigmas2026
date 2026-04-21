% Archivo de soluciones de referencia para el docente.
% NO SE INCLUYE EN EL REPO DE ALUMNOS.
% Es una copia del ejercicios-clase2-3.pl con TODOS los predicados resueltos.
% Sirve para validar que los tests pasan.

:- use_module(library(lists)).

% --- Base compartida ---
persona(ana,    22).
persona(beto,   30).
persona(carla,  22).
persona(diego,  45).
persona(elena,  18).
persona(fede,   30).

viaja(ana,    parana).
viaja(ana,    rosario).
viaja(beto,   rosario).
viaja(carla,  parana).
viaja(diego,  ushuaia).
viaja(elena,  ushuaia).
viaja(fede,   rosario).

vuelo(ush, bue, 210).
vuelo(bue, mvd, 45).
vuelo(bue, spo, 140).
vuelo(mvd, spo, 135).
vuelo(spo, bog, 360).
vuelo(bue, bog, 380).

% --- Soluciones ---
iguales(X, Y) :- X = Y.

son_identicos(X, Y) :- X == Y.

descomponer(T, L) :- T =.. L.

comparten_destino(X, Y) :- viaja(X, D), viaja(Y, D), X \= Y.

todos_los_viajeros(D, L) :- findall(P, viaja(P, D), L).

destinos_unicos(L) :- setof(D, P^viaja(P, D), L).

cuadrado(N, C) :- C is N * N.

factorial(0, 1) :- !.
factorial(N, F) :- N > 0, N1 is N - 1, factorial(N1, F1), F is N * F1.

maximo(X, Y, X) :- X >= Y, !.
maximo(_, Y, Y).

valor_absoluto(X, X) :- X >= 0, !.
valor_absoluto(X, A) :- A is -X.

clasificar_edad(E, C) :-
    ( E < 18    -> C = menor
    ; E >= 65   -> C = mayor
    ; C = adulto ).

no_viaja(P, D) :- persona(P, _), \+ viaja(P, D).

pertenece(X, [X|_]).
pertenece(X, [_|T]) :- pertenece(X, T).

concatenar([], L, L).
concatenar([H|T], L, [H|R]) :- concatenar(T, L, R).

longitud([], 0).
longitud([_|T], N) :- longitud(T, N1), N is N1 + 1.

ultimo([X], X).
ultimo([_|T], U) :- ultimo(T, U).

reversa(L, R) :- reversa_aux(L, [], R).
reversa_aux([], Acc, Acc).
reversa_aux([H|T], Acc, R) :- reversa_aux(T, [H|Acc], R).

suma_lista(L, S) :- suma_lista_aux(L, 0, S).
suma_lista_aux([], Acc, Acc).
suma_lista_aux([H|T], Acc, S) :- Acc1 is Acc + H, suma_lista_aux(T, Acc1, S).

maximo_lista([X], X).
maximo_lista([H|T], M) :- maximo_lista(T, MT), ( H >= MT -> M = H ; M = MT ).

contar(_, [], 0).
contar(X, [X|T], N) :- !, contar(X, T, N1), N is N1 + 1.
contar(X, [_|T], N) :- contar(X, T, N).

pares(L, P) :- findall(X, (member(X, L), 0 is X mod 2), P).

promedio_edades(P) :-
    findall(E, persona(_, E), Es),
    sum_list(Es, S),
    length(Es, N),
    P is S / N.

vuelo_directo_o_escala(A, B) :- vuelo(A, B, _).
vuelo_directo_o_escala(A, B) :- vuelo(A, C, _), vuelo(C, B, _).

ruta(A, B, [A, B]) :- vuelo(A, B, _).
ruta(A, B, [A | R]) :- vuelo(A, C, _), ruta(C, B, R).

color_disponible(rojo).
color_disponible(verde).
color_disponible(azul).

colorear_triangulo(A, B, C) :-
    color_disponible(A), color_disponible(B), color_disponible(C),
    A \= B, A \= C, B \= C.

mayores_de(Edad, L) :- setof(P, E^(persona(P, E), E > Edad), L).

estadisticas_lista(L, Min, Max, Prom) :-
    min_list(L, Min),
    max_list(L, Max),
    sum_list(L, S),
    length(L, N),
    Prom is S / N.

no_ataca_diagonales([]).
no_ataca_diagonales([C|Cs]) :-
    no_ataca(C, Cs, 1),
    no_ataca_diagonales(Cs).
no_ataca(_, [], _).
no_ataca(C, [C2|Cs], Dist) :-
    abs(C - C2) =\= Dist,
    Dist1 is Dist + 1,
    no_ataca(C, Cs, Dist1).

cuatro_reinas(Sol) :-
    permutation([1,2,3,4], Sol),
    no_ataca_diagonales(Sol).
