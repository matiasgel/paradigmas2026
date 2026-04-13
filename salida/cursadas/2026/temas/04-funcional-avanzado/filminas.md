## Plan de Filminas — Tema 04

@tipo: plan-filminas

### [F-01] Portada
@tipo: portada
@imagen: background
# Aspectos Avanzados de Programación Funcional
**Paradigmas de Programación — UNTDF / IDEI 2026**
Tema 04 · Clojure + TypeScript

---
## BLOQUE 1 — Funciones de orden superior y composición (35 min)

### [F-02] Alcance de la clase
@tipo: concepto
# Qué construimos hoy
- **Bloque 1 (35 min):** First-class functions, HOF, compose/pipe, pipelines con datos reales.
- **Bloque 2 (35 min):** Partial application, currying, `Result`, validación y middleware web.
- **Bloque 3 (30 min):** Recursión de cola, memoization, lazy sequences, patrones avanzados.
- **Bloque 4 (20 min):** Taller integrador y comparación Clojure ↔ TypeScript.
- Dos lenguajes, una misma idea: **datos inmutables + funciones puras + composición**.
- Al terminar: podés diseñar un pipeline real de validación/request sin variables mutables.

### [F-03] Qué no cubrimos hoy
@tipo: concepto
# Fuera de scope
- **Concurrency / `core.async`:** canales, go-blocks, STM — temas propios del modelo de actores.
- **Teoría categórica:** funtores, mónadas formales, flechas — abstracto e innecesario en esta etapa.
- **Librerías FP completas:** Ramda, fp-ts, crocks — excelentes, pero no las necesitamos para entender los patrones.
- **Frameworks async/reactive:** RxJS, Effect-TS — dependen de conceptos que aún no vimos.
- Razón: en 120 minutos priorizamos **comprensión profunda > cobertura superficial**.

### [F-04] ¿Qué son las first-class functions?
@tipo: concepto
# Funciones como valores de primera clase
- En FP, una función es un valor igual que un número o un string.
- Se puede **asignar** a una variable, **pasar** como argumento, **devolver** como resultado.
- Esto hace posible las funciones de orden superior (HOF).
- Sin first-class functions no existe `map`, `filter`, ni `compose`.
- **Imperativo:** digo *cómo* iterar. **Funcional:** digo *qué* hacer con cada elemento.
- Ambos lenguajes lo soportan: JavaScript/TypeScript y Clojure son lenguajes funcionales de primera clase.

### [F-05] Anatomía de una HOF
@tipo: concepto
# Higher-Order Function (HOF)
Una función que **recibe** y/o **devuelve** otra función.
```
HOF = f(g, datos) → resultado
```
**Patrones fundamentales:**
- `map(f, lista)` → aplica `f` a cada elemento.
- `filter(pred, lista)` → mantiene los que satisfacen `pred`.
- `reduce(f, acc, lista)` → pliega la lista a un único valor.
- `compose(f, g)(x)` → ejecuta `g(x)` y pasa el resultado a `f`.
- `pipe(f, g)(x)` → igual que compose pero en orden izquierda → derecha.

**Por qué importa:** constituyen el vocabulario con el que se construyen todos los patrones avanzados.

### [F-06] `compose` y `pipe` explicados
@tipo: concepto
# Composición de funciones
`compose` aplica funciones de derecha a izquierda (matemáticamente natural):
```
compose(f, g, h)(x) === f(g(h(x)))
```
`pipe` aplica de izquierda a derecha (más legible para desarrollo):
```
pipe(h, g, f)(x) === f(g(h(x)))
```
**Reglas de composición:**
- Cada función recibe el output de la anterior.
- Los tipos deben ser compatibles entre funciones consecutivas.
- El resultado es una **nueva función** — no se ejecuta nada hasta que se llame.
- Permite nombrar pipelines: `const processUser = pipe(trim, normalize, validate)`.
- En Clojure: el operador `->>`  hace exactamente lo mismo (thread-last macro).

