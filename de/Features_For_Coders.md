# <%= @title %>

## Abgegrenzte Codeblöcke [fenced-code-blocks]

Abgegrenzte Codeblöcke sind in beiden enthaltenen Prozessoren (MultiMarkdown und Discount) standardmäßig aktiviert. Sie werden durch drei oder mehr Tilden (~) oder Backticks (\`) begrenzt. Sie können mehr als drei Zeichen verwenden, aber das öffnende und das schließende Trennzeichen müssen aus genau gleich vielen Zeichen bestehen.

    ~~~~
    Some code to be rendered as a pre/code block
    ~~~~

Sprachen können mit dem Namen (oder Kurznamen) der Sprache nach dem Trennzeichen in der ersten Zeile oder in geschweiften Klammern (mit oder ohne führenden Punkt) nach dem letzten Trennzeichen angegeben werden. Beispiel:

    ~~~~~ruby
    some ruby code
    ~~~~~

Wird wie folgt gerendert:

    <pre><code class="ruby">some ruby code</code></pre>


Oder mit Backticks:

    `````
    some Java code
    `````{.java}

Marked erkennt sowohl Sprachangaben im Format von Markdown Extra/Python Markdown (`{.lang}` nach dem schließenden Trennzeichen) als auch im Discount-Format (`lang` nach dem ersten Trennzeichen). Das folgende Beispiel im Discount-Format erzeugt dasselbe Ergebnis wie das obige Beispiel im Python-Markdown-Format:

    `````java
    some Java code
    `````


Marked verarbeitet auch eingerückte, abgegrenzte Codeblöcke, sodass Sie sie in verschachtelten Listen verwenden können.

Die integrierte Syntaxhervorhebung erkennt **256** Sprachbezeichner (siehe [Unterstützte Sprachen](#supported-languages) unten). Wird keine Sprache angegeben, erkennt Marked sie automatisch; für die Vorschau ist die Angabe daher nicht erforderlich. Der angegebene Sprachbezeichner wird im endgültigen HTML als Klasse des `<code>`-Tags ausgegeben.

Im Abschnitt [Spezielle Syntax in Marked](Special_Syntax.html#includingcode) erfahren Sie, wie Sie externe Codedateien in Ihr Dokument einbinden.

## Syntaxhervorhebung [syntax-highlighting]

![Automatische Syntaxhervorhebung][highlight]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

Die Syntaxhervorhebung kann unter {% prefspane Style %} aktiviert werden. Sie erkennt Codeblöcke und deren Sprache und stellt die Ausgabe in der Vorschau farblich hervorgehoben dar. In den Einstellungen stehen im Einblendmenü unterhalb der Option mehrere Stile zur Auswahl. Der gewählte Stil gilt für alle Dokumente.

Marked verwendet [highlight.js](https://highlightjs.org/), um alle Arten von eingebettetem Code einheitlich farblich hervorzuheben – auch bei Markdown-Syntaxvarianten, die keine Sprachangabe zulassen. Die automatische Erkennung von highlight.js funktioniert zuverlässig. Gegenüber Werkzeugen wie Pygments (GitHub-Stil) gibt es kleinere Unterschiede beim Rendern, die Ausgabe ist jedoch ähnlich. Mit dem Stil `github.css` sieht Ruby-Code beispielsweise fast genauso aus wie auf GitHub.

> *Das GitHub-Stylesheet enthält Ersatzstile für mit Pygments gerenderte Blöcke. Befindet sich das `<pre>`-Tag in einem `div` mit der Klasse „highlight“, wird es im standardmäßigen GitHub-Stil statt im Stil von Marked angezeigt. Sie können den Code extern rendern und HTML einfügen oder ihn mit `pygmentize` in HTML-Dateien rendern und diese über die Syntax [`<<(source.html)`](Special_Syntax.html#includingcode) einbinden.*

Die Option „Nur wenn Sprache angegeben“ rechts neben der Auswahl für den Syntaxstil gilt für abgegrenzte Codeblöcke. Ist sie aktiviert, wird die Syntaxhervorhebung nur auf Codeblöcke angewendet, bei denen nach dem öffnenden Trennzeichen eine Sprache angegeben ist, zum Beispiel:

    ```js
    code
    ```

Die Syntaxhervorhebung erscheint in der Vorschau sowie beim Drucken und im PDF-Export. Ist sie in den Einstellungen aktiviert und wird der Stil beim HTML-Export eingebunden, bettet Marked die verwendete highlight.js-Bibliothek in die HTML-Ausgabe ein. Dadurch sieht das exportierte HTML genauso aus wie in Marked.

### Unterstützte Sprachen [supported-languages]

Marked enthält **highlight.js 11.11.1** mit allen Kernsprachen sowie Grammatiken von Drittanbietern aus der Liste der von [highlight.js unterstützten Sprachen](https://highlightjs.readthedocs.io/en/latest/supported-languages.html). Geben Sie nach dem öffnenden Trennzeichen einen der unten aufgeführten primären Sprachnamen (oder einen dokumentierten Alias wie `js` für JavaScript) an.

Zwei auf der highlight.js-Website aufgeführte Sprachen sind nicht im Paket von Marked enthalten: **Pine Script** (Upstream-Paket nicht verfügbar) und **Supercollider** (nicht mit highlight.js 11 kompatibel).

    1c, 4d, GN, abap, abnf, accesslog, actionscript, ada, alan, angelscript, apache, apex,
    applescript, arcade, arduino, armasm, asciidoc, aspectj, autohotkey, autoit, avrasm, awk,
    axapta, ballerina, bash, basic, bbcode, blade, bnf, bqn, brainfuck, c, c3, cal, capnproto,
    ceylon, chaos, chapel, cisco, clean, clojure, clojure-repl, cmake, cobol, coffeescript,
    coq, cos, cpc, cpp, crmsh, crystal, csharp, cshtml-razor, csp, css, curl, cypher, d, dafny,
    dart, delphi, diff, django, dns, dockerfile, dos, dsconfig, dts, dust, dylan, ebnf, elixir,
    elm, erb, erlang, erlang-repl, excel, extempore, fix, flix, fortran, fsharp, func, gams,
    gauss, gcode, gdscript, gf, gherkin, glimmer, glsl, gml, go, golo, gradle, graphql, groovy,
    gsql, haml, handlebars, haskell, haxe, hlsl, hsp, http, hy, inform7, ini, iptables, irpf90,
    isbl, java, javascript, jboss-cli, jolie, json, julia, julia-repl, kotlin, lang, lasso,
    latex, ldif, leaf, lean, less, lisp, livecodeserver, livescript, llvm, lookml, lsl, lua,
    macaulay2, makefile, markdown, mathematica, matlab, maxima, mel, mercury, mint, mipsasm,
    mirc, mizar, mkb, mlir, mojolicious, monkey, moonscript, motoko, n1ql, nestedtext, never,
    nginx, nim, nix, node-repl, nsis, oak, objectivec, ocaml, ocl, openscad, oxygene, papyrus,
    parser3, perl, pf, pgsql, php, php-template, plaintext, pony, powershell, processing,
    profile, prolog, properties, protobuf, puppet, purebasic, python, python-repl, q, qml,
    qsharp, r, reasonml, rebol, rib, riscript, riscvasm, roboconf, robot, routeros,
    rpm-specfile, rsl, ruby, ruleslanguage, rust, rvt-script, sas, scala, scheme, scilab, scss,
    sfz, shell, shexc, smali, smalltalk, sml, solidity, spl, sqf, sql, stan, stata, step21,
    structured-text, stylus, subunit, svelte, swift, taggerscript, tap, tcl, terraform, thrift,
    toit, tp, tsql, twig, typescript, unicorn-rails-log, vala, vba, vbnet, vbscript,
    vbscript-html, verilog, vhdl, vim, wasm, wren, x86asm, x86asmatt, xl, xml, xquery, xsharp,
    yaml, yul, zenscript, zephir

### Syntaxhervorhebungsthemen [syntax-highlighting-themes]

Unter {% prefspane Style %} stehen **239** Stile für die Syntaxhervorhebung zur Auswahl. Sie werden automatisch aus den mitgelieferten Stylesheets von Marked geladen. Die Namen entsprechen dem CSS-Dateinamen ohne Erweiterung (beispielsweise lädt `github-dark` die Datei `github-dark.css`).

Allgemeine Themen:

    1c-light, a11y-dark, a11y-light, agate, an-old-hope, androidstudio, arduino-light, arta,
    atom-one-dark, atom-one-dark-reasonable, atom-one-light, codepen-embed, color-brewer, dark,
    default, foundation, github, github-dark, github-dark-dimmed, googlecode, grayscale,
    hybrid, idea, intellij-light, ir-black, isbl-editor-dark, isbl-editor-light, kimbie-dark,
    kimbie-light, mono-blue, monokai, monokai-sublime, night-owl, nnfx-dark, nnfx-light, nord,
    obsidian, panda-syntax-dark, panda-syntax-light, paraiso-dark, paraiso-light, pojoaque,
    purebasic, qtcreator-dark, qtcreator-light, rainbow, rose-pine, rose-pine-dawn,
    rose-pine-moon, school-book, shades-of-purple, srcery, stackoverflow-dark,
    stackoverflow-light, sunburst, tokyo-night-dark, tokyo-night-light, tomorrow-night-blue,
    tomorrow-night-bright, vs, vs2015, xcode, xt256

Base16-Themen (176 Varianten, jeweils mit dem Präfix `base16-`):

    base16-3024, base16-apathy, base16-apprentice, base16-ashes, base16-atelier-cave,
    base16-atelier-cave-light, base16-atelier-dune, base16-atelier-dune-light,
    base16-atelier-estuary, base16-atelier-estuary-light, base16-atelier-forest,
    base16-atelier-forest-light, base16-atelier-heath, base16-atelier-heath-light,
    base16-atelier-lakeside, base16-atelier-lakeside-light, base16-atelier-plateau,
    base16-atelier-plateau-light, base16-atelier-savanna, base16-atelier-savanna-light,
    base16-atelier-seaside, base16-atelier-seaside-light, base16-atelier-sulphurpool,
    base16-atelier-sulphurpool-light, base16-atlas, base16-bespin, base16-black-metal,
    base16-black-metal-bathory, base16-black-metal-burzum, base16-black-metal-dark-funeral,
    base16-black-metal-gorgoroth, base16-black-metal-immortal, base16-black-metal-khold,
    base16-black-metal-marduk, base16-black-metal-mayhem, base16-black-metal-nile,
    base16-black-metal-venom, base16-brewer, base16-bright, base16-brogrammer,
    base16-brush-trees, base16-brush-trees-dark, base16-chalk, base16-circus,
    base16-classic-dark, base16-classic-light, base16-codeschool, base16-colors,
    base16-cupcake, base16-cupertino, base16-danqing, base16-darcula, base16-dark-violet,
    base16-darkmoss, base16-darktooth, base16-decaf, base16-default-dark, base16-default-light,
    base16-dirtysea, base16-dracula, base16-edge-dark, base16-edge-light, base16-eighties,
    base16-embers, base16-equilibrium-dark, base16-equilibrium-gray-dark,
    base16-equilibrium-gray-light, base16-equilibrium-light, base16-espresso, base16-eva,
    base16-eva-dim, base16-flat, base16-framer, base16-fruit-soda, base16-gigavolt,
    base16-github, base16-google-dark, base16-google-light, base16-grayscale-dark,
    base16-grayscale-light, base16-green-screen, base16-gruvbox-dark-hard,
    base16-gruvbox-dark-medium, base16-gruvbox-dark-pale, base16-gruvbox-dark-soft,
    base16-gruvbox-light-hard, base16-gruvbox-light-medium, base16-gruvbox-light-soft,
    base16-hardcore, base16-harmonic16-dark, base16-harmonic16-light, base16-heetch-dark,
    base16-heetch-light, base16-helios, base16-hopscotch, base16-horizon-dark,
    base16-horizon-light, base16-humanoid-dark, base16-humanoid-light, base16-ia-dark,
    base16-ia-light, base16-icy-dark, base16-ir-black, base16-isotope, base16-kimber,
    base16-london-tube, base16-macintosh, base16-marrakesh, base16-materia, base16-material,
    base16-material-darker, base16-material-lighter, base16-material-palenight,
    base16-material-vivid, base16-mellow-purple, base16-mexico-light, base16-mocha,
    base16-monokai, base16-nebula, base16-nord, base16-nova, base16-ocean, base16-oceanicnext,
    base16-one-light, base16-onedark, base16-outrun-dark, base16-papercolor-dark,
    base16-papercolor-light, base16-paraiso, base16-pasque, base16-phd, base16-pico,
    base16-pop, base16-porple, base16-qualia, base16-railscasts, base16-rebecca,
    base16-ros-pine, base16-ros-pine-dawn, base16-ros-pine-moon, base16-sagelight,
    base16-sandcastle, base16-seti-ui, base16-shapeshifter, base16-silk-dark,
    base16-silk-light, base16-snazzy, base16-solar-flare, base16-solar-flare-light,
    base16-solarized-dark, base16-solarized-light, base16-spacemacs, base16-summercamp,
    base16-summerfruit-dark, base16-summerfruit-light, base16-synth-midnight-terminal-dark,
    base16-synth-midnight-terminal-light, base16-tango, base16-tender, base16-tomorrow,
    base16-tomorrow-night, base16-twilight, base16-unikitty-dark, base16-unikitty-light,
    base16-vulcan, base16-windows-10, base16-windows-10-light, base16-windows-95,
    base16-windows-95-light, base16-windows-high-contrast, base16-windows-high-contrast-light,
    base16-windows-nt, base16-windows-nt-light, base16-woodland, base16-xcode-dusk,
    base16-zenburn

## GitHub-Zeilenumbrüche [github-line-breaks]

Marked kann Zeilenumbrüche in Absätzen beibehalten. Aktivieren Sie dazu unter {% prefspane Processor %} die entsprechende Option.

## GitHub-Kontrollkästchen [github-checkboxes]

Listenelemente mit folgender Formatierung:

    - [ ] Unfinished task
    - [x] Finished task

werden in der Vorschau als Kontrollkästchen dargestellt. Sie sind nicht interaktiv, geben aber stets den Status im Quelldokument wieder.

## Codeblockumbruch [code-block-wrapping]

Unter {% prefspane Style %} finden Sie im Bereich „Layout und Typografie“ die Option „Stilen erlauben, Text in Codeblöcken umzubrechen“. Wenn Sie sie deaktivieren, lassen sich überbreite Codeblöcke unabhängig vom aktuellen Vorschaustil horizontal scrollen, statt den Text umzubrechen.
