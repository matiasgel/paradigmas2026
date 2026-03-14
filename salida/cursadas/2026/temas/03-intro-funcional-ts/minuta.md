# Minuta de Clase — Tema 03: Introducción a Programación Funcional con TypeScript

> **Estado:** BORRADOR — pendiente de revisión del docente
> **Agente:** Dr. Roberto ✍️ (class-writer)
> **Fecha de generación:** 2026-03-13
> **Duración total:** 120 minutos (constraint absoluto)
> **Clase:** 1 de 1 — Semana 2
> **Perfil docente:** profesor-teorico
> **Lenguaje principal:** TypeScript (contraste Haskell — solo lectura)
> **Workflow:** topic-cycle / Step 4
> **Input:** `temas/03-intro-funcional-ts/diseno.md`

---

## Datos de la clase

| Campo | Valor |
|-------|-------|
| Materia | Paradigmas y Lenguajes de Programación 2026 |
| Institución | Universidad Nacional de Tierra del Fuego — Instituto IDEI |
| Tema Nº | 03 |
| Nombre del tema | Introducción a Programación Funcional con TypeScript |
| Semana | 2 |
| Clase | 1 de 1 |
| Duración | 120 minutos |
| Plan mínimo | Contenidos #8 (Paradigma funcional) |

---

## Pregunta motivadora de apertura

> *"Tenemos dos versiones del mismo código que calculan promedios: una con bucles y variables mutables, otra con `map`, `filter` y `reduce`. ¿Cuál preferís? ¿Por qué? ¿Importa?"*

Esta pregunta establece el arco de la clase: de la intuición hacia los principios formales del paradigma funcional, y del código "lindo" hacia el código que es *correcto por construcción*.

---

## Bloque 1 — Arranque y motivación (10 min)

### Objetivo
Crear tensión cognitiva entre el estilo imperativo ya conocido y el funcional. Motivar el paradigma desde sus ventajas prácticas.

### Desarrollo narrativo

**Hook de continuidad con Tema 01:**
> *"En el Tema 01 vimos que TypeScript es multiparadigma. Hoy exploramos uno de esos paradigmas en profundidad: el funcional. No como una 'forma alternativa de escribir lo mismo', sino como un modelo de cómputo diferente."*

**Mini-caso de apertura — dos versiones:**

```typescript
// Versión imperativa
function promedioPositivos(nums: number[]): number {
  let suma = 0;
  let cantidad = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) {
      suma += nums[i];
      cantidad++;
    }
  }
  return cantidad === 0 ? 0 : suma / cantidad;
}

// Versión funcional pura — solo expresiones, sin if
const promedioPositivos = (nums: number[]): number => {
  const positivos = nums.filter(n => n > 0);
  return positivos.length === 0
    ? 0
    : positivos.reduce((acc, n) => acc + n, 0) / positivos.length;
};

// 💡 Expresión vs sentencia: el operador ternario `? :` es una *expresión* (tiene valor).
// `if` es una *sentencia* (ejecuta acciones). En funcional puro, preferimos expresiones.
```

**Preguntas para el aula:**
- ¿Cuál es más fácil de leer?
- ¿Cuál es más fácil de testear?
- ¿Cuál tiene menos lugares donde puede fallar?

El objetivo no es dar la respuesta todavía — es generar curiosidad sobre *por qué* la versión funcional tiene ciertas propiedades.

**Contexto histórico brevísimo (2 min):**
- El paradigma funcional es tan viejo como el imperativo: el λ-cálculo (Alonzo Church, 1930s) es previo a la Máquina de Turing.
- LISP (1958) fue el primer lenguaje inspirado en funciones matemáticas puras.
- Haskell, ML, Erlang: lenguajes funcionales puros.
- JavaScript, TypeScript, Python, Java, Kotlin: lenguajes multiparadigma que adoptaron ideas funcionales.
- Hoy, la industria usa estas ideas constantemente (React, RxJS, monadic error handling, etc.).

---

## Bloque 2 — Fundamentos: funciones puras, inmutabilidad, recursión (20 min)

### Objetivo
Establecer los tres pilares conceptuales del paradigma. Que el alumno pueda identificar si una función es pura o no.

### 2.1 — Cómputo sin estado

**Paradigma imperativo**: el cómputo avanza modificando la memoria. El modelo es la Máquina de von Neumann.

**Paradigma funcional**: el cómputo avanza evaluando expresiones. No hay estado global — una expresión siempre denota el mismo valor en el mismo entorno.

