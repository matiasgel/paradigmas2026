# Tema 06 — Autenticación, Autorización y Django Admin
## Módulo VI completo — UNTDF IF009 2026

> **Fecha**: 2026-05-27
> **Semanas del plan**: 12–13 (ver `salida/cursadas/2026/plan-borrador.md` §Módulo VI)
> **Estado**: DESIGN — pendiente aprobación docente
> **Prerequisito confirmado**: Vistas genéricas OOP (CBV), ModelForm, templates con herencia completa, Bootstrap integrado, sesiones HTTP (`request.session`) introducidas en Tema 05 §T5.
> **Fuentes base**: django-6.0-docs (auth, admin) · plan-minimo.md Módulo VI · plan-borrador.md §Semanas 12-14

---

## 1. Metadatos

| Campo | Valor |
|-------|-------|
| Número | 06 |
| Nombre | Módulo VI — Autenticación, Autorización y Django Admin |
| Módulos plan | VI completo (auth, permisos, grupos, admin) |
| Duración total | **360 min = 6 h = 2 clases teóricas de 180 min c/u** |
| Audiencia | 3º año UNTDF Sistemas/AUS, niveles heterogéneos |
| Paradigma docente | **POO estricto: CBV + Mixins obligatorios. Decoradores solo para FBV legacy. Admin como herramienta de producción, no juguete.** |
| Dominio | BlogApp — `Post`, `Category`, `Comment` + extensión `User` como autor |
| Prerequisitos | Tema 05 aprobado: vistas genéricas OOP, ModelForm, templates herencia |

---

## 2. Cobertura del Plan Mínimo

### Módulo VI — Autorización y Autenticación

| Tópico mínimo obligatorio | Clase | Cobertura |
|---------------------------|-------|-----------|
| Sesiones de usuario en aplicaciones web | C1 §T1 | Sesiones Django, backends, `request.session` ampliado |
| Manejo de autenticación en Django | C1 §T2 | `django.contrib.auth`, User model, `authenticate()`, `login()`, `logout()` |
| Vistas genéricas para manejo de usuario y formularios | C1 §T3 | `LoginView`, `LogoutView`, `PasswordChangeView`, `PasswordResetView` |
| Desarrollo de templates para manejo de usuarios | C1 §T4 | `registration/` naming, `LOGIN_URL`, `LOGIN_REDIRECT_URL`, templates base |
| Autorización en Django: permisos en modelos y vistas | C2 §T1 | `has_perm()`, permisos por defecto, permisos personalizados en `Meta` |
| Grupos y permisos: modelo `Group`, modelo `Permission`, asignación | C2 §T2 | `Group`, `Permission`, `user.groups.add()`, `user.user_permissions.add()` |
| Permisos por defecto (`add`, `change`, `delete`, `view`) y personalizados | C2 §T1 | Creados automáticamente por Django + `class Meta: permissions` |
| Decoradores de autorización: `@login_required`, `@permission_required`, `@user_passes_test` | C2 §T3a | Uso en FBV y con `method_decorator` en CBV (solo como alternativa) |
| Mixins de autorización: `LoginRequiredMixin`, `PermissionRequiredMixin` | C2 §T3b | **Enfoque principal CBV** — `login_url`, `permission_required`, `raise_exception` |
| Verificación de permisos en templates con `{% if perms %}` | C2 §T4 | `{% if perms.blog.add_post %}`, `{% if user.is_authenticated %}` |
| App de administración de Django (`django.contrib.admin`) | C2 §T5 | `admin.site.register()`, `@admin.register` |
| Registro de modelos | C2 §T5 | Ambas formas, `ModelAdmin` básico vs personalizado |
| Personalización `ModelAdmin` | C2 §T6 | `list_display`, `list_filter`, `search_fields`, `ordering`, `date_hierarchy` |
| Campos y formularios admin | C2 §T6 | `fields`, `fieldsets`, `readonly_fields`, `exclude` |
| Acciones en masa personalizadas | C2 §T7 | `actions`, función action, `@admin.action`, feedback al admin |
| Relaciones en el admin: `InlineModelAdmin` | C2 §T8 | `TabularInline`, `StackedInline`, `max_num`, `min_num` |
| Control de acceso en el admin | C2 §T9 | `has_add_permission`, `has_change_permission`, `has_delete_permission` + request |
| Personalización del sitio admin: `AdminSite` | C2 §T10 | `site.site_header`, `site_title`, `index_title` — y `AdminSite` custom si hay tiempo |
| Generación de interfaz de admin con permisos | C2 §T6-T9 | Integración completa BlogApp: Post + Comment + User admin |

