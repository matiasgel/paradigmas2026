# Minuta de Clase — Tema 02: Sintaxis y Semántica de Lenguajes

> **Estado:** APROBADO (revisado post-debate)
> **Aprobado por:** Matías Gel (docente)
> **Fecha de aprobación:** 2026-03-10
> **Última revisión:** 2026-03-10 — ajustes de claridad (debate panel + ejemplo LLMs/EBNF)
> **Agente:** Dr. Roberto ✍️ (class-writer)
> **Fecha de generación:** 2026-03-10
> **Duración total:** 120 minutos (constraint absoluto)
> **Clase:** 2 de 2 — Semana 1
> **Perfil docente:** profesor-teorico
> **Lenguaje principal:** TypeScript
> **Workflow:** topic-cycle / Step 4
> **Input:** `temas/02-sintaxis-semantica/diseno.md`

---

## Datos de la clase

| Campo | Valor |
|-------|-------|
| Materia | Paradigmas y Lenguajes de Programación 2026 |
| Institución | Universidad Nacional de Tierra del Fuego — Instituto IDEI |
| Tema Nº | 02 |
| Nombre del tema | Sintaxis y Semántica de Lenguajes |
| Semana | 1 |
| Clase | 2 de 2 |
| Duración | 120 minutos |
| Plan mínimo | Contenidos #1 y #6 |

---

## Pregunta motivadora de apertura

> *"El compilador de TypeScript rechazó tu programa. ¿Cómo sabe que está mal? ¿Y sabe siempre cuándo está mal?"*

Esta pregunta habilita el arco narrativo completo de la clase: de la forma (sintaxis) al significado (semántica), pasando por el análisis léxico, las gramáticas formales y el rol del compilador.

---

## Bloque 1 — Sintaxis y semántica: conceptos fundamentales (20 min)

### Objetivo
Distinguir forma de significado. Comprender por qué ambas dimensiones son independientes pero relacionadas.

### Desarrollo narrativo

Arrancar con el hook del Tema 01: *"En la clase anterior dijimos que TypeScript compila a JavaScript, que corre en V8. Hoy respondemos la pregunta técnica detrás de eso: ¿cómo sabe el compilador si un programa está bien escrito, y qué significa que esté bien?"*

**Definición de lenguaje de programación:** Una notación formal para describir algoritmos. "Formal" es la palabra clave — implica reglas precisas, no convenciones.

**Sintaxis:**
- Conjunto de reglas que determinan cuándo un programa está *bien formado*.
- La sintaxis se ocupa de la **forma**, no del comportamiento.
- Responde: ¿es este texto un programa válido?
- Ejemplo canónico: en C, `if (<expresión>) <sentencia>` es la forma correcta. Cualquier desviación es un error sintáctico.

**Semántica:**
- Le asigna **significado** a los programas sintácticamente correctos.
- Responde: ¿qué hace este programa?
- Ejemplo: `x = null` es sintácticamente válido en TypeScript, pero puede ser un error semántico según el contexto.

**Punto de tensión central — presentar explícitamente:**

> Un programa puede ser sintácticamente correcto y semánticamente incorrecto. El compilador siempre detecta errores sintácticos, pero NO siempre detecta errores semánticos.

**Criterios de buena sintaxis** (slides cátedra):
- Legibilidad
- Facilidad de escritura
- Facilidad de verificación
- Facilidad de traducción
- Carencia de ambigüedad

**Actividad de apertura (5 min) — clasificación rápida:**

Mostrar en pantalla y pedir a los estudiantes que clasifiquen cada caso antes de revelar la respuesta:

```typescript
// Caso A: ¿Error de sintaxis o de semántica?
const x: number = "hola"

// Caso B: ¿Error de sintaxis o de semántica?
if true { console.log("ok") }

// Caso C: ¿Error de sintaxis o de semántica?
const y = undefined; y.length
```

**Respuestas:**
- A → Error semántico estático (type error en compilación — `tsc` lo detecta)
- B → Error de sintaxis (falta paréntesis — `tsc` falla antes de entender qué hace el código)
- C → Error semántico dinámico (falla en runtime — `tsc` no puede saberlo en compilación)

**Mensaje de cierre del bloque:** "La definición formal de un lenguaje necesita AMBAS piezas: una gramática (sintaxis) y reglas semánticas. Ahora vamos a ver cómo se construye la primera."

### 🪤 Trampas anti-IA — Bloque 1

*Usar después de la actividad de clasificación. Pedir que respondan con el vocabulario exacto de la clase.*

**Trampa 1 — Tipos de error semántico:**
> *"¿Cuántos tipos de error semántico vimos hoy? Nombrá cada uno con el término exacto y un ejemplo."*

Respuesta esperada: **dos** — *semántico estático* (detectado en compilación por `tsc`) y *semántico dinámico* (detectado en runtime). El alumno que copió de IA puede agregar "error lógico", "error de intención" o "error de diseño" — términos que no existen en el vocabulario de esta clase.

