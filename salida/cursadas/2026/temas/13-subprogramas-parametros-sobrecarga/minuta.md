# Minuta docente — Clase 13A

> Tema: Subprogramas, Parámetros y Sobrecarga (Clase 13A)
> Duración total: 120 minutos
> Lenguaje principal: TypeScript
> Fuente baseline: `clase_dada.txt`
> Profesor: Dr. Roberto ✍️
> Hilo conductor: del problema del acoplamiento a la representación, al módulo como frontera de visibilidad y al genérico como reutilización sin mezcla de tipos.

## Trazabilidad bibliográfica

Las siguientes referencias respaldan los conceptos de la clase. Fueron consultadas en ChromaDB (`scripts/knowledge_base.py search ... --type material`) y se citan aquí para que el docente pueda profundizar. **No se citan inline en las filminas** (regla editorial del pipeline).

- **Sebesta, R. W. — *Concepts of Programming Languages* (Pearson, 2019), Cap. 11, pp. 471-506.** Abstract data types, encapsulation, modules. Soporta F-03, F-06, F-10, F-11, F-12.
- **Gabbrielli, M. & Martini, S. — *Programming Languages: Principles and Paradigms* (Springer, 2nd ed., 2023), Cap. 9, pp. 283-294.** ADTs y módulos; imports y visibilidad. Soporta F-03, F-12, F-13.
- **Gabbrielli & Martini, Cap. 9, pp. 295-350.** Encapsulation and information hiding; módulos como partición estática con visibilidad. Soporta F-06, F-10.
- **Louden, K. C. & Lambert, K. A. — *Programming Languages: Principles and Practices* (Course Technology, 2012), Cap. 11, pp. 496-545.** ADT mechanisms and modules; criterios de modificabilidad, reusabilidad y seguridad. Soporta F-03, F-08, F-10.
- **Sebesta, Cap. 9, pp. 389-440.** Generic subprograms, parametric polymorphism, ad hoc polymorphism (overloading). Soporta F-14 (genéricos como polimorfismo paramétrico).

> Nota de drift: el `clase_dada.txt` trata en realidad sobre TAD/ADT, encapsulamiento, módulos, interfaces y genéricos en TypeScript — no sobre subprogramas, parámetros ni sobrecarga como sugiere el título del tema. La minuta y las filminas son fieles al `.txt` (baseline de la clase dada), que es la fuente de verdad indicada por el docente. El título del tema se conserva por consistencia con `topic.yaml`.

---

## [F-00] Portada 13A — 3 min

**Guion del docente.** "Buenas tardes. Hoy cerramos la idea de abstracción que venimos construyendo: vamos a pasar del problema del acoplamiento a la representación, al módulo como frontera de visibilidad. La clase se llama *Módulos, interfaces y genéricos en TypeScript*. Cuatro conceptos formales, cuatro preguntas de diseño. TypeScript es nuestro lenguaje de trabajo porque permite expresar todos estos conceptos de forma directa."

**Conceptos clave a enfatizar.**
- La clase recorre un problema (acoplamiento) y cuatro construcciones que lo resuelven (TAD, interfaz, módulo, genéricos).
- TypeScript como lenguaje vehículo: privado real con `#`, interfaces estructurales, genéricos.

**Preguntas anticipadas.**
- *¿Por qué TypeScript y no Java?* — Porque `#` da privacidad real y las interfaces son estructurales, no nominales.
- *¿Esto no era de la clase anterior?* — Es la continuación: hoy pasamos de la idea de abstracción a su materialización en módulos.

**Transición.** "Antes de construir, veamos qué pregunta responde cada concepto. Ahí está la ruta de la clase."

---

## [F-01] Ruta de la clase — 8 min

**Guion del docente.** "Cuatro conceptos formales, cuatro preguntas. El TAD responde: ¿qué significa usar un tipo sin ver su representación? La interfaz: ¿qué operaciones puede asumir el cliente? El módulo: ¿dónde se declara una frontera de visibilidad? Los genéricos: ¿cómo reutilizar sin mezclar tipos? Cada uno responde a una pregunta de diseño distinta. No son sinónimos. Si los confundimos, terminamos con clases enormes o con representación expuesta. La clase recorre el problema que motiva cada uno y la construcción concreta en TypeScript."

**Conceptos clave a enfatizar.**
- TAD → abstracción de datos.
- Interfaz → especificación pública.
- Módulo → encapsulamiento modular / frontera de visibilidad.
- Genéricos → polimorfismo paramétrico.
- Cada concepto responde a una pregunta **distinta**: no son intercambiables.

