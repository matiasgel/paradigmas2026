# Diseño de Tema 06 — Paradigma Lógico: Prolog — Clase 1 de 3: Introducción

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Institución:** UNTDF — Instituto IDEI  
**Docente:** Matías Gel  
**Duración de clase:** 120 minutos  
**Estado:** borrador  
**Fecha de diseño:** 2026-04-17  
**Clase en el ciclo:** 1 de 3 (Introducción)  
**Tema siguiente (clase 2):** Unificación y búsqueda con backtracking  
**Tema siguiente (clase 3):** Listas, recursión y aplicaciones  

---

## 1. Objetivo General de la Clase

Introducir el **paradigma lógico** como forma radicalmente distinta de programar: en lugar de describir *cómo* resolver un problema, se describe *qué* es verdadero sobre el mundo y se deja al motor de inferencia encontrar las respuestas. Al finalizar la clase el alumno debe poder escribir una base de conocimiento simple en Prolog con hechos, reglas y consultas básicas.

---

## 2. Objetivos Específicos (Bloom)

| Nivel | Objetivo |
|-------|----------|
| **Recordar** | Nombrar los tres tipos de enunciados Prolog: hecho, regla, consulta |
| **Comprender** | Explicar qué significa que Prolog "deduce" en lugar de "ejecutar" |
| **Aplicar** | Escribir una base de conocimiento con hechos y reglas y responder consultas simples |
| **Analizar** | Trazar manualmente la resolución de una consulta sobre una base pequeña |
| **Evaluar** | Comparar el paradigma lógico con el imperativo y el funcional en términos de expresividad |

---

## 3. Conocimientos Previos Requeridos

- Paradigma imperativo (Clase 1) — asignación, secuencia, control
- Paradigma funcional (Clases 3–6) — funciones puras, sin estado
- Noción básica de proposición lógica (si… entonces…)
- Familiaridad con Python o TypeScript como referencia comparativa

---

## 4. Estructura de la Clase (120 min)

| Bloque | Duración | Contenido | Tipo |
|--------|----------|-----------|------|
| **B1** | 15 min | Motivación: ¿Qué es programar declarativamente? El problema de la base de datos de relaciones | Exposición + pregunta |
| **B2** | 20 min | Fundamentos: Cálculo de predicados y cláusulas de Horn (conceptual, no formal) | Exposición con ejemplos |
| **B3** | 25 min | Prolog: hechos, reglas y consultas — sintaxis y primeros ejemplos EN CLASE | Demostración en vivo |
| **B4** | 25 min | Ejemplos paso a paso con trazado manual de resolución | Pizarrón + participación |
| **B5** | 10 min | Comparación con paradigmas previos | Discusión guiada |
| **B6** | 10 min | Ejercicios rápidos en clase | Práctica guiada |
| **B7** | 15 min | Cierre, resumen, preguntas y anticipo Clase 2 | Cierre |

---

## 5. Contenidos Detallados

### 5.1 Bloque 1 — Motivación (15 min)

**Problema motivador:**  
"Tengo una familia: Ana es madre de Carlos. Carlos es padre de Laura. ¿Cómo escribo en Python una función que, dada cualquier persona, encuentre todos sus abuelos?"

Mostrar cómo en Python se necesita lógica explícita de búsqueda. Luego mostrar que en Prolog alcanza con declarar las relaciones.

> *"Logic programs are sets of statements that represent facts and rules about some problem. An execution of a logic program is a proof that a goal statement follows from the program statements."*  
> — Sebesta, *Concepts of Programming Languages*, Cap. 16

**Punto clave:** en Prolog no se programa el *algoritmo*, se programa el *conocimiento*.

---

### 5.2 Bloque 2 — Fundamentos conceptuales (20 min)

#### 5.2.1 Cálculo de Predicados (informal)

Un **predicado** expresa una propiedad o relación:
- `esMadre(ana, carlos)` — "Ana es madre de Carlos"
- `mayor(5, 3)` — "5 es mayor que 3"

Una **proposición** puede ser:
- Un hecho atómico: `pez(trucha)`
- Una implicación: `si pez(X) entonces animal(X)`

#### 5.2.2 Cláusulas de Horn

