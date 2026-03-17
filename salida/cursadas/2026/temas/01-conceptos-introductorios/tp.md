# TP — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Tipo:** Repo GitHub Classroom (autograding)
> **Agente:** Aux. Valeria (tp-designer)
> **Fecha:** 2026-03-10
> **Trazado desde:** `temas/01-conceptos-introductorios/minuta.md` · `filminas.md`
> **Output asociado:** `temas/01-conceptos-introductorios/autograde-repo/`

---

## Configuración del Quiz

| Campo | Valor |
|-------|-------|
| Título | TP 01 — Conceptos Introductorios + Intro a TypeScript |
| Tiempo límite | 30 minutos |
| Intentos permitidos | 1 |
| Puntaje por pregunta | 1 punto (11 pts total) |
| Penalización por respuesta incorrecta | 0 |
| Mostrar respuestas correctas al alumno | Sí, al completar |
| Categoría Moodle | TP01-ConceptosIntroductorios |

---

## Instrucciones para el alumno

Este quiz evalúa los conceptos trabajados en la Clase 1. Algunas preguntas requieren recordar ejemplos y código específicos presentados en clase — no busques las respuestas en internet ni en IA: varias preguntas contienen referencias que solo podés responder correctamente si estuviste en clase. Tenés **30 minutos** y **1 intento**.

---

## Preguntas

> ⚠️ Columna `[TRAMPA]` visible solo para el docente — no aparece en el quiz.

---

### P01 — Criterio Sebesta aplicado al error de TypeScript en clase

**Trazabilidad:** Bloque 4 — F-38, demo en vivo de error de tipos

**Enunciado:**
En clase vimos en vivo este error de TypeScript al pasar `["hola", "mundo"]` a la función `sumaAbs`:

```
Argument of type 'string[]' is not assignable to parameter of type 'number[]'
```

El compilador (`tsc`) detectó este problema **antes de ejecutar el programa**. Según los criterios de Sebesta (F-06), ¿cuál es el criterio que mejor describe esta capacidad del lenguaje?

**Opciones:**
- ✅ **Confiabilidad** — el sistema de tipos reduce bugs antes de la ejecución
- ~ Legibilidad — la facilidad para leer el mensaje de error
- ~ Portabilidad — la capacidad de ejecutar en múltiples plataformas
- ~ Escribibilidad — la facilidad para expresar la intención del programador

---

### P02 — Pipeline de ejecución de TypeScript ⚠️ [TRAMPA: DATO INCORRECTO PLANTADO]

**Trazabilidad:** Bloque 4 — F-35, pipeline dibujado en clase

**Enunciado:**
En clase dibujamos el pipeline completo de TypeScript (F-35). Evaluá la siguiente afirmación:

> *"TypeScript compila a bytecode de la JVM (Java Virtual Machine), que luego es interpretado y ejecutado por la máquina virtual de Java — a la manera de Java y Kotlin."*

¿Es correcta esta afirmación?

**Opciones:**
- ✅ **Es incorrecta** — TypeScript compila a JavaScript (`.js`), que es ejecutado por V8, Node.js o Deno; no interviene ninguna JVM
- ~ Es correcta — TypeScript y Kotlin comparten la misma máquina virtual por diseño
- ~ Es parcialmente correcta — TypeScript puede compilar a JVM opcionalmente con `tsc --target jvm`
- ~ Es correcta — V8 es el motor JVM de Google Chrome, por eso el flujo es equivalente

> 🎯 **NOTA DOCENTE (trampa):** La afirmación es deliberadamente falsa. La IA tiende a validarla o confundirse porque asocia TypeScript con Java/Kotlin en ecosistemas empresariales. Un alumno que vio la filmina F-35 sabe que el pipeline es `archivo.ts → tsc → archivo.js → V8/Deno`.

---

### P03 — Código C de clase: variable acumuladora ⚠️ [TRAMPA: REFERENCIA A CÓDIGO DE CLASE]

**Trazabilidad:** Bloque 3 — F-23, ejemplo comparativo en tres niveles

**Enunciado:**
En clase (F-23) mostramos este fragmento de código C como ejemplo del **paradigma imperativo puro**:

```c
int suma_abs(int arr[], int n) {
    int acc = 0;
    for (int i = 0; i < n; i++)
        acc += (arr[i] < 0) ? -arr[i] : arr[i];
    return acc;
}
```

¿Cuál es la variable que actúa como **acumulador mutable** y constituye evidencia directa del estilo imperativo?

**Opciones:**
- ✅ `acc`
- ~ `arr`
- ~ `n`
- ~ `i`

> 🎯 **NOTA DOCENTE (trampa):** La IA podría elegir `i` (variable de iteración, también mutable) o no distinguir. La respuesta pedagógicamente relevante es `acc` porque es la que acumula el **estado** del cómputo — que es exactamente lo que define el paradigma imperativo según lo discutido.

---

### P04 — Von Neumann y el paradigma imperativo

