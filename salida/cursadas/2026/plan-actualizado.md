# Plan Actualizado — Laboratorio de Programación y Lenguajes (IF009) — UNTDF — 2026

> Actualizado: 2026-05-27
> Base de referencia: `salida/cursadas/2026/plan-borrador.md`
> Ancla institucional inmutable: `salida/cursadas/2026/plan-minimo.md`

---

## Parte I — Replanificación Semanas 8 y 9

> Generado por `/edu-adaptive-replan` el 2026-04-29.
> Estado: propuesta lista para revisión docente

---

### 1. Estado actual evaluado

El plan vigente llega a la semana 8 con el cierre de persistencia y ORM, y recién abre Módulo V en la semana 9 mediante un bloque general de vistas, templates y formularios. Eso deja un salto demasiado abrupto entre:

- el trabajo con modelos, relaciones, migrations y consultas dinámicas;
- la construcción de interfaz con vistas orientadas a objetos, templates y manejo de formularios.

El ajuste pedido es pedagógicamente consistente: convertir las semanas 8 y 9 en una **unidad integrada de transición** entre Módulo IV y Módulo V, de modo que el estudiante vea en una misma secuencia:

- ORM avanzado aplicado sobre el dominio de BlogApp;
- introducción a vistas orientadas a objetos con `View` como clase base;
- introducción a formularios y validación en el ciclo GET/POST.

---

### 2. Replan propuesto

#### Criterio general

Las semanas 8 y 9 se reorganizan como una sola unidad pedagógica: **"ORM avanzado + introducción a vistas y formularios"**.

No se elimina ningún tópico del plan mínimo. Solo se redistribuye el orden de presentación para que el pasaje de persistencia a interfaz MVC sea más natural.

---

### 3. Cronograma actualizado

#### Semana 8 — Clase unificada: ORM avanzado + puente a interfaz MVC

##### Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 45' | ORM avanzado en Django: `QuerySet` como API de consulta, chaining, lazy evaluation, `create()`, `filter()`, `exclude()`, `get()`, `update()`, `delete()` |
| T2 | 45' | Consultas dinámicas y performance: `Q objects`, `annotate()`, `aggregate()`, `order_by()`, `select_related()` y `prefetch_related()` |
| T3 | 30' | Puente MVC: de los modelos a la interfaz. Ciclo request/response. Introducción a class-based views con `View`, `as_view()`, `dispatch()`, `get()` y `post()` |
| T4 | 20' | Introducción a formularios: HTML `<form>`, CSRF, diferencia entre `Form` y `ModelForm`, `is_valid()` y patrón POST/Redirect/GET |

##### Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | BlogApp en Codespaces: consultas avanzadas en shell y managers/querysets sobre `Post`, `Category` y `Comment` |
| P2 | 60' | Primera vista OOP con `View` base: listado y detalle mínimos conectando URL, contexto y template simple |
| P3 | 60' | Formulario inicial de alta/edición: primer `ModelForm`, validación básica y prueba manual del flujo GET/POST |

##### Ajustes asociados

- **Parcial 1** se mueve al inicio de la semana 9 teórica para no cortar la clase puente entre persistencia e interfaz.
- **TP 3** mantiene la entrega en semana 9, pero su alcance se redefine a: modelos + admin + consultas ORM + primeras vistas basadas en `View` + tests de modelos y vistas simples.
- Django Admin sigue dentro de la semana 8 como soporte de inspección del dominio, no como eje principal de cierre del módulo.

---

#### Semana 9 — Consolidación Módulo V: vistas OOP, templates y formularios

##### Teoría (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| T1 | 60' | **Parcial 1** |
| T2 | 40' | Vistas orientadas a objetos en Django: cuándo usar `View` base y cuándo pasar a genéricas. Introducción a `TemplateView`, `ListView` y `DetailView` |
| T3 | 40' | Template Language: `{{ }}`, `{% %}`, herencia con `{% extends %}`, bloques, `include`, filtros y paso de contexto |
| T4 | 20' | Formularios en Django: `ModelForm`, validaciones `clean_*`, errores de formulario y redisplay del formulario inválido |

##### Práctica (3 hs)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| P1 | 60' | Refactor de vistas: pasar de `View` base a primeras genéricas (`ListView` y `DetailView`) |
| P2 | 60' | Templates Bootstrap con herencia: layout base, listado y detalle de posts, mensajes y navegación |
| P3 | 60' | Formularios con `ModelForm` y validación. Introducción a `CreateView`/`UpdateView` como continuidad natural para la App Integradora I |