Las cláusulas de Horn son la base matemática de Prolog:

```
Head :- Body1, Body2, ..., BodyN.
```

Significa: **Head es verdadero SI Body1 Y Body2 Y … Y BodyN son verdaderos**.

Caso especial — hecho (sin cuerpo):
```prolog
pez(trucha).
```

Esto es una cláusula de Horn "sin antecedente" — incondicionalmente verdadero.

> *"Prolog has two basic statement forms; these correspond to the headless and headed Horn clauses of predicate calculus."*  
> — Sebesta, Cap. 16

---

### 5.3 Bloque 3 — Prolog: Sintaxis básica (25 min)

**Todo en Prolog termina con punto `.`**

#### ⚠️ Distinción clave: BASE DE CONOCIMIENTO vs. INFERENCIA

Antes de ver código, dejar en claro la separación conceptual:

| | Base de conocimiento | Inferencia (consulta) |
|---|---|---|
| **¿Qué es?** | El "programa" Prolog — hechos y reglas | La "pregunta" que le hacemos al motor |
| **¿Quién lo escribe?** | El programador, en un archivo `.pl` | El usuario, en el intérprete (`?-`) |
| **¿Cuándo se ejecuta?** | Al cargar el archivo (`:- consult(...)`) | Cuando se lanza la consulta |
| **Ejemplo** | `madre(ana, carlos).` | `?- madre(ana, X).` |
| **Analogía** | Escribir las reglas del juego | Jugar una partida |

**En vivo — mostrar los DOS momentos:**

```prolog
% ── MOMENTO 1: creamos la base (archivo familia.pl) ──────────────
madre(ana, carlos).
madre(ana, beatriz).
padre(carlos, laura).
progenitor(X, Y) :- madre(X, Y).
progenitor(X, Y) :- padre(X, Y).
abuelo(X, Z)     :- progenitor(X, Y), progenitor(Y, Z).

% ── MOMENTO 2: cargamos y consultamos (en el intérprete) ─────────
% ?- consult('familia.pl').   ← carga la base
% true.
%
% ?- madre(ana, carlos).      ← inferencia: ¿es esto verdadero?
% true.
%
% ?- abuelo(ana, Z).          ← inferencia: ¿quiénes son nietos de Ana?
% Z = laura.
```

> **Punto clave:** La base de conocimiento no "hace nada" sola. El motor solo actúa cuando recibe una **consulta**. Esta separación es lo que hace a Prolog declarativo: yo describo el mundo, tú buscás la prueba.

**Pregunta a la clase:** "Si agrego un nuevo hecho a la base después de cargarla, ¿cómo lo considera Prolog en la siguiente consulta?" *(Respuesta: hay que recargar o usar `assert/1`)*

---

#### 5.3.1 Términos en Prolog

| Tipo | Ejemplo | Nota |
|------|---------|------|
| Átomo | `ana`, `carlos`, `trucha` | minúscula o entre comillas |
| Número | `42`, `3.14` | |
| Variable | `X`, `Persona`, `_` | MAYÚSCULA o `_` |
| Estructura | `f(a, b)` | funtor + argumentos |

**Ejemplo en clase — paso a paso:**
```prolog
% ¿Qué es un átomo?
ana          % átomo (nombre propio en minúscula)
'Ana López'  % átomo entre comillas (puede tener espacios)

% ¿Qué es una variable?
X      % variable — Prolog la instanciará durante la consulta
_      % variable anónima — "no me importa el valor"
```

#### 5.3.2 Hechos

Un hecho declara algo verdadero incondicionalmente.

```prolog
% Base de conocimiento: familia
madre(ana, carlos).        % Ana es madre de Carlos
madre(ana, beatriz).       % Ana es madre de Beatriz
padre(carlos, laura).      % Carlos es padre de Laura
padre(carlos, pedro).      % Carlos es padre de Pedro
```

**Ejercicio en clase:** "¿Cómo agrego que Beatriz es madre de Tomás?"

```prolog
madre(beatriz, tomas).
```

#### 5.3.3 Reglas

Una regla define relaciones derivadas a partir de hechos.

