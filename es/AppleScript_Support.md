<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked incluye un diccionario AppleScript para automatizar la vista previa, la exportación y la integración del flujo de trabajo. Puede abrir documentos, controlar la vista previa (recargar, desplazarse, resaltar, desplazamiento automático, lectura rápida), leer estadísticas, cambiar procesadores y estilos, copiar HTML o RTF al portapapeles y exportar a la mayoría de los mismos formatos disponibles en el menú {% appmenu File, Export %}. **La vista previa de encabezados/tabla de contenido a través de AppleScript está en proceso** (ver más abajo).

Para la automatización basada en URL (scripts de shell, `open` comandos y devoluciones de llamadas), consulte [Manejador de URL](URL_Handler.html). AppleScript y el controlador de URL se complementan entre sí: use AppleScript cuando necesite apuntar a un documento o ventana específica, y URL cuando una simple llamada `open 'x-marked://...'` sea suficiente.

## Ver el diccionario

En **Editor de secuencias de comandos**, elija {% appmenu File, Open Dictionary... %} y seleccione Marcado. El diccionario enumera comandos en los objetos **aplicación**, **documento** y **ventana**, además de comandos de exportación en el conjunto Marked.

En macOS, puede buscar definiciones de secuencias de comandos con **Editor de secuencias de comandos**.

## Orientación marcada

Para la instalación estándar:

```applescript
tell application "Marked"
	-- commands here
end tell
```

## Documentos y ventanas

**Aplicación**

- `documents` -- abrir documentos de vista previa (lista ordenada).
- `windows` -- ventanas de vista previa.

**Documento**

- `name` -- nombre para mostrar.
- `path` -- ruta del archivo cuando el documento se guarda en el disco.
- `modified` -- si el documento tiene cambios de editor no guardados.
- `processor` -- Procesador de rebajas para esta vista previa (lectura/escritura). Nombres válidos: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. La configuración `processor` aplica una anulación por documento y recarga la vista previa; no cambia el valor predeterminado global en {% prefspane Processor %}.
- `preprocessor` -- preprocesador para esta vista previa (lectura/escritura). Utilice `true` o `false` para habilitar o deshabilitar el preprocesador personalizado, o un nombre de preprocesador cuando corresponda.
- `source text` -- fuente de Markdown sin procesar (solo lectura).
- `critic markup mode` -- si el procesamiento CriticMarkup está habilitado (lectura/escritura). Al cambiarlo se recarga la vista previa.
- `is autoscrolling` -- si el desplazamiento automático está activo (solo lectura).
- `is speed reading` -- si el modo de lectura rápida está activo (solo lectura).
- Comandos de vista previa, lector, estadísticas y exportación (ver más abajo).

**Ventana**

- `document` -- el `MarkdownDocument` que se muestra en esa ventana.
- `style` -- nombre del estilo de vista previa actual (lectura/escritura). La configuración `style` recarga la vista previa con el tema elegido (igual que elegir un estilo del menú de estilos de vista previa).
- `close`, `save`, `print`: comandos de ventana estándar.
- Los mismos comandos de vista previa, lector, estadísticas y exportación que en los documentos (reenviados al documento de la ventana).

Prefiera `tell document 1` o `tell window 1's document` al exportar una vista previa específica. Los comandos de exportación en la aplicación utilizan la ventana clave o el documento actual cuando no se especifica ningún receptor.

### Ejemplo: abrir y leer ruta

```applescript
tell application "Marked"
	open POSIX file "/Users/you/Documents/report.md"
	set docPath to path of document 1
end tell
```

### Ejemplo: cambiar el estilo de vista previa

```applescript
tell application "Marked"
	tell window 1
		set style to "Amblin"
	end tell
end tell
```

Los nombres de los estilos coinciden con el menú de estilos de vista previa (nombre para mostrar, nombre del recurso CSS como `swiss` o identificador interno). Se admiten los estilos personalizados que agregó en el Administrador de estilos.

Utilice **`get preview style names`** en el objeto de la aplicación para enumerar los nombres para mostrar de estilos habilitados.

### Ejemplo: procesador y texto fuente

```applescript
tell application "Marked"
	tell document 1
		set processor to "Kramdown"
		set md to source text
		set critic markup mode to true
	end tell
end tell
```

## Comandos de la aplicación

Estos comandos se aplican al objeto **aplicación** (no a un documento específico).

