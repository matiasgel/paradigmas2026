<!-- markdownlint-disable MD001 MD025 MD032 MD036 MD060 -->

# Filminas — Tema 02: Sintaxis y Semántica de Lenguajes

> **Estado:** REGENERADA desde `diseno.md` rediseñado
> **Agente:** Dr. Roberto ✍️ (class-writer)
> **Fecha de generación:** 2026-03-18
> **Duración total:** 120 minutos (constraint absoluto)
> **Clase:** 2 de 2 — Semana 1
> **Perfil docente:** profesor-teorico
> **Lenguaje principal:** TypeScript
> **Workflow:** topic-cycle / Step 4

---

### [F-00]

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
| 3 | 30 | BNF, EBNF, derivación y ambigüedad |
| 4 | 10 | Diagramas de sintaxis |
| 5 | 20 | Type checking, nombres y entorno |
| 6 | 15 | Pipeline del compilador e IA |

**Total:** 120 minutos

---

## BLOQUE 1 — SINTAXIS Y SEMÁNTICA (20 min)

### [F-02]

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

---

### [F-04]

## Semántica

> **Reglas que asignan significado a los programas sintácticamente correctos.**

- Responde: *¿qué hace este programa?*
- La sintaxis sola no alcanza

**Idea clave:**

Un programa puede ser **sintácticamente correcto**
y aun así ser **semánticamente incorrecto**

---

### [F-05]

## Actividad — ¿Qué tipo de error es?

```typescript
const x: number = "hola"

if true { console.log("ok") }

const y = undefined; y.length
```

**Antes de avanzar:**

clasificar cada caso en parejas

---

### [F-06]

## Respuestas

| Caso | Tipo | Dónde aparece |
|------|------|---------------|
| `const x: number = "hola"` | Semántico estático | Type checker |
| `if true { ... }` | Sintáctico | Parser |
| `const y = undefined; y.length` | Semántico dinámico | Runtime |

> **Conclusión:** parser, type checker y ejecución no detectan el mismo tipo de problema.

---

## BLOQUE 2 — DEL TEXTO AL TOKEN (20 min)

### [F-07]

## Punto de partida: texto plano

El compilador no recibe "intenciones".

Recibe caracteres:

```text
result = oldsum - value / 100;
```

Primero necesita decidir:

**dónde empieza y dónde termina cada pieza**

---

### [F-08]

## Dos niveles de análisis

| Nivel | Qué resuelve |
|-------|--------------|
| Léxico | cómo formar palabras válidas |
| Sintáctico | cómo combinar esas palabras |

**Separarlos sirve para:**

1. simplificar el análisis,
2. mejorar eficiencia,
3. aislar detalles de entrada.

---

### [F-09]

## Vocabulario básico del lenguaje

- Caracteres
- Identificadores
- Operadores
- Palabras clave y reservadas
- Comentarios
- Espacios en blanco
- Delimitadores y corchetes
- Expresiones
- Sentencias

> El lexer clasifica este vocabulario.

---

### [F-10]

## Lexema y token

**Ejemplo:**

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

---

### [F-11]

## El analizador léxico

```text
Código fuente → [ LEXER ] → tokens → [ PARSER ]
```

- Agrupa caracteres
- Descarta espacios y comentarios
- Clasifica lexemas
- Le entrega al parser una secuencia de tokens

**Todavía no sabe** si un identificador es variable, parámetro o constante.

---

## BLOQUE 3 — GRAMÁTICAS FORMALES (30 min)

### [F-12]

## ¿Por qué gramáticas formales?

Describir un lenguaje en castellano o inglés natural es ambiguo.

Una gramática formal permite:

- especificar con precisión,
- validar automáticamente,
- construir analizadores sobre esa base.

---

### [F-13]

## Gramáticas libres de contexto

Una gramática puede pensarse como la tupla:

```text
(N, T, S, P)
```

| Símbolo | Significado |
|---------|-------------|
| `N` | no terminales |
| `T` | terminales |
| `S` | símbolo inicial |
| `P` | producciones |

---

### [F-14]

## BNF — Backus-Naur Form

**Metasímbolos:**

- `::=` se define como
- `|` alternativa
- `<...>` no terminal

```text
<enunc_if> ::= if <expr_log> then <enunc>
             | if <expr_log> then <enunc> else <enunc>
```

---

### [F-15]

## Gramática de trabajo

```text
<assign> ::= <id> := <expr>
<id>     ::= A | B | C
<expr>   ::= <id> + <expr>
           | <id> * <expr>
           | (<expr>)
           | <id>
```

