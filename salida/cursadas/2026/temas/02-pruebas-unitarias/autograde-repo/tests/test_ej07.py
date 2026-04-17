import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej07 import validar_edad


class ValidarEdadTest(unittest.TestCase):

    def test_menor(self):
        self.assertEqual(validar_edad(5), "menor")

    def test_adolescente(self):
        self.assertEqual(validar_edad(15), "adolescente")

    def test_adulto(self):
        self.assertEqual(validar_edad(25), "adulto")

    def test_jubilado(self):
        self.assertEqual(validar_edad(70), "jubilado")

    def test_edad_negativa(self):
        with self.assertRaises(ValueError):
            validar_edad(-1)

    def test_edad_excesiva(self):
        with self.assertRaises(ValueError):
            validar_edad(200)

    def test_borde_menor_adolescente(self):
        self.assertEqual(validar_edad(12), "menor")
        self.assertEqual(validar_edad(13), "adolescente")


if __name__ == '__main__':
    unittest.main()
