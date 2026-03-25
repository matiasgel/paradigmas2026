# Filminas — Módulo I: Diseño Ágil + Python
## Tema 01 | Semanas 2–3 | 84 filminas + portada

> **Generado por:** Dr. Roberto ✍️ (class-writer)  
> **Fecha:** 2026-03-25  
> **Basado en:** diseno.md (aprobado), templates/filminas-template.md + filminas-schema.yaml  
> **Coherencia con:** minuta.md (misma secuencia, mismos ejemplos)

---

## PORTADA

---

### [F-00] Portada Módulo I

@tipo: portada
@imagen: background
@prompt-imagen: Large bold horizontal plain rectangle bordo #8B0000 at center. Below it, a thin dark gray horizontal line. Four small identical flat icons arranged in a row near the bottom: small gear circle, small branching tree, small document icon with folded corner, small checkmark badge. White background on upper and lower thirds. Flat minimal design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Módulo I — Diseño Ágil + Python

Laboratorio de Programación y Lenguajes 2026  
Universidad Nacional de Tierra del Fuego — IDEI  
Semanas 2 y 3 · 4 sesiones · 12 hs totales

---

## SESIÓN T1 — Semana 2, Teoría

---

## BLOQUE T1-A — El Modelo Ágil + IDEs (45 min)

---

### [F-01] Agenda T1

@tipo: concepto-abstracto

# Hoja de ruta: sesión T1

## Cuatro bloques en 180 minutos

| Bloque | Contenido | Tiempo |
|--------|-----------|--------|
| T1-A | Modelo Ágil + VS Code + Codespaces | 45 min |
| T1-B | Python 3.13 fundamentos | 45 min |
| T1-C | Control de flujo + funciones | 30 min |
| T1-D | Ruff + PEP 8 + preview TP2 | 20 min |

---

### [F-02] ¿Qué es el Modelo Ágil?

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Two columns side by side on white background. Left column: four stacked plain gray rectangles of the same size connected by thin downward arrows, rigid and evenly spaced. Right column: four small circles arranged in a circular loop connected by curved bordo arrows forming a cycle. Flat design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Una forma diferente de construir software

## ¿De dónde viene?

- Surge como respuesta al modelo de **cascada** (waterfall, 1970s)
- En cascada: fases secuenciales, sin vuelta atrás
- Problema: el cliente recibe software meses después y no era lo que quería

## La propuesta ágil

- **Iteraciones cortas** (semanas, no meses)
- Software funcional al final de cada iteración
- **Feedback continuo** del usuario → ajustes permanentes
- Equipos pequeños, comunicación directa

---

### [F-03] El Manifiesto Ágil — 2001

@tipo: tabla-comparativa

# 4 valores que cambiaron la industria

## Agile Manifesto (Beck et al., 2001)

| Valoramos **más** | Que |
|-------------------|-----|
| **Individuos e interacciones** | Procesos y herramientas |
| **Software funcionando** | Documentación exhaustiva |
| **Colaboración con el cliente** | Negociación de contratos |
| **Respuesta al cambio** | Seguimiento de un plan |

> "Esto no significa que lo de la derecha no importe — simplemente priorizamos lo de la izquierda."

---

### [F-04] Cascada vs. Ágil

@tipo: tabla-comparativa

# El cambio de paradigma en desarrollo

| Dimensión | Cascada | Ágil |
|-----------|---------|------|
| Planificación | Total al inicio | Incremental |
| Entregas | Al final del proyecto | Cada iteración |
| Cambio de requisitos | Costoso o imposible | Bienvenido |
| Feedback del cliente | Una vez, al final | Continuo |
| Riesgo | Alto (se descubre tarde) | Bajo (se descubre pronto) |
| Documentación | Muy extensa antes | Justo a tiempo |

---

### [F-05] El Ciclo Iterativo

@tipo: diagrama
@imagen: content
@prompt-imagen: Five flat icons arranged in a large circle connected by bordo curved arrows going clockwise. Top: magnifying glass (pequeño). Right: pencil shape pointing right. Bottom-right: small cube. Bottom-left: checkmark circle. Left: gear icon small. Center: one small star shape. White background. Flat minimal style. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Planificar → Diseñar → Construir → Probar → Revisar

## En cada iteración (sprint)

- **Planificar**: ¿Qué se va a hacer esta semana?
- **Diseñar**: ¿Cómo lo vamos a hacer?
- **Construir**: Código, commits, pull requests
- **Probar**: Tests automáticos, revisión humana
- **Revisar**: ¿Funcionó? ¿Qué mejoramos?

## En este curso

- La "iteración" es el módulo temático
- El "entregable" es el TP con tests en verde (CI)
- El "cliente" es el enunciado + los tests de pytest

---

### [F-06] Setup: VS Code + extensiones esenciales

@tipo: concepto-abstracto

# El IDE como herramienta de feedback inmediato

## Extensiones instaladas en el devcontainer

```
# En .devcontainer/devcontainer.json
"extensions": [
    "ms-python.python",        // Python base
    "ms-python.pylance",       // Type checking en tiempo real
    "charliermarsh.ruff",      // Linter ultrarrápido
    "eamodio.gitlens"          // Historial Git en línea
]
```

## ¿Por qué estas y no otras?

- **Pylance** → detecta errores de tipo antes de ejecutar
- **Ruff** → 100× más rápido que Flake8, reemplaza Black + isort
- **GitLens** → hace visible el historial directamente en el editor

---

### [F-07] Pylance — type checking en tiempo real

@tipo: codigo

# El linter que te habla mientras escribís

## Qué detecta antes de ejecutar

```python
def sumar(a: int, b: int) -> int:
    return a + b

resultado = sumar("hola", 3)
# Pylance subrayará "hola" en rojo:
# Argument of type "str" cannot be assigned to parameter "a"
```

## Por qué importa en el curso

- Los type hints en el TP2 son **obligatorios**
- Pylance convierte el editor en un "tutor silencioso"
- No necesitás ejecutar para saber si el tipo está mal

---

### [F-08] Ruff — linter ultrarrápido

@tipo: codigo

# PEP 8 automatizado desde el primer keystroke

## Instalación y uso

```bash
# En terminal (ya incluido en devcontainer)
pip install ruff

# Verificar un archivo
ruff check src/hello.py

# Corregir automáticamente
ruff check --fix src/hello.py
```

## Lo que detecta (entre muchas cosas)

- Espacios/indentación incorrectos (E1, W)
- Nombres que no siguen snake_case / UpperCamelCase (N)
- Imports no usados (F401)
- Funciones sin docstring (D)
- Type hints faltantes cuando están activados

---

### [F-09] GitLens — historial visible en el editor

@tipo: concepto-abstracto

# Ver el "porqué" del código sin salir del editor

## Qué muestra GitLens

- Quién escribió cada línea y en qué commit (git blame inline)
- Mensajes de commit en el margen del archivo
- Comparar versiones de una función directamente

## Relevancia para el TP2

- Los commits tienen **20% del puntaje**
- GitLens hace visible si "fix" y "update" son mensajes malos
- Muestra la diferencia entre un commit atómico y uno masivo

---

### [F-10] GitHub Codespaces

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Flat icon of a monitor with a small cloud shape floating above it connected by a thin upward arrow. Below the monitor, four small identical rectangle shapes arranged in a single row. White background. Bordo and dark gray palette. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# El entorno de desarrollo en la nube

## ¿Qué es Codespaces?

- VS Code corriendo en un servidor de GitHub
- No necesitás instalar nada en tu computadora local
- El entorno está **definido como código** (`devcontainer.json`)
- Reproducible exactamente igual para el docente y el alumno

