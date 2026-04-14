# Trabajo Práctico 04 — Aspectos Avanzados de Programación Funcional

**Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
**Tema:** 04 — Funcional Avanzado
**Tipo de entrega:** Repositorio GitHub Classroom (autograding)
**Lenguajes:** TypeScript + Clojure
**Puntos totales:** 100
**Fecha de entrega:** ___________

---

## Instrucciones generales

1. Aceptá el assignment desde el link proporcionado por tu docente.
2. GitHub crea un repo privado en tu cuenta con el código base.
3. Cloná tu repo: `git clone <url-de-tu-repo>`
4. Implementá las soluciones en los archivos indicados:
   - **TypeScript:** `typescript/src/ejXX.ts`
   - **Clojure:** `clojure/src/tp04/ejXX.clj`
5. **No modifiques los archivos de test** — solo editá los archivos en `src/`.
6. Los tests se ejecutan automáticamente con cada `git push`.
7. Verificá que el check ✅ aparece en tu repo antes de la fecha límite.

### Cómo ejecutar los tests localmente

**TypeScript:**
```bash
cd typescript
npm install
npx vitest run                          # todos los tests
npx vitest run tests/ej01.test.ts       # un ejercicio específico
```

**Clojure:**
```bash
cd clojure
lein deps
lein test                               # todos los tests
lein test tp04.ej04-test                # un ejercicio específico
```

---

## Modelo de datos compartido

Ambos lenguajes trabajan con el mismo dominio de órdenes de compra:

**TypeScript:**
```typescript
type Orden = {
  id: number;
  cliente: string;
  total: number;
  categoria: string;
  activa: boolean;
};
```

**Clojure:**
```clojure
{:id 1 :cliente "Ana" :total 250 :categoria "elect" :activa? true}
```

---

## Consignas

### BLOQUE 1 — HOF y composición

#### Ejercicio 1 — Pipeline filter/map/reduce (TypeScript) — 5 pts
**Trazabilidad:** F-04, F-05, F-10 | **Archivo:** `typescript/src/ej01.ts`

Implementá funciones que procesan un array de órdenes usando un pipeline funcional:

- `filtrarActivasYSumar(ordenes: Orden[]): number` — Filtra las órdenes activas, extrae sus totales y los suma.
- `obtenerTotalesActivas(ordenes: Orden[]): number[]` — Filtra las activas y devuelve un array con sus totales.
- `contarPorCategoria(ordenes: Orden[]): Record<string, number>` — Cuenta cuántas órdenes hay por cada categoría (usando `reduce`).

**Ejemplo:**
```typescript
const ordenes = [
  { id: 1, cliente: "Ana", total: 120, categoria: "elect", activa: true },
  { id: 2, cliente: "Boris", total: 50, categoria: "ropa", activa: false },
  { id: 3, cliente: "Carla", total: 200, categoria: "elect", activa: true },
];
filtrarActivasYSumar(ordenes);    // → 320
obtenerTotalesActivas(ordenes);   // → [120, 200]
contarPorCategoria(ordenes);      // → { elect: 2, ropa: 1 }
```

**Restricción:** No usar variables mutables (`let`, bucles `for`). Solo `filter`, `map`, `reduce`.

---

#### Ejercicio 2 — Composición con pipe y compose (TypeScript) — 6 pts
**Trazabilidad:** F-06, F-07 | **Archivo:** `typescript/src/ej02.ts`

Implementá las funciones de composición y un pipeline real:

- `pipe(...fns): (x) => result` — Compone funciones de izquierda a derecha.
- `compose(...fns): (x) => result` — Compone funciones de derecha a izquierda.
- `normalizeEmail(raw: string): string` — Pipeline que aplica `trim`, `toLowerCase`, y agrega `@empresa.com` si no tiene `@`. Construido con `pipe`.

