<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

El controlador de URL de Marked proporciona capacidades adicionales de secuencias de comandos y flujo de trabajo. Puedes incluir una URL en las notas de otra aplicación, por ejemplo, que abrirá un archivo en Marcado al hacer clic. Puede realizar varias acciones, como se enumeran a continuación.

## El esquema de URL

El esquema de URL de Marked es `x-marked`, llamado con opciones como `x-marked://open?file=/Users/username/Desktop/report.md`.

Puedes apuntar específicamente a Marked 3 usando `x-marked-3` en lugar de `x-marked`. Los métodos y parámetros son exactamente los mismos que `x-marked`, pero solo Marked 3 responderá a `x-marked-3`.

## Llamar desde la línea de comando/scripts

Se puede llamar al controlador de URL desde la línea de comando o desde un script usando macOS [`open` comando](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/):

	abra 'marcado con x://open?file=nombre de archivo.md'
	abra 'marcado con x: //refresh?file=nombre de archivo.md'

### Llamando en segundo plano

Puede llamar al comando `open` con la bandera `-g` para realizar el resultado en segundo plano sin cambiar el foco. Para ejecutar el comando en segundo plano y elevar la ventana a la parte superior sin robar el foco:

	open -g 'marcado con x://open?file=nombre de archivo.md&raise=true'

## Parámetros opcionales

### x-éxito

Cualquier comando puede proporcionar un parámetro de consulta **x-success**. Establezca esto en una URL a la que se llamará después de ejecutar el comando. Por ejemplo: `x-marked://open/?file=filename.md&x-success=ithoughts:`. También puedes proporcionar un identificador de paquete (como `com.googlecode.iterm`) para abrir una aplicación que no tiene un esquema de URL.

### aumentar

Se puede pasar un parámetro **raise** con cualquier comando que acepte un parámetro `file` o afecte a todas las ventanas. Después de realizar la acción, las ventanas afectadas se elevarán por encima de todas las demás ventanas (todas las aplicaciones) antes de devolver o ejecutar una devolución de llamada.

	"marcado con x: //refresh?file=nombre de archivo.md&raise=true"

### lectura rápida

Se puede pasar un parámetro **speedread** con comandos del controlador de URL que abren un documento de vista previa (`open`, `paste`, `preview` y `stream`). Configure `speedread=1` para iniciar automáticamente la lectura rápida tan pronto como la vista previa del objetivo esté lista.

Ejemplos:

	marcado con x://open?file=/Users/username/Desktop/report.md&speedread=1

	marcado con x://preview?text=Some%20text&speedread=1

	marcado con x://paste?speedread=1

# Comandos disponibles

Los siguientes comandos están disponibles para el controlador de URL `x-marked`.

## agregar estilo

Agregue un nuevo estilo personalizado a Marcado.

##### Parámetros:

**css**: texto CSS codificado en URL para escribir en un estilo personalizado. Obligatorio a menos que se pase un parámetro **archivo**.

**archivo**: ruta completa (POSIX) a un archivo CSS para agregar a Marked. Requerido a menos que se pase un parámetro **css**.

**nombre**: El nombre del estilo a generar.

Con el parámetro **css**, esto se usará como nombre de archivo al escribir en el disco, con ".css" agregado, y como nombre del elemento del menú. Es obligatorio para el parámetro **css** y opcional para **archivo** (el nombre de archivo se utilizará como si el parámetro de nombre estuviera vacío).

	marcado con x://addstyle?name=Mi+nuevo+estilo&css=...

	marcado con x://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

Si incluye un nombre con el parámetro de archivo, el elemento del menú obtendrá ese nombre en lugar del nombre del archivo. Si vuelve a utilizar el mismo nombre con una ruta diferente, el elemento del menú se actualizará con la nueva ruta en lugar de agregar un segundo elemento con el mismo nombre.

## valores predeterminados

Establecer la configuración del usuario. Acepta una lista de claves y valores como parámetros de consulta. Sólo se establecerán las claves existentes. Si el cambio de preferencia requiere una actualización, todas las ventanas se actualizarán automáticamente a menos que se pase `refresh=0`.

