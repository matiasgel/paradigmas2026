/**
 * Ejercicios prácticos para demostrar comprensión de:
 * - Tipado estático en TypeScript
 * - Diferencias entre errores de compilación y de ejecución
 * - Operaciones básicas con arrays y strings
 * - Estructuras de datos y algoritmos básicos
 */

/**
 * Devuelve `true` si `x` es un número (tipo `number`).
 * Se espera que el alumno use `typeof`.
 */
export function esNumero(x: unknown): boolean {
  return typeof x === 'number';
}

/**
 * Devuelve `true` si `n` es par.
 */
export function esPar(n: number): boolean {
  return n % 2 === 0;
}

/**
 * Dado un array de números, devuelve la suma de sus elementos.
 */
export function sumaArray(arr: number[]): number {
  return arr.reduce((a, b) => a + b, 0);
}

/**
 * Dado un array de números, devuelve la suma usando recursión.
 * Implementado como expresión utilizando operador ternario para evitar statements.
 */
export const sumaArrayRecursiva = (arr: number[]): number =>
  arr.length === 0 ? 0 : arr[0] + sumaArrayRecursiva(arr.slice(1));

/**
 * Divide `a` entre `b` y lanza un error si `b` es 0.
 * Se usa una IIFE en la rama ternaria para lanzar el error sin usar `if`.
 */
export const dividir = (a: number, b: number): number =>
  b === 0
    ? (() => {
        throw new Error('División por cero');
      })()
    : a / b;

/**
 * Calcula factorial de n (n >= 0) usando recursión expresiva.
 */
export const factorial = (n: number): number =>
  n < 0
    ? (() => {
        throw new Error('n debe ser no negativo');
      })()
    : n <= 1
    ? 1
    : n * factorial(n - 1);

/**
 * Devuelve el máximo y mínimo de un array de números.
 */
export const maxMin = (arr: number[]): { max: number; min: number } =>
  arr.length === 0
    ? (() => {
        throw new Error('El array no puede estar vacío');
      })()
    : arr.reduce(
        (acc, n) => ({
          max: Math.max(acc.max, n),
          min: Math.min(acc.min, n),
        }),
        { max: arr[0], min: arr[0] }
      );

/**
 * Agrupa los elementos por la clave devuelta por `keyFn`.
 * Implementado en estilo funcional (sin mutaciones explícitas fuera del reduce).
 */
export const agruparPor = <T, K extends string | number | symbol>(
  arr: T[],
  keyFn: (item: T) => K
): Record<K, T[]> =>
  arr.reduce((acc, item) => {
    const key = keyFn(item);
    return {
      ...acc,
      [key]: [...(acc[key] ?? []), item],
    };
  }, {} as Record<K, T[]>);

/**
 * Simula un error de ejecución; lanza un Error si el parámetro es `null` o `undefined`.
 */
export const lanzarSiNulo = (x: unknown): string =>
  x === null || x === undefined
    ? (() => {
        throw new Error('Valor nulo o indefinido');
      })()
    : String(x);

/**
 * Convierte un string a número. Devuelve `null` si no es un número válido.
 */
export function parseNumber(text: string): number | null {
  const n = Number(text);
  return Number.isFinite(n) ? n : null;
}

/**
 * Filtra los números pares de un arreglo.
 */
export function filtrarPares(arr: number[]): number[] {
  return arr.filter((n) => n % 2 === 0);
}

/**
 * Genera un array con los números del 1 al n (inclusive).
 */
export function range(n: number): number[] {
  return Array.from({ length: n }, (_, i) => i + 1);
}

/**
 * Retorna true si la cadena es un palíndromo (ignora mayúsculas/minúsculas y espacios).
 */
export function esPalindromo(text: string): boolean {
  const limpio = text.replace(/\s+/g, '').toLowerCase();
  return limpio === limpio.split('').reverse().join('');
}

/**
 * Invierte el contenido de un string.
 */
export function invertirCadena(text: string): string {
  return text.split('').reverse().join('');
}

/**
 * Cuenta cuántas palabras hay en un texto (separa por espacios).
 */
export function contarPalabras(text: string): number {
  return text.trim() === '' ? 0 : text.trim().split(/\s+/).length;
}

/**
 * Aplana un arreglo de profundidad 1 (concatena los sub-arrays).
 */
export function aplanar<T>(arr: T[][]): T[] {
  return arr.reduce((acc, sub) => acc.concat(sub), [] as T[]);
}

/**
 * Elimina duplicados manteniendo el orden.
 */
export function unico<T>(arr: T[]): T[] {
  return Array.from(new Set(arr));
}

/**
 * Suma los cuadrados de los números del arreglo.
 */
export function sumaCuadrados(arr: number[]): number {
  return arr.reduce((acc, n) => acc + n * n, 0);
}
