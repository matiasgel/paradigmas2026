# Filminas — Módulo II: Pruebas Unitarias
## Laboratorio de Programación y Lenguajes (IF009) — UNTDF 2026
**Semanas 4–5 · 2 sesiones teóricas × 180 min**  
*Ritmo: presentación rápida — ~3–4 min por filmina · Semana 4: 31 slides · Semana 5: 27 slides*  
*Generado por: Dr. Roberto (class-writer) — 15/04/2026*

---

## SEMANA 4 — SESIÓN TEÓRICA

---

### [F-00] Portada — Semana 4

@tipo: portada
@imagen: background
@prompt-imagen: pizarrón de código Python con tests en verde y rojo sobre fondo oscuro de laboratorio universitario, estilo tiza digital
 
# Módulo II — Pruebas Unitarias

## Laboratorio de Programación y Lenguajes · UNTDF 2026

Semana 4 · Dr. Roberto / Lic. Marcos

---

### [F-01] Agenda del día

@tipo: concepto-abstracto

# ¿Qué vemos hoy?

## Bloques (180 min)

| Bloque | Duración | Tema |
|--------|----------|------|
| T0 | 30 min | Repaso POO Python |
| T1 | 40 min | Motivación — Por qué testar |
| — | 10 min | **Pausa** |
| T2 | 40 min | Framework `unittest` |
| T3 | 30 min | TDD: Red → Green → Refactor |
| T4 | 20 min | Cierre y preview práctica |

> **Al final de hoy:** van a poder escribir su primer test unitario en Python.

---

## BLOQUE T0 — REPASO POO PYTHON (30 min)

---

### [F-02] Repaso: clases e instancias

@tipo: codigo

# Python Orientado a Objetos — lo que necesitamos hoy

## Definir una clase

```python
class Agenda:
    def __init__(self, capacidad: int = 100) -> None:
        self._contactos: dict = {}
        self.capacidad = capacidad

    def __str__(self) -> str:
        return f"Agenda con {len(self._contactos)} contacto(s)"

    def __eq__(self, other: object) -> bool:
        return (isinstance(other, Agenda)
                and self._contactos == other._contactos)
```

> `__str__` → lo que vemos en `print(agenda)`  
> `__eq__` → lo que compara `assertEqual(agenda1, agenda2)`

---

### [F-03] Repaso: herencia y super()

@tipo: codigo

# Herencia en Python

## Patrón que veremos en unittest

```python
class Error(Exception):
    """Clase base para errores de la aplicación."""
    pass

class DNIInvalidoError(Error):
    """Se lanza cuando el DNI no tiene formato válido."""
    def __init__(self, dni: str) -> None:
        super().__init__(f"DNI inválido: '{dni}'. Debe tener 7 u 8 dígitos.")
        self.dni = dni
```

> **Clave:** `unittest.TestCase` también es una clase que **vamos a heredar** hoy  
> El mismo patrón — subclase, `super()`, método especializado

---

### [F-04] Repaso: excepciones propias

@tipo: concepto-abstracto

# Excepciones propias — por qué importan para tests

## El código que queremos probar lanza excepciones:

```python
class Agenda:
    def agregar(self, dni: str, nombre: str, apellido: str,
                direccion: str, telefono: str) -> None:
        if not dni.isdigit() or not (7 <= len(dni) <= 8):
            raise ValueError(f"DNI inválido: {dni!r}")
        if dni in self._contactos:
            raise KeyError(f"DNI {dni!r} ya registrado")
        self._contactos[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "direccion": direccion,
            "telefono": telefono,
        }
```

## ¿Cómo probamos que la excepción se lanza?

> → Eso lo vemos en el Bloque T2 con `assertRaises`

---

### [F-05] Métodos especiales útiles para tests

@tipo: tabla

# Métodos especiales que ayudan a testear

| Método | Cuándo lo implementar | Impacto en tests |
|--------|----------------------|-----------------|
| `__eq__` | Cuando `==` debe comparar estado interno | Permite usar `assertEqual(obj1, obj2)` |
| `__str__` | Siempre en clases de dominio | Mejora los mensajes de error de los tests |
| `__repr__` | Para debugging y logs | Aparece en las trazas de pytest y unittest |
| `__len__` | Colecciones propias | Permite `assertEqual(len(agenda), 2)` |

> **Regla práctica:** si una clase va a ser testeada, implementá `__eq__` y `__str__`.

---

## BLOQUE T1 — MOTIVACIÓN: POR QUÉ TESTAR (40 min)

---

### [F-06] Errores

@tipo: portada
@imagen: background
@prompt-imagen: sala de control de misión con alarmas, pantallas con alertas rojas y técnicos mirando con cara de preocupación, estilo fotorrealista oscuro

# Errores

---

### [F-07] Air China 140 — 1994

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: cabina de vuelo de un Airbus A300 de Air China años 90, panel de instrumentos con luz de advertencia AUTOPILOT DISCONNECT parpadeando en rojo, altímetro mostrando descenso brusco, fecha 26 de abril de 1994 visible en una pequeña pantalla, atmósfera tensa con controles en posición incorrecta, estilo infográfico minimalista dramático — sin tripulación visible

# Vuelo 140 de Air China — 26/04/1994

## ¿Qué pasó?

- Un **error de software** desactivó el piloto automático durante el descenso
- La tripulación no advirtió el cambio de modo a tiempo
- El avión impactó contra el suelo cerca de Nagoya, Japón

## Consecuencia

**264 muertos**

## Causa raíz

> El software cambió de estado de forma inesperada bajo una combinación de entrada que no fue testeada.

