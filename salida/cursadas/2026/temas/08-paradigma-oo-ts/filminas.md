# Filminas — Tema 08: Paradigma OO — TypeScript + Smalltalk

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Docente:** Matías Gel — UNTDF / IDEI  
**Duración:** 120 minutos | **Clase:** 1 de 1 | **Slides:** 36  
**Generado por:** Lic. Marcos (topic-designer) + Dr. Roberto (class-writer) — 2026-04-28  
**Fuentes:** Gabbrielli & Martini (2023) Cap.10 OO; Sebesta (2019) Cap.12; Sweller/Chen CLT (2023)

---

## PORTADA

---

### [F-01] Paradigma OO — TypeScript + Smalltalk

@tipo: portada
@imagen: background
@prompt-imagen: sala de clases universitaria con pizarrón que muestra un diagrama de herencia de clases, ambiente académico moderno, paleta roja y blanca

# Paradigma Orientado a Objetos
## TypeScript · Smalltalk · Los 4 pilares

**Paradigmas y Lenguajes de Programación 2026**  
UNTDF — Instituto IDEI | Módulo IV — Semana 7

---

## BLOQUE 0 — Recapitulación (5 min)

---

### [F-02] ¿Qué sumamos hoy?

@tipo: socratica
@imagen: background
@prompt-imagen: tres puertas distintas etiquetadas con los tres paradigmas del cursado (Funcional, Lógico, OO), más una base representando el imperativo, ilustración minimalista, paleta roja

# ¿Qué sumamos hoy al cursado?

## Paradigmas vistos en el cursado:

- **Funcional** → *¿qué transformar?* — funciones puras, inmutabilidad
- **Lógico** → *¿qué es verdad?* — hechos, reglas, motor de inferencia
- **OO** → *(hoy)* — extensión del imperativo que encapsula estado y comportamiento

## El imperativo como base común:

OO **extiende** el imperativo — agrega encapsulamiento, herencia y polimorfismo sobre la base de instrucciones secuenciales y estado mutable.

## La pregunta generadora:

> *¿Qué tiene OO que los paradigmas funcional y lógico no tienen?*

Respuesta esperada: **estado encapsulado en objetos, comunicación por mensajes, identidad de entidades**

---

### [F-03] Los 4 pilares — adelanto

@tipo: tabla
@imagen: none

# Los 4 pilares del paradigma OO

| Pilar | Pregunta que responde | Ejemplo en una línea |
|-------|-----------------------|----------------------|
| **Encapsulamiento** | ¿Cómo protejo el estado interno? | `private saldo: number` |
| **Abstracción** | ¿Qué expongo al exterior? | `abstract area(): number` |
| **Herencia** | ¿Cómo reutilizo y especializo? | `class Perro extends Animal` |
| **Polimorfismo** | ¿Cómo trato distintos tipos uniformemente? | `formas.forEach(f => f.area())` |

Estos cuatro conceptos son el contenido central de la clase y del **Parcial 1**.  
Los trabajaremos primero en **Smalltalk** (OO puro) y luego en **TypeScript** (OO pragmático).

---

## BLOQUE 1 — Historia y filosofía del OO (20 min)

---

### [F-04] Simula 67 — el primer paso

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: línea de tiempo histórica de lenguajes de programación con Simula 67 marcado como punto de origen del paradigma OO, estilo académico

# Origen: Simula 67

## Nygaard & Dahl — Noruega, 1967

Primer lenguaje con objetos y clases — diseñado para **simular sistemas físicos**.

- Un `barco` tiene estado (velocidad, posición) y comportamiento (moverse, frenar)
- Múltiples barcos son *instancias* de la misma `clase Barco`
- No era "OO puro" — era ALGOL extendido con mecanismos de simulación

## Innovación central:

> Agrupar **datos** (estado) con las **operaciones** que los modifican → encapsulamiento

Antes de Simula: los datos eran estructuras separadas de las funciones que las procesaban.  
Simula dijo: *el barco sabe cómo moverse — no me lo decís vos desde afuera.*

---

### [F-05] Alan Kay — la visión original

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: retrato estilizado de Alan Kay trabajando en Xerox PARC en los años 70, rodeado de computadoras históricas, ilustración académica

# Alan Kay — Xerox PARC, 1970s

## La cita fundacional:

> *"The big idea is 'messaging' — that is what the kernel of Smalltalk/Squeak is all about. The key in making great and growable systems is much more to design how its modules communicate rather than what their internal properties and behaviors should be."*  
> — Alan Kay, 1998

## Los tres principios originales de Smalltalk:

1. **Todo es un objeto** — incluyendo números, booleanos, clases y métodos
2. **Los objetos se comunican únicamente por mensajes**
3. **Cada objeto tiene su propia memoria** — encapsulamiento absoluto

**Dato:** Kay consideraba que el nombre "OO" fue un **error** — el centro no son los objetos, son los **mensajes**.

