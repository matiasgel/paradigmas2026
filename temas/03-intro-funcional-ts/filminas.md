# Filminas — Tema 03: Introducción a Programación Funcional con TypeScript

> **Estado:** BORRADOR — pendiente de revisión del docente
> **Agente:** Dr. Roberto ✍️ (class-writer)
> **Fecha de generación:** 2026-03-13
> **Duración total:** 120 minutos (constraint absoluto)
> **Clase:** 1 de 1 — Semana 2
> **Perfil docente:** profesor-teorico
> **Lenguaje principal:** TypeScript (contraste Haskell — solo lectura)
> **Workflow:** topic-cycle / Step 4

---

<!-- ============================================================ -->
## SLIDE 01 — Portada
<!-- ============================================================ -->

# Introducción a la Programación Funcional

**con TypeScript**

**Paradigmas y Lenguajes de Programación — 2026**
Universidad Nacional de Tierra del Fuego — Instituto IDEI

> *"¿Por qué escribir funciones que no cambian el mundo?  
> Porque ese código es el más fácil de razonar, testear y reutilizar."*

---

<!-- ============================================================ -->
## SLIDE 02 — Agenda
<!-- ============================================================ -->

## Agenda de la clase

| Bloque | Min | Tema |
|--------|-----|------|
| 1 | 10 | Motivación y contexto histórico |
| 2 | 20 | Funciones puras, inmutabilidad, recursión |
| 3 | 30 | Funciones de orden superior y clausuras |
| 4 | 20 | Composición, aplicación parcial, currificación |
| 5 | 10 | Manejo de efectos y evaluación perezosa |
| 6 | 20 | Introducción a mónadas |
| 7 | 10 | Cierre y conexión con próximos temas |

**Total: 120 minutos**

---

<!-- ============================================================ -->
## BLOQUE 1 — MOTIVACIÓN (10 min)
<!-- ============================================================ -->

<!-- SLIDE 03 -->
## SLIDE 03 — El mismo problema, dos estilos

## ¿Cuál preferís?

```typescript
// Imperativo
function promedioPositivos(nums: number[]): number {
  let suma = 0; let cantidad = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) { suma += nums[i]; cantidad++; }
  }
  return cantidad === 0 ? 0 : suma / cantidad;
}
```

```typescript
// Funcional
const promedioPositivos = (nums: number[]): number => {
  const positivos = nums.filter(n => n > 0);
  if (positivos.length === 0) return 0;
  return positivos.reduce((acc, n) => acc + n, 0) / positivos.length;
};
```

> ❓ ¿Cuál es más legible? ¿Cuál es más fácil de testear? ¿Cuál tiene menos lugares donde puede fallar?

---

<!-- SLIDE 04 -->
## SLIDE 04 — Contexto histórico

## El paradigma funcional: tan antiguo como el imperativo

```
1930s — λ-cálculo (Church)    ← base teórica del funcional
1940s — Máquina de Turing     ← base del imperativo
1958  — LISP                  ← primer lenguaje funcional
1990  — Haskell               ← funcional puro moderno
2000s — F#, Scala, Clojure
2010s — JS/TS, Python, Java adoptan ideas funcionales
2020s — React, RxJS, monadic error handling en producción
```

> 🔑 **Hoy**: no hay un lenguaje funcional "de industria" dominante, pero **los principios están en todas partes**.

---

<!-- ============================================================ -->
## BLOQUE 2 — FUNDAMENTOS (20 min)
<!-- ============================================================ -->

<!-- SLIDE 05 -->
## SLIDE 05 — Cómputo sin estado

## Imperativo vs Funcional

| Imperativo | Funcional |
|------------|-----------|
| Cómputo = modificar memoria | Cómputo = evaluar expresiones |
| Variables mutables | Valores inmutables |
| Bucles (`for`, `while`) | Recursión + HOF |
| Efectos secundarios explícitos | Sin efectos (o aislados) |
| Modelo: Máquina de von Neumann | Modelo: λ-cálculo |

> *"Once an environment is fixed, an expression always denotes the same value."*  
> — Gabbrielli & Martini, Cap. 11

