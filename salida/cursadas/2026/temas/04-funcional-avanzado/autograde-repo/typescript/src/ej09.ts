// Ejercicio 9 — Maybe / Option
// Trazabilidad: F-17

export type Maybe<T> = { some: true; value: T } | { some: false };

// Constructores (dados — no modificar):
export const just = <T>(value: T): Maybe<T> => ({ some: true, value });
export const nothing = <T>(): Maybe<T> => ({ some: false });

/**
 * Si m tiene valor, aplica fn y retorna just con el resultado.
 * Si no tiene valor, retorna nothing.
 */
export function mapMaybe<T, U>(
  m: Maybe<T>,
  fn: (value: T) => U
): Maybe<U> {
  // TODO: Implementar
  throw new Error("TODO: Implementar mapMaybe");
}

/**
 * Si m tiene valor, aplica fn (que retorna Maybe).
 * Si no tiene valor, retorna nothing.
 */
export function flatMapMaybe<T, U>(
  m: Maybe<T>,
  fn: (value: T) => Maybe<U>
): Maybe<U> {
  // TODO: Implementar
  throw new Error("TODO: Implementar flatMapMaybe");
}

/**
 * Busca el primer elemento que cumple el predicado.
 * Retorna just(elemento) si encuentra, nothing() si no.
 */
export function buscar<T>(
  arr: T[],
  predicado: (item: T) => boolean
): Maybe<T> {
  // TODO: Implementar
  throw new Error("TODO: Implementar buscar");
}
