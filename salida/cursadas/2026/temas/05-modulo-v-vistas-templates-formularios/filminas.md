# Filminas — Módulo V: Vistas OOP, Templates y Formularios con datos ORM
# Tema 05 | Laboratorio de Programación y Lenguajes 2026
# Clase teórica — 180 min | Django 5.1 + Python 3.13 + Bootstrap 5.3.3

---

## PORTADA

---

### [F-00] Portada

@tipo: portada
@imagen: background
@prompt-imagen: dark background with faint Python code lines in transparency — keywords class def return — blurred IDE dark mode style, deep blue palette, no text labels

# Módulo V — Vistas, Templates y Formularios

El ORM constituye la capa de persistencia del sistema.
En este módulo se expone la información al usuario mediante **vistas, templates y formularios**.

Semana 9 · BlogApp · Django 5.1 · Bootstrap 5.3.3

---

## BLOQUE 1 — URLconf: el router de Django (20 min)

---

### [F-01] El URLconf: primer componente que Django ejecuta ante una petición

@tipo: tabla

# El protocolo HTTP no determina qué código Python ejecutar — el URLconf lo hace

## Función del URLconf en la arquitectura de Django

El protocolo HTTP no dispone de mecanismo alguno para determinar qué componente Python debe ejecutarse ante una URL dada. El URLconf opera como tabla de despacho: URL → clase Python. Se implementa como un módulo Python ordinario, sin dependencia de XML, anotaciones externas ni convenciones implícitas.

## Tres principios del sistema de resolución

- La lista `urlpatterns` se recorre **en orden** — el primer patrón que produce coincidencia se ejecuta
- Django **consume** el prefijo en `include()` y transfiere el segmento restante al URLconf de la aplicación
- Si ningún patrón produce coincidencia → `Http404` automático, sin intervención de la vista

## Información transferida de la URL a la vista

`path("posts/<int:pk>/", ...)` extrae `pk=42` como `int` — la vista lo recibe en `self.kwargs["pk"]` ya convertido al tipo destino

| Elemento | Función |
|----------|---------|
| `urlpatterns` | Lista de rutas; se recorre en orden, primer match gana |
| `path()` / `re_path()` | Define patrón URL → clase de vista |
| `include()` | Delega segmento restante a otro URLconf de app |
| `<int:pk>` | Conversor de tipo: extrae y convierte a `int` automáticamente |
| Sin match | Lanza `Http404` automáticamente, sin intervención de la vista |

---

### [F-02] urls.py del proyecto: delegación con include()

@tipo: codigo

# El proyecto solo sabe que las rutas bajo /blog/ pertenecen a la app blog — nada más

## Una línea de delegación hace la aplicación reubicable

Si BlogApp se mueve de `/blog/` a `/articulos/`, se cambia **solo esta línea**. El URLconf de la aplicación no necesita saber dónde está montado.

```python
# blog_project/urls.py  ← URLconf raíz del proyecto
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # include() consume el prefijo "blog/" y transfiere lo que queda:
    # petición "/blog/posts/42/" → URLconf de blog recibe "posts/42/"
    path("blog/", include("blog.urls", namespace="blog")),
]
```

- `include()` delega — el proyecto **no conoce** los detalles de rutas de la app
- `namespace="blog"` permite `{% url 'blog:post-list' %}` en templates

---

### [F-03] urls.py de la aplicación: namespace y nombres de rutas

@tipo: codigo

# La aplicación define sus propias rutas — autónoma del proyecto que la contiene

## app_name habilita el espacio de nombres para resolución inversa

Sin `app_name`, dos aplicaciones con una ruta `"post-list"` producirían colisión de nombres. Con `app_name = "blog"` todas las rutas se acceden como `blog:post-list`.

```python
# blog/urls.py  ← URLconf de la aplicación (autónomo)
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

app_name = "blog"   # → habilita namespace: {% url 'blog:nombre' %}

urlpatterns = [
    # "" coincide con /blog/ (después de que include consumió "blog/")
    path("", PostListView.as_view(), name="post-list"),

    # <int:pk> convierte el segmento a int — si es "abc" → Http404 automático
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    path("posts/crear/", PostCreateView.as_view(), name="post-create"),
]
```

- El orden en `urlpatterns` importa: Django elige el **primer match**
- Cada `name=` es el identificador para resolución inversa

---

### [F-04] Conversores de tipo: validación en la capa de ruteo

@tipo: tabla

# La URL tipada rechaza valores inválidos antes de que alcancen el código Python

## Los conversores como mecanismo de seguridad en la frontera del sistema

En ausencia de conversores, el valor `/posts/abc/` llegaría a la vista como la cadena `"abc"`. Con `<int:pk>`, Django devuelve `Http404` **automáticamente** antes de ejecutar una sola línea de la vista. La validación de tipos se produce en la frontera del sistema, no en la lógica interna.

| Conversor | Ejemplo de URL | Tipo en `self.kwargs` | Si no produce coincidencia |
|-----------|---------------|----------------------|---------------------------|
| `<int:pk>` | `/posts/42/` | `int` → `42` | `Http404` automático |
| `<str:nombre>` | `/posts/mi-titulo/` | `str` | no rechaza ningún valor |
| `<slug:slug>` | `/posts/mi-post-2026/` | `str` slug válido | caracteres inválidos → 404 |
| `<uuid:pk>` | `/posts/a3b2-.../` | `uuid.UUID` | formato inválido → 404 |

