## PORTADA

---

### [F-01] Portada

@tipo: portada
@imagen: background
@prompt-imagen: fondo oscuro abstracto con cadenas de funciones conectadas por flechas luminosas, cajas envolventes translúcidas que representan contextos monádicos, tonos azul profundo y violeta, estilo académico-tecnológico

# Mónadas en TypeScript

Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
Tema 05 · Módulo II

Una **mónada** es un tipo con dos operaciones:
- `of` / `return`: meter un valor en el contexto
- `flatMap` / `bind` / `>>=`: encadenar una función que produce otro contexto

---

### [F-07] Analogía del contenedor

---

## BLOQUE 1 — Motivación: ¿por qué mónadas?

---

### [F-02] El problema del encadenamiento

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de tres operaciones conectadas en cadena, cada una con una bifurcación "éxito/fallo", los caminos de fallo se multiplican en un árbol caótico, estilo técnico limpio

# ¿Qué pasa cuando encadenamos operaciones que pueden fallar?

## El problema real

- Obtener un usuario → su dirección → su código postal
- Cada paso puede devolver `null` o fallar
- El código defensivo se vuelve un `if/else` anidado inmanejable

---

### [F-03] Encadenamiento roto — TypeScript

@tipo: codigo
@imagen: none

# El infierno de los `null` en TypeScript

```typescript
function getPostalCode(userId: number): string | null {
  const user = findUser(userId);
  if (user === null) return null;

  const address = getAddress(user);
  if (address === null) return null;

  const postalCode = getPostalCode(address);
  if (postalCode === null) return null;

  return postalCode;
}
// 3 operaciones → 3 guardas → complejidad crece linealmente
```

---

### [F-04] Encadenamiento roto — Clojure

@tipo: codigo
@imagen: none

# El infierno de `when-let` en Clojure

```clojure
(defn get-postal-code [user-id]
  (when-let [user (find-user user-id)]
    (when-let [address (get-address user)]
      (when-let [postal (get-postal-code address)]
        postal))))
;; Anidamiento crece con cada operación
;; Y si queremos saber *por qué* falló... no podemos
```

---

### [F-05] Mismo problema, dos lenguajes

@tipo: tabla-comparativa
@imagen: none

# El patrón es el mismo

| Aspecto | TypeScript | Clojure |
|---|---|---|
| Valor ausente | `null` / `undefined` | `nil` |
| Guardia | `if (x === null) return null` | `(when-let [x ...] ...)` |
| Anidamiento | Crece linealmente | Crece linealmente |
| Razón del fallo | Perdida (solo `null`) | Perdida (solo `nil`) |
| Solución necesaria | Una abstracción que encadene | Una abstracción que encadene |

---

### [F-06] De `map` a `flatMap` — la intuición

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama: una caja Maybe contiene otra caja Maybe (map produce anidamiento), flecha hacia abajo muestra flatMap que aplana a una sola caja, estilo educativo con colores azul y verde

# ¿Por qué `map` no alcanza?

## El problema del doble envoltorio

- `map` sobre `Maybe<User>` con función `User → Maybe<Address>` produce `Maybe<Maybe<Address>>`
- Necesitamos una operación que **aplique y aplane**: eso es `flatMap` / `bind`

## Definición de trabajo

Una **mónada** es un tipo con dos operaciones:
- `of` / `return`: meter un valor en el contexto
- `flatMap` / `bind` / `>>=`: encadenar una función que produce otro contexto

---

### [F-07] Analogía del contenedor

@tipo: diagrama
@imagen: content
@prompt-imagen: tres contenedores translúcidos etiquetados Maybe, Either, IO; flechas muestran "of" empaquetando un valor y "flatMap" abriendo-transformando-reempaquetando, estilo educativo infográfico

# `of` envuelve — `flatMap` abre, transforma, reenvuelve

## Flujo monádico

1. `of(valor)` → mete el valor en la caja
2. `flatMap(f)` → abre la caja, aplica `f`, devuelve una nueva caja
3. La caja decide qué hacer si está vacía o tiene error

