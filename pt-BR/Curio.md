<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Curio][curio] é um aplicativo visual de brainstorming e anotações que pode transmitir o item que você está editando no canal **visualização de streaming** do Marked.

## Fluxo selecionado para marcado [stream-selected-to-marked]

1. Em Marcado, escolha {% appmenu File, New, Streaming Preview %} para que uma janela de visualização de streaming esteja pronta.
2. No Curio, ative **Visualizar → Transmissão selecionada para marcada**.

Quando você clica duas vezes para editar uma figura, nota, lista ou outro item no Curio, seu Markdown flui para a visualização de streaming e é atualizado conforme você escreve.

Atualizações marcadas quase em tempo real, seguindo o mesmo contrato de área de transferência `mkStreamingPreview` de outros aplicativos integrados — consulte [Detalhes técnicos](Streaming_Preview.html#developers) em [Visualização de streaming](Streaming_Preview.html).

Se as visualizações pararem de ser atualizadas, confirme se uma janela de visualização de streaming está aberta em Marcado e alterne **Stream selecionado para Marcado** uma vez no Curio.

[curio]: https://www.zengobi.com/products/curio/