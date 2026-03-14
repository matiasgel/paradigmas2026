import { esNumero, sumaArray, lanzarSiNulo } from '../src/index';

describe('TP 01 — Conceptos Introductorios', () => {
  test('esNumero debe usar tipado estático y reconocer números', () => {
    expect(esNumero(5)).toBe(true);
    expect(esNumero('5')).toBe(false);
  });

  test('sumaArray debe sumar correctamente los elementos', () => {
    expect(sumaArray([1, 2, 3, 4])).toBe(10);
    expect(sumaArray([])).toBe(0);
  });

  test('lanzarSiNulo debe tirar error si recibe null/undefined', () => {
    expect(() => lanzarSiNulo(null)).toThrow();
    expect(() => lanzarSiNulo(undefined)).toThrow();
    expect(lanzarSiNulo(42)).toBe('42');
  });
});
