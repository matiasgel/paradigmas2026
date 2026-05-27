# Filminas — Módulo VI: Autenticación, Autorización y Django Admin
# Tema 06 | Laboratorio de Programación y Lenguajes 2026
# 2 Clases teóricas — 120 min c/u | Django 6.0 · Python 3.12+ · Bootstrap 5.3.3

---

# CLASE 1 — Autenticación Django (120 min)

---

### [F1-00] Portada — Clase 1

@tipo: portada
@imagen: background
@prompt-imagen: dark background with faint lock icons and Python keyword patterns — def login logout authenticate — deep navy and teal palette, no text, blurred dark mode IDE

# Módulo VI — Autenticación Django

¿Quién sos? ¿Cómo lo prueba tu aplicación?

Semana 12 · BlogApp · `django.contrib.auth` · Django 6.0

---

## BLOQUE T1 — HTTP y Sesiones (15 min)

---

### [F1-01] HTTP no recuerda al cliente — el problema fundamental

@tipo: concepto-abstracto

# HTTP es un protocolo sin memoria. Cada request viaja sola y el servidor olvida todo.

## Por qué necesitamos sesiones

El protocolo HTTP procesa cada request de forma completamente independiente.
El servidor recibe un GET, responde, y no tiene ningún registro de quién era ese cliente.
Cualquier aplicación real necesita saber: **¿este browser ya se autenticó?**

Hay tres enfoques históricos para resolver esto:

| Enfoque | Mecanismo | Problema |
|---------|-----------|----------|
| Cookies con datos | guardar user_id en la cookie | La cookie es manipulable por el usuario |
| JWT en cookie | token firmado en cookie | Revocación compleja, tamaño grande |
| **Sesiones del servidor** (Django) | cookie con ID opaco, datos en servidor | El estándar — datos seguros en BD |

## Lo que hace Django

```
Browser                              Django Server
───────────────────────────────────────────────────────────────
GET /dashboard/   (sin cookie)  →   AnonymousUser → redirige /login/

POST /login/  {user, pass}      →   verifica credenciales
                                →   crea fila en django_session (BD)
                                ←   Set-Cookie: sessionid=a1b2c3d4  ← UUID opaco

GET /dashboard/
Cookie: sessionid=a1b2c3d4     →   AuthenticationMiddleware:
                                    busca "a1b2c3d4" en django_session
                                →   request.user = User(id=42) ok
```

- `sessionid` es un UUID opaco — **no contiene datos del usuario**
- Los datos viven en el **servidor**, no en el browser
- El atacante no puede fabricar un sessionid válido

---

### [F1-02] Backends de sesión y configuración de seguridad

@tipo: tabla

# Django tiene 4 backends de sesión — el default es BD, el de producción es cached_db.

## Los cuatro backends

| Backend | Almacenamiento | Cuándo usar |
|---------|---------------|-------------|
| `db` (default) | tabla `django_session` | Desarrollo y apps de baja carga |
| `cache` | Redis / Memcached | Alta performance, acepta pérdida de sesiones |
| `cached_db` | Redis + BD fallback | **Producción recomendada** |
| `file` | archivos en el servidor | No distribuido — no usar en producción |

## Settings críticos de seguridad

```python
# settings.py
SESSION_COOKIE_HTTPONLY = True    # JS NO puede leer sessionid → anti-XSS
SESSION_COOKIE_SECURE   = True    # solo por HTTPS (obligatorio en producción)
SESSION_COOKIE_AGE      = 1209600  # 2 semanas en segundos (default)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
```

**Por qué HTTPONLY es crítico:**
Si JavaScript pudiera leer `sessionid`, un ataque XSS podría robar la cookie
y suplantar al usuario. Con HTTPONLY, solo el browser la maneja.

---

### [F1-03] Ciclo de vida completo de una sesión

@tipo: diagrama-flujo

# Cinco momentos definen el ciclo: generación, autenticación, uso, destrucción.

## La secuencia con lo que Django hace internamente

```
1. GET /login/
   → Django genera session_key UUID4 (sesión anónima)

2. POST /login/ {username: "juan", password: "secreto"}
   → authenticate(request, username, password)
      → ModelBackend: busca User, llama check_password()
      → retorna User si válido | None si inválido | None si is_active=False
   → login(request, user)
      → session["_auth_user_id"] = str(user.pk)
      → INSERT en django_session
      → ROTA el sessionid (nuevo UUID) — previene session fixation attack

3. Requests subsiguientes: Cookie sessionid=<nuevo_uuid>
   → AuthenticationMiddleware.process_request()
   → SELECT en django_session WHERE session_key = <uuid>
   → request.user = User(id=42) — disponible en TODA vista y template

4. request.user.is_authenticated → True
   request.user.username → "juan"
   request.user.has_perm("blog.add_post") → True/False

5. POST /logout/
   → session.flush() → DELETE en django_session
   → nueva sessionid vacía
   → request.user = AnonymousUser
```

## El error más común

`authenticate()` verifica credenciales pero **NO crea la sesión**.
Olvidar `login()` → la próxima request ve `request.user = AnonymousUser`.

---

## BLOQUE T2 — django.contrib.auth (35 min)

---

### [F1-04] django.contrib.auth: un sistema de 7 componentes

@tipo: concepto-abstracto

# django.contrib.auth no es solo un modelo de usuario — es un sistema completo de identidad.

## Qué incluye el paquete