---

#### Semana 10 — Entrega App Integradora I

Se mantiene la semana 10 como semana de entrega, con el siguiente alcance explícito:

- BlogApp con modelos, admin, consultas ORM relevantes, templates Bootstrap, vistas OOP y formularios operativos.
- Se aceptan implementaciones usando `View` base cuando el grupo todavía no haya migrado todo a genéricas.
- `ListView`, `DetailView`, `CreateView` y `UpdateView` quedan como horizonte recomendado y no como requisito uniforme para todos los grupos en el primer corte.

---

### 4. Verificación de cobertura

#### Módulo IV — Manejo de Persistencia

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

#### Módulo V — Desarrollo de interfaces de usuario utilizando el patrón MVC

| Tópico mínimo obligatorio | Cobertura en el replan |
|---------------------------|------------------------|
| Vistas y templates de Django como parte del patrón MVC | Semana 8 teoría + semana 9 teoría/práctica |
| Vistas genéricas de Django | Semana 9 teoría/práctica |
| Lenguaje de templates de Django | Semana 9 teoría/práctica |
| Modelado de interfaz de usuario con Django y HTML5 | Semana 8 teoría + semana 9 práctica |
| Formularios de Django | Semana 8 teoría/práctica + semana 9 teoría/práctica |
| Vistas y validaciones de formularios | Semana 8 práctica + semana 9 teoría/práctica |

**Cobertura verificada: 100%** de los contenidos mínimos obligatorios afectados por el cambio. No se cae ningún tópico mandatorio de los módulos IV y V.

---

### 5. Impacto operativo

- No requiere tocar `plan-minimo.md`.
- No obliga a modificar semanas 10–17 más allá de aclarar el alcance de la App Integradora I.
- Reduce el salto cognitivo entre ORM y UI.
- Deja explícito que la primera entrada a vistas OOP será con `View` base y no directamente con el paquete completo de genéricas.

---

## Parte II — Split Tema 06 → Temas 06 y 07

> Decisión tomada el 2026-05-27
> Comando: `/edu-adaptive-replan ajustar el tema 06 y repartirlo en dos temas 06 y 07 separados`
> Aclaración del docente: "el tema 6 es autenticación y autorización y el tema 7 es solo django admin"

---

### 1. Situación previa

El Tema 06 original concentraba en 2 clases de 120 min los siguientes contenidos:

| Clase | Duración | Contenido |
|-------|----------|-----------|
| Clase 1 | 120 min | Ciclo HTTP y sesiones · `django.contrib.auth` · `AbstractUser` · `authenticate()`/`login()` · vistas genéricas de auth · templates de autenticación · `RegisterForm`/`RegisterView` |
| Clase 2 — primera mitad | 40 min | auth ≠ authz · permisos por defecto y personalizados · `LoginRequiredMixin` · control de acceso en `get_queryset()` · verificación de permisos en templates |
| Clase 2 — segunda mitad | 75 min | Django Admin completo |

El docente identificó que el volumen de contenido hace inviable mantener autenticación, autorización y admin en un solo tema de 2 clases.

---

### 2. Decisión de replanificación

| Tema | Nombre | Semanas | Duración | Contenido |
|------|--------|---------|----------|-----------|
| **06** | Autenticación y Autorización | 12-13 | 2 × 120 min | Autenticación + Autorización únicamente |
| **07** | Django Admin | 14 | 1 × 120 min | Django Admin completo |

---

### 3. Impacto en el cronograma

| Semana | Antes del split | Después del split |
|--------|----------------|------------------|
| 12 | Tema 06 Clase 1: Autenticación | Tema 06 Clase 1: Autenticación (sin cambio) |
| 13 | Tema 06 Clase 2: Autorización + Admin | Tema 06 Clase 2: Autorización (sin admin) |
| 14 | TP-4 (era solo evaluación) | Tema 07 Clase 1: Django Admin completo |
| 15 | Tema 07: REST API DRF | TP-4 ajustado o semana 15 |

> **Nota:** El TP-4 puede incorporar Admin como parte del enunciado (semana 16) o mantenerse como entrega combinada auth+admin. Decisión pendiente del docente.

---

### 4. Contenido de cada tema

#### Tema 06 — Autenticación y Autorización

**Clase 1 — Autenticación (120 min)**

