<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked comprende los catálogos de documentación [Apple DocC](https://www.swift.org/documentation/docc/) (`.docc` paquetes). Cuando obtiene una vista previa de Markdown que se encuentra dentro o al lado de un catálogo, Marked puede resolver referencias de imágenes **sin extensiones** a archivos en la carpeta `Resources` del catálogo, incluidas las variantes `~dark` y `@2x`.

Para documentos Markdown normales que usan **rutas con extensiones de archivo** (`images/icon.png`), consulte [Variantes de imagen](Image_Variants.html). Esa característica funciona en todas partes; La resolución DocC es específica del catálogo.

## Habilitando la resolución DocC [enabling-docc-resolution]

En {% prefspane Apps %}, habilite **Resolver referencias de imágenes DocC** (activado de forma predeterminada).

La detección de DocC se ejecuta cuando Marked encuentra un `.docc` antecesor del catálogo del documento abierto. No se requiere ningún esquema de URL especial ni integración con Xcode: abra el Markdown del catálogo de la misma manera que lo haría con cualquier otro archivo.

## Referencias sin extensión [extensionless-references]

Dentro de un catálogo DocC, los autores suelen hacer referencia a imágenes **sin** una ruta o extensión:

```markdown
![Order flow](OrderStateTransitions)
```

Marcado resuelve `OrderStateTransitions` a `Resources/OrderStateTransitions.png` (u otro tipo admitido) cuando ese archivo existe en el catálogo.

Las referencias que ya incluyen una ruta y una extensión (`images/chart.png`) se dejan en [Variantes de imagen](Image_Variants.html) y no se reescriben mediante resolución DocC.

## Modo oscuro y variantes de Retina [dark-mode-and-retina-variants]

Los catálogos DocC suelen incluir varios archivos por imagen:

| Rol | Ejemplo en `Resources/` |
|------|-------------------------|
| Luz (1x) | `diagram.png` |
| Oscuro (1x) | `diagram~dark.png` |
| Luz (2x) | `diagram@2x.png` |
| Oscuro (2x) | `diagram~dark@2x.png` |

Cuando existe más de una variante, Marked emite el mismo marcado responsivo `<picture>` descrito en [Variantes de imagen](Image_Variants.html). Una referencia de un solo archivo todavía se resuelve en una ruta normal `<img>` o `![](Resources/...)`.

## HTML y rebajas [html-and-markdown]

La resolución DocC se aplica durante el pase de inclusión de Marked:

- **Fuentes de Markdown** — `![alt](ImageName)` referencias
- **Fuentes HTML** — `<img src="ImageName">` sin extensión

Ambos se actualizan antes de la presentación preliminar.

## Observación de archivos [file-watching]

Las imágenes resueltas en la carpeta del catálogo `Resources` se agregan a la lista de observación de Marked. La edición de un archivo de variante actualiza externamente la vista previa sin necesidad de una actualización manual.

## Temas relacionados [related-topics]

- [Variantes de imagen](Image_Variants.html) — `~dark` y `@2x` detección de rutas basadas en extensiones en cualquier proyecto
- [Xcode Playgrounds](Xcode_Playgrounds.html): vista previa del comentario del área de juegos de Swift
- [Configuración: Aplicaciones](Settings_Apps.html) — Preferencias de variantes de imagen y DocC