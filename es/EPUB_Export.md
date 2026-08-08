<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked exporta archivos EPUB totalmente compatibles desde su vista previa de Markdown, diseñados con los mismos temas integrados y personalizados que usa en pantalla y legibles en **Apple Books**, **Kobo** y otros lectores de EPUB estándar.

El flujo de trabajo típico es **primero obtener una vista previa, luego exportar EPUB**: abra o compile su documento en Marked, elija un tema, revise en la vista previa en vivo y luego exporte cuando el libro esté listo.

## Exportar un EPUB [exporting-an-epub]

Abra el [Panel de exportación](Exporting.html#drawer) ({% kbd shift cmd e %}) o use **Guardar como** en el menú de ajustes y elija **EPUB**.

El cuadro de diálogo para guardar EPUB le permite configurar:

* **Título** --- el valor predeterminado es los metadatos de MultiMarkdown o el nombre del archivo
* **Autor** --- el valor predeterminado es su nombre de usuario de macOS; el último autor que ingresa se recuerda para la próxima exportación
* **Fecha** --- Formato ISO; editable al momento de guardar
* **Imagen de portada** --- PNG o JPG opcional; Marcado genera una vista previa de portada predeterminada cuando no hay ninguna configurada

Marked incorpora imágenes locales en el EPUB y puede descargar imágenes remotas para que el archivo final sea autónomo. Los EPUB exportados se validan como XHTML bien formado antes de guardarlos, lo que produce archivos que cumplen con los estándares EPUB de distribución y accesibilidad.

Consulte [Exportar perfiles](Exporting.html#export-profiles) para guardar metadatos EPUB y exportar configuraciones para su uso repetido.

## Estilo con temas integrados [styling-with-built-in-themes]

El **estilo de vista previa** seleccionado para su documento determina la apariencia del EPUB. Todos los temas marcados integrados (Swiss, GitHub, Manuscript y el resto) se pueden aplicar a la exportación a EPUB.

1. Elija un estilo en el menú de estilo de la ventana Vista previa (o establezca un valor predeterminado en {% prefspane Style %}).
2. Revise la tipografía, los títulos, los bloques de código y las imágenes en la vista previa en vivo.
3. Exportar a EPUB --- Marked agrupa el CSS del tema en el paquete EPUB.

Marked también aplica CSS específico de exportación encima de su tema de vista previa para que elementos como notas al pie, tablas y bloques de código resaltados con sintaxis se muestren correctamente en los lectores electrónicos. Los documentos en modo esquema utilizan estilos de exportación optimizados para esquemas; [Leanpub](Multi-File_Documents.html) `Book.txt` los índices utilizan automáticamente el estilo de exportación orientado a Leanpub.

I> Los lectores de EPUB ignoran algunos CSS exclusivos de la web (posicionamiento fijo, trucos de ventana gráfica, etc.). Lo que ves en la vista previa de Marked es el objetivo, pero los motores de diseño de lectores electrónicos pueden simplificar el espaciado y las fuentes. Pruebe en Apple Books o en su lector objetivo antes de publicar.

## Estilo con temas personalizados [styling-with-custom-themes]

[Estilos personalizados](Custom_Styles.html) funcionan de la misma manera para EPUB que para vista previa y PDF:

* Agregue archivos CSS en {% prefspane Style %} o el [Administrador de estilos](Custom_Styles.html).
* Seleccione el tema personalizado antes de exportar.
* Marcado incorpora su hoja de estilo en el EPUB exportado.

Consejos para CSS personalizado compatible con EPUB:

* Mantenga los diseños fluidos: utilice unidades relativas y `max-width: 100%` en las imágenes (`#wrapper img { max-width: 100%; }` es una buena base).
* Evite las `@media print` reglas para el estilo de libros electrónicos; EPUB utiliza los estilos de la pantalla principal más la hoja de estilos de exportación de Marked.
* [Modo oscuro](Previewing.html) la inversión en la vista previa utiliza `@media screen` consultas; la mayoría de los lectores de EPUB utilizan la hoja de estilo clara a menos que la aplicación del lector aplique su propio tema oscuro.
* Utilice [CSS adicional](Custom_Styles.html) en la configuración de Estilo para modificar todos los temas a la vez (por ejemplo, tamaño de fuente de cuerpo uniforme en todas las exportaciones).

Para obtener orientación sobre la creación, consulte [Creación de CSS personalizado](Writing_Custom_CSS.html).

## Resaltado de sintaxis y matemáticas [syntax-highlighting-and-math]

Si **Incluir resaltado de sintaxis en la exportación** está habilitado en {% prefspane Export %}, los bloques de código se exportan con los mismos colores de sintaxis que la vista previa. Las matemáticas renderizadas con [MathJax](MathJax.html) se incluyen en el EPUB según corresponda para la compatibilidad con lectores electrónicos.

## Metadatos en su archivo fuente [metadata-in-your-source-file]

Puede configurar metadatos EPUB en el documento en lugar del cuadro de diálogo para guardar. En la parte superior de un archivo Markdown (o en una página de metadatos de Scrivener), use teclas de estilo MultiMarkdown:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

`cover image` acepta una ruta relativa al documento o una ruta absoluta. Se admiten PNG y JPG. Los valores del cuadro de diálogo anulan o completan los metadatos faltantes en el momento de la exportación.

## Libros de varios archivos [multi-file-books]

Para trabajos largos, compile capítulos con [Documentos de archivos múltiples](Multi-File_Documents.html) --- archivos de índice, exportaciones de Scrivener, Leanpub `Book.txt` o índices estilo GitBook. Marcado observa archivos incluidos, obtiene una vista previa del libro completo y exporta un EPUB desde el HTML compilado.

Los títulos del documento compilado se convierten en el EPUB [tabla de contenido](Document_Navigation.html) para la navegación en Apple Books y otros lectores.

## Lectura y publicación [reading-and-publishing]

Los EPUB exportados se abren directamente en **Apple Books** (haga doble clic en el archivo o use **Archivo → Agregar a la biblioteca**). También funcionan en Kobo, Thorium, Calibre y la mayoría de las aplicaciones compatibles con EPUB 3.

### Libros de Apple [apple-books]

Arrastre un `.epub` exportado a la aplicación Libros o agréguelo a través de **Archivo → Importar**. Se conservan la tipografía personalizada y la portada de su tema Marked. Utilice Apple Books en Mac, iPad o iPhone para verificar el diseño antes de compartir.

### Publicación directa de Kindle (KDP) [kindle-direct-publishing-kdp]

EPUB es un formato de carga aceptado para [Kindle Direct Publishing](https://kdp.amazon.com/). Exporte desde Marcado y cargue el archivo `.epub`; Amazon lo convierte para entrega Kindle. KDP también acepta [DOCX](Working_With_DOCX.html). Consulte los [formatos de libros electrónicos admitidos] (https://kdp.amazon.com/en_US/help/topic/G200634390) de Amazon para conocer los requisitos actuales.

**No se requiere MOBI** para nuevos títulos de KDP. Marked no exporta MOBI.

Opcional: obtenga una vista previa del diseño de Kindle con el [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) gratuito de Amazon antes de cargarlo.

## Relacionado [related]

* [Exportación HTML](HTML_Export.html) --- HTML independiente con estilos e imágenes incrustados
* [Exportar](Exporting.html) --- panel de exportación, perfiles y otros formatos
* [Vista previa de Live Markdown en Mac](Live_Markdown_Preview_on_Mac.html) --- vista previa del flujo de trabajo antes de exportar
* [Estilos personalizados](Custom_Styles.html) y [Generador de estilos personalizados](Custom_Style_Generator.html)
* [Documentos de archivos múltiples](Multi-File_Documents.html) --- índices de libros y capítulos
* [Exportación de AppleScript](AppleScript_Support.html) --- automatizar la exportación a EPUB