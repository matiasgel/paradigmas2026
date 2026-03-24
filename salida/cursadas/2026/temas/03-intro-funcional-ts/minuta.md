# Minuta — Tema 03: Introducción a Programación Funcional con TypeScript

> **Estado:** GENERADA
> **Agente:** Dr. Roberto (class-writer)
> **Fecha:** 2026-03-23
> **Duración total:** 120 minutos
> **Perfil docente:** profesor-teorico
> **Semana / Clase:** Semana 2, Clase 1 de 1
> **Input:** `temas/03-intro-funcional-ts/diseno.md`
> **Output:** `minuta.md` + `filminas.md`

---

## Antes de empezar — Preparación (−10 min antes de clase)

- Abrir **Deno Playground** o **TypeScript Playground**: <https://www.typescriptlang.org/play>
- Tener preparados los snippets de TypeScript del Bloque 2 y 3 listos para pegar (están al final de esta minuta en la sección **Snippets de demo**)
- Tener abierto **REPL de Clojure** en línea: <https://tryclojure.org> o <https://repl.it/languages/clojure>
- Verificar proyector y filminas desde F-01

**Pizarrón antes de que entren (opcional pero efectivo):** escribir en el ángulo superior izquierdo:
```
Turing (1936): estado + transiciones
Church (1936): funciones + sustitución
```
Genera curiosidad antes de que empiece — muchos preguntan antes de sentarse.

---

## APERTURA (2 min, fuera del tiempo de bloques)

> 📽 **Filmina en pantalla:** F-01 (portada)

Tono: directo, situador. Esta clase es la transición del mundo imperativo al funcional.

- *"Ya vieron TypeScript imperativamente en T01. Hoy van a verlo de una forma completamente distinta — vamos a prohibirnos usar `let`, loops `for`, y cualquier mutación."*
- *"Puede parecer restrictivo. Al final de la clase van a entender por qué esa restricción es poder."*
- Anticipar la estructura: historia → fundamentos → código → HOF → recursión → IA

---

## BLOQUE 0 — Recap y punto de partida (5 min)

> 📽 **Filminas de este bloque:** F-02

**Objetivo:** conectar con T01, activar conocimiento previo.

### Entrada al bloque *(📽 F-02)* (3 min)

Mostrar la tabla de paradigmas del T01 y preguntar en frío:

> *"¿Quién me recuerda cuál era la raíz formal del paradigma funcional?"*

Esperar que alguien diga "lambda" o "Church". Si nadie responde en 10 segundos, dar el dato y continuar — no hay tiempo para esperar.

- Señalar que el funcional y el imperativo nacieron el mismo año, de la misma pregunta
- Plantear la pregunta disparadora de la clase:

> *"¿Qué tiene de especial un lenguaje donde ninguna variable puede cambiar de valor? Hoy lo descubren."*

### Anticipar el lenguaje de contraste (2 min)

- Presentar **Clojure** brevemente: dialecto moderno de Lisp, JVM, inmutabilidad por defecto
- Aclarar el modo de uso: *"Vamos a leer Clojure — no a escribirlo. Es el espejo puro que nos muestra a qué apuntamos cuando programamos TypeScript funcionalmente."*

---

## BLOQUE 0.5 — Historia y raíces formales (15 min)

> 📽 **Filminas de este bloque:** F-03 · F-04 · F-05 · F-06 · F-07 · F-08

**Objetivo:** anclar el paradigma en su historia matemática. Esta sección es narrativa — no hay demo de código. Ritmo: fluido y con énfasis en los momentos de revelación histórica.

### El Entscheidungsproblem *(📽 F-03)* (3 min)

Presentar el problema de Hilbert con el tono de un misterio matemático:

> *"1928. Hilbert plantea una pregunta aparentemente simple: ¿puede una máquina determinar si cualquier enunciado matemático es verdadero o falso? Dos jóvenes matemáticos, trabajando de forma independiente, responden — y sus respuestas cambian la historia de la computación."*

Señalar que para responder la pregunta, primero hay que definir qué es una "máquina" — y ahí es donde nacen los dos paradigmas.

### La respuesta de Turing *(📽 F-04)* (4 min)

Describir la Máquina de Turing como el modelo del "calculador humano":

