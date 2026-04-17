class Notificador:
    """Sistema de notificaciones."""

    def enviar_email(self, destinatario: str, mensaje: str) -> bool:
        """Simula envío de email. En producción conectaría con SMTP."""
        raise NotImplementedError("Conectar con servidor SMTP")

    def notificar_bienvenida(self, email: str) -> str:
        """Envía un email de bienvenida. Retorna 'enviado' o 'error'."""
        try:
            resultado = self.enviar_email(email, "¡Bienvenido!")
            return "enviado" if resultado else "error"
        except Exception:
            return "error"
