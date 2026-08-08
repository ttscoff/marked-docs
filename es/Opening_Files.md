<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado te da opciones.

## Flujo de trabajo de vista previa en vivo [live-preview-workflow]

1. Arrastre un archivo Markdown a Marked (o use {% appmenu File, Open... ({{cmd}}O) %}).
2. Edite el archivo en su editor preferido.
3. Guardar --- Marked actualiza la vista previa automáticamente.

Consulte [Vista previa de Live Markdown en Mac](Live_Markdown_Preview_on_Mac.html) para ver la bóveda, la vista previa de transmisión y guías específicas del editor.

## Arrastrar al icono del muelle [drag-to-dock-icon]

La forma más sencilla de usar Marcado en un archivo que ya estás editando es arrastrar el ícono del documento desde la barra de herramientas de tu editor o desde Finder al ícono Marcado en tu Dock. Marked comenzará inmediatamente a rastrear cualquier archivo Markdown (o archivo de texto) que se le coloque. También puedes arrastrar archivos directamente desde el Finder.

## Usando el menú [using-the-menu]

![][2]

   [2]: imágenes/file_open.jpg @2x width=300px height=118px class=center

Por supuesto, puede abrir archivos Markdown directamente usando la opción de menú {% appmenu File, Open... ({{cmd}}O) %}. Marked también funciona bien _sin_ un editor de texto. Puede obtener una vista previa y convertir su Markdown con solo un clic.

Marked también puede abrir archivos **`.rtf` y `.rtfd`** directamente (por ejemplo, exportaciones desde Pages o TextEdit). Se convierten a Markdown para obtener una vista previa y actualización cuando los guarda en la aplicación original. Consulte [Soporte RTF y RTFD](RTF_Support.html) para obtener detalles, incluidas imágenes y limitaciones.

Marked puede abrir **`.pdf`** archivos de la misma manera: la conversión se ejecuta en segundo plano y luego la vista previa se actualiza cuando finaliza. Esto funciona mejor para archivos PDF más cortos basados ​​en texto; Los manuales grandes y los documentos escaneados son más lentos y menos precisos. Consulte [Soporte de PDF](PDF_Support.html) para obtener detalles y limitaciones.

## Desde el portapapeles [from-the-clipboard]

Si tiene texto compatible (por ejemplo, Markdown) en su portapapeles, puede abrir una vista previa instantánea seleccionando {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Si copió una selección de un navegador web u otra aplicación que coloca HTML o RTF en el portapapeles, Marked la convierte a Markdown para obtener una vista previa. Cuando pegas RTF desde una aplicación como TextEdit o Pages, los tamaños de fuente más grandes se convierten aproximadamente a niveles de título (por ejemplo, el texto muy grande se convierte en un título de nivel 1, el texto grande más pequeño se convierte en nivel 2, etc.). Puede tener abiertas varias vistas previas del portapapeles a la vez y guardarlas en un archivo nuevo eligiendo {% appmenu File, Save Transient Preview %}.

## Creando un nuevo documento [creating-a-new-document]

Marcado le permite crear un archivo de texto nuevo y vacío con el comando {% appmenu File, New ({{cmd}}N) %}. Inmediatamente le pedirá una ubicación para guardar el archivo y puede habilitar la opción "Editar archivos nuevos automáticamente" en {% prefspane Apps %}, junto al botón Editor de texto para abrir automáticamente el archivo recién creado en su editor predeterminado.

## Abrir reciente [open-recent]

![][3]

   [3]: imágenes/open_recent.jpg @2x width=300px height=174px class=center

Marked también realiza un seguimiento de los documentos recientes. La opción de menú {% appmenu File, Open Recent %} le mostrará los archivos que tenía abiertos y le permitirá volver a ellos. Puede volver a abrir rápidamente el último archivo que estaba viendo con {% kbd shift cmd R %}. Utilice {% kbd shift cmd P %} o [Acciones rápidas](Quick_Actions.html) para ejecutar el menú y obtener una vista previa de los comandos desde el teclado. También hay muchos otros atajos de teclado. Si desea aprenderlos, puede encontrar un gráfico en [Teclado Atajos](Keyboard_Shortcuts.html).

## Nueva vista en el archivo actual [multiview]

Utilice {% appmenu File, New View into Current File %} ({% kbd
shift cmd N %}, también en el menú contextual de vista previa) para abrir una
segunda ventana de vista previa en el mismo archivo guardado. ambas ventanas
mire el archivo en el disco y actualícelo cuando lo guarde en su
editor, pero cada vista mantiene su propia posición de desplazamiento,
marcadores, estilo de vista previa y [Regla personalizada
anulaciones](Custom_Processor.html#manuallyenabled).

**Caso de uso de ejemplo:** Estás editando un manuscrito largo en
MultiMarkdown con tu estilo y procesador habitual. abrir un
segunda vista, cámbiela a un estilo de revisión, fije un proceso
regla que ejecuta un procesador integrado diferente y habilitar una
regla manual que resalta el marcado de revisión. tu comparas
borrador y prueba de diseños uno al lado del otro sin mantener dos
copias del expediente.

Cuando hay más de una vista de un archivo abierta, el título de la ventana
incluye **Ver 2**, **Ver 3**, etc. para que puedas saber
ventanas separadas en el menú Ventana y Mission Control.

Las vistas alternativas no están disponibles para documentos no guardados.
vistas previas del portapapeles, vistas previas de transmisión o basadas en carpetas
proyectos que no se asignan a un solo archivo en el disco.

## Apertura rápida ## [quick-open]

Puede cambiar rápidamente entre documentos abiertos, abrir documentos recientes o abrir el cuadro de diálogo Archivo->Abrir con el [Panel de apertura rápida](Quick_Open.html) ({% kbd cmd shift o %}).