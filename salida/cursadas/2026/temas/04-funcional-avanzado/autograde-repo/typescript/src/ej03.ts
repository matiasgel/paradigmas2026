// Ejercicio 3 — Inmutabilidad con spread (4 pts)
// Trazabilidad: F-09

export type Persona = {
  readonly nombre: string;
  readonly edad: number;
  readonly hobbies: readonly string[];
};

export type User = {
  readonly name: string;
  readonly email: string;
};

// Devuelve nueva persona con edad + 1.
export function cumpleanios(p: Persona): Persona {
  throw new Error("TODO: implementar");
}

// Devuelve nueva persona con hobby agregado al final.
export function agregarHobby(p: Persona, hobby: string): Persona {
  throw new Error("TODO: implementar");
}

// Devuelve nueva persona con nombre actualizado.
export function actualizarNombre(p: Persona, nombre: string): Persona {
  throw new Error("TODO: implementar");
}

// Trim name, toLowerCase + trim email. Retorna nuevo objeto.
export function normalizeUser(u: User): User {
  throw new Error("TODO: implementar");
}