**Trampa 2 — Por qué `tsc` no detecta el Caso C:**
> *"En el Caso C (`const y = undefined; y.length`), ¿por qué `tsc` no emite error? Respondé en términos de la clasificación de hoy."*

Respuesta esperada: porque el error es **semántico dinámico** — el valor de `y` solo se conoce en runtime, no en compilación. La respuesta trampa de IA es "porque falta `--strictNullChecks`" o "porque TypeScript no tiene null safety completo" — técnicamente plausible pero no responde con la clasificación vista en clase.

---

## Bloque 2 — Estructura léxica: del texto al token (20 min)

### Objetivo
Entender cómo se transforma un programa fuente en unidades mínimas para el análisis.

### Desarrollo narrativo

**El programa como texto plano:** El compilador recibe el programa como una cadena de caracteres. Antes de entender la estructura, necesita identificar las palabras.

**Reglas léxicas vs. reglas sintácticas:**
- **Léxicas:** definen el alfabeto y cómo combinar caracteres en palabras válidas.
  - Ejemplo: Java es case-sensitive (`myVar ≠ myvar`), la mayoría de los lenguajes también.
  - Ejemplo: Python distingue indentación como elemento léxico significativo.
- **Sintácticas:** definen cómo combinar palabras (tokens) en sentencias válidas.

La separación en dos niveles no es arbitraria: simplifica el diseño del compilador y mejora la eficiencia.

**Lexemas y Tokens** (Sebesta Cap. 4):

> Un **lexema** es la unidad sintáctica de más bajo nivel — la cadena de caracteres concreta.
> Un **token** es la categoría abstracta a la que pertenece ese lexema.

La distinción es análoga a lingüística: "perro", "gato", "ave" son lexemas distintos que pertenecen al token SUSTANTIVO.

**Ejemplo central — tokenización:**

La sentencia `indice = 5 * contador + 1;` se descompone así:

| Lexema | Token |
|--------|-------|
| `indice` | identificador |
| `=` | op-asignación |
| `5` | constante_entera |
| `*` | op_producto |
| `contador` | identificador |
| `+` | op_suma |
| `1` | constante_entera |
| `;` | delimitador |

Señalar: `indice` y `contador` tienen el mismo token (identificador) aunque son lexemas distintos. El analizador léxico no sabe que son nombres de variables — eso lo decide el analizador semántico.

> 💡 **Pregunta anticipada (frecuente):** "¿Entonces el lexer no sabe si `indice` es una variable, una función o una constante?" — Exacto. El lexer solo sabe que es un *identificador*. La distinción entre variable, función y constante la resuelve el analizador semántico más adelante en el pipeline.

**Elementos sintácticos de un lenguaje** (slides cátedra):
- Caracteres, identificadores, operadores
- Palabras clave y reservadas (diferencia: `if` es reservada, no puede usarse como identificador)
- Comentarios y espacios en blanco (generalmente ignorados por el parser)
- Delimitadores, expresiones, sentencias

**El analizador léxico (lexer / scanner):**
- Transforma la cadena de caracteres en una secuencia de tokens.
- Es el primer componente del compilador — el "portero" que prepara la entrada para el analizador sintáctico.
- **Por qué separarlo del parser** (Sebesta Cap. 4):
  1. **Simplicidad:** el parser opera sobre tokens abstractos, no caracteres.
  2. **Eficiencia:** el lexer puede usar autómatas muy rápidos para reconocer patrones.
  3. **Portabilidad:** cambiar el conjunto de caracteres (ASCII vs. Unicode) solo afecta al lexer.

**Ejemplo TypeScript en vivo:**
```
tsc --listEmittedFiles archivo.ts
```
El primer paso que ejecuta `tsc` internamente es exactamente este: convertir el archivo fuente en tokens. Cuando `tsc` reporta un error con número de línea y columna, esa información viene del lexer.

---

## Bloque 3 — Gramáticas formales: BNF y EBNF (30 min)

### Objetivo
Leer e interpretar una especificación formal de sintaxis. Usar BNF para describir construcciones de lenguaje.

*Este es el bloque de mayor densidad cognitiva. El paso por conceptos es gradual: primero la motivación, luego los formalismos, luego los ejercicios.*

### Desarrollo narrativo

**¿Por qué gramáticas formales?**

Antes de BNF, el lenguaje FORTRAN se especificaba con reglas en inglés. El problema: el inglés es ambiguo. Dos implementaciones distintas del compilador de FORTRAN podían comportarse diferente ante el mismo programa.

En contraste, Python tiene una gramática BNF oficial. Todo compilador conforme a esa gramática acepta exactamente los mismos programas.

Una gramática formalmente especificada permite **verificar automáticamente** si un programa es válido.

**Gramáticas libres de contexto — Clasificación de Chomsky (1959):**