## Flujo en el curso

1. Aceptar TP2 en GitHub Classroom
2. Abrir el repo → botón "Open in Codespace"
3. El devcontainer instala Python 3.13, Ruff, pytest
4. Comenzar a codear

---

### [F-11] DevContainer — el entorno como código

@tipo: codigo

# Un único archivo que define el entorno completo

```json
// .devcontainer/devcontainer.json
{
  "name": "Python 3.13",
  "image": "mcr.microsoft.com/devcontainers/python:3.13",
  "features": {
    "ghcr.io/devcontainers/features/git:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.pylance",
        "charliermarsh.ruff",
        "github.copilot"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python"
      }
    }
  },
  "postCreateCommand": "pip install -r requirements.txt"
}
```

## Resultado

- Cualquier alumno abre el repo y tiene exactamente el mismo entorno
- CI (GitHub Actions) usa la misma imagen → consistency garantizada

---

### [F-12] Cierre T1-A

@tipo: socratica

# ¿Por qué el modelo ágil encaja con el desarrollo actual?

## Pregunta para reflexionar

Tenemos el TP2 con **tests automáticos preescritos** y **CI que corre en cada push**.

- ¿Eso es más cercano a cascada o a ágil?
- ¿Los tests son el "cliente"?
- ¿Cómo sabés si "terminaste" una tarea?

## Una respuesta posible

Los tests definen el comportamiento esperado → el alumno itera hasta que todos pasen. Eso es **Red → Green → Refactor**: el ciclo ágil más chico posible.

---

## BLOQUE T1-B — Python 3.13 Fundamentos (45 min)

---

### [F-13] ¿Por qué Python en 2026?

@tipo: concepto-abstracto

# El lenguaje que llegó para quedarse

## Datos de contexto

- Primer lugar en índice TIOBE 2024–2026 (superó a C)
- Lenguaje dominante en IA/ML, scripting, web backend (FastAPI, Django)
- Python 3.13 (octubre 2024) — mejoras significativas de usabilidad

## Para este curso

- Es el lenguaje del TP2 y del Módulo I completo
- OOP se introduce en Módulo IV (Tema 04)
- Hoy: fundamentos que necesitás para el TP2

---

### [F-14] Tipos primitivos en Python

@tipo: tabla

# Cinco tipos fundamentales

| Tipo | Ejemplo | Notas |
|------|---------|-------|
| `int` | `42`, `-7`, `0` | Sin límite de tamaño en Python |
| `float` | `3.14`, `-0.5` | Punto flotante IEEE 754 |
| `str` | `"hola"`, `'mundo'` | Inmutable |
| `bool` | `True`, `False` | Subclase de `int` (True=1, False=0) |
| `None` | `None` | Ausencia de valor (tipo `NoneType`) |

---

### [F-15] Asignación y operadores

@tipo: codigo

# Python no tiene declaración de tipo obligatoria

## Asignación

```python
nombre = "Ada"           # str
edad = 25                # int
altura = 1.65            # float
activo = True            # bool
resultado = None         # NoneType
```

## Operadores aritméticos

```python
# Estándar
suma = 10 + 3        # 13
resta = 10 - 3       # 7
producto = 10 * 3    # 30
division = 10 / 3    # 3.333... (siempre float)

# Especiales
cociente = 10 // 3   # 3 (división entera)
modulo = 10 % 3      # 1 (resto)
potencia = 2 ** 8    # 256
```

---

### [F-16] Python 3.13 — Nuevo REPL interactivo

@tipo: demo

# Demo en vivo: el shell mejorado de Python 3.13

## Qué hay de nuevo en el REPL

```python
# Antes (Python < 3.13): imposible pegar código multilínea
>>> def saludar(nombre):
...     return f"Hola {nombre}"
...

# Ahora (Python 3.13): historial persistente + colores + multilínea mejorado
>>> def saludar(nombre: str) -> str:
...     """Devuelve un saludo personalizado."""
...     return f"Hola {nombre}"
...
>>> saludar("Python")
'Hola Python'
```

## Ventajas pedagógicas

- Sintaxis coloreada directamente en terminal
- Historial que persiste entre sesiones (`~/.python_history`)
- Pegado de bloques multilínea sin romperse

---

### [F-17] Mensajes de error contextuales en Python 3.13

@tipo: codigo

# Python 3.13 te dice qué quisiste escribir

## Antes vs. ahora

```python
# Python 3.12 — error genérico
>>> "hola".upper_case()
AttributeError: 'str' object has no attribute 'upper_case'

# Python 3.13 — sugerencia integrada
>>> "hola".upper_case()
AttributeError: 'str' object has no attribute 'upper_case'.
Did you mean: 'upper'?
```

## Otro ejemplo

```python
>>> import math
>>> math.squareroot(16)
AttributeError: module 'math' has no attribute 'squareroot'.
Did you mean: 'sqrt'?
```

## Por qué importa

- Reduce el tiempo de debugging para principiantes
- Se produce **antes** de buscar en Google

---

### [F-18] Strings — inmutabilidad

@tipo: concepto-mixto

# Los strings no cambian — se reemplazan

## Inmutabilidad en la práctica

```python
nombre = "Ada"
nombre[0] = "E"   # ❌ TypeError: 'str' object does not support item assignment

# Para "cambiar" un string: crear uno nuevo
nombre_nuevo = "E" + nombre[1:]   # "Eda"

# O usar métodos que devuelven un nuevo string
nombre_upper = nombre.upper()     # "ADA" (nuevo objeto)
print(nombre)                     # "Ada" (sin cambios)
```

## La diferencia con las listas

```python
lista = [1, 2, 3]
lista[0] = 99   # ✅ Las listas SÍ son mutables
print(lista)    # [99, 2, 3]
```

---

### [F-19] Strings — métodos más usados

@tipo: tabla

# Referencia rápida de métodos de string

| Método | Qué hace | Ejemplo |
|--------|----------|---------|
| `.upper()` / `.lower()` | Mayúsculas / minúsculas | `"Ada".upper()` → `"ADA"` |
| `.strip()` | Quita espacios en los extremos | `" hola ".strip()` → `"hola"` |
| `.split(sep)` | Divide en lista por separador | `"a,b".split(",")` → `["a","b"]` |
| `.join(iterable)` | Une lista en string | `",".join(["a","b"])` → `"a,b"` |
| `.replace(v, n)` | Reemplaza subcadena | `"hola".replace("o","0")` → `"h0la"` |
| `.startswith(s)` | Verifica prefijo | `"Python".startswith("Py")` → `True` |
| `f"texto {var}"` | f-string interpolación | `f"Hola {nombre}"` |

---

### [F-20] f-strings — interpolación modernaa

@tipo: codigo

# La forma pythónica de construir strings

## Sintaxis básica

```python
nombre = "Python"
version = 3.13
mensaje = f"Bienvenidos a {nombre} {version}"
# → "Bienvenidos a Python 3.13"
```

## Expresiones dentro del f-string

```python
precio = 1500
descuento = 0.1
total = f"Total: ${precio * (1 - descuento):.2f}"
# → "Total: $1350.00"
```

## Formato numérico

```python
pi = 3.14159265
print(f"Pi ≈ {pi:.4f}")   # Pi ≈ 3.1416
print(f"Pi ≈ {pi:>10.2f}")  # Pi ≈       3.14  (alineado a la derecha)
```

---

### [F-21] Variables y referencias

@tipo: concepto-abstracto

# En Python, las variables son etiquetas, no cajas

## El modelo mental correcto

