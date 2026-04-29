# Tema 04 — ORM avanzado + puente a interfaz MVC
## Módulo IV avanzado + Módulo V intro — UNTDF IF009 2026

> **Fecha**: 2026-04-29
> **Semana del plan**: 8 (replan aprobado — `salida/cursadas/2026/plan-actualizado.md`)
> **Estado**: DESIGN-COMPLETE — listo para generar minuta.md
> **Prerequisito confirmado**: ORM básico (modelos, campos, relaciones, migraciones, CRUD con shell) ya cubierto en práctica previa fuera de esta planificación formal.
> **Fuentes base**: django-6.0-docs · edu_knowledge · plan-actualizado.md §3

---

## 1. Metadatos

| Campo | Valor |
|-------|-------|
| Número | 04 |
| Nombre | ORM avanzado + puente a interfaz MVC |
| Módulos plan | IV avanzado (ORM completo) + V intro (View base + **Django Template Language completo**) |
| Duración total | **360 min = 6 h = 1 clase teórica + 1 clase práctica (180 min c/u)** |
| Audiencia | 3º año UNTDF Sistemas/AUS, niveles heterogéneos |
| Paradigma docente | **POO estricto: todas las vistas son class-based views. Prohibido FBV.** |
| Dominio | BlogApp — `Post`, `Category`, `Comment` (unificador semanas 8 y 9) |
| TP asociado | TP-5 (por definir) — alcance: modelos + admin + ORM avanzado + primeras vistas `View` + templates con DTL |
| Prerequisitos | Tema 03 + práctica previa de ORM básico (migraciones, relaciones, CRUD shell) |
| Parcial 1 | Movido al **inicio de Semana 9 teórica** — no condiciona esta clase |

---

## 2. Cobertura del Plan Mínimo

### Módulo IV — Manejo de Persistencia (tópicos avanzados)

| Tópico mínimo obligatorio | Cobertura |
|---------------------------|-----------|
| Operaciones CRUD con Django | Clase Teórica §T1 — repaso rápido + profundización QuerySet |
| Consultas dinámicas en Django | Clase Teórica §T1–§T2 + Clase Práctica §P1 |

> Los tópicos de persistencia conceptual (impedance mismatch, concepto ORM, comparación tecnologías) fueron cubiertos en Tema 03 y en la práctica previa — **no se repiten**.

### Módulo V — Desarrollo de interfaces de usuario utilizando el patrón MVC (introducción)

| Tópico mínimo obligatorio | Cobertura |
|---------------------------|-----------|
| Vistas y templates de Django como parte del patrón MVC | Clase Teórica §T3 + §T4 (DTL) + Clase Práctica §P2 |
| Modelado de interfaz de usuario con Django y HTML5 | Clase Teórica §T4 (DTL) + Clase Práctica §P2 |
| Formularios de Django | ➡️ **Movido a Tema 05** — fuera del alcance de esta clase |
| Vistas y validaciones de formularios | ➡️ **Movido a Tema 05** — fuera del alcance de esta clase |

> Los tópicos de vistas genéricas (`ListView`, `DetailView`) y Template Language completo se profundizan en **Semana 9** — aquí se introduce `View` base como primer escalón.

### Resultado de cobertura de esta clase

**Módulo IV**: 100% de los tópicos avanzados asignados a Semana 8.
**Módulo V**: introducción intencional — continuidad explícita con Semana 9.
**Sin scope creep**: nada fuera de los módulos IV y V del plan mínimo.

---

## 3. Estructura de la clase — Vista general

```
CLASE TEÓRICA (180 min) ─────────────────────────────────────────────
  T1  45'  QuerySet API avanzado + chaining + lazy evaluation + CRUD completo
  T2  40'  Consultas dinámicas: Q objects · F expressions · annotate · aggregate
           + performance: select_related · prefetch_related
  T3  25'  Puente MVC: ciclo request/response · CBV con View · as_view() · dispatch() · get() · post()
  T4  45'  Django Template Language (DTL) completo:
           variables · dot notation · filtros · modificadores · {% for %} + forloop ·
           {% if/elif/else %} operadores · {% url %} · {% load %} · {% static %} ·
           {% with %} · {% comment %} · herencia extends/block/block.super · {% include %}
  ──  25'  Breaks + apertura + cierre

NOTA: Formularios (ModelForm, PRG) → Tema 05

CLASE PRÁCTICA (180 min) ────────────────────────────────────────────
  P1  60'  BlogApp Codespaces: shell + managers/QuerySets sobre Post, Category, Comment
  P2 120'  Vista OOP + DTL completo: View base → URL → contexto → templates con herencia,
           partials con {% include %}, {% with %}, {% load static %}, forloop vars
```

---

## 4. CLASE TEÓRICA — ORM avanzado + puente a interfaz MVC (180 min)

> **Conocimiento previo de la práctica anterior (orm.pdf — 16 páginas):**  
> Los estudiantes ya saben: shell de Django, CRUD básico (`.save()`, `.filter()`, `.all()`, `.get()`), ordenamiento (`.order_by()`), eliminación (`.delete()`), Managers personalizados con `get_queryset()`, métodos de modelo a nivel instancia. El dominio era Biblioteca (Autor, Libro, Lector).  
> **Esta clase arranca** desde lazy evaluation en profundidad, Q objects, F expressions, aggregations y N+1 — todo genuinamente nuevo para los estudiantes. El dominio cambia a **BlogApp** (Post, Category, Comment).

