# Guía de Estudio — Módulo V: Vistas OOP, Templates y Formularios con datos ORM
## Tema 05 | IF009 Laboratorio de Programación y Lenguajes 2026

> **Para el estudiante.** Este material profundiza y extiende la clase teórica para que puedas estudiar de forma autónoma. No reemplaza la clase — la complementa.

---

## Objetivos de aprendizaje

Al finalizar el estudio de este módulo, el estudiante será capaz de:

| # | Nivel (Bloom) | Objetivo |
|---|---------------|---------|
| 1 | Comprender | Distinguir cuándo usar `View` base versus vistas genéricas, explicando el costo y beneficio de cada nivel de abstracción |
| 2 | Aplicar | Implementar `ListView` y `DetailView` con `get_queryset()` y `get_context_data()` sobre datos ORM reales |
| 3 | Aplicar | Construir templates con herencia (`{% extends %}`), paginación y filtros DTL sobre objetos de modelo |
| 4 | Construir | Implementar `CreateView` y `UpdateView` con `ModelForm` personalizado incluyendo validaciones en `clean_<campo>()` y `clean()` |
| 5 | Analizar | Trazar la pipeline completa de validación de Django (5 capas) y ubicar cada error en su capa correspondiente |
| 6 | Analizar | Distinguir formulario unbound de bound y explicar por qué `cleaned_data` solo existe después de `is_valid()` |
| 7 | Evaluar | Identificar y resolver: formulario inválido sin redisplay, N+1 en ListView, DeleteView sin confirmación |
| 8 | Aplicar | Configurar rutas con `path()`, conversores de tipo, namespaces y `reverse_lazy()` |
| 9 | Reconocer | Explicar el rol de `request.session` como mecanismo de estado en HTTP stateless |

---

## Prerrequisitos

Antes de estudiar este módulo, verificar que se dominan los contenidos del **Tema 04**:
- ORM avanzado: `filter()`, `select_related()`, `prefetch_related()`, `Q objects`
- `View` base: `dispatch()`, `get()`, `post()`, `as_view()`
- Django Template Language (DTL): herencia, partials, filtros, `{% load static %}`

---

## 1. El URLconf: el sistema de ruteo de Django

### 1.1 Concepto fundamental

El protocolo HTTP no determina qué componente Python debe ejecutarse ante una URL. Django resuelve esta pregunta con el **URLconf** (URL Configuration): un módulo Python que mapea patrones de URL a clases Python.

El URLconf opera en dos niveles:
- **URLconf raíz** (proyecto): conoce las aplicaciones y su prefijo de URL
- **URLconf de aplicación**: conoce el detalle de las rutas internas

```python
# blog_project/urls.py — URLconf raíz
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
]
```

```python
# blog/urls.py — URLconf de la aplicación
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "blog"   # define el namespace

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/crear/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/editar/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/eliminar/", PostDeleteView.as_view(), name="post-delete"),
]
```

**Tres principios de resolución**:
1. `urlpatterns` se recorre en orden — el primer patrón que coincide se ejecuta
2. `include()` consume el prefijo y transfiere el segmento restante
3. Si ningún patrón coincide → `Http404` automático

### 1.2 Conversores de tipo

Los conversores validan y convierten segmentos de URL antes de que lleguen a la vista:

| Conversor | Tipo Python | Ejemplo | Si no coincide |
|-----------|-------------|---------|----------------|
| `<int:pk>` | `int` | `/posts/42/` → `42` | `Http404` automático |
| `<str:nombre>` | `str` | `/posts/mi-titulo/` | nunca rechaza |
| `<slug:slug>` | `str` slug | `/posts/mi-post-2026/` | inválido → 404 |
| `<uuid:pk>` | `uuid.UUID` | `/posts/a3b2-.../` | inválido → 404 |

> **Importante**: el conversor valida el *tipo* de la URL, no la *existencia* del objeto en la base de datos. La existencia la verifica `get_object_or_404()` dentro de la vista.

