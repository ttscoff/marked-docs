<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked possui um editor de estilo integrado e pode aplicar arquivos CSS personalizados.

Você pode usar o editor para criar estilos bonitos ou, se souber CSS o suficiente para ser perigoso, pode fazer com que o Marcado tenha a aparência que desejar.

## Primeiros passos

Há uma galeria de estilos personalizados criados pelo desenvolvedor e pelos usuários em [markedapp.com/styles](https://markedapp.com/styles/). A galeria permite visualizar e instalar estilos diretamente no Marked. Qualquer estilo instalado pode ser revelado no Finder para exame e modificação. A galeria pode ser aberta usando um visualizador interno com {% appmenu Style, Generate a Custom Style %} ou clique no ícone de lápis (editar) ao lado de qualquer estilo editável no Gerenciador de estilos. primeiro você precisará duplicá-lo no gerenciador.

Há também um [repositório para estilos personalizados](https://github.com/ttscoff/MarkedCustomStyles) no GitHub com exemplos. Sinta-se à vontade para navegar, usar e contribuir lá. Se você distribuir seu tema com base em um dos temas base, sinta-se à vontade para adicionar-se aos créditos como colaborador.

Com a capacidade do Marked de usar arquivos CSS personalizados, o céu é o limite ao personalizar sua visualização. Todas as opções CSS3 que funcionam no Safari funcionarão no Marked. Com os arquivos Markdown padrão em Marked, existem apenas alguns elementos HTML que você precisa manipular; todo o conteúdo está em uma div com o id "wrapper", todo o resto é determinado pela marcação do seu documento.

Se você está projetando para uso pessoal, não há regras. Ative o rastreamento de CSS com a caixa de seleção abaixo do seletor de CSS personalizado e quando você editar e salvar seu CSS personalizado, a visualização será atualizada.

**Um [tema de esqueleto está disponível](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) para começar.**

Se você está planejando compartilhar sua criação de CSS, há alguns pontos que você precisa abordar. Primeiro, existem algumas classes corporais que precisam ter estilos aplicados:

## Aulas corporais

Os seguintes estilos devem ser incluídos em qualquer CSS marcado para ser compartilhado. As classes corporais permitem direcionar e modificar qualquer seletor sob diferentes opções de preferência.

### Invertido

 Quando o usuário seleciona {% appmenu Preview, Dark Mode %}, uma classe “invertida” é adicionada à tag body. Você pode usar isso para direcionar os estilos claros sobre escuros de alto contraste.

Você deseja que os estilos invertidos sejam aplicados apenas à visualização, não à impressão, então use uma consulta de mídia (@media screen) para restringi-lo. O código abaixo é bastante versátil e, na maioria dos casos, você pode simplesmente colocá-lo em sua folha de estilo para compatibilidade, mas fique à vontade para ajustá-lo.

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

### Poesia

O usuário pode escolher se o texto recuado por tabulação é poesia ou código. A única diferença é que os blocos de pré/código têm um estilo mais poético se o modo poesia for escolhido. A classe "poesia" é aplicada à tag body.

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

## Casos especiais

Tabelas, Figura/Figlegenda e o caso especial de `a.footnote` e `div.footnotes>a` também precisam ser considerados. Não há regras definidas sobre como lidar com eles, mas dê uma olhada nos estilos padrão para ter uma ideia de quais regras CSS o Marked precisa.

O estilo de tabela padrão em todos os estilos padrão usa transparência nas linhas alternadas para combinar suavemente com qualquer plano de fundo. Você pode copiar esses estilos ou seguir seu próprio caminho, apenas certifique-se de estilizá-los! O mesmo para figura e legenda; adicione uma imagem a um documento com texto alternativo para ver como a marcação ficará e o estilo apropriado.

As notas de rodapé incluídas em um documento renderizarão um link dentro do conteúdo (a.footnote) e um div no final com o texto referenciado (div.footnotes). Novamente, veja os estilos padrão para referência. Para evitar alterar a altura da linha em linhas que contêm um número de referência de nota de rodapé, inclua algo como:

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

Também é uma boa ideia incluir uma regra geral para todas as imagens, para mantê-las dentro da largura da página. Algo como:

```css
#wrapper img { max-width: 100% }
```

Se o seu tema tiver preenchimento adicional ou largura fixa, modifique a largura máxima para caber.

## Estilos de impressão

Certifique-se de incluir estilos de impressão que removam quaisquer cores de fundo, rolagem fixa, etc. Use "@media print" para defini-los dentro do seu tema.

A ocultação de links na impressão é feita fora do tema principal, permitindo que os usuários optem por ocultar os destaques e sublinhados dos links na impressão. Contanto que você tenha um estilo base definido para o texto, não precisa se preocupar com isso.

Então, faça isso. Converta o tema do seu blog, crie um estilo de impressão matador para documentos PDF ou crie a visualização perfeita para o estilo de escrita que você faz. Se você fizer algo incrível, me avise e eu postarei para toda a comunidade marcada.

## Configurações adicionais de CSS

No {% prefspane Style %}, você pode editar CSS adicional. Esses estilos serão anexados a qualquer tema carregado e podem ser usados ​​para fazer alterações universais em todos os temas.

Usando consultas [alta especificidade](#overridingspecificity) e @media para impressão e tela, você pode controlar praticamente todos os aspectos de estilo com um pouco de conhecimento de CSS.

## Inspetor WebKit

O Web Inspector do Safari é a maneira mais fácil de ver exatamente o que HTML e CSS marcados estão gerando e de experimentar estilos personalizados ao vivo.

### Habilitando o menu Desenvolver no Safari

1. Abra o Safari e escolha {% appmenu Safari, Settings… %}.
2. Selecione a guia **Avançado**.
3. Ative **Mostrar recursos para desenvolvedores web** (ou **Mostrar menu Desenvolver na barra de menus** em versões mais antigas do macOS).

Uma vez ativado, um menu **Desenvolver** aparecerá na barra de menu do Safari.

![Menu Safari Develop mostrando documentos marcados][menu desenvolvimento]

### Inspecionando um documento marcado

1. Com uma janela de visualização aberta no Marcado, mude para o Safari.
2. Na barra de menu, escolha **Desenvolver → _\<nome do seu Mac\>_ → Marcado → _\<título do documento\>_**.
3. O Safari abrirá uma janela do Web Inspector anexada à visualização marcada selecionada.

A partir daqui você pode:

- Use a aba **Elements** para inspecionar o DOM dentro da div `#wrapper` e ver quais regras CSS são aplicadas.
- Passe o mouse sobre os elementos na árvore DOM para destacá-los na janela Marcada.
- Use a barra lateral **Estilos** para ajustar as regras ao vivo e, em seguida, copie os trechos de trabalho de volta para um estilo personalizado ou **CSS adicional**.
    - Após editar CSS na aba Elementos, você pode obter um resumo de suas edições selecionando a aba Alterações

	![Alterações][mudanças de css]
- Use a guia **Console** para executar o JavaScript na visualização ao vivo. A [API JavaScript marcada](https://markedapp.com/help/jsapi/) completa está disponível neste console.
- Explore outras guias, como **Rede**, ao depurar recursos carregados pelo seu documento.

![Inspecionando uma visualização marcada com Safari Web Inspector][inspecionando]

## Compartilhando CSS personalizado

Use {% appmenu Style, Share a Custom Style %} para abrir o aplicativo de compartilhamento em seu navegador. Arraste seu CSS para a zona para soltar (ou clique para selecionar no disco) e carregue o CSS para seu estilo personalizado.

Os estilos compartilhados precisam ser aprovados pelo desenvolvedor antes de aparecerem na galeria, portanto você não verá resultados imediatos.

## Outras dicas

### Especificidade de substituição

Na visualização Marcada, uma classe de corpo baseada no nome do arquivo do estilo atual é adicionada. Se a visualização estiver definida como "Suíça", haverá uma classe na tag `<body>` chamada `mkstyle--swiss`. Se o seu CSS personalizado for chamado MyCustom.css, a classe do corpo será `mkstyle--mycustom`. Você pode usar isso antes das regras definidas nos estilos base para substituí-las. Para obter especificidade absoluta em uma regra, use também o ID #wrapper da div do contêiner:

	.mkstyle--mycustom #wrapper p+p { ... }

### Estilo do índice

Se você usar o token `<!--toc-->` para [inserir um índice](Special_Syntax.html#tableofcontents), poderá substituir as configurações dos indicadores de nível do Índice em um estilo personalizado usando o "#wrapper" para aumentar a especificidade:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Isso faria com que todos os itens da lista no Índice usassem um marcador quadrado em vez do que foi definido em Configurações quando seu Estilo personalizado estiver ativo.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px