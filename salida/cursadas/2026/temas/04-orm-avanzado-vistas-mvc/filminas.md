# Filminas — Tema 04
## ORM avanzado + puente a interfaz MVC
### IF009 · UNTDF · 2026 · Semana 8

---

## CLASE TEÓRICA (180 min)

---

### [F-00] Portada

@tipo: portada
@imagen: background
@prompt-imagen: ilustración minimalista de capas apiladas (base de datos → modelo Python → vista HTTP → navegador) conectadas por flechas, fondo oscuro azul profundo, estética profesional académica

# ORM avanzado + puente a interfaz MVC

Módulo IV avanzado · Módulo V intro — Semana 8

---

### [F-01] ¿Qué ya sabés? ¿Qué viene hoy?

@tipo: tabla-comparativa

# Puente pedagógico: de la práctica anterior a hoy

## Ya sabés (orm.pdf — Biblioteca)

| Concepto | Ya visto |
|----------|---------|
| `filter()`, `get()`, `order_by()` | ✅ |
| `.save()`, `.delete()` | ✅ |
| Managers con `get_queryset()` | ✅ |
| Métodos de instancia | ✅ |

## Hoy agregamos (BlogApp)

| Concepto | Nuevo |
|----------|-------|
| Lazy evaluation y caché | 🆕 |
| Q objects, F expressions | 🆕 |
| `annotate()`, `aggregate()` | 🆕 |
| N+1 → `select_related` | 🆕 |
| CBV `View` + DTL completo | 🆕 |

---

## BLOQUE T1 — QuerySet API: de lo básico a lo profesional

---

### [F-02] ¿Qué es un QuerySet realmente?

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama conceptual mostrando un QuerySet como objeto diferido en Python — caja etiquetada 'QuerySet' con flecha punteada hacia la base de datos, la flecha solo se solidifica cuando se itera; fondo neutro claro

# Un QuerySet no consulta la BD de inmediato

- Es un **objeto Python diferido** — representa la consulta, no el resultado
- La SQL se ejecuta solo cuando se **consume**
- Una vez evaluado, la segunda iteración usa la **caché interna**

---

### [F-03] Lazy evaluation: cuándo se ejecuta la SQL

@tipo: codigo

# Lazy evaluation en acción

## La SQL solo se ejecuta al consumir

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

---

### [F-04] Cuándo se evalúa un QuerySet

@tipo: tabla

# Los 6 momentos de evaluación

## Cuándo Django ejecuta la SQL

| Operación | Ejemplo |
|-----------|---------|
| Iteración (`for`) | `for post in qs:` |
| `list()` o spread | `list(qs)` |
| Slicing con paso | `qs[0:5]` |
| `bool()` en condicional | `if qs:` |
| `len()` | `len(qs)` |
| `repr()` en shell | `qs` en consola |

---

### [F-05] Chaining: encadenar filtros

@tipo: codigo

# Cada método devuelve un nuevo QuerySet

## Nada llega a la BD hasta el slicing `[:10]`

```python
Post.objects.filter(published=True)\
            .exclude(author__is_staff=True)\
            .order_by("-created_at")\
            .values("title", "author__username")[:10]
```

---

### [F-06] Métodos nuevos: más allá de get() y filter()

@tipo: tabla

# El arsenal completo del QuerySet

## Comparado con lo que ya conocías

| Método | Resultado | Estado |
|--------|-----------|--------|
| `.first()` / `.last()` | instancia o `None` | 🆕 |
| `.get_or_create(...)` | `(obj, created: bool)` | 🆕 |
| `.update_or_create(...)` | `(obj, created: bool)` | 🆕 |
| `.exists()` | `bool` | 🆕 |
| `.count()` | `int` | 🆕 |
| `.values("campo")` | QuerySet de dicts | 🆕 |
| `.values_list(..., flat=True)` | QuerySet de valores | 🆕 |
| `.only("campo")` | instancias parciales | 🆕 |
| `.defer("campo")` | excluir campos pesados | 🆕 |

