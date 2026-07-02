<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked proporciona valores predeterminados para mejorar la tipografía y el diseño de exportación, además de ofrecer un control limitado sobre las opciones si necesita más personalización.

## Tipografía

### Separación de sílabas y viudas

La opción _Separación automática de guiones en párrafos_ permite a Marked determinar dónde sería mejor dividir una línea con guiones para mejorar el "trapo" de un párrafo. Esto es más útil cuando se utiliza un estilo con alineación justificada, pero también puede mejorar el flujo de lectura en párrafos más largos.

La opción _Evitar viudas en titulares y párrafos_, si está habilitada, forzará saltos en titulares y párrafos para evitar que palabras cortas y únicas terminen solas en una línea.

Marked conecta automáticamente los titulares con el siguiente elemento, para evitar titulares huérfanos al exportar a un formato paginado (PDF, impresión).

### Signos de puntuación

Si su procesador está configurado en MultiMarkdown, tendrá la opción de habilitar o deshabilitar la "puntuación inteligente" usando la opción _Generar comillas y puntuación tipográficamente correctas_. Si está habilitado, las comillas dobles y simples emparejadas se convertirán en comillas "rizadas", los apóstrofes se reemplazarán con símbolos tipográficamente correctos y se realizarán otros ajustes automáticos.

### Marcadores de notas al pie

En la sección Diseño y tipografía de {% prefspane Style %}, _Marcadores de notas al pie rodeados con corchetes_ está habilitado de forma predeterminada cuando se utiliza el procesador MultiMarkdown y crea marcadores de notas al pie dentro del documento que están rodeados por corchetes (por ejemplo, "[1]"). Para deshabilitar la creación de corchetes, desmarque esta opción.

## Modo de esquema

El modo esquema mostrará cualquier archivo que contenga una serie jerárquica de encabezados como un esquema APA o decimal. El valor predeterminado es el estilo APA, pero se puede desactivar.

En {% prefspane Style %}, en "Diseño y tipografía", puede agregar extensiones de nombre de archivo para las cuales el modo Contorno se habilita automáticamente. Esto es especialmente útil para OPML y archivos de mapas mentales compatibles (como iThoughtsX y MindNode). La extensión debe ser solo la parte alfanumérica del nombre del archivo que aparece después del último punto.

Cambie el modo de esquema predeterminado con la casilla de verificación _Usar estilo APA_. Esto se puede alternar temporalmente desde el menú Engranaje de una ventana de documento.


## poesía

La opción _Estilizar bloques de código textual como poesía_ en {% prefspane Style %} hará que los bloques con sangría de 4 o más espacios se muestren usando el estilo de "poesía" del tema. Suele ser una sección en cursiva y sin resaltado de sintaxis.

Los saltos de línea se conservan en estos bloques de forma predeterminada, por lo que proporciona una manera fácil de incorporar secciones de poesía y lírica en un documento que no necesita otros bloques de código.

> Esta configuración agrega una clase de cuerpo de "poesía" que se puede usar en temas personalizados para diseñar bloques de código y otros elementos cuando el "modo de poesía" está habilitado.

## Ajuste de bloque de código

_Permitir que los temas ajusten texto dentro de bloques de código_ permite que el estilo de vista previa determine cómo formatear los bloques de código. Deshabilitar esta opción obliga a todos los bloques de código a desplazarse horizontalmente en lugar de ajustarlos, independientemente del estilo de vista previa actual.

## Trabajando en pantalla completa

Al utilizar Marcado en modo de pantalla completa (Control-Comando-F), es posible que desee limitar el ancho del texto mostrado para crear una columna centrada de contenido legible. La casilla de verificación _Limitar ancho de texto en vista previa_ habilitará un control deslizante con el que podrá definir el ancho máximo del contenido mostrado. Esto también afecta la visualización en pantalla no completa.