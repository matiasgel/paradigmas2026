# Minuta por Filmina — Módulo I: Diseño Ágil + Python
## Tema 01 | IF009 Laboratorio de Programación y Lenguajes 2026

> **Para:** Matías Gel — Docente  
> **Uso:** Guión slide a slide. Cada entrada tiene qué decir, qué demostrar, qué preguntar y cómo pasar a la siguiente.  
> **Dependencia:** Abrir `filminas.md` en paralelo para ver el contenido visual mientras seguís este guión.

---

## ANTES DE COMENZAR

- Checklist pre-clase verificado (véase `minuta.md`)
- Python 3.13 listo en terminal para demos
- Codespace del TP2 abierto en una segunda pantalla / tab
- Filminas F-00 a F-42 cargadas en presentador

---

## SESIÓN T1 — Semana 2, Teoría

---

### [F-00] Portada Módulo I
**⏱ Antes del inicio — sin crono activo**

Proyectar mientras los alumnos ingresan. No explicar nada todavía.  
Cuando el aula está lista: *"Buenas, arrancamos."* → pasar a F-01.

---

### [F-01] Agenda T1
**⏱ 0:00 – 0:02 | T1-A apertura**

Leer la tabla en voz alta nombrando los 4 bloques.  
Decir: *"Al final de los 45 minutos de este primer bloque ya van a tener el entorno de trabajo listo y van a entender por qué el modelo ágil encaja perfectamente con la forma en que vamos a trabajar en este curso."*

No profundizar — este slide es orientación, no contenido.

→ **Transición:** *"Arranquemos con el modelo ágil. ¿Alguien escuchó este término antes?"*

---

### [F-02] ¿Qué es el Modelo Ágil?
**⏱ 0:02 – 0:09 | T1-A**

Preguntar: *"¿Alguien escuchó el término cascada o waterfall en el contexto del desarrollo de software?"*  
Esperar 2-3 respuestas. No corregir todavía.

Explicar el problema del modelo cascada con una analogía:  
*"Imaginen que les encargo un viaje: les doy todos los requerimientos en enero, me traen el viaje en diciembre. ¿Qué probabilidades hay de que sea exactamente lo que quería? Cero. El cliente cambió. Las circunstancias cambiaron. Eso era el software en los 70s."*

Señalar el diagrama (columna izquierda = cascada = rectángulos en waterfall, columna derecha = ciclo con flechas curvas = ágil).

→ **Transición:** *"Y en 2001, 17 personas se reunieron en Utah y escribieron 4 valores que cambiaron la industria."*

---

### [F-03] El Manifiesto Ágil — 2001
**⏱ 0:09 – 0:14 | T1-A**

Leer la tabla fila por fila. Para cada fila preguntar:  
*"¿Por qué creen que priorizamos X sobre Y?"*

El valor más resonante para el curso:  
**"Software funcionando sobre documentación exhaustiva"** — señalar que el TP2 es exactamente esto: la entrega que vale es el código con tests en verde, no el documento de análisis.

Citar la frase del final: *"No significa que lo de la derecha no importe — simplemente priorizamos lo de la izquierda."* Esto evita el anti-patrón "ágil = sin documentación".

→ **Transición:** *"¿Cómo se ve esto en la práctica? La tabla siguiente compara cascada con ágil dimensión por dimensión."*

---

### [F-04] Cascada vs. Ágil
**⏱ 0:14 – 0:18 | T1-A**

Recorrer la tabla rápido, resaltar **dos filas** con más detención:
1. **Entregas**: *"En cascada, la primera entrega real es al final del proyecto. En ágil, al final de cada iteración."*
2. **Riesgo**: *"En cascada, el riesgo se descubre tarde — cuando ya se invirtió todo. En ágil, se descubre pronto — cuando todavía se puede ajustar."*

El resto de filas no necesitan comentario extendido.

→ **Transición:** *"¿Cómo se materializa este ciclo iterativo? El próximo slide."*

---

### [F-05] El Ciclo Iterativo
**⏱ 0:18 – 0:25 | T1-A**

Señalar el ciclo de 5 íconos en sentido horario (la imagen muestra flechas curvas formando un loop).  
Nombrarlo: Planificar → Diseñar → Construir → Probar → Revisar.

**La conexión con el curso — decir esto textualmente:**  
*"En este curso, la iteración es el módulo temático. El entregable es el TP con tests en verde. El cliente es el enunciado más los tests de pytest. El ciclo no dura un sprint de 2 semanas — dura el tiempo entre semana 2 y el deadline de la semana 4. Pero el patrón es exactamente el mismo."*

Preguntar: *"¿En qué fase del ciclo estamos ahora mismo?" — Respuesta: Planificar.*

→ **Transición:** *"Para construir necesitamos herramientas. El próximo bloque es setup del entorno."*

---

### [F-06] Setup: VS Code + extensiones esenciales
**⏱ 0:25 – 0:29 | T1-A**

Mostrar el bloque JSON del devcontainer en la filmina. No leerlo línea a línea — señalar los 4 nombres de extensiones y vincularlos brevemente:  
*"Pylance verifica tipos en tiempo real. Ruff es el linter automático. GitLens hace visible el historial de commits sin salir del editor."*

Decir: *"Todas estas extensiones están preinstaladas en el devcontainer del TP2. No tienen que instalar nada."*

→ **Transición:** *"Abran el Codespace del TP2 ahora si no lo tienen abierto. Mientras, les muestro qué hace Pylance."*

---

### [F-07] Pylance — type checking en tiempo real
**⏱ 0:29 – 0:32 | T1-A | 🔵 DEMO**

**Hacer en vivo:** Abrir `src/hello.py` del TP2 en el Codespace (pantalla del docente).  
Escribir el código del slide:
```python
def sumar(a: int, b: int) -> int:
    return a + b

resultado = sumar("hola", 3)
```
Señalar el subrayado rojo bajo `"hola"` antes de ejecutar.  
*"El editor me está diciendo que hay un error de tipo antes de correr el programa. No voy a esperar hasta el CI para descubrirlo."*

→ **Transición:** *"Pylance ve los tipos. Ruff ve el estilo. ¿Qué hace Ruff exactamente?"*

---

### [F-08] Ruff — linter ultrarrápido
**⏱ 0:32 – 0:35 | T1-A | 🔵 DEMO**

No extenderse aquí — hay un demo dedicado en F-40.  
Solo decir: *"Ruff detecta violaciones a PEP 8 y también imports sin usar, funciones sin docstring, y más. Lo vamos a ver en acción al final de la clase."*

Mostrar el comando del slide: `ruff check src/hello.py` en terminal brevemente.

→ **Transición:** *"GitLens — el historial de commits, directo en el editor."*