### Objetivos (Bloom)

1. **Analizar** (4) el ciclo de vida de un `QuerySet`: lazy evaluation, caché interna, y cuándo se evalúa realmente.
2. **Construir** (4) consultas complejas usando `Q objects`, `F expressions`, `annotate()` y `aggregate()` — no vistas en la práctica anterior.
3. **Evaluar** (5) el costo del problema N+1 con `connection.queries` e implementar `select_related` / `prefetch_related`.
4. **Extender** (3) managers personalizados ya conocidos hacia el dominio BlogApp, aplicando `only()`, `defer()` y `values()`.
5. **Comprender** (2) el ciclo request/response de Django y la responsabilidad de cada capa MVT.
6. **Reconocer** (2) `View` como clase base, `as_view()`, `dispatch()`, y los métodos `get()` / `post()`.
7. **Construir** (3) templates con DTL completo: herencia, partials, filtros encadenados, `{% load static %}` y `forloop` variables.

### Agenda

| Tiempo | Código | Bloque |
|--------|--------|--------|
| 0–10 | — | Apertura: contextualización — "ya saben ORM básico, hoy lo usamos como profesionales" |
| 10–55 | T1 | QuerySet API avanzado |
| 55–95 | T2 | Consultas dinámicas y performance |
| 95–100 | — | **Break** |
| 100–125 | T3 | Puente MVC + Class-Based Views con `View` base |
| 125–170 | T4 | **Django Template Language (DTL) completo** |
| 170–180 | — | Cierre + mapa de la práctica + preview Semana 9 (formularios) |

---

### §T1 — QuerySet API: de lo básico a lo profesional (45 min)

> **Puente pedagógico**: los estudiantes usaron `filter()`, `all()`, `get()` y `order_by()` en la práctica anterior sobre el modelo Biblioteca. Saben que funciona — hoy entendemos **por qué funciona** y sumamos las herramientas que faltan.

#### Lazy evaluation: por qué el ORM no consulta la BD inmediatamente

Esto **no estaba en la práctica anterior** — el porqué de la eficiencia del ORM:

- Un `QuerySet` es un **objeto Python diferido** — representa la consulta, no el resultado.
- La SQL **solo se ejecuta** cuando se consume: iteración, `list()`, slicing, `bool()`, `len()`, `repr()`.
- **Caché interna**: una vez evaluado, una segunda iteración **no vuelve a la BD**.

```python
# Construye el QuerySet — cero SQL ejecutada
qs = Post.objects.filter(published=True).order_by("-created_at")

# SQL ejecuta aquí (iteración)
for post in qs:
    print(post.title)

# Segunda iteración — usa caché, no va a la BD
for post in qs:
    print(post.title)   # sin SQL extra
```

**Por qué importa**: en templates Django, el QuerySet se evalúa una sola vez. Construirlo en la vista (como ya haremos en §T3) es económico.

#### Chaining: encadenar vs repetir filtros

```python
# Los alumnos ya conocen filter() y order_by() por separado
# Hoy los combinamos en cadenas expresivas
Post.objects.filter(published=True)\
            .exclude(author__is_staff=True)\
            .order_by("-created_at")\
            .values("title", "author__username")[:10]
```

> **Cada método devuelve un nuevo QuerySet** — la BD no recibe nada hasta el slicing `[:10]`.

#### Métodos nuevos: más allá de `.get()` y `.filter()`

| Método | Resultado | Novedad vs orm.pdf |
|--------|-----------|-------------------|
| `.first()` / `.last()` | instancia o `None` | ✅ nuevo |
| `.get_or_create(...)` | `(obj, created: bool)` | ✅ nuevo |
| `.update_or_create(...)` | `(obj, created: bool)` | ✅ nuevo |
| `.exists()` | `bool` | ✅ nuevo |
| `.count()` | `int` | ✅ nuevo |
| `.values("campo")` | `QuerySet` de dicts | ✅ nuevo |
| `.values_list("campo", flat=True)` | `QuerySet` de valores | ✅ nuevo |
| `.only("campo")` | instancias parciales (eficiente) | ✅ nuevo |
| `.defer("campo")` | excluir campos pesados (ej: `body`) | ✅ nuevo |

#### Escritura masiva — nuevo respecto a la práctica anterior

```python
# Los alumnos conocen .save() individual
# Hoy: update() y bulk_create() para operaciones masivas

# update() → SQL UPDATE directo, no llama a .save(), más eficiente
Post.objects.filter(author=user).update(published=True)

# delete() ya visto — lo que es nuevo: el valor de retorno
n_deleted, by_type = Post.objects.filter(published=False).delete()
# by_type → {'blog.Post': 3, 'blog.Comment': 12}

# bulk_create → inserts masivos sin llamar save() por cada objeto
Post.objects.bulk_create([
    Post(title="Post A", author=user),
    Post(title="Post B", author=user),
])
```

**Filminas previstas §T1: ~12**

---

### §T2 — Consultas dinámicas y performance (45 min)

#### Q objects — condiciones lógicas compuestas

```python
from django.db.models import Q

# OR
Post.objects.filter(Q(published=True) | Q(author=request.user))

# AND explícito
Post.objects.filter(Q(category=cat) & Q(published=True))

# NOT
Post.objects.filter(~Q(author__is_staff=True))

# Combinación dinámica (construida en runtime)
filters = Q()
if search:
    filters &= Q(title__icontains=search)
if category_id:
    filters &= Q(category_id=category_id)
Post.objects.filter(filters)
```

