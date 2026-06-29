# Diseño — Tema 09.1: Variables, Binding y Ámbito

> **Agente:** Lic. Marcos 🗂️ — Topic Designer  
> **Fecha:** 2026-05-14  
> **Origen:** Extraído de `09-variables-binding/diseno.md` — Clase 1 de 2  
> **Estado:** 🟡 EN PRODUCCION — clase dada 2026-06-28; filminas/minuta corregidas contra `clase_dada.txt`  
> **Duración:** **120 min (1 clase)**  
> **Lenguaje principal:** TypeScript  
> **Lenguajes de contraste:** Python (binding dinámico, tipado duck), Kotlin (val/var, null safety), Go (zero values, punteros seguros), Rust (ownership como binding explícito), Haskell (bindings inmutables)  
> **Fuente primaria:** Sebesta — *Concepts of Programming Languages* (Pearson 2019), Cap. 5  
> **Fuentes secundarias:** Gabbrielli & Martini — *Programming Languages: Principles and Paradigms* (Springer 2023), Cap. 4, 8; Louden & Lambert — *Programming Languages: Principles and Practices* (2012), Cap. 7; Filminas UNTDF 2024  
> **Bloque IA:** Errores de ámbito en código generado. Variables globales silenciosas. Hoisting con `var`.  
> **Continuación:** → Tema 09.2: Aliases, Closures, GC y Tipos

---

## 1. Contexto en el Plan

**Posición:** Tema 09.1 de 15 — Bloque post-OO, pre-tipos  
**Duración:** 1 clase × 120 min  
**Tópico del plan mínimo:** Entidades y ligaduras (VI.9) — primera parte  
**Conexiones:**  
- ← Tema 08 (OO TypeScript): el `this`, los objetos son variables con atributos; paso de objetos por referencia  
- → Tema 09.2 (Aliases/Closures/GC): continuación directa con las mismas variables de ejemplo  
- → Tema 10 (Tipos de Datos): el tipo es uno de los atributos de la variable; union types, discriminated unions  
- → Tema 14 (Sistemas de Tipos): binding estático de tipos en TypeScript, inferencia, gradual typing  

---

## 2. Objetivos de Aprendizaje

Al finalizar la clase el alumno debe poder:

| # | Objetivo | Nivel Bloom |
|---|----------|-------------|
| OA1 | Describir la variable como 5-tupla `<nombre, dirección, tipo, valor-i, valor-d>` | Recordar |
| OA2 | Distinguir los 6 momentos de binding: diseño, implementación, compilación, linkeo, carga, ejecución | Comprender |
| OA3 | Clasificar variables según sus 4 categorías de tiempo de vida y zona de almacenamiento | Analizar |
| OA4 | Comparar ámbito estático vs. dinámico: reglas de resolución, ventajas y problemas | Analizar |
| OA5 | Diferenciar tipado fuerte vs. débil y binding estático vs. dinámico como dimensiones ortogonales | Analizar |
| OA6 | Aplicar el algoritmo de resolución de ámbito estático en código TypeScript | Aplicar |
| OA7 | Detectar errores de ámbito, hoisting y variables globales silenciosas en código generado por IA | Evaluar |

---

## 3. Tópicos y Distribución de Tiempo

