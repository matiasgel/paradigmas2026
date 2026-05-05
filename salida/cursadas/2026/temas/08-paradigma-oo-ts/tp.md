# TP Tema 08 — Paradigma Orientado a Objetos en TypeScript

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Docente:** Matías Gel — UNTDF / IDEI  
**Tema:** 08 — Paradigma OO: TypeScript  
**Modalidad:** Repo individual en GitHub Classroom  
**Puntos totales:** 100  
**Ejercicios:** 12  

---

## ¿Cómo aceptar el TP?

1. Hacé click en el link de invitación publicado en el aula virtual
2. GitHub Classroom crea un repo privado para vos automáticamente
3. Clonás tu repo:  
   ```bash
   git clone https://github.com/Laboratorio-y-paradigmas-UNTDF/tp08-oo-typescript-<tuusuario>.git
   cd tp08-oo-typescript-<tuusuario>
   ```
4. Trabajás en `src/tp08_oo.ts`
5. Cada `git push` dispara los tests automáticamente en GitHub Actions

---

## Objetivo pedagógico

Aplicar los **cuatro pilares del paradigma OO** — encapsulamiento, abstracción, herencia y polimorfismo — en TypeScript, siguiendo los patrones vistos en clase (filminas F-16 a F-32).

Cada ejercicio aplica uno o más pilares en forma progresiva. Al completar el TP debería quedar clara la diferencia entre:
- herencia de implementación vs. composición
- clase abstracta vs. interfaz
- polimorfismo en tiempo de compilación vs. en tiempo de ejecución

---

## Estructura del TP

| Sección | Ejercicios | Tema OO | Puntos |
|---------|-----------|---------|--------|
| **A — Encapsulamiento** | 1–3 | `private`, `protected`, accessors, validación | 25 |
| **B — Abstracción y herencia** | 4–7 | `abstract`, `extends`, `super`, polimorfismo | 35 |
| **C — Interfaces y composición** | 8–10 | `interface`, `implements`, composición sobre herencia | 25 |
| **D — Integración** | 11–12 | Patrones Template Method y Strategy con los 4 pilares | 15 |
| **Total** | | | **100** |

---

## Reglas del TP

- **Modificá únicamente** el archivo `src/tp08_oo.ts`
- No cambies las firmas de los métodos — los tests dependen de ellas
- No importes librerías externas (solo TypeScript estándar y Node.js built-ins)
- Para cálculos con floats los tests aceptan una tolerancia de `±0.01`
- El autograding corre con `jest` (`npm test`) — no hace falta compilar manualmente

---

## Recursos de referencia

- Filminas F-16 a F-32 (Google Slides del tema)
- Guía de estudio Tema 08 (`guia-estudio.md`)
- [TypeScript Handbook — Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)
- [TypeScript Handbook — Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)

---

## Cómo correr los tests localmente

```bash
# Instalar dependencias (una sola vez)
npm install

# Correr todos los tests
npm test

# Correr tests de un ejercicio específico
npm test -- --testNamePattern="Ejercicio 3"

# Correr en modo watch (re-corre al guardar)
npm run test:watch
```

---

## SECCIÓN A — Encapsulamiento

---

### Ejercicio 1 — CuentaBancaria (8 pts)

**Concepto:** encapsulamiento con `private`, validación de invariantes de clase.

**Referencia:** filmina F-16 — *"Clases en TypeScript — la base"*

**Contexto:**  
Una cuenta bancaria tiene estado interno (`saldo`, `titular`) que no debe ser modificado directamente desde afuera. Solo ciertos mensajes (`depositar`, `retirar`) tienen permiso de alterarlo, y solo si los datos son válidos.  
Este es el principio fundamental del encapsulamiento: **el objeto protege su propio estado**.

**Consigna:**  
Completá la clase `CuentaBancaria` en `src/tp08_oo.ts`:

