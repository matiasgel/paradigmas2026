# Diseño — Tema 09.2: Aliases, Closures, GC y Tipos

> **Agente:** Lic. Marcos 🗂️ — Topic Designer  
> **Fecha:** 2026-05-14  
> **Origen:** Extraído de `09-variables-binding/diseno.md` — Clase 2 de 2  
> **Estado:** 🟡 EN PRODUCCION — filminas.md y minuta.md corregidos contra `clase_dada.txt` + ChromaDB el 2026-06-28  
> **Duración:** **120 min (1 clase)**  
> **Lenguaje principal:** TypeScript  
> **Lenguajes de contraste:** Python (closures, reference counting), Kotlin (lambdas, val/var), Go (closures, escape analysis), Rust (ownership, drop), Haskell (bindings inmutables, sin mutabilidad), Scala (var vs. val), C (solo referencia histórica)  
> **Fuente primaria:** Sebesta — *Concepts of Programming Languages* (Pearson 2019), Cap. 5, 6, 10  
> **Fuentes secundarias:** Gabbrielli & Martini — *Programming Languages: Principles and Paradigms* (Springer 2023), Cap. 7, 11, 16.9; Louden & Lambert — *Programming Languages: Principles and Practices* (2012), Cap. 10  
> **Bloque IA:** Aliases de objeto sin advertencia. Closures con `var` (bug clásico). Type narrowing como guardrail.  
> **Prerequisito:** → Tema 09.1: Variables, Binding y Ámbito (5-tupla, categorías de variables, ámbito estático)

---

## 1. Contexto en el Plan

**Posición:** Tema 09.2 de 15 — segunda clase del bloque Variables/Binding  
**Duración:** 1 clase × 120 min  
**Tópico del plan mínimo:** Entidades y ligaduras (VI.9) — segunda parte  
**Prerequisito directo:** Tema 09.1 — se asume conocimiento de la 5-tupla, 4 categorías y ámbito estático  
**Conexiones:**  
- ← Tema 09.1: aliases son posibles porque L-value ≠ R-value; closures extienden el tiempo de vida de variables stack-dynamic al heap  
- → Tema 10 (Tipos de Datos): union types y discriminated unions; type narrowing como herramienta de los tipos  
- → Tema 11 (FP): inmutabilidad como principio central del paradigma funcional  
- → Tema 14 (Sistemas de Tipos): TypeScript como gradual typing, inferencia, strict mode  

---

## 2. Objetivos de Aprendizaje

Al finalizar la clase el alumno debe poder:

| # | Objetivo | Nivel Bloom |
|---|----------|-------------|
| OA1 | Analizar aliases: identificar sus fuentes (referencias de objeto, parámetros ref, uniones), razonar sobre sus implicancias en verificación formal y análisis estático | Analizar |
| OA2 | Analizar closures: comparar binding profundo vs. superficial, evaluar consecuencias en el ciclo de vida de variables y semántica de programas funcionales | Analizar |
| OA3 | Comparar garbage collection (reference counting vs. mark-sweep) con gestión manual y por ownership | Analizar |
| OA4 | Explicar gradual typing y el rol de TypeScript como lenguaje gradualmente tipado | Comprender |
| OA5 | Contrastar variables mutables (imperativo) con bindings inmutables (funcional) usando Haskell y TypeScript funcional | Analizar |
| OA6 | Aplicar type narrowing en TypeScript para manejar union types de forma segura | Aplicar |
| OA7 | Detectar errores de aliases y mutabilidad en código generado por IA; proponer correcciones | Evaluar |

---

## 3. Tópicos y Distribución de Tiempo

| # | Tópico | Tiempo | Fuente |
|---|--------|--------|--------|
| 3.1 | Aliases: definición, fuentes (referencias obj., parámetros ref, union types), consecuencias | 15 min | Sebesta §5.3.3, Louden §7.7 |
| 3.2 | Closures: entorno léxico capturado, ciclo de vida extendido, deep vs. shallow binding | 18 min | Sebesta §10, Gabbrielli §7.4, Louden §10.3 |
| 3.3 | Garbage Collection: reference counting vs. mark-sweep | 18 min | Sebesta §6.11, Louden §10.5 |
| 3.4 | Gradual typing: TypeScript como caso paradigmático + type narrowing | 15 min | Gabbrielli §16.9 |
| 3.5 | Variables en programación funcional: sin mutabilidad. val vs. var | 12 min | Sebesta §5.8 (FP), Gabbrielli §11 |
| 3.6 | Contraste multilenguaje: Python, Kotlin, Go, Rust — gestión de memoria moderna | 10 min | Sebesta §5.4.3, Gabbrielli §16 |
| — | **Bloque IA:** aliases y mutabilidad, closures con var, type narrowing como guardrail | 12 min | — |
| — | Buffer / preguntas | 10 min | — |
| **Total** | | **110 min + 10 buffer** | |

