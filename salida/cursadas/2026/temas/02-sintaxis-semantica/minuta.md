# Minuta — Tema 02: Sintaxis y Semántica de Lenguajes

> **Estado:** GENERADA
> **Agente:** Dr. Roberto ✍️ (class-writer)
> **Fecha:** 2026-03-19
> **Duración total:** 120 minutos
> **Perfil docente:** profesor-teorico
> **Semana / Clase:** Semana 1 · Clase 2 de 2
> **Input:** `salida/cursadas/2026/temas/02-sintaxis-semantica/diseno.md` (REDISEÑO)
> **Filminas:** F-00 a F-37

---

## Antes de empezar — Preparación (−10 min antes de clase)

- Abrir Deno Playground: **<https://playground.deno.land>** — tener listo el snippet de la actividad B1
- Preparar en el editor (o en el playground) los tres ejemplos de error de TypeScript de F-06b
- Escribir en el pizarrón antes de que entren los alumnos:
  ```
  sintaxis = forma
  semántica = significado
  ```
  *Genera curiosidad y ancla la clase antes de abrir la boca.*
- Verificar proyector y que las filminas cargan correctamente
- Imprimir o tener visible el mapa de bloques (F-01) para seguimiento temporal

---

## APERTURA — Conexión con Tema 01 (5 min, fuera del tiempo de bloques)

> 📽 **Filmina en pantalla:** F-00 (portada)

Abrir con la pregunta de la portada, pero sin leerla — dejar que los alumnos la lean:

> *"¿Cómo sabe el compilador si tu programa está bien escrito?"*

Esperar reacciones. Es probable que respondan "por las reglas del lenguaje" o "por la gramática".

Decir: *"Exacto. Hoy vamos a precisar qué es eso. Y la segunda pregunta — ¿sabe SIEMPRE cuándo está mal? — la responderemos al final."*

> 📽 **Filmina F-01** → Mostrar la agenda.

Contextualizar la clase en el arco del cursado: *"En la clase anterior vimos que TypeScript compila a JavaScript. Hoy vamos a abrir la caja del compilador: ¿cómo decide si lo que escribimos es válido? Eso requiere entender sintaxis y semántica."*

---

## BLOQUE 1 — Sintaxis y semántica: conceptos fundamentales (20 min)

> 📽 **Filminas:** F-02 · F-03 · F-04 · F-05 · F-06 · F-06b

**Objetivo del bloque:** Distinguir forma de significado. Establecer que un programa puede tener forma correcta y significado incorrecto.

---

### Entrada al bloque *(📽 F-02)* (2 min)

Mostrar F-02 (continuidad con Tema 01):

*"La clase pasada cerramos con que `tsc` compila TypeScript a JavaScript. Hoy la pregunta técnica es: ¿cómo sabe `tsc` si el programa está bien escrito antes de compilar? La respuesta tiene dos capas: sintaxis y semántica."*

---

### Definición de sintaxis *(📽 F-03)* (4 min)

> *"¿Qué entienden por sintaxis? No den la definición del libro — díganme con sus palabras."*

Anotar las ideas que surjan en el pizarrón. Luego mostrar F-03 y formalizar:

- **Sintaxis = reglas de forma**. No importa todavía qué hace el programa — solo si está bien construido.
- El ejemplo canónico `if (<expresión>) <sentencia>` viene de las slides de cátedra: mostrar que es una regla abstracta que no dice nada sobre el efecto.

> *"La sintaxis es como la ortografía y la gramática del español: una oración puede estar bien escrita y no tener sentido."*

---

### Definición de semántica *(📽 F-04)* (4 min)

Mostrar F-04. Punto de tensión clave:

> *"Un programa puede ser sintácticamente correcto y semánticamente incorrecto. ¿Alguno puede dar un ejemplo intuitivo?"*

Dejar que intentan. Si no hay respuestas, adelantar: *"En un momento lo vemos con TypeScript."*

