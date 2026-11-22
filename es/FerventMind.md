# <%= @title %>

Los mapas de FerventMind (`.fvmd`) se abren en Marked. Marked descomprime el paquete y muestra el `text.md` que FerventMind guardó.

## Markdown en el mapa [markdown-in-the-map]

Cómo se escribe ese Markdown se define en FerventMind, en **Settings > Files And Export**, dentro del grupo **Markdown**. Marked muestra el archivo tal como se guardó.

![FerventMind Files And Export][fm-export]

**Headings** fija cuántos niveles siguen siendo títulos. **Visible topics only** omite los temas que están dentro de una rama plegada. **Notes** y **Task checkboxes** deciden si las notas y las tareas se escriben en ese Markdown. Estas opciones valen para la exportación Markdown, para Copy As y para la copia Markdown guardada en cada mapa para aplicaciones como Marked. Un mapa puede cambiarlas en **Definitions • MAP**.

Si un mapa antiguo no tiene `text.md`, Marked construye un esquema a partir de `map.xml`: el título es el título 1, el nivel siguiente es el título 2 y los temas más profundos pasan a ser viñetas anidadas. Las notas pasan a ser el cuerpo de la sección. Una tarea terminada se muestra como una casilla marcada, y una tarea parcial muestra su porcentaje. Las imágenes son los archivos de `assets/`, sin un pie con el nombre del archivo.

## Incluir un mapa [including-a-map]

Incluir un `.fvmd` usa **FerventMind files** bajo **Embed as Mermaid mind maps:** en {% prefspane Apps %}. Activado produce un diagrama Mermaid a partir del mapa. Desactivado incrusta el `preview.png` del mapa. Consulte [Incorporar esquemas y mapas mentales](Embedding_Mind_Maps_and_Outlines.html).

## Abrir en el editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) abre FerventMind.

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