- Enfatizar el movimiento físico: cabezal, cinta, leer/escribir, moverse, cambiar estado
- Trazar el camino directo: **Máquina de Turing → Von Neumann (1945) → CPU + RAM → Fortran → C → Java → el imperativo que ya conocen**
- Nombrar el Problema de la Parada como la respuesta "NO" de Turing: ninguna máquina puede decidir si otra terminará
- Una sola frase para anclar: *"Variables en C son celdas de la cinta. Un `for` loop es una tabla de transiciones. El imperativo es la Máquina de Turing con mejor sintaxis."*

### La respuesta de Church *(📽 F-05 · F-06)* (5 min)

Introducir el λ-cálculo desdramatizándolo:

> *"Church no pensó en máquinas. Pensó en funciones matemáticas. Su sistema tiene tres reglas: definir una función, aplicarla, y sustituir el argumento en el cuerpo. Nada más."*

Usar la filmina del factorial para mostrar la reducción paso a paso:

```
fact 3 → if 3=0 then 1 else 3 * fact(2) → 3 * fact(2) → ...
```

Preguntar en voz alta: *"¿Cuántas variables se modificaron en ese proceso? Cero. No hay ninguna."*

Dar la respuesta de Church al Entscheidungsproblem: también NO — y en 1937, Turing demostró que ambos modelos son equivalentes.

### Los dos paradigmas como consecuencia *(📽 F-07)* (2 min)

Mostrar la tabla comparativa y hacer la observación histórica:

> *"Von Neumann implementó la Máquina de Turing en silicio. Por eso el imperativo domina el hardware. Pero el λ-cálculo no desapareció — se convirtió en Lisp."*

### La línea de tiempo *(📽 F-08)* (1 min, rápido)

Recorrer la tabla de forma expeditiva — el dato clave es Backus (1977):

> *"El mismísimo creador de Fortran, en su discurso del Premio Turing, dijo que el estilo imperativo era pobre y propuso reemplazarlo por programación funcional pura. Lo llamó FP. Nadie le hizo caso... durante 30 años. React, Rust y TypeScript moderno le están dando la razón."*

---

## BLOQUE 1 — Fundamentos del paradigma funcional (20 min)

> 📽 **Filminas de este bloque:** F-09 · F-10 · F-11 · F-12

**Objetivo:** construir el modelo mental correcto antes de ver código TypeScript.

### La función matemática como modelo *(📽 F-09)* (5 min)

Arrancar con la pregunta:

> *"¿`getTime()` es una función matemática? Tiene nombre, recibe argumentos... pero a las 10:00 devuelve un valor y a las 10:01 devuelve otro. ¿Es la misma función?"*

Dejar que respondan. La respuesta correcta: no — porque el resultado no depende solo del input.

Presentar las tres propiedades (determinismo, sin efecto colateral, sin historia) y discutir brevemente cada una:

- Determinismo: `suma(3, 4)` → siempre `7`
- Sin efecto colateral: evaluar `suma(3, 4)` no escribe en ningún log, no cambia ningún estado global
- Sin historia: `suma(3, 4)` no depende de cuántas veces se llamó antes

Cerrar con la idea central: *"Un programa funcional es un sistema de ecuaciones. No un guión de instrucciones."*

### Cómputo sin estado *(📽 F-10)* (5 min)

Contrastar los dos modelos en el pizarrón — dibujar rápido:

```
Imperativo:  estado₀ → instrucción₁ → estado₁ → instrucción₂ → estado₂ → ...
Funcional:   expresión₀ → reducción → expresión₁ → reducción → valor final
```

Presentar la **transparencia referencial** como la propiedad clave:
- *"Si `f(x) = y` hoy, entonces `f(x) = y` siempre. Podemos sustituir `f(x)` por `y` en cualquier parte del programa sin cambiar el comportamiento."*
- Preguntar: *"¿Por qué es poderoso esto? Porque podemos razonar sobre el programa como una ecuación matemática. Podemos probarlo, reusarlo, paralelizarlo."*

### Funciones puras vs. impuras *(📽 F-11)* (5 min)

Ir a la filmina con los tres ejemplos de TypeScript. Para cada uno, pedir a alguien del aula que clasifique antes de revelar la respuesta:

1. `const suma = (a, b) => a + b` — pedir clasificación. Correcta: pura.
2. `const getSaldo = () => bancoDB.query("saldo")` — impura: depende de estado externo.
3. `const log = (msg) => console.log(msg)` — impura: tiene efecto colateral de escritura.