Utilice 1 para verdadero y 0 para falso en valores booleanos.

##### Parámetros:

**actualizar** _(opcional)_: si se establece en 0, la actualización automática de las ventanas de vista previa abiertas está deshabilitada

* Predeterminado: 1 (verdadero)

##### Ejemplo:

marcado con x://defaults?syntaxHighlight=1&includeMathJax=0

El método `defaults` está diseñado principalmente para que el desarrollador pueda agregar enlaces a funciones esotéricas que de otro modo no estarían disponibles en Configuración. Sin embargo, es posible que haya algunas opciones estándar que quieras alternar al automatizar. Algunas configuraciones comunes que quizás quieras controlar durante la automatización:

sintaxisResaltar
: habilitar o deshabilitar el resaltado de sintaxis

incluirMathJax
: habilita o deshabilita el manejo interno de MathJax

procesador
: establezca en `multimarkdown` o `mmd` para cambiar el procesador a MultiMarkdown, `discount` o `gfm` para usar el procesador de descuento

h1IsPageBreak, h1IsPageBreak, breakBeforeFootnotes
: Saltos de página automáticos en la exportación antes de los niveles de encabezado 1 y 2 y notas al pie.


## dingus

Abra Markdown Dingus para probar diferentes procesadores Markdown.

	marcado con x://dingus

##### Parámetros:

**procesador** (opcional): especifique qué procesador seleccionar de forma predeterminada. Valores válidos:

- `multimarkdown` - Procesador MultiMarkdown
- `commonmark` - Procesador CommonMark (GFM)
- `discount` o `discount (gfm)` - Procesador de descuentos
- `kramdown` - Procesador Kramdown

Ejemplos:

- `x-marked://dingus?processor=kramdown` - Se abre con Kramdown seleccionado
- `x-marked://dingus?processor=commonmark` - Se abre con CommonMark (GFM) seleccionado

*Nota:* Esto abre la ventana Markdown Dingus, que le permite probar y comparar diferentes procesadores Markdown (MultiMarkdown, CommonMark (GFM), Discount y Kramdown) uno al lado del otro. Perfecto para experimentar con la sintaxis de Markdown y comprender las diferencias del procesador.

## ladrón de estilos / robar

Abre el HUD del ladrón de estilos. Útil cuando desea capturar CSS de una página activa o ejecutar una sesión de extracción de contenido manual sin iniciarla a través de la interfaz de usuario.

	Sinónimos: marcado x://robarestilos… , marcado x://robar…

##### Parámetros:

**url** _(opcional)_: una URL para completar previamente en la ventana Style Stealer. Si se omite, el HUD se abre en blanco.

Ejemplos:

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl / markdownify

Abra la ventana "Importar URL" (Extractor de contenido) para poder ejecutar la canalización de Markdownifier manualmente. Esto **no** realiza la extracción automáticamente; eso se maneja con el comando `extract` a continuación.

	Sinónimos: x-marked://importurl… , x-marked://markdownify…

##### Parámetros:

**url** _(opcional)_: rellena previamente el campo URL de importación. Si se omite, la ventana se abre con un campo vacío esperando que pegue un enlace.
**html** _(opcional, solo markdownify)_: cuando se proporciona en `x-marked://markdownify`, debe ser HTML sin formato codificado en URL. Marked convertirá el HTML a Markdown usando las mismas reglas que la Vista previa del portapapeles y lo abrirá en un documento transitorio, como si hubiera pegado ese HTML en una ventana de Vista previa del portapapeles.

Ejemplos:

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## hacer

