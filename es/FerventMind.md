# <%= @title %>

Los mapas de FerventMind (`.fvmd`) se abren en Marked. Marked descomprime el paquete. Si dentro hay un `text.md`, ese archivo es la vista previa. Si no lo hay, Marked construye un esquema a partir de `map.xml`.

## Esquema a partir del mapa [outline-from-the-map]

El texto de cada tema se convierte en títulos hasta el nivel fijado por **Headings through level** (2 de forma predeterminada). Los temas más profundos pasan a ser viñetas anidadas, de modo que las tareas de esos niveles conservan una casilla de lista. Las notas pasan a ser el cuerpo de la sección. Una tarea terminada se muestra como una casilla marcada, y una tarea parcial muestra su porcentaje. Las imágenes son los archivos de `assets/`, sin un pie con el nombre del archivo.

## Mostrar solo los temas visibles [display-only-visible-topics]

**Display only visible topics**, en {% prefspane Apps %} dentro de *FerventMind*, omite los temas que están dentro de una rama plegada cuando Marked construye ese esquema. No modifica un `text.md` que la aplicación ya haya guardado.

## Incluir un mapa [including-a-map]

Incluir un `.fvmd` usa **FerventMind files** bajo **Embed as Mermaid mind maps:** en {% prefspane Apps %}. Activado produce un diagrama Mermaid del árbol visible o completo, según la casilla anterior. Desactivado incrusta el `preview.png` del mapa. Consulte [Incorporar esquemas y mapas mentales](Embedding_Mind_Maps_and_Outlines.html).

## Abrir en el editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) abre FerventMind.
