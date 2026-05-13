# Minuta de Clase — Tema 05: Vistas OOP, Templates y Formularios con datos ORM
## Módulo V completo | Clase Teórica | 180 min | Semana 9

> **Documento para el docente.** Cada sección corresponde a una filmina (`filminas.md`).
> El docente puede dar la clase utilizando únicamente este archivo.

---

## Metadatos de la clase

| Campo | Valor |
|-------|-------|
| Fecha estimada | Semana 9 — IF009 2026 |
| Duración total | 180 minutos |
| Dominio | BlogApp — `Post`, `Category`, `Comment` |
| Stack | Django 5.1 · Python 3.13 · Bootstrap 5.3.3 |
| Prerequisito confirmado | ORM avanzado + `View` base + DTL completo (Tema 04) |
| Estilo pedagógico | Expositivo con preguntas socráticas — CBV obligatorio, FBV prohibido |

---

## Agenda resumida

| Tiempo | Bloque | Filminas |
|--------|--------|---------|
| 0–10 min | Apertura y conexión con Tema 04 | F-00 |
| 10–30 min | **BLOQUE 1** URLconf: router de Django | F-01 a F-04 |
| 30–65 min | **BLOQUE 2** Vistas genéricas OOP | F-05 a F-10 |
| 65–95 min | **BLOQUE 3** Templates con QuerySets reales | F-11 a F-13 |
| 95–150 min | **BLOQUE 4** Formularios: ciclo de enlace y validación | F-14 a F-22 |
| 150–170 min | **BLOQUE 5** Sesiones HTTP | F-23 a F-24 |
| 170–180 min | Cierre + anticipo práctica | F-25 |

---

## APERTURA

---

### [F-00] Portada — Apertura (10 min)

**Guion**:
> "Cerramos el Tema 04 con el ORM funcionando: podemos guardar posts, filtrarlos, paginarlos. Pero hasta ahora solo lo probamos desde la shell o desde el admin. Hoy damos el paso que lo hace visible al usuario real: vistas, templates y formularios. Al final de esta clase, BlogApp va a tener una interfaz web completa con listado, detalle, creación, edición y eliminación de posts. Todo con clases. Ninguna función."

**Conexión con Tema 04**: hacer una pausa y preguntar al grupo:
- *"¿Qué hacía `Post.objects.select_related('author')` y por qué lo usábamos?"*
- *"¿Alguien recuerda qué era el problema N+1?"*

**Objetivo de apertura**: activar conocimientos previos del ORM antes de introducir las vistas genéricas.

**Transición**: *"Antes de hablar de vistas, necesitamos entender cómo una URL en el navegador llega a una clase Python. Ese es el rol del URLconf."*

---

## BLOQUE 1 — URLconf: el router de Django (20 min)

---

### [F-01] El URLconf: primer componente que Django ejecuta (5 min)

**Guion**:
> "Cuando el navegador hace `GET /blog/posts/42/`, Django no sabe todavía qué código ejecutar. Necesita traducir esa cadena de texto a una clase Python. Eso lo hace el URLconf: es básicamente una tabla de correspondencia URL → vista. No es XML, no es una anotación, es un módulo Python común. Lo que cambia es que tiene una lista llamada `urlpatterns`."

**Conceptos clave**:
- El URLconf se recorre en orden — el primer patrón que coincide se ejecuta
- Si ningún patrón coincide → `Http404` automático, la vista no se llega a ejecutar
- `include()` consume el prefijo y delega el resto

**Pregunta anticipada**: *"¿Por qué importa el orden de los patrones?"*
**Respuesta**: patrones más específicos deben ir antes que más generales (ej: `posts/crear/` antes que `posts/<int:pk>/`).

**Transición**: *"Ese URLconf tiene dos niveles. El del proyecto sabe poco — el de la aplicación sabe todo."*

---

### [F-02] Dos niveles de urls.py (5 min)

