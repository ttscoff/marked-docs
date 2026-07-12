<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

O Style Manager fornece uma interface centralizada para gerenciar todos os seus
estilos integrados e personalizados. Dá a você controle total sobre quais
Os estilos aparecem em menus, em sua ordem, em atalhos de teclado e muito mais.

## Abrindo o Gerenciador de Estilos

Para abrir o Gerenciador de estilos, clique no botão **Gerenciar estilos…** no {% prefspane Style %}
painel ou use {% appmenu Style, Manage Styles (~@$m) %}. Você também pode arrastar arquivos CSS diretamente para a janela de preferências --- Marcado
irá importá-los, abrir o Style Manager e selecionar a linha recém-adicionada para
você.

![Gerenciador de estilo][gerenciador de estilo img]

  [img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

## A tabela de estilos

O Style Manager exibe todos os seus estilos em uma tabela classificável que mistura
estilos integrados e personalizados perfeitamente. Cada linha da tabela contém vários
colunas:

### Caixa de seleção habilitada

A caixa de seleção **Ativado** adiciona ou remove imediatamente o estilo da janela Estilo
menu, pop-up Estilo padrão e atalhos de teclado. Quando você desabilita um estilo,
ele fica oculto nos menus, mas permanece no Gerenciador de estilos para fácil reativação.

Se você desabilitar o estilo atualmente ativo, Marcado muda automaticamente para o estilo
próximo estilo habilitado disponível.

### Coluna Nome

A coluna **Nome** exibe o nome de exibição do estilo. Você pode editar este nome
inline clicando diretamente nele; as mudanças persistem e se propagam para todos os menus
onde o estilo aparece. Isto é especialmente útil para estilos personalizados onde você
pode querer um nome mais descritivo do que o nome do arquivo.

Os estilos integrados têm nomes bloqueados que não podem ser editados. Para personalizar um
nome do estilo integrado, duplique-o primeiro para criar uma cópia editável.

### Coluna de origem

A coluna **Fonte** indica de onde vem o estilo:

- **Integrado**: estilos que vêm com Marcado e são armazenados no aplicativo
  pacote
- **Personalizado**: estilos que você adicionou de arquivos CSS em sua unidade
- **Duplicado**: estilos criados pela duplicação de outro estilo (integrado
  ou personalizado)

### Coluna Ações

Cada linha inclui uma pilha de **Ações** com botões para gerenciar esse estilo:

**Editar**: Abre o arquivo CSS em seu editor padrão. Os estilos integrados não podem ser
editados diretamente - você precisará duplicá-los primeiro para criar uma cópia editável.

**Duplicar**: Cria uma cópia do estilo e um novo arquivo CSS no disco. O
duplicado aparece imediatamente abaixo do estilo original na tabela. Isto é
a maneira recomendada de personalizar estilos integrados.

**Revelar**: mostra o arquivo CSS no Finder, facilitando a localização do arquivo no
sua unidade. Este botão está disponível apenas para estilos personalizados com um caminho de arquivo.

**Excluir**: Remove o estilo de Marcado. Para estilos personalizados, você receberá
a opção de remover apenas a referência (mantendo o arquivo CSS) ou mover
o arquivo CSS para a Lixeira. Os estilos integrados não podem ser excluídos, mas podem ser
desativado.

**Restaurar**: para estilos integrados, este botão restaura o estilo ao seu estado original.
estado padrão se tiver sido modificado. Este botão só é visível para
estilos integrados.

## Reordenando estilos

As linhas podem ser reordenadas arrastando e soltando. Basta arrastar uma linha de estilo para um novo
posição na tabela. A ordem que você define aqui determina:

- A ordem do menu Estilo nos menus do Marked
- Atribuições de atalhos de teclado (`⌘1`–`⌘9` para os primeiros nove estilos habilitados,
  `⌥⌘1`–`⌥⌘0` para os próximos dez e assim por diante)

Arraste os estilos para os slots de atalho do teclado que você deseja
ocupar.

## Adicionando estilos

Existem várias maneiras de adicionar novos estilos personalizados ao Style Manager:

### Adicionar botão

Clique no botão **Adicionar novo estilo** para abrir um seletor de arquivos
onde você pode selecionar um ou mais arquivos CSS para importar. Os arquivos selecionados serão
adicionado ao Style Manager e ativado por padrão.

### Arraste e solte

Você pode arrastar arquivos CSS diretamente para a janela do Style Manager. Quando você arrasta
arquivos na janela, uma sobreposição aparecerá mostrando "Adicionar um estilo personalizado" (ou
"Adicionar N estilos personalizados" para vários arquivos). Solte os arquivos para importá-los.

Você também pode arrastar arquivos CSS para posições específicas na tabela — o botão soltar
indicador mostra onde o novo estilo será inserido, permitindo controlar
importar e posicionar em uma ação.

Arrastar arquivos CSS para o painel de preferências {% prefspane Style %} também
importe-os e abra o Style Manager automaticamente.

## Visualização ao vivo

O painel direito do Style Manager exibe uma visualização ao vivo do selecionado
estilo. A visualização renderiza um documento de amostra abrangente com títulos,
listas, tabelas, blocos de código, blockquotes e outros elementos Markdown comuns,
todos estilizados com o CSS real do estilo selecionado.

A visualização usa o arquivo CSS diretamente do disco, então qualquer edição que você fizer no seu
o editor externo será atualizado instantaneamente na visualização. Isso torna mais fácil
veja suas alterações em tempo real à medida que desenvolve estilos personalizados.

### Visualização do modo escuro

Uma caixa de seleção acima da visualização permite alternar entre o modo claro e escuro
prévias. Isso é útil para testar a aparência dos estilos em ambos os modos de aparência,
especialmente se você estiver criando estilos que se adaptam à aparência do sistema.

## Atalhos de teclado

O Style Manager exibe uma legenda abaixo da tabela mostrando como o teclado
atalhos são atribuídos. Os primeiros nove estilos habilitados recebem {% kbd cmd 1 %} até
{% kbd cmd 9 %} ({% kbd cmd 0 %} é reservado), os próximos dez recebem {% kbd opt cmd 1 %} a {% kbd opt cmd 0 %} e assim por diante. Você pode ver os atalhos de teclado atribuídos no menu pop-up Estilo em qualquer visualização.

## Filtrando estilos desativados

Uma caixa de seleção na parte inferior da janela permite mostrar ou ocultar
estilos. Quando desmarcada, apenas os estilos habilitados são exibidos, facilitando
concentre-se e reordene seus estilos ativos. Quando marcado, todos os estilos (ativados e desativados)
são mostrados, permitindo que você gerencie sua coleção completa de estilos.

## Restaurando estilos integrados

O botão **Restaurar todos os estilos integrados** na parte inferior da janela
restaura todos os estilos integrados ao seu estado padrão. Isto é útil se você tiver
estilos integrados desativados e deseja reativá-los ou se deseja redefinir
quaisquer modificações feitas nos estilos integrados.

## Dicas

- **Organize por frequência**: arraste os estilos mais usados para o topo para obter
  apresentam os atalhos de teclado mais fáceis ({% kbd cmd 1 %}, {% kbd cmd 2 %}, etc.)

- **Desativar em vez de excluir**: em vez de excluir estilos que você não está usando,
  desative-os. Eles ficarão fora do seu caminho, mas permanecerão disponíveis se você precisar
  eles mais tarde.

- **Use duplicado para experimentação**: duplique um estilo antes de fazer major
  alterações para que você possa sempre retornar ao original.

- **Visualizar durante a edição**: mantenha o Gerenciador de estilos aberto durante a edição do CSS
  arquivos para ver suas alterações atualizadas em tempo real no painel de visualização.

- **Importação em lote**: você pode selecionar vários arquivos CSS de uma vez ao usar o
  Botão Adicionar ou arraste vários arquivos para importá-los todos em uma única ação.