---

### [F-06] Kay vs. lo que el mundo hizo después

@tipo: socratica
@imagen: background
@prompt-imagen: dos caminos divergentes en un bosque, uno limpio hacia Smalltalk y otro más ancho y pragmático hacia Java y TypeScript, ilustración conceptual académica

# La tensión central del paradigma OO

## Kay quería esto:

Objetos autónomos como células biológicas — cada uno con su propia lógica interna, comunicándose **solo por mensajes**. Sin clases rígidas si no eran necesarias. Sin primitivos. Todo objeto.

## El mundo hizo esto:

Java, C++, Python, TypeScript — lenguajes con **clases** como mecanismo central, primitivos por performance, verificación estática para escalar en equipo.

## La pregunta:

> *¿Importa la pureza filosófica o el resultado práctico?*

No hay una respuesta única. La tensión **pureza vs. pragmatismo** es la pregunta de diseño de lenguajes más importante del paradigma OO — y es lo que esta clase explora.

---

### [F-07] Evolución del OO — de la pureza al pragmatismo

@tipo: timeline
@imagen: none

# Evolución de los lenguajes OO

| Lenguaje | Año | Característica OO |
|----------|-----|-------------------|
| Simula 67 | 1967 | Clases, objetos, herencia |
| Smalltalk-80 | 1980 | Todo es objeto, mensajes, metaclases — **OO puro** |
| C++ | 1983 | OO sobre C — herencia múltiple, sin GC, tipos estáticos |
| Eiffel | 1986 | OO con contratos formales (precondiciones, postcondiciones) |
| Java | 1995 | OO con JVM, GC, herencia simple, interfaces — **OO pragmático** |
| Python | 1991 | OO multi-paradigma, duck typing dinámico |
| JavaScript | 1995 | OO **prototípico** (herencia sin clases hasta ES6) |
| TypeScript | 2012 | OO sobre JS — tipado estático estructural, `class` ES6+ |

**Tendencia:** cada generación gana en pragmatismo, pierde en pureza.  
**Pregunta clave de la clase:** ¿importa la pureza, o solo el resultado?

---

## BLOQUE 2 — Smalltalk: OO Puro (25 min)

---

### [F-08] "Todo es un objeto" — sin excepciones

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de jerarquía de clases de Smalltalk mostrando que números, booleanos y clases heredan de Object, estilo académico limpio con paleta roja y blanca

# Smalltalk — "Todo es un objeto"

## No hay primitivos. Ninguno.

En Smalltalk cada valor es una instancia de una clase:

- `5` → instancia de `SmallInteger` → hereda de `Integer → Number → Magnitude → Object`
- `true` → instancia de `True` → hereda de `Boolean → Object`
- `$A` → instancia de `Character` → hereda de `Magnitude → Object`
- `'hola'` → instancia de `String` → hereda de `Collection → Object`
- La clase `Animal` → instancia de su **metaclase** `Animal class`

## En TypeScript — primitivos existen:

```typescript
typeof 5        // "number"  ← NO es un objeto
typeof true     // "boolean" ← NO es un objeto
(5).toString()  // funciona por autoboxing implícito del runtime JS
```

**Autoboxing** = TypeScript/JS envuelven primitivos en objetos temporalmente. Smalltalk no necesita simularlo — son objetos de verdad.

---

### [F-09] "Todo es un objeto" — en código

@tipo: codigo

# Todo es objeto — ejemplos reales

## El número 5 sabe su clase

```smalltalk
5 class.               "→ SmallInteger"
5 class superclass.    "→ Integer"
5 class superclass superclass. "→ Number"
5 factorial.           "→ 120"
5 between: 1 and: 10.  "→ true"
5 printString.         "→ '5'"
```

## Los booleanos son objetos reales

```smalltalk
true class.       "→ True"
false class.      "→ False"
true & false.     "→ false"
true | false.     "→ true"
(3 > 2) ifTrue: ['mayor'] ifFalse: ['menor'].  "→ 'mayor'"
```

## Las clases son objetos

```smalltalk
SmallInteger superclass.        "→ Integer"
SmallInteger allSubclasses.     "→ todas las subclases"
SmallInteger methodDictionary.  "→ todos los métodos"
SmallInteger canUnderstand: #factorial.  "→ true"
```

**Consecuencia directa:** podés enviar mensajes a las clases igual que a cualquier objeto.

---

### [F-10] Cascades y `yourself` — sintaxis expresiva

@tipo: codigo

# Cascades — encadenar mensajes al mismo objeto

## El problema sin cascades:

```smalltalk
| col |
col := OrderedCollection new.
col add: 'primero'.
col add: 'segundo'.
col add: 'tercero'.
```

## Con cascades — el `;` repite el receptor:

```smalltalk
| col |
col := (OrderedCollection new)
    add: 'primero';
    add: 'segundo';
    add: 'tercero';
    yourself.   "← retorna la colección, no el último add:"
```