- `private saldo: number` — no accesible directamente desde afuera
- `constructor(titular: string, saldoInicial: number)` — lanza `Error("Saldo inicial negativo")` si `saldoInicial < 0`
- `depositar(monto: number): void` — suma `monto` al saldo; ignora montos `<= 0`
- `retirar(monto: number): boolean` — retorna `true` y descuenta si `monto > 0` y `monto <= saldo`; retorna `false` en caso contrario (sin modificar el saldo)
- `obtenerSaldo(): number` — retorna el saldo actual
- `get titular(): string` — getter de solo lectura

**Ejemplos:**
```typescript
const c = new CuentaBancaria("Ana", 1000);
c.depositar(500);
c.obtenerSaldo();           // 1500
c.retirar(200);             // true
c.obtenerSaldo();           // 1300
c.retirar(9999);            // false — fondos insuficientes
c.obtenerSaldo();           // 1300 — sin cambio
c.titular;                  // "Ana"

new CuentaBancaria("X", -1); // lanza Error
```

**Pista:**  
El getter `titular` se define con la keyword `get`. Para que TypeScript no confunda la propiedad interna con el getter, usá `private _titular: string` internamente y exponelo como `get titular()`.

---

### Ejercicio 2 — Temperatura (8 pts)

**Concepto:** encapsulamiento con validación, `readonly`, múltiples constructores simulados con factory methods.

**Referencia:** filmina F-17 — *"Shorthand constructor"*

**Contexto:**  
Una temperatura tiene un valor y una escala (Celsius o Fahrenheit). El estado es inmutable post-construcción (`readonly`). Sin embargo, el usuario quiere poder crear temperaturas en cualquier escala y convertirlas. Los factory methods permiten "múltiples constructores" de forma idiomática en TypeScript.

**Consigna:**  
Completá la clase `Temperatura`:

- Constructor privado: `private constructor(readonly valor: number, readonly escala: "C" | "F")`
- Factory method: `static desdeCelsius(v: number): Temperatura`
- Factory method: `static desdeFahrenheit(v: number): Temperatura`
- `aCelsius(): number` — si ya es Celsius retorna `valor`; si es Fahrenheit aplica `(valor - 32) * 5/9`
- `aFahrenheit(): number` — si ya es Fahrenheit retorna `valor`; si es Celsius aplica `valor * 9/5 + 32`
- `esMasCaliente(otra: Temperatura): boolean` — compara ambas en Celsius

**Ejemplos:**
```typescript
const t1 = Temperatura.desdeCelsius(100);
t1.valor;               // 100
t1.escala;              // "C"
t1.aFahrenheit();       // 212
t1.aCelsius();          // 100

const t2 = Temperatura.desdeFahrenheit(32);
t2.aCelsius();          // 0
t2.aFahrenheit();       // 32

t1.esMasCaliente(t2);   // true — 100°C > 0°C

// new Temperatura(100, "C"); // ❌ constructor privado
```

**Pista:**  
Con el constructor privado, los usuarios solo pueden crear `Temperatura` vía los factory methods. Esto garantiza que el estado siempre sea válido y la escala siempre sea `"C"` o `"F"`.

---

### Ejercicio 3 — Historial de cuenta (9 pts)

**Concepto:** encapsulamiento de colecciones — exponer vista de solo lectura, no la colección interna.

**Referencia:** filmina F-16 + F-22 (*composición*)

**Contexto:**  
Un problema clásico de encapsulamiento es con colecciones: si el getter retorna la referencia al array interno, el código externo puede modificarlo directamente (`cuenta.historial.push(...)`) sin pasar por los métodos validados. La solución es retornar una copia o una vista de solo lectura.

**Consigna:**  
Extendé `CuentaBancaria` creando la clase `CuentaConHistorial`:

- Hereda de `CuentaBancaria`
- Registra cada operación en un `private _historial: string[]`
- `depositar(monto: number): void` — además de depositar, agrega al historial `"Depósito: +${monto}"` (solo si el monto es > 0)
- `retirar(monto: number): boolean` — si la operación tiene éxito agrega `"Retiro: -${monto}"`; si falla agrega `"Retiro fallido: ${monto}"`
- `get historial(): readonly string[]` — retorna una copia del historial como `readonly` (usá `[...this._historial]`)
- `cantidadMovimientos(): number`

