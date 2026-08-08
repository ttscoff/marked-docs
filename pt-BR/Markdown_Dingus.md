<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

O Markdown Dingus é uma ferramenta de teste especializada que ajuda
você entende como diferentes processadores Markdown lidam com seu
conteúdo. Ele fornece uma interface de três painéis onde você pode
edite Markdown, visualize a fonte HTML gerada e veja o
visualização renderizada simultaneamente.

O Dingus compartilha algum manuseio de baixo nível com o Marked
visualização, como tratamento especial de blocos de código protegidos.
__não__ executa [Regras Personalizadas](Custom_Processor.html)
(Condutor). Ele usa a maioria das configurações padrão, ignorando as configurações
como "novas linhas do GitHub" e "caixas de seleção do GitHub", então o
O resultado pode ser diferente do que você vê em um Marcado normal
visualização.

## Regras personalizadas não se aplicam [custom-rules-do-not-apply]

O Dingus é um __processador sandbox__: seu Markdown vai
direto para o processador integrado que você escolher (MultiMarkdown,
CommonMark (GFM), Desconto ou Kramdown). [Regras personalizadas](Custom_Processor.html)
nunca execute lá - sem ações de pré-processamento, regras de localização/substituição,
comandos shell, Inserir texto/arquivo ou outras etapas do Conductor.

Em uma visualização normal, as regras personalizadas podem alterar o Markdown
antes da renderização, defina estilos, injete CSS ou JavaScript e
mais. Nada disso acontece quando você edita no Dingus.
Alterar regras personalizadas enquanto o Dingus está aberto não
atualize sua visualização.

O Dingus __pode__ usar os mesmos [estilos CSS de visualização](Custom_Styles.html)
como a janela principal (através do menu de estilo no painel de saída).
Isso é apenas aparência; não é o mesmo que executar Custom
Regras.

__Open in Dingus__ a partir de uma visualização carrega o documento
buffer Markdown atual. Se as regras personalizadas já foram executadas quando
esse arquivo foi aberto em Marcado, você poderá ver seus efeitos em
o texto (por exemplo, texto inserido por uma regra), mas o
Dingus não reaplicará regras enquanto você digita. Para testar personalizado
Regras, use uma visualização marcada padrão ou salve no Dingus
e abra o arquivo com __Open in Marked__.

## O que é um "Dingus"? [what-is-a-dingus]

Um "dingus" é um termo emprestado do desenvolvimento web que
refere-se a uma ferramenta de teste simples ou ambiente sandbox. O
Markdown Dingus permite experimentar a sintaxe Markdown e
veja imediatamente como diferentes processadores o interpretam.

## Acessando o Dingus [accessing-the-dingus]

O Markdown Dingus pode ser acessado em
[{% appmenu Help, Open Markdown Dingus %}][2]. É particularmente
útil quando você está:

* Aprendendo a nova sintaxe do Markdown
* Solução de problemas de renderização
* Escolhendo entre diferentes processadores
* Escrever documentação que precisa funcionar em vários
  sistemas

## Layout de três painéis [three-pane-layout]

![][1]

A janela do Dingus está dividida em três painéis sincronizados:

### 1. Entrada de redução (painel esquerdo) [1-markdown-input-left-pane]

* __Destaque de sintaxe__: Seu Markdown é destacado com
  cores para deixar a estrutura clara
* __Live Editing__: Digite e veja as alterações refletidas instantaneamente
  nos outros painéis
* __Fonte Grande__: Fonte Menlo 21pt para edição confortável

__Options dropdown__ (canto superior direito do painel esquerdo): O
O menu **Opções** permite alternar:

* __Mostrar números de linha__: Exibe uma medianiz à esquerda com
  um número de linha por parágrafo (linhas quebradas contam como um
  linha).
* __Mostrar invisíveis__: Mostra espaços como pontos intermediários (·), tabulações como
  uma seta para a direita (→) e novas linhas como retorno de carro
  símbolo (↵) em cinza claro para que você possa identificar
  espaço em branco.
