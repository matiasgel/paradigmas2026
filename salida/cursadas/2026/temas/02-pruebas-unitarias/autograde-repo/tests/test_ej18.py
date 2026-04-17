import unittest
from unittest.mock import patch
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej18 import Notificador


class NotificadorTest(unittest.TestCase):

    @patch.object(Notificador, 'enviar_email', return_value=True)
    def test_bienvenida_exitosa(self, mock_enviar):
        n = Notificador()
        self.assertEqual(n.notificar_bienvenida("usuario@test.com"), "enviado")

    @patch.object(Notificador, 'enviar_email', return_value=False)
    def test_bienvenida_fallida(self, mock_enviar):
        n = Notificador()
        self.assertEqual(n.notificar_bienvenida("usuario@test.com"), "error")

    @patch.object(Notificador, 'enviar_email', side_effect=Exception("SMTP error"))
    def test_bienvenida_excepcion(self, mock_enviar):
        n = Notificador()
        self.assertEqual(n.notificar_bienvenida("usuario@test.com"), "error")

    @patch.object(Notificador, 'enviar_email', return_value=True)
    def test_email_correcto(self, mock_enviar):
        n = Notificador()
        n.notificar_bienvenida("usuario@test.com")
        mock_enviar.assert_called_once_with("usuario@test.com", "¡Bienvenido!")


if __name__ == '__main__':
    unittest.main()
