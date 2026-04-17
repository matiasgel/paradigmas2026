# Filminas — Tema 06: Paradigma Lógico: Prolog — Clase 1 de 3: Introducción

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Docente:** Matías Gel — UNTDF / IDEI  
**Duración:** 120 minutos | **Clase:** 1 de 3  
**Generado por:** Dr. Roberto (class-writer) — 2026-04-17  

---

## BLOQUE 1 — Motivación (15 min) · Filminas F-01 a F-05

---

### [F-01] El Cuarto Paradigma



Hasta ahora vimos:
- **Imperativo** → decimos *cómo* hacer las cosas paso a paso
- **Funcional** → transformamos datos con funciones puras

El **Paradigma Lógico** dice:
> *"Describí lo que sabés. Yo encuentro las respuestas."*

**Lenguaje representativo:** Prolog (Programming in Logic)  
**Creadores:** Colmerauer y Roussel (Marsella, 1972) + Kowalski (Edinburgh)

---

**Idea central:**
```
Programa Imperativo  = instrucciones de control
Programa Funcional   = transformaciones de datos
Programa Lógico      = base de conocimiento + motor de inferencia
```

**Analogía:** un experto legal. No le decís *cómo* razonar — le describís los hechos del caso y las leyes aplicables. Él deduce si el acusado es culpable.

---

### [F-02] ¿Quiénes son los abuelos de Laura?


**Base de datos familiar:**

```
Ana → madre → Carlos
Ana → madre → Beatriz
Carlos → padre → Laura
Carlos → padre → Pedro
Beatriz → madre → Tomás
```

**En Python** necesitamos escribir la *lógica de búsqueda*:

```python
def abuelos(persona, relaciones):
    padres_de = [p for p, h, _ in relaciones if h == persona]
    result = []
    for padre in padres_de:
        abuelos_de_padre = [p for p, h, _ in relaciones if h == padre]
        result.extend(abuelos_de_padre)
    return result
```

**En Prolog** describimos el *conocimiento* y consultamos:

```prolog
madre(ana, carlos).
madre(ana, beatriz).
padre(carlos, laura).
abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).

?- abuelo(ana, laura).
true.
```

**La diferencia:** Prolog *infiere* la respuesta. Python la *calcula* explícitamente.

---

### [F-03] Decir QUÉ vs. decir CÓMO


| | Imperativo / Funcional | Lógico |
|---|---|---|
| **Foco** | Algoritmo de solución | Conocimiento del dominio |
| **Pregunta** | ¿Cómo lo calculo? | ¿Qué es verdadero? |
| **Control** | Explícito (loops, recursión) | Implícito (motor Prolog) |
| **Reutilización** | Funciones / métodos | Relaciones (consultas múltiples) |
| **Depuración** | Seguir el flujo de ejecución | Revisar la base de conocimiento |

**Ejemplo — mismo problema, distinto enfoque:**

```python
# Imperativo: yo controlo la búsqueda
def es_primo(a, b):
    comunes = set(padres(a)) & set(padres(b))
    return len(comunes) > 0 and a != b
```

```prolog
% Lógico: yo declaro la relación
primo(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y.
```

---

### [F-04] Prolog en el mundo real


**Historia:**
- 1972 — Marsella: primer intérprete Prolog (Colmerauer + Roussel)
- 1977 — Edinburgh: versión estándar (Warren)
- 1995 — ISO Prolog (estándar internacional)
- Hoy: SWI-Prolog, GNU Prolog, SICStus, Ciao

**Aplicaciones reales:**
- 🧠 **Sistemas expertos médicos** (MYCIN, 1970s — diagnóstico de infecciones)
- 💬 **Procesamiento de lenguaje natural** — parsers, gramáticas
- 🕹️ **Resolución de puzzles** — Sudoku, 8-reinas, planificación
- 📊 **Bases de datos deductivas** — consultas sobre ontologías (OWL, RDF)
- 🤖 **IA simbólica** — planificación, razonamiento automático
- 📡 **Erlang** — lenguaje de telecomunicaciones inspirado en Prolog

**Curiosidad:** IBM Watson usó componentes de razonamiento lógico para ganar en Jeopardy! (2011).

---

### [F-05] Relevancia en 2026


**No por su uso masivo — sino por lo que enseña:**

1. **Pensar relacionalmente:** las bases de datos NoSQL, los grafos de conocimiento y las ontologías son "Prolog moderno"
2. **Separar conocimiento de control:** arquitectura limpia, mantenible
3. **Entender la inferencia automática:** los motores de reglas de negocio (Drools, Cortex) funcionan igual
4. **Fundamentos de IA simbólica:** necesario para entender sistemas híbridos neuro-simbólicos (GPT + razonamiento formal)
5. **Paradigma completo:** te obliga a pensar diferente — amplía el repertorio de soluciones

