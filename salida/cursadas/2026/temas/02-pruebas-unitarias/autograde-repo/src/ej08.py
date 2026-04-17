class PilaVaciaError(Exception):
    """Se lanza al intentar desapilar o ver el tope de una pila vacía."""
    pass


class Pila:
    """Pila (stack) con capacidad limitada."""

    def __init__(self, capacidad: int = 10) -> None:
        pass

    def apilar(self, elemento) -> None:
        """Agrega un elemento. Lanza OverflowError si está llena."""
        pass

    def desapilar(self):
        """Remueve y retorna el tope. Lanza PilaVaciaError si está vacía."""
        pass

    def tope(self):
        """Retorna el tope sin removerlo. Lanza PilaVaciaError si está vacía."""
        pass

    def esta_vacia(self) -> bool:
        pass

    def tamanio(self) -> int:
        pass