---

### Criterios sintácticos de un buen lenguaje *(📽 F-05)* (4 min)

Mostrar F-05. Estas son las cinco propiedades que debería tener la sintaxis de un lenguaje bien diseñado (slides cátedra 2025):

- **Legibilidad:** enfatizar que Python prioriza esto explícitamente en su diseño
- **Facilidad de escritura:** Perl sacrificó esto para ganar expresividad comprimida — todo tiene costo
- **Carencia de ambigüedad:** anticipa el Bloque 3 (gramáticas ambiguas)

> *"Estos criterios no son independientes — hay trade-offs. Vamos a ver ambigüedad en detalle en el Bloque 3."*

---

### Actividad y respuestas *(📽 F-06 → F-06b)* (6 min)

Mostrar F-06 y pedir que clasifiquen en parejas (2 min). Luego mostrar F-06b con las respuestas y discutir:

- `const x: number = "hola"` → semántico estático: el árbol sintáctico es válido, el tipo es incompatible
- `if true { ... }` → sintáctico: falta el paréntesis, el parser no puede construir el árbol
- `y = undefined; y.length` → semántico dinámico: en runtime, `.length` sobre `undefined` lanza excepción

> *"Este cuadro va a reaparecer al final de la clase, en el Bloque 5. Guárdenlo en la cabeza."*

---

## BLOQUE 2 — Estructura léxica: del texto al token (20 min)

> 📽 **Filminas:** F-07 · F-08 · F-09 · F-10 · F-11

**Objetivo del bloque:** Entender cómo se transforma un programa-texto en unidades mínimas para el análisis formal.

> 📌 **Nota pedagógica:** Este bloque anticipa Sebesta Cap. 4 §4.1 *antes* de Cap. 3 (gramáticas formales — Bloque 3). La inversión es intencional: el lexer produce tokens, y esos tokens son los *terminales* que las reglas BNF del Bloque 3 combinarán. Orden didáctico: concreto → abstracto. Si los alumnos notan la inversión, confirmarlo: *"Sí, el libro va al revés. Lo hacemos así porque ver primero el lexer hace que las gramáticas tengan anclaje práctico."*

---

### El punto de partida: texto plano *(📽 F-07)* (4 min)

Mostrar F-07.

> *"Antes de entrar en gramáticas formales, una pregunta básica: ¿qué le llega al compilador? No llega TypeScript 'con sentido' — llega una cadena de caracteres. El primer paso es cortar esa cadena en piezas con nombre."*

Escribir en el pizarrón: `result = oldsum - value / 100;`

> *"¿Cuántas 'piezas' ven en esta línea? ¿Cómo las cortarían?"*

---

### Dos niveles de análisis *(📽 F-08)* (3 min)

Mostrar F-08. Remarcar que la separación léxica/sintáctica tiene tres razones prácticas (Sebesta §4.1): simplificar, eficiencia, portabilidad. No profundizar — cada una es intuitiva.

---

### Vocabulario básico del LP *(📽 F-09)* (4 min)

Mostrar F-09. Esta lista viene de las slides de cátedra 2025.

> *"Todo lenguaje define cómo se construyen estas categorías. Java y Python tratan diferente a las mayúsculas — eso es una regla léxica."*

Pausa de reconocimiento: *"¿Cuál de estas categorías no tienen en TypeScript o es diferente a otros lenguajes que conocen?"*

---

### Lexemas y tokens *(📽 F-10)* (4 min)

Mostrar F-10. La tabla de `indice = 5 * contador + 1` viene exactamente de las slides de cátedra 2025.

- **Lexema:** la cadena de caracteres concreta (`indice`, `5`)
- **Token:** la categoría abstracta (`identificador`, `constante_entera`)

> *"El lexema es lo que escribieron. El token es cómo el compilador lo clasifica. Un mismo token (`identificador`) puede tener miles de lexemas distintos."*

---

