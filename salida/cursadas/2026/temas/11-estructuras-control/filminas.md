# Filminas - Tema 11: Expresiones y Estructuras de Control

> Curso: Paradigmas y Lenguajes de Programación · UNTDF IDEI 2026
> Cobertura: F-00 a F-44
> Referencia principal: Sebesta, *Concepts of Programming Languages*, caps. 7–8
> Referencias auxiliares: Gabbrielli-Martini caps. 4–5, Louden cap. 8

---

## PORTADA

### [F-00] Portada

@tipo: concepto-mixto
@imagen: none

# Expresiones y Estructuras de Control

Paradigmas y Lenguajes de Programación · Tema 11 · Módulo VIII
UNTDF IDEI 2026

---

### [F-01] Pregunta de apertura

@tipo: concepto-mixto
@imagen: none

# ¿Dos expresiones equivalentes siempre se comportan igual?

- ¿Dónde puede cambiar el resultado: en el parseo, la evaluación, o los side effects?
- ¿Puede una expresión producir resultados distintos según el lenguaje que la ejecute?
- ¿Qué garantiza realmente una tabla de precedencia de operadores?

---

## BLOQUE A — Fundamentos de expresiones y semántica

### [F-02] Objetivos

@tipo: concepto-mixto

# Objetivos de la secuencia

## Al finalizar este tema el estudiante podrá

- Definir formalmente expresión, sentencia y contexto de evaluación (Sebesta §7.1).
- Aplicar precedencia, asociatividad y orden de evaluación con y sin side effects.
- Distinguir short-circuit de evaluación estricta y justificar su uso por corrección semántica.
- Elegir estructuras de control por criterio semántico y de mantenibilidad.
- Modelar iteración con invariantes y condición de terminación verificable.

---

### [F-03] Mapa conceptual del tema

@tipo: concepto-mixto
@imagen: none

# Expresiones → Evaluación → Control

## Ejes del tema

- **Expresiones**: forma sintáctica que produce un valor o efecto colateral.
- **Evaluación**: orden, precedencia y semántica operacional.
- **Selección**: decisión estructurada y criterios de mantenibilidad.
- **Iteración**: invariante, terminación y costo cognitivo.
- **Abstracciones de flujo**: iteradores, generadores y asincronía.

---

### [F-04] Expresión y sentencia

@tipo: concepto-mixto
@imagen: none

# Expresión produce valor · Sentencia causa efecto

## Distinción fundamental (Sebesta §7.1)

- **Expresión**: construcción sintáctica que se evalúa y retorna un valor.
- **Sentencia**: unidad de ejecución que controla el flujo o provoca efectos colaterales.
- Un lenguaje que permite *assignment expressions* mezcla ambos roles: mayor poder, mayor riesgo.
- Sebesta: en C, `x = 5` es simultáneamente expresión (valor: 5) y sentencia (efecto: asignación).
- La distinción impacta el diseño: Haskell elimina sentencias; C las maximiza.

---

### [F-05] AST y parseo

@tipo: concepto-mixto
@imagen: none

# El árbol sintáctico abstracto fija la forma de la expresión

## Cómo el AST determina semántica (Sebesta §7.2)

- La **precedencia** de operadores determina la estructura del árbol de parseo.
- La **asociatividad** resuelve empates entre operadores de igual precedencia.
- El AST captura estructura, no evaluación: es una representación intermedia.
- Parseo y evaluación son **fases distintas**: el árbol no garantiza orden de evaluación temporal.
- Sebesta: el operador con mayor precedencia queda más profundo en el árbol → se evalúa primero.

---

### [F-06] Precedencia

@tipo: concepto-mixto

# La precedencia determina la agrupación sintáctica

## Reglas de prioridad (Sebesta §7.2)

- Multiplicación y división se agrupan antes que suma y resta (convención matemática).
- **Lenguajes difieren** en precedencia de operadores relacionales, lógicos y de bits.
- Parentizar explícitamente mejora legibilidad y elimina dependencia de reglas implícitas.
- Sebesta: la tabla de precedencias es una decisión de diseño del lenguaje, no un estándar universal.

