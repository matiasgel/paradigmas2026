# Guía del Profesor — Tema 02: Sintaxis y Semántica de Lenguajes

**Materia:** Paradigmas y Lenguajes de Programación 2026  
**Tema:** 02 — Sintaxis y Semántica de Lenguajes  
**Duración objetivo:** 120 minutos  
**Perfil docente:** profesor-teórico

Documento de revisión integral para dictado y ajuste fino de la clase.

---

## 1. Propósito de esta guía

Esta guía concentra, en un solo documento, el plan de clase, los recursos ya producidos, los puntos conceptuales críticos y los fragmentos fuente relevantes para dictado, repaso y evaluación formativa.

Objetivo operativo docente:

1. Entrar al aula con un hilo narrativo claro de punta a punta.
2. Tener a mano ejemplos, contraejemplos y puentes didácticos.
3. Evitar desalineaciones de scope respecto del diseño aprobado.

---

## 2. Estado de artefactos del tema

- Diseño del tema: `diseno.md` (aprobado).
- Clase docente: `minuta.md`.
- Filminas: `filminas.md` (F-00 a F-37).
- Guía de estudio del alumno: `guia-estudio.md`.

Uso recomendado en preparación:

1. Leer esta guía completa primero.
2. Validar timing con `minuta.md`.
3. Ajustar énfasis visual con `filminas.md`.
4. Verificar consistencia de profundización con `guia-estudio.md`.

---

## 3. Plan de clase por bloques (120 min)

### Apertura (5 min)

Objetivo: activar continuidad con Tema 01 y fijar pregunta-problema.

- Disparador: "¿Cómo sabe el compilador si el programa está bien escrito?"
- Encuadre: de TypeScript->JavaScript al interior del compilador.
- Filminas sugeridas: F-00, F-01.

### Bloque 1 (20 min): Sintaxis vs. semántica

Objetivo: consolidar diferencia forma/significado y tipos de error.

- Definiciones operativas de sintaxis y semántica.
- Cuadro de tres errores (sintáctico, semántico estático, dinámico).
- Actividad breve en parejas (clasificación de ejemplos TS).
- Filminas: F-02 a F-06b.

Riesgo didáctico:

- Que el grupo reduzca "semántica" solo a "tipos".

Intervención:

- Enfatizar que tipos son una parte de la semántica estática, no toda la semántica.

### Bloque 2 (20 min): Léxico y tokenización

Objetivo: explicar la transición texto->token y el rol del lexer.

- Lexema vs token con ejemplo clásico `indice = 5 * contador + 1`.
- Separación léxico/sintáctico por simplicidad, eficiencia y portabilidad.
- Filminas: F-07 a F-11.

Decisión pedagógica explícita:

- Se anticipa material de análisis léxico antes de gramáticas para anclaje concreto.

### Bloque 3 (30 min): Gramáticas formales, derivación y árboles

Objetivo: lectura funcional de BNF/EBNF y detección de ambigüedad.

- Tupla de gramática libre de contexto (uso liviano, no formalismo duro).
- Derivación de `A := B * (A + C)`.
- Árbol sintáctico y ambigüedad con `1 + 2 * 3`.
- Filminas: F-12 a F-20.

Punto de control:

- Antes de cerrar bloque, pedir que expliquen por qué dos árboles implican dos significados.

### Bloque 4 (10 min): Diagramas de sintaxis

Objetivo: lectura gráfica y equivalencia con reglas.

- Railroad diagrams para condicional.
- Conexión con documentación de lenguajes reales.
- Filminas: F-21 a F-23.

### Bloque 5 (12 min): Síntesis de semántica

Objetivo: panorámica clara sin salir del scope.

- Semántica estática: gramáticas de atributos, chequeo de tipos.
- Semántica dinámica: operacional, denotacional, axiomática (nivel introductorio).
- Filminas: F-24 a F-28.

Criterio de alcance:

- No derivar formalismos completos en pizarrón. Reservar profundidad para temas posteriores.

### Bloque 6 (15 min): Pipeline e IA

Objetivo: cerrar relevancia contemporánea.

- Pipeline compilador/intérprete.
- Constrained decoding como aplicación actual de gramáticas.
- Filminas: F-29 a F-34.

### Cierre (8 min)

Objetivo: consolidación y transición.

- Mapa conceptual final.
- Preguntas de chequeo rápido.
- Filminas: F-35, F-36, F-37.

---

## 4. Núcleo conceptual que no puede faltar

1. Sintaxis determina forma; semántica determina significado.
2. Lexer y parser no compiten: resuelven capas distintas.
3. BNF/EBNF no son "solo teoría": definen estructuras que compiladores y herramientas consumen.
4. Ambigüedad gramatical es un defecto de diseño porque rompe interpretación única.
5. Semántica estática y dinámica ocurren en momentos distintos del ciclo de vida del programa.

---

## 5. Extractos clave de material fuente para apoyo docente

### 5.1 Definición de lenguaje (fuente cátedra)

