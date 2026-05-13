# Filminas — Módulo V: Vistas OOP, Templates y Formularios con datos ORM
# Tema 05 | Laboratorio de Programación y Lenguajes 2026
# Clase teórica — 180 min | Django 5.1 + Python 3.13 + Bootstrap 5.3.3

---

## PORTADA

---

### [F-00] Portada

@tipo: portada
@imagen: background
@prompt-imagen: fondo oscuro con código Python en transparencia — class, def, return — líneas difuminadas estilo IDE en modo oscuro, paleta azul profundo

# Módulo V — Vistas, Templates y Formularios

El ORM ya lo dominamos. Hoy lo **exponemos al usuario**.

Semana 9 · BlogApp · Django 5.1 · Bootstrap 5.3.3

---

## BLOQUE 1 — URLconf: el router de Django (20 min)

---

### [F-01] El URLconf: primer código que ejecuta Django ante una petición

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama horizontal con tres bloques — "Browser: GET /posts/42/" → caja "URLconf: recorre urlpatterns en orden, primer match gana" → "PostDetailView(pk=42)" — etiqueta inferior "si ningún patrón hace match → Http404 automático" — fondo blanco, bordes redondeados, flechas gruesas

# Antes de que llegue a la vista, Django resuelve la URL

## Por qué existe el URLconf

HTTP no sabe qué función Python ejecutar ante una URL. El URLconf es la tabla de traducción: URL → clase Python. Es un módulo Python ordinario — no XML, no anotaciones, no magia.

## Tres reglas del sistema de resolución

- La lista `urlpatterns` se recorre **en orden** — el primer patrón que hace match ejecuta
- Django **consume** el prefijo en `include()` y pasa el resto al URLconf de la app
- Si ningún patrón hace match → `Http404` automático, sin código en la vista

## Qué viaja de la URL a la vista

`path("posts/<int:pk>/", ...)` extrae `pk=42` como `int` — la vista lo recibe en `self.kwargs["pk"]` ya convertido

---

### [F-02] Dos niveles de urls.py: proyecto y aplicación

@tipo: codigo

# El proyecto delega — la app es dueña de sus propias rutas

## Por qué dos niveles

El URLconf raíz solo sabe que "todo lo que empiece con `/blog/`" pertenece a la app `blog`. La app define sus propias rutas internamente. Si mañana movemos la app a `/articulos/`, solo cambia **una línea** en el proyecto.

```python
# blog_project/urls.py  ← URLconf raíz
from django.urls import path, include
urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    # Django consume "blog/" y pasa el resto: "/posts/42/" → "posts/42/"
]
```

```python
# blog/urls.py  ← URLconf de la aplicación
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

app_name = "blog"   # habilita el namespace → {% url 'blog:post-list' %}

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/crear/", PostCreateView.as_view(), name="post-create"),
]
```

---

### [F-03] Conversores de tipo: validación en la capa de ruteo

@tipo: tabla

# La URL tipada rechaza valores inválidos antes de llegar a Python

## Por qué los conversores son una ventaja de seguridad

Sin conversores, `/posts/abc/` llegaría a la vista como el string `"abc"`. Con `<int:pk>`, Django devuelve 404 **automáticamente** antes de ejecutar una sola línea de la vista. La validación de tipos ocurre en la frontera del sistema.

| Conversor | Ejemplo de URL | Tipo en `self.kwargs` | Si no hace match |
|-----------|---------------|----------------------|-----------------|
| `<int:pk>` | `/posts/42/` | `int` → `42` | `Http404` automático |
| `<str:nombre>` | `/posts/mi-titulo/` | `str` | nunca rechaza |
| `<slug:slug>` | `/posts/mi-post-2026/` | `str` slug válido | caracteres inválidos → 404 |
| `<uuid:pk>` | `/posts/a3b2-.../` | `uuid.UUID` | formato inválido → 404 |

**En la vista**: `self.kwargs["pk"]` ya es `int` — no hace falta `int(pk)` manual, nunca

---

### [F-04] Resolución inversa: el principio de URL indirecta

@tipo: concepto-mixto
@imagen: none

# Nunca escribir `/blog/posts/42/` directamente en el código

## El problema del hardcoding