#### F expressions — operaciones sobre valores de campo

```python
from django.db.models import F

# Incrementar sin traer el objeto a Python
Post.objects.filter(pk=pk).update(views=F("views") + 1)

# Comparar campos entre sí
Post.objects.filter(updated_at__gt=F("created_at"))
```

#### Agregaciones

```python
from django.db.models import Count, Avg, Sum, Max, Min

# aggregate() → dict con el resultado global
stats = Post.objects.aggregate(
    total=Count("id"),
    avg_comments=Avg("comment__id")
)

# annotate() → agrega un campo calculado a cada objeto del QuerySet
categories = Category.objects.annotate(post_count=Count("post"))
for cat in categories:
    print(cat.name, cat.post_count)
```

#### Performance: el problema N+1

```python
# ❌ N+1: 1 query para posts + 1 query por post para su autor
posts = Post.objects.all()
for post in posts:
    print(post.author.username)   # query extra aquí

# ✅ select_related: JOIN SQL → 1 sola query (FK / O2O)
posts = Post.objects.select_related("author").all()

# ✅ prefetch_related: queries separadas con IN → para M2M y reverse FK
posts = Post.objects.prefetch_related("categories", "comments").all()

# Combinación real
posts = Post.objects.select_related("author")\
                    .prefetch_related("categories")\
                    .filter(published=True)\
                    .order_by("-created_at")
```

**Filminas previstas §T2: ~10**
**Evaluación formativa §T2**: ejercicio pizarra — dar el código con N+1 y pedir la corrección.

---

### §T3 — Puente MVC: ciclo request/response + CBV con `View` base (25 min)

> **Pivote de la clase**: pasamos de *datos* a *interfaz*. Django ya conoce los modelos — ahora les ponemos cara.

#### Ciclo request/response en Django (MVT completo)

```
Browser → HTTP Request → urls.py → View (clase) → Model (si necesita datos)
                                                 → Template (renderizado)
                    ← HTTP Response ← Template renderizado ←
```

Responsabilidades:
- **Model**: datos y lógica de dominio.
- **Template**: presentación HTML — no tiene lógica de negocio.
- **View (controlador)**: recibe request, consulta modelos, pasa contexto al template, devuelve response.

#### `View` como clase base — jerarquía CBV

```python
from django.views import View
from django.shortcuts import render
from .models import Post

class PostListView(View):
    template_name = "blog/post_list.html"

    def get(self, request):
        posts = Post.objects.filter(published=True).order_by("-created_at")
        return render(request, self.template_name, {"posts": posts})
```

Puntos clave:
- `View.as_view()` es el entry point — convierte la clase en callable.
- `dispatch()` enruta a `get()`, `post()`, `put()`, etc. según el método HTTP.
- `get()` maneja GET; `post()` manejará POST (formularios).
- **Cada acción HTTP = un método de la clase** — esto es OOP, no spaghetti.

```python
# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
```

**¿Por qué `View` base y no genérica?**
- `View` expone el mecanismo completo sin magia — ideal para primera exposición.
- En Semana 9 se migrará a `ListView` / `DetailView` — el estudiante entenderá *qué automatizan* porque ya vio el manual.

**Filminas previstas §T3: ~8**

---

### §T4 — Django Template Language (DTL) completo (45 min)

> **Fuente**: Django 6.0 Official Docs — *The Django template language* (`docs.djangoproject.com/en/6.0/ref/templates/language/`)  
> **Objetivo**: dominio operativo completo de DTL — variables, filtros/modificadores, todos los tags básicos y herencia de templates. Los formularios quedan para Tema 05.

#### Los 4 constructos fundamentales de DTL

| Constructo | Sintaxis | Propósito |
|-----------|----------|-----------|
| Variable | `{{ variable }}` | Renderizar un valor del contexto |
| Filtro | `{{ valor\|filtro }}` | Transformar un valor al mostrarlo |
| Tag | `{% tag %}` | Lógica: bucles, condicionales, herencia |
| Comentario | `{# texto #}` | Documentación — no se renderiza |

#### Variables y notación de punto

El contexto es un diccionario Python que la vista pasa al template:

```python
# En la vista
context = {
    "post": post_instance,
    "posts": Post.objects.filter(published=True),
}
return render(request, "blog/post_list.html", context)
```

En el template:

```html
{{ post.title }}              {# accede al atributo title del objeto post #}
{{ post.author.username }}    {# notación encadenada: post → author → username #}
{{ posts.0.title }}           {# primer elemento de la lista #}
```

- Django resuelve el punto probando en orden: atributo, índice de diccionario, índice de lista, método callable.
- **Atributos privados** (prefijo `_`) son inaccesibles por seguridad.

#### Filtros: transformar datos en el template

Sintaxis: `{{ valor|filtro }}` o `{{ valor|filtro:argumento }}`.  
Se pueden encadenar: `{{ texto|escape|linebreaks }}` — se aplican izquierda a derecha.

| Filtro | Ejemplo | Resultado |
|--------|---------|-----------|
| `lower` | `{{ post.title\|lower }}` | todo en minúsculas |
| `upper` | `{{ post.title\|upper }}` | TODO EN MAYÚSCULAS |
| `date` | `{{ post.created_at\|date:"d/m/Y" }}` | `28/06/2025` |
| `truncatewords` | `{{ post.body\|truncatewords:30 }}` | primeras 30 palabras + `…` |
| `linebreaks` | `{{ post.body\|linebreaks }}` | convierte `\n` en `<p>` / `<br>` |
| `default` | `{{ post.subtitle\|default:"Sin subtítulo" }}` | valor de fallback si vacío |
| `length` | `{{ comments\|length }}` | cantidad de elementos |
| `escape` | `{{ user_input\|escape }}` | escapa HTML (activado por defecto) |

