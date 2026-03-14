/**
 * Ejercicios prácticos para demostrar comprensión de:
 * - Tipado estático en TypeScript
 * - Diferencias entre errores de compilación y de ejecución
 * - Operaciones básicas con arrays y strings
 */

/**
 * Devuelve `true` si `x` es un número (tipo `number`).
 * Se espera que el alumno use `typeof`.
 */
export function esNumero(x: unknown): boolean {
  return typeof x === 'number';
}

/**
 * Dado un array de números, devuelve la suma de sus elementos.
 */
export function sumaArray(arr: number[]): number {
  return arr.reduce((a, b) => a + b, 0);
}

/**
 * Simula un error de ejecución; lanza un Error si el parámetro es `null` o `undefined`.
 */
export function lanzarSiNulo(x: unknown): string {
  if (x === null || x === undefined) {
    throw new Error('Valor nulo o indefinido');
  }
  return String(x);
}
