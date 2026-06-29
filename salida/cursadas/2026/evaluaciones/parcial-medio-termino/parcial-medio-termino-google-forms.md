# Parcial de Medio Termino - Banco para Google Forms

**Materia:** Laboratorio de Programacion y Lenguajes 2026  
**Tipo:** parcial conceptual de medio termino  
**Formato:** 30 preguntas multiple choice, una unica respuesta correcta  
**Estado:** borrador para revision docente antes de publicar en Google Forms  
**Publicacion:** no usar loop de publicacion  
**Nota Forms:** activar "barajar opciones" al cargar el formulario.

## Criterios de diseno

- Preguntas conceptuales, sin consignas capciosas ni opciones deliberadamente ambiguas.
- Cuatro opciones por pregunta, con una respuesta correcta clara.
- Distractores plausibles pero no tramposos: representan confusiones frecuentes.
- Nivel Bloom explicito en cada item.
- Trazabilidad por tema y filmina/minuta cuando corresponde.
- No se reutilizan literalmente las preguntas registradas del cuestionario previo de Tema 12.

## Blueprint

| Tema | Carpeta | Preguntas | Ejes evaluados |
|---|---|---:|---|
| 9.1 | `09.1-variables-binding` | 4 | bindings, l-value/r-value, alcance, tiempo de vida |
| 9.2 | `09.2-aliases-closures-gc` | 4 | aliases, closures, GC, gradual typing |
| 10 | `10-tipos-de-datos` | 4 | tipos, ordinales, ADT, equivalencia de tipos |
| 11 | `11-estructuras-control` | 4 | expresiones, precedencia, control, iteracion |
| 12 | `12-manejo-excepciones` | 4 | excepciones, terminacion, Result, estrategias por lenguaje |
| 13.1 | `13-subprogramas-parametros-sobrecarga` | 3 | TAD, interfaces, modulos, genericos |
| 13.2 | `13-modulos-interfaces-genericos` | 3 | subprogramas, parametros, callbacks, dispatch |
| 15 | `15-concurrencia-paralelismo` | 4 | concurrencia, carreras, sincronizacion, modelos |

## Version para estudiantes

### Pregunta 1

En el contexto de variables, que significa "binding"?

A. La transformacion automatica de un tipo numerico en otro tipo numerico.  
B. La eliminacion de una variable cuando termina el programa completo.  
C. El proceso de asociar dos o mas atributos, como nombre, tipo, valor o ubicacion de memoria.  
D. La regla que decide si una funcion puede retornar o no un valor.

### Pregunta 2

Cual afirmacion distingue mejor l-value y r-value?

A. Un l-value identifica una ubicacion asignable; un r-value es el valor que puede leerse o computarse.  
B. Un l-value siempre es una constante; un r-value siempre es una variable mutable.  
C. Un l-value existe solo en lenguajes funcionales; un r-value existe solo en lenguajes imperativos.  
D. Un l-value es un error de tipo; un r-value es un error de sintaxis.

### Pregunta 3

Que diferencia hay entre alcance y tiempo de vida de una variable?

A. El alcance indica cuanto ocupa en memoria; el tiempo de vida indica que nombre tiene.  
B. El alcance solo aplica al heap; el tiempo de vida solo aplica al stack.  
C. Son sinonimos: ambos significan el tipo estatico de una variable.  
D. El alcance indica donde el nombre es visible; el tiempo de vida indica durante cuanto existe su almacenamiento.

### Pregunta 4

Por que el binding dinamico puede dificultar el razonamiento sobre un programa?

A. Porque impide declarar funciones con parametros.  
B. Porque una misma referencia puede resolverse segun la cadena de llamadas en ejecucion, no solo por la estructura textual.  
C. Porque elimina por completo la posibilidad de usar variables locales.  
D. Porque convierte todos los valores en strings antes de operar.

### Pregunta 5

Que problema aparece cuando dos nombres son aliases del mismo objeto mutable?

A. El programa deja de poder compilar aunque el tipo sea correcto.  
B. El objeto se vuelve automaticamente inmutable.  
C. Modificar el objeto desde un nombre puede afectar lo observado desde el otro.  
D. Cada nombre recibe una copia profunda sin que el programador lo pida.