### [F-07] `compose` y `pipe` en TypeScript
@tipo: ejemplo-codigo
# Implementación real en TS
```typescript
// Implementación simple de pipe
const pipe = <T>(...fns: Array<(x: T) => T>) =>
  (x: T): T => fns.reduce((acc, fn) => fn(acc), x);

// Funciones unitarias, puras, testeables por separado
const trim = (s: string) => s.trim();
const lowercase = (s: string) => s.toLowerCase();
const addDomain = (s: string) =>
  s.includes("@") ? s : `${s}@empresa.com`;

// Pipeline nombrado: se lee como una especificación
const normalizeEmail = pipe(trim, lowercase, addDomain);

// Uso en handler de formulario
const handleLogin = (raw: string) => {
  const email = normalizeEmail(raw);   // "  ANA  " → "ana@empresa.com"
  return fetchUser(email);
};
```
- Cada función es independiente → testeable en aislamiento.
- `normalizeEmail` es composable: puede usarse en otros pipelines.

### [F-08] Thread macro en Clojure
@tipo: ejemplo-codigo
# `->>` como pipe en Clojure
```clojure
;; Sin thread macro — difícil de leer
(reduce + (map #(* % %) (filter even? [1 2 3 4 5])))

;; Con ->> — fluye de arriba hacia abajo
(->> [1 2 3 4 5]
     (filter even?)          ; → (2 4)
     (map #(* % %))          ; → (4 16)
     (reduce +))             ; → 20

;; Ejemplo real: pipeline de pedidos
(->> orders
     (filter #(= (:status %) :completed))
     (map :total)
     (reduce + 0))
;; Devuelve la suma de pedidos completados
```
- `->>` inserta el resultado anterior como **último argumento** de cada forma.
- Legible de arriba hacia abajo: cada línea es un paso de transformación.
- Cero variables intermedias: el dato fluye sin ser retenido.

### [F-09] Datos inmutables: el contrato FP
@tipo: ejemplo-codigo
# Inmutabilidad en TypeScript
```typescript
// ❌ Imperativo: mutación directa del objeto
function normalize(user: User): void {
  user.email = user.email.trim().toLowerCase();  // mutación
  user.name = user.name.trim();                  // mutación
}

// ✅ Funcional: cada función produce un nuevo objeto
const trimUser = (u: User): User =>
  ({ ...u, email: u.email.trim(), name: u.name.trim() });

const lowercaseEmail = (u: User): User =>
  ({ ...u, email: u.email.toLowerCase() });

const normalizeUser = pipe(trimUser, lowercaseEmail);

// El objeto original nunca se modifica
const raw = { name: "  Ana  ", email: "  ANA@test.com  " };
const clean = normalizeUser(raw);
// raw sigue igual; clean es el nuevo valor
```
- Spread `{ ...u, key: newVal }` crea nuevo objeto, no modifica el original.
- Facilita debugging: el historial de estados es rastreable.
- Permite comparar estados por referencia (clave para React/Vue).

### [F-10] `map`, `filter` y `flatMap` en profundidad
@tipo: concepto
# Transformación declarativa de colecciones
**`map`:** transforma cada elemento sin cambiar la cantidad.
- `Array<A>.map(A → B): Array<B>`
- Ejemplo: `users.map(u => u.email)` — de usuarios a emails.

**`filter`:** selecciona un subconjunto; el tipo no cambia.
- `Array<A>.filter(A → boolean): Array<A>`
- Ejemplo: `users.filter(u => u.active)` — solo activos.

**`flatMap`:** transforma Y aplana un nivel — útil cuando cada elemento produce una lista.
- `Array<A>.flatMap(A → Array<B>): Array<B>`
- Ejemplo: `users.flatMap(u => u.roles)` — lista plana de todos los roles.
- Sin `flatMap` necesitaríamos `.map(...).flat()` — `flatMap` es más eficiente.

**En Clojure:**  `map`, `filter`, `mapcat` (≡ flatMap). Todo trabaja sobre *seq* (secuencias perezosas).

