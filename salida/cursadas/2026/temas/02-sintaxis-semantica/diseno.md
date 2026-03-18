# Diseño — Tema 02: Sintaxis y Semántica de Lenguajes

> **Estado:** REDISEÑO — pendiente de aprobación
> **Rediseño generado por:** Lic. Marcos (topic-designer)
> **Fecha de rediseño:** 2026-03-18
> **Historial:**
> - Aprobado originalmente: 2026-03-10 (Matías Gel)
> - Rediseñado el 2026-03-18 tomando como baseline las filminas año anterior (`02 sintaxis.pdf`) y las filminas 2026 desarrolladas (F-00 a F-37)
> **Material fuente:**
> - `material/02-sintaxis/txt/02 sintaxis.txt` — filminas cátedra año anterior (baseline año previo)
> - `material/02-sintaxis/txt/185-220.txt` — Sebesta Cap. 3 y Cap. 4 (Lexical and Syntax Analysis)
> - `material/02-sintaxis/txt/083-105.txt` — Gabbrielli & Martini Cap. 4 (Names and the Environment)
> - `material/02-sintaxis/txt/210-330.txt` — material complementario
> **Referencia de implementación:** `filminas.md` actual (F-00 a F-37) — producto del ciclo anterior, usada como evidencia de lo que funciona

---

## Datos del Tema

| Campo | Valor |
|-------|-------|
| Número | 02 |
| Nombre | Sintaxis y Semántica de Lenguajes |
| Módulo del plan mínimo | Módulo V (Sintaxis y Semántica) |
| Contenido mínimo cubierto | #1 — Sintaxis y semántica. Nociones básicas de semántica formal. Semántica operacional. / #6 — Conceptos de intérpretes y compiladores. |
| Semana | 1 |
| Clase | 2 de 2 |
| Duración total | **120 minutos** ← constraint de generación, no sugerencia |
| Lenguaje principal | TypeScript (como caso concreto de lenguaje con gramática formal) |
| Perfil docente | profesor-teorico |

---

## Tópicos del Plan Mínimo cubiertos en este tema

| Tópico | Código plan mínimo | Fuente principal |
|--------|--------------------|-----------------|
| Sintaxis y semántica — definición y relación | Contenido mínimo #1 | slides cátedra; Sebesta Cap. 3 |
| Nociones básicas de semántica formal | Contenido mínimo #1 | Gabbrielli & Martini Cap. 4 (introductorio) |
| Semántica operacional (introducción) | Contenido mínimo #1 | Gabbrielli & Martini Cap. 4 |
| Conceptos de intérpretes y compiladores | Contenido mínimo #6 | Sebesta Cap. 4; conecta con Tema 01 Bloque 3 |

> ⚠️ **OUT OF SCOPE:** Scope rules, binding y entorno (variables/nombres como denotable objects) se abordan en detalle en Tema 09 (Variables, Binding y Ámbito), aunque se hace una mención breve para motivar la semántica.
> ⚠️ **OUT OF SCOPE:** Algoritmos de parsing (recursive-descent, LR) se mencionan a nivel conceptual únicamente. No se enseñan algoritmos de construcción de parsers — eso correspondería a Teoría de Compiladores.

---

## Análisis comparativo — Año anterior vs. Rediseño 2026

### Qué se mantuvo del año anterior (`02 sintaxis.pdf`)

Las filminas del año anterior cubrían el núcleo sintáctico. Los siguientes contenidos se conservaron y mejoraron:

| Contenido (2025) | Estado en 2026 | Filmina(s) |
|-----------------|----------------|-----------|
| Definición de LP: sintaxis + semántica | ✅ mantenido y expandido | F-02, F-03, F-04 |
| Criterios sintácticos (legibilidad, writability, etc.) | ✅ mantenido en F-03 | F-03 |
| Elementos sintácticos de un LP (tokens, identificadores, operadores…) | ✅ integrado en Bloque 2 | F-07 a F-11 |
| Estructura léxica: lexemas y tokens | ✅ mantenido con mejor ejemplo (tabla indice=5*contador+1) | F-09, F-10 |
| BNF: metasímbolos, reglas, LHS/RHS | ✅ mantenido con gramática de trabajo extendida | F-14, F-15 |
| Derivaciones con símbolo `⇒` | ✅ mantenido, derivación completa de A:=B*(A+C) | F-16 |
| Árboles sintácticos | ✅ mantenido con árbol ASCII de la misma derivación | F-17 |
| Ambigüedad y gramáticas ambiguas | ✅ mantenido con ejemplo J:=1+2*3 | F-18 |
| EBNF (extensiones `[]`, `{}`) | ✅ mantenido con ejemplo completo de lenguaje simple | F-19 |
| Diagramas de sintaxis (railroad diagrams) | ✅ mantenido con diagrama ASCII del condicional | F-21, F-22 |

### Qué es nuevo en 2026 (no estaba en 2025)

| Contenido nuevo | Justificación | Filmina(s) |
|----------------|---------------|-----------|
| **TypeScript como lenguaje principal** — todos los ejemplos en TS | Lenguaje de la cursada; conecta con Tema 01 | F-02 a F-07, F-11, F-31 |
| **Actividad participativa** — identificar error sintáctico vs semántico | Pausa activa en Bloque 1; alta retención | F-05, F-06 |
| **Analizador léxico como componente explícito** del pipeline | Sebesta Cap. 4; clarifica el rol del lexer | F-11 |
| **Bloque 5 completo: nombres, entorno, binding, semántica operacional** | Gabbrielli & Martini Cap. 4; cubre contenido mínimo #1 explícitamente | F-25 a F-28 |
| **Pipeline integrado del compilador** (Lexer→Parser→Type-checker→Emitter) | Conecta todos los bloques; cierra con `tsc` como ejemplo real | F-29 |
| **Síntesis: tres tipos de error en TypeScript** con código real | Consolida la distinción sintáctico/semántico estático/semántico dinámico | F-31 |
| **Las gramáticas hoy: constrained decoding en LLMs** | Motivación de relevancia; conecta con Tema 01 (era de la IA) | F-32, F-33 |
| **Línea del tiempo** Chomsky 1957 → BNF 1960 → EBNF → 2023 | Perspectiva histórica + relevancia actual | F-33 |
| **Preguntas para pensar** y **Mapa de la clase** al cierre | Cierre cognitivo y herramienta de repaso | F-34, F-35 |
| **Referencias actualizadas** (Willard & Louf 2023, LMQL, Grammar-Constrained Decoding 2023) | Alineación con literatura 2023 | F-37 |

### Ajuste de énfasis respecto a 2025

- **Criterios sintácticos (legibilidad, writability, etc.):** En 2025 tenían sección propia y se desarrollaban con ejemplos comparativos entre lenguajes. En el rediseño están en F-03 como lista breve. **Recomendación para próximo ciclo:** agregar una filmina dedicada con ejemplos comparativos (Python vs. C vs. APL en legibilidad).
- **Elementos sintácticos de un LP** (caracteres, identificadores, operadores, palabras reservadas, comentarios, espacios en blanco, delimitadores): En 2025 eran un bullet list explícito. En el rediseño están dispersos en Bloque 2. **Recomendación:** unificarlos en una slide tipo checklist en Bloque 2, previo a la slide de tokenización.

---

## Conexión con Tema 01 (Continuidad pedagógica)

El Tema 01 cerró con la pregunta: *"¿Por qué estudiar lenguajes de programación en la era de la IA?"* y la idea de que TypeScript compila a JavaScript, que ejecuta en V8. Este tema responde la pregunta técnica subyacente: **¿cómo sabe el compilador si un programa está bien escrito, y qué significa que esté bien?**

- Tema 01 → máquinas abstractas, intérpretes vs. compiladores (hook para este tema)  
- Tema 02 → sintaxis formal, semántica, papel del analizador léxico y sintáctico  
- Tema 03 → el sistema de tipos, primer mecanismo semántico concreto