---

## 4. Desarrollo de Contenidos

### 4.1 Aliases

**Definición (Sebesta §5.3.3, Louden §7.7):** Un alias ocurre cuando dos nombres distintos están vinculados al mismo objeto (misma celda de memoria) en el mismo momento.

**Fuentes de aliases:**

**1. Referencias de objeto en TypeScript** (fuente más común hoy):

```typescript
const obj1 = { valor: 42 };
const obj2 = obj1;     // obj1 y obj2 son aliases del mismo objeto en heap
obj2.valor = 99;
console.log(obj1.valor);  // 99 — modificado a través del alias
```

**2. Parámetros por referencia** (Kotlin, Go):

```kotlin
// Kotlin — los objetos se pasan por referencia (alias implícito)
data class Punto(var x: Int, var y: Int)
fun desplazar(p: Punto, dx: Int) { p.x += dx }  // alias: p apunta al mismo objeto
val origen = Punto(0, 0)
desplazar(origen, 5)
println(origen.x)  // 5 — objeto modificado a través del alias
```

```go
// Go — punteros explícitos (seguros: sin aritmética de punteros)
func duplicar(p *int) { *p *= 2 }  // alias: p y la variable original comparten celda
x := 10
duplicar(&x)
fmt.Println(x)  // 20
```

**3. Union types en TypeScript** (alias de tipo, no de objeto — como contrapunto):

```typescript
// Union types no crean aliases, pero sí múltiples "nombres" para el mismo valor
type ID = string | number;
const userId: ID = "abc123";  // no alias — un solo binding
```

**Consecuencias:**
- Hace difícil razonar sobre el programa (cambiar un nombre afecta otros)
- Dificulta la **verificación formal** y el análisis estático
- El compilador no puede optimizar bien código con aliases potenciales
- Fuente de bugs sutiles en programas concurrentes (race conditions)

**TypeScript — detección con `readonly`:**

```typescript
function procesarPuro(data: readonly number[]): number[] {
    // data no puede ser modificado — sin aliases peligrosos
    return data.map(x => x * 2);
}
```

**Shallow copy vs. deep copy — evitar aliases accidentales:**

```typescript
const original = { nombre: "Ana", config: { debug: true } };

// Shallow copy (alias del objeto anidado):
const copia1 = { ...original };
copia1.config.debug = false;   // ← modifica original.config también!

// Deep copy (sin aliases):
const copia2 = structuredClone(original);  // ES2022
copia2.config.debug = false;   // original intacto ✅
```

---

### 4.2 Closures: Entorno Léxico Capturado

**Definición (Sebesta §10, Gabbrielli §7.4):** Una closure es la combinación de una función y el entorno léxico en el que fue definida. Captura variables del ámbito externo aunque ese ámbito haya terminado de ejecutar.

**Por qué existen:** cuando una función accede a variables de un ámbito anidado pero no global, esas variables no pueden vivir solo en el activation record (se destruye al retornar). Se almacenan en el **heap con duración extendida** (Sebesta §10).

```typescript
function crearContador(inicio: number) {
    let cuenta = inicio;  // ← capturada por closure

    return {
        incrementar: () => ++cuenta,  // closure sobre cuenta
        valor: () => cuenta           // closure sobre cuenta
    };
}

const c = crearContador(10);
console.log(c.incrementar());  // 11
console.log(c.incrementar());  // 12
// crearContador() ya retornó, pero cuenta sigue viva en heap
```

```python
# Python — closures con nonlocal
def crear_contador(inicio: int):
    cuenta = inicio
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return incrementar

contar = crear_contador(10)
print(contar())  # 11
print(contar())  # 12
```

```go
// Go — closures de primera clase
func crearContador(inicio int) func() int {
    cuenta := inicio
    return func() int {
        cuenta++
        return cuenta
    }
}
```

```kotlin
// Kotlin — lambdas con captura de entorno léxico
fun crearContador(inicio: Int): () -> Int {
    var cuenta = inicio
    return { ++cuenta }
}
```

