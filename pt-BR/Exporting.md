<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Transformando seu Markdown em um documento finalizado.

## Exportar após visualização

A visualização do Marked é a base para a exportação --- o que você vê na janela de visualização é o que você obtém em PDF, DOCX, EPUB e outros formatos (configurações específicas de exportação do módulo, como margens, cabeçalhos e paginação). Configure seu estilo e revise primeiro na visualização e depois exporte quando o documento estiver pronto. Consulte [Live Markdown Preview no Mac](Live_Markdown_Preview_on_Mac.html) para obter o fluxo de trabalho de visualização completo.

## O Painel de Exportação [gaveta]

![Painel de exportação][painel de exportação]

O **Painel de Exportação** é um painel estilo holofote controlado por teclado que fornece acesso rápido a todas as opções de exportação. Abra-o clicando no ícone de exportação na barra de status ou pressionando {% kbd shift cmd e %}.

![Botão Exportar][expbut]

O painel de exportação permite que você salve seu documento como HTML, PDF de página única, PDF paginado, pacote RTF ou arquivo DOC ou DOCX do Microsoft Word. Você também pode salvar em um novo arquivo Markdown (recursos específicos marcados serão renderizados e seus resultados incluídos), um documento aberto (ODT) ou como OPML para uso em outros aplicativos.

## Copiar HTML

Use o recurso Copiar HTML para colocar o código-fonte HTML da sua visualização na área de transferência sem complicações. Você pode selecioná-lo no menu de engrenagem ou simplesmente clicar em {% kbd shift cmd C %}. O HTML copiado será um snippet pronto para inserção em um blog, fórum ou documento HTML.

Você não precisa estar na visualização de origem para copiar. Com a visualização focada (clique nela), basta digitar {% kbd shift cmd C %} e você verá uma mensagem pop-up informando que a fonte está na sua área de transferência.

## Salvar HTML

![][exportarhtmlacessório]



O comando Salvar HTML – acessível no menu de engrenagem ou simplesmente digitando **{% kbd cmd S %}** – permitirá que você salve um documento completo pronto para compartilhamento ou publicação.

Opcionalmente, você pode incluir qualquer um dos estilos do Marked (ou um de seus [estilos personalizados][personalizados]) em sua exportação, fornecendo um documento pronto para uso com a formatação necessária já incorporada.

Além disso, você pode optar por incorporar quaisquer imagens locais incluídas no documento no HTML exportado, permitindo que você tenha um documento independente que pode ser hospedado em qualquer lugar sem a necessidade de mover as imagens com ele. Isso só funciona com imagens referenciadas na sua unidade local com caminhos relativos ou absolutos. Evite usar caminhos `file:///` se quiser usar esse recurso.

## Exportar Markdown para PDF no Mac

Visualização de impressão/PDF ({% kbd cmd P %}) abrirá uma caixa de diálogo de impressão padrão. Cada estilo de visualização em Marcado tem seus próprios estilos de impressão que removem fundos, modificam tamanhos de tipo e fornecem bordas. A visualização será impressa com base no estilo atualmente selecionado.

Em destaque na caixa de diálogo de impressão estão os botões PDF e Visualização. O PDF oferece uma variedade de opções para exportar para PDF (com base nos aplicativos disponíveis) e o Preview exporta uma versão em PDF diretamente para Preview.app, onde você pode salvá-la ou enviá-la por e-mail.

Imprimir em PDF usando este método incluirá paginação. Ao imprimir em papel ou PDF, as quebras de página podem ser inseridas manualmente usando a [sintaxe `<!--BREAK-->`][quebra] ou definindo opções em {% prefspane Export %} para usar cabeçalhos de nível um e/ou nível dois como divisores de seção.

Também há preferência por transformar linhas horizontais (`<hr>`) em quebras de página durante a impressão. Fazer isso substituirá a linha criada pela tag por uma quebra de página, removendo-a da saída final. A visualização não é afetada por esta configuração.

![Margens de impressão][margens de impressão]

As margens da página podem ser definidas em {% prefspane Export %} e afetarão a saída de PDF impresso e paginado.

