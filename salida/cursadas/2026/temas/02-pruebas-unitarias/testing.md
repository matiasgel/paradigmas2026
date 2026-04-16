# Referencia: `unittest` — Framework de Pruebas Unitarias en Python

**Fuente:** [docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)  
**Versión:** Python 3.14 (última estable al 15/04/2026)  
**Módulo:** II — Pruebas Unitarias (semanas 3–4)  
**Materia:** Laboratorio de Programación y Lenguajes (IF009) — UNTDF 2026

---

## 1. Conceptos Fundamentales

`unittest` es el framework estándar de Python para pruebas unitarias, inspirado en JUnit. Soporta:

- Automatización de pruebas
- Código de setup/teardown compartido
- Agrupación de tests en colecciones
- Independencia de los tests respecto al framework de reporte

### Conceptos clave

| Concepto | Descripción |
|----------|-------------|
| **test fixture** | Preparación necesaria para ejecutar uno o más tests (crear DBs, directorios, servidores, etc.) |
| **test case** | Unidad individual de testing: verifica una respuesta específica a un conjunto de entradas |
| **test suite** | Colección de test cases y/o test suites que se ejecutan juntos |
| **test runner** | Componente que orquesta la ejecución y reporta los resultados |

---

## 2. Ejemplo mínimo

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

> **Regla:** Los métodos de test deben comenzar con `test`. El runner los detecta automáticamente.

---

## 3. Organización del código de tests

### setUp y tearDown (por método)

```python
class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')   # se ejecuta ANTES de cada test

    def tearDown(self):
        self.widget.dispose()                # se ejecuta DESPUÉS de cada test (siempre)
```

- Si `setUp()` falla, el test se marca como error y `tearDown()` no se ejecuta.
- Si `setUp()` tiene éxito, `tearDown()` se ejecuta siempre (aunque el test falle).

### setUpClass y tearDownClass (por clase)

```python
class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()   # una sola vez por clase

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()
```

### setUpModule y tearDownModule (por módulo)

```python
def setUpModule():
    createConnection()      # una sola vez por módulo

def tearDownModule():
    closeConnection()
```

### Orden de ejecución

```
setUpModule → setUpClass → setUp → test → tearDown → tearDownClass → tearDownModule
```

---

## 4. Métodos de aserción

### Aserciones básicas (más usadas)

| Método | Condición que verifica | Desde |
|--------|----------------------|-------|
| `assertEqual(a, b)` | `a == b` | — |
| `assertNotEqual(a, b)` | `a != b` | — |
| `assertTrue(x)` | `bool(x) is True` | — |
| `assertFalse(x)` | `bool(x) is False` | — |
| `assertIs(a, b)` | `a is b` | 3.1 |
| `assertIsNot(a, b)` | `a is not b` | 3.1 |
| `assertIsNone(x)` | `x is None` | 3.1 |
| `assertIsNotNone(x)` | `x is not None` | 3.1 |
| `assertIn(a, b)` | `a in b` | 3.1 |
| `assertNotIn(a, b)` | `a not in b` | 3.1 |
| `assertIsInstance(a, b)` | `isinstance(a, b)` | 3.2 |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` | 3.2 |
| `assertIsSubclass(a, b)` | `issubclass(a, b)` | 3.14 |

### Excepciones, warnings y logs

| Método | Condición | Desde |
|--------|-----------|-------|
| `assertRaises(exc, fun, *args)` | `fun()` lanza `exc` | — |
| `assertRaisesRegex(exc, r, fun)` | lanza `exc` y mensaje matchea regex | 3.1 |
| `assertWarns(warn, fun)` | `fun()` dispara `warn` | 3.2 |
| `assertWarnsRegex(warn, r, fun)` | dispara `warn` y mensaje matchea regex | 3.2 |
| `assertLogs(logger, level)` | el bloque `with` loguea al menos un mensaje | 3.4 |
| `assertNoLogs(logger, level)` | el bloque `with` no loguea nada | 3.10 |

**Uso como context manager (recomendado):**

```python
with self.assertRaises(ValueError) as cm:
    int('XYZ')
