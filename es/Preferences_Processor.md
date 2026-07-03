<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opciones en el {% prefspane Processor %}:

![Configuración: Procesador][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane


### Procesar Markdown con

Procesador Markdown predeterminado. El procesador Discount es el preferido por los usuarios de GitHub, MultiMarkdown es ideal para los escritores. Marked compensa algunas diferencias entre la sintaxis. Consulte __Ayuda->Referencia de Markdown__ para obtener información adicional.

Reglas personalizadas
: utilice el botón Reglas personalizadas para abrir el editor de Reglas personalizadas, lo que le permitirá determinar las opciones de procesamiento y las transformaciones de documentos según criterios. Consulte la [documentación del procesador personalizado](Custom_Processor.html) para obtener más detalles.

Los nuevos documentos utilizan personalizados.
: seleccione preprocesador y/o procesador para habilitar automáticamente el procesamiento de reglas en documentos nuevos. Si está utilizando reglas personalizadas, es probable que desee habilitar ambas.

###HTML

Generar identificaciones en titulares
: genera ID de encabezado según el contenido de la etiqueta h1-h6.

Utilice ID de notas al pie aleatorias
: genere ID de notas al pie aleatorias para evitar conflictos cuando se muestran varios documentos en una página.

Procesar Markdown dentro de HTML
: De forma predeterminada, Markdown dentro de las etiquetas HTML generalmente se ignora. Esta opción obliga a Marked a continuar procesando dentro de los elementos del bloque. Tenga en cuenta que algunas marcas pueden causar problemas.


### Representación

Conservar saltos de línea en los párrafos
: Respete los saltos de línea en el texto del párrafo, reemplazándolos con saltos duros en lugar de concatenar con la línea anterior.

Representar casillas de verificación de GitHub
: Renderice `- [ ]` y `- [x]` para crear casillas de verificación en listas. Las casillas de verificación se muestran para vista previa pero no funcionan dentro de Marcado.

\#El texto es una etiqueta
: permite que los hashtags (`#` seguidos inmediatamente por texto sin espacios) se interpreten como etiquetas, no como titulares. Esta funcionalidad es predeterminada para los usuarios de Bear.
: __Etiquetas de estilo__ hace que las etiquetas se muestren con formato de "cápsula" para distinguirlas del texto. Cuando esto está habilitado, las etiquetas se pueden mostrar/ocultar usando {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Texto con etiqueta habilitada][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Renderizar `==highlight==` y `~~delete~~`
: Si esta opción está habilitada, el texto `==highlight==` se representará como una etiqueta HTML `<mark>`, que aparecerá resaltada en amarillo a menos que un Estilo la modifique de otra manera. Además, la sintaxis `~~delete~~` se representará con una etiqueta `<del>`.

: Si __Renderizar como CriticMarkup__ está habilitado, entonces la sintaxis `==highlight==` y `~~delete~~` se convertirá a CriticMarkup, que luego se podrá mostrar en las vistas original, de marcado y editada.

Renderizar `~text~` como guión bajo
: Si esta opción está habilitada, `~text~` rodeado de tildes simples se mostrará subrayado. Esto entra en conflicto con la sintaxis de MultiMarkdown para el subíndice y está deshabilitado de forma predeterminada.