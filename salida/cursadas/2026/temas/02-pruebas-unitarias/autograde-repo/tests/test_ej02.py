import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej02 import invertir_cadena


class InvertirCadenaTest(unittest.TestCase):

    def test_palabra_normal(self):
        self.assertEqual(invertir_cadena("hola"), "aloh")

    def test_cadena_vacia(self):
        self.assertEqual(invertir_cadena(""), "")

    def test_un_caracter(self):
        self.assertEqual(invertir_cadena("a"), "a")

    def test_palindromo(self):
        self.assertEqual(invertir_cadena("anana"), "anana")

    def test_con_espacios(self):
        self.assertEqual(invertir_cadena("hola mundo"), "odnum aloh")


if __name__ == '__main__':
    unittest.main()
