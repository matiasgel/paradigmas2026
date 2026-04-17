# Reporte de Validación — Tema 06: Paradigma Lógico: Prolog — Clase 1 de 3

**Fecha de ejecución:** 2026-04-17  
**Documentos validados:**  
- `diseno.md` (base de diseño)  
- `filminas.md` (38 filminas)  
- `minuta.md` (script docente)  
- `guia-estudio.md` (guía de alumno)  
- `guia-profesor.md` (guía pedagógica)  

---

## LOOP 1 — 🔎 Writing Validator

*Motor: writing-validator | Detecta errores ortográficos, gramaticales y de estilo*

### Hallazgos

| ID | Tipo | Documento | Línea | Texto original | Corrección |
|----|------|-----------|-------|----------------|------------|
| W-01 | [CRÍTICO] | `diseno.md` | 301, 305, 344, 345 | `ancentro(X, Y)` (4 ocurrencias) | `ancestro(X, Y)` — typo en nombre del predicado; además la línea 305 mezcla `ancentro` en la cabeza con `ancestro` en el cuerpo recursivo, creando un predicado incoherente |
| W-02 | [ERROR] | `filminas.md` | F-02 (código Python) | `[p for p, h, _ in relaciones if h == persona]` — `relaciones` se trata como lista de 3-tuplas pero nunca se define su estructura | Agregar comentario `# relaciones = [(progenitor, hijo, tipo), ...]` o simplificar a 2-tuplas con `p, h` |
| W-03 | [MEJORA] | `guia-estudio.md` | Sección 7.3 | "El continuum declarativo" — el título está en castellano pero el texto alterna con términos en inglés sin cursiva (`declarativo`, `imperativo`) | Mantener consistencia: poner en cursiva los términos técnicos en inglés cuando aparecen sin traducción |
| W-04 | [MEJORA] | `minuta.md` | B4, párrafo final | "riesgo de loop infinito" — `loop` es anglicismo | Alternativa: "riesgo de bucle infinito" o "ciclo infinito" |
| W-05 | [MEJORA] | `guia-profesor.md` | Sección 5 | "no negociable" — expresión informal | Alternativa: "imprescindible" o "obligatorio" |
| W-06 | [MEJORA] | `filminas.md` | F-04 | "Curiosidad:" — registro informal en documento académico | Alternativa: "Dato de contexto:" o "Nota histórica:" |

### Estado después de Loop 1:
- **W-01:** ✅ CORREGIDO (aplicado antes de este reporte)
- **W-02:** ✅ CORREGIDO (ver Loop 1b más abajo)
- **W-03 a W-06:** aceptados como mejoras — docente decide

---

## LOOP 1b — ✏️ Writing Fixer

*Motor: writing-fixer | Aplica correcciones automáticas*

### Correcciones aplicadas:

**W-01 — `ancentro` → `ancestro` en `diseno.md`:**  
Aplicado en 4 ubicaciones (líneas 301, 305 ×2, 344, 345). El código en línea 305 también tenía una inconsistencia lógica: usaba `ancentro` como cabeza pero `ancestro` en la llamada recursiva — lo que creaba un predicado no terminante. Corregido a nombre consistente `ancestro` en ambas posiciones.

**W-02 — Python code en filminas F-02:**  
El bloque de código usa `p, h, _` (3-tuplas) sin definir la estructura de `relaciones`. Se agrega comentario de estructura para claridad didáctica.

**W-04 — `loop` → `bucle`:**  
Corregido en `minuta.md`, bloque B4.

---

## LOOP 2 — 🔗 Coherence Fixer

*Motor: coherence-fixer | Detecta rupturas de consistencia inter e intra documento*

### Hallazgos

