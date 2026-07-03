<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

{% apponly div %}
*Para obtener la última versión de esta documentación, visite la [versión en línea][ayuda].*
{% endapponly %}

**Asegúrate de revisar la creciente colección de [videos tutoriales marcados](https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ).**

## ¿Qué es Markdown?

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

Markdown es un lenguaje de marcado básico que utiliza símbolos simples, lo que le permite escribir HTML (y exportar a otros formatos) con una sintaxis simple como `*italics*` y `**bold**`. Markdown fue creado por John Gruber y se está convirtiendo rápidamente en el estándar de facto para la publicación web, la toma de notas e incluso la publicación de libros. Le permite escribir sin un montón de barras de herramientas y sin necesidad de formatear, simplemente colocando palabras en la página y dejando que sus procesadores (como Marked) se encarguen del estilo y el formato.

Marked funciona con GitHub Flavored Markdown, CommonMark (GFM), Kramdown y MultiMarkdown, y puede convertir la sintaxis de varias variantes para obtener una vista previa (también se puede ampliar para que funcione con casi cualquier procesador que necesite, incluidos Textile, reStructuredText, Wikitext y más). Supongo que, ya que estás aquí, sabes cuál es al menos uno de estos lenguajes de marcado. De lo contrario, deberías comenzar con [Conceptos básicos de Markdown][daringfireball] de John Gruber, consulta [MarkdownGuide.org][mdguide]. Marked incluye una guía completa de sintaxis de Markdown en el menú de ayuda.

Puede utilizar [Markdown Dingus](x-marked-3://dingus) para experimentar con los diferentes tipos de Markdown que admite Marked.

## ¿Qué está marcado?

Marked es una aplicación de vista previa de Markdown en vivo para macOS: una aplicación de vista previa de (Multi)Markdown independiente del editor que observa un archivo en busca de cambios y actualiza la vista previa cada vez que lo guarda. Al separar y automatizar los detalles del formato, le permite concentrarse más en la escritura y menos en la presentación, todo ello sin dejar de controlar el producto final.

Para configurar flujos de trabajo e inicios rápidos específicos del editor, consulte [Vista previa de Live Markdown en Mac](Live_Markdown_Preview_on_Mac.html). Para obtener una descripción general más breve del producto, visite [markedapp.com/markdown-preview](https://markedapp.com/markdown-preview/).

Marked funciona con cualquier archivo accesible localmente, incluidos los documentos de iCloud. Simplemente arrastre un documento de texto desde la barra de herramientas de cualquier editor a Marcado y lo representará como una vista previa HTML y comenzará a rastrear los cambios, actualizando la vista previa a medida que escribe. Incluso puede compilar [documentos de varios archivos](Multi-File_Documents.html) usando una sintaxis básica de "inclusión", o desde los formatos de índice Scrivener, Leanpub y mmd_merge.

Marked tiene características adicionales, incluido el recuento de palabras y otras estadísticas de documentos, la capacidad de flotar sobre otras aplicaciones o atenuarse en segundo plano, y puede mostrar su trabajo en una variedad de estilos bien diseñados. Puede imprimir o imprimir documentos PDF, Word, documentos HTML completos (incluidos estilos e imágenes) o copiar datos fuente HTML o RTF a su portapapeles con solo presionar una tecla. Marked también tiene un diccionario AppleScript básico y un [controlador de URL](URL_Handler.html) que facilitan la integración en su flujo de trabajo.

Ah, sí, y funciona con un montón de tus aplicaciones favoritas: editores de texto que van desde Vim y Emacs hasta Sublime Text y TextMate, editores de Markdown como MultiMarkdown Composer, Byword e iA Writer, incluso aplicaciones que quizás no esperes como Ulysses, Scrivener, VoodooPad, MarsEdit y más.

## Usos de ejemplo

Marked convierte cualquier editor de texto en un editor habilitado para Markdown. Su vista previa siempre está disponible y se actualiza a medida que trabaja.

* Si su editor favorito no ofrece una vista previa de Markdown en vivo, abra el documento en el que está trabajando en Marked y mueva la ventana hacia un lado para disfrutar de una experiencia de escritura de Markdown con todas las funciones.
* ¿Te gusta escribir o bloguear en MacVim u otro editor basado en terminal? Ahora tienes una vista previa de Markdown sincronizada mientras trabajas.
* Marked también ofrece capacidades de visualización más allá de cualquier vista previa de Markdown existente, y puede usarse en su lugar para proporcionar un recuento completo de palabras y estadísticas de documentos, sugerencias de escritura e incluso resaltar errores en el formato de Markdown.
* También puedes usar Marcado sin editor. Simplemente arrastre los archivos Markdown al ícono para obtener una vista previa de ellos, imprimirlos y exportarlos a código fuente PDF, DOC, RTF o HTML. Marked también puede **abrir archivos `.rtf` y `.rtfd`** como documentos fuente ([Soporte RTF y RTFD](RTF_Support.html)).
* En las aplicaciones que guardan automáticamente, encontrarás que la vista previa sigue el ritmo de tu escritura sin ninguna ayuda. Úselo con cualquier editor... o *todos* sus editores.
* ¿Escribir un libro? Marked puede compilar varios archivos para obtener una vista previa completa de su trabajo e incluso observar los archivos incluidos en busca de cambios, actualizando el documento principal cada vez que lo guarda. Incluso puede observar una carpeta completa en busca de cambios, cambiando automáticamente la vista previa a cualquier archivo que esté actualizando actualmente. Cuando esté listo, puede publicar en formatos EPUB, DOCX o TextBundle.
* ¿Trabajas con una plataforma de codificación de IA? Abra una carpeta de plan o documentación en Marked y cada vez que cambie un archivo Markdown en esa carpeta, Marked lo mostrará y se desplazará automáticamente hasta el punto de la edición más reciente. Marked muestra diagramas de sirena y puede manejar todo tipo de sintaxis extendida. Realice un seguimiento de los planos y la documentación mientras trabaja, sin cambiar de archivo.