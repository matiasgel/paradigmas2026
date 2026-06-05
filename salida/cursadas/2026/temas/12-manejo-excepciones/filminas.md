# Filminas — Tema 12: Manejo de Excepciones

> Curso: Paradigmas y Lenguajes de Programación · UNTDF IDEI 2026
> Cobertura: F-00 a F-17
> Referencia principal: Sebesta, *Concepts of Programming Languages*, Cap. 14, pp. 611–646
> Referencias auxiliares: Gabbrielli-Martini §7.3.1, Louden §9.5
> Lenguaje principal: TypeScript | Contraste: Go, Kotlin, Rust
> Pipeline: v3 · Nivel densidad: 2 · Generado: 2026-06-04

---

## PORTADA

---

### [F-00] Portada

@tipo: portada
@imagen: background
@prompt-imagen: ilustración conceptual de un flujo de programa que se bifurca ante un error — una flecha roja diverge del camino principal hacia un handler, con símbolos de TypeScript, Go, Kotlin y Rust en el fondo difuminado

# Manejo de Excepciones

Paradigmas y Lenguajes de Programación · Tema 12 · Módulo IX
UNTDF IDEI 2026

---

## BLOQUE A — Fundamentos conceptuales (Sebesta-first)

---

### [F-01] Pregunta de apertura

@tipo: socratica
@imagen: none

# ¿Qué hace tu programa cuando algo falla?

## Pensá en este escenario

- Una función llama a una API externa. La respuesta tarda 30 segundos y llega vacía.
- Otra función divide por un número que el usuario ingresó. Ese número es cero.
- Un agente de IA intenta ejecutar una tool. La tool lanza un error interno.

## Preguntas

- ¿El programa sigue ejecutando? ¿Se detiene? ¿Avisa al usuario?
- ¿Quién es responsable de manejar el error: quien llama, o quien es llamado?
- ¿El error es un valor de retorno normal, o una "salida de emergencia"?

---

### [F-02] Objetivos

@tipo: concepto-abstracto
@imagen: none

# Al finalizar esta clase vas a poder

- Definir excepción, handler, raise y propagación — terminología Sebesta §14.1
- Distinguir el modelo de **terminación** del de **reanudación** y saber cuál usan los lenguajes modernos
- Escribir `try / catch / finally` en TypeScript con excepciones user-defined
- Implementar el patrón `Result<T,E>` (enfoque funcional) en TypeScript
- Comparar cómo Go, Kotlin y Rust manejan errores — como decisiones de diseño de lenguaje
- Evaluar cuándo usar throw vs. Result en código real
- Identificar por qué el manejo de excepciones es crítico en programación agéntica

---

### [F-03] ¿Qué es una excepción?

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama conceptual mostrando el flujo normal de un programa (flecha verde) y el flujo excepcional (flecha roja que salta hacia un bloque handler), con etiquetas 'raise', 'propagation' y 'catch'

# Evento anómalo que el código normal no puede manejar

## Definición (Sebesta §14.1, p. 611)

> "An **exception** is any unusual event, either erroneous or not, detectable by either hardware or software, that may require special processing."

## Componentes clave

- **Exception**: el evento en sí — detectado en runtime
- **Exception handler**: el código que responde al evento
- **Raise / throw**: disparar la excepción
- **Catch**: capturarla en el handler

## No todo error es una excepción

- Error de lógica en el código → bug (se resuelve con debugging)
- Condición inesperada en runtime → excepción (se maneja con handlers)
- Archivo no encontrado, red caída, input inválido → candidatos naturales

`[Sebesta, Cap. 14 §14.1, p. 611]`

---

### [F-04] El problema antes de las excepciones

@tipo: codigo
@imagen: none

# Manejo de errores sin try/catch

## Patrón clásico: códigos de retorno (C)

```c
// C — sin excepciones: flags de error + errno global
FILE *f = fopen("data.txt", "r");
if (f == NULL) {
    fprintf(stderr, "Error: %s\n", strerror(errno));
    return -1;  // propagar manualmente por cada nivel
}
// el llamador también debe chequear el -1...
```

## Patrón: callback de error (Louden §9.5)