## Ejemplo

```
a + b * c     →   a + (b * c)      # precedencia mayor de *
(a + b) * c   →   suma antes        # paréntesis explicitan intención
a ** b ** c   →   a ** (b ** c)    # asociatividad derecha en Python
```

---

### [F-07] Asociatividad

@tipo: concepto-mixto

# Mismo nivel de precedencia: ¿izquierda o derecha?

## Resolución de empates (Sebesta §7.2)

- **Asociatividad izquierda**: mayoría de los operadores aritméticos (`+`, `-`, `*`, `/`).
- **Asociatividad derecha**: exponenciación, asignación en C/Java, operador condicional ternario.
- La asociatividad izquierda es la esperada intuitivamente para operaciones aritméticas.
- Caso crítico: `a = b = c = 5` en C evalúa de derecha a izquierda.

## Ejemplo

```
a - b - c   →   (a - b) - c    # asociatividad izquierda
a = b = c   →   a = (b = c)    # asociatividad derecha (C, Java)
2 ** 3 ** 2 →   2 ** (3 ** 2)  # derecha → 512, no 64 (Python)
```

---

### [F-08] Orden de evaluación de operandos

@tipo: concepto-mixto
@imagen: none

# Parseo ≠ orden de evaluación temporal de los operandos

## Semántica operacional (Sebesta §7.3)

- El AST fija la **forma** de la expresión (qué se calcula).
- El **orden en que se evalúan los operandos** lo define —o no define— el lenguaje.
- Java garantiza evaluación de izquierda a derecha en todos los contextos.
- C/C++ deja el orden **sin especificar**: cada compilador puede optimizarlo libremente.
- Con **side effects**, el orden de evaluación altera el resultado observable del programa.
- Sebesta: esta ambigüedad en C fue fuente histórica de bugs de portabilidad entre compiladores.

---

### [F-09] Efectos colaterales

@tipo: codigo

# Side effects ocultos en expresiones

## Ejemplo con post-incremento (Sebesta §7.3)

```ts
let i = 1
const a = [10, 20, 30]
const x = a[i] + i++
// ¿x = a[1] + 1 = 21?  → si i se lee antes de incrementar
// ¿x = a[2] + 1 = 31?  → si a[i] se evalúa después del incremento
// El resultado depende del orden garantizado por el lenguaje
```

## Regla de diseño (Sebesta §7.3)

- Evitar expresiones que **mezclen cálculo y mutación** en la misma sentencia.
- Preferir separación explícita: primero mutar, luego calcular.
- C deja este comportamiento **undefined** → el compilador puede producir cualquier resultado.

---

### [F-10] Asignación como expresión

@tipo: codigo

# Asignación: sentencia y expresión a la vez

## Decisiones de lenguaje (Sebesta §7.7)

```c
while ((c = getchar()) != EOF) {
    procesar(c);
    // Idiomático en C: getchar() asigna y su valor se compara con EOF
}
```

```ts
let y = (x = 5) + 3   // x queda 5, y queda 8
```

## Riesgo

- Lenguajes que admiten *assignment expressions* en condiciones habilitan el bug clásico `if (x = 0)`.
- C lo permite; compiladores modernos emiten warning con `-Wall`.
- Rust, Swift, Kotlin **prohíben** assignment expressions en condiciones por diseño.

---

### [F-11] Prevención de bugs de asignación

@tipo: concepto-mixto

# `if (x = 0)`: el bug clásico de asignación en condición

## Estrategias de prevención (Sebesta §7.7, Louden §8)

- **Yoda conditions**: `if (0 == x)` → una asignación accidental falla al compilar.
- Activar warnings del compilador (`-Wparentheses`, `-Wall` en GCC/Clang).
- Lenguajes modernos (Rust, Swift, Kotlin) eliminan el problema por diseño del lenguaje.
- Linters como ESLint/TSLint detectan automáticamente este patrón.
- Sebesta: uno de los ejemplos canónicos de cómo decisiones de diseño impactan en confiabilidad del código.

---

### [F-12] Conversión y coerción

