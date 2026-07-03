<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Arraste um documento [MindNode][mn] para Marked (ou use o comando **Open in Marked** / preview do MindNode, dependendo da versão do MindNode). Marked trata o arquivo como a exportação Markdown do MindNode, de modo que a hierarquia do seu mapa se torna títulos e listas na visualização.

## Visualização de streaming (MindNode 2026.3+)

I> **MindNode 2026.3** e mais recente adiciona Marcado [visualização de streaming](Streaming_Preview.html). No MindNode, escolha **Visualizar → Visualizar em Marcado** para abri-lo; a visualização é atualizada conforme você altera o mapa.

## MindNode Clássico versus MindNode 7+

W> A integração atual tem como alvo os pacotes **MindNode Classic**. As versões mais recentes do MindNode usam um formato de pacote diferente; se a abertura de um mapa falhar ou Marcado mostrar uma planilha **"Por favor, abra no MindNode"**, prepare o mapa no menu **Avançado** do MindNode (geralmente **Abrir em outro aplicativo** / Marcado) ou exporte um pacote compatível, em vez de arrastar um pacote `.mindnode` bruto que não foi preparado para visualização.

Como o arquivo é preparado pelo MindNode antes de Marked lê-lo, sempre salve no MindNode antes de esperar uma atualização no Marked.

[mn]: https://mindnode.com/
[mn-beta]: https://testflight.apple.com/join/jSvVBpnt