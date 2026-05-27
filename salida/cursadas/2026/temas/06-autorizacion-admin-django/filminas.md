# Filminas — Módulo VI: Autenticación, Autorización y Django Admin
# Tema 06 | Laboratorio de Programación y Lenguajes 2026
# 2 Clases teóricas — 180 min c/u | Django 5.1 · Python 3.13 · Bootstrap 5.3.3

---

# ═══════════════════════════════════════════════════════
# CLASE 1 — Autenticación Django (180 min)
# ═══════════════════════════════════════════════════════

---

## PORTADA

---

### [F1-00] Portada — Clase 1

@tipo: portada
@imagen: background
@prompt-imagen: dark background with faint lock icons and Python keyword patterns — def login logout authenticate — deep navy and teal palette, no text, blurred dark mode IDE

# Módulo VI — Autenticación Django

Quién sos y cómo lo demuestra tu aplicación web.

Semana 12 · BlogApp · `django.contrib.auth` · Django 5.1

---

## BLOQUE T1 — Sesiones Django (25 min)

---

### [F1-01] HTTP es stateless — las sesiones son el puente

@tipo: concepto-abstracto

# HTTP no recuerda al cliente — Django resuelve esto con sesiones del lado del servidor

## El problema fundamental

El protocolo HTTP procesa cada request de forma completamente independiente.
El servidor no tiene memoria de la request anterior. Pero las aplicaciones necesitan saber **"este browser ya se autenticó"**.

## La solución: sesiones

```
Browser                         Django Server
─────────────────────────────────────────────────────────
Cookie: sessionid=a1b2c3d4   →  Busca en BD:
                                  session_data para "a1b2c3d4"
                                  → request.session = {"_auth_user_id": "42"}
```

- `sessionid` — string opaco (UUID4). **No contiene datos del usuario**
- Los datos viven en el servidor, no en el browser
- El atacante no puede fabricar una `sessionid` válida — es criptográficamente aleatoria

---

### [F1-02] Backends de sesión y configuración de seguridad

@tipo: tabla

# Django tiene 4 backends de sesión — el default es BD, el de producción es cached_db

## Backends disponibles

| Backend | Almacenamiento | Uso recomendado |
|---------|---------------|-----------------|
| `db` (default) | tabla `django_session` | Desarrollo y apps de baja carga |
| `cache` | Redis / Memcached | Alta performance, sin persistencia |
| `cached_db` | Redis + BD | **Producción recomendada** |
| `file` | archivos del servidor | No distribuido — evitar |

## Settings críticos de seguridad

```python
SESSION_COOKIE_HTTPONLY = True   # JS no puede leer sessionid → anti-XSS
SESSION_COOKIE_SECURE   = True   # Solo HTTPS → producción obligatorio
SESSION_COOKIE_AGE      = 1209600  # 2 semanas en segundos (default)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
```

---

### [F1-03] Ciclo de vida completo de una sesión Django

@tipo: diagrama-flujo

# Desde el GET /login/ hasta el POST /logout/ — 5 momentos clave

## Secuencia de eventos

```
1. GET /login/
   → Django genera session_key UUID4 (sesión anónima, no autenticada)

2. POST /login/ credenciales
   → authenticate(request, username, password)
   → login(request, user)
      → INSERT django_session con session_data = {"_auth_user_id": "42"}
      → Set-Cookie: sessionid=<nueva_key>  ← rotación anti-fixation

3. Requests subsiguientes
   → Cookie sessionid → Django carga session_data
   → request.user = User(id=42)  ← AuthenticationMiddleware

4. request.user disponible en toda vista y template
   → user.is_authenticated == True

5. POST /logout/
   → session.flush()  → DELETE django_session
   → Cookie sessionid nueva vacía
   → request.user = AnonymousUser
```

## Error frecuente

`authenticate()` verifica credenciales pero **NO crea sesión**.
`login()` es obligatorio para que la sesión persista entre requests.

---

## BLOQUE T2 — django.contrib.auth (40 min)

---

### [F1-04] Mapa de componentes de django.contrib.auth

@tipo: concepto-abstracto

# django.contrib.auth no es un modelo — es un sistema completo de 7 componentes

## Arquitectura del paquete

```
django.contrib.auth
│
├── models.py      User · Group · Permission · AbstractUser · AbstractBaseUser
├── backends.py    ModelBackend (verifica credenciales contra BD)
├── middleware.py  AuthenticationMiddleware → request.user en TODA vista
├── views.py       LoginView · LogoutView · PasswordChangeView · PasswordResetView
├── forms.py       AuthenticationForm · UserCreationForm · UserChangeForm
├── decorators.py  @login_required · @permission_required · @user_passes_test
└── mixins.py      LoginRequiredMixin · PermissionRequiredMixin
```

## AuthenticationMiddleware

Sin este middleware en `MIDDLEWARE`, `request.user` no existe.
Convierte `sessionid` → `User | AnonymousUser` en cada request, antes de que llegue a la vista.

---

### [F1-05] El modelo User — campos organizados por propósito

@tipo: tabla