### [F-11] `flatMap` aplicado: usuarios y permisos
@tipo: ejemplo-codigo
# `flatMap` en contexto real
```typescript
type User = { name: string; roles: string[] };

const users: User[] = [
  { name: "Ana",   roles: ["admin", "editor"] },
  { name: "Luis",  roles: ["editor"] },
  { name: "María", roles: ["viewer", "editor"] },
];

// Lista única de todos los roles (con duplicados)
const allRoles = users.flatMap(u => u.roles);
// → ["admin", "editor", "editor", "viewer", "editor"]

// Roles únicos sin duplicados
const uniqueRoles = [...new Set(users.flatMap(u => u.roles))];
// → ["admin", "editor", "viewer"]

// En Clojure con mapcat (equivalente a flatMap)
(mapcat :roles users)
;; → ("admin" "editor" "editor" "viewer" "editor")
```
- `flatMap` evita anidar arrays; produce una secuencia plana y componible.

### [F-12] `reduce` y `fold`: plegar colecciones
@tipo: ejemplo-codigo
# `reduce` generaliza todo
```typescript
// reduce: (acc, item) → nuevo acc
// Es el patrón más general: map y filter son casos especiales de reduce

// Suma de revenues
const totalRevenue = orders
  .filter(o => o.status === "completed")
  .map(o => o.amount)
  .reduce((sum, amt) => sum + amt, 0);

// Construir un índice (dict) a partir de una lista
const userById = users.reduce(
  (index, user) => ({ ...index, [user.id]: user }),
  {} as Record<string, User>
);

// En Clojure
(reduce + 0 (map :amount (filter #(= :completed (:status %)) orders)))
;; o usando ->>
(->> orders
     (filter #(= :completed (:status %)))
     (map :amount)
     (reduce + 0))
```
- `reduce` es el "fold" de FP: convierte una colección en cualquier tipo.
- Puede construir arrays, objetos, strings, números — lo que se necesite.

---
## BLOQUE 2 — Aplicación parcial, currying y validación web (35 min)

### [F-13] Aplicación parcial: el concepto
@tipo: concepto
# Partial Application
Una función de N argumentos → función con algunos argumentos *prefijados*.
- Produce una función más específica a partir de una genérica.
- No ejecuta la función todavía — espera los argumentos restantes.
- Es la base de las *fábricas de funciones* y los *builders*.

**Ejemplo conceptual:**
```
add(a, b) = a + b          // función 2-aria
add5 = partial(add, 5)     // función 1-aria, con a=5 prefijado
add5(3) → 8
```
**Por qué es útil en web:**
- `makeValidator("email")` → validador especializado para emails.
- `makeLogger("auth")` → logger prefijado con módulo "auth".
- `makeRoute("/api/users")` → route handler especializado.

### [F-14] Partial application en TypeScript
@tipo: ejemplo-codigo
# `partial` en TS con closures
```typescript
// Función genérica de 2 argumentos
const add = (a: number, b: number) => a + b;

// Partial manual con closure
const add5 = (b: number) => add(5, b);
add5(3);  // → 8

// Utility general
const partial = <A, B, C>(fn: (a: A, b: B) => C, a: A) =>
  (b: B): C => fn(a, b);

// Caso real: validador configurable
const makeRequiredValidator =
  (fieldName: string) =>
  (value: string): Result<string, string> =>
    value.trim()
      ? { status: "ok",    value }
      : { status: "error", error: `${fieldName} es obligatorio` };

// Validators especializados — listos para usar en cualquier formulario
const validateName  = makeRequiredValidator("nombre");
const validateEmail = makeRequiredValidator("email");
```
- `makeRequiredValidator` es una fábrica: produce validators distintos desde una lógica genérica.
- Cada validator es stateless y testeable en aislamiento.

