<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

O recurso “rolar para editar” no Marked monitora as diferenças entre a atualização mais recente e a última, tentando encontrar o ponto onde você fez as alterações mais recentes. Marcado sempre rastreia isso e uma pequena linha vermelha aparece na visualização para mostrar a localização da primeira alteração detectada. No painel de preferências Comportamento, você pode ativar "Rolar para a primeira edição" e quando uma visualização for atualizada, ela rolará suavemente a visualização para esse local.

Com a opção "Rolar para a primeira edição" desativada, você ainda pode pressionar a tecla "e" a qualquer momento na visualização para ir para o último ponto de edição armazenado.


### Notas sobre "Rolar para editar"

Esse é um recurso ótimo quando funciona, mas traz muitas complicações. Especialmente nas primeiras vezes em que o documento é atualizado, pode haver alguns movimentos irregulares na rolagem. Se suas alterações estiverem todas dentro de um elemento muito grande (um parágrafo excessivamente longo, por exemplo), ele só conseguirá aproximar com o marcador. Da mesma forma, se você adicionar uma ou duas palavras ao final do documento, o marcador de alteração será posicionado no elemento acima até que haja conteúdo suficiente para ancorar no novo elemento.