**Guion**:
> "Hay un `urls.py` en el proyecto raíz y otro en cada aplicación. El raíz solo sabe que 'todo lo que empiece con /blog/ es asunto de la app blog'. La app tiene su propio `urls.py` con el detalle. Esta separación nos da portabilidad: si queremos mover la app a otro proyecto, movemos la carpeta y una línea del URLconf raíz."

**Demostración**: mostrar el código del slide. Señalar:
- `include("blog.urls", namespace="blog")` — el namespace `"blog"` habilita `{% url 'blog:post-list' %}`
- `app_name = "blog"` en el URLconf de la app — es el otro extremo del namespace

**Error frecuente**: definir el namespace en `include()` pero olvidar `app_name` en la app → Django lanza error en runtime.

**Transición**: *"Antes de que la URL llegue a la vista, pasa por un filtro de tipo — los conversores."*

---

### [F-03] Conversores de tipo (5 min)

**Guion**:
> "Los conversores hacen algo valioso: validan la URL antes de que ejecute una sola línea de la vista. Si el patrón es `<int:pk>` y alguien escribe `/posts/abc/`, Django devuelve 404 automáticamente. El string `'abc'` nunca llega a la vista. Esto es seguridad en la frontera del sistema — exactamente donde queremos que esté."

**Mostrar la tabla**: repasar los cuatro conversores. Enfatizar:
- `<int:pk>` es el más frecuente — convierte a `int` y rechaza no-numéricos
- `<slug:slug>` permite solo caracteres seguros para URLs

**Pregunta anticipada**: *"¿Qué pasa si el objeto con ese pk no existe en la BD?"*
**Respuesta**: el conversor valida el **tipo**, no la **existencia**. `pk=42` es un int válido aunque no haya un `Post` con ese id. La existencia la verifica `get_object_or_404()` dentro de la vista.

**Transición**: *"Con el tipo validado, el valor llega a la vista en `self.kwargs`. Pero nunca usamos ese valor en strings — lo referenciamos por nombre."*

---

### [F-04] Resolución inversa (5 min)

**Guion**:
> "Escribir `/blog/posts/42/` directamente en el código es un problema de mantenimiento: si cambia la URL, hay que buscar y reemplazar en todo el proyecto. La solución es referenciar las URLs por nombre y dejar que Django genere la cadena. Esto se llama resolución inversa."

**Dos contextos**:
1. En templates: `{% url 'blog:post-detail' post.pk %}` → Django genera `/blog/posts/42/`
2. En Python: `reverse_lazy("blog:post-list")` — notar el `_lazy`

**Por qué `reverse_lazy` y no `reverse`**:
> "Los atributos de clase como `success_url` se evalúan cuando Python importa el módulo, antes de que Django haya cargado las URLs. `reverse_lazy()` difiere la evaluación al momento de uso. `reverse()` en ese contexto lanzaría error de URLs no cargadas."

**Transición**: *"Ya sabemos cómo llega la URL a la vista. Ahora vamos a ver qué hace la vista cuando la recibe."*

---

## BLOQUE 2 — El controlador View (35 min)

---

### [F-05] Django MVT vs. MVC clásico (5 min)

**Guion**:
> "Django usa el término 'Vista' para lo que MVC llama 'Controlador'. Es una decisión histórica que genera confusión. Lo importante es qué hace cada capa, no cómo se llama. La Vista de Django recibe la petición, consulta el modelo, construye el contexto, y delega la presentación al template. Es el coordinador del flujo."

**Mostrar la tabla comparativa**: MVC clásico vs. Django MVT.

**Punto de énfasis**:
> "Noten que el Template de Django hace lo que la Vista hace en MVC: solo presenta datos, no tiene lógica de negocio. El Template Language (DTL) es deliberadamente limitado — no tiene `import`, no puede ejecutar queries directas. La lógica está en la Vista."

