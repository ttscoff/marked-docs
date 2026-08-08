<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked puede abrir documentos PDF (`.pdf`) directamente. Arrastre un archivo a Marcado o use {% appmenu File, Open... ({{cmd}}O) %}. El documento se convierte a Markdown para obtener una vista previa y exportar.

La importación de PDF funciona mejor en **PDF más pequeños basados ​​en texto** (diapositivas, artículos, informes breves). Se admiten manuales, libros y documentos escaneados de gran tamaño, pero a menudo se convierten de forma lenta o imperfecta; consulte **Limitaciones** a continuación.

Marked sigue siendo una herramienta de **vista previa**: no editas el PDF dentro de Marked. Utilice {% kbd cmd E %} para abrir el PDF en **Vista previa** (o el valor predeterminado de su sistema) y Marcado se actualiza cuando el archivo cambia en el disco.

## Cómo funciona la conversión [how-conversion-works]

La importación de PDF utiliza la biblioteca [pdf22md](https://github.com/twardoch/pdf22md) (Licencia MIT; consulte [Licencia pdf22md](PDF22MD_License.html)). La conversión ejecutada marcada en segundo plano mientras muestra un breve aviso de **Conversión**.

El convertidor:

- Extrae **texto** de archivos PDF digitales usando PDFKit
- Utiliza **Vision OCR** en páginas donde falta texto incrustado (común con escaneos)
- Detecta **títulos** según el tamaño de fuente cuando sea posible
- Guarda **imágenes** en una carpeta `assets` junto al Markdown generado

Marked **no** habilita la limpieza de IA opcional de pdf22md en la aplicación. La calidad de la conversión depende de cómo se creó el PDF.

## Caché y vista previa en vivo [cache-and-live-preview]

Markdown y las imágenes convertidas se almacenan en la caché de Watchers de Marked (`~/Library/Caches/Marked/Watchers/PDF/`). La ruta del PDF original sigue siendo la fuente del documento para visualizar archivos.

Cuando guarda o reemplaza el PDF en otra aplicación, Marked detecta el cambio y lo vuelve a convertir automáticamente (el mismo comportamiento de recarga fusionada que [RTF](RTF_Support.html) y [Scrivener](Scrivener_Support.html)).

## Exportación y otras funciones [export-and-other-features]

Después de la conversión, Marked trata el documento como otras fuentes compiladas: la exportación, las estadísticas y la mayoría de las funciones de vista previa se ejecutan en función del Markdown generado. Las rutas de las imágenes en la vista previa apuntan a los recursos almacenados en caché hasta que los exporte.

## Limitaciones [limitations]

Establezca sus expectativas en consecuencia: PDF-to-Markdown es útil, no perfecto.

**Lo que funciona bien**

- **PDF basados en vectores y texto** con texto real incrustado (exportado desde Word, Pages, InDesign, etc.)
- **Extensión moderada**: unas pocas docenas de páginas suelen convertirse en un tiempo razonable y con una buena estructura.

**Lo que no es confiable**

- **OCR (PDF escaneados)**: Vision completa el texto faltante, pero la precisión suele ser deficiente en comparación con una herramienta de OCR dedicada; espere errores tipográficos, palabras entrecortadas y columnas perdidas
- **Tablas**: el diseño se adivina a partir de las posiciones del texto; Las celdas fusionadas, las tablas anidadas y las cuadrículas complejas rara vez sobreviven como tablas Markdown limpias.
- **Ubicación de la imagen**: las figuras se extraen a `assets/`, pero la alineación, los títulos y el ajuste del texto alrededor de las imágenes no se conservan de manera confiable

**Tamaño y rendimiento**

- **Los PDF de gran tamaño** (guías de usuario, libros de texto, manuales extensos) pueden tardar **mucho tiempo** en convertirse, consumir mucha memoria o no producir Markdown útil. Marked sigue respondiendo mientras la conversión se ejecuta en segundo plano, pero no hay garantía de que un manual de 500 páginas finalice correctamente
- Si la conversión se completa con poco o ningún contenido, Marcado muestra un error en lugar de dejar una vista previa en blanco.

**Otros límites**

- **Los archivos PDF protegidos con contraseña** no son compatibles con la versión 1
- **Las imágenes PDF incrustadas en Markdown** (`![]()` que hacen referencia a un archivo `.pdf`) no están relacionadas con la importación de PDF: solo abrir un `.pdf` como documento principal activa la conversión

Para documentos de Word, utilice [Trabajar con DOCX](Working_With_DOCX.html). Para texto enriquecido, utilice [Soporte RTF y RTFD](RTF_Support.html).

## Temas relacionados [related-topics]

- [Abrir archivos](Opening_Files.html): arrastrar y soltar, Abrir recientes, portapapeles
- [Exportar](Exporting.html): guarda HTML, PDF, DOCX y Markdown desde la vista previa
- [Licencia pdf22md](PDF22MD_License.html) — texto de licencia MIT de terceros