**Trazabilidad:** Bloque 2 — F-15 · F-16

**Enunciado:**
En clase explicamos que el paradigma imperativo surgió como abstracción directa de la arquitectura de Von Neumann. Según lo discutido, ¿qué elemento del paradigma imperativo **mapea directamente a una celda de memoria**?

**Opciones:**
- ✅ Una variable
- ~ Una función
- ~ Una clase
- ~ Un predicado lógico (como en Prolog)

---

### P05 — Demo de IA en clase: evidencia de imperativo ⚠️ [TRAMPA: REFERENCIA A CLASE]

**Trazabilidad:** Bloque 5 — F-42, Prompt 1 de la demo en vivo

**Enunciado:**
En la demo de IA (F-42), el docente usó este prompt **sin restricción de paradigma**:

> *"Escribí en TypeScript una función que devuelva la suma de los valores absolutos de una lista de números"*

La IA generó código con la variable `sum` declarada con `let` y un loop `for...of` con mutación acumulativa. ¿Cuál fue el rasgo que el docente identificó como **evidencia del paradigma imperativo** en ese output?

**Opciones:**
- ✅ El uso de `let sum = 0` (variable mutable) y la mutación acumulativa dentro del loop — estado que cambia instrucción a instrucción
- ~ El uso de tipos estáticos como `number[]` — que son propios del sistema de tipos de TypeScript
- ~ La declaración con `function` en lugar de arrow function — que indica estilo clásico imperativo
- ~ El nombre de la variable `numbers` en inglés — convención del paradigma imperativo

> 🎯 **NOTA DOCENTE (trampa):** La IA puede razonar correctamente pero sin referencia al momento específico de clase. Un alumno presente sabe que el marcador principal fue `let sum = 0` — variable mutable que muta en el loop — exactamente lo que vinculamos con Von Neumann.

---

### P06 — Cuello de botella de Von Neumann: ¿qué bus? ⚠️ [TRAMPA: TÉRMINO INCORRECTO PLANTADO]

**Trazabilidad:** Bloque 2 — F-16 · F-18, Louden & Lambert Cap. 1

**Enunciado:**
Según Louden & Lambert (Capítulo 1), discutido en la filmina F-16, el **cuello de botella de Von Neumann** surge de la limitación de velocidad de un bus específico. ¿Entre qué componentes está ese bus?

**Opciones:**
- ✅ Entre la **CPU** y la **memoria** (RAM)
- ~ Entre la GPU y la memoria de video (VRAM)
- ~ Entre la CPU y el disco rígido (almacenamiento secundario)
- ~ Entre los núcleos del procesador en sistemas multicore

> 🎯 **NOTA DOCENTE (trampa):** Las opciones incorrectas suenan plausibles. La GPU es un distractor efectivo porque la IA moderna asocia cómputo paralelo con GPU. La respuesta correcta es explícita en la filmina F-16 y en el texto de Louden & Lambert Cap. 1.

---

### P07 — LISP 1960: aporte al paradigma funcional

**Trazabilidad:** Bloque 1 — F-05, timeline histórico

**Enunciado:**
La perspectiva histórica de F-05 ubicó a **LISP (1960)** como un hito clave. ¿Cuál fue el concepto que LISP introdujo y que se convirtió en la base del paradigma funcional?

**Opciones:**
- ✅ Las **funciones como datos de primera clase** y la **recursión** — base del cálculo lambda
- ~ La orientación a objetos con encapsulamiento y mensajes entre objetos
- ~ Los tipos estáticos y la verificación formal en tiempo de compilación
- ~ La ejecución concurrente de múltiples hilos de código

---

### P08 — Escalera de abstracciones: ¿qué se pierde al subir?

**Trazabilidad:** Bloque 3 — F-21, metáfora de la escalera de Gabbrielli

**Enunciado:**
En la "escalera de abstracciones" presentada en F-21 (Gabbrielli), el docente planteó un trade-off central. Al **subir** niveles de abstracción (de ensamblador → C → TypeScript → frameworks), ¿qué se **pierde**?

**Opciones:**
- ✅ **Control y eficiencia** de ejecución — menor acceso directo al hardware
- ~ Legibilidad y expresividad del código
- ~ Confiabilidad y capacidad de verificación estática
- ~ Portabilidad entre distintas plataformas

---

### P09 — TypeScript multiparadigma: ¿existe un paradigma predeterminado?

**Trazabilidad:** Bloque 4 — F-39, cierre del bloque TypeScript

**Enunciado:**
Al cerrar el Bloque 4 (F-39), el docente afirmó algo sobre TypeScript como lenguaje multiparadigma. ¿Cuál de las siguientes opciones refleja **lo que se dijo en clase**?

