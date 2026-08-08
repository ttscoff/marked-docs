<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Convirtiendo su Markdown en un documento terminado.

## Exportar después de la vista previa [export-after-preview]

La vista previa de Marked es la base para la exportación: lo que ve en la ventana de vista previa es lo que obtiene en PDF, DOCX, EPUB y otros formatos (configuraciones específicas de exportación de módulo, como márgenes, encabezados y paginación). Configure su estilo y revise primero en la vista previa, luego exporte cuando el documento esté listo. Consulte [Vista previa de Live Markdown en Mac](Live_Markdown_Preview_on_Mac.html) para ver el flujo de trabajo de vista previa completo.

## El panel de exportación [cajón] [drawer]

![Panel de exportación][panel de exportación]

El **Panel de exportación** es un panel estilo foco controlado por teclado que brinda acceso rápido a todas las opciones de exportación. Ábrelo haciendo clic en el icono de exportación en la barra de estado o presionando {% kbd shift cmd e %}.

![Botón Exportar][expbut]

El Panel de exportación le permite guardar su documento como HTML, PDF de una sola página, PDF paginado, paquete RTF o un archivo DOC o DOCX de Microsoft Word. También puede guardar en un nuevo archivo Markdown (las funciones específicas de Markdown se representarán y se incluirán sus resultados), un documento abierto (ODT) o como OPML para usar en otras aplicaciones.

## Copiar HTML [copyhtml]

Utilice la función Copiar HTML para colocar el código fuente HTML para su vista previa en su portapapeles sin ningún problema. Puedes seleccionarlo desde el menú de ajustes o simplemente presionar {% kbd shift cmd C %}. El HTML copiado será un fragmento listo para insertarse en un blog, foro o documento HTML.

No es necesario estar en la vista de código fuente para copiar. Con la vista previa enfocada (haga clic en ella), simplemente escriba {% kbd shift cmd C %} y verá un mensaje emergente que le informará que la fuente está en su portapapeles.

## Guardar HTML [save-html]

![][exportarhtmlaccesorio]



El comando Guardar HTML, accesible desde el menú de ajustes o simplemente escribiendo **{% kbd cmd S %}**, le permitirá guardar un documento completo listo para compartir o publicar.

Opcionalmente, puede incluir cualquiera de los estilos de Marked (o uno de sus [estilos personalizados][personalizado]) en su exportación, lo que le brindará un documento listo para usar con el formato necesario ya incorporado.

Además, puede optar por incrustar cualquier imagen local incluida en el documento dentro del HTML exportado, lo que le permite tener un documento independiente que se puede alojar en cualquier lugar sin necesidad de mover las imágenes con él. Esto solo funciona con imágenes a las que se hace referencia en su disco local con rutas relativas o absolutas. Evite el uso de rutas `file:///` si desea utilizar esta función.

## Exportar Markdown a PDF en Mac [export-markdown-to-pdf-on-mac]

Imprimir/Vista previa de PDF ({% kbd cmd P %}) abrirá un cuadro de diálogo de impresión estándar. Cada estilo de vista previa en Marked tiene sus propios estilos de impresión que eliminan fondos, modifican el tamaño de las letras y proporcionan bordes. La vista previa se imprimirá según el estilo seleccionado actualmente.

En el cuadro de diálogo de impresión se destacan los botones PDF y Vista previa. PDF le brindará una variedad de opciones para exportar a PDF (según sus aplicaciones disponibles) y Preview exportará una versión PDF directamente a Preview.app, donde podrá guardarla o enviarla por correo electrónico.

La impresión en PDF utilizando este método incluirá la paginación. Al imprimir en papel o PDF, los saltos de página se pueden insertar manualmente usando la sintaxis [`<!--BREAK-->`][salto] o configurando opciones en {% prefspane Export %} para usar encabezados de nivel uno y/o nivel dos como divisores de sección.

También existe una preferencia por convertir las reglas horizontales (`<hr>`) en saltos de página al imprimir. Al hacerlo, se reemplazará la línea creada por la etiqueta con un salto de página, eliminándola del resultado final. La vista previa no se ve afectada por esta configuración.

![Imprimir márgenes][imprimir márgenes]

Los márgenes de página se pueden configurar en {% prefspane Export %} y afectarán la salida de Impresión y PDF paginado.