> **C no tiene closures verdaderas** (Gabbrielli §7.4). Las funciones de callback (`void (*f)(int)`) no pueden capturar entorno — toda variable no-local debe ser global. Esto ilustra por contraste qué hace especial al closure.

**Relación con el ciclo de vida:** las variables capturadas por una closure tienen tiempo de vida extendido — viven en el heap hasta que el closure es garbage-collected. Esto extiende el ciclo de vida más allá del frame de pila original.

#### Deep Binding vs. Shallow Binding (Gabbrielli §7.4)

- **Deep binding (Vinculación profunda):** la closure captura el entorno en el momento de su **creación** → TypeScript/JavaScript, Python, Haskell
- **Shallow binding (Vinculación superficial):** la función usa el entorno en el momento de la **llamada** → algunos lenguajes con ámbito dinámico

```typescript
// Deep binding — bug clásico de var en loops:
const funcs: (() => number)[] = [];
for (var i = 0; i < 3; i++) {
    funcs.push(() => i);  // var: captura REFERENCIA a i, no valor
}
console.log(funcs[0]());  // 3, no 0 — i ya llegó a 3

// Corrección con let (deep binding por bloque):
const funcs2: (() => number)[] = [];
for (let j = 0; j < 3; j++) {
    funcs2.push(() => j);  // let: nueva j por iteración
}
console.log(funcs2[0]());  // 0 — correcto
```

---

### 4.3 Garbage Collection

**Contexto (Sebesta §6.11, Louden §10.5):** Las variables de heap (Categorías 3 y 4) son liberadas automáticamente. El GC determina cuándo una celda es "inaccesible" y la devuelve al pool.

#### Reference Counting (Conteo de Referencias) — Enfoque *eager*

Cada celda mantiene un contador de referencias activas hacia ella. Cuando el contador llega a 0, la celda se libera inmediatamente.

```
[Objeto A] → ref_count: 2
     ↑           ↑
 [x]         [y]      // x e y apuntan a A → ref_count = 2

del x  →  ref_count = 1
del y  →  ref_count = 0 → LIBERAR inmediatamente
```

**Problema crítico: referencias circulares** (Louden §10.5):

```typescript
class Nodo {
    siguiente: Nodo | null = null;
}
const a = new Nodo();
const b = new Nodo();
a.siguiente = b;
b.siguiente = a;  // ciclo: a → b → a
// Si se eliminan a y b del scope externo:
// ref_count(a) = 1 (b lo apunta), ref_count(b) = 1 (a lo apunta)
// Ninguno llega a 0 → memory leak con reference counting puro
```

Python usa reference counting + **cycle detector** para resolver esto.

#### Mark-and-Sweep — Enfoque *lazy*

Opera en dos fases cuando el allocator se queda sin espacio:

1. **Mark (Marcar):** a partir de todas las raíces (stack, variables globales), trazar transitivamente todos los objetos alcanzables → marcarlos  
2. **Sweep (Barrer):** recorrer todo el heap; las celdas **no marcadas** son inaccesibles → liberar

```
Roots: [x → Obj1, y → Obj3]

Heap antes de sweep:
  Obj1 ✓ (alcanzable desde x)
  Obj2   (no alcanzable → LIBERAR)
  Obj3 ✓ (alcanzable desde y)
  Obj4   (no alcanzable → LIBERAR)
```

**Ventaja:** Resuelve referencias circulares correctamente  
**Desventajas:** Pausas del programa durante GC (stop-the-world), fragmentación del heap

**V8 (motor de TypeScript/JavaScript):** GC generacional que combina ambas técnicas. Divide el heap en generación joven (minor GC frecuente, cheap) y generación vieja (major GC infrecuente, costoso). Se suma **compactación** para eliminar fragmentación.

---

### 4.4 Gradual Typing: TypeScript como Caso Paradigmático

**(Gabbrielli §16.9 — sección sobre TypeScript)**

**Motivación:** La dicotomía typing estático/dinámico es absoluta en muchos lenguajes. El **gradual typing** permite elegir cuándo y dónde se quiere verificación estática.

**TypeScript — el ejemplo canónico:**

```typescript
// Zona sin tipos (dinámico puro) — compatible con JavaScript
function sumar(a: any, b: any): any {
    return a + b;
}

// Zona con tipos (estático puro)
function sumarSeguro(a: number, b: number): number {
    return a + b;
}

// Zona intermedia — partial typing
function procesarElemento(elemento: unknown): string {
    if (typeof elemento === "string") {   // type narrowing
        return elemento.toUpperCase();    // aquí el tipo es string
    }
    return String(elemento);
}
```

