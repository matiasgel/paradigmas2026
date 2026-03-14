import { esFuncionPura, aplicarMap, sumaRecursiva, curry2, pipe, rangeLazy } from '../src/index';

describe('TP 03 — Programación Funcional (TypeScript)', () => {
  test('esFuncionPura debe detectar funciones puras', () => {
    const pura = () => 42;
    const impura = (() => {
      let i = 0;
      return () => ++i;
    })();

    expect(esFuncionPura(pura)).toBe(true);
    expect(esFuncionPura(impura)).toBe(false);
  });

  test('aplicarMap debe comportarse como Array.prototype.map', () => {
    const nums = [1, 2, 3];
    const result = aplicarMap(nums, (n) => n * 2);
    expect(result).toEqual([2, 4, 6]);
  });

  test('sumaRecursiva debe sumar todos los elementos usando recursión', () => {
    expect(sumaRecursiva([1, 2, 3, 4])).toBe(10);
    expect(sumaRecursiva([])).toBe(0);
  });

  test('curry2 debe currificar funciones de dos argumentos', () => {
    const suma = (a: number, b: number) => a + b;
    const curried = curry2(suma);
    expect(curried(2)(3)).toBe(5);
  });

  test('pipe debe componer funciones de izquierda a derecha', () => {
    const doble = (x: number) => x * 2;
    const masUno = (x: number) => x + 1;
    const pipeline = pipe(doble, masUno);
    expect(pipeline(3)).toBe(7); // (3*2)+1
  });

  test('rangeLazy debe generar números de forma perezosa', () => {
    const gen = rangeLazy(3);
    expect(gen.next().value).toBe(1);
    expect(gen.next().value).toBe(2);
    expect(gen.next().value).toBe(3);
    expect(gen.next().done).toBe(true);
  });
});
