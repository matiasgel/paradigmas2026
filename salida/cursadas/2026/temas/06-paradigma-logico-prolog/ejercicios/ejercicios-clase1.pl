% ============================================================
%  EJERCICIOS — Paradigma Lógico: Prolog — Clase 1
%  Paradigmas y Lenguajes de Programación 2026 — UNTdF
%
%  INSTRUCCIONES:
%    1. Cargá este archivo en SWI-Prolog: ?- consult('ejercicios-clase1.pl').
%       O en SWISH: https://swish.swi-prolog.org/
%    2. Cada ejercicio tiene un bloque %--- que indica qué hacer.
%    3. Las consultas de verificación están al final de cada sección.
% ============================================================


% ============================================================
%  BASE DE CONOCIMIENTO — familia.pl (la de clase)
%  No modificar esta sección.
% ============================================================

madre(ana, carlos).
madre(ana, beatriz).
madre(beatriz, laura).
madre(beatriz, pedro).
madre(laura, tomas).

padre(jorge, carlos).
padre(jorge, beatriz).
padre(carlos, laura).
padre(carlos, pedro).

progenitor(X, Y) :- madre(X, Y).
progenitor(X, Y) :- padre(X, Y).

abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).

hermano(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y.

ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).

tio(X, Z) :- hermano(X, Y), progenitor(Y, Z).

descendiente(X, Y) :- ancestro(Y, X).


% ============================================================
%  EJERCICIO 1 — Verificación de hechos simples
%  ¿Verdadero o falso? Probá estas consultas en el intérprete
%  y anotá el resultado esperado ANTES de ejecutar.
%
%  ?- madre(ana, carlos).          % ¿true o false?
%  ?- madre(carlos, ana).          % ¿true o false?
%  ?- padre(jorge, beatriz).       % ¿true o false?
%  ?- madre(jorge, carlos).        % ¿true o false?
% ============================================================


% ============================================================
%  EJERCICIO 2 — Consultas con variable libre
%  Ejecutá y escribí TODAS las respuestas (usá ; para seguir).
%
%  ?- madre(ana, X).
%  ?- padre(X, pedro).
%  ?- progenitor(X, laura).
% ============================================================


% ============================================================
%  EJERCICIO 3 — findall/3
%  Completá y ejecutá:
%
%  % "Todos los hijos de Ana"
%  ?- findall(X, madre(ana, X), L).
%
%  % "Todos los progenitores de Laura"
%  ?- findall(X, progenitor(X, laura), L).
%
%  % "Todos los pares progenitor-hijo"
%  ?- findall(P-H, progenitor(P, H), L).
% ============================================================


% ============================================================
%  EJERCICIO 4 — Regla: bisabuelo/2
%  (Tarea de la clase — completá la definición)
%
%  bisabuelo(X, Z) :- ??? (completar)
%
%  Verificación:
%  ?- bisabuelo(ana, tomas).       % debe ser true
%  ?- bisabuelo(jorge, tomas).     % debe ser true
%  ?- bisabuelo(X, tomas).         % debe dar ana y jorge
% ============================================================

% COMPLETAR: bisabuelo(X, Z) :- ???
bisabuelo(_, _) :- fail.


% ============================================================
%  EJERCICIO 5 — Regla: madre_de_madre/2
%  Definí una regla que sea verdadera cuando X es la madre
%  de la madre de Y. Solo usar el predicado madre/2.
%
%  madre_de_madre(X, Y) :- ??? (completar)
%
%  ?- madre_de_madre(ana, laura).  % debe ser true
%  ?- madre_de_madre(ana, tomas).  % debe ser true
%  ?- madre_de_madre(ana, pedro).  % debe ser true
%  ?- madre_de_madre(ana, beatriz).% debe ser false
% ============================================================

% COMPLETAR: madre_de_madre(X, Y) :- ???
madre_de_madre(_, _) :- fail.


% ============================================================
%  EJERCICIO 6 — Nueva base: animales
%  Agregá los siguientes hechos y respondé las consultas.
%
%  animal(perro).
%  animal(gato).
%  animal(aguila).
%  animal(salmon).
%
%  vuela(aguila).
%  vuela(pinguino).    % ← ojo: esto está bien o mal?
%  nada(salmon).
%  nada(pinguino).
%
%  Consultas:
%  ?- animal(perro).
%  ?- vuela(perro).
%  ?- findall(X, vuela(X), L).
% ============================================================

animal(perro).
animal(gato).
animal(aguila).
animal(salmon).
animal(pinguino).

vuela(aguila).
vuela(pinguino).
nada(salmon).
nada(pinguino).


