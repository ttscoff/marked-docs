<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked tiene un amplio soporte para trabajar con archivos de Microsoft Word. El flujo de trabajo típico es **primero obtener una vista previa, luego exportar DOCX**: abra o mire su Markdown en Marked, refine los estilos y corrija en la vista previa en vivo, luego exporte a Word cuando el documento esté listo.

## Abrir archivos DOCX [opening-docx-files]

Marked puede leer un archivo DOCX y convertirlo a limpio
Rebaja. Los elementos de estilo válidos, como titulares y listas,
convertirse a su equivalente Markdown.

El seguimiento de cambios y los comentarios se convertirán en
Marcado crítico. Los aspectos destacados se convertirán en etiquetas `<mark>`,
con colores cuando corresponda.

## Exportación de archivos DOCX [exporting-docx-files]

Utilice la paleta Exportar para generar un archivo DOCX desde su
Rebaja. En el cuadro de diálogo para guardar, puede especificar un archivo incorporado.
estilos --- este estilo se puede cambiar fácilmente en Word simplemente
abriendo el selector de temas y seleccionando un nuevo tema.

### Encabezados y pies de página [headers-and-footers]

Si configura encabezados y pies de página en {% prefspane Export %}, se incluyen en el DOCX exportado. Los marcadores de posición estándar como `%title`, `%date`, `%page` y `%total` se sustituyen en el momento de la exportación. `%logo` y `%image` incrustan el logotipo desde las preferencias de Encabezado/Pie de página. `%md_*` las variables de metadatos se resuelven a partir de los metadatos MultiMarkdown del documento. `%h1`--`%h6` se convierten en campos **STYLEREF** de Word vinculados a los estilos de encabezado exportados; Word los completa al abrir el documento. Consulte [Exportar](Exporting.html#headers-and-footers) para obtener la lista completa de variables y las diferencias entre el comportamiento de DOCX y de impresión/PDF.

## Seguimiento de cambios [change-tracking]

La sintaxis de CriticMarkup en un documento Markdown se convertirá
a Word Change Tracking cuando se exporta a DOCX. Comentarios
siguientes inserciones, eliminaciones y sustituciones
aparecer en la columna de la derecha en Word cuando se realiza el seguimiento de cambios
está habilitado.

Al importar un archivo DOCX en Marked, el seguimiento de cambios se realizará
convertirse a CriticMarkup y etiquetas `<mark>` como
apropiado.

## Matemáticas [math]

Las ecuaciones de MathJax y Katex que se muestran en el documento se convertirán a MathML para mostrarlas en Word. Esta conversión no es perfecta, pero en la mayoría de los casos generará un bloque matemático válido en el documento de Word. Esto solo se aplica a la exportación. Los bloques matemáticos en documentos de Word no se convertirán al importar.

## Agregar estilos de exportación personalizados [adding-custom-export-styles]

Puede agregar sus propios estilos de exportación incluyendo una plantilla y un archivo estilos.xml en `~/Library/Application Support/Marked/Custom Word Styles/`. Para crear estos:

1. Abra un archivo DOCX generado por Marked en Word
2. Edite los estilos allí en el editor de estilos para cada elemento, seleccionando "Agregar a plantilla" para cada uno.
3. Guarde el archivo DOCX.
4. Genere una plantilla yendo a **Diseño** en la barra superior y, en el menú desplegable *Plantilla* de la izquierda, haga clic en **Guardar plantilla actual**. Asígnele el nombre que desee que aparezca en el menú Estilo marcado y guárdelo en `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx`, donde `STYLENAME` es el nombre de su estilo.
5. Vaya al Finder y busque el archivo DOCX que guardó desde Word. Duplíquelo y cambie el nombre de la copia a `FILENAME.zip` y haga doble clic para descomprimirlo.
6. En el documento descomprimido, verá una carpeta "Word" que contiene un archivo estilos.xml. Copie ese archivo estilos.xml en la misma carpeta que el anterior y asígnele el nombre `STYLENAME.xml` (donde `STYLENAME` es el nombre de su estilo). Los archivos `.thmx` y `.xml` deben tener el mismo nombre base (solo extensiones diferentes).

La próxima vez que exportes un DOCX desde Marked, verás tu nuevo estilo en el menú Estilo del cuadro de diálogo Guardar.