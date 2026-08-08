# <%= @title %>

Marked est construit avec beaucoup d'aide de la communauté open source. Cette page répertorie le code tiers fourni dans Marked. Le texte complet de la licence pour les processeurs Markdown est disponible sur les pages liées dans [À propos de Markdown](MultiMarkdown_Information.html).

## Processeurs Markdown et conversion [markdown-processors-and-conversion]

| Composant | Auteurs | Licence | Utilisé pour |
| --- | --- | --- | --- |
| [MultiMarkdown](MultiMarkdown_License.html) | [John Gruber](http://daringfireball.net/), [Fletcher Penney](http://fletcherpenney.net/) | BSD-style | Processeur Markdown par défaut |
| [Discount](Discount_License.html) | [David Loren Parsons](http://www.pell.portland.or.us/~orc/) | BSD | Processeur Markdown alternatif (via GHMarkdownParser) |
| [GHMarkdownParser](Discount_License.html) | [Olivier Letterer](https://github.com/OliverLetterer) | MIT | Wrapper Objective-C autour de Discount |
| [cmark-gfm](CommonMark_License.html) | [John MacFarlane](https://github.com/jgm) et contributeurs | BSD-2-Clause | Analyse Markdown façon GitHub |
| [Kramdown](Kramdown_License.html) | [Carsten Bormann](https://github.com/gettalong) | MIT | Option de processeur Kramdown (Ruby fourni) |
| [pdf22md](PDF22MD_License.html) | [Adam Twardoch](https://github.com/twardoch) | MIT | Import PDF vers Markdown |

## Code et frameworks natifs [native-code-and-frameworks]

| Composant | Auteurs | Licence | Utilisé pour |
| --- | --- | --- | --- |
| [Fountain](https://fountain.io/) | Nima Yousefi et John August | MIT | Analyse du scénario de Fountain |
| [CocoaLumberjack](https://github.com/CocoaLumberjack/CocoaLumberjack) | Deusty, LLC | BSD-3-Clause | Journalisation de débogage |
| [Sparkle](https://sparkle-project.org/) | Sparkle Project | MIT | Mises à jour automatiques (versions à téléchargement direct) |
| [YACYAML](https://github.com/yaml/YACYAML) | James Montgomerie | BSD-2-Clause | Analyse des métadonnées YAML |
| [libyaml](https://github.com/yaml/libyaml) | Kirill Simonov | MIT | Bibliothèque YAML (utilisée par YACYAML) |
| [CHCSVParser](https://github.com/davedelong/CHCSVParser) | Dave DeLong | MIT | Import de tableaux CSV |
| [RNTextStatistics](https://github.com/rnystrom/RNTextStatistics) | Ryan Nystrom | MIT | Lisibilité et statistiques de texte |
| [RegexKitLite](http://regexkit.sourceforge.net/) | John Engelhart | BSD | Utilitaires d'expressions régulières |
| [RegExCategories](https://github.com/bendytree/Objective-C-RegEx-Categories) | Josh Wright | MIT | Catégories d'expressions régulières |
| [AppSandboxFileAccess](https://github.com/leighmcculloch/AppSandboxFileAccess) | Leigh McCulloch | BSD-2-Clause | Aides à l'accès aux fichiers Sandbox |
| [VDKQueue](https://github.com/bdkjones/VDKQueue) | Bryan D K Jones | Custom permissive | Notifications de modification de fichier |
| [minizip](https://www.winimage.com/zLibDll/minizip.html) | Gilles Vollant; Info-ZIP | zlib-style | Gestion des archives ZIP |
| [JNWScrollView](https://github.com/jonathonjohnson/JNWScrollView) | ButterKit | MIT | Utilitaires de vue de défilement |
| [DBPrefsWindowController](http://www.mere-mortal-software.com/blog/) | Dave Batton | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | Barre d'outils de la fenêtre Préférences |
| [NTYCSVTable](https://github.com/naotokano/NTYCSVTable) | Naoto Kaneko | Voir le projet | Rendu de tableaux CSV |
| [DJProgressHUD](https://github.com/DanielJackson-DJ/DJProgressHUD) | Daniel Jackson | Voir le projet | Indicateurs de progression |
| [IAPManager](https://github.com/mruegenberg/IAPManager) | Marcel Ruegenberg | Voir le projet | Aides aux achats intégrés (ancienne version) |

## JavaScript d'aperçu [preview-javascript]

Ces bibliothèques sont concaténées dans le bundle de prévisualisation de Marked (`marked.min.js` et ressources associées) :

| Composant | Auteurs | Licence | Utilisé pour |
| --- | --- | --- | --- |
| [jQuery](https://jquery.com/) | jQuery Foundation | MIT | DOM et utilitaires d'événements |
| [Hammer.js](https://hammerjs.github.io/) | Jorik Tangelder | MIT | Gestion du toucher et des gestes |
| [Highlight.js](https://highlightjs.org/) | Josh Goebel et contributeurs | BSD-3-Clause | Coloration syntaxique |
| [MathJax](MathJax.html) | The MathJax Consortium | Apache-2.0 | Rendu mathématique (bundle local) |
| [KaTeX](https://katex.org/) | Khan Academy et contributeurs | MIT | Rendu mathématique (option KaTeX) |
| [Mermaid](https://mermaid.js.org/) | Mermaid contributors | MIT | Rendu de diagrammes |
| [Modernizr](https://modernizr.com/) | Faruk Ates, Paul Irish, Alex Sexton | MIT | Détection de fonctionnalités |
| [html5shiv](https://github.com/aFarkas/html5shiv) | Alexander Farkas | MIT/GPL2 | Prise en charge des éléments HTML5 (via la version Modernizr) |
| [Yepnope](https://github.com/SlexAxton/yepnope) | Alex Sexton et Paul Irish | MIT/WTFPL | Chargement du script (via la version Modernizr) |
| [BookBlock](https://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/) | Codrops | MIT | Mode de présentation page-flip |
| [jwerty](https://github.com/keithamus/jwerty) | Keith Cirkel; Ben Alman (accélérateur/anti-rebond) | MIT | Raccourcis clavier |
| [bidiweb](https://github.com/tylergaw/js-bidiweb) | Hasen el Judy | WTFPL | Détection de texte bidirectionnelle |
| [strftime.js](https://github.com/phillipTellis/strftime-js) | Philip S Tellis | BSD | Formatage de dates |
| [viewport.js](https://github.com/tuupola/jquery_viewport) | Mika Tuupola | MIT | Détection du viewport |
| [wordhighlight.js](https://github.com/bartaz/sandbox.js) | Bartek Szopka | MIT | Mise en évidence de la recherche dans le document |

## Localisation [localization]

Marked est disponible en plusieurs langues grâce à des traducteurs bénévoles :

- Akira
- Brett Crawley
- Enoch Ko
- Flemming Mahler
- Hans Tammen
- Mathias Maul
- Miguel Martínez de la Torre
- Normand Primeau
- PG Neuromonaco
- Richard Kranendonk
- Sébastien Gaïde
- Yuki Tamari
- 亮 王

## Remerciements [acknowledgments]

Merci également à Daniel Jalkut pour ses années de conseils et à Felippe van Eekhout pour l'icône Marked.
