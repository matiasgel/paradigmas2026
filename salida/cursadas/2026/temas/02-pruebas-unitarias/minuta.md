# Minuta de Clase — Módulo II: Pruebas Unitarias
## Laboratorio de Programación y Lenguajes (IF009) — UNTDF 2026
**Semanas 4–5 · 2 sesiones teóricas × 180 min**
*Generada por: Dr. Roberto (class-writer) — 15/04/2026*

> **Cómo usar esta minuta:** cada sección corresponde a una filmina de `filminas.md`.  
> El código de filmina `[F-XX]` es el mismo en ambos archivos.  
> Esta minuta es **autocontenida** — no es necesario abrir otros archivos para dar la clase.
>
> **Ritmo:** presentación rápida — promedio **3–4 min por filmina**.  
> Los tiempos indicados son orientativos; el docente puede ajustar en el momento.  
> Semana 4: 31 slides · Semana 5: 27 slides.

---

## SEMANA 4 — SESIÓN TEÓRICA (180 min)

---

### [F-00] Portada — Semana 4

**Tiempo:** 2 min  
**Qué decir:**  
> "Buen día a todos. Módulo II: Pruebas Unitarias. Dos semanas donde el objetivo concreto es que al final estén escribiendo tests en Python antes de escribir código. Hoy vamos a ver el framework `unittest` que viene incluido en Python — sin instalar nada extra."

**Transición:** Mostrar la agenda del día ([F-01]).

---

### [F-01] Agenda del día

**Tiempo:** 3 min  
**Qué decir:**  
> "Arrancamos con un repaso de POO porque `unittest` usa herencia y si no tienen fresco el modelo de objetos se van a perder. Después vamos a ver por qué testear con casos reales — y cuando digo reales, digo muertes y millones de dólares. Luego el framework. Luego TDD. Y cerramos con el ejercicio que hacen en la práctica de hoy."

**Puntos a enfatizar:**
- La pausa está en el medio del bloque T2 — respetarla
- La práctica de hoy (Kata FizzBuzz + Agenda) es extensión directa de esta teórica

**Transición:** "Empezamos con el repaso de POO — ¿quién me dice qué es un método `__init__`?"

---

## BLOQUE T0 — REPASO POO (30 min total)

---

### [F-02] Repaso: clases e instancias

**Tiempo:** 3 min  
**Formato:** Código en vivo — tipear el ejemplo de la filmina desde cero en el IDE  
**Qué decir:**  
> "La clase `Agenda` que vamos a usar en toda la práctica de hoy. Fíjense que implementa `__eq__` y `__str__`. ¿Por qué `__eq__`? Porque cuando usemos `assertEqual(agenda1, agenda2)`, Python va a llamar a este método. Sin `__eq__` estamos comparando identidad de objetos, no estado."

**Preguntas anticipadas:**
- *"¿Qué pasa si no implemento `__eq__`?"* → Respuesta: `assertEqual(a1, a2)` falla aunque tengan los mismos datos, porque compara `id()`.
- *"¿`__str__` es obligatorio?"* → No, pero hace los mensajes de error mucho más legibles.

**Concepto clave:** `__eq__` es necesario para `assertEqual` cuando se comparan instancias.

**Transición:** "Ahora herencia — porque `TestCase` es una clase que vamos a heredar en unos minutos."

---

### [F-03] Repaso: herencia y super()

**Tiempo:** 3 min  
**Formato:** Código en vivo — extender el ejemplo de `Agenda` con una excepción propia  
**Qué decir:**  
> "Creo una excepción propia para la Agenda — `DNIInvalidoError` que hereda de `ValueError`. Por qué esto importa: cuando ustedes hagan `with self.assertRaises(ValueError)` en los tests, va a atrapar también `DNIInvalidoError` porque es una subclase. Eso puede ser un comportamiento deseado o no — es una decisión de diseño."

**Preguntas anticipadas:**
- *"¿Por qué heredar de `Exception` y no crear una clase sola?"* → Para poder usar `except Exception` o `except Error` en el código que llama.

**Concepto clave:** La herencia de `unittest.TestCase` es el mismo patrón — mi clase `AgendaTest` IS-A `TestCase`.

**Transición:** "¿Cuándo tiene sentido hacer que una excepción sea tan específica? Cuando quien la usa necesita distinguirla de otras. Sigamos."

---

### [F-04] Repaso: excepciones propias

**Tiempo:** 3 min  
**Formato:** Código en vivo — mostrar el método `agregar` con validaciones  
**Qué decir:**  
> "Acá está el código que vamos a testear en la práctica. Fíjense la validación del DNI: `not dni.isdigit()` atrapa letras, espacios, guiones. `not (7 <= len(dni) <= 8)` atrapa DNIs muy cortos o muy largos. Cuando escribamos los tests, vamos a necesitar un caso para cada una de estas condiciones."

**Preguntas anticipadas:**
- *"¿`isdigit()` acepta negativos?"* → No, `-123` no pasa `isdigit()`. Eso es intencional para un DNI.

**Transición:** "Un método más de repaso antes de pasar a los tests."

---

### [F-05] Métodos especiales útiles para tests

**Tiempo:** 3 min  
**Formato:** Tabla en filmina — no tipear, explicar cada fila  
**Qué decir:**  
> "Esta tabla la tienen en la filmina. No la memoricen ahora — vuelvan a ella cuando estén escribiendo tests y el mensaje de error sea incomprensible. `__repr__` es especialmente útil: aparece en la traza de unittest cuando un test falla. Si `__repr__` dice `<Agenda object at 0x...>` no te dice nada. Si dice `Agenda(contactos=2)` sí."

