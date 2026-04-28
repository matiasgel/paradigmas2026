# Filminas — Tema 07: Paradigma Lógico — Clase 2+3 (Unificación, Listas, Backtracking y Corte)

**Materia:** Paradigmas y Lenguajes de Programación 2026
**Docente:** Matías Gel — UNTDF / IDEI
**Duración:** 240 minutos | **Clase:** doble (fusión de clases 2 y 3 del módulo III)
**Fecha:** 2026-04-21
**Total:** ≈158 filminas planeadas

> **⚠️ NOTA DE DICTADO (2026-04-27):** Este archivo fue reorganizado para reflejar el orden y contenido real de la clase.
> **Orden real dictado:** B0 Repaso → B1 Unificación → **B2 Listas** → B3 SLD → B4 Backtracking → B5 Corte → B6 Panorama 2026
> **Bloques NO cubiertos en clase:** B7 Aritmética, B8 Recursión avanzada, B9 Meta-predicados, B10 Aplicaciones (marcados con ⚠️ NO DICTADO).
> La Negación por falla fue mencionada brevemente en el contexto del corte (implementación de `not/1`).

---

## BLOQUE 0 — Repaso relámpago (10 min) · F-001 a F-005

---

### [F-001] Tema 07 — Paradigma Lógico: la segunda mitad
`@tipo: portada`

**Prolog en profundidad**

- Unificación (algoritmo, MGU, operadores)
- Listas (`[H|T]`, `member`, `append`, `last`, `msort`, `forall`)
- Resolución SLD + Backtracking
- Corte (`!`) verde vs. rojo
- Panorama Prolog 2026
- Clase doble — 240 min

> *"We are going to open the black box of Prolog."*

---

### [F-002] ¿Qué traemos de Clase 1?
`@tipo: tabla`

| Concepto | Recordatorio |
|----------|--------------|
| Hecho | `madre(ana, carlos).` |
| Regla | `abuelo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).` |
| Consulta | `?- abuelo(ana, Z).` |
| Término | átomo, número, variable, estructura |
| Recursión | `ancestro(X,Y) :- progenitor(X,Y). ancestro(X,Y) :- progenitor(X,Z), ancestro(Z,Y).` |

---

### [F-003] Quiz relámpago (30 s cada pregunta)
`@tipo: socratica`

1. ¿Un hecho Prolog termina en punto? **(sí)**
2. ¿`X` con mayúscula es variable? **(sí)**
3. ¿`padre(juan, X)` busca al padre de Juan? **(no — busca al hijo)**
4. ¿Prolog prueba cláusulas en cualquier orden? **(no — de arriba a abajo)**

---

### [F-004] Lo que NO vimos todavía
`@tipo: concepto-mixto`

Clase 1 dejó la **caja negra cerrada**:

- ¿Cómo *calza* `X` con `ana`? → **Unificación**
- ¿Cómo encuentra Prolog *la siguiente* solución? → **Backtracking**
- ¿Cómo sumo 2 + 3? → **Aritmética** (no es obvia)
- ¿Cómo guardo una lista? → **`[H|T]`**
- ¿Cómo *mapeo* o *filtro*? → **Meta-predicados**

---

### [F-005] Mapa de la clase — como fue dictada
`@tipo: timeline`

| Min | Bloque | Estado |
|-----|--------|--------|
| 0–10 | B0 Repaso Clase 1 | ✅ dictado |
| 10–50 | B1 Unificación (algoritmo, MGU, `=`, `==`, `=..`, pattern matching) | ✅ dictado |
| 50–85 | B2 Listas (`[H\|T]`, `member`, `append`, `last`, `msort`, `forall`, `between`) | ✅ dictado |
| 85–115 | B3 Resolución SLD (vocabulario, árbol, regla de selección, DFS) | ✅ dictado |
| 115–145 | B4 Backtracking (choice points, trail, fail-loop, árbol de búsqueda) | ✅ dictado |
| 145–175 | B5 Corte — `!` verde vs. rojo, `max/3`, `if-then-else`, impl. `not/1` | ✅ dictado |
| 175–200 | B6 Panorama 2026 (Datalog, neuro-simbólico, implementaciones) | ✅ dictado |
| — | Aritmética `is/2` | ⚠️ no dictado |
| — | Recursión con acumulador / `reverse/2` | ⚠️ no dictado |
| — | Meta-predicados (`findall`, `bagof`, `setof`) | ⚠️ no dictado |
| — | Aplicaciones (N-reinas, mapa de colores) | ⚠️ no dictado |

---

## BLOQUE 1 — Unificación (25 min) · F-006 a F-023

---

### [F-006] ¿Qué es "unificar"?
`@tipo: concepto-abstracto`

**Unificar dos términos** = encontrar una sustitución de variables que los haga **sintácticamente idénticos**.

No es igualdad. No es comparación. Es un **matching con pega**:

> *"Fitting two puzzle pieces by filling in the variables on both sides."*

La unificación es el **único** mecanismo de pasaje de información en Prolog. No hay `=` de asignación; hay unificación.

---

### [F-007] Los 4 casos de unificación
`@tipo: tabla`

| Caso | Ejemplo | Resultado |
|------|---------|-----------|
| **Átomos iguales** | `ana = ana` | éxito, sustitución `{}` |
| **Variable libre** | `X = ana` | éxito, `{X/ana}` |
| **Dos variables** | `X = Y` | éxito, `{X/Y}` (se unen) |
| **Estructura** | `padre(A,B) = padre(juan,X)` | éxito, `{A/juan, B/X}` |

---

### [F-008] Cuándo falla
`@tipo: codigo`

```prolog
?- ana = beatriz.
false.

?- f(X, X) = f(ana, beatriz).
false.           % X no puede ser ana Y beatriz al mismo tiempo

?- padre(X) = madre(X).
false.           % funtores distintos

?- f(a, b) = f(a, b, c).
false.           % aridad distinta (2 ≠ 3)
```

---

### [F-009] El operador `=/2`
`@tipo: concepto-mixto`

```prolog
?- X = 5.
X = 5.

?- 5 = 5.
true.

?- X = Y.
X = Y.          % ambas quedan ligadas mutuamente
```

**Regla mental:** `=` intenta unificar. Si logra, las variables quedan **ligadas**. Si falla, backtrack.

`=` **nunca** evalúa expresiones: `?- X = 2 + 3. → X = 2+3.` (sí, el término, no 5).

---

### [F-010] Algoritmo de unificación (Robinson 1965)
`@tipo: codigo`

```text
unify(t1, t2):
    if t1 == t2:                    # mismos átomos o variables
        return ÉXITO
    if t1 es variable libre:        # ligo t1 a t2
        bind(t1, t2); return ÉXITO
    if t2 es variable libre:
        bind(t2, t1); return ÉXITO
    if t1 = f(a₁..aₙ) ∧ t2 = f(b₁..bₙ):   # mismo funtor y aridad
        for i in 1..n: unify(aᵢ, bᵢ)
        return ÉXITO
    return FALLA
```

---

### [F-011] Trazado paso a paso
`@tipo: demo`

Unificar `padre(juan, hijo(pedro, X))` con `padre(Y, hijo(Z, ana))`:

```
Paso 1:  padre(juan, hijo(pedro,X)) ≡ padre(Y, hijo(Z,ana))
         Funtores iguales (padre/2) → unificar argumentos
Paso 2:  juan ≡ Y            → bind {Y/juan}
Paso 3:  hijo(pedro,X) ≡ hijo(Z,ana)
         Funtores iguales (hijo/2) → unificar argumentos
Paso 4:  pedro ≡ Z           → bind {Z/pedro}
Paso 5:  X ≡ ana             → bind {X/ana}
Resultado: {Y/juan, Z/pedro, X/ana}
```

---

### [F-012] MGU: sustitución más general
`@tipo: concepto-mixto`

Al unificar `f(X)` con `f(Y)`:

- `{X/Y}` ← MGU (más general posible)
- `{X/ana, Y/ana}` ← también unifica pero innecesariamente específica

**Definición:** una sustitución σ es **más general** que τ si existe una sustitución ρ tal que τ = σ ∘ ρ.

Prolog siempre computa la **MGU** — no toma decisiones arbitrarias.

> Consecuencia práctica: las variables quedan lo más libres posible para el resto de la resolución.

---

### [F-013] Unificación en uso — hechos
`@tipo: demo`

```prolog
madre(ana, carlos).
madre(ana, beatriz).

?- madre(ana, X).
X = carlos ;
X = beatriz.
```

Paso a paso para `madre(ana, X)`:
1. Intenta `madre(ana, X) = madre(ana, carlos)` → `{X/carlos}` ✓
2. Usuario pide más (`;`) → backtrack
3. Intenta `madre(ana, X) = madre(ana, beatriz)` → `{X/beatriz}` ✓

---

### [F-014] Unificación en uso — reglas
`@tipo: demo`

```prolog
progenitor(X,Y) :- madre(X,Y).
progenitor(X,Y) :- padre(X,Y).

?- progenitor(P, carlos).
```

1. Unifica con la 1ª regla: `{X/P, Y/carlos}` → nuevo goal `madre(P, carlos)`
2. `madre(P, carlos)` unifica con `madre(ana, carlos)` → `{P/ana}` ✓
3. Usuario pide más → backtrack a la 2ª regla
4. `padre(P, carlos)` busca un hecho `padre(_, carlos)` → falla/éxito según base

---

### [F-015] `=` vs. `==`
`@tipo: tabla-comparativa`

| Operador | Qué hace | Ejemplo | Resultado |
|----------|----------|---------|-----------|
| `X = Y` | Unificación (liga) | `?- X = 5.` | `X = 5` |
| `X == Y` | Identidad estricta | `?- X == 5.` | `false` |
| `X == Y` | (después de ligar) | `?- X = 5, X == 5.` | `true` |
| `X \= Y` | No unifica | `?- 1 \= 2.` | `true` |
| `X \== Y` | No idénticos | `?- X \== 5.` | `true` |