# User tiene 3 tipos de campos — identidad, seguridad y flags de autorización

## Campos de identidad

| Campo | Tipo | Nota |
|-------|------|------|
| `username` | CharField(150) | Único, obligatorio |
| `email` | EmailField | **No único por defecto** — trampa frecuente |
| `first_name` | CharField | Opcional |
| `last_name` | CharField | Opcional |

## Flags de autorización

| Campo | Significado |
|-------|-------------|
| `is_active` | `False` = cuenta desactivada, no eliminada (soft delete) |
| `is_staff` | `True` = puede entrar al `/admin/` |
| `is_superuser` | `True` = bypasses TODAS las verificaciones de permisos |

## Regla crítica

```python
# ❌ NUNCA — guarda texto plano
user.password = "secreto123"

# ✅ SIEMPRE — hashea con PBKDF2+SHA256
user.set_password("secreto123")
```

---

### [F1-06] AbstractUser — extensión del modelo de usuario

@tipo: codigo

# Extender AbstractUser es la forma recomendada de agregar campos personalizados

## Implementación

```python
# blog/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class BlogUser(AbstractUser):
    bio    = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    # Hereda TODOS los campos de User:
    # username, email, password, is_active, is_staff, is_superuser, groups...
```

## Registro en settings.py

```python
# settings.py  ← DEBE estar ANTES de la primera migración
AUTH_USER_MODEL = "blog.BlogUser"
```

## Importar User de forma genérica

```python
# En lugar de: from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()  # retorna BlogUser si AUTH_USER_MODEL está configurado
```

## Advertencia

Si `AUTH_USER_MODEL` se define **después** de ejecutar `migrate` → errores de migración inconsistentes → solución: borrar BD y reconstruir.

---

### [F1-07] authenticate() vs login() — la distinción crítica

@tipo: codigo

# authenticate() verifica. login() crea la sesión. Ambas son obligatorias.

## El flujo correcto

```python
from django.contrib.auth import authenticate, login

user = authenticate(request, username="juan", password="secreto")
# ┌─ authenticate() hace:
# │   → ModelBackend.authenticate()
# │   → User.check_password(raw_password)
# │   → retorna User si válido | None si inválido
# └─ NO crea sesión

if user is not None:
    login(request, user)
    # ┌─ login() hace:
    # │   → Crea fila en django_session
    # │   → Rota sessionid (previene session fixation)
    # └─  → request.user = user
    return redirect("blog:post-list")
```

## La confusión más común

```python
user = authenticate(request, username="juan", password="secreto")
# Sin login() → próxima request: request.user = AnonymousUser
# El usuario "se logueó" solo en esa función — la sesión no existe
```

---

### [F1-08] logout() — tres acciones de seguridad en una llamada

@tipo: codigo

# logout() no es solo limpiar la sesión — rota la cookie y borra los datos

## Lo que hace logout()

```python
from django.contrib.auth import logout

def cerrar_sesion(request):
    logout(request)
    # 1. session.flush() → DELETE django_session
    # 2. Genera nueva sessionid vacía → cookie actualizada
    # 3. request.user = AnonymousUser
    return redirect("blog:post-list")
```

## Django 5.x — LogoutView solo acepta POST

```html
<!-- ❌ GET rechazado en Django 5 — vulnerable a CSRF logout forzado -->
<a href="{% url 'logout' %}">Salir</a>

<!-- ✅ POST con csrf_token — único método válido -->
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit" class="btn btn-outline-secondary btn-sm">Salir</button>
</form>
```

---

## BLOQUE T3 — Vistas genéricas de auth (40 min)

---

### [F1-09] include("django.contrib.auth.urls") — 8 vistas con una línea

@tipo: codigo

# Una línea de URLconf registra todo el ciclo de autenticación de Django

## Configuración

```python
# blog_project/urls.py
from django.urls import path, include

urlpatterns = [
    path("admin/",    admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("blog/",     include("blog.urls", namespace="blog")),
]
```

## Rutas registradas automáticamente

```
accounts/login/                   → LoginView          name="login"
accounts/logout/                  → LogoutView         name="logout"
accounts/password_change/         → PasswordChangeView
accounts/password_change/done/    → PasswordChangeDoneView
accounts/password_reset/          → PasswordResetView
accounts/password_reset/done/     → PasswordResetDoneView
accounts/reset/<uidb64>/<token>/  → PasswordResetConfirmView
accounts/reset/done/              → PasswordResetCompleteView
```

`/accounts/register/` **no está incluido** — hay que implementarlo manualmente.

---

### [F1-10] LoginView — flow y configuración

@tipo: codigo

# LoginView encapsula authenticate() + login() — solo necesita template y redirect

## Flow interno

```
GET  /accounts/login/  →  render AuthenticationForm vacío
POST /accounts/login/  →  form.is_valid()
                            → authenticate()
                            → login()
                            → redirect a LOGIN_REDIRECT_URL (o ?next=)
                          form inválido → render con errores
```

## Configuración personalizada

