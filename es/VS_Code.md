<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Visual Studio Code][vscode] no incluye Marked listo para usar, pero puede usar una extensión comunitaria para **vista previa en vivo de Markdown** en Marked: vista previa, exportación y revisión mientras sigue escribiendo en VS Code.

## Inicio rápido [quick-start]

1. Instale una extensión VS Code **Abrir en marcada** (consulte [Abrir en extensión marcada][ext] a continuación).
2. Abra su archivo Markdown en VS Code.
3. Envíe el archivo a Marcado. La vista previa se actualiza cuando lo guarda.

## Abrir en extensión marcada [open-in-marked-extension]

La extensión [Abrir en Marked][ext] (Visual Studio Marketplace) agrega una acción **Abrir en Marked**: botón de título del editor, **{% kbd shift cmd m %}**, menús contextuales en el editor y el explorador de archivos, **abrir carpeta** opcional para el explorador de archivos de Marked, un indicador de barra de estado y guardado automático opcional antes de abrir. La configuración le permite establecer la ruta a la aplicación marcada si no está en la ubicación predeterminada.

I> La extensión se publicó originalmente para Marked 2. Marked 3 usa el mismo estilo de archivo y transferencia de URL, por lo que esta integración continúa funcionando; Si algo cambia, consulte la [página de extensión] [ext] o el repositorio del autor para obtener actualizaciones.

## Requisitos [requirements]

Marcado se ejecuta solo en macOS. Instale [Marked 3][marked] y la extensión, luego apunte **ruta de la aplicación** a su aplicación Marked si es necesario.

[ext]: https://marketplace.visualstudio.com/items?itemName=vikgamov.vscode-open-in-marked2
[marked]: https://markedapp.com/
[vscode]: https://code.visualstudio.com/