**Regla:** `=` transforma el mundo (liga variables). `==` solo inspecciona.

---

### [F-016] `=..` (univ): descomponer términos
`@tipo: codigo`

```prolog
?- padre(juan, maria) =.. L.
L = [padre, juan, maria].

?- T =.. [saludo, hola, mundo].
T = saludo(hola, mundo).

?- f(a, b, c) =.. [F | Args].
F = f, Args = [a, b, c].
```

**Usos:**
- Construir términos dinámicamente
- Inspeccionar la estructura de un término

---

### [F-017] El gotcha: occurs-check
`@tipo: concepto-mixto`

```prolog
?- X = f(X).
```

¿Qué devuelve?
- **Prolog ISO:** debería fallar (hay ciclo: X = f(f(f(…))))
- **SWI-Prolog por default:** `X = f(X).` ← ¡éxito! (crea término cíclico)

**Riesgo:** algoritmos que asumen no-ciclos pueden colgar.

---

### [F-018] Forzar occurs-check
`@tipo: codigo`

```prolog
?- unify_with_occurs_check(X, f(X)).
false.

% O activar globalmente:
?- set_prolog_flag(occurs_check, true).
true.

?- X = f(X).
false.
```

Decisión de diseño: **occurs-check cuesta tiempo**. Los implementadores lo desactivan para velocidad. El estudiante avanzado lo activa cuando desarrolla.

> 🧘 **Para la práctica: no te preocupes.**
> En el **99%** de los programas Prolog que vas a escribir este año, occurs-check **no es un problema**. SWI lo desactiva por defecto por una razón: es lentísimo y raramente importa. Lo veremos de nuevo solo si trabajás con estructuras que puedan generar ciclos. **Seguimos.**

---

### [F-019] Variable anónima `_`
`@tipo: codigo`

```prolog
?- madre(ana, _).      % "¿Ana es madre de alguien?" — sí/no
true.

?- padre(_, _).        % "¿Hay algún padre?"
true.
```

**Clave:** cada `_` es **distinto** de otros `_`:

```prolog
?- _ = _.               % dos variables anónimas distintas
true.                   % se unifican (ambas libres)
```

---

### [F-020] Aplicación: pattern matching
`@tipo: codigo`

```prolog
primerElemento([X|_], X).
tercerElemento([_,_,X|_], X).
esPar(par(_, _)).

?- primerElemento([1,2,3], E).
E = 1.

?- esPar(par(ana, beto)).
true.
```

**Prolog = pattern matching nativo** — equivalente a `match`/`case` de Haskell o Rust.

---

### [F-021] Profundidad infinita (trampa)
`@tipo: codigo`

```prolog
lista_rara([a | X]).

?- lista_rara([a | X]).
X = X.          % X permanece libre — es una lista "abierta"

?- X = [1,2,3 | X].   % ¡término cíclico sin occurs-check!
X = [1, 2, 3, 1, 2, 3, 1, 2, 3|...].
```

Esto suele ser un bug. Revisar el occurs-check o usar `write_canonical/1` para ver la estructura.

---

### [F-022] Ejercicio relámpago (30 s)
`@tipo: socratica`

¿Qué imprime cada consulta?

```prolog
?- X = 3, Y = 4, X + Y == 7.
?- X = 3, Y = 4, X + Y =:= 7.
?- f(a, Y) = f(X, b).
```

*(Respuestas en la siguiente filmina.)*

---

### [F-023] Respuestas
`@tipo: codigo`

```prolog
?- X = 3, Y = 4, X + Y == 7.
false.           % 3+4 es el término "+(3,4)", distinto del átomo 7

?- X = 3, Y = 4, X + Y =:= 7.
true.            % =:= evalúa aritméticamente

?- f(a, Y) = f(X, b).
X = a, Y = b.    % unificación estructural clásica
```

**Lección:** `==`, `=`, `=:=` son **tres operadores distintos**. No confundirlos.

---

## BLOQUE 2 — Listas (35 min) · [Ver BLOQUE 8 original → F-097 a F-112]

> ℹ️ **Nota de dictado:** En la clase real, las Listas fueron enseñadas ANTES que SLD/Backtracking (después de Unificación). El contenido de listas está en el BLOQUE 8 original de este archivo. Para la guía del alumno y el diseño actualizado, Listas es el Bloque 2.

---

## BLOQUE 3 — Resolución SLD (25 min) · F-024 a F-038

*(En el dictado real: Bloque 3 — después de Listas)*

---

### [F-024] ¿Qué es SLD?
`@tipo: concepto-abstracto`

**SLD = Selective Linear Definite clause resolution**

Algoritmo de inferencia que usa Prolog:
- **Selective**: hay una regla para elegir qué goal probar (el de más a la izquierda)
- **Linear**: cada paso consume un goal y produce una resolvente
- **Definite**: solo cláusulas definidas de Horn (una cabeza, cuerpo conjuntivo)

Resolución = *refutación* de la negación del objetivo.

---

### [F-025] Vocabulario
`@tipo: tabla`

| Término | Significado |
|---------|-------------|
| Goal | Objetivo a demostrar |
| Resolvente | Conjunción de goals pendientes |
| Cláusula | Hecho o regla del programa |
| Sustitución θ | Mapeo variable → término |
| Refutación | Demostración por contradicción |
| Prueba | Cadena de sustituciones que vacía la resolvente |

---

### [F-026] El algoritmo SLD (paso a paso)
`@tipo: codigo`

```text
PROGRAM P, GOAL G:
    resolvente := [G]
    sustituciones := {}
    mientras resolvente no vacía:
        elegir primer goal de resolvente: A
        elegir cláusula de P (top-down): H :- B₁,…,Bₙ
        si unify(A, H) con MGU θ:
            resolvente := (B₁,…,Bₙ, rest(resolvente)) θ
            sustituciones := sustituciones ∘ θ
        si no unifica ninguna → BACKTRACK
    retornar sustituciones
```

---

### [F-027] Ejemplo integrado
`@tipo: demo`

Base:
```prolog
madre(ana, carlos).
padre(carlos, laura).
progenitor(X,Y) :- madre(X,Y).
progenitor(X,Y) :- padre(X,Y).
abuelo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).
```

Consulta: `?- abuelo(ana, N).`

Vamos al pizarrón a trazar el árbol SLD completo.

---

### [F-028] Árbol SLD — nodo raíz
`@tipo: diagrama`

```
                 abuelo(ana, N)
                       |
              (regla abuelo con θ₁ = {X/ana, Z/N})
                       |
                       v
     progenitor(ana, Y), progenitor(Y, N)
```

---

### [F-029] Árbol SLD — expansión izquierda
`@tipo: diagrama`

```
     progenitor(ana, Y), progenitor(Y, N)
                       |
               ┌───────┴────────┐
    (regla 1)  |                |  (regla 2)
               v                v
        madre(ana,Y)        padre(ana,Y)
        , progenitor(Y,N)   , progenitor(Y,N)
```

---

### [F-030] Árbol SLD — rama exitosa
`@tipo: diagrama`

```
     madre(ana, Y), progenitor(Y, N)
                |
      (hecho madre(ana, carlos), θ = {Y/carlos})
                |
                v
        progenitor(carlos, N)
                |
          ┌─────┴──────┐
   madre(carlos,N)   padre(carlos,N)
          |               |
        falla      padre(carlos, laura) → {N/laura} ✓
```

Primera solución: **`N = laura`**.

---

### [F-031] Regla de selección
`@tipo: concepto-mixto`

Prolog siempre selecciona el **goal más a la izquierda** (leftmost).

Consecuencia: en

```prolog
abuelo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).
```

primero resuelve `progenitor(X,Y)`, después `progenitor(Y,Z)`.

¿Por qué importa?
- El orden cambia la eficiencia (no la corrección, en teoría)
- En la práctica, el mal orden puede caer en loops infinitos

---

### [F-032] Orden malo = loop infinito
`@tipo: codigo`

```prolog
% Versión MALA de ancestro:
ancestro(X, Y) :- ancestro(X, Z), progenitor(Z, Y).   % recursión primero
ancestro(X, Y) :- progenitor(X, Y).

?- ancestro(ana, laura).
% 🔥 BUCLE INFINITO 🔥
```

Prolog expande `ancestro(X,Z)` indefinidamente antes de tocar el caso base.

**Regla de oro:** en recursiones, **caso base primero**, o asegurar terminación con una condición de corte.

---

### [F-033] Estrategia de búsqueda: DFS
`@tipo: concepto-abstracto`

Prolog explora el árbol SLD en **profundidad** (*depth-first*) con backtracking cronológico.

Alternativas teóricas (no implementadas en Prolog estándar):
- BFS → garantiza solución si existe, pero costoso en memoria
- Iterative deepening → combina ambos

Algunas implementaciones (Ciao, Prolog con `tabling`) agregan memoización para evitar loops.

---

### [F-034] Regla de escritura
`@tipo: concepto-mixto`

La **regla de escritura** (computation rule) = qué cláusula probar.

Prolog usa **top-down**: de la primera cláusula hacia abajo.

Consecuencia: **el orden de las cláusulas importa** para:
- Eficiencia (poner caso común primero)
- Terminación (caso base antes del recursivo)
- Comportamiento del `!` (se ve en B4)

---

### [F-035] Prueba = demostración
`@tipo: concepto-abstracto`

Una **respuesta** de Prolog NO es "encontré un valor".

Es: **"He construido una demostración formal de que tu goal es verdadero, usando estas cláusulas y estas sustituciones."**

Eso lo hace único entre lenguajes: cada ejecución es un teorema demostrado.

