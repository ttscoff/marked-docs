<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Flexibilidade é fundamental.

## Menu de engrenagem

![][4]

   [4]: images/gearmenu.jpg @2x largura=740px altura=235px class=centro

O menu Gear oferece a maioria dos recursos encontrados na barra de menus, além de algumas funções específicas de visualização. Basta clicar na engrenagem no canto inferior direito da janela para acessar essas funções.

## Mantenha-se no topo

![][5]

   [5]: images/KeepOnTopPin.jpg @2x largura=740px altura=345px class=centro

O ícone de cadeado no canto inferior esquerdo trará a janela de visualização para a frente e a manterá lá (flutuará) ao alternar para outros aplicativos. Você pode definir uma transparência na janela em {% prefspane General %} que permitirá que a janela desapareça ao usar outros aplicativos.

Este recurso também pode ser alternado com {% kbd shift-opt-cmd-f %}.

## Padrões de nível de janela

No {% prefspane General %} você pode usar "Manter novas janelas no topo" para definir novas janelas para sempre permanecerem acima de outras janelas e/ou definir janelas para subirem ao topo quando o documento associado for atualizado. As janelas configuradas para serem atualizadas não "roubarão o foco" do seu editor, elas apenas ficarão visíveis sem se tornarem ativas.

## Ver fonte

![][6]

   [6]: images/view_source.jpg @2x largura=740px altura=345px class=centro

Você pode alternar entre visualizações de visualização e código-fonte com o botão no canto superior direito. Esta visualização também pode ser alternada com U.

## Pesquisa

![][7]

   [7]: images/SearchBarFull.jpg @2x largura=818px altura=195px class=centro

A barra de localização pode ser acessada com {% kbd cmd F %} e permite que você pesquise uma palavra ou frase na visualização. Depois de pesquisar, você pode usar {% kbd cmd G %} e {% kbd shift cmd G %} para navegar para frente e para trás em resultados adicionais.

As caixas de seleção no lado direito da barra de pesquisa permitem restringir a pesquisa por distinção entre maiúsculas e minúsculas, apenas palavras inteiras e expressões regulares. Além da pesquisa por expressão regular, as pesquisas curinga (*?) sempre funcionam, mesmo quando a opção regex está desativada.

Você também pode colocar um termo ou frase de pesquisa entre barras para interpretá-lo como uma expressão regular automaticamente (por exemplo, '/term.+?\b/').