---

### [F-08] Therac-25 — 1985-1987

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: máquina de radioterapia Therac-25 de los años 80 — carcasa metálica gris grande con brazo articulado apuntando a una camilla vacía, pantalla terminal verde mostrando el texto "MALFUNCTION 54" y debajo "UNDERDOSE", sala de oncología hospitalaria con luz tenue, sin paciente visible, atmósfera de error técnico silencioso, estilo fotorrealista vintage dramático

# Therac-25 — Máquina de radioterapia

## ¿Qué pasó?

- Bajo **ciertas condiciones de carrera** (race condition), emitía hasta **100× más radiación** de lo normal
- El error provenía de reutilizar código de la Therac-20 sin re-testear en el nuevo contexto

## Consecuencia

**4 muertes confirmadas**, al menos 3 heridos graves

## Causa raíz

> Overflow de software. Los tests de la versión anterior no cubrían la nueva interfaz de usuario.

---

### [F-09] Ariane 5 — 1996

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: cohete Ariane 5 explotando a 3700 metros de altura sobre la Guayana Francesa, 4 de junio de 1996 — bola de fuego naranja intensa contra cielo azul, fragmentos del cohete dispersos con estelas de humo blanco, contador en pantalla superpuesta mostrando "T+37s", costo "$370M" visible como texto de subtítulo, estilo infográfico dramático con colores naranja negro y blanco

# Ariane 5 — Vuelo 501 · 04/06/1996

## ¿Qué pasó?

- Se reutilizó software de navegación del **Ariane 4** sin re-testear con los nuevos parámetros de velocidad
- El Ariane 5 es más rápido → **overflow al convertir float de 64 bits a entero de 16 bits**
- El cohete se auto-destruyó a los 37 segundos de despegue

## Consecuencia

**$370 millones de dólares** destruidos en 37 segundos

## Causa raíz

> Reutilización de código sin pruebas de regresiór en el nuevo contexto.

---

### [F-10] ¿Qué tienen en común?

@tipo: socratica

# ¿Qué tienen en común Air China, Therac-25 y Ariane 5?

## Pensemos...

- ¿Todos tenían código funcionando?  **Sí**
- ¿Todos pasaban por ingenieros profesionales?  **Sí**
- ¿Todos fallaron en producción?  **Sí**

## La respuesta

> **No se testearon los casos de borde ni el comportamiento bajo nuevas condiciones.**

## Definición de testing (IEEE):

> *"Proceso que busca verificar la exactitud, integridad y calidad de un software. Incluye actividades que buscan encontrar errores antes de que lleguen al usuario."*

---

### [F-11] Caja Negra vs Caja Blanca

@tipo: tabla-comparativa

# Tipos de tests — por conocimiento del sistema

## Caja Negra

- Se prueban **entradas y salidas** contra la especificación
- **Sin conocer** la implementación interna
- Ejemplo: dar DNI `"abc"` → esperar `ValueError`

## Caja Blanca

- Se prueban **ramas, condiciones y caminos** internos del código
- **Conociendo** la estructura interna
- Ejemplo: dar DNI de exactamente 6 dígitos para cubrir el `if len(dni) < 7`

> **Práctica:** los tests que van a escribir en la clase Agenda van a ser una mezcla de ambos.

---

### [F-12] Pirámide de niveles de testing

@tipo: diagrama
@imagen: content
@prompt-imagen: pirámide de capas con cuatro niveles de testing — base ancha Unit Test verde, Integration Test amarilla, System Test naranja, Acceptance Test roja en la cima — estilo infográfico educativo limpio con flechas de velocidad y costo

# Los 4 niveles de testing

| Nivel | Nombre | Qué prueba | Velocidad |
|-------|--------|------------|-----------|
| 1 — base | **Prueba de Unidad** | Una clase o función aislada | Milisegundos |
| 2 | **Prueba de Integración** | Interacción entre módulos | Segundos |
| 3 | **Prueba de Sistema** | El sistema completo | Minutos |
| 4 — cima | **Prueba de Aceptación** | Requisitos del usuario | Horas |

> **Este módulo:** Nivel 1 — Unit Test con `unittest`  
> *"Son pruebas de bajo nivel que se focalizan en una pequeña parte del software.  
> En POO, esas unidades suelen ser las clases."*

---

### [F-13] Pruebas de regresión

@tipo: concepto-abstracto

# Prueba de regresión — la red de seguridad

## ¿Qué es?

> Re-ejecutar todos los tests existentes **después de cada cambio** para verificar que nada se rompió.

## ¿Por qué importa?

- Ariane 5 falló por falta de pruebas de regresión al reutilizar código
- Therac-25 falló por falta de pruebas de regresión al cambiar la interfaz

## En TDD esto es automático

```bash
# Cada vez que modificás código, ejecutás:
python -m unittest discover
# Si todos los tests pasan → el cambio no rompió nada ✅
```

> **Mensaje clave:** el suite de tests es tu red de seguridad para refactorizar con confianza.

---

## BLOQUE T2 — FRAMEWORK UNITTEST (40 min)

---

### [F-14] La familia xUnit

@tipo: timeline
@imagen: content
@prompt-imagen: línea de tiempo horizontal desde 1989 hasta 2024 mostrando SUnit Smalltalk 1989, JUnit Java 1997, NUnit .NET 2002, unittest Python 2001, con iconos de los lenguajes en estilo minimalista plano

# La familia xUnit

## Historia