**Transición**: *"Ahora veamos qué sucede internamente cuando una petición llega a una Vista — el ciclo completo."*

---

### [F-06] Ciclo completo de una petición HTTP (5 min)

**Guion**:
> "El diagrama muestra las seis capas que atraviesa una petición. Empezamos en el navegador y terminamos con HTML. Cada capa tiene un rol específico."

**Recorrer el diagrama capa por capa**:
- **Middleware**: *"Aquí vive el CSRF. Antes de que cualquier vista reciba la petición, el middleware verificó que el token CSRF es válido."*
- **URL Resolver**: *"Ya lo vimos — extrae pk=42 como int."*
- **dispatch()**: *"Aquí está la magia — vamos a profundizar en el siguiente slide."*
- **ORM**: *"La vista le pide datos al modelo. El template nunca ejecuta SQL."*
- **Template Engine**: *"Toma el diccionario de contexto y renderiza HTML."*

**Pregunta anticipada**: *"¿El middleware se ejecuta antes Y después de la vista?"*
**Respuesta**: sí — el middleware tiene `process_request()` (antes) y `process_response()` (después). Los estudiantes lo verán con `LoginRequiredMixin` en Módulo VI.

**Transición**: *"El paso clave del ciclo es `dispatch()` — el método que decide si ejecutar `get()` o `post()`."*

---

### [F-07] `dispatch()`: el despachador (5 min)

**Guion**:
> "Cuando subclasificamos `View` y definimos `get()` y `post()`, ¿cómo sabe Django cuál llamar? Lo hace `dispatch()`. Lee `request.method`, lo convierte a minúsculas, y llama el método correspondiente con `getattr(self, 'get')` o `getattr(self, 'post')`."

**Mostrar el código**: señalar `getattr(self, method, self.http_method_not_allowed)`.

> "Si alguien hace un `DELETE` a una vista que solo define `get()` y `post()`, `getattr` cae al tercer argumento — `http_method_not_allowed` — que devuelve un 405 Method Not Allowed automáticamente."

**Por qué importa para vistas genéricas**:
> "Cuando sobreescriben `get_queryset()` en una `ListView`, nunca tocan `dispatch()`. Esto es porque `ListView` ya implementó `get()` internamente, que a su vez llama `get_queryset()`. Están extendiendo el comportamiento en el punto correcto."

**Transición**: *"Dentro de cualquier método de la vista, disponemos de toda la información de la petición a través del objeto `request`."*

---

### [F-08] El objeto `request` (5 min)

**Guion**:
> "El objeto `request` es la instancia de `HttpRequest` que Django crea para cada petición. Está disponible en todos los métodos de la vista. Contiene absolutamente todo lo que vino del navegador."

**Recorrer los atributos del slide**:
- `request.method`: siempre en mayúsculas — `"GET"`, `"POST"`
- `request.GET`: parámetros de URL (`?page=2` → `{"page": "2"}`)
- `request.POST`: cuerpo del formulario — **solo existe en POST**
- `request.user`: el usuario autenticado — `AnonymousUser` si no está logueado
- `request.session`: el diccionario de sesión (lo veremos en Bloque 5)

**Punto importante sobre inmutabilidad**:
> "`request.POST` es inmutable — Django no permite modificarlo. Si necesitan agregar datos al formulario antes de guardarlo, lo hacen en `form.instance.campo = valor` antes de `form.save()`."

**Transición**: *"Con dispatch y request claros, veamos las vistas que usaremos en BlogApp."*

---

### [F-09] Jerarquía de vistas genéricas (5 min)

**Guion**:
> "Django incluye cinco vistas genéricas para los patrones más frecuentes de una aplicación web. No reemplazan a `View` — la extienden. Quien entiende `View` puede leer el código fuente de cualquiera de estas en GitHub y entender exactamente qué hace."

