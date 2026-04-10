import { describe, it, expect } from "vitest";
import { aplicarNVeces, crearMultiplicador, curry2 } from "../src/ej14.js";

describe("Ej14 — Funciones de orden superior", () => {
  describe("aplicarNVeces", () => {
    it("aplica 3 veces", () => {
      expect(aplicarNVeces((x: number) => x * 2, 3)(1)).toBe(8);
    });

    it("0 veces es identidad", () => {
      expect(aplicarNVeces((x: number) => x + 100, 0)(5)).toBe(5);
    });

    it("1 vez aplica una sola vez", () => {
      expect(aplicarNVeces((x: number) => x + 1, 1)(10)).toBe(11);
    });

    it("funciona con strings", () => {
      expect(aplicarNVeces((s: string) => s + "!", 3)("hola")).toBe("hola!!!");
    });
  });

  describe("crearMultiplicador", () => {
    it("crea multiplicador por 5", () => {
      expect(crearMultiplicador(5)(7)).toBe(35);
    });

    it("multiplicar por 0", () => {
      expect(crearMultiplicador(0)(100)).toBe(0);
    });

    it("multiplicar por 1 es identidad", () => {
      expect(crearMultiplicador(1)(42)).toBe(42);
    });
  });

  describe("curry2", () => {
    it("curry suma", () => {
      const sumar = curry2((a: number, b: number) => a + b);
      expect(sumar(3)(4)).toBe(7);
    });

    it("curry concatenación", () => {
      const concat = curry2((a: string, b: string) => a + b);
      expect(concat("hola ")("mundo")).toBe("hola mundo");
    });

    it("aplicación parcial reutilizable", () => {
      const potencia = curry2((base: number, exp: number) => base ** exp);
      const cuadrado = potencia(2);
      expect(cuadrado(3)).toBe(8);
      expect(cuadrado(10)).toBe(1024);
    });
  });
});
