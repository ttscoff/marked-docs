# <%= @title %>

Veja seus documentos *do seu jeito*.

## Usando estilos personalizados [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

A maneira mais fácil de explorar os Estilos Personalizados é através da
[Galeria de Estilos Personalizados][2]. Lá você pode navegar pelos
estilos disponíveis em ação, instalá-los com um clique de
botão, e até [enviar suas próprias criações][6] para
inclusão.

Para adicionar folhas de estilo personalizadas do seu disco local ao Marked,
use o {% prefspane Style %}. Os novos estilos serão adicionados aos
menus suspensos nas configurações de Janela e em cada janela,
e serão nomeados com base no nome do arquivo CSS
adicionado. Guarde seus arquivos CSS personalizados em um local seguro no
disco. Se eles forem movidos, serão removidos do
Marked até que você os adicione novamente a partir do novo local. É
uma boa ideia fechar os documentos abertos e remover o estilo
das Configurações antes de excluir ou renomear um arquivo CSS usado
pelo Marked. Nada será quebrado se você não fizer isso, mas evita
alguma confusão.

Adicione Estilos Personalizados usando o Gerenciador de Estilos com o botão Adicionar, ou arrastando um ou mais arquivos CSS para o painel de Configurações.

## Gerenciando estilos com o Gerenciador de Estilos [managing-styles-with-the-style-manager]

Ao abrir o Gerenciador de Estilos, você tem um único lugar para organizar todos os temas
integrados e personalizados. Clique no botão **Gerenciar Estilos…** no painel
{% prefspane Style %},
ou simplesmente solte arquivos CSS na janela de preferências --- o Marked vai importá-los,
abrir o Gerenciador de Estilos e selecionar a linha recém-adicionada para você. Arrastar
arquivos CSS diretamente para a janela do Gerenciador de Estilos também funciona; quando vários arquivos
são arrastados, a sobreposição é atualizada para "Adicionar N Estilos Personalizados", deixando claro
que você está importando um lote.

![][img-style-manager]

Dentro do Gerenciador de Estilos você encontrará uma tabela ordenável que combina estilos
integrados e personalizados. Cada linha oferece:

- Uma caixa de seleção **Ativado** que adiciona/remove imediatamente o estilo do menu
  Estilo, do popup de Estilo Padrão e dos atalhos de teclado. Desativar o estilo
  atualmente ativo alterna automaticamente para o próximo item disponível.
- Uma coluna **Nome** que você pode editar diretamente; as alterações persistem e se propagam para todos
  os menus. Clique no nome do estilo para editá-lo no local.
- Uma coluna **Origem** que indica Integrado, Personalizado ou Duplicado.
- Uma pilha de **Ações** com botões para **Editar** (abre o arquivo CSS no seu
  editor), **Duplicar** (cria uma cópia e um novo arquivo CSS no disco), **Revelar**
  (mostra o arquivo no Finder), e **Excluir** (com opções para remover a referência ou
  mover o arquivo CSS para a Lixeira).

As linhas são reordenadas por arrastar e soltar, e a ordem determina o menu Estilo, assim como
as atribuições de atalho `⌘/#`, então você pode literalmente arrastar estilos para os lugares
que quiser. Você também pode arrastar arquivos CSS externos para posições específicas; o indicador
de soltura determina onde o novo estilo será inserido.

### Pré-visualização ao vivo [live-preview]

O painel direito contém uma pré-visualização que renderiza o estilo selecionado
dentro de um documento HTML completo, com um conjunto abrangente de títulos, listas, tabelas, blocos de código etc. A
pré-visualização usa o CSS real no disco, então as edições feitas no seu editor externo são atualizadas instantaneamente. Uma caixa de seleção alterna a pré-visualização do Modo Escuro.

Você pode encontrar estilos adicionais para usar (ou como exemplos para
criar os seus próprios) [no GitHub][1] (veja os [exemplos][2] para
uma olhada rápida no que há disponível). Veja [Criando CSS Personalizado][3]
para detalhes e dicas.

## CSS Adicional [additional-css]

No {% prefspane Style %}, você encontrará uma opção
chamada CSS Adicional com um botão rotulado "Editar CSS".
Clicar nesse botão abre uma janela onde você pode adicionar
regras CSS universais que serão aplicadas a todos os estilos. Observe
que a especificidade das regras pode ser importante ao
sobrescrever parte da estilização padrão do Marked. O corpo principal
do documento é envolvido em uma div com o id "#wrapper".
Prefixar um seletor com isso pode facilitar as
sobrescritas, por exemplo:

    #wrapper img { width: 100%; height: auto; }

O CSS nesse campo é **anexado ao tema ativo**. Não é um
substituto para um Estilo Personalizado completo: uma folha de estilo escrita apenas para esse
campo é deliberadamente parcial, e carregá-la pelo Gerenciador de Estilos como
tema deixaria sem estilo tudo o que ela não cobre.

