import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej11 import Contador


class ContadorTest(unittest.TestCase):

    def setUp(self):
        self.contador = Contador(10)

    def test_valor_inicial(self):
        self.assertEqual(self.contador.valor(), 10)

    def test_incrementar(self):
        self.contador.incrementar()
        self.assertEqual(self.contador.valor(), 11)

    def test_decrementar(self):
        self.contador.decrementar()
        self.assertEqual(self.contador.valor(), 9)

    def test_reiniciar(self):
        self.contador.incrementar()
        self.contador.incrementar()
        self.contador.reiniciar()
        self.assertEqual(self.contador.valor(), 10)

    def test_multiples_operaciones(self):
        self.contador.incrementar()
        self.contador.incrementar()
        self.contador.incrementar()
        self.contador.decrementar()
        self.assertEqual(self.contador.valor(), 12)


if __name__ == '__main__':
    unittest.main()
