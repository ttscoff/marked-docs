<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Visualize seus documentos do seu jeito.

## Usando estilos personalizados

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

A maneira mais fácil de explorar estilos personalizados é através do
[Galeria de estilos personalizados][2]. A partir daí você pode navegar
estilos disponíveis em ação, instale-os com o clique de um
botão e até [envie suas próprias criações] [6] para
inclusão.

Para adicionar folhas de estilo personalizadas da sua unidade local ao Marcado,
use o {% prefspane Style %}. Novos estilos serão adicionados a
os menus suspensos nas configurações da janela e em cada janela,
e será nomeado com base no nome do arquivo base do arquivo CSS
adicionado. Armazene seus arquivos CSS personalizados em um local seguro no seu
dirigir. Se eles se moverem na sua unidade, serão removidos do
Marcado até que você os adicione novamente a partir do novo local. É
uma boa ideia fechar documentos abertos e remover o estilo
em Configurações antes de excluir ou renomear um arquivo CSS usado por
Marcado. Não vai quebrar nada se você não fizer isso, mas salva
alguma confusão.

Adicione estilos personalizados usando o Gerenciador de estilos com o botão Adicionar ou arrastando um ou mais arquivos CSS para as configurações
painel.

## Gerenciando estilos com o Style Manager

Iniciar o Style Manager oferece um único local para selecionar todos os estilos integrados.
e tema personalizado. Clique no botão **Gerenciar estilos…** em {% prefspane Style %}
painel,
ou simplesmente solte os arquivos CSS na janela de preferências --- Marcado irá importá-los,
abra o Gerenciador de estilos e selecione a linha recém-adicionada para você. Arrastar CSS
arquivos diretamente na janela do Style Manager também funcionam; quando vários arquivos
são arrastados, você verá a atualização da sobreposição para "Adicionar N estilos personalizados", para que fique claro
você está importando um lote.

![][gerenciador de estilo img]

Dentro do Style Manager você encontrará uma tabela classificável que mistura recursos integrados e
estilos personalizados. Cada linha oferece:

- Uma caixa de seleção **Ativada** que adiciona/remove imediatamente o estilo do Estilo
  menu, pop-up Estilo padrão e atalhos de teclado. Desativando o atualmente
  o estilo ativo muda automaticamente para a próxima entrada disponível.
- Uma coluna **Nome** que você pode editar inline; as mudanças persistem e se propagam para todos
  menu. Clique no nome do estilo para editá-lo no lugar.
- Uma coluna **Origem** que indica Integrado, Personalizado ou Duplicado.
- Uma pilha de **Ações** com botões para **Editar** (abre o arquivo CSS em seu
  editor), **Duplicar** (cria uma cópia e um novo arquivo CSS no disco), **Revelar**
  (mostra o arquivo no Finder) e **Excluir** (com opções para remover a referência ou
  mova o arquivo CSS para a Lixeira).

As linhas são reordenadas arrastando e soltando, e a ordem direciona o menu Estilo, bem como
as atribuições de atalho `⌘/#`, para que você possa literalmente arrastar estilos para os slots
você quer. Você também pode arrastar arquivos CSS externos para posições específicas; a gota
indicador determina onde o novo estilo será inserido.

### Visualização ao vivo

O painel direito contém uma visualização que renderiza o estilo selecionado
dentro de um documento HTML completo com um conjunto abrangente de títulos, listas, tabelas, blocos de código, etc.
a visualização usa o CSS real no disco, portanto, as edições feitas em seu editor externo são atualizadas instantaneamente. Uma caixa de seleção alterna a visualização do Modo Escuro.

Você pode encontrar estilos adicionais para uso (ou como exemplos para
criando o seu próprio) [no GitHub][1] (veja os [exemplos][2] para
uma rápida olhada no que está lá). Consulte [Criando CSS personalizado][3]
para detalhes e dicas.

## CSS adicional

