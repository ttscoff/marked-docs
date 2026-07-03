<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Hay varias formas de incrustar JavaScripts adicionales en Marked.

## Incluyendo JavaScript por documento

Puede incluir scripts en un solo documento usando etiquetas `<script>` en el contenido mismo. Esto puede ser útil para bibliotecas como [D3](https://d3js.org/) para visualizaciones de datos que solo necesitas en documentos específicos:

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

Si está utilizando MultiMarkdown como procesador, puede incluir secuencias de comandos en los metadatos y se insertarán en el documento. Debido a que Marked genera solo "fragmentos", la clave `XHTML Header` no es ideal. En su lugar, utilice `CSS Header` y los scripts se insertarán en la parte inferior del documento.

	Encabezado CSS: <script src="file.js"></script>

Para que los scripts incluidos se actualicen cuando cambia el contenido, consulte [Hooks](#hooks).

## Incluyendo JavaScript

Puede incluir su propio JavaScript desde archivos locales, CDN o pegando código sin formato. Para acceder a esto, abra {% prefspane Style %} y haga clic en el botón *Reglas personalizadas*.

Configure una nueva regla personalizada o agregue scripts a una existente. Para agregar scripts a cada archivo, establezca el predicado en "el nombre del archivo contiene *".

El editor de acciones para una regla personalizada tiene tres opciones para incluir scripts:

Insertar archivo JavaScript
: Le permite seleccionar un archivo local para insertarlo al final del documento.

Insertar JavaScript desde la URL
: Le permite incluir una CDN u otra URL remota, lo que creará una etiqueta `<script>` al final del documento con la URL vinculada

Insertar JavaScript
: abre un editor de código donde puedes escribir/pegar tu propio código JavaScript.

Estos scripts se insertarán al final de la vista previa, antes de la etiqueta del documento. Si necesita llamar a una función de inicio o actualizar cada vez que se actualiza la vista previa, consulte [Incluyendo JavaScript sin formato](#rawjs) y familiarícese con los [ganchos](#hooks) de Marked.

## Sirena y otros guiones {#mermaid}

jQuery está incluido de forma predeterminada y puede usarlo en cualquier script que agregue a Marked usando cualquiera de los métodos siguientes.

[Sirena](https://mermaid.js.org/intro/) para diagramas similares a Markdown ahora se incluye de forma predeterminada en todos los documentos. Cualquier bloque de código delimitado con el lenguaje `mermaid` se representará automáticamente como un diagrama.

En la parte inferior de {% prefspane Style %}, hay una casilla de verificación disponible para "Diagramas de panorámica y zoom" cuando hay contenido de Mermaid. Al marcar esta casilla, los diagramas se ampliarán con {% kbd cmd %}-desplazamiento y se desplazarán haciendo clic y arrastrando. El script para esta función se incluye desde una CDN y requiere una conexión a Internet.

Si hay una biblioteca en particular que le gustaría que se incluyera de forma predeterminada, hágamelo saber en el [foro BrettTerpstra.com](https://forum.brettterpstra.com/) o a través de [el sitio de soporte](https://support.markedapp.com/questions/add).

## Ganchos [ganchos]

A partir de versiones recientes, Marked ya no realiza una actualización de página completa al actualizar el contenido, sino que inyecta el nuevo contenido en el DOM sin necesidad de cargar la página. Esto significa que los scripts que se incluyeron y que se activan al cargar la página no se volverán a activar cuando se actualice el contenido. Marked proporciona una función de "ganchos" para adaptarse a esto. Para registrar un gancho, debe incluir un segundo bloque de secuencia de comandos que llame a la [`Marked.hooks.register()` función](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor), que acepta un activador, en este caso 'actualizar', y una función para ejecutar.

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// Re-run your D3 visualization when content updates
		d3.selectAll('.chart').each(function() {
			// your D3 render logic here
		});
	});
</script>
```

Toda la [funcionalidad API](https://markedapp.com/jsapi/) de Marked se puede utilizar en este campo. (También puede usar la API en cualquier script cargado). Para depurar interactivamente y experimentar con la API en una vista previa en vivo, consulte la sección [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) para obtener detalles sobre el uso del menú Desarrollar de Safari con Marked.

Ahora, cada vez que se realiza una actualización (cada vez que se guarda el archivo fuente observado), se ejecutará la función pasada. Siempre que el script que estás ejecutando tenga una función de inicio o renderizado de algún tipo, puedes llamarlo con un gancho y hacer que se renderice cada vez que se guarde el documento y se active una actualización.



*[CDN]: Red de distribución de contenidos