```c
typedef void (*ErrorHandler)(ErrorKind);

void processFile(const char *path, ErrorHandler onError) {
    // si algo falla: llamar onError en lugar de retornar -1
    // el handler es inyectado por el caller
}
```

## Problemas de estos enfoques

- Fácil olvidar chequear el código de retorno → error silenciado
- El código de manejo de errores **mezcla** con la lógica principal
- `errno` es global — no thread-safe, se sobreescribe
- Callback solo cubre **un** tipo de error por función

`[Louden & Lambert, Cap. 9 §9.5, p. 406]`

---

### [F-05] Historia: de PL/I a TypeScript

@tipo: timeline
@imagen: content
@prompt-imagen: línea de tiempo horizontal con hitos de lenguajes desde los años 70 hasta hoy: PL/I (1964), Ada (1983), C++ (1985), Java (1995), Python (2001), Go (2009), Kotlin (2011), TypeScript (2012), Rust (2015) — cada uno con su ícono y color

# Evolución del manejo de excepciones

| Año | Lenguaje | Aporte |
|-----|----------|--------|
| ~1964 | **PL/I** | Primer mecanismo formal — modelo de **reanudación** |
| 1983 | **Ada** | Modelo de **terminación** — se convierte en el estándar |
| 1985 | **C++** | `try/catch/throw` — excepciones como objetos |
| 1995 | **Java** | Jerarquía `Throwable` + checked exceptions |
| 2009 | **Go** | Rechaza excepciones — `(T, error)` como valores |
| 2011 | **Kotlin** | Sin checked exceptions + `sealed class` para errores tipados |
| 2015 | **Rust** | Sin excepciones en runtime — `Result<T,E>` obligatorio |
| 2012+ | **TypeScript** | `try/catch` heredado de JS + tipado con union types |

> Tendencia: los lenguajes más recientes prefieren errores como **valores** sobre excepciones como **flujo de control**.

---

### [F-06] Terminación vs. Reanudación

@tipo: tabla-comparativa
@imagen: content
@prompt-imagen: diagrama de dos flujos de control paralelos: izquierda muestra 'terminación' donde el bloque que generó el error se termina y el handler toma control permanentemente; derecha muestra 'reanudación' donde el handler ejecuta y retorna al punto exacto donde se levantó la excepción

# Dos modelos de continuación (Sebesta §14.1)

| Aspecto | **Terminación** | **Reanudación** |
|---------|-----------------|-----------------|
| ¿Qué pasa al lanzar? | El scope que generó la excepción **termina** | El scope que generó la excepción **se pausa** |
| ¿Dónde sigue? | En el handler — nunca vuelve al raise | El handler ejecuta → **vuelve** al punto del raise |
| Lenguajes | Java, C++, C#, TypeScript, Kotlin, Go*, Rust*, Python | PL/I (legacy), algunos LISP |
| Ventaja | Simple, predecible, stack unwinding claro | Permite "corrección" y retry in-place |
| Desventaja | No se puede continuar donde se cortó | El handler debe conocer el contexto interno del caller |

## La conclusión de Sebesta

> "Termination is **obviously the simpler** of the two models and is the model used in most contemporary languages."
> — Sebesta, p. 612

## Gabbrielli & Martini sobre terminación

> "This way of working is called 'handling with termination' — the construct where the exception is determined is **terminated**."
> — Gabbrielli §7.3.1

---

### [F-07] Las 8 preguntas de diseño (Sebesta §14.1)

@tipo: concepto-abstracto
@imagen: none

# Todo lenguaje debe responder estas preguntas

## Sebesta enumera las decisiones de diseño clave (pp. 612–614)

1. ¿Cómo se **especifican y clasifican** las excepciones?
2. ¿Cómo se **levanta** (raise/throw) una excepción?
3. ¿Cómo se **liga** una excepción a su handler?
4. ¿Puede **información** de la excepción pasarse al handler?
5. ¿Dónde **continúa** la ejecución después del handler?
6. ¿Se provee alguna forma de **finalización** (`finally`)?
7. ¿Pueden **definirse excepciones** por el usuario?
8. ¿Deben **declararse** excepciones predefinidas (checked vs. unchecked)?

## Por qué importa