Ejecute un comando de JavaScript en una ventana de documento. Toda la API de JavaScript de Marked está [documentada aquí](https://markedapp.com/help/jsapi/).

##### Parámetros:

**js** _(obligatorio)_: cadena de consulta que contiene un comando de JavaScript

* Acepta parámetros de ruta que hacen referencia a nombres de archivos, o "todos"
* Las rutas divididas por / buscarán en varios archivos
* Los nombres de archivos parciales completarán la mejor coincidencia

		marcado con x: //do/nombre de archivo1/nombre de archivo2?js=...
		marcado con x://do/all?js=...

**archivo**: parámetro de consulta que contiene rutas/nombres de archivo separados por comas

	marcado con x://do?file=nombredearchivo1,nombredearchivo2&js=...

Operará en la ventana del frente si no se proporciona un nombre de archivo (o no se pasa "todos")

## ayuda

Abra el sistema de ayuda interno Marcado, especificando opcionalmente un tema. Esto es principalmente para uso interno, pero se puede acceder a él a través de URL. Se puede copiar una URL a cualquier sección determinada haciendo clic derecho en el icono de marcador a la derecha de un título y seleccionando __Copiar enlace__. **La ayuda y la búsqueda en la aplicación de Marked 3** utilizan el esquema `x-marked-3` para estos enlaces para que macOS los abra en Marked 3 cuando Marked 2 también esté instalado; los ejemplos siguientes utilizan esa forma.

##### dingus

Abra Markdown Dingus para probar diferentes procesadores Markdown.

	marcado con x://dingus

######## Parámetros:

**procesador** (opcional): especifique qué procesador seleccionar de forma predeterminada. Valores válidos:

- `multimarkdown` - Procesador MultiMarkdown
- `commonmark` - Procesador CommonMark (GFM)
- `discount` o `discount (gfm)` - Procesador de descuentos
- `kramdown` - Procesador Kramdown

Ejemplos:

- `x-marked://dingus?processor=kramdown` - Se abre con Kramdown seleccionado
- `x-marked://dingus?processor=commonmark` - Se abre con CommonMark (GFM) seleccionado

*Nota:* Esto abre la ventana Markdown Dingus, que le permite probar y comparar diferentes procesadores Markdown (MultiMarkdown, CommonMark (GFM), Discount y Kramdown) uno al lado del otro. Perfecto para experimentar con la sintaxis de Markdown y comprender las diferencias del procesador.

##### Parámetros:

**página** _(opcional)_: el título exacto de una página existente, con hash de anclaje opcional

	x-marked-3://help?page=Document_Statistics

Los espacios se reemplazan con guiones bajos, según la convención de nomenclatura de archivos de ayuda marcados. Se pueden utilizar dos puntos (:) en lugar de una almohadilla (#) al especificar un ancla.

El destino puede especificarse únicamente mediante la ruta (sin cadena de consulta):

	x-marked-3://help/Keyword_Highlighting:editingkeywords


## extraer

Extraiga contenido de una URL web y ábralo como un documento nuevo en Marcado.

	marcado con x://extract?url=https://example.com

##### Parámetros:

**url** _(obligatorio)_: la URL web de la que extraer contenido. Debe comenzar con `http://` o `https://`

**ventana** _(opcional)_: Nombre de la ventana

**id** _(opcional)_: identificador del espacio de nombres

**base** _(opcional)_: URL base para enlaces relativos

**levantar** _(opcional)_: establezca en `true` para elevar la ventana después de abrirla

**manual** _(opcional)_: Establezca en `true` para abrir la ventana de extracción manual de Style Stealer en lugar de realizar la extracción automática.

- Cuando `manual=true`, Marked abre Style Stealer, completa previamente el campo URL (si se proporciona), suprime cualquier cuadro de diálogo Abrir automático y le permite seleccionar y extraer estilos/contenido de forma interactiva antes de guardar.
- Cuando se omite o `false`, Marked ejecuta el extractor automático (Markdownifier) ​​y abre el resultado directamente como un nuevo documento temporal.

##### Ejemplos:

	marcado con x://extract?url=https://news.ycombinator.com

	marcado con x://extract?url=https://github.com&window=GitHub&raise=true

	marcado con x://extract?url=https://example.com/article&manual=true

	marcado con x://extract?url=https://blog.example.com/post-title

*Nota:* Este comando utiliza el servicio de extracción de contenido de Marked para buscar páginas web, extraer contenido limpio usando Readability, convertir al formato Markdown y abrir el resultado en un nuevo documento temporal. El contenido extraído incluye metadatos (título, URL de origen, fecha) y tiene el formato Markdown limpio. Perfecto para capturar y editar rápidamente contenido web.

## abierto

Abre el documento especificado en Marcado.

	marcado con x://open?file=/Users/username/Desktop/report.md

##### Parámetros:

**archivo** *(obligatorio)*: la ruta POSIX completa al documento que se va a abrir, o una lista de rutas separadas por comas

**speedread** *(opcional)*: configúrelo en `1` para iniciar la lectura rápida automáticamente después de abrir.

`open` también acepta una ruta cuyos componentes se combinarán en una única URL

	marcado con x://open/~/nvALT2.2

Si la ruta del archivo proporcionada no existe o no se puede abrir, Marked seguirá estando en primer plano. Ejecutarlo sin el parámetro *archivo* o con un valor en blanco simplemente abrirá Marcado.

Marked también abrirá archivos si solo se llama a la ruta de un archivo en el controlador de URL, p. `x-marked:///Users/username/Desktop/report.md`.

## pegar

Cree un nuevo documento a partir del contenido actual del portapapeles.

	marcado con x://pegar

##### Parámetros:

**speedread** *(opcional)*: Establezca en `1` para iniciar la lectura rápida automáticamente después de abrir la vista previa del portapapeles.

*Nota:* Esto crea un documento temporal usando el comando "Vista previa del portapapeles". Cualquier texto en su portapapeles se agrega a un documento nuevo en blanco, que luego se abre en Marcado. Si se cierra sin guardar, se descarta.

## vista previa

Vista previa del texto especificado en un documento nuevo.

	marcado con x://preview?text=Some%20text%20to%20%2A%2Apreview%2A%2A%0A

##### Parámetros:

**texto** *(obligatorio)*: El texto que se insertará en la vista previa. El texto codificado por porcentaje se descodificará antes de ver el documento.

**lectura rápida** *(opcional)*: configúrelo en `1` para iniciar la lectura rápida automáticamente después de abrir el texto de vista previa.

## corriente

Abra una ventana de vista previa del portapapeles de transmisión.

	marcado con x://corriente

##### Parámetros:

**speedread** *(opcional)*: configúrelo en `1` para iniciar la lectura rápida automáticamente después de abrir la vista previa de la transmisión.

*Nota:* Esto crea un documento temporal usando el comando "Vista previa del portapapeles". El texto pasado se agrega a un documento nuevo en blanco, que luego se abre en Marcado. Si se cierra sin guardar, se descarta.

## actualizar

Actualizar una vista previa del documento o todas las vistas previas abiertas.

##### Parámetros:

**archivo**: parámetro de consulta que contiene rutas/nombres de archivo separados por comas (los archivos deben estar abiertos actualmente en Marcado). Llamar sin parámetro `file` o `?file=all` actualizará todas las ventanas abiertas.

El parámetro *archivo* puede ser parcial. Marcado actualizará todas las ventanas abiertas con una coincidencia parcial en el *nombre de archivo* (no la ruta completa). Al pasar "todos", se actualizarán todas las ventanas.

	marcado con x://actualizar

	marcado con x://refresh?file=/Users/username/Desktop/report.md

	marcado con x://refresh?file=report.md

Si se llama sin ningún parámetro `file` pero con rutas de documentos especificadas en la URL, las rutas divididas por / buscarán varios archivos y los nombres de archivos parciales completarán la mejor coincidencia.

	marcado con x://actualizar/nombre de archivo1/nombre de archivo2

## estilo

Establezca el estilo de vista previa (CSS) para uno o más documentos.

##### Parámetros:

**css** _(obligatorio)_: cadena de consulta que contiene el nombre o ruta de un estilo. Los estilos deben estar presentes en el menú de estilos de Marked como estilos predeterminados o personalizados agregados manualmente.

* Acepta parámetros de ruta que hacen referencia a nombres de archivos, o "todos"
* Las rutas divididas por / buscarán en varios archivos
* Los nombres de archivos parciales completarán la mejor coincidencia

		marcado con x://estilo/nombre de archivo1/nombre de archivo2?css=...
		marcado con x://style/all?css=...

**archivo**: parámetro de consulta que contiene rutas/nombres de archivo separados por comas

	marcado con x://style?file=filename1,filename2&css=...

Este método funcionará en la ventana del frente si no se proporciona un nombre de archivo (o si no se pasa "todo").