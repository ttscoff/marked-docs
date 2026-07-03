<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Llamadas

## Oso/Obsidiana ##

Marked admite llamadas con la sintaxis utilizada por Obsidian y Bear, que es una cita en bloque con formato especial:

	> [!NOTE] Título de la nota
	> Texto adicional

La "NOTA" en `[!NOTE]` no distingue entre mayúsculas y minúsculas. Puede ser cualquiera de:

- NOTA
- RESUMEN, RESUMEN, TLDR
- INFORMACIÓN
- TODO
- CONSEJO, PISTA, IMPORTANTE
- ÉXITO, VERIFICAR, TERMINAR
- PREGUNTA, AYUDA, Preguntas frecuentes
- ADVERTENCIA, PRECAUCIÓN, ATENCIÓN
- FRACASO, FRACASO, DESAPARECIDO
- PELIGRO, ERROR
- ERROR
- EJEMPLO
- COTIZACIÓN, CITA

Estos crearán bloques con formato especial.

Puede usar `+` o `-` para hacer que la leyenda sea plegable. Un signo más (`+`) significa que la leyenda se puede contraer pero se abre de forma predeterminada. Un signo menos (`-`) significa que la leyenda se puede contraer pero está cerrada de forma predeterminada.

  ![Rótulos en Marcado][rrótulos]

[callouts]: images/callouts-800.jpg @2x width=800

### Zona de juegos Xcode ###

Al obtener una vista previa de los archivos de Xcode Playground, Marked admite la sintaxis de llamada nativa de Xcode Playground:

	- Atención: Título opcional
	El contenido destacado va aquí.

El tipo de llamada (por ejemplo, "Atención") no distingue entre mayúsculas y minúsculas y puede ser cualquiera de los siguientes tipos de llamada de Xcode Playground:

- **Atención** - Diseñado como llamada de información
- **Autor** - Llamada de metadatos
- **Autores** - Llamada de metadatos
- **Error** - Aviso de error/peligro
- **Complejidad** - Llamada estilo nota
- **Copyright** - Llamada de metadatos
- **Llamada personalizada** - Llamada de estilo de ejemplo
- **Fecha** - Llamada de metadatos
- **Ejemplo** - Ejemplo de llamada
- **Experimento** - Llamada estilo sugerencia
- **Importante** - Llamada de estilo informativo
- **Invariante** - Llamada estilo nota
- **Nota** - Llamada de nota
- **Condición previa** - Llamada estilo nota
- **Poscondición** - Llamada estilo nota
- **Observación** - Llamada estilo nota
- **Requiere** - Llamada estilo nota
- **Ver también** - Llamada de estilo informativo
- **Desde** - Llamada de metadatos
- **Versión** - Llamada de metadatos
- **Advertencia** - Aviso de advertencia

El título opcional después de los dos puntos se utilizará como título destacado. Si no se proporciona ningún título, se utilizará el nombre del tipo de llamada como título.

El contenido de la leyenda sigue inmediatamente en la siguiente línea (no se requiere una línea en blanco). El contenido continúa hasta una línea en blanco, la siguiente leyenda, un bloque de código delimitado o el final del documento.

Ejemplo:

````rebaja
- Importante: Nota de rendimiento
Este algoritmo tiene complejidad O (n log n).

- Ejemplo: clasificación rápida
Aquí se explica cómo implementarlo:

```swift
func quickSort(_ array: [Int]) -> [Int] {
   // implementation
}
```
````

También puedes omitir el título por completo:

	- Advertencia
	Esta es una advertencia sin un título personalizado.

Estos rótulos se convierten automáticamente al formato de rótulo de Marked y se les aplica el estilo adecuado. El tipo de llamada original se conserva en el atributo `data-callout`, lo que permite un estilo CSS personalizado si se desea.

> Esta función solo funciona al obtener una vista previa de archivos de Xcode Playground (`.playground`). Los archivos de rebajas normales no procesarán esta sintaxis.


## Tabla de contenidos

Puede especificar en qué parte del documento debe aparecer la tabla de contenido usando `<!--TOC-->`. Si esto está configurado, anula la opción en Preferencias y siempre se mostrará en la ventana de vista previa, así como al guardar e imprimir. La tabla de contenido se mostrará solo una vez, incluso si hay varios especificadores `<!--TOC-->` en el contenido.

