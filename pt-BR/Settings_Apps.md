<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opções em {% prefspane Apps %}:

(Consulte [Suporte adicional para aplicativos](Additional_Application_Support.html))

![Configurações: Aplicativos][1]

[1]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Configurações gerais

Editor de texto
: selecione um editor de texto para receber o documento atual ao digitar {% kbd cmd E %}.

Edite novos arquivos automaticamente
: Ao utilizar o comando "Novo Arquivo", esta opção abrirá automaticamente o arquivo criado no editor externo de sua escolha.

Links para arquivos de texto devem abrir em:
: determine o comportamento de Marked quando um link clicado em uma janela de visualização leva a um arquivo de texto local.

Editor de imagens
: Selecione um aplicativo para abrir quando uma imagem local for clicada com o botão direito e "Editar imagem" for selecionado.

Editor de anotação/marcação de imagem
: selecione um aplicativo para abrir quando uma imagem local for clicada com o botão direito e "Anotar imagem" estiver selecionado.

Se nenhum editor for escolhido, Marcado apresenta um menu de aplicativos instalados quando você edita ou anota. O menu inclui ferramentas comuns de Markdown, imagem e anotação encontradas no seu Mac, uma opção **Outros…** para escolher qualquer aplicativo de `/Applications` e **Sempre usar este aplicativo** (ativado por padrão) para salvar sua escolha como padrão. Use o botão Limpar (círculo com um X) próximo a cada controle Escolher em {% prefspane Apps %} para remover uma seleção e retornar ao seletor.

### Configurações específicas do aplicativo

Mostrar comentários e anotações por padrão
: Se marcada, as anotações feitas nos documentos Scrivener, Fountain, Word e CriticMarkup aparecerão destacadas na visualização. Desmarque para ocultar completamente. Eles também podem ser alternados durante a leitura de um documento no menu {% appmenu Gear, Proofing ({{ctrl}}{{cmd}}C)%}.
: quando os comentários estão ativados, comentários e notas de rodapé aparecerão em uma barra lateral. Passar o mouse sobre um comentário apontará para onde ele ocorre no documento.

####DocC

[(Informações sobre suporte DocC)](DocC_Support.html)

Resolver referências de imagem DocC
: Dentro de um catálogo de documentação `.docc`, resolva referências `![](ImageName)` sem extensão para imagens na pasta `Resources` do catálogo, incluindo variantes `~dark` e `@2x`.

Resolver variantes de imagem escura e @2x
: Para imagens locais com extensão de arquivo (`images/icon.png`), detecte os arquivos complementares `~dark` e `@2x` na mesma pasta e emita a marcação `<picture>` responsiva. Funciona em qualquer documento Markdown ou HTML, não apenas em catálogos DocC. Consulte [Variantes de imagem](Image_Variants.html).

#### Marca de gancho

Resolva URLs hook:// em imagens e links
: Marked pode ler URLs criados pelo Hookmark, resolvendo-os para seu caminho no disco.

####Leanpub/GitBook

Habilitar suporte Leanpub
: Interpreta arquivos nomeados `Book.txt` como arquivos de índice e manipula a sintaxe Leanpub especial.

Habilite o suporte GitBook
: Interpreta arquivos nomeados `SUMMARY.md` como arquivos de índice para documentação do GitBook.

#### Markdownificador

Use links embutidos
: os documentos Markdown criados pelo Markdownifier usarão links embutidos em vez de links de referência.

#### Marte

Incluir o título da postagem como cabeçalho Markdown (h1)
: use o título da postagem selecionada como cabeçalho Markdown.

Mostrar metadados como tabela
: Quando ativado, metadados como categorias e títulos serão exibidos como uma tabela Markdown na visualização.

#### Pastas

Visualize apenas essas extensões
: Ao abrir uma pasta, Marcado procurará o documento alterado mais recentemente, padronizando extensões como `md`, `mmd` e `html`. A lista aqui substitui o padrão.

#### Escriturário

[(Informações sobre suporte do Scrivener)](Scrivener_Support.html)

Incluir títulos de documentos como cabeçalhos Markdown
: analisa o título das páginas e páginas aninhadas para criar cabeçalhos Markdown hierárquicos.

Adicionar metadados de compilação (título, autor) quando ausentes
: Quando um projeto Scrivener não possui documento `metadata` ou cabeçalho MultiMarkdown existente, acrescente Título e Autor nas configurações de compilação do projeto (`Settings/compile.xml`).

Abra arquivos .scriv no Scrivener quando abertos no Marked
: quando um documento do Scrivener é aberto no Marked, abra-o automaticamente também no Scrivener.

#### Palavra

Converter controle de alterações <-> CriticMarkup
: se ativado, o controle de alterações em documentos do Word será convertido em CriticMarkup quando importado, e o CriticMarkup será convertido em controle de alterações do Word ao exportar arquivos DOCX.

#### Mapas Mentais/Esboços {#MindMapsOutlines}

Incorporar mapas mentais como sereia
: cada caixa de seleção controla um formato incluído. Quando **ativado**, o arquivo incluído é convertido em um diagrama de mapa mental Mermaid (layout de árvore organizada). Quando **desativado**, Marcado usa a alternativa para esse formato.
: **Mapas mentais** — iThoughts X (.itmz), MindManager (.mmap), FreeMind (.mm). Se estiver ativado: mapa mental da sereia. Se desativado: o iThoughts incorpora sua imagem de visualização; MindManager e FreeMind são convertidos em listas Markdown aninhadas.
: **Arquivos OPML** (.opml). Se estiver ativado: mapa mental da sereia. Se desativado: lista Markdown aninhada.
: **Contornos do OmniOutliner** (.ooutline). Se estiver ativado: mapa mental da sereia. Se desativado: lista Markdown aninhada (ou lista de verificação quando aplicável).
: **Contornos da bicicleta**. Se estiver ativado: mapa mental da sereia. Se desativado: lista Markdown aninhada.