**En la vista**: `self.kwargs["pk"]` es ya de tipo `int` — no se requiere conversión manual mediante `int(pk)`

---

### [F-05] Resolución inversa en Python: reverse() y reverse_lazy()

@tipo: codigo

# Nunca escribir "/blog/posts/42/" en el código — usar el nombre de la ruta

## reverse_lazy() es obligatorio en atributos de clase

Los atributos de clase se evalúan en tiempo de importación, antes de que el sistema de URLs esté completamente cargado. `reverse()` en ese momento lanzaría error — `reverse_lazy()` difiere la evaluación hasta el primer acceso.

```python
# views.py — resolución inversa en código Python
from django.urls import reverse, reverse_lazy

# reverse() en tiempo de ejecución (dentro de un método):
url = reverse("blog:post-detail", kwargs={"pk": 42})
# → devuelve "/blog/posts/42/"

# reverse_lazy() en atributo de clase (tiempo de importación):
class PostCreateView(CreateView):
    success_url = reverse_lazy("blog:post-list")
    # ← si se usara reverse() aquí, fallaría al importar el módulo
```

- `reverse()` → dentro de funciones o métodos
- `reverse_lazy()` → en atributos de clase (`success_url`, `login_url`, etc.)

---

### [F-06] Resolución inversa en templates: la etiqueta {% url %}

@tipo: codigo

# En templates se usa {% url %} — nunca strings literales de URL

## La misma ruta puede pasarse argumentos posicionales o con nombre

```html
<!-- templates/blog/post_list.html -->

<!-- argumento posicional -->
<a href="{% url 'blog:post-detail' post.pk %}">
  Ver publicación
</a>

<!-- argumento con nombre (más explícito) -->
<a href="{% url 'blog:post-update' pk=post.pk %}">
  Editar
</a>

<!-- sin argumentos -->
<a href="{% url 'blog:post-create' %}">
  Nueva publicación
</a>
```

- Si la URL no existe, Django lanza `NoReverseMatch` en tiempo de render — visible de inmediato
- Si el proyecto cambia el prefijo de `/blog/` a `/articulos/`, **ningún template necesita modificarse**

---

## BLOQUE 2 — El controlador View: dispatch y vistas genéricas

---

### [F-07] Django MVT: la "Vista" cumple el rol del controlador

@tipo: tabla-comparativa

# Django redenomina las capas — las responsabilidades son equivalentes a las de MVC clásico

## Diferencia terminológica entre MVC clásico y el patrón MVT de Django

En MVC clásico, la Vista es la capa de presentación. Django denomina "Vista" al componente de lógica de negocio — una decisión de diseño histórica que puede generar confusión inicial. Lo relevante es comprender la responsabilidad de cada capa, con independencia de su denominación.

| Capa en MVC clásico | Equivalente Django | Archivo | Responsabilidad |
|--------------------|-------------------|---------|----------------|
| **Modelo** | `models.py` + ORM | `models.py` | Estado, persistencia, reglas de negocio |
| **Controlador** | Vista — clases `View` | `views.py` | Recibe la petición, consulta el modelo, selecciona el template |
| **Vista** | Template — DTL | `templates/` | Renderiza los datos como HTML para el navegador |

**La Vista de Django** recibe la `HttpRequest`, consulta el ORM, construye el contexto y delega la presentación al template; actúa como coordinador del flujo de procesamiento.

---

### [F-08] Ciclo completo de una petición HTTP en Django

@tipo: tabla

# Seis capas transforman una URL en un documento HTML

## Función de cada capa en el ciclo de procesamiento

- **Middleware**: intercepta la petición antes de su despacho y la respuesta antes de su envío — aquí reside el control CSRF y la gestión de sesiones
- **URL Resolver**: extrae `pk=42` como `int` e instancia la clase de vista correspondiente
- **dispatch()**: determina si delegar en `get()` o `post()` según `request.method`
- **ORM**: retorna objetos Python — el template nunca ejecuta SQL de forma directa
- **Template Engine**: combina el template DTL con el contexto y produce el HTML final

## Punto de extensión por capa

En cada capa existe un método que puede ser sobreescrito. En esta clase se utilizan `get_queryset()`, `get_context_data()`, `form_valid()` y `clean_<campo>()`.

| Capa | Función | Método extensible |
|------|---------|-------------------|
| Middleware | CSRF, Session — intercepta antes y después de la vista | `process_request()` |
| URL Resolver | Extrae `pk=42` como `int`, instancia la vista | `resolve()` |
| `dispatch()` | Elige `get()` o `post()` según `request.method` | `dispatch()` |
| ORM | `Post.objects.get(pk=42)` → objeto Python | `get_queryset()` |
| Template Engine | Combina template DTL + contexto → HTML | `get_context_data()` |
| HttpResponse | Retorna la respuesta al cliente | `render_to_response()` |

---

### [F-09] `dispatch()`: el despachador interno de la Vista

@tipo: codigo

# dispatch() determina qué método ejecutar según el verbo HTTP recibido

## Relevancia de dispatch() para el diseño de vistas