### 1.3 Resolución inversa

Principio: nunca escribir URLs hardcodeadas en el código fuente.

```python
# En Python — reverse_lazy() en atributos de clase, reverse() en funciones
from django.urls import reverse, reverse_lazy

reverse("blog:post-detail", kwargs={"pk": 42})    # → "/blog/posts/42/"
success_url = reverse_lazy("blog:post-list")       # diferida — para atributos de clase
```

```html
<!-- En templates DTL -->
<a href="{% url 'blog:post-detail' post.pk %}">Ver publicación</a>
<a href="{% url 'blog:post-update' pk=post.pk %}">Editar</a>
```

**Por qué `reverse_lazy()` en atributos de clase**: los atributos se evalúan en tiempo de importación del módulo, antes de que Django haya cargado el sistema de URLs. `reverse_lazy()` difiere la evaluación al momento de uso real.

### 1.4 Ejercicio de autoevaluación — URLconf

1. ¿Qué ocurre si se visita `/blog/posts/abc/` con el patrón `posts/<int:pk>/`?
2. ¿Cuál es la diferencia entre definir `namespace="blog"` en `include()` y definir `app_name = "blog"` en la aplicación? ¿Son equivalentes? ¿Se necesitan ambos?
3. ¿Por qué `success_url = reverse("blog:post-list")` lanzaría un error en import time?
4. Escribir el tag DTL para generar el enlace a `PostDeleteView` para el post con `pk=7`.

---

## 2. El controlador View: dispatch y vistas genéricas

### 2.1 El patrón MVT de Django

Django implementa el patrón MVT (Model-View-Template), una adaptación de MVC:

| Capa MVC | Equivalente Django | Responsabilidad |
|----------|-------------------|----------------|
| Modelo | `models.py` + ORM | Estado y persistencia |
| Controlador | `views.py` — clases `View` | Lógica de negocio y orquestación |
| Vista | `templates/` — DTL | Presentación al usuario |

La **Vista de Django** es el controlador: recibe la `HttpRequest`, consulta el modelo, construye el contexto y delega la presentación al template.

### 2.2 El mecanismo dispatch()

`dispatch()` determina qué método ejecutar según el verbo HTTP:

```python
# Implementación real simplificada — Django 5.1
class View:
    def dispatch(self, request, *args, **kwargs):
        method = request.method.lower()          # "get" | "post" | ...
        handler = getattr(self, method, self.http_method_not_allowed)
        return handler(request, *args, **kwargs)
```

Este mecanismo explica por qué:
- Definir `get()` en una subclase responde solo a peticiones GET
- Definir `post()` responde solo a peticiones POST
- Si se hace una petición DELETE a una vista que no define `delete()` → 405 automático

### 2.3 El objeto request

`HttpRequest` encapsula toda la información de la petición entrante:

```python
request.method          # "GET" | "POST" — siempre mayúsculas
request.path            # "/blog/posts/42/"
request.GET             # QueryDict — parámetros de URL: ?page=2 → {"page": "2"}
request.POST            # QueryDict — cuerpo del formulario (solo POST/PUT)
request.user            # User autenticado o AnonymousUser
request.session         # diccionario de sesión persistente
request.META            # diccionario de cabeceras HTTP
```

> `request.POST` es **inmutable**. Para agregar datos al formulario antes de guardarlo: `form.instance.campo = valor` antes de `form.save()`.

### 2.4 Jerarquía de vistas genéricas

```
View (base)
├── TemplateView       — página estática con contexto
├── ListView           — lista de objetos + paginación
├── DetailView         — un objeto por pk/slug + Http404
├── CreateView         — formulario → INSERT + redirect
├── UpdateView         — formulario con instance= → UPDATE + redirect
└── DeleteView         — confirmación GET / eliminación POST
```

Todas extienden `View`. Quien comprende `View` puede leer y entender el código fuente de cualquier vista genérica.

### 2.5 ListView con ORM