O Marked **reescreve** os seletores de CSS Adicional antes da injeção. Classes de
body iniciais como `.mkprinting` são mescladas em `body` em vez de
aninhadas sob `#wrapper`, então as regras de impressão nesse campo devem usar
`body.mkprinting #wrapper …` (veja [Criando CSS
Personalizado](Writing_Custom_CSS.html#additional-css-settings) para as regras completas
de reescrita). Não há limite de tamanho nem verificação de validade nesse campo
--- CSS inválido simplesmente não tem efeito.

O CSS nesse campo será aplicado a todo documento, independentemente
do Estilo que estiver sendo usado --- incluindo exportação em HTML quando os estilos são
incluídos. Se você quiser aplicar CSS personalizado
com base em correspondências condicionais, use as ações Definir Estilo, Inserir
Arquivo CSS ou Inserir CSS em {% prefspane Processor %}
Regras Personalizadas.

## Exportação para impressão e PDF [print-and-pdf-export]

O Marked injeta um bloco `@media print` integrado (`mkprintstyles`) em toda
pré-visualização. Ele define padrões como uma base de **10pt** em `html`, `body` e
`#wrapper` (ou o tamanho definido em **Tamanho de fonte personalizado para exportação/impressão** em
{% prefspane Export %} quando essa opção está ativada), e normaliza o texto de parágrafos
com `p { font-size: 1em; }` e `li p { font-size: 1em; }`, para que regras exclusivas de tela como
`p { font-size: 1.1429em; }` não aumentem o corpo do texto
em PDFs e material impresso.

A exportação em PDF pode usar mídia **print** ou **screen** na WebView oculta usada para
a geração. Os temas integrados normalmente usam mídia de impressão; **estilos personalizados** e
documentos [Fountain](Fountain_for_Screenwriters.html) costumam usar mídia de tela, para que o
layout corresponda à pré-visualização. Isso significa que as regras `@media print { ... }` nem sempre
são aplicadas durante a exportação em PDF.

Para uma estilização confiável em PDF e na Pré-visualização de Impressão/PDF, prefixe os seletores com a
classe `mkprinting` que o Marked adiciona a `<body>` durante a exportação (veja [Escrevendo CSS
Personalizado](Writing_Custom_CSS.html#printstyles) para detalhes e exemplos). Em um
arquivo de **Estilo Personalizado**, você pode usar apenas `.mkprinting`. Em **CSS Adicional**,
use a forma qualificada pelo body `body.mkprinting #wrapper …`, porque esse campo
reescreve os seletores. Você também pode combinar qualquer uma das formas com `@media print` quando
precisar cobrir os dois caminhos.

Para definir tamanhos diferentes dos padrões de impressão do Marked, adicione regras explícitas no
seu CSS personalizado (ou em CSS Adicional). Use `!important` quando precisar
sobrescrever os estilos de impressão injetados pelo Marked --- por exemplo:

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

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

Regras sem `!important` podem perder para regras posteriores em `mkprintstyles` ou para
outros seletores não qualificados na sua folha de estilo que ainda se aplicam na impressão. Colocar
ajustes exclusivos de impressão em `@media print` e/ou em regras `.mkprinting` / `body.mkprinting`
(em vez de somente em regras de tela) mantém o comportamento da pré-visualização e da exportação
mais fácil de entender.

## Observando alterações no CSS [watching-css-changes]

Você pode marcar uma caixa na seção Estilos Personalizados do {% prefspane Style %}
para que o Marked observe o arquivo CSS ativo,
além do arquivo Markdown que você está editando. Quando
alterações forem detectadas em qualquer um dos arquivos, a pré-visualização será
atualizada. Isso é útil para editar estilos personalizados sem
precisar atualizar constantemente, e também pode ser usado para tarefas simples de
desenvolvimento web.

Isso também é útil para algum trabalho básico de design web e
experimentação com CSS (como criar estilos personalizados). Carregue um
arquivo Markdown contendo toda a marcação que você deseja estilizar,
crie um estilo personalizado e observe a pré-visualização mudar ao vivo
enquanto você edita.

## Escrevendo CSS personalizado [writing-custom-css]

Se você já conhece CSS, pode criar suas próprias folhas de
estilo para usar no Marked. Veja [Escrevendo CSS Personalizado][3] para
detalhes. Sempre que criar algo novo, considere
[enviá-lo][6] para a [galeria][2] e compartilhar com outros
usuários. Não deixe de cobrir os itens básicos listados no guia, e
inclua o comentário de metadados no topo.

### Estilos Personalizados automáticos com o StyleStealer [automatic-custom-styles-with-stylestealer]

Você pode até gerar um estilo automaticamente com base em um
site existente usando o [Style Stealer][4]. Isso permite carregar uma página web e capturar os estilos calculados de todos os elementos principais encontrados no Markdown, e então salvá-los como um estilo personalizado.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Gerencie os Estilos Personalizados (renomear, reordenar, duplicar e excluir) pelo [Gerenciador de Estilos](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
