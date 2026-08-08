<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado inclui extensões de navegador que permitem enviar URLs de páginas ou conteúdo selecionado diretamente para Marcado 3.

## Instalar [install]

Baixe e instale em [https://markedapp.com/extensions](https://markedapp.com/extensions):

- Firefox/Zen
- Cromo / Bravo / Borda
- Safari (pacote)

## Como funciona a extensão [how-the-extension-works]

Quando você clica em um botão de extensão, ele abre um URL personalizado tratado pelo Marcado 3 usando o esquema `x-marked-3://markdownify`.

### `Markdownify URL` [markdownify-url]

No pop-up da extensão, clique em **`Markdownify URL`** para enviar o URL da página atual para Marcado.

### `Markdownify Selection` [markdownify-selection]

No pop-up da extensão, clique em **`Markdownify Selection`** quando tiver uma seleção na página.

Marked recebe o HTML da seleção atual e o converte em Markdown.

### Selecionar seção (modo de seleção de bloco) [select-section-block-selection-mode]

![][1]

[1]: images/marked-3-chrome-1.jpg width=1280px height=800px class=center

Clique em **Selecionar seção** para entrar no “modo de seleção de seção”:

- Passe o mouse sobre a página para destacar os elementos do bloco que você pode selecionar.
- Clique em um bloco para enviá-lo imediatamente para Marcado (envio único).
- Clique com a tecla Cmd nos blocos para selecionar vários blocos (clique com a tecla Cmd novamente para remover um bloco).
- Pressione Return para enviar os blocos atualmente selecionados.
- Pressione Esc para cancelar o modo de seleção de seção.

Ao selecionar, o pop-up também fornece controles de zoom para ajudá-lo a clicar em seções pequenas ou densas:

![][2]

[2]: images/marked-3-chrome-2.jpg width=1280px height=800px class=center

- `-` diminui o zoom
- **Ajustar altura** amplia para que a página se ajuste à altura da janela de visualização
- `+` aumenta o zoom