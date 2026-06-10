# Tema 07 — Accesos, usuarios y tienda de ropa con variantes
## Tutorial guiado e-commerce — Clase 1

> **Fecha**: 2026-06-10  
> **Estado**: APPROVED — aprobado por pedido docente de producción de clase el 2026-06-10  
> **Duración**: flexible — el tópico continúa en la próxima clase si es necesario  
> **Modalidad**: tutorial guiado con live coding del profesor  
> **Plan de referencia**: `salida/cursadas/2026/plan-actualizado.md` §5  
> **Material local específico**: no disponible  
> **Fuentes técnicas**: documentación Django auth/admin, documentación Jazzmin, repositorio ThemeWagon MiniStore

---

## 1. Propósito del tópico

El profesor construye en vivo el primer incremento funcional de una tienda de ropa.
La clase muestra cómo una aplicación Django separa responsabilidades, usuarios,
interfaces y permisos sin intentar completar todavía el proceso de compra.

La web debe percibirse como una tienda realista y coherente, no como una colección de
ejemplos aislados. Ese realismo se consigue utilizando las tecnologías enseñadas durante
la cursada: Django Templates como base de la interfaz, vistas orientadas a objetos, ORM,
formularios, sesiones, autenticación y Django Admin. No se incorporan tecnologías que
oculten el funcionamiento del framework.

El testing forma parte de la construcción. Cada decisión central se acompaña con una
prueba automatizada breve que el profesor ejecuta durante el live coding. La clase muestra
el ciclo test que falla → implementación → test que pasa, sin relegar las pruebas al cierre.

Al terminar la demostración existe una **Tienda v0.1**, primera versión funcional,
navegable y poblada con productos:

```text
cliente inicia sesión y accede a Mi cuenta
→ administrador crea un operador y asigna permisos
→ operador ingresa al mismo admin Jazzmin con acceso limitado
→ operador carga prendas, imágenes y variantes por talle/color
→ visitante navega MiniStore adaptado con datos reales del ORM
```

La clase no es una práctica. El profesor escribe, explica y verifica todo el código.
Los estudiantes participan mediante predicciones, lectura de errores y preguntas de
control.

### Producto final de la clase: Tienda v0.1

La primera versión debe poder ejecutarse y recorrerse como un producto coherente:

| Superficie | Resultado final |
|------------|-----------------|
| Storefront | Home MiniStore adaptada, catálogo y detalle de productos |
| Productos | Prendas reales cargadas con imágenes y variantes de talle/color |
| Cliente | Login, logout y página Mi cuenta |
| Operador | Acceso al admin Jazzmin y gestión del catálogo |
| Administrador | Gestión de usuarios, grupos y permisos |
| Seguridad | Diferencias de acceso verificadas por permisos |
| Calidad | Batería mínima de tests en verde |

El tópico no cierra mostrando archivos aislados. Cuando se completa, se recorre la Tienda
v0.1 de punta a punta con productos visibles y utilizando los tres perfiles. Si no se llega
a ese estado en una sesión, se guarda el checkpoint alcanzado y se continúa en la próxima
clase.

---

## 2. Decisión de alcance

Este tópico concentra autenticación, autorización, admin, persistencia y templates porque
los presenta dentro de una única feature vertical observable. Se parte de un repositorio
inicial preparado para concentrar la clase en decisiones relevantes. La secuencia avanza
por checkpoints funcionales y puede continuar en la clase siguiente.

### Repositorio inicial obligatorio

Antes de comenzar, el repositorio debe contener:

- proyecto Django creado y servidor de desarrollo verificable;
- `requirements.txt` con dependencias fijadas para instalar frente al curso;
- una versión de `django-jazzmin` compatible y probada con la versión de Django elegida;
- `pytest.ini` preparado; `pytest` y `pytest-django` se instalan durante la clase;
- MiniStore descargado con su licencia y assets disponibles;
- configuración básica de templates, static y media;
- base de datos descartable sin migraciones propias ejecutadas;
- commits de recuperación para cada bloque de live coding.

Las apps `accounts` y `products` no deben existir: su creación es parte central de la clase.

### Fuera de alcance inmediato

Eso está fuera de scope del Tema 07:

