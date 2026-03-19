<!-- markdownlint-disable MD024 MD060 -->

# Minuta de Clase — Tema 02: Sintaxis y Semántica de Lenguajes

> **Estado:** REGENERADA desde `diseno.md` rediseñado
> **Agente:** Dr. Roberto ✍️ (class-writer)
> **Fecha de generación:** 2026-03-18
> **Duración total:** 120 minutos (constraint absoluto)
> **Clase:** 2 de 2 — Semana 1
> **Perfil docente:** profesor-teorico
> **Lenguaje principal:** TypeScript
> **Workflow:** topic-cycle / Step 4
> **Input principal:** `salida/cursadas/2026/temas/02-sintaxis-semantica/diseno.md`

---

## Datos de la clase

| Campo | Valor |
|-------|-------|
| Materia | Paradigmas y Lenguajes de Programación 2026 |
| Institución | Universidad Nacional de Tierra del Fuego — Instituto IDEI |
| Tema Nº | 02 |
| Nombre del tema | Sintaxis y Semántica de Lenguajes |
| Duración | 120 minutos |
| Plan mínimo | Contenidos #1 y #6 |
| Foco disciplinar | Forma, significado y pipeline del compilador |

---

## Hipótesis de trabajo de la clase

La clase responde la pregunta técnica que quedó abierta en el Tema 01: si TypeScript compila a JavaScript y luego corre sobre V8, ¿cómo decide el compilador si un programa está bien escrito y qué significa que esté bien? La respuesta se construye en seis bloques encadenados:

1. Diferencia entre sintaxis y semántica.
2. Paso de texto plano a tokens.
3. Gramáticas formales para describir programas válidos.
4. Notación gráfica de esa misma sintaxis.
5. Introducción pragmática a la semántica mediante tipos, nombres y entorno.
6. Integración de todo eso en el pipeline de compilación y su vigencia actual en IA.

La secuencia conceptual, los ejemplos y la terminología deben coincidir con `filminas.md`.

---

## Apertura de clase

### Pregunta disparadora

> *"El compilador de TypeScript rechazó tu programa. ¿Cómo sabe que está mal? ¿Y sabe siempre cuándo está mal?"*

### Reenganche con Tema 01

Recordar brevemente la clase anterior:

- TypeScript compila a JavaScript.
- JavaScript corre sobre una máquina de ejecución concreta.
- Estudiar lenguajes no es solo estudiar sintaxis superficial, sino entender cómo un sistema decide qué programas acepta y qué significado les asigna.

Frase de transición sugerida:

> "En la clase pasada miramos el mapa general. Hoy nos metemos dentro del frente del compilador: texto, tokens, gramática, significado y chequeos."

---

## Estructura temporal

| Bloque | Minutos | Eje |
|--------|---------|-----|
| 1 | 20 | Sintaxis y semántica: conceptos fundamentales |
| 2 | 20 | Estructura léxica: del texto al token |
| 3 | 30 | Gramáticas formales: BNF, EBNF, derivación y ambigüedad |
| 4 | 10 | Diagramas de sintaxis |
| 5 | 20 | Semántica: type checking, nombres, entorno y binding |
| 6 | 15 | Pipeline del compilador y gramáticas en IA |
| Buffer | 5 | Preguntas y cierre |

**Total:** 120 minutos

---

## Bloque 1 — Sintaxis y semántica: conceptos fundamentales (20 min)

### Objetivo

Distinguir con claridad la forma de un programa de su significado, y fijar la idea de que ambas dimensiones son necesarias para definir un lenguaje.

### Desarrollo sugerido

1. Definir lenguaje de programación como notación formal para describir algoritmos.
2. Presentar **sintaxis** como reglas de buena formación.
3. Presentar **semántica** como reglas que asignan significado.
4. Hacer explícito el punto central del bloque:

> Un programa puede ser sintácticamente correcto y semánticamente incorrecto.

### Ideas a verbalizar

