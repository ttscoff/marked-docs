# <%= @title %>

O [Traverse][traverse] inclui o comando **Stream to Marked**. Ele aparece no menu de exportação quando o Marked 2 ou o Marked 3 está instalado.

## Stream to Marked [stream-to-marked]

Abra o menu de exportação (o botão com uma seta para cima) e escolha **Stream to Marked**.

![Stream to Marked no menu de exportação do Traverse][stream]

O que o Traverse envia depende do esboço:

- Se você adicionou o atributo **Type**, o Traverse envia o mesmo Markdown usado na exportação Markdown.
- Se o formato no Traverse estiver definido como **[Fountain](Fountain_for_Screenwriters.html)**, a visualização ativa automaticamente o tratamento de Fountain. O Traverse começa o texto enviado com `<!--format:fountain-->`, e é esse comentário que ativa o tratamento. Veja [Streaming Preview](Streaming_Preview.html).
- Se nenhum dos dois estiver selecionado, o Traverse envia uma lista Markdown simples.

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
