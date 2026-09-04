# <%= @title %>

Vea sus documentos a *su* manera.

## Uso de estilos personalizados [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

La forma más sencilla de explorar los Estilos personalizados es a través de la
[Galería de Estilos Personalizados][2]. Allí puede explorar los
estilos disponibles en acción, instalarlos con solo pulsar un
botón, e incluso [enviar sus propias creaciones][6] para
que sean incluidas.

Para agregar hojas de estilo personalizadas desde su disco local a Marked,
use el {% prefspane Style %}. Los nuevos estilos se añadirán a
los menús desplegables en los ajustes de Ventana y en cada ventana,
y se nombrarán según el nombre base del archivo CSS
añadido. Guarde sus archivos CSS personalizados en un lugar seguro de su
disco. Si se mueven de ubicación, se eliminarán de
Marked hasta que los vuelva a agregar desde la nueva ubicación. Es
recomendable cerrar los documentos abiertos y quitar el estilo
de Ajustes antes de eliminar o renombrar un archivo CSS usado
por Marked. No pasa nada grave si no lo hace, pero evita
alguna que otra confusión.

Agregue Estilos personalizados usando el Gestor de Estilos con el botón Añadir, o arrastrando uno o más archivos CSS al panel de
Ajustes.

## Gestión de estilos con el Gestor de Estilos [managing-styles-with-the-style-manager]

Al abrir el Gestor de Estilos obtiene un único lugar para organizar todos los
temas integrados y personalizados. Pulse el botón **Gestionar Estilos…** en el panel
{% prefspane Style %},
o simplemente suelte archivos CSS en la ventana de ajustes: Marked los importará,
abrirá el Gestor de Estilos y seleccionará por usted la fila recién añadida. Arrastrar
archivos CSS directamente sobre la ventana del Gestor de Estilos también funciona; cuando
se arrastran varios archivos verá que la superposición cambia a "Add N Custom Styles" para dejar claro
que está importando un lote.

![][img-style-manager]

Dentro del Gestor de Estilos encontrará una tabla ordenable que combina estilos
integrados y personalizados. Cada fila ofrece:

- Una casilla **Enabled** que agrega o quita de inmediato el estilo del menú
  Estilo, del menú emergente de Estilo predeterminado y de los atajos de teclado. Si desactiva el
  estilo activo actual, se cambia automáticamente a la siguiente entrada disponible.
- Una columna **Name** que puede editar directamente; los cambios persisten y se propagan a todos
  los menús. Pulse sobre el nombre del Estilo para editarlo en el lugar.
- Una columna **Source** que indica si es integrado (Built‑in), personalizado (Custom) o duplicado (Duplicated).
- Un conjunto de **Actions** con botones para **Edit** (abre el archivo CSS en su
  editor), **Duplicate** (crea una copia y un nuevo archivo CSS en el disco), **Reveal**
  (muestra el archivo en el Finder) y **Delete** (con opciones para quitar la referencia o
  mover el archivo CSS a la Papelera).

Las filas se reordenan arrastrando y soltando, y ese orden determina tanto el menú Estilo como
las asignaciones de atajos `⌘/#`, de modo que puede literalmente arrastrar los estilos a las posiciones
que desee. También puede arrastrar archivos CSS externos a posiciones concretas; el indicador de
colocación determina dónde se inserta el nuevo estilo.

### Vista previa en vivo [live-preview]

El panel derecho contiene una vista previa que muestra el estilo seleccionado
dentro de un documento HTML completo con un amplio conjunto de encabezados, listas, tablas, bloques de código, etc. La
vista previa usa el CSS real del disco, así que las ediciones que haga en su editor externo se actualizan al instante. Una casilla activa o desactiva la vista previa en Modo oscuro.

Puede encontrar estilos adicionales para usar (o como ejemplos
para crear los suyos propios) [en GitHub][1] (vea los [ejemplos][2] para
echar un vistazo rápido a lo que hay disponible). Consulte [Crear CSS personalizado][3]
para más detalles y consejos.

## CSS adicional [additional-css]

En {% prefspane Style %}, encontrará una opción
titulada CSS adicional con un botón etiquetado "Edit CSS."
Al pulsar este botón se abre una ventana donde puede agregar
reglas CSS universales que se aplicarán a todos los estilos. Tenga en cuenta
que la especificidad de las reglas puede ser importante al
anular parte del estilo predeterminado de Marked. El cuerpo
principal del documento está envuelto en un div con el id "#wrapper".
Anteponer un selector con esto puede facilitar las
anulaciones, por ejemplo:

    #wrapper img { width: 100%; height: auto; }

El CSS de este campo se **añade al tema activo**. No sustituye
a un Estilo personalizado completo: una hoja de estilo escrita solo para este
campo es deliberadamente parcial, y cargarla mediante el Gestor de Estilos como
tema dejaría sin estilo todo lo que no cubre.