**Árbol de herencia**: señalar cada nivel.
- `View` → base absoluta, nada automático
- `ListView` / `DetailView` → ORM automático
- `CreateView` / `UpdateView` / `DeleteView` → ORM + formulario automático

**Principio pedagógico**:
> "El patrón de las vistas genéricas es siempre el mismo: heredar, declarar `model` y `template_name`, y sobreescribir el método específico que necesitan cambiar. `get_queryset()` para filtrar, `get_context_data()` para agregar variables al template, `form_valid()` para interceptar la creación exitosa."

**Transición**: *"Vamos a ver el más fundamental: ListView con un QuerySet real del ORM."*

---

### [F-10] `ListView` con `get_queryset()` (10 min)

**Guion**:
> "ListView automatiza el patrón de 'traer una lista de objetos y renderizarla'. El mínimo es declarar `model` y `template_name`. Pero en producción casi siempre sobreescribimos `get_queryset()` porque queremos filtrar, ordenar y evitar el N+1."

**Código del slide** — señalar cada línea:
- `context_object_name = "posts"`: *"Sin esto, el template tiene que usar `object_list`. Siempre definir un nombre semántico."*
- `paginate_by = 10`: *"Con esta sola línea, ListView divide el queryset en páginas. El template recibe `page_obj` con todos los métodos de navegación."*
- `select_related("author", "category")`: *"Conexión directa con Tema 04. Sin esto, cada `post.author.username` en el template dispararía una query extra — N+1."*

**Pregunta anticipada**: *"¿Qué pasa si `get_queryset()` devuelve un QuerySet vacío?"*
**Respuesta**: el template recibe `posts` como una lista vacía. Si el template tiene `{% empty %}` en el `{% for %}`, lo muestra. Si no, simplemente no itera.

---

## BLOQUE 3 — Templates con QuerySets reales (30 min)

---

### [F-11] Contexto automático (10 min)

**Guion**:
> "Las vistas genéricas pasan variables al template automáticamente. No hace falta declararlas. El problema es cuando no sabemos cuáles son y buscamos una variable que tiene otro nombre."

**Mostrar la tabla**: recorrer los cuatro casos.

**Error frecuente**:
> "El error más común es escribir `{{ posts }}` en el template de una ListView que no definió `context_object_name`. Django usó `object_list`. El template tiene `{{ object_list }}` disponible pero el estudiante busca `{{ posts }}`."

**Código de `get_context_data()`**: enfatizar `super()`.
> "Siempre llamar `super().get_context_data(**kwargs)` primero. Sin eso, las variables automáticas — `page_obj`, `form`, `object` — desaparecen del contexto."

**Transición**: *"Con el contexto claro, veamos cómo el template accede a los atributos del modelo con dot notation."*

---

### [F-12] Filtros DTL sobre datos ORM (12 min)

**Guion**:
> "El DTL resuelve el acceso a atributos de modelos con dot notation. `post.author.username` navega la relación ForeignKey automáticamente. Pero hay un costo si no tenemos cuidado."

**Recorrer el código del slide**:
- `{{ post.title|upper }}`: filtro estándar — funciona igual con strings del modelo
- `{{ post.created_at|date:"d/m/Y" }}`: el campo `DateTimeField` se formatea con el filtro `date`
- `{{ post.author.get_full_name|default:"Anónimo" }}`: llamada a método del modelo + fallback

**El problema N+1** — explicar con cuidado:
> "Cuando iteramos `{% for post in posts %}` y dentro accedemos a `post.comments.all`, Django hace una query por cada post. Si hay 100 posts, son 101 queries. La solución está en la vista, no en el template: `prefetch_related('comments')` en `get_queryset()` precarga todos los comentarios en una sola query extra."

**Pregunta anticipada**: *"¿Podemos hacer `select_related` y `prefetch_related` en la misma vista?"*
**Respuesta**: sí — `select_related` para FK/OneToOne (JOIN), `prefetch_related` para M2M y reverse FK.