**Ejemplo:**
```typescript
const inc = (x: number) => x + 1;
const doble = (x: number) => x * 2;

pipe(inc, doble)(3);      // → 8   (primero +1, luego ×2)
compose(inc, doble)(3);   // → 7   (primero ×2, luego +1)
pipe()(5);                // → 5   (sin funciones, identidad)

normalizeEmail("  ANA  ");           // → "ana@empresa.com"
normalizeEmail("  Bob@test.com  ");  // → "bob@test.com"
```

**Restricción:** Usar `reduce` / `reduceRight` internamente. No usar loops.

---

#### Ejercicio 3 — Inmutabilidad con spread (TypeScript) — 4 pts
**Trazabilidad:** F-09 | **Archivo:** `typescript/src/ej03.ts`

Implementá funciones que devuelven nuevos objetos sin modificar los originales:

- `cumpleanios(p: Persona): Persona` — Devuelve una nueva persona con `edad + 1`.
- `agregarHobby(p: Persona, hobby: string): Persona` — Devuelve una nueva persona con el hobby agregado al final.
- `actualizarNombre(p: Persona, nombre: string): Persona` — Devuelve una nueva persona con el nombre actualizado.
- `normalizeUser(u: User): User` — Aplica `trim` a `name` y `toLowerCase` + `trim` a `email`, retornando un nuevo objeto.

**Tipos dados:**
```typescript
type Persona = { readonly nombre: string; readonly edad: number; readonly hobbies: readonly string[] };
type User = { readonly name: string; readonly email: string };
```

**Ejemplo:**
```typescript
const ana = { nombre: "Ana", edad: 28, hobbies: ["leer", "correr"] };
const ana29 = cumpleanios(ana);
ana29.edad;   // → 29
ana.edad;     // → 28 (intacto)

normalizeUser({ name: "  Ana  ", email: "  ANA@test.com  " });
// → { name: "Ana", email: "ana@test.com" }
```

**Restricción:** No usar `Object.assign` ni mutación directa. Solo spread `{ ...obj }` y `[...arr]`.

---

#### Ejercicio 4 — Pipeline con ->> (Clojure) — 5 pts
**Trazabilidad:** F-08 | **Archivo:** `clojure/src/tp04/ej04.clj`

Implementá funciones que usen el macro `->>` para procesar órdenes:

- `(total-activas ordenes)` — Filtra las activas, extrae `:total` y suma.
- `(nombres-activas ordenes)` — Filtra las activas y devuelve un vector con sus `:cliente`.
- `(cuadrados-pares nums)` — Filtra pares, eleva al cuadrado, suma. Todo con `->>`.

**Ejemplo:**
```clojure
(def ordenes [{:id 1 :cliente "Ana" :total 120 :activa? true}
              {:id 2 :cliente "Boris" :total 50 :activa? false}
              {:id 3 :cliente "Carla" :total 200 :activa? true}])

(total-activas ordenes)     ; => 320
(nombres-activas ordenes)   ; => ["Ana" "Carla"]
(cuadrados-pares [1 2 3 4 5]) ; => 20  (4 + 16)
```

**Restricción:** Cada función DEBE usar `->>`. No usar `loop/recur` ni variables mutables.

---

#### Ejercicio 5 — flatMap y reduce avanzado (TypeScript) — 5 pts
**Trazabilidad:** F-11, F-12 | **Archivo:** `typescript/src/ej05.ts`

Implementá funciones que demuestren `flatMap` y `reduce` como herramientas de transformación:

- `todosLosRoles(users: UserWithRoles[]): string[]` — Extrae todos los roles de todos los usuarios usando `flatMap` (con duplicados).
- `rolesUnicos(users: UserWithRoles[]): string[]` — Como el anterior pero sin duplicados (usar `Set`).
- `indexarPorId(items: { id: number; nombre: string }[]): Record<number, string>` — Construye un diccionario `id → nombre` con `reduce`.

**Tipo dado:**
```typescript
type UserWithRoles = { name: string; roles: string[] };
```