---

### [F-09] GitLens — historial visible en el editor
**⏱ 0:35 – 0:38 | T1-A**

Abrir cualquier archivo del TP2 con GitLens instalado. Señalar el texto de blame inline (quién modificó cada línea y cuándo).

*"El 20% del puntaje del TP2 son los commits. GitLens hace visible si sus mensajes dicen algo útil o no. 'fix' y 'update' son los peores mensajes posibles — los vamos a ver en el aula la semana que viene y va a quedar claro por qué."*

→ **Transición:** *"¿Dónde corre todo esto? En Codespaces."*

---

### [F-10] GitHub Codespaces
**⏱ 0:38 – 0:41 | T1-A**

Señalar el ícono (monitor + nube en la imagen).  
*"Codespaces es VS Code corriendo en un servidor de GitHub. No instalan Python localmente — el entorno vive en la nube y está definido exactamente en el devcontainer."*

Verificar que todos tienen el Codespace del TP2 abierto. Si alguien no puede → el link está en F-41 al final de la clase.

→ **Transición:** *"¿Cómo se define ese entorno? El próximo slide."*

---

### [F-11] DevContainer — el entorno como código
**⏱ 0:41 – 0:44 | T1-A**

Leer el JSON del slide lentamente, señalando:  
- `"image": "...python:3.13"` → versión fija de Python  
- `"extensions": [...]` → las 3 extensiones que vimos  
- `"postCreateCommand": "pip install -r requirements.txt"` → instala dependencias automáticamente al abrir

*"Si yo abro este repo y vos abrís este repo, tenemos exactamente el mismo entorno. Eso es reproducibilidad. El CI de GitHub Actions también usa la misma imagen."*

→ **Transición:** *"Pregunta de cierre antes de pasar a Python."*

---

### [F-12] Cierre T1-A
**⏱ 0:44 – 0:47 | T1-A — SOCRÁTICA**

Leer las tres preguntas del slide en voz alta. Dar 30 segundos de silencio para que piensen.  
Pedir 1-2 respuestas voluntarias.

**Respuesta que buscar:** *"Los tests de pytest son el cliente. El TP2 con tests en verde es el software funcionando. Cada push que hace el CI correr es una mini-iteración."*

Si alguien lo dice bien: *"Exacto — Red→Green→Refactor es el ciclo ágil más pequeño posible. Lo vamos a ver de nuevo en el Módulo II cuando aprendamos TDD."*

→ **PAUSA 5 min antes de T1-B.**

---

## BLOQUE T1-B — Python 3.13 Fundamentos

---

### [F-13] ¿Por qué Python en 2026?
**⏱ 0:50 – 0:53 | T1-B**

Decir los 3 puntos rápido. No es el foco de este bloque.  
*"TIOBE es el índice de popularidad de lenguajes — Python lleva 2 años primero, superando a C. Para este curso importa porque es el lenguaje del TP2, los Módulos I–II–III lo usan y ya tienen el REPL disponible en Codespaces."*

No discutir "Python vs otros lenguajes" más de 1 minuto.

→ **Transición:** *"Arrancamos. ¿Qué tipos de datos tiene Python?"*

---

### [F-14] Tipos primitivos en Python
**⏱ 0:53 – 0:58 | T1-B**

Leer la tabla fila por fila con el REPL abierto para verificar en vivo:  
```python
type(42)         # <class 'int'>
type(3.14)       # <class 'float'>
type("hola")     # <class 'str'>
type(True)       # <class 'bool'>
type(None)       # <class 'NoneType'>
```

**Provocar curiosidad:** *"¿Cuál es el tipo de `True + True`?"* → Esperar respuestas → mostrar: resultado `2`.  
Decir: *"bool es subclase de int en Python. True vale 1, False vale 0."*

→ **Transición:** *"¿Cómo se asignan variables en Python?"*

---

### [F-15] Asignación y operadores
**⏱ 0:58 – 1:04 | T1-B | 🔵 REPL**

Tipear los ejemplos del slide en el REPL junto con la clase, pedir que lo repliquen en sus Codespaces.

Destacar los operadores especiales:  
- `//` → división entera: *"10 // 3 es 3, no 3.33."*
- `%` → módulo: *"10 % 3 es 1. Útil para saber si un número es par: `n % 2 == 0`."*
- `**` → potencia: *"2 ** 8 es 256. También funciona como raíz: `16 ** 0.5` es 4.0."*

→ **Transición:** *"Ahora les muestro el nuevo REPL interactivo de Python 3.13."*

---

### [F-16] Python 3.13 — Nuevo REPL interactivo
**⏱ 1:04 – 1:10 | T1-B | 🔵 DEMO CLAVE**

**Demo en vivo en terminal del Codespace:**
1. Escribir `python3` y mostrar el nuevo prompt (`>>>`).
2. Definir la función del slide con sangría — mostrar que acepta código multilínea.
3. Llamar a `saludar("Python")`.
4. Presionar flecha ↑ para mostrar el historial.
5. Mostrar la sintaxis coloreada.

*"Antes de la versión 3.13, pegar un bloque de código de múltiples líneas en el REPL se rompía. Ahora funciona bien. Útil para testear ideas rápido."*

→ **Transición:** *"Y si me equivoco al escribir algo, ¿qué pasa ahora?"*

---

### [F-17] Mensajes de error contextuales en Python 3.13
**⏱ 1:10 – 1:14 | T1-B | 🔵 DEMO**

**Demostrar en el REPL:**
```python
"hola".upper_case()
```
Mostrar el mensaje: `Did you mean: 'upper'?`

```python
import math
math.squareroot(16)
```
Mostrar: `Did you mean: 'sqrt'?`

*"En Python 3.12 esto daba un error genérico y tenían que buscar en Google. En 3.13 el intérprete ya sugiere la corrección. Reduce el tiempo de debugging para código simple."*

→ **Transición:** *"Ahora: strings. La inmutabilidad es lo más importante de este tipo."*

---

### [F-18] Strings — inmutabilidad
**⏱ 1:14 – 1:18 | T1-B**

Tipear en el REPL:
```python
nombre = "Ada"
nombre[0] = "E"   # Error → mostrar el TypeError
```

*"¿Por qué falla? Porque los strings son inmutables — no se pueden modificar in-place. Para 'cambiar' uno hay que crear uno nuevo."*

Mostrar la solución:
```python
nombre_nuevo = "E" + nombre[1:]
```

Contrastar con lista:
```python
lista = [1, 2, 3]
lista[0] = 99   # Esto SÍ funciona
```

→ **Transición:** *"Los métodos más usados de string para el TP2."*

---

### [F-19] Strings — métodos más usados
**⏱ 1:18 – 1:22 | T1-B**