**Transición**: *"Ahora veamos cómo organizar los templates con herencia."*

---

### [F-13] Herencia de templates (13 min)

**Guion**:
> "La herencia de templates resuelve la duplicación. Sin ella, cada página tendría su propio `<head>`, `<nav>`, footer. Con `{% extends %}` y `{% block %}`, el HTML estructural existe en un solo lugar — `base.html`."

**Mostrar `base.html`** — recorrer línea a línea:
- `{% block content %}{% endblock %}`: *"Este bloque es el 'espacio en blanco' que cada página hija llena."*
- `{% url 'blog:post-list' %}`: *"Resolución inversa — no hay strings hardcodeados de URL."*
- `{% if messages %}`: *"El messages framework — lo conectamos cuando hablemos de sesiones."*

**Mostrar `post_detail.html`**:
- `{% extends "blog/base.html" %}`: *"Esta línea tiene que ser la primera del archivo — antes de cualquier cosa."*
- `{% block content %}`: *"Solo definimos lo que cambia. Todo el resto viene de base.html."*

**Demo imaginaria**: *"Si ahora cambio la versión de Bootstrap en `base.html` de 5.3.3 a 5.4, ese cambio se propaga a todas las páginas automáticamente."*

---

## BLOQUE 4 — Formularios Django (55 min)

---

### [F-14] El ciclo de enlace: bound vs unbound (8 min)

**Guion**:
> "El ciclo de enlace es el concepto central de los formularios Django. Un formulario puede estar en dos estados: sin datos del usuario — unbound — o con datos del usuario — bound. Solo un formulario bound puede ser validado. Esto explica por qué en un GET construimos `PostForm()` y en un POST construimos `PostForm(data=request.POST)`."

**Mostrar la tabla del slide** — recorrer los cuatro casos.

**Pregunta anticipada**: *"¿Por qué `PostForm(instance=post)` también es unbound si tiene datos?"*
**Respuesta**: tiene datos del modelo pero no del usuario. `is_bound` indica si el formulario tiene datos que el usuario envió para validar. Los datos de la instancia son para pre-poblar el formulario en el GET — no para validar.

**Conexión PRG**: adelantar brevemente.
> "El GET construye unbound, renderiza vacío. El POST construye bound, valida. Si válido → redirect. Si inválido → render con errores. Ese ciclo de tres estados lo veremos en detalle en F-19."

**Transición**: *"Cuando el formulario está bound y llamamos `is_valid()`, Django ejecuta un pipeline de cinco capas."*

---

### [F-15] Pipeline de validación — las 5 capas (10 min)

**Guion**:
> "Este es el diagrama más importante de la clase. `is_valid()` no es una función — es un pipeline. Ejecuta cinco capas en secuencia. Si cualquier capa falla, el proceso se detiene para ese campo."

**Recorrer cada capa lentamente**:
1. `to_python()`: *"El POST llega como strings. '42' no es el int 42. Esta capa hace la conversión. Si el tipo no se puede convertir, el campo queda inválido y las siguientes capas no se ejecutan para él."*
2. `validate()`: *"Reglas del campo: ¿es required? ¿cumple max_length? Estas vienen de la definición del campo."*
3. `run_validators()`: *"Lista personalizada de validators. No es muy frecuente pero existe."*
4. `clean_<campo>()`: *"La nuestra — accede al ORM, puede transformar el valor, lanza `ValidationError`."*
5. `clean()`: *"Ve todos los campos simultáneamente — para reglas que cruzan campos."*

**Punto crítico sobre `cleaned_data`**:
> "`cleaned_data` solo existe DESPUÉS de llamar a `is_valid()`. Si lo acceden antes — `AttributeError`. Si un campo falló en la capa 4, no está en `cleaned_data`."

**Transición**: *"El punto de entrada a todo esto es `ModelForm`. Vamos a verlo."*

