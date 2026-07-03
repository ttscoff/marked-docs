<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Si un archivo incluido mediante [sintaxis de inclusión de Marked o sintaxis de bloque de IA Writer][incluir] tiene una extensión CSV o TSV, Marked intentará analizarlo y convertirlo en una tabla MultiMarkdown. Esto funciona con la mayoría de los formatos estándar, incluidos los separados por comas y tabulaciones, así como con separadores adicionales y formatos de citas que se detectan automáticamente.

Una ventaja de utilizar archivos CSV en lugar de escribir tablas Markdown es que los saltos de línea dentro de las celdas se convierten automáticamente en etiquetas `<br>`. Esto debe hacerse manualmente para incluir saltos de línea al escribir tablas MultiMarkdown, por lo que ahorra tiempo adicional.

Como nota al margen, hay una excelente aplicación llamada [TableFlip][] que facilita mucho la edición de tablas dentro de su documento. Vale la pena echarle un vistazo si trabaja frecuentemente con datos tabulares.

Los archivos CSV incluidos se observarán en busca de cambios, por lo que se pueden realizar ediciones adicionales en el archivo CSV original y Marked actualizará automáticamente la vista previa al guardar.

Las tablas convertidas se incluirán en la exportación de Markdown, por lo que Marked se puede utilizar para compilar documentos que contengan datos estructurados y exportar un solo archivo.

[include]: Multi-File_Documents.html
[TableFlip]: http://tableflipapp.com/