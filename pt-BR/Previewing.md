<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

I> Esta página cobre a visualização *aparência* --- estilos, zoom, modo escuro e barra de status. Para configurar a visualização ao vivo no seu editor, consulte [Visualização do Live Markdown no Mac](Live_Markdown_Preview_on_Mac.html).

Mudando a maneira como você vê as coisas.

## Escolhendo um estilo [choosing-a-style]

![][1]

   [1]: images/StylePicker.jpg @2x width=896px height=195px class=center

Você pode definir um estilo padrão para novos documentos em {% prefspane Style %}. Se o menu de estilo na barra de ferramentas estiver ativado nas configurações da janela, você poderá ajustar o estilo por documento diretamente na janela de visualização. Sua seleção de estilo será lembrada e será a primeira escolha para opções de exportação e impressão.

Os estilos personalizados adicionados nas configurações de Estilo estarão disponíveis em ambos os menus.

Os estilos podem ser selecionados com atalhos de teclado. Abra o menu de estilos para ver o atalho de teclado para cada estilo. Os atalhos de teclado são atribuídos na ordem dos estilos: os primeiros 9 estilos da lista podem ser acessados com {% kbd cmd 1 %} -- {% kbd cmd 9 %}, os próximos 10 estilos com {% kbd cmd opt 1 %} -- {% kbd cmd opt 0 %}, etc.

## Modo de contorno [outline-mode]

Se o seu documento for uma lista hierárquica, como uma gerada a partir de um mapa mental ou aplicativo de estrutura de tópicos, você poderá ativar o Modo de estrutura de tópicos no menu Engrenagem para aplicar formatação especial no estilo de estrutura de tópicos APA ou Decimal.

O modo de contorno automático pode ser ativado para extensões de arquivo específicas em {% prefspane Style %}.

## Zoom de texto [text-zoom]

![][2]

   [2]: images/textzoom.jpg @2x width=800px height=414px class=center

Você pode alterar o tamanho do texto usando {% kbd cmd shift + %} e {% kbd cmd shift - %} ou usar o menu Zoom em Visualização na barra de menu ou no menu de engrenagem na janela do documento. Marcado lembrará todas as alterações feitas na próxima vez (e sempre). Redefina o zoom para 100% com {% kbd cmd 0 %} (ou acesse **Zoom Reset** no menu Zoom).

## Modo escuro/alto contraste [dark-modehigh-contrast]

Se você preferir texto claro em um fundo escuro, Marcado tem o que você precisa. No menu __Preview__ você pode usar {% appmenu Preview, Dark Mode ({{opt}}{{cmd}}I) %} inverter as cores de qualquer um dos esquemas padrão para um resultado claro sobre escuro, e se um tema personalizado for [construído corretamente](Writing_Custom_CSS.html) ele funcionará lá também.

## Mostrar/ocultar barra de status [showhide-status-bar]

A barra de status na parte inferior da janela de visualização pode ser alternada com o item de menu {% appmenu Preview, Show Status Bar ({{ctrl}}/) %}. Quando está oculto, pode ser visualizado e interagido passando o mouse sobre o espaço na parte inferior da visualização.