Si la URL cambia de `/posts/42/` a `/articulos/42/`, hay que buscar y reemplazar en todo el proyecto. La resolución inversa desacopla el código de la estructura de URLs: se referencia por nombre, Django genera la cadena.

```python
# views.py / models.py — resolución en Python
from django.urls import reverse, reverse_lazy

reverse("blog:post-detail", kwargs={"pk": 42})  # → "/blog/posts/42/"

# reverse_lazy(): versión diferida — obligatoria en atributos de clase
# porque los atributos se evalúan en import time, antes de que las URLs
# estén completamente cargadas
success_url = reverse_lazy("blog:post-list")
```

```html
<!-- templates/ — resolución en DTL -->
<a href="{% url 'blog:post-detail' post.pk %}">Ver post</a>
<a href="{% url 'blog:post-update' pk=post.pk %}">Editar</a>
```

**Regla sin excepción**: `{% url %}` en templates · `reverse_lazy()` en clases · `reverse()` en funciones

---

## BLOQUE 2 — El controlador View: dispatch y vistas genéricas (35 min)

---

### [F-05] Django MVT: la "Vista" es el controlador

@tipo: tabla-comparativa

# Django renombra las capas — los roles son los mismos que en MVC clásico

## Por qué Django usa "Vista" para lo que MVC llama "Controlador"

En MVC clásico, la Vista es la capa de presentación. Django llama "Vista" a la lógica de negocio — una decisión histórica que confunde al principio. Lo importante es entender qué hace cada capa, no cómo se llama.

| Capa en MVC clásico | Equivalente Django | Archivo | Responsabilidad |
|--------------------|-------------------|---------|----------------|
| **Modelo** | `models.py` + ORM | `models.py` | Estado, persistencia, reglas de negocio |
| **Controlador** | Vista — clases `View` | `views.py` | Recibe request, consulta modelo, elige template |
| **Vista** | Template — DTL | `templates/` | Renderiza datos como HTML para el browser |

**La Vista de Django** recibe la `HttpRequest`, consulta el ORM, construye el contexto y delega la presentación al template. Es el director de orquesta.

---

### [F-06] Ciclo completo de una petición HTTP en Django

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama vertical de flujo con 6 cajas apiladas — "Browser GET /posts/42/" → "Middleware Stack (CSRF, Session)" → "URL Resolver → pk=42" → "View.dispatch() → get()" → "ORM: Post.objects.get(pk=42)" → "Template Engine → HTML" → "HttpResponse 200" — colores distintos por capa, fondo blanco

# Seis capas transforman una URL en una página HTML

## Qué hace cada capa y cuándo importa entenderla

- **Middleware**: intercepta la request antes y la response después — aquí vive CSRF y la sesión
- **URL Resolver**: extrae `pk=42` como `int`, instancia la clase de vista correcta
- **dispatch()**: decide si delegar a `get()` o `post()` según `request.method`
- **ORM**: retorna objetos Python — el template nunca ejecuta SQL directamente
- **Template Engine**: combina el template DTL con el contexto → HTML puro

## Un punto de extensión por capa

En cada capa hay un método que podés sobreescribir. Hoy trabajamos con `get_queryset()`, `get_context_data()`, `form_valid()` y `clean_<campo>()`.

---

### [F-07] `dispatch()`: el despachador interno de la Vista

@tipo: codigo

# dispatch() decide qué método ejecutar según el verbo HTTP

## Por qué importa conocerlo

Cuando sobreescribís `get()` en una subclase de `View`, `dispatch()` lo llama automáticamente. Sobreescribir `dispatch()` intercepta **todos** los verbos HTTP — útil para lógica que debe correr antes de cualquier handler.

```python
# Implementación real simplificada de View.dispatch():
class View:
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def dispatch(self, request, *args, **kwargs):
        method = request.method.lower()             # "get" | "post" | ...
        if method in self.http_method_names:
            # Busca self.get() / self.post() en la subclase
            handler = getattr(self, method, self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
```

**Regla práctica**: sobreescribir `get()` / `post()` para lógica específica del verbo. Sobreescribir `dispatch()` solo para lógica que aplica a todos los verbos (ej: autenticación manual antes de cualquier acción).

---

