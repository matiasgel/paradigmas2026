# Filminas — Tema 03: Desarrollo Web con Django: Intro Web + Django + ORM
## Laboratorio de Programación y Lenguajes (IF009) — UNTDF 2026
**Módulo III completo + Módulo IV parcial · 3 sesiones × 180 min · ~74 filminas**
*Ritmo objetivo: ~4 min por filmina · Clase 1: 22 slides · Clase 2: 22 slides · Clase 3: 30 slides*

---

## CLASE 1 — INTRODUCCIÓN A PROGRAMACIÓN WEB + PATRÓN MVC (180 min)

---

### [F-00] Portada — Clase 1

@tipo: portada
@imagen: background
@prompt-imagen: composición flat design con formas geométricas, rectángulos bordo y gris oscuro conectados por líneas grises, ícono abstracto de globo terráqueo con flechas circulares, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Tema 03 — Clase 1
## Introducción a Programación Web y patrón MVC
### Laboratorio de Programación y Lenguajes · UNTDF 2026
### Prof. Matías Gel

---

### [F-01] Agenda del día

@tipo: tabla

# ¿Qué vemos hoy? (180 min)

| Bloque | Duración | Tema |
|--------|----------|------|
| T0 | 15 min | Apertura: DevTools Network en vivo |
| T1 | 25 min | App Web vs Sitio Web |
| T2 | 30 min | Cliente/Servidor + modelo 3 capas |
| — | 20 min | **Pausa + diseño responsive** |
| T3 | 50 min | **Patrón MVC (bloque central)** |
| T4 | 30 min | HTTP hands-on con curl |
| T5 | 10 min | Cierre + preview Clase 2 |

> **Al final de hoy:** van a poder mapear cualquier web a Modelo / Vista / Controlador.

---

### [F-02] Apertura: DevTools abierto

@tipo: demo

# Abrimos DevTools ahora

## Actividad conjunta (pizarra digital)

1. Ir a `https://www.untdf.edu.ar`
2. Abrir DevTools (F12) → pestaña **Network**
3. Recargar con Ctrl+F5
4. Observar: URL, Method, Status, Type, Size, Time

```
GET  /            200  document  45 KB  220 ms
GET  /style.css   200  stylesheet  12 KB  18 ms
GET  /logo.png    200  image       32 KB  25 ms
```

> ¿Qué es cada fila? ¿Por qué hay varias para **una** página?

---

### [F-03] App Web vs Sitio Web

@tipo: tabla-comparativa

# App web vs Sitio web

| Dimensión | Sitio web estático | App web |
|-----------|-------------------|---------|
| Contenido | Mismo HTML para todos | Generado según usuario |
| Estado | No tiene | Tiene (sesión, BD) |
| Interactividad | Mínima (links) | Formularios, acciones |
| Ejemplos UNTDF | Landing institucional | Moodle, SIU-Guaraní |
| Backend | Archivos en servidor | Proceso + BD |

> **Clave:** la **app web** tiene lógica del lado del servidor → necesita un framework como Django.

---

### [F-04] Ejemplos del mundo real

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Diagrama flat: tres rectángulos bordo apilados verticalmente en el lado derecho, conectados por flechas grises. El superior es pequeño, el medio mediano y el inferior grande. A la izquierda, tres íconos abstractos: una ventana, un engranaje y un cilindro. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Apps web que usan todos los días

## Estudiantes
- **Moodle UNTDF** → estado: cursadas, entregas
- **SIU-Guaraní** → estado: inscripciones, notas
- **Instagram / YouTube** → estado: feed, historial

## Contra-ejemplo
- Un blog de WordPress servido como HTML pre-renderizado

> Ejercicio rápido: ¿qué parte de cada una es "app" y qué parte "sitio"?

---

### [F-05] Cliente-Servidor — el modelo base

@tipo: diagrama
@imagen: content
@prompt-imagen: Diagrama flat de dos rectángulos bordo — uno pequeño a la izquierda (cliente) y uno grande a la derecha (servidor) — conectados por dos flechas horizontales grises: una arriba apuntando a la derecha, otra abajo apuntando a la izquierda. En el centro entre ambos, una nube gris. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Modelo Cliente-Servidor

## Dos procesos que se comunican por red

- **Cliente** → inicia la conversación ("dame /productos")
- **Servidor** → escucha, procesa y responde

## Propiedades

- Separación de responsabilidades
- Múltiples clientes por un servidor
- El cliente **NO** sabe cómo el servidor almacena los datos
- El servidor **NO** sabe si el cliente es Chrome, Firefox, curl o un script Python

---

### [F-06] Arquitectura 3 capas

@tipo: diagrama
@imagen: content
@prompt-imagen: Tres rectángulos horizontales apilados verticalmente, todos bordo, separados por espacios grises. El superior es más angosto, el medio el más ancho, el inferior del mismo ancho que el superior. A la derecha, una flecha doble vertical gris los conecta a todos. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Arquitectura en 3 capas

## Capa Presentación
- HTML, CSS, JS que ve el usuario
- Responsabilidad: mostrar y capturar

## Capa Negocio (Aplicación)
- Reglas del dominio
- Responsabilidad: decidir qué hacer

## Capa Datos (Persistencia)
- Base de datos relacional (PostgreSQL, SQLite)
- Responsabilidad: guardar y recuperar

> **Django** cubre las 3 capas con ayuda de librerías externas.

---

### [F-07] Ejercicio en clase: mapear un e-commerce

@tipo: socratica

# Ejercicio conjunto (10 min)

## Caso: tienda online

> Un usuario agrega un libro al carrito, paga con tarjeta y recibe email de confirmación.

## Identifiquemos cada capa

- **Presentación** → ¿qué ve el usuario?
- **Negocio** → ¿qué reglas hay? (stock, descuentos, impuestos)
- **Datos** → ¿qué se guarda? (pedido, pago, usuario)

## En pizarra:

- Libramos 3 columnas y anotamos juntos
- El docente reparte responsabilidades: A/B/C

---

### [F-08] Patrón MVC — la idea central

@tipo: diagrama
@imagen: content
@prompt-imagen: Diagrama triangular con tres rectángulos bordo en los vértices — uno arriba, uno abajo-izquierda, uno abajo-derecha — conectados entre sí por tres flechas grises curvas formando un triángulo. En el centro del triángulo, un pequeño círculo gris. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Patrón MVC