| # | Tópico | Tiempo | Fuente |
|---|--------|--------|--------|
| 3.1 | Variable como abstracción. Von Neumann. La 5-tupla. L-value/R-value | 20 min | Sebesta §5.3–5.3.2, `clase_dada.txt` F-00–F-07 |
| 3.2 | Binding: definición y 6 tiempos de vinculación | 12 min | Sebesta §5.4, Louden §7.5, `clase_dada.txt` F-08–F-10 |
| 3.3 | Binding de tipos: estático vs. dinámico + inferencia + fuerte vs. débil + coerciones | 16 min | Sebesta §5.4.1–5.4.2, Gabbrielli §8.3/§8.8, `clase_dada.txt` F-11–F-17 |
| 3.4 | Binding de almacenamiento: 4 categorías de variables (estáticas, stack-dynamic, heap explícita/implícita) | 26 min | Sebesta §5.4.3, Gabbrielli §5/§14, `clase_dada.txt` F-18–F-27 |
| 3.5 | Ámbito estático vs. dinámico + scope holes + `this` en JavaScript | 18 min | Sebesta §5.5, Gabbrielli §4.3, `clase_dada.txt` F-28–F-33 |
| 3.6 | Entorno de referencia. Constantes. Inicialización comparativa | 10 min | Sebesta §5.6–5.8, `clase_dada.txt` F-34–F-38 |
| 3.7 | **Bloque IA:** globales silenciosas, `var` hoisting, shadowing inesperado | 12 min | `clase_dada.txt` F-39–F-44 |
| — | Actividad + prompt seguro + cierre | 6 min | `clase_dada.txt` F-45–F-47 |
| **Total** | | **120 min** | |

---

## 4. Desarrollo de Contenidos

### 4.1 Variable como Abstracción

**Contexto arquitectural:**  
La arquitectura Von Neumann tiene dos componentes clave: memoria (celdas con dirección) y procesador. Los lenguajes abstraen eso:

| Elemento concreto | Abstracción en LP |
|------------------|-------------------|
| Celda de memoria | **Variable** |
| Dirección de celda | **Nombre/identificador** |
| Modificación destructiva | **Sentencia de asignación** |

**Los 6 atributos de una variable** (Sebesta §5.3 — formalización central):

| Atributo | Notación | Descripción |
|----------|----------|-------------|
| **Nombre** | — | Identificador simbólico; puede no existir (variables anónimas) |
| **Dirección** | L-value | Celda(s) de memoria asociada(s); puede variar entre activaciones recursivas |
| **Tipo** | — | Conjunto de valores posibles + operaciones legales + representación interna |
| **Valor** | R-value | Contenido codificado almacenado según el tipo |
| **Tiempo de vida** | lifetime | Período durante el cual la variable está vinculada a una dirección |
| **Ámbito** | scope | Rango de instrucciones donde el nombre es visible |

> **Distinción L-value / R-value (Sebesta §5.3.2):** en `x = y`, `x` denota dirección (L-value) e `y` denota contenido (R-value). Un mismo nombre puede tener distintos L-values en distintas invocaciones (recursión) o en distintos módulos.

Algunos textos condensan estos atributos en una **5-tupla** (agrupando tiempo de vida con ámbito):

```
Variable = <nombre, dirección, tipo, l-valor, r-valor>   [+ ámbito como atributo de contexto]
```

```typescript
// TypeScript — la 5-tupla en acción
let contador: number = 42;
//   ↑nombre  ↑tipo    ↑valor-d
// valor-i = dirección de memoria asignada por el runtime (oculta)
// ámbito  = bloque donde está declarado

// TypeScript oculta el valor-i — no hay acceso directo a la dirección
// Rust lo hace explícito de forma segura:
// let x = 42i32;
// let addr = &x as *const i32;  // valor-i visible como puntero raw
```

```python
# Python — la 5-tupla con binding en runtime
contador = 42          # nombre: contador, tipo: int (inferido), valor-d: 42
id(contador)           # id() expone el valor-i (dirección del objeto)
type(contador)         # int — binding de tipo dinámico
```

```kotlin
// Kotlin — la 5-tupla con null safety integrada
var contador: Int = 42    // mutable — valor-d puede cambiar
val limite: Int = 100     // inmutable — binding de valor-d fijo desde creación
```

> 📌 **Sebesta §5.3.2:** Un mismo nombre puede tener distintas direcciones en distintos lugares del programa o en distintos momentos de ejecución. **L-value ≠ R-value** — fundamental para entender aliases y paso por referencia (tema 09.2).

---

### 4.2 Atributos de Variables

#### Nombre / Identificador

El nombre de una variable participa en tres mecanismos formales:

