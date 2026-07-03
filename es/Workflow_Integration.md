<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## AppleScript

Marked incluye un [diccionario AppleScript](AppleScript_Support.html) completo para abrir archivos, controlar la vista previa (recargar, desplazarse, resaltar, desplazamiento automático, lectura rápida), leer estadísticas, configurar procesadores, copiar HTML o RTF, cambiar estilos de vista previa y exportar a Markdown, HTML, PDF, EPUB, DOCX, ODT, TextBundle, RTF y OPML. **La vista previa de encabezados/tabla de contenido** a través de AppleScript está [documentada como trabajo en progreso](AppleScript_Support.html#table-of-contents-work-in-progress) y aún no es confiable.

Puede apuntar a la aplicación, una ventana específica o un documento. Los comandos de la aplicación incluyen **abrir vista previa de transmisión**, **vista previa del portapapeles** y **cerrar todo**. Los comandos de documentos incluyen **obtener estadísticas** e **imprimir con perfil**. Los comandos de exportación aceptan un **perfil** de exportación opcional o un registro **`with`** para opciones como vista previa **estilo**, **tamaño de página** y **márgenes**. Por ejemplo:

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

Consulte [Compatibilidad con AppleScript](AppleScript_Support.html) para obtener la lista de comandos, la abreviatura de márgenes, las notas de la zona de pruebas y los consejos de depuración.

La integración de AppleScript también permite que aplicaciones como Tags.app funcionen directamente dentro de Marked.

{% note %}
## Atajos

Marcado incluye [Acciones de atajos](Shortcuts_Integration.html) nativas en macOS 13 o posterior. Utilice **Abrir y exportar archivo** para flujos de trabajo de Finder a PDF, **Exportar documento** para lo que ya esté abierto en Marcado o **Establecer estilo de vista previa** para cambiar los temas antes de exportar. Las acciones de exportación aceptan **perfiles**, **estilos** de vista previa y opciones como **tamaño de página**, **márgenes** y **tamaño de fuente** (la misma semántica que los registros AppleScript `with`).

[shortcuts]: Shortcuts_Integration.html
{% endnote %}

## Controlador de URL

El [controlador de URL marcado][urlhandler] permite una integración amplia simplemente llamando a las URL, ya sea desde AppleScript o con un comando `open` básico en un script de shell.

## Paquete de bonificación marcado

El Marked Bonus Pack es una colección de scripts, comandos y servicios. Algunos funcionan con varios editores, otros son específicos de determinados editores. Los Servicios generalmente funcionarán con cualquier editor que tenga las capacidades necesarias. El resto están organizados en carpetas según la aplicación con la que trabajan.

Puede descargar el paquete de bonificación y encontrar instrucciones para instalarlo y usarlo en este [artículo de la base de conocimientos](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html