## Separación en 3 responsabilidades

- **Modelo** → los datos y las reglas de dominio
- **Vista** → la presentación (HTML que ve el usuario)
- **Controlador** → el pegamento: recibe pedido, coordina, decide qué vista mostrar

## ¿Por qué importa?

- Equipos distintos pueden trabajar en paralelo
- Cambiar el look & feel no toca la lógica
- Cambiar la BD no toca las pantallas

---

### [F-09] MVC — quién habla con quién

@tipo: concepto-mixto

# Flujo de una petición en MVC

## Secuencia

1. Usuario hace click → Navegador envía `GET /libros/42`
2. **Controlador** recibe la URL
3. **Controlador** pide datos al **Modelo**: `Libro.get(42)`
4. **Modelo** consulta la BD y devuelve el objeto
5. **Controlador** pasa los datos a la **Vista**
6. **Vista** arma el HTML
7. **Controlador** devuelve el HTML al navegador

```
Navegador → Controlador → Modelo → BD
               ↓              ↑
               Vista ←────────┘
               ↓
          HTML al navegador
```

---

### [F-10] Aclaración MVC vs MVT de Django

@tipo: tabla-comparativa

# MVC clásico vs MVT de Django

| MVC (Ruby on Rails, Spring) | MVT (Django) | ¿Qué hace? |
|-----------------------------|--------------|------------|
| Model | **Model** | Datos + reglas de dominio |
| View (HTML) | **Template** | Presentación HTML |
| Controller | **View** (en `views.py`) | Decide, coordina, responde |

> **Trampa**: en Django, el archivo `views.py` contiene lo que MVC llama **controladores**.
> La "vista" (HTML) en Django se llama **template**.

> Regla para no confundirse: cuando escribimos `class LibroDetailView(...)` en `views.py`, estamos escribiendo un **controlador**.

---

### [F-11] Ejercicio en clase: clasificar responsabilidades

@tipo: socratica

# Ejercicio conjunto (15 min) — Caso biblioteca

> Un alumno entra a /libros/ → ve listado → hace click en uno → ve detalle y puede reservar.

## Clasifiquemos cada cosa en M, V o C

1. La tabla `libros` en SQLite
2. El HTML con la lista de libros
3. La función que recibe `/libros/` y arma la página
4. El método `libro.tiene_disponibles()`
5. El CSS del sitio
6. La regla "no se puede reservar si hay 0 disponibles"
7. La consulta `SELECT * FROM libros WHERE categoria='SF'`

> **Docente**: se debate cada ítem con los alumnos antes de marcar.

---

### [F-12] HTTP — el idioma de la web

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Dos rectángulos bordo, uno a la izquierda pequeño y uno a la derecha grande, conectados por dos flechas horizontales grises — la superior con un ícono abstracto de sobre, la inferior con un círculo concéntrico. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# HTTP — modelo petición / respuesta

## Cada interacción web es

- **Una petición** (request) del cliente
- **Una respuesta** (response) del servidor

## Stateless

- Cada petición es independiente
- El servidor no "recuerda" al cliente entre pedidos (salvo usando cookies/sesión)

> HTTP viaja sobre TCP/IP — pero como programadores web, trabajamos al nivel de request/response.

---

### [F-13] Métodos HTTP

@tipo: tabla

# Métodos HTTP que vamos a usar

| Método | Para qué | Ejemplo Django |
|--------|----------|---------------|
| **GET** | Leer sin efectos | Ver listado de libros |
| **POST** | Crear / enviar datos | Registrar un préstamo |
| **PUT** | Reemplazar entero | Actualizar perfil completo |
| **PATCH** | Modificar parcial | Cambiar solo el email |
| **DELETE** | Borrar | Cancelar reserva |

> En Clase 2-3 usaremos casi siempre **GET** y **POST**.
> Forms con PUT/PATCH/DELETE se ven en Tema 05.

---

### [F-14] Códigos de estado HTTP

@tipo: tabla

# Códigos de respuesta que verán a diario

| Código | Significado | Cuándo aparece |
|--------|-------------|----------------|
| 200 OK | Todo bien | Petición exitosa |
| 301 Moved | Redirigido permanente | `/libros` → `/libros/` |
| 302 Found | Redirigido temporal | Post-login |
| 400 Bad Request | Error del cliente | Formulario malformado |
| 403 Forbidden | Sin permiso | Ruta protegida sin login |
| 404 Not Found | No existe | URL mal tipeada |
| 500 Server Error | Error del servidor | Excepción no atrapada |

> En DevTools → Network van a ver estos códigos en la columna **Status**.

---

### [F-15] Demo en vivo: curl

@tipo: demo

# Demo conjunta — curl (20 min)

```bash
# 1. GET simple
curl -i https://httpbin.org/get

# 2. Ver solo la cabecera
curl -I https://www.untdf.edu.ar

# 3. POST con datos
curl -X POST https://httpbin.org/post \
     -d "nombre=Ana&libro=Sapiens"

# 4. Ver el 404
curl -i https://httpbin.org/status/404
```

## Tarea para ustedes ahora

Cada alumno corre los 4 comandos y anota:
- El **status code**
- El **Content-Type**
- Los primeros 3 headers

---

### [F-16] Framework vs Librería

@tipo: tabla-comparativa

# Framework vs Librería

| Librería | Framework |
|----------|-----------|
| **Vos** llamás al código | El código **te llama a vos** |
| Vos diseñás la arquitectura | El framework impone arquitectura |
| Ejemplo Python: `requests`, `numpy` | Ejemplo Python: **Django**, FastAPI |
| "Te uso cuando quiero" | "Llenás los huecos que te pido" |

## Principio de Hollywood

> *"Don't call us — we'll call you"*
>
> Un framework te dice: "escribí una clase que herede de `ListView`, yo me encargo del resto".

---

### [F-17] Panorama de frameworks MVC web

@tipo: tabla-comparativa

# Frameworks MVC para web (por lenguaje)

| Lenguaje | Framework | Característica |
|----------|-----------|----------------|
| Python | **Django** | Baterías incluidas, ORM propio, admin |
| Python | Flask, FastAPI | Micro, componible |
| Ruby | Ruby on Rails | Convention over configuration |
| PHP | Laravel | Pragmático, Blade templates |
| Java | Spring MVC | Enterprise, inyección de dependencias |
| JavaScript | Express (backend) | Minimalista |

