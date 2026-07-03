<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Speed Read é um modo de leitura no estilo RSVP que exibe uma palavra por vez em uma sobreposição focada.

## Como funciona a leitura rápida

O Speed Read usa um método chamado **Rapid Serial Visual Presentation** (RSVP). Em vez de mover os olhos pelas linhas do texto, as palavras aparecem em uma posição fixa. Isso reduz os movimentos dos olhos, as mudanças de linha e o retrocesso que normalmente ocorrem durante a leitura, o que pode torná-lo útil para folhear, revisar material familiar ou mover-se rapidamente pelo texto sem perder o lugar.

O método não é mágico e não garante melhor compreensão em velocidades muito altas. A compreensão da leitura ainda depende da complexidade da escrita, da sua familiaridade com o assunto e da configuração do WPM. Para materiais densos ou desconhecidos, uma velocidade moderada é geralmente mais eficaz do que aumentar a taxa o mais alto possível.

A letra vermelha marca o ponto de ancoragem visual da palavra, às vezes chamado de **ponto de reconhecimento ideal**. Em muitas palavras, os leitores identificam a palavra com mais eficiência quando seu olhar pousa ligeiramente à esquerda do centro, e não na primeira letra. Ao manter esse ponto de ancoragem no mesmo lugar e destacá-lo, o Speed ​​Read dá ao seu olho um alvo consistente. O resultado é menos reorientação entre as palavras e um ritmo mais constante à medida que o texto avança.

## Leitura da velocidade de abertura

Use **Preview > Speed Read**, o item **Speed Read** no menu Gear da janela de visualização, ou pressione {% kbd ctrl opt S %}. O item de menu está disponível quando uma janela de visualização do documento Markdown está ativa (está desabilitada para visualizações HTML brutas e quando nenhum documento está aberto).

Quando o Speed ​​Read é aberto, ele começa em um estado de pausa para que você possa se orientar antes do início da reprodução.

<controles de vídeo preload="metadata" poster="images/speedread-poster.png">
  <fonte src="images/speedread.webm" type="video/webm">
  <fonte src="images/speedread.mp4" type="video/mp4">
  Seu navegador não suporta o vídeo de demonstração do Speed Read.
</vídeo>
<p><em>Sobreposição de leitura rápida mostrando controles de reprodução, opção de sincronização e acesso à ajuda.</em></p>

## Controles de sobreposição

Assim que a sobreposição estiver visível, estas chaves estarão disponíveis:

| Atalho | Função |
| :-- | :-- |
| {% kbd space %} | Reproduzir/Pausar |
| {% kbd [ %} | Ir para o início do parágrafo (pressione novamente para o parágrafo anterior) |
| {% kbd ] %} | Ir para o início do próximo parágrafo |
| {% kbd left %} | Diminuir a velocidade de leitura (WPM) |
| {% kbd right %} | Aumentar a velocidade de leitura (WPM) |
| {% kbd esc %} | Leitura de velocidade de saída |

Os colchetes são capturados para navegação de parágrafo e as setas esquerda/direita são capturadas para alterações de velocidade, portanto, essas teclas não acionam a navegação de visualização enquanto a leitura rápida está aberta. Você também pode clicar no botão circular **X** no canto superior esquerdo da sobreposição para descartá-la.

Outros atalhos normais de navegação de visualização ainda funcionam enquanto a leitura rápida está ativa, incluindo `t`/`gg` (parte superior), `G`/`b` (parte inferior) e `,`/`.` (navegação no cabeçalho). Consulte [Navegação de visualização](Keyboard_Shortcuts#preview-navigation) para obter a lista completa.

O Índice também pode ser usado durante a Leitura Rápida. Pressione {% kbd cmd t %} para abri-lo e navegar ou pressione {% kbd f %} para focar imediatamente a pesquisa rápida para navegar pelos cabeçalhos dos documentos.

## Partindo de uma seleção

Se o texto for selecionado na visualização quando você iniciar a leitura rápida, a reprodução usará o texto selecionado. Se nenhuma seleção estiver ativa, o Speed ​​Read usa o texto completo do documento.

## Sincronizando com a posição de rolagem

Ative **Sincronizar leitura rápida com posição de rolagem** em {% prefspane Preview %} ou use a caixa de seleção na sobreposição de leitura rápida para manter a visualização e a posição de leitura rápida juntas.

Quando esta opção está ativada, a leitura rápida começa no conteúdo atualmente visível na parte superior da visualização, em vez de no início do documento. À medida que a reprodução avança, a visualização rola junto com as palavras exibidas.

Se você fechar o Speed ​​Read, rolar a visualização e reabrir a sobreposição, a reprodução começará a partir da nova posição visível. Se você ativar a caixa de seleção de sobreposição depois que a leitura rápida já estiver aberta, a reprodução será redefinida para a posição de rolagem atual e continuará a partir daí.

## Velocidade lembrada

O valor WPM é salvo automaticamente quando você o altera com {% kbd ← %} e {% kbd → %}. A velocidade escolhida será restaurada na próxima vez que você usar o Speed ​​Read.