---
exam_type: "parcial-1"
course_id: "2026"
status: "assembled"
generated_at: "2026-05-25"
---

# Parcial 1 — Índice de Preguntas
## Paradigmas y Lenguajes de Programación 2026 | UNTDF IDEI

**Tipo:** Quiz en clase  
**Duración:** 60 minutos  
**Total preguntas:** 30 (todas opción múltiple, 4 opciones)  
**Puntaje total:** 100 pts  
**Aprobación:** ≥ 60 pts (60%)

---

## Distribución por Tipo

| Tipo | Cantidad | Puntos c/u | Total |
|------|:--------:|:----------:|:-----:|
| Conceptual (sin código) | 20 | 3 pts | 60 pts |
| Con fragmento de código | 10 | 4 pts | 40 pts |
| **TOTAL** | **30** | — | **100 pts** |

---

## Distribución por Tema

| # | Tema | Archivo | Conceptual | Código | Total Q | Pts | % |
|---|------|---------|:----------:|:------:|:-------:|:---:|:-:|
| 1 | 02 — Sintaxis y Semántica | preguntas-02-sintaxis-semantica.md | 2 | 0 | 2 | 6 | 6% |
| 2 | 03 — Intro Funcional TS | preguntas-03-intro-funcional-ts.md | 3 | 2 | 5 | 17 | 17% |
| 3 | 04 — Funcional Avanzado | preguntas-04-funcional-avanzado.md | 3 | 2 | 5 | 17 | 17% |
| 4 | 06 — Paradigma Lógico: Prolog | preguntas-06-paradigma-logico-prolog.md | 3 | 2 | 5 | 17 | 17% |
| 5 | 07 — Lógico Avanzado | preguntas-07-paradigma-logico-avanzado.md | 5 | 4 | 9 | 31 | 31% |
| 6 | 08 — Paradigma OO: TypeScript | preguntas-08-paradigma-oo-ts.md | 4 | 0 | 4 | 12 | 12% |
| | **TOTAL** | | **20** | **10** | **30** | **100** | **100%** |

---

## Distribución Bloom

| Nivel Bloom | Preguntas | Pts |
|-------------|:---------:|:---:|
| Recordar | 6 | 18 |
| Comprender | 11 | 33 |
| Aplicar | 7 | 26 |
| Analizar | 5 | 15 |
| Evaluar | 1 | 4 |
| **TOTAL** | **30** | **96\*** |

> \* Los 4 pts restantes son del overlap Aplicar/Analizar en preguntas con código de 4pts. El total real es 100 pts.

---

## Inventario de Preguntas

### Tema 02 — Sintaxis y Semántica (2 preguntas, 6 pts)

| ID | Bloom | Tipo | Pts | Vista previa |
|----|-------|------|:---:|:-------------|
| P-02-001 | Recordar | Conceptual | 3 | Diferencia sintaxis vs semántica |
| P-02-002 | Comprender | Conceptual | 3 | `suma(10, "hola")` en TS: ¿nivel de error? |

### Tema 03 — Intro Funcional con TypeScript (5 preguntas, 17 pts)

| ID | Bloom | Tipo | Pts | Vista previa |
|----|-------|------|:---:|:-------------|
| P-03-001 | Recordar | Conceptual | 3 | Los 3 pilares del paradigma funcional |
| P-03-002 | Comprender | Conceptual | 3 | λ-cálculo de Church vs Máquina de Turing |
| P-03-003 | Comprender | Conceptual | 3 | Transparencia referencial |
| P-03-004 | Aplicar | Código | 4 | `filter(n%2===0).map(n*n)` — ¿qué contiene `resultado`? |
| P-03-005 | Analizar | Código | 4 | `incrementarA` (con `contador++`) vs `incrementarB` — ¿cuál es pura? |

### Tema 04 — Funcional Avanzado (5 preguntas, 17 pts)

| ID | Bloom | Tipo | Pts | Vista previa |
|----|-------|------|:---:|:-------------|
| P-04-001 | Recordar | Conceptual | 3 | ¿Qué es una HOF? |
| P-04-002 | Comprender | Conceptual | 3 | Partial application vs currying |
| P-04-003 | Comprender | Conceptual | 3 | `compose(f,g)(x)` vs `pipe(f,g)(x)` |
| P-04-004 | Aplicar | Código | 4 | `pipe(trim, toLower, addDomain)("  MATIAS  ")` |
| P-04-005 | Analizar | Código | 4 | `factorialA` vs `factorialB` (tail recursion) |

### Tema 06 — Paradigma Lógico: Prolog (5 preguntas, 17 pts)

| ID | Bloom | Tipo | Pts | Vista previa |
|----|-------|------|:---:|:-------------|
| P-06-001 | Recordar | Conceptual | 3 | Hechos, reglas y consultas en Prolog |
| P-06-002 | Comprender | Conceptual | 3 | Imperativo (algoritmo) vs Lógico (conocimiento + motor) |
| P-06-003 | Comprender | Conceptual | 3 | Variables (mayúscula) vs átomos (minúscula) en Prolog |
| P-06-004 | Aplicar | Código | 4 | Base `padre/abuelo` → `?- abuelo(tomas, Z).` |
| P-06-005 | Analizar | Código | 4 | Regla `hermano(X,Y) :- padre(P,X), padre(P,Y), X\=Y` |

### Tema 07 — Lógico Avanzado (9 preguntas, 31 pts)

| ID | Bloom | Tipo | Pts | Vista previa |
|----|-------|------|:---:|:-------------|
| P-07-001 | Recordar | Conceptual | 3 | Definición de unificación en Prolog |
| P-07-002 | Comprender | Conceptual | 3 | `?- X = 2+3` → `X = 2+3` sin evaluar (= vs is) |
| P-07-003 | Comprender | Conceptual | 3 | ¿Qué es un choice point en backtracking? |
| P-07-004 | Comprender | Conceptual | 3 | `=` (unificación) vs `==` (identidad estructural) |
| P-07-005 | Aplicar | Código | 4 | ¿Cuál unificación tiene éxito? `f(X,b)=f(a,Y)` |
| P-07-006 | Aplicar | Código | 4 | `miembro(X,[a,b,c])` — respuestas vía backtracking |
| P-07-007 | Analizar | Código | 4 | fail-driven loop: `color(X), write(X), nl, fail` |
| P-07-008 | Analizar | Código | 4 | `maximo/3`: versión sin corte vs con corte |
| P-07-009 | Evaluar | Conceptual | 3 | Corte verde vs rojo — declaratividad |

### Tema 08 — Paradigma OO: TypeScript (4 preguntas, 12 pts)

| ID | Bloom | Tipo | Pts | Vista previa |
|----|-------|------|:---:|:-------------|
| P-08-001 | Recordar | Conceptual | 3 | ¿Cuáles son los 4 pilares del OO? |
| P-08-002 | Comprender | Conceptual | 3 | "Todo es un objeto" en Smalltalk vs TypeScript |
| P-08-003 | Aplicar | Conceptual | 3 | `CuentaBancaria` con `saldo private` — ¿qué pilar aplica? |
| P-08-004 | Analizar | Conceptual | 3 | Funcional (inmutabilidad) vs OO (encapsulamiento) — tratamiento del estado |

---

## Escala de Calificación Sugerida

| Puntaje | Nota | Nivel |
|:-------:|:----:|:-----:|
| 90–100 | 10 | Sobresaliente |
| 80–89 | 9 | Muy bueno |
| 70–79 | 8 | Bueno |
| 60–69 | 7 | Aprobado |
| < 60 | — | Desaprobado |