---

## Estructura temporal (120 min)

### Bloque 1 — Sintaxis y semántica: conceptos fundamentales (20 min)

**Objetivo:** Distinguir forma de significado. Comprender por qué ambas dimensiones son independientes pero relacionadas.

**Contenidos:**
- Definición de lenguaje de programación como *notación formal para describir algoritmos*
- **Sintaxis** = conjunto de reglas que determinan cuándo un programa está bien formado *(forma; representación)*
  - Ejemplo canónico: `if (<expresión>) <sentencia>` — C, slides cátedra
  - La sintaxis responde: ¿es este texto un programa válido?
- **Semántica** = le asigna significado a los programas sintácticamente correctos
  - La semántica responde: ¿qué hace este programa?
  - Ejemplo contrastivo: `int x = "hola";` — sintácticamente inválido en TypeScript; `x = null` — sintácticamente válido pero semánticamente puede ser un error
- La definición formal de un lenguaje = gramática (sintaxis) + semántica
- **Punto de tensión:** Un programa puede ser sintácticamente correcto y semánticamente incorrecto — el compilador detecta errores sintácticos pero no todos los semánticos
- **Criterios sintácticos de un buen lenguaje** *(slides cátedra — sección explícita del material 2025)*:
  - **Legibilidad**: lo que se escribe puede leerse y entenderse fácilmente
  - **Facilidad de escritura** (writability): es natural expresar algoritmos en el lenguaje
  - **Facilidad de verificación**: es posible demostrar propiedades del programa
  - **Facilidad de traducción**: el compilador puede procesarlo eficientemente
  - **Carencia de ambigüedad**: cada construcción tiene exactamente un significado
  - *Estrategia: mostrar un ejemplo de lenguaje con mala legibilidad (APL o Perl) y uno con buena (Python) — sin profundizar, solo para anclar el concepto*

**Estrategia pedagógica:** Abrir con 3 ejemplos rápidos en TypeScript. Para cada uno, preguntar: ¿error de sintaxis o de semántica?
```typescript
// ¿Sintaxis o semántica?
const x: number = "hola"       // Error de tipo (semántica estática)
if true { console.log("ok") }  // Error de sintaxis (falta paréntesis)
const y = undefined; y.length  // Error semántico en runtime
```

---

### Bloque 2 — Estructura léxica: del texto al token (20 min)

**Objetivo:** Entender cómo se transforma un programa fuente en unidades mínimas para el análisis.

**Contenidos:**

- **Cadena de caracteres → programa**: el programa llega al compilador como texto plano
- **Reglas léxicas** vs. **reglas sintácticas** — slides cátedra; Sebesta Cap. 4:
  - Léxicas: definen el alfabeto y cómo combinar caracteres en palabras válidas (ej: case-sensitivity en Java vs. Python)
  - Sintácticas: definen cómo combinar palabras en sentencias
- **Elementos sintácticos de un LP** *(sección propia en slides cátedra 2025 — restituida en rediseño)*:
  - **Caracteres**: conjunto de símbolos permitidos (ASCII, Unicode)
  - **Identificadores**: nombres para variables, funciones, tipos — reglas: longitud, case-sensitivity, caracteres permitidos
  - **Operadores**: símbolos para operaciones (aritméticos, lógicos, relacionales, de asignación)
  - **Palabras clave y reservadas**: `if`, `while`, `const` — no pueden usarse como identificadores
  - **Comentarios**: texto ignorado por el compilador (`//`, `/* */`)
  - **Espacios en blanco**: generalmente ignorados salvo en lenguajes como Python (indentación significativa)
  - **Delimitadores y corchetes**: `{}`, `()`, `[]`, `;` — estructuran el programa
  - **Expresiones**: combinaciones de operandos y operadores que producen un valor
  - **Sentencias**: unidades de ejecución del programa
  - *Esta lista es el "vocabulario" que el lexer categoriza en tokens*