Cerrar con el diagrama mental del "núcleo funcional puro":
> *"El truco es que los efectos siguen existiendo. El I/O existe, la base de datos existe. Lo que hacemos es empujarlos al borde del sistema — el núcleo de la lógica es puro y testeable."*

### Inmutabilidad: no hay variables, hay bindings *(📽 F-12)* (5 min)

Contrastar en vivo el código del pizarrón:

```
Imperativo: x = 5; x = x + 1;  // misma celda, dos valores
Funcional:  val x = 5           // un nombre, un valor, para siempre
```

Conectar explícitamente con TypeScript: `const` en TypeScript es la implementación de esta idea. No es una optimización — es una declaración de intención.

Plantear la pregunta para el debate breve:
> *"Si todo es inmutable, ¿cómo hacemos para 'modificar' algo? Por ejemplo, ¿agregar un elemento a una lista?"*

Dejar que intenten responder antes de mostrar el spread `[...nums, 4]` en el Bloque 2.

---

## BLOQUE 2 — TypeScript funcional: funciones como valores (20 min)

> 📽 **Filminas de este bloque:** F-13 · F-14 · F-15 · F-16 · F-17

**Objetivo:** pasar de los conceptos al código real en TypeScript con restricción funcional.

**Instrucción explícita al aula antes de este bloque:**
> *"A partir de ahora, si escribo `let` o hago un `push()`, me llaman la atención. Estamos en modo funcional puro."*

### Funciones como ciudadanos de primera clase *(📽 F-13)* (5 min)

Demo en vivo en TypeScript Playground. Escribir en tiempo real:

```typescript
const duplicar = (n: number): number => n * 2;

// ¿Puedo guardar una función en una variable?
const operacion: (x: number) => number = duplicar;

// ¿Puedo pasar una función como argumento?
const aplicar = (f: (x: number) => number, valor: number): number => f(valor);
console.log(aplicar(duplicar, 5));  // 10
```

Pausar en el tipo `(x: number) => number` — señalar que TypeScript hace ciudadanas de primera clase a las funciones *en el sistema de tipos*, no solo en la práctica.

Pedir al aula: *"¿Alguien puede decirme qué imprimiría `aplicar(n => n * n, 4)`?"* — 16.

### Inmutabilidad en TypeScript: `readonly` *(📽 F-14)* (5 min)

Continuar en el Playground:

```typescript
type Punto = {
  readonly x: number;
  readonly y: number;
};

const p: Punto = { x: 3, y: 4 };
// p.x = 10;  // <-- Escribir esto y mostrar el error de TypeScript en tiempo real
```

Hacer el experimento en vivo — que el error del compilador sea visible en la pantalla.

Luego mostrar `ReadonlyArray` y el patrón de transformación:

```typescript
const nums: ReadonlyArray<number> = [1, 2, 3];
// nums.push(4);  // error
const nuevoNums = [...nums, 4];  // ✓ — nueva colección
```

Responder la pregunta que quedó abierta en el bloque anterior: así "modificamos" en el funcional — creando nuevo valor, no mutando.

### Contraste en Clojure *(📽 F-15)* (2 min, rápido)

Abrir Clojure REPL y ejecutar:

```clojure
(def nums [1 2 3])
(conj nums 4)
nums  ; => sigue siendo [1 2 3]
```

Señalar la diferencia filosófica: en TypeScript elegimos no mutar; en Clojure no podemos aunque quisiéramos.

### Arrow functions y closures *(📽 F-16)* (5 min)

Demo en vivo:

```typescript
const crearSumador = (n: number) => (x: number) => x + n;
const sumar5 = crearSumador(5);
console.log(sumar5(3));   // 8
console.log(sumar5(10));  // 15
```

Explicar slowmotion qué pasa:
1. `crearSumador(5)` retorna una función nueva — *no un número*
2. Esa función recuerda que `n = 5` aunque `crearSumador` ya terminó de ejecutarse
3. Eso es una clausura: la función cerró sobre el entorno donde fue creada

Preguntar: *"¿`sumar5` tiene estado? Hay un valor `5` ahí adentro..."*
Respuesta: no — el `5` es parte de la definición de la función, no un estado mutable. Es un binding.

### Contraste en Clojure *(📽 F-17)* (3 min)