- **Resolución de nombres:** el proceso por el que el compilador/intérprete mapea un identificador a la entidad que denota. En ámbito estático → compilación; en dinámico → ejecución.
- **Espacios de nombres (namespaces):** partición del espacio de identificadores para evitar colisiones. TypeScript usa módulos ES; Rust usa `mod`; Go usa paquetes con visibilidad determinada por mayúscula/minúscula.
- **⚠️ Aliasing de nombres:** NO cubrir en esta clase — pertenece estrictamente a 09.2 (Aliases, Closures, GC). Solo mencionar el nombre si surge una pregunta; redirigir inmediatamente.

> **Variables sin nombre (anónimas):** literales como `new Nodo(42)` crean objetos en heap sin asignarles nombre — tienen dirección (L-value) y valor (R-value) pero no nombre. Solo son accesibles mientras exista al menos una referencia.

#### Tipo

Define: (a) rango de valores posibles, (b) operaciones legales, (c) representación interna.  
TypeScript extiende esto con **structural typing** — el tipo es compatible por estructura, no por nombre nominal.

#### Valor-d (R-value) y Valor-i (L-value)

El contenido codificado de la celda, interpretado según el tipo.  
En `x = y`: `x` denota dirección (valor-i), `y` denota contenido (valor-d).

---

### 4.3 Binding (Vinculación)

**Definición (Sebesta §5.4):** Binding es la asociación entre una entidad del programa y un atributo. Ocurre en distintos momentos:

| Momento | Descripción | Ejemplo |
|---------|-------------|---------|
| **Tiempo de diseño** | Significados posibles para símbolos | `*` = multiplicación |
| **Tiempo de implementación** | Rango de valores para tipos primitivos | `int` de 32 o 64 bits según arquitectura |
| **Tiempo de compilación** | Variable → tipo (C, Java, TypeScript) | `int count;` |
| **Tiempo de linkeo** | Llamada a librería → código del subprograma | `printf` en libc |
| **Tiempo de carga** | Variables globales → celdas de memoria | variables estáticas globales |
| **Tiempo de ejecución** | Variable → valor | `count = count + 5` |

**Ejemplo integrador en TypeScript** — los mismos 6 momentos:

```typescript
let count: number;
count = count + 5;
// Tipos posibles para una variable    → tiempo de diseño del lenguaje
// Tipo de count (number)              → tiempo de compilación (inferencia TS)
// Rango de valores de number          → tiempo de implementación (IEEE 754 float64)
// Valor de count                      → tiempo de ejecución
// Significado del operador +          → tiempo de compilación
// Representación interna del literal 5 → tiempo de diseño del compilador
```

**Comparativa de binding de tipos:**

| Lenguaje | Binding de tipo | Momento |
|----------|----------------|---------|
| TypeScript | Estático + inferencia | Compilación |
| Kotlin | Estático + inferencia | Compilación |
| Go | Estático + inferencia (`:=`) | Compilación |
| Rust | Estático + inferencia (Hindley-Milner) | Compilación |
| Python | Dinámico (+ type hints opcionales) | Ejecución |
| JavaScript | Dinámico | Ejecución |

---

### 4.4 Binding de Tipos

#### Binding Estático

```typescript
let i: number;          // TypeScript — explícito
let x = 5;              // TypeScript — inferencia: x: number
```

**Inferencia de tipos** (Gabbrielli §8): el compilador determina el tipo sin declaración explícita. TypeScript usa inferencia bidireccional:

```typescript
const items = [1, 2, 3];          // number[]
const first = items[0];            // number

items.forEach(x => {               // x: number (inferido del contexto)
    console.log(x.toFixed(2));
});
```

```haskell
-- Haskell: inferencia total (Hindley-Milner)
f x y
  | x == True = y * y
  | otherwise = y / 2
-- El compilador infiere: f :: Bool -> Double -> Double
```

#### Binding Dinámico de Tipos

```python
x = [2, 3, 4, 5]        # x: list
x = "uno, dos, tres"     # x: str — binding de tipo cambió en runtime
```

**Problema:** Errores de tipo no detectables en compilación; mayor overhead.

---

