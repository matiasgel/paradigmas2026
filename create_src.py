import os

base = 'salida/cursadas/2026/temas/02-pruebas-unitarias/autograde-repo'

src_files = {
    'ej02.py': '''def invertir_cadena(texto: str) -> str:
    """Retorna el texto invertido."""
    pass
''',
    'ej03.py': '''def maximo_de_tres(a: int, b: int, c: int) -> int:
    """Retorna el mayor de tres n\u00fameros enteros."""
    pass
''',
    'ej04.py': '''def contar_vocales(texto: str) -> int:
    """Retorna la cantidad de vocales (a, e, i, o, u) en el texto. Case-insensitive."""
    pass
''',
    'ej05.py': '''def es_palindromo(texto: str) -> bool:
    """Retorna True si el texto es un pal\u00edndromo (ignora may\u00fasculas y espacios)."""
    pass
''',
    'ej06.py': '''def dividir(a: float, b: float) -> float:
    """Retorna a / b. Lanza ValueError si b es 0."""
    pass
''',
    'ej07.py': '''def validar_edad(edad: int) -> str:
    """
    Retorna la categor\u00eda de edad:
    - 0-12: \'menor\'
    - 13-17: \'adolescente\'
    - 18-64: \'adulto\'
    - 65+: \'jubilado\'
    Lanza ValueError si edad < 0 o edad > 150.
    """
    pass
''',
    'ej08.py': '''class PilaVaciaError(Exception):
    """Se lanza al intentar desapilar o ver el tope de una pila vac\u00eda."""
    pass


class Pila:
    """Pila (stack) con capacidad limitada."""

    def __init__(self, capacidad: int = 10) -> None:
        pass

    def apilar(self, elemento) -> None:
        """Agrega un elemento. Lanza OverflowError si est\u00e1 llena."""
        pass

    def desapilar(self):
        """Remueve y retorna el tope. Lanza PilaVaciaError si est\u00e1 vac\u00eda."""
        pass

    def tope(self):
        """Retorna el tope sin removerlo. Lanza PilaVaciaError si est\u00e1 vac\u00eda."""
        pass

    def esta_vacia(self) -> bool:
        pass

    def tamanio(self) -> int:
        pass
''',
    'ej09.py': '''def calcular_descuento(precio: float, porcentaje: float) -> float:
    """
    Aplica un descuento porcentual al precio.
    Lanza ValueError si precio < 0, porcentaje < 0, o porcentaje > 100.
    Retorna el precio final redondeado a 2 decimales.
    """
    pass
''',
    'ej10.py': '''def validar_contrasenia(password: str) -> bool:
    """
    Retorna True si la contrase\u00f1a cumple todas las reglas:
    - M\u00ednimo 8 caracteres
    - Al menos una may\u00fascula
    - Al menos una min\u00fascula
    - Al menos un d\u00edgito
    Lanza ValueError con mensaje descriptivo si no cumple alguna regla.
    """
    pass
''',
    'ej11.py': '''class Contador:
    """Contador con valor inicial, incremento y decremento."""

    def __init__(self, inicio: int = 0) -> None:
        pass

    def incrementar(self) -> None:
        pass

    def decrementar(self) -> None:
        pass

    def valor(self) -> int:
        pass

    def reiniciar(self) -> None:
        """Vuelve al valor inicial."""
        pass
''',
    'ej12.py': '''class ListaOrdenada:
    """Lista que mantiene sus elementos ordenados de menor a mayor."""

    def __init__(self) -> None:
        pass

    def insertar(self, elemento) -> None:
        """Inserta manteniendo el orden."""
        pass

    def contiene(self, elemento) -> bool:
        pass

    def obtener(self, indice: int):
        """Retorna el elemento en la posici\u00f3n dada. Lanza IndexError si est\u00e1 fuera de rango."""
        pass

    def tamanio(self) -> int:
        pass

    def __str__(self) -> str:
        pass
''',
    'ej13.py': '''class SaldoInsuficienteError(Exception):
    pass


class CuentaBancaria:
    """Cuenta bancaria con dep\u00f3sito, extracci\u00f3n y transferencia."""

    def __init__(self, titular: str, saldo_inicial: float = 0) -> None:
        pass

    def depositar(self, monto: float) -> None:
        """Lanza ValueError si monto <= 0."""
        pass

    def extraer(self, monto: float) -> None:
        """Lanza ValueError si monto <= 0. Lanza SaldoInsuficienteError si no hay fondos."""
        pass

    def transferir(self, destino: \'CuentaBancaria\', monto: float) -> None:
        """Extrae de esta cuenta y deposita en destino."""
        pass

    def saldo(self) -> float:
        pass
''',
    'ej14.py': '''class ConversorTemperatura:
    """Conversiones entre Celsius, Fahrenheit y Kelvin."""

    @staticmethod
    def celsius_a_fahrenheit(c: float) -> float:
        pass

    @staticmethod
    def fahrenheit_a_celsius(f: float) -> float:
        pass

    @staticmethod
    def celsius_a_kelvin(c: float) -> float:
        """Lanza ValueError si el resultado es menor a 0 K (cero absoluto)."""
        pass

    @staticmethod
    def kelvin_a_celsius(k: float) -> float:
        """Lanza ValueError si k < 0."""
        pass
''',
    'ej15.py': '''class Agenda:
    """
    Gestiona contactos usando el DNI como clave.
    """

    def __init__(self) -> None:
        pass

    def agregar(self, dni: str, nombre: str, apellido: str,
                direccion: str, telefono: str) -> None:
        """
        Registra un contacto.
        Lanza ValueError si DNI no es num\u00e9rico o no tiene 7-8 d\u00edgitos.
        Lanza KeyError si el DNI ya est\u00e1 registrado.
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
''',
    'ej16.py': '''def contar_lineas(ruta: str) -> int:
    """Abre el archivo en ruta y retorna la cantidad de l\u00edneas."""
    with open(ruta, \'r\') as f:
        return len(f.readlines())


def primera_linea(ruta: str) -> str:
    """Retorna la primera l\u00ednea del archivo (sin salto de l\u00ednea). Lanza FileNotFoundError si no existe."""
    with open(ruta, \'r\') as f:
        linea = f.readline()
        return linea.rstrip(\'\\n\')
''',
    'ej17.py': '''class ServicioClima:
    """Servicio externo que devuelve la temperatura (simulado)."""

    def obtener_temperatura(self, ciudad: str) -> float:
        """En producci\u00f3n har\u00eda una llamada HTTP. Ac\u00e1 es un placeholder."""
        raise NotImplementedError("Conectar con API real")


def alerta_frio(servicio: ServicioClima, ciudad: str) -> str:
    """
    Consulta la temperatura de una ciudad.
    Retorna \'\u00a1Alerta de fr\u00edo!\' si temp < 5.
    Retorna \'Temperatura normal\' si 5 <= temp <= 35.
    Retorna \'\u00a1Alerta de calor!\' si temp > 35.
    """
    pass
''',
    'ej18.py': '''class Notificador:
    """Sistema de notificaciones."""

    def enviar_email(self, destinatario: str, mensaje: str) -> bool:
        """Simula env\u00edo de email. En producci\u00f3n conectar\u00eda con SMTP."""
        raise NotImplementedError("Conectar con servidor SMTP")

    def notificar_bienvenida(self, email: str) -> str:
        """Env\u00eda un email de bienvenida. Retorna \'enviado\' o \'error\'."""
        try:
            resultado = self.enviar_email(email, "\u00a1Bienvenido!")
            return "enviado" if resultado else "error"
        except Exception:
            return "error"
''',
    'ej19.py': '''class CalculadoraError(Exception):
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
        """Retorna lista de operaciones realizadas, ej: [\'2 + 3 = 5\', \'10 / 2 = 5.0\']"""
        pass

    def limpiar_historial(self) -> None:
        pass
''',
    'ej20.py': '''from datetime import date


class TareaNoEncontradaError(Exception):
    pass


class Tarea:
    """Representa una tarea con t\u00edtulo, fecha de vencimiento y estado."""

    def __init__(self, titulo: str, vencimiento: date) -> None:
        self.titulo = titulo
        self.vencimiento = vencimiento
        self.completada = False

    def completar(self) -> None:
        self.completada = True

    def esta_vencida(self) -> bool:
        """Retorna True si no est\u00e1 completada y la fecha de vencimiento ya pas\u00f3."""
        pass

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Tarea) and self.titulo == other.titulo

    def __str__(self) -> str:
        estado = "\u2713" if self.completada else "\u2717"
        return f"[{estado}] {self.titulo} (vence: {self.vencimiento})"


class GestorTareas:
    """Gestor de tareas con operaciones CRUD y filtros."""

    def __init__(self) -> None:
        pass

    def agregar(self, tarea: Tarea) -> None:
        """Agrega una tarea. Lanza ValueError si ya existe una con el mismo t\u00edtulo."""
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
        """Busca por t\u00edtulo. Lanza TareaNoEncontradaError si no existe."""
        pass

    def cantidad_total(self) -> int:
        pass

    def cantidad_pendientes(self) -> int:
        pass
''',
}

for fname, content in src_files.items():
    with open(f"{base}/src/{fname}", 'w', encoding='utf-8') as f:
        f.write(content)

print('src done:', len(src_files))