> *"Logic program execution is theorem proving."* — Kowalski, 1974

---

### [F-036] Retorno con `;`
`@tipo: demo`

```prolog
?- progenitor(ana, Y).
Y = carlos ;      % primera demo
Y = beatriz ;     % segunda demo (backtrack)
false.            % no hay más
```

Cada `;` fuerza a Prolog a **rehacer la última elección** y buscar una demostración alternativa.

`.` → acepta la solución actual y detiene la búsqueda.

---

### [F-037] ¿Y si no hay ninguna demostración?
`@tipo: codigo`

```prolog
?- abuelo(tomas, X).
false.
```

Prolog **no dice "no existe"** — dice "no pude demostrarlo con esta base". Esta sutileza se desarrolla en B5 (negación por falla).

Es la famosa **Closed World Assumption**: lo que no está probado, no está en la base.

---

### [F-038] Resumen B2
`@tipo: concepto-mixto`

- SLD = algoritmo de resolución de Prolog
- Resolvente = conjunción de goals pendientes
- Regla de selección: leftmost
- Regla de escritura: top-down
- DFS con backtracking
- Una solución = una demostración formal
- El orden de cláusulas influye en terminación

---

## BLOQUE 4 — Backtracking (25 min) · F-039 a F-054

*(En el dictado real: Bloque 4 — después de SLD)*

---

### [F-039] ¿Qué es el backtracking?
`@tipo: concepto-abstracto`

Cuando una rama del árbol SLD **falla**, Prolog **retrocede** hasta el último **punto de elección** y prueba la siguiente alternativa.

Es **automático**: no lo programás, viene con el motor.

> *"Backtracking is the engine's memory of 'roads not taken'."*

---

### [F-040] Punto de elección
`@tipo: concepto-mixto`

Se crea un **punto de elección** (*choice point*) cuando:
1. Hay **más de una cláusula** que unifica con un goal, o
2. Un goal tiene múltiples respuestas (hechos con mismo funtor)

El motor lo apila en el **stack de elecciones** para poder volver si la rama falla.

Comparación: como un `try { } catch { ...try again... }` con backup completo del estado.

---

### [F-041] Ejemplo canónico
`@tipo: codigo`

```prolog
color(rojo).
color(verde).
color(azul).

?- color(X).
X = rojo ;       % 1er choice point
X = verde ;      % 2do choice point
X = azul.        % última opción, no deja choice point
false.           % ya no hay más
```

---

### [F-042] `fail`-driven loop
`@tipo: demo`

Patrón clásico Prolog para "iterar por todas las soluciones":

```prolog
?- color(X), write(X), nl, fail.
rojo
verde
azul
false.
```

El `fail` fuerza backtracking tras cada `write`. Así se imprimen **todas** las soluciones sin recolectarlas.

> En 2026 preferimos `forall/2` o `findall/3`, pero `fail` sigue siendo pedagógicamente útil.

---

### [F-043] Árbol de búsqueda con bifurcación
`@tipo: diagrama`

Base:
```prolog
bebida(agua).
bebida(vino).
comida(pasta).
comida(ensalada).

almuerzo(B, C) :- bebida(B), comida(C).
```

Consulta `?- almuerzo(B, C).`:

```
       almuerzo(B,C)
            |
   ┌────────┼─────────┐
  B=agua            B=vino
  |                    |
┌─┴─┐              ┌────┴────┐
C=pasta  C=ens.    C=pasta   C=ens.
```

**4 soluciones** — DFS las enumera en orden.

---

### [F-044] Restricción con `\=`
`@tipo: codigo`

```prolog
almuerzo_raro(B, C) :-
    bebida(B), comida(C),
    B \= C.     % solo se cumple si son distintos

?- almuerzo_raro(agua, X).
X = pasta ;
X = ensalada.
```

Cuando `B = C`, falla y backtrackea. Cuando son distintos, sigue.

---

### [F-045] Anatomía del stack de backtracking
`@tipo: concepto-mixto`

Prolog mantiene **dos stacks**:

1. **Stack de control** → llamadas/retornos (como cualquier lenguaje)
2. **Trail** → log de ligaduras de variables

Al fallar:
- El stack de control vuelve al último choice point
- El **trail deshace las ligaduras** hechas desde ese punto → las variables vuelven a estar libres

Esta *restauración destructiva* es lo que Hace Prolog "mágico".

---

### [F-046] Visualización: ligadura → falla → deshacer
`@tipo: diagrama`

```
paso 1: goal1 → liga X=5     ┐
paso 2: goal2 → liga Y=7     │ trail = [X,Y]
paso 3: goal3 → FALLA        │
                              ↓ backtrack al último choice
paso 4: deshacer Y,X         ← trail = []
paso 5: probar otra cláusula de goal1
```

Nada queda "pegado". Siempre empieza limpio.

---

### [F-047] Múltiples soluciones con reglas
`@tipo: demo`

```prolog
par(X,Y) :- color(X), color(Y), X \= Y.

?- par(rojo, Y).
Y = verde ;
Y = azul.

?- par(X, Y).
% 6 soluciones (3 × 2 posibles)
X = rojo, Y = verde ; X = rojo, Y = azul ;
X = verde, Y = rojo ; X = verde, Y = azul ;
X = azul, Y = rojo ; X = azul, Y = verde.
```

---

### [F-048] Eficiencia y backtracking
`@tipo: concepto-mixto`

Backtracking exhaustivo = **explosión combinatoria**.

Con 10 goals binarios independientes: 2¹⁰ = 1024 ramas.

**Estrategias:**
- Poner los goals más **restrictivos primero** (filtrar temprano)
- Ordenar cláusulas para que la probable primero
- Usar `!` (corte) para podar

> *"Programar bien en Prolog = diseñar el árbol de búsqueda."*

---

### [F-049] ¿Cuándo NO hace backtracking?
`@tipo: codigo`

```prolog
% Con una sola cláusula que unifica → no hay choice point
unico([X]) :- atom(X).

?- unico([hola]).
true.           % no deja "resto" de exploración
```

Menos choice points = ejecución más rápida. El compilador Prolog detecta "determinismo" y optimiza (WAM).

---

### [F-050] Árbol de backtracking — ejemplo no trivial
`@tipo: diagrama`

```prolog
amigo(ana, beto).    amigo(ana, carla).
amigo(beto, dario).  amigo(beto, elena).
amigo(carla, fran).

conoce(X, Y) :- amigo(X, Y).
conoce(X, Z) :- amigo(X, Y), conoce(Y, Z).
```

Consulta `?- conoce(ana, Q).` produce:
- beto, carla (amigos directos)
- dario, elena (amigos de beto)
- fran (amiga de carla)

Total: 5 respuestas. Trazar el árbol en vivo.

---

### [F-051] Infinito en backtracking
`@tipo: codigo`

```prolog
% Si hay ciclos en la base:
amigo(ana, beto).
amigo(beto, ana).       % ← ciclo

conoce(X, Z) :- amigo(X, Y), conoce(Y, Z).

?- conoce(ana, Q).
% Puede entrar en bucle infinito: ana→beto→ana→beto…
```

Prevención:
- Llevar lista de visitados (se ve en B9)
- Usar `tabling` (extensión SWI)

---

### [F-052] El costo oculto del backtracking
`@tipo: concepto-abstracto`

**Tiempo:** O(productos cartesianos × unificaciones)
**Espacio:** crece con el número de choice points vivos
**Memoria:** el trail puede ocupar MB en consultas pesadas

En producción:
- Índices en el primer argumento (automático en SWI)
- `nth_clause/3`, `jiti_list/1` para observar qué se indexa
- Reordenar para fallar temprano

---

### [F-053] Backtracking vs. streams
`@tipo: tabla-comparativa`

| | Backtracking Prolog | Generadores/Streams |
|---|---|---|
| Control | Automático | Explícito (`yield`) |
| Memoria | Trail | Frame de iterador |
| Reuso | Recomputación | Memoización posible |
| Paralelismo | No trivial | `async`/`await` |
| Ejemplo | `?- member(X, L).` | `for x in L` |

Son duales: un generador Python ≈ un predicado Prolog con múltiples respuestas.

---

### [F-054] Cheatsheet de backtracking
`@tipo: tabla`

| Truco | Sintaxis |
|-------|----------|
| Forzar siguiente solución | `;` en REPL |
| Parar en la primera | `once(Goal)` |
| Colectar todas | `findall(T, G, L)` |
| Ignorar fracaso | `catch(G, _, true)` |
| Backtrack forzado | `fail` |
| Sin backtracking | `!` (siguiente bloque) |

---

## BLOQUE 5 — Corte (!) (20 min) · F-055 a F-066

*(En el dictado real: Bloque 5 — incluye implementación de `not/1` como única mención de negación por falla)*

---

### [F-055] El operador `!`
`@tipo: concepto-abstracto`

`!` (*cut*) = compromiso irrevocable con la rama actual.

Efecto:
1. Quita los choice points **a la izquierda** del `!` en la cláusula actual
2. Quita el choice point de la propia cláusula (no se probarán más cláusulas del mismo predicado)

> *"Cut tells Prolog: I'm sure about this path. Don't look back."*

---

### [F-056] ¿Por qué cortar?
`@tipo: concepto-mixto`

Tres razones:

1. **Eficiencia**: evitar recomputación de ramas que sabemos que fallarían
2. **Determinismo**: garantizar que un predicado dé **una sola** respuesta
3. **Expresar "else"**: codificar alternativas exclusivas

Trade-off: **pierde declaratividad**. Un programa con `!` ya no es "puro".

---

### [F-057] `max/3` — caso canónico
`@tipo: codigo`

Sin corte (correcto pero con choice point de sobra):
```prolog
max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.
```

Con corte **verde**:
```prolog
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
```

Ambos devuelven el mismo resultado — el `!` solo elimina un choice point inútil.

