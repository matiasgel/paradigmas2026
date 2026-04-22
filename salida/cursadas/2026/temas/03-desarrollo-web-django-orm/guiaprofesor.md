# Guía del Profesor — Tema 03: Desarrollo Web con Django
## Cheatsheet docente condensado · UNTDF 2026

> Documento de bolsillo para el profesor. Sin ceremonia. Todo lo "para qué" va en `diseno.md`; todo el "guion paso a paso" en `minuta.md`; toda la profundidad en `guia-estudio.md`. **Acá va solo lo que el docente necesita a mano mientras da la clase.**

---

## 1. Panorama del tema

| Dato | Valor |
|------|-------|
| Tema | 03 — Desarrollo Web + Django + ORM |
| Módulos plan | III completo + IV parcial |
| Duración | 3 × 180 min = 9 h |
| Filminas | 74 (clases 22 / 22 / 30) |
| Paradigma | **POO estricto**: CBV siempre, nunca FBV |
| TP asociado | TP-4 Django ORM (autograder GitHub Actions) |

## 2. Mensajes clave que el docente debe repetir

1. "En esta cátedra **todas las vistas son clases**. Nunca funciones."
2. "MVT es MVC: Template = View, View = Controller."
3. "`null` es BD, `blank` es formulario."
4. "`PROTECT` protege padres; `CASCADE` arrastra hijos."
5. "QuerySet es **lazy** — no ejecuta SQL hasta que lo usás."
6. "Si resolvés con `for libro in ... if ...` en lugar de ORM → **N+1 queries** → rojo."

## 3. Tiempos por clase (resumen)

| Clase | Bloque crítico | Tiempo mínimo |
|-------|----------------|---------------|
| 1 | T3 Patrón MVC + ejercicio clasificación | 50 min |
| 2 | T5 Primera CBV hands-on | 30 min |
| 3 | T6 Las 4 queries del TP-4 | 25 min |

> Si el tiempo aprieta, sacrificá apertura/recap antes que los bloques críticos.

## 4. Ejercicios en clase — respuestas rápidas

### Clase 1 — F-07 E-commerce
| Cosa | Capa |
|------|------|
| Carrito | Negocio |
| HTML del checkout | Presentación |
| Tabla `pedido` | Datos |
| Regla "stock ≥ 1" | Negocio |
| CSS | Presentación |
| Gateway de pago | Negocio (integración) |

### Clase 1 — F-11 Biblioteca MVC
| # | Item | M/V/C |
|---|------|-------|
| 1 | Tabla `libros` | M |
| 2 | HTML lista | V |
| 3 | Función que atiende `/libros/` | **C** |
| 4 | `libro.tiene_disponibles()` | M |
| 5 | CSS | V |
| 6 | Invariante "no reservar si 0" | M |
| 7 | SELECT de libros por categoría | M |

### Clase 2 — F-36 HolaView con nombre
```python
# urls.py
path("hola/<str:nombre>/", HolaMundoView.as_view(), name="hola"),
```
```python
# views.py
ctx["mensaje"] = f"Hola {self.kwargs['nombre']} — 3° año UNTDF"
```

### Clase 3 — F-62 Variantes queries
```python
# V1: con orden
Libro.objects.filter(categorias__nombre=n).order_by("-fecha_publicacion")

# V2: menos de n
Autor.objects.annotate(x=Count("libros")).filter(x__lt=n)

# V3: al menos una disponible
Libro.objects.annotate(
    activos=Count("prestamos", filter=Q(prestamos__fecha_devolucion__isnull=True))
).filter(activos__lt=F("cantidad_total"))

# V4: top N prestatarios
Prestamo.objects.values("nombre_prestatario").annotate(n=Count("id")).order_by("-n")[:n]
```

## 5. Errores típicos del alumno (y cómo responder)

| Síntoma | Diagnóstico rápido | Respuesta docente |
|---------|-------------------|-------------------|
| `TemplateDoesNotExist: catalogo/hola.html` | Falta `templates/catalogo/`  o falta app en INSTALLED_APPS | "Revisá ruta y settings.py" |
| `FieldError: cannot resolve keyword 'prestamo'` | Usó `prestamo` en vez de `prestamos` | "Usaste related_name mal" |
| `IntegrityError UNIQUE` en tests | Email/isbn duplicado | "Cambiá el email de los fixtures" |
| Autograder rojo, local verde | Migraciones sin commit | "`git add migrations/`" |
| Query lenta (>2 s) | N+1 | "Usá annotate en vez del for" |
| `OperationalError no such table` | Falta migrate | "`python manage.py migrate`" |

## 6. Preguntas frecuentes del alumno

**P: ¿Puedo usar `@login_required`?**
R: **No**. `LoginRequiredMixin` en CBV.

**P: ¿Por qué no usamos FastAPI?**
R: Maduración + ORM integrado + objetivo pedagógico POO. FastAPI se ve al cierre del año.

**P: ¿`annotate` y `aggregate` son lo mismo?**
R: No. `annotate` agrega una columna por fila; `aggregate` colapsa a un valor único.

**P: ¿Puedo poner todo el código en `views.py`?**
R: Para el TP-4 no importa (no hay vistas). Pero **reglas de dominio van en métodos del modelo**, no en la vista.

## 7. Checklist docente post-clase

- [ ] Subí el ticket de salida escaneado al repo docente
- [ ] Anoté en `_edu-memory/material/` qué alumnos quedaron atrás
- [ ] Actualicé `.pipeline-state.json` del tema
- [ ] Consulté `_edu-memory/memory.db` por errores nuevos para registrar

## 8. Referencias rápidas

- `diseno.md` — por qué de cada bloque (consultarlo si alguien pregunta "por qué enseñamos esto")
- `minuta.md` — cronograma + resoluciones de ejercicios
- `guia-estudio.md` — mandar al alumno que falta o que pide más
- `filminas.md` → `slides/plan-filminas-*.json` → Google Slides publicadas
- `tp-repo/` — clon del TP-4 con models/queries stub (usar para mostrar en clase)

---

**Fin.** — 22/04/2026.