### Pregunta 6

Que captura una closure?

A. El subprograma junto con el entorno necesario para resolver variables libres.  
B. Solo el resultado numerico de la ultima llamada realizada.  
C. Unicamente los parametros primitivos pasados por valor.  
D. El codigo fuente completo del programa en tiempo de ejecucion.

### Pregunta 7

Cual es la limitacion clasica de reference counting puro?

A. No puede liberar objetos con un unico propietario.  
B. Solo funciona si todos los objetos son strings.  
C. Requiere detener siempre todos los hilos durante varios segundos.  
D. No libera ciclos de objetos que se referencian mutuamente aunque sean inaccesibles.

### Pregunta 8

Que expresa mejor la idea de gradual typing?

A. Obliga a que todos los programas sean completamente dinamicos.  
B. Permite combinar zonas con chequeo estatico y zonas mas dinamicas dentro de un mismo sistema.  
C. Reemplaza los tipos por tests unitarios obligatorios.  
D. Prohibe migrar codigo JavaScript existente.

### Pregunta 9

Que define un tipo de dato en sentido formal?

A. Un conjunto de valores y un conjunto de operaciones validas sobre esos valores.  
B. Un nombre de variable elegido por el programador.  
C. El archivo fisico donde se guarda el programa.  
D. La cantidad de comentarios que tiene una definicion.

### Pregunta 10

Que caracteriza a un tipo ordinal?

A. Sus valores necesariamente son objetos en heap.  
B. Sus valores solo pueden ser funciones anonimas.  
C. Sus valores forman un conjunto discreto con un orden y sucesor/predecesor definidos.  
D. Sus valores no pueden compararse bajo ninguna regla.

### Pregunta 11

En tipos algebraicos, cual es la diferencia entre producto y suma?

A. Producto significa herencia; suma significa sobrecarga.  
B. Producto combina componentes simultaneos; suma representa alternativas posibles.  
C. Producto solo existe en C; suma solo existe en TypeScript.  
D. Producto elimina informacion; suma duplica todos los campos.

### Pregunta 12

Que diferencia hay entre equivalencia nominal y estructural de tipos?

A. La nominal compara valores en runtime; la estructural compara nombres de archivos.  
B. La nominal no existe en lenguajes compilados; la estructural no existe en lenguajes interpretados.  
C. Son dos nombres para la misma regla de coercion implicita.  
D. La nominal depende del nombre declarado; la estructural depende de la forma o miembros compatibles.

### Pregunta 13

Que diferencia conceptual hay entre expresion y sentencia?

A. Una expresion siempre modifica memoria; una sentencia nunca ejecuta nada.  
B. Una expresion solo aparece en lenguajes logicos; una sentencia solo en lenguajes funcionales.  
C. Una expresion produce un valor; una sentencia organiza el flujo o provoca un efecto.  
D. No hay diferencia: todos los lenguajes las tratan igual.

### Pregunta 14

Para que sirven precedencia y asociatividad?

A. Para determinar como se agrupan los operadores cuando una expresion no tiene parentesis suficientes.  
B. Para decidir que variable se aloja en heap.  
C. Para seleccionar que excepcion captura un handler.  
D. Para convertir automaticamente un programa sincrono en asincrono.

### Pregunta 15

Que ventaja aporta la evaluacion de corto circuito en operadores booleanos?

A. Garantiza que todas las subexpresiones se evaluen siempre.  
B. Convierte cualquier condicion en una sentencia `switch`.  
C. Elimina la necesidad de tipos booleanos.  
D. Puede evitar evaluar una parte innecesaria o insegura de la condicion.

### Pregunta 16

Que expresa mejor un invariante de bucle?

A. Una variable que cambia de tipo en cada vuelta.  
B. Una propiedad que debe mantenerse antes y despues de cada iteracion para razonar sobre correccion.  
C. Una condicion que solo se verifica cuando el programa falla.  
D. Una optimizacion del compilador para borrar el bucle.

### Pregunta 17

Que es una excepcion en el diseno de lenguajes?

