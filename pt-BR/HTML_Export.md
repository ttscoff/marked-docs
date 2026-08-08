<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado exporta HTML da sua **visualização ao vivo** --- a mesma saída renderizada que você vê na tela. Use a exportação HTML quando precisar de um snippet para colar em um blog ou CMS, ou um arquivo `.html` independente com estilos e imagens incorporados que você pode abrir em qualquer navegador ou host em qualquer lugar.

O fluxo de trabalho típico é **visualizar primeiro, depois exportar HTML**: abrir ou compilar seu documento no Marked, escolher um tema, revisar na visualização ao vivo e exportar quando a marcação estiver correta.

## Duas maneiras de obter HTML [two-ways-to-get-html]

### Copiar HTML (snippet) [copy-html-snippet]

**Copiar HTML** coloca o código-fonte HTML da visualização na área de transferência --- pronto para colar no WordPress, Ghost, Squarespace, um fórum, um modelo de e-mail ou qualquer aplicativo que aceite fragmentos de HTML.

* Menu de engrenagem → **Copiar HTML** ou {% kbd shift cmd C %} com a visualização em foco
* Copia o **HTML do corpo renderizado** (não um documento completo com wrapper `<html>`)
* Opcional: habilite **Incorporar imagens ao copiar HTML** em {% prefspane Export %} para imagens locais codificadas em Base64 como `data:` URLs na fonte colada

Copiar HTML é ideal quando seu destino já possui sua própria folha de estilo e você só precisa da marcação do conteúdo.

### Salvar HTML (arquivo) [save-html-file]

**Salvar HTML** grava um arquivo `.html` completo no disco.

