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
| Módulos plan | IV avanzado (ORM completo) + V intro (View base + formularios) |
| Duración total | **360 min = 6 h = 1 clase teórica + 1 clase práctica (180 min c/u)** |
| Audiencia | 3º año UNTDF Sistemas/AUS, niveles heterogéneos |
| Paradigma docente | **POO estricto: todas las vistas son class-based views. Prohibido FBV.** |
| Dominio | BlogApp — `Post`, `Category`, `Comment` (unificador semanas 8 y 9) |
| TP asociado | TP-5 (por definir) — alcance: modelos + admin + ORM avanzado + primeras vistas `View` + `ModelForm` básico |
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
| Formularios de Django | Clase Teórica §T5 + Clase Práctica §P3 |
| Vistas y validaciones de formularios | Clase Práctica §P3 (intro — se profundiza en Semana 9) |

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
  T4  30'  Django Template Language (DTL): variables · filtros · tags · herencia extends/block · include
  T5  15'  Formularios: HTML <form> · CSRF · Form vs ModelForm · is_valid() · PRG
  ──  25'  Breaks + apertura + cierre

CLASE PRÁCTICA (180 min) ────────────────────────────────────────────
  P1  60'  BlogApp Codespaces: shell + managers/QuerySets sobre Post, Category, Comment
  P2  60'  Primera vista OOP: View base → URL → contexto → template con herencia
  P3  60'  Primer ModelForm: alta/edición BlogApp · validación básica · flujo GET/POST manual
```

---

## 4. CLASE TEÓRICA — ORM avanzado + puente a interfaz MVC (180 min)

### Objetivos (Bloom)

1. **Analizar** (4) el ciclo de vida de un `QuerySet`: lazy evaluation, caché, y cuándo se evalúa.
2. **Aplicar** (3) chaining de métodos sobre `QuerySet` para filtrar, excluir, ordenar y obtener resultados.
3. **Construir** (4) consultas complejas usando `Q objects`, `F expressions`, `annotate()` y `aggregate()`.
4. **Evaluar** (5) el costo de N+1 queries e implementar `select_related` / `prefetch_related` como solución.
5. **Comprender** (2) el ciclo request/response de Django y la responsabilidad de cada capa MVT.
6. **Reconocer** (2) `View` como clase base, `as_view()`, `dispatch()`, y los métodos `get()` / `post()`.
7. **Distinguir** (2) `Form` de `ModelForm` y el patrón POST/Redirect/GET como buena práctica.

### Agenda

| Tiempo | Código | Bloque |
|--------|--------|--------|
| 0–10 | — | Apertura: contextualización — "ya saben ORM básico, hoy lo usamos como profesionales" |
| 10–55 | T1 | QuerySet API avanzado |
| 55–95 | T2 | Consultas dinámicas y performance |
| 95–100 | — | **Break** |
| 100–125 | T3 | Puente MVC + Class-Based Views con `View` base |
| 125–155 | T4 | **Django Template Language (DTL)** |
| 155–170 | T5 | Introducción a formularios |
| 170–180 | — | Cierre + mapa de la práctica + preview Semana 9 |

---

### §T1 — QuerySet API avanzado (45 min)

> **Punto de partida explícito**: los estudiantes ya saben crear modelos, correr migraciones y hacer CRUD básico en el shell. Esta sección profundiza la API.

#### QuerySet como API de consulta orientada a objetos

- Un `QuerySet` es un objeto Python que representa una consulta diferida a la BD.
- **Lazy evaluation**: la consulta SQL **no se ejecuta** hasta que se consume el QuerySet (iteración, slicing, `list()`, `bool()`, `len()`).
- **Caché**: el resultado se almacena al evaluar; una segunda iteración **no vuelve a la BD**.

```python
# Solo se construye el QuerySet — no va a la BD todavía
qs = Post.objects.filter(published=True).order_by("-created_at")

# Aquí sí evalúa (iteración en template o explícita)
for post in qs:
    print(post.title)
```

#### Chaining: operaciones encadenables

Todos los métodos que devuelven `QuerySet` son encadenables:

```python
Post.objects.filter(published=True)\
            .exclude(author__is_staff=True)\
            .order_by("-created_at")\
            .values("title", "author__username")[:10]