Una gramática es la tupla `(N, T, S, P)`:
- **N:** símbolos no terminales — abstracciones, categorías, "clases de cosas"
- **T:** símbolos terminales — lexemas/tokens reales que aparecen en el código
- **S:** símbolo inicial — el punto de partida de toda derivación
- **P:** producciones / reglas — cómo expandir no terminales

*No es necesario profundizar en la jerarquía de Chomsky — usar solo como referencia histórica y para dar nombre a la clase de gramáticas que estudiamos.*

**BNF (Backus-Naur Form):**

Metasímbolos:
- `::=` — "se define como"
- `|` — alternativa ("o")
- `< >` — encierra símbolos no terminales

Regla: el lado izquierdo (LHS) es el no terminal a definir; el lado derecho (RHS) es su definición.

```
<assign>    ::= <var> = <expression>
<enunc_if>  ::= if <expr_log> then <enunc>
              | if <expr_log> then <enunc> else <enunc>
```

Ejercicio de lectura: ¿qué dice la segunda regla? Que un `<enunc_if>` puede ser un `if` simple O un `if-else`. Ambas formas son válidas.
y
**Gramática de ejemplo completa** (para derivación):

```
<assign> ::= <id> := <expr>
<id>     ::= A | B | C
<expr>   ::= <id> + <expr> | <id> * <expr> | (<expr>) | <id>
```

> ⚠️ **Nota de convención:** En gramáticas formales se usan variables de una letra (A, B, C) por tradición académica. No son variables TypeScript — son símbolos abstractos que representan cualquier identificador válido en el lenguaje.

**Derivación de `A := B * (A + C)` paso a paso:**

| Forma de sentencia | Regla aplicada |
|-------------------|---------------|
| `<assign>` | — (símbolo inicial) |
| `<id> := <expr>` | `assign → id := expr` |
| `A := <expr>` | `id → A` |
| `A := <id> * <expr>` | `expr → id * expr` |
| `A := B * <expr>` | `id → B` |
| `A := B * (<expr>)` | `expr → (expr)` |
| `A := B * (<id> + <expr>)` | `expr → id + expr` |
| `A := B * (A + <expr>)` | `id → A` |
| `A := B * (A + <id>)` | `expr → id` |
| `A := B * (A + C)` | `id → C` |

Cada fila aplica exactamente una producción de la gramática. La forma de sentencia es la cadena en cada paso intermedio de la derivación.

**Árboles sintácticos (parse trees):**

El árbol de derivación para `A := B * (A + C)`:

```
         <assign>
        /    |    \
      <id>  :=   <expr>
       |           |
       A     <id> * <expr>
              |      |
              B    (<expr>)
                    |
               <id> + <expr>
                |       |
                A      <id>
                        |
                        C
```

Nodos internos = no terminales. Hojas = terminales. El árbol muestra la **estructura jerárquica** de la derivación — qué se agrupa con qué.

**Ambigüedad:**

Una gramática es **ambigua** si permite dos árboles de derivación distintos para la misma cadena.

Ejemplo: con una gramática simple sin precedencia, `J := 1 + 2 * 3` puede derivarse de dos formas:
1. `(1 + 2) * 3 = 9`
2. `1 + (2 * 3) = 7`

Dos árboles → dos significados. Esto es un **defecto de diseño del lenguaje**: el compilador no sabe cuál árbol es el correcto.

**Solución:** Codificar precedencia y asociatividad de operadores en la gramática misma (agregando reglas jerárquicas para cada nivel de precedencia).

**EBNF (Extended BNF):**

Notación extendida que evita recursión en algunos casos:
- `[ ]` — la parte es opcional (0 o 1 vez)
- `{ }` — la parte se repite (0 o más veces)
- `|` dentro de corchetes — alternativas dentro del grupo

```
<programa>   ::= { <sentencia>* }
<sentencia>  ::= <asignación> | <condicional> | <loop>y
<asignación> ::= <identificador> = <expr>
<condicional>::= if <expr> { <sentencia>* }
               | if <expr> { <sentencia>* } else { <sentencia>* }
<loop>       ::= while <expr> { <sentencia>* }
```

**Actividad participativa (5 min):**

> *"Dado `C := D – E * F`, derivar el árbol de derivación usando la gramática del ejemplo."*

Usar la pizarra o proyección interactiva. El árbol correcto muestra que `E * F` se resuelve primero (si la gramática tiene la precedencia correcta) o que hay ambigüedad (si no la tiene). Este es el punto de aprendizaje.

### 🪤 Trampas anti-IA — Bloque 3

*Aplicar justo después de la actividad de derivación. Requieren referencia a la gramática concreta de la clase.*

**Trampa 3 — Conteo de pasos de derivación:**
> *"¿Cuántos pasos de derivación tiene `A := B * (A + C)` en la gramática de hoy? Mostrá la tabla completa: forma de sentencia + regla aplicada en cada fila."*

