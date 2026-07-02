<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked utiliza mucho JavaScript para proporcionar las funciones que ofrece en la vista previa. Por este motivo, pueden surgir bastantes complicaciones cuando se incluyen scripts dentro del cuerpo del documento.

## Guiones externos

Puede incluir algunos scripts externos usando una línea de metadatos "Encabezado CSS:" en la parte superior de su documento. Estos scripts no se insertarán en el encabezado, sino en el pie de página después de que los scripts de jQuery y Marked ya se hayan cargado. Esto es ideal en la mayoría de los casos. Es posible que aún experimentes un comportamiento inesperado, ya que Marked no puede compensar todos los posibles conflictos de secuencias de comandos. Los cambios de DOM pueden ser especialmente problemáticos.

    Encabezado CSS: <script src="file.js"></script>

## En línea incluye

Existen muchas aplicaciones para que JavaScript aparezca en el cuerpo de un documento, como generadores de gráficos u otras herramientas de Canvas. Dependiendo de los ajustes de configuración y del procesador que esté utilizando, estos suelen estar estropeados. La solución es colocar su script y elementos DOM adicionales en un archivo externo y usar la sintaxis de Marked para [archivos de inclusión "sin formato"][sintaxis]. Estos archivos no se procesan de ninguna manera; su contenido se agrega al archivo una vez que se completa el resto del procesamiento.

    Texto de rebajas.

    <<{archivo.html}

    Más texto de rebajas...

Para experimentar y depurar el JavaScript que se ejecuta en la vista previa de Marked, puede adjuntar el Inspector web de Safari a la ventana de vista previa siguiendo los pasos en [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector).

[syntax]: Special_Syntax.html#includingunprocessedtextorhtml