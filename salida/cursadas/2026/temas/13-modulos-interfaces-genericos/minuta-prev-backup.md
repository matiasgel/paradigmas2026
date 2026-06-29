# Minuta - Clase 13B - Modulos, interfaces y genericos

> Duracion total: 120 minutos
> Objetivo docente: explicar el eje Sebesta de ADT, encapsulamiento, modulos, compilacion separada y genericos sin repetir la clase 13A.
> Regla de frontera: 13A queda reservada para subprogramas, parametros, sobrecarga, closures y activation records. 13B usa esos conceptos como prerequisito, pero no los vuelve a desarrollar.

---

## [F-00] Portada 13B - 2 min

**Que decir:** Abrir con una reformulacion simple: "en 13A miramos una operacion aislada; hoy miramos como un conjunto de operaciones se vuelve una frontera estable". Presentar la pregunta de la clase: que debe ver el cliente y que debe quedar oculto para que el programa pueda cambiar.

**Conceptos clave:** ADT, interfaz, modulo, generico, frontera de cambio.

**Pregunta anticipada:** "Vamos a volver a ver sobrecarga?" Responder que no: sobrecarga fue 13A; hoy los genericos aparecen como herramienta para tipos y modulos reutilizables.

**Transicion:** "Primero marco exactamente la frontera con la clase anterior."

---

## [F-01] Puente: 13A termina donde 13B empieza - 4 min

**Que decir:** Recorrer la tabla de izquierda a derecha. Subrayar que 13B no se entiende sin 13A, pero tampoco la repite. El perfil de una operacion se convierte en parte de una interfaz; los tipos de parametros y retornos permiten verificar contratos; los generic functions abren la puerta a generic ADTs.

**Conceptos clave:** reutilizacion de prerequisitos, no solapamiento, cambio de escala.

**Pregunta anticipada:** "Si una interfaz tiene metodos, eso no es otra vez subprogramas?" Responder: si, cada metodo es un subprograma; la novedad de 13B es la unidad mayor que los agrupa y decide visibilidad.

**Transicion:** "Ahora veamos el mapa de la clase para no perdernos en conceptos parecidos."

---

## [F-02] Ruta de la clase - 2 min

**Que decir:** Presentar los cuatro bloques como escalones. ADT responde como usar un tipo sin ver su almacenamiento. Interfaz responde que operaciones puede asumir el cliente. Modulo responde donde queda la frontera de nombres y dependencias. Genericos responden como no duplicar estructuras por tipo. Usar "interfaz publica", "declaracion" y "unidad de compilacion" como vocabulario central; no llevar la explicacion al plano de servicios o plataformas.

**Conceptos clave:** ADT, interfaz, modulo, generico, progresion Sebesta.

**Pregunta anticipada:** "Interfaz y modulo son lo mismo?" Responder que no: una interfaz describe capacidades; un modulo agrupa nombres, codigo y dependencias.

**Transicion:** "El primer problema aparece cuando el cliente conoce demasiado."

---

## [F-03] El problema: los clientes se pegan a detalles - 4 min

**Que decir:** Mostrar el ejemplo `pila.datos[0] = 99`. Explicar que ese cliente ya no esta usando una pila: esta manipulando el array interno. La consecuencia pedagogica es fuerte: si el cliente toca la representacion, la representacion deja de ser privada aunque la documentacion diga lo contrario.

**Conceptos clave:** acoplamiento accidental, representacion expuesta, perdida de libertad de cambio.

**Pregunta anticipada:** "Pero si funciona, cual es el problema?" Responder: funciona hasta que se cambia el array por otra estructura; el codigo externo quedo escrito contra una decision interna.

**Transicion:** "Sebesta formaliza la solucion con el tipo de dato abstracto."

---

## [F-04] Sebesta: un ADT se define por operaciones, no por almacenamiento - 5 min

**Que decir:** Definir ADT con tres ideas: nombre del tipo, operaciones publicas e invariantes. Aclarar que "abstracto" no quiere decir complicado: quiere decir que el cliente usa el tipo por su comportamiento observable, no por su representacion.

**Conceptos clave:** representacion oculta, operaciones publicas, invariante, LIFO.

**Pregunta anticipada:** "ADT es una clase?" Responder: una clase puede implementar un ADT, pero el concepto de ADT es anterior y mas general que la POO.

**Transicion:** "Para que el ADT funcione, no alcanza con agrupar: hay que ocultar decisiones."

---

## [F-05] Encapsular no alcanza si no se ocultan decisiones - 4 min

