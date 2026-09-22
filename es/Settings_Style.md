Opciones en {% prefspane Style %}:

![Ajustes: Estilo][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Diseño y tipografía [layout-and-typography]

Limitar el ancho del texto en la vista previa
: Establece un ancho máximo para el cuerpo de la vista previa mediante el control deslizante (en píxeles).

Auto-guionizar en párrafos
: Permite que las palabras se dividan automáticamente con guiones.

Evitar líneas viudas en titulares y párrafos
: Fuerza un espacio irrompible entre las dos últimas palabras de titulares y párrafos para evitar que una sola palabra pase a una nueva línea.

Generar comillas y puntuación tipográficamente correctas
: Usa SmartyPants para comillas tipográficas, conversión de puntos suspensivos y otras funciones tipográficas (MultiMarkdown).

Rodear los marcadores de notas al pie con corchetes
: Si está activado, usa el formato predeterminado de MultiMarkdown para los marcadores de notas al pie ([1]). Desactívalo para eliminar los corchetes.

Activar Esquema para extensiones
: Activa automáticamente el modo Esquema para archivos con las extensiones indicadas.

Usar estilo APA
: Usa esquemas con estilo APA en lugar del formato decimal predeterminado.

Dar estilo de poesía a los bloques verbatim (código)
: Si está activado, el código con sangría de tabulación, en bloques delimitados o incluido se muestra como poesía en lugar de como bloque de código (sin resaltado de sintaxis, y con un estilo especial según el tema).

Permitir que los estilos ajusten el texto dentro de los bloques de código
: Si está activado, los estilos pueden hacer que el texto se ajuste dentro de los bloques `pre>code`. Si está desactivado, el desbordamiento horizontal siempre se desplazará.

Ajustar siempre el código
: Fuerza el ajuste de línea en los bloques de código independientemente de la configuración del estilo (anula el comportamiento de ajuste del estilo).

Detectar y aplicar estilo a texto RTL
: Detecta el idioma de cada elemento del documento y le aplica el estilo de derecha a izquierda correspondiente.

### Estilo [theme]

Gestionar estilos
: Abre la ventana del [Gestor de estilos](Style_Manager.html). Añade archivos CSS desde tu disco para que aparezcan en los menús del selector de estilos. Usa el botón `Add New Style` o arrastra archivos CSS a esta ventana. Arrastra para reordenar y usa las casillas para activar o desactivar los estilos.

Más estilos
: Abre la galería de estilos en línea para explorar e instalar estilos adicionales.

Estilo predeterminado
: El estilo seleccionado aquí se cargará para todas las ventanas nuevas, a menos que se [indique un estilo específico del documento en los metadatos](Per-Document_Settings.html) (por ejemplo, "Marked Style: Grump").

Seguir cambios en el CSS
: Cuando está activado, Marked vigilará el estilo actual en busca de cambios en el disco, lo que facilita la edición de estilos personalizados y el desarrollo web.

CSS adicional
: El CSS añadido aquí se agrega después de la hoja de estilos normal de cada estilo. Es una superposición parcial, no un sustituto completo del estilo.
: Marked reescribe los selectores en este campo (por ejemplo, las reglas de impresión deben usar `body.mkprinting #wrapper …`). No hay ninguna comprobación de tamaño o validez; consulta [Crear CSS personalizado](Writing_Custom_CSS.html#additional-css-settings).
: Esto se aplica a todos los documentos y todos los estilos, incluida la exportación a HTML cuando se incluyen los estilos. Si quieres aplicar CSS personalizado a documentos según ciertas condiciones, usa Reglas personalizadas en {% prefspane Processor %}.

### Incluir scripts [include-scripts]

Resaltado de sintaxis
: Activa el [resaltado de sintaxis](Syntax_Highlighting.html) de highlight.js para los bloques de código. Selecciona un estilo en el menú desplegable.
: Si **Solo si se especifica el idioma** está activado, el resaltado de sintaxis solo se aplicará a los bloques de código delimitados con un idioma especificado.

Activar MathJax
: Carga [MathJax](MathJax.html) para mostrar ecuaciones MathML. Elige **Local** (incluido) o **CDN** en el menú desplegable.
: **Paquetes adicionales** abre una hoja para incluir paquetes adicionales de MathJax (por ejemplo, Física y Química).
: **Configuración avanzada** abre una hoja para la configuración personalizada de MathJax.

Activar KaTeX
: Carga [KaTeX](MathJax.html#katex) como alternativa a MathJax. Solo se puede seleccionar uno de los dos.

Numerar ecuaciones
: Cuando corresponda, Marked añadirá números de figura a las ecuaciones renderizadas. Elige **Lado izquierdo** o **Lado derecho** para la numeración. Si usas MathJax, puedes elegir **Solo AMS** para numerar únicamente las ecuaciones AMS.

Mermaid
: Carga [mermaid.js](https://mermaid.js) desde una CDN para habilitar la creación de diagramas al estilo Markdown. El enlace necesario para renderizar los diagramas de Mermaid en cada actualización del documento se incluye automáticamente.

Desplazar y ampliar diagramas
: Cuando hay diagramas de Mermaid presentes, activa el zoom con {% kbd cmd %}-desplazamiento y desplázate haciendo clic y arrastrando.