---

### [F-07] get_or_create y update_or_create

@tipo: codigo

# Operaciones atómicas: buscar o crear

## Devuelven tupla (objeto, creado: bool)

```python
# get_or_create: busca primero, crea solo si no existe
cat, created = Category.objects.get_or_create(
    slug="python",
    defaults={"name": "Python"}
)
print(f"{'Creado' if created else 'Encontrado'}: {cat.name}")

# update_or_create: busca y actualiza, o crea
post, created = Post.objects.update_or_create(
    slug="mi-post",
    defaults={"title": "Mi Post Actualizado", "published": True}
)
```

---

### [F-08] Escritura masiva: update() y bulk_create()

@tipo: codigo

# Operaciones en bloque sin llamar .save()

## Mucho más eficientes para N registros

```python
# update() → SQL UPDATE directo, no llama a .save()
Post.objects.filter(author=user).update(published=True)

# delete() — el valor de retorno informa qué se borró
n_deleted, by_type = Post.objects.filter(published=False).delete()
# {'blog.Post': 3, 'blog.Comment': 12}

# bulk_create → inserts masivos sin save() individual
Post.objects.bulk_create([
    Post(title="Post A", author=user),
    Post(title="Post B", author=user),
])
```

---

### [F-09] values() y values_list(): eficiencia selectiva

@tipo: codigo

# Traer solo los campos necesarios

## Sin instanciar modelos completos

```python
# values() → lista de dicts
titulos = Post.objects.filter(published=True)\
                      .values("title", "author__username")
# [{"title": "...", "author__username": "..."}, ...]

# values_list() → lista de tuplas
ids = Post.objects.values_list("id", flat=True)
# QuerySet[1, 2, 3, 4]

# Caso de uso: select en formulario HTML
cats = Category.objects.values_list("id", "name")
```

---

### [F-10] only() y defer(): campos parciales

@tipo: codigo

# Instanciar modelos sin traer todo

## only() → solo los campos declarados

```python
# only(): solo title y created_at — el body no viaja por la red
posts = Post.objects.only("title", "created_at", "author__username")\
                    .select_related("author")

# defer(): todo EXCEPTO los campos indicados
# Útil para excluir campos grandes (content, body)
posts = Post.objects.defer("body", "raw_content")
```

---

### [F-11] Managers personalizados: transferir el patrón a BlogApp

@tipo: demo

# Lo que hiciste con Biblioteca, ahora en BlogApp

## Mismo patrón, nuevo dominio y optimizaciones

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

    def recientes(self, n=10):
        """Top N publicados — con only() para eficiencia."""
        return self.get_queryset()\
                   .select_related("author")\
                   .only("title", "created_at", "author__username")\
                   .order_by("-created_at")[:n]

class Post(models.Model):
    objects = models.Manager()        # siempre declarar el default
    published = PublishedManager()    # manager custom

# Uso
Post.published.all()          # solo publicados
Post.published.recientes(5)   # top 5 eficiente
```

---

### [F-12] Resumen §T1: el QuerySet como profesional

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: mapa mental compacto con 'QuerySet' en el centro, ramas: 'Lazy evaluation', 'Chaining', 'bulk_create/update', 'values/only', 'Managers', estilo minimalista blanco sobre gris oscuro

# §T1 — Lo que ganaste hoy

- **Lazy evaluation**: la BD no trabaja hasta que vos decís
- **Métodos nuevos**: `exists()`, `count()`, `get_or_create()`, `values_list()`
- **Escritura masiva**: `bulk_create()`, `update()` sin tocar instancias
- **Eficiencia selectiva**: `only()`, `defer()`, `values()`
- **Managers**: encapsulan estrategias de consulta reutilizables

---

## BLOQUE T2 — Consultas dinámicas y performance

---

### [F-13] El problema: filtros con lógica compleja

@tipo: socratica
@imagen: background
@prompt-imagen: pantalla oscura con código Python borroso mostrando condiciones if/else complicadas para construir filtros, sensación de código difícil de mantener

# ¿Cómo filtrás cuando la condición es "publicado O del usuario actual"?

Con `filter()` solo podés `AND` implícito.

¿Qué pasa si necesitás OR, NOT, o condiciones dinámicas?

---

### [F-14] Q objects: condiciones lógicas compuestas

@tipo: codigo

# Q: el objeto de condición reutilizable

## Permite OR, AND, NOT en queries

```python
from django.db.models import Q