#### Tipado Fuerte vs. Débil — Dimensión Ortogonal (Sebesta §5.4.2, Gabbrielli §8.3)

**Esta dimensión es ortogonal a estático/dinámico.** Un lenguaje puede ser estático y débil (C), estático y fuerte (Haskell, Rust), dinámico y fuerte (Python), o gradual (TypeScript).

| | **Tipado fuerte** | **Tipado débil** |
|---|---|---|
| **Definición** | Cada operación verifica compatibilidad; no hay conversiones implícitas inseguras | Se permiten conversiones implícitas arbitrarias |
| **Error de tipo** | Error en compilación o excepción en runtime | Comportamiento silencioso (resultado incorrecto sin aviso) |
| **Ejemplos** | Haskell, Rust, Python, TypeScript (strict) | C, JavaScript, PHP |

```typescript
// JavaScript (débil) — coerciones implícitas silenciosas:
// "5" + 3   →  "53"   (number coercionado a string)
// "5" - 3   →  2      (string coercionada a number)

// TypeScript (strong) — error de compilación:
const a: string = "5";
const b: number = 3;
// a + b  →  Error TS2365: Operator '+' cannot be applied to types 'string' and 'number'
```

```python
# Python — fuerte y dinámico: rechaza coerciones implícitas inseguras
x = "5"
y = 3
# x + y  →  TypeError: can only concatenate str (not "int") to str
```

```c
// C — débil y estático: permite coerciones arbitrarias sin aviso
int i = 65;
char c = i;        // coercionado a char silenciosamente → 'A'
float *fp = &i;    // puntero interpretado como otro tipo: undefined behavior
```

> **Implicación de diseño (Gabbrielli §8.3):** El tipado fuerte es la tendencia dominante en lenguajes modernos porque los errores de tipo son detectables o generan excepciones explícitas. Rust lleva esto al extremo: **no hay coerciones implícitas de ningún tipo** — toda conversión es explícita (`.into()`, `as`, `From::from()`).

---

### 4.5 Binding de Almacenamiento: Las 4 Categorías

**Tiempo de vida:** período durante el cual la variable está vinculada a una dirección específica. *(Sebesta §5.4.3)*

#### Categoría 1 — Variables Estáticas

Vinculadas antes de la ejecución, permanecen hasta el fin del programa.

```typescript
let sesionesActivas = 0;        // variable de módulo: estática en la práctica
const VERSION = "1.0.0";        // estática e inmutable

let _cache: Map<string, string> | null = null;
export function getCache() {
    _cache ??= new Map();  // inicialización lazy — una sola vez
    return _cache;
}
```

```kotlin
class Sesion {
    companion object {
        private var contadorGlobal = 0   // estático de clase
        fun nuevaId() = ++contadorGlobal
    }
}
```

**Ventajas:** Eficiencia (dirección conocida en compilación), historial entre llamadas  
**Desventajas:** No soporta recursión efectiva, ocupa memoria siempre

#### Categoría 2 — Variables Dinámicas de Pila (Stack-dynamic)

Creadas al activar el subprograma, destruidas al retornar.

```typescript
function calcular(n: number): number {
    let resultado = 0;  // stack-dynamic
    let temp = n * 2;   // stack-dynamic
    return resultado + temp;
    // Al retornar: resultado y temp destruidas
}
```

**Permite recursión** porque cada activación tiene su propio frame en la pila.

**Activation Record (Sebesta §9.3):** Cada llamada crea un *stack frame* independiente en la pila. Por eso la recursión es posible: cada invocación tiene sus propias variables locales, sin interferir con las de las otras activaciones en curso.

> ⚠️ Los detalles internos del activation record (static link, dynamic link, dirección de retorno) pertenecen a Tema 13 (Abstracción Procedural). En esta clase solo interesa la consecuencia: **frame independiente → recursión segura**.

```typescript
function factorial(n: number): number {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
    // Cada llamada recursiva: su propia 'n' en su propio frame
    // Al retornar: frame destruido, frame del llamador restaurado via dynamic link
}
```

