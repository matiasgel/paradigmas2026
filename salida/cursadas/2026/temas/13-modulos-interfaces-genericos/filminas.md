# Filminas - Clase 13B - ADTs, módulos e interfaces

> Duración: 120 minutos
> Hilo conductor: de una especificación observable a una unidad modular
> Fuentes: Sebesta, capítulos 11 y 12; Louden/Lambert, capítulo 11; Gabbrielli/Martini, capítulo 9

---

### [F-00] Portada 13B

@tipo: portada

# CLASE 13B

## ADTs y módulos: organizar abstracciones que pueden cambiar

- ¿Cómo se especifica un tipo sin revelar su representación?
- ¿Qué debe garantizar una interfaz?
- ¿Cómo escala la abstracción desde un tipo hacia un módulo?
- ¿Qué permite compilar y evolucionar partes por separado?

---

### [F-01] La abstracción de datos separa uso y representación

@tipo: concepto-abstracto

# Un ADT se define por valores y operaciones observables

- El cliente conoce qué valores conceptuales existen.
- Solo accede mediante operaciones definidas por el tipo.
- La representación interna permanece oculta.
- Las operaciones preservan las invariantes.
- Dos implementaciones equivalentes pueden representar los datos distinto.

`[Sebesta, §11.1 · Gabbrielli/Martini, cap. 9]`

---

### [F-02] Una Stack no es simplemente un array

@tipo: tabla-comparativa

# La abstracción limita operaciones para preservar significado

| Pregunta | Array | Stack |
|---|---|---|
| Acceso permitido | Cualquier posición | Solo el tope |
| Inserción | En múltiples posiciones | `push` en el tope |
| Eliminación | Por índice o criterio | `pop` del tope |
| Regla observable | Secuencia indexada | LIFO |
| Representación posible | Celdas contiguas | Array, lista enlazada u otra |

`[Louden/Lambert, §11.1]`

---

### [F-03] La especificación algebraica describe comportamiento

@tipo: concepto-abstracto

# Las ecuaciones definen qué debe cumplir cualquier implementación

- `create` construye una Stack vacía.
- `push(s, x)` construye una Stack con `x` en el tope.
- `top(push(s, x)) = x`.
- `pop(push(s, x)) = s`.
- Las ecuaciones hablan de comportamiento, no de arrays ni nodos.

`[Louden/Lambert, §11.1, pp. 494-498]`

---

### [F-04] Constructores, observadores y transformadores cumplen roles

@tipo: tabla

# Clasificar operaciones revela el contrato del ADT

| Rol | Operación de Stack | Qué aporta |
|---|---|---|
| Constructor base | `create()` | Produce el valor inicial |
| Constructor no base | `push(s, x)` | Produce una nueva configuración |
| Observador | `top(s)`, `isEmpty(s)` | Informa sin cambiar el valor conceptual |
| Transformador | `pop(s)` | Produce o establece otro estado |
| Condición de error | `top(create())` | Define comportamiento fuera del dominio válido |

---

### [F-05] Actividad: especificar antes de implementar

@tipo: socratica

# Diseñen el contrato de una Queue

- Clasifiquen `create`, `enqueue`, `front`, `dequeue` e `isEmpty`.
- Escriban dos ecuaciones observables.
- Definan qué ocurre al consultar una Queue vacía.
- Eviten mencionar arrays, índices o nodos.

---

### [F-06] Encapsulación e information hiding no son sinónimos

@tipo: tabla-comparativa

# Agrupar ayuda; ocultar decisiones permite cambiar

| Concepto | Pregunta que responde | Ejemplo |
|---|---|---|
| Encapsulación | ¿Qué datos y operaciones forman una unidad? | Clase `Stack<T>` |
| Information hiding | ¿Qué decisiones pueden cambiar sin afectar clientes? | Array o lista enlazada |
| Interfaz | ¿Qué puede observar y solicitar el cliente? | `push`, `pop`, `top` |
| Invariante | ¿Qué debe permanecer cierto? | Solo se elimina el último agregado |

`[Sebesta, §§11.1-11.3 · Gabbrielli/Martini, cap. 9]`

---

### [F-07] La interfaz debe expresar semántica, no conveniencia

@tipo: concepto-mixto

# Una operación pública amplía para siempre lo que el cliente puede asumir

