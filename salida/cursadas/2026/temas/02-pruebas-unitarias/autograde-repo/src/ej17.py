class ServicioClima:
    """Servicio externo que devuelve la temperatura (simulado)."""

    def obtener_temperatura(self, ciudad: str) -> float:
        """En producción haría una llamada HTTP. Acá es un placeholder."""
        raise NotImplementedError("Conectar con API real")


def alerta_frio(servicio: ServicioClima, ciudad: str) -> str:
    """
    Consulta la temperatura de una ciudad.
    Retorna '¡Alerta de frío!' si temp < 5.
    Retorna 'Temperatura normal' si 5 <= temp <= 35.
    Retorna '¡Alerta de calor!' si temp > 35.
    """
    pass
