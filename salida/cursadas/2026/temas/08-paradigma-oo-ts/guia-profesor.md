# Guía del Profesor — Tema 08: Paradigma OO: TypeScript + Smalltalk

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Docente:** Matías Gel — UNTDF / IDEI  
**Duración:** 120 minutos | **Módulo IV — Semana 7**  
**Generado por:** Lic. Marcos (topic-designer) | **Fecha:** 2026-04-28  

---

## 1. Checklist pre-clase (hacer 15 min antes)

- [ ] TypeScript Playground abierto en: https://www.typescriptlang.org/play
- [ ] Pharo descargado o pestaña de demo online en: https://pharo.org/try
- [ ] Repositorio de la materia con `guia-estudio.md` accesible para mostrar a alumnos
- [ ] Link de GitHub Classroom para TP08 listo para pegar en el canal
- [ ] Proyector funcionando — verificar que el código sea legible desde el fondo del aula
- [ ] Pizarrón disponible para: (1) diagrama metaclases, (2) jerarquía de formas UML

---

## 2. Timing detallado — 36 slides en 120 minutos

> **Promedio: 3.3 min/slide.** El docente pasa rápido las slides de código — la explicación es oral y en el IDE, no leyendo la slide.

| Bloque | Slides | Min disponibles | Min/slide | Ritmo |
|--------|--------|-----------------|-----------|-------|
| **B0** Recapitulación | F-01 a F-03 | 5 | ~1.5 | Muy rápido |
| **B1** Historia | F-04 a F-07 | 20 | ~5 | Narrativo, pausas para debate |
| **B2** Smalltalk | F-08 a F-15 | 25 | ~3 | Demo + código |
| **B3** TypeScript | F-16 a F-22 | 25 | ~3.5 | Live coding en Playground |
| **B4** Comparación | F-23 a F-28 | 20 | ~3.3 | Análisis guiado |
| **B-IA** | F-29 a F-30 | 10 | ~5 | Demo Copilot + discusión |
| **B5** Cierre | F-31 a F-36 | 15 | ~2.5 | Síntesis rápida |

### Señales de alerta de tiempo

| Momento | Si llegaste a | Situación |
|---------|--------------|-----------|
| Min 25 | F-07 | ✅ En tiempo |
| Min 45 | F-15 | ✅ En tiempo |
| Min 70 | F-22 | ✅ En tiempo |
| Min 90 | F-28 | ✅ En tiempo |
| Min 100 | F-30 | ✅ En tiempo |
| Min 25 | F-04 | ⚠️ Atrasado — comprimir B1 |
| Min 45 | F-11 | ⚠️ Atrasado — saltar F-13 (bloques) |
| Min 70 | F-18 | ⚠️ Atrasado — ir directo a F-23 |

### Plan de contingencia si te atrasás

1. **Saltear F-13 (Bloques)** — se puede mencionar de pasada, es conceptualmente redundante con lambdas.
2. **Comprimir F-07 (Timeline)** — mostrar solo Smalltalk-80 y TypeScript, saltar el resto.
3. **Comprimir F-29-F-30 (Bloque IA)** — dejarlo como lectura opcional.
4. **F-34 (Conceptos clave)** es obligatoria — nunca saltearla.
5. **F-36 (Cierre)** es obligatoria — siempre terminar con el anuncio del Parcial.

---

## 3. Demos en vivo — setup y scripts

### Demo 1: TypeScript Playground (B3 — slides F-16 a F-26)

**URL:** https://www.typescriptlang.org/play

**Script de sesión** — copiar y pegar progresivamente:

```typescript
// PASO 1 — F-16: Encapsulamiento
class CuentaBancaria {
  private saldo: number;
  protected titular: string;
  readonly numero: string;

  constructor(titular: string, numero: string, saldoInicial: number) {
    this.titular = titular;
    this.numero = numero;
    this.saldo = saldoInicial;
  }

  depositar(monto: number): void {
    if (monto > 0) this.saldo += monto;
  }

  obtenerSaldo(): number { return this.saldo; }
}

const c = new CuentaBancaria("Ana", "001", 1000);
c.depositar(500);
console.log(c.obtenerSaldo()); // 1500
// c.saldo = 9999; // ← descomentar para mostrar error

// PASO 2 — F-18: Herencia y polimorfismo
class Animal {
  constructor(protected nombre: string) {}
  hablar(): string { return `Soy ${this.nombre}, un animal.`; }
}

class Perro extends Animal {
  constructor(nombre: string, private raza: string) { super(nombre); }
  hablar(): string { return `${this.nombre} dice: ¡Guau!`; }
}

class PerroEntrenado extends Perro {
  hablar(): string { return `${super.hablar()} (bien entrenado)`; }
}

const animales: Animal[] = [
  new Animal("Genérico"),
  new Perro("Rex", "Labrador"),
  new PerroEntrenado("Max", "Poodle"),
];
animales.forEach(a => console.log(a.hablar()));

// PASO 3 — F-25/F-26: Dominio de formas
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

class Triangulo extends Forma {
  constructor(
    private base: number,
    private lado1: number,
    private lado2: number,
    color: string
  ) { super(color); }

  area(): number {
    const s = (this.base + this.lado1 + this.lado2) / 2;
    return Math.sqrt(s * (s - this.base) * (s - this.lado1) * (s - this.lado2));
  }

  perimetro(): number { return this.base + this.lado1 + this.lado2; }
}

// new Forma("rojo"); // ← descomentar para mostrar error de abstract

const formas: Forma[] = [
  new Circulo(5, "rojo"),
  new Rectangulo(4, 6, "azul"),
  new Triangulo(3, 4, 5, "verde"), // área = 6, verificar con Herón
];
formas.forEach(f => console.log(f.toString()));
```

