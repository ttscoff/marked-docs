<!-- MT draft for es — Reading Mode help. Review before publishing. -->
# <%= @title %>

El modo de lectura mantiene su lugar en documentos largos, enfoca el bloque actual y le permite guardar aspectos destacados persistentes.

## Entrar al modo de lectura [entering-reading-mode]

Elija {% appmenu Preview, Reading Mode %} o presione {% kbd ctrl opt r %}. Si se está ejecutando la lectura rápida, Marked la detiene antes de ingresar al modo de lectura.

El párrafo, encabezado, elemento de lista, imagen, bloque de código, tabla u otra unidad de lectura actual recibe un marcador izquierdo. La navegación con el teclado se mueve suavemente entre bloques y mantiene la unidad actual cerca del tercio superior de la vista previa. Al desplazarse manualmente, se reorienta el enfoque sin ajustar la página.

## Navegación y currículum [navigation-and-resume]

Mientras el modo de lectura está activo:

- {% kbd j %} o {% kbd down %}: Pasar a la siguiente unidad de lectura.
- {% kbd k %} o {% kbd up %}: Pasar a la unidad de lectura anterior.
- {% kbd h %}: resalta la selección o alterna un resaltado en la unidad actual cuando no hay texto seleccionado.

Marked guarda la posición de lectura actual para cada documento. Cuando una posición guardada difiere de la vista actual, ingresar al modo de lectura ofrece dos opciones:

- **Reanudar** vuelve a la posición de lectura guardada.
- **Empezar desde aquí** utiliza la unidad de lectura actualmente visible en la vista previa.

## Modo enfoque [focus-mode]

Haga clic en la herramienta Modo de enfoque en la parte superior de la vista previa para atenuar todos los bloques excepto la unidad de lectura actual. El modo de enfoque sigue la unidad actual mientras navegas. Haga clic en la herramienta nuevamente para restaurar los otros bloques, o salga del modo de lectura para borrar el modo de enfoque automáticamente.

## Crear y editar aspectos destacados [creating-and-editing-highlights]

Seleccione el texto y presione {% kbd h %} para crear un resaltado de marcador en línea. Sin selección, presione {% kbd h %} para resaltar toda la unidad de lectura actual, o presiónelo nuevamente para eliminar esa unidad resaltada. El primer resaltado solicita una firma, que Marked utiliza al crear CriticMarkup. Puedes cambiar la firma en {% prefspane Preview %}.

### Ventana emergente de selección

Seleccione texto para mostrar la ventana emergente de selección con botones de íconos centrados en la fila:

- **Resaltar** crea un resaltado en línea (o **X** elimina el último resaltado automático cuando el resaltado automático está activado).
- **Comentar** abre un cuadro de diálogo para agregar o editar una nota para resaltar. Si la selección aún no está resaltada, Marked la resalta primero.

La ventana emergente también muestra el recuento de palabras de selección cuando **Mostrar recuento de palabras en la selección** está habilitado.

### Resaltar comentarios [highlight-comments]

Los comentarios están separados de las firmas. Una firma atribuye lo más destacado; un comentario es tu nota al respecto.

Agregue o edite un comentario desde el ícono de comentario emergente de selección, o haga clic con la tecla Control presionada en un resaltado y elija **Agregar comentario…** o **Editar comentario…**. Elija **Eliminar comentario** para eliminar la nota sin eliminar el resaltado.

Los aspectos destacados con comentarios muestran un pequeño punto indicador. Cuando la barra lateral de Comentarios está visible (**Vista previa > Mostrar comentarios**), los comentarios resaltados del modo de lectura aparecen allí con una línea conectora al resaltado principal, junto con CriticMarkup y otros comentarios del documento.

### Destacados automáticos

Haga clic en la herramienta de resaltado en la parte superior de la vista previa para resaltar automáticamente el texto a medida que lo selecciona. Haga clic en el resaltador en la ventana emergente de selección para deshacer el último resaltado automático, o haga clic en la herramienta de resaltado superior nuevamente para desactivar el resaltado automático.