---

### [F-058] Corte verde vs. rojo
`@tipo: tabla-comparativa`

| Tipo | Efecto | Si lo quito… |
|------|--------|--------------|
| **Verde** | Solo eficiencia | El programa sigue funcionando igual |
| **Rojo** | Cambia la lógica | El programa responde distinto o mal |

**Preferencia ética:** solo corte verde. El rojo es para cuando no hay alternativa.

---

### [F-059] Ejemplo de corte rojo
`@tipo: codigo`

```prolog
abs(X, X)  :- X >= 0, !.
abs(X, Y)  :- Y is -X.

?- abs(3, Z).
Z = 3.              % correcto

?- abs(-5, Z).
Z = 5.              % correcto
```

**Sin el `!`:**
```prolog
?- abs(3, Z).
Z = 3 ;             % correcto
Z = -3.             % ¡MAL! también se cumple "Y is -X"
```

El `!` es *esencial* aquí — sin él, la semántica rompe.

---

### [F-060] `if-then-else` explícito
`@tipo: codigo`

SWI-Prolog soporta sintaxis explícita:

```prolog
abs(X, Y) :-
    (   X >= 0
    ->  Y = X
    ;   Y is -X
    ).
```

Equivalente a la versión con `!`, pero más **legible** y más **local** (no afecta a otras cláusulas).

**Guía en 2026:** preferir `(-> ;)` sobre `!` siempre que se pueda.

---

### [F-061] Corte y backtracking: el efecto barrera
`@tipo: diagrama`

```
                cláusula(X) :- g1, g2, !, g3, g4.
                              |   |   |   |   |
                              v   v   v   v   v
backtrack antes del corte:    ✓   ✓   —   —   —
backtrack después del corte:  —   —   —   ✓   ✓
```

El `!` divide la cláusula en dos mitades. Después, no se puede volver a la izquierda.

---

### [F-062] Corte dentro de un `or`
`@tipo: codigo`

```prolog
p(X) :- q(X), !, r(X).
p(X) :- s(X).

?- p(a).
```

Si `q(a)` unifica, el `!` corta:
- NO probar más cláusulas de `q`
- NO probar la 2ª cláusula de `p`

Sólo si `q(a)` falla, se prueba `s(a)`.

---

### [F-063] Corte, `!` y negación
`@tipo: codigo`

Implementación clásica de negación por falla:

```prolog
not(P) :- call(P), !, fail.
not(_).
```

Lectura:
- Si `P` es demostrable → `!` y `fail` → `not(P)` falla
- Si `P` falla → se prueba segunda cláusula → `not(P)` es verdadero

Así se construye `\+/1` en sistemas mínimos.

---

### [F-064] Corte rojo: el contraejemplo ejecutable
`@tipo: codigo`

**Mismo predicado — con y sin corte. Cambia el resultado.**

```prolog
% CON cortes rojos
clasificar(X, positivo) :- X > 0, !.
clasificar(X, negativo) :- X < 0, !.
clasificar(_, cero).

?- clasificar(5, C).
C = positivo.                     % ← una sola respuesta ✓

% SIN cortes
clasificar(X, positivo) :- X > 0.
clasificar(X, negativo) :- X < 0.
clasificar(_, cero).

?- clasificar(5, C).
C = positivo ;
C = cero.                         % ← ¡dos! la segunda es errónea ✗
```

Los cortes eran **rojos**: filtraban resultados. Sin ellos, se rompe la semántica.

**Reescritura declarativa pura** (sin corte):

```prolog
clasificar(X, positivo) :- X > 0.
clasificar(X, negativo) :- X < 0.
clasificar(X, cero)     :- X =:= 0.
```

Ahora las condiciones son **mutuamente excluyentes** → no hace falta corte.

**Moraleja:** si usás corte rojo, preguntate si podés reformular con condiciones mutuamente excluyentes.

---

### [F-065] Reglas de uso responsable del corte
`@tipo: tabla`

| Regla | Justificación |
|-------|---------------|
| Preferir `(-> ;)` | Más local y legible |
| Sólo corte **verde** cuando se pueda | Preserva declaratividad |
| Documentar corte rojo con comentario | Debugging futuro |
| No usar `!` en predicados de librería | Puede romper invariantes |
| Probar sin `!` primero | Detectar falta de casos |

---

### [F-066] Resumen B4
`@tipo: concepto-mixto`

- `!` poda choice points a su izquierda y de la cláusula
- Corte verde = optimización; rojo = cambio semántico
- Preferir `(Cond -> Then ; Else)` cuando sea claro
- Regla mental: “si lo quito, ¿sigue siendo correcto?” → define si es verde o rojo

---

## ⚠️ NO DICTADO — Negación por falla · F-067 a F-075

> Este bloque **no fue dictado** en la clase del 2026-04-21. La negación por falla fue mencionada brevemente en el Bloque 5 (Corte) a través de la implementación de `not(P) :- call(P), !, fail.` pero no se desarrolló como bloque independiente.

---

### [F-067] `\+` y su semántica
`@tipo: concepto-abstracto`

`\+ Goal` = **"Goal no es demostrable con la base actual"**.

NO es lo mismo que "Goal es falso".

Esto se llama **Closed World Assumption** (CWA): asumimos que todo lo no demostrado es falso.

> Vivimos en un mundo cerrado dentro de la base. Afuera, Prolog no sabe nada.

---

### [F-068] Ejemplo inocuo
`@tipo: codigo`

```prolog
mamifero(perro).
mamifero(gato).
ave(paloma).

?- \+ ave(perro).
true.             % no hay hecho "ave(perro)"

?- \+ mamifero(perro).
false.            % "mamifero(perro)" sí se demuestra
```

---

### [F-069] La trampa del mundo abierto
`@tipo: concepto-mixto`

```prolog
casado(ana).
soltero(X) :- \+ casado(X).

?- soltero(juan).
true.             % ¡pero no sabemos si juan está casado!
```

**Problema:** Prolog no distingue "no está en la base" de "es falso".

En la vida real (bases incompletas), esto es peligroso.

---

### [F-070] `\+` con variables libres — la trampa
`@tipo: codigo`

```prolog
?- \+ X = 1.
false.             % ¿por qué? X=1 SÍ se puede demostrar

?- X = 2, \+ X = 1.
true.              % ahora X está ligado y X=1 falla

?- \+ X = 1, X = 2.
false.             % el primer goal ya falló
```

**Regla:** `\+` funciona confiablemente solo sobre goals **ground** (sin variables libres).

---

### [F-071] `\+` no liga variables
`@tipo: concepto-abstracto`

Como `\+` prueba por **fracaso**, si tiene éxito no hay sustitución para recordar — las variables dentro **no quedan ligadas**.

```prolog
?- \+ (padre(juan, X)).
```

- Si falla `padre(juan, X)` para todo X → `\+` es verdadero
- Pero `X` queda libre (no hay instancia)

---

### [F-072] `\+` vs. `not/1`
`@tipo: tabla-comparativa`

| Operador | Origen | Estándar |
|----------|--------|----------|
| `\+` | ISO Prolog | ✓ preferido |
| `not/1` | Edinburgh Prolog (legado) | Deprecado |

Son semánticamente iguales. Usar `\+` por compatibilidad ISO.

---

### [F-073] Negación correcta: `dif/2`
`@tipo: codigo`

SWI-Prolog y muchas implementaciones tienen:

```prolog
?- dif(X, Y), X = 1, Y = 2.
X = 1, Y = 2.

?- dif(X, Y), X = 1, Y = 1.
false.
```

`dif/2` **se pospone** hasta que las variables se liguen. Es la negación correcta en Prolog con restricciones (CLP).

---

### [F-074] Ejemplo combinado
`@tipo: codigo`

```prolog
animal(perro).
animal(gato).
animal(salmon).
acuatico(salmon).

terrestre(X) :- animal(X), \+ acuatico(X).

?- terrestre(Y).
Y = perro ;
Y = gato.
```

Lectura: "Un animal es terrestre si no es acuático."

---

### [F-075] Resumen B5
`@tipo: concepto-mixto`

- `\+` = falla demostrativa, no negación lógica
- Closed World Assumption: "lo no demostrado no se asume cierto"
- Usar `\+` solo con goals **ground**
- Para variables, preferir `dif/2`
- No confundir fracaso con falsedad

---

## ⚠️ NO DICTADO — Ejercicio colaborativo · F-076 a F-083

> Este bloque **no fue dictado** en la clase del 2026-04-21.

---

### [F-076] ☕ Descanso 10 min
`@tipo: portada`

**Pausa**

- Estiramos piernas
- Consultas libres
- Café y mate

Volvemos en 10 minutos con trabajo en pares.

---

### [F-077] Ejercicio colaborativo — reglas
`@tipo: socratica`

- **Trabajo en pares** (5 min por ejercicio + 5 min puesta en común)
- Cada par presenta **1** resultado
- Si se traban → levantar la mano, no Google todavía
- Prolog a mano en papel: trazar, no correr

---

### [F-078] Ejercicio 1 — Viajes compartidos
`@tipo: codigo`

Base:
```prolog
viaja(ana, parana).
viaja(ana, rosario).
viaja(beto, rosario).
viaja(carla, parana).

comparten_destino(X, Y) :-
    viaja(X, D), viaja(Y, D), X \= Y.
```

**Tracear `?- comparten_destino(ana, Q).`**
¿Cuántas soluciones? ¿En qué orden aparecen?

---

### [F-079] Ejercicio 1 — solución
`@tipo: codigo`

```prolog
?- comparten_destino(ana, Q).
Q = carla ;       % ambas viajan a parana
Q = beto  ;       % ambas viajan a rosario
false.
```