## En esta cátedra usamos Django

- Maduro (2005), estable, LTS
- Usado en Instagram, Mozilla, Disqus
- ORM incluido, admin generado automático

---

### [F-18] ¿Por qué Django y no Flask?

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Dos rectángulos bordo lado a lado — el de la izquierda pequeño y liviano con pocos elementos internos (tres puntos grises), el de la derecha grande y denso con una grilla de pequeños cuadrados grises dentro. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# ¿Por qué Django y no Flask?

## Flask (micro)
- Vos elegís todo: ORM, forms, auth, admin
- Más libertad → **más decisiones**
- Ideal para APIs pequeñas o prototipos

## Django (baterías incluidas)
- Elecciones ya tomadas: **ORM propio**, forms, auth, admin, migrations
- Menos libertad → **más velocidad de entrega**
- Ideal para apps CRUD medianas/grandes

> **Para aprender**: Django enseña convenciones del mundo real.
> **Para el TP-4**: Django nos da el ORM + tests + admin sin escribir nada extra.

---

### [F-19] Preview Clase 2

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Flecha grande bordo apuntando a la derecha, siguiendo un camino de tres círculos grises pequeños de izquierda a derecha. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Preview — Clase 2 (jueves)

## Van a salir con

1. Un proyecto Django instalado
2. Una app `catalogo` creada
3. Una primera **class-based view** funcionando
4. El servidor `runserver` corriendo localmente

## Traen para la próxima

- Laptop con Python 3.13+ instalado
- Git configurado
- (opcional) cuenta GitHub para el TP-4

---

### [F-20] Ticket de salida — Clase 1

@tipo: socratica

# Ticket de salida (3 min)

## En una hoja, responder:

1. Diferencia entre **sitio web** y **app web** en una oración.
2. Cuál es la diferencia entre **Modelo, Vista y Controlador** (una oración cada uno).
3. ¿Qué código HTTP devuelve una ruta que no existe?
4. ¿Qué es el **principio de Hollywood**?

> Lo entregan al salir — sin nombre si prefieren. Se repasan las respuestas al inicio de la Clase 2.

---

### [F-21] Cierre Clase 1

@tipo: cierre
@imagen: background
@prompt-imagen: composición flat con un gran círculo bordo a la derecha y tres pequeños círculos grises a la izquierda alineados horizontalmente, conectados por una flecha gris al círculo grande. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Clase 1 cerrada

## Hoy aprendimos

- App web vs sitio web estático
- Arquitectura 3 capas + cliente/servidor
- Patrón MVC / MVT
- HTTP: métodos y códigos
- Por qué Django

> **Próxima clase (Clase 2):** instalamos Django y escribimos nuestra primera class-based view.

---


## CLASE 2 — INTRODUCCIÓN A DJANGO CON POO (180 min)

---

### [F-22] Portada — Clase 2

@tipo: portada
@imagen: background
@prompt-imagen: composición flat design con un rectángulo grande bordo en el centro dividido en cuatro cuadrantes por líneas grises, con pequeños íconos abstractos geométricos en cada cuadrante. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Tema 03 — Clase 2
## Introducción a Django con Programación Orientada a Objetos
### Laboratorio de Programación y Lenguajes · UNTDF 2026

---

### [F-23] Recap Clase 1 + Agenda

@tipo: tabla

# Agenda (180 min)

| Bloque | Duración | Tema |
|--------|----------|------|
| T0 | 10 min | Recap Clase 1 (tickets de salida) |
| T1 | 20 min | Framework vs librería (Hollywood) |
| T2 | 25 min | Django en el ecosistema Python |
| T3 | 20 min | Instalación + venv |
| — | 15 min | **Pausa** |
| T4 | 40 min | startproject, startapp, settings, urls |
| T5 | 30 min | **Primera CBV — hands-on juntos** |
| T6 | 10 min | runserver + preview Clase 3 |
| T7 | 10 min | Ticket de salida + cierre |

---

### [F-24] Framework = inversión de control

@tipo: concepto-mixto

# Principio de Hollywood en acción

## Lo que NO vamos a escribir

```python
# NO: nosotros NO escribimos el servidor HTTP
servidor = HTTPServer(...)
while True:
    conexion = servidor.accept()
    pedido = parsear(conexion)
    ...
```

## Lo que SÍ vamos a escribir

```python
# SÍ: solo llenamos los "huecos" que pide Django
class ListaLibrosView(ListView):
    model = Libro
    template_name = "catalogo/lista.html"
```

> Django arma el servidor, parsea HTTP, matchea URLs, instancia tu clase y llama tus métodos.

---

### [F-25] Django en el ecosistema Python

@tipo: tabla

# Django en números (2026)

| Característica | Valor |
|----------------|-------|
| Primera versión | 2005 |
| Versión LTS actual | **5.2 LTS** |
| Usuarios notables | Instagram, Mozilla, Pinterest, Disqus |
| Licencia | BSD (libre y comercial) |
| Lenguaje | Python 3.13+ |
| Baterías | ORM, admin, auth, migrations, forms, tests |

> Para el TP-4 usamos **Django 5.1+** (el repo viene configurado así).

---

### [F-26] Instalación juntos — paso a paso

@tipo: codigo

# Setup del entorno (20 min — todos conmigo)

```bash
# 1. Crear venv (en la carpeta del TP)
python -m venv .venv

# 2. Activar
# Windows:
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# 3. Instalar Django
pip install "django>=5.1,<6.0"

# 4. Verificar
django-admin --version
python -c "import django; print(django.get_version())"
```

> Antes de seguir: TODOS levantan la mano si les falló algo. Lo resolvemos juntos.

---

### [F-27] Crear proyecto + app

@tipo: codigo

# Actividad conjunta — creamos el proyecto del TP-4

```bash
# 1. Crear proyecto llamado 'biblioteca'
django-admin startproject biblioteca .
# El punto al final → proyecto en la carpeta actual

# 2. Entrar a la carpeta y crear la app 'catalogo'
python manage.py startapp catalogo

# 3. Migraciones iniciales
python manage.py migrate

# 4. Correr el servidor
python manage.py runserver
```

> Abrir `http://127.0.0.1:8000/` — debería aparecer el cohete de Django.

---

### [F-28] Estructura del proyecto

@tipo: codigo

# Estructura generada

