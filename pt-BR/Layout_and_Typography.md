<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado fornece padrões para melhorar a tipografia e o layout de exportação, além de oferecer controle finito sobre as opções se você precisar de mais personalização.

## Tipografia

### Hifenização e viúvas

A opção _Hifenização automática em parágrafos_ permite que Marcado determine onde uma linha seria melhor hifenizada para melhorar o "trapo" de um parágrafo. Isso é mais útil ao usar um estilo com alinhamento justificado, mas também pode melhorar o fluxo de leitura em parágrafos mais longos.

A opção _Evitar viúvas em títulos e parágrafos_, se habilitada, forçará quebras em títulos e parágrafos para evitar que palavras curtas e únicas terminem sozinhas em uma linha.

Marcado conecta automaticamente os títulos ao seguinte elemento, para evitar títulos órfãos ao exportar para um formato paginado (PDF, impressão).

### Sinais de pontuação

Se o seu processador estiver configurado para MultiMarkdown, você terá a opção de ativar ou desativar a "pontuação inteligente" usando a opção _Gerar aspas e pontuação tipograficamente corretas_. Se ativado, as aspas duplas e simples emparelhadas serão transformadas em aspas "curvas", os apóstrofos serão substituídos por símbolos tipograficamente corretos e outros ajustes automáticos serão realizados.

### Marcadores de notas de rodapé

Na seção Layout e Tipografia de {% prefspane Style %}, _Surround marcadores de notas de rodapé com colchetes_ é habilitado por padrão ao usar o processador MultiMarkdown e cria marcadores de notas de rodapé dentro do documento que são cercados por colchetes (por exemplo, "[1]"). Para desabilitar a criação de colchetes, desmarque esta opção.

## Modo de contorno

O modo de estrutura de tópicos exibirá qualquer arquivo contendo uma série hierárquica de cabeçalhos como um APA ou estrutura de tópicos decimal. O padrão é o estilo APA, mas pode ser desativado.

Em {% prefspane Style %} em "Layout e tipografia", você pode adicionar extensões de nome de arquivo para as quais o modo Outline é ativado automaticamente. Isso é especialmente útil para OPML e arquivos de mapas mentais suportados (como iThoughtsX e MindNode). A extensão deve ser apenas a parte alfanumérica do nome do arquivo que aparece após o último caractere de ponto.

Alterne o modo de contorno padrão com a caixa de seleção _Usar estilo APA_. Isso pode ser alternado temporariamente no menu de engrenagem da janela de um documento.


## Poesia

A opção _Estilo de blocos de código literal como poesia_ em {% prefspane Style %} fará com que blocos recuados por 4 ou mais espaços sejam exibidos usando o estilo "poesia" do tema. Geralmente é uma seção em itálico e sem destaque de sintaxe.

As quebras de linha são preservadas nesses blocos por padrão, proporcionando uma maneira fácil de incorporar poesia e seções líricas em um documento que não precisa de outros blocos de código.

> Esta configuração adiciona uma classe de corpo "poesia" que pode ser usada em temas personalizados para estilizar blocos de código e outros elementos quando o "modo poesia" está ativado.

## Quebra de bloco de código

_Permitir que os temas envolvam o texto dentro dos blocos de código_ permite que o estilo de visualização determine como formatar os blocos de código. Desabilitar esta opção força todos os blocos de código a rolarem o estouro horizontal em vez de envolvê-los, independentemente do estilo de visualização atual.

## Trabalhando em tela cheia

Ao usar Marcado no modo de tela inteira (Control-Command-F), você pode limitar a largura do texto exibido para criar uma coluna centralizada de conteúdo legível. A caixa de seleção _Limitar largura do texto na visualização_ ativará um controle deslizante com o qual você pode definir a largura máxima do conteúdo exibido. Isso também afeta a exibição em tela não cheia.