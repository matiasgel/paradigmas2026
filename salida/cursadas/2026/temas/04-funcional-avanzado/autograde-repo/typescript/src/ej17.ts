// Ejercicio 17 — async/await
// Trazabilidad: F-30, F-31

/**
 * Aplica `transformar` a cada item en paralelo usando Promise.all.
 * Retorna un array con todos los resultados.
 */
export async function procesarLote<T, U>(
  items: T[],
  transformar: (item: T) => Promise<U>
): Promise<U[]> {
  // TODO: Implementar con Promise.all
  throw new Error("TODO: Implementar procesarLote");
}

/**
 * Filtra items evaluando el predicado asincrónicamente.
 * El predicado es async y devuelve Promise<boolean>.
 * Retorna solo los items donde el predicado resolvió true.
 */
export async function filtrarAsync<T>(
  items: T[],
  predicado: (item: T) => Promise<boolean>
): Promise<T[]> {
  // TODO: Implementar
  throw new Error("TODO: Implementar filtrarAsync");
}
