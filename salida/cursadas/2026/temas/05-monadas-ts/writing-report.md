# Writing Report — Tema 05: Mónadas en TypeScript

> **Agente:** writing-validator 🔎
> **Course ID:** paradigmas-2026
> **Fecha:** 2026-04-10
> **Documentos analizados:** diseno.md · minuta.md · filminas.md · guia-estudio.md · guiaprofesor.md
> **Alcance:** errores de escritura únicamente (ortografía, gramática, estilo, puntuación). No se tocó contenido temático ni técnico.

---

## Resumen Ejecutivo

| Tipo | Cantidad |
|---|---|
| 🔴 CRÍTICO | 1 |
| 🟠 ERROR | 1 |
| 🟡 MEJORA | 12 |
| **TOTAL** | **14** |

---

## Hallazgos por Documento

### diseno.md — 4 hallazgos

| ID | Tipo | Línea | Texto original | Sugerencia |
|---|---|---|---|---|
| W-01 | 🔴 CRÍTICO ✅ APLICADO | 77–139 | `Analogía del contenedor: \`of\` envuelPlease choose one (or "q" to quit): 2\nLaunching lib/main.dart...` (63 líneas de salida de terminal Flutter/Dart insertadas en medio de la oración) | Eliminar todo el bloque de salida de terminal (líneas 77–139). Texto original recuperable: `Analogía del contenedor: \`of\` envuelve, \`flatMap\` abre-transforma-reenvuelve.` |
| W-03 | 🟡 MEJORA ✅ APLICADO | 28 | `REPL — vista en T04` | → `REPL — vistas en T04` (concordancia con los ítems enumerados: sintaxis, colecciones, REPL) |
| W-04 | 🟡 MEJORA ✅ APLICADO | 53 | `en una o dos slides comparativas` | → `en una o dos filminas comparativas` (terminología inconsistente con el resto del documento) |
| W-05 | 🟡 MEJORA ✅ APLICADO | 299 | `Todos los ejemplos Clojure vienen pre-armados en el REPL` | → `Todos los ejemplos en Clojure vienen pre-cargados en el REPL` ("pre-armados" no es natural; "pre-cargados" o "preparados" es más apropiado) |

---

### minuta.md — 2 hallazgos

| ID | Tipo | Línea | Texto original | Sugerencia |
|---|---|---|---|---|
| W-06 | 🟡 MEJORA ✅ APLICADO | 758 | `por el aplanamiento automático en edge cases con \`then\`` | → `por el aplanamiento automático en casos límite con \`then\`` (anglicismo innecesario) |
| W-07 | 🟡 MEJORA ✅ APLICADO | 775 | `Es la List monad — no determinismo.` | → `Es la List monad — no-determinismo.` (se requiere guion; o mejor: `indeterminismo`) |

---

### filminas.md — 1 hallazgo

| ID | Tipo | Línea | Texto original | Sugerencia |
|---|---|---|---|---|
| W-08 | 🟡 MEJORA ✅ APLICADO | 186 | `\`flatMap\` / \`bind\` / \`>>=\`: encadenar una función que ya devuelve un contexto, aplanando` | → `…encadenar una función que ya devuelve un contexto, aplanando el resultado` (el bullet en la filmina termina abruptamente sin complemento) |

---

### guia-estudio.md — 3 hallazgos

> Se aplicó validación adicional de claridad y accesibilidad para alumnos.

| ID | Tipo | Línea | Texto original | Sugerencia |
|---|---|---|---|---|
| W-09 | 🟡 MEJORA ✅ APLICADO | 14 | `Se basa en el alcance aprobado en [diseno.md](diseno.md), la secuencia didáctica de [minuta.md](minuta.md) y el mapa visual de [filminas.md](filminas.md).` | Jerga y links docentes internos expuestos al alumno. Reemplazar por: `Se basa en el programa de la materia y la secuencia de contenidos de la clase.` |
| W-10 | 🟡 MEJORA ✅ APLICADO | 584 | `mejora testabilidad: podemos inspeccionar y componer programas sin ejecutarlos` | → `mejora la capacidad de prueba: podemos inspeccionar y componer programas sin ejecutarlos` ("testabilidad" es un neologismo que puede resultar opaco para el alumno) |
| W-11 | 🟡 MEJORA ✅ APLICADO | 980 | `Clasifiquen estas APIs según la mónada que modelan:` | → `Clasificá estas APIs según la mónada que modelan:` (inconsistencia de registro verbal: el documento usa voseo singular — "Respondé", "Implementá", "Revisá" — y aquí cambia a tuteo plural) |

---

### guiaprofesor.md — 4 hallazgos

| ID | Tipo | Línea | Texto original | Sugerencia |
|---|---|---|---|---|
| W-02 | 🟠 ERROR ✅ APLICADO | 204 | `Alumnos confundidos en F-06 (map vs flatMap)` | → `Alumnos confundidos en F-06c (map vs flatMap)`. F-06 es la analogía del sobre certificado; la explicación técnica de `map` vs `flatMap` corresponde a F-06c. La referencia incorrecta puede desorientar al docente en clase. |
| W-12 | 🟡 MEJORA ✅ APLICADO | 45 | `Control de scope (evitar desvíos)` | → `Control de alcance (evitar desvíos)` (anglicismo evitable) |
| W-13 | 🟡 MEJORA ✅ APLICADO | 227 | `Están fuera de scope de este tema` | → `Están fuera del alcance de este tema` (mismo anglicismo) |
| W-14 | 🟡 MEJORA ✅ APLICADO | 194 | `requieren overhead conceptual que no todos los equipos aceptan` | → `requieren sobrecarga conceptual que no todos los equipos aceptan` (traducción directa disponible) |

---

## Resumen por Documento

| Documento | CRÍTICO | ERROR | MEJORA | Total |
|---|---|---|---|---|
| diseno.md | 1 | 0 | 3 | **4** |
| minuta.md | 0 | 0 | 2 | **2** |
| filminas.md | 0 | 0 | 1 | **1** |
| guia-estudio.md | 0 | 0 | 3 | **3** |
| guiaprofesor.md | 0 | 1 | 3 | **4** |
| **TOTAL** | **1** | **1** | **12** | **14** |

---

## Notas

- **W-01 requiere intervención urgente:** el bloque de texto corrupto en diseno.md (líneas 77–139) incluye output de terminal Flutter de otro proyecto (`parksense_app`), stack traces de Dart y URLs de debug. No pertenece al documento. El `writing-fixer` debe eliminarlo y restaurar la frase original.

- **W-02 puede causar confusión operativa:** la señal de alerta en guiaprofesor.md apunta a F-06 (analogía), cuando el contenido conflictivo (diferencia `map`/`flatMap`) está en F-06c. El docente que consulte la guía de alerta podría buscar la filmina equivocada durante la clase.

- **guia-estudio.md general:** la redacción es clara, accesible y consistente en voseo. No se detectó jerga interna docente más allá de lo señalado en W-09. Los ejemplos de código están bien contextualizados para el alumno. Nivel apropiado para 4° año de Licenciatura en Sistemas.

---

> Próximo paso: pasar este reporte al agente `writing-fixer ✏️` para aplicar las correcciones.
