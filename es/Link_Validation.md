<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La validación de enlaces hace ping al destino de una URL y comprueba si hay errores. Esto ayuda a evitar enlaces rotos e inválidos en su documento publicado y es especialmente útil para blogueros.

## Validar enlaces individuales

![][1]

   [1]: imágenes/validate_single.png @2x width=832px height=267px class=center

Haga clic y mantenga presionado un enlace en la vista previa hasta que parpadee, luego suéltelo para abrir el menú de acción del enlace. Elija "Validar enlace" para ejecutar la prueba. Los resultados se muestran en la ventana emergente.

## Validando todos los enlaces

![][2]

   [2]: imágenes/capturas de pantalla/mainwindow-feature-urlvalidate-crop.jpg @2x width=1089px height=300px class=center

Elija "Validar todos los enlaces" (atajo {% kbd ctrl cmd L %}) en el menú de ajustes o en el menú contextual. Se comprobarán todos los enlaces remotos del documento y los resultados se mostrarán en una ventana emergente. Al hacer clic en un enlace en la ventana emergente, se desplazará y resaltará su enlace respectivo en el documento.

Las URL válidas se pueden ocultar en la ventana emergente con el botón "Ocultar válidas" en la parte superior. Esto mostrará solo las URL que hayan devuelto un estado de error.

Al presionar Escape se ocultarán los resultados de la validación. Se pueden revelar nuevamente usando {% kbd ctrl cmd L %} o el menú Engranaje.

## Validando automáticamente

Active "Validar automáticamente las URL al actualizar" en la configuración de Vista previa (o en la parte inferior de la ventana emergente de validación de enlaces). Cuando se carga el documento, los enlaces contenidos se probarán en segundo plano. Sólo se mostrará un cuadro de diálogo si hay errores.

Para desactivar la ventana emergente, desactívela en la configuración o desmarque la casilla en la parte inferior de la ventana emergente.