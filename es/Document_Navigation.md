<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Esta página describe cómo moverse por vistas previas largas: la [Tabla de contenido](#tabla de contenido), [búsqueda rápida](#búsqueda rápida), [marcadores](#marcadores-y-mini-mapa) y el [Minimapa](#minimapa). Para conocer los atajos de desplazamiento que se aplican en todas partes (como {% kbd j %}/{% kbd k %}), consulte [Navegación con teclado](Interface_Features.html#keyboardnavigation) en [Funciones de interfaz](Interface_Features.html).

## Tabla de contenidos

![][8]

   [8]: imágenes/tableofcontentsbutton.jpg @2x width=740px height=238px class=center

Si su documento tiene encabezados, aparece un botón de lista en la barra de herramientas. Haga clic en él para expandir la tabla de contenido; haga clic en un título para saltar a esa sección de la vista previa. Utilice {% kbd j %}/{% kbd k %} (abajo/arriba) para moverse por la lista y {% kbd Enter %} o {% kbd o %} para saltar al encabezado resaltado.

**Barra de filtro:** Con la tabla de contenido abierta, presione {% kbd Space %} (barra espaciadora) para abrir el campo de escritura anticipada. Escriba cualquier parte del nombre de un título (Marked usa coincidencia de estilo TextMate; por ejemplo, puede escribir la primera letra de cada palabra) y presione Tab ({% kbd ⇥ %}) o la flecha hacia abajo ({% kbd ↓ %}) para moverse por la lista filtrada.

Al presionar {% kbd cmd T %} también se abre (o cierra) la tabla de contenido.

Si ["Titulares Contraer Secciones"](Interface_Features.html#collapsibleheadlines) está habilitado en {% prefspane General %}, mantener presionada la tecla Comando mientras hace clic en un elemento en la Tabla de Contenido contraerá o expandirá esa sección, revelando las secciones principales según sea necesario.

Cuando está en modo de pantalla completa, la tabla de contenido aparece como una barra lateral fija en lugar de un menú emergente. Para usar ese diseño en una vista previa de ventana normal, use el interruptor de pantalla completa en la parte inferior derecha del panel TOC.

![Alternar pantalla completa][12]

   [12]: imágenes/tableofcontentsfullscreentoggle.jpg @2x width=740px height=238px class=center


Para obtener una lista resumida de teclas, consulte [Atajos de teclado](Keyboard_Shortcuts.html#TableofContentsNavigation).

Consulte también el [vídeo de navegación de documentos en YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Modo de pantalla completa para la tabla de contenidos

Cuando una ventana de vista previa marcada está en pantalla completa, la tabla de contenido puede permanecer fija a la izquierda para una navegación constante. Todavía alterna con {% kbd cmd T %}; Al hacer clic fuera del TOC a menudo no se descartará mientras se encuentre en este diseño.

En una ventana normal, haga clic en el icono en la parte inferior del panel TOC para acoplarlo como barra lateral; haga clic en el icono en la parte superior de la barra lateral para volver al modo emergente.

### Personalizando dónde aparece el TOC

La tabla de contenido se puede insertar en el documento exportado usando la [sintaxis especial](Special_Syntax.html#tocplacement) `<!--TOC-->`.

Agregue `max#` (por ejemplo `<!--TOC max2-->`) para limitar la cantidad de niveles de encabezado que aparecen.

## Búsqueda rápida

**Navegación rápida** combina la tabla de contenido con el filtro enfocado para que puedas saltar con un mínimo de escritura:

- Presione {% kbd f %} en la vista previa para abrir el TOC con el **campo de filtro enfocado** (la misma idea que abrir el TOC y luego presionar {% kbd Space %}, sin el paso adicional).
- Escriba parte de cualquier título de título; la lista se filtra por coincidencias.
- Si solo queda un título, al presionar Retorno ({% kbd ↩ %}) se salta directamente a él.
- Si quedan varios titulares, presione Tab ({% kbd ⇥ %}) para salir del campo de filtro, muévase con {% kbd j %}/{% kbd k %} o las teclas de flecha, luego presione {% kbd o %} o Retorno ({% kbd ↩ %}) para ir al titular y cerrar el TOC.
- Tabulador vuelve a devolver el foco al campo de búsqueda.

> **Recordatorio de acceso directo:** Al abrir el TOC y presionar {% kbd Space %} se abre la barra de filtro, lo cual resulta útil siempre que el TOC ya esté visible.

(Los documentos anteriores se referían a esto como "Fast Switcher"; es la misma característica).

## Marcadores y minimapa {#marcadores-y-mini-mapa}

Utilice el menú de vista previa {% appmenu Gear %} y {% kbd Tab %} ({% kbd ⇥ %}) enfocando el documento junto a [búsqueda](Interface_Features.html#search) para colocar y volver a visitar marcadores mientras hojea.

### Configuración de marcadores

Establezca marcadores en la posición de desplazamiento usando {% kbd shift 1 %}--{% kbd shift 9 %} y retroceda usando {% kbd 1 %}--{% kbd 9 %} solo. Utilice {% kbd n %} y {% kbd p %} para siguiente/anterior en **orden de documentos**; {% kbd shift n %} y {% kbd shift p %} para siguiente/anterior en orden **numérico**.

Al cambiar el estilo o el tamaño de la página se puede mover donde aparece un marcador. Los marcadores están pensados ​​como ayudas de revisión temporales: no persisten entre sesiones de documentos, pero sí sobreviven a las actualizaciones y ediciones de la vista previa.

**Marcadores de títulos:** Mantenga presionada la opción y presione {% kbd opt 1 %}--{% kbd opt 9 %} para marcar el título más cercano a la parte superior de la ventana gráfica (o el último título antes de la parte superior).

**Siguiente espacio libre:** {% kbd cmd D %} (o acento grave {% kbd \`\` %}, para usuarios de vim) agrega un marcador en el siguiente espacio numerado disponible.

Presione {% kbd 0 %} para expandir la franja de marcadores (títulos de titulares cuando estén disponibles). Cuando el [Minimapa](#minimapa) está habilitado, {% kbd 0 %} lo muestra al mismo tiempo. Presione Escape o {% kbd 0 %} nuevamente para colapsar.

Presione {% kbd x %} dos veces ({% kbd xx %}) para borrar todos los marcadores.

Hay [más atajos de vista previa](Keyboard_Shortcuts.html); presione {% kbd h %} en la vista previa para obtener una lista de avisos, o {% kbd opt cmd K %} para obtener la referencia completa.

### Minimapa {#minimapa}

Si el Mini mapa está habilitado en la configuración {% prefspane Preview %}, {% kbd 0 %} abre una miniatura escalada de todo el documento a lo largo de la franja de marcadores. Haga clic en cualquier parte del mapa para ver la vista previa completa allí. Los marcadores guardados aparecen como líneas horizontales con números (y títulos cuando sea relevante).

Mantenga presionado **Comando** y muévase sobre el minimapa para obtener una lupa ampliada; mantenga presionada **Opción** y arrastre para desplazarse como si arrastrara la barra de desplazamiento.

El mapa se regenera cuando cambia el tamaño o el diseño de la ventana. En documentos muy largos, presionar {% kbd 0 %} una vez puede tardar un momento; Marked evita crear el Mini Mapa automáticamente en la carga inicial hasta que lo solicites.

Presione {% kbd 0 %} o Escape para cerrar el Mini Mapa.

**Nota de rendimiento:** La generación del mapa puede pausar brevemente la vista previa en documentos grandes; esto sólo se ejecuta cuando el mapa está visible o después de cambiar su tamaño.

### Descripción general de Zoom (relacionada)

Para obtener una descripción general a escala de texto sin el minimapa, consulte [Descripción general del zoom](Zoom_Overview.html) ({% kbd z %}).