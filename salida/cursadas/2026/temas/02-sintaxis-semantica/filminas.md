<!-- markdownlint-disable MD001 MD025 MD032 MD036 MD060 -->

# Filminas — Tema 02: Sintaxis y Semántica de Lenguajes

> **Estado:** GENERADA
> **Agente:** Dr. Roberto ✍️ (class-writer)
> **Fecha de generación:** 2026-03-19
> **Baseline:** `informefinal/archivos/filminas.md` (F-00 a F-39, generado 2026-03-18)
> **Cambios respecto al baseline:** B5 rediseñado — semántica estática (gramáticas de atributos) + tres enfoques de semántica dinámica (Sebesta Cap. 3 §§3.4–3.5); nombres/entorno/binding diferidos a Tema 09
> **Duración total:** 120 minutos · Portada + 38 filminas (F-01 a F-37)
> **Clase:** 2 de 2 — Semana 1
> **Perfil docente:** profesor-teorico
> **Lenguaje principal:** TypeScript
> **Input:** `salida/cursadas/2026/temas/02-sintaxis-semantica/diseno.md` (REDISEÑO — APROBADO)
> **Workflow:** topic-cycle / Step 4

---

### [F-00]

@imagen: background
@prompt-imagen: prompt="Escena académica contemporánea sobre compiladores y lenguajes de programación: pantalla con código TypeScript, flujo lexer-parser-árbol sintáctico, cuaderno universitario y contexto de aula. Tema: Sintaxis y Semántica de Lenguajes." local_asset="slides/assets/F-00-bg.png"

# Sintaxis y Semántica de Lenguajes

**Paradigmas y Lenguajes de Programación — 2026**
Universidad Nacional de Tierra del Fuego — Instituto IDEI

> *"¿Cómo sabe el compilador si tu programa está bien escrito?*
> *¿Y sabe siempre cuándo está mal?"*

---

### [F-01]

## Agenda

| Bloque | Minutos | Tema |
|--------|---------|------|
| 1 | 20 | Sintaxis y semántica |
| 2 | 20 | Del texto al token |
| 3 | 30 | BNF, EBNF, derivación y árboles |
| 4 | 10 | Diagramas de sintaxis |
| 5 | 12 | Semántica: síntesis y tipos |
| 6 | 15 | Pipeline del compilador e IA |

**Total:** 120 minutos

---

## BLOQUE 1 — SINTAXIS Y SEMÁNTICA (20 min)

---

### [F-02]

@imagen: content
@prompt-imagen: prompt="Diagrama que conecta Tema 01 con Tema 02: flecha desde TypeScript→JavaScript (compilación) hacia el interior del compilador, mostrando que hoy respondemos la pregunta técnica subyacente. Infografía técnica académica, fondo claro, sin texto." local_asset="slides/assets/F-02-content.png"

## Continuidad con Tema 01

**La clase pasada:**
- TypeScript compila a JavaScript
- JavaScript corre sobre una máquina de ejecución real

**La pregunta técnica de hoy:**

> ¿Cómo decide el compilador si un programa está bien escrito?

La respuesta requiere dos capas:

**sintaxis** + **semántica**

---

### [F-03]

## Sintaxis

> **Reglas que determinan cuándo un programa está bien formado.**

- Se ocupa de la **forma**
- No decide todavía el comportamiento
- Responde: *¿es este texto un programa válido?*

**Ejemplo canónico:**

```text
if (<expresión>) <sentencia>
```

*Slides cátedra UNTDF 2025 · Sebesta, Cap. 3*

---

### [F-04]

@imagen: content
@prompt-imagen: prompt="Diagrama conceptual que muestra la diferencia entre sintaxis (forma) y semántica (significado): una balanza o dos columnas, una con el texto del programa y otra con el efecto/significado. Infografía técnica académica, fondo claro, sin texto." local_asset="slides/assets/F-04-content.png"

## Semántica

> **Reglas que asignan significado a los programas sintácticamente correctos.**

- Responde: *¿qué hace este programa?*
- La sintaxis sola no alcanza

**Idea clave:**

Un programa puede ser **sintácticamente correcto**
y aun así ser **semánticamente incorrecto**