* Exportar → **Salvar HTML**, {% kbd cmd S %} ou **HTML** no [Painel de exportação](Exporting.html#drawer) ({% kbd shift cmd e %})
* Escolha o nome do arquivo e o local na caixa de diálogo salvar
* Configure as opções de exportação no acessório de diálogo (veja abaixo)

Salvar HTML é ideal para arquivar, compartilhar um arquivo independente ou abrir o resultado diretamente em um navegador.

## Salvar opções de HTML [save-html-options]

A caixa de diálogo Salvar HTML inclui um seletor de perfil de exportação e estas opções:

![Opções de salvar HTML][savehtml]

**Incluir estilo na saída**

Quando marcado, Marcado incorpora o CSS do tema de visualização selecionado em um bloco `<style>` dentro do arquivo exportado. Escolha qualquer tema integrado ou [Estilo personalizado](Custom_Styles.html) no menu de estilo próximo à caixa de seleção. A saída é um documento HTML completo com `<!DOCTYPE html>`, `<head>` e um `#wrapper` div em torno do seu conteúdo --- correspondendo ao que você visualizou.

Quando desmarcado, Marcado salva um documento HTML mínimo apenas com seu conteúdo renderizado (sem CSS de tema Marcado). Use isto quando desejar que o HTML bruto seja colado ou importado para outro sistema que forneça seu próprio estilo.

**Incorpore imagens locais para HTML independente**

Quando **Incluir estilo na saída** está ativado, você também pode incorporar imagens locais como URLs Base64 `data:` dentro do arquivo HTML. O resultado é um único arquivo que você pode enviar por e-mail, fazer upload ou hospedar sem uma pasta `images/` separada.

* Funciona com imagens referenciadas por **caminhos relativos ou absolutos** na sua unidade local
* Evite `file:///` URLs --- eles não podem ser incorporados de forma confiável
* Imagens remotas (http/https) permanecem como URLs externos, a menos que você as baixe primeiro
* A incorporação Base64 pode produzir arquivos grandes; use-o quando a portabilidade for mais importante do que o tamanho do arquivo

**Incluir JavaScript de realce de sintaxe**

Quando o realce de sintaxe está habilitado em {% prefspane Preview %}, esta opção adiciona CSS e JavaScript destaque.js de um CDN para que os blocos de código mantenham suas cores no arquivo exportado. O HTML exportado precisa de uma conexão com a Internet para que os recursos CDN sejam carregados.

**Incluir link MathJax ou KaTeX CDN**

Quando [MathJax](MathJax.html) ou KaTeX está ativado para visualização, você pode incluir os scripts CDN correspondentes no HTML salvo para que as equações sejam renderizadas em um navegador. Assim como o realce de sintaxe, isso requer acesso à rede ao visualizar o arquivo, a menos que você mesmo hospede os scripts.

**Tipo de exportação CriticMarkup**

Documentos com [CriticMarkup](CriticMarkup.html) podem escolher se a exportação mostra texto editado, texto original ou marcação completa.

**Exportar perfil**

Selecione um [Perfil de exportação](Exporting.html#export-profiles) salvo para restaurar suas configurações de exportação HTML preferidas (estilos incorporados, imagens, realce de sintaxe, matemática) em uma única etapa.

## Estilo com temas integrados e personalizados [styling-with-built-in-and-custom-themes]

O **estilo de visualização** gera a aparência do HTML quando **Incluir estilo na saída** está marcado:

1. Escolha um estilo no menu de estilos da janela de visualização (ou defina um padrão em {% prefspane Style %}).
2. Revise tipografia, títulos, blocos de código e imagens na visualização ao vivo.
3. Salve o HTML com o mesmo estilo selecionado na caixa de diálogo de exportação.

Cada tema marcado integrado --- Swiss, GitHub, Manuscript e o resto --- pode ser incorporado. [Estilos personalizados](Custom_Styles.html) e estilos do [Gerenciador de estilos](Custom_Styles.html) funcionam da mesma maneira.

I> Alguns CSS somente de visualização (posicionamento fixo, truques de janela de visualização, modo escuro `@media screen` inversão) podem não ser traduzidos um para um fora do Marcado. Abra o arquivo salvo em um navegador para verificar antes de publicar.

Para orientação de autoria, consulte [Criando CSS personalizado](Writing_Custom_CSS.html).

## Metadados e cabeçalhos MultiMarkdown [metadata-and-multimarkdown-headers]

Os metadados MultiMarkdown na parte superior do seu arquivo de origem podem afetar a exportação de HTML:

* **`Title:`** --- usado para o elemento `<title>` ao salvar um documento HTML completo
* **`XHTML Header:`** / **`HTML Header:`** --- injeta tags adicionais no `<head>` exportado (scripts, tags de link, meta tags)
* Outras chaves de metadados são processadas de acordo com seu [processador Markdown](Choosing_a_Processor.html)

Se você usa metadados para configurações de exportação, mas não deseja que as chaves fiquem visíveis em outras saídas, envolva-as em comentários HTML --- Marcado localiza e processa metadados comentados em qualquer lugar do documento. Consulte [Configurações por documento](Per-Document_Settings.html).

## Documentos com vários arquivos [multi-file-documents]

Para compilações de livros e capítulos, use [Documentos de vários arquivos](Multi-File_Documents.html). Marcado visualiza o documento mesclado e exporta um arquivo HTML do resultado compilado. Os arquivos incluídos são marcados com comentários HTML mostrando seus caminhos de origem – útil ao auditar qual capítulo contribuiu com qual seção.

## Colando em outros aplicativos [pasting-into-other-applications]

| Destino | Abordagem sugerida |
| :-- | :-- |
| Blog/CMS com tema próprio | **Copiar HTML** (snippet, sem CSS marcado incorporado) |
| Site estático ou arquivo | **Salve HTML** com **Incluir estilo na saída** |
| E-mail ou compartilhamento de arquivo (um anexo) | **Salve HTML** com **Incorpore imagens locais** |
| WordPress, Ghost, Noção, etc. | **Copiar HTML**; habilite **Incorporar imagens ao copiar HTML** se o editor não resolver caminhos locais |
| Edição adicional em um editor de código | **Salve HTML** sem estilo incorporado ou copie o snippet e ajuste manualmente |

[Copiar Rich Text](Exporting.html#rtfexportoptions) (menu de engrenagem) é uma alternativa quando o aplicativo de destino aceita texto formatado em vez de fonte HTML.

## Tópicos relacionados [related-topics]

* [Exportando](Exporting.html) --- painel de exportação, perfis e outros formatos
* [Exportação de EPUB](EPUB_Export.html) --- saída de e-book com CSS incorporado
* [Live Markdown Preview no Mac](Live_Markdown_Preview_on_Mac.html) --- visualizar o fluxo de trabalho antes de exportar
* [Estilos personalizados](Custom_Styles.html) e [Configurações: Exportar](Settings_Export.html)
* [Configurações específicas de HTML](HTML_Specific_Settings.html) --- opções de processador para saída HTML
* [Exportação AppleScript](AppleScript_Support.html) --- automatizar cópia e salvar HTML

[savehtml]: images/SaveHTML.png @2x width=740px height=229px 
R