## Comparación con TypeScript — method chaining

```typescript
// En TypeScript con fluent interface / builder pattern:
class ColeccionBuilder {
  private items: string[] = [];
  add(item: string): this { this.items.push(item); return this; }
  build(): string[] { return this.items; }
}

const col = new ColeccionBuilder()
  .add("primero")
  .add("segundo")
  .add("tercero")
  .build();
```

**Nota:** `yourself` retorna el **receptor del cascade** (la colección), no el resultado del último mensaje enviado. Sin él, `col` sería `'tercero'` — el valor de retorno del último `add:`.

---

### [F-11] Mensajes — los tres tipos

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de tres sobres con flechas representando los tres tipos de mensajes Smalltalk (unario, binario, palabra clave), paleta roja y blanca, estilo académico

# Mensajes — tres tipos, una filosofía

## Mensajes unarios — sin argumentos (mayor precedencia)

```smalltalk
5 factorial.      "→ 120"
'hola' size.      "→ 4"
3.14 rounded.     "→ 3"
3.14 class.       "→ Float"
```

## Mensajes binarios — un argumento, notación infija

```smalltalk
3 + 4.        "→ 7    ← '+' es mensaje enviado a 3 con argumento 4"
5 > 3.        "→ true"
'ho' , 'la'.  "→ 'hola'"
3 + 4 * 2.    "→ 14   ← ¡NO es 11! binarios de izquierda a derecha"
```

## Mensajes de palabra clave — uno o más argumentos (menor precedencia)

```smalltalk
10 between: 5 and: 15.      "→ true"
anArray at: 2 put: 99.      "→ modifica posición 2"
a ifTrue: [x] ifFalse: [y]. "→ condicional"
```

**Regla:** `unarios > binarios > palabras clave`. Usá paréntesis para cambiar el orden.

---

### [F-12] Clases y herencia en Smalltalk

@tipo: codigo

# Clases y herencia — definición completa

## Definir la jerarquía

```smalltalk
Object subclass: #Animal
    instanceVariableNames: 'nombre'
    category: 'Ejemplo'.

Animal subclass: #Perro
    instanceVariableNames: 'raza'
    category: 'Ejemplo'.

"Accessors"
Animal >> nombre       ^ nombre
Animal >> nombre: n    nombre := n
Perro  >> raza: r      raza := r

"Comportamiento"
Animal >> hablar       ^ 'Soy un animal'
Perro  >> hablar       ^ 'Guau! Soy ', nombre, ', un ', raza
```

## Polimorfismo puro

```smalltalk
| animales |
animales := OrderedCollection new.
animales add: (Animal new nombre: 'Genérico').
animales add: (Perro new nombre: 'Rex'; raza: 'Labrador'; yourself).

animales do: [:a | Transcript showCr: a hablar].
"→ Soy un animal"
"→ Guau! Soy Rex, un Labrador"
```

El cliente solo sabe que recibe objetos que entienden `hablar`. No importa el tipo concreto.

---

### [F-13] Bloques — las lambdas de Smalltalk

@tipo: codigo

# Bloques — código como objeto

## Un bloque es un objeto que representa código diferido

```smalltalk
"Bloque con argumentos"
| cuadrado |
cuadrado := [:x | x * x].
cuadrado value: 5.    "→ 25"
cuadrado value: 12.   "→ 144"

"Bloque como condicional — ifTrue: recibe un bloque"
(temperatura > 30) ifTrue: ['Calor'] ifFalse: ['Fresco'].
```

## Los bloques son los mecanismos de control

```smalltalk
"Iteración — do: recibe un bloque"
#(1 2 3 4 5) do: [:n | Transcript showCr: n printString].

"Collect — equivalente a map"
#(1 2 3) collect: [:n | n * 2].  "→ #(2 4 6)"

"Select — equivalente a filter"
#(1 2 3 4 5) select: [:n | n > 3].  "→ #(4 5)"
```

## Comparación con TypeScript

```typescript
const cuadrado = (x: number) => x * x;
cuadrado(5); // 25

[1, 2, 3, 4, 5].forEach(n => console.log(n));
[1, 2, 3].map(n => n * 2);           // [2, 4, 6]
[1, 2, 3, 4, 5].filter(n => n > 3); // [4, 5]
```

Los bloques de Smalltalk son **objetos de primera clase** — igual que las funciones en TypeScript.

---

### [F-14] Metaclases — las clases son objetos

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de metaclases de Smalltalk mostrando que Animal es instancia de Animal class y Animal class es instancia de Metaclass, fondo blanco, diseño académico

# Metaclases — lo que hace único a Smalltalk

## La cadena de metaclases

```smalltalk
Animal class.            "→ Animal class"
Animal class class.      "→ Metaclass"
Animal class superclass. "→ Object class"
```

## Métodos de clase via metaclase

