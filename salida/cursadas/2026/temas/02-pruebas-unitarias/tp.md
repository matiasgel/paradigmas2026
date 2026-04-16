# Trabajo Práctico N° 2 — Pruebas Unitarias

## Laboratorio de Programación y Lenguajes (IF009)
### Universidad Nacional de Tierra del Fuego — Instituto IDEI
### Ciclo Lectivo 2026 — 1er Cuatrimestre

**Tema:** 02 — Pruebas Unitarias  
**Modalidad:** Repositorio con autograding (GitHub Classroom)  
**Fecha de entrega:** Semana 6  
**Lenguaje:** Python 3.12+  
**Framework:** `unittest` (stdlib)

---

## Instrucciones Generales

1. Aceptá la asignación de GitHub Classroom (link en el aula virtual).
2. Cloná el repositorio en GitHub Codespaces o en tu máquina local.
3. Cada ejercicio tiene su propio archivo de test (`test_ejNN.py`) y su archivo de implementación (`ejNN.py`).
4. Ejecutá los tests con: `python -m unittest discover -v`
5. Los tests de autograding se ejecutan automáticamente al hacer `push`. Tu nota se calcula según la cantidad de tests que pasen.
6. **Regla TDD:** En los ejercicios marcados con 🔴🟢🔁, escribí el test **antes** de la implementación.

### Estructura del repositorio

```
tp-02-pruebas-unitarias/
├── ej01.py ... ej20.py         # Archivos de implementación
├── test_ej01.py ... test_ej20.py   # Archivos de test
├── README.md
└── .github/
    └── workflows/
        └── classroom.yml       # Autograding
```

---

## Bloque A — Aserciones Básicas (Ejercicios 1–5)

---

### Ejercicio 1 — `es_par`

**Objetivo:** Escribir una función y testearla con `assertEqual` y `assertTrue`/`assertFalse`.

**Implementar en `ej01.py`:**

```python
def es_par(n: int) -> bool:
    """Retorna True si n es par, False si es impar."""
    ...
```

**Ejemplo:**

```python
>>> es_par(4)
True
>>> es_par(7)
False
>>> es_par(0)
True
```

**Tests requeridos en `test_ej01.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_par_positivo` | `es_par(4)` retorna `True` |
| `test_impar_positivo` | `es_par(7)` retorna `False` |
| `test_cero` | `es_par(0)` retorna `True` |
| `test_par_negativo` | `es_par(-2)` retorna `True` |
| `test_impar_negativo` | `es_par(-3)` retorna `False` |

---

### Ejercicio 2 — `invertir_cadena`

**Objetivo:** Practicar `assertEqual` con strings.

**Implementar en `ej02.py`:**

```python
def invertir_cadena(texto: str) -> str:
    """Retorna el texto invertido."""
    ...
```

**Ejemplo:**

```python
>>> invertir_cadena("hola")
'aloh'
>>> invertir_cadena("")
''
>>> invertir_cadena("a")
'a'
```

**Tests requeridos en `test_ej02.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_palabra_normal` | `invertir_cadena("hola")` → `"aloh"` |
| `test_cadena_vacia` | `invertir_cadena("")` → `""` |
| `test_un_caracter` | `invertir_cadena("a")` → `"a"` |
| `test_palindromo` | `invertir_cadena("anana")` → `"anana"` |
| `test_con_espacios` | `invertir_cadena("hola mundo")` → `"odnum aloh"` |

---

### Ejercicio 3 — `maximo_de_tres`

**Objetivo:** Testear múltiples caminos de ejecución con `assertEqual`.

**Implementar en `ej03.py`:**

```python
def maximo_de_tres(a: int, b: int, c: int) -> int:
    """Retorna el mayor de tres números enteros."""
    ...
```

**Ejemplo:**

```python
>>> maximo_de_tres(1, 2, 3)
3
>>> maximo_de_tres(5, 5, 5)
5
>>> maximo_de_tres(-1, -2, -3)
-1
```

**Tests requeridos en `test_ej03.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_tercero_mayor` | `maximo_de_tres(1, 2, 3)` → `3` |
| `test_primero_mayor` | `maximo_de_tres(9, 2, 3)` → `9` |
| `test_segundo_mayor` | `maximo_de_tres(1, 8, 3)` → `8` |
| `test_todos_iguales` | `maximo_de_tres(5, 5, 5)` → `5` |
| `test_negativos` | `maximo_de_tres(-1, -2, -3)` → `-1` |

