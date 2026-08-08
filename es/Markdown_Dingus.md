<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Markdown Dingus es una herramienta de prueba especializada que ayuda
comprende cómo los diferentes procesadores Markdown manejan su
contenido. Proporciona una interfaz de tres paneles donde puede
editar Markdown, ver la fuente HTML generada y ver el
vista previa renderizada simultáneamente.

El Dingus comparte algo de manejo de bajo nivel con el de Marked.
vista previa, como el tratamiento especial de bloques de código vallados.
__No__ ejecuta [Reglas personalizadas](Custom_Processor.html)
(Director de orquesta). Utiliza la mayoría de las configuraciones predeterminadas, ignorando las configuraciones.
como "nuevas líneas de GitHub" y "casillas de verificación de GitHub", por lo que
El resultado puede diferir de lo que se ve en un marcado normal.
vista previa.

## Las reglas personalizadas no se aplican [custom-rules-do-not-apply]

El Dingus es un __procesador sandbox__: tu Markdown va
directamente al procesador integrado que elijas (MultiMarkdown,
CommonMark (GFM), Descuento o Kramdown). [Reglas personalizadas](Custom_Processor.html)
nunca ejecute allí: no hay acciones previas al proceso, buscar/reemplazar reglas,
comandos de shell, insertar texto/archivo u otros pasos de Conductor.

En una vista previa normal, las reglas personalizadas pueden cambiar el Markdown
antes de renderizar, establecer estilos, inyectar CSS o JavaScript, y
más. Nada de eso sucede cuando editas en el Dingus.
Cambiar las reglas personalizadas mientras el Dingus está abierto no
actualizar su vista previa.

El Dingus __puede__ usar los mismos [estilos CSS de vista previa](Custom_Styles.html)
como ventana principal (a través del menú de estilo en el panel de salida).
Eso es sólo apariencia; no es lo mismo que ejecutar Personalizado
Reglas.

__Abrir en Dingus__ desde una vista previa carga el documento
búfer de Markdown actual. Si las reglas personalizadas ya se ejecutaron cuando
ese archivo se abrió en Marcado, puede ver sus efectos en
el texto (por ejemplo, texto insertado por una regla), pero el
Dingus no volverá a aplicar las reglas mientras escribe. Para probar personalizado
Reglas, use una vista previa marcada estándar o guarde desde Dingus
y abra el archivo con __Abrir en Marcado__.

## ¿Qué es un "Dingus"? [what-is-a-dingus]

Un "dingus" es un término tomado del desarrollo web que
se refiere a una herramienta de prueba simple o un entorno sandbox. el
Markdown Dingus te permite experimentar con la sintaxis de Markdown y
Vea inmediatamente cómo lo interpretan los diferentes procesadores.

## Accediendo al Dingus [accessing-the-dingus]

Se puede acceder al Markdown Dingus desde
[{% appmenu Help, Markdown Dingus %}][2]. es particularmente
útil cuando estás:

* Aprender nueva sintaxis de Markdown
* Solución de problemas de renderizado
* Elegir entre diferentes procesadores
* Redacción de documentación que debe funcionar en múltiples
  sistemas

## Diseño de tres paneles [three-pane-layout]

![][1]

La ventana de Dingus se divide en tres paneles sincronizados:

### 1. Entrada de rebajas (panel izquierdo) [1-markdown-input-left-pane]

* __Resaltado de sintaxis__: Su Markdown se resalta con
  colores para aclarar la estructura
* __Edición en vivo__: escriba y vea los cambios reflejados al instante
  en los otros paneles
* __Fuente grande__: fuente Menlo de 21 puntos para una edición cómoda

__Menú desplegable de opciones__ (arriba a la derecha del panel izquierdo): El
El menú **Opciones** te permite alternar:

* __Mostrar números de línea__: Muestra un medianil a la izquierda con
  un número de línea por párrafo (las líneas ajustadas cuentan como una
  línea).
* __Mostrar invisibles__: Muestra espacios como puntos medios (·), tabulaciones como
  una flecha hacia la derecha (→) y nuevas líneas como retorno de carro
  símbolo (↵) en gris claro para que puedas detectar
  espacio en blanco.
* __Resaltar gremlins__: Pone un fondo rojo claro
  caracteres no ASCII (por ejemplo, comillas, emoji) y un color oscuro
  fondo rojo en personajes invisibles problemáticos (p. ej.
  espacios de ancho cero). Los caracteres de tabulación y nueva línea normales son
  no resaltado.