- registro público de clientes;
- recuperación o cambio de contraseña;
- checkout, creación de órdenes y aprobación;
- pagos y envíos;
- APIs, AJAX o actualización dinámica de variantes;
- dos instancias diferentes de `AdminSite`;
- despliegue, WhiteNoise, almacenamiento cloud y `collectstatic`;
- edición completa del theme o diseño visual desde cero;
- cobertura porcentual obligatoria y batería exhaustiva de casos;
- SPA, React, Vue, frontend desacoplado o API REST para renderizar la tienda;
- lógica comercial crítica implementada solamente en JavaScript;

---

## 3. Cobertura del plan mínimo

| Contenido obligatorio | Tratamiento en este tópico |
|-----------------------|-----------------------------|
| Persistencia en Django | Modelos `User`, `Category`, `Product`, `ProductVariant`, `ProductImage` |
| Mapeo de entidades y relaciones | FK producto-categoría, variante-producto e imagen-producto |
| CRUD con Django | Carga y edición desde Django Admin |
| Consultas dinámicas | Productos activos, variantes activas y disponibilidad |
| Templates Django | Herencia, includes, `{% static %}`, loops y URLs |
| Modelado de interfaz con Django y HTML5 | Adaptación de MiniStore a datos reales |
| Manejo de autenticación | Login/logout del cliente y login del admin |
| Grupos y permisos | Grupo `Operadores` y permisos de modelos |
| Permisos por defecto y personalizados | `view/add/change` + `publish_product` |
| Verificación de permisos en templates | Navegación según autenticación |
| App de administración Django | Gestión interna de usuarios y catálogo |
| Personalización de `ModelAdmin` | Listados, filtros, búsqueda, fieldsets e inlines |
| Control de acceso en admin | Operador sin usuarios, grupos, permisos ni borrado |
| Personalización del sitio admin | Jazzmin como skin del único `/admin/` |

---

## 4. Objetivos de aprendizaje

| # | Bloom | Objetivo observable |
|---|-------|---------------------|
| 1 | Comprender | Explicar por qué el proyecto separa `accounts` y `products` en apps distintas |
| 2 | Aplicar | Crear una app Django, registrarla y completar su ciclo modelo-migración-admin-URL-template |
| 3 | Aplicar | Configurar un usuario extendido desde `AbstractUser` antes de la primera migración |
| 4 | Analizar | Distinguir autenticación, `is_staff`, grupos, permisos y superusuario |
| 5 | Aplicar | Configurar el grupo `Operadores` con permisos comerciales limitados |
| 6 | Analizar | Explicar por qué Jazzmin cambia la presentación pero no concede autorización |
| 7 | Construir | Modelar una prenda separando `Product` de la unidad vendible `ProductVariant` |
| 8 | Aplicar | Personalizar Django Admin con filtros, búsqueda e inlines para cargar catálogo |
| 9 | Aplicar | Transformar secciones estáticas de MiniStore en templates alimentados por ORM |
| 10 | Evaluar | Verificar por URL directa que el operador no puede gestionar usuarios ni permisos |
| 11 | Construir | Componer una experiencia de tienda realista mediante templates, vistas y datos coherentes |
| 12 | Aplicar | Escribir y ejecutar tests de modelos, permisos y vistas como parte de cada incremento |
| 13 | Analizar | Interpretar un fallo de test y relacionarlo con una regla de dominio o autorización |

---

## 5. Arquitectura enseñada

### Apps creadas en clase

| App | Propiedad funcional | No debe contener |
|-----|--------------------|-----------------|
| `accounts` | Identidad, perfil, login/logout y administración de usuarios | Catálogo, órdenes o lógica comercial |
| `products` | Categorías, prendas, variantes, imágenes, stock y storefront | Usuarios, carrito, pagos o envíos |
| `orders` — opcional | Carrito temporal y carrito persistente del cliente | Checkout, órdenes confirmadas, pagos o envíos |

### Continuidad futura

```text
accounts
   ↑ settings.AUTH_USER_MODEL
products ← orders ← operations
           opcional   Clase 3
           al cierre
```

La clase cierra primero `accounts` y `products` en `C07-v01`. Después puede iniciar
`orders` únicamente con carrito; la creación y aprobación de órdenes permanece en el
siguiente incremento.

### Estructura mínima esperada

