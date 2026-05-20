# TP 09.1 — Variables, Binding y Ámbito

**Materia:** Paradigmas y Lenguajes de Programación 2026 — UNTDF / IDEI  
**Tema:** 09.1 — Variables, Binding y Ámbito  
**Semana:** 9 (clase 09.1)  
**Lenguaje:** TypeScript  
**Entrega:** Repositorio en GitHub Classroom — autograding automático  
**Puntos totales:** 100  
**Fecha límite:** ver GitHub Classroom

---

## Trazabilidad con la clase

| Ejercicio | Filminas | Objetivos (OA) | Nivel Bloom |
|-----------|----------|----------------|-------------|
| Ej01 — L-value y R-value: variables como contenedores | F-01, F-02, F-03 | OA1 | Aplicar |
| Ej02 — Binding de tipos: tipado estático y coerciones | F-05, F-08, F-09, F-10 | OA2, OA5 | Aplicar |
| Ej03 — Binding de almacenamiento: closures y recursión | F-11, F-13, F-14, F-15 | OA3 | Aplicar |
| Ej04 — Ámbito estático y resolución de nombres | F-16, F-17, F-19 | OA4, OA6 | Aplicar / Analizar |
| Ej05 — Detectar y corregir errores de binding y ámbito | F-06, F-17, F-19 | OA7 | Evaluar |

---

## Instrucciones de entrega

1. Aceptá la asignación desde el link de GitHub Classroom publicado en el aula.
2. Cloná tu repositorio: `git clone <url-de-tu-repo>`
3. Implementá las funciones en los archivos `src/ej0X.ts`.
4. **No modifiques los archivos de test** (`tests/ej0X.test.ts`).
5. Los tests se ejecutan automáticamente con cada `git push`.
6. El estado del check ✅/❌ aparece en la pestaña **Actions** de tu repo.
7. Verificá que el check ✅ aparece antes de la fecha límite.

### Ejecutar tests localmente

```bash
npm install
npx vitest run             # todos los tests
npx vitest run tests/ej01.test.ts   # un solo ejercicio
```

---

## Ejercicio 1 — L-value y R-value: variables como contenedores (20 pts)

**Archivo:** `src/ej01.ts`

Una variable es una abstracción de la celda de memoria Von Neumann. Cuando aparece a la
izquierda de una asignación actúa como **L-value** (posición/dirección que recibe el valor);
cuando aparece a la derecha actúa como **R-value** (contenido que se lee).

Todas las funciones de este ejercicio operan **in-place**: modifican el array original
sin crear uno nuevo. Esto demuestra directamente que cada posición del array es un L-value.

### 1a. `swap<T>(arr: T[], i: number, j: number): void` — 5 pts

Intercambia `arr[i]` y `arr[j]` in-place usando una variable temporal.

```typescript
const nums = [1, 2, 3, 4];
swap(nums, 0, 3);
// nums → [4, 2, 3, 1]
```

### 1b. `rotateLeft<T>(arr: T[]): void` — 5 pts

Rota el array una posición hacia la izquierda: el primer elemento pasa al final.
Si el array tiene 0 o 1 elementos, no hace nada.

```typescript
const nums = [1, 2, 3, 4];
rotateLeft(nums);
// nums → [2, 3, 4, 1]
```

### 1c. `doubleAll(arr: number[]): void` — 5 pts

Duplica cada elemento del array in-place: lee el valor (R-value), lo duplica y lo
escribe de vuelta en la misma posición (L-value).

```typescript
const nums = [1, 2, 3];
doubleAll(nums);
// nums → [2, 4, 6]
```

### 1d. `findAndReplace<T>(arr: T[], oldVal: T, newVal: T): number` — 5 pts

Reemplaza todas las ocurrencias de `oldVal` por `newVal` in-place.
Retorna la cantidad de reemplazos realizados.

```typescript
const arr = [1, 2, 1, 3, 1];
findAndReplace(arr, 1, 9);
// arr → [9, 2, 9, 3, 9], retorna 3
```

---

## Ejercicio 2 — Binding de tipos: dimensiones ortogonales (20 pts)

**Archivo:** `src/ej02.ts`

El binding de tipos tiene **dos dimensiones independientes**:

- **Estático vs. dinámico**: ¿cuándo se establece el tipo? En compilación (estático) o en ejecución (dinámico).
- **Fuerte vs. débil**: ¿cuán estricto es el sistema de tipos? Sin coerciones implícitas arbitrarias (fuerte) o con ellas (débil).

Lenguajes de referencia:

| Lenguaje | Binding | Fortaleza |
|----------|---------|-----------|
| TypeScript | estático | fuerte |
| Haskell | estático | fuerte |
| C | estático | débil |
| Python | dinámico | fuerte |
| JavaScript | dinámico | débil |
| Prolog | dinámico | fuerte |

### 2a. `classifyTypeBinding(lang: string): "static" | "dynamic"` — 4 pts

Clasifica el binding de tipos del lenguaje. Lanzar `Error("unknown language")` para lenguajes no reconocidos.

### 2b. `classifyTypeStrength(lang: string): "strong" | "weak"` — 4 pts

Clasifica la fortaleza de tipos del lenguaje. Mismos lenguajes reconocidos que 2a.

### 2c. `classifyBoth(lang: string): TypeProfile` — 4 pts

Devuelve `{ binding, strength }` para el lenguaje. Implementar usando 2a y 2b.

### 2d. `strictAdd(a: string, b: string): number` — 4 pts

Dado dos strings que representan enteros, devuelve su suma como `number`.
**Sin coerciones implícitas** — no usar `+` directamente sobre strings en modo que dependa de coerción JS.

```typescript
strictAdd("3", "4") // → 7
strictAdd("10", "20") // → 30
```

### 2e. `filterStaticTyped(langs: string[]): string[]` — 4 pts

Filtra y retorna solo los lenguajes de la lista que tienen binding de tipos **estático**.
Usar `classifyTypeBinding` internamente.

---

## Ejercicio 3 — Binding de almacenamiento: closures y recursión (25 pts)

**Archivo:** `src/ej03.ts`

Las variables tienen 4 categorías de tiempo de vida según cómo se vinculan al almacenamiento:
1. **Estáticas** — existen toda la ejecución del programa
2. **Stack-dynamic** — creadas al entrar a un subprograma, destruidas al salir (permiten recursión)
3. **Heap-dynamic-explicit** — `malloc`/`new`, gestionadas manualmente
4. **Heap-dynamic-implicit** — gestionadas automáticamente (closures, GC)

### 3a. `factorial(n: number): number` — 5 pts

Implementar factorial de forma **recursiva**. Cada llamada crea su propio frame de stack
(stack-dynamic binding): `n` en cada invocación es una variable distinta.

```
factorial(0) = 1
factorial(n) = n * factorial(n - 1)   para n > 0
```

### 3b. `makeCounter(initial: number): Counter` — 5 pts

Crea un contador con estado encapsulado en un **closure** (heap-dynamic-implicit).
El estado vive en el heap — no en el stack.

```typescript
const c = makeCounter(5);
c.increment() // → 6
c.increment() // → 7
c.decrement() // → 6
c.value()     // → 6
c.reset()     // vuelve a 5
c.value()     // → 5
```

El tipo `Counter` ya está definido en el archivo.

### 3c. `makeAdder(n: number): (x: number) => number` — 5 pts

Retorna una función que suma `n` a su argumento. `n` queda capturado en el closure.

```typescript
const add3 = makeAdder(3);
add3(4)  // → 7
add3(10) // → 13
makeAdder(0)(99) // → 99
```

### 3d. `makeAccumulator(): { add: (n: number) => void; total: () => number }` — 5 pts

Crea un acumulador que inicia en 0. `add(n)` suma `n` al acumulado. `total()` retorna el total
sin modificarlo.

```typescript
const { add, total } = makeAccumulator();
add(5); add(3);
total() // → 8
```

### 3e. `memoize(fn: (n: number) => number): (n: number) => number` — 5 pts

Retorna una versión memorizada de `fn`: la primera llamada con un `n` dado computa y guarda
`fn(n)` en una `Map` (heap-dynamic-implicit). Llamadas siguientes con el mismo `n` retornan
el valor del caché sin llamar a `fn` de nuevo.

```typescript
let calls = 0;
const fn = memoize((n) => { calls++; return n * n; });
fn(4); fn(4); fn(4);
calls // → 1  (fn original invocada una sola vez)
fn(5); fn(5);
calls // → 2  (nueva clave, nueva llamada a fn)
```

---