@tipo: tabla-comparativa

# Conversión explícita vs. coerción implícita

## Taxonomía (Sebesta §7.4, Gabbrielli-Martini §4.3)

| Mecanismo | Control | Riesgo | Ejemplo |
|-----------|---------|--------|---------|
| Conversión explícita (cast) | Programador | Bajo | `int(3.7)` → 3 |
| Coerción implícita widening | Lenguaje | Medio | `int` → `float` automático |
| Coerción implícita narrowing | Lenguaje | Alto | `float` → `int` (pérdida de datos) |
| Sobrecarga de operadores | Lenguaje/Prog. | Variable | `+` en strings y enteros |

## Principio de Sebesta

- La coerción implícita puede **enmascarar errores de tipo** que el sistema de tipos debería detectar.
- Lenguajes con tipado estático fuerte (Haskell, Rust) minimizan las coerciones implícitas.

---

### [F-13] Control conceptual — Bloque A

@tipo: concepto-mixto
@imagen: none

# Consolidando fundamentos de expresiones

- ¿Cuál es la diferencia entre precedencia de operadores y orden de evaluación de operandos?
- ¿Cuándo una *assignment expression* en un `if` se convierte en bug?
- Dar un ejemplo donde la coerción implícita produce un resultado diferente al esperado.

---

## BLOQUE B — Booleanos, short-circuit y seguridad semántica

### [F-14] Álgebra booleana aplicada

@tipo: concepto-mixto
@imagen: none

# Operadores lógicos como control del flujo de evaluación

## Más que tablas de verdad (Sebesta §7.6)

- En código real, `&&` y `||` **controlan qué sub-expresiones se evalúan**.
- La conjunción y disyunción permiten codificar precondiciones de forma declarativa.
- Sebesta distingue: operadores lógicos con y sin short-circuit tienen **semánticas distintas**.
- La forma normal DNF/CNF permite simplificar condiciones complejas antes de codificarlas.
- Gabbrielli-Martini: formalizan el short-circuit como semántica perezosa de operadores lógicos.

---

### [F-15] Truthiness entre lenguajes

@tipo: tabla-comparativa

# Verdad no booleana: qué cuenta como `true` según el lenguaje

## Variación semántica (Sebesta §7.6, Louden §8)

| Lenguaje | `0` es falsy | `""` es falsy | `null`/`None` falsy | Bool estricto |
|----------|------------|-------------|--------------------|--------------------|
| C | Sí | N/A | — | No (usa `int`) |
| Python | Sí | Sí | Sí | Sí, flexible |
| TypeScript | Sí | Sí | Sí | Sí, flexible |
| Java | No | No | Sí | Sí, estricto |
| Kotlin | No | No | Error de compilación | Sí, estricto |

## Regla de diseño

- No migrar intuiciones de truthiness de un lenguaje a otro sin validar la semántica local.

---

### [F-16] Evaluación estricta

@tipo: concepto-mixto
@imagen: none

# Evaluación estricta: todos los operandos se evalúan siempre

## Semántica estricta (Sebesta §7.6)

- Evalúa **todos** los operandos antes de aplicar el operador lógico.
- Predecible y conveniente para análisis formal y optimizaciones del compilador.
- Puede ejecutar **sub-expresiones inválidas** innecesariamente (división por cero, acceso null).
- Pascal original usaba `and`/`or` sin garantía de short-circuit.
- Sebesta: la evaluación estricta favorece la verificabilidad; el short-circuit favorece la corrección operativa.

---

### [F-17] Short-circuit

@tipo: concepto-mixto
@imagen: none

# Short-circuit: evaluación que se detiene cuando el resultado ya es conocido

## Semántica de corto circuito (Sebesta §7.6)

- `p && q`: si `p` es **false**, `q` **no se evalúa** — el resultado ya es `false`.
- `p || q`: si `p` es **true**, `q` **no se evalúa** — el resultado ya es `true`.
- Es una herramienta de **corrección semántica**, no solo de rendimiento.
- Permite usar la primera condición como **guarda** de seguridad de la segunda.
- Gabbrielli-Martini: el short-circuit es semántica perezosa de operadores lógicos.