**Gradual typing en la práctica:**

```typescript
// JavaScript existente → TypeScript gradual
// Paso 1: archivo .js renombrado a .ts — compila con any implícito
// Paso 2: agregar tipos donde sea más crítico
// Paso 3: habilitar strict: true para máxima cobertura

// tsconfig.json:
// { "strict": true }  ← cambia de gradual a completamente estático
```

**Gabbrielli §16.9:** TypeScript permite tomar una codebase JavaScript existente, agregarle anotaciones de tipo gradualmente, y compilar de vuelta a JavaScript (con optimizaciones y checks adicionales).

#### Type Narrowing — binding de tipo en runtime dentro de tipos estáticos

```typescript
type Resultado = string | number | null;

function formatear(r: Resultado): string {
    if (r === null) return "—";                           // narrowing: r: null
    if (typeof r === "number") return r.toFixed(2);      // r: number
    return r.toUpperCase();                               // r: string (único restante)
}
// TypeScript verifica estáticamente que todos los casos están cubiertos
```

---

### 4.5 Variables en Programación Funcional

**(Sebesta §5.8, Gabbrielli §11)**

**Contraste fundamental:** En los LP imperativos, las variables son celdas de memoria mutables. En los LP funcionales puros, **no existen variables mutables** — solo bindings inmutables.

```haskell
-- Haskell: NO hay variables. Solo bindings.
let x = 5      -- x se vincula a 5 PARA SIEMPRE en este scope
-- x = 6       -- ← ILEGAL: el binding no puede cambiar
```

**Implicación semántica (Gabbrielli §11):**
- En FP puro: la computación es **reescritura de expresiones** (no modificación de estado)
- No hay valor-i (L-value) porque no hay concepto de dirección modificable
- El binding es definitivo: más cercano a las constantes de LP imperativos que a sus variables

**Scala — `var` vs. `val`** (Gabbrielli §11):

```scala
var x = 5    // var: nombre que puede ser reasignado (variable imperativa)
val y = 5    // val: binding inmutable (como const en TypeScript)
```

**TypeScript funcional — inmutabilidad como práctica:**

```typescript
// Imperativo: muta estado
let suma = 0;
for (const x of [1, 2, 3]) suma += x;

// Funcional: sin mutación, solo bindings nuevos
const suma = [1, 2, 3].reduce((acc, x) => acc + x, 0);

// Objetos inmutables con readonly
type Config = Readonly<{
    host: string;
    port: number;
}>;
const cfg: Config = { host: "localhost", port: 8080 };
// cfg.host = "otro";  // ❌ Error: Cannot assign to 'host' because it is read-only
```

> **¿Por qué importa para IA?** Los LLMs tienden a generar código imperativo con mutación porque predomina en el corpus. El FP reduce bugs de aliasing y estado compartido.

---

### 4.6 Gestión de Memoria — Perspectiva Comparativa

**¿Cómo los lenguajes modernos resuelven los problemas que C dejó expuestos?**

```typescript
// TypeScript/JavaScript — GC automático (V8 generacional)
let sesion = { id: 1, datos: ["a", "b"] };
sesion = null;  // referencia anterior sin refs → GC la libera
// Imposible crear dangling pointer: el GC garantiza que un objeto vivo es accesible
```

```python
# Python — GC con reference counting + cycle detector
sesion = {"id": 1, "datos": ["a", "b"]}
sesion = None   # ref_count → 0 → liberado inmediatamente (si no hay ciclos)
# sys.getrefcount() permite inspeccionar el conteo de referencias
```

```go
// Go — GC con escape analysis
type Sesion struct { ID int; Datos []string }
func nuevaSesion(id int) *Sesion {
    s := Sesion{ID: id}   // compilador "escapa" s al heap porque retorna puntero
    return &s             // seguro: Go garantiza que s vive en heap
}
```

```rust
// Rust — ownership: garantía en tiempo de compilación, sin GC
struct Sesion { id: u32, datos: Vec<String> }
// Al salir del scope: destructor automático (Drop trait), sin GC, sin leak posible
// El borrow checker previene dangling pointers en compilación:
// let ref1 = &s; drop(s); println!("{}", ref1.id);  // Error: compile-time
```

