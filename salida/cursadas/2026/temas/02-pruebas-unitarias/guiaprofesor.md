# Guía del Profesor — Módulo II: Pruebas Unitarias

## Laboratorio de Programación y Lenguajes (IF009) — UNTDF 2026

**Tema:** 02 — Pruebas Unitarias  
**Semana:** 4 (1 semana = 6 hs totales)  
**Docente:** Matías Gel  
**Fecha de generación:** 15/04/2026

> **Ajuste de alcance:** el diseño original contemplaba 2 semanas (12 hs). Se comprime a **1 semana** (1 teórica + 1 práctica de 3 hs cada una). Los contenidos de mocking (`unittest.mock`), subtests/skipping y el anticipo de Django quedan como lectura recomendada en la guía de estudio y se retoman orgánicamente al iniciar el Módulo III. El foco de esta semana es: motivación, `unittest` base, TDD, y ejercicio Agenda.

---

## 1. Objetivos y competencias de la semana

### Objetivos para el alumno

| # | Objetivo | Bloom | Evidencia de logro |
|---|----------|-------|-------------------|
| 1 | Explicar por qué el testing es crítico, con ejemplos reales | Comprender | Participa en la discusión de los casos históricos |
| 2 | Distinguir caja negra / caja blanca y los niveles de la pirámide | Comprender | Responde correctamente en el cierre socrático |
| 3 | Escribir tests unitarios con `unittest`: TestCase, aserciones, fixtures | Aplicar | Completa Kata FizzBuzz en la práctica |
| 4 | Aplicar el ciclo TDD (Red → Green → Refactor) | Aplicar | Escribe tests de la Agenda antes de la implementación |
| 5 | Verificar excepciones con `assertRaises` | Aplicar | Tests de `ValueError` y `KeyError` en la Agenda |

### Competencias transversales

- Trabajo en parejas (pair programming en la kata)
- Uso de Codespaces + GitHub Classroom (continuidad del Módulo I)
- Lectura de salida de tests como herramienta de diagnóstico

---

## 2. Plan de clase — Sesión Teórica (180 min)

### Resumen visual

```
 0        30        70       110  120      150      170  180
 ├─ T0 ──┼── T1 ──┼── T2 ──┤PAUS├── T3 ──┼── T4 ──┤BUF┤
 Repaso   Motiv.   unittest  10'  TDD      Cierre   10'
 POO      Por qué  framework      R-G-R    Agenda
 30'      testar   40'            30'      preview
          40'                              20'
```

### Bloque T0 — Repaso POO Python (30 min)

| Min | Filmina | Actividad | Notas para el docente |
|-----|---------|-----------|----------------------|
| 0–3 | [F-00] Portada | Presentar el módulo. *"Hoy: escribir código que verifica código."* | Tono directo, sin preámbulo largo |
| 3–6 | [F-01] Agenda del día | Recorrer los bloques. Mencionar la pausa. | Dejar claro que la práctica de hoy es extensión directa de la teórica |
| 6–9 | [F-02] Clases e instancias | Tipear `Agenda.__init__`, `__str__`, `__eq__` en vivo. Preguntar: *"¿Qué pasa sin `__eq__`?"* | **Clave:** `__eq__` es necesario para `assertEqual` — si no lo entienden ahora, van a tener problemas con los tests |
| 9–12 | [F-03] Herencia y super() | Ejemplo: `DNIInvalidoError(ValueError)`. Preguntar: *"¿`assertRaises(ValueError)` la atrapa?"* | Sí, porque es subclase. Decisión de diseño. |
| 12–15 | [F-04] Excepciones propias | Mostrar `agregar()` con validaciones. *"Este es el código que vamos a testear."* | No implementar la clase completa todavía — solo la interfaz |
| 15–18 | [F-05] Métodos especiales para tests | Tabla rápida. *"No memoricen esto, vuelvan a la filmina cuando escriban tests."* | No demorarse — es referencia, no contenido nuevo |

**Transición:** *"Tienen fresco el modelo de objetos. Ahora: ¿por qué es crítico testear?"*

### Bloque T1 — Motivación: por qué testar (40 min)