**Concepto clave:** Invertir 5 minutos en `__eq__` y `__str__` ahorra horas de debugging de tests.

**Transición:** "Bien. Tienen fresco el modelo de objetos. Ahora vamos a hablar de por qué es crítico testear el código — y lo vamos a hacer con casos reales."

---

## BLOQUE T1 — MOTIVACIÓN: POR QUÉ TESTAR (40 min total)

---

### [F-06] Errores (slide impacto)

**Tiempo:** 1 min  
**Qué decir:**  
> "Una sola palabra." [silencio] "Errors."

**Nota:** Efecto dramático — pausa de 10 segundos después de mostrar la filmina antes de hablar.

**Transición:** Pasar directamente a [F-07].

---

### [F-07] Air China 140 — 1994

**Tiempo:** 4 min  
**Qué decir:**  
> "26 de abril de 1994. El vuelo 140 de Air China va de Nagoya, Japón, a Osaka. El avión ya había aterrizado en Nagoya antes — el software del piloto automático había funcionado. Pero en este vuelo, bajo una combinación específica de entradas que nunca fue testeada, el piloto automático se desactivó durante el descenso sin aviso claro. La tripulación no detectó el cambio a tiempo. Impacto contra el suelo. 264 muertos."

> "Hay un patrón acá: el software 'funcionaba' en todos los escenarios que habían testeado."

**Pregunta para el grupo:** *"¿Qué tendría que haber hecho el equipo de testing para evitar esto?"*  
→ Respuesta esperada: testear combinaciones de estado del piloto automático + condiciones de descenso.

**Transición:** "Ese es un caso de falla en aviónica. Veamos uno médico."

---

### [F-08] Therac-25 — 1985-1987

**Tiempo:** 4 min  
**Qué decir:**  
> "El Therac-25 era una máquina de radioterapia de los 80s. Versión anterior: Therac-20. El equipo reutilizó código del Therac-20 — les pareció que funcionaba, ¿para qué re-testear?"

> "El problema: la Therac-20 tenía bloqueos de hardware que la Therac-25 no tenía. El software asumía que esos bloqueos existían. Bajo ciertas condiciones de carrera de interfaz — que solo ocurrían si el operador escribía rápido en secuencia específica de teclas — la máquina emitía 100 veces más radiación de lo normal. 4 muertes. Al menos 3 heridos graves con quemaduras severas."

> "El error era intermitente. A veces ocurría, a veces no. Eso lo hace especialmente traicionero."

**Pregunta para el grupo:** *"¿Este error es de caja negra o caja blanca?"*  
→ Respuesta: caja blanca — la condición de carrera solo podía descubrirse conociendo la estructura interna del código.

**Preguntas anticipadas:**
- *"¿Cómo se descubrió?"* → Los pacientes reportaron sensaciones de quemadura. Los logs decían "error de malfunction 54" — sin descripción. Tomó dos años identificar la causa raíz.

**Transición:** "Un caso espacial."

---

### [F-09] Ariane 5 — 1996

**Tiempo:** 4 min  
**Qué decir:**  
> "4 de junio de 1996. El Ariane 5 era el cohete más caro y esperado de la ESA. Primer vuelo. 37 segundos después del despegue se auto-destruye."

> "La causa: reutilizaron el módulo de referencia inercial del Ariane 4. Ese módulo tenía código que convertía un número de punto flotante de 64 bits a un entero de 16 bits. En el Ariane 4, ese número nunca excedía el rango de 16 bits. El Ariane 5 es más rápido — el número excedía el rango y producía overflow."

> "El análisis de seguridad del código del Ariane 4 concluía: 'Este valor no puede exceder el rango'. Correcto para el Ariane 4. Incorrecto para el Ariane 5."

> "370 millones de dólares en 37 segundos. Y lo más irónico: el código que falló no era el código de vuelo activo — era un módulo de alineación que ni siquiera se usaba durante el vuelo."

**Pregunta para el grupo:** *"¿Qué tipo de prueba habría detectado esto?"*  
→ Prueba de regresión con los nuevos parámetros del Ariane 5 + prueba de borde en los valores máximos.

**Transición:** "¿Qué tienen en común estos tres casos?"

---

### [F-10] ¿Qué tienen en común?

**Tiempo:** 3 min  
**Formato:** Socrático — preguntar antes de mostrar la respuesta  
**Qué decir:**  
> "Les pregunto a ustedes: ¿qué tienen en común Air China, Therac-25 y Ariane 5? [Esperar respuestas del grupo]"

> "Exacto. Los tres tenían software que 'funcionaba'. Los tres pasaron por ingenieros profesionales. Los tres fallaron porque no se testearon los casos de borde ni el comportamiento bajo condiciones nuevas."

> "Esta es la definición de testing que vamos a usar en el módulo: [leer la definición de la filmina]. No es un proceso para confirmar que funciona. Es un proceso para **encontrar los casos donde no funciona**."

**Concepto clave:** Testing es una actividad de falsificación — buscamos demostrar que el código falla.

**Transición:** "Bien. Ahora clasificamos: ¿qué tipos de tests existen?"

---

### [F-11] Caja Negra vs Caja Blanca

**Tiempo:** 3 min  
**Qué decir:**  
> "Caja negra: pruebo entradas y salidas sin mirar el código. Para la clase Agenda: doy DNI 'abc', espero `ValueError`. No me importa cómo está implementada la validación."

> "Caja blanca: miro el código y diseño tests para cubrir ramas específicas. Veo que la condición es `len(dni) < 7`. Entonces creo un test con DNI de 6 dígitos — exactamente en el borde de la condición."

> "En la práctica de hoy van a hacer las dos cosas. Los primeros tests que escriban van a ser caja negra. Cuando quieran asegurarse de cubrir los límites — van a cambiar a caja blanca."