> **Nota pedagógica**: Django auto-escapa variables por defecto — protección XSS incorporada.

#### Tags de control de flujo y utilidad

##### `{% for %}` — iteración completa

```html
{% for post in posts %}
    <p>{{ forloop.counter }}. {{ post.title }}</p>
{% empty %}
    <p>No hay posts publicados todavía.</p>
{% endfor %}
```

**Variables automáticas de `forloop`** — disponibles dentro de cualquier `{% for %}`:

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `forloop.counter` | int | Índice actual, empezando en **1** |
| `forloop.counter0` | int | Índice actual, empezando en **0** |
| `forloop.revcounter` | int | Índice inverso, terminando en 1 |
| `forloop.revcounter0` | int | Índice inverso, terminando en 0 |
| `forloop.first` | bool | `True` si es la primera iteración |
| `forloop.last` | bool | `True` si es la última iteración |
| `forloop.parentloop` | objeto | En loops anidados, accede al loop padre |

```html
{% for post in posts %}
    {% if forloop.first %}<ul>{% endif %}
    <li class="{% if forloop.last %}last{% endif %}">
        {{ forloop.counter }}. {{ post.title }}
    </li>
    {% if forloop.last %}</ul>{% endif %}
{% endfor %}
```

Iterar sobre diccionarios:
```html
{% for key, value in my_dict.items %}
    <dt>{{ key }}</dt><dd>{{ value }}</dd>
{% endfor %}
```

##### `{% if %}` — condicionales con operadores completos

Operadores soportados: `==`, `!=`, `<`, `>`, `<=`, `>=`, `and`, `or`, `not`, `in`, `not in`, `is`, `is not`

```html
{% if posts %}
    <p>Hay {{ posts|length }} publicaciones.</p>
{% elif drafts %}
    <p>Solo hay borradores: {{ drafts|length }}.</p>
{% else %}
    <p>Sin contenido aún.</p>
{% endif %}

{# Operadores combinados #}
{% if post.published and post.author == request.user %}
    <a href="...">Editar</a>
{% endif %}

{% if "django" in post.tags %}
    <span class="tag">Django</span>
{% endif %}

{# not: negación #}
{% if not post.published %}
    <span class="draft">Borrador</span>
{% endif %}

{# Filtros dentro de if #}
{% if posts|length > 5 %}
    <p>Blog activo — más de 5 publicaciones.</p>
{% endif %}
```

> **Trampa**: la precedencia de operadores en DTL es **izquierda a derecha** — no como Python. Usar `{% if (a or b) and c %}` no funciona. Anidar `{% if %}` cuando se necesite lógica compleja.

##### `{% with %}` — alias de variables

Evitar acceder repetidas veces al mismo valor costoso (ej: FK lookup):

```html
{% with author=post.author %}
    <p>Autor: {{ author.get_full_name }}</p>
    <p>Email: {{ author.email }}</p>
    <p>Posts: {{ author.post_set.count }}</p>
{% endwith %}
{# Fuera del with, author ya no está disponible #}
```

También válido para acortar expresiones largas:
```html
{% with total=business.employees.count %}
    Hay {{ total }} empleado{{ total|pluralize }}.
{% endwith %}
```

##### `{% load %}` — cargar librerías de tags

Antes de usar tags o filtros de una librería, hay que cargarla con `{% load %}`:

```html
{# En la primera línea útil del template (después de {% extends %} si lo hay) #}
{% load static %}
{% load humanize %}
{% load i18n %}
```

> `{% load %}` es necesario en **cada template** que use la librería — no se hereda.

##### `{% static %}` — URLs de archivos estáticos

```html
{% load static %}

<link rel="stylesheet" href="{% static 'blog/css/styles.css' %}">
<script src="{% static 'blog/js/app.js' %}"></script>
<img src="{% static 'blog/img/logo.png' %}" alt="Logo">
```

Requiere en `settings.py`:
```python
STATIC_URL = "/static/"          # prefijo de URL
STATICFILES_DIRS = [BASE_DIR / "static"]  # carpeta del proyecto
```

##### `{% comment %}` — comentarios multi-línea

```html
{# Comentario de una sola línea — no se renderiza #}

{% comment "Razón opcional del comentario" %}
    <p>Este bloque completo es ignorado por el motor de templates.</p>
    {% for post in posts %}{{ post.title }}{% endfor %}
    Útil para desactivar temporalmente secciones largas.
{% endcomment %}
```

##### `{% now %}` — fecha y hora actuales

```html
<p>Actualizado: {% now "d/m/Y H:i" %}</p>
<p>Año actual: {% now "Y" %}</p>
{# Formatos: "Y" año, "m" mes, "d" día, "H:i" hora:min #}
```

##### `{% url %}` — resolver URLs por nombre (repaso + casos avanzados)

