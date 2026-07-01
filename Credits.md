# <%= @title %>

Marked is built with a lot of help from the open source community. This page lists third-party code that ships inside Marked. Full license text for the Markdown processors is available on the linked pages in [About Markdown](MultiMarkdown_Information.html).

## Markdown processors and conversion

| Component | Authors | License | Used for |
| --- | --- | --- | --- |
| [MultiMarkdown](MultiMarkdown_License.html) | [John Gruber](http://daringfireball.net/), [Fletcher Penney](http://fletcherpenney.net/) | BSD-style | Default Markdown processor |
| [Discount](Discount_License.html) | [David Loren Parsons](http://www.pell.portland.or.us/~orc/) | BSD | Alternative Markdown processor (via GHMarkdownParser) |
| [GHMarkdownParser](Discount_License.html) | [Oliver Letterer](https://github.com/OliverLetterer) | MIT | Objective-C wrapper around Discount |
| [cmark-gfm](CommonMark_License.html) | [John MacFarlane](https://github.com/jgm) and contributors | BSD-2-Clause | GitHub Flavored Markdown parsing |
| [Kramdown](Kramdown_License.html) | [Carsten Bormann](https://github.com/gettalong) | MIT | Kramdown processor option (bundled Ruby) |
| [pdf22md](PDF22MD_License.html) | [Adam Twardoch](https://github.com/twardoch) | MIT | PDF to Markdown import |

## Native code and frameworks

| Component | Authors | License | Used for |
| --- | --- | --- | --- |
| [Fountain](https://fountain.io/) | Nima Yousefi and John August | MIT | Fountain screenplay parsing |
| [CocoaLumberjack](https://github.com/CocoaLumberjack/CocoaLumberjack) | Deusty, LLC | BSD-3-Clause | Debug logging |
| [Sparkle](https://sparkle-project.org/) | Sparkle Project | MIT | Automatic updates (direct-download builds) |
| [YACYAML](https://github.com/yaml/YACYAML) | James Montgomerie | BSD-2-Clause | YAML metadata parsing |
| [libyaml](https://github.com/yaml/libyaml) | Kirill Simonov | MIT | YAML library (used by YACYAML) |
| [CHCSVParser](https://github.com/davedelong/CHCSVParser) | Dave DeLong | MIT | CSV table import |
| [RNTextStatistics](https://github.com/rnystrom/RNTextStatistics) | Ryan Nystrom | MIT | Readability and text statistics |
| [RegexKitLite](http://regexkit.sourceforge.net/) | John Engelhart | BSD | Regular expression utilities |
| [RegExCategories](https://github.com/bendytree/Objective-C-RegEx-Categories) | Josh Wright | MIT | Regular expression categories |
| [AppSandboxFileAccess](https://github.com/leighmcculloch/AppSandboxFileAccess) | Leigh McCulloch | BSD-2-Clause | Sandbox file access helpers |
| [VDKQueue](https://github.com/bdkjones/VDKQueue) | Bryan D K Jones | Custom permissive | File change notifications |
| [minizip](https://www.winimage.com/zLibDll/minizip.html) | Gilles Vollant; Info-ZIP | zlib-style | ZIP archive handling |
| [JNWScrollView](https://github.com/jonathonjohnson/JNWScrollView) | ButterKit | MIT | Scroll view utilities |
| [DBPrefsWindowController](http://www.mere-mortal-software.com/blog/) | Dave Batton | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | Preferences window toolbar |
| [NTYCSVTable](https://github.com/naotokano/NTYCSVTable) | Naoto Kaneko | See project | CSV table rendering |
| [DJProgressHUD](https://github.com/DanielJackson-DJ/DJProgressHUD) | Daniel Jackson | See project | Progress indicators |
| [IAPManager](https://github.com/mruegenberg/IAPManager) | Marcel Ruegenberg | See project | In-app purchase helpers (legacy) |

## Preview JavaScript

These libraries are concatenated into Marked's preview bundle (`marked.min.js` and related resources):

| Component | Authors | License | Used for |
| --- | --- | --- | --- |
| [jQuery](https://jquery.com/) | jQuery Foundation | MIT | DOM and event utilities |
| [Hammer.js](https://hammerjs.github.io/) | Jorik Tangelder | MIT | Touch and gesture handling |
| [Highlight.js](https://highlightjs.org/) | Josh Goebel and contributors | BSD-3-Clause | Syntax highlighting |
| [MathJax](MathJax.html) | The MathJax Consortium | Apache-2.0 | Math rendering (local bundle) |
| [KaTeX](https://katex.org/) | Khan Academy and contributors | MIT | Math rendering (KaTeX option) |
| [Mermaid](https://mermaid.js.org/) | Mermaid contributors | MIT | Diagram rendering |
| [Modernizr](https://modernizr.com/) | Faruk Ates, Paul Irish, Alex Sexton | MIT | Feature detection |
| [html5shiv](https://github.com/aFarkas/html5shiv) | Alexander Farkas | MIT/GPL2 | HTML5 element support (via Modernizr build) |
| [Yepnope](https://github.com/SlexAxton/yepnope) | Alex Sexton and Paul Irish | MIT/WTFPL | Script loading (via Modernizr build) |
| [BookBlock](https://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/) | Codrops | MIT | Page-flip presentation mode |
| [jwerty](https://github.com/keithamus/jwerty) | Keith Cirkel; Ben Alman (throttle/debounce) | MIT | Keyboard shortcuts |
| [bidiweb](https://github.com/tylergaw/js-bidiweb) | Hasen el Judy | WTFPL | Bidirectional text detection |
| [strftime.js](https://github.com/phillipTellis/strftime-js) | Philip S Tellis | BSD | Date formatting |
| [viewport.js](https://github.com/tuupola/jquery_viewport) | Mika Tuupola | MIT | Viewport detection |
| [wordhighlight.js](https://github.com/bartaz/sandbox.js) | Bartek Szopka | MIT | In-document search highlighting |

## Localization

Marked is available in multiple languages thanks to volunteer translators:

- Akira
- Brett Crawley
- Enoch Ko
- Flemming Mahler
- Hans Tammen
- Mathias Maul
- Miguel Martinez de la Torre
- Normand Primeau
- PG Neuromonaco
- Richard Kranendonk
- Sébastien Gaïde
- Yuki Tamari
- 亮 王

## Acknowledgments

Thanks also to Daniel Jalkut for years of guidance, and to Felippe van Eekhout for the Marked icon.
