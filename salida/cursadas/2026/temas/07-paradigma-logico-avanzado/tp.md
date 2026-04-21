# Trabajo Práctico — Tema 07: Paradigma Lógico — Clase 2+3

**Materia:** Paradigmas y Lenguajes de Programación 2026
**Docente:** Matías Gel
**Tipo de entrega:** Desarrollo (archivo `.pl` + documento `tp-entrega.md`)
**Fecha de entrega:** 2 semanas desde el día de la clase
**Modalidad:** individual o en pares
**Autora:** Aux. Valeria (tp-designer) — 2026-04-21

---

## Objetivos

Integrar y aplicar los conceptos de la clase 2+3 del módulo Prolog:
- Modelado declarativo de un dominio
- Consultas múltiples sobre una base
- Recursión con y sin acumulador
- Backtracking, corte, meta-predicados
- Resolución de un puzzle con restricciones

---

## Parte 1 — Modelado de un dominio (35% de la nota)

Elegí **uno** de los siguientes dominios (o proponé uno propio justificado):

- **Cine:** películas, directores, actores, géneros, años.
- **Música:** artistas, álbumes, canciones, géneros, colaboraciones.
- **Genealogía:** tu familia real o una ficticia de mínimo 4 generaciones.
- **Transporte:** red de trenes/subtes/colectivos de una ciudad.
- **Red social:** usuarios, amistades, publicaciones, reacciones.
- **Biblioteca:** libros, autores, préstamos, categorías.
- **Deporte:** equipos, jugadores, partidos, resultados.

**Requisitos mínimos:**
- [ ] Al menos **20 hechos** distribuidos en 4 o más predicados distintos.
- [ ] Al menos **5 reglas derivadas** (predicados definidos con `:-`).
- [ ] Al menos **1 regla recursiva** (directa o mutua).
- [ ] El dominio debe ser **coherente** (no hechos contradictorios).

**Entregable:** archivo `tp-dominio.pl` con comentarios explicando la estructura.

### Ejemplo orientativo (no lo copies — es ilustrativo)

```prolog
% Dominio: biblioteca universitaria
libro(prolog_art, sterling, 1994, prolog).
libro(spl_sebesta, sebesta, 2019, teoria).
libro(clean_code, martin, 2008, sw_eng).
% … (al menos 20 hechos)

prestamo(ana, clean_code, '2026-04-10').
prestamo(beto, prolog_art, '2026-04-15').

autor(sterling).
autor(sebesta).

% Reglas derivadas
autor_de(A, L) :- libro(L, A, _, _).

libros_de_genero(G, L) :- libro(L, _, _, G).

tiene_prestamo_activo(P) :- prestamo(P, _, _).

% Recursiva: ¿quién más leyó lo que yo leo?
lectores_en_comun(P1, P2) :-
    prestamo(P1, L, _), prestamo(P2, L, _), P1 \= P2.
```

---

## Parte 2 — 10 consultas significativas (30% de la nota)

Sobre el dominio de la Parte 1, escribir **10 consultas** que demuestren los mecanismos de Prolog.

**Requisitos:**
- [ ] Al menos **3 consultas con múltiples soluciones** (backtracking explícito).
- [ ] Al menos **2 consultas con `findall/3`, `bagof/3` o `setof/3`**.
- [ ] Al menos **1 consulta que use recursión** (p. ej. transitividad, caminos).
- [ ] Al menos **1 consulta con `\+` o `dif/2`** (negación).
- [ ] Al menos **1 consulta con aritmética** (`is/2` o comparadores).

**Entregable:** en `tp-entrega.md`, sección "Consultas":
- Enunciado en lenguaje natural ("¿Cuáles son los libros del autor X?")
- Consulta Prolog correspondiente
- Resultado esperado

### Ejemplo de formato

**Consulta 7 — Promedio de préstamos por persona:**
> Enunciado: "¿Cuál es el número promedio de libros tomados por persona?"
```prolog
promedio_prestamos(P) :-
    findall(C, (setof(L, F^prestamo(Persona, L, F), Libros), length(Libros, C)), Cs),
    sum_list(Cs, S),
    length(Cs, N),
    P is S / N.
```
> Resultado esperado: `P = 1.5` (por ejemplo).

---

## Parte 3 — Puzzle con restricciones (25% de la nota)

Resolver **uno** de los siguientes puzzles:

### Opción A — Zebra Puzzle (Einstein)

Versión simplificada: 3 casas con 3 atributos cada una (color, nacionalidad, mascota), 4 restricciones. Programar la solución y explicar el razonamiento.

### Opción B — Sudoku 4×4