Cuando se sobreescribe `get()` en una subclase de `View`, `dispatch()` lo invoca automáticamente. Sobreescribir `dispatch()` directamente permite interceptar **todos** los verbos HTTP, lo cual resulta apropiado para lógica que debe ejecutarse con anterioridad a cualquier handler específico.

```python
# Implementación simplificada de View.dispatch() (fuente: Django 5.1):
class View:
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def dispatch(self, request, *args, **kwargs):
        method = request.method.lower()             # "get" | "post" | ...
        if method in self.http_method_names:
            # Busca self.get() / self.post() en la subclase mediante MRO
            handler = getattr(self, method, self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
```

**Directiva de diseño**: sobreescribir `get()` / `post()` para lógica específica del verbo. Sobreescribir `dispatch()` exclusivamente para lógica transversal a todos los verbos (por ejemplo, verificación de permisos previa a cualquier acción).

---

### [F-10] El objeto `request`: representación completa de la petición HTTP

@tipo: codigo

# HttpRequest encapsula toda la información de la petición entrante

## request como fuente única de verdad sobre la petición del cliente

`HttpRequest` es una instancia que Django crea para cada petición entrante. Contiene el verbo HTTP, la ruta, los datos del formulario, el usuario autenticado y la sesión. No existe otro mecanismo para acceder a dicha información desde la vista.

```python
class PostCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        request.method          # "POST" — el verbo HTTP
        request.path            # "/blog/posts/crear/"
        request.GET             # QueryDict — parámetros de URL: ?page=2
        request.POST            # QueryDict — cuerpo del formulario: {"title": "..."}
        request.user            # instancia User autenticado, o AnonymousUser
        request.session         # diccionario persistente entre peticiones (→ bloque 5)
        request.META["HTTP_USER_AGENT"]  # cabeceras HTTP sin procesar
        return super().post(request, *args, **kwargs)
```

**`request.POST` es inmutable** — Django prohibe su modificación para evitar efectos laterales silenciosos. Para incorporar datos adicionales al formulario, se utiliza `form.instance.campo = valor` antes de `form.save()`.

---

### [F-11] Jerarquía de vistas genéricas: reutilización de patrones consolidados

@tipo: tabla

# Cada vista genérica encapsula el patrón más frecuente de su operación correspondiente

## Fundamento del uso de vistas genéricas sobre la clase base View

Con la clase base `View`, toda la lógica debe implementarse manualmente: recuperar el objeto, construir el contexto, renderizar la respuesta. Las vistas genéricas encapsulan ese código repetitivo y exponen puntos de extensión bien definidos. El código resultante en la subclase expresa **qué cambia**, en lugar de describir el funcionamiento del patrón.

## Las cinco vistas utilizadas en BlogApp

- **`ListView`**: `Post.objects.all()` + paginación automática mediante `paginate_by`
- **`DetailView`**: `Post.objects.get(pk=pk)` + `Http404` automático si el objeto no existe
- **`CreateView`**: formulario unbound → bound → `save()` INSERT → redirección
- **`UpdateView`**: idéntico a CreateView pero con `instance=objeto` → `save()` UPDATE
- **`DeleteView`**: GET presenta confirmación — POST ejecuta `objeto.delete()`

| Clase | Operación SQL | Template por defecto | Método clave |
|-------|--------------|---------------------|--------------|
| `ListView` | SELECT all | `post_list.html` | `get_queryset()` |
| `DetailView` | SELECT by pk | `post_detail.html` | `get_object()` |
| `CreateView` | INSERT | `post_form.html` | `form_valid()` |
| `UpdateView` | UPDATE | `post_form.html` | `form_valid()` |
| `DeleteView` | DELETE | `post_confirm_delete.html` | `delete()` |

---

### [F-12] `ListView` con `get_queryset()`: integración del ORM en la vista

@tipo: demo

# get_queryset() es el punto de extensión entre la vista y la capa de persistencia

## Motivo para sobreescribir get_queryset() en lugar de declarar model

El atributo `model = Post` produce `Post.objects.all()` — la totalidad de los registros sin filtrado. `get_queryset()` otorga control total sobre la consulta: `filter()`, `select_related()`, `order_by()`. Corresponde al mismo QuerySet construido en el Tema 04, ahora integrado en la capa de vista.

```python
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"   # nombre de la variable en el template (default: object_list)
    paginate_by = 10                # Django segmenta los resultados automáticamente

    def get_queryset(self):
        # select_related previene N+1 al acceder a post.author y post.category en el template
        return Post.objects.filter(published=True)\
                           .select_related("author", "category")\
                           .order_by("-created_at")
```

**Paginación automática**: con `paginate_by=10`, el template recibe `page_obj` con métodos `has_next()`, `has_previous()` y `next_page_number()`. El parámetro de URL es `?page=2`, sin necesidad de código adicional en la vista.

---

## BLOQUE 3 — Templates con QuerySets reales (35 min)

---

### [F-13] Contexto automático: variables inyectadas por cada vista genérica

@tipo: tabla

# Las vistas genéricas transfieren variables al template de forma implícita

## Si {{ posts }} no se resuelve en el template, la causa más frecuente es esta tabla

`context_object_name` no definido → Django usa `object_list` como nombre por defecto. Conocer las variables automáticas evita buscar bugs donde no los hay.

