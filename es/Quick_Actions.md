<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La paleta Acciones rápidas es un iniciador de comandos con capacidad de búsqueda para Marked. Recopila acciones de la barra de menú principal y del **menú de ajustes** de vista previa, además de comandos de teclado de solo vista previa que no aparecen en los menús (como **Desplazamiento automático**). Úselo cuando sepa lo que quiere hacer pero no recuerde qué menú lo contiene.

## Abrir la paleta de acciones rápidas

Abre la paleta con {% kbd shift cmd P %} o desde {% appmenu File, Quick Actions… %}. El panel aparece como una ventana flotante encima de su documento actual.

Presione el mismo atajo nuevamente o presione **Escape** para cerrar la paleta. Si la paleta ya está abierta, al elegir **Acciones rápidas...** en el menú también se cierra.

## Personalizando el acceso directo

El acceso directo predeterminado es {% kbd shift cmd P %}. Para cambiarlo, abra {% prefspane General %} y registre una nueva combinación en **Abrir paleta de acciones** en la sección **Atajos**.

A diferencia de **Activar Marcado** y **Abrir primera ventana**, el acceso directo de Acciones rápidas funciona solo cuando Marcado es la aplicación activa. Actualiza el acceso directo del menú {% appmenu File, Quick Actions… %} para que coincida con su configuración.

## Buscar y filtrar

Escriba en el campo de búsqueda en la parte superior del panel para filtrar comandos en tiempo real. La combinación es confusa e indulgente:

- El orden de las palabras no importa (`view source` coincide con **Alternar vista de código fuente**)
- Las iniciales funcionan bien (`sv` coincide con **Vista fuente**)
- La coincidencia contraída busca comandos sin espacios (`akdoc` coincide con **Preguntar sobre el documento**)

Cada resultado muestra el nombre del comando a la izquierda y su método abreviado de teclado (cuando esté disponible) a la derecha en gris. Algunos comandos también muestran una ruta de navegación (por ejemplo, `Preview › Autoscroll`) cuando la acción proviene de un submenú o del motor de vista previa.

## Lo que aparece en la lista

La paleta incluye:

- **Comandos de menú** desde la barra de menú principal, incluidos menús dinámicos como **Estilo**, **Historial** y pestañas abiertas de **Ventana**
- Comandos del **menú de ajustes** desde la ventana de vista previa
- **Atajos de vista previa** desde el mapa del teclado en la vista previa (los mismos comandos que se muestran en el HUD de ayuda de vista previa), incluida navegación, desplazamiento automático, marcadores, búsqueda y otras acciones solo de vista previa

Cuando el mismo comando aparece en más de un lugar, Marcado muestra la ruta de menú más corta y combina información de accesos directos de duplicados.

## Navegación por teclado

Navegue por la paleta Acciones rápidas completamente desde el teclado:

- ** ↑/↓ Teclas de flecha **: moverse por la lista filtrada
- **Regresar**: ejecuta el comando seleccionado
- **Escape**: cierra la paleta
- **Atajos de teclas ⌘**: cierra la paleta y ejecuta el comando de menú correspondiente (por ejemplo, presiona {% kbd cmd U %} para ejecutar **Alternar vista de código fuente** en lugar de seleccionarlo en la lista)

La escritura simple (sin la tecla Comando) filtra el campo de búsqueda. Los atajos de una sola tecla de solo vista previa, como `s` para el desplazamiento automático, filtran la lista; presione **Regresar** para ejecutar el comando seleccionado.

## Ejecutando comandos

Al seleccionar un comando de menú, se envía de la misma manera que se elige en el menú, incluidos los elementos del menú dinámico y de engranaje.

Al seleccionar un **atajo de vista previa** se ejecuta la acción asociada en la vista previa activa (por ejemplo, alternar el desplazamiento automático o saltar al siguiente encabezado). Estos comandos requieren un documento abierto con vista previa; Si no hay una vista previa disponible, la paleta aún se abre pero las acciones de solo vista previa no tendrán ningún efecto.

Para cambiar archivos relacionados, consulte [Apertura rápida](Quick_Open.html). Para obtener la referencia completa del teclado de vista previa, consulte [Atajos de teclado](Keyboard_Shortcuts.html) o presione {% kbd h %} en la vista previa para mostrar el HUD de ayuda.