**Transición:** "¿Y a qué nivel pertenecen los tests que vamos a escribir hoy?"

---

### [F-12] Pirámide de niveles de testing

**Tiempo:** 3 min  
**Qué decir:**  
> "La pirámide de testing. Base ancha: tests unitarios — rápidos, baratos, muchos. Cima: tests de aceptación — lentos, caros, pocos."

> "Hoy trabajamos en el Nivel 1. Los tests de la clase Agenda son unitarios: prueban una clase en aislamiento. No conectan a una BD real, no hacen requests HTTP, no dependen del sistema de archivos."

> "La definición de las filminas 2025 para este nivel: [leer de la filmina]. Lo que cambia en 2026: también vamos a aprender a aislar dependencias cuando el código que queremos testear sí toca el disco o la red — eso es lo que hace `unittest.mock`."

**Preguntas anticipadas:**
- *"¿Cuándo hacemos Nivel 2?"* → En Módulo III con Django — testear que una vista devuelve el HTML correcto ya es integración.

**Transición:** "Un concepto más y pasamos al framework."

---

### [F-13] Pruebas de regresión

**Tiempo:** 3 min  
**Qué decir:**  
> "Prueba de regresión: re-ejecutar el suite completo después de cada cambio. El Ariane 5 falló por no hacer esto."

> "Con TDD esto es automático: cada vez que modifican código, ejecutan `python -m unittest discover`. Si todos pasan, el cambio no rompió nada. Si alguno falla, saben exactamente qué cambio causó el problema — porque acaban de hacer un cambio."

> "Esta es la razón por la que TDD da confianza para refactorizar. La red de seguridad es el suite de tests."

**Transición:** "Ahora sí — el framework. `unittest`."

---

## BLOQUE T2 — FRAMEWORK UNITTEST (40 min total)

---

### [F-14] La familia xUnit

**Tiempo:** 3 min  
**Qué decir:**  
> "Kent Beck, 1989. Smalltalk era el lenguaje más avanzado de la época en diseño orientado a objetos. Beck crea SUnit para Smalltalk — el primer framework de pruebas unitarias moderno."

> "En 1997, Beck y Gamma lo portan a Java: JUnit. Hoy JUnit tiene 200 millones de descargas al mes. En 2001, Steve Purcell porta JUnit a Python: `unittest`. Está en la stdlib desde Python 2.1."

> "¿Por qué importa la historia? Porque van a ver el mismo patrón en todos los lenguajes: clase de test que hereda de una clase base, métodos `setUp`/`tearDown`, ejecución por discovery. Una vez que entienden `unittest`, entienden JUnit, NUnit, RSpec."

**Transición:** "Los tres conceptos centrales."

---

### [F-15] TestCase · TestSuite · TestRunner

**Tiempo:** 3 min  
**Qué decir:**  
> "TestCase: la unidad de organización de tests. Hereden de `unittest.TestCase` y cada método `test_*` es un caso de prueba."

> "TestSuite: una colección de TestCases. Raramente la crean a mano — el runner la construye automáticamente por discovery."

> "TestRunner: el ejecutor. `python -m unittest` es el runner por defecto. Muestra el resultado en la terminal. En CI (GitHub Actions) el runner lee el código de salida — 0 si todos pasan, 1 si alguno falla."

**Transición:** "Código. Mi primer test."

---

### [F-16] Mi primer test

**Tiempo:** 3 min  
**Formato:** Código en vivo — tipear desde cero, ejecutar en la terminal  
**Qué decir:**  
> "Abro un archivo `test_primera.py`. Importo `unittest`. Creo una clase que hereda de `unittest.TestCase`."

> [Tipear el ejemplo de la filmina]

> "Ejecuto: `python -m unittest -v test_primera.py`. Los métodos `test_suma` y `test_tipo` aparecen separados. Cada uno pasa o falla de forma independiente."

> "Ahora lo rompo: cambio `assertEqual(resultado, 4)` por `assertEqual(resultado, 5)`. Ejecuto de nuevo. Vean el mensaje de error: `AssertionError: 4 != 5`. Eso es útil. Si hubiera usado `assertTrue(resultado == 5)`, el mensaje sería `AssertionError: False is not true` — completamente inútil."

**Concepto clave:** Usar las aserciones semánticas (`assertEqual`, etc.) en lugar de `assertTrue(a == b)`.

**Transición:** "La tabla de aserciones disponibles."

---

### [F-16b] Leer el output de un test fallido

**Tiempo:** 2 min  
**Formato:** Filmina — recorrer el output de arriba a abajo  
**Qué decir:**  
> "FAIL = la aserción no se cumplió. ERROR = excepción no esperada — un bug en el código, no en el test. Con `-v` ven el nombre de cada test. Empiecen a leer siempre desde la línea del `AssertionError` — les dice exactamente qué valor esperaban y qué obtuvieron."

**Transición:** "Tabla de aserciones."

---

### [F-17] Aserciones esenciales

**Tiempo:** 3 min  
**Formato:** Tabla en filmina — recorrer las filas más importantes  
**Qué decir:**  
> "Las que más van a usar: `assertEqual`, `assertRaises`, `assertIn`. Memoricen estas tres. Las demás las tienen en la filmina y en la referencia de Python."

> "`assertIn(a, b)` es muy útil para verificar que un elemento está en una lista o diccionario. `assertIsInstance` es útil cuando la función puede retornar tipos distintos según la entrada."

> "Una regla de oro: el mensaje de error de la aserción debe alcanzar para entender qué falló sin abrir el código."

**Transición:** "Las aserciones para colecciones tienen su propio bloque."

---