**Que decir:** Diferenciar cuidadosamente encapsulamiento e information hiding. Encapsular es poner juntos datos y operaciones. Information hiding es decidir que detalles pueden cambiar sin que el cliente se entere. Usar la frase: "un modulo puede estar encapsulado y aun asi filtrar demasiada informacion".

**Conceptos clave:** encapsulamiento, information hiding, interfaz publica, invariante.

**Pregunta anticipada:** "Entonces todo deberia ser privado?" Responder que no; lo publico debe ser lo que el cliente necesita para cumplir su tarea, no todo lo que existe.

**Transicion:** "La Stack es el ejemplo minimo porque su regla observable es muy clara."

---

## [F-06] La pila enseña la idea porque tiene una regla simple - 5 min

**Que decir:** Explicar LIFO con una analogia rapida: una pila de platos. El ultimo plato que pongo arriba es el primero que puedo sacar. Luego conectar la analogia con `push`, `pop`, `peek` e `isEmpty`.

**Conceptos clave:** LIFO, operaciones esenciales, comportamiento observable.

**Pregunta anticipada:** "Por que `isEmpty` es parte del contrato?" Responder que permite preguntar por un estado observable del ADT sin mirar la representacion interna.

**Transicion:** "Veamos como se expresa esto en TypeScript."

---

## [F-07] TypeScript puede expresar el ADT con una clase generica - 5 min

**Que decir:** Recorrer el codigo lentamente. `datos` es privado; `push`, `pop` y `peek` son las operaciones. Aclarar que `T` se explicara mas adelante: por ahora basta entender que la pila puede guardar elementos de algun tipo.

**Conceptos clave:** `private`, clase generica, operaciones publicas, representacion interna.

**Pregunta anticipada:** "Si `private` es de TypeScript, existe en JavaScript?" Responder brevemente que `private` protege en compilacion; la privacidad runtime se vera en F-13.

**Transicion:** "Ahora probemos el criterio: que operaciones merecen entrar a la interfaz?"

---

## [F-08] Pregunta de diseno: que debe exponer una Stack? - 4 min

**Que decir:** Dar 60 segundos para que el aula clasifique `clear`, `toArray` y `at`. Luego guiar: `clear` puede ser legitima; `toArray` depende de si devuelve copia o referencia interna; `at` contradice la semantica LIFO porque vuelve aleatorio el acceso.

**Conceptos clave:** semantica del ADT, operacion esencial, fuga de representacion.

**Pregunta anticipada:** "Y `contains`?" Responder que puede ser valido, pero deberia documentar costo y semantica; no es esencial para toda Stack.

**Transicion:** "La prueba real del ADT es cambiar la implementacion sin cambiar clientes."

---

## [F-09] Independencia de representacion: dos cuerpos, mismo contrato - 5 min

**Que decir:** Comparar `ArrayStack` y `LinkedStack`. Insistir: si el cliente solo usa `push/pop/peek`, no le importa la estructura interna. Si conoce `datos[0]`, la independencia se perdio.

**Conceptos clave:** independencia de representacion, implementaciones alternativas, contrato estable.

**Pregunta anticipada:** "Pero algunas implementaciones tienen costos distintos." Responder que eso tambien puede ser parte del contrato si importa: complejidad esperada, capacidad maxima o garantias de performance.

**Transicion:** "Por eso la regla de lectura de codigo es mirar primero el contrato."

---

## [F-10] Regla de lectura: mirar primero el contrato - 3 min

**Que decir:** Mostrar que `pila: IStack<string>` no revela clase concreta. El cliente sabe que puede apilar strings y recuperar strings o `undefined`; no sabe si hay array, lista o estructura persistente.

**Conceptos clave:** programar contra interfaz, tipo declarado, ocultamiento de clase concreta.

**Pregunta anticipada:** "Entonces nunca deberia usar clases concretas?" Responder que alguna parte del sistema debe construirlas; la regla es no propagarlas donde basta el contrato.

**Transicion:** "Formalizamos esa separacion entre contrato y cuerpo."

---

## [F-11] Interfaz e implementacion tienen responsabilidades distintas - 5 min

**Que decir:** Usar la tabla para separar cuatro niveles. La interfaz contiene promesas publicas. La implementacion contiene decisiones internas. El cliente llama lo permitido. Los tests de contrato verifican que toda implementacion cumpla lo mismo.

**Conceptos clave:** contrato observable, implementacion, cliente, tests de contrato.

**Pregunta anticipada:** "Los tests tambien son parte del contrato?" Responder que no son la interfaz formal, pero vuelven ejecutable la semantica esperada.