### [F-08] El objeto `request`: toda la información de la petición HTTP

@tipo: codigo

# request está disponible en todos los métodos de la vista

## Es la única fuente de verdad sobre lo que envió el browser

`HttpRequest` es una instancia que Django crea para cada petición entrante. Contiene todo: el verbo HTTP, la ruta, los datos del formulario, el usuario autenticado y la sesión. No hay otra forma de acceder a estos datos en la vista.

```python
class PostCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        request.method          # "POST" — el verbo HTTP
        request.path            # "/blog/posts/crear/"
        request.GET             # QueryDict — parámetros de URL: ?page=2
        request.POST            # QueryDict — cuerpo del form: {"title": "Mi post"}
        request.user            # instancia User autenticado, o AnonymousUser
        request.session         # dict persistente entre peticiones (→ bloque 5)
        request.META["HTTP_USER_AGENT"]  # headers HTTP crudos
        return super().post(request, *args, **kwargs)
```

**request.POST es inmutable** — Django no permite modificarlo para evitar efectos laterales silenciosos. Para pasar datos extra al formulario, usar `form.instance.campo = valor` antes de `form.save()`.

---

### [F-09] Jerarquía de vistas genéricas: no reimplementar lo que Django ya resolvió

@tipo: concepto-abstracto
@imagen: right-half
@prompt-imagen: árbol de herencia con cajas — raíz "View" en gris, segundo nivel "TemplateView / ListView / DetailView" en azul, tercer nivel "CreateView / UpdateView / DeleteView" en verde — etiquetas cortas: "dispatch manual", "lista + pagina", "un objeto", "INSERT", "UPDATE", "DELETE" — fondo blanco, tipografía monospace

# Cada vista genérica automatiza el patrón más común de cada operación

## Por qué usar vistas genéricas en lugar de View base

Con `View` base escribís todo a mano: recuperar el objeto, construir el contexto, renderizar. Las vistas genéricas implementan ese boilerplate una sola vez y dan puntos de extensión claros. El código que queda en tu clase expresa **qué cambia**, no cómo funciona el patrón.

## Las cinco vistas que usamos en BlogApp

- **`ListView`**: `Post.objects.all()` + paginación automática con `paginate_by`
- **`DetailView`**: `Post.objects.get(pk=pk)` + `Http404` automático si no existe
- **`CreateView`**: form unbound → bound → `save()` INSERT → redirect
- **`UpdateView`**: igual que Create pero con `instance=objeto` → `save()` UPDATE
- **`DeleteView`**: GET muestra confirmación — POST ejecuta `objeto.delete()`

---

### [F-10] `ListView` con `get_queryset()`: ORM avanzado en la vista

@tipo: demo

# get_queryset() es el punto de extensión entre la vista y el ORM

## Por qué sobreescribir get_queryset() y no model

El atributo `model = Post` hace `Post.objects.all()` — todos los posts sin filtrar. `get_queryset()` da control total: `filter()`, `select_related()`, `order_by()`. Es el mismo QuerySet de Tema 04, ahora integrado en la vista.

```python
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"   # nombre en el template (default: object_list)
    paginate_by = 10                # Django divide en páginas automáticamente

    def get_queryset(self):
        # select_related evita N+1 al acceder a post.author y post.category en el template
        return Post.objects.filter(published=True)\
                           .select_related("author", "category")\
                           .order_by("-created_at")
```

**Paginación automática**: con `paginate_by=10` el template recibe `page_obj` con `has_next()`, `has_previous()`, `next_page_number()`. El parámetro de URL es `?page=2` — sin código extra en la vista.

---

## BLOQUE 3 — Templates con QuerySets reales (35 min)

---

### [F-11] Contexto automático: cada vista inyecta variables sin declaración

@tipo: tabla

# Las vistas genéricas ya pasan variables al template — no hay que redeclararlas

## Por qué es importante conocer las variables automáticas

Si pedís `{{ posts }}` en el template y no funciona, la causa es casi siempre que no definiste `context_object_name` y Django usó `object_list`. Conocer las variables automáticas evita esta confusión.