| Vista | Variables automáticas en el contexto |
|-------|--------------------------------------|
| `ListView` | `object_list`, `page_obj`, `paginator`, `is_paginated` |
| `DetailView` | `object` (y el alias de `context_object_name`) |
| `CreateView` / `UpdateView` | `form` (instancia del formulario) |
| `DeleteView` | `object` (el objeto candidato a eliminación) |

- `context_object_name = "posts"` agrega `posts` como alias de `object_list`
- Ambos nombres coexisten en el contexto — no se reemplaza, se agrega

---

### [F-14] get_context_data(): agregar variables al contexto sin perder las automáticas

@tipo: codigo

# super().get_context_data() es obligatorio — omitirlo elimina todas las variables automáticas

## El defecto silencioso más frecuente con las vistas genéricas

Sin `super()`, `page_obj`, `form` y demás variables de la vista genérica desaparecen del template. El template no lanza error — simplemente no renderiza datos. El bug parece estar en el template pero está en la vista.

```python
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # OBLIGATORIO: preserva todas las variables automáticas (page_obj, paginator, etc.)
        ctx = super().get_context_data(**kwargs)

        # Agregar variables propias al mismo diccionario:
        ctx["categorias"] = Category.objects.all()   # para un filtro por categoría
        ctx["total_publicados"] = self.get_queryset().count()

        return ctx  # ← siempre retornar el contexto completo
```

- `ctx` es un dict estándar — se pueden agregar cualquier clave/valor
- El template accede a `{{ categorias }}` y `{{ total_publicados }}` directamente

---

### [F-15] DTL: dot notation sobre atributos, filtros y propiedades

@tipo: codigo

# Django resuelve post.author.username navegando atributo por atributo — si alguno es None, retorna cadena vacía

## Dot notation: cómo Django evalúa cada expresión

Para `post.author.username`: accede a `post.author` (ForeignKey → ORM), luego `.username` del objeto `User`. Sin excepción si algún paso es `None` — silencio controlado.

```html
<!-- Acceso a atributos simples con filtros -->
{{ post.title|upper }}                         {# filtro: convierte a mayúsculas #}
{{ post.created_at|date:"d/m/Y" }}             {# filtro: formatea fecha #}
{{ post.body|truncatewords:50 }}               {# filtro: recorta a 50 palabras #}

<!-- Acceso a método del modelo (sin paréntesis) -->
{{ post.author.get_full_name|default:"Anónimo" }}

<!-- Acceso a ForeignKey: navega al objeto relacionado -->
{{ post.category.name }}
```

- Los filtros se encadenan con `|`
- El método se llama sin `()` — Django lo invoca automáticamente
- `|default:"valor"` cubre el caso `None` o cadena vacía

---

### [F-16] DTL: relaciones inversas y el problema N+1

@tipo: codigo

# post.comments.all dentro de un for ejecuta una consulta SQL por cada post — prefetch_related lo resuelve

## El problema N+1 en templates: invisible pero costoso

Un template inocente puede generar decenas de consultas SQL. `{% for comment in post.comments.all %}` parece inofensivo, pero dentro de un `{% for posts %}` ejecuta 1 consulta por cada post. Con 100 posts → 101 consultas.

```html
<!-- templates/blog/post_list.html -->
{% for post in posts %}

  <!-- FK simple: 1 consulta por post si no hay select_related en get_queryset() -->
  {{ post.category.name }}

  <!-- Relación inversa (reverse FK): 1 consulta por post si no hay prefetch_related -->
  {% for comment in post.comments.all %}
    {{ comment.author.username }}: {{ comment.body }}
  {% endfor %}

{% endfor %}
```

```python
# Solución en get_queryset() — los datos llegan precargados al template:
def get_queryset(self):
    return Post.objects.filter(published=True)\
                       .select_related("author", "category")  # FK → JOIN en SQL
                       .prefetch_related("comments__author")  # reverseFK → 2 queries total
```

- `select_related` → hace JOIN en la consulta principal (para FK)
- `prefetch_related` → hace consulta separada y cachea (para reverse FK y M2M)

---

### [F-17] Herencia de templates: base.html — la estructura compartida

@tipo: codigo

# base.html define nav, head y layout — todas las páginas heredan de aquí

## Un cambio en base.html afecta toda la aplicación

Bootstrap, la barra de navegación, el manejo de mensajes flash: todo en un único lugar. Los templates hijos solo necesitan definir el contenido específico de cada página.

```html
<!-- templates/blog/base.html — se define UNA vez, se hereda en TODOS los templates -->
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}BlogApp{% endblock %}</title>
  <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
</head>
<body>
<nav class="navbar navbar-dark bg-dark">
  <a class="navbar-brand" href="{% url 'blog:post-list' %}">BlogApp</a>
  <a class="nav-link text-white" href="{% url 'blog:post-create' %}">Nueva publicación</a>
</nav>
<div class="container mt-4">
  {% if messages %}
    {% for m in messages %}
      <div class="alert alert-{{ m.tags }}">{{ m }}</div>
    {% endfor %}
  {% endif %}

  {% block content %}{% endblock %}  <!-- cada template hijo rellena este bloque -->
</div>
</body>
</html>
```

---

### [F-18] Herencia de templates: el template hijo — solo el contenido específico

@tipo: codigo

# {% extends %} hace que el template hijo solo declare qué cambia respecto a base.html