A. Un evento anomalo que interrumpe el flujo normal y requiere un mecanismo de manejo separado.  
B. Cualquier valor booleano falso.  
C. Una funcion que siempre retorna `null`.  
D. Un comentario especial entendido por el compilador.

### Pregunta 18

Que distingue al modelo de terminacion frente al de reanudacion?

A. En terminacion el programa siempre ignora el error y sigue como si nada.  
B. En reanudacion no existe ningun handler.  
C. En terminacion no se vuelve al punto exacto del fallo; el control continua desde el handler o se propaga.  
D. Ambos modelos exigen que todas las excepciones sean checked.

### Pregunta 19

Que ventaja conceptual tiene representar fallos con `Result<T,E>`?

A. Oculta todos los errores para que el llamador no los vea.  
B. Hace explicito en el tipo que una operacion puede producir exito o error.  
C. Hace que el runtime capture automaticamente cualquier excepcion externa.  
D. Reemplaza la necesidad de validar datos de entrada.

### Pregunta 20

Que criterio ayuda a elegir entre `throw/catch` y errores como valores?

A. Siempre usar `throw/catch`, incluso para resultados esperados del dominio.  
B. Siempre ignorar el error y retornar un valor por defecto.  
C. Elegir segun el nombre mas corto de la funcion.  
D. Si el fallo forma parte esperada del contrato de la API, conviene hacerlo visible para el llamador.

### Pregunta 21

Que define mejor a un Tipo Abstracto de Datos (TAD)?

A. Un array concreto expuesto para que el cliente lo manipule directamente.  
B. Un conjunto de operaciones observables y reglas de comportamiento, independiente de la representacion interna.  
C. Un tipo que solo puede implementarse sin metodos.  
D. Una clase cuyo unico objetivo es mostrar todos sus campos internos.

### Pregunta 22

Por que una interfaz no deberia exponer detalles de representacion?

A. Porque limita la libertad de cambiar la implementacion sin romper clientes.  
B. Porque impide que el compilador haga chequeo de tipos.  
C. Porque obliga a usar siempre herencia multiple.  
D. Porque hace imposible documentar operaciones publicas.

### Pregunta 23

Que aporta un generico como `Stack<T>`?

A. Mezclar valores de cualquier tipo sin chequeo.  
B. Convertir una pila en una cola automaticamente.  
C. Reutilizar una abstraccion para distintos tipos manteniendo consistencia de tipos.  
D. Eliminar la necesidad de definir operaciones.

### Pregunta 24

Que diferencia hay entre definicion y llamada de un subprograma?

A. La definicion ocurre en runtime; la llamada ocurre solo al compilar.  
B. La definicion solo existe para procedimientos; la llamada solo para funciones.  
C. Son equivalentes: ambas declaran el mismo nombre.  
D. La definicion establece el contrato y el cuerpo; la llamada activa ese contrato con argumentos concretos.

### Pregunta 25

Que indica un modo de parametro `inout`?

A. Que el parametro solo puede usarse como constante local.  
B. Que el subprograma puede leer el argumento recibido y tambien modificarlo de forma observable.  
C. Que el argumento se elimina al terminar la llamada.  
D. Que la funcion no puede producir efectos.

### Pregunta 26

Por que un callback forma parte del contrato de un subprograma?

A. Porque siempre se ejecuta antes de que empiece el programa.  
B. Porque convierte cualquier funcion en un tipo ordinal.  
C. Porque el subprograma recibe comportamiento externo y debe definir como, cuando y con que efectos lo invoca.  
D. Porque impide que existan errores en tiempo de ejecucion.

### Pregunta 27

Que diferencia central hay entre concurrencia y paralelismo?

A. La concurrencia organiza multiples tareas en progreso; el paralelismo ejecuta tareas simultaneamente en recursos distintos.  
B. La concurrencia solo ocurre en hardware; el paralelismo solo en pseudocodigo.  
C. La concurrencia es sinonimo de asincronia; el paralelismo es sinonimo de excepcion.  
D. No hay diferencia conceptual entre ambos terminos.

### Pregunta 28

Cuando hay una condicion de carrera?

A. Cuando una funcion tarda mucho aunque no comparta ningun dato.  
B. Cuando una variable local se declara con `const`.  
C. Cuando un programa tiene muchas clases.  
D. Cuando el resultado depende del interleaving de accesos concurrentes a estado compartido.

