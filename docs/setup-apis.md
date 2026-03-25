# Setup de APIs — Google OAuth + Gemini

Guía para configurar las credenciales necesarias para el módulo EDU:

- `credentials.json` → Google OAuth 2.0 para **Google Slides API**
- `gemini_api_key` → Para **generación de imágenes** en filminas

Al final del proceso debés tener:

- `_edu/credentials.json`
- `_edu/secrets.local.yaml`

> Ambos archivos ya están en `.gitignore` — nunca se subirán al repo.

---

## 1. Google OAuth 2.0 — `credentials.json`

### 1.1 Crear o seleccionar proyecto

1. Ir a https://console.cloud.google.com
2. Iniciar sesión con la cuenta de Google dueña de las presentaciones
3. En la barra superior, hacer clic en el selector de proyecto
4. Crear proyecto nuevo (ej: `paradigmas2026`) o elegir uno existente

---

### 1.2 Habilitar APIs necesarias

1. Ir a **APIs y servicios → Biblioteca**
2. Buscar y habilitar **Google Slides API**
3. Recomendado: buscar y habilitar también **Google Drive API**

---

### 1.3 Configurar pantalla de consentimiento OAuth

1. Ir a **APIs y servicios → Pantalla de consentimiento OAuth**
2. Elegir tipo de usuario:
   - **External** para cuentas personales de Google (caso más común)
   - **Internal** si se usa Google Workspace institucional
3. Completar datos mínimos requeridos:
   - Nombre de la app (ej: `EDU Slides`)
   - Correo de soporte
   - Correo del desarrollador
4. Guardar

---

### 1.4 Agregar usuario de prueba (si la app queda en modo Testing)

Si elegiste **External**, la app queda en estado **Testing**.

1. En la pantalla de consentimiento, ir a la sección **Test users**
2. Agregar tu propio correo de Google como usuario de prueba

Esto evita el error "app no verificada / acceso denegado" al autenticarse.

---

### 1.5 Crear credencial OAuth 2.0

1. Ir a **APIs y servicios → Credenciales**
2. Hacer clic en **Crear credenciales → ID de cliente OAuth**
3. En tipo de aplicación, elegir **Aplicación de escritorio** (Desktop App)
4. Poner un nombre descriptivo (ej: `EDU Local Desktop`)
5. Guardar

---

### 1.6 Descargar y colocar el JSON

1. En la lista de credenciales, buscar la recién creada
2. Hacer clic en el ícono de descarga (JSON)
3. Renombrar el archivo descargado a `credentials.json`
4. Moverlo a:

```
_edu/credentials.json
```

El archivo debe contener campos como `client_id`, `project_id`, `auth_uri`, `token_uri`. No hay que editar nada a mano.

---

### Problemas comunes

| Problema | Solución |
|----------|----------|
| No deja crear credenciales OAuth | Completar primero la pantalla de consentimiento OAuth |
| "App no verificada" o acceso bloqueado | Agregar tu cuenta como **Test user** en la pantalla de consentimiento |
| No aparece Google Slides API en la búsqueda | Buscar el término exacto `Google Slides API` |
| El archivo descargado tiene otro nombre | Renombrarlo a `credentials.json` antes de moverlo |

---

## 2. Gemini API Key

### 2.1 Crear la key

1. Ir a https://aistudio.google.com/app/apikey
2. Iniciar sesión con tu cuenta de Google
3. Hacer clic en **Create API key** (o **Get API key**)
4. Elegir el proyecto de Google Cloud si lo pide
5. Confirmar la creación

---

### 2.2 Copiar la key

La key se muestra una sola vez como texto largo, tipo `AIza...`.  
Copiarla y guardarla de forma temporal hasta completar el paso siguiente.

---

## 3. Crear `_edu/secrets.local.yaml`

Con ambas credenciales listas, crear (o actualizar) el archivo:

```yaml
google_credentials_path: "_edu/credentials.json"
gemini_api_key: "<pegar-aquí-la-key-de-gemini>"
```

> ⚠️ En `google_credentials_path` va **solo la ruta** al JSON, nunca el contenido del archivo.

---

## 4. Orden recomendado

1. Crear/seleccionar proyecto en Google Cloud
2. Habilitar Google Slides API
3. Habilitar Google Drive API (recomendado)
4. Configurar pantalla OAuth
5. Agregar usuario de prueba
6. Crear credencial OAuth tipo Desktop App
7. Descargar JSON → renombrar a `credentials.json` → mover a `_edu/`
8. Ir a Google AI Studio → crear Gemini API key → copiarla
9. Crear `_edu/secrets.local.yaml` con ambos campos

---

## 5. Verificación final

Confirmar que existen los dos archivos:

```
_edu/credentials.json
_edu/secrets.local.yaml
```

Y que `secrets.local.yaml` tiene exactamente estos campos:

```yaml
google_credentials_path: "_edu/credentials.json"
gemini_api_key: "AIza..."
```

Si todo está correcto, podés correr `/edu_slides_designer` para definir el diseño visual de las filminas.
