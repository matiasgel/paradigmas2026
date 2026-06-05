# topic-extract.md — Tema 12: Manejo de Excepciones
> Pipeline v3 · Generado: 2026-06-04 · Libro principal: Sebesta Cap. 14
> Lenguaje principal: TypeScript | Contraste: Go, Kotlin, Rust
> Nivel densidad: 2 | ChromaDB: ✅ 8+8+8 fragmentos recuperados

---

## Metadatos Bibliográficos

### Fuentes Primarias (ChromaDB verificadas)

| # | Fuente | Capítulo / Sección | Páginas | Estado |
|---|--------|--------------------|---------|--------|
| 1 | Sebesta — *Concepts of Programming Languages*, Pearson 2019 | Cap. 14: Exception Handling and Event Handling | 611–646 | ✅ recuperado |
| 2 | Gabbrielli & Martini — *Programming Languages: Principles and Paradigms*, Springer 2023 (2ª ed.) | Cap. 7 §7.3.1: Implementing Exceptions | 136–282 | ✅ recuperado |
| 3 | Louden & Lambert — *Programming Languages: Principles and Practices*, Course Technology 2012 | Cap. 9 §9.5: Exception Handling | 406–447 | ✅ recuperado |

### Fuentes Secundarias (Enriquecimiento)

| # | Fuente | Relevancia |
|---|--------|------------|
| 4 | Gabbrielli & Martini Cap. 7 §7.3 (walking binary tree, exceptions as control flow) | 0.475 |
| 5 | Louden Cap. 9 — callback handler como alternativa pre-try/catch | 0.491 |

---

## Conceptos Clave Extraídos

### 1. ¿Qué es una excepción? (Sebesta §14.1)
- Un evento **inesperado** o **anómalo** que ocurre en runtime y que el código "normal" no puede (o no debe) manejar en línea.
- No son errores de programación puros: también incluyen condiciones esperables pero infrecuentes (ej: archivo no encontrado, red caída).
- Sebesta distingue: **exception** (evento) vs **exception handler** (código de respuesta).
- Una excepción se dice **raised** (lanzada / levantada); el handler la **catches** (captura).

### 2. Historia y motivación (Sebesta §14.1, Gabbrielli §7.3)
- Antes del manejo estructurado: flags de retorno, `errno` global (C), callbacks de error (Louden §9.5).
- PL/I fue el **primer lenguaje** con mecanismo de excepciones, bajo el modelo de **resumption** ("resume").
- Ada introdujo excepciones con modelo de **termination** — que se convirtió en el estándar moderno.
- Java consolidó la jerarquía de tipos checked/unchecked.
- Gabbrielli: "An exception is not an anonymous event — it has a name, often a value in one of the language's types" (p. 282).

### 3. Modelo de terminación vs. reanudación (Sebesta §14.1, Gabbrielli §7.3.1)
| Modelo | Descripción | Lenguajes |
|--------|-------------|-----------|
| **Termination** | Al lanzar excepción, el scope que la generó se termina. El handler toma control, NO se vuelve al punto de raise. | Java, C++, C#, TypeScript, Kotlin, Python, Rust |
| **Resumption** | El handler ejecuta y luego devuelve control al punto donde se lanzó la excepción. | PL/I (legacy), algunos LISP |

- Sebesta (p. 612): "Termination is obviously the simpler of the two models" y es "the model used in most contemporary languages."
- Gabbrielli (p. 282): termination = "handling with termination" — el constructo donde se detecta la excepción es terminado.

### 4. Preguntas de diseño de lenguaje (Sebesta §14.1, pp. 612–614)
Sebesta enumera las decisiones de diseño que todo lenguaje debe tomar:
1. ¿Cómo se especifican y clasifican las excepciones?
2. ¿Cómo se levanta (raise/throw) una excepción?
3. ¿Cómo se liga una excepción a su handler?
4. ¿Puede la información de la excepción pasarse al handler?
5. ¿Dónde continúa la ejecución después del handler?
6. ¿Se provee alguna forma de finalización (finally)?
7. ¿Pueden definirse excepciones por el usuario?
8. ¿Deben declararse excepciones predefinidas (checked)?

