# Checkpoints docentes

El repo inicial representa `C00`. Antes de la clase, el docente debe preparar localmente
los commits de recuperación siguientes. No se incluyen como solución dentro de este
starter.

| Checkpoint | Estado esperado |
|------------|-----------------|
| `C00-starter` | Django, Jazzmin, MiniStore y pytest funcionando |
| `C01-environment` | `.venv` activo y dependencias verificadas |
| `C02-accounts` | `accounts.User`, login y Mi cuenta funcionando |
| `C03-permissions` | cliente, operador y administrador diferenciados |
| `C04-products` | modelos y tests de variantes en verde |
| `C05-admin-data` | catálogo cargable desde admin |
| `C06-storefront` | home, catálogo y detalle conectados al ORM |
| `C07-v01` | Tienda v0.1 navegable y batería mínima en verde |
| `C08-session-cart` | carrito público temporal respaldado por sesión |
| `C09-persistent-cart` | carrito del cliente persistido y migración al iniciar sesión |

Al terminar cada sesión, guardar el checkpoint consistente alcanzado. La próxima clase
continúa desde allí. Nunca saltear testing, permisos ni recorrido final para terminar antes.

`C07-v01` cierra el incremento obligatorio. `C08` y `C09` son extensiones opcionales:
pueden implementarse al final o trasladarse completas a la clase siguiente.
