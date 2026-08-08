<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked inclui um dicionário AppleScript para automatizar a visualização, exportação e integração de fluxo de trabalho. Você pode abrir documentos, controlar a visualização (recarregar, rolar, realçar, rolagem automática, leitura rápida), ler estatísticas, alterar processadores e estilos, copiar HTML ou RTF para a área de transferência e exportar para a maioria dos mesmos formatos disponíveis no menu {% appmenu File, Export %}. **A visualização dos títulos/índice via AppleScript é um trabalho em andamento** (veja abaixo).

Para automação baseada em URL (shell scripts, comandos `open` e retornos de chamada), consulte [Manipulador de URL](URL_Handler.html). AppleScript e o manipulador de URL se complementam: use AppleScript quando precisar direcionar um documento ou janela específica e URLs quando uma simples chamada `open 'x-marked://...'` for suficiente.

## Visualizando o dicionário [viewing-the-dictionary]

No **Editor de Scripts**, escolha **Arquivo → Abrir Dicionário…** e selecione Marcado. O dicionário lista comandos nos objetos **application**, **document** e **window**, além de comandos de exportação no conjunto Marked.

No macOS, você pode navegar pelas definições de script com o **Editor de Scripts**.

## Segmentação marcada [targeting-marked]

Para a instalação padrão:

```applescript
tell application "Marked"
	-- commands here
end tell
```

## Documentos e janelas [documents-and-windows]

**Inscrição**

- `documents` -- abre documentos de visualização (lista ordenada).
- `windows` -- visualizar janelas.

**Documento**

- `name` -- nome de exibição.
- `path` -- caminho do arquivo quando o documento é salvo no disco.
- `modified` -- se o documento possui alterações de editor não salvas.
- `processor` -- Processador Markdown para esta visualização (leitura/gravação). Nomes válidos: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. A configuração `processor` aplica uma substituição por documento e recarrega a visualização; isso não altera o padrão global em {% prefspane Processor %}.
- `preprocessor` -- pré-processador para esta visualização (leitura/gravação). Use `true` ou `false` para ativar ou desativar o pré-processador personalizado ou um nome de pré-processador quando aplicável.
- `source text` -- fonte Markdown bruta (somente leitura).
- `critic markup mode` -- se o processamento CriticMarkup está habilitado (leitura/gravação). Alterá-lo recarrega a visualização.
- `is autoscrolling` -- se a rolagem automática está ativa (somente leitura).
- `is speed reading` -- se o modo de leitura rápida está ativo (somente leitura).
- Comandos de visualização, leitor, estatísticas e exportação (veja abaixo).

**Janela**

- `document` -- o `MarkdownDocument` mostrado nessa janela.
- `style` -- nome do estilo de visualização atual (leitura/gravação). A configuração `style` recarrega a visualização com o tema escolhido (o mesmo que escolher um estilo no menu de estilos de visualização).
- `close`, `save`, `print` – comandos de janela padrão.
- Os mesmos comandos de visualização, leitor, estatísticas e exportação dos documentos (encaminhados para o documento da janela).

Prefira `tell document 1` ou `tell window 1's document` ao exportar uma visualização específica. Os comandos de exportação no aplicativo usam a janela principal ou o documento atual quando nenhum receptor é especificado.

### Exemplo: abrir e ler caminho [example-open-and-read-path]

```applescript
tell application "Marked"
	open POSIX file "/Users/you/Documents/report.md"
	set docPath to path of document 1
end tell
```

### Exemplo: alterar estilo de visualização [example-change-preview-style]

```applescript
tell application "Marked"
	tell window 1
		set style to "Amblin"
	end tell
end tell
```

Os nomes dos estilos correspondem ao menu de estilo de visualização (nome de exibição, nome do recurso CSS, como `swiss`, ou identificador interno). Os estilos personalizados adicionados no Gerenciador de estilos são suportados.

Use **`get preview style names`** no objeto do aplicativo para listar os nomes de exibição dos estilos habilitados.

### Exemplo: processador e texto fonte [example-processor-and-source-text]

```applescript
tell application "Marked"
	tell document 1
		set processor to "Kramdown"
		set md to source text
		set critic markup mode to true
	end tell
end tell
```

## Comandos do aplicativo [application-commands]

Esses comandos se aplicam ao objeto **aplicativo** (não a um documento específico).