#### Categoría 3 — Variables Dinámicas de Heap Explícitas

Asignadas y liberadas de forma controlada (manual o por GC/ownership).

```typescript
class Nodo {
    constructor(
        public valor: number,
        public siguiente: Nodo | null = null
    ) {}
}
let cabeza = new Nodo(42);      // asignado en heap
cabeza = new Nodo(99);          // Nodo(42) queda sin referencias → GC lo libera
```

```rust
// Rust — heap con ownership: compilador garantiza la liberación
let elemento = Box::new(42);    // Box<i32> asigna en heap
// Al salir del scope: destructor automático — sin GC, sin leak posible
```

#### Categoría 4 — Variables Dinámicas de Heap Implícitas

Todos sus atributos (tipo, valor, dirección) se establecen cuando se les asigna un valor.

```python
# Python — el caso más claro:
x = [1, 2, 3]          # x: list — todos los atributos vinculados aquí
x = "uno, dos, tres"   # x: str — todos los atributos cambian
x = 42                 # x: int
type(x)                # int — binding en runtime
```

```typescript
// TypeScript con 'any' — se aproxima a Cat. 4 (desaconsejado)
let x: any = [1, 2, 3];
x = "uno, dos, tres";   // binding de tipo cambia — TypeScript permite con any
// Con tipos declarados: TypeScript es Cat. 2/3 (tipo fijo en compilación)
```

---

### 4.6 Ámbito (Scope)

**Definición:** Rango de instrucciones donde el nombre de una variable es visible.

#### Ámbito Estático (Léxico)

Introducido por ALGOL 60. Determinado en **tiempo de compilación**.

**Algoritmo de resolución:**  
1. Buscar en ámbito local → 2. Buscar en el bloque padre estático → ... → Error de compilación si no se encuentra

```typescript
let x = 10;  // ámbito: módulo

function externa() {
    let y = 20;
    function interna() {
        let z = 30;
        console.log(x);  // ✅ antepasado estático: módulo
        console.log(y);  // ✅ antepasado estático: externa
    }
    // console.log(z);  // ❌ z no visible aquí
}
```

**Problema (Sebesta §5.5.5):** Las variables del programa principal son visibles en **todos** los procedimientos → acceso involuntario a demasiados datos.

#### Ámbito Dinámico

Determinado en **tiempo de ejecución** según la cadena de llamadas.

**Algoritmo:** buscar en declaración local → subprograma que llamó → antepasados dinámicos → Runtime Error si no se encuentra.

**Problemas (Sebesta §5.5.4):**
- Variables locales del llamador visibles en el llamado → sin protección
- Imposibilidad de verificación estática de tipos para no-locales
- Acceso más lento que ámbito estático
- Programas difíciles de leer (hay que rastrear la cadena de llamadas)

> **Nota histórica:** Ámbito estático introducido por **ALGOL 60**. Los primeros dialectos de **Lisp** usaban ámbito dinámico; **Common Lisp** (1984) adoptó estático como default. El `this` de JavaScript tiene semántica de **ámbito dinámico** (se resuelve en tiempo de llamada) — por eso TypeScript recomienda arrow functions para capturarlo léxicamente.

#### Agujeros de Ámbito (Scope Holes)

Cuando una variable local tiene el mismo nombre que una del bloque envolvente, la exterior queda **oculta** en el bloque interior.

```typescript
let x = 10;           // x exterior

function procesarLista(items: number[]): void {
    for (const item of items) {
        const x = item * 2;   // x interior — oculta x exterior
        // "scope hole" de x exterior: empieza aquí
        console.log(x);       // 20, 40, ...
    }
    console.log(x);   // x exterior visible nuevamente: 10
}
```

Los linters modernos detectan shadowing: `@typescript-eslint/no-shadow` produce advertencia en el ejemplo anterior.

---

### 4.7 Entorno de Referencia. Constantes. Inicialización

**Entorno de referencia:** colección de todos los identificadores visibles en una sentencia dada.

**Constantes:**