No leer toda la tabla. Demostrar los 3 más importantes para el TP2:
```python
# strip — limpiar entrada de usuario
"  hola  ".strip()            # "hola"

# split — parsear CSV o palabras
"a,b,c".split(",")            # ["a", "b", "c"]

# f-string join
", ".join(["Ana", "Bob"])     # "Ana, Bob"
```

*"Estos tres los van a usar en el TP2 con casi certeza."*

→ **Transición:** *"f-strings — la sintaxis de interpolación moderna."*

---

### [F-20] f-strings — interpolación moderna
**⏱ 1:22 – 1:25 | T1-B**

Tipear en REPL los tres ejemplos del slide. Énfasis en el formato numérico:
```python
precio = 1500
descuento = 0.1
f"Total: ${precio * (1 - descuento):.2f}"
```

*"El `:.2f` dentro del f-string es format spec — 2 decimales, notación float. Lo van a usar en calculadora.py del TP2 si devuelven precios o porcentajes."*

→ **Transición:** *"Ahora el concepto más importante de este bloque — y que tiene consecuencias directas en el TP2."*

---

### [F-21] Variables y referencias
**⏱ 1:25 – 1:30 | T1-B | ⚠️ PAUSA SOCRÁTICA**

**Ejercicio de predicción — hacer antes de mostrar el resultado:**
```python
a = [1, 2, 3]
b = a
b.append(99)
```
*"Sin ejecutar — ¿qué imprime `print(a)`?"*  
Esperar predicciones. Luego ejecutar.

Cuando la clase ve `[1, 2, 3, 99]`: *"¿Por qué? Porque `b = a` no copia la lista — hace que `b` apunte al mismo objeto en memoria."*

Mostrar la solución:
```python
c = a.copy()   # o: a[:] o: list(a)
c.append(100)
print(a)       # sin cambios
```

*"¿Por qué importa para el TP2? Si una función modifica la lista que recibe como argumento, podría afectar la lista original del test. Siempre copiar antes de modificar si no queremos ese efecto."*

→ **Transición:** *"None y booleans — detalles que sorprenden."*

---

### [F-22] None y Boolean — detalles que sorprenden
**⏱ 1:30 – 1:34 | T1-B**

Demostrar en REPL:
```python
True + True       # 2
bool("")          # False
bool([])          # False
bool(0)           # False
bool("0")         # True  ← sorprende a algunos
```

*"Regla de oro: `0`, `None`, `[]`, `{}`, `""` son todos `falsy` en Python. Todo lo demás es `truthy`."*

Mostrar el patrón de comparar con `None`:
```python
resultado = None
if resultado is None:   # ✅ correcto
    print("no encontrado")
```

*"`is None` no es `== None` — funcionan igual para None pero `is` es semánticamente más correcto."*

→ **Transición:** *"Conversiones de tipo — Python no convierte automáticamente."*

---

### [F-23] Conversiones de tipo
**⏱ 1:34 – 1:37 | T1-B**

Tipear brevemente en REPL los ejemplos de conversión:
```python
int("25")           # 25
float("19.99")      # 19.99
str(42)             # "42"
```

Mostrar el caso de validación — relevante para TP2 con entrada del usuario:
```python
entrada = "abc"
if entrada.isdigit():
    numero = int(entrada)
else:
    print("No es un número válido")
```

*"En el TP2 no van a manejar input del usuario directamente, pero cuando Copilot genere código con conversiones, asegúrense de que valida antes de convertir."*

→ **Transición:** *"Tabla comparativa: string vs. lista."*

---

### [F-24] Inmutabilidad: str vs. list
**⏱ 1:37 – 1:40 | T1-B**

Leer la tabla resumiendo: *"El punto clave: str es hashable — se puede usar como clave de diccionario. list no, porque es mutable. Tuple sí — lo vemos en T2."*

Demostrar la diferencia con dict:
```python
d = {"hola": 1}      # ✅ — str como clave
d = {[1,2]: 1}       # ❌ TypeError — list no hashable
```

→ **Transición:** *"Dos operadores importantes: `is` e `in`."*

---

### [F-25] Operadores de identidad y pertenencia
**⏱ 1:40 – 1:43 | T1-B**

Demostrar el punto de `is` vs `==`:
```python
a = [1, 2, 3]
c = [1, 2, 3]
a == c    # True  — mismo contenido
a is c    # False — objetos distintos
```

Regla práctica: *"Usen `is` solo para comparar con `None`, `True`, `False`. Para comparar valores, usen `==`."*

Demostrar `in`:
```python
2 in [1, 2, 3]        # True
"Py" in "Python"      # True
```

→ **Transición:** *"Cierre rápido de T1-B."*

---

### [F-26] Cierre T1-B
**⏱ 1:43 – 1:45 | T1-B — RONDA RÁPIDA**

Hacer las 5 preguntas del slide en modo "preguntas rápidas" — respuesta en 3 segundos cada una.  
Si alguien duda en la pregunta 5 (tuple para colección que no debe cambiar): es una anticipación a T2.

*"Perfecto. Ya tienen los tipos base. Pasamos a controlar el flujo."*

→ **PAUSA 5 min antes de T1-C.**

---

## BLOQUE T1-C — Control de flujo + Funciones

---

### [F-27] if / elif / else
**⏱ 1:50 – 1:54 | T1-C | 🔵 LIVE CODING**

Tipear la función `clasificar_nota` del slide en el editor (no en REPL).  
Pedir que los alumnos dicten la lógica:  
*"¿Qué condición va primero? ¿Por qué importa el orden?"*

Mostrar también el anti-patrón del slide: sin type hints, sin docstring, lógica invertida.  
*"Ruff va a marcar este código con D103 (falta docstring) y puede marcar B007 o similares por la lógica confusa."*

→ **Transición:** *"Para recorrer una lista usamos `for`."*

---

### [F-28] for sobre secuencias
**⏱ 1:54 – 1:58 | T1-C | 🔵 LIVE CODING**

Tipear los tres ejemplos del slide en orden.  
El anti-patrón a mostrar:
```python
# ❌ Antipatrón — índice manual innecesario
for i in range(len(frutas)):
    print(frutas[i])

# ✅ Pythónico
for fruta in frutas:
    print(fruta)
```

*"Cuando necesitan el índice Y el valor, usen `enumerate()` — lo vemos en T2. Por ahora: iterar directamente sobre la secuencia."*

→ **Transición:** *"`while` para cuando no sabemos cuántas iteraciones vamos a hacer."*

---

### [F-29] while + break + continue
**⏱ 1:58 – 2:02 | T1-C | 🔵 LIVE CODING**

Tipear el ejemplo del login con `while`. Señalar el bloque `else` del `while` — *"este `else` se ejecuta si el while terminó normalmente, sin `break`. Es un patrón Python bastante especial."*