### [F-17b] Aserciones para colecciones

**Tiempo:** 2 min  
**Formato:** Tabla — recorrer rápido  
**Qué decir:**  
> "`assertCountEqual` verifica mismos elementos sin importar el orden — lo van a usar mucho cuando la Agenda retorne listas. `assertDictEqual` da un diff legible cuando el dict es grande. Las demás las ven en la filmina."

**Transición:** "La aserción más importante para las clases que definimos: `assertRaises`."

---

### [F-18] assertRaises — probar excepciones

**Tiempo:** 4 min  
**Formato:** Código en vivo — tipear ambas variantes  
**Qué decir:**  
> "Cómo verifico que mi código lanza `ValueError` cuando le doy un DNI inválido."

> [Tipear la variante con context manager]

> "El `with self.assertRaises(ValueError):` crea un contexto. Todo lo que ocurra dentro de ese bloque se monitorea. Si `ValueError` se lanza — el test pasa. Si no se lanza — el test falla con `AssertionError: ValueError not raised`."

> "La segunda variante: capturo la excepción en `ctx` y verifico el mensaje. Útil cuando quiero asegurarme de que el error describe correctamente qué salió mal."

**Preguntas anticipadas:**
- *"¿Puedo usar `assertRaises` con `try/except`?"* → No es necesario — `assertRaises` ya lo hace. Mezclar los dos complica el test.
- *"¿Qué pasa si el código lanza un error diferente, por ejemplo `TypeError`?"* → El test falla con el `TypeError` propagándose — es un resultado de fallo diferente a `AssertionError`.

**Transición:** "Ahora, el código que se repite en cada test: los fixtures."

---

### [F-19] Fixtures: setUp y tearDown

**Tiempo:** 4 min  
**Formato:** Código en vivo — escribir la clase `AgendaTest` con setUp  
**Qué decir:**  
> "`setUp` se llama antes de **cada** test. Cada test recibe un estado limpio. Esto es fundamental: los tests no deben depender del orden de ejecución ni del estado que dejó el test anterior."

> [Tipear el ejemplo de la filmina]

> "¿Por qué `del self.agenda` en `tearDown`? En este caso no es estrictamente necesario porque Python garbage-collect los objetos al terminar el método. Pero para recursos que manejan conexiones a BD o archivos abiertos, sí es crítico cerrarlos en `tearDown` — porque `tearDown` se ejecuta **incluso si el test falla**."

**Preguntas anticipadas:**
- *"¿Por qué `setUp` en minúscula pero `TestCase` con mayúscula?"* → Convención heredada de Java/Smalltalk. Los métodos de configuración son snake_case, las clases PascalCase.

**Transición:** "Ejecutamos los tests desde la terminal."

---

### [F-19b] Orden de ejecución garantizado

**Tiempo:** 2 min  
**Formato:** Diagrama en filmina — apuntar las flechas  
**Qué decir:**  
> "El orden es siempre: setUpClass una vez, setUp antes de cada test, tearDown después de cada test, tearDownClass al final. El orden entre tests no está garantizado — por eso cada setUp debe dejar un estado completamente limpio e independiente."

**Transición:** "CLI."

---

### [F-20] Ejecución CLI

**Tiempo:** 3 min  
**Formato:** Terminal en vivo — mostrar los comandos  
**Qué decir:**  
> "`python -m unittest -v test_agenda.py` — el `-v` (verbose) muestra el nombre completo de cada test. En CI van a ver exactamente qué test falló."

> "`python -m unittest discover` — busca todos los archivos que matcheen `test*.py` en el directorio actual. Eso es lo que va a correr GitHub Actions en el TP 3."

> "Vean la salida: `Ran X tests in Y.YYYs`. Si todos pasan: `OK`. Si alguno falla: `FAILED (failures=N)`."

**⏸️ PAUSA (10 min)**

---

## BLOQUE T3 — TDD (30 min total)

---

### [F-21] ¿Qué es TDD?

**Tiempo:** 3 min  
**Qué decir:**  
> "Test-Driven Development. La misma persona que inventó SUnit y JUnit — Kent Beck — formalizó esta metodología en 2002."

> "La idea es contraintuitiva: escribís el test antes de tener el código que lo hace pasar. El test define el comportamiento esperado. El código es la implementación de esa especificación."

> "¿Por qué esto mejora el diseño? Porque para escribir un test, necesitás pensar en cómo se va a usar el código — la API pública, los casos de error, los valores de retorno. Eso te fuerza a diseñar la interfaz antes de la implementación."

**Transición:** "El ciclo tiene tres pasos."

---

### [F-22] El ciclo Red → Green → Refactor

**Tiempo:** 3 min  
**Qué decir:**  
> "Rojo: escribís el test. Lo ejecutás. Debe fallar — si pasa sin código, hay algo mal."

> "Verde: escribís el mínimo código posible para hacer pasar el test. No optimizés, no generalicés todavía. 'Fake it till you make it' — si el test dice que `fizzbuzz(3)` retorna `'Fizz'`, podés escribir `return 'Fizz'` y el test va a pasar. Eso está bien por ahora."

> "Azul/refactor: mejorar el código con los tests como red de seguridad. Type hints, nombres mejores, eliminar duplicación. Los tests siguen en verde."

> "El ciclo completo debería durar entre 2 y 10 minutos. Ciclos cortos, cambios pequeños, feedback constante."

**Transición:** "Lo hacemos en vivo con FizzBuzz."

---

### [F-23] Demo FizzBuzz — 🔴 RED

**Tiempo:** 7 min  
**Formato:** Código en vivo — tipear el test, ejecutarlo, mostrar el error  
**Qué decir:**  
> "Abro `test_fizzbuzz.py`. Escribo solo el primer test: `test_tres_retorna_fizz`."