Puede anular la configuración de márgenes por documento usando la tecla de metadatos `Margins:`. Los valores se interpretan como puntos; Los sufijos de unidades como `px`, `pt` y `em` se ignoran. Utilice dos números para los márgenes vertical y horizontal (`10 20`), o cuatro números para los márgenes superior, derecho, inferior e izquierdo (`10, 20, 10, 20` o `10 20 10 20`). Los márgenes de metadatos anulan la configuración {% prefspane Export %}.

### Encabezados y pies de página [headers-and-footers]

Los encabezados y pies de página definidos en {% prefspane Export %} aparecerán en la parte superior e inferior de cualquier página impresa o guardada en un PDF paginado y en la exportación DOCX. Puede colocar cualquier texto en la parte superior izquierda, superior central, superior derecha, inferior izquierda, inferior central e inferior derecha. El texto central está alineado en el centro de la página. Las siguientes variables se reemplazarán en las cadenas si se usan:

    %título = Título del documento
    % fecha = fecha actual
    %tiempo = Hora actual
    %página = Número de página actual
    %total = Número total de páginas
    %path = Ruta del sistema de archivos al documento
    %filename = Solo el nombre de archivo del documento
    %basename = El nombre del archivo sin extensión
    %logo/%image = Un logotipo establecido en la imagen en las preferencias de Encabezado/Pie de página
    %%(texto) = Texto para imprimir solo en la primera página
    %h1/h2/h3/h4/h5/h6 = Títulos de sección basados en encabezados de Markdown
    %sep(X) = Texto para colocar entre los títulos de las secciones si existe una subsección

**Imprima y pague el PDF** resuelva `%h1`--`%h6` usando la paginación de Marked, de modo que cada página muestre la jerarquía de encabezados visible en esa página. Las variables de metadatos `%sep(X)` y `%md_*` también se admiten en la salida impresa/PDF.

**Exportación DOCX** incrusta `%logo`/`%image` en el encabezado o pie de página de Word (escalado a aproximadamente 50 píxeles de alto, coincidiendo con la vista previa de impresión). Los marcadores de posición de encabezado se convierten en campos **STYLEREF** de Word que hacen referencia a los estilos `Heading 1`--`Heading 6` exportados. Word actualiza esos campos cuando se abre el documento, según el diseño y los saltos de página de Word, no la paginación de vista previa de Marked. `%md_*` las variables de metadatos se sustituyen una vez en el momento de la exportación, igual que en la impresión/PDF. `%sep(X)` no se convierte en encabezados/pies de página DOCX.

`%title` utilizará cualquier información de "Título:" definida en los encabezados de metadatos de MultiMarkdown; de lo contrario, recurrirá al nombre del archivo sin la extensión del archivo. Para definir un título utilizando metadatos MMD, coloque lo siguiente en la primera línea del documento:

    Título: El título de su documento.

Siga la línea con una línea en blanco (o cualquier otro metadato que desee definir, seguido de una línea en blanco).

También puede utilizar cualquier clave de metadatos MMD como variable anteponiendole el prefijo `%md_` y combinando las palabras de la clave como una cadena en minúsculas. Por ejemplo, si su documento tiene una clave de metadatos en la parte superior, como por ejemplo:

    Funky Monkey: El mono más funky

Luego, usar `%md_funkymonkey` en un campo de encabezado colocaría "El mono más original" en el documento exportado en la ubicación de ese encabezado. Los documentos que no contengan esa clave en particular dejarán el campo en blanco, lo que le permitirá agregar encabezados de forma selectiva según los metadatos.