> **Cobertura Módulo VI**: 100% de los tópicos del plan mínimo.

---

## 3. Estructura de las clases — Vista general

```
CLASE 1 — TEÓRICA (180 min) ─────────────────────────────────────────
  [0–10]   Apertura: HTTP stateless → sesiones → auth → authz (arco narrativo)
  T1  25'  Sesiones Django ampliadas: backends, configuración, ciclo de vida
  T2  40'  django.contrib.auth: User model, AbstractUser, authenticate()/login()/logout()
  T3  40'  Vistas genéricas de auth: LoginView, LogoutView, PasswordChangeView,
           PasswordResetView — configuración, flow, redirect_field_name
  T4  25'  Templates de autenticación: naming convention registration/,
           LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, context auth
  T5  30'  Registro de usuario: UserCreationForm, UserChangeForm, vista CBV
           con CreateView + success_url + email como unique
  [175-180] Cierre + anticipo Clase 2

CLASE 2 — TEÓRICA (180 min) ─────────────────────────────────────────
  [0–5]    Apertura: auth ≠ authz — diferencia crítica
  T1  30'  Sistema de permisos: permisos por defecto (add/change/delete/view),
           has_perm(), has_module_perms(), permisos personalizados (Meta)
  T2  20'  Grupos: Group model, asignación masiva de permisos, user.groups
  T3a 15'  Decoradores: @login_required, @permission_required, @user_passes_test
  T3b 25'  Mixins CBV: LoginRequiredMixin, PermissionRequiredMixin — enfoque principal
  T4  15'  Templates: {% if perms.blog.add_post %}, {% if user.is_authenticated %}
  T5  10'  Admin setup: register() vs @admin.register, ModelAdmin básico
  T6  20'  ModelAdmin avanzado: list_display, list_filter, search_fields, fieldsets
  T7  10'  Acciones en masa: función action, @admin.action, mensajes feedback
  T8  15'  InlineModelAdmin: TabularInline vs StackedInline aplicado en BlogApp
  T9  10'  Control de acceso admin: has_add_permission, has_change_permission
  T10  5'  AdminSite: site_header, site_title, index_title
  [175-180] Cierre + introducción TP 4

PRÁCTICA (paralela a Clase 2, semana 13-14):
  BlogApp: login/logout/register funcional + permisos author/reader + admin completo
```

---

## 4. Objetivos de aprendizaje (Bloom)

### Clase 1 — Autenticación

| # | Nivel Bloom | Objetivo |
|---|-------------|---------|
| 1 | **Comprender** (2) | Explicar la diferencia entre autenticación y autorización y por qué Django separa estos conceptos en módulos distintos |
| 2 | **Comprender** (2) | Describir el ciclo completo de una sesión Django: creación al login, persistencia via cookie `sessionid`, destrucción al logout |
| 3 | **Aplicar** (3) | Configurar `LoginView` y `LogoutView` con templates propios y redirecciones personalizadas usando `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` |
| 4 | **Aplicar** (3) | Implementar el flujo de registro de usuario con `UserCreationForm` mediante `CreateView` y validar email único |
| 5 | **Analizar** (4) | Trazar el flujo completo `authenticate()` → `login()` → sesión → `request.user` y explicar qué falla si se omite `login()` después de `authenticate()` |
| 6 | **Aplicar** (3) | Extender `AbstractUser` para agregar campos personalizados (bio, avatar) y migrar sin romper el sistema de auth |

### Clase 2 — Autorización + Admin

| # | Nivel Bloom | Objetivo |
|---|-------------|---------|
| 7 | **Comprender** (2) | Distinguir permisos de objeto vs permisos de modelo y explicar los 4 permisos por defecto que Django genera automáticamente |
| 8 | **Aplicar** (3) | Implementar `LoginRequiredMixin` y `PermissionRequiredMixin` en CBV de BlogApp para restringir creación/edición a autores propietarios |
| 9 | **Analizar** (4) | Elegir entre `@login_required`, `LoginRequiredMixin` y `PermissionRequiredMixin` para cada caso de uso y justificar la elección |
| 10 | **Aplicar** (3) | Configurar `Group` con permisos para roles `author` y `reader` y asignarlos programáticamente al registrar usuario |
| 11 | **Construir** (3) | Personalizar `ModelAdmin` para `Post` con `list_display`, `list_filter`, `search_fields`, `fieldsets` y una acción en masa de publicación |
| 12 | **Aplicar** (3) | Implementar `TabularInline` para gestionar `Comment` dentro del admin de `Post` |
| 13 | **Analizar** (4) | Identificar qué permite `has_change_permission()` que no permite `PermissionRequiredMixin` a nivel de objeto |