### Pregunta 29

Que protege una seccion critica?

A. Todo el codigo fuente de una aplicacion, incluso partes sin estado compartido.  
B. La region donde el acceso concurrente a un recurso compartido debe controlarse.  
C. Solo las llamadas a funciones puras.  
D. La conversion de strings a numeros.

### Pregunta 30

Que ventaja ofrece el pasaje de mensajes frente a memoria compartida?

A. Garantiza que todos los mensajes sean instantaneos y no puedan fallar.  
B. Elimina cualquier necesidad de disenar contratos entre componentes.  
C. Hace explicito el protocolo de comunicacion y reduce la dependencia de estado mutable compartido.  
D. Convierte automaticamente la ejecucion concurrente en secuencial.

## Clave docente y trazabilidad

| ID | Tema | Bloom | Trazabilidad | Respuesta | Justificacion breve |
|---|---|---|---|---|---|
| PMT-01 | 9.1 | Recordar | filminas F-01/F-02 | C | Binding es asociacion entre atributos de una entidad. |
| PMT-02 | 9.1 | Comprender | filminas F sobre l-value/r-value | A | l-value nombra ubicacion; r-value expresa valor. |
| PMT-03 | 9.1 | Comprender | alcance y lifetime | D | Visibilidad del nombre y existencia del almacenamiento son dimensiones distintas. |
| PMT-04 | 9.1 | Analizar | alcance dinamico | B | La resolucion depende de la cadena de llamadas. |
| PMT-05 | 9.2 | Comprender | aliases | C | El aliasing comparte objeto mutable. |
| PMT-06 | 9.2 | Recordar | closures | A | Closure = codigo + entorno capturado. |
| PMT-07 | 9.2 | Comprender | reference counting | D | RC puro no detecta ciclos inaccesibles. |
| PMT-08 | 9.2 | Comprender | gradual typing | B | Combina chequeo estatico y dinamico. |
| PMT-09 | 10 | Recordar | filminas F-04 | A | Tipo = valores + operaciones. |
| PMT-10 | 10 | Comprender | tipos ordinales | C | Los ordinales tienen orden discreto. |
| PMT-11 | 10 | Comprender | tipos producto/suma | B | Producto acumula campos; suma elige variante. |
| PMT-12 | 10 | Comprender | equivalencia nominal/estructural | D | Nominal mira nombre; estructural mira forma. |
| PMT-13 | 11 | Comprender | expresiones y sentencias | C | Expresion produce valor; sentencia estructura flujo/efecto. |
| PMT-14 | 11 | Recordar | precedencia/asociatividad | A | Definen agrupamiento de operadores. |
| PMT-15 | 11 | Aplicar | short-circuit | D | Evita evaluar partes innecesarias o riesgosas. |
| PMT-16 | 11 | Comprender | bucles/invariantes | B | Invariante sostiene razonamiento de correccion. |
| PMT-17 | 12 | Recordar | filminas F-03 | A | Excepcion separa flujo normal y manejo anomalo. |
| PMT-18 | 12 | Comprender | filminas F-06 | C | Terminacion no reanuda en el punto del fallo. |
| PMT-19 | 12 | Comprender | filminas F-11 | B | Result hace explicito exito/error en el tipo. |
| PMT-20 | 12 | Evaluar | filminas F-15 | D | La estrategia debe reflejar el contrato esperado. |
| PMT-21 | 13.1 | Comprender | 13A F-03/F-04 | B | TAD se define por operaciones e invariantes observables. |
| PMT-22 | 13.1 | Analizar | 13A F-06/F-10 | A | Ocultar representacion preserva independencia. |
| PMT-23 | 13.1 | Aplicar | 13A F-14 | C | Generics reutilizan abstraccion con tipos consistentes. |
| PMT-24 | 13.2 | Comprender | 13B F-02 | D | Definir y llamar son roles distintos del contrato. |
| PMT-25 | 13.2 | Comprender | 13B F-05/F-06 | B | inout implica lectura y mutacion observable. |
| PMT-26 | 13.2 | Analizar | 13B F-14/F-15 | C | Callback recibido requiere protocolo de invocacion. |
| PMT-27 | 15 | Comprender | tema 15 F-02/F-03 | A | Concurrencia es progreso intercalado; paralelismo simultaneidad real. |
| PMT-28 | 15 | Comprender | tema 15 F-05 | D | Carrera depende del interleaving sobre estado compartido. |
| PMT-29 | 15 | Recordar | tema 15 F-06 | B | La seccion critica protege acceso compartido. |
| PMT-30 | 15 | Comprender | tema 15 F-12/F-13 | C | Mensajes explicitan protocolo y reducen estado compartido. |

