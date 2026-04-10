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

### BLOQUE 1 — Fundamentos avanzados

#### Ejercicio 1 — Pipeline filter/map/reduce (TypeScript) — 3 pts
**Trazabilidad:** F-06, F-07, F-08 | **Archivo:** `typescript/src/ej01.ts`

Implementá dos funciones que procesan un array de órdenes usando un pipeline funcional:

- `filtrarActivasYSumar(ordenes: Orden[]): number` — Filtra las órdenes activas, extrae sus totales y los suma.
- `obtenerTotalesActivas(ordenes: Orden[]): number[]` — Filtra las activas y devuelve un array con sus totales.

**Ejemplo:**
```typescript
const ordenes = [
  { id: 1, cliente: "Ana", total: 120, categoria: "elect", activa: true },
  { id: 2, cliente: "Boris", total: 50, categoria: "ropa", activa: false },
  { id: 3, cliente: "Carla", total: 200, categoria: "elect", activa: true },
];
filtrarActivasYSumar(ordenes); // → 320
obtenerTotalesActivas(ordenes); // → [120, 200]
```

**Restricción:** No usar variables mutables (`let`, bucles `for`). Solo `filter`, `map`, `reduce`.

---

#### Ejercicio 2 — Composición con pipe y compose (TypeScript) — 5 pts
**Trazabilidad:** F-09 | **Archivo:** `typescript/src/ej02.ts`

Implementá las funciones de composición:

- `pipe(...fns): (x) => result` — Compone funciones de izquierda a derecha.
- `compose(...fns): (x) => result` — Compone funciones de derecha a izquierda.

**Ejemplo:**
```typescript
const inc = (x: number) => x + 1;
const doble = (x: number) => x * 2;

pipe(inc, doble)(3);      // → 8   (primero +1, luego ×2)
compose(inc, doble)(3);   // → 7   (primero ×2, luego +1)
pipe()(5);                // → 5   (sin funciones, identidad)
```

**Restricción:** Usar `reduce` / `reduceRight` internamente.

---

#### Ejercicio 3 — Inmutabilidad (TypeScript) — 3 pts
**Trazabilidad:** F-05, F-10 | **Archivo:** `typescript/src/ej03.ts`

Implementá funciones que devuelven nuevos objetos sin modificar los originales:

- `cumpleanios(p: Persona): Persona` — Devuelve una nueva persona con `edad + 1`.
- `agregarHobby(p: Persona, hobby: string): Persona` — Devuelve una nueva persona con el hobby agregado al final.
- `actualizarNombre(p: Persona, nombre: string): Persona` — Devuelve una nueva persona con el nombre actualizado.

**Tipo dado:**
```typescript
type Persona = { readonly nombre: string; readonly edad: number; readonly hobbies: readonly string[] };
```

**Ejemplo:**
```typescript
const ana = { nombre: "Ana", edad: 28, hobbies: ["leer", "correr"] };
const ana29 = cumpleanios(ana);
ana29.edad;   // → 29
ana.edad;     // → 28 (intacto)
```

---

#### Ejercicio 4 — Pipeline con ->> (Clojure) — 3 pts
**Trazabilidad:** F-12 | **Archivo:** `clojure/src/tp04/ej04.clj`

Implementá funciones que usen el macro `->>` para procesar órdenes:

- `(total-activas ordenes)` — Filtra las activas, extrae `:total` y suma.
- `(nombres-activas ordenes)` — Filtra las activas y devuelve un vector con sus `:cliente`.

**Ejemplo:**
```clojure
(def ordenes [{:id 1 :cliente "Ana" :total 120 :activa? true}
              {:id 2 :cliente "Boris" :total 50 :activa? false}
              {:id 3 :cliente "Carla" :total 200 :activa? true}])
(total-activas ordenes)   ; => 320
(nombres-activas ordenes) ; => ["Ana" "Carla"]
```

---

#### Ejercicio 5 — Secuencias perezosas (Clojure) — 5 pts
**Trazabilidad:** F-11 | **Archivo:** `clojure/src/tp04/ej05.clj`

Implementá funciones que generen secuencias perezosas:

- `(primeros-n-pares n)` — Los primeros `n` números pares positivos (2, 4, 6...).
- `(fibonacci)` — Secuencia infinita de Fibonacci (0, 1, 1, 2, 3, 5, 8...).
- `(tomar-mientras-menor coll umbral)` — Toma elementos de `coll` mientras sean menores que `umbral`.

