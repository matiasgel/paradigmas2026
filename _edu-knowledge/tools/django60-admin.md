# Django 6.0 — Admin Site
**Documentation version:** 6.0
**Source:** https://docs.djangoproject.com/en/6.0/ref/contrib/admin/

## Overview

The Django admin is an automatic admin interface that reads metadata from models.
Intended for organization's internal management (not for building complete frontends).

## Installation / Requirements

In `INSTALLED_APPS`:
```python
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.messages',
'django.contrib.sessions',
```
In `MIDDLEWARE`: `SessionMiddleware`, `AuthenticationMiddleware`, `MessageMiddleware`
In `TEMPLATES` context_processors: `request`, `django.contrib.auth.context_processors.auth`, `django.contrib.messages.context_processors.messages`

## Registering Models

```python
from django.contrib import admin
from myapp.models import Author, Post

# Simple registration (default ModelAdmin)
admin.site.register(Author)

# With custom ModelAdmin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
admin.site.register(Author, AuthorAdmin)

# Using @register decorator (preferred)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'status']
    list_filter = ['status', 'created_at', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ['title']}
```

## ModelAdmin Options (Key Attributes)

### Display Options
```python
class PostAdmin(admin.ModelAdmin):
    # Columns shown in changelist
    list_display = ['title', 'author', 'published_date', 'is_published']
    
    # Sidebar filters (right side)
    list_filter = ['status', 'created_at', 'author']
    
    # Search box fields
    search_fields = ['title', 'body', 'author__username']
    
    # Clickable columns for change form (default: first column)
    list_display_links = ['title']
    
    # Editable columns inline in changelist
    list_editable = ['status']
    
    # Date hierarchy navigation at top
    date_hierarchy = 'published_date'
    
    # Default ordering
    ordering = ['-published_date']
    
    # Number of items per page (default: 100)
    list_per_page = 25
```

### Form Layout Options
```python
class PostAdmin(admin.ModelAdmin):
    # Simple list of fields in order
    fields = ['title', 'slug', 'body', 'author']
    
    # Grouped fieldsets (overrides fields if set)
    fieldsets = [
        (None, {
            'fields': ['title', 'slug', 'body'],
        }),
        ('Publishing', {
            'fields': ['author', 'status', 'published_date'],
            'classes': ['collapse'],  # collapsible section
        }),
    ]
    
    # Read-only fields (displayed but not editable)
    readonly_fields = ['created_at', 'updated_at', 'author_display']
    
    # Exclude from form
    exclude = ['internal_notes']
    
    # Auto-populate slug from title
    prepopulated_fields = {'slug': ['title']}
```

### Permission Methods
```python
class PostAdmin(admin.ModelAdmin):
    # Object-level permission checks
    def has_view_permission(self, request, obj=None):
        # True → show in admin; False → hidden
        return True

    def has_add_permission(self, request):
        return request.user.has_perm('blog.add_post')

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True  # changelist access
        return obj.author == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
```

### Custom Actions
```python
from django.contrib import admin
from django.contrib import messages

class PostAdmin(admin.ModelAdmin):
    actions = ['publish_posts', 'unpublish_posts']
    
    @admin.action(description="Publish selected posts")
    def publish_posts(self, request, queryset):
        count = queryset.update(status='published')
        self.message_user(
            request,
            f"{count} posts published.",
            messages.SUCCESS  # Django 6.0: use SUCCESS for green checkmark icon
        )
    
    @admin.action(description="Unpublish selected posts")  
    def unpublish_posts(self, request, queryset):
        queryset.update(status='draft')
        self.message_user(request, "Posts unpublished.")
        # Note: message_user() default is messages.INFO (Django 6.0 INFO has distinct icon)
```

### ModelAdmin.message_user() — Django 6.0 CHANGE
In Django 6.0, `messages.DEBUG` and `messages.INFO` now have **distinct icons** from `messages.SUCCESS`.
Previously, all three showed the same green checkmark icon.
- `message_user()` uses `messages.INFO` by default
- **If you want the old "success" green icon → explicitly pass `messages.SUCCESS`**

```python
# Django 6.0: INFO and SUCCESS now display differently
self.message_user(request, "Done.", messages.SUCCESS)  # green checkmark ✓
self.message_user(request, "Done.", messages.INFO)     # distinct info icon (new)
self.message_user(request, "Warning.", messages.WARNING)
self.message_user(request, "Error occurred.", messages.ERROR)
```

## ModelAdmin Methods (Hooks)

```python
class PostAdmin(admin.ModelAdmin):
    
    # Override save behavior
    def save_model(self, request, obj, form, change):
        if not change:  # new object
            obj.author = request.user
        super().save_model(request, obj, form, change)
    
    # Override delete behavior (REMOVED log_deletion in Django 6.0)
    def delete_model(self, request, obj):
        super().delete_model(request, obj)
    
    # Filter queryset for changelist
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    
    # Dynamic readonly fields
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['author', 'created_at']
        return ['created_at']
```

## REMOVED in Django 6.0: log_deletion and log_action

**`ModelAdmin.log_deletion()` and `LogEntryManager.log_action()` are REMOVED in Django 6.0** (deprecated since 5.1).
If you need to log model changes use `LogEntry` directly or `save_model()`/`delete_model()` overrides.