Você pode substituir as configurações de margem por documento usando a chave de metadados `Margins:`. Os valores são interpretados como pontos; sufixos de unidade como `px`, `pt` e `em` são ignorados. Use dois números para margens verticais e horizontais (`10 20`) ou quatro números para superior, direita, inferior e esquerda (`10, 20, 10, 20` ou `10 20 10 20`). As margens de metadados substituem as configurações {% prefspane Export %}.

### Cabeçalhos e rodapés

Cabeçalhos e rodapés definidos em {% prefspane Export %} aparecerão na parte superior e inferior de qualquer página impressa ou salva em PDF paginado e na exportação DOCX. Você pode colocar qualquer texto no canto superior esquerdo, no centro superior, no canto superior direito, no canto inferior esquerdo, no centro inferior e no canto inferior direito. O texto central é alinhado ao centro da página. As seguintes variáveis serão substituídas nas strings, se usadas:

    %título = Título do Documento
    %data = Data Atual
    %tempo = Hora Atual
    %page = Número da página atual
    %total = número total de páginas
    %path = Caminho do sistema de arquivos para o documento
    %filename = Apenas o nome do arquivo do documento
    %basename = O nome do arquivo sem extensão
    %logo/%image = Um logotipo definido na imagem nas preferências de Cabeçalho/Rodapé
    %%(text) = Texto para imprimir apenas na primeira página
    %h1/h2/h3/h4/h5/h6 = Títulos de seção baseados em cabeçalhos Markdown
    %sep(X) = Texto a ser colocado entre os títulos das seções se existir uma subseção

**Impressão e PDF paginado** resolve `%h1`--`%h6` usando a paginação de Marked, para que cada página mostre a hierarquia de títulos visível naquela página. Variáveis ​​de metadados `%sep(X)` e `%md_*` também são suportadas na saída impressa/PDF.

**Exportação DOCX** incorpora `%logo`/`%image` no cabeçalho ou rodapé do Word (dimensionado para cerca de 50px de altura, correspondendo à visualização de impressão). Os espaços reservados de título tornam-se campos do Word **STYLEREF** que fazem referência aos estilos `Heading 1`--`Heading 6` exportados. O Word atualiza esses campos quando o documento é aberto, com base no layout e nas quebras de página do próprio Word - não na paginação de visualização do Marked. `%md_*` variáveis ​​de metadados são substituídas uma vez no momento da exportação, da mesma forma que na impressão/PDF. `%sep(X)` não é convertido em cabeçalhos/rodapés DOCX.

`%title` usará qualquer informação de "Título:" definida nos cabeçalhos de metadados do MultiMarkdown, caso contrário, retornará ao nome do arquivo sem a extensão do arquivo. Para definir um título usando metadados MMD, coloque o seguinte na primeira linha do documento:

    Título: O título do seu documento

Siga a linha com uma linha em branco (ou qualquer outro metadado que você queira definir, seguido por uma linha em branco).

Você também pode usar qualquer chave de metadados MMD como uma variável prefixando-a com `%md_` e combinando as palavras da chave como uma string minúscula. Por exemplo, se o seu documento tiver uma chave de metadados na parte superior, como:

    Macaco Funky: O macaco mais descolado

Então, usar `%md_funkymonkey` em um campo de cabeçalho colocaria "O macaco mais descolado" no documento exportado no local desse cabeçalho. Os documentos que não contêm essa chave específica deixarão o campo em branco, permitindo adicionar cabeçalhos seletivamente com base nos metadados.

