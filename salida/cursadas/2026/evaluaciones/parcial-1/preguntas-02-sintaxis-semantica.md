---
topic_id: "02-sintaxis-semantica"
topic_name: "Sintaxis y Semántica de Lenguajes"
exam_type: "parcial-1"
course_id: "2026"
question_count: 2
points_total: 6
bloom_mix: "recordar: 3pts, comprender: 3pts"
generated_at: "2026-05-25"
---

# Preguntas — Tema 02: Sintaxis y Semántica

---

## P-02-001 | Recordar | Conceptual | 3 pts

**¿Cuál de las siguientes afirmaciones describe correctamente la diferencia entre sintaxis y semántica de un lenguaje de programación?**

a) La sintaxis define el significado de los programas; la semántica define su forma correcta  
b) La sintaxis define las reglas de forma que determinan si un programa está bien construido; la semántica define el significado de los programas  
c) La sintaxis y la semántica son equivalentes: un error en una implica un error en la otra  
d) La semántica es responsabilidad del programador; la sintaxis es responsabilidad del compilador  

**Respuesta correcta:** b  
**Justificación:** La sintaxis establece las reglas formales (gramática) que determinan qué secuencias de tokens son programas válidos. La semántica determina qué significan esos programas — qué efecto computacional tienen. Un programa puede ser sintácticamente correcto y semánticamente incorrecto (por ejemplo, sumar un entero con un booleano pasa la gramática pero viola el sistema de tipos).  
**Fuente:** minuta.md §BLOQUE 1 — Definición de sintaxis (F-03) y Definición de semántica (F-04)  
**Bloom:** Recordar  
**Nivel de dificultad:** Básica — 4to año

---

## P-02-002 | Comprender | Conceptual | 3 pts

**Considerá el siguiente programa TypeScript:**

```typescript
function suma(a: number, b: number): number {
  return a + b;
}

const resultado = suma(10, "hola");
```

**¿En qué nivel es incorrecto este programa y por qué?**

a) Es incorrecto sintácticamente: la llamada `suma(10, "hola")` no respeta la gramática de TypeScript  
b) Es incorrecto semánticamente: pasa el análisis de forma, pero viola las reglas de tipo al pasar un `string` donde se espera un `number`  
c) Es correcto tanto sintáctica como semánticamente: TypeScript acepta cualquier valor en una llamada a función  
d) Es incorrecto léxicamente: el string `"hola"` no es un token válido en TypeScript  

**Respuesta correcta:** b  
**Justificación:** El programa está sintácticamente bien formado — todas las construcciones respetan la gramática del lenguaje. El error es semántico (específicamente, de semántica estática / chequeo de tipos): el segundo argumento es `string` pero el parámetro `b` está declarado como `number`. TypeScript detecta este error en tiempo de compilación a través del sistema de tipos.  
**Fuente:** minuta.md §BLOQUE 1 — Punto de tensión (F-04), Errores de tipo en TypeScript (F-06b)  
**Bloom:** Comprender  
**Nivel de dificultad:** Media — 4to año
