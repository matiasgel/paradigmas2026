# Tema 05 — Vistas OOP genéricas + Templates con ORM + Formularios Django
## Módulo V completo — UNTDF IF009 2026

> **Fecha**: 2026-05-12
> **Semana del plan**: 9 (ver `salida/cursadas/2026/plan-actualizado.md` §Semana 9)
> **Estado**: DESIGN — pendiente aprobación docente
> **Prerequisito confirmado**: ORM avanzado (QuerySet API, Q objects, select_related, prefetch_related), `View` base, `as_view()`, DTL completo, templates con herencia — todo cubierto en **Tema 04**.
> **Fuentes base**: django-5.1-docs · edu_knowledge · plan-actualizado.md §9 · plan-minimo.md Módulo V

---

## 1. Metadatos

| Campo | Valor |
|-------|-------|
| Número | 05 |
| Nombre | Módulo V — Vistas OOP, Templates y Formularios con datos ORM |
| Módulos plan | V completo (vistas genéricas, templates aplicados, formularios y validación) |
| Duración total | **360 min = 6 h = 1 clase teórica + 1 clase práctica (180 min c/u)** |
| Audiencia | 3º año UNTDF Sistemas/AUS, niveles heterogéneos |
| Paradigma docente | **POO estricto: todas las vistas son class-based views. Prohibido FBV.** |
| Dominio | BlogApp — `Post`, `Category`, `Comment` (continuidad desde Tema 04) |
| Prerequisitos | Tema 04 aprobado: ORM avanzado + View base + DTL completo |

---

## 2. Cobertura del Plan Mínimo

### Módulo V — Desarrollo de interfaces de usuario utilizando el patrón MVC

| Tópico mínimo obligatorio | Cobertura | Notas |
|---------------------------|-----------|-------|
| Las vistas y templates de Django como parte del patrón MVC | §T2 | Profundización desde Tema 04 — ciclo completo MVT |
| Vistas genéricas de Django | §T2 | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| El lenguaje de templates de Django | §T3 | Aplicado con QuerySets reales — complementa DTL de Tema 04 |
| Modelado de interfaz de usuario con Django y HTML5 | §T3 | Bootstrap 5 + templates con datos ORM |
| Formularios de Django | §T4 | `ModelForm`, `clean_*`, errores, redisplay — **diferido desde Tema 04** |
| Vistas y validaciones de formularios | §T4 | `CreateView`, `UpdateView`, patrón PRG, pipeline 5 capas |

> **Cobertura Módulo V**: 100% de los tópicos del plan mínimo (clase teórica §T2–§T4).
> Sin scope creep: autenticación/permisos (`LoginRequiredMixin`) → Módulo VI.

---

## 3. Estructura de la clase — Vista general

```
CLASE TEÓRICA (180 min) ─────────────────────────────────────────────
  [0–10]   Apertura: cierre ORM → apertura Módulo V
  T2  40'  Vistas OOP genéricas con datos ORM:
           TemplateView · ListView (get_queryset) · DetailView (get_object_or_404)
           CreateView · UpdateView · DeleteView — override de métodos clave
  T3  35'  Templates aplicados con QuerySets reales:
           context_data · filtros sobre QuerySets · paginación en ListView ·
           integración Bootstrap 5 con listas y detalle · links con {% url %}
  T4  55'  **Formularios Django — ciclo de enlace y validación por capas:**
           unbound vs bound · is_bound / is_valid() · pipeline 5 capas ·
           to_python → validate → run_validators → clean_field → clean() ·
           cleaned_data · form.errors · non_field_errors ·
           ModelForm INSERT vs UPDATE (instance=) · PRG completo ·
           form_valid() / form_invalid() · redisplay con errores por campo
  [175–180] Cierre + mapa práctica

CLAUSURA: formularios de auth → Módulo VI (LoginRequiredMixin, signals)
```

> La clase práctica se planifica como artefacto separado.

---

## 4. Objetivos de aprendizaje (Bloom)

| # | Nivel Bloom | Objetivo |
|---|-------------|---------|
| 1 | **Comprender** (2) | Distinguir cuándo usar `View` base vs. vistas genéricas y el costo/beneficio de cada nivel de abstracción |
| 2 | **Aplicar** (3) | Implementar `ListView` y `DetailView` sobreescribiendo `get_queryset()` y `get_context_data()` con datos ORM reales de BlogApp |
| 3 | **Aplicar** (3) | Construir templates que consuman `object_list` y `object` del contexto, con paginación y filtros |
| 4 | **Construir** (3) | Implementar `CreateView` y `UpdateView` con `ModelForm` personalizado incluyendo validaciones `clean_*` y manejo de `instance` para distinguir INSERT de UPDATE |
| 5 | **Analizar** (4) | Trazar la pipeline completa de validación de Django (5 capas: `to_python` → `validate` → `run_validators` → `clean_<campo>` → `clean`) y ubicar cada error en su capa correspondiente |
| 6 | **Analizar** (4) | Distinguir formulario unbound vs bound y explicar por qué `cleaned_data` solo existe después de `is_valid()` |
| 7 | **Evaluar** (5) | Identificar y resolver problemas comunes: formulario inválido sin redisplay, N+1 en `ListView` sin `select_related`, `DeleteView` sin confirmación |
| 7 | **Comprender** (2) | Explicar el ciclo completo request→URLconf→View.dispatch()→handler→response y el rol del controlador en el patrón MVT |
| 8 | **Aplicar** (3) | Definir rutas con `path()`, conversores de tipo, `include()` con namespaces y generar URLs inversas con `reverse_lazy()` |
| 9 | **Reconocer** (1) | Identificar el rol de `request.session` como mecanismo de estado en HTTP stateless y su relación con cookies de sesión |

---

## 5. CLASE TEÓRICA — Vistas OOP + Templates + Formularios (180 min)