---

### [F-18] Patrón defensivo con short-circuit

@tipo: codigo

# Short-circuit como guarda de corrección

## Evitar división por cero y acceso null (Sebesta §7.6)

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

## Por qué funciona

- Si la primera condición **falla**, la segunda nunca se evalúa.
- Sebesta: este patrón es la base del *guarded command* en programación defensiva.
- Invertir el orden destruye la guarda y puede causar runtime error.

---

### [F-19] Side effects en booleanos: anti-patrón

@tipo: codigo

# Mezclar predicados con efectos en operadores lógicos

## Anti-patrón con side effects (Sebesta §7.3 + §7.6)

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

- Separar **predicados** (sin efectos) de **funciones con efectos colaterales**.
- Short-circuit convierte un efecto secundario en un efecto condicional → comportamiento inesperado.

---

### [F-20] Operadores lógicos: comparativa por lenguaje

@tipo: tabla-comparativa

# Operadores lógicos y bit a bit por lenguaje

## Comparativa (Sebesta §7.6, Louden §8)

| Lenguaje | AND lógico | OR lógico | Short-circuit | AND bit | OR bit |
|----------|-----------|-----------|---------------|---------|--------|
| C/C++ | `&&` | `\|\|` | Sí | `&` | `\|` |
| Java | `&&` | `\|\|` | Sí | `&` | `\|` |
| TypeScript | `&&` | `\|\|` | Sí | `&` | `\|` |
| Python | `and` | `or` | Sí | `&` | `\|` |
| Kotlin | `&&` | `\|\|` | Sí | `and` | `or` |

---

### [F-21] Null safety con operadores lógicos

@tipo: codigo

# `?.` y `??`: short-circuit especializado para null

## TypeScript (Sebesta §7, extensión moderna)

```ts
// Optional chaining: corta en null/undefined
const ciudad = usuario?.direccion?.ciudad

// Nullish coalescing: default solo para null/undefined (no para 0 ni "")
const nombre = entrada ?? "sin nombre"

// Combinados: guarda completa de acceso y fallback
const zip = usuario?.direccion?.codigoPostal ?? "0000"
```

## Semántica

- `?.` implementa short-circuit ante `null` o `undefined`.
- `??` es más estricto que `||`: no cortocircuita ante `0` o `""`.

---

### [F-22] Guard clauses

@tipo: codigo

# Reducir anidamiento con cláusulas de guarda

## Patrón de *early return* (Sebesta §8, Louden §8)

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

### [F-23] Control conceptual — Bloque B

@tipo: concepto-mixto
@imagen: none

# Consolidando booleanos y short-circuit

- Reescribir una condición compleja a forma legible sin cambiar la semántica de short-circuit.
- ¿Por qué `if (ptr != null && ptr->value > 0)` es correcto pero invertido puede producir segfault?
- Nombrar dos lenguajes donde el tipo booleano es estricto y no acepta truthiness implícita.

---

## BLOQUE C — Selección estructurada y decisiones de diseño

### [F-24] Programación estructurada y el debate sobre goto

@tipo: concepto-mixto
@imagen: none

# Goto y la emergencia de las estructuras de control

## Contexto histórico (Sebesta §8.2, Louden §8)

- `goto` permite saltos **arbitrarios** a cualquier punto del programa.
- Aumenta el poder de expresión local; reduce la trazabilidad y verificabilidad global.
- Dijkstra (1968): "Go To Statement Considered Harmful" — fundamento del movimiento estructurado.
- Las estructuras de control buscan **control explícito**: entrada única, salida única, verificable.
- Sebesta: el `goto` moderno restringido (C, C++) sobrevive para manejo de errores y salida de bucles anidados — uso justificado y acotado.

---

### [F-25] If y else if: árbol de decisiones

@tipo: codigo

# Selección simple y encadenada

## Semántica del if-else (Sebesta §8.3)

```ts
if (score >= 9)      grado = "A"
else if (score >= 7) grado = "B"
else if (score >= 4) grado = "C"
else                 grado = "D"
```