```python
# urls.py — override de defaults
from django.contrib.auth import views as auth_views

urlpatterns += [
    path("login/",
         auth_views.LoginView.as_view(
             template_name="registration/login.html",
             redirect_authenticated_user=True,  # ya logueado → redirect directo
         ),
         name="login"),
]
```

## settings.py

```python
LOGIN_URL           = "/accounts/login/"  # destino de @login_required
LOGIN_REDIRECT_URL  = "/blog/"            # después de login exitoso
```

## El parámetro ?next=

Si la URL tiene `?next=/posts/crear/`, LoginView redirige ahí en lugar de `LOGIN_REDIRECT_URL`.
Siempre incluir en el template: `<input type="hidden" name="next" value="{{ next }}">`

---

### [F1-11] LogoutView y Django 5.x

@tipo: codigo

# LogoutView rechaza GET en Django 5 — requiere POST con csrf_token

## Cambio de comportamiento en Django 5

```python
# settings.py
LOGOUT_REDIRECT_URL = "/blog/"   # dónde va el usuario después del logout
```

```html
<!-- ❌ ROTO en Django 5 -->
<a href="/accounts/logout/">Salir</a>

<!-- ✅ CORRECTO — siempre POST -->
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit" class="btn btn-outline-danger btn-sm">Salir</button>
</form>
```

## ¿Por qué GET es peligroso para logout?

Una imagen en una página de terceros:
`<img src="https://mi-app.com/logout/">` haría logout involuntario del usuario sin su consentimiento.

---

### [F1-12] PasswordChangeView — cambio con sesión activa

@tipo: codigo

# PasswordChangeView requiere usuario logueado — verifica contraseña actual antes de cambiar

## Flow del cambio de contraseña

```python
# PasswordChangeView hace automáticamente:
# 1. Verifica old_password con check_password()
# 2. Valida new_password1 == new_password2
# 3. Ejecuta AUTH_PASSWORD_VALIDATORS sobre la nueva contraseña
# 4. user.set_password(new_password1)  ← hashea
# 5. update_session_auth_hash(request, user)  ← mantiene al usuario logueado
# 6. redirect a /accounts/password_change/done/
```

## Validators de contraseña

```python
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "...UserAttributeSimilarityValidator"},
    {"NAME": "...MinimumLengthValidator", "OPTIONS": {"min_length": 8}},
    {"NAME": "...CommonPasswordValidator"},
    {"NAME": "...NumericPasswordValidator"},
]
```

Si se omite `update_session_auth_hash()` → el usuario queda deslogueado después de cambiar la contraseña.

---

### [F1-13] PasswordResetView — flujo de 4 vistas encadenadas

@tipo: diagrama-flujo

# El reset de contraseña usa un token de un solo uso — 4 vistas en cadena

## Flujo completo

```
1. /accounts/password_reset/
   PasswordResetView → form con email
   → genera token HMAC firmado (expira según PASSWORD_RESET_TIMEOUT)
   → envía email con /reset/<uidb64>/<token>/

2. /accounts/password_reset/done/
   PasswordResetDoneView → "Revisá tu email"

3. /accounts/reset/<uidb64>/<token>/
   PasswordResetConfirmView → form nueva contraseña
   → verifica token (one-time use — se invalida al usarse)
   → user.set_password()

4. /accounts/reset/done/
   PasswordResetCompleteView → "Contraseña cambiada exitosamente"
```

## Config para desarrollo

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# Imprime el email en la consola — sin servidor SMTP
```

---

## BLOQUE T4 — Templates de autenticación (25 min)

---

### [F1-14] Naming convention registration/ — estructura obligatoria

@tipo: tabla

# Django busca templates de auth en registration/ — el nombre del archivo es el contrato

## Estructura de directorios

```
templates/
  registration/
    login.html                    ← LoginView
    password_change_form.html     ← PasswordChangeView
    password_change_done.html     ← PasswordChangeDoneView
    password_reset_form.html      ← PasswordResetView
    password_reset_done.html      ← PasswordResetDoneView
    password_reset_email.html     ← email con el link de reset
    password_reset_confirm.html   ← PasswordResetConfirmView
    password_reset_complete.html  ← PasswordResetCompleteView
  blog/
    register.html                 ← vista custom de registro
```

## settings.py — templates en raíz del proyecto

```python
TEMPLATES = [{
    "DIRS": [BASE_DIR / "templates"],  # ← busca aquí antes que en las apps
    "APP_DIRS": True,
    ...
}]
```

---

### [F1-15] Template login.html con Bootstrap — los 3 elementos críticos

@tipo: codigo

# Un template de login tiene 3 elementos sin los cuales algo se rompe

## Los 3 elementos críticos

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
            {% csrf_token %}                   {# 1. Sin esto → 403 Forbidden #}
            {{ form.as_p }}
            <input type="hidden"
                   name="next"
                   value="{{ next }}">         {# 2. Sin esto → ?next= ignorado #}
            <button type="submit"
                    class="btn btn-primary w-100">Entrar</button>
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
{# 3. Sin form.errors → el usuario no sabe por qué falló el login #}
```

---

### [F1-16] Variables de auth en templates y settings de redirect

