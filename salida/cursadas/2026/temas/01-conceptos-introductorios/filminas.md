# Filminas — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Estado:** GENERADA
> **Agente:** Dr. Roberto (class-writer)
> **Fecha:** 2026-03-09
> **Duración total:** 120 minutos · 6 bloques · 29 filminas (F-00 portada + F-01 a F-28)
> **Formato:** Markdown estructurado para exportar a presentación
> **Input:** `temas/01-conceptos-introductorios/diseno.md` (aprobado)

---

## PORTADA

---

### [F-00] Portada

# Conceptos Introductorios + Intro a TypeScript

**Paradigmas y Lenguajes de Programación 2026**
Universidad Nacional de Tierra del Fuego — IDEI

Semana 1 · Clase 1 de 2 · 120 minutos

---

## BLOQUE 1 — ¿Por qué estudiar lenguajes de programación? (20 min)

---

### [F-01] La pregunta incómoda

# ¿Para qué estudiar lenguajes si ya saben programar?

> *"La elección del lenguaje determina el modelo mental con el que pensás el problema."*

**Hoy respondemos esta pregunta.**

---

### [F-01b] ¿Qué es un lenguaje de programación?

# Definición formal

**Cómputo**
> Una serie de operaciones estructuradas aplicadas a un conjunto de datos de entrada para obtener nuevos datos como resultado.

**Programa**
> Una colección definida y ordenada de cómputos diseñada para realizar una tarea específica o resolver un problema concreto.

**Lenguaje de programación**
> Un conjunto de **reglas sintácticas y semánticas** usadas para definir programas. Sistema de notación cuyas instrucciones son comprendidas y ejecutadas por máquinas.

*(Slides cátedra UNTDF 2024 · Aaby, A. — citado en Louden & Lambert, Cap. 1)*

> Una descripción completa incluye el **modelo computacional**, la **sintaxis**, la **semántica** y las **consideraciones pragmáticas** que dan forma al lenguaje.

---

### [F-02] El costo de elegir mal

# Elegir el lenguaje equivocado tiene consecuencias reales

**Caso típico:**
- Startup elige Node.js para procesamiento numérico intensivo
- 2 años después → migración masiva a Python + NumPy
- Costo: código descartado, tiempo perdido, equipo frustrado

**¿Por qué pasa?**
Quien eligió el lenguaje no conocía los paradigmas ni sus trade-offs.

---

### [F-03] Perspectiva histórica

# La línea de tiempo de los lenguajes

| Año | Lenguaje | Aporte clave |
|-----|----------|-------------|
| 1957 | FORTRAN | El primero de alto nivel |
| 1960 | LISP | Funciones como datos, recursión |
| 1972 | C | Imperativo estructurado, portabilidad |
| 1980 | Smalltalk | Orientación a objetos pura |
| 1995 | Java | OO + máquina virtual |
| 2008 | Python 3 | Multiparadigma, ecosistema IA |
| 2012 | TypeScript | Tipos estáticos sobre JavaScript |

> Cada lenguaje resuelve un problema que el anterior no resolvía bien.

---

### [F-04] Criterios de evaluación de lenguajes

# ¿Cómo evaluamos un lenguaje? — Sebesta (2018)

Sebesta propone un conjunto de criterios para comparar lenguajes de programación de manera sistemática. Cada criterio aborda un aspecto distinto del uso real del lenguaje (lectura, escritura, seguridad, costo, portabilidad y eficiencia).

| Criterio | Pregunta clave | Ejemplo de tensión |
|----------|---------------|-------------------|
| **Legibilidad** | ¿Se puede leer código ajeno? | Python vs. Perl |
| **Expresividad** | ¿El lenguaje facilita la expresión? | SQL vs. ensamblador |
| **Seguridad** | ¿Los tipos reducen bugs? | TypeScript vs. JS puro |
| **Costo** | ¿Cuánto cuesta desarrollar y mantener? | — |
| **Portabilidad** | ¿Funciona en distintas plataformas? | Java vs. C |
| **Eficiencia** | ¿Qué tan rápido y cuánta memoria? | C vs. Python |

> No hay lenguaje perfecto — hay **trade-offs**.

