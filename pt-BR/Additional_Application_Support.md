<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked funciona com muitos editores e aplicativos de escrita. Esta página aborda **configurações** compartilhadas, **visualização da área de transferência**, ponteiros para **visualização de streaming** e recursos de script. Guias detalhados para aplicativos populares estão em seus próprios tópicos de ajuda (consulte a seção **Aplicativos compatíveis** na barra lateral).

## Guias por aplicativo [per-app-guides]

Comece com [Live Markdown Preview no Mac](Live_Markdown_Preview_on_Mac.html) para o fluxo de trabalho geral. Se você usa Obsidian, consulte [Visualização de Marcado vs Obsidian](Marked_vs_Obsidian_Preview.html) para decidir quando Marcado agrega valor junto com a visualização integrada do Obsidian.

| Tópico | Página de ajuda |
| :-- | :-- |
| **Urso** | [Urso](Bear.html) |
| **Curio** (visualização da transmissão) | [Curiosidade](Curio.html) |
| **Rascunhos** (visualização de streaming + ações) | [Rascunhos](Drafts.html) |
| **DEVONthink** (Integração do menu de script) | [DEVONthink](DEVONthink.html) |
| **Visualização de pastas** (nvALT, nvUltra, etc.) | [Assistindo Pastas](Folder_Watching.html) |
| **Montanhas** | [Montanhas](Highland.html) |
| **Marcador** Resolução de URL | [Marcador](Hookmark.html) |
| **Eu sou um escritor** | [Escritor iA](iA_Writer.html) |
| **iThoughtsX** `.itmz` mapas | [iPensamentosX](iThoughtsX.html) |
| **MarsEdit** visualização ao vivo | [MarteEditar](MarsEdit.html) |
| **MindNode** | [MindNode](MindNode.html) |
| **Compositor MultiMarkdown** | [Compositor MultiMarkdown](MultiMarkdown_Composer.html) |
| **nvUltra** | [nvUltra](nvUltra.html) |
| **Obsidian** abóbadas e legendas | [Obsidiana](Obsidian.html) |
| **OmniOutliner/OPML** | [OmniOutliner e OPML](OmniOutliner_and_OPML.html) |
| **RTF/RTFD** (Páginas, TextEdit, etc.) | [Suporte RTF e RTFD](RTF_Support.html) |
| **PDF** | [Suporte para PDF](PDF_Support.html) |
| **Escrivão 3** | [Suporte ao Scrivener 3](Scrivener_Support.html) |
| **O Arquivo** visualização de streaming | [O Arquivo](The_Archive.html) |
| **Ulisses** fluxo de trabalho de exportação | [Ulisses](Ulysses.html) |
| **Vim** (plugin marcado com vim) | [Vim](Vim.html) |
| **Código VS** (Abrir em extensão marcada) | [Código VS](VS_Code.html) |
| **VoodooPad** | [VoodooPad](VoodooPad.html) |
| **Parques Xcode** | [Parques Xcode](Xcode_Playgrounds.html) |

## Configurações do aplicativo [application-settings]

I> Várias integrações expõem alternâncias dentro de {% prefspane Apps %} e {% prefspane Preview %}.

![Configurações do aplicativo][appsettings]

Use esses painéis para padrões de link wiki, transferência do Scrivener, configurações de área de transferência transmitida, opções de incorporação de mapa mental para OPML/OmniOutliner, integrações Obsidian ou outros processadores que dependem de editores cooperativos.

## Visualização da área de transferência [clipboard-preview]

![][Menu de visualização da área de transferência]

Markdown (ou texto simples compatível) na área de transferência abre com {% appmenu File, New, Clipboard Preview %} ({% kbd shift cmd V %}). Se a área de transferência contiver **HTML ou RTF**, o Marked o converterá em uma fonte semelhante ao Markdown antes da visualização, incluindo detecção aproximada de cabeçalho quando parágrafos RTF usam tamanhos de fonte de folha de estilo grandes.

## Visualização de streaming [streaming-preview]

Bear, Curio, Drafts, The Archive, nvALT, nvUltra e vários outros editores podem enviar Markdown para Marked enquanto você digita via **Streaming Preview**. Consulte [Visualização de streaming](Streaming_Preview.html) para configuração e solução de problemas.

## Scripts e pacote de bônus [scripts-and-bonus-pack]

Automações para BBEdit, TextMate, DEVONthink, Emacs, Vim e muito mais são fornecidas com o [Marked Bonus Pack][bonus]. Instale ou adapte esses scripts quando desejar macros da barra de menu ou do editor além das integrações listadas acima.


[appsettings]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane
[ClipboardPreviewMenu]: images/ClipboardPreviewMenu.jpg @2x width=600px height=198px class=center
[bonus]: https://github.com/kotfu/marked-bonus-pack