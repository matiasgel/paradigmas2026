# Django 6.0 — User Authentication System
**Documentation version:** 6.0
**Source:** https://docs.djangoproject.com/en/6.0/topics/auth/ and /topics/auth/default/

## Overview

Django's authentication system handles both authentication AND authorization.
- **Authentication**: verifies a user is who they claim to be
- **Authorization**: determines what an authenticated user is allowed to do

Components: Users, Permissions, Groups, configurable password hashing, forms/view tools, pluggable backends.

## Installation

Required in `INSTALLED_APPS`:
- `'django.contrib.auth'` — core auth framework and default models
- `'django.contrib.contenttypes'` — allows permissions associated with models

Required in `MIDDLEWARE`:
- `SessionMiddleware` — manages sessions across requests
- `AuthenticationMiddleware` — associates users with requests using sessions

## User Objects

The primary attributes of the default User model:
- `username`, `password`, `email`, `first_name`, `last_name`
- `is_active` (bool), `is_staff` (bool), `is_superuser` (bool)
- `groups` (M2M), `user_permissions` (M2M)
- `last_login`, `date_joined`

```python
# Creating users
from django.contrib.auth.models import User
user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

# Creating superusers
python manage.py createsuperuser --username=joe --email=joe@example.com

# Changing passwords (never manipulate password attribute directly)
u = User.objects.get(username="john")
u.set_password("new password")
u.save()
```

## Authenticating Users

```python
from django.contrib.auth import authenticate, login

user = authenticate(request, username=username, password=password)
if user is not None:
    login(request, user)
    # success

# Async versions (Django 6.0):
user = await aauthenticate(request, username=username, password=password)
await alogin(request, user)
```

## Session Authentication (web requests)

```python
# request.user is always available
if request.user.is_authenticated:
    # authenticated user
else:
    # AnonymousUser

# Async version (Django 6.0):
user = await request.auser()
if user.is_authenticated:
    pass
```

## Login/Logout Functions

```python
from django.contrib.auth import login, logout

# Login: saves user ID in session
login(request, user)  # or alogin() async

# Logout: cleans out ALL session data for current request
logout(request)  # or alogout() async
```

## Limiting Access to Logged-in Users

### Raw Way
```python
from django.conf import settings
from django.shortcuts import redirect

def my_view(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
```

### @login_required Decorator (for FBV — use only when no CBV alternative)
```python
from django.contrib.auth.decorators import login_required

@login_required  # redirects to LOGIN_URL if not authenticated
def my_view(request): ...

@login_required(login_url="/accounts/login/")  # custom login URL
def my_view(request): ...
```

### LoginRequiredMixin (PRIMARY CBV approach — preferred)
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    raise_exception = False  # True → 403 instead of redirect
```

### login_not_required Decorator (Django 6.0 — NEW)
When `LoginRequiredMiddleware` is installed (all views require auth by default),
use `login_not_required` to exempt views like the login view itself:
```python
from django.contrib.auth.decorators import login_not_required

@login_not_required
def login_view(request): ...
```

### AccessMixin Base Class
Used by LoginRequiredMixin and PermissionRequiredMixin:
- `login_url`: URL to redirect unauthorized users to (defaults to `settings.LOGIN_URL`)
- `permission_denied_message`: message passed to error handler
- `redirect_field_name`: name of query param (default `"next"`)
- `raise_exception`: if True → PermissionDenied (403) instead of redirect

## Permissions and Authorization

### Default Permissions
Django auto-creates 4 permissions per model: `add`, `change`, `delete`, `view`.

```python
# Check permissions
user.has_perm('foo.add_bar')    # app_label.action_modelname
user.has_perm('foo.change_bar')
user.has_perm('foo.delete_bar')
user.has_perm('foo.view_bar')

# Module-level check
user.has_module_perms('foo')  # has any permissions in app 'foo'
```

### Custom Permissions in Model Meta
```python
class Post(models.Model):
    class Meta:
        permissions = [
            ("can_publish", "Can publish posts"),
            ("can_feature", "Can feature posts"),
        ]
```

### Groups
```python
from django.contrib.auth.models import Group

# User in a group gets all group permissions
myuser.groups.set([group_list])
myuser.groups.add(group)
myuser.groups.remove(group)
myuser.groups.clear()
myuser.user_permissions.add(permission)
myuser.user_permissions.remove(permission)
```

### Programmatically Creating Permissions
```python
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(BlogPost)
permission = Permission.objects.create(
    codename="can_publish",
    name="Can Publish Posts",
    content_type=content_type,
)
```

### Permission Caching Warning
`ModelBackend` caches permissions on the user object after first fetch.
After adding permissions in same request, re-fetch user: `user = User.objects.get(pk=user_id)`
(Note: `user.refresh_from_db()` does NOT clear permission cache)

### @permission_required Decorator (FBV)
```python
from django.contrib.auth.decorators import permission_required

