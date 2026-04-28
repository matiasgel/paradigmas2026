# Minuta de Clase — Tema 08: Paradigma OO: TypeScript + Smalltalk

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Institución:** UNTDF — Instituto IDEI  
**Docente:** Matías Gel  
**Duración:** 120 minutos | **Clase:** 1 de 1 | **Módulo IV — Semana 7**  
**Estado:** APROBADO (diseño 2026-04-28)  
**Generado por:** Dr. Roberto (class-writer) | **Fecha:** 2026-04-28  

---

## Objetivos de la clase

| Nivel Bloom | Objetivo |
|-------------|----------|
| Recordar | Enumerar los cuatro pilares del OO: encapsulamiento, abstracción, herencia, polimorfismo |
| Comprender | Explicar qué significa "todo es un objeto" en Smalltalk y por qué TypeScript no lo cumple igual |
| Aplicar | Implementar jerarquía de clases con herencia y polimorfismo en TypeScript |
| Analizar | Comparar el mismo problema en Smalltalk vs. TypeScript identificando diferencias filosóficas |
| Evaluar | Argumentar ventajas y compromisos de TypeScript respecto a OO puro |
| Crear | Modelar un mini-dominio en TypeScript aplicando los principios OO |

---

## Recursos para la clase

- **TypeScript Playground:** https://www.typescriptlang.org/play (tener abierto antes de entrar)
- **Pharo:** https://pharo.org/ (descargado, o usar demo online en https://pharo.org/try)
- **Pizarrón:** para el diagrama de metaclases y la comparación final
- **TP08:** link de GitHub Classroom listo para anunciar al cierre

---

## BLOQUE 0 — Recapitulación y apertura (5 min)

---

### [F-01] Portada — Paradigma OO: TypeScript + Smalltalk

**Tiempo:** 1 min  
**Qué decir:**
- Proyectar la portada mientras los estudiantes se ubican.
- *"Hoy arrancamos el Módulo IV — Paradigma Orientado a Objetos. Lo vamos a estudiar desde dos lenguajes muy distintos: Smalltalk, que es OO puro en su forma más radical, y TypeScript, que es lo que ustedes ya están usando."*
- *"Al final de la clase van a poder decir qué significa exactamente que un lenguaje es OO, y qué compromisos hace TypeScript respecto a la visión original."*

**Conceptos clave:** [solo introducción — no hay contenido técnico aquí]  
**Transición:** pasar a F-02 sin demora.

---

### [F-02] ¿Qué sumamos hoy al cursado?

**Tiempo:** 2 min  
**Qué decir:**
- *"¿Qué paradigmas vimos hasta ahora?"* → esperar respuesta: funcional (Haskell/Elixir), lógico (Prolog).
- *"El imperativo fue la base desde siempre — TypeScript imperativo lo usaron desde el día uno. OO es una extensión del imperativo: le agrega estructura para organizar el estado."*
- *"Entonces hoy no estudiamos un cuarto paradigma desde cero — estamos estudiando cómo el imperativo evoluciona cuando decimos: el estado vive adentro de los objetos y se accede por mensajes."*
- Dejar que algún estudiante intente responder la pregunta generadora: *"¿Qué tiene OO que funcional y lógico no tienen?"*
- Respuesta esperada: **identidad de entidades, estado mutable encapsulado, comunicación por mensajes**.

**Conceptos clave:** OO como extensión del imperativo; estado encapsulado; mensajes.  
**Preguntas anticipadas:**
- *"¿OO no es totalmente distinto al imperativo?"* → No: loops, if, variables mutables siguen siendo el motor. OO organiza ese motor en torno a objetos.  
**Transición:** *"Antes de empezar con código — les muestro los cuatro pilares del paradigma que vamos a trabajar hoy."*

---

### [F-03] Los 4 pilares — adelanto

**Tiempo:** 2 min  
**Qué decir:**
- Presentar la tabla brevemente — **no explicar cada pilar todavía**, solo mostrar el mapa.
- *"Estos cuatro conceptos son el núcleo de la clase y del Parcial 1. Los vamos a ver primero en Smalltalk y después en TypeScript."*
- *"Encapsulamiento: cómo protejo el estado. Abstracción: qué muestro al exterior. Herencia: cómo reutilizo. Polimorfismo: cómo trato distintos tipos uniformemente."*
- Enfatizar: *"Al final de la clase tienen que poder poner un ejemplo de código para cada uno de estos cuatro."*

**Conceptos clave:** los 4 pilares como mapa de navegación de la clase.  
**Transición:** *"Empecemos por la historia — ¿de dónde viene OO?"*

---

## BLOQUE 1 — Historia y filosofía del OO (20 min)

---

### [F-04] Simula 67 — el primer paso

