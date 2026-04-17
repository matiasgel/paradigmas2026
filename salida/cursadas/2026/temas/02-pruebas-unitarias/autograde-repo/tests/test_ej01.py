import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej01 import es_par


class EsParTest(unittest.TestCase):

    def test_par_positivo(self):
        self.assertTrue(es_par(4))

    def test_impar_positivo(self):
        self.assertFalse(es_par(7))

    def test_cero(self):
        self.assertTrue(es_par(0))

    def test_par_negativo(self):
        self.assertTrue(es_par(-2))

    def test_impar_negativo(self):
        self.assertFalse(es_par(-3))


if __name__ == '__main__':
    unittest.main()
