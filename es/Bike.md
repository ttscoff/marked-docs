# <%= @title %>

Arrastre un esquema de [Bike][bike] a Marked para verlo como una lista Markdown anidada, con las filas de título en negrita y las tareas como casillas de verificación. Un esquema suelto es un archivo `.bike`. Bike 2 guarda un paquete `.biked` cuando el esquema contiene imágenes incrustadas.

## Abrir un esquema de Bike [opening-a-bike-outline]

Marked convierte el esquema al abrir el archivo:

- Las filas marcadas como título pasan a ser elementos de lista en **negrita**.
- Las tareas pasan a ser casillas al estilo de GitHub. Una tarea aparece marcada cuando Bike guarda una hora de finalización o la marca como hecha.
- Los enlaces y el formato en línea del texto de la fila se conservan como Markdown.

Abrir un archivo `.bike` usa siempre esta lista. No convierte el esquema en un diagrama Mermaid. Un paquete `.biked` sigue el ajuste **Bike outlines** que se describe más abajo.

## Incluir un esquema de Bike [including-a-bike-outline]

Un archivo `.bike` también se puede incluir en otro documento Markdown. Consulte [Incrustar mapas mentales y esquemas](Embedding_Mind_Maps_and_Outlines.html).

En {% prefspane Apps %}, en *Mind Maps and Outlines*, **Bike outlines** se aplica a los archivos incluidos:

- **Activado** (el valor predeterminado): un diagrama Mermaid. El nombre del archivo, sin `.bike`, es el nodo raíz.
- **Desactivado**: la misma lista Markdown anidada que al abrir el archivo, sin título de documento.

## Esquemas con imágenes [outlines-with-images]

Bike 2 guarda un paquete `.biked` cuando el esquema contiene imágenes incrustadas. El paquete es un TextBundle: `text.bike` y una carpeta `assets`. Abra el archivo `.biked`. Marked lee el esquema que hay dentro y pone el nombre del paquete en el título de la ventana.

Desactive **Bike outlines** para ver ese paquete como la lista anidada, que conserva las imágenes incrustadas. **Activado** convierte el esquema en un diagrama Mermaid.

[bike]: https://www.hogbaysoftware.com/bike/
