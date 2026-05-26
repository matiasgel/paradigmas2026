---
exam_type: "parcial-1"
course_id: "2026"
status: "assembled"
total_questions: 30
points: 100
duration_minutes: 60
generated_at: "2026-05-25"
---

# PARCIAL 1 — Paradigmas y Lenguajes de Programación 2026
## UNTDF — Instituto de Industria, Economía e Ingeniería (IDEI)

**Docente:** Matías Gel  
**Modalidad:** Quiz en clase | **Duración:** 60 minutos  
**Tipo:** Opción múltiple (4 opciones por pregunta)  
**Total:** 30 preguntas | **Puntaje máximo:** 100 pts | **Aprobación:** ≥ 60 pts  

> **Instrucciones:** Seleccioná UNA sola opción por pregunta. No hay respuestas trampa — todas las preguntas son sobre conceptos fundamentales vistos en clase.

---

# Preguntas — Tema 02: Sintaxis y Semántica

---

## P-02-001 | Recordar | Conceptual | 3 pts

**¿Cuál de las siguientes afirmaciones describe correctamente la diferencia entre sintaxis y semántica de un lenguaje de programación?**

a) La sintaxis define el significado de los programas; la semántica define su forma correcta  
b) La sintaxis define las reglas de forma que determinan si un programa está bien construido; la semántica define el significado de los programas  
c) La sintaxis y la semántica son equivalentes: un error en una implica un error en la otra  
d) La semántica es responsabilidad del programador; la sintaxis es responsabilidad del compilador  

**Respuesta correcta:** b  
**Justificación:** La sintaxis establece las reglas formales (gramática) que determinan qué secuencias de tokens son programas válidos. La semántica determina qué significan esos programas — qué efecto computacional tienen. Un programa puede ser sintácticamente correcto y semánticamente incorrecto (por ejemplo, sumar un entero con un booleano pasa la gramática pero viola el sistema de tipos).  
**Fuente:** minuta.md §BLOQUE 1 — Definición de sintaxis (F-03) y Definición de semántica (F-04)  
**Bloom:** Recordar  
**Nivel de dificultad:** Básica — 4to año

---

## P-02-002 | Comprender | Conceptual | 3 pts

**Considerá el siguiente programa TypeScript:**

```typescript
function suma(a: number, b: number): number {
  return a + b;
}

const resultado = suma(10, "hola");
```

**¿En qué nivel es incorrecto este programa y por qué?**

a) Es incorrecto sintácticamente: la llamada `suma(10, "hola")` no respeta la gramática de TypeScript  
b) Es incorrecto semánticamente: pasa el análisis de forma, pero viola las reglas de tipo al pasar un `string` donde se espera un `number`  
c) Es correcto tanto sintáctica como semánticamente: TypeScript acepta cualquier valor en una llamada a función  
d) Es incorrecto léxicamente: el string `"hola"` no es un token válido en TypeScript  

**Respuesta correcta:** b  
**Justificación:** El programa está sintácticamente bien formado — todas las construcciones respetan la gramática del lenguaje. El error es semántico (específicamente, de semántica estática / chequeo de tipos): el segundo argumento es `string` pero el parámetro `b` está declarado como `number`. TypeScript detecta este error en tiempo de compilación a través del sistema de tipos.  
**Fuente:** minuta.md §BLOQUE 1 — Punto de tensión (F-04), Errores de tipo en TypeScript (F-06b)  
**Bloom:** Comprender  
**Nivel de dificultad:** Media — 4to año

---

# Preguntas — Tema 03: Introducción a Programación Funcional con TypeScript

---

## P-03-001 | Recordar | Conceptual | 3 pts

**¿Cuáles son los tres pilares del paradigma de programación funcional?**

a) Herencia, polimorfismo y encapsulamiento  
b) Secuencia, selección e iteración  
c) Funciones puras, inmutabilidad y transparencia referencial  
d) Abstracción, modularidad y encapsulamiento  

**Respuesta correcta:** c  
**Justificación:** Los tres pilares del paradigma funcional son: (1) **funciones puras** — siempre producen el mismo resultado para los mismos argumentos sin efectos colaterales; (2) **inmutabilidad** — los valores no se modifican después de ser creados; (3) **transparencia referencial** — una expresión puede ser reemplazada por su valor sin cambiar el comportamiento del programa.  
**Fuente:** minuta.md §BLOQUE B — Tres pilares del funcional (OA-2)  
**Bloom:** Recordar  