Use o recurso de pesquisa em combinação com os favoritos para salvar os locais à medida que os encontra. Pressione Tab ({% kbd ⇥ %}) para focar o documento e digite Shift-[1-9] para definir um marcador nesse número. Você pode voltar ao marcador apenas digitando o número (sem a tecla Shift) ou usando n/p para navegar por eles na ordem do documento. N/P navegará em ordem numérica. Para marcadores, índice, minimapa e pesquisa rápida de cabeçalho, consulte [Navegação no documento](Document_Navigation.html). Consulte a seção [Navegação de visualização](Keyboard_Shortcuts.html#previewnavigation) para obter mais opções ou digite "?" a qualquer momento na visualização.

> **Observação:** A pesquisa não pode ser quebrada entre elementos, o que significa que uma string de pesquisa não pode continuar entre um parágrafo e um título, entre itens de lista, etc.

Você pode alternar as caixas de seleção "Palavras inteiras", "Diferencia maiúsculas de minúsculas" e "Regex" usando {% kbd ctrl shift 1 %}, {% kbd 2 %} e {% kbd 3 %}, respectivamente.

### Pesquisa avançada ###

Você pode usar curingas em uma pesquisa não regex. `*` corresponderá a qualquer série de caracteres que não sejam espaços e `?` corresponderá a qualquer caractere único.

Iniciar uma pesquisa com `*` tornará a pesquisa no seletor jQuery. Você pode usar qualquer seletor jQuery e todos os elementos correspondentes serão destacados e navegáveis ​​com {% kbd cmd G %} e {% kbd shift cmd G %}. Para limitar o escopo de uma pesquisa de texto a um determinado tipo de elemento, adicione os termos de pesquisa entre aspas duplas após a definição do seletor:

    *h2 "Alice"

Isso é equivalente a `*h2:contains(Alice)`

## Navegação de documentos (TOC, favoritos, Minimapa)

A página [Navegação no Documento](Document_Navigation.html) cobre o Índice (incluindo a abertura do filtro com {% kbd Space %}), pesquisa rápida com {% kbd f %}, marcadores e o Minimapa.

## Navegação pelo teclado

A janela de visualização pode ser navegada rapidamente usando atalhos de teclado. Use {% kbd j %} e {% kbd k %} para mover para cima e para baixo e mantenha pressionada a tecla Shift ({% kbd J %}/{% kbd K %}) para mover mais rápido. {% kbd t %} e {% kbd b %} serão movidos para a parte superior e inferior do documento (assim como {% kbd gg %} e {% kbd G %}, para fãs do Vim). {% kbd u %} e {% kbd d %} moverão meia página para cima e para baixo.

### Salto de cabeçalho

Pressionar as teclas vírgula ({% kbd , %}) e ponto final ({% kbd . %}) irá retroceder e avançar em qualquer cabeçalho do documento. Manter pressionada a tecla Shift ({% kbd shift  %}) saltará apenas entre os cabeçalhos de nível 1 e 2.


## Tela inteira

O modo de tela inteira pode ser alternado no menu Visualização ou digitando {% kbd ctrl cmd F %}.

## Clicando em links externos

![][10]

[10]: images/linkpopover.png @2x width=706px height=213px class=center

Clicar em um link externo na visualização do seu documento irá abri-lo no seu navegador padrão. Se você clicar e segurar, ao soltar Marcado você terá três opções: você pode copiar o URL do link para a área de transferência, validar o link ou abrir o link em seu navegador padrão. Basta clicar em qualquer lugar da visualização para fechar a janela. Este recurso pode ser desativado em {% prefspane Preview %} ("Ativar popovers de link").

Veja um [vídeo de visão geral no YouTube](https://www.youtube.com/watch?v=nrt7YZPrnv0&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=1).

## Títulos recolhíveis ##

Quando "Recolher seções de títulos" estiver ativado em {% prefspane Preview %}, clicar nos títulos recolherá a seção entre esse título e o próximo título no mesmo nível. As subseções dessa seção ficam ocultas. Opcionalmente, você pode limitar esse comportamento a {% kbd cmd %} cliques.

![][13]

[13]: images/headlines.jpg @2x width=740px height=287px class=center

Manter {% kbd opt  %} pressionado ao clicar (ou clicar com {% kbd cmd %}) irá expandir/recolher todas as seções secundárias abaixo do título clicado. Manter pressionada a tecla {% kbd shift  %} (Shift) enquanto clica irá recolher todas as outras seções no mesmo nível, revelando apenas a seção clicada.

As seções recolhidas são marcadas com um destaque amarelo à direita do título e o cursor indicará o que acontecerá quando o item for clicado.

Se for feita uma edição que precisa estar visível, ou se clicar em uma seção do índice que está atualmente dentro de uma seção recolhida, as seções pai necessárias serão expandidas para revelá-la.

Você pode recolher/expandir todas as seções de um documento de uma vez com "Recolher todas as seções" ({% kbd opt cmd left  %}) e "Expandir todas as seções" ({% kbd opt cmd right  %}).

Veja o [vídeo Navegação de documentos no YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2) para obter mais detalhes.

## Indicadores/alternâncias personalizadas do processador ##

![][indicadores]

[indicators]: images/processorindicators.png @2x width=874px height=255px class=center

Quando o processador e/ou pré-processador personalizado está ativado, luzes indicadoras aparecem na barra de ferramentas. Eles podem ser usados ​​para ver se o processador está ou não ativado para o documento atual (o indicador será destacado) e clicar neles alternará o uso do pré-processador e do processador personalizados, respectivamente.

## Role para editar

O recurso “rolar para editar” no Marked monitora as diferenças entre a atualização mais recente e a última, tentando encontrar o ponto onde você fez as alterações mais recentes. Marcado sempre rastreia isso e uma pequena linha vermelha aparece na visualização para mostrar a localização da primeira alteração detectada. No {% prefspane Preview %}, você pode ativar "Rolar para a primeira edição" e quando uma visualização for atualizada, ela rolará suavemente a visualização para esse local.

Com a opção "Rolar para a primeira edição" desativada, você ainda pode pressionar a tecla "e" a qualquer momento na visualização para ir para o último ponto de edição armazenado.

## Rolagem automática

Veja a página dedicada [Autoscroll](Autoscroll.html). Ao usar Autoscroll como teleprompter, [sintaxe especial pode inserir pausas](Special_Syntax.html#pauses).

## Visão geral do zoom

Consulte a página [Visão geral do zoom](Zoom_Overview.html) ({% kbd z %} na visualização; também funciona em repetição de palavras com {% kbd ctrl cmd w %}).

## Referência de redução

![][11]

   [11]: images/markdown_reference.jpg @2x largura=1148px altura=267px class=centro

Selecione Markdown Reference no menu {% appmenu Help %} para exibir um guia que flutua sobre as outras janelas. Isso é útil para quem ainda está aprendendo a sintaxe do Markdown. Você pode abrir este painel através do teclado usando {% kbd opt cmd M %}.

## Atalhos de teclado globais

No {% prefspane General %}, você pode designar um atalho de teclado personalizado para ativar Marcado e um para elevar apenas a janela frontal para o topo sem sair do editor.