```text
accounts/
  admin.py
  models.py
  urls.py
  views.py
  templates/accounts/

products/
  admin.py
  models.py
  urls.py
  views.py
  templates/products/

templates/
  store/base.html
  store/includes/

static/store/
  css/
  js/
  images/
```

---

## 6. Modelo de dominio

### Usuarios

`accounts.User` extiende `AbstractUser` antes de la primera migración y representa la
identidad común: autenticación, estado staff, grupos y permisos. Los datos exclusivos de
la experiencia de compra viven en `accounts.CustomerProfile`, asociado uno a uno solamente
cuando el usuario actúa como cliente.

| Tipo | Configuración | Acceso |
|------|---------------|--------|
| Cliente | activo, `is_staff=False` | MiniStore + Mi cuenta |
| Operador | activo, `is_staff=True`, grupo `Operadores` | mismo `/admin/`, modelos comerciales autorizados |
| Administrador | superusuario | acceso completo |

Los roles no se duplican en un campo `role`. Se expresan mediante `is_staff`, grupos y
permisos. Operador y administrador no poseen `CustomerProfile`; teléfono y dirección no
aparecen en `UserAdmin`.

### Catálogo

| Modelo | Responsabilidad | Invariantes |
|--------|-----------------|-------------|
| `Category` | Agrupar prendas | nombre y slug únicos |
| `Product` | Información común de una prenda | no almacena talle, color ni stock |
| `ProductVariant` | Unidad vendible | SKU único; producto+talle+color único; stock no negativo |
| `ProductImage` | Imágenes de producto | texto alternativo obligatorio; una principal por convención |

`ProductVariant` posee talle, color, SKU, precio, stock y estado activo. La tienda muestra
un producto, pero la compra futura operará siempre sobre una variante.

---

## 7. Autorización y admin

### Matriz de permisos

| Recurso | Cliente | Operador | Administrador |
|---------|---------|----------|---------------|
| `accounts.User` | sin permisos de modelo | ninguno | todos |
| `accounts.CustomerProfile` | sin permisos de modelo; usa vistas propias | ninguno; fuera del admin | fuera del admin |
| `auth.Group` / permisos | ninguno | ninguno | todos |
| `products.Category` | ninguno | `view`, `add`, `change` | todos |
| `products.Product` | ninguno | `view`, `add`, `change`, `publish_product` | todos |
| `products.ProductVariant` | ninguno | `view`, `add`, `change` | todos |
| `products.ProductImage` | ninguno | `view`, `add`, `change` | todos |

El operador no recibe permisos `delete`. La desactivación reemplaza el borrado físico.

### Contrato Jazzmin

- Existe un único `/admin/` para operador y administrador.
- Jazzmin personaliza branding, orden, íconos y organización visual.
- Django decide qué modelos y acciones ve cada usuario según permisos.
- No se usa `hide_models` para separar operador y administrador porque es global.
- No se incluye `accounts.User` en la búsqueda global destinada al operador.
- Ocultar un enlace nunca reemplaza una comprobación de permisos.

### Personalizaciones `ModelAdmin`

| Admin | Configuración mostrada |
|-------|------------------------|
| `UserAdmin` | identidad, estado staff, grupos y permisos; sin datos comerciales |
| `ProductAdmin` | `list_display`, `list_filter`, `search_fields`, acción publicar |
| `ProductVariantInline` | carga de talle, color, SKU, precio y stock |
| `ProductImageInline` | carga de imágenes y texto alternativo |

---

## 8. Testing integrado

El proyecto utiliza `pytest` y `pytest-django`, en continuidad con el enfoque de testing
de la cursada. Los tests viven dentro de la app propietaria de la regla:

```text
accounts/tests/
  test_auth.py
  test_admin_permissions.py

products/tests/
  test_models.py
  test_views.py
```

### Estrategia durante el live coding

| Feature | Test escrito o ejecutado antes de avanzar |
|---------|--------------------------------------------|
| Usuario cliente | cliente autenticado accede a Mi cuenta |
| Separación de perfiles | operador y administrador no poseen ni abren `CustomerProfile` |
| Acceso al admin | cliente recibe acceso denegado; operador puede ingresar |
| Permisos operador | operador no puede abrir usuarios/grupos por URL directa |
| Variante vendible | SKU y producto+talle+color no pueden repetirse |
| Stock | una variante no acepta stock negativo |
| Catálogo público | solo muestra productos activos con variantes activas |
| Estados visuales | producto sin imagen usa fallback; variante sin stock aparece no disponible |

