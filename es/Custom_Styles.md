<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Vea sus documentos *a su* manera.

## Usando estilos personalizados

![][img1]

  [img1]: imágenes/estilos_personalizados.jpg @2x width=544px height=196px class=center

La forma más sencilla de explorar estilos personalizados es a través del
[Galería de estilos personalizados][2]. Desde allí puedes navegar por
estilos disponibles en acción, instálelos con el clic de un
botón, e incluso [envía tus propias creaciones][6] para
inclusión.

Para agregar hojas de estilo personalizadas desde su disco local a Marked,
usa el {% prefspane Style %}. Se agregarán nuevos estilos a
los menús desplegables en la configuración de ventana y en cada ventana,
y será nombrado según el nombre de archivo base del archivo CSS
añadido. Guarde sus archivos CSS personalizados en un lugar seguro en su
conducir. Si se mueven en su disco, serán eliminados de
Marcados hasta que los agregues nuevamente desde la nueva ubicación. es
una buena idea cerrar documentos abiertos y eliminar el estilo
desde Configuración antes de eliminar o cambiar el nombre de un archivo CSS utilizado por
Marcado. No romperá nada si no lo haces, pero salva
cierta confusión.

Agregue estilos personalizados usando el Administrador de estilos con el botón Agregar o arrastrando uno o más archivos CSS a la Configuración
panel.

## Administrar estilos con el Administrador de estilos

Al iniciar el Administrador de estilos, tendrás un lugar único para seleccionar cada elemento integrado.
y tema personalizado. Haga clic en el botón **Administrar estilos...** en {% prefspane Style %}
panel,
o simplemente suelte archivos CSS en la ventana de preferencias. Marked los importará,
Abra el Administrador de estilos y seleccione la fila recién agregada. Arrastrando CSS
Los archivos directamente en la ventana del Administrador de estilos también funcionan; cuando varios archivos
Si los arrastra, verá la actualización superpuesta a "Agregar N estilos personalizados" para que quede claro
estás importando un lote.

![][img-estilo-manager]

Dentro del Administrador de estilos encontrarás una tabla ordenable que combina elementos integrados y
estilos personalizados. Cada fila ofrece:

- Una casilla de verificación **Habilitada** que agrega/elimina inmediatamente el estilo del Estilo
  menú, ventana emergente Estilo predeterminado y métodos abreviados de teclado. Deshabilitar el actualmente
  El estilo activo cambia automáticamente a la siguiente entrada disponible.
- Una columna **Nombre** que puedes editar en línea; Los cambios persisten y se propagan a todos.
  menú. Haga clic en el nombre del estilo para editarlo en su lugar.
- Una columna **Fuente** que indica Integrado, Personalizado o Duplicado.
- Una pila de **Acciones** con botones para **Editar** (abre el archivo CSS en tu
  editor), **Duplicar** (crea una copia y un nuevo archivo CSS en el disco), **Revelar**
  (muestra el archivo en Finder) y **Eliminar** (con opciones para eliminar la referencia o
  mover el archivo CSS a la Papelera).

Las filas se reordenan mediante arrastrar y soltar, y el orden controla el menú Estilo, así como
las asignaciones de accesos directos `⌘/#`, para que puedas literalmente arrastrar estilos a las ranuras
quieres. También puedes arrastrar archivos CSS externos a posiciones específicas; la gota
El indicador determina dónde se inserta el nuevo estilo.

### Vista previa en vivo

El panel derecho contiene una vista previa que representa el estilo seleccionado.
dentro de un documento HTML completo con un conjunto completo de encabezados, listas, tablas, bloques de código, etc.
La vista previa utiliza el CSS real en el disco, por lo que las ediciones que realice en su editor externo se actualizan instantáneamente. Una casilla de verificación alterna la vista previa del modo oscuro.

Puede encontrar estilos adicionales para usar (o como ejemplos para
creando el tuyo propio) [en GitHub][1] (consulta los [ejemplos][2] para
un vistazo rápido a lo que hay allí). Consulte [Creación de CSS personalizado][3]
para detalles y consejos.

## CSS adicional