---

### Ejercicio 4 — `contar_vocales`

**Objetivo:** Practicar `assertEqual` con conteos y casos de borde.

**Implementar en `ej04.py`:**

```python
def contar_vocales(texto: str) -> int:
    """Retorna la cantidad de vocales (a, e, i, o, u) en el texto. Case-insensitive."""
    ...
```

**Ejemplo:**

```python
>>> contar_vocales("Hola Mundo")
4
>>> contar_vocales("xyz")
0
>>> contar_vocales("AEIOU")
5
```

**Tests requeridos en `test_ej04.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_frase_normal` | `contar_vocales("Hola Mundo")` → `4` |
| `test_sin_vocales` | `contar_vocales("xyz")` → `0` |
| `test_todas_vocales_mayusculas` | `contar_vocales("AEIOU")` → `5` |
| `test_cadena_vacia` | `contar_vocales("")` → `0` |
| `test_solo_vocales_minusculas` | `contar_vocales("aeiou")` → `5` |

---

### Ejercicio 5 — `es_palindromo`

**Objetivo:** Testear con `assertTrue` y `assertFalse` en un caso real.

**Implementar en `ej05.py`:**

```python
def es_palindromo(texto: str) -> bool:
    """Retorna True si el texto es un palíndromo (ignora mayúsculas y espacios)."""
    ...
```

**Ejemplo:**

```python
>>> es_palindromo("anita lava la tina")
True
>>> es_palindromo("hola")
False
>>> es_palindromo("Oso")
True
```

**Tests requeridos en `test_ej05.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_palindromo_con_espacios` | `es_palindromo("anita lava la tina")` → `True` |
| `test_no_palindromo` | `es_palindromo("hola")` → `False` |
| `test_palindromo_mixto` | `es_palindromo("Oso")` → `True` |
| `test_cadena_vacia` | `es_palindromo("")` → `True` |
| `test_un_caracter` | `es_palindromo("a")` → `True` |

---

## Bloque B — Excepciones y Validaciones (Ejercicios 6–10)

---

### Ejercicio 6 — `dividir`

**Objetivo:** Testear excepciones con `assertRaises`.

**Implementar en `ej06.py`:**

```python
def dividir(a: float, b: float) -> float:
    """Retorna a / b. Lanza ValueError si b es 0."""
    ...
```

**Ejemplo:**

```python
>>> dividir(10, 2)
5.0
>>> dividir(7, 0)
ValueError: No se puede dividir por cero
```

**Tests requeridos en `test_ej06.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_division_entera` | `dividir(10, 2)` → `5.0` |
| `test_division_decimal` | `dividir(7, 3)` → resultado cercano a `2.333...` (usar `assertAlmostEqual`) |
| `test_dividir_por_cero` | `dividir(7, 0)` lanza `ValueError` |
| `test_dividir_cero_entre_algo` | `dividir(0, 5)` → `0.0` |
| `test_dividir_negativos` | `dividir(-10, 2)` → `-5.0` |

---

### Ejercicio 7 — `validar_edad`

**Objetivo:** Testear múltiples condiciones de validación con excepciones.

**Implementar en `ej07.py`:**

```python
def validar_edad(edad: int) -> str:
    """
    Retorna la categoría de edad:
    - 0-12: 'menor'
    - 13-17: 'adolescente'
    - 18-64: 'adulto'
    - 65+: 'jubilado'
    Lanza ValueError si edad < 0 o edad > 150.
    """
    ...
```

**Ejemplo:**

```python
>>> validar_edad(5)
'menor'
>>> validar_edad(25)
'adulto'
>>> validar_edad(-1)
ValueError: Edad inválida: -1
```

**Tests requeridos en `test_ej07.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_menor` | `validar_edad(5)` → `"menor"` |
| `test_adolescente` | `validar_edad(15)` → `"adolescente"` |
| `test_adulto` | `validar_edad(25)` → `"adulto"` |
| `test_jubilado` | `validar_edad(70)` → `"jubilado"` |
| `test_edad_negativa` | `validar_edad(-1)` lanza `ValueError` |
| `test_edad_excesiva` | `validar_edad(200)` lanza `ValueError` |
| `test_borde_menor_adolescente` | `validar_edad(12)` → `"menor"`, `validar_edad(13)` → `"adolescente"` |

