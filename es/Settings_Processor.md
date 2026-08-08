<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opciones en el {% prefspane Processor %}:

![Configuración: Procesador][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Procesar Markdown con [process-markdown-with]

Procesador Markdown predeterminado. El procesador CommonMark es el preferido por los usuarios de GitHub, MultiMarkdown es ideal para escritores y Discount y Kramdown tienen propósitos especializados. Marked compensa algunas diferencias entre la sintaxis. Consulte __Ayuda->Referencia de Markdown__ para obtener información adicional.

Reglas personalizadas
: Haga clic en el botón Reglas personalizadas para abrir el Editor de reglas, donde puede especificar diferentes procesadores y transformaciones de documentos para ejecutar según criterios coincidentes. Consulte [Procesador personalizado](Custom_Processor.html) para obtener más detalles.

Los nuevos documentos utilizan personalizados.
: Cuando está marcada, los documentos nuevos utilizan automáticamente su **preprocesador** y/o **procesador** guardado de Reglas personalizadas sin necesidad de configuración por documento.

Acceso completo al disco
: Haga clic en **Conceder** para otorgar permiso a Marked para leer archivos fuera de su zona de pruebas cuando utilice procesadores personalizados u otras funciones que necesiten un acceso más amplio a los archivos.

Para explorar las diferencias entre los procesadores, consulte [Markdown Dingus](Markdown_Dingus.html).

###HTML

Generar identificaciones en titulares
: genera ID de encabezado según el contenido de la etiqueta h1-h6.

Utilice ID de notas al pie aleatorias
: genere ID de notas al pie aleatorias para evitar conflictos cuando se muestran varios documentos en una página.

Procesar Markdown dentro de HTML
: De forma predeterminada, Markdown dentro de las etiquetas HTML generalmente se ignora. Esta opción obliga a Marked a continuar procesando dentro de los elementos del bloque. Tenga en cuenta que algunas marcas pueden causar problemas.

### Representación [html]

Conservar saltos de línea en los párrafos
: Respete los saltos de línea en el texto del párrafo, reemplazándolos con saltos duros en lugar de concatenar con la línea anterior.

Representar casillas de verificación de GitHub
: Renderice `- [ ]` y `- [x]` para crear casillas de verificación en listas. Las casillas de verificación se muestran para vista previa pero no funcionan dentro de Marcado.

Renderizar GitHub :emoji:
: Representa los códigos cortos `:name:` como emoji estilo GitHub en la vista previa.

\#El texto es una etiqueta
: permite que los hashtags (`#` seguidos inmediatamente por texto sin espacios) se interpreten como etiquetas, no como titulares. Esta funcionalidad es predeterminada para los usuarios de Bear.

Etiquetas de estilo
: Cuando **#Texto es etiqueta** está habilitado, muestra las etiquetas reconocidas con un estilo de cápsula. Las etiquetas se pueden mostrar u ocultar desde {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Texto con etiqueta habilitada][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Renderizar `==highlight==` y `~~delete~~`
: Si esta opción está habilitada, el texto `==highlight==` se representará como una etiqueta HTML `<mark>`, que aparecerá resaltada en amarillo a menos que un Estilo la modifique de otra manera. Además, la sintaxis `~~delete~~` se representará con una etiqueta `<del>`.

: Si __Renderizar como CriticMarkup__ está habilitado, entonces la sintaxis `==highlight==` y `~~delete~~` se convertirá a CriticMarkup, que luego se podrá mostrar en las vistas original, de marcado y editada.

Renderizar `~text~` como guión bajo
: Si esta opción está habilitada, `~text~` rodeado de tildes simples se mostrará subrayado. Esto entra en conflicto con la sintaxis de MultiMarkdown para el subíndice y está deshabilitado de forma predeterminada.