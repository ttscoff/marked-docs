<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked tiene un editor de estilo incorporado y puede aplicar archivos CSS personalizados.

Puedes usar el editor para crear hermosos estilos, o si conoces suficiente CSS como para ser peligroso, puedes hacer que Marked se vea como quieras.

## Empezando [getting-started]

Hay una galería de estilos personalizados creada por el desarrollador y por los usuarios en [markedapp.com/styles](https://markedapp.com/styles/). La galería le permite obtener una vista previa e instalar estilos directamente en Marked. Cualquier estilo instalado se puede revelar en el Finder para examinarlo y modificarlo. La galería se puede abrir usando un visor interno con {% appmenu Style, Generate a Custom Style %}, o hacer clic en el ícono de lápiz (editar) al lado de cualquier estilo editable en el Administrador de estilos. Si desea editar un estilo incorporado, deberá Primero hay que duplicarlo en el administrador.

También hay un [repositorio de estilos personalizados](https://github.com/ttscoff/MarkedCustomStyles) en GitHub con ejemplos. Siéntete libre de navegar, utilizar y contribuir allí. Si distribuye su tema basándose en uno de los temas básicos, no dude en agregarse a los créditos como colaborador.

Con la capacidad de Marked para usar archivos CSS personalizados, el cielo es el límite al personalizar su Vista previa. Todas las opciones de CSS3 que funcionan en Safari funcionarán en Marked. Con los archivos Markdown predeterminados en Marked, solo hay que manejar unos pocos elementos HTML; todo el contenido está en un div con la identificación de "contenedor", todo lo demás está determinado por el marcado del documento.

Si estás diseñando para uso personal, no hay reglas. Active el seguimiento de CSS con la casilla de verificación debajo del selector de CSS personalizado y cuando edite y guarde su CSS personalizado, se actualizará la vista previa.

**Hay un [tema de esqueleto disponible](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) para comenzar.**

Si planeas compartir tu creación de CSS, hay algunos puntos que debes cubrir. Primero, hay algunas clases de cuerpo a las que se les debe aplicar estilos:

## Clases de cuerpo [body-classes]

Los siguientes estilos deben incluirse en cualquier CSS marcado que se vaya a compartir. Las clases de cuerpo le permiten apuntar y modificar cualquier selector bajo diferentes opciones de preferencia.

### Invertido [inverted]

 Cuando el usuario selecciona {% appmenu Preview, Dark Mode %}, se agrega una clase de "invertido" a la etiqueta del cuerpo. Puede utilizar esto para apuntar a estilos claros sobre oscuros de alto contraste.

Solo desea que los estilos invertidos se apliquen a la vista previa, no a la impresión, así que use una consulta de medios (@media screen) para restringirlo. El código siguiente es bastante multiusos y en la mayoría de los casos puede simplemente colocarlo en su hoja de estilo para compatibilidad, pero siéntase libre de modificarlo.

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### Poesía [poetry]

El usuario puede elegir si el texto con tabulación es poesía o código. La única diferencia es que los bloques pre/código tienen un estilo más poético si se elige el modo poesía. La clase "poesía" se aplica a la etiqueta del cuerpo.

Sea tan creativo como quiera con el formato, pero aquí tiene un fragmento básico:

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## Casos especiales [special-cases]

También se deben considerar las tablas, la figura/pie de figura y el caso especial de `a.footnote` y `div.footnotes>a`. No hay reglas establecidas sobre cómo manejarlos, pero eche un vistazo a los estilos predeterminados para tener una idea de qué reglas CSS necesita Marked.

El estilo de tabla estándar en todos los estilos predeterminados utiliza transparencia en las filas alternas para que se combine suavemente con cualquier fondo. Puedes copiar esos estilos o seguir tu propio camino, ¡solo asegúrate de haberlos diseñado! Lo mismo para figura y leyenda de figura; agregue una imagen a un documento con texto alternativo para ver cómo quedará el marcado y el estilo adecuado.

Las notas al pie incluidas en un documento mostrarán un enlace dentro del contenido (a.footnote) y un div al final con el texto al que se hace referencia (div.footnotes). Nuevamente, consulte los estilos predeterminados como referencia. Para evitar cambiar la altura de la línea en líneas que contienen un número de referencia de nota al pie, asegúrese de incluir algo como:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Para mantener la flecha de retorno en la misma línea, incluya:

```css
.footnotes p {display:inline}
```

También es una buena idea incluir una regla general para que todas las imágenes se mantengan dentro del ancho de la página. Algo como:

```css
#wrapper img { max-width: 100% }
```

Si su tema tiene relleno adicional o un ancho fijo, modifique el ancho máximo para que se ajuste.

## Estilos de impresión [printstyles]

Asegúrese de incluir estilos de impresión que eliminen colores de fondo, desplazamiento fijo y la interfaz solo de vista previa. Marked ofrece dos formas de orientar la salida de impresión y PDF.

### `@media print` [media-print]

Las reglas CSS de impresión estándar se aplican al imprimir desde Marked o cuando la exportación a PDF usa medios de impresión:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### La clase `.mkprinting` [the-mkprinting-class]

Cuando Marked prepara un documento para **exportación a PDF** o **vista previa de impresión/PDF** ({% kbd cmd P %}), añade la clase `mkprinting` a la etiqueta `<body>` (junto con clases de exportación como `bandw`, `breakAfterTOC` y la clase `mkstyle--*` de su estilo). Los temas integrados de Marked usan esta clase para la mayoría de las reglas específicas de impresión, en lugar de depender solo de `@media print`.

La exportación a PDF a menudo carga el WebView de renderizado oculto con medios de **pantalla** (sobre todo con estilos personalizados y documentos [Fountain](Fountain_for_Screenwriters.html)), de modo que los bloques `@media print` de su hoja de estilo **pueden no** aplicarse a la salida PDF. Las reglas con el prefijo `.mkprinting` sí se aplican durante la exportación porque son selectores de clase normales, no consultas de medios.

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Para estilos que deben funcionar **tanto** al imprimir desde el navegador como al exportar PDF desde Marked, duplique las reglas críticas o combine selectores:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

Al depurar CSS de impresión personalizado, abra la vista previa de impresión/PDF o exporte a PDF y use el [Web Inspector de Safari](#webkitinspector) para inspeccionar el documento: el `<body>` tendrá la clase `mkprinting` mientras el diseño de impresión esté activo.

La ocultación de enlaces en la impresión se maneja fuera del tema principal, lo que permite a los usuarios elegir que los resaltados y subrayados de enlaces queden ocultos en la impresión. Mientras tenga un estilo base para el texto, no necesita preocuparse por esto.

Así que manos a la obra. Convierta el tema de su blog, cree un estilo de impresión excelente para PDF o prepare la vista previa perfecta para su forma de escribir. Si crea algo genial, [compártalo con la comunidad](https://markedapp.com/styleshare/).

## Configuraciones CSS adicionales [additional-css-settings]

En {% prefspane Style %} puede editar CSS adicional. Estos estilos se añaden a cualquier tema cargado y sirven para aplicar cambios universales a todos los temas.

Con [alta especificidad](#overridingspecificity), consultas `@media` para impresión y pantalla, y selectores `.mkprinting` para la exportación a PDF, puede controlar casi todos los aspectos del estilo con un poco de conocimiento de CSS.

## Inspector de WebKit [webkitinspector]

El inspector web de Safari es la forma más sencilla de ver exactamente qué HTML y CSS marcado se generan y de experimentar con estilos personalizados en vivo.

### Habilitar el menú Desarrollar en Safari [enabling-the-develop-menu-in-safari]

1. Abra Safari y elija {% appmenu Safari, Settings… %}.
2. Seleccione la pestaña **Avanzado**.
3. Habilite **Mostrar funciones para desarrolladores web** (o **Mostrar menú Desarrollar en la barra de menú** en versiones anteriores de macOS).

Una vez habilitado, aparecerá un menú **Desarrollar** en la barra de menú de Safari.

![Menú Desarrollo de Safari que muestra documentos marcados][develop-menu]

### Inspeccionar un documento marcado [inspecting-a-marked-document]

1. Con una ventana de vista previa abierta en Marcado, cambie a Safari.
2. En la barra de menú, elija **Desarrollar → _\<nombre de su Mac\>_ → Marcado → _\<título del documento\>_**.
3. Safari abrirá una ventana del Inspector web adjunta a la vista previa marcada seleccionada.

Desde aquí puedes:

- Utilice la pestaña **Elementos** para inspeccionar el DOM dentro del `#wrapper` div y ver qué reglas CSS se aplican.
- Pase el cursor sobre los elementos en el árbol DOM para resaltarlos en la ventana Marcada.
- Utilice la barra lateral **Estilos** para modificar las reglas en vivo, luego copie los fragmentos de trabajo nuevamente en un estilo personalizado o **CSS adicional**.
    - Después de editar CSS en la pestaña Elementos, puede obtener un resumen de sus ediciones seleccionando la pestaña Cambios

	![Cambios][css-changes]
- Utilice la pestaña **Consola** para ejecutar JavaScript en la vista previa en vivo. La [API JavaScript marcada](https://markedapp.com/help/jsapi/) completa está disponible en esta consola.
- Explore otras pestañas como **Red** al depurar recursos cargados por su documento.

![Inspeccionar una vista previa marcada con Safari Web Inspector][inspecting]

## Compartir CSS personalizado [sharing-custom-css]

Utilice {% appmenu Style, Share a Custom Style %} para abrir la aplicación para compartir en su navegador web. Arrastre su CSS a la zona de colocación (o haga clic para seleccionar desde el disco) y cargue el CSS para su estilo personalizado.

Los estilos compartidos deben ser aprobados por el desarrollador antes de que aparezcan en la galería, por lo que no verás resultados inmediatos.

## Otros consejos [other-tips]

### Especificidad primordial [overridingspecificity]

Dentro de la vista previa marcada, se agrega una clase de cuerpo basada en el nombre de archivo del estilo actual. Si la vista previa está configurada en "Suizo", habrá una clase en la etiqueta `<body>` llamada `mkstyle--swiss`. Si su CSS personalizado se llama MyCustom.css, entonces la clase del cuerpo será `mkstyle--mycustom`. Puede usar esto antes de las reglas definidas en los estilos base para anularlas. Para obtener especificidad absoluta en una regla, use también el ID #wrapper del div contenedor:

	.mkstyle--mycustom #wrapper p+p {...}

### Estilo del índice [table-of-contents-styling]

Si usa el token `<!--toc-->` para [insertar una tabla de contenido](Special_Syntax.html#tableofcontents), puede anular la configuración de los indicadores de nivel de la tabla de contenido en un estilo personalizado usando el "#wrapper" para aumentar la especificidad:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Esto haría que todos los elementos de la lista en la Tabla de contenido usen una viñeta cuadrada en lugar de lo que se definió en Configuración cuando su Estilo personalizado está activo.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