* __Highlight gremlins__: Coloca um fundo vermelho claro
  caracteres não ASCII (por exemplo, aspas curvas, emoji) e um escuro
  fundo vermelho em caracteres invisíveis problemáticos (por exemplo
  espaços de largura zero). Caracteres normais de tabulação e nova linha são
  não destacado.

Suas escolhas serão salvas e restauradas na próxima vez que você abrir
o Dingus.

__Find bar__: Pressione **⌘F** para mostrar a barra de localização abaixo do
Rótulo "Entrada de Markdown". Você pode pesquisar e substituir no
editor, use **⌘G** para Encontrar Próximo e **⇧⌘G** para Encontrar
Anterior e substitua uma ou todas as correspondências. Pressione o botão fechar
botão ou **⌘F** novamente para ocultar a barra de localização.

### 2. Fonte HTML (painel central) [2-html-source-middle-pane]

* __Generated HTML__: Veja exatamente qual HTML foi selecionado
  processador cria
* __Syntax Highlighted__: HTML é codificado por cores para facilitar
  lendo

### 3. Visualização renderizada (painel direito) [3-rendered-preview-right-pane]

* __Live Preview__: Veja como ficará seu Markdown quando
  renderizado
* __Emoji Support__: emojis estilo GitHub como `:zzz:` são
  convertido em imagens
* __Auto-scrolling__: Rola automaticamente para mostrar seu
  posição de edição atual

## Edição no Dingus [editing-in-the-dingus]

O painel Markdown Input inclui recursos de edição inteligentes para
torne a escrita do Markdown mais rápida e natural.

### Nova linha inteligente (tecla Return) [smart-newline-return-key]

Pressionar Return se adapta à linha atual:

* __Lists__: Em uma linha de lista (`-`, `*` , `+` ou `1.` ),
  insere um novo item da lista com o marcador correto. Numerado
  as listas continuam com o próximo número.
* __Blockquotes__: Em uma linha começando com `>` , insere um
  nova linha de blockquote.
