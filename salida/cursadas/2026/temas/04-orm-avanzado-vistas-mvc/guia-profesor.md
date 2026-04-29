# Guía del Profesor — Tema 04
## ORM avanzado + puente a interfaz MVC
**Materia:** Laboratorio de Programación y Lenguajes · IF009 · UNTDF  
**Ciclo lectivo:** 2026 · Semana 8  
**Duración total:** 360 min (180 min teórica + 180 min práctica)  
**Autor:** class-writer (Roberto) · Generado: 2026-04-29

---

> Esta guía es un documento de referencia pedagógica para el docente. Complementa la **minuta.md** (guion slide a slide) con estrategias de enseñanza, errores comunes, rúbricas y configuración de laboratorio.

---

## 1. Resumen ejecutivo de la clase

Esta clase cubre dos módulos del plan mínimo en una sola jornada:

| Módulo | Contenido | Tiempo |
|--------|-----------|--------|
| IV avanzado | QuerySet API avanzado, Q/F, aggregate/annotate, N+1 | T1 + T2 (90 min teórica + P1 práctica) |
| V intro | CBV con View base, ciclo request/response, DTL completo | T3 + T4 (90 min teórica + P2 práctica) |

**Prerequisito crítico validado**: los estudiantes completaron la práctica de ORM básico (orm.pdf) — Biblioteca con Autor, Libro, Lector. El diseño asume este conocimiento.

**Decisión curricular intencional**: Formularios (`ModelForm`, PRG) están en Tema 05. DTL se cubre completo en esta clase para darle el espacio que merece.

---

## 2. Objetivos de aprendizaje y niveles Bloom

| Objetivo | Nivel Bloom | Evaluación |
|----------|-------------|------------|
| Analizar el ciclo de vida de un QuerySet | Analizar (4) | Ejercicio pizarra §T2 |
| Construir queries con Q/F/annotate/aggregate | Aplicar (3) | Shell §P1 |
| Evaluar N+1 e implementar optimizaciones | Evaluar (5) | connection.queries §P1 |
| Extender Managers al dominio BlogApp | Aplicar (3) | Ejercicio 6 §P1 |
| Comprender el ciclo request/response MVT | Comprender (2) | Pregunta clase §T3 |
| Construir templates DTL completos | Aplicar (3) | Mini-ejercicio §T4 + Ticket salida |
| Integrar cadena completa ORM→Vista→Template | Sintetizar (5) | §P2 completa |

---

## 3. Configuración de laboratorio

### 3.1 Requisitos técnicos

- **Codespaces**: el repositorio `blogapp-starter` debe estar disponible para todos los estudiantes.
- **Datos de prueba**: el script `scripts/seed.py` crea posts, categorías y comentarios de prueba.
- **Versión**: Django 6.0, Python 3.12+
- **Verificación previa**: ejecutar `python manage.py check --deploy` y confirmar que `DEBUG = True` está activo en el entorno de desarrollo.

### 3.2 Estructura del proyecto BlogApp esperada

```
blogapp/
  blog/
    models.py       ← Post, Category, Comment (con FKs y M2M)
    views.py        ← vacío al inicio de la práctica
    urls.py         ← con app_name = "blog"
    admin.py        ← modelos registrados (para inspección)
    templates/
      blog/         ← crear en §P2
  blogapp/
    settings.py     ← DEBUG=True, STATICFILES_DIRS configurado
    urls.py         ← include("blog.urls", namespace="blog") ya conectado
  static/
    blog/
      css/          ← crear en Paso 8
```

### 3.3 Datos de prueba esperados

El `seed.py` debe generar:
- 10+ posts (mezcla de publicados y borradores)
- 3+ categorías
- 5+ comentarios distribuidos
- 2+ usuarios con posts

---

## 4. Mapa pedagógico por bloque

### 4.1 §T1 — QuerySet API (45 min): estrategia de enseñanza

**Concepto ancla**: lazy evaluation. Todo lo demás fluye de aquí.

**Secuencia recomendada:**
1. Pregunta abierta: "¿Cuándo creen que Django consulta la base de datos?" — 2 min de debate.
2. Dibujar en pizarra el QuerySet como objeto diferido (la caja con flecha punteada).
3. Los métodos nuevos: presentar como tabla visual, no individualmente.
4. Managers: ligar explícitamente con lo que hicieron en la práctica de Biblioteca — "mismo patrón, nuevo dominio".

**Errores comunes en §T1:**