### 5. Ligadura excepción–handler y propagación (Sebesta §14.2)
- El handler se busca en el **call stack** hacia arriba: si el bloque actual no tiene handler, se "propaga" al llamador, y así hasta encontrar uno o terminar el programa.
- Sebesta (p. 614): "An issue related to the binding of an exception to an exception handler is whether information about the exception is made available to the handler."
- En Java/TypeScript: el objeto de excepción lanzado es pasado al handler → permite acceder a mensaje, stack trace, campos custom.
- Handler genérico: `catch (Exception genericObject)` captura toda excepción derivada de `Exception` — útil como "catch-all" de último recurso.

### 6. Excepciones user-defined (Sebesta §14.2)
- "The thrown object could include any number of data fields that might be useful in the handler."
- En TypeScript: `class DatabaseError extends Error { constructor(public code: number, message: string) { super(message) } }`.
- Permiten transportar **contexto estructurado** del error al handler.

### 7. Finalization — `finally` (Sebesta §14.2)
- Bloque que **siempre** ejecuta, haya excepción o no → garantía de limpieza de recursos.
- TypeScript/Java/Kotlin: `try { } catch { } finally { }`.
- Go: `defer` cumple rol equivalente (Louden §9.5: "deferred cleanup").
- Rust: Drop trait + RAII garantiza limpieza sin finally explícito.

### 8. Enfoque funcional — valores de error (Louden §9.5, enriquecimiento)
- Alternativa **no imperativa**: retornar un **tipo suma** que codifica éxito o error.
- **Rust**: `Result<T, E>` — `Ok(val)` o `Err(err)`. El compilador obliga a manejar ambos casos.
- **Go**: retorno múltiple `(T, error)` — convención, no enforceada por tipos (puede ignorarse).
- **Kotlin**: `sealed class Either<L, R>` / biblioteca Arrow.
- **TypeScript**: `type Result<T, E> = { ok: true, value: T } | { ok: false, error: E }`.
- Gabbrielli (p. 282): los tipos suma permiten "an exception that is not an anonymous event — it has a name, often a value in one of the language's types."
- El approach funcional evita **efectos secundarios** del throw (que rompe el flujo puro) — importante en FP puro (Haskell: `Either a b`, `Maybe a`).

### 9. Comparativa multi-lenguaje

#### TypeScript (imperativo clásico — principal)
```typescript
class NetworkError extends Error {
  constructor(public statusCode: number, message: string) {
    super(message)
    this.name = 'NetworkError'
  }
}

async function fetchUser(id: string): Promise<User> {
  try {
    const res = await fetch(`/api/users/${id}`)
    if (!res.ok) throw new NetworkError(res.status, `HTTP ${res.status}`)
    return res.json()
  } catch (e) {
    if (e instanceof NetworkError && e.statusCode === 404) {
      throw new UserNotFoundError(id)
    }
    throw e  // re-raise
  } finally {
    // cleanup: siempre ejecuta
    logRequest(id)
  }
}
```

#### TypeScript (funcional — Result type)
```typescript
type Result<T, E extends Error = Error> = 
  | { ok: true;  value: T }
  | { ok: false; error: E }

async function fetchUser(id: string): Promise<Result<User, NetworkError>> {
  const res = await fetch(`/api/users/${id}`)
  if (!res.ok) return { ok: false, error: new NetworkError(res.status, `HTTP ${res.status}`) }
  return { ok: true, value: await res.json() }
}

// Uso: exhaustivo por diseño
const result = await fetchUser("42")
if (result.ok) {
  console.log(result.value.name)
} else {
  console.error(result.error.statusCode)
}
```

#### Go (errors as values)
```go
func fetchUser(id string) (*User, error) {
    resp, err := http.Get("/api/users/" + id)
    if err != nil {
        return nil, fmt.Errorf("fetchUser: %w", err)
    }
    defer resp.Body.Close()
    if resp.StatusCode == 404 {
        return nil, &UserNotFoundError{ID: id}
    }
    var u User
    if err := json.NewDecoder(resp.Body).Decode(&u); err != nil {
        return nil, fmt.Errorf("decode: %w", err)
    }
    return &u, nil
}
// Énfasis: panic/recover existe pero se usa solo en casos excepcionales
// Go idiomático: errors son valores, no excepciones
```