- No es que TypeScript "tiene try/catch" — es que TypeScript **tomó decisiones concretas** en estas 8 dimensiones.
- Kotlin y Rust tomaron decisiones **diferentes** — y eso cambia cómo escribís código.

---

## BLOQUE B — TypeScript: imperativo y funcional

---

### [F-08] try / catch / finally en TypeScript

@tipo: codigo
@imagen: none

# Anatomía del bloque try/catch/finally

```typescript
// Ejemplo completo — TypeScript
async function loadUserData(userId: string): Promise<UserProfile> {
  try {
    // Bloque try: código que puede lanzar excepciones
    const response = await fetch(`/api/users/${userId}`)
    
    if (!response.ok) {
      // Lanzar excepción user-defined con contexto
      throw new HttpError(response.status, `User ${userId} not found`)
    }
    
    return await response.json() as UserProfile
    
  } catch (error) {
    // Bloque catch: handler — recibe el objeto lanzado
    if (error instanceof HttpError && error.statusCode === 404) {
      throw new UserNotFoundError(userId)   // re-lanzar más específica
    }
    throw error   // re-lanzar si no podemos manejarla aquí
    
  } finally {
    // Bloque finally: SIEMPRE ejecuta (con o sin excepción)
    console.log(`loadUserData(${userId}) completado`)
  }
}
```

## Flujo de control

- Si no hay excepción: `try` → `finally` → retorno normal
- Si hay excepción capturada: `try` (hasta el throw) → `catch` → `finally`
- Si hay excepción no capturada: `try` → `finally` → propagación al llamador

`[Sebesta §14.1, preguntas 5 y 6, p. 613]`

---

### [F-09] Propagación por el call stack

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama vertical de call stack con 4 capas: main → fetchUserProfile → loadUserData → fetch(). Una excepción HttpError se lanza en fetch(), sube por loadUserData (tiene handler catch → relanza UserNotFoundError), sube por fetchUserProfile (no tiene handler), llega a main (tiene catch genérico). Flechas rojas hacia arriba muestran la propagación

# La excepción sube el stack hasta encontrar un handler

## Regla de Sebesta §14.2

> "If the current block doesn't have a handler, the exception propagates to the caller — and so on, until a handler is found or the program terminates."

## Ejemplo de propagación

```
main()
  └─ fetchUserProfile(id)          ← no tiene catch para HttpError
       └─ loadUserData(id)          ← tiene catch → relanza UserNotFoundError
            └─ fetch("/api/...")    ← lanza HttpError(404)
```

## Pasos de propagación

1. `fetch()` lanza `HttpError(404)` → busca handler en `loadUserData`
2. `loadUserData` tiene `catch` → captura, transforma, relanza `UserNotFoundError`
3. `fetchUserProfile` no tiene handler para `UserNotFoundError` → propaga
4. `main` tiene `catch (e: UserNotFoundError)` → captura y maneja

## Información disponible en el handler

```typescript
catch (error) {
  if (error instanceof HttpError) {
    console.log(error.statusCode)   // campo custom
    console.log(error.message)      // heredado de Error
    console.log(error.stack)        // stack trace completo
  }
}
```

`[Sebesta, p. 614: "information about the exception is made available to the handler"]`

---

### [F-10] Excepciones user-defined en TypeScript

@tipo: codigo
@imagen: none

# Excepciones propias con contexto estructurado

## Jerarquía de clases (respuesta al diseño de lenguaje #7)

```typescript
// Base: extender Error siempre
class AppError extends Error {
  constructor(message: string, public readonly code: string) {
    super(message)
    this.name = this.constructor.name
    // Fix para stack trace en TypeScript con targets ES5
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor)
    }
  }
}

// Errors específicos del dominio
class HttpError extends AppError {
  constructor(
    public readonly statusCode: number,
    message: string
  ) {
    super(message, `HTTP_${statusCode}`)
  }
}

class UserNotFoundError extends AppError {
  constructor(public readonly userId: string) {
    super(`User ${userId} not found`, 'USER_NOT_FOUND')
  }
}

class DatabaseError extends AppError {
  constructor(
    message: string,
    public readonly query?: string
  ) {
    super(message, 'DB_ERROR')
  }
}
```

