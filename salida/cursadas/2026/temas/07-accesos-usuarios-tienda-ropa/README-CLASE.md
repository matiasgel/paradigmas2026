# Clase 07 — Guía de uso

## Artefactos

- `diseno.md`: alcance y decisiones pedagógicas.
- `filminas.md`: narración visual de lo que realiza el profesor.
- `minuta.md`: guion autocontenido y código exacto por filmina.
- `repo-inicial/`: starter docente pre-preparado.

## Antes de la clase

1. Verificar conectividad y disponibilidad de Python 3.11.
2. Mantener disponible `repo-inicial/requirements.txt`.
3. Preparar localmente los checkpoints de `repo-inicial/CHECKPOINTS-DOCENTE.md`.
4. No ejecutar `migrate` antes de crear `accounts.User` durante la demostración.

La creación y activación de `.venv`, la instalación de dependencias y los primeros checks
se realizan frente al curso en la filmina F-03.

## Durante la clase

- Abrir `filminas.md` para sostener la narrativa.
- Usar `minuta.md` como único guion técnico.
- Cerrar la sesión en el último checkpoint consistente alcanzado.
- No recortar testing, permisos ni recorrido final.
- No convertir las filminas en tareas para alumnos.
- No generar imágenes Gemini para las filminas; usar código, tablas, ASCII o capturas reales.

No se calculan tiempos por filmina. Si no se completa Tienda v0.1, la próxima clase
retoma desde el checkpoint alcanzado.

## Cierre obligatorio

El tópico termina recorriendo Tienda v0.1 como visitante, cliente, operador y administrador,
con productos visibles y la batería mínima de tests en verde. Puede requerir más de una clase.

## Extensión opcional

Después de `C07-v01`, las filminas F-28 a F-35 incorporan carrito público temporal y
carrito persistente del cliente. Si no se implementan, quedan completas para continuar
en la próxima clase; no forman parte del cierre obligatorio de Tienda v0.1.
