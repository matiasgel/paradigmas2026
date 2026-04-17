import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej13 import CuentaBancaria, SaldoInsuficienteError


class CuentaBancariaTest(unittest.TestCase):

    def test_saldo_inicial(self):
        self.assertEqual(CuentaBancaria("Ana", 1000).saldo(), 1000)

    def test_depositar(self):
        c = CuentaBancaria("Ana", 1000)
        c.depositar(500)
        self.assertEqual(c.saldo(), 1500)

    def test_depositar_monto_negativo(self):
        with self.assertRaises(ValueError):
            CuentaBancaria("Ana").depositar(-100)

    def test_extraer(self):
        c = CuentaBancaria("Ana", 1000)
        c.extraer(200)
        self.assertEqual(c.saldo(), 800)

    def test_extraer_sin_fondos(self):
        with self.assertRaises(SaldoInsuficienteError):
            CuentaBancaria("Ana", 1000).extraer(5000)

    def test_extraer_monto_negativo(self):
        with self.assertRaises(ValueError):
            CuentaBancaria("Ana", 1000).extraer(-100)

    def test_transferir(self):
        a = CuentaBancaria("Ana", 1000)
        b = CuentaBancaria("Luis", 0)
        a.transferir(b, 300)
        self.assertEqual(a.saldo(), 700)
        self.assertEqual(b.saldo(), 300)

    def test_transferir_sin_fondos(self):
        a = CuentaBancaria("Ana", 100)
        b = CuentaBancaria("Luis", 0)
        with self.assertRaises(SaldoInsuficienteError):
            a.transferir(b, 500)


if __name__ == '__main__':
    unittest.main()