```smalltalk
Animal class >> crearConNombre: unNombre
    ^ self new nombre: unNombre

| p |
p := Perro crearConNombre: 'Fido'.
p hablar.  "→ 'Guau! Soy Fido...'"
```

## Comparación con TypeScript

```typescript
class Animal {
  static crearConNombre(nombre: string): Animal {
    const a = new Animal();
    a.nombre = nombre;
    return a;
  }
}
const p = Animal.crearConNombre("Fido");
```

**Diferencia:** en TypeScript los métodos `static` son un atajo sintáctico. Las clases no son ciudadanos de primera clase — no podés inspeccionar su metaclase ni enviarles mensajes arbitrarios en runtime.

---

### [F-15] Smalltalk hoy — Pharo

@tipo: demo

# Pharo — Smalltalk moderno (2026)

## Ejecutar Smalltalk hoy, sin instalar nada

```smalltalk
"En Pharo Playground — ejecutá esto:"
| col |
col := OrderedCollection new.
1 to: 10 do: [:i | col add: i * i].
col select: [:n | n > 20].
"→ OrderedCollection (25 36 49 64 81 100 )"
```

## ¿Para qué sirve aprender Pharo hoy?

| Uso | Ejemplo |
|-----|---------|
| **Pedagogía** | Pharo es el entorno de enseñanza de OO puro en Inria y U. de Berna |
| **Investigación** | Moose (análisis de código) está escrito en Pharo |
| **Comprensión** | Entender OO puro hace entender los trade-offs de TypeScript, Python, Java |

## El IDE de Pharo — todo es un objeto, incluso el IDE

El IDE de Pharo está escrito en Pharo. Podés inspeccionar el IDE con el IDE. No hay separación entre herramienta y lenguaje.

**Recurso:** https://pharo.org/ → IDE descargable en 2 minutos.

---

## BLOQUE 3 — TypeScript OO (25 min)

---

### [F-16] Clases en TypeScript — encapsulamiento

@tipo: codigo

# Clases TypeScript — la base

## Estructura canónica con modificadores de acceso

```typescript
class CuentaBancaria {
  private saldo: number;       // solo accesible internamente
  protected titular: string;   // accesible en subclases
  readonly numero: string;     // inmutable post-construcción

  constructor(titular: string, numero: string, saldoInicial: number) {
    this.titular = titular;
    this.numero = numero;
    this.saldo = saldoInicial;
  }

  depositar(monto: number): void {
    if (monto > 0) this.saldo += monto;
  }

  retirar(monto: number): boolean {
    if (monto > 0 && monto <= this.saldo) {
      this.saldo -= monto;
      return true;
    }
    return false;
  }

  obtenerSaldo(): number { return this.saldo; }
}

const c = new CuentaBancaria("Ana", "001-99", 1000);
c.depositar(500);
console.log(c.obtenerSaldo()); // 1500
// c.saldo = 9999;             // ❌ Error de compilación
```

---

### [F-17] Shorthand de constructor — menos boilerplate

@tipo: concepto-mixto

# Shorthand constructor — TypeScript idiomático

## Sin shorthand (verboso):

```typescript
class Punto {
  private x: number;
  private y: number;
  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}
```

## Con shorthand (idiomático):

```typescript
class Punto {
  constructor(private x: number, private y: number) {}

  distanciaAlOrigen(): number {
    return Math.sqrt(this.x ** 2 + this.y ** 2);
  }
}
```

## Mixto — con valores por defecto:

```typescript
class Configuracion {
  constructor(
    public readonly host: string,
    public puerto: number = 3000,
    private debug: boolean = false
  ) {}
}

const cfg = new Configuracion("localhost");
console.log(cfg.host, cfg.puerto); // "localhost" 3000
```

**Regla:** si el constructor solo asigna propiedades → shorthand. Si tiene lógica (validaciones, transformaciones) → forma explícita.

---

### [F-18] Herencia con `extends` — polimorfismo en acción

@tipo: codigo

# Herencia y polimorfismo — TypeScript

## La jerarquía Animal → Perro → PerroEntrenado

```typescript
class Animal {
  constructor(protected nombre: string) {}
  hablar(): string { return `Soy ${this.nombre}, un animal.`; }
}

class Perro extends Animal {
  constructor(nombre: string, private raza: string) {
    super(nombre); // OBLIGATORIO — llama al constructor del padre
  }
  hablar(): string { return `${this.nombre} dice: ¡Guau!`; }
  describirse(): string { return `${this.nombre} es un ${this.raza}`; }
}

class PerroEntrenado extends Perro {
  hablar(): string { return `${super.hablar()} (bien entrenado)`; }
}
```

## Polimorfismo en práctica

