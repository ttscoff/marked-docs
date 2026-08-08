<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## AppleScript [applescript]

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

## Controlador de URL [url-handler]

El [controlador de URL marcado][urlhandler] permite una integración amplia simplemente llamando a las URL, ya sea desde AppleScript o con un comando `open` básico en un script de shell.

## Paquete de bonificación marcado [marked-bonus-pack]

El Marked Bonus Pack es una colección de scripts, comandos y servicios. Algunos funcionan con varios editores, otros son específicos de determinados editores. Los Servicios generalmente funcionarán con cualquier editor que tenga las capacidades necesarias. El resto están organizados en carpetas según la aplicación con la que trabajan.

Puede descargar el paquete de bonificación y encontrar instrucciones para instalarlo y usarlo en este [artículo de la base de conocimientos](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html