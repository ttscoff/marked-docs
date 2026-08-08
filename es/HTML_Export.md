<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked exporta HTML desde su **vista previa en vivo**: el mismo resultado renderizado que ve en la pantalla. Utilice la exportación HTML cuando necesite un fragmento para pegarlo en un blog o CMS, o un archivo `.html` autónomo con estilos e imágenes incrustados que pueda abrir en cualquier navegador o host en cualquier lugar.

El flujo de trabajo típico es **primero obtener una vista previa, luego exportar HTML**: abra o compile su documento en Marked, elija un tema, revise en la vista previa en vivo y luego exporte cuando el marcado se vea bien.

## Dos formas de obtener HTML [two-ways-to-get-html]

### Copiar HTML (fragmento) [copy-html-snippet]

**Copiar HTML** coloca la fuente HTML de la vista previa en el portapapeles, lista para pegar en WordPress, Ghost, Squarespace, un foro, una plantilla de correo electrónico o cualquier aplicación que acepte fragmentos HTML.

* Menú de ajustes → **Copiar HTML**, o {% kbd shift cmd C %} con la vista previa enfocada
* Copia el **HTML del cuerpo renderizado** (no es un documento completo con el contenedor `<html>`)
* Opcional: habilite **Incrustar imágenes al copiar HTML** en {% prefspane Export %} para codificar imágenes locales en Base64 como `data:` URL en la fuente pegada

Copiar HTML es ideal cuando tu destino ya tiene su propia hoja de estilo y solo necesitas el marcado del contenido.

### Guardar HTML (archivo) [save-html-file]

**Guardar HTML** escribe un archivo `.html` completo en el disco.