- **Lexemas y Tokens** — slides cátedra; Sebesta Cap. 4:
  - Lexema: unidad sintáctica de más bajo nivel (identificadores, operadores, palabras especiales)
  - Token: categoría del lexema (clase abstracta)
  - Ejemplo: `indice = 5 * contador + 1;`
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
  - *Nota: los Elementos sintácticos completos se desarrollaron en la sub-sección anterior*
- **Analizador léxico (lexer/scanner)**: transforma la cadena de caracteres en secuencia de tokens — Sebesta Cap. 4
  - Es el "front-end" del analizador sintáctico
  - Motivo de separación: simplicidad, eficiencia, portabilidad — Sebesta Cap. 4
  - Ejemplo concreto: `result = oldsum - value / 100;` → tabla de tokens (Sebesta Cap. 4)

**Ejemplo TypeScript en vivo:** mostrar que el compilador de TypeScript (`tsc --listEmittedFiles`) hace exactamente esto en el primer paso

---

### Bloque 3 — Gramáticas formales: BNF y EBNF (30 min)

**Objetivo:** Leer e interpretar una especificación formal de sintaxis. Usar BNF para describir construcciones de lenguaje.

**Contenidos:**

- **Definición formal de sintaxis = gramática** — slides cátedra; Sebesta Cap. 3:
  - Ejemplo histórico: FORTRAN con reglas en inglés vs. Python con BNF oficial
  - Una gramática formalmente especificada permite verificar automáticamente si un programa es válido
- **Gramáticas libres de contexto — Clasificación de Chomsky (1959)** — slides cátedra; Sebesta Cap. 3:
  - La tupla `(N, T, S, P)`:
    - N: símbolos no terminales (abstracciones)
    - T: símbolos terminales (lexemas/tokens reales)
    - S: símbolo inicial
    - P: producciones / reglas
  - *No es necesario formalismo matemático pesado — se enseña con ejemplos*

- **BNF (Backus-Naur Form)** — slides cátedra; Sebesta Cap. 3:
  - Metasímbolos: `::=` (se define como), `|` (alternativa), `<>` (no terminal)
  - Ejemplo: sentencia de asignación en C/Pascal:
    ```
    <assign> ::= <var> = <expression>
    <enunc_if> ::= if <expr_log> then <enunc>
                 | if <expr_log> then <enunc> else <enunc>
    ```
  - Regla: LHS (no terminal a definir) → RHS (definición)
  - *Identificar en cada regla: qué es terminal y qué es no terminal*

- **Gramática de un lenguaje simple** — slides cátedra:
  ```
  <assign> ::= <id> := <expr>
  <id>     ::= A | B | C
  <expr>   ::= <id> + <expr> | <id> * <expr> | (<expr>) | <id>
  ```
  - Derivación de `A := B * (A + C)` paso a paso (con flechas `⇒`)
  - Forma de sentencia = string en un paso intermedio de la derivación

- **Árboles sintácticos (parse trees)** — slides cátedra; Sebesta Cap. 3:
  - Representan la estructura jerárquica de la derivación
  - Nodos internos = no terminales; nodos hoja = terminales
  - Construir el árbol para `A := B * (A + C)`

- **Ambigüedad** — Sebesta Cap. 3; slides cátedra:
  - Definición: una gramática es ambigua si permite dos árboles de derivación distintos para la misma cadena
  - Ejemplo: `J := 1 + 2 * 3` con gramática ambigua → dos árboles → dos significados distintos
  - **Implicación práctica:** La ambigüedad es un defecto de diseño del lenguaje — el compilador no sabe qué árbol elegir
  - Cómo se resuelve: precedencia y asociatividad de operadores en la gramática