# OR: publicados O del usuario actual
Post.objects.filter(Q(published=True) | Q(author=request.user))

# AND explícito
Post.objects.filter(Q(category=cat) & Q(published=True))

# NOT
Post.objects.filter(~Q(author__is_staff=True))
```

---

### [F-15] Q objects: construcción dinámica

@tipo: codigo

# Construir filtros en runtime

## Sin Q objects esto requeriría if/else complicados

```python
# Filtro dinámico: se construye según el input del usuario
filters = Q()
if search:
    filters &= Q(title__icontains=search)
if category_id:
    filters &= Q(category_id=category_id)
if only_mine:
    filters &= Q(author=request.user)

# Un solo QuerySet limpio al final
Post.objects.filter(filters, published=True)
```

---

### [F-16] F expressions: operar sobre valores de campo

@tipo: codigo

# F: referenciar un campo en la query SQL

## Sin traer el objeto a Python

```python
from django.db.models import F

# Incrementar un contador sin fetch — un solo UPDATE
Post.objects.filter(pk=pk).update(views=F("views") + 1)

# Comparar dos campos en la misma fila
Post.objects.filter(updated_at__gt=F("created_at"))

# Diferencia de campos numéricos
Post.objects.annotate(
    days_old=F("updated_at") - F("created_at")
)
```

---

### [F-17] aggregate(): estadísticas globales

@tipo: codigo

# aggregate() → una sola fila de estadísticas

## Devuelve un diccionario, no un QuerySet

```python
from django.db.models import Count, Avg, Sum, Max, Min

stats = Post.objects.aggregate(
    total=Count("id"),
    avg_comments=Avg("comment__id"),
    max_views=Max("views")
)
# {"total": 42, "avg_comments": 3.7, "max_views": 1200}
```

---

### [F-18] annotate(): agregar campo calculado a cada objeto

@tipo: codigo

# annotate() → campo extra en cada instancia del QuerySet

## Diferencia clave con aggregate(): resultado por fila, no global

```python
from django.db.models import Count

# Cada categoría ahora tiene .post_count
categories = Category.objects.annotate(
    post_count=Count("post")
).order_by("-post_count")

for cat in categories:
    print(f"{cat.name}: {cat.post_count} posts")

# También con avg, sum, etc.
categories = Category.objects.annotate(
    avg_views=Avg("post__views")
)
```

---

### [F-19] aggregate() vs annotate(): cuándo usar cada uno

@tipo: tabla-comparativa

# Elegir entre aggregate y annotate

## La diferencia está en el nivel de agrupación

| Aspecto | `aggregate()` | `annotate()` |
|---------|--------------|-------------|
| Resultado | Un `dict` | QuerySet con campo extra |
| Nivel | Todo el QuerySet | Por cada objeto |
| SQL generada | `SELECT COUNT(*) FROM ...` | `GROUP BY` implícito |
| Uso típico | Estadísticas globales | Enriquecer objetos |
| Ejemplo | Total de posts del blog | Posts por categoría |

---

### [F-20] El problema N+1: el bug silencioso de performance

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama secuencial mostrando 1 query inicial a la tabla posts seguida de N flechas individuales a la tabla users (una por cada post), con un contador 'N+1 queries' en rojo; contraste visual claro del problema

# 1 query + N queries = el bug de performance clásico

## Django no lo avisa — tenés que detectarlo vos

```python
# ❌ N+1: 1 query para posts + 1 por post para author
posts = Post.objects.all()
for post in posts:
    print(post.author.username)   # SQL extra aquí