**Ejemplos:**
```typescript
const c = new CuentaConHistorial("Luis", 500);
c.depositar(200);
c.retirar(100);
c.retirar(9999);
c.historial;
// ["Depósito: +200", "Retiro: -100", "Retiro fallido: 9999"]
c.cantidadMovimientos(); // 3

// El historial expuesto es de solo lectura:
const h = c.historial;
// h.push("hack"); // ❌ Error TypeScript — readonly
```

**Pista:**  
Al usar `[...this._historial]` retornás una copia superficial del array. El tipo de retorno `readonly string[]` le dice a TypeScript que quien recibe el historial no puede modificarlo. Esto es diferente a `ReadonlyArray<string>` pero tiene el mismo efecto.

---

## SECCIÓN B — Abstracción y herencia

---

### Ejercicio 4 — Jerarquía de Formas (8 pts)

**Concepto:** clase abstracta, métodos abstractos, herencia simple.

**Referencia:** filminas F-21 y F-25 — *"Clase abstracta"* y *"Formas en TypeScript"*

**Contexto:**  
Una clase abstracta define el **contrato** (qué métodos deben existir) sin implementarlos. Las subclases están obligadas a implementar esos métodos — TypeScript lo verifica en compilación, a diferencia de Smalltalk que lo detecta en runtime. Este es el mecanismo de **abstracción** del paradigma OO.

**Consigna:**  
Implementá la clase abstracta `Forma` y las subclases `Circulo` y `Rectangulo`:

Clase `Forma` (abstracta):
- `constructor(protected color: string)`
- `abstract area(): number`
- `abstract perimetro(): number`
- `describe(): string` — retorna `"${this.constructor.name}(${this.color}): área=${this.area().toFixed(2)}, p=${this.perimetro().toFixed(2)}"`
- `esMasGrande(otra: Forma): boolean` — compara por área

Clase `Circulo extends Forma`:
- `constructor(private radio: number, color: string)`
- `area()`: `Math.PI * radio²`
- `perimetro()`: `2 * Math.PI * radio`

Clase `Rectangulo extends Forma`:
- `constructor(private ancho: number, private alto: number, color: string)`
- `area()`: `ancho * alto`
- `perimetro()`: `2 * (ancho + alto)`

**Ejemplos:**
```typescript
const c = new Circulo(5, "rojo");
c.area();        // ≈78.54
c.perimetro();   // ≈31.42
c.describe();    // "Circulo(rojo): área=78.54, p=31.42"

const r = new Rectangulo(4, 6, "azul");
r.area();        // 24
r.esMasGrande(c); // false (24 < 78.54)

// new Forma("verde"); // ❌ no se puede instanciar
```

**Pista:**  
`this.constructor.name` en el método `describe()` retorna el nombre de la clase concreta (ej: `"Circulo"`), no `"Forma"`. Esto funciona porque TypeScript resuelve el método en el objeto real en tiempo de ejecución.

---

### Ejercicio 5 — Triángulo y Open/Closed (8 pts)

**Concepto:** Principio Open/Closed — extender sin modificar código existente.

**Referencia:** filmina F-26 — *"Agregar Triángulo sin tocar código existente"*

**Contexto:**  
El Principio Open/Closed (OCP) dice que el software debe estar *abierto para extensión pero cerrado para modificación*. En OO esto se logra con herencia: agregás una nueva subclase sin tocar la jerarquía existente, y el código polimórfico del cliente funciona sin cambios.

**Consigna:**  
Implementá `Triangulo extends Forma`:

- `constructor(private base: number, private lado1: number, private lado2: number, color: string)`
- `area()`: fórmula de Herón — `s = (base + lado1 + lado2) / 2`, área = `sqrt(s*(s-base)*(s-lado1)*(s-lado2))`
- `perimetro()`: `base + lado1 + lado2`
- `esRectangulo(): boolean` — retorna `true` si cumple Pitágoras con los tres lados (usá `Math.round` para comparar con enteros o tolerancia `0.001`)

