<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked è realizzato con il grande aiuto della comunità open source. Questa pagina elenca il codice di terze parti fornito all'interno di Marked. Il testo completo della licenza per i processori Markdown è disponibile nelle pagine collegate in [Informazioni su Markdown](MultiMarkdown_Information.html).

## Processori di markdown e conversione [markdown-processors-and-conversion]

| Componente | Autori | Licenza | Utilizzato per |
| --- | --- | --- | --- |
| [MultiMarkdown](MultiMarkdown_License.html) | [John Gruber](http://daringfireball.net/), [Fletcher Penney](http://fletcherpenney.net/) | Stile BSD | Processore Markdown predefinito |
| [Sconto](Discount_License.html) | [David Loren Parsons](http://www.pell.portland.or.us/~orc/) | BSD | Processore Markdown alternativo (tramite GHMarkdownParser) |
| [GHMarkdownParser](Discount_License.html) | [Oliver Letterer](https://github.com/OliverLetterer) | MIT | Wrapper Objective-C attorno a Discount |
| [cmark-gfm](CommonMark_License.html) | [John MacFarlane](https://github.com/jgm) e collaboratori | Clausola BSD-2 | Analisi GitHub Flavored Markdown |
| [Kramdown](Kramdown_License.html) | [Carsten Bormann](https://github.com/gettalong) | MIT | Opzione processore Kramdown (Ruby in bundle) |
| [pdf22md](PDF22MD_License.html) | [Adam Twardoch](https://github.com/twardoch) | MIT | Importazione da PDF a Markdown |

## Codice e framework nativi [native-code-and-frameworks]

| Componente | Autori | Licenza | Utilizzato per |
| --- | --- | --- | --- |
| [Fontana](https://fountain.io/) | Nima Yousefi e John August | MIT | Analisi della sceneggiatura di Fountain |
| [CacaoLumberjack](https://github.com/CocoaLumberjack/CocoaLumberjack) | Deusty, LLC | Clausola BSD-3 | Registrazione debug |
| [Scintillio](https://sparkle-project.org/) | Progetto Scintilla | MIT | Aggiornamenti automatici (build con download diretto) |
| [YACYAML](https://github.com/yaml/YACYAML) | James Montgomerie | Clausola BSD-2 | Analisi dei metadati YAML |
| [libiaml](https://github.com/yaml/libyaml) | Kirill Simonov | MIT | Libreria YAML (usata da YACYAML) |
| [CHCSVParser](https://github.com/davedelong/CHCSVParser) | Dave DeLong | MIT | Importazione tabella CSV |
| [RNTextStatistics](https://github.com/rnystrom/RNTextStatistics) | Ryan Nystrom | MIT | Leggibilità e statistiche del testo |
| [RegexKitLite](http://regexkit.sourceforge.net/) | John Engelhart | BSD | Utilità per le espressioni regolari |
| [Categorie RegEx](https://github.com/bendytree/Objective-C-RegEx-Categories) | Josh Wright | MIT | Categorie di espressioni regolari |
| [AppSandboxFileAccess](https://github.com/leighmcculloch/AppSandboxFileAccess) | Leigh McCulloch | Clausola BSD-2 | Aiutanti per l'accesso ai file sandbox |
| [VDKQueue](https://github.com/bdkjones/VDKQueue) | Bryan DK Jones | Permissivo personalizzato | Notifiche di modifica file |
| [minizip](https://www.winimage.com/zLibDll/minizip.html) | Gilles Vollant; Info-ZIP | stile zlib | Gestione archivio ZIP |
| [JNWScrollView](https://github.com/jonathonjohnson/JNWScrollView) | BurroKit | MIT | Utilità di visualizzazione a scorrimento |
| [DBPrefsWindowController](http://www.mere-mortal-software.com/blog/) | Dave Batton | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | Barra degli strumenti della finestra Preferenze |
| [NTYCSVTable](https://github.com/naotokano/NTYCSVTable) | Naoto Kaneko | Vedi progetto | Rendering della tabella CSV |
| [DJProgressHUD](https://github.com/DanielJackson-DJ/DJProgressHUD) | Daniel Jackson | Vedi progetto | Indicatori di progresso |
| [IAPManager](https://github.com/mruegenberg/IAPManager) | Marcel Ruegenberg | Vedi progetto | Assistenti per gli acquisti in-app (legacy) |

## Anteprima JavaScript [preview-javascript]

Queste librerie sono concatenate nel bundle di anteprima di Marked (`marked.min.js` e risorse correlate):

| Componente | Autori | Licenza | Utilizzato per |
| --- | --- | --- | --- |
| [jQuery](https://jquery.com/) | Fondazione jQuery | MIT | DOM e utilità per eventi |
| [Hammer.js](https://hammerjs.github.io/) | Jorik Tangelder | MIT | Gestione del tocco e dei gesti |
| [Highlight.js](https://highlightjs.org/) | Josh Goebel e collaboratori | Clausola BSD-3 | Evidenziazione della sintassi |
| [MathJax](MathJax.html) | Il Consorzio MathJax | Apache-2.0 | Rendering matematico (pacchetto locale) |
| [KaTeX](https://katex.org/) | Khan Academy e collaboratori | MIT | Rendering matematico (opzione KaTeX) |
| [Sirena](https://mermaid.js.org/) | Collaboratori della sirena | MIT | Rappresentazione del diagramma |
| [Modernizr](https://modernizr.com/) | Faruk Ates, Paul Irish, Alex Sexton | MIT | Rilevamento delle funzionalità |
| [html5shiv](https://github.com/aFarkas/html5shiv) | Alexander Farkas | MIT/GPL2 | Supporto per elementi HTML5 (tramite Modernizr build) |
| [Sì](https://github.com/SlexAxton/yepnope) | Alex Sexton e Paul irlandese | MIT/WTFPL | Caricamento dello script (tramite Modernizr build) |
| [BloccoLibro](https://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/) | Codrops | MIT | Modalità di presentazione sfoglia pagina |
| [jwerty](https://github.com/keithamus/jwerty) | Keith Cirkel; Ben Alman (acceleratore/rimbalzo) | MIT | Scorciatoie da tastiera |
| [bidiweb](https://github.com/tylergaw/js-bidiweb) | Hasen el Judy | WTFPL | Rilevamento testo bidirezionale |
| [strftime.js](https://github.com/phillipTellis/strftime-js) | Filippo S Tellis | BSD | Formattazione della data |
| [viewport.js](https://github.com/tuupola/jquery_viewport) | Mika Tuupola | MIT | Rilevamento del viewport |
| [wordhighlight.js](https://github.com/bartaz/sandbox.js) | Bartek Szopka | MIT | Evidenziazione della ricerca nel documento |

## Localizzazione [localization]

Marked è disponibile in più lingue grazie a traduttori volontari:

-Akira
-Brett Crawley
- Enoch Ko
- Flemming Mahler
- Hans Tammen
-Mathias Maul
-Miguel Martínez de la Torre
- Normand Primeau
-PG Neuromonaco
- Richard Kranendonk
- Sébastien Gaïde
-Yuki Tamari
- 亮 王

## Ringraziamenti [acknowledgments]

Grazie anche a Daniel Jalkut per anni di guida e a Felippe van Eekhout per l'icona Marked.