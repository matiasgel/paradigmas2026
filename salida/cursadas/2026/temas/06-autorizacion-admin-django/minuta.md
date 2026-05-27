# Minuta de Clase — Tema 06: Autenticación, Autorización y Django Admin
## Módulo VI completo | 2 Clases Teóricas | 180 min c/u | Semanas 12–13

> **Documento para el docente.** Cada sección corresponde a una filmina (`filminas.md`).
> El docente puede dar la clase utilizando únicamente este archivo.

---

## Metadatos

| Campo | Valor |
|-------|-------|
| Fecha estimada | Semanas 12–13 — IF009 2026 |
| Duración total | 2 × 180 minutos |
| Dominio | BlogApp — `Post`, `Category`, `Comment` + `BlogUser` (AbstractUser) |
| Stack | Django 5.1 · Python 3.13 · Bootstrap 5.3.3 |
| Prerequisito confirmado | Tema 05: CBV genéricas, ModelForm, templates herencia, sesiones §T5 |
| Estilo pedagógico | Expositivo con preguntas socráticas — CBV + Mixins obligatorio, FBV prohibido |

---

# CLASE 1 — Autenticación Django (180 min)

## Agenda Clase 1

| Tiempo | Bloque | Filminas |
|--------|--------|---------|
| 0–10 min | Apertura: el arco auth → authz | F1-00 |
| 10–35 min | **§T1** Sesiones Django: backends, ciclo de vida | F1-01 a F1-03 |
| 35–75 min | **§T2** `django.contrib.auth`: User, AbstractUser, authenticate/login/logout | F1-04 a F1-08 |
| 75–115 min | **§T3** Vistas genéricas de auth: LoginView, LogoutView, PasswordChangeView | F1-09 a F1-13 |
| 115–140 min | **§T4** Templates de autenticación: naming, settings, context | F1-14 a F1-16 |
| 140–175 min | **§T5** Registro de usuario: UserCreationForm + CreateView | F1-17 a F1-20 |
| 175–180 min | Cierre + anticipo Clase 2 | F1-21 |

---

## APERTURA CLASE 1

### [F1-00] Portada — Apertura (10 min)

**Guion**:
> "En el Tema 05 le dimos una interfaz web completa a BlogApp: cualquiera puede ver posts, crear posts, borrar posts. ¿Eso es bueno? No. Cualquiera puede borrar el trabajo de otro. Hoy empezamos a resolver eso en dos pasos. Paso uno hoy: autenticación — quién sos. Paso dos en la Clase 2: autorización — qué podés hacer."

**Dibujar en pizarrón** (o mostrar diagrama):
```
AUTENTICACIÓN          AUTORIZACIÓN
"¿Quién sos?"    →     "¿Qué podés hacer?"
   login()               has_perm()
   User model            Group / Permission
```

**Pregunta activadora**: *"¿Alguien puede describir la diferencia entre autenticación y autorización con un ejemplo de la vida real?"*

**Respuesta esperada**: pasaporte (autenticación) vs. permiso de ingreso a una zona restringida (autorización).

**Transición**: *"Django separa estas dos responsabilidades en el mismo paquete: `django.contrib.auth`. Pero antes de llegar al User, necesitamos entender sobre qué mecanismo se apoya todo: las sesiones."*

---

## BLOQUE T1 — Sesiones Django (25 min)

### [F1-01] Sesiones: el puente entre HTTP stateless y el estado de usuario (8 min)

**Guion**:
> "HTTP es un protocolo sin estado — cada request es independiente, el servidor no recuerda al cliente. Pero una aplicación web necesita saber 'este browser ya se logueó'. Las sesiones son la solución de Django: un diccionario del lado del servidor, indexado por un ID de sesión que viaja en una cookie."

**Conceptos clave**:
- `request.session` — dict-like, disponible en toda vista
- `sessionid` cookie — string opaco (UUID4), NO contiene datos del usuario
- El servidor guarda los datos; la cookie solo contiene la llave

**Dibujo en pizarrón**:
```
Browser                  Django Server
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cookie: sessionid=abc → Busca en BD: session_data para "abc"
                         request.session = {"user_id": 42, "_auth_user_..."}
```

**Pregunta anticipada**: *"¿Por qué no guardar el user_id directamente en la cookie?"*
**Respuesta**: el cliente podría modificar la cookie y suplantar a otro usuario. Con la cookie solo siendo un índice, el atacante no puede fabricar sesiones válidas.

---

### [F1-02] Backends de sesión y configuración (8 min)

**Guion**:
> "Django tiene 4 backends de sesión. El default es base de datos — la tabla `django_session`. Para producción con alta carga se usa `cached_db`: Redis como cache con BD como respaldo."

**Mostrar tabla de backends**:
```
BACKEND                                      USO RECOMENDADO
django_session (db)         → default, simple, auditeable
django.backends.cache       → Redis/Memcached — rápido, sin persistencia
django.backends.cached_db   → Redis + BD — producción de alta carga
django.backends.file        → desarrollo, no distribuido
```

**Settings críticos de seguridad**:
```python
SESSION_COOKIE_HTTPONLY = True   # JS no puede leer sessionid → previene XSS
SESSION_COOKIE_SECURE   = True   # Solo HTTPS → producción
SESSION_COOKIE_AGE      = 1209600  # 2 semanas (default)
```

**Pregunta anticipada**: *"¿Qué pasa si no ponemos `HTTPONLY = True`?"*
**Respuesta**: un script XSS podría robar la cookie de sesión y hacer session hijacking.

---

### [F1-03] Ciclo de vida de la sesión (9 min)