---

### [F-16] `ModelForm`: generación automática de campos (8 min)

**Guion**:
> "ModelForm inspecciona el modelo y genera los campos del formulario automáticamente. No hay que declarar `title = forms.CharField(max_length=200)` porque ya está en el modelo. Si cambia el modelo, el formulario se actualiza solo."

**Recorrer el código del slide**:
- `fields = [...]`: *"Lista explícita de qué campos exponer. Nunca usar `fields = '__all__'` en producción — expone campos internos como `author`, `created_at`."*
- `widgets = {...}`: *"Aquí conectamos las clases de Bootstrap. No en el template."*
- `labels` y `error_messages`: *"Personalización sin tocar el template."*

**Mostrar la tabla de correspondencias**: señalar que `DateTimeField(auto_now_add=True)` se excluye automáticamente.

**Pregunta anticipada**: *"¿Podemos tener un campo de formulario que no existe en el modelo?"*
**Respuesta**: sí — se declara explícitamente en el `ModelForm` fuera de `Meta`. Útil para campos de confirmación (ej: confirmar email, confirmar contraseña).

**Transición**: *"Una vez que tenemos el ModelForm, podemos agregar validación personalizada — la Capa 4."*

---

### [F-17] Capa 4: `clean_<campo>()` (7 min)

**Guion**:
> "La Capa 4 es donde ponemos nuestra lógica. El método se llama `clean_` más el nombre del campo. Recibe `self.cleaned_data['campo']` ya convertido al tipo correcto. Puede consultar la BD. Debe retornar el valor."

**Recorrer el código**:
- `.strip()`: *"Es una buena práctica de higiene — siempre limpiar espacios."*
- `if self.instance.pk`: *"Este patrón es crítico para UpdateView. Sin él, el post existente se marca como duplicado de sí mismo."*
- `return title`: *"Enfatizar: OBLIGATORIO. Sin return, `cleaned_data['title']` es `None`. El error es silencioso — el formulario es válido pero el campo queda vacío en la BD."*

**Pregunta anticipada**: *"¿Puedo acceder a otros campos en `clean_title()`?"*
**Respuesta**: técnicamente sí con `self.cleaned_data.get('otro_campo')`, pero solo si ese campo ya pasó sus capas 1-3. Para validación cruzada real, usar `clean()`.

**Transición**: *"Para reglas que involucran múltiples campos simultáneamente, existe la Capa 5."*

---

### [F-18] Capa 5: `clean()` — validación cruzada (7 min)

**Guion**:
> "`clean()` ve el estado de todos los campos después de que pasaron sus capas 1-4. Es el lugar correcto para reglas del tipo 'si publicado entonces el cuerpo debe tener mínimo 100 caracteres'."

**El error más frecuente**:
> "En `clean()` nunca acceder a `cleaned_data['campo']` con corchetes. Si ese campo falló en su capa 4, la clave no existe — `KeyError`. Siempre usar `.get('campo', valor_default)`."

**`self.add_error()` vs `raise ValidationError`**:
- `self.add_error('body', '...')` → el error aparece junto al campo `body` en el template
- `raise ValidationError('...')` → el error va a `form.non_field_errors()` → se muestra en la sección de alertas general

**Transición**: *"Ya entendemos cómo funciona la validación. Ahora veamos el ciclo completo de una petición de creación."*

---

### [F-19] Ciclo completo GET → POST → Redirect (5 min)

**Guion**:
> "El ciclo tiene tres estados: GET inicial, POST inválido, POST válido. CreateView gestiona los tres con el mismo método — no hay que escribir lógica de control."

**Mostrar la tabla del slide** — enfatizar la columna HTTP:
> "El POST inválido devuelve 200 con el formulario y sus errores. El POST válido devuelve 302. Esta diferencia es el patrón PRG."

