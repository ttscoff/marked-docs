<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Rascunhos][rascunhos] no Mac podem espelhar o rascunho ativo em Marcado usando **Visualização de streaming marcada** — o mesmo canal baseado na área de transferência descrito em [Visualização de streaming](Streaming_Preview.html). Você também pode enviar o rascunho atual uma vez com uma **ação** da comunidade (sem atualizações ao vivo até que você o execute novamente).

## Visualização de streaming (Rascunhos para Mac) [streaming-preview-drafts-for-mac]

1. Em Marcado, escolha {% appmenu File, New, Streaming Preview %} para que uma janela de visualização de streaming esteja pronta.
2. Em **Rascunhos para Mac**, abra **Configurações** e ative **Ativar suporte para visualização de streaming de aplicativos marcados**.
3. Use **Abrir Marcado** se Rascunhos oferecer a opção de trazer Marcado para frente e depois editar em Rascunhos; a visualização é atualizada conforme seu rascunho muda.

![][rascunhosprefs]

Quando esta opção está ativada, Rascunhos envia Markdown para Marcado por meio da integração Marcada expõe para visualizações de streaming (em vez de depender da visualização de um arquivo no disco).

### Seja marcado [get-marked]

Se **Get Marked App** aparecer na folha de configurações de Rascunhos, use-o quando o Marked ainda não estiver instalado.

## Visualização em ação marcada (atualização manual) [preview-in-marked-action-manual-refresh]

Instale a ação da comunidade [**Visualizar em Marcado**](https://actions.getdrafts.com/a/11f) do Diretório de Rascunhos. Ele envia o **rascunho de texto atual** para Marcado usando uma URL `x-marked://preview?text=…` (Rascunhos substitui o conteúdo do rascunho). **O conteúdo não é atualizado ao vivo**: execute a ação novamente sempre que desejar que Marcado corresponda ao rascunho.

Essa abordagem é útil para verificações ocasionais, enquanto a **visualização de streaming** é adequada para sessões de gravação contínuas.

Os rascunhos também funcionam no iPhone e no iPad; a integração de visualização de streaming documentada aqui se aplica a **Rascunhos para Mac** com Marcado no mesmo Mac.

[draftsprefs]: images/Drafts_streaming_preview_preference.png width=842px height=182px class=center

[drafts]: https://getdrafts.com/