### [F-15] Partial application en Clojure
@tipo: ejemplo-codigo
# `partial` nativo de Clojure
```clojure
;; partial en Clojure: devuelve función con args prefijados
(defn multiply [factor n] (* factor n))

(def double  (partial multiply 2))
(def triple  (partial multiply 3))

(map double [1 2 3 4])   ;→ (2 4 6 8)
(map triple [1 2 3 4])   ;→ (3 6 9 12)

;; Validador configurable
(defn required-field [field-name value]
  (if (seq (clojure.string/trim value))
    {:status :ok    :value value}
    {:status :error :error (str field-name " es obligatorio")}))

(def validate-name  (partial required-field "nombre"))
(def validate-email (partial required-field "email"))

(validate-name "Ana")   ;→ {:status :ok, :value "Ana"}
(validate-name "")      ;→ {:status :error, :error "nombre es obligatorio"}
```

### [F-16] Currying: concepto y diferencia con partial
@tipo: concepto
# Currying
Transformar una función de N argumentos en **N funciones anidadas de 1 argumento**.
```
f(a, b, c)      →  a → b → c → resultado
curriedF(a)(b)(c) → resultado
```
**Diferencia clave con partial application:**
| | Partial Application | Currying |
|---|---|---|
| Qué hace | Fija *algunos* argumentos | Convierte en cadena de 1-arg |
| Cuándo aplica | En el momento de usar | Al definir la función |
| Flexibilidad | Cualquier cantidad de args | Siempre 1 arg por vez |

**Por qué importa:**
- Currying permite construir variantes de funciones sin duplicar código.
- Habilita la composición cuando `pipe/compose` necesita funciones de 1 argumento.
- Es idiomático en Haskell, Elm, F# — en TS/Clojure se hace explícitamente.

### [F-17] Currying en TypeScript: implementación
@tipo: ejemplo-codigo
# Curry genérico y uso real
```typescript
// Curry genérico para funciones de 2 args
const curry2 = <A, B, C>(fn: (a: A, b: B) => C) =>
  (a: A) => (b: B): C => fn(a, b);

// Función 2-aria base
const hasMinLength = (min: number, str: string) => str.length >= min;

// Versión currificada
const cHasMinLength = curry2(hasMinLength);

// Validators especializados via currying
const atLeast3 = cHasMinLength(3);   // nombre
const atLeast8 = cHasMinLength(8);   // contraseña

// Uso en pipeline de validación
const validatePassword = pipe(
  trim,
  (s: string) => atLeast8(s)
    ? { status: "ok" as const, value: s }
    : { status: "error" as const, error: "mínimo 8 caracteres" }
);
```
- `cHasMinLength(8)` es una función `string → boolean` usable en cualquier pipeline.
- El tipado de TypeScript infiere correctamente los tipos en cada paso.

### [F-18] Currying en Clojure: estilo HOF
@tipo: ejemplo-codigo
# Currying idiomático en Clojure
```clojure
;; En Clojure se logra con lambdas anidadas
(defn make-validator [pred error-msg]
  (fn [value]
    (if (pred value)
      {:status :ok    :value value}
      {:status :error :error error-msg})))

;; Validators especializados
(def validate-email
  (make-validator
    #(re-matches #".+@.+\..+" %)
    "email inválido"))

(def validate-not-empty
  (make-validator
    #(seq (clojure.string/trim %))
    "campo vacío"))

;; Composición de validators sobre un campo
(defn validate-field [value & validators]
  (reduce
    (fn [result v]
      (if (= :ok (:status result))
        (v (:value result))
        result))
    {:status :ok :value value}
    validators))

(validate-field "ana@test.com" validate-not-empty validate-email)
;; → {:status :ok, :value "ana@test.com"}
```

### [F-19] El tipo `Result<T, E>`
@tipo: concepto
# Errores sin excepciones
Las excepciones rompen el flujo funcional: son un `goto` encubierto.
`Result` modela el éxito o el fracaso **como un valor**.

```typescript
type Result<T, E> =
  | { status: "ok";    value: T }
  | { status: "error"; error: E };
```

**Ventajas sobre try/catch:**
- El tipo de retorno hace explícito que puede fallar — no hay sorpresas.
- El compilador obliga a manejar ambos casos.
- Es composable: se puede encadenar con `flatMap` o `andThen`.
- Más fácil de testear: no necesita `expect(...).toThrow()`.