Abaixo de {% prefspane Style %}, você encontrará uma opção
intitulado CSS adicional com um botão denominado "Editar CSS".
Clicar neste botão abre uma janela onde você pode adicionar
regras CSS universais que serão aplicadas a todos os estilos. Nota
que a especificidade das regras pode ser importante quando
substituindo alguns dos estilos padrão do Marked. O corpo principal
do documento é agrupado em uma div com o id "#wrapper".
Prefixar um seletor com isso pode facilitar
substituições, por exemplo:

    #wrapper img { largura: 100%; altura: automático; }

CSS neste campo será aplicado a todos os documentos, não
não importa o estilo que ele está usando. Se você deseja aplicar personalizado
CSS baseado em correspondências condicionais, use Set Style, Insert
Arquivo CSS ou Inserir ações CSS em {% prefspane Processor %}
Regras personalizadas.

## Impressão e exportação de PDF

Marcado injeta um bloco `@media print` integrado (`mkprintstyles`) em cada
visualização. Ele define padrões como **10pt** com base em `html`, `body` e
`#wrapper` (ou o tamanho de **Tamanho de fonte personalizado para exportação/impressão** em
{% prefspane Export %} quando essa opção está habilitada) e normaliza o parágrafo
texto com `p { font-size: 1em; }` e `li p { font-size: 1em; }` então
regras somente de tela como `p { font-size: 1.1429em; }` não aumentam a cópia do corpo
em PDFs e saída impressa.

A exportação de PDF usa mídia impressa no WebView oculto usado para geração, portanto
`@media print { ... }` as regras em sua folha de estilo se aplicam da mesma forma que para
impressão.

Para definir tamanhos diferentes dos padrões de impressão do Marked, adicione regras explícitas
dentro de `@media print` em seu CSS personalizado (ou em CSS adicional). Usar
`!important` quando você precisar substituir os estilos de impressão injetados do Marked --- para
exemplo:

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}
```

Regras sem `!important` podem perder para regras posteriores em `mkprintstyles` ou para
outros seletores não qualificados em sua planilha que ainda se aplicam na impressão. Colocando
ajustes somente para impressão em `@media print` (em vez de apenas nas regras da tela) mantêm
o comportamento de visualização e exportação é mais fácil de raciocinar.

## Observando alterações de CSS

Você pode marcar uma caixa na seção Estilos Personalizados do {% prefspane Style %}
para marcar o arquivo CSS ativo
além do arquivo Markdown que você está editando. Quando
alterações forem detectadas em qualquer arquivo, a visualização será
atualizar. Isto é útil para editar estilos personalizados sem
constantemente atualizado e também pode ser usado para web simples
tarefas de desenvolvimento.

Isso também é útil para alguns trabalhos básicos de web design e CSS
experimentação (como criar estilos personalizados). Carregue um
Arquivo Markdown contendo toda a marcação que você deseja estilizar
para, crie um estilo personalizado e assista à prévia ao vivo
muda à medida que você o edita.

## Escrevendo CSS personalizado

Se você estiver familiarizado com CSS, poderá criar seu próprio estilo
folhas para uso em Marcado. Consulte [Escrever CSS personalizado][3] para
detalhes. Sempre que você criar algo novo, considere
[enviando] [6] para a [galeria] [2] para compartilhar com outros
usuários. Certifique-se de cobrir os princípios básicos listados no guia e
inclua o comentário de metadados na parte superior.

### Estilos personalizados automáticos com StyleStealer

Você pode até gerar automaticamente um estilo baseado em um
site existente usando o [Style Stealer][4]. Isso permite que você carregue uma página da web e obtenha os estilos calculados para todos os principais elementos encontrados no Markdown e, em seguida, salve-os em um estilo personalizado.

![Ladrão de estilo][ladrão de estilo]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Gerencie estilos personalizados (renomeie, reordene, duplique e exclua) no [Style Manager](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center