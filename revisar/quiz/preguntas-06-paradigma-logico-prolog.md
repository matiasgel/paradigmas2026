---
topic_id: "06-paradigma-logico-prolog"
topic_name: "Paradigma Lógico: Prolog — Clase 1 (Introducción)"
exam_type: "parcial-1"
course_id: "2026"
question_count: 5
points_total: 17
bloom_mix: "recordar: 3pts, comprender: 6pts, aplicar: 4pts, analizar: 4pts"
generated_at: "2026-05-25"
---

# Preguntas — Tema 06: Paradigma Lógico — Prolog Clase 1

---

## P-06-001 | Recordar | Conceptual | 3 pts

**¿Cuáles son los tres tipos de enunciados que forman un programa Prolog?**

a) Variables, predicados y términos  
b) Hechos, reglas y consultas  
c) Funciones, clases y módulos  
d) Proposiciones, implicaciones y conjunciones  

**Respuesta correcta:** b  
**Justificación:** Un programa Prolog se estructura en tres tipos de enunciados: (1) **Hechos** — afirmaciones incondicionales sobre el dominio (`madre(ana, carlos).`); (2) **Reglas** — implicaciones que definen nuevas relaciones en función de otras (`abuela(X, Z) :- madre(X, Y), madre(Y, Z).`); (3) **Consultas** — preguntas que se hacen al motor de inferencia (`?- abuela(ana, laura).`). La ejecución de un programa Prolog es esencialmente el proceso de responder consultas usando la base de conocimiento.  
**Fuente:** minuta.md §B3 — Prolog: hechos, reglas y consultas; diseno.md §5.1 Objetivos Bloom Recordar  
**Bloom:** Recordar  

---

## P-06-002 | Comprender | Conceptual | 3 pts

**¿Cuál es la diferencia fundamental en la forma de "programar" entre el paradigma imperativo y el paradigma lógico?**

a) En el imperativo se usa `if-else`; en el lógico se usa `case-when`  
b) En el imperativo se describe el conocimiento del dominio; en el lógico se describe el algoritmo de resolución  
c) En el imperativo se especifica cómo resolver el problema (algoritmo); en el lógico se especifica qué es verdadero (conocimiento) y el motor de inferencia encuentra las soluciones  
d) El paradigma lógico solo funciona para problemas matemáticos; el imperativo es de propósito general  

**Respuesta correcta:** c  
**Justificación:** La diferencia esencial es de nivel de abstracción. En el paradigma imperativo el programador escribe el algoritmo de búsqueda: los pasos exactos para encontrar la respuesta. En el paradigma lógico el programador declara hechos y reglas (el conocimiento del dominio) y el motor de inferencia de Prolog se encarga de la estrategia de búsqueda. Sebesta: "An execution of a logic program is a proof that a goal statement follows from the program statements."  
**Fuente:** minuta.md §B1 — Declarativo vs Imperativo (F-03); diseno.md §5.1  
**Bloom:** Comprender  

---

## P-06-003 | Comprender | Conceptual | 3 pts

**En Prolog, ¿qué representa una variable y cómo se diferencia de una constante en la sintaxis del lenguaje?**

a) Las variables comienzan con minúscula (ej: `ana`); las constantes comienzan con mayúscula (ej: `X`)  
b) Las variables comienzan con mayúscula o `_` (ej: `X`, `_Y`); las constantes (átomos) comienzan con minúscula (ej: `ana`, `carlos`)  
c) No hay variables en Prolog; todo son constantes simbólicas  
d) Las variables se declaran con `var`; las constantes con `const`, igual que en JavaScript  

**Respuesta correcta:** b  
**Justificación:** En Prolog, la convención es opuesta a la mayoría de los lenguajes: los **átomos** (constantes simbólicas) comienzan con minúscula (`ana`, `madre`, `carlos`) y las **variables** comienzan con mayúscula o `_` (`X`, `Y`, `_Anon`). Cuando el motor encuentra una variable en una consulta, intenta unificarla con algún valor de la base de conocimiento. Esta distinción sintáctica es fundamental para interpretar correctamente las consultas y reglas.  
**Fuente:** minuta.md §B3 — Sintaxis Prolog (F-13 a F-20)  
**Bloom:** Comprender  

---

## P-06-004 | Aplicar | Con código Prolog | 4 pts

**Dada la siguiente base de conocimiento Prolog:**

```prolog
padre(carlos, laura).
padre(carlos, pedro).
padre(tomas, carlos).
padre(tomas, beatriz).

abuelo(X, Z) :- padre(X, Y), padre(Y, Z).
```

**¿Cuál es el resultado de la consulta `?- abuelo(tomas, Z).`?**

a) `false` — no hay suficiente información en la base  
b) `Z = carlos` — Tomás es abuelo de Carlos  
c) `Z = laura ; Z = pedro` — Tomás es abuelo de Laura y Pedro  
d) `Z = carlos ; Z = beatriz` — Tomás es padre de Carlos y Beatriz, no abuelo  

**Respuesta correcta:** c  
**Justificación:** La regla `abuelo(X, Z) :- padre(X, Y), padre(Y, Z)` busca un `Y` intermedio tal que `padre(tomas, Y)` y `padre(Y, Z)`. Instanciando `X = tomas`: se busca `Y` tal que `padre(tomas, Y)`. Hay dos soluciones: `Y = carlos` y `Y = beatriz`. Para `Y = carlos`: se busca `Z` tal que `padre(carlos, Z)` → `Z = laura` y `Z = pedro`. Para `Y = beatriz`: no hay hechos `padre(beatriz, ?)` → sin solución. Resultado: `Z = laura ; Z = pedro`.  
**Fuente:** minuta.md §B3, B4 — Base de conocimiento familiar y trazado (OA-Aplicar, OA-Analizar)  
**Bloom:** Aplicar  

---

## P-06-005 | Analizar | Con código Prolog | 4 pts

**Considerá la siguiente regla Prolog:**

```prolog
hermano(X, Y) :- padre(P, X), padre(P, Y), X \= Y.
```

**¿Cuál de las siguientes afirmaciones describe correctamente lo que hace esta regla?**

a) Define que X es hermano de Y si X y Y tienen el mismo padre P y X es distinto de Y  
b) Define que X es hermano de Y si X es padre de P y P es padre de Y  
c) Define que X es hermano de Y solo si ambos tienen exactamente un padre en común  
d) La regla tiene un error: en Prolog no se puede usar `\=` para comparar variables  

**Respuesta correcta:** a  
**Justificación:** La regla se lee: "X es hermano de Y si existe un P tal que P es padre de X (`padre(P, X)`), P es padre de Y (`padre(P, Y)`), y X es distinto de Y (`X \= Y`)." El operador `\=` en Prolog significa "no unificable", lo que evita que X y Y sean la misma persona (un individuo no puede ser hermano de sí mismo). Esta es la forma declarativa estándar de expresar una relación de hermandad en Prolog.  
**Fuente:** minuta.md §B3 — Reglas en Prolog (OA-Analizar)  
**Bloom:** Analizar  