**Preguntas anticipadas.**
- *¿Diferencia entre TAD e interfaz?* — El TAD es la idea matemática (nombre + operaciones + semántica + invariantes); la interfaz es la materialización sintáctica del contrato.
- *¿Y la clase?* — La clase es una forma de implementar un TAD, pero no es lo mismo que el TAD.

**Transición.** "Empecemos por el problema que motiva todo esto: el acoplamiento a la representación."

---

## [F-02] El problema: acoplamiento a la representación — 8 min

**Guion del docente.** "Imaginen que tienen una pila y el cliente sabe que internamente es un array. ¿Qué pasa? El cliente deja de usar una pila y pasa a usar un array disfrazado. Escribe `pila.datos[0] = 99` o `pila.datos.reverse()`. Ya no está usando la abstracción pila: está usando la representación. La consecuencia es brutal: cualquier cambio interno rompe código externo. Si mañana cambio el array por una lista enlazada, todo el código que accede a `datos` se rompe. La abstracción aparece cuando el cliente solo puede usar operaciones permitidas. Ese es el punto de partida de toda la clase."

**Conceptos clave a enfatizar.**
- Acoplamiento a la representación: el cliente conoce el *cómo* y deja de depender del *qué*.
- `pila.datos[0] = 99` y `pila.datos.reverse()` son accesos que rompen la abstracción.
- Cambio interno → rotura externa. Es el síntoma del acoplamiento.
- La abstracción aparece al restringir el acceso a operaciones permitidas.

**Preguntas anticipadas.**
- *¿Y si el array es privado?* — Justamente: si lo es, no hay acoplamiento. El problema es cuando se expone, sea por descuido o por diseño.
- *¿Esto pasa en TypeScript?* — Sí, si se declaran campos públicos o se devuelve el array interno sin copia. Lo veremos en la copia defensiva.

**Transición.** "¿Cómo evitamos esto? Con el Tipo Abstracto de Datos."

---

## [F-03] TAD: Tipo Abstracto de Datos — 8 min

**Guion del docente.** "Un TAD no se define por cómo guarda los datos, sino por cuatro cosas: nombre, operaciones, semántica observable e invariantes. Miren la tabla. El cliente ve el nombre del tipo `Stack<T>`, las operaciones `push`, `pop`, `peek`, la semántica LIFO y los errores definidos. Qué queda oculto: si usa array, lista o buffer; los algoritmos auxiliares; cómo se mantiene el orden; el caso interno de pila vacía. Esa separación entre lo visible y lo oculto es el corazón del TAD. No es ocultar por ocultar: es definir qué prometo y qué me reservo cambiar."

**Conceptos clave a enfatizar.**
- TAD = Nombre + Operaciones + Semántica observable + Invariantes.
- Lo visible: nombre, operaciones, semántica, errores definidos.
- Lo oculto: representación, algoritmos auxiliares, detalles internos.
- La separación visible/oculto **es** la abstracción.

**Preguntas anticipadas.**
- *¿LIFO es una invariante?* — Sí, observable. El array no la garantiza: por eso la pila es un TAD y el array no.
- *¿Qué es una invariante observable?* — Una propiedad que el cliente puede asumir sin importar la implementación.

**Transición.** "Para que esto sea concreto, necesitamos un ejemplo mínimo. La pila es perfecta."

---

## [F-04] La pila como ejemplo mínimo — 7 min

**Guion del docente.** "La pila es buena explicación de un ADT porque tiene una regla simple: LIFO, Last In First Out. Esa es una invariante observable: el array no la tiene. Miren la tabla. Cada operación tiene una promesa observable y un detalle irrelevante. `push(x)` agrega x como próximo candidato a salir — dónde se almacena es irrelevante. `pop()` devuelve y remueve el último agregado disponible — cómo se mueve el índice interno es irrelevante. `peek()` observa sin remover — si usa cache o cálculo directo, irrelevante. `isEmpty()` informa si hay elementos disponibles — si guarda size o lo calcula, irrelevante. Esa es la independencia entre promesa y detalle."

**Conceptos clave a enfatizar.**
- LIFO como invariante observable (no como detalle de implementación).
- Cada operación separa **promesa observable** de **detalle irrelevante**.
- El array no garantiza LIFO: por eso no es un TAD pila.

