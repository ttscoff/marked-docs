<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Utilice sus dos herramientas de escritura favoritas juntas.

> Marked todavía puede leer archivos Scrivener 2.0, pero el desarrollo se centrará en la versión 3 después de Marked 2.5.11.

## Conceptos básicos de Scrivener 3.0 [scrivener-30-basics]

Arrastre un proyecto de Scrivener (.scriv) a Marcado y se compilará y obtendrá una vista previa. Si elige la opción de abrir archivos .scriv en Scrivener (arriba), Marked también iniciará Scrivener cuando arrastre el archivo a Marked.

Al igual que con otros documentos, los cambios en los archivos de Scrivener se actualizan en vivo al guardarlos. Además, cuando un documento de Scrivener esté en primer plano en Marked, {% kbd cmd E %} lo abrirá en Scrivener.

## Filtrado de documentos de carpeta [filtering-binder-documents]

Cuando abre un proyecto de Scrivener en Marked, el contenido de vista previa se crea solo a partir de los documentos de carpeta que seleccione. El filtrado siempre está activo para archivos `.scriv`; El panel de filtro es solo una forma conveniente de cambiar lo que se incluye.

Abra el panel desde **Revisión > Filtrar documentos de Scrivener** ({% kbd opt-cmd-f %}). El elemento del menú muestra una marca de verificación mientras el panel está visible. Cerrar el panel no desactiva el filtrado ni restablece sus selecciones.

El panel de filtro enumera las secciones de carpeta de su proyecto (Borrador, Investigación y otras carpetas de nivel superior excepto Papelera). Cada sección está contraída de forma predeterminada. Expanda una sección para ver sus documentos y carpetas en un esquema:

- Marque o desmarque cualquier **documento de texto** para incluirlo o excluirlo de la vista previa.
- Haga clic en una fila de **carpeta** para seleccionar o anular la selección de todos sus descendientes. Un guión en la casilla de verificación significa que solo se seleccionan algunos descendientes.
- Las filas con **Incluir en compilación** desactivado en Scrivener aparecen en gris, pero aún puedes verificarlas para obtener una vista previa de ellas en Marcado.
- **Imágenes, archivos PDF y otros elementos de carpeta que no son texto** aparecen en la lista pero no se pueden seleccionar.
- **Aún aparecen archivos RTF faltantes**; Si agrega contenido en Scrivener mientras Marked está abierto, la vista previa se actualiza al guardar como cualquier otro cambio de Scrivener.

Utilice **Seleccionar todo** y **Deseleccionar todo** en la parte superior del panel para todo el proyecto. Cada encabezado de sección tiene botones **Todos** y **Ninguno** solo para esa sección. **Deseleccionar todo** significa que no se verifican documentos.

Si no se selecciona nada, la vista previa muestra un mensaje corto con un enlace para abrir el panel de filtro (`x-marked://scrivenerfilter`). Puede usar esa URL en scripts u otras aplicaciones para abrir el panel del documento frontal de Scrivener en Marked.

Las selecciones de sus casillas de verificación se guardan por proyecto de Scrivener (mediante el identificador del proyecto en el archivo `.scrivx`) y se restauran la próxima vez que abra ese proyecto en Marked. La primera vez que abre un proyecto, Marcado selecciona solo documentos de carpeta **Borrador** cuyo indicador **Incluir en compilación** sea Sí (o no configurado, lo que Scrivener trata como Sí). La investigación y otros obstáculos comienzan sin control; Los elementos Borrador excluidos de compilación comienzan sin marcar pero permanecen seleccionables en la lista.

Los proyectos de Scrivener 2 muestran solo la carpeta **Borrador** en el panel de filtro. Los proyectos de Scrivener 3 incluyen todas las carpetas excepto la Papelera.

El panel de filtro puede permanecer abierto junto con otras herramientas como **Visualizar repetición de palabras**. Al cambiar una casilla de verificación se vuelve a compilar la vista previa después de un breve retraso; Si aún se está compilando un proyecto grande, Marked cancela la importación en progreso y comienza nuevamente con su nueva selección.

## Encabezados de rebajas de títulos de Scrivener [markdown-headers-from-scrivener-titles]