```

**En producción con 1000 posts = 1001 queries**

---

### [F-21] Solución N+1: select_related y prefetch_related

@tipo: codigo

# Eliminar N+1 con optimización de consultas

## Elegir según el tipo de relación

```python
# select_related: JOIN SQL — para FK y O2O (1 query total)
posts = Post.objects.select_related("author").all()

# prefetch_related: queries separadas con IN
# Para M2M y reverse FK
posts = Post.objects.prefetch_related("categories", "comments").all()

# Combinación para relaciones múltiples
posts = Post.objects.select_related("author")\
                    .prefetch_related("categories")\
                    .filter(published=True)\
                    .order_by("-created_at")
```

---

### [F-22] Detectar N+1 con connection.queries

@tipo: demo

# Medir queries con connection.queries

## La herramienta de diagnóstico del ORM

```python
from django.db import connection, reset_queries
from django.conf import settings

settings.DEBUG = True
reset_queries()

# ❌ versión con N+1
posts = Post.objects.all()
for p in posts: _ = p.author.username
print(f"Sin select_related: {len(connection.queries)} queries")

reset_queries()

# ✅ versión optimizada
posts = Post.objects.select_related("author").all()
for p in posts: _ = p.author.username
print(f"Con select_related: {len(connection.queries)} queries")
# → 1 sola query
```

---

### [F-23] Evaluación formativa §T2 — Ejercicio pizarra

@tipo: socratica
@imagen: background
@prompt-imagen: pizarrón estilizado con código Python mostrando un loop que accede a post.author.username dentro de un for, con un signo de interrogación grande sobre la cantidad de queries generadas, estética académica

# Encontrá el N+1

Dado este código, ¿cuántas queries se ejecutan si hay 50 posts?

```python
posts = Post.objects.filter(published=True)
for post in posts:
    print(post.author.username)
    for comment in post.comments.all():
        print(comment.user.username)
```

**¿Cómo lo corregís?**

---

## BLOQUE T3 — Puente MVC: CBV con View base

---

### [F-24] El ciclo request/response en Django

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama de flujo horizontal del ciclo Django MVT: Browser → urls.py → View (clase) → Model (datos) → Template (HTML) → Response → Browser, cada capa en un bloque de color diferente, estilo limpio técnico

# Django MVT: cada capa tiene su responsabilidad

## Model → Template → View (no es exactamente MVC, es MVT)

```
Browser → HTTP Request
    → urls.py         (enrutador)
    → View (clase)    (controlador: orquesta)
    → Model           (datos y lógica de dominio)
    → Template        (presentación HTML)
← HTTP Response ← Template renderizado
```

---

### [F-25] Responsabilidades por capa

@tipo: tabla

# ¿Quién hace qué en Django MVT?

| Capa | Responsabilidad | Regla |
|------|----------------|-------|
| **Model** | Datos + lógica de dominio | No HTML, no requests |
| **Template** | Presentación HTML | No lógica de negocio |
| **View** | Orquesta: request → modelo → template → response | Sin lógica de dominio |
| **urls.py** | Enrutar URL → View | Solo mapeo |

---

### [F-26] View como clase base: el entry point OOP

@tipo: codigo

# La CBV más simple: View base + método get()

## Sin magia — cada método HTTP = un método de clase

```python
from django.views import View
from django.shortcuts import render
from .models import Post

class PostListView(View):
    template_name = "blog/post_list.html"

    def get(self, request):
        posts = Post.objects.filter(published=True)\
                            .order_by("-created_at")
        return render(request, self.template_name, {"posts": posts})
```

---

### [F-27] as_view() y dispatch(): la mecánica interna

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de método dispatch en Python, mostrando una petición HTTP entrando con método GET/POST/PUT, y dispatch() enrutando a get(), post(), put() según el método, fondo claro minimalista

# ¿Cómo convierte Django la clase en un callable?

- `as_view()` — crea el callable que Django necesita para urls.py
- `dispatch()` — lee `request.method` y llama `get()`, `post()`, etc.
- Si el método no existe → `405 Method Not Allowed`

```python
# blog/urls.py
urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
```

---

### [F-28] PostDetailView: get_object_or_404

@tipo: codigo

# Detalle de un post: manejo de Not Found

## get_object_or_404 — el atajo correcto

```python
from django.shortcuts import get_object_or_404