**Guion**:
> "Veamos qué pasa exactamente desde que el usuario ingresa su contraseña hasta que cierra sesión. Son 5 momentos clave."

**Secuencia completa**:
```
1. GET /login/    → Django genera session_key UUID4 (anónima)
2. POST /login/   → authenticate() verifica credenciales → login() crea sesión
                    → INSERT en django_session + Set-Cookie: sessionid=<key>
3. Requests sgts  → Cookie sessionid → request.session cargado desde BD
4. request.user   → AnonymousUser (sin auth) | User (con auth)
5. POST /logout/  → session.flush() DELETE django_session + nueva cookie vacía
```

**Error frecuente para anticipar**: *"¿Qué pasa si llamo `authenticate()` pero olvido llamar `login()`?"*
**Respuesta**: `authenticate()` solo verifica — NO crea sesión. La siguiente request tendrá `request.user = AnonymousUser`.

**Transición**: *"Ahora que entendemos el mecanismo de sesiones, veamos el sistema completo que Django construye sobre él."*

---

## BLOQUE T2 — `django.contrib.auth` (40 min)

### [F1-04] Arquitectura de django.contrib.auth (7 min)

**Guion**:
> "El paquete auth de Django tiene 7 componentes. No es solo un modelo de usuario — es un sistema completo. Hoy usamos todos."

**Mostrar mapa de componentes**:
```
django.contrib.auth
├── models.py      → User, Group, Permission, AbstractUser
├── backends.py    → ModelBackend (quién verifica credenciales)
├── middleware.py  → AuthenticationMiddleware → request.user siempre disponible
├── views.py       → LoginView, LogoutView, PasswordChangeView...
├── forms.py       → AuthenticationForm, UserCreationForm, UserChangeForm
├── decorators.py  → @login_required, @permission_required
└── mixins.py      → LoginRequiredMixin, PermissionRequiredMixin
```

**Punto importante**: `AuthenticationMiddleware` es el que pone `request.user` en cada request. Sin él en `MIDDLEWARE`, no hay `request.user`.

---

### [F1-05] El modelo User — campos y flags (8 min)

**Guion**:
> "El modelo `User` tiene tres tipos de campos: identidad, seguridad y flags de autorización. Hay trampas frecuentes que vamos a anticipar."

**Mostrar campos organizados**:
```python
# Identidad
user.username    # max 150, único, obligatorio
user.email       # EmailField — ¡NO único por defecto! Trampa frecuente.
user.first_name  # opcional
user.last_name   # opcional

# Seguridad (internos)
user.password    # NUNCA texto plano — PBKDF2+SHA256+iteraciones
user.last_login  # DateTimeField
user.date_joined # DateTimeField

# Flags de autorización
user.is_active    # False = desactivado (NO eliminado) → soft delete
user.is_staff     # True = puede entrar al /admin/
user.is_superuser # True = bypasses ALL permission checks
```

**Error crítico para marcar**:
```python
# ❌ NUNCA hacer esto
user.password = "secreto123"

# ✅ Siempre
user.set_password("secreto123")
# set_password hace: hashea + itera PBKDF2 + guarda
```

**Pregunta**: *"¿Por qué `is_active = False` en lugar de borrar el usuario?"*
**Respuesta**: preserva el historial (posts del usuario, auditoría), cumple regulaciones de retención de datos.

---

### [F1-06] AbstractUser — extensión del modelo de usuario (10 min)

**Guion**:
> "El User de Django no tiene avatar ni bio. Para agregar campos personalizados, extendemos `AbstractUser`. La regla de oro: hacerlo ANTES de la primera migración."

**Código completo**:
```python
# blog/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class BlogUser(AbstractUser):
    bio    = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    # Todos los campos de User siguen disponibles:
    # username, email, first_name, last_name, is_staff, is_active...

# settings.py  ← CRÍTICO: antes de la primera migración
AUTH_USER_MODEL = "blog.BlogUser"
```

**Advertencia en negrita**:
> Si `AUTH_USER_MODEL` se define DESPUÉS de ejecutar `migrate`, Django lanzará errores de migración inconsistentes. La solución: borrar la BD y reconstruir desde cero.

**Impacto en el código existente**:
```python
# En lugar de importar User directamente, usar get_user_model()
from django.contrib.auth import get_user_model
User = get_user_model()  # retorna BlogUser (o User si no hay AUTH_USER_MODEL)
```

---

### [F1-07] authenticate() y login() — la distinción crítica (8 min)

**Guion**:
> "Dos funciones, dos responsabilidades distintas. Confundirlas es el error más común al implementar login manual."

```python
from django.contrib.auth import authenticate, login, logout

# authenticate() — SOLO verifica credenciales, NO crea sesión
user = authenticate(request, username="juan", password="secreto")
# Retorna: User si credenciales válidas | None si inválidas

if user is not None:
    login(request, user)
    # login() hace 3 cosas:
    # 1. Crea la sesión en django_session
    # 2. Rota la sessionid (previene session fixation)
    # 3. Pone request.user = user
    return redirect("blog:post-list")
else:
    # credenciales inválidas
    pass
```

**Diagrama de secuencia**:
```
POST /login/ credenciales
    → authenticate(request, username, password)
         → ModelBackend.authenticate()
              → User.check_password(raw_password)
                   → True? retorna User | False? retorna None
    → login(request, user) → sesión creada → sessionid rotada
    → redirect()
```

**Rotación de sessionid**: previene "session fixation attack" — un atacante que inyectó una sessionid conocida antes del login no puede usarla después, porque se genera una nueva.

---

### [F1-08] logout() — limpieza completa de sesión (7 min)