El profesor escribe en vivo cuatro tests representativos:

1. cliente sin acceso al admin;
2. operador sin acceso a usuarios;
3. variante rechaza una combinación duplicada;
4. catálogo público excluye productos inactivos.

Los demás tests de la batería están preparados en commits posteriores y se leen,
explican y ejecutan durante la clase. Esto mantiene visible la estrategia de testing sin
repetir fixtures equivalentes.

### Tipos de prueba incluidos

- **Modelo**: constraints e invariantes de `ProductVariant`.
- **Autenticación**: login y acceso a Mi cuenta.
- **Autorización**: diferencias entre cliente, operador y administrador.
- **Vista**: status code, template utilizado y contenido del catálogo.
- **Template**: presencia de estados vacíos, fallback y disponibilidad.

### Regla pedagógica

No se explica nuevamente todo pytest desde cero. El profesor recupera el ciclo
Red-Green-Refactor ya visto y se concentra en qué comportamiento de Django necesita
protección. Cada test debe tener una intención observable y un nombre que exprese la regla.

---

## 9. Adaptación de MiniStore

MiniStore aporta una landing e-commerce Bootstrap 5 con banners, cards, navegación,
búsqueda y enlaces placeholder. No aporta lógica Django ni páginas funcionales completas.

### Principio de implementación

La interfaz se construye mediante **server-side rendering**. Cada pantalla visible parte
de un template Django que recibe contexto desde una CBV y consulta datos mediante el ORM.
MiniStore define la presentación base; Django controla navegación, contenido, estado,
autenticación y reglas.

```text
URL Django → CBV → QuerySet/contexto → Django Template → HTML MiniStore adaptado
```

JavaScript se limita al comportamiento visual que ya trae el theme y a mejoras
progresivas no esenciales. La aplicación debe seguir siendo navegable y comprensible sin
depender de una SPA ni de una API.

### Transformación demostrada

| Origen estático | Resultado Django |
|-----------------|------------------|
| rutas relativas a assets | `{% static %}` y `static/store/` |
| `index.html` monolítico | `base.html`, home e includes |
| navegación fija | `{% url %}`, login/logout y Mi cuenta |
| categorías de tecnología | categorías de indumentaria |
| cards escritas manualmente | loop de productos activos |
| imágenes demo | imagen principal o fallback |
| precio fijo | precio mínimo de variantes activas |

### Experiencia realista mínima de la Clase 1

| Pantalla / estado | Comportamiento esperado con templates |
|-------------------|----------------------------------------|
| Home | Hero, categorías, destacados y novedades obtenidos del ORM |
| Catálogo | Grilla de productos activos, imagen, nombre, categoría y precio inicial |
| Detalle | Galería, descripción, variantes disponibles, talles, colores y stock |
| Login | Formulario Django integrado visualmente con MiniStore |
| Mi cuenta | Datos básicos del cliente y anticipación de futuras órdenes |
| Navbar | Estado de autenticación, categorías y enlaces reales con `{% url %}` |
| Sin resultados | Estado vacío coherente, no una pantalla rota |
| Producto sin imagen | Fallback visual estable |
| Variante sin stock | Se muestra no disponible y no como opción comprable |

El selector de talle/color y el carrito pueden resolverse con formularios HTML, sesiones,
modelos y renderizado del servidor. No requieren JavaScript complejo para considerarse
realistas.

### Datos de demostración

La carga debe representar una tienda creíble:

- al menos tres categorías de indumentaria;
- al menos seis prendas con textos e imágenes coherentes;
- múltiples variantes por producto;
- combinaciones con y sin stock;
- productos destacados, novedades e inactivos para demostrar consultas;
- usuarios separados para cliente, operador y administrador.

Los datos pueden estar preparados parcialmente para evitar trabajo mecánico, pero el
profesor debe cargar al menos un producto completo con variantes e imagen frente al curso.

### Arquitectura de templates

```text
templates/
  store/
    base.html
    includes/
      navbar.html
      footer.html
      messages.html
      product_card.html

accounts/templates/accounts/
  login.html
  profile.html

products/templates/products/
  home.html
  product_list.html
  product_detail.html
```