| Vista | Variables automáticas en el contexto |
|-------|--------------------------------------|
| `ListView` | `object_list`, `page_obj`, `paginator`, `is_paginated` |
| `DetailView` | `object` (y el alias de `context_object_name`) |
| `CreateView` / `UpdateView` | `form` (instancia del formulario) |
| `DeleteView` | `object` (el objeto a eliminar) |

## Agregar variables extra sin perder las automáticas

```python
def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)  # siempre: preserva las automáticas
    ctx["categorias"] = Category.objects.all()
    ctx["total"] = self.get_queryset().count()
    return ctx
```

**Sin `super()`** el contexto automático se pierde — `page_obj`, `form`, etc. dejan de existir en el template

---

### [F-12] Filtros DTL sobre datos ORM: dot notation y relaciones

@tipo: codigo

# El template accede a campos, propiedades, métodos y relaciones FK directamente

## Por qué dot notation funciona con modelos

Django resuelve `post.author.username` en tres pasos: accede al atributo `author` del `Post` (ForeignKey → consulta ORM si no hay caché), luego `username` del `User`. Si algún paso devuelve `None`, el resultado es string vacío — sin excepción.

```html
{{ post.title|upper }}
{{ post.created_at|date:"d/m/Y" }}
{{ post.body|truncatewords:50 }}
{{ post.author.get_full_name|default:"Anónimo" }}

<!-- Relación FK — dot notation dispara la query si no hay select_related -->
{{ post.category.name }}

<!-- Relación inversa (reverse FK / M2M) -->
{% for comment in post.comments.all %}
  {{ comment.author.username }}: {{ comment.body }}
{% endfor %}
```

**Problema N+1**: `post.comments.all` dentro de un `{% for posts %}` ejecuta una query por post. Solución: `prefetch_related("comments")` en `get_queryset()` de la vista — los datos llegan cacheados al template.

---

### [F-13] Herencia de templates: base.html + extensión con datos ORM

@tipo: demo

# Un template base define la estructura — las páginas hijas solo agregan contenido

## Por qué la herencia evita duplicar el HTML

Sin herencia, cada template repite el `<head>`, el `<nav>`, el footer. Con `{% extends %}` y `{% block %}`, el HTML estructural existe en un solo lugar. Cambiar el navbar requiere editar un solo archivo.

```html
<!-- templates/blog/base.html — una sola vez para toda la app -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
<nav class="navbar navbar-dark bg-dark">
  <a class="navbar-brand" href="{% url 'blog:post-list' %}">BlogApp</a>
  <a class="nav-link" href="{% url 'blog:post-create' %}">Nuevo Post</a>
</nav>
<div class="container mt-4">
  {% if messages %}
    {% for m in messages %}<div class="alert alert-{{ m.tags }}">{{ m }}</div>{% endfor %}
  {% endif %}
  {% block content %}{% endblock %}   <!-- cada hija llena este bloque -->
</div>
```

```html
<!-- templates/blog/post_detail.html — solo el contenido propio -->
{% extends "blog/base.html" %}
{% block title %}{{ post.title }}{% endblock %}
{% block content %}
  <h1>{{ post.title }}</h1>
  <span class="badge bg-secondary">{{ post.category.name }}</span>
  <p class="text-muted">{{ post.created_at|date:"d \d\e F \d\e Y" }}</p>
  {{ post.body|linebreaks }}
{% endblock %}
```

---

## BLOQUE 4 — Formularios Django: ciclo de enlace y validación (55 min)

---

### [F-14] El ciclo de enlace: bound vs unbound

@tipo: concepto-abstracto
@imagen: right-half
@prompt-imagen: dos cajas lado a lado — izquierda "UNBOUND: GET /crear/ → campos vacíos → render" — derecha "BOUND: POST /crear/ → is_valid()=True → save() → redirect" y "is_valid()=False → redisplay con errores" — bifurcación con flechas verde y roja — fondo blanco

# Un formulario solo puede validarse si tiene datos del usuario

## El estado de enlace es la clave para entender todo lo demás

`PostForm()` sin argumentos crea un formulario **unbound**: `is_bound=False`, y `is_valid()` retorna `False` sin ejecutar ninguna validación — no importa si los datos son buenos o malos, simplemente no hay datos. Solo con `data=request.POST` el formulario está **bound** y la validación tiene sentido.

