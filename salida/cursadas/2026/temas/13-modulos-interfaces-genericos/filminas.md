# Filminas — Clase 13B: Subprogramas: del contrato a la ejecución

> **Tema (topic.yaml):** Módulos, Interfaces y Genéricos
> **Contenido real:** Subprogramas: del contrato a la ejecución
> **Duración:** 120 minutos | **Lenguaje principal:** TypeScript
> **Contrastes:** Go, Rust, Swift, Kotlin
> **Fecha de generación:** 2026-06-28

---

## PORTADA

---

### [F-00] Subprogramas: del contrato a la ejecución

@tipo: portada
@layout: portada
@imagen: background
@prompt-imagen: Dos formas geométricas rectangulares de bordo y gris oscuro, una a la izquierda y otra a la derecha, conectadas por una flecha curva bidireccional que cruza el centro. La forma izquierda es sólida; la derecha es un contorno. Flat design, bordo y gris oscuro, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Subprogramas: del contrato a la ejecución

Clase 13B — Laboratorio de Programación y Lenguajes 2026

---

## BLOQUE A — El subprograma como abstracción de acción

---

### [F-01] Un subprograma abstrae una acción

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: content
@prompt-imagen: Una caja sólida de bordo en el centro con una flecha horizontal que entra por la izquierda y sale por la derecha, retornando hacia arriba con una curva. La caja tiene un borde grueso que oculta su interior. Flat design, bordo y gris oscuro, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Un subprograma abstrae una acción

- Permite razonar por **contrato**, no por instrucciones
- Tiene un **punto de entrada** único y devuelve el control al llamador
- Su encabezado establece qué datos recibe y qué resultado produce
- El cuerpo queda **oculto** durante el uso: el cliente invoca una abstracción
- Cada llamada crea una **activación distinta** del mismo código

---

### [F-02] Definición y llamada forman un contrato

@tipo: tabla-mixta
@layout: tabla-mixta
@imagen: none

# Definición y llamada cumplen roles distintos

## La función distancia

```ts
function distancia(x1: number, y1: number,
                   x2: number, y2: number): number {
  return Math.hypot(x2 - x1, y2 - y1);
}
```

## Elemento: definición vs. llamada

| Elemento | En la definición | En la llamada |
|----------|-------------------|---------------|
| Nombre | Identifica el servicio | Selecciona el servicio |
| Parámetros | Formales: variables locales del llamado | Reales: valores o expresiones aportadas |
| Perfil | Número, orden y tipos de parámetros | Debe ser compatible con los argumentos |
| Protocolo | Perfil más tipo de retorno | Determina el tipo de la expresión resultante |
| Cuerpo | Implementa el servicio | Permanece oculto al cliente |

---

### [F-03] Procedimiento vs. función

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# Procedimiento y función expresan intenciones diferentes

## El retorno distingue cálculo de efecto

| Decisión | Procedimiento | Función |
|-----------|---------------|---------|
| Intención principal | Cambiar el estado o producir un efecto | Calcular un valor |
| Resultado | Implícito en el estado modificado | Explícito mediante retorno |
| Composición | Se encadena por secuencia | Se compone dentro de expresiones |
| Contraste moderno | Kotlin usa `Unit` para efectos | Rust exige declarar el tipo retornado cuando no es `()` |
| Riesgo | Efectos difíciles de rastrear | Dependencia de entradas y entorno |

---

### [F-04] Perfil y protocolo: verificar sin leer el cuerpo

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# El protocolo convierte una función en un valor tipado

## El contrato permite validar sin leer el cuerpo

- El **perfil** incluye cantidad, orden y tipos de los parámetros
- El **protocolo** agrega el tipo de retorno
- El chequeo estático rechaza llamadas incompatibles antes de ejecutar
- El mismo concepto reaparece en sobrecarga y funciones de orden superior

```ts
type Distancia = (
  x1: number, y1: number,
  x2: number, y2: number
) => number;

const euclidea: Distancia = (x1, y1, x2, y2) =>
  Math.hypot(x2 - x1, y2 - y1);

const resultado = euclidea(0, 0, 3, 4); // 5
```