**Guion**:
> "logout() hace tres cosas. Si solo hacés una de las tres, dejás agujeros de seguridad."

```python
from django.contrib.auth import logout

def cerrar_sesion(request):
    logout(request)
    # 1. Borra session data de la BD → session.flush()
    # 2. Regenera sessionid → cookie nueva vacía
    # 3. Pone request.user = AnonymousUser
    return redirect("blog:post-list")
```

**Django 5.x — cambio importante**:
```html
<!-- ❌ ROTO en Django 5: LogoutView rechaza GET por seguridad CSRF -->
<a href="/accounts/logout/">Salir</a>

<!-- ✅ CORRECTO: siempre POST con csrf_token -->
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit">Salir</button>
</form>
```

**¿Por qué GET está prohibido para logout?** Un `<img src="/logout/">` en una página de terceros haría logout involuntario (CSRF via GET).

**Transición**: *"Implementar authenticate/login/logout manualmente es posible, pero Django ya tiene vistas listas que hacen todo esto. Las vemos ahora."*

---

## BLOQUE T3 — Vistas genéricas de autenticación (40 min)

### [F1-09] include("django.contrib.auth.urls") — todo con una línea (7 min)

**Guion**:
> "Django incluye vistas listas para todo el ciclo de auth. Con una sola línea de URLconf tenemos login, logout, cambio de contraseña y reset."

```python
# blog_project/urls.py
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("blog/", include("blog.urls", namespace="blog")),
]
```

**Rutas registradas automáticamente**:
```
accounts/login/                    → LoginView         (name="login")
accounts/logout/                   → LogoutView        (name="logout")
accounts/password_change/          → PasswordChangeView
accounts/password_change/done/     → PasswordChangeDoneView
accounts/password_reset/           → PasswordResetView
accounts/password_reset/done/      → PasswordResetDoneView
accounts/reset/<uidb64>/<token>/   → PasswordResetConfirmView
accounts/reset/done/               → PasswordResetCompleteView
```

**Registro** (`/accounts/register/`) NO está incluido — hay que implementarlo. Lo veremos en §T5.

---

### [F1-10] LoginView — configuración y flow (10 min)

**Guion**:
> "LoginView ya tiene toda la lógica de authenticate + login. Solo necesitamos darle un template y decirle a dónde redirigir."

**Flow interno de LoginView**:
```
GET  /accounts/login/  → instancia AuthenticationForm → render template vacío
POST /accounts/login/  → form.is_valid() → authenticate() → login() → redirect
                       → form inválido → render template con errores
```

**Configuración explícita (override de defaults)**:
```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns += [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,  # ya logueado → redirect directo
        ),
        name="login",
    ),
]
```

**Settings en settings.py**:
```python
LOGIN_REDIRECT_URL  = "/blog/"           # después de login exitoso
LOGIN_URL           = "/accounts/login/" # donde redirige @login_required
```

**El parámetro `?next=`**: si la URL tiene `?next=/posts/crear/`, LoginView redirige ahí en lugar de `LOGIN_REDIRECT_URL`. **Siempre** incluir en el template:
```html
<input type="hidden" name="next" value="{{ next }}">
```

---

### [F1-11] LogoutView en Django 5.x (5 min)

**Guion**:
> "LogoutView cambió en Django 5: ahora solo acepta POST. Esto es una decisión de seguridad — CSRF protection para logout."

```python
# settings.py
LOGOUT_REDIRECT_URL = "/blog/"

# template — OBLIGATORIO usar form POST
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit" class="btn btn-outline-secondary btn-sm">Salir</button>
</form>
```

**Recordatorio**: `next_page` o `LOGOUT_REDIRECT_URL` — si ambos están definidos, `next_page` gana.

---

### [F1-12] PasswordChangeView — cambio de contraseña con sesión activa (8 min)

**Guion**:
> "PasswordChangeView requiere usuario logueado. Verifica la contraseña actual, valida la nueva con los PASSWORD_VALIDATORS y hace set_password + re-login automático."

```python
# Flow de PasswordChangeView
# 1. Renderiza PasswordChangeForm (old_password + new_password1 + new_password2)
# 2. old_password → check_password() → verifica contraseña actual
# 3. new_password1 == new_password2 → validate_password() (validators)
# 4. set_password(new_password1) → re-hashea
# 5. update_session_auth_hash(request, user)  ← clave: mantiene al usuario logueado
# 6. redirect a /accounts/password_change/done/

# Si NO se usa update_session_auth_hash → usuario queda deslogueado al cambiar contraseña
```

**Validators de contraseña en settings.py**:
```python
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
     "OPTIONS": {"min_length": 8}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
```

---

### [F1-13] PasswordResetView — flujo de 4 pasos (10 min)

**Guion**:
> "El reset de contraseña es el flujo más complejo de auth. Son 4 vistas encadenadas con un token temporal de un solo uso."

**Flujo completo**:
```
1. /accounts/password_reset/
   → PasswordResetView: form con email
   → Genera token firmado con HMAC (válido por PASSWORD_RESET_TIMEOUT segundos)
   → Envía email con link /reset/<uidb64>/<token>/

2. /accounts/password_reset/done/
   → PasswordResetDoneView: "Revisá tu email"

3. /accounts/reset/<uidb64>/<token>/
   → PasswordResetConfirmView: form nueva contraseña
   → Verifica que token no fue usado (one-time use)
   → set_password()

4. /accounts/reset/done/
   → PasswordResetCompleteView: "Contraseña cambiada"
```

