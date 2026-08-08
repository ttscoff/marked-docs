<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked permite varias sintaxis diferentes para incluir un archivo dentro de otro.

## Sintaxis marcada [marked-syntax]

Puede incluir archivos externos en un único documento de vista previa utilizando la sintaxis especial `<<[path/file]` al principio de una línea. La línea debe tener líneas en blanco encima y debajo, y se supone que la ruta es relativa al documento principal a menos que comience con una barra (`/`) o una tilde (`~`). Se pueden utilizar barra diagonal (directorio raíz) y tilde (directorio de inicio) para definir rutas absolutas a los archivos. No se necesita ninguna ruta si los archivos externos están en la misma carpeta que el documento principal, simplemente coloque el nombre del archivo (distingue entre mayúsculas y minúsculas e incluye la extensión) entre corchetes.

Puede utilizar los encabezados de metadatos "Incluir base" o "Transcluir base" para cambiar la ubicación base de los archivos incluidos, por ejemplo:

    Transcluir base: ~/Escritorio

*Tenga en cuenta que al visualizar documentos con archivos incluidos, puede escribir "I" (shift-i) para ver qué archivo incluido está en el área visible. Al presionar Enter mientras se muestra la ruta del archivo incluido, se abrirá el archivo incluido en el editor predeterminado.*

Con esta función, puede crear documentos/libros grandes utilizando varios archivos (por ejemplo, un archivo para cada capítulo) y luego especificar el orden de los documentos en un único archivo de índice. No importa cómo se nombren los archivos ni cómo estén organizadas las carpetas; el archivo que abra en Marcado se considerará el índice y se incluirán los archivos enumerados en su interior. Un ejemplo de un archivo de índice para un documento de tres partes:

Estructura de carpetas:

![][1]

   [1]: imágenes/multifiledocumentstructure.jpg @2x width=316px height=163px class=center

Índice.md:

	# Título del documento

	## Sección 1

	<<[secciones/sección1.md]

	## Sección 2

	<<[secciones/sección2.md]

	## Sección 3

	<<[secciones/sección3.md]

Al abrir Index.md en Marked se mostrará su contenido con los tres archivos incluidos expandidos en su interior. Todos los archivos incluidos serán monitoreados para detectar cambios. A diferencia del documento abierto en Marked, el seguimiento de archivos incluidos depende de Spotlight para obtener actualizaciones y debe existir en una carpeta indexada por Spotlight en su disco.