```typescript
const animales: Animal[] = [
  new Animal("Genérico"),
  new Perro("Rex", "Labrador"),
  new PerroEntrenado("Max", "Poodle"),
];

animales.forEach(a => console.log(a.hablar()));
// "Soy Genérico, un animal."
// "Rex dice: ¡Guau!"
// "Max dice: ¡Guau! (bien entrenado)"
```

TypeScript resuelve el método en **runtime** según el tipo real del objeto — aunque la variable sea `Animal`.

---

### [F-19] Interfaces — contratos estructurales

@tipo: codigo

# Interfaces — abstracción sin implementación

## Una clase puede implementar múltiples interfaces

```typescript
interface Describible { describirse(): string; }
interface Serializable { serializar(): string; }

class Perro extends Animal implements Describible, Serializable {
  constructor(nombre: string, private raza: string) { super(nombre); }

  hablar(): string { return `${this.nombre}: ¡Guau!`; }

  describirse(): string { return `${this.nombre} es un ${this.raza}`; }

  serializar(): string {
    return JSON.stringify({ nombre: this.nombre, raza: this.raza });
  }
}
```

## Interfaces como tipos de parámetros

```typescript
function mostrar(obj: Describible): void {
  console.log(obj.describirse());
}

mostrar(new Perro("Rex", "Labrador")); // ✓
```

**Nota:** una clase puede extender **una sola clase** pero implementar **múltiples interfaces** — esto resuelve el problema de la herencia múltiple de forma segura.

---

### [F-20] Tipado estructural — duck typing estático

@tipo: tabla-comparativa

# Tipado estructural vs. Nominal vs. Dinámico

| Aspecto | TypeScript (estructural) | Java (nominal) | Smalltalk (dinámico) |
|---------|--------------------------|-----------------|----------------------|
| Base de compatibilidad | Forma del objeto | Declaración explícita | Responde al mensaje |
| `implements` | Opcional | Obligatorio | No existe |
| Verificación | Compilación | Compilación | Runtime |
| Flexibilidad | Alta | Media | Máxima |
| Seguridad | Alta (estática) | Alta (estática) | Solo en runtime |

## Duck typing estático — ejemplo

```typescript
interface Medible { area(): number; }

class Circulo { area() { return Math.PI * 5 ** 2; } }

// Sin declarar 'implements Medible' — funciona igual:
const cuadradoLiteral = { area: () => 25 };

function imprimirArea(m: Medible) {
  console.log(`Área: ${m.area().toFixed(2)}`);
}

imprimirArea(new Circulo());    // ✓
imprimirArea(cuadradoLiteral);  // ✓ — estructuralmente compatible
```

**Gabbrielli & Martini (2023):** TypeScript es un lenguaje *gradualmente tipado* — la compatibilidad se define por estructura, no por nombre de clase.

---

### [F-21] Modificadores de acceso y clases abstractas

@tipo: tabla

# Modificadores y abstracción

| Modificador | Acceso | Smalltalk equivalente |
|-------------|--------|-----------------------|
| `public` | Desde cualquier lugar | Mensajes (todo) |
| `protected` | Clase + subclases | No existe formalmente |
| `private` | Solo la clase | Instancia vars siempre privadas |
| `readonly` | Inmutable post-init | — |
| `abstract` (clase) | No instanciable | Convención — no existe keyword |
| `abstract` (método) | Obliga implementación en subclase | `^ self subclassResponsibility` |

## Clase abstracta en TypeScript

```typescript
abstract class Forma {
  protected color: string;
  constructor(color: string) { this.color = color; }

  abstract area(): number;      // error en compilación si falta
  abstract perimetro(): number;

  esMasGrande(otra: Forma): boolean {
    return this.area() > otra.area();
  }
}

// new Forma("rojo"); // ❌ Cannot create an instance of an abstract class
```

---

### [F-22] Composición vs. herencia

@tipo: concepto-mixto

# Composición vs. herencia — elegir bien

## El anti-patrón: herencia por reutilización

```typescript
// ❌ Pila NO ES UN Array — herencia por conveniencia
class Pila extends Array<number> {
  tope(): number { return this[this.length - 1]; }
}

const p = new Pila();
p[0] = 99;      // ✓ TypeScript lo permite — pero rompe la abstracción de Pila
p.splice(0, 1); // ✓ TypeScript lo permite — viola el contrato de una Pila
```

## La solución: composición

```typescript
// ✓ Pila TIENE UN array — no es un array
class Pila<T> {
  private items: T[] = [];

  push(item: T): void { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
  tope(): T | undefined { return this.items[this.items.length - 1]; }
  estaVacia(): boolean { return this.items.length === 0; }
}
```

**Regla:** usá herencia cuando la subclase **es-un** tipo de la superclase (relación semántica real). Usá composición cuando solo querés **reutilizar comportamiento**.

---

## BLOQUE 4 — Comparación directa (20 min)

---

### [F-23] El dominio — formas geométricas

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: tres figuras geométricas (círculo rojo, rectángulo azul, triángulo verde) conectadas por flechas a una clase abstracta Forma, diagrama UML limpio, paleta académica