| Aspecto | TypeScript | Python | Go | Rust |
|---------|------------|--------|-----|------|
| Gestión de memoria | GC (V8 generacional) | RC + cycle GC | GC (escape analysis) | Ownership + Drop |
| Variables estáticas | Module-level `let`/`const` | Module-level | Package-level `var` | `static` con lifetime `'static` |
| Acceso al valor-i | No directo (GC opaco) | `id()` expone dirección | `&x` (puntero seguro) | `&x` (borrow) / `*mut x` (raw unsafe) |
| Variables sin inicializar | Error de compilación (strict) | NameError en runtime | Zero values (0, nil, "") | Error de compilación |
| Dangling pointer | Imposible (GC) | Imposible (GC) | Imposible (GC) | Imposible (borrow checker) |
| Aliases explícitos | Referencias de objeto | Referencias de objeto | Punteros + interfaces | Borrows (inmutables o un mutable) |

---

### 4.7 Bloque IA — Aliases, Mutabilidad y Type Narrowing (12 min)

#### Patrón 1: IA genera alias de objeto sin advertencia

```typescript
// Prompt: "Duplica el objeto de configuración para modificarlo"
// IA genera (INCORRECTO — alias):
const configBackup = config;   // no es copia, es alias
configBackup.debug = true;     // modifica config también!

// Correcto — shallow copy:
const configBackup = { ...config };

// Correcto — deep copy (objetos anidados):
const configBackup = structuredClone(config);  // ES2022
```

#### Patrón 2: IA genera closures con `var` (bug clásico de binding)

```typescript
// Prompt: "Genera un array de funciones que retornen su índice"
// IA con var (INCORRECTO):
const funcs = [];
for (var i = 0; i < 5; i++) {
    funcs.push(() => i);      // todas capturan la MISMA i
}
// funcs[0]() === 5, funcs[1]() === 5, etc.

// Correcto con let:
const funcs2: (() => number)[] = [];
for (let i = 0; i < 5; i++) {
    funcs2.push(() => i);     // cada iteración tiene su propia i
}
```

#### Patrón 3: Type narrowing como guardrail del código generado

```typescript
// IA genera (sin narrowing — puede crashear):
function procesar(valor: string | number) {
    return valor.toUpperCase();  // ❌ Error si valor es number
}

// Con narrowing — TypeScript obliga a manejar todos los casos:
function procesarSeguro(valor: string | number): string {
    if (typeof valor === "string") return valor.toUpperCase();
    return valor.toString();
}
// TypeScript verifica estáticamente exhaustividad de los casos
```

---

## 5. Ejemplos Integradores

### Ejemplo 1: Closure con ciclo de vida extendido

```typescript
function crearAcumulador(inicial: number) {
    let total = inicial;  // capturada — vivirá en heap mientras exista la closure

    return {
        agregar: (n: number) => { total += n; },
        leer: () => total
    };
}

const acc = crearAcumulador(0);
acc.agregar(5);
acc.agregar(3);
console.log(acc.leer());  // 8
// total vive en heap aunque crearAcumulador() ya retornó
```

### Ejemplo 2: Gradual typing progresivo

```typescript
// Fase 1: JavaScript puro (sin tipos)
function calcular(a, b) { return a + b; }  // any implícito

// Fase 2: Tipos parciales
function calcular(a: number, b): number { return a + b; }

// Fase 3: Tipos completos + strict
function calcular(a: number, b: number): number { return a + b; }
// 'calcular("hola", 3)' → Error en compilación
```

### Ejemplo 3: Immutabilidad en FP vs. imperativo

```typescript
// Imperativo — muta estado acumulado
function sumaImperativa(nums: number[]): number {
    let acc = 0;
    for (const n of nums) acc += n;
    return acc;
}

// Funcional — sin mutación
const sumaFuncional = (nums: number[]) =>
    nums.reduce((acc, n) => acc + n, 0);

// Estructuras inmutables encadenadas
const resultado = [1, 2, 3, 4, 5]
    .filter(n => n % 2 === 0)
    .map(n => n * n)
    .reduce((acc, n) => acc + n, 0);  // 4 + 16 = 20
```

---

## 6. Conexiones al Plan Mínimo

| Tópico plan mínimo | Cobertura |
|-------------------|-----------|
| Aliases | ✅ Fuentes, consecuencias, detección con readonly |
| Closures y entorno léxico | ✅ Deep binding, ciclo de vida extendido |
| GC (gestión automática) | ✅ Reference counting + mark-sweep + comparativa |
| Gradual typing / TypeScript | ✅ Gabbrielli §16.9 — caso canónico, type narrowing |
| Variables en FP vs. imperativo | ✅ Inmutabilidad, val vs. var, Haskell/Scala/TypeScript |