```prolog
% X es progenitor de Y si X es madre de Y
progenitor(X, Y) :- madre(X, Y).

% X es progenitor de Y si X es padre de Y  
progenitor(X, Y) :- padre(X, Y).

% X es abuelo de Z si X es progenitor de Y, e Y es progenitor de Z
abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
```

**Lectura en voz alta de la regla `abuelo`:**  
"X es abuelo de Z si existe algún Y tal que X es progenitor de Y **y** Y es progenitor de Z."

#### 5.3.4 Consultas

En el intérprete Prolog, las consultas se hacen con `?-`:

```prolog
?- madre(ana, carlos).
true.

?- madre(ana, X).
X = carlos ;
X = beatriz.

?- abuelo(ana, Z).
Z = laura ;
Z = pedro ;
Z = tomas.
```

**Demostración en vivo:** abrir SWI-Prolog, cargar la base, ejecutar cada consulta.

---

### 5.4 Bloque 4 — Trazado manual de resolución (25 min)

Este bloque es el más importante. Se hace en el pizarrón, paso a paso, con participación del alumno.

#### Ejemplo 1 — Consulta simple: `?- madre(ana, carlos).`

```
Meta: madre(ana, carlos)

Busco en la base:
  Cláusula 1: madre(ana, carlos).  ← ¡Calza! (unifica con la meta)

Resultado: true
```

#### Ejemplo 2 — Consulta con variable: `?- madre(ana, X).`

```
Meta: madre(ana, X)

Busco en la base (de arriba a abajo):
  Cláusula 1: madre(ana, carlos).  ← Calza con X = carlos
    → Respuesta: X = carlos. (¿más soluciones? usuario pide ;)

  Cláusula 2: madre(ana, beatriz). ← Calza con X = beatriz
    → Respuesta: X = beatriz. (¿más soluciones? usuario pide ;)

  Cláusula 3: madre(beatriz, tomas). ← NO calza (primer arg es beatriz, no ana)

No hay más cláusulas. FIN.
```

**Concepto clave:** Prolog prueba cláusulas **en orden**, de arriba a abajo.

#### Ejemplo 3 — Regla derivada: `?- abuelo(ana, Z).`

```
Meta: abuelo(ana, Z)

Busco regla para abuelo:
  Regla: abuelo(X, Z) :- progenitor(X, Y), progenitor(Y, Z).
  Unifica: X = ana, Z libre

  Nueva meta: progenitor(ana, Y), progenitor(Y, Z)

  → Resuelvo progenitor(ana, Y):
      Regla 1: progenitor(X,Y) :- madre(X,Y). → madre(ana, Y)
        Cláusula 1: madre(ana, carlos) → Y = carlos ✓

  → Resuelvo progenitor(carlos, Z):
      Regla 2: progenitor(X,Y) :- padre(X,Y). → padre(carlos, Z)
        Cláusula: padre(carlos, laura) → Z = laura ✓
        → Respuesta: Z = laura

      Continúa: padre(carlos, pedro) → Z = pedro ✓
        → Respuesta: Z = pedro

  → Vuelvo: progenitor(ana, Y) con Y = beatriz
      madre(ana, beatriz) ✓
      progenitor(beatriz, Z) → madre(beatriz, tomas) → Z = tomas ✓
        → Respuesta: Z = tomas
```

**Diagrama en pizarrón:** árbol de derivación con las 3 ramas.

#### Ejemplo 4 — Recursión: `ancestro/2`

Este ejemplo introduce **recursión en Prolog** — uno de los mecanismos más poderosos y fundamentales.

**Problema:** la regla `abuelo` solo funciona para 2 generaciones. ¿Cómo escribimos una regla que encuentre *cualquier* antepasado, sin importar cuántas generaciones haya?

```prolog
% Caso base: X es ancestro de Y si X es progenitor directo de Y
ancestro(X, Y) :- progenitor(X, Y).

% Caso recursivo: X es ancestro de Y si X es progenitor de Z
%                 y Z es ancestro de Y
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).
```

**Lectura en voz alta:**
- Caso base: "X es ancestro de Y si X es su progenitor directo."
- Caso recursivo: "X es ancestro de Y si X es progenitor de alguien (Z) que a su vez es ancestro de Y."