## Tabla para Google Forms

Formato sugerido para importacion manual o script posterior: una pregunta por fila. Todas son de opcion multiple con una sola correcta.

| id | titulo | opcion_a | opcion_b | opcion_c | opcion_d | correcta | puntos | tema | bloom |
|---|---|---|---|---|---|---|---:|---|---|
| PMT-01 | En el contexto de variables, que significa "binding"? | La transformacion automatica de un tipo numerico en otro tipo numerico. | La eliminacion de una variable cuando termina el programa completo. | El proceso de asociar dos o mas atributos, como nombre, tipo, valor o ubicacion de memoria. | La regla que decide si una funcion puede retornar o no un valor. | C | 1 | 9.1 | Recordar |
| PMT-02 | Cual afirmacion distingue mejor l-value y r-value? | Un l-value identifica una ubicacion asignable; un r-value es el valor que puede leerse o computarse. | Un l-value siempre es una constante; un r-value siempre es una variable mutable. | Un l-value existe solo en lenguajes funcionales; un r-value existe solo en lenguajes imperativos. | Un l-value es un error de tipo; un r-value es un error de sintaxis. | A | 1 | 9.1 | Comprender |
| PMT-03 | Que diferencia hay entre alcance y tiempo de vida de una variable? | El alcance indica cuanto ocupa en memoria; el tiempo de vida indica que nombre tiene. | El alcance solo aplica al heap; el tiempo de vida solo aplica al stack. | Son sinonimos: ambos significan el tipo estatico de una variable. | El alcance indica donde el nombre es visible; el tiempo de vida indica durante cuanto existe su almacenamiento. | D | 1 | 9.1 | Comprender |
| PMT-04 | Por que el binding dinamico puede dificultar el razonamiento sobre un programa? | Porque impide declarar funciones con parametros. | Porque una misma referencia puede resolverse segun la cadena de llamadas en ejecucion, no solo por la estructura textual. | Porque elimina por completo la posibilidad de usar variables locales. | Porque convierte todos los valores en strings antes de operar. | B | 1 | 9.1 | Analizar |
| PMT-05 | Que problema aparece cuando dos nombres son aliases del mismo objeto mutable? | El programa deja de poder compilar aunque el tipo sea correcto. | El objeto se vuelve automaticamente inmutable. | Modificar el objeto desde un nombre puede afectar lo observado desde el otro. | Cada nombre recibe una copia profunda sin que el programador lo pida. | C | 1 | 9.2 | Comprender |
| PMT-06 | Que captura una closure? | El subprograma junto con el entorno necesario para resolver variables libres. | Solo el resultado numerico de la ultima llamada realizada. | Unicamente los parametros primitivos pasados por valor. | El codigo fuente completo del programa en tiempo de ejecucion. | A | 1 | 9.2 | Recordar |
| PMT-07 | Cual es la limitacion clasica de reference counting puro? | No puede liberar objetos con un unico propietario. | Solo funciona si todos los objetos son strings. | Requiere detener siempre todos los hilos durante varios segundos. | No libera ciclos de objetos que se referencian mutuamente aunque sean inaccesibles. | D | 1 | 9.2 | Comprender |
| PMT-08 | Que expresa mejor la idea de gradual typing? | Obliga a que todos los programas sean completamente dinamicos. | Permite combinar zonas con chequeo estatico y zonas mas dinamicas dentro de un mismo sistema. | Reemplaza los tipos por tests unitarios obligatorios. | Prohibe migrar codigo JavaScript existente. | B | 1 | 9.2 | Comprender |
| PMT-09 | Que define un tipo de dato en sentido formal? | Un conjunto de valores y un conjunto de operaciones validas sobre esos valores. | Un nombre de variable elegido por el programador. | El archivo fisico donde se guarda el programa. | La cantidad de comentarios que tiene una definicion. | A | 1 | 10 | Recordar |
| PMT-10 | Que caracteriza a un tipo ordinal? | Sus valores necesariamente son objetos en heap. | Sus valores solo pueden ser funciones anonimas. | Sus valores forman un conjunto discreto con un orden y sucesor/predecesor definidos. | Sus valores no pueden compararse bajo ninguna regla. | C | 1 | 10 | Comprender |
| PMT-11 | En tipos algebraicos, cual es la diferencia entre producto y suma? | Producto significa herencia; suma significa sobrecarga. | Producto combina componentes simultaneos; suma representa alternativas posibles. | Producto solo existe en C; suma solo existe en TypeScript. | Producto elimina informacion; suma duplica todos los campos. | B | 1 | 10 | Comprender |
| PMT-12 | Que diferencia hay entre equivalencia nominal y estructural de tipos? | La nominal compara valores en runtime; la estructural compara nombres de archivos. | La nominal no existe en lenguajes compilados; la estructural no existe en lenguajes interpretados. | Son dos nombres para la misma regla de coercion implicita. | La nominal depende del nombre declarado; la estructural depende de la forma o miembros compatibles. | D | 1 | 10 | Comprender |
| PMT-13 | Que diferencia conceptual hay entre expresion y sentencia? | Una expresion siempre modifica memoria; una sentencia nunca ejecuta nada. | Una expresion solo aparece en lenguajes logicos; una sentencia solo en lenguajes funcionales. | Una expresion produce un valor; una sentencia organiza el flujo o provoca un efecto. | No hay diferencia: todos los lenguajes las tratan igual. | C | 1 | 11 | Comprender |
| PMT-14 | Para que sirven precedencia y asociatividad? | Para determinar como se agrupan los operadores cuando una expresion no tiene parentesis suficientes. | Para decidir que variable se aloja en heap. | Para seleccionar que excepcion captura un handler. | Para convertir automaticamente un programa sincrono en asincrono. | A | 1 | 11 | Recordar |
| PMT-15 | Que ventaja aporta la evaluacion de corto circuito en operadores booleanos? | Garantiza que todas las subexpresiones se evaluen siempre. | Convierte cualquier condicion en una sentencia switch. | Elimina la necesidad de tipos booleanos. | Puede evitar evaluar una parte innecesaria o insegura de la condicion. | D | 1 | 11 | Aplicar |
| PMT-16 | Que expresa mejor un invariante de bucle? | Una variable que cambia de tipo en cada vuelta. | Una propiedad que debe mantenerse antes y despues de cada iteracion para razonar sobre correccion. | Una condicion que solo se verifica cuando el programa falla. | Una optimizacion del compilador para borrar el bucle. | B | 1 | 11 | Comprender |
| PMT-17 | Que es una excepcion en el diseno de lenguajes? | Un evento anomalo que interrumpe el flujo normal y requiere un mecanismo de manejo separado. | Cualquier valor booleano falso. | Una funcion que siempre retorna null. | Un comentario especial entendido por el compilador. | A | 1 | 12 | Recordar |
| PMT-18 | Que distingue al modelo de terminacion frente al de reanudacion? | En terminacion el programa siempre ignora el error y sigue como si nada. | En reanudacion no existe ningun handler. | En terminacion no se vuelve al punto exacto del fallo; el control continua desde el handler o se propaga. | Ambos modelos exigen que todas las excepciones sean checked. | C | 1 | 12 | Comprender |
| PMT-19 | Que ventaja conceptual tiene representar fallos con Result<T,E>? | Oculta todos los errores para que el llamador no los vea. | Hace explicito en el tipo que una operacion puede producir exito o error. | Hace que el runtime capture automaticamente cualquier excepcion externa. | Reemplaza la necesidad de validar datos de entrada. | B | 1 | 12 | Comprender |
| PMT-20 | Que criterio ayuda a elegir entre throw/catch y errores como valores? | Siempre usar throw/catch, incluso para resultados esperados del dominio. | Siempre ignorar el error y retornar un valor por defecto. | Elegir segun el nombre mas corto de la funcion. | Si el fallo forma parte esperada del contrato de la API, conviene hacerlo visible para el llamador. | D | 1 | 12 | Evaluar |
| PMT-21 | Que define mejor a un Tipo Abstracto de Datos (TAD)? | Un array concreto expuesto para que el cliente lo manipule directamente. | Un conjunto de operaciones observables y reglas de comportamiento, independiente de la representacion interna. | Un tipo que solo puede implementarse sin metodos. | Una clase cuyo unico objetivo es mostrar todos sus campos internos. | B | 1 | 13.1 | Comprender |
| PMT-22 | Por que una interfaz no deberia exponer detalles de representacion? | Porque limita la libertad de cambiar la implementacion sin romper clientes. | Porque impide que el compilador haga chequeo de tipos. | Porque obliga a usar siempre herencia multiple. | Porque hace imposible documentar operaciones publicas. | A | 1 | 13.1 | Analizar |
| PMT-23 | Que aporta un generico como Stack<T>? | Mezclar valores de cualquier tipo sin chequeo. | Convertir una pila en una cola automaticamente. | Reutilizar una abstraccion para distintos tipos manteniendo consistencia de tipos. | Eliminar la necesidad de definir operaciones. | C | 1 | 13.1 | Aplicar |
| PMT-24 | Que diferencia hay entre definicion y llamada de un subprograma? | La definicion ocurre en runtime; la llamada ocurre solo al compilar. | La definicion solo existe para procedimientos; la llamada solo para funciones. | Son equivalentes: ambas declaran el mismo nombre. | La definicion establece el contrato y el cuerpo; la llamada activa ese contrato con argumentos concretos. | D | 1 | 13.2 | Comprender |
| PMT-25 | Que indica un modo de parametro inout? | Que el parametro solo puede usarse como constante local. | Que el subprograma puede leer el argumento recibido y tambien modificarlo de forma observable. | Que el argumento se elimina al terminar la llamada. | Que la funcion no puede producir efectos. | B | 1 | 13.2 | Comprender |
| PMT-26 | Por que un callback forma parte del contrato de un subprograma? | Porque siempre se ejecuta antes de que empiece el programa. | Porque convierte cualquier funcion en un tipo ordinal. | Porque el subprograma recibe comportamiento externo y debe definir como, cuando y con que efectos lo invoca. | Porque impide que existan errores en tiempo de ejecucion. | C | 1 | 13.2 | Analizar |
| PMT-27 | Que diferencia central hay entre concurrencia y paralelismo? | La concurrencia organiza multiples tareas en progreso; el paralelismo ejecuta tareas simultaneamente en recursos distintos. | La concurrencia solo ocurre en hardware; el paralelismo solo en pseudocodigo. | La concurrencia es sinonimo de asincronia; el paralelismo es sinonimo de excepcion. | No hay diferencia conceptual entre ambos terminos. | A | 1 | 15 | Comprender |
| PMT-28 | Cuando hay una condicion de carrera? | Cuando una funcion tarda mucho aunque no comparta ningun dato. | Cuando una variable local se declara con const. | Cuando un programa tiene muchas clases. | Cuando el resultado depende del interleaving de accesos concurrentes a estado compartido. | D | 1 | 15 | Comprender |
| PMT-29 | Que protege una seccion critica? | Todo el codigo fuente de una aplicacion, incluso partes sin estado compartido. | La region donde el acceso concurrente a un recurso compartido debe controlarse. | Solo las llamadas a funciones puras. | La conversion de strings a numeros. | B | 1 | 15 | Recordar |
| PMT-30 | Que ventaja ofrece el pasaje de mensajes frente a memoria compartida? | Garantiza que todos los mensajes sean instantaneos y no puedan fallar. | Elimina cualquier necesidad de disenar contratos entre componentes. | Hace explicito el protocolo de comunicacion y reduce la dependencia de estado mutable compartido. | Convierte automaticamente la ejecucion concurrente en secuencial. | C | 1 | 15 | Comprender |
