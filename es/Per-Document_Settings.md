<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado permitirá que ciertos atributos de un documento se establezcan en formato de metadatos MultiMarkdown (detallado a continuación). Puede usarlos para definir características y estilos que solo afectan a ese documento sin alterar la configuración predeterminada.

La vista previa ignora la mayoría de los encabezados de MultiMarkdown, pero los siguientes están permitidos y afectan la representación. Puede incluir otros metadatos que se representarán en el resultado final. Marcado simplemente ignorará las claves que no se enumeran a continuación. Si guarda como HTML y *no* incluye una plantilla, Marked representará todas las claves de metadatos como se esperaba.

## Formato de metadatos [metadata-format]

Los metadatos se ingresan en la parte superior del archivo Markdown o inmediatamente después de cualquier encabezado YAML. Consisten en una clave, seguida de dos puntos, espacios o tabulaciones opcionales y el valor:

	Metadatos de ejemplo: clave de ejemplo

Varias entradas de metadatos deben estar en sus propias líneas, pero sin saltos de línea entre ellas. La última entrada de metadatos debe ir seguida de una línea en blanco antes del inicio del texto del documento.

	Primero: esta es la primera entrada de metadatos.
	Segundo: esta es la segunda entrada.
	Tercero: la última entrada de metadatos

	# El comienzo del texto del documento.

## Claves de metadatos marcadas [marked-metadata-keys]

### Ocultar metadatos para otros procesadores [hidingmeta]

**Nota:** Si está utilizando un procesador personalizado o publicando su Markdown directamente en una fuente que no procesa estos metadatos, aún puede usarlo agregando marcadores de comentarios HTML antes y después de los metadatos. A diferencia de MultiMarkdown y otros procesadores, Marked ubicará estas etiquetas en cualquier parte del documento y las procesará/eliminará de la salida. Por lo tanto, lo siguiente en el encabezado proporcionará los resultados que desea en Marcado, pero no aparecerá en ningún otro lugar:

	<!--
	Estilo marcado: Mi estilo personalizado
	Procesador personalizado: verdadero
	-->

*Solo asegúrese de que la clave de metadatos comience al principio de la línea, sin espacios ni tabulaciones, y no coloque nada más en la línea después del valor.*

### Estilos por documento [per-document-styles]

La tecla "Estilo marcado:" establecerá un estilo de vista previa para el documento. El valor puede ser el nombre de un estilo predeterminado o un nombre o ruta para cualquier [Estilo personalizado](Custom_Styles.html) que haya definido en la configuración. Si se encuentra esta clave y coincide con un estilo que Marked conoce, ese estilo se utilizará para la vista previa cada vez que se cargue el documento que la contiene.

**Ejemplo**

	Estilo marcado: ciudadano honrado

### Idioma de las citas [quotes-language]

De forma predeterminada, Marked utiliza comillas al estilo inglés. Puede modificar esto por documento con la tecla "Idioma de cotizaciones:". Los idiomas disponibles son:

* holandés
* ingles
* francés
* alemán
* guillemets
* sueco

**Ejemplo**

	Cotizaciones Idioma: francés

	Crea «comillas» en francés.

### Nivel de encabezado base [base-header-level]

Puede establecer el nivel de encabezado desde el que Marcado comienza a contar con la tecla "Nivel de encabezado base:". Debe ser un número del 1 al 6 y modificará la forma en que se representan los encabezados "#". Si establece el nivel del encabezado en 3, lo que normalmente sería un encabezado de primer nivel (h1) se representa como un encabezado de tercer nivel (h3), y los encabezados posteriores en la jerarquía se desplazan hacia arriba en 2.

**Ejemplo**

	Nivel de encabezado base: 3

	# Este título se representará como h3

	## Este titular será un h4

	Se representa como:

	<h3>Este título se mostrará como h3</h3>

	<h4>Este titular será un h4</h4>

### Procesadores personalizados [custom-processors]

Como se detalla en [Procesador personalizado](Custom_Processor.html#preprocessor), puede habilitar o deshabilitar un procesador personalizado y un preprocesador personalizado utilizando metadatos:

    Procesador personalizado: verdadero
    Preprocesador personalizado: falso

"verdadero" o "falso" enciende y apaga el preprocesador.

El valor de "Procesador" se puede establecer en "multimarkdown" o "descuento" para forzar el uso de uno u otro de los procesadores internos. Esta configuración por documento no cambiará la configuración predeterminada en {% prefspane Processor %}.

### Imprimir encabezados/pies de página [print-headersfooters]

Puede anular la configuración en {% prefspane Export %} para imprimir encabezados y pies de página usando las siguientes teclas:

	imprimir encabezado a la izquierda:
	Centro de encabezado de impresión:
	imprimir encabezado a la derecha:
	imprimir pie de página a la izquierda:
	Centro de pie de página de impresión:
	imprimir pie de página a la derecha:

Estos pueden incluir [variables de impresión](Exporting.html#headers-and-footers) como `%title`, `%page`, `%total`, etc., así como referencias a otros metadatos usando `%md_[key without spaces]`.

### Imprimir márgenes [print-margins]

Configure los márgenes de página para impresión y salida de PDF paginado con la tecla `Margins:`. Los valores están en puntos; los sufijos como `px`, `pt` y `em` se ignoran. Proporcione dos números para los márgenes vertical y horizontal, o cuatro números para la parte superior, derecha, inferior e izquierda:

	Márgenes: 10 20
	Márgenes: 10, 20, 10, 20

Los márgenes de metadatos anulan la configuración {% prefspane Export %} y los campos de margen en el panel de exportación de PDF.

### Insertando JavaScript [inserting-javascript]

Este método especifica datos que se incluyen en la etiqueta `<head>` del documento. Marked ignora la mayoría de los valores de esta clave, excepto en la salida del documento completo, pero respetará los scripts incluidos de esta manera. Las etiquetas de secuencia de comandos definidas aquí no estarán en el encabezado; sin embargo, se agregarán antes de la etiqueta de cierre `</body>`. jQuery ya está cargado y puedes aprovecharlo en cualquier script que inyecte.

**Ejemplo**

	Encabezado XHTML: <script>(function($){$('#wrapper').fadeOut();})(jQuery);</script>

		-o-

	Encabezado XHTML: <script src="myfancyscript.js"></script>