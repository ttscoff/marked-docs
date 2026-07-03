<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked incluye acciones nativas de **Atajos** (App Intents) para abrir archivos, cambiar estilos de vista previa y exportar documentos. Estas acciones aparecen en la aplicación Atajos cuando buscas **Marcado** y están disponibles en **macOS 13 (Ventura)** o posterior.

Para la automatización basada en scripts con un modelo de objetos completo, consulte [Soporte de AppleScript](AppleScript_Support.html). Para flujos de trabajo basados ​​en URL desde el shell, consulte [Manejador de URL](URL_Handler.html).

## Encontrar acciones

1. Abra la aplicación **Atajos**.
2. Cree un nuevo acceso directo o edite uno existente.
3. Busque **Marcado** en la biblioteca de acciones.

Las acciones se agrupan en **Documentos** y **Exportar**. Marked también registra frases de Siri como "Exportar archivo con Marked" y "Abrir en Marked" para atajos rápidos.

## Resumen de acciones

| Acción | Propósito |
| --- | --- |
| **Abrir archivo en Marcado** | Abra un archivo de Markdown o de texto en una ventana de vista previa. |
| **Establecer estilo de vista previa** | Cambie el tema de vista previa de un documento abierto (o abra un archivo primero). |
| **Abrir y exportar archivo** | Abra un archivo y luego expórtelo a otro formato. |
| **Documento de exportación** | Exportar un documento abierto (ventana frontal o un archivo específico). |
| **Exportar documentos abiertos** | Exporte todos los documentos actualmente abiertos en Marked. |

Todas las acciones de exportación devuelven el archivo (o archivos) exportados como accesos directos **Archivo** para que pueda pasarlos al siguiente paso (Correo, Finder, otra aplicación).

## Abrir archivo en marcado

**Parámetro:** **Archivo**: el documento que se va a abrir (desde Finder, Hoja para compartir o un paso de Accesos directos anterior).

Marcado abre el archivo en una ventana de vista previa. Utilízalo cuando quieras obtener una vista previa o editar en Marcado antes de hacer cualquier otra cosa.

## Establecer estilo de vista previa

**Parámetros:**

- **Estilo**: vista previa del estilo desde un selector (los mismos nombres que el menú de estilo de vista previa y el Administrador de estilos).
- **Archivo** (opcional): un archivo específico. Si se omite, Marked utiliza el documento frontal. Si el archivo aún no está abierto, Marked lo abre primero.

Al establecer un estilo, se recarga la vista previa con ese tema (igual que elegir un estilo en el menú de estilos de vista previa).

## Exportar acciones

Las acciones de exportación comparten las mismas opciones principales:

| Parámetro | Descripción |
| --- | --- |
| **Formato** | Markdown, HTML, PDF paginado, PDF continuo, EPUB, DOCX, ODT, RTF, RTFD, TextBundle, TextPack u OPML. |
| **Perfil** (opcional) | Un perfil de exportación guardado de {% prefspane Export %}. |
| **Estilo** (opcional) | Estilo de vista previa que se aplicará antes de la exportación (recarga de vista previa completa). |
| **Tamaño de página** (opcional) | Imprima el nombre del tamaño de la página, como `A4` o `Letter`. |
| **Márgenes** (opcional) | Taquigrafía de margen (ver más abajo). |
| **Tamaño de fuente** (opcional) | Tamaño de fuente base en puntos para la exportación de PDF, como `14` o `12pt`. |
| **Archivo de salida** / **Carpeta de salida** (opcional) | Ruta de destino. Si se omite, Marked escribe junto al archivo fuente usando la extensión correcta. |

**Notas**

- **PDF paginado** utiliza el mismo proceso de diseño de impresión que {% appmenu File, Export, Paginated PDF %}. No está disponible para documentos de vista previa HTML sin formato.
- La exportación **HTML** utiliza la vista previa renderizada (lo que se ve en WebView), no el archivo fuente de Markdown sin formato.
- **PDF continuo** captura el diseño de vista previa actual de WebView.
- **Tamaño de fuente** habilita la misma opción personalizada de tamaño de fuente para exportar/imprimir desde {% prefspane Export %}. No afecta a los documentos de Fountain.

### Abrir y exportar archivo

Lo mejor para los flujos de trabajo de Finder: elija un archivo Markdown, ábralo en Marked y expórtelo en un solo paso.

**Parámetros:** **Archivo** (obligatorio), más las opciones de exportación anteriores.

Uso de ejemplo: una acción rápida que toma archivos del Finder y exporta **PDF paginado** con un perfil y estilo elegidos.

### Exportar documento

Exporte un documento que **ya esté abierto** en Marcado.

**Parámetros:**

- **Archivo** (opcional): un archivo abierto específico. Si se omite, Marked exporta el documento frontal.
- Opciones de exportación y **Archivo de salida** como arriba.

Úselo cuando Marked ya se esté ejecutando y desee exportar la vista previa actual sin volver a abrir el archivo.

### Exportar documentos abiertos

Exporte **todos** los documentos de vista previa abiertos actualmente en Marked.

**Parámetros:**

- **Formato** y opciones de exportación (perfil, estilo, tamaño de página, márgenes, tamaño de fuente).
- **Carpeta de salida** (opcional): directorio para archivos exportados. Si se omite, cada archivo se exporta junto a su documento de origen.

Útil para la exportación por lotes después de revisar varios capítulos o notas en Marcado.