Si agrega `max#` a la etiqueta anterior (donde # es un dígito del 1 al 5), controlará la profundidad de la tabla de contenido mostrada. Por ejemplo, `<!--TOC max2-->` solo mostrará encabezados de primer y segundo nivel en la lista. También puede especificar un nivel de encabezado mínimo con `<!--TOC min2-->`. Los máximos y mínimos se basan en los niveles de titulares reales, no en los niveles anidados. El máximo y el mínimo se pueden utilizar juntos.

Marked también reconoce el estilo MultiMarkdown `{{TOC}}` y el estilo Pandoc `{{TOC:2-6}}`, donde `2-6` es el rango de niveles mínimo y máximo de encabezados a incluir.

De forma predeterminada, la tabla de contenido se imprimirá en la primera página del documento si "Imprimir tabla de contenido" está habilitado en {% prefspane Export %}. Si existe un marcador en el documento, se colocará en ese punto.

I> Puede especificar el tipo de numeración o letras de cada nivel de una jerarquía de Tabla de contenido anidada en {% prefspane Export %}.

## Saltos de página

Puede forzar un salto de página para la salida impresa/PDF utilizando la sintaxis:

```html
<!--BREAK-->
```

Coloque el token en una línea por sí solo y generará un marcado que forzará una nueva página en ese punto. Marked también entiende el formato Leanpub:

	{::salto de página /}

## El desplazamiento automático se detiene [pausa]

Marked puede funcionar como un Teleprompter usando la función [Desplazamiento automático](Autoscroll.html) (debe agregar el [Estilo de Teleprompter](https://markedapp.com/styles/preview?style=teleprompter)). Al hacerlo, puede resultar útil incluir pausas en el documento. Haz esto usando:

```html
<!--PAUSE:X-->
```

Donde `X` es la cantidad de segundos durante los cuales Marked debe pausar. Entonces, insertar `<!--PAUSE:15-->` le daría una pausa de 15 segundos cuando ese punto del documento llegue a la mitad de la pantalla.

## El archivo incluye

El contenido de archivos adicionales se puede insertar utilizando la sintaxis:

	<<[carpeta/nombre de archivo]

La ruta al archivo puede ser relativa al archivo de índice o absoluta. Incluye se pueden anidar; puedes usar esta misma sintaxis dentro de un archivo incluido. Si utiliza rutas relativas, las inclusiones en archivos anidados deben ser relativas a ese archivo. ***Sin embargo,*** MultiMarkdown procesará todo según la ubicación del primer archivo abierto, por lo que todas las rutas de imágenes u otras incrustaciones deben ser relativas al primer archivo principal, incluso cuando existan en documentos secundarios.

Los metadatos de MultiMarkdown y los encabezados YAML se eliminan automáticamente de los archivos incluidos antes de renderizarlos. Esto evitará que los encabezados aparezcan en el documento, pero tenga en cuenta que los metadatos como el "nivel de encabezado base" se ignorarán en los documentos incluidos.

T> Tenga en cuenta que al visualizar documentos con archivos incluidos, puede escribir "I" (shift-i) para ver qué archivo incluido está en el área visible.

Consulte ["Documentos de varios archivos"][ext] para obtener más información.

[ext]: Multi-File_Documents.html

## Incluyendo código

Marked puede incluir archivos externos como código usando una sintaxis similar a la del archivo incluido arriba:

	<<(carpeta/nombre de archivo)

Tenga en cuenta el paréntesis en lugar de corchetes. Para compatibilidad con la sintaxis de Leanpub, Marked también reconocerá un conjunto anterior de corchetes que contiene un título, pero en este momento no se hace nada con él en Marked:

	<<[Título del código](carpeta/nombre de archivo)

El contenido del archivo especificado se insertará dentro de un bloque de pre>código en su documento y estará disponible para resaltado automático de sintaxis si está habilitado. Los bloques de código no se pueden anidar y no se procesarán con MultiMarkdown. Los procesadores personalizados seguirán ejecutándose sobre el bloque de código previo creado.

## Incluyendo texto sin procesar o html

E> **Nota:** Esta función es para usuarios avanzados.

Si desea incluir HTML sin formato u otro texto que no debe ser procesado por MultiMarkdown (o su procesador personalizado), puede usar llaves (`{}`) para incluir un archivo *después* de procesar el resto del documento:

	<<{carpeta/raw_file.html}

No se reconocerá ninguna sintaxis de inclusión dentro de estos archivos (sin anidamiento) y el contenido **sin formato** del archivo se insertará en la salida HTML final. Esto es excelente para insertar HTML sin atascar el procesador de texto o convertir o escapar cosas cuando no lo desea, pero tenga cuidado ya que existen pocas medidas de seguridad para garantizar que se conserve el formato del documento alrededor de lo que inserta.