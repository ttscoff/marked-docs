# <%= @title %>

## Blocs de code clôturés [fenced-code-blocks]

Les blocs de code clôturés sont activés par défaut dans les deux processeurs inclus (MultiMarkdown et Discount). Les blocs de code clôturés sont délimités par au moins trois tildes (~) ou backticks (\`). Vous pouvez en utiliser plus de trois, mais les délimiteurs de début et de fin doivent avoir exactement le même nombre de caractères.

    ~~~~
    Du code à rendre sous forme de bloc pré/code
    ~~~~

Les langues peuvent être spécifiées en utilisant le titre de la langue (ou le titre abrégé) après le délimiteur de la première ligne, ou entre accolades (avec ou sans point) après le dernier délimiteur. Par exemple :

    ~~~~~ruby
    du code Ruby
    ~~~~~

Rendu comme suit :

    <pre><code class="ruby">du code Ruby</code></pre>


Ou avec des backticks :

    `````
    du code Java
    `````{.java}

Marked peut détecter à la fois les spécifications linguistiques Markdown Extra/Python Markdown (`{.lang}` après la clôture) et Discount (`lang` après la première clôture). Ce qui suit (format Discount) créerait le même résultat que ci-dessus (format Python Markdown) :

    `````java
    du code Java
    `````


Marked gère également les blocs de code clôturés en retrait afin que vous puissiez les utiliser dans des listes imbriquées.

La coloration syntaxique intégrée reconnaîtra **256** spécificateurs de langue (voir [Langues prises en charge](#supported-linguals) ci-dessous). Si aucune langue n'est spécifiée, il la détectera automatiquement, elle n'est donc pas requise pour l'aperçu. La chaîne de langue donnée sera affichée dans le code HTML final en tant que classe sur la balise `<code>`.

Consultez la section sur [Syntaxe spéciale de Marked](Special_Syntax.html#includingcode) pour savoir comment inclure des fichiers de code externes dans votre document.

## Mise en évidence de la syntaxe [syntax-highlighting]

![Surlignage automatique de la syntaxe][highlight]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

La mise en évidence de la syntaxe peut être activée dans le {% prefspane Style %}. Il reconnaîtra les blocs de code, détectera la langue et affichera une sortie codée par couleur dans l'aperçu. Plusieurs thèmes sont disponibles, sélectionnés dans la liste déroulante située sous l'option dans les paramètres. Le thème sélectionné s'appliquera à tous les documents.

Marked utilise [highlight.js](https://highlightjs.org/) pour fournir un codage couleur cohérent pour tous les types de code intégré, y compris les syntaxes Markdown standard qui ne permettent pas de spécifier la langue. Highlight.js se détecte bien automatiquement. Il existe quelques différences de rendu mineures entre celui-ci et les coloriseurs tels que Pygments (style GitHub), mais le résultat est similaire. L'utilisation du thème github.css sur le code Ruby, par exemple, donne presque exactement le résultat que vous verriez sur GitHub.

> *La feuille de style GitHub fournit des styles de sauvegarde pour les blocs rendus avec Pygments. Si la balise `<pre>` se trouve à l'intérieur d'un div avec la classe "highlight", elle s'affichera en utilisant le style standard de GitHub, et non celui de Marked. Vous pouvez restituer le code en externe et coller du HTML, ou utiliser `pygmentize` pour le restituer dans des fichiers HTML et les inclure avec la [syntaxe `<<(source.html)`](Special_Syntax.html#includingcode)*.

L'option « Uniquement si la langue est spécifiée » à droite du sélecteur de style de syntaxe s'applique aux blocs de code isolés. Si elle est activée, la coloration syntaxique ne sera appliquée qu'aux blocs de code avec un spécificateur de langage après la clôture d'ouverture, par ex.

    ```js
    coder
    ```

La mise en évidence de la syntaxe apparaîtra dans l'aperçu et lors de l'impression et de l'exportation PDF. Si elle est activée dans les paramètres et que le thème est inclus lors de l'exportation HTML, la bibliothèque highlight.js utilisée par Marked sera intégrée dans la sortie HTML, permettant à votre HTML exporté d'apparaître comme il le fait dans Marked.

### Langues prises en charge [supported-languages]

Marked est livré avec **highlight.js 11.11.1**, y compris toutes les langues principales ainsi que les grammaires tierces de la liste [langues prises en charge par highlight.js](https://highlightjs.readthedocs.io/en/latest/supported-languages.html). Spécifiez n'importe quel nom de langue principale ci-dessous (ou un alias documenté tel que `js` pour JavaScript) après la clôture d'ouverture.

Deux langages répertoriés sur le site highlight.js ne sont pas inclus dans le bundle de Marked : **Pine Script** (package en amont indisponible) et **Supercollider** (incompatible avec highlight.js 11).

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

### Thèmes de mise en évidence de la syntaxe [syntax-highlighting-themes]

**239** thèmes de coloration syntaxique sont disponibles dans la liste déroulante {% prefspane Style %}. Les thèmes sont chargés automatiquement à partir des feuilles de style fournies par Marked ; les noms correspondent au nom du fichier CSS sans l'extension (par exemple, `github-dark` charge `github-dark.css`).

Thèmes généraux :

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

Thèmes Base16 (176 variantes, chacune préfixée par `base16-`) :

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

## Sauts de ligne GitHub [github-line-breaks]

Marked peut conserver les sauts de ligne dans vos paragraphes. Sélectionnez simplement le {% prefspane Processor %} et cochez la case pour conserver les sauts de ligne dans les paragraphes.

## Cases à cocher GitHub [github-checkboxes]

Répertoriez les éléments au format :

    - [ ] Tâche inachevée
    - [x] Tâche terminée

apparaîtra dans l'aperçu sous forme d'éléments de case à cocher rendus. Il n'est pas possible d'interagir avec eux, mais leur état reflétera toute modification apportée au document source.

## Emballage du bloc de code [code-block-wrapping]

Dans le {% prefspane Style %}, vous trouverez une option sous Mise en page et typographie : « Autoriser les thèmes à envelopper le texte dans des blocs de code. » La désactivation de cette option forcera tous les blocs de code à faire défiler le débordement horizontal plutôt que de l'envelopper, quel que soit le style d'aperçu actuel.
