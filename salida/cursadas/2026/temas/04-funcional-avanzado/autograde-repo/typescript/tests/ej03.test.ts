// Tests — Ejercicio 3: Inmutabilidad con spread
import { describe, it, expect } from "vitest";
import { cumpleanios, agregarHobby, actualizarNombre, normalizeUser, Persona } from "../src/ej03";

const ana: Persona = { nombre: "Ana", edad: 28, hobbies: ["leer", "correr"] };

describe("cumpleanios", () => {
  it("incrementa edad", () => {
    expect(cumpleanios(ana).edad).toBe(29);
  });
  it("no modifica original", () => {
    cumpleanios(ana);
    expect(ana.edad).toBe(28);
  });
});

describe("agregarHobby", () => {
  it("agrega hobby al final", () => {
    expect(agregarHobby(ana, "nadar").hobbies).toEqual(["leer", "correr", "nadar"]);
  });
  it("no modifica original", () => {
    agregarHobby(ana, "nadar");
    expect(ana.hobbies).toEqual(["leer", "correr"]);
  });
});

describe("actualizarNombre", () => {
  it("cambia nombre", () => {
    expect(actualizarNombre(ana, "Anita").nombre).toBe("Anita");
  });
  it("no modifica original", () => {
    actualizarNombre(ana, "Anita");
    expect(ana.nombre).toBe("Ana");
  });
});

describe("normalizeUser", () => {
  it("trim y lowercase", () => {
    expect(normalizeUser({ name: "  Ana  ", email: "  ANA@test.com  " })).toEqual({
      name: "Ana",
      email: "ana@test.com",
    });
  });
  it("no modifica original", () => {
    const u = { name: "  X  ", email: "  Y  " };
    normalizeUser(u);
    expect(u.name).toBe("  X  ");
  });
});
