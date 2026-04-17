import unittest
from unittest.mock import MagicMock
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej17 import ServicioClima, alerta_frio


class AlertaFrioTest(unittest.TestCase):

    def setUp(self):
        self.servicio = MagicMock(spec=ServicioClima)

    def test_alerta_frio(self):
        self.servicio.obtener_temperatura.return_value = -2
        self.assertEqual(alerta_frio(self.servicio, "Ushuaia"), "¡Alerta de frío!")

    def test_temperatura_normal(self):
        self.servicio.obtener_temperatura.return_value = 20
        self.assertEqual(alerta_frio(self.servicio, "BsAs"), "Temperatura normal")

    def test_alerta_calor(self):
        self.servicio.obtener_temperatura.return_value = 40
        self.assertEqual(alerta_frio(self.servicio, "Formosa"), "¡Alerta de calor!")

    def test_borde_frio(self):
        self.servicio.obtener_temperatura.return_value = 5
        self.assertEqual(alerta_frio(self.servicio, "Ushuaia"), "Temperatura normal")

    def test_borde_calor(self):
        self.servicio.obtener_temperatura.return_value = 35
        self.assertEqual(alerta_frio(self.servicio, "Formosa"), "Temperatura normal")

    def test_servicio_llamado(self):
        self.servicio.obtener_temperatura.return_value = 20
        alerta_frio(self.servicio, "Ushuaia")
        self.servicio.obtener_temperatura.assert_called_once_with("Ushuaia")


if __name__ == '__main__':
    unittest.main()
