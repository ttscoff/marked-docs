<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opciones en el {% prefspane Export %}:

(Consulte [Exportar](Exporting.html) para obtener más información)

![Configuración: Exportar][1]

[1]: images/screenshots/preferences-Export.jpg @2x width=920px height=1031px class=preferencepane-scroll

### Exportar perfil [export-profile]

Perfil de exportación
: seleccione un perfil guardado en el menú emergente. Los perfiles almacenan un conjunto completo de preferencias de exportación para cambiar rápidamente entre flujos de trabajo (por ejemplo, imprimir PDF frente a HTML web). Consulte [Exportar perfiles](Exporting.html#export-profiles).

Nuevo
: crea un nuevo perfil a partir de la configuración actual.

Administrar
: abra el administrador de perfiles para cambiar el nombre, duplicar o eliminar perfiles.

### Imprimir/PDF [printpdf]

Deshabilite enlaces/resaltados al exportar PDF o imprimir
: Elimina el formato (subrayado y color) de los enlaces al imprimir.

Incluir URL como anotación de texto
: Al imprimir o exportar PDF, la URL de un enlace aparecerá después del texto vinculado.

Reemplazar reglas horizontales con saltos de página
: Convierte las reglas horizontales del documento en saltos de página (esto además forzará las notas al pie en una página nueva).

Incrustar imágenes al copiar HTML
: Cuando está habilitado, copiar HTML al portapapeles buscará imágenes locales y Base64 las codificará para incluirlas como URL de datos en el código fuente.

Imprimir colores e imágenes de fondo
: De forma predeterminada, Marcado se imprimirá/exportará con un fondo blanco. Si desea incluir colores de fondo e imágenes de temas personalizados, habilite esta opción.

Evite titulares huérfanos
: Esta opción evita que los titulares de la siguiente sección aparezcan en la parte inferior de una página sin contenido posterior.

Excluir el primer H1
: Ignore el primer título de nivel uno del documento cuando utilice H1 como saltos de página.

Utilice el primer H1 como título alternativo
: cuando usa aplicaciones como Bear o la vista previa de transmisión, esta opción le permite anular el nombre del archivo con el contenido del primer H1 del documento. Si se especifican metadatos para "título", eso siempre tendrá prioridad.

Agregar saltos de página antes
: Utilice encabezados de nivel 1/2 como divisores de sección, iniciándolos siempre en una página nueva. Seleccione "Notas al pie" para agregar siempre un salto de página antes de las notas al pie del documento.

Indicar saltos de página en la vista previa
: Muestra una línea discontinua clara donde se insertan saltos con la sintaxis <!\--BREAK\--> o marcando las opciones de salto automático en la configuración de Exportación.

Tamaño de fuente personalizado para exportar/imprimir
: Si se establece, todo el texto se escalará según la configuración de puntos seleccionada (el valor predeterminado es una base de 10 puntos).

Márgenes
: define los márgenes de impresión (especificados en puntos) para superior, inferior, izquierdo y derecho.

Imprimir tabla de contenidos
: Incluye tabla de contenidos automática en formato impreso/PDF.

Salto de página después
: pasa automáticamente a una nueva página después de insertar una tabla de contenido.

Marcadores de nivel de tabla de contenido
: utilice los menús desplegables para configurar el marcador de elementos de la lista para cada nivel de sangría en una tabla de contenido.

### Encabezados y pies de página [headers-and-footers]

Configure la fuente, el logotipo, los campos de encabezado/pie de página, los formatos de fecha y hora, la inclusión de la primera página, el desplazamiento de la numeración de páginas y los bordes. Los marcadores de posición de campo incluyen `%title`, `%logo`, `%page`, `%total`, `%date`, `%time`, `%h1`, `%h2` y otros.

Consulte [Encabezados y pies de página](Exporting.html#headers-and-footers) en [Exportar](Exporting.html) para referencias de marcadores de posición y ejemplos. Consulte [Formatos de fecha y hora](Exporting.html#dateandtimeformats) para conocer los códigos de formato `%date` y `%time`.

Incluir en la primera página
: Si la opción para encabezado y/o pie de página no está marcada, la primera página no se imprimirá del tipo especificado.

Formato de fecha
: cadena de formato estilo strftime para `%date` en encabezados y pies de página. Consulte [Formatos de fecha y hora](Exporting.html#dateandtimeformats).

Formato de hora
: cadena de formato estilo strftime para `%time` en encabezados y pies de página. Consulte [Formatos de fecha y hora](Exporting.html#dateandtimeformats).

Desplazamiento de numeración de páginas
: Se utiliza para ajustar en qué número comienzan los números de página. Por ejemplo, si tiene una tabla de contenido en la primera página y desea que la numeración comience en la segunda página, establezca el desplazamiento en -1. La página 2 ahora será la página 1 y el total de páginas se ajustará en consecuencia.

frontera
: imprime una línea horizontal debajo del encabezado y/o encima del pie de página.

Restaurar formatos predeterminados
: Restablece las cadenas de formato de fecha y hora a los valores predeterminados de Marked (`%m-%d-%Y` y `%I:%M %p`). Consulte [Formatos de fecha y hora](Exporting.html#dateandtimeformats).