- `push`, `pop` y `peek` preservan la semántica LIFO.
- `at(index)` permite tratar la Stack como un array.
- `toArray()` puede filtrar detalles o exponerlos, según su contrato.
- Una interfaz mínima reduce acoplamiento y mantiene opciones abiertas.

```typescript
export interface Stack<T> {
  push(value: T): void;
  pop(): T | undefined;
  peek(): T | undefined;
  readonly size: number;
}
```

---

### [F-08] La representación debe quedar detrás de las operaciones

@tipo: concepto-mixto

# `private` impide accesos que romperían la invariante

- El cliente no puede insertar debajo del tope.
- Toda modificación pasa por operaciones controladas.
- La clase puede cambiar su representación interna.
- Ocultar datos no alcanza: las operaciones públicas también deben ser cuidadosas.

```typescript
class ArrayStack<T> implements Stack<T> {
  private data: T[] = [];
  push(x: T): void { this.data.push(x); }
  pop(): T | undefined { return this.data.pop(); }
  peek(): T | undefined { return this.data.at(-1); }
  get size(): number { return this.data.length; }
}
```

---

### [F-09] Devolver una referencia puede romper el ocultamiento

@tipo: concepto-mixto

# Una interfaz segura controla también los valores que escapan

- Devolver `data` permite modificar la representación sin usar operaciones.
- `readonly T[]` restringe mutaciones directas en TypeScript.
- Una copia evita compartir el contenedor interno.
- Una copia superficial todavía comparte los elementos.

```typescript
toArray(): readonly T[] {
  return [...this.data];
}
```

---

### [F-10] Actividad: auditar una interfaz

@tipo: socratica

# ¿Qué operaciones pertenecen realmente a Stack?

- Evalúen `clear`, `contains`, `at`, `sort` y `toArray`.
- Para cada operación, indiquen si preserva la abstracción LIFO.
- Identifiquen qué compromiso agrega al contrato.
- Propongan una interfaz mínima y una interfaz extendida.

---

### [F-11] Parametrizar el ADT separa estructura y elemento

@tipo: concepto-mixto

# `Stack<T>` reutiliza la abstracción sin fijar el tipo almacenado

- Las reglas LIFO son independientes del tipo de elemento.
- El parámetro `T` mantiene consistencia entre `push`, `pop` y `peek`.
- Una única implementación sirve para muchas instanciaciones.
- El cliente conserva información precisa de tipos.
- El ADT genérico combina abstracción de datos y polimorfismo paramétrico.

`[Sebesta, §11.4, pp. 487-492]`

```typescript
const números = new ArrayStack<number>();
const nombres = new ArrayStack<string>();
// T preserva el tipo entre push, pop y peek.
```

---

### [F-12] Un constraint solo corresponde si una operación lo necesita

@tipo: tabla-comparativa

# Restringir de más reduce reutilización

| Diseño | Operaciones usadas por la implementación | Constraint necesario |
|---|---|---|
| `Stack<T>` | Almacenar y devolver | Ninguno |
| `SortedSet<T>` | Comparar elementos | Comparador o capacidad de comparación |
| `PrintableQueue<T>` | Formatear elementos | Capacidad de representación textual |
| `Map<K,V>` | Identificar claves | Depende de la estrategia de claves |

---

### [F-13] Un módulo encapsula más que un tipo

@tipo: concepto-abstracto

# El módulo lleva information hiding a programas grandes

- Un ADT suele encapsular un tipo y sus operaciones.
- Un módulo puede contener varios tipos, funciones, constantes y estado.
- Expone una interfaz seleccionada y oculta decisiones internas.
- Declara dependencias con otros módulos.
- Puede constituir una unidad de compilación y despliegue.

`[Sebesta, §11.6 · Gabbrielli/Martini, §9.3]`

---

### [F-14] ADT y módulo resuelven problemas relacionados, pero distintos

@tipo: tabla-comparativa

# Programar “en pequeño” y “en grande” exige mecanismos diferentes

| Dimensión | ADT | Módulo |
|---|---|---|
| Centro de la abstracción | Un tipo | Un subsistema |
| Puede agrupar | Representación y operaciones | Varios tipos, funciones y recursos |
| Instancias | Normalmente muchas | Frecuentemente una unidad |
| Interfaz | Operaciones del tipo | Exportaciones del subsistema |
| Dependencias | Otras abstracciones usadas | Imports explícitos |

