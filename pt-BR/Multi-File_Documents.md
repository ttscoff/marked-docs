<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado permite diversas sintaxes diferentes para incluir um arquivo dentro de outro.

## Sintaxe marcada [marked-syntax]

Você pode incluir arquivos externos em um único documento de visualização usando a sintaxe especial `<<[path/file]` no início de uma linha. A linha deve ter linhas em branco acima e abaixo dela, e o caminho é considerado relativo ao documento principal, a menos que comece com uma barra (`/`) ou um til (`~`). Barra (diretório raiz) e til (diretório inicial) podem ser usados ​​para definir caminhos absolutos para arquivos. Nenhum caminho é necessário se os arquivos externos estiverem na mesma pasta do documento principal, basta colocar o nome do arquivo (diferenciando maiúsculas de minúsculas e incluindo extensão) entre colchetes.

Você pode usar os cabeçalhos de metadados "Incluir Base" ou "Transcluir Base" para alterar a localização base dos arquivos incluídos, por exemplo:

    Transcluir Base: ~/Desktop

*Observe que ao visualizar documentos com arquivos incluídos, você pode digitar “I” (shift-i) para ver qual arquivo incluído está na área visível. Pressionar Enter enquanto o caminho do arquivo incluído é exibido abrirá o arquivo incluído no editor padrão.*

Usando este recurso você pode criar documentos/livros grandes usando vários arquivos (por exemplo, um arquivo para cada capítulo) e então especificar a ordem dos documentos em um único arquivo de índice. Não importa como os arquivos são nomeados ou como as pastas são organizadas; o arquivo que você abrir em Marcado será considerado o índice e os arquivos listados dentro dele serão incluídos. Um exemplo de arquivo de índice para um documento de três partes:

Estrutura de pastas:

![][1]

   [1]: images/multifiledocumentstructure.jpg @2x width=316px height=163px class=center

Índice.md:

	# Título do documento

	## Seção 1

	<<[seções/seção1.md]

	## Seção 2

	<<[seções/seção2.md]

	## Seção 3

	<<[seções/seção3.md]

Abrir Index.md em Marcado exibirá seu conteúdo com todos os três arquivos incluídos expandidos dentro. Todos os arquivos incluídos serão monitorados em busca de alterações. Ao contrário do documento aberto no Marked, o rastreamento de arquivos incluídos depende do Spotlight para obter atualizações e deve existir em uma pasta indexada pelo Spotlight em seu disco.

