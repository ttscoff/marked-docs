<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opções em {% prefspane Export %}:

(Veja [Exportando](Exporting.html) para mais informações)

![Configurações: Exportar][1]

[1]: images/screenshots/preferences-Export.jpg @2x width=920px height=1031px class=preferencepane-scroll

### Exportar perfil [export-profile]

Exportar perfil
: selecione um perfil salvo no menu pop-up. Os perfis armazenam um conjunto completo de preferências de exportação para alternar rapidamente entre fluxos de trabalho (por exemplo, impressão de PDF versus HTML da web). Consulte [Exportar perfis](Exporting.html#export-profiles).

Novo
: crie um novo perfil a partir das configurações atuais.

Gerenciar
: abra o gerenciador de perfis para renomear, duplicar ou excluir perfis.

### Imprimir/PDF [printpdf]

Desative links/destaques ao exportar PDF ou imprimir
: remove a formatação (sublinhado e cor) dos links durante a impressão.

Incluir URL como anotação de texto
: ao imprimir ou exportar PDF, o URL de um link aparecerá após o texto vinculado.

Substitua regras horizontais por quebras de página
: transforma as regras horizontais do documento em quebras de página (isso também forçará as notas de rodapé em uma nova página).

Incorporar imagens ao copiar HTML
: quando ativado, copiar HTML para a área de transferência irá procurar imagens locais e codificá-las em Base64 para incluí-las como URLs de dados no código-fonte.

Imprimir cores e imagens de fundo
: Por padrão, Marcado irá imprimir/exportar com um fundo branco. Se quiser incluir cores de fundo e imagens de temas personalizados, habilite esta opção.

Evite manchetes órfãs
: esta opção evita que os títulos da próxima seção apareçam na parte inferior de uma página sem sucesso no conteúdo.

Excluir primeiro H1
: ignore o título do primeiro nível no documento ao usar H1s como quebras de página.

Use o primeiro H1 como título substituto
: ao usar aplicativos como o Bear ou a visualização de streaming, esta opção permite substituir o nome do arquivo pelo conteúdo do primeiro H1 do documento. Se os metadados para "título" forem especificados, eles sempre terão precedência.

Adicione quebras de página antes
: Utilize cabeçalhos de nível 1/2 como divisores de seção, sempre iniciando-os em uma nova página. Selecione “Notas de rodapé” para sempre adicionar uma quebra de página antes de qualquer nota de rodapé no documento.

Indicar quebras de página na visualização
: mostra uma linha tracejada clara onde as quebras são inseridas com a sintaxe <!\--BREAK\--> ou marcando as opções de quebra automática nas configurações de exportação.

Tamanho de fonte personalizado para exportação/impressão
: Se definido, todo o texto será dimensionado com base na configuração de ponto selecionada (o padrão é uma base de 10 pontos).

Margens
: define as margens de impressão (especificadas em pontos) para cima, para baixo, para a esquerda e para a direita.

Imprimir índice
: Inclui índice automático em impressão/PDF.

Quebra de página depois
: passa automaticamente para uma nova página após um Índice inserido.

Marcadores de nível do índice
: use os menus suspensos para definir o marcador de item da lista para cada nível de recuo em um sumário.

### Cabeçalhos e rodapés [headers-and-footers]

Configure fonte, logotipo, campos de cabeçalho/rodapé, formatos de data e hora, inclusão de primeira página, deslocamento de numeração de página e bordas. Os marcadores de campo incluem `%title`, `%logo`, `%page`, `%total`, `%date`, `%time`, `%h1`, `%h2` e outros.

Consulte [Cabeçalhos e Rodapés](Exporting.html#headers-and-footers) em [Exportando](Exporting.html) para referências e exemplos de espaços reservados. Consulte [Formatos de data e hora](Exporting.html#dateandtimeformats) para códigos de formato `%date` e `%time`.

Incluir na primeira página
: Se a opção de cabeçalho e/ou rodapé estiver desmarcada, a primeira página não imprimirá o tipo especificado.

Formato de data
: string de formato no estilo strftime para `%date` em cabeçalhos e rodapés. Consulte [Formatos de data e hora](Exporting.html#dateandtimeformats).

Formato de hora
: string de formato no estilo strftime para `%time` em cabeçalhos e rodapés. Consulte [Formatos de data e hora](Exporting.html#dateandtimeformats).

Deslocamento de numeração de página
: Usado para ajustar em que número os números das páginas começam. Por exemplo, se você tiver um índice na primeira página e quiser que a numeração comece na segunda página, defina o deslocamento como -1. A página 2 agora será a página 1 e o total de páginas será ajustado de acordo.

Fronteira
: imprima uma linha horizontal abaixo do cabeçalho e/ou acima do rodapé.

Restaurar formatos padrão
: redefine as strings de formato de data e hora para os padrões de Marked (`%m-%d-%Y` e `%I:%M %p`). Consulte [Formatos de data e hora](Exporting.html#dateandtimeformats).