# Dominio compartido — mismo problema, dos lenguajes

## El problema:

- Jerarquía de **formas geométricas** (Círculo, Rectángulo, Triángulo)
- Cada forma tiene un `color` y puede calcular su `área` y `perímetro`
- Una colección itera todas las formas **polimórficamente**
- El cliente no sabe (ni necesita saber) el tipo concreto de cada forma

## ¿Por qué este dominio?

- Pequeño pero **estructuralmente completo** — usa los 4 pilares
- Sebesta (2019) lo usa para contrastar OO puro vs. pragmático
- Revela cómo cada lenguaje **fuerza** (o no) la abstracción
- Es el dominio tipo del **Parcial 1**

---

### [F-24] Formas en Smalltalk — OO puro

@tipo: codigo

# Formas en Smalltalk

## Definición

```smalltalk
Object subclass: #Forma
    instanceVariableNames: 'color'
    category: 'Geometria'.

Forma subclass: #Circulo
    instanceVariableNames: 'radio'.
Forma subclass: #Rectangulo
    instanceVariableNames: 'ancho alto'.

Forma >> area
    ^ self subclassResponsibility   "error en runtime si subclase no implementa"

Circulo >> radio: r    radio := r
Circulo >> area        ^ Float pi * radio * radio
Circulo >> perimetro   ^ 2 * Float pi * radio

Rectangulo >> ancho: a alto: h    ancho := a. alto := h.
Rectangulo >> area                ^ ancho * alto
Rectangulo >> perimetro           ^ 2 * (ancho + alto)
```

## Uso — polimorfismo puro

```smalltalk
| formas |
formas := OrderedCollection new.
formas add: (Circulo new radio: 5; color: 'rojo'; yourself).
formas add: (Rectangulo new ancho: 4 alto: 6; color: 'azul'; yourself).

formas do: [:f | Transcript showCr: f area printString].
"→ 78.53981..."
"→ 24"
```

---

### [F-25] Formas en TypeScript — definición base

@tipo: codigo

# Formas en TypeScript — clase abstracta

## Definición

```typescript
abstract class Forma {
  constructor(protected color: string) {}
  abstract area(): number;
  abstract perimetro(): number;

  toString(): string {
    return `${this.constructor.name}(${this.color}) → área=${this.area().toFixed(2)}, p=${this.perimetro().toFixed(2)}`;
  }
}

class Circulo extends Forma {
  constructor(private radio: number, color: string) { super(color); }
  area(): number { return Math.PI * this.radio ** 2; }
  perimetro(): number { return 2 * Math.PI * this.radio; }
}

class Rectangulo extends Forma {
  constructor(private ancho: number, private alto: number, color: string) {
    super(color);
  }
  area(): number { return this.ancho * this.alto; }
  perimetro(): number { return 2 * (this.ancho + this.alto); }
}
```

## Polimorfismo

```typescript
const formas: Forma[] = [
  new Circulo(5, "rojo"),
  new Rectangulo(4, 6, "azul"),
];
formas.forEach(f => console.log(f.toString()));
```

---

### [F-26] Extender el dominio — Principio Open/Closed

@tipo: codigo

# Agregar Triángulo sin tocar código existente

## Principio Open/Closed (OCP):

> *Abierto para extensión, cerrado para modificación.*

Agregar `Triangulo` **no requiere modificar** `Forma`, `Circulo` ni `Rectangulo`.

```typescript
class Triangulo extends Forma {
  constructor(
    private base: number,
    private lado1: number,
    private lado2: number,
    color: string
  ) { super(color); }

  area(): number {
    // Fórmula de Herón
    const s = (this.base + this.lado1 + this.lado2) / 2;
    return Math.sqrt(s * (s - this.base) * (s - this.lado1) * (s - this.lado2));
  }

  perimetro(): number { return this.base + this.lado1 + this.lado2; }
}

// El cliente polimórfico no cambió ni una línea:
const formas: Forma[] = [
  new Circulo(5, "rojo"),
  new Rectangulo(4, 6, "azul"),
  new Triangulo(3, 4, 5, "verde"),  // ← solo esto se agregó
];

formas.forEach(f => console.log(f.toString()));
// "Circulo(rojo) → área=78.54, p=31.42"
// "Rectangulo(azul) → área=24.00, p=20.00"
// "Triangulo(verde) → área=6.00, p=12.00"
```

---

### [F-27] Comparación directa — tabla

@tipo: tabla-comparativa

# Smalltalk vs. TypeScript — mismo dominio

| Aspecto | Smalltalk | TypeScript |
|---------|-----------|-----------|
| Método abstracto | `^ self subclassResponsibility` | `abstract area(): number` |
| Error si no se implementa | Runtime (al llamar) | **Compilación** (inmediato) |
| Iteración | Mensaje `do:` sobre Collection | Método `.forEach()` sobre Array |
| Instanciación | `Circulo new radio: 5; yourself` | `new Circulo(5, "rojo")` |
| Tipo de variable | Dinámico — cualquier objeto | Estático — `Forma[]` |
| Error de tipo | Runtime | Compilación |