**Transicion:** "Ahora lo escribimos en TypeScript con `interface` y `class`."

---

## [F-12] TypeScript separa contrato y cuerpo con `interface` y `class` - 5 min

**Que decir:** Recorrer primero `IStack<T>` completo. Luego mostrar que `ArrayStack<T>` promete cumplirlo. Destacar que el cliente puede declarar variables del tipo interfaz, aunque el objeto real sea una clase.

**Conceptos clave:** `interface`, `implements`, contrato generico, sustitucion.

**Pregunta anticipada:** "Que pasa si `ArrayStack` se olvida de `peek`?" Responder: el compilador rechaza la clase porque no cumple `IStack<T>`.

**Transicion:** "Hay un detalle de TypeScript importante: no toda privacidad ocurre en el mismo momento."

---

## [F-13] TypeScript tiene dos niveles de privacidad - 3 min

**Que decir:** Explicar sin profundizar demasiado: `private` es verificacion de TypeScript; `#datos` es privacidad del JavaScript moderno. `readonly` no vuelve inmutable el contenido de un array: evita reasignar la referencia.

**Conceptos clave:** privacidad estatica, privacidad runtime, `readonly`, copia defensiva.

**Pregunta anticipada:** "Cual usamos en la materia?" Responder: para estudiar ADTs alcanza `private`; para produccion moderna conviene considerar `#` si hace falta proteccion runtime.

**Transicion:** "Hasta aca hablamos de tipos. Ahora subimos al modulo."

---

## [F-14] Un modulo selecciona que nombres salen al exterior - 5 min

**Que decir:** Explicar que `export` es una decision de diseno. Si exporto una clase, funcion o helper, la convierto en parte de la superficie observable. Si no la exporto, queda como detalle interno del modulo.

**Conceptos clave:** modulo, exportacion selectiva, helper privado, frontera publica.

**Pregunta anticipada:** "Por que no exportar todo para testear?" Responder: porque testear detalles internos congela decisiones privadas. Preferir tests de contrato o tests del comportamiento publico.

**Transicion:** "Los imports muestran la otra mitad de la frontera: de que depende el modulo."

---

## [F-15] Leer imports es leer dependencias entre modulos - 4 min

**Que decir:** Leer la tabla como lectura de dependencias entre modulos. `import type` dice "solo necesito la interfaz para compilar". Importar una clase concreta dice "me ato a una implementacion". Importar otro modulo local introduce una dependencia que debe estar justificada.

**Conceptos clave:** dependencia explicita, import type, dependencia concreta, efecto global.

**Pregunta anticipada:** "Un import siempre es malo?" Responder: no; un import es informacion. Lo malo es una dependencia injustificada o demasiado amplia.

**Transicion:** "Veamos un cliente que importa solo lo necesario."

---

## [F-16] El modulo cliente deberia importar lo minimo necesario - 5 min

**Que decir:** Mostrar que `cliente.ts` no conoce `ArrayStack<T>`. Solo necesita una interfaz `IStack<T>`. Esa es la idea modular en el nivel del lenguaje: el cliente compila contra operaciones declaradas y no contra la representacion.

**Conceptos clave:** interfaz de tipo, implementacion concreta, modulo cliente, compilacion contra declaraciones.

**Pregunta anticipada:** "Donde se decide la implementacion real?" Responder: en otra unidad del programa que construye la pila concreta; esa decision no pertenece al modulo cliente si el cliente solo necesita `IStack<T>`.

**Transicion:** "Sebesta y Louden conectan esto con compilacion separada."

---

## [F-17] Compilacion separada no significa compilar a ciegas - 5 min

**Que decir:** Explicar la diferencia central: compilar independiente es no conocer nada de otros modulos; compilar separado es compilar unidades por separado, pero verificando contra sus interfaces. TypeScript puede leer `.d.ts` y verificar llamadas sin tener que reanalizar todo el cuerpo.

**Conceptos clave:** compilacion separada, compilacion independiente, `.d.ts`, especificacion.

**Pregunta anticipada:** "Por que esto importa hoy si todo lo hace el build tool?" Responder: porque explica por que los cambios de interfaz son caros y los cambios internos son baratos.

**Transicion:** "Modula-2 lo muestra en una forma muy pura."

---

## [F-18] Modula-2 muestra la separacion de forma clasica - 4 min

**Que decir:** Presentar `DEFINITION MODULE` como contrato publico y `IMPLEMENTATION MODULE` como cuerpo oculto. No detenerse en la sintaxis; el objetivo es que vean la idea historica que TypeScript reinterpreta con `interface`, `export` y `.d.ts`.

