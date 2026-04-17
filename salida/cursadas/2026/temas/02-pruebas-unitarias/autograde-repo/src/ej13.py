class SaldoInsuficienteError(Exception):
    pass


class CuentaBancaria:
    """Cuenta bancaria con depósito, extracción y transferencia."""

    def __init__(self, titular: str, saldo_inicial: float = 0) -> None:
        pass

    def depositar(self, monto: float) -> None:
        """Lanza ValueError si monto <= 0."""
        pass

    def extraer(self, monto: float) -> None:
        """Lanza ValueError si monto <= 0. Lanza SaldoInsuficienteError si no hay fondos."""
        pass

    def transferir(self, destino: 'CuentaBancaria', monto: float) -> None:
        """Extrae de esta cuenta y deposita en destino."""
        pass

    def saldo(self) -> float:
        pass