```python
a = [1, 2, 3]
b = a           # b apunta al MISMO objeto
b.append(4)
print(a)        # [1, 2, 3, 4] — ambas apuntan al mismo objeto

# Para hacer una copia independiente:
c = a.copy()    # o c = list(a) o c = a[:]
c.append(99)
print(a)        # [1, 2, 3, 4] — sin cambios
```

## Por qué importa para el TP2

- Las funciones reciben **referencias**, no copias
- Si modificás una lista dentro de una función, la original cambia
- Para evitarlo: copiar explícitamente o usar `tuple` (inmutable)

---

### [F-22] None y Boolean — detalles que sorprenden

@tipo: codigo

# None no es False, pero se comporta parecido

## None

```python
def buscar(lista: list, valor: int) -> int | None:
    for i, x in enumerate(lista):
        if x == valor:
            return i
    return None   # Señal explícita de "no encontrado"

resultado = buscar([1, 2, 3], 99)
if resultado is None:          # ✅ Comparar con "is", no "=="
    print("No encontrado")
```

## Boolean — sorpresas

```python
print(True + True)    # 2  (bool es subclase de int)
print(bool(""))       # False (string vacío es falsy)
print(bool([]))       # False (lista vacía es falsy)
print(bool(0))        # False  →  0, None, [], {}, "" son todos falsy
```

---

### [F-23] Conversiones de tipo

@tipo: codigo

# Python no convierte automáticamente — hay que pedirlo

## Funciones de conversión

```python
# str → int / float
edad = int("25")           # 25
precio = float("19.99")    # 19.99

# int / float → str
texto = str(42)            # "42"
texto = str(3.14)          # "3.14"

# str → lista de caracteres
letras = list("Python")    # ["P", "y", "t", "h", "o", "n"]

# Validar antes de convertir
entrada = "abc"
if entrada.isdigit():
    numero = int(entrada)
else:
    print("No es un número válido")
```

---

### [F-24] Inmutabilidad: str vs list

@tipo: tabla-comparativa

# Cuándo usar str vs list

| Característica | `str` | `list` |
|----------------|-------|--------|
| Mutabilidad | Inmutable ❌ | Mutable ✅ |
| Indexación | `s[0]` | `l[0]` |
| Modificar elemento | ❌ TypeError | ✅ `l[0] = x` |
| Concatenar | `s1 + s2` (crea nuevo) | `l1 + l2` o `.append()` |
| Longitud | `len(s)` | `len(l)` |
| Iterable | ✅ | ✅ |
| Hashable (usable como clave de dict) | ✅ | ❌ |

---

### [F-25] Operadores de identidad y pertenencia

@tipo: codigo

# is, is not, in, not in

## Identidad (¿es el mismo objeto?)

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)    # True  — misma referencia
print(a is c)    # False — mismo contenido, objetos distintos
print(a == c)    # True  — == compara contenido

# Usar "is" solo para None, True, False
valor = None
if valor is None: ...   # ✅ Pythónico
if valor == None: ...   # ⚠️  Funciona pero es menos correcto
```

## Pertenencia

```python
lista = [1, 2, 3]
print(2 in lista)           # True
print("Py" in "Python")     # True  — funciona con strings también
print(5 not in lista)       # True
```

---

### [F-26] Cierre T1-B

@tipo: socratica

# ¿Qué tipo Python usarías para...?

## Preguntas rápidas (1 minuto)

1. Almacenar el nombre de un usuario → `str`
2. Almacenar la edad → `int`
3. Almacenar si está activo → `bool`
4. Devolver "no encontrado" desde una función → `None`
5. Una colección de nombres que no debe cambiar → `tuple`

## El punto central

Python infiere el tipo → **no necesitás declararlo**  
Pero declararlo (type hints) hace el código **legible y verificable con Ruff/Pylance**

---

## BLOQUE T1-C — Control de flujo + funciones (30 min)

---

### [F-27] if / elif / else

@tipo: codigo

# Selección condicional — la forma pythónica

```python
def clasificar_nota(nota: int) -> str:
    """Clasifica una nota numérica en categoría textual."""
    if nota >= 90:
        return "Sobresaliente"
    elif nota >= 70:
        return "Aprobado"
    elif nota >= 50:
        return "Regular"
    else:
        return "Desaprobado"

print(clasificar_nota(85))   # "Aprobado"
```

## Lo que NOT hacer

```python
# ❌ Sin type hints, sin docstring, lógica invertida
def check(x):
    if not x >= 70:
        return "malo"
    return "bueno"
```

---

### [F-28] for sobre secuencias

@tipo: codigo

# Iteración directa — sin índices cuando no se necesitan

## Sobre una lista

```python
frutas = ["manzana", "banana", "pera"]
for fruta in frutas:
    print(fruta.upper())
```

## Sobre un rango de números

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(f"Iteración {i}")

for i in range(1, 11):    # 1 hasta 10
    print(i)

for i in range(0, 20, 2): # 0, 2, 4, ..., 18 (paso 2)
    print(i)
```

## Sobre string (carácter por carácter)

```python
for letra in "Python":
    print(letra)          # P, y, t, h, o, n
```

---

### [F-29] while + break + continue

@tipo: codigo

# Iteración condicional y control de flujo

## while

```python
intentos = 0
MAX_INTENTOS = 3

while intentos < MAX_INTENTOS:
    clave = input("Ingresá tu clave: ")
    if clave == "1234":
        print("Acceso concedido")
        break
    intentos += 1
    print(f"Intento {intentos} de {MAX_INTENTOS}")
else:
    # Bloque else del while: se ejecuta si NO hubo break
    print("Acceso bloqueado")
```

## continue — saltar iteración

```python
for i in range(10):
    if i % 2 == 0:
        continue    # salta los pares
    print(i)        # imprime 1, 3, 5, 7, 9
```

---

### [F-30] match — Pattern Matching (Python 3.10+)

@tipo: codigo

# PEP 636: más expresivo que if/elif encadenado

## Caso básico — valores literales

```python
def describir_http(codigo: int) -> str:
    """Describe un código HTTP."""
    match codigo:
        case 200:
            return "OK"
        case 404:
            return "No encontrado"
        case 500:
            return "Error del servidor"
        case _:
            return f"Código desconocido: {codigo}"
```

## Caso con tuplas (destructuring)

```python
punto = (1, 0)
match punto:
    case (0, 0):
        print("Origen")
    case (x, 0):
        print(f"En el eje X: {x}")
    case (0, y):
        print(f"En el eje Y: {y}")
    case (x, y):
        print(f"Punto general: ({x}, {y})")
```

---

### [F-31] def + return + docstrings

@tipo: codigo

# La anatomía de una función Python

```python
def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso_kg: Peso del paciente en kilogramos.
        altura_m: Altura del paciente en metros.

    Returns:
        IMC calculado como peso / altura^2.
    """
    if altura_m <= 0:
        raise ValueError("La altura debe ser positiva")
    return peso_kg / (altura_m ** 2)

# Uso
imc = calcular_imc(70, 1.75)
print(f"IMC: {imc:.1f}")   # IMC: 22.9
```

---

### [F-32] Parámetros — posicionales y keyword

@tipo: codigo

# Python distingue cómo se pasan los argumentos

## Posicionales, keyword y por defecto

```python
def crear_usuario(
    nombre: str,
    edad: int,
    rol: str = "alumno"   # valor por defecto
) -> dict:
    """Crea un dict representando un usuario."""
    return {"nombre": nombre, "edad": edad, "rol": rol}

# Llamadas válidas
u1 = crear_usuario("Ana", 22)                   # usa default
u2 = crear_usuario("Bob", 30, "docente")        # posicional
u3 = crear_usuario(edad=25, nombre="Carlos")    # keyword
u4 = crear_usuario("Dani", 19, rol="admin")     # mixto
```