### Demo 2: Pharo Playground (B2 — slides F-09, F-12, F-15)

**Instalar:** Pharo 12 desde https://pharo.org/  
**Alternativa online:** https://pharo.org/try (limitado pero funciona para demos básicos)

**Script de sesión Pharo:**

```smalltalk
"Demo F-09 — todo es objeto"
5 class.                          "SmallInteger"
5 class superclass.               "Integer"
#(1 2 3 4 5) collect: [:n | n * n].   "1 4 9 16 25"
#(1 2 3 4 5) select: [:n | n > 3].    "4 5"
#(1 2 3 4 5) inject: 0 into: [:acc :n | acc + n].  "15"

"Demo F-12 — jerarquía Animal"
Object subclass: #Animal
    instanceVariableNames: 'nombre'
    category: 'Demo'.

Animal subclass: #Perro
    instanceVariableNames: 'raza'
    category: 'Demo'.

Animal >> nombre: n    nombre := n.
Animal >> hablar       ^ 'Soy un animal'.
Perro  >> raza: r      raza := r.
Perro  >> hablar       ^ 'Guau! Soy ', nombre, ', un ', raza.

| animales |
animales := OrderedCollection new.
animales add: (Animal new nombre: 'Genérico').
animales add: (Perro new nombre: 'Rex'; raza: 'Labrador'; yourself).
animales do: [:a | Transcript showCr: a hablar].

"Demo F-15 — cuadrados y filtro"
| col |
col := OrderedCollection new.
1 to: 10 do: [:i | col add: i * i].
(col select: [:n | n > 20]) printString.
```

### Demo 3: GitHub Copilot (B-IA — slide F-29)

```typescript
// Escribir solo esto y mostrar qué completa Copilot:
abstract class Vehiculo {
  constructor(protected marca: string, protected velocidadMax: number) {}
  abstract tipoCombustible(): string;
  // ← dejar que Copilot sugiera el resto
}

// También: pedir verbalmente:
// "Creá una jerarquía para un sistema de notificaciones
//  con Email, SMS y Push. Usá abstract, implements y polimorfismo."
```

---

## 4. Preguntas frecuentes y respuestas sugeridas

### Sobre Smalltalk

**"¿Para qué aprender Smalltalk si nadie lo usa?"**  
→ *"Smalltalk es como el latín para los lingüistas: casi nadie lo habla, pero entenderlo explica todos los demás lenguajes. Cuando ven `forEach` en TypeScript o `each` en Ruby, están viendo Smalltalk. Cuando ven metaclases en Python, están viendo Smalltalk."*

**"¿Pharo se usa en el mundo real?"**  
→ *"Sí: Moose (análisis de código estático) está en Pharo. ESUG (European Smalltalk Users Group) tiene conferencias anuales. Universidades de Berna, Inria (Francia) y varias alemanas lo enseñan. No es masivo, pero está vivo."*

**"¿`=` en Smalltalk es igualdad o asignación?"**  
→ *"`=` es igualdad (comparación). `:=` es asignación. Ojo: es al revés que en C/Java/TypeScript donde `=` asigna y `==` compara."*

### Sobre TypeScript

**"¿Por qué `super()` es obligatorio?"**  
→ *"Porque el constructor del padre puede inicializar propiedades que el hijo necesita. TypeScript lo verifica en compilación para evitar que `this` esté en estado inconsistente."*

**"¿Se puede hacer herencia múltiple en TypeScript?"**  
→ *"No con `extends` — solo una clase padre. Pero podés implementar múltiples interfaces. Esto es intencional: la herencia múltiple de implementación (como en C++) genera ambigüedades difíciles de resolver."*

**"¿Qué diferencia hay entre `interface` y `type` en TypeScript?"**  
→ *"Para clases OO: casi ninguna en práctica. `interface` es la convención para contratos de clases. `type` es más flexible para tipos complejos (uniones, intersecciones). Para el parcial y TPs: usen `interface`."*

**"¿TypeScript compila a qué?"**  
→ *"A JavaScript. El sistema de tipos desaparece en tiempo de ejecución — `tsc` lo borra. En runtime, TypeScript ES JavaScript."*

### Sobre OO en general