Respuesta esperada: **10 pasos** (la tabla tiene 10 filas incluyendo el símbolo inicial). Los LLMs se equivocan frecuentemente en este conteo (traen 8, 9 o 11). La forma de validar es que presenten la tabla con la columna "Regla aplicada" — eso no se puede fabricar sin haber seguido la derivación paso a paso.

**Trampa 4 — Cadena vacía:**
> *"En la gramática de hoy, ¿puede `<expr>` derivar la cadena vacía? ¿Por qué?"*

Respuesta esperada: **No** — todas las producciones de `<expr>` requieren al menos un `<id>` y ninguna tiene una producción vacía (epsilon). La respuesta trampa de IA es "depende de la gramática" — que elude responder sobre *la gramática específica de clase*.

**Trampa 5 — EBNF vs. BNF en la práctica:**
> *"Reescribí la producción `<expr> ::= <id> + <expr> | <id> * <expr> | (<expr>) | <id>` usando notación EBNF para eliminar la recursión."*

Respuesta esperada: algo como `<expr> ::= <id> { ("+" | "*") <expr> } | "(" <expr> ")"`. Requiere entender cuándo `{ }` reemplaza recursión — los LLMs frecuentemente devuelven BNF con otro nombre o EBNF incorrecta que no es equivalente.

---

## Bloque 4 — Diagramas de sintaxis y notación gráfica (10 min)

### Objetivo
Leer especificaciones gráficas de sintaxis — usadas en documentación oficial de lenguajes.

*Este bloque actúa como alivio visual después del Bloque 3. Ritmo más lento, más visual.*

### Desarrollo narrativo

**¿Qué son los diagramas de sintaxis (railroad diagrams)?**

Son la representación gráfica equivalente a EBNF. Se llaman "railroad" porque muestran caminos posibles como rieles de tren.

**Convención visual:**
- Recuadro (rectángulo) → símbolo **no terminal** (categoría)
- Óvalo o círculo → símbolo **terminal** (token concreto)

**Cómo leer un diagrama:**
Una cadena es válida si podés "viajar" de izquierda a derecha atravesando el diagrama. En cada bifurcación, elegís un camino. Si llegás al final, la cadena es sintácticamente válida.

**Diagrama para `<condicional>`** (descripción textual — se proyecta en filmina):

```
  ──► [if] ──► (expr) ──► [{] ──► {<sentencia>} ──► [}] ──────────────────────────►
                                                           ↑ (saltear else es válido)
                                                       ──► [else] ──► [{] ──► {<sentencia>} ──► [}] ──►
```

**Dos usos de la descripción sintáctica:**
1. **Para el programador:** entender qué construcciones son válidas en el lenguaje → escribir código correcto.
2. **Para el compilador:** la gramática es la especificación que el parser implementa.

**Conexión con TypeScript:** la documentación oficial de TypeScript usa diagramas de sintaxis para documentar cada construcción del lenguaje. No es notación teórica — es la herramienta de documentación estándar de la industria.

---

## Bloque 5 — Semántica: de la forma al significado (20 min)

### Objetivo
Comprender qué es la semántica formal e introducir la semántica operacional como el enfoque más intuitivo.

### Desarrollo narrativo

**¿Por qué necesitamos semántica formal?**

Sintaxis correcta ≠ programa correcto. Tenemos dos tipos de error semántico:
1. **Errores semánticos estáticos** (detectables en compilación): asignar un `string` a una variable `number` en TypeScript.
2. **Errores semánticos dinámicos** (solo detectable en ejecución): acceder al índice 100 de un array vacío.

Sin semántica formal, el comportamiento del lenguaje depende de la implementación → el mismo programa puede comportarse diferente en dos compiladores distintos → no es portable.

**Nombres y objetos denotables** (Gabbrielli & Martini Cap. 4, §4.1):

> Un **nombre** es una secuencia de caracteres que *denota* (refiere a) otro objeto.

Distinción importante: nombre ≠ objeto que denota.
- El mismo objeto puede tener varios nombres → **aliasing**.
- El mismo nombre puede referir a objetos distintos en distintos contextos → **scope**.

**Objetos denotables en un lenguaje de programación:**
- Variables, parámetros formales
- Procedimientos / funciones
- Tipos, etiquetas, módulos
- Constantes, excepciones
- Tipos primitivos y operaciones predefinidas del lenguaje

**Concepto de entorno (environment):**

> El **entorno** es el componente de la máquina abstracta que mantiene las asociaciones `nombre → objeto` en cada punto de ejecución.

Es decir: en cada instante de ejecución, el entorno sabe a qué objeto refiere cada nombre.

*Nota pedagógica: esto se profundizará en Tema 09 (Variables, Binding y Ámbito). Hoy lo introducimos como noción semántica base.*

**Binding (ligadura) — mención anticipatoria:**

> Una **ligadura** es la asociación entre un nombre y un objeto denotable. Por ejemplo: `const PI = 3.14159` liga el nombre `PI` al valor numérico `3.14159`.