| Error | Causa | Corrección |
|-------|-------|-----------|
| `qs.filter(...)` después de `list(qs)` no re-evalúa | No entienden que `list()` devuelve una lista Python, no un QuerySet | Mostrar `type(list(qs))` — es `list`, ya no QuerySet |
| Usar `if qs:` cuando solo importa si hay resultados | No conocen `.exists()` | Benchmark visual: `exists()` genera `SELECT 1 LIMIT 1` |
| Olvidar declarar `objects = models.Manager()` al agregar custom manager | No leyeron la doc | Mostrar el error: `Post.objects.all()` → `AttributeError` |
| `get_or_create` sin `defaults` modifica el objeto si ya existe | Confusión con `update_or_create` | Ejemplo con `defaults` vacío vs con `defaults` |

---

### 4.2 §T2 — Consultas dinámicas (45 min): estrategia de enseñanza

**Concepto ancla**: el N+1 como problema real con costo medible.

**Secuencia recomendada:**
1. Arrancar con la pregunta socrática (F-13) — generar la necesidad antes de dar la solución.
2. Q objects: construir el ejemplo dinámico paso a paso en el proyector, mostrando cómo crece el `Q()`.
3. F expressions: usar el escenario del contador de vistas — hace concreto el race condition.
4. aggregate/annotate: la tabla comparativa (F-19) como ancla visual.
5. N+1: esto es el highlight emocional de la clase — el "wow" del costo real.

**Errores comunes en §T2:**

| Error | Causa | Corrección |
|-------|-------|-----------|
| Confundir `aggregate()` con `annotate()` | Nombres similares | "aggregate = una fila global, annotate = campo extra por objeto" |
| `Q()` vacío como filtro real | No saben que `Q()` es el elemento neutro del AND | `Post.objects.filter(Q())` == `Post.objects.all()` — demostrar |
| Usar `F()` en `filter()` directamente | Confusión entre F para operaciones y F para comparaciones | `update(views=F('views')+1)` vs `filter(updated_at__gt=F('created_at'))` |
| N+1 con `prefetch_related` que no resuelve | El campo M2M no está en el `prefetch_related` | Mostrar que `post.comments.all()` en el template requiere `prefetch_related("comments")` |

---

### 4.3 §T3 — CBV con View base (25 min): estrategia de enseñanza

**Concepto ancla**: la View como clase donde cada método HTTP = un método Python.

**Nota crítica**: mantener la coherencia paradigmática del curso — **siempre class-based views, prohibido FBV**. Si algún estudiante propone FBV, explicar por qué el paradigma OOP es el eje del curso.

**Secuencia recomendada:**
1. Dibujar el ciclo MVT en pizarra desde cero — tomar 5 min para esto.
2. Mostrar el código de `PostListView` línea por línea, no como bloque.
3. `as_view()` y `dispatch()`: usar el análogo del recepcionista que deriva llamadas.
4. La pregunta socrática (F-30) como evaluación formativa.

**Errores comunes en §T3:**

| Error | Causa | Corrección |
|-------|-------|-----------|
| Poner lógica de dominio en la View | Confusión MVT | "La View orquesta. La lógica de qué posts son 'populares' va en el Manager o el modelo" |
| Olvidar `as_view()` en `urls.py` | Copiar el nombre de la clase sin llamar `as_view()` | Error: `PostListView is not callable` — claro y diagnóstico fácil |
| `app_name` en el lugar equivocado | Lo ponen en `blogapp/urls.py` en lugar de `blog/urls.py` | El namespace se declara en el `urls.py` de la app que define las rutas |

---

### 4.4 §T4 — DTL completo (45 min): estrategia de enseñanza

**Concepto ancla**: herencia de templates como el DRY aplicado a HTML.

**Secuencia recomendada:**
1. Los 4 constructos: tabla visual, 2 minutos.
2. Variables y filtros: ejemplo en vivo en el proyector con el shell mostrando el contexto.
3. `{% for %}` + forloop: escribir en pizarra el loop con `forloop.first` y `forloop.last`.
4. La trampa de precedencia (F-38): **punto más difícil del bloque** — un ejemplo concreto donde Python y DTL dan resultados distintos.
5. Herencia: construir el `base.html` desde cero en el proyector, luego el primer child template.

**Errores comunes en §T4:**

