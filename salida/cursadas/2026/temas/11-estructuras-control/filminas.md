# Filminas - Tema 11: Expresiones y Estructuras de Control

> Curso: Laboratorio de Programación y Lenguajes · UNTDF IDEI 2026
> Cobertura: F-00 a F-44 (45 filminas)
> Duración: 180 minutos (constraint absoluto)
> Lenguaje principal: TypeScript
> Referencia principal: Sebesta, Concepts of Programming Languages, caps. 7–8
> Referencias auxiliares: Gabbrielli-Martini caps. 4–6, Louden cap. 8
> Baseline de corrección: clase_dada.txt (859 líneas)

---

## PORTADA

---

### [F-00] Portada

@tipo: portada
@layout: portada
@imagen: background
@prompt-imagen: composición abstracta minimalista con un árbol sintáctico (nodos y ramas) que se transforma gradualmente en flechas de flujo de control; paleta azul profundo y acentos ámbar; sin texto, estilo diagrama técnico limpio

# Expresiones y Estructuras de Control

Paradigmas y Lenguajes de Programación · Tema 11 · Módulo VIII
UNTDF IDEI 2026

---

### [F-01] Pregunta de apertura

@tipo: socratica
@layout: socratica
@imagen: none

# ¿Dos expresiones equivalentes siempre se comportan igual?

## Pueden diferir por

- Precedencia
- Asociatividad
- Orden de evaluación
- Efectos colaterales
- Coerciones del lenguaje

## Ejemplo TypeScript

```ts
let x = 1
const r = x++ + x
```

¿El problema está en la matemática o en la semántica del lenguaje?

---

## BLOQUE A — Fundamentos de expresiones y semántica

---

### [F-02] Objetivos

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Al finalizar este tema el estudiante podrá

- Distinguir expresión, sentencia y efecto colateral
- Explicar precedencia y asociatividad
- Analizar orden de evaluación
- Reconocer conversiones, coerciones y sobrecarga de operadores
- Justificar short-circuit
- Comparar estructuras de selección e iteración
- Evaluar decisiones de diseño de lenguajes modernos

---

### [F-03] Mapa conceptual del tema

@tipo: diagrama
@layout: diagrama
@imagen: content
@prompt-imagen: diagrama de flujo vertical con cajas conectadas por flechas descendentes: Expresiones → Evaluación → Asignación y efectos → Booleanos y short-circuit → Selección → Iteración → Saltos restringidos y mecanismos modernos; estilo blueprint técnico, paleta azul/gris, sin texto legible solo formas

# Expresiones → Evaluación → Control

## Ejes del tema

- **Expresiones** → **Evaluación** → **Asignación y efectos**
- **Booleanos y short-circuit** → **Selección**
- **Iteración** → **Saltos restringidos y mecanismos modernos**

---

### [F-04] Expresión y sentencia

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Expresión produce valor · Sentencia causa efecto

## Distinción fundamental

- **Expresión**: construcción sintáctica que se evalúa.
- **Sentencia**: unidad ejecutable del programa.
- En lenguajes imperativos, muchas sentencias modifican estado.
- En TypeScript, una asignación también es una expresión.

```ts
let x = 0
let y = (x = 5)
```

---

### [F-05] Por qué esta distinción importa

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Si una expresión solo calcula, es más fácil razonar

## Riesgo semántico

- Si una expresión solo calcula, es más fácil razonar.
- Si una expresión además muta estado, aparece riesgo semántico.
- La misma sintaxis puede mezclar cálculo y efecto.

```ts
let total = 0
function sumar(x: number): number {
    total += x
    return total
}
```

---

### [F-06] AST y parseo

@tipo: diagrama
@layout: diagrama
@imagen: content
@prompt-imagen: árbol sintáctico abstracto binario con raíz "+", hijo izquierdo "a" y hijo derecho "*" que tiene hijos "b" y "c"; nodos circulares azul oscuro, aristas grises, estilo diagrama técnico limpio sobre fondo claro

# El árbol sintáctico abstracto fija la semántica de la expresión

## Cómo el AST determina semántica

