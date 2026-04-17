# Guía de Estudio — Tema 06: Paradigma Lógico: Prolog — Clase 1 de 3

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**UNTDF / IDEI | Docente:** Matías Gel  
**Preparada por:** Dra. Sofía (study-guide-writer) — 2026-04-17  
**Bibliografía principal:** Sebesta Cap. 16 (pp. 703–784) · Gabbrielli & Martini pp. 351–423 · Louden & Lambert

---

## ¿Cómo usar esta guía?

Esta guía está diseñada para **antes y después de la clase**:

- **Antes:** leer las secciones 1–3 (40 min) para llegar con el contexto teórico
- **Durante:** usar los ejemplos como referencia cuando el docente trace en pizarrón
- **Después:** resolver todos los ejercicios, especialmente los de trazado manual

Los recuadros **📖 Lectura obligatoria** indican páginas específicas del Sebesta.  
Los recuadros **⚠️ Confusión frecuente** marcan errores típicos del primer contacto.  
Los recuadros **🔧 Para practicar** son ejercicios con solución al final.

---

## Tabla de Contenidos

1. [El Paradigma Lógico — Conceptos Fundamentales](#1-el-paradigma-lógico--conceptos-fundamentales)
2. [Bases Matemáticas: Predicados y Cláusulas de Horn](#2-bases-matemáticas-predicados-y-cláusulas-de-horn)
3. [Sintaxis de Prolog](#3-sintaxis-de-prolog)
4. [Base de Conocimiento vs. Inferencia](#4-base-de-conocimiento-vs-inferencia)
5. [El Motor de Resolución y el Trazado](#5-el-motor-de-resolución-y-el-trazado)
6. [Recursión en Prolog](#6-recursión-en-prolog)
7. [Comparación de Paradigmas](#7-comparación-de-paradigmas)
8. [Ejercicios Resueltos](#8-ejercicios-resueltos)
9. [Ejercicios para Resolver](#9-ejercicios-para-resolver)
10. [Preguntas de Autoevaluación](#10-preguntas-de-autoevaluación)
11. [Bibliografía y Recursos](#11-bibliografía-y-recursos)

---

## 1. El Paradigma Lógico — Conceptos Fundamentales

### 1.1 ¿Qué es el paradigma lógico?

El paradigma lógico es el cuarto gran paradigma de programación. A diferencia del imperativo (que especifica *cómo* hacer las cosas) o del funcional (que describe *transformaciones* de datos), el paradigma lógico se basa en **declarar conocimiento** y dejar que un motor automático encuentre las respuestas.

> *"In logic programming, we use a symbolic logic as a programming language. We attempt to express knowledge in a neutral way and allow the system to apply whatever control and search is needed."*  
> — Sebesta, Cap. 16, p. 703

**La metáfora central:** imaginen un experto legal. No le damos instrucciones paso a paso sobre cómo razonar — le describimos los hechos del caso y las leyes aplicables. El experto deduce las conclusiones. En Prolog, nosotros somos quienes escribimos "los hechos y las leyes" (la base de conocimiento), y el motor de Prolog es el "experto" que razona.

### 1.2 Los componentes de un programa lógico

Todo programa Prolog tiene tres componentes:

```
┌─────────────────────────────────────────┐
│          Programa Prolog                │
│                                         │
│  BASE DE CONOCIMIENTO                   │
│  ├── Hechos (verdades incondicionales)  │
│  └── Reglas (verdades condicionales)    │
│                                         │
│  MOTOR DE INFERENCIA (automático)       │
│  └── Resolución SLD + Backtracking      │
│                                         │
│  CONSULTAS (preguntas al sistema)       │
└─────────────────────────────────────────┘
```

El programador solo escribe la base de conocimiento y formula consultas. El motor de inferencia lo provee Prolog — no necesitamos (ni debemos) escribirlo.

### 1.3 Historia del lenguaje

Prolog (PROgramming in LOGic) fue creado en 1972 por Alain Colmerauer y Philippe Roussel en la Universidad de Marsella, Francia, inspirados en el trabajo de Robert Kowalski en Edinburgh sobre resolución automática de teoremas.

La versión de Edinburgh (Warren, 1977) se convirtió en el estándar de facto. El estándar ISO fue adoptado en 1995.

**Implementaciones modernas:**
- **SWI-Prolog** (https://www.swi-prolog.org) — la más usada en educación e industria
- **GNU Prolog** — optimizada para constraint solving
- **SICStus Prolog** — commercial, muy usada en industria
- **SWISH** (https://swish.swi-prolog.org) — SWI-Prolog online, sin instalación

### 1.4 Aplicaciones del paradigma lógico

El paradigma lógico no es de nicho histórico — tiene aplicaciones concretas y vigentes:

| Aplicación | Descripción | Tecnología |
|---|---|---|
| **Sistemas expertos** | Diagnóstico médico, legal, industrial | Prolog, Drools |
| **Bases de datos deductivas** | Consultas sobre ontologías OWL/RDF | Datalog, SPARQL |
| **Procesamiento de lenguaje natural** | Parsers, gramáticas formales | Prolog DCG |
| **Verificación de software** | Model checking, análisis estático | Datalog (Doop, Soufflé) |
| **Planificación en IA** | STRIPS, HTN planning | PDDL, Prolog |
| **Knowledge Graphs** | Google Knowledge Graph, Wikidata | Derivados de Prolog |
| **Erlang** | Telecom, concurrencia masiva | Inspirado en Prolog |

---

## 2. Bases Matemáticas: Predicados y Cláusulas de Horn

### 2.1 Del álgebra de proposiciones al cálculo de predicados

La **lógica proposicional** trabaja con enunciados atómicos que son verdaderos o falsos:
- `P`: "Ana es madre de Carlos" → verdadero
- `Q`: "Carlos tiene hermanos" → verdadero

Pero tiene una limitación fundamental: **no puede hablar de individuos ni relaciones**.

El **cálculo de predicados de primer orden** (lógica de predicados) agrega:
- **Predicados:** relaciones entre individuos — `madre(ana, carlos)`, `esPar(4)`
- **Variables:** `X`, `Y`, `Z` — representan individuos arbitrarios
- **Cuantificadores:**
  - `∀X P(X)` — "para todo X vale P(X)"
  - `∃X P(X)` — "existe algún X tal que vale P(X)"

**Ejemplo de fórmula en lógica de predicados:**
```
∀X ∀Y: madre(X, Y) → progenitor(X, Y)
"Para todo X e Y, si X es madre de Y, entonces X es progenitor de Y"
```

### 2.2 Cláusulas de Horn

Una **cláusula de Horn** es una disyunción de literales con *a lo sumo un literal positivo*. Es la restricción que hace que la lógica de predicados sea computacionalmente tratable.

**Forma general de una cláusula de Horn:**
$$H \leftarrow B_1 \wedge B_2 \wedge \ldots \wedge B_n$$

Se lee: *"H es verdadero si B₁ y B₂ y ... y Bₙ son verdaderos"*

**Sintaxis equivalente en Prolog:**
```prolog
H :- B1, B2, ..., Bn.
```

📖 **Lectura obligatoria:** Sebesta, Cap. 16, pp. 703–710 — "Introduction to Logic Programming" y "Basic Elements of Prolog"

**Los tres tipos de cláusulas de Horn en Prolog:**

| Tipo | Descripción | Forma | Ejemplo |
|------|-------------|-------|---------|
| **Hecho** | Verdad incondicional — `n=0` | `H.` | `madre(ana, carlos).` |
| **Regla** | Verdad condicional — `n≥1` | `H :- B1,...,Bn.` | `abuelo(X,Z) :- progenitor(X,Y), progenitor(Y,Z).` |
| **Consulta** | Pregunta al sistema | `?- B1,...,Bn.` | `?- abuelo(ana, Z).` |

### 2.3 Resolución

El **principio de resolución** (Robinson, 1965) es el mecanismo de inferencia de Prolog. Dado:
- Una regla `H :- B`
- La prueba de `B`

Podemos concluir `H`.

Prolog usa **Resolución SLD** (Selective Linear Definite clause resolution):
- **Selectiva:** selecciona metas de izquierda a derecha
- **Lineal:** cada paso parte de la meta actual
- **Definite:** trabaja solo con cláusulas de Horn (cabeza positiva)

El resultado es un algoritmo de búsqueda **en profundidad primero (depth-first)** que es completo para cláusulas de Horn.

---

## 3. Sintaxis de Prolog

### 3.1 Términos — La unidad básica

Todo en Prolog está construido con **términos**. Hay cuatro tipos:

#### Átomos
- Secuencias de letras/dígitos/`_` que empiezan con **minúscula**
- O cualquier secuencia entre comillas simples
- Ejemplos: `ana`, `carlos`, `hello_world`, `'Ana López'`, `'Buenos Aires'`

#### Números
- Enteros: `42`, `-7`, `0`
- Flotantes: `3.14`, `-0.5`
- Ejemplos: `edad(ana, 45)`, `pi(3.14159)`

#### Variables
- Empiezan con **MAYÚSCULA** o guión bajo `_`
- La variable anónima `_` se usa cuando no nos importa el valor
- Ejemplos: `X`, `Persona`, `_Aux`, `_` (anónima)

⚠️ **Confusión frecuente:**
```prolog
madre(ana, carlos).   % 'ana' y 'carlos' son ÁTOMOS (minúscula)
madre(Ana, Carlos).   % 'Ana' y 'Carlos' son VARIABLES (mayúscula)
                      % ¡Muy diferente semánticamente!
```

#### Términos compuestos (estructuras)
- `funtor(arg1, arg2, ..., argN)` — el funtor es un átomo
- La **aridad** es el número de argumentos
- Pueden anidarse: `f(a, g(b, X), h(3))`

**Tabla de identificación rápida:**
```prolog
ana              % Átomo
'Ana López'      % Átomo con espacio
X                % Variable
_                % Variable anónima
42               % Número
madre(ana, X)    % Término compuesto, aridad 2
punto(3, 7)      % Término compuesto, aridad 2
```

### 3.2 Hechos

**Definición:** Un hecho es una cláusula sin cuerpo que declara una relación como verdadera incondicionalmente.

**Sintaxis:**
```
nombre_predicado(argumento1, ..., argumentoN).
```
- El predicado siempre empieza con minúscula
- Los argumentos son términos (átomos, números, variables, compuestos)
- **Obligatorio:** terminar con punto `.`

**Ejemplo — base de conocimiento familiar:**
```prolog
% Relaciones de maternidad
madre(ana, carlos).
madre(ana, beatriz).
madre(beatriz, tomas).

% Relaciones de paternidad
padre(carlos, laura).
padre(carlos, pedro).
```

**El árbol familiar que representa esta base:**
```
         Ana
        /    \
    Carlos  Beatriz
    /   \       \
Laura  Pedro   Tomás
```

📖 **Lectura obligatoria:** Sebesta, Cap. 16, pp. 710–715 — "Fact Statements" y "Rule Statements"

### 3.3 Reglas

**Definición:** Una regla define un predicado derivado en términos de otros predicados.

**Sintaxis:**
```prolog
cabeza :- condicion1, condicion2, ..., condicionN.
```

- **`cabeza`**: lo que será verdadero
- **`:-`**: se lee "si" o "es verdadero si"  
- **`,`**: conjunción (AND lógico) — todas las condiciones deben ser verdaderas
- **Variables**: implícitamente cuantificadas universalmente

**Ejemplo completo — construyendo la jerarquía:**

```prolog
% NIVEL 1: relaciones directas (hechos)
madre(ana, carlos).
madre(ana, beatriz).
padre(carlos, laura).
padre(carlos, pedro).
madre(beatriz, tomas).

% NIVEL 2: reglas directas
progenitor(X, Y) :- madre(X, Y).      % si X es madre de Y
progenitor(X, Y) :- padre(X, Y).      % si X es padre de Y

% NIVEL 3: relaciones derivadas
abuelo(X, Z) :-                        % X es abuelo de Z si...
    progenitor(X, Y),                  % X es progenitor de Y
    progenitor(Y, Z).                  % Y es progenitor de Z

hermano(X, Y) :-                       % X es hermano de Y si...
    progenitor(P, X),                  % P es progenitor de X
    progenitor(P, Y),                  % P es progenitor de Y (mismo P)
    X \= Y.                            % y X no es Y
```

**Observación sobre múltiples cláusulas:**
Cuando hay dos o más cláusulas para el mismo predicado, actúan como OR:
```prolog
progenitor(X, Y) :- madre(X, Y).   % alternativa 1
progenitor(X, Y) :- padre(X, Y).   % alternativa 2
```
Prolog las prueba en orden, de arriba a abajo.

### 3.4 Consultas

**Definición:** Una consulta es una pregunta al sistema — una cláusula sin cabeza.

**En el intérprete SWI-Prolog:**
```prolog
?-    ← el prompt (indica que espera una consulta)
```

**Tipos de consultas:**

**Consulta booleana** (sin variables):
```prolog
?- madre(ana, carlos).
true.              % Sí, es un hecho

?- madre(carlos, ana).
false.             % No está en la base
```

**Consulta existencial** (con variables):
```prolog
?- madre(ana, X).
X = carlos.        % Primera solución (presionar ; para más)

?- madre(ana, X).
X = carlos ;       % ← ';' pedimos más
X = beatriz ;      % ← ';' pedimos más
false.             % No hay más soluciones
```

**Consulta con múltiples variables:**
```prolog
?- abuelo(X, Z).
X = ana, Z = laura ;
X = ana, Z = pedro ;
X = ana, Z = tomas.
```

**Consulta con findall/3** (todas las soluciones de una vez):
```prolog
?- findall(Z, abuelo(ana, Z), Nietos).
Nietos = [laura, pedro, tomas].
```

---

## 4. Base de Conocimiento vs. Inferencia

Esta distinción es **fundamental** y fuente de muchas confusiones iniciales.

### 4.1 El archivo `.pl` — base de conocimiento estática

El archivo Prolog contiene hechos y reglas. **No hace nada por sí solo.** Es simplemente una descripción declarativa del conocimiento del dominio.

```prolog
% familia.pl — BASE DE CONOCIMIENTO
% Este archivo no "ejecuta" nada.
% Solo declara qué es verdadero.

madre(ana, carlos).
madre(ana, beatriz).
padre(carlos, laura).
padre(carlos, pedro).
madre(beatriz, tomas).

progenitor(X, Y) :- madre(X, Y).
progenitor(X, Y) :- padre(X, Y).
abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
```

### 4.2 El intérprete — motor de inferencia dinámico

La inferencia ocurre **solo cuando hacemos una consulta**:

```prolog
% PASO 1: cargar la base en el intérprete
?- consult('familia.pl').
true.

% PASO 2: ahora el motor puede razonar
?- abuelo(ana, laura).
true.

?- abuelo(X, tomas).
X = ana.
```

**Analogía:** la diferencia entre un libro de leyes (estático) y un juicio (dinámico). Las leyes están escritas, pero la interpretación ocurre cuando se plantea un caso concreto.

### 4.3 El Supuesto del Mundo Cerrado (CWA)

Prolog adopta el **Closed World Assumption**: todo lo que no está en la base se asume **falso**.

```prolog
?- madre(pedro, X).
false.
```

Esto no significa que Pedro no tenga hijos en el mundo real — significa que **no declaramos** esa información en nuestra base. El motor solo conoce lo que le decimos.

⚠️ **Confusión frecuente:** mucho cuidado con interpretar `false` como "es imposible". En Prolog `false` significa "no tengo evidencia de que sea verdadero".

---

## 5. El Motor de Resolución y el Trazado

### 5.1 Algoritmo de resolución de Prolog

Cuando Prolog recibe una consulta, ejecuta el siguiente proceso:

```
Algoritmo de Resolución SLD (simplificado):

Entrada: lista de metas [G1, G2, ..., Gn]

1. Si la lista está vacía → ÉXITO (true)
2. Tomar la primera meta G1
3. Buscar en la base, de arriba a abajo, una cláusula cuya
   CABEZA unifique con G1
4. Si encontró una cláusula H :- B1,...,Bk:
   a. Aplicar la sustitución de unificación a todo
   b. Reemplazar G1 por B1,...,Bk en la lista de metas
   c. Continuar recursivamente
5. Si no encontró ninguna cláusula aplicable → FALLA
   a. BACKTRACKING: deshacer la última elección
   b. Continuar buscando desde la siguiente cláusula
6. Si se agotaron todas las opciones → false
```

### 5.2 Trazado Ejemplo 1 — Consulta simple

```prolog
% Base:
% madre(ana, carlos).  [cláusula 1]
% madre(ana, beatriz). [cláusula 2]

?- madre(ana, carlos).
```

**Trazado:**
```
Meta actual:    [ madre(ana, carlos) ]

Paso 1: Tomar primera meta → madre(ana, carlos)
Paso 2: Buscar en la base...
   Cláusula 1: madre(ana, carlos).
   Unificar madre(ana, carlos) con madre(ana, carlos):
     ana = ana   ✓
     carlos = carlos   ✓
   → ÉXITO de unificación
Paso 3: Cuerpo vacío → no hay nuevas metas
Paso 4: Lista de metas = [ ] → ÉXITO

Respuesta: true
```

### 5.3 Trazado Ejemplo 2 — Variable libre

```prolog
?- madre(ana, X).
```

**Trazado:**
```
Meta actual:    [ madre(ana, X) ]    [X libre]

Paso 1: meta → madre(ana, X)
Paso 2: Buscar en la base...
   Cláusula 1: madre(ana, carlos).
   Unificar madre(ana, X) con madre(ana, carlos):
     ana = ana ✓, X unifica con carlos → X = carlos
   → ÉXITO → Lista vacía

Primera respuesta: X = carlos
─────────────────────────────
[usuario presiona ;]
BACKTRACKING: deshago X = carlos, X vuelve a ser libre
Continúo desde siguiente cláusula...

   Cláusula 2: madre(ana, beatriz).
   Unificar madre(ana, X) con madre(ana, beatriz):
     ana = ana ✓, X = beatriz
   → ÉXITO

Segunda respuesta: X = beatriz
─────────────────────────────
[usuario presiona ;]
BACKTRACKING: no hay más cláusulas de madre/2
→ false (no más soluciones)
```

### 5.4 Trazado Ejemplo 3 — Regla derivada

```prolog
?- abuelo(ana, Z).
```

**Regla disponible:**
```prolog
abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
progenitor(X, Y) :- madre(X, Y).
progenitor(X, Y) :- padre(X, Y).
```

**Trazado completo:**
```
Metas: [ abuelo(ana, Z) ]

Paso 1: meta → abuelo(ana, Z)
        Regla: abuelo(X', Z') :- progenitor(X', Y'), progenitor(Y', Z').
        Unificar: X' = ana, Z = Z' (libre), Y' libre
        Nuevas metas: [ progenitor(ana, Y'), progenitor(Y', Z) ]

Paso 2: meta → progenitor(ana, Y')
        Regla 1: progenitor(X'',Y'') :- madre(X'',Y'').
        Unificar: X'' = ana, Y'' = Y'
        Nuevas metas: [ madre(ana, Y'), progenitor(Y', Z) ]
        → madre(ana, Y'): calza con madre(ana, carlos) → Y' = carlos
        Metas: [ progenitor(carlos, Z) ]

Paso 3: meta → progenitor(carlos, Z)
        Regla 2 de progenitor: progenitor(X,Y) :- padre(X,Y).
        → padre(carlos, Z): calza con padre(carlos, laura) → Z = laura
        Metas: []   → ÉXITO
        
Primera respuesta: Z = laura

[;] → backtracking en padre(carlos, Z)
      padre(carlos, pedro) → Z = pedro   ÉXITO
      
Segunda respuesta: Z = pedro

[;] → backtracking, agotados padre(carlos,_)
      backtracking en progenitor(ana, Y')
      madre(ana, beatriz) → Y' = beatriz
      
      meta → progenitor(beatriz, Z)
      → madre(beatriz, tomas) → Z = tomas   ÉXITO
      
Tercera respuesta: Z = tomas

[;] → false (sin más soluciones)
```

**Árbol de búsqueda completo:**
```
             abuelo(ana, Z)
                    │
        progenitor(ana,Y), progenitor(Y,Z)
               /                \
          Y=carlos            Y=beatriz
              │                    │
     progenitor(carlos,Z)  progenitor(beatriz,Z)
         /          \              │
     Z=laura      Z=pedro       Z=tomas
       ✓             ✓            ✓
```

### 5.5 Herramienta de trazado en SWI-Prolog

SWI-Prolog incluye un depurador interactivo que muestra cada paso de la resolución:

```prolog
?- trace.
true.

[trace] ?- abuelo(ana, Z).
   Call: (10) abuelo(ana, _G1)
   Call: (11) progenitor(ana, _G2)
   Call: (12) madre(ana, _G2)
   Exit: (12) madre(ana, carlos)
   Exit: (11) progenitor(ana, carlos)
   Call: (11) progenitor(carlos, _G1)
   ...
```

Para desactivar: `?- notrace.`

---

## 6. Recursión en Prolog

### 6.1 ¿Por qué la recursión es natural en Prolog?

Las relaciones transitivas (ancestro, conectado, alcanzable) tienen una profundidad variable que no podemos conocer de antemano. En Prolog, la recursión emerge naturalmente de las reglas sin necesidad de estructuras de control explícitas.

### 6.2 Estructura de un predicado recursivo

Todo predicado recursivo correcto en Prolog tiene:
1. **Caso base:** una cláusula que termina sin llamada recursiva
2. **Caso recursivo:** una cláusula que se llama a sí misma (con argumentos más "simples")

```prolog
% CASO BASE: "da un paso directo"
ancestro(X, Y) :- progenitor(X, Y).

% CASO RECURSIVO: "da un paso y continúa"
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).
```

**Lectura del caso recursivo:**  
*"X es ancestro de Y si existe algún Z tal que X es progenitor de Z y Z es ancestro de Y."*

### 6.3 Trazado de `ancestro(ana, pedro)`

```
Meta: ancestro(ana, pedro)

INTENTO 1 — Caso base:
  progenitor(ana, pedro)?
    madre(ana, pedro)? → NO
    padre(ana, pedro)? → NO
  → FALLA el caso base

INTENTO 2 — Caso recursivo:
  progenitor(ana, Z), ancestro(Z, pedro)
  
  progenitor(ana, Z):
    madre(ana, carlos) → Z = carlos ✓

  ancestro(carlos, pedro):
    INTENTO 1 — Caso base:
      progenitor(carlos, pedro)?
        padre(carlos, pedro) → ✓   ÉXITO!

Resultado: true
Camino: ana → carlos → pedro
```

### 6.4 ⚠️ El orden de las cláusulas importa

**Caso correcto:** caso base ANTES del recursivo
```prolog
ancestro(X, Y) :- progenitor(X, Y).       % caso base primero ✓
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).
```

**Caso peligroso:** caso recursivo ANTES del base
```prolog
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).  % recursivo primero ⚠️
ancestro(X, Y) :- progenitor(X, Y).
```

En el segundo caso, para `ancestro(ana, carlos)`:
- Intenta el caso recursivo primero → `ancestro(carlos, carlos)` → vuelve a intentar recursivo → loop potencial

La regla de oro: **el caso base siempre primero**.

### 6.5 Comparación: recursión Prolog vs. Python

**Problema:** determinar si X es ancestro de Y en una jerarquía de profundidad arbitraria.

**Python (imperativo/recursivo):**
```python
def es_ancestro(x, y, progenitores):
    """
    progenitores: dict {persona: [lista de hijos]}
    """
    # caso base
    if y in progenitores.get(x, []):
        return True
    # caso recursivo
    for hijo in progenitores.get(x, []):
        if es_ancestro(hijo, y, progenitores):
            return True
    return False

# Para obtener TODAS las respuestas (más trabajo):
def todos_ancestros(y, progenitores):
    resultado = []
    for candidato in progenitores:
        if es_ancestro(candidato, y, progenitores):
            resultado.append(candidato)
    return resultado
```

**Prolog (lógico/declarativo):**
```prolog
ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).

% Obtener todos los ancestros: automático con ?-
?- ancestro(X, pedro).
X = carlos ;
X = ana.
```

**Diferencias fundamentales:**

| Aspecto | Python | Prolog |
|---|---|---|
| Estructura de datos | dict/list | base de conocimiento |
| Control de búsqueda | explícito (for/if) | automático |
| Múltiples resultados | hay que acumularlos | automático con `;` |
| Definición | describe el algoritmo | describe la relación |
| Líneas de código | ~15 | 2 |

---

## 7. Comparación de Paradigmas

### 7.1 Los cuatro paradigmas en un problema

**Problema:** encontrar si alguien es ancestro de otra persona en un árbol genealógico.

**Imperativo (C/Python):**
```python
def es_ancestro(x, y, arbol):
    # Control explícito, estado mutable, algoritmo de búsqueda manual
    cola = [x]
    while cola:
        actual = cola.pop(0)
        if actual == y:
            return True
        cola.extend(arbol.hijos(actual))
    return False
```

**Funcional (Haskell):**
```haskell
-- Transformación recursiva pura sin estado
esAncestro :: Arbol -> Persona -> Persona -> Bool
esAncestro arbol x y =
    y `elem` hijos arbol x ||
    any (\h -> esAncestro arbol h y) (hijos arbol x)
```

**Orientado a Objetos (Java):**
```java
public boolean esAncestro(Persona x, Persona y) {
    // Método en el objeto Persona, encapsula estado
    if (this.equals(x)) return hijos.contains(y);
    return hijos.stream().anyMatch(h -> h.esAncestro(x, y));
}
```

**Lógico (Prolog):**
```prolog
% Declaración de la relación — el resto es automático
ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).
```

### 7.2 Tabla comparativa completa

| | Imperativo | Funcional | OOP | Lógico |
|---|---|---|---|---|
| **Abstracción** | Algoritmo | Función matemática | Objeto/mensaje | Relación/hecho |
| **Estado** | Mutable | Inmutable | Encapsulado | Sin estado |
| **Control de flujo** | Explícito | Por estructura | Por mensajes | Automático |
| **Composición** | Secuenciación | Composición de funciones | Herencia/delegación | Unificación de términos |
| **Paradigma de búsqueda** | Manual | No aplica | No aplica | Backtracking automático |
| **Preguntas múltiples** | Loop manual | Map/filter | Iterator | Natural con `;` |
| **Fortaleza** | Control preciso | Transformaciones | Modelado de sistemas | Relaciones complejas |
| **Debilidad** | Complejidad accidental | Entrada/salida | Sobrediseño | I/O, cálculo numérico |

### 7.3 El continuum declarativo

```
Más imperativo ←────────────────────→ Más declarativo

  C/C++   Java    Python    Haskell    SQL    Prolog
  (cómo)                              (qué)  (qué es verdad)
```

Prolog está en el extremo más declarativo: no solo describe *qué* calcular, sino *qué es verdadero*, y deja el *cómo encontrarlo* completamente al motor.

---

## 8. Ejercicios Resueltos

### Ejercicio R-1: Hermano

**Enunciado:** Definir `hermano(X, Y)` — X e Y son hermanos si comparten al menos un progenitor y son distintos.

**Análisis:**
- Necesitamos "un progenitor P de X" → `progenitor(P, X)`
- Mismo P para Y → `progenitor(P, Y)`  
- X ≠ Y → `X \= Y`

**Solución:**
```prolog
hermano(X, Y) :-
    progenitor(P, X),
    progenitor(P, Y),
    X \= Y.
```

**Prueba:**
```prolog
?- hermano(carlos, beatriz).
true.

?- hermano(X, carlos).
X = beatriz.

?- hermano(laura, Z).
Z = pedro.

?- hermano(laura, laura).
false.    % por el X \= Y
```

**Trazado de `hermano(carlos, beatriz)`:**
```
Meta: hermano(carlos, beatriz)
Regla: hermano(X,Y) :- progenitor(P,X), progenitor(P,Y), X\=Y.
X=carlos, Y=beatriz

progenitor(P, carlos):
  madre(P, carlos) → madre(ana, carlos) → P = ana  ✓

progenitor(ana, beatriz):
  madre(ana, beatriz) → ✓

carlos \= beatriz: ✓

Resultado: true
```

---

### Ejercicio R-2: Tío

**Enunciado:** X es tío de Z si X es hermano de algún progenitor de Z.

**Solución:**
```prolog
tio(X, Z) :-
    hermano(X, Y),
    progenitor(Y, Z).
```

**Verificación:**
```prolog
?- tio(beatriz, laura).
true.
% beatriz es hermana de carlos, carlos es padre de laura

?- tio(X, tomas).
X = carlos.
% carlos es hermano de beatriz, beatriz es madre de tomas
```

---

### Ejercicio R-3: Descendiente (reutilizando ancestro)

**Enunciado:** X es descendiente de Y si Y es ancestro de X.

**Solución:**
```prolog
descendiente(X, Y) :- ancestro(Y, X).
```

Esta solución tiene solo **una cláusula** porque toda la lógica recursiva ya está en `ancestro/2`. Esto ilustra el poder de la composición en Prolog.

**Verificación:**
```prolog
?- descendiente(tomas, ana).
true.

?- descendiente(X, ana).
X = carlos ;
X = beatriz ;
X = laura ;
X = pedro ;
X = tomas.
```

---

## 9. Ejercicios para Resolver

### Nivel Básico

**E-1.** Definir `madre_de_dos(X)` — X es madre de al menos dos personas distintas.
```prolog
madre_de_dos(X) :- ???
```
*Pista: necesitás dos consultas a `madre/2` y una comparación.*

**E-2.** Definir `tiene_hermano(X)` — X tiene al menos un hermano.
```prolog
tiene_hermano(X) :- ???
```

**E-3.** ¿Cuántas respuestas da `?- hermano(X, Y).`? Escribirlas todas sin ejecutar Prolog.

### Nivel Intermedio

**E-4.** Definir `primo(X, Y)` — X e Y son primos si son hijos de hermanos.
```prolog
primo(X, Y) :- ???
```

**E-5.** Definir `bisabuelo(X, Z)` de dos formas:
- Usando `abuelo/2` y `progenitor/2`
- Usando `ancestro/2` con un contador de pasos (más difícil)

**E-6.** Trazar manualmente `?- primo(laura, tomas).` con la base de conocimiento completa.  
*(Primero definir `primo/2`, luego trazar paso a paso)*

### Nivel Avanzado

**E-7.** Definir `familia(X, Y)` — X e Y son familia si comparten algún ancestro.
¿Cuál es el problema con esta definición con la base actual?

**E-8.** Agregar a la base:
```prolog
padre(tomas, lucia).
padre(pedro, martin).
```
Y ahora ejecutar `?- ancestro(ana, X).` ¿Cuántas respuestas hay?  
¿Cuántas habrá con `?- descendiente(X, ana).`?

**E-9. (Desafío)** Definir `camino(X, Y, Camino)` donde `Camino` es la lista de personas por las que pasa la relación de ancestro de X a Y.

---

## 10. Preguntas de Autoevaluación

Usá estas preguntas para verificar tu comprensión. Si no podés responder alguna, volvé a la sección correspondiente.

**Comprensión conceptual:**
1. ¿Cuál es la diferencia fundamental entre un programa imperativo y uno lógico?
2. ¿Por qué se dice que Prolog es un lenguaje "declarativo"?
3. ¿Qué es el Supuesto del Mundo Cerrado? ¿Cuándo puede causar problemas?
4. ¿Qué diferencia hay entre una base de conocimiento Prolog y una base de datos SQL?

**Sintaxis:**
5. ¿Qué diferencia hay entre `ana` y `Ana` en Prolog?
6. ¿Qué significa `:-` en una regla? ¿Y `,`?
7. ¿Cuándo usamos `_` (guión bajo)?
8. ¿Qué significa `X \= Y`?

**Semántica y ejecución:**
9. Describir paso a paso qué hace Prolog al resolver `?- hermano(carlos, X).`
10. ¿Qué pasa si escribimos `hermano(X, Y) :- progenitor(P, X), progenitor(P, Y).` sin `X \= Y`? ¿Qué respuestas extra aparecen?
11. ¿Por qué se pone el caso base antes del recursivo en `ancestro/2`?
12. ¿Qué devuelve `?- madre(X, Y).`? ¿Cuántas soluciones hay?

**Trazado:**
13. Trazar `?- abuelo(beatriz, Z).` con la base de conocimiento familiar.  
*(Nota: en nuestra base, Beatriz no tiene abuelos ni nietos directos — ¿qué devuelve?)*
14. ¿Cuántos pasos de backtracking ocurren en `?- hermano(laura, Z).`?

---

## 11. Bibliografía y Recursos

### Bibliografía Obligatoria

**Sebesta, R.W.** — *Concepts of Programming Languages*, 11ª edición (2016).  
Capítulo 16: Logic Programming Languages, pp. 703–784.  
Cubre: introducción al paradigma, sintaxis Prolog, hechos, reglas, consultas, aritmética, listas, aplicaciones.

**Gabbrielli, M. & Martini, S.** — *Programming Languages: Principles and Paradigms* (2010).  
Capítulo correspondiente a Programación Lógica, pp. 351–423.  
Cubre: fundamentos lógicos, resolución, unificación, semántica operacional de Prolog.

**Louden, K.C. & Lambert, K.A.** — *Programming Languages: Principles and Practice*, 3ª edición (2011).  
Capítulo de Logic Programming.  
Perspectiva más accesible para lectores con background imperativo.

### Bibliografía Complementaria

**Clocksin, W.F. & Mellish, C.S.** — *Programming in Prolog*, 5ª edición (2003).  
El libro clásico de Prolog. Ideal para aprender el lenguaje en profundidad.

**Sterling, L. & Shapiro, E.** — *The Art of Prolog*, 2ª edición (1994).  
Enfoque más avanzado, técnicas de programación en Prolog.

### Recursos Online

- 🌐 **SWISH** — Prolog online, sin instalación: https://swish.swi-prolog.org
- 🖥️ **SWI-Prolog** — Instalación local: https://www.swi-prolog.org/Download.html
- 📚 **Learn Prolog Now!** (gratuito online): http://www.learnprolognow.org/
- 📝 **SWI-Prolog Reference Manual**: https://www.swi-prolog.org/pldoc/
- 🎥 **Tutorial introductorio** (Derek Banas, YouTube): "Prolog Tutorial" — cubre esta clase en ~45 minutos

### Guía de Instalación Rápida — SWI-Prolog

**Windows:**
1. Descargar de https://www.swi-prolog.org/Download.html
2. Ejecutar el instalador `.exe`
3. Abrir "SWI-Prolog" desde el menú inicio

**Primer programa (probar instalación):**
```prolog
% Escribir en un archivo: test.pl
saludo :- write('Hola desde Prolog'), nl.
```
```prolog
?- consult('test.pl').
?- saludo.
Hola desde Prolog
true.
```

---

## Apéndice — Código Completo de la Clase

```prolog
% ═══════════════════════════════════════════════
%  BASE DE CONOCIMIENTO: familia.pl
%  Paradigmas y Lenguajes 2026 — Tema 06 Clase 1
% ═══════════════════════════════════════════════

% ── HECHOS (relaciones primarias) ───────────────
madre(ana,     carlos).
madre(ana,     beatriz).
padre(carlos,  laura).
padre(carlos,  pedro).
madre(beatriz, tomas).

% ── REGLAS NIVEL 1 ──────────────────────────────
progenitor(X, Y) :- madre(X, Y).
progenitor(X, Y) :- padre(X, Y).

% ── REGLAS NIVEL 2 ──────────────────────────────
abuelo(X, Z) :-
    progenitor(X, Y),
    progenitor(Y, Z).

hermano(X, Y) :-
    progenitor(P, X),
    progenitor(P, Y),
    X \= Y.

% ── REGLAS NIVEL 3 ──────────────────────────────
tio(X, Z) :-
    hermano(X, Y),
    progenitor(Y, Z).

% ── RECURSIÓN ───────────────────────────────────
ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).

% ── DERIVADA ────────────────────────────────────
descendiente(X, Y) :- ancestro(Y, X).
```

**Árbol familiar de referencia:**
```
           Ana
          /    \
      Carlos  Beatriz
      /   \       \
  Laura  Pedro   Tomás
```

**Consultas de referencia:**
```prolog
?- abuelo(ana, Z).          % Z = laura; Z = pedro; Z = tomas
?- hermano(carlos, Z).      % Z = beatriz
?- tio(beatriz, Z).         % Z = laura; Z = pedro
?- ancestro(ana, tomas).    % true
?- descendiente(X, ana).    % carlos; beatriz; laura; pedro; tomas
```

---

*Guía generada por: Dra. Sofía (study-guide-writer) — 2026-04-17*  
*Revisión pendiente: writing-validator → coherence-fixer → academic-guardrail*
