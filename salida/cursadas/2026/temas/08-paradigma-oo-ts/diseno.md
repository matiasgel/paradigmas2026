# Diseño de Tema 08 — Paradigma OO: TypeScript + Smalltalk (OO Puro)

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Institución:** UNTDF — Instituto IDEI  
**Docente:** Matías Gel  
**Duración de clase:** 120 minutos ← CONSTRAINT DE GENERACIÓN. No superar.  
**Estado:** APROBADO  
**Fecha de aprobación:** 2026-04-28  
**Fecha de diseño:** 2026-04-27  
**Módulo del plan:** IV — Paradigma de Programación Orientada a Objetos  
**Semana:** 7 | **Clase en el ciclo:** 1 de 1  
**Lenguaje principal:** TypeScript  
**Lenguaje de contraste (OO puro):** Smalltalk  
**Clase anterior (T07):** Paradigma Lógico — Prolog Avanzado (unificación, listas, recursión)  
**Clase siguiente (T09):** Variables, Binding y Ámbito  

---

## 1. Objetivo General de la Clase

Introducir el **paradigma orientado a objetos** desde su concepción más pura — Smalltalk — para luego estudiar cómo TypeScript implementa el mismo paradigma con compromisos pragmáticos. El alumno debe al final de la clase poder identificar los conceptos nucleares de OO (objetos, mensajes, clases, herencia, polimorfismo, encapsulamiento), articularlos en código TypeScript, y contrastarlos con la forma en que Smalltalk los realiza como principios de diseño absolutos.

**Pregunta generadora de la clase:**  
*"¿Qué significa que un lenguaje sea 'orientado a objetos'? ¿Es TypeScript tan OO como Smalltalk, o solo lo simula?"*

---

## 2. Objetivos Específicos (Bloom)

| Nivel | Objetivo |
|-------|----------|
| **Recordar** | Enumerar los cuatro pilares del paradigma OO: encapsulamiento, abstracción, herencia, polimorfismo |
| **Comprender** | Explicar qué significa "todo es un objeto" en Smalltalk y por qué TypeScript no lo cumple del mismo modo |
| **Aplicar** | Implementar una jerarquía de clases simple con herencia y polimorfismo en TypeScript |
| **Analizar** | Comparar el mismo problema resuelto en Smalltalk vs. TypeScript, identificando diferencias en filosofía de diseño |
| **Evaluar** | Argumentar qué ventajas y compromisos introduce TypeScript respecto a un OO puro |
| **Crear** | Modelar un mini-dominio en TypeScript aplicando los principios de OO estudiados |

---

## 3. Conocimientos Previos Requeridos

- TypeScript básico (tipos, funciones, arrow functions) — cubierto en T03–T05
- Concepto de tipo y sistema de tipos — cubierto en T01
- Paradigma funcional (funciones puras, inmutabilidad) — T03–T05 como contrapunto
- Paradigma lógico (Prolog, declaratividad) — T06–T07 como contrapunto

---

## 4. Estructura de la Clase (120 min)

| Bloque | Duración | Contenido | Tipo |
|--------|----------|-----------|------|
| **B0** | 5 min | Recapitulación: paradigmas vistos. ¿Cuál viene ahora? | Retiro rápido / pregunta al grupo |
| **B1** | 20 min | Historia y filosofía del paradigma OO. Alan Kay, Simula, Smalltalk | Exposición + citas |
| **B2** | 25 min | Smalltalk: OO puro — todo es objeto, mensajes, metaclases, sin primitivos | Demostración + lectura de código |
| **B3** | 25 min | TypeScript OO: clases, interfaces, herencia, polimorfismo, tipado estructural | Demostración en vivo |
| **B4** | 20 min | Comparación directa: mismo dominio en Smalltalk vs. TypeScript | Pizarrón + análisis guiado |
| **IA** | 10 min | Bloque IA: OO en el desarrollo moderno + herramientas IA y patrones OO | Discusión |
| **B5** | 15 min | Cierre, síntesis, apertura de conceptos para Parcial 1 | Cierre estructurado |

---

## 5. Contenidos Detallados

### 5.1 Bloque 0 — Repaso (5 min)

Tres paradigmas vistos: **imperativo** (cómo hacerlo paso a paso), **funcional** (qué transformaciones hacer sin estado), **lógico** (qué es verdad, que el motor infiera).

Pregunta al grupo: *¿Qué agregaría un cuarto paradigma que no hayan tenido los anteriores?*

