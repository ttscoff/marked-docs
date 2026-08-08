<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked funciona con muchos editores y aplicaciones de escritura. Esta página cubre **configuraciones** compartidas, la **vista previa del portapapeles**, sugerencias para la **vista previa de transmisión** y recursos de secuencias de comandos. Las guías detalladas para aplicaciones populares se encuentran en sus propios temas de ayuda (consulte la sección **Aplicaciones compatibles** en la barra lateral).

## Guías por aplicación [per-app-guides]

Comience con [Vista previa de Live Markdown en Mac](Live_Markdown_Preview_on_Mac.html) para el flujo de trabajo general. Si usa Obsidian, consulte [Vista previa de Marked vs Obsidian](Marked_vs_Obsidian_Preview.html) para decidir cuándo Marked agrega valor junto con la vista previa integrada de Obsidian.

| Tema | Página de ayuda |
| :-- | :-- |
| **Oso** | [Oso](Bear.html) |
| **Curio** (vista previa de transmisión) | [Curiosidad](Curio.html) |
| **Borradores** (vista previa del streaming + acciones) | [Borradores](Drafts.html) |
| **DEVONthink** (Integración del menú Script) | [DEVONthink](DEVONthink.html) |
| **Visualización de carpetas** (nvALT, nvUltra, etc.) | [Visualización de carpetas](Folder_Watching.html) |
| **Tierras Altas** | [Tierras Altas](Highland.html) |
| **Marca de gancho** Resolución de URL | [Marca de gancho](Hookmark.html) |
| **iA escritor** | [iA Writer](iA_Writer.html) |
| **iThoughtsX** `.itmz` mapas | [iThoughtsX](iThoughtsX.html) |
| **MarsEdit** vista previa en vivo | [MarteEditar](MarsEdit.html) |
| **Nodo mental** | [NodoMente](MindNode.html) |
| **Compositor de MultiMarkdown** | [Compositor de MultiMarkdown](MultiMarkdown_Composer.html) |
| **nvUltra** | [nvUltra](nvUltra.html) |
| **Obsidiana** bóvedas y rótulos | [Obsidiana](Obsidian.html) |
| **OmniOutliner/OPML** | [OmniOutliner y OPML](OmniOutliner_and_OPML.html) |
| **RTF / RTFD** (Páginas, Edición de texto, etc.) | [Soporte RTF y RTFD](RTF_Support.html) |
| **PDF** | [Soporte PDF](PDF_Support.html) |
| **escribiente 3** | [Soporte de Scrivener 3](Scrivener_Support.html) |
| **El Archivo** vista previa de transmisión | [El Archivo](The_Archive.html) |
| **Ulises** flujo de trabajo de exportación | [Ulises](Ulysses.html) |
| **Vim** (complemento marcado con vim) | [Vim](Vim.html) |
| **Código VS** (Abrir en extensión marcada) | [Código VS](VS_Code.html) |
| **VudúPad** | [VoodooPad](VoodooPad.html) |
| **Patios de juegos Xcode** | [Parques infantiles de Xcode](Xcode_Playgrounds.html) |

## Configuración de la aplicación [application-settings]

I> Varias integraciones exponen alternancias dentro de {% prefspane Apps %} y {% prefspane Preview %}.

![Configuración de la aplicación][configuración de la aplicación]

Utilice estos paneles para valores predeterminados de enlaces wiki, transferencia de Scrivener, configuraciones de portapapeles transmitidas, opciones de incrustación de mapas mentales para OPML/OmniOutliner, integraciones de Obsidian u otros procesadores que dependen de editores cooperativos.

## Vista previa del portapapeles [clipboard-preview]

![][Menú de vista previa del portapapeles]

Markdown (o texto sin formato compatible) en el portapapeles se abre con {% appmenu File, New, Clipboard Preview %} ({% kbd shift cmd V %}). Si el portapapeles contiene **HTML o RTF**, Marked lo convierte en una fuente similar a Markdown antes de la vista previa, incluida la detección aproximada de títulos cuando los párrafos RTF utilizan tamaños de fuente de hoja de estilo grandes.

## Vista previa de transmisión [streaming-preview]

Bear, Curio, Drafts, The Archive, nvALT, nvUltra y varios otros editores pueden insertar Markdown en Marked mientras escribe a través de **Vista previa de transmisión**. Consulte [Vista previa de transmisión](Streaming_Preview.html) para configuración y solución de problemas.

## Guiones y paquete de bonificación [scripts-and-bonus-pack]

Las automatizaciones para BBEdit, TextMate, DEVONthink, Emacs, Vim y más se envían con el [Paquete de bonificación marcado][bonificación]. Instale o adapte esos scripts cuando desee macros de barra de menú o editor más allá de las integraciones enumeradas anteriormente.


[appsettings]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane
[ClipboardPreviewMenu]: images/ClipboardPreviewMenu.jpg @2x width=600px height=198px class=center
[bonus]: https://github.com/kotfu/marked-bonus-pack