- La **precedencia** de operadores determina la estructura del árbol de parseo.
- La **asociatividad** resuelve empates entre operadores de igual precedencia.
- El AST captura estructura, no evaluación: es una representación intermedia.
- Parseo y evaluación son **fases distintas**: el árbol no garantiza orden de evaluación temporal.
- El operador con mayor precedencia queda más profundo en el árbol → se evalúa primero.

```ts
const r = a + b * c   // a + (b * c)
```

---

### [F-07] Precedencia de operadores

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# La precedencia determina la agrupación

## Reglas de prioridad

- Multiplicación precede a suma.
- Los paréntesis expresan intención.
- La tabla de precedencia es decisión de diseño.

## Ejemplo

```ts
const r = a + b << c
```

¿Se suma antes o se desplaza antes?

---

### [F-08] Precedencia no es una ley universal

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Leer una expresión requiere conocer el lenguaje

## Variación entre lenguajes

- Las reglas aritméticas suelen coincidir.
- Las reglas lógicas, bit a bit y de asignación varían.

```ts
const a = 2 + 3 * 4      // 14
const b = (2 + 3) * 4    // 20
```

- TypeScript, Java, Kotlin: reglas similares.
- Python agrega `**` como operador de exponenciación.
- Scheme evita el problema usando notación prefija.

---

### [F-09] Asociatividad

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Mismo nivel de precedencia: ¿izquierda o derecha?

## Resolución de empates

- **Asociatividad izquierda**: mayoría de los operadores aritméticos (`+`, `-`, `*`, `/`).
- **Asociatividad derecha**: exponenciación, asignación en C/Java, operador condicional ternario.
- La asociatividad izquierda es la esperada intuitivamente para operaciones aritméticas.
- Caso crítico: `a = b = c = 5` en C evalúa de derecha a izquierda.

## Ejemplo

```ts
const r = 10 - 3 - 2   // (10 - 3) - 2 = 5
```

```scheme
(- (- 10 3) 2)
```

En Scheme no se depende de asociatividad infija.

---

### [F-10] Paréntesis como decisión semántica

@tipo: codigo
@layout: codigo
@imagen: none

# Parentizar no es redundante si mejora la lectura

## Cuándo usar paréntesis

- Si una expresión exige recordar demasiadas reglas, se usan paréntesis.

```ts
const habilitado =
    (usuario.activo && usuario.emailVerificado) || usuario.esAdmin
```

---

### [F-11] Orden de evaluación de operandos

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Parseo ≠ orden de evaluación temporal de los operandos

## Semántica operacional

- El AST indica estructura.
- El lenguaje define, o deja sin definir, el orden temporal.
- Con funciones puras, puede no importar.
- Con efectos colaterales, importa mucho.

---

### [F-12] Efectos colaterales en expresiones

@tipo: codigo
@layout: codigo
@imagen: none

# TypeScript define más orden que C, pero no elimina el problema

## Ejemplo TypeScript

```ts
let i = 1
const r = i++ + ++i
```

## Contraste histórico

```c
// C/C++: algunos casos son indefinidos o no especificados
i = i++ + ++i;
```

```rust
// Rust: no existe i++
i += 1;
```

## Regla de diseño

- En TypeScript, puede estar definido pero seguir siendo ilegible.
- Evitar expresiones que mezclen cálculo y mutación en la misma sentencia.

---

### [F-13] Asignación como expresión

@tipo: codigo
@layout: codigo
@imagen: none

# Asignación: sentencia y expresión a la vez

## Decisiones de lenguaje

```c
// C: idiomático — getchar() asigna y su valor se compara con EOF
while ((c = getchar()) != EOF) {
    procesar(c);
}
```

```ts
// TypeScript
let x = 0
let y = (x = 5) + 3
```

```kotlin
// Kotlin: no se usa asignación como expresión de valor
x = 5
```

## Riesgo

- Lenguajes que admiten *assignment expressions* en condiciones habilitan el bug clásico `if (x = 0)`.
- C lo permite; compiladores modernos emiten warning con `-Wall`.
- Rust, Swift, Kotlin restringen el patrón en condiciones por diseño.

---

### [F-14] Prevención de bugs de asignación

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# `if (x = 0)`: el bug clásico de asignación en condición

## Estrategias de prevención

