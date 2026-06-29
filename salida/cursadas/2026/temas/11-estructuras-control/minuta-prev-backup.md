# Minuta de Clase - Tema 11

## Expresiones y Estructuras de Control

> Docente: Matias Gel
> Estado: APROBADO (autoaprobacion solicitada)
> Referencia de soporte: filminas.md (F-00 a F-44)
> Enfoque: desarrollo teorico integral y profundo (sin restriccion de tiempo)
> Bibliografia principal: Sebesta cap. 7
> Bibliografia auxiliar: Gabbrielli-Martini, Louden

---

## Modo de uso de esta minuta

- Esta minuta esta pensada para lectura docente previa y conduccion en aula.
- Cada entrada referencia una filmina y define foco conceptual, guion y alertas de confusion.
- El objetivo no es "pasar slides", sino construir criterios semanticos para leer y escribir codigo.

---

## BLOQUE A - Fundamentos de expresiones y semantica (F-00 a F-13)

### [F-00] Portada

Foco: presentar alcance extendido del tema y criterio Sebesta-first.
Guion: aclarar que se prioriza profundidad teorica y lectura critica de decisiones de lenguaje.

### [F-01] Pregunta de apertura

Foco: activar conflicto cognitivo.
Guion: preguntar por que dos expresiones equivalentes sintacticamente pueden divergir en resultado semantico.

### [F-02] Objetivos extendidos

Foco: explicitar metas de la secuencia.
Guion: remarcar que no solo se vera "como" escribir control, sino "cuando" y "por que".

### [F-03] Mapa conceptual

Foco: ubicar ejes.
Guion: recorrer mapa: expresiones -> evaluacion -> control estructurado -> abstracciones iterativas.

### [F-04] Expresion vs sentencia

Foco: distincion base.
Guion: definir expresion como forma que produce valor; sentencia como accion de control/efecto.
Confusion esperada: pensar que toda sentencia devuelve valor.

### [F-05] Arboles sintacticos

Foco: forma sintactica y evaluacion.
Guion: mostrar que precedencia/asociatividad son reglas de parseo, no opiniones de estilo.

### [F-06] Precedencia

Foco: jerarquia de operadores.
Guion: resolver ejemplos progresivos y mostrar como parentesis explicitos mejoran mantenibilidad.

### [F-07] Asociatividad

Foco: empate entre operadores de misma precedencia.
Guion: contrastar asociacion izquierda/derecha y efectos en resultados.

### [F-08] Orden de evaluacion de operandos

Foco: semantica operacional.
Guion: explicar que lenguajes difieren en garantia de orden y que los side effects importan.

### [F-09] Efectos colaterales en expresiones

Foco: fragilidad semantica.
Guion: usar ejemplos con post-incremento y llamadas mutables para mostrar comportamiento inesperado.

### [F-10] Asignacion como sentencia vs expresion

Foco: decisiones de lenguaje.
Guion: comparar lenguajes que permiten assignment expressions en condiciones y riesgos asociados.

### [F-11] Bug historico: if (x = 0)

Foco: error recurrente.
Guion: explicar por que compila en ciertos lenguajes y como prevenirlo con estilo y tooling.

### [F-12] Sobrecarga, conversion y coercion

Foco: poder vs ambiguedad.
Guion: separar conversion explicita de coercion implicita; discutir impacto en legibilidad.

### [F-13] Punto de control conceptual

Foco: consolidar bloque A.
Guion: mini chequeo oral con 3 expresiones y justificacion de evaluacion.

---

## BLOQUE B - Booleanos, short-circuit y seguridad semantica (F-14 a F-23)

### [F-14] Algebra booleana aplicada

Foco: operadores logicos en contexto de programacion.
Guion: conectar tablas de verdad con decisiones de flujo reales.

### [F-15] Truthiness por lenguaje

Foco: semantica de verdad no booleana.
Guion: contrastar comportamiento en TypeScript/JavaScript, Python y C.
Riesgo: asumir que todo lenguaje evalua igual valores vacios.

### [F-16] Evaluacion estricta

Foco: ambos operandos siempre evaluados.
Guion: mostrar cuando esto puede disparar errores evitables.

### [F-17] Short-circuit

Foco: evaluacion condicional del segundo operando.
Guion: enfatizar razon de correccion semantica (evitar estados invalidos).

### [F-18] Patron de seguridad

Foco: evitar division por cero o acceso invalido.
Guion: comparar `a != 0 && b/a > 2` contra version estricta.

### [F-19] Side effects ocultos

Foco: costo cognitivo.
Guion: demostrar que funciones con efectos dentro de booleanos rompen trazabilidad mental.

### [F-20] Operadores logicos en lenguajes

Foco: variaciones de sintaxis y significado.
Guion: revisar operadores de C, Kotlin y TypeScript con foco en semantica compartida.