- La sintaxis responde: *"¿esto tiene la forma correcta?"*
- La semántica responde: *"¿qué efecto tiene esto?"*
- La definición completa de un lenguaje necesita ambas capas.

### Criterios sintácticos a recuperar del material de cátedra

- Legibilidad.
- Facilidad de escritura.
- Facilidad de verificación.
- Facilidad de traducción.
- Carencia de ambigüedad.

### Actividad de apertura

Proyectar o escribir en pizarra:

```typescript
const x: number = "hola"
if true { console.log("ok") }
const y = undefined; y.length
```

Pedir clasificación rápida:

- Caso 1: error semántico estático.
- Caso 2: error sintáctico.
- Caso 3: error semántico dinámico.

### Cómo desarrollar la actividad

1. Dar 20 a 30 segundos de lectura silenciosa y pedir que no respondan todavía.
2. Leer cada línea por separado y preguntar primero: "¿qué tipo de problema ven acá?", antes de aceptar etiquetas técnicas.
3. Si responden solo "está mal", repreguntar: "¿está mal por la forma, por los tipos o porque al ejecutar pasa algo?".
4. Cerrar nombrando explícitamente el criterio correcto en cada caso.

Resolución esperada para el docente:

- `const x: number = "hola"`: la sintaxis está bien, pero el chequeo de tipos falla; es error semántico estático.
- `if true { console.log("ok") }`: falta la sintaxis válida del `if`; el parser no puede reconocer la estructura; es error sintáctico.
- `const y = undefined; y.length`: puede pasar parsing y type checking laxo, pero falla al ejecutar cuando se intenta acceder a una propiedad de `undefined`; es error semántico dinámico.

Idea de cierre para verbalizar:

> "No todo error aparece en la misma etapa. Unos se detectan por forma, otros por significado estático y otros recién cuando el programa corre."

### Cierre del bloque

Transición sugerida:

> "Si el compilador primero decide si la forma es válida, antes de hablar de significado tiene que cortar el texto en piezas reconocibles. Eso hace el análisis léxico."

---

## Bloque 2 — Estructura léxica: del texto al token (20 min)

### Objetivo

Entender cómo un programa fuente, que llega como texto plano, se convierte en una secuencia de unidades mínimas útiles para el parser.

### Nota de navegación didáctica

En este bloque se anticipa el análisis léxico del capítulo 4 antes de entrar de lleno en las gramáticas del capítulo 3. El orden es deliberado: primero lo concreto, después la formalización.

### Desarrollo sugerido

1. Mostrar que el compilador recibe caracteres, no estructuras listas para usar.
2. Diferenciar reglas léxicas y reglas sintácticas.
3. Restituir la lista de elementos sintácticos del material 2025.
4. Introducir lexema y token.
5. Ubicar al lexer dentro del pipeline.

### Elementos sintácticos del lenguaje

- Caracteres.
- Identificadores.
- Operadores.
- Palabras clave y reservadas.
- Comentarios.
- Espacios en blanco.
- Delimitadores y corchetes.
- Expresiones.
- Sentencias.

### Ejemplo central del bloque

Trabajar con:

```text
indice = 5 * contador + 1;
```

Descomposición:

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

### Cómo desarrollar el ejemplo

1. Escribir la línea completa y preguntar qué ve el compilador primero: "¿ideas" o "caracteres".
2. Marcar barras verticales o espacios entre lexemas para separar visualmente cada pieza.
3. Pedir a estudiantes que nombren la categoría de cada fragmento sin discutir todavía su significado en el programa.
4. Cerrar con la distinción entre reconocer un token y entender su rol semántico.

Punto a enfatizar al conducir:

- `indice` y `contador` ya pueden reconocerse como identificadores.
- Todavía no corresponde discutir si `contador` fue declarado o qué valor tiene.
- El objetivo del ejemplo es mostrar segmentación y clasificación léxica, no análisis semántico.

### Punto fino a remarcar

El lexer sabe que `indice` es un identificador, pero todavía no sabe si es variable, parámetro o constante. Ese significado aparece más tarde.

### Conexión con TypeScript