---

## 5. CLASE 1 — Autenticación Django (180 min)

> **Punto de partida**: los estudiantes ya conocen `request.session` como dict de sesión (Tema 05 §T5). El sistema de auth de Django construye sobre ese mecanismo.  
> **Este tema** introduce la capa de autenticación completa: User model, vistas genéricas, templates y registro.

### Agenda Clase 1

| Tiempo | Código | Bloque |
|--------|--------|--------|
| 0–10 | — | Apertura: el arco auth → authz — por qué importa el orden |
| 10–35 | T1 | Sesiones Django: backends, configuración, ciclo de vida de la sesión |
| 35–75 | T2 | `django.contrib.auth`: User model, `AbstractUser`, `authenticate()`, `login()`, `logout()` |
| 75–115 | T3 | Vistas genéricas de auth: `LoginView`, `LogoutView`, `PasswordChangeView`, `PasswordResetView` |
| 115–140 | T4 | Templates de autenticación: naming convention, settings de redirect |
| 140–175 | T5 | Registro: `UserCreationForm`, `CreateView`, email único, señales |
| 175–180 | — | Cierre + anticipo Clase 2 |

---

### §T1 — Sesiones Django ampliadas (25 min)

> **Concepto central**: las sesiones son el puente entre HTTP stateless y el estado de usuario. Django las abstrae en un dict-like `request.session` respaldado por un backend configurable.

#### Backends de sesión disponibles

Django ofrece 4 backends:

```
BACKEND                             PERSISTENCIA
─────────────────────────────────────────────────────
django.contrib.sessions.backends.db      → tabla django_session (default)
django.contrib.sessions.backends.cache   → Redis/Memcached (rápido, volátil)
django.contrib.sessions.backends.cached_db → cache + BD (rápido + persistente)
django.contrib.sessions.backends.file   → archivos en servidor (no distribuido)
```

**Configuración mínima** (`settings.py`):
```python
SESSION_COOKIE_AGE = 1209600          # 2 semanas (default)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_HTTPONLY = True        # Seguridad: JS no puede leer sessionid
SESSION_COOKIE_SECURE = True          # Solo HTTPS en producción
```

#### Ciclo de vida de la sesión

```
1. GET /login/   → Django genera session_key = UUID4 (no existe sesión previa)
2. POST /login/  → authenticate() + login() → django_session INSERT
3. Response      → Set-Cookie: sessionid=<session_key>; HttpOnly
4. Requests sgts → Cookie sessionid → request.session = session data
5. POST /logout/ → session.flush() → django_session DELETE → sessionid inválida
```

**Pregunta anticipada**: *"¿Por qué `SESSION_COOKIE_HTTPONLY = True` es importante?"*  
**Respuesta**: Previene que JavaScript lea la cookie de sesión — protección contra XSS. Si JavaScript pudiera leer `sessionid`, un atacante podría robar la sesión.

---

### §T2 — `django.contrib.auth`: arquitectura (40 min)

> **Concepto central**: `django.contrib.auth` no es solo un modelo de usuario — es un sistema completo con backends de autenticación, middleware de request y vistas reutilizables.

#### Componentes del sistema

```
django.contrib.auth
│
├── models.py          User, Group, Permission, AbstractUser, AbstractBaseUser
├── backends.py        ModelBackend (default), RemoteUserBackend
├── middleware.py      AuthenticationMiddleware → request.user siempre disponible
├── views.py           LoginView, LogoutView, PasswordChangeView, etc.
├── forms.py           AuthenticationForm, UserCreationForm, UserChangeForm
├── decorators.py      @login_required, @permission_required, @user_passes_test
└── mixins.py          LoginRequiredMixin, PermissionRequiredMixin
```

#### El modelo `User` — campos principales

```python
from django.contrib.auth.models import User

# Campos de identidad
user.username          # CharField — identificador único (max 150)
user.email             # EmailField — no único por defecto (¡trampa frecuente!)
user.first_name        # CharField (optional)
user.last_name         # CharField (optional)

# Campos de seguridad
user.password          # CharField — NUNCA en texto plano (PBKDF2+SHA256)
user.last_login        # DateTimeField
user.date_joined       # DateTimeField

# Flags de autorización
user.is_active         # Bool — False = cuenta desactivada (no eliminada)
user.is_staff          # Bool — True = puede acceder al admin
user.is_superuser      # Bool — True = bypasses ALL permission checks
```

