<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La función "desplazarse para editar" en Marked realiza un seguimiento de las diferencias entre la última actualización y la última, intentando encontrar el punto donde realizó los cambios más recientes. Marcado siempre realiza un seguimiento de esto y aparece una pequeña línea roja en la vista previa para mostrarle la ubicación del primer cambio detectado. En el panel de preferencias de Comportamiento, puede activar "Desplazarse hasta la primera edición" y cuando se actualice una vista previa, la vista se desplazará suavemente hasta esa ubicación.

Con "Desplazarse a la primera edición" desactivado, aún puedes presionar la tecla "e" en cualquier momento en la vista previa para ir al último punto de edición almacenado.


### Notas sobre "Desplazarse para editar"

Esta es una característica excelente cuando funciona, pero presenta muchas complicaciones. Especialmente las primeras veces que se actualiza el documento, puede haber algunas sacudidas en el desplazamiento. Si todos sus cambios están dentro de un elemento muy grande (un párrafo excesivamente largo, por ejemplo), solo podrá acercarse con el marcador. De manera similar, si agrega una o dos palabras al final del documento, el marcador de cambio se colocará en el elemento de arriba hasta que haya suficiente contenido para anclar en el nuevo elemento.