```

#### Métodos de recuperación (devuelven instancia, no QuerySet)

| Método | Resultado | Excepción si falla |
|--------|-----------|-------------------|
| `.get(pk=1)` | una instancia | `DoesNotExist` / `MultipleObjectsReturned` |
| `.first()` / `.last()` | instancia o `None` | — |
| `.get_or_create(...)` | `(obj, created)` | — |
| `.update_or_create(...)` | `(obj, created)` | — |

#### Escritura masiva

```python
# create() devuelve la instancia guardada
post = Post.objects.create(title="Nuevo", author=user, published=False)

# update() devuelve cantidad de filas afectadas — NO llama a save()
Post.objects.filter(author=user).update(published=True)

# delete() devuelve (n, dict) con conteo por tipo
Post.objects.filter(published=False, created_at__lt=cutoff).delete()

# bulk_create — inserts masivos sin save() individual
Post.objects.bulk_create([Post(title=t) for t in titles])
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

### §T4 — Django Template Language (DTL) (30 min)

> **Fuente**: Django 6.0 Official Docs — *The Django template language* (`docs.djangoproject.com/en/6.0/ref/templates/language/`)  
> **Objetivo**: que los estudiantes lean y escriban templates de forma autónoma — esencial para las vistas de BlogApp.

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

#### Tags de control de flujo

**`{% for %}`** — iteración sobre cualquier iterable del contexto:

```html
{% for post in posts %}
    <article>
        <h2>{{ post.title }}</h2>
        <p>{{ post.body|truncatewords:50 }}</p>
    </article>
{% empty %}
    <p>No hay posts publicados todavía.</p>
{% endfor %}
```

Variables mágicas dentro de `for`: `{{ forloop.counter }}`, `{{ forloop.first }}`, `{{ forloop.last }}`.

**`{% if %}`** — condicionales completos:

```html
{% if posts|length > 1 %}
    <p>Mostrando {{ posts|length }} publicaciones.</p>
{% elif posts|length == 1 %}
    <p>Una sola publicación.</p>
{% else %}
    <p>Sin publicaciones.</p>
{% endif %}
```

**`{% url %}`** — resolución de URLs por nombre (never hardcode URLs):

```html
<a href="{% url 'blog:post-detail' pk=post.pk %}">Leer más</a>
<a href="{% url 'blog:post-list' %}">Volver al listado</a>
```

**`{% csrf_token %}`** — token anti-CSRF obligatorio en formularios POST:

```html
<form method="post">
    {% csrf_token %}
    ...
</form>
```

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
3. `{{ block.super }}` permite incluir el contenido del bloque padre + agregar contenido propio.
4. Cuantos más bloques, más flexible — pero no agregar bloques que nunca se sobreescriben.

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

**Filminas previstas §T4 (DTL): ~10**

---

### §T5 — Introducción a formularios (15 min)

> **Objetivo**: primer contacto conceptual — los detalles se profundizan en Semana 9.

#### HTML `<form>` y Django

```html
<form method="post" action="{% url 'blog:post-create' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
</form>
```

- **`{% csrf_token %}`**: token de seguridad anti-CSRF obligatorio en **todo** formulario POST. Django lo verifica automáticamente — sin él, `403 Forbidden`.
- **`method="post"`**: datos van en el body HTTP, no en la URL.

#### `Form` vs `ModelForm`

| | `Form` | `ModelForm` |
|--|--------|-------------|
| Campos | Definidos manualmente | Derivados del modelo |
| Guardado | Manual (`form.cleaned_data`) | Automático (`form.save()`) |
| Cuándo usar | Formularios sin modelo directo | Alta/edición de instancias de modelo |

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "published"]
```

#### Patrón POST/Redirect/GET (PRG)

```python
class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "blog/post_form.html", {"form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:post-list")   # PRG: redirect evita doble submit
        return render(request, "blog/post_form.html", {"form": form})