---

<!-- SLIDE 06 -->
## SLIDE 06 — Funciones puras

## ¿Qué es una función pura?

**Una función es pura si:**
1. Para los mismos argumentos → **siempre el mismo resultado**
2. **No modifica** nada fuera de su scope (sin efectos secundarios)

```typescript
// ✅ PURA
const doble = (n: number): number => n * 2;

// ❌ IMPURA — depende de estado externo
let factor = 2;
const dobleImpura = (n: number) => n * factor;

// ❌ IMPURA — modifica estado externo
const nums: number[] = [];
const agregarYDoble = (n: number) => {
  nums.push(n); // efecto secundario
  return n * 2;
};
```

> 🎯 **Las funciones puras son testeables, componibles y paralelizables**

---

<!-- SLIDE 07 -->
## SLIDE 07 — Inmutabilidad en TypeScript

## No mutés — creá uno nuevo

```typescript
// ❌ Muta el array original
const agregarMutable = (arr: number[], item: number): void => {
  arr.push(item);
};

// ✅ Retorna un nuevo array
const agregarInmutable = (arr: readonly number[], item: number): readonly number[] =>
  [...arr, item];
```

**Herramientas en TypeScript:**
- `readonly` — previene reasignación a nivel de tipo
- `as const` — convierte literales en tipos inmutables
- Spread (`...`) — copia sin mutar
- `map`, `filter`, `slice` — métodos no mutantes

> ⚠️ `sort()` y `splice()` **mutan** el array. Usar `[...arr].sort()`.

---

<!-- SLIDE 08 -->
## SLIDE 08 — Recursión como control de flujo

## Sin loops, con recursión

```typescript
// Suma imperativa — usa estado (total)
const sumaImperativa = (nums: number[]): number => {
  let total = 0;
  for (const n of nums) total += n;
  return total;
};

// Suma funcional — sin estado mutable
const sumaRecursiva = (nums: number[]): number =>
  nums.length === 0 ? 0 : nums[0] + sumaRecursiva(nums.slice(1));

// Práctica: usar reduce (más eficiente en JS)
const suma = (nums: number[]) => nums.reduce((acc, n) => acc + n, 0);
```

> ⚠️ **Limitación JS/TS:** No hay TCO (tail call optimization) en V8.  
> En Haskell y lenguajes puramente funcionales, la recursión de cola es eficiente.

---

<!-- ============================================================ -->
## BLOQUE 3 — FUNCIONES DE ORDEN SUPERIOR (30 min)
<!-- ============================================================ -->

<!-- SLIDE 09 -->
## SLIDE 09 — Funciones como valores de primera clase

## Las funciones son valores

```typescript
// Guardadas en variables
const saludar = (nombre: string) => `Hola, ${nombre}!`;

// Pasadas como argumento
const aplicar = (fn: (x: number) => number, valor: number) => fn(valor);
aplicar(x => x * 2, 5); // 10

// Retornadas como resultado (función generadora)
const multiplicadorPor = (factor: number) => (n: number) => n * factor;
const triple = multiplicadorPor(3);
triple(4); // 12
```

> 🔑 Esto se llama **ciudadanos de primera clase** (*first-class functions*)

---

<!-- SLIDE 10 -->
## SLIDE 10 — map, filter, reduce

## Las tres joyas del funcional

```typescript
const nums = [1, 2, 3, 4, 5, 6];

// map — transforma cada elemento
nums.map(n => n ** 2);           // [1, 4, 9, 16, 25, 36]

// filter — selecciona por predicado
nums.filter(n => n % 2 === 0);   // [2, 4, 6]

// reduce — colapsa en un valor
nums.reduce((acc, n) => acc + n, 0); // 21
```

**Composición de los tres:**
```typescript
const resultado = [1, 2, 3, 4, 5, 6]
  .filter(n => n % 2 === 0)       // [2, 4, 6]
  .map(n => n ** 2)               // [4, 16, 36]
  .reduce((acc, n) => acc + n, 0); // 56
```

---