---

### [F-28] Reflexión guiada

@tipo: socratica
@imagen: background
@prompt-imagen: pizarrón universitario con tres preguntas escritas en tiza sobre fondo oscuro, ambiente de aula de debate, estilo académico

# Comparación — análisis del dominio

## Tres preguntas para discutir:

### 1. ¿En qué caso Smalltalk es más expresivo?

- Mensajes como ciudadanos de primera clase
- Cascades — construir objetos en una línea
- Metaclases — las clases mismas son configurables en runtime

### 2. ¿En qué caso TypeScript es más robusto para equipos?

- Errores en compilación → el IDE te avisa antes de ejecutar
- `abstract` obliga a la implementación antes de deployar
- Tipado estructural permite verificar contratos en el repositorio

### 3. ¿Cuál sigue más la visión original de Alan Kay?

- Smalltalk — sin duda
- TypeScript hace concesiones al desarrollo industrial moderno
- La pregunta interesante: ¿Kay estaría de acuerdo con esas concesiones?

---

## BLOQUE IA — OO en el desarrollo moderno (10 min)

---

### [F-29] OO + LLMs — el paradigma dominante

@tipo: demo

# OO en el mundo moderno

## El paradigma más entrenado

Los LLMs (GPT, Copilot, Claude) fueron entrenados con enormes repositorios OO — Python, Java y TypeScript dominan el corpus.

**Implicación:** cuando el prompt pide una jerarquía con `abstract`, `implements` y polimorfismo, Copilot suele completar mejor.

```typescript
// Prompt a Copilot:
// "Modelá Email, SMS y Push con una interfaz común"
interface Notificacion { enviar(): void }

abstract class Canal implements Notificacion {
  constructor(protected destino: string) {}
  abstract enviar(): void;
}
```

---

### [F-30] Patrones GoF — OO destilado

@tipo: tabla

# Patrones de Diseño GoF (Gang of Four, 1994)

Los patrones GoF son **soluciones OO reutilizables a problemas recurrentes**.

| Patrón | Tipo | Qué resuelve | Ejemplo |
|--------|------|--------------|---------|
| **Strategy** | Comportamiento | Algoritmos intercambiables sin modificar el cliente | Ordenamiento — burbuja, merge |
| **Observer** | Comportamiento | Notificar a múltiples objetos cuando cambia el estado | EventEmitter, Redux |
| **Factory Method** | Creación | Delegar la instanciación a subclases | `crearForma(tipo): Forma` |
| **Decorator** | Estructura | Agregar responsabilidades dinámicamente | Middleware en Express.js |
| **Template Method** | Comportamiento | Esqueleto en clase base, pasos en subclases | `toString()` usa `area()` abstracto |

**Template Method** ya lo usamos sin nombrarlo: `toString()` en `Forma` llama a `area()` — definido en la clase abstracta, implementado en subclases.

---

## CIERRE (15 min)

---

### [F-31] Síntesis — Smalltalk vs. TypeScript

@tipo: tabla-comparativa

# Síntesis del Módulo IV — Clase 1

| Concepto OO | Smalltalk | TypeScript |
|-------------|-----------|-----------|
| Todo es objeto | ✅ absoluto | ❌ primitivos (`number`, `boolean`) |
| Mensajes | ✅ única forma de interacción | ✅ llamadas a métodos |
| Clases como objetos | ✅ metaclases | ⚠️ parcial — métodos `static` |
| Herencia | ✅ simple (`subclass:`) | ✅ simple (`extends`) |
| Polimorfismo | ✅ dinámico puro | ✅ dinámico + verificación estática |
| Encapsulamiento | ✅ inst. vars siempre privadas | ✅ `private`/`protected`/`readonly` |
| Clases abstractas | ⚠️ `subclassResponsibility` (runtime) | ✅ `abstract` (compilación) |
| Interfaces | ❌ no existen | ✅ duck typing estático |
| Bloques/lambdas | ✅ objetos de primera clase | ✅ arrow functions |
| Operadores redefinibles | ✅ son mensajes | ❌ operadores fijos |
| Verificación de tipos | Runtime | Compilación |

**Conclusión:** Smalltalk realiza la visión de Kay con más pureza. TypeScript hace concesiones al desarrollo industrial moderno.

---

### [F-32] Los 4 pilares — síntesis con código

@tipo: tabla

# Los 4 pilares — síntesis

