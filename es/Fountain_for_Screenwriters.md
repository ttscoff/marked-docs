<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Fuente](http://fountain.io/) es un lenguaje de marcado de texto especializado diseñado para escribir guiones. Los guionistas que escriben utilizando la sintaxis de Fountain pueden utilizar Marked para obtener una vista previa de su trabajo. 

Al abrir cualquier archivo con la extensión ".fountain", se habilitará automáticamente la compatibilidad con Fountain para la ventana. Se aplicará una hoja de estilo Fountain predeterminada para vista previa y exportación.

Puede forzar que cualquier documento se procese como Markdown abriendo el menú Engranaje en la parte inferior derecha de la ventana Vista previa y seleccionando **Procesar como Fuente**.

Los encabezados de secciones y escenas aparecerán en la tabla de contenido para una navegación rápida por el guión.

## Guiones [scrippets]

También puede utilizar "scriptets" en un documento normal para procesar y diseñar secciones individuales con Fountain. Simplemente rodee su marcado de Fountain dentro del documento principal con etiquetas `[scrippet]`:

    [guión]
    El texto de tu guión...
    [/script]

También puede utilizar etiquetas estándar de estilo Marcado:

    <!--SCRIPPET-->
    El texto de tu guión...
    <!--/SCRIPPET-->