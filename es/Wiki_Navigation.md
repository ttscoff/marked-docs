<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked incluye un sistema de navegación wiki que le permite saltar rápidamente entre archivos de texto relacionados mediante enlaces `[[wiki]]` simples. Este sistema está diseñado para una navegación fluida y funciona mejor cuando se configura para abrir enlaces en la ventana actual.

## Configuración óptima [optimal-settings]

Para usar enlaces wiki, habilite **Convertir `[[wiki links]]`** en {% prefspane Preview %} y configure la extensión predeterminada que Marked usará cuando busque archivos coincidentes.

Para obtener la mejor experiencia, establezca **"Los enlaces a archivos de texto deben abrirse en:"** en *"la ventana actual"* en {% prefspane Apps %}. Esto garantiza que la navegación se sienta natural y se preserve la historia.

Si **Resaltar errores de sintaxis de Markdown** está habilitado en {% prefspane Proofing %}, la sintaxis de `[[wiki link]]` que no coincide con un nombre de archivo en el directorio actual se resaltará en rojo para indicar que el archivo al que se hace referencia no existe. Estos aspectos destacados se actualizarán a medida que se agreguen archivos, pero solo después de guardar o volver a cargar el archivo actual. Al hacer clic en el enlace de un archivo faltante resaltado, se le ofrecerá crear un nuevo archivo, agregando la extensión predeterminada si es necesario. El nuevo archivo vacío se abrirá en Marcado y, si está habilitado Editar nuevos documentos, su editor se abrirá con el nuevo archivo.

## Cómo funcionan los enlaces Wiki [how-wiki-links-work]

- **Enlaces Wiki** utilizan el formato: `[[wiki link]]`.
- Cuando haces clic en un enlace wiki, Marked buscará un archivo coincidente en el **mismo directorio** que el documento actual.
- El archivo debe tener la extensión especificada en la configuración de Marked (p. ej., `.md`), a menos que proporcione un nombre de archivo completo con extensión en el enlace (p. ej., `[[notes.txt]]`).
- Si desea utilizar texto para el enlace que difiere del nombre del archivo, agréguelo después de una barra vertical (`|`) en el enlace, por ejemplo. `[[wiki linking|A note about linking]]`, que se mostrará como `[A note about linking](wiki-link.md)`.
- Si un enlace wiki comienza con `#`, se verá como un enlace ancla en la misma página. Los nombres de los anclajes se normalizan usando minúsculas y reemplazando todos los espacios con guiones. Para procesadores que crean ID de encabezado sin guiones (como MultiMarkdown), p. `## wiki links` obtiene una identificación de `wikilinks`, esta navegación podría fallar. En esos casos, especifique la identificación del enlace correcto, con una barra vertical y un título si es necesario, por ejemplo. `[[#wikilinks|#wiki links]]`.

### Nombres de archivos coincidentes [matching-file-names]

Cuando utiliza un enlace como `[[wiki link]]`, Marked buscará un archivo con cualquiera de los siguientes nombres (suponiendo que su extensión predeterminada sea `.md`):

- `wiki link.md`
- `WikiLink.md`
- `wiki-link.md`
- `Wiki-Link.md`
- `wiki_link.md`
- `Wiki_Link.md`
- `wikilink.md`
- `WikiLink.md`
- (y otras combinaciones de espacios, guiones, guiones bajos e intercaps)

**Todas las coincidencias no distinguen entre mayúsculas y minúsculas y son flexibles con separadores.**
Si especifica una extensión en el enlace (por ejemplo, `[[notes.txt]]`), Marked buscará ese archivo exacto.

## Vínculos de retroceso [backlinks]

Cuando se abre un archivo de texto y se habilita la navegación wiki, el resto de los archivos en el directorio se escanearán en busca de `[[links]]` hasta el archivo actual. Esto sucederá en segundo plano y el documento abierto se actualizará con una lista de vínculos de retroceso, si se encuentra alguno. Para ver los vínculos de retroceso, la barra lateral de comentarios debe estar abierta. Si está cerrado, use el menú de ajustes (**Revisión->Mostrar comentarios**) o presione {% kbd ^@c %} para abrirlo.


## Historial de navegación [navigation-history]

Marked rastrea su navegación a través de enlaces wiki, lo que le permite moverse **hacia adelante y hacia atrás** a través de su historial de archivos, como un navegador web.

- **Volver:** {% kbd @[ %}
- **Adelante:** {% kbd @] %}

También puede utilizar el menú **Historial** para saltar a cualquier archivo visitado anteriormente.