---

### Ejercicio 8 — `Pila` (clase con excepciones)

**Objetivo:** Testear una clase con estado y excepciones propias.

**Implementar en `ej08.py`:**

```python
class PilaVaciaError(Exception):
    """Se lanza al intentar desapilar o ver el tope de una pila vacía."""
    pass

class Pila:
    """Pila (stack) con capacidad limitada."""

    def __init__(self, capacidad: int = 10) -> None:
        ...

    def apilar(self, elemento) -> None:
        """Agrega un elemento. Lanza OverflowError si está llena."""
        ...

    def desapilar(self):
        """Remueve y retorna el tope. Lanza PilaVaciaError si está vacía."""
        ...

    def tope(self):
        """Retorna el tope sin removerlo. Lanza PilaVaciaError si está vacía."""
        ...

    def esta_vacia(self) -> bool:
        ...

    def tamanio(self) -> int:
        ...
```

**Ejemplo:**

```python
>>> p = Pila(3)
>>> p.apilar("a")
>>> p.apilar("b")
>>> p.tope()
'b'
>>> p.desapilar()
'b'
>>> p.tamanio()
1
```

**Tests requeridos en `test_ej08.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_pila_nueva_esta_vacia` | `Pila().esta_vacia()` → `True` |
| `test_apilar_y_tope` | Apilar `"a"` → `tope()` retorna `"a"` |
| `test_desapilar_retorna_ultimo` | Apilar `"a"`, `"b"` → `desapilar()` retorna `"b"` |
| `test_desapilar_pila_vacia` | `Pila().desapilar()` lanza `PilaVaciaError` |
| `test_tope_pila_vacia` | `Pila().tope()` lanza `PilaVaciaError` |
| `test_overflow` | Apilar más elementos que la capacidad lanza `OverflowError` |
| `test_tamanio` | Apilar 3 elementos → `tamanio()` retorna `3` |

---

### Ejercicio 9 — `calcular_descuento`

**Objetivo:** Testear valores límite (boundary testing).

**Implementar en `ej09.py`:**

```python
def calcular_descuento(precio: float, porcentaje: float) -> float:
    """
    Aplica un descuento porcentual al precio.
    Lanza ValueError si precio < 0, porcentaje < 0, o porcentaje > 100.
    Retorna el precio final redondeado a 2 decimales.
    """
    ...
```

**Ejemplo:**

```python
>>> calcular_descuento(100, 25)
75.0
>>> calcular_descuento(200, 0)
200.0
>>> calcular_descuento(100, -5)
ValueError: Porcentaje inválido: -5
```

**Tests requeridos en `test_ej09.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_descuento_normal` | `calcular_descuento(100, 25)` → `75.0` |
| `test_sin_descuento` | `calcular_descuento(200, 0)` → `200.0` |
| `test_descuento_total` | `calcular_descuento(50, 100)` → `0.0` |
| `test_precio_negativo` | `calcular_descuento(-10, 20)` lanza `ValueError` |
| `test_porcentaje_negativo` | `calcular_descuento(100, -5)` lanza `ValueError` |
| `test_porcentaje_mayor_100` | `calcular_descuento(100, 150)` lanza `ValueError` |
| `test_redondeo` | `calcular_descuento(99.99, 33)` → resultado con 2 decimales |

---

### Ejercicio 10 — `validar_contrasenia`

**Objetivo:** Testear múltiples reglas de validación.

**Implementar en `ej10.py`:**

```python
def validar_contrasenia(password: str) -> bool:
    """
    Retorna True si la contraseña cumple todas las reglas:
    - Mínimo 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un dígito
    Lanza ValueError con mensaje descriptivo si no cumple alguna regla.
    """
    ...
```

**Ejemplo:**

```python
>>> validar_contrasenia("Abc12345")
True
>>> validar_contrasenia("abc")
ValueError: La contraseña debe tener al menos 8 caracteres
>>> validar_contrasenia("abcdefgh")
ValueError: La contraseña debe tener al menos una mayúscula
```