---

### [F-05]

## Criterios sintácticos de un buen lenguaje

*Slides cátedra UNTDF 2025*

| Criterio | Qué garantiza |
|----------|---------------|
| **Legibilidad** | el código escrito puede leerse y entenderse |
| **Facilidad de escritura** | es natural expresar algoritmos |
| **Facilidad de verificación** | es posible demostrar propiedades |
| **Facilidad de traducción** | el compilador puede procesarlo eficientemente |
| **Carencia de ambigüedad** | cada construcción tiene exactamente un significado |

---

### [F-06]

## Actividad — ¿Qué tipo de error es?

```typescript
const x: number = "hola"

if true { console.log("ok") }

const y = undefined; y.length
```

**Antes de avanzar:** clasificar cada caso en parejas

---

### [F-06b]

## Respuestas

| Caso | Tipo | Dónde aparece |
|------|------|---------------|
| `const x: number = "hola"` | Semántico estático | Type checker |
| `if true { ... }` | Sintáctico | Parser |
| `y = undefined; y.length` | Semántico dinámico | Runtime |

> **Conclusión:** parser, type checker y ejecución no detectan el mismo tipo de problema.
>
> Volveremos a este cuadro al final de la clase.

---

## BLOQUE 2 — DEL TEXTO AL TOKEN (20 min)

---

### [F-07]

## Punto de partida: texto plano

El compilador no recibe "intenciones".

Recibe caracteres:

```text
result = oldsum - value / 100;
```

Primero necesita decidir:

**dónde empieza y dónde termina cada pieza**

*Sebesta, Cap. 4 §4.1*

---

### [F-08]

## Dos niveles de análisis

| Nivel | Qué resuelve | Formalismo |
|-------|--------------|------------|
| **Léxico** | cómo formar palabras válidas | expresiones regulares |
| **Sintáctico** | cómo combinar esas palabras | gramáticas libres de contexto |

**Separarlos sirve para:**

1. simplificar el análisis
2. mejorar eficiencia
3. aislar detalles dependientes del hardware

*Sebesta, Cap. 4 §4.1 — tres razones de separación*

---

### [F-09]

@imagen: content
@prompt-imagen: prompt="Checklist visual de los elementos sintácticos de un lenguaje de programación: caracteres, identificadores, operadores, palabras clave, comentarios, espacios, delimitadores, expresiones, sentencias. Lista limpia estilo infografía académica, sin texto embebido." local_asset="slides/assets/F-09-content.png"

## Vocabulario básico del lenguaje

*Slides cátedra UNTDF 2025*

- **Caracteres** — conjunto de símbolos permitidos (ASCII, Unicode)
- **Identificadores** — nombres para variables, funciones, tipos
- **Operadores** — aritméticos, lógicos, relacionales, de asignación
- **Palabras clave y reservadas** — `if`, `while`, `const`
- **Comentarios** — texto ignorado por el compilador
- **Espacios en blanco** — generalmente ignorados (salvo Python)
- **Delimitadores** — `{}`, `()`, `[]`, `;`
- **Expresiones** — combinaciones que producen un valor
- **Sentencias** — unidades de ejecución

> El lexer clasifica este vocabulario en tokens.

---

### [F-10]

## Lexema y token

**Ejemplo clásico:**

```text
indice = 5 * contador + 1;
```

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

*Slides cátedra UNTDF 2025 · Sebesta, Cap. 4*

---

### [F-11]

## El analizador léxico

```text
Código fuente → [ LEXER ] → tokens → [ PARSER ]
```

**El lexer:**
- agrupa caracteres en lexemas
- descarta espacios y comentarios
- clasifica lexemas en tokens
- entrega al parser una secuencia de tokens

**Todavía no sabe** si un identificador es variable, parámetro o constante — eso lo decide el análisis semántico.

**Razones para separar lexer de parser:** simplificar, eficiencia, portabilidad

*Sebesta, Cap. 4 §4.1*

---

## BLOQUE 3 — GRAMÁTICAS FORMALES (30 min)

---

### [F-12]

## ¿Por qué gramáticas formales?