Explicar que el compilador de TypeScript también comienza así: texto fuente, tokenización y luego análisis sintáctico.

### Cierre del bloque

Transición sugerida:

> "Ahora que ya tenemos palabras, falta la regla que diga qué combinaciones de palabras forman programas válidos. Eso es una gramática."

---

## Bloque 3 — Gramáticas formales: BNF, EBNF, derivación y ambigüedad (30 min)

### Objetivo

Leer una gramática formal, seguir una derivación y comprender por qué la ambigüedad es un problema de diseño de lenguajes.

### Desarrollo sugerido

1. Motivar el pasaje de descripciones en lenguaje natural a gramáticas formales.
2. Introducir gramáticas libres de contexto con la tupla `(N, T, S, P)` a nivel conceptual.
3. Explicar BNF.
4. Usar una gramática de trabajo simple para derivación y árbol.
5. Mostrar un caso de ambigüedad.
6. Cerrar con EBNF como notación compacta.

### Gramática de trabajo

```text
<assign> ::= <id> := <expr>
<id>     ::= A | B | C
<expr>   ::= <id> + <expr> | <id> * <expr> | (<expr>) | <id>
```

### Derivación a desarrollar en clase

Cadena objetivo:

```text
A := B * (A + C)
```

Secuencia sugerida:

1. `<assign>`
2. `<id> := <expr>`
3. `A := <expr>`
4. `A := <id> * <expr>`
5. `A := B * <expr>`
6. `A := B * (<expr>)`
7. `A := B * (<id> + <expr>)`
8. `A := B * (A + <expr>)`
9. `A := B * (A + <id>)`
10. `A := B * (A + C)`

### Árbol sintáctico

Construir el árbol de la misma derivación y remarcar:

- Nodos internos: no terminales.
- Hojas: terminales.
- La estructura del árbol representa agrupamiento y precedencia implícita.

### Ambigüedad

Usar:

```text
J := 1 + 2 * 3
```

Preguntar qué pasa si la gramática no codifica precedencia. Concluir:

- Dos árboles posibles.
- Dos significados posibles.
- Eso es una mala especificación del lenguaje.

### Cómo conducir la discusión

1. Pedir primero una lectura matemática intuitiva de `1 + 2 * 3` y anotar la respuesta más común.
2. Preguntar luego si esa precedencia está escrita en la gramática o si la estamos aportando nosotros desde afuera.
3. Mostrar que, sin una regla adicional, la expresión puede agruparse de más de una manera.
4. Cerrar con la idea de que una gramática debe eliminar ambigüedades relevantes, no confiar en la intuición del lector.

### EBNF

Presentar la notación extendida para reducir ruido sintáctico:

- `[ ]` opcional.
- `{ }` repetición.

### Actividad breve

Dar `C := D - E * F` y pedir que indiquen si la gramática usada deja dudas de asociación o no. No se busca resolver algoritmos de parsing, solo interpretar la especificación.

### Cómo desarrollar la actividad

1. Dar un minuto para que miren la gramática y la cadena objetivo.
2. Pedir una respuesta binaria primero: "¿hay duda o no hay duda?".
3. Solicitar justificación breve apoyada en la forma de las producciones, no en reglas aritméticas aprendidas antes.
4. Si aparece confusión, volver a la pregunta base: "¿la gramática obliga un único árbol o permite varios?".

### Cierre del bloque

Transición sugerida:

> "La misma sintaxis formal puede mostrarse también de forma gráfica. Eso es útil para documentación y para leer estructuras complejas sin tantas reglas escritas."

---

## Bloque 4 — Diagramas de sintaxis y notación gráfica (10 min)

### Objetivo

Reconocer que los diagramas de sintaxis son otra representación de la misma información gramatical y que no son un adorno, sino una herramienta de lectura técnica.

### Desarrollo sugerido

1. Definir railroad diagrams como representación gráfica equivalente a EBNF.
2. Explicar convención mínima:
   - Recuadro: no terminal.
   - Óvalo o terminal destacado: token.