Resolver un Sudoku 4×4 (cuadros 2×2, valores 1–4) con `library(clpfd)`. Mostrar la solución de al menos 2 tableros distintos.

### Opción C — N-reinas para N=6

Resolver el problema de las 6 reinas usando CLP(FD). Mostrar al menos 3 soluciones distintas. Explicar qué hace `all_distinct/1` y cómo se codifican las diagonales.

### Opción D — Propuesta propia

Cualquier puzzle combinatorio con al menos 3 variables y 3 restricciones. Debe estar **justificado por escrito**.

**Entregable:** archivo `tp-puzzle.pl` + sección "Puzzle" en `tp-entrega.md` con:
- Enunciado del puzzle
- Modelado (variables y dominios)
- Restricciones
- Código Prolog completo
- Al menos 1 solución mostrada en el REPL

---

## Parte 4 — Reflexión (10% de la nota)

En `tp-entrega.md`, sección "Reflexión" (máx. 400 palabras), responder:

1. ¿Qué parte del TP fue la más difícil? ¿Por qué?
2. ¿Qué hiciste que habría sido más difícil en Python/TypeScript?
3. ¿Encontraste algún caso donde Prolog no parecía la mejor herramienta? Describilo.
4. Si tuvieras que enseñar 1 concepto de Prolog a un compañero, ¿cuál sería y cómo lo enseñarías?

---

## Formato de entrega

Crear una carpeta con:

```
tp-07-paradigma-logico/
├── tp-entrega.md         # documento integrador
├── tp-dominio.pl          # base de conocimiento
├── tp-puzzle.pl           # puzzle resuelto
└── README.md              # instrucciones para correr el TP
```

**Subir a:**
- Moodle (zip) o Google Classroom, según la consigna del aula.
- Commit + push a un repo personal si lo tenés.

---

## Criterios de evaluación

| Dimensión | Peso | Criterio |
|-----------|:---:|----------|
| **Modelado del dominio** | 35% | Coherencia, número suficiente de hechos/reglas, recursión significativa |
| **Consultas** | 30% | Variedad, uso correcto de mecanismos, claridad del enunciado |
| **Puzzle** | 25% | Resolución correcta, uso de CLP(FD) o generate-and-test, explicación |
| **Reflexión** | 10% | Profundidad, ejemplos concretos, honestidad intelectual |

**Calificación:**
- **10**: excepcional, creativo, usa mecanismos avanzados (cut, meta-predicados, DCG).
- **7–9**: cumple todos los requisitos con calidad.
- **4–6**: cumple los requisitos mínimos.
- **< 4**: rehacer (feedback individual).

---

## Tips y recursos

### Dónde programar
- **SWISH** (online, sin instalar): https://swish.swi-prolog.org/
- **SWI-Prolog** (local): https://www.swi-prolog.org/ (recomendado para TP largo)

### Depuración
- `?- trace, tu_goal.` → ver cada paso
- `?- listing(predicado).` → ver definiciones cargadas

### CLP(FD) cheat
```prolog
:- use_module(library(clpfd)).

% Variables en rango
?- X in 1..10, Y in 1..10.

% Restricciones
?- X + Y #= 15.
?- all_distinct([X, Y, Z]).

% Buscar solución
?- label([X, Y, Z]).
```

### Bibliografía
- Ver `guia-estudio.md` sección 8.
- **The Power of Prolog** (Triska) — altamente recomendado: https://www.metalevel.at/prolog

---

## Preguntas frecuentes

**¿Puedo hacer el TP en pareja?**
Sí. Entrega única con ambos nombres. La nota es igual para ambos.

**¿Puedo reutilizar código de Internet?**
Sí, citado en `tp-entrega.md`. Pero el modelado del dominio debe ser **original**.

**¿Cuándo uso `!` y cuándo `(-> ;)`?**
Preferir `(-> ;)`. Usar `!` solo si es corte verde (ver guía de estudio sección 3.4).

**¿Tengo que usar CLP(FD)?**
Solo si elegís un puzzle que lo requiera (Opción B, C, o propuesta similar). Para Zebra (Opción A) podés hacerlo con generate-and-test.

**¿Puedo elegir un dominio mío que no esté en la lista?**
Sí, siempre que lo justifiques en la primera sección y tenga complejidad comparable.

**¿Hay clase de consulta antes de la entrega?**
Sí, el jueves de la semana 1 entre clase y entrega. 18–20 hs.

---

*TP elaborado por Aux. Valeria (tp-designer) — 2026-04-21*
*Trazabilidad: cubre B1, B3, B4, B7, B8, B9, B10, B11 de `minuta.md`.*