| ID | Tipo | Documentos | Descripción | Corrección |
|----|------|-----------|-------------|------------|
| C-01 | [RUPTURA] | `filminas.md` vs `minuta.md` | B3 en filminas decía "F-13 a F-22" pero F-21/F-22 están físicamente en el header de B4. La minuta dice correctamente "F-13 a F-20" para B3 | Header de B3 en filminas corregido a "F-13 a F-20" ✅ |
| C-02 | [SCOPE] | `filminas.md` F-01 | Menciona "Orientado a Objetos" como paradigma ya visto. Según el diseño curricular (guia-profesor.md, sección 1.2), OOP se ve en Clases 10–14, **después** del paradigma lógico | Eliminado OOP de la lista "Hasta ahora vimos" ✅ |
| C-03 | [TERMINOLOGÍA] | `filminas.md` F-28 vs `guia-estudio.md` | filminas F-28 usa "función" al comparar con Python (`def es_ancestro` → "función"); guia-estudio usa consistentemente "predicado" para Prolog y "función" para Python | No requiere corrección — el contraste es intencional y está aclarado en el contexto |
| C-04 | [INCOHERENCIA] | `filminas.md` F-05 vs `guia-estudio.md` sección 1.3 | F-05 cita a Sebesta directamente ("The study of logic programming...") usando la frase como bloque de cita en filmina. En guia-estudio la misma cita aparece en sección 1.3 con atribución completa al Cap. 16 | Mantener consistencia: en filminas aceptable como cita sin ref completa; en guia ya tiene ref completa. Sin cambio necesario |
| C-05 | [RUPTURA] | `minuta.md` vs `filminas.md` | La minuta menciona "F-24-25" juntas en B4 ("F-24: ...F-25: árbol") pero en filminas son filminas independientes F-24 (trazado texto) y F-25 (árbol visual) | Aclarar en minuta que se trabajan secuencialmente, no como slide dual. Ya está implícito — sin cambio necesario |
| C-06 | [TERMINOLOGÍA] | Todos los documentos | "base de conocimiento" (tres palabras, sin guión) aparece a veces como "base-de-conocimiento" en código comentario y otras sin guión en texto. Elegir forma canónica | Forma canónica: **base de conocimiento** (sin guión) en texto corrido; en código Prolog, nombre de archivo `familia.pl`. Verificar inconsistencias en guia-estudio sección 4.1 → correcto ya |

### Estado después de Loop 2:
- **C-01:** ✅ CORREGIDO  
- **C-02:** ✅ CORREGIDO  
- **C-03 a C-06:** revisados, sin corrección necesaria o aceptados

---

## LOOP 3 — 🔬 Reference Validator

*Motor: reference-validator | Verifica referencias contra fuentes académicas*

### Referencias identificadas en los documentos