Django viene con autenticación completa preinstalada.
No hay que instalar librerías externas para login, logout,
cambio y reset de contraseña, grupos y permisos.

```
django.contrib.auth
|
├── models.py      User · Group · Permission
|                  AbstractUser · AbstractBaseUser
|
├── backends.py    ModelBackend       — verifica credenciales contra la BD
|                  RemoteUserBackend  — para LDAP / SSO corporativo
|
├── middleware.py  AuthenticationMiddleware
|                  → convierte sessionid en User | AnonymousUser en CADA request
|                  → popula request.user ANTES de llegar a la vista
|
├── views.py       LoginView · LogoutView
|                  PasswordChangeView · PasswordResetView (flujo de 4 vistas)
|
├── forms.py       AuthenticationForm · UserCreationForm · UserChangeForm
|
├── decorators.py  @login_required · @permission_required · @user_passes_test
|
└── mixins.py      LoginRequiredMixin · PermissionRequiredMixin · UserPassesTestMixin
```

## Activación (ya viene en proyectos nuevos)

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",           # el sistema de auth
    "django.contrib.contenttypes",   # base del sistema de permisos
    "django.contrib.sessions",
    "django.contrib.messages",       # requerido para el admin
]
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]
```

---

### [F1-05] El modelo User — tres categorías de campos

@tipo: tabla

# User tiene campos de identidad, seguridad y flags de autorización — cada uno con semántica precisa.

## Campos de identidad

| Campo | Tipo | Nota |
|-------|------|------|
| `username` | CharField(150) | Único, obligatorio |
| `email` | EmailField | **No único por defecto** — trampa clásica |
| `first_name` / `last_name` | CharField | Opcionales |

## Campos de seguridad

| Campo | Nota |
|-------|------|
| `password` | `pbkdf2_sha256$1200000$<salt>$<hash>` — siempre hasheado |
| `last_login` | Actualizado automáticamente por `login()` |

## Flags de autorización

| Campo | Semántica operativa |
|-------|---------------------|
| `is_active` | False = desactivada (soft delete). `login()` falla si es False. |
| `is_staff` | True = puede entrar a /admin/. No implica permisos específicos. |
| `is_superuser` | True = `has_perm()` siempre True. Solo administradores técnicos. |

## Regla de oro con passwords

```python
# MAL — texto plano en la BD
user.password = "secreto123"

# BIEN — PBKDF2+SHA256 (1.200.000 iteraciones en Django 6.0)
user.set_password("secreto123")
# Django 6.0: iteraciones subieron de 1.000.000 a 1.200.000
# Contraseñas existentes se re-hashean al próximo login automáticamente
```

---

### [F1-06] AbstractUser — extender sin perder el sistema de auth

@tipo: codigo

# AbstractUser hereda toda la funcionalidad de User y permite agregar campos propios.

## La regla: definir AUTH_USER_MODEL antes de la primera migración

Si queremos agregar bio, teléfono o avatar después de migrar,
es imposible sin borrar las tablas. `AbstractUser` nos da flexibilidad desde el inicio.

```python
# blog/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class BlogUser(AbstractUser):
    bio    = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    # Hereda: username, email, password, is_active, is_staff,
    #         is_superuser, groups, user_permissions, last_login, date_joined
```

```python
# settings.py — ANTES de la primera migración
AUTH_USER_MODEL = "blog.BlogUser"
```

## Importar User de forma genérica

```python
# MAL — acoplado al modelo concreto:
from django.contrib.auth.models import User

# BIEN — funciona con cualquier AUTH_USER_MODEL:
from django.contrib.auth import get_user_model
User = get_user_model()

# Para ForeignKey — usar settings, no importar el modelo directamente:
from django.conf import settings
author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

---

### [F1-07] authenticate() vs login() — la distinción que más confunde

@tipo: codigo

# authenticate() verifica identidad. login() crea la sesión. Ambas son necesarias y hacen cosas distintas.

## Por qué son funciones separadas

La separación permite autenticar desde múltiples backends (BD, OAuth, LDAP)
sin cambiar cómo se crea la sesión.
`authenticate()` normaliza la identidad; `login()` la persiste.

```python
from django.contrib.auth import authenticate, login

user = authenticate(request, username="juan", password="secreto")
# → recorre AUTHENTICATION_BACKENDS en orden
# → ModelBackend: busca User, llama check_password()
# → retorna User si válido | None si inválido | None si is_active=False

if user is not None:
    login(request, user)
    # → session["_auth_user_id"] = str(user.pk)
    # → INSERT en django_session
    # → ROTA el sessionid (previene session fixation attack)
    return redirect("blog:post-list")
else:
    # No revelar cuál campo es incorrecto — esa info ayuda a atacantes
    messages.error(request, "Usuario o contraseña incorrectos.")
```

## logout() — tres acciones en una llamada

```python
from django.contrib.auth import logout

logout(request)
# 1. session.flush() → DELETE en django_session
# 2. genera nueva sessionid vacía en cookie
# 3. request.user = AnonymousUser
```

---

### [F1-08] Vistas genéricas de auth y novedades Django 6.0

@tipo: codigo

# Una línea en urls.py registra todo el ciclo de autenticación. Django 6.0 agrega login_not_required().

## Por qué usar las vistas de Django y no implementar las propias

Las vistas de `django.contrib.auth.views` manejan correctamente:
rotación de sessionid, parámetro `?next=`, CSRF en logout,
invalidación de sesión al cambiar contraseña.
Implementar esto desde cero es un camino conocido a vulnerabilidades.