> **Punto de partida**: los estudiantes ya saben `View` base, `as_view()`, `dispatch()`, `get()`, `post()` y DTL completo (herencia, partials, filtros, `{% load static %}`). Todo eso fue Tema 04.  
> **Este tema** da el salto a vistas genéricas que hacen ORM automáticamente y formularios que validan y persisten.

### Agenda

| Tiempo | Código | Bloque |
|--------|--------|--------|
| 0–10 | — | Apertura: "el ORM ya lo dominamos — ahora lo exponemos al usuario" |
| 10–30 | T1.5 | URLconf: cómo Django rutea una request — `path()`, conversores, `include()`, namespaces |
| 30–65 | T2 | El controlador View: ciclo dispatch → HTTP handler → response + vistas genéricas OOP |
| 65–95 | T3 | Templates aplicados con QuerySets reales |
| 95–150 | **T4** | **Formularios Django: ciclo de enlace, validación por capas y CRUD** |
| 150–170 | T5 | Sesiones HTTP: estado en un protocolo stateless — `request.session` |
| 170–180 | — | Cierre + anticipo práctica |

---

### §T1.5 — URLconf: cómo Django rutea una petición HTTP (20 min)

> **Concepto central**: antes de que cualquier vista reciba una request, Django ejecuta un proceso de resolución de URLs. Entender este proceso es entender cómo el framework conecta la web con el código Python.

#### HTTP stateless y el rol del router

HTTP es un protocolo **sin estado** — cada petición es independiente. El servidor no recuerda la anterior. Django resuelve la pregunta *"¿qué código ejecuto ante esta URL?"* con el **URLconf** (URL Configuration): un módulo Python que mapea patrones de URL a clases o funciones Python.

```
Navegador            Django                    Python
──────────────────────────────────────────────────────
GET /posts/          →   URLconf               →   PostListView
GET /posts/42/       →   URLconf               →   PostDetailView  (pk=42)
POST /posts/crear/   →   URLconf               →   PostCreateView
```

#### Anatomía de `urls.py` — el despachador de rutas

Django lleva el control de URLs en dos niveles:

```
blog_project/
  urls.py        ← URLconf raíz (settings.ROOT_URLCONF)
  blog/
    urls.py      ← URLconf de la aplicación (incluido con include())
```

**URLconf raíz:**

```python
# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    # include() delega el resto del path a blog/urls.py
    # Django consume "blog/" y pasa el resto: "/posts/42/" → "posts/42/"
]
```

**URLconf de aplicación:**

```python
# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "blog"   # define el namespace para {% url 'blog:...' %}

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),         # /blog/
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # /blog/posts/42/
    path("posts/crear/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/editar/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/eliminar/", PostDeleteView.as_view(), name="post-delete"),
]
```

#### Conversores de tipo en `path()` — tipado en la URL

Django no recibe strings crudos: los conversores extraen y validan partes de la URL **antes** de que lleguen a la vista.

| Conversor | Patrón | Ejemplo | Tipo Python |
|-----------|--------|---------|-------------|
| `<int:pk>` | dígitos positivos | `/posts/42/` | `int` → `42` |
| `<str:slug>` | cualquier carácter sin `/` | `/posts/mi-titulo/` | `str` → `"mi-titulo"` |
| `<slug:slug>` | letras, números, guiones, guiones bajos | `/posts/mi-post-2026/` | `str` |
| `<uuid:pk>` | UUID estándar | `/posts/a3b2-...` | `uuid.UUID` |

```python
# El conversor garantiza que pk es int antes de llegar a la vista
path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail")

# En la vista, self.kwargs["pk"] ya es int — no hace falta int()
def get_object(self):
    return get_object_or_404(Post, pk=self.kwargs["pk"])
```

Si el usuario visita `/posts/abc/` y el conversor es `<int:pk>`, Django devuelve 404 **automáticamente** — sin código extra en la vista.

#### Resolución inversa de URLs — nunca hardcodear

Hardcodear `/blog/posts/42/` en el código es frágil: si la URL cambia, hay que buscar todos los lugares. Django provee resolución inversa:

```python
# En código Python (views.py, models.py)
from django.urls import reverse, reverse_lazy

reverse("blog:post-detail", kwargs={"pk": 42})
# → "/blog/posts/42/"

reverse_lazy("blog:post-list")
# Versión lazy: se evalúa cuando se necesita — obligatorio en atributos de clase
```

```html
<!-- En templates DTL -->
<a href="{% url 'blog:post-detail' post.pk %}">Ver post</a>
<a href="{% url 'blog:post-update' pk=post.pk %}">Editar</a>
```

**Regla académica**: nunca hardcodear URLs. Usar siempre `{% url %}` en templates y `reverse_lazy()` en vistas.

#### El proceso de resolución completo

```
  1. Browser → GET /blog/posts/42/ HTTP/1.1
  2. Django lee settings.ROOT_URLCONF = "blog_project.urls"
  3. Recorre urlpatterns en orden, busca primer match:
       path("blog/", include("blog.urls", namespace="blog")) → match
  4. Elimina "blog/", pasa "posts/42/" a blog/urls.py
  5. Recorre urlpatterns de blog:
       path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail") → match
  6. Extrae pk=42 (int), instancia PostDetailView, llama .dispatch(request, pk=42)
  7. dispatch() delega a .get(request, pk=42)
  8. Vista construye respuesta, Django envía HTTP/1.1 200 OK
```

Si ningún patrón hace match → Django levanta `Http404` automáticamente.

---

### §T2 — El controlador View: ciclo dispatch y vistas genéricas OOP (20 min)

> **Puente pedagógico**: en Tema 04 implementaron `View` manualmente — `get()` construía el contexto, llamaba al template. Las vistas genéricas automatizan exactamente eso, con más convenciones y menos código.

#### El rol del controlador en el patrón MVT de Django

Django implementa el patrón **MVT** (Model-View-Template) — una adaptación de MVC donde:

