<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked exporta arquivos EPUB totalmente compatíveis da visualização do Markdown --- estilizados com os mesmos temas integrados e personalizados que você usa na tela e legíveis em **Apple Books**, **Kobo** e outros leitores EPUB padrão.

O fluxo de trabalho típico é **visualizar primeiro, depois exportar EPUB**: abrir ou compilar seu documento no Marked, escolher um tema, revisar na visualização ao vivo e exportar quando o livro estiver pronto.

## Exportando um EPUB

Abra o [Painel de exportação](Exporting.html#drawer) ({% kbd shift cmd e %}) ou use **Salvar como** no menu de engrenagem e escolha **EPUB**.

A caixa de diálogo para salvar EPUB permite definir:

* **Título** --- o padrão é metadados MultiMarkdown ou o nome do arquivo
* **Autor** --- o padrão é seu nome de usuário do macOS; o último autor inserido será lembrado para a próxima exportação
* **Data** --- Formato ISO; editável na hora de salvar
* **Imagem da capa** --- PNG ou JPG opcional; Marcado gera uma visualização de capa padrão quando nenhuma está definida

Marked incorpora imagens locais no EPUB e pode baixar imagens remotas para que o arquivo finalizado seja independente. Os EPUBs exportados são validados como XHTML bem formados antes de serem salvos, produzindo arquivos que atendem aos padrões EPUB para distribuição e acessibilidade.

Consulte [Exportar perfis](Exporting.html#export-profiles) para salvar metadados EPUB e exportar configurações para uso repetido.

## Estilo com temas integrados

O **estilo de visualização** selecionado para o seu documento gera a aparência do EPUB. Cada tema marcado integrado --- Swiss, GitHub, Manuscript e o resto --- pode ser aplicado à exportação de EPUB.

1. Escolha um estilo no menu Estilo da janela de visualização (ou defina um padrão em {% prefspane Style %}).
2. Revise tipografia, títulos, blocos de código e imagens na visualização ao vivo.
3. Exportar para EPUB --- Marcado agrupa o CSS do tema no pacote EPUB.

Marcado também aplica CSS específico de exportação sobre seu tema de visualização para que elementos como notas de rodapé, tabelas e blocos de código realçados por sintaxe sejam renderizados corretamente em leitores eletrônicos. Documentos no modo de estrutura de tópicos usam estilos de exportação otimizados para estrutura de tópicos; Os índices [Leanpub](Multi-File_Documents.html) `Book.txt` usam o estilo de exportação orientado ao Leanpub automaticamente.

I> Os leitores de EPUB ignoram alguns CSS somente da web (posicionamento fixo, truques de janela de visualização, etc.). O que você vê na visualização do Marked é o objetivo, mas os mecanismos de layout do e-reader podem simplificar o espaçamento e as fontes. Teste no Apple Books ou no seu leitor alvo antes de publicar.

## Estilo com temas personalizados

[Estilos personalizados](Custom_Styles.html) funcionam da mesma maneira para EPUB e para visualização e PDF:

* Adicione arquivos CSS em {% prefspane Style %} ou no [Style Manager](Custom_Styles.html).
* Selecione o tema personalizado antes de exportar.
* Marcado incorpora sua folha de estilo no EPUB exportado.

Dicas para CSS personalizado compatível com EPUB:

* Mantenha os layouts fluidos --- use unidades relativas e `max-width: 100%` nas imagens (`#wrapper img { max-width: 100%; }` é uma boa linha de base).
* Evite `@media print` regras para estilo de e-book; EPUB usa os estilos de tela principal mais a folha de estilo de exportação do Marked.
* [Modo Escuro](Previewing.html) inversão na visualização usa `@media screen` consultas; a maioria dos leitores EPUB usa a folha de estilo clara, a menos que o aplicativo leitor aplique seu próprio tema escuro.
* Use [CSS adicional](Custom_Styles.html) nas configurações de estilo para ajustar todos os temas de uma vez (por exemplo, tamanho uniforme da fonte do corpo nas exportações).

Para orientação de autoria, consulte [Criando CSS personalizado](Writing_Custom_CSS.html).

## Destaque de sintaxe e matemática

Se **Incluir destaque de sintaxe na exportação** estiver habilitado em {% prefspane Export %}, os blocos de código serão exportados com as mesmas cores de sintaxe da sua visualização. A matemática renderizada com [MathJax](MathJax.html) está incluída no EPUB conforme apropriado para suporte ao leitor eletrônico.

## Metadados no seu arquivo de origem

Você pode definir metadados EPUB no documento em vez da caixa de diálogo para salvar. Na parte superior de um arquivo Markdown (ou em uma página de metadados do Scrivener), use chaves no estilo MultiMarkdown:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

`cover image` aceita um caminho relativo ao documento ou um caminho absoluto. PNG e JPG são suportados. Os valores da caixa de diálogo substituem ou preenchem os metadados ausentes no momento da exportação.

## Livros com vários arquivos

Para trabalhos longos, compile capítulos com [Documentos Multi-Arquivos](Multi-File_Documents.html) --- arquivos de índice, exportações do Scrivener, Leanpub `Book.txt` ou índices estilo GitBook. Marcado observa arquivos incluídos, visualiza o livro completo e exporta um EPUB do HTML compilado.

Os títulos do documento compilado tornam-se o EPUB [índice](Document_Navigation.html) para navegação no Apple Books e outros leitores.

## Leitura e publicação

Os EPUBs exportados abrem diretamente no **Apple Books** (clique duas vezes no arquivo ou use **Arquivo → Adicionar à biblioteca**). Eles também funcionam em Kobo, Thorium, Caliber e na maioria dos aplicativos compatíveis com EPUB 3.

### Apple Livros

Arraste um `.epub` exportado para o aplicativo Livros ou adicione-o através de **Arquivo → Importar**. A tipografia personalizada e a arte da capa do seu tema marcado são executadas. Use o Apple Books no Mac, iPad ou iPhone para verificar o layout antes de compartilhar.

### Publicação direta Kindle (KDP)

EPUB é um formato de upload aceito para [Kindle Direct Publishing](https://kdp.amazon.com/). Exporte de Marked e carregue o arquivo `.epub`; A Amazon o converte para entrega no Kindle. O KDP também aceita [DOCX](Working_with_DOCX.html). Consulte [formatos de e-books suportados](https://kdp.amazon.com/en_US/help/topic/G200634390) da Amazon para obter os requisitos atuais.

**MOBI não é necessário** para novos títulos KDP. Marcado não exporta MOBI.

Opcional: visualize o layout do Kindle com o [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) gratuito da Amazon antes de fazer o upload.

## Relacionado

* [Exportação de HTML](HTML_Export.html) --- HTML autônomo com estilos e imagens incorporados
* [Exportando](Exporting.html) --- painel de exportação, perfis e outros formatos
* [Live Markdown Preview no Mac](Live_Markdown_Preview_on_Mac.html) --- visualizar o fluxo de trabalho antes de exportar
* [Estilos personalizados](Custom_Styles.html) e [Gerador de estilo personalizado](Custom_Style_Generator.html)
* [Documentos com vários arquivos](Multi-File_Documents.html) --- livros e índices de capítulos
* [Exportação AppleScript](AppleScript_Support.html) --- automatizar a exportação de EPUB