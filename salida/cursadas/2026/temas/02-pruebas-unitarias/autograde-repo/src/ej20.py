from datetime import date


class TareaNoEncontradaError(Exception):
    pass


class Tarea:
    """Representa una tarea con título, fecha de vencimiento y estado."""

    def __init__(self, titulo: str, vencimiento: date) -> None:
        self.titulo = titulo
        self.vencimiento = vencimiento
        self.completada = False

    def completar(self) -> None:
        self.completada = True

    def esta_vencida(self) -> bool:
        """Retorna True si no está completada y la fecha de vencimiento ya pasó."""
        pass

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Tarea) and self.titulo == other.titulo

    def __str__(self) -> str:
        estado = "✓" if self.completada else "✗"
        return f"[{estado}] {self.titulo} (vence: {self.vencimiento})"


class GestorTareas:
    """Gestor de tareas con operaciones CRUD y filtros."""

    def __init__(self) -> None:
        pass

    def agregar(self, tarea: Tarea) -> None:
        """Agrega una tarea. Lanza ValueError si ya existe una con el mismo título."""
        pass

    def completar(self, titulo: str) -> None:
        """Marca como completada. Lanza TareaNoEncontradaError si no existe."""
        pass

    def eliminar(self, titulo: str) -> None:
        """Elimina una tarea. Lanza TareaNoEncontradaError si no existe."""
        pass

    def pendientes(self) -> list:
        """Retorna las tareas no completadas."""
        pass

    def vencidas(self) -> list:
        """Retorna las tareas vencidas (no completadas y fecha pasada)."""
        pass

    def buscar(self, titulo: str) -> Tarea:
        """Busca por título. Lanza TareaNoEncontradaError si no existe."""
        pass

    def cantidad_total(self) -> int:
        pass

    def cantidad_pendientes(self) -> int:
        pass
