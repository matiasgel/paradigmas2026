import { describe, it, expect } from "vitest";
import { area, perimetro, describir, type Shape } from "../src/ej07.js";

describe("Ej07 — ADT tipo suma", () => {
  describe("area", () => {
    it("calcula área de círculo", () => {
      expect(area({ kind: "circle", radius: 5 })).toBeCloseTo(78.5398, 3);
    });

    it("calcula área de rectángulo", () => {
      expect(area({ kind: "rectangle", width: 4, height: 3 })).toBe(12);
    });

    it("calcula área de triángulo", () => {
      expect(area({ kind: "triangle", base: 6, height: 4 })).toBe(12);
    });

    it("área de círculo con radio 1", () => {
      expect(area({ kind: "circle", radius: 1 })).toBeCloseTo(Math.PI, 5);
    });
  });

  describe("perimetro", () => {
    it("perímetro de círculo", () => {
      expect(perimetro({ kind: "circle", radius: 5 })).toBeCloseTo(31.4159, 3);
    });

    it("perímetro de rectángulo", () => {
      expect(perimetro({ kind: "rectangle", width: 4, height: 3 })).toBe(14);
    });

    it("perímetro de triángulo isósceles", () => {
      const p = perimetro({ kind: "triangle", base: 6, height: 4 });
      // lados = sqrt((3)² + 4²) = sqrt(25) = 5, perímetro = 6 + 5 + 5 = 16
      expect(p).toBeCloseTo(16, 3);
    });
  });

  describe("describir", () => {
    it("formato correcto para círculo", () => {
      expect(describir({ kind: "circle", radius: 5 })).toBe("circle: area=78.54");
    });

    it("formato correcto para rectángulo", () => {
      expect(describir({ kind: "rectangle", width: 4, height: 3 })).toBe("rectangle: area=12.00");
    });
  });
});
