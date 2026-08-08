<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Coloque una **carpeta** de notas de texto sin formato en Marcado. Marked abre una ventana de vista previa que siempre rastrea el archivo elegible **editado más recientemente** dentro de esa carpeta (.md, .txt, .markdown, etc., que coincida con los filtros de tipo de archivo de Marked).

Las actualizaciones se ejecutan cada vez que se guarda un archivo observado: si el archivo más nuevo coincide con el anterior, Marcado se desplaza hacia la región de edición detectada; cuando cambia de documento, toda la vista previa cambia al archivo activo.

## Funciona bien con nvUltra, nvALT y herramientas similares [works-well-with-nvultra-nvalt-and-similar-tools]

Las aplicaciones de Notebook que dejan archivos individuales en el disco (las clásicas **nvALT**, **nvUltra**, bibliotecas de estilo **Notational Velocity**, carpetas Git sincronizadas, carpetas temporales de Dropbox, etc.) se combinan naturalmente con la observación de carpetas: escribes en una ventana y mantienes Marcado fijado junto a ella sin volver a abrir manualmente las vistas previas.

**nvUltra** también ofrece **[Vista previa de archivo(s) en Marked](nvUltra.html)** en su menú contextual cuando desea abrir notas específicas en Marked directamente en lugar de adjuntar Marked al flujo de observación de carpetas completa descrito anteriormente.

Marked también expone el mismo comportamiento del observador en otros nombres de menú cuando consolidas muchos capítulos pequeños en lo que parece una experiencia de lectura; consulte también [Documentos de archivos múltiples](Multi-File_Documents.html) para manuscritos que combinan intencionalmente múltiples fuentes de Markdown.