Los resaltados en línea muestran controladores de inicio y fin cuando los señala o los selecciona. Arrastre cualquiera de los controladores para extender o contraer el rango resaltado. Los cambios se guardan automáticamente y se restauran cuando el documento se actualiza o se vuelve a abrir.

Haga clic en un resaltado para enfocarlo, luego presione Eliminar o Retroceso para eliminarlo. Mantenga presionada la tecla Control y haga clic en un resaltado y elija **Compartir...** para abrir la hoja Compartir de macOS con el título del documento y el texto resaltado, **Agregar comentario...** / **Editar comentario...** para adjuntar una nota, o **Eliminar comentario** para borrar la nota.

La configuración **Mostrar resaltados cuando el modo de lectura está desactivado** controla si los resaltados guardados permanecen visibles después de salir del modo.

## Exportar aspectos destacados [exporting-highlights]

Elija **Vista previa > Exportar aspectos destacados…** o haga clic en la herramienta Exportar aspectos destacados en la barra de herramientas del modo de lectura. Formatos: Markdown, HTML (estilo de vista previa actual), texto sin formato, CSV (compatible con Readwise, con comentarios en la columna **Nota** y firmas en **Firma**) y JSON (incluye un campo `comment` en cada resaltado).

HTML los nidos de exportación resaltan los comentarios como citas en bloque debajo de cada pasaje resaltado.

El formato JSON es el archivo de intercambio de Marked. Guárdelo junto a un documento Markdown como `Document.markedhighlights.json` o inclúyalo automáticamente al exportar un TextBundle.

## Importando aspectos destacados [importing-highlights]

Elija **Vista previa > Importar aspectos destacados…** y seleccione un archivo JSON de aspectos destacados Marked. Los aspectos destacados se fusionan por identificación: se agregan nuevos identificadores, los identificadores coincidentes se actualizan y los aspectos destacados existentes que no están en el archivo permanecen.

Cuando abres un TextBundle que contiene `highlights.json`, Marked fusiona esos aspectos destacados automáticamente. Mientras un TextBundle está abierto, Marked también guarda los cambios destacados y de comentarios en `highlights.json` en el paquete (sin modificar `text.md`).

## TextBundle destacados [textbundle-highlights]

En **Guardar TextBundle**, habilite **Incluir aspectos destacados** para insertar `highlights.json` en el paquete (o TextPack). Comparta el paquete para que los colaboradores puedan abrirlo en Marked y mantener un conjunto destacado combinado.

## CriticMarkup acciones [criticmarkup-actions]

Aparte de la exportación e importación de aspectos destacados, el menú Vista previa proporciona dos CriticMarkup acciones para los aspectos destacados guardados:

- **Copiar resaltados como CriticMarkup** copia cada resaltado en formato CriticMarkup sin cambiar el archivo fuente.
- **Inyectar aspectos destacados en el documento...** solicita confirmación y luego ajusta el texto fuente coincidente inequívoco en CriticMarkup. Marked omite las coincidencias faltantes, duplicadas o superpuestas e informa el resultado.

Con una firma y un comentario, el marcado generado utiliza <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature: comment&lt;&lt;}</code>. Con solo un comentario, Marked usa <code>{=<span>=</span>highlighted text==}{&gt;&gt;comment&lt;&lt;}</code>. Con solo una firma, usa <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code>. Sin ninguno de los dos, Marked crea solo el marcador <code>{=<span>=</span>highlighted text==}</code>.

## Aspectos destacados de la impresión [printing-highlights]

Los aspectos destacados del modo de lectura se incluyen al imprimir o guardar como PDF de forma predeterminada. Utilice **Incluir aspectos destacados del modo de lectura** en la hoja de impresión para cambiarla para la salida actual. La configuración coincidente en {% prefspane Export %} controla el valor predeterminado para trabajos de impresión futuros y PDF.