**Preguntas anticipadas.**
- *¿Por qué LIFO y no FIFO?* — FIFO sería una cola (queue). La pila es LIFO por definición.
- *¿`peek` puede modificar?* — No, es observadora. Si modificara, rompería la semántica.

**Transición.** "Pero no todas las operaciones que uno se imagina pertenecen al TAD. Veamos cómo clasificarlas."

---

## [F-05] Operaciones de un TAD — 7 min

**Guion del docente.** "Una interfaz no debería ser una lista arbitraria de métodos. Una operación pública pertenece al TAD si respeta su semántica. `push`, `pop`, `peek` sí son operaciones de pila. `at(index)` rompe la abstracción de pila: convierte la pila en acceso aleatorio. Hay tres tipos de operaciones. Constructoras: crean valores del TAD, como `new Stack<T>()` o `emptyStack()`. Transformadoras: cambian el estado abstracto, como `push`, `pop`, `clear`. Observadoras: consultan sin romper la abstracción, como `peek`, `isEmpty`, `size`. Esta clasificación no es decorativa: decide qué publicar y qué no."

**Conceptos clave a enfatizar.**
- La pertenencia de una operación al TAD depende de la **semántica**, no de la comodidad.
- `at(index)` rompe la abstracción pila → no pertenece.
- Tres tipos: constructoras, transformadoras, observadoras.
- Decidir qué publicar es decidir qué promesas asumir.

**Preguntas anticipadas.**
- *¿`clear` pertenece?* — Sí, puede ser operación válida de pila: vacía el estado abstracto sin romper LIFO.
- *¿Y `size`?* — Es observadora: consulta sin romper la abstracción.

**Transición.** "Antes de implementar, una distinción que casi siempre se confunde: encapsulamiento no es ocultamiento de información."

---

## [F-06] Encapsulamiento ≠ ocultamiento de información — 8 min

**Guion del docente.** "Esto lo veo confundir siempre. Encapsulamiento responde: ¿qué datos y operaciones forman una unidad? Ocultamiento de información responde: ¿qué decisiones internas pueden cambiar? No son sinónimos. Encapsular agrupa. Ocultar información protege cambios futuros. El error común del encapsulamiento es poner todo en una clase enorme. El error común del ocultamiento es exponer campos, arrays o conexiones. La interfaz pública responde: ¿qué promesas recibe el cliente? Y su error es publicar helpers por comodidad. La invariante responde: ¿qué debe ser siempre cierto? Y su error es permitir estados imposibles. Cuatro preguntas, cuatro errores. Si las confunden, el diseño se degrada."

**Conceptos clave a enfatizar.**
- Encapsulamiento = agrupar datos y operaciones en una unidad.
- Ocultamiento de información = proteger decisiones internas que pueden cambiar.
- Interfaz pública = promesas que recibe el cliente.
- Invariante = lo que debe ser siempre cierto.
- Confundirlos produce clases enormes, representación expuesta, helpers públicos o estados imposibles.

**Preguntas anticipadas.**
- *¿Java los separa?* — Parcialmente: `private` oculta, la clase agrupa. Pero la clase enorme sigue siendo un error de encapsulamiento.
- *¿Una invariante y un assert?* — El assert verifica en runtime; la invariante es una propiedad del diseño que el tipo debería hacer inverificable.

**Transición.** "Construyamos el TAD en TypeScript. Ahí vamos a ver los cuatro conceptos en acción."

---

## [F-07] Implementación de Stack en TypeScript — 8 min

**Guion del docente.** "TypeScript permite expresar el TAD con una clase genérica. Miren: `class Stack<T>` con `#items: T[] = []`. El símbolo `#` es propiedad privada real, no el `private` de TypeScript que solo afecta el tipado. El cliente usa operaciones: `push`, `pop`, `peek`, `isEmpty`. No toca la estructura interna. `pop` devuelve `T | undefined` porque la pila puede estar vacía: ese `undefined` es el error definido del TAD. `peek` usa `this.#items.at(-1)` para mirar el tope sin remover. `isEmpty` consulta length. Todo respeta la semántica LIFO. Esta clase es un TAD pila: nombre, operaciones, semántica e invariantes, todo en una sola unidad."

**Conceptos clave a enfatizar.**
- `#items` es privacidad real en TypeScript (no solo tipado).
- `T | undefined` modela el error definido (pila vacía).
- `peek` con `at(-1)` observa sin remover.
- El cliente usa operaciones; no toca la estructura interna.