**Tests requeridos en `test_ej10.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_contrasenia_valida` | `validar_contrasenia("Abc12345")` → `True` |
| `test_muy_corta` | `validar_contrasenia("Ab1")` lanza `ValueError` |
| `test_sin_mayuscula` | `validar_contrasenia("abcdefg1")` lanza `ValueError` |
| `test_sin_minuscula` | `validar_contrasenia("ABCDEFG1")` lanza `ValueError` |
| `test_sin_digito` | `validar_contrasenia("Abcdefgh")` lanza `ValueError` |
| `test_exacto_8_caracteres` | `validar_contrasenia("Abcdefg1")` → `True` |

---

## Bloque C — Fixtures y Clases bajo Test (Ejercicios 11–15)

---

### Ejercicio 11 — `Contador` con `setUp` 🔴🟢🔁

**Objetivo:** Usar `setUp` para preparar el estado antes de cada test. Aplicar TDD.

**Implementar en `ej11.py`:**

```python
class Contador:
    """Contador con valor inicial, incremento y decremento."""

    def __init__(self, inicio: int = 0) -> None:
        ...

    def incrementar(self) -> None:
        ...

    def decrementar(self) -> None:
        ...

    def valor(self) -> int:
        ...

    def reiniciar(self) -> None:
        """Vuelve al valor inicial."""
        ...
```

**Ejemplo:**

```python
>>> c = Contador(10)
>>> c.incrementar()
>>> c.incrementar()
>>> c.valor()
12
>>> c.reiniciar()
>>> c.valor()
10
```

**Tests requeridos en `test_ej11.py`:**

```python
class ContadorTest(unittest.TestCase):

    def setUp(self):
        self.contador = Contador(10)
```

| Test | Qué verifica |
|------|-------------|
| `test_valor_inicial` | `self.contador.valor()` → `10` |
| `test_incrementar` | Después de `incrementar()`, `valor()` → `11` |
| `test_decrementar` | Después de `decrementar()`, `valor()` → `9` |
| `test_reiniciar` | Incrementar dos veces, `reiniciar()`, `valor()` → `10` |
| `test_multiples_operaciones` | Incrementar 3 veces, decrementar 1 → `valor()` → `12` |

---

### Ejercicio 12 — `ListaOrdenada` con `setUp` y `tearDown`

**Objetivo:** Practicar fixtures completas con una estructura de datos.

**Implementar en `ej12.py`:**

```python
class ListaOrdenada:
    """Lista que mantiene sus elementos ordenados de menor a mayor."""

    def __init__(self) -> None:
        ...

    def insertar(self, elemento) -> None:
        """Inserta manteniendo el orden."""
        ...

    def contiene(self, elemento) -> bool:
        ...

    def obtener(self, indice: int):
        """Retorna el elemento en la posición dada. Lanza IndexError si está fuera de rango."""
        ...

    def tamanio(self) -> int:
        ...

    def __str__(self) -> str:
        ...
```

**Ejemplo:**

```python
>>> lo = ListaOrdenada()
>>> lo.insertar(3)
>>> lo.insertar(1)
>>> lo.insertar(2)
>>> lo.obtener(0)
1
>>> lo.obtener(2)
3
>>> lo.tamanio()
3
```

**Tests requeridos en `test_ej12.py`:**

```python
class ListaOrdenadaTest(unittest.TestCase):

    def setUp(self):
        self.lista = ListaOrdenada()
        self.lista.insertar(30)
        self.lista.insertar(10)
        self.lista.insertar(20)
```

| Test | Qué verifica |
|------|-------------|
| `test_orden_correcto` | `obtener(0)` → `10`, `obtener(1)` → `20`, `obtener(2)` → `30` |
| `test_tamanio` | `tamanio()` → `3` |
| `test_contiene_existente` | `contiene(20)` → `True` |
| `test_contiene_inexistente` | `contiene(99)` → `False` |
| `test_indice_fuera_de_rango` | `obtener(10)` lanza `IndexError` |
| `test_insertar_duplicado` | Insertar `20` de nuevo → `tamanio()` → `4` |

---

### Ejercicio 13 — `CuentaBancaria` 🔴🟢🔁

**Objetivo:** TDD sobre una clase con reglas de negocio y excepciones.

**Implementar en `ej13.py`:**