## El template hijo no repite HTML estructural

`{% extends "blog/base.html" %}` indica que este template es un "relleno" para los `{% block %}` de base. Todo lo que no esté en un bloque se ignora.

```html
<!-- templates/blog/post_detail.html — solo el contenido de esta página -->
{% extends "blog/base.html" %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
  <h1 class="mb-3">{{ post.title }}</h1>

  <!-- Acceso a FK con dot notation — post.category usa select_related del queryset -->
  <span class="badge bg-secondary">{{ post.category.name }}</span>

  <!-- Filtro de fecha con escape de caracteres especiales -->
  <p class="text-muted">{{ post.created_at|date:"d \d\e F \d\e Y" }}</p>

  <!-- linebreaks convierte \n en <br> y párrafos -->
  {{ post.body|linebreaks }}
{% endblock %}
```

- `{% block title %}` sobreescribe el título en `<head>` de base.html
- `{% block content %}` proporciona el cuerpo de la página
- `post` llega del contexto automático de `DetailView` (`context_object_name`)

---

## BLOQUE 4 — Formularios Django: ciclo de enlace y validación

---

### [F-19] El ciclo de enlace: estado bound vs unbound

@tipo: tabla-comparativa

# Un formulario solo puede ser validado si tiene datos del usuario asociados

## El estado de enlace como fundamento del ciclo de procesamiento de formularios

`PostForm()` sin argumentos crea un formulario **unbound**: `is_bound=False`, por lo que `is_valid()` retorna `False` sin ejecutar validación alguna, independientemente de la calidad de los datos, dado que no existe información asociada al formulario. Únicamente cuando se construye con `data=request.POST` el formulario queda **bound** y la validación adquiere sentido.

| Construcción | `is_bound` | `is_valid()` | Cuándo utilizarlo |
|-------------|-----------|-------------|------------------|
| `PostForm()` | `False` | siempre `False` | GET — presentar formulario vacío |
| `PostForm(instance=post)` | `False` | siempre `False` | GET — pre-poblar para edición |
| `PostForm(data=request.POST)` | `True` | ejecuta el pipeline | POST — crear nuevo registro |
| `PostForm(data=request.POST, instance=post)` | `True` | ejecuta el pipeline | POST — actualizar registro existente |

---

### [F-20] Pipeline de validación: las cinco capas de procesamiento en secuencia

@tipo: timeline

# `form.is_valid()` ejecuta esta cadena de procesamiento — si una capa falla, la ejecución se detiene

## Función de cada capa y relevancia del orden de ejecución

1. **`to_python()`** — convierte el string recibido por POST al tipo Python destino: `"42"` → `int(42)`. Si la conversión falla, el campo queda inválido y las capas posteriores se omiten para ese campo.
2. **`validate()`** — aplica las reglas declaradas en el campo: `required`, `max_length`, `min_value`, etc.
3. **`run_validators()`** — ejecuta la lista `validators=[MinLengthValidator(10), ...]` definida en el campo.
4. **`clean_<campo>()`** — lógica personalizada: permite consultar el ORM, transformar el valor y lanzar `ValidationError`.
5. **`clean()`** — validación cruzada entre campos; `self.cleaned_data` contiene únicamente los campos que superaron las capas 1 a 4.

**`cleaned_data`** solo existe a partir de que `is_valid()` haya sido invocado — acceder con anterioridad produce `AttributeError`

| Paso | Método | Función |
|------|--------|---------|
| 1 | `to_python()` | String HTTP → tipo Python destino |
| 2 | `validate()` | Aplica `required`, `max_length`, `min_value` |
| 3 | `run_validators()` | Ejecuta lista `validators=[]` del campo |
| 4 | `clean_<campo>()` | Lógica custom + ORM, puede lanzar `ValidationError` |
| 5 | `clean()` | Validación cruzada entre campos |

---

### [F-21] ``ModelForm``: generación automática de campos a partir del modelo

@tipo: codigo

# ModelForm inspecciona el modelo y genera los campos correspondientes, sin duplicar definiciones

## Ventaja de ModelForm sobre la clase Form base

Con `Form` sería necesario declarar `title = forms.CharField(max_length=200)`, duplicando lo que ya está definido en el modelo. `ModelForm` inspecciona el modelo y genera el campo de forma automática. Ante modificaciones en el modelo, el formulario se actualiza sin intervención adicional.

```python
# forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        # Solo los campos que el usuario puede editar — auto_now y pk quedan fuera
        fields = ["title", "body", "category", "published"]

        widgets = {
            # attrs agrega clases CSS de Bootstrap al widget HTML generado
            "title":    forms.TextInput(attrs={"class": "form-control"}),
            "body":     forms.Textarea(attrs={"class": "form-control", "rows": 8}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
        labels        = {"title": "Título", "body": "Contenido", "category": "Categoría"}
        error_messages = {"title": {"required": "El título es obligatorio."}}
```

---

### [F-22] ModelForm: campos generados automáticamente por tipo de modelo

@tipo: tabla

# ModelForm lee el modelo y elige el campo de formulario más apropiado para cada tipo

## Los campos auto_now y auto_now_add quedan automáticamente excluidos

Django los marca internamente como `editable=False` — si se incluyen en `fields`, se lanza `FieldError` en tiempo de ejecución.