% ============================================================
%  EJERCICIO 7 — Regla: es_anfibio/1
%  Un animal es anfibio si vuela Y nada.
%
%  es_anfibio(X) :- ??? (completar)
%
%  ?- es_anfibio(pinguino).   % debe ser true
%  ?- es_anfibio(aguila).     % debe ser false
%  ?- findall(X, es_anfibio(X), L).
% ============================================================

% COMPLETAR: es_anfibio(X) :- ???
es_anfibio(_) :- fail.


% ============================================================
%  EJERCICIO 8 — Regla: no_vuela/1
%  Un animal no vuela si es animal y NO vuela.
%  (Usar \+/1 que es el "not provable" de Prolog)
%
%  no_vuela(X) :- ??? (completar)
%
%  ?- no_vuela(perro).    % true
%  ?- no_vuela(aguila).   % false
%  ?- findall(X, no_vuela(X), L).
% ============================================================

% COMPLETAR: no_vuela(X) :- ???
no_vuela(_) :- fail.


% ============================================================
%  EJERCICIO 9 — Nueva base: libros
%
%  libro(sebesta, 'Concepts of Programming Languages', 792).
%  libro(louden,  'Programming Languages: Principles and Practices', 640).
%  libro(gabbrielli, 'Programming Languages: Principles and Paradigms', 390).
%
%  Consultas:
%  ?- libro(sebesta, T, P).        % ¿título y páginas de Sebesta?
%  ?- libro(A, _, P), P > 500.     % ¿libros con más de 500 páginas?
%  ?- findall(A, libro(A,_,_), L). % ¿todos los autores?
% ============================================================

libro(sebesta,    'Concepts of Programming Languages', 792).
libro(louden,     'Programming Languages: Principles and Practices', 640).
libro(gabbrielli, 'Programming Languages: Principles and Paradigms', 390).


% ============================================================
%  EJERCICIO 10 — Regla: libro_largo/1
%  Un libro es largo si tiene más de 600 páginas.
%
%  libro_largo(A) :- ??? (completar)
%
%  ?- libro_largo(sebesta).     % true
%  ?- libro_largo(gabbrielli).  % false
%  ?- findall(A, libro_largo(A), L).
% ============================================================

% COMPLETAR: libro_largo(A) :- ???
libro_largo(_) :- fail.


% ============================================================
%  EJERCICIO 11 — Trazado manual (en papel)
%  Sin ejecutar, trazá paso a paso la resolución de:
%
%    ?- abuelo(jorge, laura).
%
%  ¿Qué cláusulas usa Prolog? ¿Cuántas unificaciones?
%  Dibujá el árbol de derivación.
%
%  (No hay código que escribir — es análisis en papel)
% ============================================================


% ============================================================
%  EJERCICIO 12 — Trazado manual: backtracking
%  Sin ejecutar, trazá:
%
%    ?- abuelo(ana, Z).
%
%  ¿Cuántas soluciones devuelve? ¿En qué orden?
%  Verificá después con: ?- findall(Z, abuelo(ana, Z), L).
% ============================================================


% ============================================================
%  EJERCICIO 13 — Regla: primos/2
%  Dos personas son primas si tienen un abuelo en común
%  y NO son la misma persona.
%
%  primo(X, Y) :- ??? (completar)
%
%  ?- primo(laura, pedro).   % true (mismo abuelo: ana/jorge)
%  ?- primo(laura, tomas).   % false (tomas es hijo de laura)
%  ?- findall(X-Y, primo(X,Y), L).
% ============================================================

% COMPLETAR: primo(X, Y) :- ???
primo(_, _) :- fail.


% ============================================================
%  EJERCICIO 14 — Regla: son_hermanos/1
%  Dado un grupo [H|T], todos son hermanos si H es hermano de
%  cada elemento en T. (Versión simplificada: dos personas)
%
%  Más simple: definí 'son_hermanos_entre_si(X, Y)' usando
%  hermano/2 de forma simétrica (X herm Y y Y herm X).
%
%  ?- son_hermanos_entre_si(carlos, beatriz). % true
%  ?- son_hermanos_entre_si(laura, pedro).    % true
%  ?- son_hermanos_entre_si(carlos, laura).   % false
% ============================================================

% COMPLETAR: son_hermanos_entre_si(X, Y) :- ???
son_hermanos_entre_si(_, _) :- fail.


% ============================================================
%  EJERCICIO 15 — Recursión: contar_generaciones/3
%  contar_generaciones(Ancestro, Descendiente, N) es true
%  si Ancestro está N generaciones arriba de Descendiente.
%
%  Caso base:   N = 1 si progenitor(Ancestro, Descendiente)
%  Caso recursivo: N = N1 + 1 si progenitor(Ancestro, Medio)
%                  y contar_generaciones(Medio, Descendiente, N1)
%
%  contar_generaciones(X, Y, 1) :- progenitor(X, Y).
%  contar_generaciones(X, Y, N) :- ??? (completar)
%
%  ?- contar_generaciones(ana, carlos, N).  % N = 1
%  ?- contar_generaciones(ana, laura, N).   % N = 2
%  ?- contar_generaciones(ana, tomas, N).   % N = 3
% ============================================================