Mostrar la equivalencia sintáctica en Clojure — hacer énfasis en que la semántica es idéntica:

```clojure
(defn crear-sumador [n]
  (fn [x] (+ x n)))

(def sumar5 (crear-sumador 5))
(sumar5 3)  ; => 8
```

*"La sintaxis cambia. La idea de capturar el entorno léxico es igual."*

---

## BLOQUE 3 — Funciones de Orden Superior: map, filter, reduce (30 min)

> 📽 **Filminas de este bloque:** F-18 · F-19 · F-20 · F-21 · F-22

**Objetivo:** dominar las tres HOF fundamentales. Este es el núcleo práctico de la clase.

### ¿Qué es una HOF? *(📽 F-18)* (3 min)

Plantear el concepto brevemente con el contexto del λ-cálculo:

> *"En el λ-cálculo, las funciones siempre fueron de orden superior — no había otra forma. En la Máquina de Turing, las funciones eran procedimientos: no se pasaban ni devolvían. Esto marca la diferencia cultural entre los dos paradigmas."*

Presentar las tres HOF como el toolkit mínimo. Anticipar: van a ver las tres en demos.

### `map` *(📽 F-19)* (7 min)

Demo progresiva:

```typescript
const nums: ReadonlyArray<number> = [1, 2, 3, 4, 5];

// Paso 1: lambda inline
const dobles = nums.map(n => n * 2);
// => [2, 4, 6, 8, 10]

// Paso 2: función nombrada pasada como argumento
const esPar = (n: number): boolean => n % 2 === 0;
const sonPares = nums.map(esPar);
// => [false, true, false, true, false]
```

Señalar el tipo polimórfico de `map`: recibe `A[]`, devuelve `B[]` — puede cambiar el tipo del elemento.

Hacer el contraste en Clojure REPL: `(map #(* % 2) [1 2 3 4 5])`.

Preguntar: *"¿Cuántas veces pasaría el elemento [1,2,3,4,5] por el cuerpo del `map`?"* — 5 veces, para cada elemento.

### `filter` *(📽 F-20)* (7 min)

Demo con el ejemplo del catálogo:

```typescript
type Producto = { readonly nombre: string; readonly precio: number };
const catalogo: ReadonlyArray<Producto> = [
  { nombre: "Laptop",  precio: 1200 },
  { nombre: "Mouse",   precio: 25 },
  { nombre: "Monitor", precio: 400 },
];

const económicos = catalogo.filter(p => p.precio < 100);
```

Ejecutar en tiempo real — mostrar el resultado antes de escribirlo en el comentario.

Preguntar: *"¿Qué tipo devuelve `filter` en relación al tipo de entrada?"* — mismo tipo. `filter` no transforma, solo selecciona.

Contrastar con `map`: `map` puede cambiar el tipo del elemento; `filter` siempre devuelve elementos del mismo tipo.

### `reduce` *(📽 F-21)* (8 min)

`reduce` merece más tiempo — es la más poderosa y la más confusa al principio.

Arrancar con el ejemplo simple de suma:

```typescript
const nums = [1, 2, 3, 4, 5];
const suma = nums.reduce((acc, n) => acc + n, 0);
```

Hacer el trace en el pizarrón paso a paso:
```
acc=0, n=1 → acc=1
acc=1, n=2 → acc=3
acc=3, n=3 → acc=6
acc=6, n=4 → acc=10
acc=10, n=5 → acc=15
```

Luego mostrar el ejemplo más potente (conteo de ocurrencias) que devuelve un tipo diferente al input:

```typescript
const letras = ["a", "b", "a", "c", "b", "a"];
const conteo = letras.reduce<Record<string, number>>(
  (acc, letra) => ({ ...acc, [letra]: (acc[letra] ?? 0) + 1 }),
  {}
);
// => { a: 3, b: 2, c: 1 }
```

Señalar: *"`reduce` puede producir cualquier tipo. Es la más general — y por eso la más poderosa."*

### El pipeline funcional *(📽 F-22)* (5 min)

Demo en vivo del pipeline encadenado: filter → map → reduce sobre el catálogo.

```typescript
const totalEconómicos = catalogo
  .filter(p => p.precio < 100)
  .map(p => p.precio)
  .reduce((acc, precio) => acc + precio, 0);
```

Ejecutar y mostrar el resultado: 105.

Mostrar la versión Clojure con el thread-last macro `->>`:

```clojure
(->> catalogo
     (filter #(< (:precio %) 100))
     (map :precio)
     (reduce + 0))
```

Hacer la observación de cierre del bloque:
> *"Comparar esto con el equivalente imperativo: un `for`, una variable acumuladora `total`, reasignaciones... Esta versión no tiene ninguna de esas cosas. Cada línea dice QUÉ hacer con los datos, no CÓMO iterar."*

---

## BLOQUE 4 — Clausuras, ámbito léxico y recursión (15 min)

> 📽 **Filminas de este bloque:** F-23 · F-24 · F-25

**Objetivo:** cerrar los mecanismos de control fundamentales del paradigma.

### Fábricas de funciones *(📽 F-23)* (5 min)

Demo en vivo:

```typescript
const crearMultiplicador = (factor: number) =>
  (x: number): number => x * factor;

const triple  = crearMultiplicador(3);
const décuplo = crearMultiplicador(10);

[1, 2, 3].map(triple);   // [3, 6, 9]
[1, 2, 3].map(décuplo);  // [10, 20, 30]
```

El punto pedagógico: `triple` es una función que *recuerda* que `factor = 3`. Se puede pasar a `map` directamente.

Hacer la observación sobre scope léxico vs. dinámico — sin profundizar demasiado:
> *"En lenguajes con scope dinámico, lo que `triple` recuerda depende de *desde dónde la llamás*. Con scope léxico, lo que recuerda depende de *dónde fue definida*. Scope léxico = predecible."*

Mencionar que la composición de `triple` y `décuplo` en una sola función viene en T04.

### Recursión como mecanismo de iteración *(📽 F-24)* (5 min)

Recordar la premisa: en el paradigma puro no hay `for`, no hay `while`.

Demo en tiempo real:

```typescript
const factorial = (n: number): number =>
  n <= 1 ? 1 : n * factorial(n - 1);

console.log(factorial(5));  // 120
```

Hacer el trace breve en el pizarrón: `factorial(3) = 3 * factorial(2) = 3 * 2 * factorial(1) = 3 * 2 * 1 = 6`.

Conectar explícitamente con el λ-cálculo:
> *"Esto es literalmente la reducción β del λ-cálculo que vimos en la filmina F-06. La función se sustituye por su cuerpo, el argumento reemplaza el parámetro, el proceso se repite. Sin estado, sin asignación."*

Mostrar el mismo en Clojure.

### Tail recursion *(📽 F-25)* (5 min)

Plantear el problema:

> *"¿Qué pasa con `factorial(10000)`? La pila de llamadas explota."*

Demostrar el patrón con acumulador:

```typescript
const factAux = (n: number, acc: number): number =>
  n <= 1 ? acc : factAux(n - 1, n * acc);

const factorial = (n: number): number => factAux(n, 1);
```

Hacer el trace con acumulador: la última operación es siempre la llamada recursiva — no hay más cómputo pendiente.

Mostrar `recur` en Clojure como el mecanismo garantizado de TCO.

Dar la advertencia honesta sobre JS/TS: *"El runtime de JavaScript no garantiza TCO optimizado. En producción con recursión profunda, se usa trampolín o iteración equivalente. Pero el patrón conceptual es correcto y vale la pena entenderlo."*

---

## BLOQUE IA — IA Generativa y el Paradigma Funcional (10 min)

> 📽 **Filminas de este bloque:** F-26 · F-27

**Objetivo:** conectar el paradigma funcional con la realidad del desarrollo asistido por IA.

### Funcional como lenguaje de especificación *(📽 F-26)* (5 min)

Arrancar con la cita de Schmidt & Runfola y conectarla con lo que vieron hoy:

> *"El pensamiento computacional no es saber sintaxis — es la capacidad de descomponer problemas en transformaciones precisas sobre datos. Eso es exactamente lo que hace el paradigma funcional."*

Demo en vivo con asistente de IA (GitHub Copilot o Claude en el chat):

Formular la misma tarea de dos formas:
1. *"Escribí código que itere sobre un array de productos, filtre los que tengan precio menor a 100, y sume sus precios."* — observar el código devuelto (probablemente imperativo con `for`)
2. *"Escribí en TypeScript funcional puro: `catalogo.filter(...).map(...).reduce(...)` para obtener el total de productos económicos."* — observar el código devuelto (más limpio, más directo)

