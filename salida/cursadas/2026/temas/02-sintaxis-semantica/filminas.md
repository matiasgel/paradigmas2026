# Filminas — Tema 02: Sintaxis y Semántica de Lenguajes

> **Estado:** APROBADO
> **Aprobado por:** Matías Gel (docente)
> **Fecha de aprobación:** 2026-03-10
> **Agente:** Dr. Roberto ✍️ (class-writer)
> **Fecha de generación:** 2026-03-10
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

> *"¿Cómo sabe el compilador si tu programa está bien escrito?  
> ¿Y sabe siempre cuándo está mal?"*

---

### [F-01]

## Agenda

| Bloq | Minutos | Tema |
|------|---------|------|
| 1 | 20 | Sintaxis y semántica: conceptos fundamentales |
| 2 | 20 | Estructura léxica: del texto al token |
| 3 | 30 | Gramáticas formales: BNF, EBNF, ambigüedad |
| 4 | 10 | Diagramas de sintaxis |
| 5 | 20 | Semántica: nombres, entorno, ligaduras |
| 6 | 15 | Parser + Gramáticas en IA (cierre) |

**Total: 120 minutos**

---

## BLOQUE 1 — SINTAXIS Y SEMÁNTICA (20 min)

### [F-02]

## ¿Cómo sabe el compilador?

**Tema 01 cerró con:**
> TypeScript compila a JavaScript, que ejecuta en V8

**Hoy respondemos la pregunta técnica subyacente:**
> ¿Cómo sabe el compilador si un programa está bien escrito?  
> ¿Y qué significa que esté "bien"?

🔗 *La respuesta requiere dos conceptos: **sintaxis** y **semántica**.*

---

### [F-03]

## Sintaxis

> **Conjunto de reglas que determinan cuándo un programa está bien formado.**

- Se ocupa de la **forma** — no del comportamiento
- Responde: *¿es este texto un programa válido?*

**Ejemplo — C:**
```
if (<expresión>) <sentencia>
```
Cualquier desviación de esta forma → **error sintáctico**

**Criterios de buena sintaxis:**
legibilidad · facilidad de escritura · verificabilidad · traducibilidad · no ambigüedad

---

### [F-04]

## Semántica

> **Le asigna significado a los programas sintácticamente correctos.**

- Responde: *¿qué hace este programa?*
- Sintaxis correcta **no implica** programa correcto

**Ejemplo TypeScript:**
```typescript
x = null         // ✓ sintácticamente válido
                 // ⚠ puede ser error semántico
```

---

### [F-05]

## Actividad — ¿Sintaxis o semántica?

```typescript
// Caso A
const x: number = "hola"

// Caso B
if true { console.log("ok") }

// Caso C
const y = undefined; y.length
```

*Antes de la próxima slide: ¿cuál es cuál?*

---

### [F-06]

## Respuestas

| Caso | Tipo de error | Cuándo se detecta |
|------|--------------|-------------------|
| A — `const x: number = "hola"` | **Semántico estático** (type error) | Compilación — `tsc` lo detecta |
| B — `if true { ... }` | **Sintáctico** | Compilación — falta `()` |
| C — `const y = undefined; y.length` | **Semántico dinámico** | Runtime — `tsc` no puede saberlo |

> ⚡ **Punto clave:** Un programa puede ser sintácticamente correcto y semánticamente incorrecto. El compilador siempre detecta errores sintácticos, pero NO siempre detecta errores semánticos.

---

## BLOQUE 2 — ESTRUCTURA LÉXICA (20 min)

### [F-07]

## El punto de partida: texto plano

El compilador recibe el programa como **una cadena de caracteres**.

Antes de entender la estructura, necesita identificar las **palabras**.

```
result = oldsum - value / 100;
```

↓ ¿Cómo sabe el compilador dónde empieza y termina cada unidad?

---

### [F-08]

## Dos niveles de análisis

| Nivel | Qué define | Ejemplo |
|-------|-----------|---------|
| **Reglas léxicas** | Cómo combinar caracteres en palabras | Java es case-sensitive: `myVar ≠ myvar` |
| **Reglas sintácticas** | Cómo combinar palabras en sentencias | `if (<expr>) <sent>` |

**¿Por qué separarlos?**
1. **Simplicidad:** el parser opera sobre tokens, no caracteres
2. **Eficiencia:** el lexer usa autómatas rápidos
3. **Portabilidad:** cambiar el charset solo afecta al lexer

---

### [F-09]

## Lexemas y Tokens

> **Lexema:** unidad sintáctica de más bajo nivel — la cadena concreta
> **Token:** categoría abstracta del lexema