Você também pode incluir trechos de código e HTML bruto ou texto usando [variações desta sintaxe](Special_Syntax.html#includingcode).

A exportação HTML final de um documento contendo inclusões terá comentários HTML contendo o caminho relativo do arquivo incluído no início e no final do texto importado.

**Observação:** quanto mais arquivos forem incluídos em um documento, mais lento será o tempo geral de compilação da visualização. Marcado tenta otimizar e armazenar em cache o processo, mas espera alguns atrasos na renderização à medida que o tamanho do documento aumenta.

## Sintaxe de transclusão de MultiMarkdown [multimarkdown-transclude-syntax]

Você também pode usar a sintaxe `{{filename}}` baseada na especificação MultiMarkdown mais recente. Marked reconhecerá `Transclude Base: path` nos metadados MMD e os usará como base para transclusão de arquivos.

O Transclude Base só será reconhecido no documento pai, e não em documentos adicionais incluídos. Todas as inclusões aninhadas devem ter caminhos baseados na Base de Transclusão inicial ou no local do documento pai.

A sintaxe do código protegido que o MultiMarkdown fornece para incluir arquivos sem processamento não funcionará no Marked. Para fazer isso, use a sintaxe `<<(file)` (bloco de código) ou `<<{file}` (bruto).

## Sintaxe do bloco IA Writer [ia-writer-block-syntax]

Marcado como 2.5.11+ suporta a sintaxe IA Writer [Content Block][ia]. Esta é uma referência que começa com uma barra (`/`) em sua própria linha. Pode ser um exemplo de código, uma imagem, um arquivo markdown ou um arquivo CSV. Tudo será tratado adequadamente com base na extensão do arquivo incluído, e os CSVs serão [convertidos em tabelas Markdown][csv], se possível.

No gravador IA, os arquivos incluídos são trazidos para o contêiner do iCloud e nem sempre exigem caminhos "reais". Em Marcado, a menos que os arquivos incluídos já existam na mesma pasta do arquivo que está sendo visualizado, esta sintaxe deve ser usada com um caminho, absoluto ou relativo. A primeira barra será ignorada, portanto, se for um caminho absoluto, comece com duas barras.

Um snippet de código na mesma pasta do documento que está sendo visualizado:

    /snippet.h

Caminho relativo para um subdiretório chamado "images":

    /images/image.png "título opcional"

Caminho absoluto para a pasta Documentos:

    //Usuários/nome de usuário/Documentos/content.csv

[ia]: https://github.com/iainc/Markdown-Content-Blocks
[csv]: Creating_Tables_using_CSV_files.html

## Como o esboço, o mapa mental e as inclusões de CSV são convertidos [how-outline-mind-map-and-csv-includes-are-converted]

Quando você inclui certos tipos de arquivo com sintaxe de bloco `<<[path]` ou IA Writer, Marked os converte em vez de inserir o conteúdo do arquivo bruto. O comportamento do esboço e do mapa mental depende da extensão do arquivo e de suas preferências [Configurações: Aplicativos → Mapas Mentais/Esboços][mapas mentais]. Arquivos CSV/TSV são sempre convertidos em tabelas Markdown (consulte [Criando tabelas usando arquivos CSV][csv]).

| Formato | Extensão | Quando "Incorporar como sereia" está **ativado** | Quando **desligado** |
|--------|------------|-----------------------------------|-------------|
| **iPensamentos X** | .itmz | Diagrama de mapa mental de sereia (árvore arrumada) | Imagem de visualização do .itmz |
| **MindManager** | .mmap | Diagrama de mapa mental de sereia | Lista Markdown aninhada |
| **FreeMind** | .mm | Diagrama de mapa mental de sereia | Lista Markdown aninhada |
| **OPML** | .opml | Diagrama de mapa mental de sereia | Lista Markdown aninhada |
| **OmniOutliner** | .ooutline | Diagrama de mapa mental de sereia | Lista Markdown aninhada |
| **Bicicleta** | .bicicleta | Mapa mental da sereia (nome do arquivo como nó raiz) | Lista Markdown aninhada (sem título do documento) |
| **CSV/TSV** | .csv, .tsv | Tabela de descontos ||
| **RTF/RTFD** | .rtf, .rtfd | Markdown via conversão RTF (consulte [Suporte RTF e RTFD](RTF_Support.html)) ||
| **PDF** | .pdf | Markdown via conversão de PDF quando aberto como documento principal (veja [Suporte PDF](PDF_Support.html)) ||

Cada formato de esboço/mapa mental tem sua própria caixa de seleção em *Mapas Mentais/Esboços* (mapas mentais, arquivos OPML, contornos de bicicleta, contornos OmniOutliner). Desativar um formato usa o comportamento "desativado" somente para esse tipo. Consulte [Incorporando mapas mentais e contornos](Embedding_Mind_Maps_and_Outlines.html) para detalhes de formato e [Configurações: Aplicativos][mapas mentais] para alterar essas opções. Para obter detalhes de conversão CSV, consulte [Criando tabelas usando arquivos CSV][csv].

[mindmaps]: Settings_Apps.html#MindMapsOutlines

## Formatos de livros [book-formats]

Marked também suporta arquivos de índice em formatos como [Leanpub][lp], [GitBook][gb] e mmd\_merge (MultiMarkdown). Os arquivos incluídos nos índices de formato de livro serão monitorados em busca de alterações e o resultado será uma visualização completa do documento compilado, assim como o exemplo "Index.md" acima.

###Lean Pub

Se você ativar a opção {% prefspane Apps %} em suporte Leanpub/GitBook, os arquivos chamados "Book.txt" serão tratados como arquivos de índice Leanpub automaticamente. O antigo formato "frontmatter:" também é reconhecido.

[Documentação do Leanpub.][lpdocs]

Exemplo de Leanpub Book.txt:

    assunto inicial:
    Agradecimentos.txt
    Prefácio.txt
    Introdução.txt
    assunto principal:
    Markdown.txt
    Exemplos de livros.txt
    Inserindo Imagens.txt


###mmd_merge

Para mmd\_merge, Marked exige que a primeira linha seja "#merge" (um gatilho especial marcado para mmd\_merge, tratado como um comentário e ignorado por outros processadores).

[documentação mmd_merge.][mmdm]

Exemplo de mmd_merge:

    #mesclar
    metadados.txt
    Capítulo-1.md
        subcapítulo-1-1.md
        subcapítulo-1-2.md
    Capítulo-2.md
        subcapítulo-2-1.md
        subcapítulo-2-2.md
    FAQ.md
    Agradecimentos.md

### GitBook [leanpub]

A formatação do GitBook usa uma lista Markdown para criar a estrutura e o índice. Se o suporte ao GitBook estiver habilitado em {% prefspane Apps %} no suporte Leanpub/GitBook, um arquivo chamado SUMMARY.md será lido e convertido automaticamente para o formato mmd_merge, permitindo uma visualização completa do seu documento GitBook.

[Documentação do GitHub.][gbdocs]

Exemplo GitBook SUMMARY.md:

    # Resumo

    * [Parte I](parte1/README.md)
        * [Escrever é bom](part1/writing.md)
        * [GitBook é legal](part1/gitbook.md)
    * [Parte II](parte2/README.md)
        * [Adoramos feedback](part2/feedback_please.md)
        * [Melhores ferramentas para autores](part2/better_tools.md)

O GitBook permite que âncoras sejam usadas no índice SUMMARY.md, mas Marked as ignorará e incluirá apenas o documento base uma vez.

[gbdocs]: https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md
[lp]: http://leanpub.com/
[lpdocs]: https://leanpub.com/help/manual#leanpub-auto-how-to-set-the-books-structure
[mmdm]: http://fletcher.github.io/peg-multimarkdown/#howdoisplitamultimarkdowndocumentintoseveralparts
[gb]: https://www.gitbook.com/

## Recursos de visualização de documentos com vários arquivos [multi-file-document-preview-features]

![Limites de arquivo incluídos][2]

   [2]: images/includeboundaries.png @2x width=859px height=239px class=center

Ao visualizar um documento contendo arquivos incluídos, você pode usar dois recursos para ajudar a descobrir qual arquivo está visualizando.

* **Teclado:** Pressionar {% kbd shift I %} exibirá brevemente um pop-up mostrando o título do arquivo atualmente visível na posição de rolagem da visualização.
    * Pressionar {% kbd Return %} e {% kbd I %} editará o arquivo exibido com seu editor externo.
* **Rato:** Selecionar "Mostrar limites dos arquivos incluídos" no menu de engrenagem ({% kbd ctrl cmd B %}) adicionará uma barra colorida ao lado esquerdo da visualização, segmentada para mostrar o início e o fim dos arquivos incluídos. Também mostra inclusões aninhadas. Passar o mouse sobre uma seção desta barra mostrará o nome do arquivo que ela representa e clicar nele abrirá esse arquivo no editor escolhido.