**Corolario:** si una función puede fallar, su tipo de retorno debe decirlo.
`(data: FormData): Result<ValidData, ValidationError>` — el contrato es claro.

### [F-20] Validación encadenada con `Result`
@tipo: ejemplo-codigo
# Pipeline de validación completo
```typescript
type FormData = { name: string; email: string; password: string };
type Validator<T> = (data: T) => Result<T, string>;

// Validators individuales — cada uno hace UNA cosa
const requireName: Validator<FormData> =
  data => data.name.trim()
    ? { status: "ok", value: data }
    : { status: "error", error: "nombre requerido" };

const requireValidEmail: Validator<FormData> =
  data => /^.+@.+\..+$/.test(data.email)
    ? { status: "ok", value: data }
    : { status: "error", error: "email inválido" };

const requireStrongPassword: Validator<FormData> =
  data => data.password.length >= 8
    ? { status: "ok", value: data }
    : { status: "error", error: "contraseña muy corta" };

// Combinar validators: para en el primer error
const chain = <T>(
  result: Result<T, string>,
  validator: Validator<T>
): Result<T, string> =>
  result.status === "error" ? result : validator(result.value);

const validateForm = (data: FormData): Result<FormData, string> =>
  [requireName, requireValidEmail, requireStrongPassword]
    .reduce(chain, { status: "ok", value: data });
```
- `chain` es el "then" del pipeline: si hay error, propaga; si no, continúa.
- Los validators se acumulan en un array — fácil de añadir nuevas reglas.

### [F-21] Usar el `Result` en un handler HTTP
@tipo: ejemplo-codigo
# Del formulario al servidor
```typescript
// Handler de Express / Hono / Fastify
const registerHandler = async (req: Request, res: Response) => {
  const result = validateForm(req.body);

  if (result.status === "error") {
    // El error ya está tipado: no hay string enmascarada en un throw
    return res.status(400).json({ error: result.error });
  }

  // TypeScript sabe que result.value es FormData válido
  const user = await userService.create(result.value);
  return res.status(201).json(user);
};
```
**Observaciones:**
- No hay try/catch: el flujo es lineal y explícito.
- El tipo `Result` actúa como *protocolo* entre validación y lógica de negocio.
- Lo mismo aplica en validaciones de middleware, pipes de datos, parsing de configs.

### [F-22] Middleware como HOF
@tipo: concepto
# Middleware composable
Un middleware es una función que **recibe** un handler y **devuelve** un handler transformado.
```
Middleware = (Request → Response) → (Request → Response)
```
- Esto es una HOF: recibe y devuelve funciones.
- Se pueden componer en cadena con `pipe` o `compose`.
- Patrón usado en: Express, Koa, Hono, Redux, RxJS operators.

**Sin FP:**
```javascript
// Lógica mezclada, difícil de reusar
router.post("/register", authCheck, logRequest, validateSchema, handler);
```
**Con FP:**
```typescript
const processRegister = pipe(authCheck, logRequest, validateSchema);
router.post("/register", processRegister(handler));
```
- Cada middleware tiene una responsabilidad clara.
- Se pueden reordenar, combinar, testear por separado.

### [F-23] Middleware en TypeScript: implementación
@tipo: ejemplo-codigo
# HOF generadora de middlewares
```typescript
type Request  = { headers: Record<string, string>; body: unknown; meta: Record<string, unknown> };
type Response = { status: number; body: unknown };
type Handler  = (req: Request) => Promise<Response>;
type Middleware = (handler: Handler) => Handler;

// Middleware de autenticación
const withAuth = (secret: string): Middleware =>
  handler => async req => {
    const token = req.headers["authorization"];
    if (token !== `Bearer ${secret}`) {
      return { status: 401, body: { error: "unauthorized" } };
    }
    return handler(req);
  };

// Middleware de logging
const withLogging = (prefix: string): Middleware =>
  handler => async req => {
    console.log(`[${prefix}] incoming request`);
    const res = await handler(req);
    console.log(`[${prefix}] response ${res.status}`);
    return res;
  };

// Composición de middlewares
const secured = pipe(
  withLogging("auth-route"),
  withAuth("my-secret")
)(baseHandler);
```
- `withAuth("my-secret")` es partial application: fija el secreto, devuelve middleware.
- La composición con `pipe` aplica middlewares de afuera hacia adentro.