Analogía lingüística: "perro", "gato", "ave" → distintos lexemas, mismo token: **SUSTANTIVO**

---

### [F-10]

## Tokenización de `indice = 5 * contador + 1;`

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

⚑ `indice` y `contador` → mismo token, distintos lexemas. El lexer no sabe que son variables.

---

### [F-11]

## El analizador léxico

**Función:** transforma cadena de caracteres → secuencia de tokens

**Posición en el pipeline:**
```
Código fuente → [LEXER] → tokens → [PARSER] → árbol
```

**En TypeScript:**
```
tsc --listEmittedFiles archivo.ts
```
Paso 1 interno de `tsc`: **lexer**  
Los mensajes de error con número de línea y columna vienen del lexer.

---

## BLOQUE 3 — GRAMÁTICAS FORMALES (30 min)

### [F-12]

## El problema del lenguaje natural

**FORTRAN** se especificaba con reglas en inglés → el inglés es ambiguo → dos compiladores podían comportarse distinto ante el mismo programa.

**Python** tiene una gramática BNF oficial → todo compilador conforme acepta exactamente los mismos programas.

> Una gramática formalmente especificada permite **verificar automáticamente** si un programa es válido.

---

### [F-13]

## Gramáticas LCF — Clasificación de Chomsky (1959)

Una gramática es la tupla `(N, T, S, P)`:

| Componente | Nombre | Descripción |
|-----------|--------|-------------|
| **N** | No terminales | Abstracciones / categorías |
| **T** | Terminales | Lexemas / tokens reales del código |
| **S** | Símbolo inicial | Punto de partida de toda derivación |
| **P** | Producciones | Reglas: cómo expandir no terminales |

---

### [F-14]

## BNF — Backus-Naur Form

**Metasímbolos:**
- `::=` — "se define como"
- `|` — alternativa ("o")
- `< >` — encierra no terminales

```
<assign>    ::= <var> = <expression>

<enunc_if>  ::= if <expr_log> then <enunc>
              | if <expr_log> then <enunc> else <enunc>
```

📌 **Regla:** LHS (no terminal a definir) → RHS (su definición)

---

### [F-15]

## Gramática de trabajo

```
<assign> ::= <id> := <expr>
<id>     ::= A | B | C
<expr>   ::= <id> + <expr>
           | <id> * <expr>
           | (<expr>)
           | <id>
```

**Usaremos esta gramática para:**
1. Derivar `A := B * (A + C)` paso a paso
2. Construir el árbol sintáctico
3. Ver un caso de ambigüedad

---

### [F-16]

## Derivación de `A := B * (A + C)`

```
<assign>
  ⇒ <id> := <expr>              [assign]
  ⇒ A := <expr>                 [id → A]
  ⇒ A := <id> * <expr>          [expr → id * expr]
  ⇒ A := B * <expr>             [id → B]
  ⇒ A := B * (<expr>)           [expr → (expr)]
  ⇒ A := B * (<id> + <expr>)    [expr → id + expr]
  ⇒ A := B * (A + <expr>)       [id → A]
  ⇒ A := B * (A + <id>)         [expr → id]
  ⇒ A := B * (A + C)            [id → C]
```

Cada paso aplica exactamente **una producción**. La cadena intermedia = **forma de sentencia**.

---

### [F-17]

## Árbol de derivación (parse tree)

```
         <assign>
        /    |    \
      <id>  :=   <expr>
       |         /  |  \
       A      <id>  *  <expr>
               |         |
               B      (<expr>)
                           |
                      <id>  +  <expr>
                       |          |
                       A        <id>
                                  |
                                  C
```

**Nodos internos:** no terminales
**Nodos hoja:** terminales
**El árbol muestra la estructura jerárquica** — qué se agrupa con qué.

---

### [F-18]

## Gramática ambigua

> **Definición:** una gramática es ambigua si permite **dos árboles de derivación distintos** para la misma cadena.

**Ejemplo:** `J := 1 + 2 * 3` con gramática sin precedencia:

| Árbol 1 | Árbol 2 |
|---------|---------|
| `(1 + 2) * 3 = 9` | `1 + (2 * 3) = 7` |

**Consecuencia:** el compilador no sabe cuál árbol elegir → no sabe cuál es el comportamiento correcto.

**Solución:** codificar precedencia y asociatividad de operadores en la gramática.

---

### [F-19]

## EBNF — Extended BNF

**Extensiones sobre BNF:**

| Símbolo | Significado |
|---------|------------|
| `[ x ]` | x es **opcional** (0 o 1 vez) |
| `{ x }` | x se **repite** (0 o más veces) |
| `\|` dentro de `[ ]` | alternativas dentro del grupo |

