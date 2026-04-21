:- encoding(utf8).
:- use_module(library(plunit)).
:- use_module(library(lists)).
:- consult('../ejercicios-clase2-3').

% ============================================================
%  TEST SUITE — Paradigma Lógico Clase 2+3
%  Correr con: swipl -l tests/test_ejercicios.pl
% ============================================================

% --- Ej 1: iguales/2 ---
:- begin_tests(ej01_iguales).
test(iguales_atomos)        :- iguales(ana, ana).
test(iguales_compuestos)    :- iguales(foo(1,2), foo(1,2)).
test(iguales_con_variable)  :- iguales(X, ana), X == ana.
test(no_iguales_funtores)   :- \+ iguales(foo(1), bar(1)).
test(no_iguales_aridad)     :- \+ iguales(foo(1), foo(1,2)).
:- end_tests(ej01_iguales).

% --- Ej 2: son_identicos/2 ---
:- begin_tests(ej02_son_identicos).
test(identicos_atomo)           :- son_identicos(ana, ana).
test(identicos_compuesto)       :- son_identicos(f(1,2), f(1,2)).
test(no_identicos_var_libre)    :- \+ son_identicos(_X, ana).
test(identicos_tras_ligadura)   :- X = ana, son_identicos(X, ana).
test(no_identicos_distintos)    :- \+ son_identicos(ana, beto).
:- end_tests(ej02_son_identicos).

% --- Ej 3: descomponer/2 ---
:- begin_tests(ej03_descomponer).
test(descomp_punto, [true(L == [punto,3,4])])      :- descomponer(punto(3,4), L).
test(descomp_atomo, [true(L == [ana])])            :- descomponer(ana, L).
test(descomp_persona, [true(L == [persona,ana,22])]) :- descomponer(persona(ana,22), L).
:- end_tests(ej03_descomponer).

% --- Ej 4: comparten_destino/2 ---
:- begin_tests(ej04_comparten_destino).
test(cd_ana_carla)      :- comparten_destino(ana, carla).
test(cd_ana_beto)       :- comparten_destino(ana, beto).
test(cd_beto_fede)      :- comparten_destino(beto, fede).
test(cd_diego_elena)    :- comparten_destino(diego, elena).
test(no_cd_mismo)       :- \+ comparten_destino(ana, ana).
test(no_cd_sin_comun)   :- \+ comparten_destino(ana, diego).
:- end_tests(ej04_comparten_destino).

% --- Ej 5: todos_los_viajeros/2 ---
:- begin_tests(ej05_todos_viajeros).
test(viaj_rosario, [true(Sorted == [ana,beto,fede])]) :-
    todos_los_viajeros(rosario, L), msort(L, Sorted).
test(viaj_ushuaia, [true(Sorted == [diego,elena])]) :-
    todos_los_viajeros(ushuaia, L), msort(L, Sorted).
test(viaj_inexistente, [true(L == [])]) :-
    todos_los_viajeros(mendoza, L).
:- end_tests(ej05_todos_viajeros).

% --- Ej 6: destinos_unicos/1 ---
:- begin_tests(ej06_destinos_unicos).
test(destinos, [true(L == [parana, rosario, ushuaia])]) :-
    destinos_unicos(L).
:- end_tests(ej06_destinos_unicos).

% --- Ej 7: cuadrado/2 ---
:- begin_tests(ej07_cuadrado).
test(cuad_5)   :- cuadrado(5, C), C =:= 25.
test(cuad_0)   :- cuadrado(0, C), C =:= 0.
test(cuad_neg) :- cuadrado(-3, C), C =:= 9.
test(cuad_10)  :- cuadrado(10, C), C =:= 100.
:- end_tests(ej07_cuadrado).

% --- Ej 8: factorial/2 ---
:- begin_tests(ej08_factorial).
test(fact_0)  :- factorial(0, F), F =:= 1.
test(fact_1)  :- factorial(1, F), F =:= 1.
test(fact_5)  :- factorial(5, F), F =:= 120.
test(fact_7)  :- factorial(7, F), F =:= 5040.
test(fact_10) :- factorial(10, F), F =:= 3628800.
:- end_tests(ej08_factorial).

% --- Ej 9: maximo/3 ---
:- begin_tests(ej09_maximo).
test(max_mayor_primero) :- maximo(7, 3, M), M =:= 7.
test(max_mayor_segundo) :- maximo(3, 7, M), M =:= 7.
test(max_iguales)       :- maximo(5, 5, M), M =:= 5.
test(max_negativos)     :- maximo(-3, -7, M), M =:= -3.
:- end_tests(ej09_maximo).