**Error frecuente**: `user.password = "texto"` — NUNCA. Siempre `user.set_password("texto")`.

> 🆕 **Django 6.0**: El hasher PBKDF2 aumentó de 1.000.000 a **1.200.000 iteraciones** (mayor seguridad, contraseñas existentes se actualizan al próximo login).

#### `AbstractUser` — extensión recomendada

```python
# blog/models.py
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    # Todos los campos de User están disponibles

# settings.py — CRÍTICO: ANTES de la primera migración
AUTH_USER_MODEL = "blog.BlogUser"
```

**Advertencia**: `AUTH_USER_MODEL` DEBE definirse antes de `python manage.py migrate`. Cambiar después de crear tablas requiere borrar la BD y reconstruir.

#### `authenticate()` vs `login()` — la distinción crítica

```python
from django.contrib.auth import authenticate, login, logout

# authenticate() — SOLO verifica credenciales, NO crea sesión
user = authenticate(request, username="juan", password="secreto")
# Retorna: User | None

if user is not None:
    login(request, user)   # ESTO crea la sesión y rota la sessionid
    # Rotación de sessionid previene session fixation attacks
```

> 🆕 **Django 6.0 — API asíncrona** (para vistas async con `async def`):
> ```python
> user = await aauthenticate(request, username=username, password=password)
> await alogin(request, user)    # async login
> await alogout(request)         # async logout
> user = await request.auser()   # obtener usuario actual async
> ```

**Pregunta anticipada**: *"¿Qué pasa si llamo authenticate() pero no login()?"*  
**Respuesta**: El usuario queda autenticado solo en esa función — la próxima request tendrá `request.user = AnonymousUser`. La sesión no se creó.

#### `logout()` — limpieza completa

```python
from django.contrib.auth import logout

def my_logout(request):
    logout(request)   # Hace tres cosas:
    # 1. Borra los datos de sesión de la BD (session.flush())
    # 2. Regenera la cookie sessionid (previene session reuse)
    # 3. Pone request.user = AnonymousUser
```

> 🆕 **Django 6.0 — `login_not_required()`**: Cuando se usa `LoginRequiredMiddleware` (todas las vistas requieren auth por defecto), este decorador exime vistas específicas:
> ```python
> from django.contrib.auth.decorators import login_not_required
> 
> @login_not_required
> def login_view(request): ...  # no requiere auth aunque el middleware esté activo
> ```

---

### §T3 — Vistas genéricas de autenticación (40 min)

> Django provee vistas listas para usar en `django.contrib.auth.views`. No hay que implementar el ciclo authenticate/login — ya está hecho.

#### Configuración con una sola línea

```python
# blog_project/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    # Registra automáticamente:
    # accounts/login/          → LoginView
    # accounts/logout/         → LogoutView
    # accounts/password_change/ → PasswordChangeView
    # accounts/password_reset/  → PasswordResetView
    # ... y más
]
```

#### `LoginView` — configuración completa

```python
# urls.py — versión explícita para personalizar
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,  # si ya logueado → redirect
            next_page="/blog/",                # alternativa a settings.LOGIN_REDIRECT_URL
        ),
        name="login",
    ),
]
```

**El flujo de LoginView**:
```
GET /login/   → form vacío (AuthenticationForm)
POST /login/  → form.is_valid() → authenticate() → login() → redirect
             → form inválido → redisplay con errores
```

**El parámetro `?next=`**: si la URL tiene `?next=/posts/crear/`, después del login Django redirige a `/posts/crear/` en lugar de `LOGIN_REDIRECT_URL`.

#### `LogoutView`

```python
# settings.py
LOGOUT_REDIRECT_URL = "/blog/"   # dónde va el usuario después del logout

# urls.py (Django 5.0+)
# LogoutView solo acepta POST — protección CSRF contra logout forzado
```

**Error frecuente Django 5.x**: `<a href="/logout/">Salir</a>` ya NO funciona. Requiere un form con `method="POST"` y `{% csrf_token %}`.

#### `PasswordChangeView` y `PasswordResetView`