**Ejemplo:**
```clojure
(primeros-n-pares 4)          ; => (2 4 6 8)
(take 7 (fibonacci))          ; => (0 1 1 2 3 5 8)
(tomar-mientras-menor [1 3 5 7 2] 6) ; => (1 3 5)
```

**Restricción:** `fibonacci` debe ser lazy — no precomputar. Usar `lazy-seq` o `iterate`.

---

#### Ejercicio 6 — Colecciones persistentes (Clojure) — 3 pts
**Trazabilidad:** F-13 | **Archivo:** `clojure/src/tp04/ej06.clj`

Implementá funciones que demuestren inmutabilidad por diseño:

- `(agregar-al-vector v elem)` — Retorna un nuevo vector con `elem` al final.
- `(actualizar-mapa m k v)` — Retorna un nuevo mapa con la clave `k` asociada a `v`.
- `(combinar-mapas m1 m2)` — Retorna un nuevo mapa con todas las claves de ambos (m2 prevalece en conflictos).

**Ejemplo:**
```clojure
(agregar-al-vector [1 2 3] 4)                   ; => [1 2 3 4]
(actualizar-mapa {:a 1} :b 2)                    ; => {:a 1 :b 2}
(combinar-mapas {:a 1 :b 2} {:b 99 :c 3})        ; => {:a 1 :b 99 :c 3}
```

---

### BLOQUE 2 — Abstracciones y efectos

#### Ejercicio 7 — Algebraic Data Types (TypeScript) — 5 pts
**Trazabilidad:** F-14 | **Archivo:** `typescript/src/ej07.ts`

Definí el tipo suma `Shape` e implementá funciones de procesamiento:

- `type Shape = Circle | Rectangle | Triangle` (con discriminante `kind`)
- `area(s: Shape): number`
- `perimetro(s: Shape): number`
- `describir(s: Shape): string` — Retorna `"<kind>: area=X.XX"`.

**Ejemplo:**
```typescript
area({ kind: "circle", radius: 5 });         // → 78.5398...
perimetro({ kind: "rectangle", width: 4, height: 3 }); // → 14
describir({ kind: "triangle", base: 6, height: 4 });   // → "triangle: area=12.00"
```

---

#### Ejercicio 8 — Result<T, E> (TypeScript) — 6 pts
**Trazabilidad:** F-15, F-16 | **Archivo:** `typescript/src/ej08.ts`

El archivo provee el tipo `Result` y los constructores `ok`/`err`. Implementá:

- `mapResult(r, fn)` — Si `r` es ok, aplica `fn` al valor. Si es error, propaga.
- `flatMapResult(r, fn)` — Si `r` es ok, aplica `fn` (que retorna Result). Si es error, propaga.
- `dividir(a, b)` — Retorna `ok(a/b)` o `err("División por cero")`.

**Ejemplo:**
```typescript
mapResult(ok(10), x => x * 2);           // → { ok: true, value: 20 }
mapResult(err("fallo"), x => x * 2);     // → { ok: false, error: "fallo" }
flatMapResult(ok(10), x => dividir(x, 2)); // → { ok: true, value: 5 }
flatMapResult(ok(10), x => dividir(x, 0)); // → { ok: false, error: "División por cero" }
```

---

#### Ejercicio 9 — Maybe / Option (TypeScript) — 5 pts
**Trazabilidad:** F-17 | **Archivo:** `typescript/src/ej09.ts`

El archivo provee el tipo `Maybe` y los constructores `just`/`nothing`. Implementá:

- `mapMaybe(m, fn)` — Si hay valor, aplica `fn`. Si no, retorna nothing.
- `flatMapMaybe(m, fn)` — Si hay valor, aplica `fn` (que retorna Maybe). Si no, retorna nothing.
- `buscar(arr, predicado)` — Retorna `just(elemento)` del primero que cumple, o `nothing()`.

**Ejemplo:**
```typescript
mapMaybe(just(5), x => x * 2);           // → { some: true, value: 10 }
mapMaybe(nothing(), x => x * 2);         // → { some: false }
buscar([1,2,3], x => x > 2);             // → { some: true, value: 3 }
buscar([1,2,3], x => x > 10);            // → { some: false }
```

---

#### Ejercicio 10 — Errores como datos (Clojure) — 5 pts
**Trazabilidad:** F-18 | **Archivo:** `clojure/src/tp04/ej10.clj`

Implementá manejo de errores sin excepciones, usando mapas:

- `(dividir-seguro a b)` — Retorna `{:ok true :value resultado}` o `{:ok false :error "División por cero"}`.
- `(raiz-segura n)` — Retorna ok con `Math/sqrt` si n ≥ 0, o error `"Raíz de negativo"`.
- `(operar-cadena a b)` — Divide `a/b`, luego calcula la raíz del resultado. Propaga el primer error.