| Capa MVC | Equivalente Django | Responsabilidad |
|----------|-------------------|----------------|
| **Modelo (M)** | `models.py` + ORM | Estado y persistencia |
| **Controlador (C)** | `views.py` — clases `View` | Lógica de negocio + orquestación |
| **Vista (V)** | `templates/` — DTL | Presentación al usuario |

En Django la **Vista es el controlador**: recibe la request, consulta el modelo (ORM), construye el contexto y delega la presentación al template.

#### Ciclo de vida completo de una petición en Django

```
┌─────────────────────────────────────────────────────────────────┐
│  Browser: GET /blog/posts/42/                                   │
└──────────────────────┬──────────────────────────────────────────┘
                       │
              ┌────────▼─────────┐
              │  WSGI/ASGI Layer │  (Gunicorn, Uvicorn)
              └────────┬─────────┘
                       │
              ┌────────▼─────────────────────────────────┐
              │  Middleware Stack (en orden)              │
              │  SecurityMiddleware → SessionMiddleware   │
              │  → CommonMiddleware → CsrfViewMiddleware  │
              └────────┬─────────────────────────────────┘
                       │  request enriquecido
              ┌────────▼─────────┐
              │  URL Resolver    │  URLconf → kwargs={pk:42}
              └────────┬─────────┘
                       │
              ┌────────▼──────────────────────────┐
              │  View.as_view()(request, pk=42)   │
              │  ┌──────────────────────────────┐ │
              │  │  dispatch(request, *args)    │ │  ← método HTTP → handler
              │  │  if GET  → self.get()        │ │
              │  │  if POST → self.post()       │ │
              │  └──────────────────────────────┘ │
              └────────┬──────────────────────────┘
                       │
              ┌────────▼──────────────────────┐
              │  ORM Query (Model Layer)       │
              │  Post.objects.get(pk=42)       │
              └────────┬──────────────────────┘
                       │  objeto Python
              ┌────────▼──────────────────────┐
              │  Template Engine               │
              │  render(request, tmpl, ctx)    │
              └────────┬──────────────────────┘
                       │
              ┌────────▼──────────────────────┐
              │  HttpResponse (HTML, 200 OK)   │
              └───────────────────────────────┘
                       │
              Browser recibe la página
```

#### El objeto `request` — información de la petición HTTP

`request` es la instancia de `HttpRequest` que Django crea para cada petición. Está disponible en **todos** los métodos de la vista:

```python
class PostDetailView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        # Información de la petición
        print(request.method)          # "GET"
        print(request.path)            # "/blog/posts/42/"
        print(request.GET)             # QueryDict — parámetros de URL (?page=2)
        print(request.POST)            # QueryDict — datos de formulario (solo en POST)
        print(request.user)            # Usuario autenticado (o AnonymousUser)
        print(request.session)         # Diccionario de sesión (ver §T5)
        print(request.META["HTTP_USER_AGENT"])  # Headers HTTP
        return super().get(request, *args, **kwargs)
```

#### `dispatch()` — el despachador por método HTTP

```python
# Implementación real simplificada de View.dispatch() en Django:
class View:
    http_method_names = ["get", "post", "put", "patch", "delete", "head", "options"]

    def dispatch(self, request, *args, **kwargs):
        method = request.method.lower()
        if method in self.http_method_names:
            handler = getattr(self, method, self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
```

Esto explica por qué definir `get()` en una subclase de `View` responde solo a GET, y `post()` solo a POST. `dispatch()` es el **punto de extensión principal** del controlador.

#### Tipos de respuesta HTTP que retorna la vista

```python
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Respuesta HTML directa
return HttpResponse("<h1>Hola</h1>", content_type="text/html", status=200)

# Render: template + contexto → HttpResponse
return render(request, "blog/post_list.html", {"posts": queryset})

# Redirect: 302 hacia otra URL (patrón PRG)
return redirect("blog:post-list")
# equivalente a:
return HttpResponseRedirect(reverse("blog:post-list"))

# 404 limpio
post = get_object_or_404(Post, pk=pk)
```

#### Por qué vistas genéricas

Django incluye vistas predefinidas para los patrones más comunes. No reemplazan a `View` — lo extienden. El estudiante que entiende `View` puede leer el código fuente de cualquier vista genérica en GitHub.

```
View (base)
  └── TemplateResponseMixin + ContextMixin
        └── TemplateView          ← página estática con contexto
        └── ListView              ← lista de objetos del modelo
        └── DetailView            ← un objeto por pk/slug
              └── CreateView      ← formulario de alta
              └── UpdateView      ← formulario de edición
              └── DeleteView      ← confirmación de eliminación
```

Django incluye vistas predefinidas para los patrones más comunes. No reemplazan a `View` — lo extienden. El estudiante que entiende `View` puede leer el código fuente de cualquier vista genérica en GitHub.

```
View (base)
  └── TemplateResponseMixin + ContextMixin
        └── TemplateView          ← página estática con contexto
        └── ListView              ← lista de objetos del modelo
        └── DetailView            ← un objeto por pk/slug
              └── CreateView      ← formulario de alta
              └── UpdateView      ← formulario de edición
              └── DeleteView      ← confirmación de eliminación
```

#### `TemplateView` — la más simple

```python
# views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["total_posts"] = Post.objects.filter(published=True).count()
        return ctx
```

`get_context_data()` es el mecanismo universal para pasar datos a templates en **todas** las vistas genéricas. Siempre llamar `super()` primero.

#### `ListView` — listas con ORM automático

```python
# views.py
from django.views.generic import ListView

class PostListView(ListView):
    model = Post                          # hace Post.objects.all() por defecto
    template_name = "blog/post_list.html"
    context_object_name = "posts"         # nombre en el template (default: object_list)
    paginate_by = 10                      # paginación automática

    def get_queryset(self):
        """Sobreescribir para filtrar — aquí conectamos con el ORM avanzado de Tema 04."""
        return Post.objects.filter(published=True)\
                           .select_related("author", "category")\
                           .order_by("-created_at")
```