```python
# urls.py
urlpatterns = [
    path("admin/",    admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # Registra: login/ · logout/ · password_change/ · password_change/done/
    #           password_reset/ · password_reset/done/
    #           reset/<uidb64>/<token>/ · reset/done/
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path("blog/",     include("blog.urls", namespace="blog")),
]
```

```python
# settings.py
LOGIN_URL           = "/accounts/login/"
LOGIN_REDIRECT_URL  = "/blog/"
LOGOUT_REDIRECT_URL = "/blog/"
```

## LogoutView — solo POST desde Django 5.x (y 6.0)

```html
<!-- MAL — GET en logout rechazado por protección CSRF -->
<a href="{% url 'logout' %}">Salir</a>

<!-- BIEN — POST con csrf_token -->
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit" class="btn btn-outline-secondary btn-sm">Salir</button>
</form>
```

**Por qué GET es peligroso:** `<img src="https://mi-app.com/accounts/logout/">` en
una página de terceros provocaría logout involuntario sin consentimiento del usuario.

## Django 6.0 — login_not_required() y API async

```python
# Para proyectos con LoginRequiredMiddleware (todo requiere auth por defecto):
from django.contrib.auth.decorators import login_not_required

@login_not_required          # exime esta vista del middleware global
def login_view(request): ...

@login_not_required
def register_view(request): ...
```

```python
# API async para vistas ASGI / Django Channels:
from django.contrib.auth import aauthenticate, alogin, alogout

async def mi_login(request):
    user = await aauthenticate(request, username=..., password=...)
    if user:
        await alogin(request, user)

user = await request.auser()   # obtener usuario en vista async
```

---

## BLOQUE T3 — Templates y Registro (30 min)

---

### [F1-09] Templates de auth: naming convention y variables de contexto

@tipo: tabla

# Django busca templates de auth en registration/ — el nombre del archivo es el contrato.

## Estructura obligatoria

```
templates/
  registration/
    login.html                  ← LoginView
    password_change_form.html   ← PasswordChangeView
    password_change_done.html
    password_reset_form.html    ← PasswordResetView (inicio del flujo)
    password_reset_done.html    ← "revisá tu email"
    password_reset_email.html   ← email con el link de reset
    password_reset_confirm.html ← nueva contraseña (valida el token)
    password_reset_complete.html
  blog/
    register.html               ← nuestra vista custom
```

```python
TEMPLATES = [{"DIRS": [BASE_DIR / "templates"], "APP_DIRS": True, ...}]
```

## Variables de contexto en todos los templates (automáticas)

| Variable | Descripción |
|----------|-------------|
| `user` | User o AnonymousUser |
| `user.is_authenticated` | True si hay sesión activa |
| `user.username` | vacío si es anónimo |
| `user.is_staff` | puede acceder al admin |
| `perms` | PermWrapper — verificador lazy de permisos |

## Template login.html — los 3 elementos críticos

```html
{% extends "base.html" %}
{% block content %}
<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-5">
      <div class="card shadow-sm">
        <div class="card-body p-4">
          <h3 class="mb-4">Iniciar sesión</h3>
          {% if form.errors %}
          <div class="alert alert-danger">Usuario o contraseña incorrectos.</div>
          {% endif %}
          <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="hidden" name="next" value="{{ next }}">
            <button type="submit" class="btn btn-primary w-100">Entrar</button>
          </form>
          <p class="mt-3 text-center">
            ¿No tenés cuenta? <a href="{% url 'register' %}">Registrate</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
```

- Sin `{% csrf_token %}` → 403 Forbidden en el POST
- Sin `name="next"` → `?next=` es ignorado, redirige siempre a `LOGIN_REDIRECT_URL`
- Sin `{% if form.errors %}` → el usuario no sabe qué salió mal

---

### [F1-10] Registro: RegisterForm y RegisterView

@tipo: codigo

# El registro no viene en auth.urls. UserCreationForm es la base que extendemos.

## Por qué Django no incluye el registro

El sistema de auth es genérico. Algunas apps requieren solo username,
otras email obligatorio, otras campos de perfil adicionales.
`UserCreationForm` es la base — la extendemos según necesidades.

## RegisterForm con email único

```python
# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        # User.email no tiene unique=True — validamos unicidad manualmente
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
```

## RegisterView con auto-login y grupo por defecto

```python
# blog/views.py
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class    = RegisterForm
    template_name = "registration/register.html"
    success_url   = reverse_lazy("blog:post-list")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            reader_group = Group.objects.get(name="reader")
            self.object.groups.add(reader_group)   # nuevo usuario = lector por defecto
        except Group.DoesNotExist:
            pass
        login(self.request, self.object)           # auto-login post-registro
        return response
```

---

### [F1-11] Cierre Clase 1

@tipo: portada
@imagen: none

# Al terminar la Clase 1: BlogApp autentica usuarios. La Clase 2 controla qué pueden hacer.

## Lo que construimos en la Clase 1

```
OK  BlogUser (AbstractUser con bio + avatar)
OK  Registro con RegisterForm (email único) + auto-login + grupo reader
OK  Login con LoginView + templates Bootstrap en registration/
OK  Logout con form POST (Django 6.0 compatible)
OK  PasswordChangeView y PasswordResetView configuradas
OK  Variables user / perms disponibles en todos los templates
OK  login_not_required() para vistas públicas con LoginRequiredMiddleware
```

## El problema que resuelve la Clase 2