* __Code fences__: Em uma linha com três ou mais crases
  (por exemplo, ` ``` `), insere uma linha em branco entre a abertura
  e fechando cercas.
* __Outras linhas__: Insere uma nova linha normal.

### Emparelhamento de personagens [character-pairing]

Quando você digita um caractere de abertura, o editor automaticamente
insere o caractere de fechamento e coloca o cursor entre
eles. Pares suportados: `"` `'` `(` `[` `` ` `` `<` .

* __With selection__: Quebra o texto selecionado no par.
* __Sem seleção__: Insere o par com o cursor
  entre eles.
* __Type-over__: Se o próximo caractere já for o
  fechando o delimitador, digitá-lo novamente move o cursor além
  em vez de inserir uma duplicata.
- __Espaço em par vazio__: Se o cursor estiver entre um par vazio (por exemplo, `(|)`), digitar um espaço substitui o caractere de fechamento por um espaço.

### Teclas de atalho [shortcut-keys]

| Atalho | Ação |
|:----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⌘F** | Mostrar ou ocultar a barra de localização no painel Markdown Input |
| **⌘G** | Encontre o próximo (quando a barra de localização estiver visível) |
| **⇧⌘G** | Localizar anterior (quando a barra de localização estiver visível) |
| **⌘B** | Negrito: envolva a seleção em `**` ou insira `**\|**` com o cursor entre |
| **⌘EU** | Itálico: envolva a seleção em `_` ou insira `_\|_` com o cursor entre |
| **⇧⌘L** | Marcador de lista de ciclos (não ordenado ↔ ordenado) |
| **Guia** | Recuar linha ou item de lista |
| **Shift+Tab** | Recuar linha ou item de lista |
| **⌃⌘→** | Recuar linha ou item de lista (igual a Tab) |
| **⌃⌘←** | Recuar linha ou item de lista (igual a Shift+Tab) |
| **⌃⌘↑** | Mover parágrafo para cima (cortar parágrafo incluindo nova linha, colar uma linha acima) |
| **⌃⌘↓** | Mover o parágrafo para baixo (cortar o parágrafo incluindo a nova linha, colar uma linha abaixo) |
| **⌘K** | Insira ou ajuste um link Markdown: coloque a seleção como `[text]()` e coloque o cursor na URL, ou insira `[]()` com o cursor entre colchetes quando não houver seleção |
| **⌘U** | Alternar painel de saída (Fonte/Visualização) |
| **⌥⌘↑** | Expanda a seleção: palavra → delimitadores internos/externos → frase → parágrafo → bloco contíguo (como uma tabela ou bloco de código) → lista delimitadora/citação de bloco/bloco de código → documento |
| **⌥⌘↓** | Seleção de contratos de volta aos mesmos níveis até a posição original do cursor |

Tab/Shift+Tab (e ⌃⌘←/⌃⌘→) respeitam a estrutura da lista e
blockquotes: eles recuam/recuam itens da lista e adicionam ou
remova `>` das linhas de citação. Mover parágrafo para cima/para baixo
seleciona o parágrafo inteiro sob o cursor (incluindo seu
nova linha à direita), corta e cola acima ou abaixo do
parágrafo adjacente para que os parágrafos não se fundam.

### Colar URL inteligente [magic-links-and-footnotes-f6-f7]

Quando você cola e a área de transferência contém um URL no formato
`protocol://...` sem espaços:

* __Com uma seleção__: a seleção é transformada em um
  Link de redução: `[selected text](url)` .
* __Sem seleção__: a URL é inserida como um
  auto-link: `<url>` .

Isso torna mais fácil transformar URLs copiados em links sem
digitação manual.

### Seleção inteligente (⌥⌘↑ / ⌥⌘↓) [smart-url-paste]

O editor Dingus suporta __expansão de seleção semântica__:

* __⌥⌘↑__ começa no cursor e expande a seleção
  através de:
	- a palavra atual
	- conteúdo delimitado interna e externamente (aspas, colchetes,
   parênteses e blocos de código protegidos)
	- a frase atual
	- o parágrafo atual
	- o bloco contíguo de linhas não vazias (por exemplo, um
   tabela inteira ou bloco de código multilinha sem linhas em branco)
	- o item da lista, blockquote ou bloco de código anexo
	- todo o documento
* __⌥⌘↓__ desce pelos mesmos níveis até
  retorna à posição original do cursor.

Cada pressão sempre se move para um valor estritamente maior ou menor
seleção, para que você nunca pressione as teclas "no-op" enquanto
expandindo ou contraindo.

## Usando o Dingus como editor [using-the-dingus-as-an-editor]

O Dingus não pretende substituir um texto completo
editor, mas pode ser muito útil para edições __rápidas com um
visualização ao vivo__, especialmente quando você deseja ver exatamente como
as alterações serão renderizadas. Todo o comportamento de edição de texto
descrito em [Editando no Dingus][3] se aplica aqui.

### Abrindo um arquivo/criando um novo arquivo [opening-a-filecreating-a-new-file]

* __Crie um novo arquivo no Dingus__
	- Escolha __{% appmenu File, New, New Markdown File %}__
   (⌘N).
	- Quando solicitado, escolha __Dingus__ para iniciar um novo e não salvo
   Documento Dingus.
	- Novos documentos Dingus abertos com conteúdo de amostra selecionado;
   basta começar a digitar para substituí-lo.
* __Abra um arquivo existente no Dingus__
	- Use __{% appmenu File, Open in Dingus... %}__ (⌥⌘O), ou
   com a janela do Dingus ativa, clique em __Open…__ no status
   barra. O comando abre a janela Dingus se necessário, então
   mostra o painel Abrir.
	- Escolha qualquer arquivo de texto simples/Markdown compatível; é
   o conteúdo substituirá o buffer Dingus atual.
* __Abra um documento de visualização marcado no Dingus__
	- Em uma janela de visualização normal, use __{% appmenu Preview,
   Open in Dingus %}__ (⌥⌘E).
	- O Markdown do documento atual é carregado no Dingus
   para que você possa experimentar sem tocar no arquivo original
   até você decidir salvar. Regras personalizadas não são aplicadas em
   o Dingus; consulte [Regras personalizadas não se aplicam](#custom-rules-do-not-apply).

### Salvando um arquivo [saving-a-file]

* __Salvar alterações no arquivo atual__
	- Na janela do Dingus, clique em __Salvar__ na barra de status,
   ou usar
    __{% appmenu File, Save Dingus %}__ (⌘S).
	- Se o documento Dingus ainda não tiver sido salvo, você será
   solicitado um local e nome de arquivo; depois disso, ⌘S
   atualiza o mesmo arquivo.
* __Salvar como/duplicar em um novo arquivo__
	- Use __{% appmenu File, Save Dingus As... %}__ (⌥⌘S).
	- Isso sempre abre uma caixa de diálogo __Salvar como__ e grava o
   conteúdo atual do Dingus para um novo arquivo sem sobrescrever
   o original.

### Pré-visualização em Marcado [previewing-in-marked]

* __Abra o documento Dingus como uma visualização completa marcada__
	- Clique em __Open in Marked__ na barra de status do Dingus ou use

__{% appmenu File, Open Dingus in Marked %}__ (⌘P).
	- Se o documento Dingus não for salvo ou tiver alterações não salvas,
   você será solicitado a salvar primeiro; então Marcado abre um
   visualização padrão para esse arquivo.

Usando estes comandos, você pode tratar o Dingus como um
editor leve para soluções rápidas e experimentos, então
pule para uma visualização completa marcada ou para seu editor normal quando
você está pronto para uma edição mais extensa.

## Seleção do processador [processor-selection]

Use o menu suspenso na parte superior para alternar entre diferentes
Processadores de redução:

* __MultiMarkdown__: Processador completo com tabelas,
  notas de rodapé e suporte matemático
* __CommonMark (GFM)__: Processador padrão e rápido seguindo o
  Especificação CommonMark
* __Discount__: Markdown com sabor do GitHub com tarefa
  listas e tabelas
* __Kramdown__: Processador avançado com recursos adicionais
  como IALs e tipografia

## Por que usar o Dingus? [why-use-the-dingus]

### Compreendendo as diferenças do processador [understanding-processor-differences]

Diferentes processadores Markdown lidam com a sintaxe de maneira diferente. O
Dingus ajuda você:

* __Compare Output__: Veja exatamente como cada processador é renderizado
  o mesmo Markdown
* __Problemas de depuração__: Identifique por que determinada sintaxe não é
  funcionando como esperado
* __Aprenda Sintaxe__: Entenda as diferenças sutis
  entre implementações de processador

### Testando antes de escrever [testing-before-writing]

Antes de se comprometer com um estilo Markdown específico em seu
documentos:

* __Validate Syntax__: Certifique-se de que seu Markdown será renderizado
  corretamente
* __Choose Processors__: Decida qual processador funciona melhor
  para o seu conteúdo
* __Experimente com segurança__: experimente uma nova sintaxe sem afetar
  seus documentos reais

## Casos de uso comuns [common-use-cases]

### Diferenças de sintaxe de tabela [table-syntax-differences]

Alguns processadores lidam com a sintaxe da tabela de maneira diferente. O Dingus
permite que você veja qual processador suporta melhor sua mesa
necessidades de formatação.

### Suporte para notas de rodapé [footnote-support]

Nem todos os processadores suportam notas de rodapé. Use o Dingus para
verifique se a sintaxe da nota de rodapé funciona com o processador escolhido.

### Matemática e caracteres especiais [math-and-special-characters]

Teste como diferentes processadores lidam com matemática
expressões e caracteres tipográficos especiais.

## Dicas para uso eficaz [tips-for-effective-use]

1. __Start Simple__: Comece com Markdown básico e gradualmente
   adicionar complexidade
2. __Teste casos extremos__: experimente combinações de sintaxe incomuns para
   entenda os limites do processador
3. __Compare Side-by-Side__: Alternar entre processadores para
   veja as diferenças claramente
4. __Use Conteúdo Real__: Copie o conteúdo real do seu
   documentos para testar cenários do mundo real

O Dingus é uma ferramenta poderosa para quem deseja
compreender as nuances de diferentes implementações de Markdown
e garantir que seu conteúdo seja renderizado corretamente em vários
plataformas e processadores.

[1]: images/dingus-interface-800.jpg @2x width=800px height=573px class=center
[2]: x-marked-3://dingus
[3]: #editing-in-the-dingus