## ¿Por qué una jerarquía?

- `catch (e instanceof AppError)` → captura todos los errores de dominio
- `catch (e instanceof HttpError)` → solo HTTP
- El campo `code` permite switch/match sin `instanceof` anidados
- Sebesta: "the thrown object could include **any number of data fields** useful in the handler" (p. 614)

---

### [F-11] El enfoque funcional: Result\<T,E\>

@tipo: codigo
@imagen: none

# Errores como valores — sin romper el flujo

## Motivación

- `throw` es un **efecto secundario**: rompe el flujo de ejecución, difícil de componer en FP
- Alternativa: retornar un **tipo suma** que codifica éxito o error

```typescript
// Definición de Result<T,E>
type Result<T, E extends Error = Error> =
  | { ok: true;  value: T }
  | { ok: false; error: E }

// Helpers
const ok  = <T>(value: T): Result<T, never> => ({ ok: true, value })
const err = <E extends Error>(error: E): Result<never, E> => ({ ok: false, error })
```

## Implementación

```typescript
async function fetchUser(id: string): Promise<Result<User, HttpError>> {
  const res = await fetch(`/api/users/${id}`)
  if (!res.ok) return err(new HttpError(res.status, `HTTP ${res.status}`))
  return ok(await res.json() as User)
}
```

## Uso — exhaustivo por discriminated union

```typescript
const result = await fetchUser("42")

if (result.ok) {
  // TypeScript sabe que result.value: User
  console.log(result.value.name)
} else {
  // TypeScript sabe que result.error: HttpError
  console.error(`Error ${result.error.statusCode}: ${result.error.message}`)
}
```

## Composición con map/flatMap

```typescript
const user = await fetchUser("42")
  .then(r => r.ok ? ok(r.value.email.toLowerCase()) : r)

// O con librería como neverthrow / fp-ts
```

`[Conexión curricular: Tema 5 — Mónadas. Result<T,E> es la mónada Either]`

---

## BLOQUE C — Contraste multi-lenguaje

---

### [F-12] Go: errors as values

@tipo: codigo
@imagen: none

# La filosofía de Go — no hay excepciones

## Decisión de diseño de Go

- Go **no tiene** `try/catch` — fue una decisión deliberada de los diseñadores
- Los errores son **valores** de retorno normales, tipo `error` (interfaz)
- `panic` / `recover` existen pero se usan solo para casos excepcionales reales

## Patrón idiomático Go

```go
// Go — retorno múltiple: (resultado, error)
func fetchUser(id string) (*User, error) {
    resp, err := http.Get("/api/users/" + id)
    if err != nil {
        // Wrap error con contexto usando %w (Go 1.13+)
        return nil, fmt.Errorf("fetchUser: %w", err)
    }
    defer resp.Body.Close()  // defer = equivalente a finally

    if resp.StatusCode == 404 {
        return nil, &UserNotFoundError{ID: id}
    }

    var u User
    if err := json.NewDecoder(resp.Body).Decode(&u); err != nil {
        return nil, fmt.Errorf("decode user: %w", err)
    }
    return &u, nil
}

// Caller — OBLIGADO a manejar el error (o ignorarlo explícitamente con _)
user, err := fetchUser("42")
if err != nil {
    var notFound *UserNotFoundError
    if errors.As(err, &notFound) {  // errors.As unwrap la cadena
        log.Printf("usuario %s no existe", notFound.ID)
        return
    }
    return fmt.Errorf("error inesperado: %w", err)
}
```

## Ventajas e inconvenientes

- ✅ Explícito: el error está visible en la firma de la función
- ✅ Sin stack unwinding — más predecible en performance
- ❌ Verboso: `if err != nil` repetido en cada llamada
- ❌ Fácil de ignorar: `user, _ := fetchUser("42")` silencia el error

---

### [F-13] Kotlin: sealed classes y try-expression

@tipo: codigo
@imagen: none

# Kotlin — exhaustividad en compilación

## sealed class para errores tipados

