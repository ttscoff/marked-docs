<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked puede abrir documentos en formato de texto enriquecido (`.rtf`) y RTFD (`.rtfd`) directamente. Arrastre un archivo a Marcado o use {% appmenu File, Open... ({{cmd}}O) %}. El documento se convierte a Markdown para obtener una vista previa y exportar.

Esto funciona bien con documentos de **Pages**, **TextEdit**, **Word** y otras aplicaciones que guardan RTF o RTFD. Marked sigue siendo una herramienta de **vista previa**: se edita en la aplicación original y Marked se actualiza cuando se guarda.

## Cómo funciona la conversión [how-conversion-works]

Marked convierte RTF a HTML utilizando el motor de texto del sistema y luego a Markdown. El convertidor:

- Asigna **tamaños de fuente de párrafos grandes** a niveles de encabezado (en relación con el tamaño de cuerpo más común en el documento)
- Conserva **negrita**, *cursiva* y enlaces siempre que sea posible
- Extrae **imágenes** de paquetes RTFD y archivos adjuntos incrustados
- **No** trata los nombres de archivos RTF como títulos de imágenes (consulte las imágenes a continuación)

Se utiliza el mismo proceso de conversión para la compilación Scrivener RTF y para los archivos RTF incluidos en otros documentos.

## Vista previa en vivo [live-preview]

Cuando guarda el archivo RTF o RTFD en otra aplicación, Marked detecta el cambio y actualiza la vista previa automáticamente.

## Imágenes [images]

RTF no define un campo de "título" separado de la forma en que Cocoa exporta a HTML. Lo que parece un título en su diseño suele ser **texto normal** en el siguiente párrafo, y Marked lo mantiene como texto del cuerpo.

Las imágenes incrustadas y las imágenes dentro de paquetes RTFD (por ejemplo, `pastedGraphic.png` en una exportación de páginas) se copian a una carpeta de caché en `~/Library/Caches/Marked/Watchers/`. Las rutas de las imágenes de vista previa apuntan a esos archivos almacenados en caché hasta que los exporte.

Marked **no** usa el nombre del archivo de la imagen como texto alternativo o título de figura de MultiMarkdown. No deberías ver `pastedGraphic.png` debajo de la imagen a menos que hayas escrito ese texto en el documento.

## Exportación y otras funciones [export-and-other-features]

Después de la conversión, Marked trata el documento como otras fuentes compiladas (similar a [Scrivener](Scrivener_Support.html) y [DOCX](Working_With_DOCX.html)): exportación, estadísticas y la mayoría de las funciones de vista previa se ejecutan contra el Markdown generado almacenado en la caché de Watchers.

## Limitaciones [limitations]

La calidad de la conversión depende de la aplicación de origen. En general:

- Los **Títulos** se deducen del tamaño de fuente, no de los estilos de esquema de Word/Pages.
- **El diseño complejo** (tablas de varias columnas utilizadas solo para posicionamiento, cuadros de texto) puede no asignarse claramente a Markdown
- **Las ecuaciones** en RTF no se admiten en la vista previa (consulte [MathJax](MathJax.html) para las matemáticas de Markdown)
- **Legacy `.doc`** (Word binario) no es compatible; guardar como DOCX o RTF primero

Para pegar una sola vez sin guardar un archivo, utilice [Vista previa del portapapeles](Opening_Files.html#from-the-clipboard) en su lugar.

## Temas relacionados [related-topics]

- [Soporte PDF](PDF_Support.html): abre documentos PDF como fuentes de Markdown
- [Trabajar con DOCX](Working_With_DOCX.html) -- Documentos de Word con seguimiento de cambios y comentarios
- [Abrir archivos](Opening_Files.html): arrastrar y soltar, Abrir recientes, portapapeles
- [Exportar](Exporting.html) -- Copiar texto enriquecido y guardar RTFD (exportar), distinto de abrir RTF como archivo fuente