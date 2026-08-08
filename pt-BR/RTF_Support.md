<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado pode abrir documentos Rich Text Format (`.rtf`) e RTFD (`.rtfd`) diretamente. Arraste um arquivo para Marcado ou use {% appmenu File, Open... ({{cmd}}O) %}. O documento é convertido em Markdown para visualização e exportação.

Isso funciona bem com documentos do **Pages**, **TextEdit**, **Word** e outros aplicativos que salvam RTF ou RTFD. Marcado ainda é uma ferramenta de **visualização**: você edita no aplicativo original e Marcado atualiza quando salva.

## Como funciona a conversão [how-conversion-works]

Marcado converte RTF em HTML usando o mecanismo de texto do sistema e depois em Markdown. O conversor:

- Mapeia **tamanhos de fonte de parágrafo grande** para níveis de título (em relação ao tamanho de corpo mais comum no documento)
- Preserva **negrito**, *itálico* e links sempre que possível
- Extrai **imagens** de pacotes RTFD e anexos incorporados
- **não** trata nomes de arquivos RTF como legendas de imagens (veja imagens abaixo)

O mesmo pipeline de conversão é usado para compilação RTF do Scrivener e para arquivos RTF incluídos em outros documentos.

## Visualização ao vivo [live-preview]

Quando você salva o arquivo RTF ou RTFD em outro aplicativo, o Marked detecta a alteração e atualiza a visualização automaticamente.

## Imagens [images]

O RTF não define um campo de "legenda" separado da forma como o Cocoa exporta para HTML. O que parece ser uma legenda em seu layout geralmente é **texto normal** no próximo parágrafo, e Marcado mantém isso como corpo de texto.

Imagens incorporadas e imagens dentro de pacotes RTFD (por exemplo, `pastedGraphic.png` em uma exportação de páginas) são copiadas para uma pasta de cache em `~/Library/Caches/Marked/Watchers/`. Os caminhos da imagem de visualização apontam para esses arquivos em cache até você exportar.

Marcado **não** usa o nome do arquivo da imagem como texto alternativo ou legenda de figura MultiMarkdown. Você não deverá ver `pastedGraphic.png` abaixo da imagem, a menos que tenha digitado esse texto no documento.

## Exportação e outros recursos [export-and-other-features]

Após a conversão, Marked trata o documento como outras fontes compiladas (semelhante a [Scrivener](Scrivener_Support.html) e [DOCX](Working_With_DOCX.html)): exportação, estatísticas e a maioria dos recursos de visualização são executados no Markdown gerado armazenado no cache do Watchers.

## Limitações [limitations]

A qualidade da conversão depende do aplicativo de origem. Em geral:

- **Títulos** são inferidos pelo tamanho da fonte, não pelos estilos de contorno do Word/Páginas
- **Layout complexo** (tabelas com múltiplas colunas usadas apenas para posicionamento, caixas de texto) podem não ser mapeadas corretamente para Markdown
- **Equações** em RTF não são suportadas na visualização (veja [MathJax](MathJax.html) para matemática Markdown)
- **Legacy `.doc`** (Word binário) não é suportado; salve como DOCX ou RTF primeiro

Para colar uma única vez sem salvar um arquivo, use [Pré-visualização da área de transferência](Opening_Files.html#from-the-clipboard).

## Tópicos relacionados [related-topics]

- [Suporte PDF](PDF_Support.html) - abra documentos PDF como fontes Markdown
- [Trabalhando com DOCX](Working_With_DOCX.html) -- Documentos Word com controle de alterações e comentários
- [Abrindo arquivos](Opening_Files.html) -- arrastar e soltar, Abrir recente, área de transferência
- [Exportando](Exporting.html) -- Copie Rich Text e salve RTFD (exportação), diferente de abrir RTF como arquivo de origem