> *"The study of logic programming can broaden a programmer's perspective on what programming languages can do and how they can be designed."*  
> — Sebesta, Cap. 16

---

## BLOQUE 2 — Fundamentos Teóricos (20 min) · Filminas F-06 a F-12

---

### [F-06] El sustento matemático (versión rápida)


**Proposición:** enunciado que puede ser verdadero o falso.

```
P: "Ana es madre de Carlos"       → verdadero
Q: "Carlos es madre de Ana"       → falso
```

**Conectivos:**
| Símbolo | Nombre | Significado |
|---------|--------|-------------|
| `¬P` | Negación | "No P" |
| `P ∧ Q` | Conjunción | "P y Q" |
| `P ∨ Q` | Disyunción | "P o Q" |
| `P → Q` | Implicación | "Si P, entonces Q" |
| `P ↔ Q` | Bicondicional | "P si y solo si Q" |

**En Prolog:**
- `∧` → `,` (coma)
- `→` → `:-`
- `¬` → `\+` (negación por falla)

---

### [F-07] De proposiciones a predicados


**Problema de la lógica proposicional:** no puede hablar de *individuos*.

`P: "alguien es madre de alguien"` — ¿quiénes?

**Cálculo de predicados (lógica de primer orden):** agrega variables y cuantificadores.

**Predicado:** relación entre individuos.
```
madre(ana, carlos)     % "ana" y "carlos" son los argumentos
esPar(4)               % predicado unario
suma(2, 3, 5)          % predicado ternario
```

**Cuantificadores:**
```
∀X: pez(X) → animal(X)    % "Para todo X, si X es pez entonces X es animal"
∃X: madre(X, carlos)       % "Existe algún X que es madre de Carlos"
```

**En Prolog:**
- Variables con mayúscula representan cuantificación universal en hechos/reglas
- Las consultas buscan instancias que satisfagan la fórmula (cuantificación existencial implícita)

---

### [F-08] Cláusulas de Horn: el lenguaje de Prolog


**Definición:** Una cláusula de Horn es una disyunción de literales con *al más uno positivo*.

**Forma general:**
```
B₁ ∧ B₂ ∧ ... ∧ Bₙ → H
```
Se lee: "Si B₁ y B₂ y ... y Bₙ son verdaderos, entonces H es verdadero"

**En sintaxis Prolog:**
```prolog
H :- B₁, B₂, ..., Bₙ.
```

**Tres tipos de cláusulas:**

| Tipo | Forma | Ejemplo Prolog |
|------|-------|----------------|
| Hecho (cláusula unitaria) | `H.` | `madre(ana, carlos).` |
| Regla (cláusula de Horn con cabeza) | `H :- B₁, ..., Bₙ.` | `abuelo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).` |
| Consulta (cláusula sin cabeza) | `:- B₁, ..., Bₙ.` | `?- abuelo(ana, Z).` |

> *"Prolog has two basic statement forms; these correspond to the headless and headed Horn clauses of predicate calculus."*  
> — Sebesta, Cap. 16

---

### [F-09] ¿Cómo "piensa" Prolog?


**Principio de Resolución (Robinson, 1965):**  
Si tenemos `A :- B` y `B` es verdadero, podemos concluir `A`.

**Ejemplo:**
```
Regla:   abuelo(ana, Z) :- progenitor(ana, Y), progenitor(Y, Z).
Hecho:   progenitor(ana, carlos).
Hecho:   progenitor(carlos, laura).

Consulta: ?- abuelo(ana, laura).

Paso 1: Unificar consulta con cabeza de la regla → Y libre, Z = laura
Paso 2: Nueva meta: progenitor(ana, Y), progenitor(Y, laura)
Paso 3: progenitor(ana, Y) → calza con hecho → Y = carlos
Paso 4: progenitor(carlos, laura) → calza con hecho → ✓
Resultado: true
```

**Prolog = Resolución SLD** (Selective Linear Definite clause resolution)
- Selecciona metas de izquierda a derecha
- Prueba cláusulas de arriba a abajo
- Usa backtracking cuando falla

---

### [F-10] Dos momentos completamente distintos


**MOMENTO 1 — Crear la base de conocimiento (archivo `.pl`)**

```prolog
% archivo: familia.pl
madre(ana, carlos).
madre(ana, beatriz).
padre(carlos, laura).
padre(carlos, pedro).
madre(beatriz, tomas).

progenitor(X, Y) :- madre(X, Y).
progenitor(X, Y) :- padre(X, Y).
abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
```
→ El archivo **no hace nada** solo. Es conocimiento estático.