**Conexión explícita con ORM (Tema 04)**: `get_queryset()` retorna el mismo `QuerySet` que construimos en la práctica anterior. La vista genérica sabe cuándo evaluarlo.

**Paginación automática**: cuando `paginate_by` está definido, el template recibe `page_obj` con métodos `has_previous()`, `has_next()`, `previous_page_number()`, `next_page_number()`.

```html
<!-- blog/post_list.html -->
{% for post in posts %}
  <div class="card mb-3">
    <div class="card-body">
      <h5 class="card-title">{{ post.title }}</h5>
      <p class="card-text">{{ post.body|truncatewords:30 }}</p>
      <a href="{% url 'blog:post-detail' post.pk %}" class="btn btn-primary">Leer más</a>
    </div>
  </div>
{% empty %}
  <p>No hay posts publicados aún.</p>
{% endfor %}

<!-- Paginación Bootstrap -->
{% if page_obj.has_other_pages %}
  <nav>
    <ul class="pagination">
      {% if page_obj.has_previous %}
        <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">«</a></li>
      {% endif %}
      <li class="page-item active"><span class="page-link">{{ page_obj.number }}</span></li>
      {% if page_obj.has_next %}
        <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">»</a></li>
      {% endif %}
    </ul>
  </nav>
{% endif %}
```

#### `DetailView` — un objeto con relaciones ORM

```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        """Cargar relaciones en una sola query — select_related desde Tema 04."""
        return Post.objects.select_related("author", "category")\
                           .prefetch_related("comments")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Agregar QuerySet adicional — datos ORM combinados
        ctx["related_posts"] = Post.objects.filter(
            category=self.object.category,
            published=True
        ).exclude(pk=self.object.pk)[:3]
        return ctx
```

`self.object` dentro de `get_context_data()` siempre está disponible y es el objeto ya recuperado de la BD.

#### `CreateView`, `UpdateView`, `DeleteView` — anticipación para §T4

```python
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm        # ModelForm personalizado — ver §T4
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post-list")

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post-list")

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post-list")
```

**URLs — namespace blog:**

```python
# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("crear/", PostCreateView.as_view(), name="post-create"),
    path("<int:pk>/editar/", PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/eliminar/", PostDeleteView.as_view(), name="post-delete"),
]
```

---

### §T3 — Templates con QuerySets reales: context y filtros aplicados (35 min)

> **Puente pedagógico**: en Tema 04 aprendieron todos los tags y filtros del DTL. Aquí los aplicamos sobre objetos de modelos reales — no strings fijos.

#### Contexto automático de las vistas genéricas

| Vista | Variables de contexto automáticas |
|-------|-----------------------------------|
| `ListView` | `object_list`, `page_obj`, `paginator`, `is_paginated` |
| `DetailView` | `object` (+ alias con `context_object_name`) |
| `CreateView` / `UpdateView` | `form` |
| `DeleteView` | `object` |

Si se define `context_object_name`, existe **tanto** el alias como `object`. Siempre usar el alias.

#### Filtros sobre atributos de modelos

```html
<!-- Acceso a campos del modelo -->
{{ post.title|upper }}
{{ post.created_at|date:"d/m/Y" }}
{{ post.body|truncatewords:50|linebreaks }}
{{ post.author.get_full_name|default:"Anónimo" }}

<!-- Relaciones: dot notation accede a FK y M2M -->
{{ post.category.name }}
{% for comment in post.comments.all %}
  <p>{{ comment.author.username }}: {{ comment.body }}</p>
{% endfor %}
```

**Nota de performance**: `post.comments.all` en un template evalúa la query si no se usó `prefetch_related`. Siempre resolver en `get_queryset()` de la vista.

#### Template base + extensión con datos ORM

```html
<!-- templates/blog/base.html -->
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}BlogApp{% endblock %}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="{% url 'blog:post-list' %}">BlogApp</a>
      <div class="navbar-nav ms-auto">
        <a class="nav-link {% if request.resolver_match.url_name == 'post-list' %}active{% endif %}"
           href="{% url 'blog:post-list' %}">Posts</a>
        <a class="nav-link" href="{% url 'blog:post-create' %}">Nuevo Post</a>
      </div>
    </div>
  </nav>
  <div class="container mt-4">
    {% if messages %}
      {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
      {% endfor %}
    {% endif %}
    {% block content %}{% endblock %}
  </div>
</body>
</html>
```

#### Detalle con relaciones y datos ORM combinados

```html
<!-- templates/blog/post_detail.html -->
{% extends "blog/base.html" %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
<article class="mb-5">
  <header class="mb-4">
    <h1>{{ post.title }}</h1>
    <p class="text-muted">
      Por {{ post.author.get_full_name }} en
      <span class="badge bg-secondary">{{ post.category.name }}</span>
      &mdash; {{ post.created_at|date:"d \d\e F \d\e Y" }}
    </p>
    <a href="{% url 'blog:post-update' post.pk %}" class="btn btn-sm btn-outline-secondary">Editar</a>
    <a href="{% url 'blog:post-delete' post.pk %}" class="btn btn-sm btn-outline-danger">Eliminar</a>
  </header>
  <div class="mb-4">{{ post.body|linebreaks }}</div>
</article>

<!-- Posts relacionados — QuerySet adicional desde get_context_data -->
{% if related_posts %}
<section>
  <h4>Posts relacionados en {{ post.category.name }}</h4>
  <div class="row">
    {% for related in related_posts %}
    <div class="col-md-4">
      <div class="card">
        <div class="card-body">
          <h6 class="card-title">
            <a href="{% url 'blog:post-detail' related.pk %}">{{ related.title }}</a>
          </h6>
          <small class="text-muted">{{ related.created_at|date:"d/m/Y" }}</small>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</section>
{% endif %}
{% endblock %}
```

---

### §T4 — Formularios Django: ciclo de enlace, validación por capas y CRUD (55 min)

