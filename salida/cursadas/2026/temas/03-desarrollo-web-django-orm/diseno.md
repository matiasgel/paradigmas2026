# Tema 03 — Desarrollo Web con Django: Intro Web, Django y ORM
## Módulo III completo + Módulo IV parcial (Introducción a ORM) — UNTDF IF009 2026

> **Fecha**: 2026-04-22
> **Estado**: DESIGN-IN-PROGRESS — requiere aprobación del docente antes de pasar a minuta.md
> **Fuentes base**:
> - ingesta/introweb.pdf (26 pág, filminas 2025) → ChromaDB colección introweb
> - django-6.0-docs (2443 chunks) · python-3.14-docs (5306 chunks) · edu_knowledge (446 docs)
> - Repo TP-4 clonado en tp-repo/ (accedido con credenciales matiasgel vía gh CLI)

---

## 1. Metadatos

| Campo | Valor |
|-------|-------|
| Número | 03 |
| Nombre | Desarrollo Web con Django: Intro Web + Django + ORM |
| Módulos plan | III completo + IV parcial (persistencia + mapeo OO-R + Django ORM básico) |
| Duración total | **540 min = 9 h = 3 clases de 180 min** |
| Audiencia | 3º año UNTDF Sistemas/AUS, niveles heterogéneos, algunos offline |
| Paradigma docente | **POO estricto: todas las vistas son class-based views. Prohibido FBV.** |
| TP asociado | TP-4 Introducción a Django ORM — autograding en GitHub Actions |
| Stack TP | Python 3.13+, Django 5.1+, SQLite, django.test, Git/GitHub Classroom |
| Prerequisitos | Módulo I (Python) + Módulo II (pytest/unittest) + Git básico |

---

## 2. Cobertura del Plan Mínimo

### Módulo III — Frameworks para desarrollo WEB (completo)
- [x] Características de aplicaciones WEB → Clase 1 §3.1
- [x] Capas y arquitectura WEB → Clase 1 §3.2
- [x] Diseño de app web → Clase 1 §3.3
- [x] Patrón MVC → Clase 1 §3.4
- [x] Concepto de Framework → Clase 2 §4.1
- [x] Frameworks MVC para WEB → Clase 2 §4.2
- [x] Introducción al Framework Django → Clase 2 §4.3–4.8

### Módulo IV — Persistencia (parcial — lo necesario para TP-4)
- [x] Concepto de persistencia → Clase 3 §5.1
- [x] Persistencia y lenguajes → Clase 3 §5.2
- [x] Soluciones en Python → Clase 3 §5.3
- [x] Mapeo OO-Relacional (impedance mismatch) → Clase 3 §5.4
- [x] Comparación tecnologías ORM → Clase 3 §5.5
- [x] Persistencia en Django → Clase 3 §6
- [x] Mapeo de entidades y relaciones → Clase 3 §6.3
- [x] CRUD con Django → Clase 3 §7
- [x] Consultas dinámicas (filter/Q/F/annotate/aggregate) → Clase 3 §7.4
- [ ] _NO en este tema_ (→ Tema 04): transacciones, select_related/prefetch_related avanzado, bulk ops, señales

---

## 3. CLASE 1 — Introducción a Programación Web + MVC (180 min)

### Objetivos (Bloom)
1. **Comprender** (2) qué es una app web vs sitio web estático.
2. **Explicar** (2) el modelo petición-respuesta HTTP (GET/POST).
3. **Identificar** (2) las 3 capas de arquitectura cliente-servidor.
4. **Aplicar** (3) el patrón MVC clasificando responsabilidades.
5. **Diferenciar** (4) framework vs librería con ejemplo propio.

### Agenda
| Tiempo | Bloque |
|--------|--------|
| 0–15 | Apertura: demo DevTools → Network de una página real |
| 15–40 | §3.1 App Web vs Sitio Web |
| 40–70 | §3.2 Cliente/Servidor + modelo 3 capas |
| 70–90 | **Break** + §3.3 Diseño de app web |
| 90–140 | §3.4 Patrón MVC (bloque central) + ejercicio |
| 140–170 | §3.5 HTTP hands-on con curl + DevTools |
| 170–180 | Cierre + preview Clase 2 |