Tus elecciones se guardan y se restauran la próxima vez que abras
los Dingus.

__Barra de búsqueda__: Presione **⌘F** para mostrar la barra de búsqueda debajo del
Etiqueta "Entrada de rebajas". Puedes buscar y reemplazar en el
editor, use **⌘G** para Buscar siguiente y **⇧⌘G** para Buscar
Anterior y reemplazar una o todas las coincidencias. Presione el cierre
o **⌘F** nuevamente para ocultar la barra de búsqueda.

### 2. Fuente HTML (panel central) [2-html-source-middle-pane]

* __HTML generado__: vea exactamente qué HTML es el seleccionado
  el procesador crea
* __Sintaxis resaltada__: HTML está codificado por colores para facilitar
  leyendo

### 3. Vista previa renderizada (panel derecho) [3-rendered-preview-right-pane]

* __Vista previa en vivo__: vea cómo se verá su Markdown cuando
  prestado
* __Soporte de emoji__: emojis estilo GitHub como `:zzz:` son
  convertidos a imágenes
* __Desplazamiento automático__: se desplaza automáticamente para mostrar su
  posición de edición actual

## Edición en el Dingus [editing-in-the-dingus]

El panel Entrada de Markdown incluye funciones de edición inteligentes para
Haga que escribir Markdown sea más rápido y natural.

### Nueva línea inteligente (tecla de retorno) [smart-newline-return-key]

Al pulsar Retorno se adapta a la línea actual:

* __Lists__: En una línea de lista (`-`, `*`, `+` o `1.`),
  inserta un nuevo elemento de lista con el marcador correcto. Numerado
  las listas continúan con el siguiente número.
* __Blockquotes__: En una línea que comienza con `>`, inserta un
  nueva línea de cita en bloque.