**Ejemplo:**
```typescript
const users = [
  { name: "Ana", roles: ["admin", "editor"] },
  { name: "Luis", roles: ["editor"] },
  { name: "María", roles: ["viewer", "editor"] },
];
todosLosRoles(users);  // → ["admin", "editor", "editor", "viewer", "editor"]
rolesUnicos(users);    // → ["admin", "editor", "viewer"]

indexarPorId([{ id: 1, nombre: "Ana" }, { id: 2, nombre: "Luis" }]);
// → { 1: "Ana", 2: "Luis" }
```

---

### BLOQUE 2 — Partial application, currying y validación

#### Ejercicio 6 — Partial application (TypeScript) — 6 pts
**Trazabilidad:** F-13, F-14 | **Archivo:** `typescript/src/ej06.ts`

Implementá partial application con closures:

- `partial(fn, a)` — Recibe una función de 2 args y el primer arg, devuelve función de 1 arg.
- `makeGreeter(saludo: string): (nombre: string) => string` — Fábrica de saludadores. `makeGreeter("Hola")("Ana")` → `"Hola, Ana"`.
- `makeRequiredValidator(fieldName: string): (value: string) => Result<string, string>` — Fábrica de validadores. Retorna `ok(value)` si no está vacío (después de trim), o `err("${fieldName} es obligatorio")`.

**Tipo dado:**
```typescript
type Result<T, E> = { status: "ok"; value: T } | { status: "error"; error: E };
```

**Ejemplo:**
```typescript
const add = (a: number, b: number) => a + b;
const add5 = partial(add, 5);
add5(3);  // → 8

makeGreeter("Hola")("Ana");       // → "Hola, Ana"
makeRequiredValidator("email")("ana@test.com");  // → { status: "ok", value: "ana@test.com" }
makeRequiredValidator("email")("");              // → { status: "error", error: "email es obligatorio" }
```

---

#### Ejercicio 7 — Partial en Clojure (Clojure) — 5 pts
**Trazabilidad:** F-15 | **Archivo:** `clojure/src/tp04/ej07.clj`

Implementá funciones usando `partial` nativo de Clojure:

- `(def doble (partial * 2))` — Duplica un número.
- `(def triple (partial * 3))` — Triplica un número.
- `(def validate-name (partial required-field "nombre"))` — Validador parcializado.
- `(def validate-email (partial required-field "email"))` — Validador parcializado.
- `(required-field field-name value)` — Retorna `{:status :ok :value value}` si `(seq (str/trim value))`, o `{:status :error :error "FIELD es obligatorio"}`.

**Ejemplo:**
```clojure
(doble 5)              ; => 10
(triple 4)             ; => 12
(map doble [1 2 3])    ; => (2 4 6)

(validate-name "Ana")  ; => {:status :ok, :value "Ana"}
(validate-name "")     ; => {:status :error, :error "nombre es obligatorio"}
(validate-email "")    ; => {:status :error, :error "email es obligatorio"}
```

---

#### Ejercicio 8 — Currying (TypeScript) — 6 pts
**Trazabilidad:** F-16, F-17 | **Archivo:** `typescript/src/ej08.ts`

Implementá currying y úsalo para construir validators:

- `curry2(fn)` — Convierte una función de 2 args en cadena de funciones de 1 arg.
- `curry3(fn)` — Convierte una función de 3 args en cadena de funciones de 1 arg.
- `cHasMinLength` — Versión currificada de `hasMinLength(min, str)` que retorna `boolean`.
- `cMultiply` — Versión currificada de `multiply(a, b)`.

**Ejemplo:**
```typescript
const add = (a: number, b: number) => a + b;
const cAdd = curry2(add);
cAdd(3)(4);  // → 7

const hasMinLength = (min: number, str: string) => str.length >= min;
const cHasMinLength = curry2(hasMinLength);
const atLeast8 = cHasMinLength(8);
atLeast8("password123");  // → true
atLeast8("short");        // → false

const sum3 = (a: number, b: number, c: number) => a + b + c;
const cSum3 = curry3(sum3);
cSum3(1)(2)(3);  // → 6
```

---

#### Ejercicio 9 — Validadores con currying (Clojure) — 5 pts
**Trazabilidad:** F-18 | **Archivo:** `clojure/src/tp04/ej09.clj`

