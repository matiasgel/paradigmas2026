import {
  esNumero,
  sumaArray,
  sumaArrayRecursiva,
  esPar,
  filtrarPares,
  range,
  factorial,
  esPalindromo,
  invertirCadena,
  contarPalabras,
  maxMin,
  aplanar,
  unico,
  agruparPor,
  sumaCuadrados,
  lanzarSiNulo,
  parseNumber,
  dividir,
} from '../src/index';

describe('TP 01 — Conceptos Introductorios', () => {
  test('esNumero debe usar tipado estático y reconocer números', () => {
    expect(esNumero(5)).toBe(true);
    expect(esNumero('5')).toBe(false);
  });

  test('parseNumber debe convertir strings a número o devolver null', () => {
    expect(parseNumber('42')).toBe(42);
    expect(parseNumber('3.14')).toBeCloseTo(3.14);
    expect(parseNumber('hola')).toBeNull();
  });

  test('sumaArray debe sumar correctamente los elementos', () => {
    expect(sumaArray([1, 2, 3, 4])).toBe(10);
    expect(sumaArray([])).toBe(0);
  });

  test('sumaArrayRecursiva debe sumar correctamente usando recursión', () => {
    expect(sumaArrayRecursiva([1, 2, 3, 4])).toBe(10);
    expect(sumaArrayRecursiva([])).toBe(0);
  });

  test('dividir debe lanzar error al dividir por cero', () => {
    expect(dividir(10, 2)).toBe(5);
    expect(() => dividir(10, 0)).toThrow('División por cero');
  });

  test('esPar identifica números pares', () => {
    expect(esPar(4)).toBe(true);
    expect(esPar(5)).toBe(false);
  });

  test('filtrarPares extrae los pares del array', () => {
    expect(filtrarPares([1, 2, 3, 4])).toEqual([2, 4]);
    expect(filtrarPares([])).toEqual([]);
  });

  test('range genera la secuencia correcta', () => {
    expect(range(5)).toEqual([1, 2, 3, 4, 5]);
    expect(range(0)).toEqual([]);
  });

  test('factorial calcula correctamente', () => {
    expect(factorial(0)).toBe(1);
    expect(factorial(5)).toBe(120);
  });

  test('esPalindromo detecta palíndromos', () => {
    expect(esPalindromo('Anita lava la tina')).toBe(true);
    expect(esPalindromo('no es palindromo')).toBe(false);
  });

  test('invertirCadena invierte correctamente', () => {
    expect(invertirCadena('abc')).toBe('cba');
  });

  test('contarPalabras cuenta palabras separadas por espacios', () => {
    expect(contarPalabras('uno dos tres')).toBe(3);
    expect(contarPalabras('   ')).toBe(0);
  });

  test('maxMin devuelve el máximo y mínimo', () => {
    expect(maxMin([5, 1, 9])).toEqual({ max: 9, min: 1 });
  });

  test('aplanar convierte arreglo de arreglos en uno solo', () => {
    expect(aplanar([[1, 2], [3]])).toEqual([1, 2, 3]);
  });

  test('unico elimina duplicados manteniendo orden', () => {
    expect(unico([1, 2, 2, 3])).toEqual([1, 2, 3]);
  });

  test('agruparPor agrupa correctamente según la función clave', () => {
    const arr = [{ n: 1 }, { n: 2 }, { n: 1 }];
    expect(agruparPor(arr, (x) => x.n)).toEqual({ '1': [{ n: 1 }, { n: 1 }], '2': [{ n: 2 }] });
  });

  test('sumaCuadrados suma los cuadrados de los elementos', () => {
    expect(sumaCuadrados([1, 2, 3])).toBe(14);
  });

  test('lanzarSiNulo debe tirar error si recibe null/undefined', () => {
    expect(() => lanzarSiNulo(null)).toThrow();
    expect(() => lanzarSiNulo(undefined)).toThrow();
    expect(lanzarSiNulo(42)).toBe('42');
  });
});
