# Minuta de Clase — Módulo I: Diseño Ágil + Python
## Tema 01 | Semanas 2–3 | 4 sesiones | 12 hs totales

> **Generado por:** Dr. Roberto ✍️ (class-writer)  
> **Fecha:** 2026-03-25  
> **Para:** Matías Gel — Docente  
> **TP asociado:** TP2 — Python + Prompting con Autograding (`classroom.github.com/a/X4xiTEDQ`)  
> **Deadline TP2:** Semana 4, lunes 23:59

---

## Checklist pre-clase

- [ ] DevContainer del TP2 verificado (push a repo plantilla, abrir en Codespaces, confirmar que pytest corre)
- [ ] Tener `python3.13` instalado en equipo docente para la demo del REPL
- [ ] Filminas F-00 a F-84 cargadas en presentación
- [ ] Link TP2 accesible: `classroom.github.com/a/X4xiTEDQ`
- [ ] GitLens instalado y mostrando historial en VS Code (demo F-09)

---

## SESIÓN T1 — Semana 2, Teoría (180 min)

> **Estructura de bloques:** T1-A (45') + T1-B (45') + T1-C (30') + T1-D (20') = **140' de clase** + **40' de pausas/transiciones** distribuidas entre bloques
>
> **Precondición para el alumno:** Han completado el Tema 00 (setup GitHub, Codespaces funcional, TP1 entregado).

---

### BLOQUE T1-A — El Modelo Ágil + IDEs (0:00 – 0:45)

**Objetivo:** Que los alumnos entiendan el ciclo ágil como marco conceptual para todo lo que sigue en el curso, y que tengan claro el entorno de desarrollo (VS Code + Codespaces) como herramienta de trabajo.

#### Plan de tiempos (45 min)

| Min | Actividad | Filminas |
|-----|-----------|---------|
| 0–3 | Bienvenida semana 2, agenda del módulo (leer F-01) | F-00, F-01 |
| 3–10 | ¿Qué es el modelo ágil? — presentación + pregunta inicial | F-02, F-03 |
| 10–18 | Cascada vs. Ágil — tabla comparativa colectiva | F-04 |
| 18–25 | El ciclo iterativo — conectar con TP2 ("el cliente son los tests") | F-05 |
| 25–32 | Demo VS Code en Codespaces: abrir TP2, mostrar extensiones instaladas | F-06, F-07 |
| 32–38 | Ruff y GitLens — demo en vivo (abrir archivo con errores PEP 8, mostrar marcas) | F-08, F-09 |
| 38–42 | DevContainer — leer el JSON, relacionar con reproducibilidad | F-10, F-11 |
| 42–45 | Pregunta socrática F-12 + pausa activa (¿el TP2 es más ágil o cascada?) | F-12 |

#### Notas docentes

- **Apertura:** Preguntar quién tiene el Codespace del TP2 abierto ya. Los que no → abrir durante la presentación de F-10.
- **Demo F-07 (Pylance):** abrir `src/hello.py` del TP2 vacío, escribir `sumar("hola", 3)` y mostrar el subrayado rojo antes de ejecutar. Enfatizar: "el error aparece sin correr el programa".
- **Demo F-08 (Ruff):** introducir intencionalmente un error de espaciado (`x=1+2` sin espacios), guardar, mostrar que Ruff lo marca. Luego `ruff check --fix` desde terminal.
- **Trampa habitual:** Los alumnos confunden "ágil" con "sin planificación". Aclarar explícitamente: ágil tiene iteraciones bien planificadas, simplemente son más cortas.
- **Conexión con plan mínimo:** El modelo ágil es el primer ítem del plan mínimo institucional — dejar constancia en la filmina o verbalizarlo.

#### Transición a T1-B

> "Ahora que tenemos el entorno y el marco de trabajo, pasemos al lenguaje. ¿Qué tipo es `True + True` en Python? Lo vamos a ver en un segundo."

---

### BLOQUE T1-B — Python 3.13 Fundamentos (0:50 – 1:35)

**Objetivo:** Que los alumnos puedan escribir variables, operaciones básicas y strings en Python, con las novedades de versión 3.13 que son pedagógicamente relevantes.

#### Plan de tiempos (45 min)

