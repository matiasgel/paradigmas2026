import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej04 import contar_vocales


class ContarVocalesTest(unittest.TestCase):

    def test_frase_normal(self):
        self.assertEqual(contar_vocales("Hola Mundo"), 4)

    def test_sin_vocales(self):
        self.assertEqual(contar_vocales("xyz"), 0)

    def test_todas_vocales_mayusculas(self):
        self.assertEqual(contar_vocales("AEIOU"), 5)

    def test_cadena_vacia(self):
        self.assertEqual(contar_vocales(""), 0)

    def test_solo_vocales_minusculas(self):
        self.assertEqual(contar_vocales("aeiou"), 5)


if __name__ == '__main__':
    unittest.main()