```kotlin
// Sealed class = union type exhaustiva y verificada por el compilador
sealed class UserResult {
    data class Success(val user: User) : UserResult()
    data class NotFound(val id: String) : UserResult()
    data class NetworkError(val statusCode: Int) : UserResult()
}

// try en Kotlin es una EXPRESIÓN (retorna valor)
fun fetchUser(id: String): UserResult = try {
    val resp = httpClient.get("/api/users/$id")
    when (resp.status) {
        200  -> UserResult.Success(resp.body<User>())
        404  -> UserResult.NotFound(id)
        else -> UserResult.NetworkError(resp.status)
    }
} catch (e: IOException) {
    UserResult.NetworkError(-1)
}
```

## Uso — when es exhaustivo

```kotlin
val result = fetchUser("42")
when (result) {
    is UserResult.Success      -> println(result.user.name)
    is UserResult.NotFound     -> println("No encontrado: ${result.id}")
    is UserResult.NetworkError -> println("Error HTTP ${result.statusCode}")
    // No hay else — el compilador verifica que todos los casos estén cubiertos
}
```

## Diferencias con TypeScript

- Kotlin: **sin checked exceptions** (a diferencia de Java)
- `try` como expresión → integra naturalmente con FP
- `sealed class` = discriminated union del compilador (vs. union types estructurales de TS)

---

### [F-14] Rust: Result\<T,E\> y el operador `?`

@tipo: codigo
@imagen: none

# Rust — sin excepciones en runtime por diseño

## Filosofía de Rust

- Rust garantiza que **no existen excepciones en runtime** (excepto `panic!` explícito)
- Toda operación fallable retorna `Result<T, E>` — el tipo fuerza el manejo en el compilador
- El operador `?` azucariza la propagación

## Implementación

```rust
// Definir errores del dominio
#[derive(Debug)]
enum FetchError {
    Network(reqwest::Error),
    NotFound(String),
    Decode(serde_json::Error),
}

// impl From<reqwest::Error> for FetchError { ... }  → permite usar ?

async fn fetch_user(id: &str) -> Result<User, FetchError> {
    let resp = reqwest::get(format!("/api/users/{id}"))
        .await
        .map_err(FetchError::Network)?;  // ? = propagación implícita

    if resp.status() == 404 {
        return Err(FetchError::NotFound(id.to_string()));
    }

    resp.json::<User>()
        .await
        .map_err(FetchError::Decode)
}
```

## El operador `?` desazucarado

```rust
// Esto:
let resp = reqwest::get(url).await?;

// Es equivalente a:
let resp = match reqwest::get(url).await {
    Ok(val)  => val,
    Err(e)   => return Err(e.into()),
};
```

## Ventajas clave

- ✅ Exhaustividad **garantizada por el compilador** — no podés ignorar un error
- ✅ Sin runtime overhead de stack unwinding
- ✅ `?` hace el código conciso manteniendo la seguridad
- ✅ Drop trait = RAII → limpieza automática sin `finally`

---

### [F-15] Tabla comparativa

@tipo: tabla-comparativa
@imagen: none

# Imperativo vs. Funcional — 4 lenguajes

| Aspecto | TS `throw/catch` | TS `Result<T,E>` | Go `(T, error)` | Kotlin `sealed` | Rust `Result<T,E>` |
|---------|-----------------|-----------------|-----------------|-----------------|-------------------|
| **Mecanismo** | Excepción (throw) | Valor de retorno | Valor de retorno | Expresión (try) | Valor de retorno |
| **Flujo** | Ruptura de stack | Normal | Normal | Normal | Normal |
| **Exhaustividad** | Runtime | Union type TS | Ninguna (ignorable) | Compilador (when) | Compilador (match) |
| **Composabilidad** | Difícil en FP | map/flatMap | Secuencial if/err | Fluida (expr) | ? operator |
| **Stack unwinding** | Sí (costoso) | No | No | Sí (si lanza) | No |
| **Limpieza recursos** | `finally` | Manual | `defer` | `finally` / use | Drop (RAII) |
| **Verbose** | Bajo | Medio | Alto (if err ≠ nil) | Bajo | Bajo (con `?`) |
| **async/Promise** | Natural | `Promise<Result>` | goroutines | `suspend` | `async/await` |

## Regla de selección