> *"Functional languages, at least in their 'pure' form, do not use the concept of memory (and therefore there is no side effect). Once an environment is fixed, an expression always denotes the same value."*  
> — Gabbrielli & Martini, *Programming Languages: Principles and Paradigms*, Cap. 11

### 2.2 — Funciones puras

**Definición:** Una función es *pura* si:
1. Para los mismos argumentos, siempre devuelve el **mismo resultado**.
2. No produce efectos secundarios (no modifica estado global, no hace I/O, no depende de variables que pueden cambiar).

```typescript
// ✅ PURA — devuelve siempre el mismo resultado, sin efectos laterales
const doble = (n: number): number => n * 2;
double(5); // 10 — siempre
double(5); // 10 — siempre (2 minutos después, sigue siendo 10)

// ❌ IMPURA — el resultado depende de estado externo (puede cambiar entre llamadas)
let factor = 2;
const dobleExterno = (n: number): number => n * factor;

dobleExterno(5); // 10 (factor=2)
factor = 3;      // ← cambiamos factor
dobleExterno(5); // 15 (factor=3) — ¡diferente resultado con el MISMO argumento!
```

**Concepto clave:** La pureza se define por **el contrato de la función**, no solo por cómo la usamos en este momento. Si alguien *puede* cambiar las variables del entorno (variables globales, estado de objetos compartidos), la función es impura.

```typescript
// ❌ IMPURA — modifica estado externo (efecto secundario)
const nums: number[] = [];
const agregarYDoble = (n: number): number => {
  nums.push(n);   // ← modifica array global — efecto secundario
  return n * 2;
};
```

**¿Por qué importa?** Las funciones puras son:
- **Testeables**: no requieren mocks ni setup — `doble(5)` siempre vale `10`.
- **Componibles**: se pueden encadenar sin sorpresas.
- **Paralelizables**: sin estado compartido, no hay condiciones de carrera.
- **Memoizables**: el resultado puede cachearse de forma segura — si `doble(5)` = 10 hoy, valdrá 10 siempre.

### 2.3 — Inmutabilidad

En funcional, *no se modifica* — se crea una nueva versión del dato.

```typescript
// Imperativo — muta
const agregarItem = (arr: number[], item: number): void => {
  arr.push(item); // ← modifica el array original
};

// Funcional — no muta
const agregarItem = (arr: readonly number[], item: number): readonly number[] =>
  [...arr, item]; // ← retorna un nuevo array
```

**En TypeScript:** usar `readonly`, `as const`, el operador spread (`...`), y métodos que devuelven nuevos arrays (`map`, `filter`, `slice`) en lugar de mutaciones (`push`, `splice`, `sort`).

### 2.4 — Recursión como control de flujo

Sin estado mutable, los bucles (`for`, `while`) pierden sentido. El mecanismo de sustitución es la recursión.

```typescript
// Suma de array — estilo imperativo
const sumaImperativa = (nums: number[]): number => {
  let total = 0;
  for (const n of nums) total += n;
  return total;
};

// Suma de array — estilo recursivo
const sumaRecursiva = (nums: number[]): number =>
  nums.length === 0 ? 0 : nums[0] + sumaRecursiva(nums.slice(1));
```

**Limitación en JavaScript/TypeScript:** No hay optimización de recursión de cola (tail call optimization) en la mayoría de los engines V8. En Haskell y lenguajes funcionales puros esto está garantizado. Solución práctica: usar `reduce`.

---

## Bloque 3 — Funciones de orden superior y clausuras (30 min)

### Objetivo
Dominar el concepto de función como valor de primera clase. Implementar `map`, `filter`, `reduce` desde cero.

### 3.1 — Funciones como valores de primera clase

> En TypeScript (y JavaScript), las funciones son valores que pueden:
> - Guardarse en variables
> - Pasarse como argumentos
> - Retornarse como resultado

```typescript
// Función guardada en variable
const saludar = (nombre: string) => `Hola, ${nombre}!`;

// Función pasada como argumento
const aplicar = (fn: (x: number) => number, valor: number) => fn(valor);
console.log(aplicar(x => x * 2, 5)); // 10

// Función retornada como resultado (función generadora)
const multiplicadorPor = (factor: number) => (n: number) => n * factor;
const triple = multiplicadorPor(3);
console.log(triple(4)); // 12
```

### 3.2 — `map`, `filter`, `reduce` — las tres joyas funcionales

**`map`** — transforma cada elemento de un arreglo aplicando una función:

```typescript
// Implementación propia de map
const myMap = <A, B>(fn: (a: A) => B, arr: readonly A[]): B[] =>
  arr.length === 0 ? [] : [fn(arr[0]), ...myMap(fn, arr.slice(1))];

// O con reduce:
const myMap2 = <A, B>(fn: (a: A) => B, arr: readonly A[]): B[] =>
  arr.reduce<B[]>((acc, x) => [...acc, fn(x)], []);

// Uso nativo:
const cuadrados = [1, 2, 3, 4].map(n => n ** 2); // [1, 4, 9, 16]
```

**`filter`** — selecciona los elementos que cumplen un predicado:

```typescript
const myFilter = <A>(pred: (a: A) => boolean, arr: readonly A[]): A[] =>
  arr.reduce<A[]>((acc, x) => pred(x) ? [...acc, x] : acc, []);

const pares = [1, 2, 3, 4, 5, 6].filter(n => n % 2 === 0); // [2, 4, 6]
```

**`reduce` (fold)** — colapsa un arreglo en un valor acumulando con una función:

```typescript
const myReduce = <A, B>(fn: (acc: B, x: A) => B, init: B, arr: readonly A[]): B =>
  arr.length === 0 ? init : myReduce(fn, fn(init, arr[0]), arr.slice(1));

const suma = [1, 2, 3, 4].reduce((acc, n) => acc + n, 0); // 10
```

#### 🔧 Ejercicio guiado en clase (10 min)

> *"Implementen en parejas una función `frecuencias` que tome un arreglo de strings y devuelva un objeto con cuántas veces aparece cada string. Solo usando `reduce` — sin bucles."*

```typescript
const frecuencias = (palabras: readonly string[]): Record<string, number> =>
  palabras.reduce<Record<string, number>>(
    (acc, palabra) => ({ ...acc, [palabra]: (acc[palabra] ?? 0) + 1 }),
    {}
  );

frecuencias(["hola", "mundo", "hola", "TS"]); // { hola: 2, mundo: 1, TS: 1 }
```

### 3.3 — Clausuras y ámbito léxico

Una **clausura** (*closure*) captura las variables del entorno donde fue definida, incluso después de que ese entorno ya no existe en el stack.

```typescript
const crearContador = (inicio = 0) => {
  let cuenta = inicio; // capturado en la clausura
  return {
    incrementar: () => ++cuenta,
    valor: () => cuenta,
  };
};

const c = crearContador(10);
c.incrementar(); // 11
c.incrementar(); // 12
c.valor();       // 12
```

> **Nota:** Este `crearContador` *no es puro* (tiene estado mutable interno). Es un ejemplo de cómo las clausuras se usan fuera del paradigma funcional estricto. En funcional puro, el estado se pasa como argumento.

---

## Bloque 4 — Composición, aplicación parcial y currificación (20 min)

### Objetivo
Construir pipelines de transformación. Entender la currificación como mecanismo de aplicación parcial.

### 4.1 — Composición de funciones

> *"Componer es la operación fundamental del paradigma: f ∘ g significa aplicar g primero y luego f."*

```typescript
// compose: de derecha a izquierda (matemática estándar)
const compose = <A, B, C>(f: (b: B) => C, g: (a: A) => B) => (a: A): C => f(g(a));

// pipe: de izquierda a derecha (más legible en código)
const pipe = <A, B, C>(g: (a: A) => B, f: (b: B) => C) => (a: A): C => f(g(a));

// Ejemplo práctico — pipeline de transformación de texto:
const limpiarEspacios = (s: string) => s.trim();
const aMayusculas = (s: string) => s.toUpperCase();
const agregarExclamacion = (s: string) => `${s}!`;

const gritar = pipe(pipe(limpiarEspacios, aMayusculas), agregarExclamacion);
gritar("  hola mundo  "); // "HOLA MUNDO!"
```

### 4.2 — Aplicación parcial y currificación

**Aplicación parcial:** dada una función de N argumentos, fijar K de ellos y obtener una función de N-K argumentos.

**Currificación:** transformar una función de múltiples argumentos en una cadena de funciones de un argumento.

#### Paso 1 — Función binaria tradicional

```typescript
const add = (a: number, b: number) => a + b;
add(5, 3);  // 8
```

#### Paso 2 — Separar los argumentos manualmente (forma explícita)

```typescript
// La función interna también es arrow — mantenemos estilo expresivo
const addStep = (a: number) => (b: number) => a + b;

const add5 = addStep(5);  // ← retorna una FUNCIÓN: (b: number) => a + b
console.log(add5);        // [Function (anonymous)]
add5(3);                  // 8 — ahora aplicamos la segunda parte
```

> **Cómo leerlo:** `addStep` es una función que toma `a` y *devuelve otra función* que toma `b`.
> `addStep(5)` devuelve `(b: number) => 5 + b`. Solo cuando ejecutamos `add5(3)` se completa el cómputo.