## Ejercicio 4 — Ámbito estático y resolución de nombres (20 pts)

**Archivo:** `src/ej04.ts`

El **ámbito estático** (léxico) determina la visibilidad de un nombre en base a la
estructura textual del programa. El algoritmo de resolución sube por la cadena de entornos
desde el más interno al más externo.

### 4a. `scopeChainLookup(scopes: Record<string, number>[], name: string): number | undefined` — 5 pts

Implementar el algoritmo de resolución de ámbito estático:

- `scopes[0]` es el entorno más interno (bloque local actual).
- `scopes[scopes.length - 1]` es el entorno más externo (global).
- Retornar el valor en el entorno **más interno** donde `name` esté definido.
- Retornar `undefined` si no existe en ningún entorno (**scope error**).

```typescript
scopeChainLookup([{x:1}, {x:2, y:3}, {z:5}], "x")  // → 1  (entorno 0 gana)
scopeChainLookup([{x:1}, {x:2, y:3}, {z:5}], "z")  // → 5  (solo en entorno 2)
scopeChainLookup([{x:1}], "w")                       // → undefined
```

### 4b. `makeMultiplier(factor: number): (x: number) => number` — 4 pts

`factor` es capturado en el ámbito léxico externo. La función retornada multiplica su argumento por `factor`.

```typescript
makeMultiplier(3)(5) // → 15
```

### 4c. `makeFunctions(n: number): Array<() => number>` — 4 pts

Retorna un array de `n` funciones donde la función en posición `i` retorna `i`.

**Clave**: usar `let` en el loop (no `var`). Con `let`, cada iteración crea un **nuevo binding**
de `i`, por lo que cada closure captura su propio valor. Con `var`, todas capturarían `n`.

```typescript
const fns = makeFunctions(3);
fns[0]() // → 0
fns[1]() // → 1
fns[2]() // → 2
```

### 4d. `makeLogger(prefix: string): (msg: string) => string` — 4 pts

Retorna una función que antepone `prefix` a cada mensaje con el formato `"${prefix}: ${msg}"`.
El `prefix` queda capturado en el ámbito léxico del closure (heap-dynamic-implicit) y no
cambia entre llamadas.

```typescript
const log = makeLogger("[INFO]");
log("servidor iniciado") // → "[INFO]: servidor iniciado"
log("request recibido")  // → "[INFO]: request recibido"

const warn = makeLogger("[WARN]");
warn("memoria alta")     // → "[WARN]: memoria alta"
```

---

## Ejercicio 5 — Detectar y corregir errores de binding y ámbito (15 pts)

**Archivo:** `src/ej05.ts`

El archivo contiene funciones **buggy** con errores clásicos de binding y ámbito en JavaScript/TypeScript.
Los tests verifican primero que la versión buggy **falla de la manera esperada** (para que entiendas
el bug), y luego verifican que tu versión **fixed** se comporta correctamente.

**No modificar** las funciones `buggy*`.

### 5a. `fixedVarLoop(n: number): number[]` — 6 pts

**Bug en `buggyVarLoop`**: usa `var` para el índice del loop. `var` tiene **función-scope** (no
bloque-scope), entonces todas las clausuras capturan la **misma variable `i`** (que al final del
loop vale `n`). Resultado: `buggyVarLoop(3)` → `[3, 3, 3]`.

**Tu tarea**: implementar `fixedVarLoop` con `let` → cada iteración crea un binding nuevo.
`fixedVarLoop(3)` → `[0, 1, 2]`.

### 5b. `fixedSum(nums: number[]): number` — 5 pts

**Bug en `buggySum`**: dentro del `forEach`, se declara `const result = n` que **opaca** al
`result` externo (shadowing involuntario). El acumulador externo nunca se modifica. Resultado:
`buggySum([1,2,3])` → `0`.

**Tu tarea**: implementar `fixedSum` que suma correctamente todos los elementos.

### 5c. `fixedSumArray(nums: number[]): number` — 4 pts

Implementar una suma de array **sin variables globales implícitas**.
En modo strict de TypeScript, el compilador ya previene asignaciones a variables no declaradas.
Usar `const`/`let` correctamente para todos los bindings locales.

```typescript
fixedSumArray([1, 2, 3]) // → 6
fixedSumArray([])         // → 0
fixedSumArray([-1, -2, 3]) // → 0
```
