import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej19 import Calculadora, CalculadoraError


class CalculadoraTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumas_parametrizadas(self):
        casos = [(1, 1, 2), (0, 0, 0), (-1, 1, 0), (100, 200, 300)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.sumar(a, b), esperado)

    def test_restas_parametrizadas(self):
        casos = [(5, 3, 2), (0, 0, 0), (-1, -1, 0), (100, 50, 50)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.restar(a, b), esperado)

    def test_multiplicaciones_parametrizadas(self):
        casos = [(2, 3, 6), (0, 5, 0), (-2, 3, -6), (1, 100, 100)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiplicar(a, b), esperado)

    def test_dividir_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_dividir_por_cero(self):
        with self.assertRaises(CalculadoraError):
            self.calc.dividir(5, 0)

    def test_historial(self):
        self.calc.sumar(1, 2)
        self.calc.restar(5, 3)
        self.calc.multiplicar(2, 4)
        self.assertEqual(len(self.calc.historial()), 3)

    def test_limpiar_historial(self):
        self.calc.sumar(1, 2)
        self.calc.limpiar_historial()
        self.assertEqual(self.calc.historial(), [])


if __name__ == '__main__':
    unittest.main()
