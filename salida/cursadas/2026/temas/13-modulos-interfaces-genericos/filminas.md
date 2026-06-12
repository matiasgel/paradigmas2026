# Filminas - Clase 13B - Módulos, contratos e interfaces

> Duración: 120 minutos
> Hilo conductor: de un contrato tipado a una frontera modular versionada
> Fuentes: Sebesta, capítulos 11 y 12; Louden/Lambert, capítulo 11; Gabbrielli/Martini, capítulo 9
> Lenguaje principal: TypeScript | Contraste: Kotlin, Rust, Swift y Go
> Enfoque actualizado: tipos algebraicos, capacidades, privacidad, dependencias y compatibilidad
> Documentación contemporánea: Rust Book, Kotlin Docs, TypeScript Handbook y Go Modules

---

### [F-00] Portada 13B

@tipo: portada

# CLASE 13B

## Módulos y contratos: organizar decisiones que pueden cambiar

- Tipos algebraicos para modelar datos con casos cerrados.
- Interfaces y protocolos para expresar capacidades.
- Módulos y paquetes para seleccionar una API pública.
- Compatibilidad y evolución separada de componentes.

---

### [F-01] Tres mecanismos parecidos resuelven problemas distintos

@tipo: tabla-comparativa

# Tipo algebraico, interfaz y módulo no son sinónimos

| Mecanismo | Pregunta central | Ejemplo moderno |
|---|---|---|
| Tipo algebraico | ¿Qué formas puede tener un dato? | `sealed class` de Kotlin, `enum` de Rust |
| Interfaz o protocolo | ¿Qué capacidades debe ofrecer una implementación? | `interface` de Kotlin, trait de Rust |
| Módulo o paquete | ¿Qué nombres son públicos y de qué depende el componente? | módulo Rust, package Go |

> Un tipo algebraico modela datos; no implica por sí mismo ocultamiento de representación ni una frontera modular.

---

### [F-02] La independencia de representación preserva clientes

@tipo: tabla-comparativa

# Una frontera estable permite reemplazar decisiones internas

| Decisión interna que cambia | Contrato que permanece | Cliente que no debería cambiar |
|---|---|---|
| Memoria o base de datos | `Repository.save/findById` | Servicio de aplicación |
| Caché local o distribuida | `Cache.get/put` | Consumidor de la caché |
| HTTP o cola de mensajes | `PaymentGateway.charge` | Módulo de pedidos |
| Algoritmo secuencial o paralelo | Firma y semántica del servicio | Orquestador |

`[Gabbrielli/Martini, cap. 9 · Sebesta, cap. 11]`

---

### [F-03] Un tipo algebraico describe la forma de los datos

@tipo: concepto-mixto

# Sumas y productos hacen explícitos estados posibles

- Un producto combina campos: un pago aprobado tiene identificador y fecha.
- Una suma ofrece alternativas: pendiente, aprobado o rechazado.
- Una jerarquía sellada permite verificar que todos los casos fueron tratados.
- Esto modela estados; la privacidad y las dependencias pertenecen a otros mecanismos.

```kotlin
sealed interface ResultadoPago {
    data object Pendiente : ResultadoPago
    data class Aprobado(val id: String) : ResultadoPago
    data class Rechazado(val motivo: String) : ResultadoPago
}
```

---

### [F-04] Mundo cerrado y mundo abierto favorecen diseños distintos

@tipo: tabla-comparativa

# La extensibilidad deseada orienta el mecanismo

| Diseño | Quién agrega variantes | Verificación favorecida | Ejemplo |
|---|---|---|---|
| Tipo algebraico sellado | Autor del tipo | Exhaustividad de casos | Estados de una operación |
| Interfaz abierta | Autores de implementaciones | Capacidades requeridas | Proveedores de pago |
| Módulo cerrado | Equipo propietario | Superficie exportada | Núcleo de facturación |
| Plugin | Terceros autorizados | Integración en runtime | Adaptadores externos |

---

### [F-05] Los tipos de dominio pueden impedir estados inválidos

@tipo: concepto-mixto

# Un wrapper nominal agrega significado sin inventar una arquitectura

- `String` no distingue un correo de un identificador.
- Un tipo de valor evita intercambiar datos con igual representación.
- La validación puede concentrarse en la construcción.
- Kotlin puede representar ciertos value classes sin wrapper adicional en runtime.

```kotlin
@JvmInline
value class UserId(val value: String)

fun buscarUsuario(id: UserId): Usuario
```

---