<!-- SLIDE 11 -->
## SLIDE 11 — Implementando map y filter desde cero

## Bajo el capó

```typescript
// map con reduce
const myMap = <A, B>(fn: (a: A) => B, arr: readonly A[]): B[] =>
  arr.reduce<B[]>((acc, x) => [...acc, fn(x)], []);

// filter con reduce
const myFilter = <A>(pred: (a: A) => boolean, arr: readonly A[]): A[] =>
  arr.reduce<A[]>((acc, x) => pred(x) ? [...acc, x] : acc, []);
```

> 💡 `reduce` es la función más poderosa: `map` y `filter` son casos especiales de `reduce`.

---

<!-- SLIDE 12 -->
## SLIDE 12 — 🔧 Ejercicio: frecuencias con reduce

## Ejercicio en parejas (10 min)

> *Implementar una función `frecuencias` que tome un arreglo de strings y devuelva cuántas veces aparece cada string. Solo usando `reduce`, sin bucles.*

```typescript
const frecuencias = (palabras: readonly string[]): Record<string, number> =>
  palabras.reduce<Record<string, number>>(
    (acc, palabra) => ({ ...acc, [palabra]: (acc[palabra] ?? 0) + 1 }),
    {}
  );

frecuencias(["hola", "mundo", "hola", "TS"]);
// { hola: 2, mundo: 1, TS: 1 }
```

---

<!-- SLIDE 13 -->
## SLIDE 13 — Clausuras y ámbito léxico

## Clausuras (Closures)

Una *clausura* captura las variables de su entorno de definición:

```typescript
const crearContador = (inicio = 0) => {
  let cuenta = inicio; // capturado
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

> ⚠️ *Este ejemplo tiene estado mutable interno — no es "puro".*  
> En funcional puro, el estado se pasa como argumento (pattern: *state passing style*).

> 🔑 **Ámbito léxico**: la función captura el entorno donde fue **definida**, no donde fue **llamada**.

---

<!-- ============================================================ -->
## BLOQUE 4 — COMPOSICIÓN Y CURRIFICACIÓN (20 min)
<!-- ============================================================ -->

<!-- SLIDE 14 -->
## SLIDE 14 — Composición de funciones

## Componer: la operación fundamental

> **f ∘ g** significa: aplicar g primero, luego f.

```typescript
// compose: de derecha a izquierda
const compose = <A, B, C>(f: (b: B) => C, g: (a: A) => B) => (a: A): C => f(g(a));

// pipe: de izquierda a derecha (más legible)
const pipe = <A, B, C>(g: (a: A) => B, f: (b: B) => C) => (a: A): C => f(g(a));

// Ejemplo:
const limpiar = (s: string) => s.trim();
const mayus   = (s: string) => s.toUpperCase();
const excl    = (s: string) => `${s}!`;

const gritar = pipe(pipe(limpiar, mayus), excl);
gritar("  hola mundo  "); // "HOLA MUNDO!"
```

> 🔑 *Cada función hace una sola cosa. La complejidad emerge de la composición.*

---

<!-- SLIDE 15 -->
## SLIDE 15 — Currificación y aplicación parcial

## Curry: funciones de un argumento a la vez

```typescript
// Sin currificación
const add = (a: number, b: number) => a + b;

// Currificada
const addCurried = (a: number) => (b: number) => a + b;

// Aplicación parcial:
const add5 = addCurried(5);
add5(3);  // 8
add5(10); // 15

// En pipelines:
[1, 2, 3, 4, 5].map(addCurried(10));
// [11, 12, 13, 14, 15]
```

---

<!-- SLIDE 16 -->
## SLIDE 16 — 🔧 Ejercicio: pipeline funcional

## Ejercicio rápido (5 min)

> *Con `pipe`, construir un pipeline que:*
> 1. *Filtre los números pares*
> 2. *Los multiplique por 3*
> 3. *Los sume*

```typescript
const filtrarPares = (arr: number[]) => arr.filter(n => n % 2 === 0);
const triplicar    = (arr: number[]) => arr.map(n => n * 3);
const sumar        = (arr: number[]) => arr.reduce((a, b) => a + b, 0);