Marked también puede crear encabezados Markdown jerárquicos basados en las páginas de su archivo Scrivener. Para habilitar esto, simplemente marque la opción que se muestra arriba.

## Metadatos de MultiMarkdown [multimarkdown-metadata]

Si el primer documento en su carpeta Borrador se llama "metadatos", se tratará como metadatos de MultiMarkdown al comienzo del documento de vista previa. No se insertará ningún encabezado para esta sección, independientemente de la configuración "Encabezados de Markdown de títulos de Scrivener" (descrita anteriormente), lo que permite que el procesador MultiMarkdown los lea como metadatos y permita reemplazos y opciones de exportación en consecuencia.

Puede crear este archivo con formato YAML si su procesador es uno que maneja YAML.

Si no utiliza un documento `metadata`, Marked también puede anteponer metadatos de MultiMarkdown de la configuración de compilación de su proyecto (`Settings/compile.xml`), usando los mismos campos **Título** y **Autor** que Scrivener exportaría a MultiMarkdown. Esto está habilitado de forma predeterminada (tecla de preferencia `scrivenerCompileMetadata`). Los campos de metadatos personalizados solo se incluyen cuando aparecen en la configuración de compilación de **Metadatos MMD** del proyecto, no en campos personalizados por documento.

## Enlaces [links]

Para enlaces externos (HTTP), puede utilizar la sintaxis de Markdown o el formato de enlace de Scrivener. Marked convertirá el formato Scrivener a Markdown antes de procesarlo.

## Comentarios [comments]

Marked puede procesar comentarios y notas a pie de página creados en línea dentro del documento.

## Tablas [tables]

Marked puede convertir tablas básicas de Scrivener. Sin embargo, si desea incluir una tabla en su salida, es mejor hacerlo en [formato de tabla MultiMarkdown](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#tables). (Una aplicación llamada [TableFlip](http://tableflipapp.com/) puede hacer que generarlos sea una tarea sencilla).

## Funciones adicionales de escribano [additional-scrivener-features]

Además de las funciones básicas de compilación y vista previa, Marked también admite algunas convenciones específicas de Scrivener. Primero, en su documento de Scrivener, puede usar "Conservar formato" en línea o en un bloque de texto independiente y se convertirá en bloques de código en la vista previa.

Marked también lee notas a pie de página _inline_ de Scrivener. Si ingresa una nota al pie dentro o al final de un párrafo, se convertirá en una nota al pie de MultiMarkdown en la vista previa.

## Uso de imágenes en su documento de Scrivener [using-images-in-your-scrivener-document]

Las imágenes se pueden incrustar en el documento de Scrivener o hacer referencia a ellas con la sintaxis de imagen de Markdown. La versión Markdown de una etiqueta de imagen es `![alt text](path/to/image.ext "optional title/description")`. También se puede utilizar el formato de referencia:

    ![texto alternativo][img1]

    [img1]: /ruta/a/imagen.ext "descripción opcional"

La ruta base para la salida HTML en la Vista previa se establecerá en la carpeta que contiene el documento de Scrivener. Así, colocar las imágenes en la misma carpeta que el documento de trabajo permitirá acceder a ellas directamente. Si su documento de Scrivener está en `~/Desktop/TestDoc.scriv` y tiene una imagen llamada "testimage.png" en `~/Desktop/testimage.png`, puede agregar la imagen a su documento usando:

    ![Imagen de prueba](testimage.png)

Las rutas relativas basadas en la carpeta principal del documento funcionarán y las rutas absolutas permitirán el acceso a las imágenes en cualquier lugar, pero es posible que no sean tan portátiles para la salida HTML.

## Nota de seguridad [security-note]

Se creará una carpeta de caché en ~/Library/Application Support/Marked cuando abra su archivo .scriv en Marked. Esta no es una carpeta protegida, por lo que si su documento original está en un disco cifrado o está protegido de otro modo, tenga en cuenta que su contenido no estará cifrado en la memoria caché. Para una protección limitada, puede asegurarse de que este caché no aparezca en Spotlight agregando ~/Library/Application Support/Marked a su configuración de privacidad en Spotlight.

Consulte [Integraciones de aplicaciones adicionales](Additional_Application_Support.html) para obtener una vista previa del portapapeles, enlaces wiki, secuencias de comandos y la lista completa de guías por aplicación.