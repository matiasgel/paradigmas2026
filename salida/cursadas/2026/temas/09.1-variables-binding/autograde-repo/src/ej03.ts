// Ejercicio 3 — Binding de almacenamiento: closures y recursión (25 pts)
// Trazabilidad: OA3 — F-11, F-13, F-14, F-15

export interface Counter {
  increment: () => number;
  decrement: () => number;
  reset: () => void;
  value: () => number;
}

// 3a. Implementar factorial de forma RECURSIVA (stack-dynamic).
// Cada llamada crea un nuevo frame con su propia copia de n.
// factorial(0) = 1
// factorial(n) = n * factorial(n - 1)   para n > 0
export function factorial(n: number): number {
  throw new Error("TODO: implementar");
}

// 3b. Crear un contador con estado encapsulado en un closure (heap-dynamic-implicit).
// makeCounter(5).increment() → 6
// makeCounter(5).decrement() → 4
// makeCounter(5).value()     → 5
// reset() vuelve al valor con que fue creado (initial).
export function makeCounter(initial: number): Counter {
  throw new Error("TODO: implementar");
}

// 3c. Retorna una función que suma n a su argumento (currying/closure).
// n queda capturado en el closure — heap-dynamic-implicit.
// makeAdder(3)(4) → 7
export function makeAdder(n: number): (x: number) => number {
  throw new Error("TODO: implementar");
}

// 3d. Crea un acumulador que inicia en 0.
// add(n) suma n al total acumulado.
// total() retorna el total actual sin modificarlo.
// const { add, total } = makeAccumulator(); add(5); add(3); total() → 8
export function makeAccumulator(): { add: (n: number) => void; total: () => number } {
  throw new Error("TODO: implementar");
}

// 3e. Retorna una versión memorizada de fn: la primera llamada con n computa y almacena
// fn(n) en una Map (heap-dynamic-implicit). Llamadas siguientes con el mismo n retornan
// el valor del caché sin invocar fn de nuevo. Útil para funciones costosas.
// Ejemplo:
//   let calls = 0;
//   const fn = memoize((n) => { calls++; return n * n; });
//   fn(4); fn(4); fn(4);  → calls === 1  (fn real se invoca una sola vez)
export function memoize(fn: (n: number) => number): (n: number) => number {
  throw new Error("TODO: implementar");
}