**Config para desarrollo** (email a consola):
```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

**Seguridad del token**: usa `django.utils.crypto.salted_hmac` + timestamp. Expiración configurable con `PASSWORD_RESET_TIMEOUT` (default: 3 días).

---

## BLOQUE T4 — Templates de autenticación (25 min)

### [F1-14] Naming convention — carpeta registration/ (8 min)

**Guion**:
> "Las vistas de auth buscan sus templates en `registration/` por convención. Si el template no está ahí, Django levanta `TemplateDoesNotExist`."

**Estructura obligatoria**:
```
templates/
  registration/
    login.html                    ← LoginView
    password_change_form.html     ← PasswordChangeView
    password_change_done.html     ← PasswordChangeDoneView
    password_reset_form.html      ← PasswordResetView
    password_reset_done.html      ← PasswordResetDoneView
    password_reset_email.html     ← email que se envía
    password_reset_confirm.html   ← PasswordResetConfirmView
    password_reset_complete.html  ← PasswordResetCompleteView
  blog/
    register.html                 ← vista custom de registro
```

**Configuración en settings.py** (necesaria si templates está en raíz del proyecto):
```python
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],   # ← busca aquí primero
    "APP_DIRS": True,
    ...
}]
```

---

### [F1-15] Template login.html completo con Bootstrap (10 min)

**Guion**:
> "El template de login tiene tres elementos críticos: csrf_token, el campo `next` oculto, y los errores del formulario. Cualquiera de los tres que falte rompe algo."

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
          <div class="alert alert-danger">
            Usuario o contraseña incorrectos.
          </div>
          {% endif %}

          <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            {# next: LoginView redirige aquí después del login #}
            <input type="hidden" name="next" value="{{ next }}">
            <button type="submit" class="btn btn-primary w-100">Entrar</button>
          </form>

          <hr>
          <p class="text-center mb-0">
            ¿No tenés cuenta?
            <a href="{% url 'register' %}">Registrate</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
```

**Los tres errores del template de login**:
1. Olvidar `{% csrf_token %}` → `403 Forbidden` en el POST
2. Olvidar `<input name="next">` → después del login no redirige al destino original
3. No mostrar `form.errors` → usuario no sabe por qué falló el login

---

### [F1-16] Variables de auth en templates y settings de redirect (7 min)

**Guion**:
> "El context processor `django.template.context_processors.auth` inyecta automáticamente `user` y `perms` en todos los templates. Sin importar nada."

**Variables disponibles en cualquier template**:
```html
{{ user }}                      <!-- User o AnonymousUser -->
{{ user.username }}             <!-- string o "" -->
{{ user.is_authenticated }}     <!-- True | False -->
{{ user.is_staff }}             <!-- True | False -->
{{ user.get_full_name }}        <!-- first_name + last_name -->

<!-- Condicional básico en base.html -->
{% if user.is_authenticated %}
    Hola, {{ user.username }}
    <form method="post" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit">Salir</button>
    </form>
{% else %}
    <a href="{% url 'login' %}">Iniciar sesión</a>
{% endif %}
```

**Settings de redirect (resumen)**:
```python
LOGIN_URL           = "/accounts/login/"   # destino de @login_required
LOGIN_REDIRECT_URL  = "/blog/"             # después de login exitoso
LOGOUT_REDIRECT_URL = "/blog/"             # después de logout
```

---

## BLOQUE T5 — Registro de usuario (30 min)

### [F1-17] Por qué el registro no está en auth.urls (5 min)

**Guion**:
> "Django no incluye vista de registro en `auth.urls`. La razón: cada aplicación define sus propios campos de registro. Django no puede saber si quieren username, email, nombre completo o cualquier combinación. Provee el formulario base — nosotros construimos la vista."

**Lo que provee Django**:
- `UserCreationForm` — formulario con username + password1 + password2
- Validación automática de unicidad de username
- Validación de contraseña contra AUTH_PASSWORD_VALIDATORS

**Lo que hacemos nosotros**:
- Agregar campo `email` como obligatorio y único
- `CreateView` CBV para manejar la lógica
- Auto-login después del registro

---

### [F1-18] UserCreationForm — extensión con email único (10 min)

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

**Por qué `clean_email()`**: `User.email` no tiene `unique=True` por defecto. Sin esta validación, dos usuarios pueden registrarse con el mismo email y el reset de contraseña enviará al primero que encuentre.

---

### [F1-19] RegisterView con CBV — CreateView (12 min)

```python
# blog/views.py
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import RegisterForm

class RegisterView(CreateView):
    form_class   = RegisterForm
    template_name = "registration/register.html"
    success_url  = reverse_lazy("blog:post-list")

    def dispatch(self, request, *args, **kwargs):
        # Si ya está logueado, no tiene sentido registrarse
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        # Auto-login: el usuario queda logueado inmediatamente tras registrarse
        login(self.request, self.object)
        return response
```

**URL**:
```python
# blog/urls.py o accounts/urls.py
path("register/", RegisterView.as_view(), name="register"),
```

**El flujo completo**:
```
GET  /register/  → form vacío (RegisterForm)
POST /register/  → form.is_valid() → user.save() → login(request, user) → redirect
                → form inválido → redisplay con errores campo por campo
```

---

### [F1-20] Template register.html (8 min)

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

**Renderizado campo por campo** vs `{{ form.as_p }}`: permite agregar clases Bootstrap por campo. Para campos de password, Django renderiza `<input type="password">` automáticamente.

---

## CIERRE CLASE 1

### [F1-21] Cierre y anticipo Clase 2 (5 min)

