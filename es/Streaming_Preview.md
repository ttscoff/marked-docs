<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Al abrir {% appmenu File, New, Streaming Preview %}, Marked recibe actualizaciones en vivo a través de un portapapeles con nombre en lugar de mirar un archivo en el disco. La aplicación fuente debe integrarse con Marked.

[Curio](Curio.html), [Borradores](Drafts.html) y [The Archive](The_Archive.html) documentan sus propios cambios y comandos de menú. nvUltra, nvALT, Bear y otros usan el mismo canal: abra la vista previa de la transmisión en Marked, habilite la integración en su editor y comience a escribir; Las actualizaciones llegan casi en tiempo real.

## Desarrolladores [developers]

Para integrar Streaming Preview con su aplicación, solo necesita colocar el texto de rebajas para obtener una vista previa en un portapapeles con nombre. Utilice el siguiente código (Objective-C) para actualizar, preferiblemente en un método didEndEditing o en intervalos limitados:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Declarar una URL base para activos relativos [declaring-a-base-url-for-relative-assets]

También puede proporcionar una URL base para la vista previa de la transmisión, lo que permite que las URL relativas en imágenes y otros recursos funcionen como lo harían en la aplicación de origen. Si la URL base incluye un nombre de archivo, su nombre y extensión estarán disponibles para los procesadores personalizados, pero no es obligatorio hacerlo. Para incluir la URL base, simplemente coloque un objeto NSURL en el portapapeles:

```obj-c
NSString *rawString = @"The text to be processed\\n\\n![](images/screenshots/mainwindow-feature-stats.jpg)";
NSURL *baseURL = [NSURL fileURLWithPath:@"/Users/username/Documents/HelpDocs/Main Window.md"];
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb writeObjects:@[rawString, baseURL]];
```

O en Swift:

```swift
let rawString = "The text to be processed\n\n![](images/screenshots/mainwindow-feature-stats.jpg)"
let baseURL = URL(fileURLWithPath: "/Users/username/Documents/HelpDocs/Main Window.md")
let pb = NSPasteboard(name: "mkStreamingPreview")
pb.clearContents()
pb.writeObjects([rawString, baseURL])
```

Si se utiliza la versión de Marked para Mac App Store y no se puede acceder a la URL base a través del espacio aislado, se solicitará permiso la primera vez que se cargue la URL en la vista previa.

### Declaración de la aplicación fuente [declaring-the-source-application]

Las aplicaciones también pueden declararse como fuente del contenido de la vista previa al incluir una línea de metadatos `source`. Por lo general, esto se logrará dentro de un comentario HTML para permitir la compatibilidad con los procesadores GFM y MultiMarkdown. Simplemente indique el nombre de la aplicación o la identificación del paquete:

```html
<!--
source: Bear.app
-->
```

### Abrir la vista previa de transmisión mediante programación [opening-the-streaming-preview-programatically]

Su aplicación puede abrir la Vista previa de transmisión mediante programación utilizando el método de controlador de URL `x-marked-3://stream/`. Este método también acepta un parámetro `x-success` en el que puede pasar un ID de paquete de una aplicación para activarla al finalizar.