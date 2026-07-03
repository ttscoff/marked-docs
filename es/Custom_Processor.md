<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>


Marked te brinda control total con reglas personalizadas y texto
transformaciones y la capacidad de ejecutar sus propios comandos o ejecutar
diferentes procesadores basados en propiedades de archivos coincidentes.


## Uso de preprocesadores/procesadores personalizados

Para agregar procesadores personalizados, vaya a {% prefspane Processor %}
y haga clic en **Reglas personalizadas**.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


En el Editor de reglas (también conocido como "Conductor"), puede agregar reglas personalizadas.
reglas que tienen criterios para hacer coincidir archivos según el nombre del archivo,
ruta, coincidencias en el contenido, metadatos e incluso si
existen otros archivos en el mismo árbol que el documento que se está
abierto. Cuando una regla coincide, las acciones definidas para la
La regla se ejecuta en ese archivo.

> Debajo del campo Procesador, las casillas de verificación en "Nuevo
> los documentos usan personalizado: "determinar si las reglas se prueban
> en absoluto para las fases de Preprocesador y Procesador. En general,
> déjelos marcados, pero si desea anularlos por completo
> cualquier procesador personalizado, configúrelo aquí.

![Editor de reglas][2]

  [2]: imágenes/CustomRules-800.jpg @2x ancho=800

Para crear una nueva regla, use el `+`
en la parte inferior de la lista de reglas de la izquierda. Dale el
regule un nombre y configúrelo como preprocesador o procesador.

Los tres puntos junto a una regla indican Preprocesador, Procesador y Habilitado. Solo se puede resaltar uno de los Preprocesador o Procesador y puede hacer clic en los puntos para cambiar los estados de la regla.

Preprocesador
: se ejecuta después de que el archivo se procesa inicialmente, cuando Marked agrega archivos incluidos, maneja preferencias de estilo como nuevas líneas de GitHub, etc., pero antes de la fase de procesamiento. El documento todavía es Markdown sin formato en este punto y puede realizar cambios en el contenido para pasarlo al procesador. Si ningún procesador personalizado coincide, o no se ejecuta ninguna acción Ejecutar procesador en un procesador personalizado coincidente, se ejecutará el procesador predeterminado.

Procesador
: Un procesador personalizado reemplaza el procesador integrado definido en {% prefspane Processor %}. Puede manejar todas las acciones que puede realizar un preprocesador y agrega acciones Ejecutar comando y Ejecutar procesador. Esto le permite ejecutar un comando personalizado, p. Pandoc, o ejecute un procesador integrado diferente en archivos que coincidan con los criterios.

Todas las tablas en el editor de reglas personalizadas se pueden reordenar mediante
arrastrar y soltar, para que pueda afectar el orden en el que
se ejecutan las reglas, el orden de los criterios en el predicado
editor y el orden de las acciones que se ejecutarán en secuencia.

### Editor de predicados

![Editor de predicados][predicado]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

Una vez agregada una regla, use el editor de predicados para definir
criterios que determinarán si la regla se ejecuta para un
archivo dado. Utilice el menú desplegable del lado izquierdo para seleccionar un
criterio, luego use los campos comparador y valor para construir
el predicado.

- _filename_ coincide solo con el nombre del archivo
- _extension_ coincide solo con la extensión del archivo
- _path_ coincide con la ruta POSIX (Unix) completa del archivo
- _tree_ busca coincidencias de nombres de archivos en cualquier parte del
  árbol de directorios del archivo
- _text_ coincide con el contenido de texto del archivo. Usar hacia adelante
  barra diagonal alrededor del valor del texto para convertirlo en un valor normal
  búsqueda de expresiones.
- _fileIncludes_ prueba si el archivo contiene datos incluidos.
  archivos (usando cualquiera de [Marked's include
  sintaxis](Multi-File_Documents.html)).
- _metaType_ prueba si el archivo incluye YAML,
  Metadatos de MultiMarkdown o Pandoc
- _metadata.X_ prueba claves de metadatos específicas como autor,
  fecha, título, etc.