Y completá la función libre:
```typescript
function formaConMayorArea(formas: Forma[]): Forma
```
Que retorna la forma con mayor área. Si la lista está vacía lanza `Error("Lista vacía")`.

**Ejemplos:**
```typescript
const t = new Triangulo(3, 4, 5, "verde");
t.area();            // 6
t.perimetro();       // 12
t.esRectangulo();    // true (3² + 4² = 5²)
t.describe();        // "Triangulo(verde): área=6.00, p=12.00"

const formas: Forma[] = [
  new Circulo(5, "rojo"),
  new Rectangulo(4, 6, "azul"),
  new Triangulo(3, 4, 5, "verde"),
];
formaConMayorArea(formas).constructor.name; // "Circulo"
```

**Pista:**  
Para verificar Pitágoras con lados flotantes no compares directamente (`a² + b² === c²`). Ordená los tres lados de menor a mayor y compará `lados[0]² + lados[1]² ≈ lados[2]²` con tolerancia `< 0.001`.

---

### Ejercicio 6 — Jerarquía de Empleados (9 pts)

**Concepto:** herencia multi-nivel, `super`, sobrescritura de métodos.

**Referencia:** filmina F-18 — *"Herencia y polimorfismo — TypeScript"* (Animal → Perro → PerroEntrenado)

**Contexto:**  
La herencia multi-nivel modela especialización incremental. Cada nivel agrega o especializa el comportamiento del nivel anterior usando `super` para reusar la lógica de la clase padre. El polimorfismo permite tratar un array de `Empleado` sin importar si son `EmpleadoFullTime` o `Gerente`.

**Consigna:**  
Implementá la jerarquía:

Clase base `Empleado`:
- `constructor(protected nombre: string, protected salarioBase: number)`
- `calcularSueldo(): number` — retorna `salarioBase`
- `presentarse(): string` — retorna `"Empleado: ${nombre}, sueldo: $${this.calcularSueldo()}"`

Clase `EmpleadoFullTime extends Empleado`:
- `constructor(nombre: string, salarioBase: number, private bonoAnual: number)`
- `calcularSueldo(): number` — retorna `salarioBase + bonoAnual / 12`
- `presentarse(): string` — retorna `"${super.presentarse()} (full-time)"`

Clase `Gerente extends EmpleadoFullTime`:
- `constructor(nombre: string, salarioBase: number, bonoAnual: number, private porcentajeComision: number)`
- `calcularSueldo(): number` — retorna `super.calcularSueldo() * (1 + porcentajeComision / 100)`
- `presentarse(): string` — retorna `"${super.presentarse()} [Gerente, comisión ${porcentajeComision}%]"`

**Ejemplos:**
```typescript
const e = new Empleado("Carlos", 1000);
e.calcularSueldo();  // 1000
e.presentarse();     // "Empleado: Carlos, sueldo: $1000"

const ft = new EmpleadoFullTime("Ana", 1000, 2400);
ft.calcularSueldo(); // 1200 (1000 + 2400/12)
ft.presentarse();    // "Empleado: Ana, sueldo: $1200 (full-time)"

const g = new Gerente("Luis", 1000, 2400, 20);
g.calcularSueldo();  // 1440 (1200 * 1.20)
g.presentarse();     // "Empleado: Luis, sueldo: $1440 (full-time) [Gerente, comisión 20%]"

// Polimorfismo:
const equipo: Empleado[] = [e, ft, g];
equipo.map(emp => emp.calcularSueldo()); // [1000, 1200, 1440]
```

**Pista:**  
`super.presentarse()` llama al método del nivel inmediatamente superior. En `Gerente`, llama a `EmpleadoFullTime.presentarse()`, que a su vez ya llamó a `Empleado.presentarse()`. El resultado se va construyendo por capas.

---

### Ejercicio 7 — Animal con `toString` Template Method (10 pts)

**Concepto:** patrón Template Method — la clase abstracta define el esqueleto del algoritmo, las subclases implementan los pasos.