**MOMENTO 2 — Consultar (en el intérprete)**

```prolog
?- consult('familia.pl').     % cargar la base
true.

?- madre(ana, carlos).        % ¿es verdad?
true.

?- abuelo(ana, Z).            % ¿quiénes son nietos de Ana?
Z = laura ;
Z = pedro ;
Z = tomas.
```

→ **El motor infiere**, no "ejecuta". Busca una prueba de que la consulta es verdadera.

**Analogía:**
- Base = las reglas del ajedrez escritas en un libro
- Consulta = hacer una jugada y preguntar si es legal

---

### [F-11] Todo en Prolog es un Término


**Árbol de tipos:**
```
Término
├── Atómico
│   ├── Átomo         → ana, carlos, 'Ana López', hello_world
│   └── Número        → 42, 3.14, -7
├── Variable          → X, Persona, _Aux, _
└── Término Compuesto → funtor(arg1, arg2, ...)
    ├── madre(ana, carlos)     ← aridad 2
    ├── pez(trucha)            ← aridad 1
    └── f(a, g(b), X)          ← anidados
```

**Reglas de sintaxis:**
| Tipo | Regla | Ejemplos válidos | Ejemplos inválidos |
|------|-------|------------------|--------------------|
| Átomo | empieza con minúscula o entre `'...'` | `ana`, `'Ana'`, `hello` | `Ana`, `Hello` |
| Variable | empieza con MAYÚSCULA o `_` | `X`, `Persona`, `_tmp` | `ana` (si queremos variable) |
| Anónima | `_` solo | `_` | — |
| Número | dígitos | `42`, `3.14` | — |

**En clase — identificar tipos:**
```prolog
madre(ana, carlos).      % átomo, átomo, átomo
progenitor(X, Y).        % átomo, Variable, Variable
f(g(a), h(X, 3)).        % compuesto anidado con variable y número
```

---

### [F-12] ¿Cómo "calzan" los términos? (preview de Clase 2)


**Unificación:** proceso de hacer que dos términos sean iguales mediante sustitución de variables.

**Casos básicos:**
```prolog
?- X = ana.
X = ana.              % X se instancia a 'ana'

?- f(X, 3) = f(ana, Y).
X = ana,
Y = 3.               % X→ana, Y→3

?- madre(ana, X) = madre(ana, carlos).
X = carlos.          % X→carlos

?- X = X.
true.                % siempre unifica

?- ana = carlos.
false.               % átomos distintos nunca unifican
```

**Punto clave:** en Prolog `=` **no** es asignación — es **unificación**. Si falla, el motor hace backtracking.

> *(La unificación completa, con el algoritmo de Martelli-Montanari, se desarrolla en Clase 2)*

---

## BLOQUE 3 — Sintaxis Prolog (25 min) · Filminas F-13 a F-20

---

### [F-13] Hechos: la verdad incondicional


**Definición:** Un hecho es una cláusula de Horn sin antecedente. Declara algo verdadero incondicionalmente.

**Sintaxis:**
```
nombre_predicado(arg1, arg2, ..., argN).
```
- Predicado: átomo (minúscula)
- Argumentos: cualquier término
- **Obligatorio:** terminar con punto `.`

**Base de conocimiento familia — construcción paso a paso:**

```prolog
% Paso 1: hechos sobre relaciones de parentesco
madre(ana, carlos).      % "Ana es madre de Carlos"
madre(ana, beatriz).     % "Ana es madre de Beatriz"
padre(carlos, laura).    % "Carlos es padre de Laura"
padre(carlos, pedro).    % "Carlos es padre de Pedro"
madre(beatriz, tomas).   % "Beatriz es madre de Tomás"
```

**¿Qué puede ser un argumento?**
```prolog
edad(ana, 45).               % átomo + número
vive_en(carlos, 'Ushuaia').  % átomo + átomo con espacios
coordenadas(p1, punto(3, 7)). % átomo + término compuesto
```

---

### [F-14] Hechos en distintos dominios


**Dominio 1: Parentesco**
```prolog
madre(ana, carlos).
padre(carlos, laura).
```

**Dominio 2: Geografía**
```prolog
capital(argentina, 'Buenos Aires').
capital(chile, santiago).
pais(argentina).
pais(chile).
frontera(argentina, chile).
```

**Dominio 3: Cursos universitarios**
```prolog
materia('Paradigmas', codigo_IF040).
docente('Matías Gel', 'Paradigmas').
alumno(legajo(1234), 'Juan Pérez').
inscripto(legajo(1234), codigo_IF040, 2026).
```

