<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Se um arquivo incluído por meio de [sintaxe de inclusão do Marked ou sintaxe de bloco do IA Writer] [include] tiver uma extensão CSV ou TSV, o Marked tentará analisá-lo e convertê-lo em uma tabela MultiMarkdown. Isso funciona com a maioria dos formatos padrão, incluindo separado por vírgula e tabulação, bem como separadores adicionais e formatos de cotação que são detectados automaticamente.

Um benefício de usar arquivos CSV em vez de escrever tabelas Markdown é que as quebras de linha nas células são automaticamente convertidas em tags `<br>`. Isso deve ser feito manualmente para incluir quebras de linha ao escrever tabelas MultiMarkdown, portanto, economiza tempo adicional.

Como observação lateral, existe um excelente aplicativo chamado [TableFlip][] que facilita muito a edição de tabelas em seu documento. Vale a pena conferir se você trabalha frequentemente com dados tabulares.

Os arquivos CSV incluídos serão monitorados em busca de alterações, portanto, edições adicionais podem ser feitas no arquivo CSV original e Marcado atualizará automaticamente a visualização ao salvar.

As tabelas convertidas serão incluídas na exportação do Markdown, portanto o Marked pode ser usado para compilar documentos contendo dados estruturados e exportar um único arquivo.

[include]: Multi-File_Documents.html
[TableFlip]: http://tableflipapp.com/