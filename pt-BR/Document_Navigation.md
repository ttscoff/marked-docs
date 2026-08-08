<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Esta página descreve como navegar pelas visualizações longas: o [Índice](#índice), [pesquisa rápida](#pesquisa rápida), [marcadores](#marcadores-e-minimapa) e o [Minimapa](#minimapa). Para atalhos de rolagem que se aplicam a todos os lugares (como {% kbd j %}/{% kbd k %}), consulte [Navegação pelo teclado](Interface_Features.html#keyboardnavigation) em [Recursos de interface](Interface_Features.html).

## Índice [table-of-contents]

![][8]

   [8]: images/tableofcontentsbutton.jpg @2x width=740px height=238px class=center

Se o seu documento contiver cabeçalhos, um botão de lista aparecerá na barra de ferramentas. Clique nele para expandir o Índice; clique em um título para ir para essa seção da visualização. Use {% kbd j %}/{% kbd k %} (para baixo/para cima) para percorrer a lista e {% kbd Enter %} ou {% kbd o %} para pular para o cabeçalho destacado.

**Barra de filtro:** Com o Índice aberto, pressione {% kbd Space %} (barra de espaço) para abrir o campo de digitação antecipada. Digite qualquer parte do nome de um título (Marcado usa correspondência no estilo TextMate - por exemplo, você pode digitar a primeira letra de cada palavra) e pressione Tab ({% kbd ⇥ %}) ou a seta para baixo ({% kbd ↓ %}) para percorrer a lista filtrada.

Pressionar {% kbd cmd T %} também abre (ou fecha) o Índice.

Se ["Títulos Recolher Seções"](Interface_Features.html#collapsibleheadlines) estiver ativado em {% prefspane General %}, segurar a tecla Command enquanto clica em um item no Índice irá recolher ou expandir essa seção, revelando as seções principais conforme necessário.

No modo de tela inteira, o índice aparece como uma barra lateral fixa em vez de um menu pop-up. Para usar esse layout em uma visualização em janela normal, use o botão de alternância de tela inteira no canto inferior direito do painel TOC.

![Alternar tela cheia][12]

   [12]: images/tableofcontentsfullscreentoggle.jpg @2x width=740px height=238px class=center


Para obter uma lista condensada de teclas, consulte [Atalhos de teclado](Keyboard_Shortcuts.html#TableofContentsNavigation).

Veja também o [vídeo Navegação de documentos no YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Modo de tela inteira para o Índice [full-screen-mode-for-the-table-of-contents]

Quando uma janela de visualização marcada está em tela cheia, o Índice pode permanecer fixo à esquerda para navegação constante. Ainda alterna com {% kbd cmd T %}; clicar fora do sumário geralmente não o descartará neste layout.

Em uma janela normal, clique no ícone na parte inferior do painel TOC para encaixá-lo como barra lateral; clique no ícone na parte superior da barra lateral para retornar ao modo pop-up.

### Personalizando onde o sumário aparece [customizing-where-the-toc-appears]

O Índice pode ser injetado no documento exportado usando a [sintaxe especial](Special_Syntax.html#tableofcontents) `<!--TOC-->`.

Adicione `max#` (por exemplo `<!--TOC max2-->`) para limitar quantos níveis de título aparecem.

## Pesquisa rápida [fast-search]

**Navegação rápida** combina o Índice com o filtro focado para que você possa pular com o mínimo de digitação:

- Pressione {% kbd f %} na visualização para abrir o TOC com o **campo de filtro em foco** (mesma ideia de abrir o TOC e pressionar {% kbd Space %}, sem a etapa extra).
- Digite parte de qualquer título de título; a lista é filtrada para correspondências.
- Se restar apenas um título, pressionar Return ({% kbd ↩ %}) vai direto para ele.
- Se restarem vários títulos, pressione Tab ({% kbd ⇥ %}) para sair do campo de filtro, mova com {% kbd j %}/{% kbd k %} ou as teclas de seta e pressione {% kbd o %} ou Return ({% kbd ↩ %}) para ir para o título e fechar o sumário.
- Tab novamente retorna o foco para o campo de pesquisa.

> **Lembrete de atalho:** Abrir o sumário e pressionar {% kbd Space %} abre a barra de filtro – útil sempre que o sumário já estiver visível.

(Documentos anteriores se referiam a isso como "Fast Switcher"; é o mesmo recurso.)

## Marcadores e Minimapa [bookmarks-and-mini-map]

Use o menu de visualização {% appmenu Gear %} e {% kbd Tab %} ({% kbd ⇥ %}) focando o documento ao lado de [pesquisar](Interface_Features.html#search) para colocar e revisitar os favoritos enquanto você folheia.

### Configurando favoritos [setting-bookmarks]

Defina marcadores na posição de rolagem usando {% kbd shift 1 %}--{% kbd shift 9 %} e volte usando {% kbd 1 %}--{% kbd 9 %} sozinho. Use {% kbd n %} e {% kbd p %} para próximo/anterior na **ordem dos documentos**; {% kbd shift n %} e {% kbd shift p %} para próximo/anterior em ordem **numérica**.

Alterar o estilo ou o tamanho da página pode mover o local onde um marcador aparece. Os marcadores servem como auxílios de revisão temporários: eles não persistem entre sessões de documentos, mas sobrevivem a atualizações e edições de visualização.

**Marcadores de título:** Segure Option e pressione {% kbd opt 1 %}--{% kbd opt 9 %} para marcar o título mais próximo do topo da janela de visualização (ou o último título antes do topo).

**Próximo slot livre:** {% kbd cmd D %} (ou backtick {% kbd \`\` %}, para usuários do vim) adiciona um marcador no próximo slot numerado disponível.

Pressione {% kbd 0 %} para expandir a faixa de marcadores (títulos de títulos quando disponíveis). Quando o [Mini Mapa](#minimap) está ativado, {% kbd 0 %} mostra-o ao mesmo tempo. Pressione Escape ou {% kbd 0 %} novamente para recolher.

Pressione {% kbd x %} duas vezes ({% kbd xx %}) para limpar todos os favoritos.

Existem [mais atalhos de visualização](Keyboard_Shortcuts.html); pressione {% kbd h %} na visualização para obter uma lista de alerta ou {% kbd opt cmd K %} para a referência completa.

### Minimapa [minimap]

Se o Minimapa estiver ativado nas configurações {% prefspane Preview %}, {% kbd 0 %} abre uma miniatura em escala de todo o documento ao longo da faixa de marcadores. Clique em qualquer lugar do mapa para rolar a visualização completa até lá. Os marcadores salvos aparecem como linhas horizontais com números (e títulos quando relevante).

Segure **Command** e mova sobre o Minimapa para obter uma lupa ampliada; segure **Option** e arraste para rolar como se estivesse arrastando a barra de rolagem.

O mapa é regenerado quando o tamanho ou o layout da janela é alterado. Em documentos muito longos, pressionar {% kbd 0 %} uma vez pode demorar um pouco; Marcado evita construir o Minimapa automaticamente no carregamento inicial até que você o solicite.

Pressione {% kbd 0 %} ou Escape para fechar o Minimapa.

**Nota de desempenho:** A geração do mapa pode pausar brevemente a visualização em documentos grandes; isso só é executado quando o mapa está visível ou após um redimensionamento.

### Visão geral do zoom (relacionado) [zoom-overview-related]

Para uma visão geral em escala de texto sem o Minimapa, consulte [Visão Geral do Zoom](Zoom_Overview.html) ({% kbd z %}).