## Propiedades

- Las ramas son **mutuamente excluyentes** y evaluadas en orden.
- El `else` final cubre todos los casos no capturados: actúa como caso base implícito.
- Sebesta: la ausencia de `else` puede dejar variables sin inicializar → bug silencioso.
- El orden de las condiciones importa: una condición más general antes de una específica puede oscurecer ramas.

---

### [F-26] Switch: selección múltiple

@tipo: codigo

# Switch como alternativa estructurada a cadenas de if-else

## Semántica del switch (Sebesta §8.4)

```ts
switch (token) {
    case "INT": parseIntToken();    break
    case "ID":  parseIdToken();     break
    case "STR": parseStringToken(); break
    default:    reportError()
}
```

## Decisiones de diseño por lenguaje (Sebesta §8.4)

- **C**: fallthrough implícito → `break` es necesario; fuente de bugs históricos.
- **Java**: igual que C para primitivos; switch expressions (Java 14+) son exhaustivas.
- **TypeScript/Kotlin**: `when` con exhaustividad verificable en tiempo de compilación.
- Sebesta: el fallthrough es una decisión controvertida con implicancias directas de mantenibilidad.

---

### [F-27] Pattern matching: evolución del control múltiple

@tipo: concepto-mixto
@imagen: none

# Pattern matching como selección estructural sobre datos

## Evolución del switch (Sebesta §8.4, Gabbrielli-Martini §5.1)

- `switch` clásico: discrimina por **valor** (escalar, enum).
- **Pattern matching**: discrimina por **estructura** del dato — forma, tipo y desestructuración.
- Disponible en Haskell, Scala, Rust, Python 3.10+, Java 21+.
- Tabla de despacho: extensibilidad en dominios abiertos (polimorfismo por datos).
- Sebesta: en lenguajes con tipos algebraicos, pattern matching reemplaza la selección como estructura primaria.

---

### [F-28] Complejidad cognitiva del anidamiento

@tipo: concepto-mixto

# Cada nivel de anidamiento incrementa la carga cognitiva

## Impacto en mantenibilidad (Sebesta §8, Louden §8)

- Cada nivel de anidamiento extra **multiplica** los paths de ejecución posibles.
- Las ramas profundas elevan el riesgo de paths **no testeados** en revisión manual.
- La **complejidad ciclomática** (McCabe) mide el número de paths linealmente independientes.
- Guard clauses y early return reducen complejidad accidental sin cambiar la semántica.

## Regla práctica

- Máximo 3 niveles de anidamiento antes de extraer una función o reestructurar el flujo.

---

### [F-29] Criterios para elegir estructura de selección

@tipo: tabla-comparativa

# Elegir entre if-else, switch y tabla de despacho

## Matriz de decisión (Sebesta §8.3–8.4, Louden §8)

| Criterio | if-else | switch | Tabla de despacho |
|----------|---------|--------|-------------------|
| Pocas ramas (2–3) | óptimo | Posible | Sobreingeniería |
| Muchas ramas (>5) | Verboso | legible | extensible |
| Condiciones complejas | natural | Limitado | — |
| Cambio frecuente de casos | Costoso | Costoso | Open/Closed |
| Exhaustividad verificable | Manual | Sí (con default) | Manual |

---

### [F-30] Despacho por tabla

@tipo: codigo

# Tabla de despacho: separar lógica de control de los datos

## Patrón (Sebesta §8, extensión OOP)

```ts
const handlers: Record<string, () => void> = {
    INT: parseIntToken,
    ID:  parseIdToken,
    STR: parseStringToken,
}

;(handlers[token] ?? reportError)()
```

## Ventajas

- Agregar un caso = agregar una entrada. **No se modifica lógica de control**.
- Principio Open/Closed aplicado a estructuras de selección.
- Cada rama es testeable independientemente sin afectar al bloque completo.

---

### [F-31] Code smells de selección

@tipo: concepto-mixto

# Señales de fragilidad en estructuras de selección

## Detectar y refactorizar (Sebesta §8, Louden §8)