| Comando | Descrição |
| --- | --- |
| `open streaming preview` | Abra uma janela [visualização da área de transferência de streaming](Streaming_Preview.html). |
| `preview clipboard` | Abra uma [visualização da área de transferência](Opening_Files.html) do conteúdo atual da área de transferência (igual a {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}). |
| `close all` | Feche todos os documentos de visualização abertos (sem solicitação para salvar; Marcado não edita arquivos de origem). |
| `get available processors` | Liste os nomes dos processadores: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. |
| `get preview style names` | Lista os nomes de exibição dos estilos de visualização habilitados. |
| `get_available_formats` | Lista nomes de formatos `convert_to` suportados. |
| `get_available_profiles` | Lista os nomes dos perfis de exportação (iguais à propriedade `profiles`). |

Traga Marcado para a frente com o comando padrão AppleScript **`activate`**:

```applescript
tell application "Marked"
	activate
	open streaming preview
end tell
```

## Controle de visualização [preview-control]

Disponível em **documento** e **janela**. A maioria deles requer um WebView de visualização carregado.

| Comando | Parâmetros | Descrição |
| --- | --- | --- |
| `refresh preview` | — | Recarregue a visualização do arquivo de origem (igual a {% appmenu Preview, Refresh %}). |
| `reveal in finder` | — | Revele o arquivo do documento no Finder. |
| `show highlights` | — | Ative o destaque de palavras-chave (evite palavras, alternativas, voz passiva, listas personalizadas). |
| `full screen` | opcional `enabled` booleano | Entre, saia ou alterne o modo de visualização em tela cheia. |
| `scroll to heading` | `title` ou `id` | Role até um título pelo texto do título visível ou DOM `id`. |
| `scroll to position` | `percent` ou `line` | Role pela porcentagem da altura do documento ou número aproximado da linha. |
| `copy html` | — | Copie o HTML de visualização para a área de transferência (menu de engrenagem ou {% kbd shift cmd C %}; consulte [Copiar HTML](Exporting.html#copyhtml)). |
| `copy rtf` | — | Copie rich text para a área de transferência. |

```applescript
tell application "Marked"
	tell document 1
		refresh preview
		show highlights
		scroll to heading id "introduction"
		scroll to position percent 50
		full screen with enabled true
	end tell
end tell
```

## Rolagem automática e leitura rápida [autoscroll-and-speed-read]

| Comando | Descrição |
| --- | --- |
| `autoscroll` | Inicie a rolagem automática. O número inteiro opcional `wpm` define palavras por minuto antes de iniciar. |
| `stop autoscroll` | Pare a rolagem automática. |
| `pause autoscroll` | Pause ou retome a rolagem automática. |
| `speed read` | Inicie ou alterne [leitura rápida](Speed_Reading.html). |
| `stop speed read` | Pare a leitura de velocidade. |
| `pause speed read` | Pausar ou retomar a leitura de velocidade. |

Verifique o estado com as propriedades do documento `is autoscrolling` e `is speed reading`.

```applescript
tell application "Marked"
	tell document 1
		autoscroll with wpm 250
		-- or: speed read
	end tell
end tell
```

## Estatísticas [statistics]

**`get statistics`** retorna um `statistics_record` com valores numéricos calculados a partir da fonte Markdown atual (não as strings formatadas mostradas na gaveta de estatísticas).

| Propriedade | Descrição |
| --- | --- |
| `word_count` | Contagem de palavras |
| `sentence_count` | Contagem de frases |
| `character_count` | Contagem de caracteres |
| `paragraph_count` | Contagem de parágrafos |
| `average_words_per_sentence` | Média de palavras por frase |
| `average_syllables_per_word` | Média de sílabas por palavra |
| `complex_word_percentage` | Porcentagem de palavras complexas |
| `reading_ease` | Facilidade de leitura Flesch |
| `fog_index` | Índice de nevoeiro de tiro |
| `grade_level` | Nível de escolaridade Flesch–Kincaid |
| `gulpease` | Índice de Gulpease (legibilidade em italiano; `0` quando não aplicável) |
| `gulpease_band` | Banda Gulpease `1`–`4` (quando aplicável) |
| `reading_time_minutes` | Tempo de leitura em **250 WPM** |

```applescript
tell application "Marked"
	set stats to get statistics of document 1
	set wc to stats's word_count
	set fog to stats's fog_index
end tell
```

## Índice (trabalho em andamento) [table-of-contents-work-in-progress]

{% note %}
**WIP — ainda não confiável.** O dicionário inclui uma propriedade **`headings`** e um comando **`headings`** para leitura de títulos de visualização aninhados (registros `heading_item`). Esta automação **não está funcionando corretamente** nas compilações atuais (resultados vazios, erros de coerção ou “nenhum resultado foi retornado”). Isso será corrigido em uma versão posterior. Prefira **`scroll to heading`** com título ou id conhecido até então.
{% endnote %}

**Comportamento planejado** (quando concluído): registros `heading_item` aninhados de títulos na **visualização** (`h1`–`h6`), não do Markdown bruto.

| Propriedade | Descrição |
| --- | --- |
| `title` | Texto do título |
| `id` | Atributo DOM `id` (string vazia quando ausente) |
| `level` | Nível de título `1`–`6` |
| `children` | Lista aninhada de registros `heading_item` |

**`headings`** (propriedade do documento) — todos os níveis. **`headings levels {2, 3}`** (comando) — filtro opcional: apenas as profundidades de rumo (não um intervalo).

```applescript
-- Planned; do not rely on this yet
tell application "Marked"
	set toc to headings of document 1
	set filtered to headings levels {2, 3} of document 1
end tell
```

Use valores `id` com **`scroll to heading id "..."`** quando a automação de títulos estiver estável.

## Imprimir com perfil [print-with-profile]

**`print with profile`** aplica temporariamente as configurações de impressão de um perfil de exportação e, em seguida, imprime o documento (mesmo pacote de preferências dos perfis de exportação de {% prefspane Export %}).

```applescript
tell application "Marked"
	tell document 1
		print with profile "Print Letter"
	end tell
end tell
```

Os nomes dos perfis diferenciam maiúsculas de minúsculas. Após a impressão, Marcado restaura o perfil de exportação anteriormente ativo.

## Exportar perfis [export-profiles]

Os perfis de exportação armazenam pacotes de preferências de exportação/impressão (margens, cabeçalhos, opções de índice e configurações semelhantes de {% prefspane Export %}).

**Leia os nomes dos perfis**

```applescript
tell application "Marked"
	set profileList to profiles
	-- or: get_available_profiles
end tell
```

**Exportar com um perfil**

```applescript
tell application "Marked"
	tell document 1
		export html to "/Users/you/Desktop/report.html" with profile "My Profile"
	end tell
end tell
```

Os nomes dos perfis diferenciam maiúsculas de minúsculas e devem corresponder exatamente a um perfil salvo.

## Comandos de exportação [export-commands]

Os comandos de exportação estão disponíveis nos objetos **application**, **document** e **window**. Cada comando requer um parâmetro **`to`** com o caminho de saída (string de caminho POSIX ou objeto `file`).

| Comando | Saída |
| --- | --- |
| `export markdown` | Remarcação (.md) |
| `export html` | HTML |
| `export paginated pdf` | PDF paginado (layout de impressão) |
| `export continuous pdf` | PDF de rolagem contínua |
| `export epub` | EPUB |
| `export docx` | Microsoft Word (.docx) |
| `export odt` | Texto OpenDocument |
| `export textbundle` | Pacote de texto |
| `export rtf` | RTF |
| `export opml` | OPML |

**Notas**

- O PDF paginado usa o mesmo pipeline de HTML para PDF que {% appmenu File, Export As, Save PDF (Paginated) %}. Não está disponível para documentos de visualização HTML brutos.
- A exportação HTML usa a **visualização renderizada** (o que você vê no WebView), não o arquivo de origem Markdown bruto.
- PDF contínuo captura o layout WebView de visualização atual.

### Exportação básica [basic-export]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Desktop/report.pdf"
	end tell
end tell
```

### Exportar caminhos e sandbox [export-paths-and-sandboxing]

- Use um caminho POSIX completo para o arquivo de destino.
- Marcado pode criar pastas intermediárias quando o caminho de exportação estiver **dentro da pasta do documento aberto** (por exemplo exportando para `.../MyProject/build/output.pdf` enquanto visualiza `.../MyProject/chapter.md`).
- As exportações fora da pasta do documento exigem um caminho gravável que Marcado pode acessar (local do documento salvo, marcadores com escopo de segurança ou pastas que você concedeu por meio de caixas de diálogo Abrir). Se o caminho não for gravável, o comando retornará um erro antes do início da exportação.

## `with` opções (registro de propriedades) [with-options-properties-record]

Em vez de `with profile`, você pode passar um registro de opções usando **`with`** ou **`with properties`**:

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in", fontSize:"14"}
```

O AppleScript reconhece essas chaves diretamente (elas são mapeadas antes da exportação):

| Chave | Descrição | Exemplo |
| --- | --- | --- |
| `style` | Estilo de visualização a ser aplicado antes da exportação (recarregamento da visualização completa) | `"Amblin"`, `"Swiss"` |
| `pageSize` | Imprimir nome do tamanho da página | `"A4"`, `"Letter"` |
| `margins` | Margens de impressão (veja abaixo) | `"1in"`, `"1in 2in"` |
| `fontSize` | Substituir o tamanho da fonte base de exportação/impressão em pontos (PDF paginado e contínuo) | `"14"`, `"12pt"` |

`fontSize` ativa a mesma opção **Tamanho de fonte personalizado para exportação/impressão** de {% prefspane Export %}. Isso não afeta os documentos do Fountain, que usam dimensionamento fixo do roteiro.

Quando `style` é incluído, Marked aplica esse tema, aguarda a visualização terminar de recarregar e depois exporta. Você não precisa de uma etapa `set style` separada.

Outras chaves no registro podem corresponder a nomes de **preferências de exportação** de perfis (mesmas chaves armazenadas em {% prefspane Export %}, como `printBackgrounds`, `printTOC`, `topPrintMargin`). Esses valores são aplicados temporariamente para a exportação.

Você não pode combinar fontes conflitantes descuidadamente: se você usar `with profile`, carregue esse perfil primeiro; se você usar um registro `with`, as chaves de perfil no registro substituirão as configurações atuais dessa exportação.

### Abreviação de margem [margin-shorthand]

O valor `margins` é uma string com uma a quatro medidas. Unidades: `in`, `cm`, `mm`, `pt` ou `"` para polegadas. Um número sem unidade é tratado como pontos.

| Valores | Significado |
| --- | --- |
| `1in` | Todos os lados |
| `1in 2in` | Superior e inferior `1in`, esquerda e direita `2in` |
| `1in 2in 1in` | Superior `1in`, esquerda e direita `2in`, inferior `1in` |
| `1in 2in 1in 2in` | Superior, direita, inferior, esquerda |

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in 2in"}
export paginated pdf to "/path/out.pdf" with {style:"Amblin", margins:"1in 2in 1in 2in"}
```

### Exemplo combinado [combined-example]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Documents/MyBook/build/book.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

## `convert_to` [convert_to]

O objeto de aplicativo também expõe comandos de script herdados:

- **`convert_to`** -- converte texto Markdown ou um caminho de arquivo para um formato (`html`, `pdf`, `epub`, `docx`, `rtf` e outros), opcionalmente com `profile` e `output_path`.
- **`get_available_formats`** -- lista nomes de formatos de conversão suportados.
- **`get_available_profiles`** -- lista nomes de perfis de exportação (igual à propriedade `profiles`).

`convert_to` permanece disponível para fluxos de trabalho mais antigos e automação somente AppleScript.

## Depuração [debugging]

Habilite **Modo de depuração** em {% prefspane Advanced %} (ou a preferência de depuração em Configurações). Marked então registra as etapas de exportação do AppleScript no nível Info com o prefixo `[AppleScript]` no Console.app e no visualizador de log do Marked.

Linhas de registro úteis ao rastrear uma exportação de PDF paginado:

- `paginated PDF: fetching preview HTML`
- `HTMLToPDFGenerator: loadHTMLString`
- `HTMLToPDFGenerator: didFinishLoadForFrame`
- `paginated PDF: generator finished`

Exportações longas (especialmente PDF paginado) suspendem o evento AppleScript até a conclusão para que os clientes não expirem no meio da exportação.

## Erros [errors]

As exportações com falha definem a string de erro do script no comando (visível no Editor de scripts e nos manipuladores `on error`). Mensagens comuns:

- O caminho de exportação é obrigatório.
- O diretório de exportação não existe (fora da pasta do documento).
- Não é possível criar o diretório de exportação ou erro de permissão ao gravar o arquivo.
- Nome do estilo de visualização desconhecido.
- Tempo limite de espera para recarregar a visualização após a mudança de estilo.
- A exportação de PDF paginado expirou ou falhou durante a geração de páginas.

## Integração com outras ferramentas [integration-with-other-tools]

Os aplicativos podem usar a superfície AppleScript do Marked para ler metadados de documentos. Para fluxos de trabalho controlados por shell, observadores de pastas e retornos de chamada do editor, o [Manipulador de URL](URL_Handler.html) costuma ser mais simples. O [Pacote de Bônus Marcado](Workflow_Integration.html#marked-bonus-pack) inclui scripts e serviços adicionais.