# Diseño de Clase — Tema 10.2
## Tipos Compuestos, Opcionales y Polimorfismo Aplicado

> **Estado:** BORRADOR — pendiente aprobación docente  
> **Actualizado:** 2026-05-22  
> **Agente:** Lic. Marcos 🗂️ (Topic Designer)  
> **Pedido docente aplicado:** diseñar T10.2 absorbiendo faltantes/rebalse de T10.1 y priorizando bibliografía con **Sebesta** como fuente principal.

---

## Metadata del Tema

| Campo | Valor |
|---|---|
| Número de tema | 10.2 |
| Nombre | Tipos Compuestos, Opcionales y Polimorfismo Aplicado |
| Módulo | VII — Tipos de Datos |
| Semana sugerida | 11 (clase extendida / continuación) |
| Clase | 1 |
| **Duración (constraint operativo)** | **360 minutos** |
| Perfil docente | profesor-teorico |
| Lenguaje principal | TypeScript |
| Lenguajes de contraste | Kotlin, Haskell, C |
| Bibliografía principal | **Sebesta (2019), Cap. 6, 11 y 12** |

---

## Diagnóstico de brechas que cubre T10.2 (respecto de T10.1)

Este diseño toma T10.1 como base ya avanzada y agrega cobertura profunda de puntos que quedaron comprimidos o parcialmente tratados:

1. **Tipos secuencia y List Types** (Sebesta §6.9) con foco operacional y de diseño (no solo mención).
2. **Conjunto potencia y modelado de sets** como tipo abstracto y su relación con mapeos finitos.
3. **Mapeos finitos / associative arrays** (Sebesta §6.6) con decisiones de representación y costos.
4. **Optional types** (Sebesta §6.12) formalizados como tipo suma seguro (Option/Maybe) y comparación con `null`.
5. **Polimorfismo aplicado** (Sebesta §11, §12.4) sobre APIs reales con generics, bounds y varianza.
6. **Integración de sistemas de tipos** en un mini-lenguaje de dominio (caso integrador de cierre del módulo VII).

> Resultado esperado: cerrar cobertura curricular de Módulo VII sin solapar innecesariamente con T09.2 ni adelantarse en exceso a T14.

---

## Objetivos de Aprendizaje

Al finalizar T10.2, el estudiante podrá:

| # | Objetivo | Bloom |
|---|---|---|
| OA1 | Modelar tipos secuencia y list types distinguiendo representación, mutabilidad y costo | Comprender / Analizar |
| OA2 | Diseñar y justificar mapeos finitos para distintos casos de uso (key space, colisiones, acceso) | Analizar / Evaluar |
| OA3 | Aplicar el concepto de conjunto potencia para modelar estados/permissions como tipos | Aplicar |
| OA4 | Reemplazar diseños null-prone por optional types (Option/Maybe) con APIs seguras | Aplicar / Evaluar |
| OA5 | Implementar polimorfismo ad-hoc, paramétrico y por subtipo en ejemplos comparativos TS/Kotlin/Haskell | Analizar |
| OA6 | Integrar reglas de compatibilidad de tipos en decisiones de diseño de APIs | Evaluar |
| OA7 | Resolver un caso integrador de sistema de tipos para un DSL pequeño | Crear |

---

## Cobertura explícita del plan mínimo (Módulo VII)

| Ítem institucional | Cobertura en T10.2 | Estado |
|---|---|---|
| Tipos de agregación: mapeos finitos | Bloque B + taller | ✅ Profundizado |
| Tipos secuencia | Bloque A | ✅ Profundizado |
| Conjunto potencia | Bloque C | ✅ Incorporado |
| Tipos recursivos (refuerzo aplicado) | Bloque A.3 | ✅ Consolidado |
| Sistemas monomórficos vs polimórficos | Bloque E | ✅ Consolidado |
| Tipos que aceptan null y operadores | Bloque D | ✅ Formalizado con Option |

---

## Estructura didáctica por bloques

### Bloque A — Tipos secuencia y list types (70 min)
**Fuente principal:** Sebesta §6.9 (+ §6.3 para strings)

- Secuencias homogéneas vs heterogéneas.
- Lists ligadas vs arrays dinámicos: trade-off entre acceso posicional y edición estructural.
- Recursión de listas como tipo inductivo: `Nil | Cons(head, tail)`.
- String como secuencia especializada: implicancias de encoding y operaciones.
- **Micro-lab:** implementar `map`, `filter`, `fold` sobre `List<T>` y discutir inferencia de tipos.

### Bloque B — Mapeos finitos (associative arrays) y diseño (60 min)
**Fuente principal:** Sebesta §6.6

- Definición formal: función parcial finita $K \rightharpoonup V$.
- Diseño de claves: identidad, hashabilidad, estabilidad.
- Representaciones: hash table vs árbol balanceado (complejidad esperada vs peor caso).
- TypeScript `Record<K,V>` vs `Map<K,V>`: restricciones de clave y semántica.
- Kotlin `Map<K,V>` inmutable vs `MutableMap<K,V>`.
- **Micro-lab:** rediseñar una estructura con búsquedas lineales a mapeo tipado.

