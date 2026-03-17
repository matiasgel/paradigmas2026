# Coherence Report — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Agente:** coherence-fixer 🔗 (modo detección)
> **Fecha:** 2026-03-10
> **Prerequisito:** Loop 1 completado (writing-report.md + 3 fixes aplicados)
> **Documentos validados:** `diseno.md` · `minuta.md` · `filminas.md` · `guia-estudio.md` · `tp.md`
> **Estado:** COMPLETO — 1 ERROR · 2 IMPROVEMENT

---

## Resumen ejecutivo

| Nivel | ID | Archivos afectados | Descripción |
|-------|----|--------------------|-------------|
| [ERROR] | COH-01 | tp.md | Referencia a filmina incorrecta (29 en vez de 30) |
| [IMPROVEMENT] | COH-02 | filminas.md vs guia-estudio.md | Portabilidad: en guia pero no en filminas F-11 |
| [IMPROVEMENT] | COH-03 | filminas.md vs guia-estudio.md | Smalltalk ausente en F-09 OO pero presente en guia §2.5 |

---

## [ERROR] COH-01 — Trazabilidad incorrecta en tp.md P01: "F-18" debe ser "F-19"

**Archivo:** `tp.md`
**Línea aprox.:** 39
**Descripción:** La pregunta P01 del TP indica como trazabilidad `"Bloque 4 — F-18, demo en vivo de error de tipos"`. Sin embargo, según la `minuta.md` (línea 341) y `filminas.md`, el demo de tipos y el error `Argument of type 'string[]' is not assignable to parameter of type 'number[]'` corresponden a la sección **F-19 (Sistema de tipos básico)**.

- **F-18** = "El mismo problema: funcional en TypeScript" (`arr.map().reduce()`) — sin trazabilidad con el error de tipos.
- **F-19** = "Sistema de tipos básico" → aquí aparece `sumaAbs(["hola", "mundo"])` y el mensaje de error.

**Evidencia:**
- `minuta.md` línea 341: `### Sistema de tipos básico de TypeScript *(📽 F-19)* (8 min)` → en esta sección aparece la instrucción "Mostrar el error en vivo: sumaAbs(["hola", "mundo"]);"
- `filminas.md` [F-19]: contiene el bloque de código con el error de asignación de tipos

**Texto incorrecto:**
```
**Trazabilidad:** Bloque 4 — 29, demo en vivo de error de tipos
```

**Corrección:**
```
**Trazabilidad:** Bloque 4 — F-19, demo en vivo de error de tipos
```

---

## [IMPROVEMENT] COH-02 — Criterios "al subir en la escalera": guia agrega Portabilidad, filminas no

**Archivos:** `filminas.md` (F-11) vs `guia-estudio.md` (Sección 3.1)
**Descripción:** La filmina F-11 lista lo que se gana al subir en la escalera de abstracciones como solo "más legibilidad, más escribibilidad". La guía de estudio Sección 3.1 en cambio lista tres ventajas: "Legibilidad, Escribibilidad, **Portabilidad**".

El criterio de portabilidad es pedagógicamente válido y no es incorrecto, pero un alumno que compare la filmina con la guía puede notar la diferencia.

**filminas F-11 (actual):**
```
**Al subir:** más legibilidad, más escribibilidad
**Al bajar:** más control, más eficiencia
```

**guia-estudio.md Sección 3.1 (actual):**
```
Al subir se gana:
- Legibilidad
- Escribibilidad
- Portabilidad (menos dependencia del hardware)
Al bajar se gana:
- Control
- Eficiencia
```

**Opciones para el docente:**
- **Opción A** (recomendada): agregar "Portabilidad" a la filmina F-11 para coincidir con la guía. Pedagógicamente correcto y alinea los documentos.
- **Opción B**: quitar Portabilidad de guia-estudio.md para reducir al mínimo (solo lo que se mostró en clase).

---

## [IMPROVEMENT] COH-03 — Smalltalk en paradigma OO: ausente en F-09, presente en guia §2.5

**Archivos:** `filminas.md` (F-09) vs `guia-estudio.md` (Sección 2.5)
**Descripción:** (Vinculado a IMP-02 del writing-report.md)
La tabla de los 4 paradigmas en la filmina F-09 lista como ejemplos del paradigma OO: `Java, C#, Dart`. La guía de estudio §2.5 incluye `Smalltalk` como primer ejemplo: `Java, C#, Smalltalk, Dart`.

Smalltalk es mencionado como el "lenguaje OO puro original" en el cuerpo de minuta.md, diseno.md y guia-estudio.md, por lo que su ausencia en la filmina es inconsistente.

**Opciones para el docente:**
- **Opción A** (recomendada): agregar Smalltalk a la columna de ejemplos de OO en filminas F-09.
- **Opción B**: eliminar Smalltalk de la columna de guia-estudio y dejarla como la filmina.

---

## Verificaciones que NO encontraron problemas

| Check | Resultado |
|-------|-----------|
| Referencias F-XX en guia-estudio.md | ✅ La guía no cita filminas por número — sin referencias rotas |
| Numeración de filminas minuta ↔ filminas.md | ✅ F-00 a F-28 coinciden en ambos documentos (29 filminas) |
| Output de ejemplos de código TypeScript | ✅ `sumaAbs([3, -1, 4, -1, 5])` → `14` en todos los documentos |
| Terminología "paradigma imperativo" | ✅ Consistente en los 5 documentos |
| Pipeline TypeScript `.ts → tsc → .js → V8` | ✅ Consistente en minuta, filminas, guia, tp |
| Cita arXiv Schmidt & Runfola (2511.17696) | ✅ Consistente en minuta, filminas y guia |
| Referencia al "cuello de botella de Von Neumann" | ✅ Consistente en todos los documentos (F-08, guia §2.3, minuta Bloque 2) |
| Mención del reemplazo de Kotlin por TypeScript | ✅ Consistente en diseno, minuta, filminas y guia |

---

## Próximo paso

**Loop 2b:** aplicar COH-01 automáticamente en `tp.md`.
COH-02 y COH-03 quedan pendientes de decisión del docente.
