<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Captar palabrería problemática y resaltar frases importantes.

## Resaltado de palabras clave

El resaltado de palabras clave en Marked le permite detectar frases comunes que quizás desee evitar, encontrar términos alternativos o simplemente resaltarlas para fines generales. La lista de palabras clave utilizadas para coincidir con cada categoría se puede editar en {% prefspane Proofing %}.

Habilite el resaltado con {% kbd shift cmd H %}, desde el menú de ajustes ({% appmenu {{gear}}, Highlight Keywords %}), o abra el cajón de palabras clave usando el ícono de resaltado en la parte inferior izquierda (cerca del menú de ajustes). El cajón también se puede abrir con el método abreviado de teclado {% kbd shift cmd K %}. El resaltado se habilita automáticamente cuando se abre el cajón y se puede activar y desactivar con el interruptor en el lado izquierdo del cajón.

## El cajón de palabras clave

![Cajón de palabras clave][kwd]

[kwd]: images/screenshots/mainwindow-feature-keywords-crop.jpg @2x width=1089px height=503px class=center

El cajón de palabras clave que se revela al habilitar el resaltado brinda acceso rápido a las opciones de resaltado, incluida la capacidad de habilitar y deshabilitar tipos de resaltado individuales. La fila vertical de etiquetas de colores en el lado izquierdo se correlaciona con los aspectos destacados del texto. Al hacer clic en una etiqueta, se alternan los aspectos destacados para ese tipo de palabra clave.

A la izquierda de cada etiqueta hay un icono de objetivo. Al hacer clic aquí, se comenzará a desplazar el documento a la siguiente instancia resaltada en el orden del documento. A la derecha de la etiqueta hay un recuento que muestra el número total de aspectos destacados de ese tipo.

Puede navegar rápidamente a través de los aspectos destacados usando el teclado. Al escribir `[` y `]` inicialmente se avanzará y retrocederá a través de todos los aspectos destacados. Si hace clic en un ícono de destino, `[` y `]` cambiarán para navegar solo por ese tipo de resaltado. `{` (Shift-[) y `}` (Shift-]) siempre navegarán por todos los aspectos destacados, independientemente del último objetivo en el que se hizo clic.

Si se hace clic en una palabra o frase resaltada, ese tipo se convertirá en el destino de navegación y al usar `[` o `]` se navegará desde ese punto en el documento.

## Edición de palabras clave

![Configuración de revisión][preferencias de revisión]

  [preferencias de prueba]: imágenes/capturas de pantalla/preferencias-Proofing.jpg @2x width=689px height=1031px class=preferencepane

De forma predeterminada, Marked utiliza la lista de palabras y frases usadas en exceso de la [Campaña en inglés sencillo](http://www.plainenglish.co.uk). Puede agregarlos o reemplazarlos fácilmente editándolos en {% prefspane Proofing %}. Cada campo es texto de formato libre y cada línea se interpreta como una frase de búsqueda. Utilice `*` al principio de una frase o palabra para hacer coincidir cualquier texto anterior y `?` para hacer coincidir un solo carácter como comodín.

Las expresiones regulares se pueden utilizar rodeando la expresión con barras diagonales:

    /\\S*?ly/

Lo anterior coincidirá con cualquier palabra que termine en "ly" para resaltar. La sintaxis de las expresiones regulares en el resaltado de palabras clave de Marked es [igual que JavaScript](http://www.regular-expressions.info/javascript.html).

## Palabras clave temporales

También puede agregar palabras clave temporales en el cajón de palabras clave editando el bloc de notas. Al igual que en los campos {% prefspane Proofing %}, agrega una palabra clave o frase por línea, se permiten expresiones regulares (rodeadas de barras diagonales). Después de editar las palabras clave temporales, asegúrese de hacer clic en el botón "Actualizar" (o presione {% kbd cmd return  %}) para guardar los cambios y verlos resaltados en su documento.

Las expresiones regulares también funcionan en el campo de palabras clave temporales, simplemente rodee el texto con barras diagonales (`/my expression\b/`).

Las palabras clave temporales están pensadas para situaciones en las que la densidad de palabras clave es importante y le permiten ver rápidamente cuántas veces ha utilizado las palabras objetivo, resaltando sus ubicaciones en el documento. En el cajón se muestra de forma destacada un recuento de coincidencias para las palabras clave temporales.

Consulte también el comando ["Visualizar repetición de palabras"][wordrep] para encontrar palabras usadas en exceso en su texto.

[wordrep]: Document_Statistics.html#visualizewordrepetition

## Voz pasiva

Marcado señalará el uso de "voz pasiva" en el texto en inglés. Como [definido por Wikipedia] [pasivo]:

> el sujeto gramatical expresa el tema o paciente del verbo principal, es decir, la persona o cosa que sufre la acción o cambia de estado.

La voz pasiva no es mala, como puedes leer [en publicaciones del lingüista Geoffrey K. Pullum][gkp]. Marked señala pasajes usando voz pasiva, pero la decisión sobre su validez es suya.

[passive]: https://en.wikipedia.org/wiki/Passive_voice
[gkp]: http://languagelog.ldc.upenn.edu/nll/?cat=54

## Palabras duplicadas

Las palabras dobles (por ejemplo, "el el") se resaltan automáticamente en naranja cuando está habilitado el resaltado de palabras clave. Actualmente, esto no es configurable, pero debería resultar útil para la revisión.