> [Tipear el test]

> "Ejecuto sin haber definido `fizzbuzz` todavía."

> "`NameError: name 'fizzbuzz' is not defined`. ¿Es esto un fracaso? **No. Es exactamente lo que queremos.** El test está fallando porque no existe el código. Confirmado: el test mide algo real."

**Concepto clave:** Un test que pasa sin código es un test que no sirve para nada.

**Transición:** "Ahora hago el mínimo para pasar."

---

### [F-24] Demo FizzBuzz — 🟢 GREEN

**Tiempo:** 4 min  
**Formato:** Código en vivo — escribir la función, agregar más tests, implementar completo  
**Qué decir:**  
> "Mínimo código: `return 'Fizz'`. Ejecuto. Pasa. Verde."

> "Ahora agrego `test_cinco_retorna_buzz`. Ejecuto. Falla — porque `return 'Fizz'` no funciona para 5. Implemento un poco más."

> [Repetir el ciclo 3 veces hasta llegar a la implementación completa]

> "¿Ven el patrón? Cada test nuevo me fuerza a agregar funcionalidad real. En ningún momento estoy sobre-implementando — implemento exactamente lo que los tests especifican."

**Transición:** "Refactor."

---

### [F-25] Demo FizzBuzz — 🔵 REFACTOR

**Tiempo:** 3 min  
**Formato:** Código en vivo — mejorar la función, ejecutar tests para verificar  
**Qué decir:**  
> "Ahora que los 4 tests pasan, mejoro el código. Agrego type hints, docstring, cambio el orden de los if para manejar el caso 15 primero."

> "Ejecuto después de cada cambio: `python -m unittest -v test_fizzbuzz.py`. Siempre verde."

> "Los tests documentan la especificación. Si alguien lee los tests de `FizzBuzzTest`, saben exactamente qué hace `fizzbuzz` — sin leer la implementación."

**Transición:** "Esto es lo que van a hacer en la práctica de hoy con la clase Agenda."

---

## BLOQUE T4 — CIERRE SEMANA 4 (20 min)

---

### [F-26] Ejercicio integrador — Clase Agenda

**Tiempo:** 6 min  
**Qué decir:**  
> "El ejercicio de la práctica viene directamente de las filminas del año pasado — mismo enunciado base."

> "La diferencia en 2026: aplican TDD. Primero escriben los tests de `agregar` y `buscar`. Luego implementan la clase hasta que los tests pasen."

> "En la filmina tienen la especificación completa. Para cada método, qué debe hacer y qué tests escribir. Para la práctica de hoy: `__init__`, `agregar` y `buscar`. En la semana 5 completan `eliminar` y `listar`."

> "Una pregunta antes de pasar a la práctica: ¿alguien puede decirme qué diferencia a `KeyError` de `ValueError`?"
> → Respuesta esperada: `ValueError` para valores con formato incorrecto; `KeyError` para claves que no existen en un dict.

**Preguntas anticipadas:**
- *"¿Cómo nombro la clase del test?"* → `AgendaTest` — convención: nombre de la clase bajo prueba + `Test`.
- *"¿Un archivo de test por clase de producción?"* → Sí, como regla general. `test_agenda.py` prueba `agenda.py`.

**Transición:** "Setup de GitHub Classroom TP 3 — lo hacen en la práctica, no ahora."

---

### [F-27] Cierre Semana 4

**Tiempo:** 4 min  
**Qué decir:**  
> "Repaso de lo que vimos hoy."

> [Recorrer el checklist de la filmina — preguntar al grupo por cada ítem antes de marcarlo]

> "Para la práctica de hoy: FizzBuzz en pair programming primero — 60 minutos. Luego Agenda en TDD individual."

> "La semana próxima: `unittest.mock` para aislar dependencias, subtests, y anticipo de `django.test.TestCase`. Todo lo que aprendieron hoy se transfiere directamente a Django."

**Transición:** Derivar al docente de práctica.

---

## SEMANA 5 — SESIÓN TEÓRICA (180 min)

---

### [F-28] Portada — Semana 5

**Tiempo:** 2 min  
**Qué decir:**  
> "Semana 5. Arrancamos con una pregunta: ¿qué hacen cuando el código que quieren testear depende de una base de datos o de una API externa? ¿Conectan la BD de producción en los tests? ¿Esperan respuestas HTTP en cada test?"

**Transición:** "No. Usan mocks. Eso es el primer bloque de hoy."

---

### [F-29] Agenda — Semana 5

**Tiempo:** 2 min  
**Qué decir:**  
> "Hoy cerramos el módulo. Mock, subtests, anticipo de Django, repaso completo y revisión del TP 2."  
> "Al final del módulo: TP 3 abierto en GitHub Classroom — van a estar construyendo una BlogApp con TDD desde la primera línea."

---

### [F-29b] Repaso — semana anterior

**Tiempo:** 3 min  
**Formato:** Socrático — preguntas rápidas al grupo  
**Qué decir:**  
> "Cuatro preguntas rápidas antes de arrancar. [Leer las preguntas de la filmina, esperar 15-20 seg cada una.]"

> "Estado de la Agenda: `agregar` y `buscar` ya están. Hoy en la práctica completan `eliminar` y `listar`."

**Transición:** "¿Qué pasa cuando el código que queremos testear depende de una BD o una API?"

---

## BLOQUE T1 — UNITTEST.MOCK (40 min total)

---

### [F-30] ¿Por qué aislar dependencias?

**Tiempo:** 3 min  
**Qué decir:**  
> "Miren este test. `agenda.guardar_en_db()` conecta a una base de datos real. ¿Qué puede pasar mal?"