```python
# PasswordChangeView — requiere usuario logueado
# Verifica old_password → valida new_password (reglas de validators) → set_password + login nuevamente

# PasswordResetView — flujo completo de recuperación:
# 1. /password_reset/ → PasswordResetView → envía email con token
# 2. /password_reset/done/ → PasswordResetDoneView → "revisá tu email"
# 3. /reset/<uidb64>/<token>/ → PasswordResetConfirmView → nueva contraseña
# 4. /reset/done/ → PasswordResetCompleteView → confirmación

# Configuración de email (dev):
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

---

### §T4 — Templates de autenticación (25 min)

> Django busca los templates de auth en `registration/` por convención. El lugar correcto es `templates/registration/`.

#### Naming convention obligatoria

```
templates/
  registration/
    login.html             ← LoginView
    logout.html            ← LogoutView (si se usa next_page sin redirect)
    password_change_form.html      ← PasswordChangeView
    password_change_done.html
    password_reset_form.html       ← PasswordResetView
    password_reset_done.html
    password_reset_email.html      ← email enviado al usuario
    password_reset_confirm.html
    password_reset_complete.html
```

#### Template `login.html` mínimo

```html
{% extends "base.html" %}
{% block content %}
<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-5">
      <h2>Iniciar sesión</h2>
      <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="hidden" name="next" value="{{ next }}">
        <button type="submit" class="btn btn-primary">Entrar</button>
      </form>
      <p class="mt-3"><a href="{% url 'register' %}">¿No tenés cuenta? Registrate</a></p>
    </div>
  </div>
</div>
{% endblock %}
```

#### Settings de redirección (settings.py)

```python
LOGIN_URL = "/accounts/login/"          # donde redirige @login_required
LOGIN_REDIRECT_URL = "/blog/"           # después de login exitoso
LOGOUT_REDIRECT_URL = "/blog/"          # después de logout
```

#### Variables de contexto disponibles en templates

```python
# Disponibles siempre via AuthenticationMiddleware + context processors:
request.user                 # User | AnonymousUser
request.user.is_authenticated  # True | False
request.user.is_staff         # True | False
request.user.username         # str

# En cualquier template (context processor django.template.context_processors.auth):
{{ user }}                    # User o AnonymousUser
{{ user.is_authenticated }}
{{ perms }}                   # Permission checker — ver Clase 2
```

---

### §T5 — Registro de usuario (30 min)

> El registro no está incluido en `django.contrib.auth.urls` — hay que implementarlo. Django provee `UserCreationForm` como base.

#### `UserCreationForm` — qué incluye

```python
from django.contrib.auth.forms import UserCreationForm

# Campos incluidos por defecto:
# - username (con validación de unicidad)
# - password1 (con validadores de seguridad)
# - password2 (confirmación)

# Extiender para incluir email obligatorio:
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User   # o BlogUser si AUTH_USER_MODEL está configurado
        fields = ("username", "email", "password1", "password2")
    
    def clean_email(self):
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

#### Vista de registro con CBV

```python
# blog/views.py
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:post-list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)   # auto-login después de registro
        return response
    
    def dispatch(self, request, *args, **kwargs):
        # Si ya está logueado, redirigir
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
```

---

## 6. CLASE 2 — Autorización y Django Admin (180 min)

> **Punto de partida**: los estudiantes pueden autenticar usuarios. Ahora necesitan controlar **qué puede hacer** cada usuario autenticado.  
> **Este tema** cubre el sistema de permisos, grupos, mixins CBV y la app de administración completa.

### Agenda Clase 2

| Tiempo | Código | Bloque |
|--------|--------|--------|
| 0–5 | — | Apertura: auth ≠ authz — línea clara |
| 5–35 | T1 | Sistema de permisos: permisos por defecto, `has_perm()`, permisos personalizados |
| 35–55 | T2 | Grupos: `Group`, asignación masiva, roles BlogApp |
| 55–70 | T3a | Decoradores: `@login_required`, `@permission_required`, `@user_passes_test` |
| 70–95 | T3b | Mixins CBV: `LoginRequiredMixin`, `PermissionRequiredMixin` — **enfoque principal** |
| 95–110 | T4 | Templates: `{% if perms %}`, `{% if user.is_authenticated %}` |
| 110–120 | T5 | Admin setup: register vs @admin.register |
| 120–140 | T6 | `ModelAdmin` avanzado: list_display, fieldsets, list_filter |
| 140–150 | T7 | Acciones en masa: `actions`, feedback con `message_user` |
| 150–165 | T8 | `InlineModelAdmin`: `TabularInline` vs `StackedInline` en BlogApp |
| 165–175 | T9-T10 | Control de acceso + AdminSite personalizado |
| 175–180 | — | Cierre + intro TP 4 |

---

### §T1 — Sistema de permisos de Django (30 min)

#### Permisos por defecto

Para cada modelo registrado en la app, Django crea automáticamente 4 permisos:

```
<app_label>.<accion>_<model_name>

blog.add_post       → puede crear Post
blog.change_post    → puede editar Post
blog.delete_post    → puede eliminar Post
blog.view_post      → puede ver Post (read-only)
```

Se crean en `post_migrate`. Se verifican con:

```python
# En Python
user.has_perm("blog.add_post")         # True | False
user.has_module_perms("blog")          # Tiene algún perm de la app blog

# Solo superusers y is_staff tienen acceso al admin por defecto
```

#### Permisos personalizados en `Meta`

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    
    class Meta:
        permissions = [
            ("publish_post", "Puede publicar posts (marcar is_published=True)"),
            ("feature_post", "Puede destacar posts en la página principal"),
        ]
    
    # Genera: blog.publish_post y blog.feature_post
```

**Importante**: después de agregar permisos en `Meta`, ejecutar `manage.py makemigrations && migrate`.

---

### §T2 — Grupos de permisos (20 min)

```python
from django.contrib.auth.models import Group, Permission

# Crear grupos con permisos definidos
def create_roles():
    # Grupo author — puede CRUD sus propios posts
    author_group, _ = Group.objects.get_or_create(name="author")
    author_perms = Permission.objects.filter(
        content_type__app_label="blog",
        codename__in=["add_post", "change_post", "delete_post", "view_post",
                      "add_comment", "publish_post"]
    )
    author_group.permissions.set(author_perms)
    
    # Grupo reader — solo puede ver y comentar
    reader_group, _ = Group.objects.get_or_create(name="reader")
    reader_perms = Permission.objects.filter(
        content_type__app_label="blog",
        codename__in=["view_post", "add_comment"]
    )
    reader_group.permissions.set(reader_perms)

# Asignar grupo al registrar usuario
def register_user_as_author(user):
    author_group = Group.objects.get(name="author")
    user.groups.add(author_group)
    # Los permisos del grupo son efectivos en la misma request (sin refetch)
```

**Cache de permisos**: Django cachea los permisos del usuario. Si se asignan permisos y luego se verifica `has_perm()` en la misma request, puede fallar. Hacer `refetch_from_db()` o crear nuevo request.

---

### §T3a — Decoradores de autorización (15 min)

> **Contexto**: decoradores son la forma idiomática para FBV. En CBV, la forma correcta es mixins. Igual se enseñan porque el código existente los usa.

```python
from django.contrib.auth.decorators import (
    login_required, permission_required, user_passes_test
)

# @login_required — redirige a LOGIN_URL si no autenticado
@login_required
def create_post(request):
    ...

# @login_required con URL personalizada
@login_required(login_url="/accounts/login/")
def create_post(request):
    ...

# @permission_required — requiere permiso específico
@permission_required("blog.add_post", raise_exception=True)
def create_post(request):
    # raise_exception=True → 403 en lugar de redirect al login
    ...

# @user_passes_test — condición arbitraria
def is_author(user):
    return user.groups.filter(name="author").exists()

@user_passes_test(is_author, login_url="/")
def create_post(request):
    ...

# Aplicar a CBV con method_decorator (alternativa, no preferida)
from django.utils.decorators import method_decorator

@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    ...
```

---

### §T3b — Mixins CBV: el enfoque principal (25 min)

> **Regla de la cátedra**: en CBV, siempre mixins. El orden importa: primero el mixin, después la vista genérica.

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView

# LoginRequiredMixin — básico
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post-list")
    login_url = "/accounts/login/"       # override LOGIN_URL
    redirect_field_name = "next"         # nombre del query param

# PermissionRequiredMixin — con permiso específico
class PostPublishView(PermissionRequiredMixin, UpdateView):
    model = Post
    permission_required = "blog.publish_post"    # string o tupla
    raise_exception = True    # 403 en lugar de redirect al login
    # Si el usuario está logueado pero no tiene permiso → 403
    # Si no está logueado → redirect a login (con next=)
    
    def handle_no_permission(self):
        # Override para comportamiento personalizado
        if self.request.user.is_authenticated:
            raise PermissionDenied  # 403
        return super().handle_no_permission()
```

#### Protección a nivel de objeto (ownership)

Django no tiene permisos de objeto nativos en ModelBackend. Patrón estándar:

```python
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    
    def get_queryset(self):
        # Solo el autor puede editar sus propios posts
        return Post.objects.filter(author=self.request.user)
        # Si pk no corresponde al usuario → 404 automático
    
    # Alternativa con get_object():
    def get_object(self):
        obj = super().get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj
```

---

### §T4 — Autorización en templates (15 min)