`base.html`, los includes estructurales y los assets de MiniStore pueden estar preparados
antes de la clase. El profesor demuestra en vivo las transformaciones pedagógicamente
relevantes:

1. reemplazar enlaces y assets fijos por `{% url %}` y `{% static %}`;
2. convertir cards estáticas en `product_card.html`;
3. alimentar home, catálogo y detalle desde CBV y QuerySets;
4. integrar login y Mi cuenta mediante herencia de templates;
5. representar estados vacíos, imágenes faltantes y variantes sin stock.

---

## 10. Secuencia docente por checkpoints

| Checkpoint | Bloque | Estado consistente para continuar |
|------------|--------|-----------------------------------|
| `C00-starter` | Demo del incremento, entorno y mapa de arquitectura | Starter verificado |
| `C01-environment` | Crear/activar `.venv`, instalar dependencias y verificar starter | Entorno aislado, check y test starter en verde |
| `C02-accounts` | Crear `accounts`, `User`, login y Mi cuenta | Tests de autenticación en verde |
| `C03-permissions` | Crear grupo `Operadores`, permisos, Jazzmin y `UserAdmin` | Roles diferenciados por permisos |
| `C04-products` | Crear `products`, modelos y tests de invariantes | Tests protegen SKU, combinación y stock |
| `C05-admin-data` | Configurar admin e inlines; cargar datos | Operador carga prendas, imágenes y variantes |
| `C06-storefront` | Adaptar MiniStore, CBV y tests de catálogo | Storefront conectado al ORM |
| `C07-v01` | Ejecutar batería y recorrido final | Tienda v0.1 completa |
| `C08-session-cart` — opcional | Implementar carrito público temporal | Sesión y tests del visitante en verde |
| `C09-persistent-cart` — opcional | Persistir carrito del cliente y migrar al login | Tienda v0.2 y tests integrados en verde |

### Regla de continuidad

- No se calculan tiempos por bloque ni por filmina.
- No se saltea contenido para terminar en una única sesión.
- Cada clase termina en el último checkpoint consistente alcanzado.
- Antes de cerrar la sesión se ejecutan los tests correspondientes al checkpoint.
- La próxima clase comienza recuperando el estado y recordando brevemente lo construido.
- Testing, permisos y recorrido final no se recortan.

No se recortan los estados de interfaz esenciales: catálogo vacío, producto sin imagen y
variante sin stock. Son parte del realismo funcional y muestran cómo los templates
representan situaciones reales del dominio.

---

## 11. Guion de participación guiada

| Momento | Pregunta de control |
|---------|---------------------|
| Antes de `AUTH_USER_MODEL` | ¿Qué ocurre si extendemos User después de migrar? |
| Antes de asignar permisos | ¿`is_staff=True` permite editar productos automáticamente? |
| Al entrar como operador | ¿Por qué no aparece Usuarios si Jazzmin es el mismo? |
| Antes de `ProductVariant` | ¿Dónde debería vivir el stock de una remera talle M color negro? |
| Antes del inline | ¿Qué relación permite editar variantes dentro del producto? |
| Al adaptar cards | ¿Qué parte pertenece al theme y qué parte pertenece a Django? |
| En verificación final | ¿Ocultar el enlace alcanza para impedir acceso por URL directa? |
| Ante un test rojo | ¿Qué regla del sistema está indicando que todavía no cumplimos? |

---

## 12. Verificaciones obligatorias

| Caso | Resultado esperado |
|------|--------------------|
| Cliente accede a `/admin/` | acceso denegado |
| Operador accede a `/admin/` | acceso permitido |
| Operador abre usuarios o grupos por URL directa | acceso denegado |
| Operador intenta borrar producto | acción no disponible |
| Administrador gestiona usuarios y grupos | acceso completo |
| Operador crea producto con variantes e imágenes | guardado correcto |
| Variante repite SKU o producto+talle+color | validación rechaza duplicado |
| Storefront consulta catálogo | solo productos y variantes activas |
| Navbar cambia según autenticación | login o Mi cuenta/logout visibles correctamente |
| Catálogo no posee resultados | template muestra un estado vacío útil |
| Producto no posee imagen | template utiliza fallback |
| Variante no posee stock | template la presenta como no disponible |

### Batería mínima obligatoria