- **EBNF (Extended BNF)** — slides cátedra; Sebesta Cap. 3:
  - Notación extendida con `[ ]` (opcional), `{ }` (repetición), `|` dentro de corchetes
  - Ejemplo EBNF de un lenguaje simple completo:
    ```
    <programa>  ::= { <sentencia> * }
    <sentencia> ::= <asignación> | <condicional> | <loop>
    <asignación>::= <identificador> = <expr>
    <condicional>::= if <expr> { <sentencia>* }
                   | if <expr> { <sentencia>* } else { <sentencia>* }
    <loop>      ::= while <expr> { <sentencia>* }
    ```

**Actividad de 5 min:** Dado `C := D – E * F`, derivar y dibujar el árbol de derivación (ejercicio del material de cátedra).

---

### Bloque 4 — Diagramas de sintaxis y notación gráfica (10 min)

**Objetivo:** Leer especificaciones gráficas de sintaxis — usadas en documentación oficial de lenguajes.

**Contenidos:**
- **Diagramas de sintaxis (railroad diagrams)** — slides cátedra:
  - Representación gráfica equivalente a EBNF
  - Símbolo no terminal: recuadro / Símbolo terminal: óvalo o círculo
  - Una cadena es válida si puede *"viajar"* de izquierda a derecha atravesando el diagrama
  - Mostrar diagrama para `asignación`, `condicional`, `loop` del ejemplo
- **Dos usos de la descripción sintáctica** — slides cátedra:
  1. Ayuda al programador a escribir programas sintácticamente correctos
  2. Base para el compilador / analizador sintáctico
- **Conexión con TypeScript:** el sitio oficial de TypeScript usa diagramas de sintaxis para documentar construcciones del lenguaje (observación breve, sin profundizar)

---

### Bloque 5 — Semántica: de la forma al significado (20 min)

**Objetivo:** Comprender qué es la semántica formal e introducir la semántica operacional como el enfoque más intuitivo.

**Contenidos:**

- **¿Por qué necesitamos semántica formal?** — Gabbrielli & Martini Cap. 4 (introductorio):
  - Sintaxis correcta ≠ programa correcto
  - La semántica define *cómo se ejecuta* un programa (qué estados produce)
  - Sin semántica formal, el comportamiento del lenguaje depende de la implementación → se vuelve no portable

- **Nombres y objetos denotables** — Gabbrielli & Martini Cap. 4, §4.1:
  - Un nombre es una secuencia de caracteres que *denota* otro objeto
  - Nombre ≠ objeto que denota (un mismo objeto puede tener varios nombres → aliasing)
  - **Objetos denotables**: variables, parámetros formales, procedimientos, tipos, etiquetas, módulos, constantes, excepciones; también tipos primitivos y operaciones predefinidas del lenguaje
  - **Concepto de entorno (environment)**: componente de la máquina abstracta que mantiene las asociaciones nombre → objeto en cada punto de ejecución
  - Nota: esto se profundizará en Tema 09 — hoy se introduce como noción semántica base

- **Binding (ligadura)** — Gabbrielli & Martini Cap. 4, §4.1 (introducción):
  - Una ligadura es la asociación entre un nombre y un objeto denotable
  - Las ligaduras se crean en distintas fases: diseño del lenguaje, escritura del programa, tiempo de compilación, tiempo de ejecución
  - Estático vs. dinámico: lo que ocurre antes de la ejecución (compilación) vs. durante (runtime)
  - *En Tema 09 se estudian los mecanismos de scope y las reglas de visibilidad*

- **Semántica operacional** (introducción conceptual) — Gabbrielli & Martini (referencia teórica):
  - Define el significado de un programa como la **secuencia de estados** que produce al ejecutarse
  - Estado = conjunto de pares (nombre, valor) en un instante
  - Un programa = transformación de estado inicial → estado final
  - Esto conecta con la máquina abstracta del Tema 01: la semántica en una máquina abstracta *es* su modelo de ejecución
  - Ejemplo: `x := 5; y := x + 1` → estado inicial `{}` → `{x=5}` → `{x=5, y=6}`