---

## BLOQUE 2 — Maybe: la mónada de la opcionalidad

---

### [F-08] Maybe en TypeScript — Definición

@tipo: codigo
@imagen: none

# `Maybe<T>` en TypeScript

```typescript
type Maybe<T> =
  | { tag: 'Just'; value: T }
  | { tag: 'Nothing' };

const just = <T>(value: T): Maybe<T> =>
  ({ tag: 'Just', value });

const nothing = <T>(): Maybe<T> =>
  ({ tag: 'Nothing' });
```

- Tagged union discriminada por `tag`
- El compilador fuerza manejar ambos casos

---

### [F-09] Maybe en TypeScript — `of`, `map`, `flatMap`

@tipo: codigo
@imagen: none

# Operaciones monádicas de `Maybe<T>`

```typescript
const of = <T>(value: T): Maybe<T> => just(value);

const map = <T, U>(m: Maybe<T>, f: (x: T) => U): Maybe<U> =>
  m.tag === 'Just' ? just(f(m.value)) : nothing();

const flatMap = <T, U>(m: Maybe<T>, f: (x: T) => Maybe<U>): Maybe<U> =>
  m.tag === 'Just' ? f(m.value) : nothing();
```

- `map`: transforma el valor interno sin cambiar el contexto
- `flatMap`: aplica función que ya devuelve `Maybe<U>` → aplana

---

### [F-10] Maybe en TypeScript — Pipeline completo

@tipo: codigo
@imagen: none

# Pipeline con `Maybe` — sin un solo `if/null`

```typescript
type User    = { name: string; addressId: number };
type Address = { street: string; postalCode: string };

const findUser    = (id: number): Maybe<User>    => /* ... */;
const getAddress  = (u: User): Maybe<Address>    => /* ... */;
const getPostal   = (a: Address): Maybe<string>  => just(a.postalCode);

// Pipeline monádico
const postalCode: Maybe<string> =
  flatMap(
    flatMap(findUser(1), getAddress),
    getPostal
  );
// Si cualquier paso devuelve Nothing → todo el pipeline devuelve Nothing
// Sin if, sin null checks, sin anidamiento
```

---

### [F-11] Maybe en Clojure — idiomático con `some->`

@tipo: codigo
@imagen: none

# Maybe implícito: `some->` en Clojure

```clojure
;; nil como ausencia — idiomático en Clojure
(defn find-user [id]
  (get users-db id))       ; nil si no existe

(defn get-address [user]
  (get addresses-db (:address-id user)))

(defn get-postal [address]
  (:postal-code address))

;; Pipeline: some-> corta en el primer nil
(some-> 1
        find-user
        get-address
        get-postal)
;; => "9410" o nil — sin when-let anidados
```

- `some->` es un **Maybe implícito**: threading que corta en `nil`
- No tipado, no envuelve — pragmático y conciso

---

### [F-12] Maybe en Clojure — explícito con `cats`

@tipo: codigo
@imagen: none

# Maybe explícito: `cats/maybe` en Clojure

```clojure
(require '[cats.monad.maybe :as m])
(require '[cats.core :as mc])

;; Constructores
(m/just 42)     ;=> #<Just 42>
(m/nothing)     ;=> #<Nothing>

;; Pipeline con mlet (do-notation para mónadas)
(mc/mlet [user    (find-user-m 1)       ; Maybe<User>
          address (get-address-m user)   ; Maybe<Address>
          postal  (get-postal-m address)]; Maybe<String>
  (mc/return postal))

;; Equivalente a flatMap encadenado:
(mc/bind (find-user-m 1)
  (fn [user]
    (mc/bind (get-address-m user)
      (fn [address]
        (get-postal-m address)))))
```

---

### [F-13] Maybe — `some->` vs `cats/maybe`

@tipo: concepto-abstracto
@imagen: none

# ¿Para qué wrappear si `nil` ya existe?

## `some->` = Maybe implícito

- Clojure ya tiene `nil` como valor universal de ausencia
- `some->` corta automáticamente — cero ceremonia