---

### [F-04a] Legibilidad

# Legibilidad — el costo cognitivo de leer código

- Es el esfuerzo mental necesario para entender código escrito por otro.
- Impacta directamente el mantenimiento y la colaboración en equipos.
- Lenguajes con sintaxis clara y pocas excepciones tienden a ser más legibles.

---

### [F-04b] Expresividad

# Expresividad — qué tan cercano está el código al problema real

- Refleja cuán fácil es traducir ideas del dominio a código.
- Alta expresividad reduce el código repetitivo y acelera el desarrollo.
- Puede llevar a sintaxis tersa, pero también a estilos difíciles de depurar.

---

### [F-04c] Seguridad

# Seguridad — detección temprana de errores

- Mide cuán pronto el lenguaje detecta errores (tipado estático, análisis estático, chequeos en tiempo de ejecución).
- El tipado estático contribuye a la seguridad al eliminar clases de bugs antes de ejecutar.
- La seguridad también incluye protección contra fallos y vulnerabilidades.

---

### [F-04d] Costo

# Costo — desarrollo, mantenimiento y soporte

- Incluye tiempo de desarrollo, curva de aprendizaje, herramientas y comunidad.
- Lenguajes con ecosistema maduro pueden reducir costos debido a bibliotecas y soporte.

---

### [F-04e] Portabilidad

# Portabilidad — ejecutar en distintas plataformas

- Evalúa qué tan fácil es correr el mismo código en diferentes sistemas.
- La independencia de plataforma puede ser una ventaja crítica en proyectos a gran escala.

---

### [F-04f] Eficiencia

# Eficiencia — tiempo de ejecución y uso de memoria

- Es relevante en sistemas críticos o con recursos limitados.
- Un lenguaje más eficiente puede operar en hardware más modesto o escalar mejor.

---

### [F-05] Pregunta abierta

# ¿Importa el lenguaje si la IA puede escribir en cualquiera?


---

## BLOQUE 2 — Los paradigmas: mapa general (25 min)

---

### [F-06] ¿Qué es un paradigma?

# Un paradigma de programación es una forma de pensar el cómputo

