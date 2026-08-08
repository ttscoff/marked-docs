<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

O manipulador de URL do Marked fornece recursos adicionais de script e fluxo de trabalho. Você pode incluir uma url nas notas de outro aplicativo, por exemplo, que abrirá um arquivo em Marcado ao ser clicado. Você pode realizar diversas ações, conforme listado abaixo.

## O esquema de URL [the-url-scheme]

O esquema de URL de Marked é `x-marked`, chamado com opções como `x-marked://open?file=/Users/username/Desktop/report.md`.

Você pode segmentar especificamente o Marcado 3 usando `x-marked-3` em vez de `x-marked`. Os métodos e parâmetros são exatamente iguais a `x-marked`, mas apenas Marcado 3 responderá a `x-marked-3`.

## Chamando a partir da linha de comando/scripts [calling-from-the-command-linescripts]

Chamar o manipulador de URL a partir da linha de comando ou de um script pode ser feito usando o macOS [comando `open`](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/):

	abra 'marcado com x: //open?file=filename.md'
	abra 'marcado com x: //refresh?file=filename.md'

### Chamando em segundo plano [calling-in-the-background]

Você pode chamar o comando `open` com o sinalizador `-g` para executar o resultado em segundo plano sem mudar o foco. Para executar o comando em segundo plano e elevar a janela ao topo sem roubar o foco:

	open -g 'marcado com x://open?file=filename.md&raise=true'

## Parâmetros opcionais [optional-parameters]

### x-sucesso [x-success]

Qualquer comando pode fornecer um parâmetro de consulta **x-success**. Defina isso como um URL a ser chamado após executar o comando. Por exemplo: `x-marked://open/?file=filename.md&x-success=ithoughts:`. Você também pode fornecer um identificador de pacote (como `com.googlecode.iterm`) para abrir um aplicativo que não possui um esquema de URL.

### aumentar [raise]

Um parâmetro **raise** pode ser passado com qualquer comando que aceite um parâmetro `file` ou afete todas as janelas. Depois que a ação for executada, as janelas afetadas serão levantadas acima de todas as outras janelas (todos os aplicativos) antes de retornar ou executar um retorno de chamada.

	"marcado com x://refresh?file=filename.md&raise=true"

### leitura rápida [speedread]

Um parâmetro **speedread** pode ser passado com comandos do manipulador de URL que abrem um documento de visualização (`open`, `paste`, `preview` e `stream`). Defina `speedread=1` para iniciar automaticamente a leitura rápida assim que a visualização do alvo estiver pronta.

Exemplos:

	marcado com x://open?file=/Users/username/Desktop/report.md&speedread=1

	marcado com x://preview?text=Some%20text&speedread=1

	marcado com x://paste?speedread=1

# Comandos disponíveis [available-commands]

Os seguintes comandos estão disponíveis para o manipulador de URL `x-marked`.

## adicionar estilo [addstyle]

Adicione um novo estilo personalizado a Marcado.

##### Parâmetros: [parameters]

**css**: texto CSS codificado em URL para gravar em um estilo personalizado. Obrigatório, a menos que passe um parâmetro **file**.

**arquivo**: Caminho completo (POSIX) para um arquivo CSS a ser adicionado ao Marcado. Obrigatório, a menos que passe um parâmetro **css**.

**nome**: O nome do estilo a ser gerado.

Com o parâmetro **css**, será usado tanto como o nome do arquivo ao gravar no disco, com ".css" adicionado, quanto como o nome do item de menu. É obrigatório para o parâmetro **css** e opcional para **file** (o nome do arquivo será usado como se o parâmetro name estivesse vazio).

	marcado com x://addstyle?name=Meu+novo+estilo&css=...

	marcado com x://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

Se você incluir um nome no parâmetro arquivo, o item de menu receberá esse nome em vez do nome do arquivo. Se você usar o mesmo nome novamente com um caminho diferente, o item de menu será atualizado com o novo caminho em vez de adicionar um segundo item com o mesmo nome.

## padrões [defaults]

Defina as configurações do usuário. Aceita uma lista de chaves e valores como parâmetros de consulta. Apenas as chaves existentes serão definidas. Se a mudança de preferência exigir uma atualização, todas as janelas serão atualizadas automaticamente, a menos que `refresh=0` seja aprovado.

