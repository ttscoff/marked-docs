# <%= @title %>

O Marked exporta HTML a partir da sua **preview ao vivo** --- a mesma saída renderizada que você vê na tela. Use a exportação em HTML quando precisar de um trecho para colar em um blog ou CMS, ou de um arquivo `.html` autocontido, com estilos e imagens incorporados, que possa ser aberto em qualquer navegador ou hospedado em qualquer lugar.

O fluxo de trabalho típico é **primeiro a preview, depois a exportação em HTML**: abra ou compile seu documento no Marked, escolha um tema, revise na preview ao vivo e então exporte quando a formatação estiver correta.

## Duas formas de obter HTML [two-ways-to-get-html]

### Copiar HTML (trecho) [copy-html-snippet]

**Copiar HTML** coloca o código HTML da preview na área de transferência --- pronto para colar no WordPress, Ghost, Squarespace, um fórum, um modelo de e-mail ou qualquer app que aceite fragmentos de HTML.

* Menu de engrenagem → **Copiar HTML**, ou {% kbd shift cmd C %} com a preview em foco
* Copia o **HTML do corpo renderizado** (não um documento completo com o wrapper `<html>`)
* Opcional: ative **Incorporar imagens ao copiar HTML** em {% prefspane Export %} para codificar imagens locais em Base64 como URLs `data:` no código colado

Copiar HTML é ideal quando o destino já tem sua própria folha de estilos e você só precisa da formatação do conteúdo.

### Salvar HTML (arquivo) [save-html-file]

**Salvar HTML** grava um arquivo `.html` completo no disco.

