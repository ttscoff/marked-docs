<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opciones en el {% prefspane Advanced %}:

![Configuración: Avanzada][1]

[1]: images/screenshots/preferences-Advanced.jpg @2x width=689px height=1031px class=preferencepane-scroll

Metadatos YAML y Pandoc
: - __Ignorar:__ Lo deja exactamente como existe en el documento, lo que resulta útil si su procesador o preprocesador realmente usa YAML.
: - __Eliminar antes de renderizar__: el bloque YAML se elimina
: - __Tratar como metadatos MMD:__ Convierte el bloque de metadatos YAML o Pandoc al formato MultiMarkdown.

Eliminar encabezados de metadatos de MultiMarkdown
: Si esto está habilitado, los metadatos de MultiMarkdown en la parte superior del documento se eliminarán antes de procesarlos.
: esto puede resultar útil si utiliza un procesador que no sea MultiMarkdown y que, de otro modo, mostraría los metadatos en el documento renderizado. Los metadatos aún se leen antes de la eliminación, por lo que aún se reconocerá la sintaxis específica de Marked.

Imágenes alojadas en caché
: Marked no almacena en caché las imágenes en la vista previa de forma predeterminada, porque observa esas imágenes en busca de cambios y las actualiza al instante. Si está utilizando imágenes a las que se hace referencia a través de una URL web, puede activar el almacenamiento en caché de esas imágenes para acelerar la renderización en conexiones más lentas.

Analizar estadísticas de legibilidad
: Si prefiere que no se calculen [estadísticas](Document_Statistics.html), esto deshabilitará ese procesamiento. Esto puede proporcionar algunas mejoras de rendimiento en documentos muy grandes. El recuento de caracteres, palabras y oraciones seguirá funcionando.

Utilice el panel de trabajo Buscar en todo el sistema
: Esta opción permitirá a Marked seleccionar cualquier término de búsqueda que haya utilizado más recientemente en otro editor, y cualquier cosa buscada en Marked también se convertirá en la búsqueda en otras aplicaciones. Deshabilitarlo hace que la función de búsqueda de Marked sea independiente.

Utilice {% kbd cmd E %} para buscar con selección
: De forma predeterminada, {% kbd cmd E %} abre el editor predeterminado. Si esta opción está habilitada, entonces {% kbd cmd E %} funcionará como lo hace en la mayoría de las aplicaciones de edición de texto, usando el texto seleccionado para Buscar, y Abrir en el Editor se puede activar con {% kbd opt cmd E %}.

Modo de depuración
: habilita el registro de depuración. Úselo para su propia resolución de problemas y cuando informe un problema. Seleccione __Ayuda->Abrir registro de depuración__ para ver la actividad.
: Configurar en _Todos_ mostrará mensajes de información, advertencias y mensajes de error. También puede configurarlo para que muestre sólo errores o errores y advertencias.

Copia de seguridad de configuración
: Puede hacer una copia de seguridad de su configuración en un archivo JSON que puede usarse para restaurar la configuración o transferirla a una nueva máquina.