- **Semántica estática (type checking)** — Sebesta Cap. 3 (mención breve):
  - Reglas semánticas que se verifican en tiempo de compilación
  - Ejemplo: TypeScript verifica que se asigne un `string` a una variable de tipo `number` antes de ejecutar
  - El type-checker es el primer "intérprete semántico" que ve el código

---

### Bloque 6 — Analizador sintáctico: concepto y rol en el compilador (15 min)

**Objetivo:** Entender el rol del parser en el pipeline de compilación — sin enseñar algoritmos.

**Contenidos:**
- **El parser como corazón del compilador** — Sebesta Cap. 4, §4.1:
  - El analizador sintáctico determina si la secuencia de tokens forma un programa válido según la gramática
  - Construye el árbol de derivación (parse tree) como representación interna
  - Alimenta al analizador semántico y al generador de código intermedio
- **Dos aproximaciones conceptuales al parsing** — Sebesta Cap. 4 (nivel conceptual):
  - **Top-down (descendente):** comienza en el símbolo inicial y trata de derivar la cadena de entrada — intuitivo, legible
  - **Bottom-up (ascendente):** parte de los tokens y construye el árbol hacia arriba — más poderoso, pero más complejo
  - *No se estudian los algoritmos específicos (recursive-descent, LR) — solo el contraste conceptual*
- **Relación compilador/intérprete revisitada** (continuidad con Tema 01):
  - Compilador: análisis léxico → análisis sintáctico → análisis semántico → generación de código
  - Intérprete: el mismo pipeline, pero en lugar de generar código, *ejecuta* el árbol directamente
  - `tsc` (TypeScript compiler) hace exactamente el pipeline de compilación: lexer → parser → type-checker → emite JavaScript
  - El error message de `tsc` incluye la posición en el texto fuente — evidencia de que el lexer registró dónde estaba cada token
- **Errores sintácticos vs. semánticos en TypeScript** — síntesis con ejemplos concretos:
  ```typescript
  // Error sintáctico (tsc falla en análisis sintáctico):
  function foo( { return 42 }   // falta ')'

  // Error semántico estático (tsc falla en type-checking):
  const x: number = "texto"     // violación de tipo

  // Error semántico dinámico (falla en runtime, tsc no lo detecta):
  const arr: number[] = []
  console.log(arr[100].toString())  // undefined.toString()
  ```

- **Cierre — Las gramáticas en la IA generativa** (5 min — gancho de relevancia):
  - Las gramáticas EBNF que se estudian hoy **son exactamente las mismas herramientas** que usan los LLMs modernos para generar outputs estructurados
  - **Constrained decoding**: técnica que compila una gramática EBNF a un autómata de estados finitos y lo usa para filtrar, token a token, qué puede generar el modelo — solo tokens que sean parte de una derivación válida — Willard & Louf (2023)
  - Ejemplo: cuando se le pide a un LLM que genere JSON válido, el sistema de constrained decoding verifica en tiempo real que cada token producido respeta la gramática del JSON
  - Herramientas actuales: **Outlines** (Python), **LMQL** — ambas usan gramáticas BNF/EBNF como input del programador — Beurer-Kellner et al. (2023)
  - **Punto de inflexión pedagógico:** la gramática de Chomsky (1959) → BNF de Backus-Naur (1960) → EBNF → hoy: constraint de generación de LLMs. La formalización de la sintaxis no es historia — es infraestructura activa

---

## Mapa de contenidos y fuentes

| Bloque | Minutos | Tópico | Fuente principal |
|--------|---------|--------|----------------|
| 1 | 20 | Sintaxis y semántica: definición y relación | slides cátedra |
| 2 | 20 | Estructura léxica: lexemas y tokens | slides cátedra; Sebesta Cap. 4 |
| 3 | 30 | Gramáticas formales: BNF, EBNF, árboles sintácticos, ambigüedad | slides cátedra; Sebesta Cap. 3 |
| 4 | 10 | Diagramas de sintaxis | slides cátedra |
| 5 | 20 | Semántica: nombres, entorno, ligaduras, semántica operacional | Gabbrielli & Martini Cap. 4 |
| 6 | 15 | Parser: rol en el compilador, top-down vs. bottom-up; gramáticas en IA (cierre) | Sebesta Cap. 4; Willard & Louf (2023); Beurer-Kellner et al. (2023) |
| — | 5 | Buffer / preguntas | — |