Mostrar `continue`:
```python
for i in range(10):
    if i % 2 == 0:
        continue    # salta los pares
    print(i)        # imprime 1, 3, 5, 7, 9
```

→ **Transición:** *["`match` — Python 3.10+, más expresivo que `if/elif` encadenado."*

---

### [F-30] match — Pattern Matching (Python 3.10+)
**⏱ 2:02 – 2:06 | T1-C | 🔵 LIVE CODING**

Tipear la función `describir_http` del slide.  
*"El caso `_` es el default — como el `else` del if. Disponible en Python 3.10+ — el devcontainer usa 3.13 así que está activado."*

Mostrar el ejemplo de destructuring de tuplas — solo para los que van rápido:
```python
punto = (1, 0)
match punto:
    case (0, 0): print("origen")
    case (x, 0): print(f"eje X: {x}")
```

*"Esto es muy práctico para el TP2 si la función `calculadora.py` recibe el operando y la operación en una tupla."*

→ **Transición:** *"Ahora la parte más importante de T1-C: anatomía de una función."*

---

### [F-31] def + return + docstrings
**⏱ 2:06 – 2:11 | T1-C | ⚠️ SLIDE CLAVE PARA TP2**

Tipear la función `calcular_imc` lentamente, nombrando cada parte:  
1. `def` + nombre en snake_case  
2. Parámetros con `: tipo`  
3. `-> tipo` de retorno  
4. Triple comilla `"""` — docstring  
5. `Args:` / `Returns:` — formato Google docstring  
6. Guard clause con `raise`  
7. `return`

*"Esta es la plantilla que usan para TODAS las funciones del TP2. Si falta el docstring, Ruff levanta D103. Si faltan los type hints, Pylance los marca y pueden fallar en CI dependiendo de cómo está configurado."*

Demostrar que Pylance muestra el docstring al hover sobre la función llamante.

→ **Transición:** *"Los parámetros de las funciones Python."*

---

### [F-32] Parámetros — posicionales y keyword
**⏱ 2:11 – 2:15 | T1-C | 🔵 LIVE CODING**

Tipear `crear_usuario` y las 4 llamadas del slide.  
Pregunta socrática: *"Si llamo `crear_usuario(22, 'Ana')`, ¿qué pasa?"* → Error: `int` no es `str`. Pylance lo ve antes de ejecutar.

Mostrar `def conectar(host, *, puerto=80)` de pasada — *"el `*` fuerza a que `puerto` se pase solo por keyword: `conectar('localhost', puerto=8080)`. No requerido para TP2 pero útil de conocer."*

→ **Transición:** *"`*args` y `**kwargs` — funciones con cantidad variable de argumentos."*

---

### [F-33] *args y **kwargs
**⏱ 2:15 – 2:18 | T1-C**

Tipear `sumar_todos` brevemente.  
*"En TP2 no van a necesitar implementar funciones con `*args`. Lo que sí van a ver es que algunos builtins los usan — `print(*lista)` desempaqueta la lista como argumentos."*

Demostrar en REPL:
```python
numeros = [1, 2, 3]
print(*numeros)   # imprime: 1 2 3
```

→ **Transición:** *"Scope — dónde vive cada variable."*

---

### [F-34] Scope de variables
**⏱ 2:18 – 2:21 | T1-C**

Mostrar la tabla LEGB. Decir: *"La regla simple: una variable existe desde donde se define hasta el final de ese bloque. Las funciones tienen su propio scope — no contamina al código exterior."*

*"Para el TP2: eviten `global`. Si una función necesita modificar algo externo, devuelvan el nuevo valor y reasignen. Código más limpio."*

No profundizar en closures — está fuera de scope para este módulo.

→ **Transición:** *"Recursión — una función que se llama a sí misma."*

---

### [F-35] Recursión básica
**⏱ 2:21 – 2:24 | T1-C**

Tipear `factorial`. Señalar **caso base** y **caso recursivo** explícitamente.  
Mostrar la traza de ejecución del slide.

*"La recursión tiene un límite en Python — por defecto 1000 llamadas anidadas. Para el TP2, `fibonacci.py` puede implementarse iterativamente — de hecho es más eficiente. La recursión aparece aquí como concepto, no como requerimiento del TP2."*

→ **Transición:** *"Cierre T1-C con una pregunta socrática."*

---

### [F-36] Cierre T1-C
**⏱ 2:24 – 2:27 | T1-C — SOCRÁTICA**

Leer la tabla for/while/match rápidamente.

Proyectar el código de `es_primo(n)` del slide y preguntar:  
*"¿Por qué `range(2, n)` es ineficiente para números grandes?"*

Esperar respuestas. Si nadie llega: *"Si n tiene un divisor mayor a √n, ya tiene uno menor a √n también. Entonces solo hay que verificar hasta `int(n**0.5)+1`."*

No resolver en código — dejarlo como ejercicio para P1.

→ **PAUSA 5 min antes de T1-D.**

---

## BLOQUE T1-D — Ruff + PEP 8 + Preview TP2

---

### [F-37] ¿Qué es PEP 8?
**⏱ 2:32 – 2:36 | T1-D**

Leer la tabla resaltando las dos convenciones que más se olvidan:  
- `snake_case` para funciones → importante porque el TP2 tiene funciones con nombres definidos
- 88 chars de línea → Ruff usa esta configuración

*"PEP 8 no es un capricho — es lo que hace que cualquier programador Python pueda leer tu código. 'Readability counts' es el inciso 7 del Zen de Python."*

→ **Transición:** *"Un ejemplo concreto de código opaco vs. autodocumentado."*

---

### [F-38] Código autodocumentado
**⏱ 2:36 – 2:41 | T1-D | ⚠️ COMPARACIÓN EN VIVO**

Mostrar el bloque "Antes" y preguntar: *"¿Qué hace esta función?"*  
Esperar 10 segundos. La mayoría no sabrá sin pensarlo.

Mostrar el bloque "Después":  
*"Mismo comportamiento, mismo número de líneas, pero ahora cualquier persona puede leer qué hace en 2 segundos."*

Principio de responsabilidad única — decir: *"Si necesitan escribir comentarios `# Parte 1` / `# Parte 2` dentro de una función, es una señal de que la función hace demasiado. Dividirla."*

→ **Transición:** *"Tabla de convenciones de nombres para referencia."*

---

### [F-39] Convenciones de nombres — resumen ejecutivo
**⏱ 2:41 – 2:44 | T1-D**

Leer la tabla rápido. Pedir que la dejen abierta como referencia en el TP2.

Decir: *"Ruff detecta y marca violaciones a estas convenciones bajo el grupo de reglas N. Si el CI falla con un error que empieza en N, es una convención de nombres."*

→ **Transición:** *"Demo en vivo."*

---

### [F-40] Ruff en acción — ejemplos reales
**⏱ 2:44 – 2:48 | T1-D | 🔵 DEMO CLAVE**

**Hacer en vivo en el Codespace:**
1. Crear un archivo temporal `demo_errores.py` con el código "malo" del slide.
2. Correr `ruff check demo_errores.py` → mostrar los errores F401, E231, E225.
3. Correr `ruff check --fix demo_errores.py` → mostrar que se autocorrige.
4. Borrar el archivo temporal.

*"Esto es lo que el CI del TP2 va a correr en cada push. Si `ruff check .` falla en CI, el build falla — aunque pytest pase."*

→ **Transición:** *"Un vistazo rápido a la estructura del TP2."*

---

### [F-41] Preview TP2 — ¿Qué vas a entregar?
**⏱ 2:48 – 2:52 | T1-D**

Proyectar la estructura del repo. No abrir cada archivo — solo navegar el árbol en el Codespace.

Señalar en el árbol:
- `src/` → donde van a codear
- `tests/` → los tests ya están escritos
- `PROMPTS.md` → 20% del puntaje
- `.github/workflows/` → el CI

Recordar el link: `classroom.github.com/a/X4xiTEDQ`  
*"Si no lo aceptaron todavía, háganlo antes de P1."*

→ **Transición:** *"Cierre de T1 y resumen."*

---

### [F-42] Cierre T1 — Resumen y pausa
**⏱ 2:52 – 2:57 | T1-D**

Leer los 4 bloques del resumen. Preguntar: *"¿Alguna duda rápida antes de cerrar?"*

Dejar 5 min para preguntas.

Anunciar: *"La sesión P1 es el martes/jueves. Traigan el Codespace del TP2 ya abierto."*

---

---

## SESIÓN T2 — Semana 3, Teoría

---

### [F-43] Agenda T2 / Portada
**⏱ 0:00 – 0:02 | T2-A apertura**

Igual que F-01: leer los 4 bloques brevemente.  

Preguntar: *"¿Cuántos tienen CI verde en al menos 1 script del TP2?"* — Contar a mano o mostrar Mentimeter.

*"Perfecto. Hoy vemos las colecciones y los módulos que usan los scripts más difíciles del TP2. Al terminar, los que estaban trabados van a tener todo lo que necesitan para desatascarse."*

→ **Transición:** *"Empezamos con los 4 tipos de colecciones."*

---

## BLOQUE T2-A — Colecciones Python

---

### [F-44] Las cuatro colecciones fundamentales
**⏱ 0:02 – 0:07 | T2-A**

Leer la tabla enfocando en la columna **Caso de uso**:  
*"La pregunta no es qué colección existe — es cuál me conviene para este problema."*

Preguntar: *"¿Para guardar los nombres de los alumnos de la materia, uso list o set?"*  
Respuesta: list — porque puede haber dos Anas y necesitamos mantener el orden.

*"¿Y para los lenguajes que conoce cada alumno?"*  
Respuesta: set — porque un alumno no puede conocer el mismo lenguaje "dos veces".

→ **Transición:** *"`list` — la más usada."*

---

### [F-45] list — la colección más usada
**⏱ 0:07 – 0:15 | T2-A | 🔵 LIVE CODING**

Tipear en REPL todos los ejemplos del slide.  
**Énfasis en los métodos que aparecen en el TP2:**
```python
notas = [85, 72, 91, 68, 77]
notas.append(95)        # agregar al final
notas.sort()            # ordenar in-place
sorted(notas)           # nueva lista ordenada (no modifica la original)
```

Señalar la diferencia `sort()` vs `sorted()`:  
*"`notas.sort()` modifica la lista original. `sorted(notas)` devuelve una nueva lista y deja la original intacta. Para el TP2, si el test espera la lista original sin cambios, usen `sorted()`."*

→ **Transición:** *"`tuple` — cuando los datos no deben cambiar."*

---

### [F-46] tuple — inmutabilidad como diseño
**⏱ 0:15 – 0:20 | T2-A | 🔵 LIVE CODING**

Tipear el ejemplo de `punto_2d = (3, 5)` con unpacking:
```python
x, y = punto_2d
```

Demostrar que no se puede modificar:
```python
punto_2d[0] = 99   # TypeError
```

**Conexión práctica:** *"En `type_hints.py` del TP2 van a trabajar con `tuple[float, float]` como tipo de retorno."*

Mostrar el uso como clave de dict del slide — impresiona a los alumnos:
```python
mapa = {(0, 0): "origen", (1, 0): "derecha"}
```

→ **Transición:** *"`dict` — el más versátil."*

---

### [F-47] dict — mapa clave-valor
**⏱ 0:20 – 0:28 | T2-A | 🔵 LIVE CODING**

Tipear el dict `alumno` del slide. Énfasis en `.get()` con default:
```python
email = alumno.get("email", "sin email")
```
*"Si usan `alumno['email']` y la clave no existe, KeyError. Si usan `.get('email', 'sin email')`, devuelve el default en lugar de romper. Para el TP2 con `colecciones.py`, esto evita muchos errores."*

Demostrar `items()` en REPL:
```python
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")
```

→ **Transición:** *"`set` — conjuntos sin duplicados."*

---

### [F-48] set — conjuntos sin duplicados
**⏱ 0:28 – 0:33 | T2-A | 🔵 LIVE CODING**

Tipear el ejemplo de lenguajes A y B. Demostrar las operaciones de conjunto:
```python
lenguajes_alumno_a = {"Python", "JavaScript", "C"}
lenguajes_alumno_b = {"Python", "Java", "C", "Go"}
comunes = lenguajes_alumno_a & lenguajes_alumno_b
```

Mostrar el truco de deduplicación:
```python
lista_con_dup = [1, 2, 2, 3, 3, 4]
sin_dup = list(set(lista_con_dup))
```
*"Aviso: si el orden importa, no usar este truco directamente — set no garantiza orden."*

→ **Transición:** *"Comprensiones de lista — el patrón más pythónico."*

---

### [F-49] Comprensiones de lista
**⏱ 0:33 – 0:40 | T2-A | 🔵 LIVE CODING**

**Mostrar la evolución en 3 pasos:**
```python
# Paso 1: for loop clásico
cuadrados = []
for x in range(10):
    cuadrados.append(x ** 2)

# Paso 2: comprensión
cuadrados = [x ** 2 for x in range(10)]

# Paso 3: con filtro
pares = [x for x in range(20) if x % 2 == 0]
```

Leer el patrón en voz alta: *"expresión — for x in iterable — if condición. La condición es opcional."*

Preguntar: *"¿Cómo escribirían con comprensión: 'los cuadrados de todos los números pares de 1 a 20'?"*

→ **Transición:** *"El mismo patrón para dict y set."*

---

### [F-50] Comprensiones de dict y set
**⏱ 0:40 – 0:45 | T2-A | 🔵 LIVE CODING**

Tipear el dict comprehension:
```python
nombres = ["Ana", "Roberto", "Li", "Valentina"]
longitudes = {n: len(n) for n in nombres}
```

*"La diferencia con list comprehension es que usamos `{}` y tenemos `clave: valor` después del for."*

Mostrar set comprehension brevemente.  
*"Para el TP2 con `colecciones.py`, estos tres tipos de comprensiones van a aparecer."*

→ **Transición:** *"`enumerate` y `zip` — dos builtins que evitan el contador manual."*

---

### [F-51] enumerate() y zip()
**⏱ 0:45 – 0:50 | T2-A | 🔵 LIVE CODING**

Mostrar anti-patrón vs. patrón con enumerate:
```python
# ❌ anticuado
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

# ✅ pythónico
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
```

Demostrar `zip()`:
```python
for nombre, nota in zip(nombres, notas):
    print(f"{nombre}: {nota}")
```

*"Detalle importante: `zip()` devuelve un iterator, no una lista. Para materializarlo: `list(zip(...))`."*

→ **Transición:** *"`sorted` con criterio personalizado."*

---

### [F-52] sorted(), min(), max() con key=
**⏱ 0:50 – 0:55 | T2-A | 🔵 LIVE CODING**

Tipear el ejemplo de `alumnos` y ordenar por nota.  
*"El argumento `key=` recibe cualquier función callable. Aquí usamos una lambda — la vemos en detalle en T2-B."*

Mostrar `max(key=)`:
```python
mejor = max(alumnos, key=lambda a: a["nota"])
```

→ **Transición:** *"Tabla de builtins de reducción — referencia rápida."*

---

### [F-53] Funciones builtin de reducción
**⏱ 0:55 – 0:58 | T2-A**

Leer la tabla rápido. Enfatizar `any()` y `all()` — *"menos conocidos pero muy útiles."*

Demostrar en REPL:
```python
any([0, 0, 1])   # True — al menos uno es truthy
all([1, 1, 0])   # False — no todos son truthy
all([1, 2, 3])   # True — todos truthy
```

→ **Transición:** *"Slicing avanzado — si hay tiempo."*

---

### [F-54] Slicing avanzado
**⏱ 0:58 – 1:02 | T2-A | ⚠️ OPCIONAL SI EL TIEMPO APRIETA**

Si llevan buen ritmo, tipear los ejemplos del slide:
```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[::-1]   # invertir
numeros[::2]    # cada dos
```

*"El slicing inverso `[::-1]` es el più usado. Lo van a ver en `fibonacci.py` del TP2 — `serie[:n]` trunca la lista a los primeros n elementos."*

Si el tiempo está ajustado: *"El slicing está en la guía de estudio — pueden practicarlo ahí."*

→ **Transición:** *"Pregunta socrática."*

---

### [F-55] Elegir la colección correcta
**⏱ 1:02 – 1:05 | T2-A — SOCRÁTICA**

Leer los 5 casos del slide, pedir respuesta a mano alzada.  
Caso 5 (comprensión de lista): preguntar quién puede escribirlo en REPL antes de mostrar la respuesta.

→ **Transición:** *"Resumen y cierre de T2-A."*

---

### [F-56] Cierre T2-A
**⏱ 1:05 – 1:07 | T2-A**

Leer el resumen brevemente.  
*"Los scripts `colecciones.py` y `funciones_ord.py` del TP2 usan casi todo lo que vimos en este bloque."*

→ **PAUSA 5 min antes de T2-B.**

---

## BLOQUE T2-B — Módulos + HOF + Lambdas + Decoradores

---

### [F-57] Módulos y paquetes en Python
**⏱ 1:12 – 1:17 | T2-B | 🔵 LIVE CODING**

Tipear los dos archivos del slide en el Codespace:
```python
# calculadora.py
def sumar(a: int, b: int) -> int:
    return a + b
```
```python
# main.py
import calculadora
from calculadora import sumar
```

Demostrar que `from calculadora import sumar` permite llamar `sumar()` directamente sin el prefijo.

*"En el TP2, `tests/test_calculadora.py` hace `from src.calculadora import ...`. Por eso el `src/__init__.py` es necesario."*

→ **Transición:** *"La estructura estándar del TP2."*

---

### [F-58] Estructura de proyecto Python
**⏱ 1:17 – 1:22 | T2-B**

Abrir el árbol de archivos del Codespace del TP2. Señalar cada carpeta mientras la explica.

Enfatizar: *"¿Qué es `__init__.py`?"*  
Tipear en REPL:
```python
# Sin __init__.py → ImportError
# Con __init__.py → from src.calculadora import sumar  funciona
```

*"Si el CI falla con `ModuleNotFoundError: No module named 'src'`, probablemente falta el `__init__.py`."*

→ **Transición:** *"`requirements.txt` — las dependencias declaradas."*

---

### [F-59] requirements.txt
**⏱ 1:22 – 1:25 | T2-B**

Abrir el `requirements.txt` del TP2 en el Codespace.  
Mostrar `pip install -r requirements.txt` en terminal.

*"Las versiones están fijadas para que CI local y remoto usen las mismas. Si agregan una dependencia nueva, actualicen el archivo o el CI va a fallar."*

→ **Transición:** *"HOF — funciones de orden superior. El concepto más nuevo de T2-B."*

---

### [F-60] Funciones de orden superior — el concepto
**⏱ 1:25 – 1:30 | T2-B**

Señalar el diagrama (rectángulo con dos flechas entrando y una saliendo).

Tipear el ejemplo del slide en REPL:
```python
def aplicar(func, valor):
    return func(valor)

def duplicar(x: int) -> int:
    return x * 2

aplicar(duplicar, 5)   # 10
```

*"Note que `duplicar` se pasa sin paréntesis — se pasa la función como objeto, no se la llama. Esa distinción es la clave de las HOF."*

→ **Transición:** *"`map()` — la HOF más común para transformar."*

---

### [F-61] map() — transformar todos los elementos
**⏱ 1:30 – 1:35 | T2-B | 🔵 LIVE CODING**

Tipear los dos ejemplos del slide en REPL.  
**Siempre** envolver en `list()` para materializar el resultado:
```python
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
```

Mostrar la equivalencia con comprensión:
```python
[x ** 2 for x in [1, 2, 3, 4, 5]]
```

*"Son equivalentes. En Python prefieren comprensión cuando la función es simple. `map()` se usa cuando ya tienen la función nombrada."*

→ **Transición:** *"`filter()` — para seleccionar."*

---

### [F-62] filter() — seleccionar elementos
**⏱ 1:35 – 1:40 | T2-B | 🔵 LIVE CODING**

Tipear el ejemplo de aprobados:
```python
notas = [85, 65, 90, 55, 72, 68]
list(filter(lambda n: n >= 70, notas))
```

Mostrar la equivalencia con comprensión:
```python
[n for n in notas if n >= 70]
```

*"De nuevo: preferir comprensión para casos simples. `filter()` con función nombrada es más legible cuando la condición es compleja."*

→ **Transición:** *"`lambda` — la función anónima."*

---

### [F-63] lambdas — funciones anónimas
**⏱ 1:40 – 1:44 | T2-B**

Tipear los ejemplos y señalar el patrón: `lambda parámetros: expresión`.

*"Una regla práctica: si la lambda tiene más de una expresión o necesita varias líneas, usar `def`. Lambda es para funciones de una sola expresión."*

Mostrar los dos casos de uso del slide — ✅ en key=, ❌ para funciones complejas.

→ **Transición:** *"`sorted(key=)` — la HOF más práctica del día a día."*

---

### [F-64] sorted() con key= — la HOF más práctica
**⏱ 1:44 – 1:49 | T2-B | 🔵 LIVE CODING**

Tipear el ejemplo de palabras:
```python
palabras = ["banana", "manzana", "kiwi", "pera", "cereza"]
sorted(palabras, key=len)      # por longitud
sorted(palabras, key=len, reverse=True)  # descendente
```

*"Este patrón aparece en `funciones_ord.py` del TP2. La función `key=` recibe un elemento y devuelve el criterio de ordenamiento."*

→ **Transición:** *"Decoradores — el concepto."*

---

### [F-65] Decoradores — el concepto
**⏱ 1:49 – 1:54 | T2-B**

Señalar el diagrama (tres rectángulos apilados con el bordo envolviendo al gris).

Tipear el decorador mínimo del slide:
```python
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Después")
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre: str) -> str:
    return f"Hola {nombre}"

saludar("mundo")   # imprime Antes, "Hola mundo", Después
```

*"Decoradores son azúcar sintáctica. `@mi_decorador` antes de `saludar` es equivalente a `saludar = mi_decorador(saludar)`."*

→ **Transición:** *"`@property` — el decorador más común en Python."*

---

### [F-66] @property — encapsulamiento pythónico
**⏱ 1:54 – 1:59 | T2-B**

No codear toda la clase en vivo — mostrar en el slide y señalar:  
- `@property` → getter  
- `@celsius.setter` → setter con validación  
- `@property fahrenheit` → getter calculado

*"En el TP2 no van a implementar clases. Pero cuando vean `t.fahrenheit` sin paréntesis, es un `@property`. No es un error."*

→ **Transición:** *"`@staticmethod` — función utilitaria dentro de una clase."*

---

### [F-67] @staticmethod y @classmethod
**⏱ 1:59 – 2:03 | T2-B**

Leer la tabla del slide.  
*"Para el TP2: si implementan la validación de entrada como función estática, Ruff y test quedan más limpios."*

Tipear el ejemplo de `Validador.es_email_valido` brevemente.

→ **Transición:** *"`@functools.wraps` — para decoradores bien escritos."*

---

### [F-68] @functools.wraps — decoradores correctos
**⏱ 2:03 – 2:06 | T2-B**

Tipear el ejemplo del slide. Demostrar:
```python
print(sumar.__name__)   # "sumar" — con @wraps
# Sin @wraps sería "wrapper"
```

*"No requerido en TP2, pero si alguno implementa un decorador: usar `@functools.wraps` para no perder el nombre y el docstring de la función decorada."*

→ **Transición:** *"Conectamos todo con el TP2."*

---

### [F-69] HOF en el contexto del TP2
**⏱ 2:06 – 2:10 | T2-B**

Leer la tabla de scripts y HOF relevante.  
*"En `funciones_ord.py`, el enunciado pide funciones que reciben otras funciones como argumento — exactamente las HOF que vimos."*

Tipear el patrón recomendado del slide:
```python
notas_aprobadas = list(filter(lambda n: n >= 70, [85, 65, 90, 55, 72]))
```

→ **Transición:** *"Cierre T2-B."*

---

### [F-70] Cierre T2-B
**⏱ 2:10 – 2:12 | T2-B**

Leer los seis puntos del resumen brevemente.  
Mencionar: *"Los decoradores se profundizan en el Módulo III con `@app.route()` de FastAPI."*

→ **PAUSA 5 min antes de T2-C.**

---

## BLOQUE T2-C — Type Hints Python 3.10+

---

### [F-71] ¿Qué son los type hints?
**⏱ 2:17 – 2:21 | T2-C**

Mostrar los dos bloques del slide lado a lado.  
*"El segundo bloque no ejecuta más rápido que el primero. La diferencia es comunicación: con type hints, cualquiera que lea la función sabe qué tipos espera y qué devuelve — sin ejecutarla."*

Preguntar: *"¿Python valida los type hints en runtime?"* → No. Solo Pylance/Ruff en el editor y CI los detectan.

→ **Transición:** *"¿De dónde vienen? Cronología rápida."*

---

### [F-72] PEP 484 + evolución reciente
**⏱ 2:21 – 2:25 | T2-C | ⚠️ SLIDE CRÍTICO**

Leer la tabla señalando las dos filas más importantes:  
- **PEP 585 (3.9):** `list[int]` en lugar de `typing.List[int]`  
- **PEP 604 (3.10):** `X | Y` en lugar de `Union[X, Y]`

*"Si Copilot les genera `from typing import List, Dict`, está usando Python 3.8. En 3.10+ no se necesita. Ruff puede marcarlo como deprecado con la regla UP006."*

→ **Transición:** *"Cómo anotar parámetros, retorno y variables."*

---

### [F-73] Tipos básicos y anotaciones de variable
**⏱ 2:25 – 2:29 | T2-C | 🔵 LIVE CODING**

Tipear la función `calcular_promedio` del slide con la anotación de variable:
```python
notas: list[int] = [85, 72, 91]
```

Demostrar que Python no valida en runtime:
```python
nombre: int = "Ada"  # Python ejecuta sin error
# Pylance lo marca en rojo inmediatamente
```

→ **Transición:** *"Colecciones tipadas."*

---

### [F-74] Colecciones con tipos
**⏱ 2:29 – 2:33 | T2-C | 🔵 LIVE CODING**

Tipear los 4 ejemplos del slide. Enfatizar la diferencia:  
- `list[str]` → lista de strings  
- `dict[str, int]` → dict con claves string y valores int  
- `tuple[float, float]` → tupla de exactamente 2 floats  
- `set[str]` → conjunto de strings

Mostrar la firma del TP2:
```python
def agrupar_por_aprobacion(
    notas: dict[str, int]
) -> dict[str, list[str]]:
```

→ **Transición:** *"`X | None` — la forma moderna de manejar ausencia."*

---

### [F-75] X | None — la forma moderna de Optional
**⏱ 2:33 – 2:37 | T2-C | 🔵 LIVE CODING**

Mostrar la diferencia entre `Optional[str]` y `str | None`.  
Tipear la función del slide:
```python
def buscar_alumno(legajo: int) -> str | None:
    alumnos = {1234: "Ana García", 5678: "Bob Rodríguez"}
    return alumnos.get(legajo)
```

*"Si el legajo no existe, `.get()` devuelve `None`. El type hint `str | None` documenta ese contrato explícitamente."*

→ **Transición:** *"`Union` y `Any`."*

---

### [F-76] Union y Any
**⏱ 2:37 – 2:40 | T2-C**

Tipear `procesar_id(id: int | str)` brevemente.  
Sobre `Any`: *"Es el 'no me importa el tipo'. Úsenlo como último recurso — si pueden ser más específicos, sean más específicos."*

*"En el TP2 probablemente no necesiten `Any`. Si lo ven en código que Copilot genera, es una señal de que el prompt no fue lo suficientemente específico."*

→ **Transición:** *"Retornos complejos."*

---

### [F-77] Anotaciones de retorno complejas
**⏱ 2:40 – 2:43 | T2-C**

Tipear `dividir` con retorno `tuple[int, int]`:
```python
def dividir(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b
```

Y la función sin retorno:
```python
def registrar_error(mensaje: str) -> None:
    print(f"[ERROR] {mensaje}")
```

*"`-> None` es obligatorio en el TP2 para funciones que no devuelven nada. Ruff lo puede verificar."*

→ **Transición:** *"`Callable` — para funciones que reciben funciones."*

---

### [F-78] Callable — tipar funciones como argumento
**⏱ 2:43 – 2:47 | T2-C | ⚠️ OPCIONAL SI EL TIEMPO APRIETA**

Tipear `aplicar_a_todos` del slide.  
*"Leen `Callable[[int], int]` como: 'función que recibe un int y devuelve un int'. En el TP2 con `funciones_ord.py`, van a implementar funciones que reciben otras funciones — este es su tipo."*

Si el tiempo aprieta: *"Está en la guía de estudio Parte 6 con ejemplos."*

→ **Transición:** *"El pipeline completo de calidad."*

---

### [F-79] Ruff + type hints en TP2
**⏱ 2:47 – 2:51 | T2-C | 🔵 DEMO**

**Hacer en vivo:** Mostrar el pipeline completo en el Codespace:
```bash
ruff check src/
pytest tests/ -v
```

*"En la pestaña Actions del repo de GitHub Actions van a ver exactamente estos 2 pasos. Si uno falla, el commit queda marcado en rojo."*

→ **Transición:** *"Resumen ejecutivo de type hints."*

---

### [F-80] Cierre T2-C
**⏱ 2:51 – 2:54 | T2-C**

Leer las 4 reglas y el cheat sheet.  
*"Estas 4 reglas son todo lo que necesitan para el TP2. El cheat sheet está en la guía de estudio — Parte 7."*

→ **PAUSA 5 min antes de T2-D.**

---

## BLOQUE T2-D — Prompting para Debugging

---

### [F-81] Mostrar el traceback a Copilot
**⏱ 2:59 – 3:04 | T2-D | 🔵 DEMO CLAVE**

**Provocar el error en vivo:** En el Codespace, escribir en calculadora.py:
```python
resultado = dividir(10, 0)
```
Ejecutar. Mostrar el traceback completo en terminal.

Construir el prompt del slide **en tiempo real** en un archivo de texto, nombrando cada sección:
- *Role* → quién es el asistente  
- *Contexto* → el código y el error exacto  
- *Tarea* → qué explique y cómo arreglarlo  
- *Restricción* → sin try/except todavía  

Copiar el prompt a ChatGPT/Copilot Chat y mostrar la respuesta.

→ **Transición:** *"El prompt para entender código que IA generó."*

---

### [F-82] Prompt para explicación línea a línea
**⏱ 3:04 – 3:09 | T2-D | 🔵 DEMO**

Mostrar el prompt del slide en pantalla.  
*"Este es el prompt para la sección 'Comprensión línea a línea' del PROMPTS.md. La restricción 'sin asumir que entiendo la indexación negativa' es importante — fuerza a explicar `serie[-1]` desde cero."*

Demostrar enviando el prompt y mostrando que la respuesta explica línea a línea.

*"Eso es exactamente lo que esperamos en el PROMPTS.md para el 20% del puntaje."*

→ **Transición:** *"Refactoring con IA."*

---

### [F-83] Prompt para refactoring + type hints
**⏱ 3:09 – 3:14 | T2-D | 🔵 DEMO**

Mostrar el código mal formateado del slide:
```python
def temp_convert(t, unit):
    if unit == 'C':
        return t * 9/5 + 32
    return (t - 32) * 5/9
```

Enviar el prompt del slide a Copilot Chat. Mostrar que la respuesta incluye:
- Nombres descriptivos
- Type hints completos
- Docstring Google format
- Validación del parámetro `unit`

*"El truco de 'No cambiar la lógica' en las restricciones evita que Copilot reescriba el algoritmo cuando solo queremos mejorar la forma."*

→ **Transición:** *"Cierre del Módulo I."*

---

### [F-84] Cierre Módulo I — Preview Módulo II
**⏱ 3:14 – 3:20 | T2-D**

Señalar los tres puntos del resumen del slide.

**Conexión clave — decir textualmente:**  
*"Los tests del TP2 que corrieron para que el CI se ponga verde — esos tests siguen el patrón Red→Green→Refactor del TDD. Estuvieron haciendo TDD sin saberlo. En el Módulo II vamos a aprender a escribir esos tests desde cero."*

Proyectar el deadline del TP2:  
*"Semana 4, lunes 23:59. El link es `classroom.github.com/a/X4xiTEDQ`. Dos semanas desde ahora."*

Dejar 5-10 min para preguntas finales.

---

## DESPUÉS DE LA SESIÓN

- Registrar dudas recurrentes para ajustar guía de estudio
- Verificar cuántos alumnos aceptaron el TP2 (GitLens en el repo plantilla)
- Actualizar `_edu-memory/calibracion-simulador/tema-01-calibracion.yaml` con observaciones de la clase
