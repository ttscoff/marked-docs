<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[vim-marked][vimrepo] é um plugin do Vim que abre o buffer Markdown atual em Marked. Adiciona `:MarkedOpen`, `:MarkedQuit`, `:MarkedToggle` e `:MarkedPreview` para que você possa enviar o arquivo (ou um intervalo) para Marcado sem sair do editor.

## Configuração [setup]

Instale com seu gerenciador de plugins; veja o [README do projeto][vimrepo] para `vim-plug` e outras opções. O padrão `g:marked_filetypes` inclui `markdown` e variantes comuns; estenda a lista se você usar um `filetype` personalizado.

## macOS e nome do aplicativo [macos-and-app-name]

Marcado como somente macOS, portanto o plugin não carrega em outros sistemas. O nome do aplicativo padrão é **Marcado 2**; se sua cópia do Marked estiver instalada com um nome ou caminho diferente, defina `g:marked_app` para corresponder (por exemplo, um caminho completo para o pacote de aplicativos). O README cobre encerramentos, encerramento automático e comportamento de foco.

I> Este tópico de ajuda não faz parte do projeto marcado pelo vim; para obter os comandos e opções mais recentes, use o [repositório GitHub] [vimrepo].


[vimrepo]: https://github.com/itspriddle/vim-marked