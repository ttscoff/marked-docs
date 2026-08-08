<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[MarsEdit][yo] almacena publicaciones dentro de su base de datos, no como archivos sueltos en el disco. Por lo tanto, Marked utiliza un flujo de trabajo de vista previa dedicado que se comunica con la aplicación MarsEdit en ejecución.

## Ventana de vista previa de MarsEdit [marsedit-preview-window]

Elija {% appmenu File, New, MarsEdit Preview %}. Marked le pide a AppleScript que lea la **publicación frontal en MarsEdit** (se reconocen los ID del paquete de Red Sweater para direct, Mac App Store, Setapp y MarsEdit 4/5). Mantenga MarsEdit ejecutándose con un documento abierto mientras trabaja.

- **Actualización manual:** guarde desde la vista previa de Marked si desea forzar una actualización.
- **Actualizaciones automáticas:** habilita la visualización para que cada guardado automático de MarsEdit actualice Marcado.

Si no hay ninguna publicación disponible, Marcado muestra un breve error en la vista previa en lugar de texto obsoleto.

### Publicaciones extendidas [extended-posts]

El contenido en el campo **extendido** de MarsEdit se separa en la vista previa y la fuente de Marked usando un divisor `<!--more-->` estilo WordPress para que los sitios orientados a la paginación (WordPress, Jekyll, etc.) aún vean la separación. El comentario es inofensivo en otros lugares.

### Etiquetas y categorías en metadatos [tags-and-categories-in-metadata]

Las etiquetas y categorías de MarsEdit están expuestas al bloque de metadatos MultiMarkdown. Con el procesador MultiMarkdown ({% prefspane Processor %}), puedes hacer referencia a ellos como:

    Etiquetado: [%etiquetas]
    Publicado en: [%categorías]

[me]: https://www.red-sweater.com/marsedit/