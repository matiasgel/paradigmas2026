---
topic_id: "03-intro-funcional-ts"
topic_name: "Introducción a Programación Funcional con TypeScript"
exam_type: "parcial-1"
course_id: "2026"
question_count: 5
points_total: 17
bloom_mix: "recordar: 3pts, comprender: 6pts, aplicar: 4pts, analizar: 4pts"
generated_at: "2026-05-25"
---

# Preguntas — Tema 03: Introducción a Programación Funcional con TypeScript

---

## P-03-001 | Recordar | Conceptual | 3 pts

**¿Cuáles son los tres pilares del paradigma de programación funcional?**

a) Herencia, polimorfismo y encapsulamiento  
b) Secuencia, selección e iteración  
c) Funciones puras, inmutabilidad y transparencia referencial  
d) Abstracción, modularidad y encapsulamiento  

**Respuesta correcta:** c  
**Justificación:** Los tres pilares del paradigma funcional son: (1) **funciones puras** — siempre producen el mismo resultado para los mismos argumentos sin efectos colaterales; (2) **inmutabilidad** — los valores no se modifican después de ser creados; (3) **transparencia referencial** — una expresión puede ser reemplazada por su valor sin cambiar el comportamiento del programa.  
**Fuente:** minuta.md §BLOQUE B — Tres pilares del funcional (OA-2)  
**Bloom:** Recordar  

---

## P-03-002 | Comprender | Conceptual | 3 pts

**El λ-cálculo de Alonzo Church y la Máquina de Turing de Alan Turing (ambos de 1936) demostraron ser equivalentes en poder computacional. Sin embargo, representan modelos conceptualmente distintos de qué es "computar". ¿Cuál es la diferencia fundamental entre ambos modelos?**

a) La Máquina de Turing opera sobre números enteros; el λ-cálculo opera sobre funciones de orden superior  
b) La Máquina de Turing define la computación como modificación secuencial de estado (cinta); el λ-cálculo define la computación como sustitución/reescritura de expresiones  
c) La Máquina de Turing es determinista; el λ-cálculo es no determinista  
d) El λ-cálculo requiere hardware especializado; la Máquina de Turing se puede ejecutar en cualquier computadora  

**Respuesta correcta:** b  
**Justificación:** La Máquina de Turing modela el cómputo como una secuencia de operaciones que modifican el estado de una cinta (registro, memoria). Es la base conceptual del paradigma imperativo. El λ-cálculo modela el cómputo como β-reducción: sustituir una expresión por su equivalente sin ningún estado mutable. Es la base conceptual del paradigma funcional. Ambos tienen el mismo poder expresivo (tesis Church-Turing) pero desde visiones radicalmente distintas.  
**Fuente:** minuta.md §BLOQUE A0 — Church vs Turing (F-03, F-04)  
**Bloom:** Comprender  

---

## P-03-003 | Comprender | Conceptual | 3 pts

**¿Qué significa que una función tiene "transparencia referencial"?**

a) Que la función puede recibir otras funciones como argumentos  
b) Que el nombre de la función refleja claramente lo que hace  
c) Que la función puede ser reemplazada por su valor de retorno en cualquier parte del código sin cambiar el comportamiento del programa  
d) Que la función no usa variables globales pero sí puede modificar sus argumentos  

**Respuesta correcta:** c  
**Justificación:** Transparencia referencial significa que una expresión (llamada a función incluida) puede ser sustituida por su resultado en cualquier contexto sin alterar el comportamiento del programa. Esto solo es posible si la función es pura — sin efectos colaterales. Ejemplo: si `doble(3)` siempre devuelve `6`, entonces `doble(3) + 1` y `6 + 1` son intercambiables en cualquier lugar del código.  
**Fuente:** minuta.md §BLOQUE B — Transparencia referencial (OA-2)  
**Bloom:** Comprender  

---

## P-03-004 | Aplicar | Con código | 4 pts

**Considerá el siguiente código TypeScript en estilo funcional:**

```typescript
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const resultado = numeros
  .filter(n => n % 2 === 0)
  .map(n => n * n);
```

**¿Qué contiene `resultado` después de ejecutar este código?**

a) `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` — los cuadrados de todos los números  
b) `[2, 4, 6, 8, 10]` — los números pares del arreglo original  
c) `[4, 16, 36, 64, 100]` — los cuadrados de los números pares  
d) `[1, 3, 5, 7, 9]` — los números impares del arreglo original  

**Respuesta correcta:** c  
**Justificación:** `filter(n => n % 2 === 0)` selecciona los números pares: `[2, 4, 6, 8, 10]`. Luego `map(n => n * n)` aplica la función cuadrado a cada elemento: `[4, 16, 36, 64, 100]`. La composición de `filter` y `map` es una cadena de transformaciones sin mutación del arreglo original.  
**Fuente:** minuta.md §BLOQUE C — map, filter, reduce en TypeScript (OA-4)  
**Bloom:** Aplicar  

---

## P-03-005 | Analizar | Con código | 4 pts

**Considerá las siguientes dos funciones en TypeScript:**

```typescript
// Función A
let contador = 0;
const incrementarA = (x: number): number => {
  contador++;
  return x + 1;
};

// Función B
const incrementarB = (x: number): number => {
  return x + 1;
};
```

**¿Cuál de las siguientes afirmaciones es correcta respecto a la pureza de estas funciones?**

a) Ambas son funciones puras porque las dos devuelven `x + 1`  
b) `incrementarA` es pura porque su resultado `x + 1` no depende de `contador`; `incrementarB` también es pura  
c) `incrementarA` no es una función pura porque modifica la variable externa `contador`, produciendo un efecto colateral; `incrementarB` sí es pura  
d) Ninguna es pura porque TypeScript no soporta funciones puras nativas  

**Respuesta correcta:** c  
**Justificación:** `incrementarA` viola la pureza en dos sentidos: (1) modifica una variable externa (`contador++`) — eso es un **efecto colateral**; (2) aunque su valor de retorno `x + 1` no varía, cada llamada tiene un impacto observable fuera de la función. `incrementarB` es una función pura: mismo input → mismo output, sin efectos en el entorno. La pureza requiere ausencia total de efectos colaterales, no solo consistencia en el valor de retorno.  
**Fuente:** minuta.md §BLOQUE B — Funciones puras (OA-3, OA-5)  
**Bloom:** Analizar  