La diferencia no es solo estética — la segunda especificación es más difícil de malentender.

### Auditar código generado *(📽 F-27)* (5 min)

Mostrar el ejemplo del código "con aspecto funcional" que en realidad muta:

```typescript
// ❌ La IA generó esto — parece funcional, no lo es
const procesarLista = (items: string[]): string[] => {
  const resultado: string[] = [];
  items.forEach(item => resultado.push(item.toUpperCase())); // mutación oculta
  return resultado;
};
```

Pedir al aula que identifique el problema antes de revelarlo.

Mostrar la versión correcta:

```typescript
// ✅ Funcional real
const procesarLista = (items: ReadonlyArray<string>): ReadonlyArray<string> =>
  items.map(item => item.toUpperCase());
```

Recorrer el checklist de auditoría:
- [ ] ¿Solo `const`?
- [ ] ¿Hay `push`, `pop`, `splice`?
- [ ] ¿Los tipos reflejan inmutabilidad (`ReadonlyArray`)?

Conclusión: *"Saber el paradigma no es un lujo académico. Es la capacidad de leer lo que la IA genera y detectar cuándo miente."*

---

## CIERRE — Resumen y adelanto T04 (5 min)

> 📽 **Filminas de este bloque:** F-28

### Resumen visual *(📽 F-28)* (3 min)

Recorrer la tabla de resumen en la filmina. Pedir a alguien del aula que complete una fila antes de mostrarla — activación de cierre.

### Adelanto T04 (1 min)

> *"Hoy tenemos las piezas. En T04 aprendemos a ensamblarlas: composición de funciones, aplicación parcial y currificación. Con esas herramientas, los pipelines que vieron hoy se vuelven construcciones reutilizables."*

### Pregunta para reflexión asincrónica (1 min)

Escribir en el pizarrón (o mostrar en filmina):

> *"¿Cuándo NO usarías estilo funcional en un proyecto real de TypeScript?"*

Dejar que haya dos o tres respuestas cortas — 30 segundos cada una. No hay respuesta correcta; el objetivo es que empiecen a pensar los límites del paradigma antes de T04.

---

## Snippets de Demo — Para copiar durante la clase

### Bloque 2: ciudadanos de primera clase
```typescript
const duplicar = (n: number): number => n * 2;
const aplicar = (f: (x: number) => number, valor: number): number => f(valor);
console.log(aplicar(duplicar, 5));         // 10
console.log(aplicar(n => n * n, 4));       // 16
```

### Bloque 2: readonly
```typescript
type Punto = { readonly x: number; readonly y: number };
const p: Punto = { x: 3, y: 4 };
const nums: ReadonlyArray<number> = [1, 2, 3];
const nuevoNums = [...nums, 4];
```

### Bloque 2: closures
```typescript
const crearSumador = (n: number) => (x: number) => x + n;
const sumar5 = crearSumador(5);
console.log(sumar5(3));   // 8
console.log(sumar5(10));  // 15
```

### Bloque 3: pipeline completo
```typescript
type Producto = { readonly nombre: string; readonly precio: number };
const catalogo: ReadonlyArray<Producto> = [
  { nombre: "Laptop",  precio: 1200 },
  { nombre: "Mouse",   precio: 25 },
  { nombre: "Teclado", precio: 80 },
  { nombre: "Monitor", precio: 400 },
];
const totalEconómicos = catalogo
  .filter(p => p.precio < 100)
  .map(p => p.precio)
  .reduce((acc, precio) => acc + precio, 0);
console.log(totalEconómicos);  // 105
```

### Bloque 4: recursión
```typescript
const factorial = (n: number): number =>
  n <= 1 ? 1 : n * factorial(n - 1);

const factAux = (n: number, acc: number): number =>
  n <= 1 ? acc : factAux(n - 1, n * acc);
const factorialTCO = (n: number): number => factAux(n, 1);
```

### Bloque IA: trampa del código generado
```typescript
// ❌ Parece funcional — NO lo es
const procesarLista = (items: string[]): string[] => {
  const resultado: string[] = [];
  items.forEach(item => resultado.push(item.toUpperCase()));
  return resultado;
};

// ✅ Funcional real
const procesarListaOk = (items: ReadonlyArray<string>): ReadonlyArray<string> =>
  items.map(item => item.toUpperCase());
```