**Tiempo:** 4 min  
**Qué decir:**
- *"El primer lenguaje OO nació en Noruega en 1967 — se llamaba Simula. Nació para simular sistemas físicos: barcos, puertos, tráfico."*
- Dibujá en el pizarrón: un rectángulo `Barco` con flechas a `velocidad`, `posición`, y un método `moverse()`.
- *"El insight fue: el barco no es una estructura de datos separada de las funciones que la modifican — el barco SABE cómo moverse. El estado y el comportamiento van juntos."*
- *"Antes de Simula: tenías una función `mover(barco, velocidad)`. Después: `barco.moverse()`. Parece pequeño — es enorme."*
- Preguntar: *"¿Cuál de los dos es más fácil de razonar cuando tenés 50 tipos de objetos distintos?"*

**Conceptos clave:** encapsulamiento como origen del paradigma; datos + comportamiento juntos.  
**Preguntas anticipadas:**
- *"¿Simula era OO puro?"* → No, era ALGOL extendido. El OO puro vino con Smalltalk.  
**Transición:** *"Simula plantó la semilla. Alan Kay la llevó al extremo."*

---

### [F-05] Alan Kay — la visión original

**Tiempo:** 5 min  
**Qué decir:**
- Leer la cita en voz alta: *"The big idea is 'messaging'…"*
- *"Kay trabajaba en Xerox PARC en los 70s — el mismo laboratorio donde se inventó el mouse, la GUI, Ethernet. Smalltalk fue el lenguaje que él diseñó."*
- *"Para Kay, el centro del paradigma NO eran las clases — eran los mensajes. Los objetos son como células: autónomos, encapsulados, que se comunican mandándose mensajes."*
- *"Los tres principios: (1) todo es un objeto, (2) solo mensajes, (3) cada objeto tiene su propia memoria. Si rompés cualquiera de esos tres — ya no es OO puro."*
- Dato interesante: *"Kay después dijo que se arrepentía de haber llamado a esto 'orientado a objetos' — debería haberse llamado 'orientado a mensajes'."*

**Conceptos clave:** Kay, Smalltalk, mensajes como mecanismo central, los 3 principios originales.  
**Preguntas anticipadas:**
- *"¿Por qué mensajes y no llamadas a métodos?"* → Un mensaje es una petición asíncrona — el objeto decide cómo responder. Una llamada es síncrona y directa. En Smalltalk: enviás el mensaje, el objeto decide si puede responderlo.  
**Transición:** *"¿TypeScript cumple estos tres principios?"*

---

### [F-06] Kay vs. lo que el mundo hizo después

**Tiempo:** 4 min  
**Qué decir:**
- *"La respuesta rápida: no exactamente. TypeScript tiene primitivos (`number`, `boolean`), lo que viola el principio 'todo es un objeto'."*
- Plantear la tensión: *"¿Importa la pureza filosófica?"*
- *"Smalltalk: podés hacer `5 factorial` — el 5 es un objeto que recibe el mensaje `factorial`. TypeScript: `(5).factorial()` no existe — necesitás `Math.factorial(5)`. El 5 no es un objeto real."*
- Preguntar: *"¿Qué pierden los lenguajes cuando abandonan la pureza de Kay?"*
- Respuestas esperadas: consistencia conceptual, reflexividad (el lenguaje puede inspeccionarse a sí mismo), extensibilidad (podés agregar comportamiento a cualquier cosa).
- *"¿Qué ganan?"* → performance, herramientas de análisis estático, menor curva de aprendizaje para desarrolladores industriales.

**Conceptos clave:** pureza vs. pragmatismo; trade-offs de diseño de lenguajes.  
**Transición:** *"Vean cómo evolucionó esta tensión en la historia."*

---

### [F-07] Evolución del OO — timeline

**Tiempo:** 4 min  
**Qué decir:**
- Recorrer la tabla brevemente — **no detenerse en cada lenguaje**.
- Marcar las columnas importantes: Smalltalk-80 como pico de pureza, Java como primer OO industrial masivo, TypeScript como el último.
- *"En 1967 → Simula: la idea. En 1980 → Smalltalk: la pureza máxima. En 1983 → C++: la industria necesita C con objetos. En 1995 → Java: OO para todos, con JVM. En 2012 → TypeScript: OO sobre JavaScript, con tipos."*
- *"La tendencia clara: a medida que el paradigma se masificó, se volvió más pragmático y menos puro. Hoy se lo usa sin pensar en Kay."*
- Reflexión: *"Smalltalk hoy lo usan en algunas universidades europeas para enseñar OO puro — exactamente como lo vamos a usar nosotros hoy."*

**Conceptos clave:** evolución hacia el pragmatismo; Smalltalk como referencia pedagógica.  
**Transición:** *"Vamos al código de Smalltalk — vean qué significa 'todo es un objeto' de verdad."*

---

## BLOQUE 2 — Smalltalk: OO Puro (25 min)

---

### [F-08] "Todo es un objeto" — sin excepciones