Trazado:
1. `viaja(ana, parana)` → D=parana → `viaja(Q, parana)` → Q=carla (no ana, por `\=`)
2. `viaja(ana, rosario)` → D=rosario → `viaja(Q, rosario)` → Q=beto

---

### [F-080] Ejercicio 2 — Orden de `\+`
`@tipo: concepto-mixto`

Explicar la diferencia:

```prolog
?- \+ X = 1, X = 2.
?- X = 2, \+ X = 1.
```

¿Cuál tiene éxito? ¿Por qué?

Pista: rastrear el estado de `X` goal por goal.

---

### [F-081] Ejercicio 2 — respuesta
`@tipo: codigo`

```prolog
?- \+ X = 1, X = 2.
false.
% X inicialmente libre. \+ X=1 prueba "X=1": ¡éxito!, \+ falla.

?- X = 2, \+ X = 1.
true.
% X se liga a 2. \+ X=1 prueba "2=1": falla, \+ succeeds.
```

**Lección:** el orden cambia la respuesta porque `\+` depende del estado de las variables.

---

### [F-082] Ejercicio 3 — signo
`@tipo: codigo`

Reescribir con `!` y con `(-> ;)`:

```prolog
signo(X, positivo) :- X > 0.
signo(0, cero).
signo(X, negativo) :- X < 0.
```

¿Cuál es más legible? ¿Cuál es más eficiente?

---

### [F-083] Ejercicio 3 — soluciones
`@tipo: codigo`

Con `!`:
```prolog
signo(X, cero)      :- X =:= 0, !.
signo(X, positivo)  :- X > 0, !.
signo(_, negativo).
```

Con `(-> ;)`:
```prolog
signo(X, S) :-
    (   X =:= 0 -> S = cero
    ;   X >   0 -> S = positivo
    ;               S = negativo
    ).
```

**Puesta en común:** preferencia en 2026 → `(-> ;)` por legibilidad.

---

## ⚠️ NO DICTADO — Aritmética · F-084 a F-096

> Este bloque **no fue dictado** en la clase del 2026-04-21. Solo se mencionó `is/2` vs. `=` en el ejercicio relámpago de Unificación (F-022/F-023).

---

### [F-084] ¡Momento incómodo!
`@tipo: codigo`

```prolog
?- X = 2 + 3.
X = 2+3.          % NO es 5

?- X is 2 + 3.
X = 5.            % ahora sí
```

Prolog **no evalúa expresiones** por defecto. Las trata como **términos**.

`2 + 3` es `+(2, 3)` — un árbol con funtor `+` y dos hijos.

---

### [F-085] `is/2` — evaluación forzada
`@tipo: concepto-abstracto`

`X is Expresión` =
1. Evalúa `Expresión` aritméticamente
2. Unifica el resultado con `X`

Requisitos:
- `Expresión` debe ser **ground**
- `X` debe ser variable libre o número ya unificable

---

### [F-086] Errores comunes con `is/2`
`@tipo: codigo`

```prolog
?- X is Y + 1.
ERROR: Arguments are not sufficiently instantiated
          % Y está libre — no se puede evaluar

?- 5 is 2 + X.
ERROR: same
          % is/2 NO despeja; no es ecuación

?- X = 5, X is 2 + 3.
true.      % X ya vale 5, 5 is 5 ✓

?- X is 2 + 3, X = 6.
false.     % X queda en 5, no unifica con 6
```

**is/2 NO es `=` matemático.** Es unidireccional.

---

### [F-087] Operadores aritméticos
`@tipo: tabla`

| Operador | Significado |
|----------|-------------|
| `+ - * /` | Suma, resta, mult, división (float) |
| `//` | División entera |
| `mod` | Resto |
| `**` o `^` | Potencia |
| `abs(X)` | Valor absoluto |
| `sqrt(X)` | Raíz cuadrada |
| `sin/cos/tan` | Trig |
| `min(X,Y) max(X,Y)` | Min/max |

Evaluados por `is/2`, `=:=`, `<`, `>`, `=<`, `>=`.

---

### [F-088] Comparadores aritméticos
`@tipo: tabla-comparativa`

| Operador | Evalúa lado izq. | Evalúa lado der. | Tipo |
|----------|------------------|------------------|------|
| `=:=` | ✓ | ✓ | Igualdad numérica |
| `=\=` | ✓ | ✓ | Distinto numérico |
| `<  >  =<  >=` | ✓ | ✓ | Comparación |
| `=` | ✗ (unifica) | ✗ (unifica) | Unificación estructural |
| `==` | ✗ | ✗ | Identidad estructural |

**Trampa favorita del examen:** `=<` — no `<=`.

---

### [F-089] Demos relámpago
`@tipo: codigo`

```prolog
?- 2 + 3 =:= 5.          true.
?- 2 + 3 == 5.           false.     % árbol +(2,3) ≠ 5
?- 2 + 3 = 5.            false.     % intenta unificar +(2,3) con 5 → falla
?- X = 2 + 3, X =:= 5.   X = 2+3.    % true
?- X is 10 / 3.          X = 3.333…  % float
?- X is 10 // 3.         X = 3.      % entero
?- X is 10 mod 3.        X = 1.
```

---

### [F-090] Factorial recursivo
`@tipo: codigo`

```prolog
factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

?- factorial(5, F).
F = 120.
```

**Observar:**
- `N1 is N - 1` antes de la recursiva (ground necesario)
- `F is N * F1` después, cuando `F1` ya está ligado

---

### [F-091] Anti-patrón: no evaluar
`@tipo: codigo`

```prolog
% MAL
factorial(N, N * factorial(N - 1)).

?- factorial(5, F).
F = 5 * factorial(5-1).       % queda el árbol, no evalúa
```

**Diagnóstico:** faltó `is/2`. Prolog no es Haskell — no evalúa por estructura.

---

### [F-092] Fibonacci
`@tipo: codigo`

```prolog
fib(0, 0).
fib(1, 1).
fib(N, F) :-
    N > 1,
    N1 is N - 1, N2 is N - 2,
    fib(N1, F1), fib(N2, F2),
    F is F1 + F2.

?- fib(10, F).
F = 55.
```

Ejecución exponencial sin memoización (2ⁿ).

---

### [F-093] Versión con acumulador (lineal)
`@tipo: codigo`

```prolog
fib(N, F) :- fib_aux(N, 0, 1, F).

fib_aux(0, A, _, A).
fib_aux(N, A, B, F) :-
    N > 0,
    N1 is N - 1,
    S is A + B,
    fib_aux(N1, B, S, F).

?- fib(50, F).
F = 12586269025.
```

Técnica que reaparece en B9 con listas.

---

### [F-094] `succ/2` como alternativa
`@tipo: codigo`

```prolog
?- succ(4, X).
X = 5.

?- succ(Y, 5).
Y = 4.           % reversible

?- succ(X, 0).
false.           % no hay natural antes del 0
```

`succ/2` es una **relación reversible** entre sucesor y predecesor de naturales. Funciona bidireccional — `is/2` no.

---

### [F-095] CLP(FD): aritmética reversible
`@tipo: codigo`

Para aritmética *declarativa* y reversible, SWI tiene `library(clpfd)`:

```prolog
:- use_module(library(clpfd)).

?- X #= 5 - 3.
X = 2.

?- X #= Y + 3, Y = 4.
Y = 4, X = 7.

?- X in 1..10, Y in 1..10, X + Y #= 11.
X in 1..10, Y in 1..10, X+Y#=11.    % restricción pendiente
```

**CLP(FD)** resuelve ecuaciones, no sólo evalúa. Base de puzzles modernos.

---

### [F-096] Resumen B7
`@tipo: concepto-mixto`

- `is/2` evalúa aritmética, requiere lado derecho **ground**
- `=` ≠ `==` ≠ `=:=`
- División entera: `//`, resto: `mod`
- Evitar el anti-patrón “dejar el árbol sin evaluar”
- Para aritmética relacional: `succ/2`, `clpfd`

---

## BLOQUE 2 (original: 8) — Listas (35 min) · F-097 a F-112

*(Dictado como Bloque 2, inmediatamente después de Unificación)*

---

### [F-097] La estructura más importante
`@tipo: concepto-abstracto`

**Listas** = el tipo de dato estrella de Prolog.

Representan:
- Sentencias (cadenas de tokens)
- Soluciones múltiples (colecciones)
- Árboles (listas anidadas)
- Restricciones (conjuntos simbólicos)

Prolog sin listas es como Python sin `list`.

---

### [F-098] Notación
`@tipo: tabla`

| Sintaxis | Significado |
|----------|-------------|
| `[]` | Lista vacía |
| `[a]` | Un elemento |
| `[a, b, c]` | Tres elementos |
| `[H \| T]` | Cabeza `H`, cola `T` |
| `[A, B \| T]` | Dos primeros + resto |
| `[a, b, c \| T]` | Tres primeros + resto |

---

### [F-099] La estructura interna
`@tipo: diagrama`

`[1, 2, 3]` es azúcar sintáctico de:

```
'.'(1, '.'(2, '.'(3, [])))
```

O equivalente: `[1 | [2 | [3 | []]]]`.

Es una lista ligada (cons list) — como en Lisp, Haskell.

**Consecuencia:**
- Acceso a la cabeza: O(1)
- Acceso al n-ésimo: O(n)
- Append: O(n)

---

### [F-100] Pattern matching con listas
`@tipo: codigo`

```prolog
primero([X|_], X).
segundo([_, X|_], X).
ultimos_dos([_|T], A, B) :- T = [A, B].

?- primero([a,b,c], P).        P = a.
?- segundo([a,b,c], S).        S = b.
?- ultimos_dos([a,b,c], A, B). A = b, B = c.
```

---

### [F-101] Lista vacía vs. no vacía
`@tipo: codigo`