---

## P-03-002 | Comprender | Conceptual | 3 pts

**El λ-cálculo de Alonzo Church y la Máquina de Turing de Alan Turing (ambos de 1936) demostraron ser equivalentes en poder computacional. Sin embargo, representan modelos conceptualmente distintos de qué es "computar". ¿Cuál es la diferencia fundamental entre ambos modelos?**

a) La Máquina de Turing opera sobre números enteros; el λ-cálculo opera sobre funciones de orden superior  
b) La Máquina de Turing define la computación como modificación secuencial de estado (cinta); el λ-cálculo define la computación como sustitución/reescritura de expresiones  
c) La Máquina de Turing es determinista; el λ-cálculo es no determinista  
d) El λ-cálculo requiere hardware especializado; la Máquina de Turing se puede ejecutar en cualquier computadora  

**Respuesta correcta:** b  
**Justificación:** La Máquina de Turing modela el cómputo como una secuencia de operaciones que modifican el estado de una cinta (registro, memoria). Es la base conceptual del paradigma imperativo. El λ-cálculo modela el cómputo como β-reducción: sustituir una expresión por su equivalente sin ningún estado mutable. Es la base conceptual del paradigma funcional. Ambos tienen el mismo poder expresivo (tesis Church-Turing) pero desde visiones radicalmente distintas.  
**Fuente:** minuta.md §BLOQUE A0 — Church vs Turing (F-03, F-04)  
**Bloom:** Comprender  

---

## P-03-003 | Comprender | Conceptual | 3 pts

**¿Qué significa que una función tiene "transparencia referencial"?**

a) Que la función puede recibir otras funciones como argumentos  
b) Que el nombre de la función refleja claramente lo que hace  
c) Que la función puede ser reemplazada por su valor de retorno en cualquier parte del código sin cambiar el comportamiento del programa  
d) Que la función no usa variables globales pero sí puede modificar sus argumentos  

**Respuesta correcta:** c  
**Justificación:** Transparencia referencial significa que una expresión (llamada a función incluida) puede ser sustituida por su resultado en cualquier contexto sin alterar el comportamiento del programa. Esto solo es posible si la función es pura — sin efectos colaterales. Ejemplo: si `doble(3)` siempre devuelve `6`, entonces `doble(3) + 1` y `6 + 1` son intercambiables en cualquier lugar del código.  
**Fuente:** minuta.md §BLOQUE B — Transparencia referencial (OA-2)  
**Bloom:** Comprender  

---

## P-03-004 | Aplicar | Con código | 4 pts

**Considerá el siguiente código TypeScript en estilo funcional:**

```typescript
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const resultado = numeros
  .filter(n => n % 2 === 0)
  .map(n => n * n);
```

**¿Qué contiene `resultado` después de ejecutar este código?**

a) `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` — los cuadrados de todos los números  
b) `[2, 4, 6, 8, 10]` — los números pares del arreglo original  
c) `[4, 16, 36, 64, 100]` — los cuadrados de los números pares  
d) `[1, 3, 5, 7, 9]` — los números impares del arreglo original  

**Respuesta correcta:** c  
**Justificación:** `filter(n => n % 2 === 0)` selecciona los números pares: `[2, 4, 6, 8, 10]`. Luego `map(n => n * n)` aplica la función cuadrado a cada elemento: `[4, 16, 36, 64, 100]`. La composición de `filter` y `map` es una cadena de transformaciones sin mutación del arreglo original.  
**Fuente:** minuta.md §BLOQUE C — map, filter, reduce en TypeScript (OA-4)  
**Bloom:** Aplicar  

---

## P-03-005 | Analizar | Con código | 4 pts

**Considerá las siguientes dos funciones en TypeScript:**

```typescript
// Función A
let contador = 0;
const incrementarA = (x: number): number => {
  contador++;
  return x + 1;
};

// Función B
const incrementarB = (x: number): number => {
  return x + 1;
};
```

**¿Cuál de las siguientes afirmaciones es correcta respecto a la pureza de estas funciones?**