```python
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"   # nombre en el template (default: object_list)
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(published=True)\
                           .select_related("author", "category")\
                           .order_by("-created_at")
```

**Paginación automática**: con `paginate_by=10`, el template recibe automáticamente:
- `page_obj`: objeto de paginación con `has_next()`, `has_previous()`, `next_page_number()`
- `paginator`: objeto `Paginator` con `count`, `num_pages`
- `is_paginated`: `True` si hay más de una página

### 2.6 Ejercicio de autoevaluación — Vistas

1. ¿Cuál es la diferencia entre sobreescribir `dispatch()` y sobreescribir `get()`?
2. Una `ListView` sin `context_object_name` definido: ¿qué nombre tendrá la variable en el template?
3. ¿Qué método sobreescribir para agregar una variable extra al contexto de una `DetailView`?
4. Escribir una `DetailView` que use `select_related('author', 'category')` y agregue al contexto los últimos 3 posts relacionados por categoría.

---

## 3. Templates con QuerySets reales

### 3.1 Contexto automático

Cada vista genérica inyecta variables al contexto del template:

| Vista | Variables automáticas |
|-------|----------------------|
| `ListView` | `object_list`, `page_obj`, `paginator`, `is_paginated` |
| `DetailView` | `object` (y alias de `context_object_name`) |
| `CreateView` / `UpdateView` | `form` |
| `DeleteView` | `object` |

**Extensión del contexto**:
```python
def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)  # SIEMPRE llamar super()
    ctx["categorias"] = Category.objects.all()
    return ctx
```

> Omitir `super()` elimina todas las variables automáticas del contexto.

### 3.2 Dot notation sobre modelos

Django resuelve `post.author.username` recorriendo la cadena de atributos:

```html
{{ post.title|upper }}
{{ post.created_at|date:"d/m/Y" }}
{{ post.body|truncatewords:50 }}
{{ post.author.get_full_name|default:"Anónimo" }}
{{ post.category.name }}

{% for comment in post.comments.all %}
  {{ comment.author.username }}: {{ comment.body }}
{% endfor %}
```

**El problema N+1**: `post.comments.all` dentro de `{% for post in posts %}` ejecuta una query por cada post. Con 100 posts → 101 queries. Solución en la vista:

```python
def get_queryset(self):
    return Post.objects.prefetch_related("comments").order_by("-created_at")
```

`prefetch_related("comments")` ejecuta exactamente una query extra que precarga todos los comentarios.

### 3.3 Herencia de templates

`base.html` define la estructura; cada página hija solo sobreescribe los bloques:

```html
<!-- base.html — una sola vez -->
{% block content %}{% endblock %}

<!-- post_list.html — hereda todo lo demás -->
{% extends "blog/base.html" %}
{% block content %}
  {% for post in posts %}
    <article>{{ post.title }}</article>
  {% endfor %}
{% endblock %}
```

**Regla**: `{% extends %}` debe ser la primera línea del archivo.

### 3.4 Ejercicio de autoevaluación — Templates

1. ¿Qué filtro DTL usar para mostrar los primeros 30 palabras del cuerpo de un post?
2. ¿Por qué `post.comments.all` en un template puede generar problemas de rendimiento?
3. ¿Qué pasa si en un template hijo se escribe contenido fuera de un bloque `{% block %}`?
4. Escribir el template de paginación Bootstrap 5 para una `ListView` con `paginate_by`.

---

## 4. Formularios Django: ciclo de enlace y validación

### 4.1 El ciclo de enlace

Un formulario tiene dos estados posibles:

**Unbound** (sin datos del usuario):
```python
form = PostForm()              # GET — mostrar formulario vacío
form = PostForm(instance=post) # GET — pre-poblar para edición
form.is_bound   # False
form.is_valid() # siempre False — no ejecuta validación
```

**Bound** (con datos del usuario):
```python
form = PostForm(data=request.POST)                      # POST — crear
form = PostForm(data=request.POST, instance=post)       # POST — editar
form.is_bound   # True
form.is_valid() # ejecuta el pipeline completo
```