```prolog
esVacia([]).
noEsVacia([_|_]).

?- esVacia([]).          true.
?- esVacia([a]).         false.
?- noEsVacia([a]).       true.
?- noEsVacia([]).        false.
```

Patrón base de cualquier recursión sobre listas.

---

### [F-102] `length/2`
`@tipo: codigo`

```prolog
length([], 0).
length([_|T], N) :-
    length(T, N1),
    N is N1 + 1.

?- length([a,b,c,d], N).
N = 4.
```

Built-in en SWI, pero implementarla ayuda a entender la estructura.

---

### [F-103] `member/2`
`@tipo: codigo`

```prolog
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

?- member(2, [1,2,3]).
true.

?- member(X, [1,2,3]).
X = 1 ;
X = 2 ;
X = 3.
```

**Multi-modo:** funciona tanto como *test* (elemento dado) como *generador*.

---

### [F-104] `append/3` — la joya
`@tipo: codigo`

```prolog
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).

?- append([1,2], [3,4], R).
R = [1,2,3,4].

?- append(A, B, [1,2,3]).
A = [], B = [1,2,3] ;
A = [1], B = [2,3] ;
A = [1,2], B = [3] ;
A = [1,2,3], B = [].
```

**Reversibilidad total:** concatena, divide, enumera prefijos.

---

### [F-105] `append` como generador
`@tipo: codigo`

```prolog
% ¿Los últimos 2 elementos?
?- append(_, [X, Y], [a, b, c, d]).
X = c, Y = d.

% ¿Es sublista?
subsecuencia(Sub, L) :-
    append(_, R, L),
    append(Sub, _, R).

?- subsecuencia([b,c], [a,b,c,d]).
true.
```

Una sola definición → decenas de usos. Esto es lo que hace Prolog seductor.

---

### [F-106] `last/2` y `nth0/3`
`@tipo: codigo`

```prolog
last([X], X).
last([_|T], X) :- last(T, X).

?- last([a,b,c], L).
L = c.

?- nth0(0, [a,b,c], X).
X = a.                 % index 0-based

?- nth1(2, [a,b,c], X).
X = b.                 % index 1-based
```

---

### [F-107] `msort/2` y `sort/2`
`@tipo: codigo`

```prolog
?- msort([3,1,2,1,3], L).
L = [1,1,2,3,3].          % mergesort, conserva duplicados

?- sort([3,1,2,1,3], L).
L = [1,2,3].              % sin duplicados, ordenado

?- sort(0, @>, [3,1,2], L).
L = [3,2,1].              % descendente
```

Más útiles de lo que parecen — sirven para “conjuntos” pragmáticos.

---

### [F-108] Mapas / listas de pares
`@tipo: codigo`

```prolog
edades([ana-22, beto-30, carla-22, dario-45]).

?- edades(L), member(ana-E, L).
E = 22.
```

El operador `-/2` es el `Pair` de Prolog. No tiene semántica propia — es solo un término con buen aspecto.

**Uso extendido:** `keysort/2` ordena listas de pares por clave.

---

### [F-109] Listas anidadas
`@tipo: codigo`

```prolog
matriz([[1,2,3],
        [4,5,6],
        [7,8,9]]).

fila(N, M, F) :- nth0(N, M, F).

?- matriz(M), fila(1, M, F).
F = [4, 5, 6].
```

Las listas anidadas se recorren con recursión doble.

---

### [F-110] `forall/2` y `between/3`
`@tipo: codigo`

```prolog
?- between(1, 5, X), write(X), nl, fail.
1
2
3
4
5
false.

?- forall(between(1,5,X), X > 0).
true.

?- forall(between(1,5,X), X > 3).
false.
```

`forall/2` = "para todo X tal que P, Q se cumple". Alternativa limpia a `fail`-driven loop.

---

### [F-111] Construyendo listas
`@tipo: codigo`

```prolog
% Lista de los primeros N naturales
rango(1, [1]).
rango(N, L) :-
    N > 1,
    N1 is N - 1,
    rango(N1, L1),
    append(L1, [N], L).

?- rango(5, L).
L = [1,2,3,4,5].
```

Ineficiente por el `append`. Versión lineal se ve en B9.

---

### [F-112] Resumen B8
`@tipo: concepto-mixto`

- `[]` y `[H|T]` son las dos formas canónicas
- `member/2`, `append/3`, `length/2`, `last/2`, `sort/2`
- `append/3` es reversible y versátil
- Las listas anidadas representan estructuras complejas
- `between/3` + `forall/2` sustituyen los `fail`-loops imperativos

---

## ⚠️ NO DICTADO — Recursión avanzada · F-113 a F-126

> Este bloque **no fue dictado** en la clase del 2026-04-21. Recursión con acumulador, LCO y `reverse/2` no fueron cubiertos.

---

### [F-113] Patrón de recursión básico
`@tipo: codigo`

Toda recursión sobre listas tiene la forma:

```prolog
predicado([]) :- CASO_BASE.
predicado([H|T]) :- CASO_RECURSIVO(H, T).
```

La clave:
1. Definir **qué hago con la lista vacía**
2. Definir **qué hago con la cabeza** y **recurro sobre la cola**

---

### [F-114] Recursión simple — `suma_lista/2`
`@tipo: codigo`

```prolog
suma([], 0).
suma([H|T], S) :-
    suma(T, ST),
    S is H + ST.

?- suma([1,2,3,4], S).
S = 10.
```

**Orden de evaluación:**
1. Baja hasta `suma([], 0)` → ST=0
2. Vuelve sumando: 4+0=4, 3+4=7, 2+7=9, 1+9=10

---

### [F-115] Problema de stack
`@tipo: diagrama`

```
suma([1,2,3,4], S)
  suma([2,3,4], S1), S is 1 + S1
    suma([3,4], S2), S1 is 2 + S2
      suma([4], S3), S2 is 3 + S3
        suma([], S4), S3 is 4 + S4
```

Con listas largas → **stack overflow**. Necesitamos **acumulador**.

---

### [F-116] Recursión con acumulador — `suma`
`@tipo: codigo`

```prolog
suma(L, S) :- suma(L, 0, S).

suma([], Acc, Acc).
suma([H|T], Acc, S) :-
    Acc1 is Acc + H,
    suma(T, Acc1, S).

?- suma([1,2,3,4], S).
S = 10.
```

Ahora la operación final está **antes** de la llamada recursiva → **last-call optimization**.

---

### [F-117] Last-Call Optimization (LCO)
`@tipo: concepto-abstracto`

Cuando la **última** llamada de una cláusula es recursiva Y no hay choice points pendientes, el motor reutiliza el stack frame.

Efecto:
- Recursión con acumulador = **memoria constante**
- Equivalente a un `while` imperativo

Todos los Prologs modernos lo implementan. Es la razón por la que "recursión Prolog" no es más lenta que un loop.

---

### [F-118] Reverse ingenuo vs. con acumulador
`@tipo: codigo`

Ingenuo O(n²):
```prolog
reverse([], []).
reverse([H|T], R) :-
    reverse(T, RT),
    append(RT, [H], R).
```

Acumulador O(n):
```prolog
reverse(L, R) :- rev(L, [], R).
rev([], Acc, Acc).
rev([H|T], Acc, R) :- rev(T, [H|Acc], R).

?- reverse([1,2,3], R).
R = [3,2,1].
```

**Trazado mental:** `[1,2,3],[]` → `[2,3],[1]` → `[3],[2,1]` → `[],[3,2,1]` → `[3,2,1]`.

---

### [F-119] Mapeo — `doble/2`
`@tipo: codigo`

```prolog
doble([], []).
doble([H|T], [H2|T2]) :-
    H2 is H * 2,
    doble(T, T2).

?- doble([1,2,3], D).
D = [2,4,6].
```

Patrón `map` de programación funcional, expresado directamente en Prolog.

---

### [F-120] Filtrado — `soloPares/2`
`@tipo: codigo`

```prolog
soloPares([], []).
soloPares([H|T], [H|R]) :-
    H mod 2 =:= 0, !,
    soloPares(T, R).
soloPares([_|T], R) :-
    soloPares(T, R).

?- soloPares([1,2,3,4,5,6], P).
P = [2,4,6].
```

Nota el `!` verde: evita probar la segunda cláusula si ya entró por la primera.

---

### [F-121] `maplist/2` y `maplist/3`
`@tipo: codigo`

Primitivas de orden superior built-in:

```prolog
esPositivo(X) :- X > 0.
duplicar(X, Y) :- Y is X * 2.

?- maplist(esPositivo, [1,2,3]).
true.

?- maplist(duplicar, [1,2,3], D).
D = [2,4,6].
```

Prolog tiene HOF (*higher order functions*) de verdad — aunque en estilo más formal.

---

### [F-122] `foldl/4` y `foldl/5`
`@tipo: codigo`

```prolog
sumar(X, Acc, Sum) :- Sum is Acc + X.

?- foldl(sumar, [1,2,3,4], 0, S).
S = 10.
```

Equivalente funcional:
- Haskell: `foldl (+) 0 [1,2,3,4]`
- TypeScript: `[1,2,3,4].reduce((a,x) => a+x, 0)`

---

### [F-123] Evitar ciclos con visitados
`@tipo: codigo`

```prolog
% Grafo con posibles ciclos
arco(a, b). arco(b, c). arco(c, a).   % ciclo

camino(A, B, [A,B]) :- arco(A, B).
camino(A, B, [A|Rest]) :-
    arco(A, C),
    camino(C, B, Rest).

?- camino(a, c, P).
% ¡loop infinito si hay ciclo!
```

Solución: llevar **lista de visitados**:
```prolog
camino(A, B, V, [A,B]) :- arco(A, B), \+ member(B, V).
camino(A, B, V, [A|R]) :- arco(A, C), \+ member(C, V),
                           camino(C, B, [A|V], R).

?- camino(a, c, [], P).
P = [a, b, c].
```

