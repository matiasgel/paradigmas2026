# Filminas - Clase 13A - Subprogramas, parámetros y sobrecarga

> Duración: 120 minutos
> Hilo conductor: decisiones de diseño de subprogramas
> Fuente principal: Sebesta, capítulos 9 y 10
> Complemento: Gabbrielli y Martini, capítulo 5

---

### [F-00] Portada 13A

@tipo: portada

# CLASE 13A

## Subprogramas: del contrato a la ejecución

- ¿Qué promete un subprograma?
- ¿Cómo se comunican llamador y llamado?
- ¿Qué decisiones favorecen seguridad, reutilización y recursividad?
- ¿Cómo implementa el runtime una llamada?

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
| En TypeScript | Retorno `void` | Retorno tipado |
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
```

---

### [F-05] Actividad: reconstruir el contrato

@tipo: socratica

# ¿Qué puede saber el cliente sin leer el cuerpo?

## Actividad de 5 minutos

- Escriban el perfil y el protocolo de `distancia`.
- Propongan una llamada válida y dos llamadas inválidas.
- Señalen qué errores puede detectar TypeScript.
- Expliquen qué información sigue oculta.

---

### [F-06] Las variables locales plantean una decisión de diseño

@tipo: tabla-comparativa

# Duración y alcance no son lo mismo

`[Sebesta, §9.4, pp. 398-402]`

| Variable local | Cuándo existe | Consecuencia |
|---|---|---|
| Estática | Durante toda la ejecución | Conserva historia entre llamadas |
| Stack-dynamic | Desde la llamada hasta el retorno | Cada activación obtiene su propia copia |
| Explícitamente heap-dynamic | Según creación y liberación explícita | Flexible, pero costosa y riesgosa |
| Implícitamente heap-dynamic | Según asignaciones en ejecución | Flexible, con menor previsibilidad |

---

### [F-07] La recursividad necesita activaciones independientes

@tipo: concepto-mixto

# Una variable local por llamada hace posible la recursión

- El código de `factorial` existe una sola vez.
- Cada llamada necesita un valor de `n` diferente.
- Las locales stack-dynamic viven en activation records separados.
- Con una única copia estática, las llamadas se sobrescribirían.

`[Sebesta, §§9.4 y 10.3]`

```typescript
function factorial(n: number): number {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
```

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

### [F-10] Pass-by-value crea una variable local

@tipo: concepto-mixto

# Modificar el parámetro formal no modifica el argumento

- La expresión real se evalúa antes de entrar.
- Su valor inicializa una nueva variable local.
- La asignación afecta solo esa copia.
- El retorno explícito comunica el resultado.

`[Sebesta, §9.5.2.1 · Gabbrielli/Martini, cap. 5]`

```typescript
function incrementar(n: number): number {
  n = n + 1;
  return n;
}
let edad = 20;
const siguiente = incrementar(edad); // edad sigue siendo 20
```

---

### [F-11] Pass-by-reference introduce aliasing

@tipo: concepto-abstracto

# Dos nombres para una ubicación vuelven menos local el razonamiento

- El formal se vincula con la ubicación del argumento real.
- Asignar al formal modifica directamente el dato del llamador.
- Si dos parámetros referencian la misma ubicación aparece **aliasing**.
- El resultado puede depender de un detalle invisible en el encabezado.
- Se gana eficiencia, pero se pierde aislamiento.

`[Sebesta, §9.5.2.4, pp. 412-416]`

---

### [F-12] Valor-resultado cambia aliasing por copia diferida

@tipo: concepto-abstracto

# Copy-in/copy-out evita aliasing interno, pero crea otro conflicto

- Al llamar, cada formal recibe una copia independiente.
- Durante el cuerpo, los formales no comparten ubicación.
- Al retornar, cada resultado se copia al argumento correspondiente.
- Si dos argumentos designan la misma variable, importa el orden de copia.
- El lenguaje debe definir o restringir ese caso.

`[Sebesta, §9.5.2.3, pp. 409-412]`

---

### [F-13] Actividad: elegir un mecanismo

@tipo: socratica

# ¿Qué mecanismo elegirían y qué riesgo aceptarían?

## Caso

Una función recibe una matriz grande, consulta casi todas sus celdas y debe modificar solo una.

- Comparen valor, referencia y valor-resultado.
- Evalúen eficiencia, claridad y riesgo de aliasing.
- Propongan una firma que haga explícita la intención.
- Defiendan una elección.

---

### [F-14] TypeScript siempre copia el valor del argumento

@tipo: concepto-mixto

# En objetos, el valor copiado es una referencia compartida

- Reasignar el parámetro no cambia la variable del llamador.
- Mutar el objeto alcanzado sí es observable desde afuera.
- Esta semántica suele llamarse **pass-by-sharing**.
- No equivale a la referencia de C++, porque no permite reasignar la variable externa.

```typescript
function actualizar(p: { nombre: string }): void {
  p.nombre = "Ada";          // muta el objeto compartido
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

### [F-16] Actividad: explicar pass-by-sharing

@tipo: socratica

# Predigan antes de ejecutar

```typescript
const usuario = { nombre: "Lin", roles: ["lector"] };
function cambiar(u: typeof usuario): void {
  u.roles.push("editor");
  u = { nombre: "Otro", roles: [] };
}
cambiar(usuario);
```

- ¿Qué nombre queda?
- ¿Qué roles quedan?
- Dibujen variables y objetos.
- Expliquen sin decir “se pasa por referencia”.

---

### [F-17] Pasar un subprograma exige definir su entorno

@tipo: concepto-mixto

# Una función como parámetro lleva código, pero también necesita nombres

- El protocolo permite verificar qué función puede pasarse.
- El cuerpo de esa función puede usar variables no locales.
- El lenguaje debe decidir qué entorno se usa al ejecutarla.
- Con alcance estático suele preservarse el entorno de definición.
- Ese problema conduce al concepto de closure.

`[Sebesta, §9.6, pp. 420-425]`

```typescript
type Comparador<T> = (a: T, b: T) => number;
function ordenar<T>(xs: T[], comparar: Comparador<T>): T[] {
  return [...xs].sort(comparar);
}
```

---

### [F-18] Una closure conserva el entorno que necesita

@tipo: concepto-mixto

# Closure = subprograma + entorno de referencia

- `crearContador` retorna después de crear la función interna.
- La variable `cuenta` debe sobrevivir al retorno.
- Cada invocación crea un entorno independiente.
- El runtime mantiene ese entorno mientras sea alcanzable.

`[Sebesta, §9.12 · Gabbrielli/Martini, cap. 5]`

```typescript
function crearContador(): () => number {
  let cuenta = 0;
  return () => ++cuenta;
}
```

---

### [F-19] Las funciones de orden superior reutilizan políticas

@tipo: concepto-mixto

# Separar recorrido de criterio reduce duplicación

- `filtrar` implementa el recorrido una sola vez.
- El predicado representa una política variable.
- Su protocolo limita qué políticas son compatibles.
- El parámetro de tipo conserva la relación entre entrada y salida.

```typescript
type Predicado<T> = (valor: T) => boolean;
function filtrar<T>(xs: T[], acepta: Predicado<T>): T[] {
  return xs.filter(acepta);
}
```

---

### [F-20] Sobrecarga ofrece varias implementaciones bajo un nombre

@tipo: concepto-abstracto

# Sobrecarga es polimorfismo ad hoc

- Dos subprogramas comparten nombre en el mismo entorno.
- Sus protocolos deben permitir distinguir cada llamada.
- La selección depende de los argumentos y reglas del lenguaje.
- Las implementaciones pueden realizar operaciones diferentes.
- Defaults y conversiones implícitas pueden volver ambigua la resolución.

`[Sebesta, §9.9, pp. 429-432]`

---

### [F-21] TypeScript sobrecarga contratos, no cuerpos

@tipo: concepto-mixto

# Las overload signatures describen casos visibles

- El cliente ve protocolos específicos.
- Existe una única implementación JavaScript en runtime.
- El cuerpo debe aceptar todos los casos declarados.
- Un genérico suele ser mejor cuando la relación entre tipos es uniforme.

```typescript
function longitud(x: string): number;
function longitud<T>(x: T[]): number;
function longitud(x: string | unknown[]): number {
  return x.length;
}
```

---

### [F-22] Un genérico expresa una familia uniforme

@tipo: concepto-mixto

# Polimorfismo paramétrico: una implementación para muchos tipos

- El parámetro de tipo reemplaza nombres de tipos concretos.
- La implementación solo puede asumir operaciones permitidas para `T`.
- La inferencia evita indicar el tipo en muchas llamadas.
- El resultado conserva relaciones precisas entre tipos.

`[Sebesta, §9.10, pp. 432-438]`

```typescript
function primero<T>(xs: readonly T[]): T | undefined {
  return xs[0];
}
```

---

### [F-23] Los constraints declaran capacidades necesarias

@tipo: concepto-mixto

# Un constraint debe ser tan débil como permita el algoritmo

- Sin constraint, el algoritmo no puede asumir operaciones específicas.
- `extends` exige una estructura mínima.
- Un constraint excesivo reduce reutilización sin aportar seguridad.
- El protocolo documenta exactamente qué necesita el algoritmo.

```typescript
function mayorPor<T>(
  a: T, b: T, comparar: (x: T, y: T) => number
): T {
  return comparar(a, b) >= 0 ? a : b;
}
```

---

### [F-24] Actividad: sobrecarga o genérico

@tipo: socratica

# ¿Múltiples comportamientos o una relación uniforme?

- Clasifiquen `parsear(string)`, `primero<T>(T[])` y `sumar(number|string)`.
- Decidan cuándo usar overload, unión o genérico.
- Expliquen qué relación entre entrada y salida debe preservar el tipo.
- Detecten una elección que sería engañosa para el cliente.

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

### [F-28] Actividad: construir factorial(3)

@tipo: socratica

# Dibujen las activaciones, no solo el resultado

- Representen `factorial(3)`, `factorial(2)` y `factorial(1)`.
- Incluyan parámetro, dirección de retorno y dynamic link.
- Marquen el orden de creación y liberación.
- Expliquen por qué una única variable estática `n` no alcanzaría.

---

### [F-29] Las decisiones de diseño están conectadas

@tipo: tabla

# Del contrato visible al mecanismo de ejecución

| Pregunta | Decisión | Consecuencia |
|---|---|---|
| ¿Qué acepta y retorna? | Perfil y protocolo | Verificación de llamadas |
| ¿Cómo circulan datos? | Modos y mecanismos de pasaje | Copias, aliasing y efectos |
| ¿Dónde viven las locales? | Estáticas o stack-dynamic | Historia o recursividad |
| ¿Puede recibir funciones? | Protocolo y entorno de referencia | HOF y closures |
| ¿Cómo reutiliza comportamiento? | Sobrecarga o genéricos | Ad hoc o paramétrico |
| ¿Cómo se ejecuta? | Activation records y enlaces | Call, return y acceso no local |

---

### [F-30] Cierre 13A

@tipo: cierre

# Un subprograma es simultáneamente contrato, abstracción y activación

- El contrato permite usarlo.
- Los mecanismos de pasaje determinan cómo comparte información.
- El entorno determina qué nombres puede observar.
- El activation record permite ejecutarlo y volver.

## Próxima clase: del subprograma aislado al ADT y al módulo
