# TP 01 — Quiz Moodle

> Tipo: quiz-moodle
> Tema: Conceptos Introductorios + Intro a TypeScript
> Fuente principal: guia-estudio.md
> Fecha de regeneración: 2026-03-17
> Salidas asociadas: tp-quiz.gift · tp-quiz-moodle-config.md

---

## Criterio de regeneración

Este TP reemplaza la versión anterior y fue reconstruido exclusivamente a partir de `guia-estudio.md`.

Objetivo:

- evaluar comprensión conceptual del tema;
- cubrir los bloques 1 a 5 de la guía del alumno;
- generar un banco de 30 preguntas importable en Moodle.

---

## Configuración sugerida del quiz

| Campo | Valor |
| ----- | ----- |
| Título | TP 01 — Conceptos Introductorios + Intro a TypeScript |
| Plataforma | Moodle |
| Formato | GIFT UTF-8 |
| Preguntas | 30 |
| Tiempo límite | 30 minutos |
| Intentos permitidos | 1 |
| Puntaje | 1 punto por pregunta |
| Navegación | Libre |
| Comportamiento | Deferred feedback |
| Mostrar respuestas correctas | Después del cierre del quiz |
| Categoría | TP/01-conceptos-introductorios |

---

## Instrucciones para el alumno

Respondé las 30 preguntas en base al contenido de la guía de estudio del Tema 01.
El cuestionario evalúa definiciones, relaciones entre paradigmas, criterios de evaluación de lenguajes, máquina abstracta, TypeScript como lenguaje multiparadigma e impacto de la IA generativa en la práctica de programación.

---

## Banco de preguntas

### P01 — Qué es un cómputo

**Fuente:** Guía, sección 1.0

¿Qué definición corresponde mejor a “cómputo” según la guía?

- ✅ Una serie de operaciones estructuradas aplicadas a datos de entrada para obtener nuevos datos de salida
- Una colección de archivos fuente compilados en un ejecutable
- Una interfaz gráfica para interactuar con un programa
- Un lenguaje usado para expresar algoritmos

### P02 — Qué es un programa

**Fuente:** Guía, sección 1.0

¿Qué es un programa?

- Una lista de variables declaradas en memoria
- ✅ Una colección definida y ordenada de cómputos diseñada para realizar una tarea específica
- Un conjunto de componentes de hardware conectados por un bus
- Una traducción de bytecode a lenguaje máquina

### P03 — Qué es un lenguaje de programación

**Fuente:** Guía, sección 1.0

¿Qué describe mejor a un lenguaje de programación?

- Un protocolo de comunicación entre compiladores
- Una notación para escribir solo instrucciones imperativas
- ✅ Un conjunto de reglas sintácticas y semánticas usadas para definir programas
- Un sistema de archivos para organizar proyectos

### P04 — Por qué estudiar lenguajes

**Fuente:** Guía, sección 1.1

Según la guía, estudiar lenguajes no consiste solo en aprender sintaxis sino en adquirir:

- Técnicas para memorizar comandos del compilador
- ✅ Modelos mentales diferentes para pensar problemas
- Reglas fijas para escribir todo en un único paradigma
- Habilidades de administración de servidores

### P05 — Costo de elegir mal un lenguaje

**Fuente:** Guía, sección 1.2

¿Qué ilustra el ejemplo de elegir Node.js para procesamiento numérico intensivo y luego migrar a Python más NumPy?

- Que todo lenguaje multiparadigma sirve igual para cualquier dominio
- ✅ Que elegir mal un lenguaje puede implicar costos técnicos y económicos reales
- Que JavaScript es mejor que Python para cómputo científico
- Que el rendimiento nunca depende del paradigma

### P06 — FORTRAN en la línea histórica

**Fuente:** Guía, sección 1.3

¿Qué problema resolvió FORTRAN en 1957 según la tabla histórica?

- Introdujo objetos puros y paso de mensajes
- ✅ Reemplazó al ensamblador para cómputo científico como lenguaje de alto nivel útil
- Permitió tipado estático sobre JavaScript
- Hizo posible la lógica simbólica en Prolog

