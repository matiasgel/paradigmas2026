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

El ORM constituye la capa de persistencia del sistema.
En este módulo se expone la información al usuario mediante **vistas, templates y formularios**.

Semana 9 · BlogApp · Django 5.1 · Bootstrap 5.3.3

---

## BLOQUE 1 — URLconf: el router de Django (20 min)

---

### [F-01] El URLconf: primer componente que Django ejecuta ante una petición

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama horizontal con tres bloques — "Browser: GET /posts/42/" → caja "URLconf: recorre urlpatterns en orden, primer match gana" → "PostDetailView(pk=42)" — etiqueta inferior "si ningún patrón hace match → Http404 automático" — fondo blanco, bordes redondeados, flechas gruesas

# El protocolo HTTP no determina qué código Python ejecutar — el URLconf lo hace

## Función del URLconf en la arquitectura de Django

El protocolo HTTP no dispone de mecanismo alguno para determinar qué componente Python debe ejecutarse ante una URL dada. El URLconf opera como tabla de despacho: URL → clase Python. Se implementa como un módulo Python ordinario, sin dependencia de XML, anotaciones externas ni convenciones implícitas.

## Tres principios del sistema de resolución

- La lista `urlpatterns` se recorre **en orden** — el primer patrón que produce coincidencia se ejecuta
- Django **consume** el prefijo en `include()` y transfiere el segmento restante al URLconf de la aplicación
- Si ningún patrón produce coincidencia → `Http404` automático, sin intervención de la vista

## Información transferida de la URL a la vista

`path("posts/<int:pk>/", ...)` extrae `pk=42` como `int` — la vista lo recibe en `self.kwargs["pk"]` ya convertido al tipo destino

---

### [F-02] Dos niveles de urls.py: proyecto y aplicación

@tipo: codigo

# El proyecto delega la resolución — la aplicación es responsable de sus propias rutas

## Fundamento del diseño en dos niveles

El URLconf raíz solo tiene conocimiento de que las rutas bajo `/blog/` pertenecen a la aplicación `blog`. La aplicación define su propia tabla de rutas de forma autónoma. Si en el futuro la aplicación se reubica bajo `/articulos/`, únicamente se modifica **una línea** en el proyecto raíz.

```python
# blog_project/urls.py  ← URLconf raíz
from django.urls import path, include
urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    # Django consume "blog/" y transfiere el resto: "/posts/42/" → "posts/42/"
]
```

```python
# blog/urls.py  ← URLconf de la aplicación
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

app_name = "blog"   # habilita el espacio de nombres → {% url 'blog:post-list' %}

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/crear/", PostCreateView.as_view(), name="post-create"),
]
```

---

### [F-03] Conversores de tipo: validación en la capa de ruteo

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

### [F-04] Resolución inversa: el principio de indirección de URLs

@tipo: concepto-mixto
@imagen: none

# Las URLs no deben escribirse directamente en el código fuente

## El problema del acoplamiento directo

Si la URL cambia de `/posts/42/` a `/articulos/42/`, sería necesario localizar y reemplazar todas las ocurrencias en el proyecto. La resolución inversa desacopla el código de la estructura de URLs: se referencia por nombre y el framework genera la cadena de URL correspondiente.

```python
# views.py / models.py — resolución en Python
from django.urls import reverse, reverse_lazy

reverse("blog:post-detail", kwargs={"pk": 42})  # → "/blog/posts/42/"

# reverse_lazy(): versión diferida — obligatoria en atributos de clase,
# ya que los atributos se evalúan en tiempo de importación, antes de que
# el sistema de URLs esté completamente inicializado
success_url = reverse_lazy("blog:post-list")
```

```html
<!-- templates/ — resolución en Django Template Language -->
<a href="{% url 'blog:post-detail' post.pk %}">Ver publicación</a>
<a href="{% url 'blog:post-update' pk=post.pk %}">Editar</a>
```

**Convención obligatoria**: `{% url %}` en templates · `reverse_lazy()` en clases · `reverse()` en funciones

---

## BLOQUE 2 — El controlador View: dispatch y vistas genéricas (35 min)

---

### [F-05] Django MVT: la "Vista" cumple el rol del controlador

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

### [F-06] Ciclo completo de una petición HTTP en Django

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama vertical de flujo con 6 cajas apiladas — "Browser GET /posts/42/" → "Middleware Stack (CSRF, Session)" → "URL Resolver → pk=42" → "View.dispatch() → get()" → "ORM: Post.objects.get(pk=42)" → "Template Engine → HTML" → "HttpResponse 200" — colores distintos por capa, fondo blanco

# Seis capas transforman una URL en un documento HTML

## Función de cada capa en el ciclo de procesamiento