a) Ambas son funciones puras porque las dos devuelven `x + 1`  
b) `incrementarA` es pura porque su resultado `x + 1` no depende de `contador`; `incrementarB` también es pura  
c) `incrementarA` no es una función pura porque modifica la variable externa `contador`, produciendo un efecto colateral; `incrementarB` sí es pura  
d) Ninguna es pura porque TypeScript no soporta funciones puras nativas  

**Respuesta correcta:** c  
**Justificación:** `incrementarA` viola la pureza en dos sentidos: (1) modifica una variable externa (`contador++`) — eso es un **efecto colateral**; (2) aunque su valor de retorno `x + 1` no varía, cada llamada tiene un impacto observable fuera de la función. `incrementarB` es una función pura: mismo input → mismo output, sin efectos en el entorno. La pureza requiere ausencia total de efectos colaterales, no solo consistencia en el valor de retorno.  
**Fuente:** minuta.md §BLOQUE B — Funciones puras (OA-3, OA-5)  
**Bloom:** Analizar

---

# Preguntas — Tema 04: Aspectos Avanzados de Programación Funcional

---

## P-04-001 | Recordar | Conceptual | 3 pts

**¿Qué es una función de orden superior (Higher Order Function — HOF)?**

a) Una función que solo opera sobre tipos numéricos  
b) Una función que recibe otra función como argumento y/o devuelve una función como resultado  
c) Una función que utiliza recursión para resolver un problema  
d) Una función declarada con `function` en lugar de arrow function en TypeScript  

**Respuesta correcta:** b  
**Justificación:** Una función de orden superior (HOF) es aquella que trata las funciones como valores: puede recibirlas como parámetros y/o retornarlas como resultado. Ejemplos canónicos: `map(f, lista)` recibe `f` como argumento; `compose(f, g)` devuelve una nueva función. Esto es posible porque en el paradigma funcional las funciones son valores de primera clase.  
**Fuente:** minuta.md §BLOQUE 1 — [F-05] Anatomía de una HOF (OA-1)  
**Bloom:** Recordar  

---

## P-04-002 | Comprender | Conceptual | 3 pts

**¿Cuál es la diferencia fundamental entre partial application y currying?**

a) Partial application convierte una función en una función currificada; currying aplica parcialmente sus argumentos  
b) Partial application fija uno o más argumentos de una función devolviendo una función con menos parámetros; currying transforma una función de N argumentos en una cadena de N funciones de un argumento cada una  
c) Son el mismo concepto expresado en distintos lenguajes: partial en Clojure y currying en TypeScript  
d) Currying siempre requiere especificar todos los argumentos de una vez; partial application permite aplicarlos en cualquier orden  

**Respuesta correcta:** b  
**Justificación:** **Partial application** fija algunos argumentos de una función y devuelve una nueva función que espera el resto. Ejemplo: `const add5 = add.bind(null, 5)` fija el primer argumento. **Currying** convierte `f(a, b, c)` en `f(a)(b)(c)` — una cadena de funciones unarias. La diferencia clave: en partial application podés fijar cualquier cantidad de argumentos; en currying siempre se aplica un argumento por vez en una cadena estricta.  
**Fuente:** minuta.md §BLOQUE 2 — [F-13] Partial application vs [F-16] Currying (OA-4)  
**Bloom:** Comprender  

---

## P-04-003 | Comprender | Conceptual | 3 pts

**`compose(f, g)(x)` y `pipe(f, g)(x)` aplican las mismas funciones `f` y `g` sobre `x`, pero en distinto orden. ¿Cuál de las siguientes afirmaciones es correcta?**

a) `compose(f, g)(x)` aplica `f` primero y luego `g`; `pipe(f, g)(x)` aplica `g` primero y luego `f`  
b) `compose(f, g)(x)` es equivalente a `f(g(x))` — se aplica de derecha a izquierda; `pipe(f, g)(x)` es equivalente a `g(f(x))` — se aplica de izquierda a derecha  
c) Ambos producen el mismo resultado porque la composición es conmutativa  
d) `compose` solo existe en Clojure; `pipe` solo existe en TypeScript  

