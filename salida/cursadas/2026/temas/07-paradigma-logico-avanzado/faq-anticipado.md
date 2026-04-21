# FAQ Anticipado — Tema 07: Paradigma Lógico — Clase 2+3

**Preguntas que van a salir en clase o estudiando.** Agrupadas por fuente (clase vs. autónomo) y por perfil dominante.

---

## 🎙️ En Clase

### Bloque 1 — Unificación

**P1 [ansioso, B1 min ~18]: ¿`X = 5` es asignación?**
**R:** No — es unificación. Si `X` está libre, la liga a `5`. Si `X` ya vale `7`, la unificación **falla**. No hay sobreescritura nunca.

**P2 [estratégico, B1 min ~22]: ¿Cuándo conviene usar `==` en vez de `=`?**
**R:** Cuando *comparás* sin querer ligar. Típico: predicados defensivos que chequean si dos argumentos ya son idénticos antes de operar.

**P3 [disperso, B1 min ~26]: ¿Qué es el `=..` ese del dos puntos?**
**R:** Se llama *univ*. Descompone un término en una lista `[Funtor | Args]`. Útil para metaprogramación. Ejemplo: `padre(juan, X) =.. L.` liga `L = [padre, juan, X]`.

**P4 [ansioso, B1 min ~30]: ¿Qué es occurs-check?**
**R:** Chequeo para evitar ligar `X = f(X)` (término infinito). SWI lo **desactiva** por defecto por performance. En la práctica no te lo vas a cruzar — no te preocupes ahora.

### Bloque 2 — Resolución SLD

**P5 [disperso, B2 min ~45]: ¿Qué es *resolvente*?**
**R:** La lista de goals pendientes. Empieza con la consulta. Cada paso reemplaza un goal por el cuerpo de una cláusula que unifica. Termina cuando queda vacía (éxito).

**P6 [estratégico, B2 min ~50]: ¿Por qué Prolog elige siempre el goal más a la izquierda?**
**R:** Es la **regla de selección de Prolog** (*leftmost*). Simplifica la implementación y da semántica predecible. Otros lenguajes lógicos (Mercury) usan otras reglas.

**P7 [recursero, B2 min ~55]: Entonces, ¿si pongo el caso recursivo antes del base, puede fallar?**
**R:** Puede entrar en **loop infinito**. La regla práctica es **siempre caso base antes del recursivo**.

### Bloque 3 — Backtracking

**P8 [disperso, B3 min ~70, ALTA FRECUENCIA]: ¿Dónde volvió Prolog? Me perdí.**
**R:** 🚨 **Intervención obligatoria.** Pausar, dibujar árbol SLD en pizarrón. Marcar el *choice point*. La pregunta es signo de que toda la sección se está perdiendo.

**P9 [ansioso, B3 min ~75]: ¿El trail lo guarda todo para siempre?**
**R:** No — solo hasta el siguiente choice point. Cuando termina la consulta, se vacía.

**P10 [estratégico, B3 min ~80]: ¿Qué pasa si la recursión nunca falla?**
**R:** Prolog nunca backtrackea. Es el caso típico de `member/2` pidiendo *todas* las soluciones con `;` — genera todas hasta que vos cortes.

### Bloque 4 — Corte

**P11 [recursero, B4 min ~90, FRECUENTE]: ¿El `!` es como `return` en Python?**
**R:** No — es una misconception clásica. `!` **poda choice points**: dice *"no vuelvas por aquí"*. La ejecución continúa adelante. No devuelve nada.

**P12 [estratégico, B4 min ~95]: ¿Cuál es la diferencia concreta entre corte verde y rojo?**
**R:** **Verde** = optimización (si lo sacás, el programa sigue dando los mismos resultados, solo más lento). **Rojo** = necesario (si lo sacás, el programa devuelve resultados incorrectos o más de lo debido). El rojo **rompe la semántica declarativa**.

**P13 [ansioso, B4 min ~100]: ¿Y si se me olvida el `!`, siempre es peor?**
**R:** A veces es peor (más backtracking). A veces cambia el resultado (si era rojo). La forma segura es *preferir if-then-else (`->`)* cuando sea posible — hace el corte explícito.

### Bloque 5 — Negación

**P14 [ansioso, B5 min ~110]: ¿`\+ P` es *"no P"*?**
**R:** Casi: es *"no hay forma de probar P ahora mismo"* (**negation as failure**). Es diferente de *"P es falso"* en lógica clásica. Si `P` usa variables libres, puede dar resultados contra-intuitivos.

