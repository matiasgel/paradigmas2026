---
topic_id: "04-funcional-avanzado"
topic_name: "Aspectos Avanzados de Programación Funcional"
exam_type: "parcial-1"
course_id: "2026"
question_count: 5
points_total: 17
bloom_mix: "recordar: 3pts, comprender: 6pts, aplicar: 4pts, analizar: 4pts"
generated_at: "2026-05-25"
---

# Preguntas — Tema 04: Aspectos Avanzados de Programación Funcional

---

## P-04-001 | Recordar | Conceptual | 3 pts

**¿Qué es una función de orden superior (Higher Order Function — HOF)?**

a) Una función que solo opera sobre tipos numéricos  
b) Una función que recibe otra función como argumento y/o devuelve una función como resultado  
c) Una función que utiliza recursión para resolver un problema  
d) Una función declarada con `function` en lugar de arrow function en TypeScript  

**Respuesta correcta:** b  
**Justificación:** Una función de orden superior (HOF) es aquella que trata las funciones como valores: puede recibirlas como parámetros y/o retornarlas como resultado. Ejemplos canónicos: `map(f, lista)` recibe `f` como argumento; `compose(f, g)` devuelve una nueva función. Esto es posible porque en el paradigma funcional las funciones son valores de primera clase.  
**Fuente:** minuta.md §BLOQUE 1 — [F-05] Anatomía de una HOF (OA-1)  
**Bloom:** Recordar  

---

## P-04-002 | Comprender | Conceptual | 3 pts

**¿Cuál es la diferencia fundamental entre partial application y currying?**

a) Partial application convierte una función en una función currificada; currying aplica parcialmente sus argumentos  
b) Partial application fija uno o más argumentos de una función devolviendo una función con menos parámetros; currying transforma una función de N argumentos en una cadena de N funciones de un argumento cada una  
c) Son el mismo concepto expresado en distintos lenguajes: partial en Clojure y currying en TypeScript  
d) Currying siempre requiere especificar todos los argumentos de una vez; partial application permite aplicarlos en cualquier orden  

**Respuesta correcta:** b  
**Justificación:** **Partial application** fija algunos argumentos de una función y devuelve una nueva función que espera el resto. Ejemplo: `const add5 = add.bind(null, 5)` fija el primer argumento. **Currying** convierte `f(a, b, c)` en `f(a)(b)(c)` — una cadena de funciones unarias. La diferencia clave: en partial application podés fijar cualquier cantidad de argumentos; en currying siempre se aplica un argumento por vez en una cadena estricta.  
**Fuente:** minuta.md §BLOQUE 2 — [F-13] Partial application vs [F-16] Currying (OA-4)  
**Bloom:** Comprender  

---

## P-04-003 | Comprender | Conceptual | 3 pts

**`compose(f, g)(x)` y `pipe(f, g)(x)` aplican las mismas funciones `f` y `g` sobre `x`, pero en distinto orden. ¿Cuál de las siguientes afirmaciones es correcta?**

a) `compose(f, g)(x)` aplica `f` primero y luego `g`; `pipe(f, g)(x)` aplica `g` primero y luego `f`  
b) `compose(f, g)(x)` es equivalente a `f(g(x))` — se aplica de derecha a izquierda; `pipe(f, g)(x)` es equivalente a `g(f(x))` — se aplica de izquierda a derecha  
c) Ambos producen el mismo resultado porque la composición es conmutativa  
d) `compose` solo existe en Clojure; `pipe` solo existe en TypeScript  

**Respuesta correcta:** b  
**Justificación:** `compose(f, g)(x) = f(g(x))`: primero se aplica `g`, luego `f` (notación matemática: de derecha a izquierda). `pipe(f, g)(x) = g(f(x))`: primero se aplica `f`, luego `g` (lectura de izquierda a derecha, más natural en código). Son equivalentes solo si `f = g`. En general, `compose(f, g) ≠ pipe(f, g)` a menos que `f` y `g` conmuten.  
**Fuente:** minuta.md §BLOQUE 1 — [F-06] compose vs pipe (OA-2)  
**Bloom:** Comprender  

---

## P-04-004 | Aplicar | Con código | 4 pts

**Dado el siguiente código TypeScript:**

```typescript
const trim = (s: string): string => s.trim();
const toLower = (s: string): string => s.toLowerCase();
const addDomain = (s: string): string => s + "@untdf.edu.ar";

const pipe = <T>(...fns: Array<(x: T) => T>) => (x: T) =>
  fns.reduce((acc, fn) => fn(acc), x);

const normalizeEmail = pipe(trim, toLower, addDomain);

console.log(normalizeEmail("  MATIAS  "));
```

**¿Qué imprime este código?**

a) `"  MATIAS  @untdf.edu.ar"` — `pipe` no aplica `trim` porque está primero  
b) `"matias@untdf.edu.ar"` — se aplican `trim`, luego `toLower`, luego `addDomain` en orden  
c) `"MATIAS@UNTDF.EDU.AR"` — `toLower` se aplica solo al resultado de `trim`, no a `addDomain`  
d) Error de compilación — `pipe` no acepta funciones de tipo `string => string`  

**Respuesta correcta:** b  
**Justificación:** `pipe` aplica las funciones de izquierda a derecha usando `reduce`. Traza: `"  MATIAS  "` → `trim` → `"MATIAS"` → `toLower` → `"matias"` → `addDomain` → `"matias@untdf.edu.ar"`. Cada función recibe como input el output de la anterior. El tipo es `string => string` en toda la cadena, compatible con la implementación genérica de `pipe`.  
**Fuente:** minuta.md §BLOQUE 1 — [F-07] pipe en TypeScript (OA-2)  
**Bloom:** Aplicar  

---

## P-04-005 | Analizar | Con código | 4 pts

**Considerá esta implementación de `factorial` en TypeScript:**

```typescript
// Versión A
const factorialA = (n: number): number => {
  if (n <= 1) return 1;
  return n * factorialA(n - 1);
};

// Versión B
const factorialB = (n: number, acc: number = 1): number => {
  if (n <= 1) return acc;
  return factorialB(n - 1, n * acc);
};
```

**¿Por qué `factorialB` es preferible a `factorialA` desde la perspectiva del paradigma funcional?**

a) `factorialB` es más legible porque usa un parámetro con valor por defecto  
b) `factorialA` usará menos memoria porque no necesita el acumulador; `factorialB` es más lenta  
c) `factorialB` implementa recursión de cola: la llamada recursiva es la última operación, lo que permite que el runtime optimice la pila (TCO); `factorialA` acumula marcos de stack porque necesita multiplicar por `n` al regresar  
d) Ambas son equivalentes en términos de eficiencia — TypeScript optimiza la recursión automáticamente  

**Respuesta correcta:** c  
**Justificación:** En `factorialA`, la última operación es `n * factorialA(n-1)` — hay un cálculo pendiente al retornar, por lo que cada llamada recursiva debe mantenerse en el stack. Para `n` grande, esto causa stack overflow. `factorialB` usa **tail recursion**: la llamada recursiva `factorialB(n-1, n*acc)` es la última operación, y el resultado se acumula en `acc`. Esto permite que runtimes con TCO (Clojure con `recur`) reutilicen el mismo frame de stack. TypeScript no garantiza TCO nativo, pero el patrón de acumulador es correcto funcionalmente.  
**Fuente:** minuta.md §BLOQUE 3 — [F-24 a F-27] Recursión de cola (OA-7)  
**Bloom:** Analizar  