**Concepto clave:** `addStep(5)` NO devuelve `8`. Devuelve **una función que espera `b`**. Solo cuando hacemos `add5(3)` se ejecuta la adición.

#### Paso 3 — Versión currificada compacta (arrow functions)

```typescript
const addCurried = (a: number) => (b: number) => a + b;

const add5 = addCurried(5);
add5(3);  // 8
add5(10); // 15

// Uso en pipelines:
const nums = [1, 2, 3, 4, 5];
const resultado = nums.map(addCurried(10)); // [11, 12, 13, 14, 15]
```

**Lectura de tipos en IDE:** Si posicionás el cursor en `add5` en TypeScript, verás: `add5: (b: number) => number` — es decir, `add5` es una función que toma un `b` y retorna un número. Eso confirma que una currificación devuelve funciones, no resultados directos.

#### 🔧 Ejercicio rápido (5 min)

> *"Con `pipe`, construyan un pipeline que: (1) filtre los números pares de un array, (2) los multiplique por 3, (3) los sume. ¿Qué ventajas tiene frente a escribirlo en una sola función?"*

---

## Bloque 5 — Manejo de efectos y evaluación perezosa (10 min)

### Objetivo
Entender la frontera entre el mundo puro y los efectos. Ver un ejemplo mínimo de evaluación perezosa con generadores.

### 5.1 — La frontera de la pureza

Un programa real necesita I/O: leer archivos, llamar APIs, escribir en pantalla. La estrategia funcional es *aislar* los efectos:

```
┌─────────────────────────────────────────────────┐
│                   MUNDO IMPURO                  │
│   Leer input → [efecto]  [efecto] → Escribir    │
│                    ↓           ↑                │
│               MUNDO PURO                        │
│   Transformaciones puras sobre los datos        │
└─────────────────────────────────────────────────┘
```

**Principio:** empujar los efectos hacia los bordes del sistema. El núcleo del programa es puro y testeable.

### 5.2 — Evaluación perezosa con generadores

En JavaScript/TypeScript, los generadores permiten crear pipelines *lazy*: los valores se producen solo cuando se consumen.

```typescript
// Caso especial: function* no tiene sintaxis arrow — es la única excepción al estilo expresivo.
// El estado interno (n) es puramente local e invisible para el exterior.
function* naturales(): Generator<number> {
  let n = 0;
  while (true) yield n++;
}

// const arrow: consumir un generador con for-of es el único mecanismo idiomático en TS/JS.
const tomar = <T>(n: number, gen: Generator<T>): T[] => {
  const resultado: T[] = [];
  for (const valor of gen) {
    resultado.push(valor);
    if (resultado.length >= n) break;
  }
  return resultado;
};

tomar(5, naturales()); // [0, 1, 2, 3, 4]
```

> **Nota:** En Haskell, *toda* la evaluación es perezosa por defecto. En TypeScript es opt-in (generadores). Este patrón es poderoso para procesar streams de datos sin cargar todo en memoria.

---

## Bloque 6 — Introducción a mónadas (20 min)

### Objetivo
Intuición de mónada como patrón para encadenar cálculos con contexto. Ver `Maybe`/`Either` en TypeScript.

### 6.1 — El problema que resuelven las mónadas

En muchos lenguajes, manejar opcionalidad y errores requiere verificaciones constantes:

```typescript
// ❌ Estilo imperativo — verificación en cada paso
const usuario = obtenerUsuario(1);
if (!usuario) {
  console.error("Usuario no existe");
}

const direccion = usuario?.direccion; // ← vuelvo a verificar
if (!direccion) {
  console.error("No tiene dirección");
}

const ciudad = direccion?.ciudad;     // ← y otra vez
if (!ciudad) {
  console.error("No tiene ciudad");
}

const resultado = ciudad?.toUpperCase(); // ← y una más
console.log(resultado);
```

O el temido null pointer exception (si olvidás una verificación):

```typescript
// ❌ Fácil de olvidar — crash esperando suceder
const obtenerCiudad = (usuario: any) =>
  usuario.direccion.ciudad.toUpperCase();

// Si usuario == null → TypeError no capturado
```

Las **mónadas** son un patrón para encadenar operaciones que pueden fallar **sin verificar manualmente en cada paso**. El contexto (presente/ausente, éxito/error, etc.) se propaga automáticamente.

### 6.2 — Maybe / Option