*⏭️ El mecanismo completo de ligadura — cuándo ocurre, estática vs. dinámica, reglas de scope y visibilidad — se estudia en detalle en **Tema 09 (Variables, Binding y Ámbito)**. Hoy alcanza con saber que los nombres se asocian a objetos, y que esa asociación existe en el entorno.*

**Semántica operacional** (introducción conceptual):

> La **semántica operacional** define el significado de un programa como la **secuencia de estados** que produce al ejecutarse.

- **Estado:** conjunto de pares `(nombre, valor)` en un instante dado.
- **Programa:** transformación de estado inicial → estado final (o secuencia de estados intermedios).
- Conecta directamente con la **máquina abstracta** del Tema 01: la semántica de un programa en una máquina abstracta *es* su modelo de ejecución.

**Ejemplo paso a paso:**

```
Programa:
  x := 5
  y := x + 1

Estado inicial: { }
  → ejecutar x := 5     → estado: { x = 5 }
  → ejecutar y := x + 1 → estado: { x = 5, y = 6 }
Estado final: { x = 5, y = 6 }
```

La semántica operacional nos dice que el significado de `x := 5; y := x + 1` es exactamente esta secuencia de transformaciones de estado.

**Ampliar con caso condicional** — mostrar que el estado puede NO cambiar:

```
Programa:
  x := 1
  if x > 3 then y := 0

Estado inicial: { }
  → ejecutar x := 1        → estado: { x = 1 }
  → evaluar x > 3          → false (1 > 3 es falso)
  → la rama no se ejecuta  → estado: { x = 1 }  ← sin cambio
Estado final: { x = 1 }   (y nunca fue ligada)
```

> 💡 **Punto pedagógico:** la semántica operacional modela no solo lo que cambia, sino también lo que el programa *decide no hacer*. El estado puede permanecer igual — y eso también es parte del significado del programa.

**Semántica estática (type checking):**

Un caso especial de semántica que se verifica antes de ejecutar:
- El **type-checker** de TypeScript es el primer "intérprete semántico" que ve el código.
- Verifica en compilación que los tipos sean consistentes.
- Un programa que pasa el type-checker puede aún tener errores semánticos dinámicos.

---

## Bloque 6 — Analizador sintáctico: rol en el compilador + cierre (15 min)

### Objetivo
Entender el rol del parser en el pipeline de compilación — sin enseñar algoritmos. Cerrar con el gancho de relevancia actual: gramáticas y LLMs.

### Desarrollo narrativo

**El parser como corazón del compilador** (Sebesta Cap. 4, §4.1):

El analizador sintáctico (parser) recibe la secuencia de tokens del lexer y:
1. Determina si forman un programa válido según la gramática.
2. Construye el **árbol de derivación** (parse tree) como representación interna.
3. Pasa el árbol al analizador semántico y al generador de código.

**Dos aproximaciones conceptuales al parsing** (nivel conceptual, sin algoritmos):

| Estrategia | Descripción | Característica |
|-----------|-------------|---------------|
| **Top-down** (descendente) | Comienza en el símbolo inicial, trata de derivar la cadena de entrada | Intuitivo, legible |
| **Bottom-up** (ascendente) | Parte de los tokens, construye el árbol hacia arriba | Más poderoso, más complejo |

*Los algoritmos específicos (recursive-descent, LR) corresponden a Teoría de Compiladores — están fuera del scope de esta materia.*

**Pipeline del compilador / intérprete (revisión con Tema 01):**

```
Código fuente (texto)
       ↓
  [Lexer] → secuencia de tokens
       ↓
  [Parser] → árbol de derivación
       ↓
  [Analizador semántico] → árbol anotado con tipos
       ↓
  Compilador: [Generador de código] → código objeto
  Intérprete: [Evaluador] → ejecución directa del árbol
```

`tsc` (TypeScript compiler) ejecuta exactamente este pipeline y emite JavaScript al final.

**Síntesis: errores sintácticos vs. semánticos en TypeScript:**

```typescript
// Error SINTÁCTICO (falla en análisis sintáctico):
function foo( { return 42 }   // falta ')'
// tsc: "error TS1005: ')' expected"

// Error SEMÁNTICO ESTÁTICO (falla en type-checking):
const x: number = "texto"
// tsc: "error TS2322: Type 'string' is not assignable to type 'number'"

// Error SEMÁNTICO DINÁMICO (falla en runtime, tsc NO lo detecta):
const arr: number[] = []
console.log(arr[100].toString())  // undefined.toString() → TypeError en runtime
```

**Cierre — Las gramáticas en la IA generativa (5 min):**

> *"La gramática de Chomsky (1959), la notación BNF de Backus-Naur (1960), y la EBNF que estudiamos hoy no son historia — son infraestructura activa en los sistemas de IA más modernos."*

**Constrained decoding** (Willard & Louf, 2023):