> **Eje central del Módulo V**: los formularios son el mecanismo que cierra el ciclo MVC — conectan la entrada del usuario (HTTP POST) con el modelo (ORM) y la persistencia. Entender el **ciclo de enlace** es entender cómo Django sabe si un formulario tiene datos, si son válidos, y qué hacer con ellos.

---

#### El ciclo de enlace (binding cycle) — el concepto fundamental

Un formulario en Django tiene dos estados posibles:

```
FORMULARIO NO ENLAZADO (unbound)          FORMULARIO ENLAZADO (bound)
─────────────────────────────────         ─────────────────────────────────
PostForm()                                PostForm(data=request.POST)
PostForm(instance=post)                   PostForm(data=request.POST, instance=post)

- No tiene datos del usuario              - Tiene datos del usuario (request.POST)
- is_bound → False                        - is_bound → True
- is_valid() siempre False                - is_valid() ejecuta la pipeline completa
- Se renderiza vacío (o con instancia)    - Se renderiza con datos + errores si falla
- Uso: GET /crear/ o GET /editar/42/      - Uso: POST /crear/ o POST /editar/42/
```

**Regla de oro**: un formulario solo puede ser validado si está enlazado. `is_valid()` sobre un unbound form es siempre `False` sin ejecutar nada.

```python
# Demostración del estado de enlace
f1 = PostForm()                         # unbound
print(f1.is_bound)   # False
print(f1.is_valid()) # False — sin ejecutar ninguna lógica

f2 = PostForm(data={"title": "Hola"})  # bound
print(f2.is_bound)   # True
print(f2.is_valid()) # False — ejecuta validación, title es muy corto
print(f2.errors)     # {"title": ["El título debe tener al menos 10 caracteres."]}

f3 = PostForm(data={"title": "Post válido de prueba", "body": "...", ...})
print(f3.is_valid()) # True
print(f3.cleaned_data["title"])  # "Post válido de prueba"
```

---

#### Pipeline de validación — las 5 capas en secuencia

Cuando se llama a `form.is_valid()`, Django ejecuta la siguiente secuencia estricta. Si **cualquier capa** falla, el proceso se detiene y `is_valid()` devuelve `False`.

```
┌─────────────────────────────────────────────────────────────────────┐
│  form.is_valid()  →  form.full_clean()  →  ...                     │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
          ┌─────────────────▼──────────────────────────────────┐
          │  CAPA 1: field.to_python(value)                    │
          │  Convierte el string HTTP a tipo Python             │
          │  "42"  →  int(42)    "2026-05-12"  →  date(...)    │
          │  Si falla: ValidationError → campo marcado inválido │
          └─────────────────┬──────────────────────────────────┘
                            │  valor Python
          ┌─────────────────▼──────────────────────────────────┐
          │  CAPA 2: field.validate(value)                     │
          │  Validaciones built-in del campo:                   │
          │  required, max_length, min_length, max_value,       │
          │  EmailField.validate(), URLField.validate(), etc.   │
          └─────────────────┬──────────────────────────────────┘
                            │  valor validado
          ┌─────────────────▼──────────────────────────────────┐
          │  CAPA 3: field.run_validators(value)               │
          │  Validators registrados en el campo:               │
          │  validators=[MinLengthValidator(10), ...]           │
          └─────────────────┬──────────────────────────────────┘
                            │  valor limpio → cleaned_data[campo]
          ┌─────────────────▼──────────────────────────────────┐
          │  CAPA 4: self.clean_<fieldname>()                  │
          │  Validación personalizada por campo                 │
          │  Accede a self.cleaned_data["campo"]                │
          │  Puede consultar el ORM, comparar con otros campos  │
          │  Debe retornar el valor (posiblemente transformado) │
          └─────────────────┬──────────────────────────────────┘
                            │  todos los campos limpios
          ┌─────────────────▼──────────────────────────────────┐
          │  CAPA 5: self.clean()                              │
          │  Validación cruzada entre campos                    │
          │  self.cleaned_data tiene TODOS los campos válidos   │
          │  (los inválidos en capas anteriores no están aquí) │
          │  Errores aquí van a form.non_field_errors           │
          └─────────────────┬──────────────────────────────────┘
                            │
                    ┌───────┴───────┐
                  válido         inválido
                    │               │
           cleaned_data        form.errors
           completo            (dict campo→lista errores)
           is_valid()=True     is_valid()=False
```

**Punto clave**: `cleaned_data` solo existe después de llamar a `is_valid()`. Acceder antes → `AttributeError`.

---

#### `ModelForm` — formulario enlazado al modelo ORM

`ModelForm` agrega una **capa extra** después de la Capa 5: validaciones a nivel del modelo (`Model.full_clean()`), que incluyen restricciones de la BD (`unique`, `unique_together`).

```python
# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "category", "published"]
        widgets = {
            "title":     forms.TextInput(attrs={"class": "form-control"}),
            "body":      forms.Textarea(attrs={"class": "form-control", "rows": 8}),
            "category":  forms.Select(attrs={"class": "form-select"}),
            "published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "title":     "Título",
            "body":      "Contenido",
            "category":  "Categoría",
            "published": "Publicar inmediatamente",
        }
        error_messages = {
            "title": {
                "required": "El título es obligatorio.",
                "max_length": "El título no puede superar los %(limit_value)s caracteres.",
            }
        }
```

**Cómo `ModelForm` genera los campos automáticamente:**

| Campo del modelo | Campo de formulario generado |
|-----------------|------------------------------|
| `CharField(max_length=200)` | `CharField(max_length=200, widget=TextInput)` |
| `TextField()` | `CharField(widget=Textarea)` |
| `BooleanField()` | `BooleanField(widget=CheckboxInput)` |
| `ForeignKey(Category)` | `ModelChoiceField(queryset=Category.objects.all())` |
| `DateTimeField(auto_now_add=True)` | **excluido** — `auto_now_add` no es editable |

---

#### Validaciones personalizadas — Capas 4 y 5 en detalle