Implementá validadores configurables al estilo HOF:

- `(make-validator pred error-msg)` — Retorna una función que recibe un valor y devuelve `{:status :ok :value val}` o `{:status :error :error error-msg}`.
- `(validate-field value & validators)` — Aplica validators en secuencia; para en el primer error.
- `validate-not-empty` — Validator: falla si el string está vacío (después de trim).
- `validate-email-format` — Validator: falla si no contiene `@` y `.`.

**Ejemplo:**
```clojure
(validate-not-empty "Ana")           ; => {:status :ok, :value "Ana"}
(validate-not-empty "")              ; => {:status :error, :error "campo vacío"}
(validate-email-format "a@b.com")    ; => {:status :ok, :value "a@b.com"}
(validate-email-format "invalid")    ; => {:status :error, :error "email inválido"}

(validate-field "ana@test.com" validate-not-empty validate-email-format)
; => {:status :ok, :value "ana@test.com"}

(validate-field "" validate-not-empty validate-email-format)
; => {:status :error, :error "campo vacío"}
```

---

#### Ejercicio 10 — Result y validación encadenada (TypeScript) — 7 pts
**Trazabilidad:** F-19, F-20, F-21 | **Archivo:** `typescript/src/ej10.ts`

Implementá el patrón `Result` completo con encadenamiento:

- `ok(value)` — Constructor de éxito.
- `err(error)` — Constructor de error.
- `chain(result, validator)` — Si `result` es error, propaga. Si es ok, aplica `validator` al valor.
- `validateForm(data: FormData): Result<FormData, string>` — Encadena 3 validators: nombre requerido, email válido (contiene `@` y `.`), password ≥ 8 chars.
- `handleResult(result: Result<FormData, string>): { status: number; body: unknown }` — Retorna `{ status: 400, body: { error } }` si error, o `{ status: 200, body: { user: value } }` si ok.

**Tipo dado:**
```typescript
type FormData = { name: string; email: string; password: string };
type Result<T, E> = { status: "ok"; value: T } | { status: "error"; error: E };
```

**Ejemplo:**
```typescript
validateForm({ name: "Ana", email: "ana@test.com", password: "12345678" });
// → { status: "ok", value: { name: "Ana", email: "ana@test.com", password: "12345678" } }

validateForm({ name: "", email: "ana@test.com", password: "12345678" });
// → { status: "error", error: "nombre requerido" }

validateForm({ name: "Ana", email: "invalid", password: "12345678" });
// → { status: "error", error: "email inválido" }

handleResult(ok({ name: "Ana", email: "a@b.com", password: "12345678" }));
// → { status: 200, body: { user: { name: "Ana", ... } } }
```

---

#### Ejercicio 11 — Middleware como HOF (TypeScript) — 6 pts
**Trazabilidad:** F-22, F-23 | **Archivo:** `typescript/src/ej11.ts`

Implementá middlewares composables:

- `withAuth(secret: string): Middleware` — Si `req.headers["authorization"]` es `"Bearer ${secret}"`, continúa. Si no, retorna `{ status: 401, body: { error: "unauthorized" } }`.
- `withLogging(prefix: string): Middleware` — Registra `"[prefix] request"` en `req.meta.logs` (array de strings) antes de llamar al handler.
- Componer ambos con `pipe` y aplicarlos a un handler base.

**Tipos dados:**
```typescript
type Request  = { headers: Record<string, string>; body: unknown; meta: { logs: string[] } };
type Response = { status: number; body: unknown };
type Handler  = (req: Request) => Response;
type Middleware = (handler: Handler) => Handler;
```

**Ejemplo:**
```typescript
const baseHandler: Handler = req => ({ status: 200, body: { ok: true } });

const secured = pipe(withLogging("api"), withAuth("secret123"))(baseHandler);

secured({ headers: { authorization: "Bearer secret123" }, body: {}, meta: { logs: [] } });
// → { status: 200, body: { ok: true } }
// req.meta.logs contiene ["[api] request"]

secured({ headers: { authorization: "wrong" }, body: {}, meta: { logs: [] } });
// → { status: 401, body: { error: "unauthorized" } }
```