3. Leer un ejemplo simple, preferentemente un condicional.

### Ejemplo recomendado

Usar el esquema del condicional:

- camino principal para `if ... then ...`
- desvío opcional para `else`

### Cómo desarrollar el ejemplo

1. Recorrer el diagrama con el dedo o puntero de izquierda a derecha como si fuera un camino.
2. Mostrar primero el recorrido mínimo, sin `else`, para fijar la estructura base.
3. Repetir el recorrido tomando el desvío opcional y remarcar que el diagrama expresa elección controlada.
4. Cerrar vinculando cada tramo del diagrama con los elementos que en EBNF aparecerían como secuencia y opción.

### Idea de cierre

Los diagramas sirven para dos públicos a la vez:

- el programador que necesita leer la especificación,
- el implementador que necesita saber qué construcciones soportar.

### Transición sugerida

> "Hasta acá vimos cómo decidir si un programa tiene forma válida. Ahora falta la otra mitad: cómo razonar sobre lo que significa."

---

## Bloque 5 — Semántica: type checking, nombres, entorno y binding (20 min)

### Objetivo

Introducir una semántica pragmática y útil para esta materia: tipos, nombres, entorno y ligaduras como forma concreta de pensar el significado del programa, sin entrar en formalismos fuera de alcance.

### Advertencia de alcance

Este bloque **no** desarrolla semántica operacional formal con reglas SOS, ni semántica denotacional, ni axiomática. El foco está en herramientas conceptuales básicas sostenidas por las fuentes disponibles.

### Desarrollo sugerido

#### 1. Semántica estática: el type checker

Usar TypeScript como caso concreto.

```typescript
const x: number = "texto"
```

Mensaje a enfatizar:

- El árbol sintáctico puede estar bien formado.
- Aun así, el type checker lo rechaza por incompatibilidad de tipos.
- Eso ya es semántica: no de ejecución, pero sí de significado estático.

Cómo desarrollarlo en clase:

1. Preguntar primero si la línea "parece código válido" en términos de forma.
2. Confirmar que la estructura es correcta y que el problema no está en el parser.
3. Llevar la atención a la anotación `number` y al literal `"texto"`.
4. Cerrar con la formulación: "la forma está bien, pero el significado estático no cierra".

#### 2. Nombres y objetos denotables

Definir nombre como secuencia de caracteres que denota otro objeto.

Ejemplos de objetos denotables:

- variables,
- parámetros,
- procedimientos o funciones,
- tipos,
- constantes,
- operaciones predefinidas.

#### 3. Entorno

Definir entorno como el conjunto de asociaciones nombre → objeto disponible en un punto de ejecución.

Ejemplo mínimo:

```text
{
  x        → 5
  contador → 12
  suma     → 17
}
```

Cómo desarrollarlo en clase:

1. Presentarlo como una foto del programa en un instante, no como memoria física detallada.
2. Preguntar qué información aporta cada asociación y qué pasaría si un nombre no estuviera en ese entorno.
3. Relacionar el ejemplo con la idea de que entender un nombre exige saber a qué objeto está ligado en ese punto.

#### 4. Binding

Explicar la ligadura nombre-objeto y las fases donde puede aparecer:

- diseño del lenguaje,
- escritura del programa,
- compilación,
- ejecución.

#### 5. Intuición mínima de estado

Usar una transición breve y concreta:

```text
x = 5; y = x + 1
```

como:

```text
{} → {x = 5} → {x = 5, y = 6}
```

No formalizar más allá de esto.

### Síntesis del bloque

Recuperar los tres errores trabajados en toda la clase:

```typescript
function foo( { return 42 }
const x: number = "texto"
const arr: number[] = []
console.log(arr[100].toString())
```

- El primero falla en parsing.
- El segundo falla en type checking.
- El tercero falla en ejecución.

Cómo desarrollar la síntesis:

1. Proyectar las tres líneas juntas y pedir que identifiquen en qué etapa cae cada una.
2. Recuperar verbalmente el pipeline completo: parser, type checker, ejecución.
3. Usar esta secuencia para consolidar la idea de que sintaxis y semántica no compiten, sino que operan en capas distintas.