**Resumen de la Clase 1**:
```
✅ Sesiones: mecanismo base, backends, ciclo de vida
✅ django.contrib.auth: User, AbstractUser, authenticate/login/logout
✅ Vistas genéricas: LoginView, LogoutView, PasswordChangeView, PasswordResetView
✅ Templates registration/: naming convention, login.html, variables de context
✅ Registro: UserCreationForm extendido, CreateView con auto-login
```

**Estado de BlogApp al final de Clase 1**:
- Los usuarios pueden registrarse, iniciar y cerrar sesión
- Los formularios de auth tienen templates Bootstrap
- Cualquier usuario logueado puede crear/editar/borrar posts de cualquier otro

**Pregunta de anticipo**: *"¿Cómo evitamos que Juan edite el post de María?"*

**Transición a Clase 2**: *"Eso es autorización. En la Clase 2: permisos, grupos, mixins CBV y el admin de Django completo."*

---

---

# CLASE 2 — Autorización y Django Admin (180 min)

## Agenda Clase 2

| Tiempo | Bloque | Filminas |
|--------|--------|---------|
| 0–5 min | Apertura: auth ≠ authz | F2-00 |
| 5–35 min | **§T1** Sistema de permisos: por defecto + personalizados | F2-01 a F2-03 |
| 35–55 min | **§T2** Grupos: Group model, roles BlogApp | F2-04 a F2-05 |
| 55–70 min | **§T3a** Decoradores: @login_required, @permission_required | F2-06 a F2-07 |
| 70–95 min | **§T3b** Mixins CBV: LoginRequiredMixin, PermissionRequiredMixin | F2-08 a F2-10 |
| 95–110 min | **§T4** Templates: {% if perms %} | F2-11 a F2-12 |
| 110–120 min | **§T5** Admin setup: register vs @admin.register | F2-13 |
| 120–140 min | **§T6** ModelAdmin avanzado: list_display, fieldsets | F2-14 a F2-15 |
| 140–150 min | **§T7** Acciones en masa | F2-16 |
| 150–165 min | **§T8** InlineModelAdmin: TabularInline vs StackedInline | F2-17 |
| 165–175 min | **§T9–T10** Control de acceso admin + AdminSite | F2-18 a F2-19 |
| 175–180 min | Cierre + intro TP 4 | F2-20 |

---

## APERTURA CLASE 2

### [F2-00] Apertura — auth ≠ authz (5 min)

**Guion**:
> "Al final de la Clase 1, BlogApp tiene registro y login funcionando. Pero cualquier usuario logueado puede borrar el post de cualquier otro. Hoy resolvemos eso con el sistema de autorización de Django."

**Distinción clara**:
```
AUTENTICACIÓN (Clase 1)        AUTORIZACIÓN (Clase 2)
¿Quién sos?                    ¿Qué podés hacer?
login() / logout()             has_perm() / Group
authenticate()                 LoginRequiredMixin
User model                     PermissionRequiredMixin
Sesiones                       @login_required / @permission_required
```

---

## BLOQUE T1 — Sistema de permisos (30 min)

### [F2-01] Los 4 permisos por defecto de Django (10 min)

**Guion**:
> "Cada vez que Django crea una migración para un modelo nuevo, genera automáticamente 4 permisos para ese modelo. Están disponibles después de ejecutar `migrate`."

**Los 4 permisos automáticos**:
```
<app_label>.<accion>_<model_name>

blog.add_post     → puede crear instancias de Post
blog.change_post  → puede modificar instancias de Post
blog.delete_post  → puede eliminar instancias de Post
blog.view_post    → puede ver instancias de Post (read-only)
```

**Verificación en Python**:
```python
# has_perm siempre retorna False para usuarios anónimos
user.has_perm("blog.add_post")          # True | False
user.has_perm("blog.add_post", obj)     # object-level (requiere backend custom)
user.has_module_perms("blog")           # True si tiene algún perm de la app
```

**En el shell de Django** (para demostración):
```python
from django.contrib.auth import get_user_model
User = get_user_model()
u = User.objects.get(username="juan")
u.has_perm("blog.add_post")   # → True/False
u.get_all_permissions()       # set de strings con todos sus permisos
```

---

### [F2-02] Permisos personalizados en Meta (10 min)

**Guion**:
> "Los 4 permisos por defecto no alcanzan para todos los casos de negocio. Para permisos propios del dominio, los definimos en la Meta del modelo."

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
            ("publish_post",  "Puede publicar posts (marcar is_published=True)"),
            ("feature_post",  "Puede destacar posts en la portada"),
            ("moderate_post", "Puede moderar/ocultar posts de otros usuarios"),
        ]
        # Genera: blog.publish_post, blog.feature_post, blog.moderate_post
```

**Paso obligatorio después de agregar `permissions`**:
```bash
python manage.py makemigrations
python manage.py migrate
# Los permisos se crean en la tabla auth_permission via post_migrate signal
```

**Asignar permiso a usuario en shell**:
```python
from django.contrib.auth.models import Permission
perm = Permission.objects.get(codename="publish_post")
user.user_permissions.add(perm)
```

---

### [F2-03] Cache de permisos — trampa frecuente (10 min)

**Guion**:
> "Django cachea los permisos del usuario en el objeto User para no consultar la BD en cada has_perm(). Esto tiene una trampa: si asignás permisos en una view y los verificás en la misma request, el cache todavía tiene los permisos viejos."

**El problema**:
```python
def assign_and_check(request):
    user = request.user
    perm = Permission.objects.get(codename="publish_post")
    user.user_permissions.add(perm)

    # ❌ Falla — el cache de _perm_cache no se actualizó
    user.has_perm("blog.publish_post")  # → False (cache stale)
