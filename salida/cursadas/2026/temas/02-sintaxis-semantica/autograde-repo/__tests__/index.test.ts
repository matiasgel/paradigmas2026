import { simbolosNoTerminales, esAmbigua } from '../src/index';

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
});