```typescript
const PI = 3.14159;               // binding inmutable: referencia y valor
const CONFIG = { debug: false };  // binding inmutable de referencia; objeto mutable
```

**Inicialización** (Sebesta §5.4.3): binding variable → valor en el momento del binding de almacenamiento.

| Lenguaje | Comportamiento con variables no inicializadas |
|----------|----------------------------------------------|
| C | Estáticas → 0; locales → basura (undefined behavior) |
| Java | Numéricas → 0; booleanas → false; objetos → null |
| TypeScript (`strict: true`) | Detecta usos antes de asignación en compilación |
| Python | Cada asignación inicializa; uso sin asignación → NameError |
| Go | **Zero values** automáticos: 0, false, "", nil — sin basura |

---

### 4.8 Bloque IA — Errores de Ámbito (12 min)

#### Patrón 1: `var` hoisting silencioso

```typescript
// Código generado típico por IA (malas prácticas — corpus pre-ES6):
function procesar(activo: boolean) {
    if (activo) {
        var resultado = "ok";   // ← IA usa var
    }
    console.log(resultado);     // undefined — no ReferenceError
    // Con let → ReferenceError explícito y correcto
}
```

#### Patrón 2: Variable global silenciosa

```typescript
// IA genera efecto secundario implícito:
let total = 0;  // global oculta
function acumular(n: number) {
    total += n;  // muta global sin advertencia
    return total;
}

// Correcto — sin efectos secundarios:
function acumularPuro(total: number, n: number): number {
    return total + n;
}
```
Ámbito
#### Patrón 3: Shadowing inesperado

```typescript
const limite = 100;
function validar(items: number[]) {
    const limite = items.length;  // ← shadowing silencioso
    return items.filter(x => x < limite);  // ¿qué limite?
}
```

**Actividad activa — OA7 (Bloom: Evaluar):**

Proyectar el siguiente fragmento (sin comentarios). Los alumnos tienen 2 minutos para identificar en silencio cuántos errores de scope hay y a qué patrón corresponde cada uno. Luego respuesta grupal.

```typescript
let limite = 100;
var total = 0;

function procesar(items: number[]) {
    if (items.length > 0) {
        var resultado = items[0] * 2;
    }
    for (const item of items) {
        const limite = item;       // ¿qué limite se usa en filter?
        total += limite;
    }
    console.log(resultado);        // ¿qué valor tiene aquí?
    return items.filter(x => x < limite);
}
```

*Respuesta esperada:* Patrón 1 (`var resultado` → hoisting, `undefined` en `console.log`), Patrón 2 (`total` global mutable), Patrón 3 (`limite` shadowing silencioso en el for).

**Prompt seguro para código con variables:**

```
"TypeScript strict mode. Declara todo con let/const (nunca var).
Sin variables globales — todas las dependencias son parámetros explícitos.
Declara el tipo de cada parámetro."
```

---

## 5. Ejemplo Integrador — Las 4 Categorías en un Módulo TypeScript

```typescript
// Categoría 1: estática (módulo-level)
const VERSION = "1.0.0";
let sesionesActivas = 0;

class Sesion {
    // Categoría 3: heap-dynamic explícita
    private id: number;
    private datos: string[];

    constructor(id: number) {
        this.id = id;
        this.datos = [];  // array en heap
    }

    // Categoría 2: stack-dynamic
    agregar(item: string): void {
        let validado = item.trim();      // destruida al salir
        const ts = Date.now();           // destruida al salir
        this.datos.push(`${ts}: ${validado}`);
    }
}

function crearSesion(): Sesion {
    sesionesActivas++;
    return new Sesion(sesionesActivas);
    // El objeto Sesion en heap — liberado por GC (Categoría 3)
}
// Categoría 4 — solo con `any` o en Python: todos los atributos vinculados en asignación
```

---

## 6. Conexiones al Plan Mínimo

