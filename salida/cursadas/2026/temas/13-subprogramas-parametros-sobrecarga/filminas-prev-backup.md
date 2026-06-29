# Filminas - Clase 13A - Subprogramas, parámetros y sobrecarga

> Duración: 120 minutos
> Hilo conductor: del contrato fuente al protocolo efectivo de ejecución
> Fuente principal: Sebesta, capítulos 9 y 10
> Complemento: Gabbrielli y Martini, capítulo 5
> Lenguaje principal: TypeScript | Contraste: Go, Rust, Kotlin y Swift
> Enfoque actualizado: ownership, efectos, dispatch, ABI y async
> Documentación contemporánea: Rust Book, Kotlin Docs y Swift Language Guide

---

### [F-00] Portada 13A

@tipo: portada

# CLASE 13A

## Subprogramas: del contrato a la ejecución

- Contrato observable de un subprograma.
- Comunicación entre llamador y llamado.
- Decisiones que controlan mutación, ownership y efectos.
- Implementación de llamadas síncronas y asíncronas.

---

### [F-01] Un subprograma abstrae una acción

@tipo: concepto-mixto

# Un subprograma permite razonar por contrato, no por instrucciones

- Tiene un punto de entrada y devuelve el control al llamador.
- Su encabezado establece qué datos recibe y qué resultado produce.
- El cuerpo queda oculto durante el uso: el cliente invoca una abstracción.
- Cada llamada crea una activación distinta del mismo código.

`[Sebesta, §9.1, pp. 389-394]`

```typescript
function distancia(x1: number, y1: number,
                   x2: number, y2: number): number {
  return Math.hypot(x2 - x1, y2 - y1);
}
```

---

### [F-02] La definición y la llamada cumplen roles distintos

@tipo: tabla-comparativa

# Definición y llamada forman un contrato

`[Sebesta, §9.1]`

| Elemento | En la definición | En la llamada |
|---|---|---|
| Nombre | Identifica el servicio | Selecciona el servicio |
| Parámetros | Formales: variables locales del llamado | Reales: valores o expresiones aportadas |
| Perfil | Número, orden y tipos de parámetros | Debe ser compatible con los argumentos |
| Protocolo | Perfil más tipo de retorno | Determina el tipo de la expresión resultante |
| Cuerpo | Implementa el servicio | Permanece oculto al cliente |

---

### [F-03] Procedimiento y función expresan intenciones diferentes

@tipo: tabla-comparativa

# El retorno distingue cálculo de efecto

`[Sebesta, §9.1 · Gabbrielli/Martini, cap. 5]`

| Decisión | Procedimiento | Función |
|---|---|---|
| Intención principal | Cambiar el estado o producir un efecto | Calcular un valor |
| Resultado | Implícito en el estado modificado | Explícito mediante retorno |
| Composición | Se encadena por secuencia | Se compone dentro de expresiones |
| Contraste moderno | Kotlin usa `Unit` para efectos | Rust exige declarar el tipo retornado cuando no es `()` |
| Riesgo | Efectos difíciles de rastrear | Dependencia de entradas y entorno |

---

### [F-04] Perfil y protocolo permiten verificar llamadas

@tipo: concepto-mixto

# El protocolo convierte una función en un valor tipado

- El **perfil** incluye cantidad, orden y tipos de los parámetros.
- El **protocolo** agrega el tipo de retorno.
- El chequeo estático rechaza llamadas incompatibles antes de ejecutar.
- El mismo concepto reaparece en sobrecarga y funciones de orden superior.

`[Sebesta, §9.1, pp. 392-394]`

```typescript
type Distancia = (
  x1: number, y1: number,
  x2: number, y2: number
) => number;

const euclidea: Distancia = (x1, y1, x2, y2) =>
  Math.hypot(x2 - x1, y2 - y1);

const resultado = euclidea(0, 0, 3, 4); // 5
```

---

### [F-05] El contrato permite validar sin leer el cuerpo

@tipo: concepto-abstracto

# El cliente razona con información visible