```python
class SaldoInsuficienteError(Exception):
    pass

class CuentaBancaria:
    """Cuenta bancaria con depósito, extracción y transferencia."""

    def __init__(self, titular: str, saldo_inicial: float = 0) -> None:
        ...

    def depositar(self, monto: float) -> None:
        """Lanza ValueError si monto <= 0."""
        ...

    def extraer(self, monto: float) -> None:
        """Lanza ValueError si monto <= 0. Lanza SaldoInsuficienteError si no hay fondos."""
        ...

    def transferir(self, destino: 'CuentaBancaria', monto: float) -> None:
        """Extrae de esta cuenta y deposita en destino."""
        ...

    def saldo(self) -> float:
        ...
```

**Ejemplo:**

```python
>>> cuenta = CuentaBancaria("Ana", 1000)
>>> cuenta.depositar(500)
>>> cuenta.saldo()
1500
>>> cuenta.extraer(200)
>>> cuenta.saldo()
1300
>>> cuenta.extraer(5000)
SaldoInsuficienteError: Saldo insuficiente
```

**Tests requeridos en `test_ej13.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_saldo_inicial` | `CuentaBancaria("Ana", 1000).saldo()` → `1000` |
| `test_depositar` | Depositar 500 → saldo aumenta |
| `test_depositar_monto_negativo` | `depositar(-100)` lanza `ValueError` |
| `test_extraer` | Extraer 200 de 1000 → saldo 800 |
| `test_extraer_sin_fondos` | Extraer 5000 de 1000 lanza `SaldoInsuficienteError` |
| `test_extraer_monto_negativo` | `extraer(-100)` lanza `ValueError` |
| `test_transferir` | Transferir 300 de cuenta A a B → saldos correctos en ambas |
| `test_transferir_sin_fondos` | Transferir más de lo que hay lanza `SaldoInsuficienteError` |

---

### Ejercicio 14 — `ConversorTemperatura` con `assertAlmostEqual`

**Objetivo:** Testear cálculos con punto flotante.

**Implementar en `ej14.py`:**

```python
class ConversorTemperatura:
    """Conversiones entre Celsius, Fahrenheit y Kelvin."""

    @staticmethod
    def celsius_a_fahrenheit(c: float) -> float:
        ...

    @staticmethod
    def fahrenheit_a_celsius(f: float) -> float:
        ...

    @staticmethod
    def celsius_a_kelvin(c: float) -> float:
        """Lanza ValueError si el resultado es menor a 0 K (cero absoluto)."""
        ...

    @staticmethod
    def kelvin_a_celsius(k: float) -> float:
        """Lanza ValueError si k < 0."""
        ...
```

**Ejemplo:**

```python
>>> ConversorTemperatura.celsius_a_fahrenheit(100)
212.0
>>> ConversorTemperatura.celsius_a_kelvin(0)
273.15
>>> ConversorTemperatura.celsius_a_kelvin(-300)
ValueError: Temperatura por debajo del cero absoluto
```

**Tests requeridos en `test_ej14.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_celsius_a_fahrenheit_100` | `celsius_a_fahrenheit(100)` → `212.0` |
| `test_celsius_a_fahrenheit_0` | `celsius_a_fahrenheit(0)` → `32.0` |
| `test_fahrenheit_a_celsius_32` | `fahrenheit_a_celsius(32)` → `0.0` |
| `test_celsius_a_kelvin_0` | `celsius_a_kelvin(0)` → `273.15` (usar `assertAlmostEqual`) |
| `test_kelvin_negativo` | `kelvin_a_celsius(-10)` lanza `ValueError` |
| `test_cero_absoluto` | `celsius_a_kelvin(-273.15)` → `0.0` (usar `assertAlmostEqual`) |

---

### Ejercicio 15 — `Agenda` (integrador del módulo) 🔴🟢🔁

**Objetivo:** Integrador — aplicar TDD sobre la clase Agenda vista en las filminas.

**Implementar en `ej15.py`:**

```python
class Agenda:
    """
    Gestiona contactos usando el DNI como clave.
    Origen: filminas 2025, 'python-testing.pdf'.
    """

    def __init__(self) -> None:
        ...

    def agregar(self, dni: str, nombre: str, apellido: str,
                direccion: str, telefono: str) -> None:
        """
        Registra un contacto.
        Lanza ValueError si DNI no es numérico o no tiene 7-8 dígitos.
        Lanza KeyError si el DNI ya está registrado.
        """
        ...

    def buscar(self, dni: str) -> dict:
        """Retorna los datos del contacto. Lanza KeyError si no existe."""
        ...

    def eliminar(self, dni: str) -> None:
        """Elimina un contacto. Lanza KeyError si no existe."""
        ...

    def listar(self) -> list[str]:
        """Retorna la lista de todos los DNIs registrados."""
        ...

    def cantidad(self) -> int:
        ...
```