class PostDetailView(View):
    template_name = "blog/post_detail.html"

    def get(self, request, pk):
        post = get_object_or_404(
            Post.objects.select_related("author")
                        .prefetch_related("categories"),
            pk=pk,
            published=True
        )
        return render(request, self.template_name, {"post": post})
```

### [F-29] ¿Cómo viajan los datos del View al Template?

@tipo: diagrama
@imagen: content
@prompt-imagen: diagrama de flujo vertical en dos bloques conectados por una flecha etiquetada 'render()': bloque izquierdo 'View (Python)' mostrando un dict Python con claves posts, page_title, user_name; bloque derecho 'Template (HTML)' mostrando {{ posts }}, {{ page_title }}, {{ user_name }}; fondo claro técnico educativo

# El contexto: el mensajero entre View y Template

- La vista construye un **diccionario Python** (`context`)
- Cada **clave** del dict se convierte en una **variable disponible** en el template
- `render()` es la función que conecta ambas capas
- Sin contexto el template no conoce ningún dato de la base de datos

---

### [F-30] El diccionario de contexto: anatomía

@tipo: codigo

# context = las variables que el template puede usar

## Cada clave en Python → `{{ variable }}` en el template

```python
class PostListView(View):
    def get(self, request):
        # 1. Recuperar datos del modelo
        posts = Post.objects.filter(published=True).order_by("-created_at")
        total = Post.objects.count()

        # 2. Empaquetar en el diccionario de contexto
        context = {
            "posts":      posts,          # → {% for post in posts %}
            "total":      total,          # → {{ total }}
            "page_title": "Inicio",       # → {{ page_title }}
        }

        # 3. Pasar el contexto a render()
        return render(request, "blog/post_list.html", context)
```

---

### [F-31] render(): los tres argumentos

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de función Python 'render()' con tres flechas de entrada etiquetadas: 'request — pedido HTTP original', 'template_name — ruta al archivo .html', 'context — dict con datos del modelo'; y una flecha de salida etiquetada 'HttpResponse — HTML renderizado listo para el browser'; fondo neutro minimalista

# render() es el puente entre el controlador y la vista

- **`request`** — el pedido HTTP original; el template lo recibe como `{{ request.user }}`
- **`template_name`** — ruta relativa al archivo `.html` dentro de `templates/`
- **`context`** — el dict de datos; si se omite, el template no recibe ninguna variable

El template recibe **una copia** del contexto — no puede modificar el estado de la vista

---

### [F-32] Trazando un dato de punta a punta

@tipo: demo

# De la base de datos al HTML: el camino completo

## Sin magia — cada paso es explícito

```python
# models.py — el dato vive en la BD
class Post(models.Model):
    title  = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

```python
# views.py — la vista recupera y empaqueta
class PostListView(View):
    def get(self, request):
        posts = Post.objects.select_related("author").filter(published=True)
        return render(request, "blog/post_list.html", {"posts": posts})
        #                                               ↑ clave "posts"
```

```html
<!-- post_list.html — el template recibe la variable "posts" -->
{% for post in posts %}          {# ← la clave del dict es el nombre de la variable #}
    <h2>{{ post.title }}</h2>    {# ← atributo del objeto Post #}
    <p>{{ post.author.username }}</p>  {# ← relación resuelta por select_related #}
{% endfor %}
```


---

### [F-33] ¿Por qué View base y no genérica todavía?

@tipo: tabla-comparativa

# View base vs ListView — pedagogía intencional

| Aspecto | `View` base | `ListView` (Semana 9) |
|---------|------------|----------------------|
| Transparencia | Total: ves todo | Automático: oculta detalles |
| Boilerplate | Manual | Mínimo |
| Cuándo aprender | Primera exposición | Cuando View ya domina |
| Valor pedagógico | Entender el mecanismo | Conocer la abstracción |

