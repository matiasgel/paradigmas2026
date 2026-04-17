import unittest
from unittest.mock import patch, mock_open
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej16 import contar_lineas, primera_linea


class ContarLineasTest(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data="hola\nmundo\nchau\n"))
    def test_contar_tres_lineas(self):
        self.assertEqual(contar_lineas("falso.txt"), 3)

    @patch("builtins.open", mock_open(read_data=""))
    def test_contar_archivo_vacio(self):
        resultado = contar_lineas("vacio.txt")
        self.assertIn(resultado, [0, 1])

    @patch("builtins.open", mock_open(read_data="hola\nmundo\n"))
    def test_primera_linea(self):
        self.assertEqual(primera_linea("falso.txt"), "hola")

    @patch("builtins.open", mock_open(read_data="unica"))
    def test_primera_linea_sin_salto(self):
        self.assertEqual(primera_linea("falso.txt"), "unica")


if __name__ == '__main__':
    unittest.main()