| Min | Filmina | Actividad | Notas para el docente |
|-----|---------|-----------|----------------------|
| 30–31 | [F-06] Errores (impacto) | Mostrar la slide. Silencio de 10 seg. Dejar que el título haga efecto. | Efecto dramático deliberado |
| 31–35 | [F-07] Air China 140 | Narrar el caso. Preguntar: *"¿Qué tendría que haber hecho el equipo de testing?"* | Esperar respuestas. Dirigir hacia "testear combinaciones de estado". |
| 35–39 | [F-08] Therac-25 | Narrar. Preguntar: *"¿Este error es de caja negra o caja blanca?"* | Caja blanca — la race condition solo se descubría conociendo la estructura interna |
| 39–43 | [F-09] Ariane 5 | Narrar. Preguntar: *"¿Qué tipo de prueba habría detectado esto?"* | Regresión con nuevos parámetros + prueba de borde en valores máximos |
| 43–46 | [F-10] ¿Qué tienen en común? | Socrático: preguntar antes de mostrar. Leer la definición IEEE de testing. | **Concepto clave:** testing es falsificación, no confirmación |
| 46–49 | [F-11] Caja negra vs. caja blanca | Explicar ambos. Vincular con la Agenda: caja negra = "DNI abc → ValueError"; caja blanca = "DNI de 6 dígitos para cubrir el borde del if" | En la práctica van a hacer las dos |
| 49–52 | [F-12] Pirámide de testing | Recorrer los 4 niveles. *"Hoy = Nivel 1 (unidad). Los demás se mencionan para contexto."* | Definición de filminas 2025: *"pruebas de bajo nivel que se focalizan en una pequeña parte del software"* |
| 52–55 | [F-13] Pruebas de regresión | Vincular con Ariane 5. *"Con TDD esto es automático: `python -m unittest discover` después de cada cambio."* | Concepto clave para el cierre del módulo |

> **Cita textual de `python-testing.pdf` para leer en clase:**
> *"Los errores en el software no identificados a tiempo pueden ser sumamente costosos en términos monetarios o incluso llevar a pérdidas de vidas humanas."*

**Transición:** *"Ya sabemos por qué. Ahora el cómo: el framework."*

### Bloque T2 — Framework unittest (40 min)

| Min | Filmina | Actividad | Notas para el docente |
|-----|---------|-----------|----------------------|
| 55–58 | [F-14] Familia xUnit | Historia: Beck → SUnit → JUnit → unittest. *"El mismo patrón en todos los lenguajes."* | No demorarse — es contexto, no práctica |
| 58–61 | [F-15] TestCase · TestSuite · TestRunner | Explicar los 3 conceptos. *"TestCase es lo que heredamos, el runner los ejecuta."* | |
| 61–64 | [F-16] Mi primer test | **Código en vivo:** tipear `test_suma` y `test_tipo` desde cero. Ejecutar. Después **romperlo**: cambiar `assertEqual(resultado, 4)` por `5`. Mostrar el error. | **Momento clave:** demostrar que `assertEqual` da mensajes útiles vs `assertTrue(a == b)` que dice "False is not true" |
| 64–66 | [F-16b] Leer output de test fallido | Explicar FAIL vs ERROR con la filmina. *"Lean siempre desde el AssertionError."* | |
| 66–69 | [F-17] Aserciones esenciales | Recorrer la tabla. *"Memoricen 3: assertEqual, assertRaises, assertIn. Las demás están en la referencia."* | |
| 69–71 | [F-17b] Aserciones para colecciones | Rápido. *"`assertCountEqual` ignora orden — lo van a usar con `listar()`."* | |
| 71–75 | [F-18] assertRaises | **Código en vivo:** tipear la variante con `with`. Mostrar qué pasa si la excepción no se lanza. Luego la variante que captura `ctx` y verifica el mensaje. | **Pregunta anticipada:** *"¿Y si lanza TypeError en vez de ValueError?"* → se propaga como ERROR, no como FAIL |
| 75–79 | [F-19] Fixtures: setUp/tearDown | **Código en vivo:** escribir `AgendaTest` con `setUp`. *"Cada test arranca limpio."* | Explicar por qué `tearDown` se ejecuta incluso si el test falla |
| 79–81 | [F-19b] Orden de ejecución | Mostrar el diagrama. *"El orden entre tests no está garantizado."* | |
| 81–85 | [F-20] Ejecución CLI | Ejecutar en la terminal: `-v`, `discover`. Mostrar la salida. | |

