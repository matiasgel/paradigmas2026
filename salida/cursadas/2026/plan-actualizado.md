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

---

## Parte III — Tutorial guiado de 3 clases: tienda e-commerce con Django Admin

> Propuesta generada por `edu-agent-course-planner` el 2026-06-10.
> Estado: propuesta lista para revisión y aprobación docente.
> Reemplaza el dominio BlogApp de las próximas tres clases por una tienda e-commerce incremental.
> Duración de referencia: 3 clases de 180 minutos.
> Modalidad: tutorial guiado mediante implementación en vivo del profesor.

---

### 1. Decisión pedagógica

Las próximas tres clases se organizan como un tutorial guiado incremental. El profesor
implementa en vivo una tienda e-commerce y explica cada decisión mientras el alumnado
observa la evolución del mismo repositorio. No son clases prácticas ni incluyen trabajo
autónomo de implementación durante la clase.

En lugar de enseñar modelos, vistas, autenticación y admin como bloques aislados, cada
clase muestra la construcción completa de una **feature vertical** que atraviesa:

1. modelo y persistencia;
2. web pública;
3. web autenticada del cliente;
4. Django Admin personalizado con Jazzmin para el operador;
5. permisos y administración de usuarios;
6. prueba funcional y demostración docente del incremento.

El producto final será una tienda e-commerce educativa con pagos y envíos simulados.
Jazzmin se utilizará como capa visual sobre `django.contrib.admin`; la personalización
funcional seguirá implementándose con `ModelAdmin`, permisos, grupos, acciones e inlines.
La web pública y el área del cliente se construirán adaptando el theme Bootstrap 5
[ThemeWagon MiniStore](https://github.com/themewagon/MiniStore) a templates Django.

#### Separación de interfaces

| Interfaz | Base visual | Usuarios |
|----------|-------------|----------|
| Storefront y área cliente | ThemeWagon MiniStore adaptado a Django | Visitantes y clientes |
| Panel operativo | Django Admin personalizado con Jazzmin | Operadores |
| Administración de seguridad | El mismo Django Admin estilizado por Jazzmin | Administradores |

MiniStore se incorpora respetando su licencia MIT y conservando el aviso de copyright y
licencia correspondiente dentro del proyecto.
El tutorial no diseña la tienda desde cero: enseña a transformar un theme HTML/CSS/JS
estático en una aplicación Django conectada a modelos, autenticación y reglas de negocio.

#### Verificación de coherencia de las interfaces

| Requisito | Soporte real | Decisión |
|-----------|--------------|----------|
| Home responsiva, banners, categorías y cards | MiniStore lo ofrece en su `index.html` Bootstrap 5 | Reutilizar estructura y reemplazar contenido estático |
| Búsqueda, accesos, carrito y seguimiento en navbar/footer | MiniStore ofrece elementos visuales y enlaces placeholder | Conectar a URLs y vistas Django |
| Detalle, selector talle/color, carrito y checkout | El CSS de MiniStore contiene estilos para estas pantallas, pero el repositorio publicado no entrega páginas funcionales completas | Construir templates Django propios reutilizando sus clases visuales |
| Login, “Mi cuenta” e historial de órdenes | No forman parte funcional de MiniStore | Construir vistas/templates Django coherentes con el theme |
| Panel interno responsivo | Jazzmin ofrece skin AdminLTE, menús, búsqueda, modales y personalización | Usarlo exclusivamente sobre `django.contrib.admin` |
| Permisos del operador | Jazzmin puede condicionar enlaces por permisos, pero no reemplaza autorización | Aplicar `Group`, `Permission` y controles `ModelAdmin` |

MiniStore usa Bootstrap 5. Jazzmin usa AdminLTE y Bootstrap 4. Esta diferencia no genera
conflicto porque viven en superficies separadas: MiniStore en templates públicos y Jazzmin
en `/admin/`. No deben mezclarse assets entre ambas interfaces.

Operador y administrador ingresan al mismo `/admin/` y reciben el mismo skin Jazzmin.
La diferencia entre ambos no es visual ni depende de Jazzmin: Django construye el menú y
autoriza operaciones según los permisos efectivos de cada usuario. Crear dos paneles
completamente distintos requeriría dos instancias de `AdminSite`, lo cual queda fuera del
alcance de este tutorial.

#### Dinámica didáctica

- El profesor parte de un repositorio base preparado y realiza live coding proyectado.
- Cada bloque comienza mostrando el comportamiento que se desea obtener.
- Antes de escribir código, el profesor explica los archivos y decisiones involucradas.
- El código se implementa en fragmentos pequeños y verificables.
- Los alumnos participan mediante predicciones, preguntas de control y lectura del resultado.
- El profesor ejecuta migraciones, pruebas y recorridos funcionales frente al curso.
- Cada clase termina con una versión completa y ejecutable de la tienda.

---

### 2. Objetivo del tutorial

Al terminar la tercera clase, el profesor habrá implementado y demostrado el flujo completo:

```text
administrador crea usuarios y asigna roles
→ operador publica productos con fotos y stock
→ cliente navega el catálogo y arma su carrito
→ cliente confirma una orden y realiza un pago simulado
→ operador aprueba y prepara la orden
→ cliente consulta el seguimiento del envío simulado
```

#### Roles

| Rol | Superficie principal | Responsabilidades |
|-----|----------------------|-------------------|
| Cliente | MiniStore adaptado: web pública, login y área autenticada | Navegar, gestionar carrito, crear orden, pagar y seguir envío |
| Operador | Django Admin con Jazzmin | Gestionar catálogo, fotos, stock, aprobación y estados de órdenes/envíos |
| Administrador | Django Admin | Gestionar usuarios, grupos, permisos y acceso del operador |

#### Matriz de acceso por tipo de usuario

| Capacidad | Visitante | Cliente | Operador | Administrador |
|-----------|-----------|---------|----------|---------------|
| Ver catálogo público y variantes disponibles | Sí | Sí | Sí | Sí |
| Iniciar sesión en área cliente | No | Sí | Sí, pero no es su interfaz de trabajo | Sí |
| Gestionar carrito propio | No | Sí | No requerido | Sí, para pruebas |
| Crear orden y pago simulado propios | No | Sí | No | Sí, para pruebas |
| Consultar órdenes y envíos propios | No | Sí | No | Sí |
| Acceder a `/admin/` | No | No | Sí, con `is_staff=True` | Sí |
| Gestionar catálogo y variantes | No | No | Sí | Sí |
| Aprobar/rechazar órdenes | No | No | Sí | Sí |
| Preparar/despachar envíos | No | No | Sí | Sí |
| Gestionar usuarios, grupos y permisos | No | No | No | Sí |

Cliente y operador son instancias del mismo `accounts.User`; no son clases de usuario
distintas. El cliente no necesita permisos de modelos ni `is_staff`: su acceso se controla
por autenticación y ownership en las vistas. El operador recibe permisos mediante el grupo
`Operadores`. El administrador es superusuario. Los datos exclusivos del cliente, como
teléfono y dirección de entrega, pertenecen a `accounts.CustomerProfile`; operador y
administrador no poseen ese perfil y no se expone en Django Admin.

#### Matriz de permisos Django

| App / modelo | Cliente | Grupo `Operadores` | Administrador |
|--------------|---------|---------------------|---------------|
| `accounts.User` | Ningún permiso de modelo | Ninguno | Todos |
| `accounts.CustomerProfile` | Vistas propias, sin permisos de modelo | Ninguno; fuera del admin | Fuera del admin |
| `auth.Group`, `auth.Permission` | Ninguno | Ninguno | Todos |
| `products.Category` | Ninguno | `view`, `add`, `change` | Todos |
| `products.Product` | Ninguno | `view`, `add`, `change`, `publish_product` | Todos |
| `products.ProductVariant` | Ninguno | `view`, `add`, `change` | Todos |
| `products.ProductImage` | Ninguno | `view`, `add`, `change` | Todos |
| `orders.Order` | Ninguno; ownership en vistas | `view`, `approve_order`, `reject_order` | Todos |
| `orders.OrderItem` | Ninguno; ownership en vistas | `view` | Todos |
| `operations.Payment` | Ninguno; ownership en vistas | `view` | Todos |
| `operations.Shipment` | Ninguno; ownership en vistas | `view`, `prepare_shipment`, `dispatch_shipment`, `deliver_shipment` | Todos |
| `operations.ShipmentEvent` | Ninguno; ownership en vistas | `view`, `add` | Todos |

Por defecto, el operador no recibe permisos `delete`. Tampoco recibe `change_order`,
`change_payment` ni `change_shipment`: las transiciones sensibles se realizan mediante
acciones controladas por permisos personalizados y servicios de dominio.

#### Reglas obligatorias de autorización

- `is_staff=True` permite al operador entrar al admin, pero no concede permisos de modelos.
- Los permisos `add`, `change`, `delete` y `view` son creados por Django al ejecutar migraciones.
- Los permisos personalizados se declaran en `Meta.permissions` y se asignan al grupo `Operadores`.
- Las vistas del cliente usan `LoginRequiredMixin` y filtran siempre por `customer=request.user`.
- Las vistas de Mi cuenta rechazan usuarios `is_staff`; un operador o administrador no
  se convierte accidentalmente en cliente.
- Ocultar botones o enlaces en MiniStore/Jazzmin mejora la interfaz, pero no constituye seguridad.
- `ModelAdmin.has_view_permission()`, `has_add_permission()`, `has_change_permission()` y
  `has_delete_permission()` refuerzan el acceso del operador.
- Estados, totales, pagos y eventos se muestran como `readonly_fields` en el admin cuando
  solo pueden cambiar mediante acciones controladas.
- Las acciones aprobar, rechazar, preparar, despachar y entregar validan permiso, estado
  previo y transición permitida.
- Después de asignar permisos durante una prueba, se vuelve a obtener el usuario desde la
  base antes de verificarlos, debido al cache de permisos de Django.

#### Uso coherente de Jazzmin

Jazzmin es una capa visual sobre Django Admin, no un sistema de roles. Se utilizará para:

- branding mediante `site_title`, `site_header`, `site_brand`, logos y copyright;
- ordenar catálogo, órdenes, pagos y envíos con `order_with_respect_to`;
- asignar íconos a apps y modelos;
- mostrar enlaces personalizados condicionados por `permissions`;
- organizar formularios extensos mediante tabs o secciones colapsables;
- usar modales relacionados para facilitar la carga de datos;
- aplicar CSS/JS propio solo cuando sea necesario.

No se usará `hide_models` para ocultar `accounts.User`, `auth.Group` o permisos al operador,
porque esa configuración es global y también los ocultaría al administrador. Esos modelos
desaparecerán naturalmente para el operador al no poseer permisos sobre ellos. Los enlaces
personalizados de Jazzmin también deben declarar sus permisos correspondientes.

La búsqueda global de Jazzmin se configura únicamente sobre modelos comerciales visibles
para el operador. No se incluye `accounts.User` en `search_model`, evitando presentar una
función de búsqueda que el operador no debe utilizar.

#### Implementación de operaciones sensibles

| Operación | Implementación coherente |
|-----------|--------------------------|
| Publicar producto | Acción o botón protegido por `products.publish_product` |
| Aprobar/rechazar orden | Acción protegida por `orders.approve_order` / `orders.reject_order`; estado readonly |
| Preparar/despachar/entregar | Acciones protegidas por permisos personalizados de `operations`; estado readonly |
| Desactivar producto o variante | Campo `active` mediante `change`; no borrado físico |
| Consultar cliente desde una orden | Texto readonly sin enlace editable hacia `accounts.User` |
| Registrar evento de envío | Servicio de transición crea `ShipmentEvent`; eventos existentes no se editan ni borran |

Las acciones administrativas con permisos personalizados deben declarar esos permisos y
proveer la verificación correspondiente en el `ModelAdmin`; no deben depender solamente de
la visibilidad del botón.

#### Pruebas mínimas de autorización

| Caso | Resultado esperado |
|------|--------------------|
| Cliente intenta acceder a `/admin/` | Acceso denegado |
| Operador accede al admin | Acceso permitido |
| Operador intenta abrir usuarios o grupos por URL directa | `403` o acceso denegado |
| Operador intenta borrar producto, orden, pago o envío | Acción no disponible y acceso denegado |
| Operador intenta aprobar una orden sin permiso personalizado | Acceso denegado |
| Operador aprueba una orden válida | Estado y stock cambian en una transacción |
| Cliente consulta orden de otro cliente | `404` o acceso denegado |
| Visitante intenta pagar o seguir una orden | Redirección al login |
| Administrador gestiona usuarios, grupos y permisos | Acceso completo |

La primera clase muestra explícitamente las tres superficies de acceso:

```text
/accounts/login/  → login del cliente y acceso a "Mi cuenta"
/admin/login/     → login del operador con permisos comerciales limitados
/admin/login/     → login del administrador con gestión de usuarios y permisos
```

---

### 3. Arquitectura funcional acumulativa

El proyecto se divide en aplicaciones Django por responsabilidad de negocio. Se crean
como mínimo las tres apps solicitadas (`products`, `orders`, `operations`) y una cuarta
app transversal (`accounts`) para demostrar correctamente el usuario personalizado.

| App Django | Tipo | Modelos principales | Responsabilidad |
|------------|------|---------------------|-----------------|
| `accounts` | Transversal | `User` extendido desde `AbstractUser` | Identidad, perfil, autenticación y soporte de roles |
| `products` | Negocio obligatoria 1 | `Category`, `Product`, `ProductVariant`, `ProductImage` | Prendas, variaciones, fotos, precios, publicación y stock |
| `orders` | Negocio obligatoria 2 | `Order`, `OrderItem` | Carrito confirmado, ownership, historial, aprobación y totales |
| `operations` | Negocio obligatoria 3 | `Payment`, `Shipment`, `ShipmentEvent` | Pagos y envíos simulados posteriores a la orden |

#### Límites y dependencias entre aplicaciones

```text
accounts
   ↑ referenciada mediante settings.AUTH_USER_MODEL
   │
products  ← orders  ← operations
 catálogo   compra    pago y envío simulados
```

- `products` no conoce órdenes, pagos ni envíos.
- `orders` referencia `products.ProductVariant` y `settings.AUTH_USER_MODEL`.
- `operations` referencia `orders.Order`; no modifica directamente productos.
- `accounts` no importa modelos de las apps de negocio.
- Las transiciones que afectan varias apps se coordinan mediante servicios explícitos,
  evitando colocar toda la lógica en vistas, templates o señales ocultas.
- Cada app mantiene sus propios `models.py`, `admin.py`, `views.py`, `urls.py`, templates
  con namespace, migraciones y tests.

#### Creación mostrada en el tutorial

```bash
python manage.py startapp accounts
python manage.py startapp products
python manage.py startapp orders
python manage.py startapp operations
```

Después de crear cada app, el profesor muestra su registro en `INSTALLED_APPS`, su
namespace de URLs y la razón por la cual esa responsabilidad no pertenece a otra app.

#### Namespaces y superficies por app

| App | Namespace / superficie | Ejemplos |
|-----|------------------------|----------|
| `accounts` | `accounts:` + admin de usuarios | `accounts:login`, `accounts:profile` |
| `products` | `products:` + admin de catálogo | `products:list`, `products:detail` |
| `orders` | `orders:` + admin de órdenes | `orders:cart`, `orders:checkout`, `orders:detail` |
| `operations` | `operations:` + admin operativo | `operations:pay`, `operations:tracking` |

Los templates se guardan con namespace (`templates/products/`, `templates/orders/`,
etc.) y los tests se organizan dentro de la app propietaria de la regla. Los servicios
que coordinan varias apps reciben identificadores u objetos explícitos y no importan
vistas o clases admin de otras aplicaciones.

#### Estados mínimos

```text
Order: DRAFT → PENDING_APPROVAL → APPROVED → PREPARING → SHIPPED → DELIVERED
                     ↘ REJECTED

Payment: PENDING → APPROVED | REJECTED

Shipment: PENDING → PREPARING → IN_TRANSIT → DELIVERED
```

---

### 4. Hoja de ruta de features

| ID | Historia de usuario | Clase |
|----|--------------------|-------|
| US-01 | Como operador quiero publicar prendas con fotos y variantes de talle/color para ofrecerlas en la tienda | 1 |
| US-02 | Como visitante quiero navegar y consultar el detalle de productos publicados | 1 |
| US-03 | Como administrador quiero asignar el rol operador sin otorgar privilegios de superusuario | 1 |
| US-03A | Como cliente quiero iniciar sesión y acceder a mi cuenta | 1 |
| US-03B | Como operador quiero cargar variantes de prendas con talle, color, SKU, precio y stock | 1 |
| US-04 | Como cliente quiero agregar productos al carrito y confirmar una orden | 2 |
| US-05 | Como cliente quiero consultar solo mis órdenes | 2 |
| US-06 | Como operador quiero aprobar o rechazar órdenes y actualizar stock | 2 |
| US-07 | Como cliente quiero realizar un pago simulado y ver su resultado | 3 |
| US-08 | Como operador quiero preparar y despachar órdenes desde el admin | 3 |
| US-09 | Como cliente quiero seguir el estado de mi envío | 3 |
| US-10 | Como administrador quiero auditar usuarios, grupos y permisos configurados en la Clase 1 | 3 |

---

### 5. Clase 1 — Incremento 1: accesos, usuarios y tienda de ropa con variantes

**Objetivo del tutorial:** el profesor construye los accesos de cliente, operador y
administrador; extiende el usuario de Django; personaliza el admin para el operador; carga
prendas con variaciones; y publica una web estándar de venta de ropa.

#### Feature terminada

```text
Administrador inicia sesión y crea un usuario operador
→ asigna el grupo Operadores con permisos limitados
→ operador inicia sesión en el admin personalizado
→ carga prendas, fotos y variantes por talle/color con stock
→ visitante navega MiniStore adaptado como tienda de ropa y selecciona una variante
→ cliente inicia sesión y accede a "Mi cuenta"
```

#### Modelo de usuarios mostrado

El profesor crea `accounts.User` extendiendo `AbstractUser` **antes de la primera
migración** y configura `AUTH_USER_MODEL`. `User` conserva identidad, autenticación,
grupos y permisos. Teléfono y dirección de entrega se modelan en
`accounts.CustomerProfile`, creado solamente para clientes.

También registra `UserAdmin` para que el administrador gestione usuarios, estado staff,
grupos y permisos. `CustomerProfile` permanece fuera del admin; el operador no visualiza
la sección de usuarios ni puede otorgar permisos.

| Tipo de usuario | Configuración |
|-----------------|---------------|
| Cliente | Usuario activo, sin `is_staff`, con `CustomerProfile`; accede a login y área cliente |
| Operador | Usuario activo con `is_staff=True`, sin `CustomerProfile` y grupo `Operadores`; accede al admin comercial |
| Administrador | Superusuario sin `CustomerProfile`; administra usuarios, grupos y permisos |

#### Modelo de catálogo de ropa

| Modelo | Responsabilidad | Campos principales |
|--------|-----------------|--------------------|
| `Category` | Agrupar prendas | nombre, slug |
| `Product` | Describir la prenda común a todas las variantes | nombre, descripción, categoría, marca, activo |
| `ProductVariant` | Representar la unidad realmente vendible | producto, talle, color, SKU, precio, stock, activa |
| `ProductImage` | Mostrar imágenes comerciales | producto, imagen, texto alternativo, principal |

`Product` no almacena un único talle, color o stock. La combinación vendible es
`ProductVariant`; por ejemplo: “Remera clásica / M / Negro / SKU REM-M-NEG / stock 8”.
La combinación producto + talle + color y el SKU deben ser únicos.

#### Adaptación de MiniStore como tienda de ropa

El profesor parte del repositorio
[themewagon/MiniStore](https://github.com/themewagon/MiniStore), originalmente compuesto
por `index.html`, `css/`, `js/` e `images/`. Durante el tutorial transforma esa estructura
estática en templates y assets de Django:

| Theme estático | Adaptación Django |
|----------------|-------------------|
| `index.html` completo | `base.html`, `store/home.html` e includes reutilizables |
| `css/`, `js/`, íconos e imágenes | `static/store/` y referencias mediante `{% static %}` |
| Navbar con enlaces fijos | URLs Django, categorías, login/logout y “Mi cuenta” |
| Cards de productos escritas manualmente | Loop `{% for product in products %}` con datos del ORM |
| Imágenes de demostración | `ProductImage.image.url` con fallback estático |
| Precio y stock de ejemplo | Precio inicial y disponibilidad calculados desde variantes |
| Secciones de electrónica del theme | Portada, destacados y categorías de indumentaria |

La versión adaptada conserva el lenguaje visual de MiniStore e incluye:

- navbar con marca, categorías, acceso del cliente y estado de sesión;
- portada del theme personalizada para una marca de ropa;
- grilla responsiva de prendas con imagen, nombre y precio inicial;
- secciones de productos destacados y novedades alimentadas desde Django;
- detalle con galería, descripción y selector de talle/color;
- indicación de disponibilidad según la variante seleccionada.

MiniStore aporta el lenguaje visual y componentes de referencia, pero no aporta lógica
e-commerce. Los enlaces “Shop”, “Cart”, “Checkout” y “Single Product” del `index.html`
publicado son placeholders; las vistas, URLs, formularios y reglas correspondientes se
implementan en Django.

#### Secuencia didáctica de conversión del theme

```text
MiniStore estático funcionando
→ copiar assets a static/store/
→ crear base.html y reemplazar rutas por {% static %}
→ extraer navbar y footer como includes
→ reemplazar cards fijas por un loop de productos
→ conectar imágenes y variantes del ORM
→ integrar login, logout y Mi cuenta en la navbar
```

#### Secuencia por checkpoints

Para que la clase sea viable, el profesor parte de un repositorio inicial que ya contiene:

- proyecto Django creado, entorno instalado y servidor verificable;
- MiniStore descargado con su licencia y assets disponibles;
- Jazzmin instalado y agregado a `INSTALLED_APPS`;
- dependencias para imágenes instaladas;
- commits base que permiten recuperar rápidamente cada etapa.

Las apps de negocio todavía no están creadas: su creación, registro e integración forman
parte del live coding. La creación mecánica del proyecto y la descarga de dependencias se
muestran en filminas, pero no consumen tiempo de live coding.

| Checkpoint | Etapa | Entregable |
|------------|-------|------------|
| `C00`–`C03` | Entorno, `accounts`, usuarios y permisos | Cliente, operador y administrador diferenciados |
| `C04`–`C05` | `products`, variantes y admin | Catálogo cargable con imágenes y stock |
| `C06`–`C07` | MiniStore dinámico, tests y recorrido | Tienda v0.1 completa |
| `C08` — opcional | Carrito público temporal | Visitante agrega variantes mediante sesión |
| `C09` — opcional | Carrito persistente | El login migra el carrito al cliente |

No se calculan tiempos por etapa. Si una sesión termina, se conserva el último checkpoint
consistente y se continúa en la clase siguiente.

#### Criterio de cierre de la demostración

- Las apps `accounts` y `products` fueron creadas, registradas y migradas por separado.
- El cliente puede iniciar y cerrar sesión y acceder a “Mi cuenta”.
- El administrador puede crear usuarios y asignar el grupo `Operadores`.
- El operador puede iniciar sesión en un admin personalizado para su trabajo.
- El operador no puede administrar usuarios.
- El operador puede crear prendas con fotos y múltiples variantes desde el admin.
- Cada variante posee talle, color, SKU, precio y stock propios.
- La tienda pública adapta MiniStore como home y catálogo dinámico de ropa.
- Los assets se sirven desde `static/store/` y las secciones reutilizables usan herencia e includes.
- Las cards del theme muestran productos, imágenes y precios provenientes del ORM.
- El detalle permite seleccionar únicamente variantes activas y con stock.
- El profesor demuestra al menos un test de login, uno de permisos y uno de variantes.
- El mismo admin Jazzmin muestra opciones distintas al operador y al administrador según permisos.
- Como extensión opcional, el carrito público vive en sesión y el cliente autenticado
  conserva un carrito persistente.

---

### 6. Clase 2 — Incremento 2: carrito, orden y aprobación

**Objetivo del tutorial:** el profesor retoma el carrito disponible, o lo completa si no
se alcanzó el bloque opcional anterior, y muestra cómo un cliente autenticado lo convierte
en una orden que un operador procesa desde el admin.

#### Feature terminada

```text
Cliente selecciona talle/color y agrega variantes al carrito
→ confirma checkout
→ se crean Order + OrderItem con variante, descripción y precio congelados
→ operador aprueba o rechaza desde Django Admin
→ aprobación descuenta stock
→ cliente ve la orden y su estado
```

#### Secuencia por checkpoints

| Checkpoint | Etapa | Entregable |
|------------|-------|------------|
| Inicio | Recuperar o completar carrito | Carrito persistente del cliente en verde |
| Órdenes | Implementar `Order`, `OrderItem` y checkout | Carrito convertido en orden |
| Área cliente | Adaptar MiniStore | Listado y detalle de órdenes |
| Operación | Configurar admin del operador | Aprobación y rechazo protegidos |
| Integridad | Implementar transacción y tests | Stock y estados consistentes |
| Cierre | Demostración completa | Incremento de órdenes verificable |

#### Reglas de negocio obligatorias

- El talle, color, SKU, descripción y precio de cada `OrderItem` se copian desde la variante al confirmar la orden.
- El cliente solo puede consultar sus propias órdenes.
- Una orden aprobada no puede aprobarse nuevamente.
- La aprobación falla si alguna variante no posee stock suficiente.
- El descuento de stock y el cambio de estado ocurren en una misma transacción.

#### Criterio de cierre de la demostración

- La app `orders` fue creada y depende de `products` mediante `ProductVariant`.
- Un cliente autenticado puede seleccionar, agregar, quitar y confirmar variantes.
- La orden conserva sus ítems y precios aunque cambie el catálogo.
- El operador puede aprobar o rechazar desde el admin.
- El cliente ve el estado actualizado sin ingresar al admin.
- Existen tests de ownership, aprobación y stock insuficiente.

---

### 7. Clase 3 — Incremento 3: pago y seguimiento simulados

**Objetivo del tutorial:** el profesor completa el flujo comercial con pago, preparación,
despacho, seguimiento y administración final de roles.

#### Feature terminada

```text
Cliente inicia pago simulado de una orden aprobada
→ el sistema registra Payment APPROVED o REJECTED
→ operador prepara y despacha la orden desde el admin
→ se crean eventos de seguimiento
→ cliente consulta una línea de tiempo del envío
→ administrador audita la configuración de usuarios, grupos y permisos
```

#### Secuencia de 180 minutos

| Tiempo | Etapa | Entregable |
|--------|-------|------------|
| 0–15 | Repaso y demo del flujo final | El profesor presenta US-07, US-08, US-09 y US-10 |
| 15–45 | Live coding: crear app `operations` | Ejecuta `startapp`, registra la app e implementa `Payment`, `Shipment`, `ShipmentEvent` y estados |
| 45–75 | Live coding: pago simulado | El profesor implementa el servicio de pago y la vista protegida |
| 75–105 | Live coding: seguimiento del cliente | El profesor construye el seguimiento respetando el sistema visual adaptado de MiniStore |
| 105–140 | Live coding: admin del operador | El profesor implementa acciones, inlines y campos de solo lectura |
| 140–160 | Auditoría de admin y seguridad | El profesor revisa y refuerza los usuarios, grupos, permisos y separación configurados en Clase 1 |
| 160–175 | Prueba end-to-end explicada | El profesor ejecuta el recorrido completo alternando los tres roles |
| 175–180 | Síntesis del tutorial | El profesor presenta deuda técnica y posibles próximos incrementos |

#### Reglas de negocio obligatorias

- Solo pueden pagarse órdenes aprobadas.
- Cada intento de pago queda registrado.
- Un pago aprobado habilita la preparación del envío.
- Cada cambio de estado del envío genera un `ShipmentEvent`.
- El cliente solo puede seguir envíos asociados a sus órdenes.
- El operador administra operación comercial, pero no usuarios ni permisos.

#### Criterio de cierre de la demostración

- La app `operations` fue creada y depende de `orders.Order`.
- El cliente puede ejecutar un pago aprobado o rechazado de forma simulada.
- El operador puede avanzar la orden por estados válidos.
- El cliente visualiza el seguimiento actualizado.
- El administrador puede crear operadores mediante grupos y permisos.
- Existe un test end-to-end del flujo feliz y tests de transiciones inválidas.

---

### 8. Contrato de producción para filminas y minuta

Cada clase deberá producir filminas que guíen la implementación en vivo del profesor.
No son consignas prácticas para resolver por los alumnos. Durante los bloques de código,
cada filmina indica qué implementará el profesor, por qué lo hará y cómo verificará el
resultado frente al curso.

Las filminas no contienen tareas. Cada una muestra una etapa narrativa de lo que realiza
el profesor y cómo evoluciona la aplicación. La minuta asociada contiene el código exacto
de esa etapa.

#### Contenido obligatorio de cada filmina de trabajo

| Campo | Contenido |
|-------|-----------|
| Objetivo | Resultado observable de la etapa |
| Historia | Historia de usuario o regla de negocio atendida |
| Implementación docente | Qué realiza el profesor en vivo; nunca una tarea para alumnos |
| Archivos | Archivos que se crean o modifican |
| Verificación | Comando, prueba manual o test que ejecuta el profesor |
| Participación guiada | Predicción o pregunta de control para los alumnos |
| Criterio de terminado | Condición para pasar a la siguiente filmina |

#### Contenido obligatorio de la minuta por filmina

La minuta debe usar el mismo identificador de filmina e incluir:

1. explicación docente breve;
2. código exacto que implementará el profesor en esa etapa;
3. ubicación del código por archivo;
4. orden recomendado de escritura;
5. resultado esperado;
6. errores frecuentes y forma de diagnosticarlos;
7. pregunta de control para involucrar a los alumnos antes de continuar;
8. transición verbal hacia la filmina siguiente.

#### Patrón recomendado de secuencia

```text
F-01 objetivo y demo
F-02 comportamiento objetivo + criterio de aceptación
F-03 explicación del modelo
F-04 live coding del modelo
F-05 migración y prueba en shell
F-06 live coding del admin operador
F-07 explicación de permisos
F-08 live coding de vista pública o cliente
F-09 live coding de template MiniStore adaptado
F-10 integración y diagnóstico
F-11 test explicado
F-12 demo del incremento y síntesis
```

Cada clase puede expandir esta secuencia, pero debe mantener trazabilidad directa entre
filmina, implementación docente, código de minuta y verificación. No se deben incluir
consignas de práctica autónoma ni entregables para los alumnos dentro de estas clases.

---

### 9. Cobertura del plan mínimo

| Contenido mínimo obligatorio | Cobertura en el tutorial guiado |
|-----------------------------|-----------------------------|
| Persistencia y mapeo OO-relacional | Clases 1–3 mediante modelos relacionados |
| Organización modular de Django | Creación e integración de `accounts`, `products`, `orders` y `operations` |
| CRUD y consultas dinámicas | Catálogo, órdenes, filtros del admin y área cliente |
| Vistas, templates y formularios | MiniStore adaptado: web pública, carrito, checkout y seguimiento |
| Sesiones de usuario | Carrito de compras en sesión |
| Autenticación en Django | Área cliente y acceso al admin |
| Autorización, grupos y permisos | Separación Cliente, Operador y Administrador |
| Decoradores y mixins | Protección de checkout, órdenes, pago y seguimiento |
| Verificación de permisos en templates | Navegación y acciones visibles según rol |
| Django Admin y `ModelAdmin` | Catálogo, órdenes, pagos y envíos |
| Acciones en masa e inlines | Aprobación de órdenes, fotos, ítems y eventos |
| Control de acceso en admin | Operador sin acceso a usuarios/permisos |
| Personalización del sitio admin | Jazzmin + branding + organización funcional |

**Cobertura prevista:** 100% de los contenidos obligatorios de los módulos V y VI
involucrados. El cambio modifica el dominio integrador, no elimina contenidos mínimos.

---

### 10. Decisiones de alcance

#### Incluido

- ThemeWagon MiniStore como base Bootstrap 5 para toda la web pública y del cliente.
- Conversión del theme estático a templates Django con herencia, includes y `{% static %}`.
- Jazzmin para mejorar la presentación de Django Admin.
- Fotos de producto mediante `ImageField`.
- Carrito basado en sesión.
- Pagos y envíos deterministas simulados.
- Roles implementados con `Group` y `Permission`.
- Separación explícita en apps Django por responsabilidad de negocio.
- Tests focalizados en reglas de negocio y autorización.

#### Fuera de alcance para estas tres clases

- Pasarela de pago real.
- Integración con empresa logística real.
- Promociones, cupones y devoluciones.
- API REST.
- Procesamiento asíncrono y notificaciones por correo.
- Despliegue productivo y almacenamiento cloud de imágenes.
- Rediseño visual completo de MiniStore o creación de un theme desde cero.

---

### 11. Gate de aprobación docente

Antes de producir los tres temas, confirmar:

- [ ] Reemplazar BlogApp por la tienda como dominio integrador de estas tres clases.
- [ ] Usar clases de 180 minutos.
- [ ] Adoptar el tutorial guiado incremental: catálogo → órdenes → pago y envío.
- [ ] Mantener Jazzmin como personalización visual, con `ModelAdmin` como núcleo pedagógico.
- [ ] Usar ThemeWagon MiniStore como base visual del storefront y adaptarlo progresivamente a Django.
- [ ] Mantener como mínimo las apps separadas `products`, `orders` y `operations`, además de `accounts`.
- [ ] Exigir trazabilidad filmina → implementación docente → código en minuta → verificación.
- [ ] No incluir práctica autónoma ni entregables de alumnos durante estas tres clases.