contar_generaciones(X, Y, 1) :- progenitor(X, Y).
% COMPLETAR: contar_generaciones(X, Y, N) :- ???


% ============================================================
%  EJERCICIO 16 — CWA (Supuesto del Mundo Cerrado)
%  Agregá el hecho: tiene_mascota(carlos).
%
%  Respondé:
%  ?- tiene_mascota(carlos).   % ¿qué devuelve?
%  ?- tiene_mascota(ana).      % ¿qué devuelve? ¿por qué?
%
%  REFLEXIÓN: ¿"false" significa que Ana no tiene mascota,
%  o que Prolog no lo sabe? ¿Cuál es la diferencia con el
%  mundo real?
% ============================================================

tiene_mascota(carlos).


% ============================================================
%  EJERCICIO 17 — Nueva base: notas de alumnos
%
%  nota(matias, paradigmas, 8).
%  nota(sofia,  paradigmas, 6).
%  nota(lucas,  paradigmas, 9).
%  nota(ana,    paradigmas, 4).
%
%  Definí:
%    aprobado(Alumno) :- nota del alumno >= 6
%    desaprobado(Alumno) :- nota del alumno < 6
%
%  ?- aprobado(matias).   % true
%  ?- aprobado(ana).      % false
%  ?- findall(A, desaprobado(A), L).
% ============================================================

nota(matias, paradigmas, 8).
nota(sofia,  paradigmas, 6).
nota(lucas,  paradigmas, 9).
nota(ana_a,  paradigmas, 4).

% COMPLETAR: aprobado(Alumno) :- ???
aprobado(_) :- fail.
% COMPLETAR: desaprobado(Alumno) :- ???
desaprobado(_) :- fail.


% ============================================================
%  EJERCICIO 18 — Múltiples cláusulas = OR
%  La clase mostró que dos cláusulas del mismo predicado son OR.
%
%  Definí: es_familiar_directo(X, Y) que sea true si:
%    - X es progenitor de Y, O
%    - Y es progenitor de X, O
%    - son hermanos
%
%  (Tres cláusulas separadas)
%
%  ?- es_familiar_directo(ana, carlos).   % true (madre)
%  ?- es_familiar_directo(carlos, ana).   % true (hijo de)
%  ?- es_familiar_directo(carlos, beatriz). % true (hermanos)
%  ?- es_familiar_directo(ana, tomas).    % false (abuela, no directo)
% ============================================================

% COMPLETAR (tres cláusulas separadas):
es_familiar_directo(_, _) :- fail.


% ============================================================
%  EJERCICIO 19 — Orden de cláusulas importa
%  Copiá la definición de ancestro/2 pero con el caso
%  recursivo ANTES del caso base. ¿Qué pasa con:
%
%  ?- ancestro_v2(ana, carlos).
%
%  Observá el error o el comportamiento. ¿Por qué?
%
%  ADVERTENCIA: puede causar bucle infinito. Usá Ctrl+C para
%  interrumpir en SWI-Prolog.
% ============================================================

% ancestro_v2(X, Y) :- progenitor(X, Z), ancestro_v2(Z, Y).  % caso recursivo
% ancestro_v2(X, Y) :- progenitor(X, Y).                     % caso base


% ============================================================
%  EJERCICIO 20 — Desafío integrador
%  Con TODO lo visto, definí: familia_extendida(X, Miembros)
%  que unifique Miembros con la lista de todos los familiares
%  de X (ancestros + descendientes + hermanos + tíos).
%
%  Pista: usar findall con OR (;) o múltiples findall + append.
%
%  ?- familia_extendida(carlos, M).
%  % debe incluir: ana, jorge, beatriz, laura, pedro, tomas
% ============================================================

familia_extendida(X, Miembros) :-
    findall(F, (
        ancestro(F, X)      % ancestros de X
        ; ancestro(X, F)    % descendientes de X
        ; hermano(X, F)     % hermanos de X
        ; tio(X, F)         % sobrinos de X
        ; tio(F, X)         % tíos de X
    ), Todos),
    sort(Todos, Miembros).  % sort elimina duplicados


% ============================================================
%  FIN DEL ARCHIVO
%  Para cargar en SWI-Prolog:
%    ?- consult('ejercicios-clase1.pl').
%  En SWISH: copiar y pegar el contenido completo.
% ============================================================
