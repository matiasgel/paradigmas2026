// Ejercicio 1 — L-value, R-value y la 5-tupla (20 pts)
// Trazabilidad: OA1 — F-01, F-02, F-03

export type BindingTime =
  | "design"
  | "implementation"
  | "compile"
  | "link"
  | "load"
  | "execution";

export type StorageCategory =
  | "static"
  | "stack-dynamic"
  | "heap-dynamic-explicit"
  | "heap-dynamic-implicit";

export interface VariableAttributes {
  name: string;
  type: string;
  storageCategory: StorageCategory;
  rvalue: unknown;
  typeBindingTime: BindingTime;
}

// 1a. Swap in-place: intercambia arr[i] y arr[j] usando la posición como L-value.
// Demuestra que el L-value es la dirección (posición en el array) que se escribe.
// No retorna nada — modifica el array original.
export function swap<T>(arr: T[], i: number, j: number): void {
  throw new Error("TODO: implementar");
}

// 1b. Dado el nombre y valor de una variable local TypeScript (scope de función),
// devuelve sus atributos según el modelo de la 5-tupla.
// Ejemplo: getAttributes("count", 42) →
//   { name: "count", type: "number", storageCategory: "stack-dynamic",
//     rvalue: 42, typeBindingTime: "compile" }
export function getAttributes(name: string, value: unknown): VariableAttributes {
  throw new Error("TODO: implementar");
}

// 1c. Dado un identificador TypeScript, determina si puede ser L-value.
// Regla: retorna false si el nombre está en SCREAMING_SNAKE_CASE
//        (sólo mayúsculas, dígitos y guiones bajos, con al menos un _).
// Para cualquier otro identificador retorna true.
// Ejemplos: canBeLValue("myVar") → true
//           canBeLValue("MAX_VALUE") → false
//           canBeLValue("counter") → true
export function canBeLValue(identifier: string): boolean {
  throw new Error("TODO: implementar");
}