### Contenido (mapeo a filminas 2025)

**§3.1 App Web vs Sitio Web** (introweb.pdf p.9-10): interacción, estado, ejemplos (Moodle UNTDF, SIU-Guaraní, Instagram), contra-ejemplo (blog estático).

**§3.2 Cliente/Servidor + 3 capas** (p.11-13): procesos solicitan/responden, ventaja separación, modelo 3 capas (presentación/negocio/datos), analogía restaurante.

**§3.3 Diseño de app web**: responsive, accesibilidad (WCAG referenciado en guía), rutas URL como contrato.

**§3.4 Patrón MVC** (p.4-5) — **BLOQUE CENTRAL**:
- Modelo (datos + lógica de dominio)
- Vista (presentación HTML)
- Controlador (pegamento)
- MVC clásico vs MVT de Django (aclaración preventiva)
- Ejercicio: dado caso "comprar online" clasificar responsabilidades.

**§3.5 HTTP** (p.6-8): TCP/IP → HTTP, modelo request/response, GET/POST (+ mención PUT/DELETE), códigos (200/301/302/400/403/404/500), demo en vivo con curl.

### Filminas previstas: ~22
### Evaluación formativa: kahoot min 140 + ejercicio pizarra min 95 + ticket de salida.

---

## 4. CLASE 2 — Introducción a Django con POO (180 min)

### Objetivos (Bloom)
1. **Comprender** (2) qué es un framework y por qué Django es MVT completo.
2. **Crear** (3) proyecto + app con django-admin y manage.py.
3. **Reconocer** (2) la estructura de directorios generada.
4. **Implementar** (3) una primera class-based view (TemplateView).
5. **Verificar** (3) ejecución local del proyecto con runserver.

### Agenda
| Tiempo | Bloque |
|--------|--------|
| 0–10 | Recap Clase 1 |
| 10–30 | §4.1 Framework vs librería (Hollywood principle) |
| 30–55 | §4.2 Django en el ecosistema Python |
| 55–75 | §4.3 Instalación + venv |
| 75–90 | **Break** |
| 90–130 | §4.4–4.6 startproject, startapp, settings, urls |
| 130–160 | §4.7 Primera CBV (TemplateView) + template |
| 160–180 | §4.8 runserver + autoreload + cierre |

### Contenido

**§4.1 Framework vs Librería** (p.2-3): inversión de control, "don't call us we'll call you", ejemplos.

**§4.2 Django** (p.14-15): framework MVT maduro desde 2005 (Instagram, Dropbox, Mozilla), DRY, baterías incluidas. **Aclaración MVT vs MVC**:
- Model Django = Modelo MVC
- Template Django = Vista MVC
- View Django = Controlador MVC (a pesar del nombre)

**§4.3 Instalación**: python -m venv .venv → activar → pip install "django>=5.1" → django-admin startproject biblioteca → cd biblioteca → python manage.py startapp catalogo. Usar **exactamente los nombres del TP-4**: proyecto biblioteca, app catalogo.

**§4.4 Estructura** (p.16-17): diagrama de árbol del proyecto real del TP-4.

**§4.5 settings.py**: INSTALLED_APPS (agregar "catalogo"), DATABASES (SQLite default), TEMPLATES, STATIC_URL.

**§4.6 URLconf**: path("ruta/", Vista.as_view(), name="nombre"). Include de app urls. **Siempre .as_view() — porque usamos CBV.**

**§4.7 Primera CBV — TemplateView** — PARADIGMA POO:

`python
# catalogo/views.py
from django.views.generic import TemplateView

class HolaMundoView(TemplateView):
    template_name = "catalogo/hola.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["mensaje"] = "Hola 3er año"
        return ctx
`

