// Ejercicio 3 — Inmutabilidad
// Trazabilidad: F-05, F-10

export type Persona = {
  readonly nombre: string;
  readonly edad: number;
  readonly hobbies: readonly string[];
};

/**
 * Devuelve una nueva Persona con edad + 1, sin modificar la original.
 */
export function cumpleanios(p: Persona): Persona {
  // TODO: Implementar
  throw new Error("TODO: Implementar cumpleanios");
}

/**
 * Devuelve una nueva Persona con el hobby agregado al final.
 */
export function agregarHobby(p: Persona, hobby: string): Persona {
  // TODO: Implementar
  throw new Error("TODO: Implementar agregarHobby");
}

/**
 * Devuelve una nueva Persona con el nombre actualizado.
 */
export function actualizarNombre(p: Persona, nombre: string): Persona {
  // TODO: Implementar
  throw new Error("TODO: Implementar actualizarNombre");
}
