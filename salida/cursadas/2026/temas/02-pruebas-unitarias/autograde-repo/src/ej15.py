class Agenda:
    """
    Gestiona contactos usando el DNI como clave.
    """

    def __init__(self) -> None:
        pass

    def agregar(self, dni: str, nombre: str, apellido: str,
                direccion: str, telefono: str) -> None:
        """
        Registra un contacto.
        Lanza ValueError si DNI no es numérico o no tiene 7-8 dígitos.
        Lanza KeyError si el DNI ya está registrado.
        """
        pass

    def buscar(self, dni: str) -> dict:
        """Retorna los datos del contacto. Lanza KeyError si no existe."""
        pass

    def eliminar(self, dni: str) -> None:
        """Elimina un contacto. Lanza KeyError si no existe."""
        pass

    def listar(self) -> list:
        """Retorna la lista de todos los DNIs registrados."""
        pass

    def cantidad(self) -> int:
        pass