**Tiempo:** 3 min  
**Qué decir:**
- *"En Smalltalk no hay primitivos. El número 5 es una instancia de la clase `SmallInteger`. El `true` es una instancia de la clase `True`. La clase `Animal` en sí misma es una instancia de su metaclase."*
- Mostrar el diagrama de jerarquía: `5 → SmallInteger → Integer → Number → Magnitude → Object`.
- *"Comparen con TypeScript: `typeof 5` les devuelve `"number"` — no es una clase, es un tipo primitivo del runtime de JS. Cuando hacen `(5).toString()` funciona por autoboxing — JS envuelve el 5 en un objeto temporario. Smalltalk no necesita ese truco."*
- Preguntar: *"¿Por qué importa que los números sean objetos?"* → porque podés enviarles cualquier mensaje, definir nuevos métodos en `Number`, usarlos polimórficamente con cualquier otro objeto.

**Conceptos clave:** todo es objeto; ausencia de primitivos; autoboxing de JS.  
**Transición:** directo a ejemplos de código.

---

### [F-09] "Todo es un objeto" — en código

**Tiempo:** 4 min  
**Qué decir:**
- Leer y ejecutar (si tenés Pharo) o mostrar código con resultados.
- *"Ejecuto `5 factorial` — el 5 recibe el mensaje `factorial` y responde `120`. Esto no es una llamada de función — es el objeto 5 eligiendo cómo responder."*
- *"Ahora miren `SmallInteger methodDictionary` — le pido a la clase su diccionario de métodos. La clase es un objeto que tiene métodos, y puedo inspeccionarlos en runtime."*
- *"En TypeScript, `Number.prototype.factorial` no existe — y aunque lo definís con monkey-patching, TypeScript lo desaconseja porque rompe el contrato de tipos."*
- **Ejemplo en vivo para desarrollar:** escribir en Pharo (o mostrar):
  ```smalltalk
  | nums |
  nums := #(1 2 3 4 5).
  nums collect: [:n | n * n].   "→ #(1 4 9 16 25)"
  nums select: [:n | n > 3].    "→ #(4 5)"
  nums inject: 0 into: [:acc :n | acc + n].  "→ 15"
  ```
- *"¿Les recuerda a algo? Es map, filter, reduce — pero implementados como mensajes a la colección."*

**Conceptos clave:** mensajes, colecciones Smalltalk, equivalencia con map/filter/reduce.  
**Preguntas anticipadas:**
- *"¿Smalltalk tiene arrays?"* → `Array`, `OrderedCollection`, `Set`, `Dictionary` — todos son clases.  
**Transición:** *"Un mecanismo clave de Smalltalk: los cascades."*

---

### [F-10] Cascades y `yourself` — sintaxis expresiva

**Tiempo:** 3 min  
**Qué decir:**
- *"El problema: si querés agregar tres elementos a una colección, sin cascades escribís tres líneas repetitivas."*
- *"Con cascades, el `;` repite el receptor — le mandás el mismo mensaje a la misma colección tres veces."*
- *"El `yourself` es el truco clave: sin él, la variable recibe el resultado del último `add:` — que es el string `'tercero'`. Con `yourself`, recibe la colección."*
- Comparar con TypeScript:
  ```typescript
  // Fluent interface — equivalente
  class Builder {
    private items: string[] = [];
    add(item: string) { this.items.push(item); return this; }
    build() { return this.items; }
  }
  const col = new Builder().add("a").add("b").add("c").build();
  ```
- *"En TypeScript esto no es nativo — tenés que diseñar una clase que retorne `this`. En Smalltalk es parte del lenguaje."*

**Conceptos clave:** cascades, `yourself`, fluent interface.  
**Transición:** *"Ahora los tres tipos de mensajes — esto es fundamental para leer Smalltalk."*

---

### [F-11] Mensajes — los tres tipos

**Tiempo:** 3 min  
**Qué decir:**
- *"En Smalltalk hay exactamente tres tipos de mensajes. Necesitan reconocerlos para leer código."*
- *"Unarios: sin argumentos. `5 factorial`, `'hola' size`. Alta precedencia."*
- *"Binarios: un argumento, notación infija. `3 + 4`, `5 > 3`. Precedencia media — pero cuidado: `3 + 4 * 2` da 14, no 11. Los binarios se evalúan de izquierda a derecha."*
- *"Palabras clave: uno o más argumentos. `10 between: 5 and: 15`. Baja precedencia."*
- **Preguntar a la clase:** *"En TypeScript: `[1,2,3].indexOf(2, 0)` — ¿es unario, binario, o keyword?"* → keyword (tiene argumentos nombrados en su origen).
- Marcar bien: *"El operador `+` en Smalltalk es redefinible porque es un mensaje. En TypeScript no se puede redefinir `+`. Esto determina cosas como si puedo hacer `vector1 + vector2` de forma natural."*

**Conceptos clave:** tres tipos de mensajes, precedencia, redefinibilidad de operadores.  
**Transición:** *"Ahora una jerarquía completa en Smalltalk."*

---

### [F-12] Clases y herencia en Smalltalk

