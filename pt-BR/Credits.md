<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked foi construído com muita ajuda da comunidade de código aberto. Esta página lista o código de terceiros fornecido dentro do Marked. O texto completo da licença para os processadores Markdown está disponível nas páginas vinculadas em [Sobre Markdown](MultiMarkdown_Information.html).

## Processadores Markdown e conversão

| Componente | Autores | Licença | Usado para |
| --- | --- | --- | --- |
| [MultiMarkdown](MultiMarkdown_License.html) | [John Gruber](http://daringfireball.net/), [Fletcher Penney](http://fletcherpenney.net/) | Estilo BSD | Processador Markdown padrão |
| [Desconto](Discount_License.html) | [David Loren Parsons](http://www.pell.portland.or.us/~orc/) | BSD | Processador Markdown alternativo (via GHMarkdownParser) |
| [GHMarkdownParser](Discount_License.html) | [Oliver Letterer](https://github.com/OliverLetterer) | MIT | Wrapper Objective-C em torno do Desconto |
| [cmark-gfm](CommonMark_License.html) | [John MacFarlane](https://github.com/jgm) e colaboradores | Cláusula BSD-2 | Análise de Markdown com sabor do GitHub |
| [Kramdown](Kramdown_License.html) | [Carsten Bormann](https://github.com/gettalong) | MIT | Opção de processador Kramdown (empacotado Ruby) |
| [pdf22md](PDF22MD_License.html) | [Adam Twardoch](https://github.com/twardoch) | MIT | Importação de PDF para Markdown |

## Código e estruturas nativas

| Componente | Autores | Licença | Usado para |
| --- | --- | --- | --- |
| [Fonte](https://fountain.io/) | Nima Yousefi e John August | MIT | Análise do roteiro da fonte |
| [CacauLenhador](https://github.com/CocoaLumberjack/CocoaLumberjack) | Deusty, LLC | Cláusula BSD-3 | Registro de depuração |
| [Brilho](https://sparkle-project.org/) | Projeto Brilho | MIT | Atualizações automáticas (compilações de download direto) |
| [YACYAML](https://github.com/yaml/YACYAML) | James Montgomerie | Cláusula BSD-2 | Análise de metadados YAML |
| [libyaml](https://github.com/yaml/libyaml) | Cirilo Simonov | MIT | Biblioteca YAML (usada por YACYAML) |
| [CHCSVParser](https://github.com/davedelong/CHCSVParser) | Dave DeLong | MIT | Importação de tabela CSV |
| [RNTextStatistics](https://github.com/rnystrom/RNTextStatistics) | Ryan Nystrom | MIT | Legibilidade e estatísticas de texto |
| [RegexKitLite](http://regexkit.sourceforge.net/) | João Engelhart | BSD | Utilitários de expressões regulares |
| [Categorias RegEx](https://github.com/bendytree/Objective-C-RegEx-Categories) | Josh Wright | MIT | Categorias de expressões regulares |
| [AppSandboxFileAccess](https://github.com/leighmcculloch/AppSandboxFileAccess) | Leigh McCulloch | Cláusula BSD-2 | Ajudantes de acesso a arquivos sandbox |
| [VDKQueue](https://github.com/bdkjones/VDKQueue) | Bryan DK Jones | Permissivo personalizado | Notificações de alteração de arquivo |
| [minizip](https://www.winimage.com/zLibDll/minizip.html) | Gilles Vollant; Informações-ZIP | estilo zlib | Tratamento de arquivos ZIP |
| [JNWScrollView](https://github.com/jonathonjohnson/JNWScrollView) | Kit de manteiga | MIT | Utilitários de visualização de rolagem |
| [DBPrefsWindowController](http://www.mere-mortal-software.com/blog/) | David Batton | [CC POR 3.0](https://creativecommons.org/licenses/by/3.0/) | Barra de ferramentas da janela Preferências |
| [Tabela NTYCSV](https://github.com/naotokano/NTYCSVTable) | Naoto Kaneko | Veja projeto | Renderização de tabela CSV |
| [DJProgressHUD](https://github.com/DanielJackson-DJ/DJProgressHUD) | Daniel Jackson | Veja projeto | Indicadores de progresso |
| [IAPManager](https://github.com/mruegenberg/IAPManager) | Marcel Ruegenberg | Veja projeto | Ajudantes de compra no aplicativo (legado) |

## Visualizar JavaScript

Essas bibliotecas são concatenadas no pacote de visualização do Marked (`marked.min.js` e recursos relacionados):

| Componente | Autores | Licença | Usado para |
| --- | --- | --- | --- |
| [jQuery](https://jquery.com/) | Fundação jQuery | MIT | DOM e utilitários de eventos |
| [Martelo.js](https://hammerjs.github.io/) | Jorik Tangelder | MIT | Manipulação de toque e gestos |
| [Destaque.js](https://highlightjs.org/) | Josh Goebel e colaboradores | Cláusula BSD-3 | Destaque de sintaxe |
| [MathJax](MathJax.html) | O Consórcio MathJax | Apache-2.0 | Renderização matemática (pacote local) |
| [KateX](https://katex.org/) | Khan Academy e colaboradores | MIT | Renderização matemática (opção KaTeX) |
| [Sereia](https://mermaid.js.org/) | Contribuidores da sereia | MIT | Renderização de diagrama |
| [Modernizar](https://modernizr.com/) | Faruk Ates, Paul Irish, Alex Sexton | MIT | Detecção de recursos |
| [html5shiv](https://github.com/aFarkas/html5shiv) | Alexandre Farkas | MIT/GPL2 | Suporte a elementos HTML5 (via compilação Modernizr) |
| [Sim, não](https://github.com/SlexAxton/yepnope) | Alex Sexton e Paul Irlandês | MIT/WTFPL | Carregamento de script (via compilação Modernizr) |
| [Bloco de livro](https://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/) | Codrops | MIT | Modo de apresentação de página virada |
| [jwerty](https://github.com/keithamus/jwerty) | Keith Cirkel; Ben Alman (acelerador/debounce) | MIT | Atalhos de teclado |
| [bidiweb](https://github.com/tylergaw/js-bidiweb) | Hasen e Judy | WTFPL | Detecção de texto bidirecional |
| [strftime.js](https://github.com/phillipTellis/strftime-js) | Philip S Tellis | BSD | Formatação de data |
| [viewport.js](https://github.com/tuupola/jquery_viewport) | Mika Tuupola | MIT | Detecção de janela de visualização |
| [wordhighlight.js](https://github.com/bartaz/sandbox.js) | Bartek Szopka | MIT | Destaque de pesquisa no documento |

## Localização

Marcado está disponível em vários idiomas graças a tradutores voluntários:

- Akira
- Brett Crawley
- Enoque Ko
-Flemming Mahler
-Hans Tammen
-Mathias Maul
-Miguel Martínez de la Torre
- Normand Primeau
-PG Neuromonaco
-Richard Kranendonk
-Sébastien Gaïde
-Yuki Tamari
- você

## Agradecimentos

Obrigado também a Daniel Jalkut pelos anos de orientação e a Felippe van Eekhout pelo ícone Marcado.