<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Bear][bear] puede enviar una vista previa en vivo directamente a Marked.

## Envío desde oso

En Bear, elija **Vista previa en Marcado** en el menú **Ver** (el texto puede variar ligeramente según la versión de Bear). Marked recibe un TextBundle, por lo que las imágenes y los recursos incrustados generalmente viajan con el texto.

Las imágenes a las que se hace referencia con rutas absolutas o `https` URL también se resuelven siempre que Marked pueda acceder a ellas.

## Nota de la Mac App Store

Si usa la compilación **Mac App Store** de Marked y macOS sigue solicitando permiso para abrir directorios cuando obtiene una vista previa desde Bear, [comuníquese con el soporte de Marked](http://support.markedapp.com) para obtener una versión cruzada gratuita a la edición de descarga directa, que evita esa fricción particular en la zona de pruebas.

## Etiquetas

Las etiquetas de estilo oso se pueden representar como tales activando **#Texto es etiqueta** y **Etiquetas de estilo** en {% prefspane Processor %}.

W> Esta configuración puede confundir a Marcado si escribe titulares regulares sin espacios después del `#`.

## Nombres de archivos y exportación

Si activa **Usar el primer H1 como título alternativo** en {% prefspane Export %}, ese título puede controlar el nombre del archivo y el marcador de posición `%title` cuando imprima o exporte archivos PDF desde Marked.

I> Un estilo de vista previa que se aproxima al propio aspecto de Bear [está disponible en marcadoapp.com/styles](https://markedapp.com/styles/preview?style=bear).

La vista previa de la transmisión de Bear se resume en la página [Vista previa de la transmisión](Streaming_Preview.html) y en [Integraciones de aplicaciones adicionales](Additional_Application_Support.html).

[bear]: https://bear.app/