```
<programa>   ::= { <sentencia>* }
<sentencia>  ::= <asignación> | <condicional> | <loop>
<condicional>::= if <expr> { <sentencia>* }
               | if <expr> { <sentencia>* } else { <sentencia>* }
<loop>       ::= while <expr> { <sentencia>* }
```

---

### [F-20]

## Actividad (5 min)

> **Dado `C := D – E * F`:**
> 1. Derivar usando la gramática del ejemplo
> 2. Dibujar el árbol de derivación
> 3. ¿La gramática es ambigua para esta expresión?

*(Usar pizarra o papel)*

---

## BLOQUE 4 — DIAGRAMAS DE SINTAXIS (10 min)

### [F-21]

## Diagramas de sintaxis (Railroad Diagrams)

Representación **gráfica** equivalente a EBNF.

**Convención:**
- `[Recuadro]` → no terminal (categoría)
- `(Óvalo)` → terminal (token concreto)

**Cómo leer:** una cadena es válida si podés "viajar" de izquierda a derecha atravesando el diagrama.

---

### [F-22]

## Diagrama: `<condicional>`

```
         ┌─────────────────────────────────────────┐
         │                                         │
──►─(if)─►─(expr)─►─({)─►─{sentencias}─►─(})─────►────►
                                          │
                                          └──►─(else)─►─({)─►─{sentencias}─►─(})─►
```

**Lectura:** el camino superior es el `if` simple.  
El camino inferior agrega el `else`.  
Ambos son válidos → la gramática lo expresa sin recursión.

---

### [F-23]

## Usos de la descripción sintáctica

**Para el programador:**
→ Entender qué construcciones son válidas en el lenguaje
→ Escribir código correcto

**Para el compilador:**
→ La gramática es la especificación que el parser implementa
→ Sin gramática formal → ambigüedad → comportamiento impredecible

> 💡 La documentación oficial de TypeScript usa diagramas de sintaxis  
> para documentar cada construcción del lenguaje.

---

## BLOQUE 5 — SEMÁNTICA (20 min)

### [F-24]

## Más allá de la sintaxis

**Sintaxis correcta ≠ programa correcto**

| Tipo | Ejemplo | Detectado por |
|------|---------|--------------|
| Error semántico estático | `const x: number = "hola"` | type-checker (`tsc`) |
| Error semántico dinámico | `arr[100].toString()` en array vacío | Runtime |

> Sin semántica formal → el comportamiento del lenguaje depende de la implementación → el mismo programa puede comportarse diferente en dos compiladores distintos.

---

### [F-25]

## Nombres y objetos denotables

> Un **nombre** es una secuencia de caracteres que *denota* (refiere a) otro objeto.

**Nombre ≠ objeto que denota:**
- El mismo objeto puede tener varios nombres → **aliasing**
- El mismo nombre puede referir a objetos distintos en distintos contextos → **scope**

**Objetos denotables:**
variables · parámetros formales · procedimientos · tipos · módulos · constantes · excepciones · operaciones predefinidas

---

### [F-26]

## El entorno (environment)

> El **entorno** es el componente de la máquina abstracta que mantiene las asociaciones `nombre → objeto` en cada punto de ejecución.

```
Entorno en un instante de ejecución:
{
  x        → 5
  contador → 12
  suma     → 17
}
```

*En cada instante, el entorno sabe a qué objeto refiere cada nombre.*

---

### [F-27]

## Binding — ligadura

> Una **ligadura** es la asociación entre un nombre y un objeto denotable.

| Fase | Ejemplo |
|------|---------|
| Diseño del lenguaje | `+` se liga a la operación suma |
| Escritura del programa | `const PI = 3.14159` |
| Compilación | variable → posición de memoria |
| Ejecución | variable local → valor al llamar la función |

**Estático:** antes de la ejecución (diseño, escritura, compilación)
**Dinámico:** durante la ejecución

*Las reglas de visibilidad (scope) → **Tema 09***

---

### [F-28]

## Semántica operacional

> Define el significado de un programa como la **secuencia de estados** que produce al ejecutarse.

- **Estado:** conjunto de pares `(nombre, valor)` en un instante
- **Programa:** transformación estado inicial → estado final

**Ejemplo:**
```
Programa: x := 5; y := x + 1

Estado inicial: { }
  → x := 5    → { x = 5 }
  → y := x+1  → { x = 5, y = 6 }
Estado final: { x = 5, y = 6 }
```

🔗 *Conecta con Tema 01: la semántica en una máquina abstracta es su modelo de ejecución.*

---

## BLOQUE 6 — PARSER + CIERRE (15 min)

### [F-29]

## El compilador: pipeline completo

