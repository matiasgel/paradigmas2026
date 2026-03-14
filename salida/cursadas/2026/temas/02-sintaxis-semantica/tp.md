# Trabajo Práctico — Tema 02: Sintaxis y Semántica de Lenguajes

> **Estado:** BORRADOR
> **Tipo:** Repo GitHub Classroom (autograding)
> **Agente:** Aux. Valeria 📝 (tp-designer)
> **Fecha:** 2026-03-10
> **Tema Nº:** 02 — Sintaxis y Semántica de Lenguajes
> **Trazabilidad:** minuta.md Bloques 1, 2, 3 y 6

---

## Instrucciones generales

- El TP se resuelve de forma **individual**.
- Entregá un único archivo `.md` o `.pdf` con tus respuestas. Para los ejercicios de árbol podés incluir una foto de papel o un diagrama digital.
- Cada ejercicio indica el puntaje. Total: **100 puntos**.
- No está permitido usar generadores automáticos de árboles sintácticos ni parsers en línea para los ejercicios 1–4. El ejercicio 5 **requiere** usar un LLM.

---

## Parte I — EBNF y gramáticas formales (60 puntos)

### Ejercicio 1 — Lectura de gramática (10 puntos)

Dada la siguiente gramática BNF:

```
<programa>   ::= <sentencia> { <sentencia> }
<sentencia>  ::= <asignación> | <condicional>
<asignación> ::= <id> "=" <expr> ";"
<condicional>::= "if" "(" <expr> ")" <sentencia>
               | "if" "(" <expr> ")" <sentencia> "else" <sentencia>
<expr>       ::= <id> | <número> | <expr> "+" <expr> | <expr> "*" <expr>
<id>         ::= "a" | "b" | "c"
<número>     ::= "0" | "1" | "2"
```

**a)** Indicá si cada una de las siguientes cadenas pertenece al lenguaje definido por la gramática. Justificá en una línea:

| Cadena | ¿Pertenece? | Justificación |
|--------|-------------|---------------|
| `a = 1 + b ;` | | |
| `if ( a ) b = 2 ;` | | |
| `if ( 1 ) a = b ; else c = 0 ;` | | |
| `a = d ;` | | |

**b)** ¿Qué característica de la gramática hace que `a = d ;` no pertenezca al lenguaje? Respondé en una oración.

---

### Ejercicio 2 — Derivación y árbol sintáctico (20 puntos)

Usando la gramática del Ejercicio 1:

**a)** Derivá la cadena `a = b + 1 ;` paso a paso, indicando en cada paso qué regla se aplica. Usá el formato de tabla visto en clase:

| Forma de sentencia | Regla aplicada |
|-------------------|----------------|
| `<programa>` | — |
| … | … |

**b)** Dibujá el árbol sintáctico completo para la misma cadena. Podés dibujarlo a mano y subir una foto, o representarlo en texto con indentación.

---

### Ejercicio 3 — Ambigüedad (15 puntos)

La regla `<expr> ::= <expr> "+" <expr> | <expr> "*" <expr> | <id> | <número>` es ambigua.

**a)** Mostrá dos árboles de derivación distintos para la expresión `a + b * c`. Dibujá ambos.

**b)** ¿Cuál de los dos árboles corresponde al comportamiento matemático esperado (multiplicación con mayor precedencia que suma)? Explicá por qué.

**c)** Proponé una modificación a la gramática que resuelva la ambigüedad codificando las precedencias. No hace falta que sea perfecta — lo importante es que la idea sea correcta.

---

### Ejercicio 4 — Escribir EBNF (15 puntos)

Escribí una gramática EBNF para el siguiente mini-lenguaje de consulta simplificado.

**Reglas del lenguaje:**
- Una consulta siempre empieza con `SELECT`
- Le sigue una lista de campos separados por comas: al menos uno, puede haber varios
- Un campo es un identificador: secuencia de letras minúsculas
- Luego viene `FROM` seguido de un identificador (nombre de tabla)
- Opcionalmente puede terminar con `WHERE` seguido de una condición simple: `<campo> = <valor>` donde valor es un número entero

**Ejemplos válidos:**
```
SELECT nombre FROM personas
SELECT nombre, edad FROM personas WHERE edad = 30
SELECT a, b, c FROM tabla
```

Escribí la gramática EBNF completa usando la notación vista en clase: `[ ]` para opcional, `{ }` para repetición, `|` para alternativas.

---

## Parte II — LLMs con y sin restricción gramatical (40 puntos)

### Ejercicio 5 — Experimento: instrucción vs. gramática (40 puntos)

En clase vimos que una gramática EBNF puede usarse como restricción sobre la generación de un LLM (*constrained decoding*). En este ejercicio vas a experimentar en vivo la diferencia entre darle una instrucción en texto vs. darle un esquema estructurado.

---

### Parte A — Sin esquema explícito (10 puntos)