Los LLMs modernos pueden generar texto libre. Para generar **JSON válido, SQL, o código**, se usa una técnica llamada *constrained decoding*:
1. Se compila una gramática EBNF a un autómata de estados finitos.
2. En cada paso de generación, el autómata filtra qué tokens son válidos.
3. El modelo solo puede producir tokens que pertenezcan a una derivación válida.

**Herramientas actuales:**
- **Outlines** (Python) — usa gramáticas BNF/EBNF como input del programador
- **LMQL** — lenguaje de consulta con restricciones sintácticas declarativas sobre LLMs (Beurer-Kellner et al., 2023)

**Ejemplo concreto — cómo la EBNF cambia el resultado del LLM:**

Supongamos que le pedimos a un LLM que extraiga información de un texto y la devuelva como JSON. Sin restricción gramatical, el modelo puede responder de formas distintas e incompatibles:

```
// Respuesta A (sin EBNF) — el modelo inventa el formato:
"El nombre es Juan y tiene 30 años."

// Respuesta B (sin EBNF) — otro run, otro formato:
{ nombre: "Juan", edad: 30 }    ← claves sin comillas (JSON inválido)

// Respuesta C (sin EBNF) — otro run:
{"nombre":"Juan","edad":"30"}   ← edad como string, no número
```

Con la siguiente gramática EBNF como restricción:

```ebnf
<respuesta>  ::= "{" <campo> { "," <campo> } "}"
<campo>      ::= '"nombre"' ":" '"' <texto> '"'
               | '"edad"'   ":" <entero>
<entero>     ::= [0-9]+
<texto>      ::= [a-zA-Z]+
```

El autómata compilado de esta gramática **fuerza** al LLM a producir solo tokens válidos en cada paso. El resultado es siempre:

```json
{"nombre": "Juan", "edad": 30}
```

*El modelo no puede generar otra cosa* — el autómata bloqueó todos los tokens que no encajan en la gramática, sin importar qué habría generado libremente.

> 💡 **Analogía directa:** el constrained decoding hace con el LLM lo que el parser hace con el compilador: en cada paso, pregunta a la gramática qué es válido a continuación y descarta el resto.

**Demo en vivo con ChatGPT (5-7 min) — guion completo para ejecutar en clase:**

> 🖥️ **Preparación:** Abrir chatgpt.com en el proyector. Tener los prompts copiados en un archivo de texto para pegar rápido. Usar el modelo GPT-4o.

---

#### ACTO 1 — El modelo sin restricción: formato libre (2 min)

*"Vamos a pedirle a ChatGPT que extraiga datos de un texto. Sin decirle qué formato usar."*

**Prompt 1a** — pegar en una conversación nueva:
```
Extraé el nombre y la edad del siguiente texto y devolvé el resultado.

Texto: "Me llamo Juan y tengo 30 años."
```

Ejecutar. Anotar el formato que devuelve (probablemente texto natural o YAML informal).

**Prompt 1b** — abrir OTRA conversación nueva, pegar el mismo prompt:
```
Extraé el nombre y la edad del siguiente texto y devolvé el resultado.

Texto: "Me llamo Juan y tengo 30 años."
```

Ejecutar de nuevo. Comparar los dos resultados en pantalla.

*Señalar al grupo:*
- Los resultados son distintos aunque el texto es idéntico.
- Posibles variaciones reales: texto narrativo / YAML / JSON con tipos equivocados / JSON sin comillas en claves.
- **El modelo no tiene un concepto de "formato correcto"** — produce lo que estadísticamente es más probable dado el prompt.

> 🗣️ *"¿Alguno vio esto cuando usó ChatGPT para generar datos para un proyecto? ¿Cuántas veces tuvieron que limpiar la respuesta a mano?"* (pausa breve para respuestas)

---

#### ACTO 2 — Instrucción de esquema: el modelo intenta respetar (2 min)

*"Ahora le vamos a decir exactamente qué formato queremos. Vamos a ver si alcanza."*

**Prompt 2** — conversación nueva:
```
Extraé el nombre y la edad del siguiente texto.
Respondé ÚNICAMENTE con JSON válido. Sin texto adicional, sin explicaciones.
El JSON debe tener exactamente esta estructura:
{"nombre": <string>, "edad": <number>}

Texto: "Me llamo Juan y tengo 30 años."
```

El modelo debería devolver:
```json
{"nombre": "Juan", "edad": 30}
```

*Señalar:* "Mejoró. Pero ahora hagamos una prueba más complicada."

**Prompt 2b** — mismo formato, texto ambiguo:
```
Extraé el nombre y la edad del siguiente texto.
Respondé ÚNICAMENTE con JSON válido. Sin texto adicional, sin explicaciones.
El JSON debe tener exactamente esta estructura:
{"nombre": <string>, "edad": <number>}

Texto: "Juan tiene unos 30, más o menos. Al menos eso dice su DNI."
```

El modelo puede devolver:
```json
{"nombre": "Juan", "edad": 30}   ← correcto
```
…o puede agregar texto explicativo, poner `"edad": "unos 30"`, o poner `"edad": null`.

