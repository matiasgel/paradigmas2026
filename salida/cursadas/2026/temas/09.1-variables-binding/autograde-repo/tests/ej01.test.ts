import { describe, it, expect } from "vitest";
import { swap, getAttributes, canBeLValue } from "../src/ej01";

describe("Ej01 — L-value, R-value y la 5-tupla", () => {

  // --- swap ---
  describe("swap", () => {
    it("intercambia dos posiciones de un array de números", () => {
      const arr = [1, 2, 3, 4];
      swap(arr, 0, 3);
      expect(arr).toEqual([4, 2, 3, 1]);
    });

    it("funciona con strings", () => {
      const arr = ["a", "b", "c"];
      swap(arr, 0, 2);
      expect(arr).toEqual(["c", "b", "a"]);
    });

    it("swap del mismo índice no modifica el array", () => {
      const arr = [10, 20, 30];
      swap(arr, 1, 1);
      expect(arr).toEqual([10, 20, 30]);
    });

    it("modifica el array original (L-value in-place, misma referencia)", () => {
      const original = [5, 3, 8, 1];
      const ref = original;
      swap(original, 0, 3);
      expect(ref).toEqual([1, 3, 8, 5]);
    });

    it("swap adyacentes", () => {
      const arr = [7, 8, 9];
      swap(arr, 1, 2);
      expect(arr).toEqual([7, 9, 8]);
    });
  });

  // --- getAttributes ---
  describe("getAttributes", () => {
    it("nombre es el pasado como argumento", () => {
      const r = getAttributes("x", 10);
      expect(r.name).toBe("x");
    });

    it("rvalue es el valor pasado", () => {
      const r = getAttributes("total", 99);
      expect(r.rvalue).toBe(99);
    });

    it("type de un number es 'number'", () => {
      const r = getAttributes("n", 42);
      expect(r.type).toBe("number");
    });

    it("type de un string es 'string'", () => {
      const r = getAttributes("s", "hola");
      expect(r.type).toBe("string");
    });

    it("type de un boolean es 'boolean'", () => {
      const r = getAttributes("flag", true);
      expect(r.type).toBe("boolean");
    });

    it("variable local TypeScript tiene binding de tipo en compilación", () => {
      const r = getAttributes("v", true);
      expect(r.typeBindingTime).toBe("compile");
    });

    it("variable local TypeScript tiene categoría stack-dynamic", () => {
      const r = getAttributes("v", 0);
      expect(r.storageCategory).toBe("stack-dynamic");
    });
  });

  // --- canBeLValue ---
  describe("canBeLValue", () => {
    it("nombre camelCase puede ser L-value", () => {
      expect(canBeLValue("myVar")).toBe(true);
    });

    it("nombre lowercase puede ser L-value", () => {
      expect(canBeLValue("counter")).toBe(true);
    });

    it("SCREAMING_SNAKE_CASE NO puede ser L-value", () => {
      expect(canBeLValue("MAX_VALUE")).toBe(false);
    });

    it("PI_VALUE NO puede ser L-value", () => {
      expect(canBeLValue("PI_VALUE")).toBe(false);
    });

    it("nombre mixto con minúsculas puede ser L-value", () => {
      expect(canBeLValue("some_variable")).toBe(true);
    });

    it("nombre de una sola palabra en mayúsculas sin _ puede ser L-value", () => {
      expect(canBeLValue("VALUE")).toBe(true);
    });
  });
});