**Ejercicio en clase:**  
"¿Cómo representarías 'El libro Prolog de Clocksin tiene 300 páginas'?"

```prolog
libro(clocksin_mellish, 'Programming in Prolog', 300).
```

---

### [F-15] Reglas: conocimiento derivado


**Definición:** Una regla define un predicado en términos de otros predicados. Es la "implicación" de Prolog.

**Estructura:**
```prolog
cabeza :- cuerpo.
% H     :- B₁, B₂, ..., Bₙ.
```

- **Cabeza** (`H`): lo que estamos definiendo — lo que será verdadero SI...
- **`:-`**: se lee "si" o "es verdadero si"
- **Cuerpo** (`B₁, ..., Bₙ`): condiciones — todas deben ser verdaderas (conjunción)
- **Coma `,`**: significa AND lógico

**Ejemplo construido en clase:**
```prolog
% "X es progenitor de Y si X es madre de Y"
progenitor(X, Y) :- madre(X, Y).

% "X es progenitor de Y si X es padre de Y"
progenitor(X, Y) :- padre(X, Y).
```
→ Dos cláusulas para `progenitor` = OR implícito (se prueban en orden)

```prolog
% "X es abuelo de Z si existe Y tal que X es progenitor de Y
%  y Y es progenitor de Z"
abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
```
→ La variable `Y` actúa como variable de unión (intermedia)

---

### [F-16] Cómo leer una regla Prolog


**Regla:**
```prolog
abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
```

**Lectura correcta:**  
*"X es abuelo de Z si existe algún Y tal que X es progenitor de Y **y** Y es progenitor de Z."*

**Las variables en una regla son universalmente cuantificadas:**  
La regla vale para CUALQUIER X, Y, Z — no solo para `ana` o `carlos`.

**Verificar que funciona para todos los casos:**
```prolog
?- abuelo(ana, laura).   % ¿Ana es abuela de Laura? → true
?- abuelo(ana, tomas).   % ¿Ana es abuela de Tomás? → true
?- abuelo(X, tomas).     % ¿Quiénes son abuelos de Tomás? → X = ana
```

**Regla con múltiples condiciones:**
```prolog
% X es hermano de Y si:
%   - tienen el mismo progenitor P
%   - X no es la misma persona que Y
hermano(X, Y) :-
    progenitor(P, X),
    progenitor(P, Y),
    X \= Y.
```
*(Estilo: las condiciones pueden ir en líneas separadas para legibilidad)*

---

### [F-17] Consultas: haciendo preguntas al motor


**En SWI-Prolog:**
```
?-    ← prompt del intérprete (significa "¿es verdad que...?")
```

**Tipos de consultas:**

**1. Consulta booleana (sin variables):**
```prolog
?- madre(ana, carlos).
true.

?- madre(carlos, ana).
false.
```

**2. Consulta con variables (busca instancias):**
```prolog
?- madre(ana, X).
X = carlos ;      % escribir ; para pedir más soluciones
X = beatriz.      % punto para terminar

?- madre(X, Y).
X = ana, Y = carlos ;
X = ana, Y = beatriz ;
X = beatriz, Y = tomas.
```

**3. Consulta con múltiples variables:**
```prolog
?- progenitor(X, laura).
X = carlos.          % solo un padre de Laura en la base

?- abuelo(X, Z).
X = ana, Z = laura ;
X = ana, Z = pedro ;
X = ana, Z = tomas.
```

---

### [F-18] Más de una respuesta: el operador `;`


**El motor de Prolog puede tener MÚLTIPLES soluciones:**

```prolog
?- madre(ana, X).
X = carlos ;     % presionar ; para pedir la siguiente
X = beatriz ;    % presionar ; de nuevo
false.           % no hay más soluciones
```

**¿Qué hace `;`?**
- Le pide a Prolog que busque **otra** solución
- Prolog hace **backtracking**: vuelve atrás y prueba otro camino
- Cuando no hay más soluciones devuelve `false`

**`findall/3` — todas las soluciones de una vez:**
```prolog
?- findall(X, madre(ana, X), Lista).
Lista = [carlos, beatriz].

?- findall(Z, abuelo(ana, Z), Nietos).
Nietos = [laura, pedro, tomas].
```

**Cuidado con consultas sin solución:**
```prolog
?- madre(X, ana).
false.           % nadie es madre de Ana en nuestra base
```
→ No significa que sea imposible — significa que **no está en la base**.

---

### [F-19] Base completa: resumen visual


