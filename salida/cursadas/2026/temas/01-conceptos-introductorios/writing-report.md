# Writing Report — Tema 01: Conceptos Introductorios + Intro a TypeScript

> **Agente:** writing-validator 🔎
> **Fecha:** 2026-03-10
> **Documentos validados:** `diseno.md` · `minuta.md` · `filminas.md` · `guia-estudio.md` · `tp.md`
> **Estado:** COMPLETO — 2 CRITICAL · 1 ERROR · 2 IMPROVEMENT

---

## Resumen ejecutivo

| Nivel | Cantidad | Documentos afectados | Acción |
|-------|----------|---------------------|--------|
| [CRITICAL] | 2 | guia-estudio.md | Auto-fix (writing-fixer) |
| [ERROR] | 1 | guia-estudio.md | Auto-fix (writing-fixer) |
| [IMPROVEMENT] | 2 | diseno.md · guia-estudio.md | Requiere aprobación del docente |

---

## [CRITICAL] Errores críticos — auto-fix

### CRIT-01 — Tildes faltantes: "Anos" → "Años" (×4)

**Archivo:** `guia-estudio.md`
**Sección:** Bloque 2, Section 2.4 — tabla de evolución metodológica
**Descripción:** Cuatro filas de la tabla histórica omiten la tilde en "Años", escribiéndolo como "Anos".

| Ocurrencia | Texto incorrecto | Corrección |
|------------|-----------------|-----------|
| Fila 1 | `Anos 70` | `Años 70` |
| Fila 2 | `Anos 80` | `Años 80` |
| Fila 3 | `Anos 80` | `Años 80` |
| Fila 4 | `Anos 90` | `Años 90` |

---

### CRIT-02 — Texto en inglés en documento en español

**Archivo:** `guia-estudio.md`
**Sección:** Bloque 4, Sección 4.5 "TypeScript como 'acelerador de paradigma'"
**Descripción:** Una oración está íntegramente en inglés dentro de un documento académico en español. Viola el idioma de salida del documento y la formalidad académica.

**Texto incorrecto:**
```
- **Ventaja:** each project can choose the most appropriate style for each problem.
```

**Corrección:**
```
- **Ventaja:** cada proyecto puede elegir el estilo más apropiado para cada problema.
```

---

## [ERROR] Errores — auto-fix

### ERR-01 — Abreviatura no definida "Kt" en tabla de dominios de aplicación

**Archivo:** `guia-estudio.md`
**Sección:** Bloque 2, Sección 2.6 — tabla de dominios de aplicación
**Descripción:** La tabla usa "Kt" (abreviatura de Kotlin) como nombre de lenguaje representativo del paradigma OO. El problema es doble: (1) la abreviatura no está definida ni explicada en ningún lugar del documento; (2) el cursado 2026 reemplazó explícitamente Kotlin por TypeScript, por lo que la presencia de "Kt" es inconsistente con el diseño del tema (`diseno.md`: *"Introducción a TypeScript como lenguaje multiparadigma (reemplaza Kotlin)"*).

**Texto incorrecto:**
```
| OO | Aplicaciones empresariales, GUIs, modelado de dominio complejo | Java, C#, Kt |
```

**Corrección:**
```
| OO | Aplicaciones empresariales, GUIs, modelado de dominio complejo | Java, C#, Kotlin |
```

---

## [IMPROVEMENT] Mejoras — requieren aprobación del docente

### IMP-01 — Inconsistencia de criterios Sebesta: 7 en diseno.md vs. 6 en todos los demás

**Archivo afectado primario:** `diseno.md`
**Archivos afectados secundarios:** `minuta.md`, `filminas.md` (F-04), `guia-estudio.md` (Sección 1.4), `tp.md` (P01)
**Descripción:** `diseno.md` lista 7 criterios de Sebesta (incluyendo "Entorno de programación — editores, depuradores, ecosistema"), mientras que `minuta.md`, `filminas.md`, `guia-estudio.md` y `tp.md` citan explícitamente "los 6 criterios" y no incluyen "Entorno de programación".

Esta divergencia es probablemente intencional (el docente simplificó para la clase), pero podría confundir a un alumno que compare el diseno.md con la guía o las filminas.

**Opciones para el docente:**
- **Opción A** (recomendada): agregar una nota en `diseno.md` aclarando que "Entorno de programación" fue omitido de los materiales de clase por brevedad. `← sin cambios en guia/filminas`
- **Opción B**: actualizar `minuta.md`, `filminas.md` y `guia-estudio.md` para incluir el 7° criterio.
- **Opción C**: eliminar "Entorno de programación" de `diseno.md` para alinear todos los documentos en 6 criterios.

---

### IMP-02 — Columna "lenguajes OO: Smalltalk ausente en tabla filminas (F-09)

**Archivo:** `filminas.md`
**Sección:** F-09 — tabla de 4 paradigmas fundamentales
**Descripción:** La columna "Ejemplos" del paradigma OO en F-09 lista `Java, C#, Dart` pero omite `Smalltalk`, que es mencionado como el lenguaje OO puro original en el cuerpo de `minuta.md`, `diseno.md` y `guia-estudio.md` (Sección 2.5). La inconsistencia es menor pero notable si los alumnos comparan la filmina con la guía.

**Texto actual en F-09:**
```
| **OO** | Imperativo + encapsulamiento | Objeto / mensaje | Mutable (encapsulado) | Java, C#, Dart |
```

**Sugerencia:**
```
| **OO** | Imperativo + encapsulamiento | Objeto / mensaje | Mutable (encapsulado) | Smalltalk, Java, C#, Dart |
```

---

## Estado por documento

| Documento | Estado escribura | Issues |
|-----------|-----------------|--------|
| `diseno.md` | ✅ Sin errores críticos | IMP-01 (coherencia con otros docs) |
| `minuta.md` | ✅ Sin errores | — |
| `filminas.md` | ✅ Sin errores | IMP-02 (sugerencia menor) |
| `guia-estudio.md` | ⚠️ Errores encontrados | CRIT-01, CRIT-02, ERR-01 |
| `tp.md` | ✅ Sin errores | — |

---

## Próximo paso

**Loop 1b (writing-fixer):** aplicar CRIT-01, CRIT-02, ERR-01 automáticamente en `guia-estudio.md`.
IMP-01 e IMP-02 quedan pendientes de decisión del docente.
