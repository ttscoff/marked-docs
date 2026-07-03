<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[MarsEdit][me] armazena postagens dentro de seu banco de dados, não como arquivos soltos em disco. Portanto, o Marked usa um fluxo de trabalho de visualização dedicado que se comunica com o aplicativo MarsEdit em execução.

## Janela de visualização do MarsEdit

Escolha {% appmenu File, New, MarsEdit Preview %}. Marked pede ao AppleScript para ler a **postagem inicial no MarsEdit** (os IDs do pacote Red Sweater para Direct, Mac App Store, Setapp e MarsEdit 4/5 são reconhecidos). Mantenha o MarsEdit funcionando com um documento aberto enquanto você trabalha.

- **Atualização manual:** salve na visualização do Marked se quiser forçar uma atualização.
- **Atualizações automáticas:** habilite a visualização para que cada salvamento automático do MarsEdit seja atualizado marcado.

Se nenhuma postagem estiver disponível, Marcado apresenta um pequeno erro na visualização em vez de texto obsoleto.

### Postagens estendidas

O conteúdo no campo **estendido** do MarsEdit é separado na visualização e na fonte do Marked usando um divisor `<!--more-->` no estilo WordPress para que sites orientados à paginação (WordPress, Jekyll, etc.) ainda vejam a quebra. O comentário é inofensivo em outro lugar.

### Tags e categorias em metadados

As tags e categorias do MarsEdit são expostas ao bloco de metadados MultiMarkdown. Com o processador MultiMarkdown ({% prefspane Processor %}), você pode referenciá-los como:

    Marcado: [%tags]
    Publicado em: [%categorias]

[me]: https://www.red-sweater.com/marsedit/