## Forzar keyword-only (después de *)

```python
def conectar(host: str, *, puerto: int = 80, timeout: int = 30) -> None:
    ...  # puerto y timeout SOLO se pueden pasar por keyword
```

---

### [F-33] *args y **kwargs

@tipo: codigo

# Funciones con cantidad variable de argumentos

## *args — posicionales variables

```python
def sumar_todos(*numeros: int) -> int:
    """Suma cualquier cantidad de números."""
    return sum(numeros)

print(sumar_todos(1, 2, 3))       # 6
print(sumar_todos(10, 20, 30, 40)) # 100
```

## **kwargs — keyword variables

```python
def log_evento(tipo: str, **detalles: str) -> None:
    """Registra un evento con detalles opcionales."""
    print(f"[{tipo}]", " ".join(f"{k}={v}" for k, v in detalles.items()))

log_evento("LOGIN", usuario="ana", ip="192.168.1.1")
# [LOGIN] usuario=ana ip=192.168.1.1
```

---

### [F-34] Scope de variables

@tipo: concepto-mixto

# Las variables tienen alcance definido

## Local vs global

```python
contador = 0   # Variable global

def incrementar() -> None:
    """Incrementa el contador global."""
    global contador    # Declarar explícitamente
    contador += 1

def calcular(x: int) -> int:
    resultado = x * 2  # Variable LOCAL a la función
    return resultado

# resultado no es accesible aquí → NameError
```

## Regla LEGB

| Scope | Descripción |
|-------|-------------|
| **L**ocal | Dentro de la función actual |
| **E**nclosing | Función externa (closures) |
| **G**lobal | Nivel del módulo |
| **B**uilt-in | `len`, `print`, `range`, etc. |

---

### [F-35] Recursión básica

@tipo: codigo

# Una función que se llama a sí misma

```python
def factorial(n: int) -> int:
    """Calcula n! recursivamente.

    Args:
        n: Número entero no negativo.

    Returns:
        El factorial de n.
    """
    if n == 0 or n == 1:   # Caso base
        return 1
    return n * factorial(n - 1)   # Caso recursivo

print(factorial(5))   # 120
```

## Traza de ejecución

```
factorial(5)
  = 5 * factorial(4)
  = 5 * 4 * factorial(3)
  = 5 * 4 * 3 * factorial(2)
  = 5 * 4 * 3 * 2 * factorial(1)
  = 5 * 4 * 3 * 2 * 1 = 120
```

---

### [F-36] Cierre T1-C

@tipo: socratica

# ¿Cuándo usar for, while o match?

## Preguntas rápidas

- Iterar sobre **elementos de una lista** → `for ... in ...`
- Repetir hasta que se cumpla una **condición** desconocida → `while`
- Evaluar **casos mútuamente excluyentes** → `match`

## Pregunta abierta

Tenés este código del TP2:

```python
def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

¿Cómo mejorarlo para que sea más eficiente? *(Pista: ¿hasta qué número necesitás verificar?)*

---

## BLOQUE T1-D — Ruff + PEP 8 (20 min)

---

### [F-37] ¿Qué es PEP 8?

@tipo: concepto-abstracto

# La guía de estilo oficial de Python desde 2001

## Los 5 puntos más importantes para el TP2

| Regla PEP 8 | Mal | Bien |
|------------|-----|------|
| Indentación | 2 o 3 espacios | **4 espacios** |
| Largo de línea | más de 88 chars | **máx 88 chars** (estilo Ruff) |
| Nombres de funciones | `MiFunc`, `mifunc` | **`mi_func`** (snake_case) |
| Nombres de clases | `mi_clase` | **`MiClase`** (UpperCamelCase) |
| Constantes | `mi_constante` | **`MI_CONSTANTE`** |

> "Readability counts" — The Zen of Python, Tim Peters

---

### [F-38] Código autodocumentado

@tipo: concepto-mixto

# El código debe explicarse solo antes que con comentarios

## Antes (opaco)

```python
def f(x, y):
    r = []
    for i in x:
        if i > y:
            r.append(i)
    return r
```

## Después (autodocumentado)

```python
def filtrar_mayores(numeros: list[int], umbral: int) -> list[int]:
    """Retorna los números de la lista que superan el umbral."""
    return [n for n in numeros if n > umbral]
```

## Principio de responsabilidad única

- Una función = una sola responsabilidad
- Si necesitás `# Parte 1 / Parte 2` dentro de una función → dividila

---

### [F-39] Convenciones de nombres — resumen ejecutivo

@tipo: tabla

# Qué nombre usar para qué

| Tipo | Convención | Ejemplo |
|------|------------|---------|
| Variable / función | `snake_case` | `nombre_usuario`, `calcular_imc()` |
| Módulo | `snake_case` | `mi_modulo.py` |
| Clase | `UpperCamelCase` | `CalculadoraImpuestos` |
| Constante global | `UPPER_SNAKE_CASE` | `MAX_INTENTOS = 3` |
| "Privado" | `_prefijo_bajo` | `_validar_internamente()` |
| Interno Python | `__dunder__` | `__init__`, `__str__` |

> Ruff detecta y marca automáticamente violaciones a estas convenciones (reglas del grupo N).

---

### [F-40] Ruff en acción — ejemplos reales

@tipo: codigo

# Los errores que Ruff detectará en tu TP2

```python
# Código con errores — lo que Ruff va a marcar

import os          # F401: "os" imported but unused
import sys

def calcular( x,y ):    # E231, E203: espacios incorrectos
    resultado=x+y       # E225: missing whitespace around operator
    return resultado

# Ruff --fix lo arregla automáticamente:
import sys

def calcular(x: int, y: int) -> int:
    resultado = x + y
    return resultado
```

## Activarlo en el curso

- Ruff está en el devcontainer → auto-lint al guardar
- `ruff check src/` antes de cada commit (buena práctica)
- En CI: `ruff check .` falla el build si hay errores

---

### [F-41] Preview TP2 — ¿Qué vas a entregar?

@tipo: concepto-abstracto

# Estructura del repositorio del TP2

```
tp2-python-prompting-TU_USUARIO/
├── src/
│   ├── __init__.py
│   ├── hello.py           # Script 1
│   ├── calculadora.py     # Script 2
│   ├── temperatura.py     # Script 3
│   ├── fibonacci.py       # Script 4
│   ├── colecciones.py     # Script 5
│   ├── funciones_ord.py   # Script 6
│   └── type_hints.py      # Script 7
├── tests/
│   ├── test_hello.py
│   ├── test_calculadora.py
│   └── ...
├── PROMPTS.md             # ← 20% del puntaje
└── requirements.txt
```

## Criterio de aprobación base

- ≥ 5/7 archivos con tests en verde vía CI
- ≥ 7 commits con mensajes descriptivos
- PROMPTS.md con ≥ 3 prompts completos

---

### [F-42] Cierre T1 — Resumen y pausa

@tipo: cierre

# Lo que cubrimos en esta sesión

## T1-A: Modelo Ágil + IDEs

- Manifiesto Ágil y ciclo iterativo
- VS Code + Pylance + Ruff + GitLens
- GitHub Codespaces + devcontainer.json

## T1-B: Python 3.13 Fundamentos

- Tipos: `int`, `float`, `str`, `bool`, `None`
- Inmutabilidad de strings, referencias de lista
- REPL 3.13, errores contextuales, f-strings