@tipo: tabla

# El context processor auth inyecta user y perms en TODOS los templates automáticamente

## Variables disponibles sin importar nada

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `{{ user }}` | `User` o `AnonymousUser` | Usuario actual |
| `{{ user.is_authenticated }}` | bool | `True` si logueado |
| `{{ user.username }}` | str | `""` si anónimo |
| `{{ user.is_staff }}` | bool | `True` si puede usar el admin |
| `{{ perms }}` | `PermWrapper` | Verificador de permisos (Clase 2) |

## Settings de redirección

```python
LOGIN_URL           = "/accounts/login/"   # destino de @login_required
LOGIN_REDIRECT_URL  = "/blog/"             # después de login exitoso
LOGOUT_REDIRECT_URL = "/blog/"             # después de logout
```

## Navbar condicional mínimo

```html
{% if user.is_authenticated %}
    {{ user.username }}
    <form method="post" action="{% url 'logout' %}">{% csrf_token %}
        <button type="submit">Salir</button>
    </form>
{% else %}
    <a href="{% url 'login' %}">Iniciar sesión</a>
{% endif %}
```

---

## BLOQUE T5 — Registro de usuario (30 min)

---

### [F1-17] Por qué el registro no está en auth.urls

@tipo: concepto-abstracto

# Django no incluye registro porque cada aplicación define sus propios campos

## Lo que provee Django

- `UserCreationForm` — username + password1 + password2
- Validación de unicidad de `username` automática
- Validación de contraseña contra `AUTH_PASSWORD_VALIDATORS`

## Lo que implementamos nosotros

- Agregar `email` como campo **obligatorio y único**
- `CreateView` CBV para manejar el formulario
- Auto-login después del registro exitoso

## ¿Por qué email no es único por defecto?

El modelo `User` es genérico. Muchas aplicaciones usan `username` como identificador principal y el email como campo opcional. Django no impone una política — nosotros la aplicamos.

---

### [F1-18] RegisterForm — UserCreationForm con email único

@tipo: codigo

# Extender UserCreationForm para agregar email obligatorio con validación de unicidad

```python
# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Requerido. Ingresá una dirección de email válida."
    )

    class Meta:
        model  = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        """Valida unicidad de email — User.email no tiene unique=True por defecto."""
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

---

### [F1-19] RegisterView — CreateView con auto-login

@tipo: codigo

# CreateView para registro + auto-login + redirección si ya está logueado

```python
# blog/views.py
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import RegisterForm

class RegisterView(CreateView):
    form_class    = RegisterForm
    template_name = "registration/register.html"
    success_url   = reverse_lazy("blog:post-list")

    def dispatch(self, request, *args, **kwargs):
        # Si ya está logueado → no tiene sentido registrarse
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        # Asignar grupo reader por defecto
        try:
            reader_group = Group.objects.get(name="reader")
            self.object.groups.add(reader_group)
        except Group.DoesNotExist:
            pass
        # Auto-login inmediatamente después del registro
        login(self.request, self.object)
        return response
```

## URL

```python
path("register/", RegisterView.as_view(), name="register"),
```

---

### [F1-20] Template register.html — renderizado campo por campo

@tipo: codigo

# Renderizar form campo por campo permite agregar clases Bootstrap por field

```html
{% extends "base.html" %}
{% block content %}
<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-6">
      <div class="card shadow-sm">
        <div class="card-body p-4">
          <h3 class="mb-4">Crear cuenta</h3>
          <form method="post">
            {% csrf_token %}
            {% for field in form %}
            <div class="mb-3">
              <label for="{{ field.id_for_label }}" class="form-label">
                {{ field.label }}{% if field.field.required %} *{% endif %}
              </label>
              {{ field }}
              {% if field.errors %}
              <div class="invalid-feedback d-block">
                {{ field.errors|join:", " }}
              </div>
              {% endif %}
              {% if field.help_text %}
              <div class="form-text">{{ field.help_text }}</div>
              {% endif %}
            </div>
            {% endfor %}
            <button type="submit" class="btn btn-success w-100">Crear cuenta</button>
          </form>
          <hr>
          <p class="text-center mb-0">
            ¿Ya tenés cuenta? <a href="{% url 'login' %}">Iniciar sesión</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
