import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej06 import dividir


class DividirTest(unittest.TestCase):

    def test_division_entera(self):
        self.assertEqual(dividir(10, 2), 5.0)

    def test_division_decimal(self):
        self.assertAlmostEqual(dividir(7, 3), 2.333, places=2)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(7, 0)

    def test_dividir_cero_entre_algo(self):
        self.assertEqual(dividir(0, 5), 0.0)

    def test_dividir_negativos(self):
        self.assertEqual(dividir(-10, 2), -5.0)


if __name__ == '__main__':
    unittest.main()