## T1-C: Control de flujo + funciones

- `if/elif/else`, `for`, `while`, `match`
- `def`, `return`, docstrings, parámetros

## T1-D: Ruff + PEP 8

- PEP 8: snake_case, UpperCamelCase, 4 espacios
- Ruff como linter automático desde el día 1

---

## SESIÓN T2 — Semana 3, Teoría

---

### [F-43] Agenda T2

@tipo: portada
@imagen: background
@prompt-imagen: Horizontal bar of bordo color at top third of image. Below it, four evenly spaced small flat icons in a row on white background: stacked cylinders shape, small branching tree shape, small diamond shape with arrow, small gear with arrow. Below the icons, a thin gray horizontal line at bottom. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Sesión T2 — Semana 3

## Cuatro bloques en 180 minutos

| Bloque | Contenido | Tiempo |
|--------|-----------|--------|
| T2-A | Colecciones: list, tuple, dict, set | 45 min |
| T2-B | Módulos + HOF + lambdas + decoradores | 45 min |
| T2-C | Type hints Python 3.10+ (PEP 484) | 30 min |
| T2-D | Prompting para debugging | 20 min |

---

## BLOQUE T2-A — Colecciones Python (45 min)

---

### [F-44] Las cuatro colecciones fundamentales

@tipo: tabla-comparativa

# list, tuple, dict, set — cuándo usar cada una

| Colección | Mutable | Ordenada | Duplicados | Caso de uso |
|-----------|---------|----------|------------|-------------|
| `list` | ✅ | ✅ | ✅ | Secuencia que cambia |
| `tuple` | ❌ | ✅ | ✅ | Coordenadas, registros fijos |
| `dict` | ✅ | ✅ (3.7+) | ❌ claves | Mapa clave→valor |
| `set` | ✅ | ❌ | ❌ | Conjuntos, dedup rápido |

---

### [F-45] list — la colección más usada

@tipo: codigo

# Secuencia mutable, indexada desde 0

```python
# Creación
notas = [85, 72, 91, 68, 77]

# Acceso
print(notas[0])     # 85 (primer elemento)
print(notas[-1])    # 77 (último elemento)
print(notas[1:3])   # [72, 91] (slicing)

# Modificación
notas.append(95)        # agrega al final
notas.insert(0, 100)    # inserta en posición 0
notas.remove(68)        # borra por valor
popped = notas.pop()    # extrae y devuelve el último

# Utilidades
print(len(notas))         # longitud
print(sorted(notas))      # nueva lista ordenada
notas.sort()              # ordena in-place
notas.sort(reverse=True)  # orden descendente
```

---

### [F-46] tuple — inmutabilidad como diseño

@tipo: codigo

# Cuando los datos NO deben cambiar

```python
# Crear
punto_2d = (3, 5)
coordenadas_rgb = (255, 128, 0)

# Acceso (igual que lista)
x, y = punto_2d   # unpacking
print(x)   # 3
print(y)   # 5

# No se puede modificar
punto_2d[0] = 99   # ❌ TypeError: 'tuple' object does not support item assignment

# Útil como clave de diccionario (es hashable)
mapa = {(0, 0): "origen", (1, 0): "derecha"}
print(mapa[(0, 0)])   # "origen"
```

## Cuándo usar tuple

- Coordenadas, colores RGB, resultados de funciones múltiples
- Cuando querés que la semántica diga "esto no debe cambiar"

---

### [F-47] dict — mapa clave-valor

@tipo: codigo

# La estructura de datos más versátil de Python

```python
# Crear
alumno = {
    "nombre": "Ana García",
    "legajo": 12345,
    "notas": [85, 90, 78]
}

# Acceso seguro
nombre = alumno["nombre"]               # ✅ directo
email = alumno.get("email", "sin email")  # ✅ con default

# Modificar
alumno["legajo"] = 99999           # actualiza
alumno["carrera"] = "Sistemas"     # agrega clave nueva

# Iterar
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

# Verificar existencia
if "notas" in alumno:
    print(alumno["notas"])
```

---

### [F-48] set — conjuntos sin duplicados

@tipo: codigo

# Cuando necesitás unicidad o teoría de conjuntos

```python
# Crear
lenguajes_alumno_a = {"Python", "JavaScript", "C"}
lenguajes_alumno_b = {"Python", "Java", "C", "Go"}

# Operaciones de conjuntos
comunes = lenguajes_alumno_a & lenguajes_alumno_b   # intersección
todos = lenguajes_alumno_a | lenguajes_alumno_b     # unión
solo_a = lenguajes_alumno_a - lenguajes_alumno_b    # diferencia

print(comunes)  # {'Python', 'C'}

# Eliminar duplicados de una lista
lista_con_dup = [1, 2, 2, 3, 3, 4]
sin_dup = list(set(lista_con_dup))  # [1, 2, 3, 4]
```

---

### [F-49] Comprensiones de lista

@tipo: codigo

# La forma pythónica de transformar secuencias

## Patrón base

```python
# Sin comprensión (imperativo)
cuadrados = []
for x in range(10):
    cuadrados.append(x ** 2)

# Con comprensión (expresivo)
cuadrados = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Con filtro

```python
pares = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## Comprensión anidada

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [num for fila in matriz for num in fila]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### [F-50] Comprensiones de dict y set

@tipo: codigo

# El mismo patrón para otras colecciones

## Dict comprehension

```python
# Crear un dict {nombre: longitud_nombre}
nombres = ["Ana", "Roberto", "Li", "Valentina"]
longitudes = {n: len(n) for n in nombres}
# {'Ana': 3, 'Roberto': 7, 'Li': 2, 'Valentina': 9}

# Invertir un diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

## Set comprehension

```python
# Longitudes únicas de palabras
palabras = ["hola", "mundo", "hola", "python"]
longitudes_unicas = {len(p) for p in palabras}
# {4, 5, 6}
```

---

### [F-51] enumerate() y zip()

@tipo: codigo

# Dos builtins que evitan el contador manual

## enumerate() — índice automático

```python
frutas = ["manzana", "banana", "cereza"]

# ❌ Sin enumerate (anticuado)
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

# ✅ Con enumerate
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# Empezar desde 1
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}. {fruta}")
```

## zip() — iterar en paralelo

```python
nombres = ["Ana", "Bob", "Carlos"]
notas = [85, 72, 91]

for nombre, nota in zip(nombres, notas):
    print(f"{nombre}: {nota}")
```

---

### [F-52] sorted(), min(), max() con key=

@tipo: codigo

# Ordenar y comparar por criterio personalizado

## sorted() con key

```python
alumnos = [
    {"nombre": "Carlos", "nota": 72},
    {"nombre": "Ana",    "nota": 91},
    {"nombre": "Bob",    "nota": 85},
]

# Ordenar por nota ascendente
por_nota = sorted(alumnos, key=lambda a: a["nota"])

# Ordenar por nombre
por_nombre = sorted(alumnos, key=lambda a: a["nombre"])

# Max y min por criterio
mejor = max(alumnos, key=lambda a: a["nota"])
peor = min(alumnos, key=lambda a: a["nota"])
print(mejor["nombre"])   # "Ana"
```

---

### [F-53] Funciones builtin de reducción

@tipo: tabla

# sum, len, min, max — resumen

| Función | Qué hace | Ejemplo |
|---------|----------|---------|
| `len(x)` | Longitud de cualquier iterable | `len([1,2,3])` → `3` |
| `sum(x)` | Suma de iterable numérico | `sum([1,2,3])` → `6` |
| `min(x)` | Elemento mínimo | `min([3,1,2])` → `1` |
| `max(x)` | Elemento máximo | `max([3,1,2])` → `3` |
| `sorted(x)` | Nueva lista ordenada | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed(x)` | Iterador inverso | `list(reversed([1,2,3]))` → `[3,2,1]` |
| `any(x)` | True si algún elemento es truthy | `any([0, 1, 0])` → `True` |
| `all(x)` | True si TODOS son truthy | `all([1, 1, 0])` → `False` |

