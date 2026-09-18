<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Estas opciones están en la hoja **Configurar Apex**. Ábrala desde {% prefspane Processor %} cuando el procesador predeterminado sea **Apex (beta)**. Todas las opciones de aquí se aplican solo a Apex. Las matemáticas, Critic Markup, las etiquetas, las inclusiones de archivos y los ID de encabezados siguen en los demás ajustes de Marked.

Consulte [Apex (beta)](Apex.html) para saber qué es Apex y la sintaxis que cubre.

Las casillas de la hoja tienen prioridad sobre los mismos ajustes de un archivo de metadatos de Apex. Las rutas de archivo son opcionales. Si Marked no puede leer una ruta, la omite y la vista previa sigue funcionando.

## Archivos [files]

CSL
: Un archivo de Citation Style Language (`.csl`) que Apex usa al dar formato a una bibliografía. Déjelo vacío para usar el estilo indicado en el documento o en el archivo de metadatos.

Bibliografía
: Uno o más archivos de bibliografía. Se aceptan BibTeX (`.bib`), CSL JSON (`.json`) y CSL YAML (`.yml`, `.yaml`). Pulse **Añadir** para otro archivo. Apex busca en estos archivos al resolver citas.

Concordancia
: Uno o más archivos de concordancia (`.tsv`, `.txt` o `.csv`) usados al generar un índice. Pulse **Añadir** para otro archivo.

Archivo de metadatos
: Un archivo externo de metadatos (`.yml`, `.yaml`, `.txt` o `.md`) que se combina antes de que Apex se ejecute. Si el documento y el archivo definen la misma clave, prevalecen los metadatos del documento. Las casillas de esta hoja ganan a los valores del archivo de metadatos.

## Sintaxis [syntax]

Activadas de forma predeterminada, salvo que se indique lo contrario.

Tablas
: Tablas con barras verticales, incluida una fila de encabezado y una fila separadora.

Notas al pie
: Notas de referencia (`[^id]`) y notas en línea.

Listas de definiciones
: Listas de término y definición (`: definición`).

Superíndice / subíndice
: `^super^` y `~sub~`. Desactívelo si una tilde simple no debe significar subíndice. El ajuste **Representar ~text~ como subrayado** de Marked es independiente y entra en conflicto con el subíndice.

Tachado
: `~~eliminado~~`.

Enlazar automáticamente URL y correos
: Las URL `https://` y las direcciones de correo sueltas se convierten en enlaces.

Divs delimitados
: Bloques `::: nombre` que envuelven una sección en un `<div>`.

Spans entre corchetes
: Spans de atributos en línea, como `[texto]{.class}`.

Listas alfabéticas
: Listas que empiezan por `a.` o `A.`, además de los números.

Marcadores de lista mixtos
: Una lista puede mezclar `*`, `+` y `-` y seguir siendo una sola lista.

Markdown dentro de HTML
: Se procesa el Markdown dentro de etiquetas de bloque HTML. Algunas marcas pueden seguir fallando.

Transformaciones de metadatos
: Los marcadores `[%key]` se sustituyen con los metadatos del documento.

## Tablas e imágenes [tables-and-images]

Tablas de cuadrícula
: Tablas dibujadas con `+` y `|`. Desactivadas de forma predeterminada.

Tablas flexibles
: Las tablas con barras pueden omitir las barras inicial y final. Activadas de forma predeterminada.

Alineación por celda
: Los marcadores de alineación de una celda sustituyen la alineación de la columna. Activado de forma predeterminada.

Pies de imagen
: El título de la imagen, o el texto alternativo si no hay título, se muestra como pie. Activado de forma predeterminada.

Solo pies de título
: Solo el título de la imagen se usa como pie. El texto alternativo se ignora. Desactivado de forma predeterminada. No tiene efecto si **Pies de imagen** está desactivado.

## Enlaces e índices [links-and-indexes]

Enlaces wiki
: Apex convierte `[[enlaces wiki]]`. Desactivado de forma predeterminada. Si está activado, Marked omite su propio paso de vista previa «Convertir enlaces wiki» en ese documento, y Apex puede resolver el archivo de destino de forma distinta a Marked. La extensión predeterminada sale de los ajustes de enlaces wiki de Marked.

Sanear URL de enlaces wiki
: Las URL generadas se pasan a minúsculas, se quitan los apóstrofos y se sustituyen los caracteres que no son letras ni números. Desactivado de forma predeterminada. Solo está disponible si **Enlaces wiki** está activado.

Procesamiento de índices
: Reconoce marcadores de índice (estilos MultiMarkdown, mmark, Leanpub y textindex). Activado de forma predeterminada.

Suprimir la salida del índice
: Sigue leyendo los marcadores, pero no imprime el índice generado. Desactivado de forma predeterminada.

## Avisos (extra) [callouts-extra]

Ambos están desactivados de forma predeterminada. Los avisos de Obsidian y Bear (`> [!NOTE]`) los trata Marked antes de Apex y no se controlan aquí.

Avisos de Python-Markdown (!!!)
: Avisos del estilo `!!! note`.

Avisos de Quarto
: Bloques Quarto `::: {.callout-note}`.

## Accesibilidad [accessibility]

Ambos están desactivados de forma predeterminada.

Etiquetas ARIA
: Añade atributos ARIA que describen la estructura del HTML que emite Apex.

Anclas de encabezado
: Emite un ancla `<a>` en cada encabezado en lugar de solo un `id` en el encabezado.
