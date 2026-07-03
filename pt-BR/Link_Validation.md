<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A validação do link faz ping no destino de um URL e testa erros. Isso ajuda a evitar links quebrados e inválidos no documento publicado e é especialmente útil para blogueiros.

## Validando links únicos

![][1]

   [1]: images/validate_single.png @2x largura=832px altura=267px class=centro

Clique e segure um link na visualização até que ele pisque e solte para abrir o menu de ação do link. Escolha "Validar link" para executar o teste. Os resultados são exibidos no pop-up.

## Validando todos os links

![][2]

   [2]: imagens/capturas de tela/mainwindow-feature-urlvalidate-crop.jpg @2x largura=1089px altura=300px classe=centro

Escolha "Validar todos os links" (atalho {% kbd ctrl cmd L %}) no menu Engrenagem ou no menu do botão direito. Todos os links remotos no documento serão verificados e os resultados serão exibidos em um pop-up. Clicar em um link no pop-up irá rolar e destacar seu respectivo link no documento.

URLs válidos podem ser ocultados no pop-up com o botão "Ocultar válidos" na parte superior. Isso mostrará apenas URLs que retornaram um status de erro.

Pressionar Escape ocultará os resultados da validação. Eles podem ser revelados novamente usando {% kbd ctrl cmd L %} ou o menu Gear.

## Validando automaticamente

Ative "Validar URLs automaticamente na atualização" nas configurações de visualização (ou na parte inferior do pop-up de validação do link). Quando o documento for carregado, os links contidos serão testados em segundo plano. Uma caixa de diálogo só será exibida se houver erros.

Para desativar o pop-up, desative-o nas configurações ou desmarque a caixa na parte inferior da janela pop-up.