---
## BLOQUE 3 — Recursión de cola y patrones avanzados (30 min)

### [F-24] Recursión: el problema del stack overflow
@tipo: concepto
# Por qué la recursión simple falla
```
factorial(5)
  → 5 * factorial(4)
       → 4 * factorial(3)
            → 3 * factorial(2)
                 → 2 * factorial(1)
                      → 1
```
- Cada llamada queda *pendiente* hasta que la interna termine.
- Se acumulan frames en el call stack.
- Con listas largas (10k, 100k elementos) → **stack overflow**.
- Los bucles `for/while` no tienen este problema porque no acumulan frames.

**Solución:** recursión de cola — el resultado no espera al retorno de la llamada recursiva.

### [F-25] Recursión de cola: la idea
@tipo: concepto
# Tail Call Optimization (TCO)
Una llamada es "de cola" cuando es **la última operación** de la función — no hay trabajo pendiente después.
```
// No es tail call: aún hay que multiplicar por n
factorial(n) = n * factorial(n-1)   ← queda pendiente la multiplicación

// Sí es tail call: el acumulador lleva el resultado
factorial(n, acc=1) = factorial(n-1, acc*n)  ← nada pendiente
```
- Con un acumulador, el compilador/runtime puede **reemplazar** el frame actual.
- No hay acumulación de stack → puede manejar millones de iteraciones.
- Clojure garantiza TCO explícitamente con `recur`.
- JavaScript/TypeScript **no garantizan** TCO (depende del motor) — pero la lógica es la misma.

### [F-26] `recur` en Clojure
@tipo: ejemplo-codigo
# Recursión de cola con `recur`
```clojure
;; suma de lista — versión con recur (garantiza TCO)
(defn sum-list [nums acc]
  (if (empty? nums)
    acc
    (recur (rest nums) (+ acc (first nums)))))

(sum-list [1 2 3 4 5] 0)   ;→ 15

;; flatten de lista anidada
(defn my-flatten [xs acc]
  (cond
    (empty? xs)    (reverse acc)
    (seq? (first xs))
      (recur (concat (first xs) (rest xs)) acc)
    :else
      (recur (rest xs) (cons (first xs) acc))))

(my-flatten [1 [2 3] [4 [5 6]]] [])   ;→ (1 2 3 4 5 6)
```
- `recur` solo puede llamarse desde la posición de cola — Clojure lo verifica en compilación.
- El acumulador `acc` lleva el resultado parcial; evita frames pendientes.

### [F-27] Recursión de cola en TypeScript
@tipo: ejemplo-codigo
# Equivalente TypeScript
```typescript
// Suma con acumulador
const sumList = (nums: number[], acc = 0): number =>
  nums.length === 0
    ? acc
    : sumList(nums.slice(1), acc + nums[0]);

// Búsqueda en árbol (pre-order, con stack explícito — evita TCO-problem)
type TreeNode = { value: number; children: TreeNode[] };

const findInTree = (
  nodes: TreeNode[],
  target: number
): number | null => {
  if (nodes.length === 0) return null;
  const [head, ...tail] = nodes;
  if (head.value === target) return head.value;
  return findInTree([...head.children, ...tail], target);
};
```
- Para JS/TS: si el stack puede ser muy profundo, usar trampolining o loop explícito.
- La lógica de acumulador es idéntica a Clojure — el patrón es portable.

