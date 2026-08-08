# <%= @title %>

## Omheinde codeblokken [fenced-code-blocks]

Omheinde codeblokken zijn standaard ingeschakeld in beide meegeleverde processors (MultiMarkdown en Discount). Omheinde codeblokken worden begrensd door drie of meer tildes (~) of backticks (\`). U kunt er meer dan drie gebruiken, maar de begin- en eindscheidingstekens moeten exact hetzelfde aantal tekens bevatten.

~~~~
    Sommige code moet worden weergegeven als een pre/code-blok
    ~~~~

Talen kunnen worden gespecificeerd met behulp van de taaltitel (of korte titel) na het scheidingsteken in de eerste regel, of tussen accolades (met of zonder voorafgaande punt) na het laatste scheidingsteken. Bijvoorbeeld:

~~~~~robijn
    een of andere robijncode
    ~~~~~

Wordt weergegeven als:

<pre><code class="ruby">wat ruby-code</code></pre>


Of met backticks:

`````
    wat Java-code
    `````{.java}

Marked kan zowel Markdown Extra/Python Markdown (`{.lang}` na het sluiten van de omheining) en Discount (`lang` na de eerste omheining) taalspecificaties detecteren. Het volgende (kortingsformaat) zou hetzelfde resultaat opleveren als het bovenstaande (Python Markdown formaat):

    `````java
    some Java code
    `````


Marked verwerkt ook ingesprongen, omheinde codeblokken, zodat u deze binnen geneste lijsten kunt gebruiken.

De ingebouwde syntaxisaccentuering herkent **256** taalspecificaties (zie [Supported languages](#supported-languages) hieronder). Als er geen taal is opgegeven, wordt deze automatisch gedetecteerd en is deze dus niet vereist voor de preview. De opgegeven taalreeks wordt in de uiteindelijke html uitgevoerd als een klasse op de tag `<code>`.

Zie de sectie over [Marked Special Syntax](Special_Syntax.html#includingcode) om te leren hoe u externe codebestanden in uw document kunt opnemen.

## Syntaxisaccentuering [syntax-highlighting]

![Automatic Syntax Highlighting][highlight]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

Syntaxisaccentuering kan worden ingeschakeld in de {% prefspane Style %}. Het herkent codeblokken, detecteert de taal en geeft kleurgecodeerde uitvoer weer in de preview. Er zijn meerdere thema's beschikbaar, geselecteerd via de vervolgkeuzelijst onder de optie in instellingen. Het geselecteerde thema is van toepassing op alle documenten.

Marked gebruikt [highlight.js](https://highlightjs.org/) om consistente kleurcodering te bieden voor alle typen ingesloten code, inclusief standaard Markdown syntaxis waarbij het specificeren van taal niet is toegestaan. Highlight.js detecteert automatisch goed. Er zijn enkele kleine weergaveverschillen tussen het programma en colorizers zoals Pygments (GitHub stijl), maar de uitvoer is vergelijkbaar. Als je bijvoorbeeld het github.css-thema op Ruby-code gebruikt, wordt bijna de exacte uitvoer weergegeven die je op GitHub zou zien.

> *Het stijlblad GitHub biedt back-upstijlen voor blokken die zijn weergegeven met Pygments. Als de tag `<pre>` zich in een div bevindt met de klasse "highlight", wordt deze weergegeven met de standaardstijl GitHub, niet die van Marked. U kunt de code extern weergeven en HTML plakken, of `pygmentize` gebruiken om deze naar HTML-bestanden weer te geven en deze in te voegen met de [<!--MKPH2--> syntax](Special_Syntax.html#includingcode)*.

De optie "Alleen als de taal is opgegeven" rechts van de syntaxisstijlkiezer is van toepassing op afgeschermde codeblokken. Indien ingeschakeld, wordt syntaxisaccentuering alleen toegepast op codeblokken met een taalspecificatie na het openingshek, b.v.

    ```js
    code
    ```

Syntaxisaccentuering wordt weergegeven in het voorbeeld en in print en PDF export. Indien ingeschakeld in de instellingen en het thema wordt opgenomen bij het exporteren van HTML, wordt de highlight.js-bibliotheek die door Marked wordt gebruikt, ingebed in de uitvoer van HTML, waardoor uw geëxporteerde HTML wordt weergegeven zoals in Marked.

### Ondersteunde talen [supported-languages]

Marked wordt geleverd met **highlight.js 11.11.1**, inclusief alle kerntalen plus grammatica's van derden uit de [highlight.js supported languages](https://highlightjs.readthedocs.io/en/latest/supported-languages.html) lijst. Geef hieronder een naam voor de primaire taal op (of een gedocumenteerde alias zoals `js` voor JavaScript) na het openingshek.

Twee talen die op de highlight.js-site worden vermeld, zijn niet opgenomen in de bundel van Marked: **Pine Script** (upstream-pakket niet beschikbaar) en **Supercollider** (incompatibel met highlight.js 11).

1c, 4d, GN, abap, abnf, accesslog, actionscript, ada, alan, angelscript, apache, apex,
    applescript, arcade, arduino, armasm, asciidoc, aspectj, autohotkey, autoit, avrasm, awk,
    axapta, ballerina, bash, basic, bbcode, blade, bnf, bqn, brainfuck, c, c3, cal, capnproto,
    ceylon, chaos, kapel, cisco, schoon, clojure, clojure-repl, cmake, cobol, coffeescript,
    coq, cos, cpc, cpp, crmsh, crystal, csharp, cshtml-razor, csp, css, curl, cypher, d, dafny,
    dart, delphi, diff, django, dns, dockerfile, dos, dsconfig, dts, stof, dylan, ebnf, elixir,
    iep, erb, erlang, erlang-repl, excel, extempore, fix, flix, fortran, fsharp, func, gams,
    gauss, gcode, gdscript, gf, augurk, glimmer, glsl, gml, go, golo, gradle, graphql, groovy,
    gsql, haml, stuur, haskell, haxe, hlsl, hsp, http, hy, inform7, ini, iptables, irpf90,
    isbl, java, javascript, jboss-cli, jolie, json, julia, julia-repl, kotlin, lang, lasso,
    latex, ldif, leaf, lean, less, lisp, livecodeserver, livescript, llvm, lookml, lsl, lua,
    macaulay2, makefile, markdown, mathematica, matlab, maxima, mel, mercury, mint, mipsasm,
    mirc, mizar, mkb, mlir, mojolicious, monkey, moonscript, motoko, n1ql, geneste tekst, nooit,
    nginx, nim, nix, node-repl, nsis, oak, objectivec, ocaml, ocl, openscad, oxygene, papyrus,
    parser3, perl, pf, pgsql, php, php-template, platte tekst, pony, powershell, verwerking,
    profiel, proloog, eigenschappen, protobuf, marionet, purebasic, python, python-repl, q, qml,
    qsharp, r, redenml, rebol, rib, riscript, riscvasm, roboconf, robot, routeros,
    rpm-specificatiebestand, rsl, ruby, regelstaal, roest, rvt-script, sas, scala, schema, scilab, scss,
    sfz, shell, shexc, smali, smalltalk, sml, solidity, spl, sqf, sql, stan, stata, step21,
    gestructureerde tekst, stylus, subeenheid, slank, snel, taggerscript, tik, tcl, terraform, spaarzaamheid,
    toit, tp, tsql, takje, typescript, unicorn-rails-log, vala, vba, vbnet, vbscript,
    vbscript-html, verilog, vhdl, vim, wasm, winterkoninkje, x86asm, x86asmatt, xl, xml, xquery, xsharp,
    yaml, yul, zenscript, zephir

### Syntaxis die thema's benadrukt [syntax-highlighting-themes]

**239** thema's voor syntaxisaccentuering zijn beschikbaar in de vervolgkeuzelijst {% prefspane Style %}. Thema's worden automatisch geladen vanuit de gebundelde stylesheets van Marked; namen komen overeen met de CSS-bestandsnaam zonder de extensie (bijvoorbeeld `github-dark` laadt `github-dark.css`).

Algemene thema's:

1c-licht, a11y-donker, a11y-licht, agaat, een oude hoop, androidstudio, arduino-licht, arta,
    atoom-één-donker, atoom-één-donker-redelijk, atoom-één-licht, codepen-embed, kleurbrouwer, donker,
    standaard, foundation, github, github-dark, github-dark-dimmed, googlecode, grijstinten,
    hybride, idee, intellij-licht, ir-zwart, isbl-editor-donker, isbl-editor-licht, kimbie-donker,
    kimbie-licht, mono-blauw, monokai, monokai-subliem, nachtuil, nnfx-donker, nnfx-licht, nord,
    obsidiaan, panda-syntaxis-donker, panda-syntaxis-licht, paraiso-donker, paraiso-licht, pojoaque,
    purebasic, qtcreator-dark, qtcreator-light, regenboog, rose-pine, rose-pine-dawn,
    roze-dennen-maan, schoolboek, paarse tinten, decor, stackoverflow-donker,
    stackoverflow-licht, zonnestraal, tokio-nacht-donker, tokio-nacht-licht, morgennacht-blauw,
    morgenavond helder, vs, vs2015, xcode, xt256

Base16-thema's (176 varianten, elk voorafgegaan door `base16-`):

basis16-3024, basis16-apathie, basis16-leerling, basis16-as, basis16-atelier-grot,
    basis16-atelier-grot-licht, basis16-atelier-duin, basis16-atelier-duin-licht,
    base16-atelier-estuarium, base16-atelier-estuarium-licht, base16-atelier-bos,
    basis16-atelier-bos-licht, basis16-atelier-heide, basis16-atelier-heide-licht,
    base16-atelier-lakeside, base16-atelier-lakeside-light, base16-atelier-plateau,
    basis16-atelier-plateau-licht, basis16-atelier-savanne, basis16-atelier-savanne-licht,
    base16-atelier-kust, base16-atelier-zee-licht, base16-atelier-zwavelpool,
    base16-atelier-sulphurpool-light, base16-atlas, base16-bespin, base16-zwart-metaal,
    basis 16-zwart-metaal-bathory, basis 16-zwart-metaal-burzum, basis 16-zwart-metaal-donker-begrafenis,
    basis 16-zwart-metaal-gorgoroth, basis 16-zwart-metaal-onsterfelijk, basis 16-zwart-metaal-khold,
    base16-zwart-metaal-marduk, base16-zwart-metaal-mayhem, base16-zwart-metaal-nijl,
    base16-zwart-metaal-gif, base16-brouwer, base16-helder, base16-brogrammer,
    basis16-borstelbomen, basis16-borstelbomen-donker, basis16-krijt, basis16-circus,
    base16-klassiek-donker, base16-klassiek-licht, base16-codeschool, base16-kleuren,
    base16-cupcake, base16-cupertino, base16-danqing, base16-darcula, base16-donkerviolet,
    basis16-donkermos, basis16-donkertand, basis16-decafé, basis16-standaard-donker, basis16-standaard-licht,
    basis16-dirtysea, basis16-dracula, basis16-rand-donker, basis16-rand-licht, basis16-jaren tachtig,
    basis16-embers, basis16-evenwicht-donker, basis16-evenwicht-grijs-donker,
    base16-evenwicht-grijs-licht, base16-evenwicht-licht, base16-espresso, base16-eva,
    base16-eva-dim, base16-flat, base16-framer, base16-fruit-frisdrank, base16-gigavolt,
    base16-github, base16-google-dark, base16-google-light, base16-grijstinten-donker,
    base16-grijstinten-licht, base16-groen scherm, base16-gruvbox-donker-hard,
    base16-gruvbox-donker-medium, base16-gruvbox-donker-bleek, base16-gruvbox-donker-zacht,
    base16-gruvbox-licht-hard, base16-gruvbox-licht-medium, base16-gruvbox-licht-zacht,
    base16-hardcore, base16-harmonisch16-donker, base16-harmonisch16-licht, base16-heetch-donker,
    base16-heetch-licht, base16-helios, base16-hinkelspel, base16-horizon-donker,
    base16-horizon-licht, base16-humanoid-donker, base16-humanoid-licht, base16-ia-donker,
    base16-ia-licht, base16-ijzig-donker, base16-ir-zwart, base16-isotoop, base16-kimber,
    base16-london-buis, base16-macintosh, base16-Marrakesh, base16-materia, base16-materiaal,
    base16-materiaal-donkerder, base16-materiaal-lichter, base16-materiaal-bleeklicht,
    base16-materiaal-levendig, base16-mellow-paars, base16-mexico-licht, base16-mokka,
    basis16-monokai, basis16-nevel, basis16-noord, basis16-nova, basis16-oceaan, basis16-oceaanvolgende,
    basis16-één-licht, basis16-ééndonker, basis16-outrun-donker, basis16-papierkleur-donker,
    base16-papierkleur-licht, base16-paraiso, base16-pasque, base16-phd, base16-pico,
    base16-pop, base16-porselein, base16-qualia, base16-railscasts, base16-rebecca,
    basis 16-ros-pine, basis 16-ros-pine-dageraad, basis 16-ros-pine-maan, basis 16-sagelight,
    base16-zandkasteel, base16-seti-ui, base16-shapeshifter, base16-zijde-donker,
    base16-silk-light, base16-snazzy, base16-solar-flare, base16-solar-flare-light,
    base16-gesolariseerd-donker, base16-gesolariseerd-licht, base16-spacemacs, base16-zomerkamp,
    base16-zomerfruit-donker, base16-zomerfruit-licht, base16-synth-middernacht-terminal-donker,
    base16-synth-midnight-terminal-light, base16-tango, base16-tender, base16-morgen,
    basis16-morgen-nacht, basis16-schemering, basis16-unikitty-donker, basis16-unikitty-licht,
    base16-vulcan, base16-windows-10, base16-windows-10-light, base16-windows-95,
    basis16-ramen-95-licht, basis16-ramen-hoog-contrast, basis16-ramen-hoog-contrast-licht,
    base16-windows-nt, base16-windows-nt-licht, base16-bos, base16-xcode-dusk,
    base16-zenburn

## GitHub Regeleinden [github-line-breaks]

Marked kan regeleinden in uw alinea's behouden. Selecteer gewoon de {% prefspane Processor %} en vink het vakje aan om regeleinden in alinea's te behouden.

## GitHub Selectievakjes [github-checkboxes]

Lijstitems geformatteerd als:

- [ ] Onvoltooide taak
    - [x] Voltooide taak

zal in het voorbeeld verschijnen als weergegeven selectievakje-items. Er kan geen interactie mee plaatsvinden, maar hun status weerspiegelt eventuele wijzigingen in het brondocument.

## Codeblokverpakking [code-block-wrapping]

In de {% prefspane Style %} vind je een optie onder Lay-out en typografie: "Sta toe dat thema's tekst binnen codeblokken laten lopen." Als u dit uitschakelt, worden alle codeblokken gedwongen de horizontale overloop te scrollen in plaats van deze in te wikkelen, ongeacht de huidige voorbeeldstijl.