**⏸️ PAUSA (10 min) — minuto 85 a 95**

### Bloque T3 — TDD: Red → Green → Refactor (30 min)

| Min | Filmina | Actividad | Notas para el docente |
|-----|---------|-----------|----------------------|
| 95–98 | [F-21] ¿Qué es TDD? | Definir. Cita de Beck. *"Contraintuitivo: el test primero."* | |
| 98–101 | [F-22] Ciclo R-G-R | Explicar los 3 pasos con la filmina. *"Ciclos de 2 a 10 min."* | |
| 101–108 | [F-23] Demo FizzBuzz — RED | **Código en vivo:** tipear `test_tres_retorna_fizz`. Ejecutar. Mostrar `NameError`. *"Esto es exactamente lo que queremos."* | No apurarse — es la primera vez que ven el ciclo. Dejar que el error "se sienta" |
| 108–112 | [F-24] Demo FizzBuzz — GREEN | Implementar `return "Fizz"`. Ejecutar. Verde. Agregar `test_cinco_retorna_buzz`. Falla. Implementar más. Repetir 3 ciclos. | Verbalizar cada paso: *"estoy en rojo… ahora mínimo para verde… ahora refactor"* |
| 112–115 | [F-25] Demo FizzBuzz — REFACTOR | Agregar type hints, docstring. Ejecutar para confirmar verde. *"Los tests documentan la especificación."* | |

**Transición:** *"Esto es lo que van a hacer en la práctica con la Agenda."*

### Bloque T4 — Cierre y preview práctica (20 min)

| Min | Filmina | Actividad | Notas para el docente |
|-----|---------|-----------|----------------------|
| 115–121 | [F-26] Ejercicio Agenda | Presentar el enunciado (de filminas 2025). Mostrar la tabla de métodos y tests. *"Primero tests, luego clase."* | Verificar que todos entiendan la diferencia entre `ValueError` (formato) y `KeyError` (existencia) |
| 121–125 | [F-27] Cierre | Recorrer el checklist. Preguntar cada ítem al grupo. | Reforzar: *"Todo esto se transfiere directamente a Django en el Módulo III."* |
| 125–130 | — | Setup GitHub Classroom TP 3 — mostrar el link, que clonen en Codespaces | No hacer en este momento — solo mostrar |

**Buffer:** 10 min restantes para preguntas o desborde.

---

## 3. Plan de clase — Sesión Práctica (180 min)

### Resumen visual

```
 0        60       120      160      180
 ├─ P1 ──┼── P2 ──┼── P3 ──┼── P4 ──┤
 Kata     Agenda   Agenda   Revisión
 FizzBuzz tests    implem.  colectiva
 TDD pair 1ro      verde    live code
 60'      60'      40'      20'
```

### Bloque P1 — Kata FizzBuzz TDD guiada (60 min)

| Aspecto | Detalle |
|---------|---------|
| **Formato** | Pair programming — armar parejas al azar |
| **Entorno** | GitHub Codespaces (ya configurado en Módulo 0/I) |
| **Consigna** | Escribir `test_fizzbuzz.py` con TDD estricto. Mínimo 4 tests. Después crear `fizzbuzz.py`. |
| **Rol docente** | Circular entre parejas. Verificar que escriben test → ejecutan → rojo → implementan → verde. Corregir si alguien escribe la función primero. |
| **Criterio de éxito** | Al menos 4 tests pasando y la función completa implementada. Que los alumnos hayan vivido al menos 3 iteraciones del ciclo. |
| **Peligros comunes** | ① Escribir la función primero. ② Tests que nunca fallan ("test sin assert"). ③ Un miembro de la pareja no participa. |