- **Middleware**: intercepta la petición antes de su despacho y la respuesta antes de su envío — aquí reside el control CSRF y la gestión de sesiones
- **URL Resolver**: extrae `pk=42` como `int` e instancia la clase de vista correspondiente
- **dispatch()**: determina si delegar en `get()` o `post()` según `request.method`
- **ORM**: retorna objetos Python — el template nunca ejecuta SQL de forma directa
- **Template Engine**: combina el template DTL con el contexto y produce el HTML final

## Punto de extensión por capa

En cada capa existe un método que puede ser sobreescrito. En esta clase se utilizan `get_queryset()`, `get_context_data()`, `form_valid()` y `clean_<campo>()`.

---

### [F-07] `dispatch()`: el despachador interno de la Vista

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

### [F-08] El objeto `request`: representación completa de la petición HTTP

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

### [F-09] Jerarquía de vistas genéricas: reutilización de patrones consolidados

@tipo: concepto-abstracto
@imagen: right-half
@prompt-imagen: árbol de herencia con cajas — raíz "View" en gris, segundo nivel "TemplateView / ListView / DetailView" en azul, tercer nivel "CreateView / UpdateView / DeleteView" en verde — etiquetas cortas: "dispatch manual", "lista + pagina", "un objeto", "INSERT", "UPDATE", "DELETE" — fondo blanco, tipografía monospace

# Cada vista genérica encapsula el patrón más frecuente de su operación correspondiente

## Fundamento del uso de vistas genéricas sobre la clase base View

Con la clase base `View`, toda la lógica debe implementarse manualmente: recuperar el objeto, construir el contexto, renderizar la respuesta. Las vistas genéricas encapsulan ese código repetitivo y exponen puntos de extensión bien definidos. El código resultante en la subclase expresa **qué cambia**, en lugar de describir el funcionamiento del patrón.

## Las cinco vistas utilizadas en BlogApp

- **`ListView`**: `Post.objects.all()` + paginación automática mediante `paginate_by`
- **`DetailView`**: `Post.objects.get(pk=pk)` + `Http404` automático si el objeto no existe
- **`CreateView`**: formulario unbound → bound → `save()` INSERT → redirección
- **`UpdateView`**: idéntico a CreateView pero con `instance=objeto` → `save()` UPDATE
- **`DeleteView`**: GET presenta confirmación — POST ejecuta `objeto.delete()`

---

### [F-10] `ListView` con `get_queryset()`: integración del ORM en la vista

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

### [F-11] Contexto automático: las vistas genéricas inyectan variables sin declaración explícita

@tipo: tabla

# Las vistas genéricas transfieren variables al template de forma implícita

## Importancia del conocimiento de las variables automáticas de contexto

Si se referencia `{{ posts }}` en el template y la variable no se resuelve, la causa más frecuente es no haber definido `context_object_name`, de modo que Django empleó `object_list` como nombre por defecto. El conocimiento de las variables automáticas permite evitar esta clase de errores.

| Vista | Variables automáticas en el contexto |
|-------|--------------------------------------|
| `ListView` | `object_list`, `page_obj`, `paginator`, `is_paginated` |
| `DetailView` | `object` (y el alias definido en `context_object_name`) |
| `CreateView` / `UpdateView` | `form` (instancia del formulario) |
| `DeleteView` | `object` (el objeto candidato a eliminación) |

## Incorporación de variables adicionales sin pérdida del contexto automático

```python
def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)  # obligatorio: preserva las variables automáticas
    ctx["categorias"] = Category.objects.all()
    ctx["total"] = self.get_queryset().count()
    return ctx
```

**Omitir `super()`** produce la pérdida del contexto automático — `page_obj`, `form`, etc. dejan de estar disponibles en el template

---

### [F-12] Django Template Language sobre datos ORM: dot notation y relaciones

@tipo: codigo

# El template accede a atributos, propiedades, métodos y relaciones mediante dot notation

## Mecanismo de resolución de dot notation sobre instancias de modelo

Django resuelve `post.author.username` en tres pasos: accede al atributo `author` del objeto `Post` (ForeignKey → consulta ORM si no existe caché), luego accede al atributo `username` del objeto `User`. Si algún paso retorna `None`, el resultado es una cadena vacía, sin que se produzca excepción alguna.

```html
{{ post.title|upper }}
{{ post.created_at|date:"d/m/Y" }}
{{ post.body|truncatewords:50 }}
{{ post.author.get_full_name|default:"Anónimo" }}

<!-- Relación FK — dot notation ejecuta la consulta si no existe select_related -->
{{ post.category.name }}

<!-- Relación inversa (reverse FK / M2M) -->
{% for comment in post.comments.all %}
  {{ comment.author.username }}: {{ comment.body }}
{% endfor %}
```

