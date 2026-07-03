<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Speed Read es un modo de lectura de estilo RSVP que muestra una palabra a la vez en una superposición enfocada.

## Cómo funciona la lectura rápida

Speed Read utiliza un método llamado **Presentación visual en serie rápida** (RSVP). En lugar de mover los ojos a través de líneas de texto, las palabras aparecen en una posición fija. Esto reduce los movimientos oculares, los cambios de línea y el retroceso que normalmente ocurren durante la lectura, lo que puede resultar útil para hojear, revisar material familiar o moverse rápidamente a través del texto sin perder el lugar.

El método no es mágico y no garantiza una mejor comprensión a velocidades muy altas. La comprensión lectora aún depende de la complejidad de la escritura, su familiaridad con el tema y la configuración de WPM. Para material denso o desconocido, una velocidad moderada suele ser más efectiva que aumentar la velocidad lo más alto posible.

La letra roja marca el punto de anclaje visual de la palabra, a veces llamado **punto de reconocimiento óptimo**. En muchas palabras, los lectores identifican la palabra de manera más eficiente cuando su mirada se posa ligeramente a la izquierda del centro en lugar de mirar la primera letra. Al mantener ese punto de anclaje en el mismo lugar y resaltarlo, Speed ​​Read le brinda a su ojo un objetivo consistente. El resultado es menos reenfoque entre palabras y un ritmo más constante mientras avanza el texto.

## Lectura de velocidad de apertura

Utilice **Vista previa > Lectura rápida**, el elemento **Lectura rápida** en el menú Engranaje de la ventana de vista previa, o presione {% kbd ctrl opt S %}. El elemento del menú está disponible cuando una ventana de documento de vista previa de Markdown está activa (está deshabilitada para vistas previas de HTML sin formato y cuando no hay ningún documento abierto).

Cuando se abre Speed ​​Read, comienza en un estado de pausa para que pueda orientarse antes de que comience la reproducción.

<controles de vídeo precarga="metadatos" poster="images/speedread-poster.png">
  <fuente src="images/speedread.webm" tipo="video/webm">
  <fuente src="images/speedread.mp4" tipo="video/mp4">
  Su navegador no admite el vídeo de demostración de Speed Read.
</vídeo>
<p><em>Superposición de lectura rápida que muestra los controles de reproducción, la opción de sincronización y el acceso a la ayuda.</em></p>

## Controles de superposición

Una vez que la superposición sea visible, estas claves estarán disponibles:

| Atajo | Función |
| :-- | :-- |
| {% kbd space %} | Reproducir/Pausar |
| {% kbd [ %} | Saltar al inicio del párrafo (presione nuevamente para ir al párrafo anterior) |
| {% kbd ] %} | Saltar al inicio del siguiente párrafo |
| {% kbd left %} | Disminuir la velocidad de lectura (WPM) |
| {% kbd right %} | Aumentar la velocidad de lectura (WPM) |
| {% kbd esc %} | Salir de lectura rápida |

Los corchetes se capturan para la navegación de párrafos y las flechas izquierda/derecha se capturan para los cambios de velocidad, por lo que estas teclas no activan la navegación de vista previa mientras la lectura rápida está abierta. También puedes hacer clic en el botón circular **X** en la esquina superior izquierda de la superposición para descartarla.

Otros atajos de navegación de vista previa normales aún funcionan mientras la lectura rápida está activa, incluidos `t`/`gg` (arriba), `G`/`b` (abajo) y `,`/`.` (navegación de encabezado). Consulte [Vista previa de navegación](Keyboard_Shortcuts#preview-navigation) para obtener la lista completa.

La tabla de contenidos también se puede utilizar durante la lectura rápida. Presione {% kbd cmd t %} para abrirlo y navegar, o presione {% kbd f %} para enfocar inmediatamente la búsqueda rápida para navegar por los encabezados de los documentos.

## A partir de una selección

Si se selecciona texto en la vista previa cuando inicia la lectura rápida, la reproducción utiliza el texto seleccionado. Si no hay ninguna selección activa, la lectura rápida utiliza el texto completo del documento.

## Sincronización con la posición de desplazamiento

Habilite **Sincronizar lectura rápida con posición de desplazamiento** en {% prefspane Preview %}, o use la casilla de verificación en la superposición de Lectura rápida para mantener la vista previa y la posición de Lectura rápida juntas.

Cuando esta opción está habilitada, la lectura rápida comienza en el contenido actualmente visible en la parte superior de la vista previa en lugar del comienzo del documento. A medida que avanza la reproducción, la vista previa se desplaza junto con las palabras mostradas.

Si cierra Speed ​​Read, desplaza la vista previa y vuelve a abrir la superposición, la reproducción comienza desde la nueva posición visible. Si activa la casilla de verificación de superposición después de que la lectura rápida ya esté abierta, la reproducción se restablece a la posición de desplazamiento actual y continúa desde allí.

## Velocidad recordada

El valor de WPM se guarda automáticamente cuando lo cambia con {% kbd ← %} y {% kbd → %}. La velocidad elegida se restaurará la próxima vez que utilices la lectura rápida.