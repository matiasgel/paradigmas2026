// Ejercicio 13 — API genérica funcional
// Trazabilidad: F-22

import type { Result } from "./ej08.js";
import { ok, err } from "./ej08.js";

// Re-exportar para conveniencia en tests
export { ok, err };
export type { Result };

/**
 * Encadena una serie de funciones que retornan Result.
 * Empieza con `initial` y aplica cada fn en secuencia.
 * Si alguna retorna error, propaga inmediatamente.
 */
export function chainResults<T>(
  initial: T,
  fns: Array<(value: T) => Result<T, string>>
): Result<T, string> {
  // TODO: Implementar
  throw new Error("TODO: Implementar chainResults");
}

/**
 * Si TODOS los Results son ok, retorna ok con array de valores.
 * Si alguno es error, retorna el primer error encontrado.
 */
export function traverseResults<T>(
  results: Array<Result<T, string>>
): Result<T[], string> {
  // TODO: Implementar
  throw new Error("TODO: Implementar traverseResults");
}

/**
 * Extrae solo los valores de los Results que son ok.
 * Descarta los errores.
 */
export function filterOk<T>(
  results: Array<Result<T, string>>
): T[] {
  // TODO: Implementar
  throw new Error("TODO: Implementar filterOk");
}
