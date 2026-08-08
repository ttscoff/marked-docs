<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Mapas mentais e contornos podem ser incorporados em sua visualização do Markdown usando [sintaxe de inclusão do Marked][include] ou [sintaxe de bloco do IA Writer][ia]. O comportamento depende do formato do arquivo e da configuração "Incorporar mapas como diagramas de sereia" em {% prefspane Apps %} em *Mapas Mentais/Contornos*.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Formatos Suportados [supported-formats]

### iPensamentos X (.itmz) [ithoughts-x-itmz]

Os arquivos de mapas mentais do iThoughts são arquivos zip contendo dados do mapa e uma imagem de visualização opcional.

### MindManager (.mmap) [mindmanager-mmap]

Os arquivos MindManager são arquivos zip contendo `Document.xml`. Pacotes MindManager descompactados (uma pasta contendo `Document.xml`) e caminhos diretos para `Document.xml` também são suportados.

### FreeMind (.mm) [freemind-mm]

Os arquivos de mapas mentais do FreeMind usam a extensão `.mm` e armazenam dados como XML. Marked detecta o formato FreeMind verificando se o conteúdo do arquivo começa com `<map`; caso contrário (por exemplo, um trecho de código), o arquivo será incluído como texto simples. Os arquivos FreeMind são suportados para incorporação de mapas mentais Mermaid.

### OPML (.opml) [opml-opml]

OPML (Outline Processor Markup Language) é um formato XML para contornos hierárquicos, amplamente utilizado por delineadores e leitores de feeds. iThoughts e outros aplicativos podem exportar para OPML. As conversões marcadas incluíam arquivos OPML em diagramas de mapas mentais Mermaid.

### Bicicleta (.bike) [bike-bike]

Os contornos do Bike.app são armazenados como arquivos HTML proprietários (`.bike`). Você pode abrir um arquivo `.bike` diretamente no Marked: o documento é renderizado como Markdown com o nome do arquivo (menos a extensão) como o título principal (H1), itens de cabeçalho de nível superior como H2, títulos aninhados como itens de lista em negrito e tarefas como caixas de seleção no estilo GitHub. Quando um arquivo `.bike` é incluído por meio da sintaxe de inclusão, a configuração "Incorporar como diagrama Sereia" para Bicicleta (em Aplicativos → Mapas Mentais/Esboços) controla se ele se torna um mapa mental Sereia (com o nome do arquivo como nó raiz) ou uma lista Markdown aninhada (sem H1).

## Incorporar mapas como diagramas Mermaid [embed-maps-as-mermaid-diagrams]

Quando **ativado** (o padrão), as conversões marcadas incluem mapas mentais e contornos para diagramas [Sereia](https://mermaid.js.org/):

**iThoughts, MindManager, FreeMind, OPML e Bike** — Renderizados como diagramas de mapa mental Mermaid com layout de árvore organizada. Para iThoughts e MindManager, as informações de forma (arredondado, retângulo, hexágono, etc.) são preservadas quando disponíveis. FreeMind (`.mm`) e OPML usam o mesmo formato de mapa mental. Os contornos da bicicleta (`.bike`) usam o nome do arquivo incluído (menos a extensão) como o nó raiz do mapa mental. Os rótulos dos nós são texto simples (os links se tornam texto do link; as tarefas são mostradas como prefixos ☐ / ☑). Mermaid está incluída por padrão em todas as visualizações do Markdown.

**Limitação:** A incorporação de mapas mentais (diagramas de sereia) não funciona com o analisador de desconto. Use MultiMarkdown, CommonMark (GFM) ou Kramdown para visualizações de mapas mentais.

Quando **desativado**:

- **iThoughts** — A imagem de visualização integrada (`preview.png`) do arquivo .itmz é incorporada como uma imagem base64. O texto alternativo da imagem usa o nome do arquivo.
- **MindManager** — O esboço é incorporado como uma lista Markdown aninhada.
- **FreeMind** — O esboço é incorporado como uma lista Markdown aninhada.
- **OPML** — O esboço é incorporado como uma lista Markdown aninhada (sem mapa mental).
- **Bike** — O contorno é incorporado como uma lista Markdown aninhada (sem H1); os itens de cabeçalho de nível superior tornam-se H2, os títulos aninhados ficam em negrito e as tarefas tornam-se caixas de seleção do GitHub.

## Incluir sintaxe [include-syntax]

Use a mesma sintaxe de outros arquivos:

	<<[caminho/para/map.itmz]
	<<[caminho/para/mapa.mmap]
	<<[caminho/para/mapa.mm]
	<<[caminho/para/outline.opml]
	<<[caminho/para/outline.bike]

Ou com a sintaxe do bloco iA Writer:

	/caminho/para/map.itmz

Os caminhos podem ser relativos ao documento principal ou absolutos (começando com `/` ou `~`). Consulte [Documentos com Vários Arquivos](Multi-File_Documents.html) para obter detalhes.

## Conversão OPML [opml-conversion]

Os arquivos OPML usam elementos `<outline>` aninhados com um atributo `text`. Quando "Incorporar como diagrama Sereia" está ativado (consulte [Configurações: Aplicativos](Settings_Apps.html)), a conversão produz um mapa mental Sereia usando o mesmo formato do iThoughts e MindManager:

- Os contornos filhos de `<body>` tornam-se o nível superior (ou filhos de uma raiz "Contorno" se houver vários itens de nível superior)
- Contornos aninhados definem a hierarquia
- `text` ausente ou vazio é mostrado como `(unnamed)`
- O texto é higienizado; caracteres especiais são escapados para Mermaid

## Conversão de bicicleta [bike-conversion]

Os arquivos Bike `.bike` são HTML com itens raiz `<ul>` e `<li>`. Os itens podem ter `data-type="heading"` (nível superior → H2 quando aberto ou no modo de lista; aninhado → negrito) ou `data-type="task"` (caixas de seleção do GitHub; concluído quando `data-done` tem um carimbo de data/hora ou `data-checked` / `data-completed` é verdadeiro). A formatação embutida e os links no texto do nó são convertidos em Markdown. Ao incorporar como um mapa mental Mermaid, o nome do arquivo (menos a extensão) é usado como o nó raiz único e os rótulos são formatados em texto simples para a sintaxe do mapa mental Mermaid.