**La usaremos para:**

1. derivar,
2. dibujar un árbol,
3. discutir ambigüedad.

---

### [F-16]

## Derivación de `A := B * (A + C)`

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

Cada paso aplica una producción.

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

**Nodos internos:** no terminales  
**Hojas:** terminales

---

### [F-18]

## Ambigüedad

> Una gramática es ambigua si permite dos árboles distintos para la misma cadena.

**Ejemplo:**

```text
J := 1 + 2 * 3
```

Puede leerse como:

- `(1 + 2) * 3`
- `1 + (2 * 3)`

**Problema:** dos significados posibles.

---

### [F-19]

## EBNF — notación extendida

| Símbolo | Significado |
|---------|-------------|
| `[x]` | opcional |
| `{x}` | repetición |

```text
<programa>   ::= { <sentencia>* }
<sentencia>  ::= <asignación> | <condicional> | <loop>
<condicional>::= if <expr> { <sentencia>* }
               | if <expr> { <sentencia>* } else { <sentencia>* }
```

Menos ruido, misma idea formal.

---

### [F-20]

## Actividad breve

**Consigna:**

Para `C := D - E * F`:

1. indicar una posible derivación,
2. discutir el agrupamiento,
3. decir si la gramática deja dudas o no.

---

## BLOQUE 4 — DIAGRAMAS DE SINTAXIS (10 min)

### [F-21]

## Diagramas de sintaxis

Otra forma de escribir la misma gramática.

**Convención mínima:**

- recuadro → no terminal
- terminal destacado → símbolo concreto

Una cadena es válida si puede "recorrer" el diagrama.

---

### [F-22]

## Ejemplo: condicional

```text
──► (if) ─► <expr> ─► ({) ─► {sentencias} ─► (}) ─────────►
                                 │
                                 └──► (else) ─► ({) ─► {sentencias} ─► (}) ─►
```

**Lectura:**

- camino superior: `if` simple
- camino inferior: `if ... else`

---

### [F-23]

## ¿Para qué sirven?

**Para el programador:**

- leer la forma válida de una construcción

**Para el implementador:**

- tener una especificación precisa del parser

**Para la documentación:**

- comunicar estructura con carga visual menor que BNF larga

---

## BLOQUE 5 — SEMÁNTICA PRAGMÁTICA (20 min)

### [F-24]

## ¿Qué agrega la semántica?

La sintaxis responde:

> ¿está bien formado?

La semántica responde:

> ¿qué significa y qué efecto tiene?

**Consecuencia:**

no todo programa con forma correcta es aceptable o correcto.

---

### [F-25]

## Semántica estática: el type checker

```typescript
const x: number = "texto"
```

- El parser puede construir el árbol.
- El programa sigue siendo rechazado.
- El motivo no es de forma sino de tipos.

> El type checker es una herramienta de semántica estática.

---

### [F-26]

## Nombres y objetos denotables

> Un nombre es una secuencia de caracteres que denota otro objeto.

Puede denotar:

- variables,
- parámetros,
- funciones,
- tipos,
- constantes,
- operaciones predefinidas.

**Nombre ≠ objeto**

---

### [F-27]

## Entorno

> El entorno es el conjunto de asociaciones nombre → objeto disponibles en un punto del programa.

```text
{
  x        → 5
  contador → 12
  suma     → 17
}
```

El entorno permite saber a qué refiere cada nombre en cada contexto.

---

### [F-28]

## Binding — ligadura

> Binding = asociación entre un nombre y el objeto que denota.

**Puede aparecer en distintas fases:**

| Fase | Ejemplo |
|------|---------|
| Diseño del lenguaje | `+`, `int`, `true` |
| Escritura | declaraciones del programador |
| Compilación | posiciones o estructuras resueltas estáticamente |
| Ejecución | variables locales y memoria dinámica |

---

### [F-29]

## Intuición mínima de estado

```text
x = 5; y = x + 1
```

Puede pensarse como transformación:

```text
{} → {x = 5} → {x = 5, y = 6}
```

Con esto alcanza para esta materia.

**No** vamos hoy a reglas formales SOS ni semántica denotacional.

---

### [F-30]

## Tres niveles de error en TypeScript

```typescript
function foo( { return 42 }
const x: number = "texto"
const arr: number[] = []
console.log(arr[100].toString())
```

| Caso | Detecta |
|------|---------|
| falta `)` | parser |
| tipo incompatible | type checker |
| acceso inválido en ejecución | runtime |

---

## BLOQUE 6 — PIPELINE E IA (15 min)