| Error | Causa | Corrección |
|-------|-------|-----------|
| `{% extends %}` no es la primera línea | Hay un comentario o espacio antes | TemplateSyntaxError muy claro — leer el error |
| `{% load static %}` falta en el child template | Creen que se hereda | Mostrar que `{% load %}` no se hereda — error: `Invalid block tag: 'static'` |
| `{{ block.super }}` usado fuera de un bloque | Confusión con el alcance | Solo tiene sentido dentro de `{% block %}{% endblock %}` |
| `{% include %}` sin `with post=post` | El partial no recibe el contexto | Error: `{{ post.title }}` renders como vacío, no como error — difícil de debugear |
| Precedencia `and`/`or` en `{% if %}` | Diferencia con Python no explicada | La regla: si necesitás `(a or b) and c`, anidar dos `{% if %}` |

---

## 5. Evaluaciones formativas — detalles

### §T2 — Ejercicio pizarra (min 75): N+1 anidado

**Código a mostrar:**
```python
posts = Post.objects.filter(published=True)
for post in posts:
    print(post.author.username)
    for comment in post.comments.all():
        print(comment.user.username)
```

**Respuesta esperada:**
- 1 query (posts) + N (author por post) + N (comments por post) + N*M (user por comment)
- Con 50 posts, 3 comments por post: 1 + 50 + 50 + 150 = 251 queries

**Corrección:**
```python
posts = Post.objects.select_related("author")\
                    .prefetch_related("comments__user")\
                    .filter(published=True)
```

**Tiempo sugerido**: 5 min. Dar 2 min para que calculen individualmente, luego resolver en pizarra.

---

### §T3 — Pregunta clase (min 120): PUT sin método put()

**Pregunta**: "Si una CBV tiene solo `def get()`, ¿qué devuelve Django ante un PUT?"

**Respuesta esperada**: `405 Method Not Allowed` — `dispatch()` busca el método `put()`, no lo encuentra, devuelve 405.

**Profundización opcional**: ¿Y ante un HEAD? Django maneja HEAD automáticamente — llama `get()` pero no incluye el body en la respuesta.

---

### §T4 — Mini-ejercicio (min 165): template de memoria

**Consigna:**
> Escribí en papel: un template que extiende `base.html`, cambia el `{% block title %}`, usa `{% for %}` con `forloop.counter`, destaca el primer elemento con `{% if forloop.first %}`, y tiene `{% empty %}` para el caso vacío.

**Rubrica:**
| Criterio | Puntaje |
|----------|---------|
| `{% extends %}` como primera línea | 1 |
| `{% block title %}...{% endblock %}` | 1 |
| `{% for %}...{% empty %}...{% endfor %}` | 1 |
| `forloop.counter` dentro del for | 1 |
| `{% if forloop.first %}` dentro del for | 1 |
| **Total** | **5** |

---

### Ticket de salida (min 355 — práctica): 3 tags DTL

**Criterio de aprobación**: los 3 tags deben ser diferentes, con explicación correcta de lo que hacen.

**Respuestas válidas** (ejemplos):
- `{% for %}` → itera sobre una lista o QuerySet
- `{% if %}` → muestra contenido condicionalmente
- `{% extends %}` → hereda la estructura de un template base
- `{% block %}` → define una zona sobreescribible en la herencia
- `{% include %}` → inserta un fragmento de template
- `{% with %}` → crea un alias para evitar lookups repetidos
- `{% url %}` → resuelve una URL por nombre sin hardcodear
- `{% static %}` → genera la URL de un archivo estático
- `{% load %}` → carga una librería de tags
- `{% comment %}` → bloque de comentario no renderizado

---

## 6. Gestión del tiempo — alertas

| Punto crítico | Tiempo máximo | Si se excede... |
|---------------|---------------|-----------------|
| §T1 completo | 45 min (min 10–55) | Comprimir F-09/F-10 a mención oral |
| §T2 completo | 45 min (min 55–100) | Comprimir el ejercicio pizarra a 3 min |
| §T3 completo | 25 min (min 100–125) | Mostrar solo PostListView, omitir PostDetailView |
| §T4 herencia | 15 min (min 145–160) | El mini-ejercicio puede hacerse en casa |
| §P1 completa | 60 min (min 10–70) | Comprimir Ej 1 y 2 a demostración del docente |
| §P2 pasos 7-9 | Últimos 30 min | Partial y static pueden ser homework |

**Regla de corte**: si llegan al break de §P2 (min 75 de práctica) con retraso, priorizar los Pasos 1–4 (View + URLs + base.html + templates hijos) sobre los Pasos 5–9 (with, forloop, partial, static).

---