### P07 — LISP en la línea histórica

**Fuente:** Guía, sección 1.3

¿Qué aporte se asocia a LISP en la guía?

- Máquina virtual portable entre arquitecturas
- ✅ Funciones de primera clase, recursión y evaluación simbólica
- Encapsulamiento orientado a objetos puro
- Drivers de bajo nivel con máxima eficiencia

### P08 — C en la línea histórica

**Fuente:** Guía, sección 1.3

¿Cuál fue el aporte histórico de C según la guía?

- Hizo mainstream la IA generativa
- Introdujo el paradigma lógico en producción
- ✅ Ofreció imperativo estructurado con portabilidad sin sacrificar eficiencia
- Eliminó la necesidad de compilar programas

### P09 — Java en la línea histórica

**Fuente:** Guía, sección 1.3

¿Qué idea se destaca para Java en 1995?

- Reemplazó totalmente a C en sistemas embebidos
- ✅ Write once, run anywhere mediante máquina virtual
- Introdujo recursión por primera vez
- Eliminó el uso de bytecode

### P10 — TypeScript en la línea histórica

**Fuente:** Guía, sección 1.3

¿Qué se destaca de TypeScript en 2012?

- Que fue creado como lenguaje lógico declarativo
- ✅ Que agrega tipos estáticos sobre JavaScript para escalar proyectos grandes
- Que compila a bytecode JVM
- Que reemplaza completamente a Python en IA

### P11 — Legibilidad

**Fuente:** Guía, sección 1.4.1

¿Qué criterio de Sebesta evalúa si un programador puede leer y comprender código ajeno con facilidad?

- Eficiencia
- Costo
- ✅ Legibilidad
- Portabilidad

### P12 — Expresividad

**Fuente:** Guía, sección 1.4.2

¿Qué criterio se asocia a cuán naturalmente un lenguaje permite expresar una solución?

- Confiabilidad
- ✅ Expresividad
- Eficiencia
- Portabilidad

### P13 — Seguridad o confiabilidad

**Fuente:** Guía, sección 1.4.3

En la guía, la detección de errores de tipo antes de ejecutar se usa como ejemplo de:

- Legibilidad
- ✅ Seguridad o confiabilidad del lenguaje
- Portabilidad entre plataformas
- Abstracción de hardware

### P14 — Portabilidad

**Fuente:** Guía, sección 1.4.5

¿Qué criterio mide si un lenguaje puede funcionar en distintas plataformas sin reescribir el código?

- Eficiencia
- Costo
- Legibilidad
- ✅ Portabilidad

### P15 — Eficiencia

**Fuente:** Guía, sección 1.4.6

¿Qué criterio se relaciona con velocidad de ejecución y consumo de memoria?

- Escribibilidad
- Portabilidad
- ✅ Eficiencia
- Legibilidad

### P16 — Qué es un paradigma de programación

**Fuente:** Guía, sección 2.1

Según la guía, un paradigma de programación es principalmente:

- Un conjunto de librerías de un ecosistema
- ✅ Una forma de pensar el cómputo y estructurar la solución
- Un listado de palabras reservadas del lenguaje
- Un formato de serialización de datos

### P17 — Arquitectura de Von Neumann

**Fuente:** Guía, sección 2.2

¿Qué rasgo central del paradigma imperativo se vincula directamente con la arquitectura de Von Neumann?

- La ausencia de estado mutable
- El uso exclusivo de funciones puras
- ✅ La secuencia de instrucciones que modifican variables y estado
- La búsqueda de pruebas lógicas

### P18 — Variable en el paradigma imperativo

**Fuente:** Guía, sección 2.2

En el modelo explicado en la guía, una variable imperativa mapea directamente a:

- Un mensaje entre objetos
- ✅ Una celda de memoria
- Una consulta lógica
- Un tipo algebraico

### P19 — Cuello de botella de Von Neumann

**Fuente:** Guía, sección 2.3