- **Yoda conditions**: `if (0 == x)` → una asignación accidental falla al compilar.
- Activar warnings del compilador (`-Wparentheses`, `-Wall` en GCC/Clang).
- Lenguajes modernos (Rust, Swift, Kotlin) eliminan el problema por diseño del lenguaje.
- Linters como ESLint/TSLint detectan automáticamente este patrón.

---

### [F-15] Conversión y coerción

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# Conversión explícita vs. coerción implícita

## Taxonomía

| Mecanismo | Control | Riesgo | Ejemplo |
|-----------|---------|--------|---------|
| Conversión explícita (cast) | Programador | Bajo | `int(3.7)` → 3 |
| Coerción implícita widening | Lenguaje | Medio | `int` → `float` automático |
| Coerción implícita narrowing | Lenguaje | Alto | `float` → `int` (pérdida de datos) |
| Sobrecarga de operadores | Lenguaje/Prog. | Variable | `+` en strings y enteros |

## Principio

- La coerción implícita puede enmascarar errores de tipo que el sistema de tipos debería detectar.
- Lenguajes con tipado estático fuerte (Haskell, Rust) minimizan las coerciones implícitas.

---

### [F-16] Control conceptual — Bloque A

@tipo: socratica
@layout: socratica
@imagen: none

# Consolidando fundamentos de expresiones

## Preguntas

- ¿Cuál es la diferencia entre precedencia de operadores y orden de evaluación de operandos?
- ¿Cuándo una *assignment expression* en un `if` se convierte en bug?
- Dar un ejemplo donde la coerción implícita produce un resultado diferente al esperado.

---

## BLOQUE B — Booleanos, short-circuit y seguridad semántica

---

### [F-17] Álgebra booleana aplicada

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Operadores lógicos como control del flujo de evaluación

## Más que tablas de verdad

- En código real, `&&` y `||` controlan qué sub-expresiones se evalúan.
- La conjunción y disyunción permiten codificar precondiciones de forma declarativa.
- Operadores lógicos con y sin short-circuit tienen semánticas distintas.
- El short-circuit es semántica perezosa de operadores lógicos.

---

### [F-18] Truthiness entre lenguajes

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# Verdad no booleana: qué cuenta como `true` según el lenguaje

## Variación semántica

| Lenguaje | `0` es falsy | `""` es false | `null`/`None` false | Bool estricto |
|----------|------------|-------------|--------------------|--------------------|
| C | Sí | N/A | — | No (usa `int`) |
| Python | Sí | Sí | Sí | Sí, flexible |
| TypeScript | Sí | Sí | Sí | Sí, flexible |
| Java | No | No | Sí | Sí, estricto |
| Kotlin | No | No | Error de compilación | Sí, estricto |

## Regla de diseño

- No migrar intuiciones de valores de verdad de un lenguaje a otro sin validar la semántica local.

```ts
if ("") { ... }   // TypeScript: válido, falsy
```

```kotlin
if ("") { ... }   // Kotlin: error
```

---

### [F-19] Evaluación estricta

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Evaluación estricta: todos los operandos se evalúan siempre

## Semántica estricta

- Evalúa todos los operandos antes de aplicar el operador lógico.
- Predecible y conveniente para análisis formal y optimizaciones del compilador.
- Puede ejecutar sub-expresiones inválidas innecesariamente (división por cero, acceso null).
- Pascal original usaba `and`/`or` sin garantía de short-circuit.
- La evaluación estricta favorece la verificabilidad; el short-circuit favorece la corrección operativa.

---

### [F-20] Short-circuit

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Short-circuit: evaluación que se detiene cuando el resultado ya es conocido

## Semántica de corto circuito

- `p && q`: si `p` es **false**, `q` no se evalúa — el resultado ya es false.
- `p || q`: si `p` es **true**, `q` no se evalúa — el resultado ya es true.
- Es una herramienta de **corrección semántica**, no solo de rendimiento.
- Permite usar la primera condición como **guarda** de seguridad de la segunda.
- El short-circuit es semántica perezosa de operadores lógicos.

---

### [F-21] Patrón defensivo con short-circuit

@tipo: codigo
@layout: codigo
@imagen: none

# Short-circuit como guarda de corrección

## Evitar división por cero y acceso null

```ts
// Guarda contra división por cero
if (x !== 0 && y / x > 2) {
    aprobar()
}

// Guarda contra acceso null
if (user !== null && user.isActive()) {
    procesar(user)
}
```

```c
// C
if (p != NULL && p->value > 0) { ... }
```

## Por qué funciona

- Si la primera condición falla, la segunda nunca se evalúa.
- Es una forma práctica de guarda operacional.
- Invertir el orden destruye la guarda y puede causar runtime error.

---

### [F-22] Side effects en booleanos: anti-patrón

@tipo: codigo
@layout: codigo
@imagen: none

# Mezclar predicados con efectos en operadores lógicos

## Anti-patrón

```ts
// ANTI-PATRÓN: logAndMutate() puede no ejecutarse si isReady() es true
if (isReady() || logAndMutate()) {
    ejecutar()
}

// CORRECTO: el efecto ocurre siempre, independiente del predicado
const logged = logAndMutate()
if (isReady() || logged) {
    ejecutar()
}
```

## Principio

- Separar predicados (sin efectos) de funciones con efectos colaterales.
- Short-circuit convierte un efecto secundario en un efecto condicional → comportamiento inesperado.

---

### [F-23] Operadores lógicos: comparativa por lenguaje

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# Operadores lógicos y bit a bit por lenguaje

## Comparativa

| Lenguaje | AND lógico | OR lógico | AND bit | OR bit | NOT lógico |
|----------|-----------|-----------|---------|--------|------------|
| C/C++ | `&&` | `\|\|` | `&` | `\|` | `!` |
| Java | `&&` | `\|\|` | `&` | `\|` | `!` |
| TypeScript | `&&` | `\|\|` | `&` | `\|` | `!` |
| Python | `and` | `or` | `&` | `\|` | `not` |
| Kotlin | `&&` | `\|\|` | `and` | `or` | `!` |

---

### [F-24] Null safety con operadores lógicos

@tipo: codigo
@layout: codigo
@imagen: none

# `?.` y `??`: short-circuit especializado para null

## TypeScript

```ts
// Optional chaining: corta en null/undefined
const ciudad = usuario?.direccion?.ciudad

// Nullish coalescing: default solo para null/undefined (no para 0 ni "")
const nombre = entrada ?? "sin nombre"

// Combinados: guarda completa de acceso y fallback
const zip = usuario?.direccion?.codigoPostal ?? "0000"
```

## Kotlin

```kotlin
val ciudad = usuario?.direccion?.ciudad
val nombre = entrada ?: "sin nombre"
```

## Rust

```rust
let ciudad = usuario
    .and_then(|u| u.direccion)
    .map(|d| d.ciudad);
```

## Semántica

- `?.` implementa short-circuit ante null o undefined.
- `??` es más estricto que `||`: no cortocircuita ante `0` o `""`.

---

### [F-25] Guard clauses

@tipo: codigo
@layout: codigo
@imagen: none

# Reducir anidamiento con cláusulas de guarda

## Early return

```ts
// SIN guard clauses: anidamiento profundo
function procesar(x?: number) {
    if (x != null) {
        if (x >= 0) { return `ok:${x}` }
    }
    return "inválido"
}

// CON guard clauses: flujo plano y legible
function procesar(x?: number) {
    if (x == null) return "faltante"
    if (x < 0)    return "inválido"
    return `ok:${x}`
}
```

---

## BLOQUE C — Selección estructurada y decisiones de diseño

---

### [F-26] Programación estructurada y el debate sobre goto

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: content
@prompt-imagen: ilustración conceptual dividida en dos mitades: izquierda muestra una maraña caótica de flechas entrecruzadas representando goto indiscriminado; derecha muestra bloques ordenados conectados secuencialmente representando programación estructurada; paleta rojo caótico vs azul ordenado, estilo minimalista técnico

# Goto y la emergencia de las estructuras de control

## Contexto histórico

- `goto` permite saltos arbitrarios a cualquier punto del programa.
- Aumenta el poder de expresión local; reduce la trazabilidad y verificabilidad global.
- Dijkstra (1968): "Go To Statement Considered Harmful" — fundamento del movimiento estructurado.
- Las estructuras de control buscan control explícito: entrada única, salida única, verificable.
- El `goto` moderno restringido (C, C++) sobrevive para manejo de errores y salida de bucles anidados — uso justificado y acotado.