```

**La solución**:
```python
# Opción A: refetch desde BD
from django.contrib.auth import get_user_model
User = get_user_model()
fresh_user = User.objects.get(pk=user.pk)
fresh_user.has_perm("blog.publish_post")  # → True

# Opción B: limpiar cache manualmente
if hasattr(user, "_perm_cache"):
    del user._perm_cache
if hasattr(user, "_user_perm_cache"):
    del user._user_perm_cache
user.has_perm("blog.publish_post")  # → True
```

---

## BLOQUE T2 — Grupos de permisos (20 min)

### [F2-04] Group model — asignación masiva de permisos (10 min)

**Guion**:
> "Asignar permisos usuario por usuario no escala. Los grupos resuelven esto: asignás permisos al grupo una vez, y cualquier usuario en ese grupo los hereda automáticamente."

```python
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Post

def crear_roles():
    """Idempotente: get_or_create para no duplicar."""

    # Grupo author — puede CRUD posts propios + publicar
    author_group, _ = Group.objects.get_or_create(name="author")
    author_perms = Permission.objects.filter(
        content_type__app_label="blog",
        codename__in=["add_post", "change_post", "delete_post",
                      "view_post", "add_comment", "publish_post"]
    )
    author_group.permissions.set(author_perms)

    # Grupo reader — solo puede ver y comentar
    reader_group, _ = Group.objects.get_or_create(name="reader")
    reader_perms = Permission.objects.filter(
        content_type__app_label="blog",
        codename__in=["view_post", "add_comment"]
    )
    reader_group.permissions.set(reader_perms)
```

**Mejor lugar para ejecutar esto**: `AppConfig.ready()` o un management command `python manage.py create_roles`.

---

### [F2-05] Asignar grupo al registrar usuario (10 min)

**Guion**:
> "El momento natural para asignar un grupo es en el registro. Lo hacemos en form_valid de RegisterView."

```python
# blog/views.py
from django.contrib.auth.models import Group

class RegisterView(CreateView):
    # ...
    def form_valid(self, form):
        response = super().form_valid(form)
        # Asignar grupo por defecto al nuevo usuario
        try:
            reader_group = Group.objects.get(name="reader")
            self.object.groups.add(reader_group)
        except Group.DoesNotExist:
            pass   # grupo no existe aún, no es bloqueante
        login(self.request, self.object)
        return response
```

**Verificar membresía en grupo**:
```python
user.groups.filter(name="author").exists()   # True | False
user.groups.values_list("name", flat=True)   # ["reader"] o ["author"]
```

---

## BLOQUE T3a — Decoradores de autorización (15 min)

### [F2-06] @login_required y @permission_required (8 min)

**Guion**:
> "Los decoradores son la forma idiomática para vistas FBV. Vamos a verlos porque el código existente los usa. Pero en nuestras CBV usamos mixins."

```python
from django.contrib.auth.decorators import (
    login_required, permission_required, user_passes_test
)

# @login_required — redirige a LOGIN_URL si no autenticado
@login_required
def create_post(request):
    ...

# Con URL de login personalizada
@login_required(login_url="/mi-login/")
def create_post(request):
    ...

# @permission_required — requiere permiso específico
@permission_required("blog.add_post")
def create_post(request):
    # usuario sin permiso → redirect a LOGIN_URL (aunque esté logueado)
    ...

# raise_exception=True → 403 en lugar de redirect al login
@permission_required("blog.add_post", raise_exception=True)
def create_post(request):
    ...
```

---

### [F2-07] @user_passes_test y method_decorator para CBV (7 min)

```python
# @user_passes_test — condición arbitraria
def es_autor(user):
    return user.groups.filter(name="author").exists()

@user_passes_test(es_autor, login_url="/registro/")
def publicar_post(request, pk):
    ...

# Aplicar decorador a CBV — no idiomático, preferir mixins
from django.utils.decorators import method_decorator

@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    ...
# equivalente a poner LoginRequiredMixin — usar mixin en su lugar
```

---

## BLOQUE T3b — Mixins CBV (25 min)

### [F2-08] LoginRequiredMixin — protección básica (8 min)

**Guion**:
> "La regla de la cátedra: en CBV, siempre mixins. El orden importa: primero el mixin, después la vista genérica."

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostCreateView(LoginRequiredMixin, CreateView):
    model         = Post
    form_class    = PostForm
    template_name = "blog/post_form.html"
    success_url   = reverse_lazy("blog:post-list")

    # Personalización opcional
    login_url          = "/accounts/login/"  # override LOGIN_URL
    redirect_field_name = "next"             # nombre del query param
```

**Por qué el orden importa**: Python MRO (Method Resolution Order). `LoginRequiredMixin.dispatch()` se ejecuta antes que `CreateView.dispatch()`. Si el orden está invertido, el mixin no intercepta.

**¿Qué hace `LoginRequiredMixin.dispatch()`?**:
```python
# Internamente (simplificado):
def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
        return self.handle_no_permission()
        # → redirect a login_url?next=<URL actual>
    return super().dispatch(request, *args, **kwargs)
```

---

### [F2-09] PermissionRequiredMixin — control de permisos en CBV (10 min)

```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class PostPublishView(PermissionRequiredMixin, UpdateView):
    model              = Post
    permission_required = "blog.publish_post"  # string o tupla
    raise_exception    = True   # 403 en lugar de redirect al login
    template_name      = "blog/post_publish_confirm.html"
    fields             = ["is_published"]

# Múltiples permisos (AND lógico — requiere TODOS)
class PostAdminView(PermissionRequiredMixin, UpdateView):
    permission_required = ("blog.change_post", "blog.publish_post")
```

