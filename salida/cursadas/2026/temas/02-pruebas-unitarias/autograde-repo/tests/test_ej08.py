import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej08 import Pila, PilaVaciaError


class PilaTest(unittest.TestCase):

    def test_pila_nueva_esta_vacia(self):
        self.assertTrue(Pila().esta_vacia())

    def test_apilar_y_tope(self):
        p = Pila()
        p.apilar("a")
        self.assertEqual(p.tope(), "a")

    def test_desapilar_retorna_ultimo(self):
        p = Pila()
        p.apilar("a")
        p.apilar("b")
        self.assertEqual(p.desapilar(), "b")

    def test_desapilar_pila_vacia(self):
        with self.assertRaises(PilaVaciaError):
            Pila().desapilar()

    def test_tope_pila_vacia(self):
        with self.assertRaises(PilaVaciaError):
            Pila().tope()

    def test_overflow(self):
        p = Pila(2)
        p.apilar("a")
        p.apilar("b")
        with self.assertRaises(OverflowError):
            p.apilar("c")

    def test_tamanio(self):
        p = Pila()
        p.apilar(1)
        p.apilar(2)
        p.apilar(3)
        self.assertEqual(p.tamanio(), 3)


if __name__ == '__main__':
    unittest.main()