Debajo de {% prefspane Style %}, encontrarás una opción
titulado CSS adicional con un botón denominado "Editar CSS".
Al hacer clic en este botón se abre una ventana donde puede agregar
reglas CSS universales que se aplicarán a todos los estilos. Nota
que la especificidad de las reglas puede ser importante cuando
anulando algunos de los estilos predeterminados de Marked. el cuerpo principal
del documento está envuelto en un div con el ID "#wrapper".
Prefijar un selector con esto puede facilitar
anula, por ejemplo:

    #wrapper img { ancho: 100%; altura: automático; }

CSS en este campo se aplicará a todos los documentos, no
importa qué estilo esté usando. Si desea aplicar estilos personalizados
CSS basado en coincidencias condicionales, use Establecer estilo, Insertar
Archivo CSS o Insertar acciones CSS en {% prefspane Processor %}
Reglas personalizadas.

## Imprimir y exportar PDF

Marked inyecta un bloque `@media print` (`mkprintstyles`) incorporado en cada
vista previa. Establece valores predeterminados como una base de **10 puntos** en `html`, `body` y
`#wrapper` (o el tamaño de **Tamaño de fuente personalizado para exportar/imprimir** en
{% prefspane Export %} cuando esa opción está habilitada), y normaliza el párrafo
envía un mensaje de texto con `p { font-size: 1em; }` y `li p { font-size: 1em; }` entonces
reglas de solo pantalla como `p { font-size: 1.1429em; }` no inflar el texto del cuerpo
en archivos PDF y en formato impreso.

La exportación de PDF utiliza medios impresos en el WebView oculto utilizado para la generación, por lo que
`@media print { ... }` las reglas de tu hoja de estilo se aplican de la misma manera que para
impresión.

Para establecer tamaños que difieren de los valores predeterminados de impresión de Marked, agregue reglas explícitas
dentro de `@media print` en su CSS personalizado (o en CSS adicional). uso
`!important` cuando necesita anular los estilos de impresión inyectados de Marked --- para
ejemplo:

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
```

Las reglas sin `!important` pueden perder contra reglas posteriores en `mkprintstyles` o
otros selectores no calificados en su hoja que aún se aplican en forma impresa. poniendo
Los ajustes de solo impresión en `@media print` (en lugar de solo en las reglas de pantalla) mantienen
Es más fácil razonar sobre el comportamiento de vista previa y exportación.

## Observando los cambios de CSS

Puede marcar una casilla en la sección Estilos personalizados del {% prefspane Style %}
tener marcado ver el archivo CSS activo
además del archivo Markdown que estás editando. cuando
Si se detectan cambios en cualquiera de los archivos, la vista previa
actualizar. Esto es útil para editar estilos personalizados sin
Se actualiza constantemente y también se puede utilizar para aplicaciones web sencillas.
tareas de desarrollo.

Esto también es útil para algunos trabajos básicos de diseño web y CSS.
experimentación (como crear estilos personalizados). Cargar un
Archivo Markdown que contiene todo el marcado al que desea aplicar estilo
para crear un estilo personalizado y ver la vista previa en vivo
cambia a medida que lo editas.

## Escribir CSS personalizado

Si estás familiarizado con CSS, puedes crear tu propio estilo.
Hojas para uso en Marcado. Consulte [Escribir CSS personalizado][3] para
detalles. Cada vez que crees algo nuevo, considera
[enviándolo][6] a la [galería][2] para compartirlo con otros
usuarios. Asegúrese de cubrir los conceptos básicos enumerados en la guía y
incluya el comentario de metadatos en la parte superior.

### Estilos personalizados automáticos con StyleStealer

Incluso puedes generar automáticamente un estilo basado en un
sitio web existente utilizando [Style Stealer][4]. Esto le permite cargar una página web y tomar los estilos calculados para todos los elementos principales que se encuentran en Markdown, luego guardarlos en un estilo personalizado.

![Ladrón de estilos][robador de estilos]

  [robo de estilos]: imágenes/ladrón de estilos-800.jpg @2x width=800


Administre estilos personalizados (cambiar nombre, reordenar, duplicar y eliminar) desde el [Administrador de estilos](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center