---

## BLOQUE B — Parámetros: modos, permisos y efectos

---

### [F-05] La dirección del flujo: in, out, inout

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: content
@prompt-imagen: Tres flechas horizontales de bordo en fila: la primera apunta de izquierda a derecha, la segunda de derecha a izquierda, la tercera es bidireccional con cabezas en ambos extremos. Cada flecha tiene un círculo gris oscuro en el extremo de origen. Flat design, bordo y gris oscuro, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Los parámetros describen flujo de información

## Antes del mecanismo, importa la dirección del flujo

- **Modo in:** el llamado recibe información del llamador
- **Modo out:** el llamado produce información para el llamador
- **Modo inout:** la información circula en ambas direcciones
- La elección debería minimizar acceso innecesario a datos externos
- Luego se elige un mecanismo que implemente ese modo

---

### [F-06] Intención y permiso mínimo

@tipo: tabla
@layout: tabla
@imagen: none

# Los efectos exigen permisos sobre los datos

## El contrato debe limitar qué puede hacer el subprograma

| Intención | Permiso mínimo | Evidencia moderna |
|-----------|----------------|-------------------|
| Consultar | Lectura compartida | Referencia inmutable, `readonly` |
| Modificar | Acceso mutable exclusivo | `&mut`, `inout` |
| Consumir | Transferencia de ownership | Parámetro por valor no copiable |
| Producir | Retorno tipado | Valor, `Result` o promesa |

---

### [F-07] Efectos observables en el contrato moderno

@tipo: tabla
@layout: tabla
@imagen: none

# La firma tipada no siempre cuenta toda la historia

## El contrato moderno incluye efectos observables

| Efecto | Evidencia en el contrato | Consecuencia para el llamador |
|--------|--------------------------|-------------------------------|
| Retorno normal | Tipo de retorno | Composición directa |
| Mutación | `&mut`, `inout`, objeto mutable | Estado compartido observable |
| Falla | `Result<T,E>`, excepción documentada | Flujo alternativo |
| Suspensión | `async`, `suspend` | Continuación diferida |
| Cancelación | Señal o contexto | Terminación cooperativa |

---

### [F-08] Mecanismos de pasaje: tradeoffs

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# No existe un mecanismo óptimo para todos los casos

## Los mecanismos de pasaje tienen costos y riesgos distintos

| Mecanismo | Implementa | Ventaja | Riesgo o costo |
|-----------|------------|---------|----------------|
| Valor | in | Aísla al llamador | Copiar objetos grandes |
| Resultado | out | Expresa salida | Colisión al copiar resultados |
| Valor-resultado | inout | Evita aliasing durante la llamada | Orden de copia al retornar |
| Referencia | inout | Evita copias grandes | Aliasing y efectos laterales |
| Nombre | inout | Reevalúa expresiones | Semántica difícil de predecir |

---

## BLOQUE C — Tres lenguajes, tres decisiones de pasaje

---

### [F-09] Go — aislamiento de pass-by-value

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# Modificar el parámetro formal no modifica el argumento

## Pass-by-value en Go

- La expresión real se evalúa antes de entrar
- Su valor inicializa una nueva variable local
- La asignación afecta solo esa copia
- El retorno explícito comunica el resultado

```go
func incrementar(n int) int {
    n = n + 1
    return n
}
edad := 20
siguiente := incrementar(edad) // edad sigue siendo 20
```

---

### [F-10] Rust — aliasing mutable restringido

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# Una referencia mutable exige acceso exclusivo

## El borrow checker rechaza aliasing mutable antes de ejecutar

- El formal se vincula con la ubicación del argumento real
- Asignar al formal modifica directamente el dato del llamador
- Rust permite muchas referencias inmutables o una sola mutable
- Dos `&mut` simultáneos al mismo dato serían rechazados

```rust
fn incrementar(n: &mut i32) {
    *n += 1;
}
let mut x = 10;
incrementar(&mut x);
// sumar(n: &mut i32, m: &mut i32) exige dos referencias exclusivas
```

---

### [F-11] Swift — mutación explícita con inout

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# inout distingue entrada mutable de retorno