## `cats/maybe` = Maybe explícito

- Envuelve en `Just`/`Nothing` como en TypeScript
- Habilita `mlet`, composición formal, leyes verificables
- Precio: boilerplate en un lenguaje que no lo necesita

**Criterio**: `some->` para código de producción; `cats/maybe` para enseñar el patrón

---

### [F-14] Comparativa Maybe — TS vs Clojure

@tipo: tabla-comparativa
@imagen: none

# Maybe: TypeScript vs Clojure

| Aspecto | TypeScript | Clojure |
|---|---|---|
| Representación | Tagged union `Just/Nothing` | `nil` nativo o `cats/maybe` |
| Type safety | Compilador fuerza pattern match | En runtime; no fuerza |
| Encadenamiento | `.flatMap(fn)` / pipe | `some->` o `(mc/bind v f)` |
| Ergonomía | Verboso pero seguro | Conciso pero sin red de tipos |
| Idiomático | Sí (fp-ts `Option`, Effect) | `some->` sí; `cats` nicho |
| Cuándo usar | Siempre que haya opcionalidad | `some->` por defecto |

---

## BLOQUE 3 — Either: la mónada del error tipado

---

### [F-15] Either en TypeScript — Definición

@tipo: codigo
@imagen: none

# `Either<E, T>` en TypeScript

```typescript
type Either<E, T> =
  | { tag: 'Left';  error: E }
  | { tag: 'Right'; value: T };

const left = <E, T>(error: E): Either<E, T> =>
  ({ tag: 'Left', error });

const right = <E, T>(value: T): Either<E, T> =>
  ({ tag: 'Right', value });
```

- `Right` = camino feliz (valor)
- `Left` = camino de error (tipado)
- Convención: "right is right" (correcto)

---

### [F-16] Either en TypeScript — Operaciones

@tipo: codigo
@imagen: none

# Operaciones monádicas de `Either<E, T>`

```typescript
const of = <E, T>(value: T): Either<E, T> => right(value);

const map = <E, T, U>(
  m: Either<E, T>, f: (x: T) => U
): Either<E, U> =>
  m.tag === 'Right' ? right(f(m.value)) : m;

const flatMap = <E, T, U>(
  m: Either<E, T>, f: (x: T) => Either<E, U>
): Either<E, U> =>
  m.tag === 'Right' ? f(m.value) : m;
```

- `flatMap` sobre `Left` propaga el error sin ejecutar `f`
- El tipo `E` del error se preserva en toda la cadena

---

### [F-17] Either en TypeScript — Validador de formulario

@tipo: codigo
@imagen: none

# Pipeline de validación con `Either`

```typescript
type ValidationError = { field: string; message: string };

const validateName = (name: string): Either<ValidationError, string> =>
  name.length >= 2
    ? right(name)
    : left({ field: 'name', message: 'Mínimo 2 caracteres' });

const validateEmail = (email: string): Either<ValidationError, string> =>
  email.includes('@')
    ? right(email)
    : left({ field: 'email', message: 'Email inválido' });

const validateAge = (age: number): Either<ValidationError, number> =>
  age >= 18
    ? right(age)
    : left({ field: 'age', message: 'Debe ser mayor de edad' });

// Pipeline: falla en la PRIMERA validación inválida
const validateForm = (name: string, email: string, age: number) =>
  flatMap(validateName(name), validName =>
    flatMap(validateEmail(email), validEmail =>
      map(validateAge(age), validAge =>
        ({ name: validName, email: validEmail, age: validAge })
      )
    )
  );
```

---

### [F-18] Either vs try/catch

@tipo: tabla-comparativa
@imagen: none

# Either vs try/catch — dos filosofías

| Aspecto | `try/catch` | `Either<E, T>` |
|---|---|---|
| Flujo de error | Implícito (salta stack frames) | Explícito (dato en el tipo) |
| Tipado del error | `unknown` / `any` | `E` es genérico verificable |
| Composición | No compone (rompe el pipeline) | `flatMap` compone naturalmente |
| Exhaustividad | El compilador no verifica | `switch` sobre `tag` es exhaustivo |
| Cuándo preferir | Errores verdaderamente excepcionales | Errores esperados del dominio |

