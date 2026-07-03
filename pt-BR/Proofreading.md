<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Entre no modo de revisão no menu de engrenagem. Este é um recurso experimental desenvolvido principalmente para editores que recebem textos de outras pessoas e precisam fazer comentários e fornecer feedback.

O modo de revisão congela as atualizações do documento, evitando que anotações e notas sejam perdidas quando o documento é atualizado. Um indicador vermelho aparece na barra superior para lembrá-lo de que o modo de revisão está ativo.

Navegação pelo teclado, marcação de favoritos e destaque de palavras-chave, todas as funções durante a revisão.

## Anotações

No modo de revisão, a seleção do texto no documento gerará um pop-up que permite selecionar vários tipos de realce diferentes. Clique no tipo de destaque que deseja adicionar ao texto ou cancele clicando no botão “Cancelar” ou apenas clicando fora do pop-up.

## Notas

![Anotações][1]

[1]: images/Annotating.jpg class=center

Depois que um destaque for adicionado, você poderá adicionar notas curtas clicando no destaque. O pop-up agora conterá um campo de texto onde você pode inserir quaisquer notas que possam ser pertinentes ao texto destacado. As notas podem ser excluídas e editadas clicando em um destaque que já contém uma nota.

As notas são exportadas **apenas** ao salvar em HTML. Os destaques permanecem na maioria dos formatos de exportação, incluindo RTF e PDF.

## Verificação ortográfica

No modo de revisão, você pode acessar o corretor ortográfico de todo o sistema no menu de engrenagem: {% appmenu {{gear}}, Proofing, Show Spelling Errors %}. Isso será lento em documentos grandes e um aviso será exibido notificando se o processo demorar mais de 30 segundos ou mais. Como o corretor ortográfico não funciona na visualização da web do Marked, um “hack” é implementado para fazer isso funcionar, e não é rápido.

Depois que a verificação ortográfica for executada, você poderá abrir o painel Suposições ortográficas para ativar a verificação gramatical e também ver sugestões para corrigir erros. Marcado como *não* é possível editá-los no local, você terá que voltar ao documento original para usar os resultados.

*Atalhos:* {% kbd ctrl opt cmd S %} executará o corretor ortográfico. {% kbd ctrl opt cmd N %} irá para o próximo erro no documento e {% kbd ctrl opt cmd G %} mostrará o painel de suposições.