**Por qué PRG**:
> "Si tras un POST exitoso renderizamos directamente, el usuario puede recargar la página con F5 — el navegador reenvía el formulario — inserción duplicada en la BD. El redirect convierte el POST en un GET idempotente. El botón 'recargar' ya no tiene efecto destructivo."

**Transición**: *"Para editar un objeto existente, usamos UpdateView — mismo formulario, diferente constructor."*

---

### [F-20] `UpdateView` con `instance=` (5 min)

**Guion**:
> "La única diferencia entre crear y editar es el parámetro `instance=` en el constructor del formulario. Con él, `form.save()` emite `UPDATE`. Sin él, siempre emite `INSERT` — el error más frecuente al implementar la edición."

**Mostrar el código**:
> "Noten que `template_name = 'blog/post_form.html'` es el mismo que CreateView. El template no sabe si está creando o editando — recibe el mismo objeto `form`. Esto es reutilización de código."

**Punto sobre pre-población**:
> "UpdateView recupera el objeto del ORM, lo asigna a `self.object`, y construye `PostForm(instance=self.object)`. Django inicializa cada widget con el valor actual del atributo — sin código adicional."

**Transición**: *"El template del formulario tiene que manejar tanto la creación como la edición — y mostrar los errores cuando los haya."*

---

### [F-21] Template del formulario (5 min)

**Guion**:
> "El template del formulario itera `{% for field in form %}` — obtiene todos los campos, con su label, su widget renderizado y sus errores. No hay que hardcodear cada campo."

**Señalar `novalidate`**:
> "Sin este atributo, el navegador valida los campos con HTML5 y puede bloquear el POST antes de que Django lo procese. Con `novalidate`, Django tiene control total — mensajes en español, lógica de negocio real."

**`{% csrf_token %}`**: *"Obligatorio en todos los formularios POST. El middleware `CsrfViewMiddleware` rechaza el POST si no está presente. Django lo verifica antes de llegar a la vista."*

**`form.non_field_errors`**: *"Son los errores generados por el método `clean()` que no están asociados a ningún campo específico. Mostrarlos en una alerta general al tope del formulario."*

**Transición**: *"La última operación del CRUD es la eliminación — que requiere su propia confirmación."*

---

### [F-22] `DeleteView`: GET confirma, POST elimina (5 min)

**Guion**:
> "Un enlace `<a href='/posts/42/eliminar/'>` genera un GET. Si ese GET borrara el objeto, cualquier crawler o usuario que siga el link accidentalmente perdería datos. La eliminación requiere un POST explícito."

**Mecánica de DeleteView**:
> "El GET siempre muestra el template de confirmación — nunca borra. Solo el POST ejecuta `objeto.delete()`. Django implementa esto internamente — no hay que escribirlo."

**`{% csrf_token %}` en el formulario de confirmación**: *"Igual que en cualquier formulario POST."*

**Pregunta anticipada**: *"¿Podemos hacer la eliminación sin template de confirmación?"*
**Respuesta**: técnicamente sí, sobreescribiendo `delete()` en la vista. Pero es una mala práctica — siempre dar al usuario la oportunidad de cancelar.

---

## BLOQUE 5 — Sesiones HTTP (20 min)

---

### [F-23] HTTP es stateless (10 min)

**Guion**:
> "HTTP es un protocolo sin estado por diseño. Cada petición al servidor es completamente anónima — el servidor no sabe si la petición anterior vino del mismo navegador. Esto es intencional: hace la web escalable, cualquier servidor puede responder cualquier petición."

**Problema y solución**:
> "Pero las aplicaciones necesitan recordar cosas: ¿está logueado el usuario?, ¿qué guardó en el carrito? La solución de Django son las sesiones."

**Mecánica de tres pasos** — recorrer el slide:
1. Django genera un UUID de sesión y lo envía como cookie
2. El navegador envía esa cookie en cada petición siguiente
3. Django lee la cookie, busca los datos en la BD y los expone como `request.session`