---

### [F-19] Either en Clojure — con `cats`

@tipo: codigo
@imagen: none

# Either en Clojure con `cats`

```clojure
(require '[cats.monad.either :as e])
(require '[cats.core :as mc])

;; Constructores
(e/right "dato válido")   ;=> #<Right "dato válido">
(e/left "error: vacío")   ;=> #<Left "error: vacío">

;; Validaciones
(defn validate-name [name]
  (if (>= (count name) 2)
    (e/right name)
    (e/left {:field :name :msg "Mínimo 2 caracteres"})))

(defn validate-email [email]
  (if (clojure.string/includes? email "@")
    (e/right email)
    (e/left {:field :email :msg "Email inválido"})))

;; Pipeline con mlet
(mc/mlet [name  (validate-name "Ana")
          email (validate-email "ana@mail.com")]
  (mc/return {:name name :email email}))
;; => #<Right {:name "Ana", :email "ana@mail.com"}>
```

---

### [F-20] Either en Clojure — idiomático sin `cats`

@tipo: codigo
@imagen: none

# Either "manual" en Clojure — mapas de datos

```clojure
;; Convención de equipo: mapas con :ok / :error
(defn validate-name [name]
  (if (>= (count name) 2)
    {:ok name}
    {:error {:field :name :msg "Mínimo 2 chars"}}))

(defn validate-email [email]
  (if (clojure.string/includes? email "@")
    {:ok email}
    {:error {:field :email :msg "Email inválido"}}))

;; Encadenamiento manual — sin librería
(defn validate-form [name email]
  (let [r1 (validate-name name)]
    (if (:error r1)
      r1
      (let [r2 (validate-email email)]
        (if (:error r2)
          r2
          {:ok {:name (:ok r1) :email (:ok r2)}})))))

;; Funciona, pero:
;; - No hay flatMap genérico
;; - El anidamiento vuelve a crecer
;; - Es un Either reimplementado con menos ergonomía
```

---

### [F-21] Clojure: ¿datos simples o mónadas formales?

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: balanza con dos platillos: uno tiene un mapa Clojure con :ok/:error, el otro tiene una caja formal Either con Right/Left, estilo educativo infográfico

# Clojure y los errores: datos vs tipos

## Filosofía Clojure

- "Los datos son la interfaz universal"
- Un mapa `{:ok v}` / `{:error e}` es un Either de facto
- No se necesita librería para modelar éxito/fallo

## El precio de la informalidad

- Sin `flatMap` genérico, el encadenamiento es manual
- Sin tipos, el compilador no verifica exhaustividad
- Errores de convención (`:ok` vs `:result`) causan bugs silenciosos

## Criterio

TS: mónadas formales — el sistema de tipos las recompensa
Clojure: datos simples — la filosofía del lenguaje las desincentiva

---

### [F-22] Comparativa Either — TS vs Clojure

@tipo: tabla-comparativa
@imagen: none

# Either: TypeScript vs Clojure

| Aspecto | TypeScript | Clojure |
|---|---|---|
| Representación | Tagged union `Left/Right` | `cats/either` o mapa `{:ok/:error}` |
| Error tipado | `E` es un tipo genérico verificado | String, keyword o mapa — runtime |
| Encadenamiento | `flatMap` con tipo inferido | `mlet` (cats) o `let`+`if` manual |
| vs try/catch | Reemplaza completamente | Complementa (`ex-info` sigue siendo común) |
| Idiomático | Sí (fp-ts `Either`, Effect) | `cats` nicho; mapas convencionales más común |
| Exhaustividad | Compilador verifica | Programador verifica |

---

## BLOQUE 4 — IO, leyes monádicas y mónadas ocultas

---

### [F-23] IO en TypeScript — Definición

@tipo: codigo
@imagen: none

# `IO<T>` — la computación como valor