**Hoy**: entendemos el mecanismo manual.  
**Semana 9**: refactorizamos a `ListView`/`DetailView` y entendemos *qué automatizan*.

---

### [F-34] Evaluación formativa §T3

@tipo: socratica
@imagen: background
@prompt-imagen: pantalla de error HTTP 405 Method Not Allowed en fondo oscuro con un interrogante sobre qué clase de error es y qué lo causa en Django

# Pregunta de clase

Si una CBV con `View` base tiene solo `def get(self, request)`:

**¿Qué devuelve Django si llega un request PUT?**

---

## BLOQUE T4 — Django Template Language (DTL) completo

---

### [F-35] Los 4 constructos de DTL

@tipo: tabla

# DTL tiene 4 tipos de elementos

## Todo el lenguaje se reduce a estos 4

| Constructo | Sintaxis | Propósito |
|-----------|----------|-----------|
| **Variable** | `{{ variable }}` | Renderizar valor del contexto |
| **Filtro** | `{{ valor\|filtro }}` | Transformar al mostrar |
| **Tag** | `{% tag %}` | Lógica: bucles, condicionales, herencia |
| **Comentario** | `{# texto #}` | Documentación — no se renderiza |

---

### [F-36] Variables y notación de punto

@tipo: codigo

# Acceder a atributos con notación de punto

## Django resuelve el punto probando: atributo → dict → list → método

```python
# En la vista — el contexto es un dict Python
context = {
    "post": post_instance,
    "posts": Post.objects.filter(published=True),
}
```

```html
{{ post.title }}              {# atributo title del objeto #}
{{ post.author.username }}    {# encadenado: post → author → username #}
{{ posts.0.title }}           {# primer elemento de la lista #}
```

---

### [F-37] Filtros: transformar datos al mostrar

@tipo: tabla

# Los filtros más usados en la práctica real

## Sintaxis: `{{ valor|filtro }}` — se encadenan izquierda a derecha

| Filtro | Ejemplo | Resultado |
|--------|---------|-----------|
| `lower` | `{{ post.title\|lower }}` | minúsculas |
| `date` | `{{ post.created_at\|date:"d/m/Y" }}` | `28/06/2025` |
| `truncatewords` | `{{ post.body\|truncatewords:30 }}` | 30 palabras + `…` |
| `linebreaks` | `{{ post.body\|linebreaks }}` | `\n` → `<p>` |
| `default` | `{{ post.subtitle\|default:"Sin subtítulo" }}` | fallback |
| `length` | `{{ comments\|length }}` | cantidad |
| `escape` | `{{ user_input\|escape }}` | protección XSS |

---

### [F-38] Auto-escape: protección XSS incorporada

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama mostrando input de usuario con script HTML malicioso entrando al sistema, la capa de template Django con escudo etiquetado 'auto-escape', y HTML seguro saliendo como output, fondo claro técnico

# Django protege contra XSS por defecto

- `{{ variable }}` → Django **auto-escapa** el valor
- `<script>` → se convierte en `&lt;script&gt;`
- Para desactivar intencionalmente: `{{ valor|safe }}` (solo si el origen es confiable)
- El filtro `escape` lo hace explícito

---

### [F-39] {% for %} y variables de forloop

@tipo: codigo

# Iterar sobre QuerySets y listas

## forloop trae variables automáticas gratis

```html
{% for post in posts %}
    <article {% if forloop.first %}class="featured"{% endif %}>
        <p>{{ forloop.counter }}. {{ post.title }}</p>
        {% if forloop.last %}
            <p><em>{{ forloop.counter }} posts en total.</em></p>
        {% endif %}
    </article>
{% empty %}
    <p>No hay posts publicados todavía.</p>
{% endfor %}
```

---

### [F-40] Variables de forloop: la referencia completa

@tipo: tabla