**Opciones:**
- ✅ TypeScript **no obliga** a ningún paradigma — la elección es del programador, lo que implica mayor responsabilidad de consistencia de estilo en equipos
- ~ TypeScript implementa el paradigma **funcional como predeterminado** — el imperativo requiere deshabilitar las reglas del compilador
- ~ TypeScript es multiparadigma pero `tsc` rechaza código con **variables mutables** (`let`) sin configuración especial
- ~ Solo JavaScript puro permite el paradigma imperativo; TypeScript fuerza el funcional por su sistema de tipos avanzado

---

### P10 — Cierre de la clase: ¿importa el lenguaje si la IA puede escribir en cualquiera?

**Trazabilidad:** Bloque 1 — F-13 (pregunta abierta) + Bloque 5 — F-40 (cierre)

**Enunciado:**
En el Bloque 1 (F-13) se dejó abierta la pregunta: *"¿Importa el lenguaje si la IA puede escribir en cualquiera?"*. En el Bloque 5 (F-40) se retomó y se respondió usando datos de Schmidt & Runfola (2025). ¿Cuál fue la respuesta del docente?

**Opciones:**
- ✅ **Sí, importa más que nunca** — porque el trabajo actual es supervisar, criticar y verificar el código de la IA, y para eso se necesitan conocimientos de paradigmas y semántica
- ~ No, el lenguaje dejó de importar — la IA abstrae completamente esa decisión por el programador
- ~ Solo importa para lenguajes de sistemas (C, Rust); para TypeScript la IA es autónoma y confiable sin supervisión
- ~ Importa menos que antes, pero todavía es relevante solo para optimización de performance

---

### P11 — Mutación de estado: ¿cuál de estos fragmentos es imperativo?

**Trazabilidad:** Bloque 3 + Bloque 4 — OA3 (distinguir imperativo vs funcional por mutación de estado)

**Enunciado:**
Analizar los siguientes cuatro fragmentos TypeScript. ¿Cuál de ellos es un ejemplo **inequívoco de paradigma imperativo**, independientemente del resultado que produce?

```typescript
// Fragmento A
const doble = (arr: number[]): number[] => arr.map(x => x * 2);

// Fragmento B
function doble(arr: number[]): number[] {
    let result: number[] = [];
    for (const x of arr) result.push(x * 2);
    return result;
}

// Fragmento C
const doble = (arr: number[]): number[] => arr.map(x => x * 2);

// Fragmento D
const doble = (arr: number[]): number[] =>
    arr.reduce((acc: number[], x) => [...acc, x * 2], []);
```

**Opciones:**
- ✅ **Fragmento B** — declara `let result = []` (variable mutable) y la muta instrucción a instrucción con `push` dentro del loop
- ~ Fragmento A — por usar sintaxis `function` en lugar de arrow function
- ~ Fragmento C — por nombrar la función en mayúsculas, convención del paradigma OO
- ~ Fragmento D — por usar `reduce` con acumulador, que internamente mantiene estado mutable

> 🎯 **NOTA DOCENTE:** Esta pregunta no tiene referencia a un momento específico de clase — evalúa comprensión transferible de OA3. El distractor D es efectivo porque `reduce` recibe un acumulador `acc`, que *parece* una variable mutable, pero la inmutabilidad del estilo funcional se mantiene: `acc` es el valor que devuelve la función en cada paso, no una variable que se reasigna externamente.

### P12 — Loop "trust but verify" con IA

**Trazabilidad:** Bloque 5 — F-45 (loop "trust but verify")

**Enunciado:**
En la clase se presentó el loop "trust but verify" como una forma de usar IA generativa de manera responsable. ¿Cuál es el paso que sigue inmediatamente después de pedirle algo a la IA (prompt)?

**Opciones:**
- ✅ **Verificar el output contra el conocimiento del dominio y hacer tests**
- ~ Volver a escribir el prompt sin revisar el resultado, confiando en la IA
- ~ Compartir el output directamente con el equipo sin validarlo
- ~ Usar la IA para generar un prompt mejor sin leer el output original

---

## Resumen de trampas anti-IA

| Pregunta | Tipo de trampa |
|----------|---------------|
| P02 | Dato incorrecto plantado — "JVM" en lugar de V8/Deno |
| P03 | Referencia a código específico de clase (nombre exacto de variable) |
| P05 | Referencia a demo en vivo de clase (output exacto de la IA) |
| P06 | Término incorrecto plantado — "GPU" en lugar de CPU |
| P09 | Respuesta contraintuitiva — la IA tiende a atribuir defaults funcionales a TypeScript |

---

## Detección sistemática post-entrega

1. Exportar respuestas desde Moodle → **Calificaciones → Exportar CSV**
2. Correr CSV por **GPTZero API** en lote (plan free: 10k palabras/mes; plan básico ~$10/mes)
3. Comparar respuestas entre alumnos buscando frases idénticas o muy similares en P02, P05 y P09
4. Alumnos que respondieron P02 con opciones incorrectas (validaron la JVM) → señal de uso de IA sin verificación
5. Alumnos que respondieron P03 con `i` o `arr` → posible IA que priorizó "variable de loop" sin contexto semántico de la clase
