# Plan de Solución — Defectos en generación GIFT para Moodle

**Fecha:** 2026-05-28  
**Analista:** Winston (System Architect)  
**Archivos de referencia:** `parcial-1-moodle-original.gift` · `parcial-1-moodle-arreglado.gift`  
**Alcance:** Agentes generadores de GIFT — exam-designer (Santiago) y tp-designer (Valeria)

---

## 1. Resumen ejecutivo

El archivo original generado por el agente tiene **4 defectos estructurales** que hacen imposible su uso directo en Moodle. El archivo arreglado (corregido manualmente) funciona pero introduce **2 bugs menores** propios del proceso manual. Todos los defectos tienen causa raíz en **instrucciones incompletas en el workflow y en los agentes**, no en la lógica de negocio.

---

## 2. Inventario de defectos

### Defecto D1 — Ausencia del flag `[markdown]` en preguntas con código

| | Evidencia |
|---|---|
| **Original** | `::P-02-002:: Considerá el siguiente programa TypeScript:  [CÓDIGO: function suma...` |
| **Arreglado** | `::P-02-002:: [markdown] Considerá el siguiente programa TypeScript: <pre><code>function suma...` |

Sin `[markdown]`, Moodle renderiza el enunciado como texto plano. El tag `<pre><code>` se muestra literalmente en pantalla en lugar de formatearse. **Impacto: crítico** — todas las preguntas con código son ilegibles.

**Causa raíz:** El Step 6 (GIFT export) del `exam-cycle/workflow.md` menciona "escape reserved chars" pero no especifica cuándo aplicar `[markdown]` ni cómo representar código.

---

### Defecto D2 — Bloques de código como `[CÓDIGO: ... ↵ ...]`

| | Evidencia |
|---|---|
| **Original** | `[CÓDIGO: const numeros = [1, 2, 3]; ↵  ↵ const resultado = numeros ↵   .filter(n => n % 2 === 0)]` |
| **Arreglado** | `<pre><code>const numeros = [1, 2, 3]; \nconst resultado = numeros \n   .filter(n => n % 2 === 0)</code></pre>` |

El agente usa una notación inventada `[CÓDIGO: ... ↵ ...]` durante la generación de borradores en Step 3. Al exportar en Step 6, esta notación no se convierte a HTML. Moodle la muestra literalmente.

**Causa raíz A:** No existe una regla en Step 3.b que indique el formato de código para el borrador interno.  
**Causa raíz B:** No existe una regla en Step 6.2 que indique la conversión al exportar.  
**Bug adicional en el arreglado:** En varios lugares el cierre de tags aparece como `</pre></code>` (orden incorrecto). El correcto es `</code></pre>`. Moodle puede tolerarlo, pero es HTML inválido.

---

### Defecto D3 — Feedback truncado mid-sentence

| | Evidencia |
|---|---|
| **Ambos archivos** | `#La sintaxis establece las reglas formales (gramática) que determinan qué secuencias de tokens son programas válidos. La semántica determina qué significan esos programas — qué efecto computacional tie` |
| | `#La unificación es el mecanismo central de Prolog: dados dos términos, busca la sustitución más general (MGU — Most General Unifier) que los haga iguales sintácticamente. No evalúa, no computa numérica` |

El texto de feedback (`#`) se corta en medio de una oración. El truncamiento es consistente (~180-200 caracteres de feedback generado antes del corte). **El arreglado no corrigió este defecto.**

**Causa raíz:** Durante Step 3.b el LLM genera muchas preguntas en un turn. El feedback explícito y largo agota la ventana de output disponible. Las últimas palabras de cada texto de feedback son siempre las que se pierden.

**Impacto:** No bloquea la importación en Moodle, pero el alumno recibe orientación incompleta o con oración cortada, lo que puede confundir.

---

### Defecto D4 — Caracteres `=` y `{` sin escapar en texto visible