| Campo del modelo | Campo de formulario generado | Widget por defecto |
|-----------------|------------------------------|--------------------|
| `CharField(max_length=200)` | `CharField(max_length=200)` | `TextInput` |
| `TextField()` | `CharField()` | `Textarea` |
| `BooleanField()` | `BooleanField()` | `CheckboxInput` |
| `ForeignKey(Category)` | `ModelChoiceField(queryset=Category.objects.all())` | `Select` |
| `ManyToManyField(Tag)` | `ModelMultipleChoiceField(...)` | `SelectMultiple` |
| `DateTimeField(auto_now_add=True)` | **excluido automáticamente** | — |

---

### [F-23] Capa 4: `clean_<campo>()` — validación con acceso al ORM

@tipo: codigo

# Es la capa de mayor expresividad: recibe el valor ya tipado y puede consultar la base de datos

## Obligatoriedad de retornar el valor en clean_<campo>()

`clean_title()` debe **retornar** el valor, posiblemente transformado. Si se omite el `return`, `cleaned_data["title"]` contendrá `None` aun cuando la validación haya sido superada. Django no genera excepción alguna: el defecto es silencioso.

```python
class PostForm(forms.ModelForm):

    def clean_title(self):
        # El valor ya superó las capas 1-3: es str, no None, dentro de max_length
        title = self.cleaned_data["title"].strip()

        if len(title) < 10:
            raise forms.ValidationError(
                "Mínimo %(min)s caracteres.", params={"min": 10}
            )

        # Consulta al ORM — excluir la instancia actual en operaciones de edición
        qs = Post.objects.filter(title__iexact=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe una publicación con ese título.")

        return title   # ← obligatorio: devolver el valor (posiblemente transformado)
```

El error se agrega a `form.errors["title"]` y se presenta junto al campo en el template

---

### [F-24] Capa 5: `clean()` — validación cruzada entre campos

@tipo: codigo

# clean() tiene visibilidad simultánea sobre todos los campos — apropiado para reglas que involucran múltiples campos

## Uso obligatorio de .get() sobre cleaned_data en lugar de acceso directo

Si `title` no superó la capa 4, la clave `"title"` estará ausente de `cleaned_data`; el acceso con `["title"]` lanzará `KeyError`. El uso de `.get("title", "")` es siempre seguro. Esta omisión constituye la causa más frecuente de errores inesperados en `clean()`.

```python
    def clean(self):
        cleaned = super().clean()   # ejecuta validaciones del modelo (unique, etc.)

        body      = cleaned.get("body", "")        # .get() — nunca acceso directo con []
        published = cleaned.get("published", False)

        # Regla cruzada: publicar requiere contenido mínimo sustantivo
        if published and len(body) < 100:
            self.add_error(           # asocia el error al campo "body"
                "body",
                "Para publicar, el contenido debe tener al menos 100 caracteres."
            )
        # raise ValidationError aquí → va a form.non_field_errors()

        return cleaned
```

---

### [F-25] Ciclo completo: GET → POST inválido → POST válido → Redirección

@tipo: timeline

# CreateView gestiona los tres estados de la interacción con el mismo método post()

## Fundamento del patrón PRG (Post-Redirect-Get)

En un POST exitoso, si la vista renderiza directamente la respuesta y el usuario recarga la página, el navegador **reenvía el formulario**, produciendo una inserción duplicada. La redirección convierte el POST en un GET idempotente, eliminando esta condición de error. Este es el patrón **PRG (Post-Redirect-Get)**.

| Petición | Formulario construido | `is_valid()` | Acción de la vista | HTTP |
|----------|----------------------|-------------|-------------------|----|
| `GET /posts/crear/` | `PostForm()` — unbound | — | renderizar formulario vacío | `200` |
| `POST` datos inválidos | `PostForm(data=POST)` | `False` | renderizar formulario con errores | `200` |
| `POST` datos válidos | `PostForm(data=POST)` | `True` → `form.save()` INSERT | `redirect(success_url)` | `302` |

El template es **idéntico** para ambos casos de renderizado: recibe el mismo objeto `form`, con o sin errores. El redisplay de errores no requiere lógica adicional en la vista.

---

### [F-27] `UpdateView`: la clase y sus atributos

@tipo: codigo

# UpdateView reutiliza exactamente el mismo template y formulario que CreateView

## La única diferencia visible en la clase es el nombre — el comportamiento lo determina instance=

`UpdateView` recupera automáticamente el objeto de la BD usando `pk` de la URL, lo asigna a `self.object` y construye el formulario pre-poblado. Sin código extra.

```python
# views.py
class PostUpdateView(UpdateView):
    model      = Post
    form_class = PostForm
    # Mismo template que CreateView — el form ya viene con los datos pre-cargados
    template_name = "blog/post_form.html"
    success_url   = reverse_lazy("blog:post-list")

# urls.py — la URL entrega pk a UpdateView
# path("posts/<int:pk>/editar/", PostUpdateView.as_view(), name="post-update")
```

- `UpdateView` hereda de `BaseUpdateView` → llama a `get_object()` con `pk` de la URL
- `get_object()` hace `Post.objects.get(pk=pk)` → `Http404` si no existe
- El formulario se construye internamente como `PostForm(instance=self.object)` — campos pre-llenados