Use 1 para verdadeiro e 0 para falso em valores booleanos.

##### Parâmetros: [parameters-2]

**atualizar** _(opcional)_: se definido como 0, a atualização automática de janelas de visualização abertas será desativada

* Padrão: 1 (verdadeiro)

##### Exemplo: [example]

marcado com x://defaults?syntaxHighlight=1&includeMathJax=0

O método `defaults` é projetado principalmente para que o desenvolvedor possa adicionar links para recursos esotéricos que de outra forma não estariam disponíveis em Configurações. No entanto, pode haver algumas opções padrão que você deseja alternar ao automatizar. Algumas configurações comuns que você pode querer controlar durante a automação:

sintaxeHighlight
: ativar ou desativar o realce de sintaxe

incluirMathJax
: habilita ou desabilita o manuseio interno do MathJax

processador
: defina como `multimarkdown` ou `mmd` para alterar o processador para MultiMarkdown, `discount` ou `gfm` para usar o processador de desconto

h1IsPageBreak, h2IsPageBreak, breakBeforeFootnotes
: quebras de página automáticas na exportação antes dos níveis de cabeçalho 1 e 2 e notas de rodapé.


## merda [dingus]

Abra o Markdown Dingus para testar diferentes processadores Markdown.

	marcado com x://dingus

##### Parâmetros: [parameters-3]

**processador** (opcional): Especifique qual processador selecionar por padrão. Valores válidos:

- `multimarkdown` - Processador MultiMarkdown
- `commonmark` - Processador CommonMark (GFM)
- `discount` ou `discount (gfm)` - Processador com desconto
- `kramdown` - Processador Kramdown

Exemplos:

- `x-marked://dingus?processor=kramdown` - Abre com Kramdown selecionado
- `x-marked://dingus?processor=commonmark` - Abre com CommonMark (GFM) selecionado

*Nota:* Isso abre a janela Markdown Dingus, que permite testar e comparar diferentes processadores Markdown (MultiMarkdown, CommonMark (GFM), Discount e Kramdown) lado a lado. Perfeito para experimentar a sintaxe do Markdown e entender as diferenças do processador.

##stylestealer/roubar

Abra o HUD do Style Stealer. Útil quando você deseja capturar CSS de uma página ativa ou executar uma sessão manual de extração de conteúdo sem iniciá-la por meio da IU.

	Sinônimos: marcado com x://stylestealer…, marcado com x://roubar…

##### Parâmetros:

**url** _(opcional)_: Um URL para preencher previamente na janela do Style Stealer. Se omitido, o HUD abre em branco.

Exemplos:

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl/markdownify [stylestealer-steal]

Abra a janela "Importar URL" (Content Extractor) para que você possa executar o pipeline do Markdownifier manualmente. Isso **não** executa a extração automaticamente — isso é feito pelo comando `extract` abaixo.

	Sinônimos: marcado com x://importurl…, marcado com x://markdownify…

##### Parâmetros: [parameters-4]

**url** _(opcional)_: preenche previamente o campo URL de importação. Se omitido, a janela será aberta com um campo vazio aguardando que você cole um link.
**html** _(opcional, somente markdownify)_: Quando fornecido em `x-marked://markdownify`, deve ser HTML bruto codificado em URL. Marcado converterá o HTML em Markdown usando as mesmas regras da Visualização da área de transferência e o abrirá em um documento transitório, como se você tivesse colado esse HTML em uma janela de visualização da área de transferência.

Exemplos:

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## fazer [importurl-markdownify]

