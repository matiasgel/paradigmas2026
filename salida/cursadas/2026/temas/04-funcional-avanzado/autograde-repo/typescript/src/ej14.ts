// Ejercicio 14 — Funciones de orden superior
// Trazabilidad: F-23

/**
 * Retorna una función que aplica f sobre su argumento n veces.
 * aplicarNVeces(f, 0)(x) === x
 * aplicarNVeces(f, 3)(x) === f(f(f(x)))
 */
export function aplicarNVeces<T>(
  f: (x: T) => T,
  n: number
): (x: T) => T {
  // TODO: Implementar
  throw new Error("TODO: Implementar aplicarNVeces");
}

/**
 * Retorna una función que multiplica su argumento por factor.
 */
export function crearMultiplicador(
  factor: number
): (x: number) => number {
  // TODO: Implementar
  throw new Error("TODO: Implementar crearMultiplicador");
}

/**
 * Convierte una función de 2 argumentos en una función curried.
 * curry2(f)(a)(b) === f(a, b)
 */
export function curry2<A, B, R>(
  f: (a: A, b: B) => R
): (a: A) => (b: B) => R {
  // TODO: Implementar
  throw new Error("TODO: Implementar curry2");
}