```prolog
% ═══════════════════════════════════════
%  BASE DE CONOCIMIENTO: familia.pl
% ═══════════════════════════════════════

% — HECHOS — (relaciones primarias)
madre(ana,     carlos).
madre(ana,     beatriz).
padre(carlos,  laura).
padre(carlos,  pedro).
madre(beatriz, tomas).

% — REGLAS — (relaciones derivadas)

% Progenitor: madre o padre
progenitor(X, Y) :- madre(X, Y).
progenitor(X, Y) :- padre(X, Y).

% Abuelo: progenitor del progenitor
abuelo(X, Z) :-
    progenitor(X, Y),
    progenitor(Y, Z).

% Hermano: mismo progenitor, distintas personas
hermano(X, Y) :-
    progenitor(P, X),
    progenitor(P, Y),
    X \= Y.

% Tío: hermano de un progenitor
tio(X, Z) :-
    hermano(X, Y),
    progenitor(Y, Z).
```

**Árbol familiar (para referencia visual):**
```
         Ana
        /    \
    Carlos  Beatriz
    /   \       \
Laura  Pedro   Tomás
```

---

### [F-20] Cómo visualizar la base como grafo


**Los hechos como arcos dirigidos:**
```
ana ──madre──→ carlos
ana ──madre──→ beatriz
carlos ──padre──→ laura
carlos ──padre──→ pedro
beatriz ──madre──→ tomas
```

**Las reglas como derivaciones:**
```
progenitor(X, Y) ← madre(X, Y)  O  padre(X, Y)
abuelo(X, Z)     ← progenitor(X, Y) ∧ progenitor(Y, Z)
```

**Consulta como búsqueda de camino:**
```
?- abuelo(ana, laura).

¿Existe camino  ana → ? → laura  en la relación progenitor?

ana → carlos (madre) → laura (padre)  ✓
```

---

## BLOQUE 4 — Trazado Manual (25 min) · Filminas F-21 a F-28

---

### [F-21] Cómo Prolog resuelve una consulta (algoritmo)


**Algoritmo general (simplificado):**

```
1. Tomar la primera meta de la lista de metas
2. Buscar en la base (de arriba a abajo) una cláusula cuya cabeza
   UNIFIQUE con la meta
3. Si encontró:
     a. Sustituir la meta por el cuerpo de la cláusula (unificada)
     b. Continuar con la próxima meta
4. Si no encontró (o falla en alguna meta siguiente):
     a. BACKTRACKING: deshacer la última elección
     b. Continuar buscando desde la siguiente cláusula
5. Si la lista de metas queda vacía → ¡ÉXITO! (true)
6. Si se agotaron todas las opciones → FALLO (false)
```

**Este proceso se llama:** Resolución SLD (Selective Linear Definite)

---

### [F-22] Ejemplo 1: `?- madre(ana, carlos).`


```
Consulta: madre(ana, carlos)

Lista de metas: [ madre(ana, carlos) ]

Paso 1: Tomar primera meta → madre(ana, carlos)
Paso 2: Buscar en la base...
   Cláusula 1: madre(ana, carlos).
              ↓ ¿Unifica madre(ana, carlos) con madre(ana, carlos)?
              ↓ ana = ana ✓,  carlos = carlos ✓
              → UNIFICA
Paso 3: Sustituir por cuerpo → cuerpo vacío (es un hecho)
Paso 4: Lista de metas queda vacía → ÉXITO

Resultado: true
```

**Punto clave:** Prolog encontró una **prueba**: madre(ana, carlos) es un hecho.

---

### [F-23] Ejemplo 2: `?- madre(ana, X).`


```
Consulta: madre(ana, X)    [X es variable libre]

Lista de metas: [ madre(ana, X) ]

Paso 1: meta → madre(ana, X)
Paso 2: Buscar en la base...
   Cláusula 1: madre(ana, carlos).
              ↓ ana = ana ✓, X unifica con carlos → X = carlos
              → UNIFICA → X = carlos

Lista de metas vacía → ÉXITO
Respuesta: X = carlos

[usuario pide ; → backtracking]

Deshago: X vuelve a ser libre
Cláusula 2: madre(ana, beatriz).
              ↓ ana = ana ✓, X unifica con beatriz → X = beatriz
              → UNIFICA

Respuesta: X = beatriz

[usuario pide ; → backtracking]

Cláusula 3: madre(beatriz, tomas).
              ↓ ana ≠ beatriz → NO UNIFICA → saltar

No hay más cláusulas de madre/2.
→ false (no más soluciones)
```

---

### [F-24] Ejemplo 3: `?- abuelo(ana, Z).`