**Respuesta correcta:** b  
**Justificación:** `compose(f, g)(x) = f(g(x))`: primero se aplica `g`, luego `f` (notación matemática: de derecha a izquierda). `pipe(f, g)(x) = g(f(x))`: primero se aplica `f`, luego `g` (lectura de izquierda a derecha, más natural en código). Son equivalentes solo si `f = g`. En general, `compose(f, g) ≠ pipe(f, g)` a menos que `f` y `g` conmuten.  
**Fuente:** minuta.md §BLOQUE 1 — [F-06] compose vs pipe (OA-2)  
**Bloom:** Comprender  

---

## P-04-004 | Aplicar | Con código | 4 pts

**Dado el siguiente código TypeScript:**

```typescript
const trim = (s: string): string => s.trim();
const toLower = (s: string): string => s.toLowerCase();
const addDomain = (s: string): string => s + "@untdf.edu.ar";

const pipe = <T>(...fns: Array<(x: T) => T>) => (x: T) =>
  fns.reduce((acc, fn) => fn(acc), x);

const normalizeEmail = pipe(trim, toLower, addDomain);

console.log(normalizeEmail("  MATIAS  "));
```

**¿Qué imprime este código?**

a) `"  MATIAS  @untdf.edu.ar"` — `pipe` no aplica `trim` porque está primero  
b) `"matias@untdf.edu.ar"` — se aplican `trim`, luego `toLower`, luego `addDomain` en orden  
c) `"MATIAS@UNTDF.EDU.AR"` — `toLower` se aplica solo al resultado de `trim`, no a `addDomain`  
d) Error de compilación — `pipe` no acepta funciones de tipo `string => string`  

**Respuesta correcta:** b  
**Justificación:** `pipe` aplica las funciones de izquierda a derecha usando `reduce`. Traza: `"  MATIAS  "` → `trim` → `"MATIAS"` → `toLower` → `"matias"` → `addDomain` → `"matias@untdf.edu.ar"`. Cada función recibe como input el output de la anterior. El tipo es `string => string` en toda la cadena, compatible con la implementación genérica de `pipe`.  
**Fuente:** minuta.md §BLOQUE 1 — [F-07] pipe en TypeScript (OA-2)  
**Bloom:** Aplicar  

---

## P-04-005 | Analizar | Con código | 4 pts

**Considerá esta implementación de `factorial` en TypeScript:**

```typescript
// Versión A
const factorialA = (n: number): number => {
  if (n <= 1) return 1;
  return n * factorialA(n - 1);
};

// Versión B
const factorialB = (n: number, acc: number = 1): number => {
  if (n <= 1) return acc;
  return factorialB(n - 1, n * acc);
};
```

**¿Por qué `factorialB` es preferible a `factorialA` desde la perspectiva del paradigma funcional?**

a) `factorialB` es más legible porque usa un parámetro con valor por defecto  
b) `factorialA` usará menos memoria porque no necesita el acumulador; `factorialB` es más lenta  
c) `factorialB` implementa recursión de cola: la llamada recursiva es la última operación, lo que permite que el runtime optimice la pila (TCO); `factorialA` acumula marcos de stack porque necesita multiplicar por `n` al regresar  
d) Ambas son equivalentes en términos de eficiencia — TypeScript optimiza la recursión automáticamente  

**Respuesta correcta:** c  
**Justificación:** En `factorialA`, la última operación es `n * factorialA(n-1)` — hay un cálculo pendiente al retornar, por lo que cada llamada recursiva debe mantenerse en el stack. Para `n` grande, esto causa stack overflow. `factorialB` usa **tail recursion**: la llamada recursiva `factorialB(n-1, n*acc)` es la última operación, y el resultado se acumula en `acc`. Esto permite que runtimes con TCO (Clojure con `recur`) reutilicen el mismo frame de stack. TypeScript no garantiza TCO nativo, pero el patrón de acumulador es correcto funcionalmente.  
**Fuente:** minuta.md §BLOQUE 3 — [F-24 a F-27] Recursión de cola (OA-7)  
**Bloom:** Analizar

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

---

# Preguntas — Tema 07: Paradigma Lógico — Prolog II+III

---

## P-07-001 | Recordar | Conceptual | 3 pts

**¿Qué es la unificación en Prolog?**

a) Un algoritmo de búsqueda que recorre el árbol de soluciones de izquierda a derecha  
b) El proceso de calcular el valor numérico de una expresión aritmética  
c) El proceso de encontrar una sustitución de variables que haga que dos términos sean sintácticamente idénticos  
d) La técnica de ordenar los hechos en la base de conocimiento para optimizar las consultas  