- **Condiciones duplicadas** en múltiples ramas → violan DRY y ocultan semántica.
- **Default que esconde errores** → enmascarar casos no manejados reduce trazabilidad.
- **Predicados opacos con side effects** → mezclan responsabilidades de evaluación y acción.
- **Cascadas largas sin dominio explícito** → señal de que falta una abstracción de datos.

---

### [F-32] Taller: refactorizar selección anidada

@tipo: concepto-mixto
@imagen: none

# Actividad de refactorización guiada

1. Identificar redundancias y paths no cubiertos en ramas anidadas.
2. Reestructurar con guard clauses o tabla de despacho.
3. Verificar equivalencia semántica con casos de prueba específicos.
4. ¿El cambio mejoró la complejidad ciclomática medida con McCabe?

---

## BLOQUE D — Iteración, iteradores y generadores

### [F-33] Estructuras iterativas clásicas

@tipo: concepto-mixto

# While, do-while y for: tres formas de iteración

## Semántica de bucles (Sebesta §8.5, Louden §8)

- **`while`**: evalúa condición al **inicio** → puede no ejecutarse si la condición es falsa de entrada.
- **`do-while`**: evalúa condición al **final** → garantiza al menos una ejecución.
- **`for`**: contador, condición y actualización en una línea → para iteración acotada.
- Sebesta: en la mayoría de lenguajes modernos, `for` es azúcar sintáctico sobre `while`.

## Ejemplo

```ts
while (hayDatos())           leer()
do { leer() } while (hayDatos())
for (let i = 0; i < n; i++) procesar(i)
```

---

### [F-34] Invariantes de bucle

@tipo: concepto-mixto
@imagen: none

# El invariante garantiza la corrección del bucle

## Razonamiento formal sobre iteración (Sebesta §8.5, Gabbrielli-Martini §5.2)

- **Invariante de bucle**: propiedad verdadera antes de cada iteración.
- Al inicio: el invariante debe ser **establecido** antes del bucle.
- En cada iteración: el cuerpo del bucle debe **preservar** el invariante.
- Al terminar: invariante + negación de la condición implica el resultado correcto.
- Gabbrielli-Martini: los invariantes son la base de la verificación formal (Hoare Logic).

---

### [F-35] Terminación del bucle

@tipo: concepto-mixto
@imagen: none

# El bucle termina si hay progreso medible hacia la condición de parada

## Condición de terminación (Sebesta §8.5, Gabbrielli-Martini §5.2)

- Definir una **función de ranking** (*loop variant*): entero acotado inferiormente que decrece en cada iteración.
- El bucle termina si el variant es estrictamente decreciente y acotado.
- Verificar **casos borde**: `n = 0`, colecciones vacías, centinela inalcanzable.
- Bucles con centinela: la terminación depende de que el centinela sea **alcanzable** en la entrada.

---

### [F-36] Break y continue

@tipo: codigo

# Escapar del flujo normal de iteración

## Semántica del escape estructurado (Sebesta §8.5, Louden §8)

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

## Diseño de lenguaje

- `break` y `continue` son transferencias **estructuradas**: afectan solo el bucle más cercano.
- Sebesta: Java permite `break label` para salir de bucles anidados — transferencia estructurada restringida, similar al goto limitado.

---

### [F-37] Contador y centinela

@tipo: concepto-mixto
@imagen: none

# Dos patrones clásicos de control de iteración

## Contador vs. centinela (Sebesta §8.5, Louden §8)

- **Contador**: control por límites explícitos; adecuado cuando la cota es conocida de antemano.
- **Centinela**: control por valor especial en el stream; evita evaluar longitud en cada iteración.
- El centinela es útil en lectura incremental de streams o archivos.
- Riesgo: si el valor centinela nunca aparece en la entrada, el bucle no termina.

---

### [F-38] Iteradores: separar estructura de recorrido

@tipo: concepto-mixto
@imagen: none

# El iterador desacopla la colección del recorrido

## Patrón iterador (Sebesta §8.5, Gabbrielli-Martini §5.3)

