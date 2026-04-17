import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej03 import maximo_de_tres


class MaximoDeTresTest(unittest.TestCase):

    def test_tercero_mayor(self):
        self.assertEqual(maximo_de_tres(1, 2, 3), 3)

    def test_primero_mayor(self):
        self.assertEqual(maximo_de_tres(9, 2, 3), 9)

    def test_segundo_mayor(self):
        self.assertEqual(maximo_de_tres(1, 8, 3), 8)

    def test_todos_iguales(self):
        self.assertEqual(maximo_de_tres(5, 5, 5), 5)

    def test_negativos(self):
        self.assertEqual(maximo_de_tres(-1, -2, -3), -1)


if __name__ == '__main__':
    unittest.main()