**Preguntas anticipadas.**
- *¿`#` vs `private`?* — `#` es privacidad de runtime (ES2022); `private` es solo de tipado. Para un TAD, `#` es más seguro.
- *¿Por qué `T | undefined` y no lanzar?* — Porque el TAD define `pop()` como *puede no devolver elemento*. Lanzar sería otra decisión de diseño válida, pero distinta.

**Transición.** "Ahora: ¿qué operaciones conviene exponer en la interfaz? No todas las que se pueden implementar."

---

## [F-08] ¿Qué debe exponer una interfaz? — 8 min

**Guion del docente.** "La interfaz debe respetar la semántica del TAD. Miren la tabla. `clear()`: conviene, puede ser operación válida de pila. `toArray()`: depende, debe devolver copia o vista de solo lectura. `at(index)`: no, convierte la pila en acceso aleatorio. Si una operación revela la representación, deja de ser abstracción. La interfaz pública es un contrato: cada método que publicamos es una promesa que el cliente asume. Publicar de más es asumir promesas de más. Por eso la interfaz no es una lista de todo lo que se puede hacer con la clase: es la lista de lo que respeta la semántica del TAD."

**Conceptos clave a enfatizar.**
- La interfaz respeta la semántica del TAD, no la lista de métodos posibles.
- `clear()` sí conviene; `toArray()` depende; `at(index)` no.
- `toArray(): readonly T[]` → vista de solo lectura como compromiso.
- Publicar de más = asumir promesas de más.

**Preguntas anticipadas.**
- *¿`toArray` por qué depende?* — Si devuelve el array interno, expone la representación. Si devuelve copia o vista de solo lectura, respeta la abstracción.
- *¿Y `contains(x)`?* — Sería observadora, podría pertenecer. Pero hay que decidir si la pila debe ofrecer búsqueda o si eso rompe la abstracción.

**Transición.** "Justamente `toArray` nos lleva a un patrón clave: la copia defensiva."

---

## [F-09] Copia defensiva — 7 min

**Guion del docente.** "Miren el mal diseño: `toArray(): T[]` devuelve `this.#items`. Eso expone la representación interna. El cliente puede hacer `pila.toArray().push(99)` y modificar la pila sin pasar por `push`. Eso rompe todo. El mejor diseño: `toArray(): readonly T[]` devuelve `[...this.#items]`, una copia superficial. El cliente recibe una vista nueva; si la muta, no afecta a la pila. La copia defensiva protege la representación privada. Es un patrón simple pero decisivo: cualquier método que devuelva la estructura interna debe devolver una copia o una vista de solo lectura."

**Conceptos clave a enfatizar.**
- Devolver `this.#items` directamente expone la representación.
- `[...this.#items]` es copia superficial: aísla la estructura.
- `readonly T[]` refuerza la inmutabilidad de la vista en el tipado.
- La copia defensiva protege la representación privada.

**Preguntas anticipadas.**
- *¿Copia superficial alcanza?* — Para tipos primitivos sí. Para objetos mutables internos, no: habría que copiar profundo o devolver vistas inmutables recursivas.
- *¿Costo de performance?* — Hay, pero es el precio del encapsulamiento. Si la pila es enorme, se puede devolver un iterador de solo lectura.

**Transición.** "Si protegemos bien la representación, ganamos algo más: independencia de representación."

---

## [F-10] Independencia de representación — 8 min

**Guion del docente.** "Dos implementaciones pueden tener el mismo contrato. Miren la tabla. `ArrayStack<T>` usa array `T[]`. `LinkedStack<T>` usa nodos enlazados. `BoundedStack<T>` usa array con capacidad máxima. `PersistentStack<T>` usa una estructura inmutable compartida. El cliente que usa `Stack<T>` no cambia al cambiar la implementación, salvo que cambie el contrato. Cambia solo si cambia el contrato. No cambia si conserva LIFO. El cliente no debe saber si la pila usa array, nodos o buffer. Esa es la independencia de representación: poder cambiar el *cómo* sin romper el *quién*."

**Conceptos clave a enfatizar.**
- Mismo contrato → múltiples implementaciones intercambiables.
- `ArrayStack`, `LinkedStack`, `BoundedStack`, `PersistentStack`: cuatro representaciones, un contrato.
- El cliente cambia solo si cambia el contrato, no si cambia la representación.
- Independencia de representación = poder cambiar el *cómo* sin romper el *quién*.

