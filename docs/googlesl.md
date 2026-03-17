# Google Slides API — Referencia Exhaustiva para BMAD/EDU

> Documento de referencia conectado a `.github/copilot-instructions.md`.
> Proyecto: `paradigmas2026`.
> Actualizado: **16 marzo 2026**.
> Fuentes principales: documentación oficial de Google Workspace / Google Slides API.

---

## Indice

1. [Objetivo de este documento](#1-objetivo-de-este-documento)
2. [Relacion con BMAD y este repo](#2-relacion-con-bmad-y-este-repo)
3. [Que es la Google Slides API](#3-que-es-la-google-slides-api)
4. [Superficie completa del API REST](#4-superficie-completa-del-api-rest)
5. [Modelo de datos de una presentacion](#5-modelo-de-datos-de-una-presentacion)
6. [Autenticacion y autorizacion](#6-autenticacion-y-autorizacion)
7. [Scopes OAuth relevantes](#7-scopes-oauth-relevantes)
8. [Cuotas y limites](#8-cuotas-y-limites)
9. [Concepto central: batchUpdate](#9-concepto-central-batchupdate)
10. [Metodos REST](#10-metodos-rest)
11. [Tipos de Request en batchUpdate](#11-tipos-de-request-en-batchupdate)
12. [Field masks](#12-field-masks)
13. [Transforms y geometria](#13-transforms-y-geometria)
14. [Texto, listas y estilos](#14-texto-listas-y-estilos)
15. [Imagenes, video y charts](#15-imagenes-video-y-charts)
16. [Notas del presentador](#16-notas-del-presentador)
17. [IDs, revisiones y concurrencia](#17-ids-revisiones-y-concurrencia)
18. [Patrones recomendados de integracion](#18-patrones-recomendados-de-integracion)
19. [Mapeo concreto al proyecto paradigmas2026](#19-mapeo-concreto-al-proyecto-paradigmas2026)
20. [Ejemplos minimos en Python](#20-ejemplos-minimos-en-python)
21. [Checklist operativo para futuros agentes BMAD](#21-checklist-operativo-para-futuros-agentes-bmad)
22. [Fuentes oficiales consultadas](#22-fuentes-oficiales-consultadas)

---

## 1. Objetivo de este documento

Este documento concentra una investigacion exhaustiva de la **Google Slides API v1** con foco en:

- la superficie real del API REST;
- los recursos, metodos y tipos de request disponibles;
- autenticacion, scopes y cuotas;
- restricciones operativas importantes;
- patrones correctos de uso en automatizacion;
- como debe usarse dentro de este proyecto bajo las reglas de `.github/copilot-instructions.md`.

No reemplaza la documentacion oficial de Google, pero la sintetiza y la aterriza al contexto BMAD/EDU de este repo.

---

## 2. Relacion con BMAD y este repo

Segun `.github/copilot-instructions.md`:

- el objetivo del proyecto es desarrollar `edu-standalone`;
- no se deben modificar archivos dentro de `_bmad/`;
- cualquier artefacto funcional del modulo EDU vive en `salida/edu-standalone/`;
- la documentacion tecnica general del proyecto vive en `docs/`.

Por eso este archivo vive en `docs/` y funciona como referencia transversal para agentes y prompts que publiquen filminas en Google Slides.

Implicancias practicas para este repo:

- la integracion real con Google Slides ya existe en `salida/edu-standalone/scripts/slides_pipeline.py`;
- las capturas de slides usan `presentations.pages.getThumbnail` desde `salida/edu-standalone/scripts/test_pipeline.py`;
- la configuracion de diseño se define en `_edu/slides-config.yaml` y se replica en salidas de prueba;
- los agentes EDU relacionados con Slides viven en `salida/edu-standalone/_edu/agents/` y prompts en `salida/edu-standalone/.github/prompts/`.

---

## 3. Que es la Google Slides API

La Google Slides API permite **leer y escribir presentaciones de Google Slides**.

Capacidades principales:

- crear presentaciones vacias;
- leer presentaciones completas o paginas individuales;
- modificar una presentacion con `batchUpdate`;
- crear slides, shapes, tables, images, videos, lines y charts embebidos;
- insertar, borrar, reemplazar y estilizar texto;
- mover, duplicar y borrar slides y elementos;
- generar thumbnails de slides;
- trabajar con speaker notes.

No es un API de renderizado libre tipo canvas. La unidad de trabajo es el **modelo estructurado de Slides**: presentacion → paginas → page elements.

---

## 4. Superficie completa del API REST

Servicio:

- `slides.googleapis.com`

Discovery document:

- `https://slides.googleapis.com/$discovery/rest?version=v1`

Endpoint base:

- `https://slides.googleapis.com`

Recursos REST disponibles en v1:

| Recurso | Metodos |
| --- | --- |
| `presentations` | `create`, `get`, `batchUpdate` |
| `presentations.pages` | `get`, `getThumbnail` |

Observacion importante: la API publica tiene **pocos endpoints**, pero `batchUpdate` concentra casi toda la potencia mediante una union de **44 tipos de request**.

---

## 5. Modelo de datos de una presentacion

### 5.1 Presentation

Una `Presentation` contiene, entre otros campos:

- `presentationId`
- `pageSize`
- `slides[]`
- `title`
- `masters[]`
- `layouts[]`
- `locale`
- `revisionId`
- `notesMaster`

### 5.2 Tipos de pagina

Google Slides modela cinco tipos de pagina:

| `PageType` | Significado |
| --- | --- |
| `SLIDE` | filmina visible de la presentacion |
| `MASTER` | slide master |
| `LAYOUT` | layout derivado de un master |
| `NOTES` | pagina de notas de una slide |
| `NOTES_MASTER` | master de notas |

### 5.3 Page elements soportados

Una pagina puede contener estos tipos principales de `PageElement`:

- `Group`
- `Shape`
- `Image`
- `Video`
- `Line`
- `Table`
- `WordArt`
- `SheetsChart`
- `SpeakerSpotlight`

Cada `PageElement` tiene:

- `objectId`
- `size`
- `transform`
- `title`
- `description`

Los campos `title` y `description` conforman el alt text accesible del elemento.

### 5.4 Notas del presentador

Cada slide tiene una `notesPage` asociada. El contenido editable son solo las speaker notes dentro del placeholder `BODY` identificado por `speakerNotesObjectId`.

---

## 6. Autenticacion y autorizacion

### 6.1 Modelo general

La Slides API usa OAuth 2.0. En apps de usuario final se recomienda:

- configurar el consentimiento OAuth en Google Cloud;
- pedir el scope minimo posible;
- usar credenciales de usuario para presentaciones que quedaran bajo control del usuario;
- usar cuentas de servicio solo para activos internos o plantillas controladas por la aplicacion.

### 6.2 Pantalla de consentimiento

Google exige configurar:

- branding de la app;
- audience interna o externa;
- email de soporte;
- scopes declarados;
- test users si la app es externa y aun no esta publicada.

### 6.3 Categorias de scopes

Google agrupa scopes en:

- no sensibles;
- sensibles;
- restringidos.

Principio operativo: **pedir siempre el scope mas estrecho posible**.

### 6.4 Recomendacion de arquitectura para plantillas

La documentacion oficial recomienda:

- crear y mantener la plantilla con una cuenta controlada por la aplicacion, idealmente service account;
- crear copias finales con credenciales del usuario final;
- aplicar reemplazos sobre la copia, no sobre la plantilla maestra.

Esto encaja muy bien con flujos BMAD/EDU donde hay un template institucional y multiples publicaciones por tema.

---

## 7. Scopes OAuth relevantes

### 7.1 Scopes base de Slides

| Scope | Uso |
| --- | --- |
| `https://www.googleapis.com/auth/presentations` | lectura y escritura de Slides |
| `https://www.googleapis.com/auth/presentations.readonly` | solo lectura |

### 7.2 Scopes de Drive que suelen intervenir

| Scope | Uso |
| --- | --- |
| `https://www.googleapis.com/auth/drive` | acceso amplio a Drive |
| `https://www.googleapis.com/auth/drive.file` | acceso a archivos creados o abiertos por la app |
| `https://www.googleapis.com/auth/drive.readonly` | lectura de archivos |

### 7.3 Scopes de Sheets para charts

| Scope | Uso |
| --- | --- |
| `https://www.googleapis.com/auth/spreadsheets.readonly` | recomendado para insertar o refrescar charts |
| `https://www.googleapis.com/auth/spreadsheets` | lectura/escritura en Sheets |

### 7.4 Scopes por metodo REST

| Metodo | Scopes admitidos destacados |
| --- | --- |
| `presentations.create` | `presentations`, `drive`, `drive.file` |
| `presentations.get` | `presentations`, `presentations.readonly`, `drive`, `drive.file`, `drive.readonly` |
| `presentations.batchUpdate` | `presentations`, `drive`, `drive.file`, `drive.readonly`, y tambien `spreadsheets*` para charts |
| `presentations.pages.get` | `presentations`, `presentations.readonly`, `drive*` |
| `presentations.pages.getThumbnail` | `presentations`, `presentations.readonly`, `drive*` |

### 7.5 Scopes adicionales por feature

- `createVideo` con fuente Google Drive requiere al menos uno de `drive`, `drive.readonly` o `drive.file`.
- `createSheetsChart`, `refreshSheetsChart` y `replaceAllShapesWithSheetsChart` requieren alguno de `spreadsheets.readonly`, `spreadsheets`, `drive.readonly`, `drive.file` o `drive`.

### 7.6 Scope actual del pipeline del repo

El pipeline actual usa:

```python
SCOPES = [
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/drive",
]
```

Eso alcanza para:

- crear y modificar presentaciones;
- copiar templates con Drive;
- subir assets a Drive;
- pedir thumbnails.

Si el proyecto pasa a usar charts de Sheets, conviene evaluar agregar `spreadsheets.readonly` en vez de ampliar innecesariamente permisos.

---

## 8. Cuotas y limites

Cuotas oficiales por minuto:

| Tipo | Por proyecto | Por usuario por proyecto |
| --- | ---: | ---: |
| Read requests | 3000 | 600 |
| Expensive read requests | 300 | 60 |
| Write requests | 600 | 60 |

`presentations.pages.getThumbnail` cuenta como **expensive read request**.

### 8.1 Politica de retry

Ante `429 Too many requests`, Google recomienda **truncated exponential backoff**:

- esperar `min((2^n + jitter), maximum_backoff)`;
- usar jitter aleatorio hasta 1000 ms;
- un `maximum_backoff` tipico es 32 o 64 segundos.

### 8.2 Pricing

El uso de la Slides API no tiene costo adicional segun la documentacion oficial. Exceder cuota no factura extra; simplemente falla o se rate-limita.

### 8.3 Limites funcionales relevantes

- imagenes: menos de 50 MB;
- imagenes: maximo 25 megapixeles;
- formatos de imagen para insercion: PNG, JPEG o GIF;
- URL de imagen: publica y de hasta 2 KB;
- insercion de filas/columnas en tabla: maximo 20 por request;
- `revisionId`: solo valido por 24 horas;
- thumbnails: `contentUrl` con vida util tipica de 30 minutos.

---

## 9. Concepto central: batchUpdate

`presentations.batchUpdate` es el nucleo operativo del API.

### 9.1 Que hace

Recibe una lista de `Request` y aplica todos los cambios juntos.

### 9.2 Garantias

- cada request se valida antes de aplicar;
- si un request es invalido, falla todo el batch;
- las actualizaciones validas del batch se aplican **atomicamente**;
- la respuesta devuelve `replies[]` alineadas 1:1 con `requests[]`.

### 9.3 Concurrencia

Puede haber colaboradores editando la misma presentacion. Google garantiza la atomicidad del batch, pero el resultado visual final puede coexistir con cambios externos.

### 9.4 WriteControl

`writeControl.requiredRevisionId` permite rechazar la escritura si la presentacion cambio desde la ultima lectura conocida.

Esto es importante para automatizaciones BMAD que quieran evitar sobrescribir cambios manuales.

---

## 10. Metodos REST

### 10.1 `presentations.create`

`POST /v1/presentations`

Uso real:

- crea una presentacion vacia con el `title` indicado;
- si se pasa `presentationId`, intenta usarlo;
- otros campos del body son ignorados al crear.

Punto importante: si se quiere crear una presentacion directamente en una carpeta especifica de Drive, Slides API no lo hace sola. Hay dos alternativas:

- crear y luego mover con Drive API `files.update`;
- crear el archivo desde Drive API con `mimeType=application/vnd.google-apps.presentation`.

### 10.2 `presentations.get`

`GET /v1/presentations/{presentationId}`

Uso real:

- devuelve la estructura completa de la presentacion;
- admite `fields` para lectura parcial;
- es la forma correcta de descubrir slides, layouts, masters, object IDs y revision ID.

### 10.3 `presentations.batchUpdate`

`POST /v1/presentations/{presentationId}:batchUpdate`

Uso real:

- toda mutacion importante se hace aqui;
- acepta `requests[]` y opcionalmente `writeControl`.

### 10.4 `presentations.pages.get`

`GET /v1/presentations/{presentationId}/pages/{pageObjectId}`

Uso real:

- devuelve una pagina concreta;
- util para inspeccionar una slide puntual;
- util para obtener geometria exacta de elementos o speaker notes.

### 10.5 `presentations.pages.getThumbnail`

`GET /v1/presentations/{presentationId}/pages/{pageObjectId}/thumbnail`

Uso real:

- genera una miniatura PNG de una slide;
- soporta tamanos `SMALL`, `MEDIUM`, `LARGE`;
- responde con `contentUrl` temporal.

En este proyecto se usa para screenshots automatizadas en tests/reportes.

---

## 11. Tipos de Request en batchUpdate

La union `Request` soporta **44** operaciones. A continuacion quedan agrupadas por dominio.

### 11.1 Slides y paginas

| Request | Funcion |
| --- | --- |
| `createSlide` | crea una slide |
| `updateSlidesPosition` | reordena slides |
| `duplicateObject` | duplica slide o elemento |
| `updatePageProperties` | cambia propiedades de pagina |
| `updateSlideProperties` | cambia propiedades de slide, por ejemplo `isSkipped` |
| `deleteObject` | elimina slide o elemento |

Notas:

- `createSlide` puede usar `predefinedLayout` o `layoutId`;
- se puede fijar `insertionIndex`;
- `placeholderIdMappings` permite controlar IDs de placeholders copiados desde el layout.

### 11.2 Creacion de elementos visuales

| Request | Funcion |
| --- | --- |
| `createShape` | crea un shape o textbox |
| `createTable` | crea una tabla |
| `createImage` | inserta una imagen desde URL publica |
| `createVideo` | inserta video de YouTube o Drive |
| `createSheetsChart` | inserta chart de Sheets |
| `createLine` | crea lineas o conectores |

### 11.3 Movimiento, orden y agrupacion de elementos

| Request | Funcion |
| --- | --- |
| `updatePageElementTransform` | mueve, escala, rota o refleja |
| `updatePageElementsZOrder` | cambia z-order |
| `groupObjects` | agrupa elementos |
| `ungroupObjects` | desagrupa |
| `updateLineCategory` | cambia categoria de linea/conector |
| `rerouteLine` | rerutea un conector |

### 11.4 Texto

| Request | Funcion |
| --- | --- |
| `insertText` | inserta texto en shape o celda |
| `deleteText` | borra un rango |
| `replaceAllText` | reemplazo global por substring o regex |
| `updateTextStyle` | cambia formato de caracteres |
| `updateParagraphStyle` | cambia formato de parrafos |
| `createParagraphBullets` | convierte texto en lista |
| `deleteParagraphBullets` | elimina bullets |

Notas clave:

- el texto siempre vive dentro de un `Shape` o una celda de `Table`;
- los indices son en unidades Unicode;
- existe un newline implicito al final de shapes y celdas;
- insertar texto puede desactivar `autofit`.

### 11.5 Tablas

| Request | Funcion |
| --- | --- |
| `insertTableRows` | inserta filas |
| `insertTableColumns` | inserta columnas |
| `deleteTableRow` | elimina fila |
| `deleteTableColumn` | elimina columna |
| `updateTableCellProperties` | actualiza celdas |
| `updateTableBorderProperties` | actualiza bordes |
| `updateTableColumnProperties` | ajusta columnas |
| `updateTableRowProperties` | ajusta filas |
| `mergeTableCells` | merge de celdas |
| `unmergeTableCells` | unmerge |

Notas clave:

- tablas no soportan shear;
- los transforms de tabla deben tener escala 1 y sin shear en creacion;
- hay minimo de 32 pt para `columnWidth`.

### 11.6 Imagenes, video y charts

| Request | Funcion |
| --- | --- |
| `updateImageProperties` | actualiza propiedades de imagen |
| `updateVideoProperties` | actualiza propiedades de video |
| `replaceAllShapesWithImage` | reemplaza tags por imagen |
| `replaceImage` | reemplaza una imagen existente |
| `replaceAllShapesWithSheetsChart` | reemplaza tags por chart |
| `refreshSheetsChart` | refresca chart linkeado |

### 11.7 Estilo y accesibilidad

| Request | Funcion |
| --- | --- |
| `updateShapeProperties` | relleno, outline, sombra, etc. |
| `updateLineProperties` | estilo de linea |
| `updatePageElementAltText` | actualiza alt text |

### 11.8 Observaciones importantes sobre Requests especiales

#### `replaceAllText`

Usa `SubstringMatchCriteria`:

- `text`
- `matchCase`
- `searchByRegex`

Es ideal para plantillas con tags como `{{titulo}}`.

#### `replaceAllShapesWithImage`

Permite reemplazar shapes que contienen cierto texto por una imagen.

Modos:

- `CENTER_INSIDE`
- `CENTER_CROP`

Es la herramienta correcta para merge de logos o placeholders de imagen.

#### `duplicateObject`

Puede recibir un mapa `objectIds` para controlar los nuevos IDs de elementos duplicados.

#### `updatePageElementAltText`

Muy importante para accesibilidad. `title` y `description` deben ser legibles por humanos y acordes al contenido.

---

## 12. Field masks

La Slides API usa field masks tanto para lectura parcial como para updates selectivos.

### 12.1 Lectura

Se usa el query param `fields`.

Ejemplo:

```http
GET /v1/presentations/{presentationId}?fields=slides.pageElements(objectId,size,transform)
```

Ventajas:

- menos payload;
- mejor rendimiento;
- menor acoplamiento a cambios del schema.

### 12.2 Escritura

Cada request tipo `update*` suele incluir `fields`.

Reglas:

- solo se actualizan los campos nombrados en la mask;
- si nombras un campo en la mask y lo dejas sin valor, lo reseteas al default;
- `*` existe, pero Google recomienda evitarlo en produccion.

Recomendacion fuerte para este proyecto: **siempre listar campos concretos**. No usar `*` salvo experimentacion puntual.

---

## 13. Transforms y geometria

Slides usa `AffineTransform`.

Campos principales:

- `scaleX`
- `scaleY`
- `shearX`
- `shearY`
- `translateX`
- `translateY`
- `unit` (`EMU` o `PT`)

### 13.1 Modos de aplicacion

| `ApplyMode` | Efecto |
| --- | --- |
| `ABSOLUTE` | reemplaza la matriz actual |
| `RELATIVE` | concatena la nueva matriz con la existente |

### 13.2 Operaciones soportadas

- traslacion;
- escala;
- rotacion;
- reflexion.

### 13.3 Puntos finos importantes

- la traslacion posiciona la esquina superior izquierda del elemento, no el centro;
- el orden de operaciones importa;
- para rotar alrededor del centro hay que cambiar de reference frame;
- Google puede refactorizar `size` y `transform` al crear un elemento, manteniendo el mismo resultado visual.

### 13.4 Limitaciones documentadas

| Campo | Shape | Video | Table |
| --- | --- | --- | --- |
| Translation | si | si | si |
| Scale | si | si | no |
| Shear | si | no | no |

Para tablas, el alto/ancho fino se controla con requests de filas y columnas.

---

## 14. Texto, listas y estilos

### 14.1 Donde vive el texto

Solo puede estar en:

- un `Shape`;
- una celda de `Table`.

### 14.2 Operaciones basicas

- insertar: `insertText`;
- borrar: `deleteText`;
- reemplazar globalmente: `replaceAllText`;
- reemplazar localmente: `deleteText` + `insertText` en el mismo batch.

### 14.3 Estilo de texto

`updateTextStyle` soporta, entre otros:

- `bold`
- `italic`
- `underline`
- `strikethrough`
- `smallCaps`
- `fontFamily`
- `fontSize`
- `foregroundColor`
- `baselineOffset`
- `link`

### 14.4 Estilo de parrafo

`updateParagraphStyle` soporta, entre otros:

- `alignment`
- `lineSpacing`
- indentacion;
- espaciados antes/despues;
- direccion y ornamentacion de listas.

### 14.5 Bullets

`createParagraphBullets` admite presets como:

- `BULLET_DISC_CIRCLE_SQUARE`
- `BULLET_ARROW_DIAMOND_DISC`
- `BULLET_CHECKBOX`
- `NUMBERED_DIGIT_ALPHA_ROMAN`
- `NUMBERED_DIGIT_NESTED`
- `NUMBERED_UPPERROMAN_UPPERALPHA_DIGIT`

### 14.6 Consideraciones practicas

- cuando un rango cubre un parrafo de lista completo, el estilo puede afectar tambien el bullet;
- borrar texto que cruza parrafos puede fusionar estilos;
- los indices Unicode importan cuando hay surrogate pairs o clusters.

---

## 15. Imagenes, video y charts

### 15.1 Imagenes

`createImage` requiere una URL publica accesible por Google. La imagen se descarga una vez y queda copiada dentro de la presentacion.

Restricciones:

- menos de 50 MB;
- hasta 25 MP;
- PNG, JPEG o GIF;
- URL publica hasta 2 KB.

Para imagen privada o local, la guia oficial sugiere hacerla accesible temporalmente, por ejemplo con Signed URL en Cloud Storage.

### 15.2 Videos

`createVideo` soporta YouTube y Google Drive.

Notas:

- si el origen es Drive, hace falta scope de Drive adecuado;
- la `transform` no puede tener shear.

### 15.3 Charts de Google Sheets

Flujo oficial:

1. crear chart en Sheets;
2. obtener `spreadsheetId` y `chartId`;
3. insertar con `createSheetsChart`;
4. refrescar con `refreshSheetsChart` si esta en modo `LINKED`.

`LinkingMode`:

| Modo | Efecto |
| --- | --- |
| `LINKED` | refrescable, deja vinculo visible a la planilla |
| `NOT_LINKED_IMAGE` | queda como imagen estatica |

### 15.4 Reemplazo por tags

Los merges de imagen se hacen bien con:

- `replaceAllShapesWithImage` para imagenes;
- `replaceAllShapesWithSheetsChart` para charts.

Este enfoque evita depender de object IDs estables.

---

## 16. Notas del presentador

La API soporta speaker notes de forma acotada pero suficiente.

Reglas oficiales:

- cada slide tiene una notes page;
- solo el texto del primer placeholder `BODY` es editable;
- el resto de la notes page y el notes master son de solo lectura;
- si el shape de notas no existe, una operacion de texto valida sobre `speakerNotesObjectId` puede crearlo automaticamente.

Esto permite automatizar notas docentes sin tocar el layout de la pagina de notas.

---

## 17. IDs, revisiones y concurrencia

### 17.1 Object IDs

Reglas:

- longitud entre 5 y 50 caracteres;
- primer caracter alfanumerico o `_`;
- resto: alfanumericos, `_`, `-`, `:`.

### 17.2 Recomendacion oficial

Aunque se pueden fijar object IDs al crear elementos, Google recomienda **no depender de ellos a largo plazo**, porque acciones manuales en la UI pueden regenerarlos.

Estrategia recomendada:

- para el batch inmediato, fijar IDs si necesitas crear y mutar el elemento en el mismo request;
- para seguimiento de largo plazo, localizar elementos por texto o alt text.

### 17.3 Revision ID

`revisionId`:

- es opaco;
- no es secuencial;
- solo vale por 24 horas;
- sirve para control optimista con `WriteControl.requiredRevisionId`.

---

## 18. Patrones recomendados de integracion

### 18.1 Patron recomendado para plantillas

1. Diseñar la plantilla en Google Slides.
2. Poner tags de texto del tipo `{{placeholder}}`.
3. Para imagenes, usar shapes taggeados.
4. Copiar la plantilla con Drive API.
5. Ejecutar un solo `batchUpdate` grande con reemplazos y creacion de elementos.

### 18.2 Patron recomendado para texto puntual

Si conoces el shape exacto y quieres reemplazo atomico:

- `deleteText` con rango `ALL`;
- `insertText` con `insertionIndex=0`;
- mismo `batchUpdate`.

### 18.3 Patron recomendado para screenshots

- leer slides;
- iterar `pageObjectId`;
- pedir `getThumbnail`;
- descargar el `contentUrl` antes de que expire.

### 18.4 Patron recomendado para performance

- agrupar requests relacionados en un solo batch;
- usar field masks en lecturas grandes;
- evitar loops de `batchUpdate` por elemento si puede resolverse en uno por slide o uno por presentacion;
- manejar `429` con backoff.

---

## 19. Mapeo concreto al proyecto paradigmas2026

### 19.1 Donde ya se usa la API

El uso activo del API en este repo esta concentrado en:

- `salida/edu-standalone/scripts/slides_pipeline.py`
- `salida/edu-standalone/scripts/test_pipeline.py`
- `informe/slides_pipeline.py` como variante o historial de trabajo

### 19.2 Que hace hoy el pipeline

El pipeline EDU implementa, de hecho, varios de los patrones oficiales:

- parsea `filminas.md`;
- genera un plan intermedio;
- produce assets;
- publica en Google Slides;
- usa `googleapiclient.discovery.build`;
- usa Drive para assets y copias;
- genera thumbnails de slides para testing visual.

### 19.3 Reglas de BMAD que afectan esta integracion

- la logica de produccion debe ir en `salida/edu-standalone/`;
- `docs/` puede contener conocimiento reusable como este archivo;
- no corresponde modificar `_bmad/` para resolver integracion con Slides;
- si un agente EDU genera nuevos prompts o agentes para Slides, deben ir a las rutas de `salida/edu-standalone/` definidas en `copilot-instructions.md`.

### 19.4 Decision tecnica valida para este repo

El scope actual `presentations + drive` es coherente con el pipeline actual porque:

- se crean/modifican presentaciones;
- se copian templates;
- se suben o leen assets en Drive;
- se descargan thumbnails.

Si el pipeline evoluciona hacia charts de Sheets, deberia ampliarse de forma minima y explicita.

### 19.5 Riesgos concretos para este proyecto

- depender de object IDs persistentes entre ejecuciones y edicion manual;
- abusar de `getThumbnail` y agotar expensive reads;
- no usar backoff en lotes grandes o ejecuciones concurrentes;
- usar URLs privadas para `createImage`;
- escribir sobre la plantilla original en vez de sobre una copia;
- no cortar la ejecucion ante fallas parciales del publish.

El cambio reciente del pipeline que eleva error cuando fallan lotes es una buena decision y esta alineado con la semantica atomica esperada en automatizacion seria.

---

## 20. Ejemplos minimos en Python

### 20.1 Crear servicio

```python
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

creds = Credentials.from_authorized_user_file(
    "_edu/token_slides.json",
    scopes=[
        "https://www.googleapis.com/auth/presentations",
        "https://www.googleapis.com/auth/drive",
    ],
)

slides = build("slides", "v1", credentials=creds)
```

### 20.2 Leer una presentacion con field mask

```python
presentation = slides.presentations().get(
    presentationId=presentation_id,
    fields="title,slides(objectId,pageElements(objectId,size,transform))",
).execute()
```

### 20.3 Crear una slide y un textbox en un solo batch

```python
requests = [
    {
        "createSlide": {
            "objectId": "slide_0001",
            "slideLayoutReference": {
                "predefinedLayout": "TITLE_AND_BODY"
            },
        }
    },
    {
        "createShape": {
            "objectId": "textbox_0001",
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": "slide_0001",
                "size": {
                    "width": {"magnitude": 300, "unit": "PT"},
                    "height": {"magnitude": 120, "unit": "PT"},
                },
                "transform": {
                    "scaleX": 1,
                    "scaleY": 1,
                    "translateX": 40,
                    "translateY": 80,
                    "unit": "PT",
                },
            },
        }
    },
    {
        "insertText": {
            "objectId": "textbox_0001",
            "insertionIndex": 0,
            "text": "Hola Slides API",
        }
    },
]

slides.presentations().batchUpdate(
    presentationId=presentation_id,
    body={"requests": requests},
).execute()
```

### 20.4 Reemplazo global por tags

```python
requests = [
    {
        "replaceAllText": {
            "containsText": {
                "text": "{{tema}}",
                "matchCase": True,
            },
            "replaceText": "Conceptos Introductorios",
        }
    }
]
```

### 20.5 Thumbnail de una slide

```python
thumb = slides.presentations().pages().getThumbnail(
    presentationId=presentation_id,
    pageObjectId=page_id,
    thumbnailProperties={
        "mimeType": "PNG",
        "thumbnailSize": "LARGE",
    },
).execute()

content_url = thumb["contentUrl"]
```

---

## 21. Checklist operativo para futuros agentes BMAD

Antes de tocar Google Slides en este proyecto:

1. Confirmar que el cambio pertenece a `edu-standalone` o a documentacion en `docs/`.
2. No modificar `_bmad/`.
3. Verificar scopes minimos necesarios.
4. Preferir copia de template antes que edicion directa.
5. Agrupar operaciones en `batchUpdate`.
6. Evitar depender de object IDs persistentes entre sesiones.
7. Usar `fields` en lecturas grandes.
8. Tratar `getThumbnail` como expensive read.
9. Implementar backoff ante `429`.
10. Si hay riesgo de carrera con ediciones manuales, usar `requiredRevisionId`.
11. Si el cambio agrega una nueva capacidad estable, documentarla en `docs/` y en prompts/agentes EDU correspondientes.

---

## 22. Fuentes oficiales consultadas

Referencia general:

- Google Slides API REST overview
- `presentations`
- `presentations.pages`
- `presentations.batchUpdate`
- `presentations.create`
- `presentations.get`
- `presentations.pages.get`
- `presentations.pages.getThumbnail`
- `presentations.request`
- Usage limits

Guias:

- Introduction / overview
- Create and manage presentations
- Create a slide
- Add shapes and text to a slide
- Size and position page elements
- Add images to a slide
- Merge data into a presentation
- Adding charts to your slides
- Editing and styling text
- Work with speaker notes
- Use field masks
- Configure OAuth consent screen and choose scopes

Nota final: la documentacion oficial consultada reporta actualizaciones entre febrero y marzo de 2026 para la mayor parte de las paginas clave, por lo que esta sintesis refleja el estado actual del API al 16/03/2026.
