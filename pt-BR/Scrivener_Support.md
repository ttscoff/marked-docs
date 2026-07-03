<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Use suas duas ferramentas de escrita favoritas juntas.

> Marked ainda pode ler arquivos do Scrivener 2.0, mas o desenvolvimento será focado na versão 3 após Marked 2.5.11.

## Noções básicas do Scrivener 3.0

Arraste um projeto Scrivener (.scriv) para Marcado e ele será compilado e visualizado. Se você escolher a opção de abrir arquivos .scriv no Scrivener (acima), o Marked também iniciará o Scrivener quando você arrastar o arquivo para o Marked.

Tal como acontece com outros documentos, as alterações nos arquivos do Scrivener são atualizadas ao salvar. Além disso, quando um documento do Scrivener estiver em primeiro plano no Marked, {% kbd cmd E %} irá abri-lo no Scrivener para você.

## Filtrando documentos fichários

Quando você abre um projeto do Scrivener no Marked, o conteúdo de visualização é criado apenas a partir dos documentos do fichário selecionados. A filtragem está sempre ativa para arquivos `.scriv`; o painel de filtros é apenas uma maneira conveniente de alterar o que está incluído.

Abra o painel em **Proofing > Filter Scrivener Documents** ({% kbd opt-cmd-f %}). O item de menu mostra uma marca de seleção enquanto o painel está visível. Fechar o painel não desativa a filtragem nem redefine suas seleções.

O painel de filtros lista as seções do fichário do seu projeto (Rascunho, Pesquisa e outros fichários de nível superior, exceto Lixo). Cada seção é recolhida por padrão. Expanda uma seção para ver seus documentos e pastas em um resumo:

- Marque ou desmarque qualquer **documento de texto** para incluí-lo ou excluí-lo da visualização.
- Clique em uma linha de **pasta** para selecionar ou desmarcar todos os seus descendentes. Um traço na caixa de seleção significa que apenas alguns descendentes estão selecionados.
- Linhas com **Incluir na compilação** desativadas no Scrivener aparecem acinzentadas, mas você ainda pode marcá-las para visualizá-las em Marcado.
- **Imagens, PDFs e outros itens de fichário que não sejam de texto** aparecem na lista, mas não podem ser selecionados.
- **Arquivos RTF ausentes** ainda aparecem; se você adicionar conteúdo no Scrivener enquanto Marcado estiver aberto, a visualização será atualizada ao salvar como qualquer outra alteração do Scrivener.

Use **Selecionar tudo** e **Desmarcar tudo** na parte superior do painel para todo o projeto. Cada cabeçalho de seção possui botões **Todos** e **Nenhum** somente para aquela seção. **Desmarcar tudo** significa que nenhum documento será verificado.

Se nada estiver selecionado, a visualização mostra uma mensagem curta com um link para abrir o painel de filtros (`x-marked://scrivenerfilter`). Você pode usar esse URL em scripts ou outros aplicativos para aumentar o painel do documento frontal do Scrivener em Marcado.

Suas seleções de caixa de seleção são salvas por projeto do Scrivener (pelo identificador do projeto no arquivo `.scrivx`) e restauradas na próxima vez que você abrir esse projeto em Marcado. Na primeira vez que você abre um projeto, Marcado seleciona apenas documentos do fichário **Rascunho** cujo sinalizador **Incluir na compilação** é Sim (ou não definido, que o Scrivener trata como Sim). A pesquisa e outras pastas começam sem controle; Os itens de rascunho excluídos da compilação começam desmarcados, mas permanecem selecionáveis ​​na lista.

Os projetos do Scrivener 2 mostram apenas o fichário **Rascunho** no painel de filtro. Os projetos do Scrivener 3 incluem todos os fichários, exceto Lixo.

O painel de filtros pode permanecer aberto junto com outras ferramentas, como **Visualizar Repetição de Palavras**. Alterar uma caixa de seleção recompila a visualização após um pequeno atraso; se um projeto grande ainda estiver sendo compilado, Marcado cancela a importação em andamento e inicia novamente com sua nova seleção.

## Cabeçalhos Markdown de títulos do Scrivener