```html
{# Básico — ya visto #}
<a href="{% url 'blog:post-list' %}">Listado</a>

{# Con argumento posicional #}
<a href="{% url 'blog:post-detail' post.pk %}">Ver post</a>

{# Con argumento por nombre (más legible) #}
<a href="{% url 'blog:post-detail' pk=post.pk %}">Ver post</a>

{# Guardar la URL en variable con as #}
{% url 'blog:post-detail' pk=post.pk as post_url %}
{% if post_url %}
    <a href="{{ post_url }}">Enlace</a>
{% endif %}
```

##### `{% csrf_token %}` — seguridad en formularios (intro)

```html
<form method="post">
    {% csrf_token %}
    {# ... campos ... #}
</form>
```

> Obligatorio en **todo formulario POST**. Django lo verifica automáticamente — sin él, `403 Forbidden`. Profundización en Tema 05 cuando veamos formularios.

#### Herencia de templates: el principio DRY aplicado a HTML

> *"La parte más poderosa — y por eso la más compleja — del motor de templates de Django."*  
> — Django 6.0 docs

**Problema**: sin herencia, cada template repite el mismo `<head>`, navbar, footer.  
**Solución**: template base ("esqueleto") con `{% block %}` para las partes variables; children lo extienden.

**`blog/templates/blog/base.html`** — esqueleto del sitio:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Mi Blog{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'blog:post-list' %}">Inicio</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>BlogApp © 2025</p>
    </footer>
</body>
</html>
```

**`blog/templates/blog/post_list.html`** — child template:

```html
{% extends "blog/base.html" %}

{% block title %}Listado de Posts{% endblock %}