```
biblioteca/                ← raíz (manage.py acá)
├── manage.py              ← CLI: runserver, migrate, test, shell
├── biblioteca/            ← "proyecto" (config global)
│   ├── settings.py        ← config central
│   ├── urls.py            ← URLs raíz
│   ├── wsgi.py / asgi.py  ← servidor productivo
│   └── __init__.py
└── catalogo/              ← "app" (feature)
    ├── models.py          ← datos
    ├── views.py           ← controladores (CBV)
    ├── admin.py           ← admin generado
    ├── tests.py / tests/  ← tests django.test
    ├── apps.py            ← config app
    └── migrations/
```

> Preguntita: ¿dónde van a ir las 4 queries del TP-4?
> **Respuesta**: en `catalogo/queries.py` (archivo nuevo).

---

### [F-29] settings.py — lo mínimo a conocer

@tipo: codigo

# settings.py — lo que tocan en el TP

```python
# biblioteca/settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "catalogo",              # ← agregamos nuestra app
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Ushuaia"
```

> **Importante**: agregar `"catalogo"` a `INSTALLED_APPS` es obligatorio para que detecte los modelos.

---

### [F-30] URLconf — el router de Django

@tipo: codigo

# URL routing con `.as_view()`

```python
# biblioteca/urls.py (raíz)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalogo/", include("catalogo.urls")),
]
```

```python
# catalogo/urls.py (nuevo — lo creamos juntos)
from django.urls import path
from .views import HolaMundoView

app_name = "catalogo"

urlpatterns = [
    path("hola/", HolaMundoView.as_view(), name="hola"),
]
```

> **Regla cátedra**: TODA URL usa `.as_view()` — porque todas las vistas son clases.

---

### [F-31] Primera Class-Based View — TemplateView

@tipo: codigo

# Actividad conjunta — escribimos HolaMundoView

```python
# catalogo/views.py
from django.views.generic import TemplateView


class HolaMundoView(TemplateView):
    """Primera CBV de la cátedra — muestra un saludo parametrizable."""

    template_name = "catalogo/hola.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["mensaje"] = "Hola 3° año de Sistemas UNTDF"
        ctx["anio"] = 2026
        return ctx
```

> **Sin decoradores. Sin funciones. Siempre clase.**

---

### [F-32] El template

@tipo: codigo

# catalogo/templates/catalogo/hola.html

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Hola Django</title>
</head>
<body>
    <h1>{{ mensaje }}</h1>
    <p>Año académico: {{ anio }}</p>
    <p>Si ves esto, tu primera CBV funciona.</p>
</body>
</html>
```

> Ruta exacta: `catalogo/templates/catalogo/hola.html` (sí, `catalogo` dos veces — convención).

---

### [F-33] Probar en el navegador

@tipo: demo

# Demo conjunta

```bash
python manage.py runserver
```

Abrir: `http://127.0.0.1:8000/catalogo/hola/`

> Debe verse:
> **Hola 3° año de Sistemas UNTDF**
> *Año académico: 2026*

## Si falla

- **404**: URL mal tipeada o `include` mal hecho
- **500 TemplateDoesNotExist**: ruta del template mal — recordar `templates/catalogo/`
- **500 ImproperlyConfigured**: falta `"catalogo"` en `INSTALLED_APPS`

---

### [F-34] ¿Por qué CBV y no FBV?

@tipo: tabla-comparativa

# Function-Based View (NO usamos) vs Class-Based View (SÍ usamos)

| FBV (prohibido en cátedra) | CBV (estándar cátedra) |
|----------------------------|------------------------|
| `def home(request): ...` | `class HomeView(TemplateView): ...` |
| `@login_required` (decorador) | `LoginRequiredMixin` |
| `@permission_required(...)` | `PermissionRequiredMixin` |
| Lógica mezclada en una función | Métodos extensibles: `get_context_data`, `get_queryset`, `form_valid` |
| No se reusa fácilmente | Herencia + mixins |

> **Decisión docente**: venimos del Módulo I con POO, por coherencia Django se usa POO.

---

### [F-35] Jerarquía de CBVs genéricas

@tipo: diagrama
@imagen: content
@prompt-imagen: Diagrama de árbol con un rectángulo bordo grande arriba, dos rectángulos bordo medianos debajo conectados por líneas grises, y tres rectángulos bordo pequeños en la base conectados a los medianos. Estilo flat design, fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# CBVs que van a usar

## Raíz
- **View** → base de todo

## Nivel intermedio
- **TemplateView** → mostrar un HTML con contexto
- **RedirectView** → redireccionar

## Por modelo (CRUD)
- **ListView** → listar objetos
- **DetailView** → mostrar uno
- **CreateView** → formulario de creación
- **UpdateView** → formulario de edición
- **DeleteView** → confirmar borrado

> Para el **TP-4** no piden vistas, pero van a ver `ListView` en Clase 3 como preview.

---

### [F-36] Ejercicio en clase: HolaView con nombre dinámico

@tipo: codigo

# Ejercicio conjunto (10 min)

> Modificar `HolaMundoView` para que el saludo incluya un nombre pasado por URL.

## Ruta esperada
```
/catalogo/hola/Matias/  →  "Hola Matias — 3° año..."
```

## Pistas

1. En `urls.py`: `path("hola/<str:nombre>/", HolaMundoView.as_view(), name="hola")`
2. En la vista: el parámetro llega como `self.kwargs["nombre"]`
3. Agregarlo al contexto en `get_context_data`

## Resolución conjunta

Resolvemos la pista 3 juntos en la pizarra — 5 min.

---

### [F-37] runserver + autoreload

@tipo: concepto-abstracto

# Flujo de trabajo con runserver

## Ciclo típico

1. Editar un archivo `.py`
2. Django detecta el cambio → reinicia automáticamente
3. Recargar el navegador → ver el cambio

## Lo que NO se recarga automático

- Archivos en `templates/` → sí reloads (el template se re-renderiza)
- Archivos estáticos → requieren Ctrl+F5 para saltar la cache

## runserver es SOLO para desarrollo

- Nunca se usa en producción
- Producción → gunicorn/uwsgi + nginx (Tema futuro)

---

### [F-38] Preview Clase 3

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Diagrama flat con tres cilindros bordo pequeños alineados verticalmente a la derecha, conectados a un rectángulo bordo mediano a la izquierda por tres flechas grises horizontales. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Preview — Clase 3

## La clase más importante del Tema 03