### El analizador léxico *(📽 F-11)* (5 min)

Mostrar F-11.

> *"El lexer agrupa, descarta ruido (espacios, comentarios) y clasifica. Todavía no sabe si `indice` es una variable, un parámetro o una constante — eso lo decide el análisis semántico más adelante."*

Demo rápida (opcional, 2 min): en el Deno playground, escribir:
```typescript
const x: number = 5
```
y pedir que identifiquen los tokens mentalmente. *"El lexer ve: `const` (palabra reservada), `x` (identificador), `:` (delimitador), `number` (identificador de tipo), `=` (op-asignación), `5` (constante_entera)."*

---

## BLOQUE 3 — Gramáticas formales: BNF y EBNF (30 min)

> 📽 **Filminas:** F-12 · F-13 · F-14 · F-15 · F-16 · F-17 · F-18 · F-19 · F-20

**Objetivo del bloque:** Leer e interpretar especificaciones formales de sintaxis. Usar BNF para describir y derivar construcciones. Entender la ambigüedad como defecto de diseño.

---

### ¿Por qué gramáticas formales? *(📽 F-12)* (3 min)

Mostrar F-12.

> *"¿Cómo describirían la sintaxis de TypeScript en castellano? ¿Cómo sabrían si cubrieron todos los casos?"*

La respuesta: con reglas BNF o EBNF, se puede verificar automáticamente.

> *"Python tiene su gramática oficial publicada como BNF. Podés leerla en docs.python.org. Es la fuente de verdad, no la documentación en inglés."*

---

### Gramáticas libres de contexto *(📽 F-13)* (4 min)

Mostrar F-13. Presentar la tupla `(N, T, S, P)` con ejemplos concretos de la gramática que viene en F-15. No cargarlo de teoría formal — el foco está en reconocer los componentes.

> *"Clasificación de Chomsky (1959): las gramáticas de los LP son libres de contexto. Eso significa que las reglas se aplican independientemente del contexto — veremos que la semántica, no."*

---

### BNF: metasímbolos y reglas *(📽 F-14)* (5 min)

Mostrar F-14. Leer la regla del `if` en voz alta y pedir que la lean después.

- `::=` es "se define como"
- `<enunc_if>` es no terminal (se expande por sus reglas)
- `if`, `then`, `else` son terminales

> *"Una regla BNF es como una receta: LHS es el plato, RHS son los ingredientes — que a su vez pueden ser recetas."*

---

### Gramática de trabajo *(📽 F-15)* (3 min)

Mostrar F-15. Esta es la gramática que usarán para la derivación.

> *"Esta gramática describe un mini-lenguaje con una sola sentencia de asignación. Los únicos identificadores son A, B y C. El objetivo no es representatividad — es que derivar sea manejable en clase."*

---

### Derivación paso a paso *(📽 F-16)* (5 min)

Mostrar F-16. Leer la derivación en voz alta, despacio, explicando cada `⇒`:

> *"Primera producción: `<assign> → <id> := <expr>`. Aplicamos `<id> → A`. Ahora `<expr>` tiene cuatro opciones — elegimos `<id> * <expr>`..."*

Completar hasta llegar a `A := B * (A + C)`.

> *"La secuencia entera, con los strings intermedios, se llama 'derivación'. Cada string intermedio es una 'forma sentencial'."*

---

### Árbol sintáctico *(📽 F-17)* (3 min)

Mostrar F-17. Enfatizar:

- Los **nodos internos** corresponden a no terminales del proceso de derivación
- Las **hojas** son los terminales — lo que quedó en la cadena final
- El árbol tiene **la misma información** que la derivación, organizada jerárquicamente

> *"El compilador construye este árbol internamente. Es la representación interna del programa durante el análisis."*

---

### Ambigüedad *(📽 F-18)* (4 min)

Mostrar F-18. Dibujar en el pizarrón los dos árboles posibles para `J := 1 + 2 * 3`:

