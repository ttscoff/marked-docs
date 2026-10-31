# <%= @title %>

Marked exporta HTML a partir de tu **vista previa en vivo** --- la misma salida renderizada que ves en pantalla. Usa la exportación a HTML cuando necesites un fragmento para pegar en un blog o CMS, o un archivo `.html` autónomo con estilos e imágenes incrustados que puedas abrir en cualquier navegador o alojar en cualquier lugar.

El flujo de trabajo habitual es **primero vista previa, luego exportar a HTML**: abre o compila tu documento en Marked, elige un estilo, corrige en la vista previa en vivo y exporta cuando el marcado se vea bien.

## Dos formas de obtener HTML [two-ways-to-get-html]

### Copiar HTML (fragmento) [copy-html-snippet]

**Copiar HTML** coloca el código fuente HTML de la vista previa en el portapapeles --- listo para pegarlo en WordPress, Ghost, Squarespace, un foro, una plantilla de correo electrónico o cualquier app que acepte fragmentos HTML.

* Menú de engranaje → **Copiar HTML**, o {% kbd shift cmd C %} con la vista previa enfocada
* Copia el **HTML del cuerpo renderizado** (no un documento completo con el contenedor `<html>`)
* Opcional: activa **Incrustar imágenes al copiar HTML** en {% prefspane Export %} para codificar en Base64 las imágenes locales como URLs `data:` en el código pegado

Copiar HTML es ideal cuando el destino ya tiene su propia hoja de estilos y solo necesitas el marcado del contenido.

### Guardar HTML (archivo) [save-html-file]

**Guardar HTML** escribe un archivo `.html` completo en el disco.