- No es solo sintaxis
- Es el **modelo mental** que estructura cómo describís la solución
- Dos lenguajes con sintaxis muy distintas pueden compartir paradigma (Java ≈ C#)
- Un lenguaje puede implementar varios paradigmas (TypeScript)

---

### [F-07] Arquitectura de Von Neumann

# La máquina de Von Neumann (modelo conceptual)

**Elementos clave:**
- **Memoria unificada:** los datos y el programa conviven en el mismo espacio.
- **Unidad de control:** lee (fetch) una instrucción, la decodifica y la ejecuta.
- **ALU** (unidad aritmético-lógica) + registros temporales en CPU.
- **Bus de datos** común entre CPU y memoria.

**Implicaciones para los lenguajes:**
- Una **variable** es una celda de memoria.
- La **asignación** es una transferencia de datos CPU ↔ memoria.
- La ejecución es **secuencial**: cada instrucción se ejecuta en orden.

> **Directive:** generar gráfico de la máquina Von Neumann (CPU, memoria, bus).

---

### [F-08] El cuello de botella de Von Neumann

# La máquina abstracta tiene un canal único: el bus

```
CPU ←───bus───→ Memoria
         ↑
    cuello de botella
```

- La máquina de Von Neumann define un único canal entre CPU y memoria (el bus).
- Toda lectura/escritura de datos pasa por ese canal.

> **Directive:** generar gráfico de la máquina Von Neumann destacando el bus.

---

### [F-08a] ¿Por qué esto importa para los lenguajes?

# El modelo impone restricciones a los lenguajes "pegados" a la máquina

- Lenguajes imperativos modelan explícitamente este flujo: variables = celdas, asignación = transferencia.
- Eso traslada la complejidad del acceso a memoria al diseño del lenguaje.
- El estado mutable y la ejecución secuencial se vuelven “naturales”, pero limitantes.

> **Directive:** generar diagrama de flujo: variable → memoria → asignación → estado.

---

### [F-08b] ¿Qué paradigmas buscan escapar de esto?

# El cuello de botella empuja hacia otros modelos de cómputo

- El paradigma imperativo lucha con paralelismo y efectos secundarios.
- Paradigmas alternativos proponen reducir la dependencia de la memoria compartida.

**Ejemplos contemporáneos:**
- **Funcional:** lenguajes como Haskell o Clojure adoptan un modelo donde el cómputo es una evaluación de expresiones, minimizando el estado mutable.
- **Lógico:** lenguajes como Prolog usan un modelo de resolución basada en hechos y reglas, reduciendo la dependencia de memoria compartida.

> **Directive:** generar gráfico comparativo (imperativo vs. funcional vs. lógico) en relación al acceso a memoria.

*Fuente: Louden & Lambert, Cap. 1*

---

### [F-09] Los 4 paradigmas fundamentales

# Los 4 paradigmas fundamentales

| Paradigma | Base formal | Unidad | Estado | Ejemplos |
|-----------|-------------|--------|--------|----------|
| **Imperativo** | Máquina de Von Neumann | Instrucción | Mutable | C, Go, Pascal |
| **OO** | Imperativo + encapsulamiento | Objeto / mensaje | Mutable (encapsulado) | Java, C#, Smalltalk, Dart |
| **Funcional** | Cálculo lambda (Church, 1936) | Función | **Inmutable** | Haskell, Clojure, LISP |
| **Lógico** | Lógica simbólica (resolución) | Relación / hecho | Sin estado | Prolog |

> *"El OO es una extensión del imperativo — no nació de cero. El funcional y el lógico tienen raíces matemáticas pre-computadoras."*

**Nota:** Los lenguajes *multiparadigma* (TypeScript, Python, Scala) combinan varios de estos — ver F-10.

---

### [F-10] Dominios de aplicación

# ¿Cuándo usar cada paradigma?

| Paradigma | Dominio ideal | Lenguaje representativo |
|-----------|--------------|------------------------|
| Imperativo | Sistemas operativos, drivers, embebidos | C |
| OO | Aplicaciones empresariales, GUIs | Java, C# |
| Funcional | Finanzas de alta confiabilidad, compiladores, IA | Haskell, Clojure |
| Lógico | IA simbólica, sistemas expertos, NLP | Prolog |
| Multiparadigma | Web full-stack, APIs, datos, IA aplicada | TypeScript, Python |

---

## BLOQUE 3 — Paradigma imperativo y máquina abstracta (20 min)

---

### [F-11] La escalera de abstracciones

# Todo lenguaje ocupa un nivel en la escalera de abstracción

```
Frameworks (React, Django)     ← Nivel 3: abstracción sobre el lenguaje y la plataforma
        ↑
Java, Python, TypeScript        ← Nivel 2: GC, tipos, ecosistema, runtime/VM (abstracción de plataforma)
        ↑
C, Rust, Go                    ← Nivel 1: estructura, funciones, tipos básicos
        ↑
LC-3, ensamblador               ← Nivel 0: registros, saltos, direcciones
```

**Al subir:** más legibilidad, más expresividad, más portabilidad (y más abstracciones sobre el lenguaje)
**Al bajar:** más control, más eficiencia (y más cercanía al hardware)

> *"¿Qué abstrae? ¿Qué perdí?"* — La pregunta que guía esta materia

**Nota:** los lenguajes modernos también ofrecen abstracción de plataforma (JVM, CLR, runtime), y los frameworks construyen una capa adicional de abstracciones sobre ese entorno.
*Fuente: Louden & Lambert, Cap. 1 — Fig. 1.4 y 1.5*

---

### [F-12] Von Neumann → código imperativo (correspondencia directa)

# El paradigma imperativo abstrae el hardware

| Hardware (Von Neumann) | Concepto en lenguaje imperativo |
|------------------------|--------------------------------|
| Celda de memoria con dirección | Variable con nombre |
| Transferencia CPU ↔ memoria | Instrucción de asignación (`x = 5`) |
| Salto condicional del procesador | `if`, `while`, `for` |
| Conjunto de celdas en un instante | **Estado** del programa |
| Sucesión de instrucciones | **Cómputo** = sucesión de estados |

> El paradigma imperativo no es convención — es abstracción directa del hardware.

---

### [F-13] Mismo algoritmo — 3 niveles

# Suma de valores absolutos: LC-3 vs. C

**Ensamblador LC-3** (13 líneas, opaco):
```
        AND R0, R0, #0    ; acc = 0
        LEA R1, DATA      ; puntero al inicio del array
        AND R2, R2, #0
        ADD R2, R2, #10   ; contador = 10
LOOP    LDR R3, R1, #0    ; cargar elemento
        BRzp POS          ; si >= 0, saltar
        NOT R3, R3        ; negar (complemento a 2)
        ADD R3, R3, #1
POS     ADD R0, R0, R3    ; acc += abs
        ADD R1, R1, #1    ; avanzar puntero
        ADD R2, R2, #-1   ; contador--
        BRp LOOP          ; repetir si queda
```

**C — imperativo de alto nivel** (5 líneas, legible):
```c
int suma_abs(int arr[], int n) {
    int acc = 0;
    for (int i = 0; i < n; i++)
        acc += (arr[i] < 0) ? -arr[i] : arr[i];
    return acc;
}
```

*(¿Qué haría TypeScript diferente? → Bloque 4)*

---

### [F-14] Máquina abstracta, interpretación y compilación

# Todo lenguaje define una "máquina abstracta" — Gabbrielli & Martini, Cap. 1

**Dos formas puras de implementar un lenguaje:**

```
Interpretación pura:
  Programa → [Intérprete en tiempo de ejecución] → Ejecución
  Flexible, más lento

Compilación pura:
  Programa → [Compilador] → Lenguaje objeto → Ejecución
  Rápido, menos flexible
```

**En la práctica:** siempre existe un **lenguaje intermedio**
→ JVM, Python bytecode, JavaScript (de TypeScript)

---

## BLOQUE 4 — Intro a TypeScript como lenguaje multiparadigma (30 min)

---

### [F-15] ¿Por qué TypeScript en 2026?

# TypeScript como lenguaje del cursado

| Razón | Detalle |
|-------|---------|
| **Ecosistema** | npm + 2.3M paquetes · frontend + backend · Node/Deno/Bun |
| **Tipos** | Sistema de tipos más expresivo de los lenguajes mainstream |
| **IA** | Los modelos generan TS con alta fidelidad → más fácil auditar |
| **Multiparadigma** | Imperativo + Funcional + OO en el mismo archivo |
| **Relevancia** | Lenguaje #1 o #2 en encuestas de desarrolladores 2023–2025 |


---

### [F-15a] ¿Por qué la IA obtiene mejor TypeScript?

# La IA funciona mejor con TypeScript porque...

- Los modelos se entrenan con enormes conjuntos de código (GitHub, StackOverflow, npm) donde TypeScript es abundante y consistente.
- Las anotaciones de tipo reducen la ambigüedad semántica: el código es más fácil de inferir, corregir y completar.
- TypeScript fomenta prácticas robustas (tests, linting — revisa estilo código, formateo), lo que eleva la calidad del código de entrada al entrenar los modelos.
- La salida de la IA es más fácil de **auditar** y **testear**, porque el compilador añade una barrera de verificación antes de ejecutar.
- Como resultado, los prompts que piden código suelen generar TS más confiable que JavaScript dinámico.

> *Fuente: Schmidt & Runfola (2025); Louden & Lambert, Cap. 1 (máquinas abstractas).* 

---

### [F-16] TypeScript como máquina intermedia (el pipeline)

# TypeScript = ejemplo vivo de Gabbrielli Cap. 1

```
archivo.ts
     ↓  [tsc — compilador TypeScript]       ← verificación de tipos
archivo.js  ←── LENGUAJE INTERMEDIO
     ↓  [V8 / Node.js / Deno — JIT]
   Ejecución en CPU
```

> **Directive:** generar gráfico de pipeline TS → JS → V8/Deno destacando el rol de la verificación de tipos antes de ejecutar.

**Comparación:**

| Lenguaje | Paso 1 | Intermediario | Tiempo de ejecución |
|----------|--------|---------------|---------|
| TypeScript | tsc | .js | V8 / Node / Deno |
| Java | javac | .class (bytecode) | JVM |
| Python | CPython (implícito) | bytecode (.pyc) | CPython VM |

> No es "interpretado" ni "compilado" en sentido puro.
> Usa **máquina intermedia** — exactamente como predice Gabbrielli.

---

### [F-17] El mismo problema: imperativo en TypeScript

# TypeScript — estilo imperativo

```typescript
function sumaAbs(arr: number[]): number {
    let acc = 0;
    for (let i = 0; i < arr.length; i++) {
        acc += arr[i] < 0 ? -arr[i] : arr[i];
    }
    return acc;
}

console.log(sumaAbs([3, -1, 4, -1, 5])); // → 14
```

**Diferencias respecto de C:**
- Tipos anotados (`: number[]`, `: number`)
- Sin gestión manual de punteros
- Mismo paradigma — **imperativo**

---

### [F-18] El mismo problema: funcional en TypeScript

# TypeScript — estilo funcional

```typescript
const sumaAbs = (arr: number[]): number =>
    arr.map(x => Math.abs(x))
       .reduce((acc, x) => acc + x, 0);

console.log(sumaAbs([3, -1, 4, -1, 5])); // → 14
```

**¿Qué cambió?**
- Sin `let` → sin mutación de estado
- Sin loop explícito
- `map` y `reduce` son **funciones de orden superior** (reciben funciones como argumento)

> En Scheme (LISP, 1960): `(reduce + (map abs lista))`
> La misma idea tiene 60 años. TypeScript la adopta en 2012.

*Fuente: Louden & Lambert, Cap. 1*

---

### [F-19] Sistema de tipos básico

# TypeScript: tipos estáticos que aumentan la seguridad

```typescript
// Anotaciones explícitas
let nombre: string = "Paradigmas";
let año: number = 2026;

// Inferencia automática
let materia = "Paradigmas";  // tipo: string

// Interfaces
interface Alumno {
    nombre: string;
    legajo: number;
    notas: number[];
}

// El compilador detecta errores ANTES de ejecutar:
sumaAbs(["hola", "mundo"]);
// ❌ Error: Argument of type 'string[]' is not
//    assignable to parameter of type 'number[]'
```

> **Seguridad** (criterio Sebesta #3): el compilador como primer revisor.

---

### [F-20] TypeScript como "acelerador de paradigma"

# TypeScript: ¿qué paradigma usamos?

*Mismo problema — tres estilos válidos:*

```typescript
const datos = [3, -1, 4, -1, 5];

// ← imperativo: variable mutable + loop
let acc = 0;
for (const x of datos) acc += Math.abs(x);

// ← funcional: sin estado, composición de funciones
const result = datos.map(Math.abs).reduce((a, b) => a + b, 0);

// ← OO: dato + comportamiento encapsulados
class Calculadora {
    sumaAbs(arr: number[]): number {
        return arr.reduce((a, x) => a + Math.abs(x), 0);
    }
}
```

> **Los tres producen `14`. La elección es del programador.**
> La elección de paradigma determina la legibilidad, testabilidad y mantenibilidad.
> A lo largo de la materia: vamos a escribir y comparar los tres estilos.

---

### [F-20a] Introducción al paradigma funcional

# Paradigma funcional: cálculos sin efectos secundarios

- El cómputo se define como la evaluación de expresiones.
- El estado no cambia: las funciones son mapeos de entrada → salida.
- Ventajas: razonamiento matemático, paralelismo, tests más predecibles.

> **Directive:** generar gráfico comparando función pura vs función con estado (mutación).

---

### [F-20b] Funciones puras y composición

# Composición: construir programas como cadenas de funciones

- Una función es pura si siempre devuelve el mismo resultado para los mismos argumentos.
- Componer funciones pequeñas permite razonar localmente y reutilizar código.

```typescript
const doble = (x: number) => x * 2;
const suma = (a: number, b: number) => a + b;
const dobleYSuma = (x: number, y: number) => suma(doble(x), doble(y));
```

> **Directive:** generar gráfico de composición de funciones (f ∘ g).

---

### [F-20c] Inmutabilidad y datos persistentes

# Cambiar sin mutar: estructuras inmutables

- En vez de modificar datos, se crean nuevas versiones (copias con cambios).
- Esto reduce errores y facilita la concurrencia.
- TypeScript usa `const` y prácticas funcionales; lenguajes puramente funcionales usan estructuras persistentes (Clojure).

```typescript
const lista = [1, 2, 3];
const nuevo = [...lista, 4]; // no muta la lista original
```

> **Directive:** generar gráfico “copia con cambios” vs “mutación en sitio”.

---

### [F-20d] Lenguajes funcionales más puros

# TypeScript permite el estilo funcional, pero hay lenguajes más “puros”

- **Clojure** (LISP sobre JVM) insiste en inmutabilidad y funciones puras.
- **Haskell** es un lenguaje funcional puro: los efectos se manejan explícitamente con mónadas.
- En este curso usaremos TypeScript para practicar ideas funcionales y veremos ejemplos de Clojure más adelante.

> *Fuente: Louden & Lambert, Cap. 1; Hickey (2008) sobre Clojure.*

> **Directive:** generar gráfico comparando TypeScript (híbrido) con Clojure (funcional puro).

---

### [F-20e] Introducción al paradigma lógico

# Paradigma lógico: programar declarando “qué” en lugar de “cómo”

- El programa describe hechos y reglas; el motor (intérprete) hace la inferencia.
- No se escribe el control: el sistema busca soluciones que satisfagan las restricciones.
- Ideal para problemas de búsqueda, reglas, y consultas (bases de conocimiento).

> **Directive:** generar gráfico de un motor de inferencia (hechos + reglas → solución).

---

### [F-20f] Hechos y reglas en Prolog

# Programar con hechos y reglas

```prolog
padre(alan, bob).
padre(bob, carla).
ancestro(X, Y) :- padre(X, Y).
ancestro(X, Y) :- padre(X, Z), ancestro(Z, Y).
```

- `padre/2` son hechos.
- `ancestro/2` es una regla recursiva que define la relación.

> **Directive:** generar gráfico que muestre hechos + regla → cadena de inferencia.

---

### [F-20g] Backtracking y unificación

# Cómo Prolog busca soluciones

- El motor expande posibilidades y retrocede (backtracking) cuando no encuentra solución.
- La unificación empareja variables con términos para hacer coincidir hechos y reglas.

```prolog
?- ancestro(alan, carla).
% Sí: unifica y prueba caminos.
```

> **Directive:** generar gráfico de un árbol de búsqueda con backtracking.

---

### [F-20h] Aplicaciones del paradigma lógico

# ¿Para qué sirve la programación lógica?

- Sistemas expertos y motores de reglas (diagnóstico, planificación).
- Consultas sobre bases de conocimiento (preguntas declarativas).
- En IA simbólica se usa para modelar conocimiento y razonamiento.

> **Directive:** generar gráfico de un sistema experto (reglas + hechos → decisión).

---

## BLOQUE 5 — IA Generativa y los paradigmas (15 min)

---

### [F-21] El cambio de rol del programador

# El trabajo del programador cambió radicalmente

**Antes (pre-IA generativa):**
```
70% codificación manual + depuración
30% comprensión del problema
```

**Hoy (con IA generativa):**
```
20% codificación manual
50% prompting, supervisión y orquestación de IA    ← nuevo
30% formulación del problema
```

> *"Natural language has become the new compiler,*
> *and developer's focus is migrating from syntax*
> *and semantics to **strategy**."*

*Fuente: Schmidt & Runfola (2025), arXiv:2511.17696*

---

### [F-22] La jerarquía de proficiencia en IA

# ¿Dónde apuntan los graduados de esta materia?

```
┌─────────────────────────────────────────────────────┐
│  AI MASTERY   — construir, optimizar y auditar IA   │
│               — investigadores e ingenieros de IA   │
├─────────────────────────────────────────────────────┤
│  AI FLUENCY   — diseñar prompts, criticar modelos,  │  ← USTEDES
│               — construir soluciones                │
│               — requiere pensamiento computacional  │
├─────────────────────────────────────────────────────┤
│  AI LITERACY  — leer e interpretar output de IA     │
│               — cualquier usuario                   │
└─────────────────────────────────────────────────────┘
```

> AI Fluency sin paradigmas = imposible verificar lo que genera la IA.

*Fuente: Schmidt & Runfola (2025), Fig. 12*

---

### [F-23] Demo en vivo — La IA elige paradigmas

# Prompt 1: versión base

```
"Escribí una función que devuelva la suma
de los valores absolutos de una lista de números"
```

**Observar:** ¿Qué paradigma eligió la IA por defecto?

---

### [F-24] Demo en vivo — Restricción de paradigma

# Prompt 2: paradigma funcional explícito

```
"Implementá lo mismo en estilo funcional puro,
sin mutación de estado, sin variables intermedias"
```

**Verificar:**
- ¿Entendió la restricción?
- ¿Usó `reduce` / `map`?
- ¿Hay `let` o mutación oculta?

---

### [F-25] Demo en vivo — Máquinas abstractas

# Prompt 3: verificación de comprensión

```
"Explicá qué máquina abstracta ejecuta
este código TypeScript"
```

**Verificar:**
- ¿Explica el pipeline `.ts → .js → V8`?
- ¿Distingue el compilador (`tsc`) del tiempo de ejecución (`V8`)?
- ¿Menciona el lenguaje intermedio?

---

### [F-26] El loop "trust but verify"

# Cómo trabajar con IA en programación — Schmidt & Runfola, Fig. 8

```
1. Formular el problema con precisión
         ↓
2. Hacer el prompt a la IA
         ↓
3. Revisar con conocimiento de dominio
   • ¿Qué paradigma usó?
   • ¿Es correcto semánticamente?
         ↓
4. Testear con casos borde
         ↓
5. Refinar el prompt o escribir manualmente
         ↑
   (repetir si es necesario)
```

> ⚠️ Demasiada dependencia en IA atrofia habilidades cognitivas.
> Los fundamentos son el antídoto.

---

## CIERRE (10 min)

---

### [F-27] Mapa de la materia — los 15 temas

# Cómo se conectan los temas del cursado

```
Temas 1–2      Fundamentos: lenguajes, paradigmas, sintaxis, semántica
    ↓
Temas 3–6      Paradigma funcional (TypeScript + Python)
    ↓
Tema 7          Paradigma lógico (Prolog)
    ↓
Tema 8          Paradigma OO (TypeScript)
    ↓
Temas 9–14     Conceptos transversales:
                variables · tipos · control · módulos · polimorfismo
    ↓
Tema 15         Concurrencia y paralelismo
```

> *"Lo que vimos hoy es el mapa. Las próximas 15 clases son el territorio."*

---

### [F-28] Adelanto — Clase 2: Sintaxis y Semántica

# Próxima clase: ¿qué hace un programa **válido**?

```typescript
if (x !== 0) y = 1 / x;
```

**¿Qué pasa si no hay `else`?**

- **Sintaxis:** ¿es un programa bien formado? SÍ
- **Semántica:** ¿qué hace exactamente? → lo define el lenguaje

> La diferencia entre "esto compila" y "esto hace lo que quiero"
> es la diferencia entre sintaxis y semántica.

**Para la próxima clase:**
- Instalar TypeScript → `npm install -g typescript`
- O acceder a: [playground.deno.land](https://playground.deno.land) / [typescriptlang.org/play](https://www.typescriptlang.org/play)

*Fuente: Louden & Lambert, Cap. 1 §1.4*

---

## Resumen de filminas

| Rango | Bloque | Filminas | Minutos |
|-------|--------|----------|---------|
| F-00 | Portada | 1 | — |
| F-01 a F-05 | Bloque 1: ¿Por qué LP? | 5 | 20 |
| F-06 a F-10 | Bloque 2: Paradigmas | 5 | 25 |
| F-11 a F-14 | Bloque 3: Imperativo + Máquina Abstracta | 4 | 20 |
| F-15 a F-20h | Bloque 4: TypeScript | 15 | 40 |
| F-21 a F-26 | Bloque 5: IA Generativa | 6 | 15 |
| F-27 a F-28 | Cierre | 2 | 10 |
| **Total** | | **37 filminas** | **145 min** |