% --- Ej 10: valor_absoluto/2 ---
:- begin_tests(ej10_valor_absoluto).
test(abs_positivo) :- valor_absoluto(5, A),  A =:= 5.
test(abs_negativo) :- valor_absoluto(-5, A), A =:= 5.
test(abs_cero)     :- valor_absoluto(0, A),  A =:= 0.
test(abs_grande)   :- valor_absoluto(-100, A), A =:= 100.
:- end_tests(ej10_valor_absoluto).

% --- Ej 11: clasificar_edad/2 ---
:- begin_tests(ej11_clasificar_edad).
test(clas_menor,    [true(C == menor)])  :- clasificar_edad(15, C).
test(clas_adulto,   [true(C == adulto)]) :- clasificar_edad(30, C).
test(clas_mayor,    [true(C == mayor)])  :- clasificar_edad(70, C).
test(clas_limite18, [true(C == adulto)]) :- clasificar_edad(18, C).
test(clas_limite65, [true(C == mayor)])  :- clasificar_edad(65, C).
test(clas_limite17, [true(C == menor)])  :- clasificar_edad(17, C).
:- end_tests(ej11_clasificar_edad).

% --- Ej 12: no_viaja/2 ---
:- begin_tests(ej12_no_viaja).
test(nv_ana_ushuaia)   :- no_viaja(ana, ushuaia).
test(nv_diego_parana)  :- no_viaja(diego, parana).
test(si_viaja_ana_par) :- \+ no_viaja(ana, parana).
test(si_viaja_ana_ros) :- \+ no_viaja(ana, rosario).
:- end_tests(ej12_no_viaja).

% --- Ej 13: pertenece/2 ---
:- begin_tests(ej13_pertenece).
test(pert_primer)      :- pertenece(1, [1,2,3]).
test(pert_medio)       :- pertenece(2, [1,2,3]).
test(pert_ultimo)      :- pertenece(3, [1,2,3]).
test(no_pert)          :- \+ pertenece(5, [1,2,3]).
test(no_pert_vacia)    :- \+ pertenece(x, []).
test(pert_todos, [true(Sorted == [a,b,c])]) :-
    findall(X, pertenece(X, [a,b,c]), L), msort(L, Sorted).
:- end_tests(ej13_pertenece).

% --- Ej 14: concatenar/3 ---
:- begin_tests(ej14_concatenar).
test(conc_normales, [true(L == [1,2,3,4])]) :- concatenar([1,2], [3,4], L).
test(conc_vacia_izq, [true(L == [1,2])])    :- concatenar([], [1,2], L).
test(conc_vacia_der, [true(L == [a])])      :- concatenar([a], [], L).
test(conc_ambas_vacias, [true(L == [])])    :- concatenar([], [], L).
:- end_tests(ej14_concatenar).

% --- Ej 15: longitud/2 ---
:- begin_tests(ej15_longitud).
test(long_vacia)  :- longitud([], N), N =:= 0.
test(long_tres)   :- longitud([a,b,c], N), N =:= 3.
test(long_cinco)  :- longitud([1,2,3,4,5], N), N =:= 5.
test(long_uno)    :- longitud([solo], N), N =:= 1.
:- end_tests(ej15_longitud).

% --- Ej 16: ultimo/2 ---
:- begin_tests(ej16_ultimo).
test(ult_tres)    :- ultimo([1,2,3], U), U == 3.
test(ult_uno)     :- ultimo([unico], U), U == unico.
test(ult_cinco)   :- ultimo([a,b,c,d,e], U), U == e.
test(no_ult_vacia):- \+ ultimo([], _).
:- end_tests(ej16_ultimo).

% --- Ej 17: reversa/2 ---
:- begin_tests(ej17_reversa).
test(rev_normal, [true(R == [3,2,1])])   :- reversa([1,2,3], R).
test(rev_vacia,  [true(R == [])])        :- reversa([], R).
test(rev_uno,    [true(R == [a])])       :- reversa([a], R).
test(rev_largo,  [true(R == [5,4,3,2,1])]) :- reversa([1,2,3,4,5], R).
:- end_tests(ej17_reversa).

% --- Ej 18: suma_lista/2 ---
:- begin_tests(ej18_suma_lista).
test(sum_cuatro)  :- suma_lista([1,2,3,4], S), S =:= 10.
test(sum_vacia)   :- suma_lista([], S), S =:= 0.
test(sum_uno)     :- suma_lista([10], S), S =:= 10.
test(sum_negs)    :- suma_lista([-1,-2,-3], S), S =:= -6.
:- end_tests(ej18_suma_lista).

% --- Ej 19: maximo_lista/2 ---
:- begin_tests(ej19_maximo_lista).
test(ml_mixta)    :- maximo_lista([3,1,4,1,5,9,2,6], M), M =:= 9.
test(ml_uno)      :- maximo_lista([42], M), M =:= 42.
test(ml_negs)     :- maximo_lista([-3,-1,-7], M), M =:= -1.
test(ml_orden)    :- maximo_lista([1,2,3,4,5], M), M =:= 5.
:- end_tests(ej19_maximo_lista).