> [Leer los bullets de la filmina con el grupo]

> "El último punto es el más importante: si el test falla porque la BD no está disponible, ustedes van a creer que hay un bug en `Agenda.guardar_en_db()`. Pero el bug no está ahí — está en la infraestructura. El test les mintió."

> "La solución: reemplazar la BD real con un objeto falso que simula el comportamiento necesario para el test. Eso se llama un **doble de test** o **mock**."

**Concepto clave:** Un test unitario no debe tener dependencias externas reales.

**Transición:** "Antes del MagicMock — no todos los dobles son iguales."

---

### [F-30b] Test doubles — tipos

**Tiempo:** 2 min  
**Formato:** Tabla — recorrer rápido  
**Qué decir:**  
> "Vocabulario del área: Stub, Mock, Spy, Fake, Dummy. En Python todo el mundo dice 'mock' pero conocer la distinción ayuda a elegir la herramienta correcta. `MagicMock` puede actuar como cualquiera de los cinco según cómo lo configuren."

**Transición:** "El MagicMock."

---

### [F-31] MagicMock — crear un doble

**Tiempo:** 4 min  
**Formato:** Código en vivo — tipear en REPL interactivo primero, luego en archivo  
**Qué decir:**  
> "Importo `MagicMock` de `unittest.mock`. Creo `db_falsa = MagicMock()`."

> "Llamo `db_falsa.guardar(...)`. No lanza error. `MagicMock` acepta cualquier atributo y cualquier método — es un espejo vacío que dice sí a todo."

> "Pero también registra lo que recibió. `db_falsa.guardar.assert_called_once()` — verifica que fue llamado exactamente una vez. Si no fue llamado, falla."

> "Y puedo configurar valores de retorno: `db_falsa.buscar.return_value = {'nombre': 'Juan'}`. Ahora cuando el código bajo prueba llame a `db_falsa.buscar(...)`, va a recibir ese dict — sin tocar ninguna BD."

**Preguntas anticipadas:**
- *"¿MagicMock vs Mock?"* → `MagicMock` también implementa los métodos especiales (`__len__`, `__str__`, `__iter__`, etc.). Para la mayoría de los casos usen `MagicMock`.

**Transición:** "Cómo verificamos que el mock fue llamado como esperábamos."

---

### [F-31b] MagicMock — verificar llamadas

**Tiempo:** 3 min  
**Formato:** Código en vivo — ejecutar los assert_called en REPL  
**Qué decir:**  
> "`assert_called` — fue llamado. `assert_called_once` — exactamente una vez. `assert_called_with` — última llamada con estos args. `call_args_list` — historial completo. Si el mock fue llamado dos veces y usan `assert_called_once`, falla."

**Transición:** "Cómo configuramos qué devuelve el mock."

---

### [F-31c] return_value y side_effect

**Tiempo:** 3 min  
**Formato:** Código — ejecutar ejemplos  
**Qué decir:**  
> "`return_value` es el valor que siempre retorna. `side_effect` puede lanzar excepciones o retornar valores distintos por llamada en secuencia — `side_effect = [val1, val2, KeyError()]`. Si configuran los dos, `side_effect` gana."

**Transición:** "Ahora el patch — cómo reemplazamos dependencias que el código instancia internamente."

---

### [F-32] patch — reemplazar en contexto

**Tiempo:** 4 min  
**Formato:** Código en vivo — tipear el ejemplo de `open()`  
**Qué decir:**  
> "El método `Agenda.guardar()` llama a `open()` internamente — no lo recibe como argumento. No podemos pasarle un doble directamente."

> "`patch('builtins.open', mock_open())` reemplaza la función `open` del namespace `builtins` por un doble — pero **solo dentro del bloque `with`**. Al salir del bloque, `open` vuelve a ser la función real."

> "Esto garantiza que los tests no interfieren entre sí. Cada test tiene su propio contexto de patch."

> [Tipear el ejemplo, ejecutar, mostrar el resultado]

**Preguntas anticipadas:**
- *"¿El path del patch es el módulo donde está `open`, no donde está mi clase?"* → Sí, hay que patchear donde se usa la función, no donde está definida. Eso es una confusión muy común — si `agenda.py` hace `import os` y usa `os.path.exists`, patchean `agenda.os.path.exists`, no `os.path.exists`.

**Transición:** "Una slide crítica: ¿qué path pongo en patch?"

---

### [F-32b] ¿Qué path pongo en patch?

**Tiempo:** 3 min  
**Formato:** Filmina — comparar incorrecto vs correcto  
**Qué decir:**  
> "La confusión más común: parchean `json.dump` pero `agenda.py` ya importó `json` en su namespace. El patch tiene que ir donde se usa, no donde está definido. Si `agenda.py` hace `import json`, el path correcto es `agenda.json.dump`."

**Preguntas anticipadas:**
- *"¿Cómo lo encuentro si no sé el path?"* → Mirar el `import` al inicio del módulo bajo prueba — ese es el namespace.

**Transición:** "El patch como decorador — la otra sintaxis."

---

### [F-33] patch como decorador

**Tiempo:** 3 min  
**Formato:** Código en vivo — convertir el ejemplo anterior a decorador  
**Qué decir:**  
> "La diferencia es dónde se activa el patch: el decorador lo activa para todo el método de test. El context manager lo activa solo para el bloque `with`."

> [Tipear la versión con decorador]

> "El mock llega como argumento al método de test — por eso el segundo parámetro `mock_open_obj`. Si patchean múltiples cosas, reciben múltiples argumentos en orden inverso."

> "¿Cuándo uso context manager vs decorador? Mi regla: si el patch cubre todo el test, decorador — es más legible. Si necesito que el patch se active en medio del test, context manager."