Execute um comando JavaScript em uma janela de documento. Toda a API JavaScript do Marked está [documentada aqui](https://markedapp.com/help/jsapi/).

##### Parâmetros: [parameters-5]

**js** _(obrigatório)_: string de consulta contendo um comando JavaScript

* Aceita parâmetros de caminho referenciando nomes de arquivos ou "todos"
* Caminhos divididos por / pesquisarão vários arquivos
* Nomes de arquivos parciais completarão a melhor correspondência

		marcado com x://do/nomedoarquivo1/nomedoarquivo2?js=...
		marcado com x://do/all?js=...

**arquivo**: parâmetro de consulta contendo caminhos/nomes de arquivos separados por vírgula

	marcado com x://do?file=filename1,filename2&js=...

Operará na janela mais frontal se um nome de arquivo não for fornecido (ou "todos" não for passado)

## ajuda [do]

Abra o sistema de ajuda interno marcado, especificando opcionalmente um tópico. Isto é principalmente para uso interno, mas acessível via URL. Um URL para qualquer seção pode ser copiado clicando com o botão direito no ícone do marcador à direita do título e selecionando __Copiar link__. **Marcado 3** A ajuda e a pesquisa no aplicativo usam o esquema `x-marked-3` para esses links, para que o macOS os abra no Marcado 3 quando o Marcado 2 também estiver instalado; os exemplos abaixo usam esse formulário.

##### merda [parameters-6]

Abra o Markdown Dingus para testar diferentes processadores Markdown.

	marcado com x://dingus

######## Parâmetros:

**processador** (opcional): Especifique qual processador selecionar por padrão. Valores válidos:

- `multimarkdown` - Processador MultiMarkdown
- `commonmark` - Processador CommonMark (GFM)
- `discount` ou `discount (gfm)` - Processador com desconto
- `kramdown` - Processador Kramdown

Exemplos:

- `x-marked://dingus?processor=kramdown` - Abre com Kramdown selecionado
- `x-marked://dingus?processor=commonmark` - Abre com CommonMark (GFM) selecionado

*Nota:* Isso abre a janela Markdown Dingus, que permite testar e comparar diferentes processadores Markdown (MultiMarkdown, CommonMark (GFM), Discount e Kramdown) lado a lado. Perfeito para experimentar a sintaxe do Markdown e entender as diferenças do processador.

##### Parâmetros:

**página** _(opcional)_: o título exato de uma página existente, com hash de âncora opcional

	x-marked-3://help?page=Document_Statistics

Os espaços são substituídos por sublinhados, de acordo com a convenção de nomenclatura de arquivos de ajuda marcados. Dois pontos (:) podem ser usados ​​no lugar de um hash (#) ao especificar uma âncora.

O destino pode ser especificado apenas pelo caminho (sem string de consulta):

	x-marked-3://help/Keyword_Highlighting:editingkeywords


## extrair [help]

Extraia o conteúdo de um URL da web e abra-o como um novo documento no Marked.

	marcado com x: //extrair?url=https://example.com

##### Parâmetros: [dingus-2]

**url** _(obrigatório)_: o URL da web do qual extrair o conteúdo. Deve começar com `http://` ou `https://`

**janela** _(opcional)_: Nome da janela

**id** _(opcional)_: identificador de namespace

**base** _(opcional)_: URL base para links relativos

**aumentar** _(opcional)_: Defina como `true` para levantar a janela após abrir

**manual** _(opcional)_: Defina como `true` para abrir a janela de extração manual do Style Stealer em vez de realizar a extração automática.

- Quando `manual=true`, Marcado abre o Style Stealer, preenche previamente o campo URL (se fornecido), suprime qualquer caixa de diálogo de abertura automática e permite selecionar e extrair interativamente estilos/conteúdo antes de salvar.
- Quando omitido ou `false`, Marked executa o extrator automático (Markdownifier) ​​e abre o resultado diretamente como um novo documento temporário.

##### Exemplos: [parameters-7]

	marcado com x://extrair?url=https://news.ycombinator.com

	marcado com x://extrair?url=https://github.com&window=GitHub&raise=true

	marcado com x: //extrair?url=https://example.com/article&manual=true

	marcado com x://extrair?url=https://blog.example.com/post-title

*Nota:* Este comando usa o serviço de extração de conteúdo do Marked para buscar páginas da web, extrair conteúdo limpo usando Legibilidade, converter para o formato Markdown e abrir o resultado em um novo documento temporário. O conteúdo extraído inclui metadados (título, URL de origem, data) e é formatado como Markdown limpo. Perfeito para capturar e editar rapidamente conteúdo da web.

## aberto [extract]

Abre o documento especificado em Marcado.

	marcado com x://open?file=/Users/username/Desktop/report.md

##### Parâmetros: [parameters-8]

**arquivo** *(obrigatório)*: O caminho POSIX completo para o documento a ser aberto ou uma lista de caminhos separados por vírgula

**speedread** *(opcional)*: Defina como `1` para iniciar a leitura rápida automaticamente após a abertura.

`open` também aceita um caminho cujos componentes serão combinados em uma única URL

	marcado com x://open/~/nvALT2.2

Se o caminho do arquivo fornecido não existir ou não puder ser aberto, Marcado ainda estará em primeiro plano. Executar sem o parâmetro *file* ou com um valor em branco simplesmente abrirá Marcado.

Marcado também abrirá arquivos se apenas o caminho de um arquivo for chamado no manipulador de URL, por exemplo. `x-marked:///Users/username/Desktop/report.md`.

## colar [open]

Crie um novo documento a partir do conteúdo atual da área de transferência.

	marcado com x: // colar

##### Parâmetros: [parameters-9]

**speedread** *(opcional)*: Defina como `1` para iniciar a leitura rápida automaticamente após abrir a visualização da área de transferência.

*Nota:* Isso cria um documento temporário usando o comando "Visualizar área de transferência". Qualquer texto na sua área de transferência é adicionado a um novo documento em branco, que é então aberto em Marcado. Se fechado sem salvar, é descartado.

## visualização [paste]

Visualize o texto especificado em um novo documento.

	marcado com x://preview?text=Some%20text%20to%20%2A%2Apreview%2A%2A%0A

##### Parâmetros: [parameters-10]

**texto** *(obrigatório)*: O texto a ser inserido na visualização. O texto codificado por porcentagem será decodificado antes da visualização do documento.

**speedread** *(opcional)*: Defina como `1` para iniciar a leitura rápida automaticamente após abrir o texto de visualização.

## fluxo [preview]

Abra uma janela de visualização da área de transferência de streaming.

	marcado com x://stream

##### Parâmetros: [parameters-11]

**speedread** *(opcional)*: Defina como `1` para iniciar a leitura rápida automaticamente após abrir a visualização do streaming.

*Nota:* Isso cria um documento temporário usando o comando "Visualizar área de transferência". O texto passado é adicionado a um novo documento em branco, que é então aberto em Marcado. Se fechado sem salvar, é descartado.

## atualizar [stream]

Atualize uma visualização de documento ou todas as visualizações abertas.

##### Parâmetros: [parameters-12]

**arquivo**: parâmetro de consulta contendo caminhos/nomes de arquivos separados por vírgula (os arquivos devem estar abertos no momento em Marcados). Chamar sem parâmetro `file` ou `?file=all` atualizará todas as janelas abertas.

O parâmetro *file* pode ser parcial. Marcado atualizará todas as janelas abertas com uma correspondência parcial no *nome do arquivo* (não no caminho completo). Passar "tudo" atualizará todas as janelas.

	marcado com x: // atualizar

	marcado com x://refresh?file=/Users/username/Desktop/report.md

	marcado com x://refresh?file=report.md

Se chamado sem parâmetro `file`, mas com caminhos de documento especificados na URL, os caminhos divididos por / pesquisarão vários arquivos e nomes de arquivos parciais completarão a melhor correspondência.

	marcado com x://refresh/filename1/filename2

## estilo [refresh]

Defina o estilo de visualização (CSS) para um ou mais documentos.

##### Parâmetros: [parameters-13]

**css** _(obrigatório)_: string de consulta contendo o nome ou caminho de um estilo. Os estilos devem estar presentes no menu de estilos do Marked como estilos padrão ou personalizados adicionados manualmente.

* Aceita parâmetros de caminho referenciando nomes de arquivos ou "todos"
* Caminhos divididos por / pesquisarão vários arquivos
* Nomes de arquivos parciais completarão a melhor correspondência

		marcado com x://estilo/nomedoarquivo1/nomedoarquivo2?css=...
		marcado com x://style/all?css=...

**arquivo**: parâmetro de consulta contendo caminhos/nomes de arquivos separados por vírgula

	marcado com x://style?file=filename1,filename2&css=...

Este método irá operar na janela frontal se um nome de arquivo não for fornecido (ou "todos" não for passado).