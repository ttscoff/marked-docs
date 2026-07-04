<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Elkerített kódblokkok

A bekerített kódblokkok alapértelmezés szerint engedélyezve vannak mindkét processzorban (MultiMarkdown és Discount). Az elkerített kódblokkokat három vagy több tilde (~) vagy backtick (\`) határolja. Használhat háromnál többet is, de a kezdő és a záró határolónak pontosan ugyanannyi karakterből kell állnia.

    ~~~~
    Néhány kód, amelyet elő/kód blokkként kell megjeleníteni
    ~~~~

A nyelvek megadhatók a nyelv címével (vagy rövid címével) az első sorban lévő határoló után, vagy zárójelben (bevezető ponttal vagy anélkül) az utolsó határolójel után. Például:

    ~~~~~rubin
    valami rubin kód
    ~~~~~

Így jelenik meg:

    <pre><code class="ruby">valami rubinkód</code></pre>


Vagy hátlappal:

    `````
    valami Java kódot
    `````{.java}

A Marked képes felismerni a Markdown Extra/Python Markdown (`{.lang}` lezárás után) és a Discount (`lang` az első kerítés után) nyelvi specifikációkat. A következő (Kedvezmény formátum) ugyanazt az eredményt hozza létre, mint a fenti (Python Markdown formátum):

    `````java
    valami Java kódot
    `````


A Marked kezeli a behúzott elkerített kódblokkokat is, így beágyazott listákon belül is használhatja őket.

A beépített szintaktikai kiemelés felismeri a **256** nyelvi specifikációkat (lásd alább a [Támogatott nyelvek](#supported-languages) részt). Ha nincs megadva nyelv, akkor azt automatikusan észleli, így nem szükséges az előnézethez. A megadott nyelvi karakterlánc a végső html-ben jelenik meg a `<code>` címke osztályaként.

Tekintse meg a [Megjelölt speciális szintaxis](Special_Syntax.html#includingcode) részt, hogy megtudja, hogyan lehet külső kódfájlokat belefoglalni a dokumentumba.

## Szintaxis kiemelés

![Automatikus szintaxis kiemelés][kiemelés]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

A szintaxis kiemelése a {% prefspane Style %}-ben engedélyezhető. Felismeri a kódblokkokat, felismeri a nyelvet, és színkódolt kimenetet jelenít meg az előnézetben. Több téma is elérhető, amelyeket a beállítások alatti legördülő menüből választhat ki. A kiválasztott téma minden dokumentumra vonatkozik.

A Marked a [highlight.js](https://highlightjs.org/) protokollt használja, hogy egységes színkódolást biztosítson minden típusú beágyazott kódhoz, beleértve a szabványos Markdown szintaxisokat is, amelyek nem teszik lehetővé a nyelv megadását. A Highlight.js automatikusan felismeri. Van néhány kisebb renderelési különbség közte és a színezők, például a Pygments (GitHub stílus) között, de a kimenet hasonló. Ha például a github.css témát használjuk a Ruby kódon, akkor szinte pontosan a GitHubon látható kimenetet jelenítjük meg.

> *A GitHub stíluslap biztonsági mentési stílusokat biztosít a Pygments segítségével előállított blokkokhoz. Ha a `<pre>` címke a „highlight” osztályú divben található, akkor a szabványos GitHub stílusban jelenik meg, nem a Marked stílusában. Megjelenítheti a kódot kívülről, és beillesztheti a HTML-t, vagy a `pygmentize` paranccsal előállíthatja html-fájlokká, és belefoglalhatja azokat a [`<<(source.html)` szintaxis](Special_Syntax.html#includingcode)*-ba.

A szintaxisstílus-választótól jobbra található "Csak nyelv megadása esetén" opció az elkerített kódblokkra vonatkozik. Ha engedélyezve van, akkor a szintaktikai kiemelés csak azokra a kódblokkokra vonatkozik, amelyek a nyitókeret után nyelvspecifikációt tartalmaznak, pl.

    ```js
    kódot
    ```

A szintaxis kiemelése megjelenik az előnézetben, valamint a nyomtatásban és a PDF-exportálásban. Ha engedélyezve van a beállításokban, és a téma szerepel a HTML exportálásakor, a Marked által használt highlight.js könyvtár beágyazódik a HTML-kimenetbe, így az exportált HTML ugyanúgy jelenhet meg, mint a Markedben.

### Támogatott nyelvek

A **highlight.js 11.11.1**-el van megjelölve, beleértve az összes alapvető nyelvet, valamint a [highlight.js támogatott nyelvek](https://highlightjs.readthedocs.io/en/latest/supported-languages.html) listán szereplő harmadik felek nyelvtanait. Adjon meg bármely elsődleges nyelvnevet alább (vagy egy dokumentált álnevet, például `js` a JavaScripthez) a nyitó kerítés után.

A highlight.js webhelyen felsorolt ​​két nyelv nem szerepel a Marked csomagjában: a **Pine Script** (az upstream csomag nem érhető el) és a **Supercollider** (nem kompatibilis a highlight.js 11-el).

    1c, 4d, GN, abap, abnf, accesslog, actionscript, ada, alan, angelscript, apache, apex,
    applescript, arcade, arduino, armasm, asciidoc, aspectj, autohotkey, autoit, avrasm, awk,
    axapta, balerina, bash, basic, bbcode, blade, bnf, bqn, brainfuck, c, c3, cal, capnproto,
    ceylon, káosz, kápolna, cisco, tiszta, clojure, clojure-repl, cmake, cobol, coffeescript,
    coq, cos, cpc, cpp, crmsh, crystal, csharp, cshtml-razor, csp, css, curl, cypher, d, dafny,
    dart, delphi, diff, django, dns, dockerfile, dos, dsconfig, dts, por, dylan, ebnf, elixír,
    szil, erb, erlang, erlang-repl, excel, extempore, fix, flix, fortran, fsharp, func, gams,
    gauss, gcode, gdscript, gf, uborka, glimmer, glsl, gml, go, golo, gradle, graphql, groovy,
    gsql, haml, kormány, haskell, haxe, hlsl, hsp, http, hy, inform7, ini, iptables, irpf90,
    isbl, java, javascript, jboss-cli, jolie, json, julia, julia-repl, kotlin, lang, lasso,
    latex, ldif, leaf, lean, less, lisp, livecodeserver, livescript, llvm, lookml, lsl, lua,
    macaulay2, makefile, markdown, mathematica, matlab, maxima, mel, higany, menta, mipsasm,
    mirc, mizar, mkb, mlir, mojolicious, majom, moonscript, motoko, n1ql, beágyazott szöveg, soha,
    nginx, nim, nix, node-repl, nsis, tölgy, objectc, ocaml, ocl, openscad, oxigén, papirusz,
    parser3, perl, pf, pgsql, php, php-sablon, egyszerű szöveg, pony, powershell, feldolgozás,
    profil, prolog, tulajdonságok, protobuf, puppet, purebasic, python, python-repl, q, qml,
    qsharp, r, reasonml, rebol, rib, riscript, riscvasm, roboconf, robot, routeros,
    rpm-specfile, rsl, ruby, rulelanguage, rust, rvt-script, sas, scala, séma, scilab, scss,
    sfz, shell, shexc, smali, smalltalk, sml, solidity, spl, sqf, sql, stan, stata, step21,
    strukturált szöveg, stylus, subunit, svelte, swift, taggerscript, tap, tcl, terraform, takarékosság,
    toit, tp, tsql, gally, gépirat, unicorn-rails-log, vala, vba, vbnet, vbscript,
    vbscript-html, verilog, vhdl, vim, wasm, wren, x86asm, x86asmatt, xl, xml, xquery, xsharp,
    yaml, yul, zenscript, zephir

### Szintaxis kiemelő témák

A **239** szintaxiskiemelő témák az {% prefspane Style %} legördülő menüben érhetők el. A témák automatikusan betöltődnek a Marked kötegelt stíluslapjaiból; a nevek egyeznek a CSS-fájlnévvel, kiterjesztés nélkül (például `github-dark` betölti `github-dark.css`).

Általános témák:

1c-light, a11y-dark, a11y-light, achát, an-old-hope, androidstudio, arduino-light, arta,
    atom-one-dark, atom-one-dark-reasonable, atom-one-light, codepen-embed, color-söröző, sötét,
    alapértelmezett, alapozó, github, github-dark, github-dark-dimmer, googlecode, szürkeárnyalatos,
    hibrid, ötlet, intellij-light, ir-black, isbl-editor-dark, isbl-editor-light, kimbie-dark,
    kimbie-light, mono-kék, monokai, monokai-sublime, éjszakai bagoly, nnfx-dark, nnfx-light, nord,
    obszidián, panda-szintaxis-sötét, panda-szintaxis-világos, Paraiso-sötét, Paraiso-light, Pojoaque,
    purebasic, qtcreator-dark, qtcreator-light, szivárvány, rose-pine, rose-pine-dawn,
    rózsa-fenyő-hold, iskolai könyv, lila árnyalatai, srcery, stackoverflow-dark,
    stackoverflow-light, sunburst, tokyo-night-dark, tokyo-night-light, holnap-night-blue,
    holnap-éj-világos, vs, vs2015, xcode, xt256

Base16 téma (176 változat, mindegyik `base16-` előtaggal):

base16-3024, base16-apátia, base16-tanonc, base16-hamu, base16-atelier-cave,
    base16-atelier-cave-light, base16-atelier-dine, base16-atelier-dane-light,
    base16-atelier-torkolat, base16-atelier-estuary-light, base16-atelier-forest,
    base16-atelier-forest-light, base16-atelier-heath, base16-atelier-heath-light,
    base16-atelier-tóparti, base16-atelier-lakeside-light, base16-atelier-plateau,
    base16-atelier-plateau-light, base16-atelier-savanna, base16-atelier-savanna-light,
    base16-atelier-seaside, base16-atelier-seaside-light, base16-atelier-sulphurpool,
    base16-atelier-sulphurpool-light, base16-atlas, base16-bespin, base16-black-metal,
    base16-black-metal-bathory, base16-black-metal-burzum, base16-black-metal-sötét-temetés,
    base16-black-metal-gorgoroth, base16-black-metal-immortal, base16-black-metal-khold,
    base16-black-metal-marduk, base16-black-metal-mayhem, base16-black-metal-nile,
    base16-black-metal-venom, base16-brewer, base16-bright, base16-brogrammer,
    16-os bozótfák, 16-os bozótfák sötét alapjai, 16-os kréta alapjai, 16-os cirkuszai,
    base16-classic-dark, base16-classic-light, base16-codeschool, base16-colors,
    16-os cupcake, base16-cupertino, base16-danqing, base16-darcula, base16-sötétlila,
    base16-darkmoha, base16-darktooth, base16-decaf, base16-alapértelmezett-sötét, base16-default-light,
    alap16-dirttysea, alap16-drakula, alap16-él-sötét, alap16-él-világos, alap16-80-as évek,
    16-os parázs alap, 16. bázis egyensúlyi sötét, 16. bázis egyensúlyi szürke-sötét,
    base16-equilibrium-gray-light, base16-equilibrium-light, base16-espresso, base16-eva,
    base16-eva-dim, base16-flat, base16-framer, base16-gyümölcs-szóda, base16-gigavolt,
    base16-github, base16-google-dark, base16-google-light, base16-grayscale-dark,
    base16-grayscale-light, base16-green-screen, base16-gruvbox-dark-hard,
    base16-gruvbox-dark-medium, base16-gruvbox-dark-pale, base16-gruvbox-dark-soft,
    base16-gruvbox-light-hard, base16-gruvbox-light-medium, base16-gruvbox-light-soft,
    base16-hardcore, base16-harmonikus16-sötét, alap16-harmonikus16 világos, base16-heetch-sötét,
    base16-heetch-light, base16-helios, base16-hopscotch, base16-horizon-dark,
    alap16-horizont-light, base16-humanoid-sötét, base16-humanoid-light, base16-ia-dark,
    base16-ia-light, base16-jeges-sötét, base16-ir-black, base16-izotóp, base16-kimber,
    base16-london-tube, base16-macintosh, base16-marrakesh, base16-materia, base16-anyag,
    alap16-anyag-sötétebb, alap16-anyag-világosabb, alap16-anyag-halvány éjszaka,
    alap16-anyag-élénk, base16-mellow-lila, base16-mexico-light, base16-mokka,
    alap16-monokai, alap16-köd, 16-os északi bázis, 16-os alap-nóva, 16-os óceán, 16-os óceáni bázis, következő,
    base16-one-light, base16-onedark, base16-outrun-dark, base16-papercolor-sötét,
    base16-papercolor-light, base16-paraiso, base16-pasque, base16-phd, base16-pico,
    base16-pop, base16-porple, base16-qualia, base16-railscasts, base16-rebecca,
    base16-ros-pine, base16-ros-pine-dawn, base16-ros-pine-moon, base16-sagelight,
    base16-homokvár, base16-seti-ui, base16-shapeshifter, base16-selyem-sötét,
    base16-selyemfény, base16-snazzy, base16-solar-flare, base16-solar-flare-light,
    base16-solarized-dark, base16-solarized-light, base16-spacemacs, base16-summercam,
    base16-summerfruit-dark, base16-summerfruit-light, base16-synth-midnight-terminal-dark,
    base16-synth-midnight-terminal-light, base16-tango, base16-tender, base16-holnap,
    base16-holnap éjszaka, base16-szürkület, base16-unikitty-sötét, base16-unikitty-light,
    base16-vulcan, base16-windows-10, base16-windows-10-light, base16-windows-95,
    base16-windows-95-light, base16-windows-high-contrast, base16-windows-high-contrast-light,
    base16-windows-nt, base16-windows-nt-light, base16-woodland, base16-xcode-dusk,
    alap16-zenburn

## GitHub vonalszakadások

A Megjelölve megőrizheti a sortöréseket a bekezdésekben. Csak válassza ki a {% prefspane Processor %}-t, és jelölje be a jelölőnégyzetet a sortörések megőrzéséhez a bekezdésekben.

## GitHub jelölőnégyzetek

Listaelemek a következő formátumban:

    - [ ] Befejezetlen feladat
    - [x] Befejezett feladat

jelennek meg az előnézetben renderelt jelölőnégyzet elemként. Nem lehet velük kommunikálni, de állapotuk tükrözni fogja a forrásdokumentum változásait.

## Kódblokk burkolása

A {% prefspane Style %} részben az Elrendezés és tipográfia alatt talál egy lehetőséget: "Engedélyezi, hogy a témák kódblokkokba tördeljenek szöveget." Ennek letiltása az aktuális előnézeti stílustól függetlenül az összes kódblokkot vízszintes túlcsordulásra kényszeríti, ahelyett, hogy becsomagolná.