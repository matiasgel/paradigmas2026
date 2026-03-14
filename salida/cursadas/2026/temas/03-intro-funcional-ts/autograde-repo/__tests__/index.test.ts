import { esFuncionPura, aplicarMap } from '../src/index';

describe('TP 03 — Programación Funcional (TypeScript)', () => {
  test('esFuncionPura debería ser una función y devolver booleano', () => {
    expect(typeof esFuncionPura).toBe('function');
    expect(typeof esFuncionPura(() => 1)).toBe('boolean');
  });

  test('aplicarMap debería comportarse como Array.prototype.map', () => {
    const nums = [1, 2, 3];
    const result = aplicarMap(nums, (n) => n * 2);
    expect(result).toEqual([2, 4, 6]);
  });
});