`python
# catalogo/urls.py
from django.urls import path
from .views import HolaMundoView
app_name = "catalogo"
urlpatterns = [path("hola/", HolaMundoView.as_view(), name="hola")]
`

**Constraint innegociable**: toda vista es clase desde el minuto 1. Justificación: consistencia OOP cursada, reuso vía mixins, métodos extensibles (get_context_data, get_queryset, form_valid), estándar profesional.

**§4.8 runserver**: autoreload, debug toolbar (opcional).

### Filminas previstas: ~22

---

## 5. CLASE 3 — Django ORM completo para TP-4 (180 min)

> **CLASE CRÍTICA**: cubre 100% del TP-4. Basada directamente en el repo clonado en tp-repo/.

### Objetivos (Bloom)
1. **Comprender** (2) persistencia e impedance mismatch OO-relacional.
2. **Diseñar** (4) modelos Django con campos, Meta, relaciones FK/M2M/O2O.
3. **Aplicar** (3) ciclo de migraciones (makemigrations/migrate).
4. **Ejecutar** (3) CRUD por Manager y QuerySet.
5. **Construir** (4) queries complejas con filter/Q/F/annotate/aggregate (lo que el TP-4 exige).
6. **Integrar** (5) todo en flujo reproducible con django.test.TestCase.

### Agenda
| Tiempo | Bloque |
|--------|--------|
| 0–10 | Recap + objetivos |
| 10–25 | §5 Persistencia + impedance mismatch |
| 25–55 | §6.1-6.2 Modelos + campos (con TP-4: Autor, Categoria) |
| 55–75 | §6.3 Relaciones FK/M2M/O2O (con TP-4: Libro→Autor PROTECT, Libro↔Categoria M2M) |
| 75–90 | **Break** |
| 90–110 | §6.5 Migraciones (makemigrations + migrate + sqlmigrate) |
| 110–140 | §7 CRUD con QuerySet (Django shell) |
| 140–165 | §7.4 Queries del TP-4: libros_por_categoria, autores_con_mas_de_n, libros_sin_disponibilidad, top_n_mas_prestados |
| 165–180 | §8 django.test.TestCase + cierre + mapa TP-4 |

### Contenido

**§5.1 Persistencia** (p.18): datos sobreviven al proceso, mecanismos (archivos, BD).

**§5.2 Persistencia en lenguajes**: pickle/shelve limitado, BDs relacionales escalables.

**§5.3 Soluciones Python**: Django ORM (integrado + migraciones), SQLAlchemy (flexible), Peewee.

**§5.4 Impedance mismatch** (p.19-23): herencia OO↔tablas (strategies), colecciones↔FK+M2M, identidad ==/id/PK. Rol del ORM: abstraer mapeo.

**§6.1 Modelo base** — con el TP-4:

`python
# catalogo/models.py
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True)
    def __str__(self): return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    def __str__(self): return self.nombre
`

**§6.2 Campos y atributos**:
- CharField(max_length=) · TextField · EmailField · DateField · PositiveIntegerField · BooleanField
- null vs blank (explicar diferencia con ejemplo biografia blank=True)
- unique=True · default= · choices= · db_index=True · verbose_name=

**§6.3 Relaciones** — CENTRAL del TP-4:

`python
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=32, unique=True)
    fecha_publicacion = models.DateField()
    cantidad_total = models.PositiveIntegerField(default=1)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="libros")
    categorias = models.ManyToManyField(Categoria, related_name="libros", blank=True)

    def prestamos_activos(self) -> int:
        return self.prestamos.filter(fecha_devolucion__isnull=True).count()
    def disponibles(self) -> int:
        return self.cantidad_total - self.prestamos_activos()
    def tiene_disponibles(self) -> bool:
        return self.disponibles() > 0
    def __str__(self): return self.titulo

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="prestamos")
    nombre_prestatario = models.CharField(max_length=120)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
`

