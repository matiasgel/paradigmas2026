// Ejercicio 2 — Binding de tipos: dimensiones ortogonales (20 pts)
// Trazabilidad: OA2, OA5 — F-05, F-08, F-09, F-10

export type TypeBinding = "static" | "dynamic";
export type TypeStrength = "strong" | "weak";

export interface TypeProfile {
  binding: TypeBinding;
  strength: TypeStrength;
}

// Lenguajes reconocidos: "TypeScript", "Haskell", "C", "Python", "JavaScript", "Prolog"

// 2a. Clasificar el binding de tipos del lenguaje.
// Lanzar Error("unknown language") para lenguajes no reconocidos.
export function classifyTypeBinding(lang: string): TypeBinding {
  throw new Error("TODO: implementar");
}

// 2b. Clasificar la fortaleza de tipos del lenguaje.
// Lanzar Error("unknown language") para lenguajes no reconocidos.
export function classifyTypeStrength(lang: string): TypeStrength {
  throw new Error("TODO: implementar");
}

// 2c. Devuelve el perfil completo { binding, strength } del lenguaje.
// Implementar usando classifyTypeBinding y classifyTypeStrength.
export function classifyBoth(lang: string): TypeProfile {
  throw new Error("TODO: implementar");
}

// 2d. Dadas dos cadenas numéricas, retorna su suma como number
// SIN usar coerciones implícitas (TypeScript strict mode).
// Ambos argumentos son strings de dígitos válidos (sin espacios ni signos).
// strictAdd("3", "4") → 7
export function strictAdd(a: string, b: string): number {
  throw new Error("TODO: implementar");
}

// 2e. Dada una lista de lenguajes, devuelve solo los de binding ESTÁTICO.
// Usar classifyTypeBinding internamente.
// Ignorar lenguajes no reconocidos (no lanzar error).
export function filterStaticTyped(langs: string[]): string[] {
  throw new Error("TODO: implementar");
}