Consulte [Formatos de fecha y hora](Exporting.html#dateandtimeformats) para conocer los códigos de formato `%date` y `%time`.

La configuración "Desplazamiento de numeración de páginas" se puede utilizar para ajustar en qué número comienzan los números de página. Por ejemplo, si tiene una tabla de contenido en la primera página y desea que la numeración comience en la segunda página como página 1, establezca el desplazamiento en -1. La página 2 ahora será la página 1 en el encabezado/pie de página (`%page`) y el total de páginas (`%total`) se ajustará en consecuencia.

También puede especificar una fuente de encabezado/pie de página para un documento específico utilizando metadatos MMD en la parte superior del archivo:

    Fuente del encabezado: Mensch

Tenga en cuenta que si utiliza un nombre de familia de fuentes, se seleccionará una fuente predeterminada. Puede especificar una variación utilizando el nombre del sistema de la fuente. Por ejemplo, en el caso de Helvetica Neue Ultralight, usaría "Fuente de encabezado: HelveticaNeueUltralight".

Además, puede especificar un tamaño de fuente para encabezado/pie de página por documento con los metadatos:

    Tamaño de fuente del encabezado: 10

### Formatos de fecha y hora [dateandtimeformats]

Los campos **Formato de fecha** y **Formato de hora** en {% prefspane Export %} controlan cómo se representan `%date` y `%time` en encabezados y pies de página. Ambos campos utilizan códigos de formato de estilo strftime: un `%` seguido de una letra. El texto literal (como `-`, `:` o espacios) se copia tal cual.

**Ejemplos**

    %m-%d-%Y → 20-06-2026 (formato de fecha predeterminado de Marked)
    %I:%M %p → 3:45 p.m. (formato de hora predeterminado de Marked)
    %Y-%m-%d → 2026-06-20
    %B %d, %Y → 20 de junio de 2026
    %a %H:%M → viernes 15:45

**Códigos de formato común**

| Código | Ejemplo | Descripción |
| ---- | ------- | ----------- |
| `%Y` | 2026 | Año de cuatro dígitos |
| `%y` | 26 | Año de dos dígitos |
| `%m` | 06 | Mes (01--12) |
| `%B` | junio | Nombre del mes completo |
| `%b` | junio | Nombre abreviado del mes |
| `%d` | 20 | Día del mes (01--31) |
| `%e` | 20 | Día del mes (con espacio) |
| `%A` | viernes | Nombre completo del día laborable |
| `%a` | viernes | Nombre abreviado del día laborable |
| `%H` | 15 | Hora, 24 horas (00--23) |
| `%I` | 03 | Hora, 12 horas (01--12) |
| `%M` | 45 | Minuto (00--59) |
| `%S` | 07 | Segundo (00--59) |
| `%p` | PM | AM o PM |
| `%x` | (local) | Fecha preferida del lugar |
| `%X` | (local) | Hora preferida del lugar |
| `%c` | (local) | Fecha y hora preferidas por la localidad |

**Los PDF impresos y paginados** admiten el estilo strftime completo establecido anteriormente, además de códigos adicionales como `%j` (día del año), `%U`/`%W` (número de semana), `%z` (desplazamiento de zona horaria) y `%Z` (nombre de zona horaria). Consulte la [especificación de tiempo de ejecución de Open Group](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html) para obtener una referencia completa.

**Exportación DOCX** admite los códigos enumerados en la tabla anterior. Los códigos menos comunes pueden ignorarse o pasarse sin cambios.

Utilice **Restaurar formatos predeterminados** en {% prefspane Export %} para restablecer a `%m-%d-%Y` y `%I:%M %p`.

### Encabezados y pies de página por documento [per-document-headers-and-footers]

Puede especificar encabezados y pies de página por documento utilizando los metadatos de MultiMarkdown en la parte superior del documento:

    Imprimir encabezado a la izquierda: %título
    Centro de encabezado de impresión: %basename
    Imprimir encabezado a la derecha: %fecha
    Imprimir pie de página a la derecha: %página/%total

Estos anularán cualquier configuración en las preferencias. Tenga en cuenta que si está utilizando un procesador que no sea MultiMarkdown y no desea que sus encabezados aparezcan en el documento, puede usar comentarios HTML, asegurándose de dejar una línea en blanco antes del cierre del comentario:

    <!--
    Imprimir encabezado a la izquierda: %título
    Centro de encabezado de impresión: %basename
    Imprimir encabezado a la derecha: %fecha

    -->

## Guardar PDF [save-pdf]

Esta opción guarda su vista previa directamente en un archivo PDF en su disco. Su documento se mostrará en su totalidad, sin saltos de página. Para incluir paginación en su salida, use las opciones Imprimir/PDF en el [Panel de exportación](#cajón).

## Opciones de exportación RTF [rtfexportoptions]

Marked puede exportar datos RTF (formato de texto enriquecido) directamente a su portapapeles. Simplemente elija el comando Copiar texto enriquecido en el menú de ajustes.

Marked también puede guardar su archivo como un archivo **RTFD** (formato de texto enriquecido). El formato RTFD es un formato de paquete que incluye un archivo RTF y cualquier imagen incrustada en el documento.

## Exportación DOCX [docx-export]

Exportar como DOCX creará un documento válido de Microsoft Word, con elementos como titulares, encabezados/pies de página, énfasis, listas, etc., todos asignados a estilos válidos de Word. Esto significa que puedes aplicar fácilmente tu propio tema en Word.

Consulte [Trabajar con DOCX][DOCX] para obtener más detalles sobre la importación y exportación de Word.

## Exportar rebajas a EPUB [export-markdown-to-epub]

Marked puede exportar documentos EPUB 100% válidos y 100% accesibles. Seleccione el tipo de exportación EPUB, especifique metadatos como título, autor y fecha y, opcionalmente, agregue una foto de portada. El archivo guardado se podrá leer en cualquier visor de EPUB.

Los metadatos necesarios para la exportación a EPUB se pueden incluir en el propio archivo, ya sea un documento Markdown, un archivo Scrivener (incluye una página `metadata`) u otro formato de libro. Las claves a utilizar son:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

La clave Imagen de portada puede incluir una ruta relativa al documento base o una ruta absoluta. Se aceptan archivos PNG o JPG.

Si no se establece el título, de forma predeterminada será el nombre de archivo del documento original, y si no se establece el autor, de forma predeterminada será el nombre completo de su usuario de macOS.

La fecha siempre se establecerá en la fecha actual y actualmente no se puede modificar con metadatos. Sin embargo, se puede modificar al momento de guardar, siempre que el formato (ISO) permanezca intacto.

### Publicación en Amazon Kindle (KDP) [publishing-to-amazon-kindle-kdp]

EPUB es un formato abierto utilizado por muchas aplicaciones y tiendas de lectura (Apple Books, Kobo y otras), no solo Kindle. Si publica a través de [Kindle Direct Publishing (KDP)](https://kdp.amazon.com/), exporte EPUB desde Marked y cargue ese archivo en KDP. Amazon lo convierte a su propio formato de entrega Kindle (KFX) para lectores.

KDP acepta varios formatos de manuscritos, incluidos EPUB y DOCX (que Marked también puede exportar). Consulte los [formatos de libros electrónicos admitidos] (https://kdp.amazon.com/en_US/help/topic/G200634390) y la [guía de formato de manuscritos de libros electrónicos] (https://kdp.amazon.com/en_US/help/topic/G200645680) de Amazon para conocer los requisitos.

**No se requiere MOBI.** KDP ya no acepta cargas MOBI para títulos nuevos (incluidos libros de diseño fijo, a partir de marzo de 2025). Marked no exporta MOBI y no necesita un archivo "Kindle" o Mobipocket por separado para KDP. Si prefiere las herramientas de diseño de Amazon, también puede preparar un libro con [Kindle Create](https://kdp.amazon.com/help/topic/G8UZKZD45RTQNNVT), que produce archivos KPF.

Antes de cargarlo, es posible que desees comprobar cómo se verá tu EPUB en los dispositivos Kindle utilizando el [Kindle Previewer] gratuito de Amazon (https://kdp.amazon.com/help/topic/G202131170). Se trata de un software opcional de terceros de Amazon, que no forma parte de Marked.

## Exportar perfiles [export-profiles]

Los perfiles de exportación le permiten guardar y cambiar rápidamente entre diferentes conjuntos de preferencias de exportación. Esto es especialmente útil si exporta documentos regularmente para diferentes propósitos; por ejemplo, un perfil para archivos PDF listos para imprimir con márgenes y encabezados específicos, y otro para HTML listo para web con estilos incrustados.

### Uso de perfiles de exportación [using-export-profiles]

Cuando inicia Marcado por primera vez, se crea automáticamente un perfil "Predeterminado" con su configuración de exportación actual. Puede ver y seleccionar perfiles en los cuadros de diálogo de exportación (Exportar PDF, Guardar HTML, etc.) usando el menú emergente de perfil en la parte superior del cuadro de diálogo.

**Creando un nuevo perfil:**

1. Ajuste su configuración de exportación en {% prefspane Export %} o en cualquier cuadro de diálogo de exportación
2. En el cuadro de diálogo de exportación, haga clic en el menú emergente del perfil y elija "Agregar perfil..."
3. Ingrese un nombre para su perfil (por ejemplo, "Calidad de impresión" o "Exportación web")
4. La configuración actual se guarda como ese perfil.

**Cargando un perfil:**

- Seleccione un perfil en el menú emergente en cualquier cuadro de diálogo de exportación
- Todas las configuraciones de exportación se actualizarán inmediatamente para coincidir con los valores guardados de ese perfil.

**Guardar cambios en un perfil:**

- Después de realizar cambios en la configuración de exportación, aparece un botón "Guardar" junto a la ventana emergente del perfil.
- Haga clic en "Guardar" para actualizar el perfil actual con sus cambios.
- El botón solo se habilita cuando hay cambios no guardados

**Gestión de perfiles:**

- Elija "Administrar perfiles..." en el menú emergente del perfil para abrir la ventana de administración del perfil.
- Desde allí podrás:
  - **Renombrar** perfiles haciendo doble clic en el nombre
  - **Duplicar** un perfil para crear uno nuevo basado en él
  - **Eliminar** perfiles (el perfil "predeterminado" no se puede eliminar)
  - Ver todos los perfiles disponibles en una lista

### Qué capturan los perfiles de exportación [what-export-profiles-capture]

Los perfiles de exportación guardan todas las preferencias relacionadas con la exportación, incluidas:

- **Configuración de PDF**: tamaño de página, márgenes, encabezados/pies de página, fuentes, saltos de página, tabla de contenido
- **Exportación HTML**: incrustación de estilos, incrustación de imágenes, resaltado de sintaxis, representación matemática
- **Procesamiento de rebajas**: ajuste de texto, formato de enlaces, reglas del procesador
- **CriticMarkup**: tipo de exportación y opciones de procesamiento
- **Resaltado de sintaxis**: preferencias de detección y resaltado de idioma
- **Representación matemática**: integración MathJax/KaTeX y numeración de ecuaciones
- **Manejo de imágenes**: opciones de incrustación, comportamiento de copia, configuración de ruta
- **Tipografía**: Separación de palabras, viudas/huérfanos, tamaños de fuente
- **Comportamiento de exportación**: preferencias de nombres de archivos, resolución de conflictos

Los perfiles funcionan en todos los tipos de exportación: Markdown, HTML, PDF continuo, PDF paginado, EPUB, DOCX, ODT, TextBundle, RTF y OPML.

### Almacenamiento de perfiles [profile-storage]

Los perfiles se almacenan en su carpeta de soporte de aplicaciones en:

    ~/Biblioteca/Soporte de aplicaciones/Marcado/ExportProfiles.plist

Esto significa que sus perfiles persisten incluso si restablece las preferencias de la aplicación y sobreviven a las actualizaciones de la aplicación. Puede hacer una copia de seguridad de este archivo para conservar sus perfiles en todas las instalaciones.

### Consejos para utilizar perfiles de exportación [tips-for-using-export-profiles]

- **Cree perfiles para flujos de trabajo comunes**: si exporta regularmente para impresión o web, cree perfiles separados para cada uno.
- **Utilice nombres descriptivos**: los nombres de perfil como "Imprimir - Carta" o "Web - Estilos integrados" dejan claro para qué sirve cada perfil.
- **Guardar con frecuencia**: el botón "Guardar" aparece siempre que hayas realizado cambios; haz clic en él para conservar tus ajustes.
- **Comenzar desde perfiles existentes**: use "Duplicar" en la ventana de administración para crear variaciones de perfiles existentes en lugar de comenzar desde cero.

[break]: Special_Syntax.html#pagebreaks
[DOCX]: Working_With_DOCX.html
[custom]: Custom_Styles.html
[dropbox]: http://dropbox.com
[expbut]: images/ExportButton.png @2x width=534px height=256px class=center
[export-panel]: images/export-panel-800.jpg @2x width=800 class=center
[exporthtmlaccessory]: images/SaveHTML.png @2x width=740px height=229px class=center
[printmargins]: images/PrintMargins.jpg @2x width=329px height=144px class=center