```
Consulta: abuelo(ana, Z)

Regla usada: abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
Unificar cabeza: X = ana, Z libre

Nueva lista de metas: [ progenitor(ana, Y), progenitor(Y, Z) ]

─── Resolver progenitor(ana, Y) ───
Regla 1: progenitor(X,Y) :- madre(X,Y). → madre(ana, Y)
  Hecho: madre(ana, carlos) → Y = carlos ✓

─── Resolver progenitor(carlos, Z) ───
Regla 2: progenitor(X,Y) :- padre(X,Y). → padre(carlos, Z)
  Hecho: padre(carlos, laura) → Z = laura ✓
  → Respuesta: Z = laura

[; → backtracking en progenitor(carlos, Z)]
  Hecho: padre(carlos, pedro) → Z = pedro ✓
  → Respuesta: Z = pedro

[; → backtracking, agotados padre(carlos,...)]
[backtracking en progenitor(ana, Y)]

Regla 1 de madre: madre(ana, beatriz) → Y = beatriz ✓

─── Resolver progenitor(beatriz, Z) ───
  madre(beatriz, tomas) → Z = tomas ✓
  → Respuesta: Z = tomas

[; → no más soluciones]
→ false
```

---

### [F-25] Árbol de búsqueda para `?- abuelo(ana, Z).`


```
                abuelo(ana, Z)
                      │
          progenitor(ana,Y), progenitor(Y,Z)
         /                              \
    Y=carlos                          Y=beatriz
        │                                  │
progenitor(carlos, Z)          progenitor(beatriz, Z)
      /        \                         │
  Z=laura   Z=pedro                  Z=tomas
    ✓           ✓                      ✓

Respuestas: laura, pedro, tomas (en ese orden)
```

**Observación:** Prolog recorre el árbol en **profundidad primero** (depth-first).

---

### [F-26] Recursión: el poder de las reglas autorreferentes


**Problema:** `abuelo` solo funciona para 2 generaciones. ¿Y para 10 generaciones?

**Solución: `ancestro/2` con recursión**

```prolog
% CASO BASE: X es ancestro de Y si X es progenitor directo de Y
ancestro(X, Y) :- progenitor(X, Y).

% CASO RECURSIVO: X es ancestro de Y si
%   existe Z tal que X es progenitor de Z  (un paso)
%   y Z es ancestro de Y                  (resto de la cadena)
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).
```

**Lectura:**
- Caso base: "X es ancestro de Y en un solo paso"
- Caso recursivo: "X llega a Y pasando por un intermediario Z"

**La recursión termina** porque:
1. Eventualmente llegamos a una persona sin progenitores en la base
2. El caso base se activa cuando encontramos la conexión directa

---

### [F-27] Trazado de `ancestro(ana, pedro)`


```
Meta: ancestro(ana, pedro)

① Pruebo caso base: progenitor(ana, pedro)
   → madre(ana, pedro)?  NO
   → padre(ana, pedro)?  NO  → FALLA

② Pruebo caso recursivo: progenitor(ana, Z), ancestro(Z, pedro)

   → progenitor(ana, Z):
       madre(ana, carlos) → Z = carlos ✓

   → ancestro(carlos, pedro):
       ① caso base: progenitor(carlos, pedro)
              padre(carlos, pedro) → ✓  ← ¡ÉXITO!

Resultado: true
```

**Cadena de 2 pasos:** ana → carlos → pedro

**¿Qué pasaría con `ancestro(ana, tomas)`?**
```
ana → beatriz → tomas
(2 pasos, el motor encuentra el camino automáticamente)
```

---

### [F-28] Recursión: Prolog vs. Python


**Python (explícito):**
```python
def es_ancestro(x, y, hechos):
    # caso base: ¿x es progenitor directo de y?
    if (x, y) in hechos['progenitor']:
        return True
    # caso recursivo: buscar intermediario
    for z in hechos['progenitor'].get(x, []):
        if es_ancestro(z, y, hechos):
            return True
    return False
```

**Prolog (declarativo):**
```prolog
ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).
```

**Diferencias clave:**
| | Python | Prolog |
|---|---|---|
| Control del loop | explícito (for) | implícito (motor) |
| Retorno | return True/False | éxito/falla |
| Múltiples soluciones | necesito modificar | automático con `;` |
| Legibilidad | describe el algoritmo | describe la relación |

**Punto:** En Prolog la recursión es *natural* para relaciones transitivas.

---

## BLOQUE 5 — Comparación de Paradigmas (10 min) · Filminas F-29 a F-31

---

### [F-29] Imperativo vs. Funcional vs. Lógico