## La llamada usa & para hacer visible la posible mutación

- Los parámetros comunes son constantes dentro de la función
- `inout` permite leer y escribir el argumento del llamador
- Swift restringe accesos superpuestos al mismo almacenamiento

```swift
func avanzar(posicion: inout Int, pasos: Int) -> Bool {
    posicion += pasos
    return posicion >= 100
}
var posicion = 90
let final = avanzar(posicion: &posicion, pasos: 15)
```

---

## BLOQUE D — Compartir objetos

---

### [F-12] Pass-by-sharing: separar variable y objeto

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# La mutación compartida sobrevive; la reasignación local no

## Compartir referencias no implica necesariamente compartir cambios

```ts
const usuario = { nombre: "Matias", roles: ["lector"] };
function cambiar(u: typeof usuario): void {
  u.roles.push("editor");      // muta el objeto compartido
  u = { nombre: "Otro", roles: [] }; // reasigna solo la variable formal
}
cambiar(usuario);
// usuario.nombre permanece "Matias"
// usuario.roles contiene "lector" y "editor"
```

- `u.roles.push` muta el objeto compartido → sobrevive
- Reasignar `u` cambia únicamente la variable formal → no sobrevive

---

### [F-13] Una matriz grande: copia vs. aliasing

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# Elegir un mecanismo exige balancear riesgos

## Una matriz grande muestra el compromiso entre copia y aliasing

| Mecanismo | Costo principal | Riesgo principal | Lectura del contrato |
|-----------|-----------------|------------------|----------------------|
| Valor | Copiar toda la matriz | Consumo de memoria | Aislamiento total |
| Referencia mutable | Sin copia inicial | Aliasing y efectos laterales | Mutación compartida |
| Valor-resultado | Copia al entrar y salir | Orden de copia final | Cambio diferido |
| Referencia inmutable + resultado | Copia solo del resultado | Construcción de nueva matriz | Flujo explícito |

---

## BLOQUE E — Callbacks

---

### [F-14] Un callback es parte del contrato

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# Un callback es un subprograma recibido como parámetro

## Pasar comportamiento exige definir protocolo, efectos y frecuencia

- La firma establece entradas y retorno del callback
- El contrato debe aclarar cuántas veces y cuándo será invocado
- También importa si puede fallar, suspenderse o retenerse
- Una callback retenida puede extender la vida de su entorno capturado

```ts
type Comparador<T> = (a: T, b: T) => number;
function ordenar<T>(xs: T[], comparar: Comparador<T>): T[] {
  return [...xs].sort(comparar);
}
```

---

### [F-15] Síncrono, suspendible y escapante

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# Escapar cambia duración, ownership y manejo de errores

## Kotlin distingue callback síncrono y suspendible

```kotlin
fun <T, R> transformar(xs: List<T>, f: (T) -> R): List<R> {
    // f debe devolver R antes de continuar
    return xs.map { x -> f(x) }
}

suspend fun <T, R> transformarAsync(xs: List<T>, f: suspend (T) -> R): List<R> {
    // f puede pausar su ejecución sin bloquear el hilo
    val resultado = mutableListOf<R>()
    for (x in xs) { resultado.add(f(x)) }
    return resultado
}
```

## Swift marca @escaping para hacer visible el escape

```swift
var handlers: [(Evento) -> Void] = []
func registrar(_ handler: @escaping (Evento) -> Void) {
    handlers.append(handler)  // el callback sobrevive a la llamada
}
func emitir(_ evento: Evento) {
    for h in handlers { h(evento) }
}
```

- Un callback **no diferido** se ejecuta durante la llamada
- Un callback **diferido** se almacena y ejecuta más tarde
- Retener callbacks puede crear ciclos de referencias y recursos vivos

---

## BLOQUE F — Variación: sobrecarga, dispatch y trait

---

### [F-16] Herramientas para expresar variación

@tipo: tabla-comparativa
@layout: tabla-comparativa
@imagen: none

# El contrato debe expresar la variación correcta

## Elegir dispatch evita contratos engañosos