Marked **reescribe** los selectores de CSS adicional antes de inyectarlos. Las clases
iniciales del body, como `.mkprinting`, se combinan en `body` en lugar de
anidarse bajo `#wrapper`, así que las reglas de impresión en este campo deben usar
`body.mkprinting #wrapper …` (consulte [Crear CSS personalizado](Writing_Custom_CSS.html#additional-css-settings) para conocer todas las
reglas de reescritura). No hay límite de tamaño ni comprobación de validez en el campo:
un CSS no válido simplemente no tiene ningún efecto.

El CSS de este campo se aplicará a todos los documentos, sin
importar el Estilo que estén usando, incluida la exportación a HTML cuando se incluyen los estilos. Si desea aplicar CSS
personalizado según coincidencias condicionales, use las acciones Set Style, Insert
CSS File o Insert CSS en las
Reglas personalizadas de {% prefspane Processor %}.

## Exportación a impresión y PDF [print-and-pdf-export]

Marked inyecta un bloque `@media print` integrado (`mkprintstyles`) en cada
vista previa. Este establece valores predeterminados como una base de **10pt** en `html`, `body` y
`#wrapper` (o el tamaño de **Custom font size for export/print** en
{% prefspane Export %} cuando esa opción está activada), y normaliza el
texto de los párrafos con `p { font-size: 1em; }` y `li p { font-size: 1em; }` para que
las reglas exclusivas de pantalla como `p { font-size: 1.1429em; }` no aumenten
el tamaño del cuerpo del texto en los PDF y en la salida impresa.

La exportación a PDF puede usar medios **print** o **screen** en el WebView oculto que se usa para
generarla. Los temas integrados suelen usar el medio print; los **estilos personalizados** y
los documentos [Fountain](Fountain_for_Screenwriters.html) suelen usar el medio screen para que el
diseño coincida con la vista previa. Esto significa que las reglas `@media print { ... }` no
siempre se aplican durante la exportación a PDF.

Para obtener un estilo fiable en PDF e Impresión/Vista previa de PDF, anteponga a los selectores la
clase `mkprinting` que Marked agrega a `<body>` durante la exportación (consulte [Crear CSS
personalizado](Writing_Custom_CSS.html#printstyles) para más detalles y ejemplos). En un archivo
de **Estilo personalizado** puede usar `.mkprinting` solo. En **CSS adicional**,
use la forma calificada por body `body.mkprinting #wrapper …`, porque ese campo
reescribe los selectores. También puede combinar cualquiera de las dos formas con `@media print` cuando
necesite cubrir ambas rutas.

Para establecer tamaños distintos de los valores predeterminados de impresión de Marked, agregue reglas explícitas en
su CSS personalizado (o en CSS adicional). Use `!important` cuando necesite
anular los estilos de impresión inyectados por Marked, por ejemplo:

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

Las reglas sin `!important` pueden perder frente a reglas posteriores en `mkprintstyles` o frente a
otros selectores sin calificar en su hoja que aún se apliquen en impresión. Colocar
los ajustes exclusivos de impresión en `@media print` y/o en reglas `.mkprinting` / `body.mkprinting`
(en lugar de solo en reglas de pantalla) hace que sea más fácil entender el comportamiento
tanto de la vista previa como de la exportación.

## Vigilancia de cambios en el CSS [watching-css-changes]

Puede marcar una casilla en la sección Estilos personalizados de {% prefspane Style %}
para que Marked vigile el archivo CSS activo
además del archivo Markdown que está editando. Cuando
se detectan cambios en cualquiera de los dos archivos, la vista previa se
actualizará. Esto es útil para editar estilos personalizados sin
tener que actualizar constantemente, y también puede usarse para tareas sencillas
de desarrollo web.

Esto también resulta útil para algunos trabajos básicos de diseño web y
experimentación con CSS (como crear estilos personalizados). Cargue un
archivo Markdown que contenga todo el marcado que quiera estilizar,
cree un estilo personalizado y observe la vista previa para ver los cambios en vivo
mientras lo edita.

## Cómo escribir CSS personalizado [writing-custom-css]

Si está familiarizado con CSS, puede crear sus propias hojas de
estilo para usarlas en Marked. Consulte [Cómo escribir CSS personalizado][3] para
más detalles. Cada vez que cree algo nuevo, considere
[enviarlo][6] a la [galería][2] para compartirlo con otros
usuarios. Asegúrese de cubrir los conceptos básicos indicados en la guía, e
incluya el comentario de metadatos al principio.

### Estilos personalizados automáticos con StyleStealer [automatic-custom-styles-with-stylestealer]

Incluso puede generar automáticamente un estilo a partir de un
sitio web existente usando el [Style Stealer][4]. Esto le permite cargar una página web y capturar los estilos calculados de todos los elementos principales presentes en Markdown, para luego guardarlos como un estilo personalizado.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Gestione los Estilos personalizados (renombrar, reordenar, duplicar y eliminar) desde el [Gestor de Estilos](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
