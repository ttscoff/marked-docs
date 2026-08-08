<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La flexibilidad es clave.

## Menú de engranajes [gear-menu]

![][4]

   [4]: imágenes/gearmenu.jpg @2x width=740px height=235px class=center

El menú Gear proporciona la mayoría de las funciones que se encuentran en la barra de menú, además de algunas funciones específicas de vista previa. Simplemente haga clic en el engranaje en la parte inferior derecha de la ventana para acceder a estas funciones.

## Mantente en la cima [keep-on-top]

![][5]

   [5]: imágenes/KeepOnTopPin.jpg @2x width=740px height=345px class=center

El ícono de candado en la parte inferior izquierda traerá la ventana de Vista previa al frente y la mantendrá allí (flotando) cuando cambie a otras aplicaciones. Puede establecer una transparencia en la ventana en {% prefspane General %} que permitirá que la ventana se desvanezca cuando use otras aplicaciones.

Esta función también se puede alternar con {% kbd shift-opt-cmd-f %}.

## Valores predeterminados a nivel de ventana [window-level-defaults]

En {% prefspane General %} puede usar "Mantener nuevas ventanas en la parte superior" para configurar las nuevas ventanas para que siempre permanezcan encima de otras ventanas y/o configurar las ventanas para que suban a la parte superior cuando se actualice su documento asociado. Windows configurado para aumentar con la actualización no "robará el foco" de su editor, solo aumentará para ser visible sin activarse.

## Ver código fuente [view-source]

![][6]

   [6]: imágenes/view_source.jpg @2x width=740px height=345px class=center

Puede cambiar entre vista previa y vista de código fuente con el botón en la esquina superior derecha. Esta vista también se puede alternar con U.

## Buscar [search]

![][7]

   [7]: imágenes/SearchBarFull.jpg @2x width=818px height=195px class=center

Se puede acceder a la barra de búsqueda con {% kbd cmd F %} y le permite buscar en la vista previa una palabra o frase. Una vez que realice la búsqueda, puede usar {% kbd cmd G %} y {% kbd shift cmd G %} para navegar hacia adelante y hacia atrás a través de resultados adicionales.

Las casillas de verificación en el lado derecho de la barra de búsqueda le permiten limitar la búsqueda por distinción entre mayúsculas y minúsculas, solo palabras completas y expresiones regulares. Además de la búsqueda con expresiones regulares, las búsquedas con comodines (*?) siempre funcionan, incluso cuando la opción de expresiones regulares está desactivada.

También puede rodear un término o frase de búsqueda con barras para interpretarlo automáticamente como una expresión regular (por ejemplo, '/term.+?\b/').


