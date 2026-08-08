<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Blocos de código protegidos [fenced-code-blocks]

Os blocos de código protegidos são habilitados em ambos os processadores incluídos por padrão (MultiMarkdown e Discount). Os blocos de código protegidos são delimitados por três ou mais tils (~) ou crases (\`). Você pode usar mais de três, mas os delimitadores inicial e final devem ter exatamente o mesmo número de caracteres.

    ~~~~
    Algum código a ser renderizado como um bloco de pré/código
    ~~~~

Os idiomas podem ser especificados usando o título do idioma (ou título abreviado) após o delimitador na primeira linha, ou entre chaves (com ou sem ponto inicial) após o último delimitador. Por exemplo:

    ~~~~~rubi
    algum código Ruby
    ~~~~~

Será renderizado como:

    <pre><code class="ruby">algum código Ruby</code></pre>


Ou com crases:

    `````
    algum código Java
    `````{.java}

Marcado pode detectar especificações de linguagem Markdown Extra/Python Markdown (`{.lang}` após fechar a cerca) e Desconto (`lang` após a primeira cerca). O seguinte (formato de desconto) criaria o mesmo resultado acima (formato Python Markdown):

    `````java
    algum código Java
    `````


Marcado também lida com blocos de código isolados recuados para que você possa usá-los em listas aninhadas.

O realce de sintaxe integrado reconhecerá **256** especificadores de idioma (consulte [Idiomas suportados](#idiomas suportados) abaixo). Se não houver nenhum idioma especificado, ele será detectado automaticamente, portanto não será necessário para a visualização. A string de idioma fornecida será exibida no HTML final como uma classe na tag `<code>`.

Veja a seção [Sintaxe Especial Marcada](Special_Syntax.html#includingcode) para aprender como incluir arquivos de código externo em seu documento.

## Destaque de sintaxe [syntax-highlighting]

![Destaque automático de sintaxe][destaque]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

O realce de sintaxe pode ser habilitado em {% prefspane Style %}. Ele reconhecerá blocos de código, detectará o idioma e renderizará a saída codificada por cores na visualização. Existem vários temas disponíveis, selecionados no menu suspenso abaixo da opção nas configurações. O tema selecionado será aplicado a todos os documentos.

Marked usa [highlight.js](https://highlightjs.org/) para fornecer codificação de cores consistente para todos os tipos de código incorporado, incluindo sintaxes Markdown padrão que não permitem a especificação do idioma. Highlight.js detecta automaticamente bem. Existem algumas pequenas diferenças de renderização entre ele e colorizadores como Pygments (estilo GitHub), mas a saída é semelhante. Usar o tema github.css no código Ruby, por exemplo, renderiza quase a saída exata que você veria no GitHub.

> *A folha de estilo do GitHub fornece estilos de backup para blocos renderizados com Pygments. Se a tag `<pre>` estiver dentro de uma div com a classe "destaque", ela será exibida usando o estilo padrão do GitHub, não o do Marked. Você pode renderizar o código externamente e colar HTML, ou usar `pygmentize` para renderizá-lo em arquivos html e incluí-los com a [sintaxe `<<(source.html)`](Special_Syntax.html#includingcode)*.

A opção "Somente se o idioma for especificado" à direita do seletor de estilo de sintaxe se aplica a blocos de código protegidos. Se ativado, o realce de sintaxe só será aplicado a blocos de código com um especificador de idioma após a cerca de abertura, por exemplo.

    ```js
    código
    ```

O realce de sintaxe aparecerá na visualização e na impressão e exportação de PDF. Se habilitado nas configurações e o tema estiver incluído ao exportar HTML, a biblioteca highlight.js usada pelo Marked será incorporada na saída HTML, permitindo que o HTML exportado apareça como no Marked.

### Idiomas suportados [supported-languages]

Marcado vem com **highlight.js 11.11.1**, incluindo todos os idiomas principais, além de gramáticas de terceiros da lista [idiomas suportados pelo highlight.js](https://highlightjs.readthedocs.io/en/latest/supported-languages.html). Especifique qualquer nome de idioma primário abaixo (ou um alias documentado como `js` para JavaScript) após a cerca de abertura.

Duas linguagens listadas no site destaque.js não estão incluídas no pacote do Marked: **Pine Script** (pacote upstream indisponível) e **Supercollider** (incompatível com destaque.js 11).

    1c, 4d, GN, abap, abnf, accesslog, actionscript, ada, alan, angelscript, apache, apex,
    applescript, arcade, arduino, armasm, asciidoc, aspectoj, autohotkey, autoit, avrasm, awk,
    axapta, bailarina, bash, básico, bbcode, blade, bnf, bqn, brainfuck, c, c3, cal, capnproto,
    Ceilão, caos, capela, cisco, limpo, clojure, clojure-repl, cmake, cobol, coffeescript,
    coq, cos, cpc, cpp, crmsh, cristal, csharp, cshtml-razor, csp, css, curl, cypher, d, dafny,
    dardo, delphi, diff, django, dns, dockerfile, dos, dsconfig, dts, poeira, dylan, ebnf, elixir,
    olmo, erb, erlang, erlang-repl, excel, extempore, fix, flix, fortran, fsharp, func, gams,
    gauss, gcode, gdscript, gf, maxixe, glimmer, glsl, gml, go, golo, gradle, graphql, groovy,
    gsql, haml, guidão, haskell, haxe, hlsl, hsp, http, hy, inform7, ini, iptables, irpf90,
    isbl, java, javascript, jboss-cli, jolie, json, julia, julia-repl, kotlin, lang, laço,
    látex, ldif, folha, lean, menos, lisp, livecodeserver, livescript, llvm, lookml, lsl, lua,
    macaulay2, makefile, markdown, mathematica, matlab, maxima, mel, mercúrio, mint, mipsasm,
    mirc, mizar, mkb, mlir, mojolicious, macaco, moonscript, motoko, n1ql, nestedtext, nunca,
    nginx, nim, nix, node-repl, nsis, carvalho, objetivoc, ocaml, ocl, openscad, Oxygene, papyrus,
    parser3, perl, pf, pgsql, php, php-template, texto simples, pônei, powershell, processamento,
    perfil, prólogo, propriedades, protobuf, fantoche, purebasic, python, python-repl, q, qml,
    qsharp, r, reasonml, rebol, costela, riscript, riscvasm, roboconf, robot, routeros,
    rpm-specfile, rsl, ruby, regraslinguagem, ferrugem, rvt-script, sas, scala, esquema, scilab, scss,
    sfz, shell, shexc, smali, smalltalk, sml, solidez, spl, sqf, sql, stan, stata, step21,
    texto estruturado, caneta, subunidade, esbelto, rápido, taggerscript, toque, tcl, terraform, parcimônia,
    toit, tp, tsql, twig, typescript, unicorn-rails-log, vala, vba, vbnet, vbscript,
    vbscript-html, verilog, vhdl, vim, wasm, wren, x86asm, x86asmatt, xl, xml, xquery, xsharp,
    yaml, yul, zenscript, zephir

### Temas de destaque de sintaxe [syntax-highlighting-themes]

**239** temas de realce de sintaxe estão disponíveis no menu suspenso {% prefspane Style %}. Os temas são carregados automaticamente a partir das folhas de estilo incluídas no Marked; os nomes correspondem ao nome do arquivo CSS sem a extensão (por exemplo, `github-dark` carrega `github-dark.css`).

Temas gerais:

1c-light, a11y-dark, a11y-light, ágata, an-old-hope, androidstudio, arduino-light, arta,
    átomo-um-escuro, átomo-um-escuro-razoável, átomo-um-claro, incorporação de codepen, cervejeiro colorido, escuro,
    padrão, fundação, github, github-dark, github-dark-dimmed, googlecode, escala de cinza,
    híbrido, ideia, intellij-light, ir-black, isbl-editor-dark, isbl-editor-light, kambie-dark,
    Kimbie-light, mono-blue, monokai, monokai-sublime, night-owl, nnfx-dark, nnfx-light, nord,
    obsidiana, panda-sintaxe-escuro, panda-sintaxe-luz, paraiso-escuro, paraiso-luz, pojoaque,
    purebasic, qtcreator-dark, qtcreator-light, arco-íris, rose-pine, rose-pine-dawn,
    rosa-pinheiro-lua, livro escolar, tons de roxo, srcery, stackoverflow-dark,
    stackoverflow-light, sunburst, tokyo-night-dark, tokyo-night-light, Tomorrow-night-blue,
    amanhã à noite-brilhante, vs, vs2015, xcode, xt256

Temas Base16 (176 variantes, cada uma prefixada com `base16-`):

base16-3024, base16-apatia, base16-aprendiz, base16-cinzas, base16-atelier-caverna,
    base16-atelier-cave-light, base16-atelier-dune, base16-atelier-dune-light,
    base16-atelier-estuário, base16-atelier-estuário-luz, base16-atelier-floresta,
    base16-atelier-forest-light, base16-atelier-heath, base16-atelier-heath-light,
    base16-atelier-lakeside, base16-atelier-lakeside-light, base16-atelier-plateau,
    base16-atelier-plateau-light, base16-atelier-savana, base16-atelier-savana-light,
    base16-atelier-seaside, base16-atelier-seaside-light, base16-atelier-sulfurpool,
    base16-atelier-sulfurpool-light, base16-atlas, base16-bespin, base16-black-metal,
    base16-black-metal-bathory, base16-black-metal-burzum, base16-black-metal-dark-funeral,
    base16-black-metal-gorgoroth, base16-black-metal-immortal, base16-black-metal-khold,
    base16-metal preto-marduk, base16-metal preto-caos, base16-metal preto-nilo,
    base16-black-metal-venom, base16-brewer, base16-bright, base16-brogrammer,
    base16-brush-trees, base16-brush-trees-dark, base16-giz, base16-circus,
    base16-classic-dark, base16-classic-light, base16-codeschool, base16-colors,
    base16-cupcake, base16-cupertino, base16-danqing, base16-darcula, base16-violeta escuro,
    base16-darkmoss, base16-darktooth, base16-decaf, base16-default-dark, base16-default-light,
    base16-dirtysea, base16-drácula, base16-edge-dark, base16-edge-light, base16-oitenta,
    base16-brasas, base16-equilíbrio-escuro, base16-equilíbrio-cinza-escuro,
    base16-equilíbrio-cinza-claro, base16-equilíbrio-claro, base16-espresso, base16-eva,
    base16-eva-dim, base16-flat, base16-framer, base16-fruit-soda, base16-gigavolt,
    base16-github, base16-google-dark, base16-google-light, base16-grayscale-dark,
    base16-grayscale-light, base16-green-screen, base16-gruvbox-dark-hard,
    base16-gruvbox-dark-medium, base16-gruvbox-dark-pale, base16-gruvbox-dark-soft,
    base16-gruvbox-light-hard, base16-gruvbox-light-medium, base16-gruvbox-light-soft,
    base16-hardcore, base16-harmonic16-dark, base16-harmonic16-light, base16-heetch-dark,
    base16-heetch-light, base16-helios, base16-amarelinha, base16-horizon-dark,
    base16-horizon-light, base16-humanoid-dark, base16-humanoid-light, base16-ia-dark,
    base16-ia-light, base16-icy-dark, base16-ir-black, base16-isótopo, base16-kimber,
    base16-london-tube, base16-macintosh, base16-marrakesh, base16-materia, base16-material,
    base16-material-mais escuro, base16-material-mais claro, base16-material-palenight,
    base16-material-vívido, base16-mellow-purple, base16-mexico-light, base16-mocha,
    base16-monokai, base16-nebulosa, base16-nord, base16-nova, base16-ocean, base16-oceanicnext,
    base16-one-light, base16-onedark, base16-outrun-dark, base16-papercolor-dark,
    base16-papercolor-light, base16-paraiso, base16-pasque, base16-phd, base16-pico,
    base16-pop, base16-porple, base16-qualia, base16-railscasts, base16-rebecca,
    base16-ros-pine, base16-ros-pine-dawn, base16-ros-pine-moon, base16-sagelight,
    base16-castelo de areia, base16-seti-ui, base16-metamorfo, base16-seda-escuro,
    base16-silk-light, base16-snazzy, base16-solar-flare, base16-solar-flare-light,
    base16-solarizado-escuro, base16-solarizado-luz, base16-spacemacs, base16-campo de verão,
    base16-summerfruit-dark, base16-summerfruit-light, base16-synth-midnight-terminal-dark,
    base16-synth-midnight-terminal-light, base16-tango, base16-tender, base16-amanhã,
    base16-amanhã à noite, base16-crepúsculo, base16-unikitty-escuro, base16-unikitty-luz,
    base16-vulcan, base16-windows-10, base16-windows-10-light, base16-windows-95,
    base16-windows-95-light, base16-windows-high-contrast, base16-windows-high-contrast-light,
    base16-windows-nt, base16-windows-nt-light, base16-woodland, base16-xcode-dusk,
    base16-zenburn

## Quebras de linha do GitHub [github-line-breaks]

Marcado pode preservar quebras de linha em seus parágrafos. Basta selecionar {% prefspane Processor %} e marcar a caixa para manter as quebras de linha nos parágrafos.

## Caixas de seleção do GitHub [github-checkboxes]

Listar itens formatados como:

    - [] Tarefa inacabada
    - [x] Tarefa concluída

aparecerão na visualização como itens de caixa de seleção renderizados. Não é possível interagir com eles, mas seu estado refletirá quaisquer alterações no documento de origem.

## Quebra de bloco de código [code-block-wrapping]

No {% prefspane Style %} você encontrará uma opção em Layout e Tipografia: "Permitir que temas envolvam texto dentro de blocos de código." Desabilitar isso forçará todos os blocos de código a rolarem o estouro horizontal em vez de envolvê-los, independentemente do estilo de visualização atual.