**Respuesta correcta:** c  
**Justificación:** La unificación es el mecanismo central de Prolog: dados dos términos, busca la sustitución más general (MGU — Most General Unifier) que los haga iguales sintácticamente. No evalúa, no computa numéricamente — solo hace "matching con variables". Ejemplo: `f(X, b)` unifica con `f(a, Y)` bajo la sustitución `{X=a, Y=b}`.  
**Fuente:** minuta.md §BLOQUE 1 — Unificación (F-006 a F-023)  
**Bloom:** Recordar  

---

## P-07-002 | Comprender | Conceptual | 3 pts

**En Prolog, si ejecutamos `?- X = 2 + 3.`, el motor responde `X = 2+3` sin evaluar la suma. ¿Por qué?**

a) Porque Prolog no tiene operadores aritméticos  
b) Porque `=` realiza unificación, no evaluación. `2+3` es una estructura `+(2,3)` que se unifica como término; para evaluar numéricamente se usa `is/2`  
c) Porque `X` es una variable entera y no puede contener una expresión  
d) Porque la unificación en Prolog es lazy y solo evalúa cuando se necesita el resultado  

**Respuesta correcta:** b  
**Justificación:** En Prolog `=` es el predicado de unificación. `2+3` no es "dos más tres" sino la estructura de término `+(2,3)` — un functor `+` con dos argumentos. La unificación simplemente liga `X` a esa estructura. Para evaluar aritméticamente se usa `is/2`: `?- X is 2+3.` da `X = 5`. Esta distinción entre estructura y evaluación es fundamental en Prolog.  
**Fuente:** minuta.md §BLOQUE 1 — `=` vs `==` vs `is` (F-015, F-016)  
**Bloom:** Comprender  

---

## P-07-003 | Comprender | Conceptual | 3 pts

**¿Qué es un "choice point" (punto de elección) en el backtracking de Prolog?**

a) El punto del programa donde el programador declara que hay una sola solución posible  
b) Una marca que el motor crea cuando encuentra múltiples cláusulas que pueden unificar con el goal actual, guardando las alternativas para explorar si la rama actual falla  
c) Un predicado especial que le permite al programador elegir entre varias bases de conocimiento  
d) El nodo raíz del árbol SLD a partir del cual se inicia la resolución  

**Respuesta correcta:** b  
**Justificación:** Cuando Prolog intenta resolver un goal y hay varias cláusulas que podrían unificar con él, crea un **choice point**: guarda el estado actual (bindings del trail) y la lista de cláusulas alternativas no probadas. Si la rama que tomó falla, el motor retrocede (backtrack) hasta el último choice point y prueba la siguiente alternativa. El corte `!` elimina los choice points creados en la cláusula actual.  
**Fuente:** minuta.md §BLOQUE 3 — Backtracking: choice points y trail (F-039 a F-043)  
**Bloom:** Comprender  

---

## P-07-004 | Comprender | Conceptual | 3 pts

**¿Cuál es la diferencia entre `=` y `==` en Prolog?**

a) `=` compara por valor; `==` compara por referencia de memoria  
b) `=` intenta unificar los dos términos (puede ligar variables); `==` verifica si los dos términos son ya idénticos sin ligar ninguna variable  
c) `=` solo funciona con átomos; `==` funciona con cualquier término  
d) Son sinónimos — en SWI-Prolog ambos realizan la misma operación  

**Respuesta correcta:** b  
**Justificación:** `=` es el predicado de **unificación**: `?- X = ana.` tiene éxito y liga `X = ana`. `==` es el predicado de **identidad estructural**: `?- X == ana.` falla si `X` no está ya ligada a `ana`. La diferencia clave: `=` puede ligar variables como efecto secundario; `==` nunca liga variables y solo tiene éxito si los dos términos son ya estructuralmente idénticos. Ejemplo: `?- X = Y, X == Y.` tiene éxito porque `=` liga X e Y, y luego `==` confirma que son idénticos.  
**Fuente:** minuta.md §BLOQUE 1 — `=` vs `==` vs `=..` (F-015, F-016)  
**Bloom:** Comprender  

---

## P-07-005 | Aplicar | Con código Prolog | 4 pts