> **Regla fundamental**: `is_valid()` solo tiene sentido en un formulario bound. Invocarla sobre un formulario unbound siempre retorna `False` sin ejecutar lógica alguna.

### 4.2 La pipeline de validación — 5 capas

`form.is_valid()` ejecuta esta secuencia. Si una capa falla, el campo queda inválido y las capas posteriores no se ejecutan para ese campo:

```
Capa 1 — to_python():    "42" → int(42)  |  "2026-05-12" → date(...)
Capa 2 — validate():     required, max_length, EmailField, URLField...
Capa 3 — run_validators(): validators=[MinLengthValidator(10), ...]
Capa 4 — clean_<campo>(): lógica personalizada — puede consultar ORM
Capa 5 — clean():        validación cruzada entre múltiples campos
```

Resultado:
- `is_valid() = True` → `form.cleaned_data` contiene los valores limpios
- `is_valid() = False` → `form.errors` contiene los mensajes de error por campo

> **Punto crítico**: `cleaned_data` solo existe después de invocar `is_valid()`. Acceder antes produce `AttributeError`.

### 4.3 ModelForm

`ModelForm` genera campos de formulario automáticamente a partir del modelo:

```python
# blog/forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ["title", "body", "category", "published"]
        widgets = {
            "title":    forms.TextInput(attrs={"class": "form-control"}),
            "body":     forms.Textarea(attrs={"class": "form-control", "rows": 8}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
        labels        = {"title": "Título", "body": "Contenido"}
        error_messages = {"title": {"required": "El título es obligatorio."}}
```

| Campo del modelo | Campo generado |
|-----------------|----------------|
| `CharField(max_length=200)` | `CharField(max_length=200, widget=TextInput)` |
| `ForeignKey(Category)` | `ModelChoiceField(queryset=Category.objects.all())` |
| `DateTimeField(auto_now_add=True)` | **excluido** — no editable |

> **Nunca usar** `fields = '__all__'` en producción: expone campos internos como `author`, `created_at`.

### 4.4 Validación personalizada — Capa 4

```python
def clean_title(self):
    title = self.cleaned_data["title"].strip()  # ya tipado y validado por capas 1-3

    if len(title) < 10:
        raise forms.ValidationError(
            "Mínimo %(min)s caracteres.", params={"min": 10}
        )

    qs = Post.objects.filter(title__iexact=title)
    if self.instance.pk:           # excluir instancia actual en edición
        qs = qs.exclude(pk=self.instance.pk)
    if qs.exists():
        raise forms.ValidationError("Ya existe una publicación con ese título.")

    return title   # OBLIGATORIO — si se omite, cleaned_data["title"] = None
```

> **Error silencioso**: olvidar `return title` produce un campo `None` en `cleaned_data` aunque la validación fue exitosa. Django no avisa.

### 4.5 Validación cruzada — Capa 5

```python
def clean(self):
    cleaned = super().clean()

    body      = cleaned.get("body", "")        # .get() — nunca cleaned["body"]
    published = cleaned.get("published", False)

    if published and len(body) < 100:
        self.add_error("body",                 # error asociado al campo específico
            "Para publicar: mínimo 100 caracteres.")

    return cleaned
```

> En `clean()`, usar siempre `.get()` sobre `cleaned_data`. Si un campo falló en la Capa 4, su clave no existe en `cleaned_data` y el acceso directo con `[]` lanza `KeyError`.

### 4.6 El patrón PRG (Post-Redirect-Get)

```
GET  /posts/crear/   → form = PostForm()          → render (200) formulario vacío
POST /posts/crear/
  ├─ datos inválidos → form = PostForm(data=POST) → render (200) form con errores
  └─ datos válidos   → form.save() INSERT         → redirect (302) success_url
                                                            ↓
GET  /blog/          ← navegador sigue el 302 ←──────── HttpResponse(302)
```