```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "category", "published"]

    # ── CAPA 4: clean_<campo>() ──────────────────────────────────────────────
    def clean_title(self):
        """
        Recibe self.cleaned_data["title"] ya convertido y validado por capas 1-3.
        Debe retornar el valor (puede transformarlo: .strip(), .lower(), etc.).
        Si lanza ValidationError → el error va a form.errors["title"].
        """
        title = self.cleaned_data["title"].strip()  # limpiar espacios

        if len(title) < 10:
            raise forms.ValidationError(
                "El título debe tener al menos %(min)s caracteres.",
                code="too_short",
                params={"min": 10},
            )

        # Consulta ORM — verificar unicidad excluyendo la instancia actual (edición)
        qs = Post.objects.filter(title__iexact=title)
        if self.instance.pk:          # UpdateView: excluir el post actual
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un post con ese título.")

        return title  # OBLIGATORIO retornar el valor (posiblemente transformado)

    def clean_body(self):
        """Ejemplo: strip HTML simple."""
        body = self.cleaned_data["body"].strip()
        if not body:
            raise forms.ValidationError("El contenido no puede estar vacío.")
        return body

    # ── CAPA 5: clean() ─────────────────────────────────────────────────────
    def clean(self):
        """
        self.cleaned_data contiene SOLO los campos que pasaron capas 1-4.
        Si title falló, cleaned_data.get("title") devuelve None.
        Usar .get() siempre, nunca acceso directo con [].
        Los errores aquí van a form.non_field_errors() — no a un campo específico.
        """
        cleaned = super().clean()
        body = cleaned.get("body", "")
        published = cleaned.get("published", False)

        if published and len(body) < 100:
            # Asociar el error a un campo específico desde clean():
            self.add_error("body",
                "Para publicar, el contenido debe tener al menos 100 caracteres.")

        return cleaned
```

---

#### Ciclo completo en `CreateView` — de GET a POST a Redirect

```
══════════════════════════════════════════════════════════════════════
  PETICIÓN GET /blog/posts/crear/
══════════════════════════════════════════════════════════════════════
  1. CreateView.get(request)
  2. form = PostForm()                      ← UNBOUND (sin datos)
  3. ctx = {"form": form}
  4. return render(request, "post_form.html", ctx)
  5. Template renderiza campos vacíos — sin errores

══════════════════════════════════════════════════════════════════════
  PETICIÓN POST /blog/posts/crear/ (datos inválidos)
══════════════════════════════════════════════════════════════════════
  1. CreateView.post(request)
  2. form = PostForm(data=request.POST)     ← BOUND
  3. form.is_valid()  →  False
     └── pipeline ejecutada: capas 1-5
     └── form.errors = {"title": ["Ya existe un post con ese título."]}
  4. form_invalid(form) llamado
  5. ctx = {"form": form}                   ← mismo form con errores
  6. return render(request, "post_form.html", ctx)  ← 200 (NO redirect)
  7. Template renderiza campos CON valores + errores marcados

══════════════════════════════════════════════════════════════════════
  PETICIÓN POST /blog/posts/crear/ (datos válidos)
══════════════════════════════════════════════════════════════════════
  1. CreateView.post(request)
  2. form = PostForm(data=request.POST)     ← BOUND
  3. form.is_valid()  →  True
     └── form.cleaned_data = {"title": "Mi post válido", "body": "...", ...}
  4. form_valid(form) llamado
  5. form.instance.author = request.user   ← asignar antes de save()
  6. form.save()                            ← INSERT en BD (nuevo objeto)
  7. return redirect(success_url)           ← 302 a /blog/
══════════════════════════════════════════════════════════════════════

  ¿Por qué redirect y no render?  →  Patrón PRG (Post-Redirect-Get):
  Si el usuario recarga la página tras un POST exitoso, el navegador
  re-enviaría el formulario → inserción duplicada en la BD.
  El redirect convierte el POST en un GET seguro e idempotente.
```

#### Ciclo en `UpdateView` — formulario pre-enlazado a instancia

```python
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post-list")

    def form_valid(self, form):
        # form.instance ya es el Post existente con pk —
        # form.save() emite UPDATE, no INSERT
        return super().form_valid(form)
```

```
  GET /blog/posts/42/editar/
  ─────────────────────────────────────────────────────────────────
  1. UpdateView recupera Post(pk=42) del ORM → self.object
  2. form = PostForm(instance=self.object)  ← UNBOUND pero pre-poblado
     └── Django inicializa cada campo con el valor del atributo del modelo
     └── form["title"].value() == "Post existente"
  3. Template renderiza campos CON los valores actuales del objeto

  POST /blog/posts/42/editar/ (datos modificados)
  ─────────────────────────────────────────────────────────────────
  1. form = PostForm(data=request.POST, instance=self.object)  ← BOUND + instancia
  2. form.is_valid()  →  True
  3. form.save()  →  UPDATE blog_post SET title=... WHERE id=42
  4. redirect a success_url
```

**Diferencia clave**: pasar `instance=` hace que `.save()` emita `UPDATE` en lugar de `INSERT`. Sin `instance`, siempre crea un objeto nuevo.

---

#### `ModelForm` — la conexión entre formulario y modelo ORM

```python
# blog/forms.py
from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "category", "published"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título del post"}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 8}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "title": "Título",
            "body": "Contenido",
            "category": "Categoría",
            "published": "Publicar inmediatamente",
        }
```

**Por qué `ModelForm` y no `Form`:**
- Los campos se generan **automáticamente** desde el modelo — no hay duplicación de definiciones
- `.save()` persiste el objeto directamente a la BD
- Las validaciones del modelo (`max_length`, `blank`, `unique`) se aplican automáticamente

#### Template de formulario — redisplay ante errores

