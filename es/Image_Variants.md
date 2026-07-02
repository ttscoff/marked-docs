<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked puede crear automáticamente elementos `<picture>` responsivos para imágenes locales cuando los archivos complementarios **modo oscuro** y **Retina** se encuentran junto a la imagen a la que hace referencia. Utiliza las mismas convenciones de nomenclatura que los catálogos de documentación DocC de Apple, pero funciona para **cualquier documento Markdown o HTML** con rutas de imagen normales que incluyan una extensión de archivo.

Consulte también [Soporte DocC](DocC_Support.html) para obtener referencias de catálogos sin extensión dentro de los paquetes `.docc`.

## Habilitar variantes de imagen

En {% prefspane Apps %}, habilite **Resolver variantes de imagen oscura y @2x** (activado de forma predeterminada) en la configuración de DocC.

Esta preferencia es independiente de **Resolver referencias de imágenes DocC**, que solo se aplica dentro de los catálogos `.docc`. Puede utilizar uno, ambos o ninguno según su proyecto.

## Convención de nomenclatura

Coloque los archivos variantes en la **misma carpeta** que la imagen principal. Marcado busca cuatro combinaciones basadas en el nombre base:

| Rol | Nombre de archivo de ejemplo |
|------|------------------|
| Luz (1x) | `icon.png` |
| Oscuro (1x) | `icon~dark.png` |
| Luz (2x) | `icon@2x.png` |
| Oscuro (2x) | `icon~dark@2x.png` |

El orden de los sufijos es flexible: `icon@2x~dark.png` y `icon~dark@2x.png` se tratan de la misma manera.

Extensiones admitidas: `png`, `jpg`, `jpeg`, `gif`, `svg`, `webp` y `pdf`.

## Lo que se reescribe

Marked escanea su documento **antes** de la presentación preliminar final:

- **Rebaja:** `![Alt text](images/icon.png)`
- **HTML:** `<img src="images/icon.png" alt="Alt text">`

Si existen al menos **dos** archivos de variantes coincidentes en el disco, la referencia se reemplaza con un bloque `<picture>`. Un único archivo adicional es suficiente; no necesita las cuatro variantes.

Ejemplo de salida cuando hay archivos claros, oscuros y @2x presentes:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

La vista previa (y la exportación HTML) sigue la apariencia del sistema del usuario para las variantes oscuras y la densidad de píxeles del dispositivo para los recursos @2x.

## ¿Qué se omite?

Marcado **no** reescribe:

- URL remotas (`http://`, `https://`, `data:`)
- Referencias que ya apuntan a un archivo `~dark`
- `<img>` etiquetas que ya están dentro de un elemento `<picture>` existente
- Nombres sin extensión como `![Diagram](diagram)`: use [DocC Support](DocC_Support.html) para referencias de estilo catálogo

## Vista previa en vivo y visualización de archivos

Cuando se detectan variantes, Marked agrega **todos los archivos de variantes existentes** a su lista de vigilancia junto con el documento principal. Guardar `icon~dark.png` en un editor externo activa la misma recarga de imagen en vivo que editar `icon.png`.

## Consejos

- Haga referencia a la imagen **light 1x** en su fuente cuando sea posible (`icon.png`, no `icon~dark.png`). Marked descubre hermanos de ese camino.
- Si solo tiene `@2x` activos, incluya al menos otra variante (normalmente `~dark`) o Marcado dejará la referencia sin cambios.
- La resolución variante utiliza rutas **relativas al documento** (o la carpeta del archivo incluido para inclusiones anidadas), las mismas reglas de ruta base que [Documentos de varios archivos](Multi-File_Documents.html).

## Temas relacionados

- [Soporte DocC](DocC_Support.html) — nombres de imágenes sin extensión dentro de catálogos `.docc`
- [Configuración: Aplicaciones](Settings_Apps.html): alterna preferencias para DocC y variantes de imagen
- [Vista previa](Previewing.html): vista previa en vivo y actualizaciones de archivos