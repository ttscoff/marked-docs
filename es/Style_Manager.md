<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Style Manager proporciona una interfaz centralizada para gestionar todos sus
Estilos integrados y personalizados. Le da control total sobre qué
Los estilos aparecen en los menús, su orden, atajos de teclado y más.

## Abrir el Administrador de estilos [opening-the-style-manager]

Para abrir el Administrador de estilos, haga clic en el botón **Administrar estilos...** en el {% prefspane Style %}
panel, o use {% appmenu Style, Manage Styles (~@$m) %}. También puedes arrastrar archivos CSS directamente a la ventana de preferencias --- Marcado
los importará, abrirá el Administrador de estilos y seleccionará la fila recién agregada para
usted.

![Administrador de estilos][img-style-manager]

  [img-style-manager]: imágenes/capturas de pantalla/style-manager.jpg @2x width=1009px height=517px class=center

## La tabla de estilos [the-style-table]

El Administrador de estilos muestra todos sus estilos en una tabla ordenable que combina
estilos integrados y personalizados sin problemas. Cada fila de la tabla contiene varios
columnas:

### Casilla de verificación habilitada [enabled-checkbox]

La casilla de verificación **Activada** agrega o elimina inmediatamente el estilo del Estilo
menú, ventana emergente Estilo predeterminado y métodos abreviados de teclado. Cuando desactivas un estilo,
está oculto en los menús, pero permanece en el Administrador de estilos para volver a habilitarlo fácilmente.

Si desactiva el estilo actualmente activo, Marcado cambia automáticamente al estilo
siguiente estilo habilitado disponible.

### Columna de nombre [name-column]

La columna **Nombre** muestra el nombre para mostrar del estilo. Puedes editar este nombre
en línea haciendo clic directamente en él; los cambios persisten y se propagan a cada menú
donde aparece el estilo. Esto es especialmente útil para estilos personalizados en los que
Es posible que desee un nombre más descriptivo que el nombre del archivo.

Los estilos integrados tienen nombres bloqueados que no se pueden editar. Para personalizar un
nombre del estilo incorporado, duplíquelo primero para crear una copia editable.

### Columna de origen [source-column]

La columna **Fuente** indica de dónde proviene el estilo:

- **Integrado**: estilos que vienen con Marked y se almacenan en la aplicación
  haz
- **Personalizado**: estilos que has agregado desde archivos CSS en tu disco
- **Duplicado**: Estilos creados duplicando otro Estilo (ya sea integrado
  o personalizado)

### Columna de acciones [actions-column]

Cada fila incluye una pila de **Acciones** con botones para administrar ese estilo:

**Editar**: abre el archivo CSS en su editor predeterminado. Los estilos integrados no se pueden
editados directamente: primero deberá duplicarlos para crear una copia editable.

**Duplicar**: Crea una copia del estilo y un nuevo archivo CSS en el disco. el
El duplicado aparece inmediatamente debajo del estilo original en la tabla. esto es
la forma recomendada de personalizar los estilos integrados.

**Revelar**: muestra el archivo CSS en Finder, lo que facilita su localización en
tu impulso. Este botón solo está disponible para estilos personalizados con una ruta de archivo.

**Eliminar**: Elimina el estilo de Marcado. Para estilos personalizados, se le dará
la opción de eliminar solo la referencia (manteniendo el archivo CSS) o mover
el archivo CSS a la Papelera. Los estilos integrados no se pueden eliminar, pero se pueden
discapacitado.

**Restaurar**: para estilos integrados, este botón restaura el estilo a su
estado predeterminado si ha sido modificado. Este botón sólo es visible para
estilos incorporados.

## Reordenar estilos [reordering-styles]

Las filas se pueden reordenar arrastrando y soltando. Simplemente arrastre una fila de estilo a una nueva
posición en la tabla. El orden que establezca aquí conduce:

- El orden del menú Estilo en los menús de Marked
- Asignaciones de atajos de teclado (`⌘1`–`⌘9` para los primeros nueve estilos habilitados,
  `⌥⌘1`–`⌥⌘0` para los diez siguientes, y así sucesivamente)

Arrastre los estilos a las ranuras de atajos de teclado que desee
ocupar.

## Agregar estilos [adding-styles]

Hay varias formas de agregar nuevos estilos personalizados al Administrador de estilos:

### Agregar botón [add-button]

Haga clic en el botón **Agregar nuevo estilo** para abrir un selector de archivos.
donde puede seleccionar uno o más archivos CSS para importar. Los archivos seleccionados serán
agregado al Administrador de estilos y habilitado de forma predeterminada.

### Arrastrar y soltar [drag-and-drop]

Puede arrastrar archivos CSS directamente a la ventana del Administrador de estilos. cuando arrastras
archivos sobre la ventana, aparecerá una superposición que muestra "Agregar un estilo personalizado" (o
"Agregar N estilos personalizados" para varios archivos). Suelta los archivos para importarlos.

También puedes arrastrar archivos CSS a posiciones específicas en la tabla: la opción soltar
El indicador muestra dónde se insertará el nuevo estilo, permitiéndole controlar
tanto importar como posicionar en una sola acción.

Arrastrar archivos CSS al panel de preferencias {% prefspane Style %} también
importarlos y abrir el Administrador de estilos automáticamente.

## Vista previa en vivo [live-preview]

El panel derecho del Administrador de estilos muestra una vista previa en vivo del estilo seleccionado.
estilo. La vista previa muestra un documento de muestra completo con títulos,
listas, tablas, bloques de código, citas en bloque y otros elementos comunes de Markdown,
todo diseñado con el CSS real del estilo seleccionado.

La vista previa utiliza el archivo CSS directamente desde el disco, por lo que cualquier edición que realice en su
El editor externo se actualizará instantáneamente en la vista previa. Esto hace que sea fácil
vea sus cambios en tiempo real a medida que desarrolla estilos personalizados.

### Vista previa del modo oscuro [dark-mode-preview]

Una casilla de verificación encima de la vista previa le permite alternar entre el modo claro y oscuro
vistas previas. Esto es útil para probar cómo se ven los estilos en ambos modos de apariencia,
especialmente si está creando estilos que se adaptan a la apariencia del sistema.

## Atajos de teclado [keyboard-shortcuts]

El Administrador de estilos muestra una leyenda debajo de la tabla que muestra cómo funciona el teclado.
Se asignan atajos. Los primeros nueve estilos habilitados reciben {% kbd cmd 1 %} hasta
{% kbd cmd 9 %} ({% kbd cmd 0 %} está reservado), los diez siguientes reciben {% kbd opt cmd 1 %} hasta {% kbd opt cmd 0 %}, y así sucesivamente. Puede ver los atajos de teclado asignados en el menú emergente Estilo en cualquier Vista previa.

## Filtrado de estilos deshabilitados [filtering-disabled-styles]

Una casilla de verificación en la parte inferior de la ventana le permite mostrar u ocultar personas deshabilitadas.
estilos. Cuando no está marcada, sólo se muestran los estilos habilitados, lo que facilita la
Concéntrate y reordena tus estilos activos. Cuando está marcado, todos los estilos (habilitados y deshabilitados)
se muestran, lo que le permite administrar su colección de estilos completa.

## Restaurar estilos integrados [restoring-builtin-styles]

El botón **Restaurar todos los estilos integrados** en la parte inferior de la ventana
restaura todos los estilos integrados a su estado predeterminado. Esto es útil si tienes
estilos integrados deshabilitados y desea volver a habilitarlos, o si desea restablecerlos
cualquier modificación realizada en los estilos integrados.

## Consejos [tips]

- **Organizar por frecuencia**: arrastre los estilos más utilizados hacia la parte superior para mostrar
  ellos los atajos de teclado más fáciles ({% kbd cmd 1 %}, {% kbd cmd 2 %}, etc.)

- **Desactivar en lugar de eliminar**: en lugar de eliminar estilos que no estás usando,
  desactivarlos. Se mantendrán fuera de tu camino pero permanecerán disponibles si lo necesitas.
  ellos más tarde.

- **Utilice duplicado para experimentar**: duplique un estilo antes de convertirlo en mayor.
  cambios para que siempre puedas volver al original.

- **Vista previa durante la edición**: mantenga abierto el Administrador de estilos mientras edita CSS
  archivos para ver sus cambios actualizados en tiempo real en el panel de vista previa.

- **Importación por lotes**: puede seleccionar varios archivos CSS a la vez cuando utiliza el
  Botón Agregar o arrastre varios archivos para importarlos todos en una sola acción.