**Ejemplo:**

```python
>>> ag = Agenda()
>>> ag.agregar("12345678", "Juan", "Pérez", "Calle 1", "2901-111")
>>> ag.buscar("12345678")
{'nombre': 'Juan', 'apellido': 'Pérez', 'direccion': 'Calle 1', 'telefono': '2901-111'}
>>> ag.agregar("12345678", "Otro", "Nombre", "Calle 2", "2901-222")
KeyError: DNI '12345678' ya registrado
>>> ag.agregar("abc", "Juan", "Pérez", "Calle 1", "2901-111")
ValueError: DNI inválido: 'abc'
```

**Tests requeridos en `test_ej15.py`:**

```python
class AgendaTest(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()
        self.agenda.agregar("12345678", "Juan", "Pérez", "Calle 1", "2901-111")
        self.agenda.agregar("87654321", "Ana", "García", "Calle 2", "2901-222")
```

| Test | Qué verifica |
|------|-------------|
| `test_agregar_y_buscar` | Buscar `"12345678"` retorna los datos correctos |
| `test_agregar_duplicado` | Agregar con DNI existente lanza `KeyError` |
| `test_dni_no_numerico` | Agregar con DNI `"abc"` lanza `ValueError` |
| `test_dni_muy_corto` | Agregar con DNI `"123"` lanza `ValueError` |
| `test_dni_muy_largo` | Agregar con DNI `"123456789"` lanza `ValueError` |
| `test_buscar_inexistente` | Buscar DNI no registrado lanza `KeyError` |
| `test_eliminar_existente` | Eliminar `"12345678"` → `cantidad()` disminuye |
| `test_eliminar_inexistente` | Eliminar DNI no registrado lanza `KeyError` |
| `test_listar` | `listar()` retorna lista con los DNIs registrados |
| `test_cantidad` | `cantidad()` → `2` (por el `setUp`) |

---

## Bloque D — Mock, Patch y Aislamiento (Ejercicios 16–18)

---

### Ejercicio 16 — Testear función que lee archivos

**Objetivo:** Usar `unittest.mock.patch` para aislar la lectura de archivos.

**Implementar en `ej16.py`:**

```python
def contar_lineas(ruta: str) -> int:
    """Abre el archivo en ruta y retorna la cantidad de líneas."""
    with open(ruta, 'r') as f:
        return len(f.readlines())

def primera_linea(ruta: str) -> str:
    """Retorna la primera línea del archivo (sin salto de línea). Lanza FileNotFoundError si no existe."""
    with open(ruta, 'r') as f:
        linea = f.readline()
        return linea.rstrip('\n')
```

**Ejemplo:**

```python
# Suponiendo un archivo con 3 líneas: "hola\nmundo\nchau\n"
>>> contar_lineas("datos.txt")
3
>>> primera_linea("datos.txt")
'hola'
```

**Tests requeridos en `test_ej16.py`:**

```python
from unittest.mock import patch, mock_open

class ContarLineasTest(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data="hola\nmundo\nchau\n"))
    def test_contar_tres_lineas(self):
        self.assertEqual(contar_lineas("falso.txt"), 3)
```

| Test | Qué verifica |
|------|-------------|
| `test_contar_tres_lineas` | Con mock de 3 líneas → retorna `3` |
| `test_contar_archivo_vacio` | Con mock de `""` → retorna `0` o `1` según implementación |
| `test_primera_linea` | Con mock de `"hola\nmundo\n"` → retorna `"hola"` |
| `test_primera_linea_sin_salto` | Con mock de `"unica"` → retorna `"unica"` |

---

### Ejercicio 17 — Testear función con dependencia externa

**Objetivo:** Usar `MagicMock` para reemplazar un servicio externo.

**Implementar en `ej17.py`:**

```python
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
    ...
```

**Ejemplo:**

```python
# Con un mock que retorne -2:
>>> alerta_frio(mock_servicio, "Ushuaia")
'¡Alerta de frío!'
```