Respuesta esperada → el **modelo de objetos**: encapsular estado y comportamiento juntos, comunicar mediante mensajes.

---

### 5.2 Bloque 1 — Historia y Filosofía del OO (20 min)

#### 5.2.1 Origen: Simula 67

El primer lenguaje con conceptos OO fue **Simula 67** (Nygaard & Dahl, Noruega). Introdujo clases y objetos para simular sistemas del mundo real. No era "OO puro" — era un ALGOL extendido con mecanismos de simulación.

#### 5.2.2 Alan Kay y la visión de Smalltalk

Alan Kay (Xerox PARC, 1970s) acuñó el término *"Object-Oriented Programming"*. Su visión original era radical:

> *"The big idea is 'messaging' — that is what the kernel of Smalltalk/Squeak is all about […] The key in making great and growable systems is much more to design how its modules communicate rather than what their internal properties and behaviors should be."*  
> — Alan Kay, email a la lista de Squeak, 1998

Para Kay, OO **no era** principalmente sobre clases o herencia — era sobre **mensajes entre objetos autónomos**.

Los tres principios originales de Smalltalk:
1. **Todo es un objeto** — incluyendo números, booleanos, clases, métodos
2. **Los objetos se comunican únicamente por mensajes**
3. **Cada objeto tiene su propia memoria** — encapsulamiento absoluto

#### 5.2.3 Evolución posterior

| Lenguaje | Año | Característica OO |
|----------|-----|-------------------|
| Simula 67 | 1967 | Clases, objetos, herencia |
| Smalltalk-80 | 1980 | Todo es objeto, mensajes, metaclases |
| C++ | 1983 | OO sobre C, tipos estáticos, herencia múltiple |
| Java | 1995 | OO con JVM, GC, herencia simple, interfaces |
| Python | 1991 | OO multi-paradigma, duck typing |
| JavaScript | 1995 | OO prototípico (no basado en clases inicialmente) |
| TypeScript | 2012 | OO sobre JS, tipado estático estructural, `class` ES6+ |

**Punto a marcar:** en la evolución del OO, los lenguajes se volvieron cada vez más *pragmáticos* y cada vez menos *puros*. Smalltalk es el punto de partida máximo de pureza.

---

### 5.3 Bloque 2 — Smalltalk: OO Puro (25 min)

#### 5.3.1 "Todo es un objeto" — sin excepciones

En Smalltalk, no existen primitivos:

```smalltalk
"El número 5 es un objeto de la clase SmallInt"
5 class.          "→ SmallInteger"
5 class superclass. "→ Integer → Number → Magnitude → Object"

"Los booleanos son objetos"
true class.  "→ True"
false class. "→ False"

"Los caracteres son objetos"
$A class.    "→ Character"

"Las clases son objetos"
SmallInteger class. "→ SmallInteger class (metaclass)"
```

Comparar con TypeScript:
```typescript
typeof 5         // "number" — no es un objeto, es un primitivo
(5).toString()   // funciona por autoboxing implícito
```

Este autoboxing en TypeScript (heredado de JS) es evidencia de que el modelo de tipos no es uniformemente orientado a objetos.

#### 5.3.2 Mensajes — la única forma de interacción

En Smalltalk, todo lo que pasa es el resultado de **enviar un mensaje a un objeto**. No hay llamadas a funciones globales, ni operadores especiales — todo es mensaje.

```smalltalk
"Mensajes unarios (sin argumentos)"
5 factorial.        "→ 120"
'hola' size.        "→ 4"
3.14 rounded.       "→ 3"

"Mensajes binarios (un argumento, notación infija)"
3 + 4.              "→ 7"  "  ← + es un mensaje enviado a 3 con argumento 4"
5 > 3.              "→ true"

"Mensajes de palabra clave (keyword messages)"
OrderedCollection new add: 'hola'; add: 'mundo'; yourself.
```

> *En Smalltalk, `3 + 4` no es una operación aritmética — es el objeto `3` recibiendo el mensaje `+` con argumento `4`, respondiendo con `7`.*

Esto tiene consecuencias profundas: **cualquier operador puede ser redefinido** simplemente definiendo un método con ese nombre en una clase.

#### 5.3.3 Clases y herencia en Smalltalk