```
FALTA  Juan puede editar el post de María sin ninguna restricción
FALTA  Todos los usuarios logueados tienen el mismo nivel de acceso
FALTA  No hay interfaz para que el staff administre el contenido
```

---

# CLASE 2 — Autorización y Django Admin (120 min)

---

### [F2-00] Portada — Clase 2

@tipo: portada
@imagen: background
@prompt-imagen: dark background showing abstract permission matrix grid, shield icons, key patterns — dark green and deep navy palette, no text labels, blurred technical aesthetic

# Módulo VI — Autorización y Django Admin

¿Qué puede hacer cada usuario? ¿Quién administra el sistema?

Semana 13 · Permisos · Grupos · Mixins CBV · `django.contrib.admin`

---

## BLOQUE T1 — Autorización: capas y conceptos (40 min)

---

### [F2-01] auth ≠ authz — la distinción más importante del módulo

@tipo: concepto-abstracto

# Autenticación y autorización son problemas distintos con soluciones distintas en Django.

## La diferencia conceptual

**Autenticación** responde: *¿Quién sos?*
Sesiones + credenciales → `request.user = User("juan")`

**Autorización** responde: *¿Qué podés hacer?*
Permisos + grupos → `has_perm()`, mixins, `get_queryset()`

Un usuario puede estar autenticado pero sin autorización para una acción específica.
Las dos capas son independientes y se complementan.

## Las tres capas de autorización en Django

```
Capa 1 — ¿Está logueado?
         LoginRequiredMixin / @login_required
         |
         sí
         v
Capa 2 — ¿Tiene el permiso de modelo?
         PermissionRequiredMixin / @permission_required / has_perm()
         |
         sí
         v
Capa 3 — ¿Es el dueño del objeto?
         get_queryset() → Http404 si no es el autor
         |
         sí
         v
         ejecutar la vista
```

## En BlogApp

| Acción | Capas requeridas |
|--------|-----------------|
| Ver posts | Sin restricción |
| Crear post | Capa 1 + Capa 2 (blog.add_post) |
| Editar mi propio post | Capa 1 + Capa 3 (author == request.user) |
| Publicar cualquier post | Capa 1 + Capa 2 (blog.publish_post) |
| Acceder al admin | is_staff = True |

---

### [F2-02] Permisos por defecto y permisos personalizados

@tipo: codigo

# Django crea 4 permisos por modelo automáticamente. Meta.permissions agrega los propios.

## Los 4 permisos automáticos

Para cada modelo Django crea en la señal `post_migrate`:

```
blog.add_post       → puede crear Post
blog.change_post    → puede modificar Post
blog.delete_post    → puede eliminar Post
blog.view_post      → puede ver Post (solo lectura)
```

```python
user.has_perm("blog.add_post")        # True | False
user.has_module_perms("blog")         # True si tiene algún permiso de la app
user.get_all_permissions()            # set de todos los permisos (propios + grupos)
# Superuser → siempre True | AnonymousUser → siempre False
```

## Permisos personalizados

```python
class Post(models.Model):
    # ... campos ...
    class Meta:
        permissions = [
            ("publish_post",  "Puede marcar posts como publicados"),
            ("feature_post",  "Puede destacar posts en la portada"),
            ("moderate_post", "Puede moderar posts de otros"),
        ]
        # Genera codenames: blog.publish_post · blog.feature_post · blog.moderate_post
```

```bash
# Obligatorio después de agregar permisos en Meta:
python manage.py makemigrations
python manage.py migrate   # INSERT en auth_permission via señal post_migrate
```

---

### [F2-03] LoginRequiredMixin y PermissionRequiredMixin

@tipo: codigo

# Los mixins son la forma idiomática de proteger CBV. El orden en la declaración importa.

## Regla de la cátedra: en CBV, siempre mixins. El mixin va PRIMERO en la MRO.

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView

# Orden correcto: mixin ANTES de la vista genérica
class PostCreateView(LoginRequiredMixin, CreateView):
    model         = Post
    form_class    = PostForm
    template_name = "blog/post_form.html"
    success_url   = reverse_lazy("blog:post-list")
    login_url     = "/accounts/login/"

# PermissionRequiredMixin — requiere permiso específico
class PostPublishView(PermissionRequiredMixin, UpdateView):
    model               = Post
    permission_required = "blog.publish_post"   # string o tupla para AND lógico
    raise_exception     = True   # logueado sin permiso → 403 (no redirect al login)
    template_name       = "blog/post_publish.html"
    fields              = ["is_published"]