| Aspecto | Imperativo (Python) | Funcional (TypeScript) | Lógico (Prolog) |
|---|---|---|---|
| **Descripción** | Cómo ejecutar | Cómo transformar | Qué es verdadero |
| **Unidad mínima** | Instrucción | Función | Cláusula |
| **Estado** | Mutable | Inmutable | Ninguno |
| **Control** | Explícito (`if`, `while`) | Por estructura (recursión, pattern matching) | Automático (motor de inferencia) |
| **Evaluación** | Paso a paso | Reducción de expresiones | Prueba de metas |
| **Respuesta** | Retorna valor | Retorna valor | true/false + instanciaciones |
| **Múltiples respuestas** | Necesita estructuras | Usa listas/streams | Natural (backtracking) |
| **Ejemplo** | `for p in padres: ...` | `padres.filter(p => ...)` | `progenitor(X, Y) :- madre(X, Y).` |

---

### [F-30] Prolog brilla en...


**Problemas donde Prolog es natural:**

✅ **Relaciones complejas entre entidades**
```prolog
% Árbol genealógico, red social, ontología
primo(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y.
```

✅ **Búsqueda con restricciones**
```prolog
% Asignación de recursos, horarios, sudoku
asignacion(T, A) :- tarea(T), agente(A), compatible(T, A), \+ asignado(T).
```

✅ **Parsing y gramáticas (DCG)**
```prolog
oracion --> frase_nominal, frase_verbal.
frase_nominal --> determinante, sustantivo.
```

✅ **Sistemas expertos**
```prolog
diagnostico(gripe) :- sintoma(fiebre), sintoma(tos), sintoma(cansancio).
```

**Problemas donde NO es natural:**
- ❌ Computación numérica intensiva
- ❌ Interfaces de usuario / gráficos
- ❌ Manipulación masiva de archivos

---

### [F-31] El pasado y el futuro del paradigma lógico


**Historia:**
- 1970s-80s: Prolog = IA simbólica dominante
- 1990s-2000s: perdió terreno frente a ML
- 2020s: **renacimiento** como componente simbólico en sistemas híbridos

**Conexiones actuales:**
- **Knowledge Graphs** (Google, Meta) → bases de datos relacionales en escala
- **Datalog** → lenguaje de consulta basado en Prolog, usado en análisis de programas
- **Answer Set Programming (ASP)** → Prolog moderno para planificación y razonamiento
- **Neuro-simbólico** → LLMs + razonamiento formal (investigación activa en 2026)

> *"The integration of neural and symbolic approaches is one of the most active research areas in AI."*  
> — Gabbrielli & Martini, Cap. Lógica

---

## BLOQUE 6 — Ejercicios en Clase (10 min) · Filminas F-32 a F-34

---

### [F-32] Ejercicio: definir `hermano/2`


**Enunciado:**  
Dos personas son hermanas si tienen el mismo progenitor y son distintas.

**Paso 1:** Escribir en Prolog antes de ver la solución.

```
hermano(X, Y) :- ???
```

**Pista:** necesitás tres condiciones:
1. Mismo progenitor P para X
2. Mismo progenitor P para Y  
3. X no es Y

**Solución:**
```prolog
hermano(X, Y) :-
    progenitor(P, X),
    progenitor(P, Y),
    X \= Y.
```

**Consultas para probar:**
```prolog
?- hermano(carlos, beatriz).
true.

?- hermano(X, carlos).
X = beatriz.

?- hermano(laura, Z).
Z = pedro.
```

**Pregunta:** ¿Por qué necesitamos `X \= Y`? Sin esa condición, ¿qué pasaría?

---

### [F-33] Ejercicio de trazado: `?- hermano(carlos, Z).`


```
Meta: hermano(carlos, Z)
Regla: hermano(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y.
Unificar: X = carlos, Y = Z (libre)

Nuevas metas: progenitor(P, carlos), progenitor(P, Z), carlos \= Z

→ progenitor(P, carlos):
   madre(P, carlos) → madre(ana, carlos) → P = ana ✓

→ progenitor(ana, Z):
   madre(ana, carlos) → Z = carlos
   → carlos \= carlos? FALLA  (backtrack)

   madre(ana, beatriz) → Z = beatriz
   → carlos \= beatriz? ✓ ÉXITO

Respuesta: Z = beatriz

[;] backtracking... no más soluciones
false
```

**Observación:** el `\= Y` descarta la solución "X es hermano de sí mismo".

---

### [F-34] Ejercicios de síntesis


