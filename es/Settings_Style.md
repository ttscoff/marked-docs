<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opciones en el {% prefspane Style %}:

![Configuración: Estilo][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Diseño y tipografía [layout-and-typography]

Limitar el ancho del texto en Vista previa
: establezca un ancho máximo para el cuerpo de la vista previa usando el control deslizante (en píxeles).

Separación automática de guiones en párrafos
: permite que las palabras se rompan automáticamente con la separación de palabras.

Prevenir viudas en titulares y párrafos
: fuerza un espacio sin separación entre las dos últimas palabras de los titulares y párrafos para evitar que palabras individuales se ajusten a una nueva línea.

Genere comillas y puntuación tipográficamente correctas
: utilice SmartyPants para comillas tipográficas, conversión de elipses y otras funciones de tipografía (MultiMarkdown).

Rodear los marcadores de notas a pie de página con corchetes
: Si está marcado, use el formato MultiMarkdown predeterminado para marcadores de notas al pie ([1]). Desmarque para eliminar los corchetes.

Habilitar esquema para extensiones
: activa automáticamente el modo Esquema para archivos con las extensiones enumeradas.

Utilice el estilo APA
: utilice contornos de estilo APA en lugar del formato decimal predeterminado.

Diseñe bloques textuales (código) como poesía
: Si está marcado, el código con sangría de tabulación, delimitado o incluido se muestra como poesía en lugar de un bloque de código (sin resaltado de sintaxis y con un estilo especial según el tema).

Permitir que los temas ajusten texto dentro de bloques de código
: Si está marcado, los temas pueden provocar un ajuste dentro de `pre>code` bloques. Si no está marcado, el desbordamiento horizontal siempre se desplazará.

Siempre envuelve el código
: Fuerza el ajuste de los bloques de código independientemente de la configuración del tema (anula el comportamiento de ajuste del tema).

Detectar y aplicar estilo a texto RTL
: Detecta el idioma por elemento en el documento y aplica el estilo de derecha a izquierda en consecuencia.

### Tema [theme]

Administrar estilos
: Abre la ventana [Administrador de estilos](Style_Manager.html). Agregue archivos CSS desde su disco para que aparezcan en los menús del selector de estilo. Utilice el botón `Add New Style` o arrastre archivos CSS a esta ventana. Arrastre para reordenar y use las casillas de verificación para habilitar o deshabilitar los estilos.

Más temas
: abra la galería de temas en línea para buscar e instalar estilos adicionales.

Estilo predeterminado
: El estilo seleccionado aquí se cargará para todas las ventanas nuevas, a menos que se indique un [estilo específico del documento en los metadatos](Per-Document_Settings.html) (por ejemplo, "Estilo marcado: Grump").

Seguimiento de cambios CSS
: Cuando esto está habilitado, Marked observará el estilo actual en busca de cambios en el disco, lo que ayudará en la edición de estilos personalizados y el desarrollo web.

CSS adicional
: El CSS agregado aquí se incluirá después de la hoja de estilo normal con todos los temas. Entre otras cosas, puede usarlo para anular la configuración en todos los ámbitos sin editar estilos internos.
: Esto se aplica a todos los documentos y todos los estilos. Si desea aplicar CSS personalizado a documentos según las condiciones, utilice Reglas personalizadas en {% prefspane Processor %}.

### Incluir guiones [include-scripts]

Resaltado de sintaxis
: active resaltado.js [resaltado de sintaxis](Syntax_Highlighting.html) para bloques de código. Seleccione un tema del menú desplegable.
: Si se marca **Solo si se especifica el idioma**, el resaltado de sintaxis solo se aplicará a los bloques de código delimitados con un idioma especificado.

Habilitar MathJax
: Carga [MathJax](MathJax.html) para mostrar ecuaciones de MathML. Elija **Local** (incluido) o **CDN** en el menú desplegable.
: **Paquetes adicionales** abre una hoja para incluir paquetes adicionales de MathJax (por ejemplo, Física y Química).
: **Configuración avanzada** abre una hoja para la configuración personalizada de MathJax.

Habilitar KaTeX
: Carga [KaTeX](MathJax.html#katex) como alternativa a MathJax. Sólo se podrá seleccionar uno u otro.

Ecuaciones numéricas
: Si corresponde, Marked agregará números de figuras a las ecuaciones renderizadas. Elija **Lado izquierdo** o **Lado derecho** para la numeración. Si usa MathJax, puede elegir **Solo AMS** para numerar solo ecuaciones AMS.

sirena
: Carga [mermaid.js](https://mermaid.js) desde una CDN para habilitar diagramas de estilo Markdown. El gancho necesario para representar diagramas de sirena en cada actualización de documento se incluye automáticamente.

Diagramas de panorámica y zoom
: Cuando haya diagramas de sirena, habilite el zoom con {% kbd cmd %}-desplazamiento y desplácese haciendo clic y arrastrando.