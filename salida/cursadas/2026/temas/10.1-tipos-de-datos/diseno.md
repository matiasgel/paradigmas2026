# Diseño de Clase — Tema 10.1
## Tipos de Datos y Sistemas de Tipos (Cobertura Completa T10)

> **Estado:** BORRADOR — pendiente aprobación docente
> **Actualizado:** 2026-05-22
> **Agente:** Lic. Marcos 🗂️ (Topic Designer)
> **Decisión docente aplicada:** integrar TODO el contenido del tópico 10 en 10.1, sin recorte por tiempo de clase tradicional.

---

## Metadata del Tema

| Campo | Valor |
|-------|-------|
| Número de tema | 10.1 |
| Nombre | Tipos de Datos y Sistemas de Tipos (Cobertura Completa T10) |
| Módulo | VII — Sistemas de Tipos |
| Semana | 10 |
| Clase | 1 (extendida) |
| **Duración (constraint operativo)** | **360 minutos** |
| Perfil docente | profesor-teorico |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | Haskell, C, Python |
| Sibling topic | Absorbido en 10.1 |

---

## Objetivos de Aprendizaje

Al finalizar el tema, el alumno podrá:

1. **Definir** el concepto de tipo como conjunto de valores + operaciones válidas.
2. **Clasificar** tipos primitivos y compuestos, y justificar su representación interna.
3. **Analizar** chequeo de tipos estático/dinámico, fuerte/débil y sus trade-offs.
4. **Diferenciar** equivalencia nominal y estructural con ejemplos en TypeScript, C y Haskell.
5. **Aplicar** coerciones/conversiones explícitas e implícitas identificando riesgos.
6. **Explicar y usar** polimorfismo ad-hoc, paramétrico y por subtipo en ejemplos concretos.
7. **Conectar** diseño de tipos con mantenibilidad, seguridad y legibilidad del software.

---

## Mapa de Cobertura Total T10

```
Sistemas de Tipos (T10 completo)
  ├── Fundamentos del tipo
  ├── Tipos primitivos
  ├── Tipos compuestos
  │    ├── arrays / tuplas
  │    ├── records / objetos
  │    ├── unions / discriminated unions
  │    └── referencias/punteros (contraste en C)
  ├── Reglas de chequeo
  │    ├── estático vs dinámico
  │    └── fuerte vs débil
  ├── Conversión y coerción
  ├── Equivalencia de tipos
  │    ├── nominal
  │    └── estructural
  └── Polimorfismo
       ├── ad-hoc (sobrecarga)
       ├── paramétrico (generics)
       └── subtipo (interfaces/herencia)
```

---

## Estructura Didáctica (versión extendida)

### Bloque 1 — Fundamentos y motivación (45 min)
- Definición formal de tipo y rol en diseño/corrección/implementación.
- Evolución histórica: de tipos básicos a sistemas de tipos expresivos.
- Ejercicio diagnóstico: detectar errores de tipo antes de ejecutar.

### Bloque 2 — Tipos primitivos y representación (60 min)
- Numéricos (`number`, `bigint`, precisión IEEE 754).
- Boolean, carácter/string y codificación (Unicode UTF-16).
- Enumeraciones y tipos ordenados/discretos.
- Contraste TS/C/Python sobre rangos y chequeo.

### Bloque 3 — Tipos compuestos (75 min)
- Arrays, tuplas y restricciones de estructura.
- Objetos/records e invariantes de forma.
- Unions y discriminated unions en TypeScript.
- Contraste con `struct` en C y ADTs en Haskell.

### Bloque 4 — Type checking y disciplina de tipos (60 min)
- Estático vs dinámico.
- Fuerte vs débil.
- `any`, `unknown`, narrowing y type guards.
- Riesgos de evasión del sistema de tipos (casts injustificados).

### Bloque 5 — Equivalencia, coerción y conversiones (50 min)
- Equivalencia nominal y estructural.
- Conversión explícita vs coerción implícita.
- Casos de bug por coerción silenciosa (JS/C) y mitigaciones.

### Bloque 6 — Polimorfismo y cierre integrador (70 min)
- Ad-hoc: sobrecarga y resolución.
- Paramétrico: genéricos y restricciones.
- Subtipo: interfaces, contratos y sustitución.
- Síntesis final: cómo decidir el nivel de expresividad del sistema de tipos.

---

## Actividades clave (integradas)

1. **Debug de tipos en vivo:** corregir código con errores de typing sin ejecutar.
2. **Comparativa de lenguajes:** misma estructura en TS/C/Python/Haskell y discutir diferencias.
3. **Refactor seguro:** reemplazar `any` por tipos precisos (`unknown`, unions, generics).
4. **Mini debate:** ¿cuándo conviene flexibilidad dinámica y cuándo disciplina estática?

---

## Tópicos del Plan Mínimo cubiertos (T10 completo)

| Tópico institucional | Cobertura |
|----------------------|-----------|
| Sistemas de tipos | Completa |
| Tipos primitivos y representación | Completa |
| Tipos compuestos | Completa |
| Type checking estático/dinámico | Completa |
| Strong/weak typing | Completa |
| Equivalencia de tipos | Completa |
| Niveles de polimorfismo | Completa (intro + aplicación) |

---

## Conexiones curriculares

| Dirección | Tema | Conexión |
|-----------|------|----------|
| ← Prerequisito | T09.1 Variables, Binding y Ámbito | Las ligaduras necesitan dominio de tipos |
| ← Prerequisito | T01 Intro TypeScript | Base sintáctica para expresar tipos |
| → Arrastre a T14 | Sistemas de Tipos y Polimorfismo | T14 queda como profundización avanzada (inferencia formal, HM, teoría) |

---

## Notas de alcance y decisión docente

- Se elimina la separación operativa 10.1/10.2 para producción de clase.
- Todo el contenido de tipos se diseña y dicta en 10.1.
- T14 no se elimina: se reposiciona como formalización y profundización teórica.

> **Observación de diseño (transparencia):** esta decisión aumenta densidad cognitiva y volumen de práctica. En la minuta se deberá incluir pausas activas y checkpoints de comprensión para evitar sobrecarga.

---

## Bibliografía base

- Sebesta, R.W. (2019). *Concepts of Programming Languages* (12ª ed.). Pearson. Cap. 6.
- Gabbrielli, M. & Martini, S. (2023). *Programming Languages: Principles and Paradigms* (2ª ed.). Springer. Cap. 8.
- Louden, K.C. & Lambert, K.A. (2012). *Programming Languages: Principles and Practices* (3ª ed.). Course Technology. Cap. 8.

---

## Aprobación

| Estado | Fecha | Responsable |
|--------|-------|-------------|
| 🔲 BORRADOR AJUSTADO | 2026-05-22 | Marcos (Topic Designer) |
| ⬜ APROBADO | — | Matías Gel (Docente) |