Describir un lenguaje en castellano o inglés natural es ambiguo.

> FORTRAN: definido con reglas en inglés
> Python: descripción formal con BNF *(gramática libre de contexto)*

Una gramática formal permite:

- especificar con precisión
- validar automáticamente
- construir analizadores directamente sobre esa base

*Slides cátedra UNTDF 2025 · Sebesta, Cap. 3*

---

### [F-13]

## Gramáticas libres de contexto — Chomsky (1959)

Una gramática puede pensarse como la tupla:

```text
(N, T, S, P)
```

| Símbolo | Significado | Ejemplo |
|---------|-------------|---------|
| `N` | no terminales | `<assign>`, `<expr>` |
| `T` | terminales | `A`, `B`, `:=`, `+` |
| `S` | símbolo inicial | `<assign>` |
| `P` | producciones | `<assign> ::= ...` |

*Slides cátedra UNTDF 2025 · Sebesta, Cap. 3*

---

### [F-14]

## BNF — Backus-Naur Form

*Sebesta, Cap. 3 · Slides cátedra UNTDF 2025*

**Metasímbolos:**

- `::=` — "se define como"
- `|` — alternativa
- `< >` — encierra no terminales

```text
<enunc_if> ::= if <expr_log> then <enunc>
             | if <expr_log> then <enunc> else <enunc>
```

**Regla:**
- LHS: no terminal que se define
- RHS: definición (puede contener terminales y no terminales)

---

### [F-15]

## Gramática de trabajo

*Slides cátedra UNTDF 2025*

```text
<assign> ::= <id> := <expr>
<id>     ::= A | B | C
<expr>   ::= <id> + <expr>
           | <id> * <expr>
           | (<expr>)
           | <id>
```

**La usaremos para:**

1. derivar paso a paso
2. construir el árbol sintáctico
3. discutir ambigüedad

---

### [F-16]

## Derivación de `A := B * (A + C)`

*Slides cátedra UNTDF 2025*

```text
<assign>
  ⇒ <id> := <expr>
  ⇒ A := <expr>
  ⇒ A := <id> * <expr>
  ⇒ A := B * <expr>
  ⇒ A := B * (<expr>)
  ⇒ A := B * (<id> + <expr>)
  ⇒ A := B * (A + <expr>)
  ⇒ A := B * (A + <id>)
  ⇒ A := B * (A + C)
```

Cada paso aplica exactamente una producción.

`⇒` se lee "deriva".

---

### [F-17]

## Árbol sintáctico

```text
         <assign>
        /    |    \
      <id>  :=   <expr>
       |         /  |  \
       A      <id>  *  <expr>
               |         |
               B      (<expr>)
                           |
                      <id> + <expr>
                       |       |
                       A      <id>
                               |
                               C
```

- **Nodos internos:** no terminales
- **Hojas:** terminales
- Representa la **estructura jerárquica** de la derivación

*Slides cátedra UNTDF 2025 · Sebesta, Cap. 3*

---

### [F-18]

## Ambigüedad

> **Una gramática es ambigua si genera dos árboles de derivación distintos para la misma cadena.**

*Slides cátedra UNTDF 2025 · Sebesta, Cap. 3*

**Ejemplo:**

```text
J := 1 + 2 * 3
```

Puede leerse como:

- `(1 + 2) * 3` = 9
- `1 + (2 * 3)` = 7

**Consecuencia:** el compilador no sabe cuál árbol construir → **defecto de diseño del lenguaje**.

**Solución:** rediseñar la gramática con precedencia y asociatividad explícitas, o usar regla de desambiguación.

---

### [F-19]

## EBNF — notación extendida

*Slides cátedra UNTDF 2025 · Sebesta, Cap. 3*

| Símbolo | Significado |
|---------|-------------|
| `[x]` | opcional (0 o 1 vez) |
| `{x}` o `{x*}` | repetición (0 o más) |
| `\|` (dentro de `[]`) | alternativa |