| Construcción | `is_bound` | `is_valid()` | Cuándo usarlo |
|-------------|-----------|-------------|--------------|
| `PostForm()` | `False` | siempre `False` | GET — mostrar formulario vacío |
| `PostForm(instance=post)` | `False` | siempre `False` | GET — pre-poblar para editar |
| `PostForm(data=request.POST)` | `True` | ejecuta pipeline | POST — crear nuevo |
| `PostForm(data=request.POST, instance=post)` | `True` | ejecuta pipeline | POST — actualizar existente |

---

### [F-15] Pipeline de validación: las 5 capas en secuencia

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama vertical con 5 rectángulos apilados por flechas — "1 to_python(): string HTTP → tipo Python" → "2 validate(): required, max_length" → "3 run_validators(): lista validators=[]" → "4 clean_campo(): lógica custom + ORM" → "5 clean(): validación cruzada" — bifurcación final verde "cleaned_data" y roja "form.errors"

# `form.is_valid()` ejecuta esta cadena — si una capa falla, se detiene

## Qué hace cada capa y por qué el orden importa

1. **`to_python()`** — convierte el string del POST a tipo Python: `"42"` → `int(42)`. Si falla, el campo queda inválido y las capas siguientes se saltean para ese campo.
2. **`validate()`** — reglas del campo: `required`, `max_length`, `min_value`, `EmailField`, etc.
3. **`run_validators()`** — lista `validators=[MinLengthValidator(10), ...]` definida en el campo.
4. **`clean_<campo>()`** — tu lógica: puede consultar el ORM, transformar el valor, lanzar `ValidationError`.
5. **`clean()`** — validación cruzada entre campos; `self.cleaned_data` tiene solo los que pasaron capas 1-4.

**`cleaned_data`** solo existe después de `is_valid()` — acceder antes lanza `AttributeError`

---

### [F-16] `ModelForm`: campos generados automáticamente desde el modelo

@tipo: codigo

# ModelForm inspecciona el modelo y genera los campos — sin duplicar definiciones

## Por qué ModelForm en lugar de Form

Con `Form` declararías `title = forms.CharField(max_length=200)` copiando lo que ya está en el modelo. `ModelForm` lee el modelo y genera el campo automáticamente. Si cambiás el modelo, el formulario se actualiza solo.

```python
class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ["title", "body", "category", "published"]
        widgets = {
            "title":    forms.TextInput(attrs={"class": "form-control"}),
            "body":     forms.Textarea(attrs={"class": "form-control", "rows": 8}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
        labels  = {"title": "Título", "body": "Contenido", "category": "Categoría"}
        error_messages = {"title": {"required": "El título es obligatorio."}}
```

| Campo del modelo | Campo de formulario generado |
|-----------------|------------------------------|
| `CharField(max_length=200)` | `CharField(max_length=200, widget=TextInput)` |
| `ForeignKey(Category)` | `ModelChoiceField(queryset=Category.objects.all())` |
| `DateTimeField(auto_now_add=True)` | **excluido** — no editable |

---

### [F-17] Capa 4: `clean_<campo>()` — validación con acceso al ORM

@tipo: codigo

# Es la capa más potente: recibe el valor ya tipado y puede consultar la base de datos

## Por qué retornar el valor es obligatorio

`clean_title()` debe **retornar** el valor — posiblemente transformado. Si olvidás el `return`, `cleaned_data["title"]` será `None` aunque la validación pasó. Django no lanza error: el bug es silencioso.

```python
class PostForm(forms.ModelForm):

    def clean_title(self):
        # Ya pasó capas 1-3: es str, no None, dentro de max_length
        title = self.cleaned_data["title"].strip()

        if len(title) < 10:
            raise forms.ValidationError(
                "Mínimo %(min)s caracteres.", params={"min": 10}
            )

        # Consulta ORM — excluir instancia actual en edición (UpdateView)
        qs = Post.objects.filter(title__iexact=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe un post con ese título.")

        return title   # ← obligatorio: devolver el valor (puede transformarse)
```

El error va a `form.errors["title"]` — se muestra junto al campo en el template

---

### [F-18] Capa 5: `clean()` — validación cruzada entre campos

@tipo: codigo