| Herramienta | Variación modelada | Ejemplo apropiado | Riesgo de mal uso |
|-------------|--------------------|--------------------|-------------------|
| Sobrecarga | Protocolos estáticos distintos | `parsear(string)` y `parsear(bytes)` | Ambigüedad |
| Unión sellada | Conjunto cerrado de casos | Estado de una operación | Acoplar todos los casos |
| Genérico/trait | Capacidad uniforme | Algoritmo sobre ordenables | Restricción excesiva |
| Interfaz dinámica | Implementaciones abiertas | Plugins | Fallas tardías de integración |

## Cuándo se selecciona la implementación

| Mecanismo | Cuándo se selecciona | Información usada | Costo principal |
|-----------|----------------------|-------------------|-----------------|
| Sobrecarga | Compilación | Tipos y argumentos | Complejidad de resolución |
| Despacho virtual | Ejecución | Tipo dinámico del receptor | Indirección |
| Callback | Ejecución | Valor función recibido | Indirección y captura |
| Trait/genérico | Compilación o ejecución | Estrategia del lenguaje | Código generado o tabla dinámica |

---

### [F-17] Kotlin — sobrecarga entre cuerpos distintos

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# La firma selecciona una implementación en compilación

## Cada sobrecarga tiene su propio cuerpo

- El compilador busca la mejor coincidencia según los argumentos
- Conversiones implícitas y parámetros por defecto pueden crear ambigüedad
- Si el algoritmo es uniforme, una plantilla evita duplicación

```kotlin
fun area(radio: Double): Double = Math.PI * radio * radio
fun area(base: Double, altura: Double): Double = base * altura

area(3.0)       // círculo
area(3.0, 4.0)  // rectángulo
```

---

### [F-18] Rust — impl Trait vs. dyn Trait

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# impl Trait y dyn Trait eligen costos distintos

## Un trait es una abstracción de comportamiento

- `impl Trait` permite especialización estática y optimización
- `dyn Trait` acepta implementaciones heterogéneas mediante indirección
- El compilador solo sabe que cumple el Trait, no cuál es
- La elección afecta tamaño de código, rendimiento y flexibilidad

```rust
trait Tarea {
    fn ejecutar(&self);
}
struct Email;
impl Tarea for Email {
    fn ejecutar(&self) { println!("Enviando email"); }
}

fn ejecutar_estatico(t: &impl Tarea) { t.ejecutar(); }
fn ejecutar_dinamico(t: &dyn Tarea) { t.ejecutar(); }
```

---

## BLOQUE G — Abstracción genérica

---

### [F-19] Abstracción genérica: costos de implementación

@tipo: tabla-mixta
@layout: tabla-mixta
@imagen: none

# Especializar o compartir código intercambia rendimiento, tamaño y flexibilidad

## Estrategias de abstracción genérica

| Estrategia | Idea | Ventaja | Costo |
|------------|------|---------|-------|
| Especialización por tipo | Generar código por instanciación | Optimización específica | Mayor binario |
| Implementación compartida | Compartir implementación runtime | Menor duplicación | Menor información runtime |
| Preservación selectiva | Conservar ciertos tipos | Inspección selectiva | Reglas más complejas |

## TypeScript: type erasure en runtime

```ts
// genérico: una sola definición sirve para distintos tipos
function identidad<T>(x: T): T { return x; }

const a = identidad<number>(10);
const b = identidad<string>("hola");
// en runtime no existe T — los tipos genéricos se borran

// preservación selectiva: pasar información explícitamente
function esTipo<T>(x: unknown, check: (v: unknown) => v is T): boolean {
  return check(x);
}
const esNumero = esTipo<number>(10, (v): v is number => typeof v === "number");
```

---

## BLOQUE H — Ejecución: activation records y async

---

### [F-20] El activation record materializa una llamada

@tipo: tabla
@layout: tabla
@imagen: none

# activation record = memoria de una activación

## Es la estructura que conserva el estado de una activación mientras la llamada está en ejecución