### [F-31]

## El pipeline completo

```text
Código fuente
   ↓
Lexer
   ↓
Tokens
   ↓
Parser
   ↓
Árbol
   ↓
Análisis semántico / type checking
   ↓
Emisión o ejecución
```

Cada etapa responde una pregunta distinta.

---

### [F-32]

## Dos ideas de parsing

| Estrategia | Intuición |
|------------|-----------|
| Top-down | partir del símbolo inicial |
| Bottom-up | partir de los tokens |

**Importante:**

Hoy no estudiamos algoritmos concretos.

Solo ubicamos el problema conceptualmente.

---

### [F-33]

## Compilador e intérprete revisitado

- Ambos necesitan análisis léxico y sintáctico.
- Ambos necesitan algún criterio semántico.
- La diferencia aparece después:
  - uno traduce,
  - el otro ejecuta directamente o con menos mediación.

**TypeScript:**

`lexer → parser → type checker → emite JavaScript`

---

### [F-34]

## Ejemplo práctico — guiar estructura sin EBNF

**Tarea:** extraer pendientes desde una nota de reunión.

**Prompt:**

```text
Leé esta nota y devolvé un JSON con esta forma:
{
   "action_items": [
      {"description": "...", "due_date": "...", "owner": "..."}
   ]
}

Nota: "Ana prepara las filminas para el viernes.
Luis revisa bibliografía. Marta confirma aula."
```

**Qué guía la salida:**

- el ejemplo de formato,
- los nombres de campos,
- la instrucción "devolvé JSON".

**Problema:** sigue siendo una guía blanda.

---

### [F-35]

## El mismo caso — guiar estructura con EBNF

**Prompt + gramática simplificada:**

```text
Devolvé una salida que respete esta EBNF:

<salida> ::= '{' '"action_items"' ':' '[' <item> { ',' <item> } ']' '}'
<item> ::= '{' '"description"' ':' <string> ','
                         '"due_date"' ':' <string> ','
                         '"owner"' ':' <string> '}'
```

**Efecto:**

- ya no solo sugerimos forma,
- definimos qué secuencias son válidas,
- reducimos comas de más, campos faltantes o orden inválido.

> En sistemas actuales esto suele entrar como JSON Schema, tipos o CFG compilada para constrained decoding.
> Acá usamos **EBNF como simplificación didáctica** de esa idea formal.

**Apoyo actual:**

- Para uso **explícito de EBNF** en un lenguaje de prompting para LLMs: Gong (2026) presenta SPL y reporta una gramática formal EBNF: [arXiv:2602.21257](https://arxiv.org/abs/2602.21257)
- Para *grammar-constrained decoding*: Alpay y Senturk (2026) analizan decoding guiado por CFG y sus costos estructurales: [arXiv:2603.05540](https://arxiv.org/abs/2603.05540)

---

### [F-36]

## De Chomsky a constrained decoding

```text
1957  gramáticas formales
1960  BNF
...   EBNF y parsers
2023  constrained decoding en LLMs
```

La formalización de la sintaxis sigue viva.

No es arqueología: es infraestructura.

---

### [F-37]

## Mapa final de la clase

1. Sintaxis: forma válida
2. Léxico: texto → tokens
3. Gramática: tokens → estructura
4. Diagramas: representación visual de la sintaxis
5. Semántica: significado mediante tipos, nombres y entorno
6. Pipeline: integración en compiladores e IA

---

### [F-38]

## Preguntas para cerrar

- ¿Qué detecta el parser que no detecta el type checker?
- ¿Qué detecta el type checker que no detecta el parser?
- ¿Por qué una gramática ambigua es un problema de diseño?
- ¿Qué papel cumple el entorno en el significado de un programa?
- ¿Dónde reaparecen hoy BNF y EBNF fuera de compiladores clásicos?

---

### [F-39]

## Referencias

- Slides de cátedra UNTDF 2025
- Sebesta — análisis léxico y sintáctico
- Gabbrielli & Martini — nombres y entorno
- Referencias recientes sobre constrained decoding listadas en `diseno.md`
- OpenAI — Structured Outputs y constrained decoding con CFG
- Outlines / LMQL — ejemplos de generación estructurada guiada
- Gong (2026) — *Structured Prompt Language: Declarative Context Management for LLMs*, [arXiv:2602.21257](https://arxiv.org/abs/2602.21257)
- Alpay, Senturk (2026) — *Attention Meets Reachability: Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding*, [arXiv:2603.05540](https://arxiv.org/abs/2603.05540)