| Comando | Descripción |
| --- | --- |
| `open streaming preview` | Abra una ventana [vista previa del portapapeles de transmisión](Streaming_Preview.html). |
| `preview clipboard` | Abra una [vista previa del portapapeles](Opening_Files.html) del contenido actual del portapapeles (igual que {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}). |
| `close all` | Cierre todos los documentos de vista previa abiertos (no se le pedirá que guarde; Marked no edita los archivos de origen). |
| `get available processors` | Enumere los nombres de los procesadores: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. |
| `get preview style names` | Enumere los nombres para mostrar del estilo de vista previa habilitado. |
| `get_available_formats` | Enumere los nombres de formato `convert_to` admitidos. |
| `get_available_profiles` | Enumere los nombres de los perfiles de exportación (igual que la propiedad `profiles`). |

Traiga Marcado al frente con el comando estándar AppleScript **`activate`**:

```applescript
tell application "Marked"
	activate
	open streaming preview
end tell
```

## Control de vista previa

Disponible en **documento** y **ventana**. La mayoría de estos requieren una vista previa de WebView cargada.

| Comando | Parámetros | Descripción |
| --- | --- | --- |
| `refresh preview` | — | Vuelva a cargar la vista previa desde el archivo fuente (igual que {% appmenu Preview, Refresh %}). |
| `reveal in finder` | — | Revela el archivo del documento en Finder. |
| `show highlights` | — | Habilite el resaltado de palabras clave (evite palabras, alternativas, voz pasiva, listas personalizadas). |
| `full screen` | opcional `enabled` booleano | Ingrese, salga o alterne el modo de vista previa de pantalla completa. |
| `scroll to heading` | `title` o `id` | Desplácese hasta un encabezado por texto de título visible o DOM `id`. |
| `scroll to position` | `percent` o `line` | Desplácese por porcentaje de altura del documento o número de línea aproximado. |
| `copy html` | — | Copie la vista previa de HTML al portapapeles (menú de ajustes o {% kbd shift cmd C %}; consulte [Copiar HTML](Exporting.html#copyhtml)). |
| `copy rtf` | — | Copie el texto enriquecido al portapapeles. |

```applescript
tell application "Marked"
	tell document 1
		refresh preview
		show highlights
		scroll to heading id "introduction"
		scroll to position percent 50
		full screen with enabled true
	end tell
end tell
```

## Desplazamiento automático y lectura rápida

| Comando | Descripción |
| --- | --- |
| `autoscroll` | Inicie el desplazamiento automático. El número entero `wpm` opcional establece palabras por minuto antes de comenzar. |
| `stop autoscroll` | Detener el desplazamiento automático. |
| `pause autoscroll` | Pausa o reanuda el desplazamiento automático. |
| `speed read` | Inicie o active [lectura rápida](Speed_Reading.html). |
| `stop speed read` | Detener la lectura rápida. |
| `pause speed read` | Pausar o reanudar la lectura rápida. |

Verifique el estado con las propiedades del documento `is autoscrolling` y `is speed reading`.

```applescript
tell application "Marked"
	tell document 1
		autoscroll with wpm 250
		-- or: speed read
	end tell
end tell
```

## Estadísticas

**`get statistics`** devuelve un `statistics_record` con valores numéricos calculados a partir de la fuente de Markdown actual (no las cadenas formateadas que se muestran en el cajón de estadísticas).

| Propiedad | Descripción |
| --- | --- |
| `word_count` | Recuento de palabras |
| `sentence_count` | Recuento de frases |
| `character_count` | Recuento de caracteres |
| `paragraph_count` | Recuento de párrafos |
| `average_words_per_sentence` | Promedio de palabras por oración |
| `average_syllables_per_word` | Promedio de sílabas por palabra |
| `complex_word_percentage` | Porcentaje de palabras complejas |
| `reading_ease` | Facilidad de lectura de Flesch |
| `fog_index` | Índice de niebla disparada |
| `grade_level` | Nivel de grado de Flesch-Kincaid |
| `gulpease` | Índice Gulpease (legibilidad en italiano; `0` cuando no aplicable) |
| `gulpease_band` | Banda Gulpease `1`–`4` (cuando corresponda) |
| `reading_time_minutes` | Tiempo de lectura a **250 palabras por minuto** |

```applescript
tell application "Marked"
	set stats to get statistics of document 1
	set wc to stats's word_count
	set fog to stats's fog_index
end tell
```

## Tabla de contenidos (trabajo en progreso)

{% note %}
**WIP: aún no es confiable.** El diccionario incluye una propiedad **`headings`** y un comando **`headings`** para leer encabezados de vista previa anidados (registros `heading_item`). Esta automatización **no funciona correctamente** en las compilaciones actuales (resultados vacíos, errores de coerción o "no se devolvió ningún resultado"). Se solucionará en una versión posterior. Prefiere **`scroll to heading`** con un título o identificación conocida hasta entonces.
{% endnote %}

**Comportamiento planificado** (cuando esté completo): `heading_item` registros anidados de encabezados en la **vista previa** (`h1`–`h6`), no de Markdown sin formato.

| Propiedad | Descripción |
| --- | --- |
| `title` | Texto del encabezado |
| `id` | Atributo DOM `id` (cadena vacía cuando está ausente) |
| `level` | Nivel de título `1`–`6` |
| `children` | Lista anidada de `heading_item` registros |

**`headings`** (propiedad del documento): todos los niveles. **`headings levels {2, 3}`** (comando) — filtro opcional: solo aquellas profundidades de rumbo (no un rango).

```applescript
-- Planned; do not rely on this yet
tell application "Marked"
	set toc to headings of document 1
	set filtered to headings levels {2, 3} of document 1
end tell
```

Utilice valores `id` con **`scroll to heading id "..."`** una vez que la automatización de encabezados sea estable.

## Imprimir con perfil

**`print with profile`** aplica temporalmente la configuración de impresión de un perfil de exportación y luego imprime el documento (el mismo paquete de preferencias que los perfiles de exportación de {% prefspane Export %}).

```applescript
tell application "Marked"
	tell document 1
		print with profile "Print Letter"
	end tell
end tell
```

Los nombres de los perfiles distinguen entre mayúsculas y minúsculas. Después de imprimir, Marked restaura el perfil de exportación previamente activo.

## Exportar perfiles

Los perfiles de exportación almacenan paquetes de preferencias de exportación/impresión (márgenes, encabezados, opciones de TOC y configuraciones similares de {% prefspane Export %}).

**Leer nombres de perfil**

```applescript
tell application "Marked"
	set profileList to profiles
	-- or: get_available_profiles
end tell
```

**Exportar con un perfil**

```applescript
tell application "Marked"
	tell document 1
		export html to "/Users/you/Desktop/report.html" with profile "My Profile"
	end tell
end tell
```

Los nombres de los perfiles distinguen entre mayúsculas y minúsculas y deben coincidir exactamente con un perfil guardado.

## Exportar comandos

Los comandos de exportación están disponibles en los objetos **aplicación**, **documento** y **ventana**. Cada comando requiere un parámetro **`to`** con la ruta de salida (cadena de ruta POSIX u objeto `file`).

| Comando | Salida |
| --- | --- |
| `export markdown` | Rebaja (.md) |
| `export html` | HTML |
| `export paginated pdf` | PDF paginado (diseño de impresión) |
| `export continuous pdf` | PDF de desplazamiento continuo |
| `export epub` | EPUB |
| `export docx` | Microsoft Word (.docx) |
| `export odt` | Texto de OpenDocument |
| `export textbundle` | Paquete de texto |
| `export rtf` | RTF |
| `export opml` | OPML |

**Notas**

- El PDF paginado utiliza el mismo canal de HTML a PDF que {% appmenu File, Export, Paginated PDF %}. No está disponible para documentos de vista previa HTML sin formato.
- La exportación HTML utiliza la **vista previa renderizada** (lo que se ve en WebView), no el archivo fuente sin formato de Markdown.
- PDF continuo captura el diseño de vista previa actual de WebView.

### Exportación básica

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Desktop/report.pdf"
	end tell
end tell
```

### Exportar rutas y sandboxing

- Utilice una ruta POSIX completa para el archivo de destino.
- Marked puede crear carpetas intermedias cuando la ruta de exportación está **dentro de la carpeta del documento abierto** (por ejemplo, exportar a `.../MyProject/build/output.pdf` mientras se obtiene una vista previa de `.../MyProject/chapter.md`).
- Las exportaciones fuera de la carpeta del documento requieren una ruta de escritura a la que pueda acceder Marked (ubicación del documento guardado, marcadores con alcance de seguridad o carpetas que haya otorgado a través de cuadros de diálogo Abrir). Si no se puede escribir en la ruta, el comando devuelve un error antes de que comience la exportación.

## `with` opciones (registro de propiedades)

En lugar de `with profile`, puedes pasar un registro de opciones usando **`with`** o **`with properties`**:

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in", fontSize:"14"}
```

AppleScript reconoce estas claves directamente (se asignan antes de la exportación):

| Clave | Descripción | Ejemplo |
| --- | --- | --- |
| `style` | Estilo de vista previa que se aplicará antes de la exportación (recarga de vista previa completa) | `"Amblin"`, `"Swiss"` |
| `pageSize` | Imprimir nombre del tamaño de página | `"A4"`, `"Letter"` |
| `margins` | Márgenes de impresión (ver más abajo) | `"1in"`, `"1in 2in"` |
| `fontSize` | Anular el tamaño de fuente base de exportación/impresión en puntos (PDF paginado y continuo) | `"14"`, `"12pt"` |

`fontSize` habilita la misma opción **Tamaño de fuente personalizado para exportar/imprimir** desde {% prefspane Export %}. No afecta a los documentos de Fountain, que utilizan un tamaño de guión fijo.

Cuando se incluye `style`, Marked aplica ese tema, espera a que la vista previa termine de recargarse y luego exporta. No necesita un paso `set style` por separado.

Otras claves en el registro pueden coincidir con nombres de **preferencias de exportación** de perfiles (las mismas claves almacenadas en {% prefspane Export %}, como `printBackgrounds`, `printTOC`, `topPrintMargin`). Esos valores se aplican temporalmente para la exportación.

No puedes combinar fuentes conflictivas descuidadamente: si usas `with profile`, carga ese perfil primero; Si usa un registro `with`, las claves de perfil en el registro anulan la configuración actual para esa exportación.

### Taquigrafía de margen

El valor `margins` es una cadena con una a cuatro medidas. Unidades: `in`, `cm`, `mm`, `pt` o `"` para pulgadas. Un número sin unidad se trata como puntos.

| Valores | Significado |
| --- | --- |
| `1in` | Todos los lados |
| `1in 2in` | Arriba y abajo `1in`, izquierda y derecha `2in` |
| `1in 2in 1in` | Arriba `1in`, izquierda y derecha `2in`, abajo `1in` |
| `1in 2in 1in 2in` | Arriba, derecha, abajo, izquierda |

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in 2in"}
export paginated pdf to "/path/out.pdf" with {style:"Amblin", margins:"1in 2in 1in 2in"}
```

### Ejemplo combinado

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Documents/MyBook/build/book.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

## `convert_to`

El objeto de aplicación también expone comandos de secuencias de comandos heredados:

- **`convert_to`**: convierte texto Markdown o una ruta de archivo a un formato (`html`, `pdf`, `epub`, `docx`, `rtf` y otros), opcionalmente con `profile` y `output_path`.
- **`get_available_formats`**: enumera los nombres de formatos de conversión admitidos.
- **`get_available_profiles`**: enumera los nombres de los perfiles de exportación (igual que la propiedad `profiles`).

`convert_to` permanece disponible para flujos de trabajo más antiguos y automatización exclusiva de AppleScript.

## Depuración

Habilite el **modo de depuración** en {% prefspane Advanced %} (o la preferencia de depuración en Configuración). Luego, Marked registra los pasos de exportación de AppleScript en el nivel de información con el prefijo `[AppleScript]` en Console.app y el visor de registros de Marked.

Líneas de registro útiles al rastrear una exportación de PDF paginado:

- `paginated PDF: fetching preview HTML`
- `HTMLToPDFGenerator: loadHTMLString`
- `HTMLToPDFGenerator: didFinishLoadForFrame`
- `paginated PDF: generator finished`

Las exportaciones largas (especialmente PDF paginados) suspenden el evento AppleScript hasta su finalización para que los clientes no pierdan el tiempo de espera a mitad de la exportación.

## Errores

Las exportaciones fallidas establecen la cadena de error del script en el comando (visible en el Editor de scripts y en los controladores `on error`). Mensajes comunes:

- Se requiere ruta de exportación.
- El directorio de exportación no existe (fuera de la carpeta de documentos).
- No se puede crear el directorio de exportación o se produce un error de permiso al escribir el archivo.
- Nombre de estilo de vista previa desconocido.
- Se agotó el tiempo de espera para que se recargara la vista previa después del cambio de estilo.
- La exportación de PDF paginado agotó el tiempo de espera o falló al generar páginas.

## Integración con otras herramientas

Las aplicaciones pueden utilizar la superficie AppleScript de Marked para leer metadatos de documentos. Para la aplicación Atajos, consulte [Integración de atajos](Shortcuts_Integration.html). Para flujos de trabajo controlados por shell, observadores de carpetas y devoluciones de llamadas del editor, el [Manejador de URL](URL_Handler.html) suele ser más simple. El [Paquete de bonificación marcado](Workflow_Integration.html#marked-bonus-pack) incluye scripts y servicios adicionales.