```typescript
type IO<T> = { run: () => T };

const ioOf = <T>(value: T): IO<T> =>
  ({ run: () => value });

const ioMap = <T, U>(io: IO<T>, f: (x: T) => U): IO<U> =>
  ({ run: () => f(io.run()) });

const ioFlatMap = <T, U>(io: IO<T>, f: (x: T) => IO<U>): IO<U> =>
  ({ run: () => f(io.run()).run() });
```

- `IO<T>` envuelve un efecto: nada se ejecuta hasta `.run()`
- Separa **qué hacer** de **cuándo hacerlo**

---

### [F-24] IO en TypeScript — Ejemplo

@tipo: codigo
@imagen: none

# Pipeline IO: leer → transformar → escribir

```typescript
const readLine: IO<string> =
  ({ run: () => prompt("Ingrese su nombre:") ?? "" });

const greet = (name: string): IO<string> =>
  ({ run: () => {
    const msg = `Hola, ${name.toUpperCase()}!`;
    console.log(msg);
    return msg;
  }});

// Composición: nada se ejecuta al definir el pipeline
const program: IO<string> = ioFlatMap(readLine, greet);

// Ejecución: un solo punto de entrada con efectos
program.run();
```

- Todo el programa es una descripción pura de efectos
- Los efectos se ejecutan solo al final: `program.run()`
- IO es puro hasta el borde del sistema

---

### [F-25] IO en Clojure — thunks y `delay`

@tipo: codigo
@imagen: none

# IO en Clojure: ¿necesaria?

```clojure
;; Clojure es impuro por defecto — los efectos son directos
(println "Hola")  ; efecto inmediato, sin wrapper

;; Pero podemos diferir con closures (thunks)
(def read-input
  (fn [] (read-line)))  ; no se ejecuta hasta invocar

;; O con delay (evaluación lazy de un solo uso)
(def greeting
  (delay (str "Hola, " (read-line))))

@greeting  ; force: ejecuta y cachea resultado

;; core.async: composición de efectos asincrónicos
(require '[clojure.core.async :refer [go <! >! chan]])
(def c (chan))
(go (>! c (str "Hola, " (<! (go (read-line))))))
```

- Clojure **no necesita IO como wrapper obligatorio**
- `delay` y closures cumplen el rol de diferir efectos
- `core.async` compone efectos asincrónicos por canales

---

### [F-26] Comparativa IO — TS vs Clojure

@tipo: tabla-comparativa
@imagen: none

# IO: TypeScript vs Clojure

| Aspecto | TypeScript | Clojure |
|---|---|---|
| Necesidad | Alta — separa puro de impuro | Baja — el lenguaje es pragmáticamente impuro |
| Representación | `{ run: () => T }` | Thunks, `delay`, closures |
| Ejecución diferida | `.run()` explícito | `@delay` o `(force d)` |
| Composición de efectos | `ioFlatMap` | `core.async` / `go` blocks |
| Filosofía | Pureza por tipo | Control por convención |

---

### [F-27] Las tres leyes monádicas

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: tres ecuaciones matemáticas enmarcadas como leyes fundamentales, con flechas de verificación verde a su lado, estilo pizarra académica con tiza blanca sobre fondo oscuro

# Las tres leyes que toda mónada debe cumplir

## 1. Identidad izquierda

`of(a).flatMap(f) === f(a)`

Envolver y aplicar = aplicar directamente

## 2. Identidad derecha

`m.flatMap(of) === m`

Envolver lo que ya está envuelto no cambia nada

## 3. Asociatividad

`m.flatMap(f).flatMap(g) === m.flatMap(x => f(x).flatMap(g))`

El orden de agrupación no importa

---

### [F-28] Leyes verificadas en TypeScript

@tipo: codigo
@imagen: none

# Verificación con tests — TypeScript