- Persistencia e **impedance mismatch**
- **Modelos Django** del TP-4 (Autor, Categoria, Libro, Prestamo)
- Migraciones (`makemigrations` + `migrate`)
- CRUD con QuerySet
- **Las 4 queries del TP-4** resueltas juntos

> **Traen**: el proyecto `biblioteca` + app `catalogo` funcionando de hoy.
> **No traen**: el TP-4 clonado todavía — lo hacemos juntos en Clase 3.

---

### [F-39] Ticket de salida — Clase 2

@tipo: socratica

# Ticket de salida (3 min)

## En una hoja:

1. ¿Qué significa que Django usa el **principio de Hollywood**?
2. ¿Por qué agregamos `"catalogo"` a `INSTALLED_APPS`?
3. ¿Qué hace `.as_view()` en una URL?
4. ¿Por qué **no** usamos funciones como vistas en esta cátedra?

> Se entrega al salir. Se revisan las respuestas al inicio de Clase 3.

---

### [F-40] Cierre Clase 2

@tipo: cierre
@imagen: background
@prompt-imagen: Composición flat design con un gran rectángulo bordo central con una línea gris vertical que lo divide, y pequeños círculos grises dispersos alrededor. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Clase 2 cerrada

## Hoy aprendimos

- Framework = inversión de control
- Estructura de proyecto Django
- settings, URLconf, TemplateView
- Primera CBV funcionando
- Regla cátedra: **CBV siempre**

> **Próxima clase (Clase 3):** la más intensa — ORM completo + las 4 queries del TP-4.

---


## CLASE 3 — DJANGO ORM COMPLETO PARA TP-4 (180 min)

---

### [F-41] Portada — Clase 3

@tipo: portada
@imagen: background
@prompt-imagen: Composición flat design con cuatro cilindros bordo de distintos tamaños alineados horizontalmente, conectados entre sí por flechas grises dobles. Sobre los cilindros, un rectángulo bordo con líneas horizontales grises dentro. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Tema 03 — Clase 3
## Django ORM completo para TP-4
### La clase más densa: 4 modelos, 4 queries, tests

---

### [F-42] Agenda Clase 3

@tipo: tabla

# Agenda (180 min) — CLASE ORM

| Bloque | Duración | Tema |
|--------|----------|------|
| T0 | 10 min | Recap Clase 2 + objetivos |
| T1 | 15 min | Persistencia + impedance mismatch |
| T2 | 30 min | Modelos + campos (Autor, Categoria) |
| T3 | 20 min | Relaciones FK / M2M (Libro, Prestamo) |
| — | 15 min | **Pausa** |
| T4 | 20 min | Migraciones |
| T5 | 30 min | CRUD con QuerySet — en el shell |
| T6 | 25 min | **Las 4 queries del TP-4** |
| T7 | 15 min | django.test.TestCase + cierre |

> **Objetivo**: al final de hoy, pueden resolver el 100% del TP-4.

---

### [F-43] Persistencia — el problema

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Dos rectángulos bordo: uno a la izquierda mediano con elementos abstractos circulares y hexagonales dentro (representando objetos), otro a la derecha con líneas horizontales paralelas grises (representando filas de tabla). Entre ambos, una flecha gris doble con un signo de interrogación gris en el medio. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Persistencia — el problema

## En memoria tenemos objetos
```python
libro = Libro("Sapiens", autor=harari)
```

## En disco tenemos tablas relacionales
```
id | titulo  | autor_id
1  | Sapiens | 17
```

## ¿Cómo pasamos de uno al otro?

> Ése es el problema del **ORM**: Object-Relational Mapping.

---

### [F-44] Soluciones en Python

@tipo: tabla

# Alternativas para persistir en Python

| Solución | Tipo | Uso típico |
|----------|------|------------|
| pickle / shelve | Serialización | Caché local, NO para BD multiusuario |
| CSV / JSON | Archivos planos | Export/import |
| **Django ORM** | ORM integrado | Apps web Django |
| SQLAlchemy | ORM standalone | Apps Python cualquier framework |
| Peewee | ORM minimalista | Scripts pequeños |
| SQL crudo | Sin ORM | Control total, más código |

> **Cátedra**: Django ORM para el TP-4. SQLAlchemy se ve en Tema 06 para comparar.

---

### [F-45] Impedance Mismatch — el choque

@tipo: tabla-comparativa

# Mundo OO vs mundo relacional

| Mundo OO (Python) | Mundo Relacional (SQL) |
|-------------------|------------------------|
| Objetos con identidad y métodos | Filas con PK, sin comportamiento |
| Herencia (Libro(Publicacion)) | No hay herencia nativa — hay estrategias |
| Colecciones (`libro.categorias`) | FK + tablas intermedias (M2M) |
| `==` lógico (`__eq__`) | Identidad = misma PK |
| Navegación: `libro.autor.nombre` | JOIN explícito |

> Rol del **ORM**: traducir automáticamente entre los dos mundos.

---

### [F-46] Primer modelo Django — Autor

@tipo: codigo

# Empezamos el TP-4 — modelo Autor

```python
# catalogo/models.py
from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre
```

## Decisiones

- `CharField` requiere `max_length` (límite de columna VARCHAR)
- `EmailField` → valida formato + usa VARCHAR
- `unique=True` → índice único en la BD
- `blank=True` → opcional en formularios

> Escribimos este modelo juntos ahora en el proyecto del TP-4.

---

### [F-47] Modelo Categoria

@tipo: codigo

# Modelo Categoria — el más simple

```python
class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self) -> str:
        return self.nombre
```

## Ejercicio en clase (5 min)

> Cada alumno lo escribe en su archivo `models.py` y lo muestra al compañero de al lado.

## Preguntita

¿Qué pasa si dos categorías quieren llamarse "fantasía"?

> **Respuesta**: `IntegrityError: UNIQUE constraint failed` → exactamente lo que queremos.

---

### [F-48] null vs blank — el clásico

@tipo: tabla-comparativa

# null vs blank — no son lo mismo

| Parámetro | Dónde actúa | Ejemplo |
|-----------|-------------|---------|
| `null=True` | **Base de datos** — permite NULL | `fecha_devolucion = DateField(null=True)` |
| `blank=True` | **Validación de formularios** — permite vacío | `biografia = TextField(blank=True)` |

## Regla práctica

