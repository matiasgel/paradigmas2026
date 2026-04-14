// Tests — Ejercicio 14: Memoization
import { describe, it, expect } from "vitest";
import { memoize, fibonacci, callCounter } from "../src/ej14";

describe("fibonacci", () => {
  it("fib(0) = 0", () => expect(fibonacci(0)).toBe(0));
  it("fib(1) = 1", () => expect(fibonacci(1)).toBe(1));
  it("fib(10) = 55", () => expect(fibonacci(10)).toBe(55));
});

describe("memoize", () => {
  it("retorna mismo resultado", () => {
    const mFib = memoize(fibonacci);
    expect(mFib(10)).toBe(55);
    expect(mFib(10)).toBe(55);
  });
  it("cache funciona con counter", () => {
    let calls = 0;
    const expensive = (n: number) => { calls++; return n * 2; };
    const mExpensive = memoize(expensive);
    mExpensive(5);
    mExpensive(5);
    mExpensive(5);
    expect(calls).toBe(1);
  });
  it("diferentes args se calculan", () => {
    let calls = 0;
    const fn = (n: number) => { calls++; return n; };
    const mFn = memoize(fn);
    mFn(1);
    mFn(2);
    mFn(1);
    expect(calls).toBe(2);
  });
});

describe("callCounter", () => {
  it("cuenta llamadas", () => {
    const counter = callCounter((x: number) => x * 2);
    expect(counter.call(5)).toBe(10);
    expect(counter.call(3)).toBe(6);
    expect(counter.count()).toBe(2);
  });
  it("empieza en 0", () => {
    const counter = callCounter(() => 42);
    expect(counter.count()).toBe(0);
  });
});