**¿Cuál de las siguientes consultas de unificación tiene ÉXITO en Prolog?**

a) `?- f(X, b) = f(a, a).`  
b) `?- f(X, X) = f(ana, beatriz).`  
c) `?- f(X, b) = f(a, Y).`  
d) `?- f(X, g(X)) = f(a, g(b)).`  

**Respuesta correcta:** c  
**Justificación:** Analisis de cada opción:  
a) `f(X, b) = f(a, a)`: liga `X=a` pero el segundo argumento `b ≠ a` → **falla**.  
b) `f(X, X) = f(ana, beatriz)`: `X` debe unificar con `ana` y con `beatriz` simultáneamente → **falla** (conflicto).  
c) `f(X, b) = f(a, Y)`: liga `X=a` y `Y=b` → **éxito** con sustitución `{X=a, Y=b}`.  
d) `f(X, g(X)) = f(a, g(b))`: liga `X=a` pero luego `g(a) ≠ g(b)` → **falla**.  
**Fuente:** minuta.md §BLOQUE 1 — Ejemplos de unificación y falla (F-008, F-009)  
**Bloom:** Aplicar  

---

## P-07-006 | Aplicar | Con código Prolog | 4 pts

**Dada la siguiente base de conocimiento:**

```prolog
miembro(X, [X|_]).
miembro(X, [_|T]) :- miembro(X, T).
```

**¿Cuáles son TODAS las respuestas que da Prolog a `?- miembro(X, [a, b, c]).`?**

a) Solo `X = a` — Prolog devuelve la primera solución encontrada y se detiene  
b) `X = a ; X = b ; X = c` — Prolog devuelve las tres soluciones vía backtracking  
c) `X = [a, b, c]` — Prolog unifica X con la lista completa  
d) `false` — `miembro/2` requiere que el primer argumento ya esté instanciado  

**Respuesta correcta:** b  
**Justificación:** `miembro/2` tiene dos cláusulas. Primera: unifica `X` con la cabeza de la lista → `X = a` (éxito). Si se pide más (`;`), backtrack: segunda cláusula con `T = [b, c]` → aplica de nuevo → `X = b`. Backtrack: `T = [c]` → `X = c`. Backtrack: `T = []` → falla la segunda cláusula → fin. Resultado: tres soluciones `a`, `b`, `c` via backtracking. Este es `member/2` canónico de Prolog.  
**Fuente:** minuta.md §BLOQUE 2 — Listas: `member/2` (B2)  
**Bloom:** Aplicar  

---

## P-07-007 | Analizar | Con código Prolog | 4 pts

**Considerá el siguiente programa:**

```prolog
color(rojo). color(verde). color(azul).

?- color(X), write(X), nl, fail.
```

**¿Qué imprime esta consulta y por qué?**

a) Solo `rojo` — porque `fail` hace que la consulta falle después del primer resultado  
b) No imprime nada — `fail` hace que toda la consulta falle antes de ejecutar `write`  
c) Imprime `rojo`, luego `verde`, luego `azul`, luego falla — `fail` fuerza el backtracking que agota todos los valores de `color/1`  
d) Imprime `rojo verde azul` en una sola línea separado por espacios  

**Respuesta correcta:** c  
**Justificación:** Este es el patrón **fail-driven loop** de Prolog. La secuencia: (1) `color(X)` unifica `X=rojo`; (2) `write(rojo)` imprime `rojo`; (3) `nl` imprime nueva línea; (4) `fail` fuerza backtrack al choice point de `color(X)`; (5) `X=verde` → imprime `verde` → fail → backtrack; (6) `X=azul` → imprime `azul` → fail → no hay más cláusulas → consulta falla. Resultado: imprime las tres líneas y termina con `false`.  
**Fuente:** minuta.md §BLOQUE 3 — fail-driven loop y backtracking (F-041 a F-043)  
**Bloom:** Analizar  

---

## P-07-008 | Analizar | Con código Prolog | 4 pts

**Considerá los siguientes dos predicados:**

```prolog
% Versión A
maximo(X, Y, X) :- X >= Y.
maximo(X, Y, Y) :- X < Y.

% Versión B
maximo(X, Y, X) :- X >= Y, !.
maximo(_, Y, Y).
```

**¿Cuál es la diferencia de comportamiento entre la Versión A y la Versión B?**