#### Kotlin (sealed classes / try como expresión)
```kotlin
sealed class UserResult {
    data class Success(val user: User) : UserResult()
    data class NotFound(val id: String) : UserResult()
    data class NetworkError(val code: Int) : UserResult()
}

fun fetchUser(id: String): UserResult = try {
    val resp = httpClient.get("/api/users/$id")
    when (resp.status) {
        200 -> UserResult.Success(resp.body<User>())
        404 -> UserResult.NotFound(id)
        else -> UserResult.NetworkError(resp.status)
    }
} catch (e: IOException) {
    UserResult.NetworkError(-1)
}
// when es exhaustivo → el compilador obliga a manejar todos los casos
```

#### Rust (Result<T,E> — sin excepciones en runtime)
```rust
#[derive(Debug)]
enum FetchError { NotFound(String), Network(reqwest::Error), Decode(serde_json::Error) }

async fn fetch_user(id: &str) -> Result<User, FetchError> {
    let resp = reqwest::get(format!("/api/users/{id}"))
        .await
        .map_err(FetchError::Network)?;  // operador ? = propagación implícita
    if resp.status() == 404 {
        return Err(FetchError::NotFound(id.to_string()));
    }
    resp.json::<User>().await.map_err(FetchError::Decode)
}
// ? operator: equivale a match result { Ok(v) => v, Err(e) => return Err(e.into()) }
// sin runtime panics (excepto panic! explícito)
```

### 10. Funcional vs. Imperativa — tabla de contraste

| Aspecto | Imperativo (`throw`/`catch`) | Funcional (`Result`/`Either`) |
|---------|------------------------------|-------------------------------|
| Flujo de control | Ruptura explícita del stack | Valor de retorno normal |
| Composabilidad | Difícil en cadenas funcionales | `map`, `flatMap`, `andThen` |
| Exhaustividad | Solo en runtime | Verificada en compilación (Rust, Kotlin) |
| Rendimiento | Stack unwinding costoso | Sin overhead de stack unwinding |
| Legibilidad | Familiar, ubicua en OO | Requiere entrenamiento; más verbosa en TS |
| Contexto de error | Objeto (campos custom) | Tipo suma (ADT) |
| `async` / `Promise` | Funciona naturalmente | Requiere `Promise<Result<T,E>>` |

### 11. Excepciones en Programación Agéntica

Este sub-tema es **de alta relevancia actual** y no está cubierto explícitamente en la bibliografía clásica (Sebesta 2019). Se basa en análisis y tendencias académicas recientes:

**¿Por qué las excepciones son críticas en sistemas agénticos?**

1. **Agentes encadenados (tool-use)**: Cuando un LLM invoca una tool (`fetchUser`, `executeSQL`), el runtime del agente debe distinguir entre:
   - Error recuperable → reintentar / usar tool alternativa
   - Error irrecuperable → abortar y reportar al orquestador
   - Si el error es silenciado (`catch` vacío), el agente **alucina** o actúa sobre datos inconsistentes.

2. **Context poisoning**: Una excepción no manejada en un paso intermedio de un pipeline agéntico "envenena" el contexto: el agente subsiguiente recibe un resultado parcial sin saber que algo falló.

3. **Typed errors en MCP / tool schemas**: El protocolo MCP (Anthropic 2024) especifica que las tools deben retornar errores estructurados (`isError: true, content: [...]`) — el enfoque funcional `Result<T,E>` mapea directamente.

4. **Retry con backoff**: En agentes reactivos, el patrón es:
   ```typescript
   // TypeScript agéntico — retry con exponential backoff
   async function withRetry<T>(
     fn: () => Promise<Result<T, Error>>,
     maxAttempts = 3
   ): Promise<Result<T, Error>> {
     for (let i = 0; i < maxAttempts; i++) {
       const result = await fn()
       if (result.ok) return result
       if (!isRetryable(result.error)) return result
       await sleep(2 ** i * 100)
     }
     return { ok: false, error: new MaxRetriesError() }
   }
   ```