## Taquigrafía de margen

Cuando se configura **Márgenes** en una acción de exportación, utilice una cadena con una a cuatro medidas. Unidades: `in`, `cm`, `mm`, `pt` o `"` para pulgadas. Un número sin unidad se trata como puntos.

| Valor | Significado |
| --- | --- |
| `1in` | Todos los lados |
| `1in 2in` | Arriba y abajo `1in`, izquierda y derecha `2in` |
| `1in 2in 1in` | Arriba `1in`, izquierda y derecha `2in`, abajo `1in` |
| `1in 2in 1in 2in` | Arriba, derecha, abajo, izquierda |

Esto coincide con la clave `margins` en [AppleScript](AppleScript_Support.html#with-options-properties-record) registros de exportación.

## Flujos de trabajo de ejemplo

### Archivo del buscador a PDF

1. **Abrir y exportar archivo**
2. **Archivo**: entrada desde Hoja para compartir o Acción rápida del Finder.
3. **Formato**: PDF paginado.
4. **Estilo**: tema opcional (por ejemplo, Amblin).
5. **Perfil**: perfil de exportación guardado opcional.
6. **Archivo de salida** -- opcional; déjelo vacío para escribir `filename.pdf` junto a la fuente.

### Exportar lo que está abierto en Marcado

1. **Documento de exportación**
2. Deje **Archivo** vacío para usar la ventana frontal.
3. Elija **Formato** y perfil o estilo opcional.

### Exportar por lotes documentos abiertos

1. **Exportar documentos abiertos**
2. Elija **Formato** (por ejemplo EPUB).
3. Opcionalmente, configure **Carpeta de salida** para recopilar todas las exportaciones en un directorio.

### Estilo y luego exportar (dos pasos)

1. **Establecer estilo de vista previa**: elija un estilo (opcionalmente, seleccione un **Archivo** específico).
2. **Exportar documento**: el mismo archivo o documento frontal, con el **Formato** deseado.

También puedes pasar **Estilo** directamente en una acción de exportación; Marked aplica el tema y espera a que se vuelva a cargar la vista previa antes de exportar.

## Exportar rutas y sandboxing

- Si se omite **Archivo de salida** o **Carpeta de salida**, Marcado escribe junto al documento de origen.
- Marked puede crear carpetas intermedias cuando la ruta de exportación está **dentro de la carpeta del documento abierto**.
- Las exportaciones fuera de la carpeta del documento requieren una ruta de escritura a la que pueda acceder Marked (ubicación del documento guardado, marcadores con alcance de seguridad o carpetas que haya otorgado a través de cuadros de diálogo Abrir).

Consulte [Soporte de AppleScript](AppleScript_Support.html#export-paths-and-sandboxing) para conocer las mismas reglas de la zona de pruebas.

## Legado `convert_to` acción

El diccionario AppleScript todavía expone **`convert_to`** para convertir texto o archivos Markdown sin una vista previa abierta. Se prefieren las acciones de accesos directos nativos anteriores: abren documentos correctamente, esperan la carga de la vista previa y admiten la exportación de PDF paginados de forma asincrónica.

Consulte [Atajos y `convert_to` en compatibilidad con AppleScript](AppleScript_Support.html#shortcuts-and-convert_to) para obtener detalles sobre el comando heredado.

## Solución de problemas: acciones que no aparecen en los accesos directos

Índices de accesos directos **uno** Instalación marcada por identificador de paquete (`com.brettterpstra.marked`). Prefiere la copia con el **número de compilación más alto** (`CFBundleVersion`), no necesariamente la aplicación que acabas de crear en Xcode.

Si Marcado no aparece en **Aplicaciones** en la biblioteca de acciones de Accesos directos:

1. Enumere cada copia en el disco:
   ```golpecito
   mdfind 'kMDItemCFBundleIdentifier == "com.brettterpstra.marked"'
   ```
2. Elimine o cambie el nombre de las copias obsoletas (por ejemplo, una antigua `Marked.app` en el escritorio o en `/Applications` que se copió de una compilación **sin** metadatos de accesos directos).
3. Ejecute la compilación que desea que utilicen los accesos directos (Xcode **Ejecutar** o abra `.app` en DerivedData directamente).
4. Salga y vuelva a abrir la aplicación **Atajos**.

Una compilación que incluye accesos directos contiene `Contents/Resources/Metadata.appintents`. Puedes verificar:

```bash
ls "/path/to/Marked.app/Contents/Resources/Metadata.appintents"
```

Al iniciarse, Marked registra `[MKShortcuts] Registering App Intents` en Console.app cuando se ejecuta el registro (macOS 13+).

## Depuración

Habilite el **modo de depuración** en {% prefspane Advanced %}. Los registros marcados exportan pasos a nivel de información con el prefijo `[AppleScript]` en Console.app y el visor de registros de Marked (la canalización de exportación se comparte con AppleScript).

## Errores

Mensajes comunes cuando una acción falla:

- No hay ningún documento marcado disponible (no hay nada abierto ni ningún archivo especificado).
- Ese archivo no está abierto en Marcado (use **Abrir archivo** o **Abrir y exportar archivo**).
- Perfil de exportación desconocido o nombre de estilo de vista previa.
- Se agotó el tiempo de espera para que se cargue o recargue la vista previa.
- Errores de permiso de ruta de exportación o falla en la generación de PDF paginado.