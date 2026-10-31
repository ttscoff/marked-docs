<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Los mapas mentales y los esquemas se pueden incrustar en su vista previa de Markdown usando la [sintaxis de inclusión de Marked][incluir] o la [sintaxis de bloque de IA Writer][ia]. El comportamiento depende del formato del archivo y de la configuración "Incrustar mapas como diagramas de sirena" en {% prefspane Apps %} en *Mapas mentales/Contornos*.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Formatos admitidos [supported-formats]

### iPensamientos X (.itmz) [ithoughts-x-itmz]

Los archivos de mapas mentales de iThoughts son archivos zip que contienen datos de mapas y una imagen de vista previa opcional.

### Administrador mental (.mmap) [mindmanager-mmap]

Los archivos MindManager son archivos zip que contienen `Document.xml`. También se admiten paquetes de MindManager descomprimidos (una carpeta que contiene `Document.xml`) y rutas directas a `Document.xml`.

### Mente libre (.mm) [freemind-mm]

Los archivos de mapas mentales de FreeMind utilizan la extensión `.mm` y almacenan datos como XML. Marked detecta el formato FreeMind comprobando que el contenido del archivo comienza con `<map`; de lo contrario (por ejemplo, un fragmento de código), el archivo se incluye como texto sin formato. Los archivos FreeMind son compatibles con la incrustación de mapas mentales de Mermaid.

### OPML (.opml) [opml-opml]

OPML (lenguaje de marcado del procesador de esquemas) es un formato XML para esquemas jerárquicos, ampliamente utilizado por delineadores y lectores de feeds. iThoughts y otras aplicaciones pueden exportar a OPML. Las conversiones marcadas incluyeron archivos OPML a diagramas de mapas mentales de Mermaid.

### Bicicleta (.bicicleta) [bike-bike]

Consulte [Bike](Bike.html) para abrir un archivo `.bike`. Los esquemas de Bike incluidos siguen la casilla **Bike outlines**: activada dibuja un mapa mental Mermaid (el nombre del archivo, sin `.bike`, es el nodo raíz); desactivada dibuja una lista Markdown anidada sin título de documento.

### Tree Outliner (.treeoutline) [tree-outliner-treeoutline]

Consulte [Tree Outliner](Tree_Outliner.html). La casilla **Tree Outliner outlines** controla tanto abrir un archivo `.treeoutline` como incluirlo. Activada dibuja un mapa mental Mermaid con el título del documento como raíz. Desactivada compila títulos y listas; **Headings through level** en el grupo *Tree Outliner* fija hasta qué nivel llegan los títulos.

## Insertar mapas como diagramas de sirena [embed-maps-as-mermaid-diagrams]

Cuando está **habilitado** (el valor predeterminado), Marked convierte mapas mentales y esquemas incluidos en diagramas [Sirena](https://mermaid.js.org/):

**iThoughts, MindManager, FreeMind, OPML y Bike**: renderizados como diagramas de mapas mentales de sirena con un diseño de árbol ordenado. Para iThoughts y MindManager, la información de forma (redondeada, rectangular, hexágono, etc.) se conserva cuando esté disponible. FreeMind (`.mm`) y OPML utilizan el mismo formato de mapa mental. Los esquemas de bicicletas (`.bike`) utilizan el nombre de archivo incluido (menos la extensión) como nodo raíz del mapa mental. Las etiquetas de los nodos son texto sin formato (los enlaces se convierten en texto de enlace; las tareas se muestran como prefijos ☐ / ☑). Mermaid se incluye de forma predeterminada en cada vista previa de Markdown.

**Limitación:** La incrustación de mapas mentales (diagramas de sirena) no funciona con el analizador de descuentos. Utilice MultiMarkdown, CommonMark (GFM) o Kramdown para obtener vistas previas de mapas mentales.

Cuando **deshabilitado**:

- **iThoughts**: la imagen de vista previa incorporada (`preview.png`) del archivo .itmz está incrustada como una imagen base64. El texto alternativo de la imagen utiliza el nombre del archivo.
- **MindManager**: el esquema está incrustado como una lista Markdown anidada.
- **FreeMind**: el esquema está incrustado como una lista Markdown anidada.
- **OPML**: el esquema está incrustado como una lista Markdown anidada (sin mapa mental).
- **Bicicleta**: el esquema está incrustado como una lista Markdown anidada (sin H1); los elementos de encabezado de nivel superior se vuelven H2, los encabezados anidados están en negrita y las tareas se convierten en casillas de verificación de GitHub.

## Incluir sintaxis [include-syntax]

Utilice la misma sintaxis que para otros archivos, incluidos:

	<<[ruta/hacia/map.itmz]
	<<[ruta/hacia/mapa.mmap]
	<<[ruta/hacia/mapa.mm]
	<<[ruta/hacia/esquema.opml]
	<<[ruta/hacia/esquema.bicicleta]
	<<[path/to/outline.treeoutline]

O con la sintaxis del bloque iA Writer:

	/ruta/al/map.itmz

Las rutas pueden ser relativas al documento principal o absolutas (comenzando con `/` o `~`). Consulte [Documentos de varios archivos](Multi-File_Documents.html) para obtener más detalles.

## Conversión OPML [opml-conversion]

Los archivos OPML utilizan elementos `<outline>` anidados con un atributo `text`. When "Embed as Mermaid diagram" is enabled (see [Settings: Apps](Settings_Apps.html)), conversion produces a Mermaid mind map using the same format as iThoughts and MindManager:

- Los esquemas secundarios de `<body>` se convierten en el nivel superior (o hijos de una raíz de "Esquema" si hay varios elementos de nivel superior)
- Los contornos anidados definen la jerarquía
- `text` faltante o vacío se muestra como `(unnamed)`
- El texto se desinfecta; Se escaparon personajes especiales para Mermaid.

## Conversión de bicicletas [bike-conversion]

Los archivos `.bike` de Bike son HTML con una `<ul>` raíz y elementos `<li>`. En el modo de lista, cada fila es un elemento de lista: las filas `data-type="heading"` van en negrita, y las filas `data-type="task"` son casillas de GitHub (marcadas cuando `data-done` tiene una marca de tiempo, o cuando `data-checked` / `data-completed` es verdadero). El formato en línea y los enlaces del texto del nodo se convierten a Markdown. Abrir un archivo `.bike` usa siempre esta lista. Cuando un archivo incluido se incrusta como mapa mental Mermaid, el nombre del archivo (sin la extensión) es el único nodo raíz y las etiquetas son texto sin formato para la sintaxis mindmap de Mermaid.