**Transición:** "`patch.object` y múltiples patches — dos slides rápidas."

---

### [F-33b] patch.object y múltiples patches

**Tiempo:** 3 min  
**Formato:** Filmina — recorrer ambas secciones  
**Qué decir:**  
> "`patch.object(Clase, 'metodo', return_value=True)` — cuando conocen la clase y quieren parchear un método específico, más legible que el string path. Con múltiples decoradores: el más cercano al método llega como primer argumento — es contra-intuitivo, hay que saberlo de memoria."

**Transición:** "Cambio de tema: subTest y skipping."

---

## BLOQUE T2 — SUBTESTS Y SKIPPING (30 min total)

---

### [F-34] subTest — parametrizar sin duplicar

**Tiempo:** 4 min  
**Formato:** Código en vivo — mostrar el problema primero, luego la solución  
**Qué decir:**  
> "El problema: tengo 5 casos para FizzBuzz. Si escribo 5 métodos `test_*`, el primero que falla detiene los demás — no sé cuántos casos fallaron en total."

> "Con `subTest`: todos los casos se ejecutan aunque alguno falle. El reporte muestra exactamente cuáles fallaron, con el valor de `n` en el mensaje."

> [Tipear el ejemplo de la filmina, ejecutar]

> "Escenario típico: tienen una función de validación con 10 reglas. Con `subTest` escriben un solo método de test con 10 casos — y el reporte les dice exactamente qué reglas no pasan."

**Transición:** "Cómo leer el reporte cuando fallan subtests."

---

### [F-34b] subTest — leer el reporte

**Tiempo:** 2 min  
**Formato:** Filmina — recorrer el output  
**Qué decir:**  
> "El valor del parámetro del subTest (`n=5`) aparece en el nombre del test fallido. No hay que adivinar qué entrada falló — el reporte lo dice explícitamente. `FAILED (failures=2)` con un solo método de test."

**Transición:** "Skipping."

---

### [F-35] Skipping — saltear tests

**Tiempo:** 3 min  
**Formato:** Código en vivo — tipear los ejemplos principales  
**Qué decir:**  
> "`@unittest.skip('razón')` — skipea el test incondicionalmente. Lo usan cuando implementan TDD y escriben los tests de todos los métodos antes de implementar ninguno: todos los tests excepto el primero llevan `@skip`."

> "`@unittest.skipIf(condicion, 'razón')` — skipea si la condición es verdadera. Útil para tests que solo funcionan en ciertos entornos o versiones de Python."

> "`@unittest.expectedFailure` — el test **debe** fallar. Si pasa, se reporta como error inesperado. Útil para documentar bugs conocidos formalmente en el suite."

**Preguntas anticipadas:**
- *"¿Los tests skipeados aparecen en el reporte?"* → Sí, aparecen como `s` (skip) en el conteo. `Ran 5 tests, 2 skipped`.

**Transición:** "@expectedFailure en el workflow TDD — una slide sobre cómo usarlo en práctica."

---

### [F-35b] @expectedFailure en workflow TDD

**Tiempo:** 2 min  
**Formato:** Filmina — recorrer el ejemplo rápido  
**Qué decir:**  
> "Flujo TDD cuando tienen que implementar varios métodos: escriben todos los tests al inicio, los de los métodos pendientes van con `@expectedFailure`. El suite no falla ruidosamente pero los tests documentan qué falta. Cuando implementan `eliminar`, sacan el decorador — el test pasa a correr normalmente."

**Transición:** "Un fixture más: `setUpClass`."

---

### [F-36] setUpClass y tearDownClass

**Tiempo:** 3 min  
**Qué decir:**  
> "`setUpClass` se ejecuta **una sola vez** antes de todos los tests de la clase. Es un `classmethod` — recibe `cls`, no `self`."

> "¿Cuándo lo usan? Para recursos costosos de inicializar: conexiones a BD, carga de archivos grandes, configuración de un servidor de prueba. Si usan `setUp` para eso, pagan el costo de inicialización en **cada test** — puede ser muy lento."

> "La tabla de la filmina: `setUp` para objetos simples, `setUpClass` para recursos externos. La práctica habitual en Módulo II (solo unittest sin BD) es usar `setUp`. En Módulo III con Django lo van a ver en acción."

---

### [F-36b] addCleanup

**Tiempo:** 2 min  
**Formato:** Filmina — comparar con tearDown  
**Qué decir:**  
> "`addCleanup` se registra dentro de `setUp` o del test — se ejecuta siempre al final, incluso si `setUp` falla a la mitad. Pueden encadenar múltiples `addCleanup` — se ejecutan en orden LIFO. Más robusto que `tearDown` cuando `setUp` puede fallar parcialmente."

**Transición:** "Pausa."

**⏸️ PAUSA (10 min)**

---

## BLOQUE T3 — TDD EN BLOGAPP (30 min total)

---

### [F-37] django.test.TestCase — continuidad directa

**Tiempo:** 4 min  
**Qué decir:**  
> "La mejor noticia del módulo: todo lo que aprendieron se transfiere directamente a Django."

> "`django.test.TestCase` hereda de `unittest.TestCase`. Mismos métodos `setUp`/`tearDown`, mismas aserciones `assertEqual`/`assertRaises`, mismo descubrimiento automático con `discover`."

> "Lo que Django agrega: un cliente HTTP de prueba para simular requests, una base de datos de test que se crea al inicio y se destruye al final, rollback automático entre tests para que no se contaminen."

> "En el TP 3 van a tener una clase `PostTest(TestCase)` donde `TestCase` es `from django.test import TestCase`. La diferencia con lo que hicieron en la Agenda es mínima."