```
Código fuente (texto)
       ↓
  [Lexer]   → secuencia de tokens
       ↓
  [Parser]  → árbol de derivación
       ↓
  [Type-checker] → árbol anotado con tipos
       ↓
  ┌──────────────────────────┐
  │ Compilador | Intérprete  │
  │ ↓ código   | ↓ ejecuta   │
  └──────────────────────────┘
```

`tsc` ejecuta este pipeline completo y emite JavaScript.

---

### [F-30]

## Dos estrategias de parsing

| Estrategia | Dirección | Característica |
|-----------|-----------|---------------|
| **Top-down** (descendente) | Símbolo inicial → tokens | Intuitivo, legible |
| **Bottom-up** (ascendente) | Tokens → símbolo inicial | Más poderoso, más complejo |

*Los algoritmos específicos (recursive-descent, LR) → Teoría de Compiladores (fuera del scope).*

---

### [F-31]

## Síntesis: errores en TypeScript

```typescript
// Error SINTÁCTICO — falla en el parser:
function foo( { return 42 }
// tsc: "error TS1005: ')' expected"

// Error SEMÁNTICO ESTÁTICO — falla en type-checking:
const x: number = "texto"
// tsc: "error TS2322: Type 'string' is not assignable to type 'number'"

// Error SEMÁNTICO DINÁMICO — falla en runtime:
const arr: number[] = []
console.log(arr[100].toString())
// TypeError: Cannot read properties of undefined
```

---

### [F-32]

## Las gramáticas hoy: IA generativa

**El problema:** los LLMs generan texto libre. ¿Cómo garantizar JSON válido, SQL válido, código válido?

**Constrained decoding** (Willard & Louf, 2023):
1. Compilar gramática EBNF → autómata de estados finitos
2. En cada paso de generación: el autómata filtra tokens válidos
3. El modelo **solo puede producir** tokens en derivaciones válidas

**Herramientas actuales:**
- **Outlines** (Python) — gramáticas BNF/EBNF como input del programador
- **LMQL** — lenguaje de consulta con restricciones declarativas sobre LLMs

---

### [F-33]

## La línea del tiempo

```
1957 → Chomsky: Sintactic Structures — jerarquía de gramáticas
1960 → Backus-Naur Form — especificación formal del Algol 60
1977 → EBNF — notación extendida
2023 → Constrained decoding en LLMs — Outlines, LMQL
```

> *La formalización de la sintaxis no es historia — es infraestructura activa en los sistemas de IA más modernos.*

---

### [F-34]

## Preguntas para pensar

1. Un programa TypeScript que pasa `tsc` sin errores, ¿puede tener errores semánticos? Dar un ejemplo.

2. ¿Por qué una gramática ambigua es problemática para un compilador?

3. Diferencia entre un token y un lexema — dar un ejemplo concreto.

---

### [F-35]

## Mapa: lo que vimos hoy

```
LENGUAJE DE PROGRAMACIÓN
├── SINTAXIS (forma)
│   ├── Reglas léxicas → lexemas → tokens → [Lexer]
│   ├── Reglas sintácticas → gramática (BNF / EBNF)
│   │   ├── No terminales, terminales, producciones
│   │   ├── Derivaciones → árbol sintáctico
│   │   ├── Ambigüedad → defecto de diseño
│   │   └── Diagramas de sintaxis (railroad)
│   └── [Parser] → árbol de derivación
└── SEMÁNTICA (significado)
    ├── Nombres y objetos denotables
    ├── Entorno = { nombre → objeto }
    ├── Binding estático / dinámico
    ├── Semántica operacional = secuencia de estados
    └── Semántica estática = type checking
```

---

### [F-36]

## Próxima clase — Tema 03: Sistema de Tipos

**Para pensar:**
> *"El type-checker rechazó tu programa.  
> ¿Qué información necesita el compilador para poder hacer eso?"*

**Conexión:** el type-checker es el analizador semántico estático del pipeline que estudiamos hoy.

---

### [F-37]

## Referencias

- **Sebesta, R.** (2019). *Concepts of Programming Languages* (12ª ed.). Cap. 3 y Cap. 4. Addison-Wesley.
- **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms*. Cap. 4, §4.1. Springer.
- **Willard, B. T. & Louf, R.** (2023). *Efficient Guided Generation for Large Language Models*. arXiv:2307.09702.
- **Beurer-Kellner, L. et al.** (2023). *Prompting Is Programming: A Query Language for Large Language Models* (LMQL). VLDB 2023.
- **Geng, S. et al.** (2023). *Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning*. ACL 2023.

---

> **Fin de filminas — Tema 02: Sintaxis y Semántica de Lenguajes**
> 38 slides · 6 bloques · 120 minutos