1. cliente sin acceso al admin;
2. operador sin acceso a Mi cuenta ni perfil cliente;
3. operador sin permisos sobre usuarios;
4. unicidad de variante;
5. catálogo público excluye productos inactivos.
6. variante rechaza SKU duplicado;
7. variante rechaza combinación producto+talle+color duplicada;
8. variante rechaza stock negativo;
9. producto sin imagen utiliza fallback;
10. variante sin stock se presenta como no disponible.

### Batería opcional del carrito

1. visitante agrega una variante y el estado queda en sesión;
2. visitante no crea `orders.Cart`;
3. cliente autenticado agrega una variante a su carrito persistente;
4. login migra cantidades válidas desde la sesión;
5. variante inactiva o sin stock no puede agregarse.

Comando de cierre:

```bash
pytest accounts products -q
```

Todos los tests de esta batería deben quedar en verde antes de cerrar la clase.
Si se implementa el bloque opcional, el cierre utiliza `pytest accounts products orders -q`.

---

## 13. Errores frecuentes anticipados

| Error | Causa | Recuperación docente |
|-------|-------|----------------------|
| Migración inconsistente de User | `AUTH_USER_MODEL` definido después de migrar | restaurar base inicial y definirlo antes |
| Operador entra pero no ve modelos | `is_staff=True` sin permisos del grupo | asignar grupo y volver a obtener el usuario |
| Operador ve usuarios | permisos heredados o asignados accidentalmente | revisar grupo y permisos individuales |
| Se confunde Jazzmin con autorización | menú oculto interpretado como seguridad | probar URL directa y explicar permisos Django |
| Productos duplican stock por talle/color | stock ubicado en `Product` | moverlo a `ProductVariant` |
| Inline no aparece | FK o registro admin incorrectos | revisar relación y `inlines` |
| Assets MiniStore no cargan | rutas relativas no convertidas | usar `{% load static %}` y `{% static %}` |
| `NoReverseMatch` en navbar | namespace o URL ausente | revisar `app_name`, `include()` y nombre |
| Cards no muestran imagen | producto sin imagen principal | usar fallback estático |
| El refinamiento visual desplaza reglas centrales | scope visual excesivo | detener estilos y continuar con integración en la próxima clase |
| Test depende de datos previos | fixture implícita o base compartida | crear datos explícitos dentro del test |
| Permiso recién asignado no aparece | cache de permisos del usuario | volver a obtener el usuario desde la base |
| Test de imagen falla por archivo real | prueba acoplada al filesystem | usar archivo temporal o comprobar fallback |

---

## 14. Contrato para filminas y minuta

### Filminas

Cada filmina representa una etapa observable de la implementación docente. Muestra
**qué realiza el profesor en ese momento**, qué cambia en la aplicación y cuál es el
resultado visible. No se presenta como tarea, consigna, checklist ni instrucción dirigida
al alumno.

Las filminas no utilizan imágenes generadas con Gemini. La comunicación visual se resuelve
con texto, código, tablas, diagramas ASCII y capturas reales de Tienda v0.1 cuando sean
necesarias. Durante la publicación, todas las filminas deben conservar capa de imagen
`none`; no se generan assets visuales por IA.

| Elemento | Contenido |
|----------|-----------|
| Título narrativo | Qué cambio se incorpora a la Tienda v0.1 |
| Acción docente | Qué crea, modifica, ejecuta o demuestra el profesor |
| Decisión técnica | Por qué se implementa de esa forma |
| Evolución visible | Cómo cambia la aplicación después de la etapa |
| Verificación | Test, recorrido o resultado que confirma el cambio |
| Pregunta de control | Pregunta breve para interpretar lo observado |

Ejemplos correctos:

```text
F-08 — Creamos el grupo Operadores y limitamos su acceso
F-15 — Modelamos cada combinación vendible como ProductVariant
F-24 — MiniStore deja de mostrar cards fijas y consulta productos reales
F-28 — Recorremos la Tienda v0.1 con cliente, operador y administrador
```

Formulaciones prohibidas:

```text
Tarea: crear el grupo Operadores
Actividad: completar ProductVariant
Ahora ustedes deben adaptar las cards
Checklist de ejercicios
```

No incluir tareas, consignas de práctica autónoma ni instrucciones para los alumnos.
No incluir `@prompt-imagen`, `@asset` ni directivas que activen generación Gemini.