## Go: goto restringido

```go
package main

import "fmt"

func main() {
    i := 0
inicio:
    fmt.Println(i)
    i++
    if i < 3 {
        goto inicio
    }
}
```

`goto` está permitido en Go, pero restringido: permite saltar a una etiqueta dentro de la misma función, sin entrar ilegalmente en un bloque ni saltarse inicializaciones de variables.

---

### [F-27] If y else if: árbol de decisiones

@tipo: codigo
@layout: codigo
@imagen: none

# Selección simple y encadenada

## Semántica del if-else

- Ramas mutuamente excluyentes.
- Evaluación en orden.
- `else` como caso no capturado.
- Orden de condiciones importa.

## TypeScript

```ts
if (score >= 9)      grado = "A"
else if (score >= 7) grado = "B"
else if (score >= 4) grado = "C"
else                 grado = "D"
```

## Kotlin

```kotlin
val grado =
    if (score >= 9) "A"
    else if (score >= 7) "B"
    else if (score >= 4) "C"
    else "D"
```

---

### [F-28] Switch: selección múltiple

@tipo: codigo
@layout: codigo
@imagen: none

# Switch como alternativa estructurada a cadenas de if-else

## Semántica del switch

- `switch` clásico discrimina por valor.
- C/JavaScript/TypeScript heredan la necesidad de `break`.
- Kotlin reemplaza `switch` por `when`.
- Rust usa `match` exhaustivo.
- La decisión de diseño afecta confiabilidad.
- El problema de confiabilidad aparece cuando hay continuación implícita de una rama a otra.

## TypeScript

```ts
switch (token) {
    case "INT": parseIntToken();    break
    case "ID":  parseIdToken();     break
    case "STR": parseStringToken(); break
    default:    reportError()
}
```

## Kotlin

```kotlin
when (token) {
    "INT" -> parseIntToken()
    "ID"  -> parseIdToken()
    "STR" -> parseStringToken()
    else  -> reportError()
}
```

---

### [F-29] Pattern matching: evolución del control múltiple

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Pattern matching como selección estructural sobre datos

## Evolución del switch

- `switch` clásico: discrimina por valor (escalar, enum).
- **Pattern matching**: discrimina por estructura del dato — forma, tipo y desestructuración.
- Disponible en Haskell, Scala, Rust, Python 3.10+, Java 21+.
- Tabla de despacho: extensibilidad en dominios abiertos (polimorfismo por datos).
- En lenguajes con tipos algebraicos, pattern matching reemplaza la selección como estructura primaria.

---

### [F-30] Complejidad cognitiva del anidamiento

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Cada nivel de anidamiento incrementa la carga cognitiva

## Impacto en mantenibilidad

- Cada nivel de anidamiento extra multiplica los paths de ejecución posibles.
- Las ramas profundas elevan el riesgo de paths no testeados en revisión manual.
- La complejidad ciclomática mide el número de paths linealmente independientes.
- Guard clauses y early return reducen complejidad accidental sin cambiar la semántica.

## Regla práctica

- Máximo 3 niveles de anidamiento antes de extraer una función o reestructurar el flujo.

---

### [F-31] Criterios para elegir estructura de selección

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# Elegir entre if-else, switch y tabla de despacho

## Matriz de decisión

| Criterio | if-else | switch | Tabla de despacho |
|----------|---------|--------|-------------------|
| Pocas ramas (2–3) | óptimo | Posible | Sobreingeniería |
| Muchas ramas (>5) | Verboso | legible | extensible |
| Condiciones complejas | natural | Limitado | — |
| Cambio frecuente de casos | Costoso | Costoso | Open/Closed |
| Exhaustividad verificable | Manual | Sí (con default) | Manual |

---

### [F-32] Despacho por tabla

@tipo: codigo
@layout: codigo
@imagen: none

# Tabla de despacho: separar lógica de control de los datos

## Patrón (extensión OOP)

```ts
const handlers: Record<string, () => void> = {
    INT: parseIntToken,
    ID:  parseIdToken,
    STR: parseStringToken,
};

(handlers[token] ?? reportError)();
```