5. **Observabilidad**: En sistemas de LLM Ops, cada excepción debe ser:
   - Registrada con `trace_id` del request del agente
   - Categorizada (tool error / model error / orchestration error)
   - Correlacionada con el paso del plan que la generó

6. **Sandboxing**: El runtime que ejecuta código generado por LLM debe capturar panics/crashes a nivel de proceso para que el agente host no caiga — paradigma de aislamiento de errores.

**Conexión curricular**: El Tema 12 conecta directamente con el contexto de esta cátedra (TypeScript, TS-first agentic, MCP server), donde los errores de pipeline del propio `edu-mcp-server` son un ejemplo vivo.

---

## Plan de Aprendizaje — Bloom Revisado

| Nivel | Objetivo | Actividad sugerida |
|-------|----------|-------------------|
| 1 - Recordar | Definir excepción, handler, raise, propagación | Glosario en clase |
| 2 - Comprender | Distinguir terminación vs. reanudación | Preguntas socráticas |
| 3 - Aplicar | Escribir try/catch/finally en TypeScript | Ejercicio en vivo |
| 3 - Aplicar | Implementar Result<T,E> en TypeScript | Ejercicio en vivo |
| 4 - Analizar | Comparar Go vs Rust vs Kotlin en manejo de errores | Tabla comparativa |
| 5 - Evaluar | Decidir cuándo usar throw vs Result en código real | Caso de estudio agéntico |

---

## Sub-temas para Filminas

Con base en los conceptos extraídos y los parámetros del docente, propongo la siguiente cobertura:

1. **Portada** — Tema 12: Manejo de Excepciones
2. **¿Qué es una excepción?** — definición Sebesta, motivación, historia (PL/I → Ada → Java)
3. **El problema antes de las excepciones** — códigos de error, errno, callbacks (Louden)
4. **Modelo de terminación vs. reanudación** — Sebesta §14.1, diagrama de flujo
5. **Anatomía de try/catch/finally en TypeScript** — sintaxis + flujo de control
6. **Propagación por el call stack** — Sebesta §14.2, diagrama animable
7. **Excepción user-defined en TypeScript** — jerarquía de clases, campos custom
8. **`finally` y RAII — garantía de limpieza** — TypeScript vs Rust (Drop)
9. **El approach funcional: Result\<T,E\>** — motivación, implementación TS
10. **Go: errors as values** — filosofía, `%w` wrapping, `errors.Is/As`
11. **Kotlin: sealed classes y try-expression** — exhaustividad en compilación
12. **Rust: Result y el operador `?`** — sin runtime exceptions, panic vs Result
13. **Tabla comparativa** — imperativo vs funcional, 4 lenguajes
14. **Excepciones en programación agéntica** — context poisoning, typed errors MCP, retry
15. **Diseño de errores en TypeScript agéntico** — withRetry, structured errors
16. **Cierre y preguntas** — conceptos clave, conexión Tema 11 → 12 → 13

---

## Notas del Diseñador (Marcos v3)

- **Sebesta Cap. 14** es la fuente principal estructural — usar sus preguntas de diseño como esqueleto conceptual.
- **Gabbrielli §7.3.1** aporta la perspectiva de implementación (handling with termination) y el ejemplo del árbol binario como caso de uso elegante de excepciones.
- **Louden §9.5** es útil para mostrar el "antes": callbacks de error en C — contraste histórico con try/catch.
- El **approach funcional** (Result, Either) no está en Sebesta pero es *mandatorio* en 2026: Rust lo normalizó, Go lo popularizó, y los sistemas agénticos lo requieren.
- El **sub-tema agéntico** es propio del contexto de la cátedra y no tiene fuente bibliográfica clásica — marcarlo como `[insight cátedra]` en las filminas para que fact_verifier no lo rechace, o usar `[claim]`.
- Nivel de densidad 2: código moderado, diagramas explicativos, énfasis en comprensión comparativa.