# ¿Qué sabe forloop de sí mismo?

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `forloop.counter` | int | Índice desde **1** |
| `forloop.counter0` | int | Índice desde **0** |
| `forloop.revcounter` | int | Inverso, termina en 1 |
| `forloop.first` | bool | `True` en primera iteración |
| `forloop.last` | bool | `True` en última iteración |
| `forloop.parentloop` | objeto | Loop padre (loops anidados) |

---

### [F-41] {% if %} con operadores completos

@tipo: codigo

# Condicionales con toda la potencia de Python

## Operadores: ==, !=, <, >, and, or, not, in, is

```html
{% if posts %}
    <p>Hay {{ posts|length }} publicaciones.</p>
{% elif drafts %}
    <p>Solo hay borradores.</p>
{% else %}
    <p>Sin contenido aún.</p>
{% endif %}

{# Combinados #}
{% if post.published and post.author == request.user %}
    <a href="...">Editar</a>
{% endif %}

{# in operator #}
{% if "django" in post.tags %}
    <span class="tag">Django</span>
{% endif %}
```

---

### [F-42] Trampa de precedencia en {% if %}

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama comparativo de dos columnas: Python con precedencia clásica (and antes que or) versus DTL con evaluación izquierda a derecha, ilustrando con expresión booleana donde el resultado difiere, estilo técnico educativo

# ¡Atención! DTL evalúa de izquierda a derecha

- **Python**: `and` tiene precedencia sobre `or`
- **DTL**: evaluación estrictamente **izquierda a derecha**
- `{% if a or b and c %}` en DTL ≠ en Python
- **Solución**: anidar `{% if %}` cuando se necesita lógica compleja

---

### [F-43] {% with %}: alias para evitar lookups repetidos

@tipo: codigo

# Calcular una vez, usar muchas

## Sin with: cada {{post.author}} puede ser un SQL extra

```html
{% with author=post.author %}
    <p>Nombre: {{ author.get_full_name }}</p>
    <p>Email: {{ author.email }}</p>
    <p>Posts publicados: {{ author.post_set.count }}</p>
{% endwith %}
{# Fuera del with, 'author' ya no existe #}

{# También para acortar expresiones #}
{% with total=business.employees.count %}
    Hay {{ total }} empleado{{ total|pluralize }}.
{% endwith %}
```

---

### [F-44] {% load %} y {% static %}: archivos estáticos

@tipo: codigo

# Servir CSS, JS e imágenes desde Django

## {% load %} debe estar en cada template que usa la librería

```html
{% load static %}

<link rel="stylesheet" href="{% static 'blog/css/styles.css' %}">
<script src="{% static 'blog/js/app.js' %}"></script>
<img src="{% static 'blog/img/logo.png' %}" alt="Logo">
```

```python
# settings.py — requerido
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
```

---

### [F-45] {% url %}: resolver URLs por nombre

@tipo: codigo

# Nunca hardcodear URLs en templates

## {% url %} es equivalente a reverse() pero en templates

```html
{# Básico #}
<a href="{% url 'blog:post-list' %}">Inicio</a>

{# Con argumento posicional #}
<a href="{% url 'blog:post-detail' post.pk %}">Ver post</a>

{# Con argumento por nombre — más legible #}
<a href="{% url 'blog:post-detail' pk=post.pk %}">Ver post</a>

{# Guardar en variable para reutilizar #}
{% url 'blog:post-detail' pk=post.pk as post_url %}
{% if post_url %}<a href="{{ post_url }}">Enlace</a>{% endif %}
```

---

### [F-46] {% comment %} y {# #}: documentar templates

@tipo: codigo

# Los comentarios en DTL no llegan al navegador

## Dos formas: una línea vs bloque

```html
{# Este comentario no se renderiza — para una línea #}

{% comment "Sección pendiente de diseño" %}
    <section class="sidebar">
        {# aquí irá el widget de categorías en Semana 9 #}
    </section>
{% endcomment %}

{# Truco: usar comment para desactivar código temporalmente #}
{# Inspeccioná el HTML (Ctrl+U) — los comentarios DTL no aparecen #}
```