```

---

### [F1-21] Cierre Clase 1 — estado de BlogApp + anticipo

@tipo: concepto-abstracto

# Al final de la Clase 1: BlogApp tiene autenticación completa

## Lo que tenemos

```
✅ AbstractUser extendido con bio y avatar
✅ Registro con RegisterForm (email único) + auto-login
✅ Login con LoginView + templates Bootstrap en registration/
✅ Logout con POST form (Django 5.x compatible)
✅ PasswordChangeView y PasswordResetView configuradas
✅ Variables user/perms disponibles en todos los templates
```

## Lo que FALTA — anticipo Clase 2

```
❌ Cualquier usuario logueado puede editar el post de otro
❌ No hay diferencia entre roles (autor vs lector)
❌ No hay interfaz de administración configurada
```

## La pregunta que resuelve la Clase 2

> "Juan está logueado. ¿Puede editar el post de María?"
> Respuesta actual: **sí, cualquiera puede**.
> Respuesta después de la Clase 2: **solo si tiene permiso o es el autor**.

---

# ═══════════════════════════════════════════════════════
# CLASE 2 — Autorización y Django Admin (180 min)
# ═══════════════════════════════════════════════════════

---

## PORTADA

---

### [F2-00] Portada — Clase 2

@tipo: portada
@imagen: background
@prompt-imagen: dark background showing abstract permission matrix grid, shield icons, key patterns — dark green and deep navy palette, no text labels, blurred technical aesthetic

# Módulo VI — Autorización y Django Admin

Qué puede hacer cada usuario — y cómo administrar el sistema.

Semana 13 · Permisos · Grupos · Mixins CBV · `django.contrib.admin`

---

## BLOQUE T1 — Sistema de permisos (30 min)

---

### [F2-01] Los 4 permisos automáticos de Django por modelo

@tipo: tabla

# Django crea 4 permisos automáticamente para cada modelo después de migrate

## Naming convention

```
<app_label>.<accion>_<model_name>

blog.add_post       puede crear instancias de Post
blog.change_post    puede modificar instancias de Post
blog.delete_post    puede eliminar instancias de Post
blog.view_post      puede ver instancias de Post (read-only)
```

## Verificación en Python

```python
user.has_perm("blog.add_post")       # True | False
user.has_module_perms("blog")        # True si tiene algún perm de la app
user.get_all_permissions()           # set de todos sus permisos

# Superuser: has_perm() siempre retorna True (bypasses)
# AnonymousUser: has_perm() siempre retorna False
```

## Creación

Los permisos se crean automáticamente en la señal `post_migrate`.
Sin `migrate` → no existen en la BD.

---

### [F2-02] Permisos personalizados en class Meta

@tipo: codigo

# Permisos de dominio que van más allá de add/change/delete/view

```python
# blog/models.py
class Post(models.Model):
    title        = models.CharField(max_length=200)
    author       = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    is_published = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("publish_post",  "Puede publicar posts (is_published=True)"),
            ("feature_post",  "Puede destacar posts en la portada"),
            ("moderate_post", "Puede moderar/ocultar posts de otros"),
        ]
        # Genera codenames: blog.publish_post · blog.feature_post · blog.moderate_post
```

## Flujo obligatorio

```bash
python manage.py makemigrations   # genera migración con los permisos
python manage.py migrate          # INSERT en auth_permission via post_migrate
```

## Asignar a un usuario

```python
from django.contrib.auth.models import Permission
perm = Permission.objects.get(codename="publish_post")
user.user_permissions.add(perm)
```

---

### [F2-03] Cache de permisos — trampa en la misma request

@tipo: codigo

# Django cachea permisos en el objeto User — asignar y verificar en la misma request puede fallar

## El problema

```python
def mi_vista(request):
    from django.contrib.auth.models import Permission
    perm = Permission.objects.get(codename="publish_post")
    request.user.user_permissions.add(perm)

    # ❌ FALLA — _perm_cache fue creado ANTES de agregar el permiso
    request.user.has_perm("blog.publish_post")  # → False
```

## La solución

```python
# Opción A: refetch del usuario desde BD
from django.contrib.auth import get_user_model
User = get_user_model()
fresh_user = User.objects.get(pk=request.user.pk)
fresh_user.has_perm("blog.publish_post")  # → True

# Opción B: limpiar cache manualmente
for attr in ("_perm_cache", "_user_perm_cache", "_group_perm_cache"):
    if hasattr(request.user, attr):
        delattr(request.user, attr)
request.user.has_perm("blog.publish_post")  # → True
```

---

## BLOQUE T2 — Grupos (20 min)

---

### [F2-04] Group model — asignación masiva de permisos

@tipo: codigo

# Los grupos escalan la asignación de permisos — un grupo puede tener N usuarios

```python
from django.contrib.auth.models import Group, Permission

def crear_roles():
    """Crear grupos con permisos — idempotente con get_or_create."""

    # Rol author — puede crear, editar, publicar sus posts
    author_group, _ = Group.objects.get_or_create(name="author")
    author_perms = Permission.objects.filter(
        content_type__app_label="blog",
        codename__in=[
            "add_post", "change_post", "delete_post", "view_post",
            "add_comment", "publish_post"
        ]
    )
    author_group.permissions.set(author_perms)

    # Rol reader — solo puede ver y comentar
    reader_group, _ = Group.objects.get_or_create(name="reader")
    reader_perms = Permission.objects.filter(
        content_type__app_label="blog",
        codename__in=["view_post", "add_comment"]
    )
    reader_group.permissions.set(reader_perms)
```

---

### [F2-05] Asignar grupo al registrar usuario

@tipo: codigo

# El momento natural para asignar un grupo es el registro — en form_valid de RegisterView

```python
# blog/views.py — RegisterView (Clase 1) ampliado con asignación de grupo
class RegisterView(CreateView):
    # ...

    def form_valid(self, form):
        response = super().form_valid(form)
        # Por defecto, los nuevos usuarios son readers
        try:
            reader_group = Group.objects.get(name="reader")
            self.object.groups.add(reader_group)
        except Group.DoesNotExist:
            pass  # grupo no creado aún — no es bloqueante
        login(self.request, self.object)
        return response