---

### [F-26] `instance=`: la diferencia entre INSERT y UPDATE

@tipo: codigo

# El parámetro instance= es el único factor que convierte un formulario de creación en uno de edición

## Sin instance=, form.save() siempre hace INSERT — nunca UPDATE

Este es el error más frecuente al implementar edición: olvidar `instance=` o construir el formulario a mano sin ella.

```python
# ¿Qué hace Django internamente en CreateView?
form = PostForm(data=request.POST)
# is_bound=True, instance=None
form.save()   # → INSERT INTO blog_post (title, body, ...) VALUES (...)
              # siempre crea un registro nuevo

# ¿Qué hace Django internamente en UpdateView?
post = Post.objects.get(pk=42)          # recupera el objeto existente
form = PostForm(data=request.POST, instance=post)
# is_bound=True, instance.pk=42
form.save()   # → UPDATE blog_post SET title=... WHERE id=42
              # actualiza el registro cuyo pk coincide con instance.pk
```

- `instance=None` → el `form.save()` hace **INSERT**
- `instance=objeto_con_pk` → el `form.save()` hace **UPDATE**
- El template HTML es **idéntico** en ambos casos — `{{ form }}` renderiza el formulario igual

---

### [F-28] Template del formulario: presentación de errores por campo

@tipo: demo

# El mismo template sirve tanto para creación como para edición — el objeto form encapsula el estado

## Necesidad del atributo novalidate en el formulario HTML

Sin `novalidate`, el navegador ejecuta la validación HTML5 y puede impedir el envío antes de que Django procese el formulario. Con `novalidate`, el framework tiene control total sobre los mensajes de error, permitiendo su presentación en el idioma requerido con la lógica de negocio efectiva.

```html
<form method="post" novalidate>
  {% csrf_token %}

  {% if form.non_field_errors %}   {# errores de clean() sin campo específico asociado #}
    <div class="alert alert-danger">
      {% for e in form.non_field_errors %}{{ e }}{% endfor %}
    </div>
  {% endif %}

  {% for field in form %}
    <div class="mb-3">
      <label class="form-label fw-semibold">
        {{ field.label }}{% if field.field.required %} *{% endif %}
      </label>
      {{ field }}   <!-- widget con class="form-control" definido en Meta.widgets -->
      {% for error in field.errors %}
        <div class="text-danger small mt-1">{{ error }}</div>
      {% endfor %}
    </div>
  {% endfor %}

  <button type="submit" class="btn btn-primary">Guardar</button>
  <a href="{% url 'blog:post-list' %}" class="btn btn-secondary">Cancelar</a>
</form>
```

---

### [F-29] ``DeleteView``: la clase Python — GET muestra, POST elimina

@tipo: codigo

# GET sobre DeleteView nunca elimina datos — solo renderiza la confirmación

## Por qué las operaciones destructivas requieren POST y no GET

Un `<a href="/posts/42/eliminar/">` genera un GET. Si ese GET eliminara, cualquier bot de indexación o clic accidental destruiría datos. La eliminación requiere un POST explícito con `{% csrf_token %}`.

```python
# views.py
class PostDeleteView(DeleteView):
    model         = Post
    template_name = "blog/post_confirm_delete.html"
    success_url   = reverse_lazy("blog:post-list")
    # GET  → llama a get()  → renderiza template de confirmación (NO toca la BD)
    # POST → llama a post() → ejecuta self.object.delete() → redirect a success_url

# urls.py
# path("posts/<int:pk>/eliminar/", PostDeleteView.as_view(), name="post-delete")
```

- `DeleteView` hereda de `BaseDeleteView` — el método `delete()` ejecuta `self.object.delete()`
- Solo el POST activa la eliminación — el GET es siempre seguro de llamar

---

### [F-30] `DeleteView`: el template de confirmación

@tipo: codigo

# El template solo presenta la pregunta — el formulario POST es el que elimina

## El botón de confirmación es un formulario POST sin campos, solo csrf_token

El template recibe `object` (el objeto a eliminar) del contexto automático de `DeleteView`.

```html
<!-- templates/blog/post_confirm_delete.html -->
{% extends "blog/base.html" %}

{% block content %}
<div class="card border-danger">
  <div class="card-body">
    <h4 class="card-title text-danger">Confirmar eliminación</h4>

    <!-- object = instancia de Post, inyectada por DeleteView -->
    <p>¿Eliminar la publicación <strong>"{{ object.title }}"</strong>?</p>
    <p class="text-muted">Esta operación no puede revertirse.</p>

    <!-- Este formulario POST es el que dispara objeto.delete() en la vista -->
    <form method="post">
      {% csrf_token %}   {# obligatorio: sin este token Django rechaza el POST #}
      <button type="submit" class="btn btn-danger">Eliminar</button>
      <a href="{% url 'blog:post-list' %}" class="btn btn-secondary">Cancelar</a>
    </form>
  </div>
</div>
{% endblock %}
```

---

## BLOQUE 5 — Sesiones HTTP: persistencia de estado en un protocolo sin estado (8 min)

---

### [F-31] HTTP es stateless: el protocolo no conserva estado entre peticiones

@tipo: tabla

# Cada petición HTTP es anónima por diseño — el mecanismo de sesiones resuelve la persistencia de estado

