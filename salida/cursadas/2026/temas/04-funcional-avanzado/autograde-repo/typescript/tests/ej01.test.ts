// Tests — Ejercicio 1: Pipeline filter/map/reduce
import { describe, it, expect } from "vitest";
import { filtrarActivasYSumar, obtenerTotalesActivas, contarPorCategoria, Orden } from "../src/ej01";

const ordenes: Orden[] = [
  { id: 1, cliente: "Ana", total: 120, categoria: "elect", activa: true },
  { id: 2, cliente: "Boris", total: 50, categoria: "ropa", activa: false },
  { id: 3, cliente: "Carla", total: 200, categoria: "elect", activa: true },
  { id: 4, cliente: "Diana", total: 30, categoria: "alim", activa: true },
];

describe("filtrarActivasYSumar", () => {
  it("suma totales de activas", () => {
    expect(filtrarActivasYSumar(ordenes)).toBe(350);
  });
  it("retorna 0 para array vacío", () => {
    expect(filtrarActivasYSumar([])).toBe(0);
  });
  it("retorna 0 si ninguna es activa", () => {
    expect(filtrarActivasYSumar([ordenes[1]])).toBe(0);
  });
});

describe("obtenerTotalesActivas", () => {
  it("retorna array de totales de activas", () => {
    expect(obtenerTotalesActivas(ordenes)).toEqual([120, 200, 30]);
  });
  it("retorna [] para array vacío", () => {
    expect(obtenerTotalesActivas([])).toEqual([]);
  });
});

describe("contarPorCategoria", () => {
  it("cuenta por categoría", () => {
    expect(contarPorCategoria(ordenes)).toEqual({ elect: 2, ropa: 1, alim: 1 });
  });
  it("retorna {} para array vacío", () => {
    expect(contarPorCategoria([])).toEqual({});
  });
});