```html
<!-- templates/blog/post_form.html -->
{% extends "blog/base.html" %}

{% block title %}{% if object %}Editar{% else %}Nuevo{% endif %} Post{% endblock %}

{% block content %}
<div class="row justify-content-center">
  <div class="col-md-8">
    <h2>{% if object %}Editar Post{% else %}Nuevo Post{% endif %}</h2>
    <form method="post" novalidate>
      {% csrf_token %}

      {# Errores de validación cruzada (clean()) — no asociados a ningún campo #}
      {% if form.non_field_errors %}
        <div class="alert alert-danger">
          {% for error in form.non_field_errors %}<p>{{ error }}</p>{% endfor %}
        </div>
      {% endif %}

      {% for field in form %}
        <div class="mb-3">
          <label for="{{ field.id_for_label }}" class="form-label fw-semibold">
            {{ field.label }}{% if field.field.required %} *{% endif %}
          </label>
          {{ field }}
          {# Errores de este campo específico — generados por clean_<campo>() #}
          {% if field.errors %}
            <div class="text-danger small mt-1">
              {% for error in field.errors %}{{ error }}{% endfor %}
            </div>
          {% endif %}
        </div>
      {% endfor %}

      <div class="d-flex gap-2">
        <button type="submit" class="btn btn-primary">Guardar</button>
        <a href="{% url 'blog:post-list' %}" class="btn btn-secondary">Cancelar</a>
      </div>
    </form>
  </div>
</div>
{% endblock %}
```

**Por qué `novalidate`**: sin este atributo, el browser ejecuta su propia validación HTML5 y puede bloquear el envío *antes* de que Django procese el formulario. Con `novalidate`, la validación la hace Django — más control, mensajes en español.

#### `DeleteView` — confirmación obligatoria

```python
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post-list")
```

```html
<!-- templates/blog/post_confirm_delete.html -->
{% extends "blog/base.html" %}
{% block content %}
<div class="alert alert-warning">
  <h4>¿Eliminar "{{ object.title }}"?</h4>
  <p>Esta acción no se puede deshacer.</p>
  <form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Sí, eliminar</button>
    <a href="{% url 'blog:post-list' %}" class="btn btn-secondary">Cancelar</a>
  </form>
</div>
{% endblock %}
```

**`DeleteView` solo responde a POST para borrar** — un GET siempre muestra el template de confirmación.

---

### §T5 — Sesiones HTTP: estado persistente en un protocolo sin estado (8 min)

> **Concepto motivador**: hasta aquí cada petición HTTP es completamente independiente. El servidor no sabe si el mismo navegador hizo la petición anterior. Sin embargo, las aplicaciones web necesitan recordar cosas entre peticiones — ¿cómo?

#### HTTP es stateless — el problema fundamental

HTTP/1.1 no guarda estado entre peticiones. Cada `GET /blog/posts/` es, para el servidor, como si llegara de un desconocido. Esto es un diseño intencional que hace la web escalable, pero genera el problema: **¿cómo le preguntamos al servidor si el usuario ya inició sesión?**

La solución general son las **sesiones**: un mecanismo para asociar un identificador de sesión a una petición y almacenar datos asociados a ese identificador en el servidor.

#### Anatomía de una sesión HTTP

```
1ª petición:                             2ª petición (mismo usuario):
GET /blog/                               GET /blog/posts/crear/
Headers: (sin cookies)                   Headers: Cookie: sessionid=abc123xyz

                  ↓                                       ↓
        Django crea sesión nueva                Django busca sesión abc123xyz
        session_key = "abc123xyz"               en la base de datos/cache
        Guarda: {} en DB                        Recupera: {"last_page": "/blog/"}
        Set-Cookie: sessionid=abc123xyz

        ─────────────────────────────────────────────────────────
        Navegador guarda la cookie. La envía en TODAS las peticiones siguientes.
        ─────────────────────────────────────────────────────────
```

**La cookie solo contiene el identificador** (`sessionid`). Los datos reales viven en el servidor (BD, caché, archivo). Esto es más seguro que cookies con datos completos.

#### `request.session` — el diccionario de sesión en Django

El middleware `SessionMiddleware` (activo por defecto en `settings.py`) adjunta un diccionario `session` a cada `request`:

```python
# blog/views.py
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get(self, request, *args, **kwargs):
        # Leer de la sesión
        last_filter = request.session.get("last_category_filter", None)

        # Escribir en la sesión
        request.session["last_page_visited"] = request.path
        request.session["visit_count"] = request.session.get("visit_count", 0) + 1

        # session es un dict Python — cualquier valor serializable a JSON
        return super().get(request, *args, **kwargs)
```

```python
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        # Guardar un mensaje de éxito en sesión (messages framework usa esto internamente)
        self.request.session["last_created_post_id"] = self.object.pk
        return response
```

#### Backends de sesión disponibles en Django

| Backend | Dónde se guardan los datos | Cuándo usar |
|---------|---------------------------|-------------|
| `db` (default) | Tabla `django_session` en BD | Desarrollo y producción general |
| `cache` | Redis, Memcached | Alta frecuencia de lectura |
| `file` | Sistema de archivos | Desarrollo local sin BD |
| `cookie` | En la cookie misma (firmada) | Solo datos mínimos no sensibles |

Configuración en `settings.py`:
```python
SESSION_ENGINE = "django.contrib.sessions.backends.db"  # default
SESSION_COOKIE_AGE = 1209600    # 2 semanas en segundos
SESSION_COOKIE_SECURE = True    # Solo HTTPS (producción)
SESSION_COOKIE_HTTPONLY = True  # No accesible desde JavaScript
```

#### Messages framework — sesiones para el usuario final

Django incluye `django.contrib.messages`, construido sobre sesiones, para enviar mensajes temporales al usuario (notificaciones de éxito, error, advertencia):

```python
from django.contrib import messages

class PostCreateView(CreateView):
    def form_valid(self, form):
        messages.success(self.request, f"Post '{form.instance.title}' creado exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hay errores en el formulario. Revisá los campos marcados.")
        return super().form_invalid(form)
```