### Bloque C — Conjunto potencia y modelado de estados (45 min)
**Fuente principal:** Sebesta (modelado matemático de tipos) + Gabbrielli (álgebra de tipos)

- Recordatorio matemático: $\mathcal{P}(S)$ y su utilidad para modelar combinaciones válidas.
- Representación en código: `Set<Permission>` como aproximación práctica de subconjuntos.
- Bitmasks vs `Set<T>`: eficiencia, legibilidad, seguridad de tipos.
- Caso de uso: permisos de usuario, flags de compilación, capacidades de un actor.
- **Actividad guiada:** pasar de enteros mágicos a modelo tipado con conjunto potencia.

### Bloque D — Optional types y eliminación de errores por null (55 min)
**Fuente principal:** Sebesta §6.12

- Optional type como unión discriminada segura: `None | Some(T)`.
- Relación con `null`: por qué `Option<T>` expresa intención y reduce ambigüedad.
- TypeScript: `T | undefined` + narrowing; Kotlin: `T?`, safe calls y Elvis.
- Haskell `Maybe a` como referencia conceptual limpia.
- Refactor de API: de “retorna null” a “retorna Option”.
- **Micro-lab:** migrar 3 funciones legacy null-prone a diseño explícito con optional types.

### Bloque E — Polimorfismo aplicado a diseño de APIs (90 min)
**Fuente principal:** Sebesta §11.1–§11.3, §12.4

- Ad-hoc: sobrecarga y límites prácticos.
- Paramétrico: generics, constraints y reutilización segura.
- Subtipo: principio de sustitución y errores de varianza.
- Varianza en colecciones: `in`, `out`, invariancia; cuándo abrir/cerrar tipos.
- Anti-patrones frecuentes: `any` indiscriminado, casts inseguros, bounds inexistentes.
- **Taller central:** diseñar API de repositorio tipado `Repository<T, Id>` con constraints reales.

### Bloque F — Caso integrador (40 min)

- Construcción de mini-DSL de reglas académicas:
  - tipos de entidad (Alumno, Comisión, Parcial)
  - mapeos finitos para índices
  - optional para resultados parciales
  - conjunto potencia para permisos
  - polimorfismo paramétrico para repositorio genérico
- Entregable del bloque: diagrama de tipos + justificación de decisiones.

---

## Distribución total de tiempo

| Bloque | Min |
|---|---:|
| A | 70 |
| B | 60 |
| C | 45 |
| D | 55 |
| E | 90 |
| F | 40 |
| **Total** | **360** |

---

## Actividades evaluables en clase

| # | Actividad | Duración | Evidencia |
|---|---|---:|---|
| AC1 | Comparativa `Array` vs `List` vs `Map` con matriz de decisión | 20 min | Tabla argumentada |
| AC2 | Refactor null-safe con Option/Maybe | 20 min | Código antes/después |
| AC3 | Diseño de permisos con conjunto potencia | 15 min | Modelo + justificación |
| AC4 | API genérica con bounds | 25 min | Firma + implementación mínima |
| AC5 | Caso integrador DSL | 40 min | Diagrama de tipos + explicación |

---

## Riesgos de scope y reglas de control

- **Fuera de scope en T10.2:** demostraciones formales completas de soundness/progress-preservation (se profundiza en T14).
- **No repetir en detalle:** gradiente estático/dinámico/gradual (`any`, `unknown`, narrowing) ya cubierto en T09.2.
- **Control de alcance:** si aparece teoría de inferencia HM extensa, se corta y se deriva a T14.

> Catchphrase operativa: **“Eso está fuera de scope del Tema 10.2.”**

---

## Bibliografía (trazable)

1. **Sebesta, R. W. (2019). _Concepts of Programming Languages_ (12th ed.). Pearson.**  
   - Cap. 6: Data Types (secuencia, mapeos finitos, listas, unions, pointers/references, optional, type checking)  
   - Cap. 11: Abstracción y polimorfismo  
   - Cap. 12.4: Subtipado y compatibilidad
2. Gabbrielli, M. & Martini, S. (2023). _Programming Languages: Principles and Paradigms_ (2nd ed.). Springer. Cap. 8.
3. Louden, K. C. & Lambert, K. A. (2012). _Programming Languages: Principles and Practices_ (3rd ed.). Cengage.

---

## Próximo paso sugerido del ciclo

Con este diseño en BORRADOR, el próximo comando recomendado es:

`/edu-approve-design`

Si querés iterar ajustes antes de aprobar (más ejemplos, más carga práctica o cambios de foco), usar:

`/edu-design-topic`

---

## Aprobación

| Estado | Fecha | Responsable |
|---|---|---|
| 🔲 BORRADOR | 2026-05-22 | Lic. Marcos (Topic Designer) |
| ⬜ APROBADO | — | Matías Gel |
