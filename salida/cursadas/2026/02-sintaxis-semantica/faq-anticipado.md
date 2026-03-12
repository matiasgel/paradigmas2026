# FAQ Anticipado — Tema 02: Sintaxis y Semántica de Lenguajes
# Generado: 2026-03-11 | Agente: student-simulator + test-runner
# Modo: BATCH — 4 perfiles

---

## EN CLASE (durante la cursada de 120 min)

### Bloque 1 — Sintaxis y semántica

**[Ansioso]** *"¿La diferencia entre error estático y dinámico entra en el parcial?"*
> Sí. Es una distinción central: el error estático lo detecta el compilador sin ejecutar el programa. El dinámico aparece en runtime. En TypeScript, `const x: number = "hola"` es error estático (el compilador lo ve). Dividir por una variable que resulta ser cero en runtime es un error dinámico.

**[Disperso]** *"Profe, ¿esto es lo mismo que lo del Tema 01?"*
> Relacionado, no igual. En Tema 01 vimos que TypeScript compila a JavaScript. Hoy respondemos *por qué* ese proceso existe: para verificar que el código respeta las reglas de sintaxis y semántica. Es la capa teórica detrás del compilador.

**[Estratégico]** *"¿TypeScript usa BNF para definir su sintaxis?"*
> Sí. El spec oficial de TypeScript define su gramática en una variante de EBNF. Si ingresan a la especificación en typescriptlang.org pueden ver las producciones. El compilador `tsc` implementa ese parser.

**[Recursero]** *"¿Hay una regla para saber si es error de sintaxis o semántica?"*
> Heurística útil: si el compilador lo rechaza *sin ejecutar*, es sintáctico o semántico estático. Si falla *en ejecución*, es semántico dinámico. Pero ojo — no es 100% precisa, porque algunos checkers difieren entre lenguajes.

---

### Bloque 2 — Análisis léxico

**[Ansioso]** *"¿Un lexema siempre corresponde a un solo token?"*
> Sí. Un lexema es la cadena de caracteres concreta; el token es la categoría. `indice` es el lexema, `<identificador>` es su token. Cada lexema pertenece a exactamente una categoría en un momento dado.

**[Disperso]** *"¿El scanner somos nosotros o lo hace el compilador solo?"*
> El compilador. El scanner (o lexer) es el primer módulo del compilador. Lee el código fuente caracter por caracter y agrupa en lexemas. Nosotros lo estamos modelando manualmente para entender qué hace internamente.

**[Recursero]** *"¿Puedo usar la tabla de la guía como plantilla para el TP?"*
> El ejercicio 2 del TP pide que vos hagas la derivación, no que copies la tabla. El formato de la guía es referencia — el contenido tiene que ser tuyo aplicando las reglas de la gramática dada.

**[Estratégico]** *"¿Por qué el analizador léxico es un módulo aparte y no parte del parser?"*
> Separación de responsabilidades: el lexer trabaja sobre caracteres individuales (nivel regular, DFA), el parser trabaja sobre tokens (nivel libre de contexto, gramática). Mezclarlos haría el compilador mucho más complejo. Chomsky hierarchy explica por qué son niveles distintos.

---

### Bloque 3 — Gramáticas formales, BNF y EBNF

**[Ansioso]** *"¿Tengo que memorizar la notación BNF para el parcial?"*
> No memorizarla: entenderla. En el parcial vas a tener la gramática dada. Lo que se evalúa es que puedas leer una producción, aplicarla en una derivación, y construir el árbol. Es como aprender a leer un mapa — no memorizás el mapa, aprendés a usarlo.

**[Ansioso]** *"¿El árbol tiene que quedar exactamente igual al de la guía?"*
> Si la derivación es la misma, sí. Pero una gramática ambigua puede producir más de un árbol. En ese caso cualquier árbol válido (que derive la cadena correctamente) es correcto. Lo importante es que cada nodo interno corresponda a un símbolo no-terminal y cada hoja a un terminal.

**[Disperso]** *"¿Esto entra en el examen?"*
> Sí. Derivación y árboles de análisis son parte del parcial. Específicamente: leer una gramática BNF/EBNF, derivar una cadena mostrando los pasos, y construir el árbol de análisis sintáctico.

**[Disperso]** *"¿Está grabada la clase?"*
> [Señal de desconexión]. El material completo está en la guía de estudio §4 con la derivación resuelta paso a paso. Ahora en clase estamos haciendo el proceso en vivo — resulta más fácil entenderlo cuando lo ven construirse.

**[Recursero]** *"¿Hay un ejemplo de gramática ya resuelta para copiar en el ejercicio 4?"*
> El ejercicio 4 pide que escribas tu propia gramática para un lenguaje nuevo (expresiones booleanas). No hay solución previa porque es un ejercicio de diseño. Lo que sí tenés es la gramática del ejercicio 1 como modelo de estructura — mismos componentes, distinto lenguaje.

**[Estratégico]** *"¿La diferencia entre BNF y EBNF es solo notacional o hay diferencias de poder expresivo?"*
> Solo notacional. EBNF no agrega poder expresivo — cualquier gramática EBNF puede reescribirse en BNF pura. La diferencia es ergonómica: EBNF es más compacta y legible para expresar repetición (`{}`) y opcionalidad (`[]`). Los lenguajes que describen son los mismos: lenguajes libres de contexto.