En el template base (ya incluido en §T3):
```html
{% if messages %}
  {% for message in messages %}
    <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
      {{ message }}
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
  {% endfor %}
{% endif %}
```

El mensaje se guarda en la sesión, se muestra **una vez** en el siguiente render, y se elimina automáticamente. Exactamente el mecanismo del patrón PRG: POST → redirect → GET muestra el mensaje.

#### Alcance de esta clase vs. Módulo VI

| Concepto | Este tema (05) | Módulo VI (Semana 12) |
|----------|---------------|-----------------------|
| `request.session` como dict | ✅ Introducido | — |
| Messages framework | ✅ Usado en formularios | — |
| Sesión en URLs genéricas | ✅ `form_valid` / `form_invalid` | — |
| Login / logout con sesión | ❌ Out of scope | ✅ `django.contrib.auth` |
| `request.user` y autenticación | Mencionado como `AnonymousUser` | ✅ Implementación completa |
| `LoginRequiredMixin` | ❌ Out of scope | ✅ Permisos en vistas |

---

## 6. Scope explícito

### Dentro del alcance (IN)

| Elemento | Justificación |
|----------|---------------|
| URLconf: `path()`, conversores `<int:pk>`, `<slug:slug>` | Base de todo el ruteo — sin esto no hay vista accesible |
| `include()` con `app_name` / `namespace` | Estructura de URLs escalable — necesario para `{% url 'blog:...' %}` |
| `reverse_lazy()` y `{% url %}` en templates | Principio de URL indirecta — nunca hardcodear |
| Ciclo completo request → dispatch() → ORM → template → response | Marco conceptual del controlador — el mapa mental fundamental |
| Objeto `request`: `.method`, `.GET`, `.POST`, `.user`, `.session`, `.path` | Fuente de toda información de la petición en la vista |
| `TemplateView`, `ListView`, `DetailView` | Tríada básica — todo proyecto Django las usa |
| `CreateView`, `UpdateView`, `DeleteView` | CRUD completo — Create, Update, Delete con CBV |
| `get_queryset()`, `get_context_data()`, `form_valid()` | Puntos de extensión fundamentales |
| `ModelForm` con `fields`, `widgets`, `labels` | Formulario principal del stack |
| `clean_field()` y `clean()` | Validación a nivel campo y cruzada |
| Paginación automática en `ListView` | Requisito práctico de toda lista real |
| `{% url %}` con namespaces, `{% csrf_token %}` | Requisito de seguridad y navegación |
| Bootstrap 5 + templates con datos ORM | Interfaz visible — motiva la entrega del TP |
| `request.session` como dict — lectura y escritura básica | Fundamento de estado HTTP — intro sin autenticación |
| Messages framework (`messages.success`, `messages.error`) | Patrón PRG completo — feedback al usuario post-formulario |

### Fuera del alcance (OUT) — con destino explícito

| Elemento | Destino |
|----------|---------|
| `LoginRequiredMixin`, `PermissionRequiredMixin` | Módulo VI (Semana 12) |
| `UserCreationForm`, `AuthenticationForm` | Módulo VI (Semana 12) |
| `FormView` puro sin modelo | Fuera del stack — no se usa en BlogApp |
| AJAX / `fetch` con JSON | Módulo VII (REST API) |
| `django-crispy-forms` | Fuera del scope de la cursada |
| Tests de vistas genéricas | Se mencionan pero el taller es en Semana 10 |

---

## 7. Errores frecuentes anticipados (FAQ pedagógico)

| Error | Causa | Solución |
|-------|-------|---------|
| Template no encontrado | `template_name` mal definido o no está en `TEMPLATES[0]['DIRS']` | Verificar `APP_DIRS = True` en settings y que el template está en `{app}/templates/{app}/` |
| `NoReverseMatch` en `{% url %}` | Falta `app_name` en `urls.py` o nombre de URL incorrecto | Agregar `app_name = "blog"` y usar `blog:nombre-url` |
| `NoReverseMatch: Reverse for '...' not found` | Se usa `reverse()` en atributo de clase (evaluado en import time) | Reemplazar `reverse(...)` por `reverse_lazy(...)` |
| URL captura el patrón equivocado | Orden incorrecto en `urlpatterns` — `path("")` antes de `path("<int:pk>/")` | Los patrones más específicos deben ir primero; Django toma el primer match |
| `TypeError` en vista con `<int:pk>` pero valor no numérico en URL | El conversor rechaza el valor — Django lanza 404 | Correcto — el conversor valida; no hace falta validar `pk` manualmente |
| Formulario no muestra errores | Falta `novalidate` en `<form>` → el browser bloquea antes del servidor | Agregar `novalidate` para que Django procese las validaciones |
| N+1 en template | `post.comments.all` evaluado en el template sin `prefetch_related` | Mover a `get_queryset()` con `.prefetch_related("comments")` |
| `DeleteView` borra en GET | Template no tiene el `<form method="post">` — botón de "eliminar" hace GET | El template de confirmación DEBE tener un form POST |
| Sesión no persiste entre peticiones | `SessionMiddleware` no está en `MIDDLEWARE` o `django.contrib.sessions` no en `INSTALLED_APPS` | Verificar ambos en `settings.py` |
| Messages no aparecen en el template | `{% if messages %}` en template que no extiende el base | Agregar el bloque de messages en el template base y extenderlo |

---

## 8. Artefactos a producir

| Artefacto | Agente | Estado |
|-----------|--------|--------|
| `diseno.md` | Marcos (topic-designer) | ✅ Este documento |
| `minuta.md` | Roberto (class-writer) | ⏳ Pendiente aprobación del diseño |
| `filminas.md` | Roberto (class-writer) | ⏳ Pendiente aprobación del diseño |
| `guia-estudio.md` | Sofía (study-guide-writer) | ⏳ Pendiente minuta |

---

> **Aprobación requerida**: confirmar este diseño con `/edu-approve-design` o indicar ajustes antes de proceder con `minuta.md`.
