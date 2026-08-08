<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Bear][bear] pode enviar uma prévia ao vivo direto para Marked.

## Enviando do Urso [sending-from-bear]

No Bear, escolha **Visualizar em Marcado** no menu **Visualizar** (o texto pode variar ligeiramente de acordo com a versão do Bear). Marked recebe um TextBundle, portanto, imagens e ativos incorporados geralmente acompanham o texto.

Imagens referenciadas com caminhos absolutos ou URLs `https` também são resolvidas, desde que Marcadas possam alcançá-las.

## Nota da Mac App Store [mac-app-store-note]

Se você usa a versão **Mac App Store** do Marked e o macOS continua pedindo permissão para abrir diretórios durante a visualização do Bear, [entre em contato com o suporte do Marked](http://support.markedapp.com) para obter uma classificação cruzada gratuita para a edição de download direto, o que evita esse atrito específico da sandbox.

## Tags [tags]

Tags estilo urso podem ser renderizadas como tal ativando **#Text is tag** e **Style tags** em {% prefspane Processor %}.

W> Esta configuração pode confundir Marcado se você escrever títulos regulares sem espaços após `#`.

## Nomes de arquivos e exportação [filenames-and-export]

Se você ativar **Usar primeiro H1 como título alternativo** em {% prefspane Export %}, esse título poderá direcionar o nome do arquivo e o espaço reservado `%title` quando você imprimir ou exportar PDFs de Marcado.

I> Um estilo de visualização que se aproxima da aparência do Bear [está disponível emmarkedapp.com/styles](https://markedapp.com/styles/preview?style=bear).

A visualização de streaming do Bear está resumida na página [Visualização de streaming](Streaming_Preview.html) e em [Integrações adicionais de aplicativos](Additional_Application_Support.html).

[bear]: https://bear.app/