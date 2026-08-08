<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

{% apponly div %}
*Para obter a versão mais recente desta documentação, visite a [versão online][ajuda].*
{% endapponly %}

**Não deixe de conferir a crescente coleção de [Vídeos tutoriais marcados](https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ).**

## O que é Markdown? [whats-markdown]

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

Markdown é uma linguagem de marcação básica que usa símbolos simples, permitindo escrever HTML (e exportar para outros formatos) com sintaxe simples como `*italics*` e `**bold**`. Markdown foi criado por John Gruber e está rapidamente se tornando o padrão para publicação na web, anotações e até publicação de livros. Ele permite que você escreva sem um monte de barras de ferramentas e sem mexer na formatação, apenas colocando palavras na página e deixando seus processadores (como Marcado) lidarem com o estilo e a formatação.

Marked funciona com GitHub Flavored Markdown, CommonMark (GFM), Kramdown e MultiMarkdown e pode converter sintaxe de diversas variantes para visualização (também pode ser estendido para funcionar com praticamente qualquer processador que você precisar, incluindo Textile, reStructuredText, Wikitext e mais). Presumo que --- já que você está aqui --- você sabe o que é pelo menos uma dessas linguagens de marcação. Caso contrário, você deve começar com [Markdown Basics][daringfireball] de John Gruber, confira [MarkdownGuide.org][mdguide]. Marcado inclui um guia completo de sintaxe do Markdown no menu de ajuda.

Você pode usar o [Markdown Dingus](x-marked-3://dingus) para experimentar os diferentes sabores de Markdown que o Marked suporta.

## O que está marcado? [whats-marked]

Marked é um aplicativo de visualização Markdown ao vivo para macOS --- um aplicativo independente de editor (Multi) Markdown Preview que observa alterações em um arquivo, atualizando a visualização sempre que você salva. Ao separar e automatizar os detalhes da formatação, você pode se concentrar mais na escrita e menos na apresentação, ao mesmo tempo em que mantém o controle sobre o produto final.

Para fluxos de trabalho de configuração e inícios rápidos específicos do editor, consulte [Live Markdown Preview no Mac](Live_Markdown_Preview_on_Mac.html). Para uma visão geral mais curta do produto, visite [markedapp.com/markdown-preview](https://markedapp.com/markdown-preview/).

Marcado funciona com qualquer arquivo acessível localmente, incluindo documentos do iCloud. Basta arrastar um documento de texto da barra de ferramentas de qualquer editor para Marcado e ele será renderizado como uma visualização HTML e começará a rastrear as alterações, atualizando a visualização conforme você escreve. Ele pode até compilar [documentos de vários arquivos](Multi-File_Documents.html) usando uma sintaxe básica de "inclusão" ou dos formatos de índice Scrivener, Leanpub e mmd_merge.

Marcado possui recursos adicionais, incluindo contagem de palavras e outras estatísticas de documentos, a capacidade de flutuar acima de outros aplicativos ou escurecer em segundo plano, e pode exibir seu trabalho em uma variedade de estilos bem elaborados. Ele pode imprimir documentos em PDF ou Word, documentos HTML completos (incluindo estilos e imagens) ou copiar fontes HTML ou dados RTF para sua área de transferência com um toque de tecla. Marked também possui um dicionário AppleScript básico e um [manipulador de URL](URL_Handler.html) que facilitam a integração ao seu fluxo de trabalho.

Ah, sim, e funciona com vários de seus aplicativos favoritos: editores de texto que vão de Vim e Emacs a Sublime Text e TextMate, editores Markdown como MultiMarkdown Composer, Byword e iA Writer, até mesmo aplicativos que você não espera, como Ulysses, Scrivener, VoodooPad, MarsEdit e muito mais.

## Exemplo de uso [example-uses]

Marcado transforma qualquer editor de texto em um editor habilitado para Markdown. Sua visualização está sempre disponível e é atualizada conforme você trabalha.

* Se o seu editor favorito não oferece uma visualização ao vivo do Markdown, abra o documento em que você está trabalhando no Marked e mova a janela para o lado para obter uma experiência de escrita Markdown completa.
* Você gosta de escrever ou blogar no MacVim ou outro editor baseado em terminal? Agora você tem uma visualização sincronizada do Markdown enquanto trabalha.
* Marcado também oferece recursos de exibição acima e além de qualquer visualização existente do Markdown e pode ser usado para fornecer contagem completa de palavras e estatísticas do documento, sugestões de redação e até mesmo destacar erros na formatação do Markdown.
* Você também pode usar Marcado sem editor. Basta arrastar os arquivos Markdown até o ícone para visualizá-los, imprimi-los e exportá-los para código-fonte PDF, DOC, RTF ou HTML. Marcado também pode **abrir arquivos `.rtf` e `.rtfd`** como documentos de origem ([Suporte RTF e RTFD](RTF_Support.html)).
* Em aplicativos com salvamento automático, você descobrirá que a visualização acompanha sua escrita sem qualquer ajuda. Use-o com qualquer editor... ou *todos* os seus editores.
* Escrevendo um livro? Marcado pode compilar vários arquivos para uma visualização completa do seu trabalho e até mesmo observar se há alterações nos arquivos incluídos, atualizando o documento principal a cada salvamento. Ele pode até monitorar alterações em uma pasta inteira, alternando automaticamente a visualização para qualquer arquivo que você esteja atualizando no momento. Quando estiver pronto, você poderá publicar nos formatos EPUB, DOCX ou TextBundle.
* Trabalhando com uma plataforma de codificação de IA? Abra um plano ou pasta de documentação no Marked e sempre que um arquivo Markdown nessa pasta for alterado, o Marked irá exibi-lo, rolando automaticamente até o ponto da edição mais recente. Marcado exibe diagramas Mermaid e pode lidar com todos os tipos de sintaxe estendida. Acompanhe os planos e a documentação enquanto trabalha, sem alternar entre arquivos.