**Tiempo:** 4 min  
**Qué decir:**
- Recorrer el código lentamente — es verboso pero declarativo.
- *"En Smalltalk no hay un archivo por clase — todo vive en el sistema de imágenes (image). Definís las clases interactivamente."*
- *"El `^` es el return. El `:=` es la asignación. El `|animales|` declara la variable local."*
- **Ejemplo en vivo para desarrollar** — pedir a un estudiante que prediga el output antes de ejecutar:
  ```smalltalk
  | animales |
  animales := OrderedCollection new.
  animales add: (Animal new nombre: 'Genérico').
  animales add: (Perro new nombre: 'Rex'; raza: 'Labrador'; yourself).
  animales do: [:a | Transcript showCr: a hablar].
  ```
- *"El cliente (`do:`) no sabe nada del tipo real de cada objeto. Solo sabe que entiende `hablar`. Eso es polimorfismo puro."*

**Conceptos clave:** sintaxis de definición de clase, polimorfismo por despacho de mensajes.  
**Preguntas anticipadas:**
- *"¿Hay tipos en Smalltalk?"* → Dinámicos. El sistema descubre en runtime si el objeto entiende el mensaje.  
**Transición:** *"Uno de los mecanismos más únicos de Smalltalk: los bloques."*

---

### [F-13] Bloques — las lambdas de Smalltalk

**Tiempo:** 3 min  
**Qué decir:**
- *"Un bloque en Smalltalk es literalmente un objeto que representa código que no ejecutaste todavía. Igual que una lambda en TypeScript."*
- *"La diferencia: en TypeScript `() => x * x` es una función. En Smalltalk `[:x | x * x]` es un objeto de clase `BlockClosure` — tiene métodos, tiene estado de cierre, puede ser almacenado en una variable."*
- *"Los condicionales e iteradores en Smalltalk son mensajes que reciben bloques como argumentos. No hay `if` como palabra clave — es `ifTrue: [un bloque] ifFalse: [otro bloque]`."*
- Comparar `collect:`, `select:`, `inject:into:` con `map`, `filter`, `reduce`.
- **Preguntar:** *"¿Cuál de ustedes implementó `forEach` desde cero?"* → así funciona `do:` — es un método en `Collection` que toma un bloque y lo evalúa para cada elemento.

**Conceptos clave:** bloques como objetos, relación con lambdas, control de flujo por mensajes.  
**Transición:** *"El concepto más avanzado de Smalltalk: metaclases."*

---

### [F-14] Metaclases — las clases son objetos

**Tiempo:** 4 min  
**Qué decir:**
- *"Esto es lo que hace a Smalltalk verdaderamente diferente. En Smalltalk, la clase `Animal` en sí misma es un objeto."*
- Dibujar en el pizarrón la cadena:
  ```
  Animal → instancia de → Animal class → instancia de → Metaclass → instancia de → Class
  ```
- *"¿Para qué sirve? Para que las clases tengan métodos propios — métodos de clase. En Smalltalk el equivalente de `static` en TypeScript es simplemente un método definido en la metaclase."*
- *"La diferencia: en TypeScript las clases no son ciudadanos de primera clase — no podés guardar la clase en una variable y enviarle mensajes arbitrarios en runtime de la misma manera."*
- **Ejemplo concreto:**
  ```smalltalk
  | clases |
  clases := Array with: Animal with: Perro.
  clases do: [:c | Transcript showCr: c name, ' tiene ', c methodDictionary size printString, ' métodos'].
  ```
- *"Esto en TypeScript requeriría reflection avanzada — en Smalltalk es trivial porque las clases son objetos como cualquier otro."*

**Conceptos clave:** metaclases, clases como objetos, métodos de clase.  
**Preguntas anticipadas:**
- *"¿Es útil esto en práctica?"* → Sí: Pharo usa metaclases para hacer el IDE completamente introspectable. Los frameworks de test en Smalltalk usan esto para descubrir métodos de test automáticamente.  
**Transición:** *"¿Usamos Smalltalk hoy? Sí — se llama Pharo."*

---

### [F-15] Smalltalk hoy — Pharo

**Tiempo:** 4 min — **DEMO EN VIVO**  
**Qué decir:**
- Si tenés Pharo descargado: abrir el Playground y ejecutar el código de la slide.
- Si no: usar la imagen de pantalla de la slide como referencia.
- *"Pharo es Smalltalk moderno — tiene una comunidad activa, se usa en investigación y en enseñanza de OO puro en universidades europeas como la U. de Berna y Inria."*
- Ejecutar:
  ```smalltalk
  | col |
  col := OrderedCollection new.
  1 to: 10 do: [:i | col add: i * i].
  col select: [:n | n > 20].
  ```
- *"El resultado: `OrderedCollection (25 36 49 64 81 100)`. Todo en mensajes, sin una sola función global."*
- *"¿Para qué sirve aprenderlo? Para entender OO puro hace que vean los compromisos de TypeScript con otros ojos."*

**Conceptos clave:** Pharo, Smalltalk activo, OO como herramienta pedagógica.  
**Transición:** *"Pasamos al otro lado — TypeScript OO."*

---

## BLOQUE 3 — TypeScript OO (25 min)

---

### [F-16] Clases en TypeScript — encapsulamiento