Utilice la función de búsqueda en combinación con los marcadores para guardar ubicaciones a medida que las encuentre. Presione Tab ({% kbd ⇥ %}) para enfocar el documento, luego escriba Shift-[1-9] para establecer un marcador en ese número. Puede volver al marcador simplemente escribiendo el número (sin la tecla Mayús) o usando n/p para navegar a través de ellos en el orden del documento. N/P navegará en orden numérico. Para los marcadores, la tabla de contenido, el minimapa y la búsqueda rápida de encabezados, consulte [Navegación del documento](Document_Navigation.html). Consulte la sección [Vista previa de navegación](Keyboard_Shortcuts.html#previewnavigation) para obtener más opciones o escriba "?" en cualquier momento en la Vista previa.

> **Nota:** La búsqueda no puede ajustarse entre elementos, lo que significa que una cadena de búsqueda no puede continuar entre un párrafo y un título, entre elementos de una lista, etc.

Puede alternar las casillas de verificación "Palabras completas", "Distingue entre mayúsculas y minúsculas" y "Regex" usando {% kbd ctrl shift 1 %}, {% kbd 2 %} y {% kbd 3 %}, respectivamente.

### Búsqueda avanzada ### [advanced-search]

Puede utilizar comodines en una búsqueda que no sea de expresiones regulares. `*` coincidirá con cualquier serie de caracteres que no sean espacios y `?` coincidirá con cualquier carácter individual.

Iniciar una búsqueda con `*` la convertirá en una búsqueda de selector jQuery. Puede utilizar cualquier selector de jQuery y todos los elementos coincidentes se resaltarán y serán navegables con {% kbd cmd G %} y {% kbd shift cmd G %}. Para limitar el alcance de una búsqueda de texto a un determinado tipo de elemento, agregue los términos de búsqueda entre comillas dobles después de la definición del selector:

    *h2 "Alicia"

Esto es el equivalente a `*h2:contains(Alice)`

## Navegación de documentos (TOC, marcadores, minimapa) [document-navigation-toc-bookmarks-mini-map]

La página [Navegación del documento](Document_Navigation.html) cubre la tabla de contenido (incluida la apertura del filtro con {% kbd Space %}), la búsqueda rápida con {% kbd f %}, los marcadores y el minimapa.

## Navegación por teclado [keyboardnavigation]

Se puede navegar rápidamente por la ventana de vista previa mediante atajos de teclado. Utilice {% kbd j %} y {% kbd k %} para moverse hacia arriba y hacia abajo, y mantenga presionada la tecla Mayús ({% kbd J %}/{% kbd K %}) para moverse más rápido. {% kbd t %} y {% kbd b %} se moverán a la parte superior e inferior del documento (al igual que {% kbd gg %} y {% kbd G %}, para los fanáticos de Vim). {% kbd u %} y {% kbd d %} se moverán 1/2 página hacia arriba y hacia abajo.

### Salto de encabezado [header-jumping]

Al presionar las teclas coma ({% kbd , %}) y punto ({% kbd . %}), se saltará hacia adelante y hacia atrás a través de los encabezados del documento. Al mantener presionada la tecla Mayús ({% kbd shift  %}), se saltará solo entre los encabezados de nivel 1 y 2.


## Pantalla completa [full-screen]

El modo de pantalla completa se puede alternar desde el menú Vista previa o escribiendo {% kbd ctrl cmd F %}.

## Hacer clic en enlaces externos [clicking-external-links]

![][10]

[10]: images/linkpopover.png @2x width=706px height=213px class=center

Al hacer clic en un enlace externo en la vista previa de su documento, se abrirá en su navegador predeterminado. Si hace clic y mantiene presionado, cuando suelte Marcado le dará tres opciones: puede copiar la URL del enlace a su portapapeles, validar el enlace o abrir el enlace en su navegador predeterminado. Simplemente haga clic en cualquier lugar de su vista previa para cerrar la ventana. Esta función se puede desactivar en {% prefspane Preview %} ("Habilitar ventanas emergentes de enlaces").

Vea un [video de descripción general en YouTube](https://www.youtube.com/watch?v=nrt7YZPrnv0&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=1).

## Titulares plegables ## [collapsibleheadlines]

Cuando "Títulos contraer secciones" está habilitado en {% prefspane Preview %}, al hacer clic en los titulares se contraerá la sección entre ese título y el siguiente título en el mismo nivel. Las subsecciones dentro de esa sección están ocultas. Opcionalmente, puedes limitar este comportamiento a {% kbd cmd %}-hacer clic.

![][13]

[13]: images/headlines.jpg @2x width=740px height=287px class=center

Si mantiene presionado {% kbd opt  %} al hacer clic (o {% kbd cmd %} y hace clic), se expandirán/contraerán todas las secciones secundarias debajo del encabezado en el que se hizo clic. Si mantiene presionada la tecla {% kbd shift  %} (Mayús) mientras hace clic, se colapsarán todas las demás secciones en el mismo nivel, revelando solo la sección en la que se hizo clic.

Las secciones contraídas están marcadas con un resaltado amarillo a la derecha del título y el cursor indicará lo que sucederá cuando se haga clic en el elemento.

Si se realiza una edición que debe ser visible, o se hace clic en una sección de la tabla de contenido que actualmente se encuentra dentro de una sección contraída, las secciones principales necesarias se expandirán para revelarla.

Puede contraer/expandir todas las secciones de un documento a la vez con "Contraer todas las secciones" ({% kbd opt cmd left  %}) y "Expandir todas las secciones" ({% kbd opt cmd right  %}).

Consulte el [vídeo de navegación de documentos en YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2) para obtener más detalles.

## Indicadores/alternadores de procesador personalizados ## [custom-processor-indicatorstoggles]

![][indicadores]

[indicators]: images/processorindicators.png @2x width=874px height=255px class=center

Cuando el procesador personalizado y/o el preprocesador están habilitados, aparecen luces indicadoras en la barra de herramientas. Estos se pueden usar para ver si el procesador está activado o no para el documento actual (el indicador se resaltará) y al hacer clic en ellos se alternará el uso del preprocesador y el procesador personalizados, respectivamente.

## Desplácese para editar [scrolltoedit]

La función "desplazarse para editar" en Marked realiza un seguimiento de las diferencias entre la última actualización y la última, intentando encontrar el punto donde realizó los cambios más recientes. Marcado siempre realiza un seguimiento de esto y aparece una pequeña línea roja en la vista previa para mostrarle la ubicación del primer cambio detectado. En {% prefspane Preview %}, puede activar "Desplazarse hasta la primera edición" y cuando se actualice una vista previa, la vista se desplazará suavemente hasta esa ubicación.

Con "Desplazarse a la primera edición" desactivado, aún puedes presionar la tecla "e" en cualquier momento en la vista previa para ir al último punto de edición almacenado.

## Desplazamiento automático [autoscroll]

Consulte la página dedicada [Desplazamiento automático](Autoscroll.html). Cuando se utiliza el desplazamiento automático como teleprompter, [la sintaxis especial puede insertar pausas](Special_Syntax.html#pauses).

## Descripción general de zoom [zoom-overview]

Consulte la página [Descripción general del zoom](Zoom_Overview.html) ({% kbd z %} en la vista previa; también funciona en Repetición de palabras con {% kbd ctrl cmd w %}).

## Referencia de rebajas [markdown-reference]

![][11]

   [11]: imágenes/markdown_reference.jpg @2x width=1148px height=267px class=center

Seleccione Referencia de Markdown en el menú {% appmenu Help %} para mostrar una guía que flota sobre las otras ventanas. Esto es útil para aquellos que todavía están aprendiendo la sintaxis de Markdown. Puede abrir este panel a través del teclado usando {% kbd opt cmd M %}.

## Atajos de teclado globales [global-keyboard-shortcuts]

En el {% prefspane General %}, puedes designar un atajo de teclado personalizado para activar Marcado y uno para elevar solo la ventana frontal a la parte superior sin salir del editor.