### Cierre del bloque

Transición sugerida:

> "Ya tenemos todas las piezas separadas. Falta ver el sistema completo: cómo se encadenan en un compilador real y por qué esto sigue importando hoy incluso fuera de los compiladores clásicos."

---

## Bloque 6 — Síntesis: pipeline del compilador y gramáticas en IA (15 min)

### Objetivo

Integrar lo visto en un modelo único del frente del compilador y cerrar mostrando la vigencia contemporánea de las gramáticas formales.

### Desarrollo sugerido

#### 1. Pipeline del compilador

Mostrar la secuencia:

```text
Código fuente → Lexer → Tokens → Parser → Árbol → Type-checker / análisis semántico → Emisión o ejecución
```

Explicar:

- el lexer corta,
- el parser reconoce estructura,
- el análisis semántico chequea coherencia,
- el compilador o intérprete produce un resultado posterior.

#### 2. Parsing top-down vs bottom-up

Solo a nivel conceptual:

- top-down: desde el símbolo inicial hacia la cadena,
- bottom-up: desde tokens hacia el árbol.

Dejar explícito que los algoritmos concretos quedan fuera de alcance.

#### 3. Compilador e intérprete

Vincular con Tema 01:

- ambos necesitan análisis léxico y sintáctico,
- la diferencia aparece después, en qué hacen con la representación obtenida.

#### 4. Gramáticas en IA

Cerrar con relevancia actual:

- constrained decoding,
- generación de JSON válido,
- herramientas que imponen una gramática al output del modelo.

Anclaje bibliográfico actual sugerido para el docente:

- **Reddy et al. (2026), *Draft-Conditioned Constrained Decoding for Structured Generation in LLMs***: muestra que un borrador libre seguido por constrained decoding mejora la exactitud estructurada respecto del constrained decoding estándar, lo que refuerza la idea didáctica de que restringir estructura no es solo "forzar JSON", sino controlar validez sin perder demasiada calidad semántica.

Mensaje de cierre:

> "La gramática no es una reliquia del siglo XX. Es infraestructura actual para compiladores, analizadores y también para sistemas de IA que deben producir salida estructurada."

---

## Cierre general

### Recapitulación en una frase por bloque

1. Sintaxis: qué forma es válida.
2. Léxico: cómo el texto se vuelve tokens.
3. Gramática: cómo los tokens se combinan con reglas formales.
4. Diagramas: otra forma de leer la misma sintaxis.
5. Semántica: cómo hablar del significado usando tipos, nombres y entorno.
6. Pipeline: cómo todo eso trabaja junto en compiladores e IA.

### Preguntas de salida sugeridas

- ¿Puede un programa ser semánticamente erróneo y aun así pasar el parser?
- ¿Qué diferencia hay entre lexema y token?
- ¿Por qué una gramática ambigua es un problema real y no solo notacional?
- ¿Qué chequea el type checker que el parser no chequea?
- ¿Qué relación hay entre EBNF y constrained decoding?

---

## Fuera de alcance explícito

No desarrollar en esta clase:

- algoritmos de parsing concretos como recursive descent o LR,
- semántica operacional estructural formal,
- semántica denotacional,
- semántica axiomática,
- scope y binding en profundidad más allá de la intuición base,
- detalles avanzados de TypeScript como generics o decorators.

---

## Referencias utilizadas para la reconstrucción

- Slides de cátedra 2025 sobre sintaxis de lenguajes.
- Sebesta, capítulos sobre análisis léxico y sintáctico.
- Gabbrielli y Martini, capítulo sobre nombres y entorno.
- Literatura reciente sobre constrained decoding y gramáticas en LLMs, tal como figura en `diseno.md`.
- Reddy, A., Walker, T. T., Ide, J. S., Bedi, A. S. (2026). *Draft-Conditioned Constrained Decoding for Structured Generation in LLMs*. arXiv:2603.03305.
