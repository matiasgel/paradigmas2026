class CalculadoraError(Exception):
    pass


class Calculadora:
    """Calculadora con historial de operaciones."""

    def __init__(self) -> None:
        pass

    def sumar(self, a: float, b: float) -> float:
        pass

    def restar(self, a: float, b: float) -> float:
        pass

    def multiplicar(self, a: float, b: float) -> float:
        pass

    def dividir(self, a: float, b: float) -> float:
        """Lanza CalculadoraError si b == 0."""
        pass

    def historial(self) -> list:
        """Retorna lista de operaciones realizadas, ej: ['2 + 3 = 5', '10 / 2 = 5.0']"""
        pass

    def limpiar_historial(self) -> None:
        pass