**Tiempo:** 4 min  
**Qué decir:**
- *"Ya usaron clases en TypeScript — ahora las vamos a analizar con el vocabulario del paradigma."*
- Recorrer el código de `CuentaBancaria`:
  - `private saldo` → encapsulamiento. *"El saldo no es accesible desde afuera. El objeto decide cómo modificarlo."*
  - `protected titular` → herencia. *"Las subclases pueden acceder. El mundo exterior no."*
  - `readonly numero` → inmutabilidad parcial. *"Una vez asignado, no se puede cambiar."*
- *"Este es el primer pilar en acción: el objeto protege su estado interno. Solo el objeto sabe cómo cambiar el saldo. Si alguien quiere depositar, pasa por `depositar()` — que puede validar, registrar, notificar."*
- **Ejemplo en vivo para desarrollar en TypeScript Playground:**
  ```typescript
  const c = new CuentaBancaria("Ana", "001", 1000);
  c.depositar(500);
  c.retirar(200);
  console.log(c.obtenerSaldo()); // 1300
  c.saldo = 9999;                // ❌ Error de compilación — mostrar el mensaje
  ```

**Conceptos clave:** private, protected, readonly, encapsulamiento real vs. nominal.  
**Transición:** *"El shorthand de constructor reduce el boilerplate."*

---

### [F-17] Shorthand de constructor

**Tiempo:** 2 min  
**Qué decir:**
- *"Si el constructor solo asigna propiedades — TypeScript tiene un atajo."*
- Mostrar las dos versiones. Preguntar: *"¿Cuándo usarían la forma explícita?"* → cuando hay validaciones, transformaciones, lógica.
- *"Regla de oro: si hay lógica → forma explícita. Si solo asigna → shorthand. No abuses del shorthand para ocultar código."*

**Conceptos clave:** shorthand de constructor, cuándo aplicarlo.  
**Transición:** *"Herencia."*

---

### [F-18] Herencia con `extends` — polimorfismo en acción

**Tiempo:** 4 min  
**Qué decir:**
- *"El `super(nombre)` es obligatorio cuando la clase padre tiene constructor. TypeScript lo verifica en compilación."*
- Recorrer `PerroEntrenado extends Perro extends Animal` — tres niveles.
- **Ejemplo en vivo para desarrollar:**
  ```typescript
  const animales: Animal[] = [
    new Animal("Genérico"),
    new Perro("Rex", "Labrador"),
    new PerroEntrenado("Max", "Poodle"),
  ];
  animales.forEach(a => console.log(a.hablar()));
  ```
- *"La variable es `Animal[]` — TypeScript solo garantiza que cada elemento tiene `hablar()`. Pero en runtime ejecuta el método del tipo real. Eso es despacho dinámico."*
- Comparar con Smalltalk: *"En Smalltalk no hay `Animal[]` — la colección acepta cualquier objeto. La diferencia: TypeScript verifica en compilación que todos tengan `hablar()`. Smalltalk lo descubre en runtime."*

**Conceptos clave:** `super()`, despacho dinámico, polimorfismo de inclusión.  
**Preguntas anticipadas:**
- *"¿Puedo hacer `animales[0].describirse()`?"* → No — TypeScript solo ve el tipo declarado `Animal`, que no tiene `describirse()`. Necesitaría un cast.  
**Transición:** *"Interfaces — abstracción sin implementación."*

---

### [F-19] Interfaces — contratos estructurales

**Tiempo:** 3 min  
**Qué decir:**
- *"Una clase puede extender UNA sola clase. Pero puede implementar MÚLTIPLES interfaces — esto resuelve el problema de herencia múltiple de forma segura."*
- *"La interfaz define el contrato: qué métodos existen y qué tipos tienen. No da implementación."*
- **Ejemplo en vivo:**
  ```typescript
  function guardar(obj: Serializable): void {
    const json = obj.serializar();
    console.log("Guardando:", json);
  }
  guardar(new Perro("Rex", "Labrador"));
  ```
- *"La función no sabe que es un `Perro` — solo sabe que tiene `serializar()`. Eso es abstracción."*

**Conceptos clave:** interfaces, múltiple implementación, separación contrato/implementación.  
**Transición:** *"El tipado estructural de TypeScript es un tema aparte."*

---

### [F-20] Tipado estructural — duck typing estático

**Tiempo:** 3 min  
**Qué decir:**
- *"En Java, para que algo sea `Serializable` tenés que declararlo explícitamente: `implements Serializable`. En TypeScript, alcanza con que el objeto tenga la forma correcta."*
- Mostrar el ejemplo de `cuadradoLiteral` — no declara `implements Medible` pero funciona.
- *"Esto se llama tipado estructural o duck typing estático: si camina como un pato y grazna como un pato, TypeScript lo trata como un pato — pero verifica los tipos en compilación, no en runtime."*
- Tabla: estructural (TS) vs. nominal (Java) vs. dinámico (Smalltalk).
- *"¿Cuál es más flexible? Smalltalk. ¿Cuál da más garantías? Java/TS. ¿Cuál es más productivo para un equipo de 20 personas? TS o Java."*

