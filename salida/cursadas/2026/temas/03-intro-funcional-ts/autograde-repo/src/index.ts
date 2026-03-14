/**
 * Implementá las funciones solicitadas para completar el TP.
 *
 * El test inspecciona que estas funciones existan y tengan los comportamientos
 * básicos descritos en los enunciados del tema.
 */

/**
 * Indica si una función es pura según su implementación.
 * (Ejemplo didáctico: devolver `true` si la función no lee ni escribe variables externas.)
 */
export function esFuncionPura(fn: () => unknown): boolean {
  // En este contexto, asumimos que la función es pura si no lanza errores
  // y devuelve siempre el mismo valor cuando se invoca varias veces.
  try {
    const a = fn();
    const b = fn();
    return Object.is(a, b);
  } catch {
    return false;
  }
}

/**
 * Devuelve el arreglo resultante al aplicar `map` sobre `arr`.
 */
export function aplicarMap<T, U>(arr: T[], fn: (x: T) => U): U[] {
  return arr.map(fn);
}

/**
 * Devuelve la suma de un array usando recursión.
 */
export function sumaRecursiva(nums: number[]): number {
  if (nums.length === 0) return 0;
  const [head, ...tail] = nums;
  return head + sumaRecursiva(tail);
}

/**
 * Currifica una función de dos argumentos.
 */
export function curry2<A, B, R>(fn: (a: A, b: B) => R): (a: A) => (b: B) => R {
  return (a: A) => (b: B) => fn(a, b);
}

/**
 * Implementa `pipe` para componer funciones de izquierda a derecha.
 */
export function pipe<A>(...fns: Array<(a: A) => A>): (input: A) => A {
  return (input: A) => fns.reduce((acc, fn) => fn(acc), input);
}

/**
 * Crea una lista perezosa (lazy) de números del 1 al n.
 * La generación ocurre sólo cuando se itera sobre el iterable.
 */
export function* rangeLazy(n: number): Generator<number> {
  for (let i = 1; i <= n; i++) {
    yield i;
  }
}