**Referencia:** filmina F-30 — *"Template Method"* (tabla de patrones GoF)

**Contexto:**  
El patrón **Template Method** es el patrón OO más básico: la clase abstracta define un método que llama a otros métodos abstractos que las subclases deben implementar. Así, el "esqueleto" del algoritmo queda en la clase base (no se duplica) y solo los "pasos" varían. En el ejercicio 4 ya usaste esto sin nombrarlo: `describe()` llama a `area()` y `perimetro()`, que son abstractos.

**Consigna:**  
Implementá la jerarquía:

Clase abstracta `Animal`:
- `constructor(protected nombre: string, protected edad: number)`
- `abstract sonido(): string` — el sonido que hace el animal
- `abstract tipoAlimentacion(): string` — `"herbívoro"`, `"carnívoro"` o `"omnívoro"`
- `abstract velocidadMaxima(): number` — en km/h
- `presentarse(): string` — **Template Method** que retorna:  
  `"${nombre} (${edad} años) dice '${sonido()}', es ${tipoAlimentacion()} y corre a ${velocidadMaxima()} km/h"`
- `esMasRapido(otro: Animal): boolean`

Subclases (implementan los tres métodos abstractos):

`Perro`: sonido `"Guau"`, alimentación `"omnívoro"`, velocidad `48`  
`Gato`: sonido `"Miau"`, alimentación `"carnívoro"`, velocidad `48`  
`Caballo`: sonido `"Hiiiii"`, alimentación `"herbívoro"`, velocidad `88`  
`Vaca`: sonido `"Mu"`, alimentación `"herbívoro"`, velocidad `25`

Cada subclase tiene `constructor(nombre: string, edad: number)` que llama a `super`.

**Ejemplos:**
```typescript
const p = new Perro("Rex", 3);
p.presentarse();
// "Rex (3 años) dice 'Guau', es omnívoro y corre a 48 km/h"

const c = new Caballo("Spirit", 5);
c.esMasRapido(p); // true (88 > 48)

const animales: Animal[] = [new Perro("Rex", 3), new Gato("Misi", 2), new Caballo("Spirit", 5)];
animales.map(a => a.sonido()); // ["Guau", "Miau", "Hiiiii"]
```

**Pista:**  
El Template Method (`presentarse`) queda en `Animal` una sola vez. Las subclases nunca sobrescriben `presentarse` — solo implementan los pasos abstractos. Si querés cambiar el formato de presentación lo cambiás en un solo lugar.

---

## SECCIÓN C — Interfaces y composición

---

### Ejercicio 8 — Interfaces múltiples (8 pts)

**Concepto:** `interface`, `implements`, tipado estructural, compatibilidad sin herencia.

**Referencia:** filmina F-19 — *"Interfaces — contratos estructurales"* y F-20 — *"Duck typing estático"*

**Contexto:**  
Una clase puede implementar múltiples interfaces pero solo extender una clase. Las interfaces son contratos puros — no aportan implementación, solo verifican que el objeto expone los métodos requeridos. El tipado estructural de TypeScript permite que un objeto sin `implements` sea compatible con una interfaz si tiene la forma correcta.

**Consigna:**  
Define las interfaces y la clase:

```typescript
interface Serializable {
  serializar(): string;      // retorna JSON del objeto
  static deserializar?(json: string): any; // opcional — no la testeamos
}

interface Comparable<T> {
  comparar(otro: T): -1 | 0 | 1;  // -1 si this < otro, 0 si igual, 1 si mayor
}

interface Imprimible {
  imprimir(): void;  // imprime con console.log
}
```

Clase `Producto implements Serializable, Comparable<Producto>, Imprimible`:
- `constructor(public nombre: string, public precio: number, public stock: number)`
- `serializar(): string` — retorna `JSON.stringify({nombre, precio, stock})`
- `comparar(otro: Producto): -1 | 0 | 1` — compara por `precio`
- `imprimir(): void` — imprime `"[${nombre}] $${precio} (stock: ${stock})"`