**Tests requeridos en `test_ej17.py`:**

```python
from unittest.mock import MagicMock

class AlertaFrioTest(unittest.TestCase):

    def setUp(self):
        self.servicio = MagicMock(spec=ServicioClima)
```

| Test | Qué verifica |
|------|-------------|
| `test_alerta_frio` | Mock retorna `-2` → `"¡Alerta de frío!"` |
| `test_temperatura_normal` | Mock retorna `20` → `"Temperatura normal"` |
| `test_alerta_calor` | Mock retorna `40` → `"¡Alerta de calor!"` |
| `test_borde_frio` | Mock retorna `5` → `"Temperatura normal"` |
| `test_borde_calor` | Mock retorna `35` → `"Temperatura normal"` |
| `test_servicio_llamado` | Verificar que `obtener_temperatura` fue llamado con la ciudad correcta |

---

### Ejercicio 18 — `Notificador` con `patch` como decorador

**Objetivo:** Usar `@patch` para interceptar un método.

**Implementar en `ej18.py`:**

```python
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
```

**Ejemplo:**

```python
# Con mock que simula envío exitoso:
>>> n = Notificador()
>>> n.notificar_bienvenida("usuario@test.com")
'enviado'
```

**Tests requeridos en `test_ej18.py`:**

| Test | Qué verifica |
|------|-------------|
| `test_bienvenida_exitosa` | `patch` hace que `enviar_email` retorne `True` → `"enviado"` |
| `test_bienvenida_fallida` | `patch` hace que `enviar_email` retorne `False` → `"error"` |
| `test_bienvenida_excepcion` | `patch` hace que `enviar_email` lance excepción → `"error"` |
| `test_email_correcto` | Verificar que `enviar_email` fue llamado con `"¡Bienvenido!"` |

---

## Bloque E — TDD Avanzado e Integración (Ejercicios 19–20)

---

### Ejercicio 19 — `Calculadora` con `subTest` 🔴🟢🔁

**Objetivo:** Usar `subTest()` para parametrizar tests y TDD completo.

**Implementar en `ej19.py`:**

```python
class CalculadoraError(Exception):
    pass

class Calculadora:
    """Calculadora con historial de operaciones."""

    def __init__(self) -> None:
        ...

    def sumar(self, a: float, b: float) -> float:
        ...

    def restar(self, a: float, b: float) -> float:
        ...

    def multiplicar(self, a: float, b: float) -> float:
        ...

    def dividir(self, a: float, b: float) -> float:
        """Lanza CalculadoraError si b == 0."""
        ...

    def historial(self) -> list[str]:
        """Retorna lista de operaciones realizadas, ej: ['2 + 3 = 5', '10 / 2 = 5.0']"""
        ...

    def limpiar_historial(self) -> None:
        ...
```

**Ejemplo:**

```python
>>> calc = Calculadora()
>>> calc.sumar(2, 3)
5
>>> calc.dividir(10, 2)
5.0
>>> calc.historial()
['2 + 3 = 5', '10 / 2 = 5.0']
```

**Tests requeridos en `test_ej19.py`:**

```python
class CalculadoraTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumas_parametrizadas(self):
        casos = [(1, 1, 2), (0, 0, 0), (-1, 1, 0), (100, 200, 300)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.sumar(a, b), esperado)
```

| Test | Qué verifica |
|------|-------------|
| `test_sumas_parametrizadas` | Múltiples sumas con `subTest` |
| `test_restas_parametrizadas` | Múltiples restas con `subTest` |
| `test_multiplicaciones_parametrizadas` | Múltiples multiplicaciones con `subTest` |
| `test_dividir_normal` | `dividir(10, 2)` → `5.0` |
| `test_dividir_por_cero` | `dividir(5, 0)` lanza `CalculadoraError` |
| `test_historial` | Después de 3 operaciones, `historial()` tiene 3 entradas |
| `test_limpiar_historial` | Después de `limpiar_historial()`, la lista está vacía |

---

### Ejercicio 20 — `GestorTareas` (integrador final) 🔴🟢🔁

**Objetivo:** Ejercicio integrador que combina TDD, fixtures, excepciones, mock y subTest.

**Implementar en `ej20.py`:**