**Conceptos clave:** tipado estructural, nominal, duck typing estático.  
**Transición:** *"Modificadores y clases abstractas."*

---

### [F-21] Modificadores de acceso y clases abstractas

**Tiempo:** 4 min  
**Qué decir:**
- Recorrer la tabla de modificadores — comparar columna TypeScript vs. Smalltalk.
- *"La diferencia más importante con Smalltalk: en Smalltalk todas las variables de instancia son siempre privadas — no hay opción. En TypeScript tenés que elegir."*
- Mostrar la clase `Forma abstract`:
  - `abstract area(): number` → el compilador OBLIGA a que cualquier subclase implemente `area()`.
  - Intentar `new Forma("rojo")` → error de compilación en vivo.
- *"En Smalltalk, `^ self subclassResponsibility` lanza un error en RUNTIME si la subclase olvidó implementar el método. En TypeScript el error es en COMPILACIÓN. ¿Cuál prefieren para trabajar en equipo?"*

**Conceptos clave:** abstract, subclassResponsibility, compilación vs. runtime.  
**Transición:** *"Un principio importante: composición vs. herencia."*

---

### [F-22] Composición vs. herencia

**Tiempo:** 3 min  
**Qué decir:**
- *"Este es un error clásico que se llama anti-patrón de herencia por conveniencia: usar herencia no porque 'es-un' sino porque 'quiero reusar código'."*
- Mostrar `Pila extends Array` — TypeScript lo permite, pero expone métodos de Array que no deberían estar.
- *"Si la pila es un Array, un usuario puede hacer `pila.splice(0, 1)` y romper la abstracción."*
- *"Con composición, la Pila TIENE un array pero no LO ES. Solo expone lo que decide exponer: `push`, `pop`, `tope`, `estaVacia`."*
- **Regla:** *"Herencia: relación semántica real ('Perro ES UN Animal'). Composición: reutilizar comportamiento sin exponer la implementación."*

**Conceptos clave:** composición vs. herencia, principio ES-UN, encapsulamiento.  
**Transición:** *"Ahora lo más importante de la clase — el mismo dominio en los dos lenguajes."*

---

## BLOQUE 4 — Comparación directa: formas geométricas (20 min)

---

### [F-23] El dominio — formas geométricas

**Tiempo:** 2 min  
**Qué decir:**
- *"Van a ver el mismo problema resuelto en Smalltalk y en TypeScript. El dominio es formas geométricas — el mismo que va a estar en el tipo del Parcial 1."*
- *"El requisito: Círculo, Rectángulo y Triángulo. Cada uno calcula área y perímetro. El cliente itera polimórficamente sobre una colección sin saber el tipo concreto."*
- *"Es pequeño pero completo — usa los cuatro pilares."*

**Conceptos clave:** dominio del Parcial 1, los 4 pilares de OO en un solo ejemplo.  
**Transición:** *"Smalltalk primero."*

---

### [F-24] Formas en Smalltalk — OO puro

**Tiempo:** 4 min  
**Qué decir:**
- Recorrer el código. Marcar `^ self subclassResponsibility` — *"si Circulo no implementa `area`, al llamarlo se lanza un error en runtime."*
- Marcar los cascades: `Circulo new radio: 5; color: 'rojo'; yourself`.
- **Ejemplo en vivo o proyectar:**
  ```smalltalk
  | formas |
  formas := OrderedCollection new.
  formas add: (Circulo new radio: 5; color: 'rojo'; yourself).
  formas add: (Rectangulo new ancho: 4 alto: 6; color: 'azul'; yourself).
  formas do: [:f | Transcript showCr: f area printString].
  ```
- *"El `do:` no sabe que hay Círculos y Rectángulos — solo que cada objeto en la colección entiende el mensaje `area`. Polimorfismo puro."*

**Conceptos clave:** polimorfismo por despacho de mensajes, cascades, subclassResponsibility.  
**Transición:** *"Ahora TypeScript — misma estructura, filosofía distinta."*

---

### [F-25] Formas en TypeScript — definición base

**Tiempo:** 4 min  
**Qué decir:**
- *"La estructura es paralela pero con las diferencias de TypeScript: `abstract`, tipos explícitos, verificación en compilación."*
- **Ejemplo en vivo para desarrollar en TypeScript Playground:**
  ```typescript
  const formas: Forma[] = [
    new Circulo(5, "rojo"),
    new Rectangulo(4, 6, "azul"),
  ];
  formas.forEach(f => console.log(f.toString()));
  ```
- Intentar `new Forma("rojo")` → error inmediato en el IDE.
- *"¿Cuál es la ventaja? El IDE me dice antes de ejecutar que no puedo instanciar una clase abstracta. En Smalltalk lo descubrís cuando ejecutás."*

**Conceptos clave:** abstract en compilación, polimorfismo tipado, IDE como herramienta.  
**Transición:** *"Ahora la parte más importante — agregar Triángulo."*

---

### [F-26] Extender el dominio — Principio Open/Closed