```

## Comportamiento según estado del usuario

| Usuario | raise_exception | Resultado |
|---------|----------------|-----------|
| No logueado | cualquiera | redirect a login?next=url |
| Logueado, sin permiso | False | redirect al login (confuso) |
| Logueado, sin permiso | **True** | **403 Forbidden** (correcto) |
| Logueado, con permiso | cualquiera | ejecuta la vista |

## Por qué mixins en lugar de @decoradores para CBV

`@login_required` sobre una clase solo protege el método decorado.
El mixin se integra al `dispatch()` y protege **todos** los métodos HTTP
(GET, POST, DELETE, PATCH) de forma consistente.

---

### [F2-04] Protección de objeto con get_queryset() y grupos

@tipo: codigo

# Filtrar el queryset por autor es el patrón estándar para ownership en Django.

## Por qué Http404 es mejor que 403 para ownership

Con `get_queryset()` filtrado: si el objeto no es del usuario,
`get_object()` lanza Http404 automáticamente.
El atacante no puede saber si el objeto existe pero no puede acceder,
o si directamente no existe.
**Para ownership: 404 es más privado que 403.**

```python
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model         = Post
    form_class    = PostForm
    success_url   = reverse_lazy("blog:post-list")

    def get_queryset(self):
        # pk=5 no pertenece a request.user → get_object() → Http404 automático
        return Post.objects.filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model       = Post
    success_url = reverse_lazy("blog:post-list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
```

## Grupos: asignación masiva de permisos a roles

```python
from django.contrib.auth.models import Group, Permission

def crear_roles():
    author_group, _ = Group.objects.get_or_create(name="author")
    author_group.permissions.set(Permission.objects.filter(
        content_type__app_label="blog",
        codename__in=["add_post", "change_post", "delete_post",
                      "view_post", "add_comment", "publish_post"]
    ))
    reader_group, _ = Group.objects.get_or_create(name="reader")
    reader_group.permissions.set(Permission.objects.filter(
        content_type__app_label="blog",
        codename__in=["view_post", "add_comment"]
    ))

# Verificar membresía desde el código:
user.groups.filter(name="author").exists()   # True | False
```

---

### [F2-05] Permisos en templates: navbar y botones condicionales

@tipo: codigo

# El objeto perms evalúa has_perm() de forma lazy — sin queries extras si no se referencia.

## Cómo funciona `{{ perms }}`

`perms` es un `PermWrapper` que envuelve `request.user.has_perm()` de forma lazy.
`perms.blog.add_post` evalúa `request.user.has_perm("blog.add_post")` solo cuando se accede.
No genera queries si no se usa en el template.

```html
<!-- Botones condicionales por permiso de modelo -->
{% if perms.blog.add_post %}
    <a href="{% url 'blog:post-create' %}" class="btn btn-primary">Nuevo post</a>
{% endif %}

<!-- Ownership del objeto: mostrar solo al autor o staff -->
{% if user == post.author or user.is_staff %}
    <a href="{% url 'blog:post-update' pk=post.pk %}">Editar</a>
    <form method="post" action="{% url 'blog:post-delete' pk=post.pk %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger btn-sm">Eliminar</button>
    </form>
{% endif %}

<!-- Navbar completo en base.html -->
{% if user.is_authenticated %}
    {% if perms.blog.add_post %}
    <a class="nav-link" href="{% url 'blog:post-create' %}">Nuevo Post</a>
    {% endif %}
    <span class="navbar-text me-2">{{ user.username }}</span>
    <form method="post" action="{% url 'logout' %}" class="d-inline">
        {% csrf_token %}
        <button type="submit" class="btn btn-outline-light btn-sm">Salir</button>
    </form>
{% else %}
    <a class="nav-link" href="{% url 'login' %}">Iniciar sesión</a>
    <a class="nav-link" href="{% url 'register' %}">Registrarse</a>
{% endif %}
```

---

## BLOQUE T5-T10 — Django Admin (75 min)

---

### [F2-06] Qué es el Django Admin y para qué sirve

@tipo: concepto-abstracto

# El admin es una interfaz de gestión automática — no es un panel público, es una herramienta de producción.

## La filosofía del admin de Django

El admin de Django es uno de los rasgos más distintivos del framework.
Lee los metadatos de los modelos (campos, tipos, relaciones) y genera
una interfaz CRUD completa sin escribir HTML ni JavaScript.

**Para qué está pensado:**
- Gestión interna: editores de contenido, moderadores, soporte técnico
- Inspección y debug de datos en desarrollo y producción
- Operaciones administrativas que no justifican una vista custom

**Para qué NO está pensado:**
- Interfaz pública para usuarios finales
- Reemplazar un panel de control diseñado para el negocio
- Operaciones masivas en millones de filas (usar management commands)

## Lo que genera al registrar un modelo

```
/admin/                          → index — listado de apps y modelos registrados
/admin/blog/post/                → changelist — lista paginada con filtros y búsqueda
/admin/blog/post/add/            → add_view — formulario de alta
/admin/blog/post/5/change/       → change_view — formulario de edición
/admin/blog/post/5/delete/       → delete_view — confirmación de borrado
/admin/blog/post/5/history/      → history_view — LOG AUTOMATICO de todos los cambios
```

## El log automático de cambios (LogEntry)

El admin registra CADA operación (alta, edición, borrado) en `django_admin_log`.
Funciona sin configurar nada. Desde `/admin/blog/post/5/history/`
se ve quién cambió qué campo y cuándo.

```python
# Acceder al log programáticamente:
from django.contrib.admin.models import LogEntry
LogEntry.objects.filter(user=request.user).order_by("-action_time")[:10]
```

## Prerequisitos

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",  # requerido para el feedback visual del admin
]
urlpatterns = [path("admin/", admin.site.urls)]  # una línea registra todo
```

---

### [F2-07] Registrar modelos: @admin.register y ModelAdmin

@tipo: codigo

# @admin.register es el decorador preferido. ModelAdmin vacío es el punto de partida.

## Las dos formas de registrar

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Comment

# Forma 1: register() directo — simple, sin personalización
admin.site.register(Category)
# → lista mostrando "Category object (1)" — sin más información

# Forma 2: @admin.register — preferido para personalizar
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass   # punto de partida — equivale a register() pero expandible
```

## Por qué ModelAdmin vacío es mejor que register() simple

`@admin.register` + clase permite agregar atributos progresivamente
sin cambiar la línea de registro. Es la convención estándar del ecosistema Django.

## Quién puede usar el admin

- `is_staff = True` → puede entrar a /admin/
- `is_superuser = True` → acceso completo (bypassa todos los permisos)
- Staff sin superuser → solo los permisos asignados explícitamente

La sesión del admin usa las mismas sesiones Django que la app — un solo login.

---

### [F2-08] List view: list_display, list_filter y search_fields

@tipo: codigo

# Tres atributos transforman una lista plana en una herramienta de búsqueda y gestión real.

## Qué hace cada atributo

**`list_display`**: columnas de la tabla. Sin esto, solo aparece `str(objeto)`.
**`list_filter`**: sidebar derecho con checkboxes. Django genera las opciones automáticamente.
**`search_fields`**: barra de búsqueda arriba. Usa ILIKE. Con `__` cruza relaciones con JOIN.

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Columnas de la tabla
    list_display   = ["title", "author", "is_published", "created_at", "comment_count"]

    # Sidebar de filtros (derecha)
    list_filter    = ["is_published", "author", "created_at"]

    # Barra de búsqueda (arriba)
    search_fields  = ["title", "body", "author__username"]

    # Opciones de navegación
    ordering       = ["-created_at"]
    date_hierarchy = "created_at"   # drill-down: año → mes → día en la parte superior
    list_per_page  = 20
    list_display_links = ["title"]  # columnas que son links al objeto

    # Columna calculada (no es un campo del modelo)
    @admin.display(description="Comentarios")
    def comment_count(self, obj):
        return obj.comments.count()

    # Columna con icono booleano
    @admin.display(description="Publicado", boolean=True, ordering="is_published")
    def publicado_icon(self, obj):
        return obj.is_published   # muestra checkmark o X en lugar de True/False
```

## Búsqueda con search_fields — sintaxis de lookups

```python
search_fields = [
    "title",             # ILIKE '%query%'  (default)
    "^title",            # ^ starts with — más eficiente con índice
    "=title",            # = exact match
    "@body",             # @ full text search — solo PostgreSQL
    "author__username",  # JOIN automático a User
    "category__name",    # JOIN automático a Category
]
```

---

### [F2-09] Detail view: fieldsets, readonly_fields y save_model()

@tipo: codigo

# fieldsets organiza el formulario en secciones. save_model() intercepta el guardado.

## Por qué usar fieldsets

Sin `fieldsets`, todos los campos en una lista plana.
Con `fieldsets`: grupos lógicos, secciones colapsables, orden controlado.

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Contenido principal", {
            "fields": ["title", "slug", "body", "category"],
        }),
        ("Estado y publicacion", {
            "fields":      ["author", "is_published"],
            "classes":    ["collapse"],     # colapsable (cerrada por defecto)
            "description": "Configurar antes de publicar.",
        }),
        ("Timestamps (solo lectura)", {
            "fields":  ["created_at", "updated_at"],
            "classes": ["collapse"],
        }),
    ]

    readonly_fields     = ["created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}   # auto-genera slug con JS
    raw_id_fields       = ["author"]             # reemplaza select con busqueda + popup

    def save_model(self, request, obj, form, change):
        # change=False → creacion | change=True → edicion
        if not change:
            obj.author = request.user   # asignar usuario del admin como autor
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)   # staff solo ve sus propios posts
```

---

### [F2-10] Acciones en masa: @admin.action y message_user()

@tipo: codigo

# Las acciones operan sobre el queryset de los registros seleccionados con los checkboxes.

## Cómo funcionan las acciones

El usuario selecciona registros con los checkboxes de la list view,
elige una acción del dropdown "Action" y hace clic en "Go".
Django llama a la función con el queryset de todos los seleccionados.

```python
from django.contrib import admin, messages

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ["publish_selected", "unpublish_selected"]

    @admin.action(description="Publicar posts seleccionados")
    def publish_selected(self, request, queryset):
        # queryset.update() → UNA sola query SQL para todos los seleccionados
        # No llama a save() ni dispara señales post_save
        updated = queryset.update(is_published=True)
        self.message_user(
            request,
            f"{updated} post(s) publicado(s) exitosamente.",
            messages.SUCCESS   # pasar SUCCESS explicitamente para icono verde
        )

    @admin.action(description="Despublicar posts seleccionados")
    def unpublish_selected(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"{updated} despublicado(s).", messages.WARNING)