**Tip docente:** Si una pareja termina rápido, pedirles que agreguen tests de borde: `fizzbuzz(0)`, `fizzbuzz(-3)`, `fizzbuzz(1000000)`.

### Bloque P2 — Ejercicio Agenda: escribir tests primero (60 min)

| Aspecto | Detalle |
|---------|---------|
| **Formato** | Individual con soporte docente |
| **Consigna** | Crear `test_agenda.py`. Escribir tests para `agregar`, `buscar` y sus excepciones (`ValueError` para DNI inválido, `KeyError` para duplicado/inexistente). **No escribir la clase Agenda todavía.** |
| **Tests mínimos requeridos** | `test_agregar_y_buscar`, `test_dni_no_numerico`, `test_dni_muy_corto`, `test_agregar_duplicado`, `test_buscar_inexistente` |
| **Rol docente** | Verificar que los tests fallan (no existe `Agenda`). Preguntar: *"¿tu test falla? Bien, eso es el RED."* Ayudar con la sintaxis de `assertRaises`. |
| **Peligros comunes** | ① Escribir la Agenda y los tests juntos. ② Olvidar `setUp`. ③ Usar `assertTrue(a == b)` en vez de `assertEqual`. |

**Tip docente:** Recomendar nombres descriptivos: `test_agregar_dni_invalido_lanza_ValueError`, no `test_1`.

### Bloque P3 — Ejercicio Agenda: implementar hasta verde (40 min)

| Aspecto | Detalle |
|---------|---------|
| **Formato** | Individual |
| **Consigna** | Crear `agenda.py`. Implementar `__init__`, `agregar` y `buscar` hasta que todos los tests de P2 pasen. Agregar tests y código para `eliminar` y `listar` si da el tiempo. |
| **Rol docente** | Verificar que ejecutan tests después de cada cambio. *"¿Pasaron todos? Ahora podés agregar el siguiente método."* |
| **Criterio de éxito** | Mínimo 5 tests en verde. Quien termine puede agregar `eliminar`/`listar` con sus tests. |

### Bloque P4 — Revisión colectiva (20 min)

| Aspecto | Detalle |
|---------|---------|
| **Formato** | Live coding al frente — proyectar pantalla del docente |
| **Actividad** | Tomar el código de un alumno (pedir voluntario). Mostrar tests fallando → implementar → verde. Recorrer 2-3 ciclos completos. |
| **Cierre** | Preguntar: *"¿Qué diferencia hubo entre escribir el test primero vs. después?"*. Recoger impresiones. |
| **Anuncio** | Mencionar que la guía de estudio (`guia-estudio.md`) cubre mocking, subtests y el anticipo de Django — que la lean como preparación para el Módulo III. Presentar TP 3 brevemente. |

---

## 4. Contenidos que quedan como lectura autónoma

> **Decisión pedagógica:** al comprimir a 1 semana, estos temas se mueven a la guía de estudio del alumno y se retoman al iniciar el Módulo III.

| Tema | Referencia en guía de estudio | Cuándo se retoma |
|------|------------------------------|-----------------|
| `unittest.mock` (MagicMock, patch) | Sección 4.6 | Módulo III — al testear vistas Django con BD mock |
| `subTest`, `@skip`, `@expectedFailure` | Sección 4.7 | Módulo III — al parametrizar tests de modelos |
| `django.test.TestCase` (anticipo) | Sección 4.8 | Módulo III — apertura (transición directa) |
| `setUpClass` / `addCleanup` | Sección 4.4.8 | Módulo III — cuando aparecen fixtures costosos |
| Test smells | Filmina [F-40b] | Revisión del TP 3 |

---

## 5. Extractos clave del material fuente

### De `python-testing.pdf` (filminas 2025) — para leer o proyectar en clase

**Slide "Testing de software" — definición:**
> *"Es un proceso que busca verificar la exactitud, integridad y calidad de un software. Incluye una serie de actividades que buscan encontrar errores y fallas en el software previo a que lleguen al usuario."*

**Slide "Test de unidades – Unit Test" — definición:**
> *"Son pruebas de bajo nivel (a nivel de código) que se focalizan en una pequeña parte del software. En programación orientada a objetos estas unidades suelen ser las clases."*

