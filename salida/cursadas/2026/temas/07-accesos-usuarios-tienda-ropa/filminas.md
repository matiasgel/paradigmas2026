# Clase 07 — Accesos, usuarios y tienda de ropa con variantes

## PORTADA

---

### [F-00] De un theme a una tienda
@tipo: demo
@imagen: none

# Construimos Tienda v0.1 con Django

MiniStore + Templates + ORM + Auth + Admin + Testing

---

### [F-01] El producto final ya es visible
@tipo: demo

# Tienda v0.1 se recorre con cuatro perspectivas

- Visitante: navega productos
- Cliente: inicia sesión y abre Mi cuenta
- Operador: carga catálogo desde Jazzmin
- Administrador: gestiona usuarios y permisos

---

### [F-02] La arquitectura separa responsabilidades
@tipo: demo
@imagen: none

# Hoy creamos accounts y products

- `accounts`: identidad, autenticación y perfiles de cliente
- `products`: catálogo, imágenes, variantes y stock
- `orders`: depende de usuarios y variantes
- `operations`: depende de las órdenes

---

## BLOQUE A — Identidad y acceso

---

### [F-03] Activamos un entorno reproducible
@tipo: demo

# Instalamos dependencias antes de ejecutar el starter

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py check
python -m pytest -q
```

El entorno contiene Django, Jazzmin, Pillow y pytest-django.

---

### [F-04] Creamos la app propietaria de la identidad
@tipo: codigo

# accounts encapsula usuarios y autenticación

```powershell
python manage.py startapp accounts
```

```python
INSTALLED_APPS = [
    "jazzmin",
    "accounts",
    # django.contrib...
]
```

---

### [F-05] Separamos identidad común y perfil cliente
@tipo: codigo

# AUTH_USER_MODEL es una decisión temprana

```python
class User(AbstractUser):
    pass

class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, ...)
    phone = models.CharField(max_length=30, blank=True)
    shipping_address = models.TextField(blank=True)
