<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked tiene un manejo especial para comentarios y anotaciones.

## Fuentes de anotaciones

Marked reconoce los comentarios provenientes de:

- Notas al pie de rebajas
- Comentarios de CriticMarkup
- Comentarios y cambios de Microsoft Word.

## La barra lateral de Comentarios

Todas las anotaciones se muestran en una barra lateral y se ocultan en la vista previa del documento. Para mostrar la barra lateral de anotaciones, use el **Menú de ajustes -> Revisión -> Mostrar comentarios** o presione {% kbd ctrl cmd C %}.

![Una nota al pie en la barra lateral de comentarios][barra lateral]

  [barra lateral]: imágenes/comment-sidebar-800.jpg @2x width=800

Al pasar el cursor sobre un comentario en la barra lateral, se dibujará una línea hacia su ubicación en el documento. En el caso de notas al pie, esto indicará dónde aparece la nota al pie en el texto. En el caso de comentarios, apuntará a la ubicación original del comentario, que puede ser un espacio en blanco en la vista previa.

Al hacer clic en un comentario en la barra lateral, se dibujará una animación resaltada que apunta a su ubicación.

La fuente y el estilo de la barra lateral dependen del estilo actual, por lo que puede verse diferente con diferentes estilos.