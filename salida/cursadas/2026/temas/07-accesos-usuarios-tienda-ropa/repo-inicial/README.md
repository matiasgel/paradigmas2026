# Tienda v0.1 — Repositorio inicial docente

Base preparada para el tutorial guiado continuable por checkpoints.

## Qué incluye

- Django 5.2.15.
- Jazzmin 3.0.4 configurado sobre Django Admin.
- pytest + pytest-django.
- GitHub Actions para ejecutar check y tests en cada push.
- ThemeWagon MiniStore copiado en `static/store/`.
- Template base y portada inicial servidos por Django.
- Configuración de `templates/`, `static/` y `media/`.

## Qué no incluye intencionalmente

- Apps `accounts` y `products`.
- Usuario personalizado.
- Modelos de productos o variantes.
- Permisos del operador.
- Catálogo dinámico.

Esas partes se implementan durante la clase.

No se asignan tiempos a las etapas. Al terminar cada sesión se conserva el último
checkpoint consistente, con sus verificaciones en verde, y se continúa desde allí.

## Puesta en marcha

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py check
pytest -q
python manage.py runserver
```

Abrir:

- Storefront inicial: `http://127.0.0.1:8000/`
- Admin Jazzmin: `http://127.0.0.1:8000/admin/`

No ejecutar `migrate` antes de crear `accounts.User` y configurar `AUTH_USER_MODEL`
durante la clase.

## Archivos de referencia

- `ministore-original.html`: HTML original para comparar y adaptar.
- `static/store/`: assets originales de MiniStore.
- `MINISTORE-LICENSE-NOTICE.md`: autoría y licencia del theme.
- `CHECKPOINTS-DOCENTE.md`: puntos de recuperación de la demostración.