**Ejemplo:**
```clojure
(dividir-seguro 10 2)   ; => {:ok true :value 5}
(dividir-seguro 10 0)   ; => {:ok false :error "División por cero"}
(operar-cadena 100 4)   ; => {:ok true :value 5.0}  (√(100/4) = √25 = 5)
(operar-cadena 10 0)    ; => {:ok false :error "División por cero"}
(operar-cadena -100 1)  ; => {:ok false :error "Raíz de negativo"}
```

---

#### Ejercicio 11 — Transducer básico (Clojure) — 5 pts
**Trazabilidad:** F-19, F-20 | **Archivo:** `clojure/src/tp04/ej11.clj`

Implementá un transducer que procese órdenes:

- `xf-activas-totales` — Transducer (con `comp`) que filtra activas y extrae `:total`.
- `(sumar-activas-xf ordenes)` — Aplica `xf-activas-totales` con `transduce` y suma los totales.
- `(totales-activas-vec ordenes)` — Aplica el transducer con `into` para obtener un vector de totales.

**Ejemplo:**
```clojure
(sumar-activas-xf [{:total 100 :activa? true} {:total 50 :activa? false} {:total 200 :activa? true}])
; => 300
(totales-activas-vec [{:total 100 :activa? true} {:total 50 :activa? false}])
; => [100]
```

---

#### Ejercicio 12 — Transducer vs pipeline (Clojure) — 5 pts
**Trazabilidad:** F-21 | **Archivo:** `clojure/src/tp04/ej12.clj`

Implementá el mismo procesamiento de dos formas y verificá equivalencia:

- `(procesar-pipeline ordenes)` — Pipeline clásico con `->>`: filtrar activas con total > 100, extraer totales, sumar.
- `(procesar-transducer ordenes)` — Mismo resultado usando `transduce` con un transducer compuesto.
- `(totales-pipeline ordenes)` — Pipeline clásico: vector de totales de activas con total > 100.
- `(totales-transducer ordenes)` — Mismo resultado con `into` y transducer.

**Ejemplo:**
```clojure
(def datos [{:total 300 :activa? true} {:total 80 :activa? false}
            {:total 150 :activa? true} {:total 50 :activa? true}])
(procesar-pipeline datos)      ; => 450  (300 + 150)
(procesar-transducer datos)    ; => 450
(totales-pipeline datos)       ; => [300 150]
(totales-transducer datos)     ; => [300 150]
```

---

#### Ejercicio 13 — API genérica funcional (TypeScript) — 7 pts
**Trazabilidad:** F-22 | **Archivo:** `typescript/src/ej13.ts`

Implementá funciones genéricas que trabajen con `Result`:

- `chainResults<T>(initial: T, fns: Array<(v: T) => Result<T, string>>): Result<T, string>` — Encadena funciones, propagando el primer error.
- `traverseResults<T>(results: Result<T, string>[]): Result<T[], string>` — Si todos son ok, retorna ok con array. Si alguno es error, retorna el primer error.
- `filterOk<T>(results: Result<T, string>[]): T[]` — Extrae solo los valores de los ok.

**Ejemplo:**
```typescript
const inc = (x: number): Result<number, string> => ok(x + 1);
const doble = (x: number): Result<number, string> => ok(x * 2);
chainResults(3, [inc, doble]);  // → ok(8)  — (3+1)×2

traverseResults([ok(1), ok(2), ok(3)]); // → ok([1, 2, 3])
traverseResults([ok(1), err("x")]);     // → err("x")

filterOk([ok(1), err("x"), ok(3)]);     // → [1, 3]
```

---

#### Ejercicio 14 — Funciones de orden superior (TypeScript) — 5 pts
**Trazabilidad:** F-23 | **Archivo:** `typescript/src/ej14.ts`

Implementá HOFs que demuestren funciones como valores:

- `aplicarNVeces<T>(f: (x: T) => T, n: number): (x: T) => T` — Aplica `f` sobre el resultado `n` veces.
- `crearMultiplicador(factor: number): (x: number) => number` — Retorna función que multiplica por `factor`.
- `curry2<A, B, R>(f: (a: A, b: B) => R): (a: A) => (b: B) => R` — Convierte función de 2 args en curried.

**Ejemplo:**
```typescript
aplicarNVeces((x: number) => x * 2, 3)(1);  // → 8  (1→2→4→8)
crearMultiplicador(5)(7);                     // → 35
const sumar = curry2((a: number, b: number) => a + b);
sumar(3)(4); // → 7
```

