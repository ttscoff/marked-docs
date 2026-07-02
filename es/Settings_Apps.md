<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opciones en el {% prefspane Apps %}:

(Consulte [Soporte adicional para aplicaciones](Additional_Application_Support.html))

![Configuración: Aplicaciones][1]

[1]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Configuración general

Editor de texto
: seleccione un editor de texto para recibir el documento actual cuando escriba {% kbd cmd E %}.

Editar nuevos archivos automáticamente
: Al utilizar el comando "Nuevo archivo", esta opción abrirá automáticamente el archivo creado en el editor externo elegido.

Los enlaces a archivos de texto deben abrirse en:
: determina el comportamiento de Marked cuando se hace clic en un enlace en una ventana de vista previa que conduce a un archivo de texto local.

Editor de imágenes
: Seleccione una aplicación para abrir cuando se haga clic derecho en una imagen local y se seleccione "Editar imagen".

Editor de anotaciones/marcas de imágenes
: Seleccione una aplicación para abrir cuando se haga clic derecho en una imagen local y se seleccione "Anotar imagen".

Si no se elige ningún editor, Marked presenta un menú de aplicaciones instaladas cuando edita o anota. El menú incluye herramientas comunes de Markdown, imágenes y anotaciones que se encuentran en su Mac, una opción **Otro...** para elegir cualquier aplicación de `/Applications` y **Usar siempre esta aplicación** (habilitada de forma predeterminada) para guardar su elección como predeterminada. Utilice el botón de borrar (círculo con una X) al lado de cada control Elegir en {% prefspane Apps %} para eliminar una selección y volver al selector.

### Configuración específica de la aplicación

Mostrar comentarios y anotaciones de forma predeterminada
: Si está marcada, las anotaciones realizadas en documentos de Scrivener, Fountain, Word y CriticMarkup aparecerán resaltadas en la vista previa. Desmarque para ocultar completamente. También se pueden alternar mientras se lee un documento desde el menú {% appmenu Gear, Proofing ({{ctrl}}{{cmd}}C)%}.
: Cuando los comentarios están habilitados, los comentarios y las notas al pie aparecerán en una barra lateral. Al pasar el cursor sobre un comentario, se indicará dónde aparece en el documento.

#### DocC

[(Información sobre soporte DocC)](DocC_Support.html)

Resolver referencias de imágenes DocC
: Dentro de un catálogo de documentación `.docc`, resuelva referencias `![](ImageName)` sin extensión a imágenes en la carpeta del catálogo `Resources`, incluidas las variantes `~dark` y `@2x`.

Resolver variantes de imagen oscura y @2x
: Para imágenes locales con una extensión de archivo (`images/icon.png`), detecta archivos complementarios `~dark` y `@2x` en la misma carpeta y emite un marcado `<picture>` responsivo. Funciona en cualquier documento Markdown o HTML, no solo en catálogos DocC. Consulte [Variantes de imagen](Image_Variants.html).

#### Marca de gancho

Resolver URL hook:// en imágenes y enlaces
: Marked puede leer las URL creadas por Hookmark y resolverlas en su ruta en el disco.

#### Leanpub/GitBook

Habilitar el soporte Leanpub
: Interprete los archivos denominados `Book.txt` como archivos de índice y maneje la sintaxis especial de Leanpub.

Habilitar la compatibilidad con GitBook
: Interprete los archivos denominados `SUMMARY.md` como archivos de índice para la documentación de GitBook.

#### Rebajador

Utilice enlaces en línea
: Los documentos de Markdown creados por Markdownifier utilizarán enlaces en línea en lugar de enlaces de referencia.

#### Marte

Incluir el título de la publicación como encabezado de Markdown (h1)
: utilice el título de la publicación seleccionada como encabezado de Markdown.

Mostrar metadatos como tabla
: Cuando está habilitado, los metadatos como categorías y títulos se mostrarán como una tabla Markdown en la vista previa.

#### Carpetas

Solo obtenga una vista previa de estas extensiones
: Al abrir una carpeta, Marked buscará el documento modificado más recientemente, y de forma predeterminada utilizará extensiones como `md`, `mmd` y `html`. La lista aquí anula la predeterminada.

#### Escribano

[(Información sobre soporte de Scrivener)](Scrivener_Support.html)

Incluir títulos de documentos como encabezados de Markdown
: analiza el título de las páginas y las páginas anidadas para crear encabezados jerárquicos de Markdown.

Agregue metadatos de compilación (título, autor) cuando falten
: Cuando un proyecto de Scrivener no tiene ningún documento `metadata` o un encabezado MultiMarkdown existente, anteponga Título y Autor desde la configuración de compilación del proyecto (`Settings/compile.xml`).

Abra archivos .scriv en Scrivener cuando se abran en Marked
: Cuando se abre un documento de Scrivener en Marked, también se abre automáticamente en Scrivener.

#### Palabra

Convertir seguimiento de cambios <-> CriticMarkup
: Si está habilitado, el seguimiento de cambios en documentos de Word se convertirá a CriticMarkup cuando se importen, y CriticMarkup se convertirá a seguimiento de cambios de Word al exportar archivos DOCX.

#### Mapas mentales/esquemas {#MindMapsOutlines}

Insertar como mapas mentales de sirena
: Cada casilla controla un formato incluido. Cuando está **activado**, el archivo incluido se convierte en un diagrama de mapa mental de Sirena (diseño de árbol ordenado). Cuando está **desactivado**, Marked usa la alternativa para ese formato.
: **Mapas mentales** — iThoughts X (.itmz), MindManager (.mmap), FreeMind (.mm). Si está activado: mapa mental de sirena. Si está desactivado: iThoughts incorpora su imagen de vista previa; MindManager y FreeMind se convierten en listas Markdown anidadas.
: **archivos OPML** (.opml). Si está activado: mapa mental de sirena. Si está desactivado: lista Markdown anidada.
: **Contornos OmniOutliner** (.ooutline). Si está activado: mapa mental de sirena. Si está desactivado: lista Markdown anidada (o lista de verificación cuando corresponda).
: **Contornos de bicicletas**. Si está activado: mapa mental de sirena. Si está desactivado: lista Markdown anidada.