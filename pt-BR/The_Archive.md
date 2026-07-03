<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[O Arquivo][arquivo] mantém suas notas como arquivos em disco e pode espelhar a nota que você está editando diretamente no canal **visualização de streaming** do Marked.

## Visualização do stream para marcado

1. Em Marcado, abra {% appmenu File, New, Streaming Preview %} (ou reutilize uma janela de visualização de streaming existente).
2. Mude para The Archive e escolha **Note → Stream Preview to Marked** para que The Archive ative Marked e comece a enviar o texto da nota mais inicial.

Atualizações marcadas conforme você digita no The Archive, seguindo o mesmo contrato da área de transferência `mkStreamingPreview` de outros aplicativos integrados — consulte [Detalhes técnicos](Streaming_Preview.html#developers) em [Visualização de streaming](Streaming_Preview.html).

Se as visualizações parecerem desatualizadas, confirme se a janela de streaming ainda está na frente em Marcado e alterne o comando do menu Arquivar uma vez.

[archive]: https://www.zettelkasten.de/the-archive/