*Señalar:* **La instrucción en texto es semántica** — el modelo la interpreta. Si el texto de entrada es ambiguo, la interpretación puede ser incorrecta. No hay nada que lo bloquee formalmente.

---

#### ACTO 3 — GPT-4o con Structured Outputs: la gramática en producción (1-2 min)

*"ChatGPT tiene desde 2024 un modo que implementa exactamente el mecanismo de Willard & Louf. Se llama Structured Outputs."*

Proyectar el siguiente fragmento de código Python (no hace falta ejecutarlo — solo mostrarlo):

```python
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class Persona(BaseModel):
    nombre: str
    edad: int          # int, no str — el tipo está en la gramática

response = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "user",
         "content": "Extraé nombre y edad: 'Me llamo Juan y tengo 30 años.'"}
    ],
    response_format=Persona,   # ← acá se pasa la gramática
)

print(response.choices[0].message.parsed)
# Persona(nombre='Juan', edad=30)   ← siempre, garantizado
```

*Explicar:*
- `Persona` es un esquema (una gramática de estructura de datos).
- Al pasarlo como `response_format`, la API compila ese esquema a un autómata interno.
- El modelo **no puede producir** una respuesta que no sea una `Persona` válida.
- Si el texto no tiene edad, el modelo devuelve un error de parseo — no inventa un valor.

**La diferencia clave:**

```
Prompt 2 (instrucción):    "respondé con este formato"  →  el modelo lo INTENTA
Prompt 3 (gramática):      response_format=Persona      →  el autómata lo FUERZA
```

> 🎯 **Pregunta de cierre para el grupo:**
> *"¿En qué se parece este `response_format` al rol que cumple una gramática BNF para un compilador?"*
>
> Respuesta esperada: **en ambos casos la gramática define qué secuencias son válidas, y cualquier desviación es rechazada antes de llegar al resultado final** — ya sea por el parser del compilador o por el autómata del LLM.

### 🪤 Trampas anti-IA — Bloque 6

*Aplicar inmediatamente después del demo, mientras los resultados están en pantalla. Estas preguntas requieren haber observado la demo en vivo.*

**Trampa 6 — Observación directa del Acto 1:**
> *"En el Acto 1, las dos respuestas de ChatGPT al mismo prompt, ¿tenían el mismo contenido? ¿El mismo formato?"*

Respuesta esperada: mismo contenido (nombre y edad correctos) pero **formato distinto** entre los dos runs. El alumno sin clase dirá "sí, eran iguales" o "no, el contenido también difería" — dependiendo de lo que pegue de ChatGPT. La respuesta correcta depende exactamente de lo que se vio en pantalla hoy.

**Trampa 7 — Acto 2 y texto ambiguo:**
> *"En el Acto 2 con el texto ambiguo ('Juan tiene unos 30, más o menos'), ¿qué pasó exactamente con el campo `edad` en la respuesta de ChatGPT?"*

Respuesta esperada: referencia al resultado real de esta demo. Si devolvió `30`, `"unos 30"`, `null` o texto adicional — la única respuesta correcta es la que se vio en pantalla. Ningún alumno sin haber estado puede responder con certeza.

**Trampa 8 — Constrained decoding vs. validación posterior:**
> *"¿El autómata del constrained decoding verifica la respuesta después de generarla, o filtra token a token durante la generación? ¿Cuál es la diferencia práctica?"*

Respuesta esperada: **filtra token a token durante la generación** — en cada paso el autómata dice qué tokens son válidos a continuación. La diferencia práctica: nunca produce una respuesta inválida para descartarla después — directamente *no puede generarla*. La trampa de IA es decir "verifica al final" (post-hoc validation), que es lo que hacen sistemas más simples pero NO es constrained decoding.

> 💡 **Nota técnica para el docente:** OpenAI documentó Structured Outputs en agosto 2024. Internamente usa un motor de constrained decoding basado en el trabajo de Willard & Louf (2023). El esquema Pydantic se convierte a JSON Schema, que se compila al autómata. La clave `response_format` activa ese pipeline — el mismo que estudiamos hoy en la teoría.

El punto de inflexión: la misma formalización que estudiamos hoy es la que hace que los LLMs puedan garantizar outputs estructurados. No es una curiosidad histórica — es una herramienta activa.

---

## Preguntas de cierre

*(Últimos 2-3 minutos — elegir 1 o 2 según tiempo disponible)*

1. *"Un programa TypeScript que pasa `tsc` sin errores, ¿puede tener errores semánticos? Dar un ejemplo."*
   → Respuesta esperada: sí — acceder a un índice inexistente de un array, llamar a un método en `undefined`, etc.

2. *"¿Por qué una gramática ambigua es problemática para un compilador?"*
   → Respuesta esperada: porque el compilador no sabe qué árbol de derivación elegir → no sabe cuál es el comportamiento correcto del programa.

