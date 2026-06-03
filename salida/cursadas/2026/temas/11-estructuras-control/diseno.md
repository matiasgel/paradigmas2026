# Diseno de Clase - Tema 11

## Expresiones y Estructuras de Control

> Estado: APROBADO (autoaprobacion docente solicitada)
> Creado: 2026-06-01
> Agente: Marcos v3 (Topic Designer)
> Modalidad: profundidad teorica extendida (sin restriccion por tiempo de clase)
> Referencia principal: Sebesta, Concepts of Programming Languages, cap. 7
> Referencias auxiliares: Gabbrielli-Martini (cap. expresiones/control), Louden (control statements)

---

## Resolucion de alcance

Se redefine este tema en modalidad extendida para generar una narrativa teorica completa en 45 filminas, priorizando densidad conceptual y trazabilidad bibliografica sobre la duracion habitual de clase.

### Criterios de diseno aplicados

1. Sebesta-first: el hilo argumental principal sigue definiciones y taxonomia del capitulo de expresiones y control.
2. Auxiliares por contraste: Gabbrielli-Martini y Louden se usan para tensionar decisiones de diseno, edge cases y variaciones de sintaxis/semantica.
3. Teoria antes de receta: cada patron practico queda anclado en una decision semantica.
4. Cobertura integral de modulo VIII, incluyendo conexiones explicitas con tipos (modulo VII) y concurrencia (modulo XI) cuando impacta el flujo de control.
5. Restriccion de publicacion: no se generan imagenes para ninguna filmina; todas las slides son de texto o codigo y no se usa Gemini.

---

## Objetivos de aprendizaje (version extendida)

Al finalizar la secuencia completa del tema, el estudiante podra:

1. Definir formalmente expresion, sentencia y contexto de evaluacion.
2. Aplicar precedencia, asociatividad y orden de evaluacion de operandos con y sin efectos colaterales.
3. Diferenciar semantica de short-circuit versus evaluacion estricta y justificar su uso por correccion, no solo por eficiencia.
4. Analizar asignacion como sentencia y como expresion, incluyendo patrones de bug historicos.
5. Evaluar impacto de coerciones y conversiones en legibilidad, seguridad y verificabilidad.
6. Comparar seleccion simple, multiple y anidada segun criterios de mantenibilidad y acoplamiento.
7. Razonar sobre iteracion con invariantes, terminacion y mecanismos de escape.
8. Explicar iteradores y generadores como abstracciones de control de flujo.
9. Diseccionar anti-patrones de control (goto indiscriminado, cascadas no normalizadas, efectos ocultos).
10. Integrar teoria y practica en lectura critica de codigo real.

---

## Cobertura del plan minimo (Modulo VIII)

| Topico institucional | Cobertura en tema 11 |
| -------------------- | -------------------- |
| Expresiones aritmeticas, relacionales y booleanas | Completa y profundizada |
| Reglas de precedencia, asociatividad, parentesis | Completa y formalizada |
| Sentencias de asignacion; asignacion como expresion; modo mixto | Completa con casos de bug |
| Evaluacion corto-circuito vs evaluacion estricta | Completa con semantica operacional |
| Sobrecarga de operadores; conversiones y coerciones | Completa con trade-offs |
| Estructuras de control: seleccion y seleccion multiple | Completa con criterios de diseno |
| Enunciados iterativos y control de bucle | Completa con invariantes y terminacion |
| Iteradores y generadores | Completa con modelo de ejecucion |
| Ejemplos en lenguaje principal y contrastes | Completa |

---

## Arquitectura de filminas (45)

### Bloque A - Fundamentos de expresiones y semantica (F-00 a F-13)

- Definiciones formales, arboles sintacticos, precedencia, asociatividad.
- Orden de evaluacion de operandos y efectos colaterales.
- Asignacion como expresion y riesgos.

### Bloque B - Booleanos, short-circuit y seguridad semantica (F-14 a F-23)

- Modelo de verdad y truthiness segun lenguaje.
- Short-circuit por correccion semantica (evitar estados invalidos).
- Guard clauses y estilo defensivo.

### Bloque C - Seleccion estructurada y decisiones de diseno (F-24 a F-32)

- If/else, switch, pattern matching, dispatch por tabla.
- Complejidad cognitiva y normalizacion de ramas.

### Bloque D - Iteracion, iteradores y generadores (F-33 a F-42)

- While/for/do, invariantes y terminacion.
- Break/continue/return y sus implicancias de lectura.
- Iteradores y generadores como control del flujo de ejecucion.

### Bloque E - Integracion, cierre y bibliografia (F-43 a F-44)

- Caso integrador de lectura de codigo.
- Sintesis conceptual y referencias.

---

## Evidencia de grounding bibliografico (MCP ChromaDB)

Hallazgos aplicados al diseno:

1. Sebesta: precedencia/asociatividad y orden de evaluacion de operandos como fuente de diferencias semanticas en presencia de side effects.
2. Sebesta + Gabbrielli-Martini: short-circuit como mecanismo de correccion (evitar division por cero, null access), no solo optimizacion.
3. Sebesta: asignacion como expresion y error historico de usar `=` en condiciones.
4. Sebesta + Louden: taxonomia de control statements (seleccion, iteracion, transferencia incondicional) y debate estructurado sobre goto.
5. Louden + Gabbrielli-Martini: variantes en for-each e iteracion sobre colecciones, utiles para enlazar con iteradores y generadores.

---

## Decision de aprobacion

Diseno autoaprobado por solicitud explicita del docente para continuar sin checkpoints manuales.

Estado resultante del tema:

- Diseno: aprobado
- Minuta: generar completa
- Filminas: generar 45 teoricas completas