Ingresá el siguiente prompt *exactamente como está* en una conversación nueva con ChatGPT. Ejecutalo **tres veces** en conversaciones separadas.

```
Extraé los datos del siguiente texto y devolvé el resultado.

Texto: "El producto 'Teclado mecánico' tiene un precio de 45000 pesos
y hay 12 unidades en stock. Fue agregado el 5 de marzo de 2026."
```

**Completá la tabla** con los tres resultados obtenidos:

| Run | Formato de la respuesta | ¿Los tipos de dato son consistentes? |
|-----|-------------------------|--------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |

**Respondé:** ¿Cuántos formatos distintos obtuviste? ¿Qué tipos de dato usó el modelo para `precio`, `stock` y `fecha` en cada caso?

---

### Parte B — Con esquema en el prompt (15 puntos)

Usá este prompt en una conversación nueva:

```
Extraé los datos del siguiente texto. Respondé ÚNICAMENTE con un objeto JSON válido.
Sin texto adicional, sin explicaciones, sin bloques de código markdown.
El JSON debe tener exactamente esta estructura:
{
  "nombre": <string>,
  "precio": <number>,
  "stock": <number>,
  "fecha": <string con formato YYYY-MM-DD>
}

Texto: "El producto 'Teclado mecánico' tiene un precio de 45000 pesos
y hay 12 unidades en stock. Fue agregado el 5 de marzo de 2026."
```

Ejecutalo **tres veces** en conversaciones separadas.

**Completá la tabla:**

| Run | ¿El JSON es válido? | ¿`precio` es number? | ¿`fecha` tiene formato YYYY-MM-DD? | ¿Hay texto extra fuera del JSON? |
|-----|---------------------|----------------------|------------------------------------|----------------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Respondé:** ¿El modelo siempre respetó el esquema? Si alguna vez no lo hizo, ¿en qué se desvió?

---

### Parte C — Texto ambiguo: límite de la instrucción (15 puntos)

Usá el mismo prompt de la Parte B, pero reemplazá el texto por este:

```
Texto: "El teclado ese que vimos cuesta como cuarenta y pico de miles.
No sé bien cuándo lo cargaron, creo que fue la semana pasada. Quedan pocos."
```

Ejecutalo tres veces y respondé:

1. ¿Qué devolvió el modelo para `precio`? ¿Fue un `number` válido, una aproximación, o `null`?
2. ¿Qué devolvió para `fecha`? ¿Pudo inferir una fecha concreta en formato `YYYY-MM-DD`?
3. ¿Qué devolvió para `stock`? ¿Inventó un número, puso `null`, o se desvió del esquema?
4. ¿El modelo "alucinó" algún dato (inventó un valor que no está en el texto)? Describí el caso si lo hubo.

**Reflexión final (obligatoria):**

En 4 a 6 oraciones, explicá la diferencia entre:
- Darle una **instrucción en texto** al modelo ("respondé con este formato")
- Tener un **autómata compilado desde una gramática** que bloquea tokens inválidos
y
¿Por qué la instrucción puede fallar con texto ambiguo pero la gramática no? Usá los conceptos de sintaxis, semántica e interpretación vistos en clase.

---
y
## Criterios de evaluación

| Ejercicio | Puntaje | Criterio principal |
|-----------|---------|-------------------|
| 1a — pertenencia (4 filas) | 6 | Corrección + justificación en una línea |
| 1b — característica | 4 | Identificya que `d` no está en `<id>` |
| 2a — derivación | 10 | Tabla completa con reglas correctas en cada paso |
| 2b — árbol | 10 | Estructura jerárquica correcta |
| 3a — dos árboles | 8 | Ambos árboles distintos y sintácticamente válidos |
| 3b — precedencia | 4 | Identifica el árbol correcto y justifica |
| 3c — gramática sin ambigüedad | 3 | Idea correcta aunque no perfecta |
| 4 — EBNF propia | 15 | Cubre todos los casos, notación correcta |
| 5A — sin esquema | 10 | Tabla completa, observación de variación de formato |
| 5B — con esquema | 15 | Tabla completa, análisis de consistencia |
| 5C — texto ambiguo + reflexión | 15 | Reflexión conecta instrucción vs. gramática con conceptos de clase |
| **Total** | **100** | |

---

## Trazabilidad a minuta.md

| Ejercicio | Bloque de la minuta | Concepto |
|-----------|---------------------|----------|
| 1 | Bloque 3 | BNF: leer gramática, terminales/no terminales, pertenencia al lenguaje |
| 2 | Bloque 3 | Derivación con tabla de reglas aplicadas, árbol sintáctico |
| 3 | Bloque 3 | Ambigüedad: dos árboles, precedencia de operadores, solución en gramática |
| 4 | Bloque 3 | EBNF: `[ ]`, `{ }`, escritura de gramática propia desde especificación |
| 5 | Bloque 6 | Constrained decoding, instrucción en texto vs. autómata gramatical, demo ChatGPT |
