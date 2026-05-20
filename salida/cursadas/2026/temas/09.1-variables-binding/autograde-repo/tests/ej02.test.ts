import { describe, it, expect } from "vitest";
import {
  classifyTypeBinding,
  classifyTypeStrength,
  classifyBoth,
  strictAdd,
  filterStaticTyped,
} from "../src/ej02";

describe("Ej02 — Binding de tipos: dimensiones ortogonales", () => {

  describe("classifyTypeBinding", () => {
    it("TypeScript es estático", () => expect(classifyTypeBinding("TypeScript")).toBe("static"));
    it("Haskell es estático", () => expect(classifyTypeBinding("Haskell")).toBe("static"));
    it("C es estático", () => expect(classifyTypeBinding("C")).toBe("static"));
    it("Python es dinámico", () => expect(classifyTypeBinding("Python")).toBe("dynamic"));
    it("JavaScript es dinámico", () => expect(classifyTypeBinding("JavaScript")).toBe("dynamic"));
    it("Prolog es dinámico", () => expect(classifyTypeBinding("Prolog")).toBe("dynamic"));

    it("lenguaje desconocido lanza Error('unknown language')", () => {
      expect(() => classifyTypeBinding("COBOL")).toThrow("unknown language");
    });

    it("lenguaje desconocido (Java) lanza error", () => {
      expect(() => classifyTypeBinding("Java")).toThrow("unknown language");
    });
  });

  describe("classifyTypeStrength", () => {
    it("TypeScript es fuerte", () => expect(classifyTypeStrength("TypeScript")).toBe("strong"));
    it("Haskell es fuerte", () => expect(classifyTypeStrength("Haskell")).toBe("strong"));
    it("Python es fuerte", () => expect(classifyTypeStrength("Python")).toBe("strong"));
    it("Prolog es fuerte", () => expect(classifyTypeStrength("Prolog")).toBe("strong"));
    it("JavaScript es débil", () => expect(classifyTypeStrength("JavaScript")).toBe("weak"));
    it("C es débil", () => expect(classifyTypeStrength("C")).toBe("weak"));
  });

  describe("classifyBoth", () => {
    it("TypeScript: static + strong", () => {
      expect(classifyBoth("TypeScript")).toEqual({ binding: "static", strength: "strong" });
    });
    it("JavaScript: dynamic + weak", () => {
      expect(classifyBoth("JavaScript")).toEqual({ binding: "dynamic", strength: "weak" });
    });
    it("Python: dynamic + strong", () => {
      expect(classifyBoth("Python")).toEqual({ binding: "dynamic", strength: "strong" });
    });
    it("C: static + weak", () => {
      expect(classifyBoth("C")).toEqual({ binding: "static", strength: "weak" });
    });
    it("Haskell: static + strong", () => {
      expect(classifyBoth("Haskell")).toEqual({ binding: "static", strength: "strong" });
    });
  });

  describe("strictAdd", () => {
    it("suma básica: '3' + '4' = 7", () => expect(strictAdd("3", "4")).toBe(7));
    it("suma con cero: '0' + '5' = 5", () => expect(strictAdd("0", "5")).toBe(5));
    it("suma doble dígito: '10' + '20' = 30", () => expect(strictAdd("10", "20")).toBe(30));
    it("retorna un number (no string)", () => expect(typeof strictAdd("1", "2")).toBe("number"));
    it("'100' + '200' = 300", () => expect(strictAdd("100", "200")).toBe(300));
  });

  describe("filterStaticTyped", () => {
    it("filtra TypeScript y C de una lista mixta", () => {
      expect(filterStaticTyped(["TypeScript", "Python", "JavaScript", "C"])).toEqual([
        "TypeScript",
        "C",
      ]);
    });

    it("Haskell es estático", () => {
      expect(filterStaticTyped(["Haskell", "Python"])).toEqual(["Haskell"]);
    });

    it("lista vacía retorna vacía", () => {
      expect(filterStaticTyped([])).toEqual([]);
    });

    it("solo dinámicos retorna vacío", () => {
      expect(filterStaticTyped(["Python", "JavaScript", "Prolog"])).toEqual([]);
    });

    it("conserva el orden original", () => {
      expect(filterStaticTyped(["C", "Haskell", "TypeScript"])).toEqual(["C", "Haskell", "TypeScript"]);
    });
  });
});