**Trazado en pizarrón — `?- ancestro(ana, pedro).`:**

```
Meta: ancestro(ana, pedro)

① Pruebo caso base: progenitor(ana, pedro)
   → madre(ana, pedro)? NO
   → padre(ana, pedro)?  NO  ← falla

② Pruebo caso recursivo: progenitor(ana, Z), ancestro(Z, pedro)
   → progenitor(ana, Z):
       madre(ana, carlos) → Z = carlos ✓

   → ancestro(carlos, pedro):
       ① caso base: progenitor(carlos, pedro)
           padre(carlos, pedro) → ✓  ← ¡ÉXITO!

Resultado: true
```

**Comparación con funcional** (mostrar en pantalla):
```python
# Python / TypeScript: necesitás un loop o función explícita
def es_ancestro(persona, objetivo, relaciones):
    directos = [h for p, h in relaciones if p == persona]
    if objetivo in directos:
        return True
    return any(es_ancestro(d, objetivo, relaciones) for d in directos)
```

```prolog
% Prolog: la recursión emerge de las reglas mismas
ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :- progenitor(X, Z), ancestro(Z, Y).
```

> **Punto clave:** En Prolog la recursión no es un truco de control — es la forma natural de expresar relaciones transitivas. El motor maneja el stack automáticamente.

**⚠️ Advertencia:** ¿Qué pasa si ponemos el caso recursivo *antes* que el caso base? → riesgo de bucle infinito. El **orden importa**. Esto se profundiza en Clase 2 con backtracking.

---

### 5.5 Bloque 5 — Comparación de paradigmas (10 min)

| Aspecto | Imperativo | Funcional | Lógico |
|---------|-----------|-----------|--------|
| ¿Qué describe? | Cómo ejecutar | Cómo transformar | Qué es verdadero |
| Unidad básica | Instrucción | Función | Cláusula (hecho/regla) |
| Estado | Mutable | Inmutable | Sin estado |
| Control | Explícito | Por estructura | Automático (motor) |
| Ejemplo base | `if/while/for` | `map/filter/reduce` | `madre(X,Y) :- ...` |
| Lenguaje típico | Python, C | Haskell, TypeScript | Prolog |

**Pregunta para la clase:** "¿Qué tipo de problemas creen que se resuelven mejor con Prolog?"  
*(Respuestas esperadas: bases de datos relacionales, sistemas expertos, resolución de puzzles, parsing)*

---

### 5.6 Bloque 6 — Ejercicios rápidos (10 min)

**Ejercicio 1:** Agregar a la base de familia la relación `hermano(X, Y)`.  
Pista: X e Y son hermanos si tienen el mismo progenitor y X ≠ Y.

```prolog
% Solución:
hermano(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y.
```

**Ejercicio 2:** ¿Qué devuelve `?- hermano(carlos, Z).`? Trazar a mano.

**Ejercicio 3:** Definir `tio(X, Z)` (X es tío de Z si X es hermano de un progenitor de Z).

**Ejercicio 4 — Recursión:** Definir `descendiente(X, Y)` (X es descendiente de Y si Y es ancestro de X). ¿Cuántas cláusulas necesitás? ¿Podés reutilizar `ancestro/2`?

```prolog
% Solución:
descendiente(X, Y) :- ancestro(Y, X).
```

**Reflexión:** "¿Por qué esta definición funciona con una sola cláusula?"

---

### 5.7 Bloque 7 — Cierre (15 min)

**Resumen de la clase:**
1. Prolog = declarar conocimiento, no escribir algoritmos
2. Tres elementos: hechos, reglas, consultas
3. El motor de Prolog busca pruebas automáticamente
4. La base se lee de arriba a abajo; las variables se instancian durante la búsqueda

**Anticipo Clase 2:**
- ¿Qué pasa cuando hay múltiples soluciones? → **Backtracking**
- ¿Cómo funciona `\=` y por qué X \= X falla? → **Unificación profunda**
- Estructuras compuestas y listas

**Pregunta de salida:**  
"Escribí en papel una regla Prolog para `bisabuelo(X, Z)`. ¿Cuántas cláusulas necesitás?"

---

## 6. Ejemplos de Filminas Propuestos (referencia para class-writer)