```text
<programa>    ::= { <sentencia>* }
<sentencia>   ::= <asignación> | <condicional> | <loop>
<asignación>  ::= <identificador> = <expr>
<condicional> ::= if <expr> { <sentencia>* }
                | if <expr> { <sentencia>* } else { <sentencia>* }
<loop>        ::= while <expr> { <sentencia>* }
```

Menos ruido que BNF pura, misma potencia formal.

---

### [F-20]

@imagen: content
@prompt-imagen: prompt="Pizarrón con derivación parcial del árbol sintáctico de la expresión C := D - E * F, mostrando los pasos de derivación BNF. Estilo ilustración técnica académica, sin texto embebido, fondo claro." local_asset="slides/assets/F-20-content.png"

## Actividad — derivar `C := D − E * F`

**Consigna:**

Dado:
```text
<assign> ::= <id> := <expr>
<id>     ::= A | B | C | D | E | F
<expr>   ::= <id> + <expr> | <id> * <expr>
           | <id> – <expr> | (<expr>) | <id>
```

1. Indicar una derivación para `C := D – E * F`
2. Construir el árbol correspondiente
3. ¿Hay más de un árbol posible? ¿La gramática es ambigua?

---

## BLOQUE 4 — DIAGRAMAS DE SINTAXIS (10 min)

---

### [F-21]

## Diagramas de sintaxis

*Slides cátedra UNTDF 2025 · Sebesta, Cap. 3*

Otra forma de representar la misma gramática.

**Convención:**

- `[ recuadro ]` → no terminal
- `( óvalo )` → terminal

Una cadena es válida si puede "recorrer" el diagrama de izquierda a derecha.

---

### [F-22]

## Ejemplo: condicional

```text
──► (if) ─► [expr] ─► ({) ─► {[sent]*} ─► (}) ──────────────────►
                                │
                                └─► (else) ─► ({) ─► {[sent]*} ─► (}) ─►
```

**Lectura:**
- camino superior: `if` simple
- camino inferior: `if ... else`

Equivale a la regla EBNF del `<condicional>`.

---

### [F-23]

## ¿Para qué sirven los diagramas de sintaxis?

**Para el programador:**
- leer de forma visual la forma válida de una construcción del lenguaje

**Para el implementador:**
- tener una especificación precisa del parser que puede convertirse en código

**Dos usos de la descripción sintáctica** *(slides cátedra UNTDF 2025)*:
1. Ayuda al programador a escribir programas válidos
2. Base para el analizador sintáctico

**Conexión actual:** la documentación oficial de TypeScript usa diagramas de sintaxis para describir construcciones del lenguaje.

---

## BLOQUE 5 — SEMÁNTICA: SÍNTESIS Y TIPOS (12 min)

*Fuente: Sebesta, Cap. 3 §§3.4–3.5*

---

### [F-24]

## Semántica — el significado de los programas

- **Sintaxis** responde: ¿está bien formado?
- **Semántica** responde: ¿qué hace?

Un programa sintácticamente correcto puede tener semántica inválida.

Sin semántica formalmente especificada, el comportamiento del lenguaje
depende de la implementación → no portable entre compiladores / intérpretes.

> *"There is no universal method for describing the semantics of a programming language that is generally acceptable."*
>
> — Sebesta (2019)

**Dos grandes dimensiones:**
- **estática** — verificada antes de ejecutar
- **dinámica** — significado en ejecución

---

### [F-25]

## Semántica estática — gramáticas de atributos

*Sebesta, Cap. 3 §3.4 · Knuth (1968)*

**El problema:** no toda restricción semántica puede expresarse con BNF.

Ejemplo: la compatibilidad de tipos en una asignación es **sensible al contexto** — no es una regla libre de contexto.

**Solución: gramáticas de atributos**
- Extienden BNF agregando **atributos** (ej.: tipo, valor) a los símbolos
- Definen **reglas semánticas** que calculan esos atributos a partir del árbol
- Permiten describir restricciones contextuales de forma rigurosa

**Cubren típicamente:**
- compatibilidad de tipos en asignaciones y llamadas
- declaración antes de uso de variables
- aridad de funciones

---

### [F-26]

## TypeScript como semántica estática en acción

```typescript
const x: number = "texto"
// → Type 'string' is not assignable to type 'number'
```