* Exportar → **Salvar HTML**, {% kbd cmd S %}, ou **HTML** a partir do [Painel de Exportação](Exporting.html#drawer) ({% kbd shift cmd e %})
* Escolha o nome do arquivo e o local na caixa de diálogo de salvamento
* Configure as opções de exportação no acessório da caixa de diálogo (veja abaixo)

Salvar HTML é ideal para arquivamento, para compartilhar um arquivo independente ou para abrir o resultado diretamente em um navegador.

## Opções de Salvar HTML [save-html-options]

A caixa de diálogo Salvar HTML inclui um seletor de perfil de exportação e estas opções:

![Opções de Salvar HTML][savehtml]

**Incluir estilo na saída**

Quando marcada, o Marked incorpora o CSS do tema de preview selecionado em um bloco `<style>` dentro do arquivo exportado. Escolha qualquer tema integrado ou [Estilo Personalizado](Custom_Styles.html) no menu de estilos ao lado da caixa de seleção. A saída é um documento HTML completo com `<!DOCTYPE html>`, `<head>` e uma div `#wrapper` envolvendo seu conteúdo --- igual ao que você viu na preview.

Quando desmarcada, o Marked salva um documento HTML mínimo contendo apenas o conteúdo renderizado (sem o CSS de tema do Marked). Use essa opção quando quiser HTML bruto para colar ou importar em outro sistema que forneça sua própria estilização.

**Incorporar imagens locais para HTML autocontido**

Quando **Incluir estilo na saída** está ativada, você também pode incorporar imagens locais como URLs Base64 `data:` dentro do arquivo HTML. O resultado é um único arquivo que pode ser enviado por e-mail, publicado ou hospedado sem uma pasta `images/` separada.

* Funciona com imagens referenciadas por **caminhos relativos ou absolutos** na sua unidade local
* Evite URLs `file:///` --- elas não podem ser incorporadas de forma confiável
* Imagens remotas (http/https) permanecem como URLs externas, a menos que você as baixe antes
* A incorporação em Base64 pode gerar arquivos grandes; use-a quando a portabilidade for mais importante do que o tamanho do arquivo

**Incluir JavaScript de Realce de Sintaxe**

Quando o realce de sintaxe está ativado em {% prefspane Preview %}, essa opção adiciona o CSS e o JavaScript do highlight.js a partir de uma CDN, para que os blocos de código mantenham as cores no arquivo exportado. O HTML exportado precisa de conexão com a internet para carregar os recursos da CDN.

**Incluir link de CDN do MathJax ou KaTeX**

Quando o [MathJax](MathJax.html) ou o KaTeX está ativado na preview, você pode incluir os scripts de CDN correspondentes no HTML salvo para que as equações sejam renderizadas em um navegador. Assim como o realce de sintaxe, isso exige acesso à rede ao visualizar o arquivo, a menos que você hospede os scripts por conta própria.

**Tipo de exportação do CriticMarkup**

Documentos com [CriticMarkup](CriticMarkup.html) podem escolher se a exportação mostra o texto editado, o texto original ou a marcação completa.

**Perfil de exportação**

Selecione um [Perfil de Exportação](Exporting.html#export-profiles) salvo para restaurar suas configurações preferidas de exportação em HTML (estilos incorporados, imagens, realce de sintaxe, fórmulas matemáticas) em uma única etapa.

## Estilização com temas integrados e personalizados [styling-with-built-in-and-custom-themes]

O **estilo de preview** determina a aparência do HTML quando **Incluir estilo na saída** está marcada:

1. Escolha um estilo no menu de estilos da janela de preview (ou defina um padrão em {% prefspane Style %}).
2. Revise a tipografia, os títulos, os blocos de código e as imagens na preview ao vivo.
3. Salve o HTML com o mesmo estilo selecionado na caixa de diálogo de exportação.

Todo tema integrado do Marked --- Swiss, GitHub, Manuscript e os demais --- pode ser incorporado. [Estilos Personalizados](Custom_Styles.html) e estilos do [Gerenciador de Estilos](Custom_Styles.html) funcionam da mesma forma.

O **CSS Adicional** de {% prefspane Style %} é incluído na exportação em HTML quando os estilos são incorporados. O `<body>` exportado recebe a classe `mk-has-additional-css` para que os seletores de CSS Adicional reescritos pelo Marked correspondam corretamente. Veja [Criando CSS Personalizado](Writing_Custom_CSS.html#additional-css-settings).

I> Alguns CSS exclusivos da preview (posicionamento fixo, truques de viewport, inversão do Modo Escuro `@media screen`) podem não se traduzir perfeitamente fora do Marked. Abra o arquivo salvo em um navegador para conferir antes de publicar.

Para orientações sobre criação, veja [Criando CSS Personalizado](Writing_Custom_CSS.html).

## Metadados e cabeçalhos MultiMarkdown [metadata-and-multimarkdown-headers]

Metadados do MultiMarkdown no topo do arquivo de origem podem afetar a exportação em HTML:

* **`Title:`** --- usado no elemento `<title>` ao salvar um documento HTML completo
* **`XHTML Header:`** / **`HTML Header:`** --- injeta tags adicionais no `<head>` exportado (scripts, tags link, meta tags)
* Outras chaves de metadados são processadas de acordo com o seu [processador Markdown](Choosing_a_Processor.html)

Se você usa metadados para configurações de exportação, mas não quer que as chaves fiquem visíveis em outras saídas, envolva-as em comentários HTML --- o Marked encontra e processa metadados comentados em qualquer parte do documento. Veja [Configurações por Documento](Per-Document_Settings.html).

## Documentos com múltiplos arquivos [multi-file-documents]

Para livros e compilações de capítulos, use [Documentos com Múltiplos Arquivos](Multi-File_Documents.html). O Marked visualiza o documento combinado e exporta um único arquivo HTML a partir do resultado compilado. Os arquivos incluídos são marcados com comentários HTML mostrando seus caminhos de origem --- útil para verificar qual capítulo contribuiu com qual seção.

## Colando em outros aplicativos [pasting-into-other-applications]

| Destino | Abordagem sugerida |
| :-- | :-- |
| Blog / CMS com tema próprio | **Copiar HTML** (trecho, sem CSS do Marked incorporado) |
| Site estático ou arquivamento | **Salvar HTML** com **Incluir estilo na saída** |
| E-mail ou compartilhamento de arquivo (um anexo) | **Salvar HTML** com **Incorporar imagens locais** |
| WordPress, Ghost, Notion, etc. | **Copiar HTML**; ative **Incorporar imagens ao copiar HTML** se o editor não resolver caminhos locais |
| Edição adicional em um editor de código | **Salvar HTML** sem estilo incorporado, ou copie o trecho e envolva manualmente |

[Copiar Texto Formatado](Exporting.html#rtfexportoptions) (menu de engrenagem) é uma alternativa quando o app de destino aceita texto formatado em vez de código HTML.

## Tópicos relacionados [related-topics]

* [Exportando](Exporting.html) --- painel de exportação, perfis e outros formatos
* [Exportação em EPUB](EPUB_Export.html) --- saída em e-book com CSS incorporado
* [Preview de Markdown ao Vivo no Mac](Live_Markdown_Preview_on_Mac.html) --- fluxo de trabalho de preview antes da exportação
* [Estilos Personalizados](Custom_Styles.html) e [Configurações: Exportar](Settings_Export.html)
* [Configurações Específicas de HTML](HTML_Specific_Settings.html) --- opções do processador para saída em HTML
* [Exportação via AppleScript](AppleScript_Support.html) --- automatize a cópia e o salvamento em HTML

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