| Min | Actividad | Filminas |
|-----|-----------|---------|
| 0–3 | Transición + por qué Python en 2026 | F-13 |
| 3–8 | Tipos primitivos — tabla + preguntas (¿cuál es el tipo de `3.0`?) | F-14 |
| 8–14 | Asignación + operadores — escribir en REPL junto con la clase | F-15 |
| 14–20 | **Demo REPL 3.13** — mostrar historial, multilínea, colores | F-16 |
| 20–24 | Mensajes error contextuales 3.13 — provocar error intencionalmente | F-17 |
| 24–30 | Strings: inmutabilidad + métodos + f-strings | F-18, F-19, F-20 |
| 30–35 | Variables y referencias: el ejercicio de la lista compartida | F-21 |
| 35–40 | None + Boolean peculiaridades, conversiones | F-22, F-23 |
| 40–45 | Tabla str vs list + operadores `is` / `in` | F-24, F-25 |
| 45 | Cierre T1-B — preguntas rápidas | F-26 |

#### Notas docentes

- **Demo REPL 3.13 (F-16):** Abrir terminal en Codespace, escribir `python3`. La demo debe mostrar:
  1. Pegar un bloque de 3 líneas (function definition) sin errores
  2. Mostrar el historial con flecha arriba
  3. Provocar un error de atributo: `"hola".upper_case()` → aparece "Did you mean: 'upper'?"
  
- **Ejercicio live (F-21 — referencias):**
  ```python
  a = [1, 2, 3]
  b = a
  b.append(99)
  print(a)  # ← preguntar qué imprime ANTES de ejecutar
  ```
  Pausar y pedir predicción. Este ejercicio es recurrente en TP2 cuando trabajan con listas.

- **Trampa habitual:** `True + True == 2`. Mostrarlo. Los alumnos se sorprenden. Conectar con "en Python, bool es subclase de int".

- **No entrar en profundidad:** Hashing, __hash__, intern de strings — fuera de scope T1.

#### Transición a T1-C

> "Tenemos los tipos y las variables. Hora de controlar el flujo — if, for, while, y las funciones que vamos a usar en el TP2."

---

### BLOQUE T1-C — Control de flujo + Funciones (1:40 – 2:10)

**Objetivo:** Los alumnos escriben funciones Python correctas con docstrings, type hints, condicionales y loops. Es el bloque más práctico de T1 — cada filmina debe tener código en pantalla.

#### Plan de tiempos (30 min)

| Min | Actividad | Filminas |
|-----|-----------|---------|
| 0–4 | if/elif/else — función `clasificar_nota` en vivo | F-27 |
| 4–7 | for sobre secuencias — live coding frutas + rango | F-28 |
| 7–11 | while + break + continue — el ejemplo de intentos de login | F-29 |
| 11–15 | match (Python 3.10+) — función `describir_http` | F-30 |
| 15–20 | def + return + docstrings — anatomía completa de una función | F-31 |
| 20–24 | Parámetros posicionales, keyword, default | F-32 |
| 24–27 | *args y **kwargs — uso mínimo | F-33 |
| 27–30 | Cierre + pregunta socrática sobre `es_primo()` | F-35, F-36 |

#### Notas docentes