```smalltalk
"Definición de clase"
Object subclass: #Animal
    instanceVariableNames: 'nombre'
    classVariableNames: ''
    poolDictionaries: ''
    category: 'Ejemplo'.

Animal subclass: #Perro
    instanceVariableNames: ''
    classVariableNames: ''
    poolDictionaries: ''
    category: 'Ejemplo'.

"Definición de métodos"
Animal >> hablar
    ^ 'Soy un animal'

Perro >> hablar
    ^ 'Guau!'

"Uso"
| a p |
a := Animal new.
p := Perro new.
a hablar.   "→ 'Soy un animal'"
p hablar.   "→ 'Guau!'"
```

#### 5.3.4 Metaclases — las clases son objetos

En Smalltalk, la clase `Animal` en sí misma es un objeto — una instancia de su **metaclase** (`Animal class`). Esto permite que las clases tengan comportamiento propio (métodos de clase).

Esta característica no existe de manera limpia en TypeScript — los métodos `static` de TypeScript son un atajo práctico, pero las clases no son ciudadanos de primera clase de la misma manera.

---

### 5.4 Bloque 3 — TypeScript OO (25 min)

#### 5.4.1 Clases en TypeScript (ES6+)

```typescript
class Animal {
  // Encapsulamiento con modificadores de acceso
  protected nombre: string;
  
  constructor(nombre: string) {
    this.nombre = nombre;
  }
  
  hablar(): string {
    return `Soy ${this.nombre}, un animal.`;
  }
  
  toString(): string {
    return `Animal(${this.nombre})`;
  }
}

class Perro extends Animal {
  private raza: string;
  
  constructor(nombre: string, raza: string) {
    super(nombre);
    this.raza = raza;
  }
  
  // Polimorfismo por override
  hablar(): string {
    return `${this.nombre} dice: ¡Guau!`;
  }
  
  // Método propio
  describirse(): string {
    return `${this.nombre} es un ${this.raza}`;
  }
}

const a: Animal = new Animal("Genérico");
const p: Animal = new Perro("Rex", "Labrador");

console.log(a.hablar()); // "Soy Genérico, un animal."
console.log(p.hablar()); // "Rex dice: ¡Guau!"  ← polimorfismo
```

#### 5.4.2 Interfaces — abstracción y contratos

```typescript
interface Serializable {
  serializar(): string;
  static deserializar(data: string): Serializable; // Error: no se puede en TS
}

// En TypeScript se usa así:
interface Serializable {
  serializar(): string;
}

class Perro extends Animal implements Serializable {
  // ...
  serializar(): string {
    return JSON.stringify({ nombre: this.nombre, raza: this.raza });
  }
}
```

**Punto clave:** Las interfaces en TypeScript son contratos estructurales, no de identidad. Esto es tipado estructural (*duck typing* estático).

#### 5.4.3 Tipado Estructural vs. Tipado Nominal

```typescript
// Tipado estructural en acción
interface Ladrador {
  ladrar(): string;
}

class Perro implements Ladrador {
  ladrar() { return "Guau!"; }
}

// Esto también es válido — sin declarar 'implements':
const gato = {
  ladrar: () => "Miau... pero ladra"
};

function hacerLadrar(animal: Ladrador) {
  console.log(animal.ladrar());
}

hacerLadrar(new Perro());  // ✓
hacerLadrar(gato);          // ✓ — tipado estructural
```

**Contraste con Smalltalk:** En Smalltalk, la compatibilidad de tipos se verifica en *runtime* por la capacidad del objeto de responder a un mensaje — esto es duck typing dinámico. En TypeScript, la compatibilidad se verifica en *compilación* por la forma de la estructura — duck typing estático.

#### 5.4.4 Modificadores de acceso y encapsulamiento

| Modificador | TypeScript | Smalltalk |
|-------------|-----------|-----------|
| `public` | visible externamente | acceso por mensajes (todo) |
| `protected` | visible en subclases | no existe formalmente |
| `private` | solo en la clase | variables de instancia privadas por defecto |
| `readonly` | inmutable después de init | — |

**Nota:** En Smalltalk, las variables de instancia son **siempre privadas** — no hay acceso directo desde fuera del objeto. La única forma de acceder a ellas es a través de métodos (*accessors*). TypeScript permite lo mismo con `private`, pero también permite `public` en constructor con shorthand.

---

### 5.5 Bloque 4 — Comparación directa (20 min)

**Dominio de ejemplo:** Sistema de formas geométricas con cálculo de área.

#### En Smalltalk:

```smalltalk
Object subclass: #Forma
    instanceVariableNames: 'color'
    ...

Forma subclass: #Circulo
    instanceVariableNames: 'radio'
    ...

Forma subclass: #Rectangulo
    instanceVariableNames: 'ancho alto'
    ...

"Métodos"
Forma >> area
    ^ self subclassResponsibility  "obliga a las subclases a implementarlo"

Circulo >> area
    ^ Float pi * radio * radio

Rectangulo >> area
    ^ ancho * alto

"Polimorfismo puro — el cliente no sabe el tipo concreto"
| formas |
formas := OrderedCollection new.
formas add: (Circulo new radio: 5).
formas add: (Rectangulo new ancho: 4 alto: 6).
formas do: [:f | Transcript showCr: f area printString].
```

#### En TypeScript:

```typescript
abstract class Forma {
  protected color: string;
  
  constructor(color: string) { this.color = color; }
  
  abstract area(): number; // obliga a las subclases a implementarlo
  
  toString(): string {
    return `${this.constructor.name}(area=${this.area().toFixed(2)})`;
  }
}

class Circulo extends Forma {
  constructor(private radio: number, color: string) { super(color); }
  area(): number { return Math.PI * this.radio ** 2; }
}

class Rectangulo extends Forma {
  constructor(private ancho: number, private alto: number, color: string) {
    super(color);
  }
  area(): number { return this.ancho * this.alto; }
}

// Polimorfismo
const formas: Forma[] = [
  new Circulo(5, "rojo"),
  new Rectangulo(4, 6, "azul"),
];

formas.forEach(f => console.log(f.toString()));
```

#### Tabla comparativa del dominio:

| Aspecto | Smalltalk | TypeScript |
|---------|-----------|-----------|
| Método abstracto | `^ self subclassResponsibility` | `abstract area(): number` |
| Polimorfismo | Por despacho dinámico de mensajes | Por herencia + despacho dinámico |
| Sin implementación forzada | Error en runtime | Error en compilación |
| Iteración | `do:` (mensaje a Collection) | `.forEach()` (método de Array) |
| Acceso a tipo | `self class name` | `this.constructor.name` |
| Tipo de colección | `OrderedCollection` (objeto, mensaje `add:`) | `Array` (objeto JS, método `.push`) |

**Reflexión guiada:**
- *¿En qué caso Smalltalk es más expresivo?* — sintaxis de mensajes, metaclases, todo-objeto
- *¿En qué caso TypeScript es más robusto?* — chequeo estático en compilación, herramientas IDE
- *¿Cuál es más cercano a la visión original de Alan Kay?* — Smalltalk

---

### 5.6 Bloque IA — OO en el desarrollo moderno y herramientas IA (10 min)

**Temas a cubrir:**

1. **OO y los LLMs:** Los grandes modelos de lenguaje (ChatGPT, Copilot) fueron entrenados masivamente con código OO (Python, Java, TypeScript). El paradigma OO domina el código de producción en la web y mobile.

2. **GitHub Copilot y OO:** Demostrar cómo Copilot puede generar clases, sugerir herencia y completar métodos — y por qué el contexto OO del prompt mejora la calidad de las sugerencias.

3. **Patrones de diseño como OO destilado:** Los patrones GoF (Gang of Four) son soluciones OO reutilizables. Mencionar brevemente Strategy, Observer, Factory como patrones que emergerán en TPs.

4. **Reflexión:** ¿Tiene sentido aprender Smalltalk hoy? — Sí, como herramienta pedagógica: Pharo (Smalltalk moderno) se usa para enseñar OO puro en universidades europeas. La distinción entre OO puro y OO pragmático es clave para entender los trade-offs del diseño de lenguajes.

---

### 5.7 Bloque de Cierre (15 min)

#### Síntesis de la clase:

| Concepto | Smalltalk | TypeScript |
|----------|-----------|-----------|
| Todo es objeto | ✅ absoluto | ❌ primitivos existen |
| Comunicación por mensajes | ✅ única forma | ✅ llamadas a métodos (similar) |
| Clases como objetos | ✅ metaclases | ⚠️ parcial (métodos `static`) |
| Herencia | ✅ simple | ✅ simple (`extends`) |
| Polimorfismo | ✅ dinámico puro | ✅ dinámico + control estático |
| Encapsulamiento | ✅ instancia vars privadas | ✅ `private`/`protected` |
| Tipado | Dinámico (duck typing) | Estático estructural |
| Verificación de contratos | Runtime | Compilación |

#### Conceptos clave para el Parcial 1:
- Los cuatro pilares: encapsulamiento, abstracción, herencia, polimorfismo
- Diferencia entre OO puro (Smalltalk) y OO pragmático (TypeScript)
- Polimorfismo por herencia vs. polimorfismo por interfaz
- Tipado nominal vs. tipado estructural