- El **parser** construyó el árbol → no hay error sintáctico
- El **type checker** evalúa atributos (tipos) sobre ese árbol
- Rechaza porque los tipos son incompatibles → error **semántico estático**

**Type soundness:**
> Si el programa pasa el type checker, no producirá errores de tipo en runtime.

`tsc` ES un intérprete de semántica estática: evalúa el árbol sin ejecutarlo.

---

### [F-27]

## Tres enfoques de semántica dinámica

*Sebesta, Cap. 3 §3.5*

| Enfoque | Idea central | Origen |
|---------|--------------|--------|
| **Operacional** | el significado = la secuencia de pasos en una máquina abstracta | Landin (1964); SOS, Plotkin (1981) |
| **Denotacional** | el significado = función matemática estado → estado | Scott & Strachey (1970) |
| **Axiomática** | el significado = aserciones lógicas (pre/postcondiciones) | Floyd (1967); Hoare (1969) |

- No existe método universalmente aceptado
- Cada uno sirve para distintos propósitos: implementación, verificación, corrección formal
- El rigor formal de cada enfoque corresponde a **Semántica Formal / Lógica**

---

### [F-28]

## Síntesis — tres niveles de corrección en TypeScript

```typescript
// Error sintáctico — el parser falla (no puede construir el árbol):
function foo( { return 42 }      // falta ')'

// Error semántico estático — el type-checker falla (árbol válido, tipos incompatibles):
const x: number = "texto"        // violación de tipo en compilación

// Error semántico dinámico — falla en runtime (el compilador no lo detecta):
const arr: number[] = []
console.log(arr[100].toString()) // undefined.toString() en ejecución
```

| Nivel | Herramienta | Cuándo |
|-------|-------------|--------|
| Sintáctico | Parser | compilación |
| Semántico estático | Type checker | compilación |
| Semántico dinámico | Runtime | ejecución |

---

## BLOQUE 6 — PIPELINE E IA (15 min)

---

### [F-29]

## El pipeline del compilador

```text
Código fuente
      ↓ Lexer
   Tokens
      ↓ Parser
   Árbol sintáctico
      ↓ Análisis semántico / type checking
   Árbol anotado
      ↓ Generación de código (compilador)
        ó ejecución directa (intérprete)
```

Cada etapa responde una pregunta distinta.

`tsc` hace: lexer → parser → type checker → emite JavaScript.

*Sebesta, Cap. 4 §§4.1–4.3*

---

### [F-30]

## Dos ideas de parsing

*Sebesta, Cap. 4 §§4.3–4.4 (conceptual)*

| Estrategia | Intuición | Dirección |
|------------|-----------|-----------|
| **Top-down** | partir del símbolo inicial, derivar hasta los tokens | S → ... → tokens |
| **Bottom-up** | partir de los tokens, reducir hasta el símbolo inicial | tokens → ... → S |

**Importante para hoy:**

No estudiamos algoritmos concretos (recursive-descent, LR).

Solo ubicamos el problema conceptualmente.

---

### [F-31]

@imagen: content
@prompt-imagen: prompt="Diagrama del pipeline completo de un compilador e intérprete: lexer, parser, type checker, generación de código vs ejecución. Comparación lado a lado compilador vs intérprete. Infografía técnica académica clara, fondo blanco, sin texto embebido." local_asset="slides/assets/F-31-content.png"

## Compilador e intérprete revisitado

- Ambos necesitan análisis léxico y sintáctico
- Ambos aplican algún criterio semántico
- La diferencia aparece **después** del análisis semántico:
  - el **compilador** traduce a otro lenguaje (ej.: JavaScript)
  - el **intérprete** ejecuta el árbol directamente

**TypeScript con `tsc`:**

```text
lexer → parser → type checker → emite JavaScript
```

El mensaje de error de `tsc` incluye línea y columna → evidencia de que el lexer registró la posición de cada token.

---

### [F-32]

## Ejemplo práctico — guiar estructura con prompt blando

**Tarea:** extraer pendientes desde una nota de reunión.

**Prompt sin estructura formal:**
```text
Leé esta nota y devolvé las acciones pendientes.
```
→ variación libre en formato, campos, orden