**Por qué redirect y no render en el caso válido**: si se renderiza directamente tras un POST exitoso y el usuario recarga la página (F5), el navegador reenvía el formulario, generando una inserción duplicada. La redirección convierte el POST en un GET idempotente.

### 4.7 CreateView y UpdateView

```python
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post-list")

    def form_valid(self, form):
        form.instance.author = self.request.user   # asignar antes de save()
        messages.success(self.request, "Publicación creada.")
        return super().form_valid(form)
```

```python
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"   # mismo template que CreateView
    success_url = reverse_lazy("blog:post-list")
```

**La diferencia entre CreateView y UpdateView**: `UpdateView` construye el formulario con `PostForm(data=request.POST, instance=self.object)`. El parámetro `instance=` hace que `form.save()` emita `UPDATE` en lugar de `INSERT`.

### 4.8 Template del formulario con manejo de errores

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
      <label class="form-label">{{ field.label }}</label>
      {{ field }}
      {% for error in field.errors %}
        <div class="text-danger small">{{ error }}</div>
      {% endfor %}
    </div>
  {% endfor %}

  <button type="submit" class="btn btn-primary">Guardar</button>
</form>
```

**`novalidate`**: desactiva la validación HTML5 del navegador, dejando el control completo a Django. Sin este atributo, el navegador puede bloquear el POST con mensajes en inglés antes de que Django lo procese.

### 4.9 DeleteView

```python
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post-list")
    # GET  → template de confirmación (nunca elimina)
    # POST → objeto.delete() → redirect
```

> Un enlace `<a href="/posts/42/eliminar/">` genera un GET. Si ese GET eliminara datos, cualquier agente de indexación o acceso accidental provocaría pérdida de datos. Las operaciones destructivas siempre requieren POST.

### 4.10 Ejercicio de autoevaluación — Formularios

1. Un estudiante escribe `form = PostForm()` y luego `form.is_valid()` en una vista GET. ¿Qué retorna `is_valid()` y por qué?
2. ¿Qué ocurre si en `clean_title()` se olvida el `return title` al final?
3. En `clean()`, ¿por qué se usa `cleaned.get("body", "")` en lugar de `cleaned["body"]`?
4. ¿Cuándo `form.save()` emite INSERT y cuándo UPDATE?
5. Implementar un `ModelForm` para el modelo `Comment` con validación en `clean_body()` que rechace comentarios de menos de 10 caracteres.
6. Explicar qué problema resuelve el patrón PRG y en qué caso podría no necesitarse.

---

## 5. Sesiones HTTP: persistencia de estado

### 5.1 HTTP stateless y el problema del estado

HTTP es un protocolo sin estado (*stateless*): cada petición es independiente. El servidor no recuerda si la petición anterior vino del mismo cliente. Esta característica hace la web escalable, pero genera la necesidad de mecanismos para recordar información entre peticiones.

**El mecanismo de sesiones en tres pasos**:
1. Django genera un UUID de sesión y lo envía en la cookie `sessionid`
2. El navegador envía esa cookie en cada petición subsiguiente
3. Django lee `sessionid`, recupera los datos del servidor y los expone como `request.session`

> La cookie solo contiene el identificador. Los datos reales residen en el servidor (tabla `django_session` en la base de datos por defecto).

### 5.2 request.session como diccionario

```python
# Escritura
request.session["ultimo_post_id"] = 42
request.session["filtro_activo"] = "tecnologia"

# Lectura con valor por defecto
ultimo = request.session.get("ultimo_post_id")
filtro = request.session.get("filtro_activo", "todos")

# Eliminación
del request.session["filtro_activo"]
```

### 5.3 El messages framework

`django.contrib.messages` es una abstracción sobre sesiones para el patrón PRG:

```python
from django.contrib import messages

class PostCreateView(CreateView):
    def form_valid(self, form):
        messages.success(self.request, "Publicación creada correctamente.")
        return super().form_valid(form)   # → redirect

    def form_invalid(self, form):
        messages.error(self.request, "Se detectaron errores en el formulario.")
        return super().form_invalid(form)
