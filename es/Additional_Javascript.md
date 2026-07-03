<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Puede incluir su propio JavaScript desde CDN o pegando código sin formato.

## Una nota sobre el conductor marcado

La forma más sencilla de implementar JavaScript personalizado que varía según los tipos de documentos y las ubicaciones es con el [Conductor marcado][conductor]. Le permite usar una configuración YAML para agregar scripts usando "filtros". Consulte la [página del conductor][conductor] para obtener más detalles y consulte la [configuración de muestra][configuración de muestra] para ver ejemplos.

[conductor]: https://brettterpstra.com/projects/conductor/
[sample config]: https://github.com/ttscoff/conductor-config/

## Agregar JavaScript desde CDN [cdns]

![][1]

   [1]: imágenes/capturas de pantalla/AdditionalJavascript.jpg @2x ancho=592px alto=576px clase=centro

Puede agregar URL de CDN de JavaScript en la ventana "Scripts adicionales", accesible desde {% prefspane Style %}. Ingrese las URL de CDN, una por línea. No incluya ninguna etiqueta `<script>`, solo la URL:

```
https://cdn.jsdelivr.net/gh/user/repo@version/file
https://cdn.jsdelivr.net/npm/micromark-extension-gfm-strikethrough@2.1.0/lib/html.min.js
```

> Tenga en cuenta que jQuery ya está incluido en la ventana de vista previa.

Estos scripts se insertarán al final de la vista previa, antes de la etiqueta del documento. Si necesita llamar a una función de inicio o actualizar cada vez que lo hace la vista previa, consulte [Incluyendo JavaScript sin formato](#rawjs). Para inspeccionar el DOM y depurar estos scripts en una vista previa marcada en vivo, puede adjuntar el inspector web de Safari como se describe en [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector).


### Incluyendo JavaScript sin formato [rawjs]

En el campo de texto inferior de la ventana Scripts adicionales, puede insertar JavaScript sin formato. Esto se incluirá dentro de un par `<script></script>`, así que no lo incluya en la entrada. Este campo puede contener cualquier comando JavaScript que necesite para inicializar una biblioteca incluida, realizar modificaciones DOM o cualquier cosa que desee hacer dentro de una vista WebKit. jQuery ya está incluido para facilitar la manipulación de DOM.

Estos scripts solo se ejecutarán cuando la ventana se cargue por primera vez. Cuando la Vista previa se actualiza, se realiza reemplazando partes del DOM, por lo que los scripts que necesitan actuar sobre el contenido actualizado deben hacerlo usando [Hooks](Embedding_Scripts.html#hooks).

Incluya en el campo JavaScript sin formato una llamada como esta:

```javascript
Marked.hooks.register('update', function() { myCustomFunction(); });
```
