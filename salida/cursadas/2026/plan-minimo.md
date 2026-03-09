# Plan Mínimo — Paradigmas y Lenguajes de Programación 2026

> ⚠️ **DOCUMENTO INMUTABLE** — Este plan es el contrato oficial del cursado.
> Ningún agente puede modificarlo una vez confirmado.
> Fuente: Programa institucional IF020 — UNTDF / IDEI (revisión 2024-11-30)

---

## Datos del Curso

| Campo | Valor |
|-------|-------|
| Materia | Paradigmas y Lenguajes de Programación |
| Código | IF020 |
| Institución | Universidad Nacional de Tierra del Fuego — Instituto IDEI |
| Carrera | Licenciatura en Sistemas (OCS 049/2017) |
| Año de cursada | 2026 |
| Año del plan de estudios | 4° año |
| Carácter | Cuatrimestral (1° cuatrimestre) |
| Tipo | Obligatoria |
| Modalidad | Presencial |
| Carga horaria semanal | 8 hs |
| Carga horaria total | 120 hs |
| Duración de clase | 120 minutos |
| Perfil docente | profesor-teorico |
| Docente | Matías Gel |

---

## Contenidos Mínimos Institucionales

Estos tópicos son obligatorios por el plan de estudios y **no pueden eliminarse**:

1. Sintaxis y semántica. Nociones básicas de semántica formal. Semántica operacional.
2. Lenguajes de programación: entidades y ligaduras.
3. Sistemas de tipos.
4. Niveles de polimorfismo.
5. Encapsulamiento y abstracción.
6. Conceptos de intérpretes y compiladores.
7. Criterios de diseño y de implementación de lenguajes de programación.
8. Paradigmas de programación: imperativo, orientado a objetos, funcional, lógico.
9. Concurrencia y paralelismo.

---

## Programa Analítico — Módulos

### MÓDULO I: Conceptos Introductorios
- Razones e importancia del estudio de lenguajes de programación
- Síntesis de los paradigmas de programación
- Paradigma imperativo: conceptos fundamentales
- Paradigma declarativo: conceptos fundamentales
- Aportes de cada paradigma y dominios de aplicación
- Lenguajes característicos de los diferentes dominios
- Criterios para el estudio, análisis, selección y evaluación de lenguajes
- Evolución de los lenguajes de programación — perspectiva histórica
- Introducción a Kotlin como lenguaje multiparadigma

### MÓDULO II: Paradigma de Programación Funcional
- Introducción y fundamentos de la programación funcional
- Importancia e impacto en lenguajes y frameworks actuales
- Funciones puras, inmutabilidad, recursividad
- Ventajas, desventajas y dominios de aplicación
- Kotlin como lenguaje funcional; comparación con lenguajes funcionales puros
- Expresiones lambda y funciones anónimas (Kotlin y comparación)
- Funciones de orden superior, clausuras y ámbito léxico
- Composición de funciones, aplicación parcial y currificación
- Evaluación perezosa en Kotlin
- Manejo de efectos secundarios
- Introducción a mónadas con Kotlin
- Tendencias actuales: programación funcional en Python, Java, JavaScript
- Programación funcional reactiva

### MÓDULO III: Paradigma de Programación Lógica (Prolog)
- Fundamentos de la programación lógica
- Sintaxis y estructuras básicas de Prolog: hechos, reglas y consultas
- Variables, unificación y backtracking
- Modelado de bases de conocimiento
- Consultas complejas
- Dominios de aplicación

### MÓDULO IV: Paradigma de Programación Orientada a Objetos
- Fundamentos de la programación orientada a objetos
- Estudio y práctica en Kotlin como representativo del paradigma OO
- Ejemplos comparativos en Python, Java, TypeScript

### MÓDULO V: Sintaxis y Semántica de Lenguajes de Programación
- Sintaxis: criterios generales, elementos sintácticos
- Descripción y definición formal de la sintaxis
- Gramática BNF y BNF extendido
- Árboles sintácticos, diagramas de sintaxis
- Sintaxis abstracta y concreta; ambigüedad
- Semántica: estática, gramática de atributos
- Herramientas para la descripción semántica
- Procesadores de lenguajes: interpretación y compilación
- Etapas de un proceso de traducción

### MÓDULO VI: Variables
- Atributos de variables: nombres, ámbito, valor izquierdo/derecho, tiempo de vida, tipos
- Concepto de binding: tiempo de vinculación
- Binding de tipos: estático y dinámico
- Binding de almacenamiento y tiempo de vida
- Variables estáticas, dinámicas de pila y de heap
- Chequeo de tipos, tipado fuerte
- Compatibilidad nominal y estructural; subtipo; tipo derivado
- Ámbito estático y dinámico; entorno de referencia
- Inicialización de variables; asignación estática y dinámica de memoria
- Ejemplos en Kotlin y comparación con otros lenguajes

### MÓDULO VII: Tipos de Datos
- Tipos built-in y primitivos
- Tipos ordinales definidos por el usuario
- Tipos de agregación: producto cartesiano, uniones, uniones discriminadas, mapeos finitos
- Arrays: estáticos, de pila dinámica, dinámicos de heap
- Tipos secuencia, strings, conjunto potencia, tipos recursivos
- Tipo puntero: inseguridad, punteros colgantes, recolección de basura
- Sistemas de tipos: monomórficos vs. polimórficos
- Tipos que aceptan null y sus operadores
- Lenguajes fuertemente tipados; clases
- Ejemplos en Kotlin y otros lenguajes

### MÓDULO VIII: Expresiones y Estructuras de Control
- Expresiones aritméticas, relacionales y booleanas
- Reglas de precedencia, asociatividad, paréntesis
- Sentencias de asignación; asignación como expresión; modo mixto
- Evaluación corto-circuito vs. evaluación estricta
- Sobrecarga de operadores; conversiones de tipo y coerciones
- Estructuras de control: enunciados compuestos, de selección, selectores anidados, selección múltiple
- Enunciados iterativos, ejecución condicional, mecanismos de control de bucle
- Iteradores y generadores
- Ejemplos en Kotlin y otros lenguajes

### MÓDULO IX: Manejo de Excepciones
- Gestión de excepciones; eventos excepcionales
- Programas tolerantes a fallos
- Lanzamiento, manejador y propagación de excepciones
- Formas de manejar excepciones; facilidades de lenguajes
- Manejo de excepciones en Kotlin y comparación con otros lenguajes

### MÓDULO X: Estructuración de Programas
- Abstracción procedural; fundamentos de subprogramas
- Parámetros, procedimientos y funciones
- Métodos de paso de parámetros; modos de implementación
- Subprogramas como parámetros; tipos de valores de retorno
- Subprogramas sobrecargados y polimórficos
- Implementación de subprogramas
- Soporte de modularidad y encapsulación
- Interface e Implementación; separación; compilación separada e independiente
- Librerías de módulos; estructuras de datos genéricas
- Ejemplos en Kotlin y otros lenguajes

### MÓDULO XI: Concurrencia
- Conceptos fundamentales de concurrencia a nivel de subprogramas
- Niveles de concurrencia; threads
- Sincronización de cooperación y competencia
- Comunicación entre procesos, tareas
- Programación asíncrona
- Ejemplos en Kotlin y otros lenguajes

---

## Programación Semanal (17 semanas)

| Semana | Módulo | Descripción | Hito |
|--------|--------|-------------|------|
| 1 | I | Conceptos introductorios. Práctica: intro a Kotlin | |
| 2 | II | Introducción a programación funcional con Kotlin | |
| 3 | II | Aspectos avanzados de programación funcional | |
| 4 | II | Introducción a mónadas en Kotlin | |
| 5 | II | Programación funcional en Python y JavaScript | |
| 6 | III | Paradigma lógico. Introducción a Prolog | |
| 7 | IV | Paradigma OO. Clases, objetos y polimorfismo en Kotlin | |
| 8 | I-IV | Presentación trabajo final sobre paradigmas | **Parcial Práctico Nº 1** |
| 9 | V | Sintaxis y semántica de lenguajes de programación | |
| 10 | VI | Variables, binding y ámbito. Práctica en Kotlin | |
| 11 | VII | Tipos de datos y estructuración | |
| 12 | VIII | Estructuras de control | |
| 13 | IX | Manejo de excepciones | |
| 14 | X | Abstracción procedural, modularidad, genericidad | |
| 15 | XI | Concurrencia y paralelismo | |
| 16 | I-XI | Presentación oral de trabajos sobre lenguajes | **Parcial Práctico Nº 2** |
| 17 | I-XI | Trabajo final para promoción / Reunión de cátedra | |

---

## Evaluación

| Instancia | Descripción | Aprobación |
|-----------|-------------|-----------|
| Parcial 1 | Trabajo de programación sobre paradigmas (1 semana, defensa oral) | ≥ 4/10 |
| Parcial 2 | Presentación de un lenguaje elegido por el alumno | ≥ 4/10 |
| Nota final cursada | Promedio de parciales | ≥ 4/10 |
| Promoción directa | Ambos parciales ≥ 7 + examen oral | ≥ 7/10 |

---

## Bibliografía Obligatoria

1. **Louden, Kenneth C.** (2011). *Programming Languages: Principles and Practice*, 3rd ed. Cengage Learning. Caps. 1–13.
2. **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms*, 2nd ed. Springer. Caps. 1–12.
3. **Sebesta, Robert** (2019). *Concepts of Programming Languages*, 12th ed. Pearson. Caps. 1–16.
4. **Spivey, Michael** (2005). *An Introduction to Logic Programming through Prolog*. Caps. 1–7.

---

## Estado

| Campo | Valor |
|-------|-------|
| Estado | PENDIENTE DE CONFIRMACIÓN |
| Generado | 2026-03-09 |
| Confirmado | — |
| Bloqueado | No (pendiente confirmación docente) |