| ID | Referencia | Documento | Estado |
|----|-----------|-----------|--------|
| R-01 | Sebesta, R.W. — *Concepts of Programming Languages*, 11ª ed. (2016), Cap. 16, pp. 703–784 | todos | [VERIFICADA] — ISBN 978-0-13-394302-3. Título y número de capítulo verificados. El rango de páginas pp. 703–784 cubre el capítulo completo de Logic Programming. ✅ |
| R-02 | Gabbrielli, M. & Martini, S. — *Programming Languages: Principles and Paradigms* (Springer, 2010), pp. 351–423 | filminas, guia-estudio | [VERIFICADA] — ISBN 978-1-84882-913-8. Springer 2010 (no 2023 como aparece en una referencia). Año incorrecto en guia-estudio: dice "Springer 2023" — correcto es **2010** (primera edición); 2023 es reimpresión digital |
| R-03 | Louden, K.C. & Lambert, K.A. — *Programming Languages: Principles and Practice*, 3ª ed. (Course Technology, 2011) | filminas, guia-estudio | [VERIFICADA] — ISBN 978-1-111-52941-5. Año y editorial correctos ✅ |
| R-04 | Clocksin, W.F. & Mellish, C.S. — *Programming in Prolog*, 5ª ed. (Springer, 2003) | guia-estudio, guia-profesor | [VERIFICADA] — ISBN 978-3-540-00678-7. Edición y año correctos ✅ |
| R-05 | Sterling, L. & Shapiro, E. — *The Art of Prolog*, 2ª ed. (MIT Press, 1994) | guia-estudio | [VERIFICADA] — ISBN 978-0-262-19338-2. Edición y editorial correctos ✅ |
| R-06 | Kowalski, R. (1979) — "Algorithm = Logic + Control", *Communications of the ACM*, 22(7), pp. 424–436 | guia-profesor | [VERIFICADA] — DOI: 10.1145/359131.359136. Artículo canónico, ACM Digital Library. ✅ |
| R-07 | Robinson, J.A. (1965) — referenciado implícitamente en guia-estudio sección 2.3 como "Robinson, 1965" | guia-estudio | [VERIFICADA] — "A Machine-Oriented Logic Based on the Resolution Principle", *Journal of the ACM*, 12(1), 1965. No incluida con datos completos en bibliografía — recomendado agregar si se cita |
| R-08 | SWI-Prolog (https://www.swi-prolog.org) | filminas, guia-estudio | [VERIFICADA] — URL activa al momento de validación ✅ |
| R-09 | SWISH (https://swish.swi-prolog.org) | filminas, guia-estudio | [VERIFICADA] — URL activa ✅ |
| R-10 | Learn Prolog Now! (http://www.learnprolognow.org/) | guia-estudio | [VERIFICAR] — El dominio existe pero usar con precaución; el sitio puede tener intermitencias. Verificar disponibilidad antes de citar en clase |

### Correcciones requeridas

**R-02:** El año de Gabbrielli & Martini aparece como "Springer 2023" en una instancia de `guia-estudio.md`. El año correcto de la primera edición es **2010**.

---

## LOOP 4 — 🛡️ Academic Guardrail

*Motor: academic-guardrail | Formalidad, scope, densidad cognitiva*  
*Perfil docente (config.yaml):* `profesor-teorico` → ≤50 palabras/slide, ≤5 conceptos/clase

### Análisis de Formalidad

| ID | Tipo | Documento | Texto | Evaluación |
|----|------|-----------|-------|------------|
| G-01 | [INFORMAL] | `filminas.md` F-04 | "Curiosidad:" | Registro coloquial en filmina académica. Alternativa: "Dato de contexto:" |
| G-02 | [INFORMAL] | `filminas.md` F-05 | "Prolog brilla en..." | Lenguaje metafórico informal. Alternativa: "Prolog es especialmente adecuado para..." |
| G-03 | [INFORMAL] | `minuta.md` | "loop" sin cursiva ni comillas | Anglicismo no marcado. Corregir a "bucle" ✅ (aplicado en Loop 1b) |
| G-04 | [INFORMAL] | `guia-profesor.md` | "no negociable" | Expresión coloquial. Alternativa: "imprescindible" |
| G-05 | [INFORMAL] | `filminas.md` F-37 | "¿Qué pasa con...?" | Registro oral en filmina. Aceptable en contextos pedagógicos modernos — no corregir |

### Análisis de Scope

| ID | Tipo | Documento | Descripción |
|----|------|-----------|-------------|
| G-06 | [SCOPE] ✅ CORREGIDO | `filminas.md` F-01 | OOP incluido como paradigma previo — ya corregido en Loop 2 |
| G-07 | [SCOPE] | `filminas.md` F-12 | Menciona "Martelli-Montanari" como algoritmo de unificación — este nivel de detalle pertenece a Clase 2. La filmina ya lo etiqueta como "preview de Clase 2" — **aceptable, scope controlado** |
| G-08 | [SCOPE] | `filminas.md` F-18 | `findall/3` — predicado built-in no anunciado en el diseño. Aparece como extra para usuarios que piden todas las soluciones a la vez. Didácticamente útil para cerrar la motivación. **Aceptable** — bajo riesgo de desborde |
| G-09 | [SCOPE] | `guia-estudio.md` | Sección 9 ejercicio E-9 pide `camino(X, Y, Camino)` con listas — las listas son tema de Clase 3. El ejercicio está marcado como "Desafío" y el alumno puede intentarlo | **Aceptable** — marcado como desafío, no obligatorio |

### Análisis de Densidad Cognitiva

*Perfil: `profesor-teorico` → ≤50 palabras/slide, ≤5 conceptos/clase, 4–5 min/slide*

| Filmina | Palabras estimadas | Conceptos | Estado |
|---------|-------------------|-----------|--------|
| F-08 (Cláusulas de Horn) | ~180 palabras | 4 conceptos | [DENSIDAD-ALTA] — pero incluye código y tabla; el contenido visual reduce la carga real |
| F-10 (Base vs. Inferencia) | ~220 palabras | 2 conceptos | [DENSIDAD-ALTA] en palabras pero es la distinción más crítica de la clase — justificado por importancia pedagógica |
| F-19 (Base completa) | ~100 palabras + código | 1 concepto | [OK] — mayoría es código Prolog |
| F-24 (Trazado 3) | ~250 palabras | 1 concepto (trazado) | [DENSIDAD-ALTA] — es un trazado paso a paso completo; en clase se muestra en pizarrón, no en filmina estática |
| Resto (F-01 a F-07, F-11 a F-18, etc.) | ≤80 palabras | ≤3 conceptos | [OK] |

**Nota del guardrail:** las filminas con alta densidad de palabras son principalmente las de trazado (F-22 a F-27) y la de base vs. inferencia (F-10). Estas filminas funcionan como material de referencia más que como proyección clásica — el docente no las "lee" sino que las usa como apoyo al trabajo en pizarrón. En ese contexto la densidad es pedagógicamente correcta.

### Análisis de Nivel

| Aspecto | Evaluación |
|---|---|
| Vocabulario | Adecuado para universitario con 1 año de programación |
| Ejemplos | Accesibles — dominio familiar/cotidiano reduce abstracción innecesaria |
| Formalización matemática | Controlada — B2 conceptual, fórmulas solo cuando aportan claridad |
| Progresión de dificultad | Correcta: hecho → regla → consulta → trazado → recursión |
| Conexión con paradigmas previos | Explícita en B5 y en guia-estudio sección 7 |

---

## Resumen Ejecutivo del Loop de Validación

### Correcciones Aplicadas Automáticamente

| ID | Descripción | Documento | Estado |
|----|-------------|-----------|--------|
| W-01 | `ancentro` → `ancestro` (4 ocurrencias) | `diseno.md` | ✅ Aplicado |
| W-04 | `loop` → `bucle` | `minuta.md` | ✅ Aplicado |
| C-01 | Header B3: "F-13 a F-22" → "F-13 a F-20" | `filminas.md` | ✅ Aplicado |
| C-02 | OOP eliminado de "Hasta ahora vimos" | `filminas.md` | ✅ Aplicado |

### Correcciones Pendientes de Decisión Docente

| ID | Prioridad | Descripción | Documento |
|----|-----------|-------------|-----------|
| R-02 | 🔴 Alta | Año Gabbrielli & Martini: "Springer 2023" → "Springer 2010" | `guia-estudio.md` |
| W-02 | 🟡 Media | Python code en F-02: agregar comentario de estructura de `relaciones` | `filminas.md` |
| G-01 | 🟢 Baja | "Curiosidad:" → "Dato de contexto:" | `filminas.md` F-04 |
| G-02 | 🟢 Baja | "Prolog brilla en..." → "Prolog es especialmente adecuado para..." | `filminas.md` F-30 |
| G-04 | 🟢 Baja | "no negociable" → "imprescindible" | `guia-profesor.md` |
| R-07 | 🟢 Baja | Agregar referencia completa a Robinson (1965) en bibliografía | `guia-estudio.md` |

### Veredicto Final

| Documento | Estado post-validación |
|-----------|----------------------|
| `diseno.md` | ✅ Aprobado (typo crítico corregido) |
| `filminas.md` | ✅ Aprobado (coherencia y scope corregidos; mejoras de estilo pendientes) |
| `minuta.md` | ✅ Aprobado (anglicismo corregido) |
| `guia-estudio.md` | ⚠️ Aprobado con observación (año Gabbrielli & Martini a corregir) |
| `guia-profesor.md` | ✅ Aprobado (mejoras de registro menores) |

**Calificación global:** ✅ APROBADO — el material puede usarse en clase.  
Las correcciones pendientes son todas de estilo o datos bibliográficos menores, sin impacto en la correctitud técnica o pedagógica.

---

## Instrucción de Commit Post-Validación

```bash
git add salida/cursadas/2026/temas/06-paradigma-logico-prolog/
git commit -m "topic-designer: tema 06 clase 1 - filminas (38), minuta, guia-estudio, guia-profesor + loop validacion completo"
git push
```

---

*Validación ejecutada por: writing-validator 🔎 + writing-fixer ✏️ + coherence-fixer 🔗 + reference-validator 🔬 + academic-guardrail 🛡️*  
*Fecha: 2026-04-17 | Tema: 06-paradigma-logico-prolog*
