# Django 6.0 Release Notes
**Released:** December 3, 2025
**Documentation version:** 6.0
**Source:** https://docs.djangoproject.com/en/6.0/releases/6.0/

## Python Compatibility

Django 6.0 supports **Python 3.12, 3.13, and 3.14** only.
The Django 5.2.x series is the last to support Python 3.10 and 3.11.
**Minimum Python for Django 6.0: Python 3.12**.

## What's New in Django 6.0

### Content Security Policy (CSP) Support — MAJOR NEW FEATURE
Built-in support for the Content Security Policy standard. Protects against XSS attacks.
- `ContentSecurityPolicyMiddleware` adds CSP headers
- Nonces via `csp()` context processor
- Configured using `SECURE_CSP` and `SECURE_CSP_REPORT_ONLY` settings (Python dicts)
- `django.utils.csp.CSP` provides constants (CSP.SELF, CSP.NONCE, etc.)
- Per-view decorators to override or disable CSP policies

```python
from django.utils.csp import CSP
SECURE_CSP = {
    "default-src": [CSP.SELF],
    "script-src": [CSP.SELF, CSP.NONCE],
    "img-src": [CSP.SELF, "https:"],
}
```

### Template Partials — NEW
Django Template Language now supports template partials with `{% partialdef %}` and `{% partial %}` tags.
- Encapsulate and reuse small named fragments within a template file
- Reference: `template_name#partial_name` syntax with `get_template()`, `render()`, `{% include %}`
- Migration guide available from `django-template-partials` third-party package

### Background Tasks Framework — NEW
Built-in Tasks framework for running code outside the HTTP request-response cycle.
- `@task` decorator for defining tasks
- `task.enqueue()` to queue tasks
- Configured via `TASKS` setting with two built-in backends (dev/testing focused)
- Django handles task creation/queuing; execution managed externally

```python
from django.tasks import task

@task
def send_notification(user_id, message):
    # runs outside HTTP cycle
    pass

send_notification.enqueue(user_id=42, message="Hello")
```

### Modern Python Email API Adoption
Email handling now uses Python's modern email API (`email.message.EmailMessage`).
- Replaces legacy Compat32 API
- `EmailMessage.message()` returns `email.message.EmailMessage` instance
- `SafeMIMEText` and `SafeMIMEMultipart` deprecated

## Minor Features — django.contrib.auth

- **PBKDF2 password hasher**: iteration count increased from 1,000,000 to **1,200,000** (security hardening)
- No breaking changes to `User` model, `authenticate()`, `login()`, `logout()`
- Async API stable: `aauthenticate()`, `alogin()`, `alogout()`, `aupdate_session_auth_hash()`

## Minor Features — django.contrib.admin

- **Font Awesome Free icon set (version 6.7.2)** now used for admin interface icons (visual change)
- **`AdminSite.password_change_form`** — NEW attribute: customizes the form used in admin password change view (subclass of `PasswordChangeForm`)
- **`messages.DEBUG` and `messages.INFO`** now have distinct icons and CSS styling (previously both shared `messages.SUCCESS` appearance)
  - **IMPORTANT**: `ModelAdmin.message_user()` uses `messages.INFO` by default — set to `messages.SUCCESS` to keep old icon/style

## Minor Features — Templates

- `forloop.length` variable now available within `{% for %}` loops
- `{% querystring %}` tag now consistently prefixes with `?`
- `{% querystring %}` accepts multiple positional mapping arguments

## Minor Features — Models

- `DEFAULT_AUTO_FIELD` now defaults to `BigAutoField` (was `AutoField`)
- `Model.save()` raises specialized `Model.NotUpdated` exception on failed forced update
- `GeneratedField` and expression-assigned fields refreshed after `save()` on backends supporting RETURNING clause
- `StringAgg` aggregate now available on all backends (not PostgreSQL-only)
- `AnyValue` aggregate on SQLite, MySQL, Oracle, PostgreSQL 16+

## Minor Features — Management Commands

- `startproject` and `startapp` create custom target directory if it doesn't exist
- Common utilities like `django.conf.settings` auto-imported in `shell`

## Minor Features — Migrations

- Squashed migrations can themselves be squashed before transitioning to normal migrations
- Migrations support serialization of `zoneinfo.ZoneInfo` instances

## Minor Features — Pagination

- `AsyncPaginator` and `AsyncPage` for async pagination

## Backwards Incompatible Changes in 6.0

### Dropped Support
- **Python < 3.12** dropped (3.12 is minimum)
- **MariaDB 10.5** dropped (10.6+ required)

### DEFAULT_AUTO_FIELD Changes to BigAutoField
In Django 6.0, `DEFAULT_AUTO_FIELD` now defaults to `django.db.models.BigAutoField`.
The explicit lines in project and app templates are removed.
If needed, add to settings: `DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'`

### Email API Breaking Changes
- `mixed_subtype` and `alternative_subtype` properties removed from `EmailMessage`/`EmailMultiAlternatives`
- `django.core.mail.BadHeaderError` deprecated (use Python's `ValueError`)
- `SafeMIMEText` and `SafeMIMEMultipart` deprecated

## Features Removed in 6.0 (from 5.0/5.1 deprecations)

- **`ModelAdmin.log_deletion()` and `LogEntryManager.log_action()` REMOVED** — use `LogEntry` directly
- `request` is **required** in signature of `ModelAdmin.lookup_allowed()` subclasses
- `DjangoDivFormRenderer` and `Jinja2DivFormRenderer` removed
- `format_html()` without args/kwargs removed
- `forms.URLField` default scheme changed from `"http"` to `"https"`
- `cx_Oracle` support removed
- `django.urls.register_converter()` no longer allows overriding existing converters

## Features Deprecated in 6.0

- `django.core.mail` APIs: most optional parameters must now use keyword arguments
- PostgreSQL `StringAgg` deprecated in favor of generally available `StringAgg`
- `ADMINS`/`MANAGERS` as list of (name, address) tuples deprecated (use email strings)
- `URLIZE_ASSUME_HTTPS` transitional setting deprecated
- Support for Python legacy `MIMEBase` in `EmailMessage.attach()` deprecated