- El perfil de `distancia` exige cuatro argumentos numéricos.
- El protocolo agrega que el resultado también es numérico.
- TypeScript rechaza cantidad y tipos incompatibles antes de ejecutar.
- El algoritmo, sus variables locales y su costo permanecen ocultos.
- El contrato reduce conocimiento necesario, pero no describe toda la semántica.

---

### [F-06] El contrato moderno incluye efectos observables

@tipo: tabla-comparativa

# La firma tipada no siempre cuenta toda la historia

`[Sebesta, §§9.1 y 9.8 · Gabbrielli/Martini, cap. 5]`

| Efecto | Evidencia en el contrato | Consecuencia para el llamador |
|---|---|---|
| Retorno normal | Tipo de retorno | Composición directa |
| Mutación | `&mut`, `inout`, objeto mutable | Estado compartido observable |
| Falla | `Result<T,E>`, excepción documentada | Flujo alternativo |
| Suspensión | `async`, `suspend` | Continuación diferida |
| Cancelación | Señal o contexto | Terminación cooperativa |

---

### [F-07] Los efectos exigen permisos sobre los datos

@tipo: tabla-comparativa

# El contrato debe limitar qué puede hacer el subprograma

| Intención | Permiso mínimo | Evidencia moderna |
|---|---|---|
| Consultar | Lectura compartida | Referencia inmutable, `readonly` |
| Modificar | Acceso mutable exclusivo | `&mut`, `inout` |
| Consumir | Transferencia de ownership | Parámetro por valor no copiable |
| Producir | Retorno tipado | Valor, `Result` o promesa |

> Esta relación entre intención y permiso conduce a los modos y mecanismos de pasaje.

---

### [F-08] Los parámetros describen flujo de información

@tipo: concepto-abstracto

# Antes del mecanismo, importa la dirección del flujo

- Modo **in**: el llamado recibe información del llamador.
- Modo **out**: el llamado produce información para el llamador.
- Modo **inout**: la información circula en ambas direcciones.
- La elección debería minimizar acceso innecesario a datos externos.
- Luego se elige un mecanismo que implemente ese modo.

`[Sebesta, §9.5 · Gabbrielli/Martini, cap. 5]`

---

### [F-09] Los mecanismos de pasaje tienen costos y riesgos distintos

@tipo: tabla-comparativa

# No existe un mecanismo óptimo para todos los casos

`[Sebesta, §9.5, pp. 403-420]`

| Mecanismo | Implementa | Ventaja | Riesgo o costo |
|---|---|---|---|
| Valor | in | Aísla al llamador | Copiar objetos grandes |
| Resultado | out | Expresa salida | Colisión al copiar resultados |
| Valor-resultado | inout | Evita aliasing durante la llamada | Orden de copia al retornar |
| Referencia | inout | Evita copias grandes | Aliasing y efectos laterales |
| Nombre | inout | Reevalúa expresiones | Semántica difícil de predecir |

---

### [F-10] Go muestra el aislamiento de pass-by-value

@tipo: concepto-mixto

# Modificar el parámetro formal no modifica el argumento

- La expresión real se evalúa antes de entrar.
- Su valor inicializa una nueva variable local.
- La asignación afecta solo esa copia.
- El retorno explícito comunica el resultado.

`[Sebesta, §9.5.2.1 · Gabbrielli/Martini, cap. 5]`

```go
func incrementar(n int) int {
    n = n + 1
    return n
}
edad := 20
siguiente := incrementar(edad) // edad sigue siendo 20
```

---

### [F-11] Rust restringe el aliasing mutable

@tipo: concepto-mixto

# Una referencia mutable exige acceso exclusivo

- El formal se vincula con la ubicación del argumento real.
- Asignar al formal modifica directamente el dato del llamador.
- Rust permite muchas referencias inmutables o una sola mutable.
- El borrow checker rechaza aliasing mutable antes de ejecutar.

`[Sebesta, §9.5.2.4, pp. 412-416]`

```rust
fn incrementar(n: &mut i32) {
    *n += 1;
}
let mut x = 10;
incrementar(&mut x);
// dos &mut x simultáneos serían rechazados
```