¿Dónde se produce el cuello de botella de Von Neumann?

- Entre GPU y VRAM
- Entre disco y CPU
- ✅ Entre CPU y memoria
- Entre navegador y compilador

### P20 — Evolución metodológica

**Fuente:** Guía, sección 2.4

¿Qué hito metodológico se asocia a los años 70 en la guía?

- Multiparadigma en TypeScript
- ✅ Análisis y diseño estructurado con modularización y eliminación del GOTO
- Aparición de la JVM
- Adopción masiva de IA generativa

### P21 — Paradigma funcional

**Fuente:** Guía, sección 2.5

¿Qué base formal aparece asociada al paradigma funcional?

- Arquitectura de Von Neumann
- Lógica de resolución de Robinson
- ✅ Cálculo lambda de Church
- Encapsulamiento de Smalltalk

### P22 — Paradigma lógico

**Fuente:** Guía, sección 2.5

¿Qué caracteriza al paradigma lógico según la guía?

- El cómputo como mutación explícita de estado
- ✅ Un programa como hechos y reglas cuya ejecución es una búsqueda de pruebas
- El uso obligatorio de clases e interfaces
- El reemplazo del compilador por un framework web

### P23 — Orientado a objetos

**Fuente:** Guía, sección 2.5

¿Cómo presenta la guía al paradigma orientado a objetos?

- Como una ruptura total con el imperativo
- ✅ Como una extensión del imperativo con encapsulamiento y mensajes
- Como un caso particular del lógico
- Como sinónimo de programación funcional

### P24 — Dominio de aplicación del paradigma lógico

**Fuente:** Guía, sección 2.6

¿Cuál es un dominio de aplicación ideal del paradigma lógico según la tabla?

- Drivers y sistemas embebidos
- Interfaces gráficas empresariales
- ✅ IA simbólica y sistemas expertos
- Renderizado 3D en GPU

### P25 — Escalera de abstracciones

**Fuente:** Guía, sección 3.1

Al subir en la escalera de abstracciones, ¿qué se gana según la guía?

- Control directo sobre registros y memoria
- ✅ Legibilidad, escribibilidad y portabilidad
- Ejecución puramente nativa sin intermediarios
- Menor overhead del runtime

### P26 — Correspondencia Von Neumann y código

**Fuente:** Guía, sección 3.2

¿Qué construcción del lenguaje imperativo corresponde a un salto condicional del procesador?

- Una interfaz
- ✅ Un if
- Un predicado lógico
- Una lambda pura

### P27 — Ejemplo comparativo en tres niveles

**Fuente:** Guía, sección 3.3

En el ejemplo de suma de valores absolutos, ¿qué nivel se identifica como estilo funcional?

- LC-3
- C imperativo de alto nivel
- ✅ TypeScript con map y reduce
- Ensamblador con registros R0 y R1

### P28 — Máquina abstracta

**Fuente:** Guía, sección 3.4

Según Gabbrielli y Martini, todo lenguaje define:

- Un único compilador obligatorio a lenguaje máquina
- ✅ Una máquina abstracta que ejecuta los programas del lenguaje
- Un sistema operativo propio
- Una GPU dedicada

### P29 — Pipeline de TypeScript

**Fuente:** Guía, sección 4.2

¿Cuál es el pipeline correcto de TypeScript según la guía?

- archivo.ts → JVM → archivo.class → CPU
- archivo.ts → intérprete Python → archivo.pyc → CPU
- ✅ archivo.ts → tsc → archivo.js → V8 o Node.js o Deno → CPU
- archivo.ts → gcc → archivo.o → CPU

### P30 — Trust but verify

**Fuente:** Guía, secciones 5.3 y 5.4

En el loop trust but verify, ¿qué debe hacer el programador después de recibir el output de la IA?

- Ejecutarlo sin revisar para ganar tiempo
- Publicarlo directamente si compila
- ✅ Revisarlo con conocimiento de dominio para verificar paradigma y semántica
- Pedirle a otra IA que lo apruebe sin leerlo