```

## Django 6.0: message_user() con Font Awesome 6.7.2 — iconos diferenciados

En Django 6.0, `messages.INFO` y `messages.SUCCESS` tienen iconos **distintos**.
Antes ambos mostraban el mismo icono verde. Ahora son visualmente diferenciables.

```python
self.message_user(request, "Exito.",  messages.SUCCESS)  # icono verde (explicito)
self.message_user(request, "Info.",   messages.INFO)     # icono info (nuevo en 6.0)
self.message_user(request, "Aviso.",  messages.WARNING)  # icono de advertencia
self.message_user(request, "Error.",  messages.ERROR)    # icono rojo

# message_user() default = messages.INFO → icono distinto en 6.0
# Para icono verde de exito: siempre pasar messages.SUCCESS explicitamente
```

## queryset.update() vs loop con save()

| Metodo | Queries | Llama save() | Senales post_save | Cuando usar |
|--------|---------|-------------|-------------------|-------------|
| queryset.update() | 1 | No | No | Actualizar campos simples masivamente |
| loop + obj.save() | N | Si | Si | Cuando la logica en save() o senales importan |

---

### [F2-11] InlineModelAdmin: TabularInline y StackedInline

@tipo: codigo

# Los inlines permiten editar modelos relacionados directamente desde el formulario del padre.

## Para qué sirven los inlines

Sin inlines, para gestionar comentarios de un post hay que ir a
`/admin/blog/comment/` y filtrar por post manualmente.
Con inlines, los comentarios aparecen en la misma pagina de edicion del post.
Es la forma mas eficiente de gestionar relaciones OneToMany en el admin.

## TabularInline — filas horizontales (muchos items, pocos campos)

```python
class CommentInline(admin.TabularInline):
    model            = Comment
    extra            = 1            # forms vacios para agregar nuevos
    max_num          = 20
    can_delete       = True
    fields           = ["author", "body", "approved", "created_at"]
    readonly_fields  = ["created_at"]
    show_change_link = True         # link para abrir el comentario en su propia pagina

    def get_queryset(self, request):
        # select_related previene N+1 queries al cargar author de cada comentario
        return super().get_queryset(request).select_related("author")
