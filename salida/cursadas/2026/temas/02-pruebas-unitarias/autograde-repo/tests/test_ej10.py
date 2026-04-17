import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej10 import validar_contrasenia


class ValidarContraseniaTest(unittest.TestCase):

    def test_contrasenia_valida(self):
        self.assertTrue(validar_contrasenia("Abc12345"))

    def test_muy_corta(self):
        with self.assertRaises(ValueError):
            validar_contrasenia("Ab1")

    def test_sin_mayuscula(self):
        with self.assertRaises(ValueError):
            validar_contrasenia("abcdefg1")

    def test_sin_minuscula(self):
        with self.assertRaises(ValueError):
            validar_contrasenia("ABCDEFG1")

    def test_sin_digito(self):
        with self.assertRaises(ValueError):
            validar_contrasenia("Abcdefgh")

    def test_exacto_8_caracteres(self):
        self.assertTrue(validar_contrasenia("Abcdefg1"))


if __name__ == '__main__':
    unittest.main()
