// Ejercicio 4 — Ámbito estático y algoritmo de resolución de nombres (20 pts)
// Trazabilidad: OA4, OA6 — F-16, F-17, F-18, F-19

// 4a. Algoritmo de resolución de ámbito estático.
// scopes[0] = entorno más interno (bloque local actual).
// scopes[n-1] = entorno más externo (global).
// Retorna el valor del nombre en el entorno más interno donde exista.
// Retorna undefined si no existe en ningún entorno.
//
// Ejemplo:
//   scopeChainLookup([{x:1}, {x:2, y:3}, {z:5}], "x") → 1
//   scopeChainLookup([{x:1}, {x:2, y:3}, {z:5}], "z") → 5
//   scopeChainLookup([{x:1}], "w")                     → undefined
export function scopeChainLookup(
  scopes: Record<string, number>[],
  name: string
): number | undefined {
  throw new Error("TODO: implementar");
}

// 4b. makeMultiplier: el factor queda capturado en el ámbito léxico externo.
// makeMultiplier(3)(5) → 15
export function makeMultiplier(factor: number): (x: number) => number {
  throw new Error("TODO: implementar");
}

// 4c. makeFunctions: retorna un array de n funciones donde la función en
// posición i retorna i.
// CLAVE: usar let en el loop para que cada iteración cree un binding nuevo.
// Con var, todas las closures capturarían n (el valor final de i).
// makeFunctions(3): [() => 0, () => 1, () => 2]
export function makeFunctions(n: number): Array<() => number> {
  throw new Error("TODO: implementar");
}

// 4d. makeLogger: retorna una función que antepone el prefijo a cada mensaje (5 pts).
// El prefix queda capturado en el ámbito léxico externo (heap-dynamic-implicit).
// Esto es útil para distinguir logs de distintos módulos sin pasar el prefijo cada vez.
// const log = makeLogger("[INFO]");
// log("servidor iniciado") → "[INFO]: servidor iniciado"
// log("request recibido")  → "[INFO]: request recibido"
// const warn = makeLogger("[WARN]");
// warn("memoria alta")     → "[WARN]: memoria alta"
export function makeLogger(prefix: string): (msg: string) => string {
  throw new Error("TODO: implementar");
}