**Transición:** "El cliente HTTP de Django para tests."

---

### [F-37b] django.test.Client

**Tiempo:** 3 min  
**Formato:** Filmina — recorrer los tres tests de ejemplo  
**Qué decir:**  
> "`self.client` simula requests HTTP sin tocar la red. `self.client.get('/blog/posts/')` retorna un objeto `response` con `status_code`, `content`, etc. `assertContains` verifica que el string está en el HTML de respuesta. Esto es integración — Nivel 2 de la pirámide. Lo profundizan en Módulo III."

**Transición:** "Cómo se estructura el código de tests en un proyecto Django real."

---

### [F-38] Estructura de tests en Django

**Tiempo:** 3 min  
**Formato:** Árbol de archivos en filmina — explicar cada carpeta  
**Qué decir:**  
> "El estándar en proyectos Django: una carpeta `tests/` dentro de cada app. `__init__.py` vacío para que Python lo trate como paquete. `test_models.py` para pruebas unitarias de modelos. `test_views.py` para pruebas de integración de vistas."

> "El comando: `python manage.py test blog` — descubre todos los archivos `test_*.py` dentro de la app `blog` y los ejecuta."

> "Por debajo, `manage.py test` llama al runner de `unittest`. El mecanismo es exactamente el mismo que `python -m unittest discover`."

**Transición:** "Las opciones útiles de manage.py test."

---

### [F-38b] manage.py test — opciones

**Tiempo:** 2 min  
**Formato:** Filmina — recorrer rápido  
**Qué decir:**  
> "Los que van a usar en el TP 3: `--failfast` para parar en el primer fallo mientras desarrollan, path específico a un método para correr solo el test en el que están trabajando, `--keepdb` para no recrear la BD cada vez."

**Transición:** "Preview TP 3."

---

### [F-39] Preview TP 3

**Tiempo:** 5 min  
**Qué decir:**  
> "TP 3 es una BlogApp en Django. La diferencia con el TP 2: en el TP 2 nosotros escribimos los tests del autograding. En el TP 3, **ustedes** escriben los tests."

> "El repo tiene `blog/models.py` con los modelos a implementar y `blog/tests/test_models.py` con un esqueleto de tests vacíos. La consigna: completen los tests **primero** siguiendo TDD, luego implementen los modelos."

> "El autograding va a correr los tests que ustedes escribieron — y también un suite de tests secreto nuestro. Si sus tests son buenos, el código que implementen también va a pasar el suite secreto."

**Preguntas anticipadas:**
- *"¿Podemos usar pytest en el TP 3?"* → No, solo `unittest` y `django.test.TestCase`. Es la restricción del módulo.

---

## BLOQUE T4 — CIERRE MÓDULO II (30 min total)

---

### [F-40] Repaso Módulo II completo

**Tiempo:** 5 min  
**Formato:** Tabla — recorrer con preguntas al grupo  
**Qué decir:**  
> "Repaso rápido en forma de preguntas. [Leer cada ítem de la tabla, esperar respuesta del grupo antes de confirmar]"

**Transición:** "Test smells — los errores más comunes."

---

### [F-40b] Test smells

**Tiempo:** 3 min  
**Formato:** Tabla — recorrer rápido  
**Qué decir:**  
> "Los patrones que más van a ver — y cometer — en las próximas semanas. El más crítico: el test que nunca falla. Si un test siempre está verde sin importar qué rompen, no sirve para nada. El segundo: nombres genéricos. `test_agenda` no dice nada; `test_agregar_dni_invalido_lanza_ValueError` sí."

**Transición:** "Cierre."

---

### [F-41] Cierre — Módulo II

**Tiempo:** 6 min  
**Qué decir:**  
> [Leer la cita de la filmina lentamente]

> "Esta cita resume por qué los tests no son una garantía de corrección — son una garantía de que el código cumple la especificación que vos escribiste. Si la especificación está incompleta, los tests también lo están."

> "Por eso TDD mejora el diseño: te fuerza a escribir una especificación ejecutable antes de implementar. Los casos de borde que no pensaste antes de implementar — los pensás cuando escribís los tests."

> "Próximas clases: Módulo III — Django MVC. La pirámide de testing cambia: van a tener pruebas de modelos (Nivel 1), pruebas de vistas (Nivel 2) y pruebas de flujo completo (Nivel 3). Todo con las mismas herramientas que usaron hoy."

> "TP 3 ya está en GitHub Classroom. Tienen una semana para el primer ciclo TDD. Cualquier duda en el canal de Discord."

---

## BLOQUE T5 — REVISIÓN TP 2 (25 min)

---

**Tiempo:** 25 min (sin filmina dedicada — proyectar resultados del autograding)

**Qué hacer:**
1. Proyectar el reporte de autograding de GitHub Classroom (resultados por grupo)
2. Mostrar 2-3 patrones de errores comunes encontrados en el TP 2:
   - Tests que pasan por coincidencia (ej: `assertEqual(resultado, None)` cuando la función no retorna nada)
   - Falta de tests de casos de borde
   - Código que hardcodea la respuesta en lugar de implementar la lógica
3. Para cada patrón: mostrar el test que falló y la corrección

**Preguntas anticipadas:**
- *"¿El TP 2 se puede re-entregar?"* → Según la política del docente — aclarar en el momento.
- *"¿Cómo veo mis errores de autograding?"* → En GitHub → Actions → el run fallido → log del paso de tests.

---

*Minuta generada por: Dr. Roberto (class-writer) — 15/04/2026*  
*Para regenerar: `/edu-create-class` en el agente class-writer*  
*Filminas correspondientes: `salida/cursadas/2026/temas/02-pruebas-unitarias/filminas.md`*
