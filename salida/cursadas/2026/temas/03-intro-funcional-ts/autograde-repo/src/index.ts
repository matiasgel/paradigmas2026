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
  // TODO: reemplazar por una implementación real desde la teoría.
  return true;
}

/**
 * Devuelve el arreglo resultante al aplicar `map` sobre `arr`.
 */
export function aplicarMap<T, U>(arr: T[], fn: (x: T) => U): U[] {
  return arr.map(fn);
}