```html
<!-- base.html — menú condicional -->
{% if user.is_authenticated %}
    <span>Hola, {{ user.username }}</span>
    <form method="post" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-sm btn-outline-danger">Salir</button>
    </form>
{% else %}
    <a href="{% url 'login' %}">Iniciar sesión</a>
{% endif %}

<!-- Botones condicionales por permiso -->
{% if perms.blog.add_post %}
    <a href="{% url 'blog:post-create' %}" class="btn btn-primary">Nuevo post</a>
{% endif %}

{% if perms.blog.change_post %}
    <a href="{% url 'blog:post-update' pk=post.pk %}">Editar</a>
{% endif %}

{% if perms.blog.delete_post %}
    <form method="post" action="{% url 'blog:post-delete' pk=post.pk %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger btn-sm">Eliminar</button>
    </form>
{% endif %}

<!-- Combinaciones complejas -->
{% if user.is_authenticated and perms.blog.publish_post %}
    <button>Publicar</button>
{% endif %}
```

**Nota**: `{{ perms }}` es el objeto `PermWrapper` — no es un dict. `perms.blog` retorna un `PermLookupDict` que evalúa lazy.

---

### §T5-T6 — Django Admin: setup y ModelAdmin (30 min)

#### Setup inicial

```python
# settings.py — ya está por defecto en INSTALLED_APPS
INSTALLED_APPS = [
    "django.contrib.admin",   # ← App de admin
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    ...
]
```

#### Registrar modelos — dos formas

```python
# blog/admin.py

# Forma 1: register() — simple, para modelos sin personalización
from django.contrib import admin
from .models import Category

admin.site.register(Category)

# Forma 2: @admin.register — decorador, preferida para personalización
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # List view
    list_display = ["title", "author", "is_published", "created_at"]
    list_filter = ["is_published", "author", "created_at"]
    search_fields = ["title", "body", "author__username"]
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
    list_per_page = 20
    
    # Detail view — organización en secciones
    fieldsets = [
        ("Contenido", {
            "fields": ["title", "slug", "body", "category"]
        }),
        ("Estado y autoría", {
            "fields": ["author", "is_published"],
            "classes": ["collapse"]   # sección colapsable
        }),
        ("Metadata", {
            "fields": ["created_at", "updated_at"],
            "classes": ["collapse"]
        }),
    ]
    readonly_fields = ["created_at", "updated_at", "slug"]
    prepopulated_fields = {"slug": ("title",)}   # genera slug desde title
    raw_id_fields = ["author"]   # ForeignKey con millones de usuarios: búsqueda en lugar de select
```

---