**Señalar**: *"La cookie solo contiene el identificador de sesión — un UUID. Los datos reales están en el servidor. Esto es más seguro que cookies con datos completos."*

**Transición**: *"Vemos cómo usar `request.session` y el messages framework."*

---

### [F-24] `request.session` y messages framework (10 min)

**Guion**:
> "`request.session` es un diccionario Python estándar. Se lee y escribe como cualquier dict. Los datos persisten entre peticiones del mismo usuario."

**Recorrer el código — dos niveles**:
1. Nivel bajo: `request.session["key"] = value` y `.get("key")`
2. Nivel alto: messages framework

**Conexión con PRG**:
> "El messages framework es la solución perfecta para el patrón PRG: en `form_valid()` guardamos el mensaje de éxito, hacemos el redirect, y en la siguiente página el template lo muestra. La cookie transporta el mensaje a través del redirect de forma invisible."

**Tipos de mensajes**: `messages.success`, `messages.error`, `messages.warning`, `messages.info`.

**Alcance**: *"Autenticación completa — `request.user`, `LoginRequiredMixin`, `logout()` — es el Módulo VI. Hoy solo el mecanismo de base."*

---

## CIERRE

---

### [F-25] Síntesis del Módulo V (10 min)

**Guion**:
> "Cubrimos cinco bloques que juntos forman el ciclo completo: una URL llega, Django la rutea, una vista la procesa con datos del ORM, un formulario valida los datos del usuario, el template los presenta, y la sesión preserva el estado entre peticiones."

**Recorrer los contenidos abordados** — rápido repaso.

**El hilo conductor** — escribir en el pizarrón si es posible:
```
URL → URLconf → dispatch() → ORM → Form → Template → Redirect
```

**Anticipo de la práctica**:
> "En la clase práctica van a implementar el CRUD completo de BlogApp: Lista, Detalle, Crear, Editar, Eliminar. Todo con vistas genéricas basadas en clases. Las vistas que vimos hoy son exactamente las que van a usar."

**Preguntas de cierre** — hacer al menos dos:
- *"¿Cuándo `form.is_valid()` retorna `False` sin ejecutar validación alguna?"*
- *"¿Por qué `form.save()` a veces hace INSERT y a veces UPDATE?"*
- *"¿Qué problema resuelve el patrón PRG?"*

---

## Errores frecuentes anticipados

| Error | Causa | Corrección |
|-------|-------|-----------|
| `{% url 'post-list' %}` no funciona | Falta el namespace `blog:` | Usar `{% url 'blog:post-list' %}` |
| Template recibe `object_list` en lugar de `posts` | No definió `context_object_name` | Agregar `context_object_name = "posts"` |
| Contexto pierde `page_obj` y `form` | Olvidó `super()` en `get_context_data()` | Siempre llamar `super()` primero |
| N+1 queries en ListView | `post.comments.all` sin `prefetch_related` | Agregar `prefetch_related('comments')` en `get_queryset()` |
| `AttributeError: 'PostForm' has no attribute 'cleaned_data'` | Accedió a `cleaned_data` antes de `is_valid()` | Acceder solo después de `form.is_valid()` |
| `form.save()` crea un nuevo objeto en UpdateView | No pasó `instance=` al constructor | `PostForm(data=request.POST, instance=self.object)` |
| `reverse_lazy` no necesaria → lanza error en import | Usó `reverse()` en atributo de clase | Cambiar a `reverse_lazy()` |
| Form valida `None` en `clean_title()` | Olvidó `return title` al final | Siempre retornar el valor en `clean_<campo>()` |
| `KeyError` en `clean()` | Accedió con `['campo']` en lugar de `.get()` | Siempre `.get('campo', default)` en `clean()` |
| Formulario no muestra errores | Faltó `{% for error in field.errors %}` en el template | Agregar el loop de errores por campo |