**"¿El polimorfismo funciona igual que en Haskell con typeclasses?"**  
→ *"Similar pero diferente. En Haskell el polimorfismo es paramétrico y de tipo — el compilador especializa. En OO es de subtipo — el dispatch es dinámico en runtime basado en el tipo real del objeto."*

**"¿OO y funcional son compatibles?"**  
→ *"Completamente. Scala, Kotlin, F# y el propio TypeScript lo mezclan. Las arrow functions, `map`, `filter` que usaron en bloques anteriores son programación funcional dentro de TypeScript OO."*

---

## 5. Conceptos con mayor riesgo de confusión

| Concepto | Confusión típica | Corrección |
|----------|-----------------|------------|
| Autoboxing en JS/TS | "Si `(5).toString()` funciona, entonces 5 es un objeto" | El 5 se envuelve temporalmente en `Number` para la llamada — luego se descarta. No es un objeto persistente. |
| `private` en TS | "¿Es igual que en Java?" | En runtime JavaScript NO hay `private` — TypeScript lo elimina en compilación. En Java es enforced en JVM. |
| `abstract` en TS | "¿Puedo hacer `new Forma()`?" | No — TypeScript lo bloquea en compilación. Smalltalk permite instanciar `Forma` pero falla al llamar `area()` en runtime. |
| `extends` vs `implements` | "¿Cuándo uso uno u otro?" | `extends` = hereda implementación (una sola). `implements` = solo el contrato (múltiples). |
| `this` vs `self` | "`this` en TypeScript es `self` en Smalltalk?" | Conceptualmente sí — ambos refieren al objeto receptor. `this` en JS puede perder contexto en callbacks (usar arrow functions). |
| Composición | "Si Pila extends Array funciona, ¿para qué composición?" | Funciona tecnicamente, pero expone la API completa de Array. La composición da control explícito de qué se expone. |
| Tipado estructural | "¿Puedo pasar cualquier objeto a cualquier función?" | Solo si tiene la estructura que la función espera — TypeScript verifica las propiedades y métodos requeridos. |

---

## 6. Diagrama de pizarrón — metaclases

Dibujar durante F-14:

```
Animal new  ──────instancia de──────▶  Animal
                                          │
                                     instancia de
                                          │
                                          ▼
                                     Animal class  ──────instancia de──────▶  Metaclass
                                          │
                                     superclass
                                          │
                                          ▼
                                     Object class
```

**Punto clave para decir:** *"En TypeScript, la clase `Animal` es solo una sintaxis — en runtime es una función constructora de JS. En Smalltalk, `Animal` es un objeto real de la clase `Animal class` que tiene su propia memoria y métodos."*

---

## 7. Anuncio del TP08 — script

**En F-35, decir exactamente:**

*"El TP08 está disponible ahora — pego el link en el canal. Lo aceptan hoy así tienen la semana completa.*

*Cuatro ejercicios en TypeScript:*
- *Primero: jerarquía de herencia básica con polimorfismo.*  
- *Segundo: usar interfaces como contratos estructurales.*  
- *Tercero: dominio libre — modelen una entidad del mundo real con los cuatro pilares.*  
- *Cuarto (opcional): el mismo dominio del ejercicio tres en Pharo — no entra a la nota pero suma puntos extra.*

*El autograding corre en cada push — van a ver inmediatamente si los tests pasan. El `package.json` ya tiene todo configurado: instalen con `npm install` y ejecuten con `npm test`.*

*Fecha límite: en una semana. Si tienen problemas con el setup de TypeScript en su máquina, díganme después de clase."*

---

## 8. Apertura del Parcial 1 — contexto para el docente

**Parcial 1 — semana siguiente**

- **Formato:** problema modelado en dos paradigmas a elección (OO + funcional, o OO + lógico)
- **Implementación esperada:** TypeScript (OO) + Haskell/Elixir o Prolog
- **Duración:** 100 minutos | Material: documentación oficial + apuntes propios
- **Dominio tipo:** similar al de formas geométricas — pequeño, con jerarquía de objetos clara

**Lo que necesitan dominar:**
1. Los cuatro pilares con ejemplos de código (F-32)
2. Diferencias TS vs. Smalltalk en la tabla de F-31
3. Cuándo usar composición vs. herencia (F-22)
4. Extender un dominio sin modificar código existente — OCP (F-26)

**Rubrica orientativa:**
- Código correcto que compila: 40%
- Uso correcto de los pilares OO: 30%
- Argumentación de decisiones de diseño: 30%

---

## 9. Referencias de la clase

- Gabbrielli & Martini (2023). *Programming Languages: Principles and Paradigms*, 3ª ed. Cap. 10 — OO. Springer.
- Sebesta (2019). *Concepts of Programming Languages*, 12ª ed. Cap. 12 — OO. Pearson.
- Sweller, J. & Chen, O. (2023). *Cognitive Load Theory: A Handbook for Applied Practice*. Routledge.
- Pharo Project: https://pharo.org/ | Pharo by Example: https://books.pharo.org/
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/
