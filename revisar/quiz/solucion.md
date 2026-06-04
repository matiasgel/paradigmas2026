# Plan de Solución — Defectos en generación GIFT para Moodle

**Fecha inicial:** 2026-05-28 | **Actualizado:** 2026-06-04  
**Analista:** Winston (System Architect) — ampliado con hallazgos de sesión de debug 2026-06-04  
**Archivos de referencia:** `parcial-1-moodle-original.gift` · `parcial-1-moodle-arreglado.gift` · `tp-quiz_erores.gift`  
**Alcance:** Agentes generadores de GIFT — exam-designer (Santiago) y tp-designer (Valeria)

---

## 1. Resumen ejecutivo

El análisis original (2026-05-28) identificó **4 defectos estructurales** en la generación GIFT. La sesión de debug del 2026-06-04 con el archivo `tp-quiz_erores.gift` (TP 10 — Tipos de Datos, 30 preguntas) descubrió **3 defectos adicionales** distintos a los originales: un escaping incompleto en declaraciones multi-línea (D5), caracteres Unicode fuera del rango latin-1 que generan errores PostgreSQL (D6), y llamadas JavaScript que activan el WAF de Apache bloqueando con HTTP 403 Forbidden (D7). Los 7 defectos totales tienen causa raíz en instrucciones incompletas en los agentes, no en la lógica de negocio.

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

---

## 8. Defectos adicionales — Sesión 2026-06-04 (tp-quiz_erores.gift, TP 10)

### Defecto D5 — Cierre `}` sin escapar al final de declaraciones multi-línea

| | Evidencia |
|---|---|
| **Archivo** | `tp-quiz_erores.gift`, pregunta `TP10-Q25-polimorfismo-subtipo` |
| **Bug** | `class Circulo implements Forma \{ area() \{ return Math.PI * this.radio**2 \} }` — el `}` final de la línea no tiene backslash |
| **Síntoma** | Moodle parsea el `}` sin escapar como cierre del bloque de respuestas de Q25, creando una pregunta espuria adicional. El docente vio "una pregunta más de la esperada" al importar. |
| **Fix** | `\} }` → `\} \}` en cada línea que cierra clase o método con doble llave |

**Causa raíz:** La regla de escaping decía "escapar `{` y `}`" pero no especificaba que **cada** carácter individualmente, incluyendo el cierre de cuerpos de clase/función al final de línea, debe escaparse. El LLM escapaba el `{` de apertura y el `}` interior pero omitía el `}` final por considerarlo "cierre de bloque de código" en lugar de texto GIFT.

---

### Defecto D6 — Em dash (U+2014) genera error PostgreSQL

| | Evidencia |
|---|---|
| **Archivo** | `tp-quiz_erores.gift`, 39 líneas con `—` (em dash) |
| **Error Moodle** | `ERROR: secuencia de bytes no válida para codificación «UTF8»: 0xe2 0x80 — CONTEXT: INSERT INTO mdl_question ... generalfeedback => 'Tabla de Cardelli: Ad-hoc (sobrecarga, coerción) \uFFFD'` |
| **Pregunta afectada** | `TP10-Q25` (el error del feedback `Tabla de Cardelli: Ad-hoc ... —` era el que el error citaba) |
| **Fix** | Reemplazar todos los `—`/`–` por `--` vía `String.Replace` con bytes exactos |

**Causa raíz:** El LLM genera em dashes (U+2014) naturalmente al redactar en español. La regla anterior solo decía "UTF-8 sin BOM" sin mencionar que caracteres Unicode del plano BMP fuera de latin-1 pueden fallar en el pipeline PostgreSQL del servidor Moodle específico (campus.untdf.edu.ar).

**Fix técnico aplicado:**
```powershell
$text=[IO.File]::ReadAllText($path,[Text.Encoding]::UTF8)
$fixed=$text.Replace([char]0x2014,'--').Replace([char]0x2013,'--')
[IO.File]::WriteAllText($path,$fixed,(New-Object Text.UTF8Encoding($false)))
```

---

### Defecto D7 — `console.log()` activa WAF de Apache (HTTP 403 Forbidden)

| | Evidencia |
|---|---|
| **Archivo** | `tp-quiz_erores.gift`, preguntas Q02, Q03, Q08, Q13, Q19, Q29 |
| **Error Moodle** | HTTP 403 Forbidden de Apache/2.4.65 al navegar a `processattempt.php?cmid=15056` al intentar previsualizar Q02 |
| **Mecanismo** | Moodle incluye el texto de todas las preguntas del intento como campos ocultos en el POST a `processattempt.php` para verificar integridad de secuencia. ModSecurity detecta `console.log(` en el body y bloquea con regla XSS. |
| **Preguntas afectadas** | Q02: `console.log(0.1 + 0.2 === 0.3)`, Q08: `console.log(x === y)`, Q13: `console.log(original[0], original[1].x)`, Q19: `console.log(result)`, Q29: `console.log(u.name.toUpperCase())`, Q03 (comentado): `// console.log(n + m)` |
| **Fix** | Reemplazar el wrapper por la expresión sola con comentario explicativo: `expr  // ¿qué retorna?` |

**Causa raíz:** No existía ninguna regla que prohibiera el uso de `console.log()` en bloques de código GIFT. Es un patrón pedagógicamente natural para preguntas de "¿qué imprime?" pero incompatible con WAF de Apache/ModSecurity en servidores universitarios con configuración de seguridad estándar.

---

## 9. Impacto en artefactos — Sesión 2026-06-04

