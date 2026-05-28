---
topic_id: "08-paradigma-oo-ts"
topic_name: "Paradigma OO con TypeScript"
exam_type: "parcial-1"
course_id: "2026"
question_count: 4
points_total: 12
bloom_mix: "recordar: 3pts, comprender: 3pts, aplicar: 3pts, analizar: 3pts"
generated_at: "2026-05-25"
---

# Preguntas — Tema 08: Paradigma OO con TypeScript

---

## P-08-001 | Recordar | Conceptual | 3 pts

**¿Cuáles son los cuatro pilares del paradigma orientado a objetos?**

a) Secuencia, selección, iteración y recursión  
b) Encapsulamiento, abstracción, herencia y polimorfismo  
c) Funciones puras, inmutabilidad, composición y transparencia referencial  
d) Tipos, clases, interfaces y módulos  

**Respuesta correcta:** b  
**Justificación:** Los cuatro pilares del paradigma OO son: (1) **Encapsulamiento** — agrupar estado y comportamiento en un objeto, controlando el acceso externo; (2) **Abstracción** — exponer solo lo necesario, ocultar la implementación; (3) **Herencia** — reutilización de estructura y comportamiento entre clases en relación "es-un"; (4) **Polimorfismo** — tratar distintos tipos de objetos de manera uniforme a través de una interfaz común.  
**Fuente:** minuta.md §BLOQUE 0 — [F-03] Los 4 pilares (OA Recordar)  
**Bloom:** Recordar  

---

## P-08-002 | Comprender | Conceptual | 3 pts

**Smalltalk afirma que "todo es un objeto" — incluyendo los números enteros y los booleanos. TypeScript no cumple este principio de la misma manera. ¿Por qué TypeScript no realiza el OO puro en el sentido de Smalltalk?**

a) Porque TypeScript no tiene clases — solo tiene interfaces y tipos estructurales  
b) Porque TypeScript tiene tipos primitivos (`number`, `boolean`, `string`) que no son objetos sino valores sin métodos propios, a diferencia de Smalltalk donde `1` y `true` son instancias de clases con métodos  
c) Porque TypeScript fue diseñado como lenguaje funcional con sintaxis de clases opcional  
d) Porque en TypeScript no existe el concepto de mensaje — las llamadas a método son solo invocaciones de función  

**Respuesta correcta:** b  
**Justificación:** En Smalltalk el principio "todo es un objeto" es absoluto: el número `1` es una instancia de `SmallInt`, `true` es una instancia de `True`, incluso las clases son objetos. TypeScript (como JavaScript) tiene tipos primitivos (`number`, `boolean`, `string`, `null`, `undefined`) que no son objetos y se acceden de forma distinta. TypeScript tiene `class` y permite OO, pero con compromisos pragmáticos: no es OO puro en el sentido de Alan Kay.  
**Fuente:** minuta.md §BLOQUE 2 — Smalltalk OO puro vs. TypeScript (OA Comprender)  
**Bloom:** Comprender  

---

## P-08-003 | Aplicar | Conceptual | 3 pts

**Considerá la siguiente clase TypeScript:**

```typescript
class CuentaBancaria {
  private saldo: number;

  constructor(saldoInicial: number) {
    this.saldo = saldoInicial;
  }

  depositar(monto: number): void {
    this.saldo += monto;
  }

  getSaldo(): number {
    return this.saldo;
  }
}
```

**¿Cuál de los cuatro pilares del OO aplica PRINCIPALMENTE este diseño, y cómo?**

a) Herencia — la clase hereda de `Object` y extiende su comportamiento  
b) Polimorfismo — `depositar` puede recibir distintos tipos de valores  
c) Encapsulamiento — el campo `saldo` es `private`, accesible solo a través de los métodos públicos `depositar` y `getSaldo`  
d) Abstracción — la clase oculta la implementación del sistema bancario completo  

**Respuesta correcta:** c  
**Justificación:** El diseño aplica principalmente **encapsulamiento**: el campo `saldo` está marcado `private`, lo que significa que no puede ser accedido ni modificado directamente desde afuera de la clase. Solo se puede interactuar con él a través de los métodos públicos `depositar()` y `getSaldo()`. Esto garantiza que el estado interno solo cambie de formas controladas y que las invariantes (ej: saldo nunca negativo) puedan mantenerse. El encapsulamiento es el pilar fundacional de OO según Simula y Smalltalk.  
**Fuente:** minuta.md §BLOQUE 3 — TypeScript OO: clases (OA Aplicar)  
**Bloom:** Aplicar  

---

## P-08-004 | Analizar | Conceptual | 3 pts

**En el paradigma funcional, la inmutabilidad es un principio central: los datos no se modifican. En el paradigma OO, el encapsulamiento gestiona el estado mutable. ¿Cuál de las siguientes afirmaciones describe mejor la diferencia en cómo cada paradigma trata el estado?**

a) No hay diferencia — ambos paradigmas prohíben la mutación del estado  
b) El funcional elimina el estado mutable; el OO lo contiene dentro de los objetos y controla el acceso a él. El funcional gana en predecibilidad; el OO gana en capacidad de modelar entidades con identidad y ciclo de vida  
c) El OO elimina el estado porque encapsular significa que el estado no existe fuera del objeto  
d) El funcional permite mutación pero solo dentro de funciones; el OO permite mutación solo dentro de clases  

**Respuesta correcta:** b  
**Justificación:** El paradigma **funcional** evita el estado mutable: las funciones puras siempre devuelven el mismo resultado para el mismo input y no tienen efectos colaterales. El paradigma **OO** acepta el estado mutable pero lo encapsula: cada objeto es responsable de su propio estado, que solo cambia a través de mensajes/métodos controlados. La elección entre paradigmas implica una compensación: el funcional es más predecible y testeable; el OO modela mejor las entidades del mundo real que tienen identidad propia y cambian a lo largo del tiempo (una cuenta bancaria, un pedido, un usuario).  
**Fuente:** minuta.md §BLOQUE 4 — Comparación OO vs funcional (OA Analizar)  
**Bloom:** Analizar  