```

**¿Por qué PRG?** Evitar reenvío del formulario al recargar la página (F5 → "¿desea reenviar?").

**Filminas previstas §T5: ~6**

### Resumen teórica: ~46 filminas previstas

---

## 5. CLASE PRÁCTICA — BlogApp en Codespaces (180 min)

### Objetivos (Bloom)

1. **Ejecutar** (3) consultas avanzadas con Q objects, F expressions, annotate y aggregate en Django shell sobre BlogApp.
2. **Construir** (3) managers personalizados con `get_queryset()` para encapsular consultas frecuentes.
3. **Implementar** (3) una primera CBV con `View` base que conecte URL → contexto de modelo → template.
4. **Demostrar** (3) el flujo GET/POST con un `ModelForm` mínimo en la práctica guiada.
5. **Detectar** (4) el problema N+1 con `connection.queries` y aplicar `select_related` como solución.

### Agenda

| Tiempo | Código | Bloque |
|--------|--------|--------|
| 0–10 | — | Apertura: abrir Codespace BlogApp + verificar migraciones aplicadas |
| 10–70 | P1 | Shell avanzado: consultas sobre Post, Category, Comment |
| 70–75 | — | **Break** |
| 75–135 | P2 | Primera vista OOP: `View` base → URL → templates con herencia |
| 135–180 | P3 | Primer `ModelForm`: alta de Post + validación básica + flujo GET/POST |

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

#### Ejercicios guiados (resolución paso a paso con el docente)

**Ejercicio 1 — Recuperación segura y chaining**
```python
# ¿Qué diferencia hay entre get() y filter().first()?
cat_python = Category.objects.get(slug="python")                    # DoesNotExist si no existe
cat_python = Category.objects.filter(slug="python").first()         # None si no existe

# 5 posts publicados más recientes con su categoría
recientes = Post.objects.filter(published=True)\
                        .select_related("author")\
                        .order_by("-created_at")[:5]
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

**Ejercicio 6 — Manager personalizado**
```python
# blog/models.py — ampliar Post
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Post(models.Model):
    objects = models.Manager()          # manager por defecto
    published = PublishedManager()      # manager custom

# Uso:
Post.published.all()                   # solo publicados
Post.published.order_by("-created_at")[:5]
```

---

### §P2 — Primera vista OOP con `View` base (60 min)

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

**Verificación**: `python manage.py runserver` → navegar a `/blog/` → ver listado con navbar del base → clic en un post → ver detalle con el mismo esqueleto sin duplicar HTML.

---

### §P3 — Primer `ModelForm`: alta de Post (60 min)

> **Meta**: el estudiante completa el ciclo CRUD completo desde la interfaz web. Alta de un post con validación.

#### Paso 1 — Definir `PostForm`

```python
# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "published"]
        labels = {
            "title": "Título",
            "content": "Contenido",
            "category": "Categoría",
            "published": "¿Publicar?",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 6}),
        }

    def clean_title(self):
        """Validación custom: título no puede ser demasiado corto."""
        title = self.cleaned_data.get("title", "")
        if len(title) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return title
```

#### Paso 2 — `PostCreateView` con patrón PRG

```python
# blog/views.py (agregar)
from django.shortcuts import redirect
from .forms import PostForm

class PostCreateView(View):
    """Alta de un nuevo post — patrón POST/Redirect/GET."""
    template_name = "blog/post_form.html"

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {"form": form, "accion": "Crear"})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user   # asignar autor desde sesión
            post.save()
            return redirect("blog:post-list")   # PRG: evita doble submit
        # Formulario inválido: re-render con errores
        return render(request, self.template_name, {"form": form, "accion": "Crear"})
```

#### Paso 3 — URL y template del formulario

```python
# blog/urls.py (agregar)
from .views import PostCreateView
urlpatterns += [
    path("nuevo/", PostCreateView.as_view(), name="post-create"),
]
```

```html
{# blog/post_form.html #}
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>{{ accion }} Post</title></head>
<body>
  <h1>{{ accion }} Post</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    {% if form.errors %}
      <div class="errores">
        {{ form.errors }}
      </div>
    {% endif %}
    <button type="submit">{{ accion }}</button>
  </form>
  <a href="{% url 'blog:post-list' %}">← Cancelar</a>
</body>
</html>
```

#### Paso 4 — Prueba manual del flujo

1. Navegar a `/blog/nuevo/` → ver formulario vacío (GET).
2. Enviar formulario con título corto → ver errores de validación (POST inválido).
3. Enviar formulario completo → redirección a listado → ver nuevo post (PRG completo).