Y la función libre:
```typescript
function ordenarProductos(productos: Comparable<Producto>[]): Producto[]
```
Que ordena usando `comparar()` (de menor a mayor precio).

**Ejemplos:**
```typescript
const p1 = new Producto("Mouse", 25, 10);
const p2 = new Producto("Teclado", 50, 5);
const p3 = new Producto("Monitor", 200, 2);

p1.serializar();     // '{"nombre":"Mouse","precio":25,"stock":10}'
p1.comparar(p2);     // -1
p2.comparar(p1);     // 1
p1.comparar(new Producto("Otro", 25, 99)); // 0

ordenarProductos([p3, p1, p2]).map(p => p.nombre);
// ["Mouse", "Teclado", "Monitor"]
```

**Pista:**  
Para `comparar`: `precio < otro.precio → -1`, `precio > otro.precio → 1`, `precio === otro.precio → 0`. Para ordenar con `comparar` podés usar `Array.sort()` con `(a, b) => a.comparar(b)`.

---

### Ejercicio 9 — Composición sobre herencia (8 pts)

**Concepto:** composición — un objeto "tiene un" objeto de otro tipo en lugar de "ser un" subtipo.

**Referencia:** filmina F-22 — *"Composición vs. herencia — elegir bien"* (Pila<T>)

**Contexto:**  
La herencia se usa mal cuando el único motivo es reutilizar código de otra clase, no porque exista una relación "es-un" real. La composición es más flexible: el objeto delega comportamiento a otros objetos que contiene. En TypeScript, las pilas, colas y buffers se modelan con composición sobre un array interno.

**Consigna:**  
Implementá usando composición (NO herencia de Array):

Clase `Pila<T>`:
- `private items: T[] = []`
- `push(item: T): void`
- `pop(): T` — lanza `Error("Pila vacía")` si está vacía
- `tope(): T` — lanza `Error("Pila vacía")` si está vacía; no modifica
- `estaVacia(): boolean`
- `tamaño(): number`
- `toArray(): T[]` — retorna copia del contenido (el tope al final)

Clase `Cola<T>`:
- `private items: T[] = []`
- `encolar(item: T): void`
- `desencolar(): T` — lanza `Error("Cola vacía")` si está vacía
- `frente(): T` — lanza `Error("Cola vacía")` si está vacía; no modifica
- `estaVacia(): boolean`
- `tamaño(): number`

**Ejemplos:**
```typescript
const pila = new Pila<number>();
pila.push(1); pila.push(2); pila.push(3);
pila.tope();         // 3
pila.pop();          // 3
pila.tamaño();       // 2
pila.toArray();      // [1, 2]

const cola = new Cola<string>();
cola.encolar("a"); cola.encolar("b"); cola.encolar("c");
cola.frente();       // "a"
cola.desencolar();   // "a"
cola.tamaño();       // 2

const pilaVacia = new Pila<number>();
pilaVacia.pop();     // lanza Error("Pila vacía")
```

**Pista:**  
Para `Pila`, el `tope()` es `items[items.length - 1]` y `pop()` usa `Array.pop()`. Para `Cola`, el `frente()` es `items[0]` y `desencolar()` usa `Array.shift()`. Recordá que `toArray()` debe retornar una copia (`[...this.items]`), no la referencia interna.

---

### Ejercicio 10 — Sistema de notificaciones (9 pts)

**Concepto:** composición + interfaces + polimorfismo sin herencia.

**Referencia:** filmina F-29 — *"OO + LLMs — el paradigma dominante"* (ejemplo `Canal`, `Email`, `SMS`, `Push`)

**Contexto:**  
Un sistema de notificaciones puede enviar mensajes por distintos canales (email, SMS, push). Cada canal tiene su propia lógica de envío. El sistema no sabe (ni necesita saber) qué canal concreto usa — solo que implementa la interfaz `Canal`. Esto es polimorfismo sin herencia: la interfaz es el contrato, no hay clase abstracta común.

**Consigna:**

Interface `Canal`:
- `tipo: string` — propiedad (no método)
- `enviar(destinatario: string, mensaje: string): string` — retorna confirmación