a) Ambas son equivalentes en todos los casos — el corte `!` es solo una optimización de rendimiento sin impacto semántico  
b) La Versión B usa corte **verde**: elimina elección cuando ya se sabe cuál es el máximo, sin cambiar las soluciones; la Versión A recalcula ambas condiciones; ambas dan el mismo resultado para enteros instanciados  
c) La Versión B usa corte **rojo**: si se llama con variables no instanciadas, el corte hace que se devuelva una sola solución posiblemente incorrecta; la Versión A se comporta correctamente en más contextos  
d) La Versión A falla si X e Y son iguales; la Versión B siempre devuelve X en ese caso  

**Respuesta correcta:** b  
**Justificación:** El corte en Versión B es de tipo **verde** para inputs numéricos instanciados: si `X >= Y`, corta para evitar probar la segunda cláusula (que fallaría de todas formas, ya que `X < Y` sería falso). No elimina soluciones correctas. La Versión A es más declarativa pero hace dos tests. Para los propósitos del parcial, con argumentos instanciados ambas versiones producen el mismo resultado. Si se usaran con variables, Versión B produce resultados incorrectos (corte rojo), pero eso no se pide aquí.  
**Fuente:** minuta.md §BLOQUE 5 — Corte verde vs. rojo, `max/3` (B5)  
**Bloom:** Analizar  

---

## P-07-009 | Evaluar | Conceptual | 3 pts

**El corte `!` en Prolog fue descrito en clase como una "navaja de doble filo". ¿Cuál de las siguientes afirmaciones captura mejor esta idea?**

a) El corte es siempre perjudicial y no debería usarse en programas bien diseñados  
b) El corte verde mejora la eficiencia sin cambiar las soluciones; el corte rojo cambia el significado declarativo del programa, haciendo que Prolog encuentre menos soluciones de las que debería encontrar lógicamente  
c) El corte siempre mejora la eficiencia porque poda el árbol de búsqueda, pero nunca afecta la corrección del programa  
d) El corte rojo y el verde son sinónimos — la diferencia es solo de estilo  

**Respuesta correcta:** b  
**Justificación:** El **corte verde** (`!` que solo elimina alternativas que de todas formas fallarían) no cambia el significado declarativo: el programa con y sin `!` tiene las mismas soluciones, solo difiere en eficiencia. El **corte rojo** (`!` que elimina alternativas que podrían tener éxito) rompe la declaratividad: el programa ya no es una descripción pura de lo que es verdadero, sino que su comportamiento depende del orden de las cláusulas y de cuándo se coloca el corte. Es un compromiso entre eficiencia y claridad conceptual — de ahí la "navaja de doble filo".  
**Fuente:** minuta.md §BLOQUE 5 — Corte: dilema ético de declaratividad (B5)  
**Bloom:** Evaluar

---

# Preguntas — Tema 08: Paradigma OO con TypeScript

---

## P-08-001 | Recordar | Conceptual | 3 pts

**¿Cuáles son los cuatro pilares del paradigma orientado a objetos?**

a) Secuencia, selección, iteración y recursión  
b) Encapsulamiento, abstracción, herencia y polimorfismo  
c) Funciones puras, inmutabilidad, composición y transparencia referencial  
d) Tipos, clases, interfaces y módulos  

**Respuesta correcta:** b  
**Justificación:** Los cuatro pilares del paradigma OO son: (1) **Encapsulamiento** — agrupar estado y comportamiento en un objeto, controlando el acceso externo; (2) **Abstracción** — exponer solo lo necesario, ocultar la implementación; (3) **Herencia** — reutilización de estructura y comportamiento entre clases en relación "es-un"; (4) **Polimorfismo** — tratar distintos tipos de objetos de manera uniforme a través de una interfaz común.  
**Fuente:** minuta.md §BLOQUE 0 — [F-03] Los 4 pilares (OA Recordar)  
**Bloom:** Recordar  

---

## P-08-002 | Comprender | Conceptual | 3 pts

**Smalltalk afirma que "todo es un objeto" — incluyendo los números enteros y los booleanos. TypeScript no cumple este principio de la misma manera. ¿Por qué TypeScript no realiza el OO puro en el sentido de Smalltalk?**