**P15 [estratégico, B5 min ~115]: ¿Cuándo usar `dif/2` en lugar de `\+(X=Y)`?**
**R:** Siempre que las variables puedan no estar aún ligadas. `dif/2` **difiere** el chequeo hasta que las variables tomen valor. `\+` chequea *ahora* y puede fallar falsamente.

### Bloque 7 — Aritmética

**P16 [ansioso, B7 min ~132]: ¿`X = 2+3` no me da 5?**
**R:** ¡No! `=` es unificación — queda `X = 2+3` (el término). Para evaluar necesitás `is/2`: `X is 2+3` → `X = 5`.

**P17 [disperso, B7 min ~138]: ¿Y `=:=`?**
**R:** Compara dos expresiones aritméticas evaluándolas. `2+3 =:= 5` → `true`. No liga nada, solo compara.

### Bloque 8 — Listas

**P18 [recursero, B8 min ~155]: `append/3` — ¿por qué funciona al revés?**
**R:** Porque es declarativo. `append([1,2], Y, [1,2,3,4])` → `Y = [3,4]`. No es una función — es una **relación**. Lo mismo para descomposición.

**P19 [ansioso, B8 min ~165]: `[H|T]` con lista vacía da error?**
**R:** Falla la unificación (no hay `H` ni `T`). Por eso las cláusulas recursivas de listas separan caso `[]` (base) y `[H|T]` (recursivo).

### Bloque 9 — Recursión con Acumulador

**P20 [disperso, B9 min ~185, CRÍTICA]: ¿Por qué necesito un parámetro extra?**
**R:** 🚨 **Pizarrón obligatorio.** Analogía: una **mochila** que vas llenando a medida que bajás la recursión. Cuando llegás al caso base, la mochila tiene el resultado. Sin mochila, el resultado se *construye al volver* (no es tail-recursive).

**P21 [recursero, B9 min ~190, FILTRO DETECTOR]: ¿Por qué `factorial(0, Acc, Acc).` y no `factorial(0, _, 1).`?**
**R:** Porque el acumulador ya tiene el resultado cuando llegamos al caso base. Si devolvemos `1`, estamos ignorando todo el trabajo hecho.

**P22 [estratégico, B9 min ~195]: Entonces, ¿la versión sin acumulador no es tail-recursive?**
**R:** Correcto. `factorial(N, F) :- ..., F is N*F1.` — la multiplicación está *después* de la llamada recursiva, por lo que no es la *última* operación. No hay tail-call optimization.

### Bloque 10 — Meta-predicados

**P23 [ansioso, B10 min ~205]: `findall`, `bagof`, `setof` — ¿cuál uso?**
**R:** Tabla:
- `findall(T, Q, L)` — lista con *todas* las soluciones (incluye duplicados; L = [] si no hay).
- `bagof(T, Q, L)` — como findall pero **falla** si no hay soluciones; respeta variables libres agrupando.
- `setof(T, Q, L)` — como bagof, pero ordenada y sin duplicados.

**P24 [recursero, B10 min ~215]: ¿Puedo hacer `findall` adentro de otro `findall`?**
**R:** Sí. Es patrón común en análisis de grafos (*todos los caminos desde todos los nodos*). Cuidado con complejidad.

### Bloque 11 — Aplicaciones

**P25 [todos, B11 min ~225]: ¿Cómo resuelvo el problema de las 4 reinas?**
**R:** 🚨 *No se alcanza a ver completo en clase.* Se deja como ejercicio integrador (ej28 del TP). En clase se muestra solo el **esqueleto** y el patrón *generate-and-test*.

---

## 📖 Estudiando Solos (Guía de Estudio)

### Sección 3.1 — Unificación

**Q1 [disperso]: ¿Qué es MGU y para qué me sirve en el examen?**
**R:** MGU = sustitución más general. En el parcial te pueden pedir *"aplicar el algoritmo de Robinson a `f(X, g(a)) = f(h(Y), Z)`"* — la respuesta es un MGU {X/h(Y), Z/g(a)}. Lo más libre posible.

**Q2 [ansioso]: La tabla de operadores (`=`, `==`, `\=`, `\==`, `=..`) — ¿me la aprendo de memoria?**
**R:** Mejor entender cada uno con un ejemplo. Patrón:
- `=` → unifica, puede ligar.
- `==` → compara, nunca liga.
- `=..` → descompone.
Hacé una tarjeta con un ejemplo mínimo de cada uno.

### Sección 3.2 — SLD

**Q3 [todos]: ¿Cómo dibujo un árbol SLD en el parcial?**
**R:** Raíz = consulta. Cada hijo = aplicación de una cláusula (anotar cuál + la sustitución). Hoja verde ✓ = resolvente vacía. Hoja roja ✗ = no unifica. Marcar el camino que Prolog recorre (DFS izquierda a derecha). **Practicar con ≥5 ejemplos antes del parcial.**