---

### [F-124] Recursión de árboles
`@tipo: codigo`

```prolog
% Representación: arbol(Valor, Izq, Der) o hoja
arbol(1, arbol(2, hoja, hoja), arbol(3, hoja, arbol(4, hoja, hoja))).

suma_arbol(hoja, 0).
suma_arbol(arbol(V, I, D), S) :-
    suma_arbol(I, SI),
    suma_arbol(D, SD),
    S is V + SI + SD.
```

Recursión estructural directa — el matching hace el trabajo.

---

### [F-125] Debugging recursión
`@tipo: codigo`

```prolog
?- trace, suma([1,2,3], S).
   Call: suma([1,2,3], _)
   Call: suma([2,3], _)
   Call: suma([3], _)
   Call: suma([], _)
   Exit: suma([], 0)
   Exit: suma([3], 3)
   Exit: suma([2,3], 5)
   Exit: suma([1,2,3], 6)
```

Comandos:
- `trace` / `notrace`
- `spy/1` — poner spy point en un predicado
- `leash/1` — controlar qué puertos paran

---

### [F-126] Resumen B9
`@tipo: concepto-mixto`

- Patrón: caso base `[]` + caso recursivo `[H|T]`
- Acumulador → LCO → recursión en memoria constante
- `maplist/foldl` = `map/reduce` nativo
- Para grafos con ciclos: lista de visitados
- `trace` es tu mejor amigo al depurar

---

## ⚠️ NO DICTADO — Meta-predicados · F-127 a F-136

> Este bloque **no fue dictado** en la clase del 2026-04-21. `findall/3`, `bagof/3` y `setof/3` no fueron cubiertos.

---

### [F-127] ¿Qué es un meta-predicado?
`@tipo: concepto-abstracto`

**Meta-predicado** = predicado que toma otros predicados como argumentos.

Ejemplos: `findall/3`, `bagof/3`, `setof/3`, `forall/2`, `call/N`, `maplist/2-4`, `foldl/4-6`.

Son el mecanismo de Prolog para hacer **orden superior**.

---

### [F-128] `findall/3` — el workhorse
`@tipo: codigo`

```prolog
findall(+Template, +Goal, -Result).
```

Colecta TODAS las instancias de `Template` para las que `Goal` es verdadero.

```prolog
edad(ana, 22). edad(beto, 30). edad(carla, 22).

?- findall(N, edad(N, 22), L).
L = [ana, carla].

?- findall(N-E, edad(N, E), L).
L = [ana-22, beto-30, carla-22].
```

Si no hay soluciones → `L = []`.

---

### [F-129] `bagof/3`
`@tipo: codigo`

```prolog
?- bagof(N, edad(N, 22), L).
L = [ana, carla].

?- bagof(N, edad(N, 99), L).
false.                     % ¡falla si no hay soluciones!
```

Diferencia clave con `findall`: **falla** si la bolsa queda vacía.

---

### [F-130] `setof/3` y comparación final
`@tipo: concepto-mixto`

```prolog
?- setof(N, E^edad(N, E), L).
L = [ana, beto, carla].     % ordenado, sin duplicados
```

- `E^` = "cuantificación existencial" — "algún E cualquiera"
- Sin `E^`, `bagof/setof` agrupan por cada valor de las variables libres

**Los 3 lado a lado — misma consulta.** Base: `color(rojo). color(verde). color(rojo).`

| Operador | Consulta | Resultado | Si no hay soluciones |
|----------|----------|-----------|----------------------|
| `findall/3` | `findall(C, color(C), L)` | `[rojo, verde, rojo]` | `L = []` (éxito) |
| `bagof/3`   | `bagof(C, color(C), L)`   | `[rojo, verde, rojo]` | **falla** |
| `setof/3`   | `setof(C, color(C), L)`   | `[rojo, verde]` | **falla** |

**Regla mental de bolsillo:**
- *"dame lo que haya, aunque sea nada"* → **`findall`**
- *"si hay algo, agrupado"* → **`bagof`**
- *"ordenado y sin duplicados"* → **`setof`**

---

### [F-131] Agrupar con `bagof` + variable libre
`@tipo: codigo`

```prolog
curso(ana, prolog).
curso(beto, prolog).
curso(ana, lisp).
curso(carla, haskell).

?- bagof(Est, curso(Est, Lenguaje), Estudiantes).
Lenguaje = haskell, Estudiantes = [carla] ;
Lenguaje = lisp,    Estudiantes = [ana] ;
Lenguaje = prolog,  Estudiantes = [ana, beto].
```

Devuelve una bolsa **por cada valor de la variable libre** `Lenguaje`.

---

### [F-132] Comparación findall / bagof / setof
`@tipo: tabla-comparativa`

| Aspecto | `findall/3` | `bagof/3` | `setof/3` |
|---------|:---:|:---:|:---:|
| Sin soluciones | `[]` | falla | falla |
| Duplicados | sí | sí | no |
| Orden | preserva | preserva | ordenado |
| Agrupa por vars libres | no | sí | sí |
| `^` para cuantificar | — | sí | sí |

**Regla práctica:** usar `findall` salvo que necesites agrupación o unicidad.

---

### [F-133] `call/N` — invocación dinámica
`@tipo: codigo`

```prolog
?- call(write, hola).
hola

?- P = write, call(P, mundo).
mundo

?- maplist(write, [a,b,c]).
abc
```

`call/N` permite invocar predicados cuyo nombre solo se conoce en runtime — el mecanismo de HOF.

---

### [F-134] Ejemplo integrador: promedio de edades
`@tipo: codigo`

```prolog
promedio_edad(Prom) :-
    findall(E, edad(_, E), L),
    length(L, N),
    sum_list(L, S),
    Prom is S / N.

?- promedio_edad(P).
P = 24.666...
```

Combina:
- `findall/3` → colectar
- `length/2` → contar
- `sum_list/2` → sumar
- `is/2` → calcular

---

### [F-135] `aggregate_all/3` (SWI)
`@tipo: codigo`

```prolog
?- aggregate_all(count, edad(_, _), N).
N = 3.

?- aggregate_all(sum(E), edad(_, E), S).
S = 74.

?- aggregate_all(bag(N), edad(N, _), L).
L = [ana, beto, carla].
```

Wrapper limpio sobre `findall` + aritmética. Menos plumbing.

---

### [F-136] Resumen B10
`@tipo: concepto-mixto`

- `findall/3` → colecta todas las soluciones (lista vacía si ninguna)
- `bagof/3` → como findall pero falla en vacío + agrupa
- `setof/3` → ordenado, sin duplicados
- `call/N` → invocación dinámica, base de HOF
- `aggregate_all/3` → agregaciones SQL-style

---

## ⚠️ NO DICTADO — Aplicaciones · F-137 a F-149

> Este bloque **no fue dictado** en la clase del 2026-04-21. Mapa de colores, N-reinas y base deductiva de grafos no fueron cubiertos.

---

### [F-137] El valor de Prolog como modelador
`@tipo: concepto-abstracto`

Prolog es ideal cuando:
- Modelas **relaciones**, no transformaciones
- Necesitas **búsqueda exhaustiva** con backtracking
- El problema es **declarativo** (restricciones)
- Querés **una sola base** para múltiples consultas

---

### [F-138] Aplicación 1: Coloreo de mapas
`@tipo: codigo`

```prolog
color(rojo). color(verde). color(azul). color(amarillo).
distinto(A, B) :- A \= B.

mapa_argentino(Norte, Centro, Sur, Costa) :-
    color(Norte), color(Centro), color(Sur), color(Costa),
    distinto(Norte, Centro),
    distinto(Centro, Sur),
    distinto(Costa, Norte),
    distinto(Costa, Centro),
    distinto(Costa, Sur).

?- mapa_argentino(N, C, S, Co).
```

*Generate and test*: genera posibilidades, testea restricciones.

---

### [F-139] Aplicación 2: Sudoku en 4 líneas
`@tipo: codigo`

```prolog
:- use_module(library(clpfd)).

sudoku(Rows) :-
    length(Rows, 9), maplist(same_length(Rows), Rows),
    append(Rows, Vars), Vars ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Columns), maplist(all_distinct, Columns),
    % ... restricciones de cajas 3x3 ...
    maplist(label, Rows).
```

**Impresionante:** 4 líneas reales de lógica declarativa vs. cientos en Java.

---

### [F-140] Aplicación 3: Base deductiva de vuelos
`@tipo: codigo`

```prolog
vuelo(ush, bue, 2200).
vuelo(bue, mvd, 150).
vuelo(mvd, spo, 1500).
vuelo(bue, spo, 1650).

ruta(A, B, [A,B], T) :- vuelo(A, B, T).
ruta(A, B, [A|R], T) :-
    vuelo(A, C, T1),
    ruta(C, B, R, T2),
    T is T1 + T2.

?- ruta(ush, spo, Camino, T).
Camino = [ush, bue, spo],      T = 3850 ;
Camino = [ush, bue, mvd, spo], T = 3850.
```

---

### [F-141] La misma base, varias consultas
`@tipo: codigo`

```prolog
% ¿Hay vuelo directo?
?- vuelo(ush, bue, _).
true.

% ¿Cuánto dura la ruta más corta?
?- findall(T, ruta(ush, spo, _, T), Ts),
   min_list(Ts, Min).
Min = 3850.

% ¿Cuántas escalas mínimas?
?- findall(C, ruta(ush, spo, C, _), Cs),
   maplist(length, Cs, Ns),
   min_list(Ns, MinLen),
   Escalas is MinLen - 2.
Escalas = 1.
```

Una base → infinitas consultas. **Ese** es el superpoder de Prolog.

---

### [F-142] Aplicación 4: N-reinas (planteo)
`@tipo: codigo`

