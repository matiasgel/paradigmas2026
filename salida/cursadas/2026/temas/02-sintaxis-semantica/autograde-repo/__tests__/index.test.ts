import { simbolosNoTerminales, esAmbigua, esExpresionValida } from '../src/index';

describe('TP 02 — Sintaxis y Semántica de Lenguajes', () => {
  test('simbolosNoTerminales debe devolver los no terminales de una gramática', () => {
    const reglas = [
      { left: 'S', right: ['A', 'B'] },
      { left: 'A', right: ['a'] },
      { left: 'B', right: ['b'] },
    ];
    expect(simbolosNoTerminales(reglas).sort()).toEqual(['A', 'B', 'S']);
  });

  test('esAmbigua debe reconocer la ambigüedad de la gramática de ejemplo', () => {
    expect(esAmbigua()).toBe(true);
  });

  test('esExpresionValida debe validar expresiones simples del tipo a + b * c', () => {
    expect(esExpresionValida('a + b * c')).toBe(true);
    expect(esExpresionValida('a+b*c')).toBe(true);
    expect(esExpresionValida('a + b')).toBe(false);
    expect(esExpresionValida('x + y * z')).toBe(false);
  });
});