### [F-06] Encapsulación e information hiding no son sinónimos

@tipo: tabla-comparativa

# Agrupar ayuda; ocultar decisiones permite cambiar

| Concepto | Pregunta que responde | Ejemplo |
|---|---|---|
| Encapsulación | ¿Qué datos y operaciones forman una unidad? | Componente de pagos |
| Information hiding | ¿Qué decisiones pueden cambiar sin afectar clientes? | Proveedor HTTP o cola |
| Interfaz | ¿Qué puede observar y solicitar el cliente? | `charge`, `refund`, `status` |
| Invariante | ¿Qué debe permanecer cierto? | Un pago confirmado no vuelve a pendiente |

`[Sebesta, §§11.1-11.3 · Gabbrielli/Martini, cap. 9]`

---

### [F-07] Kotlin expresa capacidades sin fijar implementaciones

@tipo: concepto-mixto

# Una operación pública amplía para siempre lo que el cliente puede asumir

- La interfaz declara operaciones que el cliente necesita.
- Cada proveedor conserva autenticación, transporte y reintentos internos.
- Una interfaz mínima reduce acoplamiento y mantiene opciones abiertas.
- La semántica documentada importa tanto como las firmas.

```kotlin
interface PaymentGateway {
    suspend fun charge(order: OrderId, amount: Money): ResultadoPago
    suspend fun refund(payment: PaymentId): ResultadoPago
}
```

---

### [F-08] Rust oculta la representación por defecto

@tipo: concepto-mixto

# `pub` selecciona la superficie observable del módulo

- Los campos privados solo son visibles dentro de su módulo.
- Los métodos `pub` forman la interfaz accesible al cliente.
- Toda modificación pasa por operaciones controladas.
- La implementación puede cambiar sin reescribir clientes.

`[Louden/Lambert, §11.2 · Sebesta, §11.4]`

```rust
pub struct Token {
    raw: String, // privado fuera del módulo
}
impl Token {
    pub fn parse(raw: String) -> Result<Self, TokenError> {
        validar(&raw)?;
        Ok(Self { raw })
    }
}
```

---

### [F-09] Devolver una referencia puede romper el ocultamiento

@tipo: concepto-mixto

# Una interfaz segura controla también los valores y permisos que escapan

- Devolver una colección mutable filtra decisiones internas.
- Una vista de solo lectura restringe capacidades del cliente.
- Un iterador permite recorrer sin revelar almacenamiento.
- Una copia aísla el contenedor, pero puede conservar elementos compartidos.

```typescript
listar(): readonly UsuarioResumen[] {
  return this.usuarios.map(resumir);
}
```

---

### [F-10] Una interfaz puede preservar o filtrar la abstracción

@tipo: tabla-comparativa

# Cada operación pública amplía dependencias y compromisos

| Operación pública | Capacidad expuesta | Consecuencia contractual |
|---|---|---|
| `findById` | Consulta por identidad | Exige definir ausencia y errores |
| `save` | Persistencia | Exige definir consistencia |
| `rawConnection` | Acceso a infraestructura | Filtra representación |
| `clearCache` | Control operacional | Acopla al uso de caché |
| `list` | Recorrido | Exige definir orden y paginación |

---

### [F-11] Swift relaciona tipos a través de un protocolo genérico

@tipo: concepto-mixto

# `associatedtype` conserva relaciones precisas en una frontera

- Cada repositorio define qué entidad administra.
- `Entity.ID` mantiene consistencia entre consulta y resultado.
- Varias implementaciones cumplen el mismo protocolo.
- El cliente conserva información precisa sin conocer infraestructura.

`[Sebesta, §11.4, pp. 487-492, reinterpretado como contrato genérico]`

```swift
protocol Repository {
    associatedtype Entity: Identifiable
    func find(id: Entity.ID) async throws -> Entity?
    func save(_ entity: Entity) async throws
}
```

---

### [F-12] Un constraint solo corresponde si una operación lo necesita

@tipo: tabla-comparativa

# Restringir de más reduce reutilización

| Diseño | Operaciones usadas por la implementación | Constraint necesario |
|---|---|---|
| `Repository<E>` | Identificar y persistir | Identidad estable |
| `Orderer<T>` | Comparar elementos | Comparador |
| `Serializer<T>` | Codificar y decodificar | Esquema o codec |
| `Cache<K,V>` | Identificar claves | Igualdad y hashing |

---

### [F-13] Go permite sustituir implementaciones por comportamiento

@tipo: concepto-mixto

