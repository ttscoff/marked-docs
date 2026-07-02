<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Lleve un registro mientras escribe.

## Recuento de palabras y estadísticas de documentos

![][1]

   [1]: imágenes/WordCount.jpg @2x ancho=840px alto=61px clase=centro

El recuento de palabras se encuentra en la barra de estado inferior y se puede habilitar y deshabilitar desde {% prefspane General %} en la barra de estado. Puede ver más estadísticas en la ventana de vista previa o fuente desde el menú de ajustes, haciendo clic en el recuento de palabras o escribiendo Opción-Comando-S ({% kbd opt cmd S %}). Mantenga presionada la tecla Opción ({% kbd opt  %}) mientras hace clic para mostrar Estadísticas de legibilidad y mantenga presionada Opción-Comando ({% kbd opt cmd %}) para abrir el panel Estadísticas avanzadas.

Si se selecciona texto, la pantalla del recuento de palabras y la ventana emergente de párrafo/frases/caracteres se actualizarán con información solo para la selección.

## Recuento de palabras para la selección

![Ventana emergente de recuento de palabras al seleccionar texto][2]

   [2]: imágenes/wordcountforselection.jpg @2x ancho=749px alto=144px clase=centro

Cuando selecciona texto en la vista previa, el recuento de palabras en la parte inferior de la ventana mostrará estadísticas solo para el texto seleccionado.

Si "Mostrar recuento de palabras para la selección" está habilitado en {% prefspane Preview %}, aparecerá una pequeña ventana emergente junto al cursor para mostrar el recuento de palabras/líneas/caracteres del texto seleccionado. Esto se descarta simplemente alejando el mouse de la ventana emergente.

La función de zoom es útil para seleccionar y obtener recuentos rápidamente para fragmentos de texto más grandes. Escriba {% kbd z %} para alejar y hacer su selección.

## Estadísticas de legibilidad

![Barra de estadísticas de legibilidad][3]

   [3]: imágenes/capturas de pantalla/mainwindow-feature-stats-lower-crop.jpg @2x ancho=1089px alto=111px clase=centro

Estadísticas adicionales de Flesch/Kincaid y el Fog Index están disponibles en {% kbd opt shift cmd S %}.

### Información de legibilidad

**Facilidad de lectura de Flesch:** las puntuaciones más altas indican material que es más fácil de leer; los números más bajos marcan pasajes que son más difíciles de leer.

**90,0--100,0**: estudiante promedio de 11 años
**60.0--70.0**: estudiantes de 13 a 15 años
**0,0--30,0**: graduados universitarios

**Nivel de grado Flesch-Kincaid:** la cantidad de años de educación que generalmente se requieren para comprender este texto.

**Índice de niebla Gunning:** mide la legibilidad de la escritura en inglés. El índice estima los años de educación formal necesarios para comprender el texto en una primera lectura. Un índice de niebla de 12 requiere el nivel de lectura de un estudiante de último año de secundaria de Estados Unidos (alrededor de 18 años).

## Estadísticas avanzadas

![Ventana emergente de Estadísticas avanzadas][adv]

[adv]: images/screenshots/mainwindow-feature-stats-info-crop.jpg @2x width=800px height=800px class=center

Al seleccionar Estadísticas avanzadas en el menú de ajustes ---- o presionar {% kbd cmd I %} --- se desplegará un panel que contiene estadísticas de documentos más avanzadas, incluida la longitud promedio de palabras y oraciones y la complejidad promedio de las palabras.

### Estadísticas avanzadas flotantes

![Ventana de información flotante][flotante]

[floating]: images/floatinginfo.jpg @2x width=999px height=522px class=center

Al presionar {% kbd shift cmd I %} se abrirá un panel flotante que contiene todas las estadísticas detalladas e información de legibilidad. Este panel puede permanecer en primer plano cuando cambia a su editor, para que pueda ver sus estadísticas actualizadas cada vez que guarda, ya sea que la vista previa sea visible o no. Al presionar el ícono `<`, la Vista previa marcada asociada volverá al primer plano. Si mantiene presionada la opción y hace clic en el mismo botón, se abrirá el archivo Markdown en su editor de texto predeterminado (configurado en {% prefspane Apps %}).

### Objetivos de palabras

Si tiene un objetivo específico para el recuento de palabras mientras escribe, puede agregar una clave de metadatos "destino:" en la parte superior de su documento y Marked realizará un seguimiento de su progreso, mostrando un indicador de finalización en el panel Estadísticas detalladas ({% kbd cmd I %}) y en Estadísticas flotantes ({% kbd shift cmd I %}).

![][recuento de palabras objetivo]

[targetwordcount]: images/wordtargets.jpg @2x width=740px height=191px class=center


## Visualizar la repetición de palabras

Al seleccionar Visualizar repetición de palabras en el menú de ajustes (o presionar {% kbd ctrl cmd W %}) se cambiará a una vista especial que elimina elementos que no son de texto y resalta las palabras que se repiten en su documento. Las palabras repetidas se resaltan en rosa claro y, al pasar el cursor sobre una palabra resaltada, se iluminarán las palabras coincidentes en todo el documento. Al hacer clic en una palabra resaltada, se oscurecerá el fondo y se "pegará" el resaltado para su posterior revisión.

![Repetición de palabras][4]

[4]: images/screenshots/mainwindow-word-repetition.jpg @2x width=1369px height=1084px

También puede utilizar la función "zoom" (escriba "z") en este modo, lo que le permite resaltar una palabra repetida y luego escanear rápidamente todo el documento para ver dónde se concentran las repeticiones.

Las palabras se comparan por su "raíz", lo que significa que "parte", "en parte" y "partes" se considerarán palabras repetidas. Esto tiene en cuenta las sílabas y la conjugación al comprobar la densidad de repetición.

**Alcance**

El alcance de la verificación de repetición se puede cambiar en la barra de herramientas inferior del documento y se puede establecer en Documento o Párrafo. El modo de documento es el predeterminado; Al seleccionar Párrafo solo se cuentan las repeticiones dentro de cada bloque de texto. Las repeticiones seguirán resaltadas en todo el documento, pero solo se contarán si una palabra aparece más de una vez dentro de un solo párrafo.

**Ignorando palabras**

Puede excluir temporalmente una palabra y todas sus conjugaciones y pluralizaciones presionando Opción y haciendo clic en la palabra resaltada. Las palabras ignoradas temporalmente aparecerán en la esquina inferior derecha de la vista previa. Al hacer clic en una palabra en la lista de palabras ignoradas, se restaurará a la visualización.

Para ignorar palabras permanentemente, puede editar una lista en {% prefspane Proofing %} en la pestaña Ignorar repeticiones. Las palabras (o raíces de palabras) agregadas una por línea en esta lista siempre se ignorarán. Para agregar automáticamente una palabra a esta lista, haga clic en Opción-Mayús y haga clic en ella en la visualización de repetición de palabras.

**Salir del modo de repetición de palabras**

Puede cerrar la vista de repetición de palabras usando el ícono Cerrar al lado del selector de alcance en la barra de herramientas inferior o presionando Escape.