**Preguntas anticipadas.**
- *¿Y si una implementación tiene complejidad distinta?* — El contrato no fija complejidad. Si el cliente depende de O(1) y una implementación es O(n), el contrato debería documentarlo o restringirlo.
- *¿Esto es el principio de sustitución de Liskov?* — Está relacionado: LSP exige que las subtipos respeten el contrato. Aquí hablamos de implementaciones del mismo contrato.

**Transición.** "Para que esta independencia sea efectiva, necesitamos separar especificación e implementación sintácticamente."

---

## [F-11] Separación entre especificación e implementación — 8 min

**Guion del docente.** "Miren el código. La interfaz `Stack<T>` declara `push`, `pop`, `peek` y `readonly size`. La clase `ArrayStack<T>` implementa esa interfaz con `#items: T[]`. La interfaz dice qué promete. La implementación decide cómo se cumple. Esta separación es la que permite la independencia de representación que vimos antes. Si mañana escribo `LinkedStack<T>`, implemento la misma interfaz con otra representación. El cliente que depende de `Stack<T>` no se entera. Esa es la diferencia entre depender de un contrato y depender de una implementación."

**Conceptos clave a enfatizar.**
- `interface Stack<T>` declara el contrato; `class ArrayStack<T>` lo implementa.
- `readonly size: number` en la interfaz → observable sin mutación.
- `get size(): number` en la clase → calcula sin exponer el campo.
- La separación sintáctica habilita la independencia de representación.

**Preguntas anticipadas.**
- *¿Por qué `readonly size` y no `size()`?* — Es una decisión de estilo. `readonly` declara propiedad observable; `size()` declara método. Ambos respetan el TAD.
- *¿Una interfaz puede tener implementación?* — En TypeScript, sí (métodos por defecto). Pero para un TAD puro, conviene que la interfaz solo declare.

**Transición.** "Hasta acá hablamos de tipos. Pero hay una frontera más gruesa: el módulo."

---

## [F-12] Módulo como frontera de visibilidad — 8 min

**Guion del docente.** "Un módulo decide qué nombres salen al exterior. Miren `stack.ts`. Exporto `Stack` como tipo y `ArrayStack` como clase. Pero `NodeStack<T>` y `validarCapacidad` no los exporto: son detalles internos del módulo. Exportado → parte de la frontera pública. No exportado → detalle interno del módulo. TypeScript separa contrato y cuerpo con `interface` y `class`. La interfaz `IStack<T>` declara; la clase `ArrayStack<T>` implementa con `private readonly datos`. Esa es la frontera: lo que exporto es promesa, lo que no exporto es implementación. El módulo es la unidad de visibilidad, no la clase."

**Conceptos clave a enfatizar.**
- El módulo decide qué nombres son públicos (`export`) y cuáles son internos.
- `NodeStack` y `validarCapacidad` son internos: no salen del archivo.
- `interface` + `class` separa contrato y cuerpo dentro del módulo.
- El módulo es la unidad de visibilidad, no la clase.

**Preguntas anticipadas.**
- *¿Un módulo es un archivo?* — En TypeScript, sí: cada archivo es un módulo. En otros lenguajes, un módulo puede agrupar varios archivos.
- *¿`private` y `#` son lo mismo?* — No: `private` es de tipado, `#` es de runtime. Para frontera de módulo, `export`/`no export` es lo decisivo.

**Transición.** "Pero los módulos no viven aislados: importan de otros. Veamos los tipos de dependencia."

---

## [F-13] Imports, dependencias y compilación separada — 8 min

**Guion del docente.** "Compilación separada no significa compilar a ciegas. El compilador necesita contratos. Miren la tabla. `import type { Stack }` es dependencia estática de tipos: alcanza con el contrato. `import { ArrayStack }` es dependencia de implementación: hay que preguntarse si es correcto acoplarme a ella. `import { compare } from "./order.js"` es dependencia funcional: ¿pertenece a este módulo? `import "./polyfill"` es dependencia por efecto lateral: ¿está documentada? Cada import es una decisión de acoplamiento. El código de abajo muestra lo correcto: `import type { Stack }` para depender solo del contrato. La función `mover` opera sobre cualquier `Stack<T>` sin saber si es `ArrayStack` o `LinkedStack`. Esa es la compilación separada bien entendida."

**Conceptos clave a enfatizar.**
- Cuatro tipos de import: estática de tipos, de implementación, funcional, por efecto lateral.
- Cada import es una decisión de acoplamiento.
- `import type` → dependencia solo del contrato (lo más débil).
- Compilación separada ≠ compilar a ciegas: el compilador necesita contratos.