---

## 7. Stack de Lenguajes

| Rol | Lenguaje | Propósito |
|-----|----------|-----------|
| **Principal** | TypeScript | Aliases (readonly, structuredClone), closures (var vs. let), gradual typing, type narrowing |
| **Contraste OO-JVM** | Kotlin | Lambdas con captura de entorno, val/var |
| **Contraste sistemas** | Rust | Ownership, borrow checker, Drop, sin GC |
| **Contraste concurrente** | Go | Escape analysis, closures, punteros seguros |
| **Contraste dinámico** | Python | Reference counting, cycle detector, nonlocal |
| **Contraste funcional** | Haskell | Bindings inmutables, sin mutabilidad, FP puro |
| **Gradual** | Scala | `var` vs. `val` — paradigma mixto |
| **Referencia histórica** | C | Solo para contexto GC manual / dangling pointers (nunca primario) |

---

## 8. Materiales Requeridos

- [ ] Slides Clase 9.2: aliases, diagrama de closures, GC reference counting vs. mark-sweep, gradual typing, FP immutability (a generar por Roberto)
- [ ] Diagrama: referencias circulares y memory leak en reference counting
- [ ] Diagrama: mark-sweep — raíces → alcanzable vs. inaccesible
- [ ] `variables.pdf` UNTDF 2024 (ya en ChromaDB)

---

## 9. FAQ Anticipado

**P: ¿Una closure "previene" el GC de liberar las variables capturadas?**  
R: Exactamente. Mientras la closure exista y sea accesible, las variables que captura tienen referencias activas. El GC no las libera. Es la fuente clásica de memory leaks accidentales en JavaScript largo-running.

**P: ¿El `const` evita aliases?**  
R: No. `const obj1 = {}; const obj2 = obj1;` — ambas constantes referencian el mismo objeto. `const` hace inmutable la referencia (no la puede reasignar), pero el objeto sigue siendo mutable y aliaseable.

**P: ¿V8 (Node/browsers) usa GC generacional?**  
R: Sí. Divide el heap en "generación joven" (minor GC frecuente, cheap) y "generación vieja" (major GC infrecuente, costoso). La mayoría de los objetos muere joven (generational hypothesis).

**P: ¿El `val` de Haskell es como el `const` de TypeScript?**  
R: No exactamente. `const` hace inmutable la **referencia**, no el objeto. `val` de Haskell hace el binding completamente inmutable — no hay concepto de objeto mutable separado. `Object.freeze()` + `Readonly<T>` en TypeScript se acerca más.

**P: ¿TypeScript puede tener deep binding y shallow binding en el mismo programa?**  
R: Sí. Las arrow functions (`=>`) usan deep binding para `this` (léxico). Los métodos con `function` keyword usan `this` dinámico (shallow, determinado en llamada). Por eso TypeScript recomienda `=>` en callbacks de clase.

---

## 10. Fuentes

1. **Sebesta, R. W.** (2019). *Concepts of Programming Languages* (12th ed.). Pearson. Cap. 5 (§5.3.3 aliases, §5.8 FP), Cap. 6 (§6.11 GC), Cap. 10 (closures en implementación de subprogramas).
2. **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms* (2nd ed.). Springer. Cap. 7 (§7.4 closures, binding policy), Cap. 11 (FP paradigm), Cap. 16 (§16.9 TypeScript gradual typing).
3. **Louden, K. C. & Lambert, K. A.** (2012). *Programming Languages: Principles and Practices* (3rd ed.). Course Technology. Cap. 7 (§7.7 aliases), Cap. 10 (§10.3 closures, §10.5 GC: reference counting + mark-sweep).
4. **Filminas UNTDF 2024.** *Cuestiones semánticas vinculadas a Variables.* (ingesta/variables.pdf)
5. **TypeScript Handbook.** Narrowing, Template Literal Types. https://www.typescriptlang.org/docs/

---

*Generado por Lic. Marcos 🗂️ — Topic Designer (EDU)*  
*1 clase × 120 min | Extraído de: 09-variables-binding/diseno.md (Clase 2 de 2)*  
*Fuentes: Sebesta Cap.5/6/10 + Gabbrielli Cap.7/11/16 + Louden Cap.7/10 + Filminas UNTDF 2024*  
*Estado: Borrador — requiere aprobación del docente*