```typescript
// Tipo Option — representa un valor que puede o no existir
type Option<A> = { tag: "some"; value: A } | { tag: "none" };

const some = <A>(value: A): Option<A> => ({ tag: "some", value });
const none = <A>(): Option<A> => ({ tag: "none" });

// map — transforma el valor si existe
const mapOption = <A, B>(fn: (a: A) => B, opt: Option<A>): Option<B> =>
  opt.tag === "some" ? some(fn(opt.value)) : none();

// flatMap (bind) — encadena operaciones que pueden fallar
const flatMapOption = <A, B>(fn: (a: A) => Option<B>, opt: Option<A>): Option<B> =>
  opt.tag === "some" ? fn(opt.value) : none();

// Ejemplo: pipeline seguro
const obtenerUsuario = (id: number): Option<{ nombre: string; edad: number }> =>
  id === 1 ? some({ nombre: "Ana", edad: 22 }) : none();

const obtenerNombre = (u: { nombre: string }) => some(u.nombre.toUpperCase());

const resultado = flatMapOption(obtenerNombre, obtenerUsuario(1));
// { tag: "some", value: "ANA" }
const vacio = flatMapOption(obtenerNombre, obtenerUsuario(99));
// { tag: "none" }
```

### 6.3 — Either — mónada de error

```typescript
type Either<E, A> = { tag: "left"; error: E } | { tag: "right"; value: A };

const left = <E>(error: E): Either<E, never> => ({ tag: "left", error });
const right = <A>(value: A): Either<never, A> => ({ tag: "right", value });

// Uso: parsear un número de forma segura
const parsearNumero = (s: string): Either<string, number> => {
  const n = Number(s);
  return isNaN(n) ? left(`"${s}" no es un número válido`) : right(n);
};

parsearNumero("42");   // { tag: "right", value: 42 }
parsearNumero("abc");  // { tag: "left", error: '"abc" no es un número válido' }
```

### 6.4 — Promise como mónada

> *"Ya usan mónadas sin saberlo. `Promise` en JavaScript es una mónada: `.then()` es `flatMap`."*

```typescript
fetch("/api/usuario")
  .then(res => res.json())        // flatMap: si falla, los .then siguientes se saltan
  .then(data => data.nombre)
  .catch(err => console.error(err));
```

> **Nota:** Profundizaremos en mónadas en el **Tema 05**. Por ahora, la intuición es suficiente: mónada = patrón para encadenar cálculos con contexto (opcional, error, async, etc.).

---

## Bloque 7 — Cierre y conexión (10 min)

### Recapitulación

| Concepto | Definición en 1 línea |
|----------|----------------------|
| **Función pura** | Mismo input → mismo output, sin efectos laterales |
| **Inmutabilidad** | No se modifica el dato, se crea uno nuevo |
| **Recursión** | Control de flujo sin estado mutable |
| **HOF** | Funciones que reciben o retornan funciones |
| **Clausura** | Función que captura su entorno léxico |
| **Composición** | Pipe de transformaciones pequeñas y puras |
| **Currificación** | Funciones de un argumento encadenadas |
| **Mónada** | Patrón para encadenar cómputos con contexto |

### Conexión con próximos temas

- **Tema 04 — Aspectos avanzados de programación funcional**: pattern matching, functores, composición avanzada, programación funcional reactiva.
- **Tema 05 — Mónadas en TypeScript**: `Maybe`, `Either`, `IO`, `Task` — en profundidad.
- **Tema 06 — Funcional en Python**: cómo Python adoptó estas ideas (y sus limitaciones).

### Pregunta de cierre (reflexión rápida)

> *"¿Qué cambiarías en el código que escribís habitualmente si adoptaras solo uno de los principios que vimos hoy? Escribí en un papel o en el chat: un principio y una situación concreta donde lo aplicarías."*

---

## Notas del docente

- **Bloque 3 (HOF)**: el ejercicio de `frecuencias` con `reduce` suele sorprender gratamente — muchos alumnos no habían pensado que `reduce` podía construir objetos. Dejar tiempo para que lo resuelvan y discutirlo.
- **Bloque 6 (Mónadas)**: no entrar en teoría categórica. La intuición de "caja con reglas" alcanza para este tema.
- **TypeScript vs Kotlin/Haskell**: en el Tema 01 usaste TypeScript. Haskell aparece solo como contraste conceptual (lenguaje funcional puro). No instalar Haskell.
- **Eje IA (puede adaptarse según tiempo)**: mostrar cómo `Array.prototype.map` en JS es análogo al `fmap` de Haskell, y cómo frameworks de IA/ML (LangChain, etc.) usan pipelines funcionales para encadenar pasos de procesamiento.