```prolog
:- use_module(library(clpfd)).

n_reinas(N, Qs) :-
    length(Qs, N),
    Qs ins 1..N,
    all_distinct(Qs),
    diagonales_distintas(Qs),
    label(Qs).

diagonales_distintas([]).
diagonales_distintas([Q|Qs]) :-
    no_ataca(Q, Qs, 1),
    diagonales_distintas(Qs).

no_ataca(_, [], _).
no_ataca(Q, [Q1|Qs], D) :-
    Q #\= Q1 + D, Q #\= Q1 - D,
    D1 #= D + 1, no_ataca(Q, Qs, D1).

?- n_reinas(8, Qs).
Qs = [1, 5, 8, 6, 3, 7, 2, 4] ; …
```

---

### [F-143] Aplicación 5: Parser con DCG
`@tipo: codigo`

```prolog
oracion --> sujeto, verbo, complemento.
sujeto --> [el], sustantivo.
sustantivo --> [gato] ; [perro] ; [estudiante].
verbo --> [come] ; [estudia].
complemento --> [prolog] ; [pescado].

?- phrase(oracion, [el, gato, come, pescado]).
true.

?- phrase(oracion, Frase).
Frase = [el, gato, come, prolog] ;
Frase = [el, gato, come, pescado] ;
…
```

DCG (*Definite Clause Grammars*) = sintaxis limpia para parsers lógicos.

---

### [F-144] Aplicación 6: Diagnóstico médico
`@tipo: codigo`

```prolog
sintoma(juan, fiebre).
sintoma(juan, tos).
sintoma(maria, dolor_cabeza).

diagnostico(P, gripe) :-
    sintoma(P, fiebre), sintoma(P, tos).
diagnostico(P, migrana) :-
    sintoma(P, dolor_cabeza).

?- diagnostico(juan, D).
D = gripe.
```

MYCIN (1970s) y sucesores se construyeron sobre variantes de este patrón.

---

### [F-145] Aplicación 7: Planificación
`@tipo: codigo`

```prolog
accion(ir(De, A), estado(De), estado(A)).
accion(cargar, estado(deposito), estado(con_paquete)).

plan(Inicio, Inicio, []).
plan(Inicio, Fin, [A|Rest]) :-
    accion(A, Inicio, Intermedio),
    plan(Intermedio, Fin, Rest).

?- plan(estado(casa), estado(oficina), P).
```

La base del paradigma *STRIPS* y buena parte de la IA clásica de planificación.

---

### [F-146] Aplicación 8: Sistema experto
`@tipo: codigo`

```prolog
recomendar(vegetariano, lasagna_verduras).
recomendar(sin_gluten, ensalada_quinoa).
recomendar(carnivoro, milanesa).

preferencia(juan, vegetariano).
preferencia(maria, sin_gluten).

plato(P, Plato) :-
    preferencia(P, Diet),
    recomendar(Diet, Plato).

?- plato(juan, Q).
Q = lasagna_verduras.
```

Sistemas de recomendación con reglas explicables — **explainable AI** bien temprana.

---

### [F-147] Aplicación 9: Grafo de conocimiento
`@tipo: codigo`

```prolog
es_a(perro, mamifero).
es_a(mamifero, animal).
es_a(animal, ser_vivo).
es_a(canario, ave).
es_a(ave, animal).

hereda(X, Y) :- es_a(X, Y).
hereda(X, Y) :- es_a(X, Z), hereda(Z, Y).

?- hereda(perro, Q).
Q = mamifero ; Q = animal ; Q = ser_vivo.
```

Ontologías, RDF, OWL — todas tienen este patrón de fondo.

---

### [F-148] Aplicación 10: Restricciones laborales
`@tipo: codigo`

```prolog
:- use_module(library(clpfd)).

horarios(Ana, Beto, Carla) :-
    [Ana, Beto, Carla] ins 8..17,     % horario laboral
    Ana #\= Beto, Ana #\= Carla, Beto #\= Carla,
    Ana #< Beto,
    Carla #= Beto + 1,
    label([Ana, Beto, Carla]).

?- horarios(A, B, C).
A = 8, B = 9,  C = 10 ;
A = 8, B = 10, C = 11 ;
…
```

Asignación de recursos con restricciones — **scheduling** clásico.

---

### [F-149] ¿Qué tienen en común?
`@tipo: concepto-mixto`

Todas las aplicaciones usan:
1. **Una base** de hechos/reglas (conocimiento del dominio)
2. **Consultas múltiples** sobre la misma base
3. **Backtracking** para enumerar alternativas
4. Opcional: **restricciones** (CLP) para problemas NP

Esto separa Prolog de otros lenguajes: el programa ES la base de datos.

---

## BLOQUE 6 (original: 12) — Panorama Prolog 2026 (25 min) · F-150 a F-154

*(Dictado como cierre, incluye Datalog, neuro-simbólico e implementaciones modernas)*

---

### [F-150] ¿Está vivo Prolog en 2026?
`@tipo: concepto-abstracto`

**Sí — pero distribuido en nichos:**

- **Datalog**: usado en bases analíticas (Logica, Soufflé, DDlog)
- **Neuro-simbólico**: DeepProbLog, híbridos LLM+reglas
- **Verificación formal**: ACL2, Isabelle bebe ideas de Prolog
- **IA explicable**: motores de reglas auditables
- **Scheduling**: CLP(FD), CLP(Z) en industria

No es el “lenguaje universal” soñado en los ’80, pero está en todos lados.

---

### [F-151] Datalog: el hijo exitoso
`@tipo: codigo`

```datalog
padre(juan, pedro).
ancestro(X, Y) :- padre(X, Y).
ancestro(X, Y) :- padre(X, Z), ancestro(Z, Y).

?- ancestro(juan, Q).
```

Diferencias con Prolog:
- Sin términos compuestos ni listas
- Sin corte ni negación por falla (en Datalog puro)
- **Terminación garantizada** (para bases finitas)
- Evaluación bottom-up (más eficiente para bases grandes)

Usado en Google (Logica), Meta (internal), análisis estático (Soufflé).

---

### [F-152] Neuro-simbólico: LLM + Prolog
`@tipo: concepto-mixto`

```text
[Usuario] "¿Quién es el bisabuelo de Pedro?"
    ↓
[LLM] traduce a goal Prolog:
    ?- ancestro(X, pedro), ancestro(X, A), ancestro(A, pedro)
         no, mejor:  bisabuelo(X, pedro).
    ↓
[Prolog] ejecuta → 3 candidatos
    ↓
[LLM] redacta respuesta natural
```

Frameworks 2024–2026:
- **DeepProbLog** (Manhaeve et al.)
- **SymbolicAI** (Dinu et al.)
- **AlphaProof** (DeepMind, 2024)

La tendencia: **LLMs que delegan razonamiento formal** a motores lógicos.

---

### [F-153] Implementaciones modernas
`@tipo: tabla`

| Prolog | Año | Destacable |
|--------|-----|-----------|
| **SWI-Prolog** | 1987–2026 | Estándar de facto, ISO, comunidad activa |
| **Scryer Prolog** | 2020–2026 | Escrito en Rust, ISO estricto, WASM |
| **Trealla Prolog** | 2021– | C, minimalista, server-side |
| **Tau Prolog** | 2017– | JavaScript, Prolog en el navegador |
| **XSB** | 1990– | `tabling` potente, Datalog++ |
| **Ciao** | 1996– | Modular, análisis estático |

---

### [F-154] Por qué todavía lo estudiamos
`@tipo: concepto-abstracto`

- **Amplía el pensamiento**: pensar relacionalmente, no imperativamente
- **Explicabilidad**: cada respuesta es una demostración — ideal en 2026 para auditar IA
- **Conciso en ciertos dominios**: parsing, reglas de negocio, constraint-solving
- **Base conceptual**: SQL, grafos, bases deductivas, LLMs+reglas
- **El mejor diagnóstico** para futuro programador: ¿puedo pensar en relaciones?

---

## Cierre · F-155 a F-158

---

### [F-155] Síntesis en 5 puntos
`@tipo: cierre`

1. **Unificación + resolución SLD** = el motor de Prolog.
2. **Backtracking** es gratis; el orden de cláusulas importa.
3. **`!` y `\+`** dan control, cuestan declaratividad.
4. **Listas + recursión con acumulador** = 90% de los programas útiles.
5. **Prolog vive** en Datalog, neuro-simbólico y explicabilidad.

---

### [F-156] TP del tema
`@tipo: concepto-mixto`

**Consigna:**
1. Modelar un dominio propio (mínimo 20 hechos + 5 reglas derivadas)
2. Escribir 10 consultas significativas
3. Resolver 1 puzzle con CLP(FD) o generate-and-test
4. Entregar: archivo `.pl` + documento `tp.md` con explicación

**Fecha:** 2 semanas desde hoy. **Pareja:** opcional.

---

### [F-157] Pregunta de salida
`@tipo: socratica`

**Tomate 1 minuto:**

> "Dame un ejemplo (de tu vida cotidiana o profesional) que sería **más fácil** en Prolog que en Python."

Escribilo en un post-it y lo dejamos en la puerta. Lo revisamos la semana que viene.

---

### [F-158] Gracias
`@tipo: cierre`

**Gracias por una clase doble intensa.**

- Material: [repositorio del curso]
- Guía de estudio: `guia-estudio.md`
- Consultas: jueves 18–20 hs
- Próxima clase: **Paradigma OO con TypeScript**

*"Prolog no es el lenguaje que vas a usar todos los días.
Es el lenguaje que cambia cómo pensás sobre los que sí usás."*

— Bob Kowalski (parafraseado)

---

*Tema 07 — Filminas — Paradigmas y Lenguajes de Programación 2026 — UNTdF — 2026-04-21*
*Total: 158 filminas · 240 min · Auto-aprobado por el docente*