### §T7 — Acciones en masa (10 min)

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # ...
    actions = ["publish_selected", "unpublish_selected"]
    
    @admin.action(description="Publicar posts seleccionados")
    def publish_selected(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(
            request,
            f"{updated} post(s) publicado(s) exitosamente.",
            messages.SUCCESS
        )
    
    @admin.action(description="Despublicar posts seleccionados")
    def unpublish_selected(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"{updated} post(s) despublicado(s).", messages.WARNING)
```

> 🆕 **Django 6.0 — cambio de iconos en mensajes admin**: `messages.DEBUG` e `messages.INFO` ahora tienen iconos DISTINTOS de `messages.SUCCESS`.
> `message_user()` usa `messages.INFO` por defecto — para el ícono verde de éxito usar `messages.SUCCESS` explícitamente.

```python
# ✅ Correcto en Django 6.0: pasar SUCCESS para ícono verde
self.message_user(request, "Publicado.", messages.SUCCESS)
# ℹ️  INFO ahora tiene su propio ícono distinto (antes igual a SUCCESS)
```

---

### §T8 — InlineModelAdmin (15 min)

```python
# TabularInline — compacto, filas horizontales
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1             # cuántos forms vacíos mostrar
    max_num = 10          # máximo permitido
    fields = ["author", "body", "created_at"]
    readonly_fields = ["created_at"]

# StackedInline — expandido, campos apilados verticalmente
class PostImageInline(admin.StackedInline):
    model = PostImage
    extra = 0
    fields = ["image", "caption", "order"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, PostImageInline]
    # ...
```

**Cuándo usar cuál**:
- `TabularInline`: muchos items con pocos campos (ej: Comment con author + body)
- `StackedInline`: pocos items con muchos campos (ej: imagen con campos rich media)

---

### §T9-T10 — Control de acceso y AdminSite personalizado (10 min)

#### Control de acceso en ModelAdmin

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        # Solo staff con permiso blog.add_post puede crear
        return request.user.has_perm("blog.add_post")
    
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True   # puede ver la lista
        # Solo el autor puede editar su propio post (o superuser)
        return request.user == obj.author or request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser   # solo superuser puede eliminar
```

#### AdminSite personalizado (título y branding)

```python
# Forma simple — en admin.py o en AppConfig.ready()
from django.contrib import admin

admin.site.site_header = "BlogApp — Administración"
admin.site.site_title = "BlogApp Admin"
admin.site.index_title = "Panel de administración"

# 🆕 Django 6.0 — AdminSite.password_change_form
# Permite personalizar el formulario de cambio de contraseña en el admin
from myapp.forms import MyPasswordChangeForm
admin.site.password_change_form = MyPasswordChangeForm  # nuevo atributo en 6.0
```

---

## 7. Errores frecuentes anticipados

| Error | Causa | Prevención |
|-------|-------|------------|
| `AUTH_USER_MODEL` cambiado después de `migrate` | BD ya tiene tablas auth con User original | Definir en settings ANTES de cualquier migración |
| Login no redirige después del POST | Falta `next` en template o `LOGIN_REDIRECT_URL` no configurado | Siempre agregar `<input type="hidden" name="next" value="{{ next }}">`  |
| `PermissionRequiredMixin` hace loop de login | `raise_exception = False` (default) para usuario logueado sin perm | Setear `raise_exception = True` para usuarios autenticados |
| Cache de permisos stale | Permisos asignados en misma request donde se verifican | Usar nuevo request o `user = User.objects.get(pk=user.pk)` |
| `LogoutView` con GET (Django 5.x+) | Django 5+ rechaza GET en logout por CSRF | Cambiar a `<form method="post">{% csrf_token %}` |
| Admin sin `list_display` → columna "Post object (1)" | ModelAdmin sin personalizar | Siempre definir `__str__` en modelo O `list_display` en admin |
| `TabularInline` N+1 | `Comment.author` se consulta por fila | Agregar `select_related = ("author",)` en el Inline |
| `log_deletion()` o `log_action()` no existe | Removidos en **Django 6.0** (deprecated 5.1) | Usar `delete_model()` override o `LogEntry` directamente |
| `lookup_allowed()` override sin `request` param | Firma incorrecta en Django 6.0 (`request` ahora requerido) | Definir `def lookup_allowed(self, lookup, value, request):` |
| `DEFAULT_AUTO_FIELD` no declarado en Django 6.0 | 6.0 usa `BigAutoField` por defecto (antes `AutoField`) | Agregar `DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'` si se necesita int estándar |

---

## 8. Conexión con TP 4

**TP 4 — Auth + Admin completo** (entrega semana 14):
- BlogApp con login/logout/register funcional
- Roles: `author` (puede crear/editar/publicar sus posts) y `reader` (solo ver + comentar)
- `LoginRequiredMixin` en todas las vistas de escritura
- `PermissionRequiredMixin` o `get_queryset()` override para protección de objeto
- Admin con `PostAdmin` completo: list_display, fieldsets, actions, CommentInline
- Tests: `test_login_redirect`, `test_permission_denied`, `test_author_can_edit_own`, `test_reader_cannot_edit`
- Coverage ≥ 80%

---

## 9. Prerequisitos de instalación

> No hay paquetes nuevos — todo es `django.contrib` ya incluido en Django.

```
django.contrib.auth        → ya en INSTALLED_APPS por defecto
django.contrib.admin       → ya en INSTALLED_APPS por defecto
django.contrib.sessions    → ya en INSTALLED_APPS por defecto
django.contrib.messages    → ya en INSTALLED_APPS por defecto (requerido por admin)
django.contrib.contenttypes → ya en INSTALLED_APPS por defecto (base de permisos)
```

Stack: **Django 6.0** (lanzado 3 dic 2025) · **Python 3.12+** (mínimo requerido) · Bootstrap 5.3.3

> ⚠️ **Django 6.0 requiere Python 3.12 o superior.** Python 3.10 y 3.11 ya no son compatibles.

---

## 10. Mapa de dependencias entre temas

```
Tema 03 (Django, ORM básico)
   └──→ Tema 04 (ORM avanzado, View base, DTL)
          └──→ Tema 05 (CBV genéricas, ModelForm, sesiones §T5)
                  └──→ TEMA 06 (Auth + Authz + Admin) ← aquí estamos
                          └──→ Tema 07 (API REST con DRF — TokenAuth)
```

**Clausura del Módulo VI**: después de este tema, BlogApp tendrá autenticación completa, control de acceso granular y una interfaz de administración de producción. La App Integradora I cierra aquí.