| F# | Título | Contenido clave |
|----|--------|-----------------|
| F-01 | Paradigma Lógico: Introducción | Motivación, diferencia con imperativo/funcional |
| F-02 | El problema que resuelve Prolog | Ejemplo familia en Python vs Prolog |
| F-03 | Cálculo de Predicados (informal) | Predicado, proposición, implicación |
| F-04 | Cláusulas de Horn | Sintaxis `Head :- Body`, ejemplos |
| F-05 | Términos en Prolog | Tabla: átomo, número, variable, estructura |
| F-06 | Hechos en Prolog | Código + explicación |
| F-07 | Reglas en Prolog | `progenitor`, `abuelo` con lectura en voz alta |
| F-08 | Consultas en Prolog | Ejemplos con respuestas, el `;` para más soluciones |
| F-09 | Trazado Ejemplo 1 | `?- madre(ana, carlos).` paso a paso |
| F-10 | Trazado Ejemplo 2 | `?- madre(ana, X).` con variable |
| F-11 | Trazado Ejemplo 3 | `?- abuelo(ana, Z).` árbol de derivación |
| F-12 | Recursión en Prolog | `ancestro/2`: caso base + caso recursivo, trazado, comparación con Python |
| F-13 | Comparación de Paradigmas | Tabla imperativo / funcional / lógico |
| F-14 | Ejercicios en clase | `hermano`, `tio`, `descendiente` |
| F-15 | Resumen y anticipo Clase 2 | Los 3 conceptos clave + preview backtracking |

---

## 7. Recursos y Bibliografía

### Material de la materia (filminas)
- `06 programacion logica` — cubre hechos, reglas, consultas, unificación, calce de términos

### Libros de referencia (en `ingesta/`)

| Libro | Capítulo relevante |
|-------|--------------------|
| **Sebesta** — *Concepts of Programming Languages* (Pearson 2019) | Cap. 16: Logic Programming Languages (pp. 703–784) |
| **Gabbrielli & Martini** — *Programming Languages: Principles and Paradigms* (Springer 2023) | Cap. sobre Programación Lógica (pp. 351–423) |
| **Louden & Lambert** — *Programming Languages: Principles and Practices* (Course Technology 2011) | Cap. de Programación Lógica |

### Software para la clase
- [SWI-Prolog](https://www.swi-prolog.org/) — intérprete de referencia, gratuito, multiplataforma
- SWISH online: https://swish.swi-prolog.org/ (sin instalación)

---

## 8. Notas Pedagógicas

- **Énfasis en ejemplos:** cada concepto nuevo debe ir seguido inmediatamente de un ejemplo Prolog concreto que el docente escribe en vivo.
- **Trazado en pizarrón es obligatorio:** los ejemplos 1, 2 y 3 del B4 deben hacerse en el pizarrón con participación de estudiantes ("¿qué cláusula calza ahora?").
- **No formalizar el cálculo de predicados:** el B2 es conceptual. La formalización lógica es optativa; el foco es la intuición.
- **Ritmo de ejemplos:** ~1 ejemplo cada 5–7 minutos en los bloques 3 y 4.
- **Variable de clase:** si los alumnos están confundidos con la notación, extender B3 y reducir B5.
- **Preguntas frecuentes anticipadas:**
  - "¿Por qué `X` con mayúscula?" → Convención Prolog: mayúscula = variable, minúscula = átomo
  - "¿Puede haber ciclos?" → Sí, son un problema — se ve en Clase 2 con backtracking
  - "¿Prolog se usa en la industria?" → Sí: Erlang derivó de él, Watson de IBM usó lógica, PLCs, sistemas expertos

---

## 9. Restricciones de Tiempo

- **Clase 1 (esta):** solo hechos, reglas, consultas simples y trazado básico. **No** unificación profunda, **no** backtracking, **no** listas.
- **Clase 2:** unificación, backtracking, corte (`!`), aritmética.
- **Clase 3:** listas, recursión, aplicaciones (puzzles, bases de datos).

---

*Tema 06 — Diseñado por: Lic. Marcos (topic-designer) — 2026-04-17*  
*Estado: BORRADOR — pendiente de aprobación del docente*