- Campos de texto (Char/Text): **solo** `blank=True` (Django usa `""` en vez de NULL)
- Campos de fecha/número: **ambos** si el campo es opcional: `null=True, blank=True`

## En el TP-4

- `biografia = TextField(blank=True)` → opcional
- `fecha_devolucion = DateField(null=True, blank=True)` → puede estar sin devolver

---

### [F-49] Modelo Libro — con relaciones

@tipo: codigo

# Modelo Libro — FK y M2M

```python
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=32, unique=True)
    fecha_publicacion = models.DateField()
    cantidad_total = models.PositiveIntegerField(default=1)

    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        related_name="libros",
    )
    categorias = models.ManyToManyField(
        Categoria,
        related_name="libros",
        blank=True,
    )

    def __str__(self) -> str:
        return self.titulo
```

> Escribimos juntos. Una línea a la vez. Paramos en cada campo a discutir el "por qué".

---

### [F-50] on_delete — decisión de dominio

@tipo: tabla-comparativa

# on_delete — qué pasa al borrar el "padre"

| Estrategia | Efecto | Cuándo usarla |
|------------|--------|---------------|
| **CASCADE** | Borra los hijos | `Prestamo → Libro` (TP-4) |
| **PROTECT** | Prohíbe borrar si hay hijos | `Libro → Autor` (TP-4) |
| **SET_NULL** | Pone NULL en los hijos | "autor desconocido" tolerable |
| **SET_DEFAULT** | Pone un default | Autor "Anónimo" |
| **DO_NOTHING** | Django no hace nada | Control manual |

## Preguntita conjunta

> ¿Por qué en el TP-4 `Libro→Autor` es PROTECT y `Prestamo→Libro` es CASCADE?

---

### [F-51] Métodos de dominio en Libro

@tipo: codigo

# Métodos de Libro — reglas de dominio

```python
class Libro(models.Model):
    # ... campos arriba ...

    def prestamos_activos(self) -> int:
        return self.prestamos.filter(
            fecha_devolucion__isnull=True
        ).count()

    def disponibles(self) -> int:
        return self.cantidad_total - self.prestamos_activos()

    def tiene_disponibles(self) -> bool:
        return self.disponibles() > 0
```

> `self.prestamos` existe porque pusimos `related_name="prestamos"` en Prestamo.
> `__isnull=True` es el lookup ORM para `IS NULL`.

---

### [F-52] Modelo Prestamo

@tipo: codigo

# Modelo Prestamo — cierra el grafo

```python
class Prestamo(models.Model):
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="prestamos",
    )
    nombre_prestatario = models.CharField(max_length=120)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def esta_activo(self) -> bool:
        return self.fecha_devolucion is None

    def __str__(self) -> str:
        estado = "activo" if self.esta_activo() else "devuelto"
        return f"{self.libro.titulo} — {self.nombre_prestatario} ({estado})"
```

> **Regla de dominio**: `fecha_devolucion IS NULL` ⇔ préstamo activo.

---

### [F-53] Migraciones — cómo llega a la BD

@tipo: codigo

# Migraciones — conjunto

```bash
# 1. Generar archivo de migración a partir de models.py
python manage.py makemigrations catalogo

# Output esperado:
# Migrations for 'catalogo':
#   catalogo/migrations/0001_initial.py
#     - Create model Autor
#     - Create model Categoria
#     - Create model Libro
#     - Create model Prestamo

# 2. Aplicar a SQLite
python manage.py migrate

# 3. (Didáctico) Ver el SQL generado
python manage.py sqlmigrate catalogo 0001
```

> **Clave**: `makemigrations` **NO** toca la BD. Solo escribe un archivo.
> `migrate` sí toca la BD.

---

### [F-54] El shell de Django — CRUD en vivo

@tipo: codigo

# Entramos al shell juntos

```bash
python manage.py shell
```

```python
>>> from catalogo.models import Autor, Categoria, Libro
>>> from datetime import date

>>> # CREATE
>>> ursula = Autor.objects.create(
...     nombre="Ursula K. Le Guin",
...     email="ursula@example.com",
...     biografia="Autora de SF y fantasía."
... )

>>> sf = Categoria.objects.create(nombre="ciencia ficción")
>>> fant = Categoria.objects.create(nombre="fantasía")

>>> libro = Libro.objects.create(
...     titulo="Los desposeídos",
...     isbn="978-0000000001",
...     fecha_publicacion=date(1974, 1, 1),
...     cantidad_total=2,
...     autor=ursula,
... )
>>> libro.categorias.add(sf, fant)
```

> Esto es **exactamente** lo que hace el test `setUpTestData` del TP-4.

---

### [F-55] QuerySet — lectura

@tipo: codigo

# Lectura con QuerySet (en el shell)

```python
# Todos los libros
>>> Libro.objects.all()
<QuerySet [<Libro: Los desposeídos>]>

# Uno por PK o condición única
>>> Libro.objects.get(isbn="978-0000000001")
<Libro: Los desposeídos>

# Filter (siempre devuelve QuerySet)
>>> Libro.objects.filter(autor=ursula)
<QuerySet [<Libro: Los desposeídos>]>

# Lookup con __ (doble guión bajo)
>>> Libro.objects.filter(autor__nombre__icontains="le guin")
<QuerySet [<Libro: Los desposeídos>]>

# Exclude
>>> Libro.objects.exclude(cantidad_total__lt=2)
```

> **QuerySet es lazy**: la consulta se ejecuta cuando iteras, sliceas o llamás `list()`.

---

### [F-56] QuerySet — update y delete

@tipo: codigo

# Update y Delete

```python
# Update individual
>>> libro.cantidad_total = 3
>>> libro.save()

# Update masivo (una sola query SQL)
>>> from django.db.models import F
>>> Libro.objects.filter(autor=ursula).update(
...     cantidad_total=F("cantidad_total") + 1
... )
1   # filas afectadas

# Delete individual
>>> libro.delete()

# Delete masivo
>>> Categoria.objects.filter(nombre__startswith="obsoleta").delete()
```

> `F()` permite expresiones referenciando la misma columna **sin traer el valor a Python**.

---

### [F-57] Las 4 queries del TP-4 — intro

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Cuatro rectángulos bordo pequeños alineados horizontalmente, cada uno con un número abstracto de líneas grises horizontales dentro (representando consultas SQL), unidos por una línea gris horizontal base. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# El core del TP-4 — 4 funciones en queries.py