# clean() ve todos los campos simultáneamente — ideal para reglas que cruzan campos

## Por qué usar .get() en lugar de [] en cleaned_data

Si `title` falló en la capa 4, `cleaned_data` no tiene la clave `"title"` — acceder con `["title"]` lanza `KeyError`. `.get("title", "")` es siempre seguro. Esta es la causa más frecuente de errores inesperados en `clean()`.

```python
    def clean(self):
        cleaned = super().clean()   # ejecuta validaciones del modelo (unique, etc.)

        body      = cleaned.get("body", "")        # .get() — nunca []
        published = cleaned.get("published", False)

        # Regla cruzada: publicar requiere body sustancioso
        if published and len(body) < 100:
            self.add_error(           # asocia el error al campo "body"
                "body",
                "Para publicar, el contenido debe tener al menos 100 caracteres."
            )
        # raise ValidationError aquí → va a form.non_field_errors()

        return cleaned
```

---

### [F-19] Ciclo completo: GET → POST inválido → POST válido → Redirect

@tipo: timeline

# CreateView maneja los tres casos con el mismo método post()

## Por qué el éxito hace redirect y el fallo hace render

En un POST exitoso, si renderizamos directamente y el usuario recarga la página, el browser **reenvía el formulario** — inserción duplicada. El redirect convierte el POST en un GET idempotente. Este es el patrón **PRG (Post-Redirect-Get)**.

| Petición | Formulario construido | `is_valid()` | Acción | HTTP |
|----------|----------------------|-------------|--------|------|
| `GET /posts/crear/` | `PostForm()` — unbound | — | render con form vacío | `200` |
| `POST` datos inválidos | `PostForm(data=POST)` | `False` | render con form + errores | `200` |
| `POST` datos válidos | `PostForm(data=POST)` | `True` → `form.save()` INSERT | `redirect(success_url)` | `302` |

El template es **el mismo** para los dos casos de render: recibe el mismo objeto `form`, con o sin errores. El redisplay de errores no requiere lógica extra en la vista.

---

### [F-20] `UpdateView` con `instance=`: el mismo form hace UPDATE

@tipo: demo

# Pasar instance= al constructor es la única diferencia entre crear y editar

## Cómo UpdateView pre-popula los campos automáticamente

`UpdateView` recupera el objeto, lo asigna a `self.object`, y construye el formulario con `PostForm(instance=self.object)`. Django inicializa cada widget con el valor actual del atributo del modelo — sin código extra.

```python
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"   # mismo template que CreateView
    success_url = reverse_lazy("blog:post-list")
```

## La diferencia en el POST: instance= determina INSERT vs UPDATE

```python
# CreateView internamente hace:
form = PostForm(data=request.POST)           # sin instance
form.save()   # → INSERT INTO blog_post ...

# UpdateView internamente hace:
form = PostForm(data=request.POST, instance=self.object)   # pk ya está
form.save()   # → UPDATE blog_post SET title=... WHERE id=42
```

Sin `instance=`, `form.save()` siempre crea un objeto nuevo — el bug más común al implementar edición

---

### [F-21] Template del formulario: redisplay de errores campo por campo

@tipo: demo

# El mismo template funciona para crear y editar — el form sabe si tiene errores

## Por qué novalidate es necesario

Sin `novalidate`, el browser ejecuta su validación HTML5 y puede bloquear el envío antes de que Django procese el formulario. Con `novalidate`, Django tiene control total sobre los mensajes de error — en español, con la lógica de negocio real.

```html
<form method="post" novalidate>
  {% csrf_token %}

  {% if form.non_field_errors %}
    <div class="alert alert-danger">
      {% for e in form.non_field_errors %}{{ e }}{% endfor %}
    </div>
  {% endif %}

  {% for field in form %}
    <div class="mb-3">
      <label class="form-label fw-semibold">
        {{ field.label }}{% if field.field.required %} *{% endif %}
      </label>
      {{ field }}   <!-- widget ya tiene class="form-control" desde Meta.widgets -->
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

### [F-22] `DeleteView`: GET confirma, POST elimina — nunca al revés

@tipo: demo

# La confirmación es obligatoria: un GET sobre DeleteView jamás borra datos

## Por qué GET no puede borrar

Un enlace `<a href="/posts/42/eliminar/">` genera un GET. Si ese GET borrara el objeto, cualquier crawler o usuario que accidentalmente siga el link eliminaría datos. La eliminación siempre requiere un POST explícito con `{% csrf_token %}`.

```python
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post-list")
    # GET  → muestra template de confirmación (nunca borra)
    # POST → llama objeto.delete() → redirect a success_url