```

```python
AUTH_USER_MODEL = "accounts.User"
```

Operador y administrador son usuarios, pero no poseen `CustomerProfile`.

---

### [F-06] Mi cuenta confirma la autenticación
@tipo: demo

# LoginRequiredMixin protege la vista cliente

- Usuario anónimo: redirección al login
- Cliente autenticado: ve sus datos
- Usuario `is_staff`: acceso denegado
- El template hereda la base MiniStore
- El primer test de acceso queda en verde

---

### [F-07] is_staff abre la puerta, no concede permisos
@tipo: concepto-mixto
@imagen: none

# ¿Un operador staff puede editar productos automáticamente?

`is_staff=True` permite entrar a `/admin/`.

Los permisos determinan qué puede hacer adentro.

---

### [F-08] Creamos el grupo Operadores
@tipo: codigo

# El rol se expresa con Group y Permission

```python
operator_group, _ = Group.objects.get_or_create(name="Operadores")
operator.is_staff = True
operator.groups.add(operator_group)
```

---

### [F-09] El mismo admin muestra opciones diferentes
@tipo: tabla-comparativa

# Django autoriza; Jazzmin personaliza

| Capacidad | Cliente | Operador | Administrador |
|-----------|---------|----------|---------------|
| Entrar al admin | No | Sí | Sí |
| Gestionar catálogo | No | Sí | Sí |
| Gestionar usuarios | No | No | Sí |
| Gestionar permisos | No | No | Sí |

---

### [F-10] Probamos la URL que el menú no muestra
@tipo: demo

# Ocultar enlaces no reemplaza autorización

- Cliente no entra a `/admin/`
- Operador entra al admin
- Operador no abre usuarios por URL directa
- Administrador conserva acceso completo

---

### [F-11] Jazzmin organiza el panel interno
@tipo: demo

# Un único admin sirve a operador y administrador

- Branding de Tienda v0.1
- Apps y modelos ordenados
- Íconos para lectura rápida
- Menú final condicionado por permisos Django

---

### [F-12] UserAdmin administra identidad y permisos
@tipo: codigo

# El perfil comercial permanece fuera del admin

```python
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    pass
```

`CustomerProfile` no se registra en Django Admin.

---

### [F-13] El bloque de identidad queda protegido
@tipo: demo

# La batería de accounts queda en verde

```powershell
pytest accounts -q
```

- Mi cuenta requiere login
- Operador y administrador no acceden a Mi cuenta
- Cliente no accede al admin
- Operador no gestiona usuarios

---

## BLOQUE P — Productos y variantes

---

### [F-14] Creamos la app propietaria del catálogo
@tipo: codigo

# products no conoce órdenes ni pagos

```powershell
python manage.py startapp products
```

---

### [F-15] Una prenda no es una unidad vendible
@tipo: codigo
@imagen: none

# Product describe; ProductVariant vende

```text
Remera clásica
├── Negro / S / stock 4
├── Negro / M / stock 8
└── Blanco / M / stock 0
```

---

### [F-16] Modelamos catálogo, imágenes y variantes
@tipo: codigo

# El stock pertenece a ProductVariant

```python
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name="variants", ...)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=40)
    sku = models.CharField(max_length=40, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
```

---

### [F-17] Las restricciones convierten reglas en datos válidos
@tipo: codigo

# La base protege la combinación vendible

```python
constraints = [
    models.UniqueConstraint(
        fields=["product", "size", "color"],
        name="unique_product_size_color",
    )
]
```

- SKU único
- Combinación única
- Stock no negativo
- Publicación mediante permiso personalizado

---

### [F-18] El test rojo revela una regla incumplida
@tipo: demo

# Duplicar una variante debe fallar

```powershell
pytest products/tests/test_models.py -q
```

El test primero falla; la restricción lo convierte en verde.

---

### [F-19] Los inlines convierten relaciones en flujo operativo
@tipo: demo

# El operador carga una prenda completa en una pantalla

- Datos comunes en Product
- Talle, color, SKU, precio y stock en variantes
- Imágenes con texto alternativo
- Sin permiso de borrado

---

### [F-20] Cargamos productos que cuentan una historia real
@tipo: demo

# El catálogo incluye estados distintos

- Productos activos e inactivos
- Variantes con y sin stock
- Productos con y sin imagen
- Categorías y destacados

---

## BLOQUE S — Storefront con Django Templates

---

### [F-21] MiniStore aporta presentación, no lógica
@tipo: tabla-comparativa

# Transformamos HTML estático en interfaz Django

| MiniStore original | Tienda v0.1 |
|--------------------|-------------|
| Rutas relativas | `{% static %}` |
| Links fijos | `{% url %}` |
| Cards escritas | loop de productos |
| Precio de muestra | precio mínimo de variantes |

---

### [F-22] Las CBV entregan contexto real a los templates
@tipo: codigo

# Home, catálogo y detalle consultan el ORM

```python
class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"

    def get_queryset(self):
        return Product.objects.filter(active=True)
```

---

### [F-23] Una card reutilizable reemplaza contenido duplicado
@tipo: codigo

# product_card.html representa un producto real

```django
{% for product in products %}
  {% include "store/includes/product_card.html" %}
{% empty %}
  <p>Todavía no hay productos disponibles.</p>
{% endfor %}
```

---

### [F-24] El detalle muestra variantes y disponibilidad
@tipo: demo

# La tienda ya permite explorar una prenda

- Galería o imagen fallback
- Talles y colores disponibles
- Precio por variante
- Sin stock claramente visible

---

### [F-25] La batería integrada protege Tienda v0.1
@tipo: demo

# Ejecutamos todos los tests de accounts y products

```powershell
pytest accounts products -q
```

- Modelos
- Autenticación
- Autorización
- Vistas y templates

---

### [F-26] Recorremos la aplicación sin mirar el código
@tipo: demo

# Tienda v0.1 funciona como producto

1. Visitante navega productos
2. Cliente inicia sesión
3. Operador carga una variante
4. Administrador gestiona usuarios

---

### [F-27] Tienda v0.1 queda cerrada antes de extenderla
@tipo: demo
@imagen: none

# Tienda v0.1 ya vende una idea completa

Hoy: identidad + catálogo + storefront + testing

Si termina la sesión, guardamos `C07-v01` y continuamos desde aquí.

---

## BLOQUE OPCIONAL — Carrito público y persistencia del cliente

---

### [F-28] El carrito comienza como estado temporal
@tipo: tabla-comparativa
@imagen: none

# Un carrito público no necesita una orden

| Carrito público | Carrito del cliente |
|-----------------|---------------------|
| Vive en `request.session` | Vive en modelos de `orders` |
| No identifica una persona | Pertenece a `request.user` |
| Guarda variante y cantidad | Guarda relaciones persistentes |
| Puede migrarse al iniciar sesión | Continúa entre sesiones |

---

### [F-29] La sesión guarda identificadores, no productos
@tipo: codigo
@imagen: none

# El carrito temporal referencia ProductVariant

```python
CART_SESSION_KEY = "cart"

cart = request.session.setdefault(CART_SESSION_KEY, {})
key = str(variant.id)
cart[key] = min(cart.get(key, 0) + 1, variant.stock)
request.session.modified = True
```

El precio y la disponibilidad siempre vuelven a consultarse en el ORM.

---

### [F-30] Agregar y ver el carrito completa el flujo público
@tipo: demo
@imagen: none

# Visitante agrega una variante y revisa su carrito

1. Selecciona una variante disponible
2. Envía un `POST` para agregarla
3. Django actualiza la sesión
4. La vista resuelve variantes y calcula subtotales

El carrito no reserva stock ni crea una orden.

---

### [F-31] Un test demuestra que el carrito público no crea modelos
@tipo: codigo
@imagen: none

# La sesión cambia; la base comercial todavía no

```python
response = client.post(reverse("orders:cart-add", args=[variant.pk]))

assert client.session["cart"][str(variant.pk)] == 1
```

En este checkpoint `orders` todavía no define modelos de carrito.

---

### [F-32] El cliente autenticado obtiene un carrito persistente
@tipo: codigo
@imagen: none

# orders incorpora Cart y CartItem

```python
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, ...)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", ...)
    variant = models.ForeignKey("products.ProductVariant", ...)
    quantity = models.PositiveIntegerField(default=1)
```

---

### [F-33] Iniciar sesión migra el carrito temporal
@tipo: demo
@imagen: none

# La autenticación conserva la intención de compra

1. Django autentica al usuario
2. Recuperamos `request.session["cart"]`
3. Validamos variantes y cantidades
4. Creamos o actualizamos `CartItem`
5. Limpiamos el carrito temporal

El carrito persistente conserva la intención de compra del visitante.

---

### [F-34] Los tests protegen continuidad y separación
@tipo: demo
@imagen: none

# Verificamos ambos recorridos del carrito

```powershell
pytest orders -q
```

- visitante agrega sin crear `Cart`
- cliente agrega en su carrito persistente
- login migra el carrito temporal
- variante sin stock no puede agregarse

---

### [F-35] El carrito prepara la próxima versión
@tipo: demo
@imagen: none

# Tienda v0.2 conserva intención de compra

Obligatorio: `C07-v01` — identidad + catálogo + storefront + tests

Opcional: `C08-session-cart` y `C09-persistent-cart`

Próxima evolución: convertir el carrito persistente en una orden