### Sección 3.3 — Backtracking

**Q4 [disperso]: No entiendo cuándo Prolog backtrackea.**
**R:** 🚨 *Ejercicio propuesto:* tomá `color(rojo). color(verde). color(azul). ?- color(X), fail.` y anotá **cada paso** que hace Prolog. Vas a ver que recorre las 3 opciones en orden.

### Sección 3.4 — Corte

**Q5 [estratégico, frecuente]: La diferencia corte verde/rojo — ¿es nomenclatura o hay prueba formal?**
**R:** Hay prueba informal: *si ejecutás el predicado sin el corte con todas las consultas posibles y las respuestas son las mismas que con corte → verde*. Si cambian → rojo.

### Sección 3.5 — Negación

**Q6 [ansioso]: `\+ P` y `dif(X, Y)` — ¿cuándo cuál?**
**R:** Regla: **si hay variables libres que se van a ligar después, usá `dif/2`**. Si las variables ya están ligadas, `\+` es suficiente y más rápido.

### Sección 3.7 — Aritmética

**Q7 [disperso]: ¿Qué pasa con `X is Y + 1` si `Y` es variable libre?**
**R:** Error en runtime: *"Arguments are not sufficiently instantiated"*. `is/2` requiere que el lado derecho esté *totalmente ligado* en el momento de evaluar.

### Sección 3.8 — Listas

**Q8 [recursero]: La guía dice *"implementar `member/2` sin usar `member/2`"*. ¿Cómo?**
**R:** Dos cláusulas:
```prolog
mi_member(X, [X|_]).           % la cabeza es X
mi_member(X, [_|T]) :- mi_member(X, T).  % está en el resto
```
Leer en voz alta: *"X es miembro de la lista si es la cabeza, o si es miembro del resto"*.

### Sección 3.9 — Acumulador

**Q9 [recursero, CRÍTICA]: Escribo `factorial(N, F)` con acumulador y da error. ¿Por qué?**
**R:** Patrón correcto:
```prolog
factorial(N, F) :- factorial_aux(N, 1, F).   % inicio con acumulador = 1
factorial_aux(0, Acc, Acc).                  % base: el acumulador es el resultado
factorial_aux(N, Acc, F) :-
    N > 0, N1 is N - 1, Acc1 is Acc * N,
    factorial_aux(N1, Acc1, F).
```
La clave: el predicado *aux* tiene un parámetro de más (el acumulador). Siempre se pasa el acumulador inicial desde el wrapper.

### Sección 3.10 — Meta-predicados

**Q10 [disperso]: ¿`findall` con lista vacía da error?**
**R:** No — da `[]`. *Esa es la diferencia con `bagof`:* `bagof` **falla** si no hay soluciones; `findall` devuelve `[]`.

### Sección 3.11 — Aplicaciones

**Q11 [todos, FRECUENTE]: ¿Cómo estudio para el TP de las 4 reinas si en clase no lo terminamos?**
**R:**
1. Leé §3.11 de la guía — esqueleto `generate-and-test`.
2. Mirá el pseudocódigo: generar permutación de `[1,2,3,4]` → chequear que no haya conflictos diagonales.
3. Implementalo en SWISH con `permutation/2` y una función `seguras/1`.
4. Si te traba, postealo en el canal de la materia (traje de aula).

---

## 🚨 Preguntas Detectoras (para el docente)

Si durante la clase aparece alguna de estas preguntas, **parar y atender antes de seguir**:

1. *"¿Dónde backtrackea Prolog?"* → dispersa, la clase **necesita pausa + pizarrón**.
2. *"¿`!` es como `return`?"* → recursero, **bloquea todo B4**.
3. *"¿Por qué `=` no suma?"* → ansioso en B7, **revisar 5 minutos más el concepto**.
4. *"¿Y la mochila del acumulador cómo sabe dónde ir?"* → disperso o recursero, **pizarrón con traza paso a paso**.

---

## Frecuencia Estimada

| Pregunta | Frecuencia | Cohort afectado |
|----------|-----------|-----------------|
| P8 (dónde backtrackea) | Alta | 60%+ |
| P11 (`!` = return) | Muy alta | 70%+ |
| P14 (`\+` como negación) | Media | 40% |
| P20 (acumulador por qué) | Alta | 50%+ |
| P23 (findall/bagof/setof) | Alta | 65%+ |
| P25 (4 reinas) | Muy alta | 80%+ (sobre TP) |

---

*Fuente: simulación 4 perfiles + literatura (Mayer, Sweller, Hoq et al.) + calibración temas 03/04.*