**Preguntas anticipadas.**
- *¿`import type` se borra en runtime?* — Sí, el compilador lo elimina. Es solo para chequeo de tipos.
- *¿Qué pasa si importo implementación sin necesitarla?* — Me acoplo a detalles que pueden cambiar. Mejor importar solo el contrato.

**Transición.** "Último concepto: los genéricos. Cómo reutilizar la abstracción sin mezclar tipos."

---

## [F-14] Genéricos — 8 min

**Guion del docente.** "Sin genéricos: `NumberStack`, `StringStack`, `UserStack`. Una clase por cada tipo. Con genéricos: `Stack<T>` parametriza el tipo una sola vez. Miren el código. `new ArrayStack<number>()` crea una pila de números. `numeros.push("hola")` es error: string no es number. `numeros.pop()` devuelve `number | undefined`. El genérico reutiliza la abstracción sin mezclar tipos. Pero hay más: las interfaces pueden ser restricciones. `Comparable<T>` declara `compareTo(other: T): number`. `SortedSet<T extends Comparable<T>` exige que `T` sea comparable. Esa es la idea: el genérico no es solo un placeholder, es una restricción que el compilador hace cumplir."

**Conceptos clave a enfatizar.**
- Sin genéricos: una clase por tipo (duplicación).
- Con genéricos: `Stack<T>` parametriza una sola vez.
- `push("hola")` en `ArrayStack<number>` → error de tipado.
- `T extends Comparable<T>` → restricción: el tipo debe ser comparable.
- El genérico es polimorfismo paramétrico: misma abstracción, tipos distintos.

**Preguntas anticipadas.**
- *¿Esto es sobrecarga?* — No. Sobrecarga es ad hoc polymorphism (mismo nombre, cuerpos distintos). Genéricos es parametric polymorphism (mismo cuerpo, tipos distintos).
- *¿`T extends Comparable<T>` es recursivo?* — Sí, el tipo se refiere a sí mismo. Es común en patrones como Comparable o Cloneable.

**Transición.** "Cerramos con un repaso de las cuatro ideas."

---

## [F-15] Repaso y cierre — 8 min

**Guion del docente.** "Cuatro ideas para llevarse. Un TAD protege una representación: nombre, operaciones, semántica e invariantes. Una interfaz transforma decisiones en promesas: lo que publico es lo que asumo. Un módulo controla qué nombres son públicos: la frontera de visibilidad. Un genérico reutiliza la abstracción sin mezclar tipos: polimorfismo paramétrico. Si se llevan estas cuatro, se llevan la clase. La próxima clase vamos a pasar del módulo aislado a la composición de abstracciones: cómo se combinan módulos sin perder las fronteras que hoy construimos."

**Conceptos clave a enfatizar.**
- TAD protege representación.
- Interfaz transforma decisiones en promesas.
- Módulo controla qué nombres son públicos.
- Genérico reutiliza sin mezclar tipos.

**Preguntas anticipadas.**
- *¿En el TP vamos a implementar un TAD?* — Sí, van a implementar un TAD con interfaz, módulo y genérico. La guía de estudio y el TP salen a continuación.
- *¿Qué lectura recomienda?* — Sebesta capítulo 11 y Gabbrielli capítulo 9. Las referencias completas están en esta minuta.

**Transición.** "Gracias. La próxima clase: del módulo aislado a la composición de abstracciones."

---

## Resumen de tiempos

| Filmina | Título | Minutos |
|---|---|---|
| F-00 | Portada 13A | 3 |
| F-01 | Ruta de la clase | 8 |
| F-02 | El problema: acoplamiento a la representación | 8 |
| F-03 | TAD: Tipo Abstracto de Datos | 8 |
| F-04 | La pila como ejemplo mínimo | 7 |
| F-05 | Operaciones de un TAD | 7 |
| F-06 | Encapsulamiento ≠ ocultamiento de información | 8 |
| F-07 | Implementación de Stack en TypeScript | 8 |
| F-08 | ¿Qué debe exponer una interfaz? | 8 |
| F-09 | Copia defensiva | 7 |
| F-10 | Independencia de representación | 8 |
| F-11 | Separación entre especificación e implementación | 8 |
| F-12 | Módulo como frontera de visibilidad | 8 |
| F-13 | Imports, dependencias y compilación separada | 8 |
| F-14 | Genéricos | 8 |
| F-15 | Repaso y cierre | 8 |
| **Total** | | **120** |