```python
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
        ...

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Tarea) and self.titulo == other.titulo

    def __str__(self) -> str:
        estado = "✓" if self.completada else "✗"
        return f"[{estado}] {self.titulo} (vence: {self.vencimiento})"

class GestorTareas:
    """Gestor de tareas con operaciones CRUD y filtros."""

    def __init__(self) -> None:
        ...

    def agregar(self, tarea: Tarea) -> None:
        """Agrega una tarea. Lanza ValueError si ya existe una con el mismo título."""
        ...

    def completar(self, titulo: str) -> None:
        """Marca como completada. Lanza TareaNoEncontradaError si no existe."""
        ...

    def eliminar(self, titulo: str) -> None:
        """Elimina una tarea. Lanza TareaNoEncontradaError si no existe."""
        ...

    def pendientes(self) -> list[Tarea]:
        """Retorna las tareas no completadas."""
        ...

    def vencidas(self) -> list[Tarea]:
        """Retorna las tareas vencidas (no completadas y fecha pasada)."""
        ...

    def buscar(self, titulo: str) -> Tarea:
        """Busca por título. Lanza TareaNoEncontradaError si no existe."""
        ...

    def cantidad_total(self) -> int:
        ...

    def cantidad_pendientes(self) -> int:
        ...
```

**Ejemplo:**

```python
>>> from datetime import date
>>> g = GestorTareas()
>>> g.agregar(Tarea("Estudiar unittest", date(2026, 4, 20)))
>>> g.agregar(Tarea("Entregar TP", date(2026, 4, 25)))
>>> g.completar("Estudiar unittest")
>>> g.pendientes()
[Tarea("Entregar TP")]
>>> g.cantidad_total()
2
>>> g.cantidad_pendientes()
1
```

**Tests requeridos en `test_ej20.py`:**

```python
from unittest.mock import patch
from datetime import date

class GestorTareasTest(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTareas()
        self.tarea1 = Tarea("Estudiar unittest", date(2026, 4, 20))
        self.tarea2 = Tarea("Entregar TP", date(2026, 4, 25))
        self.tarea_vencida = Tarea("Leer apuntes", date(2026, 3, 1))
        self.gestor.agregar(self.tarea1)
        self.gestor.agregar(self.tarea2)
        self.gestor.agregar(self.tarea_vencida)
```

| Test | Qué verifica |
|------|-------------|
| `test_agregar_y_buscar` | Buscar `"Estudiar unittest"` retorna la tarea correcta |
| `test_agregar_duplicada` | Agregar tarea con mismo título lanza `ValueError` |
| `test_completar` | Completar y verificar que ya no está en `pendientes()` |
| `test_completar_inexistente` | Completar tarea que no existe lanza `TareaNoEncontradaError` |
| `test_eliminar` | Eliminar tarea → `cantidad_total()` disminuye |
| `test_eliminar_inexistente` | Eliminar tarea que no existe lanza `TareaNoEncontradaError` |
| `test_pendientes` | `pendientes()` retorna solo las no completadas |
| `test_vencidas` | `vencidas()` retorna tareas pasadas de fecha y no completadas (usar `@patch` sobre `date.today`) |
| `test_cantidad_total` | `cantidad_total()` → `3` |
| `test_cantidad_pendientes` | Completar 1, `cantidad_pendientes()` → `2` |
| `test_str_tarea` | Verificar formato de `__str__` con `assertIn` |

---

## Criterios de Evaluación

| Criterio | Peso |
|----------|------|
| Tests pasan (autograding) | 60% |
| Implementación correcta | 25% |
| Código limpio (nombres, type hints, docstrings) | 10% |
| Aplicación de TDD en ejercicios marcados (evidencia en commits) | 5% |

**Escala de autograding:**

| Tests que pasan | Nota |
|----------------|------|
| 20/20 ejercicios | 10 |
| 18-19 | 9 |
| 16-17 | 8 |
| 14-15 | 7 |
| 12-13 | 6 |
| 10-11 | 5 |
| 8-9 | 4 |
| < 8 | Rehacer |

---

## Recursos

- **Guía de estudio:** `guia-estudio.md` del Módulo II
- **Referencia unittest:** [docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)
- **Referencia mock:** [docs.python.org/3/library/unittest.mock.html](https://docs.python.org/3/library/unittest.mock.html)
- **Filminas del módulo:** `filminas.md`

---

*Generado por: Aux. Valeria (tp-designer) — 16/04/2026*