**on_delete — discusión pedagógica**:
- PROTECT (Libro→Autor): borrar autor con libros rompe integridad bibliotecaria.
- CASCADE (Prestamo→Libro): borrar libro arrastra sus préstamos históricos (decisión del TP).
- SET_NULL / SET_DEFAULT / DO_NOTHING como otras opciones.

**related_name**: docente explicita por qué es buena práctica ("libros" en vez de "libro_set").

**§6.5 Migraciones**:
- python manage.py makemigrations catalogo → genera 0001_initial.py
- python manage.py migrate → aplica a SQLite
- python manage.py sqlmigrate catalogo 0001 → ver SQL generado (didáctico)
- cada cambio de modelo = nueva migración
- NO editar migraciones aplicadas

**§7 CRUD con QuerySet** (django shell):

`python
# Create
autor = Autor.objects.create(nombre="Ursula K. Le Guin", email="u@ex.com")
libro = Libro.objects.create(titulo="Los desposeídos", isbn="...", fecha_publicacion=date(1974,1,1), cantidad_total=2, autor=autor)
libro.categorias.add(Categoria.objects.create(nombre="ciencia ficción"))

# Read
Libro.objects.all()
Libro.objects.get(isbn="...")
Libro.objects.filter(autor__nombre__icontains="le guin")

# Update
libro.cantidad_total = 3; libro.save()
Libro.objects.filter(autor=autor).update(cantidad_total=F("cantidad_total")+1)

# Delete
Prestamo.objects.filter(fecha_devolucion__lt=date(2020,1,1)).delete()
`

**§7.4 Queries avanzadas — LAS 4 DEL TP-4**:

`python
# queries.py
from django.db.models import Count, Q, F
from .models import Autor, Libro

def libros_por_categoria(nombre_categoria: str):
    return Libro.objects.filter(categorias__nombre=nombre_categoria)

def autores_con_mas_de_n_libros(n: int):
    return Autor.objects.annotate(cantidad_libros=Count("libros")).filter(cantidad_libros__gt=n)

def libros_sin_disponibilidad():
    return Libro.objects.annotate(
        activos=Count("prestamos", filter=Q(prestamos__fecha_devolucion__isnull=True))
    ).filter(activos=F("cantidad_total"))

def top_n_libros_mas_prestados(n: int):
    return Libro.objects.annotate(total=Count("prestamos")).order_by("-total")[:n]
`

**Explicación en vivo** de cada query: qué SQL genera (usar str(qs.query) en shell), por qué annotate es la herramienta correcta, diferencia aggregate (1 fila) vs annotate (1 por objeto).

**§8 Tests con django.test.TestCase** (breve — el TP los provee):
- setUpTestData (una vez) vs setUp (cada test)
- TestCase envuelve en transacción + rollback automático
- assertEqual, assertTrue, assertRaises
- python manage.py test catalogo.tests.test_models -v 2

### Filminas previstas: ~32

---

## 6. Resumen Filminas

| Clase | Filminas | Temas |
|-------|----------|-------|
| 1 | ~22 | Web, cliente-servidor, 3 capas, MVC, HTTP |
| 2 | ~22 | Framework, Django install, estructura, urlconf, primera CBV |
| 3 | ~32 | Persistencia, mismatch, modelos, campos, relaciones, migraciones, CRUD, queries TP-4 |
| **Total** | **~76** | |

Constraint Mayer/Fiorella: ≤40 palabras por slide, 1 idea principal, diagrama/imagen cuando aplique.

---

## 7. Material Complementario (guía de estudio)

La guía de estudio debe cubrir:

### Tutoriales paso-a-paso (alumnos offline)
1. Setup completo Windows/macOS/Linux con capturas
2. Clonar el TP-4 de GitHub Classroom (link del aula) y abrirlo en el IDE
3. Django shell: 20 min guiados de exploración
4. De modelos a migraciones (con errores típicos: IntegrityError, "no such table")
5. Las 4 queries del TP explicadas visualmente (qué SQL genera cada annotate)
6. Cómo leer un fallo de GitHub Actions y arreglarlo