**Tiempo:** 4 min  
**Qué decir:**
- *"El Principio Open/Closed dice: el código debe estar abierto para extensión y cerrado para modificación."*
- *"Para agregar Triángulo: solo creo la clase nueva. No toco `Forma`, no toco `Circulo`, no toco `Rectangulo`. El cliente polimórfico no cambia una sola línea."*
- Mostrar la fórmula de Herón — un momento de matemática en la clase:
  - `s = (a + b + c) / 2`
  - `área = √(s(s-a)(s-b)(s-c))`
- **Agregar al ejemplo en vivo:**
  ```typescript
  formas.push(new Triangulo(3, 4, 5, "verde"));
  formas.forEach(f => console.log(f.toString()));
  ```
- *"El triángulo 3-4-5 tiene área 6. Verifiquen: `s = 6`, `√(6*3*2*1) = √36 = 6`. Correcto."*

**Conceptos clave:** Open/Closed Principle, extensión sin modificación, fórmula de Herón.  
**Preguntas anticipadas:**
- *"¿Esto aplica a Smalltalk también?"* → Sí — el OCP es un principio de diseño OO, no de lenguaje.  
**Transición:** *"La tabla comparativa final."*

---

### [F-27] Comparación directa — tabla

**Tiempo:** 3 min  
**Qué decir:**
- Recorrer la tabla fila por fila, enfatizando:
  - `abstract` → compilación (TS) vs. `subclassResponsibility` → runtime (Smalltalk).
  - Iteración: `do:` (Smalltalk) vs. `forEach` (TS) — funcionalmente idénticos.
  - Redefinir `+` → solo Smalltalk.
  - Error de tipo → compilación (TS) vs. runtime (Smalltalk).
- *"¿Cuál de los dos prefieres para un proyecto de producción con 10 desarrolladores? TypeScript — por las verificaciones en compilación. ¿Cuál para entender OO en profundidad? Smalltalk."*

**Conceptos clave:** síntesis comparativa, compilación vs. runtime, pragmatismo.  
**Transición:** *"Una reflexión guiada antes de continuar."*

---

### [F-28] Reflexión guiada

**Tiempo:** 3 min  
**Qué decir:**
- Dar 30 segundos para pensar a cada pregunta antes de abrir el debate.
- Pregunta 1: *"¿En qué caso Smalltalk es más expresivo?"* → Esperar: mensajes redefinibles, metaclases, cascades.
- Pregunta 2: *"¿En qué caso TypeScript es más robusto para equipos?"* → Esperar: errores en compilación, IDE, refactoring seguro.
- Pregunta 3: *"¿Cuál sigue más la visión de Kay?"* → Smalltalk, sin discusión.
- *"La tensión entre pureza y pragmatismo no tiene una respuesta correcta — tiene un contexto. El mismo diseñador puede elegir Smalltalk para investigar y TypeScript para producción."*

**Conceptos clave:** pureza vs. pragmatismo, contexto de decisión.  
**Transición:** *"Bloque rápido de OO en el mundo moderno."*

---

## BLOQUE IA — OO en el desarrollo moderno (10 min)

---

### [F-29] OO + LLMs — el paradigma dominante

**Tiempo:** 5 min  
**Qué decir:**
- *"Los LLMs como Copilot fueron entrenados con miles de millones de líneas de código — la mayoría en lenguajes OO: Python, Java, TypeScript."*
- *"Práctica implicación: si escribís código OO bien estructurado, Copilot es mucho más preciso. El contexto del paradigma está en los pesos del modelo."*
- **Demo en vivo con Copilot (si está disponible):**
  - Escribir `abstract class Vehiculo {` y ver qué sugiere Copilot.
  - Pedirle: *"Creá una jerarquía de notificaciones con Email, SMS y Push usando abstract y polimorfismo."*
- *"El prompt mismo usa el vocabulario OO — Copilot reconoce el patrón y completa la jerarquía completa."*
- Reflexión: *"¿Esto reemplaza entender OO? No — Copilot se equivoca con exactamente los errores que no entiende: herencia mal usada, composición vs. herencia, violaciones de encapsulamiento."*

**Conceptos clave:** LLMs y código OO, prompting orientado al paradigma.  
**Transición:** *"Una tabla de patrones de diseño OO."*

---

### [F-30] Patrones GoF — OO destilado

**Tiempo:** 5 min  
**Qué decir:**
- *"Los patrones GoF (Gang of Four, 1994) son soluciones OO reutilizables. No son algoritmos — son estructuras de diseño."*
- *"Ya usamos uno sin nombrarlo: Template Method. La clase abstracta `Forma` define `toString()` que llama a `area()` abstracto — eso es Template Method."*
- Recorrer la tabla brevemente:
  - **Strategy:** algoritmos intercambiables — *"¿querés que el precio se calcule con descuento o sin? Pasá la estrategia como objeto."*
  - **Observer:** notificación — *"EventEmitter de Node.js es Observer."*
  - **Factory Method:** *"`crearForma('circulo')` devuelve un `Circulo` sin que el cliente sepa el tipo."*
  - **Decorator:** *"Middleware de Express: `app.use(auth)` agrega autenticación sin modificar el handler."*
