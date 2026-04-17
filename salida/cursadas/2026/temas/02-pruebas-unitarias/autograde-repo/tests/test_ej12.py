import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej12 import ListaOrdenada


class ListaOrdenadaTest(unittest.TestCase):

    def setUp(self):
        self.lista = ListaOrdenada()
        self.lista.insertar(30)
        self.lista.insertar(10)
        self.lista.insertar(20)

    def test_orden_correcto(self):
        self.assertEqual(self.lista.obtener(0), 10)
        self.assertEqual(self.lista.obtener(1), 20)
        self.assertEqual(self.lista.obtener(2), 30)

    def test_tamanio(self):
        self.assertEqual(self.lista.tamanio(), 3)

    def test_contiene_existente(self):
        self.assertTrue(self.lista.contiene(20))

    def test_contiene_inexistente(self):
        self.assertFalse(self.lista.contiene(99))

    def test_indice_fuera_de_rango(self):
        with self.assertRaises(IndexError):
            self.lista.obtener(10)

    def test_insertar_duplicado(self):
        self.lista.insertar(20)
        self.assertEqual(self.lista.tamanio(), 4)


if __name__ == '__main__':
    unittest.main()