* Exportar → **Guardar HTML**, {% kbd cmd S %}, o **HTML** desde el [panel de exportación](Exporting.html#drawer) ({% kbd shift cmd e %})
* Elige el nombre de archivo y la ubicación en el cuadro de diálogo de guardado
* Configura las opciones de exportación en el accesorio del cuadro de diálogo (ver más abajo)

Guardar HTML es ideal para archivar, compartir un archivo independiente o abrir el resultado directamente en un navegador.

## Opciones de Guardar HTML [save-html-options]

El cuadro de diálogo Guardar HTML incluye un selector de perfil de exportación y estas opciones:

![Opciones de Guardar HTML][savehtml]

**Incluir estilo en la salida**

Cuando está marcada, Marked incrusta el CSS del estilo de vista previa seleccionado en un bloque `<style>` dentro del archivo exportado. Elige cualquier estilo integrado o [Estilo personalizado](Custom_Styles.html) en el menú de estilos junto a la casilla. El resultado es un documento HTML completo con `<!DOCTYPE html>`, `<head>` y un div `#wrapper` alrededor de tu contenido --- igual que lo que viste en la vista previa.

Cuando no está marcada, Marked guarda un documento HTML mínimo solo con tu contenido renderizado (sin el CSS del estilo de Marked). Usa esta opción cuando quieras HTML sin procesar para pegarlo o importarlo en otro sistema que aporte su propio estilo.

**Incrustar imágenes locales para HTML independiente**

Cuando **Incluir estilo en la salida** está activada, también puedes incrustar imágenes locales como URLs `data:` en Base64 dentro del archivo HTML. El resultado es un único archivo que puedes enviar por correo, subir o alojar sin necesidad de una carpeta `images/` aparte.

* Funciona con imágenes referenciadas mediante **rutas relativas o absolutas** en tu unidad local
* Evita las URLs `file:///` --- no se pueden incrustar de forma fiable
* Las imágenes remotas (http/https) permanecen como URLs externas a menos que las descargues antes
* La incrustación en Base64 puede generar archivos grandes; úsala cuando la portabilidad importe más que el tamaño del archivo

**Incluir JavaScript de resaltado de sintaxis**

Cuando el resaltado de sintaxis está activado en {% prefspane Preview %}, esta opción añade el CSS y el JavaScript de highlight.js desde una CDN para que los bloques de código conserven sus colores en el archivo exportado. El HTML exportado necesita conexión a internet para que se carguen los recursos de la CDN.

**Incluir enlace CDN de MathJax o KaTeX**

Cuando [MathJax](MathJax.html) o KaTeX está activado para la vista previa, puedes incluir los scripts CDN correspondientes en el HTML guardado para que las ecuaciones se rendericen en un navegador. Al igual que con el resaltado de sintaxis, esto requiere acceso a la red al ver el archivo, a menos que alojes tú mismo los scripts.

**Tipo de exportación de CriticMarkup**

Los documentos con [CriticMarkup](CriticMarkup.html) pueden elegir si la exportación muestra el texto editado, el texto original o el marcado completo.

**Perfil de exportación**

Selecciona un [perfil de exportación](Exporting.html#export-profiles) guardado para restablecer de un solo paso tus ajustes preferidos de exportación a HTML (estilos incrustados, imágenes, resaltado de sintaxis, matemáticas).

## Estilizado con estilos integrados y personalizados [styling-with-built-in-and-custom-themes]

El **estilo de vista previa** determina la apariencia del HTML cuando **Incluir estilo en la salida** está marcada:

1. Elige un estilo en el menú de estilos de la ventana de vista previa (o establece uno predeterminado en {% prefspane Style %}).
2. Revisa la tipografía, los encabezados, los bloques de código y las imágenes en la vista previa en vivo.
3. Guarda el HTML con el mismo estilo seleccionado en el cuadro de diálogo de exportación.

Todos los estilos integrados de Marked --- Swiss, GitHub, Manuscript y el resto --- se pueden incrustar. Los [Estilos personalizados](Custom_Styles.html) y los estilos del [Administrador de estilos](Custom_Styles.html) funcionan de la misma manera.

El **CSS adicional** de {% prefspane Style %} se incluye en la exportación a HTML cuando los estilos están incrustados. El `<body>` exportado recibe la clase `mk-has-additional-css` para que los selectores reescritos del CSS adicional de Marked coincidan. Consulta [Crear CSS personalizado](Writing_Custom_CSS.html#additional-css-settings).

I> Es posible que parte del CSS exclusivo de la vista previa (posicionamiento fijo, trucos de viewport, inversión de `@media screen` en modo oscuro) no se traduzca de forma exacta fuera de Marked. Abre el archivo guardado en un navegador para comprobarlo antes de publicar.

Para obtener orientación sobre su creación, consulta [Crear CSS personalizado](Writing_Custom_CSS.html).

## Metadatos y encabezados de MultiMarkdown [metadata-and-multimarkdown-headers]

Los metadatos de MultiMarkdown en la parte superior de tu archivo fuente pueden afectar a la exportación a HTML:

* **`Title:`** --- se usa para el elemento `<title>` al guardar un documento HTML completo
* **`XHTML Header:`** / **`HTML Header:`** --- inyecta etiquetas adicionales en el `<head>` exportado (scripts, etiquetas link, etiquetas meta)
* Las demás claves de metadatos se procesan según tu [procesador de Markdown](Choosing_a_Processor.html)

Si usas metadatos para ajustes de exportación pero no quieres que las claves sean visibles en otras salidas, envuélvelas en comentarios HTML --- Marked encuentra y procesa los metadatos comentados en cualquier parte del documento. Consulta [Ajustes por documento](Per-Document_Settings.html).

## Documentos multiarchivo [multi-file-documents]

Para libros y compilaciones de capítulos, usa [Documentos multiarchivo](Multi-File_Documents.html). Marked muestra la vista previa del documento combinado y exporta un único archivo HTML a partir del resultado compilado. Los archivos incluidos se marcan con comentarios HTML que muestran sus rutas de origen --- útil para auditar qué capítulo aportó cada sección.

## Pegar en otras aplicaciones [pasting-into-other-applications]

| Destino | Enfoque sugerido |
| :-- | :-- |
| Blog o CMS con su propio estilo | **Copiar HTML** (fragmento, sin CSS de Marked incrustado) |
| Sitio estático o archivo | **Guardar HTML** con **Incluir estilo en la salida** |
| Correo electrónico o uso compartido de archivos (un adjunto) | **Guardar HTML** con **Incrustar imágenes locales** |
| WordPress, Ghost, Notion, etc. | **Copiar HTML**; activa **Incrustar imágenes al copiar HTML** si el editor no resuelve rutas locales |
| Edición adicional en un editor de código | **Guardar HTML** sin estilo incrustado, o copia el fragmento y envuélvelo manualmente |

[Copiar texto enriquecido](Exporting.html#rtfexportoptions) (menú de engranaje) es una alternativa cuando la app de destino acepta texto con formato en lugar de código fuente HTML.

## Temas relacionados [related-topics]

* [Exportar](Exporting.html) --- panel de exportación, perfiles y otros formatos
* [Exportación a EPUB](EPUB_Export.html) --- salida de libro electrónico con CSS incrustado
* [Vista previa de Markdown en vivo en Mac](Live_Markdown_Preview_on_Mac.html) --- flujo de trabajo de vista previa antes de exportar
* [Estilos personalizados](Custom_Styles.html) y [Ajustes: Exportar](Settings_Export.html)
* [Ajustes específicos de HTML](HTML_Specific_Settings.html) --- opciones del procesador para la salida HTML
* [Exportación con AppleScript](AppleScript_Support.html) --- automatiza la copia y el guardado de HTML

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