| Año | Framework | Lenguaje | Creador |
|-----|-----------|----------|---------|
| 1989 | **SUnit** | Smalltalk | Kent Beck |
| 1997 | **JUnit** | Java | Kent Beck + Erich Gamma |
| 2001 | **unittest** | Python | Steve Purcell (port de JUnit) |
| 2002 | **NUnit** | .NET | Charlie Poole |

> `unittest` es parte de la **stdlib de Python** — no necesitás instalar nada.

---

### [F-15] TestCase · TestSuite · TestRunner

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama con tres cajas conectadas por flechas — TestCase a la izquierda con métodos test_, TestSuite en el centro agrupando múltiples TestCases, TestRunner a la derecha ejecutando y mostrando resultados — estilo de arquitectura de software minimalista

# Los tres conceptos del framework

## TestCase

> Un **caso de prueba** individual. Se crea heredando de `unittest.TestCase`.  
> Cada método que empieza con `test_` es un test independiente.

## TestSuite

> Una **colección** de casos de prueba. Se usa para ejecutar varios TestCase juntos.  
> El runner lo construye automáticamente por discovery.

## TestRunner

> El componente que **orquesta la ejecución** y muestra los resultados.  
> `python -m unittest` es el runner por defecto — salida de texto en la terminal.

---

### [F-16] Mi primer test

@tipo: codigo

# Estructura mínima de un test

```python
import unittest

class PrimeraVez(unittest.TestCase):

    def test_suma(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 4)

    def test_tipo(self):
        self.assertIsInstance("hola", str)

if __name__ == "__main__":
    unittest.main()
```

## Reglas del runner

- Métodos con nombre `test_*` → se ejecutan automáticamente
- Un método = un test = un resultado (✅ ok / ❌ FAIL / 💥 ERROR)
- El orden de ejecución **no está garantizado** → cada test debe ser independiente

---

### [F-16b] Leer el output de un test fallido

@tipo: codigo

# Cuando el test falla — qué leer primero

## FAIL — aserción que no se cumplió

```
FAIL: test_nombre_correcto (test_agenda.AgendaTest)
AssertionError: 'Juana' != 'Juan'
```

## ERROR — excepción inesperada (bug en el código, no en el test)

```
ERROR: test_buscar_existente (test_agenda.AgendaTest)
KeyError: '12345678'
```

## Con -v (verbose)

```
test_agregar_nuevo ... ok
test_buscar_existente ... FAIL
test_dni_invalido ... ok

Ran 3 tests in 0.002s  FAILED (failures=1)
```

> **Regla:** empezá a leer desde la línea del `AssertionError` — ahí está el problema.

---

### [F-17] Aserciones esenciales

@tipo: tabla

# Las aserciones más usadas

| Método | Verifica |
|--------|----------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIsNone(x)` | `x is None` |
| `assertIsNotNone(x)` | `x is not None` |
| `assertIn(a, b)` | `a in b` |
| `assertIsInstance(a, T)` | `isinstance(a, T)` |
| `assertRaises(Exc)` | se lanza la excepción `Exc` |

> **Tip:** preferí `assertEqual` sobre `assertTrue(a == b)` — los mensajes de error son mucho más claros.

---

### [F-17b] Aserciones para colecciones

@tipo: tabla

# Cuando verificás listas, dicts y strings

| Método | Verifica |
|--------|----------|
| `assertIn(a, b)` | `a in b` (lista, dict, string) |
| `assertNotIn(a, b)` | `a not in b` |
| `assertCountEqual(a, b)` | mismos elementos, **cualquier orden** |
| `assertListEqual(a, b)` | listas iguales — diff detallado |
| `assertDictEqual(a, b)` | dicts iguales — diff detallado |
| `assertRegex(s, r)` | string `s` matchea regex `r` |

> `assertCountEqual([1,2,3], [3,1,2])` pasa. `assertEqual` fallaría porque el orden importa.

---

### [F-18] assertRaises — probar excepciones

@tipo: codigo

# ¿Cómo probamos que una excepción se lanza?

## Con context manager (recomendado)

```python
def test_dni_invalido_lanza_error(self):
    with self.assertRaises(ValueError):
        Agenda().agregar("abc", "Juan", "Pérez", "Calle 1", "111")
```

## También podemos verificar el mensaje

```python
def test_mensaje_de_error_correcto(self):
    with self.assertRaises(ValueError) as ctx:
        Agenda().agregar("abc", "Juan", "Pérez", "Calle 1", "111")
    self.assertIn("abc", str(ctx.exception))
```

## ¿Qué pasa si la excepción NO se lanza?

> El test **falla** — el framework reporta `AssertionError: ValueError not raised`.

---

### [F-19] Fixtures: setUp y tearDown

@tipo: codigo

# Fixtures — preparar y limpiar el entorno

## ¿Por qué fixtures?

> Sin fixtures → repetir código de inicialización en cada test → violación de DRY.

```python
class AgendaTest(unittest.TestCase):

    def setUp(self):
        """Se ejecuta ANTES de cada test."""
        self.agenda = Agenda()
        self.agenda.agregar("12345678", "Juan", "Pérez", "Calle 1", "2901-111")

    def tearDown(self):
        """Se ejecuta DESPUÉS de cada test (incluso si falla)."""
        del self.agenda

    def test_buscar_existente(self):
        resultado = self.agenda.buscar("12345678")
        self.assertEqual(resultado["nombre"], "Juan")

    def test_buscar_inexistente(self):
        with self.assertRaises(KeyError):
            self.agenda.buscar("00000000")
