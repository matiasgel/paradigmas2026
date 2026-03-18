# Moodle 5 Quiz y GIFT para BMAD/EDU

## Propósito

Esta nota consolida reglas operativas para generar quizzes compatibles con Moodle 5 dentro del módulo EDU.

Debe usarse como referencia cuando agentes, prompts o workflows produzcan:

- `tp-quiz.gift`
- guías de configuración de actividad Quiz
- instrucciones de importación al banco de preguntas

## Hallazgo principal

En Moodle 5 hay una separación estructural entre:

1. **Question bank**: repositorio de preguntas reutilizables.
2. **Quiz activity**: actividad que define tiempo, intentos, revisión, navegación, restricciones y calificación.

Consecuencia para EDU:

- Un archivo `GIFT` **no define por sí solo** el cuestionario completo.
- El `GIFT` importa preguntas al banco.
- La actividad Quiz se crea y configura aparte dentro de Moodle.

## Fuentes consultadas

Referencias oficiales leídas en MoodleDocs:

- `GIFT format` 5.1
- `Import questions` 5.1
- `Question banks` 5.1
- `Quiz activity` 5.1
- `Quiz settings` 5.1

Se usó MoodleDocs 5.1 como referencia operativa porque la estructura funcional es válida para Moodle 5 actual y fue accesible desde el navegador integrado.

## Reglas GIFT que el generador debe respetar

### Estructura mínima

- El archivo debe estar en `UTF-8`.
- Conviene evitar `UTF-8 BOM` porque puede romper la primera pregunta o el primer `$CATEGORY:`.
- Debe haber al menos una línea en blanco entre preguntas.
- Los comentarios se escriben con `//` y no se importan.
- El título de la pregunta se define con `::titulo::`.
- El cuerpo de respuestas va entre `{ ... }`.

### Múltiple opción simple

- `=` marca la correcta.
- `~` marca las incorrectas.

Ejemplo:

```gift
::TP03-C1-evaluacion-perezosa::[markdown]¿Qué propiedad distingue a una evaluación perezosa? {
=No evalúa hasta que el valor se necesita
~Evalúa todos los argumentos antes de entrar a la función
~Impide definir listas infinitas
~Obliga a memoizar siempre
}
```

### Múltiple opción con varias correctas

- No usar `=`.
- Usar pesos con `%...%` sobre alternativas `~`.
- La suma de pesos correctos no debe superar `100%`.
- Conviene usar pesos negativos en distractores para evitar que marcar todo dé puntaje perfecto.

Ejemplo:

```gift
::TP03-C2-evaluacion-perezosa-aplica::¿Qué afirmaciones son correctas? {
~%50%Permite trabajar con estructuras potencialmente infinitas
~%50%Evita computar ramas que nunca se consumen
~%-50%Fuerza evaluación inmediata de todos los argumentos
~%-50%Elimina la necesidad de razonar sobre costo temporal
}
```

### Feedback

- `#` agrega feedback específico por alternativa.
- `####` agrega feedback general.

Ejemplo:

```gift
::TP03-C3-streams::[markdown]¿Qué ocurre si una cola infinita se consume solo parcialmente? {
=Solo se evalúa la parte necesaria#Correcto: el resto queda diferido.
~Se materializa completa#Eso contradice la idea de evaluación perezosa.
~Provoca error por tamaño infinito#No necesariamente.
#### La idea central es diferir cómputo hasta que haya demanda real del valor.
}
```

### Formato del texto

El texto de la pregunta puede prefijarse con:

- `[html]`
- `[markdown]`
- `[moodle]`
- `[plain]`

Para EDU conviene:

- usar `[markdown]` para texto simple con código inline y listas cortas;
- usar `[html]` si hace falta control fino del render;
- evitar mezclar formatos en el mismo archivo sin motivo.

### Caracteres reservados