| Pilar | Definición en una línea | TypeScript | Smalltalk |
|-------|------------------------|------------|-----------|
| **Encapsulamiento** | Ocultar el estado interno | `private saldo: number` | Variables de inst. siempre privadas |
| **Abstracción** | Exponer solo la interfaz | `abstract area(): number` | `^ self subclassResponsibility` |
| **Herencia** | Reutilizar y especializar | `class Perro extends Animal` | `Animal subclass: #Perro` |
| **Polimorfismo** | Un contrato, muchas formas | `formas.forEach(f => f.area())` | `formas do: [:f | f area]` |

## Los 4 pilares en un solo fragmento

```typescript
abstract class Forma {              // abstracción — no instanciable
  constructor(protected color: string) {} // encapsulamiento

  abstract area(): number;          // abstracción — obliga implementación
}

class Circulo extends Forma {       // herencia
  constructor(private radio: number, color: string) { super(color); }
  area(): number { return Math.PI * this.radio ** 2; } // encapsulamiento
}

const formas: Forma[] = [new Circulo(5, "rojo")];
formas.forEach(f => console.log(f.area())); // polimorfismo
```

---

### [F-33] Mapa de paradigmas del cursado

@tipo: diagrama
@imagen: content
@prompt-imagen: mapa conceptual con tres nodos principales (Funcional, Lógico, OO) y un nodo base (Imperativo) del que OO extiende, flechas que muestran relaciones y contrastes, estilo de mapa mental académico con paleta roja y blanca

# Los tres paradigmas del cursado — mapa comparativo

**OO** es una extensión del **imperativo** — por eso no se estudia como paradigma separado sino como evolución.

| | Funcional | Lógico | OO (extiende Imperativo) |
|-|-----------|--------|-------------------------|
| **Control** | Recursión, combinadores | Motor de inferencia | Despacho de mensajes + loops/if |
| **Estado** | Inmutable | Hechos / unificación | Mutable, encapsulado en objetos |
| **Abstracción** | Funciones de orden superior | Relaciones | Clases, interfaces |
| **Reutilización** | Composición funcional | Reglas generales | Herencia, composición |
| **Lenguaje tipo** | Haskell, Elixir, TS parcial | Prolog | Smalltalk, Java, TypeScript |
| **Modelo central** | Transformación de datos | Satisfacción de restricciones | Objetos que colaboran |

**Para el Parcial 1:** deberías poder contrastar al menos dos de estos paradigmas para el mismo problema y argumentar las decisiones de diseño.

---

### [F-34] Conceptos clave — Parcial 1

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: lista de conceptos clave resaltados en una pizarra universitaria con marcadores de colores, ambiente académico de preparación para examen

# Para el Parcial 1 — lo que hay que saber

## Los 4 pilares — definición + ejemplo en código:

1. **Encapsulamiento** → `private`, `protected`, accessors
2. **Abstracción** → `abstract`, interfaces
3. **Herencia** → `extends`, `super()`
4. **Polimorfismo** → override, despacho dinámico

## Diferencias clave a argumentar:

- **OO puro (Smalltalk)** vs. **OO pragmático (TypeScript)** — todo es objeto vs. primitivos
- **Polimorfismo por herencia** (`extends`) vs. **por interfaz** (`implements`)
- **Tipado nominal** (Java) vs. **estructural** (TS) vs. **duck typing dinámico** (Smalltalk)
- **Composición** vs. **herencia** — cuándo elegir cada una

## Formato del Parcial 1:

- Dominio: un problema modelado en **dos paradigmas** (OO + funcional o lógico)
- Implementación en TypeScript (OO) + argumentación de decisiones
- Duración: 100 minutos | Material: documentación oficial + apuntes

---

### [F-35] TP08 — GitHub + autograding

@tipo: tabla

# TP08 — OO en TypeScript

GitHub Classroom crea tu repositorio personal y el autograding publica la nota en cada `git push`.

| Tramo | Qué hacés | Cómo se evalúa |
|-------|-----------|----------------|
| Ejercicio 1 | Jerarquía con herencia y polimorfismo | Tests Vitest |
| Ejercicio 2 | Interfaces y contratos estructurales | Tests Vitest |
| Ejercicio 3 | Dominio libre en TypeScript OO | Tests + revisión docente |
| Entrega | `git push` dispara GitHub Actions | Nota automática en el commit |

---

### [F-36] Cierre — Parcial 1

@tipo: cierre
@imagen: background
@prompt-imagen: aula universitaria al final de la clase con luz cálida, estudiantes guardando cosas y conversando, ambiente de cierre de jornada académica, paleta roja y blanca

# Cierre — Tema 08

## TP08 — disponible en GitHub Classroom:

**Repositorio:** asignado al aceptar el assignment  
**Fecha límite:** una semana | **Autograding:** automático en cada push via GitHub Actions

## Próxima semana:

**Semana 8 — Parcial Práctico Nº 1**  
Dominio: dos paradigmas para un mismo problema (OO + funcional o lógico)  
Duración: 100 minutos | Material: documentación + apuntes

## Preguntas:

---
