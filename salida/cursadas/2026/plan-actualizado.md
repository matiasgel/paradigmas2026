# Plan Actualizado — Replanificación Adaptativa Semanas 8 y 9
## Laboratorio de Programación y Lenguajes (IF009) — UNTDF — 2026

> Generado por `/edu-adaptive-replan` el 2026-04-29.
> Base de referencia: `salida/cursadas/2026/plan-borrador.md`
> Ancla institucional inmutable: `salida/cursadas/2026/plan-minimo.md`
> Estado: propuesta lista para revisión docente

---

## 1. Estado actual evaluado

El plan vigente llega a la semana 8 con el cierre de persistencia y ORM, y recién abre Módulo V en la semana 9 mediante un bloque general de vistas, templates y formularios. Eso deja un salto demasiado abrupto entre:

- el trabajo con modelos, relaciones, migrations y consultas dinámicas;
- la construcción de interfaz con vistas orientadas a objetos, templates y manejo de formularios.

El ajuste pedido es pedagógicamente consistente: convertir las semanas 8 y 9 en una **unidad integrada de transición** entre Módulo IV y Módulo V, de modo que el estudiante vea en una misma secuencia:

- ORM avanzado aplicado sobre el dominio de BlogApp;
- introducción a vistas orientadas a objetos con `View` como clase base;
- introducción a formularios y validación en el ciclo GET/POST.

---

## 2. Replan propuesto

### Criterio general

Las semanas 8 y 9 se reorganizan como una sola unidad pedagógica: **"ORM avanzado + introducción a vistas y formularios"**.

No se elimina ningún tópico del plan mínimo. Solo se redistribuye el orden de presentación para que el pasaje de persistencia a interfaz MVC sea más natural.

---

## 3. Cronograma actualizado

### Semana 8 — Clase unificada: ORM avanzado + puente a interfaz MVC

#### Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | ORM avanzado en Django: `QuerySet` como API de consulta, chaining, lazy evaluation, `create()`, `filter()`, `exclude()`, `get()`, `update()`, `delete()` |
| T2 | 45' | Consultas dinámicas y performance: `Q objects`, `annotate()`, `aggregate()`, `order_by()`, `select_related()` y `prefetch_related()` |
| T3 | 30' | Puente MVC: de los modelos a la interfaz. Ciclo request/response. Introducción a class-based views con `View`, `as_view()`, `dispatch()`, `get()` y `post()` |
| T4 | 20' | Introducción a formularios: HTML `<form>`, CSRF, diferencia entre `Form` y `ModelForm`, `is_valid()` y patrón POST/Redirect/GET |

#### Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | BlogApp en Codespaces: consultas avanzadas en shell y managers/querysets sobre `Post`, `Category` y `Comment` |
| P2 | 60' | Primera vista OOP con `View` base: listado y detalle mínimos conectando URL, contexto y template simple |
| P3 | 60' | Formulario inicial de alta/edición: primer `ModelForm`, validación básica y prueba manual del flujo GET/POST |

#### Ajustes asociados

- **Parcial 1** se mueve al inicio de la semana 9 teórica para no cortar la clase puente entre persistencia e interfaz.
- **TP 3** mantiene la entrega en semana 9, pero su alcance se redefine a: modelos + admin + consultas ORM + primeras vistas basadas en `View` + tests de modelos y vistas simples.
- Django Admin sigue dentro de la semana 8 como soporte de inspección del dominio, no como eje principal de cierre del módulo.

---

### Semana 9 — Consolidación Módulo V: vistas OOP, templates y formularios

#### Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 60' | **Parcial 1** |
| T2 | 40' | Vistas orientadas a objetos en Django: cuándo usar `View` base y cuándo pasar a genéricas. Introducción a `TemplateView`, `ListView` y `DetailView` |
| T3 | 40' | Template Language: `{{ }}`, `{% %}`, herencia con `{% extends %}`, bloques, `include`, filtros y paso de contexto |
| T4 | 20' | Formularios en Django: `ModelForm`, validaciones `clean_*`, errores de formulario y redisplay del formulario inválido |

#### Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | Refactor de vistas: pasar de `View` base a primeras genéricas (`ListView` y `DetailView`) |
| P2 | 60' | Templates Bootstrap con herencia: layout base, listado y detalle de posts, mensajes y navegación |
| P3 | 60' | Formularios con `ModelForm` y validación. Introducción a `CreateView`/`UpdateView` como continuidad natural para la App Integradora I |

---

### Semana 10 — Entrega App Integradora I

Se mantiene la semana 10 como semana de entrega, pero con el siguiente alcance explícito:

- BlogApp con modelos, admin, consultas ORM relevantes, templates Bootstrap, vistas OOP y formularios operativos.
- Se aceptan implementaciones usando `View` base cuando el grupo todavía no haya migrado todo a genéricas.
- `ListView`, `DetailView`, `CreateView` y `UpdateView` quedan como horizonte recomendado y no como requisito uniforme para todos los grupos en el primer corte.

---

## 4. Verificación de cobertura

### Módulo IV — Manejo de Persistencia

| Tópico mínimo obligatorio | Cobertura en el replan |
|---------------------------|------------------------|
| Concepto de persistencia | Semana 7 teoría |
| Soluciones al problema de la persistencia en Python | Semana 7 teoría |
| Mapeo OO–Relacional | Semana 7 teoría/práctica |
| Comparación de tecnologías ORM | Semana 7 teoría |
| Persistencia en Django | Semana 7 práctica |
| Mapeo de entidades y relaciones en Django | Semana 7 práctica |
| Operaciones CRUD con Django | Semana 8 teoría/práctica |
| Consultas dinámicas en Django | Semana 8 teoría/práctica |

### Módulo V — Desarrollo de interfaces de usuario utilizando el patrón MVC

| Tópico mínimo obligatorio | Cobertura en el replan |
|---------------------------|------------------------|
| Vistas y templates de Django como parte del patrón MVC | Semana 8 teoría + semana 9 teoría/práctica |
| Vistas genéricas de Django | Semana 9 teoría/práctica |
| Lenguaje de templates de Django | Semana 9 teoría/práctica |
| Modelado de interfaz de usuario con Django y HTML5 | Semana 8 teoría + semana 9 práctica |
| Formularios de Django | Semana 8 teoría/práctica + semana 9 teoría/práctica |
| Vistas y validaciones de formularios | Semana 8 práctica + semana 9 teoría/práctica |

### Resultado

**Cobertura verificada: 100%** de los contenidos mínimos obligatorios afectados por el cambio.

No se cae ningún tópico mandatorio de los módulos IV y V. El cambio mejora la progresión conceptual entre persistencia, vistas y formularios.

---

## 5. Impacto operativo

- No requiere tocar `plan-minimo.md`.
- No obliga a modificar semanas 10–17 más allá de aclarar el alcance de la App Integradora I.
- Reduce el salto cognitivo entre ORM y UI.
- Deja explícito que la primera entrada a vistas OOP será con `View` base y no directamente con el paquete completo de genéricas.

---

## 6. Próximo paso

Si el docente aprueba esta propuesta, el siguiente cambio operativo es incorporar este delta en `salida/cursadas/2026/plan-borrador.md` como nueva versión del cronograma activo.