self.assertEqual(cm.exception.args[0], "invalid literal for int() with base 10: 'XYZ'")
```

### Comparaciones numéricas y de colecciones

| Método | Condición | Desde |
|--------|-----------|-------|
| `assertAlmostEqual(a, b, places=7)` | `round(a-b, 7) == 0` | — |
| `assertGreater(a, b)` | `a > b` | 3.1 |
| `assertGreaterEqual(a, b)` | `a >= b` | 3.1 |
| `assertLess(a, b)` | `a < b` | 3.1 |
| `assertLessEqual(a, b)` | `a <= b` | 3.1 |
| `assertRegex(s, r)` | `r.search(s)` | 3.1 |
| `assertCountEqual(a, b)` | mismos elementos sin importar orden | 3.2 |
| `assertStartsWith(s, prefix)` | `s.startswith(prefix)` | 3.14 |
| `assertEndsWith(s, suffix)` | `s.endswith(suffix)` | 3.14 |
| `assertHasAttr(obj, name)` | `hasattr(obj, name)` | 3.14 |

### Aserciones por tipo (usadas automáticamente por `assertEqual`)

| Método | Tipos | Desde |
|--------|-------|-------|
| `assertMultiLineEqual(a, b)` | strings | 3.1 |
| `assertSequenceEqual(a, b)` | secuencias | 3.1 |
| `assertListEqual(a, b)` | listas | 3.1 |
| `assertTupleEqual(a, b)` | tuplas | 3.1 |
| `assertSetEqual(a, b)` | sets / frozensets | 3.1 |
| `assertDictEqual(a, b)` | dicts | 3.1 |

> Todos los métodos `assert*` aceptan un argumento `msg` opcional para personalizar el mensaje de error.

---

## 5. Saltar tests y fallas esperadas

```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("razón del skip")
    def test_nada(self):
        self.fail("no debería ejecutarse")

    @unittest.skipIf(sys.version_info < (3, 12), "requiere Python 3.12+")
    def test_feature_nueva(self):
        pass

    @unittest.skipUnless(sys.platform.startswith("linux"), "solo en Linux")
    def test_linux(self):
        pass

    @unittest.expectedFailure
    def test_roto(self):
        self.assertEqual(1, 0, "bug conocido")

    def test_condicional(self):
        if not recurso_disponible():
            self.skipTest("recurso no disponible")