---

### BLOQUE 3 — Concurrencia y efectos

#### Ejercicio 15 — core.async canales (Clojure) — 6 pts
**Trazabilidad:** F-26, F-27 | **Archivo:** `clojure/src/tp04/ej15.clj`

Implementá un pipeline de datos usando canales de `core.async`:

- `(pipeline-canal datos filtro-fn transformar-fn)` — Crea un canal de entrada y uno de salida. Un go-block productor pone los datos. Un go-block consumidor filtra con `filtro-fn` y transforma con `transformar-fn`. Retorna un **vector** con los resultados (recolección bloqueante).

**Ejemplo:**
```clojure
(pipeline-canal [1 2 3 4 5 6] even? #(* 2 %))
; => [4 8 12]  — filtra pares (2,4,6) y duplica

(pipeline-canal [10 -3 5 -7 20] pos? inc)
; => [11 6 21]  — filtra positivos y suma 1
```

**Pista:** Usá `>!` y `<!` dentro de go-blocks. Para recolectar, usá `<!!` (blocking take) fuera del go-block.

---

#### Ejercicio 16 — STM y transacciones (Clojure) — 6 pts
**Trazabilidad:** F-28 | **Archivo:** `clojure/src/tp04/ej16.clj`

Implementá un sistema bancario simple con STM:

- `(crear-banco cuentas-map)` — Recibe `{:ana 1000 :boris 500}`, retorna mapa `{:ana (ref 1000) :boris (ref 500)}`.
- `(saldo banco cuenta)` — Retorna el saldo actual de una cuenta (deref del ref).
- `(transferir banco origen destino monto)` — Transfiere `monto` de `origen` a `destino` dentro de `dosync`.
- `(total-banco banco)` — Suma todos los saldos (el invariante: el total nunca cambia).

**Ejemplo:**
```clojure
(def banco (crear-banco {:ana 1000 :boris 500}))
(total-banco banco)              ; => 1500
(transferir banco :ana :boris 200)
(saldo banco :ana)               ; => 800
(saldo banco :boris)             ; => 700
(total-banco banco)              ; => 1500 (invariante preservado)
```

---

#### Ejercicio 17 — async/await (TypeScript) — 5 pts
**Trazabilidad:** F-30, F-31 | **Archivo:** `typescript/src/ej17.ts`

Implementá funciones asíncronas que compongan Promises:

- `procesarLote<T, U>(items: T[], transformar: (item: T) => Promise<U>): Promise<U[]>` — Aplica `transformar` a cada item en paralelo con `Promise.all`.
- `filtrarAsync<T>(items: T[], predicado: (item: T) => Promise<boolean>): Promise<T[]>` — Filtra items evaluando el predicado asincrónicamente.

**Ejemplo:**
```typescript
await procesarLote([1,2,3], async x => x * 10);
// → [10, 20, 30]

await filtrarAsync([1,2,3,4,5], async x => x % 2 === 0);
// → [2, 4]
```

---

#### Ejercicio 18 — Separar efectos puros de I/O (TypeScript) — 5 pts
**Trazabilidad:** F-32 | **Archivo:** `typescript/src/ej18.ts`

Implementá la lógica **pura** de un sistema de descuentos, separada de los efectos:

- `calcularDescuento(precio: number, porcentaje: number): number` — Retorna el precio con descuento aplicado.
- `aplicarReglas(orden: Orden, reglas: Regla[]): OrdenConDescuento` — Aplica la primera regla cuya condición se cumple. Si ninguna aplica, descuento = 0.
- `generarResumen(ordenes: OrdenConDescuento[]): Resumen` — Agrega: total original, total con descuento, ahorro total, cantidad de órdenes.

**Tipos dados:**
```typescript
type Regla = { nombre: string; condicion: (o: Orden) => boolean; porcentaje: number };
type OrdenConDescuento = Orden & { descuento: number; totalFinal: number };
type Resumen = { totalOriginal: number; totalFinal: number; ahorro: number; cantidad: number };
```

**Ejemplo:**
```typescript
const reglas: Regla[] = [
  { nombre: "VIP", condicion: o => o.total > 500, porcentaje: 20 },
  { nombre: "Regular", condicion: o => o.total > 100, porcentaje: 10 },
];
const orden = { id: 1, cliente: "Ana", total: 200, categoria: "elect", activa: true };
aplicarReglas(orden, reglas);
// → { ...orden, descuento: 10, totalFinal: 180 }
```

---

### BLOQUE 4 — Integrador

