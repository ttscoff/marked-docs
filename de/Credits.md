# <%= @title %>

Marked wurde mit viel Hilfe der Open-Source-Community erstellt. Auf dieser Seite wird der Code von Drittanbietern aufgeführt, der in Marked enthalten ist. Der vollständige Lizenztext für die Markdown-Prozessoren ist auf den verlinkten Seiten in [About Markdown](MultiMarkdown_Information.html) verfügbar.

## Markdown-Prozessoren und -Konvertierung [markdown-processors-and-conversion]

| Komponente | Autoren | Lizenz | Wird für |
| --- | --- | --- | --- |
| [MultiMarkdown](MultiMarkdown_License.html) | [John Gruber](http://daringfireball.net/), [Fletcher Penney](http://fletcherpenney.net/) | BSD-Stil | Standard-Markdown-Prozessor |
| [Discount](Discount_License.html) | [David Loren Parsons](http://www.pell.portland.or.us/~orc/) | BSD | Alternativer Markdown-Prozessor (über GHMarkdownParser) |
| [GHMarkdownParser](Discount_License.html) | [Oliver Letterer](https://github.com/OliverLetterer) | MIT | Objective-C-Wrapper um Discount |
| [cmark-gfm](CommonMark_License.html) | [John MacFarlane](https://github.com/jgm) und Mitwirkende | BSD-2-Klausel | Parsing von GitHub Flavored Markdown |
| [Kramdown](Kramdown_License.html) | [Carsten Bormann](https://github.com/gettalong) | MIT | Kramdown-Prozessoroption (im Lieferumfang von Ruby enthalten) |
| [pdf22md](PDF22MD_License.html) | [Adam Twardoch](https://github.com/twardoch) | MIT | PDF-zu-Markdown-Import |

## Nativer Code und Frameworks [native-code-and-frameworks]

| Komponente | Autoren | Lizenz | Wird für |
| --- | --- | --- | --- |
| [Fountain](https://fountain.io/) | Nima Yousefi und John August | MIT | Fountain-Drehbuchanalyse |
| [CocoaLumberjack](https://github.com/CocoaLumberjack/CocoaLumberjack) | Deusty, LLC | BSD-3-Klausel | Debug-Protokollierung |
| [Sparkle](https://sparkle-project.org/) | Sparkle-Projekt | MIT | Automatische Updates (Builds direkt herunterladen) |
| [YACYAML](https://github.com/yaml/YACYAML) | James Montgomerie | BSD-2-Klausel | YAML-Metadatenanalyse |
| [libyaml](https://github.com/yaml/libyaml) | Kirill Simonov | MIT | YAML-Bibliothek (verwendet von YACYAML) |
| [CHCSVParser](https://github.com/davedelong/CHCSVParser) | Dave DeLong | MIT | CSV-Tabellenimport |
| [RNTextStatistics](https://github.com/rnystrom/RNTextStatistics) | Ryan Nystrom | MIT | Lesbarkeit und Textstatistik |
| [RegexKitLite](http://regexkit.sourceforge.net/) | John Engelhart | BSD | Dienstprogramme für reguläre Ausdrücke |
| [RegExCategories](https://github.com/bendytree/Objective-C-RegEx-Categories) | Josh Wright | MIT | Kategorien für reguläre Ausdrücke |
| [AppSandboxFileAccess](https://github.com/leighmcculloch/AppSandboxFileAccess) | Leigh McCulloch | BSD-2-Klausel | Sandbox-Dateizugriffshilfen |
| [VDKQueue](https://github.com/bdkjones/VDKQueue) | Bryan D K Jones | Eigene, freizügige Lizenz | Benachrichtigungen über Dateiänderungen |
| [minizip](https://www.winimage.com/zLibDll/minizip.html) | Gilles Vollant; Info-ZIP | zlib-Stil | Handhabung von ZIP-Archiven |
| [JNWScrollView](https://github.com/jonathonjohnson/JNWScrollView) | ButterKit | MIT | Dienstprogramme für Bildlaufansicht |
| [DBPrefsWindowController](http://www.mere-mortal-software.com/blog/) | Dave Batton | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | Symbolleiste des Fensters „Einstellungen“ |
| [NTYCSVTable](https://github.com/naotokano/NTYCSVTable) | Naoto Kaneko | Siehe Projekt | CSV-Tabellen-Rendering |
| [DJProgressHUD](https://github.com/DanielJackson-DJ/DJProgressHUD) | Daniel Jackson | Siehe Projekt | Fortschrittsindikatoren |
| [IAPManager](https://github.com/mruegenberg/IAPManager) | Marcel Ruegenberg | Siehe Projekt | In-App-Kaufhilfen (alt) |

## Vorschau-JavaScript [preview-javascript]

Diese Bibliotheken sind im Vorschaupaket von Marked (`marked.min.js` und zugehörige Ressourcen) zusammengefasst:

| Komponente | Autoren | Lizenz | Wird für |
| --- | --- | --- | --- |
| [jQuery](https://jquery.com/) | jQuery Foundation | MIT | DOM- und Event-Dienstprogramme |
| [Hammer.js](https://hammerjs.github.io/) | Jorik Tangelder | MIT | Berührungs- und Gestenhandhabung |
| [Highlight.js](https://highlightjs.org/) | Josh Goebel und Mitwirkende | BSD-3-Klausel | Syntaxhervorhebung |
| [MathJax](MathJax.html) | Das MathJax-Konsortium | Apache-2.0 | Mathe-Rendering (lokales Bundle) |
| [KaTeX](https://katex.org/) | Khan Academy und Mitwirkende | MIT | Mathematische Darstellung (Option KaTeX) |
| [Mermaid](https://mermaid.js.org/) | Mermaid-Mitwirkende | MIT | Diagrammdarstellung |
| [Modernizr](https://modernizr.com/) | Faruk Ates, Paul Irish, Alex Sexton | MIT | Merkmalserkennung |
| [html5shiv](https://github.com/aFarkas/html5shiv) | Alexander Farkas | MIT/GPL2 | HTML5-Elementunterstützung (über Modernizr-Build) |
| [Yepnope](https://github.com/SlexAxton/yepnope) | Alex Sexton und Paul Irish | MIT/WTFPL | Laden des Skripts (über Modernizr-Build) |
| [BookBlock](https://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/) | Codrops | MIT | Page-Flip-Präsentationsmodus |
| [jwerty](https://github.com/keithamus/jwerty) | Keith Cirkel; Ben Alman (Throttling/Debouncing) | MIT | Tastaturkürzel |
| [bidiweb](https://github.com/tylergaw/js-bidiweb) | Hasen el Judy | WTFPL | Bidirektionale Texterkennung |
| [strftime.js](https://github.com/phillipTellis/strftime-js) | Philip S Tellis | BSD | Datumsformatierung |
| [viewport.js](https://github.com/tuupola/jquery_viewport) | Mika Tuupola | MIT | Viewport-Erkennung |
| [wordhighlight.js](https://github.com/bartaz/sandbox.js) | Bartek Szopka | MIT | Hervorhebung der Suche im Dokument |

## Lokalisierung [localization]

Marked ist dank freiwilliger Übersetzer in mehreren Sprachen verfügbar:

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

## Danksagungen [acknowledgments]

Vielen Dank auch an Daniel Jalkut für die jahrelange Anleitung und an Felippe van Eekhout für das Marked-Symbol.
