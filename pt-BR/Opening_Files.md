<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado oferece opções.

## Fluxo de trabalho de visualização ao vivo

1. Arraste um arquivo Markdown para Marcado (ou use {% appmenu File, Open... ({{cmd}}O) %}).
2. Edite o arquivo no editor de sua preferência.
3. Salvar --- Marcado atualiza a visualização automaticamente.

Consulte [Live Markdown Preview no Mac](Live_Markdown_Preview_on_Mac.html) para assistir ao vault, visualizar streaming e guias específicos do editor.

## Arraste para o ícone do Dock

A maneira mais fácil de usar Marcado em um arquivo que você já está editando é arrastar o ícone do documento da barra de ferramentas do seu editor ou do Finder para o ícone Marcado no Dock. Marcado começará imediatamente a rastrear qualquer arquivo Markdown (ou arquivo de texto) colocado nele. Você também pode arrastar arquivos diretamente do Finder.

## Usando o menu

![][2]

   [2]: images/file_open.jpg @2x largura=300px altura=118px class=centro

Você pode, é claro, abrir arquivos Markdown diretamente usando a opção de menu {% appmenu File, Open... ({{cmd}}O) %}. Marcado também funciona bem _sem_ um editor de texto. Você pode visualizar e converter seu Markdown com apenas um clique.

Marked também pode abrir arquivos **`.rtf` e `.rtfd`** diretamente (por exemplo, exportações de Pages ou TextEdit). Eles são convertidos em Markdown para visualização e atualização quando você salva no aplicativo original. Consulte [Suporte RTF e RTFD](RTF_Support.html) para obter detalhes, incluindo imagens e limitações.

Marcado pode abrir arquivos **`.pdf`** da mesma maneira: a conversão é executada em segundo plano e a visualização é atualizada quando concluída. Isso funciona melhor para PDFs mais curtos baseados em texto; manuais grandes e documentos digitalizados são mais lentos e menos precisos. Consulte [Suporte PDF](PDF_Support.html) para detalhes e limitações.

## Da área de transferência

Se você tiver texto compatível (por exemplo, Markdown) em sua área de transferência, poderá abrir uma visualização instantânea selecionando {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Se você copiou uma seleção de um navegador da web ou outro aplicativo que coloca HTML ou RTF na área de transferência, Marcado converte-a em Markdown para visualização. Quando você cola RTF de um aplicativo como TextEdit ou Pages, tamanhos de fonte maiores são aproximadamente convertidos em níveis de título (por exemplo, texto muito grande torna-se um título de nível 1, texto grande menor torna-se nível 2 e assim por diante). Você pode abrir várias visualizações da área de transferência ao mesmo tempo e salvá-las em um novo arquivo escolhendo {% appmenu File, Save Transient Preview %}.

## Criando um novo documento

Marcado permite que você crie um novo arquivo de texto vazio com o comando {% appmenu File, New ({{cmd}}N) %}. Ele solicitará imediatamente um local para salvar o arquivo, e você poderá ativar a opção "Editar novos arquivos automaticamente" em {% prefspane Apps %}, próximo ao botão Editor de texto para abrir automaticamente o arquivo recém-criado em seu editor padrão.

## Abrir recente

![][3]

   [3]: images/open_recent.jpg @2x largura=300px altura=174px class=centro

Marcado também mantém registro de documentos recentes. A opção de menu {% appmenu File, Open Recent %} mostrará os arquivos que você abriu e permitirá que você volte para eles. Você pode reabrir rapidamente o último arquivo que estava visualizando com {% kbd shift cmd R %}. Use {% kbd shift cmd P %} ou [Ações rápidas](Quick_Actions.html) para executar o menu e visualizar comandos do teclado. Se quiser aprendê-los, você pode encontrar um gráfico em [Atalhos de teclado](Keyboard_Shortcuts.html).

## Nova visualização no arquivo atual [multiview]

Use {% appmenu File, New View into Current File %} ({% kbd
shift cmd N %}, também no menu de contexto de visualização) para abrir um
segunda janela de visualização no mesmo arquivo salvo. Ambas as janelas
observe o arquivo no disco e atualize quando salvar em seu
editor, mas cada visualização mantém sua própria posição de rolagem,
marcadores, estilo de visualização e [regra personalizada
substituições](Custom_Processor.html#manuallyenabled).

**Exemplo de caso de uso:** Você está editando um manuscrito longo em
MultiMarkdown com seu estilo e processador habituais. Abra um
segunda visualização, mude para um estilo de revisão, fixe um Processo
regra que executa um processador integrado diferente e permite um
regra manual que destaca a marcação de revisão. Você compara
layouts de rascunho e prova lado a lado sem manter dois
cópias do arquivo.

Quando mais de uma visualização de um arquivo estiver aberta, o título da janela
inclui **Visualização 2**, **Visualização 3** e assim por diante para que você possa saber
janelas separadas no menu Janela e no Controle da Missão.

Visualizações alternativas não estão disponíveis para documentos não salvos,
visualizações da área de transferência, visualizações de streaming ou baseadas em pastas
projetos que não são mapeados para um único arquivo no disco.

## Abertura rápida ##

Você pode alternar rapidamente entre documentos abertos, abrir documentos recentes ou abrir a caixa de diálogo Arquivo->Abrir com o [Painel de abertura rápida](Quick_Open.html) ({% kbd cmd shift o %}).