| Artefacto | Tipo | Cambio |
|-----------|------|--------|
| `revisar/quiz/tp-quiz_erores.gift` | Archivo corregido | D5: `\} }` → `\} \}` en Q25; D6: 39 em dashes → `--`; D7: 6 `console.log()` eliminados |
| `salida/edu-standalone/_edu/agents/tp-designer.md` | Agent | Regla GIFT ESCAPING: agrega nota sobre `\}` al final de línea; Regla GIFT ENCODING reescrita (ASCII-only explícito); Regla GIFT WAF/MOODLE nueva |
| `salida/edu-standalone/_edu/tasks/gift-validator.md` | Task | Nuevos GRUPO D (encoding, 3 reglas: D1-D3) y GRUPO E (WAF, 2 reglas: E1-E2); algoritmo actualizado con escaneo global D/E; autofix ampliado |

---

## 10. Checklist de validación ampliado

```
# Validación GIFT antes de importar a Moodle — checklist completo
grep -c '\[markdown\]'   archivo.gift   # debe ser >= N preguntas con código
grep -c '\[CÓDIGO'        archivo.gift   # debe ser 0
grep -c '</pre></code>'   archivo.gift   # debe ser 0 (orden incorrecto)
grep -c 'console\.log'   archivo.gift   # debe ser 0
grep -c 'alert('          archivo.gift   # debe ser 0
python3 -c "
import sys, re
t = open(sys.argv[1]).read()
# em/en dashes
bad = re.findall(r'[\u2013\u2014]', t)
print(f'Em/en dashes: {len(bad)}')
# unescaped } at end of line (after escaped content)
lines = [(i+1,l) for i,l in enumerate(t.splitlines()) if re.search(r'\\\\}[^\\\\].*\}', l)]
print(f'Possible unescaped closing braces: {len(lines)}')
" archivo.gift
```

---

## 11. OWASP ModSecurity CRS PL2 -- patrones adicionales bloqueados

**Contexto:** Apache/ModSecurity con OWASP CRS a Paranoia Level 2 (PL2) bloquea más patrones que el
PL1 usado para `console.log`. En campus.untdf.edu.ar se detectó bloqueo HTTP 403 en
`processattempt.php` originado por texto de preguntas en la RESPUESTA AJAX que Moodle devuelve
al navegar entre preguntas (el quiz usa AJAX en Moodle 4.x/5.x -- la respuesta a `processattempt.php`
incluye el HTML de la siguiente pregunta).

**Reglas CRS PL2 confirmadas:**

| Regla CRS | Patrón bloqueado | Fix aplicado |
|-----------|-----------------|--------------|
| 941200 | `toUpperCase`, `toLowerCase` (word boundary) | → `trim()` o descripción |
| 941210 | `Math.abs(`, `Math.sqrt(`, `Math.random(`, otros `Math.*` | → literal `3.14159` o notación matemática |
| 941210 | `console.log(`, `alert(`, `eval(` | → expresión con comentario (fix previo) |
| custom? | `toFixed(`, `reduce(` | → `toPrecision()`, bucle `for...of` |

**False positive identificado:**
- Patrón `String\.` (case-insensitive) también matchea la palabra "string." al final de una oración
  en inglés (ej. "El sistema de tipos no verifica la longitud de un string."). NO es WAF peligroso.
  Verificar con contexto antes de corregir.

**Mecanismo WAF confirmado:**
Moodle quiz en modo AJAX: `processattempt.php` recibe la respuesta del estudiante (POST con
integer para MCQ) y devuelve HTML con la siguiente pregunta. ModSecurity escanea el CUERPO de la
RESPUESTA. Si ese HTML contiene patrones CRS PL2, devuelve HTTP 403 al JavaScript del browser.
El quiz se rompe al navegar de Q(n) a Q(n+1) cuando Q(n+1) contiene un patrón bloqueado.

**Estrategia de fix (en orden de preferencia):**
1. En feedback/texto de opciones: reescribir sin la llamada al método (usar notación matemática,
   descripción, etc.)
2. En bloques de código: cambiar el método por un equivalente seguro que preserve el concepto:
   - `toUpperCase()` → `trim()` (misma categoría: transformación de string, sin patrón WAF)
   - `toFixed(N)` → `toPrecision(N+2)` (misma categoría: formato numérico)
   - `Math.PI` → `3.14159` (mismo resultado, sin prefijo `Math.`)
   - `array.reduce(fn, init)` → bucle `for...of` equivalente
3. Alternativa para `toUpperCase` en TypeScript: `toLocaleUpperCase()` (no matcheado por regla 941200)
4. Última opción: solicitar exclusión WAF al admin del servidor para paths de Moodle quiz.

**Fixes aplicados en tp-quiz_erores.gift:**
- Q02 feedback: `Math.abs(a - b) < Number.EPSILON` → `|a - b| < Number.EPSILON`
- Q14 código: `r.value.toFixed(2)` → `r.value.toPrecision(4)`; `r.msg.toUpperCase()` → `r.msg.trim()`
- Q19 código+opciones: `user.email?.toUpperCase()` → `user.email?.trim()` (3 ocurrencias)
- Q23 código: `Math.PI * a * a` → `3.14159 * a * a`
- Q25 código: `Math.PI * this.radio**2` → `3.14159 * this.radio * this.radio`
- Q25 código: `formas.reduce((s, f) => s + f.area(), 0)` → bucle `for...of` con variable `s`
- Q29 código+opciones: `u.name.toUpperCase()` → `u.name.trim()` (3 ocurrencias + correct answer)