const procesarPares = pipe(pipe(filtrarPares, triplicar), sumar);
procesarPares([1, 2, 3, 4, 5, 6]); // (2+4+6)*3 = 36
```

> ❓ *¿Qué ventaja tiene esto frente a una función monolítica `f(arr) { ... }`?*

---

<!-- ============================================================ -->
## BLOQUE 5 — EFECTOS Y LAZY (10 min)
<!-- ============================================================ -->

<!-- SLIDE 17 -->
## SLIDE 17 — La frontera de la pureza

## Aislar los efectos

```
╔══════════════════════════════════════════╗
║              MUNDO IMPURO                ║
║  Input [IO]  ──────────────  Output [IO] ║
║       ↓                          ↑       ║
║    ┌──────────────────────────┐  ║       ║
║    │      NÚCLEO PURO         │  ║       ║
║    │ Transformaciones puras   │  ║       ║
║    │ Sin efectos, testeable   │  ║       ║
║    └──────────────────────────┘  ║       ║
╚══════════════════════════════════════════╝
```

> 🎯 **Principio**: empujar los efectos hacia los *bordes* del sistema.  
> El núcleo es puro → fácil de testear, razonar y componer.

---

<!-- SLIDE 18 -->
## SLIDE 18 — Evaluación perezosa con generadores

## Lazy en TypeScript

```typescript
// Generador lazy — produce infinitos naturales
function* naturales(): Generator<number> {
  let n = 0;
  while (true) yield n++;
}

// Tomar los primeros N — sin evaluar todo el stream
function tomar<T>(n: number, gen: Generator<T>): T[] {
  const res: T[] = [];
  for (const v of gen) {
    res.push(v);
    if (res.length >= n) break;
  }
  return res;
}

tomar(5, naturales()); // [0, 1, 2, 3, 4]
```

> 🔁 En **Haskell**, toda la evaluación es perezosa por defecto.  
> En **TypeScript**, es opt-in con generadores.

---

<!-- ============================================================ -->
## BLOQUE 6 — MÓNADAS (20 min)
<!-- ============================================================ -->

<!-- SLIDE 19 -->
## SLIDE 19 — El problema que resuelven las mónadas

## Sin protección: crashes en cadena

```typescript
// ¿Qué pasa si usuario.direccion es null?
const obtenerCiudad = (usuario: any) =>
  usuario.direccion.ciudad.toUpperCase(); // 💥 TypeError

// Solución imperativa: verificar en cada paso
const obtenerCiudadSeguro = (usuario: any) => {
  if (!usuario) return null;
  if (!usuario.direccion) return null;
  if (!usuario.direccion.ciudad) return null;
  return usuario.direccion.ciudad.toUpperCase();
};
```

> ❓ *¿Hay una forma de encadenar estas operaciones sin los `if null` manuales?*  
> → **Sí. Mónadas.**

---

<!-- SLIDE 20 -->
## SLIDE 20 — Maybe / Option

## La mónada de opcionalidad

```typescript
type Option<A> = { tag: "some"; value: A } | { tag: "none" };

const some = <A>(value: A): Option<A> => ({ tag: "some", value });
const none = <A>(): Option<A> => ({ tag: "none" });

// flatMap — encadena operaciones que pueden fallar
const flatMap = <A, B>(fn: (a: A) => Option<B>, opt: Option<A>): Option<B> =>
  opt.tag === "some" ? fn(opt.value) : none();
```

```typescript
// Uso: pipeline seguro sin verificaciones manuales
const obtenerUsuario = (id: number): Option<{ nombre: string }> =>
  id === 1 ? some({ nombre: "Ana" }) : none();

const aNombre = (u: { nombre: string }) => some(u.nombre.toUpperCase());

flatMap(aNombre, obtenerUsuario(1));  // { tag: "some", value: "ANA" }
flatMap(aNombre, obtenerUsuario(99)); // { tag: "none" }
```

---

<!-- SLIDE 21 -->
## SLIDE 21 — Either — mónada de error

## Éxito o error, sin excepciones

```typescript
type Either<E, A> =
  | { tag: "left";  error: E   }   // Error — Left
  | { tag: "right"; value: A  };   // Éxito — Right