```python
# WRONG (removed in 6.0):
# self.log_deletion(request, object, object_repr)
# LogEntry.objects.log_action(...)

# CORRECT: use save_model()/delete_model() hooks or LogEntry directly:
from django.contrib.admin.models import LogEntry, DELETION

def delete_model(self, request, obj):
    LogEntry.objects.create(
        user_id=request.user.pk,
        content_type_id=get_content_type_for_model(obj).pk,
        object_id=obj.pk,
        object_repr=str(obj),
        action_flag=DELETION,
    )
    super().delete_model(request, obj)
```

## CHANGED in Django 6.0: lookup_allowed Signature

Subclasses that override `lookup_allowed()` MUST include `request` in signature:

```python
# Django 6.0 REQUIRED signature:
def lookup_allowed(self, lookup, value, request):
    # request is now required (was optional in 5.x)
    return super().lookup_allowed(lookup, value, request)
```

## Inline Models (TabularInline / StackedInline)

```python
class CommentInline(admin.TabularInline):
    model = Comment        # required
    extra = 1              # extra blank forms (default: 3)
    max_num = 10           # max forms allowed
    can_delete = True      # show delete checkbox (default: True)
    fields = ['author', 'body', 'approved']
    readonly_fields = ['created_at']
    
    def has_add_permission(self, request, obj):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]  # list of inline classes

class CommentStackedInline(admin.StackedInline):
    # Same options as TabularInline, different visual layout
    model = Comment
    extra = 0
    show_change_link = True  # link to full change form for each inline
```

## AdminSite Customization

```python
from django.contrib import admin

# Customize existing site
admin.site.site_header = "Blog Administration"   # top of every admin page
admin.site.site_title = "Blog Site Admin"        # <title> tag suffix  
admin.site.index_title = "Welcome to Blog Admin" # index page heading

# NEW in Django 6.0: password_change_form
# Customize the form used in admin password change view
from myapp.forms import MyPasswordChangeForm
admin.site.password_change_form = MyPasswordChangeForm
```

### Custom AdminSite (for multi-site setups)
```python
# admin.py
from django.contrib import admin

class MyAdminSite(admin.AdminSite):
    site_header = "My Custom Admin"
    login_template = "admin/my_login.html"
    # Django 6.0 NEW: password_change_form attribute
    password_change_form = MyPasswordChangeForm

admin_site = MyAdminSite(name="myadmin")

# urls.py
from myapp.admin import admin_site
urlpatterns = [
    path("myadmin/", admin_site.urls),
]
```

## AdminSite Attributes

```python
# Templates
admin.site.login_template = "admin/login.html"
admin.site.logout_template = "admin/logged_out.html"
admin.site.password_change_template = "admin/password_change_form.html"
admin.site.password_change_done_template = "admin/password_change_done.html"
admin.site.password_change_form = PasswordChangeForm  # Django 6.0 NEW

# Display
admin.site.empty_value_display = "-"   # shown for empty/None values
admin.site.enable_nav_sidebar = True   # sidebar on large screens
```

## Django 6.0 Admin Icon Changes (Font Awesome Free 6.7.2)

Django 6.0 includes Font Awesome Free 6.7.2 icon set for admin interface.
The admin UI uses icons for messages, actions, navigation.

**Breaking visual change**: `messages.INFO` and `messages.DEBUG` now have DISTINCT icons
from `messages.SUCCESS`. Before Django 6.0, all three used the same green icon.

## Theming Support

```html
<!-- Override admin/base.html for custom theme -->
{% extends 'admin/base.html' %}
{% block extrastyle %}{{ block.super }}
<style>
html[data-theme="light"], :root {
  --primary: #9774d5;
  --secondary: #785cab;
}
</style>
{% endblock %}
```

## URL Patterns and Reversing

```python
# Hook admin to URLconf
from django.contrib import admin
urlpatterns = [
    path("admin/", admin.site.urls),
]

# Reverse admin URLs
from django.urls import reverse
change_url = reverse("admin:polls_choice_change", args=(choice.id,))
add_url = reverse("admin:polls_choice_add")
list_url = reverse("admin:polls_choice_changelist")
```

## LogEntry (Audit Log)

```python
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

# Query admin actions
recent_changes = LogEntry.objects.filter(
    user=request.user,
).select_related('content_type', 'user')

# Check action type
entry.action_flag == ADDITION  # True if add
entry.action_flag == CHANGE    # True if edit
entry.action_flag == DELETION  # True if delete

# Get the modified object
obj = entry.get_edited_object()

# Get translated change message
message = entry.get_change_message()
```

## Overriding Admin Templates

```
templates/admin/
    <app_label>/
        <model_name>/
            change_form.html     # per-model
        change_list.html         # per-app
    change_form.html             # global override
    login.html
    base_site.html
```

Overridable templates: `actions.html`, `change_form.html`, `change_list.html`,
`delete_confirmation.html`, `object_history.html`, `search_form.html`, `submit_line.html`

## staff_member_required Decorator

```python
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required  # is_staff=True AND is_active=True
def my_admin_view(request): ...
```