---

### [F-47] Herencia de templates: el principio DRY aplicado a HTML

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: diagrama de árbol mostrando un archivo base.html con bloques etiquetados title, content, extra_scripts, y dos archivos hijo post_list.html y post_detail.html que extienden de base con sus propios bloques coloreados, fondo blanco limpio

# Sin herencia: cada template repite el mismo HTML

**El problema**:
- `<head>`, navbar, footer se copian en cada archivo
- Un cambio de logo = tocar todos los templates

**La solución**: `{% extends %}` + `{% block %}`

---

### [F-48] Herencia en práctica: base.html y children

@tipo: demo

# Esqueleto base + hijos que extienden

## extends debe ser la primera línea del child

```html
{# base.html — esqueleto con bloques para personalizar #}
<html>
<head><title>{% block title %}Mi Blog{% endblock %}</title></head>
<body>
<nav><a href="{% url 'blog:post-list' %}">Inicio</a></nav>
<main>{% block content %}{% endblock %}</main>
</body>
</html>
```

```html
{# post_list.html — child template #}
{% extends "blog/base.html" %}
{% block title %}Listado de Posts{% endblock %}
{% block content %}
    <h1>Publicaciones</h1>
    {# ... contenido específico ... #}
{% endblock %}
```

---

### [F-49] block.super: extender sin reemplazar

@tipo: codigo

# Combinar contenido del padre y del hijo

## block.super incluye lo que el padre tenía en ese bloque

```html
{# base.html #}
{% block extra_head %}
    <link rel="stylesheet" href="{% static 'blog/css/main.css' %}">
{% endblock %}

{# post_detail.html — agrega sin borrar el CSS base #}
{% block extra_head %}
    {{ block.super }}  {# incluye el main.css del padre #}
    <link rel="stylesheet" href="{% static 'blog/css/post.css' %}">
{% endblock %}
```

---

### [F-50] {% include %}: reutilizar fragmentos (partials)

@tipo: codigo

# Componentes parciales reutilizables

## La tarjeta de post como un componente

```html
{# blog/templates/blog/partials/post_card.html #}
<article class="post-card">
    <h2><a href="{% url 'blog:post-detail' post.pk %}">{{ post.title }}</a></h2>
    <p>{{ post.author.username }} — {{ post.created_at|date:"d/m/Y" }}</p>
    <p>{{ post.body|truncatewords:25 }}</p>
</article>
```

```html
{# post_list.html: usa el partial en el loop #}
{% for post in posts %}
    {% include "blog/partials/post_card.html" with post=post %}
{% empty %}
    <p>No hay posts publicados todavía.</p>
{% endfor %}
```

---

### [F-51] Mini-ejercicio §T4: pizarra DTL

@tipo: socratica
@imagen: background
@prompt-imagen: pizarrón estilizado con HTML mezclado con tags DTL incompletos, alumno apuntando a la pantalla, ambiente de clase interactivo

# Escribí este template de memoria

Un template que:

1. Extiende `base.html`
2. Cambia el `{% block title %}`
3. Usa `{% for %}` con `forloop.counter`
4. Incluye `{% if forloop.first %}` para destacar el primero
5. Tiene `{% empty %}` para el caso vacío

---

### [F-52] Cierre de clase teórica

@tipo: cierre
@imagen: background
@prompt-imagen: pizarrón con mapa conceptual dibujado a mano: ORM avanzado (Q/F/annotate) conectado a Views (CBV) conectado a Templates (DTL), flecha circular cerrando el ciclo, luz cálida

# Lo que construiste hoy

- **ORM**: lazy evaluation, Q/F, aggregate/annotate, N+1 → select_related
- **CBV**: `View` base, `as_view()`, `dispatch()`, `get()`/`post()`
- **DTL**: variables, filtros, `{% for %}`, `{% if %}`, `{% with %}`, `{% static %}`, herencia, partials

**Semana 9**: `ListView`/`DetailView` + formularios `ModelForm` + Parcial 1
