<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Bloques de código vallados [fenced-code-blocks]

Los bloques de código delimitados están habilitados en ambos procesadores incluidos de forma predeterminada (MultiMarkdown y Discount). Los bloques de código delimitados están delimitados por tres o más tildes (~) o comillas invertidas (\`). Puede utilizar más de tres, pero los delimitadores de inicio y fin deben tener exactamente la misma cantidad de caracteres.

    ~~~~
    Parte del código se representará como un bloque de código/previo
    ~~~~

Los idiomas se pueden especificar usando el título del idioma (o título corto) después del delimitador en la primera línea, o entre llaves (con o sin punto inicial) después del último delimitador. Por ejemplo:

    ~~~~~rubí
    algún código rubí
    ~~~~~

Se representará como:

    <pre><code class="ruby">algo de código ruby</code></pre>


O con comillas invertidas:

    `````
    algo de código java
    `````{.java}

Marked puede detectar especificaciones de lenguaje Markdown Extra/Python Markdown (`{.lang}` después de cerrar la valla) y Discount (`lang` después de la primera valla). Lo siguiente (formato de descuento) crearía el mismo resultado que el anterior (formato Python Markdown):

    `````java
    algo de código java
    `````


Marked también maneja bloques de código delimitados con sangría para que puedas usarlos dentro de listas anidadas.

El resaltado de sintaxis integrado reconocerá **256** especificadores de idioma (consulte [Idiomas admitidos](#idiomas admitidos) a continuación). Si no se especifica ningún idioma, lo detectará automáticamente, por lo que no es necesario para la vista previa. La cadena de idioma proporcionada se generará en el html final como una clase en la etiqueta `<code>`.

Consulte la sección sobre [Sintaxis especial marcada](Special_Syntax.html#includingcode) para aprender cómo incluir archivos de código externo en su documento.

## Resaltado de sintaxis [syntax-highlighting]

![Resaltado automático de sintaxis][resaltado]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

El resaltado de sintaxis se puede habilitar en {% prefspane Style %}. Reconocerá bloques de código, detectará el idioma y generará resultados codificados por colores en la vista previa. Hay varios temas disponibles, seleccionados en el menú desplegable debajo de la opción en la configuración. El tema seleccionado se aplicará a todos los documentos.

Marked utiliza [highlight.js](https://highlightjs.org/) para proporcionar codificación de colores consistente para todo tipo de código incrustado, incluidas las sintaxis estándar de Markdown que no permiten especificar el idioma. Highlight.js se autodetecta bien. Existen algunas diferencias menores de representación entre este y los colorizadores como Pygments (estilo GitHub), pero el resultado es similar. Usar el tema github.css en código Ruby, por ejemplo, genera casi el mismo resultado que verías en GitHub.

> *La hoja de estilo de GitHub proporciona estilos de respaldo para bloques renderizados con Pygments. Si la etiqueta `<pre>` está dentro de un div con la clase "resaltado", se mostrará usando el estilo estándar de GitHub, no el de Marked. Puede renderizar el código externamente y pegar HTML, o usar `pygmentize` para renderizarlo en archivos html e incluirlos con la [`<<(source.html)` sintaxis](Special_Syntax.html#includingcode)*.

La opción "Solo si se especifica el idioma" a la derecha del selector de estilo de sintaxis se aplica a bloques de código delimitados. Si está habilitado, el resaltado de sintaxis solo se aplicará a los bloques de código con un especificador de idioma después de la valla de apertura, p.

    ```js
    código
    ```

El resaltado de sintaxis aparecerá en la vista previa y en la impresión y exportación de PDF. Si está habilitado en la configuración y el tema se incluye al exportar HTML, la biblioteca resaltada.js utilizada por Marked se incrustará en la salida HTML, lo que permitirá que el HTML exportado aparezca como aparece en Marked.

### Idiomas admitidos [supported-languages]

Marked se envía con **highlight.js 11.11.1**, incluidos todos los idiomas principales más gramáticas de terceros de la lista [idiomas compatibles con Highlight.js](https://highlightjs.readthedocs.io/en/latest/supported-languages.html). Especifique cualquier nombre de idioma principal a continuación (o un alias documentado como `js` para JavaScript) después de la valla de apertura.

Dos idiomas enumerados en el sitio destacado.js no están incluidos en el paquete de Marked: **Pine Script** (paquete anterior no disponible) y **Supercollider** (incompatible con resaltado.js 11).

    1c, 4d, GN, abap, abnf, accesslog, actionscript, ada, alan, angelscript, apache, apex,
    applescript, arcade, arduino, armasm, asciidoc, aspectoj, autohotkey, autoit, avrasm, awk,
    axapta, bailarina, bash, basic, bbcode, blade, bnf, bqn, Brainfuck, c, c3, cal, capnproto,
    ceilán, caos, capilla, cisco, limpiar, clojure, clojure-repl, cmake, cobol, coffeescript,
    coq, cos, cpc, cpp, crmsh, cristal, csharp, cshtml-razor, csp, css, curl, cifrar, d, dafny,
    dardo, delphi, diff, django, dns, dockerfile, dos, dsconfig, dts, polvo, dylan, ebnf, elixir,
    olmo, erb, erlang, erlang-repl, excel, improvisado, fix, flix, fortran, fsharp, func, gams,
    gauss, gcode, gdscript, gf, pepinillo, luz tenue, glsl, gml, go, golo, gradle, graphql, groovy,
    gsql, haml, manillar, haskell, haxe, hlsl, hsp, http, hy, inform7, ini, iptables, irpf90,
    isbl, java, javascript, jboss-cli, jolie, json, julia, julia-repl, kotlin, lang, lasso,
    látex, ldif, hoja, magra, menos, ceceo, livecodeserver, livescript, llvm, lookml, lsl, lua,
    macaulay2, makefile, markdown, mathematica, matlab, maxima, mel, mercury, mint, mipsasm,
    mirc, mizar, mkb, mlir, mojolicious, mono, moonscript, motoko, n1ql, nestedtext, nunca,
    nginx, nim, nix, node-repl, nsis, oak, Objectivec, ocaml, ocl, openscad, oxígeno, papiro,
    parser3, perl, pf, pgsql, php, plantilla php, texto plano, pony, powershell, procesamiento,
    perfil, prólogo, propiedades, protobuf, puppet, purebasic, python, python-repl, q, qml,
    qsharp, r, Reasonml, rebol, costilla, riscript, riscvasm, roboconf, robot, routeros,
    rpm-specfile, rsl, ruby, reglas de lenguaje, óxido, rvt-script, sas, scala, esquema, scilab, scss,
    sfz, shell, shexc, smali, Smalltalk, sml, solidity, spl, sqf, sql, stan, stata, step21,
    texto estructurado, lápiz óptico, subunidad, esbelto, rápido, taggerscript, grifo, tcl, terraform, ahorro,
    toit, tp, tsql, twig, mecanografiado, unicorn-rails-log, vala, vba, vbnet, vbscript,
    vbscript-html, verilog, vhdl, vim, wasm, wren, x86asm, x86asmatt, xl, xml, xquery, xsharp,
    yaml, yul, zenscript, céfiro

### Temas de resaltado de sintaxis [syntax-highlighting-themes]

**239** temas de resaltado de sintaxis están disponibles en el menú desplegable {% prefspane Style %}. Los temas se cargan automáticamente desde las hojas de estilo incluidas en Marked; Los nombres coinciden con el nombre del archivo CSS sin la extensión (por ejemplo, `github-dark` carga `github-dark.css`).

Temas generales:

1c-light, a11y-dark, a11y-light, ágata, androidstudio, arduino-light, arta,
    átomo-uno-oscuro, átomo-uno-oscuro-razonable, átomo-una-luz, codepen-embed, color-brewer, oscuro,
    predeterminado, fundación, github, github-dark, github-dark-dimmed, googlecode, escala de grises,
    híbrido, idea, intellij-light, ir-black, isbl-editor-dark, isbl-editor-light, kimbie-dark,
    kimbie-light, mono-blue, monokai, monokai-sublime, noctámbulo, nnfx-dark, nnfx-light, nord,
    obsidiana, panda-sintaxis-oscura, panda-sintaxis-ligera, paraiso-oscuro, paraiso-ligero, pojoaque,
    purebasic, qtcreator-dark, qtcreator-light, arcoiris, rose-pine, rose-pine-dawn,
    rosa-pino-luna, libro escolar, tonos-de-púrpura, brujería, stackoverflow-dark,
    stackoverflow-light, sunburst, tokyo-night-dark, tokyo-night-light, mañana-noche-azul,
    mañana-noche-brillante, vs, vs2015, xcode, xt256

Temas Base16 (176 variantes, cada una con el prefijo `base16-`):

base16-3024, base16-apatía, base16-aprendiz, base16-cenizas, base16-atelier-cueva,
    base16-atelier-cueva-luz, base16-atelier-dune, base16-atelier-dune-light,
    base16-atelier-estuario, base16-atelier-estuario-luz, base16-atelier-bosque,
    base16-atelier-forest-light, base16-atelier-heath, base16-atelier-heath-light,
    base16-atelier-lakeside, base16-atelier-lakeside-light, base16-atelier-plateau,
    base16-atelier-plateau-light, base16-atelier-savanna, base16-atelier-savanna-light,
    base16-atelier-playa, base16-atelier-playa-luz, base16-atelier-sulphurpool,
    base16-atelier-sulphurpool-light, base16-atlas, base16-bespin, base16-black-metal,
    base16-black-metal-bathory, base16-black-metal-burzum, base16-black-metal-dark-funeral,
    base16-black-metal-gorgoroth, base16-black-metal-inmortal, base16-black-metal-khold,
    base16-black-metal-marduk, base16-black-metal-mayhem, base16-black-metal-nile,
    base16-veneno-de-metal-negro, base16-cervecero, base16-brillante, base16-brogrammer,
    base16-pincel-árboles, base16-pincel-árboles-oscuro, base16-tiza, base16-circo,
    base16-clásico-oscuro, base16-clásico-claro, base16-codeschool, base16-colores,
    base16-cupcake, base16-cupertino, base16-danqing, base16-darcula, base16-violeta oscuro,
    base16-darkmoss, base16-darktooth, base16-decaf, base16-default-dark, base16-default-light,
    base16-mar sucio, base16-drácula, base16-borde-oscuro, base16-borde-claro, base16-ochenta,
    base16-brasas, base16-equilibrio-oscuro, base16-equilibrio-gris-oscuro,
    base16-equilibrio-luz-gris, base16-equilibrio-luz, base16-espresso, base16-eva,
    base16-eva-dim, base16-plana, base16-framer, base16-refresco de frutas, base16-gigavoltio,
    base16-github, base16-google-dark, base16-google-light, base16-escala de grises-dark,
    base16-escala-de-grises-claro, base16-pantalla-verde, base16-gruvbox-oscuro-duro,
    base16-gruvbox-oscuro-medio, base16-gruvbox-oscuro-pálido, base16-gruvbox-oscuro-suave,
    base16-gruvbox-ligero-duro, base16-gruvbox-ligero-medio, base16-gruvbox-ligero-suave,
    base16-hardcore, base16-armónico16-oscuro, base16-armónico16-claro, base16-heetch-oscuro,
    base16-heetch-luz, base16-helios, base16-rayuela, base16-horizonte-oscuro,
    base16-horizonte-luz, base16-humanoide-oscuro, base16-humanoide-luz, base16-ia-oscuro,
    base16-ia-light, base16-icy-dark, base16-ir-black, base16-isotopo, base16-kimber,
    base16-london-tube, base16-macintosh, base16-marrakesh, base16-materia, base16-material,
    base16-material-más oscuro, base16-material-más claro, base16-material-noche pálida,
    base16-material-vivid, base16-mellow-purple, base16-mexico-light, base16-mocha,
    base16-monokai, base16-nebulosa, base16-nord, base16-nova, base16-océano, base16-oceanicnext,
    base16-una-luz, base16-una-oscura, base16-supera-la-oscuridad, base16-color-papel-oscuro,
    base16-papercolor-light, base16-paraiso, base16-pasque, base16-phd, base16-pico,
    base16-pop, base16-porple, base16-qualia, base16-railscasts, base16-rebecca,
    base16-ros-pino, base16-ros-pino-amanecer, base16-ros-pino-luna, base16-sagelight,
    base16-castillo de arena, base16-seti-ui, base16-cambiaformas, base16-seda-oscura,
    base16-luz-de-seda, base16-elegante, base16-llamarada-solar, base16-luz-de-llamarada-solar,
    base16-solarizada-oscura, base16-solarizada-clara, base16-spacemacs, base16-summercamp,
    base16-summerfruit-dark, base16-summerfruit-light, base16-synth-midnight-terminal-dark,
    base16-synth-midnight-terminal-light, base16-tango, base16-tender, base16-mañana,
    base16-mañana-noche, base16-crepúsculo, base16-unikitty-oscuro, base16-unikitty-luz,
    base16-vulcan, base16-windows-10, base16-windows-10-light, base16-windows-95,
    base16-windows-95-luz, base16-windows-alto-contraste, base16-windows-alto-contraste-luz,
    base16-windows-nt, base16-windows-nt-light, base16-woodland, base16-xcode-dusk,
    base16-zenburn

## Saltos de línea de GitHub [github-line-breaks]

Marcado puede conservar los saltos de línea en sus párrafos. Simplemente seleccione {% prefspane Processor %} y marque la casilla para conservar los saltos de línea en los párrafos.

## Casillas de verificación de GitHub [github-checkboxes]

Listar elementos formateados como:

    - [] Tarea inacabada
    - [x] Tarea terminada

aparecerán en la vista previa como elementos de casilla de verificación representados. No se puede interactuar con ellos, pero su estado reflejará cualquier cambio en el documento fuente.

## Ajuste de bloque de código [code-block-wrapping]

En {% prefspane Style %} encontrarás una opción en Diseño y Tipografía: "Permitir que los temas ajusten texto dentro de bloques de código". Deshabilitar esto obligará a todos los bloques de código a desplazarse horizontalmente en lugar de ajustarlos, independientemente del estilo de vista previa actual.