Para hacer coincidir todos los archivos (es decir, un procesador personalizado que siempre
se ejecuta), establezca `filename` en `contains` `*`. El asterisco
actúa como comodín y coincide con todos los archivos.

[Agregar un predicado][agregarpredicado]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Haga clic en el signo más (+) en la fila de predicados para agregar otro predicado. Mantenga presionada la opción mientras hace clic en + para agregar un grupo booleano que se puede configurar en Todos (Y) o Cualquiera (O).

### Acciones

Utilice el botón *+ Acción* para agregar acciones a la regla.

![Agregar una acción][agregar]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

Las acciones disponibles incluyen:

Establecer estilo
: establece el estilo para la vista previa. Cualquier estilo integrado o estilo personalizado que haya agregado está disponible.

Ejecutar comando
: Esto toma un comando de línea de comando, incluidos los argumentos, y pasará el contenido del archivo en STDIN. El comando debería devolver el resultado resultante en STDOUT.

> **Mac App Store Sandboxing**: la versión Mac App Store (MAS) de Marked se ejecuta en un entorno sandboxing que restringe la ejecución de archivos binarios externos. Si necesita utilizar procesadores externos como Pandoc en la versión MAS, debe copiar el binario en el paquete de la aplicación. Para hacer esto:
>
> 1. Haga clic derecho en Marked.app → Mostrar contenido del paquete
> 2. Navegue a Contenidos/Recursos/
> 3. Crea una carpeta `bin` si no existe
> 4. Copie su binario (por ejemplo, `pandoc`) en este
> `bin` carpeta
> 5. Hazlo ejecutable: `chmod +x` el binario
> 6. En la acción Ejecutar comando, haga referencia a él como:
>
> `YOUR_BINARY_NAME [arguments]`
> O utilice la ruta completa:
> `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **Nota**: Los scripts con shebangs externos (como los scripts de Python que apuntan a `/opt/homebrew/bin/python`) se ejecutarán automáticamente a través de intérpretes del sistema cuando se copien en el paquete. Es posible que la versión MAS aún tenga problemas para ejecutar archivos binarios que en realidad son scripts de Python o Ruby en lugar de archivos binarios.
> Deberá volver a copiar los archivos binarios después de cada actualización de la aplicación, ya que las actualizaciones reemplazan el paquete completo. Alternativamente, use **Ayuda->Crossgrade** para obtener la versión sin espacio aislado que no tiene tales restricciones.

Ejecutar secuencia de comandos incrustada
: edite un script completo en el editor de código integrado. Al igual que Ejecutar comando, esto debería recibir entrada en STDIN y devolver salida en STDOUT.

Establecer metadatos
: Agrega o establece metadatos. Proporcione una clave y un valor. Si la clave existe, se actualizará su valor, si no, se agregará. El tipo de metadatos utilizados estará determinado automáticamente por el contenido del archivo (o el resultado de una acción de conversión de metadatos).
: Si no se encuentran metadatos existentes, los metadatos se agregarán en formato MultiMarkdown dentro de un comentario HTML. Marked puede leer estos metadatos, pero no aparecerán en la vista previa sin importar qué procesador se utilice.

Eliminar metadatos
: elimina un metadato según su clave.

Tirar metadatos
: elimina todos los metadatos. Afecta a los metadatos de YAML, MultiMarkdown y Pandoc.

Convertir YAML Meta a MMD
: convierte un bloque de metadatos YAML en la parte superior del archivo en metadatos de estilo MultiMarkdown.

Convertir MMD Meta a YAML
: convierte un bloque de metadatos MultiMarkdown a YAML.

Buscar y reemplazar
: realice una búsqueda y reemplace el contenido del archivo.
: Si la cadena de búsqueda está rodeada de barras diagonales (por ejemplo, `/Project \w+/`), se tratará como una expresión regular. Puede utilizar `$1`, `$2`, etc. para incluir grupos coincidentes en la cadena de reemplazo.
: El campo de reemplazo admite algunas secuencias de escape (una barra invertida seguida de): `\n` inserta una nueva línea, `\t` inserta un carácter de tabulación, `\\` inserta una barra invertida literal, `\$` inserta un signo de dólar literal (en lugar de un grupo de coincidencia)
: Cualquier otra secuencia `\X` se trata simplemente como `X` (la barra invertida se elimina), por lo que `\e` se convierte en `e`. Un \ final sin ningún carácter después se conserva como una barra invertida literal.
: Utilice `[%key]` en la cadena de reemplazo para insertar un valor de los metadatos del documento, variables de entorno o contexto (por ejemplo, `[%title]`, `[%MARKED_PATH]`). Están disponibles las claves establecidas por acciones anteriores en la misma regla o por una regla anterior. Las claves no coincidentes se reemplazan por una cadena vacía.

Insertar título H1
: Inserta un H1 en el documento. Esto se puede extraer de los metadatos o del nombre del archivo.

Encabezados de cambio
: Ajusta los niveles del encabezado, desde -5--+5. Por ejemplo, si configura esto en -1, entonces todos los H1 se convierten en H2, los H2 se convierten en H3, etc. Configúrelo en un número positivo para elevar los niveles del encabezado en esa cantidad.

Normalizar encabezados
: Esta acción garantizará, si es posible, que solo haya un H1 en el documento y ajustará todos los niveles de encabezado para que estén en un orden semántico y no se salten niveles, p. de H2 a H4. Si, para empezar, el documento original está ordenado semánticamente, esto refinará bien la jerarquía.

Insertar tabla de contenidos
: Insertar una tabla de contenido. El TOC puede ir después del primer H1, el primer H2 o en la parte superior del archivo (se insertará después de cualquier metadato).

Insertar archivo
: Inserta un archivo de texto seleccionado en un punto determinado del documento. Esto puede ser después del primer H1, primer H2, arriba, abajo o después de una coincidencia de texto (use `/pattern/` para buscar una expresión regular).

Insertar texto
: Proporciona un editor emergente con el que puede incrustar texto directamente en la acción. Las opciones de posicionamiento son las mismas que _Insertar archivo_.
: utilice `[%key]` en cualquier parte del texto insertado para extraer valores de los metadatos del documento, variables de entorno o contexto marcado (por ejemplo, `[%author]`, `[%MARKED_PATH]`). Esto funciona independientemente del procesador que utilice, por lo que no necesita MultiMarkdown para la sustitución de metadatos. Se incluyen los valores de acciones anteriores en la misma regla (como **Establecer metadatos**) o de una regla anterior. Las claves no coincidentes se reemplazan por una cadena vacía.

Insertar archivo CSS
: inyecta un archivo CSS seleccionado en el documento. Esto se cargará después de cualquier selección de estilo y se puede usar para anular estilos existentes o agregar otros nuevos.

Insertar CSS
: Ofrece un editor CSS emergente donde puedes agregar tu propio CSS directamente a la acción. Este CSS se inyectará en la parte superior del documento, después de cualquier estilo existente. El orden de los estilos inyectados coincidirá con el orden de las acciones en la regla.

Insertar archivo JavaScript
: inyecta un archivo JavaScript seleccionado al final del documento. Tenga en cuenta que debe utilizar una acción *Insertar JavaScript* con un [gancho de actualización](#updatehook) si desea que el script se recargue con cada actualización.

Insertar JavaScript desde la URL
: utilice esto para insertar una etiqueta `<script>` vinculada a una CDN u otra URL remota al final del documento. Tenga en cuenta que debe utilizar una acción *Insertar JavaScript* con un [gancho de actualización](#updatehook) si desea que el script se recargue con cada actualización.

Insertar JavaScript
: Proporciona un editor de JavaScript emergente con el que puede incrustar JavaScript personalizado directamente en la acción. Esto se inyectará al final del documento, y el orden de JavaScript ejecutado por la regla estará determinado por la secuencia de las acciones, con la última acción agregada en último lugar.
: Tenga en cuenta que necesita utilizar un [gancho de actualización](#updatehook) si desea que los scripts se ejecuten con cada actualización.

URL de autoenlace
: convierta cualquier URL simple a `<url>`, lo que generará un hipervínculo en cualquier procesador.

Ejecutar acceso directo
: ejecute un acceso directo de Apple. Cualquier ejecución de acceso directo debe recibir información de STDIN y devolver la salida al final (Detener y devolver salida). Si desea realizar acciones que no modifiquen el texto, establezca la entrada en una variable, ejecute sus acciones y luego genere la variable de texto original al final.

Ejecutar servicio del sistema
: Ejecute cualquier servicio del sistema en `~/Library/Services`. El Servicio debe aceptar entradas y devolver salidas.

Ejecutar el flujo de trabajo de Automator
: Ejecute cualquier archivo de Automator `.workflow`. La entrada se pasará por STDIN y se espera la salida por STDOUT.

Continuar
: De forma predeterminada, una vez que una regla coincide, el procesamiento se detendrá (por separado para preprocesadores y procesadores, de modo que un preprocesador y un procesador puedan coincidir). Esta acción forzará que la coincidencia de reglas continúe después de que la regla realice sus acciones.

### Gancho de actualización

Marked no realiza una actualización completa con cada actualización, por lo que si
tienes scripts que representan partes del DOM, necesitan
para ejecutar su función de renderizado utilizando la API Hook de Marked.

El siguiente ejemplo utiliza Mermaid, que en realidad nunca
Tienes que hacerlo, ya que Mermaid ahora está incluida de forma predeterminada. pero
así es como lo haría si lo incluyera manualmente.

Agregue una acción **Insertar JavaScript** y en "Editar JS"
ventana, inicialice el script y agregue el gancho:

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

Esto hará que `mermaid.run()` se ejecute cada vez
Marked realiza una actualización parcial.

### Reglas de prueba

El botón _Probar reglas_ debajo de la lista de reglas abrirá una
cuadro de diálogo donde puede seleccionar cualquier archivo Markdown y será
probado contra todas sus reglas. Las reglas que coincidan obtendrán
resaltado con una pestaña verde en el lado izquierdo. Al hacer coincidir
contra un archivo, aparecerá un botón X que se puede utilizar para
borre la prueba y destaque las filas.

## Arrastrar y soltar

La ventana del conductor admite arrastrar y soltar mejorados
capacidades que detectan de forma inteligente tipos de archivos y
proporcionar acciones apropiadas basadas en el archivo arrastrado. el
La implementación incluye un sistema de superposición dividida para texto.
archivos que permite a los usuarios elegir entre probar el archivo
contra reglas o agregarlo como una acción.

![Arrastrar y soltar en reglas personalizadas][arrastrar]

[drag]: images/draganddropconductor.jpg @2x width=800

### Detección de tipo de archivo

El sistema detecta automáticamente diferentes tipos de archivos y
muestra mensajes superpuestos apropiados:

- **Archivos CSS** (`.css`): muestra la superposición "Insertar archivo CSS"
- **Archivos JavaScript** (`.js`, `.javascript`): muestra "Insertar
  Superposición de archivo JS
- **Archivos de script** (cualquier archivo ejecutable)): muestra "Ejecutar
  Superposición de comando
- **Archivos de texto**: muestra superposición dividida
- **Archivos ejecutables**: muestra la superposición "Ejecutar comando"
- **Extensiones desconocidas**: El valor predeterminado es el tipo "texto" y se muestra
  superposición dividida

## Registro de procesador personalizado

Si obtiene resultados extraños y desea ver lo que está sucediendo, el Registro de reglas personalizadas le mostrará qué reglas se están ejecutando y en qué orden. Utilice **Ayuda->Mostrar registro de reglas personalizadas** para abrirlo.

![Registro de reglas personalizadas][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Ejecutar múltiples comandos

Una regla puede tener varios comandos en secuencia. La salida de
cada comando se pasará al siguiente. si quieres tener
un comando genera algo al mismo tiempo que Marked
actualizaciones de vista previa, asegúrese de devolver el contenido original
a STDOUT para procesar el siguiente comando o incorporado
procesador.

Por ejemplo, si desea que un comando actualice un PDF
documento usando Pandoc, simplemente pase la ruta del archivo original
(de variables de entorno) a Pandoc con el correspondiente
opciones de línea de comando y luego repetir el contenido STDIN
hacia STDOUT.

## Omitir dinámicamente procesadores personalizados

Si un procesador personalizado devuelve "NOCUSTOM" en STDOUT, marcado
finalizará el procesador personalizado y volverá al
Procesador interno predeterminado. Esto le permite crear un
procesador personalizado que puede decidir si necesita o no
ejecutar usando las [variables de entorno] (#environmentvariables)
a continuación, el nombre del archivo del documento o la extensión, la coincidencia de contenido
u otra lógica.

Si en lugar de `NOCUSTOM` devuelve un Procesador personalizado
`MULTIMARKDOWN` o `DISCOUNT` (o `GFM`), `KRAMDOWN` o
`COMMONMARK`, entonces ese procesador interno se utilizará para
solo ese documento. Este cambio no afectará el valor predeterminado.
procesador configurado en Configuración.

## Variables de entorno

La acción Ejecutar comando tiene un editor de entorno donde
Puede configurar sus propias variables de entorno que serán
disponible para el comando o script. Además de estos
variables personalizadas, Marked incluye algunas propias.

Marked ejecuta el procesador personalizado en su propio shell, lo que significa
Las variables de entorno estándar no se pasan automáticamente.
Puede utilizar las variables de entorno de Marked para aumentar su
propio en sus guiones. Marcado hace las siguientes variables
disponible para usar en sus scripts de shell:

**ORIGEN_MARCADO**
: La ubicación (directorio base) de su archivo de trabajo principal (la carpeta del texto de trabajo, Scrivener o archivo de índice).

**RUTA**
: Marcado establece una ruta que incluye carpetas ejecutables predeterminadas y agrega el directorio en el `MARKED_ORIGIN` anterior. Los valores predeterminados son: `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. Puede agregar el suyo propio configurando la variable PATH según sea necesario y agregando o sobrescribiendo la ruta de Marked (por ejemplo, `PATH=/usr/local/yourfolder:$PATH`).