**Total: 120 minutos** ✓

---

## Tópicos OUT OF SCOPE (freno explícito a scope creep)

Los siguientes contenidos están fuera de scope para esta clase y **no deben incluirse** en minuta ni filminas:

| Tópico excluido | Razón | Cubierto en |
|-----------------|-------|-------------|
| Algoritmos de parsing (recursive-descent, LR) | Nivel de compiladores, no de LP | Fuera del plan |
| Reglas de visibilidad (scope) y bloqueo de nombres | Tema 09 | Tema 09 |
| Gestión de memoria y stack frames | Tema 09 | Tema 09 |
| Implementación del analizador léxico | Compiladores | Fuera del plan |
| Semántica denotacional y axiomática completas | Demasiado formal para este nivel | Fuera del plan |
| Construcciones semánticas avanzadas de TypeScript (generics, decorators) | Temas 10 y 14 | Temas 10 y 14 |

---

## Criterio de densidad cognitiva

- Perfil: `profesor-teorico` — exposición conceptual con ejemplos elaborados
- Complejidad máxima por bloque: 1 concepto nuevo dominante + ejemplos de anclaje
- Los Bloques 3 y 5 son los de mayor carga cognitiva — el Bloque 4 actúa como alivio visual intencional
- La actividad del Bloque 3 (derivar árbol de `C := D – E * F`) es la única actividad participativa — mantiene atención en la zona más densa

---

## Referencias académicas del diseño

- **Sebesta, R.** (2019). *Concepts of Programming Languages* (12ª ed.), Addison-Wesley. Cap. 3 (Syntax) y Cap. 4 (Lexical and Syntax Analysis). Archivo: `material/02-sintaxis/txt/185-220.txt`
- **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms*. Springer. Cap. 4 (Names and the Environment). Archivo: `material/02-sintaxis/txt/083-105.txt`
- **Schmidt, D. & Runfola, D.** (2025). *Liberating Logic in the Age of AI*. — Referenciado indirectamente desde Tema 01 para motivar el estudio de LP. Archivo: `material/txt/2511.17696v1.txt`
- **Willard, B. T. & Louf, R.** (2023). *Efficient Guided Generation for Large Language Models*. arXiv:2307.09702. https://arxiv.org/abs/2307.09702 — Framework Outlines: compilación de gramáticas EBNF a autómatas para constrained decoding en LLMs. Acceso abierto.
- **Beurer-Kellner, L. et al.** (2023). *Prompting Is Programming: A Query Language for Large Language Models* (LMQL). VLDB 2023. DOI: 10.14778/3611479.3611484. arXiv:2212.06094. — Lenguaje de consulta con restricciones sintácticas declarativas sobre LLMs. Acceso abierto en arXiv.
- **Geng, S. et al.** (2023). *Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning*. ACL 2023. https://aclanthology.org/2023.acl-long.244 — Constrained decoding usando gramáticas libres de contexto (JSON, SQL, código). Acceso abierto.

---

## Preguntas de cierre (para los últimos minutos)

1. *Un programa TypeScript que pasa el chequeo de `tsc` sin errores, ¿puede tener errores semánticos? Dar un ejemplo.*
2. *¿Por qué una gramática ambigua es problemática para un compilador?*
3. *Diferencia entre un token y un lexema — dar un ejemplo concreto.*

---

> **⚙️ REDISEÑO — pendiente de aprobación:** Rediseñado el 2026-03-18 incorporando el material de filminas año anterior (`02 sintaxis.pdf`). Cubre contenidos mínimos #1 y #6 en 120 minutos exactos. Para aprobar: ejecutar `/edu-approve-design`.
