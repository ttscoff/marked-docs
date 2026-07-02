<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La velocidad de renderizado general y el rendimiento de Marked pueden variar mucho según su configuración y el tipo de contenido que tenga en su documento. Hay varios factores que pueden provocar una renderización lenta o retrasos prolongados:

* **Time Machine.** Si Time Machine se está ejecutando y su sistema experimenta mucha actividad en el disco, es posible que Marked responda más lentamente a los cambios en su documento. La velocidad de procesamiento no se ve afectada, sólo el tiempo de reacción.
* **Representación de un documento Markdown que contiene mucho HTML.** Esto siempre tardará más en procesarse. Discount lo maneja un poco mejor que MultiMarkdown, por lo que si es necesario, podría considerar cambiar el procesador predeterminado (**Advertencia:** perderá las notas a pie de página y algunas otras funciones de MultiMarkdown).
* **Usar muchas inclusiones.** Ya sea que se trate de inclusiones de código o de un archivo de combinación de índice, Marked tarda un segundo en recoger todas las piezas. Lo mismo ocurre con los documentos grandes de Scrivener. No hay mucho que puedas hacer para solucionar este problema, Marked simplemente hará todo lo posible para mantenerse al día con la forma en que elijas estructurar tu documento.
* **Condición del disco duro.** Si su disco duro está casi lleno, su índice de Spotlight está dañado o sus permisos no se han reparado por un tiempo, Marked puede tener más dificultades para detectar los cambios en el archivo que está viendo. Optimizar su disco reparando los permisos a menudo será útil, y reconstruir el índice de Spotlight suele ser una solución para los problemas marcados.