---

### [F-54] Slicing avanzado

@tipo: codigo

# Extraer subsecuencias en listas y strings

## Sintaxis: `seq[inicio:fin:paso]`

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros[2:5]    # [2, 3, 4]  (desde índice 2, hasta antes del 5)
numeros[:3]     # [0, 1, 2]  (desde el inicio hasta antes del 3)
numeros[7:]     # [7, 8, 9]  (desde índice 7 hasta el final)
numeros[::2]    # [0, 2, 4, 6, 8]  (cada dos elementos)
numeros[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  (invertir)
```

## Con strings (identica sintaxis)

```python
texto = "Python 3.13"
texto[7:]      # "3.13"
texto[:6]      # "Python"
texto[::-1]    # "31.3 nohtyP"
```

---

### [F-55] Elegir la colección correcta

@tipo: socratica

# ¿Qué colección usarías para...?

## Casos de uso del TP2

1. Guardar los resultados de las notas de varios alumnos (puede cambiar) → **list**
2. Representar las coordenadas (x, y) de un punto → **tuple**
3. Mapear legajo → nombre del alumno → **dict**
4. Guardar el conjunto de lenguajes únicos que conoce cada alumno → **set**
5. Filtrar solo los alumnos con nota ≥ 70 sin un for explícito → **comprensión de lista**

---

### [F-56] Cierre T2-A

@tipo: cierre

# Colecciones — lo esencial

## Qué vimos

- `list` — secuencia mutable: `append`, `sort`, slicing
- `tuple` — inmutable: unpacking, hashable, semántica de "no cambia"
- `dict` — mapa: `items()`, `get()`, dict comprehension
- `set` — unicidad: intersección, unión, diferencia
- Comprensiones: `[expr for x in iter if cond]`
- `enumerate()`, `zip()`, `sorted(key=)`, `any()`, `all()`

---

## BLOQUE T2-B — Módulos + HOF + Lambdas + Decoradores (45 min)

---

### [F-57] Módulos y paquetes en Python

@tipo: concepto-abstracto

# Organizar código en unidades reutilizables

## Módulo = un archivo `.py`

```python
# archivo: calculadora.py
def sumar(a: int, b: int) -> int:
    return a + b

def restar(a: int, b: int) -> int:
    return a - b
```

```python
# archivo: main.py
import calculadora             # importa todo el módulo
from calculadora import sumar  # importa solo una función

resultado = calculadora.restar(10, 3)   # 7
suma = sumar(5, 5)                      # 10
```

---

### [F-58] Estructura de proyecto Python

@tipo: concepto-abstracto

# La organización estándar del TP2

```
tp2-python-prompting/
├── src/
│   ├── __init__.py      ← hace que src/ sea un paquete
│   ├── hello.py
│   └── calculadora.py
├── tests/
│   ├── __init__.py
│   ├── test_hello.py
│   └── test_calculadora.py
└── requirements.txt
```

## ¿Qué es `__init__.py`?

- Archivo vacío (o con código de inicialización)
- Le dice a Python: "esta carpeta es un paquete"
- Permite `from src.calculadora import sumar`

---

### [F-59] requirements.txt

@tipo: codigo

# Declarar las dependencias del proyecto

```
# requirements.txt
pytest==8.1.0
ruff==0.4.5
```

## Instalar dependencias

```bash
# Instalar exactamente las versiones declaradas
pip install -r requirements.txt

# El devcontainer lo hace automáticamente con postCreateCommand
```

## Por qué fijar versiones

- `pytest==8.1.0` garantiza que CI y local usen la misma versión
- Sin versión fija (`pytest`) puede romper el build si la librería cambia
- Buena práctica para proyectos reproducibles

---

### [F-60] Funciones de orden superior — el concepto

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: One large bordo plain rectangle in the center. Two thin arrows point into it from the left: one from a small plain square, one from a small horizontal oval shape representing "functions as input". One thin arrow exits to the right pointing at another small square. White background. Flat minimal style. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Una función que recibe o devuelve funciones

## ¿Qué es una HOF (Higher-Order Function)?

- En Python, las funciones son **objetos de primera clase**
- Podés pasarlas como argumento a otra función
- Podés devolver una función como resultado
- Podés almacenarlas en una variable

```python
def aplicar(func, valor):
    return func(valor)

def duplicar(x: int) -> int:
    return x * 2

result = aplicar(duplicar, 5)   # 10
```

---

### [F-61] map() — transformar todos los elementos

@tipo: codigo

# Aplicar una función a cada elemento

```python
numeros = [1, 2, 3, 4, 5]

# map(función, iterable) → devuelve un iterator
al_cuadrado = list(map(lambda x: x ** 2, numeros))
# [1, 4, 9, 16, 25]

# Con función nombrada (más legible si la función es compleja)
def celsius_a_fahrenheit(c: float) -> float:
    return c * 9/5 + 32

temperaturas_c = [0, 20, 37, 100]
temperaturas_f = list(map(celsius_a_fahrenheit, temperaturas_c))
# [32.0, 68.0, 98.6, 212.0]
```

## map() vs comprensión de lista

```python
# Equivalentes:
cuadrados_a = list(map(lambda x: x**2, range(5)))
cuadrados_b = [x**2 for x in range(5)]
# Preferir comprensión cuando se puede — más legible en Python
```

---

### [F-62] filter() — seleccionar elementos

@tipo: codigo

# Conservar solo los elementos que cumplen la condición

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(función_predicado, iterable)
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4, 6, 8, 10]

# Con función nombrada
def es_aprobado(nota: int) -> bool:
    return nota >= 70

notas = [85, 65, 90, 55, 72, 68]
aprobados = list(filter(es_aprobado, notas))
# [85, 90, 72]
```

## filter() equivalente en comprensión

```python
# Equivalentes:
pares_a = list(filter(lambda x: x % 2 == 0, range(10)))
pares_b = [x for x in range(10) if x % 2 == 0]
# Preferir comprensión cuando la condición es simple
```

---

### [F-63] lambdas — funciones anónimas

@tipo: codigo

# Funciones pequeñas sin nombre

## Sintaxis

```python
# lambda parámetros: expresión
cuadrado = lambda x: x ** 2
print(cuadrado(5))   # 25

# Equivalente a:
def cuadrado(x: int) -> int:
    return x ** 2
```

## Cuándo usar lambda (y cuándo no)

```python
# ✅ En argumentos de funciones de orden superior (uso común)
alumnos.sort(key=lambda a: a["nota"])

# ✅ Funciones muy simples, uso único
identidad = lambda x: x

# ❌ No usar para funciones complejas de más de una expresión
# En ese caso: usar def
```

---

### [F-64] sorted() con key= — la HOF más práctica

@tipo: codigo

# Ordenar por cualquier criterio sin código extra

```python
palabras = ["banana", "manzana", "kiwi", "pera", "cereza"]

# Ordenar por longitud
por_longitud = sorted(palabras, key=len)
# ['kiwi', 'pera', 'banana', 'cereza', 'manzana']

# Ordenar por último carácter
por_ultimo = sorted(palabras, key=lambda p: p[-1])

# Ordenar por longitud descendente
por_longitud_desc = sorted(palabras, key=len, reverse=True)

# Ordenar por múltiples criterios (tuplas)
from operator import attrgetter
# Para objetos: sorted(lista, key=attrgetter('attr1', 'attr2'))
```

---

### [F-65] Decoradores — el concepto

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Three stacked plain rectangles vertically aligned on white background. The top rectangle is slightly wider and bordo colored. The middle rectangle is dark gray colored. The bottom rectangle is the same size as the top, bordo colored. Thin arrows pointing downward from top to middle to bottom. Flat design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Una función que envuelve otra función

## ¿Qué es un decorador?

- Patrón que permite **agregar comportamiento** a una función existente
- Sin modificar el código de esa función
- Sintaxis: `@nombre_decorador` sobre la función

```python
# El decorador más simple posible
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = func(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre: str) -> str:
    return f"Hola {nombre}"
```

---

### [F-66] @property — encapsulamiento pythónico

@tipo: codigo

# Getters sin el `getX()` de Java

```python
class Temperatura:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Temperatura en grados Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor: float) -> None:
        if valor < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self) -> float:
        """Convierte a Fahrenheit automáticamente."""
        return self._celsius * 9/5 + 32

t = Temperatura(100)
print(t.fahrenheit)   # 212.0  — acceso como atributo, no como método
```

---

### [F-67] @staticmethod y @classmethod

@tipo: codigo

# Métodos que no necesitan la instancia (o la clase)

## @staticmethod — función dentro de la clase sin self

```python
class Validador:
    @staticmethod
    def es_email_valido(email: str) -> bool:
        """Valida formato básico de email."""
        return "@" in email and "." in email.split("@")[-1]

# Se llama sin instanciar la clase
print(Validador.es_email_valido("user@example.com"))  # True
print(Validador.es_email_valido("inventado"))         # False
```

## Cuándo usar cada uno

| Decorador | Recibe | Cuándo usarlo |
|-----------|--------|---------------|
| Método normal | `self` (instancia) | Accede al estado del objeto |
| `@property` | `self` | Atributo calculado o con validación |
| `@staticmethod` | Nada | Función utilitaria relacionada con la clase |
| `@classmethod` | `cls` (la clase) | Constructores alternativos, acceso a clase |

---

### [F-68] @functools.wraps — decoradores correctos

@tipo: codigo

# Preservar la identidad de la función decorada

```python
import functools

def registrar_llamada(func):
    @functools.wraps(func)    # ← importantísimo
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__!r}")
        return func(*args, **kwargs)
    return wrapper

@registrar_llamada
def sumar(a: int, b: int) -> int:
    """Suma dos números enteros."""
    return a + b

# Sin @functools.wraps, esto daría "wrapper" y perdería el docstring
print(sumar.__name__)   # "sumar"   ✅
print(sumar.__doc__)    # "Suma dos números enteros."  ✅
```

---

### [F-69] HOF en el contexto del TP2

@tipo: concepto-abstracto

# Dónde vas a aplicar estas herramientas

## Ejercicios TP2 que usan HOF / lambdas

| Script | HOF relevante |
|--------|---------------|
| `colecciones.py` | `sorted(key=)`, `filter()`, `map()` |
| `funciones_ord.py` | `map()`, `filter()`, lambdas explícitas |
| `calculadora.py` | Funciones puras → `reduce()` en chain |

## Patrón recomendado

```python
# En lugar de 4 líneas de for loop:
notas_aprobadas = list(
    filter(lambda n: n >= 70, [85, 65, 90, 55, 72])
)
promedios = [sum(g) / len(g) for g in grupos if len(g) > 0]
```

---

### [F-70] Cierre T2-B

@tipo: cierre

# Módulos + HOF + Lambdas + Decoradores

## Lo que vimos

- Módulos y paquetes: `import`, `from...import`, `__init__.py`
- `requirements.txt` y reproducibilidad
- HOF: funciones de primera clase, `map()`, `filter()`
- `lambda`: funciones anónimas para casos simples
- `sorted(key=)`: la HOF más práctica del día a día
- `@property`, `@staticmethod`, `@functools.wraps`

## Preview Módulo III

Los decoradores se profundizan con `@app.route()` de Flask/FastAPI y con `@pytest.fixture` en Módulo II.

---

## BLOQUE T2-C — Type Hints Python 3.10+ (30 min)

---

### [F-71] ¿Qué son los type hints?

@tipo: concepto-abstracto

# Documentación ejecutable del contrato de una función

## Definición

- Anotaciones que indican qué tipo espera / devuelve una función
- **No son obligatorias** para Python (tipado dinámico)
- **Sí son obligatorias** en el TP2 (checkeadas por Ruff/Pylance)
- La idea: el código debe comunicar su intención claramente

```python
# Sin type hints — Python puede ejecutarlo pero no sabes qué espera
def procesar(datos, limite):
    return [x for x in datos if x > limite]

# Con type hints — contrato explícito
def procesar(datos: list[int], limite: int) -> list[int]:
    return [x for x in datos if x > limite]
```

---

### [F-72] PEP 484 + evolución reciente

@tipo: tabla

# Cronología de type hints en Python

| PEP / Versión | Año | Qué aportó |
|---------------|-----|------------|
| PEP 484 | 2015 / Python 3.5 | `typing` module: `List`, `Dict`, `Optional` |
| PEP 526 | 2016 / Python 3.6 | Anotaciones de variables: `x: int = 5` |
| PEP 585 | 2021 / Python 3.9 | `list[int]` en lugar de `typing.List[int]` |
| PEP 604 | 2021 / Python 3.10 | `X \| Y` en lugar de `Union[X, Y]` |
| PEP 673 | 2022 / Python 3.11 | `Self` type |
| Python 3.13 | 2024 | Pylance y Ruff validan inline |

## Hoy usamos

- Python 3.13 → usar la sintaxis moderna (`list[int]`, `X | Y`)
- NO necesitás `from typing import List, Dict, Optional` (obsoleto en 3.9+)

---

### [F-73] Tipos básicos y anotaciones de variable

@tipo: codigo

# Anotar parámetros, retorno y variables

## Anotaciones en funciones

```python
def calcular_promedio(notas: list[int]) -> float:
    """Calcula el promedio de una lista de notas."""
    return sum(notas) / len(notas)
```

## Anotaciones en variables

```python
nombre: str = "Ada"
edad: int = 25
activo: bool = True
notas: list[int] = [85, 72, 91]
```

## ¿Se chequean en runtime?

```python
# Python NO valida en runtime — solo Pylance/Ruff lo detectan
nombre: int = "Ada"
# Pylance: ⚠️  — Ruff puede marcar este error (si está configurado)
# Python: ejecuta sin error (dynamic typing)
```

---

### [F-74] Colecciones con tipos

@tipo: codigo

# generic types: list, dict, tuple, set

```python
# Python 3.9+: usar la sintaxis nativa directamente
nombres: list[str] = ["Ana", "Bob", "Carlos"]
edades: dict[str, int] = {"Ana": 22, "Bob": 30}
coordenada: tuple[float, float] = (3.5, -1.2)
lenguajes: set[str] = {"Python", "JavaScript"}

# Diccionario anidado
registro: dict[str, dict[str, int]] = {
    "Ana": {"nota_tp1": 85, "nota_tp2": 90}
}
```

## En funciones del TP2

```python
def agrupar_por_aprobacion(
    notas: dict[str, int]
) -> dict[str, list[str]]:
    """Agrupa alumnos en 'aprobados' y 'desaprobados'."""
    ...
```

---

### [F-75] X | None — la forma moderna de Optional

@tipo: codigo

# Python 3.10+ reemplaza Optional[X] con X | None

## Antes (Python 3.8 / 3.9)

```python
from typing import Optional

def buscar_alumno(legajo: int) -> Optional[str]:
    ...
```

## Ahora (Python 3.10+)

```python
def buscar_alumno(legajo: int) -> str | None:
    """Busca el nombre del alumno por legajo.

    Returns:
        Nombre del alumno si existe, None si no se encuentra.
    """
    alumnos = {1234: "Ana García", 5678: "Bob Rodríguez"}
    return alumnos.get(legajo)
```

---

### [F-76] Union y Any

@tipo: codigo

# Cuando el tipo puede ser más de uno

## Union (Python 3.10+: X | Y)

```python
# Un campo que puede ser int o str
def procesar_id(id: int | str) -> str:
    """Procesa un identificador que puede ser numérico o texto."""
    return str(id).zfill(5)

print(procesar_id(123))      # "00123"
print(procesar_id("AB001"))  # "AB001"
```

## Any — el tipo "no me importa el tipo"

```python
from typing import Any

def almacenar(clave: str, valor: Any) -> None:
    """Almacena cualquier valor con una clave texto."""
    ...
```

> **Regla de uso:** `Any` es el "último recurso" — si podés ser más específico, sé más específico.

---

### [F-77] Anotaciones de retorno complejas

@tipo: codigo

# Retornos de funciones con tipos compuestos

## Retorno de múltiples valores (tuple)

```python
def dividir(a: int, b: int) -> tuple[int, int]:
    """Devuelve cociente y resto."""
    return a // b, a % b

cociente, resto = dividir(17, 5)   # (3, 2)
```

## Retorno de colección tipada

```python
def filtrar_aprobados(notas: dict[str, int]) -> list[str]:
    """Retorna nombres de alumnos con nota >= 70."""
    return [nombre for nombre, nota in notas.items() if nota >= 70]
```

## Funciones sin retorno

```python
def registrar_error(mensaje: str) -> None:
    """Registra un mensaje de error en stdout."""
    print(f"[ERROR] {mensaje}")
```

---

### [F-78] Callable — tipar funciones como argumento

@tipo: codigo

# Anotar cuando el argumento ES una función

```python
from collections.abc import Callable

def aplicar_a_todos(
    lista: list[int],
    func: Callable[[int], int]
) -> list[int]:
    """Aplica func a cada elemento de lista."""
    return [func(x) for x in lista]

# Uso
duplicados = aplicar_a_todos([1, 2, 3], lambda x: x * 2)
# [2, 4, 6]
```

## Lectura de Callable[[int], int]

- `Callable[[parámetros], retorno]`
- `Callable[[int], int]`: función que recibe un int y devuelve un int

---

### [F-79] Ruff + type hints en TP2

@tipo: concepto-abstracto

# El pipeline de calidad para el TP2

## Cadena de verificación automática

```bash
# Paso 1: Ruff identifica violaciones de estilo + type hints (si están en reglas)
ruff check src/

# Paso 2: Pylance en VS Code muestra errores de tipo en tiempo real

# Paso 3: pytest ejecuta los tests funcionales
pytest tests/ -v

# Paso 4: CI en GitHub Actions corre los 3 pasos en cada push
```

## Lo que el CI del TP2 verifica

1. `ruff check .` — sin errores de linter
2. `pytest tests/ -v` — todos los tests deben pasar

---

### [F-80] Cierre T2-C

@tipo: cierre

# Type hints — resumen ejecutivo

## Cuatro reglas para el TP2

1. **Todos los parámetros** de funciones públicas deben tener tipo
2. **Todos los retornos** deben tener tipo (incluyendo `-> None`)
3. Usar sintaxis **Python 3.10+**: `list[int]`, `str | None`, `X | Y`
4. **Not usar** `from typing import List, Dict` (obsoleto en 3.9+)

## Cheat sheet rápida

```python
nombre: str                   # primitivo
notas: list[int]              # lista tipada
mapa: dict[str, float]        # dict tipado
coordenada: tuple[int, int]   # tupla fija
resultado: int | None         # puede ser None
func: Callable[[int], int]    # función como argumento
```

---

## BLOQUE T2-D — Prompting para Debugging (20 min)

---

### [F-81] Mostrar el traceback a Copilot

@tipo: demo

# El traceback es tu mejor prompt de partida

## Anatomía de un traceback de Python

```
Traceback (most recent call last):
  File "src/calculadora.py", line 12, in main
    resultado = dividir(10, 0)
  File "src/calculadora.py", line 6, in dividir
    return a / b
ZeroDivisionError: division by zero
```

## Prompt efectivo

```
Role: Eres un tutor de Python 3.13 experto en debugging.
Contexto: Tengo esta función en calculadora.py:

def dividir(a: int, b: int) -> float:
    return a / b

Error: ZeroDivisionError cuando b=0.
Tarea: Explícame línea a línea por qué ocurre y cómo prevenirlo 
con type hints y guard clause.
Restricción: No uses try/except todavía, solo validación explícita.
```

---

### [F-82] Prompt para explicación línea a línea

@tipo: demo

# Entender el código IA-asistido antes de entregarlo

## El patrón "Explain before use"

```
Role: Eres un profesor de Python paciente y detallista.
Contexto: GitHub Copilot me generó este código para el ejercicio de Fibonacci:

def fibonacci(n: int) -> list[int]:
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie[:n]

Tarea: Explicame cada línea con sus propias palabras, 
sin asumir que entiendo la indexación negativa.
Restricción: Usar ejemplos concretos con n=5.
Ejemplo de lo que busco: "La línea 2 crea..."
```

---

### [F-83] Prompt para refactoring + type hints

@tipo: demo

# Mejorar código existente con IA

## El patrón "Refactor with constraints"

```
Role: Eres un revisor senior de código Python siguiendo PEP 8 y PEP 484.
Contexto: Tengo este script del TP2 que funciona pero tiene issues:

def temp_convert(t, unit):
    if unit == 'C':
        return t * 9/5 + 32
    return (t - 32) * 5/9

Tarea: Refactorizá la función para que:
1. Tenga type hints completos (incluida anotación de retorno)
2. Tenga docstring con Args/Returns
3. Use nombres descriptivos en snake_case
4. Agregue validación del parámetro unit
Restricción: No cambiar la lógica, solo mejorar forma y robustez.
```

---

### [F-84] Cierre Módulo I — Preview Módulo II

@tipo: cierre
@imagen: background
@prompt-imagen: Clean white background with large bordo horizontal rectangle in center. Below the rectangle, three small flat icons in a triangle arrangement: top icon is a small checkmark badge, bottom-left is a small red circle, bottom-right is a small green filled circle. Thin bordo arrows connecting them clockwise. Flat design. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Módulo I completado — ¿Qué sigue?

## Lo que construiste en este módulo

- Entorno ágil: Git + Codespaces + CI
- Python 3.13: tipos, control, funciones, colecciones, HOF, type hints
- Herramientas: Ruff, Pylance, GitHub Copilot + PROMPTS.md

## Connexión Módulo I → Módulo II

Los **tests del TP2** que corriste para aprobar son exactamente el patrón **Red → Green → Refactor** del TDD. En el Módulo II vamos a aprender a **escribir esos tests**.

## TP2 — Recordatorio final

- **Deadline:** Semana 4, lunes 23:59
- **Link:** `classroom.github.com/a/X4xiTEDQ`
- **Mínimo para aprobar:** 5/7 tests en verde + 7 commits + 3 prompts en PROMPTS.md