**Comportamiento según estado del usuario**:
```
Usuario no logueado + raise_exception=False → redirect a login?next=...
Usuario no logueado + raise_exception=True  → redirect a login?next=...
Usuario logueado + sin permiso + raise_exception=False → redirect a login
Usuario logueado + sin permiso + raise_exception=True  → 403 Forbidden
Usuario logueado + con permiso → ejecuta la vista normal
```

**Regla**: si el usuario ya está logueado pero le falta permiso, siempre usar `raise_exception=True` — redirigirlo al login es confuso (ya está logueado).

---

### [F2-10] Protección a nivel de objeto con get_queryset() (7 min)

**Guion**:
> "Django no tiene permisos de objeto out-of-the-box con ModelBackend. El patrón estándar: filtrar el queryset por `author=request.user`. Si el pk no corresponde al usuario → 404 automático."

```python
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = "blog/post_form.html"
    success_url   = reverse_lazy("blog:post-list")

    def get_queryset(self):
        # Solo el autor puede editar sus propios posts
        # Si pk no corresponde al usuario → get_object() → Http404
        return Post.objects.filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post-list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
```

**Alternativa con get_object()** (más explícita):
```python
from django.core.exceptions import PermissionDenied

def get_object(self):
    obj = super().get_object()
    if obj.author != self.request.user:
        raise PermissionDenied   # 403 explícito
    return obj
```

---

## BLOQUE T4 — Autorización en templates (15 min)

### [F2-11] {% if perms %} — el objeto PermWrapper (7 min)

**Guion**:
> "`{{ perms }}` no es un diccionario — es un `PermWrapper` que hace lazy evaluation. Cada acceso a `perms.blog` genera un `PermLookupDict` que consulta `has_perm()` solo cuando se evalúa."

```html
<!-- Botón condicional por permiso -->
{% if perms.blog.add_post %}
    <a href="{% url 'blog:post-create' %}" class="btn btn-primary">
        Nuevo post
    </a>
{% endif %}

<!-- Combinación de condiciones -->
{% if user.is_authenticated and perms.blog.publish_post %}
    <button class="btn btn-warning btn-sm">Publicar</button>
{% endif %}

<!-- Acciones en lista de posts -->
{% for post in posts %}
    <div class="card mb-3">
        <div class="card-body">
            <h5>{{ post.title }}</h5>
            {% if user == post.author or user.is_staff %}
                <a href="{% url 'blog:post-update' pk=post.pk %}">Editar</a>
                <form method="post" action="{% url 'blog:post-delete' pk=post.pk %}"
                      style="display:inline">
                    {% csrf_token %}
                    <button type="submit" class="btn btn-danger btn-sm">Eliminar</button>
                </form>
            {% endif %}
        </div>
    </div>
{% endfor %}
```

---

### [F2-12] Navbar condicional — auth completa en base.html (8 min)

```html
<!-- templates/base.html — navbar completo con auth -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{% url 'blog:post-list' %}">BlogApp</a>
        <div class="navbar-nav ms-auto">
            {% if user.is_authenticated %}
                {% if perms.blog.add_post %}
                <a class="nav-link" href="{% url 'blog:post-create' %}">
                    Nuevo Post
                </a>
                {% endif %}
                <span class="navbar-text me-2">{{ user.username }}</span>
                <form method="post" action="{% url 'logout' %}" class="d-inline">
                    {% csrf_token %}
                    <button type="submit" class="btn btn-outline-light btn-sm">
                        Salir
                    </button>
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

## BLOQUE T5–T6 — Django Admin (30 min)

### [F2-13] Admin setup: register() vs @admin.register (10 min)

**Guion**:
> "La app de admin de Django genera una interfaz CRUD completa para cualquier modelo registrado. El `/admin/` que vieron desde Tema 03 se configura en `blog/admin.py`."

**Las dos formas de registrar un modelo**:

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Comment

# Forma 1: register() — simple, sin personalización
admin.site.register(Category)
# → columna "Category object (N)" — poco útil sin __str__ o list_display

# Forma 2: @admin.register — decorador, para personalización
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass   # ModelAdmin vacío = mismo resultado que register()

# Forma 2 equivalente:
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)
```

**Prerequisitos para que el admin funcione**:
```python
# settings.py — INSTALLED_APPS
"django.contrib.admin",           # la app del admin
"django.contrib.contenttypes",    # base del sistema de permisos
"django.contrib.sessions",        # sesiones para el admin
"django.contrib.messages",        # mensajes de feedback (requerido por admin)
```

---

### [F2-14] ModelAdmin — list view personalizada (12 min)

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # ─── List view ───────────────────────────────
    list_display  = ["title", "author", "is_published", "created_at"]
    # list_display puede incluir:
    # - nombres de campo del modelo
    # - métodos del modelo con short_description
    # - callables del ModelAdmin

    list_filter   = ["is_published", "author", "created_at"]
    # Agrega sidebar con filtros de click

    search_fields = ["title", "body", "author__username"]
    # search_fields usa LIKE — para campos con __ usa JOIN automático

    ordering      = ["-created_at"]
    date_hierarchy = "created_at"   # barra de drill-down por fecha
    list_per_page  = 20

    # Método personalizado para list_display
    @admin.display(description="Estado", boolean=True)
    def publicado(self, obj):
        return obj.is_published
    # → muestra ícono ✓/✗ en lugar de True/False