> Buscar en la tabla `handlers` la función asociada al valor de `token`; si no existe, usar `reportError`; luego ejecutar la función elegida.

## Ventajas

- Agregar un caso = agregar una entrada. No se modifica lógica de control.
- Principio Open/Closed aplicado a estructuras de selección.
- Cada rama es testeable independientemente sin afectar al bloque completo.

---

### [F-33] Code smells de selección

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Señales de fragilidad en estructuras de selección

## Detectar y refactorizar

- **Condiciones duplicadas** en múltiples ramas → violan DRY y ocultan semántica.
- **Default que esconde errores** → enmascarar casos no manejados reduce trazabilidad.
- **Predicados opacos con side effects** → mezclan responsabilidades de evaluación y acción.
- **Cascadas largas sin dominio explícito** → señal de que falta una abstracción de datos.

---

## BLOQUE D — Iteración, iteradores y generadores

---

### [F-34] Estructuras iterativas clásicas

@tipo: codigo
@layout: codigo
@imagen: none

# While, do-while y for: tres formas de iteración

## Semántica de bucles

- **`while`**: evalúa condición al inicio → puede no ejecutarse si la condición es falsa de entrada.
- **`do-while`**: evalúa condición al final → garantiza al menos una ejecución.
- **`for`**: contador, condición y actualización en una línea → para iteración acotada.
- En la mayoría de lenguajes modernos, `for` es azúcar sintáctico sobre `while`.

## TypeScript

```ts
while (hayDatos())           leer()
do { leer() } while (hayDatos())
for (let i = 0; i < n; i++) procesar(i)
```

## Kotlin

```kotlin
while (hayDatos())           leer()
for (i in 0 until n)        procesar(i)
```

---

### [F-35] Invariantes de bucle

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de tres estados temporales de un bucle: "antes" (caja vacía con check verde), "durante" (caja con flecha circular representando preservación del invariante), "después" (caja con check verde y resultado); estilo diagrama técnico, paleta azul/verde, sin texto legible

# El invariante garantiza la corrección del bucle

## Razonamiento formal sobre iteración

- **Qué se mantiene verdadero**: la propiedad que define el invariante.
- **Cómo se establece**: el invariante debe ser verdadero antes de entrar al bucle.
- **Cómo se preserva**: el cuerpo del bucle debe mantener el invariante en cada iteración.
- **Qué permite concluir al terminar**: invariante + negación de la condición → resultado correcto.

---

### [F-36] Terminación del bucle

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# El bucle termina si hay progreso medible hacia la condición de parada

## Condición de terminación

- Definir una **función de ranking** (*loop variant*): entero acotado inferiormente que decrece en cada iteración.
- El bucle termina si el variant es estrictamente decreciente y acotado.
- Verificar **casos borde**: `n = 0`, colecciones vacías, centinela inalcanzable.
- Bucles con centinela: la terminación depende de que el centinela sea alcanzable en la entrada.

---

### [F-37] Break y continue

@tipo: codigo
@layout: codigo
@imagen: none

# Escapar del flujo normal de iteración

## Semántica del escape estructurado

- `break` y `continue` son transferencias estructuradas: afectan solo el bucle más cercano.
- Java permite `break label` para salir de bucles anidados — transferencia estructurada restringida, similar al `goto` limitado.

```ts
for (const x of xs) {
    if (!esValido(x)) continue       // salta al próximo elemento
    if (x === objetivo) {
        encontrado = true
        break                         // sale del bucle
    }
    procesar(x)
}
```

---

### [F-38] Contador y centinela

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Dos patrones clásicos de control de iteración

## Contador vs. centinela

- **Contador**: control por límites explícitos; adecuado cuando la cota es conocida de antemano.
- **Centinela** (`while`): control por valor especial en el stream; evita evaluar longitud en cada iteración.
- El centinela es útil en lectura incremental de streams o archivos: `while ((c = getchar()) != EOF)` en C.
- Riesgo: si el valor centinela nunca aparece en la entrada, el bucle no termina.

---

### [F-39] Iteradores: separar estructura de recorrido

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# El iterador desacopla la colección del recorrido

## Patrón iterador