```

En `base.html`:
```html
{% for m in messages %}
  <div class="alert alert-{{ m.tags }}">{{ m }}</div>
{% endfor %}
```

El mensaje se guarda en la sesión antes del redirect y se elimina automáticamente tras ser renderizado — exactamente una vez.

### 5.4 Alcance de este módulo vs. Módulo VI

| Concepto | Tema 05 | Módulo VI |
|----------|---------|-----------|
| `request.session` | ✅ | — |
| Messages framework | ✅ | — |
| Login / logout / autenticación | ❌ | ✅ |
| `LoginRequiredMixin` | ❌ | ✅ |
| Permisos en vistas | ❌ | ✅ |

### 5.5 Ejercicio de autoevaluación — Sesiones

1. ¿Por qué HTTP es un protocolo sin estado y qué ventaja tiene ese diseño?
2. ¿Qué contiene la cookie `sessionid` que Django envía al navegador?
3. ¿Cuándo se elimina un mensaje del messages framework?
4. Escribir la vista `PostCreateView` completa con `form_valid()` que: (a) asigne `request.user` como autor, (b) envíe un mensaje de éxito, (c) haga redirect a la lista.

---

## 6. Errores frecuentes y cómo resolverlos

| Síntoma | Causa probable | Solución |
|---------|---------------|---------|
| Template muestra `object_list` vacío | No se definió `context_object_name` | Agregar `context_object_name = "posts"` |
| `page_obj` no disponible en template | `super()` omitido en `get_context_data()` | Llamar `super().get_context_data(**kwargs)` primero |
| N+1 queries al acceder a `post.category.name` | Sin `select_related` en `get_queryset()` | Agregar `.select_related("category")` |
| `AttributeError: 'PostForm' has no attribute 'cleaned_data'` | Acceso a `cleaned_data` antes de `is_valid()` | Acceder solo después de `form.is_valid()` |
| `form.save()` crea duplicado en UpdateView | Faltó `instance=self.object` | `PostForm(data=request.POST, instance=self.object)` |
| `reverse()` lanza error en import | Usado en atributo de clase | Reemplazar con `reverse_lazy()` |
| Campo queda `None` en BD aunque el form es válido | Faltó `return` en `clean_<campo>()` | Siempre retornar el valor al final |
| `KeyError` en `clean()` | Acceso directo `cleaned["campo"]` | Usar `cleaned.get("campo", default)` |
| Formulario no muestra errores al usuario | Falta el loop `{% for error in field.errors %}` | Agregar el loop en el template |
| `403 Forbidden` en POST | Falta `{% csrf_token %}` en el formulario | Agregar `{% csrf_token %}` dentro de `<form>` |
| `NoReverseMatch` en template | Namespace incorrecto o faltante | Verificar `app_name = "blog"` y usar `'blog:nombre'` |

---

## 7. Resumen conceptual

```
URL → URLconf → dispatch() → ORM → Form → Template → Redirect
 ↑        ↑          ↑         ↑      ↑        ↑         ↑
path()  include()  get()/   select_  is_    {% block %} PRG
slug     namespace  post()  related  valid   extends   302→GET
uuid     reverse_                    clean_  {% url %}
         lazy()                      campo() novalidate
```

**Cinco conceptos que integran el módulo**:

1. **URLconf tipado**: la URL llega a la vista con tipos Python validados, no strings crudos
2. **dispatch()**: el mecanismo de despacho HTTP → método Python
3. **Vistas genéricas**: encapsulan el patrón, exponen puntos de extensión (`get_queryset`, `get_context_data`, `form_valid`)
4. **Pipeline de 5 capas**: la validación es secuencial; `cleaned_data` es el resultado exitoso
5. **PRG**: el ciclo correcto de un formulario — GET vacío → POST inválido (render) → POST válido (redirect)