- Ciclo HTTP y gestión de sesiones
- `django.contrib.auth`: arquitectura y componentes
- Modelo `User` y extensión con `AbstractUser`
- Flujo `authenticate()` / `login()` / `logout()`
- Vistas genéricas de autenticación: `LoginView`, `LogoutView`, `PasswordChangeView`
- Templates de autenticación: personalización y estilos
- Registro de usuarios: `RegisterForm` y `RegisterView`

**Clase 2 — Autorización (120 min)**

- Diferencia entre autenticación y autorización
- Permisos por defecto y permisos personalizados
- `LoginRequiredMixin` y `PermissionRequiredMixin`
- Control de acceso en `get_queryset()` (ownership por autor)
- Verificación de permisos en templates con `{% if perms %}`
- Cierre: estado final de BlogApp con auth+authz completos y anticipo del Tema 07

#### Tema 07 — Django Admin

**Clase 1 — Django Admin completo (120 min)**

- Qué es el Django Admin y para qué sirve
- Registrar modelos: `@admin.register` y `ModelAdmin`
- List view: `list_display`, `list_filter` y `search_fields`
- Detail view: `fieldsets`, `readonly_fields` y `save_model()`
- Acciones en masa: `@admin.action` y `message_user()`
- `InlineModelAdmin`: `TabularInline` y `StackedInline`
- Control de acceso: `has_*_permission()`
- `AdminSite`: branding y `password_change_form` (Django 6.0)
- APIs removidas en Django 6.0 y `DEFAULT_AUTO_FIELD`
- `PostAdmin` completo integrado con BlogApp
- Cierre: BlogApp completa y errores frecuentes en admin

---

### 5. Contexto técnico Django 6.0

#### Tema 06 (auth + authz)

- PBKDF2 con 1.200.000 iteraciones (subió de 1M en Django 6.0)
- Nuevo decorator `login_not_required()` (Django 6.0)
- API async: `aauthenticate`, `alogin`, `alogout`, `request.auser()`
- `LogoutView` solo acepta POST (desde Django 5.x, vigente en 6.0)

#### Tema 07 (admin)

- `AdminSite.password_change_form`: nuevo atributo en Django 6.0
- `ModelAdmin.log_deletion()` y `log_addition()` **REMOVIDAS** (deprecadas desde 5.1)
- `lookup_allowed()` requiere `request` como tercer parámetro (Django 6.0)
- `DEFAULT_AUTO_FIELD` cambia a `BigAutoField` por defecto (Django 6.0)
- Font Awesome Free 6.7.2: `messages.INFO` y `messages.SUCCESS` tienen íconos distintos
- `message_user()` requiere `messages.SUCCESS` explícito para mostrar ícono verde

---

### 6. Estado de artefactos

#### Tema 06 (`salida/cursadas/2026/temas/06-autorizacion-admin-django/`)

| Artefacto | Estado |
|-----------|--------|
| `filminas.md` | Existe — requiere recorte: eliminar sección de Django Admin y agregar cierre de auth+authz |
| `topic.yaml` | Existe — requiere actualización: renombrar slug y ajustar duración |
| `diseno.md` | Existe — actualizado para Django 6.0 |
| `minuta.md` | No existe |
| `tp.md` | No existe |
| `guia-estudio.md` | No existe |
| `.pipeline-v3-state.yaml` | Existe |

#### Tema 07 (`salida/cursadas/2026/temas/07-django-admin/`)

| Artefacto | Estado |
|-----------|--------|
| Carpeta | No existe — crear |
| `filminas.md` | No existe — crear con el contenido de Admin extraído del Tema 06 |
| `topic.yaml` | No existe — crear |
| `diseno.md` | No existe — crear |

---

### 7. Acciones pendientes

1. **Recortar Tema 06 `filminas.md`**: eliminar la sección de Django Admin y reemplazar por un cierre de auth+authz con anticipo del Tema 07.
2. **Actualizar Tema 06 `topic.yaml`**: renombrar slug a `autenticacion-autorizacion-django`, ajustar duración y semanas (12-13).
3. **Crear `salida/cursadas/2026/temas/07-django-admin/`** con `topic.yaml`, `filminas.md` y `diseno.md`.
4. **Verificar cobertura** del `plan-minimo.md` para el Módulo VI completo con los dos temas.

---

### 8. Knowledge base Django 6.0 disponible

Documentos ingestados en ChromaDB (ruta local: `C:\Users\matia\chroma_db`):

- `django60-release-notes.md` — notas de versión completas
- `django60-auth.md` — autenticación y autorización
- `django60-admin.md` — Django Admin

Consultar con: `python scripts/knowledge_base.py search "django admin" --type tool`
