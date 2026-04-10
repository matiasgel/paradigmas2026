import { describe, it, expect } from "vitest";
import { cumpleanios, agregarHobby, actualizarNombre, type Persona } from "../src/ej03.js";

const ana: Persona = { nombre: "Ana", edad: 28, hobbies: ["leer", "correr"] };

describe("Ej03 — Inmutabilidad", () => {
  describe("cumpleanios", () => {
    it("incrementa la edad en 1", () => {
      expect(cumpleanios(ana).edad).toBe(29);
    });

    it("no modifica el original", () => {
      cumpleanios(ana);
      expect(ana.edad).toBe(28);
    });

    it("preserva los otros campos", () => {
      const result = cumpleanios(ana);
      expect(result.nombre).toBe("Ana");
      expect(result.hobbies).toEqual(["leer", "correr"]);
    });
  });

  describe("agregarHobby", () => {
    it("agrega un hobby al final", () => {
      expect(agregarHobby(ana, "nadar").hobbies).toEqual(["leer", "correr", "nadar"]);
    });

    it("no modifica el original", () => {
      agregarHobby(ana, "nadar");
      expect(ana.hobbies).toEqual(["leer", "correr"]);
    });
  });

  describe("actualizarNombre", () => {
    it("cambia el nombre", () => {
      expect(actualizarNombre(ana, "Ana María").nombre).toBe("Ana María");
    });

    it("no modifica el original", () => {
      actualizarNombre(ana, "Ana María");
      expect(ana.nombre).toBe("Ana");
    });
  });
});
