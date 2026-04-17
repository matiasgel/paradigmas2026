import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej05 import es_palindromo


class EsPalindromoTest(unittest.TestCase):

    def test_palindromo_con_espacios(self):
        self.assertTrue(es_palindromo("anita lava la tina"))

    def test_no_palindromo(self):
        self.assertFalse(es_palindromo("hola"))

    def test_palindromo_mixto(self):
        self.assertTrue(es_palindromo("Oso"))

    def test_cadena_vacia(self):
        self.assertTrue(es_palindromo(""))

    def test_un_caracter(self):
        self.assertTrue(es_palindromo("a"))


if __name__ == '__main__':
    unittest.main()
