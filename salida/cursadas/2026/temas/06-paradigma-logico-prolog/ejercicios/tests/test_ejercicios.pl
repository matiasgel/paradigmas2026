:- use_module(library(plunit)).
:- consult('../ejercicios-clase1').

% ============================================================
%  TEST SUITE — Paradigma Lógico Clase 1
%  Correr con: swipl -l tests/test_ejercicios.pl
% ============================================================

% --- Ejercicio 4: bisabuelo/2 ---
:- begin_tests(ej04_bisabuelo).
test(bisabuelo_ana_tomas)    :- bisabuelo(ana, tomas).
test(bisabuelo_jorge_tomas)  :- bisabuelo(jorge, tomas).
test(bisabuelo_no_generacion_1) :- \+ bisabuelo(ana, carlos).
test(bisabuelo_todos, set(X == [ana, jorge])) :- bisabuelo(X, tomas).
:- end_tests(ej04_bisabuelo).

% --- Ejercicio 5: madre_de_madre/2 ---
:- begin_tests(ej05_madre_de_madre).
test(mdm_ana_laura)   :- madre_de_madre(ana, laura).
test(mdm_ana_tomas)   :- madre_de_madre(ana, tomas).
test(mdm_ana_pedro)   :- madre_de_madre(ana, pedro).
test(mdm_no_beatriz)  :- \+ madre_de_madre(ana, beatriz).
test(mdm_no_carlos)   :- \+ madre_de_madre(ana, carlos).
:- end_tests(ej05_madre_de_madre).

% --- Ejercicio 7: es_anfibio/1 ---
:- begin_tests(ej07_es_anfibio).
test(anfibio_pinguino) :- es_anfibio(pinguino).
test(no_anfibio_aguila):- \+ es_anfibio(aguila).
test(no_anfibio_perro) :- \+ es_anfibio(perro).
test(anfibio_lista, set(X == [pinguino])) :- es_anfibio(X).
:- end_tests(ej07_es_anfibio).

% --- Ejercicio 8: no_vuela/1 ---
:- begin_tests(ej08_no_vuela).
test(no_vuela_perro)  :- no_vuela(perro).
test(no_vuela_gato)   :- no_vuela(gato).
test(no_vuela_salmon) :- no_vuela(salmon).
test(si_vuela_aguila) :- \+ no_vuela(aguila).
:- end_tests(ej08_no_vuela).

% --- Ejercicio 10: libro_largo/1 ---
:- begin_tests(ej10_libro_largo).
test(largo_sebesta)       :- libro_largo(sebesta).
test(largo_louden)        :- libro_largo(louden).
test(no_largo_gabbrielli) :- \+ libro_largo(gabbrielli).
test(todos_largos, set(A == [louden, sebesta])) :- libro_largo(A).
:- end_tests(ej10_libro_largo).

% --- Ejercicio 13: primo/2 ---
:- begin_tests(ej13_primo).
test(primo_laura_pedro) :- primo(laura, pedro).
test(primo_pedro_laura) :- primo(pedro, laura).
test(no_primo_hermanos) :- \+ primo(carlos, beatriz).
test(no_primo_padre_hijo):- \+ primo(laura, tomas).
:- end_tests(ej13_primo).

% --- Ejercicio 14: son_hermanos_entre_si/2 ---
:- begin_tests(ej14_hermanos_entre_si).
test(hsi_carlos_beatriz)  :- son_hermanos_entre_si(carlos, beatriz).
test(hsi_beatriz_carlos)  :- son_hermanos_entre_si(beatriz, carlos).
test(hsi_laura_pedro)     :- son_hermanos_entre_si(laura, pedro).
test(hsi_no_padre_hijo)   :- \+ son_hermanos_entre_si(carlos, laura).
test(hsi_no_abuela_nieto) :- \+ son_hermanos_entre_si(ana, laura).
:- end_tests(ej14_hermanos_entre_si).

% --- Ejercicio 15: contar_generaciones/3 ---
:- begin_tests(ej15_contar_generaciones).
test(gen_1_ana_carlos) :- contar_generaciones(ana, carlos, 1).
test(gen_1_ana_beatriz):- contar_generaciones(ana, beatriz, 1).
test(gen_2_ana_laura)  :- contar_generaciones(ana, laura, 2).
test(gen_3_ana_tomas)  :- contar_generaciones(ana, tomas, 3).
:- end_tests(ej15_contar_generaciones).

% --- Ejercicio 17: aprobado/1 y desaprobado/1 ---
:- begin_tests(ej17_notas).
test(aprobado_matias) :- aprobado(matias).
test(aprobado_sofia)  :- aprobado(sofia).
test(aprobado_lucas)  :- aprobado(lucas).
test(no_aprobado_ana) :- \+ aprobado(ana_a).
test(desaprobado_ana) :- desaprobado(ana_a).
test(no_desaprobado_matias) :- \+ desaprobado(matias).
:- end_tests(ej17_notas).

% --- Ejercicio 18: es_familiar_directo/2 ---
:- begin_tests(ej18_familiar_directo).
test(fd_progenitor)    :- es_familiar_directo(ana, carlos).
test(fd_hijo)          :- es_familiar_directo(carlos, ana).
test(fd_hermanos)      :- es_familiar_directo(carlos, beatriz).
test(no_fd_abuela_nieto) :- \+ es_familiar_directo(ana, tomas).
test(no_fd_tio_sobrino)  :- \+ es_familiar_directo(carlos, tomas).
:- end_tests(ej18_familiar_directo).

:- run_tests.
:- halt(0).
