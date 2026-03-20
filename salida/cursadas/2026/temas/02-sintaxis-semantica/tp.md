# TP 02 — Sintaxis y Semántica: BNF, EBNF y Análisis

> **Estado:** GENERADO
> **Agente:** Aux. Valeria 📝 (tp-designer)
> **Fecha:** 2026-03-20
> **Tipo:** Quiz Moodle — 40 preguntas de opción múltiple
> **Trazabilidad:** `minuta.md` Bloques 1–4 (F-02 a F-23) + Bloque 6 (F-32, F-33)
> **Archivo Moodle:** `tp-quiz.gift`
> **Configuración Moodle:** `tp-quiz-moodle-config.md`

---

## Datos del trabajo práctico

| Campo             | Valor |
|-------------------|-------|
| **Materia**       | Paradigmas y Lenguajes de Programación 2026 |
| **Institución**   | Universidad Nacional de Tierra del Fuego — IDEI |
| **Tema**          | 02 — Sintaxis y Semántica de Lenguajes |
| **Modalidad**     | Individual · Quiz Moodle |
| **Extensión**     | 40 preguntas de opción múltiple |
| **Duración**      | 60 minutos (práctica formativa) |
| **Énfasis**       | BNF, EBNF y análisis de gramáticas formales |

---

## Objetivos de aprendizaje evaluados

1. **Léxico:** Identificar categorías de tokens, lexemas y la función del analizador léxico.
2. **Sintaxis vs. semántica:** Clasificar errores de compilación/runtime en las categorías correctas.
3. **BNF — Lectura:** Interpretar producciones BNF, identificar terminales y no-terminales.
4. **BNF — Derivaciones:** Realizar derivaciones paso a paso y construir árboles sintácticos.
5. **Ambigüedad:** Detectar gramáticas ambiguas y entender cómo resolverlas.
6. **EBNF:** Leer e interpretar los metasímbolos `[...]`, `{...}`, `(a|b)` y comparar con BNF.
7. **Aplicaciones:** Conectar BNF/EBNF con compiladores reales, `tsc`, Python y constrained decoding.

---

## Gramáticas de referencia

Las siguientes gramáticas se usan a lo largo del quiz. Se muestran también en las preguntas individuales cuando corresponde.

### Gramática G1 — Mini-lenguaje de asignación (Sebesta Cap. 3)

```
<assign> ::= <id> := <expr>
<id>     ::= A | B | C
<expr>   ::= <expr> + <term> | <expr> - <term> | <term>
<term>   ::= <term> * <factor> | <factor>
<factor> ::= ( <expr> ) | <id>
```

**Propiedades de G1:**
- Terminales: `:=`, `+`, `-`, `*`, `(`, `)`, `A`, `B`, `C`
- No-terminales: `<assign>`, `<id>`, `<expr>`, `<term>`, `<factor>`
- Símbolo inicial: `<assign>`
- `*` tiene mayor precedencia que `+`/`-` (estratificación de niveles)
- `<expr>` es recursiva izquierda (asociatividad izquierda para `+`/`-`)

### Gramática G2 — Lista simple (BNF)

```
<lista> ::= <elem> | <lista> , <elem>
<elem>  ::= a | b | c
```

### Gramática G3 — Sentencias con EBNF

```
stmt   ::= 'if' '(' expr ')' stmt ['else' stmt] | id ':=' expr
expr   ::= term { ('+' | '-') term }
term   ::= factor { '*' factor }
factor ::= '(' expr ')' | id | number
id     ::= letter { letter | digit }
number ::= digit { digit }
```

---

## Distribución de secciones (40 preguntas)

| Sección | Contenido | Preguntas | Filminas relacionadas |
|---------|-----------|-----------|----------------------|
| A | Análisis Léxico | Q01–Q05 | F-07 a F-11 |
| B | Sintaxis vs. Semántica | Q06–Q10 | F-02 a F-06b |
| C | BNF — Conceptos y Lectura | Q11–Q17 | F-12 a F-15 |
| D | BNF — Derivaciones y Árboles | Q18–Q24 | F-16 a F-17 |
| E | Ambigüedad | Q25–Q28 | F-18 |
| F | EBNF | Q29–Q36 | F-19 a F-20 |
| G | Aplicaciones | Q37–Q40 | F-30, F-32, F-34 |

---

## Notas pedagógicas

- **Énfasis BNF/EBNF:** 26 de 40 preguntas (65%) trabajan directamente sobre derivaciones, lectura de gramáticas, EBNF o ambigüedad.
- **Preguntas basadas en problemas:** Los alumnos deben aplicar las reglas de G1 para determinar si cadenas son válidas, cuántos pasos requiere una derivación, qué producciones se usaron, y cómo se resuelve la ambigüedad.
- **Feedback formativo:** Todas las preguntas incluyen feedback por alternativa y feedback general en el archivo GIFT.
- **Distractores plausibles:** Cada pregunta tiene al menos 3 distractores que reflejan errores conceptuales frecuentes detectados en cursos anteriores.

---

## Artefactos generados

| Archivo | Descripción |
|---------|-------------|
| `tp-quiz.gift` | Banco de 40 preguntas en formato GIFT para importar a Moodle 5 |
| `tp-quiz-moodle-config.md` | Guía operativa para crear la actividad Quiz en Moodle 5 |