---

### BLOQUE 3 — Recursión de cola y patrones avanzados

#### Ejercicio 12 — Recursión de cola (Clojure) — 6 pts
**Trazabilidad:** F-24, F-25, F-26 | **Archivo:** `clojure/src/tp04/ej12.clj`

Implementá funciones usando `recur` para garantizar TCO:

- `(sum-list nums acc)` — Suma todos los elementos con acumulador.
- `(factorial n acc)` — Factorial con acumulador (`(factorial 5 1)` → `120`).
- `(my-reverse xs acc)` — Revierte una lista con acumulador.
- `(my-count xs acc)` — Cuenta elementos de una lista con acumulador.

**Ejemplo:**
```clojure
(sum-list [1 2 3 4 5] 0)   ; => 15
(factorial 5 1)             ; => 120
(factorial 0 1)             ; => 1
(my-reverse [1 2 3] [])    ; => [3 2 1]
(my-count [10 20 30] 0)    ; => 3
```

**Restricción:** Todas DEBEN usar `recur`. No usar `reduce`, `count`, `reverse` ni funciones built-in equivalentes.

---

#### Ejercicio 13 — Recursión de cola (TypeScript) — 5 pts
**Trazabilidad:** F-27 | **Archivo:** `typescript/src/ej13.ts`

Implementá funciones recursivas con acumulador en TypeScript:

- `sumList(nums: number[], acc?: number): number` — Suma con acumulador (default 0).
- `factorial(n: number, acc?: number): number` — Factorial con acumulador (default 1).
- `findInTree(nodes: TreeNode[], target: number): number | null` — Busca un valor en un árbol N-ario recorriendo en pre-order con stack explícito.

**Tipo dado:**
```typescript
type TreeNode = { value: number; children: TreeNode[] };
```

**Ejemplo:**
```typescript
sumList([1, 2, 3, 4, 5]);  // → 15
factorial(5);               // → 120
factorial(0);               // → 1

const tree: TreeNode = {
  value: 1,
  children: [
    { value: 2, children: [{ value: 4, children: [] }] },
    { value: 3, children: [] },
  ],
};
findInTree([tree], 4);  // → 4
findInTree([tree], 9);  // → null
```

**Restricción:** No usar bucles `for`/`while`. Las funciones de suma/factorial DEBEN ser recursivas con acumulador.

---

#### Ejercicio 14 — Memoization (TypeScript) — 5 pts
**Trazabilidad:** F-28, F-29 | **Archivo:** `typescript/src/ej14.ts`

Implementá memoization genérica y verificá su efecto:

- `memoize(fn)` — Recibe una función de 1 argumento y retorna una versión con cache (usar `Map`).
- `fibonacci(n: number): number` — Fibonacci recursivo clásico (sin memo).
- `fibonacciMemo` — Fibonacci con `memoize` aplicado.
- `callCounter(fn)` — Wrapper que cuenta cuántas veces se llama la función original. Retorna `{ call: (...args) => result, count: () => number }`.

**Ejemplo:**
```typescript
const mFib = memoize(fibonacci);
mFib(10);  // → 55
mFib(10);  // → 55 (desde cache, sin recalcular)

const counter = callCounter((x: number) => x * 2);
counter.call(5);   // → 10
counter.call(5);   // → 10
counter.count();   // → 2

// Con memoize + counter, la función original se llama solo 1 vez para el mismo input
```

---

#### Ejercicio 15 — Lazy sequences (Clojure) — 5 pts
**Trazabilidad:** F-30 | **Archivo:** `clojure/src/tp04/ej15.clj`

Implementá funciones que generen y consuman secuencias perezosas:

- `(primeros-n-pares n)` — Los primeros `n` números pares positivos (2, 4, 6...).
- `(fibonacci)` — Secuencia infinita de Fibonacci (0, 1, 1, 2, 3, 5, 8...).
- `(tomar-mientras-menor coll umbral)` — Toma elementos mientras sean menores que `umbral`.