```

> **setUp** corre antes de **cada** test — cada test empieza con un estado limpio.

---

### [F-19b] Orden de ejecución garantizado

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama de flujo vertical con cajas — setUpClass arriba en azul, luego setUp verde → test_A gris → tearDown verde, luego setUp verde → test_B gris → tearDown verde, luego tearDownClass azul abajo — flechas hacia abajo, estilo minimalista educativo

# El ciclo completo de una clase de tests

```
setUpClass()       ← 1 vez por clase
  setUp()          ← antes de test_A
    test_A()
  tearDown()       ← después de test_A (aunque falle)
  setUp()          ← antes de test_B
    test_B()
  tearDown()
tearDownClass()    ← 1 vez al final
```

> El **orden entre tests** no está garantizado — diseñalos independientes.

---

### [F-20] Ejecución CLI

@tipo: codigo

# Ejecutar tests desde la terminal

## Comandos básicos

```bash
# Ejecutar un archivo
python -m unittest test_agenda.py

# Con detalle (verbose) — muestra el nombre de cada test
python -m unittest -v test_agenda.py

# Descubrimiento automático — busca test*.py en todo el proyecto
python -m unittest discover

# Descubrimiento en una carpeta específica
python -m unittest discover -s tests/ -p "test_*.py"
```

## Salida esperada

```
test_agregar_nuevo (test_agenda.AgendaTest) ... ok
test_agregar_duplicado (test_agenda.AgendaTest) ... ok
test_buscar_existente (test_agenda.AgendaTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

## BLOQUE T3 — TDD: RED → GREEN → REFACTOR (30 min)

---

### [F-21] ¿Qué es TDD?

@tipo: concepto-abstracto

# Test-Driven Development

## Definición

> **TDD** es una metodología de diseño en la que **el test se escribe antes que el código de producción**.

## Origen

- Formalizado por **Kent Beck** (el mismo de SUnit/JUnit) en el libro *Test-Driven Development by Example* (2002)
- Parte de la metodología **Extreme Programming (XP)**

## El mantra

> *"Never write a single line of production code unless you have a failing test."*  
> — Kent Beck

## ¿Por qué importa?

- Los tests son la **especificación ejecutable** del comportamiento
- Diseño emergente — el código evoluciona guiado por los tests
- Red de seguridad automática para refactorizar

---

### [F-22] El ciclo Red → Green → Refactor

@tipo: diagrama
@imagen: content
@prompt-imagen: ciclo circular de tres pasos — círculo rojo con texto RED escribir test, círculo verde con texto GREEN pasar test, círculo azul con texto REFACTOR limpiar código — flechas conectando los tres en sentido horario, estilo infográfico moderno

# El ciclo TDD

## 🔴 RED — Escribir un test que falla

- Escribís el test **antes** de tener el código
- El test **debe fallar** (si pasa, hay un problema)
- El fallo confirma que el test está testeando algo real

## 🟢 GREEN — Hacer pasar el test

- Escribís el **mínimo código posible** para que el test pase
- No optimizés aún — solo hacé pasar el test
- "Fake it till you make it"

## 🔵 REFACTOR — Limpiar el código

- Mejorar la implementación **sin cambiar el comportamiento**
- Los tests siguen en verde después del refactor
- Aplicar DRY, type hints, nombres claros

---

### [F-23] Demo FizzBuzz — 🔴 RED

@tipo: codigo

# Demo en vivo — FizzBuzz TDD · Paso 1: RED

## Especificación

- Si `n` es divisible por 3 → `"Fizz"`
- Si `n` es divisible por 5 → `"Buzz"`
- Si es divisible por ambos → `"FizzBuzz"`
- Si no → el número como string

## Primer test (escribimos ANTES del código)

```python
import unittest

class FizzBuzzTest(unittest.TestCase):

    def test_tres_retorna_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
```

## ¿Qué pasa al ejecutar?

```
ERROR: test_tres_retorna_fizz
NameError: name 'fizzbuzz' is not defined
```

> **¡Perfecto! El test falla — el RED está confirmado.**

---

### [F-24] Demo FizzBuzz — 🟢 GREEN

@tipo: codigo

# Demo en vivo — FizzBuzz TDD · Paso 2: GREEN

## Mínimo código para pasar el test

```python
def fizzbuzz(n: int) -> str:
    return "Fizz"
```

## Resultado

```
test_tres_retorna_fizz ... ok
Ran 1 test in 0.000s OK
```

## Agregar más tests (el ciclo se repite)

```python
def test_cinco_retorna_buzz(self):
    self.assertEqual(fizzbuzz(5), "Buzz")

def test_quince_retorna_fizzbuzz(self):
    self.assertEqual(fizzbuzz(15), "FizzBuzz")

def test_uno_retorna_uno(self):
    self.assertEqual(fizzbuzz(1), "1")
```

> Ahora implementamos la función completa para pasar todos los tests.

---

### [F-25] Demo FizzBuzz — 🔵 REFACTOR

@tipo: codigo

# Demo en vivo — FizzBuzz TDD · Paso 3: REFACTOR

## Implementación completa (ya con todos los tests en verde)

```python
def fizzbuzz(n: int) -> str:
    """Retorna Fizz, Buzz, FizzBuzz o el número como string."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
```

## Verificación final

```
test_cinco_retorna_buzz ... ok
test_quince_retorna_fizzbuzz ... ok
test_tres_retorna_fizz ... ok
test_uno_retorna_uno ... ok

Ran 4 tests in 0.000s  OK
```

> **Los tests documentan la especificación. El código la implementa.**

---

## BLOQUE T4 — CIERRE SEMANA 4 (20 min)

---

### [F-26] Ejercicio integrador — Clase Agenda

@tipo: concepto-abstracto

# Para la práctica de hoy: Clase Agenda

## Origen — filminas 2025

> *"Realizar la clase Agenda que guarde nombre, apellido, dirección y teléfono de una persona utilizando su DNI como referencia. Desarrollar los métodos necesarios para gestionar los datos incluyendo excepciones por datos inválidos."*

## Consigna 2026 (con TDD)

1. **Primero** escribís los tests de `__init__`, `agregar` y `buscar`
2. **Luego** implementás la clase `Agenda` hasta que todos los tests pasen
3. **Después** agregás `eliminar` y `listar` con sus tests

## Métodos a implementar

| Método | Qué hace |
|--------|----------|
| `agregar(dni, nombre, apellido, dir, tel)` | Registra — lanza `KeyError` si DNI ya existe |
| `buscar(dni)` | Retorna dict — lanza `KeyError` si no existe |
| `eliminar(dni)` | Elimina — lanza `KeyError` si no existe |
| `listar()` | Retorna lista de DNIs |

---

### [F-27] Cierre Semana 4

@tipo: cierre

# Resumen de hoy

## Lo que vimos

- ✅ Repaso POO: `__eq__`, `__str__`, excepciones propias
- ✅ Por qué testar: Air China, Therac-25, Ariane 5
- ✅ Tipos de tests: caja negra / blanca, pirámide de niveles
- ✅ `unittest`: TestCase, aserciones, fixtures, CLI
- ✅ TDD: ciclo Red → Green → Refactor (demo FizzBuzz)

## Para la práctica (hoy)

- Kata FizzBuzz TDD con pair programming
- Ejercicio Agenda fase 1: tests primero
- Ejercicio Agenda fase 2: implementación

## Para la próxima clase (Semana 5)

- `unittest.mock` — aislar dependencias
- Subtests y skipping
- Anticipo `django.test.TestCase`

---

## SEMANA 5 — SESIÓN TEÓRICA

---

### [F-28] Portada — Semana 5

@tipo: portada
@imagen: background
@prompt-imagen: diagrama de dependencias de software con flechas entre módulos, algunas flechas cortadas con tijeras digitales representando el aislamiento de tests, estilo oscuro con acentos azul eléctrico

# Módulo II — Pruebas Unitarias

## Semana 5: Mocking y cierre del módulo

Semana 5 · Dr. Roberto / Lic. Marcos

---

### [F-29] Agenda — Semana 5

@tipo: concepto-abstracto

# ¿Qué vemos hoy?

| Bloque | Duración | Tema |
|--------|----------|------|
| T1 | 40 min | `unittest.mock` — MagicMock, patch, return_value, side_effect |
| T2 | 30 min | subTest, skip, addCleanup |
| — | 10 min | **Pausa** |
| T3 | 30 min | TDD en BlogApp — `django.test.TestCase` |
| T4 | 30 min | Cierre Módulo II + test smells |
| T5 | 25 min | Revisión TP 2 |

> *~27 filminas — ritmo rápido ~4 min/filmina*

---

### [F-29b] Repaso — semana anterior

@tipo: socratica

# Preguntas rápidas — 2 min

- ¿Diferencia entre `FAIL` y `ERROR` en el output?
- ¿Qué hace `setUp`? ¿Cuántas veces corre?
- ¿Cuándo `assertRaises` pasa vs falla?
- Tres pasos del TDD — decílos en orden

> [Respuestas del grupo]

## Estado del ejercicio Agenda

- ✅ `agregar` + tests (semana 4)
- ✅ `buscar` + tests (semana 4)
- ⏳ `eliminar` y `listar` — práctica de hoy

---

## BLOQUE T1 — UNITTEST.MOCK (40 min)

---

### [F-30] ¿Por qué aislar dependencias?

@tipo: concepto-abstracto

# El problema de las dependencias externas

## Este test tiene un problema

```python
def test_guardar_contacto(self):
    agenda = Agenda()
    agenda.agregar("12345678", "Juan", "Pérez", "Calle 1", "111")
    agenda.guardar_en_db()   # ← llama a una base de datos real
    self.assertEqual(agenda.total(), 1)
```

## ¿Qué puede salir mal?

- La base de datos no está disponible en CI
- El test deja datos sucios para el siguiente test
- Es lento (red, disco)
- El fallo de la BD oculta el error real del código

## La solución: un doble (mock)

> Reemplazar la dependencia real con un **objeto falso** que simula su comportamiento.

---

### [F-30b] Test doubles — tipos

@tipo: tabla

# No todos los "mocks" son iguales

| Tipo | Qué hace | Cuándo usarlo |
|------|----------|---------------|
| **Stub** | Retorna valores fijos | Aislar una fuente de datos |
| **Mock** | Registra llamadas + verificación | Verificar que un método fue llamado |
| **Spy** | Como mock pero usa implementación real | Verificar interacciones sin reemplazar lógica |
| **Fake** | Implementación simplificada que funciona | BD en memoria |

> `MagicMock` puede actuar como Stub, Mock o Spy según cómo lo configures.

---

### [F-31] MagicMock — crear un doble

@tipo: codigo

# `unittest.mock.MagicMock`

## ¿Qué es?

> Un objeto que **acepta cualquier método o atributo** y registra todas las llamadas recibidas.

```python
from unittest.mock import MagicMock

# Crear el doble
db_falsa = MagicMock()

# Llamar cualquier método — no lanza error
db_falsa.guardar({"dni": "12345678", "nombre": "Juan"})

# Verificar que fue llamado
db_falsa.guardar.assert_called_once()

# Verificar el argumento exacto
db_falsa.guardar.assert_called_with({"dni": "12345678", "nombre": "Juan"})

# Configurar valor de retorno
db_falsa.buscar.return_value = {"nombre": "Juan"}
resultado = db_falsa.buscar("12345678")  # → {"nombre": "Juan"}
```

---

### [F-31b] MagicMock — verificar llamadas

@tipo: codigo

# Los métodos de verificación más usados

```python
m = MagicMock()
m.guardar("a.json")
m.guardar("b.json")

m.guardar.assert_called()                        # ¿fue llamado alguna vez?
m.guardar.assert_called_with("b.json")          # ¿última llamada con este arg?
m.guardar.assert_called_once_with("a.json")     # ❌ falla — fue llamado 2 veces
m.guardar.assert_any_call("a.json")             # ¿en alguna llamada usó este arg?

print(m.guardar.call_count)        # → 2
print(m.guardar.call_args_list)
# → [call('a.json'), call('b.json')]
```

---

### [F-31c] return_value y side_effect

@tipo: codigo

# Controlar qué devuelve el mock

## return_value — siempre lo mismo

```python
db = MagicMock()
db.buscar.return_value = {"nombre": "Juan"}
db.buscar("cualquier-dni")  # → siempre {"nombre": "Juan"}
```

## side_effect — comportamiento dinámico

```python
# Lanzar excepción
db.buscar.side_effect = KeyError("no encontrado")

# Distintos valores por llamada
db.buscar.side_effect = [{"nombre": "Juan"}, {"nombre": "Ana"}, KeyError("fin")]
db.buscar("1")  # → {"nombre": "Juan"}
db.buscar("2")  # → {"nombre": "Ana"}
db.buscar("3")  # → KeyError!
```

> `side_effect` tiene prioridad sobre `return_value`.

---

### [F-32] patch — reemplazar en contexto

@tipo: codigo

# `unittest.mock.patch` — como context manager

## El escenario

```python
# agenda.py
import json

class Agenda:
    def guardar(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump(self._contactos, f)
```

## El test con patch

```python
from unittest.mock import patch, mock_open

class AgendaTest(unittest.TestCase):

    def test_guardar_llama_open(self):
        agenda = Agenda()
        agenda.agregar("12345678", "Juan", "Pérez", "Calle 1", "111")

        with patch("builtins.open", mock_open()) as m:
            agenda.guardar("agenda.json")

        m.assert_called_once_with("agenda.json", "w")
```

> `patch` reemplaza `open` **solo dentro del bloque `with`** — luego lo restaura automáticamente.

---

### [F-32b] ¿Qué path pongo en patch?

@tipo: concepto-abstracto

# La regla: patchear donde se USA, no donde se DEFINE

## Ejemplo — `agenda.py` usa `json.dump`

```python
# agenda.py
import json
class Agenda:
    def guardar(self, path):
        json.dump(self._contactos, open(path, "w"))  # usa json acá
```

## ¿Qué path va en patch?

```python
# ❌ INCORRECTO — parchea la definición
with patch("json.dump") as m: ...

# ✅ CORRECTO — parchea donde agenda.py lo usa
with patch("agenda.json.dump") as m: ...
```

> **Regla mnemónica:** el path empieza por el módulo que importa el símbolo, no por donde está definido.

---

### [F-33] patch como decorador

@tipo: codigo

# `patch` como decorador

## El mismo test, otra sintaxis

```python
from unittest.mock import patch, mock_open

class AgendaTest(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_guardar_llama_open(self, mock_open_obj):
        agenda = Agenda()
        agenda.agregar("12345678", "Juan", "Pérez", "Calle 1", "111")
        agenda.guardar("agenda.json")

        mock_open_obj.assert_called_once_with("agenda.json", "w")
```

## Context manager vs decorador

| Forma | Cuándo usarla |
|-------|--------------|
| Context manager (`with patch(...)`) | Cuando el patch se activa en medio del test |
| Decorador (`@patch(...)`) | Cuando el patch cubre todo el test (más común) |

> **Regla:** usá la que haga el test más legible. No hay respuesta correcta única.

---

### [F-33b] patch.object y múltiples patches

@tipo: codigo

# patch.object — patchear un método de una clase conocida

```python
from unittest.mock import patch

# En vez de: patch("agenda.AgendaService.validar_dni")
with patch.object(AgendaService, "validar_dni", return_value=True):
    agenda = Agenda()
    agenda.agregar("12345678", "Juan", "Pérez", "Calle 1", "111")
```

## Múltiples @patch — los mocks llegan en orden INVERSO

```python
@patch("agenda.json.dump")       # llega como: mock_dump (último decorador = primer arg)
@patch("builtins.open")          # llega como: mock_open (primer decorador = último arg)
def test_guardar(self, mock_open, mock_dump):
    ...
```

> Con múltiples decoradores: el más cercano al método llega como primer argumento.

---

## BLOQUE T2 — SUBTESTS Y SKIPPING (30 min)

---

### [F-34] subTest — parametrizar sin duplicar

@tipo: codigo

# `subTest()` — probar múltiples casos en un test

## El problema sin subTest

```python
# ❌ Código duplicado — si falla uno, los demás no se ejecutan
def test_fizzbuzz_3(self): self.assertEqual(fizzbuzz(3), "Fizz")
def test_fizzbuzz_5(self): self.assertEqual(fizzbuzz(5), "Buzz")
def test_fizzbuzz_15(self): self.assertEqual(fizzbuzz(15), "FizzBuzz")
```

## Con subTest

```python
def test_fizzbuzz_casos(self):
    casos = [
        (3,  "Fizz"),
        (5,  "Buzz"),
        (15, "FizzBuzz"),
        (1,  "1"),
        (30, "FizzBuzz"),
    ]
    for entrada, esperado in casos:
        with self.subTest(n=entrada):
            self.assertEqual(fizzbuzz(entrada), esperado)
```

> Si falla un caso, los demás **continúan ejecutándose** — el reporte muestra cuáles fallaron.

---

### [F-34b] subTest — leer el reporte de fallo

@tipo: codigo

# El reporte muestra exactamente qué caso falló

```python
def test_fizzbuzz_casos(self):
    casos = [(3, "Fizz"), (5, "WRONG"), (15, "FizzBuzz"), (7, "WRONG")]
    for n, esperado in casos:
        with self.subTest(n=n):
            self.assertEqual(fizzbuzz(n), esperado)
```

## Reporte

```
FAIL: test_fizzbuzz_casos (n=5)
AssertionError: 'Buzz' != 'WRONG'

FAIL: test_fizzbuzz_casos (n=7)
AssertionError: '7' != 'WRONG'

Ran 1 test in 0.001s  FAILED (failures=2)
```

> El valor `n=5` aparece en el nombre → sabés exactamente qué entrada falló.

---

### [F-35] Skipping — saltear tests

@tipo: codigo

# Decoradores de skip

```python
import sys
import unittest

class EjemploSkip(unittest.TestCase):

    @unittest.skip("Función aún no implementada")
    def test_en_construccion(self):
        self.assertTrue(funcion_pendiente())

    @unittest.skipIf(sys.version_info < (3, 11),
                     "Requiere Python 3.11+")
    def test_solo_en_python_nuevo(self):
        ...

    @unittest.skipUnless(sys.platform == "linux",
                         "Solo en Linux")
    def test_solo_linux(self):
        ...

    @unittest.expectedFailure
    def test_bug_conocido(self):
        # Este test DEBE fallar — si pasa, es un error
        self.assertEqual(1, 2)
```

> `@skip` y `@skipIf` son útiles durante desarrollo.  
> `@expectedFailure` documenta bugs conocidos formalmente.

---

### [F-35b] @expectedFailure — workflow TDD con métodos pendientes

@tipo: codigo

# Usar @expectedFailure para marcar trabajo pendiente

```python
class AgendaTest(unittest.TestCase):

    def test_agregar(self):              # ✅ implementado — pasa
        ...

    @unittest.expectedFailure
    def test_eliminar(self):             # ⏳ por implementar
        self.agenda.eliminar("12345678")
        self.assertNotIn("12345678", self.agenda.listar())

    @unittest.expectedFailure
    def test_listar_ordenado(self):      # ⏳ por implementar
        ...
```

## Output

```
test_agregar ... ok
test_eliminar ... expected failure    (x)
test_listar_ordenado ... expected failure    (x)
```

> Si accidentalmente `test_eliminar` pasa, el runner reporta **unexpected success** — te avisa.

---

### [F-36] setUpClass y tearDownClass

@tipo: codigo

# Fixtures de clase — para recursos costosos

```python
class AgendaIntegrationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta UNA VEZ antes de todos los tests de la clase."""
        cls.conexion = inicializar_conexion_bd()

    @classmethod
    def tearDownClass(cls):
        """Se ejecuta UNA VEZ después de todos los tests de la clase."""
        cls.conexion.cerrar()

    def test_persistir_contacto(self):
        # usa self.conexion — ya inicializada
        ...
```

## Diferencia con setUp

| Fixture | Frecuencia | Uso típico |
|---------|-----------|-----------|
| `setUp` | Antes de **cada** test | Objetos simples, dicts, listas |
| `setUpClass` | Una vez por clase | BD, conexiones, recursos costosos |

---

### [F-36b] addCleanup — limpieza sin tearDown

@tipo: codigo

# Registrar limpieza desde setUp

```python
class AgendaTest(unittest.TestCase):

    def setUp(self):
        self.archivo_temp = crear_archivo_temporal()
        # Registra la limpieza aquí — no hay tearDown separado
        self.addCleanup(os.remove, self.archivo_temp)

    def test_guardar_carga(self):
        ...  # si este test falla, addCleanup igual se ejecuta
```

## addCleanup vs tearDown

| | `tearDown` | `addCleanup` |
|--|---|---|
| Múltiples limpiezas | Un solo método | Ilimitadas, en orden LIFO |
| Si setUp falla a la mitad | No se ejecuta | Se ejecutan las ya registradas |

---

## BLOQUE T3 — TDD EN BLOGAPP (30 min)

---

### [F-37] django.test.TestCase — continuidad directa

@tipo: concepto-abstracto

# Todo lo que aprendieron se transfiere directamente

## `django.test.TestCase` hereda de `unittest.TestCase`

```python
# unittest — lo que aprendieron hoy
class AgendaTest(unittest.TestCase):
    def setUp(self): ...
    def test_algo(self): self.assertEqual(...)

# Django — lo que verán en Módulo III
from django.test import TestCase

class PostTest(TestCase):    # ← es un unittest.TestCase
    def setUp(self): ...
    def test_algo(self): self.assertEqual(...)
```

> **Mismos métodos, mismas aserciones, mismos fixtures.**  
> Django agrega funcionalidades extras (cliente de pruebas, BD de test, rollback automático).

---

### [F-37b] django.test.Client — requests de prueba

@tipo: codigo

# El cliente HTTP de Django — sin tocar la red

```python
from django.test import TestCase, Client

class PostViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_lista_posts_devuelve_200(self):
        response = self.client.get("/blog/posts/")
        self.assertEqual(response.status_code, 200)

    def test_crear_requiere_login(self):
        response = self.client.post("/blog/posts/crear/", {"titulo": "Hola"})
        self.assertEqual(response.status_code, 302)   # redirect a login

    def test_contenido_en_respuesta(self):
        response = self.client.get("/blog/posts/")
        self.assertContains(response, "Últimas entradas")
```

> Esto es **Nivel 2 (Integración)** — vista + URL + template. Se profundiza en Módulo III.

---

### [F-38] Estructura de tests en Django

@tipo: codigo

# Dónde van los tests en un proyecto Django

```
blogapp/
├── manage.py
├── blog/
│   ├── models.py
│   ├── views.py
│   └── tests/              ← carpeta de tests
│       ├── __init__.py
│       ├── test_models.py  ← tests de modelos (Nivel 1 — Unit)
│       ├── test_views.py   ← tests de vistas (Nivel 2 — Integration)
│       └── test_forms.py
```

## Ejecutar con Django

```bash
python manage.py test blog
```

> **La lógica es idéntica** — el comando llama al runner de `unittest` por debajo.

---

### [F-38b] manage.py test — opciones útiles

@tipo: codigo

# Los flags que van a usar en el TP 3

```bash
# Correr toda la app
python manage.py test blog

# Solo un TestCase
python manage.py test blog.tests.test_models.PostTest

# Solo un método
python manage.py test blog.tests.test_models.PostTest.test_titulo_requerido

# Verbose — muestra el nombre de cada test
python manage.py test blog --verbosity=2

# Detener en el primer fallo (útil al desarrollar)
python manage.py test blog --failfast

# Mantener la BD entre corridas (más rápido)
python manage.py test blog --keepdb
```

---

### [F-39] Preview TP 3

@tipo: concepto-abstracto

# TP 3 — Blog App con tests desde el inicio

## La diferencia con TP 2

| TP 2 | TP 3 |
|------|------|
| Tests escritos por nosotros (autograding) | **Ustedes escriben los tests** |
| TDD opcional | **TDD obligatorio** |
| Foco en funciones | Foco en modelos y vistas Django |

## Estructura del repo (GitHub Classroom)

```
tp03-blog-app/
├── blog/
│   ├── models.py      ← implementar aquí
│   └── tests/
│       ├── test_models.py  ← escribir tests aquí PRIMERO
│       └── test_views.py
└── README.md          ← consigna y criterios de evaluación
```

> **Más detalles en la sesión práctica de hoy.**

---

## BLOQUE T4 — CIERRE MÓDULO II (30 min)

---

### [F-40] Repaso Módulo II completo

@tipo: tabla

# ¿Qué aprendimos en el Módulo II?

| Concepto | Estado |
|----------|--------|
| Caja negra / caja blanca | ✅ |
| Pirámide de niveles de testing | ✅ |
| `unittest.TestCase` — estructura | ✅ |
| Aserciones: `assertEqual`, `assertRaises`, etc. | ✅ |
| Fixtures: `setUp`, `tearDown`, `setUpClass` | ✅ |
| TDD: ciclo Red → Green → Refactor | ✅ |
| `unittest.mock`: `MagicMock`, `patch` | ✅ |
| `subTest()` y decoradores de skip | ✅ |
| `python -m unittest discover` | ✅ |
| `django.test.TestCase` (anticipo) | ✅ (preview) |

---

### [F-40b] Test smells — qué evitar

@tipo: tabla

# Los errores más comunes al escribir tests

| Smell | Síntoma | Solución |
|-------|---------|----------|
| **Test que nunca falla** | Siempre ok aunque rompas el código | Verificar que el test mida algo real |
| **Test del mock** | `assertEqual(mock.val, mock.val)` | Verificar comportamiento del código real |
| **setUp gigante** | setUp de 30+ líneas | Separar en múltiples TestCase |
| **Test sin assert** | Corre pero no verifica nada | Agregar al menos un assert |
| **Tests interdependientes** | El orden importa | Cada test debe ser autocontenido |
| **Nombre genérico** | `test_1`, `test_a` | `test_agregar_dni_invalido_lanza_ValueError` |

> Un test que falla por razones no relacionadas con el código bajo prueba es ruido, no señal.

---

### [F-41] Cierre — Módulo II

@tipo: cierre
@imagen: background
@prompt-imagen: pantalla de terminal mostrando "Ran 12 tests in 0.003s — OK" con todos los tests en verde, fondo oscuro de IDE, sensación de satisfacción y logro

# Módulo II — Completado

## El mensaje final

> *"Un test que pasa no prueba que tu código es correcto.  
> Prueba que tu código hace lo que vos especificaste.  
> Escribí mejores especificaciones."*

## Lo que llevan al Módulo III

- `django.test.TestCase` es `unittest.TestCase` con superpoderes
- TDD es la metodología — se aplica igual en Django
- Los tests del TP 3 son **suyos** — diseñenlos bien

## Próximas clases

- Módulo III — Django MVC: modelos, vistas, URLs, templates
- TP 3 — BlogApp con TDD desde la primera línea

---

*Filminas generadas por: Dr. Roberto (class-writer) — 15/04/2026*  
*Fuentes: `python-testing.pdf` (filminas 2025, ChromaDB), `python-unittest-reference.md` (Python 3.14, ChromaDB), `diseno.md` aprobado*