---

### [F-12] Swift hace explícita la mutación del argumento

@tipo: concepto-mixto

# `inout` distingue entrada mutable de retorno

- Los parámetros comunes son constantes dentro de la función.
- `inout` permite leer y escribir el argumento del llamador.
- La llamada usa `&` para hacer visible la posible mutación.
- Swift restringe accesos superpuestos al mismo almacenamiento.

`[Sebesta, §9.5.2.3, pp. 409-412]`

```swift
func avanzar(posicion: inout Int, pasos: Int) -> Bool {
    posicion += pasos
    return posicion >= 100
}
var posicion = 90
let final = avanzar(posicion: &posicion, pasos: 15)
```

---

### [F-13] Elegir un mecanismo exige balancear riesgos

@tipo: tabla-comparativa

# Una matriz grande muestra el compromiso entre copia y aliasing

| Mecanismo | Costo principal | Riesgo principal | Lectura del contrato |
|---|---|---|---|
| Valor | Copiar toda la matriz | Consumo de memoria | Aislamiento total |
| Referencia mutable | Sin copia inicial | Aliasing y efectos laterales | Mutación compartida |
| Valor-resultado | Copia al entrar y salir | Orden de copia final | Cambio diferido |
| Referencia inmutable + resultado | Copia solo del resultado | Construcción de nueva matriz | Flujo explícito |

---

### [F-14] TypeScript siempre copia el valor del argumento

@tipo: concepto-mixto

# En objetos, el valor copiado es una referencia compartida

- Reasignar el parámetro no cambia la variable del llamador.
- Mutar el objeto alcanzado sí es observable desde afuera.
- Esta semántica suele llamarse **pass-by-sharing**.
- No equivale a `inout` de Swift, porque no permite reasignar la variable externa.

```typescript
function actualizar(p: { nombre: string }): void {
  p.nombre = "Lin";          // muta el objeto compartido
  p = { nombre: "Grace" };   // reasigna solo el formal
}
```

---

### [F-15] La mutabilidad define si compartir es peligroso

@tipo: tabla-comparativa

# Compartir referencias no implica necesariamente compartir cambios

| Estrategia | Qué recibe el llamado | Efecto observable |
|---|---|---|
| Objeto mutable | Referencia al mismo objeto | Puede modificar propiedades |
| `Readonly<T>` | Referencia con restricción estática | TypeScript impide mutación directa |
| Copia superficial | Nuevo contenedor, elementos compartidos | Aísla estructura, no objetos internos |
| Copia profunda | Nuevo grafo de objetos | Mayor aislamiento y costo |
| Valor de retorno | Resultado nuevo | Flujo explícito y fácil de probar |

---

### [F-16] Pass-by-sharing separa variable y objeto

@tipo: concepto-mixto

# La mutación compartida sobrevive; la reasignación local no

```typescript
const usuario = { nombre: "Lin", roles: ["lector"] };
function cambiar(u: typeof usuario): void {
  u.roles.push("editor");
  u = { nombre: "Otro", roles: [] };
}
cambiar(usuario);
```

- `usuario.nombre` permanece `"Lin"`.
- `usuario.roles` contiene `"lector"` y `"editor"`.
- `u.roles.push` muta el objeto compartido.
- Reasignar `u` cambia únicamente la variable formal.

---

### [F-17] Un callback es parte del contrato del llamador

@tipo: concepto-mixto

# Pasar comportamiento exige definir protocolo, efectos y frecuencia

- La firma establece entradas y retorno del callback.
- El contrato debe aclarar cuántas veces y cuándo será invocado.
- También importa si puede fallar, suspenderse o retenerse.
- Una callback retenida puede extender la vida de su entorno capturado.
- La closure ya fue estudiada; aquí importa su impacto contractual.

`[Sebesta, §9.6, pp. 420-425]`

```typescript
type Comparador<T> = (a: T, b: T) => number;
function ordenar<T>(xs: T[], comparar: Comparador<T>): T[] {
  return [...xs].sort(comparar);
}
```

---