% --- Ej 20: contar/3 ---
:- begin_tests(ej20_contar).
test(cnt_tres)    :- contar(a, [a,b,a,c,a], N), N =:= 3.
test(cnt_cero)    :- contar(z, [a,b,c], N), N =:= 0.
test(cnt_vacia)   :- contar(1, [], N), N =:= 0.
test(cnt_todos)   :- contar(x, [x,x,x], N), N =:= 3.
:- end_tests(ej20_contar).

% --- Ej 21: pares/2 ---
:- begin_tests(ej21_pares).
test(par_normal, [true(Sorted == [2,4,6])]) :-
    pares([1,2,3,4,5,6], P), msort(P, Sorted).
test(par_ninguno, [true(P == [])])          :- pares([1,3,5], P).
test(par_vacia,   [true(P == [])])          :- pares([], P).
test(par_todos,   [true(Sorted == [2,4,6,8])]) :-
    pares([2,4,6,8], P), msort(P, Sorted).
:- end_tests(ej21_pares).

% --- Ej 22: promedio_edades/1 ---
:- begin_tests(ej22_promedio_edades).
test(prom)  :- promedio_edades(P), P > 27.8, P < 27.9.
:- end_tests(ej22_promedio_edades).

% --- Ej 23: vuelo_directo_o_escala/2 ---
:- begin_tests(ej23_vuelo_directo_escala).
test(directo_ush_bue)  :- vuelo_directo_o_escala(ush, bue).
test(escala_ush_mvd)   :- vuelo_directo_o_escala(ush, mvd).
test(escala_ush_spo)   :- vuelo_directo_o_escala(ush, spo).
test(directo_bue_bog)  :- vuelo_directo_o_escala(bue, bog).
test(no_hay_vuelta)    :- \+ vuelo_directo_o_escala(bog, ush).
:- end_tests(ej23_vuelo_directo_escala).

% --- Ej 24: ruta/3 ---
:- begin_tests(ej24_ruta).
test(ruta_directa, [true(C == [ush,bue])])       :- ruta(ush, bue, C).
test(ruta_bue_bog_directa, [true(C == [bue,bog])]) :- ruta(bue, bog, C).
test(ruta_existe_ush_bog)  :-
    findall(C, ruta(ush, bog, C), L), length(L, N), N >= 2.
:- end_tests(ej24_ruta).

% --- Ej 25: colorear_triangulo/3 ---
:- begin_tests(ej25_colorear).
test(color_distintos) :- colorear_triangulo(A, B, C),
    A \= B, A \= C, B \= C.
test(color_seis_soluciones) :-
    findall(A-B-C, colorear_triangulo(A,B,C), L), length(L, N), N =:= 6.
:- end_tests(ej25_colorear).

% --- Ej 26: mayores_de/2 ---
:- begin_tests(ej26_mayores_de).
test(m25, [true(L == [beto,diego,fede])])  :- mayores_de(25, L).
test(m40, [true(L == [diego])])            :- mayores_de(40, L).
test(m50_falla)                            :- \+ mayores_de(50, _).
:- end_tests(ej26_mayores_de).

% --- Ej 27: estadisticas_lista/4 ---
:- begin_tests(ej27_estadisticas).
test(est_cinco) :- estadisticas_lista([1,2,3,4,5], Min, Max, P),
    Min =:= 1, Max =:= 5, P =:= 3.0.
test(est_uno)   :- estadisticas_lista([10], Min, Max, P),
    Min =:= 10, Max =:= 10, P =:= 10.0.
test(est_diez)  :- estadisticas_lista([10,20,30,40], Min, Max, P),
    Min =:= 10, Max =:= 40, P =:= 25.0.
:- end_tests(ej27_estadisticas).

% --- Ej 28: cuatro_reinas/1 ---
:- begin_tests(ej28_cuatro_reinas).
test(reinas_tiene_solucion) :- cuatro_reinas(_).
test(reinas_dos_soluciones) :-
    findall(S, cuatro_reinas(S), L), length(L, N), N =:= 2.
test(reinas_sol_valida) :-
    cuatro_reinas(S), length(S, 4),
    sort(S, Sorted), length(Sorted, 4).  % sin repetidos
:- end_tests(ej28_cuatro_reinas).

% Para correr TODA la suite: swipl -q -t 'run_tests,halt(0)' -l tests/test_ejercicios.pl
% Para correr UN grupo:      swipl -q -t 'run_tests(ej08_factorial),halt(0)' -l tests/test_ejercicios.pl