**Ejemplo:**
```clojure
(primeros-n-pares 4)          ; => (2 4 6 8)
(take 7 (fibonacci))          ; => (0 1 1 2 3 5 8)
(tomar-mientras-menor [1 3 5 7 2] 6) ; => (1 3 5)
```

**Restricción:** `fibonacci` debe ser lazy — no precomputar. Usar `lazy-seq` o `iterate`.

---

#### Ejercicio 16 — DSL data-driven (Clojure) — 5 pts
**Trazabilidad:** F-31 | **Archivo:** `clojure/src/tp04/ej16.clj`

Implementá un motor de validación genérico donde las reglas son datos:

- `user-rules` — Vector de mapas `{:field :name :pred fn :msg "..."}` con al menos 3 reglas (nombre no vacío, email con `@`, edad ≥ 18).
- `(validate rules data)` — Aplica todas las reglas al mapa `data`. Retorna vector de errores `{:field :error}` (vacío si todo ok).
- `(valid? rules data)` — `true` si no hay errores.

**Ejemplo:**
```clojure
(validate user-rules {:name "" :email "x" :age 16})
; => [{:field :name, :error "nombre requerido"}
;     {:field :email, :error "email inválido"}
;     {:field :age, :error "debe ser mayor de edad"}]

(validate user-rules {:name "Ana" :email "ana@test.com" :age 20})
; => []

(valid? user-rules {:name "Ana" :email "ana@test.com" :age 20})
; => true
```

---

### BLOQUE 4 — Integrador

#### Ejercicio 17 — Integrador TypeScript — 7 pts
**Trazabilidad:** F-33 | **Archivo:** `typescript/src/ej17.ts`

Implementá un pipeline funcional completo de validación y procesamiento de órdenes, combinando todos los patrones del TP:

- `clasificarOrden(o: Orden): Result<Orden, string>` — Retorna `ok(orden)` si la orden es activa Y tiene total > 100. Si no es activa, `err("orden inactiva")`. Si total ≤ 100, `err("monto insuficiente")`.
- `aplicarDescuento(porcentaje: number): (o: Orden) => Orden` — Partial application: retorna función que crea nueva orden con `total` reducido (inmutable).
- `procesarOrdenes(ordenes: Orden[]): { aprobadas: Orden[]; rechazadas: string[]; totalFinal: number }` — Pipeline: clasificar cada orden → separar ok/error → aplicar 10% de descuento a las aprobadas → sumar totales finales.

**Ejemplo:**
```typescript
const ordenes = [
  { id: 1, cliente: "Ana",   total: 250, categoria: "elect", activa: true },
  { id: 2, cliente: "Boris", total: 80,  categoria: "ropa",  activa: false },
  { id: 3, cliente: "Carla", total: 420, categoria: "elect", activa: true },
  { id: 4, cliente: "Diana", total: 50,  categoria: "ropa",  activa: true },
];

clasificarOrden(ordenes[0]);  // → { status: "ok", value: { id: 1, ... } }
clasificarOrden(ordenes[1]);  // → { status: "error", error: "orden inactiva" }
clasificarOrden(ordenes[3]);  // → { status: "error", error: "monto insuficiente" }

aplicarDescuento(10)(ordenes[0]);  // → { ...ordenes[0], total: 225 }

procesarOrdenes(ordenes);
// → {
//   aprobadas: [{ id: 1, ..., total: 225 }, { id: 3, ..., total: 378 }],
//   rechazadas: ["orden inactiva", "monto insuficiente"],
//   totalFinal: 603
// }
```

**Requisitos:**
- Usar `Result` para clasificación.
- Usar partial application para el descuento.
- Usar `filter`, `map`, `reduce` — sin bucles ni mutación.

---

#### Ejercicio 18 — Integrador Clojure — 7 pts
**Trazabilidad:** F-33 | **Archivo:** `clojure/src/tp04/ej18.clj`

Implementá el mismo pipeline integrador en Clojure:

- `(clasificar-orden orden)` — Retorna `{:ok true :value orden}` si activa y total > 100. Error con razón si no.
- `(aplicar-descuento porcentaje orden)` — Retorna nueva orden con total reducido. Usar con `partial` para crear `(def descuento-10 (partial aplicar-descuento 10))`.
- `(procesar-ordenes ordenes)` — Pipeline completo con `->>`: clasificar → separar ok/error → aplicar descuento → sumar. Retorna `{:aprobadas [...] :rechazadas [...] :total-final N}`.

**Ejemplo:**
```clojure
(def ordenes
  [{:id 1 :cliente "Ana"   :total 250 :categoria "elect" :activa? true}
   {:id 2 :cliente "Boris" :total 80  :categoria "ropa"  :activa? false}
   {:id 3 :cliente "Carla" :total 420 :categoria "elect" :activa? true}
   {:id 4 :cliente "Diana" :total 50  :categoria "ropa"  :activa? true}])

(clasificar-orden (first ordenes))
; => {:ok true, :value {:id 1, :cliente "Ana", ...}}

(clasificar-orden (second ordenes))
; => {:ok false, :error "orden inactiva"}

(def descuento-10 (partial aplicar-descuento 10))
(descuento-10 {:id 1 :total 250})  ; => {:id 1, :total 225}

(procesar-ordenes ordenes)
; => {:aprobadas [{:id 1 :total 225 ...} {:id 3 :total 378 ...}]
;     :rechazadas ["orden inactiva" "monto insuficiente"]
;     :total-final 603}
```

---

## Distribución de puntos

| Ej | Tema | Lenguaje | Filminas | Pts |
|----|------|----------|----------|-----|
| 1 | Pipeline filter/map/reduce | TypeScript | F-04, F-05, F-10 | 5 |
| 2 | Composición pipe/compose | TypeScript | F-06, F-07 | 6 |
| 3 | Inmutabilidad con spread | TypeScript | F-09 | 4 |
| 4 | Pipeline con ->> | Clojure | F-08 | 5 |
| 5 | flatMap y reduce avanzado | TypeScript | F-11, F-12 | 5 |
| 6 | Partial application | TypeScript | F-13, F-14 | 6 |
| 7 | Partial en Clojure | Clojure | F-15 | 5 |
| 8 | Currying | TypeScript | F-16, F-17 | 6 |
| 9 | Validadores con currying | Clojure | F-18 | 5 |
| 10 | Result y validación encadenada | TypeScript | F-19, F-20, F-21 | 7 |
| 11 | Middleware como HOF | TypeScript | F-22, F-23 | 6 |
| 12 | Recursión de cola | Clojure | F-24, F-25, F-26 | 6 |
| 13 | Recursión de cola | TypeScript | F-27 | 5 |
| 14 | Memoization | TypeScript | F-28, F-29 | 5 |
| 15 | Lazy sequences | Clojure | F-30 | 5 |
| 16 | DSL data-driven | Clojure | F-31 | 5 |
| 17 | Integrador TypeScript | TypeScript | F-33 | 7 |
| 18 | Integrador Clojure | Clojure | F-33 | 7 |
| | | | **Total** | **100** |

**TypeScript:** 11 ejercicios — 62 pts | **Clojure:** 7 ejercicios — 38 pts

---

## Criterios de evaluación

- **Corrección funcional:** los tests automáticos validan inputs normales y bordes.
- **Estilo funcional:** no se aceptan `let` mutables, bucles `for`/`while` ni mutación de objetos.
- **Trazabilidad:** cada ejercicio corresponde a filminas específicas de la clase.

---

## Correlación con la guía de estudio

Si te trabás en un ejercicio, buscá en la guía de estudio (`guia-estudio.md`) la sección correspondiente:

| Ejercicios | Sección de la guía |
|------------|-------------------|
| 1–5 | Parte 1 — HOF y composición |
| 6–9 | Parte 2 — Partial application y currying |
| 10–11 | Parte 2 — Result y middleware |
| 12–16 | Parte 3 — Recursión, memoization, lazy, DSL |
| 17–18 | Parte 4 — Integración de patrones |