Consulte [Formatos de data e hora](Exporting.html#dateandtimeformats) para códigos de formato `%date` e `%time`.

A configuração "Deslocamento da numeração de páginas" pode ser usada para ajustar o número em que os números das páginas começam. Por exemplo, se você tiver um índice na primeira página e quiser que a numeração comece na segunda página como página 1, defina o deslocamento como -1. A página 2 agora será a página 1 no cabeçalho/rodapé (`%page`) e o total de páginas (`%total`) será ajustado de acordo.

Você também pode especificar uma fonte de cabeçalho/rodapé para um documento específico usando metadados MMD na parte superior do arquivo:

    Fonte do cabeçalho: Mensch

Observe que se você usar um nome de família de fontes, uma fonte padrão será selecionada. Você pode especificar uma variação usando o nome do sistema da fonte. Por exemplo, no caso de Helvetica Neue Ultralight, você usaria "Header Font: HelveticaNeueUltralight".

Além disso, você pode especificar um tamanho de fonte de cabeçalho/rodapé por documento com os metadados:

    Tamanho da fonte do cabeçalho: 10

### Formatos de data e hora

Os campos **Formato de data** e **Formato de hora** em {% prefspane Export %} controlam como `%date` e `%time` são renderizados em cabeçalhos e rodapés. Ambos os campos usam códigos de formato no estilo strftime: um `%` seguido por uma letra. Texto literal (como `-`, `:` ou espaços) é copiado como está.

**Exemplos**

    %m-%d-%Y → 20/06/2026 (formato de data padrão marcado)
    %I:%M %p → 15h45 (formato de hora padrão marcado)
    %Y-%m-%d → 20/06/2026
    %B %d, %Y → 20 de junho de 2026
    %a %H:%M → Sex 15:45

**Códigos de formato comuns**

| Código | Exemplo | Descrição |
| ---- | ------- | ----------- |
| `%Y` | 2026 | Ano de quatro dígitos |
| `%y` | 26 | Ano de dois dígitos |
| `%m` | 06 | Mês (01--12) |
| `%B` | Junho | Nome completo do mês |
| `%b` | junho | Nome abreviado do mês |
| `%d` | 20 | Dia do mês (01--31) |
| `%e` | 20 | Dia do mês (preenchido com espaço) |
| `%A` | Sexta-feira | Nome completo do dia da semana |
| `%a` | Sex | Nome abreviado do dia da semana |
| `%H` | 15 | Hora, 24 horas (00--23) |
| `%I` | 03 | Hora, 12 horas (01--12) |
| `%M` | 45 | Minuto (00--59) |
| `%S` | 07 | Segundo (00--59) |
| `%p` | PM | AM ou PM |
| `%x` | (localidade) | Data preferida do local |
| `%X` | (localidade) | Horário preferido do local |
| `%c` | (localidade) | Data e hora preferidas do local |

**PDF impresso e paginado** suporta o estilo strftime completo definido acima, além de códigos adicionais como `%j` (dia do ano), `%U`/`%W` (número da semana), `%z` (deslocamento de fuso horário) e `%Z` (nome do fuso horário). Consulte a [especificação strftime do Open Group](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html) para obter uma referência completa.

**Exportação DOCX** suporta os códigos listados na tabela acima. Códigos menos comuns podem ser ignorados ou transmitidos inalterados.

Use **Restaurar formatos padrão** em {% prefspane Export %} para redefinir para `%m-%d-%Y` e `%I:%M %p`.

### Cabeçalhos e rodapés por documento

Você pode especificar cabeçalhos e rodapés por documento usando metadados MultiMarkdown na parte superior do documento:

    Imprimir cabeçalho à esquerda:% título
    Centro de cabeçalho de impressão: %basename
    Imprimir cabeçalho à direita: %data
    Imprimir rodapé à direita: %página/%total

Eles substituirão quaisquer configurações nas preferências. Observe que se você estiver usando um processador diferente do MultiMarkdown e não quiser que seus cabeçalhos apareçam no documento em si, você pode usar comentários HTML, deixando uma linha em branco antes de fechar o comentário:

    <!--
    Imprimir cabeçalho à esquerda:% título
    Centro de cabeçalho de impressão: %basename
    Imprimir cabeçalho à direita: %data

    -->

## Salvar PDF

Esta opção salva sua visualização diretamente em um arquivo PDF em sua unidade. Seu documento será renderizado na íntegra, sem quebras de página. Para incluir paginação em sua saída, use as opções Imprimir/PDF no [Painel de exportação](#drawer).

## Opções de exportação RTF

Marcado pode exportar dados RTF (Rich Text Format) diretamente para sua área de transferência. Basta escolher o comando Copiar Rich Text no menu de engrenagem.

Marcado também pode salvar seu arquivo como um arquivo **RTFD** (Rich Text Format). O formato RTFD é um formato de pacote que inclui um arquivo RTF e quaisquer imagens incorporadas no documento.

## Exportação DOCX

Exportar como DOCX criará um documento válido do Microsoft Word, com elementos como títulos, cabeçalhos/rodapés, ênfases, listas, etc., todos mapeados para estilos válidos do Word. Isso significa que você pode aplicar facilmente seu próprio tema no Word.

Consulte [Trabalhando com DOCX][DOCX] para obter mais detalhes sobre importação e exportação do Word.

## Exportar Markdown para EPUB

Marked pode exportar documentos EPUB 100% válidos e 100% acessíveis. Selecione o tipo de exportação EPUB, especifique metadados como título, autor e data e, opcionalmente, adicione uma foto de capa. O arquivo salvo poderá ser lido em qualquer visualizador EPUB.

Os metadados necessários para a exportação de EPUB podem ser incluídos no próprio arquivo, seja um documento Markdown, um arquivo Scrivener (inclua uma página `metadata`) ou outro formato de livro. As chaves a serem usadas são:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

A chave Imagem da Capa pode incluir um caminho relativo ao documento base ou um caminho absoluto. Arquivos PNG ou JPG são aceitáveis.

Se o título não for definido, o padrão será o nome do arquivo do documento original e, se o autor não for definido, o padrão será o nome completo do usuário do macOS.

A data sempre será definida como a data atual e não pode ser modificada com metadados. Porém, ele pode ser alterado no momento de salvar, desde que a formatação (ISO) permaneça intacta.

### Publicação no Amazon Kindle (KDP)

EPUB é um formato aberto usado por muitos aplicativos e lojas de leitura (Apple Books, Kobo e outros), não apenas pelo Kindle. Se você estiver publicando através do [Kindle Direct Publishing (KDP)](https://kdp.amazon.com/), exporte o EPUB de Marked e carregue esse arquivo para o KDP. A Amazon o converte em seu próprio formato de entrega Kindle (KFX) para leitores.

O KDP aceita vários formatos de manuscrito, incluindo EPUB e DOCX (que o Marked também pode exportar). Consulte [formatos de e-books suportados](https://kdp.amazon.com/en_US/help/topic/G200634390) e [guia de formatação de manuscritos de e-books](https://kdp.amazon.com/en_US/help/topic/G200645680) da Amazon para obter os requisitos.

**MOBI não é obrigatório.** O KDP não aceita mais uploads de MOBI para novos títulos (incluindo livros de layout fixo, a partir de março de 2025). Marked não exporta MOBI e você não precisa de um arquivo "Kindle" ou Mobipocket separado para KDP. Se preferir as ferramentas de layout da Amazon, você também pode preparar um livro com [Kindle Create](https://kdp.amazon.com/help/topic/G8UZKZD45RTQNNVT), que produz arquivos KPF.

Antes de fazer o upload, você pode verificar a aparência do seu EPUB em dispositivos Kindle usando o [Kindle Previewer] gratuito da Amazon (https://kdp.amazon.com/help/topic/G202131170). Esse é um software opcional de terceiros da Amazon, não faz parte do Marked.

## Exportar perfis

Os perfis de exportação permitem salvar e alternar rapidamente entre diferentes conjuntos de preferências de exportação. Isso é especialmente útil se você exporta regularmente documentos para finalidades diferentes — por exemplo, um perfil para PDFs prontos para impressão com margens e cabeçalhos específicos e outro para HTML pronto para a Web com estilos incorporados.

### Usando perfis de exportação

Quando você inicia o Marked pela primeira vez, um perfil "Padrão" é criado automaticamente com suas configurações de exportação atuais. Você pode ver e selecionar perfis nas caixas de diálogo de exportação (Exportar PDF, Salvar HTML, etc.) usando o menu pop-up de perfil na parte superior da caixa de diálogo.

**Criando um novo perfil:**

1. Ajuste suas configurações de exportação em {% prefspane Export %} ou em qualquer caixa de diálogo de exportação
2. Na caixa de diálogo de exportação, clique no menu pop-up do perfil e escolha "Adicionar perfil…"
3. Insira um nome para o seu perfil (por exemplo, “Qualidade de impressão” ou “Exportação para Web”)
4. As configurações atuais são salvas como esse perfil

**Carregando um perfil:**

- Selecione um perfil no menu pop-up em qualquer caixa de diálogo de exportação
- Todas as configurações de exportação serão atualizadas imediatamente para corresponder aos valores salvos desse perfil

**Salvar alterações em um perfil:**

- Depois de fazer alterações nas configurações de exportação, um botão "Salvar" aparece próximo ao pop-up do perfil
- Clique em "Salvar" para atualizar o perfil atual com suas alterações
- O botão só fica habilitado quando há alterações não salvas

**Gerenciando Perfis:**

- Escolha "Gerenciar perfis…" no menu pop-up do perfil para abrir a janela de gerenciamento de perfil
- A partir daí você pode:
  - **Renomear** perfis clicando duas vezes no nome
  - **Duplicar** um perfil para criar um novo baseado nele
  - **Excluir** perfis (o perfil "Padrão" não pode ser excluído)
  - Veja todos os perfis disponíveis em uma lista

### O que os perfis de exportação capturam

Os perfis de exportação salvam todas as preferências relacionadas à exportação, incluindo:

- **Configurações de PDF**: tamanho da página, margens, cabeçalhos/rodapés, fontes, quebras de página, índice
- **Exportação HTML**: incorporação de estilo, incorporação de imagem, realce de sintaxe, renderização matemática
- **Processamento de Markdown**: quebra automática de texto, formatação de link, regras do processador
- **CriticMarkup**: tipo de exportação e opções de processamento
- **Destaque de sintaxe**: detecção de idioma e preferências de destaque
- **Renderização matemática**: integração MathJax/KaTeX e numeração de equações
- **Manipulação de imagens**: opções de incorporação, comportamento de cópia, configurações de caminho
- **Tipografia**: Hifenização, viúvas/órfãs, tamanhos de fonte
- **Comportamento de exportação**: preferências de nomenclatura de arquivos, resolução de conflitos

Os perfis funcionam em todos os tipos de exportação: Markdown, HTML, PDF contínuo, PDF paginado, EPUB, DOCX, ODT, TextBundle, RTF e OPML.

### Armazenamento de perfil

Os perfis são armazenados na pasta Application Support em:

    ~/Library/Application Support/Marked/ExportProfiles.plist

Isso significa que seus perfis persistem mesmo se você redefinir as preferências do aplicativo e eles sobrevivem às atualizações do aplicativo. Você pode fazer backup desse arquivo para preservar seus perfis nas instalações.

### Dicas para usar perfis de exportação

- **Crie perfis para fluxos de trabalho comuns**: se você exporta regularmente para impressão ou web, crie perfis separados para cada
- **Use nomes descritivos**: nomes de perfis como "Impressão - Carta" ou "Web - Estilos incorporados" deixam claro para que serve cada perfil
- **Salvar com frequência**: o botão "Salvar" aparece sempre que você faz alterações — clique nele para preservar seus ajustes
- **Comece a partir de perfis existentes**: use "Duplicar" na janela de gerenciamento para criar variações de perfis existentes em vez de começar do zero

[break]: Special_Syntax.html#pagebreaks
[DOCX]: Working_with_DOCX.html
[custom]: Custom_Styles.html
[dropbox]: http://dropbox.com
[expbut]: images/ExportButton.png @2x width=534px height=256px class=center
[export-panel]: images/export-panel-800.jpg @2x width=800 class=center
[exporthtmlaccessory]: images/SaveHTML.png @2x width=740px height=229px class=center
[printmargins]: images/PrintMargins.jpg @2x width=329px height=144px class=center