**Problema N+1**: `post.comments.all` dentro de un `{% for posts %}` ejecuta una consulta por cada post. Solución: `prefetch_related("comments")` en `get_queryset()` — los datos se reciben precargados en el template.

---

### [F-13] Herencia de templates: base.html y extensión con datos ORM

@tipo: demo

# Un template base define la estructura del documento — las páginas hijas aportan el contenido específico

## La herencia de templates como mecanismo de reutilización estructural

En ausencia de herencia, cada template replicaría la estructura completa: `<head>`, `<nav>` y pie de página. Mediante `{% extends %}` y `{% block %}`, el HTML estructural reside en un único archivo. Cualquier modificación en la barra de navegación requiere editar un único archivo.

```html
<!-- templates/blog/base.html — definición única para toda la aplicación -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
<nav class="navbar navbar-dark bg-dark">
  <a class="navbar-brand" href="{% url 'blog:post-list' %}">BlogApp</a>
  <a class="nav-link" href="{% url 'blog:post-create' %}">Nueva publicación</a>
</nav>
<div class="container mt-4">
  {% if messages %}
    {% for m in messages %}<div class="alert alert-{{ m.tags }}">{{ m }}</div>{% endfor %}
  {% endif %}
  {% block content %}{% endblock %}   <!-- cada template hijo proporciona este bloque -->
</div>
```

```html
<!-- templates/blog/post_detail.html — únicamente el contenido específico -->
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

### [F-14] El ciclo de enlace: estado bound vs unbound

@tipo: concepto-abstracto
@imagen: right-half
@prompt-imagen: dos cajas lado a lado — izquierda "UNBOUND: GET /crear/ → campos vacíos → render" — derecha "BOUND: POST /crear/ → is_valid()=True → save() → redirect" y "is_valid()=False → redisplay con errores" — bifurcación con flechas verde y roja — fondo blanco

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

### [F-15] Pipeline de validación: las cinco capas de procesamiento en secuencia

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama vertical con 5 rectángulos apilados por flechas — "1 to_python(): string HTTP → tipo Python" → "2 validate(): required, max_length" → "3 run_validators(): lista validators=[]" → "4 clean_campo(): lógica custom + ORM" → "5 clean(): validación cruzada" — bifurcación final verde "cleaned_data" y roja "form.errors"

# `form.is_valid()` ejecuta esta cadena de procesamiento — si una capa falla, la ejecución se detiene

## Función de cada capa y relevancia del orden de ejecución

1. **`to_python()`** — convierte el string recibido por POST al tipo Python destino: `"42"` → `int(42)`. Si la conversión falla, el campo queda inválido y las capas posteriores se omiten para ese campo.
2. **`validate()`** — aplica las reglas declaradas en el campo: `required`, `max_length`, `min_value`, etc.
3. **`run_validators()`** — ejecuta la lista `validators=[MinLengthValidator(10), ...]` definida en el campo.
4. **`clean_<campo>()`** — lógica personalizada: permite consultar el ORM, transformar el valor y lanzar `ValidationError`.
5. **`clean()`** — validación cruzada entre campos; `self.cleaned_data` contiene únicamente los campos que superaron las capas 1 a 4.

**`cleaned_data`** solo existe a partir de que `is_valid()` haya sido invocado — acceder con anterioridad produce `AttributeError`

---

### [F-16] `ModelForm`: generación automática de campos a partir del modelo

@tipo: codigo

# ModelForm inspecciona el modelo y genera los campos correspondientes, sin duplicar definiciones

## Ventaja de ModelForm sobre la clase Form base

Con `Form` sería necesario declarar `title = forms.CharField(max_length=200)`, duplicando lo que ya está definido en el modelo. `ModelForm` inspecciona el modelo y genera el campo de forma automática. Ante modificaciones en el modelo, el formulario se actualiza sin intervención adicional.

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
| `DateTimeField(auto_now_add=True)` | **excluido** — no editable por el usuario |

---

### [F-17] Capa 4: `clean_<campo>()` — validación con acceso al ORM

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

### [F-18] Capa 5: `clean()` — validación cruzada entre campos

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

### [F-19] Ciclo completo: GET → POST inválido → POST válido → Redirección

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

### [F-20] `UpdateView` con `instance=`: el mismo formulario produce UPDATE

@tipo: demo

# El parámetro instance= es el único factor que distingue la creación de la edición

## Mecanismo de pre-población de campos en UpdateView

`UpdateView` recupera el objeto, lo asigna a `self.object` y construye el formulario con `PostForm(instance=self.object)`. Django inicializa cada widget con el valor actual del atributo correspondiente en el modelo — sin código adicional.

```python
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"   # mismo template que CreateView
    success_url = reverse_lazy("blog:post-list")