| | Evidencia |
|---|---|
| **Original** | Código TypeScript `n % 2 === 0`, `(x: T) => T` aparece con `=` sin escapar |
| **Original** | Código Prolog `?- abuelo(tomas, Z).` con `=` en opciones de respuesta sin escapar |
| **Arreglado** | `n % 2 \=\=\= 0`, `(x\: T) \=\> T`, `?- abuelo(tomas, Z).` → `Z \= laura ; Z \= pedro` |

El `=` sin escapar en texto de opciones es ambiguo para el parser GIFT: puede interpretarse como inicio de una respuesta correcta. La regla A7 del `gift-validator.md` debe capturarlo.

**Causa raíz:** El agente no tiene una regla explícita que diga "al generar código TypeScript/Prolog en opciones de respuesta, aplicar escape GIFT a `=`, `{`, `}`, `#`". El validator A7 existe pero **no se invoca en el exam-cycle** (solo en el tp-designer workflow).

---

## 3. Causa raíz sistémica

Los 4 defectos comparten una sola causa estructural:

> **El workflow `exam-cycle/workflow.md` Step 6 (GIFT export) carece de reglas específicas para preguntas con código, y el `gift-validator` no se invoca antes de la exportación.**

En contraste, el tp-designer (Valeria) sí tiene la regla `ANTES de escribir el archivo GIFT a disco, ejecutar SIEMPRE la validación` y su workflow invoca `gift-validator.md`. El exam-designer (Santiago) no tiene ese gate.

---

## 4. Plan de solución — 5 acciones ordenadas por impacto

### Acción A1 — Agregar reglas de código GIFT al Step 6 del exam-cycle

**Archivo:** `_edu/workflows/exam-cycle/workflow.md`  
**Sección:** Step 6.2 "For GIFT"  
**Cambio:** Reemplazar la línea genérica `Rules: UTF-8 sin BOM, ::id:: titles, blank line...` por un bloque con reglas explícitas para código:

```markdown
- **Formato de texto con código:** Si la pregunta contiene un bloque de código, OBLIGATORIO usar `[markdown]` después del `::id::` y representar el código como `<pre><code>CÓDIGO</code></pre>` con saltos de línea reales (no `\n` ni `↵`). El cierre correcto es siempre `</code></pre>` (primero `</code>`, luego `</pre>`).
- **Escape de caracteres reservados en texto visible:** `=` → `\=`, `{` → `\{`, `}` → `\}`, `#` → `\#`. Esto incluye código TypeScript (`===` → `\=\=\=`, `=>` → `\=>`), Prolog (`=` → `\=`, `\=` → `\\=`) y cualquier otro lenguaje.
- **Feedback:** Máximo 3 oraciones de feedback por pregunta. Siempre completar la última oración. No dejar oraciones incompletas.
- **Validación obligatoria:** Antes de escribir el GIFT a disco, ejecutar la validación completa del task `{project-root}/_edu/tasks/gift-validator.md`. Si hay errores del Grupo A, corregir antes de exportar.
```

---

### Acción A2 — Agregar regla `<r>` de código GIFT al agente exam-designer

**Archivo:** `salida/edu-standalone/_edu/agents/exam-designer.md`  
**Sección:** bloque `<rules>` dentro de `<activation>`  
**Cambio:** Agregar regla nueva después de la regla `GATE DE APROBACIÓN`:

```xml
<r>GIFT CON CÓDIGO: Preguntas con bloques de código SIEMPRE usan [markdown] después del ::id::. El código va en &lt;pre&gt;&lt;code&gt;...&lt;/code&gt;&lt;/pre&gt; con newlines reales. En texto visible escapar: = → \=, { → \{, } → \}, # → \#. Incluye TypeScript (=== → \=\=\=), Prolog (= → \=). Feedback máximo 3 oraciones completas. ANTES de exportar GIFT, ejecutar gift-validator.md.</r>
```

---

### Acción A3 — Invocar gift-validator en el exam-cycle Step 6

**Archivo:** `_edu/workflows/exam-cycle/workflow.md`  
**Sección:** Step 6.2 "For GIFT", sub-paso después de convertir preguntas  
**Cambio:** Agregar paso de validación explícito:

```markdown
- Antes de escribir `examen.gift` a disco: ejecutar task `{project-root}/_edu/tasks/gift-validator.md` sobre el contenido generado. Si hay errores Grupo A → corregir inline antes de guardar. Reportar al docente: "✅ Validación GIFT: N preguntas OK, M advertencias." No exportar si hay errores A o B sin resolver.
```

---

### Acción A4 — Agregar regla de código GIFT al agente tp-designer

**Archivo:** `salida/edu-standalone/_edu/agents/tp-designer.md`  
**Sección:** bloque `<rules>` dentro de `<activation>`  
**Cambio:** Agregar regla nueva después de la regla `El archivo GIFT debe respetar...`:

```xml
<r>GIFT CON CÓDIGO: Preguntas con bloques de código SIEMPRE usan [markdown] después del ::id::. El código va en &lt;pre&gt;&lt;code&gt;...&lt;/code&gt;&lt;/pre&gt; con newlines reales. Cierre correcto: &lt;/code&gt;&lt;/pre&gt;. En texto visible escapar = → \=, { → \{, } → \}, # → \#. Feedback máximo 3 oraciones completas.</r>
```

---

### Acción A5 — Agregar regla A10 al gift-validator para `[markdown]` sin código

**Archivo:** `salida/edu-standalone/_edu/tasks/gift-validator.md`  
**Sección:** GRUPO C — Advertencias  
**Cambio:** Agregar:

| ID | Regla | Descripción |
|----|-------|-------------|
| C7 | `[markdown]` ausente en pregunta con código | Si el enunciado contiene `<pre>`, `<code>`, o patrones de código (backtick, `function`, `class`, `:-`) pero NO tiene `[markdown]` → advertencia. |
| C8 | Cierre HTML incorrecto | Si el enunciado contiene `</pre></code>` (orden incorrecto) → advertencia. El correcto es `</code></pre>`. |
| C9 | Feedback truncado | Si el texto de feedback termina mid-word (sin punto, ?, !) → advertencia. |

---

## 5. Prioridad de implementación

| Acción | Impacto | Esfuerzo | Prioridad |
|--------|---------|----------|-----------|
| A1 — GIFT rules en exam-cycle workflow | Alto — previene D1, D2, D3, D4 en origin | Bajo — edición de texto | **P0** |
| A2 — Regla `<r>` en exam-designer | Alto — agente la aplica en cada generación | Bajo — 1 línea XML | **P0** |
| A3 — Invocar validator en exam-cycle | Alto — detecta D4 antes de exportar | Bajo — agregar step | **P1** |
| A4 — Regla `<r>` en tp-designer | Medio — el TP designer ya tiene mejor cobertura | Bajo — 1 línea XML | **P1** |
| A5 — Reglas C7/C8/C9 en gift-validator | Medio — mejora la red de seguridad | Bajo — tabla markdown | **P2** |

---

## 6. Artefactos a modificar

| Archivo | Tipo | Acciones |
|---------|------|----------|
| `_edu/workflows/exam-cycle/workflow.md` | Workflow | A1, A3 |
| `salida/edu-standalone/_edu/agents/exam-designer.md` | Agent | A2 |
| `salida/edu-standalone/_edu/agents/tp-designer.md` | Agent | A4 |
| `salida/edu-standalone/_edu/tasks/gift-validator.md` | Task | A5 |

> **Nota:** `generate_gift_quiz.py` (script programático) no necesita cambios — su `_escape_gift()` ya maneja el escaping correctamente. Los defectos son exclusivos del path de generación LLM (agentes).

---

## 7. Verificación post-implementación

Para validar que las correcciones funcionan, el próximo ciclo de examen debe producir un GIFT que:

1. Todas las preguntas con código tienen `[markdown]` → verificar con `grep '\[markdown\]'`
2. No hay ocurrencias de `[CÓDIGO:` → verificar con `grep '\[CÓDIGO'`
3. Todo cierre de tag es `</code></pre>` → verificar con `grep '</pre></code>'` (debe dar 0)
4. Todo feedback termina con `.`, `?` o `!` → revisión manual de 5 preguntas muestra
5. El GIFT pasa la validación completa del gift-validator sin errores del Grupo A
