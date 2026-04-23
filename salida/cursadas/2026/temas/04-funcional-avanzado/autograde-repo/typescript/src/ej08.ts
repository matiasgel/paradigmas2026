// Ejercicio 8 — Result<T, E>
// Trazabilidad: F-15, F-16

export type Result<T, E = string> =
  | { ok: true; value: T }
  | { ok: false; error: E };

// Constructores (dados — no modificar):
export const ok = <T>(value: T): Result<T, never> => ({ ok: true, value });
export const err = <E>(error: E): Result<never, E> => ({ ok: false, error });

/**
 * Si r es ok, aplica fn al valor y retorna ok con el resultado.
 * Si r es error, retorna el error sin modificar.
 */
export function mapResult<T, U, E>(
  r: Result<T, E>,
  fn: (value: T) => U
): Result<U, E> {
  // TODO: Implementar
  throw new Error("TODO: Implementar mapResult");
}

/**
 * Si r es ok, aplica fn al valor (fn retorna Result).
 * Si r es error, retorna el error sin modificar.
 */
export function flatMapResult<T, U, E>(
  r: Result<T, E>,
  fn: (value: T) => Result<U, E>
): Result<U, E> {
  // TODO: Implementar
  throw new Error("TODO: Implementar flatMapResult");
}

/**
 * Divide a / b. Retorna ok(resultado) o err("División por cero").
 */
export function dividir(a: number, b: number): Result<number, string> {
  // TODO: Implementar
  throw new Error("TODO: Implementar dividir");
}