const parsearNumero = (s: string): Either<string, number> => {
  const n = Number(s);
  return isNaN(n)
    ? { tag: "left",  error: `"${s}" no es un número` }
    : { tag: "right", value: n };
};

parsearNumero("42");   // { tag: "right", value: 42 }
parsearNumero("abc");  // { tag: "left",  error: '"abc" no es un número' }
```

> 🎯 `Either` = resultado **o** error, siempre explícito en el tipo.  
> No hay `try/catch` ocultos.

---

<!-- SLIDE 22 -->
## SLIDE 22 — Promise: la mónada que ya usás

## Ya trabajás con mónadas

```typescript
// .then() = flatMap de la mónada Promise
fetch("/api/usuario")
  .then(res => res.json())          // si falla → los .then siguientes se saltean
  .then(data => data.nombre)
  .catch(err => console.error(err));

// async/await es syntactic sugar sobre la mónada Promise
const obtenerNombre = async () => {
  const res  = await fetch("/api/usuario");
  const data = await res.json();
  return data.nombre;
};
```

> 💡 *`Promise` tiene `then` (flatMap) y `catch` (manejo del error) — es una mónada.*  
> → **Profundizamos en Tema 05.**

---

<!-- ============================================================ -->
## BLOQUE 7 — CIERRE (10 min)
<!-- ============================================================ -->

<!-- SLIDE 23 -->
## SLIDE 23 — Mapa conceptual del paradigma funcional

## ¿Qué vimos hoy?

```
Paradigma Funcional
│
├── Fundamentos
│   ├── Función pura     → deterministmo + sin efectos
│   ├── Inmutabilidad    → no se muta, se crea nuevo
│   └── Recursión        → control de flujo sin estado
│
├── Funciones de orden superior
│   ├── map / filter / reduce
│   ├── Clausuras        → captura del entorno léxico
│   └── Funciones generadoras
│
├── Composición
│   ├── pipe / compose
│   ├── Currificación    → f(a)(b) en lugar de f(a,b)
│   └── Aplicación parcial
│
├── Efectos
│   ├── Aislar efectos   → núcleo puro, bordes impuros
│   └── Evaluación lazy  → generadores en TS
│
└── Mónadas (intro)
    ├── Option / Maybe   → opcionalidad sin null
    ├── Either           → error explícito en tipo
    └── Promise          → asincronía encadenada
```

---

<!-- SLIDE 24 -->
## SLIDE 24 — Próximos temas

## ¿A dónde vamos?

| Tema | Contenido |
|------|-----------|
| **Tema 04** | Aspectos avanzados: pattern matching, functores, FP reactiva |
| **Tema 05** | Mónadas en TypeScript: `Maybe`, `Either`, `IO`, `Task` |
| **Tema 06** | Funcional en Python — ecosistema IA |

> 🔁 *Los conceptos de hoy son el lenguaje de los próximos tres temas.*  
> Si algo quedó difuso: está en la guía de estudio del Tema 03.

---

<!-- SLIDE 25 -->
## SLIDE 25 — Reflexión de cierre

## Pregunta para llevarte

> *"¿Qué cambiarías en el código que escribís habitualmente  
> si adoptaras solo uno de los principios que vimos hoy?"*

**Escribe:**
- Un principio funcional
- Una situación concreta donde lo aplicarías

> *No hay respuesta única. La idea es conectar el paradigma con su práctica real.*

---

<!-- SLIDE 26 -->
## SLIDE 26 — Referencias

## Fuentes de esta clase

- Gabbrielli, M. & Martini, S. (2023). *Programming Languages: Principles and Paradigms* — Cap. 11: Functional Programming Paradigm.
- Sebesta, R. (2018). *Concepts of Programming Languages*, 12th ed. — Cap. 15: Functional Programming Languages.
- Material de cátedra: *Introducción a la Programación Funcional con Kotlin* — UNTDF, 2025 (adaptado a TypeScript).

---