```typescript
// 1. Identidad izquierda: of(a).flatMap(f) === f(a)
const f = (x: number): Maybe<number> => just(x * 2);
const a = 5;
console.assert(
  JSON.stringify(flatMap(of(a), f)) === JSON.stringify(f(a)),
  "Ley 1 — identidad izquierda"
);

// 2. Identidad derecha: m.flatMap(of) === m
const m = just(10);
console.assert(
  JSON.stringify(flatMap(m, of)) === JSON.stringify(m),
  "Ley 2 — identidad derecha"
);

// 3. Asociatividad:
//    m.flatMap(f).flatMap(g) === m.flatMap(x => f(x).flatMap(g))
const g = (x: number): Maybe<string> => just(`val: ${x}`);
const lhs = flatMap(flatMap(m, f), g);
const rhs = flatMap(m, x => flatMap(f(x), g));
console.assert(
  JSON.stringify(lhs) === JSON.stringify(rhs),
  "Ley 3 — asociatividad"
);
```

---

### [F-29] Leyes verificadas en Clojure

@tipo: codigo
@imagen: none

# Verificación en el REPL — Clojure

```clojure
(require '[cats.monad.maybe :as m])
(require '[cats.core :as mc])

;; 1. Identidad izquierda: (bind (return a) f) == (f a)
(let [f (fn [x] (m/just (* x 2)))
      a 5]
  (assert (= (mc/bind (mc/return m/context a) f)
             (f a))))

;; 2. Identidad derecha: (bind m return) == m
(let [mv (m/just 10)]
  (assert (= (mc/bind mv mc/return)
             mv)))

;; 3. Asociatividad:
;;    (bind (bind m f) g) == (bind m (fn [x] (bind (f x) g)))
(let [mv (m/just 10)
      f  (fn [x] (m/just (* x 2)))
      g  (fn [x] (m/just (str "val: " x)))]
  (assert (= (mc/bind (mc/bind mv f) g)
             (mc/bind mv (fn [x] (mc/bind (f x) g))))))
;; Las tres pasan ✓
```

---

### [F-30] Mónadas escondidas — `Promise`

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: un paquete de regalo que al abrirse revela un símbolo de mónada, con etiquetas Promise, Array, some->, estilo revelación visual educativa

# `Promise` es (casi) una mónada

```typescript
// Promise.resolve = of
const p = Promise.resolve(42);

// .then = flatMap (cuando devolvemos otra Promise)
p.then(x => Promise.resolve(x * 2))
 .then(x => console.log(x));  // 84

// Diferencia: Promise es eager (se ejecuta al crearla)
// Una mónada IO es lazy (se ejecuta con .run())
// Promise aplana automáticamente — no existe Promise<Promise<T>>
```

---

### [F-31] Mónadas escondidas — más ejemplos

@tipo: tabla
@imagen: none

# Patrones monádicos en APIs existentes

| API | `of` equivalente | `flatMap` equivalente | Efecto |
|---|---|---|---|
| `Promise<T>` | `Promise.resolve(v)` | `.then(f)` | Asincronía |
| `Array<T>` | `[v]` | `.flatMap(f)` | No-determinismo |
| `?.` (optional chaining) | valor presente | `x?.prop` | Opcionalidad |
| `some->` (Clojure) | valor no-nil | threading que corta en nil | Maybe implícito |
| `for` (Clojure) | `[v]` | comprehension con `:let` | List monad |
| `go` blocks | canal con valor | `<!` dentro de `go` | Async/IO |

---

### [F-32] Jerarquía: Functor → Monad

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama de capas concéntricas: capa externa "Functor (map)", capa media "Applicative (ap)", capa interna "Monad (flatMap/bind)", cada capa con un color distinto (azul, verde, violeta), estilo académico

# De Functor a Monad

## Jerarquía de abstracciones

- **Functor**: tiene `map` — transforma el valor dentro del contexto
- **Applicative**: tiene `ap` — aplica función envuelta a valor envuelto
- **Monad**: tiene `flatMap`/`bind` — encadena operaciones que producen contexto

## En Haskell (contraste notacional)

```haskell
class Functor f where
  fmap :: (a -> b) -> f a -> f b

class Functor f => Applicative f where
  pure :: a -> f a
  (<*>) :: f (a -> b) -> f a -> f b

class Applicative m => Monad m where
  return :: a -> m a
  (>>=) :: m a -> (a -> m b) -> m b
```

