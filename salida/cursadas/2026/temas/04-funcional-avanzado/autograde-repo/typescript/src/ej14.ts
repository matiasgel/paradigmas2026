// Ejercicio 14 — Memoization (5 pts)
// Trazabilidad: F-28, F-29

// Memoize genérico para funciones de 1 argumento. Usa Map como cache.
export function memoize<T, R>(fn: (arg: T) => R): (arg: T) => R {
  throw new Error("TODO: implementar");
}

// Fibonacci recursivo clásico (sin memo).
export function fibonacci(n: number): number {
  throw new Error("TODO: implementar");
}

// Wrapper que cuenta llamadas. Retorna { call, count }.
export function callCounter<A extends unknown[], R>(fn: (...args: A) => R): {
  call: (...args: A) => R;
  count: () => number;
} {
  throw new Error("TODO: implementar");
}