- Árbol 1: `(1+2)*3 = 9`
- Árbol 2: `1+(2*3) = 7`

> *"La gramática produce dos estructuras para la misma cadena. El compilador no sabe cuál elegir. Esto no es un problema del compilador — es un defecto de la gramática."*

*"¿Cómo se resuelve en la práctica? Rediseñando la gramática con reglas que impongan precedencia (multiplicación sobre suma), o declarando una regla de desambiguación explícita."*

---

### EBNF *(📽 F-19)* (3 min)

Mostrar F-19. Comparar con BNF: misma potencia, menos ruido.

> *"EBNF agrega `[]` para opcional y `{}` para repetición. El mismo LP simple del pizarrón queda más legible. Las gramáticas oficiales de lenguajes modernos usan EBNF o variantes."*

---

### Actividad breve *(📽 F-20)* (5 min — incluyendo discusión)

Mostrar F-20. Dar 2-3 min para que trabajen solos o en pares.

**Respuesta esperada:**
```
C := D - E * F
C := D - E * F  →  <assign> ⇒ <id> := <expr> ⇒ C := <id> – <expr> ⇒ ...
```

Preguntar si la gramática deja ambigüedad para la resta: *"¿`D - E * F` puede leerse como `(D-E)*F` o `D-(E*F)`? Si la gramática no define precedencia, sí."*

---

## BLOQUE 4 — Diagramas de sintaxis y notación gráfica (10 min)

> 📽 **Filminas:** F-21 · F-22 · F-23

**Objetivo del bloque:** Leer especificaciones gráficas de sintaxis. Entender que son equivalentes a EBNF pero más visuales.

---

### Definición y convención *(📽 F-21)* (3 min)

Mostrar F-21.

> *"Los diagramas de sintaxis describen exactamente lo mismo que BNF/EBNF — solo cambia el medio. En lugar de texto, usamos flechas y cajas."*

Enfatizar la analogía de "recorrer el diagrama": una cadena es válida si puede viajar de la entrada a la salida atravesando exactamente los terminales y no terminales en el orden correcto.

---

### Ejemplo del condicional *(📽 F-22)* (4 min)

Mostrar F-22. Trazar con el dedo (o puntero) los dos caminos del diagrama:

- Camino superior: `if expr { ... }` → sin `else`
- Camino inferior: `if expr { ... } else { ... }` → con `else`

> *"El camino superior no es optativo casualmente — es exactamente el primer caso de la regla EBNF del F-19. Los dos formatos son intercambiables."*

---

### ¿Para qué sirven? *(📽 F-23)* (3 min)

Mostrar F-23.

Breve mención: *"La documentación oficial de TypeScript usa diagramas de sintaxis para describir construcciones. La próxima vez que vean uno, ya saben leerlo."*

---

## BLOQUE 5 — Semántica: síntesis y tipos (12 min)

> 📽 **Filminas:** F-24 · F-25 · F-26 · F-27 · F-28
>
> *Fuente: Sebesta, Cap. 3 §§3.4–3.5*

**Objetivo del bloque:** Definir la semántica como disciplina del lenguaje, distinguir semántica estática de dinámica, y presentar los tres enfoques formales de semántica dinámica. Tratamiento de **síntesis** — sin desarrollo de formalismos internos.

---

### ¿Qué es la semántica? *(📽 F-24)* (3 min)

Mostrar F-24.

> *"Retomemos la actividad de la apertura. Clasificamos tres errores de TypeScript. El del `if` era sintáctico. Los otros dos son semánticos — uno antes de ejecutar, uno durante. ¿Cuál es cuál y por qué?"*

Dejar que respondan. Luego:

> *"Sebesta dice explícitamente que no existe un método universalmente aceptado para describir semántica. La sintaxis tiene su BNF — la semántica no tiene un equivalente único. Hay tres enfoques."*

Marcar la dimensión estática/dinámica en el pizarrón.