```

## Verificar membresía

```python
user.groups.filter(name="author").exists()     # True | False
user.groups.values_list("name", flat=True)     # <QuerySet ["reader"]>

# Para promover a author desde el admin (o un panel de moderación):
author_group = Group.objects.get(name="author")
user.groups.add(author_group)
user.groups.remove(reader_group)
```

---

## BLOQUE T3a — Decoradores (15 min)

---

### [F2-06] @login_required y @permission_required

@tipo: codigo

# Decoradores de autorización para FBV — en CBV usamos mixins (T3b)

```python
from django.contrib.auth.decorators import (
    login_required, permission_required, user_passes_test
)

# @login_required — redirige a LOGIN_URL si el usuario no está autenticado
@login_required
def create_post(request): ...

# Con URL personalizada
@login_required(login_url="/mi-login/")
def create_post(request): ...

# @permission_required — requiere permiso específico
@permission_required("blog.add_post")
def create_post(request):
    # sin permiso → redirect a LOGIN_URL (aunque esté logueado)
    ...

# raise_exception=True → 403 en lugar de redirect al login
# Usar cuando el usuario YA está logueado pero le falta el permiso
@permission_required("blog.add_post", raise_exception=True)
def create_post(request): ...
```

---

### [F2-07] @user_passes_test y method_decorator

@tipo: codigo

# @user_passes_test para condiciones arbitrarias — method_decorator para aplicar a CBV

```python
# @user_passes_test — condición customizada
def es_autor(user):
    return user.groups.filter(name="author").exists()

@user_passes_test(es_autor, login_url="/registro/")
def publicar_post(request, pk): ...

# Aplicar @login_required a CBV con method_decorator
# (alternativa a LoginRequiredMixin — no es preferida)
from django.utils.decorators import method_decorator

@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    ...
# → equivalente a LoginRequiredMixin — preferir el mixin
```

---

## BLOQUE T3b — Mixins CBV (25 min)

---

### [F2-08] LoginRequiredMixin — protección básica de CBV

@tipo: codigo

# Regla de la cátedra: en CBV, siempre mixins. El orden importa.

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# ✅ Orden correcto: mixin ANTES de la vista genérica (MRO)
class PostCreateView(LoginRequiredMixin, CreateView):
    model         = Post
    form_class    = PostForm
    template_name = "blog/post_form.html"
    success_url   = reverse_lazy("blog:post-list")
    login_url     = "/accounts/login/"  # override de LOGIN_URL settings

# ❌ Orden incorrecto — LoginRequiredMixin no intercepta
class PostCreateView(CreateView, LoginRequiredMixin):  # WRONG
    ...
```

## ¿Qué hace LoginRequiredMixin.dispatch()?

```python
# Simplificado:
def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
        return self.handle_no_permission()
        # → redirect a login_url?next=<URL actual>
    return super().dispatch(request, *args, **kwargs)
```

---

### [F2-09] PermissionRequiredMixin — verificación de permisos en CBV

@tipo: codigo

# PermissionRequiredMixin verifica permisos específicos — más granular que LoginRequiredMixin

```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class PostPublishView(PermissionRequiredMixin, UpdateView):
    model              = Post
    permission_required = "blog.publish_post"   # string o tupla (AND lógico)
    raise_exception    = True   # usuario logueado sin permiso → 403 (no redirect)
    template_name      = "blog/post_publish.html"
    fields             = ["is_published"]

# Múltiples permisos — requiere TODOS (AND)
class PostAdminView(PermissionRequiredMixin, UpdateView):
    permission_required = ("blog.change_post", "blog.publish_post")
```

## Comportamiento por estado del usuario

| Usuario | raise_exception | Resultado |
|---------|----------------|-----------|
| No logueado | False | redirect a `login?next=...` |
| No logueado | True | redirect a `login?next=...` |
| Logueado sin permiso | False | redirect a `login?next=...` (confuso) |
| Logueado sin permiso | True | **403 Forbidden** (correcto) |
| Logueado con permiso | cualquiera | ejecuta la vista |

---

### [F2-10] Protección a nivel de objeto — get_queryset() override

@tipo: codigo

# Django no tiene permisos de objeto nativos — filtrar por author es el patrón estándar

```python
# Patrón recomendado: filtrar queryset por autor
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = "blog/post_form.html"
    success_url   = reverse_lazy("blog:post-list")

    def get_queryset(self):
        # Solo el autor puede editar sus propios posts
        # Si el pk no pertenece al usuario → get_object() → Http404 automático
        return Post.objects.filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model       = Post
    success_url = reverse_lazy("blog:post-list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
```

## Alternativa explícita con PermissionDenied

```python
from django.core.exceptions import PermissionDenied

def get_object(self):
    obj = super().get_object()
    if obj.author != self.request.user:
        raise PermissionDenied   # → 403 Forbidden
    return obj
```

