<!-- MT draft for pt-BR — Reading Mode help. Review before publishing. -->
# <%= @title %>

O modo de leitura mantém seu lugar em documentos longos, concentra o bloco atual e permite salvar destaques persistentes.

## Entrando no modo de leitura [entering-reading-mode]

Escolha {% appmenu Preview, Reading Mode %} ou pressione {% kbd ctrl opt r %}. Se o Speed ​​Read estiver em execução, Marked o interrompe antes de entrar no modo de leitura.

O parágrafo, título, item de lista, imagem, bloco de código, tabela ou outra unidade de leitura atual recebe um marcador à esquerda. A navegação pelo teclado se move suavemente entre os blocos e mantém a unidade atual próxima ao terço superior da visualização. A rolagem manual redireciona o foco sem ajustar a página.

## Navegação e currículo [navigation-and-resume]

Enquanto o modo de leitura estiver ativo:

- {% kbd j %} ou {% kbd down %}: Move para a próxima unidade de leitura.
- {% kbd k %} ou {% kbd up %}: Move para a unidade de leitura anterior.
- {% kbd h %}: Realce a seleção ou alterne um destaque na unidade atual quando nenhum texto for selecionado.

Marked salva a posição de leitura atual de cada documento. Quando uma posição salva difere da visualização atual, entrar no Modo de Leitura oferece duas opções:

- **Resume** retorna à posição de leitura salva.
- **Comece daqui** usa a unidade de leitura atualmente visível na visualização.

## Modo foco [focus-mode]

Clique na ferramenta Modo de foco na parte superior da visualização para escurecer todos os blocos, exceto a unidade de leitura atual. O modo de foco segue a unidade atual conforme você navega. Clique na ferramenta novamente para restaurar os outros blocos ou saia do Modo de Leitura para limpar o modo Foco automaticamente.

## Criação e edição de destaques [creating-and-editing-highlights]

Selecione o texto e pressione {% kbd h %} para criar um destaque de marcador embutido. Sem seleção, pressione {% kbd h %} para destacar toda a unidade de leitura atual ou pressione novamente para remover o destaque dessa unidade. O primeiro destaque solicita uma assinatura, que Marked usa ao criar CriticMarkup. Você pode alterar a assinatura em {% prefspane Preview %}.

### Pop-up de seleção

Selecione o texto para mostrar o pop-up de seleção com botões de ícone centralizados na linha:

- **Marcador** cria um realce embutido (ou **X** remove o último realce automático quando o realce automático está ativado).
- **Comentário** abre uma caixa de diálogo para adicionar ou editar uma nota para o destaque. Se a seleção ainda não estiver destacada, Marked a destaca primeiro.

O pop-up também mostra a contagem de palavras de seleção quando **Mostrar contagem de palavras na seleção** está ativado.

### Destacar comentários [highlight-comments]

Os comentários são separados das assinaturas. Uma assinatura atribui o destaque; um comentário é sua nota sobre isso.

Adicione ou edite um comentário no ícone de comentário pop-up de seleção ou clique com a tecla Control pressionada em um destaque e escolha **Adicionar comentário…** ou **Editar comentário…**. Escolha **Excluir comentário** para remover a nota sem excluir o destaque.

Os destaques com comentários mostram um pequeno ponto indicador. Quando a barra lateral Comentários está visível (**Visualização > Mostrar comentários**), os comentários de destaque do Modo de leitura aparecem lá com uma linha de conexão ao destaque pai, ao lado de CriticMarkup e outros comentários do documento.

### Destaques automáticos

Clique na ferramenta de realce na parte superior da visualização para destacar automaticamente o texto conforme você o seleciona. Clique no marcador no pop-up de seleção para desfazer o último realce automático ou clique novamente na ferramenta de realce superior para desativar o realce automático.

Os destaques embutidos exibem alças de início e fim quando você aponta ou seleciona-os. Arraste uma das alças para estender ou contrair o intervalo destacado. As alterações são salvas automaticamente e restauradas quando o documento é atualizado ou reaberto.

Clique em um destaque para focalizá-lo e pressione Delete ou Backspace para removê-lo. Clique com a tecla Control pressionada em um destaque e escolha **Compartilhar...** para abrir a planilha de compartilhamento do macOS com o título do documento e o texto destacado, **Adicionar comentário…** / **Editar comentário…** para anexar uma nota ou **Excluir comentário** para limpar a nota.

A configuração **Mostrar destaques quando o modo de leitura está desativado** controla se os destaques salvos permanecem visíveis depois que você sai do modo.

## Exportando destaques [exporting-highlights]

Escolha **Visualizar > Exportar destaques…** ou clique na ferramenta Exportar destaques na barra de ferramentas Modo de leitura. Formatos: Markdown, HTML (estilo de visualização atual), texto simples, CSV (compatível com Readwise, com comentários na coluna **Nota** e assinaturas em **Assinatura**) e JSON (inclui um campo `comment` em cada destaque).

Os ninhos de exportação HTML destacam os comentários como aspas abaixo de cada passagem destacada.

O formato JSON é o arquivo de intercâmbio de Marked. Salve-o ao lado de um documento Markdown como `Document.markedhighlights.json` ou inclua-o automaticamente ao exportar um TextBundle.

## Importando destaques [importing-highlights]

Escolha **Visualizar > Importar destaques…** e selecione um arquivo JSON de Marked destaques. Os destaques são mesclados por ID: novos IDs são adicionados, os IDs correspondentes são atualizados e os destaques existentes que não estão no arquivo permanecem.

Quando você abre um TextBundle que contém `highlights.json`, Marked mescla esses destaques automaticamente. Enquanto um TextBundle está aberto, Marked também salva as alterações de destaque e comentário de volta para `highlights.json` no pacote (sem modificar `text.md`).

## TextBundle destaques [textbundle-highlights]

Em **Salvar TextBundle**, ative **Incluir destaques** para incorporar `highlights.json` no pacote (ou TextPack). Compartilhe o pacote para que os colaboradores possam abri-lo em Marked e manter um conjunto de destaques combinado.

## CriticMarkup ações [criticmarkup-actions]

Separado da exportação e importação de destaques, o menu Visualização fornece duas ações CriticMarkup para destaques salvos:

- **Copiar destaques como CriticMarkup** copia todos os destaques no formato CriticMarkup sem alterar o arquivo de origem.
- **Injetar destaques no documento...** pede confirmação e, em seguida, agrupa o texto fonte correspondente inequívoco em CriticMarkup. Marked ignora correspondências ausentes, duplicadas ou sobrepostas e relata o resultado.

Com assinatura e comentário, a marcação gerada usa <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature: comment&lt;&lt;}</code>. Com apenas um comentário, Marked usa <code>{=<span>=</span>highlighted text==}{&gt;&gt;comment&lt;&lt;}</code>. Com apenas uma assinatura, usa <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code>. Sem nenhum deles, Marked cria apenas o marcador <code>{=<span>=</span>highlighted text==}</code>.

## Imprimindo destaques [printing-highlights]

Os destaques do modo de leitura são incluídos ao imprimir ou salvar como PDF por padrão. Use **Incluir destaques do modo de leitura** na folha de impressão para alterá-lo para a saída atual. A configuração correspondente em {% prefspane Export %} controla o padrão para trabalhos futuros de impressão e PDF.
