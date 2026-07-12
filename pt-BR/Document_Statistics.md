<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Acompanhe enquanto você escreve.

## Contagem de palavras e estatísticas de documentos

![][1]

   [1]: images/WordCount.jpg @2x width=840px height=61px class=center

A contagem de palavras está localizada na barra de status inferior e pode ser ativada e desativada em {% prefspane General %} na barra de status. Você pode visualizar mais estatísticas na janela de visualização ou de origem no menu de engrenagem, clicando na contagem de palavras ou digitando Option-Command-S ({% kbd opt cmd S %}). Mantenha pressionada a tecla Option ({% kbd opt  %}) enquanto clica para mostrar as estatísticas de legibilidade e mantenha pressionada a tecla Option-Command ({% kbd opt cmd %}) para abrir o painel Advanced Statistics.

Se o texto for selecionado, a exibição da contagem de palavras e o pop-up de parágrafo/frase/caractere serão atualizados com informações apenas para a seleção.

## Contagem de palavras para seleção

![Pop-up de contagem de palavras na seleção de texto][2]

   [2]: images/wordcountforselection.jpg @2x width=749px height=144px class=center

Quando você seleciona texto na visualização, a contagem de palavras na parte inferior da janela mostrará estatísticas apenas para o texto selecionado.

Se "Mostrar contagem de palavras para seleção" estiver habilitado em {% prefspane Preview %}, um pequeno pop-up aparecerá perto do cursor para mostrar a contagem de palavras/linhas/caracteres do texto selecionado. Isso é descartado simplesmente afastando o mouse do pop-up.

O recurso de zoom é útil para selecionar e obter rapidamente contagens de pedaços maiores de texto. Digite {% kbd z %} para diminuir o zoom e fazer sua seleção.

## Estatísticas de legibilidade

![Barra de estatísticas de legibilidade][3]

   [3]: images/screenshots/mainwindow-feature-stats-lower-crop.jpg @2x width=1089px height=111px class=center

Estatísticas adicionais de Flesch/Kincaid e do Fog Index estão disponíveis em {% kbd opt shift cmd S %}.

### Informações de legibilidade

**Facilidade de leitura Flesch:** pontuações mais altas indicam material mais fácil de ler; números mais baixos marcam passagens que são mais difíceis de ler.

**90,0--100,0**: aluno médio de 11 anos
**60,0--70,0**: alunos de 13 a 15 anos
**0,0--30,0**: graduados universitários

**Nível de escolaridade Flesch-Kincaid:** o número de anos de educação geralmente necessários para compreender este texto.

**Índice Gunning Fog:** mede a legibilidade da escrita em inglês. O índice estima os anos de educação formal necessários para compreender o texto na primeira leitura. Um índice de neblina de 12 requer o nível de leitura de um aluno do último ano do ensino médio nos EUA (cerca de 18 anos).

## Estatísticas Avançadas

![Pop-up de estatísticas avançadas][adv]

[adv]: images/screenshots/mainwindow-feature-stats-info-crop.jpg @2x width=800px height=800px class=center

Selecionar Estatísticas Avançadas no menu de engrenagem ---- ou pressionar {% kbd cmd I %} --- abrirá um painel contendo estatísticas de documentos mais avançadas, incluindo comprimento médio de palavras e frases e complexidade média de palavras.

### Estatísticas Avançadas Flutuantes

![Janela de informações flutuante][flutuante]

[floating]: images/floatinginfo.jpg @2x width=999px height=522px class=center

Pressionar {% kbd shift cmd I %} abrirá um painel flutuante contendo todas as estatísticas detalhadas e informações de legibilidade. Este painel pode permanecer em primeiro plano quando você muda para o seu editor, para que você possa ver suas estatísticas atualizadas sempre que salvar, esteja a visualização visível ou não. Pressionar o ícone `<` retornará a visualização marcada associada ao primeiro plano. Se você segurar a opção e clicar no mesmo botão, o arquivo Markdown será aberto em seu editor de texto padrão (definido em {% prefspane Apps %}).

### Alvos de palavras

Se você tiver uma meta específica para contagem de palavras enquanto escreve, poderá adicionar uma chave de metadados "target:" na parte superior do documento e Marcado acompanhará seu progresso, exibindo um indicador de conclusão no painel Estatísticas detalhadas ({% kbd cmd I %}) e nas Estatísticas flutuantes ({% kbd shift cmd I %}).

![][targetwordcount]

[targetwordcount]: images/wordtargets.jpg @2x width=740px height=191px class=center


## Visualize a repetição de palavras

Selecionar Visualizar repetição de palavras no menu de engrenagem (ou pressionar {% kbd ctrl cmd W %}) mudará para uma visualização especial que remove elementos não textuais e destaca palavras repetidas em seu documento. Palavras repetidas são destacadas em rosa claro e passar o mouse sobre uma palavra destacada iluminará as palavras correspondentes em todo o documento. Clicar em uma palavra destacada escurecerá o fundo e “colará” o destaque para revisão posterior.

![Repetição de palavras][4]

[4]: images/screenshots/mainwindow-word-repetition.jpg @2x width=1369px height=1084px

Você também pode usar o recurso “zoom” (digite “z”) neste modo, permitindo destacar uma palavra repetida e, em seguida, digitalizar rapidamente todo o documento para ver onde as repetições estão concentradas.

As palavras são comparadas por seu “radical”, o que significa que “parte”, “parcialmente” e “partes” serão consideradas palavras repetidas. Isso leva em conta as sílabas e a conjugação ao verificar a densidade de repetição.

**Escopo**

O escopo da verificação de repetição pode ser alterado na barra de ferramentas inferior do documento e pode ser definido como Documento ou Parágrafo. O modo de documento é o padrão; selecionar Parágrafo conta apenas a repetição dentro de cada bloco de texto. As repetições ainda serão destacadas em todo o documento, mas serão contadas apenas se uma palavra aparecer mais de uma vez em um único parágrafo.

**Ignorando palavras**

Você pode excluir temporariamente uma palavra e todas as suas diversas conjugações e pluralizações clicando com a tecla Option pressionada na palavra destacada. Palavras temporariamente ignoradas aparecerão no canto inferior direito da visualização. Clicar em uma palavra na lista de palavras ignoradas irá restaurá-la para a visualização.

Para ignorar palavras permanentemente, você pode editar uma lista em {% prefspane Proofing %} na guia Ignorar repetições. Palavras (ou radicais de palavras) adicionadas uma por linha nesta lista serão sempre ignoradas. Para adicionar automaticamente uma palavra a esta lista, Option-Shift-Clique nela na visualização de repetição de palavras.

**Saindo do modo de repetição de palavras**

Você pode fechar a visualização de repetição de palavras usando o ícone Fechar próximo ao seletor de escopo na barra de ferramentas inferior ou pressionando escape.