# <%= @title %>

## Fenced Code Blocks [fenced-code-blocks]

Fenced code blocks are enabled in both included processors by default (MultiMarkdown and Discount). Fenced code blocks are delimited by three or more tildes (~) or backticks (\`). You can use more than three, but the beginning and ending delimiters must have exactly the same number of characters.

    ~~~~
    Some code to be rendered as a pre/code block
    ~~~~

Languages may be specified using the language title (or short title) after the delimiter in the first line, or in curly brackets (with or without a leading period) after the last delimiter. For example:

    ~~~~~ruby
    some ruby code
    ~~~~~

Will render as:

    <pre><code class="ruby">some ruby code</code></pre>


Or with backticks:

    `````
    some Java code
    `````{.java}

Marked can detect both Markdown Extra/Python Markdown (`{.lang}` after closing fence) and Discount (`lang` after first fence) language specifications. The following (Discount format) would create the same result as the above (Python Markdown format):

    `````java
    some Java code
    `````


Marked also handles indented fenced code blocks so you can use them within nested lists.

The built in syntax highlighting will recognize **256** language specifiers (see [Supported languages](#supported-languages) below). If there is no language specified, it will detect it automatically, so it's not required for the preview. The language string given will be output in the final html as a class on the `<code>` tag.

See the section on [Marked Special Syntax](Special_Syntax.html#includingcode) to learn how to include external code files in your document.

## Syntax Highlighting [syntax-highlighting]

![Automatic Syntax Highlighting][highlight]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

Syntax highlighting can be enabled in the {% prefspane Style %}. It will recognize code blocks, detect the language and render color-coded output in the preview. There are multiple themes available, selected by the dropdown below the option in settings. The selected theme will apply to all documents.

Marked uses [highlight.js](https://highlightjs.org/) to provide consistent color coding for all types of embedded code, including standard Markdown syntaxes that don't allow language to be specified. Highlight.js autodetects well. There are some minor rendering differences between it and colorizers such as Pygments (GitHub style), but the output is similar. Using the github.css theme on Ruby code, for example, renders almost the exact output you'd see on GitHub.

> *The GitHub stylesheet provides backup styles for blocks rendered with Pygments. If the `<pre>` tag is inside a div with the class "highlight", it will display using the standard GitHub styling, not Marked's. You can render the code externally and paste HTML, or use `pygmentize` to render it to html files and include them with the [`<<(source.html)` syntax](Special_Syntax.html#includingcode)*.

The "Only if language specified" option to the right of the syntax style selector applies to fenced code blocks. If enabled, syntax highlighting will only be applied to code blocks with a language specifier after the opening fence, e.g.

    ```js
    code
    ```

Syntax highlighting will show up in the preview and in print and PDF export. If enabled in settings and the theme is included when exporting HTML, the highlight.js library used by Marked will be embedded in the HTML output, allowing your exported HTML to appear as it does in Marked.

### Supported languages [supported-languages]

Marked ships with **highlight.js 11.11.1**, including all core languages plus third-party grammars from the [highlight.js supported languages](https://highlightjs.readthedocs.io/en/latest/supported-languages.html) list. Specify any primary language name below (or a documented alias such as `js` for JavaScript) after the opening fence.

Two languages listed on the highlight.js site are not included in Marked's bundle: **Pine Script** (upstream package unavailable) and **Supercollider** (incompatible with highlight.js 11).

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

### Syntax highlighting themes [syntax-highlighting-themes]

**239** syntax highlighting themes are available in the {% prefspane Style %} dropdown. Themes are loaded automatically from Marked's bundled stylesheets; names match the CSS filename without the extension (for example, `github-dark` loads `github-dark.css`).

General themes:

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

Base16 themes (176 variants, each prefixed with `base16-`):

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

## GitHub Line Breaks [github-line-breaks]

Marked can preserve line breaks in your paragraphs. Just select the {% prefspane Processor %} and check the box to retain line breaks in paragraphs.

## GitHub Checkboxes [github-checkboxes]

List items formatted as:

    - [ ] Unfinished task
    - [x] Finished task

will appear in the preview as rendered checkbox items. They cannot be interacted with, but their state will reflect any changes in the source document.

## Code block wrapping [code-block-wrapping]

In the {% prefspane Style %} you'll find an option under Layout and Typography: "Allow themes to wrap text inside code blocks." Disabling this will force all code blocks to scroll horizontal overflow rather than wrapping it, regardless of the current preview style.