### [F-21] Null safety y operadores modernos

Foco: `?.`, `??`, guardado defensivo.
Guion: explicar que son atajos de control de flujo, no magia de tipos.

### [F-22] Guard clauses

Foco: simplificacion estructural.
Guion: transformar anidamientos profundos en salidas tempranas justificadas.

### [F-23] Ejercicio de reescritura logica

Foco: practicar equivalencias y legibilidad.
Guion: reescribir condicion compleja a forma legible sin cambiar semantica.

---

## BLOQUE C - Seleccion estructurada y decisiones de diseno (F-24 a F-32)

### [F-24] Programacion estructurada vs goto

Foco: contexto historico y criterio actual.
Guion: explicar por que goto es poderoso pero riesgoso para mantenimiento.

### [F-25] If / else if / else

Foco: arbol de decisiones simple.
Guion: introducir regla de oro: cada rama debe responder una pregunta unica y verificable.

### [F-26] Switch

Foco: seleccion multiple.
Guion: discutir expresion controladora, casos y default, con advertencia de fallthrough.

### [F-27] Pattern matching y alternativas

Foco: expresividad moderna.
Guion: mostrar como algunas plataformas elevan la seguridad de la seleccion multiple.

### [F-28] Anidamiento y complejidad cognitiva

Foco: deuda de legibilidad.
Guion: medir profundidad y costo de comprension.

### [F-29] Criterios de eleccion de estructura

Foco: decision engineering.
Guion: entregar matriz: cardinalidad de casos, estabilidad de reglas, necesidad de extensibilidad.

### [F-30] Dispatch por tabla

Foco: desacople de control.
Guion: mostrar diccionario de funciones como alternativa a cascada de if.

### [F-31] Smells de seleccion

Foco: deteccion temprana.
Guion: listar anti-patrones: condiciones duplicadas, default tragatodo, condiciones opacas.

### [F-32] Actividad de refactor

Foco: transferencia aplicada.
Guion: tomar bloque real y migrarlo de if-anidado a estructura mas mantenible.

---

## BLOQUE D - Iteracion, iteradores y generadores (F-33 a F-42)

### [F-33] Panorama de iteracion

Foco: while, do-while, for.
Guion: comparar semantica de entrada/salida y casos naturales de uso.

### [F-34] Invariantes de bucle

Foco: correccion formal.
Guion: definir invariante, inicializacion, preservacion y terminacion.

### [F-35] Terminacion

Foco: progreso y condiciones de corte.
Guion: mostrar como detectar riesgo de loop infinito en lectura estatica.

### [F-36] Break, continue, return

Foco: control local de flujo.
Guion: explicar ganancia practica y costo de dispersion semantica.

### [F-37] Bucles por contador vs centinela

Foco: patron adecuado al problema.
Guion: contrastar robustez en datos incompletos o streams.

### [F-38] Iteradores

Foco: protocolo de recorrido.
Guion: separar estructura de datos de estrategia de traversal.

### [F-39] Generadores

Foco: produccion perezosa de secuencias.
Guion: explicar `yield` como suspension y reanudacion de contexto.

### [F-40] for...of vs for...in

Foco: error frecuente en TypeScript.
Guion: reafirmar `for...of` para valores iterables y `for...in` para claves.

### [F-41] Recursion vs iteracion

Foco: equivalencia expresiva y trade-offs.
Guion: elegir segun claridad, stack depth y optimizacion disponible.

### [F-42] Control de flujo en asincronia

Foco: `async/await` como secuenciacion explicita.
Guion: conectar con concurrencia futura sin mezclar niveles de abstraccion.

---

## BLOQUE E - Integracion y cierre (F-43 a F-44)

### [F-43] Caso integrador

Foco: lectura critica integral.
Guion: analizar fragmento real y justificar cada decision de expresion/control.
Criterio: no aceptar respuestas de estilo sin fundamento semantico.

### [F-44] Cierre y bibliografia

Foco: consolidacion.
Guion: resumir 10 ideas fuerza y anclar en bibliografia.

---

## Criterios de evaluacion sugeridos

1. Razonamiento semantico: explica por que una expresion se evalua como se evalua.
2. Criterio de estructura: justifica if/switch/dispatch con argumentos de mantenibilidad.
3. Solidez de iteracion: demuestra invariantes y terminacion.
4. Higiene de codigo: evita coerciones ambiguas y side effects ocultos.

---

## Bibliografia de referencia para esta minuta

- Sebesta, Concepts of Programming Languages, capitulo de expresiones y sentencias de control (fuente principal).
- Gabbrielli, Martini, Programming Languages: Principles and Paradigms (complemento semantico y ejercicios de short-circuit).
- Louden, Programming Languages: Principles and Practice (variantes de estructuras de control y contexto historico).