### [F-18] Kotlin distingue callback síncrono y suspendible

@tipo: concepto-mixto

# `suspend` cambia qué implementaciones son compatibles

- `(T) -> R` debe completar antes de devolver el control.
- `suspend (T) -> R` puede suspender y reanudarse.
- El modificador comunica un efecto que el tipo de retorno no expresa solo.
- Un API debe elegir cuál de los dos protocolos acepta.

```kotlin
fun <T, R> transformar(xs: List<T>, f: (T) -> R): List<R>
suspend fun <T, R> transformarAsync(
    xs: List<T>, f: suspend (T) -> R
): List<R>
```

---

### [F-19] Una callback puede escapar de la llamada

@tipo: concepto-mixto

# Escapar cambia duración, ownership y manejo de errores

- Una callback no escapante se ejecuta durante la llamada.
- Una callback escapante se almacena y ejecuta más tarde.
- Swift exige marcar `@escaping` para volver visible esa diferencia.
- Retener callbacks puede crear ciclos de referencias y recursos vivos.

```swift
func registrar(_ handler: @escaping (Evento) -> Void) {
    handlers.append(handler)
}
```

---

### [F-20] Un nombre puede resolverse en momentos diferentes

@tipo: tabla-comparativa

# Resolución estática, despacho dinámico e indirección no son equivalentes

| Mecanismo | Cuándo se selecciona | Información usada | Costo principal |
|---|---|---|---|
| Sobrecarga | Compilación | Tipos y argumentos | Complejidad de resolución |
| Despacho virtual | Ejecución | Tipo dinámico del receptor | Indirección |
| Callback | Ejecución | Valor función recibido | Indirección y captura |
| Trait/genérico | Compilación o ejecución | Estrategia del lenguaje | Código generado o tabla dinámica |

---

### [F-21] Kotlin resuelve sobrecargas entre cuerpos distintos

@tipo: concepto-mixto

# La firma selecciona una implementación en compilación

- Cada sobrecarga tiene su propio cuerpo.
- El compilador busca la mejor coincidencia según los argumentos.
- Conversiones implícitas y parámetros por defecto pueden crear ambigüedad.
- Si el algoritmo es uniforme, una plantilla evita duplicación.

`[Sebesta, §9.9, pp. 429-432]`

```kotlin
fun area(radio: Double): Double = Math.PI * radio * radio
fun area(base: Double, altura: Double): Double = base * altura

area(3.0)       // círculo
area(3.0, 4.0)  // rectángulo
```

---

### [F-22] Rust separa dispatch estático y dinámico

@tipo: concepto-mixto

# `impl Trait` y `dyn Trait` eligen costos distintos

- `impl Trait` permite especialización estática y optimización.
- `dyn Trait` acepta implementaciones heterogéneas mediante indirección.
- Ambos expresan capacidades, pero producen representaciones distintas.
- La elección afecta tamaño de código, rendimiento y flexibilidad.

`[Sebesta, §§9.9-9.10, reinterpretación contemporánea]`

```rust
fn ejecutar_estatico(t: &impl Tarea) { t.ejecutar(); }
fn ejecutar_dinamico(t: &dyn Tarea) { t.ejecutar(); }
```

---

### [F-23] La implementación genérica tiene una estrategia de runtime

@tipo: tabla-comparativa

# Monomorfización y borrado intercambian rendimiento por tamaño

| Estrategia | Idea | Ventaja | Costo |
|---|---|---|---|
| Monomorfización | Generar código por instanciación | Optimización específica | Mayor binario |
| Borrado de tipos | Compartir implementación runtime | Menor duplicación | Menor información runtime |
| Reificación parcial | Conservar ciertos tipos | Inspección selectiva | Reglas más complejas |

`[Sebesta, §9.10 · Gabbrielli/Martini, discusión de implementación de polimorfismo]`

---

### [F-24] La API debe expresar la variación correcta

@tipo: tabla-comparativa

# Elegir dispatch evita contratos engañosos

