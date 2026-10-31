# <%= @title %>

Marked incluye un editor de estilos integrado y puede aplicar archivos CSS personalizados.

Puedes usar el editor para crear estilos preciosos, o si sabes lo justo de CSS como para ser peligroso, puedes hacer que Marked luzca como quieras.

## Primeros pasos [getting-started]

Existe una galería de Estilos personalizados creados por el desarrollador y por los usuarios en [markedapp.com/styles](https://markedapp.com/styles/). La galería te permite previsualizar e instalar Estilos directamente en Marked. Cualquier Estilo instalado se puede mostrar en Finder para examinarlo y modificarlo. La galería se puede abrir usando un visor interno con {% appmenu Style, Generate a Custom Style %}, o haciendo clic en el icono del lápiz (editar) junto a cualquier estilo editable en el Gestor de estilos. Si quieres editar un estilo integrado, primero tendrás que duplicarlo en el gestor.

También hay un [repositorio de Estilos personalizados](https://github.com/ttscoff/MarkedCustomStyles) en GitHub con ejemplos. Siéntete libre de explorarlo, usarlo y contribuir allí. Si distribuyes tu tema basado en uno de los temas base, no dudes en añadirte a los créditos como colaborador.

Con la capacidad de Marked de usar archivos CSS personalizados, no hay límites a la hora de personalizar tu vista previa. Todas las opciones de CSS3 que funcionan en Safari funcionarán en Marked. Con los archivos Markdown predeterminados en Marked, solo hay unos pocos elementos HTML que necesitas gestionar; todo el contenido está dentro de un div con el id "wrapper", y el resto depende del marcado de tu documento.

Si estás diseñando para uso personal, no hay reglas. Activa el seguimiento de CSS con la casilla debajo del selector de CSS personalizado y, cuando edites y guardes tu CSS personalizado, la vista previa se actualizará.

**Hay disponible un [tema esqueleto](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) para empezar.**

Si planeas compartir tu creación CSS, hay algunos puntos que debes cubrir. En primer lugar, hay ciertas clases del body que necesitan tener estilos aplicados:

## Clases del body [body-classes]

Los siguientes estilos deben incluirse en cualquier CSS de Marked que se vaya a compartir. Las clases del body te permiten apuntar y modificar cualquier selector según las distintas opciones de preferencias.

### Invertido [inverted]

Cuando el usuario selecciona {% appmenu Preview, Dark Mode %}, se añade una clase "inverted" a la etiqueta body. Puedes usar esto para apuntar a los estilos de alto contraste, claro sobre oscuro.

Solo quieres que los estilos invertidos se apliquen a la vista previa, no a la impresión, así que usa una consulta de medios (@media screen) para restringirlo. El siguiente código es bastante genérico y en la mayoría de los casos puedes simplemente incluirlo en tu hoja de estilos para garantizar la compatibilidad, pero siéntete libre de ajustarlo.

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

El usuario puede elegir si el texto con sangría de tabulación es poesía o código. La única diferencia es que los bloques pre/code se estilizan de forma más, digamos, poética si se elige el modo poesía. La clase "poetry" se aplica a la etiqueta body.

Ponte tan creativo como quieras con el formato, pero aquí tienes un fragmento básico:

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

Las tablas, Figure/Figcaption y el caso especial de `a.footnote` y `div.footnotes>a` también deben tenerse en cuenta. No hay reglas fijas sobre cómo gestionarlos, pero echa un vistazo a los estilos predeterminados para hacerte una idea de qué reglas CSS necesita Marked.

El estilo de tabla estándar en todos los estilos predeterminados usa transparencia en las filas alternas para que se integre suavemente con cualquier fondo. Puedes copiar esos estilos, o seguir tu propio camino, ¡solo asegúrate de haberles dado estilo! Lo mismo aplica para figure y figcaption; añade una imagen a un documento con texto alternativo para ver cómo queda el marcado y aplícale el estilo correspondiente.

Las notas al pie incluidas en un documento generarán un enlace dentro del contenido (a.footnote), y un div al final con el texto referenciado (div.footnotes). De nuevo, consulta los estilos predeterminados como referencia. Para evitar cambiar el interlineado en las líneas que contienen un número de referencia de nota al pie, asegúrate de incluir algo como:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Para mantener la flecha de retorno en la misma línea, incluye:

```css
.footnotes p {display:inline}
```

También es buena idea incluir una regla general para todas las imágenes, de modo que se mantengan dentro del ancho de la página. Algo como:

```css
#wrapper img { max-width: 100% }
```

Si tu tema tiene relleno adicional o un ancho fijo, ajusta el max-width según corresponda.

## Estilos de impresión [printstyles]

Asegúrate de incluir estilos de impresión que eliminen cualquier color de fondo, desplazamiento fijo y elementos de interfaz exclusivos de la vista previa. Marked te ofrece dos formas de dirigirte a la salida de impresión y PDF.

### `@media print` [media-print]

Las reglas CSS de impresión estándar se aplican al imprimir desde Marked o cuando la exportación a PDF usa medios de impresión:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### La clase `.mkprinting` [the-mkprinting-class]

Cuando Marked prepara un documento para **exportación a PDF** o **Vista previa de impresión/PDF** ({% kbd cmd P %}), añade la clase `mkprinting` a la etiqueta `<body>` (junto con clases de exportación como `bandw`, `breakAfterTOC`, y la clase `mkstyle--*` de tu estilo). Los temas integrados de Marked usan esta clase para la mayoría de las reglas específicas de impresión, en lugar de depender únicamente de `@media print`.

La exportación a PDF a menudo carga el WebView de renderizado oculto con medios **screen** (especialmente para estilos personalizados y documentos [Fountain](Fountain_for_Screenwriters.html)), por lo que los bloques `@media print` de tu hoja de estilos pueden **no** aplicarse a la salida en PDF. Las reglas con el prefijo `.mkprinting` siempre se aplican durante la exportación porque son selectores de clase normales, no consultas de medios.

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

Para estilos que deben funcionar tanto en impresión desde el navegador como en la exportación a PDF de Marked, duplica las reglas críticas o combina selectores:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**Estilo personalizado frente a CSS adicional.** En una hoja de estilos de Estilo personalizado, escribe `.mkprinting #wrapper …` como se muestra arriba. En el campo **CSS adicional**, Marked reescribe los selectores antes de la inyección; usa en su lugar la forma calificada con body:

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Consulta [Ajustes de CSS adicional](#additional-css-settings) para saber cómo funciona la reescritura y por qué `.mkprinting #wrapper …` por sí solo no coincide ahí.

Al depurar CSS de impresión personalizado, abre la Vista previa de impresión/PDF o exporta a PDF, y luego usa el [Inspector web de Safari](#webkitinspector) para inspeccionar el documento; el `<body>` tendrá la clase `mkprinting` mientras el diseño de impresión esté activo.

Ocultar enlaces en la impresión se gestiona fuera del tema principal, lo que permite a los usuarios elegir si quieren ocultar los resaltados y subrayados de los enlaces en la impresión. Mientras tengas definido un estilo base para el texto, no necesitas preocuparte por esto.

Así que, adelante. Convierte el tema de tu blog, crea un estilo de impresión excelente para documentos PDF, o diseña la vista previa perfecta para el tipo de escritura que haces. Si creas algo genial, [compártelo con la comunidad](https://markedapp.com/styleshare/).

## Ajustes de CSS adicional [additional-css-settings]

En {% prefspane Style %}, puedes editar **CSS adicional**. Estas reglas se **añaden al tema que esté cargado**, sea cual sea. Son una superposición parcial deliberada, no un tema completo. Si pegas una hoja de estilos completa en este campo —o importas esa misma hoja parcial a través del [Gestor de estilos](Custom_Styles.html) como si fuera un tema—, todo lo que la hoja no cubra quedará sin estilo.

### Reescritura de selectores [additional-css-selector-rewriting]

Marked reescribe los selectores del CSS adicional antes de inyectarlos (como `body.mk-has-additional-css …`) para que las reglas permanezcan delimitadas a la vista previa:

- Una parte de selector que ya empiece por `body` o `#wrapper` recibe el prefijo `body.mk-has-additional-css`, con las clases del body combinadas en lugar de anidadas.
- Cualquier otra parte del selector queda delimitada bajo `body.mk-has-additional-css #wrapper …`.
- Las clases del body iniciales que Marked establece en `<body>` —incluyendo `.mkprinting`, `.inverted`, `.poetry`, `.bandw`, `.breakAfterTOC` y `.mkstyle--*`— se tratan como `body` y se combinan con el selector body en lugar de anidarse bajo `#wrapper`.

| Introducido en CSS adicional | Resultado |
| :-- | :-- |
| `#wrapper h2` | Coincide (correctamente delimitado) |
| `body.mkprinting #wrapper p` | Coincide durante impresión/PDF |
| `.mkprinting #wrapper p` | **No** coincide (requeriría un `#wrapper` anidado) |
| `:root { --x: 1; }` | **No** coincide (se prefiere `body` o `#wrapper` para propiedades personalizadas) |

Para las reglas de impresión en este campo, se prefiere `body.mkprinting #wrapper …`. La misma intención visual en un archivo de Estilo personalizado puede mantener la forma más corta `.mkprinting #wrapper …`.

No hay **límite de tamaño ni comprobación de validez CSS** en el CSS adicional. Marked almacena e inyecta lo que introduzcas; el CSS no válido simplemente no tiene efecto en la vista previa.

### HTML y otras exportaciones [additional-css-exports]

El CSS adicional se aplica en la vista previa en vivo, la Vista previa de impresión/PDF, la exportación a PDF y la **exportación a HTML** cuando se incluyen los estilos; el `<body>` exportado recibe la clase `mk-has-additional-css` para que los selectores reescritos coincidan. DOCX, ODT y EPUB usan sus propias rutas de estilo y no aplican el CSS adicional de la misma manera.

Usando [alta especificidad](#overridingspecificity), consultas `@media` para impresión y pantalla, y selectores `body.mkprinting` (en este campo) o selectores `.mkprinting` (en Estilos personalizados), puedes controlar prácticamente todos los aspectos de estilo con un poco de conocimiento de CSS.

## Inspector web de WebKit [webkitinspector]

El Inspector web de Safari es la forma más sencilla de ver exactamente qué HTML y CSS está generando Marked, y de experimentar con Estilos personalizados en vivo.

### Habilitar el menú Desarrollo en Safari [enabling-the-develop-menu-in-safari]

1. Abre Safari y elige {% appmenu Safari, Settings… %}.
2. Selecciona la pestaña **Avanzado**.
3. Activa **Mostrar funciones para desarrolladores web** (o **Mostrar el menú Desarrollo en la barra de menús** en versiones anteriores de macOS).

Una vez activado, aparecerá un menú **Desarrollo** en la barra de menús de Safari.

![Menú Desarrollo de Safari mostrando documentos de Marked][develop-menu]

### Inspeccionar un documento de Marked [inspecting-a-marked-document]

1. Con una ventana de vista previa abierta en Marked, cambia a Safari.
2. En la barra de menús, elige **Desarrollo → _\<nombre de tu Mac\>_ → Marked → _\<título del documento\>_**.
3. Safari abrirá una ventana del Inspector web conectada a la vista previa de Marked seleccionada.

Desde aquí puedes:

- Usar la pestaña **Elementos** para inspeccionar el DOM dentro del div `#wrapper` y ver qué reglas CSS se aplican.
- Pasar el cursor sobre los elementos en el árbol DOM para resaltarlos en la ventana de Marked.
- Usar la barra lateral **Estilos** para ajustar reglas en vivo, y luego copiar los fragmentos que funcionen de vuelta a un Estilo personalizado o a **CSS adicional**.
    - Después de editar CSS en la pestaña Elementos, puedes obtener un resumen de tus ediciones seleccionando la pestaña Cambios

	![Cambios][css-changes]
- Usar la pestaña **Consola** para ejecutar JavaScript contra la vista previa en vivo. La [API de JavaScript de Marked](https://markedapp.com/help/jsapi/) completa está disponible en esta consola.
- Explorar otras pestañas como **Red** al depurar recursos cargados por tu documento.

![Inspeccionando una vista previa de Marked con el Inspector web de Safari][inspecting]

## Compartir CSS personalizado [sharing-custom-css]

Usa {% appmenu Style, Share a Custom Style %} para abrir la aplicación de compartir en tu navegador web. Arrastra tu CSS a la zona de destino (o haz clic para seleccionarlo desde el disco) y sube el CSS de tu Estilo personalizado.

Los estilos compartidos deben ser aprobados por el desarrollador antes de aparecer en la galería, así que no verás resultados inmediatos.

## Otros consejos [other-tips]

### Anular la especificidad [overridingspecificity]

Dentro de la vista previa de Marked, se añade una clase de body basada en el nombre de archivo del estilo actual. Si la vista previa está configurada en "Swiss", habrá una clase en la etiqueta `<body>` llamada `mkstyle--swiss`. Si tu CSS personalizado se llama MyCustom.css, la clase del body será `mkstyle--mycustom`. Puedes usar esto antes de las reglas definidas en los estilos base para anularlas. Para obtener especificidad absoluta en una regla, usa también el ID #wrapper del div contenedor:

	.mkstyle--mycustom #wrapper p+p { ... }

### Estilo de la tabla de contenidos [table-of-contents-styling]

Si usas el token `<!--toc-->` para [insertar una tabla de contenidos](Special_Syntax.html#tableofcontents), puedes anular los ajustes de los indicadores de nivel de la Tabla de contenidos en un Estilo personalizado usando "#wrapper" para aumentar la especificidad:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Esto haría que todos los elementos de lista de la Tabla de contenidos usaran una viñeta cuadrada en lugar de lo definido en Ajustes cuando tu Estilo personalizado esté activo.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