`[Gabbrielli/Martini, §9.3 · Sebesta, §11.6]`

---

### [F-15] Una interfaz estable permite sustituir implementaciones

@tipo: concepto-mixto

# El cliente depende del contrato, no de la representación

- `ArrayStack` y `LinkedStack` pueden cumplir la misma interfaz.
- El cliente compila y prueba contra `Stack<T>`.
- Cambiar la implementación no debería cambiar el código cliente.
- La sustitución falla si el contrato omite propiedades importantes.

```typescript
function vaciar<T>(s: Stack<T>): T[] {
  const result: T[] = [];
  while (s.size > 0) result.push(s.pop()!);
  return result;
}
```

---

### [F-16] La sustitución exige preservar comportamiento

@tipo: concepto-abstracto

# Coincidir en tipos no garantiza cumplir el contrato

- Una implementación puede tener la firma correcta y semántica incorrecta.
- Si `pop` elimina el elemento más antiguo, implementa Queue, no Stack.
- Las invariantes y ecuaciones completan lo que los tipos no expresan.
- Los tests de contrato deben ejecutarse sobre cada implementación.
- La interfaz es sintáctica; el contrato también es semántico.

---

### [F-17] Actividad: cambiar la representación

@tipo: socratica

# De ArrayStack a LinkedStack

- Enumeren qué partes del cliente deberían permanecer iguales.
- Identifiquen qué decisiones cambian dentro de la implementación.
- Propongan tests de contrato comunes.
- Expliquen qué filtración de representación impediría el reemplazo.

---

### [F-18] Los módulos clásicos separan definición e implementación

@tipo: tabla-comparativa

# Modula-2 vuelve física la frontera del contrato

`[Louden/Lambert, §11.3, pp. 503-509]`

| Unidad | Contenido | Quién necesita verla |
|---|---|---|
| `DEFINITION MODULE` | Tipos abstractos y operaciones exportadas | Clientes y compilador |
| `IMPLEMENTATION MODULE` | Representaciones, algoritmos y auxiliares privados | Implementación |
| Cliente | Imports y uso de exportaciones | No necesita detalles internos |

---

### [F-19] TypeScript separa interfaz estática y código ejecutable

@tipo: concepto-mixto

# Tipos y valores ocupan espacios relacionados, pero distintos

- `export interface` describe un contrato solo para el compilador.
- `export class` produce también un valor JavaScript en runtime.
- `import type` declara una dependencia exclusivamente estática.
- Los archivos `.d.ts` publican tipos sin implementación.

```typescript
import type { Stack } from "./stack.js";
import { ArrayStack } from "./array-stack.js";
const s: Stack<number> = new ArrayStack<number>();
```

---

### [F-20] Las dependencias explícitas documentan arquitectura

@tipo: concepto-mixto

# Un import es una relación que debe poder justificarse

- Permite conocer qué servicios externos necesita un módulo.
- Ayuda al compilador a ordenar y verificar unidades.
- Permite detectar ciclos y cambios que requieren recompilación.
- Imports amplios aumentan acoplamiento.
- Depender de interfaces suele preservar más opciones.

`[Louden/Lambert, §11.2, pp. 500-503]`

```typescript
import type { PaymentGateway } from "./payments.js";
// El módulo depende del contrato, no de una implementación concreta.
```

---

### [F-21] Un ciclo de dependencias revela responsabilidades mezcladas

@tipo: concepto-mixto

# Romper ciclos suele exigir introducir una abstracción

- `pedidos` usa `pagos` para cobrar.
- `pagos` usa `pedidos` para actualizar estado.
- Ninguno puede comprenderse o probarse aisladamente.
- Un contrato de eventos o servicio compartido puede invertir la dependencia.

```text
pedidos -> pagos -> pedidos
          |
          v
    eventos-de-pago
```

---

### [F-22] Actividad: auditar dependencias

@tipo: socratica

# Diseñen un grafo modular

- Modelen módulos de usuarios, pedidos, pagos y notificaciones.
- Dibujen imports necesarios.
- Detecten un ciclo o dependencia excesiva.
- Introduzcan una interfaz o evento para mejorar el diseño.

---

### [F-23] Compilar por separado no significa compilar sin contexto

@tipo: tabla-comparativa