```

---

### [F2-15] ModelAdmin — detail view con fieldsets (8 min)

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # ─── Detail view ────────────────────────────
    fieldsets = [
        ("Contenido", {
            "fields": ["title", "slug", "body", "category"]
        }),
        ("Estado y autoría", {
            "fields": ["author", "is_published"],
            "classes": ["collapse"]   # sección colapsable
        }),
        ("Timestamps (solo lectura)", {
            "fields": ["created_at", "updated_at"],
            "classes": ["collapse"]
        }),
    ]
    readonly_fields     = ["created_at", "updated_at", "slug"]
    prepopulated_fields = {"slug": ("title",)}   # auto-genera slug desde title
    raw_id_fields       = ["author"]
    # raw_id_fields: reemplaza el <select> de FK por un campo de búsqueda
    # → esencial cuando hay miles de usuarios en el select
```

---

## BLOQUE T7 — Acciones en masa (10 min)

### [F2-16] @admin.action — acciones personalizadas (10 min)

**Guion**:
> "Las acciones permiten operar sobre múltiples registros seleccionados en la list view. El admin tiene 'Eliminar seleccionados' por defecto — podemos agregar las nuestras."

```python
from django.contrib import admin, messages

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ["publish_selected", "unpublish_selected"]

    @admin.action(description="✅ Publicar posts seleccionados")
    def publish_selected(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(
            request,
            f"{updated} post(s) publicado(s) exitosamente.",
            messages.SUCCESS
        )

    @admin.action(description="❌ Despublicar posts seleccionados")
    def unpublish_selected(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(
            request,
            f"{updated} post(s) despublicado(s).",
            messages.WARNING
        )
```

**`queryset.update()`** vs loop con `save()`:
- `update()` → una sola query SQL (eficiente para masa)
- loop con `save()` → N queries + dispara signals per-object (si importa la señal `post_save`)

---

## BLOQUE T8 — InlineModelAdmin (15 min)

### [F2-17] TabularInline vs StackedInline en PostAdmin (15 min)

**Guion**:
> "Los Inlines permiten editar modelos relacionados directamente desde el admin del modelo padre. `Comment` se edita dentro de la página de `Post`."

```python
# TabularInline — compacto, filas horizontales (ideal para muchos items)
class CommentInline(admin.TabularInline):
    model          = Comment
    extra          = 1         # forms vacíos extra a mostrar
    max_num        = 20        # máximo permitido
    fields         = ["author", "body", "created_at"]
    readonly_fields = ["created_at"]
    select_related  = ("author",)   # previene N+1 al cargar la lista

# StackedInline — expandido verticalmente (ideal para pocos items con muchos campos)
class PostImageInline(admin.StackedInline):
    model  = PostImage
    extra  = 0
    fields = ["image", "caption", "order"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    # ...
```

**Cuándo usar cuál**:
```
TabularInline   → muchos items, pocos campos por item (Comment: author + body)
StackedInline   → pocos items, muchos campos por item (PostImage con metadata)
```

**N+1 en Inlines**: sin `select_related`, cada fila de `CommentInline` genera una query para cargar `author`. Siempre definir `select_related` en Inlines con ForeignKey.

---

## BLOQUE T9–T10 — Control de acceso y AdminSite (10 min)

### [F2-18] has_*_permission() — control de acceso granular en admin (6 min)

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return request.user.has_perm("blog.add_post")

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True   # puede ver la lista (sin obj específico)
        # Solo el autor puede editar su propio post, o superuser
        return obj.author == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Solo superuser puede eliminar desde el admin
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return True   # todos los staff pueden ver
```

**`obj` puede ser `None`**: cuando Django renderiza la list view, llama `has_change_permission(request, obj=None)`. Si retorna `False` para `obj=None`, el botón de editar no aparece en la lista.

---

### [F2-19] AdminSite — branding personalizado (4 min)

```python
# blog/admin.py — branding simple (o en AppConfig.ready())
from django.contrib import admin

admin.site.site_header = "BlogApp — Administración"
admin.site.site_title  = "BlogApp"
admin.site.index_title = "Panel de administración"
```

**AdminSite custom** (para múltiples sitios admin en un proyecto):
```python
class BlogAdminSite(admin.AdminSite):
    site_header = "BlogApp — Admin personalizado"

blog_admin = BlogAdminSite(name="blog_admin")
blog_admin.register(Post, PostAdmin)

# urls.py
path("blog-admin/", blog_admin.urls),
```

---

## CIERRE CLASE 2

### [F2-20] Cierre — estado final de BlogApp y TP 4 (5 min)

**Estado final de BlogApp después de Módulo VI**:
```
✅ Registro, login y logout con templates Bootstrap
✅ AbstractUser extendido con bio y avatar
✅ Roles: author (puede CRUD) / reader (solo lectura + comentar)
✅ LoginRequiredMixin en todas las vistas de escritura
✅ get_queryset() protegiendo edición/borrado por autor
✅ Admin completo: PostAdmin con list_display, fieldsets, acciones, inline
✅ has_change_permission() protegiendo posts por propietario en el admin
```

**TP 4 — Auth + Admin completo** (entrega semana 14):
- BlogApp con login/logout/register funcionando
- Roles author/reader con permisos correctos
- `LoginRequiredMixin` + `get_queryset()` para ownership
- `PostAdmin` completo con `CommentInline` y acción `publish_selected`
- Tests: login redirect, 403 sin permiso, autor puede editar propio, reader no puede
- Coverage ≥ 80%

**Pregunta de cierre**: *"¿Qué problema resuelve `PermissionRequiredMixin` que `LoginRequiredMixin` no resuelve?"*
**Respuesta esperada**: que el usuario esté logueado no es suficiente — `LoginRequiredMixin` solo verifica autenticación. `PermissionRequiredMixin` verifica que el usuario logueado tenga un permiso específico.