```

```html
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

---

## BLOQUE 5 — Sesiones HTTP: estado en un protocolo sin estado (8 min)

---

### [F-23] HTTP es stateless: el servidor no recuerda peticiones anteriores

@tipo: concepto-abstracto
@imagen: right-half
@prompt-imagen: dos columnas — izquierda con tres peticiones HTTP idénticas apiladas con signo de interrogación "¿quién sos?" en cada una — derecha con cookie "sessionid=abc123" en cada petición y check verde "mismo usuario identificado" — fondo blanco, paleta azul y verde

# Cada petición HTTP es anónima por diseño — las sesiones resuelven el estado

## Por qué HTTP no tiene estado y qué consecuencia tiene

HTTP es stateless para ser escalable: cualquier servidor puede responder cualquier petición sin conocer las anteriores. Pero las aplicaciones necesitan recordar: ¿está el usuario logueado?, ¿qué guardó? La solución son las sesiones del servidor.

## Cómo funciona la sesión de Django en 3 pasos

1. Django genera un `session_id` UUID único y lo guarda en una cookie `sessionid`
2. El browser envía esa cookie en **cada petición siguiente** — automáticamente
3. Django lee `sessionid`, busca los datos en BD (o caché), y los expone como `request.session` — un dict Python normal

## Qué cubrimos en esta clase (intro sin autenticación)

`request.session` como dict y el **messages framework** que lo usa internamente para el patrón PRG. Autenticación completa → Módulo VI.

---

### [F-24] `request.session` y messages: estado entre peticiones

@tipo: codigo

# request.session es un dict que persiste entre peticiones del mismo usuario

## Dos capas de la misma solución

`request.session` es el mecanismo de bajo nivel. El **messages framework** es una abstracción construida sobre sesiones para el patrón PRG: el mensaje se guarda antes del redirect y se elimina cuando el template lo renderiza.

```python
# Nivel bajo: session como dict
request.session["ultimo_post_id"] = 42         # escribe
ultimo = request.session.get("ultimo_post_id")  # lee con default seguro

# Nivel alto: messages framework — para el patrón PRG
from django.contrib import messages

class PostCreateView(CreateView):
    def form_valid(self, form):
        messages.success(self.request, "Post creado correctamente.")
        return super().form_valid(form)  # → redirect a success_url

    def form_invalid(self, form):
        messages.error(self.request, "Revisá los errores del formulario.")
        return super().form_invalid(form)
```

```html
<!-- En base.html — el mensaje aparece en la página DESPUÉS del redirect -->
{% for m in messages %}
  <div class="alert alert-{{ m.tags }}">{{ m }}</div>
{% endfor %}
```

---

## CIERRE

---

### [F-25] Mapa del Módulo V: lo que construimos en esta clase

@tipo: cierre
@imagen: background
@prompt-imagen: fondo oscuro degradado azul profundo a negro — texto blanco centrado — estilo minimalista de cierre de clase universitaria

# Cinco bloques que conectan la petición HTTP con la base de datos

## Lo que ya dominan

- **URLconf**: `path()`, conversores de tipo, `include()`, `reverse_lazy()` — el router tipado
- **dispatch() + request**: cómo Django mapea verbos HTTP a métodos Python
- **Vistas genéricas**: ListView · DetailView · CreateView · UpdateView · DeleteView
- **Templates + ORM**: contexto automático, dot notation, filtros DTL, herencia Bootstrap 5
- **Formularios**: bound/unbound · pipeline 5 capas · ModelForm · `clean_campo()` · PRG
- **Sesiones**: `request.session` como dict · messages framework

## El hilo conductor

`URL → dispatch() → ORM → Form → Template → Redirect` — cada bloque de hoy es un eslabón de esa cadena

Siguiente paso: clase práctica — BlogApp CRUD completo con vistas genéricas