# Separada e independiente ofrecen garantías diferentes

`[Louden/Lambert, §11.2 · Sebesta, §11.6]`

| Característica | Compilación separada | Compilación independiente |
|---|---|---|
| Unidad compilada | Un módulo por vez | Una unidad aislada |
| Conoce interfaces externas | Sí | No necesariamente |
| Chequeo entre módulos | Posible en compilación | Se difiere al enlace o ejecución |
| Beneficio | Recompilar solo partes afectadas con seguridad | Máxima independencia física |
| Riesgo | Interfaces desactualizadas | Incompatibilidades tardías |

---

### [F-24] La interfaz determina el impacto de un cambio

@tipo: tabla

# No todo cambio interno obliga a recompilar clientes

| Cambio | ¿Cambia la interfaz? | Impacto esperado |
|---|---|---|
| Optimizar un algoritmo privado | No | Recompilar implementación |
| Cambiar array por lista enlazada | No | Recompilar implementación |
| Agregar un parámetro público | Sí | Revisar clientes |
| Cambiar el tipo de retorno | Sí | Revisar clientes |
| Agregar una función privada | No | Sin impacto contractual |

---

### [F-25] Un paquete publica una superficie seleccionada

@tipo: concepto-mixto

# La API pública debe ser más pequeña que el código interno

- `index.ts` reexporta únicamente los servicios estables.
- `package.json` describe entradas, versiones y dependencias.
- `.d.ts` comunica contratos a consumidores TypeScript.
- Versionar una biblioteca implica gestionar cambios de interfaz.

```typescript
// index.ts
export type { Stack } from "./stack.js";
export { ArrayStack } from "./array-stack.js";
// No exporta helpers internos ni representación.
```

---

### [F-26] La modularidad permite trabajo y evolución independientes

@tipo: concepto-abstracto

# Un buen módulo reduce el conocimiento necesario para cambiar el sistema

- Alta cohesión: sus elementos colaboran en una responsabilidad clara.
- Bajo acoplamiento: depende de pocos contratos estables.
- Interfaz pequeña: ofrece lo necesario, no todos los detalles disponibles.
- Dependencias explícitas: permiten analizar impacto.
- Implementación oculta: conserva libertad de evolución.

`[Sebesta, §11.6 · Louden/Lambert, cap. 11]`

---

### [F-27] Actividad: diseñar una API pública

@tipo: socratica

# Repositorio de usuarios: contrato o detalle

- Decidan si exportar `findById`, `save`, `pool`, `cache` y `reconnect`.
- Clasifiquen cada elemento como contrato o implementación.
- Expliquen qué pasaría al migrar de PostgreSQL a MongoDB.
- Propongan una interfaz mínima que permita probar clientes.

---

### [F-28] La progresión completa va de operación a arquitectura

@tipo: tabla

# Cada nivel oculta una clase diferente de decisiones

| Nivel | Abstrae | Oculta | Contrato visible |
|---|---|---|---|
| Subprograma | Una acción | Instrucciones y estado local | Perfil y protocolo |
| ADT | Un tipo conceptual | Representación e invariantes internas | Operaciones del tipo |
| Módulo | Un subsistema | Tipos, funciones y recursos internos | Exportaciones e imports |
| Paquete | Una biblioteca distribuible | Organización y construcción internas | API, tipos y versión |

---

### [F-29] Una interfaz útil combina tipos y leyes

@tipo: tabla

# La firma dice qué puede llamarse; el contrato dice qué significa

| Parte del contrato | Garantía |
|---|---|
| Tipos | Descartan muchas llamadas inválidas |
| Invariantes | Restringen estados válidos |
| Ecuaciones | Relacionan operaciones observables |
| Tests de contrato | Vuelven ejecutables las expectativas |
| Documentación | Comunica garantías a clientes |

`[Louden/Lambert, §11.1 · Sebesta, cap. 11]`

---

### [F-30] Cierre 13B

@tipo: cierre

# Modularidad es preservar libertad de cambio

- El ADT oculta representación detrás de operaciones significativas.
- La interfaz establece lo que clientes pueden asumir.
- El módulo agrupa abstracciones y declara dependencias.
- La compilación separada usa contratos para limitar impacto.

## Pregunta final: ¿qué decisión interna podría cambiar mañana sin romper clientes?