| Tópico plan mínimo | Cobertura |
|-------------------|-----------|
| Entidades y ligaduras (VI.9) | ✅ Completo: binding definition, 6 tiempos, atributos |
| Nombres y ámbito | ✅ Estático y dinámico, entorno de referencia |
| Categorías de variables | ✅ Las 4 categorías con ejemplos |
| Binding de tipos | ✅ Estático/dinámico/inferencia, fuerte/débil |
| Inicialización | ✅ Comparativa entre lenguajes |
| Compatibilidad nominal y estructural; subtipo; tipo derivado | 🔜 **Pendiente → Tema 10** (Tipos de Datos). TypeScript structural typing mencionado de paso en §4.2 solo como contexto. |

---

## 7. Stack de Lenguajes

| Rol | Lenguaje | Propósito |
|-----|----------|-----------|
| **Principal** | TypeScript | Binding estático + inferencia, let/const/var, scope, 4 categorías |
| **Contraste OO-JVM** | Kotlin | `val`/`var`, companion objects, null safety |
| **Contraste sistemas** | Rust | Ownership como binding explícito, drop automático, sin coerciones |
| **Contraste concurrente** | Go | Zero values, escape analysis, punteros seguros |
| **Contraste dinámico** | Python | Binding dinámico, duck typing, `id()` expone dirección |
| **Contraste funcional** | Haskell | Inferencia Hindley-Milner |
| **Referencia histórica** | C | Solo para contexto débil/fuerte (nunca como ejemplo primario) |

---

## 8. Materiales Requeridos

- [ ] Slides Clase 9.1: 5-tupla, binding times, 4 categorías, activation records, ámbito (a generar por Roberto)
- [ ] Diagrama de memoria: stack vs. heap (con activation records y GC)
- [ ] `variables.pdf` UNTDF 2024 (ya en ChromaDB)

---

## 9. FAQ Anticipado

**P: ¿Por qué `var` todavía existe en TypeScript?**  
R: Retrocompatibilidad. `var` tiene hoisting de función; `let`/`const` tienen hoisting de bloque con Temporal Dead Zone (TDZ) — no pueden usarse antes de su declaración → error de compilación.

**P: ¿El `const` de TypeScript es inmutable en todos los sentidos?**  
R: `const` hace inmutable la **referencia**, no el objeto. `const obj = {x: 1}; obj.x = 2;` es válido. Para inmutabilidad profunda: `Object.freeze()` o `Readonly<T>`.

**P: ¿El ámbito dinámico existe en algún lenguaje moderno?**  
R: Sí. Algunos dialectos de Lisp, Emacs Lisp, y Perl (`local`). El `this` de JavaScript tiene semántica de ámbito dinámico — por eso se usan arrow functions (`=>`) en TypeScript para capturarlo léxicamente.

---

## 10. Fuentes

1. **Sebesta, R. W.** (2019). *Concepts of Programming Languages* (12th ed.). Pearson. Cap. 5 (§5.3–5.8), Cap. 9 (§9.3 activation records).
2. **Gabbrielli, M. & Martini, S.** (2023). *Programming Languages: Principles and Paradigms* (2nd ed.). Springer. Cap. 4 (Names & Scope), Cap. 8 (type inference, fuerte/débil).
3. **Louden, K. C. & Lambert, K. A.** (2012). *Programming Languages: Principles and Practices* (3rd ed.). Course Technology. Cap. 7 (§7.7 scope).
4. **Filminas UNTDF 2024.** *Cuestiones semánticas vinculadas a Variables.* (ingesta/variables.pdf)
5. **TypeScript Handbook.** Variable Declarations, Strict Mode. https://www.typescriptlang.org/docs/

---

*Generado por Lic. Marcos 🗂️ — Topic Designer (EDU)*  
*1 clase × 120 min | Extraído de: 09-variables-binding/diseno.md (Clase 1 de 2)*  
*Fuentes: Sebesta Cap.5/9 + Gabbrielli Cap.4/8 + Louden Cap.7 + Filminas UNTDF 2024*  
*Estado: EN PRODUCCION — corregido contra `clase_dada.txt` por Dr. Roberto ✍️ (2026-06-28)*