a) Porque TypeScript no tiene clases — solo tiene interfaces y tipos estructurales  
b) Porque TypeScript tiene tipos primitivos (`number`, `boolean`, `string`) que no son objetos sino valores sin métodos propios, a diferencia de Smalltalk donde `1` y `true` son instancias de clases con métodos  
c) Porque TypeScript fue diseñado como lenguaje funcional con sintaxis de clases opcional  
d) Porque en TypeScript no existe el concepto de mensaje — las llamadas a método son solo invocaciones de función  

**Respuesta correcta:** b  
**Justificación:** En Smalltalk el principio "todo es un objeto" es absoluto: el número `1` es una instancia de `SmallInt`, `true` es una instancia de `True`, incluso las clases son objetos. TypeScript (como JavaScript) tiene tipos primitivos (`number`, `boolean`, `string`, `null`, `undefined`) que no son objetos y se acceden de forma distinta. TypeScript tiene `class` y permite OO, pero con compromisos pragmáticos: no es OO puro en el sentido de Alan Kay.  
**Fuente:** minuta.md §BLOQUE 2 — Smalltalk OO puro vs. TypeScript (OA Comprender)  
**Bloom:** Comprender  

---

## P-08-003 | Aplicar | Conceptual | 3 pts

**Considerá la siguiente clase TypeScript:**

```typescript
class CuentaBancaria {
  private saldo: number;

  constructor(saldoInicial: number) {
    this.saldo = saldoInicial;
  }

  depositar(monto: number): void {
    this.saldo += monto;
  }

  getSaldo(): number {
    return this.saldo;
  }
}
```

**¿Cuál de los cuatro pilares del OO aplica PRINCIPALMENTE este diseño, y cómo?**

a) Herencia — la clase hereda de `Object` y extiende su comportamiento  
b) Polimorfismo — `depositar` puede recibir distintos tipos de valores  
c) Encapsulamiento — el campo `saldo` es `private`, accesible solo a través de los métodos públicos `depositar` y `getSaldo`  
d) Abstracción — la clase oculta la implementación del sistema bancario completo  

**Respuesta correcta:** c  
**Justificación:** El diseño aplica principalmente **encapsulamiento**: el campo `saldo` está marcado `private`, lo que significa que no puede ser accedido ni modificado directamente desde afuera de la clase. Solo se puede interactuar con él a través de los métodos públicos `depositar()` y `getSaldo()`. Esto garantiza que el estado interno solo cambie de formas controladas y que las invariantes (ej: saldo nunca negativo) puedan mantenerse. El encapsulamiento es el pilar fundacional de OO según Simula y Smalltalk.  
**Fuente:** minuta.md §BLOQUE 3 — TypeScript OO: clases (OA Aplicar)  
**Bloom:** Aplicar  

---

## P-08-004 | Analizar | Conceptual | 3 pts

**En el paradigma funcional, la inmutabilidad es un principio central: los datos no se modifican. En el paradigma OO, el encapsulamiento gestiona el estado mutable. ¿Cuál de las siguientes afirmaciones describe mejor la diferencia en cómo cada paradigma trata el estado?**

a) No hay diferencia — ambos paradigmas prohíben la mutación del estado  
b) El funcional elimina el estado mutable; el OO lo contiene dentro de los objetos y controla el acceso a él. El funcional gana en predecibilidad; el OO gana en capacidad de modelar entidades con identidad y ciclo de vida  
c) El OO elimina el estado porque encapsular significa que el estado no existe fuera del objeto  
d) El funcional permite mutación pero solo dentro de funciones; el OO permite mutación solo dentro de clases  

**Respuesta correcta:** b  
**Justificación:** El paradigma **funcional** evita el estado mutable: las funciones puras siempre devuelven el mismo resultado para el mismo input y no tienen efectos colaterales. El paradigma **OO** acepta el estado mutable pero lo encapsula: cada objeto es responsable de su propio estado, que solo cambia a través de mensajes/métodos controlados. La elección entre paradigmas implica una compensación: el funcional es más predecible y testeable; el OO modela mejor las entidades del mundo real que tienen identidad propia y cambian a lo largo del tiempo (una cuenta bancaria, un pedido, un usuario).  
**Fuente:** minuta.md §BLOQUE 4 — Comparación OO vs funcional (OA Analizar)  
**Bloom:** Analizar