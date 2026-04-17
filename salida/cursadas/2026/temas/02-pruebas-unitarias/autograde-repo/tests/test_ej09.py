import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej09 import calcular_descuento


class CalcularDescuentoTest(unittest.TestCase):

    def test_descuento_normal(self):
        self.assertEqual(calcular_descuento(100, 25), 75.0)

    def test_sin_descuento(self):
        self.assertEqual(calcular_descuento(200, 0), 200.0)

    def test_descuento_total(self):
        self.assertEqual(calcular_descuento(50, 100), 0.0)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            calcular_descuento(-10, 20)

    def test_porcentaje_negativo(self):
        with self.assertRaises(ValueError):
            calcular_descuento(100, -5)

    def test_porcentaje_mayor_100(self):
        with self.assertRaises(ValueError):
            calcular_descuento(100, 150)

    def test_redondeo(self):
        resultado = calcular_descuento(99.99, 33)
        self.assertAlmostEqual(resultado, round(resultado, 2), places=2)


if __name__ == '__main__':
    unittest.main()