**Conceptos clave:** definition module, implementation module, cliente compilando contra especificacion.

**Pregunta anticipada:** "Esto existe en otros lenguajes?" Responder: Ada tiene package specification y package body; C/C++ usan headers, aunque con otros compromisos.

**Transicion:** "En TypeScript, esa separacion aparece especialmente en archivos de declaraciones."

---

## [F-19] Los archivos `.d.ts` publican una interfaz de compilacion - 2 min

**Que decir:** Explicar que `.d.ts` contiene declaraciones de tipos sin cuerpo de implementacion. Es la forma TypeScript de permitir que un cliente compile contra una interfaz declarada. Mantenerlo en el nivel de lenguaje: declaraciones, cuerpos, unidades y compilacion separada.

**Conceptos clave:** declaracion, `.d.ts`, interfaz compilable, cuerpo oculto.

**Pregunta anticipada:** "Entonces `.d.ts` es como el DEFINITION MODULE?" Responder: pedagogicamente si, cumple un rol parecido: declara lo que el cliente puede conocer sin mostrar el cuerpo.

**Transicion:** "Ahora volvemos a los ADTs, pero con parametrizacion de tipos."

---

## [F-20] Los genericos vuelven reusable al ADT - 4 min

**Que decir:** Aclarar la frontera con 13A: alla se hablo de generic functions y sobrecarga; aca hablamos de tipos, interfaces y clases genericas. El problema no es llamar una funcion con distintos tipos, sino evitar duplicar una estructura completa por cada tipo de elemento.

**Conceptos clave:** ADT generico, reutilizacion, una implementacion parametrizada.

**Pregunta anticipada:** "Generico y `any` son parecidos?" Responder: no. `any` borra garantias; `T` conserva la relacion entre entrada, almacenamiento y salida.

**Transicion:** "Veamos como `T` viaja por la estructura."

---

## [F-21] `Stack<T>` conserva el tipo de cada elemento - 4 min

**Que decir:** Mostrar los dos ejemplos. `ArrayStack<number>` devuelve `number | undefined`; `ArrayStack<Usuario>` devuelve `Usuario | undefined`. El codigo interno puede ser igual, pero el contrato instanciado cambia.

**Conceptos clave:** parametro de tipo, instanciacion, preservacion de tipo.

**Pregunta anticipada:** "Por que aparece `undefined`?" Responder: porque `pop` o `peek` sobre pila vacia no tienen elemento; esa posibilidad forma parte del contrato.

**Transicion:** "A veces un tipo generico necesita pedir una capacidad extra."

---

## [F-22] Un constraint solo aparece cuando el codigo lo necesita - 4 min

**Que decir:** Explicar que `SortedSet` necesita comparar elementos. Por eso exige `Comparable<T>`. Una `Stack<T>` no ordena, entonces no deberia pedir `Comparable<T>`. Este es un criterio de diseno: pedir la capacidad minima necesaria.

**Conceptos clave:** constraint, capacidad requerida, reutilizacion maxima.

**Pregunta anticipada:** "No es mas seguro pedir siempre muchas capacidades?" Responder: no; reduce reutilizacion y acopla tipos a operaciones que no se usan.

**Transicion:** "Generalizamos el criterio en una tabla."

---

## [F-23] Los constraints son contratos sobre capacidades - 4 min

**Que decir:** Recorrer cada fila. Enfatizar la columna del medio: primero miro que operacion necesito, luego decido el constraint. Si no hay operacion que requiera esa capacidad, el constraint sobra.

**Conceptos clave:** capacidad, constraint minimo, contrato generico.

**Pregunta anticipada:** "Un repository siempre necesita `id`?" Responder: si el contrato incluye `findById`, si; si solo guarda eventos append-only, tal vez no.

**Transicion:** "Los genericos no eliminan el problema de ocultar representacion."

---

## [F-24] Devolver datos internos puede romper el ADT - 4 min

**Que decir:** Explicar la copia superficial. `return [...this.datos]` evita que el cliente modifique el array interno. `readonly T[]` evita operaciones mutantes sobre la copia desde TypeScript. Pero si `T` es un objeto mutable, sus propiedades pueden cambiar.

**Conceptos clave:** fuga de representacion, copia defensiva, `readonly`, mutabilidad superficial.

**Pregunta anticipada:** "Entonces `toArray` siempre esta mal?" Responder: no; esta mal si devuelve la estructura interna o si promete mas inmutabilidad de la que puede garantizar.

**Transicion:** "Cerremos con un caso integrador mas realista."

