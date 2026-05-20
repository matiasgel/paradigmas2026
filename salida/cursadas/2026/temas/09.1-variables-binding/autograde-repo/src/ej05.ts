// Ejercicio 5 — Detectar y corregir errores de binding y ámbito (15 pts)
// Trazabilidad: OA7 — F-06, F-16, F-17, F-19
//
// Las funciones buggy* están completas y NO deben modificarse.
// Implementar las funciones fixed* para corregir el error de binding/ámbito.

// --- 5a: var hoisting en closures ---

// BUGGY (no modificar): var tiene scope de función, no de bloque.
// Todas las closures capturan la misma variable i (que al terminar el loop vale n).
// buggyVarLoop(3) → [3, 3, 3]
export function buggyVarLoop(n: number): number[] {
  const fns: Array<() => number> = [];
  for (var i = 0; i < n; i++) { // eslint-disable-line no-var
    fns.push(() => i);           // BUGGY: todas capturan la misma i
  }
  return fns.map((f) => f());
}

// CORRECTO: usar let para que cada iteración cree su propio binding de i.
// fixedVarLoop(3) → [0, 1, 2]
export function fixedVarLoop(n: number): number[] {
  throw new Error("TODO: implementar");
}

// --- 5b: shadowing involuntario ---

// BUGGY (no modificar): const result = n dentro del forEach crea un nuevo binding
// que opaca al result externo. El acumulador nunca se modifica.
// buggySum([1,2,3]) → 0
export function buggySum(nums: number[]): number {
  let result = 0;
  nums.forEach(function (n) {
    const result = n; // BUGGY: shadowing — nuevo binding local, no el acumulador
    void result;      // TypeScript: evitar "declared but never read"
  });
  return result;
}

// CORRECTO: sumar todos los elementos SIN crear un binding que opaque al acumulador.
// fixedSum([1, 2, 3]) → 6
export function fixedSum(nums: number[]): number {
  throw new Error("TODO: implementar");
}

// --- 5c: suma sin variables globales ---

// Implementar sumArray sin asignaciones a variables no declaradas.
// TypeScript strict mode previene variables globales implícitas en compilación.
// fixedSumArray([1, 2, 3])    → 6
// fixedSumArray([])            → 0
// fixedSumArray([-1, -2, 3])  → 0
export function fixedSumArray(nums: number[]): number {
  throw new Error("TODO: implementar");
}