> No necesitamos aprender Haskell — pero toda la terminología viene de ahí

---

## BLOQUE 5 — Ecosistemas, IA y reflexión final

---

### [F-33] fp-ts y Effect — ecosistema TS

@tipo: codigo
@imagen: none

# Ecosistema industrial TypeScript

```typescript
// fp-ts — Option (= Maybe)
import { pipe } from 'fp-ts/function';
import * as O from 'fp-ts/Option';

const result = pipe(
  O.fromNullable(findUser(1)),
  O.flatMap(u => O.fromNullable(getAddress(u))),
  O.map(a => a.postalCode),
  O.getOrElse(() => "N/A")
);

// Effect — nueva generación
import { Effect, pipe } from 'effect';

const program = pipe(
  Effect.tryPromise(() => fetch('/api/user/1')),
  Effect.flatMap(res => Effect.tryPromise(() => res.json())),
  Effect.map(user => user.name)
);
```

- fp-ts: 2019+ — maduro, basado en Haskell
- Effect: 2023+ — do-notation, concurrencia, tipado de errores

---

### [F-34] Ecosistema Clojure — cats y más

@tipo: codigo
@imagen: none

# Ecosistema monádico en Clojure

```clojure
;; cats (funcool) — la librería estándar de mónadas
(require '[cats.core :as mc])
(require '[cats.monad.maybe :as m])
(require '[cats.monad.either :as e])

;; manifold — async con deferred (mónada de promesas)
(require '[manifold.deferred :as d])
(def resultado (d/chain (d/future (fetch-data))
                        parse-json
                        extract-name))

;; missionary — reactive streams con composición monádica
;; (mencionamos, no profundizamos)
```

- `cats`: lo más cercano a fp-ts en Clojure
- `manifold`: promesas composicionales (usado en producción: Aleph server)
- Adopción: menor que fp-ts/Effect — Clojure prefiere datos simples

---

### [F-35] Pipeline IA con mónadas

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de flujo de un pipeline de IA: prompt → LLM → parseo → validación → respuesta, cada paso dentro de una caja Either con flechas flatMap entre cajas, estilo técnico moderno

# Mónadas para IA: pipelines de prompting seguros

## El pipeline

`prompt → LLM → parseo → validación → respuesta`

Cada paso puede fallar: prompt malformado, LLM timeout, JSON inválido, validación rechazada.

## En TypeScript: `Either<Error, T>`

```typescript
const pipeline =
  flatMap(buildPrompt(input), prompt =>
    flatMap(callLLM(prompt), raw =>
      flatMap(parseJSON(raw), parsed =>
        validateResponse(parsed)
      )
    )
  );
```

## En Clojure: `go` + mapas `{:ok/:error}`

```clojure
(go
  (let [prompt (<! (build-prompt input))
        raw    (when (:ok prompt) (<! (call-llm (:ok prompt))))
        parsed (when raw (parse-json raw))]
    (if parsed
      (validate-response parsed)
      {:error "Pipeline falló"})))
```

---

### [F-36] Reflexión: ¿mónadas formales en Clojure?

@tipo: socratica
@imagen: none

# Discusión: ¿todo debería ser monádico?

## Preguntas para la clase

1. Si el compilador no te obliga a usar mónadas, ¿por qué hacerlo?
2. ¿`some->` y mapas `{:ok/:error}` son "suficiente mónada" para Clojure?
3. ¿En qué lenguaje es más natural usar mónadas explícitas? ¿Por qué?

## Tesis contrapuestas

- **TS**: el sistema de tipos *recompensa* las mónadas — inferencia, autocompletado, errores en compilación
- **Clojure**: la filosofía de "datos simples" hace que las mónadas formales sean menos idiomáticas

## Conclusión provisoria

> El concepto es universal; la forma de expresarlo depende del lenguaje.
> Usá mónadas cuando el error o efecto es parte explícita del dominio. No para sumar dos números.