{% block content %}
    <h1>Publicaciones</h1>
    {% for post in posts %}
        <article>
            <h2>
                <a href="{% url 'blog:post-detail' pk=post.pk %}">
                    {{ post.title }}
                </a>
            </h2>
            <time>{{ post.created_at|date:"d/m/Y" }}</time>
            <p>{{ post.body|truncatewords:30 }}</p>
        </article>
    {% empty %}
        <p>Todavía no hay publicaciones.</p>
    {% endfor %}
{% endblock %}
```

**Reglas de herencia**:
1. `{% extends %}` **debe ser la primera línea** del child template.
2. Solo el contenido dentro de `{% block %}` puede sobreescribirse.
3. **`{{ block.super }}`** — incluye el contenido del bloque padre y agrega el propio:
   ```html
   {# child: agrega script sin borrar lo que el base ya tenía en el bloque #}
   {% block extra_scripts %}
       {{ block.super }}
       <script src="{% static 'blog/js/post.js' %}"></script>
   {% endblock %}
   ```
4. Cuantos más bloques, más flexible — pero no agregar bloques que nunca se sobreescriben.
5. Los child templates pueden ser a su vez base de otros templates (herencia multinivel).

#### `{% include %}` — reutilizar fragmentos

Para componentes parciales reutilizables (tarjetas, comentarios, paginación):

```html
{# en post_list.html #}
{% for post in posts %}
    {% include "blog/partials/post_card.html" with post=post %}
{% endfor %}
```

#### Configuración en `settings.py`

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],          # templates a nivel proyecto
        "APP_DIRS": True,                           # busca en app/templates/app/ automáticamente
        "OPTIONS": {"context_processors": [...]},
    },
]
```

Convención de estructura con `APP_DIRS=True`:
```
blog/
  templates/
    blog/          ← namespace: evita colisiones entre apps
      base.html
      post_list.html
      post_detail.html
      partials/
        post_card.html
```

**Filminas previstas §T4 (DTL): ~16**

### Resumen teórica: ~46 filminas previstas

> **Formularios (ModelForm, Form, PRG)**: movidos a **Tema 05** — fuera del alcance de esta clase.

---

## 5. CLASE PRÁCTICA — BlogApp en Codespaces (180 min)

### Objetivos (Bloom)

1. **Ejecutar** (3) consultas avanzadas con Q objects, F expressions, `annotate()` y `aggregate()` sobre BlogApp en el shell.
2. **Transferir** (4) el conocimiento de Managers del modelo Biblioteca al dominio BlogApp con `only()` y `defer()`.
3. **Construir** (3) templates DTL completos: herencia `extends`/`block`, partials con `{% include %}`, `{% with %}`, `forloop` vars, `{% load static %}` / `{% static %}`.
4. **Implementar** (3) una CBV con `View` base que entregue contexto al template.
5. **Detectar** (4) el problema N+1 con `connection.queries` y aplicar `select_related`.

### Agenda

| Tiempo | Código | Bloque |
|--------|--------|--------|
| 0–10 | — | Apertura: abrir Codespace BlogApp + verificar migraciones aplicadas |
| 10–70 | P1 | Shell avanzado: consultas sobre Post, Category, Comment |
| 70–75 | — | **Break** |
| 75–180 | P2 | Vista OOP + DTL completo: herencia, partials, with, static, forloop |

---

### §P1 — BlogApp shell: consultas avanzadas (60 min)

#### Setup del entorno

```bash
# Codespace o local con .venv activo
python manage.py shell
```

```python
from blog.models import Post, Category, Comment
from django.contrib.auth.models import User
```

> **Nota para el docente**: los estudiantes ya hicieron CRUD básico, filter/order/delete y managers en la práctica Biblioteca (orm.pdf). Los ejercicios 1 y 2 abajo son puente rápido hacia BlogApp. Los ejercicios 3–6 son el contenido nuevo real.

#### Ejercicios guiados (resolución paso a paso con el docente)

**Ejercicio 1 — Puente: adaptar lo conocido al dominio BlogApp (10 min)**
```python
# Repaso rápido — mismos conceptos, nuevo modelo
# Los alumnos ya hicieron esto con Libro/Autor/Lector

# get() vs filter().first() — consolidar la diferencia
cat = Category.objects.get(slug="python")           # DoesNotExist si no existe
cat = Category.objects.filter(slug="python").first() # None si no existe — más seguro

# Métodos nuevos: exists() y count()
Category.objects.filter(slug="python").exists()     # True/False — no trae el objeto
Post.objects.filter(published=True).count()          # int — eficiente

# values_list: solo los títulos, sin instanciar Post
titulos = Post.objects.filter(published=True).values_list("title", flat=True)
print(list(titulos))
```

**Ejercicio 2 — Q objects: búsqueda multi-campo**
```python
from django.db.models import Q

# Posts publicados O del usuario actual
qs = Post.objects.filter(Q(published=True) | Q(author=request.user))

# Búsqueda dinámica: filtrar solo si se provee valor
term = "django"   # simular input de usuario
q_filter = Q(title__icontains=term) | Q(content__icontains=term)
resultados = Post.objects.filter(q_filter, published=True)
```

**Ejercicio 3 — Aggregations: estadísticas del blog**
```python
from django.db.models import Count, Avg

# Cuántos posts hay en total
total = Post.objects.aggregate(total=Count("id"))

# Categorías con su cantidad de posts — ordenadas de mayor a menor
categorias = Category.objects.annotate(n_posts=Count("post"))\
                             .order_by("-n_posts")
for cat in categorias:
    print(f"{cat.name}: {cat.n_posts} posts")
```

**Ejercicio 4 — F expressions: incrementar contador sin traer objeto**
```python
from django.db.models import F

# Simular que un post fue visto (+1 view)
Post.objects.filter(pk=1).update(views=F("views") + 1)
```

**Ejercicio 5 — Detectar N+1 con `connection.queries`**
```python
from django.db import connection, reset_queries
from django.conf import settings

settings.DEBUG = True
reset_queries()

# ❌ versión con N+1
posts = Post.objects.all()
for p in posts:
    _ = p.author.username

print(f"Queries: {len(connection.queries)}")   # → N+1

reset_queries()

# ✅ versión con select_related
posts = Post.objects.select_related("author").all()
for p in posts:
    _ = p.author.username

print(f"Queries: {len(connection.queries)}")   # → 1
```

**Ejercicio 6 — Manager personalizado para BlogApp (extensión de lo ya visto)**

> Los alumnos crearon un `Manager` para Libro en la práctica anterior. Hoy lo **transfieren a BlogApp y extienden** con `only()` para eficiencia.

```python
# blog/models.py — misma idea que Libro.disponibles, ahora para Post
class PublishedManager(models.Manager):
    def get_queryset(self):
        # Misma estructura que vieron en orm.pdf
        return super().get_queryset().filter(published=True)

    def recientes(self, n=10):
        """Top N publicados — método nuevo sobre el manager."""
        return self.get_queryset()\
                   .select_related("author")\
                   .only("title", "created_at", "author__username")\
                   .order_by("-created_at")[:n]

class Post(models.Model):
    objects = models.Manager()          # manager por defecto (siempre declarar)
    published = PublishedManager()      # manager custom

# Uso — lo que hicieron con Libro.disponibles.all(), ahora:
Post.published.all()                    # solo publicados
Post.published.recientes(5)             # top 5 con only() — eficiente
```

**Diferencia clave respecto a la práctica anterior**: `only()` y `select_related()` dentro del manager — los alumnos ven cómo el manager puede encapsular estrategias de performance.

---

### §P2 — Vista OOP + DTL completo (105 min)

> **Meta**: conectar el ORM con la capa de presentación sin magia. El estudiante construye la cadena completa URL → Vista → Modelo → Template.

#### Estructura mínima BlogApp para la práctica

```
blogapp/
  blog/
    models.py        ← ya existe (Post, Category, Comment)
    views.py         ← aquí trabajamos
    urls.py          ← aquí conectamos
    templates/
      blog/
        post_list.html
        post_detail.html
```

#### Paso 1 — `PostListView`

```python
# blog/views.py
from django.views import View
from django.shortcuts import render
from .models import Post

class PostListView(View):
    """Lista de posts publicados — ordenados por fecha descendente."""
    template_name = "blog/post_list.html"

    def get(self, request):
        posts = Post.objects.select_related("author")\
                            .prefetch_related("categories")\
                            .filter(published=True)\
                            .order_by("-created_at")
        return render(request, self.template_name, {"posts": posts})
```

#### Paso 2 — `PostDetailView`

```python
from django.shortcuts import get_object_or_404

class PostDetailView(View):
    """Detalle de un post individual."""
    template_name = "blog/post_detail.html"

    def get(self, request, pk):
        post = get_object_or_404(
            Post.objects.select_related("author").prefetch_related("categories"),
            pk=pk,
            published=True
        )
        return render(request, self.template_name, {"post": post})
```

#### Paso 3 — Conectar URLs

```python
# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
```

#### Paso 4 — Templates con herencia (base.html + hijos)

> **Ahora aplicamos DTL completo**: en lugar de copiar el HTML en cada template, construimos el esqueleto base y los hijos lo extienden.

**Estructura de archivos:**
```
blog/
  templates/
    blog/
      base.html          ← esqueleto del sitio
      post_list.html     ← child: listado
      post_detail.html   ← child: detalle
```

```html
{# blog/templates/blog/base.html — ESQUELETO DEL SITIO #}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}BlogApp{% endblock %} | IF009</title>
</head>
<body>
    <nav>
        <a href="{% url 'blog:post-list' %}">Inicio</a>
        <a href="{% url 'blog:post-create' %}">Nuevo Post</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>BlogApp — Laboratorio de Programación 2025</p>
    </footer>
</body>
</html>
```

```html
{# blog/templates/blog/post_list.html — CHILD: extiende base #}
{% extends "blog/base.html" %}

{% block title %}Listado de Posts{% endblock %}

{% block content %}
    <h1>Publicaciones</h1>
    {% for post in posts %}
        <article>
            <h2>
                <a href="{% url 'blog:post-detail' post.pk %}">
                    {{ post.title }}
                </a>
            </h2>
            <p>
                Por <strong>{{ post.author.username }}</strong>
                — {{ post.created_at|date:"d/m/Y" }}
            </p>
            <p>{{ post.body|truncatewords:30 }}</p>
        </article>
    {% empty %}
        <p>No hay posts publicados todavía.</p>
    {% endfor %}
{% endblock %}
```

```html
{# blog/templates/blog/post_detail.html — CHILD: extiende base #}
{% extends "blog/base.html" %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
    <article>
        <h1>{{ post.title }}</h1>
        <p>Por <strong>{{ post.author.username }}</strong>
           — {{ post.created_at|date:"d/m/Y" }}</p>
        <div>{{ post.body|linebreaks }}</div>
    </article>
    <a href="{% url 'blog:post-list' %}">← Volver al listado</a>
{% endblock %}
```

**Verificación Paso 4**: `python manage.py runserver` → navegar a `/blog/` → ver listado con navbar del base → clic en un post → ver detalle con el mismo esqueleto sin duplicar HTML.

#### Paso 5 — `{% with %}`: alias para evitar lookups repetidos

Editá `post_list.html` para usar `{% with %}` en la tarjeta del post:

```html
{% for post in posts %}
    {% with author=post.author %}
        <article>
            <h2><a href="{% url 'blog:post-detail' post.pk %}">{{ post.title }}</a></h2>
            <p>Por {{ author.get_full_name|default:author.username }}</p>
            <p>{{ post.created_at|date:"d/m/Y" }}</p>
            <p>{{ post.body|truncatewords:30 }}</p>
        </article>
    {% endwith %}
{% endfor %}
```

> Sin `{% with %}`, `post.author` dispara un SQL extra por cada iteración si no usaste `select_related`. Con `{% with %}` el lookup se hace una sola vez en la expresión de asignación.

#### Paso 6 — `forloop` variables: numerar y destacar

Agregá indicadores visuales usando `forloop`:

```html
{% for post in posts %}
    <article {% if forloop.first %}class="featured"{% endif %}>
        <span class="num">{{ forloop.counter }}.</span>
        <h2>{{ post.title }}</h2>
        {% if forloop.last %}
            <p><em>Fin del listado — {{ forloop.counter }} post{{ forloop.counter|pluralize }} en total.</em></p>
        {% endif %}
    </article>
{% endfor %}
```

#### Paso 7 — Partial con `{% include %}`: tarjeta de post reutilizable

Creá `blog/templates/blog/partials/post_card.html`:

```html
{# blog/templates/blog/partials/post_card.html #}
{# Espera la variable "post" pasada por el include #}
<article class="post-card">
    <h2>
        <a href="{% url 'blog:post-detail' post.pk %}">{{ post.title }}</a>
    </h2>
    <p class="meta">
        {{ post.author.username }} — {{ post.created_at|date:"d/m/Y" }}
        {% if not post.published %}
            <span class="badge">[Borrador]</span>
        {% endif %}
    </p>
    <p>{{ post.body|truncatewords:25 }}</p>
</article>
```

Usarlo en `post_list.html`:

```html
{% block content %}
    <h1>Publicaciones</h1>
    {% for post in posts %}
        {% include "blog/partials/post_card.html" with post=post %}
    {% empty %}
        <p>No hay posts publicados todavía.</p>
    {% endfor %}
{% endblock %}
```

**Ventaja**: si más adelante otras páginas muestran tarjetas de post (ej: homepage, búsqueda), todas usan el mismo partial — un solo lugar para cambiar el diseño.

#### Paso 8 — `{% load static %}` y `{% static %}`: archivos estáticos

Agregá un CSS básico al proyecto:

```
blogapp/
  static/
    blog/
      css/
        styles.css
```

```css
/* static/blog/css/styles.css */
body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 1rem; }
nav { background: #333; padding: 0.5rem; }
nav a { color: white; margin-right: 1rem; text-decoration: none; }
.post-card { border-bottom: 1px solid #ccc; padding: 1rem 0; }
.badge { background: orange; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.8em; }
```

Actualizá `base.html` para cargarlo:

```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}BlogApp{% endblock %} | IF009</title>
    <link rel="stylesheet" href="{% static 'blog/css/styles.css' %}">
    {% block extra_head %}{% endblock %}
</head>
<body>
    <nav>
        <a href="{% url 'blog:post-list' %}">Inicio</a>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>BlogApp — Laboratorio de Programación 2026 — {% now "Y" %}</p>
    </footer>
    {% block extra_scripts %}{% endblock %}
</body>
</html>
```

Verificar en `settings.py`:
```python
STATICFILES_DIRS = [BASE_DIR / "static"]
```

Correr `python manage.py runserver` y confirmar que el CSS se aplica.

#### Paso 9 — `{% comment %}` y `{# #}`: documentar templates

Practicar en cualquier template:

```html
{# Este comentario de una línea no aparece en el HTML generado #}

{% comment "Sección pendiente de diseño" %}
    <section class="sidebar">
        {# aquí irá el widget de categorías en Semana 9 #}
    </section>
{% endcomment %}

{# Truco: usar comment para desactivar código temporalmente sin borrar #}
```

Inspeccioná el HTML generado en el navegador (Ctrl+U) → confirmar que los comentarios DTL **no aparecen** en el output.

---

## 6. Ajustes operativos del replan (Semana 8)

| Ajuste | Detalle |
|--------|---------|
| **Parcial 1** | Movido al inicio de Semana 9 teórica — no impacta esta clase |
| **TP-5 alcance** | Modelos + admin + ORM avanzado + primeras vistas `View` + DTL completo + tests básicos |
| **Django Admin** | Soporte de inspección del dominio durante la práctica — no es eje principal de la clase |
| **Vistas genéricas** | NO en esta clase — se introducen en Semana 9 (refactor de `View` → `ListView`/`DetailView`) |
| **Template Language** | **DTL completo en esta clase** — tags básicos, herencia, partials, static, forloop, with, comment |
| **Formularios (ModelForm, PRG)** | **Movido a Tema 05** — decisión del docente para dar DTL el espacio que merece |
| **Bootstrap** | NO en esta clase — CSS propio mínimo vía `{% static %}` — Bootstrap en Semana 9 |

---

## 7. Evaluación formativa

| **Momento** | **Tipo** | **Descripción** |
|---------|------|-------------|
| §T2 min 75 | Ejercicio pizarra | Código con N+1 → identificar problema → proponer corrección con `select_related` |
| §T3 min 120 | Pregunta clase | "¿Qué pasa si el método HTTP es PUT y la CBV no tiene método `put()`?" → `405 Method Not Allowed` |
| §T4 min 145 | Pregunta clase | "¿Qué pasa si un child template define un `{% block %}` que no existe en el base?" → se ignora. "¿Dónde debe estar `{% extends %}`?" → primera línea |
| §T4 min 165 | Mini-ejercicio | Escribir en pizarra: template que usa `{% for %}` + `forloop.counter` + `{% if forloop.first %}` + `{% empty %}` |
| §P1 min 65 | Verificación shell | Cada grupo ejecuta `len(connection.queries)` antes y después del `select_related` |
| §P2 min 120 | Verificación visual | Inspeccioná el HTML generado (Ctrl+U) → confirmar que `{# comentarios #}` y `{% comment %}` no aparecen |
| §P2 min 170 | Ticket de salida | Nombrar 3 tags DTL usados hoy y explicar con una oración qué hace cada uno |

---

## 8. Continuidad con Semana 9

| Tema 04 introduce | Semana 9 profundiza / agrega |
|-------------------|------------------------------|
| `View` base manual | `TemplateView`, `ListView`, `DetailView` — ver qué automatizan |
| DTL completo: for, if, with, url, static, comment, include, herencia | Filtros personalizados (`templatetags/`), paginación, mensajes flash |
| `base.html` + blocks + `{{ block.super }}` | Rediseño del base con Bootstrap — layout responsive |
| `{% static %}` con CSS propio | CDN Bootstrap + archivos JS — `{% block extra_scripts %}` |
| Partials con `{% include %}` | Partials dinámicos: widget de categorías, comentarios |
| Formularios: **pendiente** | `ModelForm`, `Form`, `is_valid()`, `clean_*`, patrón PRG completo |
| Parcial 1 al inicio de Semana 9 | Cubre: ORM avanzado + View base + DTL |

---

## 9. Notas de implementación para el docente

- **Dominio BlogApp**: usar `Post`, `Category`, `Comment` como modelos presupuestos. Si el Codespace no tiene los datos cargados, correr `python manage.py loaddata blog_sample.json` (o generarlos en el shell con el Ejercicio 1 de §P1).
- **`STATICFILES_DIRS`**: verificar que está configurado en `settings.py` antes de §P2 Paso 8. Si `{% static %}` no resuelve, Django muestra la URL vacía sin error — hay que buscar en la consola.
- **`{% load static %}` obligatorio**: recordar a los estudiantes que cada template que use `{% static %}` necesita `{% load static %}`, incluso si extiende un base que ya lo cargó. Es un error frecuente.
- **`{% load %}` en child templates**: si el base hace `{% load static %}`, los child templates NO heredan ese load — deben repetirlo si usan `{% static %}` directamente.
- **`get_object_or_404`**: no confundir con `.get()` — lanza `Http404` en vez de `DoesNotExist`. Siempre usarlo en vistas de detalle públicas.
- **Formularios en Tema 05**: preparar un breve "gancho" al cierre de esta clase — "en la próxima clase vamos a hacer que el blog acepte nuevas publicaciones desde la interfaz web".
- **Parcial 1**: cubre ORM avanzado + View base + DTL completo (todo Tema 04). Preparar 2-3 ejercicios tipo sobre templates y queries.

---

> **Estado del diseño**: COMPLETE — puede avanzar a `minuta.md` cuando el docente apruebe.
> **Siguiente paso**: `/edu-new-topic` o activar `class-writer` (Dr. Roberto) para generar la minuta.
