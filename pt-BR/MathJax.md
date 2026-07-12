<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Os números são tão importantes quanto as palavras.

## Visualize fórmulas com MathJax

![][1]

   [1]: images/mathjax.jpg @2x width=713px height=512px class=center

Ao ativar o MathJax em {% prefspane Style %}, os scripts e CSS necessários serão incluídos na visualização. Em seguida, a sintaxe matemática MultiMarkdown pode ser usada em seu documento Markdown e os resultados serão exibidos.

Exemplo de sintaxe MMD MathJax:

    \\\\[ {e}^{i\pi } 1=0 \\\\]

Se você optar por incluir MathJax em um arquivo HTML exportado, um link CDN será usado em vez do código MathJax incorporado. Isso requer uma conexão com a Internet para visualizar o MathML renderizado.

## Fonte MathJax: Local vs CDN

Quando MathJax está habilitado, Marked pode carregá-lo de:

- **Local**: uma cópia do MathJax v3 incluída no aplicativo (mais rápido para carregar, funciona offline).
- **CDN**: o CDN oficial do MathJax v3 (sempre atualizado, sem impacto no pacote de aplicativos).

O pop-up **MathJax Source** em {% prefspane Style %} permite que você escolha:

- **Local** – usa o componente ES5 `tex-chtml.js` do pacote de aplicativos.
- **CDN** – carrega o mesmo componente do CDN. Isso requer uma conexão com a Internet.

Os arquivos HTML exportados sempre fazem referência ao MathJax de um CDN, independentemente da fonte de visualização, portanto, permanecem independentes e pequenos.

## Numeração de equações

Você pode ativar a numeração das equações em {% prefspane Style %}. Isso funciona tanto com MathJax quanto com KaTeX, mas é implementado de forma diferente internamente. Para MathJax v3, Marked mapeia suas configurações para a configuração apropriada do MathJax para que:

- “Equações numéricas” controla se algum número é mostrado.
- A opção “lateral” controla se os números aparecem à esquerda ou à direita.
- A opção “somente AMS” restringe a numeração às equações do estilo AMS.

Essas opções correspondem às configurações `tex.tags` e `tex.tagSide` do MathJax nos bastidores.

## Pacotes adicionais

MathJax v3 é modular. Marcado sempre ativa os pacotes principais do TeX/AMS, e você pode opcionalmente ativar pacotes extras em {% prefspane Style %}:

- **Física** (`physics`) – notação física e conveniências.
- **Química** (`mhchem`) – equações químicas.
- **Bra–ket** (`braket`) – Notação Dirac bra–ket.
- **Símbolos em negrito** (`boldsymbol`) – símbolos matemáticos em negrito.

Clique em **Pacotes Adicionais…** para abrir uma pequena lista de verificação onde você pode ativar ou desativar esses pacotes. As alterações entrarão em vigor na próxima vez que Marcado renderizar matemática na visualização.

## Configuração avançada do MathJax

Você pode aplicar configurações personalizadas adicionais além dos padrões do Marked adicionando um objeto JSON válido no campo **Configuração avançada**. Este campo é mesclado no objeto de configuração MathJax v3 (`window.MathJax`) antes do carregamento do MathJax. Pode conter [quaisquer opções suportadas pelo MathJax v3](https://docs.mathjax.org/en/latest/options/), por exemplo:

    {
        "tex": {
            "inlineMath": [["$","$"],["\\\\(","\\\\)"]],
            "displayMath": [["$$","$$"],["\\\\[","\\\\]"]],
            "macros": {
                "tr": "{\\\\scriptscriptstyle\\\\mathrm{T}}"
            },
            "pacotes": { "[+]": ["física"] }
        }
    }

Este exemplo ajusta os delimitadores TeX, adiciona uma macro `\tr` e habilita o pacote `physics` além do conjunto padrão. Com essas configurações, todos os itens a seguir são renderizados corretamente:

    Fórmula embutida usando parênteses, \\\\({x}^{2} {y}^{2}=1\\\\), ou com cifrões, ${x}^{2} {y}^{2}=1$.

    Exibição com colchetes escapados:

    \\\\[ {e}^{i\pi } 333=0 \label{testme} \\\\]

    Ou com cifrões duplos:

    $${x}_{1,2}=\\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a}$$

![][2]

   [2]: images/mathjax2.jpg @2x width=837px height=260px class=center

A configuração adicional estende o objeto existente, portanto apenas as propriedades especificadas serão substituídas. As opções não especificadas permanecerão no padrão da predefinição atual.

Observe que usando o processador MultiMarkdown com delimitadores não padrão, os caracteres dentro da expressão são analisados, portanto, símbolos como `*` e `^` causarão alterações tipográficas que interromperão o processador MathJax. A melhor solução nestes casos é usar o processador Discount em [Configurações do processador](x-marked-3://pref/processor).

Marked faz um pouco de mágica quando MathJax ou KaTeX estão habilitados, convertendo a sintaxe matemática para garantir que seja o mais compatível possível com o processador atual (MultiMarkdown ou Discount). Isso deve ser ótimo em todas as circunstâncias, mas se você achar que está causando problemas, [entre em contato com o suporte](https://support.markedapp.com/questions/add)!


## KaTeX

[katex]: https://katex.org/

[KaTeX][] está disponível como uma alternativa ao MathJax. É mais leve e, portanto, mais rápido de carregar, o que pode ser ótimo em documentos com grande número de fórmulas. Porém, ele não possui tantos recursos e algumas equações que funcionam com MathJax (ou LaTeX) podem não ser suportadas.

## Numeração automática de equações [numeração]

Você pode ativar a numeração das equações em {% prefspane Style %}. Isso funciona com MathJax e KaTeX. Você pode selecionar se os números aparecem no lado esquerdo ou direito da equação.

### Em MathJax

No MathJax, isso usa a configuração:

    {
      TeX: {quationNumbers: {autoNumber: "all" } }
    }

Se você quiser numerar apenas as equações AMS, selecione "Somente AMS" à direita do menu suspenso "lateral".

### No KaTeX

KaTeX não oferece numeração de equações. Para simular isso no Marked, CSS é usado e todas as equações de exibição são numeradas.

## Problemas de exportação

Os formatos Rich Text não suportam equações (seja do MathJax ou do KaTeX). Eles ficarão ocultos no documento de saída, pois tentar incluir fontes especiais resulta em uma bagunça maior do que você imagina... Isso é algo que espero corrigir em algum momento, mas é uma deficiência no momento.