## 7. Instrucciones para la demostración en vivo (§P2)

El §P2 es fundamentalmente una demostración guiada donde **el docente construye en vivo y los estudiantes replican en paralelo**.

**Ritmo recomendado:**
1. Docente escribe el código en el proyector (2–3 min).
2. Estudiantes replican en Codespace (5 min).
3. Todos verifican en el navegador (2 min).
4. El docente pregunta "¿alguien vio algo distinto?" (1 min).
5. Avanzar.

**Verificaciones críticas en §P2:**

| Paso | Verificación |
|------|-------------|
| Paso 1+2+3 | `runserver` → navegar a `/blog/` → `TemplateDoesNotExist` es esperado |
| Paso 4 | `runserver` → `/blog/` → listado con navbar — herencia funciona |
| Paso 4 | `/blog/1/` → detalle con misma navbar — herencia funciona en otro template |
| Paso 5 | `{% with %}` → misma visual, diferente código — explicar la diferencia |
| Paso 8 | `Ctrl+U` → CSS aplicado, sin comentarios DTL en el HTML |

---

## 8. Diferenciación instruccional

### Estudiantes que van adelante

Si termina §P2 antes que el resto, proponer extensiones:

1. **Agregar `CategoryListView`**: vista que lista todas las categorías con su conteo de posts (`annotate`).
2. **Sidebar de categorías**: partial con la lista de categorías inyectado en `base.html` via context processor (investigar).
3. **Filtrado por categoría**: `PostListView` que acepta `?cat=python` como parámetro GET.

### Estudiantes con dificultades

Si algún estudiante no puede completar la cadena completa (View → Template):

1. Asegurar que tiene los Pasos 1–3 funcionando (View + URLs + `runserver` sin crash).
2. Darle el `base.html` pre-construido y que replique solo `post_list.html`.
3. El Partial (Paso 7) y Static (Paso 8) pueden ser tarea complementaria.

---

## 9. Conexiones con otros temas

| Tema anterior | Conexión | Cómo mencionar |
|---------------|----------|----------------|
| Tema 03 (ORM básico) | Lazy evaluation, `filter()`, Managers | "Hoy profundizamos lo que ya saben — no empezamos de cero" |
| Práctica Biblioteca | Managers, CRUD shell | "El Manager de Libro.disponibles → ahora Post.published" |

| Tema siguiente | Conexión | Cómo anticipar |
|----------------|----------|----------------|
| Semana 9 (Tema 05) | `ListView`/`DetailView`, `ModelForm` | "Refactorizamos la View de hoy a genérica — van a ver qué automatizan" |
| Parcial 1 | Todo el ORM + CBV básico | "El parcial es al inicio de Semana 9 — esta clase es el contenido más importante para prepararlos" |

---

## 10. Checklist de preparación para el docente

### Antes de la clase teórica

- [ ] Codespace de presentación abierto con BlogApp y datos de prueba
- [ ] Shell pre-ejecutado para demostración rápida si es necesario
- [ ] Pizarra/whiteboard disponible para dibujar diagrama MVT
- [ ] `settings.DEBUG = True` verificado en el entorno de demo

### Antes de la clase práctica

- [ ] Repositorio BlogApp accesible para todos los estudiantes en Codespaces
- [ ] `python manage.py migrate` y `python manage.py seed` (o fixture equivalente) ejecutados
- [ ] Verificar que `Post.objects.count() > 0` en el shell de un Codespace de estudiante
- [ ] `STATICFILES_DIRS` configurado en `settings.py` del template del proyecto

### Al inicio de la práctica

- [ ] Circular por el aula para verificar que todos tienen el Codespace abierto
- [ ] 5 min de buffer para problemas de setup antes de arrancar §P1

---

## 11. TP-5 — Vista previa de la consigna

El TP-5 cubrirá exactamente el contenido de esta clase. La consigna orientativa incluye:

1. **Modelos** (consolidación): agregar campo `views` (IntegerField, default=0) a `Post`.
2. **ORM avanzado**: implementar `PublishedManager.recientes()` con `only()` y `select_related()`.
3. **CBV**: implementar `PostListView`, `PostDetailView` y `CategoryDetailView` con `View` base.
4. **DTL completo**: `base.html` + templates hijos con herencia, `{% with %}`, `{% static %}`, partials.
5. **Opcional +**: `PostSearchView` con Q objects para búsqueda por título y categoría.

**Fecha de publicación**: esta semana. **Entrega**: antes del inicio de Semana 10.
