<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Ingrese al modo de revisión desde el menú de ajustes. Esta es una característica experimental diseñada principalmente para editores que reciben texto de otros y necesitan hacer comentarios y brindar retroalimentación.

El modo de revisión congela las actualizaciones del documento, evitando que se pierdan anotaciones y notas cuando se actualiza el documento. Aparece un indicador rojo en la barra superior para recordarle que el modo de revisión está activo.

La navegación por teclado, los marcadores y el resaltado de palabras clave funcionan durante la revisión.

## Anotaciones

Mientras está en el modo de revisión, al seleccionar texto en el documento se generará una ventana emergente que le permitirá seleccionar entre varios tipos de resaltado diferentes. Haga clic en el tipo de resaltado que desea agregar al texto, o cancele haciendo clic en el botón "Cancelar" o simplemente haciendo clic fuera de la ventana emergente.

## Notas

![Anotaciones][1]

[1]: images/Annotating.jpg class=center

Una vez que se agrega un resaltado, puede agregarle notas breves haciendo clic en el resaltado. La ventana emergente ahora contendrá un campo de texto donde podrá ingresar cualquier nota que pueda ser pertinente al texto resaltado. Las notas se pueden eliminar y editar haciendo clic en un resaltado que ya tenga una nota.

Las notas **sólo** se exportan cuando se guardan en HTML. Lo más destacado permanece en la mayoría de los formatos de exportación, incluidos RTF y PDF.

## Corrector ortográfico

Mientras está en el modo de revisión, puede acceder al corrector ortográfico de todo el sistema desde el menú de ajustes: {% appmenu {{gear}}, Proofing, Highlight All Spelling Errors %}. Esto será lento en documentos grandes y se mostrará una advertencia que le notificará si el proceso tardará más de 30 segundos aproximadamente. Debido a que el corrector ortográfico no funciona en la vista previa web de Marked, se implementa un "truco" para que esto funcione, y no es rápido.

Una vez que se haya ejecutado la revisión ortográfica, puede abrir el panel Suposiciones ortográficas para activar la revisión gramatical y ver las sugerencias para corregir errores. Marcado como *no se pueden* editar estos en su lugar, debe volver a su documento original para utilizar los resultados.

*Atajos:* {% kbd ctrl opt cmd S %} ejecutará el corrector ortográfico. {% kbd ctrl opt cmd N %} pasará al siguiente error del documento y {% kbd ctrl opt cmd G %} mostrará el panel de conjeturas.