## Lo que el autograder va a probar

1. `libros_por_categoria(nombre)` — filter con M2M
2. `autores_con_mas_de_n_libros(n)` — annotate + filter
3. `libros_sin_disponibilidad()` — annotate + Q + F
4. `top_n_libros_mas_prestados(n)` — annotate + order_by + slicing

## Las vamos a escribir juntos, una por una

> **Regla**: todo resuelto con ORM puro. Nada de `for libro in ...: if libro.disponibles() == 0`.

---

### [F-58] Query 1 — libros_por_categoria

@tipo: codigo

# Query 1 — filter a través de M2M

```python
# catalogo/queries.py
from .models import Libro

def libros_por_categoria(nombre_categoria: str):
    return Libro.objects.filter(categorias__nombre=nombre_categoria)
```

## ¿Qué SQL genera?

```sql
SELECT "catalogo_libro".*
FROM "catalogo_libro"
INNER JOIN "catalogo_libro_categorias" ON (...)
INNER JOIN "catalogo_categoria" ON (...)
WHERE "catalogo_categoria"."nombre" = 'fantasía'
```

## Demo en shell

```python
>>> from catalogo.queries import libros_por_categoria
>>> libros_por_categoria("fantasía")
<QuerySet [<Libro: Los desposeídos>]>
>>> print(libros_por_categoria("fantasía").query)  # ver el SQL
```

---

### [F-59] Query 2 — autores_con_mas_de_n_libros

@tipo: codigo

# Query 2 — annotate + filter

```python
from django.db.models import Count
from .models import Autor

def autores_con_mas_de_n_libros(n: int):
    return Autor.objects.annotate(
        cantidad_libros=Count("libros")
    ).filter(cantidad_libros__gt=n)
```

## Qué hace `annotate`

- Agrega una **columna calculada** a cada fila del QuerySet
- Acá: a cada Autor le agrega `cantidad_libros` = `COUNT(*)` de sus libros

## Uso

```python
>>> autores_con_mas_de_n_libros(1)
# → autores que tienen 2 o MÁS libros
```

> Anti-patrón (NO hacer):
> ```python
> autores = [a for a in Autor.objects.all() if a.libros.count() > n]  # ❌ N+1 queries
> ```

---

### [F-60] Query 3 — libros_sin_disponibilidad

@tipo: codigo

# Query 3 — la más compleja: annotate + Q + F

```python
from django.db.models import Count, Q, F
from .models import Libro

def libros_sin_disponibilidad():
    return Libro.objects.annotate(
        activos=Count(
            "prestamos",
            filter=Q(prestamos__fecha_devolucion__isnull=True),
        )
    ).filter(activos=F("cantidad_total"))
```

## Descompuesto

- `annotate(activos=Count("prestamos", filter=Q(...)))`: cuenta **solo** los préstamos activos (`filter=` dentro de Count)
- `.filter(activos=F("cantidad_total"))`: devuelve los libros donde esa cuenta iguala `cantidad_total` (columna de la misma tabla → necesita `F`)

> Ejercicio conjunto (10 min): escriban en pizarra qué SQL genera, fila por fila.

---

### [F-61] Query 4 — top_n_libros_mas_prestados

@tipo: codigo

# Query 4 — annotate + order_by + slicing

```python
from django.db.models import Count
from .models import Libro

def top_n_libros_mas_prestados(n: int):
    return (
        Libro.objects
        .annotate(total_prestamos=Count("prestamos"))
        .order_by("-total_prestamos")[:n]
    )
```

## Claves

- `Count("prestamos")` → cuenta TODOS los préstamos (activos + devueltos)
- `order_by("-campo")` → el `-` es DESC
- `[:n]` → slicing → `LIMIT n` en SQL

## Uso

```python
>>> top_n_libros_mas_prestados(3)
<QuerySet [<Libro: ...>, <Libro: ...>, <Libro: ...>]>
```

---

### [F-62] Ejercicio en clase: variantes de las queries

@tipo: socratica

# Ejercicio conjunto (15 min)

## Para cada alumno — escribir en papel

1. Variante Q1: libros de una categoría, ordenados por fecha_publicacion desc
2. Variante Q2: autores con **menos de** n libros
3. Variante Q3: libros con **al menos una copia** disponible (contrario al Q3 real)
4. Variante Q4: top N **prestatarios** (qué persona pidió más libros)

> Resolvemos las 4 en pizarra en conjunto — cada alumno pasa al frente con su propuesta.
> Pista Q4: GROUP BY por `nombre_prestatario` → `values("nombre_prestatario").annotate(...)`.

---

### [F-63] Tests con django.test.TestCase

@tipo: codigo

# django.test.TestCase — lo que ya viene en el TP-4

```python
from datetime import date
from django.test import TestCase
from catalogo.models import Autor, Categoria, Libro, Prestamo

class ModelsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Datos compartidos — UNA vez por clase de test."""
        cls.autor = Autor.objects.create(nombre="Ursula", email="u@ex.com")
        # ...

    def test_disponibilidad_sin_prestamos(self):
        self.assertEqual(self.libro.prestamos_activos(), 0)
        self.assertEqual(self.libro.disponibles(), 2)
```

## Ejecutar

```bash
python manage.py test catalogo -v 2
```

> `TestCase` envuelve todo en una transacción → rollback automático. BD limpia entre tests.

---

### [F-64] setUpTestData vs setUp

@tipo: tabla-comparativa

# setUpTestData vs setUp

| Método | Cuándo corre | Rollback |
|--------|--------------|----------|
| `setUpTestData` (classmethod) | **Una vez** por clase de tests | Transacción de clase |
| `setUp` (método) | **Una vez** por cada test | Por cada test |

## Regla

- **Datos compartidos**: usar `setUpTestData` (más rápido)
- **Datos mutados por test**: usar `setUp` (aislamiento)

## En el TP-4 ya está resuelto — usa `setUpTestData`

> Eso significa que los tests corren más rápido → feedback más rápido → mejor DX.

---

### [F-65] Anti-patrones ORM

@tipo: tabla

# Anti-patrones que el autograder va a castigar

