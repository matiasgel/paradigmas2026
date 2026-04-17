import unittest
from unittest.mock import patch
from datetime import date
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej20 import GestorTareas, Tarea, TareaNoEncontradaError


class GestorTareasTest(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTareas()
        self.tarea1 = Tarea("Estudiar unittest", date(2026, 4, 20))
        self.tarea2 = Tarea("Entregar TP", date(2026, 4, 25))
        self.tarea_vencida = Tarea("Leer apuntes", date(2026, 3, 1))
        self.gestor.agregar(self.tarea1)
        self.gestor.agregar(self.tarea2)
        self.gestor.agregar(self.tarea_vencida)

    def test_agregar_y_buscar(self):
        tarea = self.gestor.buscar("Estudiar unittest")
        self.assertEqual(tarea.titulo, "Estudiar unittest")

    def test_agregar_duplicada(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar(Tarea("Estudiar unittest", date(2026, 5, 1)))

    def test_completar(self):
        self.gestor.completar("Estudiar unittest")
        pendientes = [t.titulo for t in self.gestor.pendientes()]
        self.assertNotIn("Estudiar unittest", pendientes)

    def test_completar_inexistente(self):
        with self.assertRaises(TareaNoEncontradaError):
            self.gestor.completar("No existe")

    def test_eliminar(self):
        self.gestor.eliminar("Estudiar unittest")
        self.assertEqual(self.gestor.cantidad_total(), 2)

    def test_eliminar_inexistente(self):
        with self.assertRaises(TareaNoEncontradaError):
            self.gestor.eliminar("No existe")

    def test_pendientes(self):
        self.gestor.completar("Estudiar unittest")
        pendientes = self.gestor.pendientes()
        self.assertEqual(len(pendientes), 2)

    def test_vencidas(self):
        with patch('ej20.date') as mock_date:
            mock_date.today.return_value = date(2026, 4, 17)
            mock_date.side_effect = lambda *a, **kw: date(*a, **kw)
            vencidas = self.gestor.vencidas()
            titulos = [t.titulo for t in vencidas]
            self.assertIn("Leer apuntes", titulos)

    def test_cantidad_total(self):
        self.assertEqual(self.gestor.cantidad_total(), 3)

    def test_cantidad_pendientes(self):
        self.gestor.completar("Estudiar unittest")
        self.assertEqual(self.gestor.cantidad_pendientes(), 2)

    def test_str_tarea(self):
        s = str(self.tarea1)
        self.assertIn("Estudiar unittest", s)
        self.assertIn("2026-04-20", s)


if __name__ == '__main__':
    unittest.main()
