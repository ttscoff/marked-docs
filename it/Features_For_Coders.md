<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

## Blocchi di codice recintati

I blocchi di codice recintati sono abilitati in entrambi i processori inclusi per impostazione predefinita (MultiMarkdown e Discount). I blocchi di codice recintati sono delimitati da tre o più tilde (~) o apici inversi (\`). Puoi usarne più di tre, ma i delimitatori iniziale e finale devono avere esattamente lo stesso numero di caratteri.

    ~~~~
    Parte del codice deve essere renderizzata come blocco pre/codice
    ~~~~

Le lingue possono essere specificate utilizzando il titolo della lingua (o un titolo breve) dopo il delimitatore nella prima riga o tra parentesi graffe (con o senza punto iniziale) dopo l'ultimo delimitatore. Ad esempio:

    ~~~~~rubino
    qualche codice Ruby
    ~~~~~

Verrà visualizzato come:

    <pre><code class="ruby">un po' di codice Ruby</code></pre>


Oppure con gli apici inversi:

    `````
    del codice Java
    `````{.java}

Marked è in grado di rilevare sia le specifiche linguistiche di Markdown Extra/Python Markdown (`{.lang}` dopo la chiusura del recinto) che di Sconto (`lang` dopo il primo recinto). Il seguente (formato Sconto) creerebbe lo stesso risultato di quanto sopra (formato Python Markdown):

    `````java
    del codice Java
    `````


Marked gestisce anche blocchi di codice recintati rientrati in modo da poterli utilizzare all'interno di elenchi nidificati.

L'evidenziazione della sintassi incorporata riconoscerà **256** specificatori di lingua (vedi [Lingue supportate](#supported-linguals) di seguito). Se non è specificata alcuna lingua, la rileverà automaticamente, quindi non è necessaria per l'anteprima. La stringa della lingua fornita verrà generata nell'HTML finale come classe nel tag `<code>`.

Consulta la sezione su [Sintassi speciale contrassegnata](Special_Syntax.html#includingcode) per sapere come includere file di codice esterni nel tuo documento.

## Evidenziazione della sintassi

![Evidenziazione automatica della sintassi][evidenzia]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

L'evidenziazione della sintassi può essere abilitata in {% prefspane Style %}. Riconoscerà i blocchi di codice, rileverà la lingua e renderà l'output con codice colore nell'anteprima. Sono disponibili più temi, selezionati dal menu a discesa sotto l'opzione nelle impostazioni. Il tema selezionato verrà applicato a tutti i documenti.

Marked utilizza [highlight.js](https://highlightjs.org/) per fornire una codifica a colori coerente per tutti i tipi di codice incorporato, incluse le sintassi Markdown standard che non consentono la specifica della lingua. Highlight.js si rileva automaticamente bene. Ci sono alcune piccole differenze di rendering tra questo e i colorizzatori come Pygments (stile GitHub), ma l'output è simile. Utilizzando il tema github.css sul codice Ruby, ad esempio, viene visualizzato quasi l'output esatto che vedresti su GitHub.

> *Il foglio di stile GitHub fornisce stili di backup per i blocchi renderizzati con Pygments. Se il tag `<pre>` si trova all'interno di un div con la classe "evidenzia", ​​verrà visualizzato utilizzando lo stile GitHub standard, non quello di Marked. Puoi eseguire il rendering del codice esternamente e incollare HTML oppure utilizzare `pygmentize` per eseguirne il rendering in file html e includerli con la [sintassi `<<(source.html)`](Special_Syntax.html#includingcode)*.

L'opzione "Solo se è specificata la lingua" a destra del selettore dello stile di sintassi si applica ai blocchi di codice protetti. Se abilitata, l'evidenziazione della sintassi verrà applicata solo ai blocchi di codice con uno specificatore di lingua dopo il recinto di apertura, ad es.

    ```js
    codice
    ```

L'evidenziazione della sintassi verrà visualizzata nell'anteprima, nella stampa e nell'esportazione in PDF. Se abilitato nelle impostazioni e il tema è incluso durante l'esportazione dell'HTML, la libreria highlight.js utilizzata da Marked verrà incorporata nell'output HTML, consentendo all'HTML esportato di apparire come in Marked.

### Lingue supportate

Marked viene fornito con **highlight.js 11.11.1**, incluse tutte le lingue principali più grammatiche di terze parti dall'elenco [lingue supportate da highlight.js](https://highlightjs.readthedocs.io/en/latest/supported-languages.html). Specificare il nome della lingua principale di seguito (o un alias documentato come `js` per JavaScript) dopo il recinto di apertura.

Due lingue elencate sul sito highlight.js non sono incluse nel pacchetto Marked: **Pine Script** (pacchetto upstream non disponibile) e **Supercollider** (incompatibile con highlight.js 11).

    1c, 4d, GN, abap, abnf, accesslog, actionscript, ada, alan, angelscript, apache, apex,
    applescript, arcade, arduino, armasm, asciidoc, aspettij, autohotkey, autoit, avrasm, awk,
    axapta, ballerina, bash, bbcode, lama, bnf, bqn, brainfuck, c, c3, cal, capnproto,
    ceylon, caos, cappella, cisco, pulito, clojure, clojure-repl, cmake, cobol, coffeescript,
    coq, cos, cpc, cpp, crmsh, crystal, csharp, cshtml-razor, csp, css, curl, cypher, d, dafny,
    dart, delphi, diff, django, dns, dockerfile, dos, dsconfig, dts, polvere, dylan, ebnf, elixir,
    elm, erb, erlang, erlang-repl, excel, extempore, fix, flix, fortran, fsharp, func, gams,
    gauss, gcode, gdscript, gf, gherkin, glimmer, glsl, gml, go, golo, gradle, graphql, groovy,
    gsql, haml, manubri, haskell, haxe, hlsl, hsp, http, hy, inform7, ini, iptables, irpf90,
    isbl, java, javascript, jboss-cli, jolie, json, julia, julia-repl, kotlin, lang, lazo,
    latex, ldif, leaf, lean, less, lisp, livecodeserver, livescript, llvm, lookml, lsl, lua,
    macaulay2, makefile, markdown, matematica, matlab, maxima, mel, mercurio, menta, mipsasm,
    mirc, mizar, mkb, mlir, mojolicious, scimmia, moonscript, motoko, n1ql, nestedtext, mai,
    nginx, nim, nix, node-repl, nsis, quercia, objectc, ocaml, ocl, openscad, ossigeno, papiro,
    parser3, perl, pf, pgsql, php, modello php, testo in chiaro, pony, powershell, elaborazione,
    profilo, prolog, proprietà, protobuf, pupazzo, purebasic, python, python-repl, q, qml,
    qsharp, r, Reasonml, rebol, rib, riscript, riscvasm, roboconf, robot, routeros,
    rpm-specfile, rsl, ruby, regolelinguaggio, ruggine, rvt-script, sas, scala, schema, scilab, scss,
    sfz, conchiglia, shexc, smali, chiacchiere, sml, solidità, spl, sqf, sql, stan, stata, step21,
    testo strutturato, stilo, subunità, svelte, swift, taggerscript, tap, tcl, terraform, parsimonia,
    toit, tp, tsql, ramoscello, dattiloscritto, unicorn-rails-log, vala, vba, vbnet, vbscript,
    vbscript-html, verilog, vhdl, vim, wasm, scricciolo, x86asm, x86asmatt, xl, xml, xquery, xsharp,
    yaml, yul, zenscript, zephir

### Temi di evidenziazione della sintassi

**239** temi di evidenziazione della sintassi sono disponibili nel menu a discesa {% prefspane Style %}. I temi vengono caricati automaticamente dai fogli di stile in bundle di Marked; i nomi corrispondono al nome file CSS senza l'estensione (ad esempio, `github-dark` carica `github-dark.css`).

Temi generali:

1c-light, a11y-dark, a11y-light, agata, androidstudio, arduino-light, arta,
    atom-one-dark, atom-one-dark-ragionevole, atomo-one-luce, codepen-incorporato, color-brewer, buio,
    predefinito, fondazione, github, github-dark, github-dark-dimmed, googlecode, scala di grigi,
    ibrido, idea, intellij-light, ir-black, isbl-editor-dark, isbl-editor-light, kimbie-dark,
    kimbie-chiaro, mono-blu, monokai, monokai-sublime, nottambulo, nnfx-scuro, nnfx-chiaro, nord,
    ossidiana, panda-sintassi-scuro, panda-sintassi-luce, paraiso-scuro, paraiso-luce, pojoaque,
    purebasic, qtcreator-dark, qtcreator-light, arcobaleno, rose-pine, rose-pine-dawn,
    rosa-pino-luna, libro scolastico, sfumature di viola, srcery, stackoverflow-scuro,
    stackoverflow-luce, sunburst, tokyo-notte-buio, tokyo-notte-luce, domani-notte-blu,
    domani-notte-luminoso, vs, vs2015, xcode, xt256

Temi Base16 (176 varianti, ciascuna con prefisso `base16-`):

base16-3024, base16-apatia, base16-apprendista, base16-ceneri, base16-atelier-caverna,
    base16-atelier-cave-light, base16-atelier-dune, base16-atelier-dune-light,
    base16-atelier-estuario, base16-atelier-estuario-luce, base16-atelier-foresta,
    base16-atelier-forest-light, base16-atelier-heath, base16-atelier-heath-light,
    base16-atelier-lakeside, base16-atelier-lakeside-light, base16-atelier-altopiano,
    base16-atelier-plateau-light, base16-atelier-savanna, base16-atelier-savanna-light,
    base16-atelier-seaside, base16-atelier-seaside-light, base16-atelier-sulphurpool,
    base16-atelier-sulphurpool-light, base16-atlas, base16-bespin, base16-black-metal,
    base16-black-metal-bathory, base16-black-metal-burzum, base16-black-metal-dark-funeral,
    base16-black-metal-gorgoroth, base16-black-metal-immortale, base16-black-metal-khold,
    base16-black-metal-marduk, base16-black-metal-mayhem, base16-black-metal-nile,
    base16-black-metal-venom, base16-brewer, base16-bright, base16-brogrammer,
    base16-brush-trees, base16-brush-trees-dark, base16-chalk, base16-circus,
    base16-classic-dark, base16-classic-light, base16-codeschool, base16-colori,
    base16-cupcake, base16-cupertino, base16-danqing, base16-darcula, base16-viola scuro,
    base16-darkmoss, base16-darktooth, base16-decaf, base16-default-dark, base16-default-light,
    base16-dirtysea, base16-dracula, base16-edge-dark, base16-edge-light, base16-eighties,
    base16-braci, base16-equilibrio-scuro, base16-equilibrio-grigio-scuro,
    base16-equilibrium-grey-light, base16-equilibrium-light, base16-espresso, base16-eva,
    base16-eva-dim, base16-flat, base16-framer, base16-fruit-soda, base16-gigavolt,
    base16-github, base16-google-dark, base16-google-light, base16-grayscale-dark,
    base16-grayscale-light, base16-green-screen, base16-gruvbox-dark-hard,
    base16-gruvbox-dark-medium, base16-gruvbox-dark-pale, base16-gruvbox-dark-soft,
    base16-gruvbox-light-hard, base16-gruvbox-light-medium, base16-gruvbox-light-soft,
    base16-hardcore, base16-harmonic16-dark, base16-harmonic16-light, base16-heetch-dark,
    base16-heetch-light, base16-helios, base16-hopscotch, base16-horizon-dark,
    base16-horizon-light, base16-humanoid-dark, base16-humanoid-light, base16-ia-dark,
    base16-ia-light, base16-icy-dark, base16-ir-black, base16-isotopo, base16-kimber,
    base16-london-tube, base16-macintosh, base16-marrakesh, base16-materia, base16-material,
    base16-material-darker, base16-material-lighter, base16-material-palenight,
    base16-material-vivid, base16-mellow-viola, base16-mexico-light, base16-mocha,
    base16-monokai, base16-nebula, base16-nord, base16-nova, base16-ocean, base16-oceanicnext,
    base16-one-light, base16-onedark, base16-outrun-dark, base16-papercolor-dark,
    base16-papercolor-light, base16-paraiso, base16-pasque, base16-phd, base16-pico,
    base16-pop, base16-porple, base16-qualia, base16-railscasts, base16-rebecca,
    base16-ros-pine, base16-ros-pine-dawn, base16-ros-pine-moon, base16-sagelight,
    base16-castello di sabbia, base16-seti-ui, base16-mutaforma, base16-seta-scuro,
    base16-silk-light, base16-snazzy, base16-solar-flare, base16-solar-flare-light,
    base16-solarized-dark, base16-solarized-light, base16-spacemacs, base16-summercamp,
    base16-summerfruit-dark, base16-summerfruit-light, base16-synth-midnight-terminal-dark,
    base16-synth-midnight-terminal-light, base16-tango, base16-tender, base16-tomorrow,
    base16-domani-notte, base16-crepuscolo, base16-unikitty-buio, base16-unikitty-luce,
    base16-vulcan, base16-windows-10, base16-windows-10-light, base16-windows-95,
    base16-windows-95-luce, base16-windows-alto contrasto, base16-windows-alto contrasto-luce,
    base16-windows-nt, base16-windows-nt-light, base16-woodland, base16-xcode-dusk,
    base16-zenburn

## Interruzioni di riga su GitHub

Contrassegnato può preservare le interruzioni di riga nei paragrafi. Basta selezionare {% prefspane Processor %} e selezionare la casella per mantenere le interruzioni di riga nei paragrafi.

## Caselle di controllo GitHub

Elenca gli elementi formattati come:

    - [ ] Compito non completato
    - [x] Compito finito

appariranno nell'anteprima come elementi della casella di controllo renderizzata. Non è possibile interagire con essi, ma il loro stato rifletterà eventuali modifiche nel documento di origine.

## Avvolgimento del blocco di codice

Nella {% prefspane Style %} troverai un'opzione sotto Layout e tipografia: "Consenti ai temi di racchiudere il testo all'interno dei blocchi di codice". Disabilitare questa opzione costringerà tutti i blocchi di codice a scorrere l'overflow orizzontale anziché a capo, indipendentemente dallo stile di anteprima corrente.