**Prompt con estructura JSON:**
```text
Devolvé un JSON con esta forma:
{
  "action_items": [
    {"description": "...", "due_date": "...", "owner": "..."}
  ]
}
```
→ más predecible, pero sigue siendo una guía blanda.

**Problema:** el modelo puede omitir campos, cambiar orden, agregar claves.

---

### [F-33]

## El mismo caso — guiar estructura con EBNF

**Prompt + gramática simplificada:**

```text
Devolvé una salida que respete esta EBNF:

<salida> ::= '{' '"action_items"' ':' '[' <item> { ',' <item> } ']' '}'
<item>   ::= '{' '"description"' ':' <string> ','
                 '"due_date"'    ':' <string> ','
                 '"owner"'       ':' <string> '}'
```

**Efecto:** ya no sugerimos forma — definimos qué secuencias son válidas.

> En sistemas actuales esto entra como JSON Schema, tipos o CFG compilada para **constrained decoding**.
> Acá usamos EBNF como simplificación didáctica de esa idea formal.

*Referencia reciente: Gong (2026), arXiv:2602.21257 — SPL: Structured Prompt Language*

---

### [F-34]

## De Chomsky a constrained decoding

```text
1957  Chomsky — gramáticas formales
1960  Backus-Naur — BNF para Algol60
...   EBNF, diagramas de sintaxis, parsers LR
2023  Constrained decoding en LLMs (Willard & Louf, Outlines)
2026  Structured Prompt Language con EBNF (Gong, arXiv:2602.21257)
```

La formalización de la sintaxis **no es historia**.

Es infraestructura activa.

*Alpay & Senturk (2026), arXiv:2603.05540 — Attention Meets Reachability: Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding*

---

## CIERRE

---

### [F-35]

@imagen: content
@prompt-imagen: prompt="Mapa conceptual visual de la clase de Sintaxis y Semántica: seis bloques conectados por flechas — Sintaxis, Léxico, Gramáticas, Diagramas, Semántica, Pipeline. Infografía académica limpia, fondo claro, sin texto embebido." local_asset="slides/assets/F-35-content.png"

## Mapa final de la clase

1. **Sintaxis** — forma válida de los programas
2. **Léxico** — texto plano → secuencia de tokens
3. **Gramáticas** — tokens → estructura jerárquica (BNF/EBNF)
4. **Diagramas** — representación gráfica equivalente
5. **Semántica** — significado vía tipos, enfoques formales y runtime
6. **Pipeline** — integración en compiladores, intérpretes y LLMs

---

### [F-36]

## Preguntas para cerrar

- ¿Qué detecta el **parser** que no detecta el type checker?
- ¿Qué detecta el **type checker** que no detecta el parser?
- ¿Por qué una gramática **ambigua** es un problema de diseño?
- ¿Cuál es la diferencia entre **semántica estática** y **semántica dinámica**?
- ¿Dónde reaparecen hoy BNF y EBNF **fuera de compiladores clásicos**?

---

### [F-37]

## Referencias

- **Slides de cátedra UNTDF 2025** — Sintaxis de Lenguajes de Programación (baseline)
- **Sebesta, R.** (2019). *Concepts of Programming Languages*, 12ª ed. Cap. 3 (gramáticas, semántica) y Cap. 4 (análisis léxico y sintáctico)
- **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms*. Cap. 4 (nombres y entorno) — para Tema 09
- **Willard, B. T. & Louf, R.** (2023). *Efficient Guided Generation for Large Language Models*. arXiv:2307.09702 — Outlines, constrained decoding
- **Beurer-Kellner, L. et al.** (2023). *Prompting Is Programming: A Query Language for Large Language Models*. PLDI'23. arXiv:2212.06094
- **Geng, S. et al.** (2023). *Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning*. EMNLP 2023. arXiv:2305.13971
- **Gong, L.** (2026). *Structured Prompt Language: Declarative Context Management for LLMs*. arXiv:2602.21257
- **Alpay, T. & Senturk, E.** (2026). *Attention Meets Reachability: Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding*. arXiv:2603.05540
