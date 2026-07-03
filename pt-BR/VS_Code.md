<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Visual Studio Code][vscode] não inclui Marked pronto para uso, mas você pode usar uma extensão da comunidade para **visualização ao vivo do Markdown** em Marked --- visualização, exportação e revisão enquanto continua escrevendo no VS Code.

## Início rápido

1. Instale uma extensão VS Code **Open in Marked** (consulte [Open in Marked extension][ext] abaixo).
2. Abra seu arquivo Markdown no VS Code.
3. Envie o arquivo para Marcado --- a visualização é atualizada quando você salva.

## Abrir na extensão marcada

A [extensão Abrir em Marcado][ext] (Visual Studio Marketplace) adiciona uma ação **Abrir em Marcado**: botão de título do editor, **{% kbd shift cmd m %}**, menus de contexto no editor e no explorador de arquivos, **pasta aberta** opcional para o navegador de arquivos do Marcado, um indicador de barra de status e salvamento automático opcional antes de abrir. As configurações permitem definir o caminho para o aplicativo marcado, caso ele não esteja no local padrão.

I> A extensão foi publicada originalmente para Marcado 2. Marcado 3 usa o mesmo estilo de transferência de arquivo e URL, portanto, essa integração continua funcionando; se alguma coisa mudar, verifique a [página de extensão][ext] ou o repositório do autor para atualizações.

## Requisitos

Marcado é executado apenas no macOS. Instale [Marked 3][marked] e a extensão e aponte **caminho do aplicativo** para seu aplicativo marcado, se necessário.

[ext]: https://marketplace.visualstudio.com/items?itemName=vikgamov.vscode-open-in-marked2
[marked]: https://markedapp.com/
[vscode]: https://code.visualstudio.com/