- La **colección** almacena los datos.
- El **iterador** encapsula el estado de recorrido y define el *traversal*.
- Habilita recorridos alternativos sobre la misma estructura sin duplicar su estado interno.
- El protocolo `Iterable/Iterator` (TypeScript, Java, Python) estandariza el contrato.
- Los iteradores son la forma moderna de iterar sobre estructuras sin exponer su representación interna.

---

### [F-40] Generadores: secuencias perezosas

@tipo: codigo
@layout: codigo
@imagen: none

# Generadores: producir valores bajo demanda con `yield`

## Semántica de yield

- El generador suspende la ejecución en cada `yield` y la reanuda al siguiente `next()`.
- Permite trabajar con secuencias infinitas sin consumir memoria proporcional al tamaño.
- Cada `next()` reanuda la función exactamente donde se suspendió.

## TypeScript

```ts
function* rango(inicio: number, fin: number) {
    for (let i = inicio; i < fin; i++) yield i
}
```

## Python

```python
def rango(inicio, fin):
    for i in range(inicio, fin):
        yield i
```

---

### [F-41] for...of vs for...in

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# Diferencia crítica en iteración sobre colecciones

## TypeScript

| Forma | Itera sobre | Resultado |
|-------|-------------|-----------|
| `for...of` | Valores del iterable | `10, 20, 30` |
| `for...in` | Claves del objeto (strings) | `"0", "1", "2"` |

```ts
const arr = [10, 20, 30]
for (const k in arr)  console.log(k)   // "0", "1", "2"  → claves
for (const v of arr)  console.log(v)   // 10, 20, 30     → valores correctos
```

---

### [F-42] Recursión e iteración: misma potencia, costos distintos

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: none

# Recursión vs. iteración: equivalencia expresiva, costos operacionales distintos

## Análisis comparativo

- **Recursión**: estilo declarativo; el estado está implícito en la pila de llamadas.
- **Iteración**: control operativo explícito; el estado está en variables locales.
- Toda recursión primitiva puede transformarse en iteración con una pila explícita.
- Equivalencia expresiva con costos operacionales distintos (stack vs. heap).
- **Tail call optimization (TCO)**: Haskell, Scheme, Scala optimizan recursión en cola como iteración — elimina costo de stack.

---

## BLOQUE E — Integración y cierre

---

### [F-43] Control asíncrono con async/await

@tipo: codigo
@layout: codigo
@imagen: none

# async/await: secuencialidad aparente sobre operaciones asíncronas

## Flujo asíncrono como control

- `await` suspende la función actual sin bloquear el hilo de ejecución.
- Permite escribir flujo de control lineal sobre operaciones inherentemente concurrentes.
- El runtime convierte el código en una máquina de estados implícita.

```ts
async function obtenerDatos(): Promise<string[]> {
    return ["A", "B", "C"];
}

async function pipeline() {
    const datos     = await obtenerDatos()       // se suspende hasta resolución
    const validado  = await validar(datos)
    const resultado = await transformar(validado)
    return resultado
}
```

---

### [F-44] Cierre: criterios de diseño semántico

@tipo: cierre
@layout: cierre
@imagen: background
@prompt-imagen: composición minimalista de cierre: cinco pilares de luz alineados sobre un horizonte, cada uno representando una idea fuerza del tema; paleta azul nocturno con acentos dorados; sin texto, estilo conceptual limpio

# Expresiones y estructuras de control: criterios para diseñar bien

## Ideas fuerza del tema

- **Parseo ≠ evaluación**: la precedencia fija la forma; el orden de evaluación lo fija el lenguaje.
- **Short-circuit por corrección**: la semántica de corto circuito evita estados inválidos, no solo optimiza.
- **Estructuras por mantenibilidad**: if-else, switch o dispatch según el dominio y el cambio esperado.
- **Iteración correcta**: un bucle sin invariante y sin función de ranking no es correcto por accidente.
- **Legibilidad semántica**: nombrar bien predicados y estructurar el flujo previene defectos futuros.

## Referencias

- **Sebesta** (fuente principal): caps. 7 y 8 — expresiones, evaluación, asignación y estructuras de control.
- **Gabbrielli-Martini** (auxiliar): semántica operacional, coerciones, invariantes de bucle y recursión.
- **Louden** (auxiliar): implementación del control de flujo, legibilidad y decisiones de diseño de lenguajes.