- **TS imperativo (`throw`)**: código OO, async/await, equipos con background Java/JS
- **TS funcional (`Result`)**: pipelines de datos, código FP, integración con sistemas agénticos
- **Go**: sistemas de bajo nivel, microservicios, cuando la legibilidad explícita importa
- **Kotlin**: Android, backend JVM donde la exhaustividad en compile time importa
- **Rust**: sistemas, WASM, cuando la seguridad en memoria es crítica

---

## BLOQUE D — Agéntica y cierre

---

### [F-16] Excepciones en programación agéntica

@tipo: concepto-mixto
@imagen: content
@prompt-imagen: diagrama de un pipeline agéntico multi-step: orquestador LLM → tool-call A → tool-call B (falla con ícono rojo) → el error tipado sube al orquestador → decisión: retry o abortar. Flechas y nodos con colores verde/rojo/amarillo

# Por qué el manejo de errores es crítico en sistemas agénticos

## El problema: context poisoning

- Un agente encadena múltiples llamadas a tools (fetch data → process → store)
- Si `fetch` falla silenciosamente (`catch {}` vacío), el agente procesa **datos inconsistentes**
- Los pasos siguientes actúan sobre un estado corrupto → **el agente alucina resultados**

## MCP Protocol y errores tipados

```typescript
// MCP spec (Anthropic 2024): las tools deben retornar errores estructurados
interface ToolResult {
  content: Array<{ type: "text" | "image", text?: string }>
  isError?: boolean  // true = el agente sabe que falló
}

// Tool que usa Result internamente pero expone MCP
async function eduSearchTool(query: string): Promise<ToolResult> {
  const result = await searchKnowledge(query)  // retorna Result<T,E>

  if (!result.ok) {
    return {
      isError: true,
      content: [{ type: "text", text: `Error: ${result.error.message}` }]
    }
  }
  return {
    content: [{ type: "text", text: JSON.stringify(result.value) }]
  }
}
```

## Retry con backoff — patrón agéntico

```typescript
async function withRetry<T>(
  fn: () => Promise<Result<T, Error>>,
  maxAttempts = 3
): Promise<Result<T, Error>> {
  for (let i = 0; i < maxAttempts; i++) {
    const result = await fn()
    if (result.ok) return result
    if (!isRetryable(result.error)) return result  // error no recuperable
    await sleep(2 ** i * 200)  // exponential backoff
  }
  return { ok: false, error: new MaxRetriesError(maxAttempts) }
}
```

## Conexión con esta cátedra

- `publish_loop.py` de EDU usa exactamente este patrón: retry hasta 3 veces, registra errores en `error-registry.jsonl`
- `edu-mcp-server` retorna `isError: true` cuando ChromaDB falla — el agente sabe cómo reaccionar

`[insight cátedra — programación agéntica con MCP (Anthropic 2024)]`

---

### [F-17] Cierre y puntos clave

@tipo: cierre
@imagen: background
@prompt-imagen: imagen conceptual de cierre con red de conceptos: excepción, handler, propagación, terminación, Result, agéntica — conectados con líneas sobre fondo oscuro con gradiente azul-verde

# Manejo de Excepciones — Lo que se lleva hoy

## Los 5 puntos que no podés olvidar

1. **Excepción = evento anómalo en runtime** — no es un bug, es una condición que el código normal no maneja (Sebesta §14.1)

2. **El modelo de terminación domina** — al lanzar, el scope se termina. No hay vuelta al punto del raise (Sebesta p. 612)

3. **Propagación sube el stack** — si no hay handler local, sube al llamador hasta encontrar uno o terminar el programa

4. **Dos filosofías de diseño**:
   - Imperativo (`throw`): expresivo, natural en async, estándar OO
   - Funcional (`Result`): composable, exhaustivo en tipos, esencial en sistemas agénticos

5. **En programación agéntica**: los errores no manejados envenenan el contexto — siempre tipar y propagar errores en tools MCP

## Conexiones curriculares

- **← Tema 11**: excepciones como control de flujo no lineal
- **← Tema 5**: `Result<T,E>` es la mónada Either
- **→ Tema 13**: cómo las excepciones cruzan límites de módulos

## Próxima clase

**Tema 13 — Abstracción Procedural y Modularidad**
Cómo los módulos encapsulan no solo datos, sino también contratos de error.