---

## [F-25] Caso integrador: `Set<T>` como modulo con interfaz - 4 min

**Que decir:** Usar `ISet<T>` para unir ADT, interfaz y modulo sin salir del nivel de lenguaje. `add`, `has` y `delete` son operaciones del conjunto. `buckets` y `rehash` son representacion y algoritmo auxiliar. Si se exponen, el cliente queda acoplado a una implementacion concreta del conjunto.

**Conceptos clave:** interfaz publica, detalle de representacion, operacion del tipo.

**Pregunta anticipada:** "Y si el cliente necesita recorrer todos los elementos?" Responder: puede agregarse una operacion como `values(): readonly T[]`, pero debe documentar que devuelve una copia o vista segura.

**Transicion:** "Hagamos la decision como actividad breve."

---

## [F-26] Actividad breve: decidir una interfaz publica - 4 min

**Que decir:** Dar 90 segundos para votar mentalmente cada candidato. Luego resolver: `size` probablemente pertenece a la interfaz; `values` puede pertenecer si devuelve una vista segura; `rawBuckets` no debe estar porque filtra representacion; `rehash` es algoritmo interno.

**Conceptos clave:** superficie publica, capacidad de dominio, detalle operativo.

**Pregunta anticipada:** "No hay una respuesta unica?" Responder: no siempre; hay criterios. La buena respuesta justifica que promesa se vuelve publica.

**Transicion:** "Cada promesa publica tiene costo de evolucion."

---

## [F-27] Cambiar una interfaz cambia el costo para clientes - 3 min

**Que decir:** Recorrer la tabla destacando dos clases de cambio: cambios internos compatibles y cambios de interfaz. Agregar que cambiar el significado sin cambiar el tipo puede ser incluso mas peligroso porque el compilador no avisa.

**Conceptos clave:** compatibilidad, ruptura sintactica, ruptura semantica, interfaz estable.

**Pregunta anticipada:** "El compilador detecta rupturas semanticas?" Responder: no necesariamente; si el tipo no cambia pero el significado cambia, hacen falta tests de contrato y documentacion precisa.

**Transicion:** "Ahora integramos los niveles de abstraccion del modulo."

---

## [F-28] Sintesis: cada nivel oculta una decision distinta - 4 min

**Que decir:** Presentar la tabla como mapa final. Subprograma oculta instrucciones; ADT oculta representacion; interfaz oculta implementaciones concretas; modulo oculta helpers y dependencias internas; unidad de compilacion oculta cuerpo y dependencias internas.

**Conceptos clave:** jerarquia de abstraccion, ocultamiento progresivo, frontera de cambio.

**Pregunta anticipada:** "Donde queda la POO?" Responder: la POO combina varios de estos niveles: objetos y clases implementan ADTs, interfaces expresan contratos, modulos organizan paquetes.

**Transicion:** "Cerramos con el criterio practico para evaluar un diseno modular."

---

## [F-29] Cierre 13B - 4 min

**Que decir:** Leer los cuatro puntos de cierre. Repetir el criterio final dos veces: "una decision es verdaderamente interna si puede cambiar sin romper clientes". Conectar con el proximo modulo: la concurrencia requiere encapsulamiento, porque sin fronteras claras no se puede razonar que estado puede cambiar al mismo tiempo.

**Conceptos clave:** libertad de cambio, ADT, interfaz, modulo, generico.

**Pregunta anticipada:** "Que deberia poder hacer el alumno despues de esta clase?" Responder: mirar una interfaz o modulo TypeScript y distinguir contrato publico, detalle interno, constraint necesario y dependencia injustificada.

**Transicion:** "La proxima clase cambia la pregunta: que pasa cuando varias partes se ejecutan al mismo tiempo?"

---

## Distribucion temporal

| Rango | Bloque | Minutos |
|---|---|---:|
| F-00 a F-02 | Apertura y frontera con 13A | 8 |
| F-03 a F-10 | ADTs e information hiding | 35 |
| F-11 a F-19 | Interfaces, modulos y compilacion separada | 39 |
| F-20 a F-29 | Genericos, interfaz publica y cierre | 38 |
| **Total** |  | **120** |

## Bibliografia de apoyo

- Sebesta, Robert W. *Concepts of Programming Languages*. Capitulos 11 y 12.
- Louden, Kenneth C.; Lambert, Kenneth A. *Programming Languages: Principles and Practices*. Capitulo 11.
- Gabbrielli, Maurizio; Martini, Simone. *Programming Languages: Principles and Paradigms*. Capitulo 9.