```

## El parámetro instance= determina INSERT vs UPDATE

```python
# CreateView: formulario sin instancia asociada
form = PostForm(data=request.POST)
form.save()   # → INSERT INTO blog_post ...

# UpdateView: formulario con instancia asociada (pk existente)
form = PostForm(data=request.POST, instance=self.object)
form.save()   # → UPDATE blog_post SET title=... WHERE id=42
```

Sin `instance=`, `form.save()` siempre genera un nuevo registro — el defecto más frecuente al implementar la funcionalidad de edición

---

### [F-21] Template del formulario: presentación de errores por campo

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

### [F-22] `DeleteView`: GET solicita confirmación, POST ejecuta la eliminación

@tipo: demo

# La confirmación explícita es obligatoria: una petición GET sobre DeleteView no elimina datos

## Por qué las operaciones destructivas requieren POST y no GET

Un enlace `<a href="/posts/42/eliminar/">` genera una petición GET. Si dicha petición eliminara el objeto, cualquier agente de indexación o usuario que acceda al enlace de forma accidental provocaría la pérdida de datos. La eliminación requiere invariablemente un POST explícito que incluya el token `{% csrf_token %}`.

```python
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post-list")
    # GET  → renderiza el template de confirmación (nunca elimina datos)
    # POST → invoca objeto.delete() → redirección a success_url
```

```html
{% extends "blog/base.html" %}
{% block content %}
<div class="alert alert-warning">
  <h4>¿Eliminar "{{ object.title }}"?</h4>
  <p>Esta operación no puede revertirse.</p>
  <form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Confirmar eliminación</button>
    <a href="{% url 'blog:post-list' %}" class="btn btn-secondary">Cancelar</a>
  </form>
</div>
{% endblock %}
```

---

## BLOQUE 5 — Sesiones HTTP: persistencia de estado en un protocolo sin estado (8 min)

---

### [F-23] HTTP es stateless: el protocolo no conserva estado entre peticiones

@tipo: concepto-abstracto
@imagen: right-half
@prompt-imagen: dos columnas — izquierda con tres peticiones HTTP idénticas apiladas con signo de interrogación "¿quién sos?" en cada una — derecha con cookie "sessionid=abc123" en cada petición y check verde "mismo usuario identificado" — fondo blanco, paleta azul y verde

# Cada petición HTTP es anónima por diseño — el mecanismo de sesiones resuelve la persistencia de estado

## HTTP como protocolo sin estado y sus implicaciones para las aplicaciones web

HTTP es un protocolo sin estado (*stateless*) por razones de escalabilidad: cualquier servidor puede responder cualquier petición sin conocimiento de las anteriores. Sin embargo, las aplicaciones requieren persistir información entre peticiones: estado de autenticación, preferencias del usuario, datos de sesión de trabajo, entre otros. El mecanismo provisto por Django son las sesiones en el servidor.

## Funcionamiento de la sesión de Django en tres pasos

1. Django genera un identificador de sesión UUID único y lo almacena en una cookie `sessionid`
2. El navegador envía esa cookie en **cada petición subsiguiente** — de forma automática
3. Django lee `sessionid`, recupera los datos asociados en la base de datos (o caché) y los expone como `request.session` — un diccionario Python estándar

## Alcance de esta clase

`request.session` como diccionario y el **messages framework** que lo utiliza internamente para el patrón PRG. La autenticación completa se aborda en el Módulo VI.

---

### [F-24] `request.session` y el messages framework: persistencia entre peticiones

@tipo: codigo

# request.session es un diccionario que persiste entre peticiones del mismo usuario

## Dos niveles de abstracción sobre el mismo mecanismo

`request.session` es el mecanismo de bajo nivel. El **messages framework** es una abstracción construida sobre sesiones para un caso específico del patrón PRG: el mensaje se persiste antes de la redirección y se descarta una vez que el template lo ha renderizado.

```python
# Nivel de acceso directo: session como diccionario
request.session["ultimo_post_id"] = 42         # escritura
ultimo = request.session.get("ultimo_post_id")  # lectura con valor por defecto

# Nivel de abstracción: messages framework — para el patrón PRG
from django.contrib import messages

class PostCreateView(CreateView):
    def form_valid(self, form):
        messages.success(self.request, "Publicación creada correctamente.")
        return super().form_valid(form)  # → redirección a success_url

    def form_invalid(self, form):
        messages.error(self.request, "Se han detectado errores en el formulario.")
        return super().form_invalid(form)
```

```html
{# En base.html — el mensaje se presenta en la página posterior a la redirección #}
{% for m in messages %}
  <div class="alert alert-{{ m.tags }}">{{ m }}</div>
{% endfor %}
```

---

## CIERRE

---

### [F-25] Síntesis del Módulo V: conexión entre la petición HTTP y la base de datos

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