@permission_required("polls.add_choice")
def my_view(request): ...

# Multiple permissions (user must have ALL)
@permission_required(["polls.add_choice", "polls.change_choice"])
def my_view(request): ...

# raise_exception=True → 403 instead of redirect
@login_required
@permission_required("polls.add_choice", raise_exception=True)
def my_view(request): ...
```

### PermissionRequiredMixin (PRIMARY CBV approach — preferred)
```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = "polls.add_choice"
    # Multiple permissions:
    permission_required = ["polls.view_choice", "polls.change_choice"]

    # Override for dynamic logic:
    def has_permission(self):
        return self.request.user.has_perm("polls.add_choice")
```

### UserPassesTestMixin (CBV with custom test)
```python
from django.contrib.auth.mixins import UserPassesTestMixin

class MyView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.email.endswith("@example.com")
```

### @user_passes_test Decorator (FBV)
```python
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_active and u.profile.role == 'author')
def my_view(request): ...
```

## Authentication Views (Generic Class-Based Views)

### URL Configuration
```python
# Include all auth URLs at once
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
# Provides: login/, logout/, password_change/, password_change/done/,
#           password_reset/, password_reset/done/, reset/<uid>/<token>/, reset/done/
```

### LoginView
- URL name: `login`
- Template: `registration/login.html` (default)
- Attributes: `template_name`, `next_page` (→LOGIN_REDIRECT_URL), `redirect_field_name` ('next'),
  `authentication_form` (default: AuthenticationForm), `extra_context`, `redirect_authenticated_user`
- Template context: `form`, `next`, `site`, `site_name`

### LogoutView
- URL name: `logout`
- Logs out on POST requests
- Attributes: `next_page` (→LOGOUT_REDIRECT_URL), `template_name`, `redirect_field_name`

### PasswordChangeView
- URL name: `password_change`
- Attributes: `template_name`, `success_url` (→'password_change_done'), `form_class` (PasswordChangeForm)
- Template: `registration/password_change_form.html`

### PasswordResetView
- URL name: `password_reset`
- Sends email with one-time reset link
- Template: `registration/password_reset_form.html`

### Settings for Auth URLs
```python
LOGIN_URL = '/accounts/login/'          # default
LOGIN_REDIRECT_URL = '/accounts/profile/'  # default  
LOGOUT_REDIRECT_URL = None              # default
```

## Session Invalidation on Password Change
When user changes password, all sessions are invalidated (logged out everywhere).
Built-in views handle this automatically. For custom views, use:
```python
from django.contrib.auth import update_session_auth_hash
update_session_auth_hash(request, form.user)
# Async: await aupdate_session_auth_hash(request, form.user)
```

## Auth Templates Context Variables

In templates (with RequestContext):
```django
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}.</p>
{% endif %}

{# Check permissions #}
{% if perms.blog %}          {# any permission in blog app #}
{% if perms.blog.add_post %}  {# specific permission #}
{% if 'blog.add_post' in perms %}  {# alternative syntax #}
```

## Built-in Forms

- `AuthenticationForm` — login form (takes `request` as first arg)
- `UserCreationForm` — create user (username, password1, password2)
- `BaseUserCreationForm` — recommended base for custom user creation
- `PasswordChangeForm` — change password (takes `user` kwarg)
- `PasswordResetForm` — request password reset by email
- `SetPasswordForm` — set new password without old password
- `UserChangeForm` — admin: change user info and permissions
- `AdminPasswordChangeForm` — admin: change user password
- `AdminUserCreationForm` — admin: create user (inherits UserCreationForm)

## Customizing User Model (AbstractUser pattern)

```python
# models.py — ALWAYS do this before first migration
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ('author', 'Author'),
        ('reader', 'Reader'),
    ])
    bio = models.TextField(blank=True)

# settings.py
AUTH_USER_MODEL = 'myapp.User'
```

## Password Hashing (Django 6.0)

Django stores passwords as: `<algorithm>$<iterations>$<salt>$<hash>`
PBKDF2 is default hasher.
**Django 6.0**: PBKDF2 iteration count increased from 1,000,000 to **1,200,000**.

Django never stores raw passwords. Always use `set_password()`, never assign directly.

## Managing Users in Admin

When `django.contrib.admin` and `django.contrib.auth` are both installed:
- Users section under "Auth" in admin index
- Add user page requires username + password before other fields
- Can grant/revoke permissions, add to groups
- Password details displayed (not the password), with link to change form