Clases que implementan `Canal`:
- `CanalEmail`: `constructor(private dominio: string)`, tipo = `"email"`, `enviar` retorna `"[EMAIL] ${destinatario}@${dominio}: ${mensaje}"`
- `CanalSMS`: `constructor(private prefijo: string)`, tipo = `"sms"`, `enviar` retorna `"[SMS] ${prefijo}-${destinatario}: ${mensaje}"`
- `CanalPush`: sin constructor especial, tipo = `"push"`, `enviar` retorna `"[PUSH] → ${destinatario}: ${mensaje}"`

Clase `SistemaNotificaciones` (composición — tiene canales, no los hereda):
- `constructor(private canales: Canal[])`
- `notificarTodos(destinatario: string, mensaje: string): string[]` — envía por todos los canales y retorna array de confirmaciones
- `agregarCanal(canal: Canal): void`
- `cantidadCanales(): number`

**Ejemplos:**
```typescript
const sistema = new SistemaNotificaciones([
  new CanalEmail("untdf.edu.ar"),
  new CanalSMS("+54911"),
]);

sistema.notificarTodos("matias", "Nuevo TP disponible");
// [
//   "[EMAIL] matias@untdf.edu.ar: Nuevo TP disponible",
//   "[SMS] +54911-matias: Nuevo TP disponible"
// ]

sistema.agregarCanal(new CanalPush());
sistema.cantidadCanales(); // 3
```

**Pista:**  
`SistemaNotificaciones` no extiende ninguna clase ni implementa ninguna interfaz — es una clase concreta que *tiene* canales. Esto es composición pura. Si mañana se agrega `CanalWhatsApp`, basta con crear la clase e instanciarla; el sistema no cambia.

---

## SECCIÓN D — Integración

---

### Ejercicio 11 — Reporte de empleados (7 pts)

**Concepto:** integración de herencia + polimorfismo + Template Method para generación de reportes.

**Referencia:** filminas F-30 y F-32 — *"Template Method"* y *"Los 4 pilares en un solo fragmento"*

**Contexto:**  
El patrón Template Method en su forma más útil: la clase base define el formato del reporte (el esqueleto), y cada subclase solo define los datos que varían. El cliente usa la clase base `GeneradorReporte` sin saber qué tipo concreto recibe.

**Consigna:**  
Usando la jerarquía de empleados del Ejercicio 6, implementá:

Clase abstracta `GeneradorReporte`:
- `abstract titulo(): string`
- `abstract filas(empleados: Empleado[]): string[]`
- `generar(empleados: Empleado[]): string` — **Template Method** que retorna:
  ```
  === {titulo()} ===
  {cada fila unida con \n}
  Total empleados: {empleados.length}
  Masa salarial: ${suma de calcularSueldo()}
  ```

Subclase `ReporteSimple extends GeneradorReporte`:
- `titulo()`: `"Reporte de Empleados"`
- `filas(empleados)`: cada fila es `"- ${emp.nombre}: $${emp.calcularSueldo()}"`

Subclase `ReporteDetallado extends GeneradorReporte`:
- `titulo()`: `"Reporte Detallado"`
- `filas(empleados)`: cada fila es el resultado de `emp.presentarse()`

**Ejemplo:**
```typescript
const equipo: Empleado[] = [
  new Empleado("Carlos", 1000),
  new EmpleadoFullTime("Ana", 1000, 2400),
  new Gerente("Luis", 1000, 2400, 20),
];

const simple = new ReporteSimple();
console.log(simple.generar(equipo));
// === Reporte de Empleados ===
// - Carlos: $1000
// - Ana: $1200
// - Luis: $1440
// Total empleados: 3
// Masa salarial: $3640
```

**Pista:**  
`generar()` no debe saber si es un `ReporteSimple` o `ReporteDetallado` — solo llama a `titulo()` y `filas()` que son abstractos. La suma salarial se calcula con `reduce`: `empleados.reduce((acc, e) => acc + e.calcularSueldo(), 0)`.