**INICIO**
: el directorio de inicio del usuario que inició sesión. Python y otros scripts que dependen de la configuración de la variable HOME la recogerán automáticamente, pero está disponible para otros usos en sus scripts.

**MARKED_EXT**
: La extensión del archivo principal que se está procesando. Esta variable le permite programar diferentes procesos según el tipo de archivo que se está viendo. Por ejemplo, si `$MARKED_EXT == "md"` ejecuta su procesador Markdown preferido, pero si `$MARKED_EXT == "textile"` ejecuta un procesador Textil.

**MARKED_PATH**
: Esta es la ruta UNIX completa al archivo principal abierto en Marcado en el momento de cargarse.

**MARKED_INCLUDES**
: Una lista entre comillas y separados por comas de los archivos que Marked ha incluido en el texto que se pasa utilizando las distintas [incluir sintaxis](Special_Syntax.html#pagebreaks).

**MARKED_PHASE**
: Esto se establecerá en "PROCESO" o "PREPROCESO", lo que le permitirá utilizar un único script para manejar ambas fases en función de esta variable.

**MARKED_CSS_PATH**
: La ruta completa a la hoja de estilo actual.

### Variables de entorno de metadatos

Cuando la acción Ejecutar comando se ejecuta en Marked's
Sistema conductor, los metadatos del documento se almacenan automáticamente.
extraídos y puestos a disposición como variables de entorno para el
comando.

#### Cómo funciona

1. **Extracción de metadatos**: el sistema extrae metadatos del documento utilizando el método `extractMetaDataFromString:` existente, que admite:
   - Portada de YAML (`---` bloques)
   - Metadatos de MultiMarkdown (clave: líneas de valor)
   - Metadatos de Pandoc (`%` bloques de título)
   - Metadatos de comentarios HTML (`<!-- key: value -->`)

2. **Normalización de claves**: las claves de metadatos están normalizadas para su uso como variables de entorno:
   - Convertido a minúsculas
   - Se eliminan todos los caracteres no alfanuméricos.
   - Se eliminan los espacios y caracteres especiales.

3. **Formato de variable de entorno**: cada clave de metadatos se convierte en una variable de entorno con el prefijo `MD_`:
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Ejemplo

Dado un documento con estos metadatos:

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

Las siguientes variables de entorno estarían disponibles para
comandos:

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### Uso en comandos

Ahora puede usar estas variables de entorno en su Ejecución
Acciones de comando:

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### Acciones admitidas

Esta funcionalidad de variable de metadatos a entorno es
disponible en:

- Acciones **Ejecutar comando**
- Acciones **Ejecutar script incrustado**

Los metadatos se extraen automáticamente del documento.
contenido y puesto a disposición de cualquier comando o script que
recorre estas acciones.

## Habilitar y deshabilitar

Los procesadores personalizados se pueden encender y apagar para
documentos individuales usando {% kbd opt cmd C %}. tu
También puede activar un preprocesador o procesador para un documento.
automáticamente [usando metadatos](#perdocument) en la parte superior de
el documento.

Los estados actuales de los procesadores para cada documento son
mostrados como luces indicadoras (sólo visibles cuando un procesador
está habilitado) a la izquierda de los elementos de la barra de herramientas en la parte inferior
barra de herramientas derecha de la Vista previa.

### Preprocesador

Si configura reglas de preprocesador, se ejecutan después de Marcado
maneja cualquier tarea específica de Marked, como incluir
documentos y código, pero antes de ejecutar el procesador
(interno o personalizado). Esto te da la oportunidad de renderizar
variables de plantilla personalizadas, manejar sustituciones o inyectar
su propio contenido por cualquier otro medio.

Marked establece una variable de entorno para el trabajo.
directorio (`MARKED_ORIGIN`) al directorio principal del
archivo que se está previsualizando. Puedes usar esto para cambiar el funcionamiento.
directorio de un script e incluir archivos con rutas relativas
al documento original. Como ejemplo, en Ruby puedes
uso:

	Dir.chdir(ENV['MARKED_ORIGIN'])

Cuando está habilitado, el preprocesador personalizado se puede encender y
desactivado para documentos individuales usando
{% kbd ctrl opt cmd C %}.

#### Procesador/preprocesador por documento [por documento]

Los procesadores personalizados también se pueden configurar por documento
utilizando el formato de metadatos para [Por documento
configuración](Per-Document_Settings.html).

Puede especificar si desea utilizar configuraciones de procesador personalizadas y
anular el valor predeterminado para un documento usando [Por-Documento
configuración](Per-Document_Settings.html) (`Custom Processor:`
y `Custom Preprocessor:`). Cualquier configuración que no sea "verdadera"
o "sí" desactivará el preprocesador/preprocesador personalizado.

Uso de ejemplo:

    Procesador personalizado: verdadero
    Preprocesador personalizado: falso

Como se indica en el [Por-Documento
Configuración](Per-Document_Settings.html#hidingmeta) página, usted
Puede rodear estos metadatos con marcadores de comentarios HTML para ocultarlos.
desde GitHub y otros procesadores que no lo eliminan
de la salida:

    <!--
    Procesador personalizado: verdadero
    Preprocesador personalizado: verdadero
    -->

## Usando un procesador Markdown alternativo

Cualquier versión de Markdown que puedas renderizar desde la línea de comando puede
ser utilizado con marcado. Necesita poder recibir información sobre
STDIN, que es lo mismo que "canalizar" su Markdown en
línea de comando, es decir, `cat myfile.md | myprocessor`. necesita
para devolver el HTML resultante en STDOUT, que cada
El procesador con el que he trabajado alguna vez lo hace de forma predeterminada.

Utilice `which YOUR_PROCESSOR` en Terminal para determinar la ruta
al ejecutable, luego péguelo en la ruta Ejecutar comando
campo, o simplemente arrastre el ejecutable a la ventana Reglas personalizadas
con la regla a la que desea agregar la acción seleccionada.

Si su procesador requiere argumentos en la línea de comando,
También deberás ingresarlos en el campo. Algunos
los procesadores necesitan guiones para funcionar en STDIN y/o STDOUT,
por ej. `-o - -` a menudo señala la entrada desde STDIN, la salida a
SALIDA ESTÁNDAR. Consulte la documentación de su procesador para obtener más detalles.

Probé la función Procesador personalizado con Pandoc,
Kramdown, marcado (descuento), MultiMarkdown 6, Maruku y
varios otros sabores.

### Una nota sobre Pandoc y Sandboxing

Pandoc (y algunas otras herramientas de línea de comandos) no se ejecutarán en
la versión Mac App Store (en zona protegida) de Marked.
Si necesita ejecutar Pandoc, use **Ayuda->Crossgrade** para obtener una
Licencia gratuita para la versión directa (Paddle). esto es verdad
de cualquier procesador que tenga problemas de espacio aislado: si está marcado
no puedo ejecutarlo debido a problemas de permisos MAS, lo hará
Ofrecer los pasos para realizar crossgrade. Si tienes problemas
y esto no sucede, por favor contáctame a través del
[sitio de soporte](https://support.markedapp.com/questions/add).

### Pandoc como procesador de rebajas del ejército suizo

[Pandoc](https://pandoc.org/) es, con diferencia, el más flexible
Herramienta multiuso para manejar una variedad de formatos de marcado. Por
agregando un argumento `-f` con uno de los siguientes, Pandoc puede
Sea su Procesador personalizado para cualquiera de:

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

Y muchos otros. Ver el [Pandoc
documentación](https://pandoc.org/MANUAL.html) para más
información. Para usar uno de estos como formato de entrada, simplemente agregue el
siguiente en su campo Ejecutar comando:

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc es perfecto para escribir un guión que utilice el
`$MARKED_EXT` variable de entorno para determinar qué formato
para ejecutar Pandoc, o utilizar una serie de reglas con
coincidencias de extensión. Si la extensión es `md`, use
`pandoc -f gfm` o `pandoc -f markdown_mmd` (o simplemente regresar
`NOCUSTOM` en STDOUT para usar el procesador predeterminado). Pero si es
`textile`, ejecute `pandoc -f textile` dentro del script. y si
es `wiki`, usa uno de los procesadores de marcado wiki. obtienes
la idea.

Como sabrán los aficionados a Pandoc, Pandoc también puede manejar
Amplia bibliografía y escenarios LaTeX. La mayoría de las funciones
puedes acceder a través de la línea de comando están disponibles solo
mediante el uso de argumentos de paso en Marked.

## Usando Textil

Algunas personas han preguntado cómo hacer que Textile funcione en
Marcado. Necesita tener un convertidor textil disponible en
la línea de comando. Hay algunas opciones, incluido Pandoc
(ver arriba), pero si aún no tienes Pandoc instalado,
Otras dos opciones son RedCloth para Ruby y Textile para Perl.
(requiere que estén instaladas las herramientas de desarrollo). Instalar
uno u otro:

1. Instalar textil desde
   <https://github.com/bradchoate/text-textile> **O**
   `sudo gem install RedCloth` en Terminal
2. Utilice `which textile` o `which redcloth` para determinar el
   ruta a utilizar en la configuración de ruta del procesador personalizado

¡Ahora Marked es una vista previa de textiles para ti!

## Usando AsciiDoc

1. Instale [AsciiDoctor](http://asciidoctor.org/).
2. Habilite una regla personalizada en {% prefspane Processor %} para que coincida con sus archivos AsciiDoc.
3. Configure la regla para que sea un procesador y agregue una acción Ejecutar comando
    1. Determine el camino a `asciidoc`, que será
       algo como `/usr/bin/asciidoc` o
       `/opt/local/bin/asciidoc`. Si no está seguro, utilice
       `which asciidoc` para localizar
    2. Ingrese `[PATH To asciidoc] --backend html5 -o - -` como
       el comando (el - al final envía la salida como
       SALIDA ESTÁNDAR)

Esto envía el documento actual a STDIN y muestra el
HTML generado como STDOUT.

Ver [esta esencia](https://gist.github.com/mojavelinux/6324279)
de [Dan Allen](https://gist.github.com/mojavelinux) para
más información.