| Componente | Función durante la llamada |
|------------|---------------------------|
| Parámetros | Comunican datos desde el llamador |
| Variables locales | Conservan el estado privado de esa activación |
| Dirección de retorno | Indica dónde continuar al terminar |
| Dynamic link | Apunta al activation record del llamador — ¿quién me llamó? |
| Valor de retorno | Comunica el resultado |
| Static link, si aplica | Permite acceder a variables no locales léxicas — ¿dónde busco? |

---

### [F-21] Call y return: administrar el stack

@tipo: tabla-mixta
@layout: tabla-mixta
@imagen: none

# Llamar crea un nuevo contexto; retornar restaura el anterior

## Secuencia de una llamada

| Momento | Acción |
|---------|--------|
| 1. Preparar llamada | Evaluar argumentos y establecer parámetros |
| 2. Crear activación | Reservar activation record |
| 3. Transferir control | Guardar retorno y saltar al punto de entrada |
| 4. Ejecutar | Usar parámetros, locales y enlaces |
| 5. Retornar | Producir resultado y restaurar al llamador |
| 6. Liberar | Retirar el activation record terminado |

## Ejemplo: AR de `sumar(2, 3)`

```kotlin
fun sumar(a: Int, b: Int): Int {
    val z = a + b
    return z
}
sumar(2, 3)
```

```
Activation Record(sumar)
------------------------
a = 2
b = 3
z = ?
ret addr -> main
dynamic link -> AR(main)
```

---

### [F-22] async extiende el modelo de ejecución

@tipo: concepto-mixto
@layout: concepto-mixto
@imagen: none

# Una suspensión conserva estado sin mantener el stack síncrono completo

## El compilador materializa una máquina de estados reanudable

- Antes del primer `await`, la función ejecuta como una llamada ordinaria
- Al suspenderse, debe conservar parámetros, locales y punto de continuación
- Los stack traces async reconstruyen una cadena lógica, no siempre el stack físico original

```ts
async function cargar(id: string): Promise<Usuario> {
  const respuesta = await fetch(`/usuarios/${id}`);
  return respuesta.json() as Promise<Usuario>;
}
```

---

### [F-23] Dynamic link vs. static link

@tipo: concepto-abstracto
@layout: concepto-abstracto
@imagen: content
@prompt-imagen: Dos pilas verticales de rectángulos grises apilados, una a la izquierda y otra a la derecha. En la pila izquierda, una flecha bordo vertical apunta al rectángulo inmediatamente abajo. En la pila derecha, una flecha bordo diagonal apunta a un rectángulo más abajo saltando varios niveles. Flat design, bordo y gris oscuro, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Dynamic link y static link responden preguntas diferentes

## El orden de llamadas y la estructura del programa no siempre coinciden

- **Dynamic link** apunta al activation record del llamador
  - Permite restaurar el stack al retornar
  - Responde: ¿quién me llamó?
- **Static link** apunta hacia un ancestro léxico
  - Permite buscar variables no locales con alcance estático
  - Responde: ¿dónde busco variables no locales?

---

## BLOQUE I — Cierre

---

### [F-24] Las decisiones de diseño están conectadas

@tipo: cierre
@layout: cierre
@imagen: background
@prompt-imagen: Seis círculos pequeños de bordo dispuestos en hexágono en el centro, conectados por líneas grises que forman una red completa donde cada círculo se conecta con todos los demás. Un círculo central más grande de gris oscuro une toda la composición. Flat design, bordo y gris oscuro, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Del contrato visible al mecanismo de ejecución

## Las decisiones de diseño están conectadas

| Pregunta | Decisión | Consecuencia |
|----------|----------|--------------|
| ¿Qué acepta y retorna? | Perfil y protocolo | Verificación de llamadas |
| ¿Cómo circulan datos? | Modos y mecanismos de pasaje | Copias, aliasing y efectos |
| ¿Qué efectos produce? | Mutación, falla, suspensión | Obligaciones del llamador |
| ¿Puede retener callbacks? | Escapante o no escapante | Duración y recursos |
| ¿Cómo selecciona implementación? | Sobrecarga, trait o dispatch | Costo y extensibilidad |
| ¿Cómo se ejecuta? | Frames, continuaciones y ABI | Call, return y depuración |