También puede incluir fragmentos de código y HTML o texto sin formato usando [variaciones de esta sintaxis](Special_Syntax.html#includingcode).

La exportación HTML final de un documento que contiene inclusiones tendrá comentarios HTML que contienen la ruta relativa del archivo incluido al principio y al final del texto importado.

**Nota:** cuantos más archivos se incluyan en un documento, más lento será el tiempo de compilación general de la vista previa. Marked intenta optimizar y almacenar en caché el proceso, pero espera algunos retrasos en la renderización a medida que aumenta el tamaño del documento.

## Sintaxis de transclusión de MultiMarkdown [multimarkdown-transclude-syntax]

También puede utilizar la sintaxis `{{filename}}` basada en la especificación MultiMarkdown más nueva. Marked reconocerá `Transclude Base: path` en los metadatos MMD y los utilizará como base para la transclusión de archivos.

Transclude Base solo se reconocerá en el documento principal, no en documentos adicionales incluidos. Todas las inclusiones anidadas deben tener rutas basadas en la base de transclusión inicial o desde la ubicación del documento principal.

La sintaxis de código delimitado que proporciona MultiMarkdown para incluir archivos sin procesamiento no funcionará en Marked. Para hacer esto, utilice la sintaxis `<<(file)` (bloque de código) o `<<{file}` (sin formato).

## Sintaxis del bloque IA Writer [ia-writer-block-syntax]

Marked 2.5.11+ admite la sintaxis de IA Writer [Bloque de contenido][ia]. Esta es una referencia que comienza con una barra diagonal (`/`) en su propia línea. Puede ser un ejemplo de código, una imagen, un archivo de rebajas o un archivo CSV. Todo se manejará adecuadamente según la extensión del archivo incluido y los CSV se [convertirán en tablas Markdown][csv] si es posible.

En IA Writer, los archivos incluidos se llevan al contenedor de iCloud y no siempre requieren rutas "reales". En Marcado, a menos que los archivos incluidos ya existan en la misma carpeta que el archivo que se está viendo, esta sintaxis debe usarse con una ruta, ya sea absoluta o relativa. La primera barra se ignorará, por lo que si es una ruta absoluta, comience con dos barras.

Un fragmento de código en la misma carpeta que el documento que se está obteniendo en vista previa:

    /fragmento.h

Ruta relativa a un subdirectorio llamado "imágenes":

    /images/image.png "título opcional"

Ruta absoluta a la carpeta Documentos:

    //Usuarios/nombre de usuario/Documentos/content.csv

[ia]: https://github.com/iainc/Markdown-Content-Blocks
[csv]: Creating_Tables_using_CSV_files.html

## Cómo se convierten el esquema, el mapa mental y las inclusiones CSV [how-outline-mind-map-and-csv-includes-are-converted]

Cuando incluye ciertos tipos de archivos con sintaxis de bloque `<<[path]` o IA Writer, Marked los convierte en lugar de insertar contenidos de archivos sin formato. El comportamiento de los esquemas y mapas mentales depende de la extensión del archivo y de sus preferencias [Configuración: Aplicaciones → Mapas mentales/Contornos][mapas mentales]. Los archivos CSV/TSV siempre se convierten a tablas Markdown (consulte [Creación de tablas usando archivos CSV][csv]).

| Formato | Ampliación | Cuando "Incrustar como sirena" está **activado** | Cuando **apagado** |
|--------|------------|-----------------------------------|--------------|
| **iPensamientos X** | .itmz | Diagrama de mapa mental de sirena (árbol ordenado) | Imagen de vista previa del .itmz |
| **Gestor Mental** | .mmap | Diagrama de mapa mental de sirena | Lista de rebajas anidadas |
| **Mente libre** | .mm | Diagrama de mapa mental de sirena | Lista de rebajas anidadas |
| **OPML** | .opml | Diagrama de mapa mental de sirena | Lista de rebajas anidadas |
| **OmniOutliner** | .oesquema | Diagrama de mapa mental de sirena | Lista de rebajas anidadas |
| **Bicicleta** | .bicicleta | Mapa mental de sirena (nombre de archivo como nodo raíz) | Lista de Markdown anidada (sin título de documento) |
| **CSV/TSV** | .csv, .tsv | Tabla de rebajas ||
| **RTF/RTFD** | .rtf, .rtfd | Markdown mediante conversión RTF (consulte [Soporte RTF y RTFD](RTF_Support.html)) ||
| **PDF** | .pdf | Markdown mediante conversión de PDF cuando se abre como documento principal (consulte [Soporte de PDF](PDF_Support.html)) ||

Cada formato de esquema/mapa mental tiene su propia casilla de verificación en *Mapas mentales/Contornos* (mapas mentales, archivos OPML, esquemas de bicicletas, esquemas de OmniOutliner). Al desactivar un formato se utiliza el comportamiento "desactivado" sólo para ese tipo. Consulte [Incorporar esquemas y mapas mentales](Embedding_Mind_Maps_and_Outlines.html) para obtener detalles sobre el formato y [Configuración: Aplicaciones][mapas mentales] para cambiar estas opciones. Para obtener detalles sobre la conversión a CSV, consulte [Creación de tablas utilizando archivos CSV][csv].

[mindmaps]: Settings_Apps.html#MindMapsOutlines

## Formatos de libros [book-formats]

Marked también admite archivos de índice en formatos como [Leanpub][lp], [GitBook][gb] y mmd\_merge (MultiMarkdown). Los archivos incluidos en los índices de formato de libro serán observados en busca de cambios y el resultado es una vista previa completa de su documento compilado, tal como en el ejemplo "Index.md" anterior.

### Leanpub [leanpub]

Si habilita la opción en {% prefspane Apps %} en compatibilidad con Leanpub/GitBook, los archivos denominados "Book.txt" se tratarán automáticamente como archivos de índice de Leanpub. También se reconoce el antiguo formato "frontmatter:".

[Documentación de Leanpub.][lpdocs]

Ejemplo de libro Leanpub.txt:

    front-asunto:
    Agradecimientos.txt
    Prefacio.txt
    Introducción.txt
    asunto principal:
    Rebajas.txt
    Libros de muestra.txt
    Insertar imágenes.txt


### mmd_merge [mmdmerge]

Para mmd\_merge, Marked requiere que la primera línea sea "#merge" (un activador marcado especial para mmd\_merge, tratado como un comentario e ignorado por otros procesadores).

[documentación mmd_merge.][mmdm]

Ejemplo de mmd_merge:

    #fusionar
    metadatos.txt
    Capítulo-1.md
        sub-capítulo-1-1.md
        sub-capítulo-1-2.md
    Capítulo-2.md
        sub-capítulo-2-1.md
        sub-capítulo-2-2.md
    Preguntas frecuentes.md
    Agradecimientos.md

### Libro de Git [gitbook]

El formato de GitBook utiliza una lista Markdown para crear la estructura y la tabla de contenido. Si la compatibilidad con GitBook está habilitada en {% prefspane Apps %} en compatibilidad con Leanpub/GitBook, se leerá un archivo llamado SUMMARY.md y se convertirá automáticamente al formato mmd_merge, lo que permitirá una vista previa completa de su documento GitBook.

[Documentación de GitBook.][gbdocs]

Ejemplo de GitBook SUMMARY.md:

    # Resumen

    * [Parte I](parte1/README.md)
        * [Escribir es agradable](part1/writing.md)
        * [GitBook es bueno](part1/gitbook.md)
    * [Parte II](parte2/README.md)
        * [Nos encantan los comentarios](part2/feedback_please.md)
        * [Mejores herramientas para autores](part2/better_tools.md)

GitBook permite el uso de anclajes en la tabla de contenido SUMMARY.md, pero Marked los ignorará y solo incluirá el documento base una vez.

[gbdocs]: https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md
[lp]: http://leanpub.com/
[lpdocs]: https://leanpub.com/help/manual#leanpub-auto-how-to-set-the-books-structure
[mmdm]: http://fletcher.github.io/peg-multimarkdown/#howdoisplitamultimarkdowndocumentintoseveralparts
[gb]: https://www.gitbook.com/

## Funciones de vista previa de documentos de varios archivos [multi-file-document-preview-features]

![Límites de archivos incluidos][2]

   [2]: imágenes/includeboundaries.png @2x width=859px height=239px class=center

Al visualizar un documento que contiene archivos incluidos, puede utilizar dos funciones para ayudar a determinar qué archivo está viendo.

* **Teclado:** Al presionar {% kbd shift I %} se mostrará brevemente una ventana emergente que muestra el título del archivo actualmente visible en la posición de desplazamiento de la vista previa.
    * Al presionar {% kbd Return %} después de {% kbd I %} se editará el archivo mostrado con su editor externo.
* **Ratón:** Al seleccionar "Mostrar límites de archivos incluidos" en el menú de ajustes ({% kbd ctrl cmd B %}) se agregará una barra de color al lado izquierdo de la vista previa, segmentada para mostrar el principio y el final de los archivos incluidos. También muestra inclusiones anidadas. Al pasar el cursor sobre una sección de esta barra se mostrará el nombre del archivo que representa y, al hacer clic en él, se abrirá ese archivo en el editor elegido.