```

| Decorador | Efecto |
|-----------|--------|
| `@skip(reason)` | Siempre omite el test |
| `@skipIf(cond, reason)` | Omite si `cond` es `True` |
| `@skipUnless(cond, reason)` | Omite si `cond` es `False` |
| `@expectedFailure` | Marca como esperado que falle; si pasa, se reporta como error |
| `SkipTest(reason)` | Excepción que salta el test al ser lanzada |

> Tests saltados no ejecutan `setUp`/`tearDown`. Clases saltadas no ejecutan `setUpClass`/`tearDownClass`.

---

## 6. Subtests

Permiten distinguir iteraciones dentro de un mismo método de test:

```python
class NumbersTest(unittest.TestCase):

    def test_even(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```

Sin subtests, el test se detiene en la primera falla. Con subtests, reporta **todas** las fallas encontradas en el loop.

---

## 7. Interfaz de línea de comandos

```bash
# Ejecutar un módulo
python -m unittest test_module

# Ejecutar una clase
python -m unittest test_module.TestClass

# Ejecutar un método específico
python -m unittest test_module.TestClass.test_method

# Verbose
python -m unittest -v test_module

# Opciones útiles
python -m unittest -v    # verbose
python -m unittest -f    # failfast: detener en el primer error
python -m unittest -b    # buffer: ocultar stdout/stderr en tests que pasan
python -m unittest -k foo  # solo tests cuyo nombre contiene "foo"
python -m unittest --durations 5  # mostrar los 5 tests más lentos
```

---

## 8. Descubrimiento automático de tests

```bash
cd project_directory
python -m unittest discover

# Con opciones
python -m unittest discover -s tests/ -p "*_test.py" -v
```

| Opción | Descripción | Default |
|--------|-------------|---------|
| `-s, --start-directory` | Directorio inicial | `.` |
| `-p, --pattern` | Patrón de archivos | `test*.py` |
| `-t, --top-level-directory` | Directorio raíz del proyecto | igual a `-s` |

> Todos los archivos de test deben ser importables como módulos (nombres válidos como identificadores Python).

---

## 9. Agrupación de tests con `TestSuite`

```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

---

## 10. Limpieza con `addCleanup`

Alternativa a `tearDown` para recursos específicos:

```python
class MyTest(unittest.TestCase):

    def setUp(self):
        self.db = open_db()
        self.addCleanup(self.db.close)   # se llama siempre, incluso si setUp falla después
```

- `addCleanup` funciona en orden LIFO (el último agregado se ejecuta primero).
- Incluso si `setUp()` falla parcialmente, las cleanups ya registradas se ejecutan.
- Para el nivel de clase: `addClassCleanup()`.
- Para el nivel de módulo: `addModuleCleanup()`.

---

## 11. Tests asíncronos con `IsolatedAsyncioTestCase`

```python
from unittest import IsolatedAsyncioTestCase

class AsyncTest(IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self._conn = await AsyncConnection()

    async def test_response(self):
        response = await self._conn.get("https://example.com")
        self.assertEqual(response.status_code, 200)

    async def asyncTearDown(self):
        await self._conn.close()
```

> Disponible desde Python 3.8. Cada test corre en un event loop separado.

---

## 12. Clases y funciones principales

| Clase / Función | Descripción |
|-----------------|-------------|
| `unittest.TestCase` | Clase base para todos los tests |
| `unittest.IsolatedAsyncioTestCase` | TestCase para coroutines (async/await) |
| `unittest.FunctionTestCase` | Adaptador para funciones de test legadas |
| `unittest.TestSuite` | Colección de tests |
| `unittest.TestLoader` | Carga y crea suites desde módulos/clases |
| `unittest.TestResult` | Almacena resultados (errores, failures, skips) |
| `unittest.TextTestRunner` | Runner que escribe resultados en texto |
| `unittest.defaultTestLoader` | Instancia compartida de `TestLoader` |
| `unittest.main()` | Función para ejecutar tests desde CLI |

---

## 13. `mock` — Objetos dobles para testing

El módulo complementario `unittest.mock` permite reemplazar partes del sistema bajo test:

```python
from unittest.mock import patch, MagicMock

# Mockear una función externa
with patch('modulo.funcion_externa') as mock_fn:
    mock_fn.return_value = 42
    resultado = funcion_que_usa_externa()
    mock_fn.assert_called_once_with()

# Mockear un objeto completo
mock_obj = MagicMock()
mock_obj.metodo.return_value = "ok"
```

> Documentación completa: [docs.python.org/3/library/unittest.mock.html](https://docs.python.org/3/library/unittest.mock.html)

---

## 14. Comparativa: `unittest` vs `pytest`

| Característica | `unittest` | `pytest` |
|----------------|-----------|---------|
| Instalación | Incluido en stdlib | `pip install pytest` |
| Sintaxis | Orientada a objetos (herencia) | Funciones simples con `assert` |
| Descubrimiento | `test*.py` | `test_*.py` o `*_test.py` |
| Fixtures | `setUp`/`tearDown` | `@pytest.fixture` (más potente) |
| Parametrización | `subTest` | `@pytest.mark.parametrize` |
| Plugins | Limitado | Ecosistema amplio |
| Compatibilidad | Lee tests de `unittest` | Lee tests de `unittest` |

---

## 15. Estructura recomendada de proyecto

```
mi_proyecto/
├── src/
│   └── mi_modulo.py
├── tests/
│   ├── __init__.py
│   ├── test_mi_modulo.py
│   └── test_integracion.py
└── run_tests.py
```

```python
# run_tests.py
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='tests/', pattern='test*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```

---

## 16. Novedades en Python 3.14 (última versión)

- **`assertIsSubclass` / `assertNotIsSubclass`** — nuevos métodos para verificar jerarquía de clases
- **`assertStartsWith` / `assertNotStartsWith`** — verificar prefijos en strings
- **`assertEndsWith` / `assertNotEndsWith`** — verificar sufijos en strings
- **`assertHasAttr` / `assertNotHasAttr`** — verificar atributos en objetos
- **Coloreado de salida por defecto** — la salida en terminal ahora usa colores (controlable con variables de entorno)
- **Test discovery con namespace packages** — soporte restaurado como start_dir

---

## Referencias adicionales

- [Documentación oficial unittest (Python 3.14)](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — Mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [pytest (framework alternativo)](https://docs.pytest.org/)
- [Python Testing Tools Taxonomy](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)