Marked também pode criar cabeçalhos Markdown hierárquicos para você com base nas páginas do seu arquivo Scrivener. Para habilitar isso, basta marcar a opção mostrada acima.

## Metadados MultiMarkdown

Se o primeiro documento na sua pasta Rascunho for denominado "metadados", ele será tratado como metadados MultiMarkdown no início do documento de visualização. Nenhum cabeçalho será inserido para esta seção, independentemente da configuração "Markdown Headers from Scrivener Titles" (descrita acima), permitindo que o processador MultiMarkdown os leia como metadados e permita substituições e opções de exportação de acordo.

Você pode tornar este arquivo formatado em YAML se o seu processador for um que lide com YAML.

Se você não usar um documento `metadata`, Marked também pode preceder os metadados do MultiMarkdown das configurações de compilação do seu projeto (`Settings/compile.xml`), usando os mesmos campos **Título** e **Autor** que o Scrivener exportaria para o MultiMarkdown. Isso está habilitado por padrão (chave de preferência `scrivenerCompileMetadata`). Os campos de metadados personalizados são incluídos apenas quando aparecem nas configurações de compilação de **Metadados MMD** do projeto, e não em campos personalizados por documento.

##Links

Para links externos (HTTP), você pode usar a sintaxe Markdown ou a formatação de link do Scrivener. Marcado converterá o formato Scrivener em Markdown antes do processamento.

## Comentários

Marcado pode processar comentários e notas de rodapé criados embutidos no documento.

## Tabelas

Marcado pode converter tabelas básicas do Scrivener. Entretanto, se você quiser incluir uma tabela em sua saída, é melhor fazê-lo em [formato de tabela MultiMarkdown](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#tables). (Um aplicativo chamado [TableFlip](http://tableflipapp.com/) pode tornar a geração deles uma tarefa simples.)

## Recursos adicionais do Scrivener

Além dos recursos básicos de compilação e visualização, Marked também oferece suporte a algumas convenções específicas do Scrivener. Primeiro, em seu documento Scrivener, você pode usar "Preservar formatação" embutido ou em um bloco de texto independente e ele será convertido em blocos de código na visualização.

Marcado também lê notas de rodapé _inline_ do Scrivener. Se você inserir uma nota de rodapé dentro ou no final de um parágrafo, ela será convertida em uma nota de rodapé MultiMarkdown na visualização.

## Usando imagens em seu documento Scrivener

As imagens podem ser incorporadas no documento Scrivener ou referenciadas com a sintaxe de imagem Markdown. A versão Markdown de uma tag de imagem é `![alt text](path/to/image.ext "optional title/description")`. O formato de referência também pode ser usado:

    ![texto alternativo][img1]

    [img1]: /path/to/image.ext "descrição opcional"

O caminho base para a saída HTML na visualização será definido para a pasta que contém o documento Scrivener. Assim, colocar as imagens na mesma pasta do documento de trabalho permitirá que elas sejam acessadas diretamente. Se o seu documento Scrivener estiver em `~/Desktop/TestDoc.scriv` e você tiver uma imagem chamada "testimage.png" em `~/Desktop/testimage.png`, você pode adicionar a imagem ao seu documento usando:

    ![Imagem de teste](testimage.png)

Caminhos relativos baseados na pasta pai do documento funcionarão, e caminhos absolutos permitirão acesso a imagens em qualquer lugar, mas podem não ser tão portáveis para saída HTML.

## Nota de segurança

Uma pasta de cache será criada em ~/Library/Application Support/Marked quando você abrir seu arquivo .scriv em Marked. Esta não é uma pasta protegida, portanto, se o seu documento original estiver em um disco criptografado ou protegido de outra forma, observe que seu conteúdo não será criptografado no cache. Para proteção limitada, você pode garantir que esse cache não apareça no Spotlight adicionando ~/Library/Application Support/Marked às suas configurações de privacidade no Spotlight.

Consulte [Integrações adicionais de aplicativos](Additional_Application_Support.html) para visualização da área de transferência, links de wiki, scripts e a lista completa de guias por aplicativo.