### [F-28] Memoization: cache funcional
@tipo: concepto
# Memoization
Guardar el resultado de una función para evitar recalcularlo con los mismos argumentos.
```
memoize(f)(x)
  → si x ya fue calculado: devuelve cache[x]  (O(1))
  → si no: calcula f(x), guarda en cache, devuelve
```
**Cuándo usar:**
- Funciones puras con resultados caros (llamadas a API, cómputos pesados).
- Funciones que se llaman repetidamente con los mismos valores.
- Fibonacci recursivo clásico: sin memo O(2ⁿ), con memo O(n).

**Cuándo NO usar:**
- Funciones con efectos colaterales — la cache puede retornar datos stale.
- Funciones con argumentos de tipo objeto (sin serialización la key no funciona).

### [F-29] Memoization en TypeScript y Clojure
@tipo: ejemplo-codigo
# Implementación y uso real
```typescript
// Implementación simple para funciones de 1 argumento
const memoize = <T, R>(fn: (arg: T) => R): ((arg: T) => R) => {
  const cache = new Map<T, R>();
  return (arg: T): R => {
    if (cache.has(arg)) return cache.get(arg)!;
    const result = fn(arg);
    cache.set(arg, result);
    return result;
  };
};

// Caso real: lookup de configuración (costoso de parsear)
const getConfig = memoize((env: string) => parseEnvConfig(env));
getConfig("production");  // parseEnvConfig corre una vez
getConfig("production");  // desde cache
```
```clojure
;; memoize nativo en Clojure
(defn fetch-user [id]
  (Thread/sleep 100)   ; simula latencia
  {:id id :name (str "User-" id)})

(def fetch-user-cached (memoize fetch-user))

(fetch-user-cached 42)  ; llama a fetch-user
(fetch-user-cached 42)  ; desde cache, instantáneo
```

### [F-30] Lazy sequences en Clojure
@tipo: concepto
# Evaluación perezosa
Una lazy sequence **no calcula sus elementos** hasta que se necesitan.
```clojure
;; range infinita — no explota memoria
(def naturals (range))   ; 0, 1, 2, 3, ... infinito

;; Tomar solo lo que necesito
(take 5 naturals)        ;→ (0 1 2 3 4)
(take 5 (filter even? naturals))  ;→ (0 2 4 6 8)
```
**Por qué importa:**
- Procesar datos en streaming sin cargar todo en memoria.
- Modelar secuencias potencialmente infinitas de forma natural.
- Componer transformaciones sin evaluar cada paso por separado.

```clojure
;; Pipeline sobre stream de logs (infinito en producción)
(->> (read-log-stream)
     (filter #(= :error (:level %)))
     (map :message)
     (take 100))     ; solo los primeros 100 errores
```
- Sin lazy: cargar todos los logs en memoria antes de filtrar.
- Con lazy: procesar 1 elemento a la vez hasta completar `take`.

### [F-31] DSLs pequeñas con HOF en Clojure
@tipo: ejemplo-codigo
# Mini-DSL de validación declarativa
```clojure
;; Reglas expresadas como datos
(def user-rules
  [{:field :name  :pred #(seq %)           :msg "nombre requerido"}
   {:field :email :pred #(re-matches #".+@.+\..+" %) :msg "email inválido"}
   {:field :age   :pred #(>= % 18)         :msg "debe ser mayor de edad"}])

;; Motor genérico: aplica las reglas a cualquier mapa
(defn validate [rules data]
  (->> rules
       (map (fn [{:keys [field pred msg]}]
              (when-not (pred (get data field))
                {:field field :error msg})))
       (remove nil?)))

;; Uso
(validate user-rules {:name "" :email "x" :age 16})
;; → ({:field :name,  :error "nombre requerido"}
;;    {:field :email, :error "email inválido"}
;;    {:field :age,   :error "debe ser mayor de edad"})
```
- Las reglas son **datos**, no código — se pueden serializar, modificar, extender.
- El motor de validación es genérico — sirve para cualquier entidad.
- Patrón: *data-driven programming* — la lógica vive en los datos.