**Ejercicio 3a — `tio/2`:**
```prolog
% X es tío de Z si X es hermano de algún progenitor de Z
tio(X, Z) :-
    hermano(X, Y),
    progenitor(Y, Z).

?- tio(beatriz, laura).
true.    % Beatriz es hermana de Carlos, Carlos es padre de Laura
```

**Ejercicio 3b — `descendiente/2` (recursivo):**
```prolog
% X es descendiente de Y si Y es ancestro de X
% (reutiliza ancestro/2 — ¡1 sola cláusula!)
descendiente(X, Y) :- ancestro(Y, X).

?- descendiente(tomas, ana).
true.    % ana es ancestro de tomas → tomas es descendiente de ana
```

**Reflexión:** ¿Por qué `descendiente` solo necesita una cláusula? Porque `ancestro` ya tiene toda la lógica recursiva.

---

## BLOQUE 7 — Cierre (15 min) · Filminas F-35 a F-38

---

### [F-35] Lo que aprendimos hoy


**Los 5 conceptos clave:**

1. **Paradigma lógico:** declarar conocimiento, no escribir algoritmos
2. **Tres tipos de cláusulas:** hecho (`.`), regla (`:-`), consulta (`?-`)
3. **Base vs. inferencia:** el archivo `.pl` es estático; el motor infiere al consultar
4. **Resolución:** Prolog busca pruebas de arriba a abajo, con backtracking automático
5. **Recursión:** forma natural de expresar relaciones transitivas (caso base + caso recursivo)

**La base de conocimiento que construimos:**
```prolog
madre/2, padre/2         % hechos primarios
progenitor/2             % regla directa
abuelo/2, hermano/2      % reglas derivadas
tio/2                    % regla de segundo nivel
ancestro/2               % regla recursiva
descendiente/2           % reutilización
```

---

### [F-36] Confusiones comunes — ¡cuidado!


| Confusión | Incorrecto | Correcto |
|---|---|---|
| `=` como asignación | `X = 5, X = 6.` → debería funcionar | Falla: X ya está instanciada a 5 |
| Mayúscula/minúscula | `Ana` como nombre propio | `ana` (átomo), `Ana` (variable) |
| `,` vs `;` | `a, b` como OR | `,` es AND, `;` pide más soluciones |
| Orden de cláusulas | da igual el orden | El orden afecta eficiencia y puede causar loops |
| `false` = imposible | si no hay hecho, es imposible | Significa "no está en la base" (mundo cerrado) |

**Supuesto del Mundo Cerrado (CWA):**
> Lo que no está en la base se asume **falso**.

```prolog
?- madre(pedro, X).
false.
```
→ No significa que Pedro no tenga hijos — significa que **no declaramos** esa relación.

---

### [F-37] Próxima clase: profundizando el motor


**Temas de Clase 2:**

🔍 **Unificación completa:**
- Algoritmo de Martelli-Montanari
- Occur check
- Estructuras compuestas anidadas

🔄 **Backtracking:**
- El árbol de búsqueda completo
- Corte (`!`) para podar ramas
- Problemas de orden e infinitos

➕ **Aritmética en Prolog:**
```prolog
?- X is 2 + 3.
X = 5.        % ¡is/2 evalúa, = no!
```

📝 **Predicados de control:**
- `not/1` vs. `\+`
- `assert/1` y `retract/1` — modificar la base en tiempo de ejecución

**Ejercicio para pensar antes de la Clase 2:**  
¿Qué pasa con `?- ancestro(X, X).`? ¿Termina? ¿Por qué?

---

### [F-38] Para seguir practicando


**Software:**
- 🖥️ [SWI-Prolog](https://www.swi-prolog.org/) — instalación local
- 🌐 [SWISH](https://swish.swi-prolog.org/) — online, sin instalación
- 📱 [Tau Prolog](http://tau-prolog.org/) — Prolog en el navegador

**Bibliografía de la clase:**
- **Sebesta** — Cap. 16: Logic Programming Languages (pp. 703–784)
- **Gabbrielli & Martini** — Cap. Programación Lógica (pp. 351–423)
- **Louden & Lambert** — Cap. Logic Programming

**Ejercicio para casa:**  
Ampliar la base de conocimiento familiar para incluir:
1. `bisabuelo(X, Z)` — ¿cuántas cláusulas?
2. `familia(X, Y)` — X e Y son familia si comparten algún ancestro
3. Agregar una generación más a la familia (bisabuelos de Ana)

**Código de la clase:** disponible en el repositorio del curso.

---

*Total de filminas: 38 | Duración estimada: 120 minutos | Clase 1 de 3*  
*Generado por: Dr. Roberto (class-writer) — 2026-04-17*