| Anti-patrón | Por qué es malo | Alternativa ORM |
|-------------|-----------------|-----------------|
| `for libro in Libro.objects.all(): if libro.disponibles() == 0: ...` | **N+1 queries** | `libros_sin_disponibilidad()` con annotate |
| `len(qs)` para contar | Trae todo a memoria | `qs.count()` |
| `qs[0]` para "el primero" | Hace sort implícito confuso | `qs.order_by(...).first()` |
| Usar SQL crudo sin motivo | Pierde portabilidad | Lookups ORM |
| `.filter(x=1).filter(y=2).filter(z=3)` en M2M | Joins duplicados | Usar Q combinado |

> **Pauta de corrección**: si el test corre > 2 segundos, probablemente hay N+1.

---

### [F-66] Cheatsheet de lookups

@tipo: tabla

# Lookups ORM que aparecen en el TP-4

| Lookup | SQL equivalente | Ejemplo |
|--------|-----------------|---------|
| `__exact` | `= valor` | `filter(nombre__exact="Ursula")` |
| `__iexact` | `= valor` (case-insensitive) | `filter(email__iexact=...)` |
| `__contains` | `LIKE %valor%` | `filter(titulo__contains="desp")` |
| `__icontains` | idem, case-insensitive | `filter(titulo__icontains="SAPI")` |
| `__gt / __gte / __lt / __lte` | `> >= < <=` | `filter(cantidad_total__gt=0)` |
| `__in` | `IN (...)` | `filter(id__in=[1, 2, 3])` |
| `__isnull=True/False` | `IS NULL / IS NOT NULL` | `filter(fecha_devolucion__isnull=True)` |
| `__date / __year / __month` | Extraer fecha | `filter(fecha_prestamo__year=2026)` |

---

### [F-67] Flujo de trabajo para el TP-4

@tipo: concepto-abstracto
@imagen: content
@prompt-imagen: Diagrama horizontal tipo pipeline, cinco rectángulos bordo pequeños alineados horizontalmente conectados por flechas grises cortas. Debajo, una flecha gris larga que vuelve del último al primero formando un bucle. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Flujo recomendado para resolver el TP-4

## Iteración por modelo

1. Escribir modelo en `models.py`
2. `makemigrations` + `migrate`
3. `python manage.py test catalogo.tests.test_models -v 2`
4. Ver tests rojos → corregir
5. Cuando todos verdes → commit

## Iteración por query

1. Escribir query en `queries.py`
2. Probar en shell (`python manage.py shell`)
3. `python manage.py test catalogo.tests.test_queries -v 2`
4. Corregir → commit

> **Meta**: ≥ 8 commits significativos, autograder verde en GitHub Actions.

---

### [F-68] Checklist final del TP-4

@tipo: tabla

# Checklist — antes del push final

| # | Item | ✅ |
|---|------|---|
| 1 | `models.py` sin `pass` en ninguna clase | |
| 2 | `queries.py` sin `raise NotImplementedError` | |
| 3 | `python manage.py migrate` corre sin errores | |
| 4 | `python manage.py test` → 100% verde local |  |
| 5 | GitHub Actions verde en el PR |  |
| 6 | README leído → todos los items cumplidos |  |
| 7 | Sin código comentado viejo |  |
| 8 | `__str__` en todos los modelos |  |
| 9 | Uso de `related_name` explícito |  |
| 10 | Solo CBVs (no hay `def vista_...`) |  |

> Si los 10 están ✅ → push a main → autograder → nota.

---

### [F-69] Ejercicio final conjunto — escribir Query 2 desde cero

@tipo: socratica

# Ejercicio final — 10 min en pizarra

> **Objetivo**: cada alumno, sin mirar filminas, escribe `autores_con_mas_de_n_libros(n)`.

## Entrega en papel

1. `from django.db.models import ___`
2. `def autores_con_mas_de_n_libros(n: int):`
3. `    return Autor.objects.___`

## Docente recoge, lee en voz alta los errores más comunes

- "Te olvidaste el import de Count"
- "annotate va antes de filter"
- "usar `cantidad_libros__gt=n`, no `> n`"

---

### [F-70] Ticket de salida — Clase 3

@tipo: socratica

# Ticket de salida (5 min)

## Responder en hoja:

1. Diferencia entre `null=True` y `blank=True`
2. ¿Qué hace `annotate` en un QuerySet?
3. ¿Por qué `libros_sin_disponibilidad` usa `F("cantidad_total")` y no `cantidad_total`?
4. Una línea: qué vas a hacer **esta noche** antes del próximo commit.

> Se entrega al salir. Los resultados moldean la clase de consulta del martes.

---

### [F-71] Camino Tema 04

@tipo: concepto-abstracto

# Preview Tema 04

## Lo que viene después del TP-4

- **Select_related / prefetch_related** — optimizar joins (evitar N+1)
- **Agregaciones avanzadas** — `aggregate`, `Avg`, `Sum`, `StdDev`
- **Transacciones** — `with transaction.atomic():`
- **Señales** — pre_save, post_save (con cuidado)
- **Custom Managers** — encapsular queries comunes

> El Tema 03 les da las herramientas básicas. El Tema 04 las afila.

---

### [F-72] Preparación para Tema 05 — Forms + Views

@tipo: concepto-abstracto

# Hacia Tema 05 — de ORM a Web completa

## Ahora saben

- Escribir modelos
- Escribir queries complejas
- Testear ambos

## Les falta

- **Mostrarlos en HTML** → templates con `{% for %}`, `{% if %}`
- **Crear/editar vía formulario** → `ModelForm` + `CreateView` / `UpdateView`
- **Login / permisos** → `LoginRequiredMixin`

> Todo eso con CBVs. Empezamos Tema 05 después de entregar el TP-4.

---

### [F-73] Cierre del Tema 03

@tipo: cierre
@imagen: background
@prompt-imagen: Composición flat design con cuatro rectángulos bordo formando un cuadrado equilibrado en el centro, conectados por líneas grises diagonales cruzadas. En el centro, un pequeño círculo gris. Fondo blanco. Sin texto, sin letras, sin etiquetas, sin código, sin números. Alta resolución.

# Tema 03 cerrado

## Recorrimos

- 3 capas web → cliente/servidor → MVC / MVT
- Django instalado, proyecto + app + CBV
- Modelos, relaciones, migraciones
- CRUD + las 4 queries del TP-4

## Próximo paso: ustedes

- Clonar TP-4 de GitHub Classroom
- Resolver, commitear, pushear
- **Consultas**: próximo martes de 14 a 16 h

> "Un buen ORM te deja pensar en objetos; un gran ORM te deja pensar en dominio."

---