### [F-32] Comparación Clojure vs TypeScript
@tipo: concepto
# Los mismos patrones, distinta sintaxis
| Patrón | Clojure | TypeScript |
|---|---|---|
| Pipeline | `->>` thread macro | `pipe(...fns)` |
| Mapa | `(map f xs)` | `xs.map(f)` |
| Filtrado | `(filter pred xs)` | `xs.filter(pred)` |
| Reducción | `(reduce f acc xs)` | `xs.reduce(f, acc)` |
| Partial | `(partial f a)` | `(b) => f(a, b)` |
| Lazy | `(range)`, `(lazy-seq ...)` | generators `function*` |
| TCO | `recur` garantizado | manual / trampolining |
| Datos | mapas, vectores, listas | objetos, arrays |

**Clave:** los patrones son tranferibles. Si entendés uno, el otro es sintaxis.
Clojure aporta claridad conceptual; TypeScript aporta tipado estático.

---
## BLOQUE 4 — Taller y cierre (20 min)

### [F-33] Consigna del taller
@tipo: actividad
# Taller: pipeline funcional completo
**Contexto:** una API que recibe datos de registro de usuarios.
**Objetivo:** construir un pipeline funcional sin mutaciones ni try/catch.

**Parte A — TypeScript:**
1. Definir `type FormData = { name, email, password, age }`.
2. Implementar 3 validators que devuelvan `Result<FormData, string>`.
3. Componer los validators con `pipe` o `reduce`.
4. En el handler: manejar el `Result` sin excepciones.

**Parte B — Clojure:**
1. Definir `user-rules` como vector de mapas `{:field :pred :msg}`.
2. Implementar motor `validate` que devuelva todos los errores.
3. Agregar `memoize` a una función de lookup costosa.
4. Usar `->>` para componer el pipeline completo.

**Comparación final:** mostrar las soluciones lado a lado y detectar diferencias reales.

### [F-34] Checklist de patrones aprendidos
@tipo: resumen
# Lo que podés hacer ahora
- ✅ Escribir funciones puras testeables (sin efectos).
- ✅ Componer transformaciones con `pipe` / `->>`.
- ✅ Factorizar con `partial` y `curry`.
- ✅ Modelar errores con `Result<T, E>` sin excepciones.
- ✅ Construir middleware composable como HOF.
- ✅ Implementar recursión de cola con acumulador.
- ✅ Evitar recómputo con `memoize`.
- ✅ Usar lazy sequences para procesamiento eficiente.
- ✅ Leer y escribir código Clojure con `->>`, `map`, `filter`, `recur`.

### [F-35] ¿Cuándo aplicar estos patrones?
@tipo: concepto
# Guía práctica de adopción
**Pensá en funcional cuando:**
- Necesitás transformar datos sin mutar el original → HOF, `map/filter/reduce`.
- Tenés lógica que puede fallar → `Result` en lugar de throw.
- Querés construir handlers/validators configurables → `partial`, `curry`.
- Necesitás encadenar operaciones sobre datos → `pipe`.
- Una función costosa se llama muchas veces con mismos args → `memoize`.
- Procesás streams grandes → lazy sequences.

**No forzar FP cuando:**
- El estado mutable local es claro y acotado (ej: buffer interno de una clase).
- La lógica es UI-event-heavy y el modelo reactivo es más natural.

### [F-36] Cierre y nexo con los próximos temas
@tipo: resumen
# Resumen y continuidad
**Hoy establecimos:**
- Funciones como valores → base de toda la FP.
- Composición como diseño → `pipe`, `->>`.
- `Result` como protocolo → errores tipados sin excepciones.
- Recursión de cola → iteración sin estado mutable ni stack overflow.

**Próximos pasos:**
- **Tema 05:** Mónadas en TypeScript — `Result` que estudiamos hoy es la mónada `Either`.
- **Tema 06:** Efectos y IO — cómo manejar side effects de forma disciplinada.
- **Proyecto:** aplicar estos patrones al pipeline del proyecto de cursada.

> "Un programa funcional es una colección de transformaciones de datos.  
> No ejecuta pasos — *describe* qué debe suceder." — Rich Hickey
