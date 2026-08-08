<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

I> Esta página cubre la vista previa *apariencia* --- estilos, zoom, modo oscuro y la barra de estado. Para configurar la vista previa en vivo desde su editor, consulte [Vista previa de Live Markdown en Mac](Live_Markdown_Preview_on_Mac.html).

Cambiando tu forma de ver las cosas.

## Elegir un estilo [choosing-a-style]

![][1]

   [1]: imágenes/StylePicker.jpg @2x width=896px height=195px class=center

Puede establecer un estilo predeterminado para documentos nuevos en {% prefspane Style %}. Si tiene el menú de estilo en la barra de herramientas habilitado en la configuración de Ventana, puede ajustar el estilo por documento directamente desde la ventana Vista previa. Su selección de estilo será recordada y será la primera opción para las opciones de exportación e impresión.

Los estilos personalizados agregados en la configuración de Estilo estarán disponibles en ambos menús.

Los estilos se pueden seleccionar con atajos de teclado. Abra el menú de estilos para ver el método abreviado de teclado para cada estilo. Los atajos de teclado se asignan en orden de estilo: se puede acceder a los primeros 9 estilos de la lista con {% kbd cmd 1 %} -- {% kbd cmd 9 %}, a los siguientes 10 estilos con {% kbd cmd opt 1 %} -- {% kbd cmd opt 0 %}, etc.

## Modo de esquema [outline-mode]

Si su documento es una lista jerárquica, como una generada a partir de un mapa mental o una aplicación de esquematización, puede habilitar el Modo de esquema desde el menú Engranaje para aplicar un formato especial en estilo de esquematización APA o Decimal.

El modo de esquema automático se puede habilitar para extensiones de archivo específicas en el {% prefspane Style %}.

## Zoom de texto [text-zoom]

![][2]

   [2]: imágenes/textzoom.jpg @2x width=800px height=414px class=center

Puede cambiar el tamaño del texto usando {% kbd cmd shift + %} y {% kbd cmd shift - %}, o usar el menú Zoom en Vista previa en la barra de menú o en el menú de ajustes en la ventana del documento. Marked recordará cualquier cambio que realice la próxima vez (y siempre). Restablezca el zoom al 100% con {% kbd cmd 0 %} (o acceda a **Restablecer zoom** desde el menú Zoom).

## Modo oscuro/Alto contraste [dark-modehigh-contrast]

Si prefiere texto claro sobre un fondo oscuro, Marked lo tiene cubierto. En el menú __Vista previa__, puede usar {% appmenu Preview, Dark Mode ({{opt}}{{cmd}}I) %} invertir los colores en cualquiera de los esquemas predeterminados para obtener un resultado claro sobre oscuro, y si un tema personalizado está [construido correctamente](Writing_Custom_CSS.html), también funcionará allí.

## Mostrar/Ocultar barra de estado [showhide-status-bar]

La barra de estado en la parte inferior de la ventana de vista previa se puede alternar con el elemento de menú {% appmenu Preview, Show Status Bar ({{ctrl}}/) %}. Cuando está oculto, se puede ver e interactuar con él pasando el cursor sobre el espacio en la parte inferior de la vista previa.