- Lenguaje como notación formal para algoritmos.
- Composición: sintaxis + semántica.
- Fuente: `material/02-sintaxis/txt/02 sintaxis.txt`.

Uso en clase:

- Ideal para abrir Bloque 1 y legitimar vocabulario técnico.

### 5.2 Separación léxico/sintáctico (Sebesta)

Ideas textuales relevantes:

- Separar análisis léxico y sintáctico simplifica el diseño.
- Permite optimización focalizada en lexer.
- Mejora portabilidad al aislar partes dependientes de plataforma.

Fuente: `material/02-sintaxis/txt/185-220.txt`, sección lexical analysis.

Uso en clase:

- Sustenta decisión didáctica de Bloque 2.

### 5.3 Ambigüedad, precedencia y asociatividad

Material útil:

- Ejemplo canónico de ambigüedad con `3 + 4 * 5` y árboles alternativos.
- Necesidad de reglas o gramáticas no ambiguas.

Fuente: `material/02-sintaxis/txt/210-330.txt`, secciones de ambiguidad y precedencia.

Uso en clase:

- Núcleo de Bloque 3 y preparación para cursos de compiladores.

### 5.4 Entorno y binding (puente con tema 09)

Aportes clave:

- Nombre no es objeto; nombre denota objeto.
- Binding puede ser estático o dinámico según fase.
- Entorno como conjunto de asociaciones nombre->objeto.

Fuente: `material/02-sintaxis/txt/083-105.txt`, cap. 4.1-4.2.

Uso en clase:

- Mención corta en Bloque 5 para dar continuidad curricular sin profundizar fuera de scope.

---

## 6. Estrategias de mediación en aula

### 6.1 Preguntas de diagnóstico rápido

- "Si algo compila, seguro está semánticamente bien en runtime: verdadero o falso?"
- "Dónde detecta el compilador un error de paréntesis en un if?"
- "Qué parte del pipeline produce tokens?"

### 6.2 Intervenciones cuando aparece confusión frecuente

Confusión: "semántica = ejecución solamente".

Respuesta sugerida:

- "La semántica tiene parte estática y dinámica. Tipos son semántica estática porque dan significado antes de ejecutar."

Confusión: "BNF es memorizar símbolos".

Respuesta sugerida:

- "BNF es una forma de especificar estructura de manera que una herramienta la pueda procesar sin ambigüedad."

Confusión: "ambigüedad es un problema menor".

Respuesta sugerida:

- "Si hay dos árboles válidos, hay dos posibles significados. En compilación eso no es tolerable sin regla extra."

---

## 7. Mapa de trazabilidad recurso->uso docente

- `diseno.md`: alcance, restricciones y prioridades del tema.
- `minuta.md`: guion de conducción minuto a minuto.
- `filminas.md`: soporte visual y ritmo por bloque.
- `guia-estudio.md`: profundización para estudio autónomo y repaso previo a evaluación.
- `material/02-sintaxis/txt/02 sintaxis.txt`: terminología y base cátedra.
- `material/02-sintaxis/txt/185-220.txt`: fundamentos de lexer/parser.
- `material/02-sintaxis/txt/210-330.txt`: gramáticas, ambigüedad, parsing.
- `material/02-sintaxis/txt/083-105.txt`: nociones de nombres/entorno para continuidad.

---

## 8. Sugerencias para evaluación formativa en clase

1. Mini-ejercicio oral: clasificar tres errores TS (sintáctico / estático / dinámico).
2. Ejercicio en pizarrón: derivación parcial de una asignación simple en BNF.
3. Cierre rápido: pedir dos frases, una que explique lexer y otra parser, sin usar sinónimos.
4. Ticket de salida: "Un concepto que me quedó claro y uno que quiero repasar".

---

## 9. Riesgos de implementación y mitigaciones

- Riesgo: sobrecargar formalismo matemático temprano.
- Mitigación: mantener ejemplos concretos en TS y solo luego formalizar.

- Riesgo: perder tiempo en debates de herramientas IA.
- Mitigación: encapsular en Bloque 6 como aplicación, no como eje teórico principal.

- Riesgo: desbordar alcance hacia teoría completa de compiladores.
- Mitigación: repetir criterio "introductorio hoy, profundidad en espacios específicos".

---

## 10. Límites de alcance y continuidad

Fuera de scope en este tema:

- Implementación detallada de algoritmos LL/LR.
- Desarrollo formal completo de semántica operacional/denotacional/axiomática.
- Tratamiento exhaustivo de scope rules y binding (previsto para Tema 09).

Continuidad sugerida:

- Tema 03: reforzar vínculo entre semántica estática y sistema de tipos.
- Tema 09: recuperar y profundizar entorno, binding y alcance.

---

## 11. Checklist docente previo al dictado

- Revisé timing real por bloque (120 min total).
- Validé ejemplos de TypeScript que voy a ejecutar.
- Tengo claro qué parte es conceptual y qué parte es procedimental.
- Preparé dos preguntas de diagnóstico y una de cierre.
- Confirmé no salir del scope del diseño aprobado.

Con este checklist en verde, el tema queda listo para dictado consistente y trazable.