---

## 6. Ajustes operativos del replan (Semana 8)

| Ajuste | Detalle |
|--------|---------|
| **Parcial 1** | Movido al inicio de Semana 9 teórica — no impacta esta clase |
| **TP-5 alcance** | Modelos + admin + ORM avanzado + primeras vistas `View` + `ModelForm` básico + tests de modelos y vistas simples |
| **Django Admin** | Soporte de inspección del dominio durante la práctica — no es eje principal de la clase |
| **Vistas genéricas** | NO en esta clase — se introducen en Semana 9 (refactor de `View` → `ListView`/`DetailView`) |
| **Template Language** | Solo lo mínimo operativo (variables, for, url tag) — profundización en Semana 9 |
| **Bootstrap** | NO en esta clase — templates skeleton en HTML puro — Bootstrap en Semana 9 |

---

## 7. Evaluación formativa

| **Momento** | **Tipo** | **Descripción** |
|---------|------|-------------|
| §T2 min 75 | Ejercicio pizarra | Código con N+1 → identificar problema → proponer corrección con `select_related` |
| §T3 min 120 | Pregunta clase | "¿Qué pasa si el método HTTP es PUT y la CBV no tiene método `put()`?" → `405 Method Not Allowed` |
| §T4 min 140 | Pregunta clase | "¿Qué pasa si un child template define un `{% block %}` que no existe en el base?" → se ignora silenciosamente. ¿Qué error cometemos al olvidar `{% extends %}` como primera línea? |
| §T5 min 165 | Cierre reflexivo | "¿Por qué hacemos redirect después de un POST exitoso y no render directo?" |
| §P1 min 65 | Verificación shell | Cada grupo ejecuta `len(connection.queries)` antes y después del `select_related` |
| §P2 min 115 | Verificación visual | Agregar un segundo child template (`post_detail.html`) que extiende `base.html` — confirmar que el navbar aparece sin duplicar código |
| §P3 min 175 | Ticket de salida | Una oración: "El patrón PRG sirve para ___" |

---

## 8. Continuidad con Semana 9

| Tema 04 introduce | Semana 9 profundiza |
|-------------------|---------------------|
| `View` base manual | `TemplateView`, `ListView`, `DetailView` — cuando se ve qué automatizan |
| DTL: variables, filtros, tags, herencia, `{% include %}` | Filtros personalizados, templatetags, template partials más complejos |
| `base.html` + `{% block %}` + `{% extends %}` | Layout con Bootstrap: base redesign con CSS framework |
| `ModelForm` básico + `clean_*` | Validaciones avanzadas, errores de formulario, redisplay |
| `PostCreateView` manual | `CreateView` / `UpdateView` como continuidad natural |
| HTML skeleton sin CSS | Templates Bootstrap con layout completo |
| Parcial 1 al inicio | Resto de la clase Semana 9 consolida Módulo V |

---

## 9. Notas de implementación para el docente

- **Dominio BlogApp**: usar `Post`, `Category`, `Comment` como modelos presupuestos. Si el Codespace no tiene los datos cargados, correr `python manage.py loaddata blog_sample.json` (o generarlos en el shell con el Ejercicio 1).
- **`commit=False` en `form.save()`**: imprescindible explicar por qué — el formulario no tiene campo `author`, pero el modelo lo requiere. Sin `commit=False` se lanza `IntegrityError`.
- **CSRF en pruebas**: si se testea con `django.test.Client`, usar `enforce_csrf_checks=False` o el fixture de `csrf_client`. Aclarar que en tests el CSRF se deshabilita por convención.
- **`get_object_or_404`**: no confundir con `.get()` — lanza `Http404` en vez de `DoesNotExist`. Siempre usarlo en vistas de detalle públicas.
- **Parcial 1**: se recomienda cerrar la Semana 8 práctica recordando que el Parcial cubre hasta este tema (ORM avanzado + View base + ModelForm básico).

---

> **Estado del diseño**: COMPLETE — puede avanzar a `minuta.md` cuando el docente apruebe.
> **Siguiente paso**: `/edu-new-topic` o activar `class-writer` (Dr. Roberto) para generar la minuta.