* Exportar → **Guardar HTML**, {% kbd cmd S %} o **HTML** desde el [Panel de exportación](Exporting.html#drawer) ({% kbd shift cmd e %})
* Elija el nombre del archivo y la ubicación en el cuadro de diálogo para guardar
* Configurar opciones de exportación en el accesorio de diálogo (ver más abajo)

Guardar HTML es ideal para archivar, compartir un archivo independiente o abrir el resultado directamente en un navegador.

## Guardar opciones HTML [save-html-options]

El cuadro de diálogo Guardar HTML incluye un selector de perfiles de exportación y estas opciones:

![Guardar opciones HTML][savehtml]

**Incluir estilo en la salida**

Cuando está marcada, Marcado incrusta el CSS del tema de vista previa seleccionado en un bloque `<style>` dentro del archivo exportado. Elija cualquier tema integrado o [Estilo personalizado](Custom_Styles.html) en el menú de estilo junto a la casilla de verificación. El resultado es un documento HTML completo con `<!DOCTYPE html>`, `<head>` y un `#wrapper` div alrededor de su contenido, que coincide con lo que obtuvo en la vista previa.

Cuando no está marcado, Marked guarda un documento HTML mínimo solo con el contenido renderizado (sin CSS del tema Marked). Utilícelo cuando desee pegar o importar HTML sin formato en otro sistema que proporcione su propio estilo.

**Incrustar imágenes locales para HTML independiente**

Cuando **Incluir estilo en la salida** está habilitado, también puede incrustar imágenes locales como URL Base64 `data:` dentro del archivo HTML. El resultado es un único archivo que puede enviar por correo electrónico, cargar o alojar sin una carpeta `images/` separada.

* Funciona con imágenes a las que se hace referencia mediante **rutas relativas o absolutas** en su disco local
* Evite las URL `file:///`: no se pueden incrustar de manera confiable
* Las imágenes remotas (http/https) permanecen como URL externas a menos que las descargues primero
* La incrustación de Base64 puede producir archivos grandes; Úselo cuando la portabilidad importe más que el tamaño del archivo

**Incluir JavaScript resaltado de sintaxis**

Cuando el resaltado de sintaxis está habilitado en {% prefspane Preview %}, esta opción agrega CSS y JavaScript resaltado.js desde una CDN para que los bloques de código mantengan sus colores en el archivo exportado. El HTML exportado necesita una conexión a Internet para que se carguen los recursos CDN.

**Incluye enlace CDN de MathJax o KaTeX**

Cuando [MathJax](MathJax.html) o KaTeX está habilitado para la vista previa, puede incluir los scripts CDN coincidentes en el HTML guardado para que las ecuaciones se representen en un navegador. Al igual que el resaltado de sintaxis, esto requiere acceso a la red al visualizar el archivo, a menos que usted mismo aloje los scripts.

**Tipo de exportación CriticicMarkup**

Los documentos con [CriticMarkup](CriticMarkup.html) pueden elegir si la exportación muestra texto editado, texto original o marcado completo.

**Exportar perfil**

Seleccione un [Perfil de exportación](Exporting.html#export-profiles) guardado para restaurar su configuración de exportación HTML preferida (estilos incrustados, imágenes, resaltado de sintaxis, matemáticas) en un solo paso.

## Estilo con temas integrados y personalizados [styling-with-built-in-and-custom-themes]

El **estilo de vista previa** controla la apariencia HTML cuando se marca **Incluir estilo en la salida**:

1. Elija un estilo en el menú de estilos de la ventana de vista previa (o establezca un valor predeterminado en {% prefspane Style %}).
2. Revise la tipografía, los títulos, los bloques de código y las imágenes en la vista previa en vivo.
3. Guarde HTML con el mismo estilo seleccionado en el cuadro de diálogo de exportación.

Todos los temas Marked integrados (Swiss, GitHub, Manuscript y el resto) se pueden incrustar. [Estilos personalizados](Custom_Styles.html) y los estilos del [Administrador de estilos](Custom_Styles.html) funcionan de la misma manera.

I> Es posible que algunos CSS de solo vista previa (posicionamiento fijo, trucos de ventana gráfica, modo oscuro `@media screen` inversión) no se traduzcan uno a uno fuera de Marcado. Abra el archivo guardado en un navegador para verificarlo antes de publicarlo.

Para obtener orientación sobre la creación, consulte [Creación de CSS personalizado](Writing_Custom_CSS.html).

## Metadatos y encabezados MultiMarkdown [metadata-and-multimarkdown-headers]

Los metadatos de MultiMarkdown en la parte superior de su archivo fuente pueden afectar la exportación HTML:

* **`Title:`** --- utilizado para el elemento `<title>` al guardar un documento HTML completo
* **`XHTML Header:`** / **`HTML Header:`** --- inyecta etiquetas adicionales en el `<head>` exportado (scripts, etiquetas de enlace, metaetiquetas)
* Otras claves de metadatos se procesan de acuerdo con su [procesador Markdown](Choosing_a_Processor.html)

Si utiliza metadatos para la configuración de exportación pero no desea que las claves sean visibles en otras salidas, envuélvalas en comentarios HTML. Marcado busca y procesa metadatos comentados en cualquier parte del documento. Consulte [Configuración por documento](Per-Document_Settings.html).

## Documentos de varios archivos [multi-file-documents]

Para compilaciones de libros y capítulos, utilice [Documentos de archivos múltiples](Multi-File_Documents.html). Marked obtiene una vista previa del documento combinado y exporta un archivo HTML a partir del resultado compilado. Los archivos incluidos están marcados con comentarios HTML que muestran sus rutas de origen, lo que resulta útil al auditar qué capítulo contribuyó con qué sección.

## Pegar en otras aplicaciones [pasting-into-other-applications]

| Destino | Enfoque sugerido |
| :-- | :-- |
| Blog/CMS con temática propia | **Copiar HTML** (fragmento, sin CSS marcado incrustado) |
| Sitio estático o archivo | **Guarde HTML** con **Incluir estilo en la salida** |
| Correo electrónico o archivo compartido (un archivo adjunto) | **Guarde HTML** con **Incrustar imágenes locales** |
| WordPress, Ghost, Noción, etc. | **Copiar HTML**; habilitar **Incrustar imágenes al copiar HTML** si el editor no resuelve las rutas locales |
| Edición adicional en un editor de código | **Guarde HTML** sin estilo incrustado o copie el fragmento y ajuste manualmente |

[Copiar texto enriquecido](Exporting.html#rtfexportoptions) (menú de ajustes) es una alternativa cuando la aplicación de destino acepta texto formateado en lugar de fuente HTML.

## Temas relacionados [related-topics]

* [Exportar](Exporting.html) --- panel de exportación, perfiles y otros formatos
* [Exportación EPUB](EPUB_Export.html) --- salida de libro electrónico con CSS integrado
* [Vista previa de Live Markdown en Mac](Live_Markdown_Preview_on_Mac.html) --- vista previa del flujo de trabajo antes de exportar
* [Estilos personalizados](Custom_Styles.html) y [Configuración: Exportar](Settings_Export.html)
* [Configuración específica de HTML](HTML_Specific_Settings.html) --- opciones de procesador para salida HTML
* [Exportación de AppleScript](AppleScript_Support.html) --- automatizar copiar y guardar HTML

[savehtml]: images/SaveHTML.png @2x width=740px height=229px 
r