```

## StackedInline — campos apilados (pocos items, muchos campos)

```python
class PostMetaInline(admin.StackedInline):
    model  = PostMeta     # metadata SEO del post (OneToOne)
    extra  = 0            # sin forms vacios — solo aparece si ya existe
    fields = ["og_title", "og_description", "canonical_url", "structured_data"]
```

## Registro con inlines

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, PostMetaInline]  # debajo del form, en orden declarado
```

## Cuando usar cada uno

| Tipo | Cuando | Ejemplo en BlogApp |
|------|--------|-------------------|
| TabularInline | Muchos items, pocos campos | Comment: author + body + approved |
| StackedInline | Pocos items, muchos campos | Metadata SEO: og_title, og_description... |

---

### [F2-12] Control de acceso: has_*_permission()

@tipo: codigo

# Django llama a estos metodos antes de cada operacion. Permiten ownership dentro del admin.

## Por qué has_*_permission() va mas alla de is_staff

`is_staff = True` controla el acceso al admin en general.
`has_change_permission(request, obj)` permite granularidad por objeto:
- `obj=None` → decision para la list view completa (mostrar botones de edicion?)
- `obj=Post` → decision para ese objeto especifico (puede editar ESTE post?)

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return request.user.has_perm("blog.add_post")

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True   # puede ver la list view
        # Solo el autor o superuser puede editar el objeto especifico
        return obj.author == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser   # solo superuser puede borrar

    def has_view_permission(self, request, obj=None):
        return True   # cualquier staff puede ver
```

## Nota sobre obj=None

Django llama `has_change_permission(request, obj=None)` para decidir si mostrar
el boton "Editar" en la list view.
Si retorna `False` para `obj=None` → no aparece el boton en ninguna fila.
Separar la decision `obj=None` de `obj=instancia` es el patron correcto.

---

### [F2-13] AdminSite: branding y password_change_form (Django 6.0)

@tipo: codigo

# AdminSite personaliza el admin globalmente. Django 6.0 agrega password_change_form.

## Branding basico — tres atributos, impacto visual inmediato

```python
# blog/admin.py
from django.contrib import admin

admin.site.site_header = "BlogApp — Administracion"   # barra superior de cada pagina
admin.site.site_title  = "BlogApp"                    # sufijo en el <title> del browser
admin.site.index_title = "Panel de administracion"    # heading de la pagina index
```

## Django 6.0 — AdminSite.password_change_form (NUEVO)

Permite usar un formulario personalizado para el cambio de contrasena del admin.
Antes no habia forma de sobreescribir este formulario sin crear un AdminSite custom.

```python
# forms.py
from django.contrib.auth.forms import AdminPasswordChangeForm
from django import forms

class SecurePasswordChangeForm(AdminPasswordChangeForm):
    def clean_password2(self):
        password = super().clean_password2()
        if len(password) < 12:
            raise forms.ValidationError("Staff: minimo 12 caracteres.")
        return password

# admin.py — nueva forma de registrar el formulario en Django 6.0
admin.site.password_change_form = SecurePasswordChangeForm
```

## AdminSite custom — para multiples admins en un mismo proyecto

```python
class BlogAdminSite(admin.AdminSite):
    site_header          = "BlogApp — Admin Interno"
    site_title           = "BlogApp Admin"
    password_change_form = SecurePasswordChangeForm   # Django 6.0

blog_admin = BlogAdminSite(name="blog_admin")
blog_admin.register(Post, PostAdmin)
blog_admin.register(Comment)

# urls.py
urlpatterns = [
    path("admin/",      admin.site.urls),
    path("blog-admin/", blog_admin.urls),   # segundo admin separado
]
```

---

### [F2-14] APIs removidas en Django 6.0 y DEFAULT_AUTO_FIELD

@tipo: concepto-abstracto

# Tres cambios de Django 6.0 que afectan el admin y los modelos — hay que conocerlos para el TP.

## 1. log_deletion() y log_addition() del ModelAdmin — REMOVIDAS

```python
# REMOVIDAS en Django 6.0 (deprecadas desde 5.1):
#   ModelAdmin.log_deletion(request, object, object_repr)
#   ModelAdmin.log_addition(request, object, message)

# Alternativa: sobreescribir delete_model() — el log ocurre en super()
def delete_model(self, request, obj):
    super().delete_model(request, obj)  # super() registra el log automaticamente