### Minuta por filmina

La minuta deberá contener el código exacto y acumulativo por archivo. Para cada etapa debe
indicar:

1. estado inicial esperado;
2. comandos ejecutados;
3. código escrito;
4. explicación de la decisión;
5. salida esperada;
6. error frecuente y diagnóstico;
7. commit de recuperación siguiente.
8. test ejecutado y resultado esperado.

La minuta se vincula uno a uno con las filminas: mientras la filmina muestra la evolución
de la Tienda v0.1, la minuta contiene el código exacto y la explicación para realizarla.

Además, la minuta incluye una explicación docente detallada de cada fragmento escrito:
responsabilidad de imports, clases y métodos; flujo de ejecución; decisiones ORM; efectos
de cada comando; errores que evita y relación con el comportamiento visible. El profesor
puede dictar el tutorial utilizando solamente `minuta.md`.

### Terminología obligatoria

- usar `products`, no `catalog`;
- usar `ProductVariant`, no “opción” o “detalle”;
- usar cliente, operador y administrador;
- decir “Jazzmin personaliza” y “Django autoriza”;
- decir “MiniStore aporta presentación”, no lógica e-commerce.
- decir “Django Templates renderizan la interfaz”; no presentar la web como SPA.
- relacionar cada feature central con al menos un test observable.

---

## 15. Criterio de cierre del tópico

El diseño se considera implementado cuando la demostración confirma:

- apps `accounts` y `products` creadas y separadas;
- cliente autenticado con Mi cuenta;
- `CustomerProfile` exclusivo del cliente y fuera de Django Admin;
- operador y administrador sin teléfono ni dirección de entrega en `User`;
- operador creado mediante grupo y permisos;
- mismo admin Jazzmin con opciones distintas por autorización;
- prendas con fotos y variantes cargadas desde admin;
- MiniStore alimentado por productos reales;
- home, catálogo, detalle, login y Mi cuenta coherentes mediante Django Templates;
- estados vacíos, imágenes faltantes y variantes sin stock representados correctamente;
- restricciones verificadas por URL directa;
- batería mínima de tests de `accounts` y `products` completamente en verde;
- Tienda v0.1 ejecutable y navegable con productos cargados y visibles;
- recorrido final completo alternando visitante, cliente, operador y administrador;
- anticipo claro: la orden futura operará sobre `ProductVariant`.

El checkpoint `C07-v01` constituye un cierre completo y válido. Después se incorpora un
bloque opcional, sin límite temporal:

- `C08-session-cart`: visitante agrega variantes a un carrito temporal respaldado por
  `request.session`, sin modelos comerciales propios;
- `C09-persistent-cart`: el cliente autenticado posee `orders.Cart` y `CartItem`, y el
  carrito temporal migra al iniciar sesión;
- ambos recorridos quedan protegidos por tests;
- el carrito no reserva stock, no congela precios y todavía no constituye una orden.

---

## 16. Artefactos

| Artefacto | Estado |
|-----------|--------|
| `topic.yaml` | creado |
| `diseno.md` | aprobado |
| `filminas.md` | creado — borrador para revisión |
| `minuta.md` | creada — borrador para revisión |
| `guia-estudio.md` | pendiente |
| `guiaprofesor.md` | pendiente |

---

## 17. Referencias técnicas verificadas

- Django authentication and authorization:
  `https://docs.djangoproject.com/en/6.0/topics/auth/default/`
- Django Admin:
  `https://docs.djangoproject.com/en/6.0/ref/contrib/admin/`
- Jazzmin installation and configuration:
  `https://django-jazzmin.readthedocs.io/installation/`
  y `https://django-jazzmin.readthedocs.io/configuration/`
- Jazzmin releases: verificar y fijar una versión compatible antes de preparar el repo:
  `https://github.com/farridav/django-jazzmin/releases`
- ThemeWagon MiniStore, estructura estática y licencia MIT:
  `https://github.com/themewagon/MiniStore`

> Nota de estabilidad: las filminas y la minuta deben documentar la versión exacta de
> Django y Jazzmin probada en el repositorio inicial. No deben instalar “latest” en vivo.

> **Clase producida**: revisar filminas, minuta y repo inicial antes del dictado.
