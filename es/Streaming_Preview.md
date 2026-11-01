<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Al abrir {% appmenu File, New, Streaming Preview %}, Marked recibe actualizaciones en vivo a través de un portapapeles con nombre en lugar de mirar un archivo en el disco. La aplicación fuente debe integrarse con Marked.

[Curio](Curio.html), [Borradores](Drafts.html) y [The Archive](The_Archive.html) y [Traverse](Traverse.html) documentan sus propios cambios y comandos de menú. nvUltra, nvALT, Bear y otros usan el mismo canal: abra la vista previa de la transmisión en Marked, habilite la integración en su editor y comience a escribir; Las actualizaciones llegan casi en tiempo real.

## Desarrolladores [developers]

Para integrar Streaming Preview con su aplicación, solo necesita colocar el texto de rebajas para obtener una vista previa en un portapapeles con nombre. Utilice el siguiente código (Objective-C) para actualizar, preferiblemente en un método didEndEditing o en intervalos limitados:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Declarar la app de origen y el formato [declaring-the-origin-app-and-format]

Pon una palabra clave `source` o `format` en un comentario HTML al principio del texto enviado. Marked lee el comentario y lo quita de la vista previa, así que la nota sigue siendo compatible con los procesadores GFM y MultiMarkdown. El espacio después de los dos puntos es opcional (`source:Bear.app` y `source: Bear.app` son lo mismo) y la palabra clave no distingue mayúsculas.

Los dos valores son de forma libre. Marked tiene un comportamiento integrado para algunos, y todos están disponibles en el [Custom Processor](Custom_Processor.html) (Conductor) como **Origen de la vista previa en streaming** y **Formato de la vista previa en streaming**. Esos criterios aceptan **es**, **no es**, **contiene** y **no contiene**.

**`source: APP_NAME`** nombra la app de origen, con el nombre de la app o el bundle id. Marked lo usa para añadir un tratamiento especial para esa app. `source: Bear.app` y `source: Drafts.app` activan el comportamiento de vista previa de esas apps. Cualquier otro nombre se puede comparar con una regla de Conductor, para ejecutar tus propias acciones para esa app:

```html
<!--source:Bear.app-->
```

**`format: fountain`** activa el tratamiento de [Fountain](Fountain_for_Screenwriters.html), así que el envío se previsualiza como un guion en lugar de Markdown. Cualquier otro valor de formato no cambia el procesador. Sirve para que una regla de Conductor lo compare, por ejemplo **Formato de la vista previa en streaming** `es` `fountain`.

```html
<!--format:fountain-->
```

Un comentario puede llevar las dos palabras clave:

```html
<!--
source: Bear.app
format: fountain
-->
```

### Abrir la vista previa de transmisión mediante programación [opening-the-streaming-preview-programatically]

Su aplicación puede abrir la Vista previa de transmisión mediante programación utilizando el método de controlador de URL `x-marked-3://stream/`. Este método también acepta un parámetro `x-success` en el que puede pasar un ID de paquete de una aplicación para activarla al finalizar.