Los caracteres `~ = # { } :` tienen significado especial y deben escaparse con `\` si aparecen como texto literal.

Ejemplo:

```gift
::TP03-C4-operadores::¿Qué expresión contiene el símbolo literal \= ? {
=x \= y
~x = y
~x == y
~x := y
}
```

### Categorías

`$CATEGORY:` permite mandar preguntas a una categoría o subcategoría.

Ejemplo:

```gift
$CATEGORY: TP/03-evaluacion-perezosa
```

Puntos importantes:

- Si el import debe respetar el archivo, en Moodle hay que activar `Get category from file`.
- Si la categoría no existe, Moodle puede crearla.
- Hasta el primer `$CATEGORY:`, se usa la categoría elegida en la pantalla de importación.

## Importación en Moodle 5

### Lo que sí hace el GIFT

- importa preguntas al question bank;
- conserva categorías si se habilita esa opción;
- soporta feedback, pesos, títulos y varios tipos de pregunta.

### Lo que no hace el GIFT

No define por sí mismo:

- tiempo límite del quiz;
- intentos permitidos;
- método de calificación entre intentos;
- navegación libre o secuencial;
- review options;
- password o network restrictions;
- grade category del libro de notas;
- Safe Exam Browser.

Todo eso se configura en la **actividad Quiz**.

## Question banks en Moodle 5

Moodle 5 distingue:

1. **Course shared question bank**
   Las preguntas pueden reutilizarse y compartirse entre quizzes y cursos, según permisos.
2. **Quiz question bank**
   Banco privado de un quiz particular.

Consecuencias para EDU:

- Para reutilización entre temas o comisiones, conviene apuntar a categorías de un course shared question bank.
- Si se quiere un quiz autocontenido y no reutilizable, puede cargarse luego en un quiz question bank.
- Solo preguntas con estado `Ready` pueden agregarse a un quiz.

## Configuración de la actividad Quiz en Moodle 5

La creación correcta es de dos pasos:

1. Crear la actividad Quiz y configurar settings.
2. Agregar preguntas desde el banco.

### Ajustes relevantes que EDU debe preguntar o documentar

- `Open the quiz`
- `Close the quiz`
- `Time limit`
- `Attempts allowed`
- `Grading method` si hay múltiples intentos
- `Navigation method`: `Free` o `Sequential`
- `How questions behave`: por ejemplo `Deferred feedback` o `Interactive with multiple tries`
- `Review options`
- `Grade category`
- `Require password`
- `Require network address`

### Reglas importantes de Quiz settings

- Si no se fija tiempo límite, por defecto no hay límite.
- Cuando el tiempo expira, Moodle puede enviar automáticamente el intento.
- `Review options` se configuran por franja temporal:
  - durante el intento
  - inmediatamente después
  - más tarde mientras siga abierto
  - después del cierre
- `During the attempt` depende del comportamiento de preguntas; no aplica igual en todos los modos.
- La navegación secuencial impide volver atrás o saltear preguntas.
- Los overrides por usuario o grupo tienen precedencia sobre los grupales menos específicos.

## Criterio de diseño recomendado para EDU

### Para `quiz-moodle`

Siempre generar dos artefactos:

1. `tp-quiz.gift`
2. `tp-quiz-moodle-config.md`

### Contenido recomendado del `tp-quiz.gift`

- preguntas trazables a `tp.md`;
- nombres estables con prefijo de tema y consigna;
- categorías jerárquicas estables;
- distractores plausibles;
- feedback breve si el uso es formativo;
- escaping correcto de caracteres reservados.

### Contenido recomendado del `tp-quiz-moodle-config.md`

- nombre del quiz;
- categoría del banco;
- cantidad de intentos;
- método de calificación;
- tiempo límite;
- navegación;
- comportamiento de preguntas;
- review options sugeridas;
- procedimiento paso a paso para importar y luego crear el quiz.

## Restricciones para el generador EDU

- No afirmar que `tp-quiz.gift` es “el quiz completo”.
- No mezclar settings de la actividad Quiz dentro del GIFT como si fueran importables.
- No generar pesos arbitrarios incompatibles con `Match grades`.
- No omitir `::title::`.
- No usar texto con caracteres reservados sin escape.
- No asumir que Google Forms y Moodle tienen el mismo modelo de cuestionario.

## Checklist operativo para futuras interacciones

Antes de dar por correcto un quiz Moodle generado por EDU, verificar:

- `tp.md` contiene preguntas evaluables y no solo consignas abiertas.
- `tp-quiz.gift` está en UTF-8.
- Hay una línea en blanco entre preguntas.
- Todas las preguntas tienen título `::...::`.
- Las correctas e incorrectas están marcadas con sintaxis GIFT válida.
- Los caracteres reservados fueron escapados si aparecen en texto literal.
- La categoría está definida de forma estable si hace falta reutilización.
- Existe `tp-quiz-moodle-config.md`.
- La guía separa claramente importación al banco y creación de la actividad Quiz.

## Uso recomendado en prompts/agentes

Cuando el usuario pida “quiz Moodle”, interpretar siempre:

- exportación del banco en GIFT; y
- documentación operativa de configuración del Quiz en Moodle 5.

No asumir que basta con producir un solo archivo.