## HTTP como protocolo sin estado y sus implicaciones para las aplicaciones web

HTTP es un protocolo sin estado (*stateless*) por razones de escalabilidad: cualquier servidor puede responder cualquier petición sin conocimiento de las anteriores. Sin embargo, las aplicaciones requieren persistir información entre peticiones: estado de autenticación, preferencias del usuario, datos de sesión de trabajo, entre otros. El mecanismo provisto por Django son las sesiones en el servidor.

## Funcionamiento de la sesión de Django en tres pasos

1. Django genera un identificador de sesión UUID único y lo almacena en una cookie `sessionid`
2. El navegador envía esa cookie en **cada petición subsiguiente** — de forma automática
3. Django lee `sessionid`, recupera los datos asociados en la base de datos (o caché) y los expone como `request.session` — un diccionario Python estándar

## Alcance de esta clase

`request.session` como diccionario y el **messages framework** que lo utiliza internamente para el patrón PRG. La autenticación completa se aborda en el Módulo VI.

| Mecanismo | Descripción |
|-----------|-------------|
| Sin sesión | Cada petición HTTP es anónima — el servidor no reconoce al usuario |
| Cookie `sessionid` | UUID generado por Django; viaja en cada petición automáticamente |
| Store servidor | Datos del usuario asociados al `sessionid` en BD o caché |
| `request.session` | Diccionario Python para leer/escribir datos de sesión |
| Messages framework | Usa sesión internamente para el patrón POST-Redirect-GET |

---

### [F-32] ``request.session``: el diccionario que persiste entre peticiones

@tipo: codigo

# request.session es un dict estándar de Python — Django lo persiste en la BD entre peticiones

## El mecanismo: cookie → servidor → diccionario Python

1. Django genera un UUID de sesión y lo envía como cookie `sessionid` al navegador
2. El navegador envía esa cookie en cada petición siguiente
3. Django lee la cookie, busca en la BD y expone los datos como `request.session`

```python
# views.py — acceso directo a la sesión como diccionario
class PostDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        # Escritura: guardar estado entre peticiones
        request.session["ultimo_post_visto"] = self.kwargs["pk"]

        # Lectura con valor por defecto (seguro si la clave no existe aún)
        historial = request.session.get("historial", [])
        historial.append(self.kwargs["pk"])
        request.session["historial"] = historial

        return super().get(request, *args, **kwargs)
```

- La sesión se guarda automáticamente al final de cada petición si fue modificada
- `request.session` dura hasta que el navegador cierra o la sesión expira (configurable)
- La autenticación completa (`request.user`) se aborda en el Módulo VI

---

### [F-33] Messages framework: el patrón PRG con mensajes flash

@tipo: codigo

# messages.success() persiste el mensaje en la sesión — aparece en la página siguiente a la redirección

## Por qué no mostrar el mensaje directamente en el POST

El POST exitoso redirige (PRG). Si se muestra el mensaje en el POST, desaparece en el redirect. `messages` los guarda en la sesión → aparecen en el GET siguiente → se auto-descartan al renderizar.

```python
# views.py — messages se agrega ANTES de la redirección
from django.contrib import messages

class PostCreateView(CreateView):
    def form_valid(self, form):
        # El mensaje queda guardado en request.session
        messages.success(self.request, "Publicación creada correctamente.")
        return super().form_valid(form)  # → redirect a success_url (HTTP 302)

    def form_invalid(self, form):
        messages.error(self.request, "Revisá los errores en el formulario.")
        return super().form_invalid(form)  # → re-render del formulario (HTTP 200)
```

```html
{# base.html — se muestra en CUALQUIER página después del redirect #}
{% for m in messages %}
  <div class="alert alert-{{ m.tags }}">{{ m }}</div>
{% endfor %}
{# Django elimina el mensaje de la sesión después de renderizarlo #}
```

- `m.tags` es `"success"`, `"error"`, `"warning"`, `"info"` — coincide con clases de Bootstrap

---

## CIERRE

---

### [F-34] Síntesis del Módulo V: conexión entre la petición HTTP y la base de datos

@tipo: cierre
@imagen: background
@prompt-imagen: fondo oscuro degradado azul profundo a negro — texto blanco centrado — estilo minimalista de cierre de clase universitaria

# Cinco bloques articulan el flujo completo desde la petición HTTP hasta la capa de persistencia

## Contenidos abordados en esta clase

- **URLconf**: `path()`, conversores de tipo, `include()`, `reverse_lazy()` — el sistema de ruteo tipado
- **dispatch() + request**: mecanismo de despacho de verbos HTTP a métodos Python
- **Vistas genéricas**: `ListView` · `DetailView` · `CreateView` · `UpdateView` · `DeleteView`
- **Templates + ORM**: contexto automático, dot notation, filtros DTL, herencia de templates con Bootstrap 5
- **Formularios**: ciclo bound/unbound · pipeline de cinco capas · `ModelForm` · `clean_<campo>()` · patrón PRG
- **Sesiones**: `request.session` como diccionario · messages framework

## Hilo conductor del módulo

`URL → dispatch() → ORM → Form → Template → Redirect` — cada bloque abordado constituye un componente de esta cadena de procesamiento

Próxima instancia: laboratorio práctico — implementación del CRUD completo de BlogApp con vistas genéricas basadas en clases