---

### Gramáticas de atributos *(📽 F-25)* (3 min)

Mostrar F-25. Breve dado el tiempo disponible:

> *"Las gramáticas libres de contexto no pueden expresar `si la variable se usa con el mismo tipo con que se declaró`. Eso es sensible al contexto. Las gramáticas de atributos de Knuth (1968) extienden BNF con atributos — como el tipo — y reglas que los calculan sobre el árbol."*

> *"Esto es exactamente lo que hace el type checker de TypeScript: calcula atributos de tipo sobre el árbol sintáctico y verifica que sean coherentes."*

---

### TypeScript como semántica estática *(📽 F-26)* (2 min)

Mostrar F-26. Demo rápida en el playground si hay tiempo — escribir `const x: number = "texto"` y mostrar el error de TypeScript. El error dice exactamente: `Type 'string' is not assignable to type 'number'` — la incompatibilidad de atributos.

---

### Tres enfoques de semántica dinámica *(📽 F-27)* (2 min)

Mostrar F-27. No desarrollar cada uno — solo presentarlos como mapa:

> *"Para describir qué hace un programa cuando ejecuta, hay tres tradiciones formales. Operacional: defino el significado como pasos en una máquina abstracta. Denotacional: el significado es una función matemática. Axiomática: el significado son las aserciones que se cumplen antes y después."*

> *"El estudio riguroso de cada uno corresponde a Semántica Formal o Lógica. En este curso, los usamos como referencias para ubicarnos."*

---

### Síntesis — tres niveles *(📽 F-28)* (2 min)

Mostrar F-28. Cerrar el círculo con la actividad de apertura:

> *"Volvemos al cuadro del principio. Ahora tenemos los nombres: el primer error lo detecta el parser (sintaxis), el segundo el type checker (semántica estática, gramáticas de atributos), el tercero el runtime (semántica dinámica)."*

> *"El Bloque 6 muestra cómo estos tres componentes se integran en un sistema coherente."*

---

## BLOQUE 6 — Síntesis: pipeline completo y gramáticas en la IA (15 min)

> 📽 **Filminas:** F-29 · F-30 · F-31 · F-32 · F-33 · F-34

**Objetivo del bloque:** Integrar en un sistema coherente todos los hilos de la clase. Conectar gramáticas formales con el constrained decoding en LLMs actuales.

---

### El pipeline del compilador *(📽 F-29)* (4 min)

Mostrar F-29.

> *"Todo lo que estudiamos hoy encaja acá: el lexer produce tokens (Bloque 2), el parser construye el árbol a partir de la gramática (Bloque 3), el type checker evalúa semántica estática (Bloque 5), y finalmente se genera código o se ejecuta."*

Señalar que `tsc` hace exactamente este pipeline. Los mensajes de error de `tsc` incluyen línea y columna — el lexer registró la posición de cada token para que el error sea útil.

---

### Top-down vs. bottom-up *(📽 F-30)* (2 min)

Mostrar F-30. Solo conceptual — no entrar en algoritmos.

> *"Hay dos grandes familias de parsers. Top-down: arrancás del símbolo inicial y derivás hacia los tokens. Bottom-up: arrancás de los tokens y reducís hacia el símbolo inicial. Hoy no estudiamos ningún algoritmo concreto — solo ubicamos el problema."*

---

### Compilador vs. intérprete revisitado *(📽 F-31)* (3 min)

Mostrar F-31.

> *"Compilador e intérprete hacen lo mismo hasta el análisis semántico. La diferencia está en qué hacen después: el compilador traduce, el intérprete ejecuta directamente."*

> *"TypeScript con `tsc`: lexer → parser → type checker → emite .js. Luego V8 interpreta el .js. Es una cadena mixta — exactamente lo que predijo Gabbrielli con las máquinas abstractas intermedias."*

---

### Ejemplo LLM + EBNF *(📽 F-32 → F-33)* (4 min)

