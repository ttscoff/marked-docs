<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked funciona con notas de [Obsidian][obsidian-app] de dos maneras: abre una **carpeta de bóveda** para un seguimiento automático o usa el **complemento comunitario** para una sincronización más estrecha.

La vista previa incorporada de Obsidian es ideal cuando nunca sales de la aplicación. Elija Marcado cuando desee exportar con calidad de publicación, revisión avanzada, temas CSS personalizados o el mismo flujo de trabajo de vista previa en vivo en varios editores. Consulte [Vista previa de Marcado vs Obsidiana](Marked_vs_Obsidian_Preview.html) para obtener una comparación completa.

## Abrir una bóveda completa

Arrastre la **carpeta de la bóveda** (el directorio que contiene la carpeta de configuración oculta de Obsidian en la raíz de la bóveda) a Marked in the Dock. Marcado observa ese árbol, mantiene la nota **editada más recientemente** en la vista previa y se actualiza a medida que guarda en Obsidian.

Para los valores predeterminados específicos de la bóveda (estilo, procesador, URL base para imágenes, etc.), agregue una [Regla personalizada](http://support.markedapp.com) que coincida con las rutas de esa bóveda.

## Sintaxis de llamada de obsidiana

Cuando se ejecuta el procesador MultiMarkdown, Marked convierte **notas de estilo obsidiana** comunes (el patrón `> [!note]`) en marcas de bloque con estilo para que coincidan con el resto de la vista previa.

## Complemento de obsidiana marcado 3

El [complemento Marked 3 Obsidian][complemento] puede abrir la nota actual o toda la bóveda con comandos o teclas de acceso rápido para que la ventana Marcada rastree lo que está editando. Utilice la paleta de comandos (**⌘P**) y busque **Marcado**, o asigne teclas de acceso rápido en la configuración de **Teclas de acceso rápido** de Obsidian.

### Instalación desde complementos comunitarios

En Obsidian, abra **Configuración → Complementos de la comunidad**, explore o busque **marcado** e instale **Abrir en marcado**.

### Instalación manual del complemento

Si prefieres instalar desde GitHub:

1. Descargue `main.js` y `manifest.json` de la [última versión][lanzamientos de complementos] en GitHub (o compílelos desde el repositorio [Marked3-obsidian][complementos]).
2. En su bóveda, cree la carpeta de complementos en `plugins/` dentro del directorio de configuración de Obsidian en la raíz de la bóveda. El nombre de la carpeta debe coincidir con el complemento `id` en `manifest.json` (consulte el [complemento LÉAME] [complemento] para obtener la ruta completa).
3. Copie `main.js` y `manifest.json` en esa carpeta.
4. En Obsidian, abra **Configuración → Complementos comunitarios**, desactive **Modo restringido** si es necesario y habilite **Abrir en marcado**.

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest