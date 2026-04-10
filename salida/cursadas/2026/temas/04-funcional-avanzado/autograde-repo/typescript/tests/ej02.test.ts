import { describe, it, expect } from "vitest";
import { pipe, compose } from "../src/ej02.js";

describe("Ej02 — Composición con pipe y compose", () => {
  const inc = (x: number) => x + 1;
  const doble = (x: number) => x * 2;
  const cuadrado = (x: number) => x * x;

  describe("pipe", () => {
    it("compone de izquierda a derecha", () => {
      expect(pipe(inc, doble)(3)).toBe(8);
    });

    it("compone tres funciones", () => {
      expect(pipe(inc, doble, cuadrado)(2)).toBe(36);
    });

    it("sin funciones actúa como identidad", () => {
      expect(pipe()(5)).toBe(5);
    });

    it("con una sola función la aplica", () => {
      expect(pipe(doble)(7)).toBe(14);
    });

    it("funciona con tipos diferentes", () => {
      expect(pipe(String, (s: string) => s + "!")(42)).toBe("42!");
    });
  });

  describe("compose", () => {
    it("compone de derecha a izquierda", () => {
      expect(compose(inc, doble)(3)).toBe(7);
    });

    it("compose tres funciones (f∘g∘h)", () => {
      expect(compose(cuadrado, doble, inc)(2)).toBe(36);
    });

    it("sin funciones actúa como identidad", () => {
      expect(compose()(5)).toBe(5);
    });
  });
});