Mostrar F-32 → F-33 en secuencia rápida.

> *"Esto puede parecer una digresión — no lo es. Cuando pedimos a un LLM que devuelva JSON, idealmente queremos que el JSON sea válido. Hoy hay sistemas que compilan una gramática EBNF a un autómata y lo usan para filtrar, token a token, qué puede generar el modelo — solo tokens que sean parte de una derivación válida. Eso se llama constrained decoding."*

> *"Las gramáticas de Chomsky (1959) y la notación BNF de Backus (1960) son la infraestructura de esos sistemas actuales."*

---

### De Chomsky a hoy *(📽 F-34)* (2 min)

Mostrar F-34 como remate.

> *"La formalización de la sintaxis no terminó en 1960. Sigue activa en 2026 como infraestructura de sistemas de IA. Lo que estudiaron hoy no es historia — es base tecnológica."*

---

## CIERRE (13 min — buffer flexible)

> 📽 **Filminas:** F-35 · F-36 · F-37

---

### Mapa final *(📽 F-35)* (3 min)

Mostrar F-35. Recorrer el mapa en voz alta — cada bloque con una frase:

1. *"Sintaxis: la forma."*
2. *"Léxico: el texto se convierte en tokens identificados."*
3. *"Gramáticas: los tokens se organizan en estructura jerárquica."*
4. *"Diagramas: podemos representar esa gramática visualmente."*
5. *"Semántica: el significado estático (tipos) y dinámico (tres enfoques)."*
6. *"Pipeline: todo encaja para compilar e interpretar — y hoy también para controlar LLMs."*

---

### Preguntas de cierre *(📽 F-36)* (5 min)

Mostrar F-36. Leer en voz alta cada pregunta y dar 30 segundos de silencio para pensar antes de que respondan:

1. ¿Qué detecta el parser que no detecta el type checker? — *El parser detecta errores de forma; el type checker asume ya que el árbol existe y bien formado.*
2. ¿Qué detecta el type checker que no detecta el parser? — *Incompatibilidades de tipo, uso de variables no declaradas, aridad incorrecta.*
3. ¿Por qué una gramática ambigua es un problema? — *El compilador no puede elegir entre dos interpretaciones.*
4. ¿Diferencia entre semántica estática y dinámica? — *Estática: antes de ejecutar (tipo). Dinámica: en ejecución (efecto).*
5. ¿Dónde reaparecen BNF/EBNF hoy? — *Constrained decoding en LLMs, JSON Schema, parsers de defs. de configuración.*

---

### Referencias *(📽 F-37)* (2 min, o saltar si no hay tiempo)

Mostrar F-37 brevemente. Indicar que `diseno.md` tiene los links directos a los papers de 2023–2026 citados.

> *"Para el parcial: Sebesta Cap. 3 §§3.1–3.5 y Cap. 4 §§4.1–4.3 son la fuente académica principal. Las slides de cátedra 2025 son el baseline histórico."*

---

## Post-clase — Checklist docente

- [ ] Actividad de F-06 completada + corrección colectiva  
- [ ] Actividad de F-20 completada + árbol en el pizarrón  
- [ ] Cuadro de tres niveles de error (F-28) cerrado correctamente  
- [ ] Referencias de Sebesta mencionadas (Cap. 3 y Cap. 4)  
- [ ] Buffer de 13 minutos consumido (¿en qué?)  

---

## Notas de transición hacia Tema 03

El Tema 03 entra al **paradigma funcional** con TypeScript. La conexión natural con este tema:

- Las funciones como *ciudadanos de primera clase* tienen semántica que el type checker de TS necesita razonar (tipos de función, aridad)
- El sistema de tipos de TypeScript — que usamos hoy como *caso concreto* de semántica estática — se estudiará en profundidad en el Tema de sistemas de tipos
- Nombres, entorno y binding (binding time, static vs dynamic) se profundizan en Tema 09