---

### Ejercicio 12 — Patrón Strategy (8 pts)

**Concepto:** patrón Strategy — encapsular algoritmos intercambiables detrás de una interfaz.

**Referencia:** filmina F-30 — *"Patrones GoF — Strategy"*

**Contexto:**  
El patrón Strategy permite cambiar el algoritmo usado por un objeto en runtime sin modificar el objeto. En lugar de `if/else` o `switch` para elegir entre algoritmos, cada algoritmo se encapsula en un objeto que implementa una interfaz común. El cliente simplemente recibe el objeto strategy sin saber cuál es.

**Consigna:**

Interface `EstrategiaDescuento`:
- `calcularDescuento(precio: number): number` — retorna el monto del descuento (no el precio final)
- `descripcion(): string`

Clases de estrategias:
- `SinDescuento`: descuento = 0, descripción = `"Sin descuento"`
- `DescuentoPorcentual`: `constructor(private porcentaje: number)`, descuento = `precio * porcentaje / 100`, descripción = `"Descuento ${porcentaje}%"`
- `DescuentoFijo`: `constructor(private monto: number)`, descuento = `Math.min(monto, precio)` (no puede superar el precio), descripción = `"Descuento fijo $${monto}"`
- `Descuento2x1`: descuento = `Math.floor(cantidad / 2) * precio` donde `cantidad` se pasa en el constructor `constructor(private cantidad: number)`, descripción = `"2x1 (${cantidad} unidades)"`

Clase `Carrito`:
- `constructor(private estrategia: EstrategiaDescuento)`
- `private items: {nombre: string, precio: number}[] = []`
- `agregar(nombre: string, precio: number): void`
- `subtotal(): number` — suma de precios sin descuento
- `descuento(): number` — aplica `estrategia.calcularDescuento(subtotal())`
- `total(): number` — `subtotal() - descuento()`
- `cambiarEstrategia(nueva: EstrategiaDescuento): void` — cambia la estrategia en runtime
- `resumen(): string` — retorna `"Subtotal: $X | Descuento (${estrategia.descripcion()}): -$Y | Total: $Z"`

**Ejemplo:**
```typescript
const carrito = new Carrito(new SinDescuento());
carrito.agregar("Mouse", 25);
carrito.agregar("Teclado", 50);
carrito.subtotal();  // 75
carrito.total();     // 75
carrito.resumen();   // "Subtotal: $75 | Descuento (Sin descuento): -$0 | Total: $75"

carrito.cambiarEstrategia(new DescuentoPorcentual(10));
carrito.total();     // 67.5
carrito.resumen();   // "Subtotal: $75 | Descuento (Descuento 10%): -$7.5 | Total: $67.5"

carrito.cambiarEstrategia(new DescuentoFijo(20));
carrito.total();     // 55
```

**Pista:**  
El poder del patrón Strategy es `cambiarEstrategia()`: el carrito no cambia, cambia solo el objeto que calcula el descuento. Esto es polimorfismo en runtime — el carrito llama a `estrategia.calcularDescuento()` y obtiene el resultado correcto sin saber qué estrategia concreta tiene.

---

## Tabla de notas

| Ejercicio | Tema | Pts |
|-----------|------|-----|
| 1 | CuentaBancaria — encapsulamiento + validación | 8 |
| 2 | Temperatura — readonly + factory methods | 8 |
| 3 | CuentaConHistorial — herencia + colección encapsulada | 9 |
| 4 | Formas — clase abstracta + polimorfismo | 8 |
| 5 | Triángulo — Open/Closed Principle | 8 |
| 6 | Empleados — herencia multi-nivel + super | 9 |
| 7 | Animal — Template Method | 10 |
| 8 | Producto — interfaces múltiples | 8 |
| 9 | Pila/Cola — composición sobre herencia | 8 |
| 10 | Notificaciones — composición + interfaces | 9 |
| 11 | Reporte — Template Method integrado | 7 |
| 12 | Carrito — patrón Strategy | 8 |
| **Total** | | **100** |