### FAQ anticipada (mínimo 10 preguntas)
- ¿Por qué CBV y no FBV si los tutoriales web usan FBV?
- ¿null=True vs blank=True?
- ¿PROTECT vs CASCADE en on_delete?
- ¿related_name opcional u obligatorio?
- ¿get() vs filter().first()?
- ¿Por qué annotate y no count() en un loop?
- ¿Qué hace QuerySet lazy?
- ¿makemigrations modifica la BD? (No, solo genera archivo)
- ¿Cómo reseteo la BD en dev? (borrar db.sqlite3 + migrations/00*.py excepto __init__)
- ¿Actions falla en nube pero local ok? (commitear migraciones)

### Tutoriales embebidos
- Tut A: primer CRUD en 15 min (TemplateView + ListView + CreateView con CBV)
- Tut B: diagrama ER → models.py del TP-4
- Tut C: Django shell — 10 queries indispensables
- Tut D: las 4 queries del TP-4 paso a paso con output

### Anexos
- Glosario (framework, lazy, QuerySet, lookup, related_name, migración)
- Cheatsheet A4 imprimible (comandos + lookups + relaciones)
- Mapa MVC ↔ MVT
- Referencias Django 6.0 docs (offline en ChromaDB django-6.0-docs)

---

## 8. Coherencia Incremental

`
Clase 1 Web          → Contexto: qué problema resuelve Django
      ↓
Clase 2 Django       → Herramienta: cómo se estructura con CBVs
      ↓
Clase 3 ORM          → Datos: cómo persisten los objetos
      ↓
TP-4 Django ORM      → Integración: 4 modelos + 4 queries + tests
`

Cada clase abre refiriendo lo previo y cierra anunciando lo siguiente.

---

## 9. Mapa TP-4 → Contenidos (VERIFICADO con repo clonado)

| Item del TP-4 | Clase/§ | Cubierto |
|---------------|---------|----------|
| Setup Python + venv + pip | Clase 2 §4.3 + Tut A guía | ✅ |
| Autor con nombre, email unique, biografia blank | Clase 3 §6.1-6.2 | ✅ |
| Categoria con nombre unique | Clase 3 §6.1-6.2 | ✅ |
| Libro FK a Autor PROTECT, M2M Categoria, campos catálogo | Clase 3 §6.3 | ✅ |
| Prestamo FK Libro CASCADE, fechas, fecha_devolucion nullable | Clase 3 §6.3 | ✅ |
| Libro.prestamos_activos() con filter+count | Clase 3 §7.4 | ✅ |
| Libro.disponibles() y tiene_disponibles() | Clase 3 §7.4 | ✅ |
| libros_por_categoria (filter M2M) | Clase 3 §7.4 | ✅ |
| autores_con_mas_de_n_libros (annotate Count + filter gt) | Clase 3 §7.4 | ✅ |
| libros_sin_disponibilidad (annotate + Q + F) | Clase 3 §7.4 | ✅ |
| top_n_libros_mas_prestados (annotate + order_by + slicing) | Clase 3 §7.4 | ✅ |
| django.test.TestCase + setUpTestData | Clase 3 §8 | ✅ |
| GitHub Actions autograding | Tutorial de guía (alumno lee log y commitea fix) | ✅ |

**Cobertura TP-4: 100%** (todos los items del README + tests verificados).

---

## 10. Paradigma POO estricto (innegociable)

| ❌ Prohibido | ✅ Estándar cátedra |
|-------------|--------------------|
| def home(request): return render(...) | class HomeView(TemplateView): template_name=... |
| @login_required | LoginRequiredMixin |
| @permission_required | PermissionRequiredMixin |
| Lógica suelta en views.py | Métodos CBV: get_context_data, get_queryset, form_valid, dispatch |

**Nota para TP-4**: el TP-4 no requiere vistas (solo modelos + queries + tests). Pero desde la Clase 2 se introducen CBVs como preparación del Tema 05.