| Herramienta | Variación modelada | Ejemplo apropiado | Riesgo de mal uso |
|---|---|---|---|
| Sobrecarga | Protocolos estáticos distintos | `parsear(string)` y `parsear(bytes)` | Ambigüedad |
| Unión sellada | Conjunto cerrado de casos | Estado de una operación | Acoplar todos los casos |
| Genérico/trait | Capacidad uniforme | Algoritmo sobre ordenables | Restricción excesiva |
| Interfaz dinámica | Implementaciones abiertas | Plugins | Fallas tardías de integración |

---

### [F-25] El activation record materializa una llamada

@tipo: tabla

# Cada activación necesita estado propio

`[Sebesta, §10.3, pp. 420-428]`

| Componente | Función durante la llamada |
|---|---|
| Parámetros | Comunican datos desde el llamador |
| Variables locales | Conservan el estado privado de esa activación |
| Dirección de retorno | Indica dónde continuar al terminar |
| Dynamic link | Apunta al activation record del llamador |
| Valor de retorno | Comunica el resultado |
| Static link, si aplica | Permite acceder a variables no locales léxicas |

---

### [F-26] Call y return administran el stack

@tipo: tabla

# Llamar suspende un contexto; retornar lo restaura

| Momento | Acción |
|---|---|
| 1. Preparar llamada | Evaluar argumentos y establecer parámetros |
| 2. Crear activación | Reservar activation record |
| 3. Transferir control | Guardar retorno y saltar al punto de entrada |
| 4. Ejecutar | Usar parámetros, locales y enlaces |
| 5. Retornar | Producir resultado y restaurar al llamador |
| 6. Liberar | Retirar el activation record terminado |

`[Sebesta, §§10.1-10.3]`

---

### [F-27] La cadena dinámica reconstruye quién llamó a quién

@tipo: concepto-abstracto

# Dynamic link y static link responden preguntas diferentes

- El **dynamic link** apunta al activation record del llamador.
- Permite restaurar el stack al retornar.
- El **static link** apunta hacia un ancestro léxico.
- Permite buscar variables no locales con alcance estático.
- El orden de llamadas y la estructura del programa no siempre coinciden.

`[Sebesta, §10.4 · Gabbrielli/Martini, §5.3.3]`

---

### [F-28] `async` extiende el modelo de activación

@tipo: concepto-mixto

# Una suspensión conserva estado sin mantener el stack síncrono completo

- Antes del primer `await`, la función ejecuta como una llamada ordinaria.
- Al suspenderse, debe conservar parámetros, locales y punto de continuación.
- El compilador/runtime materializa una máquina de estados reanudable.
- Los stack traces async reconstruyen una cadena lógica, no siempre el stack físico original.

`[Sebesta, cap. 10, extensión contemporánea sobre implementación de llamadas]`

```typescript
async function cargar(id: string): Promise<Usuario> {
  const respuesta = await fetch(`/usuarios/${id}`);
  return respuesta.json() as Promise<Usuario>;
}
```

---

### [F-29] Las decisiones de diseño están conectadas

@tipo: tabla

# Del contrato visible al mecanismo de ejecución

| Pregunta | Decisión | Consecuencia |
|---|---|---|
| ¿Qué acepta y retorna? | Perfil y protocolo | Verificación de llamadas |
| ¿Cómo circulan datos? | Modos y mecanismos de pasaje | Copias, aliasing y efectos |
| ¿Qué efectos produce? | Mutación, falla, suspensión | Obligaciones del llamador |
| ¿Puede retener callbacks? | Escapante o no escapante | Duración y recursos |
| ¿Cómo selecciona implementación? | Sobrecarga, trait o dispatch | Costo y extensibilidad |
| ¿Cómo se ejecuta? | Frames, continuaciones y ABI | Call, return y depuración |

---

### [F-30] Cierre 13A

@tipo: cierre

# Un subprograma es simultáneamente contrato, abstracción y activación

- El contrato permite usarlo.
- Los mecanismos de pasaje determinan cómo comparte información.
- El entorno determina qué nombres puede observar.
- El activation record permite ejecutarlo y volver.

## Próxima clase: del subprograma aislado a fronteras modulares versionadas
