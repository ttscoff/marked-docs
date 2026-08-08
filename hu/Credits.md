<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked a nyílt forráskódú közösség sok segítségével készült. Ez az oldal harmadik féltől származó kódot sorol fel, amelyet a Markeden belül szállítanak. A Markdown processzorok teljes licencszövege a [A Markdown névjegye](MultiMarkdown_Information.html) hivatkozási oldalain érhető el.

## Markdown processzorok és átalakítás [markdown-processors-and-conversion]

| Alkatrész | Szerzők | Licenc | Használt |
| --- | --- | --- | --- |
| [MultiMarkdown](MultiMarkdown_License.html) | [John Gruber](http://daringfireball.net/), [Fletcher Penney](http://fletcherpenney.net/) | BSD-stílusban | Alapértelmezett Markdown processzor |
| [Kedvezmény](Discount_License.html) | [David Loren Parsons](http://www.pell.portland.or.us/~orc/) | BSD | Alternatív Markdown processzor (a GHMarkdownParseren keresztül) |
| [GHMarkdownParser](Discount_License.html) | [Letterer Olivér](https://github.com/OliverLetterer) | MIT | Objective-C wrapper around Kedvezmény |
| [cmark-gfm](CommonMark_License.html) | [John MacFarlane](https://github.com/jgm) és közreműködők | BSD-2-Clause | GitHub ízesítésű Markdown elemzése |
| [Kramdown](Kramdown_License.html) | [Carsten Bormann](https://github.com/gettalong) | MIT | Kramdown processzor opció (Ruby csomagban) |
| [pdf22md](PDF22MD_License.html) | [Adam Twardoch](https://github.com/twardoch) | MIT | PDF a Markdown importba |

## Natív kód és keretrendszerek [native-code-and-frameworks]

| Alkatrész | Szerzők | Licenc | Használt |
| --- | --- | --- | --- |
| [Szökőkút](https://fountain.io/) | Nima Yousefi és John August | MIT | Fountain forgatókönyv elemzése |
| [Kakaófavágó](https://github.com/CocoaLumberjack/CocoaLumberjack) | Deusty, LLC | BSD-3-Clause | Hibakeresési naplózás |
| [Sparkle](https://sparkle-project.org/) | Sparkle Project | MIT | Automatikus frissítések (közvetlen letöltésű buildek) |
| [YACYAML](https://github.com/yaml/YACYAML) | James Montgomerie | BSD-2-Clause | YAML metaadatok elemzése |
| [libyaml](https://github.com/yaml/libyaml) | Kirill Simonov | MIT | YAML könyvtár (a YACYAML használja) |
| [CHCSVParser](https://github.com/davedelong/CHCSVParser) | Dave DeLong | MIT | CSV-tábla importálása |
| [RNTextStatistics](https://github.com/rnystrom/RNTextStatistics) | Ryan Nystrom | MIT | Olvashatóság és szövegstatisztika |
| [RegexKitLite](http://regexkit.sourceforge.net/) | John Engelhart | BSD | Reguláris kifejezés segédprogramok |
| [RegExCategories](https://github.com/bendytree/Objective-C-RegEx-Categories) | Josh Wright | MIT | Reguláris kifejezés kategóriái |
| [AppSandboxFileAccess](https://github.com/leighmcculloch/AppSandboxFileAccess) | Leigh McCulloch | BSD-2-Clause | Sandbox fájlelérési segítők |
| [VDKQueue](https://github.com/bdkjones/VDKQueue) | Bryan D K Jones | Egyéni megengedő | Fájlmódosítási értesítések |
| [minizip](https://www.winimage.com/zLibDll/minizip.html) | Gilles Vollant; Info-ZIP | zlib-style | ZIP archívum kezelése |
| [JNWScrollView](https://github.com/jonathonjohnson/JNWScrollView) | ButterKit | MIT | Görgetéses nézet segédprogramok |
| [DBPrefsWindowController](http://www.mere-mortal-software.com/blog/) | Dave Batton | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | Beállítások ablak eszköztár |
| [NTYCSVTable](https://github.com/naotokano/NTYCSVTable) | Naoto Kaneko | Lásd a projektet | CSV-tábla megjelenítése |
| [DJProgressHUD](https://github.com/DanielJackson-DJ/DJProgressHUD) | Daniel Jackson | Lásd a projektet | Előrehaladási mutatók |
| [IAPMager](https://github.com/mruegenberg/IAPManager) | Marcel Ruegenberg | Lásd a projektet | Alkalmazáson belüli vásárlási segítők (örökölt) |

## JavaScript előnézete [preview-javascript]

Ezek a könyvtárak a Marked előnézeti csomagjában vannak összefűzve (`marked.min.js` és a kapcsolódó erőforrások):

| Alkatrész | Szerzők | Licenc | Használt |
| --- | --- | --- | --- |
| [jQuery](https://jquery.com/) | jQuery Foundation | MIT | DOM és rendezvény segédprogramok |
| [Hammer.js](https://hammerjs.github.io/) | Jorik Tangelder | MIT | Érintés- és gesztuskezelés |
| [Highlight.js](https://highlightjs.org/) | Josh Goebel és közreműködők | BSD-3-Clause | Szintaxis kiemelés |
| [MathJax](MathJax.html) | A MathJax Konzorcium | Apache-2.0 | Matematikai megjelenítés (helyi csomag) |
| [KaTeX](https://katex.org/) | Khan Academy és közreműködők | MIT | Matematikai renderelés (KaTeX opció) |
| [Hableány](https://mermaid.js.org/) | Mermaid közreműködők | MIT | Diagram renderelés |
| [Modernizr](https://modernizr.com/) | Faruk Ates, Paul Irish, Alex Sexton | MIT | Funkcióészlelés |
| [html5shiv](https://github.com/aFarkas/html5shiv) | Farkas Sándor | MIT/GPL2 | HTML5 elemek támogatása (a Modernizr builden keresztül) |
| [Yepnope](https://github.com/SlexAxton/yepnope) | Alex Sexton és Paul Irish | MIT/WTFPL | Szkript betöltése (a Modernizr build-en keresztül) |
| [BookBlock](https://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/) | Codrops | MIT | Oldallapozásos prezentációs mód |
| [jwerty](https://github.com/keithamus/jwerty) | Keith Cirkel; Ben Alman (gáz/visszapattanás) | MIT | Billentyűparancsok |
| [bidiweb](https://github.com/tylergaw/js-bidiweb) | Hasen el Judy | WTFPL | Kétirányú szövegészlelés |
| [strftime.js](https://github.com/phillipTellis/strftime-js) | Philip S Tellis | BSD | Dátum formázása |
| [viewport.js](https://github.com/tuupola/jquery_viewport) | Mika Tuupola | MIT | Nézőablak észlelése |
| [wordhighlight.js](https://github.com/bartaz/sandbox.js) | Bartek Szopka | MIT | Dokumentumkeresés kiemelése |

## Lokalizálás [localization]

A Marked több nyelven is elérhető önkéntes fordítóknak köszönhetően:

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

## Köszönetnyilvánítás [acknowledgments]

Köszönet Daniel Jalkutnak is az évekig tartó útmutatásért, és Felippe van Eekhoutnak a Megjelölt ikonért.