---

### [F-37] Síntesis: 3 mónadas × 2 lenguajes

@tipo: tabla-comparativa
@imagen: none

# Mapa comparativo final

| Mónada | Efecto | TypeScript | Clojure |
|---|---|---|---|
| `Maybe` | Opcionalidad | Tagged union `Just/Nothing` | `nil` + `some->` / `cats/maybe` |
| `Either` | Error tipado | Tagged union `Left/Right` | `cats/either` / mapa `{:ok/:error}` |
| `IO` | Efectos laterales | `{ run: () => T }` | Thunks / `delay` / `core.async` |

## Patrón común

Todas comparten: `of` (envolver) + `flatMap` (encadenar) + leyes

## Diferencia esencial

- TS: mónadas como **tipos** que el compilador verifica
- Clojure: patrones monádicos como **convenciones** que el programador respeta

---

### [F-38] ¿Cuándo usar cuál?

@tipo: tabla
@imagen: none

# Guía de decisión

| Situación | Mónada | ¿Por qué? |
|---|---|---|
| Valor puede no existir (búsqueda, campo opcional) | `Maybe` | Elimina null checks |
| Operación puede fallar con mensaje tipado | `Either` | Error explícito en el tipo |
| Operación tiene efectos (I/O, red, consola) | `IO` | Separa descripción de ejecución |
| Operación asíncrona | `Promise` (TS) / `core.async` (Clj) | Efecto temporal |
| Múltiples resultados posibles | `Array.flatMap` / `for` (Clj) | No-determinismo |

---

## CIERRE

---

### [F-39] Recapitulación visual

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama jerárquico: arriba "Problema → encadenamiento de operaciones con efectos", abajo tres ramas Maybe/Either/IO, cada rama con sub-ramas TS y Clojure, estilo mapa conceptual limpio con conexiones

# Lo que vimos hoy

1. **Problema**: encadenar operaciones que pueden fallar, ser nulas, o tener efectos
2. **Solución**: un patrón con `of` + `flatMap` → mónada
3. **Maybe**: opcionalidad (TS: `Just/Nothing` | Clj: `nil`/`some->`)
4. **Either**: error tipado (TS: `Left/Right` | Clj: `cats/either` o mapas)
5. **IO**: efectos diferidos (TS: `{ run }` | Clj: thunks/delay)
6. **Leyes**: identidad izquierda, identidad derecha, asociatividad
7. **El concepto es universal** — la forma de expresarlo depende del lenguaje

---

### [F-40] Preguntas clave

@tipo: socratica
@imagen: none

# Preguntas para verificar comprensión

1. ¿Cuándo usar Maybe vs Either?
2. ¿Por qué `flatMap` y no solo `map`?
3. ¿Clojure necesita mónadas formales o le alcanza con `some->` y mapas?
4. ¿`Promise.then` cumple las tres leyes monádicas?
5. ¿Cuál de las tres leyes garantiza que podemos refactorizar el orden de los `flatMap`?

---

### [F-41] Adelanto Tema 06

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: logo estilizado de Python con engranajes de IA y flechas funcionales, fondo gradiente violeta a azul, estilo tech moderno

# Próximamente: FP en Python y ecosistema IA

- Funcional en Python: `map`, `filter`, `reduce`, `functools`, decoradores
- Dataclasses inmutables y pattern matching (3.10+)
- Pipeline funcional para IA: `langchain`, `pydantic`, monads en Python
- Contraste: TS (tipos fuertes) vs Clojure (datos simples) vs Python (pragmático)

---

### [F-42] Cierre

@tipo: cierre
@imagen: background
@prompt-imagen: fondo oscuro con un diagrama luminoso de flatMap conectando tres cajas monádicas, con texto "of → flatMap → resultado" en tipografía limpia, estilo profesional y elegante

# Mónadas: el patrón más poderoso que ya estaban usando

> `Promise.then`, `Array.flatMap`, `some->`, `?.` — ya las conocían.
> Ahora saben por qué funcionan.

Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI
