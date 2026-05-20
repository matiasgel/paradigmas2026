import { describe, it, expect } from "vitest";
import { factorial, makeCounter, makeAdder, makeAccumulator, memoize } from "../src/ej03";

describe("Ej03 — Binding de almacenamiento: closures y recursión", () => {

  // --- factorial (stack-dynamic) ---
  describe("factorial (stack-dynamic)", () => {
    it("factorial(0) = 1 (caso base)", () => expect(factorial(0)).toBe(1));
    it("factorial(1) = 1", () => expect(factorial(1)).toBe(1));
    it("factorial(2) = 2", () => expect(factorial(2)).toBe(2));
    it("factorial(5) = 120", () => expect(factorial(5)).toBe(120));
    it("factorial(10) = 3628800", () => expect(factorial(10)).toBe(3628800));
    it("llamadas consecutivas son independientes (sin estado compartido)", () => {
      expect(factorial(3)).toBe(6);
      expect(factorial(4)).toBe(24);
      expect(factorial(3)).toBe(6);
    });
  });

  // --- makeCounter (heap-dynamic-implicit) ---
  describe("makeCounter (heap-dynamic-implicit)", () => {
    it("increment incrementa de a 1", () => {
      const c = makeCounter(0);
      expect(c.increment()).toBe(1);
      expect(c.increment()).toBe(2);
    });

    it("decrement decrementa de a 1", () => {
      const c = makeCounter(10);
      expect(c.decrement()).toBe(9);
      expect(c.decrement()).toBe(8);
    });

    it("value devuelve el valor actual sin modificarlo (idempotente)", () => {
      const c = makeCounter(5);
      c.increment();
      expect(c.value()).toBe(6);
      expect(c.value()).toBe(6);
    });

    it("reset vuelve al valor inicial", () => {
      const c = makeCounter(3);
      c.increment();
      c.increment();
      expect(c.value()).toBe(5);
      c.reset();
      expect(c.value()).toBe(3);
    });

    it("reset desde valor negativo vuelve al initial", () => {
      const c = makeCounter(0);
      c.decrement();
      c.decrement();
      c.reset();
      expect(c.value()).toBe(0);
    });

    it("dos contadores son independientes (heap separado por closure)", () => {
      const a = makeCounter(0);
      const b = makeCounter(100);
      a.increment();
      a.increment();
      expect(a.value()).toBe(2);
      expect(b.value()).toBe(100);
    });
  });

  // --- makeAdder (closure) ---
  describe("makeAdder (closure / heap-dynamic-implicit)", () => {
    it("makeAdder(3)(4) = 7", () => expect(makeAdder(3)(4)).toBe(7));
    it("makeAdder(0)(x) = x", () => expect(makeAdder(0)(99)).toBe(99));
    it("el n queda fijo en la closure", () => {
      const add5 = makeAdder(5);
      expect(add5(1)).toBe(6);
      expect(add5(10)).toBe(15);
    });
    it("dos closures distintas no interfieren", () => {
      const add2 = makeAdder(2);
      const add3 = makeAdder(3);
      expect(add2(5)).toBe(7);
      expect(add3(5)).toBe(8);
    });
    it("makeAdder(10)(0) = 10", () => expect(makeAdder(10)(0)).toBe(10));
  });

  // --- makeAccumulator ---
  describe("makeAccumulator", () => {
    it("total() inicia en 0", () => {
      const { total } = makeAccumulator();
      expect(total()).toBe(0);
    });
    it("add() suma al acumulado", () => {
      const { add, total } = makeAccumulator();
      add(5);
      add(3);
      expect(total()).toBe(8);
    });
    it("total() es idempotente (no modifica el acumulado)", () => {
      const { add, total } = makeAccumulator();
      add(10);
      expect(total()).toBe(10);
      expect(total()).toBe(10);
    });
    it("dos acumuladores son independientes", () => {
      const a1 = makeAccumulator();
      const a2 = makeAccumulator();
      a1.add(10);
      a2.add(20);
      expect(a1.total()).toBe(10);
      expect(a2.total()).toBe(20);
    });
    it("suma negativa funciona", () => {
      const { add, total } = makeAccumulator();
      add(5);
      add(-3);
      expect(total()).toBe(2);
    });
  });

  // --- memoize ---
  describe("memoize (caché en Map — heap-dynamic-implicit)", () => {
    it("retorna el mismo resultado que fn", () => {
      const double = memoize((n: number) => n * 2);
      expect(double(5)).toBe(10);
      expect(double(3)).toBe(6);
    });
    it("fn se llama solo una vez por valor (caché)", () => {
      let calls = 0;
      const fn = memoize((n: number) => { calls++; return n * n; });
      fn(4); fn(4); fn(4);
      expect(calls).toBe(1);
    });
    it("fn se llama para cada valor diferente", () => {
      let calls = 0;
      const fn = memoize((n: number) => { calls++; return n + 1; });
      fn(1); fn(2); fn(3);
      expect(calls).toBe(3);
    });
    it("dos instancias de memoize son independientes (heaps separados)", () => {
      let c1 = 0, c2 = 0;
      const fn1 = memoize((n: number) => { c1++; return n; });
      const fn2 = memoize((n: number) => { c2++; return n; });
      fn1(5); fn2(5); fn1(5); fn2(5);
      expect(c1).toBe(1);
      expect(c2).toBe(1);
    });
    it("retorna valores correctos después del caché", () => {
      const fn = memoize((n: number) => n * 3);
      expect(fn(10)).toBe(30);
      expect(fn(10)).toBe(30); // desde caché
      expect(fn(20)).toBe(60);
    });
  });
});