# El cliente depende del contrato, no de la representación

- Un reloj real y uno controlado pueden cumplir la misma interfaz.
- El cliente compila y prueba contra la capacidad `Clock`.
- Cambiar la implementación no debería cambiar el código cliente.
- La sustitución falla si el contrato omite propiedades importantes.

```go
type Clock interface {
    Now() time.Time
}
func Expired(c Clock, deadline time.Time) bool {
    return c.Now().After(deadline)
}
```

---

### [F-14] La sustitución exige preservar comportamiento

@tipo: concepto-abstracto

# Coincidir en tipos no garantiza cumplir el contrato

- Una implementación puede tener la firma correcta y semántica incorrecta.
- Un reloj que retrocede inesperadamente puede romper clientes aunque cumpla la firma.
- Invariantes, precondiciones y postcondiciones completan lo que los tipos no expresan.
- Los tests de contrato deben ejecutarse sobre cada implementación.
- La interfaz es sintáctica; el contrato también es semántico.

---

### [F-15] Los tests de contrato verifican sustitución

@tipo: tabla-comparativa

# El cliente permanece estable cuando el contrato es suficiente

| Aspecto | Contrato compartido | Variación permitida |
|---|---|---|
| Operación | `Now()` devuelve un instante | Reloj del sistema o controlado |
| Semántica | Zona, precisión y monotonicidad documentadas | Fuente temporal concreta |
| Tests | Misma suite de contrato | Casos específicos de integración |
| Rendimiento | Costo máximo publicado | Consulta local o remota |

---

### [F-16] Un módulo agrupa decisiones que cambian juntas

@tipo: concepto-abstracto

# El módulo lleva information hiding a programas grandes

- Un módulo puede contener tipos, funciones, constantes y estado.
- Expone una interfaz seleccionada y oculta decisiones internas.
- Declara dependencias con otros módulos.
- Puede constituir una unidad de compilación y despliegue.
- Su frontera debería coincidir con una responsabilidad coherente.

`[Sebesta, §11.6 · Gabbrielli/Martini, §9.3]`

---

### [F-17] Tipo, módulo, paquete y servicio operan en escalas distintas

@tipo: tabla-comparativa

# Programar “en pequeño” y “en grande” exige mecanismos diferentes

| Unidad | Organiza | Frontera observable | Evolución |
|---|---|---|---|
| Tipo | Valores relacionados | Campos, casos u operaciones | Compilación |
| Módulo | Código cohesivo | Exportaciones e imports | Recompilación |
| Paquete | Biblioteca distribuible | API y versión | Gestor de dependencias |
| Servicio | Capacidad desplegada | Protocolo de red | Despliegue independiente |

`[Gabbrielli/Martini, §9.3 · Sebesta, §11.6]`

---

### [F-18] Los lenguajes modernos seleccionan una API pública

@tipo: tabla-comparativa

# La visibilidad convierte una frontera conceptual en una regla verificable

`[Louden/Lambert, §11.3, pp. 503-509]`

| Unidad | Contenido | Quién necesita verla |
|---|---|---|
| Rust | Elementos `pub` frente a privados | El crate y sus clientes |
| Kotlin | Visibilidad `public`, `internal` y `private` | El módulo de compilación |
| Go | Nombres exportados con mayúscula | Otros packages |

> En los tres casos, la interfaz pública es menor que el conjunto de decisiones internas.

---

### [F-19] TypeScript separa interfaz estática y código ejecutable

@tipo: concepto-mixto

# Tipos y valores ocupan espacios relacionados, pero distintos

- `export interface` describe un contrato solo para el compilador.
- `export class` produce también un valor JavaScript en runtime.
- `import type` declara una dependencia exclusivamente estática.
- Los archivos `.d.ts` publican tipos sin implementación.

```typescript
import type { PaymentGateway } from "./payments.js";
import { createCheckout } from "./checkout.js";
declare const gateway: PaymentGateway;
const checkout = createCheckout(gateway);
```

> Contraste: Rust, Kotlin y Go conservan fronteras de módulo en compilación; TypeScript borra las interfaces al emitir JavaScript.

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

### [F-22] Un grafo modular revela acoplamiento

@tipo: concepto-abstracto

# Dependencias dirigidas permiten localizar ciclos

- `pedidos` depende de contratos de usuarios y pagos.
- `pagos` publica eventos sin depender de pedidos.
- `notificaciones` consume eventos y permanece periférico.
- Una interfaz compartida invierte dependencias concretas.
- El grafo acíclico permite comprender y probar módulos por separado.