* __Vallas de código__: En una línea con tres o más comillas invertidas
  (por ejemplo, ` ``` `), inserta una línea en blanco entre la apertura
  y cerrar vallas.
* __Otras líneas__: Inserta una nueva línea normal.

### Emparejamiento de personajes [character-pairing]

Cuando escribes un carácter de apertura, el editor automáticamente
inserta el carácter de cierre y coloca el cursor entre
ellos. Pares admitidos: `"` `'` `(` `[` `` ` `` `<` .

* __Con selección__: Envuelve el texto seleccionado en el par.
* __Sin selección__: Inserta el par con el cursor
  entre ellos.
* __Type-over__: Si el siguiente carácter ya es el
  cerrando el delimitador, al escribirlo nuevamente el cursor pasa
  en lugar de insertar un duplicado.
- __Espacio en par vacío__: si el cursor está entre un par vacío (por ejemplo, `(|)`), escribir un espacio reemplaza el carácter de cierre con un espacio.

### Teclas de acceso directo [shortcut-keys]

| Atajo | Acción |
|:-----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⌘F** | Mostrar u ocultar la barra de búsqueda en el panel Entrada de Markdown |
| **⌘G** | Buscar siguiente (cuando la barra de búsqueda esté visible) |
| **⇧⌘G** | Buscar anterior (cuando la barra de búsqueda está visible) |
| **⌘B** | Negrita: ajuste la selección en `**` o inserte `**\|**` con el cursor entre |
| **⌘Yo** | Cursiva: ajuste la selección en `_` o inserte `_\|_` con el cursor entre |
| **⇧⌘L** | Marcador de lista de ciclos (desordenado ↔ ordenado) |
| **Pestaña** | Sangrar línea o elemento de lista |
| **Mayús+Tab** | Línea sin sangría o elemento de lista |
| **⌃⌘→** | Sangrar línea o elemento de lista (igual que Tabulador) |
| **⌃⌘←** | Eliminar sangría de línea o elemento de lista (igual que Mayús+Tab) |
| **⌃⌘ ↑** | Mover párrafo hacia arriba (cortar párrafo incluyendo nueva línea, pegar una línea hacia arriba) |
| **⌃⌘↓** | Mover párrafo hacia abajo (cortar párrafo incluyendo nueva línea, pegar una línea hacia abajo) |
| **⌘K** | Insertar o ajustar un enlace de Markdown: ajustar la selección como `[text]()` y colocar el cursor en la URL, o insertar `[]()` con el cursor entre corchetes cuando no haya selección |
| **⌘U** | Alternar panel de salida (Fuente/Vista previa) |
| **⌥⌘ ↑** | Ampliar selección: palabra → delimitadores internos/externos → oración → párrafo → bloque contiguo (como una tabla o bloque de código) → lista adjunta/cita en bloque/bloque de código → documento |
| **⌥⌘↓** | Selección de contrato de nuevo a través de los mismos niveles hasta la posición de intercalación original |

Tab/Shift+Tab (y ⌃⌘←/⌃⌘→) respetan la estructura de la lista y
citas en bloque: sangran o eliminan la sangría de los elementos de la lista y añaden o
elimine `>` de las líneas de comillas en bloque. Mover párrafo arriba/abajo
selecciona todo el párrafo debajo del cursor (incluido su
nueva línea final), lo corta y lo pega encima o debajo del
párrafo adyacente para que los párrafos no se fusionen.

### Pegar URL inteligente [magic-links-and-footnotes-f6-f7]

Cuando pegas y el portapapeles contiene una URL del formulario
`protocol://...` sin espacios:

* __Con una selección__: la selección se convierte en una
  Enlace de rebajas: `[selected text](url)`.
* __Sin selección__: la URL se inserta como un
  autoenlace: `<url>` .

Esto facilita convertir las URL copiadas en enlaces sin
escritura manual.

### Selección inteligente (⌥⌘ ↑ / ⌥⌘↓) [smart-url-paste]

El editor Dingus admite __expansión de selección semántica__:

* __⌥⌘ ↑__ comienza en el cursor y expande la selección
  a través de:
	- la palabra actual
	- contenido delimitado interior y exterior (comillas, paréntesis,
   paréntesis y bloques de código delimitados)
	- la sentencia actual
	- el párrafo actual
	- el bloque de líneas contiguos que no están en blanco (por ejemplo, un
   tabla completa o bloque de código de varias líneas sin líneas en blanco)
	- el elemento de la lista adjunta, cita en bloque o bloque de código
	- el documento completo
* __⌥⌘↓__ vuelve a bajar por los mismos niveles hasta que
  vuelve a la posición original del cursor.

Cada pulsación siempre se mueve a un estrictamente mayor o menor
selección, para que nunca recibas pulsaciones de teclas "no operativas" mientras
expandiéndose o contrayéndose.

## Usando Dingus como editor [using-the-dingus-as-an-editor]

El Dingus no pretende reemplazar un texto completo
editor, pero puede ser muy útil para ediciones rápidas con un
vista previa en vivo__, especialmente cuando quieres ver exactamente cómo
los cambios se renderizarán. Todo el comportamiento de edición de texto.
descrito en [Edición en Dingus][3] se aplica aquí.

### Abrir un archivo/crear un archivo nuevo [opening-a-filecreating-a-new-file]

* __Crear un nuevo archivo en el Dingus__
	- Elige __{% appmenu File, New, New Markdown File %}__
   (⌘N).
	- Cuando se le solicite, elija __Dingus__ para iniciar un nuevo archivo sin guardar.
   Documento Dingus.
	- Se abren nuevos documentos de Dingus con contenido de muestra seleccionado;
   simplemente comience a escribir para reemplazarlo.
* __Abrir un archivo existente en el Dingus__
	- Utilice __{% appmenu File, Open in Dingus... %}__ (⌥⌘O), o
   con la ventana de Dingus activa, haga clic en __Abrir…__ en el estado
   barra. El comando abre la ventana de Dingus si es necesario, luego
   muestra el panel Abrir.
	- Elija cualquier archivo de texto sin formato/Markdown compatible; es
   Los contenidos reemplazarán el buffer de Dingus actual.
* __Abrir un documento de vista previa marcado en el Dingus__
	- Desde una ventana de vista previa normal, use __{% appmenu Preview,
   Open in Dingus %}__ (⌥⌘E).
	- El Markdown del documento actual se carga en Dingus
   para que puedas experimentar sin tocar el archivo original
   hasta que elijas guardar. Las reglas personalizadas no se aplican en
   los dingus; consulte [No se aplican reglas personalizadas] (#reglas-personalizadas-no-se-aplican).

### Guardar un archivo [saving-a-file]

* __Guardar cambios en el archivo actual__
	- En la ventana de Dingus, haga clic en __Guardar__ en la barra de estado,
   o usar
    __{% appmenu File, Save Dingus %}__ (⌘S).
	- Si el documento de Dingus aún no se ha guardado, serás
   se le solicita una ubicación y un nombre de archivo; después de eso, ⌘S
   actualiza el mismo archivo.
* __Guardar como/duplicar en un archivo nuevo__
	- Utilice __{% appmenu File, Save Dingus As... %}__ (⌥⌘S).
	- Esto siempre abre un cuadro de diálogo __Guardar como__ y escribe el
   contenidos actuales de Dingus a un nuevo archivo sin sobrescribir
   el original.

### Vista previa en marcado [previewing-in-marked]

* __Abrir el documento de Dingus como vista previa marcada completa__
	- Haga clic en __Abrir en Marcado__ en la barra de estado de Dingus, o use

__{% appmenu File, Open Dingus in Marked %}__ (⌘P).
	- Si el documento de Dingus no está guardado o tiene cambios no guardados,
   se le pedirá que guarde primero; luego Marcado abre un
   vista previa estándar para ese archivo.

Usando estos comandos, puedes tratar al Dingus como un
editor liviano para soluciones rápidas y experimentos, luego
salte a una vista previa marcada completa o a su editor habitual cuando
estás listo para una edición más extensa.

## Selección del procesador [processor-selection]

Utilice el menú desplegable en la parte superior para cambiar entre diferentes
Procesadores de rebajas:

* __MultiMarkdown__: Procesador con todas las funciones con tablas,
  notas a pie de página y apoyo matemático
* __CommonMark (GFM)__: Procesador estándar y rápido siguiendo el
  Especificación de marca común
* __Descuento__: GitHub Flavored Markdown con tarea
  listas y tablas
* __Kramdown__: Procesador avanzado con características adicionales
  como IAL y tipografía

## ¿Por qué utilizar el Dingus? [why-use-the-dingus]

### Comprensión de las diferencias entre procesadores [understanding-processor-differences]

Los diferentes procesadores Markdown manejan la sintaxis de manera diferente. el
Dingus te ayuda a:

* __Comparar salida__: vea exactamente cómo representa cada procesador
  la misma rebaja
* __Problemas de depuración__: Identificar por qué cierta sintaxis no es
  trabajando como se esperaba
* __Aprender sintaxis__: comprender las diferencias sutiles
  entre implementaciones de procesador

### Probar antes de escribir [testing-before-writing]

Antes de comprometerse con un estilo Markdown particular en su
documentos:

* __Validar sintaxis__: asegúrese de que su Markdown se muestre
  correctamente
* __Elija procesadores__: decida qué procesador funciona mejor
  por tu contenido
* __Experimente de forma segura__: pruebe una nueva sintaxis sin afectar
  tus documentos reales

## Casos de uso comunes [common-use-cases]

### Diferencias de sintaxis de tablas [table-syntax-differences]

Algunos procesadores manejan la sintaxis de las tablas de manera diferente. El dingus
te permite ver qué procesador soporta mejor tu mesa
necesidades de formato.

### Soporte de notas al pie [footnote-support]

No todos los procesadores admiten notas a pie de página. Usa el Dingus para
verifique que la sintaxis de las notas al pie funcione con el procesador elegido.

### Matemáticas y caracteres especiales [math-and-special-characters]

Pruebe cómo manejan las matemáticas diferentes procesadores
Expresiones y caracteres tipográficos especiales.

## Consejos para un uso eficaz [tips-for-effective-use]

1. __Empiece simple__: comience con Markdown básico y gradualmente
   agregar complejidad
2. __Probar casos extremos__: Pruebe combinaciones de sintaxis inusuales para
   comprender los límites del procesador
3. __Comparar lado a lado__: cambie entre procesadores para
   ver las diferencias claramente
4. __Utilice contenido real__: copie el contenido real de su
   documentos para probar escenarios del mundo real

El Dingus es una poderosa herramienta para cualquiera que quiera
comprender los matices de las diferentes implementaciones de Markdown
y garantizar que su contenido se muestre correctamente en varios
plataformas y procesadores.

[1]: images/dingus-interface-800.jpg @2x width=800px height=573px class=center
[2]: x-marked-3://dingus
[3]: #editing-in-the-dingus