3. *"Diferencia entre un token y un lexema — dar un ejemplo concreto."*
   → Respuesta esperada: el lexema es la cadena concreta (`indice`), el token es la categoría (`identificador`). Dos lexemas distintos pueden tener el mismo token.

---

## 🪤 Banco de trampas anti-IA — Usar en cualquier momento

*Preguntas diseñadas para ser difíciles de responder correctamente solo con un LLM. Requieren referencia a los artefactos, ejemplos y observaciones concretas de esta clase. Usar en orales, durante la clase como checkpoint, o como filtro de corrección de TPs.*

| # | Pregunta trampa | Por qué falla la IA | Respuesta esperada |
|---|-----------------|--------------------|--------------------|
| T1 | "En la sentencia `indice = 5 * contador + 1;` que tokenizamos hoy, ¿cuántos tokens tiene?" | La IA puede contar mal | **8 tokens** |
| T2 | "¿Por qué `indice` y `contador` tienen el mismo token aunque son variables distintas?" | La IA da respuesta genérica | Porque el **lexer no distingue** variable/función/constante — eso lo resuelve el analizador semántico |
| T3 | "Derivá `A := B * (A + C)` con la gramática de la clase. Mostrá la tabla con la columna 'Regla aplicada'." | La IA produce 8-9 pasos o inventa reglas que no existen | Table exacta con **10 filas** (símbolo inicial + 9 expansiones) |
| T4 | "¿Puede `<expr>` en la gramática de hoy derivar la cadena vacía? Justificá con las producciones exactas." | La IA responde genéricamente | **No**: ninguna de las 4 producciones de `<expr>` tiene epsilon |
| T5 | "¿Los dos runs del Acto 1 de la demo devolvieron el mismo formato?" | Requiere haber visto la demo | Mismo contenido, **formato distinto** entre runs |
| T6 | "El autómata de constrained decoding actúa ANTES o DESPUÉS de que el modelo genera cada token." | La IA confunde con post-hoc validation | **Antes**: filtra en cada paso qué tokens son posibles |
| T7 | "¿Qué herramienta Python open-source para constrained decoding se mencionó en clase?" | La IA puede inventar nombres | **Outlines** (y LMQL como lenguaje de consulta) |
| T8 | "¿En qué año se publicó el paper de Willard & Louf? ¿Dónde está disponible?" | Requiere referencia a la bibliografía de clase | **2023**, arXiv:2307.09702 |
| T9 | "¿Cuál criterio de buena sintaxis se relaciona directamente con la posibilidad de compilar automáticamente?" | La IA da respuestas genéricas | **Facilidad de verificación** y carencia de ambigüedad |
| T10 | "¿Cuál es la diferencia entre palabra clave y reservada? Dar un ejemplo concreto de la clase." | La IA confunde los términos | Reservada: no puede usarse como identificador (`if`). Clave: significado especial pero reutilizable en algunos contextos |

---

## Tarea / Conexión con próxima clase

> **Para la Clase 01 del Tema 03 (Sistema de Tipos):**
> Pensar en esta pregunta: *"El type-checker rechazó tu programa. ¿Qué información necesita el compilador para poder hacer eso?"*

---

## Referencias de la clase

- **Sebesta, R.** (2019). *Concepts of Programming Languages* (12ª ed.), Cap. 3 y Cap. 4.
- **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms*, Cap. 4, §4.1.
- **Willard, B. T. & Louf, R.** (2023). *Efficient Guided Generation for Large Language Models*. arXiv:2307.09702.
- **Beurer-Kellner, L. et al.** (2023). *Prompting Is Programming: A Query Language for Large Language Models* (LMQL). VLDB 2023.

---

## Cronograma de referencia

| Bloque | Inicio | Fin | Duración | Contenido |
|--------|--------|-----|----------|-----------|
| 1 | 0:00 | 0:20 | 20 min | Sintaxis y semántica: conceptos fundamentales |
| 2 | 0:20 | 0:40 | 20 min | Estructura léxica: lexemas y tokens |
| 3 | 0:40 | 1:10 | 30 min | Gramáticas formales: BNF, EBNF, árboles, ambigüedad |
| 4 | 1:10 | 1:20 | 10 min | Diagramas de sintaxis |
| 5 | 1:20 | 1:40 | 20 min | Semántica: nombres, entorno, ligaduras, semántica operacional |
| 6 | 1:40 | 1:55 | 15 min | Parser: rol en el compilador + gramáticas en IA |
| Buffer | 1:55 | 2:00 | 5 min | Preguntas / espacio libre |

**Total: 120 minutos** ✓

---

> **⚙️ PARA REVISIÓN:** Esta minuta desarrolla los 6 bloques del diseño aprobado con proporcionalidad exacta a la duración. Los bloques se marcan con transiciones explícitas para facilitar el dictado. Buffer de 5 minutos al final para preguntas o retraso natural de la clase.
