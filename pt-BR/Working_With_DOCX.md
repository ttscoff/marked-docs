<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked possui amplo suporte para trabalhar com arquivos do Microsoft Word. O fluxo de trabalho típico é **visualizar primeiro, exportar DOCX depois**: abrir ou assistir seu Markdown em Marcado, refinar estilos e revisão na visualização ao vivo e, em seguida, exportar para Word quando o documento estiver pronto.

## Abrindo arquivos DOCX

Marcado pode ler um arquivo DOCX e convertê-lo em limpo
Remarcação. Elementos de estilo válidos, como títulos e listas,
ser convertido em seu equivalente Markdown.

O rastreamento de alterações e os comentários serão convertidos em
Marcação Crítica. Os destaques serão convertidos em tags `<mark>`,
com cores quando apropriado.

## Exportando arquivos DOCX

Use a paleta Exportar para gerar um arquivo DOCX a partir do seu
Remarcação. Na caixa de diálogo salvar, você pode especificar um arquivo integrado
estilos --- este estilo pode ser facilmente alterado no Word apenas por
abrindo o seletor de tema e selecionando um novo tema.

### Cabeçalhos e rodapés

Se você configurar cabeçalhos e rodapés em {% prefspane Export %}, eles serão incluídos no DOCX exportado. Espaços reservados padrão como `%title`, `%date`, `%page` e `%total` são substituídos no momento da exportação. `%logo` e `%image` incorporam o logotipo nas preferências de Cabeçalho/Rodapé. `%md_*` variáveis ​​de metadados são resolvidas a partir dos metadados MultiMarkdown do documento. `%h1`--`%h6` tornam-se campos do Word **STYLEREF** vinculados aos estilos de título exportados; O Word os preenche quando você abre o documento. Veja [Exportando](Exporting.html#headers-and-footers) para a lista completa de variáveis ​​e diferenças entre o comportamento de DOCX e impressão/PDF.

## Rastreamento de alterações

A sintaxe CriticMarkup em um documento Markdown será convertida
para Word Change Tracking quando exportado para DOCX. Comentários
seguintes inserções, exclusões e substituições serão
aparecem na coluna da direita no Word quando o controle de alterações
está habilitado.

Ao importar um arquivo DOCX no Marked, o controle de alterações será
ser convertido em tags CriticMarkup e `<mark>` como
apropriado.

## Matemática

As equações MathJax e Katex exibidas no documento serão convertidas em MathML para exibição no Word. Esta conversão não é perfeita, mas na maioria dos casos renderizará um bloco matemático válido no documento do Word. Isso se aplica apenas à exportação --- os blocos matemáticos em documentos do Word não serão convertidos durante a importação.

## Adicionando estilos de exportação personalizados

Você pode adicionar seus próprios estilos de exportação incluindo um modelo e um arquivo estilos.xml em `~/Library/Application Support/Marked/Custom Word Styles/`. Para criá-los:

1. Abra um arquivo DOCX gerado por Marcado no Word
2. Edite os estilos no editor de estilos para cada elemento, selecionando "Adicionar ao modelo" para cada um.
3. Salve o arquivo DOCX.
4. Gere um modelo acessando **Design** na barra superior e, no menu suspenso *Modelo* à esquerda, clique em **Salvar modelo atual**. Nomeie-o como deseja que apareça no menu Estilo marcado e salve-o em `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx`, onde `STYLENAME` é o nome do seu estilo.
5. Vá para o Finder e localize o arquivo DOCX que você salvou do Word. Duplique-o e renomeie a cópia para `FILENAME.zip` e clique duas vezes para descompactar.
6. No documento descompactado, você verá uma pasta “word” contendo um arquivo estilos.xml. Copie esse arquivo estilos.xml para a mesma pasta acima e nomeie-o `STYLENAME.xml` (onde `STYLENAME` é o nome do seu estilo). Os arquivos `.thmx` e `.xml` devem ter o mesmo nome base (apenas extensões diferentes).

Na próxima vez que você exportar um DOCX do Marcado, verá seu novo estilo no menu Estilo da caixa de diálogo Salvar.