- **Codear en vivo (F-27–F-31):** Cada ejemplo en filmina debe replicarse en terminal. Dejar que los alumnos dicten las variaciones.
- **match (F-30):** Aclarar que es Python 3.10+ — el devcontainer usa 3.13 así que está disponible. No requiere `import`. El caso `_` es el "default".
- **Docstrings (F-31):** Usar el formato de Google docstrings (Args / Returns / Raises). Pylance puede mostrar el docstring al hover — demostrarlo.
- **Scope (F-34):** Mencionar brevemente, sin profundizar. El ejercicio de `es_primo` del TP2 es 100% scope local — no necesitan `global`.
- **Opional por tiempo:** Si el tiempo aprieta, F-33 (*args/**kwargs) puede mostrarse rápido como "lo que necesitan saber" sin demo.

#### Transición a T1-D

> "Tenemos funciones. Ahora necesitamos asegurarnos de que el código sea legible — y para eso tenemos Ruff y PEP 8. Último bloque de T1."

---

### BLOQUE T1-D — Ruff + PEP 8 + Preview TP2 (2:15 – 2:35)

**Objetivo:** Los alumnos activan Ruff en su Codespace y entienden que la calidad del código es parte de la nota del TP2. Preview del repositorio.

#### Plan de tiempos (20 min)

| Min | Actividad | Filminas |
|-----|-----------|---------|
| 0–4 | ¿Qué es PEP 8? — los 5 puntos para el TP2 | F-37 |
| 4–9 | Código autodocumentado — antes/después de refactoring | F-38 |
| 9–12 | Convenciones de nombres — tabla de referencia rápida | F-39 |
| 12–16 | Demo Ruff en vivo — código con errores, ruff --fix | F-40 |
| 16–20 | Preview estructura TP2 + recordatorio deadline + link | F-41, F-42 |

#### Notas docentes

- **Demo Ruff (F-40):** Abrir el Codespace del TP2, crear un archivo de prueba con errores PEP 8 deliberados, correr `ruff check`. Mostrar que CI corre `ruff check .` automáticamente.
- **Preview TP2 (F-41):** Proyectar la estructura del repo (sin abrir cada archivo). La descripción detallada va a la sesión P1.
- **Mensaje clave:** "Ruff no es una molestia — es tu mejor autocontrol antes del commit".
- **Cierre de T1:** Resumen rápido de los 4 bloques (F-42). Dejar 5 min de Q&A antes de finalizar la sesión.

---

## SESIÓN P1 — Semana 2, Práctica (180 min)

> **Estructura:** P1-A (50') + P1-B (50') + P1-C (40') + P1-D (20') = 160' + 20' transiciones  
> **Modalidad:** Laboratorio hands-on en Codespaces con GitHub Copilot habilitado  
> **Precondición:** Todos los alumnos con Codespace del TP2 abierto al inicio

---

### BLOQUE P1-A — Ejercicios guiados Python en Codespaces (0:00 – 0:50)

**Objetivo:** Los alumnos ejecutan los primeros scripts Python guiados en Codespaces, replicando lo del docente en tiempo real.

#### Plan de tiempos (50 min)

| Min | Actividad | Notas |
|-----|-----------|-------|
| 0–5 | Check inicial: todos tienen Codespace abierto y `python --version` funcionando | Si alguien no puede → acceso a Codespaces desde GitHub repo del TP2 |
| 5–15 | **Ejercicio 1:** Calculadora simple — función `calcular(a, b, operacion)` con match | Docente codea en pantalla, alumnos replican |
| 15–25 | **Ejercicio 2:** Conversor de temperatura Celsius ↔ Fahrenheit con type hints | Incluir docstring completa + comprobación con assert |
| 25–35 | **Ejercicio 3:** Generador de Fibonacci — función iterativa con comprensión | Mostrar diferencia entre versión imperativa y la de lista en una línea |
| 35–45 | **Ejercicio 4:** Clasificador de números — `par/impar/primo` con match | Introducir validación de entrada |
| 45–50 | Review colectivo: ¿cuáles fueron los errores más comunes? Mostrar traceback de algún alumno | Errores comunes esperados: indentación, tipo de dato |

#### Código de referencia para el docente

```python
# Ejercicio 1 — calculadora.py
def calcular(a: float, b: float, operacion: str) -> float | None:
    """Realiza una operación aritmética básica.

    Args:
        a: Primer operando.
        b: Segundo operando.
        operacion: Una de: 'suma', 'resta', 'mult', 'div'.

    Returns:
        Resultado de la operación, o None si la operación es inválida.
    """
    match operacion:
        case "suma":
            return a + b
        case "resta":
            return a - b
        case "mult":
            return a * b
        case "div":
            if b == 0:
                return None
            return a / b
        case _:
            return None

# Ejercicio 2 — temperatura.py
def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte temperatura de Celsius a Fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """Convierte temperatura de Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9

# Ejercicio 3 — fibonacci.py
def fibonacci(n: int) -> list[int]:
    """Devuelve los primeros n números de la serie de Fibonacci."""
    if n <= 0:
        return []
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie[:n]

# Ejercicio 4 — clasificador.py
def es_primo(n: int) -> bool:
    """Determina si n es primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def clasificar(n: int) -> str:
    """Clasifica un número como par, impar o primo."""
    if es_primo(n):
        return "primo"
    return "par" if n % 2 == 0 else "impar"
```

#### Notas docentes

- **No avanzar al siguiente ejercicio** hasta que al menos el 80% de los alumnos haya terminado el actual.
- **Error esperado más frecuente:** `IndentationError` al pegar código. Mostrar cómo Ruff lo detecta.
- **Enfatizar:** `-> float | None` es la sintaxis moderna. Si alguien usa `Optional[float]` de typing, no está mal, pero aclarar que en Python 3.10+ ya no es necesario.

---

### BLOQUE P1-B — Prompting para Python (0:55 – 1:45)

**Objetivo:** Los alumnos internalizan el patrón Role+Contexto+Tarea+Restricciones+Ejemplo y lo usan para pedir código, entenderlo, modificarlo y documentarlo en `PROMPTS.md`.

#### Plan de tiempos (50 min)

| Min | Actividad | Notas |
|-----|-----------|-------|
| 0–5 | Introducción: ¿Copilot reemplaza aprender? — no, pero cambia cómo aprendemos | Citar Fan et al. (2025): AI pair programming reduce ansiedad |
| 5–15 | Demo ChatGPT: prompt genérico vs. prompt con patrón RCTAE | Prompt malo → respuesta vaga; prompt bueno → respuesta específica |
| 15–30 | Demo Copilot: completar `fibonacci.py` con Copilot → entender línea a línea | Pausar ANTES de aceptar la sugerencia, preguntar "¿qué hace esta línea?" |
| 30–40 | Ejercicio individual: escribir un script con IA → entenderlo → modificar un parámetro → documentar en PROMPTS.md | Mínimo: 1 prompt completo anotado |
| 40–50 | Peer review: intercambiar PROMPTS.md con el compañero de al lado — ¿es reproducible el prompt? | Checklist: ¿tiene role? ¿contexto? ¿restricción? ¿ejemplo? |

#### Patrón RCTAE para documentar en PROMPTS.md

```markdown
## Prompt 01 — [Nombre del ejercicio]

**Role:** Eres un tutor senior de Python 3.13 experto en clean code.  
**Contexto:** Estoy implementando `src/fibonacci.py` para el TP2. 
La función debe devolver los primeros n números de la serie.  
**Tarea:** Escribí la función `fibonacci(n: int) -> list[int]` en Python 3.13 
con docstring formato Google y type hints completos.  
**Restricciones:** Sin recursión, sin numpy. Solo listas y bucle while.  
**Ejemplo de uso esperado:** `fibonacci(5)` debe retornar `[0, 1, 1, 2, 3]`.

### Código generado

[pegar código aquí]

### Comprensión línea a línea

- Línea 1: `serie = [0, 1]` → inicializa la serie con los dos primeros términos
- Línea 2: `while len(serie) < n:` → repite mientras la lista no tenga n elementos
- Línea 3: `serie.append(serie[-1] + serie[-2])` → suma los dos últimos y agrega

### Modificación aplicada

Cambié `while len(serie) < n` por un early return cuando `n <= 0` porque...
```

#### Notas docentes

- **Anti-patrón a marcar:** Copiar código sin el bloque de comprensión. Si el PROMPTS.md no tiene la sección "Comprensión línea a línea", el prompt **no está completo** según la rúbrica.
- **Referencia a Alves & Cipriano (2024):** Los estudiantes de primer año tienden a pedir código completo y usarlo sin comprenderlo. El PROMPTS.md es el mecanismo que hace visible ese problema.
- **Si un alumno pregunta** "¿por qué no usar Copilot inline directamente?": el objetivo es que el alumno gestione el proceso, no que Copilot lo haga solo.

---

### BLOQUE P1-C — GitHub Classroom TP2 (1:50 – 2:30)

**Objetivo:** Los alumnos aceptan el TP2 en GitHub Classroom, exploran la estructura del repo, entienden los tests de pytest, y completan el primer script mínimo con CI en verde.

#### Plan de tiempos (40 min)

| Min | Actividad | Notas |
|-----|-----------|-------|
| 0–5 | Aceptar TP2 en Classroom (link en slide F-41) | Mostrar el flow: aceptar → repo personal creado → abrir en Codespace |
| 5–12 | Explorar estructura: `src/`, `tests/`, `requirements.txt`, `.github/workflows/` | Abrir cada carpeta, leer el archivo CI: ¿qué hace `ruff check .`? ¿qué hace `pytest`? |
| 12–20 | **Leer `tests/test_hello.py`** antes de escribir código | Crucial: ¿qué espera el test? ¿qué devuelve la función que debo implementar? |
| 20–30 | Implementar `src/hello.py` — función `saludar(nombre: str) -> str` con docstring | Push → ver CI correr → primer check verde |
| 30–38 | Verificar el CI en GitHub Actions — mostrar la pestaña "Actions" del repo | Leer los logs: ¿qué paso falló/pasó? |
| 38–40 | Q&A dudas sobre estructura TP2 | Dudas más comunes: rutas de importación, cómo ver los tests que fallan |

#### Código de referencia: hello.py

```python
# src/hello.py

def saludar(nombre: str) -> str:
    """Saluda al usuario por su nombre.

    Args:
        nombre: El nombre del usuario a saludar.

    Returns:
        Un string de saludo en español.
    """
    return f"Hola, {nombre}!"
```

#### Notas docentes

- **El CI es la fuente de verdad.** Si la pantalla local dice que funciona pero el CI falla, el CI tiene razón. Mostrar esto desde el principio.
- **Test-first mindset:** Antes de escribir cada función, preguntar: "¿qué espera el test?". Este es el germen del TDD que se profundiza en Módulo II.
- **Si el CI falla por Ruff:** Mostrar cómo leer el error de linter en los logs de CI. Corrección local con `ruff check --fix` + push.

---

### BLOQUE P1-D — Revisión colectiva de commits (2:35 – 2:55)

**Objetivo:** Los alumnos aprenden a escribir mensajes de commit descriptivos y ven el historial en pantalla del docente.

#### Plan de tiempos (20 min)

| Min | Actividad | Notas |
|-----|-----------|-------|
| 0–5 | `git log --oneline` en pantalla del docente — repo con commits buenos vs. malos | Mostrar: "fix", "update", "asdf" vs. "feat(hello): implement saludar() with docstring" |
| 5–12 | Convenciones de mensajes — conventional commits básico: `feat:`, `fix:`, `docs:`, `test:` | No es obligatorio usar todos los prefijos, pero sí mensajes descriptivos |
| 12–17 | Ejercicio: cada alumno hace al menos 2 commits con mensajes descriptivos en su TP2 | Los 20% del puntaje de commits son acumulativos — mejor empezar ahora |
| 17–20 | Dudas frecuentes TP2: rutas, imports, autograding — aclarar antes de la semana siguiente | Registrar las dudas más frecuentes para abrir P2 respondiendo las mismas |

#### Notas docentes

- **Énfasis:** Los 7 commits requeridos deben ser **atómicos** — cada uno cambia una sola cosa con propósito claro. No sirve un commit con 7 archivos modificados.
- **GitLens:** Mostrar en VS Code cómo GitLens muestra el mensaje de commit en el margen del editor.

---

## SESIÓN T2 — Semana 3, Teoría (180 min)

> **Estructura:** T2-A (45') + T2-B (45') + T2-C (30') + T2-D (20') = 140' + 40' transiciones  
> **Precondición:** Los alumnos ya tienen el TP2 aceptado y al menos 2–3 scripts completados.

---

### BLOQUE T2-A — Colecciones Python (0:00 – 0:45)

**Objetivo:** Los alumnos dominan las cuatro colecciones Python y las comprensiones para usarlas en los ejercicios más complejos del TP2.

#### Plan de tiempos (45 min)

| Min | Actividad | Filminas |
|-----|-----------|---------|
| 0–3 | Apertura semana 3 — revisar dónde está el grupo con el TP2 (encuesta rápida: ¿cuántos tienen CI verde?) | F-43 |
| 3–8 | Tabla comparativa 4 colecciones — cuándo usar cada una | F-44 |
| 8–15 | list — live coding: operaciones básicas, slicing, sort | F-45 |
| 15–20 | tuple — casos de uso, unpacking, como clave de dict | F-46 |
| 20–28 | dict — operaciones, `.items()`, `.get()` con default | F-47 |
| 28–33 | set — unicidad, operaciones de conjuntos | F-48 |
| 33–38 | Comprensiones — patrón base + filtro + dict + set | F-49, F-50 |
| 38–42 | enumerate() y zip() | F-51 |
| 42–45 | sorted(key=) + builtins de reducción (sum, min, max, any, all) | F-52, F-53 |

#### Notas docentes

- **Demo live comprensiones (F-49):** Mostrar en REPL la evolución de for loop → comprensión. Preguntar antes: "¿cómo harían esto sin comprensión?".
- **Conexión con TP2:** `colecciones.py` usa list comprehensions, dict, y operaciones de set. Conectar explícitamente con los ejercicios.
- **zip() (F-51):** Mostrar que `zip()` devuelve un iterator (no una lista) — hay que envolverlo en `list()` para verlo.
- **Slicing avanzado (F-54):** Si hay tiempo, cubrir. Si no, dejarlo como lectura para guia-estudio.

#### Transición a T2-B

> "Ya tenemos las colecciones. Ahora empezamos a combinarlas con algo más expresivo: funciones de orden superior. ¿Alguien sabe qué hace `map()`?"

---

### BLOQUE T2-B — Módulos + HOF + Lambdas + Decoradores (0:50 – 1:35)

**Objetivo:** Los alumnos usan módulos correctamente (estructura del TP2) y aplican map/filter/lambda a sus ejercicios. Los decoradores se introducen como concepto, no como habilidad a evaluar en TP2.

#### Plan de tiempos (45 min)

| Min | Actividad | Filminas |
|-----|-----------|---------|
| 0–5 | Módulos: import, from...import — demo desde la estructura del TP2 | F-57, F-58 |
| 5–8 | requirements.txt — cómo declarar dependencias | F-59 |
| 8–12 | HOF — el concepto: funciones como objetos de primera clase | F-60 |
| 12–18 | map() — demo + comparación con comprensión | F-61 |
| 18–24 | filter() — demo + comparación con comprensión | F-62 |
| 24–28 | lambda — sintaxis, cuándo sí y cuándo no | F-63 |
| 28–32 | sorted(key=lambda) — el caso de uso más práctico | F-64 |
| 32–37 | Decoradores: el concepto + @property demo | F-65, F-66 |
| 37–40 | @staticmethod, @functools.wraps — mención rápida | F-67, F-68 |
| 40–45 | Conexión con TP2: dónde aplicar HOF | F-69, F-70 |

#### Notas docentes

- **Demo HOF (F-60–F-62):** Comparar siempre con la alternativa de for loop. La pregunta es "¿cuándo es más legible `map()` vs. comprensión?". Respuesta pythónica: preferir comprensión cuando se puede.
- **Decoradores (F-65–F-68):** Cubrir como concepto. En TP2 no se implementan decoradores propios. `@property` aparece si algún alumno implementa clases (no requerido en TP2).
- **@functools.wraps (F-68):** Mencionar brevemente. Su importancia se ve más en Módulo III/IV cuando los alumnos implementen middlewares.

---

### BLOQUE T2-C — Type Hints Python 3.10+ (1:40 – 2:10)

**Objetivo:** Los alumnos pueden anotar correctamente cualquier función del TP2 con type hints modernos y verificarlos con Ruff/Pylance.

#### Plan de tiempos (30 min)

| Min | Actividad | Filminas |
|-----|-----------|---------|
| 0–4 | ¿Qué son type hints? — contrato explícito vs. tipado dinámico | F-71 |
| 4–8 | Cronología PEP 484 → Python 3.10+ — sintaxis moderna vs. obsoleta | F-72 |
| 8–12 | Tipos básicos + anotaciones de variable | F-73 |
| 12–16 | Colecciones tipadas: list[int], dict[str, float], tuple[float, float] | F-74 |
| 16–20 | X | None (Optional moderno) + Union | F-75, F-76 |
| 20–24 | Any y Callable — cuándo usar cada uno | F-77, F-78 |
| 24–28 | Ruff + Pylance verificando type hints en TP2 | F-79 |
| 28–30 | Cierre: cheat sheet resumen | F-80 |

#### Notas docentes

- **Énfasis crítico (F-72):** `from typing import List, Dict` es Python 3.8. En 3.9+ usar `list[int]`, `dict[str, int]`. Ruff puede marcarlo como deprecado. Aclarar que los tests del TP2 pueden usar ambas sintaxis pero nosotros usamos la moderna.
- **Demo en vivo:** Abrir `src/hello.py` del TP2, agregar type hint incorrecto, ver Pylance marcar en rojo. Herramienta = feedback inmediato.
- **Callable (F-78):** Introducir si llegan con tiempo. Si no, dejar como referencia en guia-estudio.

---

### BLOQUE T2-D — Prompting para Debugging (2:15 – 2:35)

**Objetivo:** Los alumnos tienen patrones concretos para usar IA en debugging y refactoring, y saben que deben documentarlos en PROMPTS.md.

#### Plan de tiempos (20 min)

| Min | Actividad | Filminas |
|-----|-----------|---------|
| 0–5 | El traceback como punto de partida — anatomía del error Python | F-81 |
| 5–10 | Demo: llevar un traceback a Copilot/ChatGPT con el patrón RCTAE | F-82 |
| 10–15 | Demo refactoring con IA: función sin type hints → con prompts RCTAE | F-83 |
| 15–20 | Cierre del Módulo I + preview Módulo II + recordatorio final TP2 | F-84 |

#### Notas docentes

- **Demo debugging (F-81):** Provocar intencionalmente un ZeroDivisionError en el TP2, mostrar el traceback completo, luego construir el prompt RCTAE en vivo.
- **Mensaje final TP2 (F-84):** Recordar deadline explícitamente. Proyectar el link. Verificar que todos lo tienen en favoritos.

---

## SESIÓN P2 — Semana 3, Práctica (180 min)

> **Estructura:** P2-A (60') + P2-B (40') + P2-C (40') + P2-D (20') = 160' + 20' transiciones  
> **Precondición:** Alumnos con el Codespace del TP2 abierto y mínimo 3/7 scripts completados.

---

### BLOQUE P2-A — Taller TP2 intensivo (0:00 – 1:00)

**Objetivo:** Los alumnos alcanzan al menos 5/7 ejercicios con CI verde al finalizar el bloque.

#### Plan de tiempos (60 min)

| Min | Actividad | Notas |
|-----|-----------|-------|
| 0–5 | Check inicial: proyectar mapa de progreso (encuesta anónima: ¿cuántos scripts tienen?) | Pizarrón o Mentimeter |
| 5–50 | **Taller silencioso** — trabajo individual/pares | Docente circula, resuelve bloqueos individuales |
| 50–60 | Review colectivo de bloqueos más comunes | Elegir 2–3 casos que se repetían para mostrar en pantalla |

#### Scripts del TP2 — descripción y conexión con T1/T2

| Script | Conceptos de T1/T2 aplicados | Tips |
|--------|------------------------------|------|
| `hello.py` | f-strings, type hints básicos | El más sencillo — usarlo de warmup |
| `calculadora.py` | match, funciones, type hints | Usar `float | None` para división por cero |
| `temperatura.py` | funciones puras, type hints, docstring | Buena práctica para @staticmethod como alternativa |
| `fibonacci.py` | while, list, slicing | `serie[:n]` para truncar |
| `colecciones.py` | list, dict, set, comprensiones | Los tests esperan tipos específicos |
| `funciones_ord.py` | map(), filter(), sorted(key=), lambda | Comparar con comprensiones equivalentes |
| `type_hints.py` | Anotaciones, `X \| None`, `Callable` | Puede ser un archivo de funciones con diversas anotaciones |

#### Notas docentes

- **Copilot habilitado pero PROMPTS.md obligatorio.** Si un alumno usa Copilot, el PROMPTS.md debe registrar el prompt.
- **Frecuente: error de imports.** Cuando `src/colecciones.py` no puede importarse desde tests: verificar `src/__init__.py` existe.
- **CI rojo por Ruff:** Lo más común es `E501` (línea muy larga) o `F401` (import sin usar). Mostrar cómo leer el log de CI.

---

### BLOQUE P2-B — PROMPTS.md obligatorio (1:05 – 1:45)

**Objetivo:** Los alumnos tienen al menos 3 prompts completos, con la sección de comprensión obligatoria, antes de salir de esta sesión.

#### Plan de tiempos (40 min)

| Min | Actividad | Notas |
|-----|-----------|-------|
| 0–5 | Leer la rúbrica del PROMPTS.md en voz alta — qué necesita cada prompt | Proyectar la sección de evaluación del TP2 |
| 5–25 | Trabajo individual: completar o mejorar PROMPTS.md | Mínimo 3 prompts con role, contexto, tarea, restricción, comprensión |
| 25–40 | Revisión entre pares — intercambiar con compañero y dar feedback con checklist | ¿El prompt es reproducible? ¿Tiene comprensión línea a línea? |

#### Checklist de evaluación del PROMPTS.md

```
☐ Tiene al menos 3 prompts
☐ Cada prompt tiene: Role, Contexto, Tarea, Restricciones, Ejemplo
☐ Cada prompt tiene sección "Comprensión línea a línea"
☐ Al menos 1 prompt es de debugging (con traceback)
☐ Los prompts son reproducibles sin contexto extra
```

---

### BLOQUE P2-C — Revisión colectiva de commits (1:50 – 2:30)

**Objetivo:** Los alumnos tienen 7 commits descriptivos y entienden el valor semántico del historial de Git.

#### Plan de tiempos (40 min)

| Min | Actividad | Notas |
|-----|-----------|-------|
| 0–5 | `git log --oneline --graph` en pantalla del docente (repo con commits ejemplares) | Mostrar un historial "ideal" vs. uno con "fix fix fix" |
| 5–15 | Trabajo individual: asegurarse de tener ≥7 commits descriptivos | Usar GitLens para revisar el historial propio |
| 15–25 | Demo opcional: squash de commits vacíos con `git rebase -i` | Solo para avanzados — no requerido en TP2 |
| 25–35 | Demo: `git log --oneline --graph --all` para ver branches | Contextualizar: en el Módulo II van a trabajar con feature branches |
| 35–40 | Q&A sobre commits y Git | |

#### Notas docentes

- **El squash es opcional.** No confundir a quienes recién empezaron a usar Git. El rebase avanzado es material de Módulo II.
- **Commits mínimos:** El TP2 requiere 7 commits descriptivos. Verificar antes de P2-C cuántos alumnos tienen < 7 y hacer foco en ellos.

---

### BLOQUE P2-D — Retrospectiva + Preview Módulo II (2:35 – 2:55)

**Objetivo:** Cierre reflexivo del Módulo I y activación del curiosidad para el Módulo II.

#### Plan de tiempos (20 min)

| Min | Actividad | Notas |
|-----|-----------|-------|
| 0–8 | Retrospectiva anónima — pizarrón dividido en "Quedó claro" / "Costó mucho" / "Quiero saber más" | Opción: Mentimeter con word cloud |
| 8–16 | Preview Módulo II: TDD, pytest, ciclo Red→Green→Refactor | ¿Notaron que en el TP2 los tests ya estaban escritos? Eso es test-first |
| 16–20 | Recordatorio final: deadline TP2, link, criterio de evaluación | Proyectar F-84 (filmina de cierre) |

#### Material de la retrospectiva (pizarrón)

```
┌─────────────────┬─────────────────┬─────────────────┐
│   Quedó claro   │   Costó mucho   │ Quiero saber +  │
│                 │                 │                 │
│                 │                 │                 │
└─────────────────┴─────────────────┴─────────────────┘
```

#### Notas docentes de cierre

- **Los resultados de la retrospectiva son datos para el docente.** Registrar lo que costó más para ajustar la guía de estudio o abrir FAQs antes de Módulo II.
- **Conexión con TP2 → Módulo II:** "Los tests del TP2 que corriste son exactamente el patrón Red-Green-Refactor del TDD. En Módulo II aprendemos a escribir esos tests."

---

## Evaluación del módulo — Resumen TP2

| Componente | Criterio | Peso |
|------------|----------|------|
| Scripts `src/` | ≥5/7 con tests pytest en verde vía CI | 60% |
| `PROMPTS.md` | ≥3 prompts completos (Role+Contexto+Tarea+Restricción+Comprehensión) | 20% |
| Commits Git | ≥7 commits descriptivos con mensajes semánticos | 20% |
| **Deadline** | **Semana 4, lunes 23:59** | — |

**Calidad del código** (no ponderada pero requerida): Ruff sin errores, docstrings, type hints en todos los parámetros y retornos.