- La **colección** almacena los datos.
- El **iterador** encapsula el estado de recorrido y define el *traversal*.
- Habilita recorridos alternativos sobre la misma estructura sin duplicar su estado interno.
- El protocolo `Iterable/Iterator` (TypeScript, Java, Python) estandariza el contrato.
- Sebesta: los iteradores son la forma moderna de iterar sobre estructuras sin exponer su representación interna.

---

### [F-39] Generadores: secuencias perezosas

@tipo: codigo

# Generadores: producir valores bajo demanda con `yield`

## Semántica de yield (Sebesta §8, extensión moderna)

```ts
function* rango(inicio: number, fin: number) {
    for (let i = inicio; i < fin; i++) yield i
}

function* fibonacci() {
    let [a, b] = [0, 1]
    while (true) { yield a; [a, b] = [b, a + b] }
}
```

## Propiedades

- El generador **suspende** la ejecución en cada `yield` y la **reanuda** al siguiente `next()`.
- Permite trabajar con secuencias **infinitas** sin consumir memoria proporcional al tamaño.
- Cada `next()` reanuda la función exactamente donde se suspendió.

---

### [F-40] for...of vs for...in

@tipo: tabla-comparativa

# Diferencia crítica en iteración sobre colecciones

## TypeScript (Sebesta §8.5, extensión modern JS)

| Forma | Itera sobre | Garantías de orden | Uso correcto |
|-------|-------------|-------------------|--------------|
| `for...of` | Valores del iterable | Garantizado | Arrays, Sets, Maps, generadores |
| `for...in` | Claves del objeto (strings) | Sin garantía | Enumerar propiedades de objetos |

## Advertencia

```ts
const arr = [10, 20, 30]
for (const k in arr)  console.log(k)   // "0", "1", "2"  → claves
for (const v of arr)  console.log(v)   // 10, 20, 30     → valores correctos
```

---

### [F-41] Recursión e iteración: misma potencia, costos distintos

@tipo: concepto-mixto
@imagen: none

# Recursión vs. iteración: equivalencia expresiva, costos operacionales distintos

## Análisis comparativo (Sebesta §8.6, Gabbrielli-Martini §5.2)

- **Recursión**: estilo declarativo; el estado está implícito en la pila de llamadas.
- **Iteración**: control operativo explícito; el estado está en variables locales.
- Toda recursión primitiva puede transformarse en iteración con una pila explícita.
- Gabbrielli-Martini: equivalencia expresiva con costos operacionales distintos (stack vs. heap).
- **Tail call optimization (TCO)**: Haskell, Scheme, Scala optimizan recursión en cola como iteración — elimina costo de stack.

---

### [F-42] Control asíncrono con async/await

@tipo: codigo

# async/await: secuencialidad aparente sobre operaciones asíncronas

## Flujo asíncrono como control (Sebesta §8, extensión moderna)

```ts
async function pipeline() {
    const datos     = await obtenerDatos()       // se suspende hasta resolución
    const validado  = await validar(datos)
    const resultado = await transformar(validado)
    return resultado
}
```

## Modelo de control

- `await` **suspende** la función actual sin bloquear el hilo de ejecución.
- Permite escribir flujo de control **lineal** sobre operaciones inherentemente concurrentes.
- El runtime convierte el código en una máquina de estados implícita.

---

## BLOQUE E — Integración y cierre

### [F-43] Caso integrador: lectura crítica de código

@tipo: concepto-mixto
@imagen: none

# Checklist de lectura crítica de código

Al revisar código real, verificar:

1. ¿Hay expresiones con coerción peligrosa o precedencia ambigua que debería parentizar?
2. ¿Las ramas están bien estructuradas? ¿Existen redundancias o casos no cubiertos?
3. ¿Cada bucle tiene un invariante implícito y una condición de terminación verificable?
4. ¿Los predicados en condiciones tienen side effects ocultos?
5. ¿Se aprovecha el short-circuit donde corresponde — o se evita donde puede causar bugs?

---

### [F-44] Cierre: criterios de diseño semántico

@tipo: concepto-mixto
@imagen: none

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