**Slide "Unittest framework" — historia y contexto:**
> *"Python contiene un framework de pruebas unitarias integrado en el api estándar. Es un framework de pruebas que forma parte de la familia Xunit. Xunit no es un framework sino que se refiere a toda la familia de frameworks que heredan de Sunit el cual fue originalmente escrito para smalltalk por kent beck 1989."*

**Slide "La clase TestCase" — convención sobre configuración:**
> *"En vez de tener un archivo de configuración en donde definamos donde están las pruebas el framework las encuentra en forma automática y siempre cuando sigamos convenciones. Para que un método sea una prueba a ejecutar debe empezar de la forma 'test_'."*

**Slide "La clase TestCase - fixtures":**
> *"setUp(): Este método es llamado antes de la ejecución de cada método test. tearDown(): Este método es llamado al finalizar la ejecución de cada método y es utilizado para limpiar las instancias utilizadas. Se ejecuta incluso si una excepción es lanzada durante la ejecución de la prueba."*

**Slide "Problema" — enunciado del ejercicio Agenda:**
> *"Realizar la clase agenda que guarde el nombre, apellido, dirección y teléfono de una persona utilizando su dni como referencia. Desarrolle los métodos necesarios para gestionar los datos incluyendo excepciones por datos inválidos. Una vez realizada la clase Agenda escriba la clase AgendaTest que pruebe todos los métodos incluida las excepciones."*

---

## 6. Preguntas para clase, debates y actividades

### Preguntas socráticas (para intercalar durante la teórica)

| Momento | Pregunta | Respuesta esperada |
|---------|----------|-------------------|
| Después de [F-02] | *"¿Qué pasa si no implemento `__eq__` y uso `assertEqual` con dos Agendas iguales?"* | Falla — compara identidad (`id()`), no estado |
| Después de [F-07] | *"¿Qué tendría que haber hecho el equipo de testing del Air China?"* | Testear combinaciones de estado del piloto automático |
| Después de [F-08] | *"¿El error del Therac-25 es de caja negra o caja blanca?"* | Caja blanca — race condition solo visible conociendo la estructura interna |
| Después de [F-09] | *"¿Qué tipo de prueba habría salvado al Ariane 5?"* | Regresión con parámetros nuevos + prueba de borde |
| Después de [F-10] | *"¿Qué tienen en común los 3 casos?"* | No se testearon bordes ni condiciones nuevas |
| Después de [F-16] | *"¿Por qué `assertEqual` es mejor que `assertTrue(a == b)`?"* | El mensaje de error dice qué valores difieren vs. "False is not true" |
| Después de [F-18] | *"¿Qué pasa si `assertRaises(ValueError)` recibe un `TypeError`?"* | El TypeError se propaga — resultado ERROR, no FAIL |
| Después de [F-23] | *"¿Un test que pasa sin código es bueno o malo?"* | Malo — no está verificando nada real |

### Actividades opcionales (si sobra tiempo)

1. **Debate rápido (5 min):** *"¿Es posible escribir tests que cubran todos los bugs posibles de un programa?"* → No. Testing demuestra presencia de errores, no su ausencia (Dijkstra).
2. **Ejercicio de diagnóstico (5 min):** Proyectar un test sin `assert` que está "en verde". Pedir a los alumnos que identifiquen el problema.
3. **Mini-challenge:** ¿Quién escribe el test con el nombre más descriptivo para un caso de la Agenda?

---

## 7. Decisiones pedagógicas del docente

### ¿Por qué comprimir a 1 semana?

El Módulo II de 2 semanas resultaba desbalanceado: los contenidos de la semana 5 (mocking, subtests, Django) son mejor aprovechados **dentro** del Módulo III donde se aplican directamente. Comprimir a 1 semana permite:
- Dedicar la semana 5 a iniciar Django más temprano
- Que el alumno practique mocking con un caso real (BD de Django) en vez de un caso artificial
- Mantener la motivación alta: en 1 semana ven TODO el ciclo (teoría → práctica → TP abierto)

### ¿Qué se pierde?

- La práctica guiada de `MagicMock` y `patch` en la teórica → se compensa con la guía de estudio (secciones 4.6) y con su uso real en Módulo III
- La Kata de tests para TP 2 → pasa a ser ejercicio optativo del TP 3
- La revisión grupal del TP 2 → se hace al inicio del Módulo III

### Restricciones que se mantienen

- Solo `unittest` de la stdlib — NO pytest
- TDD obligatorio en la práctica (test primero, implementación después)
- Copilot habilitado en Codespaces para pair programming

---

## 8. Checklist pre-clase

### Antes de la teórica

- [ ] Verificar que el proyector/pantalla muestra código legible (font ≥ 18pt)
- [ ] Tener abierto en el IDE: carpeta vacía para demos en vivo (FizzBuzz + Agenda)
- [ ] Filminas cargadas: `filminas.md` [F-00] a [F-27] (semana 4 únicamente)
- [ ] Tener a mano la URL de GitHub Classroom del TP 3 para mostrar al final
- [ ] Terminal abierta con `python --version` verificado (3.11+)

### Antes de la práctica

- [ ] GitHub Classroom: verificar que el assignment del TP 3 está publicado
- [ ] Codespaces: verificar que los alumnos pueden abrir un codespace (probar con cuenta de prueba)
- [ ] Preparar un repo de ejemplo con `test_fizzbuzz.py` vacío + `test_agenda.py` vacío por si algún alumno tiene problemas con el setup
- [ ] Tener el enunciado de la Agenda ([F-26]) proyectable para referencia rápida

---

## 9. Recursos y dónde encontrarlos en el repo

| Recurso | Ruta en el repositorio | Uso |
|---------|----------------------|-----|
| Filminas del tema | `salida/cursadas/2026/temas/02-pruebas-unitarias/filminas.md` | Proyectar en clase |
| Minuta completa | `salida/cursadas/2026/temas/02-pruebas-unitarias/minuta.md` | Guión detallado del docente |
| Guía de estudio del alumno | `salida/cursadas/2026/temas/02-pruebas-unitarias/guia-estudio.md` | Distribuir después de la clase |
| Diseño del tema | `salida/cursadas/2026/temas/02-pruebas-unitarias/diseno.md` | Referencia de objetivos y mapa de contenidos |
| Referencia unittest Python 3.14 | `salida/cursadas/2026/temas/02-pruebas-unitarias/testing.md` | Material complementario |
| Filminas 2025 (texto) | `ingesta/txt/python-testing.txt` | Citas textuales para la teórica |
| Config del tema | `salida/cursadas/2026/temas/02-pruebas-unitarias/topic.yaml` | Metadata del tema |

### Documentación externa

| Recurso | URL |
|---------|-----|
| Docs oficiales unittest | https://docs.python.org/3/library/unittest.html |
| Docs oficiales unittest.mock | https://docs.python.org/3/library/unittest.mock.html |
| Beck, K. — TDD by Example | ISBN 978-0321146533 (Addison-Wesley, 2002) |

---

## 10. Notas post-clase (completar después de dar la clase)

> Estas secciones quedan vacías para que el docente las complete después de cada sesión.

### Teórica

- **¿Se cumplió el timing?** ___
- **¿Hubo preguntas inesperadas?** ___
- **¿Qué bloque necesitó más tiempo del planificado?** ___
- **¿Algún alumno mostró dificultad con los prerequisitos (POO)?** ___

### Práctica

- **¿Cuántas parejas completaron la Kata FizzBuzz?** ___/total
- **¿Cuántos alumnos escribieron los tests de la Agenda antes de la clase?** ___/total
- **¿Cuántos alumnos llegaron a `eliminar`/`listar`?** ___/total
- **¿Errores recurrentes?** ___
- **¿Alguien resistió escribir el test primero?** ___

### Ajustes para el próximo año

- ___

---

*Guía del profesor generada para: Laboratorio de Programación y Lenguajes (IF009) — UNTDF 2026*  
*Tema 02 — Pruebas Unitarias · Semana 4 (comprimido a 1 semana)*  
*Fuentes: diseno.md, minuta.md, filminas.md, python-testing.pdf, testing.md*
