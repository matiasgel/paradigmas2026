import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej15 import Agenda


class AgendaTest(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()
        self.agenda.agregar("12345678", "Juan", "Pérez", "Calle 1", "2901-111")
        self.agenda.agregar("87654321", "Ana", "García", "Calle 2", "2901-222")

    def test_agregar_y_buscar(self):
        contacto = self.agenda.buscar("12345678")
        self.assertEqual(contacto["nombre"], "Juan")
        self.assertEqual(contacto["apellido"], "Pérez")

    def test_agregar_duplicado(self):
        with self.assertRaises(KeyError):
            self.agenda.agregar("12345678", "Otro", "Nombre", "Calle 3", "2901-333")

    def test_dni_no_numerico(self):
        with self.assertRaises(ValueError):
            self.agenda.agregar("abc", "Juan", "Pérez", "Calle 1", "2901-111")

    def test_dni_muy_corto(self):
        with self.assertRaises(ValueError):
            self.agenda.agregar("123", "Juan", "Pérez", "Calle 1", "2901-111")

    def test_dni_muy_largo(self):
        with self.assertRaises(ValueError):
            self.agenda.agregar("123456789", "Juan", "Pérez", "Calle 1", "2901-111")

    def test_buscar_inexistente(self):
        with self.assertRaises(KeyError):
            self.agenda.buscar("99999999")

    def test_eliminar_existente(self):
        self.agenda.eliminar("12345678")
        self.assertEqual(self.agenda.cantidad(), 1)

    def test_eliminar_inexistente(self):
        with self.assertRaises(KeyError):
            self.agenda.eliminar("99999999")

    def test_listar(self):
        dnis = self.agenda.listar()
        self.assertIn("12345678", dnis)
        self.assertIn("87654321", dnis)

    def test_cantidad(self):
        self.assertEqual(self.agenda.cantidad(), 2)


if __name__ == '__main__':
    unittest.main()