---

## BLOQUE T4 — Autorización en templates (15 min)

---

### [F2-11] {% if perms %} — verificación en templates

@tipo: codigo

# El objeto perms verifica has_perm() de forma lazy — disponible en todos los templates

```html
<!-- Botón condicional por permiso -->
{% if perms.blog.add_post %}
    <a href="{% url 'blog:post-create' %}" class="btn btn-primary">Nuevo post</a>
{% endif %}

<!-- Combinación de condiciones -->
{% if user.is_authenticated and perms.blog.publish_post %}
    <button class="btn btn-warning btn-sm">Publicar</button>
{% endif %}

<!-- Acciones por objeto — el autor edita/borra sus propios posts -->
{% if user == post.author or user.is_staff %}
    <a href="{% url 'blog:post-update' pk=post.pk %}">Editar</a>
    <form method="post" action="{% url 'blog:post-delete' pk=post.pk %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger btn-sm">Eliminar</button>
    </form>
{% endif %}
```

---

### [F2-12] Navbar completo con auth y permisos — base.html

@tipo: codigo

# base.html integra autenticación + autorización en la navbar

```html
<!-- templates/base.html — navbar completo -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="{% url 'blog:post-list' %}">BlogApp</a>
    <div class="navbar-nav ms-auto align-items-center">

      {% if user.is_authenticated %}
        {% if perms.blog.add_post %}
        <a class="nav-link" href="{% url 'blog:post-create' %}">Nuevo Post</a>
        {% endif %}

        <span class="navbar-text me-3">
          Hola, {{ user.username }}
          {% if user.is_staff %}<small class="text-warning">(staff)</small>{% endif %}
        </span>

        <form method="post" action="{% url 'logout' %}" class="d-inline">
          {% csrf_token %}
          <button type="submit" class="btn btn-outline-light btn-sm">Salir</button>
        </form>

      {% else %}
        <a class="nav-link" href="{% url 'login' %}">Iniciar sesión</a>
        <a class="nav-link" href="{% url 'register' %}">Registrarse</a>
      {% endif %}

    </div>
  </div>
</nav>
```

---

## BLOQUE T5-T6 — Django Admin (30 min)

---

### [F2-13] Admin setup — register() vs @admin.register

@tipo: codigo

# @admin.register es el decorador preferido — más legible y organizado para ModelAdmin complejo

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Comment

# Forma 1: admin.site.register() — simple, sin personalización
admin.site.register(Category)
# → muestra "Category object (N)" — poco útil

# Forma 2: @admin.register — decorador para personalización completa
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass   # ModelAdmin vacío = mismo resultado que register()

# Prerequisitos en INSTALLED_APPS (ya están por defecto):
# "django.contrib.admin"
# "django.contrib.contenttypes"  ← base del sistema de permisos
# "django.contrib.sessions"      ← sesiones para el admin
# "django.contrib.messages"      ← requerido por admin para feedback
```

---

### [F2-14] ModelAdmin — list view: list_display, list_filter, search_fields

@tipo: codigo

# list_display, list_filter y search_fields transforman la list view del admin

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # ─── List view ──────────────────────────────────────────
    list_display   = ["title", "author", "is_published", "created_at"]
    # Puede incluir nombres de campo, métodos del modelo o callables del admin

    list_filter    = ["is_published", "author", "created_at"]
    # Sidebar derecho con filtros de un click

    search_fields  = ["title", "body", "author__username"]
    # search_fields usa ILIKE — author__username hace JOIN automático

    ordering       = ["-created_at"]
    date_hierarchy = "created_at"     # barra drill-down por fecha
    list_per_page  = 20

    # Columna personalizada con ícono booleano
    @admin.display(description="Publicado", boolean=True)
    def publicado(self, obj):
        return obj.is_published
    # list_display = [..., "publicado"]  → muestra ✓/✗ en lugar de True/False
```

---

### [F2-15] ModelAdmin — detail view: fieldsets y readonly_fields

@tipo: codigo

# fieldsets organiza el formulario de edición en secciones colapsables

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # ─── Detail view ────────────────────────────────────────
    fieldsets = [
        ("Contenido", {
            "fields": ["title", "slug", "body", "category"]
        }),
        ("Estado y autoría", {
            "fields":   ["author", "is_published"],
            "classes": ["collapse"]   # sección colapsable por defecto
        }),
        ("Timestamps", {
            "fields":   ["created_at", "updated_at"],
            "classes": ["collapse"]
        }),
    ]

    readonly_fields     = ["created_at", "updated_at", "slug"]
    prepopulated_fields = {"slug": ("title",)}   # auto-genera slug desde title
    raw_id_fields       = ["author"]
    # raw_id_fields: reemplaza <select> con miles de opciones
    # por un campo de búsqueda con popup — esencial para FKs con muchos registros