---

### [F-23] Compilar por separado no significa compilar sin contexto

@tipo: tabla-comparativa

# Compilación incremental necesita contratos y grafos confiables

`[Louden/Lambert, §11.2 · Sebesta, §11.6]`

| Mecanismo moderno | Unidad y contexto | Beneficio |
|---|---|---|
| TypeScript Project References | Proyectos con contratos `.d.ts` | Builds incrementales y límites explícitos |
| Crates de Rust | Paquetes compilados con dependencias verificadas | Privacidad y chequeo estático |
| Packages y modules de Go | Imports y versiones declaradas | Builds reproducibles |
| Caché de compilación | Artefactos identificados por entradas | Evitar trabajo no afectado |

> Separar archivos no alcanza: el sistema de build debe conocer contratos, versiones y dependencias.

---

### [F-24] La interfaz determina el impacto de un cambio

@tipo: tabla

# No todo cambio compatible obliga a revisar clientes

| Cambio | ¿Cambia la interfaz? | Impacto esperado |
|---|---|---|
| Optimizar un algoritmo privado | No | Recompilar o redesplegar implementación |
| Cambiar proveedor interno | No | Verificar contrato y operación |
| Agregar un parámetro público | Sí | Revisar clientes |
| Cambiar el tipo de retorno | Sí | Revisar clientes |
| Alterar semántica sin cambiar firma | No sintácticamente | Riesgo de ruptura semántica |

---

### [F-25] Un paquete publica una superficie seleccionada

@tipo: concepto-mixto

# La API pública debe ser más pequeña que el código interno

- `exports` selecciona puntos de entrada soportados.
- `package.json` describe versiones y dependencias.
- `.d.ts` comunica contratos a consumidores TypeScript.
- Versionar implica gestionar cambios sintácticos y semánticos.

```typescript
// index.ts
export type { PaymentGateway } from "./payments.js";
export { createCheckout } from "./checkout.js";
// No exporta adaptadores ni helpers internos.
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

### [F-27] Una API versionada clasifica cambios por compatibilidad

@tipo: tabla-comparativa

# La visibilidad y la versión comunican compromisos distintos

| Cambio | Compatibilidad esperada | Tratamiento |
|---|---|---|
| Corregir implementación privada | Compatible | Patch |
| Agregar capacidad opcional | Usualmente compatible | Minor |
| Quitar exportación pública | Incompatible | Major |
| Cambiar significado conservando firma | Potencialmente incompatible | Documentar y versionar |
| Ampliar casos de un tipo cerrado | Depende de exhaustividad del cliente | Evaluar como ruptura |

---

### [F-28] La progresión completa va de operación a arquitectura

@tipo: tabla

# Cada nivel oculta una clase diferente de decisiones

| Nivel | Abstrae | Oculta | Contrato visible |
|---|---|---|---|
| Subprograma | Una acción | Instrucciones y estado local | Perfil y protocolo |
| Tipo algebraico | Casos de un dato | Representación concreta de variantes | Constructores y patrones |
| Módulo | Un subsistema | Tipos, funciones y recursos internos | Exportaciones e imports |
| Paquete | Una biblioteca distribuible | Organización y construcción internas | API, tipos y versión |
| Servicio | Una capacidad desplegada | Procesos e infraestructura | Protocolo y política operativa |

---

### [F-29] Un contrato útil combina tipos, semántica y evolución

@tipo: tabla

# La firma dice qué puede llamarse; el contrato dice qué significa

| Parte del contrato | Garantía |
|---|---|
| Tipos | Descartan muchas llamadas inválidas |
| Invariantes | Restringen estados válidos |
| Precondiciones y postcondiciones | Relacionan entradas, efectos y resultados |
| Tests de contrato | Vuelven ejecutables las expectativas |
| Documentación | Comunica garantías a clientes |
| Política de versión | Comunica cómo puede evolucionar la API |

`[Louden/Lambert, §11.1 · Sebesta, cap. 11]`

---

### [F-30] Cierre 13B

@tipo: cierre

# Modularidad es preservar libertad de cambio

- El tipo algebraico modela un conjunto cerrado de formas de datos.
- La interfaz establece capacidades que implementaciones abiertas deben cumplir.
- El módulo agrupa decisiones y declara dependencias.
- El paquete publica una API versionada y limita el impacto de cambios.

## Criterio final: una decisión verdaderamente interna puede cambiar sin romper clientes