**[Estratégico]** *"¿Una gramática ambigua puede ser útil igual?"*
> En teoría de lenguajes formales, la ambigüedad es un problema para los compiladores (no saben cuál árbol construir). Pero algunos lenguajes permiten ambigüedades resueltas por reglas de precedencia y asociatividad (como en expresiones matemáticas). C y C++ tienen algunas ambigüedades históricas resueltas por convención.

---

### Bloque 4–5 — Semántica operacional

**[Ansioso]** *"¿'Semántica operacional' es la semántica de todos los lenguajes o solo de algunos?"*
> Es uno de los enfoques formales para definir semántica (hay otros: denotacional, axiomática). Para esta materia, nos quedamos en el nivel conceptual: la semántica operacional define el significado de un programa describiendo cómo un intérprete abstracto lo ejecutaría paso a paso. Sebesta §3 tiene más detalle si querés profundizar.

**[Disperso]** *"¿El pipeline compilador siempre tiene esas 4 etapas?"*
> Las etapas básicas (lexer → parser → análisis semántico → generación de código) son estándar. Algunos compiladores tienen más pasos (optimización, varias pasadas), algunos menos. Go y TypeScript tienen pipelines similares aunque con implementaciones distintas.

---

### Bloque 6 — LLMs y constrained decoding

**[Todos]** *"¿Los LLMs siempre usan gramáticas EBNF para constrained decoding?"*
> No exclusivamente EBNF — algunos usan JSON Schema, regex, o gramáticas definidas en librerías específicas (como Outlines o Instructor en Python). EBNF es el formalismo teórico que los fundamenta, pero en la práctica los frameworks lo abstraen. El paper de Willard & Louf (2023) que figura en la guía describe la implementación.

**[Estratégico]** *"Si TypeScript usa EBNF para su spec, ¿`tsc` implementa un parser EBNF?"*
> Técnicamente, `tsc` tiene un parser LL(k) escrito a mano que corresponds a la gramática EBNF del spec. No usa la EBNF directamente como código — el spec es la especificación, el parser es la implementación. La gramática TS está en el repositorio de TypeScript como parte de la documentación.

**[Recursero]** *"Para el ejercicio 5, ¿con qué LLM tengo que hacer el experimento?"*
> Cualquiera que soporte structured output: ChatGPT-4, Claude (sonnet/haiku), Gemini. Lo importante es que uno de los 3 intentos use instrucción en texto libre y otro use JSON Schema. La diferencia en los resultados es lo que tenés que analizar.

---

## ESTUDIANDO SOLOS (con la guía de estudio)

### Sección 4 — Derivación y árboles

**[Ansioso — leyendo la guía]** *"En el paso 5 de la derivación dice que se aplica la regla `<expr> ::= <expr> + <term>` pero no entiendo de dónde sale `<term>`."*
> En la producción `<expr> ::= <expr> + <term>`, al expandir `<expr>` obtenés tres símbolos: el nuevo `<expr>`, el terminal `+`, y `<term>`. El árbol muestra que `<term>` es hermano de `<expr>` y `+` en ese nivel. Si lográs ver cada producción como "reemplazar un nodo por sus hijos", el árbol se hace más claro que la tabla.

**[Disperso — leyendo la guía]** *"Hay muchos ejemplos pero no entiendo el orden en que se leen."*
> La guía está diseñada para leerse en orden: primero §4.1 (definiciones), luego §4.2 (tokenización), luego §4.3 (BNF y derivación). No saltes directo a §4.3 sin leer §4.1 — los símbolos no van a tener sentido aislados.

**[Recursero — buscando atajos]** *"En el glosario dice que un árbol de análisis tiene nodos internos y hojas, ¿eso alcanza para el ejercicio 2?"*
> No — el ejercicio 2 pide *construir* el árbol con la derivación dada. El glosario da la definición conceptual; para construirlo necesitás seguir el proceso de derivación paso a paso como en el ejemplo del §4.3.

---

### Sección 5 — Árbol sintáctico

**[Ansioso — leyendo la guía]** *"El árbol en ASCII es confuso, no sé cuál nodo está arriba de cuál."*
> La raíz del árbol es el símbolo inicial (`<programa>` o `<sentencia>`). Los hijos están sangrados hacia la derecha. Para leerlo más fácil, dibujalo vos en papel con círculos y líneas — transcribir el ASCII a diagrama manual es un buen ejercicio de comprensión.

**[Estratégico — leyendo la guía]** *"¿Por qué algunos tutoriales de parsers online usan ANTLR y no BNF directamente?"*
> ANTLR es un generador de parsers que usa su propia variante de EBNF como input. Internamente genera código que implementa el parser. Es una herramienta práctica que abstrae la construcción manual del árbol. Para la materia trabajamos con BNF/EBNF puro para entender el fundamento — ANTLR lo usarían en una materia de compiladores.

---

### Sección 7 — LLMs y gramáticas

**[Disperso — parte II del TP]** *"¿Con qué prompt tengo que probar el LLM para el ejercicio 5?"*
> El enunciado dice: en 3 intentos usá instrucción en lenguaje natural ("respondé en JSON con campos X, Y, Z"), y en otros 3 tentativas pasá un JSON Schema explícito. Comparás cuántas veces el output cumple exactamente el schema en cada condición. La diferencia es lo que argumentás.

**[Recursero — parte II del TP]** *"¿El análisis tiene que ser largo?"*
> No largo, pero tiene que comparar los resultados de los dos métodos. Una tabla con los 6 intentos (3 natural language + 3 JSON schema), el output obtenido, y si cumplió el schema o no, más 2–3 oraciones explicando la diferencia = respuesta completa. No es un ensayo.