```

---

## BLOQUE T7 — Acciones en masa (10 min)

---

### [F2-16] @admin.action — acciones personalizadas sobre QuerySet

@tipo: codigo

# Las acciones operan sobre el queryset de los registros seleccionados

```python
from django.contrib import admin, messages

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ["publish_selected", "unpublish_selected"]

    @admin.action(description="✅ Publicar posts seleccionados")
    def publish_selected(self, request, queryset):
        # queryset.update() → UNA sola query SQL para todos los seleccionados
        updated = queryset.update(is_published=True)
        self.message_user(
            request,
            f"{updated} post(s) publicado(s) exitosamente.",
            messages.SUCCESS
        )

    @admin.action(description="❌ Despublicar posts seleccionados")
    def unpublish_selected(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"{updated} despublicado(s).", messages.WARNING)
```

## queryset.update() vs loop con save()

| Método | Queries | Signals `post_save` |
|--------|---------|---------------------|
| `queryset.update()` | 1 (eficiente) | NO se disparan |
| loop + `obj.save()` | N (uno por objeto) | Sí se disparan |

---

## BLOQUE T8 — InlineModelAdmin (15 min)

---

### [F2-17] TabularInline vs StackedInline en PostAdmin

@tipo: codigo

# Inlines permiten editar modelos relacionados directamente desde el admin del padre

```python
# TabularInline — filas horizontales, compacto (muchos items, pocos campos)
class CommentInline(admin.TabularInline):
    model           = Comment
    extra           = 1        # forms vacíos extra
    max_num         = 20
    fields          = ["author", "body", "created_at"]
    readonly_fields = ["created_at"]
    # select_related previene N+1 al cargar la lista de comentarios
    def get_queryset(self, request):
        return super().get_queryset(request).select_related("author")

# StackedInline — campos apilados, expandido (pocos items, muchos campos)
class PostMetaInline(admin.StackedInline):
    model  = PostMeta    # hipotético modelo de metadata SEO
    extra  = 0
    fields = ["og_title", "og_description", "canonical_url"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
```

## Cuándo usar cada uno

| Inline | Cuándo usar |
|--------|-------------|
| `TabularInline` | Muchos items con pocos campos (Comment: author + body) |
| `StackedInline` | Pocos items con muchos campos (metadata, configuración) |

---

## BLOQUE T9-T10 — Control de acceso y AdminSite (10 min)

---

### [F2-18] has_*_permission() — control granular en ModelAdmin

@tipo: codigo

# has_change_permission(request, obj) permite lógica de ownership en el admin

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return request.user.has_perm("blog.add_post")

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True   # puede ver la list view
        # Solo el autor o superuser puede editar el objeto específico
        return obj.author == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser   # solo superuser borra

    def has_view_permission(self, request, obj=None):
        return True   # cualquier staff puede ver
```

## Nota sobre obj=None

Django llama `has_change_permission(request, obj=None)` para la list view.
Si retorna `False` para `obj=None` → el botón "Editar" no aparece en la lista completa.

---

### [F2-19] AdminSite — branding personalizado

@tipo: codigo

# Cambiar el título del admin es una línea — AdminSite custom es para proyectos con múltiples admins

```python
# blog/admin.py — branding simple
from django.contrib import admin

admin.site.site_header = "BlogApp — Administración"
admin.site.site_title  = "BlogApp"
admin.site.index_title = "Panel de administración"
```

## AdminSite custom (para múltiples sitios en un proyecto)

```python
class BlogAdminSite(admin.AdminSite):
    site_header = "BlogApp — Admin personalizado"
    site_title  = "BlogApp Admin"
    index_title = "Gestión de contenido"

blog_admin = BlogAdminSite(name="blog_admin")
blog_admin.register(Post, PostAdmin)
blog_admin.register(Comment)

# urls.py
path("blog-admin/", blog_admin.urls),
```

---

## CIERRE CLASE 2

---

### [F2-20] Cierre — BlogApp completa y TP 4

@tipo: portada
@imagen: none

# Módulo VI completo — BlogApp tiene auth + authz + admin de producción

## Estado final de BlogApp

```
Clase 1 + Clase 2:
✅ Registro, login, logout — templates Bootstrap, Django 5.x compatible
✅ AbstractUser extendido (bio, avatar)
✅ Roles: author (CRUD propio) / reader (solo ver + comentar)
✅ LoginRequiredMixin en todas las vistas de escritura
✅ get_queryset() protege edición/borrado por propietario → Http404
✅ {% if perms %} y {% if user.is_authenticated %} en base.html
✅ PostAdmin: list_display · fieldsets · search · acciones · CommentInline
✅ has_change_permission() protege ownership en el admin
```

## TP 4 — Auth + Admin completo (entrega semana 14)

- Login / logout / registro funcionando
- Roles `author` / `reader` con permisos correctos
- `LoginRequiredMixin` + `get_queryset()` para ownership
- `PostAdmin` con `CommentInline` y acción `publish_selected`
- Tests: login redirect · 403 sin permiso · autor edita propio · reader no puede
- Coverage ≥ 80%

## Próximo módulo: REST API con Django REST Framework

Semana 15 — Tema 07: `Serializer`, `ViewSet`, `Router`, `TokenAuthentication`