```

## 2. lookup_allowed() requiere request como tercer parametro

Si el proyecto sobreescribe `lookup_allowed()` en algun ModelAdmin:

```python
# BIEN — firma correcta en Django 6.0:
def lookup_allowed(self, lookup, value, request):
    return super().lookup_allowed(lookup, value, request)

# MAL — firma de Django 5.x — rompe con TypeError en 6.0:
# def lookup_allowed(self, lookup, value): ...
```

## 3. DEFAULT_AUTO_FIELD — BigAutoField es el nuevo default

```python
# Django 6.0: el tipo de PK automatica cambia a BigAutoField (entero 64-bit).
# Sin declararlo explicita → warning en las migraciones.

# settings.py — declarar para evitar warnings:
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # nuevo default — recomendado
# o para compatibilidad con modelos existentes de 32-bit:
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
```

---

### [F2-15] PostAdmin completo integrado — BlogApp

@tipo: codigo

# Todos los conceptos del admin integrados en un archivo admin.py de produccion.

```python
# blog/admin.py

from django.contrib import admin, messages
from .models import Post, Comment, Category


class CommentInline(admin.TabularInline):
    model           = Comment
    extra           = 0
    fields          = ["author", "body", "approved", "created_at"]
    readonly_fields = ["created_at"]
    can_delete      = True

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("author")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # ── List view ──────────────────────────────────────────────
    list_display   = ["title", "author", "is_published", "created_at", "comment_count"]
    list_filter    = ["is_published", "author", "created_at"]
    search_fields  = ["title", "body", "author__username"]
    ordering       = ["-created_at"]
    date_hierarchy = "created_at"
    list_per_page  = 20

    @admin.display(description="Comentarios")
    def comment_count(self, obj):
        return obj.comments.count()

    # ── Detail view ────────────────────────────────────────────
    fieldsets = [
        ("Contenido", {
            "fields": ["title", "slug", "body", "category"]
        }),
        ("Publicacion", {
            "fields": ["author", "is_published"],
            "classes": ["collapse"]
        }),
        ("Timestamps", {
            "fields": ["created_at", "updated_at"],
            "classes": ["collapse"]
        }),
    ]
    readonly_fields     = ["created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields       = ["author"]
    inlines             = [CommentInline]

    # ── Acciones ───────────────────────────────────────────────
    actions = ["publish_selected", "unpublish_selected"]

    @admin.action(description="Publicar posts seleccionados")
    def publish_selected(self, request, queryset):
        n = queryset.update(is_published=True)
        self.message_user(request, f"{n} post(s) publicado(s).", messages.SUCCESS)

    @admin.action(description="Despublicar posts seleccionados")
    def unpublish_selected(self, request, queryset):
        n = queryset.update(is_published=False)
        self.message_user(request, f"{n} despublicado(s).", messages.WARNING)

    # ── Control de acceso ──────────────────────────────────────
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.author == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields       = ["name"]


# ── Branding global ────────────────────────────────────────────
admin.site.site_header = "BlogApp — Administracion"
admin.site.site_title  = "BlogApp"
admin.site.index_title = "Panel de administracion"
```

---

### [F2-16] Cierre — BlogApp completa y errores frecuentes

@tipo: portada
@imagen: none

# Modulo VI completo: auth + authz + admin de produccion para BlogApp.

## Estado final de BlogApp (Clase 1 + Clase 2)

```
OK  BlogUser (AbstractUser con bio + avatar)
OK  Registro con email unico + auto-login + grupo reader
OK  Login / logout con vistas genericas + templates Bootstrap
OK  Roles: author (CRUD propio) / reader (ver + comentar)
OK  LoginRequiredMixin en todas las vistas de escritura
OK  get_queryset() protege edicion/borrado por propietario (Http404)
OK  perms y user.is_authenticated en base.html
OK  PostAdmin: list_display + fieldsets + search + date_hierarchy + acciones + CommentInline
OK  has_change_permission() con ownership en el admin
OK  CategoryAdmin registrado
OK  Branding del admin configurado
OK  Django 6.0: PBKDF2 1.2M · login_not_required · password_change_form · Font Awesome 6.7.2
```

## Errores frecuentes

| Error | Causa | Prevencion |
|-------|-------|------------|
| AUTH_USER_MODEL cambiado post-migrate | BD ya tiene tablas auth | Definir ANTES de la primera migrate |
| Login no redirige a ?next= | Falta input name="next" en template | Incluir siempre el campo hidden next |
| PermissionRequiredMixin hace loop | raise_exception=False para logueado | Setear raise_exception = True |
| LogoutView con GET | Django 5.x+ rechaza GET | form method="post" con csrf_token |
| log_deletion() no existe | Removida en Django 6.0 | Usar delete_model() override |
| lookup_allowed() sin request | Firma incorrecta en Django 6.0 | Agregar request como tercer parametro |
| Admin muestra "Post object" | Sin list_display ni __str__ | Definir __str__ en modelo O list_display |
| TabularInline N+1 | FK sin prefetch | select_related en get_queryset() del inline |

## TP 4 — Auth + Admin completo (semana 14)

- Login / logout / registro + grupos author / reader
- LoginRequiredMixin + get_queryset() para ownership
- PostAdmin con CommentInline + accion publish_selected
- Tests: login redirect · 403 sin permiso · autor edita propio · reader no puede
- Coverage >= 80%

## Proximo modulo

Semana 15 — Tema 07: REST API con Django REST Framework
`Serializer` · `ViewSet` · `Router` · `TokenAuthentication`