- *"Los van a ver en detalle en TPs posteriores."*

**Conceptos clave:** patrones GoF, Template Method, Strategy, Observer.  
**Transición:** *"Cierre y síntesis."*

---

## BLOQUE 5 — Cierre (15 min)

---

### [F-31] Síntesis — Smalltalk vs. TypeScript

**Tiempo:** 3 min  
**Qué decir:**
- Recorrer la tabla de síntesis fila por fila, rápido.
- Enfatizar las filas más importantes para el parcial:
  - Todo es objeto: TS ❌ (primitivos), Smalltalk ✅.
  - Interfaces: TS ✅, Smalltalk ❌.
  - Redefinir operadores: Smalltalk ✅, TS ❌.
  - Verificación: TS compilación, Smalltalk runtime.
- *"Esta tabla entera la tienen que poder reproducir mentalmente para el parcial."*

**Conceptos clave:** síntesis de todas las diferencias.  
**Transición:** *"Los cuatro pilares con código."*

---

### [F-32] Los 4 pilares — síntesis con código

**Tiempo:** 3 min  
**Qué decir:**
- *"El fragmento de código de esta slide usa los cuatro pilares a la vez — 10 líneas."*
- Señalar en el código:
  - `abstract class Forma` → abstracción
  - `protected color` → encapsulamiento
  - `class Circulo extends Forma` → herencia
  - `formas.forEach(f => f.area())` → polimorfismo
- *"En el parcial: si les doy un fragmento de código OO, tienen que poder señalar dónde está cada pilar y explicarlo."*

**Conceptos clave:** los 4 pilares de OO en un solo fragmento, mapa del Parcial 1.  
**Transición:** *"El mapa de los tres paradigmas del cursado."*

---

### [F-33] Mapa de paradigmas del cursado

**Tiempo:** 3 min  
**Qué decir:**
- Recorrer la tabla — enfatizar las diferencias en **modelo de estado** (la columna más importante para el parcial):
  - Funcional: inmutable.
  - Lógico: hechos y unificación.
  - OO: mutable, encapsulado en objetos.
- *"Para el parcial: el mismo problema puede modelarse en dos paradigmas. La pregunta va a ser: ¿cómo cambia el modelo de estado? ¿Cómo cambia el modelo de control?"*
- *"OO extiende el imperativo — por eso la columna OO tiene 'loops/if' además del 'despacho de mensajes'."*

**Conceptos clave:** tres paradigmas del cursado, modelo de estado, mapa para el Parcial 1.  
**Transición:** *"Lo que tienen que saber específicamente."*

---

### [F-34] Conceptos clave — Parcial 1

**Tiempo:** 2 min  
**Qué decir:**
- Leer la lista en voz alta, despacio.
- *"Cada ítem de esta lista es una pregunta potencial del parcial: 'Defina encapsulamiento y muestre un ejemplo en TypeScript.' 'Explique la diferencia entre tipado estructural y nominal.' 'Compare composición vs. herencia'."*
- *"Tienen la guía de estudio completa en el repositorio de la materia — tiene 20 preguntas de autoestudio con respuestas."*

**Conceptos clave:** mapa del Parcial 1.  
**Transición:** *"El TP que lanzamos hoy."*

---

### [F-35] TP08 — GitHub + autograding

**Tiempo:** 2 min  
**Qué decir:**
- *"El link al assignment de GitHub Classroom lo pongo en el canal ahora mismo."*
- *"Aceptan el assignment → se crea un repo personal para cada uno. Hacen push → GitHub Actions ejecuta los tests automáticamente. Ven la nota en el commit."*
- *"Hay cuatro ejercicios: jerarquía básica, interfaces, dominio libre, y uno opcional comparando con Smalltalk."*
- *"El stack: TypeScript 5 + Vitest para los tests. El `package.json` ya está configurado en el template."*
- *"Fecha límite: una semana. El autograding da feedback inmediato — úsenlo."*

**Conceptos clave:** flujo GitHub Classroom, autograding, Vitest.  
**Transición:** *"Cierre."*

---

### [F-36] Cierre — Parcial 1

**Tiempo:** 2 min  
**Qué decir:**
- *"La próxima semana es el Parcial 1. Dominios: OO + funcional o OO + lógico para el mismo problema."*
- *"¿Qué estudiar? La guía de estudio del repositorio + los TPs anteriores. Si pueden resolver el dominio de formas en TypeScript y argumentar las decisiones de diseño, están listos."*
- *"¿Preguntas sobre la clase de hoy?"*
- Dejar 1 minuto de preguntas libres.

**Conceptos clave:** Parcial 1, cómo prepararse.

---

## Notas post-clase

*(Completar después de dar la clase)*

- Conceptos que generaron más debate: ___
- Preguntas que surgieron y no estaban anticipadas: ___
- Tiempo real por bloque: B0=__ / B1=__ / B2=__ / B3=__ / B4=__ / IA=__ / B5=__
- Ajustes para la próxima vez: ___
