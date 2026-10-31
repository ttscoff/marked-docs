# <%= @title %>

O Marked tem um editor de estilos integrado e pode aplicar arquivos CSS personalizados.

Você pode usar o editor para criar estilos bonitos ou, se souber o suficiente de CSS para ser perigoso, pode fazer o Marked parecer do jeito que quiser.

## Primeiros passos [getting-started]

Existe uma galeria de Estilos Personalizados criados pelo desenvolvedor e por usuários em [markedapp.com/styles](https://markedapp.com/styles/). A galeria permite visualizar e instalar Estilos diretamente no Marked. Qualquer Estilo instalado pode ser revelado no Finder para exame e modificação. A galeria pode ser aberta usando um visualizador interno com {% appmenu Style, Generate a Custom Style %}, ou clicando no ícone de lápis (editar) ao lado de qualquer estilo editável no Gerenciador de Estilos. Se você quiser editar um estilo integrado, primeiro precisará duplicá-lo no gerenciador.

Também há um [repositório de Estilos Personalizados](https://github.com/ttscoff/MarkedCustomStyles) no GitHub com exemplos. Sinta-se à vontade para navegar, usar e contribuir por lá. Se você distribuir seu tema baseado em um dos temas base, fique à vontade para se adicionar aos créditos como colaborador.

Com a capacidade do Marked de usar arquivos CSS personalizados, o céu é o limite ao personalizar sua Pré-visualização. Todas as opções de CSS3 que funcionam no Safari também funcionam no Marked. Com arquivos Markdown padrão no Marked, há apenas alguns elementos HTML que você precisa tratar; todo o conteúdo fica dentro de uma div com o id "wrapper", e o restante é determinado pela marcação do seu documento.

Se você está criando algo para uso pessoal, não há regras. Ative o rastreamento de CSS com a caixa de seleção abaixo do seletor de CSS personalizado e, quando você editar e salvar seu CSS personalizado, a pré-visualização será atualizada.

**Um [tema esqueleto está disponível](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) para você começar.**

Se você pretende compartilhar sua criação de CSS, há alguns pontos que precisa cobrir. Primeiro, existem algumas classes do body que precisam ter estilos aplicados:

## Classes do body [body-classes]

Os estilos a seguir devem ser incluídos em qualquer CSS do Marked destinado a compartilhamento. As classes do body permitem que você direcione e modifique qualquer seletor sob diferentes opções de preferências.

### Invertido [inverted]

Quando o usuário seleciona {% appmenu Preview, Dark Mode %}, uma classe "inverted" é adicionada à tag body. Você pode usar isso para direcionar os estilos de alto contraste, claro sobre escuro.

Você só quer que os estilos invertidos se apliquem à pré-visualização, não à impressão, então use uma media query (@media screen) para restringir isso. O código abaixo é bastante genérico e, na maioria dos casos, você pode simplesmente incluí-lo na sua folha de estilos para compatibilidade, mas sinta-se à vontade para ajustá-lo.

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### Poesia [poetry]

O usuário pode escolher se o texto indentado com tabulação é poesia ou código. A única diferença é que os blocos pre/code são estilizados de forma mais... poética, digamos assim, quando o modo poesia é escolhido. A classe "poetry" é aplicada à tag body.

Seja tão criativo quanto quiser com a formatação, mas aqui está um trecho básico:

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## Casos especiais [special-cases]

Tabelas, Figure/Figcaption e o caso especial de `a.footnote` e `div.footnotes>a` também precisam ser considerados. Não há regras fixas sobre como tratá-los, mas dê uma olhada nos estilos padrão para ter uma ideia de quais regras CSS o Marked precisa.

O estilo padrão de tabela em todos os estilos padrão usa transparência nas linhas alternadas para que se misturem suavemente com qualquer plano de fundo. Você pode copiar esses estilos ou seguir seu próprio caminho, apenas certifique-se de tê-los estilizado! O mesmo vale para figure e figcaption; adicione uma imagem a um documento com texto alternativo para ver como a marcação será gerada e estilize de acordo.

Notas de rodapé incluídas em um documento renderizam um link dentro do conteúdo (a.footnote) e uma div no final com o texto referenciado (div.footnotes). Novamente, veja os estilos padrão como referência. Para evitar alterar a altura da linha em linhas que contêm um número de referência de nota de rodapé, certifique-se de incluir algo como:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Para manter a seta de retorno na mesma linha, inclua:

```css
.footnotes p {display:inline}
```

Também é uma boa ideia incluir uma regra geral para todas as imagens, mantendo-as dentro da largura da página. Algo como:

```css
#wrapper img { max-width: 100% }
```

Se o seu tema tiver preenchimento adicional ou uma largura fixa, ajuste o max-width conforme necessário.

## Estilos de impressão [printstyles]

Certifique-se de incluir estilos de impressão que removam quaisquer cores de fundo, rolagem fixa e elementos de interface exclusivos da pré-visualização. O Marked oferece duas formas de direcionar a saída de impressão e PDF.

### `@media print` [media-print]

As regras CSS de impressão padrão se aplicam ao imprimir pelo Marked ou quando a exportação em PDF usa mídia de impressão:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### A classe `.mkprinting` [the-mkprinting-class]

Quando o Marked prepara um documento para **exportação em PDF** ou **Pré-visualização de Impressão/PDF** ({% kbd cmd P %}), ele adiciona a classe `mkprinting` à tag `<body>` (junto com classes de exportação como `bandw`, `breakAfterTOC` e a classe `mkstyle--*` do seu estilo). Os temas integrados do Marked usam essa classe para a maioria das regras específicas de impressão, em vez de depender apenas de `@media print`.

A exportação em PDF frequentemente carrega a WebView de renderização oculta com mídia **screen** (especialmente para estilos personalizados e documentos [Fountain](Fountain_for_Screenwriters.html)), então blocos `@media print` na sua folha de estilos podem **não** se aplicar à saída em PDF. Regras prefixadas com `.mkprinting` sempre se aplicam durante a exportação, pois são seletores de classe comuns, não media queries.

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Para estilos que precisam funcionar **tanto** na impressão pelo navegador quanto na exportação em PDF do Marked, duplique as regras essenciais ou combine seletores:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**Estilo Personalizado vs. CSS Adicional.** Em uma folha de estilos de Estilo Personalizado, escreva `.mkprinting #wrapper …` como mostrado acima. No campo **CSS Adicional**, o Marked reescreve os seletores antes da injeção --- use a forma qualificada com body no lugar:

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Veja [Configurações de CSS Adicional](#additional-css-settings) para entender como funciona a reescrita e por que `.mkprinting #wrapper …` sozinho não corresponde nesse caso.

Ao depurar CSS de impressão personalizado, abra a Pré-visualização de Impressão/PDF ou exporte para PDF e, então, use o [Web Inspector do Safari](#webkitinspector) para inspecionar o documento --- o `<body>` terá a classe `mkprinting` enquanto o layout de impressão estiver ativo.

A ocultação de links na impressão é tratada fora do tema principal, permitindo que os usuários escolham ocultar destaques e sublinhados de links na impressão. Contanto que você tenha um estilo base definido para o texto, não precisa se preocupar com isso.

Então, mãos à obra. Converta o tema do seu blog, crie um estilo de impressão matador para documentos em PDF, ou elabore a pré-visualização perfeita para o tipo de escrita que você faz. Se você criar algo incrível, [compartilhe com a comunidade](https://markedapp.com/styleshare/).

## Configurações de CSS Adicional [additional-css-settings]

No {% prefspane Style %}, você pode editar o **CSS Adicional**. Essas regras são **anexadas a qualquer tema carregado**. Elas são uma camada parcial deliberada, não um tema completo. Se você colar uma folha de estilos completa nesse campo --- ou importar essa mesma folha parcial pelo [Gerenciador de Estilos](Custom_Styles.html) como se fosse um tema --- tudo o que a folha não cobrir ficará sem estilo.

### Reescrita de seletores [additional-css-selector-rewriting]

O Marked reescreve os seletores do CSS Adicional antes de injetá-los (como `body.mk-has-additional-css …`) para que as regras permaneçam restritas à pré-visualização:

- Uma parte do seletor que já começa com `body` ou `#wrapper` recebe o prefixo `body.mk-has-additional-css`, com as classes do body mescladas em vez de aninhadas.
- Qualquer outra parte do seletor é restrita sob `body.mk-has-additional-css #wrapper …`.
- As classes de body iniciais que o Marked define em `<body>` --- incluindo `.mkprinting`, `.inverted`, `.poetry`, `.bandw`, `.breakAfterTOC` e `.mkstyle--*` --- são tratadas como `body` e mescladas ao seletor do body, em vez de aninhadas sob `#wrapper`.

| Inserido no CSS Adicional | Resultado |
| :-- | :-- |
| `#wrapper h2` | Corresponde (com escopo correto) |
| `body.mkprinting #wrapper p` | Corresponde durante impressão/PDF |
| `.mkprinting #wrapper p` | **Não** corresponde (exigiria um `#wrapper` aninhado) |
| `:root { --x: 1; }` | **Não** corresponde (prefira `body` ou `#wrapper` para propriedades personalizadas) |

Para regras de impressão nesse campo, prefira `body.mkprinting #wrapper …`. A mesma intenção visual em um arquivo de Estilo Personalizado pode manter a forma mais curta `.mkprinting #wrapper …`.

Não há **limite de tamanho nem verificação de validade de CSS** no CSS Adicional. O Marked armazena e injeta o que você inserir; CSS inválido simplesmente não tem efeito na pré-visualização.

### HTML e outras exportações [additional-css-exports]

O CSS Adicional se aplica na pré-visualização ao vivo, na Pré-visualização de Impressão/PDF, na exportação em PDF e na **exportação em HTML** quando os estilos são incluídos --- o `<body>` exportado recebe a classe `mk-has-additional-css` para que os seletores reescritos correspondam. DOCX, ODT e EPUB usam seus próprios caminhos de estilização e não aplicam o CSS Adicional da mesma forma.

Usando [alta especificidade](#overridingspecificity), consultas `@media` para impressão e tela, e seletores `body.mkprinting` (nesse campo) ou `.mkprinting` (em Estilos Personalizados), você pode controlar praticamente todos os aspectos de estilização com um pouco de conhecimento de CSS.

## Web Inspector [webkitinspector]

O Web Inspector do Safari é a maneira mais fácil de ver exatamente qual HTML e CSS o Marked está gerando, e de experimentar Estilos Personalizados ao vivo.

### Ativando o menu Desenvolver no Safari [enabling-the-develop-menu-in-safari]

1. Abra o Safari e escolha {% appmenu Safari, Settings… %}.
2. Selecione a aba **Avançado**.
3. Ative **Mostrar recursos para desenvolvedores web** (ou **Mostrar menu Desenvolver na barra de menus** em versões mais antigas do macOS).

Uma vez ativado, um menu **Desenvolver** aparecerá na barra de menus do Safari.

![Menu Desenvolver do Safari mostrando documentos do Marked][develop-menu]

### Inspecionando um documento do Marked [inspecting-a-marked-document]

1. Com uma janela de pré-visualização aberta no Marked, mude para o Safari.
2. Na barra de menus, escolha **Desenvolver → _\<nome do seu Mac\>_ → Marked → _\<título do documento\>_**.
3. O Safari abrirá uma janela do Web Inspector conectada à pré-visualização selecionada do Marked.

A partir daqui você pode:

- Usar a aba **Elementos** para inspecionar o DOM dentro da div `#wrapper` e ver quais regras CSS estão sendo aplicadas.
- Passar o mouse sobre elementos na árvore do DOM para destacá-los na janela do Marked.
- Usar a barra lateral **Estilos** para ajustar regras ao vivo e depois copiar os trechos funcionais de volta para um Estilo Personalizado ou o **CSS Adicional**.
    - Depois de editar CSS na aba Elementos, você pode obter um resumo das suas edições selecionando a aba Alterações

	![Alterações][css-changes]
- Usar a aba **Console** para executar JavaScript na pré-visualização ao vivo. A [API JavaScript completa do Marked](https://markedapp.com/help/jsapi/) está disponível nesse console.
- Explorar outras abas, como **Rede**, ao depurar recursos carregados pelo seu documento.

![Inspecionando uma pré-visualização do Marked com o Web Inspector do Safari][inspecting]

## Compartilhando CSS Personalizado [sharing-custom-css]

Use {% appmenu Style, Share a Custom Style %} para abrir o aplicativo de compartilhamento no seu navegador. Arraste seu CSS para a área de soltar (ou clique para selecionar do disco) e envie o CSS do seu Estilo Personalizado.

Os estilos compartilhados precisam ser aprovados pelo desenvolvedor antes de aparecerem na galeria, então você não verá resultados imediatos.

## Outras dicas [other-tips]

### Sobrescrevendo especificidade [overridingspecificity]

Dentro da pré-visualização do Marked, uma classe de body baseada no nome do arquivo do estilo atual é adicionada. Se a pré-visualização estiver definida para "Swiss", haverá uma classe na tag `<body>` chamada `mkstyle--swiss`. Se o seu CSS personalizado se chamar MyCustom.css, a classe do body será `mkstyle--mycustom`. Você pode usar isso antes das regras definidas nos estilos base para sobrescrevê-las. Para obter especificidade absoluta em uma regra, use também o ID #wrapper da div contêiner:

	.mkstyle--mycustom #wrapper p+p { ... }

### Estilização do sumário [table-of-contents-styling]

Se você usar o token `<!--toc-->` para [inserir um sumário](Special_Syntax.html#tableofcontents), pode sobrescrever as configurações dos indicadores de nível do Sumário em um Estilo Personalizado usando o "#wrapper" para aumentar a especificidade:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Isso faria com que todos os itens de lista no Sumário usassem um marcador quadrado em vez do que foi definido nas Configurações quando seu Estilo Personalizado estiver ativo.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