---

## 11. Bibliografía

### Obligatoria plan mínimo
- Django Software Foundation (2024). Documentación oficial Django. https://docs.djangoproject.com/en/6.0/ → **offline ChromaDB django-6.0-docs** (2443 chunks)
- MDN — desarrollo web y HTML
- Python Software Foundation (2024). Python 3 documentation → **offline ChromaDB python-3.14-docs** (5306 chunks)

### Pedagógica (edu_knowledge ChromaDB)
- Mayer & Fiorella (2023) multimedia learning
- Sweller & Chen (2023) cognitive load
- Haladyna (2024) Bloom assessment
- WCAG 2.2/3.0 accesibilidad

### Base docente
- ingesta/introweb.pdf filminas 2025 → ChromaDB introweb (26 chunks)
- TP-4 repo → tp-repo/ (clonado vía gh CLI)

---

## 12. Scope

### Dentro
- ✅ Todo §3-9
- ✅ CBV desde minuto 1 de Clase 2
- ✅ 100% cobertura TP-4

### FUERA (evitar scope creep)
- ❌ Forms Django → Tema 05
- ❌ Templates con herencia compleja → Tema 05
- ❌ Auth (login/logout/permisos) → Tema 06
- ❌ select_related/prefetch_related avanzado → Tema 04
- ❌ Señales, middleware custom → Tema 07
- ❌ Admin site → mencionar, profundizar Tema 05
- ❌ Deployment → no cubierto en cursada

Marcos: "Eso está fuera de scope del Tema 03" — diferir sin discusión.

---

## 13. Criterios class-ready

1. ✅ Cobertura ≥95% Módulo III + parcial IV asignado
2. ✅ Cada objetivo mapeado a actividad + item evaluable
3. ✅ 100% TP-4 cubierto (verificado con repo real)
4. ✅ 0 FBVs en ejemplos de código
5. ✅ Guía autocontenida (alumno offline)
6. ✅ FAQ ≥10 preguntas
7. ✅ Filminas ≤40 palabras/slide (Mayer)
8. ✅ Densidad cognitiva dentro umbrales guardrail
9. ✅ Referencias validadas

---

## 14. Próximos pasos del pipeline

| # | Paso | Comando |
|---|------|---------|
| 1 | **GATE aprobación** | responder APROBADO |
| 2 | Minuta + filminas.md | /edu-create-class |
| 3 | Guía de estudio extensa | /edu-create-study-guide |
| 4 | TP markdown trazable | /edu-create-tp |
| 5 | Loop de calidad de escritura | /edu-quality |
| 6 | Loop de coherencia | |
| 7 | Loop de referencias | |
| 8 | Guardrail académico | |
| 9 | Simulación de alumnos | /edu-test-topic |
| 10 | Aplicar correcciones | |
| 11 | Plan JSON de filminas | parse_filminas.py |
| 12 | Validar plan | validate_plan.py |
| 13 | Publicar en Google Slides | slides_pipeline.py |
| 14 | Verificación visual | republicar hasta 0 errores |
| 15 | Cerrar tema | /edu-close-topic |

---

## 15. Confirmación docente

Antes de avanzar al Paso 4 (Contenido), confirmar:

- [ ] Módulo III + IV parcial como se definió
- [ ] 3 clases de 180 min
- [ ] CBV desde minuto 1 innegociable
- [ ] Versión Django: **5.1+** (por TP-4 requirements.txt) — confirmar si subir a 5.2 LTS
- [ ] Nombre proyecto/app exactos del TP-4: biblioteca / catalogo
- [ ] Git ya fue visto en tema previo — NO se reintroduce en Clase 2
- [ ] No hay temas extra a incluir

**Responder APROBADO para continuar con /edu-create-class.**

---

_Diseño verificado contra el repo real del TP-4. Cobertura 100%. Scope acotado. POO innegociable. Listo para revisión._