#### Ejercicio 19 — Integrador TypeScript — 6 pts
**Trazabilidad:** F-35, F-36 | **Archivo:** `typescript/src/ej19.ts`

Implementá el pipeline completo del taller usando `Result`:

- `clasificarOrden(o: Orden): Result<number, string>` — Si activa Y categoría `"elect"` Y total > 200, retorna `ok(total)`. Si no es activa, `err("inactiva")`. Si categoría no es elect, `err("categoría incorrecta")`. Si total ≤ 200, `err("monto insuficiente")`.
- `totalElectActivos(ordenes: Orden[]): number` — Clasifica cada orden, filtra los ok y suma los valores.
- `resumenClasificacion(ordenes: Orden[]): { aprobadas: number; rechazadas: number; total: number }` — Cuenta aprobadas, rechazadas y suma total de las aprobadas.

**Ejemplo:**
```typescript
const ordenes = [
  { id: 1, cliente: "Ana",   total: 250, categoria: "elect", activa: true },
  { id: 2, cliente: "Boris", total: 80,  categoria: "ropa",  activa: false },
  { id: 3, cliente: "Carla", total: 420, categoria: "elect", activa: true },
  { id: 4, cliente: "Diana", total: 30,  categoria: "ropa",  activa: true },
  { id: 5, cliente: "Edwin", total: 175, categoria: "elect", activa: true },
];
totalElectActivos(ordenes);       // → 670  (250 + 420)
resumenClasificacion(ordenes);    // → { aprobadas: 2, rechazadas: 3, total: 670 }
```

---

#### Ejercicio 20 — Integrador Clojure — 7 pts
**Trazabilidad:** F-37 | **Archivo:** `clojure/src/tp04/ej20.clj`

Implementá el mismo pipeline integrador en Clojure:

- `(clasificar-orden orden)` — Retorna `{:ok true :value total}` si activa, categoría "elect" y total > 200. Error con razón en caso contrario.
- `(total-elect-activos ordenes)` — Clasifica, filtra ok, suma valores.
- `(resumen-por-categoria ordenes)` — Retorna mapa `{"elect" suma-elect, "ropa" suma-ropa, ...}` considerando solo las activas.

**Ejemplo:**
```clojure
(def ordenes
  [{:id 1 :cliente "Ana"   :total 250 :categoria "elect" :activa? true}
   {:id 2 :cliente "Boris" :total 80  :categoria "ropa"  :activa? false}
   {:id 3 :cliente "Carla" :total 420 :categoria "elect" :activa? true}
   {:id 4 :cliente "Diana" :total 30  :categoria "ropa"  :activa? true}
   {:id 5 :cliente "Edwin" :total 175 :categoria "elect" :activa? true}])

(total-elect-activos ordenes)      ; => 670
(resumen-por-categoria ordenes)    ; => {"elect" 845, "ropa" 30}
```

---

## Distribución de puntos

| Ej | Tema | Lenguaje | Filminas | Pts |
|----|------|----------|----------|-----|
| 1 | Pipeline filter/map/reduce | TypeScript | F-06,07,08 | 3 |
| 2 | Composición pipe/compose | TypeScript | F-09 | 5 |
| 3 | Inmutabilidad | TypeScript | F-05,10 | 3 |
| 4 | Pipeline ->> | Clojure | F-12 | 3 |
| 5 | Secuencias perezosas | Clojure | F-11 | 5 |
| 6 | Colecciones persistentes | Clojure | F-13 | 3 |
| 7 | ADT tipo suma | TypeScript | F-14 | 5 |
| 8 | Result\<T,E\> | TypeScript | F-15,16 | 6 |
| 9 | Maybe / Option | TypeScript | F-17 | 5 |
| 10 | Errores como datos | Clojure | F-18 | 5 |
| 11 | Transducer básico | Clojure | F-19,20 | 5 |
| 12 | Transducer vs pipeline | Clojure | F-21 | 5 |
| 13 | API genérica funcional | TypeScript | F-22 | 7 |
| 14 | Funciones de orden superior | TypeScript | F-23 | 5 |
| 15 | core.async canales | Clojure | F-26,27 | 6 |
| 16 | STM transacciones | Clojure | F-28 | 6 |
| 17 | async/await | TypeScript | F-30,31 | 5 |
| 18 | Separar efectos puros | TypeScript | F-32 | 5 |
| 19 | Integrador TypeScript | TypeScript | F-35,36 | 6 |
| 20 | Integrador Clojure | Clojure | F-37 | 7 |
| | | | **Total** | **100** |

**TypeScript:** 11 ejercicios — 60 pts | **Clojure:** 9 ejercicios — 40 pts