#### Anuncio:
La semana siguiente (Semana 8) es el **Parcial Práctico Nº 1** — dominio: los cuatro paradigmas vistos (imperativo, funcional, lógico, OO). Se pide un programa que demuestre las diferencias entre paradigmas para un mismo problema.

---

## 6. Tópicos del Plan Mínimo Cubiertos

| Tópico del Plan Mínimo | Cobertura en esta clase |
|------------------------|------------------------|
| Niveles de polimorfismo | Polimorfismo por herencia, por interfaz, duck typing estático (TS) vs. dinámico (Smalltalk) |
| Encapsulamiento y abstracción | Modificadores de acceso en TS; variables de instancia privadas en Smalltalk; clases abstractas |
| Paradigmas: OO | Núcleo completo del Módulo IV |

---

## 7. Material de Referencia

### Bibliografía principal del curso:
- **Sebesta** — *Concepts of Programming Languages*, Cap. 12: "Support for Object-Oriented Programming"
- **Louden** — *Programming Languages: Principles and Practices*, Cap. 9: "Object-Oriented Programming"

### Para el contraste Smalltalk:
- Goldberg, A. & Robson, D. (1983). *Smalltalk-80: The Language and its Implementation*. Addison-Wesley. (fundacional)
- **Pharo by Example** (libre, online) — sintaxis Smalltalk moderna con Pharo

### Para TypeScript OO:
- Documentación oficial TypeScript — sección Classes: https://www.typescriptlang.org/docs/handbook/2/classes.html

---

## 8. Ejemplos de Código para Filminas

### Código minimal Smalltalk (para filminas — lectura, no ejecución en clase):
Los ejemplos de Smalltalk son **solo lectura** — no se pide a los alumnos que lo ejecuten, sino que lo analicen. El objetivo es entender la filosofía, no aprender la sintaxis de Smalltalk.

### Herramienta para demo en clase (opcional):
- **Pharo Playground** — https://pharo.org/ — Smalltalk moderno con IDE gráfico
- Se puede mostrar en vivo si hay tiempo, pero no es obligatorio

---

## 9. Scope del Tema — ⚠️ Fuera de Scope

Lo siguiente está **FUERA de scope** de esta clase. Decirlo explícitamente si los alumnos preguntan:

- **Mixins y traits** — se menciona de pasada, se trabaja en T14 (Sistemas de Tipos y Polimorfismo)
- **Generics en TypeScript** — cubierto en T14
- **Decoradores en TypeScript** — fuera del cursado
- **Patrones de diseño GoF** — se mencionan como referencia, pero no se desarrollan
- **Prototipos JavaScript** (mecanismo subyacente de las clases JS/TS) — fuera del cursado
- **Herencia múltiple** — se menciona como problema en C++, se muestra interfaces como alternativa en TS
- **Reflection en TypeScript** — fuera del cursado
- **Smalltalk full** — solo se usa como espejo conceptual, no se enseña el lenguaje

---

## 10. Indicaciones para el Diseñador de Filminas

### Estructura visual sugerida:
- **F-01**: Portada del tema — "Paradigma OO: TypeScript + Smalltalk"
- **F-02**: Recapitulación de paradigmas (B0) — tabla con los 4 paradigmas
- **F-03 a F-05**: Historia OO — Simula → Smalltalk → evolución (B1)
- **F-06 a F-09**: Smalltalk: todo es objeto, mensajes, código (B2) — énfasis en código y contrastes
- **F-10 a F-14**: TypeScript OO: clases, interfaces, herencia, tipado estructural (B3)
- **F-15 a F-17**: Comparación directa — formas geométricas lado a lado (B4)
- **F-18**: Bloque IA (B-IA)
- **F-19**: Síntesis comparativa — tabla grande de cierre (B5)
- **F-20**: Cierre — Parcial 1 y próxima clase

### Duración estimada por filmina: ~6 min promedio (20 filminas × 6 min ≈ 120 min)

### Código en filminas:
- Smalltalk: resaltar con estilo diferente (ej. fondo gris oscuro) para distinguirlo visualmente de TypeScript
- TypeScript: fondo oscuro estándar del cursado
- Usar comparativas lado a lado cuando sea posible (2 columnas: Smalltalk | TypeScript)

---

## Estado del Documento

- [x] Borrador generado por Marcos (topic-designer)
- [x] Revisado por Matías (docente)
- [x] **APROBADO** ← desbloquea la generación de minuta.md y filminas.md
