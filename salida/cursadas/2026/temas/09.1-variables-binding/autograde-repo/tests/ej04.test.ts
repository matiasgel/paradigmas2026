import { describe, it, expect } from "vitest";
import {
  scopeChainLookup,
  makeMultiplier,
  makeFunctions,
  makeLogger,
} from "../src/ej04";

describe("Ej04 — Ámbito estático y algoritmo de resolución de nombres", () => {

  // --- scopeChainLookup ---
  describe("scopeChainLookup — algoritmo de ámbito estático", () => {
    it("encuentra en el entorno más interno (scopes[0])", () => {
      const scopes = [{ x: 1 }, { x: 2, y: 3 }];
      expect(scopeChainLookup(scopes, "x")).toBe(1);
    });

    it("busca hacia el exterior si no está en el interno", () => {
      const scopes = [{ x: 1 }, { x: 2, y: 3 }, { z: 5 }];
      expect(scopeChainLookup(scopes, "z")).toBe(5);
    });

    it("retorna undefined si no existe en ningún entorno (scope error)", () => {
      const scopes = [{ x: 1 }, { y: 2 }];
      expect(scopeChainLookup(scopes, "w")).toBeUndefined();
    });

    it("shadowing: el entorno interno opaca al externo", () => {
      const scopes = [{ y: 99 }, { y: 1, z: 2 }, { y: 0 }];
      expect(scopeChainLookup(scopes, "y")).toBe(99);
    });

    it("cadena de un solo entorno — encontrado", () => {
      expect(scopeChainLookup([{ a: 42 }], "a")).toBe(42);
    });

    it("cadena de un solo entorno — no encontrado", () => {
      expect(scopeChainLookup([{ a: 42 }], "b")).toBeUndefined();
    });

    it("accede al entorno más externo cuando no está en ninguno interno", () => {
      const scopes = [{ local: 1 }, { mid: 2 }, { global: 99 }];
      expect(scopeChainLookup(scopes, "global")).toBe(99);
    });
  });

  // --- makeMultiplier ---
  describe("makeMultiplier (ámbito léxico)", () => {
    it("makeMultiplier(3)(5) = 15", () => {
      expect(makeMultiplier(3)(5)).toBe(15);
    });

    it("factor 0 → siempre 0", () => {
      expect(makeMultiplier(0)(999)).toBe(0);
    });

    it("factor 1 → identidad", () => {
      expect(makeMultiplier(1)(7)).toBe(7);
    });

    it("dos multiplicadores no interfieren", () => {
      const doble = makeMultiplier(2);
      const triple = makeMultiplier(3);
      expect(doble(4)).toBe(8);
      expect(triple(4)).toBe(12);
    });

    it("el factor queda capturado en el ámbito léxico", () => {
      const times10 = makeMultiplier(10);
      expect(times10(5)).toBe(50);
      expect(times10(3)).toBe(30);
    });
  });

  // --- makeFunctions (let en loop) ---
  describe("makeFunctions (let en loop — binding correcto)", () => {
    it("cada función devuelve su propio índice", () => {
      const fns = makeFunctions(5);
      for (let i = 0; i < 5; i++) {
        expect(fns[i]()).toBe(i);
      }
    });

    it("makeFunctions(3) retorna exactamente 3 funciones", () => {
      expect(makeFunctions(3)).toHaveLength(3);
    });

    it("makeFunctions(0) retorna array vacío", () => {
      expect(makeFunctions(0)).toHaveLength(0);
    });

    it("las funciones no interfieren entre sí (cada una captura su propio i)", () => {
      const fns = makeFunctions(4);
      expect(fns[0]()).toBe(0);
      expect(fns[3]()).toBe(3);
      expect(fns[0]()).toBe(0); // sigue siendo 0, no 3
    });

    it("makeFunctions(1): único elemento retorna 0", () => {
      const fns = makeFunctions(1);
      expect(fns[0]()).toBe(0);
    });
  });

  // --- makeLogger ---
  describe("makeLogger (\u00e1mbito l\u00e9xico: prefix capturado en la closure)", () => {
    it("antepone el prefijo con ': '", () => {
      const log = makeLogger("[INFO]");
      expect(log("servidor iniciado")).toBe("[INFO]: servidor iniciado");
    });
    it("funciona con prefijos distintos", () => {
      const warn = makeLogger("[WARN]");
      expect(warn("memoria alta")).toBe("[WARN]: memoria alta");
    });
    it("el prefijo queda fijo en la closure (no cambia entre llamadas)", () => {
      const err = makeLogger("[ERROR]");
      expect(err("timeout")).toBe("[ERROR]: timeout");
      expect(err("conexi\u00f3n perd\u00edda")).toBe("[ERROR]: conexi\u00f3n perd\u00edda");
    });
    it("dos loggers son independientes (cada uno captura su propio prefix)", () => {
      const info = makeLogger("[INFO]");
      const debug = makeLogger("[DEBUG]");
      expect(info("ok")).toBe("[INFO]: ok");
      expect(debug("ok")).toBe("[DEBUG]: ok");
    });
    it("prefijo vac\u00edo produce ': msg'", () => {
      const log = makeLogger("");
      expect(log("test")).toBe(": test");
    });
  });
});
